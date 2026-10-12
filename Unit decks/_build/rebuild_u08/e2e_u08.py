# -*- coding: utf-8 -*-
"""Unit 8 end to end, on the real pages with a stand-in database (nothing touches the live site or Supabase).
   Usage: python3 e2e_u08.py <site folder> <fake-supabase.js> [<screenshot folder>]
   The site folder holds unit3_m2_lens7_p.html, s2r-save.js, capstone_P.html and collection.html. fake-supabase.js is the one in rebuild_u06."""
import sys, os, json, asyncio, mimetypes, re
from playwright.async_api import async_playwright
import u8_content as C
site, fake = sys.argv[1], sys.argv[2]; shots = sys.argv[3] if len(sys.argv) > 3 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)) if (extra and not cond) else '')
FL = C.fields(); NAMES = [x[2] for x in C.PARTS]; KEYS = [x[3] for x in C.PARTS]; BOXES = ['8A', '8B', '8C', '8D']
REFS = ['ref1', 'ref2', 'ref5', 'ref6', 'ref7']
RP = ['rp_review', 'app_rootcause', 'app_corrective', 'rp_judge']
LENS = 'u3m2_lens7'
O = 'http://portal.test'
def row(lens, key, value): return {'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': lens, 'response_key': key, 'value': value}
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Member Two'}],
    'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'u-2', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
    'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': LENS, 'status': 'unlocked'}],
    'lens_responses': [],
    'submissions': [],
    'lens_catalog': [{'id': 'u3m1_lens6', 'unit': 7, 'module': 3, 'sequence': 6, 'title': 'Establishing Performance Expectations', 'requires_lens': 'u3m1_lens5'},
                     {'id': LENS, 'unit': 8, 'module': 3, 'sequence': 7, 'title': 'Performance Measurement', 'requires_lens': 'u3m1_lens6'}],
    'box_count': {'u8': 4},
    'capstone': {'brief': {'case_name': 'Test Case Ltd', 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'Test cohort'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                 'members': [{'profile_id': 'u-1', 'full_name': 'Member One'}, {'profile_id': 'u-2', 'full_name': 'Member Two'}],
                 'sections': [{'key': 'u%d' % n, 'open': n == 8, 'status': 'draft', 'content': {}, 'confirmations': []} for n in range(2, 13)]}}

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
                if name == 'collection_control.html':
                    t = open(os.path.join(site, 'collection.html'), encoding='utf-8').read(); a = ", u3m2_lens7:/^(rd_(record|warning|accountability|learning|credibility)$|confirmed_items$)/i"
                    assert t.count(a) == 1; return await r.fulfill(body=t.replace(a, ''), content_type='text/html; charset=utf-8')
                if name == 'capstone_control.html':
                    t = open(os.path.join(site, 'capstone_P.html'), encoding='utf-8').read(); m = re.search(r",\s*u8: \{ lens:'u3m2_lens7', rows:\[.*?\]\}", t, re.S)
                    assert m; return await r.fulfill(body=t.replace(m.group(0), ''), content_type='text/html; charset=utf-8')
                f = os.path.join(site, name)
                if os.path.isfile(f): return await r.fulfill(path=f, content_type=(mimetypes.guess_type(f)[0] or 'text/html') + '; charset=utf-8')
                return await r.fulfill(status=404, body='')
            await r.abort()
        await ctx.route('**/*', route)
        pg = await ctx.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text and 'ERR_' not in m.text else None)
        dialogs = []
        def on_dialog(d): dialogs.append(d.message); asyncio.ensure_future(d.accept())
        pg.on('dialog', on_dialog)
        await pg.goto(O + '/blank.html')
        await pg.evaluate("(s)=>{localStorage.clear();localStorage.setItem('fakedb',JSON.stringify(s));localStorage.setItem('fake_uid','u-1');}", SEED)
        async def dbx(): return json.loads(await pg.evaluate("localStorage.getItem('fakedb')"))
        def u8rows(d): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == LENS and r['profile_id'] == 'u-1'}

        # A · Capstone before anything is confirmed
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(900)
        ok('A · Capstone page opens, Unit 8 section is a Draft', await pg.evaluate("document.querySelector('#sec_u8 .chip').textContent") == 'Draft')
        labels = await pg.evaluate("[...document.querySelectorAll('#sec_u8 .box-l')].map(e=>e.textContent)")
        ok('A · Unit 8 section shows four boxes, 8A to 8D', [l[:2] for l in labels] == BOXES, labels)
        ok('A · the boxes carry the new headings', all(h in ' | '.join(labels) for h in ('Early warning signals', 'Accountability', 'Organisational learning', 'Leadership credibility')), labels)
        await pg.evaluate("capToggle('u8')"); await pg.click("#sec_u8 .pull .btn"); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#msg_u8')
        ok('A · nothing is brought in before the group confirms on the Unit 8 page', m.startswith('Nothing is confirmed on your Unit 8 page yet.'), m)

        # B · the real Unit 8 participant page
        await pg.goto(O + '/unit3_m2_lens7_p.html'); await pg.wait_for_timeout(1500)
        ok('B · the real Unit 8 page opens unlocked through the real save helper', await pg.evaluate("typeof S2R.submit") == 'function')
        show = "(id)=>{const e=document.getElementById(id);const m=e.closest('[id^=mod]');showMod(parseInt(m.id.slice(3),10),null);e.closest('.acc').classList.add('open');const sp=e.closest('.step-panel');if(sp){sp.parentElement.querySelectorAll('.step-panel').forEach(x=>x.classList.remove('active'));sp.classList.add('active');}}"
        for rid in REFS + RP:
            await pg.evaluate(show, rid); await pg.fill('#' + rid, 'My answer for ' + rid); await pg.wait_for_timeout(120)
        await pg.evaluate(show, 'ref4_notes'); await pg.select_option('.score-sel[data-idx="0"]', '4'); await pg.fill('#ref4_notes', 'My gap note'); await pg.wait_for_timeout(1500)
        await pg.wait_for_timeout(1800)
        rows = u8rows(await dbx())
        ok('B · the five reflections and the four 4.2 answers are saved under the member', all(rows.get(r) == 'My answer for ' + r for r in REFS + RP), {r: rows.get(r) for r in REFS + RP})
        ok('B · the 3.1 rating and note are saved in ref4', 'Horizontal Coordination): 4' in str(rows.get('ref4')) and 'My gap note' in str(rows.get('ref4')), rows.get('ref4'))
        await pg.evaluate("showMod(4,null)"); await pg.wait_for_timeout(300)
        setv = "([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}"
        for f in FL: await pg.evaluate(setv, ['u8_' + f[0], 'If signal for ' + f[0] + ', then decision, taken by the CEO.'])
        await pg.wait_for_timeout(1800)
        rows = u8rows(await dbx())
        ok('B · the group work saves while it is typed, before Confirm', isinstance(rows.get('__rd_work'), dict) and len(rows['__rd_work']) == len(FL) == 8 and isinstance(rows.get('rd_record'), str), list(rows.keys()))
        ok('B · before Confirm nothing is marked as confirmed', not any(nm in (rows.get('confirmed_items') or []) for nm in NAMES))
        await pg.click('#u8ConfBtn'); await pg.wait_for_timeout(1500)
        rows = u8rows(await dbx())
        ok('B · Confirm saves the four parts as text', all(isinstance(rows.get(k), str) and 'Decision point 2:' in rows[k] for k in KEYS), await pg.inner_text('#u8Msg'))
        ok('B · Confirm saves the four names in confirmed_items', isinstance(rows.get('confirmed_items'), list) and all(nm in rows['confirmed_items'] for nm in NAMES), rows.get('confirmed_items'))
        await pg.evaluate("sendToFacilitator()"); await pg.wait_for_timeout(900)
        d = await dbx(); subs = [s for s in d['submissions'] if s['lens_id'] == LENS]
        ok('B · Submit to Facilitator stores one submission for Unit 8', len(subs) == 1, dialogs[-2:])
        resp = subs[0]['payload']['responses'] if subs else {}
        ok('B · the submission carries the reflections, the Portfolio work and the group work', all(r in resp for r in REFS + RP + ['ref4']) and all(k in resp for k in KEYS + ['confirmed_items']), sorted(resp.keys()))

        # control
        await pg.goto(O + '/capstone_control.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u8'][0]
        ok('control · with the Unit 8 rows taken out of the Capstone page there is no bring-in', sec['content'] == {}, sec['content'])

        # C · Capstone
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u8'][0]
        want = [rows[k].strip() for k in KEYS]
        ok('C · on opening, the Capstone brings the Unit 8 work in and saves it on the Blueprint', sorted(sec['content'].keys()) == BOXES, sec['content'].keys())
        ok('C · 8A to 8D hold the four sets of decision points, word for word', [sec['content'].get(bx) for bx in BOXES] == want)
        shown = await pg.evaluate("[...document.querySelectorAll('#sec_u8 textarea.box-ta')].map(t=>t.value)")
        ok('C · the four boxes show the text on screen', shown == want)
        await pg.click("#sec_u8 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u8')
        ok('C · with four boxes expected by the database, the section goes for team confirmation', m.startswith('Sent for team confirmation.'), m)
        await pg.evaluate("localStorage.setItem('fake_uid','u-2')")
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1200); await pg.evaluate("capToggle('u8')")
        await pg.click("#sec_u8 .actions .btn.primary"); await pg.wait_for_timeout(900)
        ok('C · when the teammate confirms, the Unit 8 section is Agreed', await pg.evaluate("document.querySelector('#sec_u8 .chip').textContent") == 'Agreed', await pg.inner_text('#msg_u8'))
        if shots: await pg.screenshot(path=os.path.join(shots, 'e2e_capstone_u8.png'), full_page=True)

        # D · Learning Portfolio
        await pg.evaluate("localStorage.setItem('fake_uid','u-1')")
        await pg.goto(O + '/collection.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        chapter = "(()=>{const e=document.getElementById('ch-u3m2_lens7');if(!e)return '';e.querySelectorAll('.collapsed').forEach(x=>x.classList.remove('collapsed'));return e.innerText;})()"
        heads = await pg.evaluate("[...document.querySelectorAll('#ch-u3m2_lens7 .response-module-heading')].map(e=>e.textContent)")
        ch = await pg.evaluate(chapter)
        ok('D · the Learning Portfolio has a Unit 8 chapter', 'Performance Measurement' in ch)
        ok('D · the reflections and the 4.2 answers are in it', all(('My answer for ' + r) in ch for r in REFS + RP), [r for r in REFS + RP if ('My answer for ' + r) not in ch])
        Q = ['what are you currently measuring that reflects activity', 'Which stage of the Review', 'what is your current percentage progress', 'early warning signals have emerged', 'one key execution learning', 'How did the CXO establish execution reality', 'Which root cause did the CXO diagnose']
        ok('D · each answer shows under its question or label', all(q in ch for q in Q), [q for q in Q if q not in ch])
        answers = ch.split('UNIT SUMMARY')[0]
        gone = ['If signal for', 'Decision point 1', 'Review Discipline ·', 'rd_', 'Confirmed by the group']
        ok('D · the group work is left out of the Learning Portfolio', not any(g in answers for g in gone), [g for g in gone if g in answers])
        print('headings:', heads)
        if shots: await pg.locator('#ch-u3m2_lens7').screenshot(path=os.path.join(shots, 'e2e_portfolio_u8.png'))
        await pg.goto(O + '/collection_control.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        chc = await pg.evaluate(chapter)
        ok('control · with the Unit 8 line taken out of the Learning Portfolio page the group work shows', 'If signal for' in chc.split('UNIT SUMMARY')[0])
        ok('no page error in any of the pages', not errs, errs[:5])
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
