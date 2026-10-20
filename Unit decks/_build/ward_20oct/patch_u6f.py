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
assert 'u6sp3' not in t
anchor = [l for l in t.split('\n') if l.startswith('.step-tab.active .step-name')][0]
rep(anchor, anchor + '\n.u6w-g{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:10px 0 14px;}\n.u6w-c{background:rgba(26,122,106,.08);border:1px solid rgba(26,122,106,.3);border-radius:3px;padding:12px 14px;}\n.u6w-c b{display:block;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#5ecba1;margin-bottom:4px;}\n.u6w-c b span{font-family:"Cormorant Garamond",serif;font-size:22px;letter-spacing:0;color:#c9a84c;margin-right:6px;}\n.u6w-c p{font-size:12.5px!important;line-height:1.65!important;color:rgba(255,255,255,.75)!important;margin:0!important;}\n.u6w-ex p{font-size:12.5px!important;line-height:1.7!important;margin:0 0 6px!important;}\n@media(max-width:640px){.u6w-g{grid-template-columns:1fr;}}')
rep('<p>Application &middot; Each group builds two connected components of the Enterprise Performance Management System for the strategy in its Capstone Blueprint: the S2R® Contribution Map™ and the FACES application.</p>',
    '<p>Application &middot; Each group builds three connected components of the Enterprise Performance Management System for the strategy in its Capstone Blueprint: the S2R® Contribution Map™, the FACES application and the WARD check-up for its enterprise Key Result.</p>')
rep('<p><strong>Order:</strong> both activities are group work and Capstone work. Activity 1 needs the group&rsquo;s confirmed Enterprise OKRs from Unit 3, part 5.2. Activity 2 uses the business functions the group names in Activity 1.</p>',
    '<p><strong>Order:</strong> all three activities are group work and Capstone work. Activity 1 needs the group&rsquo;s confirmed Enterprise OKRs from Unit 3, part 5.2. Activity 2 uses the business functions the group names in Activity 1. Activity 3 sets the WARD check-up for the Key Result chosen in Activity 1, using the conditions named in the Contribution Map.</p>')
rep('In this application, the group uses that work to develop two connected components of its Enterprise Performance Management System:', 'In this application, the group uses that work to develop three connected components of its Enterprise Performance Management System:')
rep('<li><strong>5.2 &middot; Activity 2 &middot; FACES Application.</strong> Establish how these contributions will be aligned, measured, managed and continuously improved.</li>',
    '<li><strong>5.2 &middot; Activity 2 &middot; FACES Application.</strong> Establish how these contributions will be aligned, measured, managed and continuously improved.</li><li><strong>5.3 &middot; Activity 3 &middot; WARD Check-up.</strong> Establish when the enterprise Key Result is checked, which result raises a red flag, what recovery follows and who decides.</li>')
old_tab = '<div class="step-tab" onclick="u6Step(1)"><div class="step-num">5.2 &middot; Activity 2</div><div class="step-name">FACES Application</div></div></div>'
rep(old_tab, old_tab[:-6] + '<div class="step-tab" onclick="u6Step(2)"><div class="step-num">5.3 &middot; Activity 3</div><div class="step-name">WARD Check-up</div></div></div>')
rep('<li>The group reads the completion check.</li><li>Each participant reads the record and selects Agree. Print gives a copy.</li></ol><p>The agreed record feeds the team&rsquo;s Capstone Blueprint.</p></div>\n</div>',
    '<li>The group reads the completion check, then goes to Activity 3.</li></ol></div>\n</div>\nNEWPANEL')
