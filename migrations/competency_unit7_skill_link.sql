-- Unit 7 (5 Nov 2026): Section 2 evidences the Expectations Chain (skill 2), Section 3 establishing expectations (skill 1).
create or replace function public.competency_section_skill(p_unit integer, p_section integer)
returns integer language sql immutable as $$
  select (('{"2":[1,2,3,1],"3":[1,2,3,1],"4":[1,3,2,2],"5":[2,2,1,3],"6":[1,3,2,2],"7":[1,2,1,3],"8":[2,2,3,1],"9":[1,2,1,3],"10":[1,2,1,3],"11":[3,2,1,3],"12":[1,3,2,1]}'::jsonb)->p_unit::text->>(p_section - 1))::int
$$;
revoke all on function public.competency_section_skill(integer, integer) from public, anon, authenticated;
select public.competency_section_skill(7, 2) as section_2_skill, public.competency_section_skill(7, 3) as section_3_skill;

-- Skills reworded to follow the key reflections (5 Nov 2026).
update public.competency_framework set skills = '["Define a Strategy Architecture and create shared understanding of organisational position and direction","Crystallise a Strategy Intent Statement","Translate intent to future success and create one vision of Success in Practice"]'::jsonb where unit_no = 2;
update public.competency_framework set skills = '["Test Key Results against Arena, Boundaries, Competition and Value Proposition","Name Must-Be-True conditions, assign their owners and confirm them","Recognise the Industry Illusion traps of familiarity, exclusion and complacency"]'::jsonb where unit_no = 4;
update public.competency_framework set skills = '["Use the OCEAVL Assessment to adapt how you lead change","State a change through its Shift, Stake and Step and lead it through the 4 Checks of Mind, Heart, Hands and Habit","Align the leadership team to lead change with one voice"]'::jsonb where unit_no = 5;
update public.competency_framework set skills = '["Build an S2R® Contribution Map™ from a Key Result","Apply the FACES Framework to drive collective success","Align your performance scorecard to your contribution to Key Results"]'::jsonb where unit_no = 6;
update public.competency_framework set skills = '["Establish expectations through clarity, capability and commitment","Map the Expectations Chain upline and downline","Conduct an Alignment Dialogue using the GROW model"]'::jsonb where unit_no = 7;
update public.competency_framework set skills = '["Diagnose the Seven Performance Clogs and your function’s part in them","Select the right Strategic Unclogging Lever","Run the Unclogging Cycle across people and organisational performance"]'::jsonb where unit_no = 9;
update public.competency_framework set skills = '["Assess ESRG conditions and correct for executive bias","Interpret ESRG results by execution capability","Translate ESRG results into alignment interventions through cross-functional review"]'::jsonb where unit_no = 10;
update public.competency_framework set skills = '["Diagnose organisational health and strengthen its weakest trait","Quantify people-performance losses","Build a Cultural Operating Code"]'::jsonb where unit_no = 11;
