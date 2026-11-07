-- 7 Nov 2026: Unit 1 marks sit on each reflection. Each marked reflection carries the skill it evidences;
-- the skill result is worked out from these marks on the review page (set_skill_evidence).
create table if not exists public.competency_u1_marks (
  cohort_id    uuid not null,
  profile_id   uuid not null,
  response_key text not null,
  mark         text not null check (mark in ('not_evidenced', 'evidenced', 'developing_others')),
  set_by       uuid,
  set_at       timestamptz not null default now(),
  primary key (cohort_id, profile_id, response_key)
);
alter table public.competency_u1_marks enable row level security;

create or replace function public.get_u1_marks(p_submission_id uuid)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_sub record;
BEGIN
  SELECT x.cohort_id, x.profile_id INTO v_sub FROM public.submissions x WHERE x.id = p_submission_id;
  IF NOT FOUND OR NOT public.competency_can_review(v_sub.cohort_id) THEN
    RAISE EXCEPTION 'Access denied' USING ERRCODE = '42501';
  END IF;
  RETURN (SELECT coalesce(jsonb_object_agg(m.response_key, m.mark), '{}'::jsonb)
          FROM public.competency_u1_marks m
          WHERE m.cohort_id = v_sub.cohort_id AND m.profile_id = v_sub.profile_id);
END;
$function$;

create or replace function public.set_u1_mark(p_submission_id uuid, p_key text, p_mark text)
returns boolean language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
DECLARE
  v_sub record;
BEGIN
  SELECT x.cohort_id, x.profile_id INTO v_sub FROM public.submissions x WHERE x.id = p_submission_id;
  IF NOT FOUND OR NOT public.competency_can_review(v_sub.cohort_id) THEN
    RAISE EXCEPTION 'Access denied' USING ERRCODE = '42501';
  END IF;
  IF p_key !~ '^r_m[1-5]_[a-z_]+$' THEN
    RAISE EXCEPTION 'Mark not valid' USING ERRCODE = '22023';
  END IF;
  IF p_mark IS NULL OR p_mark = '' THEN
    DELETE FROM public.competency_u1_marks m
    WHERE m.cohort_id = v_sub.cohort_id AND m.profile_id = v_sub.profile_id AND m.response_key = p_key;
    RETURN true;
  END IF;
  INSERT INTO public.competency_u1_marks (cohort_id, profile_id, response_key, mark, set_by)
  VALUES (v_sub.cohort_id, v_sub.profile_id, p_key, p_mark, auth.uid())
  ON CONFLICT (cohort_id, profile_id, response_key)
  DO UPDATE SET mark = excluded.mark, set_by = excluded.set_by, set_at = now();
  RETURN true;
END;
$function$;

revoke all on function public.get_u1_marks(uuid) from public, anon;
revoke all on function public.set_u1_mark(uuid, text, text) from public, anon;
grant execute on function public.get_u1_marks(uuid) to authenticated;
grant execute on function public.set_u1_mark(uuid, text, text) to authenticated;

select 'unit 1 reflection marks ready' as result;
