# -*- coding: utf-8 -*-
"""Unit 8 · Performance Measurement — the content of the five sections in two voices (12 October 2026).
v == 'p': participant page (speaks to "you"); v == 'f': facilitator page (speaks of "participants" / "the group"; preparation only, no entry box).
Teaching text is one shared text on both pages, in the fuller facilitator wording. Lines marked NEW are Claude's wording, approved with the findings report of 12 October."""
NL = '\r\n'
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'
def esc_ph(s): return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('\n', '&#10;')

def acc(title, meta, body, after='', open_=False):
    return ('<div class="acc%s">' % (' open' if open_ else '') + NL +
            '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">%s</div></div>%s</div>' % (title, meta, ARR) + NL +
            '<div class="acc-b"><div class="cb">' + NL + body + NL + '</div>' + ((NL + after + NL) if after else '') + '</div></div>')
def guide(label, *ps):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>' % label + NL + NL.join(p if p.startswith('<') else '<p>%s</p>' % p for p in ps) + NL + '</div>'
def activity(text, steps=None):
    return ('<div class="fac-note-full u8-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + NL + '<p>%s</p>' % text +
            ((NL + '<ol>' + ''.join('<li>%s</li>' % s for s in steps) + '</ol>') if steps else '') + NL + '</div>')
REF = 'Participants write a reflection in their own file: '
def reflection(rid, label, question, ph, rows=70):
    return ('<div class="ref-block" style="margin-top:16px;"><div class="ref-label">&#x270E; Reflection &mdash; %s</div>' % label +
            '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">%s</p>' % question +
            '<textarea class="ref-ta reflection-textarea" id="%s" style="min-height:%dpx;" placeholder="%s"></textarea>' % (rid, rows, esc_ph(ph)) +
            '<div class="ref-saved reflection-saved" id="%s-saved"></div><button class="ref-save" onclick="saveTA(this)">Save Reflection</button></div>' % rid)
def hero(label, title, lead):
    return '<div class="mod-hero"><div class="mod-hero-label">%s</div><h2>%s</h2><p>%s</p></div>' % (label, title, lead)
def slo(a, b):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>%s</li><li>%s</li></ul></div>' % (a, b)
def pcard(num, colour, name, body, extra):
    return ('  <div class="p-card" onclick="toggleP(this)">' + NL +
            '    <div class="p-head"><div class="p-meta"><div class="p-num" style="color:%s;">%s</div><div class="p-name">%s</div></div><div class="p-arr">&#9660;</div></div>' % (colour, num, name) + NL +
            '    <div class="p-body"><p>%s</p>%s</div>' % (body, extra) + NL + '  </div>')
def ask(v, p_q, f_q):
    return '<div class="p-reflect">Ask yourself: %s</div>' % p_q if v == 'p' else '<div class="p-insight">Facilitator prompt: &ldquo;%s&rdquo;</div>' % f_q
def steps(tabs_names, panels, num='Stage', group=True):
    t = '<div class="step-group">' + NL + '<div class="step-tabs">' + NL + NL.join('  <div class="step-tab%s" onclick="showStep(%d,this)"><div class="step-num">%s %d</div><div class="step-name">%s</div></div>' % (' active' if i == 0 else '', i, num, i + 1, n) for i, n in enumerate(tabs_names)) + NL + '</div>' + NL
    t += NL.join('<div class="step-panel%s">' % (' active' if i == 0 else '') + NL + p + NL + '</div>' for i, p in enumerate(panels)) + NL + '</div>'
    return t
def ul(items): return '<ul>' + NL + NL.join('<li>%s</li>' % x for x in items) + NL + '</ul>'
QUOTE = '<div class="hbox"><p style="font-family:\'Cormorant Garamond\',serif;font-size:%s;font-style:italic;">%s</p></div>'

# ═══ Unit header and Facilitator Guide ═══════════════════════════════════════════════════════════════
DESC_OLD = {'p': 'and converts performance data into organisational intelligence.</p>'}
DESC_NEW = 'and converts performance data into organisational intelligence through the Review&ndash;Realign&ndash;Restore cycle.</p>'
GUIDE_EDITS = [  # facilitator Guide tab: (old, new) exact replacements
    ('<p>Unit 8 closes the loop opened by Units 6 and 7. KPIs have been established,',
     '<p>Unit 8 closes the loop opened by Units 6 and 7. Key performance indicators (KPIs) have been established,'),
    ('Leaders must leave this unit understanding that measurement is an execution recovery system. The Accountability Loop role play in Application is non-negotiable: it is where the conceptual work becomes a leadership skill.</p>',
     'Leaders must leave this unit understanding that measurement is an execution recovery system. The Accountability Loop role play in part 4.4 is where the conceptual work becomes a leadership skill, and Section 5 applies the whole cycle to the group&rsquo;s own Key Results.</p>'),
    ('through the <strong>Collective Intelligence Circle</strong>, shifting leaders', 'through the <strong>Enterprise Performance Intelligence Circle</strong>, shifting leaders'),
    ('did your organisation learn anything &mdash; or did it just record scores?&rdquo;', 'what did your organisation learn, and what did it only record?&rdquo;'),
    ('leaders who treat the Accountability Loop as a confrontation tool. It is a diagnostic discipline. Its purpose is to restore momentum.', 'leaders who treat the Accountability Loop as a confrontation tool. Its purpose is diagnosis and restored momentum.'),
]
GUIDE_DROP = [  # facilitator Guide tab: paragraphs that leave
    '<p><strong>Watch for:</strong> leaders in the Integration section who revert to functional reporting',
    '<p><strong>Timing:</strong> Awareness and Intelligence can move at pace.',
]
GUIDE_ADD = '<p><strong>Teach the circle horizontally:</strong> each signal is read for what it means for the other functions. The Enterprise Performance Intelligence Circle exists to surface cross-functional dependencies.</p>'  # NEW

