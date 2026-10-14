# -*- coding: utf-8 -*-
"""Unit 7 deck · the two performance views (14 October 2026). Works on top of Carol's current deck (24 slides).
Usage: python3 deck_u07pv.py <her deck> <out.pptx>
Surgical: slide text changed only where the pages changed (outcomes, 1.2 cards, 1.3 Crossline, 4.1 renumbering, 5.1 lines);
notes keep her wording and gain the two-view content of the pages. Slide 19 (the old 4.1 four-step slide) leaves."""
import sys, re, copy
from pptx import Presentation
import u7pv_content as C

src, out = sys.argv[1:3]
prs = Presentation(src)
S = list(prs.slides)
assert len(S) == 24


def shape(s, name):
    m = [sh for sh in s.shapes if sh.name == name]; assert len(m) == 1, name; return m[0]


def set_text(s, name, old_start, new):
    sh = shape(s, name); para = sh.text_frame.paragraphs[0]
    assert para.text.startswith(old_start), (name, para.text)
    runs = para.runs; runs[0].text = new
    for r in runs[1:]: r._r.getparent().remove(r._r)


def set_two_run(s, name, old_head, new_tail):
    """Lines like '3 · Identify the Expectations Chain  Upline, Downline and External': keep run 1, change run 2."""
    sh = shape(s, name); para = sh.text_frame.paragraphs[0]
    assert para.text.startswith(old_head), para.text
    para.runs[1].text = new_tail


def notes(s):
    return s.notes_slide.notes_text_frame


def put_notes(s, text):
    tf = notes(s); tf.text = text


def nrep(s, a, b):
    t = notes(s).text
    assert t.count(a) == 1, (a[:80], t.count(a))
    put_notes(s, t.replace(a, b))


# ── Slide 1 · subtitle and intent ──
set_text(S[0], 'Text 2', 'Turning delivery goals', 'Turning delivery goals into genuine ownership across the Human and Organisational Operating Systems')
nrep(S[0], 'genuine human commitment to deliver it.', 'genuine human commitment to deliver it.\n' + C.DESC['f'] + '\n' + C.INTENT_ADD)

# ── Slide 2 · Key learning outcomes ──
OLD_KLO = ['Articulate performance expectations', 'Evaluate the readiness', 'Recognise the contribution relationships', 'Demonstrate shared ownership']
for k, nm in enumerate(['Text 2', 'Text 4', 'Text 6', 'Text 8']):
    set_text(S[1], nm, OLD_KLO[k], C.KLO[k])
t = notes(S[1]).text
for k in range(4):
    t = re.sub(r'(?m)^%d\. .*$' % (k + 1), '%d. %s' % (k + 1, C.KLO[k]), t, count=1)
put_notes(S[1], t)

# ── Section slides · outcomes ──
for sec, idx in enumerate([3, 10, 14, 17, 21]):
    s = S[idx]
    olds = [shape(s, 'Text 6').text_frame.text, shape(s, 'Text 8').text_frame.text]
    set_text(s, 'Text 6', olds[0][:20], C.SLO[sec][0]); set_text(s, 'Text 8', olds[1][:20], C.SLO[sec][1])
    t = notes(s).text
    for k in range(2):
        o = olds[k].rstrip('.')
        m = re.search(r'(?m)^%d\. %s\.?$' % (k + 1, re.escape(o)), t)
        assert m, (sec, k, o)
        t = t[:m.start()] + '%d. %s' % (k + 1, C.SLO[sec][k]) + t[m.end():]
    put_notes(s, t)
nrep(S[17], 'Designing a shared method for establishing expectations consistently across the organisation — connecting every expectation to the future, clarifying the chain, and securing ownership through the Alignment Dialogue.',
     C.S4_HERO['f'].replace('&mdash;', '—'))

# ── Slide 5 · 1.1 ──
V11 = ('Both performance views:\n' + C.V11['f'] + '\n'
       'Human expectations describe the result, contribution, standard, timing and behaviours for which people will take responsibility. '
       'Organisational expectations specify the Environment, Systems, Resources and Governance that the organisation will provide or resolve. Both must be explicitly agreed.\n'
       'Enabling conditions: when expectations are set, they are assumed to be in place; when expectations are established, they are agreed with the owners of the Environment, Systems, Resources and Governance.\n\n')
