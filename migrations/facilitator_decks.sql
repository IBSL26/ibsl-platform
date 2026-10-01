-- Facilitator decks: private storage for the 12 unit PowerPoint decks.
-- Run once in the Supabase SQL editor.
--
-- Layout:  facilitator_decks / Module-<1..4> / unit-<01..12>.pptx
--          facilitator_decks / Module-<1..4> / unit-<01..12> / s01.jpg … + manifest.json  (deck reader)
--   Module-1: unit-01                      (Foundation)
--   Module-2: unit-02, unit-03, unit-04    (Direction)
--   Module-3: unit-05 … unit-09            (Influence)
--   Module-4: unit-10, unit-11, unit-12    (Grounding)
--
-- Access: a signed-in facilitator can read a deck only when they are assigned
-- (cohort_memberships.role_in_cohort = 'facilitator') to that module (unit column)
-- in at least one cohort. Admins (profiles.role = 'admin') can read all decks.
-- No one can upload, change or delete through the portal; uploads are done in
-- the Supabase dashboard, which uses the service role.

-- 1. Private bucket (PowerPoint decks, plus the deck-reader slide images and manifest; 50 MB limit)
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('facilitator_decks', 'facilitator_decks', false, 52428800,
        array['application/vnd.openxmlformats-officedocument.presentationml.presentation',
              'image/jpeg', 'application/json'])
on conflict (id) do update
  set public = false,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- 2. Access check (security definer so it does not depend on other tables' RLS)
create or replace function public.can_read_facilitator_deck(object_name text)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select
    exists (select 1 from public.profiles p
            where p.id = auth.uid() and p.role = 'admin')
    or exists (select 1 from public.cohort_memberships cm
               where cm.profile_id = auth.uid()
                 and cm.role_in_cohort = 'facilitator'
                 and cm.unit is not null
                 and split_part(object_name, '/', 1) = 'Module-' || cm.unit::text);
$$;

revoke all on function public.can_read_facilitator_deck(text) from public;
grant execute on function public.can_read_facilitator_deck(text) to authenticated;

-- 3. Read policy (signed URLs are created through this policy)
drop policy if exists "facilitator_decks_read" on storage.objects;
create policy "facilitator_decks_read"
  on storage.objects for select
  to authenticated
  using (bucket_id = 'facilitator_decks'
         and public.can_read_facilitator_deck(name));

-- 4. Check (should return one row: facilitator_decks | false)
select id, public from storage.buckets where id = 'facilitator_decks';
