# -*- coding: utf-8 -*-
"""Unit 7 · Establishing Performance Expectations — content for the amended pages (Carol's amendments of 11 October 2026).
Two voices: 'p' speaks to the participant ("you"), 'f' speaks of "the leader" and "participants".
Lines marked NEW are Claude's wording. Everything else is taken from the two pages or from Carol's manuscript (deck notes)."""

# ── Unit header ──────────────────────────────────────────────────────────────────────────────────────────
DESC_P_OLD = 'This unit gives you the tools to close that gap.'
DESC_P_NEW = 'This unit gives you the tools to close the gap between a well-designed performance management system and genuine commitment to deliver it.'
# Unit Intent: Carol's own slide 1 notes of 11 October (her deck is the master)
INTENT_F = ('Unit 7 addresses the single most common reason strategy fails at the human level: expectations are communicated but never truly established. '
            'The distinction is subtle in language and profound in execution impact. The unit moves leaders from announcing targets to securing genuine ownership. '
            'This unit equips leaders to close the gap between a well-designed performance management system and genuine human commitment to deliver it.')
WATCH_APP_F = ('<strong>Application:</strong> Each group applies the four steps to two of its own Objectives, then prepares the alignment dialogue with its board chair. '
               'The closer the group stays to its real strategy, the more transferable the skill.')   # NEW

# ── 1.1 · opening from Carol's manuscript (deck notes, slide 4) ──────────────────────────────────────────
OPEN_11 = {
    'p': 'Your performance management frameworks and structures have been established. Your delivery goals have been defined. Your targets have been set. '
         'If you distributed the scorecard to your team right now, without conversation, without context, without dialogue, how many of them would feel genuinely ready to own these targets?',
    'f': 'The performance management and accountability frameworks and structures have been established. The delivery goals have been defined. The targets have been set.',
}
KPI_OLD = 'KPI as metric to be monitored'
KPI_NEW = 'Key performance indicator (KPI) as metric to be monitored'
HOW_IT_SOUNDS = ('How it sounds', '“I completed everything that was asked of me.”', '“I’ll make sure this gets delivered.”')
TEST_12 = 'Test: Ask someone on your team to describe what success looks like for their key result. If the description differs from yours, clarity has not yet been established.'

# ── 1.3 · the three chains (facilitator page wording; participant definitions in "you") ─────────────────
CHAINS = [  # arrow, name, who (f), who (p), examples, key question
    ('&#8593;', 'Upline Chain', 'Individuals the leader depends on for approval, decisions, or resources', 'Those you depend on for approval, decisions, or resources',
     'Executive leadership, board members, executive sponsors, budget holders', 'Who must approve or resource this outcome for delivery to be possible?'),
    ('&#8595;', 'Downline Chain', 'Individuals responsible for executing the work required to achieve the KPI', 'Those responsible for executing the work required to achieve the KPI',
     'Direct reports, project teams, cross-functional collaborators, shared service functions', 'Who must deliver specific activities for this outcome to be achieved?'),
    ('&#8596;', 'External Chain', 'External actors whose contributions influence delivery success', 'External actors whose contributions influence delivery success',
     'Suppliers, service partners, contractors, regulatory bodies, technology vendors', 'Which external actors influence whether this outcome can be delivered?'),
]

# ── 1.4 ─────────────────────────────────────────────────────────────────────────────────────────────────
P14 = {
    'p': ['With the Expectations Chain mapped, you conduct an Alignment Dialogue with the individuals responsible for delivering the Key Result or KPI. This is a structured conversation designed to test whether the expectation has moved from instruction to commitment.',
          'The Alignment Dialogue uses a simple scale of 1–10. A score of 9 or 10 indicates genuine ownership of delivery. Anything lower demands further deliberation through the Score → Evaluate → Resolve sequence.',
          'The power of the Alignment Dialogue lies in what the number reveals. A score of 6 is data: there is something unresolved between the expectation and the person’s readiness to own it. Your job is to find it and resolve it before execution begins.'],
    'f': ['With the Expectations Chain mapped, the leader conducts an Alignment Dialogue with the individuals responsible for delivering the Key Result or KPI. This is a structured conversation designed to test whether the expectation has moved from instruction to commitment.',
          'The Alignment Dialogue uses a simple scale of 1–10. A score of 9 or 10 indicates genuine ownership of delivery. Anything lower demands further deliberation through the Score → Evaluate → Resolve sequence.',
          'The power of the Alignment Dialogue lies in what the number reveals. A score of 6 is data: there is something unresolved between the expectation and the person’s readiness to own it. The leader’s job is to find it and resolve it before execution begins.'],
}
GUIDE_14_F = ('Introduce the Alignment Dialogue as a leadership safety system. <em>“You are asking for the score so you can help. A 9 or 10 means go. '
              'Anything below 9 means there is still work for you to do as the leader.”</em>')
SER_HEAD = 'Score → Evaluate → Resolve'
GUIDE_13_F = ('Ask participants to pick one current Key Result and post in the chat one contributor from each chain: Upline, Downline and External. Then ask: '
              '<em>“Have you had an alignment dialogue with everyone in that chain? Or only with the person holding the KPI?”</em> '
              'Most will realise they have had the conversation with one person and assumed the rest of the chain would follow. That assumption is where most execution gaps begin.')

