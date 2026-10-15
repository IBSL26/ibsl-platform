# -*- coding: utf-8 -*-
"""Unit 8 · the two performance views (15 October 2026).
Content locked by Carol section by section (Review files/Unit 8/Unit 8 two views - locked amendments.md).
Helpers turn plain text into the page's HTML. ' becomes &rsquo;."""

def h(t):
    return t.replace("'", "&rsquo;")

def P(t):
    return '<p>' + h(t) + '</p>'

def LI(items):
    """items: list of (label, text) or text. Label is bolded."""
    out = []
    for it in items:
        if isinstance(it, tuple):
            out.append('<li><strong>' + h(it[0]) + '.</strong> ' + h(it[1]) + '</li>')
        else:
            out.append('<li>' + h(it) + '</li>')
    return '<ul class="u8v-l">' + ''.join(out) + '</ul>'

def side(kind, label, inner):
    return ('<div class="u8v-c u8v-' + kind + '"><div class="u8v-n">' + h(label) + '</div>' + inner + '</div>')

def pair(hin, oin, stack=False, hl='From the human side', ol='From the organisation side'):
    cls = 'u8v-hc u8v-st' if stack else 'u8v-hc'
    return ('<div class="' + cls + '" onclick="event.stopPropagation()">' + side('hu', hl, hin) + side('or', ol, oin) + '</div>')

CSS = """
/* ── Unit 8 · the two performance views (15 October 2026): human side and organisation side cards ── */
.u8v-hc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin:12px 0 14px;cursor:default;}
.u8v-hc.u8v-st{grid-template-columns:1fr;}
.u8v-c{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-top:3px solid #8ab0e8;border-radius:3px;padding:12px 16px;}
.u8v-c.u8v-or{border-top-color:#5ecba1;}
.u8v-n{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8ab0e8;margin:0 0 6px;}
.u8v-or .u8v-n{color:#5ecba1;}
.u8v-c p{font-size:12.5px!important;line-height:1.7!important;color:rgba(255,255,255,.75)!important;margin:0 0 6px!important;}
.u8v-l{padding-left:18px!important;margin:4px 0 8px!important;}
.u8v-l li{font-size:12.5px;line-height:1.7;color:rgba(255,255,255,.75);margin:0 0 5px;}
.u8v-l li strong{color:#fff;}
"""

# ───────── Header
HEAD_ADD = ' Each review examines two things: the progress of what individuals and teams deliver, and whether the organisational conditions support the execution of their tasks.'

# ───────── Section 1
S1_VIS = pair(
    P("Leaders see whether individuals and teams are moving their KPIs, OKRs and behaviours toward the enterprise result."),
    P("Leaders see whether the organisational conditions support the execution of the individuals' tasks. These conditions are the Environment, Systems, Resources and Governance (ESRG) agreed in Unit 6."))
S1_ACT = pair(
    P("The question moves from “How busy are our people?” to “What has their work changed in the Key Result?”"),
    P("The question moves from “Has the support been put in place?” to “Does the support enable the individuals' tasks to move the Key Result?”"))
S1_REF_ADD = ' What evidence do you hold on whether the organisational conditions support the tasks behind that progress?'

S1_PUR = [
    pair(P("Where individuals' and teams' KPIs are gaining momentum and where they are stalling."),
         P("Where the organisational conditions are supporting the execution of the tasks, and where they are holding it back.")),
    pair(P("Individuals and teams know which part of the strategy they are responsible for advancing, and their delivery is recorded as evidence."),
         P("Leaders account for whether the organisational conditions they undertook to provide in Unit 7 support the execution of the individuals' tasks.")),
    pair(P("The review learns what accelerates and what slows the progress of individuals and teams."),
         P("The review learns which organisational conditions enable execution and which constrain it.")),
    pair(P("An early signal in an individual's progress lets the leader intervene while the KPI is still recoverable."),
         P("An early signal in an organisational condition, such as a system outage, a capacity shortfall or a delayed decision, lets the leader responsible act before the individuals' delivery is affected.")),
]
S1_R3_INTRO = P("The cycle applies to both operating systems.")
S1_REVIEW = pair(
    P("The individual and the leader establish the progress made against the agreed target."),
    P("The leader brings the agreed measures or evidence of readiness for the organisational conditions, and the review establishes whether those conditions support the execution of the individuals' tasks."))
S1_REALIGN = pair(
    P("The Accountability Loop (part 1.4) diagnoses what is preventing the individual's expected performance."),
    P("The leader determines what is preventing an organisational condition from supporting the execution of the individuals' tasks, and agrees the response."))
S1_RESTORE = pair(
    P("The individual commits to the corrective actions and the follow-up dates."),
    P("The leader responsible commits to the actions on the organisational conditions, each with a review date."))
S1_CONT = P("The next Review examines both: the individuals' progress, and whether the organisational conditions now support their tasks.")

