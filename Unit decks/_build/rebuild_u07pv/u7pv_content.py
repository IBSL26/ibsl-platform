# -*- coding: utf-8 -*-
"""Unit 7 · Establishing Performance Expectations — the two performance views (Carol's "Unit 7 Amended content.docx", 14 October 2026, saved 21:37).
Her instruction (21:39): minor changes that bring in the human and the organisational performance; the rest stays the same; coherent, not just added.
Two voices: 'f' (facilitator: "the leader", "participants") and 'p' (participant: "you"). Lines marked NEW are Claude's wording."""


def x(v, f, p):
    return f if v == 'f' else p


# ── Header ───────────────────────────────────────────────────────────────────────────────────────────
SUB_F = 'Turning Delivery Goals into Genuine Ownership across the Human and Organisational Operating Systems'
DESC = {
    'f': 'Building on the S2R® Contribution Map™ and FACES developed in Unit 6, this unit establishes clear, realistic and mutually owned performance expectations. '
         'Every expectation is connected to an enterprise result, a human contribution and the organisational conditions required for delivery.',
    'p': 'Building on the S2R® Contribution Map™ and FACES you developed in Unit 6, this unit establishes clear, realistic and mutually owned performance expectations. '
         'Every expectation you establish is connected to an enterprise result, a human contribution and the organisational conditions required for delivery.',
}
KLO = ['Establish performance expectations linked to enterprise outcomes and mapped contributions.',
       'Test clarity, capability and commitment across the Human and Organisational Operating Systems.',
       'Identify cross-functional dependencies and agree accountability for enabling conditions.',
       'Demonstrate shared ownership and mutual accountability for agreed results.']

# ── Section learning outcomes (two per section) ──────────────────────────────────────────────────────
# Sections 1 to 3: her words. Section 4: 4.1 (the four steps) has left, so outcome 1 is the existing coaching outcome; outcome 2 is hers.
# Section 5: hers, without the tool name (house rule: outcomes never name a tool) and "Capstone Blueprint" for "capstone portfolio".
SLO = [
    ['Distinguish setting expectations from establishing shared ownership.', 'Identify human commitments and organisational conditions that require agreement.'],
    ['Explain how expectation alignment affects commitment and execution.', 'Diagnose the performance consequences of unclear human and ESRG expectations.'],
    ['Identify leadership tendencies that weaken expectation alignment.', 'Locate ownership gaps across contribution relationships and enabling conditions.'],
    ['Coach individuals from partial alignment to genuine commitment.', 'Demonstrate an alignment dialogue covering commitments and ESRG dependencies.'],
    ['Establish expectations for the contributions mapped in the Capstone.', 'Record agreed commitments, ESRG conditions and alignment actions in the Capstone Blueprint.'],
]

# ── Facilitator Guide ────────────────────────────────────────────────────────────────────────────────
INTENT_ADD = ('It builds on the S2R® Contribution Map™ and FACES of Unit 6. The expectation conversation covers both performance views: '
              'the human commitments people make, and the ESRG enabling conditions the organisation provides.')   # from her Unit purpose and her first orientation
APP_OLD = '<strong>Application:</strong> Each group applies the four steps to two of its own Objectives, then prepares the alignment dialogue with its board chair.'
APP_NEW = '<strong>Application:</strong> Each group applies the four steps to two contributions from its S2R® Contribution Map™, for the people and for the organisation, then prepares the alignment dialogue with its board chair.'

# ── 1.1 ──────────────────────────────────────────────────────────────────────────────────────────────
V11 = {
    'f': 'Unit 6 has already translated enterprise outcomes into functional contributions, team and individual commitments, and the enabling conditions captured in ESRG. '
         'Unit 7 establishes agreement around that design. An assigned KPI or OKR is a proposed expectation until the contributor and relevant enabling owners have confirmed what delivery requires.',
    'p': 'In Unit 6 you translated enterprise outcomes into functional contributions, team and individual commitments, and the enabling conditions captured in ESRG. '
         'This unit establishes agreement around that design. An assigned KPI or OKR is a proposed expectation until the contributor and the relevant enabling owners have confirmed what delivery requires.',
}
V11_CARDS = [('Human Operating System', 'Human expectations', 'Describe the result, contribution, standard, timing and behaviours for which people will take responsibility.'),
             ('Organisational Operating System', 'Organisational expectations', 'Specify the Environment, Systems, Resources and Governance that the organisation will provide or resolve.')]