# ── 3.1 · the ten roles: likely Expectations Chain (NEW, Carol's amendment of 11 October) ────────────────
ROLES = ['CEO', 'CFO', 'COO', 'CHRO', 'CTO/CIO', 'CMO', 'CCO', 'CPO', 'CRO', 'CSO']
AS_ROLE = {'CTO/CIO': 'CTO or CIO'}
ROLE_CHAIN = {  # Upline, Downline, External
    'CEO': ('Board chair, board committees, shareholders', 'The executive team, heads of business units, the strategy office', 'Regulators, investors, strategic partners, key customers'),
    'CFO': ('CEO, board audit and finance committees', 'Finance team, budget holders in every function, heads of business units', 'Auditors, banks and lenders, investors, tax authorities'),
    'COO': ('CEO, executive committee', 'Heads of operations, service and delivery teams, shared service functions', 'Suppliers, logistics and outsourced service partners, contractors'),
    'CHRO': ('CEO, board remuneration and people committee', 'HR business partners, line managers in every function, learning and talent teams', 'Unions and employee representatives, recruitment and training partners, labour regulators'),
    'CTO/CIO': ('CEO, executive investment committee, CFO as budget holder', 'Technology and project teams, the business owner of each system, data teams', 'Technology vendors, implementation partners, cloud and cybersecurity providers'),
    'CMO': ('CEO, CFO as budget holder', 'Marketing team, sales teams, the service teams that deliver the brand promise', 'Agencies, media and channel partners, market research providers'),
    'CCO': ('CEO, CFO for pricing and credit decisions', 'Sales and account teams, operations and service delivery teams, marketing', 'Key customers, distributors, channel partners'),
    'CPO': ('CEO or CFO, the tender or procurement committee', 'Procurement team, the functions that use what is bought, finance for payment', 'Suppliers, contractors, logistics providers'),
    'CRO': ('Board risk committee, CEO', 'Risk and compliance teams, the risk owner in each function', 'Regulators, external auditors, insurers'),
    'CSO': ('CEO, board', 'The strategy office, the executive who owns each Key Result, programme and project owners', 'Strategy advisers, alliance partners, market intelligence providers'),
}
CHAIN_HEAD = {'p': 'Your Likely Expectations Chain', 'f': 'Likely Expectations Chain'}
CHAIN_NOTE = {  # NEW
    'p': 'These are the contributors most roles like yours depend on. Your own chain depends on the Key Result in front of you.',
    'f': 'These are the contributors most leaders in this role depend on. The real chain depends on the Key Result in question.',
}
INTRO_31 = {
    'p': 'Each executive function communicates expectations through the mechanisms it controls. Explore your own role first, then the two roles closest to yours. '
         'Each card gives your typical tendency, the expectation gap it creates and your likely Expectations Chain.',
    'f_old': 'Click a role to explore its tendency and gap.',
    'f_new': 'Each role card gives the role’s typical tendency, the expectation gap it creates and its likely Expectations Chain.',
}
CEO_GAP_P = ('Your functional leaders may receive the strategic direction clearly yet lack confirmed ownership of the conditions required for delivery. '
             'The assumption that strategic clarity cascades automatically into execution commitment is your most common expectation gap.')
GUIDE_31_F = ('Teach each participant’s own role first, then the two roles closest to it. For each role, read the likely Expectations Chain and ask who is missing from it in the participant’s own organisation. '
              'Key question: <em>“What is the most important expectation you have set — but not yet established — with someone in your expectations chain? What would it take to establish it properly?”</em>')
REF6_OLD = 'The alignment dialogue I will have within 5 working days: ...'
REF6_NEW = 'The alignment dialogue I will have: ...'
CSO_Q_OLD = ' What is one alignment conversation you need to have this week?'
CSO_Q_NEW = ' What is one alignment conversation you need to have?'

