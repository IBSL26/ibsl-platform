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
# CSS
rep('.u6-from br+br{display:block;}', '.u6-from br+br{display:block;}\n.u6w-g{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:10px 0 14px;}\n.u6w-c{background:rgba(26,122,106,.08);border:1px solid rgba(26,122,106,.3);border-radius:3px;padding:12px 14px;}\n.u6w-c b{display:block;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#5ecba1;margin-bottom:4px;}\n.u6w-c b span{font-family:"Cormorant Garamond",serif;font-size:22px;letter-spacing:0;color:#c9a84c;margin-right:6px;}\n.u6w-c p{font-size:12.5px!important;line-height:1.65!important;color:rgba(255,255,255,.75)!important;margin:0!important;}\n.u6w-ex p{font-size:12.5px!important;line-height:1.7!important;margin:0 0 6px!important;}\n.u6w-ex p b{color:#fff;}\n@media(max-width:640px){.u6w-g{grid-template-columns:1fr;}}')
# Hero, How Section 5 works
rep('<p>Your group builds two connected components of the Enterprise Performance Management System for the strategy in your team&rsquo;s Capstone Blueprint: the S2R® Contribution Map™ and the FACES application.</p>',
    '<p>Your group builds three connected components of the Enterprise Performance Management System for the strategy in your team&rsquo;s Capstone Blueprint: the S2R® Contribution Map™, the FACES application and the WARD check-up for its enterprise Key Result.</p>')
rep('In this application, your group uses that work to develop two connected components of your Enterprise Performance Management System:', 'In this application, your group uses that work to develop three connected components of your Enterprise Performance Management System:')
rep('<li><strong>5.2 &middot; Activity 2 &middot; FACES Application.</strong> Establish how these contributions will be aligned, measured, managed and continuously improved.</li>',
    '<li><strong>5.2 &middot; Activity 2 &middot; FACES Application.</strong> Establish how these contributions will be aligned, measured, managed and continuously improved.</li><li><strong>5.3 &middot; Activity 3 &middot; WARD Check-up.</strong> Establish when your enterprise Key Result is checked, which result raises a red flag, what recovery follows and who decides.</li>')
import re
m = re.search(r'When both activities are complete', t); assert m
rep('When both activities are complete', 'When all three activities are complete')
# Tabs
rep('<div class="step-tab" onclick="u6Step(1)"><div class="step-num">5.2 &middot; Activity 2</div><div class="step-name">FACES Application</div></div></div>',
    '<div class="step-tab" onclick="u6Step(1)"><div class="step-num">5.2 &middot; Activity 2</div><div class="step-name">FACES Application</div></div><div class="step-tab" onclick="u6Step(2)"><div class="step-num">5.3 &middot; Activity 3</div><div class="step-name">WARD Check-up</div></div></div>')
# Activity 2 end: go on to Activity 3
rep('<li>Read the completion check, then read your group&rsquo;s record and select Agree.</li></ol></div>\n<div class="u6-from" id="u6KrShow2"></div>',
    '<li>Read the completion check, then go to Activity 3.</li></ol></div>\n<div class="u6-from" id="u6KrShow2"></div>')
hb = '<div class="hbox"><p>The S2R® Contribution Map™ establishes the contributions required to achieve an enterprise result.<br>FACES establishes how those contributions will be managed across the organisation.<br>Together, they connect enterprise strategy to functional performance, human contribution, organisational enablement and collective accountability.</p></div>\n</div>\n<div id="u6Rec"></div>'
cards = ''.join('<div class="u6w-c"><b><span>%s</span>%s</b><p>%s</p></div>' % (l, n, e(d)) for l, n, d in WARD)
ex = ''.join('<p><b>%s:</b> %s</p>' % (e(a), e(b)) for a, b in EX)
def wp(n, opt):
    lab = 'Waypoint %d%s' % (n, ' (optional)' if opt else '')
    return ('<div class="u6-s5"><div class="u6-s5-h"><span class="u6-s5-n">W &middot; %s</span></div><div class="u6-g2">'
            '<div><label class="wp-label" for="u6_wd_w%dd">Date</label><input class="u6-in" type="text" id="u6_wd_w%dd" data-u6="wd_w%dd" placeholder="The date of the check, for example 31 March 2027"></div>'
            '<div><label class="wp-label" for="u6_wd_w%dl">Level</label><input class="u6-in" type="text" id="u6_wd_w%dl" data-u6="wd_w%dl" placeholder="The level the Key Result must have reached by that date"></div></div></div>') % (lab, n, n, n, n, n, n)
