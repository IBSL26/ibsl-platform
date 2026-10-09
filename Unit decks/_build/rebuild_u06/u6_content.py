# -*- coding: utf-8 -*-
"""Unit 6 · Performance Management Setup — content of Carol's amendments of 9 October 2026.
Carol's own wording is kept. Lines marked NEW are Claude's wording and await her review.
v is the page: 'p' (participant, speaks to "you") or 'f' (facilitator, speaks of participants and leaders)."""

# ── 1.4 · Leader's Response: introduction ────────────────────────────────────────────────────────
# Facilitator page: Carol's narrative in full. Two of her sentences are reworded for Rule 13 (see RULE13).
INTRO_14_F = [
 ('p', 'A rating scale only has value if it is consistently understood and each rating triggers a defined leadership response.'),
 ('p', 'A good performance management system reduces subjectivity in how people’s performance is evaluated. It gives managers a common language for discussing contribution, results, behaviour and development.'),
 ('p', 'That is why many organisations use a numbered rating system. The number is meant to create consistency. It helps managers avoid vague judgements such as “doing well”, “not trying hard enough”, or “needs improvement” without evidence.'),
 ('p', 'But the rating scale only works when everyone understands what each number means. For example, a rating of 3 should not mean “average” to one manager, “safe” to another manager, and “not good enough” to another. If the meaning is unclear, the system becomes subjective again, even though it looks objective.'),
 ('h', '<strong>The real value of a rating scale lies in the leadership action that follows the number.</strong>'),
 ('p', 'To maintain objectivity within the Performance Management system, organisations use a standardised scoring scale, typically a 1 to 5 scale. This scale defines, in precise and measurable terms, what each rating represents, ensuring a common language of performance that transcends departmental boundaries and minimises individual manager bias.'),
 ('p', 'Each point on the scale is clearly defined with explicit performance descriptors and criteria. This ensures that ratings are based on demonstrated evidence of performance against agreed expectations, with subjective judgement removed. The scale is applied at an individual level across all performance components, with ratings assigned based on verifiable outcomes, behavioural demonstration, and delivery against Key Results or KPIs.'),
 ('p', 'By anchoring performance in clearly defined standards, the system achieves three critical outcomes:'),
 ('ul', ['<strong>Personal bias is significantly reduced:</strong> ratings can be challenged and defended against explicit criteria, which take the place of managerial opinion.',
         '<strong>A shared language of performance is established across teams and functions:</strong> a “3” means the same thing in Finance as it does in Operations.',
         '<strong>Evaluation becomes consistent, comparable, and defensible,</strong> enabling fair decisions on rewards, development, and advancement.']),
 ('p', '<strong>A rating should trigger a clear leadership response.</strong>'),
 ('ul', ['If performance is strong, the response may be recognition, stretch opportunities, succession consideration, or increased responsibility.',
         'If performance is acceptable but not growing, the response may be coaching, clearer goals, or a development plan.',
         'If performance is weak, the response may be closer supervision, targeted support, performance improvement actions, or consequences where needed.']),
 ('h', 'The first question is: <em>What rating did this person receive?</em><br>The more important leadership question is: <strong><em>What must we now do because of this rating?</em></strong>'),
 ('p', 'That is why a rating scale only has value if it is consistently understood and if each rating leads to a defined leadership response that addresses current performance, whether the performance is good, average, declining or poor.'),
]
# Participant page: what carries over from the narrative above, addressed to the participant.
INTRO_14_P = [
 ('p', 'A rating scale only has value if it is consistently understood and every rating triggers a defined leadership response.'),
 ('p', 'A good performance management system reduces subjectivity in how people’s performance is evaluated. It gives you and your fellow managers a common language for discussing contribution, results, behaviour and development. The number is meant to create consistency. It helps you avoid vague judgements such as “doing well”, “not trying hard enough”, or “needs improvement” without evidence.'),
 ('p', 'The rating scale only works when everyone understands what each number means. A rating of 3 should not mean “average” to one manager, “safe” to another manager, and “not good enough” to another. If the meaning is unclear, the system becomes subjective again, even though it looks objective.'),
 ('p', 'By anchoring performance in clearly defined standards, the system achieves three critical outcomes:'),
 ('ul', ['<strong>Personal bias is significantly reduced:</strong> you can challenge and defend a rating against explicit criteria, which take the place of managerial opinion.',
         '<strong>A shared language of performance is established across teams and functions:</strong> a “3” means the same thing in Finance as it does in Operations.',
         '<strong>Evaluation becomes consistent, comparable, and defensible,</strong> enabling fair decisions on rewards, development, and advancement.']),
 ('p', '<strong>A rating should trigger a clear leadership response.</strong>'),
 ('ul', ['If performance is strong, your response may be recognition, stretch opportunities, succession consideration, or increased responsibility.',
         'If performance is acceptable but not growing, your response may be coaching, clearer goals, or a development plan.',
         'If performance is weak, your response may be closer supervision, targeted support, performance improvement actions, or consequences where needed.']),
 ('h', 'The first question is: <em>What rating did this person receive?</em><br>The more important leadership question is: <strong><em>What must we now do because of this rating?</em></strong>'),
 ('p', 'The scale below defines each level and the leadership response it requires.'),
]
RULE13 = [  # Carol's sentence -> the sentence on the page (her no-contrast rule)
 ('The real value of a rating scale is not the number itself. The value is in the leadership action that follows the number.',
  'The real value of a rating scale lies in the leadership action that follows the number.'),
 ('So the question is not only: What rating did this person receive? The more important leadership question is: What must we now do because of this rating?',
  'The first question is: What rating did this person receive? The more important leadership question is: What must we now do because of this rating?'),
]

