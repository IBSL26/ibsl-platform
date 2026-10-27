# -*- coding: utf-8 -*-
"""Unit 10 Section 4 · Integration, as Carol gave it (27 Oct, 18:00). Standing rules: "lens" -> "perspective"; contrast constructions reworded; no "automatically"."""
from u10_content import acc
from u10_s2 import tbl, scale_tbl, scanner, profile, SCALE_NOTE

TITLE = 'How Does the Executive Team Create Collective Intelligence for ESRG Alignment?'
HERO = 'Combining functional operating assessments into a shared executive understanding of common conditions, differences between functions and the dependencies that determine strategic delivery.'
LO = ['Integrate functional ESRG assessments into a collective intelligence view by identifying convergence, divergence and dependency across organisational operating capabilities.',
      'Formulate collective intelligence responses that coordinate shared conditions, reconcile functional differences and align operating dependencies affecting strategic commitments.']
GUIDE = ['In Intelligence, participants learned the four execution-enabling capabilities and the Functional ESRG Scanner. In Extrapolating, they examined executive biases that can distort operating decisions. Integration brings functional perspectives together to establish what the executive team can see, understand and address collectively.',
         'Use the illustrative, prepopulated Enterprise ESRG Scanner in this section to teach interpretation and response. Participants do not rescore the illustrative data. In 4.5, each participant completes the Functional ESRG Scanner for their assigned capstone executive function. Those actual scores feed the Enterprise Scanner for the capstone work in Section 5, where the team validates findings and determines its organisational interventions.',
         '<strong>Central question:</strong> What can the executive team discover about the operating environment collectively that no function can establish from its own assessment alone?']
P41 = 'Collective intelligence progresses through three connected dimensions. Each is associated with one primary interpretive perspective and a corresponding response discipline. The pairing is a practical learning sequence; each perspective can also be applied at the other levels.'
DIMS = [('Functional Intelligence','Convergence','Common operating strengths or constraints emerging when individual functional assessments are brought together.','Where are our functions pointing to the same operating conditions?','Coordinate'),
        ('Cross-Functional Intelligence','Divergence','Differences in functional scores or experiences that need explanation and reconciliation.','Where do our functional assessments differ, and why?','Reconcile'),
        ('Enterprise Intelligence','Dependency','How capabilities in one function enable or constrain other functions and enterprise strategic commitments.','Where do we depend on one another to deliver enterprise results?','Align')]
FLOW = 'The executive conversation progresses: What do we have in common? &rarr; Where do we differ? &rarr; How do we depend on one another?'
SUBS = [('Convergence — Functional Intelligence','When multiple functions independently report a similar condition, the executive team gains evidence of a potentially shared operating pattern. For example, low Integration scores in Commercial, Operations and Technology may indicate a recurring difficulty connecting workflows. Convergence invites the team to test whether the weakness has a common cause and whether a coordinated response is warranted.'),
        ('Divergence — Cross-Functional Intelligence','Differences in scores invite investigation before any judgement is made. Technology may report that its systems are reliable while Operations reports that the same technological environment does not adequately support required activities. The executive team examines the basis of each assessment, distinguishes differing operating experiences from inconsistent criteria and reconciles the actual requirement.'),
        ('Dependency — Enterprise Intelligence','A function may score strongly while its strategic contribution remains exposed to another function’s operating weakness. Commercial growth, for example, may depend on Operations infrastructure and Finance investment. Dependency makes the chain of delivery visible and enables executives to agree shared operating requirements and commitments.')]
