# -*- coding: utf-8 -*-
"""Unit 11 Section 2 · Intelligence as Carol gave it (27 Oct 20:21, Word "Unit_11_Section_2_Intelligence_Final.docx")."""
from u11_content import acc, tbl
TITLE = 'Why Organisational Health Determines Execution Performance'
HERO = 'How organisational health multiplies execution capability, what poor health costs the enterprise, and how health sustains performance over time.'
LO = ['Determine how organisational health can be leveraged to strengthen strategy execution capability and sustain enterprise performance.',
      'Quantify the enterprise cost of poor organisational health to direct leadership attention to its performance implications.']
MULT = [('Strategic Direction','Shared commitment strengthens alignment around organisational priorities.'),
 ('Execution Accountability','Trust and ownership support consistent delivery of commitments.'),
 ('Performance Management','Openness enables constructive performance conversations and corrective action.'),
 ('Enterprise Collaboration','Shared responsibility strengthens coordination across organisational functions.'),
 ('Organisational Adaptability','Confidence and collective commitment support responsiveness to changing conditions.')]
COSTS = [('Lost Time','Repeated work, unclear communication, unnecessary meetings and unresolved disagreements.','Reduced productivity and slower execution.'),
 ('Employee Disengagement','Reduced initiative, limited discretionary effort and withdrawal from collective responsibilities.','Lower contribution and weakened performance momentum.'),
 ('Declining Trust','Defensive communication, withholding information and protection of departmental interests.','Reduced collaboration and slower problem resolution.'),
 ('Emotional Fatigue','Persistent frustration, uncertainty, interpersonal tension and self-protective behaviour.','Reduced morale, commitment and employee effectiveness.'),
 ('Talent Loss','Capable employees leave environments characterised by poor leadership practices and unhealthy working relationships.','Loss of institutional knowledge, capability and continuity.')]
CALC = [('Lost Time','20 employees each lose 2 hours weekly to rework or unclear communication; 46 working weeks; R350 hourly cost.','20 × 2 × 46 = 1,840 hours; 1,840 × R350 = R644,000/year.'),
 ('Employee Disengagement','30 employees each contribute 1 fewer productive hour per week; 46 weeks; R300 hourly cost.','30 × 1 × 46 = 1,380 hours; indicative capacity value = R414,000/year.'),
 ('Declining Trust','Eight managers each spend 3 extra hours per month on defensive reviews and duplicated checks; R600 hourly cost.','8 × 3 × 12 = 288 hours; 288 × R600 = R172,800/year.'),
 ('Emotional Fatigue','A 50-person team records an additional 1 absence day per person annually; R2,000 average daily employment cost.','50 × 1 × R2,000 = R100,000/year in indicative absence-related employment cost.'),
 ('Talent Loss','Four avoidable departures; estimated replacement and onboarding cost of R85,000 per employee.','4 × R85,000 = R340,000/year, excluding any unmeasured disruption.')]
REFLECT = ['Where is organisational health strengthening execution performance?',
 'Which hidden costs of poor organisational health are most evident?',
 'What is the estimated annual cost of the most significant organisational health loss?',
 'Which leadership response would reduce that loss, and how would its financial impact be tracked?']
CLOSING = 'Organisational health influences how effectively strategic capabilities translate into results. When health deteriorates, execution friction increases, performance systems lose effectiveness and the cost of delivering strategy rises.'
TRANSITION = 'Section 3 examines where cultural practices and organisational health vulnerabilities are affecting performance, using the Organisational Health Thermometer to identify areas requiring leadership attention.'

def tbl3(h, rows):
    return ('<div class="u11-scroll"><table class="u11-tbl u11-tbl3"><thead><tr>%s</tr></thead><tbody>\n' % ''.join('<th>%s</th>' % x for x in h)
            + '\n'.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows) + '\n</tbody></table></div>')
def box(label, text): return '<div class="hbox"><p><strong>%s:</strong> %s</p></div>' % (label, text)
def ul(items): return '<ul>%s</ul>' % ''.join('<li>%s</li>' % x for x in items)