S1_FG = ('<p><strong>1.1 &middot; The Execution Visibility Infrastructure.</strong> ' + h("Open with the question “Is the work being done actually advancing the strategy?” Teach the move from activity to progress, from the human side and the organisation side.") + '</p>\n'
         '<p><strong>1.2 &middot; The Four Strategic Purposes.</strong> ' + h("Teach execution rhythm, then the four purposes one card at a time, each from both sides.") + '</p>\n'
         '<p><strong>1.3 &middot; From Performance Measurement to Execution Recovery.</strong> ' + h("Link the four purposes to the Review–Realign–Restore Cycle (R3) and teach each stage for both operating systems.") + '</p>\n'
         '<p><strong>1.4 &middot; The Accountability Loop.</strong> ' + h("Teach the three root causes, how GROW achieves each recovery, and why the performance conversation stays separate from the role conversation.") + '</p>\n'
         '<p>' + h("The full teaching notes are in the slide notes.") + '</p>\n')

# ───────── Section 2
S2_FG = ('<p>' + h("Teach review discipline as a leadership discipline: the rhythm of review conversations is itself a strategic capability.") + '</p>\n'
         '<p><strong>2.1 &middot; Four Consequences of Weak Review Discipline.</strong> ' + h("Teach execution velocity: the rate at which strategic intent becomes measurable results. Then teach the four consequences as one chain, one card at a time, each from the human side and the organisation side.") + '</p>\n'
         '<p>' + h("Section 5 returns to these four consequences. The full teaching notes are in the slide notes.") + '</p>\n')

S2_CONS = [
    pair(
        P("Early warnings on the human side show in the review conversation before they show in the KPI. Three patterns recur:")
        + LI([("The quality of evidence falls", "Results give way to explanations, and percentages arrive without the evidence behind them."),
              ("Alignment drifts", "The individual who rated alignment at 9 when the target was agreed now gives short, guarded answers about the target, and no one asks the alignment question again."),
              ("Effort migrates", "The individual's time moves to work that senior leaders ask about, and the KPI receives what is left.")])
        + P("Each pattern leads a missed KPI by weeks. A leader who reviews monthly sees it as a trend across two or three conversations; a leader who reviews at quarter end sees the result alone. The difference is the recovery available: a capability gap seen in week four can be met with coaching; the same gap seen in week twelve leaves a revised target."),
        P("An early warning on the organisation side is evidence that an organisational condition has started to weaken in its support for the individuals' tasks. It seldom carries a number of its own, so the review sees it only when it asks for it.")
        + LI([("Resources · workforce capacity", "A contact centre carries a customer-retention Key Result. Two agents resign and their posts stay open for a quarter. The remaining team covers the volume through overtime, and resolution times hold for six weeks, then fall sharply as absenteeism rises. The vacancy and the overtime were on record weeks before the KPI moved."),
              ("Environment · psychological safety", "In a function where raising a problem in front of senior leaders has carried a cost, team leads report amber milestones as green. The review sees on-track ratings until a milestone is missed. The warning was there all along: months without a single amber rating."),
              ("Systems · data integrity", "Sales, operations and finance each report from their own platform, and every cross-functional figure is consolidated by hand. The executive review works on information a week old, and a slipping delivery reaches the review after customers have already escalated it.")])
        + P("Measures or evidence of readiness for each condition give these signals a place in the review. When the review does not ask for them, the condition shows itself through the KPI it was meant to support."),
        stack=True),
    pair(
        P("Individuals read priority from the review agenda. When a KPI is absent from three reviews in a row, the conclusion is reasonable: leadership attention has moved. Accountability then weakens in three ways:")
        + LI([("The KPI is managed for appearance", "Updates are written to reassure, and risks are held until they can no longer be hidden."),
              ("Ownership of a shared KPI spreads thin", "Each individual assumes another is carrying the result, and the dependencies between them belong to no one."),
              ("The commitment loses its force", "The commitment given when the target was agreed has not been tested since.")])
        + P("When the gap finally surfaces, the review becomes a search for who was responsible. The Accountability Loop cannot diagnose a commitment no one has been asked about."),
        P("Leaders make commitments on organisational conditions when targets are agreed. These commitments seldom appear on any scorecard, so they diffuse first.")
        + LI([("Resources · capability alignment", "A new procurement system is introduced with the promise that every buyer will be trained. Three months later half the buyers are untrained and purchase orders take twice as long. The buyers' cycle-time KPI is reviewed every month; the training commitment has never been raised."),
              ("Governance · clear accountability", "A regional manager is accountable for a margin Key Result, yet every discount above a set level still needs head-office sign-off. The change to the delegation was approved in principle and never issued. The manager carries the accountability without the authority to deliver it.")])
        + P("Individuals remain held to their targets while the support they were promised quietly lapses. Mutual accountability becomes one-sided, and individuals protect themselves: they commit to less, document more and move from commitment to compliance."),
        stack=True),
    pair(
        P("Every review produces evidence on how results are achieved, and that evidence is the raw material of the organisation's performance capability.")
        + LI([("Practices that accelerate progress", "One regional team meets its targets because its manager runs a short daily huddle on the Key Result. Recorded and examined, the practice can be taught to other teams. Unexamined, it stays one manager's habit and leaves when that manager leaves."),
              ("Capability gaps that recur", "When the same skill gap appears in reviews across several functions, it signals a development need at enterprise level."),
              ("Behaviours that strengthen ownership", "Reviews show which leaders' teams surface problems early and which conceal them.")])
        + P("When reviews only record results, talent decisions, development plans and succession rest on ratings with no evidence of how the results were achieved. The organisation keeps rewarding outcomes it cannot reproduce."),
        P("Reviews also show how the organisational conditions behave as the strategy places weight on them. The learning is cumulative: the same constraint appearing in several reviews is evidence that a condition is not yet equal to the strategy.")
        + LI([("Systems · process clarity", "Three functions each report delays at the handover between sales order and dispatch. Reviewed function by function, each delay looks local. Reviewed together, they show one handover that no one is responsible for."),
              ("Resources · financial support", "For two years running, the budget for strategic initiatives is released in the second quarter, and each year the initiatives deliver in the second half alone. The pattern becomes visible only when reviews are compared across cycles."),
              ("Governance · decision authority", "Capital requests above a set value wait a month on average for an executive decision, and every Key Result that depends on one slips by about the same margin.")])
        + P("When reviews do not capture this learning, the organisation sets its next strategy on the same conditions. Targets rise, the conditions stay where they were, and the same constraints slow execution again. This learning is the evidence the executive team needs to judge whether the organisation can carry its next level of ambition."),
        stack=True),
    pair(
        P("Credibility is built in the review. A leader who asks for evidence every month, recognises progress and addresses shortfalls consistently shows that the priority is real. Two patterns erode it:")
        + LI([("Priorities that fade", "A strategic KPI launched with energy disappears from the review agenda, and individuals conclude the announcement was symbolic. High performers, who invest most in strategic commitments, become the most sceptical, and the organisation learns to wait and see whether a priority survives its first quarter."),
              ("Standards applied unevenly", "Some individuals' KPIs are examined closely while others are excused, often by seniority. Individuals read this as unfairness, and commitment falls across the whole team.")]),
        P("Leaders make commitments when they agree organisational conditions, and individuals track these closely because their own delivery depends on them. Credibility on this side is a test of fairness.")
        + LI([("Environment · values and consequences", "The organisation states accountability as a value. A junior manager is challenged in the review for a missed milestone, while a senior executive's missed commitment to release staff for the same project is never raised."),
              ("Environment · psychological safety", "Leaders invite open reporting of risks, and the first person to raise a delivery risk in a review is questioned in front of peers. From then on, risks reach the review late."),
              ("Governance · execution oversight", "The executive team commits to a monthly decision forum to clear constraints, then postpones it twice in one quarter while the decisions wait.")])
        + P("When leaders review individuals' targets and leave their own commitments unreviewed, individuals see accountability running one way. Reviewing both, to the same evidence standard, shows that leaders hold themselves to the standard they set for others."),
        stack=True),
]
S2_REF_ADD = ' Did an organisational condition play a part in the delay?'