P42 = 'The Enterprise ESRG Scanner is populated directly from the Functional ESRG Scanners. The detailed component-level view comes first; the enterprise capability profile is calculated from that detail. There is no separate enterprise scoring exercise.'
P42B = 'The following illustration is prepopulated with example scores to demonstrate how the instrument works. In the actual tool, each cell links to the corresponding function’s 1–5 component score for the same assessment period. The figures are illustrative and come from no real organisation.'
FUN = ['Finance','Operations','Commercial','HR','Technology']
CAP = {'Environment':'Operational Readiness','Systems':'Operational Flow','Resources':'Delivery Capacity','Governance':'Decision Responsiveness'}
DET = [('Environment','Facilities',[4,3,4,4,4]),('Environment','Infrastructure',[4,2,4,4,4]),('Environment','Technology',[4,3,4,4,2]),
       ('Systems','Standardisation',[4,3,4,4,3]),('Systems','Integration',[2,2,2,3,2]),('Systems','Process Efficiency',[4,3,3,4,3]),
       ('Resources','Asset Availability',[4,2,4,4,3]),('Resources','Investment',[4,3,4,4,3]),('Resources','Resource Utilisation',[4,3,3,4,3]),
       ('Governance','Policies &amp; Procedures',[4,4,4,4,4]),('Governance','Authority',[4,2,3,4,3]),('Governance','Risk Management',[4,4,4,4,4])]
SUMM = [('Environment',['4.00','2.67','4.00','4.00','3.33','3.60']),('Systems',['3.33','2.67','3.00','3.67','2.67','3.07']),
        ('Resources',['4.00','2.67','3.67','4.00','3.00','3.47']),('Governance',['4.00','3.33','3.67','4.00','3.67','3.73'])]
LOGIC = 'Each component score is pulled from its functional source; missing assessments remain blank and are flagged, and a blank never counts as zero. The scoring definitions, annual baseline and quarterly periods remain identical to the Functional Scanner. Where a component is genuinely not applicable, this must be explicitly recorded and excluded from the relevant average.'
CALC = 'Each functional capability score is the average of its three component scores; the enterprise capability average is the average of the assessed functional capability scores. These descriptive averages are signals for investigation; the significance of individual constraints and dependencies still requires evaluation.'
READ = 'Read the detailed component view alongside the summary. A reasonable enterprise average can conceal a critical low score in a function on which strategic delivery depends.'
P43 = 'Interpret the prepopulated functional scores capability by capability. For each capability, use the three linked intelligence perspectives in sequence: identify common patterns (Convergence), investigate differences (Divergence), then establish strategic operating dependencies (Dependency). All findings below are hypotheses to validate through evidence and executive dialogue.'
PROMPTS = [('Convergence','Which functions report similar conditions, and do those ratings reflect a shared cause?'),
           ('Divergence','What explains the differences in scores, requirements or operating experience?'),
           ('Dependency','Which strategic commitment depends on these conditions, and which functions must act together?')]
CAUTION = 'A difference in ratings does not by itself prove misalignment; a shared low rating does not by itself prove a shared root cause. Executive dialogue must validate both.'
INTERP = [('Operational Readiness (Environment)','Infrastructure scores 4 in Finance, Commercial, HR and Technology: similar confidence in readiness; verify whether these functions rely on the same infrastructure or separate arrangements.','Infrastructure: Operations 2 versus four functions at 4. Determine what differs in capacity, reliability or operating requirements; do not assume identical conditions.','Commercial expansion relies on Operations fulfilment. Operations Infrastructure 2 may threaten the enterprise commitment despite Commercial Infrastructure 4.'),
          ('Operational Flow (Systems)','Integration: Finance 2, Operations 2, Commercial 2 and Technology 2. Test whether shared handover failures explain the common weakness.','Integration: HR 3 versus four functions at 2. Examine whether HR has better-connected workflows or a different basis for its rating.','Order-to-delivery performance depends on connected Commercial, Operations and Technology workflows; failures at handovers can constrain the whole delivery chain.'),
          ('Delivery Capacity (Resources)','Investment: Finance, Commercial and HR each 4. Test whether adequate provision is consistently available for their strategic requirements.','Asset Availability: Operations 2 versus Finance, Commercial and HR at 4. Examine which assets and delivery loads explain the gap.','Commercial commitments may depend on Operations assets (2), even when Commercial reports Asset Availability 4. Validate the capacity needed to fulfil enterprise demand.'),
          ('Decision Responsiveness (Governance)','Policies &amp; Procedures and Risk Management are rated 4 by every function. Confirm whether the shared strength is supported by consistent practice.','Authority: Operations 2, Commercial and Technology 3, Finance and HR 4. Investigate delegated decision rights and approval delays.','If Operations approvals are delayed (Authority 2), customer fulfilment can be held up despite responsive decisions elsewhere; agree cross-functional escalation and delegation needs.')]