def section2(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    o.append(acc('2.1 &mdash; Organisational Health as a Performance Multiplier',
      '<p>Organisational health influences how effectively an organisation converts its strategic intentions into results. An organisation may have clear priorities, capable employees and established performance systems, yet their effectiveness depends partly on the culture through which people work together.</p>\n'
      '<p>When organisational health is strong, people collaborate, fulfil commitments, address problems early and focus on collective priorities. When it deteriorates, mistrust, confusion, internal competition and disengagement can reduce the effectiveness of otherwise sound strategic systems.</p>\n'
      '<h4 class="u11-h">The Multiplier Effect</h4>\n<p>Organisational health acts as a multiplier of strategy execution capability. It influences the effectiveness of existing capabilities:</p>\n'
      + tbl('Strategic Capability', 'Influence of Organisational Health', MULT) + '\n'
      + box('Key insight', 'The effectiveness of a strategy depends partly on the organisational health of the people and teams responsible for delivering it.'), True))
    o.append(acc('2.2 &mdash; Organisational Health and Execution Velocity',
      '<p>Execution velocity refers to an organisation’s ability to convert strategic priorities into coordinated action and sustained results. Organisational health influences this velocity through the quality of collaboration, communication, accountability and collective commitment.</p>\n'
      '<p>In a healthy organisation:</p>\n' + ul(['Performance concerns are raised and addressed early.','Decisions and commitments are followed through.','Information moves effectively across organisational functions.','Teams coordinate their contributions towards shared priorities.','Employees remain engaged in delivering organisational objectives.']) + '\n'
      '<p>These conditions reduce unnecessary friction and support consistent performance momentum.</p>\n'
      '<h4 class="u11-h">The Effect on Strategy Execution</h4>\n'
      '<p>Consider two organisations implementing similar strategic priorities. Both have established objectives, KPIs, execution plans and review mechanisms. In the first, leaders encourage open reporting, departments coordinate their contributions and employees take ownership of commitments. In the second, employees avoid difficult conversations, departments protect their own interests and performance reviews become defensive.</p>\n'
      '<p>Although both organisations have similar execution systems, their ability to convert those systems into results may differ significantly. The difference lies partly in the organisational health supporting execution.</p>\n'
      + box('Strategic implication', 'As organisational health deteriorates, execution friction increases and performance momentum becomes more difficult to sustain.')))
    o.append(acc('2.3 &mdash; The Price of Poor Organisational Health',
      '<p>Poor organisational health creates costs that are often overlooked because they do not appear as separate items in financial or performance reports. These costs accumulate through everyday organisational practices and eventually affect enterprise performance.</p>\n'
      + tbl3(['Hidden Cost', 'Organisational Manifestation', 'Performance Consequence'], COSTS) + '\n'
      '<h4 class="u11-h">How These Costs Accumulate</h4>\n'
      '<p>The costs of poor organisational health often remain hidden within everyday operating expenses, lost productivity and reduced employee contribution. Quantifying these losses enables executives to establish their financial impact, identify the most significant sources of performance loss and prioritise corrective interventions. By calculating the costs associated with lost time, employee disengagement, declining trust, emotional fatigue and talent loss, organisations can build a measurable business case for strengthening organisational health and track the value recovered through improvement. The following examples demonstrate how seemingly small, recurring losses can accumulate into substantial annual costs.</p>\n'
      + tbl3(['Named Hidden Cost', 'Illustrative Assumption', 'How the Cost Accumulates'], CALC) + '\n'
      '<p class="u11-note"><strong>Note:</strong> Calculations are illustrative and should be adapted using organisational data and reasonable assumptions. Overlapping costs should be adjusted to avoid double counting.</p>\n'
      + box('Key insight', 'Repeated losses in time, engagement, trust, wellbeing and retention can accumulate into a material annual cost of poor organisational health.')))
    o.append(acc('2.4 &mdash; Organisational Health and Sustained Performance',
      '<p>Organisational health influences the ability to sustain performance over time. Short-term results may be achieved through intensive intervention, individual effort or temporary pressure. Sustained performance requires a culture that consistently reinforces the behaviours necessary for collective execution.</p>\n'
      '<p>When values are embedded in everyday practices, employees develop shared expectations about accountability, collaboration, communication and performance. These expectations reduce dependence on constant leadership intervention and strengthen execution discipline.</p>\n'
      '<p>Organisational health supports:</p>\n' + ul(['Consistent execution of organisational priorities.','Constructive performance accountability.','Effective collaboration across functions.','Employee commitment and capability retention.','Organisational learning and continuous improvement.']) + '\n'
      + box('Strategic implication', 'A healthy organisation is better positioned to maintain performance discipline as leadership responsibilities, strategic priorities and operating conditions change.')))
    o.append(acc('2.5 &mdash; Executive Reflection',
      '<p>Consider an important strategic priority currently being implemented in %s:</p>\n<ol class="u11-ol">%s</ol>' % ('participants’ organisations' if fac else 'your organisation', ''.join('<li>%s%s</li>' % ('' if fac else '<strong>Reflect:</strong> ', q) for q in REFLECT))))
    o.append('<div class="hbox"><div class="u11-ci">Section Closing Insight</div><p>%s</p></div>' % CLOSING)
    o.append('<div class="hbox"><div class="u11-ci">Transition to Section 3 &mdash; Extrapolating: Where</div><p>%s</p></div>' % TRANSITION)
    return '\n'.join(o) + '\n'

def css(fac):
    return ('.u11-scroll{overflow-x:auto;max-width:100%;}\n.u11-tbl3 td:first-child{width:20%;}\n'
            '.u11-note{font-size:12px;font-style:italic;color:rgba(255,255,255,.55);}\n.u11-ol{padding-left:22px;}\n.u11-ol li{margin-bottom:8px;line-height:1.75;}\n'
            '@media (max-width:600px){.u11-tbl3{font-size:12px;}.u11-tbl3 td:first-child{width:26%;}}\n')
