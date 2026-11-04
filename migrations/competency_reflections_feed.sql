-- Competency: reflections feed the Progressive level (4 Nov 2026).
-- Unit Feedback now carries the three admin questions only. The facilitator's skill evidence, drawn from the
-- unit's key reflections, sets the Progressive level once all three skills are reviewed.
-- Scenario questions are removed from the database. Saved feedback, self-ratings and skill evidence are kept.

drop function if exists public.submit_unit_feedback(uuid, integer, integer, integer, text, jsonb);
drop table if exists public.competency_questions;

-- Each key reflection carries a mark: full 20, part 14, none 8, blank 0. Total out of 100.
create table if not exists public.competency_reflection_marks (
  cohort_id  uuid not null references public.cohorts(id) on delete cascade,
  profile_id uuid not null references public.profiles(id) on delete cascade,
  unit_no    integer not null references public.competency_framework(unit_no),
  section_no integer not null check (section_no between 1 and 5),
  band       text not null check (band in ('full', 'part', 'none', 'blank')),
  comment    text,
  set_by     uuid references public.profiles(id),
  set_at     timestamptz not null default now(),
  primary key (cohort_id, profile_id, unit_no, section_no)
);
alter table public.competency_reflection_marks enable row level security;
revoke all on table public.competency_reflection_marks from public, anon, authenticated;

create or replace function public.competency_band_marks(p_band text)
returns integer language sql immutable as $function$
  select case p_band when 'full' then 20 when 'part' then 14 when 'none' then 8 else 0 end;
$function$;

-- Which framework skill (1 to 3) each of Sections 1 to 4 evidences. Section 5 is developing others.
create or replace function public.competency_section_skill(p_unit integer, p_section integer)
returns integer language sql immutable as $function$
  select (('{"2":[1,2,3,1],"3":[1,2,3,1],"4":[1,3,2,2],"5":[2,2,1,3],"6":[1,3,2,2],"7":[1,1,2,3],"8":[2,2,3,1],"9":[1,2,1,3],"10":[1,2,1,3],"11":[3,2,1,3],"12":[1,3,2,1]}'::jsonb)->p_unit::text->>(p_section - 1))::int;
$function$;
revoke all on function public.competency_band_marks(text) from public, anon, authenticated;
revoke all on function public.competency_section_skill(integer, integer) from public, anon, authenticated;

-- Units 2 to 12: blank until all five reflections are marked. A skill counts when each of its reflections
-- is Partly or Fully evidenced. None or one skill: Developing. Two: Practising. All three: Accomplished.
-- All three with Section 5 Fully evidenced: Leading. Unit 1: the facilitator's skill evidence, on the same counts.
create or replace function public.competency_level(p_cohort uuid, p_profile uuid, p_unit integer)
returns integer language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_n integer;
  v_leading boolean;
BEGIN
  IF p_unit = 1 THEN
    SELECT CASE WHEN count(*) < 3 THEN NULL
                ELSE count(*) FILTER (WHERE e.evidence <> 'not_evidenced') END,
           count(*) FILTER (WHERE e.evidence = 'developing_others') >= 1
    INTO v_n, v_leading
    FROM public.competency_skill_evidence e
    WHERE e.cohort_id = p_cohort AND e.profile_id = p_profile AND e.unit_no = p_unit;
  ELSE
    IF (SELECT count(*) FROM public.competency_reflection_marks m
        WHERE m.cohort_id = p_cohort AND m.profile_id = p_profile AND m.unit_no = p_unit) < 5 THEN
      RETURN NULL;
    END IF;
    SELECT 3 - count(DISTINCT public.competency_section_skill(p_unit, m.section_no))
             FILTER (WHERE m.section_no < 5 AND m.band IN ('none', 'blank')),
           bool_or(m.section_no = 5 AND m.band = 'full')
    INTO v_n, v_leading
    FROM public.competency_reflection_marks m
    WHERE m.cohort_id = p_cohort AND m.profile_id = p_profile AND m.unit_no = p_unit;
  END IF;
  IF v_n IS NULL THEN RETURN NULL; END IF;
  RETURN CASE WHEN v_n = 3 AND v_leading THEN 4 WHEN v_n = 3 THEN 3 WHEN v_n = 2 THEN 2 ELSE 1 END;
END;
$function$;
revoke all on function public.competency_level(uuid, uuid, integer) from public, anon, authenticated;

create or replace function public.get_unit_feedback_form(p_cohort_id uuid, p_unit_no integer)
returns jsonb language plpgsql volatile security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_uid uuid := auth.uid();
BEGIN
  IF NOT public.competency_is_participant(p_cohort_id, v_uid) THEN
    RAISE EXCEPTION 'Only participants complete this form' USING ERRCODE = '42501';
  END IF;
  RETURN (
    SELECT jsonb_build_object('unit_no', f.unit_no, 'competency', f.name,
      'submitted', EXISTS (SELECT 1 FROM public.unit_feedback_status s
                           WHERE s.cohort_id = p_cohort_id AND s.profile_id = v_uid AND s.unit_no = f.unit_no),
      'due', public.competency_unit_due(p_cohort_id, v_uid, f.unit_no))
    FROM public.competency_framework f WHERE f.unit_no = p_unit_no);
END;
$function$;

create or replace function public.submit_unit_feedback(
  p_cohort_id uuid, p_unit_no integer, p_content_clear integer, p_delivery_helped integer, p_improvement text)
returns jsonb language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_uid uuid := auth.uid();
  v_text text := btrim(coalesce(p_improvement, ''));