# ── 1.5 · The Impact of a Calibrated System (new part, Carol's text) ─────────────────────────────
CAL = {
 'f': {'intro': ['When a performance management system is functioning correctly, the performance review becomes a no-surprise event.',
                 'Because the criteria are transparent and the weighting is predetermined, team members understand exactly where they stand at any given moment. They know what is being measured, how much it counts, and what each rating means, including what leadership will do in response.',
                 'This transparency produces three powerful shifts in the organisational dynamic:'],
       'shifts': [('Strategic Transparency', 'Every employee sees exactly how their specific contribution fuels the enterprise’s broader strategic goals. The line of sight between individual effort and organisational outcome becomes visible and motivating.'),
                  ('Shift in Dynamics', 'The relationship between a leader and their team evolves from one of top-down oversight to one of shared investment in a common outcome. The scorecard becomes a shared tool and stops being a judgement handed down from above.'),
                  ('Pathways to Excellence', 'The rating scale provides a clear roadmap for growth, showing exactly what is required to move from one level to the next. Ambition becomes actionable.')],
       'close': 'By anchoring ratings in clear descriptors and decision triggers, the organisation replaces subjective, instinct-based assessment with a rigorous, high-alignment framework that drives execution.'},
 'p': {'intro': ['When your performance management system is functioning correctly, the performance review becomes a no-surprise event.',
                 'Because the criteria are transparent and the weighting is predetermined, your team members understand exactly where they stand at any given moment. They know what is being measured, how much it counts, and what each rating means, including what you will do in response.',
                 'This transparency produces three powerful shifts in the organisational dynamic:'],
       'shifts': [('Strategic Transparency', 'Every employee sees exactly how their specific contribution fuels the enterprise’s broader strategic goals. The line of sight between individual effort and organisational outcome becomes visible and motivating.'),
                  ('Shift in Dynamics', 'The relationship between you and your team evolves from one of top-down oversight to one of shared investment in a common outcome. The scorecard becomes a shared tool and stops being a judgement handed down from above.'),
                  ('Pathways to Excellence', 'The rating scale provides a clear roadmap for growth, showing your team members exactly what is required to move from one level to the next. Ambition becomes actionable.')],
       'close': 'By anchoring ratings in clear descriptors and decision triggers, your organisation replaces subjective, instinct-based assessment with a rigorous, high-alignment framework that drives execution.'},
}
CAL_GUIDE_F = 'Ask: <em>“When was a performance review last a surprise to someone in your team? Which was missing: the criteria, the weighting, or the meaning of the rating?”</em> Take each of the three shifts in turn and ask for one sign that it is present in the participant’s own organisation.'   # NEW