P44 = 'The Collective Intelligence Response records the operating condition, the evidence-based finding and the executive action required. Apply the response discipline appropriate to the finding: Coordinate shared conditions, Reconcile differences or Align dependencies. The perspective is established during interpretation in 4.3 and does not need another column here.'
RESP = [('Systems','Operational Flow','Integration','Four functions score Integration at 2, suggesting a possible shared workflow constraint.','<strong>COORDINATE:</strong> map the recurring handover failures; confirm whether the root cause is common; agree shared integration requirements and an accountable coordinating lead.','COO, CIO, CFO, CCO'),
        ('Environment','Operational Readiness','Technology','The Technology function scores Technology at 2 while several other functions score 4.','<strong>RECONCILE:</strong> compare assessment evidence and functional operating requirements; identify the precise shortfall; agree what must be changed and who will validate readiness.','CIO, COO, affected functional executives'),
        ('Environment','Operational Readiness','Infrastructure','Operations scores Infrastructure at 2; Commercial’s growth commitment relies on Operations fulfilment.','<strong>ALIGN:</strong> validate infrastructure capacity against commercial demand; agree required upgrades, funding and sequencing before confirming delivery commitments.','CEO, COO, CFO, CCO')]
P44B = 'The table is an illustrative Collective Intelligence Response. In Section 5, the capstone team uses its actual linked assessments to validate the findings, prioritise constraints and develop targeted organisational alignment interventions.'
DISC = ['What does the evidence actually establish?','What strategic commitment is affected?','What decision requires collective executive agreement?','Which functions must contribute?']
PURPOSE45 = 'Generate the functional operating intelligence that will populate the capstone team’s Enterprise ESRG Scanner.'
P45_F = 'Working in their assigned capstone executive roles, participants complete the Functional ESRG Performance Scanner for their respective functions within the capstone organisation. The activity is a personal functional assessment; enterprise interpretation and decisions are reserved for Section 5.'
P45_P = 'Working in your assigned capstone executive role, you complete the Functional ESRG Performance Scanner for your function within your capstone organisation. The activity is a personal functional assessment; enterprise interpretation and decisions are reserved for Section 5.'
COMPS = [('Environment','Facilities; Infrastructure; Technology'),('Systems','Standardisation; Integration; Process Efficiency'),
         ('Resources','Asset Availability; Investment; Resource Utilisation'),('Governance','Policies &amp; Procedures; Authority; Risk Management')]
INSTR_F = ['Open the Functional ESRG Scanner assigned to their capstone role and select the stated problem from the group’s Problem Charter that their function’s assessment addresses.',
           'Score all 12 components using the existing assessment statements and 1–5 criteria.',
           'Complete the annual baseline; the scores save as they work.',
           'Confirm that their function’s results are available for consolidation into the capstone Enterprise ESRG Scanner.']
INSTR_P = ['Select your capstone executive role, enter your business function and select the stated problem from your group’s Problem Charter that your assessment addresses.',
           'Score all 12 components using the assessment statements and the 1–5 scoring guide. Where a component is genuinely not applicable to your function, select N/A; it is left out of the averages.',
           'Complete the annual baseline. Your scores save as you work.',
           'Your function’s results are then available to your group’s Enterprise ESRG Scanner in Section 5.']
OUT_F = 'One completed Functional ESRG Performance Scanner per capstone executive function. The scores populate the detailed Enterprise Scanner and its calculated capability summary. In Section 5 — Application, the team uses these results to interpret convergence, divergence and dependency, and determine its collective ESRG alignment responses.'
OUT_P = 'Your completed Functional ESRG Performance Scanner for your capstone executive function. Your group’s scores populate the detailed Enterprise Scanner and its calculated capability summary. In Section 5 — Application, your group uses these results to interpret convergence, divergence and dependency, and determine its collective ESRG alignment responses.'
DEBRIEF = 'What becomes visible when functional operating assessments are brought together, compared and connected to strategic commitments?'
CLOSING = 'Collective ESRG intelligence develops as executives coordinate what functions have in common, reconcile what they experience differently and align the operating dependencies required for enterprise results.'
TRANS = 'The capstone executive team now has the functional evidence needed to populate its Enterprise ESRG Scanner and determine targeted alignment interventions.'

