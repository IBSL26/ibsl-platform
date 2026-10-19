# -*- coding: utf-8 -*-
"""Unit 2 capstone rework, end to end on the real pages with a stand-in database (19 Oct 2026).
   Two members of one team. Ann is the scribe; Ben sees her entries on his own page; both agree;
   the Capstone brings the three outputs in; Unit 3 brings the four SiP statements in.
   Usage: python3 e2e_u2cap.py <site folder> <fake-supabase-team.js> [<screenshot folder>]"""
import sys, os, json, asyncio, mimetypes
from playwright.async_api import async_playwright
site, fake = sys.argv[1], sys.argv[2]; shots = sys.argv[3] if len(sys.argv) > 3 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)[:300]) if (extra and not cond) else '')
O = 'http://portal.test'
L = 'u2m1_lens1'
PCN = ['Problem Charter · Simulated Company', 'Problem Charter · Executive Team', 'Problem Charter · Our Organisation', 'Problem Charter · Central Organisational Problem']
def pc_rows(uid):
    v = {'pc_company': 'Kafue Agro Holdings', 'pc_team': 'CEO: Ann\nCFO: Ben', 'pc_org': 'Agriculture · 900 staff · grain and inputs', 'pc_problem': 'Strategy stalls between head office and the farms.', 'confirmed_items': PCN}
    return [{'profile_id': uid, 'cohort_id': 'c-1', 'lens_id': 'u1_foundations', 'response_key': k, 'value': x} for k, x in v.items()]
