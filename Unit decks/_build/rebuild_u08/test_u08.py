# -*- coding: utf-8 -*-
"""Browser checks of the Unit 8 PREVIEW pages. Usage: python3 test_u08.py <preview folder> [<screenshot folder>]"""
import sys, os, re, json
from playwright.sync_api import sync_playwright
folder = sys.argv[1]; shots = sys.argv[2] if len(sys.argv) > 2 else None
P = 'file://' + os.path.abspath(os.path.join(folder, 'PREVIEW - Unit 8 Participant.html'))
F = 'file://' + os.path.abspath(os.path.join(folder, 'PREVIEW - Unit 8 Facilitator.html'))
ok = 0; bad = []
def check(c, what):
    global ok
    if c: ok += 1
    else: bad.append(what); print('FAIL', what)
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, url in (('p', P), ('f', F)):
        pg = b.new_page(viewport={'width': 1280, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(url); pg.wait_for_timeout(900)
        check(not errs, name + ' page errors: ' + str(errs))
        titles = pg.eval_on_selector_all('.acc-t', 'els=>els.map(e=>e.textContent.trim())')
        print(name, titles)
        if name == 'p': pt = titles
        else: ft = titles
        h2 = pg.eval_on_selector_all('.mod-hero h2', 'els=>els.map(e=>e.textContent.trim())')
        if name == 'p': ph2 = h2
        else: fh2 = h2[1:]
        slo = pg.eval_on_selector_all('.slo-box li', 'els=>els.map(e=>e.textContent.trim())')
        if name == 'p': pslo = slo
        else: fslo = slo
        subs = pg.eval_on_selector_all('.acc-meta', 'els=>els.map(e=>e.textContent.trim())')
        if name == 'p': psub = subs
        else: fsub = subs
        allv = pg.content()
        check('Brigade' not in allv and 'Criterion 0' not in allv, name + ': no Brigade, no criteria')
        if name == 'f':
            check(pg.locator('#main textarea, .main textarea, .main input, .main select').count() == 0, 'facilitator page has no entry box')
            for i in range(6):
                pg.evaluate('showMod(%d)' % i); pg.wait_for_timeout(150)
                if shots: pg.screenshot(path=os.path.join(shots, 'f_mod%d.png' % i), full_page=True)
            pg.evaluate('u8Step(3)'); pg.wait_for_timeout(100)
            check(pg.locator('#u8sp4.active').count() == 1, 'facilitator step 4 opens')
            vis = pg.inner_text('body')
            for w in ('Brigade', 'Criterion', 'criteria', 'Timing', 'five working days', 'Collective Intelligence Board', 'Report Role', 'Watch for: leaders in the Integration', 'Synthesis Layer', 'three signals:'):
                check(w not in vis, 'facilitator: ' + w)
            check(pg.locator('.u8-activity').count() == 7, 'facilitator: 7 PARTICIPANT ACTIVITY notes (got %d)' % pg.locator('.u8-activity').count())
        else:
            for i in range(5):
                pg.evaluate('showMod(%d,null)' % i); pg.wait_for_timeout(150)
                if shots: pg.screenshot(path=os.path.join(shots, 'p_mod%d.png' % i), full_page=True)
            check(pg.locator('.ref-prompt').count() == 7, 'participant: 7 ref-prompt questions (got %d)' % pg.locator('.ref-prompt').count())
            pg.evaluate('showMod(1,null)'); pg.fill('#ref8', 'Velocity gap here.'); pg.wait_for_timeout(1500)
            check(pg.evaluate('window.__store["u3m2_lens7"]').get('ref8') == 'Velocity gap here.', 'ref8 (velocity) saves')
            check(pg.locator('#mod3 .u8-grow4 > div').count() == 4, 'GROW panel in 4.2')
            check(pg.locator('#mod0 .u8-growl').count() == 3, 'GROW recovery in each 1.4 card')
            # reflection saves
            pg.evaluate('showMod(0,null)'); pg.fill('#ref1', 'Activity: projects. Progress: resolution time.'); pg.wait_for_timeout(1500)
            st = pg.evaluate('window.__store["u3m2_lens7"]')
            check(st.get('ref1', '').startswith('Activity'), 'ref1 saves')
            pg.evaluate('showMod(3,null)'); pg.evaluate("document.querySelectorAll('#mod3 .acc').forEach(a=>a.classList.add('open'))")
            for k in ('rp_review', 'app_rootcause', 'app_corrective', 'rp_judge'): pg.fill('#' + k, 'Answer ' + k)
            pg.wait_for_timeout(1600)
            st = pg.evaluate('window.__store["u3m2_lens7"]')
            check(all(st.get(k) == 'Answer ' + k for k in ('rp_review', 'app_rootcause', 'app_corrective', 'rp_judge')), 'the four 4.2 answers save')
            check(pg.locator('.u8-dlg-r').count() == 16, 'conversation shown')
            # 3.2 cards
            pg.evaluate('showMod(2,null)'); pg.evaluate("document.querySelectorAll('#mod2 .acc').forEach(a=>a.classList.add('open'))")
            pg.locator('.u8-cx-card').nth(2).click(); pg.wait_for_timeout(100)
            check(pg.locator('#u8cx2.visible').count() == 1 and 'As COO' in pg.inner_text('#u8cx2'), '3.2 role card opens')
            # Section 5
            pg.evaluate('showMod(4,null)'); pg.wait_for_timeout(300)
            fields = pg.evaluate('U8F')
            pg.click('#u8ConfBtn'); pg.wait_for_timeout(200)
            check('Before you confirm' in pg.inner_text('#u8Msg'), 'Confirm refuses an empty record')
            for f in fields:
                pg.evaluate('u8Step(%d)' % (int(f[2][1]) - 1)); pg.fill('#u8_' + f[0], 'If signal for ' + f[0] + ', then decision, taken by CEO.')
            pg.wait_for_timeout(1300)
            pg.click('#u8ConfBtn'); pg.wait_for_timeout(600)
            check('Confirmed' in pg.inner_text('#u8Msg'), 'Confirm succeeds: ' + pg.inner_text('#u8Msg'))
            st = pg.evaluate('window.__store["u3m2_lens7"]')
            for k in ('rd_warning', 'rd_accountability', 'rd_learning', 'rd_credibility', 'rd_record', '__rd_work'):
                check(k in st, 'saved ' + k)
            names = ['Review Discipline · Early Warning Signals', 'Review Discipline · Accountability', 'Review Discipline · Organisational Learning', 'Review Discipline · Leadership Credibility']
            check(all(n in st.get('confirmed_items', []) for n in names), 'four names in confirmed_items')
            print('--- rd_warning ---'); print(st.get('rd_warning'))
            pg.fill('#u8_c4_dp2', 'Changed'); pg.wait_for_timeout(1500)
            st = pg.evaluate('window.__store["u3m2_lens7"]')
            check(not any(n in st.get('confirmed_items', []) for n in names), 'edit after Confirm removes the names')
            pg.reload(); pg.wait_for_timeout(1200)
            check(pg.input_value('#u8_c1_dp1').startswith('If signal'), 'reload restores Section 5')
            check(pg.input_value('#rp_judge') == 'Answer rp_judge', 'reload restores 4.2')
            if shots:
                pg.evaluate('showMod(4,null)')
                for i in range(4):
                    pg.evaluate('u8Step(%d)' % i); pg.wait_for_timeout(150)
                    pg.screenshot(path=os.path.join(shots, 'p_s5_c%d.png' % (i + 1)), full_page=True)
            # phone width
            pg.set_viewport_size({'width': 390, 'height': 800}); pg.wait_for_timeout(200)
            w = pg.evaluate('document.documentElement.scrollWidth')
            check(pg.evaluate("document.getElementById('u8S5').scrollWidth") <= 392, 'Section 5 tool fits at phone width')
            if shots: pg.screenshot(path=os.path.join(shots, 'p_phone_s5.png'), full_page=False)
        pg.close()
    b.close()
check(pt[:11] == ft, 'part titles identical:\n%s\n%s' % (pt, ft))
check(ph2 == fh2, 'section titles identical: %s / %s' % (ph2, fh2))
check(pslo == fslo, 'section outcomes identical')
check(psub[:10] == fsub[:10], 'sub-lines identical:\n%s\n%s' % (psub, fsub))
print('%d passed, %d failed' % (ok, len(bad)))
