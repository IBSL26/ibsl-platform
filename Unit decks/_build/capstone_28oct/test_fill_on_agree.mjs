import { PGlite } from '@electric-sql/pglite';
import fs from 'fs';
const db = new PGlite();
const SP = '/tmp/claude-0/-home-claude/82e91403-961a-52d1-b108-d34a3f052e80/scratchpad/';
let pass = 0, fail = 0;
function check(name, ok, info) { if (ok) { pass++; console.log('PASS', name); } else { fail++; console.log('FAIL', name, info === undefined ? '' : JSON.stringify(info)); } }
const q = async (s, p) => (await db.query(s, p)).rows;
const as = async (uid) => db.exec(`select set_config('test.uid', '${uid || ''}', false)`);

await db.exec(`

create schema auth;
create function auth.uid() returns uuid language sql stable as $$ select nullif(current_setting('test.uid', true), '')::uuid $$;
create table profiles (id uuid primary key, full_name text, role text);
create table cohorts (id uuid primary key, name text);
create table capstone_team (id uuid primary key default gen_random_uuid(), cohort_id uuid, team_name text unique, blueprint_reopened boolean not null default false, updated_at timestamptz);
create table capstone_individual (id uuid primary key default gen_random_uuid(), team_id uuid references capstone_team(id) on delete cascade, profile_id uuid references profiles(id), cohort_id uuid);
create table capstone_brief (cohort_id uuid primary key, case_name text, brief_text text, submission_due timestamptz, showcase_at timestamptz, showcase_venue text, updated_by uuid, updated_at timestamptz default now());
create table lens_responses (profile_id uuid, cohort_id uuid, lens_id text, response_key text, value jsonb, updated_at timestamptz default now(), unique (profile_id, lens_id, response_key));
create table lens_progress (profile_id uuid, cohort_id uuid, lens_id text, status text);
create table capstone_blueprint_section (id uuid primary key default gen_random_uuid(), team_id uuid not null references capstone_team(id) on delete cascade,
  section_key text not null check (section_key in ('u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12')),
  content jsonb not null default '{}'::jsonb, status text not null default 'draft' check (status in ('draft','awaiting','agreed')),
  updated_by uuid references profiles(id), updated_at timestamptz not null default now(), sent_by uuid references profiles(id), sent_at timestamptz, agreed_at timestamptz, unique (team_id, section_key));
create table capstone_blueprint_confirmation (section_id uuid not null references capstone_blueprint_section(id) on delete cascade, profile_id uuid not null references profiles(id) on delete cascade, confirmed_at timestamptz not null default now(), primary key (section_id, profile_id));
create function is_admin() returns boolean language sql stable as $$ select exists (select 1 from profiles where id = auth.uid() and role = 'admin') $$;
create or replace function public.capstone_section_lens(p_key text) returns text language sql immutable set search_path = public as $$
  select case p_key when 'u1' then 'u1_foundations' when 'u2' then 'u2m1_lens1' when 'u3' then 'u2m1_lens2' when 'u4' then 'u2m1_lens3'
    when 'u5' then 'u3m1_lens4' when 'u6' then 'u3m1_lens5' when 'u7' then 'u3m1_lens6' when 'u8' then 'u3m2_lens7' when 'u9' then 'u3m2_lens8'
    when 'u10' then 'u4m1_lens9' when 'u11' then 'u4m1_lens10' when 'u12' then 'u4m2_lens11' end; $$;
create or replace function public.capstone_section_box_count(p_key text) returns integer language sql immutable as $$
  select case p_key when 'u1' then 8 when 'u2' then 6 when 'u3' then 6 when 'u4' then 6 when 'u5' then 3 when 'u6' then 3 when 'u7' then 5 when 'u8' then 5 when 'u9' then 5 when 'u10' then 4 when 'u11' then 5 when 'u12' then 4 else 5 end; $$;
create or replace function public.capstone_team_locked(p_team_id uuid) returns boolean language sql stable set search_path = public as $$
  select coalesce((select (not t.blueprint_reopened) and b.submission_due is not null and now() > b.submission_due
      from capstone_team t left join capstone_brief b on b.cohort_id = t.cohort_id where t.id = p_team_id), false); $$;
create role authenticated; create role anon;
`);
// the live team_work tables and functions, unchanged, from team_work_shared_record.sql (Blocks 2-12, minus begin/commit)
let tw = fs.readFileSync(SP + 'team_work_shared_record.sql', 'utf8').replace(/^begin;$/m, '').replace(/^commit;$/m, '');
await db.exec(tw);
await db.exec(fs.readFileSync(SP + 'capstone_fill_on_agree.sql', 'utf8'));
await db.exec(fs.readFileSync(SP + 'capstone_fill_on_agree.sql', 'utf8')); // run twice
check('can be run twice; trigger once', (await q(`select count(*)::int n from pg_trigger where tgname='capstone_fill_on_agreement'`))[0].n === 1);
const chk = await q(`select (select count(*) from unnest(array['u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12']) k
  where (select count(*) from jsonb_object_keys(public.capstone_section_map(k))) = public.capstone_section_box_count(k))::int n`);
check('12 sections mapped with the right box counts', chk[0].n === 12, chk);

const C = '00000000-0000-0000-0000-0000000000c1';
const A = '00000000-0000-0000-0000-00000000000a', M1 = '00000000-0000-0000-0000-000000000001', M2 = '00000000-0000-0000-0000-000000000002', M3 = '00000000-0000-0000-0000-000000000003';
await db.exec(`insert into cohorts values ('${C}','Live');
insert into profiles values ('${A}','Admin','admin'),('${M1}','Ana','participant'),('${M2}','Ben','participant'),('${M3}','Cy','participant');`);
const T = (await q(`insert into capstone_team (cohort_id, team_name) values ('${C}','Group 1') returning id`))[0].id;
await db.exec(`insert into capstone_individual (team_id, profile_id, cohort_id) values ('${T}','${M1}','${C}'),('${T}','${M2}','${C}'),('${T}','${M3}','${C}')`);

