# -*- coding: utf-8 -*-
"""Unit 9 · Strategic Unclogging — content of the amended pages, in two voices (13 October 2026).
Source: the three-way match of 13 October ("Claude outputs\\Unit 9 - Three-way match (findings).md"), Carol's instruction of 13 October 20:21:
"rework the current exercise to fit that [Section 5 as the application for Capstone building from previous units]".
v == 'p': participant page (speaks to "you"); v == 'f': facilitator page (speaks of "participants" / "the group"; preparation only, no entry box).
Teaching text is one shared text on both pages, in the fuller facilitator wording (read from the facilitator page itself)."""
import re
NL = '\r\n'
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'
def esc_ph(s): return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('\n', '&#10;')
def acc(title, meta, body, after='', open_=False):
    return ('<div class="acc%s">' % (' open' if open_ else '') + NL +
            '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">%s</div></div>%s</div>' % (title, meta, ARR) + NL +
            '<div class="acc-b"><div class="cb">' + NL + body + NL + '</div>' + ((NL + after + NL) if after else '') + '</div></div>')
def guide(label, *ps):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>' % label + NL + NL.join(p if p.startswith('<') else '<p>%s</p>' % p for p in ps) + NL + '</div>'
def activity(text, steps=None):
    return ('<div class="fac-note-full u9-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + NL + '<p>%s</p>' % text +
            ((NL + '<ol>' + ''.join('<li>%s</li>' % s for s in steps) + '</ol>') if steps else '') + NL + '</div>')
REF = 'Participants write a reflection in their own file: '
PROMPT = '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">%s</p>'
def reflection(rid, label, question, ph, rows=70):
    return ('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; %s</div>' % label + PROMPT % question +
            '<textarea class="ref-ta reflection-textarea" id="%s" style="min-height:%dpx;" placeholder="%s"></textarea>' % (rid, rows, esc_ph(ph)) +
            '<div class="ref-saved reflection-saved" id="%s-saved"></div><button class="ref-save" onclick="saveTA(this)">Save Reflection</button></div>' % rid)
def hero(label, title, lead):
    return '<div class="mod-hero"><div class="mod-hero-label">%s</div><h2>%s</h2><p>%s</p></div>' % (label, title, lead)
def slo(a, b):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>%s</li><li>%s</li></ul></div>' % (a, b)
def ul(items): return '<ul>' + NL + NL.join('<li>%s</li>' % x for x in items) + NL + '</ul>'
def strip_fac(body):
    """Remove facilitator-only boxes from a shared teaching body."""
    return re.sub(r'\r\n?<div class="fac-note-full"[^>]*>.*?\r?\n?</div>(?=\r\n|$)', '', body, flags=re.S)

# ═══ Wording fixes on the shared teaching text (both pages) ═══════════════════════════════════════════
FIXES = [
    ('Designing a brilliant strategy is only the start. ', 'Designing the strategy starts the work. '),
    (' Energy is high; progress is not.', ' Energy is high and progress stalls.'),
    (' Activity is high; advancement is not.', ' Activity is high and advancement stalls.'),
    ('flagging a problem is no longer seen as a failure or a critique of a colleague. It is treated as valuable data.', 'flagging a problem is treated as valuable data.'),
    ('The Strategic Unclogging activation is triggered when a KR/KPI shows signs of execution risk.',
     'The Strategic Unclogging activation is triggered when a Key Result (KR) or key performance indicator (KPI) shows signs of execution risk.'),
    ('intervention required within 5 working days.', 'intervention required before the next review.'),
    ('Identifying a clog is only half the work. The real discipline is lever selection.', 'Identifying a clog starts the work. Lever selection completes it.'),
    ('This is a fundamentally different diagnostic posture that moves leadership from blame to engineering.', 'This diagnostic posture moves leadership from blame to engineering.'),
    ('You stop just managing a plan and start engineering flow.', 'You start engineering flow.'),
    (' &mdash; or ', ', or '),
    (' — or ', ', or '),
]
def fix(s):
    for a, b in FIXES: s = s.replace(a, b)
    return s

# ═══ Unit header ═══════════════════════════════════════════════════════════════════════════════════════
DESC_OLD = {'p': 'This unit equips you to diagnose the blockages preventing strategic intent from flowing into execution &mdash; and to intervene with precision.</p>'}
DESC_NEW = 'This unit equips you to diagnose the blockages preventing strategic intent from flowing into real-world execution &mdash; and to intervene with precision using the 7 Strategic Unclogging Levers.</p>'

