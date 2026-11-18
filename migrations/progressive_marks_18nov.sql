-- ============================================================================
-- Progressive mark accumulation (18 Nov 2026)
-- get_participant_final_score: each reviewed unit adds its share of the final %.
--   Module 2 (Units 2–4)   = 25%  -> each unit 25/3
--   Module 3 (Units 5–9)   = 25%  -> each unit 25/5
--   Module 4 (Units 10–12) = 25%  -> each unit 25/3
--   Capstone               = 25%
-- Once every unit is scored the final % equals the agreed formula
-- (module average x 25% each + Capstone x 25%). Existing keys unchanged;
-- new keys: units (per-unit score, weight, earned, running total),
-- units_earned_pct, capstone_earned_pct, units_scored_count, units_total.
-- Return type unchanged (jsonb), so CREATE OR REPLACE is safe.
-- ============================================================================
CREATE OR REPLACE FUNCTION public.get_participant_final_score(p_profile_id uuid, p_cohort_id uuid)
 RETURNS jsonb
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
WITH cat AS (
  SELECT id, unit AS module, sequence, title,
         25.0 / count(*) OVER (PARTITION BY unit) AS weight
    FROM lens_catalog
   WHERE unit IN (2, 3, 4)
),
latest AS (
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
reviewed AS (
  SELECT lens_id, unit, score
    FROM latest
   WHERE review_status = 'reviewed'
),
per_unit AS (
  SELECT c.id, c.module, c.sequence, c.sequence + 1 AS unit_no, c.title, c.weight,
         r.score,
         CASE WHEN r.score IS NOT NULL THEN r.score * c.weight / 100.0 END AS earned
    FROM cat c
    LEFT JOIN reviewed r ON r.lens_id = c.id
),
running AS (
  SELECT p.*,
         SUM(COALESCE(earned, 0)) OVER (ORDER BY sequence) AS cumulative
    FROM per_unit p
),
cap AS (
  SELECT capstone_final_pct AS capstone
    FROM capstone_individual
   WHERE profile_id = p_profile_id
     AND cohort_id  = p_cohort_id
   LIMIT 1
),
agg AS (
  SELECT
    (SELECT AVG(score)::numeric FROM reviewed WHERE unit = 2 AND score IS NOT NULL) AS u2,
    (SELECT AVG(score)::numeric FROM reviewed WHERE unit = 3 AND score IS NOT NULL) AS u3,
    (SELECT AVG(score)::numeric FROM reviewed WHERE unit = 4 AND score IS NOT NULL) AS u4,
    (SELECT count(*) FROM reviewed WHERE score IS NULL) AS unscored,
    (SELECT capstone FROM cap) AS capstone,
    (SELECT COALESCE(SUM(earned), 0) FROM per_unit) AS units_earned,
    (SELECT count(*) FROM per_unit WHERE score IS NOT NULL) AS units_scored,
    (SELECT count(*) FROM per_unit) AS units_total,
    (SELECT jsonb_agg(jsonb_build_object(
        'lens_id',    id,
        'unit_no',    unit_no,
        'module',     module,
        'title',      title,
        'score',      score,
        'weight',     round(weight, 2),
        'earned',     CASE WHEN earned IS NOT NULL THEN round(earned, 2) END,
        'cumulative', CASE WHEN earned IS NOT NULL THEN round(cumulative, 2) END
      ) ORDER BY sequence) FROM running) AS units
)
SELECT jsonb_build_object(
  'unit2_avg',           u2,
  'unit3_avg',           u3,
  'unit4_avg',           u4,
  'capstone_avg',        capstone,
  'capstone_pending',    (capstone IS NULL),
  'units',               units,
  'units_earned_pct',    round(units_earned, 2),
  'capstone_earned_pct', CASE WHEN capstone IS NOT NULL THEN round(capstone * 0.25, 2) END,
  'units_scored_count',  units_scored,
  'units_total',         units_total,
  'final_pct', round(units_earned + COALESCE(capstone, 0) * 0.25, 2),
  'certified', (
       capstone IS NOT NULL
   AND round(units_earned + COALESCE(capstone, 0) * 0.25, 2) >= 80
  ),
  'unscored_lens_count', unscored
)
FROM agg
WHERE is_admin()
   OR p_profile_id = auth.uid()
   OR EXISTS (SELECT 1 FROM cohort_memberships cm
               WHERE cm.cohort_id = p_cohort_id
                 AND cm.profile_id = auth.uid()
                 AND cm.role_in_cohort IN ('facilitator', 'lead_facilitator'));
$function$;
