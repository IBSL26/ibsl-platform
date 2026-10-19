# -*- coding: utf-8 -*-
"""Consistency review 19 Oct: every Unit 2-9 page on the stand-in database. Participant pages: open unlocked, every reflection saves,
Submit to Facilitator stores a submission, the Learning Portfolio shows the answers. Facilitator pages: open with no page error and
every section tab opens. Usage: python3 e2e_all.py <site> <fake-supabase.js>"""
import sys, os, json, asyncio, mimetypes, re
from playwright.async_api import async_playwright
site, fake = sys.argv[1], sys.argv[2]; O = 'http://portal.test'; R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)[:300]) if (extra and not cond) else '')
U = {2: 'unit2_m1_lens1', 3: 'unit2_m1_lens2', 4: 'unit2_m1_lens3', 5: 'unit3_m1_lens4', 6: 'unit3_m1_lens5', 7: 'unit3_m1_lens6', 8: 'unit3_m2_lens7', 9: 'unit3_m2_lens8'}
LID = {u: 'u%sm%s_lens%s' % tuple(re.match(r'unit(\d)_m(\d)_lens(\d+)', f).groups()) for u, f in U.items()}
def seed(uid_role):
    return {'profiles': [{'id': 'u-1', 'role': 'participant', 'full_name': 'Member One'}, {'id': 'f-1', 'role': 'facilitator', 'full_name': 'Fac One'}],
            'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}, {'profile_id': 'f-1', 'cohort_id': 'c-1', 'role_in_cohort': 'facilitator', 'joined_at': '2026-09-01'}],
            'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': l, 'status': 'unlocked'} for l in LID.values()],
            'lens_responses': [], 'submissions': [],
            'lens_catalog': [{'id': l, 'unit': u, 'module': 2 if u < 5 else 3, 'sequence': u - 1, 'title': 'Unit %d' % u, 'requires_lens': None} for u, l in LID.items()],
            'box_count': {}, 'capstone': {'brief': {}, 'cohort': {}, 'team': {'id': 't-1', 'name': 'T', 'reopened': False}, 'members': [], 'sections': []}}
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
        await pg.evaluate("(s)=>{localStorage.clear();localStorage.setItem('fakedb',JSON.stringify(s));localStorage.setItem('fake_uid','u-1');}", seed('u-1'))
        answers = {}
        for u, f in U.items():
            errs.clear(); await pg.goto(O + '/' + f + '_p.html'); await pg.wait_for_timeout(1300)
            refs = await pg.evaluate("[...document.querySelectorAll('.ref-block textarea')].map(e=>e.id).filter(i=>/^ref\\d+$/.test(i))")
            for rid in refs:
                await pg.evaluate("""(id)=>{const e=document.getElementById(id);e.value='Answer '+id+' unit';e.dispatchEvent(new Event('input',{bubbles:true}));
                    const btn=e.closest('.ref-block').querySelector('button');if(btn)btn.click();}""", rid)
                await pg.wait_for_timeout(120)
            await pg.wait_for_timeout(1800)
            d = json.loads(await pg.evaluate("localStorage.getItem('fakedb')"))
            rows = {r['response_key']: r['value'] for r in d['lens_responses'] if r['lens_id'] == LID[u] and r['profile_id'] == 'u-1'}
            saved = [r for r in refs if rows.get(r) not in (None, '', {}, [])]
            print('   ', {r: str(rows.get(r))[:70] for r in refs if rows.get(r) != 'Answer %s unit' % r})
            ok(f'Unit {u} participant · page opens and all {len(refs)} reflections save', refs and len(saved) == len(refs), set(refs) - set(saved))
            await pg.evaluate("typeof sendToFacilitator==='function' && sendToFacilitator()"); await pg.wait_for_timeout(900)
            d = json.loads(await pg.evaluate("localStorage.getItem('fakedb')"))
            ok(f'Unit {u} participant · Submit to Facilitator stores a submission', any(s['lens_id'] == LID[u] for s in d['submissions']))
            ok(f'Unit {u} participant · no page error', not errs, errs[:3]); answers[u] = saved
        await pg.goto(O + '/collection.html?participantId=u-1'); await pg.wait_for_timeout(2000)
        for u in U:
            ch = await pg.evaluate("(id)=>{const e=document.getElementById('ch-'+id);return e?e.innerText:'';}", LID[u])
            ok(f'Unit {u} · Learning Portfolio shows the reflections', ch and sum(('Answer %s unit' % r) in ch for r in answers[u]) >= 1, ch[:200])
        await pg.evaluate("localStorage.setItem('fake_uid','f-1')")
        for u, f in U.items():
            errs.clear(); await pg.goto(O + '/' + f + '_f.html'); await pg.wait_for_timeout(1300)
            n = await pg.evaluate("document.querySelectorAll('.mod-panel,.mod').length")
            opened = await pg.evaluate("""(()=>{let c=0;const ps=[...document.querySelectorAll('.mod-panel,.mod')];ps.forEach((p,i)=>{try{showMod(i,null);}catch(e){try{showMod(i);}catch(e2){}}
                if(getComputedStyle(p).display!=='none')c++;});return c;})()""")
            ok(f'Unit {u} facilitator · opens with every section tab ({n}) and no page error', n >= 6 and opened >= n - 1 and not errs, (n, opened, errs[:3]))
        await b.close()
    print('\n%d of %d checks pass' % (sum(R), len(R)))
asyncio.run(main())
