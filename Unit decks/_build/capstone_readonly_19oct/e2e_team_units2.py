# -*- coding: utf-8 -*-
"""Shared group record on Units 1 and 3 to 9 (19 Oct 2026), with a stand-in database.
For each unit: Ann chooses herself as scribe and types one entry; the entry reaches Ben's page;
Ben's boxes are closed; Agree is held while the record is incomplete; reflections stay open.
Then, for every unit, a filled record is agreed by both and the Capstone names reach both members.
Usage: python3 e2e_team_units.py <site> <fake-supabase-team.js>"""
import sys, os, json, asyncio, mimetypes
from playwright.async_api import async_playwright
site, fake = sys.argv[1], sys.argv[2]
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)[:300]) if (extra and not cond) else '')
O = 'http://portal.test'
UNITS = [  # page, lens, section tab, Capstone names, work key
    ('unit1_P.html', 'u1_foundations', 5, ['Problem Charter · Simulated Company'], '__pc_work'),
    ('unit2_m1_lens3_p.html', 'u2m1_lens3', 4, ['MBT · Arena'], '__mbt_work'),
    ('unit2_m1_lens2_p.html', 'u2m1_lens2', 4, ['KISS · Keep', 'Enterprise OKRs'], 'kex_cx_keep'),
    ('unit3_m1_lens4_p.html', 'u3m1_lens4', 4, ['Alignment Plan · Mind'], '__align_work'),
    ('unit3_m1_lens5_p.html', 'u3m1_lens5', 4, ['Enterprise PM System · Contribution Map'], '__cm_work'),
    ('unit3_m1_lens6_p.html', 'u3m1_lens6', 4, ['Expectations · Start With the Future'], '__ex_work'),
    ('unit3_m2_lens7_p.html', 'u3m2_lens7', 4, ['Review Discipline · Early Warning Signals'], '__rd_work'),
    ('unit3_m2_lens8_p.html', 'u3m2_lens8', 4, ['Unclogging · Original Challenge'], '__uc_work'),
]
def seed():
    lp = [{'profile_id': u, 'cohort_id': 'c-1', 'lens_id': l, 'status': 'unlocked'} for u in ('u-1', 'u-2') for l in [x[1] for x in UNITS] + ['u2m1_lens1']]
    return {
        'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Ann Member'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Ben Member'}],
        'cohort_memberships': [{'profile_id': u, 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'} for u in ('u-1', 'u-2')],
        'capstone_individual': [{'team_id': 't-1', 'profile_id': u, 'cohort_id': 'c-1'} for u in ('u-1', 'u-2')],
        'lens_progress': lp, 'submissions': [], 'lens_catalog': [],
        'lens_responses': [{'profile_id': u, 'cohort_id': 'c-1', 'lens_id': 'u2m1_lens2', 'response_key': k, 'value': v} for u in ('u-1', 'u-2') for k, v in
                           [('__okr_work', {'items': [{'theme': 'Responsiveness', 'al': [1, 1, 1, 1], 'obj': 'Objective one', 'krs': [{'t': 'Raise first-contact resolution from 60% to 85% by 30 September 2027'}]}]}), ('confirmed_items', ['Enterprise OKRs'])]],
        'capstone': {'brief': {}, 'cohort': {'name': 'T'}, 'team': {'id': 't-1', 'name': 'T', 'reopened': False}, 'members': [], 'sections': []}}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
        async def route(r):
            u = r.request.url
            if 'supabase-js' in u: return await r.fulfill(path=fake, content_type='application/javascript')
            if u.startswith(O + '/'):
                name = u[len(O) + 1:].split('?')[0]
                if name == 'blank.html': return await r.fulfill(body='<html></html>', content_type='text/html')
                f = os.path.join(site, name)
                if os.path.isfile(f): return await r.fulfill(path=f, content_type=(mimetypes.guess_type(f)[0] or 'text/html') + '; charset=utf-8')
                return await r.fulfill(status=404, body='')
            await r.abort()
        await ctx.route('**/*', route)
        pg = await ctx.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('dialog', lambda d: asyncio.ensure_future(d.accept()))
        await pg.goto(O + '/blank.html')
        await pg.evaluate("(s)=>{localStorage.clear();localStorage.setItem('fakedb',JSON.stringify(s));}", seed())
        async def dbx(): return json.loads(await pg.evaluate("localStorage.getItem('fakedb')"))
        def rows(d, uid, lens): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == lens and r['profile_id'] == uid}
        async def open_as(uid, page, tab):
            await pg.evaluate("(u)=>localStorage.setItem('fake_uid',u)", uid)
            await pg.goto(O + '/' + page); await pg.wait_for_timeout(1400)
            await pg.evaluate("(t)=>{if(typeof showMod==='function')showMod(t);document.querySelectorAll('.mod-panel.active .acc,.mod.active .acc').forEach(a=>a.classList.add('open'));}", tab); await pg.wait_for_timeout(300)
        FIRST = """(root)=>{const r=document.getElementById(root)||document.querySelector('#'+root);
            const els=[...r.querySelectorAll('.kiss-ta, textarea:not(.u3-ta),input[type=text],input:not([type])')].filter(e=>!e.classList.contains('p-thread-ta')&&e.type!=='hidden'&&e.type!=='file');
            return els.length?els[0].id:null;}"""
        for page, lens, tab, names, work in UNITS:
            u = page.split('.')[0]
            if os.environ.get('DBG'): print('DBG okr', json.dumps(rows(await dbx(), 'u-1', 'u2m1_lens2').get('__okr_work'))[:300])
            root = 'pcTool' if page == 'unit1_P.html' else 'mod4'
            await open_as('u-1', page, tab)
            ok(u + ' · the group record bar is on the page', await pg.evaluate("!!document.querySelector('#twBar .tw-bar')"))
            fid = await pg.evaluate(FIRST, root)
            ok(u + ' · before a scribe is chosen, the group boxes are closed', fid is None or await pg.evaluate("(i)=>document.getElementById(i).disabled", fid), fid)
            await pg.select_option('#twScribe', 'u-1'); await pg.wait_for_timeout(600)
            fid = await pg.evaluate(FIRST, root)
            ok(u + ' · Ann is scribe: a group box opens', fid is not None and not await pg.evaluate("(i)=>document.getElementById(i).disabled", fid), fid)
            if not fid: continue
            await pg.fill('#' + fid, 'Group entry for ' + u); await pg.wait_for_timeout(1700)
            d = await dbx(); ben = rows(d, 'u-2', lens)
            ok(u + ' · the scribe\'s entry is on Ben\'s page', 'Group entry for ' + u in json.dumps(ben, ensure_ascii=False), list(ben)[:6])
            await pg.evaluate("()=>{const b=document.getElementById('twAgree');}")
            ok(u + ' · Agree is held while the record is incomplete', await pg.evaluate("document.getElementById('twAgree').disabled") and 'Still to complete' in await pg.inner_text('#twBar'))
            await open_as('u-2', page, tab)
            v = await pg.evaluate("(i)=>{const e=document.getElementById(i);return e?[e.value,e.disabled]:null}", fid)
            ok(u + ' · Ben sees the entry, and his box is closed', v and v[0] == 'Group entry for ' + u and v[1], v)
            refl = await pg.evaluate("[...document.querySelectorAll('.ref-ta,.reflection-textarea')].filter(e=>e.disabled).length")
            ok(u + ' · reflections stay open for Ben', refl == 0, refl)

        # Full path: with the record complete, the scribe's page writes the Capstone outputs; both agree; names reach both
        PATCH = {'unit1_P': ("window.pcOpen=function(){return []}", 'pcTeamOut', ['pc_record', 'pc_company', 'pc_problem']),
                 'unit2_m1_lens3_p': ("window.mbOpen=function(){return []};window.mbS3Open=function(){return []}", 'u4TeamOut', ['mbt_record', 'mbt_arena', 'mbt_value']),
                 'unit2_m1_lens2_p': ("window.kissFilled=function(){return 16};window.okrProblems=function(){return []}", 'u3TeamOut', ['kiss_keep', 'kiss_stop', 'ent_priorities', 'ent_okrs']),
                 'unit3_m1_lens4_p': ("window.s5Open=function(){return []}", 'u5TeamOut', ['kit_team', 'kit_mind', 'kit_habit']),
                 'unit3_m1_lens5_p': ("window.u6Open=function(){return []}", 'u6TeamOut', ['cm_record', 'cm_map', 'cm_faces']),
                 'unit3_m1_lens6_p': ("window.u7Open=function(){return []}", 'u7TeamOut', ['ex_record', 'ex_future', 'ex_dialogue']),
                 'unit3_m2_lens7_p': ("window.u8Open=function(){return []}", 'u8TeamOut', ['rd_record', 'rd_warning', 'rd_credibility']),
                 'unit3_m2_lens8_p': ("window.u9Open=function(){return []}", 'u9TeamOut', ['uc_record', 'uc_challenge', 'uc_restore'])}
        for page, lens, tab, names, work in UNITS:
            u = page.split('.')[0]; patch, out, keys = PATCH[u]
            for who in ('u-1', 'u-2'):
                await open_as(who, page, tab)
                await pg.evaluate(patch)
                if who == 'u-1':
                    await pg.evaluate(out + "();"); await pg.evaluate("S2RTeam.flush()"); await pg.wait_for_timeout(700)
                await pg.evaluate("S2RTeam.redraw()")
                await pg.click('#twAgree'); await pg.wait_for_timeout(900)
            d = await dbx()
            got = rows(d, 'u-2', lens)
            ok(u + ' · the scribe\'s page wrote the Capstone outputs onto Ben\'s page', all(isinstance(got.get(k), str) for k in keys), [k for k in keys if not isinstance(got.get(k), str)])
            ok(u + ' · both agreed: the Capstone names are in both members\' lists', all(n in (rows(d, w, lens).get('confirmed_items') or []) for w in ('u-1', 'u-2') for n in names))
        ok('no page errors', not errs, errs[:5])
        await b.close()
    print('%d of %d pass' % (sum(R), len(R)))
asyncio.run(main())