# ── 4.1 · the four steps, in the participant card format on both pages ───────────────────────────────────
INTRO_41 = {
    'p': 'The Expectation Architecture provides a simple, consistent method that every leader in the organisation can use — from executives to team leaders to individual contributors — to move expectations from communication into genuine ownership.',
    'f': 'The Expectation Architecture provides a simple, consistent method that every leader in the organisation can use — from executives to team leaders to individual contributors — to move expectations from communication into genuine ownership.',
}
STEP_COL = ['#8ab0e8', None, '#5ecba1', '#c39de0']   # None = the page's own accent
STEPS_41 = [  # name, rows [(label, html)], how to explain it (facilitator, NEW)
    ('Start With the Future', [
        ('Purpose', 'Connect the expectation to the organisation’s Success in Practice (SiP) — so the individual understands why the outcome matters.'),
        ('Leader framing', '<em>“As part of our goal to become the most responsive and trusted partner in our market, we need to reduce complaint response times across the service teams. This directly enables the experience we have committed to delivering to our customers.”</em>'),
        ('Why it matters', 'When expectations begin with the Future, individuals understand the contribution their work makes to the broader direction. This shifts the conversation from compliance to purpose.')],
     'Say that every expectation starts with the future it serves. Read the leader framing on the card. Then ask: <em>“When you last communicated a delivery expectation, did you start with why it matters — or with what the number is?”</em> Let two participants answer before you move on.'),
    ('Clarify the Delivery Expectation', [
        ('Purpose', 'Define the specific outcome required — in result terms. Confirm a shared picture of what success looks like.'),
        ('Leader framing', '<em>“The outcome we need is a reduction in resolution time from 48 hours to 12 hours by the end of Q3 2026. That is the result we are holding ourselves to: the outcome we are accountable for.”</em>'),
        ('Why it matters', 'Clarity is tested by asking the individual to describe what success looks like in their own words. If the description differs from the leader’s, the expectation requires further clarification before proceeding.')],
     'Show that the outcome is stated as a result, with a measure and a date. Ask participants to restate the example outcome in their own words in the chat. Read out two versions that differ and name the difference: that difference is the clarity gap this step closes.'),
    ('Identify the Expectations Chain', [
        ('Purpose', 'Map who else must contribute for the result to be achieved. Ensure dependencies are visible before execution begins.'),
        ('Explore', 'Which teams or individuals will need to collaborate on this outcome? Whose decisions or resources directly influence the delivery of the result? Where might coordination be required across functions? Which external actors influence whether the result can be achieved?'),
        ('Why it matters', 'This step helps the individual understand the execution system surrounding the expectation — they are not delivering alone, and the leader is confirming that the full chain has been considered.')],
     'Link this step to part 1.3. For the example on the cards, ask participants to post in the chat one Upline, one Downline and one External contributor. Stress that the owner leaves this step knowing who else carries the result.'),
    ('Confirm Ownership', [
        ('Purpose', 'Confirm that the individual accepts responsibility for ensuring the outcome is delivered. This is the moment the expectation moves from instruction to commitment.'),
        ('The question', '<em>“On a scale of 1–10, how aligned are you with the expectation for you to deliver this outcome?”</em>'),
        ('What it means', 'A score of 9 or 10 indicates that the expectation has moved into genuine ownership of delivery. A score below 9 means there is an unresolved concern: move to Score → Evaluate → Resolve before execution begins.')],
     'Read the alignment question exactly as it is written. Explain the scale: 9 or 10 means ownership, and a score below 9 leads into part 4.2. Tell participants that the score is information for the leader, and that part 4.2 shows what to do with it.'),
]
HOW_41_F = [  # NEW · how to explain the four steps; it sits before the cards
    'Name the four steps in order and say that together they form one conversation between a leader and the person who must deliver.',
    'Take the one example on the cards (complaint resolution) through all four steps, so that participants see the same expectation grow from purpose to ownership.',
    'Teach each step from its card: read the Purpose, then the Leader framing, then Why it matters. Put a question to participants only once the card has been taught.',
    'Close by asking participants to post in the chat the step they most often skip. The most common omission is Step 1: leaders jump straight to the number (Step 2) and skip the Future entirely. The Future is the foundation of ownership.',
]

# ── 4.2 · Score → Evaluate → Resolve, and the GROW coaching model ───────────────────────────────────────
INTRO_42_P = ('When the alignment score is below 9, you treat the number as data: it signals that something is unresolved. You do not challenge the score or move past it. '
              'The Score → Evaluate → Resolve sequence transforms that signal into a resolved commitment.')
VOICE_42 = [  # facilitator wording -> participant wording (each found once in the three panels)
    ('<th style="padding:10px 14px;text-align:left;font-size:9px;letter-spacing:2px;text-transform:uppercase;border-bottom:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.35);">Leader action</th>', None),  # set in the build
    ('If the score is below 9, the leader explores the reasons behind the rating.', 'If the score is below 9, you explore the reasons behind the rating.'),
    ('The leader guides the conversation using diagnostic questions:', 'You guide the conversation using diagnostic questions:'),
    ('Once the sources of misalignment are understood, the leader works with the individual to resolve them.', 'Once the sources of misalignment are understood, you work with the individual to resolve them.'),
    ('Once concerns are resolved, the leader asks the alignment question again', 'Once concerns are resolved, you ask the alignment question again'),
    ('Leader&rsquo;s Reflection Capture (after the dialogue):', 'After the dialogue, capture three reflections:'),
]
CARD_42_NAMES = [('Score It', 'The individual gives their alignment score — a signal of readiness'),
                 ('Evaluate It', 'Understand what is preventing full alignment'),
                 ('Resolve It', 'Work with the individual to resolve the concern')]
