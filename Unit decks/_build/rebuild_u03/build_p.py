# -*- coding: utf-8 -*-
"""Unit 3 rebuild (October 2026) — participant file, from Carol's document "unit 3 Amendments.docx".
Usage: python3 build_p.py <participant file as it stood before the rebuild> <new file>
Run it from this folder: it reads u3.css, u3_shared.js and u3_p.js.
Unchanged blocks are cut from the old file byte for byte. Line endings (CRLF) and UTF-8 are kept."""
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
def cut(start, end):
    """Text from the first `start` up to (not including) the next `end`."""
    a = h.index(start); b = h.index(end, a + len(start)); return a, b

ARR = '<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div>'
def acc(title, meta, body, open_=False, ident=''):
    return ('<div class="acc' + (' open' if open_ else '') + '"' + ident + '><div class="acc-h" onclick="tA(this)"><span class="acc-t">' + title + '</span>'
            '<div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">' + meta + '</span>' + ARR + '</div></div>\n'
            '<div class="acc-b cb">\n' + body.strip('\n') + '\n</div></div>\n')
def ref(rid, prompt, style=''):
    return ('  <div class="ref-block"' + style + '><div class="ref-head"><span class="ref-icon">✦</span><span class="ref-label">&#x270E; Reflection</span></div>\n'
            '  <div class="ref-prompt">' + prompt + '</div>\n'
            '  <textarea class="ref-ta reflection-textarea" id="' + rid + '" placeholder="Your reflection here..."></textarea>\n'
            '  <button class="ref-save" onclick="saveRef(\'' + rid + '\')">Save Reflection</button>\n'
            '  <div class="ref-saved" id="' + rid + '-saved">✓ Saved</div></div>\n')
def slo(a, b):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>' + a + '</li><li>' + b + '</li></ul></div>\n'
def hero(label, title, sub):
    return ('<div class="mod-hero">\n  <div class="mod-hero-label">' + label + '</div>\n  <h2>' + title + '</h2>\n  <p>' + sub + '</p>\n</div>\n')

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + read('u3.css') + h[i:]

# ── 1. Header ─────────────────────────────────────────────────────────────────────────────────────
rep('This unit moves you from the Success in Practice narrative into a focused', 'This unit moves you from your Success in Practice into a focused')

# ── 2. Section 1 ──────────────────────────────────────────────────────────────────────────────────
rep("in relation to the Success in Practice narrative — this is the bridge between strategy and execution.",
    "in relation to its Success in Practice — this is the bridge between strategy and execution.")
# 1.1: Unit 2 wording; the question as on the facilitator page; reflection box removed (Carol)
rep('<p>Your leadership team has produced a Strategy Intent statement and a Success in Practice (SiP) narrative. These describe',
    '<p>Your group has produced a Strategy Intent Statement and four Success in Practice (SiP) statements, one for each SiP domain. These describe')
rep('what must change today to make that future possible?</p></div>', 'what must change in the organisation today to make that future possible?</p></div>')
rep('''  <div class="ref-block"><div class="ref-head"><span class="ref-icon">✦</span><span class="ref-label">&#x270E; Reflection</span></div>
  <div class="ref-prompt">What does your SiP describe that your organisation does not yet consistently deliver? Be specific.</div>
  <textarea class="ref-ta reflection-textarea" id="ref1" placeholder="Your honest reflection here..."></textarea>
  <button class="ref-save" onclick="saveRef('ref1')">Save Reflection</button>
  <div class="ref-saved" id="ref1-saved">✓ Saved</div></div>
''', '')
# 1.2
rep('<p>KISS passes the SiP statement through four reflective filters', '<p>KISS passes the SiP statements through four reflective filters')
for k, sub in (('KEEP', 'Protect what is already working'), ('IMPROVE', 'Strengthen what is partially working'), ('START', 'Introduce what does not yet exist'), ('STOP', 'Eliminate what contradicts the SiP')):
    rep('margin-bottom:8px;">' + k + '</div><p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.65;margin:0;">',
        'margin-bottom:8px;">' + k + ' — ' + sub + '</div><p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.65;margin:0;">')
