# -*- coding: utf-8 -*-
"""Unit 5 amendments of 8 October 2026 (evening) — facilitator file, on Carol's word.
Usage: python3 amend_f.py <facilitator file built by build_f.py> <new file>
Run it from this folder: it reads u5b_content.py, u5_content.py, oceavl.json and u5b.css.
Chain: file before the three-way match -> build_f.py -> amend_f.py.
The page stays preparation-only: the build fails if a time, an entry box or a save button is left."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5b_content as B
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
def guidance(label, paras, ind='  '):
    return (ind + '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; ' + label + '</div>\n' +
            ''.join(ind + '  <p>' + p + '</p>\n' for p in paras) + ind + '</div>\n')
def activity(lead, steps=None, close=''):
    return ('  <div class="fac-note-full u5-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n    <p>' + lead + '</p>\n' +
            ('    <ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>\n' if steps else '') +
            ('    <p>' + close + '</p>\n' if close else '') + '  </div>\n')
ACC = '<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">'
ARR = '<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div>\n</div>\n<div class="acc-b cb">\n'
def acc_head(title, meta, cls='acc'):
    return ('<div class="' + cls + '">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">' + title + '</span>\n'
            '  <div style="display:flex;align-items:center;gap:10px;"><span class="acc-meta">' + meta + '</span>' + ARR)

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + read('u5b.css') + h[i:]

# ── 1. Facilitator Guide tab ───────────────────────────────────────────────────────────────────────
rep('<p>SCARF explains resistance, ACE-IT sets the behaviour standard and COMPASS locates the hot zones. The Section 5 exercise, in which leaders map how their roles connect, is the centrepiece.</p>',
    '<p>SCARF explains resistance, ACE-IT sets the behaviour standard and the OCEAVL Assessment shows the behavioural profile the leadership team brings to the strategy. The Section 5 exercise, the Alignment Toolkit, is the centrepiece.</p>')
rep('STAT tests Hands and ACE-IT holds Habit. The Section 5 exercise opens with the Change Transition Map.</p>',
    'STAT tests Hands and ACE-IT holds Habit. The Alignment Toolkit in Section 5 gives two cues and a likely trigger for each element of the four tools.</p>')
rep('<li><em>&ldquo;Which COMPASS zone would flare first in your organisation under pressure? What is the early warning?&rdquo;</em></li>',
    '<li><em>&ldquo;On which OCEAVL dimension does your team&rsquo;s level carry the highest risk for this strategy? Where has that risk already shown up?&rdquo;</em></li>')

# ── 2. Part 1.2 · Principle 1: Carol's text of 8 October ───────────────────────────────────────────
cut('        <p>Cognitive alignment focuses on', '        <div class="p-insight">&#10148; Facilitation insight: Ask leaders to name the dominant emotion', B.principle1_chain())

rep('Learning Orientation. Available on demand &mdash; Excel or HTML format with facilitated report generation.</p>', 'Learning Orientation. Each participant completes it in part 3.1.</p>')

# ── 3. Section 1: the four tools are parts of change management (1.3.1 to 1.3.4) ───────────────────
for old, new, name in (('1.4', '1.3.1', 'The 3S Check: Shift, Stake, Step'), ('1.5', '1.3.2', 'The SCARF Model: Five Triggers of Human Resistance'),
                       ('1.6', '1.3.3', 'The STAT Check: Skill, Time, Authority, Tools'), ('1.7', '1.3.4', 'ACE-IT: The Observable Behaviour Standard')):
    rep(ACC + old + ' &mdash; ' + name + '</span>', ACC.replace('class="acc"', 'class="acc u5-sub"') + new + ' &mdash; ' + name + '</span>')
    rep('FACILITATOR GUIDANCE &mdash; Section ' + old + '</div>', 'FACILITATOR GUIDANCE &mdash; Section ' + new + '</div>')
rep('explored in detail in section 1.5. The SCARF Tool', 'explored in detail in part 1.3.2. The SCARF Tool')
rep('Explored in detail in section 1.7.</p>', 'Explored in detail in part 1.3.4.</p>')
rep('the 3S Check (1.4).', 'the 3S Check (1.3.1).')
rep('the SCARF Model (1.5).', 'the SCARF Model (1.3.2).')
rep('the STAT Check (1.6).', 'the STAT Check (1.3.3).')
rep('ACE-IT (1.7).', 'ACE-IT (1.3.4).')
rep('and return to the list in 1.6.</p>', 'and return to the list in 1.3.3.</p>')
rep('Repeat the 3S test from 1.4 with the whole team', 'Repeat the 3S test from 1.3.1 with the whole team')

# ── 4. Section 3 ──────────────────────────────────────────────────────────────────────────────────
rep('  <h2>Where Are the Alignment Hot Zones Across the Organisation?</h2>\n  <p>The Alignment Brigade &middot; The COMPASS framework identifies seven High Flammable Zones where human interpretation, emotional climate, and behaviour directly influence strategic outcomes. These are the leverage points &mdash; and the danger zones.</p>',
    '  <h2>' + B.HERO3_H + '</h2>\n  <p>The Alignment Brigade &middot; ' + B.HERO3_F + '</p>')
cut('  <p><strong>Section intent:</strong> Make the alignment concept specific and organisationally urgent.',
    '</div>\n\n<div class="acc open">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">3.1 &mdash; The COMPASS Framework',
    '  <p><strong>Section intent:</strong> Make the alignment concept specific to this team and this organisation. Leaders finish this section knowing the behavioural profile their own team brings to the strategy.</p>\n'
    '  <p><strong>On the order:</strong> Teach the seven dimensions and how a profile is read. Each participant completes the assessment alone after the teaching. The team&rsquo;s profile appears in the Capstone Blueprint once every member has submitted.</p>\n')
s31 = (acc_head('3.1 &mdash; ' + B.T31, B.T31_META, 'acc open') +
       guidance('Section 3.1', [
           '<strong>Framing:</strong> Present OCEAVL as a mirror. Its power lies in the conversation it generates. Every level carries a risk, High included.',
           '<strong>On scoring:</strong> OCEAVL is a personal assessment. Each participant scores themselves alone, on their own page. No one states a score to the group, and no one records a score for another member.',
           '<strong>On the team profile:</strong> The portal shows the team&rsquo;s level on each dimension in the Capstone Blueprint once every member of the team has submitted. The team sees levels and counts, with no names.',
           '<strong>Watch for:</strong> a High level read as a strength with no risk. Ask participants to read the risk for their High levels first.']) +
       B.oceavl_teach('f') +
       activity('After the lesson, each participant completes the OCEAVL Assessment alone in part 3.1 of their own file, as portfolio work:',
                ['They score themselves from 1 to 5 on each of the seven dimensions.',
                 'They read their own profile: their level on each dimension, with its risk, its response and its routines.',
                 'They select Submit to My Team&rsquo;s Capstone. Print gives a copy of their own profile.'],
                'The team&rsquo;s profile appears in the team&rsquo;s Capstone Blueprint once every member has submitted. The team then agrees, in the Capstone, the two dimensions that carry the highest risk for the strategy. Each participant also writes a reflection in their own file: the level of their own that carries the highest risk for how they read and lead the strategy.') +
       '</div>\n</div>\n\n')
cut('<div class="acc open">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">3.1 &mdash; The COMPASS Framework',
    '<div class="mod-nav">\n  <button class="btn prev" onclick="showMod(2)">', s31)   # 3.2 (Burning Platforms) and 3.3 (Change Readiness) leave with it

# ── 5a. Section 4: COMPASS leaves; each role card names its alignment hot zone ───────────────────────
for a, b in B.SEC4: rep(a, b)
rep('causing instability across all seven COMPASS domains.</p>', 'causing instability across the organisation.</p>')
rep('Click a role to explore how each CXO function contributes to Collective Intelligence and which COMPASS domains it most directly activates.</p>',
    'Click a role to explore how each CXO function contributes to Collective Intelligence and the alignment check it is inclined to.</p>\n  <p>' + B.HOT_INTRO_F + '</p>')
for n in range(10):
    old = C.role_detail(n, 'f'); rep(old, B.role_detail(n, 'f', old))

# ── 5. Section 5: the Alignment Toolkit ────────────────────────────────────────────────────────────
m = re.search(r'  <h2>Building Collective Intelligence Through Shared Interpretation</h2>\n  <p>Application &middot; This exercise highlights how Collective Intelligence emerges when leaders.*?</p>', h)
assert m and h.count(m.group(0)) == 1
h = h[:m.start()] + '  <h2>' + B.T5 + '</h2>\n  <p>' + B.HERO5_F + '</p>' + h[m.end():]
cut('  <p><strong>Order:</strong> Steps 1 and 2 are individual.', '</div>\n\n<div class="step-tabs">',
    '  <p><strong>Order:</strong> Teach Step 1. Step 2 is individual. Step 3 is group work. Give Step 2 its full depth: the quality of the team plan depends on the watch list each member brings.</p>\n'
    '  <p><strong>Facilitation principle:</strong> Your role in Step 3 is to name patterns. When members select different triggers for the same change, name it: <em>&ldquo;Each of you is reading this change from a different seat. The plan has to cover all of them.&rdquo;</em></p>\n')
SEC5HOW = '<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div><ul>' + ''.join('<li>' + x + '</li>' for x in B.SEC5_HOW_F) + '</ul></div>\n\n'
s5 = (SEC5HOW + '<div class="step-tabs">\n'
      '  <div class="step-tab active" onclick="showSP(\'m\',this)"><div class="step-num">Step 1</div><div class="step-name">' + B.STEP_NAMES[0] + '</div></div>\n'
      '  <div class="step-tab" onclick="showSP(0,this)"><div class="step-num">Step 2</div><div class="step-name">' + B.STEP_NAMES[1] + '</div></div>\n'
      '  <div class="step-tab" onclick="showSP(1,this)"><div class="step-num">Step 3</div><div class="step-name">' + B.STEP_NAMES[2] + '</div></div>\n'
      '</div>\n\n<div class="step-panel active" id="spm">\n' +
      guidance('Step 1', [
          '<strong>Teaching:</strong> Take one check at a time. For each element, read the two cues and ask the group to name the trigger before you show it.',
          '<strong>Key distinction:</strong> A cue is what is seen or heard. A trigger is the condition behind it. A leader who answers the cue leaves the trigger in place.',
          '<strong>On the worked example:</strong> It follows the change carried through the unit. Point out that each row names one group and one owner.'], '') +
      B.toolkit_step1() +
      activity('Participants read the toolkit in Step 1 of their own file. They enter nothing in this step.') + '</div>\n\n'
      '<div class="step-panel" id="sp0">\n' +
      guidance('Step 2', [
          '<strong>Briefing:</strong> Each participant works alone, with the Start and Stop lists the group confirmed in Unit 3 in view.',
          '<strong>Watch for:</strong> every trigger selected. Ask which ones will surface first, and in whose area.',
          '<strong>Watch for:</strong> &ldquo;communicate more&rdquo; as the answer to every trigger. Ask which trigger the communication removes.'], '') +
      activity('After the lesson, each participant completes Your Watch List alone in Step 2 of their own file, as portfolio work:',
               ['They read the practices the strategy starts and stops. Their page shows the Start and Stop lists the group confirmed in Unit 3.',
                'They read the cards under each check. Each card is one trigger, with the two cues that show it.',
                'They select &ldquo;Likely to surface in my area&rdquo; on the triggers they expect, starting with the alignment hot zone of their own role in 4.2, and at least one under each check.',
                'In the box that opens, they write what they will do.'],
               'The watch list saves as the participant works and becomes part of the participant&rsquo;s Learning Portfolio. It reaches you when the participant selects Submit to Facilitator at the end of the unit. Check that each action answers its trigger and names something the participant will do.') +
      '</div>\n\n<div class="step-panel" id="sp1">\n' +
      guidance('Step 3', [
          '<strong>Synthesis question:</strong> <em>&ldquo;Across your watch lists, which trigger did most of you select? Which did only one of you select, and what does that member see from their seat?&rdquo;</em>',
          '<strong>Watch for:</strong> a committee or a function named as owner. Hold out for one person.',
          '<strong>Closing commitment:</strong> Each leader names one specific behavioural change in the next 30 days. Ask each leader to tie the commitment to one trigger in the team plan: the behaviour they will show first. Make these visible: each participant posts the commitment in the chat. Follow up at the next leadership forum.'], '') +
      activity('Participants work as a group, in Step 3 of their own file. This is Capstone work. ' + C.GROUP_RULE_F,
               ['The group compares the watch lists of its members.',
                'The group selects &ldquo;Likely to surface for our strategy&rdquo; on the triggers it agrees on, for the strategy in its Capstone Blueprint, and at least one under each check.',
                'In the boxes that open, the group writes where the trigger will surface, what the team will do and the leader who owns it.',
                'Each participant reads the record and selects Confirm. Print gives a copy of the record.'],
               'The confirmed plan feeds the team&rsquo;s Capstone Blueprint. Each participant then writes one 30-day behavioural commitment in their own file, as portfolio work. Close by asking each participant to post that commitment in the chat.'))
cut('<div class="step-tabs">', '<div class="hbox" style="margin-top:18px;"><p><strong>Unit Outcome:</strong>', s5)
rep(B.OUTCOME_TAIL_OLD_F, B.OUTCOME_TAIL_F)

# ── 6. Unit Summary ───────────────────────────────────────────────────────────────────────────────
rep('<em>&ldquo;Which COMPASS domain is this team most likely rating too generously &mdash; and which executive role has quietly stopped carrying its alignment responsibility there?&rdquo;</em>',
    '<em>&ldquo;Which trigger in your team plan is this team most likely to leave to someone else, and which leader has agreed to own it?&rdquo;</em>')
cut('  <div style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#5ecba1;margin-bottom:8px;">3 &mdash; Extrapolating: Where Misalignment Concentrates</div>',
    '</div>\n\n<!-- Stage 4 -->', B.SUMMARY_F3)
cut('Each CXO role carries a distinct alignment responsibility, mapped to two primary COMPASS activations:</p>', '<strong>Collective Intelligence is the combined signal.</strong>', B.SUMMARY_F4)
rep('>5 &mdash; Application: Mapping the Transition</div>', '>' + B.SUMMARY_F5_H + '</div>')
rep('  <p>Each participant mapped the transition for two changes the strategy requires, set out how their role connects to the two roles they depend on most, and tested both with a colleague. The group then agreed the COMPASS domain most often underactivated, where alignment is already strong, and the sequence for the changes landing on the same group. The confirmed work feeds each team&rsquo;s Capstone Blueprint.</p>',
    '  <p>' + B.SUMMARY_F5 + '</p>')

# ── 7. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<script') == h.count('</script>') == h0.count('<script')
body = re.sub(r'<script.*?</script>', ' ', re.sub(r'<style.*?</style>', ' ', h, flags=re.S), flags=re.S)
assert body.count('<div') == body.count('</div>'), 'div balance %d / %d' % (body.count('<div'), body.count('</div>'))
assert not re.search(r'<(textarea|input|select)\b', body), 'an entry box is left on the facilitator page'
assert 'onclick="saveTA(' not in body
ids = re.findall(r'\bid="([^"]+)"', body); assert len(ids) == len(set(ids)), 'an id is used twice'
for k in ('href=', 'showMod('):
    assert h.count(k) == h0.count(k), (k, h0.count(k), h.count(k))
vis = re.sub(r'<[^>]+>', ' ', body)
for bad in (r'\blens(es)?\b', r'pre-?work', r'automat', r'\b\d+\s*(–|-|&ndash;)?\s*\d*\s*minutes\b', r'Suggested (section )?time', r'rather than', r'instead of', r'in place of',
            r'Burning Platform', r'High Flammable', r'(?<![\d.])1\.[4-7]\b', r'(?<![\d.])3\.3\b', r'Change Transition Map', r'Plenary Synthesis', r'COMPASS', r'leverage (zone|point)', r'Change Readiness', r'readiness scan', r'worked scan'):
    assert not re.search(bad, vis, re.I), 'found on the page: ' + bad
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('facilitator file written:', out, len(h))
