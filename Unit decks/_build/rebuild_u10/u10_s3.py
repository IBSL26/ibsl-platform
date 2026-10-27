# -*- coding: utf-8 -*-
"""Unit 10 Section 3 · Extrapolating, as Carol gave it (27 Oct, 17:29)."""
from u10_content import acc
from u10_s2 import tbl

TITLE = 'Where Do Executive Biases Distort ESRG Operating Capabilities?'
HERO = 'Examining how executive assumptions, functional priorities and decision-making practices influence organisational operating conditions, create execution constraints and affect strategic performance.'
LO = ['Diagnose executive decision biases that distort specific ESRG components and weaken the organisational capabilities required for strategic execution.',
      'Develop evidence-based debiasing techniques that strengthen executive decision-making and prevent cross-functional operating constraints.']
GUIDE = ['Connect this section to the four execution-enabling capabilities introduced in Intelligence: Environment — Operational Readiness; Systems — Operational Flow; Resources — Delivery Capacity; Governance — Decision Responsiveness.',
         'Executives influence these capabilities through decisions within their functional portfolios. Legitimate functional priorities can introduce assumptions that affect operating conditions beyond the executive’s immediate portfolio. A decision intended to improve one function may inadvertently constrain another.',
         'For example, a CFO may reduce expenditure to protect financial performance while weakening investment required for operational continuity. A COO may standardise procedures to improve consistency while introducing unnecessary delays.',
         '<strong>Central question:</strong> Where might my executive decisions and assumptions be weakening the organisational operating capabilities required to deliver our strategy?']
