# -*- coding: utf-8 -*-
"""Unit 8 · the two performance views (15 October 2026): surgical changes on Carol's deck.
python3 deck_u08pv.py <her deck> <pictures folder> <out deck>
Slide texts change on 15 (3.2: the map of where fractures begin comes out), 19, 20 (4.2), 24 (5.1).
Notes carry the two-view content and the facilitator detail moved off the page. Reflection pictures: 1.1, 2.1 retaken; 3.2 added."""
import sys, os, copy
from pptx import Presentation
from pptx.util import Emu

src, pics, out = sys.argv[1:4]
prs = Presentation(src)
S = lambda n: prs.slides[n - 1]

def notes(n):
    return S(n).notes_slide.notes_text_frame

def get(n):
    return notes(n).text

def put(n, t):
    notes(n).text = t

def insert_before(n, heading, block):
    t = get(n)
    i = t.find(heading)
    if i < 0:
        raise SystemExit('slide %d: heading %r not found' % (n, heading))
    put(n, t[:i] + block.rstrip('\n') + '\n\n' + t[i:])

def append(n, block):
    put(n, get(n).rstrip('\n') + '\n\n' + block.rstrip('\n'))

def rep_note(n, old, new):
    t = get(n)
    if t.count(old) != 1:
        raise SystemExit('slide %d: note text not found once: %r' % (n, old[:70]))
    put(n, t.replace(old, new))

def set_text(n, shape_name, new):
    for sh in S(n).shapes:
        if sh.name == shape_name and sh.has_text_frame:
            tf = sh.text_frame
            runs = [r for p in tf.paragraphs for r in p.runs]
            # keep the first paragraph's first run formatting; one paragraph only
            first = tf.paragraphs[0]
            for p in tf.paragraphs[1:]:
                p._p.getparent().remove(p._p)
            rs = first.runs
            rs[0].text = new
            for r in rs[1:]:
                r._r.getparent().remove(r._r)
            return
    raise SystemExit('slide %d: shape %s not found' % (n, shape_name))

def set_two_runs(n, shape_name, a, b):
    """Shapes like 'Goal  Ownership again…' hold a bold run and a plain run."""
    for sh in S(n).shapes:
        if sh.name == shape_name:
            rs = [r for p in sh.text_frame.paragraphs for r in p.runs]
            if len(rs) < 2:
                set_text(n, shape_name, a + b); return
            rs[0].text = a; rs[1].text = b
            for r in rs[2:]:
                r._r.getparent().remove(r._r)
            return
    raise SystemExit('slide %d: shape %s not found' % (n, shape_name))

def swap_picture(n, name, path):
    from PIL import Image
    for sh in S(n).shapes:
        if sh.name == name:
            img_part, rId = S(n).part.get_or_add_image_part(path)
            sh._element.blipFill.blip.rEmbed = rId
            w, h = Image.open(path).size
            old_h = sh.height
            sh.height = Emu(int(sh.width * h / w))
            return sh.height - old_h
    raise SystemExit('slide %d: picture %s not found' % (n, name))

def shift(n, names, dy):
    for sh in S(n).shapes:
        if sh.name in names:
            sh.top = sh.top + dy

# ── Slide 1: unit purpose
rep_note(1, 'Now the most important discipline of execution begins: the performance review conversation.',
         'Now the most important discipline of execution begins: the performance review conversation. Each review examines two things: the progress of what individuals and teams deliver, and whether the organisational conditions support the execution of their tasks.')

