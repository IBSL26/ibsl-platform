-- 19 Nov 2026 (Carol): CESI Executive Roles can be changed by the participant and by the admin at any time.
-- 1. The role no longer closes when a group begins its Capstone work (used only by the profile page functions).
create or replace function public.participant_role_locked(p_team uuid)
returns boolean language sql stable security definer set search_path to 'public', 'pg_temp' as $function$
  select false;
$function$;

-- 2. The admin sets or clears a participant's CESI Executive Role.
create or replace function public.admin_set_exec_role(p_profile_id uuid, p_role text)
returns jsonb language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
declare v_role text := nullif(upper(btrim(coalesce(p_role, ''))), '');
begin
  if not public.is_admin() then raise exception 'Access denied' using errcode = '42501'; end if;
  if v_role is not null and v_role not in ('CEO','CFO','COO','CHRO','CTO','CMO','CCO','CPO','CRO','CSO') then
    return jsonb_build_object('ok', false, 'error', 'bad_role');
  end if;
  if not exists (select 1 from public.profiles p where p.id = p_profile_id and p.role::text = 'participant') then
    return jsonb_build_object('ok', false, 'error', 'not_participant');
  end if;
  insert into public.participant_profiles (profile_id, exec_role, updated_at)
  values (p_profile_id, v_role, now())
  on conflict (profile_id) do update set exec_role = excluded.exec_role, updated_at = now();
  return jsonb_build_object('ok', true, 'exec_role', v_role);
end;
$function$;
revoke all on function public.admin_set_exec_role(uuid, text) from public, anon;
grant execute on function public.admin_set_exec_role(uuid, text) to authenticated;
