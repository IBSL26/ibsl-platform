# -*- coding: utf-8 -*-
"""Unit 7 end to end, on the real pages with a stand-in database (nothing touches the live site or Supabase).
   The real participant page saves through the real s2r-save.js; the real Capstone page and the real Learning Portfolio page then read what was saved.
   Usage: python3 e2e_u07.py <site folder> <fake-supabase.js> [<screenshot folder>]
   The site folder holds unit3_m1_lens6_p.html, s2r-save.js, capstone_P.html and collection.html. fake-supabase.js is the one in rebuild_u06."""
import sys, os, json, asyncio, mimetypes, re
from playwright.async_api import async_playwright
import build_u07pv as C
site, fake = sys.argv[1], sys.argv[2]; shots = sys.argv[3] if len(sys.argv) > 3 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)) if (extra and not cond) else '')
FL = C.fields(); NAMES = [x[2] for x in C.PARTS]; KEYS = [x[3] for x in C.PARTS]
MAPKR = 'Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027'
CM = {'kr_obj': 'Deliver consistently fast and effortless service experiences for customers', 'kr': MAPKR, 'f1_name': 'Customer Service', 'f1_contrib': 'Resolve requests within the standard', 'f1_hos': 'Agents own each case', 'f1_hosm': 'Share answered within 4 hours', 'f1_esrg': 'Case routing that shows case age', 'f1_esrgm': 'Daily age report', 'f2_name': 'Information Technology', 'f2_contrib': 'Keep routing reliable', 'f3_name': 'Operations', 'f3_contrib': 'Staff peak demand'}; BOXES = ['7A', '7B', '7C', '7D', '7E']
REFS = ['ref1', 'ref2', 'ref3', 'ref8', 'ref4', 'ref5', 'ref6']
AD = ['ad_goal', 'ad_reality', 'ad_options', 'ad_will']
LENS = 'u3m1_lens6'
O = 'http://portal.test'
OKR = {'items': [
    {'theme': 'Customer responsiveness', 'obj': 'Deliver consistently fast and effortless service experiences for customers', 'krs': [{'t': 'Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027'}, {'t': 'Increase customer requests resolved at first contact from 60% to 85% by 30 September 2027'}]},
    {'theme': 'Value creation', 'obj': 'Strengthen enterprise performance through scalable and efficient operations', 'krs': [{'t': 'Improve operating margin from 14% to 18% by 31 December 2027'}, {'t': 'Reduce leadership time spent on low-value projects from 25% to 10% by 30 June 2027'}]}]}
SIP = [('sip_d1_st', 'SiP · Customer Experience & Value', 'Customers get a fast, effortless answer the first time they contact us.'),
       ('sip_d2_st', 'SiP · Operational Capability & Execution Rhythm', 'Teams resolve requests inside one working rhythm.'),
       ('sip_d3_st', 'SiP · People & Culture Dynamics', 'People own enterprise priorities together.'),
       ('sip_d4_st', 'SiP · Enterprise Value Creation', 'Margin grows from efficient operations.')]
