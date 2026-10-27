# -*- coding: utf-8 -*-
"""Unit 11 Section 3 · Extrapolating as Carol gave it (27 Oct 20:35, Word "Unit_11_Section_3_Extrapolating_Revised.docx")."""
from u11_content import acc, det
from u11_s2 import tbl3, box
TITLE = 'Where Are the Organisational Health Signals?'
HERO = 'Reading the Five Observable Health Traits for people-performance signals, and testing each reading against functional bias.'
LO = ['Diagnose people-performance vulnerabilities using the Five Observable Health Traits to assess how organisational culture influences employee behaviour and contribution.',
      'Apply debiasing techniques to challenge functional assumptions and establish evidence-based assessments of organisational health.']
THERMO = [('Minimal Politics','Employees cooperate, share information and prioritise collective outcomes.','Territorial behaviour, withholding information, personal agendas and internal competition.'),
 ('Minimal Confusion','Employees understand expectations, responsibilities and their contribution to organisational priorities.','Uncertainty about expectations, conflicting instructions and inconsistent accountability.'),
 ('High Morale','Employees demonstrate commitment, initiative, confidence and willingness to contribute.','Withdrawal, reduced initiative, dissatisfaction and disengagement.'),
 ('High Productivity','Employees fulfil commitments, maintain performance standards and contribute effectively.','Declining individual contribution, repeated missed commitments and reduced discretionary effort.'),
 ('Low Turnover','Capable employees remain committed to the organisation and its purpose.','Increasing voluntary departures, retention concerns and loss of experienced employees.')]
BIAS = [
 ('CEO','Minimal Politics','“My executive team works well together, so collaboration across the organisation must be healthy.”','Test across levels','Compare executive perceptions with employee experiences of cooperation, conflict and information sharing.'),
 ('CEO','High Morale','“Employees are quiet in meetings because they have nothing to contribute.”','Examine employee experiences','Establish whether employees believe their contributions are welcomed and taken seriously.'),
 ('CFO','High Productivity','“Employment costs are increasing without equivalent output; employees must be underperforming.”','Separate effort from conditions','Examine whether employees have clear expectations, appropriate support and a culture that reinforces contribution.'),
 ('CFO','Low Turnover','“Turnover is costly, so retaining employees means our people performance is healthy.”','Examine retention quality','Assess whether the organisation is retaining capable, committed employees and understand the experiences influencing their decisions to stay.'),
 ('CHRO','Minimal Confusion','“Everyone has a job description, so role expectations must be clear.”','Test lived expectations','Compare formal role descriptions with the expectations employees actually receive from their managers.'),
 ('CHRO','High Morale','“Our engagement survey scores are positive, so employee morale is strong.”','Triangulate evidence','Compare survey findings with participation, initiative, absenteeism and employee feedback.'),
 ('CHRO','Low Turnover','“Our turnover is low, which demonstrates that employees are satisfied.”','Challenge the assumption','Examine whether employees remain because of commitment, limited alternatives or other circumstances.'),
 ('COO','Minimal Politics','“Departments are protecting their interests because employees are unwilling to cooperate.”','Examine reinforced norms','Determine whether leaders reward functional achievement while neglecting collective contribution.'),
 ('COO','High Productivity','“Employees keep missing commitments because they lack discipline.”','Trace expectations and experiences','Examine whether accountability standards are clear, consistently reinforced and experienced as fair.'),
 ('CSO','Minimal Confusion','“We communicated the strategy clearly; employees should know what is expected.”','Verify understanding','Ask employees to explain their priorities, responsibilities and expected contributions in their own words.')]
REFLECT = ['Which of the Five Observable Health Traits do I personally strengthen through my everyday conduct?',
 'Which trait may be weakened by my own habits, responses or leadership practices?',
 'What assumptions or functional biases do I bring when interpreting the behaviour and performance of others?',
 'What specific change in my own behaviour would help me model the organisational values more consistently?']
CLOSING = 'The Five Observable Health Traits show where culture is influencing people performance. A credible assessment requires evidence, awareness of functional bias and personal accountability for the behaviours leaders reinforce.'
TRANSITION = 'Section 4 brings together functional perspectives to establish a shared view of organisational health and agree collective cultural reinforcement priorities.'