# ── 2.1 · the bridges, beefed up from the PPT notes (manuscript detail of slides 10 and 11) ───────
BRIDGE_INTRO = {
 'f': ['Performance management is the intelligence layer that determines whether the high-level organisational objectives actually translate into observable progress, or whether they remain aspirational statements in a presentation deck that is reviewed at the beginning of the year and quietly forgotten by the middle of it.',
       'Moving from strategy design to execution requires a bridge. Without this bridge, strategic goals may be intellectually coherent but operationally invisible. They exist in language that leadership understands, but that language has not been translated into the daily decisions, priorities, and habits of the people responsible for delivery.',
       'The primary purpose of performance management is to build and sustain that bridge, ensuring that every ounce of individual effort contributes to the organisation’s strategic direction. Without it, organisations generate what might be called <strong>random acts of excellence</strong>: genuine effort, real capability, strong intentions, none of which reliably move the needle.'],
 'p': ['Performance management is the intelligence layer that determines whether your organisation’s high-level objectives actually translate into observable progress, or whether they remain aspirational statements in a presentation deck that is reviewed at the beginning of the year and quietly forgotten by the middle of it.',
       'Moving from strategy design to execution requires a bridge. Without this bridge, your strategic goals may be intellectually coherent but operationally invisible. They exist in language that you and your leadership colleagues understand, but that language has not been translated into the daily decisions, priorities, and habits of the people responsible for delivery.',
       'The primary purpose of performance management is to build and sustain that bridge, ensuring that every ounce of individual effort contributes to your organisation’s strategic direction. Without it, organisations generate what might be called <strong>random acts of excellence</strong>: genuine effort, real capability, strong intentions, none of which reliably move the needle.'],
}
BRIDGE_LOS = {
 'f': 'Performance management frameworks create a <strong>line of sight</strong>: a direct, visible connection between enterprise strategy and individual contribution. When this line of sight exists, performance management becomes a motivational system and stops being a compliance exercise. An employee can sit down on a Monday morning and understand precisely how their work connects to the organisation’s most critical outcomes.',
 'p': 'Performance management frameworks create a <strong>line of sight</strong>: a direct, visible connection between enterprise strategy and individual contribution. When this line of sight exists, performance management becomes a motivational system and stops being a compliance exercise. A member of your team can sit down on a Monday morning and understand precisely how their work connects to the organisation’s most critical outcomes.',
}
BRIDGE_PRACTICE = {   # "In practice" line added to each bridge card
 'f': ['Breaking each Key Result into functional measurable delivery signals: the specific, daily contributions required from every team. Strategy descends from the enterprise level to the desk level.',
       'Establishing exactly how performance is measured, where the data comes from, and which levers carry the most weight. This removes ambiguity and ensures that the rules of the game are agreed before the game is played.',
       'Setting incremental targets so that leaders are never guessing about whether they are on track. The calculation logic is straightforward, and it tells the leadership team exactly what “on track” looks like every single month.',
       'Establishing a cadence for reviews so that performance updates become active leadership conversations: structured moments where the team asks what this data means and what to do next. A performance update is more than a data entry.'],
 'p': ['Breaking each Key Result into functional measurable delivery signals: the specific, daily contributions required from every team. Strategy descends from the enterprise level to the desk level.',
       'Establishing exactly how performance is measured, where the data comes from, and which levers carry the most weight. This removes ambiguity and ensures that the rules of the game are agreed before the game is played.',
       'Setting incremental targets so that you are never guessing about whether you are on track. The calculation logic is straightforward, and it tells your leadership team exactly what “on track” looks like every single month.',
       'Establishing a cadence for reviews so that performance updates become active leadership conversations: structured moments where your team asks what this data means and what to do next. A performance update is more than a data entry.'],
}

# ── 2.2 · opening (Carol's order: orientations, her narration, then "The choice is rarely made…") ─
S2R_POSITION = 'A PM system fails when it is built solely for compliance, using pressure and monitoring to force results. The Strategy2Results® approach is built on a fundamentally different architecture: shared commitment, where the scorecard is a product of alignment and shared ownership, with no directive issued from above.'   # PPT notes, slide 12
COMPLIANCE = ('A compliance-driven PM depicts an environment where:', ['Leader holds accountability', 'Assessment and judgement', 'Consequence and control'])
COMMITMENT = ('A commitment-driven PM depicts an environment where:', ['Team co-owns accountability', 'Inquiry and problem-solving', 'Root cause; co-designed recovery'])

