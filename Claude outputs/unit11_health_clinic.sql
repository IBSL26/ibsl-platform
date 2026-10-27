-- Unit 11 · Section 5 · The Cross-CXO Organisational Health Clinic (27 Oct 2026)
-- Capstone Unit 11 now has 4 boxes (11A-11D). Every other unit keeps its current count. Safe to run twice.
do $$
declare v text := ''; k text;
begin
  foreach k in array array['u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u12'] loop
    v := v || format(' when %L then %s', k, public.capstone_section_box_count(k));
  end loop;
  execute 'create or replace function public.capstone_section_box_count(p_key text) returns integer language sql immutable set search_path = public as $f$ select case p_key'
          || v || ' when ''u11'' then 4 else 5 end; $f$';
end $$;

-- Check (changes nothing). Expected: 8, 6, 6, 6, 3, 3, 5, 5, 5, 4, 4, 5
select public.capstone_section_box_count('u1') as u1, public.capstone_section_box_count('u2') as u2, public.capstone_section_box_count('u3') as u3,
       public.capstone_section_box_count('u4') as u4, public.capstone_section_box_count('u5') as u5, public.capstone_section_box_count('u6') as u6,
       public.capstone_section_box_count('u7') as u7, public.capstone_section_box_count('u8') as u8, public.capstone_section_box_count('u9') as u9,
       public.capstone_section_box_count('u10') as u10, public.capstone_section_box_count('u11') as u11, public.capstone_section_box_count('u12') as u12;
