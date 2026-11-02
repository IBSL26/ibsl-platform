-- Participant profiles (2 Nov 2026): bio, position in the simulated executive team, passport photo.
-- Run in the Supabase SQL editor ("S2R Portal Production"). Safe to run again.
-- Changes no existing table or function. Stops with a clear message if the portal's tables differ from what it expects.

begin;

do $$
declare v_missing text;
begin
  select string_agg(x.t || '.' || x.c, ', ') into v_missing
  from (values ('profiles','full_name'),('profiles','role'),
               ('cohort_memberships','cohort_id'),('cohort_memberships','profile_id'),
               ('cohort_memberships','role_in_cohort'),('cohort_memberships','joined_at'),
               ('capstone_individual','team_id'),('capstone_individual','profile_id'),('capstone_individual','cohort_id'),
               ('capstone_team','id'),('capstone_team','team_name'),
               ('lens_responses','profile_id'),('lens_responses','lens_id'),('lens_responses','response_key'),('lens_responses','value'),
               ('team_work','team_id'),('team_work','lens_id'),('team_work','version')) as x(t, c)
  where not exists (select 1 from information_schema.columns ic
                    where ic.table_schema = 'public' and ic.table_name = x.t and ic.column_name = x.c);
  if v_missing is not null then
    raise exception 'Nothing was changed. Missing columns: %', v_missing;
  end if;
end $$;

create table if not exists public.participant_profiles (
  profile_id uuid primary key references public.profiles(id) on delete cascade,
  bio        text,
  exec_role  text,
  photo_path text,
  updated_at timestamptz not null default now()
);
alter table public.participant_profiles enable row level security;
revoke all on table public.participant_profiles from public, anon, authenticated;

-- Private photo storage: JPEG only, 1 MB at most.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('participant_photos', 'participant_photos', false, 1048576, array['image/jpeg'])
on conflict (id) do update set public = false, file_size_limit = 1048576, allowed_mime_types = array['image/jpeg'];

-- The person's latest cohort, as the portal home uses it.
create or replace function public.participant_cohort(p_uid uuid)
returns uuid language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select cm.cohort_id from public.cohort_memberships cm
  where cm.profile_id = p_uid order by cm.joined_at desc nulls last limit 1;
$function$;

create or replace function public.participant_team(p_uid uuid)
returns uuid language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select ci.team_id from public.capstone_individual ci
  where ci.profile_id = p_uid and ci.cohort_id = public.participant_cohort(p_uid) limit 1;
$function$;

-- The executive team rows in the group's Problem Charter (Unit 1 Part 6.2).
create or replace function public.participant_charter_roles(p_uid uuid)
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
declare
  v jsonb;
