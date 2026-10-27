-- Session reminders, attendance and missed-session check-ins.
-- Run once in the Supabase SQL editor (safe to run again). Needs migrations/cohort_sessions.sql first.
--
-- What it adds
--   1. Reminder stamps, so each reminder goes out once:
--        cohort_sessions.reminder_for_start  (the start time the day-before reminder was sent for)
--        capstone_brief.reminder_for_due     (the deadline the Blueprint reminder was sent for)
--      A session or deadline that moves gets a fresh reminder.
--   2. session_attendance: the admin's tick per participant per session.
--   3. session_checkins: one check-in per participant not ticked, with a drafted message
--      the admin edits and sends. Nothing reaches a participant until the admin presses Send.
-- The emails themselves are sent by the Edge Functions send-reminders (hourly) and
-- send-session-email (kind "checkin").
-- Who can do what: admins only. No direct table writes from the browser.

-- 1. Reminder stamps ---------------------------------------------------------------------
alter table public.cohort_sessions add column if not exists reminder_for_start timestamptz;
alter table public.capstone_brief  add column if not exists reminder_for_due   timestamptz;

-- 2. Attendance -----------------------------------------------------------------------------
create table if not exists public.session_attendance (
  session_id uuid not null references public.cohort_sessions(id) on delete cascade,
  profile_id uuid not null references public.profiles(id) on delete cascade,
  attended   boolean not null,
  marked_by  uuid references public.profiles(id),
  marked_at  timestamptz not null default now(),
  primary key (session_id, profile_id)
);
alter table public.session_attendance enable row level security;
drop policy if exists "session_attendance_admin_read" on public.session_attendance;
create policy "session_attendance_admin_read"
  on public.session_attendance for select to authenticated
  using (public.is_admin());

-- 3. Check-ins -------------------------------------------------------------------------------
create table if not exists public.session_checkins (
  id               uuid primary key default gen_random_uuid(),
  session_id       uuid not null references public.cohort_sessions(id) on delete cascade,
  cohort_id        uuid not null references public.cohorts(id) on delete cascade,
  profile_id       uuid not null references public.profiles(id) on delete cascade,
  subject          text not null,
  body             text not null,
  status           text not null default 'open' check (status in ('open', 'sent', 'dismissed')),
  created_at       timestamptz not null default now(),
  alert_emailed_at timestamptz,
  sent_at          timestamptz,
  sent_by          uuid references public.profiles(id),
  unique (session_id, profile_id)
);
create index if not exists session_checkins_cohort_idx on public.session_checkins (cohort_id, status);
alter table public.session_checkins enable row level security;
drop policy if exists "session_checkins_admin_read" on public.session_checkins;
create policy "session_checkins_admin_read"
  on public.session_checkins for select to authenticated
  using (public.is_admin());

-- 4. Admin: who was at a session ---------------------------------------------------------------
-- One row per participant in the cohort. attended is null until the admin has ticked the list.
create or replace function public.admin_get_session_attendance(p_session_id uuid)
returns table (profile_id uuid, full_name text, email text, attended boolean, checkin_status text)
language plpgsql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_cohort uuid;
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  SELECT s.cohort_id INTO v_cohort FROM public.cohort_sessions s WHERE s.id = p_session_id;
  IF v_cohort IS NULL THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  RETURN QUERY
  SELECT p.id, p.full_name, p.email, a.attended, c.status
  FROM public.cohort_memberships cm
  JOIN public.profiles p ON p.id = cm.profile_id
  LEFT JOIN public.session_attendance a ON a.session_id = p_session_id AND a.profile_id = p.id
  LEFT JOIN public.session_checkins  c ON c.session_id = p_session_id AND c.profile_id = p.id
  WHERE cm.cohort_id = v_cohort
    AND p.role = 'participant'
  ORDER BY lower(coalesce(p.full_name, p.email));
END;
$function$;

-- 5. Admin: save the attendance ticks -----------------------------------------------------------
-- p_attended lists the participants who attended. Every other participant is marked absent and
-- gets a check-in with a drafted message. Ticking someone later removes their unsent check-in.
create or replace function public.admin_save_session_attendance(p_session_id uuid, p_attended uuid[])
returns jsonb
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_s        public.cohort_sessions%ROWTYPE;
  v_cohort   text;
  v_when     text;
  v_present  uuid[] := coalesce(p_attended, '{}');
  v_marked   integer := 0;
  v_absent   integer := 0;
  v_new      integer := 0;
  r          record;
  v_first    text;
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  SELECT * INTO v_s FROM public.cohort_sessions WHERE id = p_session_id;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Session not found' USING ERRCODE = '23503';
  END IF;
  IF v_s.status <> 'scheduled' THEN
    RAISE EXCEPTION 'This session is cancelled.' USING ERRCODE = '22023';
  END IF;
  IF v_s.starts_at > now() THEN
    RAISE EXCEPTION 'Attendance can be taken once the session has started.' USING ERRCODE = '22023';
  END IF;
  SELECT name INTO v_cohort FROM public.cohorts WHERE id = v_s.cohort_id;
  v_when := trim(to_char(v_s.starts_at AT TIME ZONE 'Africa/Johannesburg', 'FMDay FMDD FMMonth'));

  FOR r IN
    SELECT p.id, p.full_name
    FROM public.cohort_memberships cm
    JOIN public.profiles p ON p.id = cm.profile_id
    WHERE cm.cohort_id = v_s.cohort_id AND p.role = 'participant'
  LOOP
    v_marked := v_marked + 1;
    INSERT INTO public.session_attendance (session_id, profile_id, attended, marked_by, marked_at)
    VALUES (p_session_id, r.id, r.id = ANY(v_present), auth.uid(), now())
    ON CONFLICT (session_id, profile_id)
    DO UPDATE SET attended = excluded.attended, marked_by = excluded.marked_by, marked_at = excluded.marked_at;

    IF r.id = ANY(v_present) THEN
      DELETE FROM public.session_checkins
      WHERE session_id = p_session_id AND profile_id = r.id AND status = 'open';
    ELSE
      v_absent := v_absent + 1;
      v_first := coalesce(nullif(split_part(trim(coalesce(r.full_name, '')), ' ', 1), ''), 'there');
      INSERT INTO public.session_checkins (session_id, cohort_id, profile_id, subject, body)
      VALUES (
        p_session_id, v_s.cohort_id, r.id,
        'We missed you at ' || v_s.title,
        'Hi ' || v_first || ',' || E'\n\n' ||
        'We missed you at the ' || v_cohort || ' live session on ' || v_when || ', ' || v_s.title || '.' || E'\n\n' ||
        CASE WHEN v_s.will_record
          THEN 'The recording and the unit material are on your S2R® Portal, so you can catch up on what was covered.'
          ELSE 'The unit material is on your S2R® Portal, so you can catch up on what was covered.'
        END || E'\n\n' ||
        'Is everything all right? If something is making it hard to join the sessions, reply to this email and let us know how we can help.' || E'\n\n' ||
        'Kind regards' || E'\n' ||
        'IBSL Programme Team'
      )
      ON CONFLICT (session_id, profile_id) DO NOTHING;
      IF FOUND THEN v_new := v_new + 1; END IF;
    END IF;
  END LOOP;

  RETURN jsonb_build_object('marked', v_marked, 'absent', v_absent, 'new_checkins', v_new);