def section3(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    interp = ('<div class="hbox"><div class="u11-ci">Thermometer interpretation</div><ul class="u11-band">'
              '<li><span class="u11-b u11-b1">Strong</span>Positive behaviours are consistently observed.</li>'
              '<li><span class="u11-b u11-b2">Vulnerable</span>Negative signals are emerging or uneven.</li>'
              '<li><span class="u11-b u11-b3">Poor</span>Negative signals are persistent or widespread.</li></ul>'
              '<p>Ratings must be supported by evidence.</p></div>')
    o.append(acc('3.1 &mdash; Organisational Health Signals and the Health Thermometer',
      '<p>The Five Observable Health Traits reveal how organisational values are experienced through employee behaviour, relationships and contribution. The Organisational Health Thermometer uses these same traits to assess whether people-performance conditions are strong, vulnerable or poor. Assess each trait using observable employee behaviour and supporting evidence.</p>\n'
      + tbl3(['Health Trait', 'Strong Health — People-Performance Signals', 'Vulnerable Health — Emerging Signals'], THERMO) + '\n' + interp + '\n'
      '<p>For each trait, compare observed employee behaviour with the thermometer descriptions, identify supporting evidence and record whether the condition is strong, vulnerable or poor. A poor condition reflects persistent or widespread vulnerability signals. This assessment identifies where organisational health may be affecting people performance; Section 3.2 examines how functional bias may influence the interpretation.</p>', True))
    roles = []
    for r in ['CEO', 'CFO', 'CHRO', 'COO', 'CSO']:
        rows = [b for b in BIAS if b[0] == r]
        body = ''.join('<div class="u11-bias"><div class="u11-bias-t">%s</div><p><strong>Potential biased interpretation:</strong> <em>%s</em></p><p><strong>Debiasing technique &mdash; %s:</strong> %s</p></div>' % (b[1], b[2], b[3], b[4]) for b in rows)
        roles.append(det('%s &middot; %s' % (r, ' · '.join(b[1] for b in rows)), body, r == 'CEO'))
    o.append(acc('3.2 &mdash; CXO Functional Bias in Organisational Health Diagnosis',
      '<p>Executives interpret organisational health through the people-performance signals they encounter in their respective functions. Their responsibilities influence what they observe, what they consider important and how they explain employee behaviour.</p>\n'
      '<p>Functional bias occurs when an executive’s professional perspective influences the interpretation of organisational health signals, potentially leading to an incomplete or inaccurate diagnosis.</p>\n'
      '<p>The Five Observable Health Traits provide a common basis for examining these differences.</p>\n'
      '<h4 class="u11-h">CXO Functional Bias and Debiasing Matrix</h4>\n' + '\n'.join(roles) + '\n'
      '<p class="u11-note">These examples illustrate potential functional biases. They do not imply that executives in these roles necessarily hold these assumptions.</p>\n'
      + box('Key insight', 'The Five Observable Health Traits reveal where people-performance vulnerabilities are emerging. Executives strengthen diagnosis by recognising how their functional perspectives may influence interpretation and applying appropriate debiasing techniques.'), meta='Select each executive to open the examples'))
    o.append(acc('3.3 &mdash; Self-Reflection: My Organisational Health Profile',
      '<ol class="u11-ol">%s</ol>' % ''.join('<li>%s%s</li>' % ('' if fac else '<strong>Reflect:</strong> ', q) for q in REFLECT)))
    o.append('<div class="hbox"><div class="u11-ci">Section Closing Insight</div><p>%s</p></div>' % CLOSING)
    o.append('<div class="hbox"><div class="u11-ci">Transition to Section 4 &mdash; Integration: Collective</div><p>%s</p></div>' % TRANSITION)
    return '\n'.join(o) + '\n'

def css(fac):
    return ('.u11-band{list-style:none;padding:0;margin:4px 0 8px;}\n.u11-band li{font-size:13px;line-height:1.7;color:rgba(255,255,255,.75);margin:6px 0;}\n'
            '.u11-b{display:inline-block;min-width:92px;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:3px 8px;border-radius:3px;margin-right:10px;text-align:center;}\n'
            '.u11-b1{background:rgba(27,94,32,.3);color:#a5d6a7;}.u11-b2{background:rgba(230,81,0,.22);color:#ffcc80;}.u11-b3{background:rgba(183,28,28,.25);color:#ef9a9a;}\n'
            '.u11-bias{border-top:1px solid rgba(255,255,255,.07);padding:10px 0 2px;}.u11-bias:first-child{border-top:none;}\n'
            '.u11-bias-t{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:4px;}\n.u11-bias p{font-size:13px;line-height:1.75;margin-bottom:6px;}\n') % ('var(--gold)' if fac else 'var(--teall)')
