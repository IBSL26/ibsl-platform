# -*- coding: utf-8 -*-
"""Unit 5 amendments of 9 October 2026 — facilitator file, on Carol's word.
Usage: python3 amend2_f.py <facilitator file written by amend_f.py> <new file>
Run it from this folder: it reads u5c_content.py, u5b_content.py, u5_content.py and u5c.css.
Chain: file before the three-way match -> build_f.py -> amend_f.py -> amend2_f.py.
The page stays preparation-only: the build fails if a time, an entry box or a save button is left."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5b_content as B
import u5c_content as D
import u5_content as C
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
    global h
    assert h.count(start) == 1 and h.count(end) == 1, (h.count(start), h.count(end), start[:60])
    i, j = h.index(start), h.index(end)
    assert i < j
    h = h[:i] + new + h[j:]
def activity(lead, steps=None, close=''):
    return ('  <div class="fac-note-full u5-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n    <p>' + lead + '</p>\n' +
            ('    <ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>\n' if steps else '') +
            ('    <p>' + close + '</p>\n' if close else '') + '  </div>\n')
ol = lambda steps: '    <ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>\n'

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + read('u5c.css') + h[i:]

# ── 1. Facilitator Guide tab ───────────────────────────────────────────────────────────────────────
import u5d_content as E0
rep(D.GUIDE_TAB_OLD, E0.GUIDE_TAB_NEW)
rep(E0.GUIDE_TAB1_OLD, E0.GUIDE_TAB1_NEW)

# ── 2. Part 3.1: participants score first; one activity note carries how it is completed and read ──
rep('  <p><strong>On the order:</strong> Teach the seven dimensions and how a profile is read. Each participant completes the assessment alone after the teaching. '
    'The team&rsquo;s profile appears in the Capstone Blueprint once every member has submitted.</p>\n', D.OC_ORDER_F)
cut('  <h4>How the profile is read</h4>\n', '</div>\n</div>\n\n<div class="mod-nav">\n  <button class="btn prev" onclick="showMod(2)">',
    activity(D.OC_LEAD_F, D.OC_STEPS_F, D.OC_CLOSE_F) + '  <h4>' + D.OC_DIMS_H + '</h4>\n  <p>' + D.OC_DIMS_F + '</p>\n' + D.oceavl_dims())

# ── 3. Section 4: the old 4.3 becomes 4.1, with the old 4.1 as notes inside it; 4.2 follows ────────
HEAD = '<div class="acc%s">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">%s</span>'
s1 = HEAD % (' open', '4.1 &mdash; The Converging Zone: What Collective Intelligence Creates')
s2 = HEAD % (' open', '4.2 &mdash; Collective Intelligence Across the Leadership Team')
s3 = HEAD % ('', '4.3 &mdash; Leading Change with One Voice')
end = '<div class="mod-nav">\n  <button class="btn prev" onclick="showMod(3)">'
for s in (s1, s2, s3, end): assert h.count(s) == 1, s[-60:]
i1, i2, i3, ie = h.index(s1), h.index(s2), h.index(s3), h.index(end)
assert i1 < i2 < i3 < ie
a1, a2, a3 = h[i1:i2], h[i2:i3], h[i3:ie]
two = ('    <p><strong>Two states exercise:</strong> Ask leaders to identify which state their organisation is currently closer to. Then: <em>&ldquo;What is the single most important convergence '
       'you need to achieve before your next major strategy initiative?&rdquo;</em></p>\n')
assert a1.count(two) == 1
g0 = '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0;">'
g1 = '  <div class="fac-note-full u5-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n    <p>Participants write a reflection in their own file: which of the two states'
assert a1.count(g0) == 1 and a1.count(g1) == 1
grid = a1[a1.index(g0):a1.index(g1)]
assert grid.count('<div') == grid.count('</div>') and 'With Collective Intelligence' in grid and 'Without Collective Intelligence' in grid
lab3 = '  <div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; Section 4.3</div>\n'
p1 = ('  <p>The 4 Checks describe what one group of people needs from one leader. Most changes reach a group through several leaders at once. People hear from their own leader, watch the others, and compare. '
      'Where the leaders differ, the group takes the difference as the real message.</p>\n')
p2 = '  <p>In the Converging Zone, the leadership team makes four commitments that no single function can make alone. Each one protects a check. Expand each commitment.</p>\n'
assert a3.count(lab3) == 1 and a3.count(p1 + p2) == 1
n1 = (a3.replace(s3, HEAD % (' open', '4.1 &mdash; ' + D.T41))
        .replace(lab3, lab3.replace('Section 4.3', 'Section 4.1') + two)
        .replace(p1 + p2, p1 + '  <div class="chg-h">' + D.ONE_H + '</div>\n  <p>' + D.ONE_P + '</p>\n' + grid + '  <div class="chg-h">' + D.FOUR_H + '</div>\n' + p2))
assert '<span class="acc-meta">' + D.T41_META + '</span>' in n1
h = h[:i1] + n1 + a2 + h[ie:]

# ── 4. Part 4.2 in plain words ────────────────────────────────────────────────────────────────────
rep('&#9670; FACILITATOR GUIDANCE &mdash; Section 4.2</div>\n', '&#9670; FACILITATOR GUIDANCE &mdash; Section 4.2</div>\n    <p>' + D.GUIDE42_F + '</p>\n')
rep('  <p style="margin-bottom:14px;">Click a role to explore how each CXO function contributes to Collective Intelligence and the alignment check it is inclined to.</p>\n  <p>' + B.HOT_INTRO_F + '</p>\n',
    '  <p style="margin-bottom:14px;">Click a role to explore what each CXO function contributes to Collective Intelligence and where it is most likely to lose people.</p>\n' + D.teach42('f'))
for n in range(10):
    old = B.role_detail(n, 'f', C.role_detail(n, 'f')); rep(old, D.role_detail2(n, 'f', old))

# ── 5. Section 5: the group states its Shift, Stake and Step, then the ACE-IT behaviours it expects from the leadership team ──
#    (Carol, 9 October, fourth round). The cue-and-trigger toolkit, the personal watch list and the 30-Day Behavioural Commitment have left.
import u5d_content as E
G3, GA = E.guide_3s(h), E.guide_ace(h)        # the page's own lesson text from parts 1.3.1 and 1.3.4
def guidance(label, paras, ind='  '):
    return (ind + '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; ' + label + '</div>\n' +
            ''.join(ind + '  <p>' + p + '</p>\n' for p in paras) + ind + '</div>\n')
rep('  <h2>' + B.T5 + '</h2>\n  <p>' + B.HERO5_F + '</p>', '  <h2>' + E.T5 + '</h2>\n  <p>' + E.HERO_F + '</p>')
cut('  <p><strong>Order:</strong> Teach Step 1. Step 2 is individual.', '</div>\n\n<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div>',
    ''.join('  <p>' + x + '</p>\n' for x in E.SEC5_GUIDE_F))
rep('<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div><ul>' + ''.join('<li>' + x + '</li>' for x in B.SEC5_HOW_F) + '</ul></div>\n\n', E.how_box('f'))
s5 = ('<div class="step-tabs">\n'
      '  <div class="step-tab active" onclick="showSP(\'m\',this)"><div class="step-num">Step 1</div><div class="step-name">' + E.STEP_NAMES[0] + '</div></div>\n'
      '  <div class="step-tab" onclick="showSP(1,this)"><div class="step-num">Step 2</div><div class="step-name">' + E.STEP_NAMES[1] + '</div></div>\n'
      '</div>\n\n<div class="step-panel active" id="spm">\n' + guidance('Step 1', E.STEP1_GUIDE_F, '') +
      '<div class="chg-h">The guide beside each box &middot; from part 1.3.1</div>\n' + ''.join(E.card_3s(g, 'f') for g in G3) +
      activity('Participants work as a group, in Step 1 of their own file. This is Capstone work. ' + C.GROUP_RULE_F, E.STEP1_ACT_F) + '</div>\n\n'
      '<div class="step-panel" id="sp1">\n' + guidance('Step 2', E.STEP2_GUIDE_F, '') +
      '<div class="chg-h">The guide beside each box &middot; from part 1.3.4</div>\n' + ''.join(E.card_ace(g, 'f') for g in GA) +
      activity('Participants work as a group, in Step 2 of their own file. This is Capstone work. ' + C.GROUP_RULE_F, E.STEP2_ACT_F,
               'The confirmed record feeds the team&rsquo;s Capstone Blueprint: the Shift, Stake and Step, and the five expected leadership behaviours.'))
cut('<div class="step-tabs">', '<div class="hbox" style="margin-top:18px;"><p><strong>Unit Outcome:</strong>', s5)
rep(B.OUTCOME_TAIL_F, E.OUTCOME_TAIL_F)
rep('<li>' + E.SLO5_1_OLD + '</li>', '<li>' + E.SLO5_1_NEW + '</li>')

# ── 6. Unit Summary ───────────────────────────────────────────────────────────────────────────────
rep(D.SUMMARY_F4_OLD_HEAD, D.SUMMARY_F4_NEW_HEAD)
for n, r in enumerate(B.HOT):
    rep('    <li><strong>%s</strong> &mdash; %s</li>\n' % (r[0], B.hot_tag(n)), '    <li><strong>%s</strong> &mdash; %s</li>\n' % (r[0], D.hot_tag2(n)))
rep(D.SUMMARY_F4_OLD_TAIL, D.SUMMARY_F4_NEW_TAIL)
rep('  <p>' + B.SUMMARY_F5 + '</p>', '  <p>' + E.SUMMARY_F5 + '</p>')
rep('>' + B.SUMMARY_F5_H + '</div>', '>' + E.SUMMARY_F5_H + '</div>')
rep(E.CLOSE_Q_OLD, E.CLOSE_Q_NEW)

# ── 7. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<script') == h.count('</script>') == h0.count('<script')
body = re.sub(r'<script.*?</script>', ' ', re.sub(r'<style.*?</style>', ' ', h, flags=re.S), flags=re.S)
assert body.count('<div') == body.count('</div>'), 'div balance %d / %d' % (body.count('<div'), body.count('</div>'))
assert not re.search(r'<(textarea|input|select)\b', body), 'an entry box is left on the facilitator page'
assert 'onclick="saveTA(' not in body
ids = re.findall(r'\bid="([^"]+)"', body); assert len(ids) == len(set(ids)), 'an id is used twice'
for k in ('href=', 'showMod('):
    assert h.count(k) == h0.count(k), (k, h0.count(k), h.count(k))
titles = [t.replace('&mdash;', '—') for t in re.findall(r'<span class="acc-t">([^<]+)</span>', body)]
assert [t.split(' — ')[0] for t in titles if t[0].isdigit()] == ['1.1', '1.2', '1.3', '1.3.1', '1.3.2', '1.3.3', '1.3.4', '2.1', '2.2', '2.3', '3.1', '4.1', '4.2'], titles
assert body.count('<details class="u5-dim">') == 7 and body.count('How the profile is read') == 0 and body.count('<div class="u5-rt">') == 21
assert body.index(D.OC_LEAD_F) < body.index('<details class="u5-dim">')
vis = re.sub(r'<[^>]+>', ' ', body)
for bad in (r'\blens(es)?\b', r'pre-?work', r'automat', r'\b\d+\s*(–|-|&ndash;)?\s*\d*\s*minutes\b', r'Suggested (section )?time', r'rather than', r'instead of', r'in place of',
            r'Burning Platform', r'High Flammable', r'(?<![\d.])1\.[4-7]\b', r'(?<![\d.])3\.3\b', r'(?<![\d.])4\.3\b', r'Change Transition Map', r'Plenary Synthesis', r'COMPASS', r'leverage (zone|point)',
            r'Change Readiness', r'readiness scan', r'worked scan', r'inclined to set off', r'under each check', r'Alignment Toolkit in Section 5 gives', r'Heart · SCARF', r'Hands · STAT', r'four tools', r'watch list', r'Step 3', r'30.Day Behavioural Commitment', r'Closing commitment', r'The (Mind|Heart|Hands|Habit) check fails', r'likely trigger', r'two cues', r'Team Alignment Plan', r'surface for our strategy', r'Alignment Toolkit'):
    assert not re.search(bad, vis, re.I), 'found on the page: ' + bad
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('facilitator file written:', out, len(h))
