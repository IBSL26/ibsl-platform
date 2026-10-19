-- ============================================================================
-- S2R Portal · Capstone Blueprint filled from the unit pages (19 October 2026)
-- Participants no longer type on the Capstone page. When every member of a group
-- has agreed its Section 5 work on a unit page, the Capstone page calls this
-- function, which copies the agreed work into that unit's Capstone section and
-- marks the section Agreed for every member.
-- It adds one function. No table and no saved text is changed.
-- ============================================================================

create or replace function public.capstone_sync_section(p_team_id uuid, p_key text, p_map jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid     uuid := auth.uid();
  v_lens    text;
  v_w       team_work%rowtype;
  v_n       integer;
  v_a       integer;
  v_content jsonb := '{}'::jsonb;
  v_box     text;
  v_val     text;
  v_sec     capstone_blueprint_section%rowtype;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'error', 'not_authenticated'); end if;
  if not exists (select 1 from capstone_individual where team_id = p_team_id and profile_id = v_uid) then
    return jsonb_build_object('ok', false, 'error', 'not_authorised');
  end if;
  v_lens := capstone_section_lens(p_key);
  if v_lens is null then return jsonb_build_object('ok', false, 'error', 'invalid_section'); end if;
  if capstone_team_locked(p_team_id) then return jsonb_build_object('ok', false, 'error', 'locked'); end if;
  if not capstone_section_open(p_team_id, p_key) then return jsonb_build_object('ok', false, 'error', 'section_closed'); end if;
  if p_map is null or jsonb_typeof(p_map) <> 'object' then return jsonb_build_object('ok', false, 'error', 'invalid_map'); end if;

  -- The group's record for this unit must be agreed by every current member.
  select * into v_w from team_work where team_id = p_team_id and lens_id = v_lens;
  if not found or v_w.version = 0 then return jsonb_build_object('ok', false, 'error', 'not_agreed'); end if;
  select count(*) into v_n from capstone_individual where team_id = p_team_id;
  select count(*) into v_a from team_work_agreement a
   where a.team_id = p_team_id and a.lens_id = v_lens and a.version = v_w.version
     and exists (select 1 from capstone_individual ci where ci.team_id = p_team_id and ci.profile_id = a.profile_id);
  if v_a <> v_n then return jsonb_build_object('ok', false, 'error', 'not_agreed'); end if;

  -- The text comes from the database, from the agreed record on the caller's unit page.
  for v_box in select jsonb_object_keys(p_map) loop
    v_val := null;
    select case when jsonb_typeof(r.value) = 'string' then r.value #>> '{}' end into v_val
      from lens_responses r
     where r.profile_id = v_uid and r.lens_id = v_lens and r.response_key = p_map ->> v_box;
    if v_val is null or btrim(v_val) = '' then return jsonb_build_object('ok', false, 'error', 'incomplete', 'box', v_box); end if;
    v_content := v_content || jsonb_build_object(v_box, v_val);
  end loop;
  if (select count(*) from jsonb_object_keys(v_content)) < capstone_section_box_count(p_key) then
    return jsonb_build_object('ok', false, 'error', 'incomplete');
  end if;

  select * into v_sec from capstone_blueprint_section where team_id = p_team_id and section_key = p_key for update;
  if found and v_sec.status = 'agreed' and v_sec.content = v_content then
    return jsonb_build_object('ok', true, 'status', 'agreed', 'changed', false);
  end if;
  if found then
    update capstone_blueprint_section
       set content = v_content, status = 'agreed', updated_by = v_uid, updated_at = now(),
           sent_by = v_uid, sent_at = now(), agreed_at = now()
     where id = v_sec.id
     returning * into v_sec;
  else
    insert into capstone_blueprint_section (team_id, section_key, content, status, updated_by, sent_by, sent_at, agreed_at)
    values (p_team_id, p_key, v_content, 'agreed', v_uid, v_uid, now(), now())
    returning * into v_sec;
  end if;
  delete from capstone_blueprint_confirmation where section_id = v_sec.id;
  insert into capstone_blueprint_confirmation (section_id, profile_id)
  select v_sec.id, ci.profile_id from capstone_individual ci where ci.team_id = p_team_id;
  return jsonb_build_object('ok', true, 'status', 'agreed', 'changed', true);
end;
$$;

revoke execute on function public.capstone_sync_section(uuid, text, jsonb) from public, anon;
grant execute on function public.capstone_sync_section(uuid, text, jsonb) to authenticated;

-- Check (changes nothing): the function is there. Expected: one row, capstone_sync_section.
select proname from pg_proc where proname = 'capstone_sync_section';
