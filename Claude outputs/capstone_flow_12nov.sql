-- ============================================================================
-- S2R Portal · Our Position removed from the Capstone S2R Blueprint (12 November 2026)
-- Units 3 to 12 no longer carry the group's Our Position box (xS / team_summary).
-- The box map that fills each section when the group agrees drops the xS box, and the
-- box count each section needs matches its map (Unit 1 corrected from 9 to its 7 boxes).
-- No table and no saved text is changed. Can be run twice.
-- ============================================================================
create or replace function public.capstone_section_map(p_key text)
returns jsonb language sql immutable set search_path = public as $$
  select case p_key
    when 'u1' then '{"1A":"pc_company","1B":"pc_team","1C":"pc_org","1T":"pc_trigger","1D":"pc_challenges","1E":"pc_address","1H":"pc_problem"}'
    when 'u2' then '{"2P":"strategy_period","2A":"arch_output","2B":"intent_statement","2C":"sip_d1_st","2D":"sip_d2_st","2E":"sip_d3_st","2F":"sip_d4_st","2G":"sip_summary"}'
    when 'u3' then '{"3A":"kiss_keep","3B":"kiss_improve","3C":"kiss_start","3D":"kiss_stop","3E":"ent_priorities","3F":"ent_okrs"}'
    when 'u4' then '{"4A":"mbt_arena","4B":"mbt_bound","4C":"mbt_comp","4D":"mbt_value","4E":"mbt_verify","4F":"mbt_blind"}'
    when 'u5' then '{"5A":"kit_profile","5B":"kit_mind","5C":"kit_habit"}'
    when 'u6' then '{"6A":"cm_map","6B":"cm_faces","6D":"cm_scorecard","6C":"cm_ward"}'
    when 'u7' then '{"7A":"ex_future","7B":"ex_delivery","7C":"ex_chain","7D":"ex_ownership","7E":"ex_dialogue"}'
    when 'u8' then '{"8A":"rd_warning","8B":"rd_accountability","8C":"rd_learning","8D":"rd_credibility","8E":"rd_ward"}'
    when 'u9' then '{"9A":"uc_challenge","9B":"uc_clog","9C":"uc_lever","9D":"uc_review_realign","9E":"uc_restore"}'
    when 'u10' then '{"10A":"es_scanner","10B":"es_interp","10C":"es_resp","10D":"es_plan"}'
    when 'u11' then '{"11A":"oh_func","11B":"oh_cons","11C":"oh_rrr","11D":"oh_resp","11E":"oh_coc"}'
    when 'u12' then '{"12A":"qs_strategic","12B":"qs_operational","12C":"qs_behavioural","12D":"qs_kiss"}'
  end::jsonb;
$$;

create or replace function public.capstone_section_box_count(p_key text)
returns integer language sql immutable set search_path = public as $$
  select case when public.capstone_section_map(p_key) is null then 5
              else (select count(*)::int from jsonb_object_keys(public.capstone_section_map(p_key))) end;
$$;

-- Check: every section's count equals its map.
select k, public.capstone_section_box_count(k) as boxes, public.capstone_section_map(k)::text as map
  from unnest(array['u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12']) k;
