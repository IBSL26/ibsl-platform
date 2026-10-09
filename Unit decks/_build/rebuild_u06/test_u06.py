# -*- coding: utf-8 -*-
"""Browser checks of the two Unit 6 PREVIEW pages (Playwright). Usage: python3 test_u06.py <preview folder> [<screenshot folder>]"""
import sys, os, re, json, asyncio
from playwright.async_api import async_playwright
import u6_content as C
prev = sys.argv[1]; shots = sys.argv[2] if len(sys.argv) > 2 else None
if shots: os.makedirs(shots, exist_ok=True)
R = []
def ok(name, cond, extra=''):
    R.append(bool(cond)); print(('PASS' if cond else 'FAIL'), '·', name, ('· ' + str(extra)) if (extra and not cond) else '')
TITLES = ['1.1 — Measurement vs Management', '1.2 — The FACES Framework', '1.3 — The Three Sights of Progress', '1.4 — Leader’s Response', '1.5 — The Impact of a Calibrated System',
          '2.1 — PM as the Execution Bridge', '2.2 — Compliance vs Commitment Architecture', '2.3 — Leader vs Team: A Critical Distinction',
          '3.1 — Unity in Diversity', '3.2 — The Three Execution Gaps', '3.3 — The Continuous PM Shift', '4.1 — The EXECUTION Framework']
GONE = ['Rules of the Game', 'MyHealth', 'Collective Progress Signal', 'Three Elements of Enterprise PM Design', '30-Day', 'next 30 days.', 'Your Enterprise Signal', 'EXECUTION Self-Score', 'The 1–5 Rating Scale',
        'CXO Hot Zones —', 'Baseline Simulation', 'Periodic Measures', 'hospital', 'PIP', 'Apply the Formula']
