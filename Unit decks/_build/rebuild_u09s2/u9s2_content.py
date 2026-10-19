# -*- coding: utf-8 -*-
"""Unit 9 · Section 2 rework and the knock-on changes in Sections 1, 4 and 5 (Carol, 19 Oct 2026, 21:04-21:29).
Wording for review. Every block here is new text unless marked as Carol's existing text."""

def cards(people, org, people_more='', org_more=''):
    pm = ''.join('<p>%s</p>' % x for x in ([people] if isinstance(people, str) else people))
    om = ''.join('<p>%s</p>' % x for x in ([org] if isinstance(org, str) else org))
    return ('<div class="u8v-hc" onclick="event.stopPropagation()"><div class="u8v-c u8v-hu"><div class="u8v-n">People performance</div>%s</div>'
            '<div class="u8v-c u8v-or"><div class="u8v-n">Organisational performance</div>%s</div></div>') % (pm, om)

# ───────── Section 1 · 1.2 opening (moved from the old 2.1, rewritten into Section 1 terms) ─────────
S1_OPEN = ('<p>When leaders define a strategy, they set a new direction for the organisation. The organisation executes that direction through what it has today: '
 'its structure, decision rights, culture, measures, capabilities and technology, and the ways of working its people have built within them. '
 'Where any of these has not yet adapted to the strategy, friction appears.</p>\n'
 '<div class="hbox"><p>Clogs form where the strategy stretches today&rsquo;s organisation beyond what it was designed to carry. A strategy that requires rapid coordination '
 'across functions exposes Structural Misfit. A strategy that depends on data-driven decisions reveals Capability Gaps. A strategy that requires decisions closer to the '
 'customer exposes Decision Bottlenecks. Each strategy places its weight on known parts of the organisation, so leaders can anticipate where its clogs will form.</p></div>\n'
 '<p>Experienced leadership teams read a clog as a signal of where the organisation must adapt next. Setting the direction is one part of their role; ensuring the '
 'organisation can carry it is the other. To read the signal, leaders examine where performance becomes constrained.</p>\n')

S1_REF3_PROMPT = None   # prompt kept as it was (the reflection picture in the deck stays accurate)
S1_REF3_PH = None
S1_REF3_PA = ('<div class="fac-note-full u9-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n'
 '<p>Participants write a reflection in their own file: the element of their operating system most likely to create friction under their current strategic direction, and why.</p>\n</div>\n')

S1_GUIDE_OLD = '<li>1.2 · Teach the two dimensions of performance, then the seven clogs one card at a time, the ABCV connection, the three lines of sight and the worked example. Participants complete the self-assessment in their own file.</li>'
S1_GUIDE_NEW = ('<li>1.2 · Teach why clogs form where the strategy stretches today&rsquo;s organisation, then the two dimensions of performance. Participants write the reflection on where their organisation is not yet ready in their own file.</li>'
 '<li>1.3 · Teach the seven clogs one card at a time.</li>'
 '<li>1.4 · Teach the Three Performance Lines of Sight.</li>'
 '<li>1.5 · Work through the worked example and the Closing Diagnostic Principle. Participants complete the self-assessment in their own file.</li>')

S1_PARTS = {  # title, sub-line
 'u': ('1.2 &mdash; Understanding Where Performance Becomes Constrained', 'Why clogs form · Two dimensions of performance'),
 'c': ('1.3 &mdash; The Seven Performance Clogs', 'ABCV-aligned · Select each clog to explore'),
 'l': ('1.4 &mdash; The Three Performance Lines of Sight from the Seven Clogs', 'From the result to its cause'),
 'w': ('1.5 &mdash; Worked Diagnostic Example: Improving Customer Service', 'Tracing the three lines of sight'),
}

# ───────── Section 2 ─────────
S2_H2 = 'Why Disciplined Intervention Clears Strategic Clogs'
S2_SUB = 'Building the three disciplines that detect, classify and resolve strategic clogs, and applying the 7 Strategic Unclogging Levers across people and organisational performance.'

