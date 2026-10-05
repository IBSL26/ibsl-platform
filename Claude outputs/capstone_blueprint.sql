-- ============================================================================
-- S2R Portal — Capstone: Strategy2Results Blueprint (participant capstone)
-- Run in Supabase (project "S2R Portal Production"), SQL editor.
-- Run ONE block at a time, in order. Each block is a single statement.
-- Nothing here changes existing tables' data, scoring, or existing functions,
-- except Block 27 (a security guard on get_participant_final_score), which
-- you run only if you approve it separately.
-- ============================================================================


-- ── Block 1 · Cohort brief: case, brief text and dates (one row per cohort) ──
create table public.capstone_brief (
  cohort_id      uuid primary key references public.cohorts(id) on delete cascade,
  case_name      text not null,
  brief_text     text,
  submission_due timestamptz,
  showcase_at    timestamptz,
  showcase_venue text,
  updated_by     uuid,
  updated_at     timestamptz not null default now()
);

-- ── Block 2 ──
alter table public.capstone_brief enable row level security;

-- ── Block 3 · Admin reads/writes directly; participants read through get_my_capstone ──
create policy capstone_brief_admin_all on public.capstone_brief
  for all to authenticated using (is_admin()) with check (is_admin());


-- ── Block 4 · Blueprint sections: one row per team per unit section ──
create table public.capstone_blueprint_section (
  id          uuid primary key default gen_random_uuid(),
  team_id     uuid not null references public.capstone_team(id) on delete cascade,
  section_key text not null check (section_key in ('u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12')),
  content     jsonb not null default '{}'::jsonb,
  status      text not null default 'draft' check (status in ('draft','awaiting','agreed')),
  updated_by  uuid references public.profiles(id),
  updated_at  timestamptz not null default now(),
  sent_by     uuid references public.profiles(id),
  sent_at     timestamptz,
  agreed_at   timestamptz,
  unique (team_id, section_key)
);

-- ── Block 5 ──
alter table public.capstone_blueprint_section enable row level security;

-- ── Block 6 ──
create policy capstone_blueprint_section_admin_all on public.capstone_blueprint_section
  for all to authenticated using (is_admin()) with check (is_admin());


-- ── Block 7 · Member confirmations of a section's agreed text ──
create table public.capstone_blueprint_confirmation (
  section_id   uuid not null references public.capstone_blueprint_section(id) on delete cascade,
  profile_id   uuid not null references public.profiles(id) on delete cascade,
  confirmed_at timestamptz not null default now(),
  primary key (section_id, profile_id)
);

-- ── Block 8 ──
alter table public.capstone_blueprint_confirmation enable row level security;

-- ── Block 9 ──
create policy capstone_blueprint_confirmation_admin_all on public.capstone_blueprint_confirmation
  for all to authenticated using (is_admin()) with check (is_admin());


-- ── Block 10 · Admin "reopen after deadline" switch per team ──
alter table public.capstone_team add column blueprint_reopened boolean not null default false;


-- ── Block 11 · Helper: Blueprint section → unit (lens_id in the old numbering) ──
create or replace function public.capstone_section_lens(p_key text)
returns text language sql immutable set search_path = public as $$
  select case p_key
    when 'u2'  then 'u2m1_lens1'  when 'u3'  then 'u2m1_lens2'  when 'u4'  then 'u2m1_lens3'
    when 'u5'  then 'u3m1_lens4'  when 'u6'  then 'u3m1_lens5'  when 'u7'  then 'u3m1_lens6'
    when 'u8'  then 'u3m2_lens7'  when 'u9'  then 'u3m2_lens8'  when 'u10' then 'u4m1_lens9'
    when 'u11' then 'u4m1_lens10' when 'u12' then 'u4m2_lens11'
  end;
$$;

-- ── Block 12 · Helper: number of boxes in each section (Unit 2: 6 since the 5 Oct 2026 rebuild; see capstone_unit2_boxes.sql) ──
create or replace function public.capstone_section_box_count(p_key text)
returns integer language sql immutable set search_path = public as $$
  select case p_key when 'u2' then 6 when 'u3' then 6 when 'u4' then 6 when 'u10' then 6 else 5 end;
$$;

