# -*- coding: utf-8 -*-
"""Unit 9 end to end (16 Oct 2026), on the real pages with a stand-in database (nothing touches the live site or Supabase).
Usage: python3 e2e_u09pv.py <site folder> <fake-supabase.js>
The site folder holds unit3_m2_lens8_p.html, s2r-save.js, capstone_P.html and collection.html; fake-supabase.js is the one in rebuild_u06."""
import sys, os, json, asyncio, mimetypes, re
from playwright.async_api import async_playwright
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pv'))
import u9pv_content as C
site, fake = sys.argv[1], sys.argv[2]
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)[:300]) if (extra and not cond) else '')
FL = C.fields(); NAMES = [x[2] for x in C.PARTS]; KEYS = [x[3] for x in C.PARTS]; BOXES = ['9A', '9B', '9C', '9D', '9E']
LENS = 'u3m2_lens8'; O = 'http://portal.test'
def row(lens, key, value): return {'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': lens, 'response_key': key, 'value': value}
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Member Two'}],
    'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'u-2', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
    'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': LENS, 'status': 'unlocked'}],
    'lens_responses': [row('u3m1_lens6', '__ex_work', {'o1_kr': 'Seed Key Result one', 'o1_owner': 'COO', 'o2_kr': 'Seed Key Result two', 'o2_owner': 'CFO'}),
                       row('u3m1_lens6', 'confirmed_items', ['Expectations · Start With the Future'])],
    'submissions': [],
    'lens_catalog': [{'id': 'u3m2_lens7', 'unit': 8, 'module': 3, 'sequence': 7, 'title': 'Performance Measurement', 'requires_lens': 'u3m1_lens6'},
                     {'id': LENS, 'unit': 9, 'module': 3, 'sequence': 8, 'title': 'Strategic Unclogging', 'requires_lens': 'u3m2_lens7'}],
    'box_count': {'u9': 5},
    'capstone': {'brief': {'case_name': 'Test Case Ltd', 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'Test cohort'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                 'members': [{'profile_id': 'u-1', 'full_name': 'Member One'}, {'profile_id': 'u-2', 'full_name': 'Member Two'}],
                 'sections': [{'key': 'u%d' % n, 'open': n == 9, 'status': 'draft', 'content': {}, 'confirmations': []} for n in range(2, 13)]}}
