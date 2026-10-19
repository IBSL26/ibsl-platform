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
BOXES = ['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H']
KEYS = ['pc_company', 'pc_team', 'pc_org', 'pc_challenges', 'pc_manifest', 'pc_consequences', 'pc_address', 'pc_problem']
TEXT = ['company', 'sector', 'size', 'activity', 'results', 'challenges', 'manifest', 'consequences', 'capabilities', 'design', 'execution', 'sustain', 'problem', 'sources']
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Member Two'}],
    'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'u-2', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
    'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': 'u1_foundations', 'status': 'unlocked'}],
    'lens_responses': [], 'submissions': [],
    'lens_catalog': [{'id': 'u1_foundations', 'unit': 1, 'module': 1, 'sequence': 0, 'title': 'Behavioural Strategy Fundamentals', 'requires_lens': None}],
    'box_count': {'u1': 8},
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
        ok('A · the Unit 1 section has eight boxes, 1A to 1H', labels == BOXES, labels)
        ok('A · with no Charter yet, the boxes name "your simulated company"', 'executive team of your simulated company' in await pg.evaluate("document.getElementById('sec_u1').textContent"))
        ok('A · the page counts 12 sections', '0 of 12 sections agreed.' in await pg.inner_text('#root'))
        ok('A · no cohort case name on the brief card', 'Old Case' not in await pg.inner_text('#root'))

        # B · the real Unit 1 page
        await pg.goto(O + '/unit1_P.html'); await pg.wait_for_timeout(1300)
        await pg.evaluate("showMod(5)"); await pg.wait_for_timeout(300)
        ok('B · 6.2 The Problem Charter sits after 6.1 in Section 6', await pg.evaluate("(()=>{const t=[...document.querySelectorAll('#mod5 .acc-t')].map(e=>e.textContent);return t.indexOf('6.2 — The Problem Charter')===t.indexOf('6.1 — Self Reflection Bias Assessment')+1;})()"))
        ok('B · four step tabs, Step 2 is Shared reality', await pg.evaluate("[...document.querySelectorAll('#pcTool .pc-tab')].map(t=>t.textContent).join('|')") == 'Step 1 · Company|Step 2 · Shared reality|Step 3 · Central problem|Charter record')
        ok('B · no strategy-to-results reality box in Step 1', await pg.evaluate("!document.getElementById('pc_results')"))
        ok('B · ten executive team rows, each with the ten roles', await pg.evaluate("document.querySelectorAll('#pcTool select[id^=pc_role_]').length") == 10 and await pg.evaluate("document.querySelectorAll('#pc_role_0 option').length") == 11)
        await pg.fill('#pc_company', 'Kafue Agro Holdings')
        for fid in ('sector', 'size', 'activity'): await pg.fill('#pc_' + fid, 'Group entry for ' + fid)
        await pg.select_option('#pc_role_0', 'CEO'); await pg.fill('#pc_name_0', 'Member One')
        await pg.select_option('#pc_role_1', 'CEO'); await pg.fill('#pc_name_1', 'Member Two')
        await pg.evaluate("pcStep(1)")
        for a in ('design', 'execution', 'sustain'):
            for j in range(3): await pg.fill('#pc_ch_%s_%d' % (a, j), '%s challenge %d' % (a, j + 1))
        await pg.fill('#pc_mf_behaviours_0', 'Behaviour scenario 1')
        await pg.evaluate("pcStep(3)"); await pg.wait_for_timeout(500)
        await pg.click('#pcConfBtn'); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#pcMsg')
        ok('B · Confirm refused: names the role held twice, the fourth challenge, two scenarios, consequences, the three choices, the problem',
           all(x in m for x in ['CEO appears more than once', 'at least four strategy design challenges (3 so far)', 'at least two scenarios for observable behaviours (1 so far)', 'consequences for strategy execution', 'three sustaining performance challenges to address (0 chosen)', 'central organisational problem']), m)
        await pg.evaluate("pcStep(0)"); await pg.select_option('#pc_role_1', 'CFO')
        await pg.evaluate("pcStep(1)")
        for a in ('design', 'execution', 'sustain'):
            for j in range(3, 5): await pg.fill('#pc_ch_%s_%d' % (a, j), '%s challenge %d' % (a, j + 1))
            await pg.fill('#pc_cq_' + a, 'Consequences in ' + a)
        for mf in ('behaviours', 'practices', 'conditions'):
            for j in range(2): await pg.fill('#pc_mf_%s_%d' % (mf, j), '%s scenario %d' % (mf, j + 1))
        await pg.evaluate("pcStep(2)"); await pg.wait_for_timeout(600)
        n = await pg.evaluate("document.querySelectorAll('#pc_pick_design input').length")
        ok('B · Step 3 lists the five strategy design challenges from Step 2 to choose from', n == 5, n)
        for a in ('design', 'execution', 'sustain'):
            for j in (0, 2, 4): await pg.check('#pc_pick_%s .pc-pick:nth-child(%d) input' % (a, j + 1)); await pg.wait_for_timeout(60)
        await pg.click('#pc_pick_design .pc-pick:nth-child(2) input'); await pg.wait_for_timeout(200)
        ok('B · a fourth choice is refused', await pg.evaluate("document.querySelectorAll('#pc_pick_design input:checked').length") == 3 and 'Choose three' in await pg.inner_text('#pc_pickmsg_design'))
        await pg.fill('#pc_problem', 'Our central problem')
        await pg.evaluate("pcStep(3)"); await pg.wait_for_timeout(1500)
        r = rows(await dbx())
        ok('B · the group work saves while it is typed (__pc_work, pc_record)', isinstance(r.get('__pc_work'), dict) and 'Kafue Agro Holdings' in (r.get('pc_record') or ''), list(r.keys()))
        ok('B · nothing confirmed yet', not r.get('confirmed_items'))
        await pg.click('#pcConfBtn'); await pg.wait_for_timeout(1500)
        r = rows(await dbx())
        ok('B · Confirm saves the eight Capstone texts', all(isinstance(r.get(k), str) and r[k].strip() for k in KEYS), await pg.inner_text('#pcMsg'))
        ok('B · pc_company is the name alone, pc_team lists role · member', r.get('pc_company') == 'Kafue Agro Holdings' and r.get('pc_team') == 'CEO · Member One\nCFO · Member Two', [r.get('pc_company'), r.get('pc_team')])
        ok('B · pc_challenges holds the three areas, five each', r['pc_challenges'].startswith('Strategy design\n1. design challenge 1') and r['pc_challenges'].count('\n5. ') == 3, r['pc_challenges'])
        ok('B · pc_address holds the three chosen per area', r['pc_address'] == 'Strategy design\n1. design challenge 1\n2. design challenge 3\n3. design challenge 5\n\nStrategy execution\n1. execution challenge 1\n2. execution challenge 3\n3. execution challenge 5\n\nSustaining performance\n1. sustain challenge 1\n2. sustain challenge 3\n3. sustain challenge 5', r['pc_address'])
        ok('B · pc_manifest has the three headings with their scenarios', r['pc_manifest'].startswith('Observable behaviours\nScenario 1: behaviours scenario 1') and 'Organisational conditions\nScenario 1' in r['pc_manifest'] and 'gaps' not in r['pc_manifest'].lower(), r['pc_manifest'])
        ok('B · pc_consequences per area', r['pc_consequences'] == 'Strategy design: Consequences in design\nStrategy execution: Consequences in execution\nSustaining performance: Consequences in sustain')
        ok('B · the eight names are in confirmed_items', isinstance(r.get('confirmed_items'), list) and len([x for x in r['confirmed_items'] if x.startswith('Problem Charter · ')]) == 8, r.get('confirmed_items'))
        ok('B · the record shows Confirmed', 'Confirmed' in await pg.inner_text('#pcRec'))
        if shots:
            for i, nm in ((0, '1_step1'), (1, '2_step2'), (2, '3_step3')):
                await pg.evaluate("(n)=>pcStep(n)", i); await pg.wait_for_timeout(300)
                await (await pg.query_selector('#pcTool')).screenshot(path=os.path.join(shots, nm + '.png'))
            await pg.evaluate("pcStep(3)"); await pg.wait_for_timeout(300)
            await pg.evaluate("document.querySelectorAll('#pcRec details').forEach(d=>d.open=true)")
            await (await pg.query_selector('#pcTool')).screenshot(path=os.path.join(shots, '4_record.png'))
        # an edit after Confirm takes the names out again
        await pg.evaluate("pcStep(1)"); await pg.fill('#pc_cq_design', 'Consequences revised'); await pg.wait_for_timeout(1500)
        r2 = rows(await dbx())
        ok('B · an edit after Confirm takes the names out again', not any(x.startswith('Problem Charter · ') for x in (r2.get('confirmed_items') or [])), r2.get('confirmed_items'))
        await pg.evaluate("pcStep(3)"); await pg.click('#pcConfBtn'); await pg.wait_for_timeout(1500)
        r = rows(await dbx())
        ok('B · Confirm again restores them', len([x for x in r['confirmed_items'] if x.startswith('Problem Charter · ')]) == 8)
        # reload keeps everything
        await pg.reload(); await pg.wait_for_timeout(1500)
        ok('B · after reload the entries come back', await pg.input_value('#pc_company') == 'Kafue Agro Holdings' and await pg.input_value('#pc_name_1') == 'Member Two' and await pg.evaluate("document.getElementById('pc_role_1').value") == 'CFO' and await pg.evaluate("document.querySelectorAll('#pc_pick_execution input:checked').length") == 3)
        ok('B · the portfolio artefact and 6.1 are still on the page', await pg.evaluate("!!document.getElementById('port_1')&&!!document.getElementById('s1_1')"))

        # C · Capstone brings the Charter in
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1600)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u1'][0]
        ok('C · the Capstone brings the Charter in as boxes 1A to 1H', sorted(sec['content'].keys()) == BOXES, sec['content'].keys())
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