APPROACH = 'For each CXO card: introduce the bias and decision; examine the two ESRG components most directly affected; trace the execution consequences; and discuss the evidence or decision adjustment required to counter the bias. Invite participants to challenge the examples and identify alternative decisions that preserve functional objectives while strengthening enterprise performance. Examples are illustrative.'
INTRO = 'Executive leaders make decisions through the responsibilities, priorities and performance expectations of their portfolios. These perspectives are necessary, but may also determine which operating conditions receive attention, which risks are underestimated and which consequences remain invisible. Each card examines a decision at the point it is made: the approval, investment, sourcing or design choice, the assumption behind it and the ESRG component it weakens.'
CAP = {'Environment':'Operational Readiness','Systems':'Operational Flow','Resources':'Delivery Capacity','Governance':'Decision Responsiveness'}
CARDS = [
 ('CEO','Enterprise Direction','Strategic Optimism',
  'The CEO approves a 30% operational expansion within 12 months, assuming existing operations can accommodate demand because current targets are being met. Current performance is mistaken for evidence of spare capacity.',
  [('Environment','Infrastructure','Existing infrastructure is assumed to have sufficient spare capacity. Increased demand may overload utilities or connectivity, causing interruptions and reducing output reliability.','Validate infrastructure capacity and reliability against projected demand before approving the expansion timetable.'),
   ('Resources','Investment','Expansion is approved without establishing full financial provision for additional operating capacity, delaying essential investment.','Establish and approve the investment requirements needed to support the expansion commitment.')],
  'Current performance does not automatically demonstrate readiness for future strategic demands.',
  'Which strategic commitment may have been approved without sufficiently validating operating readiness and investment?'),
 ('CFO','Financial Stewardship','Short-Term Cost Preference',
  'The CFO introduces aggressive expenditure reductions and postpones replacement of ageing operational equipment to protect annual financial targets, overlooking the cost of declining reliability.',
  [('Resources','Asset Availability','Deferring replacement increases breakdowns and reduces the availability of productive assets needed for planned output.','Evaluate replacement against equipment reliability, downtime costs and strategic output requirements.'),
   ('Resources','Investment','Capital expenditure is reduced without distinguishing discretionary spending from investment essential to strategic delivery.','Prioritise investment according to its contribution to sustaining strategic delivery capacity.')],
  'Immediate savings may weaken the productive capacity required to sustain enterprise performance.',
  'Where might financial savings be achieved at the expense of operating capacity?'),
 ('COO','Operational Discipline','Standardisation Fixation',
  'The COO introduces uniform procedures across branches. Every transaction follows identical verification and approval steps, irrespective of complexity or risk, increasing routine turnaround times.',
  [('Systems','Standardisation','Uniform procedures disregard differences in operational requirements and introduce unnecessary procedural steps.','Define essential controls and outputs that must be consistent while allowing appropriate process variation.'),
   ('Systems','Process Efficiency','Additional steps reduce throughput even though procedures are followed consistently.','Test procedures against turnaround and output requirements; remove unnecessary delays and duplication.')],
  'Standardisation supports consistency; process efficiency ensures consistent operations deliver without unnecessary waste.',
  'Which standardised procedure may be creating unnecessary operational friction?'),
 ('CHRO','People and Culture','People-Centred Attribution',
  'The CHRO responds to recurring service delays with more training and performance interventions, although teams are repeatedly transferring information between disconnected systems.',
  [('Systems','Integration','Disconnected workflows remain unresolved because delays are attributed primarily to employee capability.','Examine process handovers and system connectivity before choosing the performance intervention.'),
   ('Environment','Technology','Technology limitations are overlooked while resources are directed towards training.','Verify whether the technological environment supports required operational activities.')],
  'Interventions should address the operating condition actually limiting delivery.',
  'Which problem attributed to employees may stem from technology or disconnected processes?'),
 ('CTO/CIO','Technology and Information','Legacy Loyalty',
  'The CIO extends the life of the core operating system for a further three years to defer replacement cost. Transaction volumes have doubled since it was installed, and month-end processing now runs into the next working day.',
  [('Environment','Technology','System capacity no longer matches transaction volumes, causing slow processing and outages at peak times.','Test system capacity and reliability against projected strategic volumes before approving any extension.'),
   ('Resources','Investment','Replacement is deferred without a funded plan, so the investment need grows while the system constrains delivery.','Establish a funded replacement roadmap with milestones linked to strategic demand.')],
  'Deferring technology investment preserves budget only while the technology can still carry strategic demand.',
  'Which core system is being kept beyond the capacity our strategy now requires?'),
 ('CMO','Market and Customer Insight','Brand-Led Investment',
  'The CMO directs the refurbishment budget to redesigning customer-facing branches for brand impact. Service counters, queuing layouts and the back-office processes behind them stay as they were, and customer waiting times remain unchanged.',
  [('Environment','Facilities','Space is redesigned for appearance while service points, queue capacity and customer flow stay the same, so congestion continues at peak periods.','Specify the facility requirements of the service model, including service points, queue capacity and flow, before approving the design.'),
   ('Systems','Process Efficiency','The steps, handovers and waiting time behind each transaction remain untouched.','Map the end-to-end service process and fund the changes that reduce turnaround alongside the refurbishment.')],
  'Customer-facing investment creates value when the facility and the process behind it are designed for the service the strategy promises.',
  'Which customer-facing investment improved appearance while the operating conditions behind it stayed the same?'),
 ('CCO','Commercial Performance','Revenue Prioritisation',
  'The CCO signs a major contract with aggressive delivery timelines to secure revenue growth without testing process throughput and the implications of reallocating assets.',
  [('Systems','Process Efficiency','Contractual turnaround commitments exceed process throughput, producing backlogs and delayed fulfilment.','Validate throughput and turnaround capability before agreeing delivery timelines.'),
   ('Resources','Resource Utilisation','Assets are redirected to the new contract without accounting for their allocation to other strategic commitments.','Assess enterprise-wide consequences of resource reallocation before confirming obligations.')],
  'Commercial growth must be matched by operational flow and effective resource deployment.',
  'Which commercial commitment is creating pressure because operating requirements were not validated?'),
 ('CPO','Procurement and Supply','Consolidation Efficiency',
  'The CPO consolidates the supply of critical spare parts with a single supplier to secure volume discounts. No alternative source is qualified, and a supplier stock-out halts repairs for three weeks.',
  [('Resources','Asset Availability','Equipment waiting for parts stays out of service, reducing the productive assets available for planned output.','Identify critical parts and qualify an alternative source, or hold buffer stock sized to repair lead times.'),
   ('Governance','Risk Management','Supplier concentration risk is not assessed when the contract is awarded, so no mitigation exists when supply fails.','Assess supply continuity risk in every critical sourcing decision and record the agreed mitigation.')],
  'Sourcing savings hold their value when the supply that delivery depends on is protected.',
  'Which critical supply depends on a single source with no tested fallback?'),
 ('CRO','Risk and Governance','Compliance Framing',
  'The CRO’s enterprise risk register concentrates on financial, regulatory and fraud risks. Operational continuity risks, such as power supply, connectivity and the failure of a core system, are not recorded, so no owner, mitigation or recovery plan exists.',
  [('Governance','Risk Management','Risks that threaten delivery continuity are not identified, assessed or monitored, so leaders learn of them when an outage occurs.','Extend the risk register to operational continuity risks, each with an owner, mitigation and tested recovery plan.'),
   ('Environment','Infrastructure','Single points of failure in infrastructure receive no investment priority because they are absent from the risk register.','Assess critical infrastructure for single points of failure and agree the backup capacity strategic delivery requires.')],
  'Risk management protects strategic delivery when it covers the operating conditions that delivery depends on.',
  'Which operating risk would halt delivery tomorrow, and does it appear in our risk register?'),
 ('CSO','Strategic Integration','Planning Optimism',
  'The CSO develops an ambitious roadmap with milestones that assume funding and cross-functional processes will be ready, without confirming these dependencies with accountable functions.',
  [('Resources','Investment','Milestones are confirmed before implementation funding is secured.','Validate investment commitments and funding timing before fixing delivery milestones.'),
   ('Systems','Integration','The roadmap assumes functional handovers will work cohesively without testing readiness.','Map cross-functional workflow dependencies and confirm integration requirements.')],
  'Strategic milestones depend on validated operating conditions as well as coherent plans.',
  'Which milestone depends on funding or integration that has not yet been established?'),
]
PURPOSE = 'Identify where personal executive assumptions and functional priorities may introduce bias into decisions affecting organisational operating conditions.'
INSTR = 'For each of the four ESRG domains, select one component where your executive role or functional priorities may introduce bias. Reflect on the assumption, its potential consequences and the evidence or alternative perspective needed to counter it.'
DOMS = [('Environment','bias_e',['Facilities','Infrastructure','Technology']),
        ('Systems','bias_s',['Standardisation','Integration','Process Efficiency']),
        ('Resources','bias_r',['Asset Availability','Investment','Resource Utilisation']),
        ('Governance','bias_g',['Policies & Procedures','Authority','Risk Management'])]
