# -*- coding: utf-8 -*-
"""Browser checks of the two Unit 7 PREVIEW pages (Playwright).
Usage: python3 test_u07.py <preview folder> [<screenshot folder>]"""
import sys, os, re, json, pathlib
from playwright.sync_api import sync_playwright
folder = sys.argv[1]; shots = sys.argv[2] if len(sys.argv) > 2 else None
P = pathlib.Path(folder, 'PREVIEW - Unit 7 Participant.html').resolve().as_uri()
F = pathlib.Path(folder, 'PREVIEW - Unit 7 Facilitator.html').resolve().as_uri()
res = []
def ok(name, cond, detail=''):
    res.append((name, bool(cond), detail))
    if not cond: print('FAIL', name, detail)
TITLES = ['1.1 — Setting vs Establishing Expectations', '1.2 — The Three Conditions of Established Expectations', '1.3 — The Expectations Chain', '1.4 — The Alignment Dialogue',
          '2.1 — Compliance vs Commitment: The Execution Dynamic', '2.2 — Five Mechanisms: Why Expectation Alignment Determines Outcomes', '2.3 — Engagement & Accountability: The Two Casualties',
          '3.1 — The Alignment Brigade: CXO Expectation Tendencies & Gaps', '4.1 — The Four-Step Expectation Architecture', '4.2 — Practising the Alignment Dialogue',
          '5.1 — Building the Expectation Architecture', '5.2 — Conducting the Alignment Dialogue with the Board Chair']
SLO = ['Understand the distinction between setting vs establishing expectations.', 'Design clarity, capability and commitment to establish expectations.',
       'Explain how establishing expectations builds ownership and mutual accountability.', 'Recognise how engagement and accountability degrade when expectations are only communicated.',
       'Identify where each executive function tends to set expectations without securing ownership.', 'Recognise the contributors and dependencies each executive role relies on to deliver an agreed result.',
       'Apply a consistent leadership practice for establishing expectations across the organisation.', 'Coach individuals from partial alignment to genuine commitment.',
       'Establish delivery expectations that secure personal ownership of agreed results.', 'Confirm the contributors and commitments that make mutual accountability visible.']
BAD = ['15 min', '3 minutes', 'minutes', 'Timing', 'five working days', '5 working days', '5-Day', 'this week', 'plenary', 'triads', 'In pairs', 'at the table', 'Click a role', 'Click your role',
       'rather than', 'instead of', 'in place of', 'HoD', 'OKR/KPI', 'Role Play — Establishing']
