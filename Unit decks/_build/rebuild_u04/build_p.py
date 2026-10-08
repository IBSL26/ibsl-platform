# -*- coding: utf-8 -*-
"""Unit 4 rebuild (October 2026) — participant file, on Carol's brief of 7 October 2026.
Usage: python3 build_p.py <participant file as it stood before the rebuild> <new file>
Run it from this folder: it reads u4_content.py, u4.css and u4_p.js.
Section 3 and the portal plumbing are cut from the old file byte for byte. Line endings (CRLF) and UTF-8 are kept."""
import sys, os, re, json
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
def acc(title, meta, body, open_=False):
    return ('<div class="acc' + (' open' if open_ else '') + '">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">' + title + '</span>\n'
            '  <div style="display:flex;align-items:center;gap:10px;"><span class="acc-meta">' + meta + '</span>' + ARR + '</div>\n</div>\n'
            '<div class="acc-b cb">\n' + body.strip('\n') + '\n</div>\n</div>\n')
def ref(rid, prompt, label='&#x270E; Reflection'):
    return ('  <div class="ref-block">\n    <div class="ref-block-label">' + label + '</div>\n'
            '    <p style="font-size:12px;color:rgba(255,255,255,.55);margin-bottom:8px;">' + prompt + '</p>\n'
            '    <textarea class="ref-ta reflection-textarea" id="' + rid + '" placeholder="Your reflection here…" style="min-height:80px;"></textarea>\n'
            '  <div class="ref-saved reflection-saved" id="' + rid + '-saved"></div>\n'
            '    <button class="btn" style="margin-top:10px;font-size:11px;padding:7px 16px;" onclick="saveTA(this)">Save Reflection</button>\n  </div>\n')
def slo(n):
    a, b = C.SLO[n]
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>' + a + '</li><li>' + b + '</li></ul></div>\n'
def section(idx, comment, badge, title, sub, body, nav, active=False):
    return ('<!-- ' + comment + ' -->\n<div class="mod' + (' active' if active else '') + '" id="mod%d">\n' % idx +
            '<div class="mod-hero">\n  <div class="mod-hero-content">\n    <div class="mod-badge">' + badge + '</div>\n    <h2 class="mod-title">' + title + '</h2>\n'
            '    <p class="mod-sub">' + sub + '</p>\n  </div>\n</div>\n<div class="mod-body">\n' + body.strip('\n') + '\n\n' + nav + '</div>\n</div>\n\n')
def nav(prev, nxt):
    return '<div class="mod-nav">\n  ' + prev + '\n  ' + nxt + '\n</div>\n'
def how(title, steps, close=''):
    return ('  <div class="u4-how"><div class="u4-how-h">' + title + '</div><ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>' +
            ('<p>' + close + '</p>' if close else '') + '</div>\n')

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + '\n:root{--u4:#1a7a6a;--u4-bg:rgba(26,122,106,.08);--u4-bd:rgba(26,122,106,.3);}' + read('u4.css') + h[i:]

# ── 1. Slice the page at its section markers ──────────────────────────────────────────────────────
M = ['<!-- TAB 1: AWARENESS -->', '<!-- TAB 2: INTELLIGENCE -->', '<!-- TAB 3: EXTRAPOLATING -->', '<!-- TAB 4: INTEGRATION ZONE -->', '<!-- TAB 5: APPLICATION -->']
pos = [h.index(m) for m in M]
assert pos == sorted(pos) and all(h.count(m) == 1 for m in M)
head, s3, tail = h[:pos[0]], h[pos[2]:pos[3]], h[pos[4]:]

# ── 2. Section 1 ──────────────────────────────────────────────────────────────────────────────────
def strip(items):
    return '  <div class="u4-flow">' + '<div class="u4-flow-a">&rarr;</div>'.join('<div class="u4-flow-s"><b>%s</b><span>%s</span></div>' % x for x in items) + '</div>\n'
