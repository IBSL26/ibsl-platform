-- ============================================================================
-- S2R Portal · Unit 10 · The Enterprise ESRG Alignment Clinic (27 October 2026)
-- 1. A function that lets a group member's Unit 10 page read every member's
--    part 4.5 Functional ESRG Performance Scanner (and nothing else), so that
--    Section 5 builds the group's Enterprise ESRG Scanner from them.
-- 2. The Capstone Unit 10 section now has 4 boxes (10A to 10D); every other
--    unit keeps its live box count.
-- It adds one function and changes one small helper. No table and no saved
-- text is changed. It can be run twice.
-- ============================================================================

create or replace function public.team_esrg_scans(p_cohort_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_team uuid;
begin
  if auth.uid() is null then raise exception 'not authenticated'; end if;
  v_team := team_work_my_team(p_cohort_id);
  if v_team is null then return '[]'::jsonb; end if;
  return coalesce((
    select jsonb_agg(jsonb_build_object(
             'profile_id', p.id,
             'full_name',  p.full_name,
             'head', (select case when jsonb_typeof(r.value) = 'string' then r.value #>> '{}' end
                        from lens_responses r
                       where r.profile_id = p.id and r.lens_id = 'u4m1_lens9' and r.response_key = 'esrg_scan_head'),
             'scan', (select case when jsonb_typeof(r.value) = 'string' then r.value #>> '{}' end
                        from lens_responses r
                       where r.profile_id = p.id and r.lens_id = 'u4m1_lens9' and r.response_key = 'esrg_scan'))
           order by p.full_name)
      from capstone_individual ci join profiles p on p.id = ci.profile_id
     where ci.team_id = v_team), '[]'::jsonb);
end;
$$;

revoke execute on function public.team_esrg_scans(uuid) from public, anon;
grant execute on function public.team_esrg_scans(uuid) to authenticated;

do $$
declare v text := ''; k text;
begin
  foreach k in array array['u1','u2','u3','u4','u5','u6','u7','u8','u9','u11','u12'] loop
    v := v || format(' when %L then %s', k, public.capstone_section_box_count(k));
  end loop;
  execute 'create or replace function public.capstone_section_box_count(p_key text) returns integer language sql immutable set search_path = public as $f$ select case p_key'
          || v || ' when ''u10'' then 4 else 5 end; $f$';
end $$;

-- Check (changes nothing). Expected: 8, 6, 6, 6, 3, 3, 5, 5, 5, 4, 5, 5
select public.capstone_section_box_count('u1') as u1, public.capstone_section_box_count('u2') as u2, public.capstone_section_box_count('u3') as u3,
       public.capstone_section_box_count('u4') as u4, public.capstone_section_box_count('u5') as u5, public.capstone_section_box_count('u6') as u6,
       public.capstone_section_box_count('u7') as u7, public.capstone_section_box_count('u8') as u8, public.capstone_section_box_count('u9') as u9,
       public.capstone_section_box_count('u10') as u10, public.capstone_section_box_count('u11') as u11, public.capstone_section_box_count('u12') as u12;
