-- ============================================================================
-- S2R Portal — Capstone Blueprint: the Unit 6 section now has 4 boxes (was 5)
-- Run in Supabase (project "S2R Portal Production"), SQL editor.
-- Run one block at a time, in order. Run each block once.
-- It changes one small helper function. No table and no saved text is touched.
-- ============================================================================

-- ── Block 1 · Check only (changes nothing): how many boxes does the database expect for Unit 6 today? ──
-- The answer should be 5.
select public.capstone_section_box_count('u6') as unit6_boxes_now;

-- ── Block 2 · Set Unit 6 to 4 boxes. Every other unit keeps the number it has today. ──
-- You should see "Success. No rows returned".
do $$
declare v text := ''; k text;
begin
  foreach k in array array['u2','u3','u4','u5','u7','u8','u9','u10','u11','u12'] loop
    v := v || format(' when %L then %s', k, public.capstone_section_box_count(k));
  end loop;
  execute 'create or replace function public.capstone_section_box_count(p_key text) returns integer language sql immutable set search_path = public as $f$ select case p_key'
          || v || ' when ''u6'' then 4 else 5 end; $f$';
end $$;

-- ── Block 3 · Check only (changes nothing): read the numbers back. ──
-- unit6 should now be 4 and unit5 should still be 3. Tell Claude the row you see.
select public.capstone_section_box_count('u2') as unit2, public.capstone_section_box_count('u3') as unit3, public.capstone_section_box_count('u4') as unit4,
       public.capstone_section_box_count('u5') as unit5, public.capstone_section_box_count('u6') as unit6, public.capstone_section_box_count('u7') as unit7,
       public.capstone_section_box_count('u10') as unit10;
