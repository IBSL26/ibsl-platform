# -*- coding: utf-8 -*-
"""Unit 5 amendments of 8 October 2026 (evening) — participant file, on Carol's word.
Usage: python3 amend_p.py <participant file built by build_p.py> <new file>
Run it from this folder: it reads u5b_content.py, oceavl.json, u5b.css, u5_p.js and u5b_p.js.
Chain: file before the three-way match -> build_p.py -> amend_p.py.
Every change is an exact replacement that must match the number of times given, or the build stops. Line endings (CRLF) and UTF-8 are kept."""
import sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5b_content as B
src, out = sys.argv[1], sys.argv[2]
def read(name): return open(os.path.join(HERE, name), 'rb').read().decode('utf-8').replace('\r\n', '\n')
h = open(src, 'rb').read().decode('utf-8')
assert h.count('\r\n') == h.count('\n'), 'expected CRLF line endings'
h = h.replace('\r\n', '\n')
h0 = h
def rep(old, new, count=1):
    global h
    n = h.count(old)
    assert n == count, 'expected %d match(es), found %d: %s' % (count, n, old[:110])
    h = h.replace(old, new)
def cut(start, end, new):
    """Replace everything from the start marker up to (not including) the end marker."""
    global h
    assert h.count(start) == 1 and h.count(end) == 1, (h.count(start), h.count(end), start[:60])
    i, j = h.index(start), h.index(end)
    assert i < j
    h = h[:i] + new + h[j:]
def how(title, steps, close=''):
    return ('<div class="u5-how"><div class="u5-how-h">' + title + '</div><ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>' +
            ('<p>' + close + '</p>' if close else '') + '</div>\n')
ACC = '<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">'
ARR = '<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div>\n</div>\n<div class="acc-b cb">\n'
def acc_head(title, meta, cls='acc'):
    return ('<div class="' + cls + '">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">' + title + '</span>\n'
            '  <div style="display:flex;align-items:center;gap:10px;"><span class="acc-meta">' + meta + '</span>' + ARR)
def reflection(rid, label, prompt):
    return ('  <div class="ref-block" style="margin-top:18px;"><div class="ref-label">&#x270E; Reflection &mdash; ' + label + '</div>\n'
            '    <label class="wp-label" style="margin-top:0;" for="' + rid + '">' + prompt + '</label>\n'
            '    <textarea class="ref-ta reflection-textarea" id="' + rid + '" placeholder="Your reflection..."></textarea>\n'
            '    <div class="ref-saved reflection-saved" id="' + rid + '-saved"></div>\n'
            '    <button class="ref-save" onclick="saveTA(this)">Save Reflection</button>\n  </div>\n')
GROUP = '<div class="u5-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>\n'
assert GROUP in h

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + read('u5b.css') + h[i:]

# ── 1. Part 1.2 · Principle 1: Carol's text of 8 October ───────────────────────────────────────────
cut('        <p>Cognitive alignment focuses on', '        <div class="p-insight">&#10148; Insight: Can you name the dominant emotion', B.principle1_chain())
rep('Allows leaders to stabilise engagement before demanding execution.', 'Allows you to stabilise engagement before demanding execution.')
rep('        <p>Both available on demand.</p>', '        <p>You complete the OCEAVL Assessment in part 3.1. The Emotional Climate Assessment is available on demand.</p>')

# ── 2. Section 1: the four tools are parts of change management (1.3.1 to 1.3.4) ───────────────────
for old, new, name in (('1.4', '1.3.1', 'The 3S Check: Shift, Stake, Step'), ('1.5', '1.3.2', 'The SCARF Model: Five Triggers of Human Resistance'),
                       ('1.6', '1.3.3', 'The STAT Check: Skill, Time, Authority, Tools'), ('1.7', '1.3.4', 'ACE-IT: The Observable Behaviour Standard')):
    rep(ACC + old + ' &mdash; ' + name + '</span>', ACC.replace('class="acc"', 'class="acc u5-sub"') + new + ' &mdash; ' + name + '</span>')
rep('explored in detail in section 1.5.</p>', 'explored in detail in part 1.3.2.</p>')
rep('Explored in detail in section 1.7.</p>', 'Explored in detail in part 1.3.4.</p>')
rep('the 3S Check (1.4).', 'the 3S Check (1.3.1).')
rep('the SCARF Model (1.5).', 'the SCARF Model (1.3.2).')
rep('the STAT Check (1.6).', 'the STAT Check (1.3.3).')
rep('ACE-IT (1.7).', 'ACE-IT (1.3.4).')

