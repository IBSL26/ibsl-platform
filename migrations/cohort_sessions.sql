-- Live sessions per cohort: Teams link, calendar invite, recording link.
-- Run once in the Supabase SQL editor (safe to run again).
--
-- Who can do what
--   Admin: add, edit, cancel, delete (unsent only), add the recording link, send emails.
--   Cohort members (participants and facilitators): see sessions that have been sent
--   to the cohort, through get_my_sessions(). Nobody else sees anything.
-- Emails are sent by the Edge Function send-session-email, which stamps last_sent_at.

-- 1. Table ---------------------------------------------------------------------------
create table if not exists public.cohort_sessions (
  id                 uuid primary key default gen_random_uuid(),
  cohort_id          uuid not null references public.cohorts(id) on delete cascade,
  title              text not null,
  unit_no            integer check (unit_no between 1 and 12),
  starts_at          timestamptz not null,
  duration_minutes   integer not null default 120 check (duration_minutes between 15 and 600),
  teams_url          text not null check (teams_url ~* '^https://'),
  will_record        boolean not null default false,
  recording_url      text check (recording_url is null or recording_url ~* '^https://'),
  notes              text,
  status             text not null default 'scheduled' check (status in ('scheduled', 'cancelled')),
  ical_sequence      integer not null default 0,
  changed_since_sent boolean not null default false,
  last_sent_at       timestamptz,
  recording_sent_at  timestamptz,
  created_by         uuid references public.profiles(id),
  created_at         timestamptz not null default now(),
  updated_at         timestamptz not null default now()
);

create index if not exists cohort_sessions_cohort_starts_idx
  on public.cohort_sessions (cohort_id, starts_at);

alter table public.cohort_sessions enable row level security;

-- Direct table reads: admins, and cohort members for sessions already sent. No direct writes.
drop policy if exists "cohort_sessions_read" on public.cohort_sessions;
create policy "cohort_sessions_read"
  on public.cohort_sessions for select
  to authenticated
  using (
    public.is_admin()
    or (last_sent_at is not null
        and exists (select 1 from public.cohort_memberships cm
                    where cm.cohort_id = cohort_sessions.cohort_id
                      and cm.profile_id = auth.uid()))
  );

-- 2. Activity log: allow the session events ---------------------------------------------
create or replace function public.log_activity(p_event_type text, p_event_detail jsonb default null::jsonb, p_cohort_id uuid default null::uuid)
 returns uuid
 language plpgsql
 security definer
 set search_path to 'public'
as $function$
DECLARE
  v_allowed_events text[] := ARRAY[
    -- Authentication
    'login','logout',
    -- Invitations
    'invitation_sent','invitation_accepted',
    'invitation_bulk_sent','invitation_cancelled','invitation_resent',
    -- Device binding
    'device_trusted','device_confirmed','device_revoked','device_binding_reset',
    -- Lens lifecycle
    'lens_unlocked','lens_locked','lens_completed',
    -- Submissions
    'submission_created','submission_reviewed','submission_returned_for_revision',
    -- Collaboration
    'feedback_posted','message_posted','document_uploaded','document_deleted',
    'facilitator_note_added',
    -- User lifecycle
    'role_changed','account_suspended','account_reactivated','account_deactivated',
    -- Cohort lifecycle
    'cohort_created','cohort_edited','cohort_archived','cohort_unarchived',
    'cohort_facilitator_assigned','cohort_facilitator_removed',
    'cohort_participant_added','cohort_participant_removed',
    'cohort_report_generated',
    -- Live sessions
    'session_created','session_edited','session_cancelled','session_deleted',
    'session_sent','session_recording_added',
    -- Organisation lifecycle
    'organisation_created','organisation_updated',
    'organisation_archived','organisation_unarchived',
    -- Security
    'password_changed','2fa_enabled','2fa_disabled',
    -- Moderation
    'admin_message_hidden','admin_message_flagged',
    'admin_message_unhidden','admin_message_unflagged'
  ];
  v_new_id uuid;
BEGIN
  IF NOT (p_event_type = ANY(v_allowed_events)) THEN
    RAISE EXCEPTION 'log_activity: event_type % is not on the allowlist', p_event_type;
  END IF;

  INSERT INTO public.activity_log (profile_id, cohort_id, event_type, event_detail)
  VALUES (auth.uid(), p_cohort_id, p_event_type, COALESCE(p_event_detail, '{}'::jsonb))
  RETURNING id INTO v_new_id;

  RETURN v_new_id;
