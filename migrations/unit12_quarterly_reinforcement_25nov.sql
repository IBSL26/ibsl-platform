-- Unit 12 rework (25 Nov 2026): new skills, and the reflection-to-skill links for Unit 12.
-- Run once in the Supabase SQL editor ("S2R Portal Production"). Safe to run again.
update public.competency_framework
set skills = '["Maintain the Three Lines of Sight","Detect Performance Gravity and early drift","Reinforce recovery across people and organisational performance"]'::jsonb
where unit_no = 12;

do $$
declare d text;
begin
  select pg_get_functiondef('public.competency_section_skill(integer,integer)'::regprocedure) into d;
  d := replace(d, '"12":[1,3,2,1]', '"12":[1,2,2,3]');
  execute d;
end $$;

select skills from public.competency_framework where unit_no = 12;
select public.competency_section_skill(12,1) as s1, public.competency_section_skill(12,2) as s2,
       public.competency_section_skill(12,3) as s3, public.competency_section_skill(12,4) as s4;
