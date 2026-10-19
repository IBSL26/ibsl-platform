-- S2R Portal · Problem Charter (Unit 1, part 6.2) · 19 October 2026
-- Paste ALL of this into the Supabase SQL Editor and select Run. It runs as one change: all of it or none of it.
-- The last line shows the result. Expected: the list u1 to u12, 11, u1_foundations.

begin;

-- ── Block 1 · Allow the Unit 1 section (drops the old list of allowed sections) ──
alter table public.capstone_blueprint_section drop constraint capstone_blueprint_section_section_key_check;

-- ── Block 2 · The allowed sections, Unit 1 to Unit 12 ──
alter table public.capstone_blueprint_section add constraint capstone_blueprint_section_section_key_check
  check (section_key in ('u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12'));


-- ── Block 3 · Section → unit: u1 is Unit 1 (u1_foundations) ──
create or replace function public.capstone_section_lens(p_key text)
returns text language sql immutable set search_path = public as $$
  select case p_key
    when 'u1'  then 'u1_foundations'
    when 'u2'  then 'u2m1_lens1'  when 'u3'  then 'u2m1_lens2'  when 'u4'  then 'u2m1_lens3'
    when 'u5'  then 'u3m1_lens4'  when 'u6'  then 'u3m1_lens5'  when 'u7'  then 'u3m1_lens6'
    when 'u8'  then 'u3m2_lens7'  when 'u9'  then 'u3m2_lens8'  when 'u10' then 'u4m1_lens9'
    when 'u11' then 'u4m1_lens10' when 'u12' then 'u4m2_lens11'
  end;
$$;

-- ── Block 4 · Box counts: u1 has 11 (1A to 1K); every other unit keeps its live value ──
create or replace function public.capstone_section_box_count(p_key text)
returns integer language sql immutable set search_path = public as $$
  select case p_key when 'u1' then 11 when 'u2' then 6 when 'u3' then 6 when 'u4' then 6 when 'u5' then 3 when 'u7' then 5 when 'u8' then 4 when 'u9' then 5 when 'u10' then 6 when 'u11' then 5 when 'u12' then 5 when 'u6' then 2 else 5 end;
$$;

