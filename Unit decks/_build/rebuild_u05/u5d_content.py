# -*- coding: utf-8 -*-
"""Unit 5 · Section 5 as Carol set it on 9 October (fourth round, same morning). It takes the place of the cue-and-trigger toolkit.
Her words: "for the 3 Ss let us have the groups complete it. So based on their strategy they state the shift, the stake and step. Bring back the
guiding lesson from section 1. They state what is the change, what will the organisation gain, and what must be done differently. That way we help
them reflect and build their case properly. We can then add the ACE-IT and ask them to state what behaviours from a leadership team they will expect
... since they will have to check what the team score was on the OCEAVL."
The guide beside each box is the page's own text from parts 1.3.1 and 1.3.4, word for word (read from the page at build time)."""
import re, html as _html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5b_content as B

T5 = 'Leading with Clarity'          # Carol, 9 October: "Let us change this title The Alignment Toolkit to Leading with clarity."
# Section 5 learning outcome 1, Carol's wording of 9 October ("Determine how the organisation will land the strategy agenda."). Outcome 2 stays as it was.
SLO5_1_OLD = 'Formulate how one strategic change will be led and how leadership roles connect to support it.'
SLO5_1_NEW = 'Determine how the organisation will land the strategy agenda.'
STEP_NAMES = ['The 3S Check', 'ACE-IT']
S3 = ['Shift', 'Stake', 'Step']
ACE = ['Accountability', 'Commitment', 'Engagement', 'Integrity', 'Transparency']
FIELDS = [(n.lower(), n, 'mind') for n in S3] + [(n.lower(), n, 'habit') for n in ACE]
NAMES = ['Alignment Plan · Mind', 'Alignment Plan · Habit']          # the Capstone reads kit_mind and kit_habit under these names
REC_H = {'mind': 'The 3S Check · our Shift, Stake and Step', 'habit': 'ACE-IT · the behaviours we expect from our leadership team'}

def guide_3s(h):
    """Shift, Stake, Step as part 1.3.1 gives them on this page: question, what it is, weak, clear, the move."""
    out = []
    for n in S3:
        m = re.search(r'<div class="sc-trigger" style="[^"]*">' + n + r'</div><div class="sc-q">(.*?)</div></div>\s*<div class="sc-bar"[^>]*></div>\s*<div class="sc-body">(.*?)\n      </div>\n    </div>', h, re.S)
        assert m, n
        body = m.group(2)
        row = lambda lab: re.search(r'<div class="sc-rl">' + lab + r'</div><div class="sc-rt">(.*?)</div></div>', body, re.S).group(1)
        mv = re.search(r'<div class="sc-fac">&#10148; ([^:]+): (.*?)</div>', body, re.S)
        out.append({'n': n, 'q': m.group(1), 'is': row('What It Is'), 'weak': row('Weak'), 'clear': row('Clear'), 'mv_l': mv.group(1), 'mv': mv.group(2)})
    return out

def guide_ace(h):
    """The five behaviours as part 1.3.4 gives them on this page: definition, what it does for a new practice, what is observable."""
    out = []
    for n in ACE:
        m = re.search(r'<div class="ai-name">' + n + r'</div></div>.*?<div class="ai-rl">Definition</div><div class="ai-rt">(.*?)</div></div>.*?<div class="ai-ev">&#10003; Observable: (.*?)</div>', h, re.S)
        t = re.search(r'<tr><td>' + n + r'</td><td>(.*?)</td></tr>', h)
        assert m and t, n
        out.append({'n': n, 'def': m.group(1), 'does': t.group(1), 'obs': m.group(2)})
    return out

# what the group writes
ASK = {'shift': 'What is changing?',
       'stake': 'What will the organisation gain if it changes, and what will it lose if it stays as it is?',
       'step': 'What must be done differently?'}
PH = {'shift': 'The practice that stops and the practice that starts, for whom and from when...',
      'stake': 'The gain from changing and the loss from staying as you are, in terms the people affected care about...',
      'step': 'What each group affected does differently, said in the first person...',
      'accountability': 'For example: one named leader owns the new practice and reports its result at every review...',
      'commitment': 'For example: the leadership team keeps the new practice in a busy month and declines work that pulls against it...',
      'engagement': 'For example: every leader asks their team how the change is going, and brings the answers to the leadership meeting...',
      'integrity': 'For example: a leader who misses a commitment says so first, with the fix...',
      'transparency': 'For example: progress and setbacks on the change are shown to everyone it affects...'}
ACE_ASK = 'The behaviour we expect from our leadership team'

HERO_P = ('You apply two tools from the 4 Checks to the strategy in your team’s Capstone Blueprint. With the 3S Check your group states the change. '
          'With ACE-IT your group states the leadership behaviours that will hold it in place.')
HERO_F = ('Application &middot; Each group applies two tools from the 4 Checks to the strategy in its Capstone Blueprint. With the 3S Check the group states the change. '
          'With ACE-IT the group states the leadership behaviours that will hold it in place.')
