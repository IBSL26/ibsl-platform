# -*- coding: utf-8 -*-
"""Unit 10 Section 5 · The Enterprise ESRG Alignment Clinic, as Carol gave it (27 Oct, 18:23).
Group Capstone work on the shared group record; 5.1 brings in every member's part 4.5 scanner (rpc team_esrg_scans).
Standing rules: "lens" -> "perspective"; "Facilitator Review Focus" reworded (the facilitator does not review Capstone work)."""
import os
from u10_content import acc
from u10_s2 import tbl, BANDS

TITLE = 'The Enterprise ESRG Alignment Clinic'
HERO = 'From individual functional assessments to enterprise intelligence, collective responses and implementable operating interventions.'
LO = ['Consolidate and interpret functional ESRG assessments to establish an evidence-based enterprise view of the operating capabilities required for strategic delivery.',
      'Develop and operationalise collective ESRG alignment interventions that address operating constraints and strengthen cross-functional delivery of strategic commitments.']
GUIDE = 'Participants work as the executive team of their assigned capstone organisation. Each member brings the Functional ESRG Performance Scanner completed for their assigned function in Section 4.5. The team consolidates those existing scores into the Enterprise ESRG Scanner, interprets them by execution-enabling capability, agrees a Collective Intelligence Response and then transfers each agreed response into an ESRG Alignment Intervention Plan.'
CORE = 'What must this executive team collectively strengthen in the organisation’s operating conditions to deliver its strategic commitments consistently?'
INPUTS = 'Capstone strategy and commitments; individual functional scanners; linked Enterprise ESRG Scanner; Collective Intelligence Response Table; ESRG Alignment Intervention Plan.'
NONNEG_F = 'No rescoring at enterprise level. Component scores are pulled directly from the functional scanners. The executive team may query the evidence behind a score, but any correction is made in the originating functional assessment and flows through to the enterprise view.'
NONNEG_P = 'No rescoring at enterprise level. Component scores come directly from each member’s Functional ESRG Performance Scanner in part 4.5. Your executive team may query the evidence behind a score; any correction is made by that member in part 4.5 and flows through to the enterprise view.'
HOW = ['Your group chooses its scribe for this work in the group record bar. The scribe types what your group agrees, and the entries appear on every member’s page.',
       'Part 5.1 brings in every member’s annual baseline from part 4.5. Your group checks that each function’s assessment is complete and records any missing submissions or evidence gaps.',
       'In part 5.2, interpret the Enterprise Scanner by execution-enabling capability and write each finding with its evidence.',
       'In part 5.3, record your agreed Collective Intelligence Responses. In part 5.4, complete the ESRG Alignment Intervention Plan for each of them.',
       'When your record is complete, each member selects Agree. Your group’s work then goes into your team’s Capstone S2R® Blueprint.']
Q1_F = 'It is now Q1. The executive team meets for its first quarterly ESRG review, working from the annual baseline each member completed in Section 4.5.'
Q1_P = 'It is now Q1. Your executive team meets for its first quarterly ESRG review, working from the annual baseline each member completed in part 4.5.'
S1_F = 'Confirm that each executive function has submitted one completed assessment covering all 12 components, using the same 1–5 scale and assessment period. Record missing submissions or evidence gaps before interpretation. The capstone executive team works with the functions represented in its simulation; the five columns below are illustrative.'
S1_P = 'Confirm that each executive function has submitted one completed assessment covering all 12 components, using the same 1–5 scale and assessment period. Record missing submissions or evidence gaps before interpretation. Your executive team works with the functions represented in its simulation.'
S2_F = 'This is the detailed source view. Every numeric cell is linked to the corresponding component in the relevant Functional ESRG Scanner; participants do not enter scores a second time.'
S2_P = 'This is the detailed source view. Every score comes from the corresponding component in the relevant member’s Functional ESRG Scanner; you do not enter scores a second time.'
S3 = 'The scanner calculates each function’s capability score as the mean of its three component scores, then displays an enterprise average across the participating functions. The average is a directional indicator; it does not override the significance of a critical low-scoring function or component.'
CHECK = 'Confirm that the detailed component view and calculated capability summary reflect the same source assessments. Retain both views for interpretation.'
P52 = 'For each capability, examine the three intelligence levels and their corresponding perspectives in the agreed sequence: Functional Intelligence / Convergence &rarr; Cross-Functional Intelligence / Divergence &rarr; Enterprise Intelligence / Dependency. Use the detailed component scores to support each finding; use the summary to identify areas meriting attention.'
PERSP = [('Functional Intelligence','Convergence','Where do multiple functions report a similar condition?','Coordinate'),
         ('Cross-Functional Intelligence','Divergence','Where do functional assessments differ, and why?','Reconcile'),
         ('Enterprise Intelligence','Dependency','Where does one function’s operating capability enable or constrain another’s strategic delivery?','Align')]