GROW_HEAD = 'The GROW Coaching Model'
GROW_INTRO = {  # NEW
    'p': ['GROW is the coaching model you use when you hold the Alignment Dialogue. It is a widely used coaching model, popularised by Sir John Whitmore in <em>Coaching for Performance</em>. '
          'Its four stages are Goal, Reality, Options and Will. At each stage you ask questions and the individual does the thinking, so the answers they reach are their own.',
          'Score → Evaluate → Resolve is the sequence of the dialogue. GROW is how you coach inside it.'],
    'f': ['GROW is the coaching model the leader uses when holding the Alignment Dialogue. It is a widely used coaching model, popularised by Sir John Whitmore in <em>Coaching for Performance</em>. '
          'Its four stages are Goal, Reality, Options and Will. At each stage the leader asks questions and the individual does the thinking, so the answers the individual reaches are their own.',
          'Score → Evaluate → Resolve is the sequence of the dialogue. GROW is how the leader coaches inside it.'],
}
GROW = [  # letter, name, meaning, in the dialogue (p), in the dialogue (f), questions
    ('G', 'Goal', 'What the individual wants to reach.',
     'The goal of the dialogue is ownership of the delivery expectation: an alignment score of 9 or 10. You agree this aim at Score It, as soon as the individual has given the number.',
     'The goal of the dialogue is ownership of the delivery expectation: an alignment score of 9 or 10. The leader agrees this aim at Score It, as soon as the individual has given the number.',
     ['“What would a 9 or 10 look like for you on this outcome?”', '“What do you want to be sure of before you commit to this result?”']),
    ('R', 'Reality', 'What is true today.',
     'This is Evaluate It. You explore what stands behind the score, and you listen without defending the expectation.',
     'This is Evaluate It. The leader explores what stands behind the score, and listens without defending the expectation.',
     ['“What influenced the score you gave?”', '“What feels unclear about the expectation?”', '“What concerns do you have about delivering this outcome?”', '“Where do you anticipate obstacles or constraints?”']),
    ('O', 'Options', 'What could be done.',
     'This opens Resolve It. You ask for the individual’s ideas first, then you add your own.',
     'This opens Resolve It. The leader asks for the individual’s ideas first, then adds their own.',
     ['“What would help move your alignment from where it is now to a 9 or 10?”', '“What else could we do?”', '“What support would make the difference?”']),
    ('W', 'Will', 'What will be done, and by whom.',
     'This closes Resolve It. You agree the actions each of you will take, then you ask the alignment question again.',
     'This closes Resolve It. The leader and the individual agree the actions each will take, then the leader asks the alignment question again.',
     ['“What will you do, and what do you need me to do?”', '“What could stop this, and how will we deal with it?”', '“With that agreed, where is your alignment now, on the scale of 1–10?”']),
]
GROW_ROWS = {'p': ('What it means', 'In the Alignment Dialogue', 'Questions you ask'), 'f': ('What it means', 'In the Alignment Dialogue', 'Questions the leader asks')}
GROW_MAP = {  # NEW
    'p': '<strong>How the two fit together:</strong> Goal at Score It · Reality at Evaluate It · Options and Will at Resolve It.',
    'f': '<strong>How the two fit together:</strong> Goal at Score It · Reality at Evaluate It · Options and Will at Resolve It.',
}
GUIDE_14B_F = ('The Resolve question, <em>“What would help move your alignment from where it is now to a 9 or 10?”</em>, is the most important question in the whole architecture. '
               'It keeps the leader in the right posture: solving for the person’s ability to own it. Teach GROW as the way the leader holds that posture through the whole dialogue. '
               'Participants practise it in the role play of part 4.2.')

# ── 4.2 · Practising the Alignment Dialogue (Carol, 11 October 12:20): role play in class (facilitator), Portfolio work (participant). NEW wording. ──
T42 = '4.2 &mdash; Practising the Alignment Dialogue'
M42 = 'GROW coaching model &middot; Portfolio Work'
INTRO_42 = {
    'p': 'In part 1.4 you learned the Alignment Dialogue and the GROW coaching model. Here you prepare an Alignment Dialogue of your own, with your board chair.',
    'f': 'Part 1.4 taught the Alignment Dialogue and the GROW coaching model. In this part participants practise them: in class, through a role play that you run, and then on the portal, as Portfolio work.',
}
SCENARIO = {
    'p': '<strong>The scenario.</strong> Your board chair has disagreed with the current metric and timeframe of the Key Result you have chosen. You ask the alignment question: <em>“On a scale of 1–10, how aligned are you with this Key Result as it stands?”</em> Your chair gives a 5. Your aim is to move your chair to a 10.',
    'f': '<strong>The scenario participants work on.</strong> The board chair has disagreed with the current metric and timeframe of the Key Result the participant has chosen. The participant asks the alignment question: <em>“On a scale of 1–10, how aligned are you with this Key Result as it stands?”</em> The chair gives a 5. The participant’s aim is to move the chair to a 10.',
}
AD_KR_LABEL = 'The Key Result for which you may need an alignment dialogue with your board chair'
HOW_42_P = ['Choose from the drop-down list the Key Result for which you may need an alignment dialogue with your board chair.',
            'Read the scenario.',
            'Write your side of the dialogue under each GROW stage: Goal, Reality, Options and Will. Write the questions you ask in your own words. The lesson from part 1.4 sits above each box.',
            'Under Will, state what you and your chair agree to do and how you confirm that your chair has reached a 10.']
