-- ============================================================================
-- S2R Portal — Capstone Blueprint: Unit 2 section now has 6 boxes (was 8)
-- Run in Supabase (project "S2R Portal Production"), SQL editor.
-- Run on the day the new capstone_P.html goes live. Run Block 1 once.
-- It changes one small helper function. No table and no saved text is touched.
-- ============================================================================

-- ── Block 1 · Number of boxes in each Blueprint section (Unit 2: 8 → 6) ──
create or replace function public.capstone_section_box_count(p_key text)
returns integer language sql immutable set search_path = public as $$
  select case p_key when 'u2' then 6 when 'u3' then 6 when 'u4' then 6 when 'u10' then 6 else 5 end;
$$;

-- ── Block 2 · Check only (changes nothing): has any team already saved Unit 2 text in the old boxes? ──
-- If the answer is 0, there is nothing more to do. If it is above 0, tell Claude the number.
select count(*) as teams_with_saved_unit2_text from public.capstone_blueprint_section where section_key = 'u2';
