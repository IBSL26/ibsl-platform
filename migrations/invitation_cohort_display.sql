-- Setup page: show the cohort(s) and organisation the invited person is already assigned to (1 Nov 2026).
-- The invitee cannot read the cohorts and organisations tables directly before registering, so the
-- setup page showed "To be assigned". This reads them on the invitee's behalf, for their own email only.
create or replace function public.get_my_invitation_placement()
returns table (cohort_names text[], organisation_name text)
language sql
stable
security definer
set search_path to 'public', 'pg_temp'
as $function$
  with me as (
    select auth.uid() as uid, lower(coalesce(auth.jwt() ->> 'email', '')) as email
  ),
  inv as (
    select i.cohort_id, i.organisation_id
    from public.invitations i, me
    where lower(i.email) = me.email and i.status = 'pending'
  )
  select
    (select array_agg(distinct c.name order by c.name)
     from public.cohorts c, me
     where c.archived_at is null
       and (c.id in (select cohort_id from inv where cohort_id is not null)
            or exists (select 1 from public.cohort_memberships cm
                       where cm.cohort_id = c.id and cm.profile_id = me.uid))),
    (select o.name from public.organisations o
     where o.id in (select organisation_id from inv where organisation_id is not null)
     limit 1);
$function$;
revoke all on function public.get_my_invitation_placement() from public, anon;
grant execute on function public.get_my_invitation_placement() to authenticated;
