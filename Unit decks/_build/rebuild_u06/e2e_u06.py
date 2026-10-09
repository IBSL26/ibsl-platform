# -*- coding: utf-8 -*-
"""Unit 6 end to end, on the real pages with a stand-in database (nothing touches the live site or Supabase).
   The real participant page saves through the real s2r-save.js; the real Capstone page and the real Learning Portfolio page then read what was saved.
   Usage: python3 e2e_u06.py <site folder> <fake-supabase.js> [<screenshot folder>]"""
import sys, os, json, asyncio, mimetypes
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from playwright.async_api import async_playwright
import u6_content as C
site, fake = sys.argv[1], sys.argv[2]; shots = sys.argv[3] if len(sys.argv) > 3 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)) if (extra and not cond) else '')
FL = C.fields(); NAMES = [x[2] for x in C.PARTS]; KEYS = [x[3] for x in C.PARTS]
REFS = ['ref1', 'ref2', 'ref3', 'ref4', 'ref11', 'ref6', 'ref7', 'ref12']
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
    'box_count': {'u6': 5},
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
        dialogs = []
        def on_dialog(d): dialogs.append(d.message); asyncio.ensure_future(d.accept())
        pg.on('dialog', on_dialog)
        await pg.goto(O + '/blank.html')
        await pg.evaluate("(s)=>{localStorage.clear();localStorage.setItem('fakedb',JSON.stringify(s));localStorage.setItem('fake_uid','u-1');}", SEED)
        async def dbx(): return json.loads(await pg.evaluate("localStorage.getItem('fakedb')"))
        def u6rows(d): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == 'u3m1_lens5' and r['profile_id'] == 'u-1'}

        # ───────────── A · Capstone before anything is confirmed ─────────────
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(900)
        ok('A · Capstone page opens for the member, Unit 6 section is a Draft', 'Team Test' in await pg.inner_text('#root') and await pg.evaluate("document.querySelector('#sec_u6 .chip').textContent") == 'Draft')
        labels = await pg.evaluate("[...document.querySelectorAll('#sec_u6 .box-l')].map(e=>e.textContent)")
        ok('A · Unit 6 section shows four boxes, 6A to 6D', [l[:2] for l in labels] == ['6A', '6B', '6C', '6D'], labels)
        await pg.evaluate("capToggle('u6')"); await pg.click("#sec_u6 .pull .btn"); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#msg_u6')
        ok('A · nothing is brought in while the group has not confirmed on the Unit 6 page', m.startswith('Nothing is confirmed on your Unit 6 page yet.'), m)
        ok('A · the four boxes are still empty', await pg.evaluate("[...document.querySelectorAll('#sec_u6 textarea.box-ta')].every(t=>t.value==='')"))

        # ───────────── B · the real Unit 6 participant page ─────────────
        await pg.goto(O + '/unit3_m1_lens5_p.html'); await pg.wait_for_timeout(1200)
        ok('B · the real Unit 6 page opens unlocked through the real save helper', await pg.evaluate("getComputedStyle(document.getElementById('p-lock-overlay')).display") == 'none' and await pg.evaluate("typeof S2R.submit") == 'function')
        for rid in REFS:
            await pg.evaluate("(id)=>{const e=document.getElementById(id);const m=e.closest('[id^=mod]');showMod(parseInt(m.id.slice(3),10),null);e.closest('.acc').classList.add('open');}", rid)
            if rid == 'ref1':
                n = await pg.evaluate("document.querySelectorAll('.score-sel[data-key=ref1]').length")
                for i in range(n): await pg.select_option('.score-sel[data-key="ref1"][data-idx="%d"]' % i, str(1 + i % 5))
                await pg.fill('.score-notes[data-key="ref1"]', 'My answer for ref1')
            else:
                await pg.fill('#' + rid, 'My answer for ' + rid)
            await pg.evaluate("(id)=>document.getElementById(id).closest('.ref-block').querySelector('button').click()", rid)
            await pg.wait_for_timeout(150)
        await pg.wait_for_timeout(1500)
        rows = u6rows(await dbx())
        ok('B · the eight personal reflections are saved in the database under the member', all(isinstance(rows.get(r), str) and ('My answer for ' + r) in rows[r] for r in REFS), {r: rows.get(r) for r in REFS})
        await pg.evaluate("showMod(4,null)"); await pg.wait_for_timeout(500)
        opts = await pg.evaluate("[...document.querySelectorAll('#u6_kr1 option')].map(o=>o.value).filter(Boolean)")
        ok('B · Step 4 lists the four Key Results the group confirmed in Unit 3', len(opts) == 4, opts)
        for i in range(4):
            await pg.click('#mod4 .step-tab >> nth=%d' % i); await pg.wait_for_timeout(120)
            for f in [x for x in FL if x[2] == C.PARTS[i][0]]:
                if f[4] == 't': await pg.fill('#u6_' + f[0], 'Group entry for ' + f[0])
                elif f[4] == 'k': await pg.select_option('#u6_' + f[0], opts[0 if f[0] == 'kr1' else 2])
                else: await pg.fill('#u6_' + f[0], '40' if f[0].endswith('kr1_w') else '20')
        await pg.wait_for_timeout(1500)
        rows = u6rows(await dbx())
        ok('B · the group work saves while it is typed, before Confirm', isinstance(rows.get('__pm_work'), dict) and len(rows['__pm_work']) == len(FL) and isinstance(rows.get('pm_record'), str), list(rows.keys()))
        ok('B · before Confirm nothing is marked as confirmed', not any(nm in (rows.get('confirmed_items') or []) for nm in NAMES), rows.get('confirmed_items'))
        await pg.click('#u6ConfBtn'); await pg.wait_for_timeout(1200)
        rows = u6rows(await dbx())
        ok('B · Confirm saves the four parts as text: pm_scoring, pm_faces, pm_execution, pm_scorecards', all(isinstance(rows.get(k), str) and len(rows[k]) > 50 for k in KEYS), await pg.inner_text('#u6Msg'))
        ok('B · Confirm saves the four names in confirmed_items as a list', isinstance(rows.get('confirmed_items'), list) and all(nm in rows['confirmed_items'] for nm in NAMES), rows.get('confirmed_items'))
        if shots: await pg.screenshot(path=os.path.join(shots, '1_unit6_confirmed.png'), full_page=True)
        # Send to facilitator (this is what the Learning Portfolio reads)
        await pg.evaluate("sendToFacilitator()"); await pg.wait_for_timeout(900)
        d = await dbx(); subs = [s for s in d['submissions'] if s['lens_id'] == 'u3m1_lens5']
        ok('B · Send to Facilitator stores one submission for Unit 6', len(subs) == 1 and subs[0]['profile_id'] == 'u-1', dialogs[-2:])
        resp = subs[0]['payload']['responses'] if subs else {}
        ok('B · the submission carries the reflections and the group work together', all(r in resp for r in REFS) and all(k in resp for k in KEYS + ['pm_record', '__pm_work', 'confirmed_items']), sorted(resp.keys()))

        # ───────────── C · Capstone: the group's page ─────────────
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u6'][0]
        ok('C · on opening, the Capstone brings the Unit 6 work in and saves it on the team’s Blueprint', sorted(sec['content'].keys()) == ['6A', '6B', '6C', '6D'], sec['content'].keys())
        ok('C · 6A holds the scoring logic, 6B FACES, 6C EXECUTION, 6D the scorecards, word for word',
           [sec['content'].get(bx) for bx in ('6A', '6B', '6C', '6D')] == [rows[k].strip() for k in KEYS])
        m = await pg.inner_text('#msg_u6')
        ok('C · the page says so', m.startswith('Brought in from your Unit 6 page and saved as a draft.'), m)
        shown = await pg.evaluate("[...document.querySelectorAll('#sec_u6 textarea.box-ta')].map(t=>t.value)")
        ok('C · the four boxes show the text on screen', shown == [rows[k].strip() for k in KEYS] and 'Rating 1' in shown[0] and 'PM scorecard · CEO' in shown[3], [s[:60] for s in shown])
        ok('C · 6D carries the two chosen Key Results', ('Key Result 1: ' + opts[0]) in shown[3] and ('Key Result 2: ' + opts[2]) in shown[3], shown[3][:300])
        if shots: await pg.screenshot(path=os.path.join(shots, '2_capstone_brought_in.png'), full_page=True)
        # the database still expects 5 boxes until the SQL is run
        await pg.click("#sec_u6 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u6')
        ok('C · while the database still expects 5 boxes, sending is refused', m.startswith('Complete every box before sending for confirmation.'), m)
        await pg.evaluate("(()=>{const d=JSON.parse(localStorage.getItem('fakedb'));d.box_count.u6=4;localStorage.setItem('fakedb',JSON.stringify(d));})()")
        await pg.click("#sec_u6 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u6')
        ok('C · once the database expects 4 boxes, the section goes for team confirmation', m.startswith('Sent for team confirmation.'), m)
        # a teammate
        await pg.evaluate("localStorage.setItem('fake_uid','u-2')")
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1200); await pg.evaluate("capToggle('u6')")
        seen = await pg.evaluate("[...document.querySelectorAll('#sec_u6 .box-v')].map(e=>e.textContent)")
        ok('C · a teammate sees the same four texts on the team’s Blueprint', seen == [rows[k].strip() for k in KEYS], [s[:50] for s in seen])
        await pg.click("#sec_u6 .actions .btn.primary"); await pg.wait_for_timeout(900)
        ok('C · when the teammate confirms, the Unit 6 section is Agreed', await pg.evaluate("document.querySelector('#sec_u6 .chip').textContent") == 'Agreed', await pg.inner_text('#msg_u6'))
        if shots: await pg.screenshot(path=os.path.join(shots, '3_capstone_agreed.png'), full_page=True)

        # ───────────── D · Learning Portfolio ─────────────
        await pg.evaluate("localStorage.setItem('fake_uid','u-1')")
        await pg.goto(O + '/collection.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        ch = await pg.evaluate("(()=>{const e=document.getElementById('ch-u3m1_lens5');return e?e.innerText:'';})()")
        ok('D · the Learning Portfolio opens with a Unit 6 chapter', 'Performance Management Setup' in ch, (await pg.inner_text('body'))[:300])
        ok('D · the eight personal reflections are in it', all(('My answer for ' + r) in ch for r in REFS), [r for r in REFS if ('My answer for ' + r) not in ch])
        Q = ['Biggest gap & what closing it would change', 'which rating most accurately reflects the performance standard', 'Which of the four bridge functions is most underdeveloped',
             'Where would you honestly place your current PM system', 'Does your current PM system distinguish between the evaluation of the team or individual', 'Having explored your hot zone',
             'Which of the three Execution Gaps is most present', 'What is the current PM architecture of your organisation?']
        ok('D · each reflection shows under its own question', all(q in ch for q in Q), [q for q in Q if q not in ch])
        gone = ['Group entry for', 'PM Architecture', 'PM scorecard', 'Rating 1 · Poor', 'confirmed_items', 'Confirmed by the group', 'pm_record', 'pm_scoring', 'Pm Record', 'Pm Scoring', '__pm_work', 'Key Result 1']
        answers = ch.split('UNIT SUMMARY')[0]
        ok('D · the group work is left out of the Learning Portfolio', not any(g in answers for g in gone), [g for g in gone if g in answers])
        ok('D · the FACES scores of reflection 1.2 show with the note', all(x in answers for x in ('F (Foster a Results Culture): 1', 'S (Support Continuous Development): 5')))
        ok('D · nothing else sits among the answers: eight answers, eight questions', answers.count('My answer for ') == 8, answers.count('My answer for '))
        if shots: await pg.locator('#ch-u3m1_lens5').screenshot(path=os.path.join(shots, '4_portfolio_unit6.png'))
        print('--- Unit 6 chapter as the Learning Portfolio shows it ---'); print(ch[:2600])
        ok('no page error in any of the pages', not errs, errs[:5])
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