# ───────── Section 3
S3_FG = ('<p>' + h("Open with the observation that most organisations have agreed goals, KPIs and dashboards; the breakdown occurs in how leaders review and interpret the measurement together.") + '</p>\n'
         '<p><strong>3.1 &middot; Four Fractures in Performance Measurement.</strong> ' + h("Teach the four fractures one card at a time, each with its implication for human performance and for organisational performance.") + '</p>\n'
         '<p><strong>3.2 &middot; The CXO Performance Gap Contributors.</strong> ' + h("Teach the logic of the role cards, then take each participant's own role and the two roles closest to it. Participants complete the reflection on the fracture they are most prone to as Portfolio work.") + '</p>\n'
         '<p>' + h("The full teaching notes are in the slide notes.") + '</p>\n')

HL3 = 'Implication for human performance'
OL3 = 'Implication for organisational performance'
S3_GAPS = [
    pair(
        P("When each function reviews its own KPIs, individuals are judged on the part of the result they control, and the hand-offs between functions are never examined. An operations planner meets every internal measure while customer orders wait at the boundary with sales. Individuals learn to optimise their own measure, and the commitments they made to other functions go unreviewed: no one is asked whether they delivered what another function needed from them. Individuals whose work depends on another function are held to results they cannot complete alone, and the review sees their shortfall without the dependency behind it."),
        P("The organisational conditions that span functions fall between the reviews.")
        + LI([("Systems · process clarity", "The order-to-cash process runs through sales, credit control, the warehouse and finance. Each function reviews its own step and reports it on time. No review sees the end-to-end cycle, which is where the customer experiences the delay."),
              ("Governance · decision authority", "A non-standard customer contract needs approval from legal, finance and operations. Each reports its own turnaround as acceptable; end to end, the decision takes three weeks, and the sales Key Result absorbs the wait.")])
        + P("The executive team sees each function's conditions as adequate while the conditions at the boundaries hold back the enterprise result."),
        stack=True, hl=HL3, ol=OL3),
    pair(
        P("Weak evidence harms individuals in two ways. Strong performers cannot show what their contribution changed, and weak delivery stays hidden behind narrative. When the evidence offered is activity, such as training attended or meetings held, the review rates effort. Ratings lose credibility with the individuals themselves, and the performance standard agreed at the start of the period loses its anchor. Over time, individuals learn that the persuasive account is rewarded."),
        P("Most reviews hold no evidence at all on organisational conditions. Their state is asserted: the system is stable, the roles are filled, the budget is available.")
        + LI([("Resources · workforce capacity", "HR reports headcount at budget. The review does not see that a third of the roles in the unit carrying the Key Result are held by new staff still in training. The evidence that matters is productive capacity: how many of those roles can carry the work today."),
              ("Systems · workflow visibility", "IT reports system availability at 99 per cent. The finance team reports that the month-end report takes three days to run. The first figure describes the system; the second describes whether it supports the tasks.")])
        + P("With no evidence standard for the conditions, the review cannot tell whether they support the individuals' tasks, and the discussion settles on the individuals' numbers, the only evidence in the room."),
        stack=True, hl=HL3, ol=OL3),
    pair(
        P("The rhythm of review sets the individuals' planning horizon. Reviewed quarterly, individuals work in quarterly bursts: a slow start, a surge before the period closes and figures prepared for the review. Reviewed irregularly, evidence is assembled in a hurry and the conversation is spent reconstructing what happened. The recoveries of the Accountability Loop need a rhythm short enough for coaching, development or a structural change to take effect within the period."),
        P("Organisational conditions often have no rhythm of review at all; they reach the agenda when something fails.")
        + LI([("Governance · execution oversight", "Capital and risk decisions follow the board calendar, so a decision on a condition a Key Result depends on can wait up to three months."),
              ("Resources · financial support", "Budgets are reallocated only at the mid-year forecast. An initiative found short of funds in its second month waits until its sixth."),
              ("Environment · employee sustainability", "Workload is seen through the annual engagement survey, so overload in a critical team shows first in resignations.")])
        + P("When the conditions are reviewed on a slower rhythm than the KPIs they support, the conditions lag the work they are meant to enable."),
        stack=True, hl=HL3, ol=OL3),
    pair(
        P("When reviews judge, individuals defend. They bring the explanation and hold back the obstacle, and in the next cycle they propose targets they are sure to meet. Learning moves out of the review into corridors and private conversations. The organisation loses the individuals' first-hand knowledge of what is slowing execution, the most current intelligence it has."),
        P("Suppression falls hardest on the conditions, because naming a condition often means naming a senior leader's area.")
        + LI([("Environment · psychological safety", "A team lead knows the approval process is the real constraint on the Key Result and does not say so, because the approval sits with the executive who chairs the review."),
              ("Governance · consistent consequences", "Shortfalls in individual KPIs are examined closely, while a condition failure in a senior leader's area passes without examination. People conclude that the conditions are off limits.")])
        + P("The review then hears one side of every gap, and the organisation never learns which of its conditions the strategy is outgrowing."),
        stack=True, hl=HL3, ol=OL3),
]