S2_OPEN = ('<div class="u9-open">\n'
 '<p>Section 1 traced how a strategic clog forms and how it shows: in the result that falls short, in what individuals and teams are doing or unable to do, '
 'and in the organisational conditions behind their behaviour. A named clog still holds until leaders act on it.</p>\n'
 '<p>Leaders resolve clogs through three disciplines. They identify the clog early, while it is still a signal. They classify it accurately, so the response '
 'addresses its cause. They intervene with the lever that removes that cause. Each discipline is a habit the executive team builds through practice in every review.</p>\n'
 '<p>Early action matters because a clog compounds. The delay it causes in one function becomes the constraint on the next, and a matter that one adjustment would have '
 'resolved early grows into a recovery effort across several functions.</p>\n'
 '<p>Every response works on two sides at once. In people performance, it restores the authority, capability, focus and confidence individuals need to deliver their tasks. '
 'In organisational performance, it changes the structures, processes, systems, resources and governance so that they support the execution of those tasks. '
 'A response confined to one side leaves the clog in place on the other.</p>\n'
 '<p>Part 2.1 sets out the three disciplines. Part 2.2 sets out the 7 Strategic Unclogging Levers, the interventions leaders apply once the clog is named.</p>\n'
 '</div>\n')

S2_GUIDE_P2_OLD_START = '<p>Use the pressure point examples'
S2_GUIDE_P2_NEW = ('<p>Open with the section narrative: a named clog still holds until leaders act on it. Then teach the three disciplines one at a time, each in people performance '
 'and in organisational performance: leaders detect the signals early, name the clog with the evidence of the three lines of sight, and intervene on the condition behind it.</p>')
S2_GUIDE_P3_OLD_START = '<p>For the 7 levers'
S2_GUIDE_P3_NEW = ('<p>For the 7 levers: teach what each lever changes in people performance and in organisational performance. Rarely does a single lever clear a clog alone. '
 'The diagnostic question is always: which lever combination addresses the root cause?</p>')