GROUP_P = '<div class="u5-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>\n'

def how_box(page):
    p = page == 'p'
    lead = ('This is group work. Your group builds the case for the change your strategy asks of people, in two steps:' if p else
            'This is group work. Each group builds the case for the change its strategy asks of people, in two steps:')
    steps = ([
        '<strong>Step 1 · The 3S Check.</strong> Your group states three things for the strategy in your Capstone Blueprint: the <strong>Shift</strong> (what is changing), the <strong>Stake</strong> (what the organisation gains if it changes, and what it loses if it stays as it is) and the <strong>Step</strong> (what must be done differently). The guide from part 1.3.1 sits beside each box.',
        '<strong>Step 2 · ACE-IT.</strong> Your group reads its team OCEAVL profile. It then states the behaviour it expects from the leadership team under each of the five ACE-IT behaviours: Accountability, Commitment, Engagement, Integrity and Transparency. The guide from part 1.3.4 sits beside each box.'] if p else [
        '<strong>Step 1 · The 3S Check.</strong> The group states three things for the strategy in its Capstone Blueprint: the <strong>Shift</strong> (what is changing), the <strong>Stake</strong> (what the organisation gains if it changes, and what it loses if it stays as it is) and the <strong>Step</strong> (what must be done differently). The guide from part 1.3.1 sits beside each box.',
        '<strong>Step 2 · ACE-IT.</strong> The group reads its team OCEAVL profile. It then states the behaviour it expects from the leadership team under each of the five ACE-IT behaviours: Accountability, Commitment, Engagement, Integrity and Transparency. The guide from part 1.3.4 sits beside each box.'])
    close = ('You then select Confirm. This is Capstone work, and your confirmed record feeds your team’s Capstone Blueprint.' if p else
             'Each participant then selects Confirm. This is Capstone work, and the confirmed record feeds the team’s Capstone Blueprint.')
    return ('<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div><p>' + lead + '</p><ol>' + ''.join('<li>' + x + '</li>' for x in steps) + '</ol><p>' + close + '</p></div>\n\n')

STEP1_HOW_P = ['Read the practices your strategy starts and stops, shown below. They come from the Start and Stop lists your group confirmed in Unit 3.',
               'Read the guide in each card. It is the lesson from part 1.3.1.',
               'Agree your group’s Shift, Stake and Step for the strategy, and write each one in its box.']
STEP2_HOW_P = ['Read your team’s OCEAVL profile, shown below. It appears once every member of your team has submitted their scores in part 3.1.',
               'Read the guide in each card. It is the lesson from part 1.3.4.',
               'For each behaviour, agree what your group expects to see the leadership team do so that the change in Step 1 holds. Where your team’s level carries a risk for this change, state the behaviour that answers it.',
               'Read your record at the foot of this step, then select Confirm. Select Print for a copy.']
STEP1_ACT_F = ['The group reads the practices the strategy starts and stops. Each page shows the Start and Stop lists the group confirmed in Unit 3.',
               'The group reads the guide in each card. It is the lesson from part 1.3.1.',
               'The group agrees its Shift, Stake and Step for the strategy, and each participant writes them in the three boxes.']
STEP2_ACT_F = ['The group reads its team OCEAVL profile, shown on each page once every member of the team has submitted their scores in part 3.1.',
               'The group reads the guide in each card. It is the lesson from part 1.3.4.',
               'For each behaviour, the group agrees what it expects to see the leadership team do so that the change in Step 1 holds. Where the team’s level carries a risk for this change, the group states the behaviour that answers it.',
               'Each participant reads the record and selects Confirm. Print gives a copy of the record.']
SEC5_GUIDE_F = ['<strong>Order:</strong> Both steps are group work. Step 2 needs the team&rsquo;s OCEAVL profile, so every member completes and submits the assessment in part 3.1 first.',
                '<strong>Facilitation principle:</strong> Test each statement against its guide. A statement that could be said of any organisation has not yet been written for this strategy.']
STEP1_GUIDE_F = ['<strong>Briefing:</strong> Each group works with the Start and Stop lists it confirmed in Unit 3 in view, and states one Shift, one Stake and one Step for its strategy.',
                 '<strong>Watch for:</strong> a Shift written as a direction. Ask what stops, what starts, for whom and from when.',
                 '<strong>Watch for:</strong> a Stake that gives the gain only. Ask what the organisation loses if it stays as it is.',
                 '<strong>Watch for:</strong> a Step written for the organisation. Ask each member to say their own part in the first person.']