HOW_42_TAIL = 'This is Portfolio work. Your entries save as you type. They become part of your Learning Portfolio and reach your facilitator when you select Submit to Facilitator at the end of the unit.'
AD_FIELDS = [  # response key, label, placeholder (one for each GROW stage, in the order of GROW above)
    ('ad_goal', 'Goal · what you say and ask to agree what a 10 looks like for your chair', 'The question I ask: “...”\n\nWhat a 10 would mean for my chair: ...'),
    ('ad_reality', 'Reality · the questions you ask to understand what stands behind your chair’s score', 'On the metric, I ask: “...”\n\nOn the timeframe, I ask: “...”\n\nWhat I expect to hear: ...'),
    ('ad_options', 'Options · what you explore with your chair to resolve the metric and the timeframe', 'The Resolve question in my own words: “...”\n\nOptions for the metric: ...\n\nOptions for the timeframe: ...'),
    ('ad_will', 'Will · what you and your chair agree to do, and how you confirm that your chair has reached a 10', 'What I will do: ...\n\nWhat I ask my chair to do: ...\n\nHow I ask the alignment question again: “...”'),
]
ROLEPLAY_LABEL = 'FACILITATOR GUIDANCE — Role Play in Class · The Alignment Dialogue'
ROLEPLAY = {
    'purpose': 'Participants practise the Alignment Dialogue with the GROW model, both taught in part 1.4. You run this role play in the live session, between any two roles that you choose. Nothing is entered on the portal during the role play.',
    'decide_lead': '<strong>Decide three things when you prepare:</strong>',
    'decide': [
        '<strong>The expectation.</strong> One Key Result. Use the example of part 4.1, <em>“Reduce complaint resolution time from 48 hours to 12 hours”</em>, or a Key Result from a group’s Unit 3 Enterprise OKRs.',
        '<strong>The two roles for each round.</strong> One is the leader who establishes the expectation. The other is the owner who must deliver it. Any two roles work: CEO and COO, COO and Head of Customer Service, CFO and Head of Procurement, or an executive and the board chair.',
        '<strong>The owner brief for each round.</strong> It gives the owner’s score, the concerns behind it and what moves the owner to a 9 or 10. Two briefs for the part 4.1 example are below. Write your own in the same pattern for the roles you choose.',
    ],
    'run_lead': '<strong>Run it in this order:</strong>',
    'steps': [
        '<strong>Set it up.</strong> Say: <em>“We will now practise the Alignment Dialogue on one expectation. Listen for the four GROW stages.”</em> State the expectation and name the two roles.',
        '<strong>Give the observers their task.</strong> Everyone who is not in a role posts in the chat each GROW stage as they hear it (G, R, O or W) and the question that opened it.',
        '<strong>Round 1 · You demonstrate.</strong> You play the leader. A volunteer plays the owner. Send the volunteer the owner brief in a private chat message. Connect the expectation to the Future in one sentence, state the outcome, then ask the alignment question. Work through Score → Evaluate → Resolve with the GROW questions, and end by asking the alignment question again.',
        '<strong>Pause.</strong> Ask the observers: <em>“Which question moved the score?”</em> Read two answers from the chat.',
        '<strong>Round 2 · Participants lead.</strong> One volunteer plays the leader and a second volunteer plays the owner, in the roles you chose. Send the owner brief to the owner in a private chat message. Run further rounds with other roles as you choose.',
        '<strong>Debrief.</strong> Ask: <em>“What did the leader do when the score was low?”</em> <em>“Which concern would have stayed hidden without ‘What else?’”</em> <em>“What felt unfamiliar about asking for a score?”</em>',
        '<strong>Point to the Portfolio work.</strong> Say: <em>“On the portal, in part 4.2, you prepare an Alignment Dialogue with your board chair on one of your own Key Results.”</em>',
    ],
    'briefs': [
        ('Owner brief · example A', 'You give a 7. The outcome is clear to you. Your concern is that the billing team must answer customer queries on the same day, and nobody has agreed this with them. You move to a 9 when the leader agrees to establish that expectation with the Head of Billing.'),
        ('Owner brief · example B', 'You give a 5. You have two concerns. First, you do not know how “resolved” will be measured. Second, your team has three vacancies. Give only the first concern until the leader asks “What else?” You move to a 9 when success is defined and the two of you have agreed how the vacancies will be covered.'),
    ],
    'watch': [
        'The leader defends the target or argues with the score. Stop the round and ask the leader to return to <em>“What influenced the score you gave?”</em>',
        'The leader offers solutions before asking for the owner’s options. Ask: <em>“Whose idea was that?”</em>',
        'The dialogue ends without the alignment question being asked again. Ask: <em>“How do you know where the owner stands now?”</em>',
    ],
}
ACT_42_LEAD = 'Each participant completes part 4.2 of their own file alone, as Portfolio work:'
ACT_42_STEPS = ['They choose from a drop-down list the Key Result for which they may need an alignment dialogue with their board chair. The list holds the Key Results their group confirmed in Unit 3.',
                'They read the scenario: the board chair has disagreed with the current metric and timeframe of that Key Result and gives a 5.',
                'They write their side of the dialogue under each GROW stage (Goal, Reality, Options, Will), with the questions they ask in their own words.',
                'Under Will they state what they and the chair agree to do and how they confirm that the chair has reached a 10.']
ACT_42_TAIL = 'The work becomes part of the participant’s Learning Portfolio. It reaches you when the participant selects Submit to Facilitator at the end of the unit.'
COMPLETES_42_F = ['<strong>One drop-down list:</strong> the Key Result for which the participant may need an alignment dialogue with the board chair.',
                  '<strong>Four boxes, one for each GROW stage:</strong> Goal · Reality · Options · Will. The lesson from part 1.4 sits above each box.']

