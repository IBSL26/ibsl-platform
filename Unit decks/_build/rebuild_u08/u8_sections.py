
# ═══ Round 2 · Carol's amendments of 12 October 2026 (13:10) ═══════════════════════════════════════
# 1.1 renamed and built out · 1.2 Purpose 03 "Execution Intelligence", Purpose 04 "Enables Timely Correction" · 1.3 "From Performance Measurement to Execution Recovery" in her text ·
# new 1.4 The Accountability Loop · 2.1 and 2.3 removed (2.2 becomes 2.1) · new 3.2 The CXO Performance Gap Contributors · 4.1 and 4.3 removed · EPIC becomes 4.1 ·
# the role play becomes 4.2 (participant: a personal case, a scripted conversation to analyse) · criterion 02 removed · Section 5: Applying the Four Consequences of Weak Review Discipline.
GUIDE_EDITS = [
    ('<p>Unit 8 closes the loop opened by Units 6 and 7. KPIs have been established,',
     '<p>Unit 8 closes the loop opened by Units 6 and 7. Key performance indicators (KPIs) have been established,'),
    ('Leaders must leave this unit understanding that measurement is an execution recovery system. The Accountability Loop role play in Application is non-negotiable: it is where the conceptual work becomes a leadership skill.</p>',
     'Leaders must leave this unit understanding that measurement is an execution recovery system. The Accountability Loop role play in part 4.2 is where the conceptual work becomes a leadership skill, and Section 5 applies the four consequences of weak review discipline to the group&rsquo;s own strategy.</p>'),
    ('through the <strong>Collective Intelligence Circle</strong>, shifting leaders', 'through the <strong>Enterprise Performance Intelligence Circle (EPIC)</strong>, shifting leaders'),
    ('did your organisation learn anything &mdash; or did it just record scores?&rdquo;', 'what did your organisation learn, and what did it only record?&rdquo;'),
    ('leaders who treat the Accountability Loop as a confrontation tool. It is a diagnostic discipline. Its purpose is to restore momentum.', 'leaders who treat the Accountability Loop as a confrontation tool. Its purpose is diagnosis and restored momentum.'),
]
GUIDE_ADD = '<p><strong>Teach EPIC horizontally:</strong> each signal is read for what it means for the other functions. The Enterprise Performance Intelligence Circle exists to surface cross-functional dependencies.</p>'

def para(*ps): return NL.join(x if x.startswith('<') else '<p>%s</p>' % x for x in ps)

# ═══ Section 1 ═══════════════════════════════════════════════════════════════════════════════════════
T11, M11 = '1.1 &mdash; The Execution Visibility Infrastructure', 'Are we actually moving closer to our Success in Practice?'
T12, M12 = '1.2 &mdash; The Four Strategic Purposes of Performance Measurement', 'Click each to explore'
T13, M13 = '1.3 &mdash; From Performance Measurement to Execution Recovery', 'The Review&ndash;Realign&ndash;Restore Cycle (R3)'
T14, M14 = '1.4 &mdash; The Accountability Loop', 'Diagnosing the source of performance gaps'
CAUSES14 = [  # (label, name, in full, recovery)
    ('Root Cause A', 'Lack of Accountability',
     'The individual understands the task but has lost the motivational connection to it. The work may feel detached from a meaningful outcome. Competing priorities may have diluted attention. Personal energy may have shifted elsewhere.',
     'Reconnect purpose and ownership. The leader revisits the broader organisational context of the KPI. The conversation reconnects the task to the enterprise outcome it supports, and the individual is reminded how their contribution fits into the wider organisational map. By restoring that line of sight, motivation and commitment can often be reactivated.'),
    ('Root Cause B', 'Lack of Skill',
     'The individual is committed but lacks the capability required to achieve the expected level. The challenge may involve technical expertise, analytical capability, leadership skills, or process knowledge that was initially underestimated.',
     'Develop capability, with no added pressure. Targeted coaching may be introduced. Peer support may be arranged. Formal training may be provided. In some cases the timeline attached to the KPI may also require adjustment if the capability development process requires additional time.'),
    ('Root Cause C', 'Misfit of Role or Structural Constraint',
     'The issue lies beyond motivation and skill development. The individual&rsquo;s strengths do not align with the specific responsibilities, or the role requires capabilities that the individual does not naturally bring to the task.',
     'Structural alignment. The task may be redistributed across the team. Responsibilities may be adjusted. In some situations the individual may be repositioned into a role that better aligns with their strengths.'),
]
GROW14 = [  # Carol, 13 October: each recovery achieved through the GROW model of Unit 7 (Goal, Reality, Options, Will)
    ['Reconnect the KPI to the enterprise outcome it supports, and agree what an alignment of 9 or 10 would look like.',
     'Explore what has drawn attention away from the KPI and how the individual now sees the target.',
     'The individual names how they will restore focus on the KPI among competing priorities.',
     'The individual restates ownership, the actions and the follow-up date, and the leader asks the alignment question again.'],
    ['Agree the result the KPI requires, the capability it calls for, and what an alignment of 9 or 10 would look like.',
     'Establish which part of the task the individual cannot yet do, and what they can already do well.',
     'Choose together among targeted coaching, peer support, formal training and an adjusted timeline.',
     'Agree the development plan, any adjusted milestones and the follow-up, and ask the alignment question again.'],
    ['Agree the outcome the KPI must deliver, whoever delivers it.',
     'Establish where the demands of the role and the strengths of the individual, or the structure around them, do not match.',
     'Consider redistributing the task, adjusting responsibilities or, in a separate role conversation, repositioning the individual.',
     'Agree the structural change, who decides it and by when, and ask the alignment question again with whoever now owns the KPI.'],
]
GROW_NAMES = ['Goal', 'Reality', 'Options', 'Will']
def grow_list(items):
    return '<ul class="u8-growl">' + ''.join('<li><b>%s</b>%s</li>' % (n, x) for n, x in zip(GROW_NAMES, items)) + '</ul>'