rep('Every KISS reflection must be anchored to the SiP statement. You are evaluating the organisation against the specific future your leadership team has collectively described.',
    'Every KISS reflection must be anchored to the SiP statements. You are evaluating the organisation against the specific future your group has collectively described.')
# 1.3
rep('1.3 — The KISS Reflection Table: Four Future-Reality Domains', '1.3 — The KISS Reflection Table: Four SiP Domains')
rep('The KISS reflection examines the organisation across the four future-reality dimensions of the SiP.', 'The KISS reflection examines the organisation across the four SiP domains.')
# 1.4: same content as the facilitator page
rep('<p>OKRs translate the changes identified in the KISS reflection into measurable progress.</p>',
    '<p>Objective Key Results (OKRs) translate the changes identified in the KISS reflection into measurable progress.</p>')
rep('<strong>Qualitative · Ambitious · Action-Oriented · Inspirational · Memorable.</strong></p></div>',
    '<strong>Qualitative · Ambitious · Action-Oriented · Inspirational · Memorable.</strong> If you cannot wear it on a T-shirt, it is not worth pursuing.</p></div>')
KR_GUIDE = '''  <div class="sub-acc">
    <div class="sub-acc-h" onclick="tSA(this)"><span>Key Result Construction Guide — 4 Elements</span><span class="sub-arr">▾</span></div>
    <div class="sub-acc-b">
      <div class="u3-kr4">
        <div><div class="u3-kr4-h">Verb of Change</div><p>Indicates the direction of improvement. E.g.: Increase, Reduce, Achieve, Improve, Maintain.</p></div>
        <div><div class="u3-kr4-h">Metric</div><p>A clear and measurable indicator. E.g.: Customer satisfaction score, cycle time, adoption rate.</p></div>
        <div><div class="u3-kr4-h">From X to Y</div><p>Defines the baseline and target. E.g.: From 40% to 75%. Always establish a starting point.</p></div>
        <div><div class="u3-kr4-h">Deadline</div><p>Specifies when the result must be achieved. E.g.: By Q4 2026, By end of FY.</p></div>
      </div>
    </div>
  </div>
'''
rep('  <div class="hbox red"><p><strong>Critical Distinction:</strong> OKRs define outcomes. If a statement can be checked off a to-do list, it is a task. Key Results describe the impact those tasks must produce.</p></div>\n',
    KR_GUIDE + '  <div class="hbox red"><p><strong>Critical Distinction:</strong> OKRs define outcomes. If a statement can be checked off a task list — "launch new platform" or "run customer survey" — it is a task. Those are activities that support the Key Result. Key Results describe the impact those activities must produce.</p></div>\n')

# 1.5: the five steps (Carol, 7 Oct: Step 5 Enterprise Priority removed)
STEP_NAMES = ['Find Themes', 'Inspiring Objectives', 'Define Key Results', 'Alignment Test', 'Priority Matrix']
def step_tabs(prefix):
    return ('  <div class="step-tabs" id="' + prefix + 'Tabs">\n' + ''.join(
        '    <div class="step-tab' + (' active' if i == 0 else '') + '" onclick="u3Tab(\'' + prefix + '\',' + str(i) + ')"><div class="step-num">Step ' + str(i + 1) + '</div><div class="step-name">' + n + '</div></div>\n'
        for i, n in enumerate(STEP_NAMES)) + '  </div>\n')