# ── 2.3 (was 2.4) · Leader vs Team: from the PPT notes (slide 14) ─────────────────────────────────
LVT_ONE_LINE = 'The team is measured on the quality and completion of specific activities. The leader is measured on the cumulative outcome that those activities produce.'
LVT_EXAMPLE = '<strong>Example:</strong> The strategic goal is to reduce complaint resolution time from 48 hours to 12 hours. The team is measured on their daily processing speed, quality of resolution, and adherence to handling protocols. The leader is measured on the steady, cumulative reduction in cycle time that demonstrates the strategy is gaining traction. If the team is active but the number is not moving, the leader must intervene.'
REF11_Q = 'Does your current PM system distinguish between the evaluation of the team or individual and the evaluation of the leader in this way: execution progress for the team member, and progress towards the strategic outcome or Key Result for the leader? If it does not, what would be your contribution to closing this gap?'
REF11_PH = 'In our current PM system, team members are evaluated on...\nLeaders are evaluated on...\n\nMy contribution to closing the gap: ...'
REF12_Q = 'What is the current PM architecture of your organisation? Which PM system is currently being used?'
REF12_PH = 'Our current PM architecture is... (for example: annual or continuous, rating-centric or development-centric, individual or team)\n\nThe PM system we currently use is... (for example: an enterprise platform, a feedback tool, or a scorecard built in Excel)'