old_hb = '<div class="hbox"><p>The S2R® Contribution Map™ establishes the contributions required to achieve an enterprise result.<br>FACES establishes how those contributions will be managed across the organisation.<br>Together, they connect enterprise strategy to functional performance, human contribution, organisational enablement and collective accountability.</p></div>\n'
rep(old_hb, '')
cards = ''.join('<div class="u6w-c"><b><span>%s</span>%s</b><p>%s</p></div>' % (l, n, e(d)) for l, n, d in WARD)
ex = ''.join('<p><b>%s:</b> %s</p>' % (e(a), e(b)) for a, b in EX)
panel = ('<div class="step-panel" id="u6sp3">\n'
 '<div class="u6-h" style="margin-top:4px;">5.3 &mdash; Activity 3: WARD &middot; Your Key Result&rsquo;s Vital Check-up</div>\n'
 '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; Activity 3</div>'
 '<p><strong>Open with the check-up.</strong> Say: &ldquo;' + e(INTRO_F.replace('the group', 'your group').replace('for the Key Result', 'for your Key Result')) + '&rdquo;</p>'
 '<p><strong>Teach WARD from the worked example.</strong> Take the Key Result from part 4.1 through the four letters. Ask: &ldquo;At the end of June the result is 74%. What happens on Monday morning, and who decides?&rdquo; Guide the groups to see that the waypoint, the alert and the recovery answer the question before the review takes place.</p>'
 '<p><strong>Briefing:</strong> each group sets two or three waypoints for its enterprise Key Result, the alert, the recovery for the individuals and for the organisational conditions named in its Contribution Map, and the decider. In Unit 8 the groups test their WARD: the alert fires and they run the recovery.</p></div>\n'
 '<p>' + e(INTRO_F) + '</p>\n'
 '<div class="u6w-g">' + cards + '</div>\n'
 '<div class="u6-h">WARD in the worked example</div>\n'
 '<div class="u6-from u6w-ex"><b>Enterprise Key Result &middot; part 4.1</b><p>' + e(EX_KR) + '</p>' + ex + '</div>\n'
 '<div class="u6t-cap">The template on each participant&rsquo;s page (Enterprise Key Result shown from Activity 1)</div>'
 '<div class="u6t-wrap"><table class="u6t"><thead><tr><th>Field</th><th>What to enter</th></tr></thead><tbody>'
 '<tr><td><strong>W &middot; Waypoints 1 and 2 (3 optional)</strong></td><td>The date of each check before the deadline, and the level the Key Result must have reached by that date.</td></tr>'
 '<tr><td><strong>A &middot; Alert</strong></td><td>How far off a waypoint the result can be before it raises a red flag.</td></tr>'
 '<tr><td><strong>R &middot; Recovery &middot; individuals</strong></td><td>The corrective action for the individuals delivering the Key Result.</td></tr>'
 '<tr><td><strong>R &middot; Recovery &middot; organisational conditions</strong></td><td>The corrective action for the organisational conditions, and who restores them.</td></tr>'
 '<tr><td><strong>D &middot; Decider</strong></td><td>The executive who decides on the recovery and sees it through.</td></tr></tbody></table></div>\n'
 '<div class="u6-how"><div class="u6-how-h">Completion check</div><p>Before confirming, the group checks that:</p><ol class="u6-list"><li>Each waypoint has a date and a level, and the waypoints lead to the target by the deadline.</li><li>The alert is specific enough that every member reads the same result the same way.</li><li>The recovery covers the individuals and the organisational conditions named in the Contribution Map.</li><li>One executive is named as the decider.</li></ol></div>\n'
 '<div class="hbox"><p>The S2R® Contribution Map™ establishes the contributions required to achieve an enterprise result.<br>FACES establishes how those contributions will be managed across the organisation.<br>WARD sets when the enterprise Key Result is checked, which result raises a red flag and what recovery follows.<br>Together, they connect enterprise strategy to functional performance, human contribution, organisational enablement and collective accountability.</p></div>\n'
 '<div class="fac-note-full u6-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div><p>Participants work as a group, in Activity 3 of their own file. This is Capstone work. The group chooses its scribe for this work. The scribe types what the group agrees, and the entries appear on every member&rsquo;s page.</p><ol class="u6-list"><li>The group sets two or three waypoints for its enterprise Key Result: a date and a level for each.</li><li>The group sets the alert, the recovery for the individuals and for the organisational conditions, and the decider.</li><li>The group reads the completion check.</li><li>Each participant reads the record and selects Agree. Print gives a copy.</li></ol><p>The agreed record feeds the team&rsquo;s Capstone Blueprint.</p></div>\n'
 '</div>')
rep('NEWPANEL', panel)
out = t.replace('\n', '\r\n') if crlf else t
open(F, 'wb').write(out.encode('utf-8'))
print('u6f ok')
# summary (appended)
raw = open(F, 'rb').read(); t = raw.decode('utf-8').replace('\r\n', '\n')
rep('Each group built an S2R® Contribution Map™ for one of its own enterprise Key Results and applied FACES to manage each function&rsquo;s contribution.',
    'Each group built an S2R® Contribution Map™ for one of its own enterprise Key Results, applied FACES to manage each function&rsquo;s contribution and set the WARD check-up for the Key Result.')
out = t.replace('\n', '\r\n') if crlf else t
open(F, 'wb').write(out.encode('utf-8')); print('u6f summary ok')