# ── Section 1
append(4, """TEACHING NOTES FROM THE FACILITATOR GUIDE:
1.1 · The Execution Visibility Infrastructure. Open with the provocation: "Work is happening. Teams are busy. Initiatives are underway. But can you confidently say the work being done is actually advancing the strategy?" Then teach performance measurement as the visibility infrastructure of the strategy: without it, strategy stays interpretive, each function develops its own sense of progress and activity is mistaken for advancement. The shift to land is from "What work was done?" to "What changed because of the work?", from the human side and the organisation side.
1.2 · The Four Strategic Purposes. Teach execution rhythm first: regular reviews reveal the subtle signals early and prevent the most common leadership surprise, discovering failure at the end of the reporting period. Then teach the four purposes one card at a time, each from both sides. Most leaders can name visibility and accountability; fewer name execution intelligence (data interpreted into decision insight through disciplined conversation) and timely correction.
1.3 · From Performance Measurement to Execution Recovery. Link the four purposes to the Review–Realign–Restore Cycle (R3): Review brings together visibility, accountability and execution intelligence; Realign diagnoses the gap; Restore activates timely correction. Teach each stage for both operating systems. Name the outcome of each stage, and close on how the cycle stays continuous: the next Review checks whether the corrective actions worked.
1.4 · The Accountability Loop. Start from the default response to a gap: pushing harder. The key facilitation moment is when leaders understand that most performance gaps have a diagnosable cause, and that the three root causes (accountability, skill, structural misfit) require different responses. Help leaders distinguish between team members who cannot perform and those who will not: inability needs development, and unwillingness needs accountability. Then teach how each recovery is achieved through the GROW model of Unit 7 (Goal, Reality, Options, Will). Close on keeping the performance conversation separate from the role conversation.""")

insert_before(5, 'What activity measures give:', """THE HUMAN SIDE AND THE ORGANISATION SIDE:
The visibility infrastructure.
From the human side: leaders see whether individuals and teams are moving their KPIs, OKRs and behaviours toward the enterprise result.
From the organisation side: leaders see whether the organisational conditions support the execution of the individuals' tasks. These conditions are the Environment, Systems, Resources and Governance (ESRG) agreed in Unit 6.
From activity to progress.
From the human side: the question moves from "How busy are our people?" to "What has their work changed in the Key Result?"
From the organisation side: the question moves from "Has the support been put in place?" to "Does the support enable the individuals' tasks to move the Key Result?\"""")

append(6, """THE HUMAN SIDE AND THE ORGANISATION SIDE OF EACH PURPOSE:
01 · Creates Visibility. Human side: where individuals' and teams' KPIs are gaining momentum and where they are stalling. Organisation side: where the organisational conditions are supporting the execution of the tasks, and where they are holding it back.
02 · Establishes Accountability. Human side: individuals and teams know which part of the strategy they are responsible for advancing, and their delivery is recorded as evidence. Organisation side: leaders account for whether the organisational conditions they undertook to provide in Unit 7 support the execution of the individuals' tasks.
03 · Execution Intelligence. Human side: the review learns what accelerates and what slows the progress of individuals and teams. Organisation side: the review learns which organisational conditions enable execution and which constrain it.
04 · Enables Timely Correction. Human side: an early signal in an individual's progress lets the leader intervene while the KPI is still recoverable. Organisation side: an early signal in an organisational condition, such as a system outage, a capacity shortfall or a delayed decision, lets the leader responsible act before the individuals' delivery is affected.""")

append(7, """THE CYCLE APPLIES TO BOTH OPERATING SYSTEMS:
Review. Human side: the individual and the leader establish the progress made against the agreed target. Organisation side: the leader brings the agreed measures or evidence of readiness for the organisational conditions, and the review establishes whether those conditions support the execution of the individuals' tasks.
Realign. Human side: the Accountability Loop (part 1.4) diagnoses what is preventing the individual's expected performance. Organisation side: the leader determines what is preventing an organisational condition from supporting the execution of the individuals' tasks, and agrees the response.
Restore. Human side: the individual commits to the corrective actions and the follow-up dates. Organisation side: the leader responsible commits to the actions on the organisational conditions, each with a review date.
How the cycle remains continuous: the next Review examines both: the individuals' progress, and whether the organisational conditions now support their tasks.""")

rep_note(9, 'What would reflect genuine progress toward your strategic outcome?"',
         'What would reflect genuine progress toward your strategic outcome? What evidence do you hold on whether the organisational conditions support the tasks behind that progress?"')
dy = swap_picture(9, 'Reflection 1.1', os.path.join(pics, 'r11.png'))
shift(9, ('Reflection 1.4', 'Part 1.4'), dy)

# ── Section 2
append(10, """TEACHING NOTES FROM THE FACILITATOR GUIDE:
2.1 · Execution velocity. Open with the question "What determines the velocity of the flight?" and teach execution velocity: the rate at which an organisation converts strategic intent into measurable results, shaped by how quickly leaders detect, understand, decide and act. Performance measurement provides the evidence; review discipline converts it into timely decisions.
2.1 · Four Consequences of Weak Review Discipline. Teach the four consequences as one chain, one card at a time, each from the human side and the organisation side. Ask the question on each card once the card is taught, so participants recognise the chain in their own organisations.""")