# ── 3.1 · Unity in Diversity (the old 3.1 and 3.2 as one part) ───────────────────────────────────
BRIGADE_IMAGE = {   # PPT notes, slide 16
 'f': 'Think of the executive team as <strong>The Alignment Brigade</strong>, more than heads of departments. Every leader carries deep professional instincts about what “progress” looks like. A CFO sees progress in the margins. A CTO sees it in system uptime and deployment velocity. A CHRO sees it in engagement scores and leadership capability. These instincts are valuable, but if they are not synchronised, they create measurement imbalances that fragment the organisation’s understanding of its own performance.',
 'p': 'Think of your executive team as <strong>The Alignment Brigade</strong>, more than heads of departments. Every leader carries deep professional instincts about what “progress” looks like. A CFO sees progress in the margins. A CTO sees it in system uptime and deployment velocity. A CHRO sees it in engagement scores and leadership capability. These instincts are valuable, but if they are not synchronised, they create measurement imbalances that fragment your organisation’s understanding of its own performance.',
}
# role, zone, natural bias (PPT notes, slide 17), alignment contribution (facilitator voice, participant voice),
# participant narrative ("As …, you"), participant "when absent" line. The facilitator narrative, the PM contribution lead and the tags are read off the pages.
ROLES = [
 ('CEO', 'Enterprise Visibility', 'growth, milestones, and market position',
  'Connects the Big Picture organisational goals to functional execution signals across all departments.',
  'You connect the Big Picture organisational goals to functional execution signals across all departments.',
  'As CEO, you hold the integrated view of whether the organisation as a whole is on trajectory. Your PM role is to ensure the executive team is interpreting performance coherently and that the collective response is coordinated. Yours is the only function with authority to enforce measurement alignment across all hot zones.',
  'When your PM visibility is absent, each function optimises its own metric at the expense of enterprise coherence.'),
 ('CFO', 'Financial Signals', 'revenue, cost discipline, and ROI',
  'Links financial health to the operational drivers that create value, as well as to the outcomes they produce.',
  'You link financial health to the operational drivers that create value, as well as to the outcomes they produce.',
  'As CFO, you interpret the financial performance signal: revenue, cost, margin, liquidity, and capital efficiency. In the PM context, you translate financial data into strategic resource allocation signals — identifying where investment is producing returns and where it is absorbed without output.',
  'When your PM insight is isolated, financial data becomes a constraint and loses its value as a strategic navigation tool.'),
 ('COO', 'Execution Rhythm', 'throughput, cycle times, and reliability',
  'Creates a sustainable and measurable pace of work that actually reaches strategic targets.',
  'You create a sustainable and measurable pace of work that actually reaches strategic targets.',
  'As COO, you track the execution engine: throughput, cycle times, operational quality, and delivery consistency. You ensure operational performance rhythm is matched to strategic demand — the engine is running in the right direction at the right speed.',
  'When your PM is activity-focused, the organisation confuses motion with progress.'),
 ('CHRO', 'Capability & Behaviour', 'engagement and leadership effectiveness',
  'Ensures the “how” (culture) and the “who” (skills and capability) support execution.',
  'You ensure the “how” (culture) and the “who” (skills and capability) support execution.',
  'As CHRO, you track the capability and behaviour signal: talent pipeline health, performance distribution, leadership effectiveness, and cultural alignment. You ensure the organisation has the human capability to execute the strategy — and that behaviour is aligned to values as well as outcomes.',
  'When your PM data is absent from executive reviews, capability gaps become execution crises.'),
 ('CTO/CIO', 'System Enablement', 'system reliability and digital deployment',
  'Ensures that the data used for performance management is accurate, timely, and visible.',
  'You ensure that the data used for performance management is accurate, timely, and visible.',
  'As CTO or CIO, you track system enablement: technology performance, digital capability, data quality, and system reliability. You ensure technology is an execution accelerator. Poor system performance is a PM variable — it directly affects what people can deliver.',
  'When technology performance is excluded from PM reviews, teams are held accountable for gaps caused by system failures.'),
 ('CMO', 'Market Signal', 'brand awareness and customer sentiment',
  'Measures the customer journey from first contact to long-term advocacy.',
  'You measure the customer journey from first contact to long-term advocacy.',
  'As CMO, you track brand perception, customer acquisition costs, pipeline health, campaign performance, and market share trajectory. You provide the leading indicators of future revenue — the signal that tells the enterprise whether the market is responding to the strategy.',
  'When your PM data is lagged, the enterprise acts on market signals that are already 3–6 months old.'),
 ('CCO', 'Revenue Velocity', 'pipeline strength and conversion speed',
  'Focuses on long-term customer value ahead of short-term transactional results.',
  'You focus on long-term customer value ahead of short-term transactional results.',
  'As CCO, you track win rates, deal cycle times, customer retention, revenue per customer, and commercial pipeline conversion. You translate commercial activity into revenue trajectory signals connecting market position to financial performance.',
  'When your PM is focused on activity, the organisation mistakes effort for momentum.'),
 ('CPO', 'Supply Reliability', 'procurement efficiency and resource flow',
  'Aligns supply chain and resource availability with the organisation’s actual execution capacity.',
  'You align supply chain and resource availability with the organisation’s actual execution capacity.',
  'As CPO, you track supply reliability, product pipeline health, vendor performance, and input cost management. You ensure the supply and product infrastructure can reliably support execution — that the organisation can deliver what it has committed to deliver.',
  'When your PM is reactive, supply disruptions become execution crises that consume leadership capacity.'),
 ('CRO', 'Risk & Governance', 'compliance and operational risk signals',
  'Weaves stability and governance discipline into the way results are delivered.',
  'You weave stability and governance discipline into the way results are delivered.',
  'As CRO, you track regulatory compliance, risk appetite alignment, incident frequency, and control effectiveness. You ensure strategic ambition is pursued within a coherent risk framework — enabling bold action without reckless exposure.',
  'When your PM is siloed, risk appetite is interpreted differently across functions, creating asymmetric exposure.'),
 ('CSO', 'Strategic Coherence', 'milestone tracking and initiative health',
  'Prevents measurement drift and keeps the enterprise anchored to the original strategic intent.',
  'You prevent measurement drift and keep the enterprise anchored to the original strategic intent.',
  'As CSO, you track whether the organisation’s current activities, resource allocation, and performance trajectory are aligned to its multi-year strategic intent. You provide the strategic integrity check — ensuring operational performance is not winning at the expense of strategic positioning.',
  'When your PM is absent, operational urgency systematically erodes strategic intent over time.'),
]