with sync_playwright() as pw:
    b = pw.chromium.launch()
    # ───────── participant ─────────
    ctx = b.new_context(viewport={'width': 1280, 'height': 900}); pg = ctx.new_page()
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'net::' not in m.text and 'Failed to load resource' not in m.text else None)
    pg.goto(P); pg.wait_for_timeout(900)
    ok('P no script errors', not errs, str(errs[:3]))
    ok('P lock overlay hidden', pg.eval_on_selector('#p-lock-overlay', 'e=>getComputedStyle(e).display') == 'none')
    titles = pg.eval_on_selector_all('div.acc-t', 'els=>els.map(e=>e.textContent.trim())')
    ok('P twelve part titles in order', titles == TITLES, str(titles))
    slo = pg.eval_on_selector_all('.slo-box li', 'els=>els.map(e=>e.textContent.trim())')
    ok('P section outcomes', slo == SLO, str(slo))
    text = pg.evaluate('document.body.innerText')
    alltext = pg.evaluate("Array.from(document.querySelectorAll('.mod')).map(e=>e.textContent).join(' ')")
    for bad in BAD: ok('P text free of "%s"' % bad, bad not in alltext)
    ok('P no lens word', not re.search(r'\blens\b', alltext, re.I))
    ok('P no facilitator cue', not re.search(r'\b(Ask participants|Tell participants|Participants are asked)\b', alltext))
    ok('P description names the gap', 'close the gap between a well-designed performance management system and genuine commitment to deliver it' in text)
    # reflections
    refs = pg.eval_on_selector_all('textarea.reflection-textarea', 'els=>els.map(e=>e.id)')
    ok('P eight reflections (ref8 in 1.4) and the four Portfolio boxes of 4.2', refs == ['ref1', 'ref2', 'ref3', 'ref8', 'ref4', 'ref5', 'ref6', 'ref7', 'ad_goal', 'ad_reality', 'ad_options', 'ad_will'], str(refs))
    ok('P every reflection has its question marked', pg.eval_on_selector_all('.ref-block', 'els=>els.every(e=>e.querySelectorAll("p.ref-prompt").length===1)'))
    ok('P no old app_ entries', pg.evaluate("document.querySelectorAll('[id^=app_]').length") == 0)
    pg.evaluate("showMod(0,null)"); pg.fill('#ref1', 'Test reflection one'); pg.wait_for_timeout(1700)
    ok('P reflection saves', pg.evaluate("(__store.u3m1_lens6||{}).ref1") == 'Test reflection one')
    # 1.1 table, 2.1 table
    ok('P 1.1 table six rows', pg.evaluate("document.querySelectorAll('#mod0 .acc')[0].querySelectorAll('tbody tr').length") == 6)
    ok('P 1.1 KPI spelled out', 'Key performance indicator (KPI) as metric to be monitored' in alltext)
    ok('P 2.1 table six rows with How it sounds', pg.evaluate("Array.from(document.querySelectorAll('#mod1 .acc')[0].querySelectorAll('tbody tr')).map(r=>r.cells[0].textContent)") == ['How it looks', 'Behaviour pattern', 'When obstacles arise', 'Accountability', 'Energy', 'How it sounds'])
    ok('P 1.3 cards have Examples and Key question', pg.evaluate("Array.from(document.querySelectorAll('#mod0 .acc')[2].querySelectorAll('.sc-rl')).map(e=>e.textContent)") == ['Examples', 'Key question'] * 3)
    # 3.1
    pg.evaluate("showMod(2,null)"); pg.wait_for_timeout(200)
    cards = pg.query_selector_all('#mod2 .cm-card'); ok('P ten role cards', len(cards) == 10)
    good = True; first = []
    for i, c in enumerate(cards):
        c.click(); pg.wait_for_timeout(60)
        d = pg.evaluate("(i)=>{var d=document.getElementById('px'+i);return {vis:d.classList.contains('visible'),h:Array.from(d.querySelectorAll('h5')).map(e=>e.textContent),chain:Array.from(d.querySelectorAll('.u7-chain-g>div')).map(e=>e.textContent),p:d.querySelector('.cm-col p').textContent,ask:d.querySelector('.cm-q').textContent,others:document.querySelectorAll('#mod2 .cm-detail.visible').length}}", i)
        first.append(d['p'][:22])
        if not (d['vis'] and d['others'] == 1 and d['h'] == ['Typical Tendency', 'The Expectation Gap', 'Your Likely Expectations Chain'] and len(d['chain']) == 3 and all(len(x) > 15 for x in d['chain'])
                and d['p'].startswith('As ') and ', you ' in d['p'][:22] and d['ask'].startswith('Ask yourself: ')): good = False; print(i, d)
    ok('P each role card: tendency in "you", gap, chain of three, question', good, str(first))
    if shots: pg.screenshot(path=os.path.join(shots, 'p_3_1_role_card.png'), full_page=False)
    # 4.1 and 4.2
    pg.evaluate("showMod(3,null)"); pg.wait_for_timeout(200)
    ok('P 4.1 four step cards', pg.evaluate("Array.from(document.querySelectorAll('#mod3 .acc')[0].querySelectorAll('.sc-q')).map(e=>e.textContent)") == ['Start With the Future', 'Clarify the Delivery Expectation', 'Identify the Expectations Chain', 'Confirm Ownership'])
    ok('P 4.1 has no facilitator row', 'How to explain it' not in alltext)
    # 1.4 now carries the teaching of the dialogue
    pg.evaluate("showMod(0,null)"); pg.evaluate("document.querySelectorAll('#mod0 .acc')[3].classList.add('open')"); pg.wait_for_timeout(150)
    ok('P 1.4 three dialogue cards', pg.evaluate("document.querySelectorAll('#mod0 .acc')[3].querySelectorAll('.p-card').length") == 3)
    ok('P 1.4 GROW four cards', pg.evaluate("Array.from(document.querySelectorAll('#mod0 .acc')[3].querySelectorAll('.u7-grow .sc-q')).map(e=>e.textContent)") == ['Goal', 'Reality', 'Options', 'Will'])
    ok('P 1.4 GROW rows', pg.evaluate("Array.from(document.querySelectorAll('#mod0 .u7-grow .sc-card')[0].querySelectorAll('.sc-rl')).map(e=>e.textContent)") == ['What it means', 'In the Alignment Dialogue', 'Questions you ask'])
    ok('P 1.4 speaks to you', 'you explore the reasons behind the rating' in alltext and 'Your action' in alltext)
    ok('P 1.4 holds the Resolve reflection', pg.evaluate("!!document.querySelectorAll('#mod0 .acc')[3].querySelector('#ref8')"))
    ok('P no role play exercise', 'Owner brief' not in alltext)
    if shots:
        pg.evaluate("document.querySelectorAll('#mod0 .acc').forEach((a,i)=>a.classList.toggle('open',i===3))"); pg.wait_for_timeout(200); pg.screenshot(path=os.path.join(shots, 'p_1_4.png'), full_page=True)
    # 4.2 · Portfolio work
    pg.evaluate("showMod(3,null)"); pg.evaluate("document.querySelectorAll('#mod3 .acc').forEach((a,i)=>a.classList.toggle('open',i===1))"); pg.wait_for_timeout(200)
    ok('P 4.2 sub-line marks Portfolio Work', pg.evaluate("document.querySelectorAll('#mod3 .acc')[1].querySelector('.acc-meta').textContent") == 'GROW coaching model · Portfolio Work')
    ok('P 4.2 how-to box and scenario', 'Portfolio work · How to complete the Alignment Dialogue' in alltext and 'Your board chair has disagreed with the current metric and timeframe of the Key Result you have chosen.' in alltext and 'move your chair to a 10' in alltext)
    ok('P 4.2 Key Result list holds the Unit 3 Key Results', pg.evaluate("document.querySelectorAll('#ad_kr optgroup').length") == 4 and pg.evaluate("document.querySelectorAll('#ad_kr option').length") == 9)
    ok('P 4.2 four GROW boxes with their lesson', pg.evaluate("Array.from(document.querySelectorAll('#mod3 .acc')[1].querySelectorAll('.u7-s5-n')).map(e=>e.textContent)") == ['Your Key Result', 'G · Goal', 'R · Reality', 'O · Options', 'W · Will'] and pg.evaluate("document.querySelectorAll('#mod3 .acc')[1].querySelectorAll('.u7-s5-g').length") == 4)
    kr = pg.evaluate("document.querySelectorAll('#ad_kr option')[3].value"); pg.select_option('#ad_kr', kr); pg.fill('#ad_goal', 'Goal text'); pg.wait_for_timeout(1700)
    ok('P 4.2 saves as the participant works', pg.evaluate("__store.u3m1_lens6.ad_kr") == kr and pg.evaluate("__store.u3m1_lens6.ad_goal") == 'Goal text')
    if shots: pg.screenshot(path=os.path.join(shots, 'p_4_2.png'), full_page=True)
    # Section 5
    pg.evaluate("showMod(4,null)"); pg.evaluate("document.querySelectorAll('#mod4 .acc').forEach((a,i)=>{if(i<2)a.classList.add('open')})"); pg.wait_for_timeout(300)
    ok('P S5 title', pg.eval_on_selector('#mod4 .mod-hero h2', 'e=>e.textContent') == 'Establishing Delivery Expectations')
    ok('P S4 title as on the facilitator page', pg.eval_on_selector('#mod3 .mod-hero h2', 'e=>e.textContent') == 'Cross-Leadership Expectation Architecture')
    ok('P S5 four tabs', pg.eval_on_selector_all('#mod4 .step-name', 'els=>els.map(e=>e.textContent)') == ['Start With the Future', 'Clarify the Delivery Expectation', 'Identify the Expectations Chain', 'Confirm Ownership'])
    ok('P S5 marked as Capstone and group work, once', alltext.count('This is group work and Capstone work.') == 1 and alltext.count('Working as a group.') == 0 and pg.evaluate("Array.from(document.querySelectorAll('#mod4 .acc-meta')).slice(0,2).map(e=>e.textContent)") == ['Four steps · Capstone Work', 'GROW coaching model · Capstone Work'])
    ok('P S5 has no read-only lists', pg.evaluate("document.querySelectorAll('#u7Okrs,#u7Sip,#mod4 .u7-from').length") == 0)
    ok('P S5 SiP drop-down holds the four Unit 2 statements', pg.evaluate("document.querySelectorAll('#u7_o1_sipst option').length") == 5)
    ok('P S5 forty-seven entries', pg.evaluate("document.querySelectorAll('#mod4 [data-u7]').length") == 47)
    ok('P 5.2 Key Result list, scenario and four GROW boxes', pg.evaluate("document.querySelectorAll('#u7_dg_kr optgroup').length") == 4 and alltext.count('Your board chair has disagreed with the current metric and timeframe of the Key Result you have chosen.') == 2 and pg.evaluate("Array.from(document.querySelectorAll('#mod4 .acc')[1].querySelectorAll('.u7-s5-n')).map(e=>e.textContent)") == ['Your group’s Key Result', 'G · Goal', 'R · Reality', 'O · Options', 'W · Will'])
    ok('P S5 instructions 3 and 4 of Step 1', 'For each Key Result, write the part of that Future it serves.' in alltext and 'Read your Success in Practice below' not in alltext and 'Write the leader framing: the sentence that you, as the leader, say to the owner to connect the Key Result to that Future.' in alltext)
    ok('P S5 Key Result chooser waits for the Objective', pg.evaluate("document.getElementById('u7_o1_kr').disabled") is True)
    objs = pg.evaluate("Array.from(document.getElementById('u7_o1_obj').options).map(o=>o.value).filter(Boolean)")
    pg.select_option('#u7_o1_obj', objs[0]); pg.wait_for_timeout(100)
    krs = pg.evaluate("Array.from(document.getElementById('u7_o1_kr').options).map(o=>o.value).filter(Boolean)")
    ok('P S5 Key Results follow the Objective', len(krs) == 2 and 'response time' in krs[0], str(krs))
    pg.select_option('#u7_o1_kr', krs[1])
    sips = pg.evaluate("Array.from(document.getElementById('u7_o1_sipst').options).map(o=>o.value).filter(Boolean)"); pg.select_option('#u7_o1_sipst', sips[0]); pg.select_option('#u7_o2_sipst', sips[2])
    pg.select_option('#u7_o2_obj', objs[0]); pg.wait_for_timeout(100)
    k2 = pg.evaluate("Array.from(document.getElementById('u7_o2_kr').options).map(o=>o.value).filter(Boolean)"); pg.select_option('#u7_o2_kr', k2[0])
    ok('P S5 chosen Objective shows in every step', pg.evaluate("Array.from(document.querySelectorAll('.u7-o1-obj')).every(e=>e.textContent.indexOf('Deliver consistently fast')>=0)") and pg.evaluate("document.querySelectorAll('.u7-o1-obj').length") == 3)
    def fill_all(score1='7', score2='10'):
        for n in ('1', '2'):
            for k in ('owner', 'sip', 'frame', 'what', 'when', 'std', 'evid', 'up', 'up_r', 'down', 'down_r', 'ext', 'ext_r', 'coord'):
                pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_o%s_%s' % (n, k), 'T %s %s' % (n, k)])
        pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_o1_score', score1])
        pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_o2_score', score2])
        for k in ('goal', 'reality', 'options', 'will'):
            pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_dg_' + k, 'D ' + k])
    fill_all(); pg.wait_for_timeout(500)
    pg.click('#u7ConfBtn'); pg.wait_for_timeout(300)
    msg = pg.eval_on_selector('#u7Msg', 'e=>e.textContent')
    ok('P Confirm refused: same Objective twice and open follow-up entries', 'two different Objectives' in msg and '5.1 · Step 4 · Confirm Ownership (3 entries still open)' in msg and '5.2 · Alignment Dialogue with the Board Chair (1 entry still open)' in msg, msg)
    ok('P nothing confirmed yet', not pg.evaluate("((__store.u3m1_lens6||{}).confirmed_items||[]).length"))
    pg.select_option('#u7_o2_obj', objs[2]); pg.wait_for_timeout(100)
    ok('P changing the Objective clears its Key Result', pg.evaluate("U7.w.o2_kr") == '')
    k2 = pg.evaluate("Array.from(document.getElementById('u7_o2_kr').options).map(o=>o.value).filter(Boolean)"); pg.select_option('#u7_o2_kr', k2[0])
    for k, val in (('concern', 'Billing has not agreed'), ('act', 'Leader establishes it with billing'), ('score2', '11')):
        pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_o1_' + k, val])
    dk = pg.evaluate("document.querySelectorAll('#u7_dg_kr option')[2].value"); pg.select_option('#u7_dg_kr', dk)
    pg.click('#u7ConfBtn'); pg.wait_for_timeout(300)
    ok('P Confirm refused: score outside 1 to 10', 'Step 4 · Confirm Ownership (1 entry still open)' in pg.eval_on_selector('#u7Msg', 'e=>e.textContent') and '5.2' not in pg.eval_on_selector('#u7Msg', 'e=>e.textContent'), pg.eval_on_selector('#u7Msg', 'e=>e.textContent'))
    pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_o1_score2', '9'])
    pg.wait_for_timeout(1100); pg.click('#u7ConfBtn'); pg.wait_for_timeout(500)
    st = pg.evaluate("__store.u3m1_lens6")
    ok('P Confirm saves five parts and five names', all(st.get(k) for k in ('ex_future', 'ex_delivery', 'ex_chain', 'ex_ownership', 'ex_dialogue', 'ex_record', '__ex_work')) and
       st.get('confirmed_items') == ['Expectations · Start With the Future', 'Expectations · Delivery Expectation', 'Expectations · Expectations Chain', 'Expectations · Ownership', 'Expectations · Alignment Dialogue'], str(st.get('confirmed_items')))
    ok('P dialogue text for the Capstone', st['ex_dialogue'] == 'Key Result: ' + dk + '\nGoal: D goal\nReality: D reality\nOptions: D options\nWill: D will', st.get('ex_dialogue'))
    ok('P Capstone text names both Objectives and Key Results', st['ex_future'].startswith('OBJECTIVE 1: Sample (preview only): Deliver consistently fast') and 'OBJECTIVE 2: ' in st['ex_future'] and st['ex_future'].count('\nKey Result: ') == 2 and 'Leader framing: T 1 frame' in st['ex_future'] and 'Success in Practice statement: Customer Experience & Value: Sample (preview only)' in st['ex_future'] and 'The part of that Future it serves: T 1 sip' in st['ex_future'], st['ex_future'][:400])
    ok('P ownership text: follow-up lines only where the score was below 9', 'Alignment score (1 to 10): 7' in st['ex_ownership'] and 'Revised alignment score (1 to 10): 9' in st['ex_ownership'] and st['ex_ownership'].count('What stands behind the score') == 1, st['ex_ownership'])
    ok('P chain text', 'Upline · who must approve or resource this outcome: T 1 up' in st['ex_chain'] and 'Coordination required across these contributors: T 2 coord' in st['ex_chain'])
    ok('P record shows Confirmed', 'Confirmed · into your Capstone' in pg.eval_on_selector('#u7Rec', 'e=>e.textContent'))
    if shots: pg.evaluate("document.getElementById('u7Rec').scrollIntoView()"); pg.evaluate("document.querySelectorAll('#u7Rec details')[3].open=true"); pg.wait_for_timeout(150); pg.screenshot(path=os.path.join(shots, 'p_5_record.png'))
    pg.evaluate("([id,v])=>{var e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}", ['u7_o1_owner', 'COO']); pg.wait_for_timeout(1200)
    ok('P an edit after Confirm takes the names out', pg.evaluate("__store.u3m1_lens6.confirmed_items.length") == 0 and 'Not yet confirmed' in pg.eval_on_selector('#u7Rec', 'e=>e.textContent'))
    pg.reload(); pg.wait_for_timeout(900)
    ok('P entries come back after reload', pg.evaluate("document.getElementById('u7_o1_owner').value") == 'COO' and pg.evaluate("document.getElementById('u7_o1_obj').value") == objs[0] and pg.evaluate("document.getElementById('ref1').value") == 'Test reflection one' and pg.evaluate("document.getElementById('u7_o2_score').value") == '10' and pg.evaluate("document.getElementById('u7_o1_sipst').value") == sips[0] and pg.evaluate("document.getElementById('ad_kr').value") == kr and pg.evaluate("document.getElementById('ad_goal').value") == 'Goal text')
    for i in range(4):
        pg.evaluate("showMod(4,null)"); pg.evaluate("document.querySelectorAll('#mod4 .acc').forEach((a,i)=>{if(i<2)a.classList.add('open')})"); pg.evaluate("u7Step(%d)" % i); pg.wait_for_timeout(250)
        ok('P step %d tab shows its panel' % (i + 1), pg.evaluate("Array.from(document.querySelectorAll('#mod4 .step-panel')).map(p=>getComputedStyle(p).display!=='none')") == [j == i for j in range(4)])
        if shots: pg.screenshot(path=os.path.join(shots, 'p_5_step%d.png' % (i + 1)), full_page=True)
    pg.evaluate("document.querySelectorAll('.acc').forEach(a=>{if(a.querySelector('.acc-t')&&a.querySelector('.acc-t').textContent==='Unit Summary')a.classList.add('open')})")
    ok('P Unit Summary five blocks', pg.evaluate("Array.from(document.querySelectorAll('#summaryP .sum-title')).map(e=>e.textContent)") == ['What Was Established', 'Why It Matters', 'Where the Gap Appears', 'What Was Built', 'What You Applied'])
    ok('P one Submit to Facilitator', pg.evaluate("document.querySelectorAll('.send-btn').length") == 1)
    ok('P no script errors at the end', not errs, str(errs[:3]))
    ctx.close()
    # phone width
    ctx = b.new_context(viewport={'width': 390, 'height': 800}); pg = ctx.new_page(); pg.goto(P); pg.wait_for_timeout(700)
    wide = []
    for m in range(5):
        pg.evaluate("showMod(%d,null)" % m); pg.evaluate("document.querySelectorAll('#mod%d .acc').forEach(a=>a.classList.add('open'))" % m)
        if m == 2: pg.evaluate("document.querySelector('#mod2 .cm-card').click()")
        if m == 4:
            for i in range(4):
                pg.evaluate("u7Step(%d)" % i); pg.wait_for_timeout(120); wide.append(pg.evaluate("document.documentElement.scrollWidth"))
        pg.wait_for_timeout(120); wide.append(pg.evaluate("document.documentElement.scrollWidth"))
    # the page before the amendments measures 466 (Sections 1 to 4) and 541 (Section 5) at this width: the top bar and the Unit Summary header
    ok('P phone: no wider than before the amendments', max(wide[:4]) <= 466 and max(wide[4:]) <= 541, str(wide))
    if shots: pg.evaluate("showMod(4,null)"); pg.evaluate("u7Step(2)"); pg.wait_for_timeout(200); pg.screenshot(path=os.path.join(shots, 'p_phone_step3.png'))
    ctx.close()
    # ───────── facilitator ─────────
    ctx = b.new_context(viewport={'width': 1280, 'height': 900}); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(F); pg.wait_for_timeout(600)
    ok('F gate overlay hidden', pg.eval_on_selector('#f1-gate-overlay', 'e=>getComputedStyle(e).display') == 'none')
    ftitles = pg.eval_on_selector_all('div.acc-t', 'els=>els.map(e=>e.textContent.trim())')
    ok('F same part titles, then Unit Summary', ftitles == TITLES + ['Unit Summary'], str(ftitles))
    ok('F same section outcomes', pg.eval_on_selector_all('.slo-box li', 'els=>els.map(e=>e.textContent.trim())') == SLO)
    ok('F no entry field', pg.evaluate("document.querySelectorAll('.main textarea,.main input,.main select').length") == 0)
    ft = pg.evaluate("Array.from(document.querySelectorAll('.mod-panel')).map(e=>e.textContent).join(' ')")
    for bad in BAD: ok('F text free of "%s"' % bad, bad not in ft)
    ok('F no lens word', not re.search(r'\blens\b', ft, re.I))
    labels = pg.eval_on_selector_all('.fac-note-full-label', 'els=>els.map(e=>e.textContent.trim())')
    ok('F eleven PARTICIPANT ACTIVITY notes', sum(1 for l in labels if 'PARTICIPANT ACTIVITY' in l) == 11, str(labels))
    ok('F no text sits loose in a guidance box', pg.evaluate("Array.from(document.querySelectorAll('.fac-note-full')).every(b=>Array.from(b.childNodes).every(n=>n.nodeType!==3||!n.textContent.trim()))"))
    ok('F role play box and how-to-explain box', '◆ FACILITATOR GUIDANCE — Role Play in Class · The Alignment Dialogue' in labels and '◆ FACILITATOR GUIDANCE — How to explain the four steps' in labels)
    ok('F Unit Intent is the deck wording', 'This unit equips leaders to close the gap between a well-designed performance management system and genuine human commitment to deliver it.' in pg.eval_on_selector('#mod0', 'e=>e.textContent') and 'centrepiece' not in ft)
    ok('F 1.4 guidance scale', 'A 9 or 10 means go. Anything below 9' in ft)
    ok('F 2.1 six rows, no triangle', pg.evaluate("Array.from(document.querySelectorAll('#mod2 .acc')[0].querySelectorAll('th')).map(e=>e.textContent)") == ['Dimension', 'Compliance-Driven', 'Commitment-Driven'] and pg.evaluate("document.querySelectorAll('#mod2 .acc')[0].querySelectorAll('tbody tr').length") == 6)
    pg.evaluate("showMod(3)"); pg.wait_for_timeout(200)
    cards = pg.query_selector_all('#mod3 .comp-card'); good = len(cards) == 10
    for i, c in enumerate(cards):
        c.click(); pg.wait_for_timeout(50)
        d = pg.evaluate("(i)=>{var d=document.getElementById('ex'+i);return {vis:d.style.display==='block',h:Array.from(d.querySelectorAll('h5')).map(e=>e.textContent),chain:d.querySelectorAll('.u7-chain-g>div').length,ask:d.querySelector('.u7-fask').textContent}}", i)
        if not (d['vis'] and d['h'] == ['Typical Tendency', 'Expectation Gap', 'Likely Expectations Chain'] and d['chain'] == 3 and d['ask'].startswith('Ask')): good = False; print(i, d)
    ok('F each role card: tendency, gap, chain of three, question', good)
    if shots: pg.screenshot(path=os.path.join(shots, 'f_3_1_role_card.png'))
    pg.evaluate("showMod(4)"); pg.wait_for_timeout(200)
    ok('F 4.1 in the card format, no How to explain it row', pg.evaluate("Array.from(document.querySelectorAll('#mod4 .acc')[0].querySelectorAll('.sc-card')).map(c=>Array.from(c.querySelectorAll('.sc-rl')).map(e=>e.textContent).pop())") == ['Why it matters', 'Why it matters', 'Why it matters', 'What it means'] and 'How to explain it' not in ft and pg.evaluate("document.querySelectorAll('#mod4 .acc')[0].querySelectorAll('.step-tab').length") == 0)
    ok('F 4.1 explanation box comes before the cards', pg.evaluate("(function(){var a=document.querySelectorAll('#mod4 .acc')[0],b=a.querySelector('.cb .fac-note-full'),g=a.querySelector('.scarf-grid');return !!b&&b.textContent.indexOf('How to explain the four steps')>=0&&b.querySelectorAll('ol>li').length===4&&!!(b.compareDocumentPosition(g)&Node.DOCUMENT_POSITION_FOLLOWING)})()"))
    c2 = pg.query_selector_all('#mod4 .acc')[0].query_selector_all('.sc-card')[1]; c2.click(); pg.wait_for_timeout(80)
    ok('F 4.1 cards open on click', pg.evaluate("document.querySelectorAll('#mod4 .acc')[0].querySelectorAll('.sc-card')[1].classList.contains('open')"))
    if shots: pg.screenshot(path=os.path.join(shots, 'f_4_1.png'), full_page=True)
    pg.evaluate("document.querySelectorAll('#mod4 .acc')[0].classList.remove('open');document.querySelectorAll('#mod4 .acc')[1].classList.add('open')"); pg.wait_for_timeout(150)
    ok('F 4.2 is the practice: no teaching tabs, no GROW cards', pg.evaluate("document.querySelectorAll('#mod4 .acc')[1].querySelectorAll('.step-group,.u7-grow').length") == 0 and pg.evaluate("document.querySelectorAll('#mod4 .acc')[1].querySelector('.acc-meta').textContent") == 'GROW coaching model · Portfolio Work')
    ok('F role play: three decisions, seven steps, two briefs, three watch points', pg.evaluate("(function(){var b=Array.from(document.querySelectorAll('#mod4 .fac-note-full')).filter(x=>x.textContent.indexOf('Role Play in Class · The Alignment Dialogue')>=0)[0];return [Array.from(b.querySelectorAll('ol')).map(o=>o.children.length).join(','),b.querySelectorAll('.u7-brief').length,b.querySelectorAll('ul>li').length]})()") == ['3,7', 2, 3])
    ok('F 4.2 says the role play runs between any two roles the facilitator chooses', 'between any two roles that you choose' in ft)
    ok('F 4.2 PARTICIPANT ACTIVITY note with four numbered steps', pg.evaluate("(function(){var b=Array.from(document.querySelectorAll('#mod4 .acc')[1].querySelectorAll('.u7-activity'))[0];return b.querySelectorAll('ol>li').length})()") == 4 and 'the board chair has disagreed with the current metric and timeframe of that Key Result' in ft)
    if shots: pg.screenshot(path=os.path.join(shots, 'f_4_2.png'), full_page=True)
    pg.evaluate("showMod(1)"); pg.evaluate("document.querySelectorAll('#mod1 .acc').forEach((a,i)=>a.classList.toggle('open',i===3))"); pg.wait_for_timeout(200)
    ok('F 1.4 carries the three dialogue tabs and GROW', pg.evaluate("document.querySelectorAll('#mod1 .acc')[3].querySelectorAll('.step-group .step-tab').length") == 3 and pg.evaluate("Array.from(document.querySelectorAll('#mod1 .acc')[3].querySelectorAll('.u7-grow .sc-q')).map(e=>e.textContent)") == ['Goal', 'Reality', 'Options', 'Will'])
    pg.evaluate("document.querySelectorAll('#mod1 .acc')[3].querySelectorAll('.step-tab')[2].click()"); pg.wait_for_timeout(80)
    ok('F 1.4 tabs switch', pg.evaluate("Array.from(document.querySelectorAll('#mod1 .acc')[3].querySelectorAll('.step-panel')).map(p=>getComputedStyle(p).display!=='none')") == [False, False, True])
    if shots: pg.screenshot(path=os.path.join(shots, 'f_1_4.png'), full_page=True)
    pg.evaluate("showMod(5)"); pg.wait_for_timeout(200)
    ok('F S5 title and four tabs', pg.eval_on_selector('#mod5 .mod-hero h2', 'e=>e.textContent') == 'Establishing Delivery Expectations' and pg.eval_on_selector_all('#mod5 .step-name', 'els=>els.map(e=>e.textContent)') == ['Start With the Future', 'Clarify the Delivery Expectation', 'Identify the Expectations Chain', 'Confirm Ownership'])
    for i in range(4):
        pg.evaluate("u7Step(%d)" % i); pg.wait_for_timeout(100)
        ok('F step %d tab shows its panel' % (i + 1), pg.evaluate("Array.from(document.querySelectorAll('#mod5 .step-panel')).map(p=>getComputedStyle(p).display!=='none')") == [j == i for j in range(4)])
    if shots: pg.evaluate("u7Step(0)"); pg.screenshot(path=os.path.join(shots, 'f_5.png'), full_page=True)
    pg.evaluate("document.querySelectorAll('#mod5 .acc').forEach(a=>a.classList.add('open'))")
    s5 = pg.eval_on_selector('#mod5', 'e=>e.textContent')
    ok('F S5: two exercises, guidance on how the work is completed, no reviewing of group work', pg.evaluate("Array.from(document.querySelectorAll('#mod5 .acc-t')).map(e=>e.textContent)") == TITLES[10:] + ['Unit Summary'] and 'Guide how the work is completed. The Capstone work is reviewed independently at graduation.' in s5 and not any(b in s5 for b in ('Listen for', 'Challenge any', 'Watch for', 'Check that', 'Push back', 'Probe for')))
    ok('F Unit Summary five blocks, no five-day window', pg.evaluate("document.querySelectorAll('#mod5 .acc')[2].querySelectorAll('.cb > div > div').length") == 5 and 'Application — In Practice' in pg.eval_on_selector('#mod5', 'e=>e.textContent'))
    ok('F no script errors', not errs, str(errs[:3]))
    ctx.close(); b.close()
bad = [r for r in res if not r[1]]
print('%d checks, %d passed, %d failed' % (len(res), len(res) - len(bad), len(bad)))
sys.exit(1 if bad else 0)