# ═══ Facilitator Guide tab ═════════════════════════════════════════════════════════════════════════════
GUIDE_EDITS = [
    ('<p>The Clog Clinic in Application is the centrepiece &mdash; protect the full 45 minutes. It must use real stalled KPIs. The quality of the diagnostic conversation is the measure of this unit.</p>',
     '<p>The Clog Clinic in Application is the centrepiece: each group diagnoses the friction on its own Key Results and builds its Enterprise Unclogging Agenda. The diagnostic triads of part 4.4 prepare it, on each participant&rsquo;s own stalled KPI. The quality of the diagnostic conversation is the measure of this unit.</p>'),
    ('<p><strong>Watch for:</strong> the relief response. When leaders first encounter the clog map, they often feel relieved &mdash; they recognise their organisations immediately. The facilitation risk is that the conversation stays at the level of recognition and stalls before diagnosis and intervention. Push past identification: <em>&ldquo;Recognising it is the start. Now name it precisely and select the lever.&rdquo;</em></p>',
     '<p><strong>Teach past recognition.</strong> When leaders first encounter the clog map, they often feel relieved: they recognise their organisations immediately. Take them from recognition to diagnosis and intervention: <em>&ldquo;Recognising it is the start. Now name it precisely and select the lever.&rdquo;</em></p>'),
    ('<p><strong>Watch for:</strong> Cultural Resistance overuse. It is the most comfortable diagnosis because it externalises the problem. Challenge it every time: <em>&ldquo;Is this a culture issue, or is it the downstream consequence of Leadership Avoidance?&rdquo;</em></p>',
     '<p><strong>Teach the test for Cultural Resistance.</strong> It is the most comfortable diagnosis because it externalises the problem. Teach the question that tests it: <em>&ldquo;Is this a culture issue, or is it the downstream consequence of Leadership Avoidance?&rdquo;</em></p>'),
    ('<p><strong>Watch for:</strong> lever vagueness. &ldquo;We need to improve communication&rdquo; is too vague to act on. A lever is a structural adjustment &mdash; a redesigned decision right, a reset KPI, a rebuilt process, a named accountability. Push every group until their intervention is concrete enough to own.</p>',
     '<p><strong>Teach what a lever is.</strong> &ldquo;We need to improve communication&rdquo; is too vague to act on. A lever is a structural adjustment: a redesigned decision right, a reset KPI, a rebuilt process, a named accountability.</p>'),
    ('Was the plan wrong &mdash; or was something in the system blocking its flow?', 'Was the plan wrong, or was something in the system blocking its flow?'),
    ('If Cultural Resistance is your diagnosis &mdash; is that genuinely a culture problem, or is it a Leadership Avoidance problem that has produced cultural symptoms?',
     'If Cultural Resistance is your diagnosis, is that a culture problem, or a Leadership Avoidance problem that has produced cultural symptoms?'),
]
GUIDE_DROP = ['<p><strong>Timing:</strong> Awareness and Intelligence can move at pace.']

# ═══ Section texts ═════════════════════════════════════════════════════════════════════════════════════
LEAD = {
    1: 'Naming the internal blockages that prevent strategic intent from flowing into execution &mdash; and introducing the 7-clog diagnostic map aligned to ABCV Directional Integrity.',
    2: 'Understanding why execution friction is the inevitable consequence of system misalignment &mdash; and introducing the 7 Strategic Unclogging Levers as the leadership toolkit for restoring execution flow.',
    3: 'Using COMPASS, the seven-zone map of the enterprise execution architecture, as the primary diagnostic instrument to locate where execution friction is accumulating &mdash; and applying the 4-step Strategic Unclogging activation process.',
    4: 'Building the collective discipline of normalising the unclog &mdash; where detecting and clearing execution friction becomes a shared leadership habit.',
}
SLO = {
    1: ('Recognise the systemic blockages that widen the gap between strategic intent and execution.', 'Identify the observable symptoms of friction in execution.'),
    2: ('Resolve the strategy clogs in the people and organisational performance to foster high performance.', 'Recognise the leadership disciplines that detect and resolve friction early.'),
    3: ('Evaluate where interdependent conditions are causing friction to accumulate across the enterprise.', 'Distinguish visible symptoms from their underlying organisational causes.'),
    4: ('Mobilise leaders across functions to restore execution momentum together.', 'Establish a shared leadership rhythm for surfacing and resolving friction.'),
    5: ('Diagnose the root cause of a stalled priority in their current portfolio.', 'Determine a targeted response with a named owner, action and completion date.'),
}
GUIDE_S = {  # facilitator guidance box per section: (label, [(old, new) edits])
    1: [('Work through the clog map deliberately. Do not rush. Each clog', 'Work through the clog map deliberately. Each clog')],
    2: [('Spend time on the pressure point examples &mdash; they make the abstract concrete.', 'Use the pressure point examples: they make the abstract concrete.')],
    3: [('<p>For the 4-step activation: this is the procedural backbone that connects directly to the Excel Unclogging Tool participants have. Walk it as a live demonstration with one stalled KPI from the group before moving to Application.</p>',
         '<p>For the 4-step activation: this is the procedural backbone of the diagnosis. Walk the four steps as a live demonstration with one stalled KPI before moving to Integration.</p>')],
    4: [('<p>Close this zone by having each CXO name one clog they suspect is forming outside their function &mdash; and the COMPASS zone where they believe it is accumulating. This is the seed of the Enterprise Unclogging Agenda.</p>',
         '<p>Close part 4.2 by having each executive (CXO) name one clog they suspect is forming outside their function, and the COMPASS zone where they believe it is accumulating. This is the seed of the Enterprise Unclogging Agenda.</p>' + NL +
         '<p>Part 4.4 closes the section: the diagnostic triads practise the four diagnostic questions on each participant&rsquo;s own stalled Key Result or KPI. This prepares the Clog Clinic each group runs on its own Key Results in Section 5.</p>')],
}
OPEN_11 = {'p': '<p>At this point, your strategy is clear. Your objectives are defined. Your performance expectations are in motion. Then the gears begin grinding.</p>',
           'f': '<p>At this point, the strategy is clear. Objectives are defined. Performance expectations are in motion. Then the gears begin grinding.</p>'}
