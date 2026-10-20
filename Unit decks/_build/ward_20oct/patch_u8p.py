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
assert 'u8W' not in t
rep('<p>Your group sets two decision points against each of the four consequences of weak review discipline, for the strategy in your team&rsquo;s Capstone Blueprint.</p>',
    '<p>Your group sets two decision points against each of the four consequences of weak review discipline, for the strategy in your team&rsquo;s Capstone Blueprint. It then tests the WARD check-up it set in Unit 6.</p>')
rep('<li>Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.</li></ol><p>Your group chooses its scribe',
    '<li>Writes a decision point for recovery for each gap: the decision the executive team takes when the gap appears, and who takes it.</li></ol><p>In part 5.2 your group tests the WARD check-up it set for its enterprise Key Result in Unit 6: the alert fires, and your group runs the recovery.</p><p>Your group chooses its scribe')
ex = ''.join('<p><b>%s</b>%s</p>' % (e(a), e(b)) for a, b in EX8)
fields = [('c5_flag', 'The red flag &middot; the waypoint and the result that raises the alert', 'At [waypoint], the result is [result] against [level]...'),
          ('c5_ind', 'Individuals &middot; what explains the gap', 'What the evidence shows about the individuals delivering the Key Result...'),
          ('c5_org', 'Organisational conditions &middot; what explains the gap', 'What the evidence shows about the organisational conditions named in your Contribution Map...'),
          ('c5_rec', 'The recovery &middot; what is done, who decides and when the result is checked again', 'For the individuals: ... For the organisational conditions: ... Decided by ... Checked again on ...')]
fh = ''.join('<label class="wp-label" for="u8_%s">%s</label><textarea class="wp-ta" id="u8_%s" data-u8="%s" placeholder="%s" style="min-height:80px;"></textarea>' % (i, l, i, i, p) for i, l, p in fields)
block = ('</div></div></div>\n'
 '<div class="acc open">\n'
 '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">5.2 &mdash; Testing Your WARD</div><div class="acc-meta">Capstone Work</div></div><div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div></div>\n'
 '<div class="acc-b"><div class="cb">\n'
 '<div class="u8-group"><strong>Working as a group.</strong> Your group chooses its scribe for this work in the group record bar. The scribe types what your group agrees, and the entries appear on every member&rsquo;s page.</div>\n'
 '<div id="u8W">\n'
 '<p>In Unit 6 your group set the WARD check-up for its enterprise Key Result: the waypoints, the alert, the recovery and the decider. Here the check-up takes place. At one of your waypoints the result falls beyond the alert and raises a red flag, and your group runs the recovery as the executive team would at that review.</p>\n'
 '<div class="u8-how"><div class="u8-how-h">Capstone work &middot; How to complete part 5.2</div><ol>'
 '<li>Check that your group&rsquo;s WARD from Unit 6 is shown below. If it is missing, select Bring in from my Unit 6 page.</li>'
 '<li>Simulate the red flag: choose one waypoint and write the result your executive team reads at that review, beyond the alert.</li>'
 '<li>Using your Contribution Map, state what explains the gap in the performance of individuals and in the organisational conditions.</li>'
 '<li>State the recovery your group runs: what is done, who decides and when the result is checked again.</li>'
 '<li>Read your group&rsquo;s record, then select Agree.</li></ol></div>\n'
 '<div class="u8-h">Your group&rsquo;s WARD &middot; from Unit 6</div>\n'
 '<div class="u8-from" id="u8WardShow"><i>Your group&rsquo;s WARD appears here.</i></div>\n'
 '<div class="u8-btnrow"><button type="button" class="u8-b" onclick="u8WardBring(true)">Bring in from my Unit 6 page</button></div>\n'
 '<div class="u8-note" id="u8WardMsg" style="display:none;"></div>\n'
 '<div class="u8-h">An example from the Unit 6 worked example</div>\n'
 '<div class="u8-s5-g"><p><b>Enterprise Key Result</b>' + e(EX_KR) + ' Waypoint: 80% by the end of June. Alert: more than three percentage points below a waypoint.</p>' + ex + '</div>\n'
 '<div class="u8-s5">\n  <div class="u8-s5-h"><span class="u8-s5-n">Your WARD test</span></div>\n  ' + fh + '\n</div>\n'
 '</div>\n'
 '</div></div></div>\n<div id="u8Rec"></div>')