# ── 4.1 · The EXECUTION Framework: FACES and EXECUTION (Carol's text) ────────────────────────────
FACES_TEST = 'FACES is the function test. It asks whether the PM system is serving its five essential purposes: building a results culture, aligning individual performance, making measurement transparent, embedding shared accountability, and supporting development. In simple terms, FACES answers: <strong>“What must this PM system achieve for people and performance?”</strong>'
EXEC_TEST = 'EXECUTION is the design quality test. It goes deeper into the architecture of the system. It asks whether the PM system has the right design principles: strategy anchoring, line of sight, evidence, collective ownership, outcomes, transparent logic, incentive alignment, review rhythm and collective insight. In simple terms, EXECUTION answers: <strong>“How must this PM system be designed so that it actually produces those functions?”</strong>'
FACES_EXEC_CLOSE = '<strong>FACES</strong> tells us what a PM system must deliver.<br><strong>EXECUTION</strong> tells us what must be designed into the system for it to deliver.'
# letter, word, name (facilitator page), principle (facilitator page), self-check (participant page)
EXEC = [
 ('E', 'ENTERPRISE', 'Strategy First', 'The PM system must be anchored to enterprise strategy. Every metric should be traceable to a strategic outcome. The enterprise intent is the filter through which all PM design decisions are made.', 'Can every metric in your PM system be traced back to a strategic priority?'),
 ('X', 'eXECUTION', 'Line-of-Sight', 'Every individual must see a clear line of sight from their daily work to enterprise strategy. Line-of-sight is the translation mechanism that makes strategy personal. Without it, individuals execute their role description and lose sight of the strategy.', 'Can every person on your team draw a line between their daily work and the strategy?'),
 ('E', 'EVIDENCE', 'Evidence-Based Measurement', 'Performance assessments must be grounded in defined, agreed evidence. Evidence-based measurement protects the integrity of the PM system and builds trust. Without it, ratings are subjective and disputes are inevitable.', 'Does your team know exactly what evidence is required to achieve each rating?'),
 ('C', 'COLLECTIVE', 'Collective Ownership', 'Accountability for results must be shared across the team and organisation. Collective ownership means everyone with a contribution to an outcome has a stake in its measurement and a responsibility for its achievement.', 'When a result is missed, does accountability sit with one person or is it genuinely shared?'),
 ('U', 'UNDERSTAND', 'Outcomes First', 'The PM system must measure outcomes — the actual change produced. A team can be 100% active while producing 0% of the required outcome. Leaders must measure impact.', 'If your team completed all planned activities this period, would outcomes automatically follow?'),
 ('T', 'TRANSPARENT', 'Measurement Logic', 'The logic by which performance is calculated, rated, and rewarded must be transparent to everyone subject to it. Hidden formulas and opaque scoring destroy confidence in the system and generate cynicism that undermines the entire PM architecture.', 'Does your team fully understand how their performance score is calculated?'),
 ('I', 'INCENTIVE', 'Incentive Alignment', 'The incentive structure must reward the behaviours and outcomes the strategy requires. Misaligned incentives are one of the most reliable predictors of strategy failure. When what gets rewarded diverges from what the strategy needs, people follow the incentive — this is a design failure.', 'What behaviours does your incentive system actually reward? Do they match your strategy?'),
 ('O', 'ONGOING', 'Review Rhythm', 'PM must be an ongoing rhythm. An annual review cycle produces information too infrequently to inform in-year course correction. The review rhythm must be consistent and embedded in the operational calendar so that PM is the way work is managed. Monthly reviews monitor operational signals. Quarterly reviews evaluate strategic progress. Annual reviews assess long-term performance and development.', 'Is PM embedded in how your team works week to week, or does it only surface at review time?'),
 ('N', 'NAVIGATE', 'Collective Insight', 'The ultimate function of a PM system is navigation: using performance data, collectively interpreted, to make better decisions about where to go and how to get there. A PM system that collects data but does not generate collective insight is a reporting system dressed as management.', 'In your last performance review, did you make a decision together that you would not have made individually?'),
]
EXEC_O_ADDED = 'Monthly reviews monitor operational signals. Quarterly reviews evaluate strategic progress. Annual reviews assess long-term performance and development.'   # PPT notes, slide 23