CTRL_COLL = ", u3m2_lens8:/^(uc_(record|challenge|clog|lever|review_realign|restore)$|confirmed_items$)/i"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
        async def route(r):
            u = r.request.url
            if 'supabase-js' in u or u.endswith('/supabase.umd.js'): return await r.fulfill(path=fake, content_type='application/javascript')
            if u.startswith(O + '/'):
                name = u[len(O) + 1:].split('?')[0]
                if name == 'blank.html': return await r.fulfill(body='<html><body>blank</body></html>', content_type='text/html')
                if name == 'collection_control.html':
                    t = open(os.path.join(site, 'collection.html'), encoding='utf-8').read(); assert t.count(CTRL_COLL) == 1
                    return await r.fulfill(body=t.replace(CTRL_COLL, ''), content_type='text/html; charset=utf-8')
                if name == 'capstone_control.html':
                    t = open(os.path.join(site, 'capstone_P.html'), encoding='utf-8').read(); m = re.search(r",\s*u9: \{ lens:'u3m2_lens8', rows:\[.*?\]\}", t, re.S)
                    assert m; return await r.fulfill(body=t.replace(m.group(0), ''), content_type='text/html; charset=utf-8')
                f = os.path.join(site, name)
                if os.path.isfile(f): return await r.fulfill(path=f, content_type=(mimetypes.guess_type(f)[0] or 'text/html') + '; charset=utf-8')
                return await r.fulfill(status=404, body='')
            await r.abort()
        await ctx.route('**/*', route)
        pg = await ctx.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text and 'ERR_' not in m.text else None)
        pg.on('dialog', lambda d: asyncio.ensure_future(d.accept()))
        await pg.goto(O + '/blank.html')
        await pg.evaluate("(s)=>{localStorage.clear();localStorage.setItem('fakedb',JSON.stringify(s));localStorage.setItem('fake_uid','u-1');}", SEED)
        async def dbx(): return json.loads(await pg.evaluate("localStorage.getItem('fakedb')"))
        def u9rows(d): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == LENS and r['profile_id'] == 'u-1'}
        # A · Capstone before anything is confirmed
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(900)
        labels = await pg.evaluate("[...document.querySelectorAll('#sec_u9 .box-l')].map(e=>e.textContent)")
        ok('A · Unit 9 section shows five boxes, 9A to 9E, with the new headings', [l[:2] for l in labels] == BOXES and 'Original challenge' in labels[0] and 'Restore' in labels[4], labels)
        await pg.evaluate("capToggle('u9')"); await pg.click("#sec_u9 .pull .btn"); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#msg_u9'); ok('A · nothing is brought in before the group confirms', m.startswith('Nothing is confirmed on your Unit 9 page yet.'), m)
        # B · the real Unit 9 page
        await pg.goto(O + '/unit3_m2_lens8_p.html'); await pg.wait_for_timeout(1500)
        ok('B · the real Unit 9 page opens through the real save helper', await pg.evaluate("typeof S2R.submit") == 'function')
        await pg.evaluate("document.querySelectorAll('.mod').forEach(x=>x.classList.add('active'));document.querySelectorAll('.acc').forEach(a=>a.classList.add('open'));document.querySelectorAll('details').forEach(d=>d.open=true)")
        ok('B · 5.1 shows the group’s Unit 7 Key Results', 'Seed Key Result one' in await pg.inner_text('#u9Krs'))
        for rid in ('ref1', 'ref3', 'ref4'):
            await pg.fill('#' + rid, 'My answer for ' + rid); await pg.wait_for_timeout(100)
        await pg.select_option('[data-fkey="ref2"][data-fidx="0"]', '4'); await pg.fill('[data-fkey="ref2"][data-fidx="7"]', 'My clog note')
        for k, n in (('ref7', 5), ('ref8', 7)):
            for i in range(n):
                sel = '[data-fkey="%s"][data-fidx="%d"]' % (k, i)
                if await pg.evaluate("(s)=>document.querySelector(s).tagName", sel) == 'SELECT': await pg.select_option(sel, '02 · Streamline')
                else: await pg.fill(sel, 'Answer %s %d' % (k, i))
        await pg.wait_for_timeout(2500)
        rows = u9rows(await dbx())
        ok('B · ref1, ref3, ref4 saved', all(rows.get(r) == 'My answer for ' + r for r in ('ref1', 'ref3', 'ref4')), {r: rows.get(r) for r in ('ref1', 'ref3', 'ref4')})
        ok('B · ref2 saved (rating and note)', 'Structural Misfit: 4' in str(rows.get('ref2')) and 'My clog note' in str(rows.get('ref2')), rows.get('ref2'))
        ok('B · ref7 saved (five answers)', all('Answer ref7 %d' % i in str(rows.get('ref7')) for i in range(5)), rows.get('ref7'))
        ok('B · ref8 saved (six answers and the lever)', all('Answer ref8 %d' % i in str(rows.get('ref8')) for i in (0, 1, 2, 3, 4, 6)) and '02 · Streamline' in str(rows.get('ref8')), rows.get('ref8'))
        for f in FL:
            if f[4] == 's': await pg.select_option('#u9_' + f[0], f[5][1])
            else: await pg.fill('#u9_' + f[0], 'Group entry ' + f[0])
        await pg.wait_for_timeout(1800)
        rows = u9rows(await dbx())
        ok('B · the group work saves while it is typed', isinstance(rows.get('__uc_work'), dict) and len([v for v in rows['__uc_work'].values() if v]) == len(FL) == 21 and isinstance(rows.get('uc_record'), str), list(rows.keys()))
        ok('B · before Confirm nothing is marked as confirmed', not any(nm in (rows.get('confirmed_items') or []) for nm in NAMES))
        await pg.click('#u9ConfBtn'); await pg.wait_for_timeout(1500)
        rows = u9rows(await dbx())
        ok('B · Confirm saves the five parts as text', all(isinstance(rows.get(k), str) and rows[k] for k in KEYS) and 'Selected clog: Capability Gaps' in rows['uc_clog'], await pg.inner_text('#u9Msg'))
        ok('B · Confirm saves the five names in confirmed_items', all(nm in (rows.get('confirmed_items') or []) for nm in NAMES), rows.get('confirmed_items'))
        await pg.evaluate("sendToFacilitator()"); await pg.wait_for_timeout(900)
        d = await dbx(); subs = [s for s in d['submissions'] if s['lens_id'] == LENS]
        ok('B · Submit to Facilitator stores one submission', len(subs) == 1)
        resp = subs[0]['payload']['responses'] if subs else {}
        ok('B · the submission carries the reflections and the group work', all(r in resp for r in ('ref1', 'ref2', 'ref3', 'ref4', 'ref7', 'ref8')) and all(k in resp for k in KEYS), sorted(resp.keys()))
        # control
        await pg.goto(O + '/capstone_control.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u9'][0]
        ok('control · with the Unit 9 rows taken out of the Capstone page there is no bring-in', sec['content'] == {}, sec['content'])
        # C · Capstone
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u9'][0]
        want = [rows[k].strip() for k in KEYS]
        ok('C · the Capstone brings the Unit 9 work into 9A to 9E', sorted(sec['content'].keys()) == BOXES, sec['content'].keys())
        ok('C · word for word', [sec['content'].get(bx) for bx in BOXES] == want)
        await pg.click("#sec_u9 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u9'); ok('C · with five boxes the section goes for team confirmation', m.startswith('Sent for team confirmation.'), m)
        # D · Learning Portfolio
        await pg.goto(O + '/collection.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        chapter = "(()=>{const e=document.getElementById('ch-u3m2_lens8');if(!e)return '';e.querySelectorAll('.collapsed').forEach(x=>x.classList.remove('collapsed'));return e.innerText;})()"
        ch = await pg.evaluate(chapter)
        ok('D · the Learning Portfolio has a Unit 9 chapter', 'Strategic Unclogging' in ch)
        ok('D · the reflections are in it', all(('My answer for ' + r) in ch for r in ('ref1', 'ref3', 'ref4')) and 'Answer ref7 0' in ch and 'Answer ref8 6' in ch and 'My clog note' in ch)
        Q = ['Think of a strategy initiative that stalled', 'Rate each clog', 'Think about one decision, policy or management practice', 'Reflect on how your leadership decisions']
        ok('D · each answer shows under its question', all(q in ch for q in Q), [q for q in Q if q not in ch])
        ok('D · the group work is left out', 'Group entry' not in ch.split('UNIT SUMMARY')[0])
        await pg.goto(O + '/collection_control.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        chc = await pg.evaluate(chapter)
        ok('control · with the Unit 9 line taken out of the Learning Portfolio the group work shows', 'Group entry' in chc)
        ok('no page error', not errs, errs[:5])
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
