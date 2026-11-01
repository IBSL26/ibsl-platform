-- Portal terms of use (1 Nov 2026): signed once, before live sessions.
-- Run in the Supabase SQL editor ("S2R Portal Production"). Safe to run again.

create table if not exists public.terms_acceptances (
  id            uuid primary key default gen_random_uuid(),
  profile_id    uuid references public.profiles(id) on delete set null,
  terms_type    text not null check (terms_type in ('participant', 'facilitator')),
  terms_version text not null,
  signed_name   text not null check (length(btrim(signed_name)) >= 2),
  signed_email  text,
  accepted_at   timestamptz not null default now(),
  unique (profile_id, terms_type)
);
alter table public.terms_acceptances enable row level security;
revoke all on table public.terms_acceptances from public, anon, authenticated;

-- Internal check: has this person signed the terms for their role? Only participants and facilitators sign.
create or replace function public.terms_cleared(p_uid uuid)
returns boolean
language sql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
  select exists (select 1 from public.profiles p where p.id = p_uid and p.role::text not in ('participant', 'facilitator'))
      or exists (select 1 from public.profiles p
                 join public.terms_acceptances a
                   on a.profile_id = p.id and a.terms_type = p.role::text
                 where p.id = p_uid);
$function$;
revoke all on function public.terms_cleared(uuid) from public, anon, authenticated;

-- The signed-in person's own terms status.
create or replace function public.get_my_terms()
returns table (
  required boolean, signed boolean, terms_type text, terms_version text,
  signed_name text, accepted_at timestamptz
)
language sql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
  select p.role::text in ('participant', 'facilitator'), a.id is not null,
         case when p.role::text in ('participant', 'facilitator') then p.role::text end,
         a.terms_version, a.signed_name, a.accepted_at
  from public.profiles p
  left join public.terms_acceptances a on a.profile_id = p.id and a.terms_type = p.role::text
  where p.id = auth.uid();
$function$;
revoke all on function public.get_my_terms() from public, anon;
grant execute on function public.get_my_terms() to authenticated;

-- Sign once. A second call leaves the first signature in place.
create or replace function public.accept_portal_terms(p_version text, p_signed_name text)
returns timestamptz
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_role  text;
  v_email text;
  v_name  text := btrim(coalesce(p_signed_name, ''));
  v_at    timestamptz;
BEGIN
  SELECT p.role::text, p.email INTO v_role, v_email FROM public.profiles p WHERE p.id = auth.uid();
  IF v_role IS NULL OR v_role NOT IN ('participant', 'facilitator') THEN
    RAISE EXCEPTION 'These terms apply to participants and facilitators' USING ERRCODE = '42501';
  END IF;
  IF length(v_name) < 2 OR length(v_name) > 200 THEN
    RAISE EXCEPTION 'Enter your full name' USING ERRCODE = '22023';
  END IF;
  IF coalesce(btrim(p_version), '') = '' THEN
    RAISE EXCEPTION 'Terms version missing' USING ERRCODE = '22023';
  END IF;
  INSERT INTO public.terms_acceptances (profile_id, terms_type, terms_version, signed_name, signed_email)
  VALUES (auth.uid(), v_role, btrim(p_version), v_name, v_email)
  ON CONFLICT (profile_id, terms_type) DO NOTHING;
  SELECT a.accepted_at INTO v_at FROM public.terms_acceptances a
  WHERE a.profile_id = auth.uid() AND a.terms_type = v_role;
  RETURN v_at;
END;
$function$;
revoke all on function public.accept_portal_terms(text, text) from public, anon;
grant execute on function public.accept_portal_terms(text, text) to authenticated;

-- Who has signed in a cohort: the admin record, and the facilitator's approved list.
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
      AND cm.role_in_cohort = 'facilitator'
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
revoke all on function public.get_cohort_terms_record(uuid) from public, anon;
grant execute on function public.get_cohort_terms_record(uuid) to authenticated;

-- My sessions: the Teams link is held back from anyone who has not signed the terms.
create or replace function public.get_my_sessions()
returns table (
  session_id uuid, cohort_id uuid, cohort_name text, title text, unit_no integer,
  starts_at timestamptz, duration_minutes integer, teams_url text,
  will_record boolean, recording_url text, notes text,
  unit_nos integer[], kind text
)
language sql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
  select s.id, s.cohort_id, c.name, s.title, s.unit_no,
         s.starts_at, s.duration_minutes,
         case
           when not public.terms_cleared(auth.uid()) then null
           when exists (select 1 from public.profiles p
                        where p.id = auth.uid() and p.role in ('admin', 'facilitator'))
             then s.teams_url
           when now() >= s.starts_at - interval '30 minutes'
            and now() <= s.starts_at + make_interval(mins => s.duration_minutes)
             then s.teams_url
           else null
         end,
         s.will_record, s.recording_url, s.notes,
         coalesce(s.unit_nos, case when s.unit_no is not null then array[s.unit_no] end),
         s.kind
  from public.cohort_sessions s
  join public.cohorts c on c.id = s.cohort_id
  where s.status = 'scheduled'
    and c.archived_at is null
    and exists (select 1 from public.cohort_memberships cm
                where cm.cohort_id = s.cohort_id and cm.profile_id = auth.uid())
  order by s.starts_at;
$function$;
revoke all on function public.get_my_sessions() from public, anon;
grant execute on function public.get_my_sessions() to authenticated;

-- Direct table reads: admins only, so the Teams link can only be reached through get_my_sessions().
drop policy if exists "cohort_sessions_read" on public.cohort_sessions;
create policy "cohort_sessions_read"
  on public.cohort_sessions for select
  to authenticated
  using (public.is_admin());

select 'portal terms ready' as result, (select count(*) from public.terms_acceptances) as signed;