PROMPT_12_OLD = '<p>Ask the group: <em>&ldquo;Which of these three signals is most visible in your organisation right now? Raise your hand for the one you recognise most immediately.&rdquo;</em> Use the show of hands to calibrate which clog category to explore first in the map below.</p>'
PROMPT_12_NEW = '<p>Ask the group: <em>&ldquo;Which of these three signals is most visible in your organisation right now?&rdquo;</em> Participants post in the chat the signal they recognise most immediately. Use the replies to choose which clog category to explore first in the map below.</p>'
EX_42_OLD = '<p>Ask each CXO to complete the following statement silently, then share in the group:</p>'
EX_42_NEW = '<p>Ask each executive (CXO) to complete the following statement on their own, then post it in the chat:</p>'
AGENDA_43 = '<p>Integration closes with each executive (CXO) contributing to a shared <strong>Enterprise Unclogging Agenda</strong>: the collective view of where clogs are forming, their severity, and the levers required. The agenda gives the leadership team a structured, visible, collectively owned priority list.</p>'
AGENDA_43_P = '<p>Your group builds its Enterprise Unclogging Agenda in Step 5 of Section 5.</p>'
AGENDA_43_F_GUIDE = 'Teach the agenda as the portfolio view of every active clog: its category, COMPASS zone, severity, lever and owner. Each group builds its own agenda in Step 5 of Section 5.'

# Participant reflections
Q = {
    'ref1': ('Strategic Clog in Your Organisation', 'Think of a strategy initiative that stalled in your organisation. Was the plan wrong, or was something in the system blocking its flow? What was the blockage? Could it have been named earlier?', 'The initiative:\nThe blockage:\nCould it have been named earlier?'),
    'ref3': ('Where Is Your System Not Yet Ready?', 'Given your current strategic direction, which element of your operating system is most likely to create friction (structure, decision rights, culture, metrics, capability or technology)? Why is this predictable given your strategy?', 'The element:\nWhy it is predictable:'),
    'ref4': ('Your Lever', 'For the clog you identified in Awareness: which primary lever would you pull, which second lever would you combine it with, and why this combination?', 'Primary lever:\nSecond lever:\nWhy this combination:'),
}
ACT = {  # facilitator PARTICIPANT ACTIVITY notes
    '1.1': REF + 'a strategy initiative that stalled in their organisation, the blockage behind it, and whether it could have been named earlier.',
    '1.3': REF + 'a rating of each of the seven clogs in their current strategy portfolio, from 1 (absent) to 5 (active), and the clog they will bring to the diagnostic triads in part 4.4.',
    '2.1': REF + 'the element of their operating system most likely to create friction under their current strategic direction, and why.',
    '2.3': REF + 'the primary lever and the second lever they would pull for the clog they identified in Awareness, and why this combination.',
    '4.2': REF + 'a clog they suspect is forming outside their function: its category, COMPASS zone and signal, why they have not raised it, and the consequence of not raising it.',
    '4.4': 'Participants practise in breakout rooms of three, then record in their own file, as Portfolio work: their stalled Key Result or KPI and its progress against target, the COMPASS zone, the signal, the clog, the visible symptom and its cause, and the lever with its first action.',
}