nrep(S[4], 'Setting expectations in practice: ', V11 + 'Setting expectations in practice: ')

# ── Slide 6 · 1.2 ──
set_text(S[5], 'Text 4', 'The individual understands', 'Everyone understands what is expected and why it matters.')
set_text(S[5], 'Text 8', 'The system can', 'The people and the organisation can realistically deliver.')
set_text(S[5], 'Text 12', 'The person consciously', 'Those responsible consciously accept delivering and enabling.')
intro, systems, lead, conds, principle = C.P12('f')
def plain(h):
    h = re.sub(r'<li>', '- ', h); h = re.sub(r'</li>|</p>|</tr>|<div class="hbox">|</div>', '\n', h); h = re.sub(r'</td><td>', ': ', h)
    h = re.sub(r'<[^>]+>', '', h).replace('&ldquo;', '“').replace('&rdquo;', '”').replace('&ndash;', '–')
    return re.sub(r'\n{2,}', '\n', h).strip()
INS = {0: 'Many operational failures happen because people in authority believe execution needs their presence when it needs their clarity. Authority travels with a clear instruction.',
       1: 'Strategy is weakened when leaders become so committed to movement that they ignore capability gaps. A disciplined readiness pause can prevent an expensive failure later.',
       2: 'Commitments lose strategic meaning when they are honoured only when convenient. Good intent has limited value if people cannot understand what is required of them.'}
old6 = notes(S[5]).text
g = old6[:old6.index('Content:')]
tail = old6[old6.index('When the three conditions are met:'):]
body = 'Content:\n' + '\n'.join(re.sub(r'<[^>]+>', '', x) for x in intro) + '\n' + '\n'.join('- %s: %s' % (a, b) for a, b in systems) + '\n' + lead + '\n\n'
for k, (nm, q, html) in enumerate(conds):
    txt = plain(html).replace('Test: Ask someone', 'Facilitation test: “Ask someone').replace('clarity has not yet been established.', 'clarity has not yet been established.”')
    body += 'Condition %d\n%s — %s\n%s\n%s\n\n' % (k + 1, nm, q, txt, INS[k])
body += re.sub(r'<[^>]+>', '', principle) + '\n\n'
put_notes(S[5], g + body + tail)

# ── Slide 7 · 1.3 ──
set_text(S[6], 'Text 11', 'External', 'Crossline')
set_text(S[6], 'Text 12', 'Which external actors', 'Whose contributions must connect with this one?')
old7 = notes(S[6]).text
head7 = old7[:old7.index('There are three flows')]
ins7 = 'Outcomes depend on a web of contributors beyond the visible leaders. Map and value the wider contribution system.'
assert ins7 in old7
t7 = (head7 + 'Central question: With whom must performance expectations be established for each contribution to succeed?\n' + C.USES_13['f'] + '\n\n' +
      '\n\n'.join('%d. %s\nWho\n%s\nWhat must be established\n%s\nExamples\n%s\nKey question\n%s' % (k + 1, nm, who, est, ex, q) for k, (a, nm, who, est, ex, q) in enumerate(C.CHAINS)) + '\n\n' +
      'Its output: A clear understanding of the accountability relationships in which performance expectations must be established.\n\n'
      'The Critical Distinction\n' + '\n'.join('%s: %s %s' % (n_, re.sub(r'<[^>]+>', '', e_), t_) for n_, e_, t_ in C.DIST_13) + '\n\n' + ins7 + '\n\n'
      'FACILITATOR GUIDANCE\nAsk participants to pick one current Key Result and post in the chat one contributor from each direction: Upline, Downline and Crossline. '
      'Then ask: “Have you had an alignment dialogue with everyone in that chain? Or only with the person holding the KPI?” Most will realise they have had the conversation with one person and assumed the rest of the chain would follow. '
      'That assumption is where most execution gaps begin.')