# ── Section 5 · four steps on two Objectives (group work, Capstone work; Carol's amendment of 11 October) ─
S5_TITLE = 'Establishing Delivery Expectations'
S5_OLD_H2 = 'Role Play &mdash; Establishing Delivery Expectations'
S5_LEAD = {  # NEW
    'p': 'Your group establishes delivery expectations for two Objectives of the strategy in your team’s Capstone Blueprint, then prepares an alignment dialogue with your board chair.',
    'f': 'Application · Each group establishes delivery expectations for two Objectives of the strategy in its Capstone Blueprint, then prepares an alignment dialogue with the board chair.',
}
# the two exercises of Section 5 (Carol, 11 October 12:57)
T51 = '5.1 &mdash; Building the Expectation Architecture'
M51 = 'Four steps &middot; Capstone Work'
T52 = '5.2 &mdash; Conducting the Alignment Dialogue with the Board Chair'
M52 = 'GROW coaching model &middot; Capstone Work'
# part key, name, name in confirmed_items, response key written on Confirm, heading in the group's record
PARTS = [
    ('future', 'Start With the Future', 'Expectations · Start With the Future', 'ex_future', '5.1 · Step 1 · Start With the Future'),
    ('delivery', 'Clarify the Delivery Expectation', 'Expectations · Delivery Expectation', 'ex_delivery', '5.1 · Step 2 · Clarify the Delivery Expectation'),
    ('chain', 'Identify the Expectations Chain', 'Expectations · Expectations Chain', 'ex_chain', '5.1 · Step 3 · Identify the Expectations Chain'),
    ('own', 'Confirm Ownership', 'Expectations · Ownership', 'ex_ownership', '5.1 · Step 4 · Confirm Ownership'),
    ('dialogue', 'Alignment Dialogue with the Board Chair', 'Expectations · Alignment Dialogue', 'ex_dialogue', '5.2 · Alignment Dialogue with the Board Chair'),
]
# field id (per Objective: o1_…, o2_…), label, part, kind ('' text · 'k' chosen from the Unit 3 OKRs · 'n' score 1–10 · 'o' needed only when the first score is below 9 · 'm' score, same rule), placeholder
FIELD_DEFS = [
    ('obj', 'Objective', 'sel', 'k', ''),
    ('kr', 'Key Result', 'sel', 'k', ''),
    ('sipst', 'Success in Practice statement', 'future', 'k', ''),
    ('owner', 'Owner of the Key Result', 'future', '', 'The executive role that must make sure this Key Result is delivered, for example Chief Operating Officer...'),
    ('sip', 'The part of that Future it serves', 'future', '', 'What this Key Result moves forward in the Success in Practice statement you chose...'),
    ('frame', 'Leader framing', 'future', '', '“As part of our goal to become ..., we need to ...”'),
    ('what', 'What must be delivered', 'delivery', '', 'The outcome in result terms: the change the owner must deliver...'),
    ('when', 'By when', 'delivery', '', 'The date by which the result must be in place...'),
    ('std', 'To what standard', 'delivery', '', 'The level or quality the result must reach to count as delivered...'),
    ('evid', 'How success will be recognised', 'delivery', '', 'The evidence you and the owner will both accept...'),
    ('up', 'Upline · who must approve or resource this outcome', 'chain', '', 'Names or functions...'),
    ('up_r', 'Upline · what the outcome needs from them', 'chain', '', 'The approval, decision or resource required...'),
    ('down', 'Downline · who must deliver specific activities', 'chain', '', 'Names or functions...'),
    ('down_r', 'Downline · what the outcome needs from them', 'chain', '', 'The activity each must deliver...'),
    ('ext', 'External · which external actors influence delivery', 'chain', '', 'Suppliers, partners, regulators...'),
    ('ext_r', 'External · what the outcome needs from them', 'chain', '', 'The contribution or decision required...'),
    ('coord', 'Coordination required across these contributors', 'chain', '', 'Who must work with whom, and on what, for the result to be delivered...'),
    ('score', 'Alignment score (1 to 10)', 'own', 'n', '1–10'),
    ('concern', 'What stands behind the score', 'own', 'o', 'The concerns or constraints the owner raised (Evaluate It · Reality)...'),
    ('act', 'Actions agreed to reach a 9 or 10', 'own', 'o', 'What the owner will do and what you, as the leader, will do (Resolve It · Options and Will)...'),
    ('score2', 'Revised alignment score (1 to 10)', 'own', 'm', '1–10'),
]
def fields():
    out = []
    for n in (1, 2):
        for fid, label, part, kind, ph in FIELD_DEFS:
            out.append(('o%d_%s' % (n, fid), label, part, 'Objective %d' % n, kind))
    out.append(('dg_kr', 'Key Result', 'dialogue', 'Board chair', 'k'))
    for (key, short, label, ph) in DG_FIELDS: out.append((key, short, 'dialogue', 'Board chair', ''))
    return out
PH = {f[0]: f[4] for f in FIELD_DEFS}
# 5.2 · the group's alignment dialogue with the board chair: response key, name in the record, label on the page, placeholder (NEW)
DG_FIELDS = [
    ('dg_goal', 'Goal', 'Goal · what you say and ask to agree what a 10 looks like for your chair', 'The question we ask: “...”\n\nWhat a 10 would mean for our chair: ...'),
    ('dg_reality', 'Reality', 'Reality · the questions you ask to understand what stands behind your chair’s score', 'On the metric, we ask: “...”\n\nOn the timeframe, we ask: “...”\n\nWhat we expect to hear: ...'),
    ('dg_options', 'Options', 'Options · what you explore with your chair to resolve the metric and the timeframe', 'The Resolve question in our own words: “...”\n\nOptions for the metric: ...\n\nOptions for the timeframe: ...'),
    ('dg_will', 'Will', 'Will · what you and your chair agree to do, and how you confirm that your chair has reached a 10', 'What we will do: ...\n\nWhat we ask our chair to do: ...\n\nHow we ask the alignment question again: “...”'),
]
DG_KR_LABEL = 'The Key Result for which your group may need an alignment dialogue with your board chair'
INTRO_52 = {  # NEW
    'p': 'In part 4.2 you prepared this dialogue on your own. Here your group prepares it together, and the agreed dialogue goes into your team’s Capstone Blueprint.',
    'f': 'In part 4.2 each participant prepared this dialogue alone. Here the group prepares it together, and the agreed dialogue goes into the team’s Capstone Blueprint.',
}
HOW_52_P = ['Choose from the drop-down list the Key Result for which your group may need an alignment dialogue with your board chair.',
            'Read the scenario.',
            'Agree your side of the dialogue under each GROW stage: Goal, Reality, Options and Will. Write the questions you ask in your own words. The lesson from part 1.4 sits above each box.',
            'Under Will, state what you and your chair agree to do and how you confirm that your chair has reached a 10.']
COMPLETES_52G_F = ['<strong>One drop-down list:</strong> the Key Result for which the group may need an alignment dialogue with the board chair.',
                   '<strong>Four boxes, one for each GROW stage:</strong> Goal · Reality · Options · Will. The lesson from part 1.4 sits above each box.']