def ta(i, lab, ph):
    return '<div class="u6-g1"><div><label class="wp-label" for="u6_wd_%s">%s</label><textarea class="wp-ta" id="u6_wd_%s" data-u6="wd_%s" placeholder="%s" style="min-height:70px;"></textarea></div></div>' % (i, lab, i, i, ph)
panel = ('\n<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Step(2)">Continue to Activity 3 &rarr;</button></div>\n</div>\n'
 '<div class="step-panel" id="u6sp3">\n'
 '<div class="u6-h" style="margin-top:4px;">5.3 &mdash; Activity 3: WARD &middot; Your Key Result&rsquo;s Vital Check-up</div>\n'
 '<div class="u6-group"><strong>Working as a group.</strong> Your group chooses its scribe for this work in the group record bar. The scribe types what your group agrees, and the entries appear on every member&rsquo;s page.</div>\n'
 '<p>' + e(INTRO) + '</p>\n'
 '<div class="u6w-g">' + cards + '</div>\n'
 '<div class="u6-h">WARD in the worked example</div>\n'
 '<div class="u6-from u6w-ex"><b>Enterprise Key Result &middot; part 4.1</b><p>' + e(EX_KR) + '</p>' + ex + '</div>\n'
 '<div class="u6-how"><div class="u6-how-h">Capstone work &middot; How to complete Activity 3</div><ol>'
 '<li><strong>Step 4 &middot; Set your waypoints.</strong> Name two or three dates before the deadline of your enterprise Key Result, and the level it must have reached by each.</li>'
 '<li><strong>Step 5 &middot; Set your alert.</strong> State how far off a waypoint the result can be before it raises a red flag.</li>'
 '<li><strong>Step 6 &middot; Set the recovery.</strong> State the corrective action for the individuals and for the organisational conditions, using the functions and conditions in your Contribution Map.</li>'
 '<li><strong>Step 7 &middot; Name the decider.</strong></li>'
 '<li>Read the completion check, then read your group&rsquo;s record and select Agree.</li></ol></div>\n'
 '<div class="u6-from" id="u6KrShow3"></div>\n'
 + wp(1, False) + wp(2, False) + wp(3, True) +
 '\n<div class="u6-s5"><div class="u6-s5-h"><span class="u6-s5-n">A &middot; Alert</span></div>' + ta('alert', 'Alert', 'How far off a waypoint can the result be before it raises a red flag?') + '</div>'
 '\n<div class="u6-s5"><div class="u6-s5-h"><span class="u6-s5-n">R &middot; Recovery</span></div>' + ta('rec_i', 'Recovery &middot; individuals', 'What corrective action follows a red flag for the individuals delivering the Key Result?') + ta('rec_o', 'Recovery &middot; organisational conditions', 'What corrective action follows a red flag for the organisational conditions, and who restores them?') + '</div>'
 '\n<div class="u6-s5"><div class="u6-s5-h"><span class="u6-s5-n">D &middot; Decider</span></div><div><label class="wp-label" for="u6_wd_dec">Decider</label><input class="u6-in" type="text" id="u6_wd_dec" data-u6="wd_dec" placeholder="The executive who decides on the recovery and sees it through"></div></div>\n'
 '<div class="u6-how"><div class="u6-how-h">Completion check</div><p>Before you agree, check that:</p><ol class="u6-list"><li>Each waypoint has a date and a level, and the waypoints lead to the target by the deadline.</li><li>The alert is specific enough that every member reads the same result the same way.</li><li>The recovery covers the individuals and the organisational conditions named in your Contribution Map.</li><li>One executive is named as the decider.</li></ol><p><strong>Output 3:</strong> your WARD check-up.</p></div>\n'
 '<div class="hbox"><p>The S2R® Contribution Map™ establishes the contributions required to achieve an enterprise result.<br>FACES establishes how those contributions will be managed across the organisation.<br>WARD sets when the enterprise Key Result is checked, which result raises a red flag and what recovery follows.<br>Together, they connect enterprise strategy to functional performance, human contribution, organisational enablement and collective accountability.</p></div>\n'
 '</div>\n<div id="u6Rec"></div>')
