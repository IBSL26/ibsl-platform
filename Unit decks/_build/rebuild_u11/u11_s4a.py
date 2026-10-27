# -*- coding: utf-8 -*-
"""Unit 11 Section 4 · Integration data as Carol gave it (27 Oct 21:10, Word "Unit_11_Section_4_Cross_CXO_Health_Architecture_Updated.docx").
Standing rule (no contrast constructions) applied to the sentences marked # SR."""
TITLE = 'Cross-CXO Health Architecture'
HERO = 'Grounding People Performance Through Collective Leadership Accountability'
LO = ['Establish a functional organisational health accountability discipline that enables executives to interpret team-generated health assessments and quantify associated people-performance losses.',
      'Consolidate functional health assessments into an enterprise organisational health position that informs collective leadership accountability and priorities for strengthening people performance.']
LEVELS = [('Functional','CXO interprets the team’s consolidated score, investigates vulnerabilities and quantifies evidenced losses.','Functional health and loss position.'),
          ('Enterprise','EXCO consolidates functional results, examines shared vulnerabilities and agrees enterprise priorities.','Enterprise health and loss position.')]
TRAITS = [
 ('Minimal Politics', ['Issues and concerns are raised openly in meetings and addressed there.',  # SR
   'Leaders share information freely, including information that could strengthen their own position.',  # SR
   'Decisions are guided by what serves the enterprise as a whole.',  # SR
   'When conflicts arise between teams, they are resolved directly and honestly through open discussion.']),  # SR
 ('Minimal Confusion', ['People understand the strategic direction and how their role contributes to it.',
   'Decision authority is clear — people know who should decide what, at what level.',
   'Responsibilities at the interfaces between teams are understood without constant escalation.',
   'Priorities are stable and consistently communicated, so people work towards one shared direction.']),  # SR
 ('High Morale', ['People invest discretionary effort — they go beyond the minimum because they believe in what we are doing.',
   'Contribution is recognised and valued in ways that feel meaningful and sincere.',  # SR
   'Even during demanding periods, the environment sustains commitment.',  # SR
   'People feel a genuine sense of belonging and purpose in this organisation.']),
 ('High Productivity', ['Work flows smoothly between teams — handoffs are clean and coordination is efficient.',
   'Meetings resolve issues and move work forward.',  # SR
   'Our systems and processes support smooth collaboration between teams.',  # SR
   'Effort converts reliably into results, with little output lost to rework or miscommunication.']),  # SR
 ('Low Turnover', ['People with capability and institutional knowledge choose to stay and grow within this organisation.',
   'Leadership behaviour creates an environment where long-term commitment feels worthwhile.',
   'Knowledge is retained when people move on.',  # SR
   'Relationships deepen over time, strengthening our collective execution capability.']),
]
TEMP = [('80–100','Healthy &amp; Thriving','Minimal politics, clear leadership, strong morale. Maintain momentum through continuous reinforcement.'),
 ('60–79','Stable but Uneven','Generally healthy but pockets of confusion or disengagement exist. Targeted intervention required.'),
 ('40–59','Caution Zone','Signs of mistrust, fatigue or unclear direction beginning to surface. Immediate leadership attention needed.'),
 ('20–39','Unhealthy','High politics, low trust and rising turnover risk. Leadership credibility is at stake.')]
OPS = [('Minimal Politics','16','8','−8','Collaboration and information sharing'),
 ('Minimal Confusion','16','12','−4','Expectations and responsibilities'),
 ('High Morale','16','8','−8','Commitment and initiative'),
 ('High Productivity','16','12','−4','Contribution and delivery'),
 ('Low Turnover','16','12','−4','Retention vulnerabilities'),
 ('OVERALL','80 /100','52 /100','−28','Caution Zone')]
LOSS = [('Lost Time','100 employees lose 30 minutes per week; hourly employment cost R200.','100 × 0.5 × R200 × 12','R120,000'),
 ('Employee Disengagement','20 employees show estimated 5% reduced contribution; quarterly employment cost R90,000 each.','20 × R90,000 × 5%','R90,000'),
 ('Declining Trust','10 managers spend 2 additional hours monthly on avoidable tensions; hourly cost R400.','10 × 2 × R400 × 3','R24,000'),
 ('Emotional Fatigue','15 employees each record one additional absence day linked to workplace strain; daily cost R1,500.','15 × R1,500','R22,500'),
 ('Talent Loss','Two avoidable departures; replacement and onboarding cost R45,000 each.','2 × R45,000','R90,000'),
 ('TOTAL','Illustrative gross exposure before overlap adjustments','','R346,500')]
POSITION = [('Accountable executive','COO'),('Assessment source','85 of 100 Operations employees (85%)'),
 ('Functional health score','52 /100 (Q1: 80 /100; change: −28)'),('Priority traits','Minimal Politics and High Morale'),
 ('Illustrative gross quarterly loss exposure','R346,500'),('Leadership priority','Examine and strengthen collaboration, trust and commitment.')]
ENT = [('Corporate','CEO','20','84','82','−2','R25,000'),('Finance','CFO','40','78','72','−6','R70,000'),
 ('Human Resources','CHRO','30','82','80','−2','R30,000'),('Operations','COO','100','80','52','−28','R346,500'),
 ('Strategy','CSO','60','78','70','−8','R95,000'),('ENTERPRISE','EXCO','250','79.8*','65.3*','−14.5*','R566,500')]
CLOSING = 'Organisational health is strengthened when leaders understand how their teams experience the culture they establish, take accountability for the resulting people-performance conditions and collectively address vulnerabilities affecting enterprise performance.'
TRANSITION = 'Participants apply the Cross-CXO Health Architecture to interpret functional health assessments, examine cultural vulnerabilities, quantify associated losses and consolidate the findings into an enterprise organisational health position.'
TRANSITION_P = 'Your group applies the Cross-CXO Health Architecture to interpret functional health assessments, examine cultural vulnerabilities, quantify associated losses and consolidate the findings into an enterprise organisational health position.'

# Individual reflection (Carol 21:11: "Add a reflection for individual at the end that goes into the personal profile for facilitator feedback"). Key ref7.
REF_TITLE = 'Individual Reflection: My Functional Health Accountability'
REF_INTRO_P = 'Reflect on the function you lead. Your reflection is saved to your personal profile, where your facilitator reads it and gives you feedback.'
REF_INTRO_F = 'Each participant completes this reflection on the function they lead. It is saved to the participant’s personal profile, where the facilitator reads it and gives feedback.'
REF_Q = ['Which of the Five Observable Health Traits would my employees most likely rate lowest on the thermometer, and what evidence do I see?',
         'Which of the five hidden costs (lost time, employee disengagement, declining trust, emotional fatigue, talent loss) is that vulnerability most likely creating in my function, and what evidence links it to organisational health?',
         'Using an assumption I can defend, what is the estimated quarterly loss exposure for that cost, and how did I calculate it?',
         'Which part of that estimate is observed loss and which is assumption, and where could it overlap with another cost category?',
         'What leadership action will I take as the accountable executive to reduce that loss, and how will I track the value recovered next quarter?']
REF_LABELS = ['Lowest-rated trait and evidence', 'Hidden cost and evidence', 'Estimated quarterly loss and calculation', 'Observed loss, assumptions and overlap', 'My leadership action and how I will track it']