-- ── Block 5 · Read a team's full Blueprint: the Unit 1 section comes first ──
create or replace function public.get_capstone_blueprint(p_team_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_team capstone_team%rowtype;
  v      jsonb;
begin
  if auth.uid() is null then raise exception 'not authenticated'; end if;
  select * into v_team from capstone_team where id = p_team_id;
  if not found then raise exception 'team not found'; end if;
  if not (is_admin() or exists (select 1 from capstone_individual
                                 where team_id = p_team_id and profile_id = auth.uid())) then
    raise exception 'not authorised';
  end if;

  select jsonb_build_object(
    'team',    jsonb_build_object('id', v_team.id, 'name', v_team.team_name, 'reopened', v_team.blueprint_reopened),
    'cohort',  (select jsonb_build_object('id', c.id, 'name', c.name) from cohorts c where c.id = v_team.cohort_id),
    'brief',   (select to_jsonb(b) - 'updated_by' from capstone_brief b where b.cohort_id = v_team.cohort_id),
    'locked',  capstone_team_locked(p_team_id),
    'members', coalesce((select jsonb_agg(jsonb_build_object('profile_id', p.id, 'full_name', p.full_name) order by p.full_name)
                           from capstone_individual ci join profiles p on p.id = ci.profile_id
                          where ci.team_id = p_team_id), '[]'::jsonb),
    'sections', (select jsonb_agg(jsonb_build_object(
                   'key',             k.key,
                   'open',            capstone_section_open(p_team_id, k.key),
                   'status',          coalesce(s.status, 'draft'),
                   'content',         coalesce(s.content, '{}'::jsonb),
                   'updated_at',      s.updated_at,
                   'updated_by_name', (select full_name from profiles where id = s.updated_by),
                   'sent_at',         s.sent_at,
                   'sent_by_name',    (select full_name from profiles where id = s.sent_by),
                   'agreed_at',       s.agreed_at,
                   'confirmations',   coalesce((select jsonb_agg(jsonb_build_object('profile_id', c2.profile_id, 'confirmed_at', c2.confirmed_at))
                                                  from capstone_blueprint_confirmation c2 where c2.section_id = s.id), '[]'::jsonb)
                 ) order by k.ord)
                   from (values ('u1',1),('u2',2),('u3',3),('u4',4),('u5',5),('u6',6),('u7',7),
                                ('u8',8),('u9',9),('u10',10),('u11',11),('u12',12)) as k(key, ord)
                   left join capstone_blueprint_section s on s.team_id = p_team_id and s.section_key = k.key)
  ) into v;
  return v;
end;
$$;

-- ── Block 6 · The participant's capstone page opens when Unit 1 opens ──
create or replace function public.get_my_capstone(p_cohort_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_uid    uuid := auth.uid();
  v_team   uuid;
  v_status text;
begin
  if v_uid is null then raise exception 'not authenticated'; end if;
  if not exists (select 1 from cohort_memberships
                  where profile_id = v_uid and cohort_id = p_cohort_id and role_in_cohort = 'participant') then
    raise exception 'not authorised';
  end if;
  select status  into v_status from lens_progress
   where profile_id = v_uid and cohort_id = p_cohort_id and lens_id = 'u1_foundations';
  select team_id into v_team from capstone_individual
   where profile_id = v_uid and cohort_id = p_cohort_id limit 1;

  return jsonb_build_object(
    'me',          v_uid,
    'cohort',      (select jsonb_build_object('id', id, 'name', name) from cohorts where id = p_cohort_id),
    'brief',       (select to_jsonb(b) - 'updated_by' from capstone_brief b where b.cohort_id = p_cohort_id),
    'access_open', coalesce(v_status, 'locked') in ('unlocked','in_progress','submitted','reviewed','completed'),
    'blueprint',   case when v_team is null then null else get_capstone_blueprint(v_team) end,
    'score',       get_participant_final_score(v_uid, p_cohort_id),
    'certificate', (select jsonb_build_object('participant_number', participant_number,
                                              'final_score', final_score, 'issued_at', issued_at)
                      from capstone_certificate where profile_id = v_uid and cohort_id = p_cohort_id)
  );
end;
$$;

-- ── Block 7 · The cohort brief no longer needs a case name ──
alter table public.capstone_brief alter column case_name drop not null;

-- ── Block 8 · Admin: save the cohort brief (brief text and dates; case name optional) ──
create or replace function public.admin_set_capstone_brief(
  p_cohort_id uuid, p_case_name text, p_brief_text text,
  p_submission_due timestamptz, p_showcase_at timestamptz, p_showcase_venue text)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'not authorised'; end if;
  insert into capstone_brief (cohort_id, case_name, brief_text, submission_due, showcase_at, showcase_venue, updated_by, updated_at)
  values (p_cohort_id, nullif(btrim(p_case_name), ''), p_brief_text, p_submission_due, p_showcase_at, p_showcase_venue, auth.uid(), now())
  on conflict (cohort_id) do update
     set case_name = coalesce(excluded.case_name, capstone_brief.case_name), brief_text = excluded.brief_text,
         submission_due = excluded.submission_due, showcase_at = excluded.showcase_at,
         showcase_venue = excluded.showcase_venue, updated_by = excluded.updated_by, updated_at = now();
  return jsonb_build_object('ok', true);
end;
$$;

commit;

select (select pg_get_constraintdef(oid) from pg_constraint where conrelid = 'public.capstone_blueprint_section'::regclass and conname = 'capstone_blueprint_section_section_key_check') as section_keys,
       public.capstone_section_box_count('u1') as u1_boxes,
       public.capstone_section_lens('u1') as u1_unit;