V11_TAIL = 'Both must be explicitly agreed.'
ROW11 = ('Enabling conditions', 'Assumed to be in place', 'Agreed with the owners of the Environment, Systems, Resources and Governance')   # NEW row, after "Result"

# ── 1.2 (her rewritten part) ────────────────────────────────────────────────────────────────────────
def P12(v):
    L = lambda f, p: x(v, f, p)
    intro = [
        'Establishing performance expectations is a leadership process through which strategic contributions become understood, achievable and consciously owned.',
        L('In Unit 6, the S2R® Contribution Map™ established how enterprise results depend on the contributions of business functions, teams and individuals. It also identified the organisational conditions required to support those contributions.',
          'In Unit 6, your S2R® Contribution Map™ established how enterprise results depend on the contributions of business functions, teams and individuals. It also identified the organisational conditions required to support those contributions.'),
        L('The next responsibility is to ensure that these expectations are genuinely established with everyone involved in delivering the results.',
          'Your next responsibility is to ensure that these expectations are genuinely established with everyone involved in delivering the results.'),
        'Three conditions must be addressed: <strong>Clarity, Capability and Commitment.</strong> Together, they establish accountability across two interconnected operating systems:',
    ]
    systems = [('Human Operating System', 'What individuals and teams must deliver, how they must perform and the behaviours expected of them.'),
               ('Organisational Operating System (ESRG)', 'The environment, systems, resources and governance arrangements that must support delivery.')]
    lead = 'Each condition answers a fundamental leadership question.'
    clarity = (
        '<p>Clarity establishes a shared understanding of the expected contribution.</p>'
        '<p>A performance expectation must connect directly to the enterprise result it supports. Individuals and teams need to understand the contribution they are responsible for, the standard of performance required and how success will be demonstrated.</p>'
        + L('<p>Clarity must also extend to the organisation’s responsibilities. Leaders need to establish what support, decisions and enabling conditions must be provided for the contribution to be delivered.</p>',
            '<p>Clarity must also extend to the organisation’s responsibilities. As the leader, you establish what support, decisions and enabling conditions must be provided for the contribution to be delivered.</p>') +
        '<p class="u7v-h">Clarity in the Human Operating System</p>'
        + L('<p>The leader and individual establish a shared understanding of:</p>', '<p>You and the individual establish a shared understanding of:</p>') +
        '<ol class="u7v-l"><li><strong>Strategic contribution:</strong> Which enterprise objective or result does this work support?</li>'
        '<li><strong>Performance expectations:</strong> What KPI, OKR or other agreed deliverable defines success?</li>'
        '<li><strong>Performance standard:</strong> What level of quality, quantity, timeliness or consistency is required?</li>'
        '<li><strong>Behavioural expectations:</strong> What observable behaviours and ways of working are necessary?</li>'
        '<li><strong>Evidence:</strong> How will successful performance be demonstrated and assessed?</li></ol>'
        '<p class="u7v-h">Clarity in the Organisational Operating System (ESRG)</p>'
        + L('<p>The leader establishes what the organisation must provide:</p>', '<p>You establish what the organisation must provide:</p>') +
        '<ul class="u7v-l"><li><strong>Environment:</strong> What working conditions, relationships or cultural practices must support delivery?</li>'
        '<li><strong>Systems:</strong> What processes, technology, information and coordination mechanisms must function?</li>'
        '<li><strong>Resources:</strong> What people, skills, time, funding or equipment must be available?</li>'
        '<li><strong>Governance:</strong> What decisions, authority, approvals and escalation arrangements must be established?</li></ul>'
        '<div class="hbox"><p><strong>Clarity is established when the parties share the same understanding of both the expected contribution and the conditions required to deliver it.</strong></p></div>'
        '<div class="p-insight">Test: Ask someone on your team to describe what success looks like for their key result. If the description differs from yours, clarity has not yet been established.</div>')
    capability = (
        '<p>Capability establishes whether the expectation is achievable under the conditions in which performance must occur.</p>'
        '<p>An individual may understand an expectation perfectly and be willing to deliver it, yet lack the skills, capacity, resources or organisational support required. This makes capability a shared leadership responsibility.</p>'
        '<p class="u7v-h">Capability in the Human Operating System</p>'
        + L('<p>The leader assesses whether the individual or team has:</p>', '<p>You assess whether the individual or team has:</p>') +
        '<ol class="u7v-l"><li><strong>Competence:</strong> The knowledge and skills required to perform the work.</li>'
        '<li><strong>Capacity:</strong> Sufficient time and workload capacity to meet the expectation.</li>'
        '<li><strong>Readiness:</strong> The confidence, experience and practical preparation needed to begin.</li>'
        '<li><strong>Coordination:</strong> Access to the colleagues and teams whose contributions affect the result.</li></ol>'
        + L('<p>Where gaps exist, the leader and individual agree on appropriate development, support or adjustments.</p>', '<p>Where gaps exist, you and the individual agree on appropriate development, support or adjustments.</p>') +
        '<p class="u7v-h">Capability in the Organisational Operating System (ESRG)</p>'
        + L('<p>The leader examines whether the organisation has established the conditions necessary for delivery.</p>', '<p>You examine whether the organisation has established the conditions necessary for delivery.</p>') +
        '<table class="u7v-t"><thead><tr><th>ESRG domain</th><th>Capability question</th></tr></thead><tbody>'
        '<tr><td><strong>Environment</strong></td><td>Do working conditions and relationships support the required performance?</td></tr>'
        '<tr><td><strong>Systems</strong></td><td>Can existing processes, technology and information support consistent delivery?</td></tr>'
        '<tr><td><strong>Resources</strong></td><td>Are the required people, funding, equipment and time available?</td></tr>'
        '<tr><td><strong>Governance</strong></td><td>Are decisions, authority and escalation mechanisms sufficiently clear and responsive?</td></tr></tbody></table>'
        + L('<p>An identified gap must lead to an agreed response. For every significant constraint, leaders establish:</p>', '<p>An identified gap must lead to an agreed response. For every significant constraint, you establish:</p>') +
        '<ul class="u7v-l"><li>What must be resolved.</li><li>Who is accountable for resolving it.</li><li>When the resolution is required.</li><li>What interim arrangements will apply if the constraint remains unresolved.</li></ul>'
        '<div class="hbox"><p><strong>Capability is established when the required human abilities and organisational conditions have been confirmed, or when identified gaps have accountable resolution arrangements.</strong></p></div>')
    commitment = (
        '<p>Commitment is the point at which a performance expectation becomes an agreed undertaking.</p>'
        '<p>Understanding an expectation does not automatically create ownership. Similarly, confirming that delivery is possible does not guarantee that the people involved have accepted responsibility for making it happen. '
        '<strong>Commitment must therefore be established through dialogue.</strong></p>'
        '<p class="u7v-h">Commitment in the Human Operating System</p>'
        '<p>The individual consciously accepts responsibility for:</p>'
        '<ol class="u7v-l"><li>Delivering the agreed contribution and performance standard.</li><li>Demonstrating the expected behaviours.</li>'
        '<li>Monitoring progress and providing reliable performance evidence.</li><li>Raising risks and constraints early.</li><li>Taking corrective action within their authority.</li></ol>'
        + L('<p>The leader must create space for the individual to question assumptions, discuss concerns and confirm what they can realistically undertake.</p>',
            '<p>You must create space for the individual to question assumptions, discuss concerns and confirm what they can realistically undertake.</p>') +
        '<p class="u7v-h">Commitment in the Organisational Operating System (ESRG)</p>'
        '<p>The leaders responsible for enabling delivery accept responsibility for:</p>'
        '<ul class="u7v-l"><li>Providing agreed resources and support.</li><li>Resolving systems and coordination constraints.</li><li>Making decisions within agreed timeframes.</li>'
        '<li>Removing organisational barriers that threaten delivery.</li><li>Responding when emerging conditions require intervention.</li></ul>'
        '<p>This creates <strong>mutual accountability</strong>: individuals own their performance commitments, while organisational leaders own the conditions they have undertaken to provide.</p>'
        '<div class="hbox"><p><strong>Commitment is established when the relevant parties have consciously accepted their respective responsibilities, including any agreed actions required to enable delivery.</strong></p></div>'
        '<div class="p-insight">The Alignment Dialogue asks: &ldquo;On a scale of 1&ndash;10, how aligned are you with the expectation for you to deliver this outcome?&rdquo; A score below 9 means Commitment is not yet established.</div>')
    conds = [('Clarity', 'Does everyone understand what is expected, why it matters and what successful delivery requires?', clarity),
             ('Capability', 'Can the people and the organisation realistically deliver what is expected?', capability),
             ('Commitment', 'Have the people responsible consciously accepted their respective responsibilities for delivering and enabling the result?', commitment)]
    principle = ('<strong>Key principle:</strong> Performance expectations are established when people understand their contribution, have a credible basis for delivering it and consciously accept responsibility, '
                 'supported by leaders who are equally accountable for the organisational conditions required for success.')
    return intro, systems, lead, conds, principle


