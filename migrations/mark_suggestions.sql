-- 7 Nov 2026: suggested marks (worked out by Claude in the suggest-marks Edge Function), kept until the answers change.
create table if not exists public.mark_suggestions (
  submission_id uuid not null references public.submissions(id) on delete cascade,
  scale         text not null check (scale in ('skill', 'reflection')),
  answers_hash  text not null,
  result        jsonb not null default '{}'::jsonb,
  created_at    timestamptz not null default now(),
  primary key (submission_id, scale)
);
alter table public.mark_suggestions enable row level security;
-- No policies: only the Edge Function (service role) reads and writes it.
select 'mark suggestions ready' as result;
