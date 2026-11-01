-- CESI_Women_26 programme timetable entries (1 Nov 2026). Safe to run again: an entry already there is not added twice.
do $$
declare c uuid;
begin
  select id into c from public.cohorts where name = 'CESI_Women_26';

  -- Unit 1 moves to 16:00–19:00 (it was already sent, so it is marked for Send update).
  update public.cohort_sessions
  set starts_at = '2026-11-03 16:00+02', duration_minutes = 180,
      ical_sequence = ical_sequence + case when last_sent_at is not null then 1 else 0 end,
      changed_since_sent = (last_sent_at is not null), updated_at = now()
  where cohort_id = c and unit_no = 1 and status = 'scheduled'
    and (starts_at <> '2026-11-03 16:00+02' or duration_minutes <> 180);

  insert into public.cohort_sessions (cohort_id, title, unit_no, unit_nos, kind, starts_at, duration_minutes, teams_url, will_record)
  select c, v.title, v.u[1], v.u, v.kind, v.s::timestamptz, v.m, 'https://ibslportal.netlify.app', v.rec
  from (values
    ('Unit 2 · Strategy Visioning & Success in Practice (SiP)', array[2], 'unit', '2026-11-05 16:00+02', 180, true),
    ('Unit 3 · SiP KISS Mapping & OKR Definition + Unit 4 · Direction Integrity (ABCV-MBT)', array[3,4], 'unit', '2026-11-09 16:00+02', 180, true),
    ('Unit 5 · Aligning Heart & Mind', array[5], 'unit', '2026-11-12 16:00+02', 180, true),
    ('Unit 6 · Performance Management Setup + Unit 7 · Establishing Performance Expectations', array[6,7], 'unit', '2026-11-16 16:00+02', 180, true),
    ('Unit 8 · Performance Measurement', array[8], 'unit', '2026-11-19 16:00+02', 180, true),
    ('Unit 9 · Strategic Unclogging', array[9], 'unit', '2026-11-23 16:00+02', 180, true),
    ('Unit 10 · ESRG Alignment', array[10], 'unit', '2026-11-26 16:00+02', 180, true),
    ('Unit 11 · Culture Reinforcement & Organisational Health + Unit 12 · Sustaining Performance', array[11,12], 'unit', '2026-11-30 16:00+02', 180, true),
    ('Team finalisation of the Capstone', null::integer[], 'event', '2026-12-02 15:00+02', 120, false),
    ('Capstone presentations', null::integer[], 'event', '2026-12-03 08:30+02', 210, false),
    ('Graduation and gala dinner', null::integer[], 'event', '2026-12-03 17:00+02', 300, false)
  ) as v(title, u, kind, s, m, rec)
  where not exists (select 1 from public.cohort_sessions x
                    where x.cohort_id = c and x.title = v.title and x.status = 'scheduled');
end $$;