# ── 1.3 ──────────────────────────────────────────────────────────────────────────────────────────────
CENTRAL_13 = '<strong>Central question:</strong> With whom must performance expectations be established for each contribution to succeed?'
USES_13 = {'f': 'The Expectations Chain uses the completed Contribution Map to identify the people with whom expectations must be explicitly established. It examines three directions:',
           'p': 'The Expectations Chain uses your completed Contribution Map to identify the people with whom expectations must be explicitly established. It examines three directions:'}
CHAINS = [  # arrow, name, who, what must be established, examples, key question
    ('&#8593;', 'Upline', 'Those who authorise, resource or enable delivery', 'Expectations for decisions, support, approvals and removal of constraints.',
     'Executive leadership, board members, executive sponsors, budget holders', 'Who must approve or resource this outcome for delivery to be possible?'),
    ('&#8595;', 'Downline', 'Those who perform the work', 'Expectations for results, standards, behaviours and evidence of performance.',
     'Direct reports, project teams, the teams that carry out the work', 'Who must deliver specific activities for this outcome to be achieved?'),
    ('&#8596;', 'Crossline', 'Those whose contributions are interdependent', 'Expectations for handovers, coordination, shared responsibilities and delivery commitments.',
     'Peer functions, shared service functions, suppliers, service partners, technology vendors',   # examples moved from the old Downline and External cards
     'Whose contributions must connect with this one for the outcome to be delivered?'),   # NEW
]
OUTPUT_13 = '<strong>Its output:</strong> A clear understanding of the accountability relationships in which performance expectations must be established.'
DIST_13 = [('Contribution Map', '<em>Customer Service requires IT to maintain a reliable case-management system to achieve its response-time target.</em>', 'This establishes a dependency.'),
           ('Expectations Chain', '<em>The Customer Service Executive and IT Executive must establish expectations concerning system availability, incident response times, escalation arrangements and accountability for resolving failures.</em>',
            'This establishes what must be agreed between the people responsible.')]