# ═══ Part 4.4 · Diagnostic Triads (moved from Section 5, class practice and Portfolio work) ═══════════
T44, M44 = '4.4 &mdash; Diagnostic Triads', 'Practise the four questions &middot; Portfolio Work'
HOW44 = {
    'p': ['Prepare one Key Result or KPI from your own work that is below target or stalled and has stayed unresolved across more than two review cycles. Remove identifying and confidential details. Type it into the first box below.',
          'Your facilitator places you in a breakout room of three. Each of you takes one role: Diagnostician, Challenger or Observer. The roles rotate after each round so every member runs the diagnostic once.',
          'The Diagnostician reasons aloud through the four questions, in sequence, without skipping. The Challenger draws the diagnosis out. The Observer evaluates the conversation against the four observer criteria and gives feedback after the round.',
          'Your triad nominates one diagnosis and posts it in the chat in the sentence below. The full group challenges it.',
          'Record your own diagnosis and your lever in the boxes below. Your entries save as you type and become part of your Learning Portfolio.'],
    'f': ['Each participant prepares one Key Result or KPI from their own work that is below target or stalled and has stayed unresolved across more than two review cycles, with identifying and confidential details removed.',
          'The facilitator opens breakout rooms of three. Each member takes one role: Diagnostician, Challenger or Observer. The roles rotate after each round so every member runs the diagnostic once.',
          'The Diagnostician reasons aloud through the four questions, in sequence, without skipping. The Challenger draws the diagnosis out. The Observer evaluates the conversation against the four observer criteria and gives feedback after the round.',
          'Each triad nominates one diagnosis and posts it in the chat in the sentence below. The full group challenges it.',
          'Each participant records their own diagnosis and lever in their own file, as Portfolio work.'],
}
ROLES = [('Diagnostician', 'Presents the stalled Key Result or KPI. Reasons aloud through the four questions. Must not skip Q3: the clog must be named before the lever is selected.'),
         ('Challenger', 'Guides through the four questions in sequence. Challenges comfortable answers with: <em>&ldquo;Are you sure that&rsquo;s the root, or is that the symptom of something deeper?&rdquo;</em> Does not give the diagnosis: draws it out.'),
         ('Observer', 'Listens and evaluates the conversation against the four observer criteria. Provides structured feedback after the round.')]
QUESTIONS = [('Q1 &mdash; Where is the friction?', '&ldquo;Which COMPASS zone best describes where the pain is showing up: Clarity of Direction, Organisational Alignment, Management Discipline, People &amp; Capability, Allocation of Resources, Systems &amp; Execution, or Sensing &amp; Adaptation?&rdquo;'),
             ('Q2 &mdash; What is the signal?', '&ldquo;Of the signals in that zone, which one most precisely describes what you are observing?&rdquo;'),
             ('Q3 &mdash; What is the clog?', '&ldquo;Based on that signal, what type of blockage is at the root? Structure, capability, decision, metrics, culture, technology, or leadership?&rdquo; The Challenger challenges: <em>&ldquo;Are you sure that&rsquo;s the root, or is that the symptom of something deeper?&rdquo;</em>'),
             ('Q4 &mdash; What lever would you pull?', '&ldquo;Given that diagnosis, what is the first action you would take? A specific action, with an owner and a date.&rdquo;')]
CRITERIA = [('Criterion 01 &mdash; The Diagnostician Reasoned Through It', 'Did the Diagnostician go straight to the comfortable answer, or genuinely reason through the diagnostic sequence? A good diagnostic conversation shows visible thinking.'),
            ('Criterion 02 &mdash; The Clog Was Distinguished from the Symptom', 'Was the clog correctly separated from what was initially observed? The symptom is what leadership sees first (e.g. slow delivery). The clog is the root cause (e.g. decision bottleneck). These must remain distinct.'),
            ('Criterion 03 &mdash; The Challenger Used Curiosity', 'Did the Challenger draw out the diagnosis through questions, or push the Diagnostician toward a conclusion? A good challenger maintains diagnostic curiosity throughout and challenges without prescribing.'),
            ('Criterion 04 &mdash; The Intervention Was Concrete', 'Did the conversation end with a specific, time-bound action that both parties understood and accepted? &ldquo;We&rsquo;ll improve communication&rdquo; is too vague to act on. A lever is a structural change with a named owner and a date.')]