S32_REF_P = ('<div class="u8-h">Personal reflection &middot; Portfolio Work</div>'
    '<div class="u8-how"><div class="u8-how-h">Portfolio work &middot; How to complete this reflection</div><ol>'
    '<li>Read the card for your own role and the cards for the two roles closest to yours.</li>'
    '<li>' + h("Name the fracture your review habits are most prone to open, and the habit behind it, in the way you review individuals' performance and the organisational conditions you are responsible for.") + '</li>'
    '<li>Write the remedial action you will take and the evidence that will show it is working.</li>'
    '<li>This is personal work. Your answer goes to your facilitator when you select Submit to Facilitator.</li></ol></div>'
    '<div class="ref-block" style="margin-top:16px;"><div class="ref-label">&#x270E; Reflection &mdash; The Fracture You Are Most Prone To</div>'
    '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">' + h("Which of the four fractures are your own review habits most prone to open, in the way you review individuals and the organisational conditions you are responsible for? What remedial action will you take, and what evidence will show it is working?") + '</p>'
    '<textarea class="ref-ta reflection-textarea" id="ref9" style="min-height:90px;" placeholder="The fracture I am most prone to open, and the habit behind it:&#10;My remedial action:&#10;The evidence that will show it is working:"></textarea>'
    '<div class="ref-saved reflection-saved" id="ref9-saved"></div><button class="ref-save" onclick="saveTA(this)">Save Reflection</button></div>')
S32_REF_F = ('<div class="fac-note-full u8-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>'
    '<p>' + h("Participants complete a personal reflection in their own file as Portfolio work: the fracture their own review habits are most prone to open, in the way they review individuals and the organisational conditions they are responsible for, the remedial action they will take and the evidence that will show it is working.") + '</p></div>')