DOMS = [('Environment','Operational Readiness','Facilities · Infrastructure · Technology','environment'),
        ('Systems','Operational Flow','Standardisation · Integration · Process Efficiency','systems'),
        ('Resources','Delivery Capacity','Asset Availability · Investment · Resource Utilisation','resources'),
        ('Governance','Decision Responsiveness','Policies &amp; Procedures · Authority · Risk Management','governance')]
QS = [('Functional / Convergence','Which %s components show similar scores or conditions across functions?'),
      ('Cross-functional / Divergence','Where do functions differ on the same component, and what evidence explains the difference?'),
      ('Enterprise / Dependency','Which strategic commitments rely on an operating condition supplied or controlled by another function?')]
RULE = 'A shared low score may indicate convergence; a large score difference may indicate divergence; dependency requires a demonstrable relationship between functions and a strategic commitment. Scores alone do not prove a dependency.'
P53 = 'The team selects the most consequential findings from 5.2 and records an agreed executive response. Each response must identify the specific ESRG component, the strategic commitment affected and the functions involved.'
RESP_EX = [('Systems','Operational Flow','Integration','Order-to-delivery handovers are disconnected across Commercial and Operations.','Reduce fulfilment time.','Agree a connected workflow, handover requirements and shared information standards.','COO, CCO, CIO'),
           ('Environment','Operational Readiness','Infrastructure','Operations infrastructure capacity constrains planned commercial growth.','Increase service capacity.','Confirm required capacity, funding and coordinated upgrade decision.','COO, CFO, CCO')]
DISC = 'Use the response discipline appropriate to the finding: Convergence &rarr; Coordinate shared conditions; Divergence &rarr; Reconcile differing assessments using evidence; Dependency &rarr; Align interdependent operating requirements and responsibilities. A finding may involve more than one perspective, but the table records one coherent collective response.'
PRIOR = 'Is the finding supported by component-level evidence? Does it threaten an identifiable strategic commitment? Does it require a collective executive decision? Select the responses that pass these tests.'
P54 = 'Use the completed Collective Intelligence Response Table in 5.3 as the sole starting point. Carry each agreed response into the intervention plan, then specify its implementation actions, accountable executive, contributing functions, target date and evidence of improvement. Do not introduce new findings or repeat the diagnosis.'
PLAN_EX = [('Connected workflow and shared handover requirements.','Map current handovers; agree target workflow; implement shared information checkpoints; test end-to-end processing.','COO','CCO, CIO','[date]','Reduced handover delays and fulfilment time.'),
           ('Confirm infrastructure capacity and coordinated upgrade decision.','Validate demand/capacity gap; cost options; approve investment; deliver priority upgrade.','COO','CFO, CCO','[date]','Capacity and reliability meet expansion requirements.')]
CONT = 'Every intervention in 5.4 must correspond to an agreed response in 5.3. Each implementation action must advance that response, and the evidence of improvement must demonstrate a change in the operating condition identified.'
OUTPUTS = ['Enterprise ESRG Scanner populated from the individual Functional ESRG Scanners.','Completed Collective Intelligence Response Table (5.3).','ESRG Alignment Intervention Plan developed directly from the agreed responses in 5.3.']
QUALITY = ['accurate consolidation of the functional scores', 'consistent three-level intelligence interpretation', 'evidence supporting the findings', 'relevance to strategic commitments', 'quality of the collective executive decisions', 'traceability from each agreed response to its implementation plan']
CLOSING = 'Functional assessments make operating conditions visible. Collective intelligence establishes what those conditions mean for the enterprise. The Collective Intelligence Response determines what must change; the ESRG Alignment Intervention Plan establishes how the executive team will make that change happen.'
EL = ['Facilities','Infrastructure','Technology','Standardisation','Integration','Process Efficiency','Asset Availability','Investment','Resource Utilisation','Policies &amp; Procedures','Authority','Risk Management']
CAPN = ['Operational Readiness','Operational Flow','Delivery Capacity','Decision Responsiveness']
DOMN = ['Environment','Systems','Resources','Governance']
FUN = ['Finance','Operations','Commercial','HR','Technology']

def wide(t, mw=760):
    return '<div class="u10-scroll">%s</div>' % t.replace('<table class="u10-tbl', '<table style="min-width:%dpx" class="u10-tbl' % mw, 1)

def u10det(title, body, open_=False):
    return '<details class="u10-det"%s><summary>%s</summary><div class="u10-det-b">%s</div></details>' % (' open' if open_ else '', title, body)

