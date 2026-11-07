-- 7 Nov 2026: participants see their marks only once the facilitator has selected Mark as reviewed (all units);
-- the Unit 1 marking sheet for the participant's page and the Learning Portfolio; suggested feedback storage.
begin;

create or replace function public.get_my_reflection_marks(p_lens_id text)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_uid uuid := auth.uid();
  v_unit integer := public.competency_unit_of(p_lens_id);
  v_cohort uuid;
  v_status text;
BEGIN
  SELECT x.cohort_id, x.review_status::text INTO v_cohort, v_status FROM public.submissions x
  WHERE x.profile_id = v_uid AND x.lens_id = p_lens_id
  ORDER BY x.submitted_at DESC NULLS LAST LIMIT 1;
  IF v_cohort IS NULL OR v_unit IS NULL OR v_status IS DISTINCT FROM 'reviewed' THEN RETURN NULL; END IF;
  RETURN jsonb_build_object('marks', (SELECT jsonb_object_agg(m.section_no::text, jsonb_build_object('band', m.band, 'comment', m.comment))
    FROM public.competency_reflection_marks m
    WHERE m.cohort_id = v_cohort AND m.profile_id = v_uid AND m.unit_no = v_unit));
END;
$function$;

create or replace function public.get_u1_sheet(p_profile_id uuid, p_cohort_id uuid)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_status text;
  v_payload jsonb;
BEGIN
  IF auth.uid() IS NULL OR (auth.uid() <> p_profile_id AND NOT public.competency_can_review(p_cohort_id)) THEN
    RETURN NULL;
  END IF;
  SELECT x.review_status::text, x.payload INTO v_status, v_payload FROM public.submissions x
  WHERE x.profile_id = p_profile_id AND x.cohort_id = p_cohort_id AND x.lens_id = 'u1_foundations'
  ORDER BY x.submitted_at DESC NULLS LAST LIMIT 1;
  IF v_status IS DISTINCT FROM 'reviewed' THEN RETURN NULL; END IF;
  RETURN jsonb_build_object(
    'marks', (SELECT coalesce(jsonb_object_agg(m.response_key, m.mark), '{}'::jsonb) FROM public.competency_u1_marks m
              WHERE m.cohort_id = p_cohort_id AND m.profile_id = p_profile_id),
    'answered', (SELECT coalesce(jsonb_agg(e.key), '[]'::jsonb) FROM jsonb_each(coalesce(v_payload -> 'responses', '{}'::jsonb)) e
                 WHERE e.key ~ '^r_m[1-5]_' AND jsonb_typeof(e.value) = 'string' AND btrim(e.value #>> '{}') <> ''));
END;
$function$;
revoke all on function public.get_u1_sheet(uuid, uuid) from public, anon;
grant execute on function public.get_u1_sheet(uuid, uuid) to authenticated;

alter table public.mark_suggestions drop constraint if exists mark_suggestions_scale_check;
alter table public.mark_suggestions add constraint mark_suggestions_scale_check check (scale in ('skill', 'reflection', 'feedback'));

commit;

select 'marks after review, unit 1 sheet, feedback suggestions ready' as result;