rep(hb, panel)
# Summary
rep('Your group built an S2R® Contribution Map™ for one of its own enterprise Key Results and applied FACES to manage each function&rsquo;s contribution. The agreed record feeds your team&rsquo;s Capstone Blueprint.',
    'Your group built an S2R® Contribution Map™ for one of its own enterprise Key Results, applied FACES to manage each function&rsquo;s contribution and set the WARD check-up for the Key Result. The agreed record feeds your team&rsquo;s Capstone Blueprint.')
# ── Script ──
rep("var U6P=[['map','S2R® Contribution Map™','Enterprise PM System · Contribution Map','cm_map'],['faces','FACES Application','Enterprise PM System · FACES Application','cm_faces']];",
    "var U6P=[['map','S2R® Contribution Map™','Enterprise PM System · Contribution Map','cm_map'],['faces','FACES Application','Enterprise PM System · FACES Application','cm_faces'],['ward','WARD Check-up','Enterprise PM System · WARD','cm_ward']];\n/* Activity 3 · WARD (20 Oct 2026): waypoints, alert, recovery, decider for the enterprise Key Result. Waypoint 3 is optional. */\nvar U6_WARD=[['wd_w1d'],['wd_w1l'],['wd_w2d'],['wd_w2l'],['wd_w3d'],['wd_w3l'],['wd_alert','A · Alert'],['wd_rec_i','R · Recovery · individuals'],['wd_rec_o','R · Recovery · organisational conditions'],['wd_dec','D · Decider']];")
rep("U6_FACES.forEach(function(f){a.push('f'+n+'_'+f[0]);});}return a;})();",
    "U6_FACES.forEach(function(f){a.push('f'+n+'_'+f[0]);});}U6_WARD.forEach(function(f){a.push(f[0]);});return a;})();")
rep("function u6Text(part){\n  var out=[];",
    "function u6wpUsed(n){return n<3||!!u6val('wd_w'+n+'d')||!!u6val('wd_w'+n+'l');}\nfunction u6Text(part){\n  var out=[];\n  if(part==='ward'){\n    out.push('Enterprise Key Result: '+u6val('kr'));\n    for(var w=1;w<=3;w++){if(u6wpUsed(w))out.push('W · Waypoint '+w+': '+[u6val('wd_w'+w+'d'),u6val('wd_w'+w+'l')].filter(function(x){return x;}).join(' · '));}\n    U6_WARD.slice(6).forEach(function(f){out.push(f[1]+': '+u6val(f[0]));});\n    return out.join('\\n');\n  }")
rep("['u6KrShow','u6KrShow2'].forEach", "['u6KrShow','u6KrShow2','u6KrShow3'].forEach")
rep("    if(q)open.push('Activity 2 · '+u6fnName(k)+' ('+q+(q===1?' FACES box':' FACES boxes')+' still open)');\n  }\n  return open;",
    "    if(q)open.push('Activity 2 · '+u6fnName(k)+' ('+q+(q===1?' FACES box':' FACES boxes')+' still open)');\n  }\n  var wq=0;for(var w=1;w<=3;w++){if(u6wpUsed(w)){if(!u6val('wd_w'+w+'d'))wq++;if(!u6val('wd_w'+w+'l'))wq++;}}\n  U6_WARD.slice(6).forEach(function(f){if(!u6val(f[0]))wq++;});\n  if(wq)open.push('Activity 3 · WARD ('+wq+(wq===1?' entry':' entries')+' still open)');\n  return open;")
rep("    U6P.map(function(p,i){\n      var rows=[],done=0,total=0;",
    "    U6P.map(function(p,i){\n      var rows=[],done=0,total=0;\n      if(p[0]==='ward'){\n        u6Text('ward').split('\\n').forEach(function(l){var c=l.indexOf(': '),a=l.slice(0,c),b=l.slice(c+2).trim();total++;if(b)done++;rows.push('<div class=\"u6-rec-t\"><strong>'+u6esc(a)+':</strong> '+(b?u6esc(b):'<i>to be agreed by your group</i>')+'</div>');});\n        return '<details class=\"u6-rec\"><summary>5.'+(i+1)+' &middot; '+u6esc(p[1])+'<span>'+done+' of '+total+' entries</span></summary>'+rows.join('')+'</details>';\n      }")
assert t.count('u6_wd_') >= 20
out = t.replace('\n', '\r\n') if crlf else t
open(F, 'wb').write(out.encode('utf-8'))
print('u6p ok')