-- ── Block 13 · Helper: a section opens when EVERY team member has completed its unit ──
create or replace function public.capstone_section_open(p_team_id uuid, p_key text)
returns boolean language sql stable set search_path = public as $$
  select exists (select 1 from capstone_individual where team_id = p_team_id)
     and not exists (
       select 1
         from capstone_individual ci
         left join lens_progress lp
           on lp.profile_id = ci.profile_id
          and lp.cohort_id  = ci.cohort_id
          and lp.lens_id    = capstone_section_lens(p_key)
        where ci.team_id = p_team_id
          and coalesce(lp.status, 'locked') <> 'completed');
$$;

-- ── Block 14 · Helper: Blueprint is read-only after the deadline unless the admin reopened it ──
create or replace function public.capstone_team_locked(p_team_id uuid)
returns boolean language sql stable set search_path = public as $$
  select coalesce((
    select (not t.blueprint_reopened) and b.submission_due is not null and now() > b.submission_due
      from capstone_team t
      left join capstone_brief b on b.cohort_id = t.cohort_id
     where t.id = p_team_id), false);
$$;

-- ── Block 15 · Helper: mark a section Agreed once every current member has confirmed ──
create or replace function public.capstone_finalise_if_agreed(p_section_id uuid, p_team_id uuid)
returns void language sql set search_path = public as $$
  update capstone_blueprint_section s
     set status = 'agreed', agreed_at = now()
   where s.id = p_section_id
     and s.status = 'awaiting'
     and not exists (
       select 1 from capstone_individual ci
        where ci.team_id = p_team_id
          and not exists (select 1 from capstone_blueprint_confirmation c
                           where c.section_id = p_section_id and c.profile_id = ci.profile_id));
$$;


-- ── Block 16 · Read a team's full Blueprint (team members and admin only) ──
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
                   from (values ('u2',2),('u3',3),('u4',4),('u5',5),('u6',6),('u7',7),
                                ('u8',8),('u9',9),('u10',10),('u11',11),('u12',12)) as k(key, ord)
                   left join capstone_blueprint_section s on s.team_id = p_team_id and s.section_key = k.key)
  ) into v;
  return v;
end;
$$;

-- ── Block 17 · Everything the participant's capstone page needs, in one call ──
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
   where profile_id = v_uid and cohort_id = p_cohort_id and lens_id = 'u2m1_lens1';
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

-- ── Block 18 · Save a section's draft text (any team member, Draft only) ──
create or replace function public.capstone_save_section(
  p_team_id uuid, p_key text, p_content jsonb, p_expected_updated_at timestamptz default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid uuid := auth.uid();
  v_sec capstone_blueprint_section%rowtype;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'error', 'not_authenticated'); end if;
  if not exists (select 1 from capstone_individual where team_id = p_team_id and profile_id = v_uid) then
    return jsonb_build_object('ok', false, 'error', 'not_authorised');
  end if;
  if capstone_section_lens(p_key) is null then return jsonb_build_object('ok', false, 'error', 'invalid_section'); end if;
  if capstone_team_locked(p_team_id) then return jsonb_build_object('ok', false, 'error', 'locked'); end if;
  if not capstone_section_open(p_team_id, p_key) then return jsonb_build_object('ok', false, 'error', 'section_closed'); end if;
  if p_content is null or jsonb_typeof(p_content) <> 'object' then
    return jsonb_build_object('ok', false, 'error', 'invalid_content');
  end if;

  select * into v_sec from capstone_blueprint_section
   where team_id = p_team_id and section_key = p_key for update;
  if found then
    if v_sec.status <> 'draft' then
      return jsonb_build_object('ok', false, 'error', 'not_draft', 'status', v_sec.status);
    end if;
    if p_expected_updated_at is distinct from v_sec.updated_at then
      return jsonb_build_object('ok', false, 'error', 'stale', 'updated_at', v_sec.updated_at,
                                'updated_by_name', (select full_name from profiles where id = v_sec.updated_by));
    end if;
    update capstone_blueprint_section
       set content = p_content, updated_by = v_uid, updated_at = now()
     where id = v_sec.id
     returning * into v_sec;
  else
    insert into capstone_blueprint_section (team_id, section_key, content, updated_by)
    values (p_team_id, p_key, p_content, v_uid)
    returning * into v_sec;
  end if;
  return jsonb_build_object('ok', true, 'updated_at', v_sec.updated_at);
end;
$$;