# ═══ Section 1 ═══════════════════════════════════════════════════════════════════════════════════════
def sec1(v):
    h = hero('Section 1 · Awareness — What', 'What is Performance Measurement?',
             'Establishing performance measurement as an execution visibility discipline and introducing the Review&ndash;Realign&ndash;Restore Cycle as the mechanism that keeps strategy correctable.')
    out = [h, '<div class="mod-body">', slo('Distinguish meaningful strategic progress from activity.', 'Explain how performance evidence converts into realignment and corrective action.'), '']
    if v == 'f':
        out.append(guide('FACILITATOR GUIDANCE — Awareness',
            'Open with the core provocation: <em>"Work is happening. Teams are busy. Initiatives are underway. But can you confidently say the work being done is actually advancing the strategy?"</em> This question unlocks the gap that this entire unit addresses: the difference between activity visibility and progress visibility.',
            'The <strong>four strategic purposes</strong> are the conceptual anchor. Most leaders can name visibility; fewer spontaneously name learning and course correction. These are the purposes that make performance measurement a leadership discipline.',
            'The <strong>Review&ndash;Realign&ndash;Restore Cycle</strong> is the operational centrepiece. Walk each stage with precision: Review establishes evidence-based visibility; Realign diagnoses root cause; Restore rebuilds momentum. The key facilitation moment is when leaders understand that most performance gaps have a diagnosable cause, and that the three root causes (accountability, skill, structural misfit) require different responses.'))
        out.append('')
    # 1.1
    open_ = ('<p>Your performance management system has been set and the mechanisms for establishing performance are in place. Your commitments have been secured. Now the most important discipline of execution begins.</p>' if v == 'p' else
             '<p>The performance management system has been set and mechanisms for establishing performance are in place. Commitments have been secured. Now the most important discipline of execution begins.</p>')
    b11 = NL.join([open_,
        '<p>Strategy execution fails at the level of <strong>visibility</strong>. Performance measurement is the discipline that makes execution visible. It answers a simple but decisive question:</p>',
        QUOTE % ('1.15rem', 'Are we actually moving closer to our Success in Practice?'),
        '<p>Most organisations are extremely good at measuring <strong>activity</strong>: how many projects were launched, how many meetings were held, how many deliverables were completed. These indicators provide evidence that work is occurring. But activity alone does not indicate whether the organisation is actually moving closer to the strategic outcome it set out to achieve.</p>',
        '<p>Performance measurement therefore asks a different set of questions. The question moves from <em>"What work was done?"</em> to <em>"What changed because of the work?"</em> The organisation examines evidence of progress. This shift transforms performance management from an administrative reporting exercise into an <strong>execution intelligence system</strong>.</p>'])
    if v == 'p':
        out.append(acc('1.1 &mdash; From Activity to Progress: The Visibility Shift', 'Core concept', b11 + NL + reflection('ref1', 'Activity vs Progress',
            'In your function, what are you currently measuring that reflects activity? What would reflect genuine progress toward your strategic outcome?',
            'Activity measures I use:\nProgress measures I should add:'), open_=True))
    else:
        out.append(acc('1.1 &mdash; From Activity to Progress: The Visibility Shift', 'Core concept', b11,
            activity(REF + 'what they measure today that reflects activity, and what would reflect genuine progress toward their strategic outcome.'), open_=True))
    out.append('')
    # 1.2
    intro = ('<p>At its core, performance measurement serves four strategic purposes within the organisation. Select each to explore, and ask yourself where your organisation is strongest and where it is weakest.</p>' if v == 'p' else
             '<p>At its core, performance measurement serves four strategic purposes within the organisation. Select each to explore.</p>')
    cards = [
        pcard('Purpose 01', '#8ab0e8', 'Creates Visibility', 'Leaders can observe where the organisation is gaining momentum and where it is stalling. Strategic priorities that once existed only as intentions begin to appear as measurable progress signals. Without measurement, leaders are flying blind: confident in effort but uncertain about direction.',
              ask(v, 'Where in your organisation is execution happening in the dark? Where are you most likely to be surprised at the end of a reporting period?', 'Where in your organisation does execution happen in the dark? Where are you most likely to be surprised at the end of a reporting period?')),
        pcard('Purpose 02', 'var(--teall)' if v == 'p' else 'var(--gold)', 'Establishes Accountability', 'When key performance indicators (KPIs) are clearly linked to enterprise Objectives and Key Results (OKRs), ownership becomes visible. Leaders and teams understand which part of the strategy they are responsible for advancing. Accountability without measurement is aspiration without a feedback loop: it depends entirely on personal commitment, with no organisational structure behind it.',
              ask(v, 'If your KPIs disappeared from your scorecard but the targets remained unchanged, how many would still be actively owned?', 'If your KPIs disappeared from your scorecard but the targets remained unchanged, how many would still be actively owned?')),
        pcard('Purpose 03', '#5ecba1', 'Enables Learning', 'Performance reviews reveal patterns about how work actually unfolds inside the organisation. Leaders begin to see which approaches accelerate progress and which create friction or delay. Over time, disciplined review conversations accumulate into an organisational understanding of how execution actually works: a capability that compounds over successive strategy cycles.',
              ask(v, 'What did your organisation actually learn from its last strategy cycle? What did it learn about how execution works inside your system?', 'What did your organisation actually learn from its last strategy cycle? What did it learn about how execution works inside your system?')),
        pcard('Purpose 04', '#c39de0', 'Enables Course Correction', 'Early signals allow teams to intervene while progress is still recoverable. Problems are addressed when they are small enough to resolve. This purpose is why measurement frequency matters: a signal detected in week four carries a different cost from the same signal detected in week twelve.',
              ask(v, 'What is the average gap in your organisation between when a performance problem begins and when leadership first becomes aware of it?', 'What is the average gap in your organisation between when a performance problem begins and when leadership first becomes aware of it? What does that gap cost?')),
    ]
    out.append(acc('1.2 &mdash; The Four Strategic Purposes of Performance Measurement', 'Click each to explore', intro + NL + '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>'))
    out.append('')
    # 1.3
    review = NL.join(['<h5>Establishing Evidence-Based Visibility</h5>',
        '<p>The cycle begins with Review. The purpose is to establish a clear and shared understanding of what progress has actually occurred. Execution reality must be grounded in evidence.</p>',
        '<p>In the S2R&reg; system, the review process begins with the KPI owner conducting a <strong>first-level self-assessment</strong>. The individual examines the agreed targets and assesses progress against the rating scale set in the performance management architecture (Unit 6), submitting verifiable evidence that demonstrates what progress has occurred since the previous review period. Evidence may include operational data, financial results, project milestones, customer metrics, or any other proof that demonstrates whether the intended activity produced the expected movement.</p>',
        '<p>At the same time, the leader conducts a <strong>parallel assessment</strong>, independently evaluating the level of progress achieved. When both perspectives are brought into the review conversation, the organisation avoids two common distortions: the individual evaluating without challenge, and the leader imposing evaluation without understanding operational realities.</p>',
        '<p><strong>Three questions anchor the review:</strong></p>',
        ul(['Did the agreed activity actually occur?', 'Did the activity produce the expected progress toward the target?', 'What does the available evidence tell us about execution reality?'])])
    realign = NL.join(['<h5>Diagnosing the Source of Performance Gaps</h5>',
        '<p>The second stage begins when the review reveals a gap between expected progress and actual progress. Execution gaps are common; in complex organisations they are inevitable. The purpose of realignment is to <strong>diagnose the true source of the gap</strong> so the organisation can intervene intelligently.</p>',
        '<p>When a gap is identified, the leader activates the <strong>Accountability Loop</strong>: a structured diagnostic process designed to restore traction and ownership without collapsing into unproductive performance pressure. Most performance gaps emerge from one of three underlying conditions:</p>',
        ul(['<strong>Lack of accountability</strong>: the individual understands the task but has lost the motivational connection to it. Recovery: reconnect purpose and ownership by revisiting the broader organisational context of the KPI.',
            '<strong>Lack of skill</strong>: the individual is committed but lacks the capability required to achieve the expected level. Recovery: targeted coaching, peer support, formal training, or timeline adjustment.',
            '<strong>Misfit of role or structural constraint</strong>: the individual&rsquo;s strengths do not align with the specific responsibilities. Recovery: structural alignment discussion, task redistribution, or repositioning. Note: the performance conversation must remain separate from the role conversation.'])])
    restore = NL.join(['<h5>Rebuilding Momentum</h5>',
        '<p>Once the root cause has been identified and addressed, the cycle moves to <strong>Restore</strong>. The purpose is to convert insight into concrete forward action, rebuilding momentum and re-establishing execution traction.</p>',
        ul(['Corrective actions are defined clearly', 'Specific next steps are agreed', 'Responsibilities are reaffirmed', 'Follow-up timelines are established']),
        '<p>The KPI owner leaves the conversation with a renewed understanding of what must happen next and by when. The leader confirms how progress will be monitored going forward. This stage ensures that the review conversation produces visible forward movement.</p>',
        '<p>Within the S2R&reg; system, the alignment state of the KPI is also updated at this stage. The revised state reflects whether the enabling conditions for execution (clarity, capability and commitment) are now fully restored, providing an ongoing signal of organisational readiness.</p>'])
    b13 = ('<p>Within the S2R&reg; system, performance measurement operates through a continuous execution cycle called the <strong>Review&ndash;Realign&ndash;Restore Cycle</strong>. Its purpose is to make measurement the starting point of a leadership conversation that protects momentum, strengthens accountability, and restores progress when execution drifts.</p>' + NL +
           steps(['Review', 'Realign', 'Restore'], [review, realign, restore]))
    if v == 'p':
        out.append(acc('1.3 &mdash; The Review&ndash;Realign&ndash;Restore Cycle', '3 stages', b13 + NL + reflection('ref2', 'The Review&ndash;Realign&ndash;Restore Cycle in Your Organisation',
            'Think of a current performance gap in your function. Which stage of the Review&ndash;Realign&ndash;Restore Cycle is it in? If you activated the Accountability Loop, which root cause would you most likely be diagnosing?',
            'The gap:\nThe stage it is in:\nThe root cause I would most likely diagnose:')))
    else:
        out.append(acc('1.3 &mdash; The Review&ndash;Realign&ndash;Restore Cycle', '3 stages', b13,
            activity(REF + 'one current performance gap in their function, the stage of the Review&ndash;Realign&ndash;Restore Cycle it sits in, and the root cause they would most likely diagnose.')))
    out.append('')
    return NL.join(out)