# ── 1.4 ──────────────────────────────────────────────────────────────────────────────────────────────
V14 = {
    'f': ['The Alignment Dialogue tests two questions together: <em>“What contribution will you deliver?”</em> and <em>“What must the organisation enable for you to deliver it?”</em> '
          'The leader asks the individual to explain the target in their own words, describe the behaviours and evidence, identify ESRG constraints and dependencies, and confirm what they can commit to.',
          'Where alignment is below the agreed threshold, the leader explores the reason, separating a clarity gap, a skill or commitment gap, and an ESRG or cross-functional constraint. '
          'The leader agrees a specific resolution owner and review date before recording the expectation as established.'],
    'p': ['The Alignment Dialogue tests two questions together: <em>“What contribution will you deliver?”</em> and <em>“What must the organisation enable for you to deliver it?”</em> '
          'You ask the individual to explain the target in their own words, describe the behaviours and evidence, identify ESRG constraints and dependencies, and confirm what they can commit to.',
          'Where alignment is below the agreed threshold, you explore the reason, separating a clarity gap, a skill or commitment gap, and an ESRG or cross-functional constraint. '
          'You agree a specific resolution owner and review date before you record the expectation as established.'],
}

# ── Section 2 ────────────────────────────────────────────────────────────────────────────────────────
V21 = ('A compliance response may emerge when people are held accountable for results while essential organisational conditions remain outside their control. '
       'Commitment strengthens when leaders visibly fulfil their side of the performance agreement: decisions, systems, resources, governance and working environment.')
