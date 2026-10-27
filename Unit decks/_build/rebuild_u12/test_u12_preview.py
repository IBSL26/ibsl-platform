# -*- coding: utf-8 -*-
"""Playwright checks on the Unit 12 PREVIEW pages (served from out/preview)."""
import sys, json, re
from playwright.sync_api import sync_playwright
BASE = sys.argv[1]  # e.g. http://localhost:8765
res = []
def ok(name, cond, info=''):
    res.append((name, bool(cond), info)); print(('PASS ' if cond else 'FAIL ') + name + (' · ' + str(info) if info and not cond else ''))

with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={'width': 1280, 'height': 900})
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    P = BASE + '/PREVIEW%20-%20Unit%2012%20Participant.html'
    pg.goto(P); pg.evaluate("localStorage.clear()"); pg.goto(P); pg.wait_for_timeout(1500)
    vis = pg.inner_text('body')
    ok('no lens in visible text', not re.search(r'\blens\b', vis, re.I))
    ok('header key learning outcomes', 'Maintain continuous sight of strategic, operational and behavioural performance' in vis)
    ok('section titles', all(x in pg.text_content('body') for x in ['What Sustains Performance', 'Our Quarterly Three Lines of Sight']))
    # reflections save and restore
    pg.click('text=Awareness'); pg.wait_for_timeout(200)
    pg.evaluate("document.querySelectorAll('#mod0 .acc').forEach(a=>a.classList.add('open'))")
    pg.fill('#ref11', 'We read only the strategic line (test).'); pg.wait_for_timeout(1700)
    pg.evaluate("showMod(2)"); pg.evaluate("document.querySelectorAll('#mod2 .acc').forEach(a=>a.classList.add('open'))")
    for i, v in enumerate(['COO', 'Operational', 'Reviews postponed (test)', 'Keep the review rhythm (test)']):
        pg.fill('[data-fkey="ref13"][data-fidx="%d"]' % i, v)
    pg.wait_for_timeout(1500)
    st = pg.evaluate("JSON.parse(localStorage.getItem('u12_preview_store')).lens.u4m2_lens11")
    ok('ref11 saved', st.get('ref11') == 'We read only the strategic line (test).', st.get('ref11'))
    ok('ref13 saved as labelled lines', 'My role: COO' in (st.get('ref13') or ''), st.get('ref13'))
    # Section 5
    pg.evaluate("showMod(4)"); pg.wait_for_timeout(300)
    ok('group bar drawn', pg.locator('#u12TwBar .tw-bar').count() == 1)
    ok('non-scribe locked', pg.locator('#mod4 [data-u12="s.result"]').is_disabled())
    pg.select_option('#twScribe', 'preview'); pg.wait_for_timeout(1500)
    ok('scribe unlocked', not pg.locator('#mod4 [data-u12="s.result"]').is_disabled())
    pg.evaluate("document.querySelectorAll('#mod4 .acc').forEach(a=>a.classList.add('open'))")
    pg.click('text=Bring in from my earlier units'); pg.wait_for_timeout(800)
    ok('bring-in message', 'Brought in: Unit 6 WARD, Unit 10 ESRG scan, Unit 11 health position' in pg.inner_text('#u12BringMsg'), pg.inner_text('#u12BringMsg'))
    ok('KR brought in', 'Increase customer enquiries' in pg.input_value('[data-u12="src.kr"]'))
    ok('waypoints brought in', pg.input_value('[data-u12="src.wp"]').startswith('72% by 31 March'), pg.input_value('[data-u12="src.wp"]'))
    ok('ESRG brought in', pg.input_value('[data-u12="src.es.1"]') == '2.00', pg.input_value('[data-u12="src.es.1"]'))
    ok('health brought in', pg.input_value('[data-u12="src.h_score"]') == '52.0')
    ok('strategic waypoint prefilled', pg.input_value('[data-u12="s.wp"]') == '72% by 31 March')
    ok('lowest capability shown', 'Operational Flow 2.00 (Significant constraint)' in pg.inner_text('#u12OLow') and 'raises the alert' in pg.inner_text('#u12OLow'), pg.inner_text('#u12OLow'))
    ok('health band shown', 'Caution Zone' in pg.inner_text('#u12BLow') and 'raises the alert' in pg.inner_text('#u12BLow'))
    ok('agree blocked while open', 'Still to complete' in pg.inner_text('#u12RecMsg'))
    pg.select_option('[data-u12="quarter"]', 'Quarter 2')
    pg.fill('[data-u12="s.wp"]', '80% by 30 June')
    pg.fill('[data-u12="s.result"]', '74% resolved within 48 hours')
    pg.select_option('[data-u12="s.raised"]', 'Yes')
    pg.fill('[data-u12="s.rec"]', 'Team leaders review open enquiries with each owner every morning')
    pg.fill('[data-u12="s.check"]', 'End of July')
    pg.select_option('[data-u12="o.raised"]', 'Yes'); pg.fill('[data-u12="o.rec"]', 'IT restores availability to 99% within four weeks'); pg.fill('[data-u12="o.owner"]', 'CIO'); pg.fill('[data-u12="o.check"]', 'End of July')
    pg.select_option('[data-u12="b.raised"]', 'Yes'); pg.fill('[data-u12="b.rec"]', 'COO strengthens collaboration, trust and commitment'); pg.fill('[data-u12="b.owner"]', 'COO'); pg.fill('[data-u12="b.check"]', 'Quarter 3 thermometer')
    lines = ['Behavioural', 'Operational', 'Operational', 'Strategic']
    for i in range(4):
        pg.select_option('[data-u12="kiss.%d.line"]' % i, lines[i])
        pg.fill('[data-u12="kiss.%d.practice"]' % i, 'Practice %d (test)' % (i + 1))
        pg.fill('[data-u12="kiss.%d.owner"]' % i, 'Owner %d' % (i + 1))
    pg.wait_for_timeout(300)
    ok('four decisions present by default', pg.locator('#u12Kiss .u12-krow').count() == 4)
    pg.click('text=+ Add a decision'); pg.wait_for_timeout(200)
    ok('add a decision', pg.locator('#u12Kiss .u12-krow').count() == 5)
    ok('fifth decision makes record open', 'Decision 5' in pg.inner_text('#u12RecMsg'))
    pg.on('dialog', lambda d: d.accept())
    pg.locator('#u12Kiss .u12-del').last.click(); pg.wait_for_timeout(300)
    ok('remove a decision', pg.locator('#u12Kiss .u12-krow').count() == 4)
    pg.wait_for_timeout(1500)
    ok('record complete', 'Your record is complete' in pg.inner_text('#u12RecMsg'), pg.inner_text('#u12RecMsg'))
    st = pg.evaluate("JSON.parse(localStorage.getItem('u12_preview_store')).lens.u4m2_lens11")
    ok('four Capstone texts saved', all(k in st for k in ['qs_strategic', 'qs_operational', 'qs_behavioural', 'qs_kiss']), list(st.keys()))
    ok('12A text', 'Alert raised: Yes' in st.get('qs_strategic', '') and 'D · Decider: Customer Service Executive (sample)' in st.get('qs_strategic', ''))
    ok('12B text', 'Lowest capability: Operational Flow 2.00' in st.get('qs_operational', ''), st.get('qs_operational'))
    ok('12C text', 'Health position: 52.0 /100 · Caution Zone' in st.get('qs_behavioural', ''), st.get('qs_behavioural'))
    ok('12D text', 'Keep: Practice 1 (test) · Line of sight: Behavioural · Owner: Owner 1' in st.get('qs_kiss', ''), st.get('qs_kiss'))
    ok('reflections stay out of Section 5 texts', not any('test).' in st.get(k, '') and 'strategic line' in st.get(k, '') for k in ['qs_strategic', 'qs_kiss']))
    pg.click('#u12RecMsg ~ button:has-text("Agree")'); pg.wait_for_timeout(1500)
    tm = pg.evaluate("JSON.parse(localStorage.getItem('u12_preview_store')).team")
    ok('agree recorded with the four names', tm['agree'].get('preview') == tm['version'] and tm['names'] == ["Quarterly Lines of Sight · Strategic", "Quarterly Lines of Sight · Operational", "Quarterly Lines of Sight · Behavioural", "Quarterly Lines of Sight · KISS for Next Quarter"], tm)
    # reload restores
    pg.reload(); pg.wait_for_timeout(1800); pg.evaluate("showMod(4)")
    ok('reload restores record', pg.input_value('[data-u12="s.result"]') == '74% resolved within 48 hours' and pg.input_value('[data-u12="kiss.3.practice"]') == 'Practice 4 (test)')
    ok('reload restores reflection', pg.input_value('#ref11') == 'We read only the strategic line (test).')
    ok('unit summary present', 'The quarterly page' in pg.inner_text('#summaryP'))
    ok('no page errors (participant)', not errs, errs)
    # phone width
    ph = br.new_page(viewport={'width': 390, 'height': 800})
    ph.goto(P); ph.wait_for_timeout(1200)
    widths = []
    for k in range(5):
        ph.evaluate("showMod(%d)" % k); ph.evaluate("document.querySelectorAll('.acc').forEach(a=>a.classList.add('open'))"); ph.wait_for_timeout(150)
        widths.append(ph.evaluate("Math.max.apply(null,[0].concat(Array.from(document.querySelectorAll('.mod-panel.active .mod-body *')).map(e=>e.closest('.u12-scroll')&&e!==e.closest('.u12-scroll')?0:e.getBoundingClientRect().right)))"))
    ok('phone: section content fits (wide tables scroll in their box)', max(widths) <= 392, widths)
    # facilitator
    fe = []
    fp = br.new_page(viewport={'width': 1280, 'height': 900}); fp.on('pageerror', lambda e: fe.append(str(e)))
    fp.goto(BASE + '/PREVIEW%20-%20Unit%2012%20Facilitator.html'); fp.wait_for_timeout(1200)
    fv = fp.text_content('body')
    ok('facilitator: guide sections', all(x in fv for x in ['Unit Intent', 'Key Facilitation Questions', 'Tone & Watch Points']))
    n_inputs = fp.evaluate("document.querySelectorAll('.mod-panel textarea, .mod-panel input, .mod-panel select').length")
    ok('facilitator: no entry boxes in sections', n_inputs == 0, n_inputs)
    ok('facilitator: unit summary', fp.evaluate("document.body.innerHTML.indexOf('Unit 12 synthesis')>0"))
    ok('facilitator: no lens', not re.search(r'\blens\b', fv, re.I))
    ok('no page errors (facilitator)', not fe, fe)
    pg.screenshot(path='shot_p_s5.png', full_page=False)
    br.close()
print('%d of %d passed' % (sum(1 for r in res if r[1]), len(res)))
