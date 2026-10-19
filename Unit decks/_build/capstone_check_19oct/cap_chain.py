# -*- coding: utf-8 -*-
"""Full Capstone chain, Units 1 and 3 to 9, on the real pages with a stand-in database (19 Oct 2026).
For each unit: Ann is scribe, the group boxes are filled, the scribe's page writes the Capstone outputs, both members agree.
Then: every Capstone key the Capstone page reads is on BOTH members' pages, every Capstone name is in both confirmed lists,
and the Capstone page (opened by Ben) brings every output into its box, word for word. Unit 3 also brings the SiP statements in from Unit 2.
Usage: python3 cap_chain.py <site> <fake-supabase-team.js>"""
import sys, os, re, json, asyncio, mimetypes
from playwright.async_api import async_playwright
site, fake = sys.argv[1], sys.argv[2]
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)[:400]) if (extra and not cond) else '')
O = 'http://portal.test'
cap = open(os.path.join(site, 'capstone_P.html'), encoding='utf-8').read()
PULL = {u: (lens, re.findall(r"\['(\w+)','(\w+)','([^']+)'\]", rows)) for u, lens, rows in re.findall(r"(u\d+): \{ lens:'([^']+)', rows:\[(.*?)\]\}", re.search(r'var PULL = \{(.*?)\n  \};', cap, re.S).group(1), re.S)}
BOXCOUNT = {k: len(re.findall(r"\['\d+[A-Z]'", b)) for k, b in re.findall(r"\{ key:'(u\d+)'.*?boxes:\[(.*?)\]\}", re.search(r'var BLUEPRINT = \[(.*?)\n  \];', cap, re.S).group(1), re.S)}
UNITS = [  # unit key, page, section tab, form root, patch that marks the record complete, TeamOut
    ('u1', 'unit1_P.html', 5, 'pcTool', "window.pcOpen=function(){return []}", 'pcTeamOut'),
    ('u3', 'unit2_m1_lens2_p.html', 4, 'mod4', "window.kissFilled=function(){return 16};window.okrProblems=function(){return []}", 'u3TeamOut'),
    ('u4', 'unit2_m1_lens3_p.html', 4, 'mod4', "window.mbOpen=function(){return []}", 'u4TeamOut'),
    ('u5', 'unit3_m1_lens4_p.html', 4, 'mod4', "window.s5Open=function(){return []}", 'u5TeamOut'),
    ('u6', 'unit3_m1_lens5_p.html', 4, 'mod4', "window.u6Open=function(){return []}", 'u6TeamOut'),
    ('u7', 'unit3_m1_lens6_p.html', 4, 'mod4', "window.u7Open=function(){return []}", 'u7TeamOut'),
    ('u8', 'unit3_m2_lens7_p.html', 4, 'mod4', "window.u8Open=function(){return []}", 'u8TeamOut'),
    ('u9', 'unit3_m2_lens8_p.html', 4, 'mod4', "window.u9Open=function(){return []}", 'u9TeamOut'),
]
def lr(u, lens, k, v): return {'profile_id': u, 'cohort_id': 'c-1', 'lens_id': lens, 'response_key': k, 'value': v}
SIP = {'sip_d%d_st' % n: 'SiP statement %d (from Unit 2).' % n for n in range(1, 5)}
def seed():
    lenses = [PULL[u][0] for u in PULL]
    rows = []
    for u in ('u-1', 'u-2'):
        rows += [lr(u, 'u2m1_lens1', k, v) for k, v in SIP.items()]
        rows.append(lr(u, 'u2m1_lens1', 'confirmed_items', [n for n in ('SiP · Customer Experience & Value',)]))
        rows.append(lr(u, 'u2m1_lens2', '__okr_work', {'items': [{'theme': 'Responsiveness', 'obj': 'Become the most responsive supplier in the region', 'al': [1, 1, 1, 1], 'im': 'High', 'ef': 'Low',
                     'krs': [{'t': 'Raise first-contact resolution from 60% to 85% by 30 September 2027', 'r': 'COO, CIO'}]}], 'step': 0}))
    return {
        'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Ann Member'}, {'id': 'u-2', 'role': 'participant', 'full_name': 'Ben Member'}],
        'cohort_memberships': [{'profile_id': u, 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'} for u in ('u-1', 'u-2')],
        'capstone_individual': [{'team_id': 't-1', 'profile_id': u, 'cohort_id': 'c-1'} for u in ('u-1', 'u-2')],
        'lens_progress': [{'profile_id': u, 'cohort_id': 'c-1', 'lens_id': l, 'status': 'unlocked'} for u in ('u-1', 'u-2') for l in lenses],
        'submissions': [], 'lens_catalog': [], 'lens_responses': rows,
        'box_count': BOXCOUNT,
        'capstone': {'brief': {'case_name': None, 'brief_text': 'Stand-in brief.'}, 'cohort': {'name': 'T'}, 'team': {'id': 't-1', 'name': 'Team Test', 'reopened': False},
                     'members': [{'profile_id': 'u-1', 'full_name': 'Ann Member'}, {'profile_id': 'u-2', 'full_name': 'Ben Member'}],
                     'sections': [{'key': 'u%d' % n, 'open': True, 'status': 'draft', 'content': {}, 'confirmations': []} for n in range(1, 13)]}}
FILL = """(root)=>{const r=document.getElementById(root);if(!r)return -1;let n=0;
  r.querySelectorAll('textarea,input,select').forEach((e,i)=>{
    if(e.disabled||e.type==='hidden'||e.type==='file'||e.type==='checkbox'||e.type==='radio'||e.closest('[data-team-free]')||e.classList.contains('p-thread-ta')||e.classList.contains('reflection-textarea')||e.classList.contains('ref-ta'))return;
    if(e.tagName==='SELECT'){const o=[...e.options].filter(o=>o.value);if(!o.length)return;e.value=o[o.length-1].value;}
    else{if(e.value)return;e.value=(e.type==='number'?'7':'Group entry '+(e.id||e.getAttribute('data-u9')||i));}
    e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));n++;});return n;}"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
        async def route(r):
            u = r.request.url
            if 'supabase-js' in u or u.endswith('/supabase.umd.js'): return await r.fulfill(path=fake, content_type='application/javascript')
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
            await pg.goto(O + '/' + page); await pg.wait_for_timeout(1500)
            await pg.evaluate("(t)=>{if(typeof showMod==='function')showMod(t);document.querySelectorAll('.acc').forEach(a=>a.classList.add('open'));document.querySelectorAll('details').forEach(d=>d.open=true);}", tab); await pg.wait_for_timeout(300)
        for key, page, tab, root, patch, out in UNITS:
            lens, prow = PULL[key]; u = 'Unit %s' % key[1:]
            await open_as('u-1', page, tab)
            await pg.select_option('#twScribe', 'u-1'); await pg.wait_for_timeout(700)
            if key == 'u3':
                v = await pg.evaluate("[1,2,3,4].map(n=>U3.v['sip_d'+n+'_st'])")
                ok(u + ' · the four SiP statements come in from Unit 2', v == [SIP['sip_d%d_st' % n] for n in range(1, 5)], v)
            n = await pg.evaluate(FILL, root); await pg.wait_for_timeout(1200)
            if key == 'u9':
                await open_as('u-1', page, tab)  # reload so the drop-downs carry their saved values
            await pg.evaluate(patch)
            await pg.evaluate(out + "();"); await pg.evaluate("S2RTeam.flush()"); await pg.wait_for_timeout(900)
            agreed = True
            for w in ('u-1', 'u-2'):
                if w == 'u-2': await open_as('u-2', page, tab); await pg.evaluate(patch)
                await pg.evaluate("S2RTeam.redraw()"); await pg.wait_for_timeout(300)
                if await pg.evaluate("document.getElementById('twAgree').disabled"):
                    agreed = False; ok('%s · %s can select Agree' % (u, w), False, await pg.inner_text('#twBar')); break
                await pg.click('#twAgree'); await pg.wait_for_timeout(1000)
            d = await dbx()
            for w, who in (('u-1', 'Ann'), ('u-2', 'Ben')):
                g = rows(d, w, lens)
                miss = [k for _, k, _ in prow if not (isinstance(g.get(k), str) and g.get(k).strip())]
                ok('%s · every Capstone output is on %s\'s page (%d keys, %d boxes filled by the test)' % (u, who, len(prow), n), not miss, miss)
                conf = g.get('confirmed_items') or []
                nm = [nm for _, _, nm in prow if nm not in conf]
                ok('%s · every Capstone name is in %s\'s confirmed list' % (u, who), not nm, nm)
        # The Capstone page, opened by Ben, brings everything in
        await pg.evaluate("()=>localStorage.setItem('fake_uid','u-2')")
        await pg.goto(O + '/capstone_P.html'); await pg.wait_for_timeout(8000)
        if os.environ.get('DBG'):
            print(await pg.evaluate("JSON.parse(localStorage.getItem('fake_log')).slice(-25)"))
            print(await pg.evaluate("[...document.querySelectorAll('[id^=msg_]')].map(e=>e.id+': '+e.textContent).filter(x=>x.length>10).join(' | ')"))
            print(await pg.evaluate("document.querySelectorAll('textarea.box-ta').length"), (await pg.inner_text('body'))[:600])
        d = await dbx()
        for key, page, *_ in UNITS:
            lens, prow = PULL[key]; g = rows(d, 'u-2', lens)
            sec = [s for s in d['capstone']['sections'] if s['key'] == key][0]
            want = {bx: g.get(k, '').strip() for bx, k, _ in prow}
            got = {bx: sec['content'].get(bx) for bx, _, _ in prow}
            ok('Unit %s · the Capstone brings %s in, word for word' % (key[1:], ', '.join(want)), got == want and all(want.values()), {bx: (got[bx] or '')[:40] for bx in got if got[bx] != want[bx]})
        ok('no page errors', not errs, errs[:5])
        await b.close()
    print('%d of %d pass' % (sum(R), len(R)))
asyncio.run(main())