def wide(t, mw=760):
    return '<div class="u10-scroll">%s</div>' % t.replace('<table class="u10-tbl', '<table style="min-width:%dpx" class="u10-tbl' % mw, 1)

def section4(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    if fac:
        o.append('\n<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Integration</div>\n%s\n</div>\n' % '\n'.join('<p>%s</p>' % x for x in GUIDE))
    b = ['<p>%s</p>' % P41, wide(tbl('u10-tbl u10-cap', ['Intelligence dimension','Primary perspective','What the team establishes','Guiding question','Response discipline'], DIMS)),
         '<div class="hbox"><p>%s</p></div>' % FLOW]
    b += ['<div class="u10-sub">%s</div><p>%s</p>' % s for s in SUBS]
    o.append(acc('4.1 &mdash; Three Dimensions of Collective ESRG Intelligence', '\n'.join(b), True))
    det = [(d, CAP[d], c) + tuple(str(x) for x in v) for d, c, v in DET]
    summ = [(d, CAP[d]) + tuple(v) for d, v in SUMM]
    b = ['<p>%s</p>' % P42,
         '<div class="u10-sub">B. Detailed Enterprise Component-Level View &mdash; Source of the Summary</div>', '<p>%s</p>' % P42B,
         wide(tbl('u10-tbl u10-ent', ['ESRG domain','Execution capability','Component'] + FUN, det)),
         '<p><strong>Instrument logic:</strong> %s</p>' % LOGIC,
         '<div class="u10-sub">A. Enterprise Capability Profile &mdash; Calculated Summary</div>',
         wide(tbl('u10-tbl u10-ent u10-sum', ['ESRG domain','Execution capability'] + FUN + ['Enterprise avg.'], summ)),
         '<p><strong>Calculation:</strong> %s</p>' % CALC, '<div class="hbox"><p>%s</p></div>' % READ]
    o.append(acc('4.2 &mdash; Enterprise ESRG Scanner: One Source, Two Linked Views', '\n'.join(b), False))
    b = ['<p>%s</p>' % P43]
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator prompts &mdash; for each execution-enabling capability</div><ul>%s</ul></div>' % ''.join('<li><strong>%s:</strong> %s</li>' % x for x in PROMPTS))
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator caution</div><p>%s</p></div>' % CAUTION)
    else:
        b.append('<div class="p-reflect">Reflect, for each execution-enabling capability: %s</div>' % ' '.join('<strong>%s:</strong> %s' % x for x in PROMPTS))
        b.append('<div class="hbox"><p><strong>Caution:</strong> %s</p></div>' % CAUTION)
    b.append('<div class="u10-sub">Illustrative interpretation of the prepopulated scanner</div>')
    b.append(wide(tbl('u10-tbl u10-int', ['Execution-enabling capability','Functional Intelligence / Convergence','Cross-Functional Intelligence / Divergence','Enterprise Intelligence / Dependency'], INTERP), 860))
    o.append(acc('4.3 &mdash; Interpreting the Prepopulated Scanner', '\n'.join(b), False))
    b = ['<p>%s</p>' % P44, wide(tbl('u10-tbl u10-int', ['ESRG domain','Capability','Component','Collective finding','Collective intelligence response','Executive functions'], RESP), 860),
         '<p>%s</p>' % P44B]
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Collective executive discussion</div><p>For each proposed response, ask:</p><ol>%s</ol></div>' % ''.join('<li>%s</li>' % x for x in DISC))
    else:
        b.append('<div class="p-reflect">Reflect, for each proposed response: %s</div>' % ' '.join('(%d) %s' % (i + 1, x) for i, x in enumerate(DISC)))
    o.append(acc('4.4 &mdash; Collective Intelligence Response', '\n'.join(b), False))
    b = []
    comps = wide(tbl('u10-tbl u10-cap', ['ESRG domain','Execution-enabling capability','Components to score'], [(d, CAP[d], c) for d, c in COMPS]), 560)
    if fac:
        b.append('<div class="fac-note-full u10-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div><p><strong>Purpose:</strong> %s</p><p>%s</p><ol>%s</ol></div>'
                 % (PURPOSE45, P45_F, ''.join('<li>Participants %s</li>' % (x[0].lower() + x[1:]) for x in INSTR_F)))
        b += [comps, '<div class="hbox"><p><strong>Activity output:</strong> %s</p></div>' % OUT_F,
              '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR DEBRIEF AND TRANSITION</div><p>Ask: %s</p></div>' % DEBRIEF]
    else:
        b.append('<div class="u10-how"><div class="u10-how-h">Personal activity &middot; How to complete My Capstone Functional ESRG Assessment</div><p><strong>Purpose:</strong> %s</p><ol>%s</ol></div>'
                 % (PURPOSE45, ''.join('<li>%s</li>' % x for x in INSTR_P)))
        b += ['<p>%s</p>' % P45_P, comps]
        b.append('<div class="ref-block"><div class="ref-label">&#x270E; My capstone function</div><div id="u10CoName" class="u10-co"></div>'
                 '<label class="fld-label">Capstone executive role</label><select class="fld-isel" id="u10RoleSel" data-fkey="esrg_scan_head" data-fidx="0" onchange="syncFieldDebounced(\'esrg_scan_head\')"><option value="">Select your role</option></select>'
                 '<div id="u10RoleNote" class="u10-note" style="display:none;">Your role list appears once every member of your group has agreed your Problem Charter in Unit 1, part 6.2.</div>'
                 '<label class="fld-label">Business function</label><input class="fld-input" type="text" data-fkey="esrg_scan_head" data-fidx="1" oninput="syncFieldDebounced(\'esrg_scan_head\')">'
                 '<label class="fld-label">Stated problem from your Problem Charter</label><select class="fld-isel" id="u10ProbSel" data-fkey="esrg_scan_head" data-fidx="2" onchange="syncFieldDebounced(\'esrg_scan_head\')"><option value="">Select the stated problem</option></select>'
                 '<div id="u10ProbNote" class="u10-note" style="display:none;">Your group’s stated problems appear once every member of your group has agreed your Problem Charter in Unit 1, part 6.2.</div>'
                 '<textarea id="esrg_scan_head" class="reflection-textarea" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="esrg_scan_head-saved"></div></div>')
        b.append('<div class="u10-sub">Scoring guide</div>' + scale_tbl() + '<p>%s</p>' % SCALE_NOTE)
        b.append('<div class="u10-sub">My Functional ESRG Performance Scanner &mdash; Annual Baseline</div>' + scanner(False))
        b.append('<textarea id="esrg_scan" class="reflection-textarea" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="esrg_scan-saved"></div><button class="ref-save" onclick="fldSaveBtn(this,\'esrg_scan\')">Save</button>')
        b.append('<div class="hbox"><p><strong>Activity output:</strong> %s</p></div>' % OUT_P)
    o.append(acc('4.5 &mdash; Personal Activity: My Capstone Functional ESRG Assessment', '\n'.join(b), False, 'Personal Activity'))
    o.append('<div class="hbox"><p><strong>Closing insight:</strong> %s</p><p><strong>Transition to Section 5 &mdash; Application:</strong> %s</p></div>' % (CLOSING, TRANS))
    return '\n'.join(o) + '\n'

def css(fac):
    return ('.u10-ent th:nth-child(n+4),.u10-ent td:nth-child(n+4){text-align:center;}\n.u10-sum th:nth-child(3),.u10-sum td:nth-child(3){text-align:center;}\n'
            '.u10-int td{font-size:12.5px;}\n.u10-co{font-size:13px;color:rgba(255,255,255,.8);margin:4px 0 2px;}\n.u10-note{font-size:12px;color:rgba(255,255,255,.55);margin:4px 0;}\n')
JS = open(__import__('os').path.join(__import__('os').path.dirname(__file__),'u10_s4.js'),encoding='utf-8').read()
