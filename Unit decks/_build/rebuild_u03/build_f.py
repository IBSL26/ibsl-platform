# -*- coding: utf-8 -*-
"""Unit 3 rebuild (October 2026) — facilitator file, from Carol's document "unit 3 Amendments.docx".
Usage: python3 build_f.py <facilitator file as it stood before the rebuild> <new file>
Run it from this folder: it reads u3.css, u3_shared.js and u3_f.js.
Unchanged blocks are cut from the old file byte for byte. Line endings (CRLF) and UTF-8 are kept.
No times anywhere (Carol, Unit 2): the build fails if one is left."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
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
            '  <div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">' + meta + '</span>' + ARR + '</div>\n</div>\n'
            '<div class="acc-b cb">\n' + body.strip('\n') + '\n</div>\n</div>\n')
def guide(label, *paras, **kw):
    return ('<div class="fac-note-full"' + (' style="margin-top:22px;"' if kw.get('top') else '') + '><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — ' + label + '</div>' +
            ''.join(p if p.startswith(('<ul', '<ol', '<p')) else '<p>' + p + '</p>' for p in paras) + '</div>')
def activity(*paras):
    return ('<div class="fac-note-full"><div class="fac-note-full-label">&#128203; PARTICIPANT ACTIVITY</div>' +
            ''.join(p if p.startswith(('<ul', '<ol', '<p')) else '<p>' + p + '</p>' for p in paras) + '</div>')
def move(label, text, style=''):
    return '<div class="fac-note"' + style + '><div class="fac-label">' + label + '</div><p>' + text + '</p></div>'
def slo(a, b):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>' + a + '</li><li>' + b + '</li></ul></div>\n'
def hero(label, title, sub):
    return ('<div class="mod-hero">\n  <div class="mod-hero-label">' + label + '</div>\n  <h2>' + title + '</h2>\n  <p>' + sub + '</p>\n</div>\n')
def nav(back_i, back, fwd_i=None, fwd=None):
    s = '<div class="mod-nav">\n  <button class="btn" onclick="showMod(' + str(back_i) + ')">← ' + back + '</button>\n'
    if fwd: s += '  <button class="btn" onclick="showMod(' + str(fwd_i) + ')">' + fwd + ' →</button>\n'
    return s + '</div>\n'

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + read('u3.css') + h[i:]

# ── 1. Header and Facilitator Guide tab ───────────────────────────────────────────────────────────
rep('This unit guides the leadership team from the Success in Practice narrative into a focused', 'This unit guides the leadership team from Success in Practice into a focused')
rep('<p>Unit 3 converts the Success in Practice narrative into a measurable execution architecture.', '<p>Unit 3 converts Success in Practice into a measurable execution architecture.')
rep('''<p>The six-step synthesis is the core of the unit. It moves executives from functional objectives to enterprise priorities judged on strategic merit.</p>
''', '''<p>The six-step path is the core of the unit. It moves executives from functional objectives to enterprise priorities judged on strategic merit.</p>
<p><strong>How the unit runs:</strong> Teach the whole unit from the deck first, including one learning round of the Strategy Airport game played with the room. Participants then go to the portal, in the session or after it. The six-step exercise in Section 2, the matching exercise in Section 3 and the game in Section 5 are individual work. Section 4 is group work for the Capstone.</p>
''')
rep('Use de-labelling so each proposal is judged on its merit.', 'Use the four-question alignment test so each proposal is judged on its merit.')

# ── 2. Section 1 ──────────────────────────────────────────────────────────────────────────────────
rep('the leadership team must examine current operating reality in relation to the Success in Practice narrative.</p>',
    'the leadership team must examine current operating reality in relation to its Success in Practice.</p>')
rep('and the three-step path from KISS output to OKR.', 'and the six-step path from KISS output to enterprise OKRs.')
rep('the quality of the Integration and Application sessions depends entirely', 'the quality of the Integration and Application sections depends entirely')
rep('"In Unit 2, we built our Strategic Intent and Success in Practice narrative. Today', '"In Unit 2, we built our Strategy Intent Statement and our Success in Practice. Today')
rep('<p><em>Suggested section time: 30–40 minutes across all five sections.</em></p>', '')
# 1.1 — incomplete sentence removed (Carol); the next sentence now names its subject
rep('FACILITATOR GUIDANCE — Section 1</div><p><strong>Directing participants:</strong> Read the central quote aloud', 'FACILITATOR GUIDANCE — Section 1.1</div><p><strong>Directing participants:</strong> Read the central quote aloud')
rep('They will resurface in the KISS exercise.</p>', 'They will resurface when the groups build their KISS map in Section 4.</p>')
rep('''<p><em>Suggested time: 5–7 minutes.</em></p></div>, the leadership team has produced a Strategy Intent statement and Success in Practice (SiP) narrative. These describe what, why, how, and when the organisation will deliver its value to stakeholders — and what success looks like in practice.</p>
  <p>They provide a vivid and shared description''', '''</div>
  <p>The Strategy Intent Statement and the four Success in Practice (SiP) statements provide a vivid and shared description''')
rep('must first examine its current operating reality in relation to the SiP statement.</p>', 'must first examine its current operating reality in relation to the SiP.</p>')
# 1.2
rep('FACILITATOR GUIDANCE — Section 2</div><p><strong>Directing through the four sub-accordions:</strong> Expand KEEP, IMPROVE, START, and STOP one at a time.',
    'FACILITATOR GUIDANCE — Section 1.2</div><p><strong>Teaching the four filters:</strong> Take KEEP, IMPROVE, START, and STOP one at a time.')
rep('Draw attention to the existing Facilitator Move note in this section — the difference between "improve communication" and "improve cross-functional handover time from 72 to 24 hours." Reinforce this standard before the Application section exercise begins.',
    'Use the Facilitator Move below as the standard: "improve cross-functional handover time from 72 to 24 hours" is specific enough to act on. Reinforce this standard before the group work in Section 4.')
rep('Let it run.</p><p><em>Suggested time: 8–10 minutes.</em></p></div>', 'Let it run.</p></div>')
rep('The SiP statement is passed through a simple but powerful filter called KISS', 'The SiP statements are passed through a simple but powerful filter called KISS')
rep('in relation to the future state described in the SiP narrative:</p>', 'in relation to the future state described in the SiP:</p>')
rep('Every KISS reflection must be anchored to the Success in Practice statement.', 'Every KISS reflection must be anchored to the Success in Practice statements.')
# 1.3
rep('1.3 — The KISS Reflection Table: Four Future-Reality Domains', '1.3 — The KISS Reflection Table: Four SiP Domains')
rep('FACILITATOR GUIDANCE — Section 3</div><p><strong>Directing through the domains:</strong> Walk through each domain (Customer Experience, Operational Capability, People &amp; Culture, Financial Performance)',
    'FACILITATOR GUIDANCE — Section 1.3</div><p><strong>Teaching the domains:</strong> Walk through each domain (Customer Experience &amp; Value, Operational Capability &amp; Execution Rhythm, People &amp; Culture Dynamics, Enterprise Value Creation)')
rep('This is the preparation for the Application section KISS exercise. Participants need to understand all four domains and their anchor questions before they begin writing. Rushing here creates superficial responses in the exercise.',
    'This is the preparation for the KISS map the groups build in Section 4. Participants need to understand all four domains and their anchor questions before they begin writing. Rushing here creates superficial responses in the group work.')
rep('Keeping them separate prevents the vague cross-functional generalisations that make KISS useless.</p><p><em>Suggested time: 6–8 minutes.</em></p></div>',
    'Keeping them separate prevents the vague cross-functional generalisations that make KISS useless.</p></div>')
rep('The KISS reflection is structured across the four future-reality dimensions of the Success in Practice statement.', 'The KISS reflection is structured across the four SiP domains.')
# 1.4
rep('FACILITATOR GUIDANCE — Section 4</div><p><strong>Directing through the OKR anatomy:</strong> Walk through the two panels (Objectives and Key Results) side by side.',
    'FACILITATOR GUIDANCE — Section 1.4</div><p><strong>Teaching the OKR anatomy:</strong> Present Objectives and Key Results side by side.')
rep('Expand the sub-accordion and walk through all four elements with participants.', 'Walk through all four elements with participants.')
rep('Draw specific attention to the red box — outcomes versus activities.', 'Land the Critical Distinction: outcomes versus activities.')
rep('Reinforce it every time a task-disguised-as-KR appears in the session.</p><p><em>Suggested time: 8–10 minutes.</em></p></div>', 'Reinforce it every time a task-disguised-as-KR appears in the session.</p></div>')
rep('Example: Increase digital transaction completion rate from 40% to 75% by Q4 2026.</p>', 'Example: Increase digital transaction completion rate from 40% to 75% of total transactions by Q4 2026.</p>')

# 1.5 — the six steps (Carol: align 1.5 with 4.1; "Enterprise Priority")
STEP_NAMES = ['Find Themes', 'Inspiring Objectives', 'Define Key Results', 'Alignment Test', 'Enterprise Priority', 'Priority Matrix']
def step_tabs(prefix):
    return ('  <div class="step-tabs" id="' + prefix + 'Tabs">\n' + ''.join(
        '    <div class="step-tab' + (' active' if i == 0 else '') + '" onclick="u3Tab(\'' + prefix + '\',' + str(i) + ')"><div class="step-num">Step ' + str(i + 1) + '</div><div class="step-name">' + n + '</div></div>\n'
        for i, n in enumerate(STEP_NAMES)) + '  </div>\n')
G15 = guide('Section 1.5',
    '<strong>Teaching the six steps:</strong> Take the steps in order. Each step builds on the one before it and prepares the next. For each step, read the guiding question aloud and ask participants to apply it mentally to their own area.',
    '<strong>Step 1 — Find Themes:</strong> Ask — <em>"When you review the KISS reflections across all four domains, what is the pattern? What themes keep appearing?"</em> Themes are the connective tissue between scattered KISS observations and purposeful OKRs.',
    '<strong>Step 2 — Inspiring Objectives:</strong> Reference the "T-shirt test" — if the Objective cannot survive a hallway conversation, it is too complex. Ask participants to try stating an Objective in one sentence before writing it.',
    '<strong>Step 3 — Define Key Results:</strong> Apply the four-part formula rigorously. The example in the content (shift response time from 12 to 4 hours by Q3) is a useful benchmark. Hold each KR to the same standard.',
    '<strong>Step 4 — Alignment Test:</strong> Read the four questions aloud. They show whether an OKR is enterprise-level or functionally disguised.',
    '<strong>Step 5 — Enterprise Priority:</strong> Present the Less is More Rule — maximum 4 Enterprise Objectives, maximum 3 Key Results per Objective. This constraint is non-negotiable. The discomfort of trade-offs is the work.',
    '<strong>Step 6 — Priority Matrix:</strong> Walk through the matrix structure and its nine positions. The debate about what constitutes high impact versus high effort is often more valuable than the final placements.',
    '<strong>Closing Awareness:</strong> Before moving to Intelligence, summarise — <em>"We now have the full toolkit: KISS as the honest diagnostic, OKR anatomy as the building structure, and the six-step path to connect them. The next two sections explain why this sequence matters and where it typically fails."</em>')
SIX = '  ' + G15 + '\n' + step_tabs('six') + '''  <div id="six_0" class="step-panel active">
    <h5 class="u3-gq">Guiding Question: What insights emerged from the SiP and KISS reflections?</h5>
    <p>Each leader reviews their KISS reflection. What are the 2–3 big shifts that will contribute to moving the whole organisation forward? The real question is: <em>"If the organisation is going to reach the future it has described, what is the one thing my area can change that would make the biggest difference for everyone?"</em></p>
    <p>Review the patterns that surfaced across the four SiP domains. Identify the strategic themes that repeatedly appeared in the KEEP, IMPROVE, START, and STOP reflections. These themes represent the most important shifts required to move the organisation toward the SiP.</p>
    <div class="u3-outp"><p><strong>Output produced:</strong> A small set of strategic themes that reflect the organisation's priority execution shifts.</p></div>
  </div>
  <div id="six_1" class="step-panel">
    <h5 class="u3-gq">Guiding Question: If we get this theme right, what will we be known for?</h5>
    <p>Each leader gives their themes a voice. Translate each theme into a bold, qualitative statement that expresses strategic ambition. Start with a verb and describe the desired transformation. An Objective should look like a transformation. The real question: <em>"If the organisation actually pulls this off, what will customers and competitors say it is known for?"</em></p>
    <ul>
      <li>Make it <strong>ambitious</strong> — stretch the team.</li>
      <li>Keep it <strong>qualitative</strong> — describe the destination.</li>
      <li>Keep it <strong>memorable</strong> — if you cannot say it in a hallway conversation, it is too complex.</li>
    </ul>
    <div class="u3-outp"><p><strong>Output produced:</strong> A clear Objective that expresses the strategic ambition.</p></div>
    ''' + move('Facilitator Move', 'After each Objective is proposed, ask the room: "Is this statement something we could announce publicly with pride?" If the answer is no — it lacks ambition or clarity. Objectives that describe activities ("Implement new CRM") are tasks disguised as goals.', ' style="margin-top:14px;"') + '''
  </div>
  <div id="six_2" class="step-panel">
    <h5 class="u3-gq">Guiding Question: What measurable outcomes will prove the Objective is being achieved?</h5>
    <p>For every Objective, identify 2–3 measurable results that demonstrate progress toward it. Each Key Result must describe a meaningful shift in performance and must follow the Key Result formula: <strong>Verb + Metric + From X to Y + Deadline.</strong></p>
    <p><strong>Example:</strong> Shift response time from 12 hours (frustrating) to 4 hours (exceptional) by Q3.</p>
    <div class="quote"><p>Quick check: If the team can simply "check it off" a list, it is a task. Key Results describe outcomes — the actual change in the world that proves the Objective is being achieved.</p></div>
    <div class="u3-outp"><p><strong>Output produced:</strong> Measurable Key Results that define progress toward the Objective.</p></div>
  </div>
  <div id="six_3" class="step-panel">
    <p>Before sharing, every leader tests their OKR against four questions:</p>
    <ul>
      <li>Does this truly get the organisation closer to the shared SiP vision?</li>
      <li>Would fellow leaders see this as a win for the whole organisation — or just for one function?</li>
      <li>Does it visibly improve culture, operations, or value creation?</li>
      <li>Is there clear accountability for delivering this outcome?</li>
    </ul>
  </div>
  <div id="six_4" class="step-panel">
    <p>Once initial OKRs have been drafted, the leadership team determines which Objectives deserve enterprise focus now. Strategy execution fails when too many priorities are pursued simultaneously.</p>
    <p>Each team member reviews the proposed Objectives and votes on which represent the most critical strategic movements at this moment.</p>
    <div class="hbox"><p><strong>The Less is More Rule:</strong> No more than <strong>4 Enterprise Objectives</strong>. No more than <strong>3 Key Results per Objective</strong>. This constraint forces explicit trade-offs and concentrates execution energy on what matters most.</p></div>
  </div>
  <div id="six_5" class="step-panel">
    <p>The Prioritisation Matrix evaluates each initiative against two dimensions: <strong>Impact</strong> — the degree of strategic value delivered if achieved — and <strong>Effort</strong> — the time, resources, coordination, and organisational change required. This structured approach helps distinguish initiatives that accelerate strategic movement from those that consume resources without meaningful progress.</p>
    <div id="pmGuideList"></div>
    <p>The leadership team must pay particular attention to initiatives in <strong>Strategic Catalysts</strong>, <strong>Accelerated Enablers</strong>, and <strong>Core Strategic Drivers</strong> — these represent the highest leverage execution signals.</p>
  </div>
'''
a = h.index('<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">1.5 — Three Steps: From KISS Output to OKRs</span>')
b = h.index('<div class="mod-nav"><button class="btn" onclick="showMod(0)">← Facilitator Guide</button>')
h = h[:a] + acc('1.5 — Six Steps: From KISS Output to Enterprise OKRs', '6 Steps · Click each to explore', SIX) + '\n' + h[b:]

# ── 3. Sections 2 to 5, rebuilt ───────────────────────────────────────────────────────────────────
CARD3 = lambda t, p: ('    <div style="background:#151c15;border-radius:3px;padding:16px;border-top:2px solid rgba(231,76,60,.5);">\n'
                      '      <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(231,100,80,.8);margin-bottom:8px;">' + t + '</div>\n'
                      '      <p style="font-size:12px;color:rgba(255,255,255,.55);line-height:1.65;margin:0;">' + p + '</p>\n    </div>\n')
SEQ = lambda border, colour, t, p: ('    <div style="background:#0f1f12;border:1px solid ' + border + ';border-radius:3px;padding:16px;">\n'
                                    '      <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:' + colour + ';margin-bottom:8px;">' + t + '</div>\n'
                                    '      <p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.65;margin:0;">' + p + '</p>\n    </div>\n')
S21 = ('  ' + guide('Section 2.1',
        '<strong>Directing participants:</strong> After presenting the three problems (Disconnected Targets, Fragmented Efforts, The Activity Trap), ask: <em>"Which of these three describes your organisation\'s most recent goal-setting cycle most accurately?"</em> Take a show of hands or quick responses. The near-universal recognition of at least one pattern is itself the lesson.',
        '<strong>The closing line:</strong> Read it aloud — <em>"The organisation starts measuring the finish line before it has mapped the terrain."</em> Ask: <em>"What does \'mapping the terrain\' mean practically — and what does KISS give us that we don\'t currently have?"</em>') + '''
  <p>The usual cause of OKR frustration: organisations try to measure progress before they have had an honest conversation about where they are actually standing.</p>
  <p>When leadership moves straight from a big vision to hard targets, they unintentionally skip the reality check. This creates predictable human problems:</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0;">
''' + CARD3('Disconnected Targets', 'People are asked to hit numbers without anyone acknowledging the hurdles that make those numbers nearly impossible.')
    + CARD3('Fragmented Efforts', 'Different functions row in different directions because they have not agreed on what success looks like in the trenches.')
    + CARD3('The Activity Trap', 'People default to measuring busyness because they are not sure how to prove they are achieving real outcomes.') + '''  </div>
  <div class="hbox red"><p>Essentially, the organisation starts measuring the finish line before it has mapped the terrain.</p></div>
''')
S22 = ('  ' + guide('Section 2.2',
        '<strong>Teaching the three-stage sequence:</strong> Present Success in Practice, KISS and OKRs one at a time. For each, ask participants to briefly state what stage they are at in their current strategic cycle. This creates a live diagnostic of where the group\'s execution journey currently sits.',
        '<strong>The worked example:</strong> Take the example in order: the SiP statement, the KISS table, then the six steps. Each step uses what the step before it produced. At Step 2 say — <em>"Notice how the KISS item maps directly to the Objective. There is no gap. The Objective is the direct consequence of what the KISS reflection surfaced."</em> After Step 6 ask — <em>"At this level of specificity, could you trace every OKR back to a specific KISS observation? That is the standard we are working toward."</em>',
        '<strong>Step 5 in the worked example:</strong> Show how the decision flows from Step 4. Five OKRs passed the alignment test and the Less is More Rule allows four, so the leadership team votes and one Objective is released. Ask — <em>"Which Objective would you have released, and what would that decision cost?"</em> The trade-off stated in the example is the model: the team names what it releases and why.',
        '<strong>The Facilitator Insight:</strong> Use the question in the Facilitator Insight below — <em>"At which point in this sequence does our organisation typically enter?"</em> — as a group discussion prompt. The honest answer often unlocks the most candid conversation of the unit.',
        '<strong>Closing Intelligence:</strong> Transition to Extrapolating by saying — <em>"Now we know why the sequence matters. The next section maps where it most commonly breaks down — and which leadership role is most responsible for each break point."</em>') + '''
  <p>Once these patterns are visible, strategy stops being a deck of slides and starts being a shared journey. The Strategy2Results® sequence makes the path forward clear and respectful of the people walking it:</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0;">
''' + SEQ('rgba(107,143,204,.2)', '#8ab0e8', 'Success in Practice', 'The dream of where the organisation wants to be. The vivid future state across the four SiP domains.')
    + SEQ('rgba(201,168,76,.2)', 'var(--gold)', 'KISS', 'The honest look at the changes required to get there. The bridge between the future and the present reality.')
    + SEQ('rgba(46,168,122,.2)', '#5ecba1', 'OKRs', 'The manageable, measurable steps taken to prove the organisation is moving. The execution compass.') + '''  </div>
  <div class="hbox green"><p>When this sequence is respected, OKRs become a way for the organisation to learn, breathe, and align. Strategy transforms from a statement of intent into a living system that actually helps people succeed.</p></div>
  <h4>Worked Example: One SiP Statement Through the Sequence</h4>
  <p>The example follows one simple SiP statement through the whole sequence: first through the KISS filters, then through the six steps of 1.5. Each step takes its input from the step before it.</p>
  ''' + activity('<strong>Instructions for the 2.2 exercise.</strong> Participants receive the same SiP statement and KISS table in 2.2 of their own file and take the case through the six steps themselves, as individual work, after the teaching. Each step shows what the participant recorded in the steps before it:',
                 '<ol>'
                 '<li><strong>Step 1 — Find Themes:</strong> the participant reads across the KISS table and records at least three themes and up to six.</li>'
                 '<li><strong>Step 2 — Inspiring Objectives:</strong> each theme from Step 1 is shown. The participant writes one Objective under each theme.</li>'
                 '<li><strong>Step 3 — Define Key Results:</strong> each theme is shown with its Objective. The participant writes two or three Key Results under each Objective and names the contributing roles for each Key Result.</li>'
                 '<li><strong>Step 4 — Alignment Test:</strong> each OKR is shown in full: the theme, the Objective and its Key Results. The participant ticks each of the four questions answered with a clear yes. An Objective needs two Key Results before it is tested, and all four ticks to go forward.</li>'
                 '<li><strong>Step 5 — Enterprise Priority:</strong> the OKRs that passed Step 4 are shown in full. The participant selects no more than four as enterprise priorities and states the trade-off: which Objective was released or held back, and why.</li>'
                 '<li><strong>Step 6 — Priority Matrix:</strong> each selected priority is shown in full. The participant sets its Impact and its Effort.</li>'
                 '</ol>',
                 '<strong>The six-step record:</strong> above the steps the participant\'s record builds from Step 1, theme by theme. It is saved on the page and can be printed. The participant then marks the exercise complete. The page asks for at least three themes with an Objective, one to four enterprise priorities, two Key Results in the formula with contributing roles and a matrix position for each priority, and the trade-off where an Objective was left out.',
                 'Each participant\'s exercise reaches you with their submission. The worked answers below are in this file only. A participant\'s themes and Objectives may differ from the worked example and still be sound, provided each one can be traced to the KISS table, each Key Result follows the formula, and no more than four enterprise priorities are selected.') + '''
  <div id="caseF"></div>
  <div id="workedF"></div>
  ''' + move('Facilitator Insight', 'Ask the leadership team to pause and reflect: "At which point in this sequence does our organisation typically enter? Do we skip the KISS reality check and jump straight to targets?" The honest answer often unlocks the conversation about why previous goal-setting cycles felt frustrating.') + '\n')
SEC2 = ('<!-- ══════════════════════════════════════════════ TAB 2: INTELLIGENCE ══ -->\n<div class="mod-panel" id="mod2">\n' +
        hero('Section 2 · Intelligence — Why', 'Why the KISS-to-OKR Sequence Matters',
             'Ignition Point · Most OKR failures are reflection failures. The KISS-OKR transition provides the missing bridge between strategic intent and measurable execution.') +
        '<div class="mod-body">\n' +
        slo('Recognise the benefits of mapping the terrain before setting goals.', 'Practise the translation of SiP into OKRs.') + '\n' +
        guide('Section 2 · Intelligence',
              '<strong>Section intent:</strong> This section answers the question participants are quietly asking: why can\'t we just write the OKRs directly? The answer — because OKRs without KISS become disconnected targets, fragmented efforts, and activity traps — must land personally. This section should prompt candid recognition.',
              '<strong>Framing before entering content:</strong> Ask — <em>"Has your organisation ever set goals that felt disconnected from the reality of what was actually happening on the ground? Where Key Results became a to-do list that nobody believed in?"</em> Use the responses to anchor why the sequence matters before content begins.', top=True) + '\n\n' +
        move('Facilitator Frame', 'Open this section by asking the leadership team: "Has your organisation ever set goals that felt disconnected from reality — or where Key Results became to-do lists?" Use their answers to anchor why this sequence matters before moving into content.') + '\n\n' +
        acc('2.1 — The Danger of Moving Too Fast', '3 Human Problems', S21, True) + '\n' +
        acc('2.2 — Turning Intent into Action: The Strategy2Results® Sequence', 'Case · 6 Steps', S22) + '\n' +
        nav(1, 'Section 1 — Awareness', 3, 'Section 3 — Extrapolating') + '</div>\n</div>\n\n')

S31 = ('  ' + guide('Section 3.1',
        '<strong>Teaching the natural emphasis:</strong> Read the four functional tendencies aloud (commercial, operational, people, financial). Ask each participant to privately identify which category their natural OKR emphasis falls into. Then ask 3–4 to share.',
        '<strong>Key point to reinforce:</strong> Each perspective is valid — the problem arises when these perspectives remain unexamined and unchallenged. The purpose of this part is to make the invisible visible before OKR writing begins, so that the group can consciously compensate.',
        '<strong>The four execution risks:</strong> Read each risk aloud and ask for a show of hands — <em>"Have you personally experienced this in a previous goal-setting cycle?"</em> The near-universal recognition creates the psychological readiness to work differently in the Integration section.',
        '<strong>The hot zone cards:</strong> Teach the pattern with two or three roles: the dominant future realities, the natural OKR emphasis, the typical hot zone and the alignment question. Leave the other roles for the matching exercise, which participants complete in their own file after the teaching.',
        '<strong>Group debrief:</strong> Ask — <em>"If all ten of these hot zones operated simultaneously in our OKR work — what would our final OKR landscape look like? Which domains would be over-represented, and which would be left out?"</em>',
        '<strong>The alignment question:</strong> Tell participants — <em>"Hold your alignment question in your mind throughout the group work in Section 4. It is your personal quality check on every OKR you propose."</em>',
        '<strong>The shift to name explicitly:</strong> Ask — <em>"What is the difference between a functional interpretation of success and a collective definition of success? What does that difference look like in a room full of leaders with different mandates?"</em> This is the conversation the Integration section is designed to produce.',
        '<strong>Closing Extrapolating:</strong> Before moving to Integration, tell participants — <em>"We now know what biases we each bring into the room. The Integration section is where we use that awareness to build something none of us could build alone."</em>') + '''
  <p>Every leadership role tends to emphasise some of the four SiP domains more strongly than others — because each role carries responsibility for specific organisational outcomes, leaders instinctively prioritise the realities that sit closest to their domain.</p>
  <p>This creates a natural imbalance in how OKRs are proposed and evaluated:</p>
  <ul>
    <li><strong>Commercial leaders</strong> emphasise Customer Experience &amp; Value and Enterprise Value Creation</li>
    <li><strong>Operational leaders</strong> emphasise Operational Capability &amp; Execution Rhythm and Enterprise Value Creation</li>
    <li><strong>People leaders</strong> emphasise People &amp; Culture Dynamics and Operational Capability &amp; Execution Rhythm</li>
    <li><strong>Financial leaders</strong> emphasise Enterprise Value Creation and Operational Capability &amp; Execution Rhythm</li>
  </ul>
  <p>Each perspective reflects an important dimension of strategy execution. When these perspectives remain unexamined, OKRs gradually drift into functional scorecards and the organisation accumulates <strong>functional OKRs</strong> where <strong>enterprise OKRs</strong> are needed. This produces four execution risks:</p>
  <ul>
    <li>Competing definitions of success across functions</li>
    <li>Fragmented measurement systems that cannot be integrated</li>
    <li>Functional optimisation that stalls enterprise progress</li>
    <li>Slow decision-making due to misaligned incentives</li>
  </ul>
  <p>Each leadership role therefore has a <strong>typical hot zone</strong>: the point where its natural emphasis distorts the OKRs it proposes. Each role also has an <strong>alignment question</strong> that challenges it toward enterprise thinking.</p>
  <p>When the leadership team names its natural biases explicitly, the conversation shifts from <em>functional interpretation of success</em> to <em>collective definition of success</em>.</p>
  <div class="quote"><p>Recognising these patterns allows the leadership team to integrate perspectives into a balanced execution system that reflects the full enterprise.</p></div>
  <h4>Exercise: Match the Hot Zone and the Alignment Question to Each Role</h4>
  ''' + activity('Participants complete the matching exercise in 3.1 of their own file, as individual work, after the teaching. For each of the ten leadership roles the Dominant Future Realities and the Natural OKR Emphasis are suggested. The participant selects the Typical Hot Zone and the Alignment Question that belong to the role; the page shows a green light for a match and a red alert for a choice that belongs to another role. They then write their Section 3 reflection.',
                 'Each participant\'s matches, with the number of attempts, and the reflection reach you with their submission. The ten complete cards below are your answer key.') + '''
  <p>Select each role to see its dominant future realities, natural OKR emphasis, typical hot zone, and alignment question.</p>
  <div class="hz-grid" id="hzGrid"></div>
  <div class="hz-detail" id="hzDetail"></div>
  ''' + move('Facilitator Move', 'After each leader describes their OKR perspective, ask the room: "Which hot zone does this perspective risk creating?" Name the imbalance explicitly. This builds collective intelligence by surfacing what each function cannot see about itself.', ' style="margin-top:14px;"') + '\n')
SEC3 = ('<!-- ══════════════════════════════════════════════ TAB 3: EXTRAPOLATING ══ -->\n<div class="mod-panel" id="mod3">\n' +
        hero('Section 3 · Extrapolating — Where', 'Where do OKR Hot Zones Appear?',
             'The Alignment Brigade · Where do OKR hot zones appear across leadership functions? Where does functional bias create enterprise fragility?') +
        '<div class="mod-body">\n' +
        slo('Recognise how each leadership function&rsquo;s emphasis shapes the priorities it proposes.', 'Distinguish functional contributions from the enterprise priorities they serve.') + '\n' +
        guide('Section 3 · Extrapolating',
              '<strong>Section intent:</strong> This section does for OKR definition what Unit 2\'s Extrapolating section did for the SiP — it maps where the process predictably breaks down, and who is responsible for each break. The Hot Zone cards are the diagnostic instrument. The goal is to make the systemic pattern visible before it plays out in the room.',
              '<strong>Framing before entering content:</strong> Ask — <em>"Before we start writing OKRs together, it helps to know the natural biases each of us brings to the table. This section maps those patterns so the team can compensate for them collectively."</em>', top=True) + '\n\n' +
        move('Facilitator Frame', 'This section surfaces the natural biases each leader brings to OKR definition. Use the hot zone cards to name these tendencies explicitly and reveal the systemic pattern. Ask: "Which of these descriptions resonates most with how you instinctively write Key Results?"') + '\n\n' +
        acc('3.1 — Natural OKR Emphasis Across Leadership Functions', '10 Roles · Matching Exercise', S31, True) + '\n' +
        nav(2, 'Section 2 — Intelligence', 4, 'Section 4 — Integration') + '</div>\n</div>\n\n')

S41 = ('  ' + guide('Section 4.1',
        '<strong>Before the groups begin:</strong> Remind participants — <em>"Every item you enter must be anchored to the SiP. For example: \'we should improve cross-functional handover time from 72 to 24 hours because the SiP describes seamless execution rhythm.\'"</em>',
        '<strong>Individual before collective:</strong> Each member writes their own inputs for a domain first, then the group shares and agrees its entries. This prevents the first speaker from dominating the KISS landscape.',
        '<strong>Selection:</strong> Aim for 3–4 items per KISS element per domain. More than 5 items per element means the group has not prioritised — push for selection.',
        '<strong>After all four domains are captured:</strong> Ask the group — <em>"Look across all four domains. What are the 2–3 patterns that keep appearing? What does the organisation most consistently need to START, STOP, or IMPROVE relative to the SiP?"</em> These patterns become the strategic themes of 4.2.') + '\n  ' +
       activity('In 4.1 of the participant file the group\'s four SiP statements from Unit 2 appear at the top, brought in from each member\'s Unit 2 page. For each SiP domain the group answers the four KISS guiding questions of 1.3 (Keep, Improve, Start, Stop): sixteen entries in all. The group then confirms its KISS map.',
                'The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page of the participant file, in the session or after it. The confirmed Keep, Improve, Start and Stop feed the team\'s Capstone Blueprint.') + '''
  <p>The groups pass each of their four SiP statements through the four KISS filters and record what the organisation must <strong>keep, improve, start and stop</strong> to reach it. The form follows the four SiP domains and the guiding questions of 1.3:</p>
  <div id="kissPrepList"></div>
  ''' + move('Facilitator Move', 'When leaders generate KISS items, insist on specificity. "Improve cross-functional handover time from 72 hours to 24 hours" is a KISS reflection. Push for the operating reality.', ' style="margin-top:14px;"') + '\n')
S42 = ('  ' + guide('Section 4.2',
        '<strong>Step 1 — Find Themes:</strong> Each leader identifies their 2–3 themes in writing before sharing. Written submissions prevent the anchoring bias where the first speaker dominates the room. Collect all themes before any discussion begins.',
        '<strong>Step 2 — Inspiring Objectives:</strong> After themes are collected, ask participants to draft their Objective privately. The "T-shirt test" applies — if they cannot say it in a hallway conversation, send them back to simplify.',
        '<strong>Step 3 — Define Key Results:</strong> Apply the four-part formula rigorously. The example in 1.5 (shift response time from 12 to 4 hours by Q3) is a useful benchmark. Hold each KR to the same standard.',
        '<strong>Step 4 — Alignment Test:</strong> Run the four-question test publicly. Ask each leader to read their OKR and answer the four questions aloud. The room will quickly surface whether the OKR is enterprise-level or functionally disguised.',
        '<strong>Step 5 — Enterprise Priority:</strong> Enforce the Less is More Rule — maximum 4 Enterprise Objectives, maximum 3 Key Results per Objective. This constraint is non-negotiable. The discomfort of trade-offs is the work.',
        '<strong>Step 6 — Priority Matrix:</strong> Walk through the matrix structure before the group places any items. Establish shared definitions first — <em>"What does \'high impact\' mean for this organisation specifically? What does \'high effort\' mean in our context — time, money, change management, or all three?"</em> The debate about what constitutes high impact versus high effort is often more valuable than the final placements.') + '\n  ' +
       activity('<strong>Instructions for 4.2.</strong> In 4.2 of the participant file the group works through the six steps in order. Each step shows what the steps before it produced, so the group always sees what it is working on:',
                '<ol>'
                '<li><strong>Step 1 — Find Themes:</strong> the group reads its confirmed KISS map and records up to six themes.</li>'
                '<li><strong>Step 2 — Inspiring Objectives:</strong> each theme from Step 1 is shown. The group writes one Objective under each theme.</li>'
                '<li><strong>Step 3 — Define Key Results:</strong> each theme is shown with its Objective. The group writes two or three Key Results under each Objective and names the contributing roles for each Key Result.</li>'
                '<li><strong>Step 4 — Alignment Test:</strong> each OKR is shown in full: the theme, the Objective and its Key Results. The group ticks each of the four questions it answers with a clear yes. An Objective needs two Key Results before it is tested, and all four ticks to go forward.</li>'
                '<li><strong>Step 5 — Enterprise Priority:</strong> the OKRs that passed Step 4 are shown in full. The group selects no more than four as enterprise priorities.</li>'
                '<li><strong>Step 6 — Priority Matrix:</strong> each selected priority is shown in full. The group sets its Impact and its Effort, and the priority takes its position on the matrix.</li>'
                '</ol>',
                '<strong>The six-step record:</strong> above the steps the group\'s record builds from Step 1, theme by theme: the theme, its Objective, its Key Results, the alignment test, the enterprise priority and the matrix position. It is saved on the page. When the six steps are complete the group reads the record, confirms its Enterprise Priorities and its Enterprise OKRs, and prints the record.',
                'The group agrees each entry and one member acts as scribe; every member types the agreed entries into their own page. Both confirmed outputs feed the team\'s Capstone Blueprint.') + '''
  <p>With the KISS map confirmed, each group converts it into enterprise OKRs through the six steps of 1.5:</p>
  <ol>
    <li><strong>Find Themes:</strong> up to six themes drawn from the confirmed KISS map.</li>
    <li><strong>Inspiring Objectives:</strong> one Objective for each theme.</li>
    <li><strong>Define Key Results:</strong> two or three Key Results for each Objective, each in the form Verb + Metric + From X to Y + Deadline, with the contributing roles.</li>
    <li><strong>Alignment Test:</strong> the four questions, answered for each Objective.</li>
    <li><strong>Enterprise Priority:</strong> no more than four Objectives selected for enterprise focus now.</li>
    <li><strong>Priority Matrix:</strong> each enterprise priority placed by Impact and Effort in one of the nine positions.</li>
  </ol>
  ''' + move('Facilitator Move', 'As the team debates placements, listen for disagreements about what constitutes "high impact" versus "high effort." These disagreements are where collective intelligence is built. Do not rush to consensus — the quality of the debate is as valuable as the final placement.', ' style="margin-top:14px;"') + '\n')
SEC4 = ('<!-- ══════════════════════════════════════════════ TAB 4: INTEGRATION ══ -->\n<div class="mod-panel" id="mod4">\n' +
        hero('Section 4 · Integration — Collective', 'Building Collective Intelligence: From SiP to KISS to Enterprise OKRs',
             'Integrator Zone · The groups translate their Success in Practice into a KISS map and then into enterprise OKRs. This is Capstone work: the confirmed outputs feed each team\'s Capstone Blueprint.') +
        '<div class="mod-body">\n' +
        slo('Apply the translation of SiP into OKRs as a group.', 'Gain collective intelligence for the strategic trajectory.') + '\n' +
        guide('Section 4 · Integration',
              '<strong>Section intent:</strong> This is the production section of the unit, and it is Capstone work. Everything in Awareness, Intelligence, and Extrapolating has been preparation for this. Each group translates its Success in Practice into a KISS map (4.1) and then into enterprise OKRs through the six steps (4.2).',
              '<strong>How this section runs:</strong> Explain both steps from the deck. The groups do the work itself on the portal after the teaching, in the session or after it. The guidance in 4.1 and 4.2 is for the moment the groups do the work.',
              '<strong>How the groups work:</strong> The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page of the participant file.',
              '<strong>Into the Capstone:</strong> The Unit 3 section of a team\'s Capstone Blueprint opens once every member of the team has completed this unit. It brings the confirmed outputs in from the member\'s page: Keep, Improve, Start, Stop, Enterprise Priorities and Enterprise OKRs. The team then reads them together and confirms them.', top=True) + '\n\n' +
        move('Facilitator Frame', 'The goal of this section is to find the few, vital Enterprise OKRs that will shift the needle for the entire organisation. Remind the room: Departments contribute the insight — the enterprise owns the results.') + '\n\n' +
        acc('4.1 — Translating SiP to KISS', '4 Domains · Group Work', S41, True) + '\n' +
        acc('4.2 — Translating KISS to OKRs: The Six Steps', '6 Steps · Group Work', S42) + '\n' +
        nav(3, 'Section 3 — Extrapolating', 5, 'Section 5 — Application') + '</div>\n</div>\n\n')

S51 = ('  ' + guide('Section 5.1',
        '<strong>How the game is used:</strong> In the lesson you play one learning round with the room, from this page. After the teaching, each participant plays the same game alone in 5.1 of their own file and submits it with the unit.',
        '<strong>Sharing the game in the lesson:</strong> Open this page in your browser before the lesson. At the game slide, stop sharing the deck and share this browser window. Return to the deck when the learning round is complete.',
        '<strong>Gate 1 · Baggage Check:</strong> Read the SiP statement aloud. Take KEEP, IMPROVE, START and STOP in turn. Let participants choose an option first, then select it: the answer is revealed only after selection. On a red alert ask — <em>"Why does this option fail the SiP?"</em> Collect at least two items for each filter before you proceed.',
        '<strong>Gate 2 · Flight Plan:</strong> Ask the group to pick one theme. Read the draft Objective and the two Key Results aloud and test them with the room — <em>"Is the Objective enterprise-level? Does each Key Result show a metric, a movement from X to Y and a deadline?"</em> Edit the draft with the group\'s corrections, then add the flight plan.',
        '<strong>Learning point to land:</strong> KISS is the evidence base for deciding what the Objective should be and what Key Results will prove progress.') + '\n  ' +
       activity('After the teaching, each participant plays one learning round alone in 5.1 of their own file: at least two items for each KISS filter at Gate 1, then at least one OKR flight plan at Gate 2 (one Objective, two Key Results and the contributing roles).',
                'Each participant\'s KISS choices and flight plans reach you with their submission.') + '''
  <p>Strategy Airport takes a new case, a medical health company, from its Success in Practice statement to KISS insights and then to one OKR flight plan. The game below is for the lesson round. Nothing you enter here is saved.</p>
  <div id="saHostF"></div>
''')
GSUM = guide('Unit Summary',
    '<strong>Closing the unit:</strong> Read each of the five summary blocks aloud, or ask participants to read them in turn. The summary is intentionally concise — it crystallises the arc of the unit without adding new content.',
    '<strong>Return to the opening question:</strong> Go back to the question you asked at the start of Awareness — <em>"If the Success in Practice we described is the future organisation, what must change in the organisation today to make that future possible?"</em> Ask 2–3 participants: <em>"Looking at the OKRs we have just built — have we answered that question? Where are the remaining gaps?"</em>',
    '<strong>Tangible outputs check:</strong> Confirm with the group that the following have been produced or are in progress:',
    '<ul><li>The six-step exercise from each participant (2.2)</li><li>The matching exercise from each participant (3.1)</li><li>A confirmed KISS map from each group (4.1)</li><li>Confirmed Enterprise Priorities and Enterprise OKRs from each group — maximum 4 Objectives, maximum 3 KRs each (4.2)</li><li>A completed Strategy Airport learning round from each participant (5.1)</li></ul>',
    '<strong>Closing commitment:</strong> Ask each participant to complete this sentence privately — <em>"The one thing I am committing to before our next session to make these OKRs real is…"</em> Invite 2–3 to share. These are the accountability anchors between now and Unit 4.',
    '<strong>Transition to Unit 4:</strong> Close with — <em>"We have built our Strategy Intent Statement, described our future state through SiP, and now defined how we will measure our progress through OKRs. Unit 4 tests the integrity of that direction through ABCV — the conditions that must hold true for the journey toward the organisation we have described."</em>')
SEC5 = ('<!-- ══════════════════════════════════════════════ TAB 5: APPLICATION ══ -->\n<div class="mod-panel" id="mod5">\n' +
        hero('Section 5 · Application — In Practice', 'Strategy Airport: From Strategic Imagination to Operational Clearance',
             'The Strategy Airport game · Played with the room in the lesson · Then individual work that each participant submits.') +
        '<div class="mod-body">\n' +
        slo('Reinforce strategy translation capability.', 'Establish individual capability to set a strategic trajectory.') + '\n' +
        guide('Section 5 · Application',
              '<strong>Section intent:</strong> This is the application section. Participants have seen the full path from Success in Practice to KISS to OKRs. Strategy Airport lets them apply it to a case they have not met: first with you in the lesson, then on their own.', top=True) + '\n\n' +
        acc('5.1 — Strategy Airport', '2 Gates · Learning Round', S51, True) + '\n' +
        '<!-- UNIT SUMMARY -->\n' +
        acc('Unit Summary', 'Unit 3 synthesis', '  ' + GSUM + '\n  <div id="summaryList"></div>\n') + '\n' +
        nav(4, 'Section 4 — Integration') + '</div>\n</div>\n\n')
a = h.index('<!-- ══════════════════════════════════════════════ TAB 2: INTELLIGENCE ══ -->')
b = h.index('</div><!-- /main -->')
h = h[:a] + SEC2 + SEC3 + SEC4 + SEC5 + h[b:]

# ── 4. Script ─────────────────────────────────────────────────────────────────────────────────────
a = h.index('// ── DATA ──')
b = h.index('// ── GENERIC HELPERS ──')
h = h[:a] + read('u3_shared.js').strip('\n') + '\n\n' + read('u3_f.js').strip('\n') + '\n\n' + h[b:]
rep('renderKissGuide();renderHotZones();renderPMGuide();renderBiases();\nrenderAppExample();renderSummary();',
    "renderKissGuide();renderHotZones();renderPMCards('pmGuideList');renderCase('caseF');renderWorked('workedF');renderSummary();\nsaInit('saHostF','f',null);")
rep('''function showStep(prefix,i){
  document.querySelectorAll('#'+prefix+'Tabs .step-tab').forEach(function(t,x){t.classList.toggle('active',x===i);});
  document.querySelectorAll('[id^="'+prefix+'_"]').forEach(function(p,x){p.classList.toggle('active',x===i);});
}
''', '')

# ── Section learning outcomes realigned to the rebuilt content (Carol, 7 Oct) ──
rep('<li>Distinguish results that evidence progress from the activities that produce them.</li>', '<li>Translate strategic intent into measurable results.</li>')

# ── 5. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
vis = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>', ' ', h)
t = re.search(r'Suggested\s+(?:section\s+|total\s+section\s+)?time|\b\d+(?:–\d+)?\s*(?:minutes|min)\b', vis)
assert not t, 'a time is left: ' + vis[max(0, t.start() - 80):t.end() + 40]
for gone in ('whiteboard', 'flip chart', 'Assemble Landscape', 'Session Report', 'sub-accordion', 'red box', 'gold note', 'Future-Reality', 'future-reality', 'narrative', 'Strategic Intent', 'Financial Performance',
             'Panoramic', 'Breaking the Biases', '2.3 —', '3.2 —', '3.3 —', 'Task 1', 'Task 2', 'Task 3', 'Portfolio', ', but that enthusiasm'):
    assert gone not in vis, 'still present: ' + gone
assert '</div>, ' not in h and '</div> — ' not in h, 'a sentence still opens in the middle'
assert h.count('<script') == h.count('</script>'), 'script tags do not balance'
assert '<textarea' not in vis and '<input' not in vis, 'entry box on the facilitator page outside the lesson game'
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('facilitator file written:', out, len(h))