SEED = {
    'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Ann Member'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Ben Member'}],
    'cohort_memberships': [{'profile_id': u, 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'} for u in ('u-1', 'u-2')],
    'capstone_individual': [{'team_id': 't-1', 'profile_id': u, 'cohort_id': 'c-1'} for u in ('u-1', 'u-2')],
    'lens_progress': [{'profile_id': u, 'cohort_id': 'c-1', 'lens_id': l, 'status': 'unlocked'} for u in ('u-1', 'u-2') for l in ('u1_foundations', L, 'u2m1_lens2')],
    'lens_responses': pc_rows('u-1') + pc_rows('u-2'), 'submissions': [],
    'lens_catalog': [{'id': L, 'unit': 2, 'module': 2, 'sequence': 1, 'title': 'Strategy Visioning', 'requires_lens': None}],
    'box_count': {'u1': 8, 'u2': 6},
    'capstone': {'brief': {'case_name': None, 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'Test cohort'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                 'members': [{'profile_id': 'u-1', 'full_name': 'Ann Member'}, {'profile_id': 'u-2', 'full_name': 'Ben Member'}],
                 'sections': [{'key': 'u%d' % n, 'open': n in (1, 2), 'status': 'agreed' if n == 1 else 'draft', 'content': {'1A': 'Kafue Agro Holdings'} if n == 1 else {}, 'confirmations': []} for n in range(1, 13)]}}

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
        def rows(d, uid, lens=L): return {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == lens and r['profile_id'] == uid}
        async def as_user(uid):
            await pg.evaluate("(u)=>localStorage.setItem('fake_uid',u)", uid)
            await pg.goto(O + '/unit2_m1_lens1_p.html'); await pg.wait_for_timeout(1500)

        # A · Section 4 is one worked example, read-only
        await as_user('u-1')
        await pg.evaluate("showMod(3)"); await pg.wait_for_timeout(200)
        t4 = await pg.inner_text('#mod3')
        ok('A · Section 4 titles: 4.1, 4.2, 4.3 on the worked example', await pg.evaluate("[...document.querySelectorAll('#mod3 .acc-t')].map(e=>e.textContent).join('|')") == '4.1 — Step 1: The Strategy Architecture|4.2 — Step 2: The Strategy Intent Statement|4.3 — Step 3: Success in Practice')
        ok('A · Section 4 has the 14 elements and the five headings of Kestrel Point Services', await pg.evaluate("document.querySelectorAll('#mod3 details.u2w-det').length") == 14 + 1 + 4 and 'Kestrel Point Services' in t4)
        ok('A · Section 4 has no entry box', await pg.evaluate("document.querySelectorAll('#mod3 textarea,#mod3 input,#mod3 select').length") == 0)
        ok('A · Section 4 never offers to generate anything', 'Generate' not in t4)

        # B · Section 5 opens on the Charter company, the group bar and the locked tool
        await pg.evaluate("showMod(4)"); await pg.wait_for_timeout(300)
        t5 = await pg.inner_text('#mod4')
        ok('B · 5.1 Role Contribution and 5.2 Collective Application are gone', 'Role Contribution' not in t5 and 'Collective Application' not in t5 and await pg.evaluate("!document.getElementById('col_alignment')&&!document.getElementById('appRoleSelP')"))
        ok('B · the Problem Charter company shows read-only', 'Kafue Agro Holdings' in await pg.inner_text('#u2bCharter'))
        ok('B · the group record bar lists both members', 'Ann Member' in await pg.inner_text('#u2bTeam') and 'Ben Member' in await pg.inner_text('#u2bTeam'))
        ok('B · before a scribe is chosen, the entry boxes are closed', await pg.evaluate("document.getElementById('arch_e01_q1').disabled"))
        ok('B · the closing reflection stays open to every member', await pg.evaluate("!document.getElementById('app_ref_final').disabled"))
        await pg.select_option('#twScribe', 'u-1'); await pg.wait_for_timeout(500)
        ok('B · Ann chooses herself as scribe: the boxes open', await pg.evaluate("!document.getElementById('arch_e01_q1').disabled"))
        ok('B · Agree waits until there is a record', await pg.evaluate("document.getElementById('twAgree').disabled"))

        # C · Ann types the group's entries
        await pg.fill('#strategy_period', '2027–2029')
        for i in range(14):
            await pg.evaluate("u2Go(%d)" % i)
            nq = await pg.evaluate("EL[%d].qs.length" % i)
            for j in range(nq): await pg.fill('#arch_e%02d_q%d' % (i + 1, j + 1), 'Answer %d.%d' % (i + 1, j + 1))
            if i < 13: await pg.fill('#arch_e%02d_rs' % (i + 1), 'Element %d says this.' % (i + 1))
        ok('C · the Bring button waits for all 14 elements', await pg.evaluate("document.getElementById('u2bArchBtn').disabled"))
        await pg.fill('#arch_e14_rs', 'Element 14 says this.')
        await pg.click('#u2bArchBtn'); await pg.wait_for_timeout(200)
        arch = await pg.input_value('#arch_output')
        ok('C · Bring the 14 elements together: five headings with each element', all(h in arch for h in ['Strategic Position', 'Strategic Model', 'Value Architecture', 'Strategic Navigation', 'Strategy Discipline']) and 'WHAT: Element 4 says this.' in arch, arch[:200])
        await pg.evaluate("u2Step(1)"); await pg.wait_for_timeout(200)
        ok('C · Step 2 shows what WHAT is saying, and the Intent box is empty for the group to write', 'Element 4 says this.' in await pg.inner_text('#u2bIntent') and await pg.input_value('#intent_statement') == '')
        await pg.fill('#intent_statement', 'Kafue Agro will be the grower partner of choice by 2029.')
        await pg.evaluate("u2Step(2)"); await pg.wait_for_timeout(200)
        ok('C · Step 3 shows the group\'s Intent', 'grower partner of choice' in await pg.inner_text('#u2bIntentMirror'))
        await pg.evaluate("document.querySelectorAll('#u2bSip details').forEach(d=>d.open=true)")
        for d in range(4):
            for j in range(3): await pg.fill('#sip_d%d_q%d' % (d + 1, j + 1), 'SiP answer %d.%d' % (d + 1, j + 1))
            await pg.fill('#sip_d%d_st' % (d + 1), 'SiP statement %d for Kafue.' % (d + 1))
        await pg.wait_for_timeout(1500)
        d = await dbx(); ben = rows(d, 'u-2')
        ok('C · the scribe\'s entries are on Ben\'s page too', ben.get('intent_statement', '').startswith('Kafue Agro') and ben.get('sip_d4_st') == 'SiP statement 4 for Kafue.' and ben.get('arch_output', '').startswith('Strategic Position'), list(ben)[:6])
        ok('C · nothing went into anyone\'s confirmed list yet', 'Strategy Architecture' not in (rows(d, 'u-1').get('confirmed_items') or []))
        ok('C · the page wrote no statement for the group', not any(k.startswith('appSIP_') or k == 'org_name' for k in rows(d, 'u-1')))
        await pg.evaluate("u2Step(3)"); await pg.wait_for_timeout(200)
        ok('C · the Group record shows every part written', 'Every part of the record is written' in await pg.inner_text('#u2bRecord'))
        await pg.click('#twAgree'); await pg.wait_for_timeout(800)
        d = await dbx()
        ok('C · Ann agrees: Ben has not, so nothing goes into the Capstone yet', 'Strategy Architecture' not in (rows(d, 'u-1').get('confirmed_items') or []) and 'Waiting for the other members' in await pg.inner_text('#u2bTeam'))
        if shots: await pg.screenshot(path=os.path.join(shots, 'u2_s5_scribe.png'), full_page=False)

        # D · Ben's page
        await as_user('u-2'); await pg.evaluate("showMod(4)"); await pg.wait_for_timeout(300)
        ok('D · Ben sees the group\'s entries on his own page', await pg.input_value('#arch_e01_q1') == 'Answer 1.1' and 'Ann Member is the scribe' in await pg.inner_text('#u2bTeam'))
        ok('D · Ben cannot type in the group\'s boxes', await pg.evaluate("document.getElementById('arch_e01_q1').disabled&&document.getElementById('strategy_period').disabled"))
        ok('D · Ben does not see the Bring button', await pg.evaluate("getComputedStyle(document.querySelector('#u2bArch .tw-scribe-only')).display")=='none')
        await pg.evaluate("u2Step(3)"); await pg.wait_for_timeout(200)
        await pg.click('#twAgree'); await pg.wait_for_timeout(900)
        d = await dbx()
        names = ['Strategy Architecture', 'Strategy Intent Statement', 'SiP · Customer Experience & Value', 'SiP · Operational Capability & Execution Rhythm', 'SiP · People & Culture Dynamics', 'SiP · Enterprise Value Creation', 'Success in Practice']
        ok('D · both agreed: every name is in both members\' confirmed lists', all(n in (rows(d, u).get('confirmed_items') or []) for u in ('u-1', 'u-2') for n in names))
        ok('D · the bar says every member has agreed', 'Every member has agreed' in await pg.inner_text('#u2bTeam'))
        if shots: await pg.screenshot(path=os.path.join(shots, 'u2_s5_member.png'), full_page=False)

        # E · Ben becomes scribe and changes one entry: the agreements clear
        await pg.select_option('#twScribe', 'u-2'); await pg.wait_for_timeout(600)
        await pg.evaluate("u2Step(1)"); await pg.wait_for_timeout(200)
        await pg.fill('#intent_statement', 'Kafue Agro will be the grower partner of choice by the end of 2029.')
        await pg.wait_for_timeout(1300)
        d = await dbx()
        ok('E · Ben, now scribe, changes the Intent: it changes on Ann\'s page', rows(d, 'u-1').get('intent_statement', '').endswith('end of 2029.'))
        ok('E · the change clears the agreements and the Capstone names', not any(n in (rows(d, u).get('confirmed_items') or []) for u in ('u-1', 'u-2') for n in names))
        # agree again, both
        await pg.click('#twAgree'); await pg.wait_for_timeout(700)
        await as_user('u-1'); await pg.evaluate('showMod(4)'); await pg.click('#twAgree'); await pg.wait_for_timeout(800)
        d = await dbx()
        ok('E · both agree again: the names return', all(n in (rows(d, u).get('confirmed_items') or []) for u in ('u-1', 'u-2') for n in names))

        # F · Capstone and Unit 3
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(1800)
        d = await dbx(); sec = [s for s in d['capstone']['sections'] if s['key'] == 'u2'][0]
        ok('F · the Capstone brings the three outputs into 2A to 2F', sec['content'].get('2B', '').endswith('end of 2029.') and sec['content'].get('2F') == 'SiP statement 4 for Kafue.' and sec['content'].get('2A', '').startswith('Strategic Position'), sec['content'])
        ok('F · the Capstone names the simulated company', 'Kafue Agro Holdings' in await pg.evaluate("document.getElementById('sec_u2').textContent"))
        await pg.goto(O + '/unit2_m1_lens2_p.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("typeof sipBring==='function'?sipBring(true):null"); await pg.wait_for_timeout(700)
        d = await dbx(); u3 = rows(d, 'u-1', 'u2m1_lens2')
        ok('F · Unit 3 brings the four SiP statements in from Unit 2', u3.get('sip_d1_st') == 'SiP statement 1 for Kafue.', list(u3))
        ok('F · no page errors', not errs, errs[:5])
        await b.close()
    print('%d of %d pass' % (sum(R), len(R)))
    sys.exit(0 if all(R) else 1)
asyncio.run(main())