V23 = {'f': 'Two failures often appear together: contributors disengage because promises of support are not honoured, and accountability becomes defensive because responsibility for the result is disconnected from authority over its enabling conditions. '
            'The expectation record must therefore distinguish the delivery owner from the ESRG resolution owner.',
       'p': 'Two failures often appear together: contributors disengage because promises of support are not honoured, and accountability becomes defensive because responsibility for the result is disconnected from authority over its enabling conditions. '
            'Your expectation record must therefore distinguish the delivery owner from the ESRG resolution owner.'}

# ── 3.1 ──────────────────────────────────────────────────────────────────────────────────────────────
V31 = {'f': 'For each role, examine the expectations it places on others and the ESRG commitments it must honour. Finance may control resources, operations may own systems and work design, HR may influence capability and environment, '
            'and executive leadership may own governance decisions. These are illustrative accountabilities; confirm actual ownership in the capstone organisation.',
       'p': 'For each role, examine the expectations it places on others and the ESRG commitments it must honour. Finance may control resources, operations may own systems and work design, HR may influence capability and environment, '
            'and executive leadership may own governance decisions. These are illustrative accountabilities; confirm actual ownership in your own organisation.'}
Q31_P = 'Ask of each role: <em>“Which expectation is this leader placing on another function, and what enabling promise is this leader making in return?”</em> An expectation without its enabling promise is an alignment gap.'   # participant wording of her facilitator question
Q31_F = 'Ask: <em>“Which expectation is this leader placing on another function, and what enabling promise is this leader making in return?”</em> Capture unowned dependencies as alignment gaps.'
CROSSLINE = {  # NEW · peer functions whose work connects with the role, then the external partners of the old External row
    'CEO': 'Strategic partners, key customers, regulators, investors',
    'CFO': 'Operations and commercial leaders whose plans drive the numbers; auditors, banks and lenders',
    'COO': 'Commercial, technology and HR leaders whose work connects with operations; suppliers, logistics partners, contractors',
    'CHRO': 'Line executives who own the people decisions; unions and employee representatives, recruitment and training partners',
    'CTO/CIO': 'Operations, finance and the functions that run on each system; technology vendors, implementation partners',
    'CMO': 'Sales, product and service leaders; agencies, media and channel partners',
    'CCO': 'Operations, finance and marketing leaders; key customers, distributors, channel partners',
    'CPO': 'Finance, operations and the budget holders who use what is bought; suppliers, contractors, logistics providers',
    'CRO': 'Finance, operations and technology leaders who own the risks; regulators, external auditors, insurers',
    'CSO': 'Finance and HR leaders who resource the strategy; strategy advisers, alliance partners',
}