COLS = ['My potential bias','Potential execution consequence','My debiasing technique']
WE = [('My potential bias','I may prioritise immediate expenditure reductions over investment required for long-term operating reliability.'),
      ('Potential execution consequence','My decisions could delay essential investment, reducing capacity for consistent operational delivery.'),
      ('My debiasing technique','Before approving reductions, I should examine the investment’s contribution to strategic delivery and assess longer-term consequences of postponement.')]
DEBRIEF = 'Invite participants to share one component where their executive perspective may introduce bias. Explore how different executives interpret the same operating requirement. A CFO may view an infrastructure upgrade as expenditure; a COO may view it as operational continuity. Both perspectives contribute to a better enterprise decision when examined together.'
DEBRIEF_Q = 'What changes when executives examine decisions through the operating capabilities required by the enterprise as well as through their functional priorities?'
CLOSING = 'Executive decisions shape organisational operating conditions through the priorities, assumptions and practices applied within each function. Effective ESRG alignment requires leaders to recognise how their decisions influence operating capabilities beyond their portfolios and challenge assumptions that undermine strategic delivery.'
NEXT = 'Section 4 — Integration · Collective will examine how executive leaders reconcile these perspectives and establish organisational adjustments to strengthen enterprise-wide execution capability.'

def card(n, c, fac):
    role, area, bias, dec, rows, ins, refl = c
    t = tbl('u10-tbl u10-bias', ['ESRG domain','Execution-enabling capability','Component','How the bias affects execution','Debiasing action'],
            [(d, CAP[d], comp, how, act) for d, comp, how, act in rows])
    b = ['<div class="u10-bias-tag">Potential bias &middot; %s</div>' % bias,
         '<div class="u10-sub">Executive decision or practice</div>', '<p>%s</p>' % dec,
         '<div class="u10-sub">ESRG implications</div>', '<div class="u10-scroll">%s</div>' % t.replace('u10-tbl u10-bias"', 'u10-tbl u10-bias" style="min-width:760px"'),
         '<div class="hbox"><p><strong>Executive insight:</strong> %s</p></div>' % ins]
    b.append(('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Executive reflection</div><p>%s</p></div>' % refl) if fac
             else '<div class="p-reflect">Reflect: %s</div>' % refl)
    return acc('CXO Card %d &mdash; %s &middot; %s' % (n, role, area), '\n'.join(b), n == 1, 'Potential bias: ' + bias)