four = '  <div class="u4-four">' + ''.join('<div class="u4-four-c %s"><b>%s</b><span>%s</span></div>' % (C.CP[k]['cls'], n, q) for k, n, q in C.OVERVIEW_Q) + '</div>\n'
overview = ('  <p>In Unit 3 your group translated its Success in Practice into Enterprise OKRs. They are measurable, they are ambitious and they have deadlines. The next step is to move past well-written OKRs and ask whether they are strategically sound.</p>\n'
            '  <p>ABCV is used to interrogate whether an agreed strategic direction is sound enough to carry into execution. A strategy or OKR may be clear, measurable and ambitious and still rest on assumptions that have not been tested.</p>\n'
            '  <p>Most strategies fail because of unnamed conditions. Goals are built on a bed of invisible assumptions that are discovered only once execution begins and things start to break. By then, the cost of correction is massive.</p>\n'
            '  <p>ABCV forces leaders to examine the strategic logic through four checkpoints:</p>\n' + four +
            '  <p>For each checkpoint, <strong>MBT (Must-Be-True)</strong> makes the underlying assumption explicit. It names the load-bearing walls of your goals: the specific condition that must remain true for a Key Result to survive. If one of these conditions shifts or fails, the Key Result becomes fragile by design.</p>\n'
            '  <h4>The Logic</h4>\n' + strip(C.STEPS) + '  <p>At each step, name what Must Be True.</p>\n' +
            '  <h4>From Unit 3 to Unit 4</h4>\n' + strip([('From Unit 3', 'Your group&rsquo;s Enterprise OKRs: the Objectives and Key Results you confirmed.'),
                                                           ('Four checkpoints', 'Arena &middot; Boundaries &middot; Competition &middot; Value Proposition.'),
                                                           ('Must-Be-True conditions', 'One at each checkpoint, for each Key Result.')]) +
            '  <h4>What the Test Secures</h4>\n  <p>Strategic priorities that are:</p>\n'
            '  <ol class="u4-ol"><li>Anchored in customer reality.</li><li>Designed to withstand operational constraints.</li><li>Positioned accurately against the competitive landscape.</li><li>Coherent with the organisation&rsquo;s core value.</li></ol>\n'
            '  <p>By naming these conditions early, you create an early-warning system that detects risks before a well-written ambition collapses under the weight of reality.</p>\n' +
            ref('ref1', 'Take one Key Result your group confirmed in Unit 3. What is it assuming about the world that has not yet been verified?'))
EG_LABEL = 'Examples &middot; two Key Results from the Unit 3 worked example'
s1_body = slo(1) + '\n' + acc('Overview &mdash; From Unit 3 to Unit 4', 'Strategic Context', overview, True)
for n, c in enumerate(C.CHECKPOINTS):
    s1_body += '\n' + acc('1.%d &mdash; %s' % (n + 1, c['name']), c['tag'], C.cp_part_body(c, EG_LABEL))
s1_body += '\n' + acc('Bringing ABCV Together', 'The Integrated View', C.together_html(), True)
s1_body += '\n' + ref('ref2', 'Which of the four ABCV checkpoints is your organisation least likely to examine rigorously before launching a new strategic initiative? What does that pattern cost you?')
s1 = section(0, 'TAB 1: AWARENESS', 'Section 1 · Awareness — What', 'What are the ABCV&ndash;MBT Integrity Checkpoints?',
             'Interrogative Anchor &middot; Your group has defined its OKRs. Now the question is whether they are strategically sound. The ABCV&ndash;MBT framework is the stress test for reality.',
             s1_body, nav('<button class="btn prev" onclick="goBack()">&#8592; Back to Platform</button>', '<button class="btn" onclick="showMod(1)">Section 2 — Intelligence →</button>'), True)

# ── 3. Section 2 ──────────────────────────────────────────────────────────────────────────────────
game = ('  <p>The game tests whether you fall into each of the three traps. You advise the Board of Apex University on where to focus its strategic attention. Play it on your own.</p>\n' +
        how('Portfolio work &middot; How to complete the game', [
            'Read the case brief.',
            'Play Round 1, Round 2 and Round 3 in order. Make each decision, then select Lock. A locked decision cannot be changed.',
            'Open The Reveal once all three rounds are locked.',
            'Answer the Arena questions and the final challenge.'],
            'Your decisions and your Arena answers become part of your Learning Portfolio. They reach your facilitator when you select Submit to Facilitator at the end of the unit.') +
        '  ' + C.brief_html() + '\n  <div id="iiGameP"></div>\n')