END;
$function$;

-- 6. Admin: attendance totals per session, for the Live sessions card --------------------------
create or replace function public.admin_cohort_attendance_summary(p_cohort_id uuid)
returns table (session_id uuid, marked integer, attended integer)
language plpgsql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  RETURN QUERY
  SELECT a.session_id, count(*)::integer, count(*) FILTER (WHERE a.attended)::integer
  FROM public.session_attendance a
  JOIN public.cohort_sessions s ON s.id = a.session_id
  WHERE s.cohort_id = p_cohort_id
  GROUP BY a.session_id;
END;
$function$;

-- 7. Admin: check-ins for a cohort ----------------------------------------------------------------
create or replace function public.admin_list_cohort_checkins(p_cohort_id uuid)
returns table (
  id uuid, session_id uuid, session_title text, session_starts_at timestamptz,
  profile_id uuid, full_name text, email text,
  subject text, body text, status text, created_at timestamptz, sent_at timestamptz
)
language plpgsql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  RETURN QUERY
  SELECT c.id, c.session_id, s.title, s.starts_at, c.profile_id, p.full_name, p.email,
         c.subject, c.body, c.status, c.created_at, c.sent_at
  FROM public.session_checkins c
  JOIN public.cohort_sessions s ON s.id = c.session_id
  JOIN public.profiles p ON p.id = c.profile_id
  WHERE c.cohort_id = p_cohort_id
  ORDER BY (c.status = 'open') DESC, s.starts_at DESC, lower(coalesce(p.full_name, p.email));
END;
$function$;

-- 8. Admin: edit or set aside a check-in -----------------------------------------------------------
create or replace function public.admin_save_checkin(p_checkin_id uuid, p_subject text, p_body text)
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
DECLARE
  v_subject text := trim(coalesce(p_subject, ''));
  v_body    text := trim(coalesce(p_body, ''));
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  IF v_subject = '' OR v_body = '' THEN
    RAISE EXCEPTION 'The subject and the message are both needed.' USING ERRCODE = '22023';
  END IF;
  UPDATE public.session_checkins SET subject = v_subject, body = v_body
  WHERE id = p_checkin_id AND status = 'open';
  IF NOT FOUND THEN
    RAISE EXCEPTION 'This check-in was already sent or set aside.' USING ERRCODE = '22023';
  END IF;
  RETURN p_checkin_id;
END;
$function$;

create or replace function public.admin_dismiss_checkin(p_checkin_id uuid)
returns uuid
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $function$
BEGIN
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION 'Access denied: admin role required' USING ERRCODE = '42501';
  END IF;
  UPDATE public.session_checkins SET status = 'dismissed'
  WHERE id = p_checkin_id AND status = 'open';
  IF NOT FOUND THEN
    RAISE EXCEPTION 'This check-in was already sent or set aside.' USING ERRCODE = '22023';
  END IF;
  RETURN p_checkin_id;
END;
$function$;

-- 9. Permissions: signed-in users only (each function checks for an admin) ------------------------
revoke all on function public.admin_get_session_attendance(uuid) from public, anon;
revoke all on function public.admin_save_session_attendance(uuid, uuid[]) from public, anon;
revoke all on function public.admin_cohort_attendance_summary(uuid) from public, anon;
revoke all on function public.admin_list_cohort_checkins(uuid) from public, anon;
revoke all on function public.admin_save_checkin(uuid, text, text) from public, anon;
revoke all on function public.admin_dismiss_checkin(uuid) from public, anon;
grant execute on function public.admin_get_session_attendance(uuid) to authenticated;
grant execute on function public.admin_save_session_attendance(uuid, uuid[]) to authenticated;
grant execute on function public.admin_cohort_attendance_summary(uuid) to authenticated;
grant execute on function public.admin_list_cohort_checkins(uuid) to authenticated;
grant execute on function public.admin_save_checkin(uuid, text, text) to authenticated;
grant execute on function public.admin_dismiss_checkin(uuid) to authenticated;

-- 10. Check: should return one row
select 'attendance and check-ins ready' as result,
       (select count(*) from public.session_attendance) as attendance_rows,
       (select count(*) from public.session_checkins) as checkins;