def sec1(v):
    you = v == 'p'
    out = [hero('Section 1 · Awareness — What', 'What is Performance Measurement?',
                'Establishing performance measurement as an execution visibility discipline and introducing the Review&ndash;Realign&ndash;Restore Cycle as the mechanism that keeps strategy correctable.'),
           '<div class="mod-body">', slo('Distinguish meaningful strategic progress from activity.', 'Explain how performance evidence converts into realignment and corrective action.'), '']
    if not you:
        out.append(guide('FACILITATOR GUIDANCE — Awareness',
            '<strong>1.1 · The Execution Visibility Infrastructure.</strong> Open with the provocation: <em>"Work is happening. Teams are busy. Initiatives are underway. But can you confidently say the work being done is actually advancing the strategy?"</em> Then teach performance measurement as the visibility infrastructure of the strategy: without it, strategy stays interpretive, each function develops its own sense of progress and activity is mistaken for advancement. The shift to land is from <em>"What work was done?"</em> to <em>"What changed because of the work?"</em>',
            '<strong>1.2 · The Four Strategic Purposes.</strong> Teach execution rhythm first: regular reviews reveal the subtle signals early and prevent the most common leadership surprise, discovering failure at the end of the reporting period. Then teach the four purposes one card at a time. Most leaders can name visibility and accountability; fewer name execution intelligence (data interpreted into decision insight through disciplined conversation) and timely correction.',
            '<strong>1.3 · From Performance Measurement to Execution Recovery.</strong> Link the four purposes to the Review&ndash;Realign&ndash;Restore Cycle (R3): Review brings together visibility, accountability and execution intelligence; Realign diagnoses the gap through the Accountability Loop; Restore activates timely correction. Name the outcome of each stage, and close on how the cycle stays continuous: the next Review checks whether the corrective actions worked.',
            '<strong>1.4 · The Accountability Loop.</strong> Start from the default response to a gap: pushing harder. The key facilitation moment is when leaders understand that most performance gaps have a diagnosable cause, and that the three root causes (accountability, skill, structural misfit) require different responses. Help leaders distinguish between team members who cannot perform and those who will not: inability needs development, and unwillingness needs accountability. Then teach how each recovery is achieved through the GROW model of Unit 7 (Goal, Reality, Options, Will), and that every recovery closes with the alignment question asked again. Close on keeping the performance conversation separate from the role conversation.'))
        out.append('')
    # 1.1
    open_ = ('Your performance management system has been set and the mechanisms for establishing performance are in place. Your commitments have been secured. Now the most important discipline of execution begins.' if you else
             'The performance management system has been set and mechanisms for establishing performance are in place. Commitments have been secured. Now the most important discipline of execution begins.')
    b11 = para(open_,
        'Strategy execution fails at the level of <strong>visibility</strong>. Performance measurement is the discipline that makes execution visible. It is the <strong>execution visibility infrastructure</strong> of the strategy: it shows whether the organisation is actually moving closer to its Success in Practice.',
        '<div class="u8-h">The pattern in many organisations</div>',
        'In many organisations, enormous effort goes into designing strategy. Leaders invest months clarifying direction, defining Objectives and Key Results (OKRs), setting targets, and aligning teams around ambitious outcomes. Scorecards are built. Key performance indicators (KPIs) are cascaded. Performance frameworks are communicated.',
        'Yet several months later, when leadership teams pause and reflect, the same uncertainty often appears. Work is happening. Teams are busy. Initiatives are underway. Leaders still cannot confidently answer a more fundamental question: <em>&ldquo;Is the work being done actually advancing the strategy?&rdquo;</em> This is the gap that performance measurement exists to close.',
        '<div class="u8-h">The visibility infrastructure</div>',
        'Performance measurement creates the visibility infrastructure that allows leaders to observe whether the organisation is genuinely progressing toward its strategic outcomes. Without this infrastructure, strategy remains largely interpretive. Each function develops its own sense of progress. Activity becomes mistaken for advancement. Energy is expended, but the connection to the enterprise result becomes difficult to see.',
        'Performance measurement restores that line of sight. It allows the organisation to move from <strong>activity visibility</strong> to <strong>progress visibility</strong>.',
        '<div class="u8-h">From activity to progress</div>',
        'Most organisations are extremely good at measuring <strong>activity</strong>: how many projects were launched, how many meetings were held, how many deliverables were completed. These indicators provide evidence that work is occurring and create a sense of operational movement. But activity alone does not indicate whether the organisation is actually moving closer to the strategic outcome it set out to achieve.',
        'Performance measurement therefore asks a different set of questions. The question moves from <em>"What work was done?"</em> to <em>"What changed because of the work?"</em> The organisation examines evidence of progress. This shift transforms performance management from an administrative reporting exercise into an <strong>execution intelligence system</strong>.')
    if you:
        out.append(acc(T11, M11, b11 + NL + reflection('ref1', 'Activity vs Progress',
            'In your function, what are you currently measuring that reflects activity? What would reflect genuine progress toward your strategic outcome?',
            'Activity measures I use:\nProgress measures I should add:'), open_=True))
    else:
        out.append(acc(T11, M11, b11, activity(REF + 'what they measure today that reflects activity, and what would reflect genuine progress toward their strategic outcome.'), open_=True))
    out.append('')
    # 1.2
    intro = para('Performance measurement creates <strong>execution rhythm</strong>. Most strategic outcomes are the result of cumulative progress built over time. Regular review cycles allow leaders to notice the subtle signals that indicate whether execution is strengthening or weakening. Momentum may begin to accelerate in one area while slowing in another. Resource constraints may appear. Decision bottlenecks may surface. Capability gaps may become visible. When these signals are visible early, leaders can respond while the situation is still manageable.',
        'This rhythm prevents the most common leadership surprise in organisations: discovering performance failure only at the end of the reporting period. Performance measurement ensures that strategy is observed while it is unfolding, as well as evaluated after the fact.',
        'At its core, performance measurement serves four strategic purposes within the organisation. Select each to explore%s' % (', and ask yourself where your organisation is strongest and where it is weakest.' if you else '.'))
    cards = [
        pcard('Purpose 01', '#8ab0e8', 'Creates Visibility', 'Leaders can observe where the organisation is gaining momentum and where it is stalling. Strategic priorities that once existed only as intentions begin to appear as measurable progress signals. Without measurement, leaders are flying blind: confident in effort but uncertain about direction.',
              ask(v, 'Where in your organisation is execution happening in the dark? Where are you most likely to be surprised at the end of a reporting period?', 'Where in your organisation does execution happen in the dark? Where are you most likely to be surprised at the end of a reporting period?')),
        pcard('Purpose 02', 'var(--teall)' if you else 'var(--gold)', 'Establishes Accountability', 'Strategic completion requires tracking every component of the declared goal, including the parts that bring no visible victory. What has been accomplished is recorded as evidence that commitments are being kept. Leaders and teams understand which part of the strategy they are responsible for advancing.</p><p>Accountability without measurement is aspiration without a feedback loop: it depends entirely on personal commitment, with no organisational structure behind it.',
              ask(v, 'If your key performance indicators (KPIs) disappeared from your scorecard but the targets remained unchanged, how many would still be actively owned?', 'If your KPIs disappeared from your scorecard but the targets remained unchanged, how many would still be actively owned?')),
        pcard('Purpose 03', '#5ecba1', 'Execution Intelligence', 'At this point, performance measurement begins to evolve beyond data collection. It becomes execution intelligence. Data on its own rarely improves performance. Numbers simply describe what has happened. Insight emerges only when those numbers are interpreted through disciplined conversation. Performance measurement therefore transforms data into decision insight.</p><p>Each review cycle helps leaders answer three essential questions:</p><ol><li>What progress has been achieved since the last review?</li><li>What obstacles are preventing further progress?</li><li>What adjustment will restore momentum toward the target?</li></ol><p>Through these conversations, performance management becomes a learning system. Teams develop a deeper understanding of how strategy unfolds in practice. Leaders strengthen their ability to guide execution through uncertainty and complexity.',
              ask(v, 'What did your organisation actually learn from its last strategy cycle? What did it learn about how execution works inside your system?', 'What did your organisation actually learn from its last strategy cycle? What did it learn about how execution works inside your system?')),
        pcard('Purpose 04', '#c39de0', 'Enables Timely Correction', 'Early signals allow teams to intervene while progress is still recoverable. Problems are addressed when they are small enough to resolve. Without early signals, problems are discovered only when targets have already been missed.</p><p>This purpose is why measurement frequency matters: a signal detected in week four carries a different cost from the same signal detected in week twelve.',
              ask(v, 'What is the average gap in your organisation between when a performance problem begins and when leadership first becomes aware of it?', 'What is the average gap in your organisation between when a performance problem begins and when leadership first becomes aware of it? What does that gap cost?')),
    ]
    out.append(acc(T12, M12, intro + NL + '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>')); out.append('')
    # 1.3 · Carol's text
    lead12 = 'In part 1.2, you saw that performance measurement serves four strategic purposes' if you else 'Part 1.2 established that performance measurement serves four strategic purposes'
    stage1 = para('<h5>Stage 1 &mdash; Review: Establish Execution Reality</h5>',
        'Review brings together the first three purposes of performance measurement: visibility, accountability and execution intelligence.',
        'The KPI owner assesses progress against agreed targets and submits evidence of what has been achieved. The leader independently reviews the same KPI, bringing a broader organisational perspective. Together, they establish a shared understanding of execution reality.',
        '<p><strong>Three questions guide the conversation:</strong></p>',
        '<ol><li>What progress has been achieved against the agreed target?</li><li>What does the evidence tell us about performance?</li><li>Where is actual progress falling short of expectations?</li></ol>',
        '<div class="sig-action"><strong>Outcome:</strong> A shared, evidence-based understanding of progress and any emerging performance gaps.</div>')
    stage2 = para('<h5>Stage 2 &mdash; Realign: Diagnose and Address Execution Gaps</h5>',
        'Once Review establishes where progress is falling short, Realign determines what is preventing the expected performance.',
        'The leader activates the S2R&reg; <strong>Accountability Loop</strong> (part 1.4) to investigate whether the gap arises from:',
        ul(['<strong>Ownership:</strong> the individual understands the responsibility but has lost connection to its purpose or accountability.',
            '<strong>Capability:</strong> the individual is committed but lacks the skills or support required to deliver.',
            '<strong>Role or structural constraints:</strong> the responsibilities, resources or organisational conditions are preventing effective execution.']),
        'The leader and KPI owner identify an appropriate intervention, which may include renewed ownership, coaching, additional support or structural adjustments.',
        '<div class="sig-action"><strong>Outcome:</strong> A clear understanding of the underlying performance constraint and an agreed corrective response.</div>')
    stage3 = para('<h5>Stage 3 &mdash; Restore: Rebuild Execution Momentum</h5>',
        'Restore activates the fourth purpose of performance measurement: timely correction.',
        'The agreed intervention is translated into concrete execution commitments. The leader and KPI owner establish what must happen next, who is responsible and when progress will be reviewed. At this stage, they:',
        ul(['Agree on corrective actions and expected progress.', 'Reaffirm responsibilities and accountability.', 'Establish follow-up timelines and support requirements.', 'Update the KPI alignment state to reflect whether clarity, capability and ownership have been restored.']),
        'Restoring momentum requires renewed commitment to the intended outcome, supported by the conditions necessary to achieve it.',
        '<div class="sig-action"><strong>Outcome:</strong> A clear recovery pathway, renewed execution ownership and agreed follow-through.</div>')
    b13 = para('%s: creating visibility, establishing accountability, generating execution intelligence and enabling timely correction. These four purposes work together to help leaders understand how strategy is progressing and where intervention is required.' % lead12,
        'But identifying a performance gap does not automatically resolve it. Leaders need a disciplined process for interpreting what the evidence reveals, identifying what needs attention and ensuring that corrective decisions translate into improved execution.',
        'Within the S2R&reg; system, this process is called the <strong>Review&ndash;Realign&ndash;Restore Cycle (R3)</strong>. The cycle provides a recurring leadership rhythm through which performance evidence is examined, execution gaps are addressed and progress is restored.',
        steps(['Review', 'Realign', 'Restore'], [stage1, stage2, stage3]),
        '<div class="u8-h">How the cycle remains continuous</div>',
        'The next Review examines whether the corrective actions have produced the expected improvement. If gaps remain, the cycle continues until execution returns to the required trajectory.')
    out.append(acc(T13, M13, b13)); out.append('')
    # 1.4 · the Accountability Loop
    cards14 = [pcard(a, ['#f0a070', '#8ab0e8', '#c39de0'][i], b, c + '</p><p><strong>Recovery:</strong> ' + d + '</p><p><strong>Achieving the recovery through GROW:</strong>', grow_list(GROW14[i])) for i, (a, b, c, d) in enumerate(CAUSES14)]
    b14 = para('Many organisations respond to performance gaps with one default response: they push harder. More urgency is applied. More pressure is introduced. Deadlines are reinforced. Pressure alone rarely solves execution challenges because pressure does not identify the underlying cause of the problem.',
        'When a gap is identified, the leader activates the <strong>Accountability Loop</strong>: a structured diagnostic process designed to restore traction and ownership without collapsing into unproductive performance pressure. Most performance gaps emerge from one of three underlying conditions, and each calls for its own recovery.',
        'The leader achieves the recovery through the <strong>GROW model</strong> %s for the Alignment Dialogue in Unit 7: <strong>Goal</strong>, <strong>Reality</strong>, <strong>Options</strong> and <strong>Will</strong>. The goal of the conversation is ownership of the KPI: an alignment score of 9 or 10. Select each root cause to explore its recovery.' % ('you used' if you else 'participants used'),
        '<div class="principle-stack">' + NL + NL.join(cards14) + NL + '</div>',
        '<div class="u8-h">Keep the two conversations separate</div>',
        'The performance conversation must remain separate from the role conversation. Performance discussions focus on progress toward outcomes. Role alignment discussions focus on placing individuals where their capabilities can generate the greatest organisational value. By maintaining this distinction, the organisation protects both fairness and clarity.',
        QUOTE % ('1.05rem', 'The correct root cause determines the correct recovery action: pressure alone will not solve a skill gap, and coaching will not solve a structural misfit.'))
    if you:
        out.append(acc(T14, M14, b14 + NL + reflection('ref2', 'The Cycle and the Loop in Your Organisation',
            'Think of a current performance gap in your function. Which stage of the Review&ndash;Realign&ndash;Restore Cycle is it in? If you activated the Accountability Loop, which root cause would you most likely be diagnosing, and why?',
            'The gap:\nThe stage it is in:\nThe root cause I would most likely diagnose, and why:')))
    else:
        out.append(acc(T14, M14, b14, activity(REF + 'one current performance gap in their function, the stage of the Review&ndash;Realign&ndash;Restore Cycle it sits in, and the root cause they would most likely diagnose.')))
    out.append('')
    return NL.join(out)