S2 = """THE HUMAN SIDE AND THE ORGANISATION SIDE OF EACH CONSEQUENCE:

01 · Early Warning Signals Are Missed
Human side: early warnings on the human side show in the review conversation before they show in the KPI. Three patterns recur. The quality of evidence falls: results give way to explanations, and percentages arrive without the evidence behind them. Alignment drifts: the individual who rated alignment at 9 when the target was agreed now gives short, guarded answers about the target, and no one asks the alignment question again. Effort migrates: the individual's time moves to work that senior leaders ask about, and the KPI receives what is left. Each pattern leads a missed KPI by weeks. A leader who reviews monthly sees it as a trend across two or three conversations; a leader who reviews at quarter end sees the result alone. The difference is the recovery available: a capability gap seen in week four can be met with coaching; the same gap seen in week twelve leaves a revised target.
Organisation side: an early warning on the organisation side is evidence that an organisational condition has started to weaken in its support for the individuals' tasks. It seldom carries a number of its own, so the review sees it only when it asks for it.
Resources · workforce capacity. A contact centre carries a customer-retention Key Result. Two agents resign and their posts stay open for a quarter. The remaining team covers the volume through overtime, and resolution times hold for six weeks, then fall sharply as absenteeism rises. The vacancy and the overtime were on record weeks before the KPI moved.
Environment · psychological safety. In a function where raising a problem in front of senior leaders has carried a cost, team leads report amber milestones as green. The review sees on-track ratings until a milestone is missed. The warning was there all along: months without a single amber rating.
Systems · data integrity. Sales, operations and finance each report from their own platform, and every cross-functional figure is consolidated by hand. The executive review works on information a week old, and a slipping delivery reaches the review after customers have already escalated it.
Measures or evidence of readiness for each condition give these signals a place in the review. When the review does not ask for them, the condition shows itself through the KPI it was meant to support.

02 · Gradual Diffusion of Accountability
Human side: individuals read priority from the review agenda. When a KPI is absent from three reviews in a row, the conclusion is reasonable: leadership attention has moved. Accountability then weakens in three ways. The KPI is managed for appearance: updates are written to reassure, and risks are held until they can no longer be hidden. Ownership of a shared KPI spreads thin: each individual assumes another is carrying the result, and the dependencies between them belong to no one. The commitment loses its force: the commitment given when the target was agreed has not been tested since. When the gap finally surfaces, the review becomes a search for who was responsible. The Accountability Loop cannot diagnose a commitment no one has been asked about.
Organisation side: leaders make commitments on organisational conditions when targets are agreed. These commitments seldom appear on any scorecard, so they diffuse first.
Resources · capability alignment. A new procurement system is introduced with the promise that every buyer will be trained. Three months later half the buyers are untrained and purchase orders take twice as long. The buyers' cycle-time KPI is reviewed every month; the training commitment has never been raised.
Governance · clear accountability. A regional manager is accountable for a margin Key Result, yet every discount above a set level still needs head-office sign-off. The change to the delegation was approved in principle and never issued. The manager carries the accountability without the authority to deliver it.
Individuals remain held to their targets while the support they were promised quietly lapses. Mutual accountability becomes one-sided, and individuals protect themselves: they commit to less, document more and move from commitment to compliance.

03 · Loss of Organisational Learning
Human side: every review produces evidence on how results are achieved, and that evidence is the raw material of the organisation's performance capability. Practices that accelerate progress: one regional team meets its targets because its manager runs a short daily huddle on the Key Result. Recorded and examined, the practice can be taught to other teams. Unexamined, it stays one manager's habit and leaves when that manager leaves. Capability gaps that recur: when the same skill gap appears in reviews across several functions, it signals a development need at enterprise level. Behaviours that strengthen ownership: reviews show which leaders' teams surface problems early and which conceal them. When reviews only record results, talent decisions, development plans and succession rest on ratings with no evidence of how the results were achieved. The organisation keeps rewarding outcomes it cannot reproduce.
Organisation side: reviews also show how the organisational conditions behave as the strategy places weight on them. The learning is cumulative: the same constraint appearing in several reviews is evidence that a condition is not yet equal to the strategy.
Systems · process clarity. Three functions each report delays at the handover between sales order and dispatch. Reviewed function by function, each delay looks local. Reviewed together, they show one handover that no one is responsible for.
Resources · financial support. For two years running, the budget for strategic initiatives is released in the second quarter, and each year the initiatives deliver in the second half alone. The pattern becomes visible only when reviews are compared across cycles.
Governance · decision authority. Capital requests above a set value wait a month on average for an executive decision, and every Key Result that depends on one slips by about the same margin.
When reviews do not capture this learning, the organisation sets its next strategy on the same conditions. Targets rise, the conditions stay where they were, and the same constraints slow execution again. This learning is the evidence the executive team needs to judge whether the organisation can carry its next level of ambition.

04 · Erodes Leadership Credibility
Human side: credibility is built in the review. A leader who asks for evidence every month, recognises progress and addresses shortfalls consistently shows that the priority is real. Two patterns erode it. Priorities that fade: a strategic KPI launched with energy disappears from the review agenda, and individuals conclude the announcement was symbolic. High performers, who invest most in strategic commitments, become the most sceptical, and the organisation learns to wait and see whether a priority survives its first quarter. Standards applied unevenly: some individuals' KPIs are examined closely while others are excused, often by seniority. Individuals read this as unfairness, and commitment falls across the whole team.
Organisation side: leaders make commitments when they agree organisational conditions, and individuals track these closely because their own delivery depends on them. Credibility on this side is a test of fairness.
Environment · values and consequences. The organisation states accountability as a value. A junior manager is challenged in the review for a missed milestone, while a senior executive's missed commitment to release staff for the same project is never raised.
Environment · psychological safety. Leaders invite open reporting of risks, and the first person to raise a delivery risk in a review is questioned in front of peers. From then on, risks reach the review late.
Governance · execution oversight. The executive team commits to a monthly decision forum to clear constraints, then postpones it twice in one quarter while the decisions wait.
When leaders review individuals' targets and leave their own commitments unreviewed, individuals see accountability running one way. Reviewing both, to the same evidence standard, shows that leaders hold themselves to the standard they set for others."""
insert_before(11, 'ON THE PORTAL, AFTER THE TEACHING:', S2)