s2_body = (slo(2) + '\n' + acc('2.1 &mdash; The Industry Illusion', '3 Traps', C.industry_illusion_teaching(), True) + '\n' +
           acc('2.2 &mdash; The Industry Illusion Game: The Future of a University', '3 Rounds &middot; Portfolio Work', game))
s2 = section(1, 'TAB 2: INTELLIGENCE', 'Section 2 · Intelligence — Why', 'The Industry Illusion', C.II_BOUNDARY, s2_body,
             nav('<button class="btn prev" onclick="showMod(0)">← Section 1 — Awareness</button>', '<button class="btn" onclick="showMod(2)">Section 3 — Extrapolating →</button>'))

# ── 4. Section 4 ──────────────────────────────────────────────────────────────────────────────────
STEP_LIST = ''.join('<li><strong>%s &middot; %s.</strong> %s</li>' % (C.STEPS[n][0], C.STEPS[n][1], t) for n, t in enumerate([
    'Say which customer need the Key Result serves, at three depths: functional, experiential and consequential. Then name what must remain true.',
    'List the conditions that could slow, restrict or prevent delivery of the Key Result. Then name what must remain true.',
    'List who or what else can give the customer what the Key Result delivers. Then name what must remain true.',
    'Say what about the Key Result will make customers choose you, using the three tests. Then name what must remain true.']))
worked = ('  <p>This example continues the client services company of Unit 3, part 2.2. Its Success in Practice reads: &ldquo;' + C.WORKED_SIP + '&rdquo;</p>\n'
          '  <p>The company takes one of its Key Results through the four steps. Each step ends with the condition that must remain true for the Key Result to hold. Select each step in turn.</p>\n' +
          C.worked_html('wp') + '\n'
          '  <div class="u4-quote" style="margin-top:14px;"><p>Four steps, four conditions. If one of them shifts or fails, the Key Result becomes fragile by design.</p></div>\n')
tool = ('  <p>Your group now does for its own Key Results what the worked example did in 4.1: the same four steps, in the same order. Your group&rsquo;s Key Results come in from Unit 3. No new objective or measure is added.</p>\n'
        '  <div class="u4-how"><div class="u4-how-h">Capstone work &middot; How to complete</div><ol>'
        '<li>Check that your group&rsquo;s Key Results from Unit 3 are listed below. If they are missing, select Bring in from my Unit 3 page.</li>'
        '<li>Select one Key Result.</li>' + STEP_LIST +
        '<li>Select the next Key Result and repeat the four steps.</li>'
        '<li>Read your record, then select Confirm. Select Print for a copy.</li></ol></div>\n'
        '  <div class="u4-btnrow" style="margin:0 0 14px;"><button type="button" class="u4-b" onclick="mbBring(true)">Bring in from my Unit 3 page</button></div>\n'
        '  <div class="u4-note" id="mbBringMsg" style="display:none;margin:-4px 0 14px;"></div>\n'
        '  <div class="u4-rec shut" id="mbRecP"></div>\n  <div id="mbOkrP"></div>\n  <div id="mbToolP"></div>\n  <div id="mbOutP"></div>\n')
s4_body = (slo(4) + '\n<div class="u4-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>\n\n' +
           acc('4.1 &mdash; Worked Example: Stress-Testing a Key Result', '4 Steps &middot; Worked Example', worked, True) + '\n' +
           acc('4.2 &mdash; Stress-Testing Your Key Results', '4 Steps &middot; Capstone Work', tool))
s4 = section(3, 'TAB 4: INTEGRATION', 'Section 4 · Integration — Collective', 'ABCV&#8211;MBT Working Papers',
             'With your group you stress-test your Unit 3 Key Results on the four ABCV checkpoints. This is Capstone work: your confirmed outputs feed your team&rsquo;s Capstone Blueprint.',
             s4_body, nav('<button class="btn prev" onclick="showMod(2)">← Section 3 — Extrapolating</button>', '<button class="btn" onclick="showMod(4)">Section 5 — Application →</button>'))