# ═══ Section 2 · only the four consequences remain (2.1 and 2.3 removed) ════════════════════════════
SLO2 = ('Explain why review discipline determines the pace of execution.', 'Recognise the early signs that review discipline is weakening and the cost each carries.')
CONSEQ = [  # (number, name, text, participant question, facilitator prompt, short name, signal line for Section 5)
    ('Consequence 01', 'Early Warning Signals Are Missed', 'Execution rarely collapses suddenly. Performance deterioration typically begins with small, subtle indicators: a milestone that slips by a few days, a process bottleneck beginning to slow delivery, a capability gap emerging in one team, a dependency between functions that introduces unexpected delays. These signals often appear months before the final KPI target is at risk. But if leaders are not regularly examining performance evidence, these signals remain invisible. By the time the problem becomes visible at the end of the reporting period, the opportunity for early intervention has already been lost.',
     'In your experience, what is the typical lag between when a performance problem begins and when leadership acts? What would closing that lag by half be worth?', 'In your experience, what is the typical lag between when a performance problem begins and when leadership acts? What would closing that lag by half be worth to your organisation?', 'Early Warning Signals'),
    ('Consequence 02', 'Gradual Diffusion of Accountability', 'Accountability is sustained through visibility. When review conversations disappear or become irregular, the psychological signal shifts. Targets remain written on the scorecard, but they no longer appear in leadership dialogue. KPI owners begin to interpret the absence of review as an indication that the target is no longer an active organisational priority. The KPI quietly moves from being operational to being aspirational. Work continues, but the urgency associated with the strategic outcome begins to fade. People assume progress is occurring somewhere in the system, yet no one feels the immediate responsibility to ensure that it actually is.',
     'Which KPIs in your current scorecard are operational and which have quietly become aspirational? What made the difference?', 'Which KPIs in your current scorecard are operational and which have quietly become aspirational? What made the difference?', 'Accountability'),
    ('Consequence 03', 'Loss of Organisational Learning', 'Every review conversation contains valuable insight about which approaches accelerate progress, where operational friction exists, and which cross-functional dependencies are working and which are slowing things down. When review conversations are reduced to occasional reporting exercises, results are recorded but the organisation never pauses to understand why those results occurred. Without reflection, improvement becomes accidental. The organisation&rsquo;s execution capability stagnates even as it accumulates more strategic ambition.',
     'What does your organisation know now about how execution works inside your system that it did not know eighteen months ago?', 'What does your organisation know now about how execution works inside your system that it did not know eighteen months ago? If the answer is &lsquo;not much,&rsquo; that is a review discipline signal.', 'Organisational Learning'),
    ('Consequence 04', 'Erodes Leadership Credibility', 'When leaders set ambitious targets and communicate strategic priorities, they create an expectation that those priorities will remain visible in the leadership conversation. If those targets are not revisited through structured performance discussions, a subtle message spreads: the strategy announcement was more symbolic than operational. Teams become less attentive to new strategic commitments because they have learned that priorities often quietly fade. Consistent performance reviews counteract this by demonstrating that strategic priorities are ongoing leadership commitments.',
     'What is the current level of strategic commitment in your organisation? How much of that is shaped by what leaders consistently review, and how much by what they announce?', 'What is the current level of strategic commitment in your organisation? How much of that is shaped by what leaders consistently review, and how much by what they announce?', 'Leadership Credibility'),
]
T21, M21 = '2.1 &mdash; Four Consequences of Weak Review Discipline', 'Click each to explore'
# Carol, 13 October: execution velocity (her notes of the 2.1 slide, word for word) and a personal reflection on the velocity gap
VELOCITY = ['<div class="u8-h">Execution velocity</div>',
    'Execution velocity is the rate at which an organisation converts strategic intent into measurable results. That rate is shaped by how quickly leaders detect progress or deviation, understand its causes, make decisions and translate those decisions into action.',
    'Performance measurement provides the evidence. Review discipline converts that evidence into timely decisions.',
    'This is why organisations can have well-designed strategies, clearly assigned KPIs and detailed execution plans, yet still experience slow progress. The measures may exist, but the rhythm of examining them, resolving constraints and adjusting execution may be weak.',
    '<div class="u8-h">Four consequences of weak review discipline</div>']
REF_VEL = ('ref8', 'Where You Have Seen the Velocity Gap',
    'The velocity gap is the distance between the pace of progress you planned and the pace you achieved. Think of a strategic priority in your own setting that moved more slowly than planned while its measures were in place. Where did the velocity gap open: in detecting the deviation, understanding its cause, making the decision or translating the decision into action? Which of the four consequences followed, and what did the delay cost?',
    'The priority:\nWhere the velocity gap opened (detect / understand / decide / act):\nThe consequence that followed:\nWhat the delay cost:')
def sec2(v):
    out = [hero('Section 2 · Intelligence — Why', 'Why Performance Measurement Determines Execution Velocity',
                'Understanding why the discipline of review conversations is the factor that determines whether strategy execution sustains momentum or quietly stalls.'),
           '<div class="mod-body">', slo(*SLO2), '']
    if v == 'f':
        out.append(guide('FACILITATOR GUIDANCE — Intelligence',
            'The key shift in this section is from measurement as tool to measurement as leadership discipline. Most leaders accept the logic of measurement; fewer have internalised that the rhythm of review conversations is itself a strategic capability, and that allowing that rhythm to weaken has predictable, compounding consequences.',
            '<strong>2.1 · Execution velocity.</strong> Open with the question <em>&ldquo;What determines the velocity of the flight?&rdquo;</em> and teach execution velocity: the rate at which an organisation converts strategic intent into measurable results, shaped by how quickly leaders detect, understand, decide and act. Performance measurement provides the evidence; review discipline converts it into timely decisions.',
            '<strong>2.1 · Four Consequences of Weak Review Discipline.</strong> Teach the four consequences as one chain, one card at a time: missed early warnings lead to diffused accountability; diffused accountability suppresses learning; suppressed learning erodes leadership credibility. Ask the question on each card once the card is taught, so participants recognise the chain in their own organisations.',
            'Section 5 returns to these four consequences: each group sets two decision points against each of them.'))
        out.append('')
    red = 'rgba(231,76,60,.8)'
    cards = [pcard(n, red, nm, tx, ask(v, pq, fq)) for n, nm, tx, pq, fq, s in CONSEQ]
    b21 = (para(*VELOCITY) + NL + para('When performance reviews occur inconsistently or superficially, several predictable patterns begin to emerge. These are the foreseeable consequences of allowing the review rhythm to weaken.') + NL +
           '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>')
    if v == 'p': out.append(acc(T21, M21, b21 + NL + reflection(*REF_VEL), open_=True))
    else: out.append(acc(T21, M21, b21, activity(REF + 'where they have seen the velocity gap in their own setting: a strategic priority that moved more slowly than planned, where the gap opened (detecting the deviation, understanding its cause, making the decision or translating it into action), the consequence that followed and what the delay cost.'), open_=True))
    out.append('')
    return NL.join(out)