# ═══ Section 2 ═══════════════════════════════════════════════════════════════════════════════════════
def sec2(v):
    out = [hero('Section 2 · Intelligence — Why', 'Why Performance Measurement Determines Execution Velocity',
                'Understanding why the discipline of review conversations is the factor that determines whether strategy execution sustains momentum or quietly stalls.'),
           '<div class="mod-body">', slo('Explain why review discipline determines the pace of execution.', 'Interpret the progress signals that emerge in performance reviews and the response each requires.'), '']
    if v == 'f':
        out.append(guide('FACILITATOR GUIDANCE — Intelligence',
            'The key shift in this section is from measurement as tool to measurement as leadership discipline. Most leaders accept the logic of measurement; fewer have internalised that the rhythm of review conversations is itself a strategic capability, and that allowing that rhythm to weaken has predictable, compounding consequences.',
            'The four consequences of weak review discipline are cumulative. Missed early warnings lead to diffused accountability; diffused accountability suppresses learning; suppressed learning erodes leadership credibility. Walk this chain deliberately so participants can recognise it in their own organisations.',
            'For the three signals: Progress Confirmation is a leadership opportunity to reinforce the behaviours that generated momentum. Many leaders skip past confirmation because there is nothing to fix. Redirect them: reinforcing what works is as strategically important as correcting what does not.'))
        out.append('')
    b21 = NL.join(['<p>The difference between organisations that sustain execution momentum and those that quietly stall emerges after the strategy is launched. Most leadership teams are capable of producing sophisticated strategic plans.</p>',
        '<p>The difference appears in the discipline with which leaders return to the strategy and ask a difficult but necessary question: <em>Are we actually progressing?</em></p>',
        '<p><strong>Execution discipline</strong> is the organisational habit of repeatedly examining progress, confronting evidence honestly, and adjusting behaviour before small deviations become systemic failures. Without this discipline, even well-designed strategies slowly lose traction.</p>',
        QUOTE % ('1.05rem', 'Performance measurement must be understood as an execution discipline. This understanding determines whether performance management becomes a compliance ritual or a genuine engine of execution progress.')])
    out.append(acc('2.1 &mdash; Execution Discipline: The Real Differentiator', 'Core argument', b21, open_=True)); out.append('')
    red = 'rgba(231,76,60,.8)'
    cards = [
        pcard('Consequence 01', red, 'Early Warning Signals Are Missed', 'Execution rarely collapses suddenly. Performance deterioration typically begins with small, subtle indicators: a milestone that slips by a few days, a process bottleneck beginning to slow delivery, a capability gap emerging in one team. These signals often appear months before the final KPI target is at risk. But if leaders are not regularly examining performance evidence, these signals remain invisible. By the time the problem becomes visible at the end of the reporting period, the opportunity for early intervention has already been lost.',
              ask(v, 'In your experience, what is the typical lag between when a performance problem begins and when leadership acts? What would closing that lag by half be worth?', 'In your experience, what is the typical lag between when a performance problem begins and when leadership acts? What would closing that lag by half be worth to your organisation?')),
        pcard('Consequence 02', red, 'Gradual Diffusion of Accountability', 'Accountability is sustained through visibility. When review conversations disappear or become irregular, the psychological signal shifts. Targets remain written on the scorecard, but they no longer appear in leadership dialogue. KPI owners begin to interpret the absence of review as an indication that the target is no longer an active organisational priority. The KPI quietly moves from being operational to being aspirational. Work continues, but the urgency associated with the strategic outcome begins to fade.',
              ask(v, 'Which KPIs in your current scorecard are operational and which have quietly become aspirational? What made the difference?', 'Which KPIs in your current scorecard are operational and which have quietly become aspirational? What made the difference?')),
        pcard('Consequence 03', red, 'Loss of Organisational Learning', 'Every review conversation contains valuable insight about which approaches accelerate progress, where operational friction exists, and which cross-functional dependencies are working and which are slowing things down. When review conversations are reduced to occasional reporting exercises, results are recorded but the organisation never pauses to understand why those results occurred. Without reflection, improvement becomes accidental. The organisation&rsquo;s execution capability stagnates even as it accumulates more strategic ambition.',
              ask(v, 'What does your organisation know now about how execution works inside your system that it did not know eighteen months ago?', 'What does your organisation know now about how execution works inside your system that it did not know eighteen months ago? If the answer is &lsquo;not much,&rsquo; that is a review discipline signal.')),
        pcard('Consequence 04', red, 'Erodes Leadership Credibility', 'When leaders set ambitious targets and communicate strategic priorities, they create an expectation that those priorities will remain visible in the leadership conversation. If those targets are not revisited through structured performance discussions, a subtle message spreads: the strategy announcement was more symbolic than operational. Teams become less attentive to new strategic commitments because they have learned that priorities often quietly fade. Consistent performance reviews counteract this by demonstrating that strategic priorities are ongoing leadership commitments.',
              ask(v, 'What is the current level of strategic commitment in your organisation? How much of that is shaped by what leaders consistently review, and how much by what they announce?', 'What is the current level of strategic commitment in your organisation? How much of that is shaped by what leaders consistently review, and how much by what they announce?')),
    ]
    out.append(acc('2.2 &mdash; Four Consequences of Weak Review Discipline', 'Click each to explore',
        '<p>When performance reviews occur inconsistently or superficially, several predictable patterns begin to emerge. These are the foreseeable consequences of allowing the review rhythm to weaken.</p>' + NL + '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>'))
    out.append('')
    sig = NL.join(['<p>Healthy performance reviews produce clear signals about the state of execution. Each signal requires a different leadership response. Select a signal to explore.</p>',
        '<div class="signal-grid">',
        '  <div class="sig-card" onclick="showSig(this,\'sig-a\')">', '    <div class="sig-top"><div class="sig-icon">&#9650;</div><div class="sig-name">Signal 01</div><div class="sig-label">Progress Confirmation</div></div>', '    <div class="sig-bar"></div>', '  </div>',
        '  <div class="sig-card" onclick="showSig(this,\'sig-b\')">', '    <div class="sig-top"><div class="sig-icon">&#9888;</div><div class="sig-name">Signal 02</div><div class="sig-label">Early Warning</div></div>', '    <div class="sig-bar"></div>', '  </div>',
        '  <div class="sig-card" onclick="showSig(this,\'sig-c\')">', '    <div class="sig-top"><div class="sig-icon">&#9660;</div><div class="sig-name">Signal 03</div><div class="sig-label">Significant Gap</div></div>', '    <div class="sig-bar"></div>', '  </div>',
        '</div>',
        '<div class="sig-detail" id="sig-a">',
        '  <p>The KPI is moving steadily toward its target within the expected timeline. The evidence submitted clearly demonstrates that the agreed activities are producing measurable movement toward the desired outcome.</p>',
        '  <p><strong>Leadership response:</strong> The role of the review conversation is to reinforce the behaviours and decisions that generated the progress. Leaders highlight the factors that contributed to success and acknowledge the discipline and coordination that produced the movement. By recognising these patterns, the organisation strengthens the behaviours that sustain execution momentum.</p>',
        '  <div class="sig-action">Progress confirmation serves both as validation and as reinforcement. Do not pass over it quickly. Name what worked and why: this builds the execution behaviours that compound over time.</div>',
        '</div>',
        '<div class="sig-detail" id="sig-b">',
        '  <p>Results show signs of slowing progress. The evidence indicates that the incremental targets expected for the period have not been fully achieved, but the gap is still small enough that recovery remains possible.</p>',
        '  <p><strong>Leadership response:</strong> This is precisely the moment when performance measurement demonstrates its strategic value. Because the signal has been detected early, leaders can intervene while there is still time to adjust course. Resources may be reallocated, additional support provided, processes refined, or dependencies between teams addressed. The review conversation becomes an opportunity for proactive correction.</p>',
        '  <div class="sig-action">The organisation does not wait for failure to occur before responding. Early warning signals are the primary return on investment of a disciplined review rhythm.</div>',
        '</div>',
        '<div class="sig-detail" id="sig-c">',
        '  <p>There is a significant gap between expected progress and actual progress. The review conversation must move beyond surface-level discussion. This signal activates the Accountability Loop.</p>',
        '  <p><strong>Leadership response:</strong> Leaders examine whether the gap reflects a loss of accountability, a capability constraint, or a structural misalignment between the individual and the role. Once the underlying cause becomes visible, the organisation can intervene with clarity. The Accountability Loop ensures that performance gaps become sources of organisational learning and recalibration.</p>',
        '  <div class="sig-action">Activate the Accountability Loop. Diagnose before prescribing. The correct root cause determines the correct recovery action: pressure alone will not solve a skill gap, and coaching will not solve a structural misfit.</div>',
        '</div>'])
    if v == 'p':
        out.append(acc('2.3 &mdash; Three Progress Signals in Healthy Review Conversations', 'Select each signal', sig + NL + reflection('ref3', 'Which Signal Are You Seeing?',
            'Name one KPI or Key Result in your current portfolio. Which signal does it show: Progress Confirmation, Early Warning or Significant Gap? What is the evidence, and what is your next leadership action?',
            'The KPI or Key Result:\nThe signal it shows:\nThe evidence:\nMy next leadership action:')))
    else:
        out.append(acc('2.3 &mdash; Three Progress Signals in Healthy Review Conversations', 'Select each signal', sig,
            activity(REF + 'one KPI or Key Result of their own, the signal it shows, the evidence and their next leadership action.')))
    out.append('')
    return NL.join(out)