h = head + s1 + s2 + s3 + s4 + tail

# ── 5. Section 5: the game format stays; the scenarios are tested against the Industry Illusion; portfolio work ──
rep('<p class="mod-sub">Diagnose the strategic failure. Defuse the mine before it detonates.</p>',
    '<p class="mod-sub">Portfolio work &middot; Diagnose the strategic failure &middot; Defuse the mine before it detonates.</p>')
rep('<p style="font-size:13px;color:rgba(255,255,255,.6);margin-bottom:20px;">Each scenario below describes a real-world strategy that failed. Your task: identify the investigation question that would have exposed the failure, and the ABCV checkpoint it belongs to. Choose carefully &mdash; wrong answers detonate.</p>\n',
    '<p class="u4-lead">Each scenario below describes a real-world strategy that failed. In every one, an Industry Illusion kept leaders from seeing the breakdown. Your task has two parts: find the illusion, then find the ABCV checkpoint where that illusion sits. Choose carefully &mdash; wrong answers detonate.</p>\n' +
    how('Portfolio work &middot; How to complete the game', [
        'Open a mine and read the scenario.',
        '<strong>Find the illusion.</strong> Select the investigation question that the scenario answers. Each question reveals one illusion: Familiarity, Exclusion or Complacency.',
        '<strong>Find where it sits.</strong> Select the ABCV checkpoint that the illusion hid from leaders: Arena, Boundaries, Competition or Value Proposition.',
        'Select Submit Answer. When both are right the mine is defused and the page names the illusion and the checkpoint. A wrong answer detonates: read the hint, then select Try Again.',
        'Defuse all four mines. An illusion can appear in more than one mine.'],
        'Your score and your attempts become part of your Learning Portfolio. They reach your facilitator when you select Submit to Facilitator at the end of the unit.'))
ga = h.index('<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:28px;" id="mineGrid">'); gb = h.index('</div><!-- end mine grid -->')
def mine_html(n, m):
    opts = ''.join('      <option value="%s">Q%d: %s</option>\n' % ('correct' if x['k'] == m['ill'] else 'wrong%d' % (i + 1), i + 1, x['q']) for i, x in enumerate(C.ILLUS))
    return ('<!-- MINE %d -->\n<div class="mine-card" id="mine%d">\n  <div class="mine-label" onclick="toggleMine(this)">&#128163; Mine %d &mdash; %s</div>\n  <div class="mine-body">\n'
            '  <p class="mine-scenario">%s</p>\n  <div class="mine-q">\n    <label>1 &middot; FIND THE ILLUSION: SELECT THE INVESTIGATION QUESTION</label>\n'
            '    <select id="mine%dq" onchange="clearFeedback(%d)">\n      <option value="">-- choose --</option>\n%s    </select>\n'
            '    <label style="margin-top:10px;">2 &middot; FIND WHERE IT SITS: SELECT THE ABCV CHECKPOINT</label>\n'
            '    <select id="mine%dl" onchange="clearFeedback(%d)">\n      <option value="">-- choose --</option>\n      <option value="ARENA">Arena</option>\n      <option value="BOUNDARIES">Boundaries</option>\n'
            '      <option value="COMPETITION">Competition</option>\n      <option value="VALUE PROPOSITION">Value Proposition</option>\n    </select>\n'
            '    <button class="btn" style="margin-top:12px;font-size:12px;padding:8px 18px;" onclick="checkMine(%d,\'correct\',\'%s\',2)">Submit Answer</button>\n  </div>\n  </div><!-- /mine-body -->\n'
            '  <div id="mine%dfb" class="mine-feedback"></div>\n</div>\n\n' % (n + 1, n, n + 1, m['name'], m['scenario'], n, n, opts, n, n, n, m['cp'], n))
old_grid = h[ga:gb]
assert old_grid.count('class="mine-card"') == 4
h = h[:ga] + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:28px;" id="mineGrid">\n\n' + ''.join(mine_html(n, m) for n, m in enumerate(C.MINES)) + h[gb:]