# ═══ Section 3 · 3.1 the four gaps (as round 1) · new 3.2 the CXO contributors ══════════════════════
T31, M31 = '3.1 &mdash; Four Fractures in Performance Measurement', 'Select each gap'
T32, M32 = '3.2 &mdash; The CXO Performance Gap Contributors', 'Is the chain of execution across our functions holding together?'
G_H, G_E, G_R, G_L = 'The Horizontal Coordination Gap', 'The Evidence Quality Gap', 'The Review Rhythm Breakdown', 'The Learning Suppression Gap'
FR = {G_H: 'Fracture 01 &middot; The Horizontal Coordination Gap', G_E: 'Fracture 02 &middot; The Evidence Quality Gap', G_R: 'Fracture 03 &middot; The Review Rhythm Breakdown', G_L: 'Fracture 04 &middot; The Learning Suppression Gap'}
CXO = [  # (role, focus, how the role reviews (p, f), [(fracture, what the role does (p, f), what happens as a result)], question)
    ('CEO', 'Enterprise Direction',
     ('As CEO, you chair the executive review: the meeting where the executive team reports progress on the Key Results of the strategy.',
      'The CEO chairs the executive review: the meeting where the executive team reports progress on the Key Results of the strategy.'),
     [(G_R, ('When the board, investors or a crisis crowd your diary, you postpone or shorten the executive review.', 'When the board, investors or a crisis crowd the diary, the CEO postpones or shortens the executive review.'),
       'Executives see that the executive review can slip, so they let the reviews with their own teams slip too. Weeks pass without anyone examining progress, and a small delay grows into a missed target before it is discussed.'),
      (G_L, ('When a target is missed, your first question in the review is: “Why did you miss it?”', 'When a target is missed, the CEO&rsquo;s first question in the review is: “Why did you miss it?”'),
       'Executives come to the review ready to defend their numbers. They hold back the obstacles they face, so the executive team never examines what caused the miss or what must change.')],
     'When did you last postpone or shorten the executive review, and what did your executives do with their own reviews in that time?'),
    ('CFO', 'Financial Precision',
     ('As CFO, you review performance through the monthly management accounts: actual results against budget and forecast.',
      'The CFO reviews performance through the monthly management accounts: actual results against budget and forecast.'),
     [(G_E, ('You use financial results as the main evidence of progress.', 'The CFO uses financial results as the main evidence of progress.'),
       'Financial results are available only after the month or quarter has closed. By the time the review sees a shortfall, the period is over and it is too late to correct it.'),
      (G_L, ('You ask each budget holder to explain every variance.', 'The CFO asks each budget holder to explain every variance.'),
       'Budget holders prepare explanations for the number. The discussion stays on justifying the past, and the operational cause of the variance is never examined.')],
     'Which evidence in your reviews shows a shortfall while there is still time to correct it?'),
    ('COO', 'Operational Discipline',
     ('As COO, you hold weekly operations reviews with your heads of operations, using strong data on throughput, service levels and process efficiency.',
      'The COO holds weekly operations reviews with the heads of operations, using strong data on throughput, service levels and process efficiency.'),
     [(G_H, ('Only operations attends your review. Sales, technology, procurement and HR, the functions operations depends on, are not in the room.', 'Only operations attends the review. Sales, technology, procurement and HR, the functions operations depends on, are not in the room.'),
       'When a delay comes from another function, for example a late system change or a supplier problem, the operations review can neither see it nor resolve it. Operations reports its own measures as on track while the enterprise result falls behind.')],
     'Which operational Key Result depends on a function that never attends your reviews?'),
    ('CHRO', 'People &amp; Culture',
     ('As CHRO, you review people performance through the annual engagement survey and the twice-yearly talent review.',
      'The CHRO reviews people performance through the annual engagement survey and the twice-yearly talent review.'),
     [(G_E, ('You report engagement scores and training completed, with no link to a Key Result.', 'The CHRO reports engagement scores and training completed, with no link to a Key Result.'),
       'The executive team cannot tell whether people measures help or hinder the delivery of the strategy, so the review debates what the survey means.'),
      (G_R, ('You review people measures once or twice a year.', 'The CHRO reviews people measures once or twice a year.'),
       'A skills gap that will delay a milestone is seen only at the next survey or talent review, after the milestone has already slipped.')],
     'Which people measure in your reviews shows its effect on a Key Result of the strategy?'),
    ('CTO/CIO', 'Technology Delivery',
     ('As CTO or CIO, you review technology projects against plan: milestones delivered, system uptime and budget.',
      'The CTO or CIO reviews technology projects against plan: milestones delivered, system uptime and budget.'),
     [(G_E, ('You report a system going live as progress.', 'The CTO or CIO reports a system going live as progress.'),
       'Going live is activity. Whether the business uses the system to deliver its Key Result is never checked, so the review reports success while the result does not move.'),
      (G_H, ('You review technology projects in the technology forum, without the business owner of the result.', 'The CTO or CIO reviews technology projects in the technology forum, without the business owner of the result.'),
       'Technology reports the project on track and the business reports the result off track, and no review puts the two together.')],
     'Which system did you report as live without evidence of the business result it was meant to enable?'),
    ('CMO', 'Market Performance',
     ('As CMO, you review marketing through campaign reports: reach, leads, brand measures and market share.',
      'The CMO reviews marketing through campaign reports: reach, leads, brand measures and market share.'),
     [(G_E, ('You report campaign reach and leads as progress toward the market Key Result.', 'The CMO reports campaign reach and leads as progress toward the market Key Result.'),
       'Reach and leads show marketing activity. They do not show whether customers bought or stayed, so the review cannot see whether the Key Result is moving.'),
      (G_H, ('Your campaigns promise delivery times and service levels that operations and sales must deliver, and they review their own measures elsewhere.', 'The campaigns promise delivery times and service levels that operations and sales must deliver, and they review their own measures elsewhere.'),
       'Marketing meets its campaign targets while customers receive a different experience, and no single review sees the broken promise.')],
     'Which of your marketing measures shows activity, and which shows movement toward a Key Result?'),
    ('CCO', 'Commercial Ambition',
     ('As CCO, you hold weekly sales reviews on pipeline, orders and revenue against target.',
      'The CCO holds weekly sales reviews on pipeline, orders and revenue against target.'),
     [(G_H, ('You review sales commitments without operations in the room.', 'The CCO reviews sales commitments without operations in the room.'),
       'Sales signs volumes that operations has not confirmed it can deliver. The gap appears only when orders arrive late and customers complain.'),
      (G_L, ('Every sales review puts pressure on the number.', 'Every sales review puts pressure on the number.'),
       'Sales managers stop raising obstacles, such as pricing or stock problems, until the quarter is already lost.')],
     'Where does your sales review assume a delivery capacity that no one in the room has confirmed?'),
    ('CPO', 'Procurement Discipline',
     ('As CPO, you review procurement through supplier scorecards, savings achieved and contract compliance.',
      'The CPO reviews procurement through supplier scorecards, savings achieved and contract compliance.'),
     [(G_H, ('You review supplier performance in the procurement forum, apart from the functions that depend on supply.', 'The CPO reviews supplier performance in the procurement forum, apart from the functions that depend on supply.'),
       'A late delivery from a supplier reaches a Key Result in operations before anyone connects the two.'),
      (G_E, ('You report savings achieved as procurement progress.', 'The CPO reports savings achieved as procurement progress.'),
       'The review rewards a cheaper contract without checking whether slower or lower-quality supply is now delaying delivery.')],
     'Which supplier delay would your reviews reveal only after it reached a Key Result?'),
    ('CRO', 'Risk Governance',
     ('As CRO, you review risk through the risk register, incident reports and compliance audits, on the board&rsquo;s governance calendar.',
      'The CRO reviews risk through the risk register, incident reports and compliance audits, on the board&rsquo;s governance calendar.'),
     [(G_L, ('You treat a reported breach as a failure to be punished.', 'The CRO treats a reported breach as a failure to be punished.'),
       'Teams stop reporting near misses, so the organisation loses the early information that would let it prevent the next incident.'),
      (G_R, ('You review risks quarterly for the board committee, apart from the strategy reviews.', 'The CRO reviews risks quarterly for the board committee, apart from the strategy reviews.'),
       'A risk that rises against a Key Result between quarters is not discussed until the next committee meeting.')],
     'What would make it safe for a team to report a near miss in your reviews?'),
    ('CSO', 'Strategic Planning',
     ('As CSO, you run the planning calendar: the annual strategy review and the quarterly OKR updates.',
      'The CSO runs the planning calendar: the annual strategy review and the quarterly OKR updates.'),
     [(G_R, ('You examine Key Results mainly at the quarterly and annual planning points.', 'The CSO examines Key Results mainly at the quarterly and annual planning points.'),
       'Three months pass between two looks at the same Key Result: too long to see whether it is moving or stalling.'),
      (G_L, ('Your planning sessions update the targets and plans for the next period.', 'The planning sessions update the targets and plans for the next period.'),
       'The plan is changed without first asking what the last period of execution taught the organisation, so the same mistakes repeat.')],
     'How many weeks pass between two reviews of the same Key Result in your organisation?'),
]
def gap_map():
    rows = []
    for g in (G_H, G_E, G_R, G_L):
        roles = [c[0] for c in CXO if any(x[0] == g for x in c[3])]
        assert roles, g
        rows.append('<div class="u8-map-r"><b>%s</b><span>%s</span></div>' % (FR[g], ' &middot; '.join(roles)))
    return '<div class="u8-map">' + ''.join(rows) + '</div>'