DISCIPLINES = [
 ('Discipline 1', 'Early Identification', 'Detect Signals Before They Compound',
  # Carol's existing text
  ['Leaders must detect the signals that indicate friction is forming. Bottlenecks, repeated coordination failures, declining execution speed, or growing ambiguity in decision rights are all early indicators that a clog is emerging.',
   'The strategic value of early identification is significant. A clog detected when it is a friction signal requires a targeted structural adjustment. The same clog discovered six months later, after it has compounded into a systemic execution failure, requires a crisis response. The cost &mdash; in time, capital, and leadership credibility &mdash; is vastly different.',
   'This discipline requires leaders to build signal literacy: the ability to read organisational patterns as early indicators of structural misalignment.'],
  # new
  ['Early signals appear in the rhythm of work before they appear in the results. Leaders find them in three places: in the review, where the same items carry forward and explanations replace progress; in the flow of work, where hand-offs slow, approvals queue and workarounds multiply; and in conversation, where people stop raising problems or raise the same one repeatedly.',
   'The early warning signals listed for each of the seven clogs give leaders a reference to read against. Signal literacy grows through practice: leaders ask for the signals in every review, compare them across functions and record them before the result moves.'],
  'Leaders read the signals in how individuals and teams work: decisions held for approval that the individual could take, rework rising on the same tasks, longer hours for the same output, and silence in meetings where challenge is needed. These signals appear before the KPI falls. Leaders who ask a team what is slowing its work hear them within weeks; a review that reads only the KPI sees them a quarter later.',
  ['Leaders read the signals in the organisational conditions that support the execution of the individuals&rsquo; tasks.',
   '<strong>Governance · review forums.</strong> The same unresolved item appears on three consecutive agendas, and each team waiting on it reports its delay separately.',
   '<strong>Systems · data integrity.</strong> Two reports give different figures for the same measure, and teams spend their time reconciling them.',
   '<strong>Resources · workforce capacity.</strong> One specialist&rsquo;s queue grows each week while the projects that depend on that person report small slips.',
   'None of these carries a number in the review, so leaders ask for them by name.'],
  ''),
 ('Discipline 2', 'Accurate Classification', 'Name the Clog Precisely Before Intervening',
  ['Each clog belongs to a specific category of organisational friction. Structural misfit, capability gaps, decision bottlenecks, misaligned incentives, cultural resistance, technological constraints, or leadership avoidance each require fundamentally different forms of intervention.',
   'The most common diagnostic failure is applying the wrong lever to a correctly identified symptom. A leader who observes &ldquo;slow execution&rdquo; and responds by adding resources is applying a capability lever to what may be a decision bottleneck. The additional resources do not accelerate execution because the constraint is approval latency.',
   'Accurate classification requires resisting the impulse to solve before diagnosing. The first question is &ldquo;What type of friction is this, and what does it tell us about the system?&rdquo;'],
  ['Classification uses the evidence of the Three Performance Lines of Sight. The outcome confirms that a clog exists. The behaviour shows how it acts on individuals and teams. The condition names the clog. Leaders test the evidence against each of the seven clogs in turn and keep the one that explains why the pattern persists.',
   'Several clogs often act together. Leaders name the primary clog, the one whose removal releases the others, and record the contributing clogs beside it.'],
  'Leaders separate what is within the individual&rsquo;s control from what the conditions impose. An individual who delays decisions may lack confidence. The same delay appears when the individual lacks the authority to decide. Classification establishes which applies, with evidence from the individual&rsquo;s work, before a capability or accountability response is chosen.',
  ['Leaders locate the condition behind the behaviour.',
   '<strong>Governance · decision authority.</strong> Approvals for routine work sit two levels above the people doing it. The slow delivery is a Decision Bottleneck.',
   '<strong>Systems · process clarity.</strong> The hand-offs between three functions have no single owner. The same slow delivery is Structural Misfit.',
   'One symptom leads to two different clogs, and to two different levers. Classification decides which one the team pulls.'],
  ''),
 ('Discipline 3', 'Targeted Intervention', 'Pull the Right Lever with Precision',
  ['Once the clog is identified and classified, it must be addressed through the appropriate strategic lever. Clogs rarely clear themselves through trying harder or working more hours. They require a deliberate adjustment to the organisation&rsquo;s structural, behavioural, and operational settings.',
   'Targeted intervention means matching the lever to the root cause. It also means accepting that rarely does a single clog require just one fix. A Capability Gap may require both Upgrade (systems) and Reinforce (skills). A Leadership Avoidance clog may require both Clarify (decision rights) and Rebuild Trust (credibility restoration).'],
  ['A targeted intervention names what will change, who will change it and the evidence that will show the clog clearing. Leaders set that evidence before they act: the signal they expect to fall, the behaviour they expect to change and the result they expect to move.',
   'Leaders also sequence the response. Where two levers are needed, the lever that changes the condition usually comes first, and the lever that builds the people&rsquo;s capability or confidence follows, so that individuals apply new skills in conditions that support them.'],
  'The intervention equips individuals to deliver their tasks under the changed conditions: clear authority, the skills the strategy now requires, coaching through the first cycles and consistent consequences. Leaders confirm the change in the individuals&rsquo; work: decisions taken at the right level, less rework and problems raised early.',
  ['The intervention changes the organisational condition behind the clog.',
   '<strong>Governance · decision authority.</strong> Delegation limits for routine decisions are reset and published.',
   '<strong>Systems · data integrity.</strong> One source of customer data replaces three, and every report draws on it.',
   '<strong>Resources · capability alignment.</strong> Specialist capacity is added where the strategy concentrates demand.',
   'Leaders confirm the change in the condition itself, then in the Key Result.'],
  'The goal is to develop a leadership rhythm that moves quickly and precisely: <strong>Identify the Clog &rarr; Select the Lever &rarr; Targeted Intervention.</strong>'),
]