# ───────── Section 4
S4_FG = ('<p>' + h("The shift in this section is from function to enterprise, guided by the question “Is the chain of execution across our functions holding together?”") + '</p>\n'
         '<p><strong>4.1 &middot; The Enterprise Performance Intelligence Circle (EPIC).</strong> ' + h("Teach what EPIC is for, then the three signals in order (progress, early warnings, execution learning), each with the evidence behind it.") + '</p>\n'
         '<p><strong>4.2 &middot; The Accountability Loop Role Play.</strong> ' + h("Run the role play in groups of three: leader, team member and observer. The observer deduces how the conversation went through GROW and which root cause it revealed.") + '</p>\n'
         '<p>' + h("The full teaching notes are in the slide notes.") + '</p>\n')

RC3 = 'Lack of Accountability, Lack of Skill, or Misfit of Role or Structural Constraint'

def ol(items):
    return '<ol>' + ''.join('<li>' + h(i) + '</li>' for i in items) + '</ol>'

HOW_RP_P = ['You work in groups of three: the leader, the team member and the observer.',
    'Everyone reads the scenario and the three roles.',
    'Before the conversation, the team member privately chooses one of the three root causes as the reason behind the gap: ' + RC3 + '. The team member plays the conversation from that position, drawing on their own experience, and tells no one which root cause they chose.',
    'The leader decides what the conversation must achieve and runs it through the GROW model. The observer says nothing and completes the observation sheet.',
    'The observer reports first: what the leader set out to achieve, how the conversation went at each GROW stage, and which root cause it revealed. The team member then says which root cause they chose. The leader closes with what they would do differently.']
HOW_RP_F = ['Put participants into breakout rooms of three: the leader, the team member and the observer.',
    'Each group reads the scenario and the three roles.',
    'Before the conversation, the team member privately chooses one of the three root causes as the reason behind the gap: ' + RC3 + '. The team member plays the conversation from that position, drawing on their own experience, and tells no one which root cause they chose.',
    'The leader decides what the conversation must achieve and runs it through the GROW model. The observer says nothing and completes the observation sheet.',
    'The observer reports first: what the leader set out to achieve, how the conversation went at each GROW stage, and which root cause it revealed. The team member then says which root cause they chose. The leader closes with what they would do differently.']

SCEN_CLASS = ('<p>' + h("The Head of Customer Service is responsible for the Key Result: ") + '<strong>&ldquo;Reduce the average time to resolve customer complaints from 10 working days to 5 by the end of the quarter.&rdquo;</strong> ' + h("It supports the enterprise Objective of improving customer retention.") + '</p>'
    + P("The Complaints Team Leader leads a team of eight agents and was fully committed to the Key Result when it was agreed at the start of the quarter.")
    + P("Seven weeks into the quarter, the latest Review shows that resolution time fell from 10 days to 8 in the first month and has not moved since. The Complaints Team Leader missed the last two weekly check-ins, and their written updates have become short. The Head of Customer Service calls a conversation to establish what lies behind the gap."))

ROLES = ('<div class="rp-roles">'
    '<div class="rp-role"><div class="rp-role-title">&#128100; The leader &middot; Head of Customer Service</div><p>' + h("Decides the goal of the conversation, then works through Reality, Options and Will to reach it.") + '</p></div>'
    '<div class="rp-role"><div class="rp-role-title">&#128100; The team member &middot; Complaints Team Leader</div><p>' + h("Responds as the person behind the stalled Key Result, from the root cause they chose.") + '</p></div>'
    '<div class="rp-role"><div class="rp-role-title">&#128100; The observer</div><p>' + h("Says nothing during the conversation and completes the observation sheet.") + '</p></div>'
    '</div>')

OBS = ('<div class="u8-how"><div class="u8-how-h">The observation sheet</div>' + ol([
    'Goal: what was the leader aiming to achieve? Was it clear to the team member?',
    'Reality: which questions opened up what is really happening? Which lines point to the root cause?',
    'The root cause: ' + RC3 + '? Which lines rule out the other two?',
    'Options: who generated the ways forward? Did they match the root cause?',
    'Will: what was agreed, by whom, and when will it be reviewed?',
    'Did the conversation reach its goal? What did the leader do that helped, and what closed the conversation down?']) + '</div>')

DIAG = ('<h4>Accountability Loop Diagnosis</h4>\n<p>The leader must determine whether the root cause is:</p>\n<div class="loop-diag">\n'
    '  <div class="loop-cell"><div class="loop-cell-label">Root Cause A</div><div class="loop-cell-name">Lack of Accountability</div><p>The individual understands the task but has lost motivational connection. Recovery: reconnect to purpose and enterprise context.</p></div>\n'
    '  <div class="loop-cell"><div class="loop-cell-label">Root Cause B</div><div class="loop-cell-name">Lack of Skill</div><p>The individual is committed but lacks the capability required. Recovery: coaching, training, timeline adjustment.</p></div>\n'
    '  <div class="loop-cell"><div class="loop-cell-label">Root Cause C</div><div class="loop-cell-name">Misfit of Role or Structural Constraint</div><p>Strengths do not align with responsibilities. Recovery: structural alignment, redistribution, or repositioning.</p></div>\n'
    '</div>\n')

