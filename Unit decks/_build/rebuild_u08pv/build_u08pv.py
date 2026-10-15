# -*- coding: utf-8 -*-
"""Unit 8 · the two performance views (15 October 2026).
python3 build_u08pv.py <live p> <live f> <out p> <out f>
Surgical edits on the live pages: every replacement is found the stated number of times or the build stops.
Encoding and CRLF line endings are kept as found."""
import re, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from u8pv_content import *

def load(p):
    b = open(p, 'rb').read()
    t = b.decode('utf-8')
    crlf = t.count('\r\n') == t.count('\n')
    return t.replace('\r\n', '\n'), crlf

def save(p, t, crlf):
    if crlf:
        t = t.replace('\n', '\r\n')
    open(p, 'wb').write(t.encode('utf-8'))

class Doc:
    def __init__(s, t, name):
        s.t = t; s.name = name; s.n = 0
    def rep(s, old, new, count=1):
        c = s.t.count(old)
        if c != count:
            raise SystemExit('%s: expected %d of %r, found %d' % (s.name, count, old[:90], c))
        s.t = s.t.replace(old, new); s.n += 1
    def after(s, anchor, add, count=1):
        s.rep(anchor, anchor + add, count)
    def before(s, anchor, add, count=1):
        s.rep(anchor, add + anchor, count)
    def sub(s, pattern, repl, count=1):
        m = re.findall(pattern, s.t, flags=re.S)
        if len(m) != count:
            raise SystemExit('%s: pattern %r matched %d' % (s.name, pattern[:80], len(m)))
        s.t = re.sub(pattern, lambda _m: repl, s.t, flags=re.S); s.n += 1
    def cut(s, start, end, new):
        a = s.t.find(start); b = s.t.find(end, a)
        if a < 0 or b < 0 or s.t.count(start) != 1:
            raise SystemExit('%s: cut markers not found once: %r' % (s.name, start[:80]))
        s.t = s.t[:a] + new + s.t[b:]; s.n += 1

def fg(d, label, body):
    d.sub(r'(?<=<div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — ' + label + r'</div>\n).*?(?=</div>)', body)

def common(d, voice):
    # CSS
    d.after('@media(max-width:430px){.u8-grow4{grid-template-columns:1fr;}}\n', CSS.lstrip('\n'))
    # Header
    d.rep('Review&ndash;Realign&ndash;Restore cycle.</p>', 'Review&ndash;Realign&ndash;Restore cycle.' + HEAD_ADD + '</p>')
    # Section 1
    d.after('progress visibility</strong>.</p>', '\n' + S1_VIS)
    d.after('execution intelligence system</strong>.</p>', '\n' + S1_ACT)
    anchors = (['<div class="p-reflect">Ask yourself: Where in your organisation is execution',
                '<div class="p-reflect">Ask yourself: If your key performance indicators',
                '<div class="p-reflect">Ask yourself: What did your organisation actually learn',
                '<div class="p-reflect">Ask yourself: What is the average gap'] if voice == 'p' else
               ['<div class="p-insight">Facilitator prompt: &ldquo;Where in your organisation',
                '<div class="p-insight">Facilitator prompt: &ldquo;If your KPIs disappeared',
                '<div class="p-insight">Facilitator prompt: &ldquo;What did your organisation actually learn',
                '<div class="p-insight">Facilitator prompt: &ldquo;What is the average gap'])
    for a, pr in zip(anchors, S1_PUR):
        d.before(a, pr)
    d.after('and progress is restored.</p>', '\n' + S1_R3_INTRO)
    d.before('<div class="sig-action"><strong>Outcome:</strong> A shared, evidence-based', S1_REVIEW + '\n')
    d.before('<div class="sig-action"><strong>Outcome:</strong> A clear understanding of the underlying', S1_REALIGN + '\n')
    d.before('<div class="sig-action"><strong>Outcome:</strong> A clear recovery pathway', S1_RESTORE + '\n')
    d.after('returns to the required trajectory.</p>', '\n' + S1_CONT)
    # Section 2
    anchors = (['<div class="p-reflect">Ask yourself: In your experience',
                '<div class="p-reflect">Ask yourself: Which KPIs in your current scorecard',
                '<div class="p-reflect">Ask yourself: What does your organisation know now',
                '<div class="p-reflect">Ask yourself: What is the current level'] if voice == 'p' else
               ['<div class="p-insight">Facilitator prompt: &ldquo;In your experience',
                '<div class="p-insight">Facilitator prompt: &ldquo;Which KPIs in your current scorecard',
                '<div class="p-insight">Facilitator prompt: &ldquo;What does your organisation know now',
                '<div class="p-insight">Facilitator prompt: &ldquo;What is the current level'])
    for a, pr in zip(anchors, S2_CONS):
        d.before(a, pr)
    # Section 3 · 3.1
    for tail, pr in zip(['to produce enterprise outcomes.</p>', 'Key Result being assessed.</p>',
                         'observed continuously.</p>', 'capability-building system.</p>'], S3_GAPS):
        d.after(tail, '\n      ' + pr)
    # 3.2: the map of where the fractures begin comes out
    d.sub(r'<div class="u8-h">Where the four fractures most often begin</div>\n<div class="u8-map">.*?</div></div>\n', '')
    # Section 5 · per-tab example decision points
    old_ex = ["If a Key Result shows no movement across two monthly reviews, its owner presents a recovery plan at the next executive review.",
              "If a Key Result has not been discussed in an executive review for a full month, the CEO places it first on the agenda of the next review, with its owner present.",
              "If the same obstacle is reported in two functions in one quarter, the executive team names the cause and records what it changes in the way the strategy is executed.",
              "If a strategic priority is announced, the executive team fixes the date of its first review and the evidence to be brought to it in the same meeting."]
    for o, c in zip(old_ex, CONS):
        d.rep('<b>An example decision point</b>' + o, '<b>An example decision point</b>' + h(c[3]))