rep_note(12, 'Which of the four consequences followed, and what did the delay cost?"',
         'Which of the four consequences followed, and what did the delay cost? Did an organisational condition play a part in the delay?"')
swap_picture(12, 'Reflection 2.1', os.path.join(pics, 'r21.png'))

# ── Section 3
append(13, """TEACHING NOTES FROM THE FACILITATOR GUIDE:
3.1 · Four Fractures in Performance Measurement. Teach the four gaps as observable patterns and invite participants to place their organisation honestly on each one, each with its implication for human performance and for organisational performance. The Horizontal Coordination Gap is typically the most impactful but least visible: each function may report strong progress while the enterprise outcome remains inconsistent. The Learning Suppression Gap is often the most culturally embedded and the hardest to shift, because it requires leaders to move from a judgement posture to a curiosity posture.
3.2 · The CXO Performance Gap Contributors. Teach the logic of the cards first: how the role reviews performance (its meetings and its evidence), what the role does in those reviews, and what happens as a result, which opens one of the four fractures of part 3.1. Then take each participant's own role first and the two roles closest to it. Participants complete the reflection on the fracture they are most prone to as Portfolio work.""")

S3 = """IMPLICATIONS FOR HUMAN PERFORMANCE AND FOR ORGANISATIONAL PERFORMANCE:

Gap 01 · The Horizontal Coordination Gap
Human performance: when each function reviews its own KPIs, individuals are judged on the part of the result they control, and the hand-offs between functions are never examined. An operations planner meets every internal measure while customer orders wait at the boundary with sales. Individuals learn to optimise their own measure, and the commitments they made to other functions go unreviewed: no one is asked whether they delivered what another function needed from them. Individuals whose work depends on another function are held to results they cannot complete alone, and the review sees their shortfall without the dependency behind it.
Organisational performance: the organisational conditions that span functions fall between the reviews.
Systems · process clarity. The order-to-cash process runs through sales, credit control, the warehouse and finance. Each function reviews its own step and reports it on time. No review sees the end-to-end cycle, which is where the customer experiences the delay.
Governance · decision authority. A non-standard customer contract needs approval from legal, finance and operations. Each reports its own turnaround as acceptable; end to end, the decision takes three weeks, and the sales Key Result absorbs the wait.
The executive team sees each function's conditions as adequate while the conditions at the boundaries hold back the enterprise result.

Gap 02 · The Evidence Quality Gap
Human performance: weak evidence harms individuals in two ways. Strong performers cannot show what their contribution changed, and weak delivery stays hidden behind narrative. When the evidence offered is activity, such as training attended or meetings held, the review rates effort. Ratings lose credibility with the individuals themselves, and the performance standard agreed at the start of the period loses its anchor. Over time, individuals learn that the persuasive account is rewarded.
Organisational performance: most reviews hold no evidence at all on organisational conditions. Their state is asserted: the system is stable, the roles are filled, the budget is available.
Resources · workforce capacity. HR reports headcount at budget. The review does not see that a third of the roles in the unit carrying the Key Result are held by new staff still in training. The evidence that matters is productive capacity: how many of those roles can carry the work today.
Systems · workflow visibility. IT reports system availability at 99 per cent. The finance team reports that the month-end report takes three days to run. The first figure describes the system; the second describes whether it supports the tasks.
With no evidence standard for the conditions, the review cannot tell whether they support the individuals' tasks, and the discussion settles on the individuals' numbers, the only evidence in the room.

Gap 03 · The Review Rhythm Breakdown
Human performance: the rhythm of review sets the individuals' planning horizon. Reviewed quarterly, individuals work in quarterly bursts: a slow start, a surge before the period closes and figures prepared for the review. Reviewed irregularly, evidence is assembled in a hurry and the conversation is spent reconstructing what happened. The recoveries of the Accountability Loop need a rhythm short enough for coaching, development or a structural change to take effect within the period.
Organisational performance: organisational conditions often have no rhythm of review at all; they reach the agenda when something fails.
Governance · execution oversight. Capital and risk decisions follow the board calendar, so a decision on a condition a Key Result depends on can wait up to three months.
Resources · financial support. Budgets are reallocated only at the mid-year forecast. An initiative found short of funds in its second month waits until its sixth.
Environment · employee sustainability. Workload is seen through the annual engagement survey, so overload in a critical team shows first in resignations.
When the conditions are reviewed on a slower rhythm than the KPIs they support, the conditions lag the work they are meant to enable.

Gap 04 · The Learning Suppression Gap
Human performance: when reviews judge, individuals defend. They bring the explanation and hold back the obstacle, and in the next cycle they propose targets they are sure to meet. Learning moves out of the review into corridors and private conversations. The organisation loses the individuals' first-hand knowledge of what is slowing execution, the most current intelligence it has.
Organisational performance: suppression falls hardest on the conditions, because naming a condition often means naming a senior leader's area.
Environment · psychological safety. A team lead knows the approval process is the real constraint on the Key Result and does not say so, because the approval sits with the executive who chairs the review.
Governance · consistent consequences. Shortfalls in individual KPIs are examined closely, while a condition failure in a senior leader's area passes without examination. People conclude that the conditions are off limits.
The review then hears one side of every gap, and the organisation never learns which of its conditions the strategy is outgrowing."""
insert_before(14, 'Professional insights:', S3)