# ── 6. Script ─────────────────────────────────────────────────────────────────────────────────────
a = h.index('/* ── Integration Zone ── */'); b = h.index('/* ── Mine Game ── */')
assert 'addObjective' in h[a:b] and 'addOwnership' in h[a:b]
h = h[:a] + h[b:]
assert 'addObjective' not in h and 'addOwnership' not in h
SUMMARY = [
    dict(arc='Awareness — What', title='The Four Integrity Checkpoints',
         body='You saw that a well-written OKR can still rest on unnamed conditions. ABCV examines the strategic logic at four checkpoints: Arena (what the customer is ultimately trying to achieve, read at three depths: functional, experiential and consequential), Boundaries (the conditions that could constrain delivery), Competition (who or what else can satisfy the same end game) and Value Proposition (value that is relevant, distinctive and deliverable). At each checkpoint, a Must-Be-True condition makes the underlying assumption explicit, with examples on Key Results from Unit 3.'),
    dict(arc='Intelligence — Why', title='The Industry Illusion',
         body='You saw how industry knowledge becomes a frame, and how three reinforcing traps (Familiarity, Exclusion and Complacency) turn that frame into the boundary of the world leaders examine. In the Industry Illusion game your own decisions showed what an industry frame leads leaders to notice, dismiss and trust. You then applied Arena to the case.'),
    dict(arc='Extrapolating — Where', title='The Executive Hot Zone and Role-Based Blind Spots',
         body='You saw how functional expertise produces selective strategic attention, so each C-suite role tends to under-examine one ABCV checkpoint. The CEO, CMO and CSO often overlook Boundaries; the CFO, CTO and CPO overlook Arena; the COO and CHRO overlook Competition; the CCO overlooks Value Proposition. For each role the checkpoint names the recurring symptom, what the overlooked checkpoint reveals, and the right question that shifts focus from symptom to cause.'),
    dict(arc='Integration — Collective', title='Stress-Testing Your Key Results',
         body='With your group you brought in the Key Results you confirmed in Unit 3 and took each one through the four steps of the worked example: you defined the Arena, set out the Boundaries, mapped the Competition and established the Value Proposition, and at each step you named the condition that must remain true. Your confirmed work feeds your team’s Capstone Blueprint.'),
    dict(arc='Application — In Practice', title='Diagnosing the Breakdown',
         body='In Cause of Death you tested four failed strategies against the Industry Illusion. For each one you found the illusion at work, then the ABCV checkpoint where that illusion sat. When the breakdown is misidentified, the organisation applies the wrong intervention and reinforces the problem.'),
]
m = re.search(r'var SUMMARY=\[.*?\];\n', h, re.S); assert m
h = h[:m.start()] + 'var SUMMARY=' + json.dumps(SUMMARY, ensure_ascii=False) + ';\n' + h[m.end():]
rep('var KEYS=["team_name","exec_name","exec_role","ref1","ref2","ref3","ref4","ref5","mbt_arena","mbt_bound","mbt_comp","mbt_value","syn_themes","syn_disagree","syn_top5","own_internal","own_external","own_timeline"];\n'
    '    KEYS.forEach(function(id){var ta=document.getElementById(id);if(ta&&responses[id]!=null)ta.value=responses[id];});\n',
    'var KEYS=["ref1","ref2","ref4","ref5"];\n'
    '    KEYS.forEach(function(id){var ta=document.getElementById(id);if(ta&&responses[id]!=null)ta.value=responses[id];});\n'
    '    u4Init(responses);\n')
ma = h.index('    const analyses={'); mb_ = h.index('    const wildcards={')
h = h[:ma] + '    const analyses={\n' + ''.join(
    "      %d:'<strong>%s, sitting in %s.</strong> %s'%s\n" % (n, C.illus(m['ill'])['name'], m['cpname'], m['insight'].replace("'", "\\'"), ',' if n < 3 else '') for n, m in enumerate(C.MINES)) + '    };\n' + h[mb_:]