FIVE = step_tabs('five') + '''  <div id="five_0" class="step-panel active">
    <h5 class="u3-gq">Guiding Question: What insights emerged from the SiP and KISS reflections?</h5>
    <p>Review your KISS reflection and identify the 2–3 big shifts in your area that will contribute to moving the whole organisation forward. Ask: <em>"If the organisation is to reach the future it has described, what is the one thing my area can change that would make the biggest difference for everyone?"</em></p>
    <p>Then review the patterns that surfaced across the four SiP domains. Identify the strategic themes that repeatedly appeared in the KEEP, IMPROVE, START, and STOP reflections. These themes represent the most important shifts required to move the organisation toward the SiP.</p>
    <div class="u3-outp"><p><strong>Output produced:</strong> A small set of strategic themes that reflect the organisation's priority execution shifts.</p></div>
  </div>
  <div id="five_1" class="step-panel">
    <h5 class="u3-gq">Guiding Question: If we get this theme right, what will we be known for?</h5>
    <p>Translate each theme into a bold, qualitative statement that expresses strategic ambition. Start with a verb and describe the desired transformation. An Objective should look like a transformation. Ask: <em>"If the organisation actually pulls this off, what will customers and competitors say it is known for?"</em></p>
    <ul>
      <li>Make it <strong>ambitious</strong> — stretch the team.</li>
      <li>Keep it <strong>qualitative</strong> — describe the destination.</li>
      <li>Keep it <strong>memorable</strong> — if you cannot say it in a hallway conversation, it is too complex.</li>
    </ul>
    <div class="u3-outp"><p><strong>Output produced:</strong> A clear Objective that expresses the strategic ambition.</p></div>
  </div>
  <div id="five_2" class="step-panel">
    <h5 class="u3-gq">Guiding Question: What measurable outcomes will prove the Objective is being achieved?</h5>
    <p>For every Objective, identify 2–3 measurable results that demonstrate progress toward it. Each Key Result must describe a meaningful shift in performance and must follow the Key Result formula: <strong>Verb + Metric + From X to Y + Deadline.</strong></p>
    <p><strong>Example:</strong> Shift response time from 12 hours (frustrating) to 4 hours (exceptional) by Q3.</p>
    <div class="quote"><p>Quick check: If the team can simply "check it off" a list, it is a task. Key Results describe outcomes — the actual change in the world that proves the Objective is being achieved.</p></div>
    <div class="u3-outp"><p><strong>Output produced:</strong> Measurable Key Results that define progress toward the Objective.</p></div>
  </div>
  <div id="five_3" class="step-panel">
    <p>Before sharing your OKR with the group, test it against four questions:</p>
    <ul>
      <li>Does this truly get the organisation closer to the shared SiP vision?</li>
      <li>Would fellow leaders see this as a win for the whole organisation — or just for one function?</li>
      <li>Does it visibly improve culture, operations, or value creation?</li>
      <li>Is there clear accountability for delivering this outcome?</li>
    </ul>
  </div>
  <div id="five_4" class="step-panel">
    <p>The Prioritisation Matrix evaluates each initiative against two dimensions: <strong>Impact</strong> — the degree of strategic value delivered if achieved — and <strong>Effort</strong> — the time, resources, coordination, and organisational change required. This structured approach helps distinguish initiatives that accelerate strategic movement from those that consume resources without meaningful progress.</p>
    <div id="pmGuideP"></div>
    <p>Pay particular attention to initiatives in <strong>Strategic Catalysts</strong>, <strong>Accelerated Enablers</strong>, and <strong>Core Strategic Drivers</strong> — these represent the highest leverage execution signals.</p>
  </div>
'''
a, b = cut('<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">1.5 — Three Steps: From KISS Output to OKRs</span>', '<div class="mod-nav"><button class="btn" onclick="showMod(1)">Section 2 — Intelligence →</button></div>')
h = h[:a] + acc('1.5 — Five Steps: From KISS Output to Enterprise OKRs', '5 Steps · Click each to explore', FIVE) + h[b:]

# ── 3. Section 2: 2.1 kept; 2.2 removed; old 2.3 becomes 2.2 with the worked example of the five steps (read-only on both pages) ──
rep('''People default to measuring busyness because they are unsure how to prove they are achieving real outcomes.</p></div>
  </div>
</div></div>
''', '''People default to measuring busyness because they are unsure how to prove they are achieving real outcomes.</p></div>
  </div>
  <div class="quote"><p>Essentially, the organisation starts measuring the finish line before it has mapped the terrain.</p></div>
</div></div>
''')
a, b = cut('<div class="acc"><div class="acc-h" onclick="tA(this)"><span class="acc-t">2.2 — The KISS Reflection as the Missing Bridge</span>',
           '<div class="acc"><div class="acc-h" onclick="tA(this)"><span class="acc-t">2.3 — Turning Intent into Action')