# Slide 15: the map of where the fractures begin comes out; the four boxes carry how to read the role cards
for title_shape, body_shape, title, body in [
        ('Text 3', 'Text 4', '1 · How you review performance', 'Your meetings and your evidence.'),
        ('Text 7', 'Text 8', '2 · What you do', 'A habit in those reviews.'),
        ('Text 11', 'Text 12', '3 · What happens as a result', 'The habit opens a fracture of 3.1.'),
        ('Text 15', 'Text 16', '4 · Your own role first', 'Then the two roles closest to yours.')]:
    set_text(15, title_shape, title)
    set_text(15, body_shape, body)
rep_note(15, 'Participants read the ten role cards in part 3.2 of their own file, their own role first, and answer the question on their own card for themselves.',
         'Participants read the ten role cards in part 3.2 of their own file, their own role first, and answer the question on their own card for themselves. They then complete a personal reflection as Portfolio work: the fracture their own review habits are most prone to open, in the way they review individuals and the organisational conditions they are responsible for, the remedial action they will take and the evidence that will show it is working.')

# Slide 16: the 3.2 reflection is added below 3.1
sl = S(16)
p31 = [s for s in sl.shapes if s.name == 'Reflection 3.1'][0]
o31 = [s for s in sl.shapes if s.name == 'Part 3.1'][0]
from PIL import Image
w, h = Image.open(os.path.join(pics, 'r32.png')).size
top = p31.top + p31.height + Emu(548640)
pic = sl.shapes.add_picture(os.path.join(pics, 'r32.png'), p31.left, top, p31.width, Emu(int(p31.width * h / w)))
pic.name = 'Reflection 3.2'
ov = copy.deepcopy(o31._element)
sl.shapes._spTree.append(ov)
o32 = sl.shapes[-1]
o32.name = 'Part 3.2'
o32.top = top + (pic.height - o32.height) // 2
for r in [r for p in o32.text_frame.paragraphs for r in p.runs]:
    r.text = r.text.replace('3.1', '3.2')