BEGIN
  IF NOT public.competency_is_participant(p_cohort_id, v_uid) THEN
    RAISE EXCEPTION 'Only participants complete this form' USING ERRCODE = '42501';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM public.competency_self_ratings r WHERE r.cohort_id = p_cohort_id AND r.profile_id = v_uid) THEN
    RAISE EXCEPTION 'Complete your Competency Self-Rating first' USING ERRCODE = '22023';
  END IF;
  IF NOT public.competency_unit_due(p_cohort_id, v_uid, p_unit_no) THEN
    RAISE EXCEPTION 'This form opens once the unit has been taught' USING ERRCODE = '22023';
  END IF;
  IF EXISTS (SELECT 1 FROM public.unit_feedback_status s
             WHERE s.cohort_id = p_cohort_id AND s.profile_id = v_uid AND s.unit_no = p_unit_no) THEN
    RAISE EXCEPTION 'You have already submitted this form' USING ERRCODE = '23505';
  END IF;
  IF p_content_clear NOT BETWEEN 1 AND 5 OR p_delivery_helped NOT BETWEEN 1 AND 5 THEN
    RAISE EXCEPTION 'Answer the two rating questions' USING ERRCODE = '22023';
  END IF;
  IF length(v_text) < 3 OR length(v_text) > 2000 THEN
    RAISE EXCEPTION 'Write one thing that would improve this unit' USING ERRCODE = '22023';
  END IF;
  INSERT INTO public.unit_feedback_status (cohort_id, profile_id, unit_no) VALUES (p_cohort_id, v_uid, p_unit_no);
  INSERT INTO public.unit_feedback_answers (cohort_id, unit_no, content_clear, delivery_helped, improvement)
  VALUES (p_cohort_id, p_unit_no, p_content_clear, p_delivery_helped, v_text);
  RETURN jsonb_build_object('ok', true);
END;
$function$;
revoke all on function public.submit_unit_feedback(uuid, integer, integer, integer, text) from public, anon;
grant execute on function public.submit_unit_feedback(uuid, integer, integer, integer, text) to authenticated;

-- Facilitator: read and set the marks.
create or replace function public.get_reflection_marks(p_submission_id uuid)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_sub record;
  v_unit integer;
BEGIN
  SELECT x.cohort_id, x.profile_id, x.lens_id INTO v_sub FROM public.submissions x WHERE x.id = p_submission_id;
  IF NOT FOUND OR NOT public.competency_can_review(v_sub.cohort_id) THEN
    RAISE EXCEPTION 'Access denied' USING ERRCODE = '42501';
  END IF;
  v_unit := public.competency_unit_of(v_sub.lens_id);
  RETURN jsonb_build_object('unit_no', v_unit,
    'marks', (SELECT coalesce(jsonb_object_agg(m.section_no::text, jsonb_build_object('band', m.band, 'comment', m.comment)), '{}'::jsonb)
              FROM public.competency_reflection_marks m
              WHERE m.cohort_id = v_sub.cohort_id AND m.profile_id = v_sub.profile_id AND m.unit_no = v_unit));
END;
$function$;

create or replace function public.set_reflection_mark(p_submission_id uuid, p_section integer, p_band text, p_comment text)
returns boolean language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_sub record;
  v_unit integer;
BEGIN
  SELECT x.cohort_id, x.profile_id, x.lens_id INTO v_sub FROM public.submissions x WHERE x.id = p_submission_id;
  IF NOT FOUND OR NOT public.competency_can_review(v_sub.cohort_id) THEN
    RAISE EXCEPTION 'Access denied' USING ERRCODE = '42501';
  END IF;
  v_unit := public.competency_unit_of(v_sub.lens_id);
  IF v_unit IS NULL OR v_unit < 2 OR p_section NOT BETWEEN 1 AND 5 OR p_band NOT IN ('full', 'part', 'none', 'blank') THEN
    RAISE EXCEPTION 'Mark not valid' USING ERRCODE = '22023';
  END IF;
  INSERT INTO public.competency_reflection_marks (cohort_id, profile_id, unit_no, section_no, band, comment, set_by)
  VALUES (v_sub.cohort_id, v_sub.profile_id, v_unit, p_section, p_band, nullif(left(btrim(coalesce(p_comment, '')), 1000), ''), auth.uid())
  ON CONFLICT (cohort_id, profile_id, unit_no, section_no)
  DO UPDATE SET band = excluded.band, comment = excluded.comment, set_by = excluded.set_by, set_at = now();
  RETURN true;
END;
$function$;

-- Participant: their own marks, once the unit has been reviewed or returned.
create or replace function public.get_my_reflection_marks(p_lens_id text)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_uid uuid := auth.uid();
  v_unit integer := public.competency_unit_of(p_lens_id);
  v_cohort uuid;
BEGIN
  SELECT x.cohort_id INTO v_cohort FROM public.submissions x
  WHERE x.profile_id = v_uid AND x.lens_id = p_lens_id AND x.review_status::text IN ('reviewed', 'pending_revision')
  ORDER BY x.submitted_at DESC LIMIT 1;
  IF v_cohort IS NULL OR v_unit IS NULL THEN RETURN NULL; END IF;
  RETURN jsonb_build_object('marks', (SELECT jsonb_object_agg(m.section_no::text, jsonb_build_object('band', m.band, 'comment', m.comment))
    FROM public.competency_reflection_marks m
    WHERE m.cohort_id = v_cohort AND m.profile_id = v_uid AND m.unit_no = v_unit));
END;
$function$;

do $$
declare f text;
begin
  foreach f in array array['get_reflection_marks(uuid)', 'set_reflection_mark(uuid, integer, text, text)', 'get_my_reflection_marks(text)'] loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;

select 'reflections now feed competence' as result,
       (select count(*) from information_schema.tables where table_schema = 'public' and table_name = 'competency_questions') as scenario_tables_left;
