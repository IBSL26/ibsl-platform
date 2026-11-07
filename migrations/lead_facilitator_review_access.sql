-- 7 Nov 2026: lead facilitators get the same review access as facilitators
-- (skills, reflection marks, participant profiles, signed-terms list).
begin;

create or replace function public.competency_can_review(p_cohort uuid)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select public.is_admin() or exists (select 1 from public.cohort_memberships cm
    where cm.cohort_id = p_cohort and cm.profile_id = auth.uid() and cm.role_in_cohort::text in ('facilitator', 'lead_facilitator'));
$function$;

create or replace function public.participant_visible(p_owner uuid)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select p_owner = auth.uid()
      or public.is_admin()
      or exists (select 1 from public.capstone_individual a
                 join public.capstone_individual b on b.team_id = a.team_id
                 where a.profile_id = auth.uid() and b.profile_id = p_owner)
      or exists (select 1 from public.cohort_memberships f
                 join public.cohort_memberships m on m.cohort_id = f.cohort_id
                 where f.profile_id = auth.uid() and f.role_in_cohort::text in ('facilitator', 'lead_facilitator')
                   and m.profile_id = p_owner);
$function$;

create or replace function public.get_cohort_participant_profiles(p_cohort_id uuid)
returns table (profile_id uuid, full_name text, team_name text, exec_role text, bio text, photo_path text, updated_at timestamptz)
language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
begin
  if not public.is_admin() and not exists (
    select 1 from public.cohort_memberships cm
    where cm.cohort_id = p_cohort_id and cm.profile_id = auth.uid() and cm.role_in_cohort::text in ('facilitator', 'lead_facilitator')
  ) then
    raise exception 'Access denied' using errcode = '42501';
  end if;
  return query
  select p.id, p.full_name::text, t.team_name::text, pp.exec_role, pp.bio, pp.photo_path, pp.updated_at
  from public.cohort_memberships cm
  join public.profiles p on p.id = cm.profile_id
  left join public.capstone_individual ci on ci.profile_id = p.id and ci.cohort_id = p_cohort_id
  left join public.capstone_team t on t.id = ci.team_id
  left join public.participant_profiles pp on pp.profile_id = p.id
  where cm.cohort_id = p_cohort_id and cm.role_in_cohort::text = 'participant'
  order by t.team_name nulls last, lower(coalesce(p.full_name, ''));
end;
$function$;

create or replace function public.get_cohort_terms_record(p_cohort_id uuid)
returns table (
  profile_id uuid, full_name text, email text, role_in_cohort text, required boolean,
  signed boolean, signed_name text, terms_version text, accepted_at timestamptz
)
language plpgsql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_admin boolean := public.is_admin();
BEGIN
  IF NOT v_admin AND NOT EXISTS (
    SELECT 1 FROM public.cohort_memberships cm
    WHERE cm.cohort_id = p_cohort_id AND cm.profile_id = auth.uid()
      AND cm.role_in_cohort::text IN ('facilitator', 'lead_facilitator')
  ) THEN
    RAISE EXCEPTION 'Access denied' USING ERRCODE = '42501';
  END IF;
  RETURN QUERY
  SELECT p.id, p.full_name::text, (CASE WHEN v_admin THEN p.email END)::text, cm.role_in_cohort::text,
         p.role::text IN ('participant', 'facilitator'), a.id IS NOT NULL, a.signed_name, a.terms_version, a.accepted_at
  FROM public.cohort_memberships cm
  JOIN public.profiles p ON p.id = cm.profile_id
  LEFT JOIN public.terms_acceptances a ON a.profile_id = p.id AND a.terms_type = p.role::text
  WHERE cm.cohort_id = p_cohort_id
  ORDER BY cm.role_in_cohort::text DESC, lower(coalesce(p.full_name, p.email));
END;
$function$;

commit;

select 'lead facilitator access fixed' as result;
