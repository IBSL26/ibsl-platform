-- ============================================================================
-- S2R Portal — Shared group record (19 October 2026)
-- Group work: the group chooses a scribe for each unit's group work; the scribe's
-- entries go onto every member's page; each member selects Agree; when every
-- member has agreed, the work goes into the Capstone Blueprint.
-- Run in Supabase ("S2R Portal Production"), SQL Editor. Tested in a stand-in
-- database (20 of 20 checks). Adds two tables and five functions. No existing
-- table, saved answer or function is changed.
-- Block 1 (read-only) was run by Claude on 19 Oct: lens_responses has the unique
-- key (profile_id, lens_id, response_key); capstone_individual has team_id,
-- profile_id, cohort_id; no team_work table yet.
-- ============================================================================
begin;
-- ── Block 2 · The shared group record for each team and unit: who the scribe is, the record's version and its Capstone names ──
create table public.team_work (
  team_id    uuid not null references public.capstone_team(id) on delete cascade,
  lens_id    text not null,
  scribe_id  uuid references public.profiles(id),
  names      jsonb not null default '[]'::jsonb,
  version    integer not null default 0,
  updated_by uuid references public.profiles(id),
  updated_at timestamptz not null default now(),
  primary key (team_id, lens_id)
);

-- ── Block 3 ──
alter table public.team_work enable row level security;

-- ── Block 4 · Each member's agreement to the group record ──
create table public.team_work_agreement (
  team_id    uuid not null,
  lens_id    text not null,
  profile_id uuid not null references public.profiles(id) on delete cascade,
  version    integer not null,
  agreed_at  timestamptz not null default now(),
  primary key (team_id, lens_id, profile_id),
  foreign key (team_id, lens_id) references public.team_work(team_id, lens_id) on delete cascade
);

-- ── Block 5 ──
alter table public.team_work_agreement enable row level security;

-- ── Block 6 · Helper: the caller's team in a cohort ──
create or replace function public.team_work_my_team(p_cohort_id uuid)
returns uuid language sql stable security definer set search_path = public as $$
  select team_id from capstone_individual
   where profile_id = auth.uid() and cohort_id = p_cohort_id
   limit 1;
$$;

-- ── Block 7 · What a member's page needs: team, members, scribe, version, who has agreed ──
create or replace function public.team_work_status(p_cohort_id uuid, p_lens_id text)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_uid  uuid := auth.uid();
  v_team uuid;
  v_w    team_work%rowtype;
  v_n    integer;
  v_a    integer;
begin
  if v_uid is null then raise exception 'not authenticated'; end if;
  v_team := team_work_my_team(p_cohort_id);
  if v_team is null then return jsonb_build_object('team_id', null, 'me', v_uid); end if;
  select * into v_w from team_work where team_id = v_team and lens_id = p_lens_id;
  select count(*) into v_n from capstone_individual where team_id = v_team;
  select count(*) into v_a from team_work_agreement a
   where a.team_id = v_team and a.lens_id = p_lens_id and a.version = coalesce(v_w.version, 0)
     and exists (select 1 from capstone_individual ci where ci.team_id = v_team and ci.profile_id = a.profile_id);
  return jsonb_build_object(
    'team_id',    v_team,
    'team_name',  (select team_name from capstone_team where id = v_team),
    'me',         v_uid,
    'scribe_id',  v_w.scribe_id,
    'version',    coalesce(v_w.version, 0),
    'names',      coalesce(v_w.names, '[]'::jsonb),
    'updated_at', v_w.updated_at,
    'all_agreed', v_n > 0 and v_a = v_n and coalesce(v_w.version, 0) > 0,
    'members',    coalesce((select jsonb_agg(jsonb_build_object(
                     'profile_id', p.id,
                     'full_name',  p.full_name,
                     'agreed',     exists (select 1 from team_work_agreement a
                                            where a.team_id = v_team and a.lens_id = p_lens_id
                                              and a.profile_id = p.id and a.version = coalesce(v_w.version, 0)))
                     order by p.full_name)
                    from capstone_individual ci join profiles p on p.id = ci.profile_id
                   where ci.team_id = v_team), '[]'::jsonb));
end;
$$;

-- ── Block 8 · Choose the scribe for this unit's group work (any member, any member of the team) ──
create or replace function public.team_work_set_scribe(p_cohort_id uuid, p_lens_id text, p_scribe_id uuid)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_team uuid;
begin
  if auth.uid() is null then raise exception 'not authenticated'; end if;
  v_team := team_work_my_team(p_cohort_id);
  if v_team is null then return jsonb_build_object('ok', false, 'error', 'no_team'); end if;
  if not exists (select 1 from capstone_individual where team_id = v_team and profile_id = p_scribe_id) then
    return jsonb_build_object('ok', false, 'error', 'not_member');
  end if;
  insert into team_work (team_id, lens_id, scribe_id, updated_by, updated_at)
  values (v_team, p_lens_id, p_scribe_id, auth.uid(), now())
  on conflict (team_id, lens_id) do update set scribe_id = excluded.scribe_id;
  return jsonb_build_object('ok', true);
end;
$$;