END;
$function$;

-- 3. Admin: add or edit a session ---------------------------------------------------------
create or replace function public.admin_save_cohort_session(
  p_cohort_id uuid,
  p_title text,
  p_starts_at timestamptz,
  p_teams_url text,
  p_session_id uuid default null,
  p_unit_no integer default null,
  p_duration_minutes integer default 120,
  p_will_record boolean default false,
  p_notes text default null
)
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_title text := trim(coalesce(p_title, ''));
  v_url   text := trim(coalesce(p_teams_url, ''));
  v_notes text := nullif(trim(coalesce(p_notes, '')), '');
  v_row   public.cohort_sessions%ROWTYPE;
  v_id    uuid;
  v_material boolean;
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM public.cohorts WHERE id = p_cohort_id AND archived_at IS NULL) THEN
    RAISE EXCEPTION 'Cohort not found or archived' USING ERRCODE = '23503';
  END IF;
  IF v_title = '' THEN
    RAISE EXCEPTION 'Session title is required' USING ERRCODE = '22023';
  END IF;
  IF p_starts_at IS NULL THEN
    RAISE EXCEPTION 'Session date and time are required' USING ERRCODE = '22023';
  END IF;
  IF v_url !~* '^https://' THEN
    RAISE EXCEPTION 'The Teams link must start with https://' USING ERRCODE = '22023';
  END IF;
  IF p_unit_no IS NOT NULL AND (p_unit_no < 1 OR p_unit_no > 12) THEN
    RAISE EXCEPTION 'Unit must be between 1 and 12' USING ERRCODE = '22023';
  END IF;
  IF p_duration_minutes IS NULL OR p_duration_minutes < 15 OR p_duration_minutes > 600 THEN
    RAISE EXCEPTION 'Duration must be between 15 and 600 minutes' USING ERRCODE = '22023';
  END IF;

  IF p_session_id IS NULL THEN
    INSERT INTO public.cohort_sessions
      (cohort_id, title, unit_no, starts_at, duration_minutes, teams_url, will_record, notes, created_by)
    VALUES
      (p_cohort_id, v_title, p_unit_no, p_starts_at, p_duration_minutes, v_url, coalesce(p_will_record, false), v_notes, auth.uid())
    RETURNING id INTO v_id;
    PERFORM public.log_activity('session_created',
      jsonb_build_object('session_id', v_id, 'title', v_title, 'starts_at', p_starts_at), p_cohort_id);
    RETURN v_id;
  END IF;

  SELECT * INTO v_row FROM public.cohort_sessions WHERE id = p_session_id AND cohort_id = p_cohort_id;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  IF v_row.status = 'cancelled' THEN
    RAISE EXCEPTION 'A cancelled session cannot be edited. Add a new session.' USING ERRCODE = '22023';
  END IF;

  -- Anything the cohort was told about has changed: flag it so the admin sends an update.
  v_material := v_row.title IS DISTINCT FROM v_title
             OR v_row.unit_no IS DISTINCT FROM p_unit_no
             OR v_row.starts_at IS DISTINCT FROM p_starts_at
             OR v_row.duration_minutes IS DISTINCT FROM p_duration_minutes
             OR v_row.teams_url IS DISTINCT FROM v_url
             OR v_row.will_record IS DISTINCT FROM coalesce(p_will_record, false)
             OR v_row.notes IS DISTINCT FROM v_notes;

  IF NOT v_material THEN
    RETURN p_session_id;
  END IF;

  UPDATE public.cohort_sessions
  SET title = v_title,
      unit_no = p_unit_no,
      starts_at = p_starts_at,
      duration_minutes = p_duration_minutes,
      teams_url = v_url,
      will_record = coalesce(p_will_record, false),
      notes = v_notes,
      ical_sequence = CASE WHEN v_row.last_sent_at IS NOT NULL THEN v_row.ical_sequence + 1 ELSE v_row.ical_sequence END,
      changed_since_sent = (v_row.last_sent_at IS NOT NULL),
      updated_at = now()
  WHERE id = p_session_id;

  PERFORM public.log_activity('session_edited',
    jsonb_build_object('session_id', p_session_id, 'title', v_title, 'starts_at', p_starts_at), p_cohort_id);
  RETURN p_session_id;
END;
$function$;

