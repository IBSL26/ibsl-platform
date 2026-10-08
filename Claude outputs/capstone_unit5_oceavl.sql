-- ============================================================================
-- S2R Portal — Capstone Blueprint, Unit 5: the team's OCEAVL profile
-- Run in Supabase (project "S2R Portal Production"), SQL editor.
-- Run ONE block at a time, in order. Each block is a single statement.
-- Blocks 1 and 5 only look. Blocks 2, 3 and 4 add one new function.
-- No table, no saved answer and no existing function is changed.
-- ============================================================================

-- ── Block 1 · Check only (changes nothing). The answer must be: jsonb ──
select data_type from information_schema.columns
 where table_schema = 'public' and table_name = 'lens_responses' and column_name = 'value';

-- ── Block 2 · The team's OCEAVL profile: counts of High, Balanced and Low for each dimension.
--    Team members and the admin only. It returns counts, never a name or one member's scores,
--    and it returns the counts only when every member of the team has submitted. ──
create or replace function public.get_capstone_team_oceavl(p_team_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_members integer;
  v_sub     integer;
  v_dims    jsonb;
begin
  if auth.uid() is null then raise exception 'not authenticated'; end if;
  if not (is_admin() or exists (select 1 from capstone_individual
                                 where team_id = p_team_id and profile_id = auth.uid())) then
    raise exception 'not authorised';
  end if;

  select count(*) into v_members from capstone_individual where team_id = p_team_id;

  with sub as (
    select ci.profile_id, w.value -> 's' as s
      from capstone_individual ci
      join lens_responses w on w.profile_id = ci.profile_id and w.lens_id = 'u3m1_lens4' and w.response_key = '__oceavl_work'
      join lens_responses c on c.profile_id = ci.profile_id and c.lens_id = 'u3m1_lens4' and c.response_key = 'confirmed_items'
     where ci.team_id = p_team_id
       and jsonb_typeof(c.value) = 'array'
       and c.value ? 'OCEAVL · My Scores'
       and jsonb_typeof(w.value -> 's') = 'array'
       and jsonb_array_length(w.value -> 's') = 7
  ), per as (
    select d.i,
           count(*) filter (where (sub.s ->> d.i) in ('4', '5')) as hi,
           count(*) filter (where (sub.s ->> d.i) = '3')         as ba,
           count(*) filter (where (sub.s ->> d.i) in ('1', '2')) as lo
      from sub cross join generate_series(0, 6) as d(i)
     group by d.i
  )
  select (select count(*) from sub),
         (select jsonb_agg(jsonb_build_array(hi, ba, lo) order by i) from per)
    into v_sub, v_dims;

  return jsonb_build_object(
    'members',   v_members,
    'submitted', v_sub,
    'dims',      case when v_members > 0 and v_sub = v_members then v_dims else null end);
end;
$$;

-- ── Block 3 · Signed-out visitors cannot call the new function ──
revoke execute on function public.get_capstone_team_oceavl(uuid) from public, anon;

-- ── Block 4 · Signed-in users can call it (the function checks who the caller is) ──
grant execute on function public.get_capstone_team_oceavl(uuid) to authenticated;

-- ── Block 5 · Check only (changes nothing): has any team already saved Unit 5 text in the old boxes? ──
-- If the answer is 0, there is nothing more to do. If it is above 0, tell Claude the number.
select count(*) as teams_with_saved_unit5_text from public.capstone_blueprint_section where section_key = 'u5';