def sec3(v):
    you = v == 'p'
    out = [hero('Section 3 · Extrapolating — Where', 'Where Does Performance Measurement Break Down Across Functions?',
                'Examining where %s unintentionally weakens the performance measurement discipline through four characteristic fractures.' % BRIGADE),
           '<div class="mod-body">', slo('Identify where the review and interpretation of performance evidence break down across functions.', 'Assess which breakdown is most prevalent in their own organisation.'), '']
    if not you:
        out.append(guide('FACILITATOR GUIDANCE — Extrapolating',
            'Begin with the provocation: <em>"Most modern organisations have agreed goals and KPIs, dashboards, reporting tools, and performance frameworks. The breakdown usually occurs in how leaders review and interpret the measurement together."</em>',
            '<strong>3.1 · Four Fractures in Performance Measurement.</strong> Teach the four gaps as observable patterns and invite participants to place their organisation honestly on each one. The <strong>Horizontal Coordination Gap</strong> is typically the most impactful but least visible: each function may report strong progress while the enterprise outcome remains inconsistent. The <strong>Learning Suppression Gap</strong> is often the most culturally embedded and the hardest to shift, because it requires leaders to move from a judgement posture to a curiosity posture.',
            '<strong>3.2 · The CXO Performance Gap Contributors.</strong> Teach the logic of the cards first: how the role reviews performance (its meetings and its evidence), what the role does in those reviews, and what happens as a result, which opens one of the four fractures of part 3.1. Then take each participant&rsquo;s own role first and the two roles closest to it. Ask participants to post in the chat one habit in their own reviews and the fracture it opens. The question that runs through the part is <em>&ldquo;Is the chain of execution across our functions holding together?&rdquo;</em>'))
        out.append('')
    # 3.1 as before
    cards = []
    for num, title, short, mean, ps, fq in GAPS:
        extra = ('      <div class="gap-fac">Facilitator question: &ldquo;%s&rdquo;</div>' % fq + NL) if not you else ''
        cards.append('  <div class="gap-card" onclick="toggleGap(this)">' + NL +
                     '    <div class="gap-head"><div class="gap-meta"><div class="gap-num">%s</div><div class="gap-title">%s</div></div><div class="gap-arr">&#9660;</div></div>' % (num, title) + NL +
                     '    <div class="gap-bar"></div>' + NL + '    <div class="gap-body">' + NL + NL.join('      <p>%s</p>' % p for p in ps) + NL + extra + '    </div>' + NL + '  </div>')
    body = ('<p>Performance measurement is ultimately a <strong>leadership conversation discipline</strong>. Most organisations have agreed goals and KPIs; the breakdown usually occurs in <strong>how leaders review and interpret the measurement together</strong>. When that discipline weakens, several predictable fractures appear across the organisation. Select each gap below to examine where it occurs and what it costs.</p>' + NL +
            '<div class="gap-grid">' + NL + NL.join(cards) + NL + '</div>')
    if you:
        sel = ''.join('<div class="score-row"><span class="score-lt">0%d</span><span class="score-tm">%s</span><select class="score-sel" data-key="ref4" data-idx="%d" onchange="syncScores(\'ref4\')"><option value="">&ndash;</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></div>' % (i + 1, g[2], i) + NL for i, g in enumerate(GAPS))
        refb = ('<div class="ref-block" style="margin-top:16px;"><div class="ref-label">&#x270E; Reflection &mdash; Which Gap Is Most Prevalent in Your Organisation?</div>'
                '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">Rate each gap in your organisation (1 = rare, 5 = common). Then name the gap you are most responsible for closing and your first action.</p>' + NL +
                '<div class="score-grid" data-key="ref4">' + NL + sel + '</div>' + NL +
                '<label class="score-notes-lbl" for="ref4_notes">The gap I am most responsible for closing &amp; my first action</label>' + NL +
                '<textarea class="score-notes" id="ref4_notes" data-key="ref4" oninput="syncScoresDebounced(\'ref4\')" placeholder="The gap I am most responsible for closing: ...&#10;First action I will take: ..."></textarea>' + NL +
                '<textarea id="ref4" class="reflection-textarea" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="ref4-saved"></div><button class="ref-save" onclick="scoreSaveBtn(this,\'ref4\')">Save Reflection</button></div>')
        out.append(acc(T31, M31, body + NL + refb, open_=True))
    else:
        out.append(acc(T31, M31, body, activity(REF + 'a rating of each of the four gaps in their organisation, from 1 (rare) to 5 (common), and the gap they are most responsible for closing.'), open_=True))
    out.append('')
    # 3.2 the CXO contributors (NEW content, in the style of the Unit 7 role cards)
    tiles = NL.join('<div class="u8-cx-card%s" onclick="showU8Cxo(this,\'u8cx%d\')"><div class="u8-cx-top"><div class="u8-cx-role">%s</div><div class="u8-cx-name">%s</div></div><div class="u8-cx-bar"></div></div>' % (' active' if i == 0 else '', i, c[0], c[1]) for i, c in enumerate(CXO))
    det = []
    for i, (role, focus, how_, links_, q) in enumerate(CXO):
        rl = role.replace('CTO/CIO', 'CTO or CIO')
        links = ''.join('<div class="u8-cx-link"><div class="u8-cx-gname">%s</div><div class="u8-cx-step"><span>1</span><div><b>%s</b>%s</div></div><div class="u8-cx-step"><span>2</span><div><b>What happens as a result</b>%s</div></div></div>' % (FR[g], 'What you do' if you else 'What the %s does' % rl, d[0] if you else d[1], r) for g, d, r in links_)
        qline = ('<div class="cm-q">Ask yourself: %s</div>' % q) if you else ('<div class="u8-fask"><b>Question for participants</b>%s</div>' % q)
        det.append('<div id="u8cx%d" class="u8-cx-detail%s"><div class="u8-cx-col"><h5>%s</h5><p>%s</p></div><div class="u8-cx-col"><h5>How it feeds the fractures in performance measurement</h5><div class="u8-cx-links">%s</div></div>%s</div>' % (i, ' visible' if i == 0 else '', 'How you review performance' if you else 'How the %s reviews performance' % rl, how_[0] if you else how_[1], links, qline))
    how = ('<div class="u8-how"><div class="u8-how-h">How to read each card</div><ol>'
           '<li><strong>%s.</strong> The review meetings and the evidence the role uses to track performance.</li>'
           '<li><strong>%s.</strong> A habit in those reviews.</li>'
           '<li><strong>What happens as a result.</strong> How the habit opens one of the four fractures in performance measurement of part 3.1.</li>'
           '</ol></div>') % (('How you review performance', 'What you do') if you else ('How the role reviews performance', 'What the role does'))
    intro = para('The four fractures of part 3.1 rarely begin with one leader. Each executive role reviews performance in its own meetings and with its own evidence, and the habits in those reviews open one or two of the fractures. When these habits are not seen together, the chain of execution across functions weakens without anyone noticing.',
                 how,
                 ('Explore your own role first, then the two roles closest to yours.' if you else 'Teach each participant&rsquo;s own role first, then the two roles closest to it.'))
    body32 = (intro + NL + '<div class="u8-cx-grid">' + NL + tiles + NL + '</div>' + NL + NL.join(det) + NL +
              '<div class="u8-h">Where the four fractures most often begin</div>' + NL + gap_map() + NL +
              para('No single role opens a fracture alone. The leadership team, acting as the collective intelligence for execution discipline, closes the four fractures when each leader sees how the habits in their own reviews feed them, and the executive team reviews the chain of execution together.'))
    out.append(acc(T32, M32, body32)); out.append('')
    return NL.join(out)

# ═══ Section 4 · 4.1 EPIC · 4.2 the Accountability Loop role play ═══════════════════════════════════
T41, M41 = '4.1 &mdash; The Enterprise Performance Intelligence Circle (EPIC)', 'Select each signal'
T42 = '4.2 &mdash; The Accountability Loop Role Play'
M42 = 'Practice in class &middot; Portfolio Work'
SLO4 = ('Interpret individual performance signals within a shared enterprise view of progress.', 'Determine the root cause of underperformance and the leadership action it requires.')
CRITERIA3 = [CRITERIA[0], ('Criterion 02',) + CRITERIA[2][1:], ('Criterion 03',) + CRITERIA[3][1:]]
SCENARIO2 = ('<p>You are a CXO responsible for the Objective and Key Result (OKR): <strong>&ldquo;Reduce customer complaint resolution time from 48 hours to 12 hours.&rdquo;</strong> The Key Result supports the enterprise Objective of improving customer retention.</p>' + NL +
             '<p>At the start of the quarter, in the Alignment Dialogue, the Head of Customer Service rated their alignment with this Key Result at <strong>9</strong>. The latest Review of the Review&ndash;Realign&ndash;Restore Cycle shows that progress has stalled at <strong>36 hours</strong>, six weeks before the deadline, and that alignment has fallen. You must now activate the Accountability Loop to determine which of the three root causes is behind the gap.</p>')
SCENARIO_P = ('<p>The CXO, the Chief Operating Officer, is responsible for the Objective and Key Result (OKR): <strong>&ldquo;Increase on-time delivery of customer orders from 82% to 95%.&rdquo;</strong> The Key Result supports the enterprise Objective of improving customer retention.</p>' + NL +
              '<p>At the start of the quarter, in the Alignment Dialogue, the Head of Logistics rated their alignment with this Key Result at <strong>9</strong>. The latest Review of the Review&ndash;Realign&ndash;Restore Cycle shows that on-time delivery has stalled at <strong>87%</strong>, six weeks before the deadline, and that alignment has fallen. The CXO activates the Accountability Loop to determine which of the three root causes is behind the gap.</p>')
