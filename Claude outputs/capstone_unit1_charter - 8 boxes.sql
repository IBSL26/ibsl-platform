-- S2R Portal · Problem Charter refinement (19 October 2026): the Unit 1 section now has 8 boxes, 1A to 1H.
-- Paste ALL of this into the Supabase SQL Editor and select Run. Expected result: 8.
create or replace function public.capstone_section_box_count(p_key text)
returns integer language sql immutable set search_path = public as $$
  select case p_key when 'u1' then 8 when 'u2' then 6 when 'u3' then 6 when 'u4' then 6 when 'u5' then 3 when 'u7' then 5 when 'u8' then 4 when 'u9' then 5 when 'u10' then 6 when 'u11' then 5 when 'u12' then 5 when 'u6' then 2 else 5 end;
$$;

select public.capstone_section_box_count('u1') as u1_boxes;