rep("'&#128161; Right checkpoint, wrong question &mdash; review the scenario and try again.'", "'&#128161; Right checkpoint, wrong question &mdash; which illusion kept leaders from seeing it? Read the scenario again.'")
rep("'&#128161; Right question, wrong checkpoint &mdash; which ABCV checkpoint does that question belong to?'", "'&#128161; Right question, wrong checkpoint &mdash; what did that illusion hide from leaders? That is where it sits.'")
U4D = dict(steps=C.STEPS, stepQ=C.STEP_Q, stepMbt=C.STEP_MBT, game={k: C.GAME[k] for k in ('r1_title', 'r1_prompt', 'r1_do', 'sources', 'r2_title', 'r2_prompt', 'r2_q1', 'r2_q2', 'signals', 'r3_title', 'r3_prompt',
                                         'choices', 'reveal', 'insight', 'arena_q', 'arena', 'final')},
           cps=[{k: c[k] for k in ('k', 'cls', 'name', 'tag', 'mbt')} for c in C.CHECKPOINTS],
           reportHtml=C.report_html(), chainHtml=C.chain_html().strip())
rep('/* ── Init ── */\nrenderSummaryP();',
    'var U4D=' + json.dumps(U4D, ensure_ascii=False).replace('</', '<\\/') + ';\n' + read('u4_p.js').strip('\n') + '\n\n/* ── Init ── */\nrenderSummaryP();')

# ── 7. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<div class="mod') >= 5 and h.count('id="mod') == 5
for gone in ('Q4:', 'Meridian', 'team_name', 'exec_role', 'syn_themes', 'own_timeline', 'step1Objectives', 'ownershipRegistry', 'Integration Zone', 'INTEGRATION ZONE'):
    assert gone not in h, 'still present: ' + gone