DIALOGUE = [  # Portfolio case (a different case from the class role play) · CXO = the Chief Operating Officer; HL = the Head of Logistics who owns the Key Result. The root cause is never named.
    ('CXO', 'Thank you for making time. Let us start with the evidence. Your self-assessment rates the on-time delivery Key Result at 2, and so does mine. On-time delivery is at 87%. We started at 82%, and the target is 95%, six weeks from now.'),
    ('HL', 'Yes. We reached 87% in the first two months. Since then it has not moved.'),
    ('CXO', 'When we agreed this Key Result at the start of the quarter, you rated your alignment at 9. On a scale of 1 to 10, where is it today?'),
    ('HL', 'A 5, if I am honest.'),
    ('CXO', 'What has moved it from 9 to 5?'),
    ('HL', 'Since March, most of my week has gone to the warehouse move. The CEO asked me to lead the move to the northern warehouse, and that is where the pressure is. My shift supervisors run the daily dispatch meetings now. I read their summaries when I can.'),
    ('CXO', 'Which of the agreed activities have been carried out?'),
    ('HL', 'The route planning software is live, the two extra drivers have started and the new carrier contracts are signed. The loading schedule redesign is behind. I built the first version of the schedule myself in the first month, and that is what took us from 82% to 87%. The next version needs a few days of my time with the dispatch data, and I have not given it those days.'),
    ('CXO', 'Do you have what you need to finish it?'),
    ('HL', 'Yes. The team has the people, and the system gives me all the data I need. Running dispatch is the job I know best.'),
    ('CXO', 'How do you see the 95% target now?'),
    ('HL', 'Honestly, it has started to feel like a head office number. The warehouse move is what the CEO asks about every week. Nobody has asked me about on-time delivery since the quarter started.'),
    ('CXO', 'The 95% matters, and I need the loading schedule redesign done. From next week I will add on-time delivery to the weekly operations report, so the number is in front of everyone.'),
    ('HL', 'I will try to fit it in around the warehouse move.'),
    ('CXO', 'Good. Have the redesign live in three weeks. We will look at the number again at the end of the month.'),
    ('HL', 'Understood.'),
]
SPEAKER = {'CXO': 'CXO &middot; Chief Operating Officer', 'HL': 'Head of Logistics &middot; owner of the Key Result'}
def dialogue_html():
    return ('<div class="u8-dlg">' + NL + NL.join('<div class="u8-dlg-r u8-dlg-%s"><b>%s</b><p>%s</p></div>' % (s.lower(), SPEAKER[s], l) for s, l in DIALOGUE) + NL + '</div>')
GROW42 = [  # the GROW model applied in the Accountability Loop (Unit 7 wording, carried into the loop)
    ('G', 'Goal', 'What the individual wants to reach. In the Accountability Loop: ownership of the Key Result again, an alignment score of 9 or 10.', '&ldquo;What would a 9 or 10 look like for you on this Key Result?&rdquo;'),
    ('R', 'Reality', 'What is true today. The leader explores what stands behind the score and the gap, and listens without defending the target.', '&ldquo;What has moved your alignment from where it was?&rdquo;'),
    ('O', 'Options', 'What could be done. The individual generates the ways forward, matched to the root cause.', '&ldquo;What could you do? What support would make the difference?&rdquo;'),
    ('W', 'Will', 'What will be done, and by whom. The actions, the owner and the follow-up are agreed, and the alignment question is asked again.', '&ldquo;With that agreed, where is your alignment now, on the scale of 1&ndash;10?&rdquo;'),
]
def grow_html():
    return ('<div class="u8-grow4">' + NL + NL.join('  <div><div class="g-l">%s</div><div class="g-n">%s</div><p>%s</p><p class="g-q">%s</p></div>' % g for g in GROW42) + NL + '</div>')
RP_FIELDS = [  # participant Portfolio work in 4.2: (key, label, placeholder)
    ('rp_review', 'Review &middot; What does the evidence show about the Key Result, and what has happened to the alignment score? Quote the lines.', 'The evidence:\nThe alignment score, then and now:\nThe lines that show it:'),
    ('app_rootcause', 'Realign &middot; Which of the three root causes is evident? Which lines point to it, and which lines rule out the other two?', 'The root cause:\nThe lines that point to it:\nThe lines that rule out the other two:'),
    ('app_corrective', 'Restore with GROW &middot; How was the GROW model used to resolve this root cause and move the alignment close to 10?', 'Goal:\nReality:\nOptions:\nWill:\nWhere the alignment ended, and why:'),
    ('rp_judge', 'Your judgement &middot; How well did the CXO apply the Accountability Loop, against the GROW model? What would you do differently?', 'Goal:\nReality:\nOptions:\nWill:\nWhat I would do differently:'),
]
HOW_42_P = ['Read the scenario, then read the conversation between the CXO and the Head of Logistics, who owns the Key Result. This case is different from the one you role played in class.',
            'Deduce which of the three root causes of part 1.4 is evident. The conversation does not name it.',
            'Use the GROW model (Goal, Reality, Options, Will) to work out how it was used to resolve the root cause and move the alignment close to 10, and to judge how the CXO ran the conversation.',
            'Answer the four questions below. Quote the lines of the conversation that support each answer.',
            'This is personal work. Your answers save as you type and go to your facilitator when you select Submit to Facilitator.']
KEY_42_F = [  # what the Portfolio conversation shows (facilitator preparation)
    '<strong>Review.</strong> Both assessments rate the Key Result at 2. On-time delivery rose from 82% to 87%, then stalled, against a target of 95%. Alignment has fallen from 9 at the Alignment Dialogue to 5.',
    '<strong>The root cause: lack of accountability.</strong> The owner&rsquo;s attention has moved to the warehouse move since March; the shift supervisors run the dispatch meetings; the owner has not given the loading schedule redesign the days it needs; the target &ldquo;feels like a head office number&rdquo;; and nobody has asked about on-time delivery this quarter. Skill is ruled out: the owner built the first loading schedule, which delivered the rise from 82% to 87%. Role or structure is ruled out: the people, the system and the data are in place, and the role fits the owner&rsquo;s strengths.',
    '<strong>The CXO against GROW.</strong> Goal: the CXO asks for the alignment score but never agrees what a 9 or 10 would look like, or reconnects the Key Result to customer retention. Reality: explored well, through open questions on the score, the activities and the target. Options: skipped; the CXO prescribes the solution and adds pressure through the weekly report, the default response that part 1.4 warns against. Will: the owner commits only to &ldquo;try to fit it in&rdquo;, the follow-up is vague and the alignment question is not asked again.',
    '<strong>A recovery that matches the root cause: reconnect purpose and ownership through GROW.</strong> Goal: reconnect the 95% to customer retention and ask what a 9 or 10 would look like. Reality: name the shift of attention and the absence of review. Options: the owner proposes how to protect the days for the redesign alongside the warehouse move. Will: the owner states the actions and dates, a weekly review is set, and the alignment question is asked again, aiming for 9 or 10.',
]
TM_BRIEF = 'You own the complaint resolution Key Result and you want the 12-hour target: customers tell you every week that waiting two days is why they leave. You check the numbers every day, and you and your team have been clearing the backlog by hand over weekends. The people and the new ticketing system are in place, and running the team is what you do well. The triage redesign is behind because you cannot tell from the routing reports which complaint types cause the delays, and you have never redesigned a process from data. Share this only when the CXO&rsquo;s questions bring it out.'
ROLE_PLAY_SHOWS = 'The role play case is built on a <strong>lack of skill</strong>: the owner is committed and the structure is in place, but the capability to redesign the process from data is missing. A recovery that matches it, through GROW: Goal, agree what a 9 or 10 would look like; Reality, establish what the owner cannot yet do; Options, the owner chooses among coaching, peer support, training and an adjusted interim milestone; Will, agree the plan, the follow-up and the alignment question again. The Portfolio case participants analyse after class is built on a different root cause.'
ROLES42 = [('CXO Role', 'Conducts the accountability conversation on the case. Opens with the evidence and the alignment score, then works through the GROW model with the team member: Goal, Reality, Options and Will. Aims to move the alignment close to 10.'),
           ('Team Member Role', 'Owns the Key Result. Responds authentically to the conversation, and may show defensiveness, uncertainty or genuine constraint.'),
           ('Observer Role', 'Notes how the CXO used each stage of the GROW model. Gives feedback after the role play and does not intervene during it.')]