# ── Section 4 ────────────────────────────────────────────────────────────────────────────────────────
S4_HERO = {'f': 'Practising the Alignment Dialogue across leadership roles &mdash; testing the contribution each person will deliver and what the organisation must enable for it.',
           'p': 'Practising the Alignment Dialogue across leadership roles &mdash; testing the contribution each person will deliver and what the organisation must enable for it.'}   # NEW
# ── Section 5 ────────────────────────────────────────────────────────────────────────────────────────
S5_HERO = {'f': 'Application · Each group establishes delivery expectations for two contributions from its S2R® Contribution Map™, for the people and for the organisation, then prepares an alignment dialogue with the board chair.',
           'p': 'Your group establishes delivery expectations for two contributions from your S2R® Contribution Map™, for the people and for the organisation, then prepares an alignment dialogue with your board chair.'}
HOW_S5_STEP1 = {'p': '<strong>5.1 · Building the Expectation Architecture.</strong> Your group selects two contributions from the Contribution Map you built in Unit 6 and takes each through the four steps, establishing a human performance expectation and the supporting ESRG expectations.',
                'f': '<strong>5.1 · Building the Expectation Architecture.</strong> Each group selects two contributions from the Contribution Map it built in Unit 6 and takes each through the four steps, establishing a human performance expectation and the supporting ESRG expectations.'}
GUIDE_BEFORE = ('<strong>Before the group starts:</strong> The drop-down lists of 5.1 hold the functions of the group’s Contribution Map (Unit 6, Section 5) and its Success in Practice statements (Unit 2). '
                'The list of 5.2 holds the Key Results of its Enterprise OKRs (Unit 3). Each group confirms them in those units first.')
GUIDE_DONE = ('<strong>A complete record:</strong> Every expectation has a clear enterprise line of sight, an accountable human owner, named ESRG enabling owners, agreed evidence and a documented alignment outcome.')   # her completion standard, worded as guidance

T51 = '5.1 &mdash; Building the Expectation Architecture'
STEPS = ['Start With the Future', 'Clarify the Delivery Expectation', 'Identify the Expectations Chain', 'Confirm Ownership']
# field id, label, part, kind, placeholder, group ('' · 'hos' people · 'esrg' organisation)
FIELD_DEFS = [
    ('fn', 'Contribution', 'sel', 'k', '', ''),
    ('obj', 'Objective', 'sel', 'k', '', ''),
    ('kr', 'Key Result', 'sel', 'k', '', ''),
    ('sipst', 'Success in Practice statement', 'future', 'k', '', ''),
    ('owner', 'Owner of the contribution', 'future', '', 'The role that must make sure this contribution is delivered, for example Head of Customer Service...', ''),
    ('sip', 'The part of that Future it serves', 'future', '', 'What this contribution moves forward in the Success in Practice statement you chose...', ''),
    ('frame', 'Leader framing', 'future', '', '“As part of our goal to become ..., we need to ...”', ''),
    ('what', 'What must be delivered', 'delivery', '', 'The contribution in result terms, with its KPI or OKR...', 'hos'),
    ('when', 'By when', 'delivery', '', 'The date by which the result must be in place...', 'hos'),
    ('std', 'To what standard', 'delivery', '', 'The level of quality, quantity, timeliness or consistency required...', 'hos'),
    ('evid', 'How success will be recognised', 'delivery', '', 'The evidence you and the owner will both accept...', 'hos'),
    ('beh', 'The behaviours expected', 'delivery', '', 'The observable behaviours and ways of working this contribution needs...', 'hos'),
    ('env', 'Environment · what must be provided, and who owns it', 'delivery', '', 'The working conditions, relationships or practices that must support delivery, and their owner...', 'esrg'),
    ('sys', 'Systems · what must function, and who owns it', 'delivery', '', 'The processes, technology, information or coordination that must work, and their owner...', 'esrg'),
    ('res', 'Resources · what must be available, and who owns it', 'delivery', '', 'The people, skills, time, funding or equipment required, and their owner...', 'esrg'),
    ('gov', 'Governance · what must be decided, and who owns it', 'delivery', '', 'The decisions, authority, approvals or escalation required, and their owner...', 'esrg'),
    ('up', 'Upline · who authorises, resources or enables delivery', 'chain', '', 'Names or functions...', ''),
    ('up_r', 'Upline · what must be established with them', 'chain', '', 'Decisions, support, approvals or removal of constraints...', ''),
    ('down', 'Downline · who performs the work', 'chain', '', 'Names or functions...', ''),
    ('down_r', 'Downline · what must be established with them', 'chain', '', 'Results, standards, behaviours and evidence of performance...', ''),
    ('cross', 'Crossline · whose contributions are interdependent with this one', 'chain', '', 'Names or functions...', ''),
    ('cross_r', 'Crossline · what must be established with them', 'chain', '', 'Handovers, coordination, shared responsibilities and delivery commitments...', ''),
    ('coord', 'Coordination required across these contributors', 'chain', '', 'Who must work with whom, and on what, for the result to be delivered...', ''),
    ('score', 'Alignment score (1 to 10)', 'own', 'n', '1–10', ''),
    ('concern', 'What stands behind the score', 'own', 'o', 'The clarity gap, skill or commitment gap, or ESRG or crossline constraint the owner raised (Evaluate It · Reality)...', ''),
    ('act', 'Actions agreed to reach a 9 or 10, with an owner and a review date for each', 'own', 'o', 'What the owner will do, what you as the leader will do, and who resolves each ESRG or crossline constraint, by when (Resolve It · Options and Will)...', ''),
    ('score2', 'Revised alignment score (1 to 10)', 'own', 'm', '1–10', ''),
]