# Levers: (num, name, role, Carol's summary, Carol's why, how (new), people (new), organisation (new))
LEVERS = [
 ('01', 'Standardise', 'Ensure Consistency', 'Harmonises processes and service levels across teams so everyone plays by the same rules.',
  'Variability is a silent killer of speed. By establishing a shared &ldquo;way we work,&rdquo; you reduce duplication and ensure every unit pulls in the same direction. Apply when: Variability across teams is creating drag. Best applied to: Structural Misfit, Misaligned Metrics &amp; Incentives, Technology / Infrastructure Lag.',
  'Standardise sets one agreed way of working where the strategy needs consistent results across teams, sites or channels. Leaders define the standard, the measure that shows it is met and the leader responsible for keeping it current. The standard covers the work that must be consistent and leaves local judgement where the strategy needs it.',
  'Individuals work to one set of expectations, so effort is no longer lost translating between teams. Leaders train every team on the standard and hold each individual to the same measure of quality and timeliness.',
  ['<strong>Systems · process clarity.</strong> Three regions run three versions of customer onboarding. One process replaces them, with one set of service levels.',
   '<strong>Governance · clear accountability.</strong> A named leader maintains the standard and reviews compliance each quarter.']),
 ('02', 'Streamline', 'Increase Speed', 'Simplifies workflows and removes the red tape layers that add no value to execution.',
  'Leaner processes mean faster approvals and a team that can pivot as quickly as the market demands. Apply when: Approval processes are creating latency. Best applied to: Decision Bottlenecks, Structural Misfit.',
  'Streamline removes the steps, approvals and hand-offs that add time without adding control or value. Leaders map the path a piece of work takes, mark each point where it waits, and remove or combine the steps that change nothing in the outcome. Controls that protect the organisation stay, placed at the point of greatest risk.',
  'Individuals spend their time on the task itself. Managers decide within clear limits, teams stop chasing approvals, and work moves at the pace the strategy requires.',
  ['<strong>Governance · decision authority.</strong> Routine purchases below an agreed limit no longer need senior approval.',
   '<strong>Systems · approvals.</strong> One electronic approval route replaces email chains, and every request shows where it sits.']),
 ('03', 'Clarify', 'Eliminate Confusion', 'Defines exactly who owns what, where the handoffs are, and who has the final say.',
  'Ambiguity breeds hesitation. When people know their roles and decision rights, accountability returns and work stops getting stuck in limbo. Apply when: Ownership ambiguity is causing hesitation. Best applied to: Decision Bottlenecks, Structural Misfit, Leadership Avoidance.',
  'Clarify settles who owns each outcome, who decides, who must be consulted and where work passes from one team to the next. Leaders write the decision rights and hand-offs down, agree them across the functions involved and communicate them to everyone who works across the boundary.',
  'Individuals know which decisions are theirs and act on them. Escalation falls, ownership returns to the level closest to the work, and accountability can be applied fairly because responsibility now carries matching authority.',
  ['<strong>Governance · clear accountability.</strong> One executive owns the end-to-end customer-resolution outcome across service, operations and finance.',
   '<strong>Governance · review forums.</strong> Each open trade-off has a named decision-maker and a date by which the decision is made.']),
 ('04', 'Upgrade', 'Remove Bottlenecks', 'Fixes underperforming technology and infrastructure that holds execution back.',
  'You cannot run a modern strategy on yesterday&rsquo;s tools. Upgrading removes the physical and digital friction that makes scaling feel impossible. Apply when: Systems are creating friction that blocks flow. Best applied to: Technology / Infrastructure Lag, Capability Gaps.',
  'Upgrade replaces or improves the technology, infrastructure or capability that cannot carry the strategy&rsquo;s demands. Leaders define the performance the strategy requires in speed, reliability, visibility and scale, measure the gap and invest where the gap constrains the Key Result most.',
  'Individuals stop spending their time on workarounds: re-keying data, reconciling records and building reports by hand. That time returns to the work the strategy needs, and confidence in improvement initiatives recovers.',
  ['<strong>Systems · data integrity.</strong> The customer and transport systems are connected, so delivery status updates without manual entry.',
   '<strong>Environment · infrastructure.</strong> Field teams receive reliable connectivity, so orders reach operations the same day.']),
 ('05', 'Reinforce', 'Strengthen Behaviour', 'Equips the team with the skills, coaching, and confidence they need to actually deliver.',
  'Strategy requires new behaviours. Reinforcement ensures your people are capable of making the change. Apply when: Skills or confidence are the limiting factor. Best applied to: Capability Gaps, Cultural Resistance.',
  'Reinforce builds the skills, habits and confidence the strategy requires of individuals and teams. Leaders identify the behaviours the strategy depends on, provide training and coaching, model the behaviours themselves and recognise them when they appear.',
  'Individuals gain the capability to meet the new expectations and the confidence to apply it. Coaching through the first cycles turns new skills into habits, and recognition shows people that the new behaviours count.',
  ['<strong>Resources · capability alignment.</strong> A development programme in digital credit assessment is funded for the whole lending team.',
   '<strong>Environment · values and consequences.</strong> Leaders&rsquo; own decisions and recognition reflect the behaviours the strategy asks for.']),
 ('06', 'Realign', 'Focus on Results', 'Adjusts metrics and rewards so they actually match current strategic priorities.',
  'People do what they are measured on. When you fix the incentives, the team&rsquo;s energy naturally shifts from protecting their patch to creating enterprise value. Apply when: Effort is flowing only to what is measured. Best applied to: Misaligned Metrics &amp; Incentives.',
  'Realign changes measures, targets and rewards so that they reinforce the contributions the strategy needs. Leaders trace each scorecard measure to the Key Result it serves, remove or reweight the measures that reward local results at the expense of the enterprise outcome, and add measures for shared results.',
  'Individuals no longer have to choose between their rating and the strategy. Collaboration, quality and contribution to shared outcomes are recognised, so committed people can do what the strategy requires without personal cost.',
  ['<strong>Governance · consistent consequences.</strong> Sales bonuses are paid on margin and customer retention alongside volume.',
   '<strong>Systems · performance data.</strong> Shared enterprise measures appear on every functional scorecard that contributes to them.']),
 ('07', 'Rebuild Trust', 'Restore Credibility', 'Heals relationships and introduces the transparency needed for people to commit again.',
  'Trust is the social grease of execution. Without it, the system seizes up. Rebuilding it restores the psychological safety required for high-stakes work. Apply when: Psychological safety or leadership credibility is the constraint. Best applied to: Cultural Resistance, Leadership Avoidance.',
  'Rebuild Trust restores the credibility of leadership and the safety people need to speak, challenge and commit. Leaders acknowledge what has gone wrong, act on the concerns people raise, follow through on their decisions and make the reasons for those decisions visible.',
  'Individuals raise problems early again, offer ideas and commit to decisions they helped shape. Strong performers regain confidence in the direction.',
  ['<strong>Environment · psychological safety.</strong> Leaders open each review by asking what is blocking delivery, and act on what they hear.',
   '<strong>Governance · consistent consequences.</strong> Commitments missed at senior level are addressed to the same standard applied elsewhere.']),
]