rep_note(16, '3.1 Reflection — Which Gap Is Most Prevalent in Your Organisation?: "Rate each gap in your organisation (1 = rare, 5 = common). Then name the gap you are most responsible for closing and your first action."',
         '3.1 Reflection — Which Gap Is Most Prevalent in Your Organisation?: "Rate each gap in your organisation (1 = rare, 5 = common). Then name the gap you are most responsible for closing and your first action."\n3.2 Reflection — The Fracture You Are Most Prone To (Portfolio work): "Which of the four fractures are your own review habits most prone to open, in the way you review individuals and the organisational conditions you are responsible for? What remedial action will you take, and what evidence will show it is working?"')
rep_note(16, '1. Show the slide and read the prompt aloud.', '1. Show the slide and read the two prompts aloud.')
rep_note(16, 'Participants complete this reflection in Section 3 of the participant file, at the foot of part 3.1.',
         'Participants complete these reflections in Section 3 of the participant file, at the foot of parts 3.1 and 3.2.')

# ── Section 4
append(17, """TEACHING NOTES FROM THE FACILITATOR GUIDE:
4.1 · The Enterprise Performance Intelligence Circle (EPIC). Teach what EPIC is for before its detail: it turns the separate PM reviews of each function into one shared view of enterprise execution. Then teach the three signals each leader brings from their PM review sheet, each by the question it answers: progress, "Where are we on execution?"; early warnings, "What is starting to break?"; execution learning, "What is execution teaching us?" For each signal, teach what the leader brings, the sentence the leader uses and what the executive team sees. Progress comes first because it gives the other two their meaning. Teach the evidence rule with the examples of each signal: every signal names the PM review evidence behind it. This single discipline separates EPIC from an opinion forum.
4.2 · The Accountability Loop Role Play. Run the role play in groups of three: leader, team member and observer. The observer deduces how the conversation went through GROW and which root cause it revealed.""")