# ── Section 5 · Designing the PM Architecture (group work, Capstone work; Carol's four steps) ────
S5_TITLE = 'Designing the PM Architecture'   # NEW (the old title named the MyHealth Live Portal case)
RATINGS = [(1, 'Poor'), (2, 'Needs Improvement'), (3, 'Meets Expectations · Solid Gold'), (4, 'Exceeds Expectations'), (5, 'Outstanding')]
FACES = [('F', 'Foster a Results Culture'), ('A', 'Align Individual Performance'), ('C', 'Create Measurement Transparency'), ('E', 'Embed Shared Accountability'), ('S', 'Support Continuous Development')]
SIGHTS = [('Sight 1', 'Strategy'), ('Sight 2', 'Operational'), ('Sight 3', 'Behavioural & Values Alignment')]
PARTS = [  # part, step name, name written into confirmed_items, key written on Confirm
 ('scoring', 'Scoring Logic', 'PM Architecture · Scoring Logic', 'pm_scoring'),
 ('faces', 'FACES', 'PM Architecture · FACES', 'pm_faces'),
 ('execution', 'EXECUTION', 'PM Architecture · EXECUTION', 'pm_execution'),
 ('scorecards', 'PM Scorecards', 'PM Architecture · Scorecards', 'pm_scorecards'),
]
GROUP_RULE = '<strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'
GROUP_RULE_F = 'Participants work as a group, in Step %d of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'

def fields():
    """Every entry of Section 5: (id, label for the record, part, sub-heading in the record, kind). kind: t text, n weight in %, k Key Result chosen from Unit 3."""
    F = []
    for n, name in RATINGS:
        h = 'Rating %d · %s' % (n, name)
        F += [('r%d_level' % n, 'Performance level that earns this rating', 'scoring', h, 't'),
              ('r%d_evid' % n, 'Evidence required to confirm it', 'scoring', h, 't'),
              ('r%d_resp' % n, 'Leadership response in the monthly review', 'scoring', h, 't')]
    F += [('ctx', 'Contextual factors that might legitimately affect a rating', 'scoring', 'Contextual factors', 't')]
    for i, (s, name) in enumerate(SIGHTS, 1):
        F += [('sight%d' % i, '%s · %s' % (s, name), 'scoring', 'Lines of sight of progress', 't')]
    F += [('cad_what', 'Our review cadence', 'scoring', 'Review cadence', 't'), ('cad_why', 'Why this cadence', 'scoring', 'Review cadence', 't')]
    for i, (l, name) in enumerate(FACES, 1):
        F += [('faces%d' % i, '%s · %s' % (l, name), 'faces', 'The FACES of our PM architecture', 't')]
    for i, (l, word, name, _, _) in enumerate(EXEC, 1):
        F += [('exec%d' % i, '%s · %s — %s' % (l, word.capitalize() if word != 'eXECUTION' else 'eXecution', name), 'execution', 'The EXECUTION of our PM architecture', 't')]
    F += [('kr1', 'Key Result 1', 'scorecards', 'The two Key Results', 'k'), ('kr2', 'Key Result 2', 'scorecards', 'The two Key Results', 'k')]
    for r in ('CEO', 'CFO'):
        k = r.lower(); h = 'PM scorecard · ' + r
        F += [(k + '_kr1_m', 'Sight 1 · Strategy · Key Result 1 — what the %s is measured on' % r, 'scorecards', h, 't'), (k + '_kr1_w', 'Sight 1 · Strategy · Key Result 1 — weight (%)', 'scorecards', h, 'n'),
              (k + '_kr2_m', 'Sight 1 · Strategy · Key Result 2 — what the %s is measured on' % r, 'scorecards', h, 't'), (k + '_kr2_w', 'Sight 1 · Strategy · Key Result 2 — weight (%)', 'scorecards', h, 'n'),
              (k + '_op_m', 'Sight 2 · Operational — measures', 'scorecards', h, 't'), (k + '_op_w', 'Sight 2 · Operational — weight (%)', 'scorecards', h, 'n'),
              (k + '_bv_m', 'Sight 3 · Behavioural & Values — measures', 'scorecards', h, 't'), (k + '_bv_w', 'Sight 3 · Behavioural & Values — weight (%)', 'scorecards', h, 'n')]
    return F