# ───────── Section 4 · The Unclogging Cycle ─────────
S4_41_OLD = 'Here the executive team applies it together to a clog that crosses executive portfolios.'
S4_41_NEW = 'Here the executive team applies it together, as the Unclogging Cycle, to a clog that crosses executive portfolios.'
S4_GUIDE_OLD = 'Use Review&ndash;Realign&ndash;Restore as the established S2R&reg; discipline'
S4_GUIDE_NEW = 'Use the Unclogging Cycle, Review&ndash;Realign&ndash;Restore, as the established S2R&reg; discipline'
S4_TITLE = '4.2 &mdash; The Unclogging Cycle: Review&ndash;Realign&ndash;Restore'
S4_META = 'The S2R&reg; discipline · Three stages, one record'
S4_INTRO = ('<p>The Unclogging Cycle is the S2R&reg; discipline the executive team follows to remove a clog. REVIEW establishes the performance reality and confirms the clog. '
 'REALIGN settles which leaders act and what must change. RESTORE activates the Unclogging Lever and verifies recovery. Each stage completes one part of the Unclogging Record, '
 'so the record the team holds at the end is the evidence of the whole cycle.</p>\n')
S4_SUBS = ['REVIEW &mdash; Establish the Performance Reality', 'REALIGN &mdash; Establish Collective Executive Ownership', 'RESTORE &mdash; Activate the Seven Unclogging Levers']
S4_REVIEW_CARDS = cards(
 'REVIEW examines what individuals and teams are doing, delaying or unable to do, and separates what is within their control from what the conditions impose. Leaders draw the evidence from the work itself: decisions waiting, hand-offs repeated, rework recorded.',
 'REVIEW tests whether the organisational conditions support the execution of the individuals&rsquo; tasks, and locates the condition sustaining the behaviour. Leaders examine the evidence across executive portfolios, because the condition often sits outside the function where the clog shows.')
S4_REALIGN_PEOPLE_ADD = '<p>The answer becomes the commitments made to the people delivering the result: the authority they receive, the support they are given and what is expected of them.</p>'
S4_REALIGN_ORG_ADD = '<p>The answer becomes the organisational change the executives agree, with the leader responsible for each part.</p>'
S4_RESTORE_CARDS = cards(
 'RESTORE equips individuals to deliver under the changed conditions and verifies the change in their work: decisions taken at the right level, delays falling, rework reducing and problems raised early.',
 'RESTORE applies the lever to the organisational condition and verifies that the condition has changed: the approval route, the data source, the decision right or the measure now supports the execution of the individuals&rsquo; tasks, and the Key Result begins to move.')