set_text(19, 'Text 2', 'Complaint resolution fell from 10 days to 8, then stalled, against a target of 5.')
set_text(19, 'Text 3', 'Leader · Team member · Observer. The team member privately chooses the root cause.')
put(19, """4.2 — THE ACCOUNTABILITY LOOP ROLE PLAY (PRACTICE IN CLASS)

HOW TO TEACH IT:

1. Give the case.
Say: "The Head of Customer Service is responsible for the Key Result: Reduce the average time to resolve customer complaints from 10 working days to 5 by the end of the quarter. It supports the enterprise Objective of improving customer retention. The Complaints Team Leader leads a team of eight agents and was fully committed to the Key Result when it was agreed at the start of the quarter. Seven weeks into the quarter, the latest Review shows that resolution time fell from 10 days to 8 in the first month and has not moved since. The Complaints Team Leader missed the last two weekly check-ins, and their written updates have become short. The Head of Customer Service calls a conversation to establish what lies behind the gap."

2. Form the groups of three.
Put participants into breakout rooms of three: the leader, the team member and the observer.
The leader (Head of Customer Service): decides the goal of the conversation, then works through Reality, Options and Will to reach it.
The team member (Complaints Team Leader): responds as the person behind the stalled Key Result, from the root cause they chose.
The observer: says nothing during the conversation and completes the observation sheet.

3. The team member chooses the root cause.
Say: "Team member, before the conversation, choose privately one of the three root causes as the reason behind the gap: Lack of Accountability, Lack of Skill, or Misfit of Role or Structural Constraint. Play the conversation from that position, drawing on your own experience, and tell no one which one you chose."

4. Run the conversation.
The leader decides what the conversation must achieve and runs it through the GROW model.
Brief the leader with this line: "The leader who receives honest feedback about a genuine problem and responds with honesty before justification, and action before communication, creates the conditions for real leadership." (Journal, 29 June 2026, Professional Insights: Leadership)
The observer completes the observation sheet: the goal the leader set and whether it was clear; the questions that opened up what is really happening; the root cause and the lines that rule out the other two; who generated the options and whether they matched the root cause; what was agreed, by whom and when it will be reviewed; whether the conversation reached its goal.
If the leader defaults to pressure, pause and redirect: "You have identified the gap. Now ask about the reality behind it before you move to options."

5. Debrief.
The observer reports first: what the leader set out to achieve, how the conversation went at each GROW stage, and which root cause it revealed. The team member then says which root cause they chose. The leader closes with what they would do differently.
Say: "Accountability without a pathway back becomes punishment. Correct firmly where necessary, and deliberately restore trust, contribution and dignity when change is evident." (Journal, 16 September 2026, Professional Insights: Leadership)

This is class practice. Nothing is entered on the portal during the role play.

ON THE PORTAL, AFTER THE TEACHING:
After class, participants complete personal Portfolio work in part 4.2 of their own file. They read the conversation between the Chief Financial Officer and the Credit Control Manager, in which the root cause is never named. They work out which of the three root causes is evident and the lines that rule out the other two, the goal of the conversation and how Reality, Options and Will led to it, and how well the leader ran the conversation.""")

set_two_runs(20, 'Text 2', 'Goal  ', 'What the leader aims to achieve: the root cause, alignment, or both.')
set_two_runs(20, 'Text 6', 'Reality  ', 'What stands behind the gap.')
set_two_runs(20, 'Text 8', 'Options  ', 'The ways forward the team member generates.')
set_two_runs(20, 'Text 10', 'Will  ', 'What, by whom, by when, and the review date.')
put(20, """4.2 — THE GROW CONVERSATION

HOW TO USE THIS SLIDE:

1. Recall GROW.
Say: "The GROW model guides a conversation with an end in mind. Each stage asks a question, and the team member does the thinking, so the answers reached are their own."

2. Teach each stage as it works in the Accountability Loop.
G · Goal: "What the leader aims to achieve in the conversation. It may be identifying the root cause of the gap, restoring alignment with the Key Result, or both." Question: "What do we want to have agreed by the end of this conversation?"
R · Reality: "What is true today. The leader explores what stands behind the gap and listens without defending the target." Question: "What is happening on this Key Result, and what makes it hard?"
O · Options: "What could be done. The team member generates the ways forward, matched to the root cause." Question: "What could change? What support would make the difference?"
W · Will: "What will be done, by whom and by when, and when it will be reviewed." Question: "What will you do, and when shall we look at it again?"

3. Brief the observer before the role play.
Say: "Note what the leader set out to achieve, and how each stage of GROW moved the conversation toward it: did the leader explore the reality before the options, let the team member generate the options, and close with what will be done, by whom and when it will be reviewed?"

4. Use GROW in the debrief.
The observer reports how the leader used each stage. Ask the group which stage was hardest to hold, and why.
Say: "Leaders who either conceal failure or weaponise it prevent learning. Mature accountability names what went wrong, understands why it happened and moves people toward responsible change." (Journal, 10 August 2026, Professional Insights: Leadership)
Say: "Holding people accountable for outcomes without considering intent produces a culture of blame. Intent matters." (Journal, 17 March 2026, Professional Insights)

ON THE PORTAL, AFTER THE TEACHING:
After class, in part 4.2 of their own file, participants work out the root cause in a full conversation on a new case, the goal of the conversation and how Reality, Options and Will led to it, and how well the leader ran the conversation.""")

rep_note(22, 'Say: "In 4.2, you read a full Accountability Loop conversation on a different case from the role play. The conversation never names the root cause: you deduce which of the three it is, work out how GROW was used to resolve it and move the alignment close to 10, and judge how the CXO applied the loop against GROW. This is personal work, and it builds your learning portfolio."',
         'Say: "In 4.2, you read a full Accountability Loop conversation on a new case: the Chief Financial Officer and the Credit Control Manager. The conversation never names the root cause: you work out which of the three it is, the goal of the conversation and how Reality, Options and Will led to it, and how well the leader ran the conversation. This is personal work, and it builds your learning portfolio."')