# ── 3. Participant voice, second pass (the reader is the leader) ───────────────────────────────────
VOICE2 = [
    ('how far through their own transition were the leaders, and how far were the people affected?', 'how far through your own transition were you and your fellow leaders, and how far were the people affected?'),
    ('and those conditions are set by leaders.</p>', 'and those conditions are set by you and your fellow leaders.</p>'),
    ('A leader who reads that as resistance answers with more persuasion, when the gap is', 'If you read that as resistance, you answer with more persuasion, when the gap is'),
    ('and leaders become the bottleneck.</div>', 'and you become the bottleneck.</div>'),
    ('What leaders ask about, people repeat.', 'What you ask about, people repeat.'),
    ('and adoption holds when leaders notice and reinforce the new practice.</p>', 'and adoption holds when you notice and reinforce the new practice.</p>'),
    ('The 4 Checks describe what one group of people needs from one leader. Most changes reach a group through several leaders at once. People hear from their own leader, watch the others, and compare. Where the leaders differ, the group takes the difference as the real message.',
     'The 4 Checks describe what one group of people needs from you. Most changes reach a group through several leaders at once. People hear from you, watch your fellow leaders, and compare. Where you differ, the group takes the difference as the real message.'),
    ('Every leader gives the same Shift, Stake and Step for each change. The Functional Bias Problem works on leaders first: each one translates the change through their own function before passing it on.',
     'You and your fellow leaders give the same Shift, Stake and Step for each change. The Functional Bias Problem works on you first: each of you translates the change through your own function before passing it on.'),
    ('Each leader writes the three for the same change, and the versions are compared before anyone speaks to their people.', 'Each of you writes the three for the same change, and you compare the versions before anyone speaks to their people.'),
    ('Leaders show the ACE-IT behaviours the change needs before they ask for them. People read a leader&rsquo;s diary, questions and decisions as the real message. A leader who asks for the new practice and keeps to the old one has told the organisation which of the two is safe.',
     'You show the ACE-IT behaviours the change needs before you ask for them. People read your diary, questions and decisions as the real message. If you ask for the new practice and keep to the old one, you have told the organisation which of the two is safe.'),
    ('People copy what leaders do and discount what leaders say.', 'People copy what you do and discount what you say.'),
    ('Leaders pool their changes and count how many land on the same group in the same period.', 'You and your fellow leaders pool your changes and count how many land on the same group in the same period.'),
]
for a, b in VOICE2: rep(a, b)

# ── 4. Section 3: the OCEAVL Assessment takes the place of COMPASS; 3.2 (Burning Platforms) leaves; Change Readiness becomes 3.2 ──
rep('  <h2>Where Are the Alignment Hot Zones Across the Organisation?</h2>\n  <p>The COMPASS framework identifies seven High Flammable Zones where human interpretation, emotional climate, and behaviour directly influence strategic outcomes. These are the leverage points &mdash; and the danger zones.</p>',
    '  <h2>' + B.HERO3_H + '</h2>\n  <p>' + B.HERO3_P + '</p>')
s31 = (acc_head('3.1 &mdash; ' + B.T31, B.T31_META, 'acc open') + B.oceavl_teach('p') +
       '  <h4>Your assessment</h4>\n  ' + how('Portfolio work &middot; How to complete your OCEAVL Assessment', B.OC_HOW, B.OC_CLOSE) +
       '  <div id="ocGrid"></div>\n  <div id="ocProfile"></div>\n  <div id="ocConf"></div>\n' +
       reflection('ref16', B.REF16_LABEL, B.REF16) + '</div>\n</div>\n\n')
cut('<div class="acc open">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">3.1 &mdash; The COMPASS Framework',
    '<div class="mod-nav">\n  <button class="btn prev" onclick="showMod(1,null)">', s31)   # 3.2 (Burning Platforms) and 3.3 (Change Readiness) leave with it

# ── 5a. Section 4: COMPASS leaves; each role card names its alignment hot zone ───────────────────────
import u5_content as C
for a, b in B.SEC4: rep(a, b)
rep('  <p style="margin-bottom:14px;">Click your own role first. Then explore the roles most closely connected to yours.</p>',
    '  <p style="margin-bottom:14px;">Click your own role first. Then explore the roles most closely connected to yours.</p>\n  <p>' + B.HOT_INTRO_P + '</p>')