EPIC_SIGNALS = [  # (tab name, the question it answers, what each leader brings, how the leader says it, examples, what the executive team sees)
    ('Collective Trajectory', 'Where are we on execution?',
     'The current percentage progress toward their Key Results and KPIs, taken from the PM ratings and evidence in their PM review sheet, and whether momentum is accelerating, stable or slowing. The percentage involves no estimate and no narrative opinion.',
     '&ldquo;We are at [X]% progress, supported by [evidence], and momentum is [accelerating, stable or slowing].&rdquo;',
     ['The COO reports that operational readiness KPIs show 72% progress toward the strategic Key Result, supported by throughput improvements and cycle-time reductions documented in the review sheets.',
      'The CFO reports that financial indicators show 65% progress toward the quarterly profitability milestone, supported by margin improvements and cost optimisation evidence.'],
     'Which functions show strong forward momentum and which show slower movement. The executive team sees the <strong>collective trajectory</strong> of strategy execution, and uneven progress becomes visible at once.'),
    ('Early Warnings', 'What is starting to break?',
     'One or two warning signals that emerged in their PM review conversations, with the evidence from the review sheets. An early warning appears before a KPI or Key Result is formally off target.',
     '&ldquo;An emerging risk is [signal], supported by [evidence].&rdquo;',
     ['An operational process beginning to slow delivery times', 'A capability gap that may affect upcoming milestones', 'A supply constraint that could delay implementation of strategic initiatives', 'A change in customer feedback signalling emerging dissatisfaction'],
     'Where a signal in one function is connected to activity in another. What looked like an isolated operational issue shows itself as a <strong>cross-functional execution dependency</strong>, and the leadership team, acting as the collective intelligence for execution discipline, can act on it before it becomes a measurable performance gap.'),
    ('Execution Learning', 'What is execution teaching us?',
     'One key learning from their PM reviews, with the evidence behind it: a capability insight, a coordination improvement, a leadership practice that strengthened execution, or a structural obstacle that slowed progress.',
     '&ldquo;A key execution learning is [insight], supported by [evidence].&rdquo;',
     ['The CHRO highlights that performance review discussions revealed a leadership capability gap affecting accountability conversations.', 'The CTO shares that system visibility improvements significantly accelerated operational decision-making.', 'The CMO highlights a pattern in customer experience data that revealed which service interactions most strongly influence trust.'],
     'How execution actually works inside the organisation. Over time, the organisation builds a body of practical <strong>execution intelligence</strong> that improves how strategy is implemented.'),
]
EPIC_PRODUCES = ['A clear snapshot of enterprise progress toward the strategic Key Results.', 'Emerging risks visible early enough for coordinated intervention.', 'Execution learning captured to strengthen future performance.']
REF_SIG = [
    None,  # Signal 1: no reflection in the tab (ref5 is reframed and sits at the foot of 4.1)
    ('ref6', 'Your Early Warning Signal', 'Which one or two early warning signals have emerged in your area? What evidence supports each, and what could it affect?', 'Warning signal 1: ...\nEvidence: ...\nPotential impact: ...\n\nWarning signal 2 (if applicable): ...'),
    ('ref7', 'Your Execution Learning', 'What is one key execution learning from your performance reviews? What evidence supports it, and does it apply to your function or to the enterprise?', 'Key execution learning: ...\nEvidence: ...\nWhere it applies (function / enterprise): ...'),
]
REF_CONV = ('ref5', 'The Conversation Type Most Difficult for Your Team', 'Which conversation type is most difficult for you and your team: reporting progress against evidence, naming an early warning, or sharing an execution learning? What makes it difficult, and what would make it easier?', 'The conversation type most difficult for us:\nWhat makes it difficult:\nWhat would make it easier:')
def sec4(v):
    you = v == 'p'
    out = [hero('Section 4 · Integration — Collective', 'Cross-Leadership Performance Intelligence',
                'Building the Enterprise Performance Intelligence Circle (EPIC): the mechanism through which the executive leadership team transforms individual performance management (PM) review signals into a shared view of enterprise execution momentum.'),
           '<div class="mod-body">', slo(*SLO4), '']
    if not you:
        out.append(guide('FACILITATOR GUIDANCE — Integration',
            'The shift in this section is from function to enterprise. The question that guides it is the question of part 3.2: <em>&ldquo;Is the chain of execution across our functions holding together?&rdquo;</em>',
            '<strong>4.1 · The Enterprise Performance Intelligence Circle (EPIC).</strong> Teach what EPIC is for before its detail: it turns the separate PM reviews of each function into one shared view of enterprise execution. Then teach the three signals each leader brings from their PM review sheet, each by the question it answers: progress, <em>&ldquo;Where are we on execution?&rdquo;</em>; early warnings, <em>&ldquo;What is starting to break?&rdquo;</em>; execution learning, <em>&ldquo;What is execution teaching us?&rdquo;</em> For each signal, teach what the leader brings, the sentence the leader uses and what the executive team sees. Progress comes first because it gives the other two their meaning.',
            'Teach the evidence rule with the examples of each signal: every signal names the PM review evidence behind it. This single discipline separates EPIC from an opinion forum.',
            '<strong>4.2 · The Accountability Loop Role Play.</strong> The section then moves from the enterprise view to one Key Result. In class, participants role play the case using the GROW model. After class, each participant analyses a scripted conversation on a different case and deduces the root cause alone. The guidance for running the role play online sits in part 4.2.'))
        out.append('')
    panels = []
    for k, (name, q, brings, says, ex, sees) in enumerate(EPIC_SIGNALS):
        p = NL.join(['<h5>Signal %d &middot; %s: &ldquo;%s&rdquo;</h5>' % (k + 1, name, q),
                     '<p><strong>What each leader brings.</strong> %s</p>' % brings,
                     '<p><strong>How each leader says it.</strong> %s</p>' % says,
                     '<p><strong>%s</strong></p>' % ('Examples:' if k != 1 else 'Examples of early warnings:'), '<ul>' + ''.join('<li>%s</li>' % x for x in ex) + '</ul>',
                     '<p><strong>What the executive team sees.</strong> %s</p>' % sees])
        if you and REF_SIG[k]: p += NL + reflection(*REF_SIG[k])
        panels.append(p)
    b41 = para('The <strong>Enterprise Performance Intelligence Circle (EPIC)</strong> is the executive team&rsquo;s structured review of enterprise execution. The question that guides EPIC is: <em>&ldquo;Is the chain of execution across our functions holding together?&rdquo;</em>',
               'Many organisations conduct performance reviews. Few organisations convert those reviews into collective strategic intelligence. EPIC ensures that insights emerging from PM review sheets are brought together across functions in a structured conversation that allows the leadership team, acting as the collective intelligence for execution discipline, to observe execution as a living system.',
               'In EPIC, each member of the executive team brings three signals from their own PM review sheet: where their Key Results stand, what is starting to break, and what execution is teaching them. Each signal answers one question, and the three are shared in that order. Progress comes first because it gives the warnings their context and the learning a system to learn about.',
               ('Select each signal. At the foot of the second and third tabs, write your own signal from your own Key Results and KPIs.' if you else 'Select each signal.'),
               steps([s_[0] for s_ in EPIC_SIGNALS], panels, num='Signal'),
               '<div class="u8-h">What EPIC produces</div>',
               '<ol class="u8-list">' + ''.join('<li>%s</li>' % x for x in EPIC_PRODUCES) + '</ol>',
               'Through this practice, performance measurement becomes the organisation&rsquo;s radar system for strategy execution.')
    if you: out.append(acc(T41, M41, b41 + NL + reflection(*REF_CONV), open_=True))
    else: out.append(acc(T41, M41, b41, activity(REF + 'their own early warning signal and execution learning, from their own Key Results and KPIs, at the foot of the second and third tabs; and, at the foot of part 4.1, the conversation type most difficult for them and their team: reporting progress against evidence, naming an early warning, or sharing an execution learning.'), open_=True))
    out.append('')
    roles = '<div class="rp-roles">' + NL + NL.join('  <div class="rp-role">' + NL + '    <div class="rp-role-title">&#128100; %s</div>' % a + NL + '    <p>%s</p>' % b + NL + '  </div>' for a, b in ROLES42) + NL + '</div>'
    diag = '<h4>Accountability Loop Diagnosis</h4>' + NL + '<p>The CXO must determine whether the root cause is:</p>' + NL + '<div class="loop-diag">' + NL + NL.join('  <div class="loop-cell"><div class="loop-cell-label">%s</div><div class="loop-cell-name">%s</div><p>%s</p></div>' % c for c in CAUSES) + NL + '</div>'
    crit = '<h4>The GROW Model in the Accountability Loop</h4>' + NL + para('The GROW model of Unit 7 is the basis for analysing the conversation. Each stage asks a question, and the individual does the thinking, so the answers reached are their own.') + NL + grow_html()
    sc = SCENARIO2 if not you else SCENARIO2.replace('You are a CXO responsible', 'The CXO, the Chief Operating Officer, is responsible').replace('You must now activate', 'The CXO must now activate')
    case = '<div class="rp-scenario">' + NL + '  <div class="rp-scenario-label">&#9658; %s</div>' % ('Scenario' if you else 'In class &middot; the role play scenario') + NL + (SCENARIO_P if you else SCENARIO2) + NL + '</div>'
    case_p = '<div class="rp-scenario">' + NL + '  <div class="rp-scenario-label">&#9658; After class &middot; the Portfolio scenario</div>' + NL + SCENARIO_P + NL + '</div>'
    if you:
        intro = para('In class, you role played a case using the GROW model. In this part, you work alone on a different case: you read a full conversation between the CXO and the owner of the Key Result, deduce which of the three root causes is evident, and use the GROW model to resolve it and to judge the conversation.')
        how = '<div class="u8-how"><div class="u8-how-h">Portfolio work &middot; How to complete the Accountability Loop case</div><ol>' + ''.join('<li>%s</li>' % s for s in HOW_42_P) + '</ol></div>'
        ent = NL.join(['<div class="u8-s5">', '  <div class="u8-s5-h"><span class="u8-s5-n">Your analysis of the conversation</span></div>'] +
                      ['  <label class="wp-label" for="%s">%s</label><textarea class="wp-ta reflection-textarea" id="%s" style="min-height:110px;" placeholder="%s"></textarea><div class="reflection-saved" id="%s-saved"></div>' % (k, l, k, esc_ph(ph), k) for k, l, ph in RP_FIELDS] + ['</div>'])
        out.append(acc(T42, M42, NL.join([intro, how, case, '<div class="u8-h">The conversation</div>', dialogue_html(), diag, crit, ent])))
    else:
        intro = para('Part 4.2 has two parts. <strong>In class</strong>, you give the scenario and participants role play the conversation using the GROW model. <strong>After class</strong>, in their own file, each participant reads a scripted conversation on a different case, deduces which of the three root causes is evident, and analyses the conversation with GROW.')
        g = guide('FACILITATOR GUIDANCE — In class: running the role play online',
            '<p>This is class practice. Nothing is entered on the portal during the role play.</p>',
            '<ol>' + ''.join('<li>%s</li>' % s for s in [
                'Give the scenario and assign three roles: the CXO, the team member and the observer.',
                'Give the team member the team member brief below, privately.',
                'Brief the observer on the GROW model: Goal, Reality, Options, Will.',
                'The CXO opens with the evidence and asks the alignment question, then works through Goal, Reality, Options and Will with the team member.',
                'If the CXO defaults to pressure, pause and redirect: <em>&ldquo;You have identified the gap. Now ask about the reality behind it before you move to options.&rdquo;</em>',
                'The CXO closes with the actions, the follow-up and the alignment question asked again.',
                'In the debrief, the observer posts in the chat how the CXO used each stage of GROW and the root cause that surfaced.',
                'Close each round by asking the CXO: <em>&lsquo;If you ran this conversation again, what would you change first?&rsquo;</em>']) + '</ol>')
        prep = ('<div class="u8-h">After class &middot; the case participants analyse in their own file</div>' + NL + para('This case is different from the role play case, and the root cause is never named in the conversation.') + NL + case_p + NL + dialogue_html() + NL +
                '<div class="u8-h">What the conversation shows</div>' + NL + '<ul class="u8-list">' + ''.join('<li>%s</li>' % x for x in KEY_42_F) + '</ul>')
        brief = '<div class="u8-brief"><b>Team member brief &middot; give privately to the team member</b><span>%s</span></div>' % TM_BRIEF
        shows = '<div class="u8-h">What the role play case is built on</div>' + NL + para(ROLE_PLAY_SHOWS)
        out.append(acc(T42, M42, NL.join([intro, g, case, roles, brief, shows, diag, crit, prep]),
            activity('After the role play, participants complete personal Portfolio work in their own file. They read a scripted conversation on a different case, deduce the root cause and analyse the conversation with the GROW model:', [
                'Review: what the evidence shows and what has happened to the alignment score.',
                'Realign: which of the three root causes is evident, the lines that point to it and the lines that rule out the other two.',
                'Restore with GROW: how the GROW model was used to resolve the root cause and move the alignment close to 10.',
                'Their own judgement of how the CXO applied the Accountability Loop against the GROW model, and what they would do differently.'])))
    out.append('')
    return NL.join(out)

