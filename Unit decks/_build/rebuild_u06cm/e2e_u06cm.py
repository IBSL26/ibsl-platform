# -*- coding: utf-8 -*-
"""Unit 6 (rework of 14 October 2026) end to end, on the real pages with a stand-in database (nothing touches the live site or Supabase).
Usage: python3 e2e_u06cm.py <site folder> <fake-supabase.js> [<screenshot folder>]"""
import sys, os, json, asyncio, mimetypes
from playwright.async_api import async_playwright
site, fake = sys.argv[1], sys.argv[2]; shots = sys.argv[3] if len(sys.argv) > 3 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)) if (extra and not cond) else '')
NAMES = ['Enterprise PM System · Contribution Map', 'Enterprise PM System · FACES Application']; KEYS = ['cm_map', 'cm_faces']
REFS = ['ref13', 'ref14', 'ref15', 'ref12']
O = 'http://portal.test'
OKR = {'items': [
    {'theme': 'Customer responsiveness', 'obj': 'Deliver consistently fast and effortless service experiences for customers', 'krs': [{'t': 'Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027'}, {'t': 'Increase customer requests resolved at first contact from 60% to 85% by 30 September 2027'}]},
    {'theme': 'Value creation', 'obj': 'Strengthen enterprise performance through scalable and efficient operations', 'krs': [{'t': 'Improve operating margin from 14% to 18% by 31 December 2027'}, {'t': 'Reduce leadership time spent on low-value projects from 25% to 10% by 30 June 2027'}]}]}
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Member Two'}],
    'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'u-2', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
    'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': 'u3m1_lens5', 'status': 'unlocked'}],
    'lens_responses': [
        {'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': 'u2m1_lens2', 'response_key': '__okr_work', 'value': OKR},
        {'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': 'u2m1_lens2', 'response_key': 'confirmed_items', 'value': ['Enterprise priorities', 'Enterprise OKRs']}],
    'submissions': [],
    'lens_catalog': [{'id': 'u3m1_lens4', 'unit': 5, 'module': 3, 'sequence': 4, 'title': 'Aligning Heart & Mind', 'requires_lens': None},
                     {'id': 'u3m1_lens5', 'unit': 6, 'module': 3, 'sequence': 5, 'title': 'Performance Management Setup', 'requires_lens': 'u3m1_lens4'}],
    'box_count': {'u6': 4},
    'capstone': {'brief': {'case_name': 'Test Case Ltd', 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'Test cohort'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                 'members': [{'profile_id': 'u-1', 'full_name': 'Member One'}, {'profile_id': 'u-2', 'full_name': 'Member Two'}],
                 'sections': [{'key': 'u%d' % n, 'open': n == 6, 'status': 'draft', 'content': {}, 'confirmations': []} for n in range(2, 13)]}}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
        async def route(r):
            u = r.request.url
            if 'supabase-js' in u or u.endswith('/supabase.umd.js'):
                return await r.fulfill(path=fake, content_type='application/javascript')
            if u.startswith(O + '/'):
                name = u[len(O) + 1:].split('?')[0]
                if name == 'blank.html': return await r.fulfill(body='<html><body>blank</body></html>', content_type='text/html')
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
        def u6rows(d): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == 'u3m1_lens5' and r['profile_id'] == 'u-1'}

        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(900)
        labels = await pg.evaluate("[...document.querySelectorAll('#sec_u6 .box-l')].map(e=>e.textContent)")
        ok('A · the Capstone Unit 6 section shows two boxes, 6A and 6B', [l[:2] for l in labels] == ['6A', '6B'], labels)
        await pg.evaluate("capToggle('u6')"); await pg.click("#sec_u6 .pull .btn"); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#msg_u6')
        ok('A · nothing is brought in before the group confirms', m.startswith('Nothing is confirmed on your Unit 6 page yet.'), m)

        await pg.goto(O + '/unit3_m1_lens5_p.html'); await pg.wait_for_timeout(1200)
        ok('B · the real Unit 6 page opens unlocked through the real save helper', await pg.evaluate("getComputedStyle(document.getElementById('p-lock-overlay')).display") == 'none')
        for rid in REFS:
            await pg.evaluate("(id)=>{const e=document.getElementById(id);const m=e.closest('[id^=mod]');showMod(parseInt(m.id.slice(3),10),null);e.closest('.acc').classList.add('open');}", rid)
            await pg.fill('#' + rid, 'My answer for ' + rid)
            await pg.evaluate("(id)=>document.getElementById(id).closest('.ref-block').querySelector('button').click()", rid)
            await pg.wait_for_timeout(150)
        await pg.wait_for_timeout(1500)
        rows = u6rows(await dbx())
        ok('B · the four personal reflections are saved', all(rows.get(r) == 'My answer for ' + r for r in REFS), {r: rows.get(r) for r in REFS})
        await pg.evaluate("showMod(4,null)"); await pg.wait_for_timeout(600)
        objs = await pg.evaluate("[...document.querySelectorAll('#u6_obj option')].map(o=>o.value).filter(Boolean)")
        ok('B · the Objective list holds the two Objectives confirmed in Unit 3', len(objs) == 2, objs)
        await pg.select_option('#u6_obj', objs[0]); await pg.wait_for_timeout(200)
        krs = await pg.evaluate("[...document.querySelectorAll('#u6_kr option')].map(o=>o.value).filter(Boolean)")
        ok('B · the Key Result list holds that Objective’s two Key Results', len(krs) == 2, krs)
        await pg.select_option('#u6_kr', krs[0])
        for n in range(1, 4):
            await pg.fill('#u6_f%d_name' % n, 'Function %d name' % n)
            for k in ['contrib', 'hos', 'hosm', 'esrg', 'esrgm']: await pg.fill('#u6_f%d_%s' % (n, k), 'Group entry %s %d' % (k, n))
        await pg.evaluate('u6Step(1)')
        for n in range(1, 4):
            for k in 'FACES': await pg.fill('#u6_f%d_%s' % (n, k), 'FACES entry %s %d' % (k, n))
        await pg.wait_for_timeout(1500)
        rows = u6rows(await dbx())
        ok('B · the group work saves while it is typed', isinstance(rows.get('__cm_work'), dict) and isinstance(rows.get('cm_record'), str), list(rows.keys()))
        ok('B · before Confirm nothing is marked as confirmed', not any(nm in (rows.get('confirmed_items') or []) for nm in NAMES))
        await pg.click('#u6ConfBtn'); await pg.wait_for_timeout(1200)
        rows = u6rows(await dbx())
        ok('B · Confirm saves cm_map and cm_faces as text', all(isinstance(rows.get(k), str) and len(rows[k]) > 50 for k in KEYS), await pg.inner_text('#u6Msg'))
        ok('B · Confirm saves the two names in confirmed_items', all(nm in (rows.get('confirmed_items') or []) for nm in NAMES), rows.get('confirmed_items'))
        ok('B · cm_map carries the Objective, the Key Result and the three functions', objs[0] in rows['cm_map'] and krs[0] in rows['cm_map'] and 'Function 3 · Function 3 name' in rows['cm_map'])
        await pg.evaluate("sendToFacilitator()"); await pg.wait_for_timeout(900)
        d = await dbx(); subs = [s for s in d['submissions'] if s['lens_id'] == 'u3m1_lens5']
        ok('B · Submit to Facilitator stores one submission', len(subs) == 1)

        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u6'][0]
        ok('C · the Capstone brings the Unit 6 work in, word for word', [sec['content'].get(x) for x in ('6A', '6B')] == [rows[k].strip() for k in KEYS], list(sec['content'].keys()))
        await pg.click("#sec_u6 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u6')
        ok('C · while the database still expects 4 boxes, sending is refused', m.startswith('Complete every box'), m)
        await pg.evaluate("(()=>{const d=JSON.parse(localStorage.getItem('fakedb'));d.box_count.u6=2;localStorage.setItem('fakedb',JSON.stringify(d));})()")
        await pg.click("#sec_u6 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u6')
        ok('C · once the database expects 2 boxes, the section goes for team confirmation', m.startswith('Sent for team confirmation.'), m)
        await pg.evaluate("localStorage.setItem('fake_uid','u-2')")
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1200); await pg.evaluate("capToggle('u6')")
        await pg.click("#sec_u6 .actions .btn.primary"); await pg.wait_for_timeout(900)
        ok('C · when the teammate confirms, the section is Agreed', await pg.evaluate("document.querySelector('#sec_u6 .chip').textContent") == 'Agreed')
        if shots: await pg.screenshot(path=os.path.join(shots, 'capstone_u6.png'), full_page=True)

        await pg.evaluate("localStorage.setItem('fake_uid','u-1')")
        await pg.goto(O + '/collection.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        ch = await pg.evaluate("(()=>{const e=document.getElementById('ch-u3m1_lens5');return e?e.innerText:'';})()")
        ok('D · the Learning Portfolio has a Unit 6 chapter with the four reflections', all(('My answer for ' + r) in ch for r in REFS), ch[:400])
        answers = ch.split('UNIT SUMMARY')[0]
        gone = ['Group entry', 'FACES entry', 'Enterprise PM System', 'cm_map', 'cm_record', '__cm_work', 'Confirmed by the group']
        ok('D · the group work is left out of the Learning Portfolio', not any(g in answers for g in gone), [g for g in gone if g in answers])
        ok('D · each reflection shows under its question', all(q in ch for q in ['Think of a recurring performance shortfall', 'Choose one enterprise Key Result in your own organisation', 'which FACES function is weakest', 'What is the current PM architecture']))
        ok('no page error', not errs, errs[:5])
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