h = h[:a] + h[b:]
rep('<span class="acc-t">2.3 — Turning Intent into Action: The Strategy2Results® Sequence</span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">3-Part Logic</span>',
    '<span class="acc-t">2.2 — Turning Intent into Action: The Strategy2Results® Sequence</span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">Worked Example</span>')
rep('a vivid future state across four observable dimensions.</p></div>', 'a vivid future state across the four SiP domains.</p></div>')
rep('''Strategy transforms from a statement of intent into a living system.</p></div>
''', '''Strategy transforms from a statement of intent into a living system.</p></div>
  <h4>Worked Example: One SiP Statement Through the Sequence</h4>
  <p>The example below follows one simple SiP statement through the whole sequence: first through the KISS filters, then through the five steps of 1.5. Open each step in turn. Refer to it when your group does its own work in Section 4.</p>
  <div id="caseP"></div>
  <div id="workedP"></div>
''')

# ── 4. Section 3: 3.1, 3.2 and 3.3 fused into one 3.1 with the matching exercise (Carol) ───────────
S3 = '''  <p>Every leadership role tends to emphasise some of the four SiP domains more strongly than others, because each role carries responsibility for specific organisational outcomes. This creates a natural imbalance in how OKRs are proposed and evaluated:</p>
  <ul>
    <li><strong>Commercial leaders</strong> emphasise Customer Experience &amp; Value and Enterprise Value Creation</li>
    <li><strong>Operational leaders</strong> emphasise Operational Capability &amp; Execution Rhythm and Enterprise Value Creation</li>
    <li><strong>People leaders</strong> emphasise People &amp; Culture Dynamics and Operational Capability &amp; Execution Rhythm</li>
    <li><strong>Financial leaders</strong> emphasise Enterprise Value Creation and Operational Capability &amp; Execution Rhythm</li>
  </ul>
  <p>Each perspective is valid. When these perspectives remain unexamined, OKRs gradually drift into functional scorecards and the organisation accumulates <strong>functional OKRs</strong> where <strong>enterprise OKRs</strong> are needed. This produces four execution risks:</p>
  <ul>
    <li>Competing definitions of success across functions</li>
    <li>Fragmented measurement systems that cannot be integrated</li>
    <li>Functional optimisation that stalls enterprise progress</li>
    <li>Slow decision-making due to misaligned incentives</li>
  </ul>
  <p>Each leadership role therefore has a <strong>typical hot zone</strong>: the point where its natural emphasis distorts the OKRs it proposes. Each role also has an <strong>alignment question</strong> that challenges it toward enterprise thinking.</p>
  <p>When your group names its natural biases explicitly, the conversation shifts from <em>functional interpretation of success</em> to <em>collective definition of success</em>.</p>
  <div class="quote"><p>Recognising these patterns allows the leadership team to integrate perspectives into a balanced execution system that reflects the full enterprise.</p></div>
  <h4>Exercise: Match the Hot Zone and the Alignment Question to Each Role</h4>
  <div class="hbox teal u3-how"><p><strong>Portfolio work · How to complete the exercise</strong></p>
    <ol>
      <li>Select a role. Start with the first role and work through all ten.</li>
      <li>Read the two suggested entries for the role: its Dominant Future Realities and its Natural OKR Emphasis.</li>
      <li>Choose the Typical Hot Zone that this emphasis creates. A green light confirms the match. A red alert means the choice belongs to another role: read the emphasis again and choose again.</li>
      <li>Choose the Alignment Question that brings the role back to the enterprise, in the same way.</li>
      <li>Move to the next role. The exercise is complete when ten of ten roles are matched.</li>
    </ol>
    <p>Complete the exercise on your own. Your matches are saved on this page, become part of your Learning Portfolio and reach your facilitator when you submit the unit.</p></div>
  <div id="hzMatchP"></div>
''' + ref('ref4', 'Which hot zone description most accurately reflects how you instinctively approach OKR definition? What would you need to do differently to write an enterprise-level Key Result?', ' style="margin-top:20px;"')
a, b = cut('<div class="acc open"><div class="acc-h" onclick="tA(this)"><span class="acc-t">3.1 — Natural OKR Emphasis Across Leadership Functions</span>',
           '<div class="mod-nav"><button class="btn" onclick="showMod(1)">← Section 2 — Intelligence</button>')