ACT_S5_F = 'Participants work as a group in part %s of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'
HOW_S5 = {  # NEW · one short overview; the detail sits in the how-to box of each step
    'p': {
        'lead': 'This is group work and Capstone work. Section 5 has two exercises:',
        'steps': ['<strong>5.1 · Building the Expectation Architecture.</strong> Your group takes two Objectives, with one Key Result each, through the four steps.',
                  '<strong>5.2 · Conducting the Alignment Dialogue with the Board Chair.</strong> Your group prepares the dialogue that moves your board chair to a 10 on one Key Result.'],
        'tail': ['Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
                 'You then read your group’s record at the foot of this section and select Confirm. Your confirmed record feeds your team’s Capstone Blueprint.'],
    },
    'f': {
        'lead': 'This is group work and Capstone work. Section 5 has two exercises:',
        'steps': ['<strong>5.1 · Building the Expectation Architecture.</strong> Each group takes two Objectives, with one Key Result each, through the four steps.',
                  '<strong>5.2 · Conducting the Alignment Dialogue with the Board Chair.</strong> Each group prepares the dialogue that moves its board chair to a 10 on one Key Result.'],
        'tail': ['The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
                 'Each participant then reads the group’s record at the foot of the section and selects Confirm. The confirmed record feeds the team’s Capstone Blueprint.'],
    },
}
HOW_STEP_P = [  # NEW · "Capstone work · How to complete Step N · name"; instructions 3 and 4 of Step 1 as Carol reworded them (11 October 12:20)
    ['From the drop-down lists, choose two Objectives. For each one, choose one Key Result that belongs to it and the Success in Practice statement it serves.',
     'Name the owner of each Key Result: the executive role that must make sure it is delivered.',
     'For each Key Result, write the part of that Future it serves.',
     'Write the leader framing: the sentence that you, as the leader, say to the owner to connect the Key Result to that Future. For example: <em>“As part of our goal to become the most responsive and trusted partner in our market, we need to reduce complaint response times across the service teams.”</em>'],
    ['For each Key Result, state what must be delivered, as a result the owner can be held to.',
     'State by when the result must be in place.',
     'State the standard the result must meet.',
     'State how success will be recognised: the evidence you and the owner will both accept.'],
    ['For each Key Result, name the Upline contributors and state what the outcome needs from them.',
     'Name the Downline contributors and state what the outcome needs from them.',
     'Name the External contributors and state what the outcome needs from them.',
     'State the coordination these contributors require.'],
    ['Agree which of you speaks as the leader and which of you answers as the owner of the Key Result.',
     'As the leader, ask the alignment question. Record the owner’s score.',
     'Where the score is below 9, ask the GROW questions of part 1.4. Record what stands behind the score, the actions agreed and the revised score.',
     'Where the first score is 9 or 10, the three boxes below it stay empty.'],
]
LESSON = [  # what sits above the boxes of each step: (source label, text)
    [('From part 4.1 · Step 1', 'Connect the expectation to the organisation’s Success in Practice (SiP) — so the individual understands why the outcome matters. When expectations begin with the Future, individuals understand the contribution their work makes to the broader direction.')],
    [('From part 4.1 · Step 2', 'Define the specific outcome required — in result terms. Confirm a shared picture of what success looks like.'),
     ('From part 1.2 · Clarity', 'Clarity means understanding the full picture of the expected outcome: what must be delivered, by when, at what standard, and how success will be recognised.')],
    [('From part 1.3 · Upline', 'Who must approve or resource this outcome for delivery to be possible?'),
     ('From part 1.3 · Downline', 'Who must deliver specific activities for this outcome to be achieved?'),
     ('From part 1.3 · External', 'Which external actors influence whether this outcome can be delivered?')],
    [('From part 4.1 · The alignment question', '“On a scale of 1–10, how aligned are you with the expectation for you to deliver this outcome?”'),
     ('From part 1.4', 'A score of 9 or 10: proceed and confirm the commitment. Below 9: Score → Evaluate → Resolve, with the GROW questions (Goal, Reality, Options, Will). Then ask the alignment question again.')],
]
GUIDE_S5_F = [  # NEW · the facilitator guides how the work is completed; Capstone work is reviewed independently at graduation (Carol, 11 October 12:57)
    '<strong>Your role:</strong> Guide how the work is completed. The Capstone work is reviewed independently at graduation.',
    '<strong>Order:</strong> Each group completes 5.1, then 5.2.',
    '<strong>Before the group starts:</strong> The drop-down lists hold the group’s Enterprise OKRs and its Success in Practice statements. Each group confirms them in Unit 3, part 4.2, and in Unit 2 first.',
    '<strong>To finish:</strong> Each participant reads the group’s record at the foot of Section 5 and selects Confirm.',
]
COMPLETES_F = [
    ['<strong>For each of the two Objectives, three drop-down lists:</strong> the Objective · one Key Result of that Objective · the Success in Practice statement it serves. The lists hold the group’s confirmed Unit 3 Enterprise OKRs and Unit 2 SiP statements.',
     '<strong>Three boxes:</strong> Owner of the Key Result · The part of that Future it serves · Leader framing.'],
    ['<strong>For each of the two Objectives, four boxes:</strong> What must be delivered · By when · To what standard · How success will be recognised.'],
    ['<strong>For each of the two Objectives, two boxes for each chain</strong> (Upline, Downline, External): who they are · what the outcome needs from them.',
     '<strong>One box:</strong> Coordination required across these contributors.'],
    ['<strong>For each of the two Objectives:</strong> Alignment score (1 to 10).',
     '<strong>Where the score is below 9, three boxes:</strong> What stands behind the score · Actions agreed to reach a 9 or 10 · Revised alignment score.'],
]

