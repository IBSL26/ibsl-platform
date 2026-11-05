-- Key reflections aligned to section content (5 Nov 2026): section-to-skill links and skill wording follow the reflections.
create or replace function public.competency_section_skill(p_unit integer, p_section integer)
returns integer language sql immutable as $$
  select (('{"2":[1,2,3,1],"3":[1,3,3,2],"4":[1,3,2,3],"5":[2,2,1,3],"6":[1,3,2,2],"7":[1,1,2,3],"8":[2,2,3,1],"9":[1,2,1,3],"10":[1,2,1,3],"11":[3,2,1,3],"12":[1,3,2,1]}'::jsonb)->p_unit::text->>(p_section - 1))::int
$$;
revoke all on function public.competency_section_skill(integer, integer) from public, anon, authenticated;
update public.competency_framework set skills = '["Test Key Results against Arena, Boundaries, Competition and Value Proposition","Recognise role-based ABCV blind spots and assign who verifies them","Recognise the Industry Illusion traps of familiarity, exclusion and complacency"]'::jsonb where unit_no = 4;
update public.competency_framework set skills = '["Use the OCEAVL Assessment to adapt how you lead change","Lead change through the 4 Checks of Mind, Heart, Hands and Habit and move people from compliance to commitment","Align the leadership team to lead change with one voice"]'::jsonb where unit_no = 5;
update public.competency_framework set skills = '["Establish expectations through clarity, capability and commitment","Map the Expectations Chain and the enabling promises it depends on","Conduct an Alignment Dialogue using the GROW model"]'::jsonb where unit_no = 7;
update public.competency_framework set skills = '["Lead an Enterprise Performance Intelligence Circle","Recover performance through Review–Realign–Restore and the Accountability Loop","Diagnose measurement fractures across functions"]'::jsonb where unit_no = 8;