def placeholder_tables():
    det = [(DOMN[i // 3], CAPN[i // 3], EL[i]) + ('Linked',) * 5 for i in range(12)]
    summ = [(DOMN[i], CAPN[i]) + ('Calc.',) * 6 for i in range(4)]
    return (wide(tbl('u10-tbl u10-ent', ['ESRG domain','Execution capability','Component'] + FUN, det)),
            wide(tbl('u10-tbl u10-ent u10-sum', ['ESRG domain','Execution capability'] + FUN + ['Enterprise avg.'], summ)))

def section5(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    if fac:
        o.append('\n<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDE — Overview</div>\n<p>%s</p>\n<p><strong>%s</strong></p>\n<p><strong>Core application question:</strong> %s</p>\n<p><strong>Inputs:</strong> %s</p>\n<p><strong>Non-negotiable:</strong> %s</p>\n</div>\n' % (GUIDE, Q1_F, CORE, INPUTS, NONNEG_F))
    else:
        o.append('<div class="u10-how"><div class="u10-how-h">Capstone work &middot; How Section 5 works</div><ol>%s</ol></div>' % ''.join('<li>%s</li>' % x for x in HOW))
        o.append('<div class="hbox"><p><strong>%s</strong></p><p><strong>Core application question:</strong> %s</p><p><strong>Non-negotiable:</strong> %s</p></div>' % (Q1_P, CORE, NONNEG_P))
        o.append('<div id="u10TwBar"></div>')
    # 5.1
    if fac:
        det, summ = placeholder_tables()
        b = ['<div class="u10-sub">Step 1 &middot; Verify the functional inputs</div><p>%s</p>' % S1_F,
             '<div class="u10-sub">Step 2 &middot; Populate the Enterprise Component-Level Scanner</div><p>%s</p>' % S2_F, det,
             '<div class="u10-sub">Step 3 &middot; Generate the Enterprise Capability Summary</div><p>%s</p>' % S3, summ,
             '<div class="hbox"><p><strong>Checkpoint:</strong> %s</p></div>' % CHECK]
    else:
        b = ['<div class="u10-sub">Step 1 &middot; Verify the functional inputs</div><p>%s</p>' % S1_P,
             '<div class="u10-row"><button type="button" class="ref-save u10-refresh" data-team-free onclick="u10LoadTeam()">Refresh members’ scores</button></div>',
             '<div id="u10Verify"></div>',
             '<label class="fld-label" for="u10Gaps">Missing submissions or evidence gaps</label><textarea class="fld-input u10-ta" id="u10Gaps" data-u10="gaps" style="min-height:60px;"></textarea>',
             '<div class="u10-sub">Step 2 &middot; Populate the Enterprise Component-Level Scanner</div><p>%s</p>' % S2_P, '<div id="u10Ent"></div>',
             '<div class="u10-sub">Step 3 &middot; Generate the Enterprise Capability Summary</div><p>%s</p>' % S3, '<div id="u10Sum"></div>',
             '<p class="u10-bands">%s</p>' % BANDS,
             '<div class="hbox"><p><strong>Checkpoint:</strong> %s</p></div>' % CHECK]
    o.append(acc('5.1 &mdash; Consolidate Individual Functional Scores', '\n'.join(b), True))
    # 5.2
    b = ['<p>%s</p>' % P52, wide(tbl('u10-tbl u10-cap', ['Intelligence level','Perspective','Interpretation prompt','Response discipline'], PERSP))]
    for di, (d, cap, comps, low) in enumerate(DOMS):
        blk = ['<p class="u10-comps">Components: %s</p>' % comps]
        if fac:
            blk.append(wide(tbl('u10-tbl u10-int', ['Intelligence / perspective','Question to investigate','Finding / evidence'], [(l, q % low if '%s' in q else q, '________________________') for l, q in QS]), 600))
        else:
            for k, (l, q) in enumerate(QS):
                q = q % low if '%s' in q else q
                blk.append('<div class="u10-q"><div class="u10-ql">%s</div><div class="u10-qq">%s</div><textarea class="fld-input u10-ta" data-u10="interp-%d-%d" style="min-height:60px;" aria-label="%s · %s"></textarea></div>' % (l, q, di, k, d, l))
        b.append(u10det('%s &mdash; %s' % (d, cap), '\n'.join(blk), di == 0))
    b.append('<div class="hbox"><p><strong>Interpretation rule:</strong> %s</p></div>' % RULE)
    o.append(acc('5.2 &mdash; Interpret the Enterprise Scanner by Execution Capability', '\n'.join(b), False))
    # 5.3
    ex = tbl('u10-tbl u10-int', ['ESRG domain','Execution capability','Component','Collective finding','Strategic commitment affected','Collective intelligence response','Functions involved'], RESP_EX)
    b = ['<p>%s</p>' % P53]
    if fac:
        b.append(wide(ex.replace('</tbody>', '<tr><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>\n</tbody>'), 900))
    else:
        b += ['<div class="u10-sub">Example</div>', wide(ex, 900), '<div class="u10-sub">Your Collective Intelligence Response Table</div>', '<div id="u10Resp"></div>',
              '<button type="button" class="ref-save u10-add" onclick="u10AddResp()">+ Add a response</button>']
    b += ['<p>%s</p>' % DISC, '<div class="hbox"><p><strong>Prioritisation test:</strong> %s</p></div>' % PRIOR]
    o.append(acc('5.3 &mdash; Complete the Collective Intelligence Response Table', '\n'.join(b), False))
    # 5.4
    ex = tbl('u10-tbl u10-int', ['Agreed collective response (from 5.3)','Implementation actions','Accountable executive','Contributing functions','Target date','Evidence of improvement'], PLAN_EX)
    b = ['<p>%s</p>' % P54]
    if fac:
        b.append(wide(ex.replace('</tbody>', '<tr><td>[Copy from 5.3]</td><td>[Actions]</td><td>[Owner]</td><td>[Functions]</td><td>[date]</td><td>[Measure]</td></tr>\n</tbody>'), 900))
    else:
        b += ['<div class="u10-sub">Example</div>', wide(ex, 900), '<div class="u10-sub">Your ESRG Alignment Intervention Plan</div>', '<div id="u10Plan"></div>']
    b.append('<div class="hbox"><p><strong>Continuity check:</strong> %s</p></div>' % CONT)
    o.append(acc('5.4 &mdash; Translate the Agreed Responses into an ESRG Alignment Intervention Plan', '\n'.join(b), False))
    # outputs
    qual = '<p><strong>%s</strong> %s.</p>' % ('Completion focus:' if fac else 'What your completed work shows:', '; '.join(QUALITY)[0].upper() + '; '.join(QUALITY)[1:])
    out = '<div class="u10-sub">Application outputs</div><ul class="u10-ul">%s</ul>%s' % (''.join('<li>%s</li>' % x for x in OUTPUTS), qual)
    if not fac:
        out += ('<div class="u10-rec"><div id="u10RecMsg" class="u10-note"></div>'
                '<button type="button" class="ref-save" data-team-free onclick="u10Agree()">Agree</button> '
                '<button type="button" class="ref-save" data-team-free onclick="u10Print()">Print our group record</button></div>')
    o.append('<div class="hbox">%s</div>' % out)
    o.append('<div class="hbox"><p><strong>Closing insight:</strong> %s</p></div>' % CLOSING)
    return '\n'.join(o) + '\n'

def css(fac):
    return ('.u10-row{display:flex;flex-wrap:wrap;align-items:flex-end;gap:12px;margin:8px 0;}\n.u10-row .fld-isel{width:auto;min-width:140px;}\n'
            '.u10-q{margin:10px 0 14px;}\n.u10-ql{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,.75);}\n.u10-qq{font-size:13px;color:rgba(255,255,255,.7);margin:2px 0 6px;line-height:1.6;}\n'
            '.u10-comps{font-size:13px!important;color:rgba(255,255,255,.6)!important;margin-bottom:4px!important;}\n'
            '.u10-card{border:1px solid rgba(255,255,255,.1);border-radius:3px;padding:12px 14px;margin:10px 0;background:rgba(255,255,255,.02);}\n.u10-card-h{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;}\n'
            '.u10-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0 12px;}\n.u10-ro{font-size:13px;color:rgba(255,255,255,.8);line-height:1.6;padding:6px 0;}\n'
            '.u10-miss{color:#e8955a;font-weight:700;}\n.u10-ok{color:#5ecba1;font-weight:700;}\n.u10-rec{margin-top:10px;}\n.u10-ta{min-height:60px;resize:vertical;line-height:1.6;}\n.u10-det{border:1px solid rgba(255,255,255,.1);border-radius:3px;margin:10px 0;background:rgba(255,255,255,.02);}\n.u10-det>summary{cursor:pointer;list-style:none;padding:11px 14px;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.82);display:flex;justify-content:space-between;align-items:center;}\n.u10-det>summary::-webkit-details-marker{display:none;}\n.u10-det>summary::after{content:"\\25BE";font-size:13px;opacity:.6;transition:transform .2s;}\n.u10-det[open]>summary::after{transform:rotate(180deg);}\n.u10-det-b{padding:2px 14px 12px;}\n\n.u10-add{margin-top:4px;}\n')

JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'u10_s5.js'), encoding='utf-8').read()