# ═══ Section 3 ═══════════════════════════════════════════════════════════════════════════════════════
GAPS = [  # (number, title, short name for lists, one-line meaning NEW, paragraphs, facilitator question)
    ('Gap 01', 'The Horizontal Coordination Gap', 'Horizontal Coordination', 'Reviews happen inside functions, so no one sees how the functions together move the enterprise outcome.', [
        'One of the most common breakdowns occurs when performance reviews happen <strong>inside functions, with no cross-functional view</strong>. Each department reviews its KPIs independently. Finance examines financial indicators. Operations reviews throughput. Marketing examines campaign performance. Individually, these conversations may be rigorous and technically sound.',
        'But strategy execution rarely moves through a single function. Enterprise outcomes depend on interdependent execution across multiple functions. When performance reviews remain confined within functional boundaries, leaders see partial performance signals and miss the full execution pattern. Each function may report strong progress while the overall strategic outcome remains inconsistent.',
        'The leadership team, acting as the collective intelligence for execution discipline, closes this gap by introducing periodic <strong>cross-functional performance reviews</strong> where the executive team collectively examines how the KPIs across functions interact to produce enterprise outcomes.'],
     'Name a strategic outcome in your organisation that required three or more functions to execute successfully. Where did the handoffs break down, and would a cross-functional review have caught it earlier?'),
    ('Gap 02', 'The Evidence Quality Gap', 'Evidence Quality', 'Reviews rest on weak, late or activity-only evidence, so time goes on debating the data.', [
        'Performance measurement loses power when review conversations rely on <strong>weak or inconsistent evidence</strong>. In some cases KPI owners present narrative explanations with no verifiable indicators. In others, the evidence reflects activity alone, with no evidence of progress toward the outcome. Sometimes information arrives too late to support timely decisions.',
        'When evidence quality declines, review conversations shift away from execution insight and toward <strong>interpretation debates</strong>. Leaders begin discussing whether the data can be trusted, and the review loses sight of what the data reveals about progress. Over time, the credibility of the performance system weakens.',
        'Closing this gap requires the leadership team, acting as the collective intelligence for execution discipline, to reinforce a simple but powerful principle: every performance review must be anchored in verifiable evidence that shows observable movement toward the outcome, is timely enough to inform decisions, and is clearly connected to the KPI, target, or Key Result being assessed.'],
     'In your last performance review, what share of the conversation was spent debating the data, and what share acting on it? That ratio is a proxy for your evidence quality gap.'),
    ('Gap 03', 'The Review Rhythm Breakdown', 'Review Rhythm', 'Reviews happen too rarely or irregularly, so small deviations grow unseen.', [
        'Even well-designed performance systems weaken if the organisation does not maintain a <strong>consistent rhythm of review conversations</strong>. Strategy execution unfolds over time. Progress appears gradually through incremental movement across weeks and months. If review conversations occur too infrequently, leaders lose visibility into the trajectory of that movement. Small deviations accumulate unnoticed until they become significant performance gaps.',
        'Irregular review cycles also weaken behavioural discipline. KPI owners begin to treat measurement as a reporting event.',
        'Healthy performance measurement requires a predictable organisational rhythm. Leaders know when reviews will occur. KPI owners know when evidence must be prepared. Teams expect progress to be examined regularly. This rhythm creates a cultural signal: execution progress is observed continuously.'],
     'How predictable is your organisation&rsquo;s review rhythm? If a KPI owner was asked to describe the review schedule without referring to a calendar, could they?'),
    ('Gap 04', 'The Learning Suppression Gap', 'Learning Suppression', 'Reviews only judge results, so people defend them and the causes stay hidden.', [
        'A subtle but corrosive breakdown appears when performance reviews focus <strong>exclusively on evaluation</strong>. If review conversations concentrate only on whether targets were achieved, teams often become cautious about discussing obstacles openly. People instinctively defend results and leave the deeper causes unexplored. This dynamic suppresses organisational learning.',
        'Yet strategy execution is inherently experimental. Organisations are constantly discovering what works, where friction exists, and how coordination across functions actually unfolds. Healthy performance reviews therefore balance <strong>accountability with curiosity</strong>. Leaders examine evidence rigorously, yet they also explore what the organisation is learning from execution patterns.',
        'Questions shift from <em>&ldquo;Why was the target missed?&rdquo;</em> to <em>&ldquo;What is the system teaching us about how execution actually works?&rdquo;</em> When this learning dimension becomes part of review conversations, performance measurement evolves from a scoring mechanism into a capability-building system.'],
     'What is the dominant mood in your organisation&rsquo;s performance review meetings: defence or curiosity? What would shift it?'),
]
BRIGADE = 'the collective intelligence for execution discipline of the leadership team'
def sec3(v):
    out = [hero('Section 3 · Extrapolating — Where', 'Where Does Performance Measurement Break Down Across Functions?',
                'Examining where %s unintentionally weakens the performance measurement discipline through four characteristic fractures.' % BRIGADE),
           '<div class="mod-body">', slo('Identify where the review and interpretation of performance evidence break down across functions.', 'Assess which breakdown is most prevalent in their own organisation.'), '']
    if v == 'f':
        out.append(guide('FACILITATOR GUIDANCE — Extrapolating',
            'Begin by establishing the key provocation: <em>"Most modern organisations have agreed goals and KPIs, dashboards, reporting tools, and performance frameworks. The breakdown usually occurs in how leaders review and interpret the measurement together."</em>',
            'The four gaps are observable patterns. Invite participants to place their organisation honestly on each one. The <strong>Horizontal Coordination Gap</strong> is typically the most impactful but least visible: each function may report strong progress while the enterprise outcome remains inconsistent. The <strong>Learning Suppression Gap</strong> is often the most culturally embedded and the hardest to shift because it requires leaders to move from a judgement posture to a curiosity posture.',
            'Use the CXO perspective to make this concrete: ask participants to post in the chat which gap their function is most likely to create, and the first-order impact of that gap on the organisation.'))
        out.append('')
    cards = []
    for num, title, short, mean, ps, fq in GAPS:
        extra = ('      <div class="gap-fac">Facilitator question: &ldquo;%s&rdquo;</div>' % fq + NL) if v == 'f' else ''
        cards.append('  <div class="gap-card" onclick="toggleGap(this)">' + NL +
                     '    <div class="gap-head"><div class="gap-meta"><div class="gap-num">%s</div><div class="gap-title">%s</div></div><div class="gap-arr">&#9660;</div></div>' % (num, title) + NL +
                     '    <div class="gap-bar"></div>' + NL + '    <div class="gap-body">' + NL + NL.join('      <p>%s</p>' % p for p in ps) + NL + extra + '    </div>' + NL + '  </div>')
    body = ('<p>Performance measurement is ultimately a <strong>leadership conversation discipline</strong>. Most organisations have agreed goals and KPIs; the breakdown usually occurs in <strong>how leaders review and interpret the measurement together</strong>. When that discipline weakens, several predictable fractures appear across the organisation. Select each gap below to examine where it occurs and what it costs.</p>' + NL +
            '<div class="gap-grid">' + NL + NL.join(cards) + NL + '</div>')
    if v == 'p':
        sel = ''.join('<div class="score-row"><span class="score-lt">0%d</span><span class="score-tm">%s</span><select class="score-sel" data-key="ref4" data-idx="%d" onchange="syncScores(\'ref4\')"><option value="">&ndash;</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></div>' % (i + 1, g[2], i) + NL for i, g in enumerate(GAPS))
        refb = ('<div class="ref-block" style="margin-top:16px;"><div class="ref-label">&#x270E; Reflection &mdash; Which Gap Is Most Prevalent in Your Organisation?</div>'
                '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">Rate each gap in your organisation (1 = rare, 5 = common). Then name the gap you are most responsible for closing and your first action.</p>' + NL +
                '<div class="score-grid" data-key="ref4">' + NL + sel + '</div>' + NL +
                '<label class="score-notes-lbl" for="ref4_notes">The gap I am most responsible for closing &amp; my first action</label>' + NL +
                '<textarea class="score-notes" id="ref4_notes" data-key="ref4" oninput="syncScoresDebounced(\'ref4\')" placeholder="The gap I am most responsible for closing: ...&#10;First action I will take: ..."></textarea>' + NL +
                '<textarea id="ref4" class="reflection-textarea" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="ref4-saved"></div><button class="ref-save" onclick="scoreSaveBtn(this,\'ref4\')">Save Reflection</button></div>')
        out.append(acc('3.1 &mdash; Four Fractures in Performance Measurement', 'Select each gap', body + NL + refb, open_=True))
    else:
        out.append(acc('3.1 &mdash; Four Fractures in Performance Measurement', 'Select each gap', body,
            activity(REF + 'a rating of each of the four gaps in their organisation, from 1 (rare) to 5 (common), and the gap they are most responsible for closing.'), open_=True))
    out.append('')
    return NL.join(out)

