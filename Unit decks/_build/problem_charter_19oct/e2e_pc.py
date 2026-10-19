# -*- coding: utf-8 -*-
"""Unit 1 part 6.2 · Problem Charter, end to end on the real pages with a stand-in database.
   Usage: python3 e2e_pc.py <site folder> <fake-supabase.js> [<screenshot folder>]"""
import sys, os, json, asyncio, mimetypes
from playwright.async_api import async_playwright
site, fake = sys.argv[1], sys.argv[2]; shots = sys.argv[3] if len(sys.argv) > 3 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)[:400]) if (extra and not cond) else '')
O = 'http://portal.test'
BOXES = ['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', '1I', '1J', '1K']
KEYS = ['pc_company', 'pc_team', 'pc_org', 'pc_reality', 'pc_challenges', 'pc_manifest', 'pc_consequences', 'pc_capabilities', 'pc_shared', 'pc_problem', 'pc_sources']
TEXT = ['company', 'sector', 'size', 'activity', 'results', 'challenges', 'manifest', 'consequences', 'capabilities', 'design', 'execution', 'sustain', 'problem', 'sources']
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Member Two'}],
    'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'u-2', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
    'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': 'u1_foundations', 'status': 'unlocked'}],
    'lens_responses': [], 'submissions': [],
    'lens_catalog': [{'id': 'u1_foundations', 'unit': 1, 'module': 1, 'sequence': 0, 'title': 'Behavioural Strategy Fundamentals', 'requires_lens': None}],
    'box_count': {'u1': 11},
    'capstone': {'brief': {'case_name': None, 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'Test cohort'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                 'members': [{'profile_id': 'u-1', 'full_name': 'Member One'}, {'profile_id': 'u-2', 'full_name': 'Member Two'}],
                 'sections': [{'key': 'u%d' % n, 'open': n == 1, 'status': 'draft', 'content': {}, 'confirmations': []} for n in range(1, 13)]}}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
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
        def rows(d): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == 'u1_foundations' and r['profile_id'] == 'u-1'}

        # A · Capstone before the Charter
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(900)
        first = await pg.evaluate("document.querySelector('.sec .sec-t').textContent")
        ok('A · the Blueprint opens with Unit 1 · Problem Charter', first == 'Unit 1 · Problem Charter', first)
        labels = await pg.evaluate("[...document.querySelectorAll('#sec_u1 .box-l')].map(e=>e.textContent.slice(0,2))")
        ok('A · the Unit 1 section has eleven boxes, 1A to 1K', labels == BOXES, labels)
        ok('A · with no Charter yet, the boxes name "your simulated company"', 'executive team of your simulated company' in await pg.evaluate("document.getElementById('sec_u1').textContent"))
        ok('A · the page counts 12 sections', '0 of 12 sections agreed.' in await pg.inner_text('#root'))
        ok('A · no cohort case name on the brief card', 'Old Case' not in await pg.inner_text('#root'))

        # B · the real Unit 1 page
        await pg.goto(O + '/unit1_P.html'); await pg.wait_for_timeout(1300)
        await pg.evaluate("showMod(5)"); await pg.wait_for_timeout(300)
        ok('B · 6.2 The Problem Charter sits after 6.1 in Section 6', await pg.evaluate("(()=>{const t=[...document.querySelectorAll('#mod5 .acc-t')].map(e=>e.textContent);return t.indexOf('6.2 — The Problem Charter')===t.indexOf('6.1 — Self Reflection Bias Assessment')+1;})()"))
        ok('B · five step tabs', await pg.evaluate("document.querySelectorAll('#pcTool .pc-tab').length") == 5)
        ok('B · ten executive team rows, each with the ten roles', await pg.evaluate("document.querySelectorAll('#pcTool select[id^=pc_role_]').length") == 10 and await pg.evaluate("document.querySelectorAll('#pc_role_0 option').length") == 11)
        # partly fill, then try to confirm
        await pg.fill('#pc_company', 'Kafue Agro Holdings')
        await pg.select_option('#pc_role_0', 'CEO'); await pg.fill('#pc_name_0', 'Member One')
        await pg.select_option('#pc_role_1', 'CEO'); await pg.fill('#pc_name_1', 'Member Two')
        await pg.evaluate("pcStep(4)"); await pg.wait_for_timeout(500)
        await pg.click('#pcConfBtn'); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#pcMsg')
        ok('B · Confirm is refused while entries are open, and names what is open', m.startswith('Before you confirm, complete:') and 'Step 2' in m, m)
        ok('B · Confirm names a role held twice', 'CEO appears more than once' in m, m)
        await pg.evaluate("pcStep(0)")
        await pg.select_option('#pc_role_1', 'CFO')
        await pg.select_option('#pc_role_2', 'COO')   # a role without a name
        for i, fid in enumerate(TEXT):
            await pg.evaluate("(n)=>pcStep(n)", ([0]*5 + [1]*4 + [2]*3 + [3]*2)[i])
            if fid != 'company': await pg.fill('#pc_' + fid, 'Group entry for ' + fid)
        await pg.evaluate("pcStep(4)"); await pg.wait_for_timeout(400)
        await pg.click('#pcConfBtn'); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#pcMsg')
        ok('B · a role without a name is caught', 'a role without a name' in m, m)
        await pg.evaluate("pcStep(0)"); await pg.select_option('#pc_role_2', ''); await pg.evaluate("pcStep(4)")
        await pg.wait_for_timeout(1500)
        r = rows(await dbx())
        ok('B · the group work saves while it is typed (__pc_work, pc_record)', isinstance(r.get('__pc_work'), dict) and isinstance(r.get('pc_record'), str) and 'KAFUE' not in r['pc_record'] and 'Kafue Agro Holdings' in r['pc_record'], list(r.keys()))
        ok('B · nothing confirmed yet', not r.get('confirmed_items'))
        await pg.click('#pcConfBtn'); await pg.wait_for_timeout(1500)
        r = rows(await dbx())
        ok('B · Confirm saves the eleven Capstone texts', all(isinstance(r.get(k), str) and r[k].strip() for k in KEYS), await pg.inner_text('#pcMsg'))
        ok('B · pc_company is the name alone, pc_team lists role · member', r.get('pc_company') == 'Kafue Agro Holdings' and r.get('pc_team') == 'CEO · Member One\nCFO · Member Two', [r.get('pc_company'), r.get('pc_team')])
        ok('B · pc_shared carries the three areas', r.get('pc_shared', '').startswith('Strategy design: Group entry for design\nStrategy execution:'), r.get('pc_shared'))
        ok('B · the eleven names are in confirmed_items', isinstance(r.get('confirmed_items'), list) and len([x for x in r['confirmed_items'] if x.startswith('Problem Charter · ')]) == 11, r.get('confirmed_items'))
        ok('B · the record shows Confirmed', 'Confirmed' in await pg.inner_text('#pcRec'))
        if shots:
            await pg.evaluate("pcStep(0)"); await pg.wait_for_timeout(300)
            el = await pg.query_selector('#pcTool'); acc = await el.evaluate_handle("e=>e.closest('.acc')")
            await acc.as_element().screenshot(path=os.path.join(shots, '1_unit1_62_step1.png'))
            await pg.evaluate("pcStep(4)"); await pg.wait_for_timeout(300)
            await pg.evaluate("document.querySelectorAll('#pcRec details').forEach(d=>d.open=true)")
            await (await pg.query_selector('#pcTool')).screenshot(path=os.path.join(shots, '2_unit1_62_record.png'))
        # an edit after Confirm takes the names out again
        await pg.evaluate("pcStep(1)"); await pg.fill('#pc_manifest', 'Group entry for manifest, revised'); await pg.wait_for_timeout(1500)
        r2 = rows(await dbx())
        ok('B · an edit after Confirm takes the names out again', not any(x.startswith('Problem Charter · ') for x in (r2.get('confirmed_items') or [])), r2.get('confirmed_items'))
        await pg.evaluate("pcStep(4)"); await pg.click('#pcConfBtn'); await pg.wait_for_timeout(1500)
        r = rows(await dbx())
        ok('B · Confirm again restores them', len([x for x in r['confirmed_items'] if x.startswith('Problem Charter · ')]) == 11)
        # reload keeps everything
        await pg.reload(); await pg.wait_for_timeout(1500)
        ok('B · after reload the entries come back', await pg.input_value('#pc_company') == 'Kafue Agro Holdings' and await pg.input_value('#pc_name_1') == 'Member Two' and await pg.evaluate("document.getElementById('pc_role_1').value") == 'CFO')
        ok('B · the portfolio artefact and 6.1 are still on the page', await pg.evaluate("!!document.getElementById('port_1')&&!!document.getElementById('s1_1')"))

        # C · Capstone brings the Charter in
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1600)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u1'][0]
        ok('C · the Capstone brings the Charter in as boxes 1A to 1K', sorted(sec['content'].keys()) == BOXES, sec['content'].keys())
        ok('C · word for word', [sec['content'][bx] for bx in BOXES] == [r[k].strip() for k in KEYS])
        intro = await pg.inner_text('#introText')
        ok('C · the page names the team’s simulated company', 'Kafue Agro Holdings' in intro, intro)
        ok('C · the boxes use the company name for [Case]', 'executive team of Kafue Agro Holdings' in await pg.evaluate("document.getElementById('sec_u1').textContent"))
        ok('C · the assessment criteria name the Problem Charter', 'Problem Charter' in await pg.inner_text('.crit-group'))
        await pg.click("#sec_u1 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u1')
        ok('C · the Unit 1 section goes for team confirmation', m.startswith('Sent for team confirmation.'), m)
        if shots: await pg.screenshot(path=os.path.join(shots, '3_capstone_unit1.png'), full_page=False)
        await pg.evaluate("localStorage.setItem('fake_uid','u-2')")
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1200); await pg.evaluate("capToggle('u1')")
        await pg.click("#sec_u1 .actions .btn.primary"); await pg.wait_for_timeout(900)
        ok('C · when the teammate confirms, the Problem Charter is Agreed', await pg.evaluate("document.querySelector('#sec_u1 .chip').textContent") == 'Agreed')

        ok('Z · no script errors on the pages', not errs, errs[:5])
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