GROW = ('<h4>The GROW Model in the Accountability Loop</h4>\n<p>' + h("The GROW model guides a conversation with an end in mind. Each stage asks a question, and the team member does the thinking, so the answers reached are their own.") + '</p>\n<div class="u8-grow4">\n'
    '  <div><div class="g-l">G</div><div class="g-n">Goal</div><p>' + h("What the leader aims to achieve in the conversation. It may be identifying the root cause of the gap, restoring alignment with the Key Result, or both.") + '</p><p class="g-q">&ldquo;What do we want to have agreed by the end of this conversation?&rdquo;</p></div>\n'
    '  <div><div class="g-l">R</div><div class="g-n">Reality</div><p>' + h("What is true today. The leader explores what stands behind the gap and listens without defending the target.") + '</p><p class="g-q">&ldquo;What is happening on this Key Result, and what makes it hard?&rdquo;</p></div>\n'
    '  <div><div class="g-l">O</div><div class="g-n">Options</div><p>' + h("What could be done. The team member generates the ways forward, matched to the root cause.") + '</p><p class="g-q">&ldquo;What could change? What support would make the difference?&rdquo;</p></div>\n'
    '  <div><div class="g-l">W</div><div class="g-n">Will</div><p>' + h("What will be done, by whom and by when, and when it will be reviewed.") + '</p><p class="g-q">&ldquo;What will you do, and when shall we look at it again?&rdquo;</p></div>\n'
    '</div>\n')

SCEN_PF = ('<p>' + h("The Chief Financial Officer is responsible for the Key Result: ") + '<strong>&ldquo;Reduce debtor days from 65 to 45 by the end of the half-year.&rdquo;</strong> ' + h("It supports the enterprise Objective of strengthening cash flow.") + '</p>'
    + P("The Credit Control Manager joined the finance team four years ago as a credit analyst and was appointed manager eighteen months ago. Three months into the half-year, debtor days fell from 65 to 58 in the first two months and have not moved since. Most of the overdue balance now sits with twelve large customers."))

DLG_LINES = [
 ('c', "Thank you for making time. I want us to leave this conversation with a clear view of what is holding debtor days at 58, and an agreed way to move them. Can we start with the numbers?"),
 ('m', "Of course. We went from 65 to 58 in two months. Since then, nothing."),
 ('c', "What produced the first seven days?"),
 ('m', "The clean-up. I went through every disputed invoice, matched them against the delivery notes and cleared most of the disputes. I also redesigned the monthly statements so customers can see exactly what is overdue. That took the easy part out."),
 ('c', "That was strong work. What is left?"),
 ('m', "Twelve large customers. Their invoices are correct and undisputed. They simply pay late, and they will only move if someone calls their finance director and holds firm."),
 ('c', "Who makes those calls today?"),
 ('m', "Mostly the senior clerk. I make some of them."),
 ('c', "Would another course help? You attended the negotiation programme last year."),
 ('m', "I know what to say. The course was useful, and I can tell you the techniques. The calls themselves wear me down. Every one of them becomes an argument, and I put them off for days. When I do make them, I give ground too early."),
 ('c', "So the technique is there, and the calls themselves are hard for you. Tell me more about how your week goes."),
 ('m', "Honestly, the parts I enjoy are the analysis, the reconciliations and fixing the process. I would happily spend all week on those. The phone work for the big accounts is most of what this Key Result now needs, and it is the part I am weakest at."),
 ('c', "How do you see the 45 target?"),
 ('m', "It is the right target. Cash matters, and I want us to reach it. I just do not think I am the right person to be on the phone with those twelve customers."),
 ('c', "What could change?"),
 ('m', "The senior clerk is very good on the phone. Customers respect her. If she took the twelve large accounts, I could take over all the dispute work and the reporting for the whole ledger, including her current accounts."),
 ('c', "What would she need from you?"),
 ('m', "The analysis on each account before every call: what is overdue, the payment history and the agreed terms. I can have that ready every Monday."),
 ('c', "Let us agree that. From next week she leads the calls on the twelve accounts, with your analysis every Monday, and you take the disputes and reporting for the whole ledger. I will confirm the change with her tomorrow. We will look at debtor days together at the end of the month."),
 ('m', "Thank you. That works."),
 ('c', "One more thing. Whether the shape of your role needs to change for the longer term is a separate conversation. I would like us to have it next week."),
 ('m', "I would welcome that."),
]
def dlg():
    rows = []
    for who, t in DLG_LINES:
        if who == 'c':
            rows.append('<div class="u8-dlg-r u8-dlg-cxo"><b>CFO &middot; Chief Financial Officer</b><p>' + h(t) + '</p></div>')
        else:
            rows.append('<div class="u8-dlg-r u8-dlg-hl"><b>Credit Control Manager</b><p>' + h(t) + '</p></div>')
    return '<div class="u8-dlg">\n' + '\n'.join(rows) + '\n</div>\n'