CHALLENGE_SENTENCE = '&ldquo;Our KR was [X]. The friction zone was [Y]. The signal was [Z]. We diagnosed [clog]. Our proposed lever is [action], owned by [person], by [date].&rdquo;'
CHALLENGE_QS = ['Is the COMPASS zone correctly identified?', 'Is the clog category the root cause or just a surface symptom?', 'Is the lever precise enough, or is it still general pressure?']
CLOSE_Q = '&ldquo;What would have to be true for that lever to actually clear the clog?&rdquo;'
GUIDE_44 = [
    'Each participant brings one stalled Key Result or KPI from their own work, below target and unresolved across more than two review cycles, with identifying and confidential details removed. Hypothetical clogs produce hypothetical insights.',
    'Open breakout rooms of three. Roles rotate after each round so every participant runs the diagnostic once. Bring the rooms back for the Collective Intelligence Challenge: each triad posts its nominated diagnosis in the chat, and the group challenges it. Close each challenge with: <em>&ldquo;What would have to be true for that lever to actually clear the clog?&rdquo;</em>',
    '<strong>Watch for the symptom-to-lever skip.</strong> The most common failure is jumping from observable symptom directly to lever selection without naming the clog. A lever applied to the wrong clog will not clear it, and may make the underlying problem worse. If this happens, pause and redirect: <em>&ldquo;Wait. Before we select the lever, have we correctly classified the clog? Let&rsquo;s go back to Q3.&rdquo;</em>',
    '<strong>Watch for Cultural Resistance overuse.</strong> It is the most comfortable diagnosis because it externalises the problem. Challenge it: <em>&ldquo;Is this a culture issue, or a Leadership Avoidance clog that has produced cultural symptoms?&rdquo;</em>',
    '<strong>Watch for vague levers.</strong> &ldquo;We&rsquo;ll improve communication&rdquo; is too vague to act on. A lever is a structural change: a redesigned decision right, a reset KPI, a rebuilt process, a named accountability.',
]
ZONES = ['Clarity of Direction (C)', 'Organisational Alignment (O)', 'Management Discipline (M)', 'People & Capability (P)', 'Allocation of Resources (A)', 'Systems & Execution (S1)', 'Sensing & Adaptation (S2)']
CLOGS = ['Structural Misfit', 'Capability Gaps', 'Decision Bottlenecks', 'Misaligned Metrics & Incentives', 'Cultural Resistance', 'Technology / Infrastructure Lag', 'Leadership Avoidance']
LEVERS = ['Standardise', 'Streamline', 'Clarify', 'Upgrade', 'Reinforce', 'Realign', 'Rebuild Trust']
SIGNALS = ['Decision Paralysis', 'Kinetic Misalignment', 'Output–Outcome Gap']
SEV = ['Low', 'Medium', 'High']
# Portfolio artefacts of 4.4 (field-group keys; each saves as "Label: value" lines)
PF = [
    ('tc_prep', 'Portfolio Artefact &mdash; My Stalled Key Result or KPI', [('My stalled Key Result or KPI', None), ('Current progress against target', None), ('What I observe happening', None)]),
    ('tc_diag', 'Portfolio Artefact &mdash; My Diagnosis', [('COMPASS zone (Q1)', ZONES), ('The signal (Q2)', None), ('The clog (Q3)', CLOGS), ('The visible symptom', None), ('The cause beneath it', None)]),
    ('tc_lever', 'Portfolio Artefact &mdash; My Lever', [('Primary lever (Q4)', LEVERS), ('Second lever, if any', LEVERS), ('Why the lever fits the cause', None), ('First action, with owner and date', None)]),
]

# ═══ Section 5 · The Clog Clinic (group work, Capstone work) ═══════════════════════════════════════════
S5_TITLE = 'The Clog Clinic'
S5_LEAD = {'p': 'Your group runs the Clog Clinic on the two Key Results it established in Unit 7, for the strategy in your team&rsquo;s Capstone Blueprint.',
           'f': 'Each group runs the Clog Clinic on the two Key Results it established in Unit 7, for the strategy in its team&rsquo;s Capstone Blueprint.'}