rep('</div></div></div>\n<div id="u8Rec"></div>', block)
# script
rep('["c4_dp2", "Organisational conditions", "c4", "", "t", "If [the gap appears], then [the recovery decision], taken by [who]..."]];',
    '["c4_dp2", "Organisational conditions", "c4", "", "t", "If [the gap appears], then [the recovery decision], taken by [who]..."], ["c5_flag", "The red flag", "c5", "", "t", ""], ["c5_ind", "Individuals · what explains the gap", "c5", "", "t", ""], ["c5_org", "Organisational conditions · what explains the gap", "c5", "", "t", ""], ["c5_rec", "The recovery", "c5", "", "t", ""]];')
rep('["c4", "Leadership Credibility", "Review Discipline · Leadership Credibility", "rd_credibility", "Consequence 4 · Erodes Leadership Credibility"]];',
    '["c4", "Leadership Credibility", "Review Discipline · Leadership Credibility", "rd_credibility", "Consequence 4 · Erodes Leadership Credibility"], ["c5", "WARD Test", "Review Discipline · WARD Test", "rd_ward", "5.2 · Testing Your WARD"]];')
rep("  u8Fill();u8RecDraw();\n  twAttach();", "  u8Fill();u8RecDraw();u8WardBring(false);\n  twAttach();")
rep("""  var root=u8el('u8S5');
  if(root){""", """  ['u8S5','u8W'].forEach(function(rid){var root=u8el(rid);
  if(root){""")
rep("""    root.addEventListener('change',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u8');if(id&&ev.target.tagName==='SELECT')u8In(id,ev.target.value);});
  }
  u8Fill();u8RecDraw();""", """    root.addEventListener('change',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u8');if(id&&ev.target.tagName==='SELECT')u8In(id,ev.target.value);});
  }});
  u8Fill();u8RecDraw();""")
rep("/* Part 3.2 · the CXO cards */", """/* Part 5.2 · the group's WARD from its own Unit 6 page (read only; 20 Oct 2026). */
async function u8WardBring(manual){
  var host=u8el('u8WardShow');if(!host)return;
  if(!window.S2R){if(manual)u8msg('u8WardMsg','The save system is not ready. Reload the page and try again.');return;}
  var u6={};try{u6=await S2R.loadAll('u3m1_lens5');}catch(e){u6={};}
  var w=u6&&typeof u6.cm_ward==='string'?u6.cm_ward.trim():'',conf=(u6&&Array.isArray(u6.confirmed_items))?u6.confirmed_items:[];
  if(!w||conf.indexOf('Enterprise PM System · WARD')<0){
    host.innerHTML='<i>Your group&rsquo;s WARD appears here.</i>';
    u8msg('u8WardMsg','No agreed WARD was found on your Unit 6 page. Agree your group’s WARD in Unit 6, part 5.3, then select Bring in from my Unit 6 page.');
    return;
  }
  host.innerHTML=w.split('\\n').map(function(l){var i=l.indexOf(': ');return i>0?'<b>'+u8esc(l.slice(0,i))+'</b>'+u8esc(l.slice(i+2)):u8esc(l);}).join('');
  u8msg('u8WardMsg',manual?'Brought in from your Unit 6 page.':'',manual?'ok':'');
}

/* Part 3.2 · the CXO cards */""")
rep('your group simulated a potential gap in the performance of individuals and in the organisational conditions of the strategy in your team\\u2019s Capstone Blueprint, and set a decision point for recovery for each: the decision the executive team takes when the gap appears, and who takes it."',
    'your group simulated a potential gap in the performance of individuals and in the organisational conditions of the strategy in your team\\u2019s Capstone Blueprint, and set a decision point for recovery for each: the decision the executive team takes when the gap appears, and who takes it. Your group then tested the WARD check-up it set in Unit 6: the alert fired, and your group ran the recovery."')
out = t.replace('\n', '\r\n') if crlf else t
open(F, 'wb').write(out.encode('utf-8'))
print('u8p ok')
