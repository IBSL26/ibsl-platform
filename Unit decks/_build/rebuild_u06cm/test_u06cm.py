# -*- coding: utf-8 -*-
"""Browser checks of the Unit 6 PREVIEW pages (rework of 14 October 2026).
Usage: python3 test_u06cm.py <preview folder> [<screenshot folder>]"""
import sys, os, json
from playwright.sync_api import sync_playwright
folder = sys.argv[1]; shots = sys.argv[2] if len(sys.argv) > 2 else None
P = 'file://' + os.path.abspath(os.path.join(folder, 'PREVIEW - Unit 6 Participant.html'))
F = 'file://' + os.path.abspath(os.path.join(folder, 'PREVIEW - Unit 6 Facilitator.html'))
ok = 0; bad = []


def chk(c, name):
    global ok
    if c: ok += 1
    else: bad.append(name)


with sync_playwright() as pw:
    br = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium') if os.path.exists('/opt/pw-browsers/chromium') else pw.chromium.launch()
    pg = br.new_page(viewport={'width': 1280, 'height': 900})
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(P); pg.wait_for_timeout(800)
    pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(1000)
    chk(not errs, 'participant: no script errors ' + str(errs))
    titles = pg.eval_on_selector_all('.acc-t', 'els=>els.map(e=>e.textContent.trim())')
    want = ['1.1 — Measurement vs Management', '1.2 — Two Operating Systems Behind Enterprise Performance', '1.3 — The S2R® Contribution Map™', '1.4 — The FACES Framework',
            '2.1 — Performance Management as the Execution Bridge', '2.2 — Compliance vs Commitment Architecture', '3.1 — Unity in Diversity: Executive Performance Perspectives',
            '3.2 — The Continuous Performance Management Shift', '4.1 — Mapping the Contributions Required for Enterprise Results', '4.2 — Managing the Contributions Through FACES']
    for w in want: chk(w in titles, 'participant part ' + w)
    for r in ['ref13', 'ref12', 'ref14', 'ref15']: chk(pg.query_selector('#' + r) is not None, 'participant reflection ' + r)
    chk(pg.query_selector('.fac-note-full') is None, 'participant: no facilitator boxes')
    body = pg.inner_text('body')
    for w in ['FACILITATOR GUIDANCE', 'Ask:', 'Say:', 'participants']:
        chk(w not in body, 'participant has no "%s"' % w)
    # reflection save
    pg.click('.tab-btn >> nth=0'); pg.click('text=1.2 — Two Operating Systems')
    chk(pg.query_selector('.u6-pf') is None, 'no "Personal reflection" line')
    chk(pg.query_selector('.p-card') is None and len(pg.query_selector_all('.u6-hc')) >= 4, 'short cards are horizontal, no arrows')
    chk(len(pg.query_selector_all('.u6-sub')) >= 14, 'long subsections collapsed (%d)' % len(pg.query_selector_all('.u6-sub')))
    chk(not pg.is_visible('.u6-sub-b >> nth=0'), 'subsections start closed')
    for r_, part in (('ref14', '1.3'), ('ref15', '1.4')):
        chk(pg.evaluate("(id)=>document.getElementById(id).closest('.acc').querySelector('.acc-t').textContent.trim().slice(0,3)", r_) == part, r_ + ' sits in part ' + part)
    chk(pg.query_selector('#mod4 table') is None, 'Section 5 has no guidance tables')
    pg.fill('#ref13', 'Test reflection 13'); pg.wait_for_timeout(1600)
    st = pg.evaluate("window.__store['u3m1_lens5']")
    chk(st and st.get('ref13') == 'Test reflection 13', 'ref13 saves')
    # Section 5
    pg.click('.tab-btn >> nth=4'); pg.wait_for_timeout(600)
    n_obj = pg.eval_on_selector('#u6_obj', 'e=>e.options.length')
    chk(n_obj == 5, 'Objective list holds the 4 sample Objectives (%d)' % n_obj)
    chk(pg.eval_on_selector('#u6_kr', 'e=>e.disabled'), 'Key Result list waits for an Objective')
    pg.select_option('#u6_obj', index=1); pg.wait_for_timeout(300)
    n_opts = pg.eval_on_selector('#u6_kr', 'e=>e.options.length')
    chk(n_opts == 3, 'Key Result list shows the 2 Key Results of that Objective (%d)' % n_opts)
    pg.click('#u6ConfBtn'); pg.wait_for_timeout(300)
    chk('Before you confirm' in pg.inner_text('#u6Msg'), 'Confirm refused while empty')
    kr = pg.eval_on_selector('#u6_kr', 'e=>e.options[1].value')
    pg.select_option('#u6_kr', kr); pg.wait_for_timeout(300)
    chk(kr in pg.text_content('#u6KrShow2'), 'chosen Key Result shown in Activity 2')
    names = ['Customer Service', 'IT', 'Operations']
    for n in range(1, 4):
        pg.fill('#u6_f%d_name' % n, names[n - 1])
        for k in ['contrib', 'hos', 'hosm', 'esrg', 'esrgm']: pg.fill('#u6_f%d_%s' % (n, k), 'A1 %s f%d' % (k, n))
    chk(not pg.is_visible('#u6fx4'), 'FACES Function 4 hidden while unused')
    pg.click('text=Continue to Activity 2'); pg.wait_for_timeout(300)
    chk(pg.is_visible('#u6sp2'), 'Activity 2 opens')
    chk('Customer Service' in pg.inner_text('#u6fx1 .u6-s5-h'), 'Activity 2 shows the function name')
    for n in range(1, 4):
        for k in 'FACES': pg.fill('#u6_f%d_%s' % (n, k), 'A2 %s f%d' % (k, n))
    pg.evaluate('u6Step(0)'); pg.fill('#u6_f4_contrib', 'partial'); pg.wait_for_timeout(300); pg.evaluate('u6Step(1)')
    chk(pg.is_visible('#u6fx4'), 'FACES Function 4 shown once used')
    pg.click('#u6ConfBtn'); pg.wait_for_timeout(300)
    chk('Function 4' in pg.inner_text('#u6Msg'), 'Confirm refused with a half-filled Function 4')
    pg.evaluate('u6Step(0)'); pg.fill('#u6_f4_contrib', ''); pg.wait_for_timeout(300)
    pg.click('#u6ConfBtn'); pg.wait_for_timeout(1200)
    chk('Confirmed' in pg.text_content('#u6Msg'), 'Confirm succeeds')
    st = pg.evaluate("window.__store['u3m1_lens5']")
    chk('Enterprise PM System · Contribution Map' in st.get('confirmed_items', []) and 'Enterprise PM System · FACES Application' in st.get('confirmed_items', []), 'confirmed names saved')
    chk('Function 1 · Customer Service' in st.get('cm_map', '') and kr in st.get('cm_map', '') and 'Enterprise Objective' in st.get('cm_map', ''), 'cm_map text')
    chk('F · Foster a Results Culture: A2 F f1' in st.get('cm_faces', '') and 'Function 4' not in st.get('cm_faces', ''), 'cm_faces text')
    chk(isinstance(st.get('__cm_work'), dict) and st['__cm_work'].get('f2_name') == 'IT', '__cm_work saved')
    # reload restores
    pg.reload(); pg.wait_for_timeout(1200); pg.click('.tab-btn >> nth=4'); pg.wait_for_timeout(300)
    chk(pg.input_value('#u6_f3_name') == 'Operations' and pg.input_value('#u6_kr') == kr and pg.input_value('#u6_obj') != '', 'entries restored after reload')
    chk('Confirmed' in pg.text_content('#u6Rec'), 'record shows confirmed after reload')
    chk(pg.input_value('#ref13') == 'Test reflection 13', 'reflection restored after reload')
    # edit after confirm removes names
    pg.evaluate('u6Step(0)'); pg.fill('#u6_f1_hos', 'changed'); pg.wait_for_timeout(1500)
    st = pg.evaluate("window.__store['u3m1_lens5']")
    chk('Enterprise PM System · Contribution Map' not in st.get('confirmed_items', []), 'edit after Confirm takes the names out')
    if shots:
        os.makedirs(shots, exist_ok=True)
        pg.screenshot(path=os.path.join(shots, 'p_s5.png'), full_page=True)
        m = br.new_page(viewport={'width': 390, 'height': 844}); m.goto(P); m.wait_for_timeout(900)
        m.screenshot(path=os.path.join(shots, 'p_phone.png'), full_page=False)
        m.evaluate("document.querySelectorAll('.acc').forEach(a=>a.classList.add('open'))")
        wide = m.evaluate("""(()=>{var o=[];document.querySelectorAll('.main .mod.active *').forEach(e=>{if(e.closest('.u6t-wrap'))return;var r=e.getBoundingClientRect();if(r.right>392&&r.width>0)o.push(e.tagName+'.'+e.className)});return o})()""")
        chk(not wide, 'phone: Section 1 content fits the screen ' + str(wide[:5]))
    # facilitator
    fp = br.new_page(viewport={'width': 1280, 'height': 900}); ferr = []
    fp.on('pageerror', lambda e: ferr.append(str(e)))
    fp.goto(F); fp.wait_for_timeout(800)
    chk(not ferr, 'facilitator: no script errors ' + str(ferr))
    ft = fp.eval_on_selector_all('.acc-t', 'els=>els.map(e=>e.textContent.trim())')
    for w in want: chk(w in ft, 'facilitator part ' + w)
    chk(fp.query_selector_all('textarea, input, select') == [], 'facilitator: no entry boxes')
    nfg = len(fp.query_selector_all('.fac-note-full-label'))
    chk(nfg >= 18, 'facilitator guidance and activity boxes (%d)' % nfg)
    fb = fp.evaluate('document.body.textContent')
    fp.click('.mod-tab >> nth=3'); fp.wait_for_timeout(300)
    fp.evaluate("document.querySelectorAll('.acc').forEach(a=>a.classList.add('open'));document.querySelectorAll('.u6-sub').forEach(a=>a.classList.add('open'))")
    fp.click('.u6-cx >> nth=2'); fp.wait_for_timeout(200)
    chk(fp.is_visible('#u6cxd2') and not fp.is_visible('#u6cxd0'), 'facilitator: role card opens its detail')
    for w in ['Begin by asking participants', 'Accountability must follow the contribution', 'Why do we measure both employee incident-response performance', 'who must take responsibility for the performance gap']:
        chk(w in fb, 'facilitator keeps: ' + w)
    # sub-lines identical
    pm = pg.eval_on_selector_all('.acc-meta', 'els=>els.map(e=>e.textContent.trim())')
    fm = fp.eval_on_selector_all('.acc-meta', 'els=>els.map(e=>e.textContent.trim())')
    chk(pm[:10] == fm[:10], 'part sub-lines identical')
    if shots:
        fp.screenshot(path=os.path.join(shots, 'f_s1.png'), full_page=False)
    br.close()
print('%d checks pass' % ok)
for b in bad: print('FAIL', b)
sys.exit(1 if bad else 0)
