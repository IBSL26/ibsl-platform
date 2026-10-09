# -*- coding: utf-8 -*-
"""Unit 5 amendments of 9 October 2026, on Carol's word. Shared content for amend2_p.py and amend2_f.py.
Her instructions:
  3.1  The participant scores first: the assessment comes before the seven dimensions. The instructions for the assessment
       merge with "How the profile is read" into one block.
  4    4.1 merges with 4.3 under the header "Leading Change with One Voice". The old 4.1 becomes notes inside it. It is the new 4.1.
  4.2  Plain words: what a Converging Zone Contribution is, what an Alignment Hot Zone is, why the two are linked. Clear narrative
       for each role. "We are aligning hearts and minds so it must flow and reflect that."
  5    The application is on the 3S Check and ACE-IT only.
The hot zones in 4.2 stay on the 17 elements of 3S, SCARF, STAT and ACE-IT (her word of 8 October).
Her second round, same morning, after the first review files:
  3.1  "Let us have meanings for routine - people won't know what these are."  -> ROUT: one plain line for each of the 63 routines (NEW wording).
  4.2  "We are still not clear on these in section 4, what do they actually mean" (the three lines on the role card) -> each card now tells the
       role's own story: what sets it off, what is seen and heard, what it costs, in the role's own setting (NEW wording). "How to read a role card" says what each line is.
  5    "Let us simplify the application and remove personal watch list, so that they just work as a group." -> two steps: The Toolkit, Team Alignment Plan.
Third round, same morning: "Let us remove the 30 day behavioural commitment" -> it leaves both files (key syn_30day is no longer written)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5b_content as B

# ── 3.1 · one block: how to complete the assessment and how the profile is read ─────────────────────────────────────────
OC_TITLE_P = 'Portfolio work &middot; How to complete and read your OCEAVL Assessment'
OC_STEPS_P = [
    'Score yourself from 1 to 5 on each of the seven dimensions: 1 is strongly low, 3 is balanced and 5 is strongly high. Work alone. Your scores are your own.',
    'A score of 4 or 5 is High, 3 is Balanced, and 1 or 2 is Low. This gives your own level on each dimension.',
    'Read your own profile. Each level carries a risk, a response and three routines that hold the response in place.',
    'Select Submit to My Team’s Capstone. Your scores join your team’s profile.',
    'The level held by most members of your team is the team’s level for that dimension. Your team’s profile appears in your team’s Capstone Blueprint once every member has submitted.',
]
OC_EVERY = 'Every level carries a risk. A High level is a disposition to manage, as Low and Balanced are.'
OC_DIMS_H = 'The seven dimensions · expand each'
OC_DIMS_P = 'Each dimension is shown at its three levels. Read them after you have scored yourself, and compare your own level with the other two.'
OC_DIMS_F = 'Each dimension is shown at its three levels. Participants read them after they have scored themselves.'
OC_LEAD_F = 'After the lesson, each participant completes the OCEAVL Assessment alone in part 3.1 of their own file, as portfolio work. They score first and read the seven dimensions afterwards:'
OC_STEPS_F = [
    'They score themselves from 1 to 5 on each of the seven dimensions: 1 is strongly low, 3 is balanced and 5 is strongly high.',
    'A score of 4 or 5 is High, 3 is Balanced, and 1 or 2 is Low. This gives the participant’s own level on each dimension.',
    'They read their own profile. Each level carries a risk, a response and three routines that hold the response in place.',
    'They select Submit to My Team&rsquo;s Capstone. Print gives a copy of their own profile.',
    'The level held by most members of a team is the team’s level for that dimension. The team’s profile appears in the team’s Capstone Blueprint once every member has submitted.',
]
OC_CLOSE_F = (OC_EVERY + ' The team then agrees, in the Capstone, the two dimensions that carry the highest risk for the strategy. '
              'Each participant also writes a reflection in their own file: the level of their own that carries the highest risk for how they read and lead the strategy.')
OC_ORDER_F = ('  <p><strong>On the order:</strong> Teach how the assessment is completed and read, and name the seven dimensions. In their own file, participants score themselves first '
              'and read the seven dimensions at all three levels afterwards. The team&rsquo;s profile appears in the Capstone Blueprint once every member has submitted.</p>\n')
OC_SCALE = {1: '1 · strongly low', 2: '2', 3: '3 · balanced', 4: '4', 5: '5 · strongly high'}

# One plain line for each routine. Each routine holds one of the three responses of its level in place, in the same order (NEW wording, for Carol's review).
ROUT = {
    'Clarity Trial': 'The team agrees to act when it is about 70% sure, and reviews the result afterwards.',
    'Zero-Base Huddle': 'A short meeting that asks: if we were starting from nothing today, what would we do?',
    'Trend Rotation': 'Members take turns to bring one outside trend and a short “What if” note on what it could mean.',
    'The Stretch Sync': 'Each cycle the team picks one experiment that is uncomfortable on purpose, and reports back on it.',
    'The Intuition Log': 'The team runs one pilot on judgement, records the reasoning, and checks it later against what happened.',
    'The Moonshot Minute': 'A short slot in a meeting that asks what a result ten times bigger would require.',
    '48-Hour Validation': 'A new idea waits two days and must name the work it replaces before it is accepted.',
    'Finish Line Friday': 'Each Friday the team reviews what was finished. New work waits until open work is closed.',
    'The Anchor Check': 'Before any change of direction, the team states how it serves the agreed strategic intent.',
    'Monday Commit': 'Each Monday every member states their commitments for the week, and the team tracks them as red, amber or green.',
    'Quality Spot-Check': 'A colleague reviews each piece of work before it is closed.',
    'Ownership Stand-Up': 'A short meeting in which each key result is answered for by its one named owner.',
    'Load Audit': 'The team compares the work asked of it with its real capacity, and moves or drops work to fit.',
    'Step-Check': 'A checklist is used for every high-risk task, so that no step is skipped under pressure.',
    'Health Check': 'Set time is protected to clear backlogs and repair what was rushed.',
    'Pivot Sprint': 'When a plan changes, the team is authorised to run a short Plan B and act on it.',
    'Speed-to-Action': 'Planning has a fixed time limit. When it ends, the team acts.',
    'MVR Audit': 'Before work starts, the team defines the Minimum Viable Result: the least that counts as good enough.',
    'Digital Ink-Well': 'Meetings open with everyone writing their input in silence before anyone speaks.',
    'Pulse Check': 'Leaders hold regular one-to-one conversations to reconnect with each member.',
    'Flash Update': 'Each member sends a short update without being asked for it.',
    'Outcome-Only Syncs': 'Updates cover three things only: blockers, decisions and actions.',
    '51/49 Rule': 'Each forum has one named person who makes the final call when views are split.',
    'Intent Intro': 'Every meeting opens by restating the strategic intent it serves.',
    'Rotating Facilitator': 'A different member leads each meeting, and senior leaders speak last.',
    'Evidence Gate': 'A proposal is discussed only when it comes with a summary of the data behind it.',
    'Synergy Sync': 'The team names the one overlap between agendas that does the most damage, and resolves it.',
    'Issue-Evidence-Options': 'A disagreement is stated in three parts: the issue, the evidence and the options.',
    'Result-First Review': 'The team asks of its own behaviour: is this helping the result or harming it?',
    'Seam Huddle': 'Members of two departments swap a task, then meet to fix the hand-over between them.',
    'Stop-Start-Continue': 'Feedback is given in three parts: what to stop, what to start and what to continue.',
    'Hard-Talk Slot': 'The uncomfortable issue is the first item in the meeting.',
    'Pre-Mortem': 'Before a plan is approved, the team lists the reasons it might fail.',
    'Rotating Challenger': 'One member, a different one each time, is given the job of arguing against the proposal.',
    'No-Log': 'The team checks its capacity before it accepts new work, and keeps a record of what it declined.',
    'Radical Candor Loop': 'Members raise tensions through an anonymous channel, and the team answers them in the open.',
    'Morning-After Review': 'A high-stakes decision waits a day and is reviewed the next morning before it is confirmed.',
    'Error-Share': 'Leaders share a mistake of their own first, so that others feel safe to report theirs.',
    'Daily Truth': 'In volatile periods, a short daily briefing gives the facts as they stand.',
    'Pulse Audit': 'Leaders spend visible time with their teams and ask how people are coping.',
    'Human Sync': 'A regular check-in in which leaders name what people are feeling and acknowledge it.',
    'Burn Rate Review': 'The team reviews how fast time and resources are being used, and raises the pace where it is needed.',
    'Gratitude Minute': 'Meetings open with a named thank-you for effort, strain or contribution.',
    'Red-Team Audit': 'A separate group tests the claim that all is under control, and asks for the data.',
    'Frontline Friday': 'Leaders spend regular time working alongside frontline staff.',
    'Value Filter': 'Work is tested against the stated values, and work that breaks them is paused in the open.',
    'Culture Stand-Up': 'Culture ambassadors move between departments and report what they see in a short meeting.',
    'Integrity Scorecard': 'A formal review compares what was promised with what was delivered.',
    'Narrative Share': 'Members tell short stories of the values being lived in real work.',
    'Value KPI Check': 'Each value is tied to at least one live performance measure, and the measure is reviewed.',
    'Decision Audit': 'After a hard decision, the team records which values it used to decide.',
    'Value Evolution': 'From time to time the team reviews whether its values still serve the strategy.',
    'Diversity Huddle': 'An outsider is invited in to give a different view.',
    'Merit Sync': 'Feedback is given on outcomes and values only.',
    '10-Minute Teach': 'Each month a member tries one small new tool and shows the team what they learned, in a short slot.',
    'Post-Mortem Pulse': 'After a mistake, the team records what happened and what was learned, with no blame.',
    'Reverse Feedback': 'Leaders ask their team for feedback on themselves before they give any.',
    'Quarterly Growth Review': 'Each quarter the team looks back at what it learned and at the root causes of what went wrong.',
    '7-Day Implementation': 'Within a week of a learning event, each member writes how they have applied it.',
    'Root-Cause Sync': 'After a failure, the team asks “why?” five times to reach the cause.',
    'Playbook Build': 'Time for experiments is capped, and what was learned is written into a shared playbook.',
    'Sync Cycle': 'New learning is released at the pace the organisation can absorb.',
    'Standard Build': 'A lesson becomes the standard way of working before the next new idea is taken on.',
}
ROUT_H = 'Routines · what each one is'
def rout_list(lv):
    names = [x.strip() for x in lv['rout'].split(';')]
    assert len(names) == 3 and all(n in ROUT for n in names), names
    return [[n, ROUT[n]] for n in names]
_all = [n for d in B.OCEAVL for lv in d['levels'] for n, _ in rout_list(lv)]
assert len(_all) == 63 and len(set(_all)) == 63 and set(_all) == set(ROUT), set(ROUT) ^ set(_all)
OCEAVL2 = [dict(d, levels=[dict(lv, rd=rout_list(lv)) for lv in d['levels']]) for d in B.OCEAVL]

def oceavl_dims():
    s = ''
    for d in OCEAVL2:
        s += '  <details class="u5-dim"><summary><span class="u5-dim-n">%s</span><span class="u5-dim-d">%s</span></summary>\n' % (d['name'], d['desc'])
        for lv in d['levels']:
            s += ('    <div class="u5-lv"><div class="u5-lv-h">%s</div><p class="u5-lv-dna">%s</p><div class="u5-lv-g u5-lv-g2">'
                  '<div><b>Risk</b>%s</div><div><b>Response</b>%s</div></div>'
                  '<div class="u5-rt"><b>%s</b><ul>%s</ul></div></div>\n') % (
                      lv['level'], lv['dna'], lv['risk'], lv['resp'], ROUT_H, ''.join('<li><strong>%s.</strong> %s</li>' % (n, m) for n, m in lv['rd']))
        s += '  </details>\n'
    return s

# ── 4.1 · Leading Change with One Voice (the old 4.3, with the old 4.1 as notes inside it) ───────────────────────────────
T41 = 'Leading Change with One Voice'
T41_META = 'Four Commitments'
ONE_H = 'What one voice creates'
ONE_P = ('The Converging Zone is the point where the separate views of each function come together into one shared reading of the strategy. '
         'A leadership team that reaches it has Collective Intelligence, and the organisation hears one voice. The two columns show what people receive with it and without it.')
FOUR_H = 'The four commitments'

# ── 4.2 · Collective Intelligence Across the Leadership Team ────────────────────────────────────────────────────────────
TEACH_H = 'What this part teaches'
TEACH_P = 'Every role on a leadership team affects alignment in two ways at once. This part shows both for your role, side by side.'
TEACH_F = 'Every role on a leadership team affects alignment in two ways at once. This part shows both for each role, side by side.'
CZC_H = 'Converging Zone Contribution'
CZC_P = ('What your role brings so that your leadership team reads the strategy as one. The Converging Zone is the point where the separate views of each function '
         'come together into one shared reading. Your contribution is the part of that reading only your role can supply.')
CZC_F = ('What a role brings so that the leadership team reads the strategy as one. The Converging Zone is the point where the separate views of each function '
         'come together into one shared reading. A role&rsquo;s contribution is the part of that reading only that role can supply.')
AHZ_H = 'Alignment Hot Zone'
AHZ_P = ('The one place where your role is most likely to lose people as it does its normal work. It is one of the 17 elements of 3S, SCARF, STAT and ACE-IT '
         'that you met in parts 1.3.1 to 1.3.4. It tells you which check your role puts at risk: people&rsquo;s understanding (Mind), their willingness (Heart), '
         'their ability to act (Hands) or their follow-through (Habit).')
AHZ_F = ('The one place where a role is most likely to lose people as it does its normal work. It is one of the 17 elements of 3S, SCARF, STAT and ACE-IT '
         'taught in parts 1.3.1 to 1.3.4. It tells the leader which check the role puts at risk: people&rsquo;s understanding (Mind), their willingness (Heart), '
         'their ability to act (Hands) or their follow-through (Habit).')
WHY_P = ('<strong>Why the two are shown together.</strong> They come from the same work. The work that makes your role valuable to the team is the work that creates its hot zone. '
         'The CEO sets direction: that is the contribution. A direction announced in broad terms leaves people unsure what changes for them: that is the hot zone. '
         'When you know both, you keep giving the contribution and you guard the hot zone.')
WHY_F = ('<strong>Why the two are shown together.</strong> They come from the same work. The work that makes a role valuable to the team is the work that creates its hot zone. '
         'The CEO sets direction: that is the contribution. A direction announced in broad terms leaves people unsure what changes for them: that is the hot zone. '
         'A leader who knows both keeps giving the contribution and guards the hot zone.')
READ_H = 'How to read a role card'
HOT_LINES_P = ['<strong>Why your role is inclined to it:</strong> how your normal work creates the risk.',
               '<strong>What sets it off:</strong> the action that starts the problem.',
               '<strong>What you will see and hear:</strong> the signs that it has started.',
               '<strong>What it costs:</strong> what people then do, and what the change loses.']
HOT_LINES_F = ['<strong>Why the role is inclined to it:</strong> how the role&rsquo;s normal work creates the risk.',
               '<strong>What sets it off:</strong> the action that starts the problem.',
               '<strong>What is seen and heard:</strong> the signs that it has started.',
               '<strong>What it costs:</strong> what people then do, and what the change loses.']
_lines = lambda L: '<ul>' + ''.join('<li>' + x + '</li>' for x in L) + '</ul>'
READ_P = ['Click your own role first. On the left, read your contribution.',
          'On the right, read your hot zone. It opens with what people need, and then has four lines:' + _lines(HOT_LINES_P),
          'Then read the roles closest to yours.']
READ_CLOSE_P = 'Read together, the hot zones of your team show where its changes are most likely to lose people&rsquo;s minds and hearts.'
READ_F = ['Each participant clicks their own role first and reads the contribution on the left.',
          'On the right they read the hot zone. It opens with what people need, and then has four lines:' + _lines(HOT_LINES_F),
          'They then read the roles closest to their own.']
READ_CLOSE_F = 'Read together, the hot zones of a team show where its changes are most likely to lose people&rsquo;s minds and hearts.'
GUIDE42_F = ('<strong>Teaching the two terms:</strong> Use the CEO card as the example before participants open their own role: the contribution on the left, the hot zone on the right, '
             'and the one piece of work that produces both.')

K_CZC_P = 'What your role brings to the shared reading of the strategy'
K_CZC_F = 'What the role brings to the shared reading of the strategy'
K_AHZ_P = 'Where your role is most likely to lose people'
K_AHZ_F = 'Where the role is most likely to lose people'
L_WHY_P = 'Why your role is inclined to it'
L_WHY_F = 'Why the role is inclined to it'
L_TRIG = 'What sets it off'
L_CUES_P = 'What you will see and hear'
L_CUES_F = 'What is seen and heard'
L_COST = 'What it costs'
# What people need, in plain words, for the ten elements the roles carry.
NEED = {
    'shift': 'People need to know exactly what is changing.',
    'stake': 'People need to know why the change matters to them.',
    'fairness': 'People need to see the change applied evenly.',
    'autonomy': 'People need some control over how they do their own work.',
    'skill': 'People need to know how to do the new work.',
    'time': 'People need the hours to do the new work.',
    'authority': 'People need permission to decide and act.',
    'tools': 'People need the systems and resources the new work depends on.',
    'engagement': 'People need a say in how the change is going.',
    'transparency': 'People need to see the reasoning, the progress and the constraints.',
}
# role, element id (unchanged from 8 October), participant narrative, facilitator narrative
HOT2 = [
    ('CEO', 'shift',
     'You set the direction for the whole organisation. A direction is broad, and it is easy to announce one without saying which practice changes, for which group, from which date. People then cannot picture the change, and each team fills the gap with its own version.',
     'The CEO sets the direction for the whole organisation. A direction is broad, and it is easy to announce one without saying which practice changes, for which group, from which date. People then cannot picture the change, and each team fills the gap with its own version.'),
    ('CFO', 'transparency',
     'You decide where the money goes, and every budget decision is a trade-off. A trade-off is uncomfortable to show, so the decision often reaches people without its reasons. People then read the cut as the real message about the change.',
     'The CFO decides where the money goes, and every budget decision is a trade-off. A trade-off is uncomfortable to show, so the decision often reaches people without its reasons. People then read the cut as the real message about the change.'),
    ('COO', 'time',
     'You turn the strategy into daily work. Each new practice looks small when it is added, and it is easy to add it to a day that is already full without taking any old work away. People then want the change and have no hours to do it.',
     'The COO turns the strategy into daily work. Each new practice looks small when it is added, and it is easy to add it to a day that is already full without taking any old work away. People then want the change and have no hours to do it.'),
    ('CHRO', 'skill',
     'You lead the building of capability. A briefing or a training session is easy to count as capability built. People have heard about the new work and have not yet practised it, so they make errors and go back to the old method.',
     'The CHRO leads the building of capability. A briefing or a training session is easy to count as capability built. People have heard about the new work and have not yet practised it, so they make errors and go back to the old method.'),
    ('CTO/CIO', 'tools',
     'You supply the systems people work in every day. A new practice can be agreed long before the system, the form or the budget has changed to fit it. People then try the new way, find that the system still fits the old way, and build workarounds.',
     'The CTO or CIO supplies the systems people work in every day. A new practice can be agreed long before the system, the form or the budget has changed to fit it. People then try the new way, find that the system still fits the old way, and build workarounds.'),
    ('CMO', 'engagement',
     'You shape the message about the change. A strong message travels one way, from leaders to people, and it is easy to treat the message as the conversation. People then have nowhere to say how the change is going, and they stop owning it.',
     'The CMO shapes the message about the change. A strong message travels one way, from leaders to people, and it is easy to treat the message as the conversation. People then have nowhere to say how the change is going, and they stop owning it.'),
    ('CCO', 'fairness',
     'You set the targets and the rewards. People read every target and every reward as a signal of what is fair. When the change asks more of one team than of another, or the rewards still favour the old behaviour, people stop wanting it to succeed.',
     'The CCO sets the targets and the rewards. People read every target and every reward as a signal of what is fair. When the change asks more of one team than of another, or the rewards still favour the old behaviour, people stop wanting it to succeed.'),
    ('CPO', 'authority',
     'You set the approval rules for spend. A change often moves a decision closer to the front line, and the approval rule stays where it was. People then ask permission for what the change has asked them to do, and the decision travels back up.',
     'The CPO sets the approval rules for spend. A change often moves a decision closer to the front line, and the approval rule stays where it was. People then ask permission for what the change has asked them to do, and the decision travels back up.'),
    ('CRO', 'autonomy',
     'You set the controls and the reporting. Each control is added for a sound reason, and each one takes some discretion from the people doing the work. As the controls add up, people feel they have lost control of their own work, and they comply without energy.',
     'The CRO sets the controls and the reporting. Each control is added for a sound reason, and each one takes some discretion from the people doing the work. As the controls add up, people feel they have lost control of their own work, and they comply without energy.'),
    ('CSO', 'stake',
     'You hold the reasoning behind the strategy. That reasoning is usually stated as a benefit to the enterprise: growth, margin or position. A benefit that never reaches a team&rsquo;s own work sounds like someone else&rsquo;s reason, so people can describe the change and cannot say what it is for.',
     'The CSO holds the reasoning behind the strategy. That reasoning is usually stated as a benefit to the enterprise: growth, margin or position. A benefit that never reaches a team&rsquo;s own work sounds like someone else&rsquo;s reason, so people can describe the change and cannot say what it is for.'),
]
STORY = {
    'shift': ('The change is announced as a direction, such as “we are becoming more customer-focused”. Nobody says which practice stops, which practice starts, for which group and from which date.',
              'People keep working the old way and call it by the new name. Three teams asked what is changing give three different answers.',
              'People cannot follow a change they cannot picture. Each team acts on its own version, and effort goes in different directions.'),
    'transparency': ('A budget is cut, frozen or moved, and people are told the decision without the reason. Good results are shared quickly and setbacks are shared late.',
                     'People say “Finance said no” and cannot explain why. Teams stop keeping their own figures up to date, because they never see what the figures are used for.',
                     'People treat the change as a cost exercise that will pass. They keep the new practice while it is checked and drop it afterwards.'),
    'time': ('A new practice is added to the working day and nothing is taken away. The old targets and deadlines stay as they were.',
             'The new practice is done at the end of the day, or dropped on a busy day. People say “we will get to it when things calm down.”',
             'People who agree with the change still cannot do it. Their goodwill wears out, because they are asked for more than the day can hold.'),
    'skill': ('People attend a briefing or a training session and are then expected to perform. Nobody watches them do the new work and corrects them.',
              'Errors and rework rise. Everyone goes to the same one or two experts. People say “let me do it the old way to get it done.”',
              'People lose confidence in themselves and in the change, and the old way starts to look safer.'),
    'tools': ('The new practice starts before the system, the form or the access rights have been changed to support it.',
              'People keep their own spreadsheets beside the system. Work waits on another team for access or data.',
              'People do the work twice, once in the new way and once in the old. The extra effort turns willing people against the change.'),
    'engagement': ('The change is launched as a campaign: a town hall, emails and posters. People are told about it and are never asked how it is going.',
                   'Meetings about the change are presentations, and people ask nothing. Asked why the change matters, they cannot say it in their own words.',
                   'People stay spectators of the change, so it fades when the campaign ends.'),
    'fairness': ('The change asks more of one team than of another, or the targets and rewards still pay for the old behaviour.',
                 'People ask “why us and never them?” They talk about the change in the corridor and say nothing in the meeting.',
                 'People stop wanting the change to succeed. They do what is measured and hold back the rest.'),
    'authority': ('The change asks front-line people to decide for themselves, and the approval limits stay where they were. The first person who decides alone is overruled.',
                  'Requests for approval rise. People ask “am I allowed to do this?” about the very thing the change asks of them.',
                  'Decisions travel back up, and the new way runs slower than the old one. People conclude that the change is talk.'),
    'autonomy': ('New controls, sign-offs or reports arrive with the change, and people are given no choice in how they meet them.',
                 'People do exactly what the rule says and nothing more. Forms are completed and questions stop.',
                 'People comply and stop caring. The paperwork arrives, and the judgement and energy the change depends on are lost.'),
    'stake': ('The reason for the change is given as a benefit to the organisation, such as growth or margin. Nobody says what the team gains, or what it loses by staying as it is.',
              'People say “because head office said so.” They can describe the change and cannot say what it is for.',
              'People carry out the change while they are watched and set it aside under pressure. They have the instruction and are missing the reason.'),
}
_K = {k[0]: k for k in B.KIT}
assert [h[0] for h in HOT2] == [h[0] for h in B.HOT] and [h[1] for h in HOT2] == [h[1] for h in B.HOT], 'roles and elements stay as they were'
assert all(h[1] in NEED and h[1] in STORY for h in HOT2)
def hot_tag2(n):
    k = _K[HOT2[n][1]]; c = B.CHECKS[k[1]]
    return k[2] + ' &middot; ' + c['name'] + ' (' + c['tool'] + ')'
HOT_SUMMARY2 = '; '.join('the %s at %s' % (h[0], _K[h[1]][2]) for h in HOT2)

def role_detail2(n, page, old_html):
    """The role panel as amend_[p|f].py wrote it, rebuilt: contribution on the left with its closing line, hot zone on the right in plain words."""
    p = page == 'p'
    k = _K[HOT2[n][1]]
    a = '<div class="rl-col"><h5>Converging Zone Contribution</h5>'
    b = '</div><div class="rl-col"><h5>Alignment Hot Zone</h5>'
    assert old_html.count(a) == 1 and old_html.count(b) == 1, n
    head, rest = old_html.split(a)
    contrib, hot = rest.split(b)
    m = __import__('re').search(r'(<p style="margin-top:12px;font-size:12px;color:rgba\(255,255,255,\.5\);">.*?</p>)</div></div>$', hot)
    assert m, n
    closing = m.group(1)
    return (head + a + '<p class="u5-rl-k">' + (K_CZC_P if p else K_CZC_F) + '</p>' + contrib + closing + b +
            '<p class="u5-rl-k">' + (K_AHZ_P if p else K_AHZ_F) + '</p>'
            '<div class="rl-domains"><span class="d-tag">' + hot_tag2(n) + '</span></div>'
            '<p class="u5-hot u5-need">' + NEED[k[0]] + '</p>'
            '<p class="u5-hot"><b>' + (L_WHY_P if p else L_WHY_F) + '</b>' + HOT2[n][2 if p else 3] + '</p>'
            '<p class="u5-hot"><b>' + L_TRIG + '</b>' + STORY[k[0]][0] + '</p>'
            '<p class="u5-hot"><b>' + (L_CUES_P if p else L_CUES_F) + '</b>' + STORY[k[0]][1] + '</p>'
            '<p class="u5-hot"><b>' + L_COST + '</b>' + STORY[k[0]][2] + '</p></div></div>')

def teach42(page):
    p = page == 'p'
    return ('  <div class="u5-how"><div class="u5-how-h">' + TEACH_H + '</div><p>' + (TEACH_P if p else TEACH_F) + '</p></div>\n'
            '  <div class="u5-two">\n'
            '    <div class="u5-two-c"><div class="u5-two-h">' + CZC_H + '</div><p>' + (CZC_P if p else CZC_F) + '</p></div>\n'
            '    <div class="u5-two-c"><div class="u5-two-h">' + AHZ_H + '</div><p>' + (AHZ_P if p else AHZ_F) + '</p></div>\n'
            '  </div>\n'
            '  <div class="u5-group">' + (WHY_P if p else WHY_F) + '</div>\n'
            '  <div class="u5-how"><div class="u5-how-h">' + READ_H + '</div><ol>' + ''.join('<li>' + x + '</li>' for x in (READ_P if p else READ_F)) + '</ol>'
            '<p>' + (READ_CLOSE_P if p else READ_CLOSE_F) + '</p></div>\n')

# ── Section 5 · the Alignment Toolkit on the 3S Check and ACE-IT ────────────────────────────────────────────────────────
CHECKS5 = [dict(B.CHECKS[0], label='the 3S Check'), dict(B.CHECKS[3], label='ACE-IT')]
_MAP = {0: 0, 3: 1}
KIT5 = [k for k in B.KIT if k[1] in _MAP]
assert [k[2] for k in KIT5] == ['Shift', 'Stake', 'Step', 'Accountability', 'Commitment', 'Engagement', 'Integrity', 'Transparency']
KIT5_JS = [{'id': k[0], 'c': _MAP[k[1]], 'n': k[2], 'cues': [k[3], k[4]], 'trig': k[5]} for k in KIT5]
KIT5_NAMES = ['Alignment Plan · ' + c['name'] for c in CHECKS5]
KIT5_KEYS = ['kit_' + c['id'] for c in CHECKS5]

HERO5_P = ('The Alignment Toolkit applies two tools from the 4 Checks to the strategy in your team’s Capstone Blueprint. '
           'The 3S Check gets a change understood. ACE-IT holds it in place.')
HERO5_F = ('Application &middot; The Alignment Toolkit applies two tools from the 4 Checks to the strategy in each team’s Capstone Blueprint. '
           'The 3S Check gets a change understood. ACE-IT holds it in place.')
STEP_NAMES5 = ['The Toolkit', 'Team Alignment Plan']
def sec5_how(page):
    p = page == 'p'
    if p:
        lead = ('You work with two tools you met in Section 1: the <strong>3S Check</strong> (Shift, Stake, Step) and <strong>ACE-IT</strong> '
                '(Accountability, Commitment, Engagement, Integrity, Transparency). Together they have eight elements. For each element, the toolkit gives you:')
        gives = ['<strong>Two cues.</strong> What you will see or hear when the element is missing.', '<strong>One likely trigger.</strong> The condition that causes it.']
        mid = 'You use them in two steps:'
        steps = ['<strong>Step 1 · Read the toolkit.</strong> You read the eight elements and one worked example. You enter nothing.',
                 '<strong>Step 2 · Team Alignment Plan, with your group.</strong> Your group looks at the changes the strategy in your Capstone Blueprint asks of people, and selects the triggers it expects. For each one you write where it will surface, what your team will do and the leader who owns it. You then select Confirm. This is Capstone work, and the confirmed plan feeds your team’s Capstone Blueprint.']
    else:
        lead = ('Participants work with two tools taught in Section 1: the <strong>3S Check</strong> (Shift, Stake, Step) and <strong>ACE-IT</strong> '
                '(Accountability, Commitment, Engagement, Integrity, Transparency). Together they have eight elements. For each element, the toolkit gives:')
        gives = ['<strong>Two cues.</strong> What is seen or heard when the element is missing.', '<strong>One likely trigger.</strong> The condition that causes it.']
        mid = 'They are used in two steps:'
        steps = ['<strong>Step 1 · The toolkit, taught.</strong> The eight elements and one worked example. Participants enter nothing.',
                 '<strong>Step 2 · Team Alignment Plan, group.</strong> Each group looks at the changes the strategy in its Capstone Blueprint asks of people, and selects the triggers it expects. For each one it writes where the trigger will surface, what the team will do and the leader who owns it. Each participant then selects Confirm. This is Capstone work, and the confirmed plan feeds the team’s Capstone Blueprint.']
    return ('<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div><p>' + lead + '</p><ul>' + ''.join('<li>' + x + '</li>' for x in gives) + '</ul>'
            '<p>' + mid + '</p><ol>' + ''.join('<li>' + x + '</li>' for x in steps) + '</ol></div>\n\n')

KIT_INTRO = 'The toolkit has two tables, one for each tool. Each row is one element, with its two cues and its likely trigger.'
EX_LEAD = 'A finished Team Alignment Plan looks like this: one trigger from the 3S Check and one from ACE-IT.'
KIT_EXAMPLE5 = [r for r in B.KIT_EXAMPLE if r[0].startswith(('Mind', 'Habit'))]
assert len(KIT_EXAMPLE5) == 2

def toolkit_step1():
    s = '<p>' + KIT_INTRO + '</p>\n<div class="chg-h">How to read the toolkit</div>\n<ul>' + ''.join('<li>' + x + '</li>' for x in B.KIT_READ) + '</ul>\n'
    for ci, c in enumerate(CHECKS5):
        s += ('<div class="u5-kh"><span class="u5-kh-c">%s · %s</span><span class="u5-kh-l">%s</span></div>\n'
              '<div class="chg-wrap"><table class="chg-table wide u5-kt"><thead><tr><th>Element</th><th>Two cues to look out for</th><th>Likely trigger</th></tr></thead><tbody>\n') % (c['name'], c['tool'], c['line'])
        for k in KIT5:
            if _MAP[k[1]] == ci:
                s += '<tr><td>%s</td><td>%s<br>%s</td><td>%s</td></tr>\n' % (k[2], k[3], k[4], k[5])
        s += '</tbody></table></div>\n'
    s += ('<div class="chg-h">Worked example · resolve complaints at first contact</div>\n<p>' + EX_LEAD + '</p>\n'
          '<div class="chg-wrap"><table class="chg-table wide u5-kt"><thead><tr><th>Trigger most likely to surface</th><th>Cue to look out for</th><th>Where it will surface</th><th>What we will do</th><th>Leader who owns it</th></tr></thead><tbody>\n')
    for r in KIT_EXAMPLE5:
        s += '<tr>' + ''.join('<td>%s</td>' % x for x in r) + '</tr>\n'
    s += '</tbody></table></div>\n'
    return s

ONE_EACH = 'Select at least one from the 3S Check and at least one from ACE-IT.'
TEAM_HOW = ['Read the practices your strategy starts and stops, shown below. They come from the Start and Stop lists your group confirmed in Unit 3.',
            'Read the eight cards together. Each card is one element, with its likely trigger and the two cues that show it.',
            'Select “Likely to surface for our strategy” on the triggers your group agrees on, for the strategy in your Capstone Blueprint. ' + ONE_EACH,
            'In the boxes that open, write where the trigger will surface, what your team will do and the leader who owns it.',
            'Read your record at the foot of this step, then select Confirm. Select Print for a copy.']
TEAM_HINT = 'Each card is one element. Select “Likely to surface for our strategy” on the triggers your group agrees on. Three boxes open: where, what your team will do, and the leader who owns it.'
TEAM_HOW_F = ['The group reads the practices the strategy starts and stops. Each page shows the Start and Stop lists the group confirmed in Unit 3.',
              'The group reads the eight cards together. Each card is one element, with its likely trigger and the two cues that show it.',
              'The group selects &ldquo;Likely to surface for our strategy&rdquo; on the triggers it agrees on, for the strategy in its Capstone Blueprint, with at least one from the 3S Check and at least one from ACE-IT.',
              'In the boxes that open, the group writes where the trigger will surface, what the team will do and the leader who owns it.',
              'Each participant reads the record and selects Confirm. Print gives a copy of the record.']
SEC5_GUIDE_F = ['<strong>Order:</strong> Teach Step 1. Step 2 is group work.',
                '<strong>Facilitation principle:</strong> Your role in Step 2 is to name patterns. When members select different triggers for the same change, name it: <em>&ldquo;Each of you is reading this change from a different seat. The plan has to cover all of them.&rdquo;</em>']
STEP2_GUIDE_F = ['<strong>Briefing:</strong> Each group works with the Start and Stop lists it confirmed in Unit 3 in view.',
                 '<strong>Synthesis question:</strong> <em>&ldquo;Which trigger did the whole group select at once? Which did only one of you raise, and what does that member see from their seat?&rdquo;</em>',
                 '<strong>Watch for:</strong> every trigger selected. Ask which ones will surface first, and for which group.',
                 '<strong>Watch for:</strong> &ldquo;communicate more&rdquo; as the answer to every trigger. Ask which trigger the communication removes.',
                 '<strong>Watch for:</strong> a committee or a function named as owner. Hold out for one person.']
GUIDE_TAB_OLD = 'The Alignment Toolkit in Section 5 gives two cues and a likely trigger for each element of the four tools.</p>'
GUIDE_TAB_NEW = 'The Alignment Toolkit in Section 5 applies two of the tools, the 3S Check and ACE-IT, with two cues and a likely trigger for each of their eight elements.</p>'

# ── Unit Summary ────────────────────────────────────────────────────────────────────────────────────────────────────────
SUMMARY_P4_OLD = ('Each CXO role carries a distinct alignment responsibility and an alignment hot zone, the element of 3S, SCARF, STAT or ACE-IT it is inclined to: ' + B.HOT_SUMMARY +
                  '. When any role drops its responsibility, the rest cannot fully converge — Collective Intelligence is the combined signal. '
                  'Your leadership team leads change with one voice through four commitments, each protecting a check: one message (Mind), one example (Heart), one sequence (Hands) and one owner (Habit).')
SUMMARY_P4_NEW = ('Your leadership team leads change with one voice through four commitments, each protecting a check: one message (Mind), one example (Heart), one sequence (Hands) and one owner (Habit). '
                  'Each CXO role then brings two things to the team. Its Converging Zone Contribution is what the role adds to the shared reading of the strategy. '
                  'Its Alignment Hot Zone is the one element of 3S, SCARF, STAT or ACE-IT where the role is most likely to lose people as it does its work: ' + HOT_SUMMARY2 +
                  '. When any role drops its contribution, the rest cannot fully converge — Collective Intelligence is the combined signal.')
SUMMARY_P5 = ('You worked with the Alignment Toolkit, which gives two cues and a likely trigger for each element of the 3S Check and ACE-IT. '
              'With your group you agreed the Team Alignment Plan: the triggers most likely to surface for the strategy in your Capstone Blueprint, where each will surface, what your team will do and the leader who owns it. '
              'Your group’s confirmed plan feeds your team’s Capstone Blueprint.')
SUMMARY_F4_OLD_HEAD = 'Each CXO role carries a distinct alignment responsibility and an alignment hot zone, the element of 3S, SCARF, STAT or ACE-IT it is inclined to:</p>'
SUMMARY_F4_NEW_HEAD = ('The leadership team leads change with <strong>one voice</strong> through four commitments, each protecting a check: one message (Mind), one example (Heart), one sequence (Hands) and one owner (Habit). '
                       'Each CXO role then brings two things to the team: its <strong>Converging Zone Contribution</strong>, what the role adds to the shared reading of the strategy, and its <strong>Alignment Hot Zone</strong>, '
                       'the one element of 3S, SCARF, STAT or ACE-IT where the role is most likely to lose people as it does its work:</p>')
SUMMARY_F4_OLD_TAIL = '  <p>When any role drops its responsibility, the rest cannot fully converge. '
SUMMARY_F4_NEW_TAIL = '  <p>When any role drops its contribution, the rest cannot fully converge. '
SUMMARY_F5 = ('Each group worked with the Alignment Toolkit, which gives two cues and a likely trigger for each element of the 3S Check and ACE-IT, and agreed the Team Alignment Plan: '
              'the triggers most likely to surface for the strategy in its Capstone Blueprint, where each will surface, what the team will do and the leader who owns it. '
              'The confirmed plan feeds each team’s Capstone Blueprint.')