# ── Section 5
rep_note(23, """This is group work and Capstone work. Section 2 taught the four consequences of weak review discipline. Here, each group guards the strategy in its Capstone Blueprint against each of them.
The group takes the four consequences one at a time, each on its own tab. The lesson from part 2.1 sits above the boxes.
For each consequence, the group writes two decision points. A decision point names the signal the executive team watches for, the decision it takes when the signal appears and who takes it.
Each decision point is one sentence: “If [the signal appears], then [the decision], taken by [who].” For example: “If a Key Result shows no movement across two monthly reviews, its owner presents a recovery plan at the next executive review.”
The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.
Each member then reads the group’s record at the foot of the section and selects Confirm. The confirmed record feeds the team’s Capstone Blueprint.""",
"""This is group work and Capstone work. For each of the four consequences of weak review discipline, each group:
1. Simulates a potential gap in the performance of individuals, and a potential gap in the organisational conditions of its strategy.
2. Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.
The group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page, then selects Confirm. The confirmed record feeds the team’s Capstone Blueprint.""")
rep_note(23, 'Say: "Your group sets two decision points against each of the four consequences of weak review discipline, for the strategy in your team’s Capstone Blueprint."',
         'Say: "For each of the four consequences of weak review discipline, your group simulates a potential gap in the performance of individuals and in the organisational conditions of the strategy in your team’s Capstone Blueprint, and sets a decision point for recovery for each."')

for shape, label in [('Text 2', '01  Early Warning Signals Are Missed'), ('Text 4', '02  Gradual Diffusion of Accountability'),
                     ('Text 6', '03  Loss of Organisational Learning'), ('Text 8', '04  Erodes Leadership Credibility')]:
    sh = [s for s in S(24).shapes if s.name == shape][0]
    rs = [r for p in sh.text_frame.paragraphs for r in p.runs]
    full = ''.join(r.text for r in rs)
    if '2 decision points' not in full:
        raise SystemExit('slide 24: %s' % full)
    for r in rs:
        if '2 decision points' in r.text:
            r.text = r.text.replace('2 decision points', 'individuals · conditions')
put(24, """5.1 — DECISION POINTS AGAINST THE FOUR CONSEQUENCES (CAPSTONE WORK)

HOW TO TEACH IT:

1. Recall the four consequences of part 2.1.
Say: "Missed early warning signals. Gradual diffusion of accountability. Loss of organisational learning. Eroded leadership credibility. Each shows in the performance of individuals and in the organisational conditions."

2. Say what the group completes for each consequence.
Say: "Simulate a potential gap in your strategy: one in the performance of individuals and one in the organisational conditions. For each gap, write the decision point for recovery: the decision the executive team takes when the gap appears, and who takes it. Write it as one sentence: If the gap appears, then the recovery decision, taken by whom."

3. Give one example for each consequence.
Early Warning Signals Are Missed: "If a Key Result shows no movement across two monthly reviews, then a recovery plan is presented at the next executive review, taken by the executive accountable for the Key Result."
Gradual Diffusion of Accountability: "If a Key Result has not been discussed in an executive review for a full month, then it goes first on the agenda of the next review, with the individuals delivering it present, taken by the CEO."
Loss of Organisational Learning: "If the same obstacle is reported in two functions in one quarter, then the executive team names the cause and records what it changes in the way the strategy is executed, taken by the CEO."
Erodes Leadership Credibility: "If a strategic priority is announced with no date for its first review, then the date and the evidence to be brought to it are fixed in the same meeting, taken by the CEO."

4. Say how the group completes it.
Say: "Take the four consequences one at a time, each on its own tab. The lesson for each sits above the boxes."

ON THE PORTAL, AFTER THE TEACHING:
Participants work as a group in part 5.1 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.
For each of the four consequences, each group writes a potential gap in the performance of individuals and in the organisational conditions, and a decision point for recovery for each: the decision the executive team takes when the gap appears, and who takes it.""")

prs.save(out)
print('deck written', out, len(prs.slides), 'slides')