def section3(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    if fac:
        o.append('\n<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Extrapolating</div>\n%s\n</div>' % '\n'.join('<p>%s</p>' % x for x in GUIDE))
        o.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator Approach</div>\n<p>%s</p>\n</div>\n' % APPROACH)
    o.append('<div class="u10-part">3.1 &mdash; The CXO ESRG Bias Contributors</div>\n<p class="u10-lead">%s</p>' % INTRO)
    o += [card(i + 1, c, fac) for i, c in enumerate(CARDS)]
    # 3.2
    b = []
    if fac:
        b.append('<div class="fac-note-full u10-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY — My Executive ESRG Bias Reflection</div><p><strong>Purpose:</strong> %s</p><p><strong>Instructions:</strong> %s</p></div>' % (PURPOSE, INSTR))
        b.append('<div class="u10-sub">Worked example &mdash; CFO</div><div class="u10-we"><p><strong>ESRG domain:</strong> Resources &nbsp;|&nbsp; <strong>Execution-enabling capability:</strong> Delivery Capacity &nbsp;|&nbsp; <strong>Selected component:</strong> Investment</p>%s</div>'
             % ''.join('<p><strong>%s:</strong> %s</p>' % w for w in WE))
        rows = [(d, CAP[d], ' / '.join(x.replace('&', '&amp;') for x in comps), '', '', '') for d, _, comps in DOMS]
        b.append('<div class="u10-sub">My Executive ESRG Bias Reflection</div><div class="u10-scroll">%s</div>'
                 % tbl('u10-tbl u10-bias', ['ESRG domain','Execution-enabling capability','Select one component'] + COLS, rows).replace('u10-tbl u10-bias"', 'u10-tbl u10-bias" style="min-width:760px"'))
    else:
        b.append('<div class="u10-how"><div class="u10-how-h">Portfolio work &middot; How to complete My Executive ESRG Bias Reflection</div><p><strong>Purpose:</strong> %s</p><ol>'
                 '<li>Read the CFO worked example below for the level of detail.</li><li>For each of the four ESRG domains, select one component where your executive role or functional priorities may introduce bias.</li>'
                 '<li>Write your potential bias: the assumption behind it.</li><li>Write its potential execution consequence.</li>'
                 '<li>Write your debiasing technique: the evidence or alternative perspective needed to counter it.</li>'
                 '<li>Your entries save as you type.</li></ol></div>' % PURPOSE)
        b.append('<div class="u10-sub">Worked example &mdash; CFO</div><div class="u10-we"><p><strong>ESRG domain:</strong> Resources &nbsp;|&nbsp; <strong>Execution-enabling capability:</strong> Delivery Capacity &nbsp;|&nbsp; <strong>Selected component:</strong> Investment</p>%s</div>'
             % ''.join('<p><strong>%s:</strong> %s</p>' % w for w in WE))
        for n, (d, key, comps) in enumerate(DOMS):
            f = ['<details class="u10-det"%s><summary>%s &middot; %s</summary><div class="u10-det-b"><div class="ref-block">' % (' open' if n == 0 else '', d, CAP[d]),
                 '<label class="fld-label">Select one component</label><select class="fld-isel" data-fkey="%s" data-fidx="0" onchange="syncFieldDebounced(\'%s\')"><option value="">Select a component</option>%s</select>'
                 % (key, key, ''.join('<option>%s</option>' % x.replace('&', '&amp;') for x in comps))]
            for i, col in enumerate(COLS):
                f.append('<label class="fld-label">%s</label><textarea class="ref-ta fld-input" style="min-height:64px;" data-fkey="%s" data-fidx="%d" oninput="syncFieldDebounced(\'%s\')"></textarea>' % (col, key, i + 1, key))
            f.append('<textarea id="%s" class="reflection-textarea" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="%s-saved"></div><button class="ref-save" onclick="fldSaveBtn(this,\'%s\')">Save</button></div></div></details>' % (key, key, key))
            b.append('\n'.join(f))
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR DEBRIEF</div><p>%s</p><p><strong>Debrief question:</strong> %s</p></div>' % (DEBRIEF, DEBRIEF_Q))
    o.append(acc('3.2 &mdash; Personal Activity: Where Might My Executive Bias Influence ESRG?', '\n'.join(b), False, '' if fac else 'Portfolio Work'))
    o.append('<div class="hbox"><p><strong>Closing insight:</strong> %s</p><p>%s</p></div>' % (CLOSING, NEXT))
    return '\n'.join(o) + '\n'

def css(fac):
    c, bd = ('var(--gold)', 'rgba(201,168,76,.25)') if fac else ('var(--teall)', 'rgba(26,122,106,.25)')
    return ('.u10-part{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%(c)s;margin:22px 0 6px;}\n'
            '.u10-lead{font-size:14px;line-height:1.9;color:rgba(255,255,255,.72);margin:0 0 14px;}\n'
            '.u10-bias-tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:1px;color:%(c)s;border:1px solid %(bd)s;border-radius:2px;padding:4px 10px;margin:0 0 6px;}\n'
            '.u10-bias td:nth-child(2){color:%(c)s;}\n.u10-bias td:nth-child(3){color:rgba(255,255,255,.88);font-weight:600;}\n'
            '.u10-we{border-left:3px solid %(bd)s;padding:4px 0 4px 14px;margin:8px 0 14px;}\n.u10-we p{font-size:13px!important;line-height:1.75!important;margin-bottom:6px!important;}\n') % dict(c=c, bd=bd)

JS = r'''
/* Unit 10 · part 3.2 My Executive ESRG Bias Reflection (Portfolio work): one key per ESRG domain. */
["bias_e","bias_s","bias_r","bias_g"].forEach(function(k){FIELD_SPECS[k]=[{l:"Component",k:"select"},{l:"My potential bias",k:"text"},{l:"Potential execution consequence",k:"text"},{l:"My debiasing technique",k:"text"}];});
'''