put_notes(S[6], t7)

# ── Slide 8 · 1.4 ──
nrep(S[7], 'designed to test whether the expectation has moved from instruction to commitment.\n',
     'designed to test whether the expectation has moved from instruction to commitment.\n\n' + '\n'.join(re.sub(r'<[^>]+>', '', x) for x in C.V14['f']) + '\n')
# ── Slide 10 · GROW: the role play moved to part 4.1 ──
t = notes(S[9]).text
if 'part 4.2' in t: put_notes(S[9], t.replace('part 4.2', 'part 4.1'))

# ── Slide 12 · 2.1 · Slide 14 · 2.3 · Slide 16 · 3.1 ──
nrep(S[11], 'execution becomes fragile regardless of how well the system has been designed.\n', 'execution becomes fragile regardless of how well the system has been designed.\n' + C.V21 + '\n')
nrep(S[13], 'two organisational conditions degrade in a predictable sequence.\n', 'two organisational conditions degrade in a predictable sequence.\n' + C.V23['f'] + '\n')
put_notes(S[15], 'FACILITATOR GUIDANCE\n' + C.V31['f'] + '\n' + re.sub(r'<[^>]+>', '', C.Q31_F) +
          '\nEach role card gives the Upline, Downline and Crossline of the role’s likely Expectations Chain.\n\n' + notes(S[15]).text)

# ── Slide 20 · now 4.1 ──
set_text(S[19], 'Text 0', '4.2 · Practising', '4.1 · Practising the Alignment Dialogue')
t = notes(S[19]).text
for a, b in [('4.2 — PRACTISING THE ALIGNMENT DIALOGUE', '4.1 — PRACTISING THE ALIGNMENT DIALOGUE'),
             ('Use the example of part 4.1, “Reduce complaint resolution time from 48 hours to 12 hours”,', 'Use the example “Reduce complaint resolution time from 48 hours to 12 hours”,'),
             ('Two briefs for the part 4.1 example are below.', 'Two briefs for this example are below.'),
             ('in part 4.2, you prepare', 'in part 4.1, you prepare')]:
    assert t.count(a) == 1, a; t = t.replace(a, b)
put_notes(S[19], t)

# ── Slide 21 · Section 4 Portfolio work ──
s = S[20]
set_text(s, 'Text 0', 'Section 4 Reflections', 'Section 4 · Portfolio work')
lab41 = shape(s, 'Part 4.1').left
for nm in ('Reflection 4.1', 'Part 4.1'):
    sh = shape(s, nm); sh._element.getparent().remove(sh._element)
pic = shape(s, 'Reflection 4.2'); lab = shape(s, 'Part 4.2')
off = pic.left - lab.left
lab.left = lab41; pic.left = lab41 + off
set_text(s, 'Part 4.2', '4.2', '4.1')
put_notes(s, '''SECTION 4 · PORTFOLIO WORK

HOW TO USE THIS SLIDE:

1. Explain the Portfolio work of part 4.1.
Say: "In part 4.1 you prepare an Alignment Dialogue with your board chair, using the GROW model.
You choose the Key Result for which you may need that dialogue.
The scenario is on your page: your board chair has disagreed with the current metric and timeframe of that Key Result and gives a 5.
You write your side of the dialogue under Goal, Reality, Options and Will, to move your chair to a 10."

2. Say what the Portfolio work is for.
The Portfolio work builds the learning portfolio participants receive at the end of the programme.
Say: "You complete the Portfolio work on the portal after the teaching, with as much depth as you can."

3. Set the standard.
Say: "Write the questions you would ask in your own words. A question you would never say aloud does not belong in your dialogue."
Watch for: answers that argue the case for the metric. Ask which GROW question comes first.

4. Bridge to Section 5.
Say: "You have practised the dialogue. In Section 5 your group establishes delivery expectations for two contributions from its Contribution Map, for the people and for the organisation."

ON THE PORTAL, AFTER THE TEACHING:
Each participant completes part 4.1 of their own file alone, as Portfolio work:
1. They choose from a drop-down list the Key Result for which they may need an alignment dialogue with their board chair. The list holds the Key Results their group confirmed in Unit 3.
2. They read the scenario: the board chair has disagreed with the current metric and timeframe of that Key Result and gives a 5.
3. They write their side of the dialogue under each GROW stage (Goal, Reality, Options, Will), with the questions they ask in their own words.
4. Under Will they state what they and the chair agree to do and how they confirm that the chair has reached a 10.
The work becomes part of the participant’s Learning Portfolio. It reaches you when the participant selects Submit to Facilitator at the end of the unit.''')