begin
  select r.value into v from public.lens_responses r
  where r.profile_id = p_uid and r.lens_id = 'u1_foundations' and r.response_key = '__pc_work';
  if v is null then return '[]'::jsonb; end if;
  if jsonb_typeof(v) = 'string' then
    begin v := (v #>> '{}')::jsonb; exception when others then return '[]'::jsonb; end;
  end if;
  if jsonb_typeof(v) <> 'object' or jsonb_typeof(v -> 'team') is distinct from 'array' then return '[]'::jsonb; end if;
  return coalesce((select jsonb_agg(jsonb_build_object('role', btrim(e ->> 'role'), 'name', btrim(coalesce(e ->> 'name', ''))) order by o)
                   from jsonb_array_elements(v -> 'team') with ordinality as t(e, o)
                   where btrim(coalesce(e ->> 'role', '')) <> ''), '[]'::jsonb);
end;
$function$;

-- Has every member agreed the Charter's executive team?
create or replace function public.participant_charter_ready(p_uid uuid)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select exists (select 1 from public.lens_responses r
                 where r.profile_id = p_uid and r.lens_id = 'u1_foundations' and r.response_key = 'confirmed_items'
                   and jsonb_typeof(r.value) = 'array'
                   and r.value @> '["Problem Charter · Executive Team"]'::jsonb);
$function$;

-- Positions close when the group starts its Capstone work after the Charter.
create or replace function public.participant_role_locked(p_team uuid)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select exists (select 1 from public.team_work w
                 where w.team_id = p_team and w.lens_id <> 'u1_foundations' and w.version > 0);
$function$;

-- Who may see a profile or photo: the person, their group, their facilitators, the admin.
create or replace function public.participant_visible(p_owner uuid)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select p_owner = auth.uid()
      or public.is_admin()
      or exists (select 1 from public.capstone_individual a
                 join public.capstone_individual b on b.team_id = a.team_id
                 where a.profile_id = auth.uid() and b.profile_id = p_owner)
      or exists (select 1 from public.cohort_memberships f
                 join public.cohort_memberships m on m.cohort_id = f.cohort_id
                 where f.profile_id = auth.uid() and f.role_in_cohort::text = 'facilitator'
                   and m.profile_id = p_owner);
$function$;

create or replace function public.participant_photo_readable(p_folder text)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select case when p_folder ~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
              then public.participant_visible(p_folder::uuid) else false end;
$function$;

-- What the profile page needs.
create or replace function public.get_my_participant_profile()
returns jsonb language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
declare
  v_uid   uuid := auth.uid();
  v_role  text;
  v_name  text;
  v_team  uuid;
  v_me    public.participant_profiles%rowtype;
  v_ready boolean;
begin
  select p.role::text, p.full_name into v_role, v_name from public.profiles p where p.id = v_uid;
  if v_role is distinct from 'participant' then return jsonb_build_object('required', false); end if;
  select * into v_me from public.participant_profiles where profile_id = v_uid;
  v_team  := public.participant_team(v_uid);
  v_ready := v_team is not null and public.participant_charter_ready(v_uid);
  return jsonb_build_object(
    'required',      true,
    'full_name',     v_name,
    'bio',           v_me.bio,
    'exec_role',     v_me.exec_role,
    'photo_path',    v_me.photo_path,
    'team_name',     (select t.team_name from public.capstone_team t where t.id = v_team),
    'charter_ready', v_ready,
    'role_locked',   v_team is not null and public.participant_role_locked(v_team),
    'roles',         case when v_ready then coalesce((
                       select jsonb_agg(jsonb_build_object('role', e ->> 'role', 'name', e ->> 'name', 'taken_by',
                         (select p.full_name from public.participant_profiles pp
                          join public.capstone_individual ci on ci.profile_id = pp.profile_id and ci.team_id = v_team
                          join public.profiles p on p.id = pp.profile_id
                          where lower(pp.exec_role) = lower(e ->> 'role') and pp.profile_id <> v_uid limit 1)))
                       from jsonb_array_elements(public.participant_charter_roles(v_uid)) e), '[]'::jsonb)
                     else '[]'::jsonb end,
    'members',       coalesce((
                       select jsonb_agg(jsonb_build_object('profile_id', p.id, 'full_name', p.full_name, 'bio', pp.bio,
                                        'exec_role', pp.exec_role, 'photo_path', pp.photo_path) order by p.full_name)
                       from public.capstone_individual ci
                       join public.profiles p on p.id = ci.profile_id
                       left join public.participant_profiles pp on pp.profile_id = p.id
                       where ci.team_id = v_team and ci.profile_id <> v_uid), '[]'::jsonb));
end;
$function$;

-- Save. Each field is optional; an empty position or photo leaves the saved one in place.
create or replace function public.save_my_participant_profile(p_bio text, p_exec_role text, p_photo_path text)
returns jsonb language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
declare
  v_uid   uuid := auth.uid();
  v_bio   text := nullif(btrim(coalesce(p_bio, '')), '');
  v_ask   text := nullif(btrim(coalesce(p_exec_role, '')), '');
  v_photo text := nullif(btrim(coalesce(p_photo_path, '')), '');
  v_team  uuid;
  v_me    public.participant_profiles%rowtype;
  v_role  text;
begin
  if not exists (select 1 from public.profiles p where p.id = v_uid and p.role::text = 'participant') then
    return jsonb_build_object('ok', false, 'error', 'not_participant');
  end if;
  if v_bio is not null and (length(v_bio) > 2000
     or coalesce(array_length(regexp_split_to_array(v_bio, '\s+'), 1), 0) > 150) then
    return jsonb_build_object('ok', false, 'error', 'bio_long');
  end if;
  if v_photo is not null and v_photo !~ ('^' || v_uid::text || '/[0-9]+\.jpg$') then
    return jsonb_build_object('ok', false, 'error', 'bad_photo');
  end if;
  select * into v_me from public.participant_profiles where profile_id = v_uid;
  v_role := v_me.exec_role;

  if v_ask is not null and lower(v_ask) is distinct from lower(v_me.exec_role) then
    v_team := public.participant_team(v_uid);
    if v_team is null or not public.participant_charter_ready(v_uid) then
      return jsonb_build_object('ok', false, 'error', 'charter_open');
    end if;
    perform 1 from public.capstone_team t where t.id = v_team for update;   -- one position change at a time per group
    if public.participant_role_locked(v_team) then
      return jsonb_build_object('ok', false, 'error', 'role_locked');
    end if;
    select e ->> 'role' into v_role from jsonb_array_elements(public.participant_charter_roles(v_uid)) e
    where lower(e ->> 'role') = lower(v_ask) limit 1;
    if v_role is null then return jsonb_build_object('ok', false, 'error', 'role_not_in_charter'); end if;
    if exists (select 1 from public.participant_profiles pp
               join public.capstone_individual ci on ci.profile_id = pp.profile_id and ci.team_id = v_team
               where lower(pp.exec_role) = lower(v_role) and pp.profile_id <> v_uid) then
      return jsonb_build_object('ok', false, 'error', 'role_taken');
    end if;
  end if;

  insert into public.participant_profiles (profile_id, bio, exec_role, photo_path, updated_at)
  values (v_uid, v_bio, v_role, v_photo, now())
  on conflict (profile_id) do update
    set bio = excluded.bio, exec_role = excluded.exec_role,
        photo_path = coalesce(excluded.photo_path, public.participant_profiles.photo_path), updated_at = now();
  return jsonb_build_object('ok', true, 'old_photo_path',
    case when v_photo is not null and v_me.photo_path is distinct from v_photo then v_me.photo_path end);
end;
$function$;

-- A cohort's profiles, for its facilitators and the admin.
create or replace function public.get_cohort_participant_profiles(p_cohort_id uuid)
returns table (profile_id uuid, full_name text, team_name text, exec_role text, bio text, photo_path text, updated_at timestamptz)
language plpgsql stable security definer set search_path to 'public', 'pg_temp' as $function$
begin
  if not public.is_admin() and not exists (
    select 1 from public.cohort_memberships cm
    where cm.cohort_id = p_cohort_id and cm.profile_id = auth.uid() and cm.role_in_cohort::text = 'facilitator'
  ) then
    raise exception 'Access denied' using errcode = '42501';
  end if;
  return query
  select p.id, p.full_name::text, t.team_name::text, pp.exec_role, pp.bio, pp.photo_path, pp.updated_at
  from public.cohort_memberships cm
  join public.profiles p on p.id = cm.profile_id
  left join public.capstone_individual ci on ci.profile_id = p.id and ci.cohort_id = p_cohort_id
  left join public.capstone_team t on t.id = ci.team_id
  left join public.participant_profiles pp on pp.profile_id = p.id
  where cm.cohort_id = p_cohort_id and cm.role_in_cohort::text = 'participant'
  order by t.team_name nulls last, lower(coalesce(p.full_name, ''));
end;
$function$;

revoke all on function public.participant_cohort(uuid), public.participant_team(uuid),
  public.participant_charter_roles(uuid), public.participant_charter_ready(uuid),
  public.participant_role_locked(uuid), public.participant_visible(uuid) from public, anon, authenticated;
revoke all on function public.participant_photo_readable(text), public.get_my_participant_profile(),
  public.save_my_participant_profile(text, text, text), public.get_cohort_participant_profiles(uuid) from public, anon;
grant execute on function public.participant_photo_readable(text), public.get_my_participant_profile(),
  public.save_my_participant_profile(text, text, text), public.get_cohort_participant_profiles(uuid) to authenticated;

drop policy if exists "participant_photos_read" on storage.objects;
create policy "participant_photos_read" on storage.objects for select to authenticated
  using (bucket_id = 'participant_photos' and public.participant_photo_readable((storage.foldername(name))[1]));
drop policy if exists "participant_photos_add" on storage.objects;
create policy "participant_photos_add" on storage.objects for insert to authenticated
  with check (bucket_id = 'participant_photos' and (storage.foldername(name))[1] = auth.uid()::text);
drop policy if exists "participant_photos_remove" on storage.objects;
create policy "participant_photos_remove" on storage.objects for delete to authenticated
  using (bucket_id = 'participant_photos' and (storage.foldername(name))[1] = auth.uid()::text);

commit;

select 'participant profiles ready' as result, (select count(*) from public.participant_profiles) as profiles;