# ═══ Section 5 · Applying the Four Consequences of Weak Review Discipline (group work, Capstone work) ═
S5_TITLE = 'Applying the Four Consequences of Weak Review Discipline'
S5_LEAD = {'p': 'Your group sets two decision points against each of the four consequences of weak review discipline, for the strategy in your team&rsquo;s Capstone Blueprint.',
           'f': 'Each group sets two decision points against each of the four consequences of weak review discipline, for the strategy in its team&rsquo;s Capstone Blueprint.'}
SLO5 = ('Exercise balanced judgement when performance differs from agreed expectations.', 'Determine the leadership decisions that protect the review discipline of the strategy.')
T51, M51 = '5.1 &mdash; Decision Points Against the Four Consequences', 'Capstone Work'
DP_EX = [  # an example decision point per consequence (NEW)
    'If a Key Result shows no movement across two monthly reviews, its owner presents a recovery plan at the next executive review.',
    'If a Key Result has not been discussed in an executive review for a full month, the CEO places it first on the agenda of the next review, with its owner present.',
    'If the same obstacle is reported in two functions in one quarter, the executive team names the cause and records what it changes in the way the strategy is executed.',
    'If a strategic priority is announced, the executive team fixes the date of its first review and the evidence to be brought to it in the same meeting.',
]
PARTS = [[('c%d' % (i + 1)), c[5], 'Review Discipline · %s' % c[5], ['rd_warning', 'rd_accountability', 'rd_learning', 'rd_credibility'][i], 'Consequence %d · %s' % (i + 1, c[1])] for i, c in enumerate(CONSEQ)]
def fields():
    F = []
    for i, c in enumerate(CONSEQ):
        for n in (1, 2):
            F.append(['c%d_dp%d' % (i + 1, n), 'Decision point %d' % n, 'c%d' % (i + 1), '', 't', 'If [the signal appears], then [the decision], taken by [who]...'])
    return F
HOW_S5 = {
    'p': ('This is group work and Capstone work. Section 2 taught the four consequences of weak review discipline. Here, your group guards the strategy in your Capstone Blueprint against each of them.', [
        'Your group takes the four consequences one at a time, each on its own tab. The lesson from part 2.1 sits above the boxes.',
        'For each consequence, your group writes two <strong>decision points</strong>. A decision point names the signal the executive team watches for, the decision it takes when the signal appears and who takes it.',
        'Write each decision point as one sentence: <em>&ldquo;If [the signal appears], then [the decision], taken by [who].&rdquo;</em> For example: <em>&ldquo;%s&rdquo;</em>' % DP_EX[0]],
        ['Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
         'You then read your group&rsquo;s record at the foot of this section and select Confirm. Your confirmed record feeds your team&rsquo;s Capstone Blueprint.']),
    'f': ('This is group work and Capstone work. Section 2 taught the four consequences of weak review discipline. Here, each group guards the strategy in its Capstone Blueprint against each of them.', [
        'The group takes the four consequences one at a time, each on its own tab. The lesson from part 2.1 sits above the boxes.',
        'For each consequence, the group writes two <strong>decision points</strong>. A decision point names the signal the executive team watches for, the decision it takes when the signal appears and who takes it.',
        'Each decision point is one sentence: <em>&ldquo;If [the signal appears], then [the decision], taken by [who].&rdquo;</em> For example: <em>&ldquo;%s&rdquo;</em>' % DP_EX[0]],
        ['The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
         'Each member then reads the group&rsquo;s record at the foot of the section and selects Confirm. The confirmed record feeds the team&rsquo;s Capstone Blueprint.']),
}
def how_step_p(i):
    return ['Read the lesson for this consequence. Note the signals it describes.',
            'Agree the two signals of this consequence your executive team is most likely to miss in your strategy.',
            'For each signal, write one decision point: the signal, the decision your executive team takes when it appears, and who takes it.']
def lesson5(i):
    c = CONSEQ[i]
    return [('From part 2.1 · %s' % c[1], c[2]), ('An example decision point', DP_EX[i])]
COMPLETES_F = [['two decision points against %s: for each, the signal, the decision the executive team takes when it appears and who takes it' % c[1].lower()] for c in CONSEQ]
GUIDE_S5_F = [
    '<strong>Order:</strong> the group takes the four consequences in the order of part 2.1. Recall each consequence in a sentence before the group writes its decision points.',
    '<strong>What a decision point is:</strong> one sentence that names the signal, the decision the executive team takes when it appears and who takes it. Use the example on each tab to show the shape.',
    '<strong>Online:</strong> the scribe types the agreed decision points; every member then types them into their own page.',
    '<strong>What the group builds:</strong> the confirmed record feeds the team&rsquo;s Capstone Blueprint. Capstone work is reviewed independently at graduation.',
]
ACT_S5_F = 'Participants work as a group in part 5.1 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'

# ═══ Unit Summary ═══════════════════════════════════════════════════════════════════════════════════
SUM_P = [
    ('Awareness — What', 'What Was Established', 'You saw that performance measurement is the execution visibility infrastructure of the strategy: it moves the question from “What work was done?” (activity) to “What changed because of the work?” (progress). It serves four strategic purposes: creating visibility, establishing accountability, generating execution intelligence and enabling timely correction. The Review–Realign–Restore Cycle (R3) turns these purposes into a recurring leadership rhythm: Review establishes execution reality; Realign diagnoses and addresses execution gaps; Restore rebuilds execution momentum. In Realign, the Accountability Loop diagnoses one of three root causes (lack of accountability, lack of skill, or misfit of role or structural constraint), each with its own recovery, achieved through the GROW model.'),
    ('Intelligence — Why', 'Why It Matters', 'You saw that execution velocity is set by the discipline of review conversations. When the review rhythm weakens, four predictable consequences follow: early warning signals are missed; accountability gradually diffuses (KPIs drift from operational to aspirational); organisational learning is lost (results recorded but never understood); and leadership credibility erodes (priorities look symbolic).'),
    ('Extrapolating — Where', 'Where It Breaks Down', 'You saw that performance measurement breaks down in how leaders review and interpret measurement together, through four fractures: the Horizontal Coordination Gap, the Evidence Quality Gap, the Review Rhythm Breakdown and the Learning Suppression Gap. Each executive role tends to feed one or two of them through the measures and forums it controls, so the leadership team, acting as the collective intelligence for execution discipline, asks together: “Is the chain of execution across our functions holding together?”'),
    ('Integration — Collective', 'What Was Built', 'You saw how the Enterprise Performance Intelligence Circle (EPIC) brings together three signals from each leader’s performance management (PM) review sheet: Collective Trajectory, Early Warnings and Execution Learning. You then deduced the root cause behind a fall in alignment in a full Accountability Loop conversation, and used the GROW model to plan its resolution and to judge the conversation.'),
    ('Application — In Practice', 'What You Applied', 'Your group set two decision points against each of the four consequences of weak review discipline, for the strategy in your team’s Capstone Blueprint: the signal to watch for, the decision to take when it appears and who takes it.'),
]
SUM_F = [
    ('Awareness — What', '#8ab0e8', 'Performance measurement is the execution visibility infrastructure of the strategy. It serves four strategic purposes: visibility, accountability, execution intelligence and timely correction. The Review–Realign–Restore Cycle (R3) turns them into a recurring leadership rhythm, and the Accountability Loop diagnoses the root cause of a gap.'),
    ('Intelligence — Why', 'var(--gold)', 'The rhythm of performance reviews determines execution velocity. When it weakens, early warning signals are missed, accountability diffuses, organisational learning is lost and leadership credibility erodes.'),
    ('Extrapolating — Where', '#5ecba1', 'Performance measurement weakens when reviews remain confined within functions, evidence quality is inconsistent, review rhythms become irregular, or conversations focus only on evaluation. Each executive role tends to feed one or two of these four fractures.'),
    ('Integration — Collective', '#c39de0', 'EPIC brings together three signals from each leader’s PM review sheet: collective trajectory, early warnings and execution learning. In the Accountability Loop role play, the CXO deduces the root cause behind a fall in alignment and resolves it through the GROW model.'),
    ('Application — In Practice', '#f0a070', 'Each group set two decision points against each of the four consequences of weak review discipline, for its own strategy. The confirmed record feeds the team’s Capstone Blueprint.'),
]
CLOSE_F = 'Close with the central line of the unit: measurement becomes an execution recovery system when evidence is reviewed, gaps are diagnosed and momentum is restored. Remind participants that the group&rsquo;s confirmed Section 5 record feeds the team&rsquo;s Capstone Blueprint.'