-- ── Block 19 · Send a complete Draft for team confirmation (sender's confirmation is recorded) ──
create or replace function public.capstone_send_for_confirmation(p_team_id uuid, p_key text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid    uuid := auth.uid();
  v_sec    capstone_blueprint_section%rowtype;
  v_filled int;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'error', 'not_authenticated'); end if;
  if not exists (select 1 from capstone_individual where team_id = p_team_id and profile_id = v_uid) then
    return jsonb_build_object('ok', false, 'error', 'not_authorised');
  end if;
  if capstone_team_locked(p_team_id) then return jsonb_build_object('ok', false, 'error', 'locked'); end if;
  if not capstone_section_open(p_team_id, p_key) then return jsonb_build_object('ok', false, 'error', 'section_closed'); end if;

  select * into v_sec from capstone_blueprint_section
   where team_id = p_team_id and section_key = p_key for update;
  if not found or v_sec.status <> 'draft' then return jsonb_build_object('ok', false, 'error', 'not_draft'); end if;

  select count(*) into v_filled from jsonb_each_text(v_sec.content) e where btrim(e.value) <> '';
  if v_filled < capstone_section_box_count(p_key) then
    return jsonb_build_object('ok', false, 'error', 'incomplete');
  end if;

  delete from capstone_blueprint_confirmation where section_id = v_sec.id;
  update capstone_blueprint_section set status = 'awaiting', sent_by = v_uid, sent_at = now() where id = v_sec.id;
  insert into capstone_blueprint_confirmation (section_id, profile_id) values (v_sec.id, v_uid);
  perform capstone_finalise_if_agreed(v_sec.id, p_team_id);
  return jsonb_build_object('ok', true,
                            'status', (select status from capstone_blueprint_section where id = v_sec.id));
end;
$$;

-- ── Block 20 · Confirm "this is our agreed text" (each member once) ──
create or replace function public.capstone_confirm_section(p_team_id uuid, p_key text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid uuid := auth.uid();
  v_sec capstone_blueprint_section%rowtype;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'error', 'not_authenticated'); end if;
  if not exists (select 1 from capstone_individual where team_id = p_team_id and profile_id = v_uid) then
    return jsonb_build_object('ok', false, 'error', 'not_authorised');
  end if;
  if capstone_team_locked(p_team_id) then return jsonb_build_object('ok', false, 'error', 'locked'); end if;

  select * into v_sec from capstone_blueprint_section
   where team_id = p_team_id and section_key = p_key for update;
  if not found or v_sec.status <> 'awaiting' then return jsonb_build_object('ok', false, 'error', 'not_awaiting'); end if;

  insert into capstone_blueprint_confirmation (section_id, profile_id)
  values (v_sec.id, v_uid) on conflict do nothing;
  perform capstone_finalise_if_agreed(v_sec.id, p_team_id);
  return jsonb_build_object('ok', true,
                            'status', (select status from capstone_blueprint_section where id = v_sec.id));
end;
$$;

-- ── Block 21 · "Request a change": back to Draft, all confirmations cleared ──
create or replace function public.capstone_request_change(p_team_id uuid, p_key text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid uuid := auth.uid();
  v_sec capstone_blueprint_section%rowtype;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'error', 'not_authenticated'); end if;
  if not exists (select 1 from capstone_individual where team_id = p_team_id and profile_id = v_uid) then
    return jsonb_build_object('ok', false, 'error', 'not_authorised');
  end if;
  if capstone_team_locked(p_team_id) then return jsonb_build_object('ok', false, 'error', 'locked'); end if;

  select * into v_sec from capstone_blueprint_section
   where team_id = p_team_id and section_key = p_key for update;
  if not found or v_sec.status <> 'awaiting' then return jsonb_build_object('ok', false, 'error', 'not_awaiting'); end if;

  delete from capstone_blueprint_confirmation where section_id = v_sec.id;
  update capstone_blueprint_section set status = 'draft', sent_by = null, sent_at = null where id = v_sec.id;
  return jsonb_build_object('ok', true, 'status', 'draft');
end;
$$;

-- ── Block 22 · Admin: save the cohort brief (case, brief text, dates) ──
create or replace function public.admin_set_capstone_brief(
  p_cohort_id uuid, p_case_name text, p_brief_text text,
  p_submission_due timestamptz, p_showcase_at timestamptz, p_showcase_venue text)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'not authorised'; end if;
  if coalesce(btrim(p_case_name), '') = '' then raise exception 'case name required'; end if;
  insert into capstone_brief (cohort_id, case_name, brief_text, submission_due, showcase_at, showcase_venue, updated_by, updated_at)
  values (p_cohort_id, btrim(p_case_name), p_brief_text, p_submission_due, p_showcase_at, p_showcase_venue, auth.uid(), now())
  on conflict (cohort_id) do update
     set case_name = excluded.case_name, brief_text = excluded.brief_text,
         submission_due = excluded.submission_due, showcase_at = excluded.showcase_at,
         showcase_venue = excluded.showcase_venue, updated_by = excluded.updated_by, updated_at = now();
  return jsonb_build_object('ok', true);
end;
$$;

-- ── Block 23 · Admin: reopen one section (back to Draft, confirmations cleared) ──
create or replace function public.admin_reopen_capstone_section(p_team_id uuid, p_key text)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'not authorised'; end if;
  delete from capstone_blueprint_confirmation
   where section_id in (select id from capstone_blueprint_section where team_id = p_team_id and section_key = p_key);
  update capstone_blueprint_section
     set status = 'draft', sent_by = null, sent_at = null, agreed_at = null
   where team_id = p_team_id and section_key = p_key;
  return jsonb_build_object('ok', true);
end;
$$;

-- ── Block 24 · Admin: reopen / relock a team's whole Blueprint after the deadline ──
create or replace function public.admin_set_blueprint_reopened(p_team_id uuid, p_reopened boolean)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'not authorised'; end if;
  update capstone_team set blueprint_reopened = coalesce(p_reopened, false), updated_at = now() where id = p_team_id;
  return jsonb_build_object('ok', true);
end;
$$;


-- ── Block 25 · Signed-out visitors cannot call the new functions ──
revoke execute on function
  public.get_capstone_blueprint(uuid),
  public.get_my_capstone(uuid),
  public.capstone_save_section(uuid, text, jsonb, timestamptz),
  public.capstone_send_for_confirmation(uuid, text),
  public.capstone_confirm_section(uuid, text),
  public.capstone_request_change(uuid, text),
  public.admin_set_capstone_brief(uuid, text, text, timestamptz, timestamptz, text),
  public.admin_reopen_capstone_section(uuid, text),
  public.admin_set_blueprint_reopened(uuid, boolean)
from public, anon;

-- ── Block 26 · Signed-in users can call them (each function checks who the caller is) ──
grant execute on function
  public.get_capstone_blueprint(uuid),
  public.get_my_capstone(uuid),
  public.capstone_save_section(uuid, text, jsonb, timestamptz),
  public.capstone_send_for_confirmation(uuid, text),
  public.capstone_confirm_section(uuid, text),
  public.capstone_request_change(uuid, text),
  public.admin_set_capstone_brief(uuid, text, text, timestamptz, timestamptz, text),
  public.admin_reopen_capstone_section(uuid, text),
  public.admin_set_blueprint_reopened(uuid, boolean)
to authenticated;


-- ============================================================================
-- Block 27 · RUN ONLY IF APPROVED SEPARATELY — security guard on scores.
-- The live get_participant_final_score runs with elevated rights and has no
-- caller check: any signed-in user who knows another participant's ID can
-- read that participant's scores. This adds one WHERE clause so only the
-- participant, an admin, or a facilitator of that cohort gets a result.
-- The calculation itself is unchanged, character for character.
-- ============================================================================
CREATE OR REPLACE FUNCTION public.get_participant_final_score(p_profile_id uuid, p_cohort_id uuid)
 RETURNS jsonb
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
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
    (SELECT capstone FROM cap) AS capstone
)
SELECT jsonb_build_object(
  'unit2_avg',           u2,
  'unit3_avg',           u3,
  'unit4_avg',           u4,
  'capstone_avg',        capstone,
  'capstone_pending',    (capstone IS NULL),
  'final_pct', round(
       COALESCE(u2, 0) * 0.25
     + COALESCE(u3, 0) * 0.25
     + COALESCE(u4, 0) * 0.25
     + COALESCE(capstone, 0) * 0.25
  , 2),
  'certified', (
       capstone IS NOT NULL
   AND round(
         COALESCE(u2, 0) * 0.25
       + COALESCE(u3, 0) * 0.25
       + COALESCE(u4, 0) * 0.25
       + COALESCE(capstone, 0) * 0.25
       , 2) >= 80
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
