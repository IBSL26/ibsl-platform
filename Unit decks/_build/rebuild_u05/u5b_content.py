# -*- coding: utf-8 -*-
"""Unit 5 amendments of 8 October 2026 (evening), on Carol's word. Shared content for amend_p.py and amend_f.py.
Principle 1: her text, word for word. OCEAVL: her assessment (oceavl.json). Alignment Toolkit: cues and triggers drawn from parts 1.3.1 to 1.3.4;
the ACE-IT cues and the 3S / STAT / ACE-IT triggers are new wording (marked NEW) for her review."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OCEAVL = json.load(open(os.path.join(HERE, 'oceavl.json'), encoding='utf-8'))

# ── 1.2 · Principle 1 (Carol, 8 October, word for word) ────────────────────────────────────────────
CHAIN = [
    ('Interpretation', 'People first make sense of the strategy. They interpret what it means, what matters, what has changed, what is expected, and what risks or opportunities they see. This is where assumptions, mental models, expertise, past experience and bias shape the meaning people attach to the strategy.'),
    ('Experience', 'People then experience the strategy emotionally. They may feel energised, uncertain, threatened, excluded, hopeful, tired or resistant. This emotional state affects trust, morale, psychological safety, engagement energy and the willingness to participate honestly in execution.'),
    ('Choices', 'People then make choices and trade-offs. They decide what to prioritise, what to resource, what to protect, what to stop, what to challenge and what to support. This is where strategy becomes real through judgement, commitment, accountability and allocation of attention.'),
    ('Actions', 'People finally act in ways that either carry the strategy forward or weaken it. Behaviour shows up in follow-through, handovers, routines, conversations, ownership, discipline and how people respond when execution becomes difficult.'),
    ('Results', 'Results emerge when thinking is clear, feeling is aligned, decisions are coherent, and behaviour is disciplined. When any part of the chain is weak, execution begins to leak.'),
]
CHAIN_QUOTE = '“Strategy does not jump from intention to outcome. It moves through people. It is interpreted through thinking, experienced through feeling, converted through deciding, and delivered through behaving.”'

def principle1_chain():
    """The five links and the closing line. They take the place of the two older paragraphs; the lead line and the insight line stay."""
    rows = ''.join('          <div class="u5-link"><div class="u5-link-n">%d</div><div class="u5-link-t"><div class="u5-link-h">%s</div><p>%s</p></div></div>\n' % (i + 1, h, t)
                   for i, (h, t) in enumerate(CHAIN))
    return '        <div class="u5-chain">\n' + rows + '        </div>\n        <div class="u5-quote">' + CHAIN_QUOTE + '</div>\n'

# ── 3.1 · The OCEAVL Assessment ────────────────────────────────────────────────────────────────────
T31 = 'The OCEAVL Assessment: Personal and Team Behavioural Profile'
T31_META = 'Seven Dimensions'
OC_NAME = 'OCEAVL · My Scores'
# Carol, 8 October: "The OCEAVL is a personal assessment. So each person completes the assessment. Then the system gives them the team
# score after they all submit to their capstone." No member says a score aloud or types another member's score.

def oceavl_teach(page):
    p = page == 'p'
    s = ('  <p>Principle 3 established that alignment must be designed. The OCEAVL Assessment is where the design starts. It surfaces the psychological tendencies that influence executive decision-making, across seven dimensions.</p>\n'
         '  <p>The assessment maps the behavioural dispositions that shape how a leader interprets strategy, manages disagreement and responds under pressure. ' +
         ('It is a personal assessment: you complete it for yourself, on your own page. The portal then reads the scores of your whole team together.' if p else
          'It is a personal assessment: each participant completes it alone, on their own page. The portal then reads the scores of the whole team together.') + '</p>\n'
         '  <h4>How the profile is read</h4>\n  <ol>\n'
         '    <li>' + ('You score yourself' if p else 'Each participant scores themselves') + ' from 1 to 5 on each dimension: 1 is strongly low, 3 is balanced and 5 is strongly high.</li>\n'
         '    <li>A score of 4 or 5 is High, 3 is Balanced, and 1 or 2 is Low. This gives ' + ('your own level' if p else 'the participant’s own level') + ' on each dimension.</li>\n'
         '    <li>The level held by most members of a team is the team’s level for that dimension. The team’s profile appears in the team’s Capstone Blueprint once every member has submitted.</li>\n'
         '    <li>Each level carries a risk, a response and three routines that hold the response in place.</li>\n  </ol>\n'
         '  <p>Every level carries a risk. A High level is a disposition to manage, as Low and Balanced are.</p>\n'
         '  <h4>The seven dimensions · expand each</h4>\n')
    for d in OCEAVL:
        s += '  <details class="u5-dim"><summary><span class="u5-dim-n">%s</span><span class="u5-dim-d">%s</span></summary>\n' % (d['name'], d['desc'])
        for lv in d['levels']:
            s += ('    <div class="u5-lv"><div class="u5-lv-h">%s</div><p class="u5-lv-dna">%s</p><div class="u5-lv-g">'
                  '<div><b>Risk</b>%s</div><div><b>Response</b>%s</div><div><b>Routines</b>%s</div></div></div>\n') % (
                      lv['level'], lv['dna'], lv['risk'], lv['resp'], lv['rout'])
        s += '  </details>\n'
    return s

OC_HOW = ['Score yourself from 1 to 5 on each of the seven dimensions. Work alone. Your scores are your own.',
          'Read your own profile: your level on each dimension, with its risk, its response and its routines.',
          'Select Submit to My Team’s Capstone. Your scores join your team’s profile.',
          'Your team’s profile appears in your team’s Capstone Blueprint once every member has submitted.']
OC_CLOSE = 'Your team sees the team’s levels only. Your own scores stay on your page and reach your facilitator when you select Submit to Facilitator at the end of the unit.'
REF16_LABEL = 'OCEAVL'
REF16 = 'Which of your own levels carries the highest risk for how you read and lead the strategy? Where has that risk already shown up?'

# ── Section 5 · The Alignment Toolkit ──────────────────────────────────────────────────────────────
CHECKS = [
    {'id': 'mind', 'name': 'Mind', 'tool': '3S', 'line': 'They understand the change, why it matters and what they do differently.'},
    {'id': 'heart', 'name': 'Heart', 'tool': 'SCARF', 'line': 'They want it to succeed.'},
    {'id': 'hands', 'name': 'Hands', 'tool': 'STAT', 'line': 'They are able to do it.'},
    {'id': 'habit', 'name': 'Habit', 'tool': 'ACE-IT', 'line': 'It has become the way they work.'},
]
# id, check, element, cue 1, cue 2, likely trigger. Cues: the "Shows Up As" lines of 1.3.1 to 1.3.3; SCARF triggers: the "Activated By" lines of 1.3.2.
KIT = [
    ('shift', 0, 'Shift', 'People describe the old practice under a new name.', 'Different teams describe different changes.',
     'The change was announced as a direction. No practice, group or date was named.'),                                   # trigger NEW
    ('stake', 0, 'Stake', '“Because head office said so.”', 'People can describe the change and cannot say what it is for.',
     'Only the gain was given, or the reason was an enterprise benefit that never reaches the group’s own work.'),      # trigger NEW
    ('step', 0, 'Step', '“I am waiting to be told.”', 'People agree with the change and carry on as before.',
     'The change has a Shift for the organisation and no Step for each role affected.'),                                   # trigger NEW
    ('status', 1, 'Status', 'Defensive behaviour.', 'Withholding information or cooperation.',
     'New leaders, new KPIs that expose performance, new systems that shift expertise, or changed reporting lines.'),
    ('certainty', 1, 'Certainty', 'Repeated clarification requests.', 'Delay disguised as “waiting for alignment”.',
     'New goals, ambiguous ownership, changing metrics or timelines, or shifting review processes.'),
    ('autonomy', 1, 'Autonomy', 'Passive compliance.', 'Resistance through bureaucracy.',
     'New systems, standardised processes, centralised decision rights, or increased oversight and reporting.'),
    ('relatedness', 1, 'Relatedness', 'Silo behaviour.', 'Guarded communication.',
     'Team restructuring, new leaders or external hires, cross-functional initiatives, or remote and hybrid shifts.'),
    ('fairness', 1, 'Fairness', 'Cynicism.', 'Gossip replacing dialogue.',
     'Uneven workload, selective enforcement of rules, inconsistent rewards, or unclear decision rationale.'),
    ('skill', 2, 'Skill', 'Errors and rework.', 'People revert to the old method “to get it done”.',
     'People were briefed on the new work and have not practised it with feedback.'),                                      # trigger NEW
    ('time', 2, 'Time', 'The new practice is done last.', 'The new practice is dropped on a busy day.',
     'The new work was added to a full day and no old work was taken away.'),                                              # trigger NEW
    ('authority', 2, 'Authority', 'Escalations.', 'People ask permission for what the change asks them to do.',
     'The limit of the new decision has not been stated, or an early decision made under it was overruled.'),              # trigger NEW
    ('tools', 2, 'Tools', 'Spreadsheets beside the system.', 'Requests waiting on another team.',
     'The system, the form or the budget still fits the old way.'),                                                        # trigger NEW
    ('accountability', 3, 'Accountability', 'Reviews end with no named owner.', 'A missed commitment passes without a fix.',
     'No one person owns the practice and its result.'),                                                                   # cues and trigger NEW
    ('commitment', 3, 'Commitment', 'Priorities shift from one review to the next.', 'Non-strategic work is accepted and the new practice gives way.',
     'Pressure rises and the old way is quicker.'),                                                                        # cues and trigger NEW
    ('engagement', 3, 'Engagement', 'Meetings run one way.', 'People cannot quote the shared “why”.',
     'People were told about the change and have no forum to say how it is going.'),                                       # cues and trigger NEW
    ('integrity', 3, 'Integrity', 'Slips are reported late, or softened.', 'Decisions are made before the evidence is cited.',
     'Reporting a slip has carried a cost for the person who reported it.'),                                               # cues and trigger NEW
    ('transparency', 3, 'Transparency', 'Dashboards fall out of date.', 'Decisions reach people without their rationale.',
     'Progress is shared when it is good and held back when it is a setback.'),                                            # cues and trigger NEW
]
KIT_JS = [{'id': k[0], 'c': k[1], 'n': k[2], 'cues': [k[3], k[4]], 'trig': k[5]} for k in KIT]
KIT_NAMES = ['Alignment Plan · ' + c['name'] for c in CHECKS]

T5 = 'The Alignment Toolkit'
STEP_NAMES = ['The Toolkit', 'Your Watch List', 'Team Alignment Plan']
KIT_INTRO = 'The toolkit is read check by check. Each check has its tool, and each element of the tool has two cues and a likely trigger.'
KIT_READ = ['A cue is what you see or hear.',
            'A trigger is the condition that sits behind the cue.',
            'Act on the trigger. A response aimed at the cue leaves the trigger in place.']
# Worked example: the change carried through the unit (resolve complaints at first contact), from the tools of 1.3.1 to 1.3.4.
KIT_EXAMPLE = [
    ('Mind · Step', 'People agree with the change and carry on as before.', 'Back-office specialists, once agents resolve complaints at first contact.',
     'Give the specialists their own Step and ask them to say it back.', 'Chief Operating Officer'),
    ('Heart · Status', 'Withholding information or cooperation.', 'Team leaders, as decisions move from them to their agents.',
     'Involve team leaders in setting the decision limits.', 'Chief Operating Officer'),
    ('Hands · Authority', 'People ask permission for what the change asks them to do.', 'Contact-centre agents, from the first week.',
     'Set the decision limit, state it openly and back the first decisions made under it.', 'Chief Operating Officer'),
    ('Habit · Accountability', 'A missed commitment passes without a fix.', 'Contact-centre agents and their team leaders, after the launch has passed.',
     'Each agent owns the case to closure. Team leaders review first-contact resolution every week.', 'Chief Operating Officer'),
]

def toolkit_step1():
    s = '<p>' + KIT_INTRO + '</p>\n<div class="chg-h">How to read the toolkit</div>\n<ul>' + ''.join('<li>' + x + '</li>' for x in KIT_READ) + '</ul>\n'
    for ci, c in enumerate(CHECKS):
        s += ('<div class="u5-kh"><span class="u5-kh-c">%s · %s</span><span class="u5-kh-l">%s</span></div>\n'
              '<div class="chg-wrap"><table class="chg-table wide u5-kt"><thead><tr><th>Element</th><th>Two cues to look out for</th><th>Likely trigger</th></tr></thead><tbody>\n') % (c['name'], c['tool'], c['line'])
        for k in KIT:
            if k[1] == ci:
                s += '<tr><td>%s</td><td>%s<br>%s</td><td>%s</td></tr>\n' % (k[2], k[3], k[4], k[5])
        s += '</tbody></table></div>\n'
    s += ('<div class="chg-h">Worked example · resolve complaints at first contact</div>\n'
          '<div class="chg-wrap"><table class="chg-table wide u5-kt"><thead><tr><th>Trigger most likely to surface</th><th>Cue to look out for</th><th>Where it will surface</th><th>What we will do</th><th>Leader who owns it</th></tr></thead><tbody>\n')
    for r in KIT_EXAMPLE:
        s += '<tr>' + ''.join('<td>%s</td>' % x for x in r) + '</tr>\n'
    s += '</tbody></table></div>\n'
    return s

ME_HOW = ['Read the practices your strategy starts and stops, shown below. They come from the Start and Stop lists your group confirmed in Unit 3.',
          'Read the cards under each check. Each card is one trigger, with the two cues that show it.',
          'Select “Likely to surface in my area” on the triggers you expect as these changes land. Start with the alignment hot zone of your own role in 4.2. Select at least one under each check.',
          'In the box that opens, write what you will do.']
ME_CLOSE = 'Your watch list saves as you work and becomes part of your Learning Portfolio. It reaches your facilitator when you select Submit to Facilitator at the end of the unit.'
ME_EXAMPLE = ('<strong>Example.</strong> Card: Step. Cue: people agree with the change and carry on as before. Trigger: the change has a Shift for the organisation and no Step for each role affected. '
              'What I will do: “I give each of my team leads their own Step and ask them to say it back.”')
ME_HINT = 'Each card is one trigger. Select “Likely to surface in my area” on the ones you expect. A box opens for what you will do.'
TEAM_HOW = ['Compare the watch lists of your group.',
            'Select “Likely to surface for our strategy” on the triggers your group agrees on, for the strategy in your Capstone Blueprint. Select at least one under each check.',
            'In the boxes that open, write where the trigger will surface, what your team will do and the leader who owns it.',
            'Read your record at the foot of this step, then select Confirm. Select Print for a copy.']
TEAM_HINT = 'Each card is one trigger. Select “Likely to surface for our strategy” on the ones your group agrees on. Three boxes open: where, what your team will do, and the leader who owns it.'
SEC5_HOW_H = 'How Section 5 works'
SEC5_HOW_P = ['<strong>Step 1 · Read.</strong> The toolkit has one table for each check. Each row gives one element, its two cues and its likely trigger.',
              '<strong>Step 2 · On your own.</strong> You select the triggers most likely to surface in your own area and write what you will do about each. This is Portfolio work.',
              '<strong>Step 3 · With your group.</strong> Your group agrees the triggers most likely to surface for the strategy in your Capstone Blueprint: where, what your team will do and who owns it. You confirm it. This is Capstone work.',
              '<strong>To close.</strong> You write your own 30-Day Behavioural Commitment.']
SEC5_HOW_F = ['<strong>Step 1 · Taught.</strong> The toolkit has one table for each check. Each row gives one element, its two cues and its likely trigger.',
              '<strong>Step 2 · Individual.</strong> Each participant selects the triggers most likely to surface in their own area and writes what they will do about each. This is Portfolio work.',
              '<strong>Step 3 · Group.</strong> Each group agrees the triggers most likely to surface for the strategy in its Capstone Blueprint: where, what the team will do and who owns it. Each participant confirms it. This is Capstone work.',
              '<strong>To close.</strong> Each participant writes a 30-Day Behavioural Commitment.']

HERO5_P = 'The Alignment Toolkit brings the tools of the 4 Checks into one working page: 3S, SCARF, STAT and ACE-IT. You apply it to the strategy in your team’s Capstone Blueprint.'
HERO5_F = 'Application &middot; The Alignment Toolkit brings the tools of the 4 Checks into one working page: 3S, SCARF, STAT and ACE-IT. Participants apply it to the strategy in their team’s Capstone Blueprint.'
HERO3_H = 'Where Does the Leadership Team Stand?'
HERO3_P = 'The OCEAVL Assessment shows the behavioural profile you bring to the strategy, and the profile your leadership team brings together. It shows where alignment work starts.'
HERO3_F = 'The OCEAVL Assessment shows the behavioural profile each leader brings to the strategy, and the profile the leadership team brings together. It shows where alignment work starts.'
OUTCOME_TAIL_OLD_P = 'and a transition mapped for two of the changes your strategy requires &mdash;'
OUTCOME_TAIL_OLD_F = 'and a transition mapped for two of the changes the strategy requires &mdash;'
OUTCOME_TAIL_P = 'and an agreed plan for the triggers most likely to surface as your strategy lands &mdash;'
OUTCOME_TAIL_F = 'and an agreed plan for the triggers most likely to surface as the strategy lands &mdash;'

# ── Unit Summary ───────────────────────────────────────────────────────────────────────────────────
DIMS = ', '.join(d['name'] for d in OCEAVL[:-1]) + ' and ' + OCEAVL[-1]['name']
SUMMARY_P3 = ('You completed the OCEAVL Assessment for yourself, across seven dimensions: ' + DIMS + '. '
              'You scored yourself from 1 to 5 and read your own level on each dimension: Low, Balanced or High. '
              'Every level carries a risk, a response and three routines that hold the response in place. '
              'Once every member of your team has submitted, your team’s level on each dimension, the level held by most members, appears in your team’s Capstone Blueprint.')
SUMMARY_P5 = ('You worked with the Alignment Toolkit, which gives two cues and a likely trigger for each element of 3S, SCARF, STAT and ACE-IT. '
              'You built your own watch list: the triggers most likely to surface in your area as the changes in your strategy land, and what you will do about each. '
              'With your group you agreed the Team Alignment Plan: the triggers most likely to surface under each check, where each will surface, what your team will do and the leader who owns it. '
              'Your group’s confirmed plan feeds your team’s Capstone Blueprint. You closed with one 30-day behavioural commitment.')
SUMMARY_F3 = ('  <div style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#5ecba1;margin-bottom:8px;">3 &mdash; Extrapolating: Where the Leadership Team Stands</div>\n'
              '  <p>Next, the <em>Where.</em> Each participant completed the <strong>OCEAVL Assessment</strong> for themselves, across seven dimensions:</p>\n'
              '  <ul style="margin:10px 0 10px 18px;">\n' + ''.join('    <li>%s</li>\n' % d['name'] for d in OCEAVL) + '  </ul>\n'
              '  <p>Each participant scores themselves from <strong>1</strong> to <strong>5</strong> and reads their own level on each dimension: <strong>Low</strong>, <strong>Balanced</strong> or <strong>High</strong>. '
              'Every level carries a risk, a response and three routines. Once every member of a team has submitted, the team’s level on each dimension, the level held by most members, appears in the team’s Capstone Blueprint.</p>\n')
SUMMARY_F5_H = '5 &mdash; Application: The Alignment Toolkit'
SUMMARY_F5 = ('Each participant worked with the Alignment Toolkit, which gives two cues and a likely trigger for each element of 3S, SCARF, STAT and ACE-IT, and built a watch list: '
              'the triggers most likely to surface in their own area, and what they will do about each. The group then agreed the Team Alignment Plan: the triggers most likely to surface under each check, '
              'where each will surface, what the team will do and the leader who owns it. The confirmed plan feeds each team’s Capstone Blueprint.')

# ── Section 4 · COMPASS leaves; each role card names its alignment hot zone (Carol, 8 October: "The hot zones will be of the alignment
#    checks which one would they be inclined to. So we remove the COMPASS." and "The hot zone must be aligned to the alignment of the
#    17 elements of 3S, SCARF, STAT and ACE-IT."). Each role takes one of the 17 elements. The trigger and the two cues on the card are
#    the toolkit's own (KIT), word for word. The choice of element for each role and the linking sentence are NEW, for her review.
HOT_H = 'Alignment Hot Zone'
HOT_INTRO_P = ('Each role carries an alignment hot zone: the element of 3S, SCARF, STAT or ACE-IT where the role is inclined to set off the trigger. '
               'Each card gives the likely trigger and the two cues from the Alignment Toolkit in Section 5. Read the hot zones of your team together: they show where your team is most likely to stall its own changes.')
HOT_INTRO_F = ('Each role carries an alignment hot zone: the element of 3S, SCARF, STAT or ACE-IT where the role is inclined to set off the trigger. '
               'Each card gives the likely trigger and the two cues from the Alignment Toolkit in Section 5. The team reads its hot zones together: they show where the team is most likely to stall its own changes.')
# role, toolkit element id, participant sentence, facilitator sentence
HOT = [
    ('CEO', 'shift', 'You set direction, and a direction is easy to announce without naming a practice, a group or a date.',
     'The CEO sets direction, and a direction is easy to announce without naming a practice, a group or a date.'),
    ('CFO', 'transparency', 'You hold the budget trade-offs, and a trade-off that stays unseen reaches people as a decision without its rationale.',
     'The CFO holds the budget trade-offs, and a trade-off that stays unseen reaches people as a decision without its rationale.'),
    ('COO', 'time', 'You convert strategy into operational flow, and new work is easy to add to a day that is already full.',
     'The COO converts strategy into operational flow, and new work is easy to add to a day that is already full.'),
    ('CHRO', 'skill', 'You lead capability development, and a briefing is easy to count as capability.',
     'The CHRO leads capability development, and a briefing is easy to count as capability.'),
    ('CTO/CIO', 'tools', 'You supply the systems, and a new practice stalls where the system still fits the old way.',
     'The CTO or CIO supplies the systems, and a new practice stalls where the system still fits the old way.'),
    ('CMO', 'engagement', 'You craft the message, and a message sent one way leaves people with no forum to answer it.',
     'The CMO crafts the message, and a message sent one way leaves people with no forum to answer it.'),
    ('CCO', 'fairness', 'You set targets and rewards, and people read every reward as a signal of what is fair.',
     'The CCO sets targets and rewards, and people read every reward as a signal of what is fair.'),
    ('CPO', 'authority', 'You set the approvals for spend, and an approval rule can hold a decision the change has moved to the front line.',
     'The CPO sets the approvals for spend, and an approval rule can hold a decision the change has moved to the front line.'),
    ('CRO', 'autonomy', 'You set controls and reporting, and each added control takes discretion from the people doing the work.',
     'The CRO sets controls and reporting, and each added control takes discretion from the people doing the work.'),
    ('CSO', 'stake', 'You hold the logic of the strategy, and its reasons are easy to state as enterprise benefits that never reach a team’s own work.',
     'The CSO holds the logic of the strategy, and its reasons are easy to state as enterprise benefits that never reach a team’s own work.'),
]
_K = {k[0]: k for k in KIT}
assert len(HOT) == 10 and len({h[1] for h in HOT}) == 10 and all(h[1] in _K for h in HOT)
def hot_tag(n):
    k = _K[HOT[n][1]]; c = CHECKS[k[1]]
    return c['name'] + ' &middot; ' + c['tool'] + ' &middot; ' + k[2]
HOT_SUMMARY = '; '.join('the %s to %s' % (h[0], _K[h[1]][2]) for h in HOT)
CEO_FIX = [('As CEO, you integrate all seven COMPASS domains into one coherent strategic narrative.', 'As CEO, you integrate the functional perspectives of your leadership team into one coherent strategic narrative.'),
           ('all other roles struggle to converge &mdash; the COMPASS framework loses its anchor point.', 'all other roles struggle to converge, and the leadership team loses its anchor point.'),
           ('Integrates all seven COMPASS domains into one coherent strategic narrative.', 'Integrates the functional perspectives of the leadership team into one coherent strategic narrative.')]

def role_detail(n, page, old_html):
    """The role panel as build_[p|f].py wrote it, with the COMPASS column turned into the alignment hot zone."""
    k = _K[HOT[n][1]]
    i = old_html.index('<h5>Primary COMPASS Activation</h5>'); j = old_html.index('</div>', old_html.index('<div class="rl-domains">', i)) + len('</div>')
    new = (old_html[:i] + '<h5>' + HOT_H + '</h5><div class="rl-domains"><span class="d-tag">' + hot_tag(n) + '</span></div>'
           '<p class="u5-hot">' + HOT[n][2 if page == 'p' else 3] + '</p>'
           '<p class="u5-hot"><b>Likely trigger</b>' + k[5] + '</p><p class="u5-hot"><b>Look out for</b>' + k[3] + ' ' + k[4] + '</p>' + old_html[j:])
    for a, b in CEO_FIX: new = new.replace(a, b)
    return new

SEC4 = [  # both pages
    (', stabilising all seven COMPASS domains.</p>', '.</p>'),
    ('&#10003; One coherent signal across the organisation. COMPASS domains become leverage points for performance.', '&#10003; One coherent signal across the organisation. Changes pass the 4 Checks of Mind, Heart, Hands and Habit.'),
    ('COMPASS domains begin to drift</li>', 'Changes stall at the first check they fail</li>'),
    ('&#9888; Multiple conflicting signals. Leverage zones become sources of execution friction.', '&#9888; Multiple conflicting signals. Each function becomes a source of execution friction.'),
]
SUMMARY_P4_OLD = ('Without it, different leaders transmit different interpretations, COMPASS domains drift, and strategic instability spreads invisibly. Each CXO role carries a distinct alignment responsibility mapped to two primary COMPASS activations — the CEO anchors Clarity and Organisational Alignment; CFO/CPO activate Resources; COO/CTO/CRO drive Systems & Execution; CHRO carries People & Capability; CMO/CSO maintain Clarity and Sensing. When any role drops its responsibility, the COMPASS framework loses an anchor and the rest cannot fully converge — Collective Intelligence is the combined signal.')
SUMMARY_P4_NEW = ('Without it, different leaders transmit different interpretations, changes stall at the first check they fail, and strategic instability spreads invisibly. Each CXO role carries a distinct alignment responsibility and an alignment hot zone, the element of 3S, SCARF, STAT or ACE-IT it is inclined to: ' + HOT_SUMMARY + '. When any role drops its responsibility, the rest cannot fully converge — Collective Intelligence is the combined signal.')
SUMMARY_F4 = ('Each CXO role carries a distinct alignment responsibility and an alignment hot zone, the element of 3S, SCARF, STAT or ACE-IT it is inclined to:</p>\n  <ul style="margin:10px 0 10px 18px;">\n' +
              ''.join('    <li><strong>%s</strong> &mdash; %s</li>\n' % (h[0], hot_tag(n)) for n, h in enumerate(HOT)) + '  </ul>\n'
              '  <p>When any role drops its responsibility, the rest cannot fully converge. ')