T51, M51 = '5.1 &mdash; The Clog Clinic on Your Two Key Results', 'Capstone Work'
T51F = '5.1 &mdash; The Clog Clinic on the Group&rsquo;s Two Key Results'
STEPS = [  # key, name, Capstone name, confirm key, record heading, Capstone box
    ('s1', 'Friction Signals', 'Unclogging · Friction Signals', 'uc_signals', 'Step 1 · Friction Signals', '9A'),
    ('s2', 'Clog Diagnosis', 'Unclogging · Clog Diagnosis', 'uc_diagnosis', 'Step 2 · Clog Diagnosis', '9B'),
    ('s3', 'Unclogging Levers', 'Unclogging · Unclogging Levers', 'uc_levers', 'Step 3 · Unclogging Levers', '9C'),
    ('s4', 'Unclogging Rhythm', 'Unclogging · Unclogging Rhythm', 'uc_rhythm', 'Step 4 · Unclogging Rhythm', '9D'),
    ('s5', 'Unclogging Agenda', 'Unclogging · Unclogging Agenda', 'uc_agenda', 'Step 5 · Unclogging Agenda', '9E'),
]
PARTS = [[s[0], s[1], s[2], s[3], s[4]] for s in STEPS]
def fields():
    """[id, label, part, optional, type ('t' text | 's' select), placeholder or options]"""
    F = []
    for n in (1, 2):
        F += [['k%d_signal' % n, 'Key Result %d · The friction signal' % n, 's1', False, 's', SIGNALS],
              ['k%d_observe' % n, 'Key Result %d · What your group observes' % n, 's1', False, 't', 'What your executive team sees happening on this Key Result...'],
              ['k%d_warn' % n, 'Key Result %d · The COMPASS warning signals present' % n, 's1', False, 't', 'The warning signals from part 3.1 that are present...']]
    for n in (1, 2):
        F += [['k%d_zone' % n, 'Key Result %d · COMPASS zone (Q1)' % n, 's2', False, 's', ZONES],
              ['k%d_zsig' % n, 'Key Result %d · The signal (Q2)' % n, 's2', False, 't', 'The signal in that zone that most precisely describes what you observe...'],
              ['k%d_clog' % n, 'Key Result %d · The clog (Q3)' % n, 's2', False, 's', CLOGS],
              ['k%d_symptom' % n, 'Key Result %d · The visible symptom' % n, 's2', False, 't', 'What leadership sees first...'],
              ['k%d_cause' % n, 'Key Result %d · The cause beneath it' % n, 's2', False, 't', 'The root cause the clog names...']]
    for n in (1, 2):
        F += [['k%d_lever1' % n, 'Key Result %d · Primary lever' % n, 's3', False, 's', LEVERS],
              ['k%d_lever2' % n, 'Key Result %d · Second lever, if any' % n, 's3', True, 's', LEVERS],
              ['k%d_why' % n, 'Key Result %d · Why the lever fits the cause' % n, 's3', False, 't', 'How the lever addresses the cause your group diagnosed...']]
    F += [['r_forum', 'The forum where clogs are raised', 's4', False, 't', 'The executive forum where the shared path runs...'],
          ['r_often', 'How often it meets', 's4', False, 't', 'How often the forum meets, and how it links to your review rhythm...'],
          ['r_who', 'Who raises a clog, including outside their own function', 's4', False, 't', 'Who surfaces friction, and how a leader raises a clog in another function...'],
          ['r_path', 'How the shared path runs in that forum', 's4', False, 't', 'Is there a clog? What category? Which part of the system? Which lever?...']]
    for a, lab, opt in ((1, 'Action 1 · Key Result 1', False), (2, 'Action 2 · Key Result 2', False), (3, 'Action 3 · a further action, if any', True)):
        F += [['a%d_action' % a, '%s · The action' % lab, 's5', opt, 't', 'The unclogging action...'],
              ['a%d_sev' % a, '%s · Severity' % lab, 's5', opt, 's', SEV],
              ['a%d_owner' % a, '%s · Owner' % lab, 's5', opt, 't', 'The named owner...'],
              ['a%d_date' % a, '%s · Completion date' % lab, 's5', opt, 't', 'The completion date...']]
    return F