def row(lens, key, value): return {'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': lens, 'response_key': key, 'value': value}
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Member Two'}],
    'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'u-2', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
    'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': LENS, 'status': 'unlocked'}],
    'lens_responses': [row('u2m1_lens2', '__okr_work', OKR), row('u2m1_lens2', 'confirmed_items', ['Enterprise priorities', 'Enterprise OKRs'])] +
                      [row('u2m1_lens1', k, t) for k, _, t in SIP] + [row('u2m1_lens1', 'confirmed_items', [n for _, n, _ in SIP])] +
                      [row('u3m1_lens5', '__cm_work', CM), row('u3m1_lens5', 'confirmed_items', ['Enterprise PM System · Contribution Map', 'Enterprise PM System · FACES Application'])],
    'submissions': [],
    'lens_catalog': [{'id': 'u3m1_lens5', 'unit': 6, 'module': 3, 'sequence': 5, 'title': 'Performance Management Setup', 'requires_lens': 'u3m1_lens4'},
                     {'id': LENS, 'unit': 7, 'module': 3, 'sequence': 6, 'title': 'Establishing Performance Expectations', 'requires_lens': 'u3m1_lens5'}],
    'box_count': {'u7': 5},
    'capstone': {'brief': {'case_name': 'Test Case Ltd', 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'Test cohort'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                 'members': [{'profile_id': 'u-1', 'full_name': 'Member One'}, {'profile_id': 'u-2', 'full_name': 'Member Two'}],
                 'sections': [{'key': 'u%d' % n, 'open': n == 7, 'status': 'draft', 'content': {}, 'confirmations': []} for n in range(2, 13)]}}

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
                if name == 'collection_control.html':   # control: the Learning Portfolio page with the Unit 7 line taken out
                    t = open(os.path.join(site, 'collection.html'), encoding='utf-8').read(); a = ", u3m1_lens6:/^(ex_(record|future|delivery|chain|ownership|dialogue)$|confirmed_items$)/i"
                    assert t.count(a) == 1; return await r.fulfill(body=t.replace(a, ''), content_type='text/html; charset=utf-8')
                if name == 'capstone_control.html':     # control: the Capstone page with the Unit 7 rows taken out
                    t = open(os.path.join(site, 'capstone_P.html'), encoding='utf-8').read(); m = re.search(r",\s*u7: \{ lens:'u3m1_lens6', rows:\[.*?\]\}", t, re.S)
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
        def u7rows(d): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == LENS and r['profile_id'] == 'u-1'}

        # ───────────── A · Capstone before anything is confirmed ─────────────
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(900)
        ok('A · Capstone page opens for the member, Unit 7 section is a Draft', 'Team Test' in await pg.inner_text('#root') and await pg.evaluate("document.querySelector('#sec_u7 .chip').textContent") == 'Draft')
        labels = await pg.evaluate("[...document.querySelectorAll('#sec_u7 .box-l')].map(e=>e.textContent)")
        ok('A · Unit 7 section shows five boxes, 7A to 7E', [l[:2] for l in labels] == BOXES, labels)
        ok('A · the boxes carry the new headings', all(h in ' | '.join(labels) for h in ('Start With the Future', 'Delivery expectation', 'Expectations chain', 'Ownership', 'Alignment dialogue with the board chair')), labels)
        await pg.evaluate("capToggle('u7')"); await pg.click("#sec_u7 .pull .btn"); await pg.wait_for_timeout(400)
        m = await pg.inner_text('#msg_u7')
        ok('A · nothing is brought in while the group has not confirmed on the Unit 7 page', m.startswith('Nothing is confirmed on your Unit 7 page yet.'), m)
        ok('A · the five boxes are still empty', await pg.evaluate("[...document.querySelectorAll('#sec_u7 textarea.box-ta')].every(t=>t.value==='')"))

        # ───────────── B · the real Unit 7 participant page ─────────────
        await pg.goto(O + '/unit3_m1_lens6_p.html'); await pg.wait_for_timeout(1500)
        ok('B · the real Unit 7 page opens unlocked through the real save helper', await pg.evaluate("getComputedStyle(document.getElementById('p-lock-overlay')).display") == 'none' and await pg.evaluate("typeof S2R.submit") == 'function')
        show = "(id)=>{const e=document.getElementById(id);const m=e.closest('[id^=mod]');showMod(parseInt(m.id.slice(3),10),null);e.closest('.acc').classList.add('open');}"
        for rid in REFS:
            await pg.evaluate(show, rid); await pg.fill('#' + rid, 'My answer for ' + rid); await pg.wait_for_timeout(120)
        await pg.evaluate(show, 'ad_kr')
        adk = await pg.evaluate("[...document.querySelectorAll('#ad_kr option')].map(o=>o.value).filter(Boolean)")
        ok('B · part 4.2 lists the four Key Results the group confirmed in Unit 3', len(adk) == 4, adk)
        await pg.select_option('#ad_kr', adk[3])
        for k in AD: await pg.fill('#' + k, 'My dialogue for ' + k); await pg.wait_for_timeout(120)
        await pg.wait_for_timeout(2200)
        rows = u7rows(await dbx())
        ok('B · the seven personal reflections are saved in the database under the member', all(rows.get(r) == 'My answer for ' + r for r in REFS), {r: rows.get(r) for r in REFS})
        ok('B · the Portfolio work of part 4.2 is saved: the Key Result and the four GROW boxes', rows.get('ad_kr') == adk[3] and all(rows.get(k) == 'My dialogue for ' + k for k in AD), {k: rows.get(k) for k in ['ad_kr'] + AD})
        await pg.evaluate("showMod(4,null)"); await pg.evaluate("document.querySelectorAll('#mod4 .acc').forEach((a,i)=>{if(i<2)a.classList.add('open')})"); await pg.wait_for_timeout(500)
        objs = await pg.evaluate("[...document.getElementById('u7_o1_fn').options].map(o=>o.value).filter(Boolean)")
        sips = await pg.evaluate("[...document.getElementById('u7_o1_sipst').options].map(o=>o.value).filter(Boolean)")
        ok('B · Section 5 lists the three functions of the Unit 6 Contribution Map and the four SiP statements of Unit 2', objs == ['Customer Service', 'Information Technology', 'Operations'] and len(sips) == 4, (objs, sips))
        setv = "([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event(e.tagName==='SELECT'?'change':'input',{bubbles:true}));}"
        chosen = {}
        for n in (1, 2):
            await pg.evaluate(setv, ['u7_o%d_fn' % n, objs[n - 1]]); await pg.wait_for_timeout(120)
            await pg.evaluate(setv, ['u7_o%d_sipst' % n, sips[n - 1]])
        dgk = await pg.evaluate("[...document.querySelectorAll('#u7_dg_kr option')].map(o=>o.value).filter(Boolean)")
        await pg.evaluate(setv, ['u7_dg_kr', dgk[2]])
        SCORES = {'o1_score': '7', 'o1_score2': '9', 'o2_score': '9'}
        for f in FL:
            if f[4] == 'k': continue
            if f[0] in SCORES: v = SCORES[f[0]]
            elif f[0].startswith('o2_') and f[4] in ('o', 'm'): continue      # first score 9: the three follow-up entries stay empty
            else: v = 'Group entry for ' + f[0]
            await pg.evaluate(setv, ['u7_' + f[0], v])
        await pg.wait_for_timeout(1800)
        rows = u7rows(await dbx())
        ok('B · the group work saves while it is typed, before Confirm', isinstance(rows.get('__ex_work'), dict) and len(rows['__ex_work']) == len(FL) == 59 and isinstance(rows.get('ex_record'), str), list(rows.keys()))
        ok('B · before Confirm nothing is marked as confirmed', not any(nm in (rows.get('confirmed_items') or []) for nm in NAMES), rows.get('confirmed_items'))
        await pg.click('#u7ConfBtn'); await pg.wait_for_timeout(1500)
        rows = u7rows(await dbx())
        ok('B · Confirm saves the five parts as text: ex_future, ex_delivery, ex_chain, ex_ownership, ex_dialogue', all(isinstance(rows.get(k), str) and len(rows[k]) > 50 for k in KEYS), await pg.inner_text('#u7Msg'))
        ok('B · Confirm saves the five names in confirmed_items as a list', isinstance(rows.get('confirmed_items'), list) and all(nm in rows['confirmed_items'] for nm in NAMES), rows.get('confirmed_items'))
        if shots: await pg.screenshot(path=os.path.join(shots, '1_unit7_confirmed.png'), full_page=True)
        await pg.evaluate("sendToFacilitator()"); await pg.wait_for_timeout(900)
        d = await dbx(); subs = [s for s in d['submissions'] if s['lens_id'] == LENS]
        ok('B · Submit to Facilitator stores one submission for Unit 7', len(subs) == 1 and subs[0]['profile_id'] == 'u-1', dialogs[-2:])
        resp = subs[0]['payload']['responses'] if subs else {}
        ok('B · the submission carries the reflections, the Portfolio work and the group work together', all(r in resp for r in REFS + ['ad_kr'] + AD) and all(k in resp for k in KEYS + ['ex_record', '__ex_work', 'confirmed_items']), sorted(resp.keys()))

        # ───────────── control: a Capstone page without the Unit 7 rows brings nothing in ─────────────
        await pg.goto(O + '/capstone_control.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u7'][0]
        ok('control · with the Unit 7 rows taken out of the Capstone page there is no bring-in', sec['content'] == {}, sec['content'])

        # ───────────── C · Capstone: the group's page ─────────────
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1500)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u7'][0]
        want = [rows[k].strip() for k in KEYS]
        ok('C · on opening, the Capstone brings the Unit 7 work in and saves it on the team’s Blueprint', sorted(sec['content'].keys()) == BOXES, sec['content'].keys())
        ok('C · 7A to 7D hold the four steps and 7E the alignment dialogue, word for word', [sec['content'].get(bx) for bx in BOXES] == want)
        m = await pg.inner_text('#msg_u7')
        ok('C · the page says so', m.startswith('Brought in from your Unit 7 page and saved as a draft.'), m)
        shown = await pg.evaluate("[...document.querySelectorAll('#sec_u7 textarea.box-ta')].map(t=>t.value)")
        ok('C · the five boxes show the text on screen', shown == want, [s[:60] for s in shown])
        ok('C · 7A names both contributions, the enterprise Key Result of the map, the SiP statement, the owner and the leader framing',
           all(x in shown[0] for x in ('CONTRIBUTION 1: ' + objs[0], 'CONTRIBUTION 2: ' + objs[1], 'Enterprise Key Result: ' + MAPKR, 'Success in Practice statement: ' + sips[0], 'Owner of the contribution: Group entry for o1_owner', 'Leader framing: Group entry for o2_frame')), shown[0][:500])
        ok('C · 7B holds the people and the ESRG entries', all(x in shown[1] for x in ('The behaviours expected: Group entry for o1_beh', 'Governance · what must be decided, and who owns it: Group entry for o2_gov')), shown[1][:400])
        ok('C · 7C holds the Crossline', 'Crossline · whose contributions are interdependent with this one: Group entry for o1_cross' in shown[2], shown[2][:400])
        ok('C · 7D gives the scores; the follow-up lines show only where the first score is below 9',
           'Alignment score (1 to 10): 7' in shown[3] and 'Revised alignment score (1 to 10): 9' in shown[3] and shown[3].count('What stands behind the score') == 1 and shown[3].count('Alignment score (1 to 10): 9') == 1, shown[3])
        ok('C · 7E carries the chosen Key Result and the four GROW entries', shown[4].startswith('Key Result: ' + dgk[2]) and all((g + ': Group entry for dg_' + g.lower()) in shown[4] for g in ('Goal', 'Reality', 'Options', 'Will')), shown[4])
        if shots: await pg.screenshot(path=os.path.join(shots, '2_capstone_brought_in.png'), full_page=True)
        await pg.click("#sec_u7 .actions .btn.primary"); await pg.wait_for_timeout(900)
        m = await pg.inner_text('#msg_u7')
        ok('C · with five boxes expected by the database, the section goes for team confirmation', m.startswith('Sent for team confirmation.'), m)
        await pg.evaluate("localStorage.setItem('fake_uid','u-2')")
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1200); await pg.evaluate("capToggle('u7')")
        seen = await pg.evaluate("[...document.querySelectorAll('#sec_u7 .box-v')].map(e=>e.textContent)")
        ok('C · a teammate sees the same five texts on the team’s Blueprint', seen == want, [s[:50] for s in seen])
        await pg.click("#sec_u7 .actions .btn.primary"); await pg.wait_for_timeout(900)
        ok('C · when the teammate confirms, the Unit 7 section is Agreed', await pg.evaluate("document.querySelector('#sec_u7 .chip').textContent") == 'Agreed', await pg.inner_text('#msg_u7'))
        if shots: await pg.screenshot(path=os.path.join(shots, '3_capstone_agreed.png'), full_page=True)

        # ───────────── D · Learning Portfolio ─────────────
        await pg.evaluate("localStorage.setItem('fake_uid','u-1')")
        await pg.goto(O + '/collection.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        # two headings in the chapter (Reflections, Practising the Alignment Dialogue) open closed on screen; on paper every heading prints open
        chapter = "(()=>{const e=document.getElementById('ch-u3m1_lens6');if(!e)return '';e.querySelectorAll('.collapsed').forEach(x=>x.classList.remove('collapsed'));return e.innerText;})()"
        heads = await pg.evaluate("[...document.querySelectorAll('#ch-u3m1_lens6 .response-module-heading')].map(e=>e.textContent)")
        ok('D · the Unit 7 chapter has two headings: Reflections and Practising the Alignment Dialogue', heads == ['Reflections', 'Practising the Alignment Dialogue'], heads)
        ch = await pg.evaluate(chapter)
        ok('D · the Learning Portfolio opens with a Unit 7 chapter', 'Establishing Performance Expectations' in ch, (await pg.inner_text('body'))[:300])
        ok('D · the seven personal reflections are in it', all(('My answer for ' + r) in ch for r in REFS), [r for r in REFS if ('My answer for ' + r) not in ch])
        Q = ['Was it set or established?', 'which of the three conditions do you most consistently confirm', 'Map your Expectations Chain', 'Write the Resolve question in your own words',
             'When your team hits an unexpected obstacle', 'Which of the five mechanisms is most absent', 'the most important expectation you have set but not yet established']
        ok('D · each reflection shows under its own question', all(q in ch for q in Q), [q for q in Q if q not in ch])
        ok('D · the Portfolio work of part 4.2 is in it: the Key Result and the four GROW answers', adk[3] in ch and all(('My dialogue for ' + k) in ch for k in AD), [k for k in AD if ('My dialogue for ' + k) not in ch])
        QA = ['The Key Result for which you may need an alignment dialogue with your board chair', 'Goal · what you say and ask to agree what a 10 looks like for your chair', 'Reality · the questions you ask to understand what stands behind your chair’s score',
              'Options · what you explore with your chair to resolve the metric and the timeframe', 'Will · what you and your chair agree to do, and how you confirm that your chair has reached a 10']
        ok('D · each part 4.2 answer shows under its own label', all(q in ch for q in QA), [q for q in QA if q not in ch])
        gone = ['Group entry for', 'CONTRIBUTION 1', 'Expectations ·', 'Alignment score', 'confirmed_items', 'Confirmed by the group', 'ex_record', 'ex_future', 'Ex Record', 'Ex Future', '__ex_work', 'Establishing Delivery Expectations']
        answers = ch.split('UNIT SUMMARY')[0]
        ok('D · the group work is left out of the Learning Portfolio', not any(g in answers for g in gone), [g for g in gone if g in answers])
        ok('D · nothing else sits among the answers: seven reflections and four dialogue answers', answers.count('My answer for ') == 7 and answers.count('My dialogue for ') == 4, (answers.count('My answer for '), answers.count('My dialogue for ')))
        if shots: await pg.locator('#ch-u3m1_lens6').screenshot(path=os.path.join(shots, '4_portfolio_unit7.png'))
        await pg.goto(O + '/collection_control.html?participantId=u-1'); await pg.wait_for_timeout(1500)
        chc = await pg.evaluate(chapter)
        ok('control · with the Unit 7 line taken out of the Learning Portfolio page the group work shows', 'Group entry for' in chc.split('UNIT SUMMARY')[0])
        print('--- Unit 7 chapter as the Learning Portfolio shows it ---'); print(ch[:3200])
        ok('no page error in any of the pages', not errs, errs[:5])
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