HOW_PF = ['Read the scenario, then the conversation between the Chief Financial Officer and the Credit Control Manager.',
    'Work out which of the three root causes is evident: ' + RC3 + '. The conversation does not name it.',
    'Use the GROW model to analyse how the leader ran the conversation.',
    'Answer the four questions below, quoting the lines that support each answer.',
    'This is personal work. Your answers save as you type and go to your facilitator when you select Submit to Facilitator.']

BOXES = ('<div class="u8-s5">\n'
 '  <div class="u8-s5-h"><span class="u8-s5-n">Your analysis of the conversation</span></div>\n'
 '  <label class="wp-label" for="rp_review">Review &middot; What does the evidence show about the Key Result? Quote the lines.</label><textarea class="wp-ta reflection-textarea" id="rp_review" style="min-height:110px;" placeholder="The evidence:&#10;The lines that show it:"></textarea><div class="reflection-saved" id="rp_review-saved"></div>\n'
 '  <label class="wp-label" for="app_rootcause">Realign &middot; Which of the three root causes is evident? Which lines point to it, and which lines rule out the other two?</label><textarea class="wp-ta reflection-textarea" id="app_rootcause" style="min-height:110px;" placeholder="The root cause:&#10;The lines that point to it:&#10;The lines that rule out the other two:"></textarea><div class="reflection-saved" id="app_rootcause-saved"></div>\n'
 '  <label class="wp-label" for="app_corrective">Restore with GROW &middot; What was the goal of the conversation, and how did Reality, Options and Will lead to it?</label><textarea class="wp-ta reflection-textarea" id="app_corrective" style="min-height:110px;" placeholder="Goal:&#10;Reality:&#10;Options:&#10;Will:"></textarea><div class="reflection-saved" id="app_corrective-saved"></div>\n'
 '  <label class="wp-label" for="rp_judge">Your judgement &middot; How well did the leader run the conversation? What would you do differently?</label><textarea class="wp-ta reflection-textarea" id="rp_judge" style="min-height:110px;" placeholder="What helped:&#10;What closed the conversation down:&#10;What I would do differently:"></textarea><div class="reflection-saved" id="rp_judge-saved"></div>\n'
 '</div>\n')

S42_P = ('<div class="acc-b"><div class="cb">\n'
 + P("Part 4.2 has two parts. In class, you role play an Accountability Loop conversation in a group of three. After class, you work alone on a new case: you read a full conversation, work out which of the three root causes is evident and analyse the conversation with the GROW model.") + '\n'
 + '<div class="u8-h">In class &middot; the role play</div>\n'
 + '<div class="u8-how"><div class="u8-how-h">How the role play works</div>' + ol(HOW_RP_P) + '</div>\n'
 + '<div class="rp-scenario">\n  <div class="rp-scenario-label">&#9658; In class &middot; the scenario</div>\n' + SCEN_CLASS + '\n</div>\n'
 + ROLES + '\n' + OBS + '\n' + DIAG + GROW
 + '<div class="u8-h">After class &middot; Portfolio work on a new case</div>\n'
 + '<div class="u8-how"><div class="u8-how-h">Portfolio work &middot; How to complete the case</div>' + ol(HOW_PF) + '</div>\n'
 + '<div class="rp-scenario">\n  <div class="rp-scenario-label">&#9658; After class &middot; the scenario</div>\n' + SCEN_PF + '\n</div>\n'
 + '<div class="u8-h">The conversation</div>\n' + dlg() + BOXES
 + '</div></div></div>\n\n')

ANSWER = ('<div class="u8-h">What the conversation shows</div>\n<ul class="u8-list">'
 '<li><strong>The root cause: Misfit of Role or Structural Constraint.</strong> ' + h("The misfit shows in “The calls themselves wear me down” and “the parts I enjoy are the analysis…”.") + '</li>'
 '<li><strong>Lack of Accountability is ruled out</strong> ' + h("by “It is the right target… I want us to reach it.”") + '</li>'
 '<li><strong>Lack of Skill is ruled out</strong> ' + h("by “I know what to say… I can tell you the techniques.”") + '</li>'
 '<li><strong>The conversation.</strong> ' + h("The CFO sets the goal at the start. The question about another course assumes Lack of Skill before Reality has been explored; the CFO recovers, lets the Credit Control Manager generate the option, agrees the change and the review date, and keeps the role conversation separate.") + '</li></ul>\n')

