import { PGlite } from '@electric-sql/pglite';
const db = new PGlite();
const q = (s,p)=>db.query(s,p);
await db.exec(`
create schema auth; create table auth.cur(uid uuid);
create function auth.uid() returns uuid language sql stable as $$ select uid from auth.cur limit 1 $$;
create role anon; create role authenticated;
create table profiles(id uuid primary key, full_name text);
create table capstone_individual(team_id uuid, profile_id uuid, cohort_id uuid);
create table lens_responses(profile_id uuid, cohort_id uuid, lens_id text, response_key text, value jsonb, updated_at timestamptz, unique(profile_id,lens_id,response_key));
create function public.team_work_my_team(p_cohort_id uuid) returns uuid language sql stable security definer set search_path = public as $$
  select team_id from capstone_individual where profile_id = auth.uid() and cohort_id = p_cohort_id limit 1; $$;
create function public.capstone_section_box_count(p_key text) returns integer language sql immutable set search_path = public as $$
  select case p_key when 'u1' then 8 when 'u2' then 6 when 'u3' then 6 when 'u4' then 6 when 'u5' then 3 when 'u6' then 3 when 'u8' then 5 when 'u10' then 6 else 5 end; $$;
`);
const sql = (await import('fs')).readFileSync(process.argv[2],'utf8');
await db.exec(sql);
const T1='00000000-0000-0000-0000-0000000000a1',T2='00000000-0000-0000-0000-0000000000a2',C='00000000-0000-0000-0000-0000000000c1';
const A='00000000-0000-0000-0000-000000000001',B='00000000-0000-0000-0000-000000000002',X='00000000-0000-0000-0000-000000000009';
await db.exec(`insert into profiles values ('${A}','Ann'),('${B}','Ben'),('${X}','Xena');
insert into capstone_individual values ('${T1}','${A}','${C}'),('${T1}','${B}','${C}'),('${T2}','${X}','${C}');
insert into lens_responses values ('${A}','${C}','u4m1_lens9','esrg_scan','"Facilities · Annual: 4"',now()),
 ('${A}','${C}','u4m1_lens9','esrg_scan_head','"Capstone executive role: COO · Ann"',now()),
 ('${A}','${C}','u4m1_lens9','ref9','"private reflection"',now()),
 ('${X}','${C}','u4m1_lens9','esrg_scan','"Facilities · Annual: 1"',now());`);
let ok=0,bad=0;const chk=(n,c)=>{if(c)ok++;else{bad++;console.log('FAIL',n);}};
await q(`insert into auth.cur values ('${A}')`);
let r=(await q(`select public.team_esrg_scans('${C}') j`)).rows[0].j;
chk('two members of own team',r.length===2);
chk('A scan read',r.find(m=>m.full_name==='Ann').scan==='Facilities · Annual: 4');
chk('A head read',r.find(m=>m.full_name==='Ann').head.startsWith('Capstone executive role'));
chk('B has no scan (null)',r.find(m=>m.full_name==='Ben').scan===null);
chk('other team not visible',!JSON.stringify(r).includes('Xena'));
chk('private keys not returned',!JSON.stringify(r).includes('private reflection'));
await q(`update auth.cur set uid='${X}'`);
r=(await q(`select public.team_esrg_scans('${C}') j`)).rows[0].j;chk('X sees only own team',r.length===1&&r[0].full_name==='Xena');
await q(`update auth.cur set uid='${A}'`);
r=(await q(`select public.team_esrg_scans('00000000-0000-0000-0000-0000000000c9') j`)).rows[0].j;chk('other cohort empty',r.length===0);
await q(`delete from auth.cur`);let threw=false;try{await q(`select public.team_esrg_scans('${C}')`);}catch(e){threw=true;}chk('signed out refused',threw);
const bc=(await q(`select ${['u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12'].map(k=>`public.capstone_section_box_count('${k}') as ${k}`).join(',')}`)).rows[0];
chk('box counts',JSON.stringify(Object.values(bc))===JSON.stringify([8,6,6,6,3,3,5,5,5,4,5,5]));
await db.exec(sql); // run twice
const bc2=(await q(`select public.capstone_section_box_count('u10') a, public.capstone_section_box_count('u6') b`)).rows[0];chk('second run keeps counts',bc2.a===4&&bc2.b===3);
console.log(ok+' passed, '+bad+' failed');
