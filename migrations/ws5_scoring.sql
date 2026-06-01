-- ============================================================================
-- Workstream 5 — Lens scoring & certification
-- File: migrations/ws5_scoring.sql
--
-- RUN MANUALLY in the Supabase SQL editor. This file is NOT auto-executed by
-- the app or by Claude. Read the warning on STEP 2 before running it.
--
-- Steps:
--   1. submissions.score            — new nullable 0..100 column   (safe, runnable as-is)
--   2. review_submission(...)       — add p_score param            (⚠ VERIFY-FIRST, see below)
--   3. get_participant_final_score  — new read-only scoring RPC     (safe, runnable as-is)
-- ============================================================================


-- ────────────────────────────────────────────────────────────────────────────
-- STEP 1 — submissions.score
-- Per-lens facilitator score, 0..100, nullable (NULL = reviewed but not yet
-- scored, or never reviewed). Unit 1 / Foundations is never scored.
-- ────────────────────────────────────────────────────────────────────────────
ALTER TABLE submissions
  ADD COLUMN score integer
  CHECK (score IS NULL OR (score >= 0 AND score <= 100));

COMMENT ON COLUMN submissions.score IS
  'WS5 facilitator lens score, 0..100. NULL = not yet scored. Unit 1 excluded from scoring.';


-- ────────────────────────────────────────────────────────────────────────────
-- STEP 2 — review_submission: add p_score
--
--  ⚠⚠⚠  VERIFY BEFORE RUNNING  ⚠⚠⚠
--  The live body of review_submission() is NOT stored anywhere in this repo or
--  its git history — it exists only in the database. The CREATE OR REPLACE block
--  below is a REFERENCE RECONSTRUCTION inferred from the frontend's observed
--  contract (return codes, unlock behaviour). It is NOT guaranteed to byte-match
--  your live function's auth checks, unlock logic, or return shape.
--
--  RECOMMENDED — apply the minimal delta to YOUR live body instead of pasting
--  this reconstruction:
--
--    1. Dump the current definition:
--         SELECT pg_get_functiondef(
--           'public.review_submission(uuid,text,boolean)'::regprocedure);
--
--    2. Apply ONLY these two changes to that body:
--         (a) signature: add a 4th parameter   ", p_score integer DEFAULT NULL"
--         (b) the UPDATE that sets facilitator_feedback: add   ", score = p_score"
--             to the same SET list (so score is written in the same statement).
--
--    3. Because the argument list changes (3 args -> 4 args), drop the old
--       3-arg function first so a 3-arg call resolves unambiguously to the new
--       one (PostgREST fills the defaulted p_score). Then recreate:
--         DROP FUNCTION IF EXISTS public.review_submission(uuid, text, boolean);
--         CREATE OR REPLACE FUNCTION public.review_submission(
--           p_submission_id uuid, p_feedback text, p_unlock_next boolean,
--           p_score integer DEFAULT NULL) ... <your verified body> ...
--
--  Diff the reconstruction below against step-1's dump. If they differ, TRUST
--  YOUR LIVE BODY + the two deltas above; do not paste this reconstruction blind.
--  ─────────────────────────────────────────────────────────────────────────
--
--  Drop the old 3-arg signature so the new 4-arg (defaulted) function is the
--  single resolution target for both 3-arg and 4-arg callers.
DROP FUNCTION IF EXISTS public.review_submission(uuid, text, boolean);

