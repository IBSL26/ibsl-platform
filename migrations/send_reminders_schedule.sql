-- Hourly run of the Edge Function send-reminders (session reminders, Blueprint reminder,
-- missed-session alert). Run in the Supabase SQL editor AFTER:
--   1. migrations/session_reminders_attendance.sql has been run, and
--   2. the Edge Function send-reminders is deployed with its CRON_SECRET secret set.
--
-- The secret is NOT kept in this file, because the repository is public. Claude gives the
-- full block, with the secret filled in, in the chat at go-live time. Replace both
-- placeholders below before running.
--   <CRON_SECRET>  the same random value saved as the function's CRON_SECRET secret
--   <ANON_KEY>     the project's public anon key (the SUPABASE_ANON_KEY in the portal pages)

-- 0. Read-only check: which scheduling tools are switched on, and which jobs exist
select extname, extversion from pg_extension where extname in ('pg_cron', 'pg_net');
select jobid, jobname, schedule, active from cron.job order by jobid;

-- 1. Switch on the two tools (no change if they are already on)
create extension if not exists pg_cron with schema pg_catalog;
create extension if not exists pg_net with schema extensions;

-- 2. The hourly job, at 7 minutes past each hour (replaces an earlier copy of itself)
select cron.unschedule(jobid) from cron.job where jobname = 'ibsl-send-reminders';
select cron.schedule(
  'ibsl-send-reminders',
  '7 * * * *',
  $job$
  select net.http_post(
    url     := 'https://tayrxqbrttlrdowrzobm.supabase.co/functions/v1/send-reminders',
    headers := jsonb_build_object(
      'Content-Type',  'application/json',
      'Authorization', 'Bearer <ANON_KEY>',
      'x-cron-secret', '<CRON_SECRET>'
    ),
    body    := '{}'::jsonb
  );
  $job$
);

-- 3. Check: one active row named ibsl-send-reminders
select jobid, jobname, schedule, active from cron.job where jobname = 'ibsl-send-reminders';