FL = C.fields()
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
        # ───────────── participant ─────────────
        pg = await ctx.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text and 'ERR_' not in m.text else None)
        pg.on('dialog', lambda d: asyncio.ensure_future(d.accept()))
        url = 'file://' + os.path.abspath(os.path.join(prev, 'PREVIEW - Unit 6 Participant.html'))
        await pg.goto(url); await pg.wait_for_timeout(700)
        await pg.evaluate("localStorage.clear()"); await pg.reload(); await pg.wait_for_timeout(700)
        titles = await pg.evaluate("[...document.querySelectorAll('.acc-t')].map(e=>e.textContent.trim())")
        ok('P · the twelve part titles, in order', titles[:12] == TITLES, titles[:13])
        ok('P · no part titled 5.x; Unit Summary follows', titles[12] == 'Unit Summary', titles[12:])
        subs = await pg.evaluate("[...document.querySelectorAll('.acc-meta')].slice(0,12).map(e=>e.textContent.trim())")
        ok('P · every part has a sub-line', all(subs) and len(subs) == 12, subs)
        vis = await pg.evaluate("(()=>{const c=document.body.cloneNode(true);c.querySelectorAll('script,style').forEach(e=>e.remove());return c.textContent.replace(/\\s+/g,' ');})()")
        ph = await pg.evaluate("[...document.querySelectorAll('[placeholder]')].map(e=>e.getAttribute('placeholder')).join(' | ')")
        for g in GONE: ok('P · gone: ' + g, g not in vis and g not in ph)
        ok('P · the lock overlay is hidden', await pg.evaluate("getComputedStyle(document.getElementById('p-lock-overlay')).display") == 'none')
        refs = await pg.evaluate("[...document.querySelectorAll('.ref-block textarea.reflection-textarea[id]')].map(e=>e.id)")
        ok('P · reflections ref1, ref2, ref3, ref4, ref6, ref7, ref11, ref12', sorted(refs) == sorted(['ref1', 'ref2', 'ref3', 'ref4', 'ref6', 'ref7', 'ref11', 'ref12']), refs)
        n_prompt = await pg.evaluate("document.querySelectorAll('.ref-block .ref-prompt').length")
        ok('P · each of the eight reflections carries its question as ref-prompt', n_prompt == 8, n_prompt)
        ok('P · no reflection box without a saved-answer name', await pg.evaluate("document.querySelectorAll('.ref-block textarea:not([id])').length") == 0)
        # reflections save (ref11 is the one that did not save before)
        for rid, sec in (('ref2', 0), ('ref11', 1), ('ref6', 2), ('ref12', 2)):
            await pg.evaluate("(i)=>showMod(i,null)", sec)
            await pg.evaluate("(id)=>{const a=document.getElementById(id).closest('.acc');a.classList.add('open');}", rid)
            await pg.fill('#' + rid, 'Test answer for ' + rid)
            await pg.evaluate("(id)=>document.getElementById(id).closest('.ref-block').querySelector('button').click()", rid)
        await pg.wait_for_timeout(1700)
        st = await pg.evaluate("window.__store['u3m1_lens5']||{}")
        ok('P · reflections save, the new 2.3 and 3.3 ones included', all(st.get(r) == 'Test answer for ' + r for r in ('ref2', 'ref11', 'ref6', 'ref12')), {k: st.get(k) for k in ('ref2', 'ref11', 'ref6', 'ref12')})
        # 3.1 role cards
        await pg.evaluate("showMod(2,null)")
        await pg.click(".cm-card >> nth=1"); await pg.wait_for_timeout(150)
        d = await pg.evaluate("(()=>{const v=document.querySelector('.cm-detail.visible');return v?v.textContent:'';})()")
        ok('P · 3.1 CFO card: natural bias, hot zone, PM contribution, alignment contribution, in the participant’s voice',
           all(x in d for x in ('Your natural bias', 'Revenue, cost discipline, and ROI.', 'As CFO, you interpret', 'PM Contribution', 'When your PM insight is isolated', 'Alignment Contribution', 'You link financial health')), d[:300])
        ok('P · 3.1 holds ten role cards and ten details', await pg.evaluate("document.querySelectorAll('.cm-card').length==10&&document.querySelectorAll('.cm-detail').length==10"))
        if shots: await pg.screenshot(path=os.path.join(shots, 'P_3.1_role_card.png'), full_page=True)
        # Section 4: learning content only
        await pg.evaluate("showMod(3,null)")
        ok('P · Section 4 has one part, nine principles, and no entry box', await pg.evaluate("(()=>{const m=document.getElementById('mod3');return m.querySelectorAll('.acc').length==1&&m.querySelectorAll('.ai-card').length==9&&m.querySelectorAll('textarea,select,input').length==0;})()"))
        ok('P · 4.1 carries the FACES and EXECUTION distinction', 'FACES is the function test.' in vis and 'EXECUTION is the design quality test.' in vis and 'FACES tells us what a PM system must deliver.' in vis)
        # Section 5
        await pg.evaluate("showMod(4,null)")
        ok('P · Section 5 has four step tabs and %d entries' % len(FL), await pg.evaluate("document.querySelectorAll('#mod4 .step-tab').length") == 4 and await pg.evaluate("document.querySelectorAll('#mod4 [data-u6]').length") == len(FL))
        ok('P · every Section 5 entry has its own label', await pg.evaluate("[...document.querySelectorAll('#mod4 [data-u6]')].every(e=>document.querySelector('label[for=\"'+e.id+'\"]'))"))
        await pg.click('#u6ConfBtn'); await pg.wait_for_timeout(200)
        msg = await pg.inner_text('#u6Msg')
        ok('P · Confirm on an empty record is refused and names what is open, step by step', msg.startswith('Before you confirm, complete: Step 1 · Scoring Logic (21 entries still open); Step 2 · FACES (5 entries still open); Step 3 · EXECUTION (9 entries still open); Step 4 · PM Scorecards (18 entries still open)'), msg)
        opts = await pg.evaluate("[...document.querySelectorAll('#u6_kr1 option')].map(o=>o.value).filter(Boolean)")
        ok('P · Step 4 lists the eight Key Results of the Unit 3 page', len(opts) == 8, opts)
        ok('P · Step 4 shows the Unit 3 Objectives read only', await pg.evaluate("document.querySelectorAll('#u6Okrs .u6-from').length") == 4)
        for i in range(4):
            await pg.click('#mod4 .step-tab >> nth=%d' % i); await pg.wait_for_timeout(120)
            ok('P · step %d opens on its tab' % (i + 1), await pg.evaluate("(i)=>[...document.querySelectorAll('#mod4 .step-panel')].map(p=>p.classList.contains('active')).indexOf(true)===i", i))
            for f in [x for x in FL if x[2] == C.PARTS[i][0]]:
                if f[4] == 't': await pg.fill('#u6_' + f[0], 'Entry for ' + f[0])
                elif f[4] == 'k': await pg.select_option('#u6_' + f[0], opts[0 if f[0] == 'kr1' else 3])
                else: await pg.fill('#u6_' + f[0], '30' if f[0].endswith('kr1_w') else '20')
            if shots: await pg.screenshot(path=os.path.join(shots, 'P_5_step%d.png' % (i + 1)), full_page=True)
        await pg.wait_for_timeout(400)
        ok('P · the chosen Key Results show on the scorecard rows', await pg.evaluate("(o)=>[...document.querySelectorAll('.u6-kr1-t')].every(e=>e.textContent===o[0])&&[...document.querySelectorAll('.u6-kr2-t')].every(e=>e.textContent===o[3])", opts))
        tot = await pg.inner_text('#u6_tot_ceo')
        ok('P · weights of 30, 20, 20, 20 are shown as 90% and flagged', '90%' in tot and '100%' in tot, tot)
        await pg.click('#u6ConfBtn'); await pg.wait_for_timeout(300)
        msg = await pg.inner_text('#u6Msg')
        ok('P · Confirm is refused while a scorecard does not add up to 100%', msg == 'Before you confirm, complete: the CEO weights add up to 100% (now 90%); the CFO weights add up to 100% (now 90%).', msg)
        await pg.fill('#u6_ceo_bv_w', '30'); await pg.fill('#u6_cfo_bv_w', '30'); await pg.wait_for_timeout(200)
        ok('P · total shows 100% with a tick', '100% ✓' in await pg.inner_text('#u6_tot_cfo'))
        await pg.click('#u6ConfBtn'); await pg.wait_for_timeout(900)
        st = await pg.evaluate("window.__store['u3m1_lens5']||{}")
        names = [x[2] for x in C.PARTS]
        ok('P · Confirm writes the four names into confirmed_items', all(n in (st.get('confirmed_items') or []) for n in names), st.get('confirmed_items'))
        ok('P · Confirm writes pm_scoring, pm_faces, pm_execution and pm_scorecards', all(isinstance(st.get(x[3]), str) and len(st[x[3]]) > 50 for x in C.PARTS), [len(str(st.get(x[3]))) for x in C.PARTS])
        ok('P · the scoring record carries rating, evidence, response, factors, sights and cadence',
           all(x in st.get('pm_scoring', '') for x in ('Rating 1 · Poor', 'Performance level that earns this rating: Entry for r1_level', 'Evidence required to confirm it', 'Leadership response in the monthly review', 'Contextual factors', 'Lines of sight of progress', 'Sight 3 · Behavioural & Values Alignment: Entry for sight3', 'Our review cadence', 'Why this cadence')), st.get('pm_scoring', '')[:400])
        ok('P · the scorecard record carries the two Key Results and both roles with weights',
           all(x in st.get('pm_scorecards', '') for x in ('Key Result 1: ' + opts[0], 'Key Result 2: ' + opts[3], 'PM scorecard · CEO', 'PM scorecard · CFO', 'weight (%): 30%')), st.get('pm_scorecards', '')[:500])
        ok('P · the record shows Confirmed', 'Confirmed' in await pg.text_content('#u6Rec .u6-conf'))
        if shots: await pg.screenshot(path=os.path.join(shots, 'P_5_confirmed.png'), full_page=True)
        # edit after Confirm
        await pg.click('#mod4 .step-tab >> nth=1'); await pg.fill('#u6_faces1', 'Changed entry'); await pg.wait_for_timeout(1300)
        st = await pg.evaluate("window.__store['u3m1_lens5']||{}")
        ok('P · an edit after Confirm takes the four names out again', not any(n in (st.get('confirmed_items') or []) for n in names), st.get('confirmed_items'))
        # reload
        await pg.reload(); await pg.wait_for_timeout(900)
        vals = await pg.evaluate("[...document.querySelectorAll('#mod4 [data-u6]')].map(e=>[e.getAttribute('data-u6'),e.value])")
        d = dict(vals)
        ok('P · after a reload every Section 5 entry is back', d.get('faces1') == 'Changed entry' and d.get('r3_resp') == 'Entry for r3_resp' and d.get('kr2') == opts[3] and d.get('ceo_bv_w') == '30' and all(v for v in d.values()), [k for k, v in d.items() if not v])
        ok('P · after a reload the reflections are back', await pg.input_value('#ref11') == 'Test answer for ref11' and await pg.input_value('#ref12') == 'Test answer for ref12')
        ok('P · one Submit to Facilitator, at the end', await pg.evaluate("document.querySelectorAll('[onclick=\"sendToFacilitator()\"]').length") == 1)
        sm = await pg.evaluate("[...document.querySelectorAll('#summaryP .sum-arc')].map(e=>e.textContent)")
        ok('P · Unit Summary has five blocks, the fifth Application', len(sm) == 5 and sm[4].startswith('Application'), sm)
        ok('P · no script error', not errs, errs)
        # phone width
        ph_pg = await b.new_page(viewport={'width': 390, 'height': 800}); await ph_pg.goto(url); await ph_pg.wait_for_timeout(500)
        for i in range(5):
            await ph_pg.evaluate("(i)=>{showMod(i,null);document.querySelectorAll('.mod.active .acc').forEach(a=>{if(a.style.display!=='none')a.classList.add('open')});}", i)
            await ph_pg.wait_for_timeout(500)
            if i == 4:
                for s in range(4):
                    await ph_pg.evaluate("(s)=>u6Step(s)", s)
                    await ph_pg.wait_for_timeout(500)   # the arrow of the Unit Summary header turns as the part opens; measure when it has settled
                    w = await ph_pg.evaluate("document.documentElement.scrollWidth")
                    ok('P · phone width, Section 5 step %d: no wider than before the amendments (536)' % (s + 1), w <= 536, w)
            else:
                w = await ph_pg.evaluate("document.documentElement.scrollWidth")
                ok('P · phone width, Section %d: no wider than before the amendments (466)' % (i + 1), w <= 466, w)
        if shots: await ph_pg.screenshot(path=os.path.join(shots, 'P_phone_step4.png'), full_page=True)
        # ───────────── facilitator ─────────────
        fg = await ctx.new_page(); ferr = []
        fg.on('pageerror', lambda e: ferr.append(str(e)))
        fg.on('console', lambda m: ferr.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text and 'ERR_' not in m.text else None)
        await fg.goto('file://' + os.path.abspath(os.path.join(prev, 'PREVIEW - Unit 6 Facilitator.html'))); await fg.wait_for_timeout(600)
        ft = await fg.evaluate("[...document.querySelectorAll('.acc-t')].map(e=>e.textContent.trim())")
        ok('F · the same twelve part titles', ft[:12] == TITLES and ft[12] == 'Unit Summary', ft)
        fs = await fg.evaluate("[...document.querySelectorAll('.acc-meta')].slice(0,12).map(e=>e.textContent.trim())")
        ok('F · the same sub-lines as the participant page', fs == subs, (fs, subs))
        fvis = await fg.evaluate("(()=>{const c=document.body.cloneNode(true);c.querySelectorAll('script,style').forEach(e=>e.remove());return c.textContent.replace(/\\s+/g,' ');})()")
        for g in GONE:
            if g == 'next 30 days.': continue   # the 3.1 reflection keeps "in the next 30 days" on both pages
            ok('F · gone: ' + g, g not in fvis)
        ok('F · no entry box', await fg.evaluate("document.querySelectorAll('textarea,select,input').length") == 0)
        ok('F · no times and no room wording', not re.search(r'\b\d+\s*min\b|[Ss]uggested tim|at the table|[Tt]able discussion|\bvote\b|[Cc]lick a role|, timing,', fvis))
        na = fvis.count('PARTICIPANT ACTIVITY')
        ok('F · twelve PARTICIPANT ACTIVITY notes (eight reflections, four steps)', na == 12, na)
        ok('F · seventeen FACILITATOR GUIDANCE boxes (one for each of the twelve parts, one for Section 5 and one for each step)', fvis.count('FACILITATOR GUIDANCE') == 17, fvis.count('FACILITATOR GUIDANCE'))
        await fg.evaluate("showMod(3)"); await fg.click(".comp-card >> nth=0"); await fg.wait_for_timeout(150)
        d = await fg.evaluate("(()=>{const v=[...document.querySelectorAll('.cxo-detail')].find(e=>e.style.display==='block');return v?v.textContent:'';})()")
        ok('F · 3.1 CEO card: natural bias, hot zone, PM contribution, alignment contribution and tags',
           all(x in d for x in ('Natural bias', 'Growth, milestones, and market position.', 'The CEO holds the integrated view', 'PM Contribution', 'Enterprise trajectory signal', 'When CEO PM visibility is absent', 'Alignment Contribution', 'Connects the Big Picture', 'Course Correction Authority')), d[:400])
        if shots: await fg.screenshot(path=os.path.join(shots, 'F_3.1_role_card.png'), full_page=True)
        await fg.evaluate("showMod(5)")
        for i in range(4):
            await fg.click('#mod5 .step-tab >> nth=%d' % i); await fg.wait_for_timeout(100)
            ok('F · Section 5 step %d opens on its tab' % (i + 1), await fg.evaluate("(i)=>[...document.querySelectorAll('#mod5 .step-panel')].map(p=>p.classList.contains('active')).indexOf(true)===i", i))
            if shots: await fg.screenshot(path=os.path.join(shots, 'F_5_step%d.png' % (i + 1)), full_page=True)
        ok('F · no script error', not ferr, ferr)
        # the two pages against each other
        both = ['A rating should trigger a clear leadership response.', 'This transparency produces three powerful shifts in the organisational dynamic:', 'Strategic Transparency', 'Pathways to Excellence',
                'random acts of excellence', 'A compliance-driven PM depicts an environment where:', 'A commitment-driven PM depicts an environment where:', 'Root cause; co-designed recovery',
                'The choice is rarely made explicitly — but it is always made.', 'FACES tells us what a PM system must deliver.', 'EXECUTION tells us what must be designed into the system for it to deliver.',
                'Designing the PM Architecture', 'Step 4 · PM Scorecards', 'The Alignment Brigade', C.LVT_ONE_LINE]
        for s in both: ok('both pages carry: ' + s[:60], s in vis and s in fvis)
        await b.close()
    print('\n%d checks, %d passed, %d failed' % (len(R), sum(R), len(R) - sum(R)))
    sys.exit(0 if all(R) else 1)
asyncio.run(main())