S4_REC_LINES = [
 '<div class="u9-done"><strong>Into the Unclogging Record:</strong> the performance gap, the evidence from the three lines of sight and the confirmed clog.</div>',
 '<div class="u9-done"><strong>Into the Unclogging Record:</strong> the coordinating executive, the contributing executives and the agreed changes for people and organisational performance.</div>',
 '<div class="u9-done"><strong>Into the Unclogging Record:</strong> the selected lever, the actions with their owners and completion dates, the evidence of recovery and the date of the next review.</div>']
S4_RECORD = ('<details class="u9-det"><summary class="u9-sub">The Unclogging Record</summary><div class="u9-det-b">\n'
 '<p>The Unclogging Record holds the outcome of each stage in one place. The executive team completes it as it moves through the cycle, then uses it at each later review '
 'to check that the agreed actions are complete and the evidence is moving.</p>\n'
 '<div class="u9-tw"><table class="u9-tbl"><thead><tr><th>Stage</th><th>What the record holds</th></tr></thead><tbody>'
 '<tr><td>REVIEW</td><td>The performance gap, the evidence from the three lines of sight and the confirmed clog.</td></tr>'
 '<tr><td>REALIGN</td><td>The coordinating executive, the contributing executives and the agreed changes for people and organisational performance.</td></tr>'
 '<tr><td>RESTORE</td><td>The selected lever, the actions with their owners and completion dates, the evidence of recovery and the date of the next review.</td></tr>'
 '</tbody></table></div>\n'
 '<p>The worked example in 4.3 ends with a completed Unclogging Record.</p>\n'
 '</div></details>\n')
S4_WE_OLD = '4.5 &mdash; Worked Example: Review&ndash;Realign&ndash;Restore'
S4_WE_NEW = '4.3 &mdash; Worked Example: The Unclogging Cycle'

# ───────── Section 5 ─────────
S5 = {
 'p': {
  'how1_old': 'Your group selects one challenge from the list it documented before CESI began and links it to a strategic result (5.1).',
  'how1_new': 'Your group selects one challenge from its Problem Charter and links it to one of its Objectives and Key Results (5.1).',
  'how3_old': 'Your group applies Review&ndash;Realign&ndash;Restore (5.4), then tests its response against the Diagnostic Quality Check (5.5).',
  'how3_new': 'Your group simulates the Unclogging Cycle, Review&ndash;Realign&ndash;Restore (5.4), then tests its response against the Diagnostic Quality Check (5.5).',
  'intro_old': 'Review the organisational challenges your group documented before CESI began. Select one challenge that remains relevant to your Capstone organisation and has a clear connection to disappointing organisational results.',
  'intro_new': 'Your group&rsquo;s Problem Charter holds the challenges your executive team committed to address. Select one that remains relevant to your Capstone organisation and has a clear connection to disappointing organisational results.',
  's54': '<p>Your group simulates how its executive team takes the selected challenge through the Unclogging Cycle. Work through REVIEW, REALIGN and RESTORE in turn; together they complete your group&rsquo;s Strategic Unclogging Clinic Record in 5.6.</p>\n',
 },
 'f': {
  'how1_old': 'Each group selects one challenge from the list it documented before CESI began and links it to a strategic result (5.1).',
  'how1_new': 'Each group selects one challenge from its Problem Charter and links it to one of its Objectives and Key Results (5.1).',
  'how3_old': 'The group applies Review&ndash;Realign&ndash;Restore (5.4), then tests its response against the Diagnostic Quality Check (5.5).',
  'how3_new': 'The group simulates the Unclogging Cycle, Review&ndash;Realign&ndash;Restore (5.4), then tests its response against the Diagnostic Quality Check (5.5).',
  'intro_old': 'Each group reviews the organisational challenges it documented before CESI began and selects one challenge that remains relevant to its Capstone organisation and has a clear connection to disappointing organisational results.',
  'intro_new': 'Each group selects one challenge from its Problem Charter that remains relevant to its Capstone organisation and has a clear connection to disappointing organisational results.',
  's54': '<p>The group simulates how its executive team takes the selected challenge through the Unclogging Cycle, working through REVIEW, REALIGN and RESTORE in turn. Together they complete the group&rsquo;s Strategic Unclogging Clinic Record in 5.6.</p>\n',
 },
}
S5_OUT_OLD = 'The original work-based challenge selected from its pre-CESI preparation.'
S5_OUT_NEW = 'The original work-based challenge selected from its Problem Charter.'
S5_GUIDE_OLD = 'At the beginning of CESI, each group identified recurring work-based organisational challenges drawn from its members&rsquo; professional experiences. These challenges informed the simulated Capstone organisation. Participants must now return to that original list, select one challenge'
S5_GUIDE_NEW = 'In its Problem Charter, each group recorded recurring work-based organisational challenges drawn from its members&rsquo; professional experiences and chose the challenges its executive team would address. These challenges informed the simulated Capstone organisation. Participants now return to that list, select one challenge'
S5_CLOSE_OLD = 'since you first identified it before CESI?'
S5_CLOSE_NEW = 'since you first identified it in your Problem Charter?'
S5_54_OLD = '5.4 &mdash; Apply Review&ndash;Realign&ndash;Restore'
S5_54_NEW = '5.4 &mdash; Simulate the Unclogging Cycle'
S5_P51_FIELDS = ('<div class="u9-s5"><label class="wp-label" for="u9_ch_challenge">Selected original challenge</label><div class="u9-q">Select the challenge from your group&rsquo;s Problem Charter.</div>'
 '<select class="u9-sel" id="u9_ch_challenge" data-u9="ch_challenge"><option value="">&ndash; select a challenge &ndash;</option></select><p class="u9-wait" id="u9ChNote" style="display:none;"></p></div>\n'
 '<div class="u9-s5"><label class="wp-label" for="u9_ch_link">Strategic connection</label><div class="u9-q">Which strategic Objective and Key Result does this challenge affect?</div>'
 '<select class="u9-sel" id="u9_ch_link" data-u9="ch_link"><option value="">&ndash; select an Objective and Key Result &ndash;</option></select><p class="u9-wait" id="u9KrNote" style="display:none;"></p></div>\n')