CREATE OR REPLACE FUNCTION public.review_submission(
  p_submission_id uuid,
  p_feedback      text,
  p_unlock_next   boolean,
  p_score         integer DEFAULT NULL            -- WS5: new, optional, written below
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_uid          uuid := auth.uid();
  v_sub          submissions%ROWTYPE;
  v_succ_id      text;
  v_succ_title   text;
  v_succ_count   int;
  v_prev_status  text;
  v_unlocked     boolean := false;
  v_already      boolean := false;
BEGIN
  -- ── auth ──
  IF v_uid IS NULL THEN
    RETURN jsonb_build_object('ok', false, 'error', 'not_authenticated');
  END IF;

  SELECT * INTO v_sub FROM submissions WHERE id = p_submission_id;
  IF NOT FOUND THEN
    RETURN jsonb_build_object('ok', false, 'error', 'submission_not_found');
  END IF;

  IF NOT can_facilitate_lens(v_uid, v_sub.lens_id) THEN
    RETURN jsonb_build_object('ok', false, 'error', 'not_authorised');
  END IF;

  IF v_sub.review_status = 'reviewed' THEN
    RETURN jsonb_build_object('ok', false, 'error', 'already_reviewed');
  END IF;

  -- Only submitted / pending_revision-resubmitted rows may be reviewed.
  IF v_sub.review_status NOT IN ('submitted', 'pending', 'in_review') THEN
    RETURN jsonb_build_object('ok', false, 'error', 'invalid_state',
                              'current_status', v_sub.review_status);
  END IF;

  -- ── commit feedback + score in one UPDATE (WS5: score = p_score) ──
  UPDATE submissions
     SET facilitator_feedback        = p_feedback,
         score                       = p_score,            -- WS5 addition
         review_status               = 'reviewed',
         reviewed_at                 = now(),
         facilitator_feedback_draft  = NULL,
         feedback_draft_updated_at   = NULL
   WHERE id = p_submission_id;

  -- ── mark this lens completed for the participant ──
  UPDATE lens_progress
     SET status = 'completed'
   WHERE profile_id = v_sub.profile_id
     AND cohort_id  = v_sub.cohort_id
     AND lens_id    = v_sub.lens_id;

  -- ── optionally unlock the successor lens ──
  IF p_unlock_next THEN
    SELECT count(*) INTO v_succ_count
      FROM lens_catalog WHERE requires_lens = v_sub.lens_id;

    IF v_succ_count > 1 THEN
      RETURN jsonb_build_object('ok', false, 'error', 'ambiguous_successor');
    ELSIF v_succ_count = 1 THEN
      SELECT id, title INTO v_succ_id, v_succ_title
        FROM lens_catalog WHERE requires_lens = v_sub.lens_id;

      SELECT status INTO v_prev_status
        FROM lens_progress
       WHERE profile_id = v_sub.profile_id
         AND cohort_id  = v_sub.cohort_id
         AND lens_id    = v_succ_id;

      IF v_prev_status = 'locked' OR v_prev_status IS NULL THEN
        UPDATE lens_progress
           SET status = 'unlocked'
         WHERE profile_id = v_sub.profile_id
           AND cohort_id  = v_sub.cohort_id
           AND lens_id    = v_succ_id;
        v_unlocked := true;
      ELSE
        v_already := true;
      END IF;
    END IF;
  END IF;

  RETURN jsonb_build_object(
    'ok', true,
    'next_lens_unlocked', v_unlocked,
    'next_lens_title', v_succ_title,
    'next_lens_was_already_unlocked', v_already
  );
END;
$$;

GRANT EXECUTE ON FUNCTION
  public.review_submission(uuid, text, boolean, integer) TO authenticated;


-- ────────────────────────────────────────────────────────────────────────────
-- STEP 3 — get_participant_final_score (new, read-only)
--
-- Returns a JSON object with per-unit averages for units 2/3/4, each weighted
-- x0.25, plus a x0.25 capstone slot (null for now — capstone not built).
--
--   final_pct  = u2*0.25 + u3*0.25 + u4*0.25 + capstone(=0 while null)
--   certified  = (final_pct >= 80 AND capstone IS NOT NULL)   -> always false now
--   unscored_lens_count = reviewed-but-unscored lenses in units 2/3/4
--
-- Unit 1 (Foundations) is excluded from all scoring.
--
-- SECURITY INVOKER: respects existing RLS — the caller must already be able to
-- SELECT the participant's submissions (facilitators have such a policy; the
-- dashboard reads submissions directly elsewhere). It does NOT bypass RLS.
-- ────────────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.get_participant_final_score(
  p_profile_id uuid,
  p_cohort_id  uuid
)
RETURNS jsonb
LANGUAGE sql
STABLE
SECURITY INVOKER
SET search_path = public
AS $$
WITH scored AS (
  SELECT lc.unit AS unit, s.score AS score
    FROM submissions s
    JOIN lens_catalog lc ON lc.id = s.lens_id
   WHERE s.profile_id     = p_profile_id
     AND s.cohort_id      = p_cohort_id
     AND s.review_status  = 'reviewed'
     AND lc.unit IN (2, 3, 4)
),
unit_avg AS (
  SELECT unit, AVG(score)::numeric AS avg_score
    FROM scored
   WHERE score IS NOT NULL
   GROUP BY unit
),
agg AS (
  SELECT
    (SELECT avg_score FROM unit_avg WHERE unit = 2) AS u2,
    (SELECT avg_score FROM unit_avg WHERE unit = 3) AS u3,
    (SELECT avg_score FROM unit_avg WHERE unit = 4) AS u4,
    (SELECT count(*)  FROM scored WHERE score IS NULL) AS unscored
)
SELECT jsonb_build_object(
  -- raw per-unit averages (null = no reviewed+scored submissions in that unit yet)
  'unit_averages', jsonb_build_object(
     '2', CASE WHEN u2 IS NULL THEN NULL ELSE round(u2, 2) END,
     '3', CASE WHEN u3 IS NULL THEN NULL ELSE round(u3, 2) END,
     '4', CASE WHEN u4 IS NULL THEN NULL ELSE round(u4, 2) END
  ),
  -- each unit's weighted contribution (avg * 0.25), missing unit contributes 0
  'unit_components', jsonb_build_object(
     '2', round(COALESCE(u2, 0) * 0.25, 2),
     '3', round(COALESCE(u3, 0) * 0.25, 2),
     '4', round(COALESCE(u4, 0) * 0.25, 2)
  ),
  'unit_weight',      0.25,
  'capstone',         NULL,          -- not built yet (Workstream 4 territory)
  'capstone_weight',  0.25,
  'capstone_pending', true,          -- flag: capstone counted as 0 in final_pct
  'final_pct', round(
       COALESCE(u2, 0) * 0.25
     + COALESCE(u3, 0) * 0.25
     + COALESCE(u4, 0) * 0.25
     + 0                              -- capstone treated as 0 while null
  , 2),
  -- certified requires a real capstone, so this is false until capstone ships
  'certified', (
       (COALESCE(u2,0)*0.25 + COALESCE(u3,0)*0.25 + COALESCE(u4,0)*0.25 + 0) >= 80
       AND false  -- capstone IS NOT NULL  (always null today)
  ),
  'unscored_lens_count', agg.unscored
)
FROM agg;
$$;

GRANT EXECUTE ON FUNCTION
  public.get_participant_final_score(uuid, uuid) TO authenticated;

-- ============================================================================
-- End WS5 migration.
-- ============================================================================