# ── PARTICIPANT ACTIVITY notes for the eight reflections (facilitator page) ──────────────────────────────
REF = 'Participants write a reflection in their own file: '
ACT = {
    '1.1': 'the last time they communicated a delivery expectation, whether it was set or established, and how they know.',
    '1.2': 'which of the three conditions they most consistently confirm and which they most often assume.',
    '1.3': 'their Expectations Chain for one current Key Result, and the contributors with whom they have not yet had an alignment dialogue.',
    '2.1': 'what happens first when their team hits an unexpected obstacle, and what that says about the execution dynamic they have created.',
    '2.2': 'the mechanism most absent in their current execution environment, and the cost of that absence.',
    '3.1': 'the most important expectation they have set but not yet established, and who in their chain needs that alignment dialogue.',
    '4.1': 'the step of the four they most often move through too quickly, and what would change if they gave it more attention.',
    '1.4': 'the Resolve question in their own words, applied to a real expectation they are currently facing.',
}

# ── Unit Summary ─────────────────────────────────────────────────────────────────────────────────────────
SUM_P_EDITS = [  # (old, new) in the participant SUMMARY bodies
    ('Execution begins when the person responsible internalises the expectation and accepts ownership.', 'You saw that execution begins when the person responsible internalises the expectation and accepts ownership.'),
    ('(top-down instruction; understanding assumed to equal commitment) versus Establishing one', '(top-down instruction; understanding assumed to equal commitment) and Establishing one'),
    ('The moment expectations are clarified between leader and contributor is the moment', 'You saw that the moment expectations are clarified between leader and contributor is the moment'),
    ('The issue is rarely effort — it is that ownership was assigned without being secured.', 'The issue is that ownership was assigned without being secured.'),
    ('The expectations gap is not random — it concentrates by executive function. Each CXO communicates expectations through the mechanisms it controls',
     'You saw that the expectations gap concentrates by executive function. Each executive role, yours included, communicates expectations through the mechanisms it controls'),
    ('The Expectation Architecture is a four-step practice every leader can apply consistently.', 'You saw that the Expectation Architecture is a four-step practice you can apply consistently.'),
    ('then ask “What would help move your alignment to a 9 or 10?” and re-score.', 'then ask “What would help move your alignment to a 9 or 10?” and re-score. You practised this dialogue with the GROW model (Goal, Reality, Options, Will).'),
    ('(a score below 9 means commitment is not yet established).', '(a score below 9 means commitment is not yet established). The dialogue runs Score → Evaluate → Resolve, and GROW (Goal, Reality, Options, Will) is the coaching model you use inside it.'),
]
SUM_P_5 = {'arc': 'Application — In Practice', 'title': 'What You Applied',
           'body': 'Your group established delivery expectations for two of its own Objectives. For one Key Result under each, you connected the result to your Success in Practice, defined what must be delivered, mapped the Expectations Chain and confirmed ownership through the alignment question and the Score → Evaluate → Resolve sequence. Your group then prepared the alignment dialogue that moves your board chair to a 10 on one Key Result.'}   # NEW
SUM_F_4_OLD = 'create a shared leadership discipline that transforms expectation-setting into a commitment practice.'
SUM_F_4_NEW = 'create a shared leadership discipline that transforms expectation-setting into a commitment practice. Participants practise the dialogue with the GROW model (Goal, Reality, Options, Will).'
SUM_F_5 = ('Application — In Practice', 'Each group establishes delivery expectations for two of its own Objectives, taking one Key Result under each through the four steps, and prepares the alignment dialogue with its board chair. The confirmed record feeds the team’s Capstone Blueprint.')   # NEW
CLOSE_F = 'Close by asking each leader to name one expectation they have set but not yet established — with a specific person in their expectations chain. Ask them to capture the score, the primary concern, and the action for elevation when they hold that alignment dialogue.'

# participant wording of two 4.1 rows (the page's own sentences)
P_41 = {
    (1, 'Why it matters'): 'Clarity is tested by asking the individual to describe what success looks like in their own words. If the description differs from yours, clarify further before proceeding.',
    (2, 'Why it matters'): 'This step helps the individual understand the execution system surrounding the expectation — they are not delivering alone.',
}

# ── Section learning outcomes, amended to the content (Carol, 11 October: "Amend the section outcomes according to the content") ──
# Section 1: her own two outcomes. Sections 3, 4 and 5: NEW wording by Claude where the old outcome described content the section does not hold. Section 2 stays.
SLO_EDITS = [
    ('Articulate expectations that are clear, consistent with enterprise outcomes and supported by the contributors they depend on.', 'Understand the distinction between setting vs establishing expectations.'),
    ('Evaluate whether individuals have the clarity, capability and commitment to own an expectation.', 'Design clarity, capability and commitment to establish expectations.'),
    ('Recognise when surface agreement masks unresolved ownership.', 'Recognise the contributors and dependencies each executive role relies on to deliver an agreed result.'),
    ('Interpret alignment conversations to confirm genuine commitment.', 'Coach individuals from partial alignment to genuine commitment.'),
    ('Establish a delivery expectation that secures personal ownership of an agreed result.', 'Establish delivery expectations that secure personal ownership of agreed results.'),
    ('Record the commitments that make mutual accountability visible.', 'Confirm the contributors and commitments that make mutual accountability visible.'),
]
