-- ============================================================================
-- WS5.5 v2 — get_participant_final_score: dedupe to latest submission per lens
-- ============================================================================
-- Fixes the duplicate-reviewed-row bug without changing the output JSON shape.
-- Output keys identical to the live version the dashboards consume.
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
WITH latest AS (
  SELECT DISTINCT ON (s.lens_id)
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
reviewed AS (
  SELECT unit, score
    FROM latest
   WHERE review_status = 'reviewed'
),
agg AS (
  SELECT
    (SELECT AVG(score)::numeric FROM reviewed WHERE unit = 2 AND score IS NOT NULL) AS u2,
    (SELECT AVG(score)::numeric FROM reviewed WHERE unit = 3 AND score IS NOT NULL) AS u3,
    (SELECT AVG(score)::numeric FROM reviewed WHERE unit = 4 AND score IS NOT NULL) AS u4,
    (SELECT count(*) FROM reviewed WHERE score IS NULL) AS unscored
)
SELECT jsonb_build_object(
  'unit2_avg',           u2,
  'unit3_avg',           u3,
  'unit4_avg',           u4,
  'capstone_avg',        NULL,
  'capstone_pending',    true,
  'final_pct', round(
       COALESCE(u2, 0) * 0.25
     + COALESCE(u3, 0) * 0.25
     + COALESCE(u4, 0) * 0.25
     + 0
  , 2),
  'certified', false,
  'unscored_lens_count', unscored
)
FROM agg;
$$;

GRANT EXECUTE ON FUNCTION
  public.get_participant_final_score(uuid, uuid) TO authenticated;