# ═══ Section 4 ═══════════════════════════════════════════════════════════════════════════════════════
CIRCLE_RULES = ['Every entry names its evidence from the performance management (PM) review sheets.', 'Contributions are concise and structured.', 'Signals only: no storytelling.', 'A signal that repeats across functions is marked as repeating.', 'The circle ends with one clear enterprise decision.']  # from the Facilitator Control Rules
SYN_Q = ['What execution pattern is emerging?', 'Where are warning signals repeating?', 'Where are cross-functional dependencies breaking down?', 'Where is the expectations chain weakest?', 'What decision must we take now?']
ROUNDS = [
    ('Collective Trajectory', 'Establishing the Collective Trajectory of Strategy Execution', [
        'Each leader begins by stating the current percentage progress toward their Key Results and KPIs. This percentage is derived from the PM ratings and evidence documented in their PM review sheet.',
        'The contribution follows a simple structure: the leader states the overall progress signal, briefly identifies the evidence supporting that signal, and clarifies whether execution momentum is accelerating, stable, or slowing.',
        '<em>Example:</em> The COO may report that operational readiness KPIs show 72% progress toward the strategic Key Result, supported by throughput improvements and cycle-time reductions documented in the review sheets.',
        '<em>Example:</em> The CFO may report that financial indicators show 65% progress toward the quarterly profitability milestone, supported by margin improvements and cost optimisation evidence.',
        'As each leader shares their progress signal, the circle begins to reveal a pattern. Some functions may show strong forward momentum; others may show slower movement toward their targets. The executive team begins to see the <strong>collective trajectory</strong> of strategy execution.'],
     ('ref5', 'Your Round 1 Contribution', 'For one of your Key Results or KPIs: what is your current percentage progress, what evidence supports it, and is your momentum accelerating, stable or slowing?', 'My Key Result or KPI progress: ____%\nSupporting evidence: ...\nMomentum signal: Accelerating / Stable / Slowing\nBecause: ...')),
    ('Early Warnings', 'Surfacing Early Warning Indicators', [
        'Once the progress signals are visible, the circle moves to the second signal: early warning indicators. Each leader shares one or two warning signals that emerged during their PM review conversations. These signals must again be grounded in evidence drawn from the review sheets.',
        'Early warnings typically appear before a KPI or Key Result is formally off target. They often emerge as subtle patterns that indicate potential future friction. Examples might include:',
        ul(['An operational process beginning to slow delivery times', 'A capability gap that may affect upcoming milestones', 'A supply constraint that could delay implementation of strategic initiatives', 'A change in customer feedback signalling emerging dissatisfaction']),
        'The purpose of sharing these signals is to surface emerging risks early enough for collective intervention. When these warnings are shared across the circle, leaders often discover that the signal appearing in one function is connected to activity in another: what appeared as an isolated operational issue may reveal itself as a <strong>cross-functional execution dependency</strong>.'],
     ('ref6', 'Your Round 2 Contribution', 'Which one or two early warning signals have emerged in your area? What evidence supports each, and what could it affect?', 'Warning signal 1: ...\nEvidence: ...\nPotential impact: ...\n\nWarning signal 2 (if applicable): ...')),
    ('Execution Learning', 'Capturing Execution Learning', [
        'The final round focuses on execution learning. Every review conversation produces insight about how the organisation actually executes strategy. During this round, each leader shares one key learning emerging from their PM reviews. This learning must be anchored in evidence from the review conversations.',
        ul(['The CHRO may highlight that performance review discussions revealed a leadership capability gap affecting accountability conversations', 'The CTO may share that system visibility improvements significantly accelerated operational decision-making', 'The CMO may highlight a pattern in customer experience data that revealed which service interactions most strongly influence trust']),
        'These learnings allow the executive team to develop a shared understanding of how execution works inside the organisation. Over time, the organisation accumulates a body of practical execution intelligence that improves how strategy is implemented.'],
     ('ref7', 'Your Round 3 Contribution', 'What is one key execution learning from your performance reviews? What evidence supports it, and does it apply to your function or to the enterprise?', 'Key execution learning: ...\nEvidence: ...\nWhere it applies (function / enterprise): ...')),
]
SCENARIO = ('<p>You are a CXO responsible for the OKR: <strong>&ldquo;Reduce customer complaint resolution time from 48 hours to 12 hours.&rdquo;</strong></p>' + NL +
            '<p>The latest performance review shows that progress has stalled and complaint resolution is still averaging <strong>36 hours</strong>. The target deadline is six weeks away. You must now activate the Accountability Loop.</p>')
ROLES = [('CXO Role', 'Conducts the accountability conversation. Must diagnose the root cause without blaming. Uses the Accountability Loop to identify whether the issue is accountability, skill, or structural misfit, then uses the alignment dialogue of Unit 7 to restore momentum. Aims to reach an alignment of 9&ndash;10.'),
         ('Team Member Role', 'Responsible for execution of the improvement initiative. Responds authentically to the conversation. May show defensiveness, uncertainty, or genuine constraint, reflecting real organisational dynamics.'),
         ('Observer Role', 'Evaluates the quality of the conversation against the four criteria below. Provides structured feedback after the role play. Does not intervene during the exercise.')]
CAUSES = [('Root Cause A', 'Lack of Accountability', 'The individual understands the task but has lost motivational connection. Recovery: reconnect to purpose and enterprise context.'),
          ('Root Cause B', 'Lack of Skill', 'The individual is committed but lacks the capability required. Recovery: coaching, training, timeline adjustment.'),
          ('Root Cause C', 'Misfit / Structural Constraint', 'Strengths do not align with responsibilities. Recovery: structural alignment, redistribution, or repositioning.')]
CRITERIA = [('Criterion 01', 'Evidence Was Used in the Discussion', 'Did the CXO anchor the conversation in verifiable performance data? Was the 36-hour average cited specifically? Were trends, milestones, or other evidence referenced? A conversation without evidence quickly becomes a debate about effort.'),
            ('Criterion 02', 'Leader Avoided Blame and Focused on Diagnosis', 'Did the CXO approach the conversation with curiosity? Was the tone diagnostic? Key signal: if the team member became defensive and the CXO escalated pressure in response, the blame dynamic was activated. A skilled leader redirects defensiveness by returning to evidence and narrowing to root cause.'),
            ('Criterion 03', 'Root Cause Was Correctly Identified', 'Did the CXO arrive at a root cause diagnosis through genuine dialogue, or assume one at the outset? The root cause must emerge from the conversation. A misdiagnosed root cause leads to a mismatched recovery response that will fail even if executed well.'),
            ('Criterion 04', 'Clear Corrective Actions Were Agreed', 'Did the conversation end with specific, time-bound corrective actions that both parties understood and accepted? Was an alignment score agreed? Was a follow-up mechanism established? A review conversation that does not produce a named next action has not completed the Restore stage of the cycle.')]
HOW_44_P = ['In class, your facilitator assigns three roles: the CXO, the team member and the observer.',
            'The CXO opens with the evidence: complaint resolution is still averaging 36 hours against the 12-hour target.',
            'The CXO diagnoses the root cause with the team member, using the three root causes below, then agrees the corrective actions and asks the alignment question.',
            'The observer posts in the chat how the conversation met each of the four criteria.',
            'After the role play, record below the root cause you diagnosed and how you reached it, the corrective actions agreed and the alignment score. Your entries save as you type and go to your facilitator when you select Submit to Facilitator.']