-- ── Block 9 · The scribe saves: the entries go onto every member's page, agreements clear ──
create or replace function public.team_work_write(p_cohort_id uuid, p_lens_id text, p_items jsonb, p_names jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid  uuid := auth.uid();
  v_team uuid;
  v_w    team_work%rowtype;
  v_drop jsonb;
  k      text;
  m      record;
begin
  if v_uid is null then raise exception 'not authenticated'; end if;
  if jsonb_typeof(p_items) <> 'object' or jsonb_typeof(p_names) <> 'array' then
    return jsonb_build_object('ok', false, 'error', 'bad_input');
  end if;
  if p_items ? 'confirmed_items' then return jsonb_build_object('ok', false, 'error', 'bad_input'); end if;
  v_team := team_work_my_team(p_cohort_id);
  if v_team is null then return jsonb_build_object('ok', false, 'error', 'no_team'); end if;
  select * into v_w from team_work where team_id = v_team and lens_id = p_lens_id for update;
  if not found or v_w.scribe_id is distinct from v_uid then
    return jsonb_build_object('ok', false, 'error', 'not_scribe');
  end if;

  v_drop := coalesce(v_w.names, '[]'::jsonb) || p_names;

  for m in select ci.profile_id from capstone_individual ci where ci.team_id = v_team loop
    for k in select jsonb_object_keys(p_items) loop
      insert into lens_responses (profile_id, cohort_id, lens_id, response_key, value, updated_at)
      values (m.profile_id, p_cohort_id, p_lens_id, k, p_items -> k, now())
      on conflict (profile_id, lens_id, response_key)
      do update set value = excluded.value, updated_at = excluded.updated_at;
    end loop;
    update lens_responses r
       set value = coalesce((select jsonb_agg(e) from jsonb_array_elements(r.value) e
                              where not (v_drop @> jsonb_build_array(e))), '[]'::jsonb),
           updated_at = now()
     where r.profile_id = m.profile_id and r.lens_id = p_lens_id and r.response_key = 'confirmed_items'
       and jsonb_typeof(r.value) = 'array';
  end loop;

  update team_work
     set version = v_w.version + 1, names = p_names, updated_by = v_uid, updated_at = now()
   where team_id = v_team and lens_id = p_lens_id;
  delete from team_work_agreement where team_id = v_team and lens_id = p_lens_id;
  return jsonb_build_object('ok', true, 'version', v_w.version + 1);
end;
$$;

-- ── Block 10 · A member agrees; when every member has agreed, the names go into every member's confirmed list ──
create or replace function public.team_work_agree(p_cohort_id uuid, p_lens_id text, p_version integer)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_uid  uuid := auth.uid();
  v_team uuid;
  v_w    team_work%rowtype;
  v_n    integer;
  v_a    integer;
  m      record;
begin
  if v_uid is null then raise exception 'not authenticated'; end if;
  v_team := team_work_my_team(p_cohort_id);
  if v_team is null then return jsonb_build_object('ok', false, 'error', 'no_team'); end if;
  select * into v_w from team_work where team_id = v_team and lens_id = p_lens_id for update;
  if not found or v_w.version = 0 then return jsonb_build_object('ok', false, 'error', 'nothing_to_agree'); end if;
  if v_w.version <> p_version then return jsonb_build_object('ok', false, 'error', 'changed'); end if;

  insert into team_work_agreement (team_id, lens_id, profile_id, version)
  values (v_team, p_lens_id, v_uid, v_w.version)
  on conflict (team_id, lens_id, profile_id) do update set version = excluded.version, agreed_at = now();

  select count(*) into v_n from capstone_individual where team_id = v_team;
  select count(*) into v_a from team_work_agreement a
   where a.team_id = v_team and a.lens_id = p_lens_id and a.version = v_w.version
     and exists (select 1 from capstone_individual ci where ci.team_id = v_team and ci.profile_id = a.profile_id);

  if v_a = v_n then
    for m in select ci.profile_id from capstone_individual ci where ci.team_id = v_team loop
      insert into lens_responses (profile_id, cohort_id, lens_id, response_key, value, updated_at)
      values (m.profile_id, p_cohort_id, p_lens_id, 'confirmed_items', v_w.names, now())
      on conflict (profile_id, lens_id, response_key)
      do update set value = (select coalesce(jsonb_agg(distinct e), '[]'::jsonb)
                               from jsonb_array_elements(
                                 case when jsonb_typeof(lens_responses.value) = 'array'
                                      then lens_responses.value else '[]'::jsonb end || v_w.names) e),
                    updated_at = now();
    end loop;
  end if;
  return jsonb_build_object('ok', true, 'all_agreed', v_a = v_n);
end;
$$;

-- ── Block 11 · Signed-out visitors cannot call the new functions ──
revoke execute on function public.team_work_my_team(uuid), public.team_work_status(uuid, text),
  public.team_work_set_scribe(uuid, text, uuid), public.team_work_write(uuid, text, jsonb, jsonb),
  public.team_work_agree(uuid, text, integer) from public, anon;

-- ── Block 12 · Signed-in users can call them (each function checks who the caller is) ──
grant execute on function public.team_work_my_team(uuid), public.team_work_status(uuid, text),
  public.team_work_set_scribe(uuid, text, uuid), public.team_work_write(uuid, text, jsonb, jsonb),
  public.team_work_agree(uuid, text, integer) to authenticated;

commit;
