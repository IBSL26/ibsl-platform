-- Live sessions per unit, Join from 30 minutes before the start (1 Nov 2026).
-- Run in the Supabase SQL editor ("S2R Portal Production"). Safe to run again.

-- 1. Every new or edited session must belong to a unit (existing rows are left as they are).
alter table public.cohort_sessions drop constraint if exists cohort_sessions_unit_required;
alter table public.cohort_sessions add constraint cohort_sessions_unit_required check (unit_no is not null) not valid;

-- 2. Participants and facilitators no longer read the sessions table directly (nothing in the portal
--    does); they read through get_my_sessions(), which holds back the Teams link until it is time.
drop policy if exists "cohort_sessions_read" on public.cohort_sessions;
create policy "cohort_sessions_read"
  on public.cohort_sessions for select
  to authenticated
  using (public.is_admin());

-- 3. The Teams link reaches a participant only from 30 minutes before the start until the end.
--    Facilitators and admins always receive it.
create or replace function public.get_my_sessions()
returns table (
  session_id uuid, cohort_id uuid, cohort_name text, title text, unit_no integer,
  starts_at timestamptz, duration_minutes integer, teams_url text,
  will_record boolean, recording_url text, notes text
)
language sql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
  select s.id, s.cohort_id, c.name, s.title, s.unit_no,
         s.starts_at, s.duration_minutes,
         case
           when exists (select 1 from public.profiles p
                        where p.id = auth.uid() and p.role in ('admin', 'facilitator'))
             then s.teams_url
           when now() >= s.starts_at - interval '30 minutes'
            and now() <= s.starts_at + make_interval(mins => s.duration_minutes)
             then s.teams_url
           else null
         end,
         s.will_record, s.recording_url, s.notes
  from public.cohort_sessions s
  join public.cohorts c on c.id = s.cohort_id
  where s.status = 'scheduled'
    and s.last_sent_at is not null
    and c.archived_at is null
    and exists (select 1 from public.cohort_memberships cm
                where cm.cohort_id = s.cohort_id and cm.profile_id = auth.uid())
  order by s.starts_at;
$function$;