HOW_STEP_P = [
    ['From the first drop-down list, choose two contributions. The list holds the functions your group mapped in Unit 6 for its enterprise Key Result.',
     'For each contribution, choose the Success in Practice statement it serves.',
     'Name the owner of each contribution: the role that must make sure it is delivered.',
     'For each contribution, write the part of that Future it serves.',
     'Write the leader framing: the sentence that you, as the leader, say to the owner to connect the contribution to that Future. For example: <em>“As part of our goal to become the most responsive and trusted partner in our market, we need to reduce complaint response times across the service teams.”</em>'],
    ['Read what your Contribution Map holds for each contribution.',
     'For the people (Human Operating System), state what must be delivered, by when, to what standard, how success will be recognised and the behaviours expected.',
     'For the organisation (ESRG), state what the Environment, Systems, Resources and Governance must provide, and name the owner of each condition.'],
    ['For each contribution, name the Upline and state what must be established with them.',
     'Name the Downline and state what must be established with them.',
     'Name the Crossline and state what must be established with them.',
     'State the coordination these contributors require.'],
    ['Agree which of you speaks as the leader and which of you answers as the owner of the contribution.',
     'As the leader, ask the alignment question. Record the owner’s score.',
     'Where the score is below 9, ask the GROW questions of part 1.4. Record what stands behind the score, the actions agreed with their owners and review dates, and the revised score.',
     'Where the first score is 9 or 10, the three boxes below it stay empty.'],
]
LESSON = [
    [('Step 1 · Start With the Future', 'Connect the expectation to the organisation’s Success in Practice (SiP) — so the individual understands why the outcome matters. When expectations begin with the Future, individuals understand the contribution their work makes to the broader direction.')],
    [('From part 1.2 · Clarity in the Human Operating System', 'Strategic contribution, performance expectations, performance standard, behavioural expectations and evidence.'),
     ('From part 1.2 · Clarity in the Organisational Operating System (ESRG)', 'What the Environment, Systems, Resources and Governance must provide for the contribution to be delivered.')],
    [('From part 1.3 · Upline', 'Those who authorise, resource or enable delivery: decisions, support, approvals and removal of constraints.'),
     ('From part 1.3 · Downline', 'Those who perform the work: results, standards, behaviours and evidence of performance.'),
     ('From part 1.3 · Crossline', 'Those whose contributions are interdependent: handovers, coordination, shared responsibilities and delivery commitments.')],
    [('The alignment question', '“On a scale of 1–10, how aligned are you with the expectation for you to deliver this outcome?”'),
     ('From part 1.4', 'A score of 9 or 10: proceed and confirm the commitment. Below 9: Score → Evaluate → Resolve, with the GROW questions (Goal, Reality, Options, Will). Agree a resolution owner and review date for each constraint. Then ask the alignment question again.')],
]
COMPLETES_F = [
    ['<strong>For each of the two contributions, two drop-down lists:</strong> the contribution (a function of the group’s Unit 6 Contribution Map, shown with its enterprise Key Result) · the Success in Practice statement it serves (Unit 2).',
     '<strong>Three boxes:</strong> Owner of the contribution · The part of that Future it serves · Leader framing.'],
    ['<strong>For each of the two contributions, the Contribution Map entries</strong> shown for reading.',
     '<strong>For the people, five boxes:</strong> What must be delivered · By when · To what standard · How success will be recognised · The behaviours expected.',
     '<strong>For the organisation, four boxes:</strong> Environment · Systems · Resources · Governance, each with what must be provided and who owns it.'],
    ['<strong>For each of the two contributions, two boxes for each direction</strong> (Upline, Downline, Crossline): who they are · what must be established with them.',
     '<strong>One box:</strong> Coordination required across these contributors.'],
    ['<strong>For each of the two contributions:</strong> Alignment score (1 to 10).',
     '<strong>Where the score is below 9, three boxes:</strong> What stands behind the score · Actions agreed to reach a 9 or 10, with an owner and a review date for each · Revised alignment score.'],
]