def sec4(v):
    out = [hero('Section 4 · Integration — Collective', 'Cross-Leadership Performance Intelligence',
                'Building the Enterprise Performance Intelligence Circle: the mechanism through which the executive leadership team transforms individual performance management (PM) review signals into a shared view of enterprise execution momentum.'),
           '<div class="mod-body">', slo('Interpret individual performance signals within a shared enterprise view of progress.', 'Derive enterprise decisions and organisational learning from collective performance evidence.'), '']
    if v == 'f':
        out.append(guide('FACILITATOR GUIDANCE — Integration',
            'The shift in this section is from function to enterprise. The critical reframe is the question that must guide the entire section: <em>&ldquo;Is the chain of execution across our functions holding together?&rdquo;</em>',
            'The three rounds work in sequence: teach them in order, without blending them. Round 1 establishes the baseline. Without the collective trajectory being visible first, Round 2 warning signals lack context and Round 3 learnings lack a system to learn about.',
            'The Synthesis Layer at the end is where the real intelligence emerges: that is where the enterprise decision is made.',
            'Teach the evidence rule with the 4.2 examples: each signal names the PM review evidence behind it. This single discipline separates an Enterprise Performance Intelligence Circle from an opinion forum.'))
        out.append('')
    b41 = NL.join(['<p>Because performance measurement spans the entire organisation, no single function can safeguard its integrity alone. The responsibility rests with the executive leadership collective. The collective intelligence ensures that performance reviews remain connected to enterprise outcomes.</p>',
        '<p>This means regularly stepping back and asking deeper questions:</p>',
        ul(['Are our review conversations revealing how execution is truly unfolding?', 'Are the signals we are observing early enough for corrective action?', 'Are we interpreting the evidence together or only within our functions?', 'Are we learning from execution patterns or simply recording performance scores?']),
        '<p>The key question that must guide the collective review is:</p>',
        QUOTE % ('1.1rem', '&ldquo;Is the chain of execution across our functions holding together?&rdquo;'),
        '<p>The conversation moves on from asking <em>&ldquo;Is my function achieving its KPI or Key Result?&rdquo;</em> When leaders observe performance horizontally in this way, coordination improves and performance measurement begins to reveal the true state of enterprise execution.</p>'])
    out.append(acc('4.1 &mdash; The Collective Intelligence Principle', 'Why enterprise performance requires collective review', b41, open_=True)); out.append('')
    panels = []
    for name, h5, ps, ref in ROUNDS:
        p = '<h5>%s</h5>' % h5 + NL + NL.join(x if x.startswith('<ul') else '<p>%s</p>' % x for x in ps)
        if v == 'p': p += NL + reflection(*ref)
        panels.append(p)
    b42 = ('<p>The executive team gathers around a shared board or digital canvas. Each leader contributes three signals drawn directly from their PM review sheets. The process unfolds in three disciplined rounds.</p>' + NL +
           steps([r[0] for r in ROUNDS], panels, num='Round') + NL +
           '<p>Many organisations conduct performance reviews. Few organisations convert those reviews into collective strategic intelligence. The Enterprise Performance Intelligence Circle ensures that insights emerging from PM review sheets are brought together across functions in a structured conversation that allows the leadership team, acting as the collective intelligence for execution discipline, to observe execution as a living system.</p>')
    if v == 'p':
        b42 = b42.replace('<p>The executive team gathers', '<p>In each round, write your own contribution from your own Key Results and KPIs. The executive team gathers', 1)
        out.append(acc('4.2 &mdash; The Enterprise Performance Intelligence Circle: Three Rounds', 'Step through each round', b42))
    else:
        out.append(acc('4.2 &mdash; The Enterprise Performance Intelligence Circle: Three Rounds', 'Step through each round', b42,
            activity(REF + 'their own contribution to each of the three rounds, from their own Key Results and KPIs: progress and momentum, early warnings, execution learning.')))
    out.append('')
    b43 = NL.join(['<p>After the three rounds, a synthesis layer is added to the board. This is where the collective signals are interpreted and a shared enterprise decision is made. The circle must end with a clear enterprise decision: a concrete action agreed by the leadership team.</p>',
        '<div class="u8-h">The five questions of the Synthesis Layer</div>', '<ol class="u8-list">' + ''.join('<li>%s</li>' % q for q in SYN_Q) + '</ol>',
        '<div class="u8-h">The rules of the circle</div>', '<ul class="u8-list">' + ''.join('<li>%s</li>' % q for q in CIRCLE_RULES) + '</ul>',
        '<p>%s</p>' % ('Your group runs the full circle, with the Synthesis Layer, on its own Key Results in Section 5, Step 4.' if v == 'p' else 'Each group runs the full circle, with the Synthesis Layer, on its own Key Results in Section 5, Step 4.')])
    out.append(acc('4.3 &mdash; The Synthesis Layer: Enterprise Intelligence Decisions', 'Closing the circle', b43)); out.append('')
    # 4.4 role play
    roles = '<div class="rp-roles">' + NL + NL.join('  <div class="rp-role">' + NL + '    <div class="rp-role-title">&#128100; %s</div>' % a + NL + '    <p>%s</p>' % b + NL + '  </div>' for a, b in ROLES) + NL + '</div>'
    diag = '<h4>Accountability Loop Diagnosis</h4>' + NL + '<p>The CXO must determine whether the root cause is:</p>' + NL + '<div class="loop-diag">' + NL + NL.join('  <div class="loop-cell"><div class="loop-cell-label">%s</div><div class="loop-cell-name">%s</div><p>%s</p></div>' % c for c in CAUSES) + NL + '</div>'
    crit = '<h4>Observer Evaluation Criteria</h4>' + NL + '<div class="principle-stack">' + NL + NL.join(pcard(a, 'var(--teall)' if v == 'p' else 'var(--gold)', b, c, '') for a, b, c in CRITERIA) + NL + '</div>'
    intro44 = '<p>The Accountability Loop is practised in a role play on a set case. The leader activates the Review&ndash;Realign&ndash;Restore Cycle when a Key Result shows a Significant Gap: review the evidence, diagnose the root cause, then restore momentum.</p>'
    case = '<div class="rp-scenario">' + NL + '  <div class="rp-scenario-label">&#9658; Scenario</div>' + NL + SCENARIO + NL + '</div>'
    if v == 'p':
        how = '<div class="u8-how"><div class="u8-how-h">Portfolio work &middot; How to complete the Accountability Loop role play</div><ol>' + ''.join('<li>%s</li>' % s for s in HOW_44_P) + '</ol></div>'
        ent = NL.join([
            '<div class="u8-s5">', '  <div class="u8-s5-h"><span class="u8-s5-n">Your record of the role play</span></div>',
            '  <label class="wp-label" for="app_rootcause">The root cause diagnosed, and how you arrived at it</label><textarea class="wp-ta reflection-textarea" id="app_rootcause" style="min-height:110px;" placeholder="The root cause: accountability / skill / structural&#10;The evidence used in the conversation:&#10;How blame was avoided:&#10;How the root cause was reached:"></textarea><div class="reflection-saved" id="app_rootcause-saved"></div>',
            '  <label class="wp-label" for="app_corrective">The corrective actions agreed, with the owner and the follow-up</label><textarea class="wp-ta reflection-textarea" id="app_corrective" style="min-height:110px;" placeholder="Corrective actions agreed:&#10;1. ...&#10;2. ...&#10;3. ...&#10;Owner and follow-up: ..."></textarea><div class="reflection-saved" id="app_corrective-saved"></div>',
            '  <label class="wp-label" for="rp_score">The alignment score agreed at the close (1 to 10)</label><input type="number" min="1" max="10" step="1" class="u8-num reflection-textarea" id="rp_score" placeholder="1&ndash;10"><div class="reflection-saved" id="rp_score-saved"></div>',
            '</div>'])
        out.append(acc('4.4 &mdash; The Accountability Loop Role Play', 'Practice in class &middot; Portfolio Work', NL.join([intro44, how, case, roles, diag, crit, ent])))
    else:
        g = guide('FACILITATOR GUIDANCE — Running the role play online',
            '<p>This is class practice. Nothing is entered on the portal during the role play.</p>',
            '<ol>' + ''.join('<li>%s</li>' % s for s in [
                'Assign three roles: the CXO, the team member and the observer. Brief the observer on the four criteria.',
                'The CXO opens with the evidence and diagnoses the root cause with the team member before any corrective action is discussed.',
                'If the CXO defaults to pressure and skips diagnosis, pause and redirect: <em>&ldquo;You have identified the gap. Now diagnose the cause. Is this an accountability issue, a skill gap, or a structural constraint? What evidence do you have for that?&rdquo;</em>',
                'The CXO closes with the corrective actions, the follow-up and the alignment question.',
                'In the debrief, the observer posts in the chat the root cause diagnosed (accountability, skill or structural), the evidence for it and how the conversation met each criterion.',
                'Close each round by asking the CXO: <em>&lsquo;If you ran this conversation again, what would you change first?&rsquo;</em>']) + '</ol>')
        out.append(acc('4.4 &mdash; The Accountability Loop Role Play', 'Practice in class &middot; Portfolio Work', NL.join([intro44, g, case, roles, diag, crit]),
            activity('Participants complete Portfolio work in their own file after the role play: the root cause they diagnosed and how they reached it, the corrective actions agreed, with the owner and the follow-up, and the alignment score agreed at the close.')))
    out.append('')
    return NL.join(out)

