-- 7 Nov 2026: facilitators see Capstone progress and read the Blueprint (read-only) for the units they teach.
-- Lead facilitators and the admin: all units. Adds three read-only functions; no table or existing function changes.
begin;

create or replace function public.fac_capstone_units(p_cohort_id uuid)
returns int[] language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select case
    when public.is_admin() or exists (select 1 from public.cohort_memberships cm
      where cm.cohort_id = p_cohort_id and cm.profile_id = auth.uid() and cm.role_in_cohort::text = 'lead_facilitator')
      then array[1,2,3,4,5,6,7,8,9,10,11,12]
    else coalesce((select array_agg(distinct u order by u)
      from public.cohort_memberships cm
      cross join lateral unnest(case nullif(cm.unit::text, '')
        when '1' then array[1] when '2' then array[2,3,4] when '3' then array[5,6,7,8,9] when '4' then array[10,11,12]
        else array[]::int[] end) as u
      where cm.cohort_id = p_cohort_id and cm.profile_id = auth.uid() and cm.role_in_cohort::text = 'facilitator'), array[]::int[])
  end;
$function$;

create or replace function public.get_facilitator_capstone(p_cohort_id uuid)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
declare
  v_units int[];
begin
  if auth.uid() is null then raise exception 'not authenticated'; end if;
  if not (public.is_admin() or exists (select 1 from public.cohort_memberships cm
      where cm.cohort_id = p_cohort_id and cm.profile_id = auth.uid() and cm.role_in_cohort::text in ('facilitator', 'lead_facilitator'))) then
    raise exception 'Access denied' using errcode = '42501';
  end if;
  v_units := public.fac_capstone_units(p_cohort_id);
  return coalesce((select jsonb_agg(jsonb_build_object(
      'team_id', t.id,
      'team_name', t.team_name,
      'members', coalesce((select jsonb_agg(jsonb_build_object('profile_id', p.id, 'full_name', p.full_name) order by p.full_name)
                   from public.capstone_individual ci join public.profiles p on p.id = ci.profile_id where ci.team_id = t.id), '[]'::jsonb),
      'sections', coalesce((select jsonb_agg(jsonb_build_object(
          'key', k.key,
          'unit', k.u,
          'agreed', coalesce(s.status = 'agreed', false),
          'agreed_at', s.agreed_at,
          'scribe', (select full_name from public.profiles where id = w.scribe_id),
          'version', coalesce(w.version, 0),
          'agreed_by', case when coalesce(w.version, 0) > 0 then coalesce((select jsonb_agg(p.full_name order by p.full_name)
              from public.capstone_individual ci join public.profiles p on p.id = ci.profile_id
              where ci.team_id = t.id and exists (select 1 from public.team_work_agreement a
                where a.team_id = t.id and a.lens_id = w.lens_id and a.profile_id = ci.profile_id and a.version = w.version)), '[]'::jsonb)
            else '[]'::jsonb end,
          'not_yet', case when coalesce(w.version, 0) > 0 then coalesce((select jsonb_agg(p.full_name order by p.full_name)
              from public.capstone_individual ci join public.profiles p on p.id = ci.profile_id
              where ci.team_id = t.id and not exists (select 1 from public.team_work_agreement a
                where a.team_id = t.id and a.lens_id = w.lens_id and a.profile_id = ci.profile_id and a.version = w.version)), '[]'::jsonb)
            else '[]'::jsonb end
        ) order by k.u)
        from (select u, 'u' || u as key from unnest(v_units) as u) k
        left join public.capstone_blueprint_section s on s.team_id = t.id and s.section_key = k.key
        left join public.team_work w on w.team_id = t.id and w.lens_id = public.capstone_section_lens(k.key)), '[]'::jsonb)
    ) order by t.team_name)
    from public.capstone_team t where t.cohort_id = p_cohort_id), '[]'::jsonb);
end;
$function$;

create or replace function public.get_facilitator_capstone_team(p_team_id uuid)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
declare
  v_team  public.capstone_team%rowtype;
  v_units int[];
begin
  if auth.uid() is null then raise exception 'not authenticated'; end if;
  select * into v_team from public.capstone_team where id = p_team_id;
  if not found then raise exception 'team not found'; end if;
  if not (public.is_admin() or exists (select 1 from public.cohort_memberships cm
      where cm.cohort_id = v_team.cohort_id and cm.profile_id = auth.uid() and cm.role_in_cohort::text in ('facilitator', 'lead_facilitator'))) then
    raise exception 'Access denied' using errcode = '42501';
  end if;
  v_units := public.fac_capstone_units(v_team.cohort_id);
  return jsonb_build_object(
    'team',    jsonb_build_object('id', v_team.id, 'name', v_team.team_name, 'reopened', v_team.blueprint_reopened),
    'cohort',  (select jsonb_build_object('id', c.id, 'name', c.name) from public.cohorts c where c.id = v_team.cohort_id),
    'brief',   (select to_jsonb(b) - 'updated_by' from public.capstone_brief b where b.cohort_id = v_team.cohort_id),
    'locked',  true,
    'members', coalesce((select jsonb_agg(jsonb_build_object('profile_id', p.id, 'full_name', p.full_name) order by p.full_name)
                 from public.capstone_individual ci join public.profiles p on p.id = ci.profile_id where ci.team_id = p_team_id), '[]'::jsonb),
    'sections', coalesce((select jsonb_agg(jsonb_build_object(
        'key',             k.key,
        'open',            public.capstone_section_open(p_team_id, k.key),
        'status',          coalesce(s.status, 'draft'),
        'content',         case when s.status = 'agreed' then s.content else '{}'::jsonb end,
        'updated_at',      s.updated_at,
        'updated_by_name', (select full_name from public.profiles where id = s.updated_by),
        'sent_at',         s.sent_at,
        'sent_by_name',    (select full_name from public.profiles where id = s.sent_by),
        'agreed_at',       s.agreed_at,
        'confirmations',   coalesce((select jsonb_agg(jsonb_build_object('profile_id', c2.profile_id, 'confirmed_at', c2.confirmed_at))
                                       from public.capstone_blueprint_confirmation c2 where c2.section_id = s.id), '[]'::jsonb)
      ) order by k.u)
      from (select u, 'u' || u as key from unnest(v_units) as u) k
      left join public.capstone_blueprint_section s on s.team_id = p_team_id and s.section_key = k.key), '[]'::jsonb)
  );
end;
$function$;

revoke all on function public.fac_capstone_units(uuid), public.get_facilitator_capstone(uuid), public.get_facilitator_capstone_team(uuid) from public, anon;
grant execute on function public.fac_capstone_units(uuid), public.get_facilitator_capstone(uuid), public.get_facilitator_capstone_team(uuid) to authenticated;

commit;

select 'facilitator capstone view ready' as result;