S42_F = ('<div class="acc-b"><div class="cb">\n'
 + P("Part 4.2 has two parts. In class, participants role play an Accountability Loop conversation in groups of three. After class, in their own file, each participant reads a full conversation on a new case, works out which of the three root causes is evident and analyses the conversation with the GROW model.") + '\n'
 + '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — In class: running the role play online</div>\n<p>This is class practice. Nothing is entered on the portal during the role play.</p>\n' + ol(HOW_RP_F) + '\n</div>\n'
 + '<div class="rp-scenario">\n  <div class="rp-scenario-label">&#9658; In class &middot; the scenario</div>\n' + SCEN_CLASS + '\n</div>\n'
 + ROLES + '\n' + OBS + '\n' + DIAG + GROW
 + '<div class="u8-h">After class &middot; the case participants analyse in their own file</div>\n'
 + P("This case is different from the role play, and the root cause is never named in the conversation.") + '\n'
 + '<div class="rp-scenario">\n  <div class="rp-scenario-label">&#9658; After class &middot; the Portfolio scenario</div>\n' + SCEN_PF + '\n</div>\n'
 + dlg() + ANSWER
 + '</div>\n'
 + '<div class="fac-note-full u8-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n'
 + P("After the role play, participants complete personal Portfolio work in their own file. They read the conversation between the Chief Financial Officer and the Credit Control Manager, work out the root cause and analyse the conversation with the GROW model:") + '\n'
 + ol(['Review: what the evidence shows about the Key Result.',
       'Realign: which of the three root causes is evident, the lines that point to it and the lines that rule out the other two.',
       'Restore with GROW: the goal of the conversation, and how Reality, Options and Will led to it.',
       'Their judgement: how well the leader ran the conversation, and what they would do differently.']) + '\n'
 + '</div>\n</div></div>\n\n')

# ───────── Section 5
S5_HOW_P = ('<div class="u8-how"><div class="u8-how-h">How Section 5 works</div><p>This is group work and Capstone work. For each of the four consequences of weak review discipline, your group:</p><ol>'
    '<li>' + h("Simulates a potential gap in the performance of individuals, and a potential gap in the organisational conditions of your strategy.") + '</li>'
    '<li>' + h("Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.") + '</li></ol>'
    '<p>' + h("Your group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page. Then select Confirm. Your confirmed record feeds your team's Capstone Blueprint.") + '</p></div>')
S5_HOW_F = ('<div class="u8-how"><div class="u8-how-h">How Section 5 works</div><p>This is group work and Capstone work. For each of the four consequences of weak review discipline, each group:</p><ol>'
    '<li>' + h("Simulates a potential gap in the performance of individuals, and a potential gap in the organisational conditions of its strategy.") + '</li>'
    '<li>' + h("Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.") + '</li></ol>'
    '<p>' + h("The group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page, then selects Confirm. The confirmed record feeds the team's Capstone Blueprint.") + '</p></div>')
S5_FG = ('<p>' + h("The groups apply the four consequences to the strategy in their Capstone Blueprint. For each consequence, they simulate a potential gap in the performance of individuals and in the organisational conditions, and write a decision point for recovery for each.") + '</p>\n'
         '<p>' + h("Online: the scribe types the agreed entries; every member then types them into their own page. Capstone work is reviewed independently at graduation. The full teaching notes are in the slide notes.") + '</p>\n')

S5_STEPS = ('<ol><li>Read the lesson for this consequence.</li>'
    '<li>' + h("Simulate a potential gap of this consequence in the performance of individuals, and one in the organisational conditions of your strategy.") + '</li>'
    '<li>' + h("For each gap, write the decision point for recovery: the decision the executive team takes when the gap appears, and who takes it.") + '</li></ol>')

CONS = [('1', 'Early Warning Signals Are Missed', 'missed early warning signals',
         "If a Key Result shows no movement across two monthly reviews, then a recovery plan is presented at the next executive review, taken by the executive accountable for the Key Result."),
        ('2', 'Gradual Diffusion of Accountability', 'diffused accountability',
         "If a Key Result has not been discussed in an executive review for a full month, then it goes first on the agenda of the next review, with the individuals delivering it present, taken by the CEO."),
        ('3', 'Loss of Organisational Learning', 'lost organisational learning',
         "If the same obstacle is reported in two functions in one quarter, then the executive team names the cause and records what it changes in the way the strategy is executed, taken by the CEO."),
        ('4', 'Erodes Leadership Credibility', 'eroding leadership credibility',
         "If a strategic priority is announced with no date for its first review, then the date and the evidence to be brought to it are fixed in the same meeting, taken by the CEO.")]

def s5_completes(gap):
    return ('<ul class="u8-list"><li>' + h("A potential gap of " + gap + " in the performance of individuals and in the organisational conditions, and for each gap a decision point for recovery: the decision the executive team takes when the gap appears, and who takes it.") + '</li></ul>')

PH = 'If [the gap appears], then [the recovery decision], taken by [who]...'
LBL1 = 'Individuals &middot; the potential gap and the decision point for recovery'
LBL2 = 'Organisational conditions &middot; the potential gap and the decision point for recovery'

# ───────── Unit Summary (participant SUMMARY array, JS strings) and facilitator cards
SUM_P = {
 'Awareness': " Each review examines both the progress of what individuals and teams deliver and whether the organisational conditions support the execution of their tasks.",
}