S5_F51_BRIEFS = ('<div class="u9-brief"><b>Selected original challenge</b><span>The group selects the challenge from its Problem Charter.</span></div>\n'
 '<div class="u9-brief"><b>Strategic connection</b><span>The group selects the strategic Objective and Key Result the challenge affects.</span></div>\n')

# ───────── Unit Summary ─────────
SUM_P = {
 'Awareness': 'You saw that a Strategic Clog is an internal blockage that prevents strategic intent from flowing into execution, and that clogs form where the strategy stretches today&rsquo;s organisation. Performance has two connected dimensions, organisational performance and people performance. The 7-Clog Diagnostic Map, aligned to ABCV Directional Integrity, examines both, and the Three Performance Lines of Sight trace a result from its outcome to the behaviours and the conditions behind it.',
 'Intelligence': 'You saw that leaders resolve clogs through three disciplines: early identification, accurate classification and targeted intervention. The 7 Strategic Unclogging Levers act on people performance and organisational performance together, restoring the conditions that allow strategy to flow at the intended speed.',
 'Integration': 'You saw that clogs rarely stay in one lane. The leadership team removes them together through the Unclogging Cycle: REVIEW confirms the clog, REALIGN agrees collective ownership and the changes for people and organisational performance, and RESTORE activates the Unclogging Lever and verifies recovery. Each stage completes part of the Unclogging Record.',
 'Application': 'Your group selected a challenge from its Problem Charter, identified the clog, selected the lever and simulated the Unclogging Cycle within your Capstone organisation.',
}
SUM_F = {
 'Awareness': 'A Strategic Clog is an internal blockage that prevents strategic intent from flowing into execution. Clogs form where the strategy stretches today&rsquo;s organisation. Performance has two connected dimensions, organisational performance and people performance. The 7-Clog Diagnostic Map, aligned to ABCV Directional Integrity, examines both, and the Three Performance Lines of Sight trace a result from its outcome to the behaviours and the conditions behind it.',
 'Intelligence': 'Leaders resolve clogs through three disciplines: early identification, accurate classification and targeted intervention. The 7 Strategic Unclogging Levers act on people performance and organisational performance together.',
 'Integration': 'Clogs rarely stay in one lane. The leadership team removes them together through the Unclogging Cycle: REVIEW confirms the clog, REALIGN agrees collective ownership and the changes for people and organisational performance, and RESTORE activates the Unclogging Lever and verifies recovery. Each stage completes part of the Unclogging Record.',
 'Application': 'Each group selected a challenge from its Problem Charter, identified the clog, selected the lever and simulated the Unclogging Cycle within its Capstone organisation. The agreed record feeds the team&rsquo;s Capstone Blueprint.',
}