HOW_S5 = {
    'p': ('This is group work and Capstone work. Your group takes the two Key Results it established in Unit 7, with their owners, through five steps, each on its own tab:', [
        '<strong>Step 1 &middot; Friction Signals.</strong> For each Key Result, your group names the friction signal it observes and the COMPASS warning signals present. The lessons from parts 1.2 and 3.1 sit above the boxes.',
        '<strong>Step 2 &middot; Clog Diagnosis.</strong> For each Key Result, your group answers the first three diagnostic questions: the COMPASS zone, the signal and the clog. Your group separates the visible symptom from the cause beneath it. The lessons from parts 3.2 and 4.4 sit above the boxes.',
        '<strong>Step 3 &middot; Unclogging Levers.</strong> For each clog, your group selects the primary lever, any second lever, and states why the lever fits the cause. The lessons from parts 2.2 and 2.3 sit above the boxes.',
        '<strong>Step 4 &middot; Unclogging Rhythm.</strong> Your group sets the leadership rhythm through which your executive team surfaces and resolves friction. Your Unit 8 decision points and the lessons from parts 4.1 and 4.2 sit above the boxes.',
        '<strong>Step 5 &middot; Unclogging Agenda.</strong> Your group lists each unclogging action with its severity, named owner and completion date. The lessons from parts 3.2 and 4.3 sit above the boxes.'],
        ['Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
         'You then read your group&rsquo;s record at the foot of this section and select Confirm. Your confirmed record feeds your team&rsquo;s Capstone Blueprint.']),
    'f': ('This is group work and Capstone work. Each group takes the two Key Results it established in Unit 7, with their owners, through five steps, each on its own tab:', [
        '<strong>Step 1 &middot; Friction Signals.</strong> For each Key Result, the group names the friction signal it observes and the COMPASS warning signals present. The lessons from parts 1.2 and 3.1 sit above the boxes.',
        '<strong>Step 2 &middot; Clog Diagnosis.</strong> For each Key Result, the group answers the first three diagnostic questions: the COMPASS zone, the signal and the clog. The group separates the visible symptom from the cause beneath it. The lessons from parts 3.2 and 4.4 sit above the boxes.',
        '<strong>Step 3 &middot; Unclogging Levers.</strong> For each clog, the group selects the primary lever, any second lever, and states why the lever fits the cause. The lessons from parts 2.2 and 2.3 sit above the boxes.',
        '<strong>Step 4 &middot; Unclogging Rhythm.</strong> The group sets the leadership rhythm through which its executive team surfaces and resolves friction. The group&rsquo;s Unit 8 decision points and the lessons from parts 4.1 and 4.2 sit above the boxes.',
        '<strong>Step 5 &middot; Unclogging Agenda.</strong> The group lists each unclogging action with its severity, named owner and completion date. The lessons from parts 3.2 and 4.3 sit above the boxes.'],
        ['The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
         'Each member then reads the group&rsquo;s record at the foot of the section and selects Confirm. The confirmed record feeds the team&rsquo;s Capstone Blueprint.']),
}
HOW_STEP = [
    ['Read your group&rsquo;s two Key Results above and the lesson for this step.',
     'For each Key Result, select the friction signal that shows first and write what your group observes.',
     'Name the COMPASS warning signals present for each Key Result.'],
    ['For each Key Result, answer Q1 to Q3: the COMPASS zone where the friction shows, the signal in that zone, and the clog.',
     'Separate the visible symptom from the cause beneath it. Name the clog before you move to the lever.'],
    ['For each Key Result, select the primary lever for the clog your group diagnosed in Step 2.',
     'Add a second lever where one fix will not clear the clog.',
     'Write why the lever fits the cause.'],
    ['Read your group&rsquo;s Unit 8 decision points and the lessons for this step.',
     'Name the forum where your executive team raises clogs and how often it meets.',
     'State who raises a clog, including a clog outside a leader&rsquo;s own function, and how the shared path runs in that forum.'],
    ['Write one unclogging action for each Key Result, and a third action where your diagnosis calls for one.',
     'Rate the severity of each action, and name its owner and completion date.'],
]
LESSON = [
    [('From part 1.2 &middot; Three Observable Friction Signals', '<strong>Decision Paralysis:</strong> choices that should be instinctive begin taking longer than expected, creating a bottleneck at the top. <strong>Kinetic Misalignment:</strong> teams move with intensity but pull in different directions, cancelling each other&rsquo;s efforts. <strong>Output&ndash;Outcome Gap:</strong> tasks are completed and boxes are checked, but the needle on actual strategic goals isn&rsquo;t moving.'),
     ('From part 3.1 &middot; The 7 COMPASS High-Flammability Zones', 'C Clarity of Direction &middot; O Organisational Alignment &middot; M Management Discipline &middot; P People &amp; Capability &middot; A Allocation of Resources &middot; S1 Systems &amp; Execution &middot; S2 Sensing &amp; Adaptation. When a zone heats up, its warning signals appear: for example, strategy described differently by each leader (C), KPIs that conflict across functions (O), leaders who tolerate repeated misses (M).')],
    [('From part 3.2 &middot; Steps 1 and 2', 'Select the type of friction first: structure, capability, decision, metrics, culture, technology or leadership. An incorrectly classified clog will attract an incorrectly selected lever. Then locate the COMPASS zone where the clog is forming: the combination of clog category and COMPASS zone provides diagnostic precision.'),
     ('From part 4.4 &middot; Observer criterion 02', 'The symptom is what leadership sees first (e.g. slow delivery). The clog is the root cause (e.g. decision bottleneck). These must remain distinct.')],
    [('From part 2.3 &middot; The 7 Strategic Unclogging Levers', 'Standardise (ensure consistency) &middot; Streamline (increase speed) &middot; Clarify (eliminate confusion) &middot; Upgrade (remove bottlenecks) &middot; Reinforce (strengthen behaviour) &middot; Realign (focus on results) &middot; Rebuild Trust (restore credibility).'),
     ('From part 2.2 &middot; Targeted Intervention', 'Targeted intervention means matching the lever to the root cause. Rarely does a single clog require just one fix: a Capability Gap may require both Upgrade (systems) and Reinforce (skills); a Leadership Avoidance clog may require both Clarify (decision rights) and Rebuild Trust (credibility restoration).')],
    [('From part 4.1 &middot; The shared path', 'Is there a clog? What category does it fall into? Which part of the system is it affecting? Which lever do we pull to fix it?'),
     ('From part 4.2 &middot; See Something, Say Something', 'Blockages rarely stay in one lane. If any leader sees friction forming, including outside their own area of execution, they are encouraged to surface it. Surfacing a blockage early is an act of leadership.')],
    [('From part 3.2 &middot; Step 4 &middot; Rate Severity', '<strong>Low:</strong> early signal present; limited impact on momentum; monitor and pre-empt. <strong>Medium:</strong> clear friction affecting progress; intervention required before the next review. <strong>High:</strong> significant execution risk; immediate action required; escalate to the leadership team.'),
     ('From part 4.3 &middot; Enterprise Unclogging Agenda', 'A portfolio view of all active clogs, their categories, COMPASS zones and severity ratings, constitutes the Enterprise Unclogging Agenda: a structured, visible, collectively owned priority list.')],
]
COMPLETES_F = [
    ['for each Key Result: the friction signal, what the group observes, and the COMPASS warning signals present'],
    ['for each Key Result: the COMPASS zone (Q1), the signal (Q2) and the clog (Q3)', 'the visible symptom and the cause beneath it'],
    ['for each clog: the primary lever and any second lever', 'why the lever fits the cause'],
    ['the forum where clogs are raised and how often it meets', 'who raises a clog, including outside their own function', 'how the shared path runs in that forum'],
    ['one unclogging action for each Key Result, and a third where the diagnosis calls for one', 'for each action: the severity, the owner and the completion date'],
]
GUIDE_S5_F = [
    'Section 5 is group work and Capstone work. Each group runs the Clog Clinic on the two Key Results it established in Unit 7. The diagnostic triads of part 4.4 practised the four questions; here the group applies them to its own strategy.',
    'Order: Steps 1 to 3 take the two Key Results one at a time. Step 4 sets the rhythm, with the group&rsquo;s Unit 8 decision points beside it. Step 5 brings every action into one agenda. Each group confirms its Unit 7 record before it starts, so its two Key Results show on the page.',
]
ACT_S5_F = 'Participants work as a group in part 5.1 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'