STEP2_GUIDE_F = ['<strong>Briefing:</strong> The group opens with its team OCEAVL profile. The profile shows the team&rsquo;s level on each dimension, with its risk and its response.',
                 '<strong>Linking question:</strong> <em>&ldquo;Which level in your team&rsquo;s profile carries the highest risk for this change? Which ACE-IT behaviour answers it?&rdquo;</em>',
                 '<strong>Watch for:</strong> a value written where a behaviour is asked for, such as &ldquo;we will be accountable&rdquo;. Ask what a colleague would see the leadership team do.',
                 '<strong>Watch for:</strong> behaviours expected of staff. The five boxes are for the leadership team&rsquo;s own behaviour.']
TEAM_OC_H = 'Your team&rsquo;s OCEAVL profile'
TEAM_OC_WAIT = 'Your team’s profile appears here once every member has submitted their OCEAVL scores in part 3.1.'
TEAM_OC_NONE = 'Your team’s profile could not be shown here. Read it in your team’s Capstone Blueprint, under Unit 5.'

def card_3s(g, page):
    p = page == 'p'
    k = g['n'].lower()
    s = ('<div class="u5-s5">\n  <div class="u5-s5-h"><span class="u5-s5-n">' + g['n'] + '</span><span class="u5-s5-q">' + g['q'] + '</span></div>\n'
         '  <div class="u5-s5-g"><p><b>What it is</b>' + g['is'] + '</p>\n'
         '  <div class="u5-s5-wc"><div><b>Weak</b>' + g['weak'] + '</div><div><b>Clear</b>' + g['clear'] + '</div></div>\n'
         '  <p><b>' + g['mv_l'] + '</b>' + g['mv'] + '</p></div>\n')
    if p:
        s += ('  <label class="wp-label" for="s5_' + k + '">Your group&rsquo;s ' + g['n'] + ' &middot; ' + ASK[k] + '</label>\n'
              '  <textarea class="wp-ta" id="s5_' + k + '" placeholder="' + PH[k] + '" oninput="s5In(\'' + k + '\',this.value)"></textarea>\n')
    return s + '</div>\n'

def card_ace(g, page):
    p = page == 'p'
    k = g['n'].lower()
    s = ('<div class="u5-s5">\n  <div class="u5-s5-h"><span class="u5-s5-n">' + g['n'] + '</span></div>\n'
         '  <div class="u5-s5-g"><p><b>Definition</b>' + g['def'] + '</p>\n  <p><b>What it does for a new practice</b>' + g['does'] + '</p>\n  <p><b>Observable</b>' + g['obs'] + '</p></div>\n')
    if p:
        s += ('  <label class="wp-label" for="s5_' + k + '">' + g['n'] + ' &middot; ' + ACE_ASK + '</label>\n'
              '  <textarea class="wp-ta" id="s5_' + k + '" placeholder="' + PH[k] + '" oninput="s5In(\'' + k + '\',this.value)"></textarea>\n')
    return s + '</div>\n'

OUTCOME_TAIL_P = 'and a stated Shift, Stake and Step for your strategy, with the leadership behaviours that will hold it in place &mdash;'
OUTCOME_TAIL_F = 'and a stated Shift, Stake and Step for the strategy, with the leadership behaviours that will hold it in place &mdash;'
GUIDE_TAB1_OLD = 'The Section 5 exercise, the Alignment Toolkit, is the centrepiece.</p>'
GUIDE_TAB1_NEW = 'The Section 5 exercise, Leading with Clarity, is the centrepiece.</p>'
GUIDE_TAB_NEW = 'In Section 5 each group applies two of the tools to its own strategy: it states its Shift, Stake and Step, and the ACE-IT behaviours it expects from the leadership team.</p>'
SUMMARY_P5 = ('With your group you applied two tools to the strategy in your Capstone Blueprint. With the 3S Check you stated the Shift (what is changing), the Stake (what the organisation gains if it changes, '
              'and what it loses if it stays as it is) and the Step (what must be done differently). With ACE-IT you read your team’s OCEAVL profile and stated the behaviour you expect from the leadership team '
              'under each of the five behaviours: Accountability, Commitment, Engagement, Integrity and Transparency. Your group’s confirmed record feeds your team’s Capstone Blueprint.')
SUMMARY_F5_H = '5 &mdash; Application: Leading with Clarity'
SUMMARY_F5 = ('Each group applied two tools to the strategy in its Capstone Blueprint. With the 3S Check the group stated the Shift (what is changing), the Stake (what the organisation gains if it changes, '
              'and what it loses if it stays as it is) and the Step (what must be done differently). With ACE-IT the group read its team OCEAVL profile and stated the behaviour it expects from the leadership team '
              'under each of the five behaviours. The confirmed record feeds each team’s Capstone Blueprint.')
CLOSE_Q_OLD = '<em>&ldquo;Which trigger in your team plan is this team most likely to leave to someone else, and which leader has agreed to own it?&rdquo;</em>'
CLOSE_Q_NEW = '<em>&ldquo;Which ACE-IT behaviour in your record will be hardest for this leadership team to show, and what in the team&rsquo;s OCEAVL profile makes it so?&rdquo;</em>'
