# -*- coding: utf-8 -*-
"""Unit 4 rebuild (October 2026) — facilitator file, on Carol's brief of 7 October 2026.
Usage: python3 build_f.py <facilitator file as it stood before the rebuild> <new file>
Run it from this folder: it reads u4_content.py and u4.css.
The file stays preparation-only: no entry box, no score, nothing saved. It fails if a time is left.
Section 3 (times removed) and the answer key are cut from the old file byte for byte. Line endings (CRLF) and UTF-8 are kept."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u4_content as C
src, out = sys.argv[1], sys.argv[2]
def read(name): return open(os.path.join(HERE, name), 'rb').read().decode('utf-8').replace('\r\n', '\n')
h = open(src, 'rb').read().decode('utf-8')
assert h.count('\r\n') == h.count('\n'), 'expected CRLF line endings'
h = h.replace('\r\n', '\n')

def rep(old, new, count=1):
    global h
    n = h.count(old)
    assert n == count, 'expected %d match(es), found %d: %s' % (count, n, old[:90])
    h = h.replace(old, new)

ARR = '<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div>'
def acc(title, meta, body, open_=False, style=''):
    return ('<div class="acc' + (' open' if open_ else '') + '"' + style + '>\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">' + title + '</span>\n'
            '  <div style="display:flex;align-items:center;gap:10px;"><span class="acc-meta">' + meta + '</span>' + ARR + '</div>\n</div>\n'
            '<div class="acc-b cb">\n' + body.strip('\n') + '\n</div>\n</div>\n')
def guide(label, paras, style=''):
    return ('  <div class="fac-note-full"' + style + '><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; ' + label + '</div>\n' +
            ''.join('    <p>' + p + '</p>\n' for p in paras) + '  </div>\n')
def activity(lead, steps, tail=''):
    return ('  <div class="fac-note-full u4-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n    <p>' + lead + '</p>\n' +
            ('    <ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>\n' if steps else '') + ('    <p>' + tail + '</p>\n' if tail else '') + '  </div>\n')
def slo(n):
    a, b = C.SLO[n]
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>' + a + '</li><li>' + b + '</li></ul></div>\n'
def section(idx, comment, label, title, sub, body, nav):
    return ('<!-- ' + comment + ' -->\n<div class="mod-panel" id="mod%d">\n' % idx +
            '<div class="mod-hero">\n  <div class="mod-hero-label">' + label + '</div>\n  <h2>' + title + '</h2>\n  <p>' + sub + '</p>\n</div>\n'
            '<div class="mod-body">\n' + body.strip('\n') + '\n' + nav + '</div>\n</div>\n')
def nav(prev, nxt):
    return '<div class="mod-nav">\n  ' + prev + '\n  ' + nxt + '\n</div>\n'
def say(t): return '<p class="u4-say">&ldquo;' + t + '&rdquo;</p>'

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + '\n:root{--u4:#c9a84c;--u4-bg:rgba(201,168,76,.07);--u4-bd:rgba(201,168,76,.28);}' + read('u4.css') + h[i:]

# ── 1. Facilitator Guide tab: the unit as it now runs; no times ───────────────────────────────────
rep('turn assumptions into named, verifiable conditions with owners.</p>', 'turn assumptions into named, verifiable conditions.</p>')
rep('<p>The ABCV&ndash;MBT Working Papers in Section 4 and the diagnosis exercise in Section 5 carry the unit. Insist on specific conditions and named owners.</p>',
    '<p>The Key Results tested are the ones the group confirmed in Unit 3: no new objective or metric enters the unit. The Industry Illusion game in Section 2, the ABCV&ndash;MBT Working Papers in Section 4 and the diagnosis game in Section 5 carry the unit. Insist on specific conditions.</p>')
rep('<p><strong>Close:</strong> reserve the final minutes for the unnamed Must-Be-True question above. A named owner and date are the output.</p>',
    '<p><strong>Close:</strong> end on the unnamed Must-Be-True question above.</p>')

# ── 2. Slice the page at its section markers ──────────────────────────────────────────────────────
M = ['<div class="mod-panel" id="mod1">', '<!-- ===== TAB 2: INTELLIGENCE ===== -->', '<!-- ===== TAB 3: EXTRAPOLATING ===== -->', '<!-- TAB 4: INTEGRATION ZONE -->',
     '<!-- TAB 5: APPLICATION -->', '</div><!-- end tabs-content -->']
pos = [h.index(m) for m in M]
assert pos == sorted(pos) and all(h.count(m) == 1 for m in M)
head, s3, s5_old, tail = h[:pos[0]], h[pos[2]:pos[3]], h[pos[4]:pos[5]], h[pos[5]:]

# ── 3. Section 1 ──────────────────────────────────────────────────────────────────────────────────
def strip(items):
    return '  <div class="u4-flow">' + '<div class="u4-flow-a">&rarr;</div>'.join('<div class="u4-flow-s"><b>%s</b><span>%s</span></div>' % x for x in items) + '</div>\n'
four = '  <div class="u4-four">' + ''.join('<div class="u4-four-c %s"><b>%s</b><span>%s</span></div>' % (C.CP[k]['cls'], n, q) for k, n, q in C.OVERVIEW_Q) + '</div>\n'
overview = (guide('Overview', [
                '<strong>Key message:</strong> Most strategies fail from unnamed conditions. The cost of discovering those conditions during execution is exponentially higher than naming them now.',
                '<strong>Discussion prompt:</strong> <em>"Think of a goal that failed in your organisation. Was it a lack of effort, or was there an assumption that turned out to be wrong &mdash; one you didn&#39;t name until it broke?"</em>',
                '<strong>The flow:</strong> Show how the unit runs before any checkpoint is taught: the Key Results from Unit 3, the four checkpoints, one Must-Be-True condition at each checkpoint for each Key Result.']) +
            '  <p>In Unit 3 the group translated its Success in Practice into Enterprise OKRs. They are measurable, they are ambitious and they have deadlines. The next step is to move past well-written OKRs and ask whether they are strategically sound.</p>\n'
            '  <p>ABCV is used to interrogate whether an agreed strategic direction is sound enough to carry into execution. A strategy or OKR may be clear, measurable and ambitious and still rest on assumptions that have not been tested.</p>\n'
            '  <p>Most strategies fail because of unnamed conditions. Goals are built on a bed of invisible assumptions that are discovered only once execution begins and things start to break. By then, the cost of correction is massive.</p>\n'
            '  <p>ABCV forces leaders to examine the strategic logic through four checkpoints:</p>\n' + four +
            '  <p>For each checkpoint, <strong>MBT (Must-Be-True)</strong> makes the underlying assumption explicit. It names the load-bearing walls of the goals: the specific condition that must remain true for a Key Result to survive. If one of these conditions shifts or fails, the Key Result becomes fragile by design.</p>\n'
            '  <h4>The Logic</h4>\n' + strip(C.STEPS) + '  <p>At each step, name what Must Be True.</p>\n' +
            '  <h4>From Unit 3 to Unit 4</h4>\n' + strip([('From Unit 3', 'The group&rsquo;s Enterprise OKRs: the Objectives and Key Results it confirmed.'),
                                                           ('Four checkpoints', 'Arena &middot; Boundaries &middot; Competition &middot; Value Proposition.'),
                                                           ('Must-Be-True conditions', 'One at each checkpoint, for each Key Result.')]) +
            '  <h4>What the Test Secures</h4>\n  <p>Strategic priorities that are:</p>\n'
            '  <ol class="u4-ol"><li>Anchored in customer reality.</li><li>Designed to withstand operational constraints.</li><li>Positioned accurately against the competitive landscape.</li><li>Coherent with the organisation&rsquo;s core value.</li></ol>\n'
            '  <p>By naming these conditions early, leaders create an early-warning system that detects risks before a well-written ambition collapses under the weight of reality.</p>\n' +
            activity('Participants write a reflection in their own file: one Key Result their group confirmed in Unit 3, and what it assumes about the world that has not yet been verified.', []))
MOVE = ('<strong>Facilitation move:</strong> Take one of the group&rsquo;s Unit 3 Key Results. Ask the question in the &ldquo;applied to a Key Result&rdquo; box, then ask for the condition that must remain true. '
        'Hold out for a condition that is either true or false.')
EG = '<strong>On the examples:</strong> The teaching examples come from higher education. The two Key Results in the last box come from the client services company participants met in Unit 3, part 2.2; the same two run through all four checkpoints.'
CP_GUIDE = {
    'a': ['<strong>The Nokia moment:</strong> Use the smartphone analogy specifically. Nokia defined themselves as a telecoms company. The smartphone redefined the arena entirely. Ask: <em>"Who in your industry is playing a different game that you&#39;re only just starting to notice?"</em>',
          '<strong>The three depths:</strong> Teach Functional, Experiential and Consequential as three depths of one interrogation. After presenting them, ask leaders to apply them to their primary customer. Most find the experiential and consequential depths are rarely discussed in their strategy sessions, which is exactly the blind spot.',
          MOVE, EG],
    'b': ['<strong>Key message:</strong> Defining the right Arena does not mean the organisation can succeed within it. Look for the boundaries material enough to affect the outcome.',
          '<strong>Discussion:</strong> Ask which boundaries the organisation must accept, which it can influence and which it created itself. The self-created boundary generates particularly useful executive discussion.', MOVE],
    'c': ['<strong>Key message:</strong> Once the Arena is defined by the Customer End Game, the competitive field can look very different.',
          '<strong>Watch for:</strong> competition defined as industry rivals only. Push for every alternative route the customer has to the outcome, including doing nothing.', MOVE],
    'v': ['<strong>Key message:</strong> Positive attributes do not automatically establish strategic value. Test every claim for relevance, distinctiveness and deliverability.', MOVE],
}
EG_LABEL = 'Examples &middot; two Key Results from the Unit 3 worked example'
s1_body = (slo(1) + guide('Section 1 &middot; Awareness', [
               '<strong>Section intent:</strong> This opening section introduces the ABCV&ndash;MBT framework as a strategic integrity filter. Create a felt sense of productive discomfort: <em>"Are our OKRs actually grounded in reality?"</em> Leaders must feel the danger of unnamed assumptions before they can value the discipline of naming them.',
               '<strong>Opening frame:</strong> Before content, ask: <em>"How many of you have experienced a well-crafted strategy that fell apart once execution started because of assumptions we hadn&#39;t named until they broke?"</em> Pause. Use the silence. Then introduce ABCV&ndash;MBT as the tool that names those invisible assumptions before they become expensive failures.',
               '<strong>Order:</strong> Teach the overview first, then the four checkpoints one at a time, then bring them together. The group arrives with the Enterprise OKRs it confirmed in Unit 3; every exercise in this unit works on those Key Results.'],
               ' style="margin-top:22px;"') +
           acc('Overview &mdash; From Unit 3 to Unit 4', 'Strategic Context', overview, True))
for n, c in enumerate(C.CHECKPOINTS):
    s1_body += acc('1.%d &mdash; %s' % (n + 1, c['name']), c['tag'], guide('Section 1.%d' % (n + 1), CP_GUIDE[c['k']]) + C.cp_part_body(c, EG_LABEL))
s1_body += acc('Bringing ABCV Together', 'The Integrated View', guide('Bringing ABCV Together', [
    '<strong>Close the teaching with the integrated view.</strong> Walk down the chain once, then land the line at the foot of it.']) + C.together_html(), True)
s1_body += ('<div class="fac-note" style="margin-top:18px;"><div class="fac-label">Facilitator Move &mdash; After the Checkpoints</div><p>Ask: <em>"If you had to identify the single ABCV checkpoint your organisation most consistently overlooks when setting strategy &mdash; which would it be? And what has that cost you?"</em> The answers surface role-based blind spots you will revisit in the Extrapolating section.</p></div>\n' +
            activity('Participants answer the same question as a reflection in their own file.', []))
s1 = section(1, 'TAB 1: AWARENESS', 'Section 1 · Awareness — What', 'What are the ABCV&ndash;MBT Integrity Checkpoints?',
             'Interrogative Anchor &middot; Leaders have defined their OKRs. Now the question is whether they are strategically sound. The ABCV&ndash;MBT framework is the stress test for reality.',
             s1_body, '<div class="mod-nav"><button class="btn prev" onclick="showMod(0)">← Facilitator Guide</button><button class="btn" onclick="showMod(2)">Section 2 — Intelligence →</button></div>\n')

# ── 4. Section 2 ──────────────────────────────────────────────────────────────────────────────────
G = C.GAME
def lst(items): return '<ul>' + ''.join('<li>' + x + '</li>' for x in items) + '</ul>'
def tests(n): return '  <div class="fac-note"><div class="fac-label">What this round tests &middot; facilitator only</div><p>' + G['tests'][n] + '</p></div>\n'
steps = ['Case Brief', 'Round 1', 'Round 2', 'Round 3', 'The Reveal', 'Apply Arena']
names = [G['title'], G['r1_title'], G['r2_title'], G['r3_title'], 'Their decisions', 'The learning moment']
tabs = '<div class="step-tabs">\n' + ''.join(
    '  <div class="step-tab%s" onclick="showStep(%d,this)"><div class="step-num">%s</div><div class="step-name">%s</div></div>\n' % (' active' if n == 0 else '', n, s, names[n])
    for n, s in enumerate(steps)) + '</div>\n'
panels = [
    '  <p>Tell participants:</p>\n  ' + say('You are the executive team of Apex University, an established private university.') + '\n  ' + C.brief_html() + '\n',
    '  <p>Tell participants:</p>\n  ' + say(G['r1_prompt']) + '\n  <p>Give them these eight intelligence sources and tell them: <strong>' + G['r1_do'] + '</strong></p>\n  ' +
    lst('<strong>%s.</strong> %s' % s for s in G['sources']) + '\n' + tests(0) + '  <p>Do not reveal this. Record the choices.</p>\n',
    '  <p>Tell participants:</p>\n  ' + say(G['r2_prompt']) + '\n  ' + lst('<strong>Signal %d.</strong> %s' % (n + 1, s) for n, s in enumerate(G['signals'])) +
    '\n  <p>Ask:</p>\n  ' + say(G['r2_q1']) + '\n  <p>Then:</p>\n  ' + say(G['r2_q2']) + '\n  <p>Require them to make the decision.</p>\n' + tests(1) +
    '  <p>Again, do not reveal the trap. Capture what they excluded and, importantly, why.</p>\n',
    '  <p>Give them the Apex University performance report.</p>\n  ' + C.report_html() + '\n  <p>Then tell them:</p>\n  ' + say(G['r3_prompt']) + '\n  <p>Give them three choices:</p>\n  ' +
    lst('<strong>%s. %s.</strong> %s' % c for c in G['choices']) + '\n  <p>Each group must select one and defend it.</p>\n' + tests(2),
    '  <p>Now return to their decisions.</p>\n' + ''.join(
        '  <div class="u4-rev"><div class="u4-rev-h"><small>%s</small><span>%s</span></div><div class="u4-rev-b"><p>Then reveal:</p><div class="u4-rev-trap">%s</div><div class="u4-rev-line">%s</div>%s</div></div>\n'
        % (r['round'], r['ask'], r['trap'], r['line'], say(r['q'])) for r in G['reveal']) +
    '  <p>Now show how the illusion forms:</p>\n' + C.chain_html() + '\n  <p>Then give them the crucial insight:</p>\n  ' + say(G['insight']) + '\n',
    '  <p>Only after the reveal, bring them back to ABCV. Ask:</p>\n  ' + say(G['arena_q']) + '\n  <p>Do not give them the answer. Make them work through the three depths of the Customer End Game taught in 1.1:</p>\n  ' +
    lst('<strong>%s:</strong> %s' % a for a in G['arena']) + '\n  <p>Then give them the final challenge:</p>\n  ' + say(G['final']) +
    '\n  <p>That is the learning moment. The game has not told them they suffer from the Industry Illusion. Their own choices provide the evidence. Arena becomes the mechanism for testing and expanding their field of strategic attention.</p>\n',
]
game = (guide('Section 2.2', [
            '<strong>Important:</strong> Do not tell participants which illusion each round is testing. Do not correct their answers during the game. Capture their decisions. Reveal the traps only at the end.',
            '<strong>In the lesson:</strong> Play the game with the room in groups, in this order: case brief, Round 1, Round 2, Round 3, the reveal, then Arena. Each group makes its decision and defends it.']) +
        tabs + ''.join('<div class="step-panel%s" id="step%d">\n%s</div>\n' % (' active' if n == 0 else '', n, p) for n, p in enumerate(panels)) +
        activity('After the lesson, each participant completes the game alone in 2.2 of their own file, as portfolio work:', [
            'They read the case brief.',
            'They play Round 1, Round 2 and Round 3 in order. Each decision is locked and cannot be changed.',
            'They open The Reveal once all three rounds are locked. It shows their own decisions beside each trap.',
            'They answer the Arena questions and the final challenge.'],
            'The game becomes part of the participant&rsquo;s Learning Portfolio. It reaches you when the participant selects Submit to Facilitator at the end of the unit.'))
s2_body = (slo(2) + guide('Section 2 &middot; Intelligence', [
               '<strong>Section intent:</strong> Leaders discover, through their own decisions, how an industry frame shapes what they notice, dismiss and trust. The game supplies the evidence. Arena supplies the test.',
               '<strong>Order:</strong> Teach the Industry Illusion (2.1), then play the game with the room (2.2).'], ' style="margin-top:22px;"') +
           acc('2.1 &mdash; The Industry Illusion', '3 Traps', guide('Section 2.1', [
               '<strong>Key message:</strong> Industry knowledge is essential to strategy. The illusion begins when the frame that knowledge creates is treated as the boundary of what is strategically relevant.',
               '<strong>Teach the three traps in order.</strong> Each one reinforces the next. Keep the examples general here: the game supplies the case.']) + C.industry_illusion_teaching(), True) +
           acc('2.2 &mdash; The Industry Illusion Game: The Future of a University', '3 Rounds &middot; Portfolio Work', game))
s2 = section(2, '===== TAB 2: INTELLIGENCE =====', 'Section 2 · Intelligence — Why', 'The Industry Illusion', C.II_BOUNDARY, s2_body,
             nav('<button class="btn prev" onclick="showMod(1)">← Section 1 — Awareness</button>', '<button class="btn" onclick="showMod(3)">Section 3 — Extrapolating →</button>'))

# ── 5. Section 3: as it stands; times removed ─────────────────────────────────────────────────────
for t in (' <em>Suggested section time: 20&ndash;25 minutes.</em>', ' <em>Suggested time: 10&ndash;12 minutes.</em>'):
    assert s3.count(t) == 1, t
    s3 = s3.replace(t, '')

# ── 6. Section 4 ──────────────────────────────────────────────────────────────────────────────────
STEP_NOTES = ['The group says which customer need the Key Result serves, at three depths (functional, experiential, consequential). Then it names what must remain true about that need.',
              'The group lists the boundaries material enough to slow, restrict or prevent delivery of the Key Result, with the kind of each and whether it must be accepted, can be influenced or was created by the organisation itself. Then it names what must remain true for delivery.',
              'The group lists who or what else can give the customer what the Key Result delivers, including alternatives outside the industry and doing nothing. Then it names what must remain true about its advantage.',
              'The group says what about the Key Result will make customers choose the organisation, using the three tests (relevant, distinctive, deliverable). Then it names what must remain true about its value architecture.']
worked = (guide('Section 4.1', [
              '<strong>How to teach it:</strong> The example continues the client services company participants met in Unit 3, part 2.2. It takes one Key Result through the four steps. Walk through the steps in order.',
              '<strong>At the end of each step:</strong> Read the Must-Be-True condition aloud and ask what it would look like if it failed. Each condition is either true or false.',
              '<strong>Point to draw out:</strong> The exercise in 4.2 is this example repeated on the group&rsquo;s own Key Results: the same four steps, in the same order.']) +
          '  <p>This example continues the client services company of Unit 3, part 2.2. Its Success in Practice reads: &ldquo;' + C.WORKED_SIP + '&rdquo;</p>\n'
          '  <p>The company takes one of its Key Results through the four steps. Each step ends with the condition that must remain true for the Key Result to hold. Select each step in turn.</p>\n' +
          C.worked_html('wf') + '\n'
          '  <div class="u4-quote" style="margin-top:14px;"><p>Four steps, four conditions. If one of them shifts or fails, the Key Result becomes fragile by design.</p></div>\n')
tool = (guide('Section 4.2', [
            '<strong>Briefing for participants:</strong> The group does for its own Key Results what the worked example did: the same four steps, in the same order. No new objective or measure is added.',
            '<strong>On the conditions:</strong> The condition the group names must be specific enough that someone else could attempt to verify it. Vague conditions (&ldquo;the market must support us&rdquo;) are not sufficient. Push for precision.',
            '<strong>Watch for:</strong> Groups that struggle to name a condition. This is a signal that the Key Result itself may not be sufficiently grounded. Use it as productive friction: <em>&ldquo;If you cannot name a Must-Be-True, what does that tell you about this Key Result?&rdquo;</em>',
            '<strong>Watch for:</strong> conditions written as risks or concerns. Each must be a condition that is either true or false.',
            '<strong>Closing the section:</strong> End with a commitment question: <em>&ldquo;Which one MBT condition, if left unverified, represents the greatest risk to our strategy&rsquo;s integrity? Who is leaving this room responsible for that verification?&rdquo;</em>']) +
        activity('Participants work in their groups, in 4.2 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
                 ['The group&rsquo;s confirmed Key Results from Unit 3 are listed in 4.2. If they are missing, the participant selects Bring in from my Unit 3 page. Nothing is typed again.',
                  'The group selects one Key Result.'] +
                 ['<strong>%s &middot; %s.</strong> %s' % (C.STEPS[n][0], C.STEPS[n][1], t) for n, t in enumerate(STEP_NOTES)] +
                 ['The group selects the next Key Result and repeats the four steps.',
                  'A record shows the condition named at each step for every Key Result. When every Key Result has been taken through the four steps, each participant selects Confirm. Print gives a copy of the record.'],
                 'The confirmed work feeds the team&rsquo;s Capstone Blueprint.'))
s4_body = (slo(4) + guide('Section 4 &middot; Integration', [
               '<strong>Section intent:</strong> This is where the checkpoints are applied to the group&rsquo;s own direction. The group brings in the Key Results it confirmed in Unit 3 and takes each one through four steps, naming at each step the condition that must remain true.',
               '<strong>Order:</strong> Teach the worked example in full (4.1), then brief the Capstone work (4.2). The exercise follows the worked example step for step.'], ' style="margin-top:22px;"') +
           acc('4.1 &mdash; Worked Example: Stress-Testing a Key Result', '4 Steps &middot; Worked Example', worked, True) +
           acc('4.2 &mdash; Stress-Testing Your Key Results', '4 Steps &middot; Capstone Work', tool))
s4 = section(4, 'TAB 4: INTEGRATION', 'Section 4 · Integration — Collective', 'ABCV&#8211;MBT Working Papers',
             'The group stress-tests its Unit 3 Key Results on the four ABCV checkpoints. This is Capstone work: the confirmed outputs feed each team&rsquo;s Capstone Blueprint.',
             s4_body, nav('<button class="btn prev" onclick="showMod(3)">← Section 3 — Extrapolating</button>', '<button class="btn" onclick="showMod(5)">Section 5 — Application →</button>'))

# ── 7. Section 5: the four scenarios and the answer key stay; no score, no empty labels; portfolio work ──
cards = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:28px;" id="mineGrid">\n' + ''.join(
    '<div class="mine-card" id="mine%d">\n  <div class="mine-label" onclick="toggleMine(this)">&#128163; Mine %d &mdash; %s</div>\n  <div class="mine-body">\n  <p class="mine-scenario">%s</p>\n  </div>\n</div>\n' % (n, n + 1, m['name'], m['scenario'])
    for n, m in enumerate(C.MINES)) + '</div>\n'
TH = '<th style="padding:8px 12px;text-align:left;color:var(--gold);border-bottom:1px solid rgba(201,168,76,.2);">%s</th>'
key = (acc('Facilitator &middot; Answer Key', 'FAC ONLY',
           guide('Answer Key', ['Use this key for post-game debrief. Do not reveal answers before participants have attempted each mine. The value is in the diagnostic reasoning.',
                                'Each mine is answered in two parts: the investigation question that reveals the illusion, then the ABCV checkpoint where that illusion sits. Complacency appears twice.']) +
           '<div class="u4-egs-h">The three investigation questions</div>\n<table class="u4-tbl"><tbody>' +
           ''.join('<tr><td><strong>Q%d</strong> &middot; reveals %s</td><td>%s</td></tr>' % (i + 1, x['name'], x['q']) for i, x in enumerate(C.ILLUS)) + '</tbody></table>\n'
           '<table style="width:100%;border-collapse:collapse;font-size:13px;margin-top:16px;">\n  <thead><tr style="background:rgba(201,168,76,.12);">' +
           ''.join(TH % t for t in ('Mine', 'Illusion revealed', 'Where it sits', 'Core insight')) + '</tr></thead>\n  <tbody>\n' +
           ''.join('    <tr style="border-bottom:1px solid rgba(255,255,255,.05);"><td style="padding:8px 12px;">%s</td><td style="padding:8px 12px;">Q%d &mdash; %s</td>'
                   '<td style="padding:8px 12px;color:%s;font-weight:700;">%s</td><td style="padding:8px 12px;">%s</td></tr>\n'
                   % (m['name'], [x['k'] for x in C.ILLUS].index(m['ill']) + 1, C.illus(m['ill'])['name'], m['col'], m['cpname'], m['insight']) for m in C.MINES) +
           '  </tbody>\n</table>\n', False, ' style="margin-top:10px;"') + '\n')
def stage(col, bg, title, inner, last=False):
    return ('<div style="border-left:3px solid %s;padding:16px 20px;background:%s;border-radius:0 4px 4px 0;margin-bottom:%dpx;">\n'
            '  <div style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:%s;margin-bottom:8px;">%s</div>\n%s</div>\n' % (col, bg, 20 if last else 14, col, title, inner))
summary = (guide('Unit Summary', ['<strong>Closing the unit:</strong> Unit 4 reframes strategy integrity as a testable condition. Close by asking: <em>&ldquo;What is the one MBT condition your team is most likely to avoid naming? Why? And what will you do about it before the next strategic review?&rdquo;</em>']) +
           '\n<div style="margin-bottom:22px;">\n'
           '  <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.15rem;line-height:1.85;color:rgba(255,255,255,.85);">This session was about ensuring strategic direction is structurally sound before the first move of execution is made. We&rsquo;ve all seen well-written OKRs collapse because the assumptions holding them up were never tested. The ABCV&ndash;MBT framework served as our strategic integrity filter: the stress test to ensure Key Results are anchored in customer reality, resilient to friction, and true to the organisation&rsquo;s identity.</p>\n'
           '  <p style="font-size:13px;color:rgba(255,255,255,.5);margin-top:-6px;">Here is a recap of the unit, section by section.</p>\n</div>\n\n' +
           stage('#8ab0e8', 'rgba(107,143,204,.06)', '1 &mdash; Awareness: The Four Integrity Checkpoints',
                 '  <p>We began with the <em>What.</em> A well-written OKR can still rest on unnamed conditions. ABCV examines the strategic logic at four checkpoints:</p>\n'
                 '  <ul style="margin:10px 0 10px 18px;">\n'
                 '    <li><strong style="color:#8ab0e8;">Arena</strong> &mdash; What the customer is ultimately trying to achieve, read at three depths: functional, experiential and consequential.</li>\n'
                 '    <li><strong style="color:#f0c060;">Boundaries</strong> &mdash; The conditions that could constrain our ability to deliver.</li>\n'
                 '    <li><strong style="color:#5ecba1;">Competition</strong> &mdash; Who or what else can satisfy the same end game.</li>\n'
                 '    <li><strong style="color:#c39de0;">Value Proposition</strong> &mdash; Value that is relevant, distinctive and deliverable.</li>\n  </ul>\n'
                 '  <p>At each checkpoint, a Must-Be-True (MBT) condition makes the underlying assumption explicit, with examples on Key Results from Unit 3. This is the early warning system: exposing risks before they become expensive failures.</p>\n') +
           stage('var(--gold)', 'rgba(201,168,76,.06)', '2 &mdash; Intelligence: The Industry Illusion',
                 '  <p>This stage explored the <em>Why.</em> Industry knowledge becomes a frame, and three reinforcing traps (Familiarity, Exclusion and Complacency) turn that frame into the boundary of the world leaders examine.</p>\n'
                 '  <p>In the Industry Illusion game the participants&rsquo; own decisions showed what an industry frame leads leaders to notice, dismiss and trust. They then applied Arena to the case.</p>\n') +
           stage('#5ecba1', 'rgba(46,168,122,.06)', '3 &mdash; Extrapolating: Locating the Blind Spots',
                 '  <p>Next, the <em>Where.</em> Every CXO sees the world through a specialised perspective:</p>\n'
                 '  <ul style="margin:10px 0 10px 18px;">\n    <li><strong>CEOs</strong> lean toward narrative and stakeholder credibility</li>\n    <li><strong>CFOs</strong> hunt for financial viability and return logic</li>\n'
                 '    <li><strong>COOs</strong> focus on operational feasibility and delivery rhythm</li>\n    <li><strong>CHROs</strong> look at culture and leadership readiness</li>\n  </ul>\n'
                 '  <p>While these perspectives are vital, they naturally create selective attention. Applying the ABCV&ndash;MBT checkpoints across all roles surfaced the hidden risks that usually only emerge halfway through the execution cycle.</p>\n') +
           stage('#c39de0', 'rgba(155,89,182,.06)', '4 &mdash; Integration: Stress-Testing the Key Results',
                 '  <p>The group brought in the Key Results it confirmed in Unit 3 and took each one through the four steps of the worked example: it defined the Arena, set out the Boundaries, mapped the Competition and established the Value Proposition, and at each step it named the condition that must remain true. The confirmed work feeds each team&rsquo;s Capstone Blueprint.</p>\n') +
           stage('#f0a070', 'rgba(230,126,34,.06)', '5 &mdash; Application: Diagnosing the Breakdown',
                 '  <p>In Cause of Death each participant tested four failed strategies against the Industry Illusion: first the illusion at work, then the ABCV checkpoint where that illusion sat. When the breakdown is misidentified, the organisation applies the wrong intervention and reinforces the problem.</p>\n', True) +
           '<div style="background:rgba(201,168,76,.08);border:1px solid rgba(201,168,76,.25);border-radius:4px;padding:16px 20px;">\n'
           '  <p style="font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;color:rgba(255,255,255,.9);line-height:1.8;margin:0;">The ABCV&ndash;MBT checkpoints have transformed your OKRs from polished aspirations into resilient execution signals, grounded in the hard realities of the enterprise system.</p>\n</div>\n')
s5_body = (slo(5) + guide('Section 5 &middot; Application', [
               '<strong>Section intent:</strong> Participants apply ABCV diagnostic thinking under pressure. Each scenario is a real-world strategy failure in which an Industry Illusion kept leaders from seeing the breakdown. Participants find the illusion first, then the ABCV checkpoint where that illusion sits. The mine mechanic rewards precision &mdash; guessing the right checkpoint for the wrong reason will eventually surface. Push participants to articulate their reasoning before selecting an answer.',
               '<strong>Debrief move:</strong> After the game, ask: &ldquo;Which mine was hardest to defuse? What does that tell you about your organisation&rsquo;s own ABCV blind spot?&rdquo;'], ' style="margin-top:22px;"') +
           '\n<div class="fac-note" style="margin-bottom:18px;">&#128204; <strong>Facilitator:</strong> The Answer Key accordion below is visible only in this facilitator file. Participants see the same game without the key.</div>\n\n' +
           activity('Each participant plays the game alone in Section 5 of their own file, as portfolio work:', [
               'They open a mine and read the scenario.',
               '<strong>They find the illusion.</strong> They select the investigation question the scenario answers. Each of the three questions reveals one illusion: Familiarity, Exclusion or Complacency.',
               '<strong>They find where it sits.</strong> They select the ABCV checkpoint the illusion hid from leaders: Arena, Boundaries, Competition or Value Proposition.',
               'They select Submit Answer. When both are right the mine is defused and the page names the illusion and the checkpoint. A wrong answer detonates the mine; a hint says which part was wrong, and they try again.',
               'They defuse all four mines.'],
               'A mine defused at the first attempt earns 2 points; at a later attempt, 1 point. The maximum is 8. The result becomes part of the participant&rsquo;s Learning Portfolio and reaches you when the participant selects Submit to Facilitator at the end of the unit. Participants also write a closing commitment in their own file.') +
           '\n' + cards + '\n' + key +
           acc('Unit Summary', 'Unit 4 synthesis', summary, False, ' style="margin-top:18px;"') +
           '\n<div class="mod-nav">\n  <button class="btn prev" onclick="showMod(4)">← Section 4 — Integration</button>\n  <button class="btn" onclick="goBack()">&#8592; Back to Dashboard</button>\n</div>\n')
s5 = ('<!-- TAB 5: APPLICATION -->\n<div class="mod-panel" id="mod5">\n<div class="mod-hero">\n  <div class="mod-hero-label">Section 5 · Application — In Practice</div>\n'
      '  <h2>Cause of Death &mdash; Match the Breakdown</h2>\n  <p>Portfolio work &middot; Diagnose the strategic failure &middot; Defuse the mine before it detonates.</p>\n</div>\n'
      '<div class="mod-body">\n' + s5_body + '</div>\n</div>\n\n')

h = head + s1 + s2 + s3 + s4 + s5 + tail

# ── 8. Script: no dead game code on a preparation-only page ───────────────────────────────────────
a = h.index('/* ── Integration ── */'); b = h.index('/* ── Back ── */')
U4TAB = ("function u4Tab(gid,i){var g=document.getElementById(gid);if(!g)return;g.querySelectorAll('.u4-stage').forEach(function(t,x){t.classList.toggle('active',x===i);});"
         "g.querySelectorAll('.u4-wpanel').forEach(function(p,x){p.classList.toggle('active',x===i);});}\n\n")
assert 'function checkMine' in h[a:b] and 'function saveTA' in h[a:b]
h = h[:a] + U4TAB + h[b:]

# ── 9. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
vis = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<!--[\s\S]*?-->', ' ', h)
vis = re.sub(r'<[^>]+>', ' ', vis)
for pat in (r'\bminutes?\b', r'Suggested (?:section |total section )?time', r'\bPacing\b', r'whiteboard', r'flip chart'):
    m = re.search(pat, vis, re.I)
    assert not m, 'time or board reference left: ' + vis[max(0, m.start() - 60):m.end() + 40]
for bad in ('<textarea', '<input', '<select', 'contenteditable', 'localStorage.setItem', 'id="scoreboard"', 'checkMine', 'Meridian', 'SELECT THE', 'Integration Zone', 'INTEGRATION ZONE', 'Learners'):
    assert bad not in h, 'still present: ' + bad
assert h.count('id="mod') == 6 and h.count('class="mod-panel') == 6
assert h.count('<script') == h.count('</script>')
assert h.count('<div') == h.count('</div>'), 'div balance %d / %d' % (h.count('<div'), h.count('</div>'))
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('facilitator file written:', out, len(h))
