# -*- coding: utf-8 -*-
"""Browser checks of the Unit 9 two-views PREVIEW pages (16 Oct 2026). Usage: python3 test_u09pv.py <folder with the two PREVIEW files> [shots folder]"""
import sys, os, re
from playwright.sync_api import sync_playwright
D = sys.argv[1]; SH = sys.argv[2] if len(sys.argv) > 2 else None
P = 'file://' + os.path.abspath(os.path.join(D, 'PREVIEW - Unit 9 Participant.html'))
F = 'file://' + os.path.abspath(os.path.join(D, 'PREVIEW - Unit 9 Facilitator.html'))
ok = 0; bad = []
def check(c, m):
    global ok
    if c: ok += 1
    else: bad.append(m); print('FAIL', m)
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
    for url, v in ((P, 'p'), (F, 'f')):
        pg = b.new_page(viewport={'width': 1280, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('dialog', lambda d: d.dismiss())
        pg.goto(url); pg.wait_for_timeout(800)
        pg.evaluate("document.querySelectorAll('.mod,.mod-panel').forEach(function(x){x.classList.add('active')});document.querySelectorAll('.acc').forEach(function(a){a.classList.add('open')});document.querySelectorAll('details').forEach(function(d){d.open=true})")
        txt = pg.evaluate('document.body.innerText')
        check(not errs, '%s js errors %s' % (v, errs))
        for bad_w in ('COMPASS', 'Friction Signals', 'diagnostic triads', 'Enterprise Unclogging Agenda', 'minutes', 'KR/KPI', 'rather than'):
            check(bad_w not in txt, '%s has %s' % (v, bad_w))
        for good in ('Where clogs form', 'The Seven Performance Clogs', '1.2.1 — The ABCV Diagnostic Connection', '1.2.2 — The Three Performance Lines of Sight', '1.2.3 — Worked Diagnostic Example',
                     '3.1 — The CXO Performance Clog Contributors', '4.2 — REVIEW', '4.3 — REALIGN', '4.4 — RESTORE', '4.5 — Worked Example', '5.1 — Return to Your Original Work-Based Challenge',
                     '5.6 — The Strategic Unclogging Clinic Record', 'The 7 Strategic Unclogging Levers', 'Reveal how executive decisions', 'Classify an original organisational challenge'):
            check(good in txt, '%s missing %s' % (v, good))
        check('1.3 —' not in txt and 'Three Observable Friction Signals' not in txt, v + ' old 1.2/1.3 still there')
        check(pg.locator('.clog-card').count() == 7, v + ' clog cards')
        check(pg.locator('.u9-role-b').count() == 10, v + ' role buttons')
        # role switch
        pg.evaluate("document.querySelectorAll('.mod,.mod-panel').forEach(function(x){x.classList.add('active')});document.querySelectorAll('.acc').forEach(function(a){a.classList.add('open')})")
        check(pg.evaluate("document.querySelectorAll('details.u9-det').length") == 12, v + ' collapsible sub-parts %d' % pg.evaluate("document.querySelectorAll('details.u9-det').length"))
        pg.locator('.u9-role-b').nth(3).click(); pg.wait_for_timeout(100)
        check(pg.locator('.u9-role.on').count() == 1 and 'CHRO' in pg.locator('.u9-role.on').inner_text(), v + ' role switch')
        # clog card opens and stays open on a click inside
        c = pg.locator('.clog-card').nth(0); c.locator('.clog-head').click(); pg.wait_for_timeout(100)
        check('open' in c.get_attribute('class'), v + ' clog opens')
        c.locator('.u9-ex').click(); pg.wait_for_timeout(100)
        check('open' in c.get_attribute('class'), v + ' clog stays open on inner click')
        if v == 'f':
            check(pg.locator('textarea, select, input[type=text]').count() == 0, 'f has entry boxes')
            check('Where are our people and our organisational conditions not yet ready to carry the strategy?' in txt, 'f reframe')
            check(txt.count('PARTICIPANT ACTIVITY') >= 7, 'f activity notes %d' % txt.count('PARTICIPANT ACTIVITY'))
            check('Question for participants' in txt and 'Your question' not in txt, 'f question label')
            check(pg.locator('table.u9-rrr').count() == 2 and pg.locator('td.u9-stage').count() == 3, 'f reflection tables')
            check(txt.lower().index('capstone portfolio output') < txt.lower().index('5.1 — return'), 'f output before 5.1')
        else:
            check('Your question' in txt and 'Question for participants' not in txt, 'p question label')
            for k in ('ref1', 'ref2', 'ref3', 'ref4', 'ref7', 'ref8'): check(pg.locator('#' + k).count() == 1, 'p key ' + k)
            # ref7 / ref8 save through the field widgets
            pg.locator('[data-fkey="ref7"][data-fidx="0"]').fill('Chief Financial Officer')
            pg.locator('[data-fkey="ref8"][data-fidx="5"]').select_option('02 · Streamline')
            pg.wait_for_timeout(1200)
            check('My executive function: Chief Financial Officer' in pg.locator('#ref7').input_value(), 'ref7 sync')
            check('The Unclogging Lever: 02 · Streamline' in pg.locator('#ref8').input_value(), 'ref8 sync')
            check(txt.lower().index('capstone portfolio output') < txt.lower().index('5.1 — return'), 'p output before 5.1')
            # Section 5: confirm refused when empty, then fill all and confirm
            pg.locator('#u9ConfBtn').click(); pg.wait_for_timeout(300)
            check('Before you confirm' in pg.locator('#u9Msg').inner_text(), 'confirm refused')
            ids = pg.evaluate("Array.from(document.querySelectorAll('[data-u9]')).map(function(e){return [e.id,e.tagName]})")
            check(len(ids) == 21, 'S5 boxes %d' % len(ids))
            for i, tg in ids:
                if tg == 'SELECT': pg.locator('#' + i).select_option(index=2)
                else: pg.locator('#' + i).fill('Sample ' + i)
            pg.wait_for_timeout(1300)
            pg.locator('#u9ConfBtn').click(); pg.wait_for_timeout(800)
            check('Confirmed' in pg.locator('#u9Msg').inner_text(), 'confirm ok: ' + pg.locator('#u9Msg').inner_text())
            st = pg.evaluate("JSON.parse(localStorage.getItem('u9_preview_store')||'{}')")
            s = st.get('u3m2_lens8', st)
            flat = str(st)
            for k in ('uc_challenge', 'uc_clog', 'uc_lever', 'uc_review_realign', 'uc_restore'): check(k in flat, 'saved ' + k)
            check('Unclogging · Restore' in flat, 'confirmed names')
            check('Selected clog: Capability Gaps' in flat, 'clog value saved')
            # Unit 7 Key Results shown read-only
            check('key result 1' in pg.locator('#u9Krs').inner_text().lower(), 'u7 KRs shown')
            # edit after confirm drops the confirmation
            pg.locator('#u9_cl_why').fill('changed'); pg.wait_for_timeout(1200)
            check('not yet confirmed' in pg.locator('#u9Rec').inner_text().lower(), 'edit unconfirms')
        if SH:
            os.makedirs(SH, exist_ok=True)
            for n, sel in enumerate(['#mod0' if v == 'p' else '#mod1', '#mod2' if v == 'p' else '#mod3', '#mod3' if v == 'p' else '#mod4', '#mod4' if v == 'p' else '#mod5']):
                pg.evaluate("document.querySelectorAll('.mod,.mod-panel').forEach(function(x){x.classList.remove('active')});document.querySelector('%s').classList.add('active');window.scrollTo(0,0)" % sel)
                pg.screenshot(path=os.path.join(SH, '%s_%s.png' % (v, sel[1:])), full_page=True)
        pg.close()
    # phone width
    pg = b.new_page(viewport={'width': 390, 'height': 800}); pg.goto(P); pg.wait_for_timeout(500)
    pg.evaluate("document.querySelectorAll('.mod,.mod-panel').forEach(function(x){x.classList.add('active')});document.querySelectorAll('.acc').forEach(function(a){a.classList.add('open')});document.querySelectorAll('.clog-card').forEach(function(a){a.classList.add('open')})")
    wide = pg.evaluate("""(function(){var o=[];document.querySelectorAll('[class*="u9-"],[class*="u8v-"],.clog-card').forEach(function(e){if(e.closest('.u9-tw'))return;var r=e.getBoundingClientRect();if(r.width>0&&r.right>392)o.push(e.className+' '+Math.round(r.right));});return o;})()""")
    check(not wide, 'phone: new blocks wider than the screen %s' % wide[:5])  # the page's own tab bar is wider at 390px, as before
    b.close()
print('%d checks passed, %d failed' % (ok, len(bad)))