assert h.count('<script') == h.count('</script>')
closes = h.count('</div>') + h.count('<\\/div>')
assert h.count('<div') == closes, 'div balance %d / %d' % (h.count('<div'), closes)
# ── Participant voice (Carol, 8 October): the participant page speaks to the participant throughout. No facilitator cues
#    ("Ask", "Now ask:", "Say which…"), and the role cards of Section 3 address the reader in the role. Each line must match exactly
#    the number of times given, or the build stops. The facilitator page keeps its own wording.
VOICE = [
    ('<div class="u4-ask"><span>Ask</span>', '<div class="u4-ask"><span>Your question</span>', 4),
    ('<strong>Ask of the Key Result:</strong>', '<strong>Your question for the Key Result:</strong>', 4),
    ('Say which depth the condition rests on.', 'Name the depth your condition rests on.', 1),
    ('Once Arena has been defined, ask:', 'Once you have defined the Arena, test it:', 1),
    ('<p class="u4-mbt-lead">Now ask:</p>', '<p class="u4-mbt-lead">Then test the boundary:</p>', 1),
    ('Now ask: who or what else can enable that?', 'Now the question becomes: who or what else can enable that?', 1),
    ('Once the competitive landscape has been established, ask:', 'Once you have established the competitive landscape, test it:', 1),
    ('<p class="u4-mbt-lead">Finally ask:</p>', '<p class="u4-mbt-lead">Finally, test the value proposition:</p>', 1),
    ('ABCV forces leaders to examine the strategic logic through four checkpoints:', 'ABCV takes you through the strategic logic at four checkpoints:', 1),
    ('can become the boundary of what leaders examine.', 'can become the boundary of what you examine.', 1),
    ('Functional analysis prevents leaders from confusing what the organisation sells with what the customer needs accomplished.',
     'Functional analysis prevents you from confusing what your organisation sells with what the customer needs accomplished.', 1),
    ('because it helps leaders see the result behind the result.', 'because it helps you see the result behind the result.', 1),
    ('If leaders define Arena through their industry, they will probably identify competitors through their industry.',
     'If you define Arena through your industry, you will probably identify competitors through your industry.', 1),
    ('Over time, leaders build a deep understanding of how their industry works', 'Over time, you build a deep understanding of how your industry works', 1),
    ('a frame through which leaders interpret their environment.', 'a frame through which you interpret your environment.', 1),
    ('so familiar that leaders begin to treat it as the boundary', 'so familiar that you begin to treat it as the boundary', 1),
    ('That last one can generate particularly useful executive discussion.', 'Look closely at that last one: it is the boundary your own organisation can change.', 1),
    ('That is an assumption leadership can now monitor.', 'That is an assumption you can now monitor.', 1),
    ('</strong> Say which customer need the Key Result serves', '</strong> Name the customer need the Key Result serves', 1),
    ('</strong> Say what about the Key Result will make customers choose you', '</strong> Name what about the Key Result will make customers choose you', 1),
    ('the boundary of the world leaders examine. In the Industry Illusion game your own decisions showed what an industry frame leads leaders to notice, dismiss and trust.',
     'the boundary of the world you examine. In the Industry Illusion game your own decisions showed what an industry frame leads you to notice, dismiss and trust.', 1),
    # Section 3 · the nine role cards, addressed to the reader in the role
    ('The CEO holds the vision and drives narrative &mdash; but operational friction is rarely in the chief executive&rsquo;s focus until execution stalls significantly.',
     'As CEO, you hold the vision and drive the narrative &mdash; but operational friction is rarely in your focus until execution stalls significantly.', 1),
    ('friction standing between the vision and its delivery.', 'friction standing between your vision and its delivery.', 1),
    ('The CFO tracks whether the model works &mdash; but whether the underlying customer demand is still real and growing is often outside the financial reporting frame.',
     'As CFO, you track whether the model works &mdash; but whether the underlying customer demand is still real and growing often sits outside your financial reporting frame.', 1),
    ('Operational leaders optimise the machine &mdash; but if the machine is serving the wrong arena, efficiency just accelerates the organisation in the wrong direction.',
     'As COO, you optimise the machine &mdash; but if the machine is serving the wrong arena, efficiency just accelerates your organisation in the wrong direction.', 1),
    ('People alignment and engagement are the CHRO&rsquo;s primary focus &mdash;', 'As CHRO, people alignment and engagement are your primary focus &mdash;', 1),
    ('Technical delivery is the CTO&rsquo;s primary accountability &mdash; but whether the solution addresses the customer&rsquo;s actual end-game (functional, emotional, social) is often assumed and left untested.',
     'As CTO, technical delivery is your primary accountability &mdash; but whether the solution addresses the customer&rsquo;s actual end game (functional, experiential, consequential) is often assumed and left untested.', 1),
    ('Does this solution address the functional, emotional, and social outcome the customer is actually pursuing?',
     'Does this solution address the functional, experiential and consequential outcome the customer is actually pursuing?', 1),
    ('The CMO creates demand &mdash; but if the operational infrastructure cannot fulfil that demand,', 'As CMO, you create demand &mdash; but if your operational infrastructure cannot fulfil that demand,', 1),
    ('Revenue growth is the CCO&rsquo;s scorecard &mdash; but growing by winning the wrong business can dilute the organisation&rsquo;s distinctive identity',
     'As CCO, revenue growth is your scorecard &mdash; but growing by winning the wrong business can dilute your organisation&rsquo;s distinctive identity', 1),
    ('Cost reduction and supply chain resilience are the CPO&rsquo;s primary mandate &mdash;', 'As CPO, cost reduction and supply chain resilience are your primary mandate &mdash;', 1),
    ('Strategy clarity is the CSO&rsquo;s domain &mdash;', 'As CSO, strategy clarity is your domain &mdash;', 1),
]
for a, b, n in VOICE:
    assert h.count(a) == n, ('participant voice', h.count(a), a[:70])
    h = h.replace(a, b)
# The four reflection questions carry the marker the Learning Portfolio page looks for (build_collection.js), as in Units 2 and 3. No visible change.
RP = '<p style="font-size:12px;color:rgba(255,255,255,.55);margin-bottom:8px;">'
assert h.count(RP) == 4, h.count(RP)
h = h.replace(RP, '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.55);margin-bottom:8px;">')
assert '.ref-prompt' not in h
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('participant file written:', out, len(h))