for n in range(10):
    old = C.role_detail(n, 'p'); rep(old, B.role_detail(n, 'p', old))

# ── 5. Section 5: the Alignment Toolkit ────────────────────────────────────────────────────────────
m = re.search(r'  <h2>Building Collective Intelligence Through Shared Interpretation</h2>\n  <p>This exercise highlights how Collective Intelligence emerges when you and your colleagues.*?</p>', h)
assert m and h.count(m.group(0)) == 1
h = h[:m.start()] + '  <h2>' + B.T5 + '</h2>\n  <p>' + B.HERO5_P + '</p>' + h[m.end():]
commit = ('<div class="u5-how"><div class="u5-how-h">Portfolio work &middot; Your 30-Day Behavioural Commitment</div><p>Your 30-Day Behavioural Commitment is your own. It is Portfolio work and reaches your facilitator when you select Submit to Facilitator at the end of the unit.</p></div>\n'
          '<div style="margin:16px 0;">\n  <label class="wp-label" style="margin-top:0;" for="syn_30day">Your 30-Day Behavioural Commitment</label>\n'
          '  <textarea class="wp-ta reflection-textarea" id="syn_30day" placeholder="What specific behaviour will you change in the next 30 days? How will you and others know it has happened?"></textarea>\n'
          '  <div class="ref-saved reflection-saved" id="syn_30day-saved"></div>\n  <button class="wp-save" onclick="saveTA(this)">Save Commitment</button>\n</div>\n')
assert commit in h, 'the 30-day commitment block is not as expected'
u3box = ('<div class="u5-u3">\n<div class="chg-h" style="margin-top:6px;">From Unit 3 &middot; your group&rsquo;s confirmed Start and Stop lists</div>\n<div id="u5KissP"></div>\n'
         '<div class="u5-btnrow"><button type="button" class="u5-b" onclick="u5Bring(true)">Bring in from my Unit 3 page</button></div>\n<div class="u5-note" id="u5BringMsg" style="display:none;"></div>\n</div>\n')
assert u3box in h
NEXT = lambda i, name: '<div class="u5-btnrow"><button type="button" class="u5-b ok" onclick="u5Step(%d)">Go to Step %d &middot; %s &rarr;</button></div>\n' % (i, i + 1, name)
SEC5HOW = '<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div><ul>' + ''.join('<li>' + x + '</li>' for x in B.SEC5_HOW_P) + '</ul></div>\n\n'
s5 = (SEC5HOW + '<div class="step-tabs">\n'
      '  <div class="step-tab active" onclick="showSP(\'m\',this)"><div class="step-num">Step 1</div><div class="step-name">' + B.STEP_NAMES[0] + '</div></div>\n'
      '  <div class="step-tab" onclick="showSP(0,this)"><div class="step-num">Step 2</div><div class="step-name">' + B.STEP_NAMES[1] + '</div></div>\n'
      '  <div class="step-tab" onclick="showSP(1,this)"><div class="step-num">Step 3</div><div class="step-name">' + B.STEP_NAMES[2] + '</div></div>\n'
      '</div>\n\n<div class="step-panel active" id="spm">\n' + B.toolkit_step1() + NEXT(1, B.STEP_NAMES[1]) + '</div>\n\n'
      '<div class="step-panel" id="sp0">\n' + how('Portfolio work &middot; How to complete Your Watch List', B.ME_HOW, B.ME_CLOSE) + u3box +
      '<div class="u5-group">' + B.ME_EXAMPLE + '</div>\n<div class="chg-h">Your watch list</div>\n<p class="u5-hint">' + B.ME_HINT + '</p>\n<div id="kitMe"></div>\n' + NEXT(2, B.STEP_NAMES[2]) + '</div>\n\n'
      '<div class="step-panel" id="sp1">\n' + GROUP + how('Capstone work &middot; How to complete the Team Alignment Plan', B.TEAM_HOW) +
      '<p class="u5-hint">' + B.TEAM_HINT + '</p>\n<div id="kitTeam"></div>\n<div id="kitOutP"></div>\n' + commit)
cut('<div class="step-tabs">', '<div class="hbox" style="margin-top:18px;"><p><strong>Unit Outcome:</strong>', s5)
rep(B.OUTCOME_TAIL_OLD_P, B.OUTCOME_TAIL_P)

