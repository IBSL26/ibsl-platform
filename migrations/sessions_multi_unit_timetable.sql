-- One live session can carry one or more units, or be a programme event; programme timetable (1 Nov 2026).
-- Run in the Supabase SQL editor ("S2R Portal Production"). Safe to run again.

alter table public.cohort_sessions add column if not exists unit_nos integer[];
alter table public.cohort_sessions add column if not exists kind text not null default 'unit';
alter table public.cohort_sessions drop constraint if exists cohort_sessions_kind_check;
alter table public.cohort_sessions add constraint cohort_sessions_kind_check check (kind in ('unit', 'event'));
alter table public.cohort_sessions drop constraint if exists cohort_sessions_unit_required;
update public.cohort_sessions set unit_nos = array[unit_no] where unit_nos is null and unit_no is not null;

-- Admin: set what a session is for (called by the admin dashboard straight after saving a session).
create or replace function public.admin_set_session_units(p_session_id uuid, p_kind text, p_unit_nos integer[])
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_row  public.cohort_sessions%ROWTYPE;
  v_kind text := coalesce(p_kind, 'unit');
  v_nos  integer[];
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  SELECT * INTO v_row FROM public.cohort_sessions WHERE id = p_session_id;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  IF v_kind NOT IN ('unit', 'event') THEN
    RAISE EXCEPTION 'Unknown session type' USING ERRCODE = '22023';
  END IF;
  IF v_kind = 'unit' THEN
    SELECT array_agg(DISTINCT n ORDER BY n) INTO v_nos FROM unnest(p_unit_nos) AS n WHERE n IS NOT NULL;
    IF v_nos IS NULL OR array_length(v_nos, 1) IS NULL THEN
      RAISE EXCEPTION 'Choose at least one unit' USING ERRCODE = '22023';
    END IF;
    IF EXISTS (SELECT 1 FROM unnest(v_nos) AS n WHERE n < 1 OR n > 12) THEN
      RAISE EXCEPTION 'Units must be between 1 and 12' USING ERRCODE = '22023';
    END IF;
  ELSE
    v_nos := NULL;
  END IF;
  IF v_row.kind IS DISTINCT FROM v_kind OR v_row.unit_nos IS DISTINCT FROM v_nos THEN
    UPDATE public.cohort_sessions
    SET kind = v_kind,
        unit_nos = v_nos,
        unit_no = CASE WHEN v_kind = 'unit' THEN v_nos[1] ELSE NULL END,
        changed_since_sent = (last_sent_at IS NOT NULL) OR changed_since_sent,
        updated_at = now()
    WHERE id = p_session_id;
  END IF;
  RETURN p_session_id;
END;
$function$;
revoke all on function public.admin_set_session_units(uuid, text, integer[]) from public, anon;
grant execute on function public.admin_set_session_units(uuid, text, integer[]) to authenticated;

-- My sessions: every scheduled session of my cohorts (the timetable shows them as soon as they are set up).
-- The Teams link reaches a participant only from 30 minutes before the start until the end;
-- facilitators and admins always receive it.
drop function if exists public.get_my_sessions();
create function public.get_my_sessions()
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
