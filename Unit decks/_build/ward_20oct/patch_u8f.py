# -*- coding: utf-8 -*-
import sys, html as H
sys.path.insert(0, '.')
from ward_text import *
F = sys.argv[1]
raw = open(F, 'rb').read(); crlf = b'\r\n' in raw
t = raw.decode('utf-8').replace('\r\n', '\n')
def rep(old, new, n=1):
    global t
    c = t.count(old); assert c == n, (c, old[:90]); t = t.replace(old, new)
e = lambda s: H.escape(s, quote=False).replace("’", "&rsquo;")
assert 'Testing Your WARD' not in t
rep('<p>Each group sets two decision points against each of the four consequences of weak review discipline, for the strategy in its team&rsquo;s Capstone Blueprint.</p>',
    '<p>Each group sets two decision points against each of the four consequences of weak review discipline, for the strategy in its team&rsquo;s Capstone Blueprint. It then tests the WARD check-up it set in Unit 6.</p>')
rep('<p>The groups apply the four consequences to the strategy in their Capstone Blueprint. For each consequence, they simulate a potential gap in the performance of individuals and in the organisational conditions, and write a decision point for recovery for each.</p>',
    '<p>The groups apply the four consequences to the strategy in their Capstone Blueprint. For each consequence, they simulate a potential gap in the performance of individuals and in the organisational conditions, and write a decision point for recovery for each.</p>\n<p>In part 5.2 they test the WARD check-up they set in Unit 6. Say: &ldquo;Your WARD was set while the Key Result was on track. Today the alert fires. Run the recovery as your executive team would at that review.&rdquo;</p>')
rep('<li>Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.</li></ol><p>The group chooses its scribe',
    '<li>Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.</li></ol><p>In part 5.2 each group tests the WARD check-up it set for its enterprise Key Result in Unit 6: the alert fires, and the group runs the recovery.</p><p>The group chooses its scribe')
ex = ''.join('<p><b>%s</b>%s</p>' % (e(a), e(b)) for a, b in EX8)
old = ('<p>Participants work as a group in part 5.1 of their own file. This is Capstone work. The group chooses its scribe for this work. The scribe types what the group agrees, and the entries appear on every member&rsquo;s page.</p>\n</div>\n</div></div>')
new = ('<p>Participants work as a group in part 5.1 of their own file. This is Capstone work. The group chooses its scribe for this work. The scribe types what the group agrees, and the entries appear on every member&rsquo;s page.</p>\n</div>\n</div></div>\n'
 '<div class="acc open">\n'
 '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">5.2 &mdash; Testing Your WARD</div><div class="acc-meta">Capstone Work</div></div><div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div></div>\n'
 '<div class="acc-b"><div class="cb">\n'
 '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; Part 5.2</div>'
 '<p><strong>Recall the check-up.</strong> Ask each group to read its WARD from Unit 6: the waypoints, the alert, the recovery and the decider.</p>'
 '<p><strong>Fire the alert.</strong> Each group chooses one waypoint and writes the result its executive team reads at that review, beyond the alert.</p>'
 '<p><strong>Run the recovery.</strong> Ask: &ldquo;What explains the gap in the individuals and in the organisational conditions? Which recovery do you run, who decides, and when do you check the result again?&rdquo; Guide the groups to use the evidence in their Contribution Map and the recovery they set in advance.</p></div>\n'
 '<div class="u8-h">What participants see</div>\n'
 '<p>Each participant&rsquo;s page shows the group&rsquo;s agreed WARD from its Unit 6 page, read only, with an example from the Unit 6 worked example.</p>\n'
 '<div class="u8-s5-g"><p><b>Enterprise Key Result</b>' + e(EX_KR) + ' Waypoint: 80% by the end of June. Alert: more than three percentage points below a waypoint.</p>' + ex + '</div>\n'
 '<div class="u8-h">What each group completes</div>\n'
 '<ul class="u8-list"><li>The red flag: the waypoint and the result that raises the alert.</li><li>What explains the gap in the performance of individuals and in the organisational conditions.</li><li>The recovery: what is done, who decides and when the result is checked again.</li></ul>\n'
 '<div class="fac-note-full u8-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n'
 '<p>Participants work as a group in part 5.2 of their own file. This is Capstone work, typed by the group&rsquo;s scribe. Each participant then reads the record and selects Agree. When every member has agreed, the record feeds the team&rsquo;s Capstone Blueprint.</p>\n</div>\n</div></div></div>')
rep(old, new)
rep('each group simulated a potential gap in the performance of individuals and in the organisational conditions of its own strategy, and set a decision point for recovery for each. The agreed record feeds the team’s Capstone Blueprint.',
    'each group simulated a potential gap in the performance of individuals and in the organisational conditions of its own strategy, and set a decision point for recovery for each. Each group then tested the WARD check-up it set in Unit 6: the alert fired, and the group ran the recovery. The agreed record feeds the team’s Capstone Blueprint.')
out = t.replace('\n', '\r\n') if crlf else t
open(F, 'wb').write(out.encode('utf-8'))
print('u8f ok')