# ── 6. Script ─────────────────────────────────────────────────────────────────────────────────────
m = re.search(r'var SUMMARY=(\[.*?\]);\n', h, re.S); S = json.loads(m.group(1)); assert len(S) == 5
assert 'COMPASS framework' in S[2]['body'] and 'COMPASS' in S[4]['body']
S[2]['body'] = B.SUMMARY_P3; S[4]['body'] = B.SUMMARY_P5
assert S[3]['body'].count(B.SUMMARY_P4_OLD) == 1; S[3]['body'] = S[3]['body'].replace(B.SUMMARY_P4_OLD, B.SUMMARY_P4_NEW)
h = h[:m.start()] + 'var SUMMARY=' + json.dumps(S, ensure_ascii=False) + ';\n' + h[m.end():]
m = re.search(r'var KEYS=\[[^\]]*\];', h); assert m and h.count(m.group(0)) == 1 and '"syn_missing_compass"' in m.group(0)
KEYS = ['ref1', 'ref2', 'ref3', 'ref4', 'ref5', 'ref6', 'ref8', 'ref9', 'ref10', 'ref11', 'ref12', 'ref13', 'ref15', 'ref16', 'syn_30day']
h = h[:m.start()] + 'var KEYS=' + json.dumps(KEYS, separators=(',', ':')) + ';' + h[m.end():]
old_js = read('u5_p.js').strip('\n')
js = (read('u5b_p.js').strip('\n').replace('/*OCEAVL*/[]', json.dumps(B.OCEAVL, ensure_ascii=False, separators=(',', ':')))
      .replace('/*CHECKS*/[]', json.dumps(B.CHECKS, ensure_ascii=False, separators=(',', ':'))).replace('/*KIT*/[]', json.dumps(B.KIT_JS, ensure_ascii=False, separators=(',', ':'))))
assert '/*' + 'OCEAVL' not in js and '</script' not in js
rep(old_js, js)

# ── 7. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<script') == h.count('</script>') == h0.count('<script')
body = lambda t: re.sub(r'<script.*?</script>', ' ', re.sub(r'<style.*?</style>', ' ', t, flags=re.S), flags=re.S)
b0, b1 = body(h0), body(h)
assert b1.count('<div') == b1.count('</div>'), 'div balance %d / %d' % (b1.count('<div'), b1.count('</div>'))
ids0 = set(re.findall(r'\bid="([^"]+)"', b0)); ids1 = set(re.findall(r'\bid="([^"]+)"', b1))
new_ids = {'ocGrid', 'ocProfile', 'ocConf', 'ref16', 'ref16-saved', 'kitMe', 'kitTeam', 'kitOutP'}
assert ids1 - ids0 == new_ids, ids1 - ids0
lost = ids0 - ids1
keep_lost = lambda x: (re.fullmatch(r'cm\d', x) or re.fullmatch(r'(ctm[12]_\w+|wp_\w+|exch_\w+|syn_(missing_compass|strong_compass|sequence)|ref7|ref14)(-saved)?', x) or x in ('synOutP', 'sp2'))
assert all(keep_lost(x) for x in lost), sorted(x for x in lost if not keep_lost(x))
assert len(ids1) == len(re.findall(r'\bid="([^"]+)"', b1)), 'an id is used twice'
for k in ('lens_id', 'href=', 'showMod('):
    assert h.count(k) == h0.count(k), (k, h0.count(k), h.count(k))
assert h.count('u3m1_lens4') == h0.count('u3m1_lens4')
vis = re.sub(r'<[^>]+>', ' ', b1)
for bad in (r'\blens(es)?\b', r'Save to Portfolio', r'pre-?work', r'automat', r'\b\d+\s*(–|-|&ndash;)?\s*\d*\s*minutes\b', r'facilitation question', r'\bAsk:', r'\bSay:',
            r'rather than', r'instead of', r'in place of', r'Burning Platform', r'High Flammable', r'(?<![\d.])1\.[4-7]\b', r'(?<![\d.])3\.3\b', r'Change Transition Map', r'Plenary Synthesis', r'COMPASS', r'leverage (zone|point)', r'Change Readiness', r'readiness scan', r'worked scan'):
    assert not re.search(bad, vis, re.I), 'found on the page: ' + bad
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('participant file written:', out, len(h))