-- 4. Admin: cancel a session (kept on record; a cancellation email can then be sent) ------
create or replace function public.admin_cancel_cohort_session(p_session_id uuid)
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_row public.cohort_sessions%ROWTYPE;
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  SELECT * INTO v_row FROM public.cohort_sessions WHERE id = p_session_id;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  IF v_row.status = 'cancelled' THEN
    RETURN p_session_id;
  END IF;
  UPDATE public.cohort_sessions
  SET status = 'cancelled',
      ical_sequence = ical_sequence + 1,
      changed_since_sent = (last_sent_at IS NOT NULL),
      updated_at = now()
  WHERE id = p_session_id;
  PERFORM public.log_activity('session_cancelled',
    jsonb_build_object('session_id', p_session_id, 'title', v_row.title), v_row.cohort_id);
  RETURN p_session_id;
END;
$function$;

-- 5. Admin: delete a session that was never sent to the cohort ------------------------------
create or replace function public.admin_delete_cohort_session(p_session_id uuid)
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_row public.cohort_sessions%ROWTYPE;
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  SELECT * INTO v_row FROM public.cohort_sessions WHERE id = p_session_id;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  IF v_row.last_sent_at IS NOT NULL THEN
    RAISE EXCEPTION 'This session was already sent to the cohort. Cancel it so they are told.' USING ERRCODE = '22023';
  END IF;
  PERFORM public.log_activity('session_deleted',
    jsonb_build_object('session_id', p_session_id, 'title', v_row.title), v_row.cohort_id);
  DELETE FROM public.cohort_sessions WHERE id = p_session_id;
  RETURN p_session_id;
END;
$function$;

-- 6. Admin: add, change or clear the recording link -----------------------------------------
create or replace function public.admin_set_session_recording(p_session_id uuid, p_recording_url text)
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_row public.cohort_sessions%ROWTYPE;
  v_url text := nullif(trim(coalesce(p_recording_url, '')), '');
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  SELECT * INTO v_row FROM public.cohort_sessions WHERE id = p_session_id;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  IF v_url IS NOT NULL AND v_url !~* '^https://' THEN
    RAISE EXCEPTION 'The recording link must start with https://' USING ERRCODE = '22023';
  END IF;
  UPDATE public.cohort_sessions
  SET recording_url = v_url,
      recording_sent_at = CASE WHEN v_url IS DISTINCT FROM v_row.recording_url THEN NULL ELSE recording_sent_at END,
      updated_at = now()
  WHERE id = p_session_id;
  PERFORM public.log_activity('session_recording_added',
    jsonb_build_object('session_id', p_session_id, 'title', v_row.title, 'cleared', v_url IS NULL), v_row.cohort_id);
  RETURN p_session_id;
END;
$function$;

-- 7. Admin: list a cohort's sessions -----------------------------------------------------------
create or replace function public.admin_list_cohort_sessions(p_cohort_id uuid)
returns setof public.cohort_sessions
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  RETURN QUERY
  SELECT * FROM public.cohort_sessions WHERE cohort_id = p_cohort_id ORDER BY starts_at;
END;
$function$;

-- 8. Participants and facilitators: my sessions (only those sent to my cohorts) ------------------
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
         s.starts_at, s.duration_minutes, s.teams_url,
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

-- 9. Permissions: signed-in users only -----------------------------------------------------------
revoke all on function public.admin_save_cohort_session(uuid, text, timestamptz, text, uuid, integer, integer, boolean, text) from public, anon;
revoke all on function public.admin_cancel_cohort_session(uuid) from public, anon;
revoke all on function public.admin_delete_cohort_session(uuid) from public, anon;
revoke all on function public.admin_set_session_recording(uuid, text) from public, anon;
revoke all on function public.admin_list_cohort_sessions(uuid) from public, anon;
revoke all on function public.get_my_sessions() from public, anon;
grant execute on function public.admin_save_cohort_session(uuid, text, timestamptz, text, uuid, integer, integer, boolean, text) to authenticated;
grant execute on function public.admin_cancel_cohort_session(uuid) to authenticated;
grant execute on function public.admin_delete_cohort_session(uuid) to authenticated;
grant execute on function public.admin_set_session_recording(uuid, text) to authenticated;
grant execute on function public.admin_list_cohort_sessions(uuid) to authenticated;
grant execute on function public.get_my_sessions() to authenticated;

-- 10. Check: should return one row with the table name
select 'cohort_sessions ready' as result, count(*) as sessions from public.cohort_sessions;