def build_p(src, out):
    t, crlf = load(src); d = Doc(t, 'p')
    common(d, 'p')
    d.rep('What would reflect genuine progress toward your strategic outcome?</p>',
          'What would reflect genuine progress toward your strategic outcome?' + h(S1_REF_ADD) + '</p>')
    d.rep('placeholder="Activity measures I use:&#10;Progress measures I should add:"', 'placeholder="Activity measures I use:&#10;Progress measures I should add:&#10;Evidence on the organisational conditions:"')
    d.rep('and what did the delay cost?</p>', 'and what did the delay cost?' + h(S2_REF_ADD) + '</p>')
    d.after('and the executive team reviews the chain of execution together.</p>\n', S32_REF_P + '\n')
    d.rep('var KEYS=["ref1","ref2","ref8","ref4",', 'var KEYS=["ref1","ref2","ref8","ref4","ref9",')
    d.cut('<div class="acc-b"><div class="cb">\n<p>In class, you role played a case using the GROW model.',
          '<div class="mod-nav"><button class="btn prev" onclick="showMod(2,null)">', S42_P)
    d.sub(r'<div class="u8-how"><div class="u8-how-h">How Section 5 works</div>.*?</div>(?=\n<div class="acc open">)', S5_HOW_P)
    d.rep('<ol><li>Read the lesson for this consequence. Note the signals it describes.</li><li>Agree the two signals of this consequence your executive team is most likely to miss in your strategy.</li><li>For each signal, write one decision point: the signal, the decision your executive team takes when it appears, and who takes it.</li></ol>',
          S5_STEPS, 4)
    for c in '1234':
        d.rep('<label class="wp-label" for="u8_c%s_dp1">Decision point 1</label>' % c, '<label class="wp-label" for="u8_c%s_dp1">%s</label>' % (c, LBL1))
        d.rep('<label class="wp-label" for="u8_c%s_dp2">Decision point 2</label>' % c, '<label class="wp-label" for="u8_c%s_dp2">%s</label>' % (c, LBL2))
    d.rep('placeholder="If [the signal appears], then [the decision], taken by [who]..."', 'placeholder="%s"' % PH, 8)
    d.rep('"Decision point 1", "c', '"Individuals", "c', 4)
    d.rep('"Decision point 2", "c', '"Organisational conditions", "c', 4)
    d.rep('"If [the signal appears], then [the decision], taken by [who]..."', '"%s"' % PH, 8)
    d.rep('/* ════════════ UNIT 8 · SECTION 5 · APPLYING THE FOUR CONSEQUENCES OF WEAK REVIEW DISCIPLINE (group work, Capstone work) ════════════\n   Two decision points against each of the four consequences of part 2.1,',
          '/* ════════════ UNIT 8 · SECTION 5 · APPLYING THE FOUR CONSEQUENCES OF WEAK REVIEW DISCIPLINE (group work, Capstone work) ════════════\n   For each of the four consequences of part 2.1: a potential gap and a decision point for recovery for individuals, and for the organisational conditions,')
    # Unit Summary (JS strings)
    d.rep('each with its own recovery, achieved through the GROW model."}',
          'each with its own recovery, achieved through the GROW model. Each review examines both the progress of what individuals and teams deliver and whether the organisational conditions support the execution of their tasks."}')
    d.rep('and leadership credibility erodes (priorities look symbolic)."}',
          'and leadership credibility erodes (priorities look symbolic). Each consequence shows in the performance of individuals and in the organisational conditions."}')
    d.rep('You then deduced the root cause behind a fall in alignment in a full Accountability Loop conversation, and used the GROW model to plan its resolution and to judge the conversation."}',
          'You then role played an Accountability Loop conversation in a group of three, and analysed a full conversation on a new case to work out the root cause and how the GROW model led the conversation to its goal."}')
    d.rep('body:"Your group set two decision points against each of the four consequences of weak review discipline, for the strategy in your team\\u2019s Capstone Blueprint: the signal to watch for, the decision to take when it appears and who takes it."}',
          'body:"For each of the four consequences of weak review discipline, your group simulated a potential gap in the performance of individuals and in the organisational conditions of the strategy in your team\\u2019s Capstone Blueprint, and set a decision point for recovery for each: the decision the executive team takes when the gap appears, and who takes it."}')
    save(out, d.t, crlf)
    return d.n