# ═══ Unit Summary ══════════════════════════════════════════════════════════════════════════════════════
SUM_P = [
    ('Awareness — What', 'What Was Established', 'You saw that a Strategic Clog is an internal blockage that prevents strategic intent from flowing into execution. The 7-clog diagnostic map gives you the vocabulary to name friction precisely, aligned to ABCV Directional Integrity, and to look beneath surface symptoms.'),
    ('Intelligence — Why', 'Why It Matters', 'You saw that clogs are design signals. Where strategy stretches the operating system beyond its current capacity, friction appears predictably. The 7 levers restore the structural, behavioural and operational conditions that allow strategy to flow at the intended speed.'),
    ('Extrapolating — Where', 'Where Clogs Concentrate', 'You saw that COMPASS provides the coordinate system for locating clogs within the enterprise execution architecture. The combination of clog category and COMPASS zone delivers diagnostic precision. The 4-step activation translates diagnosis into targeted intervention.'),
    ('Integration — Collective', 'What Was Built', 'You saw that clogs rarely stay in one lane. The leadership team, acting as the collective intelligence for execution discipline, owns the diagnostic conversation collectively: surfacing friction early is an act of leadership stewardship, and the Enterprise Unclogging Agenda becomes the shared instrument of execution restoration. In the diagnostic triads you practised the four questions on a stalled Key Result or KPI of your own.'),
    ('Application — In Practice', 'What You Applied', 'Your group ran the Clog Clinic on the two Key Results it established in Unit 7. You named the friction signals, diagnosed the clogs, selected the levers, set the unclogging rhythm and built your Enterprise Unclogging Agenda.'),
]
SUM_F_5 = ('Application — In Practice', 'Each group ran the Clog Clinic on its two Unit 7 Key Results: the friction signals, the clog diagnosis, the levers, the unclogging rhythm and the Enterprise Unclogging Agenda. The confirmed record feeds the team&rsquo;s Capstone Blueprint.')
CLOSE_F_ADD = ' Remind participants that the group&rsquo;s confirmed Section 5 record feeds the team&rsquo;s Capstone Blueprint.'