# ═══ Section 5 · group work, Capstone work ══════════════════════════════════════════════════════════
S5_TITLE = 'Running the Review&ndash;Realign&ndash;Restore Cycle'
S5_LEAD = {'p': 'Your group runs the Review&ndash;Realign&ndash;Restore Cycle on the two Key Results it established in Unit 7, for the strategy in your team&rsquo;s Capstone Blueprint.',
           'f': 'Each group runs the Review&ndash;Realign&ndash;Restore Cycle on the two Key Results it established in Unit 7, for the strategy in its team&rsquo;s Capstone Blueprint.'}
T51, M51 = '5.1 &mdash; Five Steps on Two Key Results', 'Capstone Work'
ROLE_LIST = [('ceo', 'CEO'), ('cfo', 'CFO'), ('coo', 'COO'), ('chro', 'CHRO'), ('cto', 'CTO'), ('cmo', 'CMO')]
GAP_OPTS = ['Horizontal Coordination Gap', 'Evidence Quality Gap', 'Review Rhythm Breakdown', 'Learning Suppression Gap']
CAUSE_OPTS = ['Lack of accountability', 'Lack of skill', 'Misfit of role or structural constraint']
# PARTS: (part key, step name, confirmed name, Capstone key, record heading)
PARTS = [
    ['review', 'Review Discipline', 'Performance Measurement · Review Discipline', 'rr_review', 'Step 1 · Review Discipline'],
    ['signals', 'Progress Signals', 'Performance Measurement · Progress Signals', 'rr_signals', 'Step 2 · Progress Signals'],
    ['breakdown', 'Breakdown Risk', 'Performance Measurement · Breakdown Risk', 'rr_breakdown', 'Step 3 · Breakdown Risk'],
    ['circle', 'Enterprise Performance Intelligence Circle', 'Performance Measurement · Enterprise Performance Intelligence', 'rr_circle', 'Step 4 · Enterprise Performance Intelligence Circle'],
    ['loop', 'Accountability Loop', 'Performance Measurement · Accountability Loop', 'rr_loop', 'Step 5 · Accountability Loop'],
]
def fields():
    """[id, label, part, group, kind, placeholder]; kind: t text (needed), o optional text (circle rows), s select, n score 1 to 10."""
    F = [
        ['rv_forums', 'Review forums and the purpose of each', 'review', '', 't', 'For example: monthly Key Result review with each KPI owner; quarterly executive review across functions...'],
        ['rv_freq', 'How often each forum meets', 'review', '', 't', 'Each forum and how often it meets...'],
        ['rv_who', 'Who attends each forum', 'review', '', 't', 'The roles present at each forum...'],
        ['rv_evid', 'The evidence the KPI owner submits before each review', 'review', '', 't', 'The self-assessment against the rating scale and the evidence that supports it...'],
        ['rv_lead', 'How the leader makes the parallel assessment', 'review', '', 't', 'What the leader examines, independently, before the review conversation...'],
    ]
    for n in (1, 2):
        for k, nm in (('conf', 'Progress Confirmation'), ('warn', 'Early Warning'), ('gap', 'Significant Gap')):
            F.append(['k%d_%s' % (n, k), '%s looks like' % nm, 'signals', 'Key Result %d' % n, 't', 'What the evidence shows for this Key Result when it is a %s...' % nm])
            F.append(['k%d_%s_r' % (n, k), 'Leadership response', 'signals', 'Key Result %d' % n, 't', 'What the leader does when this signal appears...'])
    F += [
        ['bd_gap', 'The gap most likely to weaken your reviews', 'breakdown', '', 's', ''],
        ['bd_why', 'Why, with the evidence your group sees', 'breakdown', '', 't', 'Where the gap shows in your organisation, and the evidence for it...'],
        ['bd_close', 'How your executive team closes it', 'breakdown', '', 't', 'What your executive team will do so that this gap does not weaken your reviews...'],
    ]
    for r, (code, title, ph) in enumerate((('r1', 'Round 1 · Collective Trajectory', '% progress toward the Key Results and KPIs · evidence · momentum (accelerating, stable or slowing)...'),
                                           ('r2', 'Round 2 · Early Warnings', 'One or two warning signals · evidence · what each could affect...'),
                                           ('r3', 'Round 3 · Execution Learning', 'One execution learning · evidence · where it applies (function or enterprise)...'))):
        for key, role in ROLE_LIST:
            F.append(['c_%s_%s' % (code, key), role, 'circle', title, 'o', ph])
    for i, (key, q) in enumerate(zip(('sy_pattern', 'sy_repeat', 'sy_depend', 'sy_chain', 'sy_decision'), SYN_Q)):
        F.append([key, q, 'circle', 'Synthesis Layer', 't', ['The pattern your group sees...', 'The signals that repeat, and where...', 'The dependencies at risk...', 'The weakest link, and why...', 'The enterprise decision: what, who, by when...'][i]])
    F += [
        ['lp_kr', 'The Key Result your group treats as a Significant Gap', 'loop', '', 's', ''],
        ['lp_evid', 'The evidence of the gap', 'loop', '', 't', 'What the review shows: the expected progress and the actual progress...'],
        ['lp_cause', 'The root cause', 'loop', '', 's', ''],
        ['lp_how', 'How your group arrived at the root cause', 'loop', '', 't', 'The evidence and the questions that led to this root cause...'],
        ['lp_recover', 'The recovery this root cause requires', 'loop', '', 't', 'Reconnect to purpose, build capability, or realign the structure...'],
        ['lp_actions', 'The corrective actions agreed', 'loop', '', 't', '1. ...\n2. ...\n3. ...'],
        ['lp_follow', 'The owner and the follow-up', 'loop', '', 't', 'Who owns each action, and when progress is reviewed next...'],
        ['lp_score', 'The revised alignment score of the owner (1 to 10)', 'loop', '', 'n', ''],
    ]
    return F