# ── Slide 22 · Section 5 opener ──
t = notes(S[21]).text
for a, b in [('5.1 · Building the Expectation Architecture. Each group takes two Objectives, with one Key Result each, through the four steps.', re.sub(r'<[^>]+>', '', C.HOW_S5_STEP1['f'])),
             ('In 5.1 your group builds the Expectation Architecture for two of its Objectives.', 'In 5.1 your group builds the Expectation Architecture for two contributions from its Contribution Map, for the people and for the organisation.')]:
    assert t.count(a) == 1, a; t = t.replace(a, b)
m = re.search(r'The drop-down lists hold the group’s Enterprise OKRs[^\n]*', t); assert m
t = t[:m.start()] + re.sub(r'<[^>]+>', '', C.GUIDE_BEFORE) + '\n' + re.sub(r'<[^>]+>', '', C.GUIDE_DONE) + t[m.end():]
put_notes(S[21], t)

# ── Slide 23 · 5.1 ──
set_two_run(S[22], 'Text 4', '2 · Clarify the Delivery Expectation', '  for the people and for the organisation')
set_two_run(S[22], 'Text 6', '3 · Identify the Expectations Chain', '  Upline, Downline and Crossline')
H = C.HOW_STEP_P
def lessonn(k): return 'The lesson participants see: ' + ' '.join('%s · %s' % (a, re.sub(r'<[^>]+>', '', b)) for a, b in C.LESSON[k])
def say(lines): return 'Say: "' + '\n'.join(re.sub(r'<[^>]+>', '', l) for l in lines) + '"'
put_notes(S[22], '''5.1 — BUILDING THE EXPECTATION ARCHITECTURE (CAPSTONE WORK)

HOW TO TEACH IT:

1. Say what the group does.
Say: "Each group selects two contributions from the Contribution Map it built in Unit 6 and takes each through the four steps. For each one you establish a human performance expectation and the supporting ESRG expectations."

2. Step 1 · Start With the Future.
''' + lessonn(0) + '\n' + say(H[0][:4] + ['Write the leader framing: the sentence that you, as the leader, say to the owner to connect the contribution to that Future.']) + '''
The first list holds the functions of the group's Unit 6 Contribution Map, with the enterprise Key Result they serve. The second holds the Success in Practice statements the group confirmed in Unit 2.

3. Step 2 · Clarify the Delivery Expectation.
''' + lessonn(1) + '\n' + say(H[1]) + '''
This is part 1.2 at work: Clarity in the Human Operating System and Clarity in the Organisational Operating System (ESRG).

4. Step 3 · Identify the Expectations Chain.
''' + lessonn(2) + '\n' + say(H[2]) + '''

5. Step 4 · Confirm Ownership.
''' + lessonn(3) + '\n' + say(H[3]) + '''

ON THE PORTAL, AFTER THE TEACHING:
Participants work as a group in part 5.1 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.
''' + '\n'.join('Step %d: %s' % (k + 1, ' '.join(re.sub(r'<[^>]+>', '', x) for x in C.COMPLETES_F[k])) for k in range(4)) + '\n' + re.sub(r'<[^>]+>', '', C.GUIDE_DONE))

# ── Slide 19 leaves (the old 4.1) ──
assert shape(S[18], 'Text 0').text_frame.text.startswith('4.1 · The four-step')
sld = prs.slides._sldIdLst; ids = list(sld)
rid = ids[18].get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
prs.part.drop_rel(rid); sld.remove(ids[18])
prs.save(out)
print('saved', out, len(prs.slides), 'slides')