h = h[:a] + acc('3.1 — Natural OKR Emphasis Across Leadership Functions', '10 Roles · Portfolio Work', S3, True) + h[b:]
rep('Every leadership role naturally emphasises certain future realities over others. Recognising your hot zone', 'Every leadership role naturally emphasises certain SiP domains over others. Recognising your hot zone')

# ── 5. Section 4: group work for the Capstone — 4.1 SiP to KISS, 4.2 KISS to OKRs (Carol) ──────────
S4_LEAD = '''<p class="u3-lead">Work with your group through two connected stages. Each output is the foundation for the next: <strong>Success in Practice → KISS → OKRs</strong>.</p>
<div class="hbox teal"><p><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</p></div>
'''
S41 = '''  <p>Your group's four SiP statements describe the future organisation. In this step you pass each statement through the four KISS filters and record what the organisation must <strong>keep, improve, start and stop</strong> to reach it.</p>
  <h4>Your Group's Four SiP Statements</h4>
  <p>The four statements your group confirmed in Unit 2 are brought in from your Unit 2 page. Read each one with your group. Where your team has since refined a statement in the Capstone Blueprint, type the confirmed wording in the box.</p>
  <div id="sipCaptureP"></div>
  <h4>Build Your KISS Map</h4>
  <p>Take one SiP domain at a time. Read the domain's SiP statement, then answer the four guiding questions with your group. Anchor every entry to the statement and be specific: "Improve cross-functional handover time from 72 hours to 24 hours" is a KISS entry.</p>
  <div id="kissFormP"></div>
  <h4>Confirm Your KISS Map</h4>
  <p>When all sixteen boxes are complete, read the map across the four domains as a group and confirm it. Your confirmed KISS map is the source for 4.2.</p>
  <div id="kissConfirmP"></div>
  <div class="hbox"><p><strong>Into your Capstone.</strong> Your confirmed Keep, Improve, Start and Stop feed your team's Capstone Blueprint. Its Unit 3 section opens once every member of your team has completed this unit, and brings your confirmed outputs in from your page. Your team then reads them together and confirms them.</p></div>
'''
S42 = '''  <p>With your KISS map confirmed, your group converts it into enterprise OKRs through the five steps of 1.5. Work through the steps in order. Each step shows what your group recorded in the steps before it: the themes of Step 1 become Objectives in Step 2, each Objective receives its Key Results and contributing roles in Step 3, each OKR is tested in Step 4, and the aligned OKRs are placed on the Prioritisation Matrix in Step 5.</p>
  <h4>Your Five-Step Record</h4>
  <p>Everything your group records in the five steps below builds up here from Step 1, theme by theme, and is saved on this page.</p>
  <div id="okrRecP"></div>
  <h4>The Five Steps</h4>
  <div id="okrToolP"></div>
  <h4>Confirm and Print</h4>
  <p>When the five steps are complete, read your five-step record together, confirm your Enterprise Priorities and Enterprise OKRs, then print the record.</p>
  <div id="okrOutP"></div>
  <div class="hbox"><p><strong>Into your Capstone.</strong> Your confirmed Enterprise Priorities and Enterprise OKRs feed your team's Capstone Blueprint, together with your KISS map.</p></div>
'''
SEC4 = ('<!-- TAB 4: INTEGRATION -->\n<div class="mod-panel" id="mod3">\n' +
        hero('Section 4 · Integration — Collective', 'Building Collective Intelligence: From SiP to KISS to Enterprise OKRs',
             'Integrator Zone · With your group you translate your Success in Practice into a KISS map and then into enterprise OKRs. This is Capstone work: your confirmed outputs feed your team\'s Capstone Blueprint.') +
        '<div class="mod-body">\n' +
        slo('Apply the translation of SiP into OKRs as a group.', 'Gain collective intelligence for the strategic trajectory.') +
        S4_LEAD +
        acc('4.1 — Translating SiP to KISS', '4 Domains · Group Work', S41, True) + '\n' +
        acc('4.2 — Translating KISS to OKRs: The Five Steps', '5 Steps · Group Work', S42) +
        '<div class="mod-nav"><button class="btn" onclick="showMod(2)">← Section 3 — Extrapolating</button><button class="btn" onclick="showMod(4)">Section 5 — Application →</button></div>\n</div></div>\n')