# ── Unit Summary ─────────────────────────────────────────────────────────────────────────────────
SUM_P = [   # participant page (JSON array in the page script). Blocks 1 to 3 are the page's own text with the removed parts taken out; blocks 4 and 5 are NEW.
 {'arc': 'Awareness — What', 'title': 'What Was Established', 'body': 'Performance management and performance measurement are distinct disciplines. Measurement answers ‘what happened?’; management answers ‘what do we do about it?’ — the leadership response that turns data into decisions, actions, and accountability. The correct build sequence is therefore inverted from common practice: Define Success → Design the Management System → Design the Measurement Infrastructure → Manage Using Data (most organisations start at the last step). A complete system serves the five FACES functions — Foster a results culture, Align individual performance, Create measurement transparency, Embed shared accountability, Support continuous development. It tracks the Three Sights of Progress — Strategic OKRs, Operational KPIs, and Behavioural/Values alignment — and applies a 1–5 Rating Scale in which every rating triggers a defined leadership response and a Rating 3 (Meets Expectations) is ‘Solid Gold’. A calibrated system makes the performance review a no-surprise event and produces three shifts: Strategic Transparency, a Shift in Dynamics and Pathways to Excellence.'},
 {'arc': 'Intelligence — Why', 'title': 'Why It Matters', 'body': 'Performance management is the bridge that converts strategy into individual action through four bridge functions: Decomposing the Big Picture (enterprise outcomes → unit → team → individual), Defining the Logic of Success (a measurable, evidence-backed outcome at each level), Calibrating the Rhythm (Progress per Period = (End Target − Baseline) ÷ Number of Periods), and Structuring the Dialogue (who speaks, how often, with what authority to decide). When any function is missing, strategy leaks through the gap. Every system also rests on an architecture choice — Compliance (done to people; control and anxiety) versus Commitment (done with people; shared ownership and energy) — revealed across six dimensions. The leader is measured differently from the team: the team on in-period activities and outputs, the leader on cumulative outcome trajectory across the full cycle.'},
 {'arc': 'Extrapolating — Where', 'title': 'Where Alignment Appears', 'body': 'At enterprise scale the performance management system lives in the executive team. The Alignment Brigade concept holds that each executive function owns a distinct ‘hot zone’ it is best positioned to track; integrated through a shared cadence and language your executive team becomes a precision measurement system, but operating independently it produces competing narratives. Ten CXO Hot Zones map these contributions (CEO enterprise visibility, CFO financial signals, COO execution rhythm, CHRO capability & behaviour, and so on), each with its natural bias and its alignment contribution. Three Execution Gaps account for most enterprise PM failure — Competing Definitions of Progress, Measurement Blind Spots, and Incentive Misalignment (a design failure). The industry is shifting accordingly: 41% of organisations have moved to real-time feedback, trending from annual to continuous, rating-centric to development-centric, and individual to team performance.'},
 {'arc': 'Integration — Collective', 'title': 'What Was Built', 'body': 'FACES and EXECUTION work together. FACES is the function test: it tells you what a PM system must deliver for people and performance. EXECUTION is the design quality test: it tells you what must be designed into the system for it to deliver. The nine-principle EXECUTION framework sets the design standard — Enterprise (strategy first), eXecution (line-of-sight), Evidence-based measurement, Collective ownership, Understand outcomes first, Transparent measurement logic, Incentive alignment, Ongoing review rhythm, and Navigate by collective insight.'},
 {'arc': 'Application — In Practice', 'title': 'What You Applied', 'body': 'With your group you designed the PM architecture for the strategy in your Capstone Blueprint. You set the scoring logic: what each rating means, the evidence that confirms it, the leadership response it triggers, the lines of sight of progress and the review cadence. You described the FACES and the EXECUTION of your architecture, and you designed a PM scorecard for the CEO and for the CFO on two of your Key Results. Your group’s confirmed record feeds your team’s Capstone Blueprint.'},
]
SUM_F_4 = 'FACES tells us what a PM system must deliver. EXECUTION tells us what must be designed into the system for it to deliver: nine design principles, from strategy anchoring to collective insight.'   # NEW
SUM_F_5 = 'Each group designs the PM architecture for the strategy in its Capstone Blueprint: the scoring logic, the FACES and the EXECUTION of the architecture, and a PM scorecard for the CEO and for the CFO on two of the group’s Key Results. The confirmed record feeds the team’s Capstone Blueprint.'   # NEW
CLOSE_F = 'Close with one pointed question: <em>“Which part of your PM architecture was hardest for your group to agree, and what does that tell you about the PM system in your own organisation?”</em> <strong>Specificity is the test of whether the unit has converted into intent.</strong>'   # NEW opening; last sentence is the page's own