// Unit 12 group work: M1 scribe writes all four boxes.
const u12 = { qs_strategic: 'Strategic line text', qs_operational: 'Operational line text', qs_behavioural: 'Behavioural line text', qs_kiss: 'KISS text' };
await as(M1);
check('set scribe', (await q(`select team_work_set_scribe('${C}','u4m2_lens11','${M1}') r`))[0].r.ok);
const w = (await q(`select team_work_write('${C}','u4m2_lens11',$1::jsonb,'["a"]'::jsonb) r`, [JSON.stringify(u12)]))[0].r;
check('scribe write', w.ok && w.version === 1, w);
const sec = async (k) => (await q(`select status, content, (select count(*)::int from capstone_blueprint_confirmation c where c.section_id = s.id) nconf from capstone_blueprint_section s where team_id='${T}' and section_key='${k}'`))[0];
await q(`select team_work_agree('${C}','u4m2_lens11',1)`);
check('one of three agreed: section not filled', !(await sec('u12')), await sec('u12'));
await as(M2); await q(`select team_work_agree('${C}','u4m2_lens11',1)`);
check('two of three agreed: section not filled', !(await sec('u12')));
await as(M3); const last = (await q(`select team_work_agree('${C}','u4m2_lens11',1) r`))[0].r;
check('last member agrees: agree succeeds', last.ok && last.all_agreed, last);
let s = await sec('u12');
check('last member agrees: section filled and Agreed', s && s.status === 'agreed' && s.content['12A'] === 'Strategic line text' && s.content['12D'] === 'KISS text' && Object.keys(s.content).length === 4, s);
check('confirmations for every member', s && s.nconf === 3, s);
check('confirmed_items still written by team_work_agree', (await q(`select value from lens_responses where profile_id='${M2}' and lens_id='u4m2_lens11' and response_key='confirmed_items'`))[0].value[0] === 'a');

// Scribe edits: agreements clear; section keeps old text until everyone agrees again.
await as(M1);
await q(`select team_work_write('${C}','u4m2_lens11','{"qs_kiss":"KISS v2"}'::jsonb,'["a"]'::jsonb)`);
for (const m of [M1, M2]) { await as(m); await q(`select team_work_agree('${C}','u4m2_lens11',2)`); }
check('after edit, before all agree: old text stays', (await sec('u12')).content['12D'] === 'KISS text');
await as(M3); await q(`select team_work_agree('${C}','u4m2_lens11',2)`);
check('after all agree again: new text', (await sec('u12')).content['12D'] === 'KISS v2');

// Incomplete record: agreeing still works; section not filled.
await as(M1); await q(`select team_work_set_scribe('${C}','u4m1_lens10','${M1}')`);
await q(`select team_work_write('${C}','u4m1_lens10','{"oh_func":"F","oh_cons":"C"}'::jsonb,'[]'::jsonb)`);
let ok = true; for (const m of [M1, M2, M3]) { await as(m); const r = (await q(`select team_work_agree('${C}','u4m1_lens10',1) r`))[0].r; ok = ok && r.ok; }
check('incomplete record: every Agree still succeeds', ok);
check('incomplete record: section not filled', !(await sec('u11')));

// Unit with no Capstone section (lens not mapped): agree unaffected.
await as(M1); await q(`select team_work_set_scribe('${C}','other_lens','${M1}')`); await q(`select team_work_write('${C}','other_lens','{"x":"y"}'::jsonb,'[]'::jsonb)`);
ok = true; for (const m of [M1, M2, M3]) { await as(m); ok = ok && (await q(`select team_work_agree('${C}','other_lens',1) r`))[0].r.ok; }
check('lens without a section: Agree unaffected', ok);

// After the deadline: no fill on agree; admin button fills.
await db.exec(`insert into capstone_brief (cohort_id, submission_due) values ('${C}', now() - interval '1 day')`);
await as(M1); await q(`select team_work_set_scribe('${C}','u3m1_lens4','${M1}')`);
await q(`select team_work_write('${C}','u3m1_lens4','{"kit_profile":"P","kit_mind":"M","kit_habit":"H"}'::jsonb,'[]'::jsonb)`);
for (const m of [M1, M2, M3]) { await as(m); await q(`select team_work_agree('${C}','u3m1_lens4',1)`); }
check('after deadline: agree does not fill (locked)', !(await sec('u5')));

// Admin button
await as(M1);
let err = null; try { await q(`select admin_capstone_bring_in('${T}')`); } catch (e) { err = e.message; }
check('participant cannot use admin button', err && /not authorised/.test(err), err);
await as(A);
const b = (await q(`select admin_capstone_bring_in('${T}') r`))[0].r;
check('admin button: fills u5, keeps u12, waits for others', b.ok && b.filled.includes('u5') && b.unchanged.includes('u12') && b.waiting.includes('u11') && b.waiting.includes('u1'), b);
s = await sec('u5');
check('admin-filled section Agreed with three confirmations', s.status === 'agreed' && s.content['5C'] === 'H' && s.nconf === 3, s);
const b2 = (await q(`select admin_capstone_bring_in('${T}') r`))[0].r;
check('admin button twice: nothing changes', b2.filled.length === 0 && b2.unchanged.includes('u5'), b2);

// A member removed: the remaining members' agreement counts (same rule as the live sync).
console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