def build_f(src, out):
    t, crlf = load(src); d = Doc(t, 'f')
    common(d, 'f')
    fg(d, 'Awareness', S1_FG)
    fg(d, 'Intelligence', S2_FG)
    fg(d, 'Extrapolating', S3_FG)
    fg(d, 'Integration', S4_FG)
    fg(d, 'Application', S5_FG)
    d.rep('and what would reflect genuine progress toward their strategic outcome.</p>',
          'what would reflect genuine progress toward their strategic outcome, and what evidence they hold on whether the organisational conditions support the tasks behind that progress.</p>')
    d.rep('the consequence that followed and what the delay cost.</p>',
          'the consequence that followed, what the delay cost and whether an organisational condition played a part.</p>')
    d.after('and the executive team reviews the chain of execution together.</p>\n', S32_REF_F + '\n')
    d.cut('<div class="acc-b"><div class="cb">\n<p>Part 4.2 has two parts.',
          '<div class="mod-nav"><button class="btn prev" onclick="showMod(3)">', S42_F)
    d.sub(r'<div class="u8-how"><div class="u8-how-h">How Section 5 works</div>.*?</div>(?=\n<div class="acc open">)', S5_HOW_F)
    names = ['early warning signals are missed', 'gradual diffusion of accountability', 'loss of organisational learning', 'erodes leadership credibility']
    for nm, c in zip(names, CONS):
        d.rep('<ul class="u8-list"><li>two decision points against ' + nm + ': for each, the signal, the decision the executive team takes when it appears and who takes it</li></ul>',
              s5_completes(c[2]))
    # Facilitator Unit Summary cards
    d.rep('and the Accountability Loop diagnoses the root cause of a gap.</p>',
          'and the Accountability Loop diagnoses the root cause of a gap. Each review examines the progress of individuals and teams and whether the organisational conditions support the execution of their tasks.</p>')
    d.rep('organisational learning is lost and leadership credibility erodes.</p>',
          'organisational learning is lost and leadership credibility erodes, in the performance of individuals and in the organisational conditions.</p>')
    d.rep('Each executive role tends to feed one or two of these four fractures.</p>',
          'Each fracture affects human and organisational performance, and each executive role tends to feed one or two of them.</p>')
    d.rep('In the Accountability Loop role play, the CXO deduces the root cause behind a fall in alignment and resolves it through the GROW model.</p>',
          'In the Accountability Loop role play, groups of three practise a conversation with an end in mind through the GROW model; after class, each participant works out the root cause in a full conversation on a new case.</p>')
    d.rep('Each group set two decision points against each of the four consequences of weak review discipline, for its own strategy. The confirmed record feeds the team’s Capstone Blueprint.</p>',
          'For each of the four consequences of weak review discipline, each group simulated a potential gap in the performance of individuals and in the organisational conditions of its own strategy, and set a decision point for recovery for each. The confirmed record feeds the team’s Capstone Blueprint.</p>')
    save(out, d.t, crlf)
    return d.n

if __name__ == '__main__':
    a, b, c, e = sys.argv[1:5]
    print('participant edits', build_p(a, c))
    print('facilitator edits', build_f(b, e))
