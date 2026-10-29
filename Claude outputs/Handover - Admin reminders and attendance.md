# Admin: session reminders, Blueprint reminder, attendance and missed-session check-ins

Built 27 October 2026 on Carol's decision ("We are not engaging them, we are closing the gaps ourselves"). Of the five points an outside builder offered, Carol kept two: reminders (point 2) and early alerts for a missed session (point 4). Participant record, progress tracking and the faculty view stay as they are; there are no deadline alerts (units carry no dates). Facilitators never see the Blueprint; the admin enters the final mark (existing box in Capstone Teams).

## What it does

- **Session reminder:** 1 to 26 hours before each live session that was sent to the cohort, one email to every active cohort member (participants and facilitators) with date, time and Join session. Skipped when the invite itself went out within the last day. A session whose time changes gets a fresh reminder.
- **Blueprint reminder:** 3 days before the Capstone submission deadline (Capstone brief), one email to each member of each Capstone team in the cohort, with the team's sections agreed (X of 12). Name used: "Capstone S2R Blueprint" (Carol, 27 Oct). The portal pages still say "Capstone Blueprint" (86 places) and take the new name with the unit work.
- **Attendance:** in the admin console, Cohort → Live sessions, every sent session that has started has Take attendance / Change attendance. The admin ticks who attended. Chip: "Attended N of M", or "Attendance not taken" on a past session.
- **Check-ins:** each participant left unticked gets a drafted check-in under "Check-ins · missed sessions" on the same card. The admin opens it (Read and send), edits, and presses Send, Save changes or Set aside. Replies go to projects@ibsleadership.com. Nothing reaches a participant until the admin presses Send. Ticking someone later removes their unsent check-in; a sent or set-aside check-in is never redrafted.
- **Alert:** the hourly run emails projects@ibsleadership.com once per batch of new check-ins, listing cohort, session and names.

## Files

- `migrations/session_reminders_attendance.sql`: columns `cohort_sessions.reminder_for_start`, `capstone_brief.reminder_for_due`; tables `session_attendance`, `session_checkins` (admin read only, no direct writes); functions `admin_get_session_attendance`, `admin_save_session_attendance`, `admin_cohort_attendance_summary`, `admin_list_cohort_checkins`, `admin_save_checkin`, `admin_dismiss_checkin`. Safe to run twice. `log_activity` is not touched (its allowlist was not re-created, to avoid overwriting live events).
- `migrations/send_reminders_schedule.sql`: pg_cron + pg_net hourly job `ibsl-send-reminders` (minute 7). Template only: the CRON_SECRET is never committed (public repository).
- `supabase/functions/send-reminders/index.ts`: new Edge Function. Secrets: RESEND_API_KEY, SB_SERVICE_ROLE_KEY, CRON_SECRET. Refuses any call without the secret header.
- `supabase/functions/send-session-email/index.ts`: new kind `checkin` (`{ kind: "checkin", checkin_id }`), admin-only like the other kinds; sender "IBSL Programme Team", reply-to projects@. Existing kinds unchanged.
- `dashboard_A.html`: [SESSIONS] block only (styles, two modals `sesAttModal` and `sesCiModal`, state, chips, actions, load, check-in list). If the new SQL is not run yet, the card still lists sessions and simply shows no attendance or check-ins.

## Tests (cloud workspace, 27 Oct)

- SQL in a stand-in Postgres (pglite): 18/18 (counts, drafts, re-ticking, set aside, refusal for non-admins and future sessions, run twice).
- Both Edge Functions type-checked with Deno and run against an in-memory database: 28/28 (windows, stamps, no repeats, moved session, failed send retried, alert, check-in send, refusals, existing invite still works).
- Admin card in headless Chromium with a stand-in client: 21/21, no page errors.

## Go-live order

1. Carol approves the email wording (session reminder, Blueprint reminder, check-in draft, admin alert).
2. Files into her folder; Carol pushes (dashboard_A.html, the two SQL files, the two function files, this handover).
3. SQL: session_reminders_attendance.sql (read-only check first).
4. Deploy send-reminders (new) and redeploy send-session-email; set the CRON_SECRET secret.
5. SQL: the schedule block from the chat, with the secret.
6. Live check: take attendance on a test session, send a test check-in to the test participant, run the job once by hand and read its result.

## Live (27 Oct 2026, 16:15)

- Pushed: 4679a98 (rename + admin card), 55e70ae (senders use the Supabase server key).
- Database: migrations/cohort_sessions.sql had never been run before today; run now, then session_reminders_attendance.sql. Grants added for service_role (select on cohort_sessions, cohorts, cohort_memberships, profiles, capstone_brief, capstone_team, capstone_individual, capstone_blueprint_section, session_checkins; update on cohort_sessions, capstone_brief, session_checkins). pg_net switched on; cron job `ibsl-send-reminders` (jobid 2, minute 7 hourly) active.
- Edge Functions deployed and checked in the dashboard: send-reminders (19,944 chars, reports its key type), send-session-email (23,250 chars, kind checkin). The dashboard asks for a second "Deploy updates" in a confirm box; without it nothing deploys.
- Key finding: the secret SB_SERVICE_ROLE_KEY holds the project's publishable (public) key. Both new senders use SUPABASE_SERVICE_ROLE_KEY (Supabase's own). send-invitation-email(-ts) also read SB_SERVICE_ROLE_KEY and were left untouched at Carol's word; if invitations fail with a permissions error, this is the cause.
- First good run: net._http_response id 6, status 200, nothing due.
- Still open: Storage upload of the renamed decks (Units 1–9 .pptx, manifests, Unit 5 s33.jpg), after all unit changes are complete (Carol). Unit 10 Capstone work on hold until Carol finishes cleaning Unit 10.