HOW_S5 = {
    'p': ('This is group work and Capstone work. Your group takes the two Key Results it established in Unit 7, with their owners and delivery expectations, through five steps:', [
        '<strong>Step 1 · Review Discipline.</strong> Your group sets its review rhythm: the review forums, how often each meets, who attends, and the evidence the KPI owner and the leader bring to each review.',
        '<strong>Step 2 · Progress Signals.</strong> For each Key Result, your group states what counts as Progress Confirmation, Early Warning and Significant Gap, and the leadership response each requires.',
        '<strong>Step 3 · Breakdown Risk.</strong> Your group names the gap most likely to weaken its reviews, the evidence for it and how the executive team closes it.',
        '<strong>Step 4 · Enterprise Performance Intelligence Circle.</strong> Each member speaks as one executive role. Your group runs the three rounds and the Synthesis Layer, and records the enterprise decision.',
        '<strong>Step 5 · Accountability Loop.</strong> Your group takes one of the two Key Results as a Significant Gap and records the evidence, the root cause, the recovery, the corrective actions, the follow-up and the revised alignment score.'],
        ['Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it. The lesson for each step sits above its boxes.',
         'You then read your group&rsquo;s record at the foot of this section and select Confirm. Your confirmed record feeds your team&rsquo;s Capstone Blueprint.']),
    'f': ('This is group work and Capstone work. Each group takes the two Key Results it established in Unit 7, with their owners and delivery expectations, through five steps:', [
        '<strong>Step 1 · Review Discipline.</strong> The group sets its review rhythm: the review forums, how often each meets, who attends, and the evidence the KPI owner and the leader bring to each review.',
        '<strong>Step 2 · Progress Signals.</strong> For each Key Result, the group states what counts as Progress Confirmation, Early Warning and Significant Gap, and the leadership response each requires.',
        '<strong>Step 3 · Breakdown Risk.</strong> The group names the gap most likely to weaken its reviews, the evidence for it and how the executive team closes it.',
        '<strong>Step 4 · Enterprise Performance Intelligence Circle.</strong> Each member speaks as one executive role. The group runs the three rounds and the Synthesis Layer, and records the enterprise decision.',
        '<strong>Step 5 · Accountability Loop.</strong> The group takes one of the two Key Results as a Significant Gap and records the evidence, the root cause, the recovery, the corrective actions, the follow-up and the revised alignment score.'],
        ['The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
         'Each member then reads the group&rsquo;s record at the foot of the section and selects Confirm. The confirmed record feeds the team&rsquo;s Capstone Blueprint.']),
}
HOW_STEP_P = [
    ['Read your Unit 6 review cadence, shown above the boxes.', 'Name each review forum your executive team will hold for the strategy, and its purpose.', 'State how often each forum meets and who attends.', 'State the evidence the KPI owner submits before each review.', 'State how the leader makes the parallel assessment.'],
    ['Read your two Key Results, as your group established them in Unit 7.', 'For each Key Result, state what the evidence shows when it is a Progress Confirmation, and the leadership response.', 'Do the same for an Early Warning and for a Significant Gap.'],
    ['Choose the gap most likely to weaken your group&rsquo;s reviews.', 'State why, with the evidence your group sees in its organisation.', 'State how your executive team closes it.'],
    ['Each member takes one executive role: CEO, CFO, COO, CHRO, CTO or CMO. Fill the rows of the roles your members take; each round needs at least two roles.',
     'Round 1: each role posts in the chat its progress toward its Key Results and KPIs, the evidence and the momentum. The scribe types each entry under the role.',
     'Round 2: each role posts one or two early warning signals and the evidence.', 'Round 3: each role posts one execution learning and the evidence.',
     'Your group then answers the five questions of the Synthesis Layer and records the enterprise decision. Base each entry on your two Key Results and on the evidence your Unit 6 scorecards would produce.'],
    ['Choose the Key Result your group treats as a Significant Gap.', 'State the evidence of the gap.', 'Choose the root cause and state how your group arrived at it.', 'State the recovery the root cause requires.',
     'State the corrective actions agreed, the owner and the follow-up.', 'Record the revised alignment score the owner gives once the actions are agreed.'],
]
LESSON = [
    [('From part 1.3 · Review', 'The KPI owner conducts a first-level self-assessment against the rating scale and submits verifiable evidence. At the same time, the leader conducts a parallel assessment. Three questions anchor the review: Did the agreed activity actually occur? Did the activity produce the expected progress toward the target? What does the available evidence tell us about execution reality?'),
     ('From part 3.1 · The Review Rhythm Breakdown', 'Healthy performance measurement requires a predictable organisational rhythm. Leaders know when reviews will occur. KPI owners know when evidence must be prepared. Teams expect progress to be examined regularly.')],
    [('From part 2.3 · Progress Confirmation', 'The KPI is moving steadily toward its target within the expected timeline. Leadership response: reinforce the behaviours and decisions that generated the progress.'),
     ('From part 2.3 · Early Warning', 'Progress is slowing, but the gap is still small enough that recovery remains possible. Leadership response: intervene while there is still time to adjust course.'),
     ('From part 2.3 · Significant Gap', 'There is a significant gap between expected progress and actual progress. Leadership response: activate the Accountability Loop and diagnose before prescribing.')],
    [('From part 3.1 · The four gaps', '<span class="u8-gl">' + ''.join('<span><b>%s</b> %s</span>' % (g[1].replace('The ', ''), g[3]) for g in GAPS) + '</span>')],
    [('From part 4.2 · The three rounds', 'Round 1, Collective Trajectory: % progress, evidence, momentum. Round 2, Early Warnings: one or two evidence-based signals. Round 3, Execution Learning: one key learning, with its evidence.'),
     ('From part 4.3 · The rules of the circle', ' '.join(CIRCLE_RULES))],
    [('From part 1.3 · Realign', 'Lack of accountability: reconnect purpose and ownership. Lack of skill: targeted coaching, peer support, formal training, or timeline adjustment. Misfit of role or structural constraint: structural alignment discussion, task redistribution, or repositioning. The performance conversation remains separate from the role conversation.'),
     ('From part 1.3 · Restore', 'Corrective actions are defined clearly, specific next steps are agreed, responsibilities are reaffirmed and follow-up timelines are established. The alignment state of the Key Result is updated.')],
]
COMPLETES_F = [
    ['the review forums and the purpose of each', 'how often each forum meets and who attends', 'the evidence the KPI owner submits before each review', 'how the leader makes the parallel assessment'],
    ['for each of the two Key Results: what Progress Confirmation, Early Warning and Significant Gap look like', 'the leadership response to each signal'],
    ['the gap most likely to weaken the group&rsquo;s reviews', 'why, with the evidence', 'how the executive team closes it'],
    ['Rounds 1 to 3, one entry for each executive role a member takes', 'the five questions of the Synthesis Layer, ending with the enterprise decision'],
    ['the Key Result treated as a Significant Gap and the evidence of the gap', 'the root cause and how the group arrived at it', 'the recovery, the corrective actions, the owner and the follow-up', 'the revised alignment score'],
]
GUIDE_S5_F = [
    '<strong>Order:</strong> all five steps are group work. Steps 2 and 5 use the group&rsquo;s two Key Results, so each group confirms its Unit 7 record (part 5.1) first. Step 1 shows the group&rsquo;s Unit 6 review cadence.',
    '<strong>Step 4 online:</strong> each member speaks as one executive role. In each round, every role posts its entry in the chat; the scribe types it under the role, and every member then types the agreed entries into their own page.',
    '<strong>What the group builds:</strong> the confirmed record of the five steps feeds Capstone boxes 8A to 8E. Capstone work is reviewed independently at graduation.',
]
ACT_S5_F = 'Participants work as a group in part 5.1 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'

# ═══ Unit Summary ════════════════════════════════════════════════════════════════════════════════════
SUM_P = [
    ('Awareness — What', 'What Was Established', 'You saw that performance measurement is an execution visibility discipline. Strategy fails at the level of visibility, so the discipline moves the question from “What work was done?” (activity) to “What changed because of the work?” (progress). It serves four strategic purposes: Visibility, Accountability, Learning and Course Correction. It operates through the Review–Realign–Restore Cycle: Review establishes evidence-based visibility (the KPI owner’s self-assessment and the leader’s parallel assessment against three anchor questions); Realign activates the Accountability Loop when a gap appears, diagnosing one of three root causes (lack of accountability, lack of skill, or structural misfit), each with its own recovery; Restore converts insight into corrective actions, reaffirmed ownership and follow-up timelines.'),
    ('Intelligence — Why', 'Why It Matters', 'You saw that execution velocity is set by the discipline of review conversations. Execution discipline is the habit of repeatedly examining progress, confronting evidence honestly and adjusting before small deviations become systemic failures. When the review rhythm weakens, four predictable consequences follow: early warning signals are missed; accountability gradually diffuses (KPIs drift from operational to aspirational); organisational learning is lost (results recorded but never understood); and leadership credibility erodes (priorities look symbolic). Healthy reviews produce three progress signals, each needing a different response: Progress Confirmation (reinforce what worked), Early Warning (intervene while recovery is still possible, the real return of a review rhythm) and Significant Gap (activate the Accountability Loop and diagnose the root cause).'),
    ('Extrapolating — Where', 'Where It Breaks Down', 'You saw that performance measurement breaks down in how leaders review and interpret measurement together. Four characteristic fractures weaken the collective discipline: the Horizontal Coordination Gap (reviews happen inside functions, so each function reports progress while the enterprise outcome stays inconsistent); the Evidence Quality Gap (weak or late evidence turns reviews into debates about whether the data can be trusted); the Review Rhythm Breakdown (infrequent or irregular reviews let small deviations accumulate); and the Learning Suppression Gap (evaluation-only conversations make people defend results and leave causes unexplored). The leadership team, acting as the collective intelligence for execution discipline, closes these by introducing cross-functional reviews, insisting on verifiable evidence, protecting a consistent rhythm, and balancing accountability with curiosity.'),
    ('Integration — Collective', 'What Was Built', 'You saw that at enterprise level no single function can safeguard measurement integrity alone, so the executive collective runs the Enterprise Performance Intelligence Circle around a shared question: “Is the chain of execution across our functions holding together?” Each leader contributes three signals drawn from their PM review sheets across three disciplined rounds: Collective Trajectory (progress, evidence, momentum), Early Warnings (subtle indicators that often prove to be cross-functional dependencies) and Execution Learning. A Synthesis Layer then converts the rounds into the enterprise decision. You also practised the Accountability Loop in a role play on a set case.'),
    ('Application — In Practice', 'What You Applied', 'Your group ran the Review–Realign–Restore Cycle on the two Key Results it established in Unit 7. You set the review rhythm, defined the three progress signals, named the breakdown risk, ran the Enterprise Performance Intelligence Circle to an enterprise decision and worked one Key Result through the Accountability Loop.'),
]
SUM_F_EDITS = [('The Collective Intelligence Circle synthesises performance insights through three rounds', 'The Enterprise Performance Intelligence Circle synthesises performance insights through three rounds')]
SUM_F_5 = ('Application — In Practice', 'Each group ran the Review–Realign–Restore Cycle on its two Unit 7 Key Results: the review rhythm, the progress signals, the breakdown risk, the circle and its enterprise decision, and one Key Result through the Accountability Loop. The confirmed record feeds the team’s Capstone Blueprint.')
CLOSE_F = 'Close with the central line of the unit: measurement becomes an execution recovery system when evidence is reviewed, gaps are diagnosed and momentum is restored. Remind participants that the group&rsquo;s confirmed Section 5 record feeds the team&rsquo;s Capstone Blueprint.'