# ── Unit Summary ─────────────────────────────────────────────────────────────────────────────────────
SUM_P = {
    0: [('(the surrounding system can realistically support delivery)', '(the people and the organisation can realistically deliver what is expected)'),
        ('Commitment (the person consciously accepts ownership of the result).', 'Commitment (the people responsible consciously accept their responsibilities for delivering and enabling the result). Each condition covers both performance views: what people deliver, and the Environment, Systems, Resources and Governance the organisation provides.'),
        ('mapping the Upline, Downline, and External actors whose work affects the outcome', 'mapping the Upline, Downline and Crossline relationships in which expectations must be established')],
    3: None,
    4: None,
}
SUM_P_4 = ('You practised the Alignment Dialogue. It tests two questions together: the contribution the person will deliver, and what the organisation must enable for it. '
           'The dialogue runs Score → Evaluate → Resolve: read the score as data, explore what is preventing full alignment without challenging the number, separate a clarity gap, a skill or commitment gap and an ESRG or cross-functional constraint, '
           'then ask “What would help move your alignment to a 9 or 10?” and re-score. You practised it with the GROW model (Goal, Reality, Options, Will). '
           'Each conversation closes with three leader reflections — Alignment Rating, Primary Concern, and Action for Elevation — converting a conversation into a commitment record.')
SUM_P_4_TITLE = 'What You Practised'
SUM_P_5 = ('Your group took two contributions from its Contribution Map through the four steps of the Expectation Architecture. You connected each to your Success in Practice, '
           'clarified what the people must deliver and what the organisation must provide, mapped the Upline, Downline and Crossline relationships, and confirmed ownership through the alignment question '
           'and the Score → Evaluate → Resolve sequence. Your group then prepared the alignment dialogue that moves your board chair to a 10 on one Key Result.')
SUM_F_5_OLD = 'Each group establishes delivery expectations for two of its own Objectives, taking one Key Result under each through the four steps, and prepares the alignment dialogue with its board chair.'
SUM_F_5_NEW = 'Each group establishes delivery expectations for two contributions from its Contribution Map, taking each through the four steps for the people and for the organisation, and prepares the alignment dialogue with its board chair.'