# ── 6. Section 5: the Strategy Airport game, portfolio work (Carol, 7 Oct) ─────────────────────────
S51 = '''  <p>You have built your group's KISS map and enterprise OKRs. Strategy Airport lets you practise the same translation on your own with a new case: a medical health company.</p>
  <p>Clear two gates. At <strong>Gate 1 · Baggage Check</strong> you decide what the company must keep, improve, start and stop. At <strong>Gate 2 · Flight Plan</strong> you convert one KISS theme into an Objective and two Key Results.</p>
  <div class="hbox teal u3-how"><p><strong>Portfolio work · How to complete the learning round</strong></p>
    <ol>
      <li>Read the Success in Practice statement of the company.</li>
      <li><strong>Gate 1 · Baggage Check:</strong> for each KISS filter, choose the options that belong to it. A green light confirms a choice. A red alert gives the reason the option fails the SiP. Collect at least two items for each filter.</li>
      <li><strong>Gate 2 · Flight Plan:</strong> choose one KISS theme and convert it into one Objective, two Key Results and the contributing roles. Add the flight plan.</li>
      <li>Finish the learning round.</li>
    </ol>
    <p>Play the learning round on your own. Your KISS choices and your flight plans are saved on this page, become part of your Learning Portfolio and reach your facilitator when you submit the unit.</p></div>
  <div id="saHostP"></div>
'''
SEC5_HEAD = ('<!-- TAB 5: APPLICATION -->\n<div class="mod-panel" id="mod4">\n' +
             hero('Section 5 · Application — In Practice', 'Strategy Airport: From Strategic Imagination to Operational Clearance',
                  'Portfolio work · Play the Strategy Airport game · Move from strategic imagination to operational clearance · Translate a Success in Practice statement into KISS insights and an OKR flight plan.') +
             '<div class="mod-body">\n' +
             slo('Reinforce strategy translation capability.', 'Establish individual capability to set a strategic trajectory.') + '\n' +
             acc('5.1 — Strategy Airport', '2 Gates · Portfolio Work', S51, True) + '\n')
a = h.index('<!-- TAB 4: INTEGRATION -->')
b = h.index('<div class="acc"><div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Summary</span>')
h = h[:a] + SEC4 + SEC5_HEAD + h[b:]

