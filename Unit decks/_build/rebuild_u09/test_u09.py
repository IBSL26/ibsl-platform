# -*- coding: utf-8 -*-
"""Browser checks of the Unit 9 PREVIEW pages. Usage: python3 test_u09.py <preview folder> [<screenshot folder>]"""
import sys, os, re, json
from playwright.sync_api import sync_playwright
folder = sys.argv[1]; shots = sys.argv[2] if len(sys.argv) > 2 else None
if shots: os.makedirs(shots, exist_ok=True)
P = 'file://' + os.path.abspath(os.path.join(folder, 'PREVIEW - Unit 9 Participant.html'))
F = 'file://' + os.path.abspath(os.path.join(folder, 'PREVIEW - Unit 9 Facilitator.html'))
ok = 0; bad = []
def check(c, what):
    global ok
    if c: ok += 1
    else: bad.append(what); print('FAIL', what)
R = {}
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, url in (('p', P), ('f', F)):
        pg = b.new_page(viewport={'width': 1280, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(url); pg.wait_for_timeout(1200)
        check(not errs, name + ' page errors: ' + str(errs))
        R[name] = dict(titles=pg.eval_on_selector_all('.acc-t', 'els=>els.map(e=>e.textContent.trim())'),
                       h2=pg.eval_on_selector_all('.mod-hero h2', 'els=>els.map(e=>e.textContent.trim())'),
                       slo=pg.eval_on_selector_all('.slo-box li', 'els=>els.map(e=>e.textContent.trim())'),
                       meta=pg.eval_on_selector_all('.acc-meta', 'els=>els.map(e=>e.textContent.trim())'))
        print(name, R[name]['titles'])
        if name == 'f':
            check(pg.locator('.main textarea, .main input, .main select').count() == 0, 'facilitator page has no entry box')
            for i in range(6):
                pg.evaluate('showMod(%d)' % i); pg.wait_for_timeout(150)
                if shots: pg.screenshot(path=os.path.join(shots, 'f_mod%d.png' % i), full_page=True)
            pg.evaluate('u9Step(3)'); pg.wait_for_timeout(100)
            check(pg.locator('#u9sp4.active').count() == 1, 'facilitator step tabs switch')
        else:
            pg.evaluate('showMod(4,null)'); pg.wait_for_timeout(400)
            krs = pg.inner_text('#u9Krs'); check('Reduce average response time' in krs and 'owner' in krs.lower(), 'Unit 7 Key Results show: ' + krs[:80])
            pg.evaluate('u9Step(3)'); pg.wait_for_timeout(200)
            rd = pg.inner_text('#u9Rd'); check('early warning signals' in rd.lower(), 'Unit 8 decision points show')
            # Confirm refused while empty
            pg.evaluate('u9Confirm()'); pg.wait_for_timeout(300)
            check('Before you confirm' in pg.inner_text('#u9Msg'), 'confirm refused while entries are open')
            # fill every required entry
            fl = pg.evaluate('U9F')
            for f in fl:
                if f[3]: continue
                pg.evaluate('u9Step(%d)' % (int(f[2][1]) - 1))
                sel = '#u9_' + f[0]
                if f[4] == 's': pg.select_option(sel, index=1)
                else: pg.fill(sel, 'Test ' + f[0])
            pg.wait_for_timeout(1200)
            pg.evaluate('u9Confirm()'); pg.wait_for_timeout(800)
            st = pg.evaluate("JSON.parse(localStorage.getItem('u9_preview_store'))['u3m2_lens8']")
            for k in ('uc_signals', 'uc_diagnosis', 'uc_levers', 'uc_rhythm', 'uc_agenda', 'uc_record', '__uc_work'): check(k in st, 'saved ' + k)
            check(len([x for x in st.get('confirmed_items', []) if x.startswith('Unclogging · ')]) == 5, 'five names in confirmed_items')
            check('Key Result 1 · The friction signal: Decision Paralysis' in st.get('uc_signals', ''), 'signals text: ' + st.get('uc_signals', '')[:90])
            check('Action 3' not in st.get('uc_agenda', ''), 'optional empty action left out')
            # edit after confirm drops names
            pg.evaluate('u9Step(3)'); pg.fill('#u9_r_forum', 'Changed'); pg.wait_for_timeout(1500)
            st = pg.evaluate("JSON.parse(localStorage.getItem('u9_preview_store'))['u3m2_lens8']")
            check(not [x for x in st.get('confirmed_items', []) if x.startswith('Unclogging · ')], 'edit after confirm takes the names out')
            pg.evaluate('u9Confirm()'); pg.wait_for_timeout(800)
            # Portfolio fields of 4.4 and reflections save and reload
            pg.evaluate('showMod(3,null)'); pg.wait_for_timeout(200)
            pg.click('.acc-t:has-text("4.4")'); pg.wait_for_timeout(200)
            pg.select_option('[data-fkey="tc_diag"][data-fidx="0"]', index=2)
            pg.fill('[data-fkey="tc_prep"][data-fidx="0"]', 'My KR test'); pg.wait_for_timeout(1300)
            pg.evaluate('showMod(0,null)'); pg.fill('#ref1', 'Reflection one test'); pg.wait_for_timeout(1500)
            pg.reload(); pg.wait_for_timeout(1500)
            pg.evaluate('showMod(3,null)'); pg.click('.acc-t:has-text("4.4")'); pg.wait_for_timeout(200)
            check(pg.input_value('[data-fkey="tc_prep"][data-fidx="0"]') == 'My KR test', 'tc_prep reloads')
            check(pg.input_value('[data-fkey="tc_diag"][data-fidx="0"]').startswith('Organisational Alignment'), 'tc_diag select reloads')
            check(pg.input_value('#ref1') == 'Reflection one test', 'ref1 reloads')
            check(pg.input_value('#u9_r_forum') == 'Changed', 'Section 5 entry reloads')
            check('Confirmed' in pg.inner_text('#u9Rec'), 'confirmed state reloads')
            check(pg.locator('.ref-prompt').count() == 5, 'five reflections carry ref-prompt: %d' % pg.locator('.ref-prompt').count())
            check(pg.locator('#summaryP .sum-block').count() == 5, 'five summary blocks')
            for i in range(5):
                pg.evaluate('showMod(%d,null)' % i); pg.wait_for_timeout(150)
                if shots: pg.screenshot(path=os.path.join(shots, 'p_mod%d.png' % i), full_page=True)
            if shots:
                ph = b.new_page(viewport={'width': 390, 'height': 844}); ph.goto(url); ph.wait_for_timeout(1000)
                ph.evaluate('showMod(4,null)'); ph.wait_for_timeout(300); ph.screenshot(path=os.path.join(shots, 'phone_s5.png'), full_page=False)
    # three-way between the two pages
    p, f = R['p'], R['f']
    pt = [x for x in p['titles'] if re.match(r'\d\.\d', x)]; ft = [x for x in f['titles'] if re.match(r'\d\.\d', x)]
    check([x.replace('Your Two Key Results', '').strip() for x in pt] == [x.replace('the Group’s Two Key Results', '').strip() for x in ft], 'part titles match: %s | %s' % (pt, ft))
    check(p['h2'] == f['h2'][1:], 'section titles match')
    check(p['slo'] == f['slo'], 'section outcomes match')
print('%d passed, %d failed' % (ok, len(bad)))
