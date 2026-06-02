-- ============================================================================
-- WS5.5 — get_participant_final_score: count only the LATEST submission per lens
-- ============================================================================
-- BUG (confirmed against live data):
--   A participant can have MULTIPLE reviewed submissions for the same lens —
--   an older reviewed row with score = NULL and a newer reviewed row carrying
--   the revision's score. The previous definition's `scored` CTE selected
--   EVERY reviewed row (filtered only by unit), so:
--     • unscored_lens_count counted the stale NULL-scored row
--       (→ "1 reviewed lens not yet scored" for an all-100 participant), and
--     • unit averages were skewed by duplicate rows for the same lens.
--   The repo's prior version already excluded unit 1; the real fault was
--   per-lens duplicates, not Foundations.
--
-- FIX:
--   Collapse to ONE row per lens — the most recent submission by submitted_at
--   (the timestamp that advances on each revision; same column every other
--   query orders by). reviewed_at then id break ties deterministically. This
--   single "latest per lens" set feeds BOTH the unit averages and the
--   unscored_lens_count, so a superseded NULL-scored row can no longer be
--   counted or averaged.
--
--   Semantics preserved otherwise:
--     • Only units 2/3/4 are scored (unit 1 / Foundations excluded).
--     • A lens whose LATEST submission is reviewed contributes its score
--       (NULL latest score → still counted as one unscored lens, correctly).
--     • A lens whose latest submission is not yet reviewed contributes nothing
--       (neither averaged nor counted as unscored) — it is mid-review.
--
-- Idempotent CREATE OR REPLACE. Output JSON shape is unchanged. Run in Supabase
-- (this file is NOT auto-executed).
-- ============================================================================

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
-- One row per lens: the most recent submission (units 2/3/4 only).
WITH latest AS (
  SELECT DISTINCT ON (s.lens_id)
         s.lens_id        AS lens_id,
         lc.unit          AS unit,
         s.score          AS score,
         s.review_status  AS review_status
    FROM submissions s
    JOIN lens_catalog lc ON lc.id = s.lens_id
   WHERE s.profile_id = p_profile_id
     AND s.cohort_id  = p_cohort_id
     AND lc.unit IN (2, 3, 4)
   ORDER BY s.lens_id,
            s.submitted_at DESC NULLS LAST,
            s.reviewed_at  DESC NULLS LAST,
            s.id           DESC
),
-- Of those latest-per-lens rows, keep the ones that are reviewed.
scored AS (
  SELECT unit, score
    FROM latest
   WHERE review_status = 'reviewed'
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
-- End WS5.5 fix.
-- ============================================================================