# ── 7. Script: shared data and tools in place of the old data, render and save functions ──────────
a = h.index('var KISS_DOMAINS=[')
b = h.index('// Reflection draft + save — parity with deployed Unit 2.')
h = h[:a] + read('u3_shared.js').strip('\n') + '\n\n' + read('u3_p.js').strip('\n') + '\n\n' + h[b:]
# the Portfolio Artefact is gone, so is its save function
a, b = cut('async function savePort(id){', 'async function sendToFacilitator(){')
h = h[:a] + h[b:]
# load saved answers
a = h.index('window.addEventListener("load",async function(){\n  if(!window.S2R){console.warn(\'[unit2_m1_lens2_p] S2R helper not loaded\');return;}')
b = h.index('document.body.style.overflow="";')
LOAD = '''function u3RenderAll(){
  renderKissGuideP();renderPMCards('pmGuideP');renderCase('caseP');renderWorked('workedP');renderMatch();
  renderSipCapture();renderKissForm();renderOkrTool();renderSummaryP();u3Mirrors();
}
window.addEventListener("load",async function(){
  if(!window.S2R){console.warn('[unit2_m1_lens2_p] S2R helper not loaded');return;}
  try{
    var responses=await S2R.loadAll('u2m1_lens2');
    // Reflections
    ["ref2","ref3","ref4"].forEach(function(id){
      var ta=document.getElementById(id);
      if(ta&&responses[id]!=null)ta.value=responses[id];
    });
    // Everything else: KISS entries (kex_*), SiP statements, confirmed outputs, matching, five steps, game
    Object.keys(responses).forEach(function(k){if(responses[k]!==null&&responses[k]!==undefined)U3.v[k]=responses[k];});
    if(Array.isArray(responses['confirmed_items']))U3.conf=responses['confirmed_items'].slice();
    var hz=responses['__hz_match'];
    if(hz&&Array.isArray(hz.m)&&hz.m.length===HOT_ZONES.length){
      HZ.m=hz.m.map(function(x){x=x||{};return {hot:!!x.hot,al:!!x.al,ht:Number(x.ht)||0,at:Number(x.at)||0};});
      HZ.cur=(hz.cur>=0&&hz.cur<HOT_ZONES.length)?hz.cur:0;
    }
    okrLoad(responses['__okr_work']);
    u3RenderAll();
    saLoad(responses['__game']);
    // The group's four SiP statements: brought in from the Unit 2 page while the boxes are still empty
    if(![0,1,2,3].some(function(d){return u3v(sipKey(d)).trim();}))await sipBring(false);
    // C1/C5/C6 — reveal facilitator feedback, messages, and upload if a submission exists
    loadSubmissionFeedback();
  }catch(err){
    console.error('[unit2_m1_lens2_p] Load exception:',err);
  }
});

'''
h = h[:a] + LOAD + h[b:]
rep('renderKissGuideP();renderHZP();renderPMGuideP();renderBiasP();\nrenderKissExercise();renderOKRDraft();renderSummaryP();',
    "u3RenderAll();saInit('saHostP','p',gameChanged);")
# old step-tab helper of 4.1 is no longer used
rep('''function showStepP(prefix,i){
  document.querySelectorAll("#synthTabsP .step-tab").forEach(function(t,x){t.classList.toggle("active",x===i);});
  document.querySelectorAll("[id^=\\""+prefix+"_\\"]").forEach(function(p,x){p.classList.toggle("active",x===i);});
}
''', '')

# ── Section learning outcomes as on Carol's final deck (7 Oct): Section 1 outcome 2 and Section 2 reworded; Section 3 as it was;
#    Sections 4 and 5 are set where those sections are built above ──
rep('<li>Distinguish results that evidence progress from the activities that produce them.</li>', '<li>Translate the intent to measurable results.</li>')
rep('<li>Explain why an honest review of current practice must precede the setting of priorities.</li><li>Recognise the cost of setting targets before the path to the future state is understood.</li>', '<li>Recognise the benefits of mapping the terrain before setting goals.</li><li>Practise the translation of SiP into OKRs.</li>')

# ── 8. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
for gone in ('ref1', 'ref5', 'port1', 'savePort', 'renderBiasP', 'okrDraftP', 'kissExerciseP', 'Portfolio Artefact', 'cxLoad', 'caseToolP', 'Six Steps', 'six steps', 'six-step', 'Step 6', 'Enterprise Priority<', 'Less is More', 'Future-Reality', 'future-reality', 'narrative', 'Financial Performance', '4.2 — Breaking the Biases', '2.3 —', '3.2 —', '3.3 —', 'leadership team has'):
    assert gone not in h, 'still present: ' + gone
assert h.count('<script') == h.count('</script>'), 'script tags do not balance'
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('participant file written:', out, len(h))
