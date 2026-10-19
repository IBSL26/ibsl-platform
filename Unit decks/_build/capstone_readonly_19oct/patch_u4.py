# -*- coding: utf-8 -*-
"""Unit 4 participant page: new part 5.3 Verification Ownership and Executive Blind Spots (Capstone 4E, 4F). 19 Oct 2026."""
import sys
src,out=sys.argv[1:3]
s=open(src,encoding='utf-8',newline='').read(); CR='\r\n' in s; s=s.replace('\r\n','\n')
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:90]); s=s.replace(a,b)
ARR='<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div>'
# 5.2 how-to: the last step points to 5.3; Agree moves to 5.3
once('<li>Read your record, then select Agree. Select Print for a copy.</li></ol></div>\n  <div class="u4-btnrow" style="margin:0 0 14px;"><button type="button" class="u4-b" onclick="mbBring(true)">',
     '<li>When every Key Result has been taken through the four steps, go on to 5.3.</li></ol></div>\n  <div class="u4-btnrow" style="margin:0 0 14px;"><button type="button" class="u4-b" onclick="mbBring(true)">')
once('  <div id="mbToolP"></div>\n  <div id="mbOutP"></div>\n</div>\n</div>\n',
'''  <div id="mbToolP"></div>
</div>
</div>

<div class="acc">
<div class="acc-h" onclick="tA(this)">
  <span class="acc-t">5.3 &mdash; Verification Ownership and Executive Blind Spots</span>
  <div style="display:flex;align-items:center;gap:10px;"><span class="acc-meta">Capstone Work</span>'''+ARR+'''</div>
</div>
<div class="acc-b cb">
  <p>Each Must-Be-True condition your group named in 5.2 holds only while someone checks it. In this part your group assigns each check to an executive and names the checkpoint your executive team is most likely to overlook.</p>
  <div class="u4-how"><div class="u4-how-h">Capstone work &middot; How to complete</div><ol><li>Read your group&rsquo;s Must-Be-True conditions from 5.2, listed below.</li><li><strong>Verification ownership.</strong> For each critical Must-Be-True condition, name the executive accountable for verifying it, the evidence that will confirm it still holds, and the date of the first check.</li><li><strong>Executive blind spot.</strong> Select the checkpoint your executive team is most likely to overlook, given the roles around your table, and state the enterprise risk if it does.</li><li>Read your record, then select Agree. Select Print for a copy.</li></ol></div>
  <div id="mbVerP"></div>
  <div id="mbOutP"></div>
</div>
</div>
''')
# JS
once("var MB={step:0,items:[],cur:[0,0]};","var MB={step:0,items:[],cur:[0,0],ver:{},blind:{cp:'',risk:''}};")
once("var MB_KEYS=['mbt_arena','mbt_bound','mbt_comp','mbt_value'];","var MB_KEYS=['mbt_arena','mbt_bound','mbt_comp','mbt_value'];   // 4A to 4D; 4E mbt_verify and 4F mbt_blind come from 5.3")
once("var MB_NAMES=['MBT · Arena','MBT · Boundaries','MBT · Competition','MBT · Value Proposition'];",
     "var MB_NAMES=['MBT · Arena','MBT · Boundaries','MBT · Competition','MBT · Value Proposition','MBT · Verification Ownership','MBT · Executive Blind Spot'];")
once("  MB.step=(s.step>=0&&s.step<4)?s.step:0;\n}",
     "  MB.step=(s.step>=0&&s.step<4)?s.step:0;\n  MB.ver={};if(s.ver&&typeof s.ver==='object')Object.keys(s.ver).forEach(function(id){var v=s.ver[id]||{};MB.ver[id]={who:String(v.who||''),ev:String(v.ev||''),when:String(v.when||'')};});\n  var b=s.blind||{};MB.blind={cp:String(b.cp||''),risk:String(b.risk||'')};\n}")
once("function mbOpen(){return mbAll().filter(function(x){return !mbKrDone(x.k);});}",
"""function mbOpen(){return mbAll().filter(function(x){return !mbKrDone(x.k);});}
/* ── 5.3 · Verification ownership and the executive blind spot ── */
var MB_CPN={a:'Arena',b:'Boundaries',c:'Competition',v:'Value Proposition'};
function mbConds(){var out=[];mbAll().forEach(function(x){['a','b','c','v'].forEach(function(f){var t=x.k[f].trim();if(t)out.push({id:mbId(x.i,x.j)+'-'+f,kr:mbId(x.i,x.j),cp:MB_CPN[f],t:t});});});return out;}
function mbVerRow(id){return MB.ver[id]||{who:'',ev:'',when:''};}
function mbVerFull(id){var v=mbVerRow(id);return !!(v.who.trim()&&v.ev.trim()&&v.when.trim());}
function mbVerOwned(){return mbConds().filter(function(c){return mbVerFull(c.id);});}
function mbS3Open(){var o=[];if(!mbVerOwned().length)o.push('verification ownership for at least one Must-Be-True condition (5.3)');if(!(MB.blind.cp&&MB.blind.risk.trim()))o.push('the executive blind spot (5.3)');return o;}
function mbVerText(){return mbConds().filter(function(c){var v=mbVerRow(c.id);return v.who.trim()||v.ev.trim()||v.when.trim();}).map(function(c){var v=mbVerRow(c.id);
  return 'Key Result '+c.kr+' · '+c.cp+' · Must-Be-True: '+c.t+'\\n   Executive accountable: '+v.who.trim()+'\\n   Evidence that it still holds: '+v.ev.trim()+'\\n   First check: '+v.when.trim();}).join('\\n\\n');}
function mbBlindText(){return 'Checkpoint most likely to be overlooked: '+MB.blind.cp+'\\nEnterprise risk if it is: '+MB.blind.risk.trim();}
function mbVerHtml(){
  var cs=mbConds();
  if(!cs.length)return '<div class="u4-locked">Your Must-Be-True conditions appear here once your group has named them in 5.2.</div>';
  var h='<div class="u4-egs-h">Verification ownership &middot; your group&rsquo;s Must-Be-True conditions from 5.2</div>'+cs.map(function(c){
    var v=mbVerRow(c.id);
    return '<div class="u4-ver"><div class="u4-ver-c"><span class="u4-tag">Key Result '+c.kr+' &middot; '+c.cp+'</span><div>'+u4esc(c.t)+'</div></div>'+
      '<div class="u4-ver-g"><label class="u4-lbl">Executive accountable<input class="u4-in" type="text" value="'+u4esc(v.who)+'" placeholder="Role, for example COO" oninput="mbVer(\\''+c.id+'\\',\\'who\\',this.value)"></label>'+
      '<label class="u4-lbl">Evidence that it still holds<input class="u4-in" type="text" value="'+u4esc(v.ev)+'" placeholder="The evidence the executive will check" oninput="mbVer(\\''+c.id+'\\',\\'ev\\',this.value)"></label>'+
      '<label class="u4-lbl">Date of the first check<input class="u4-in" type="text" value="'+u4esc(v.when)+'" placeholder="For example 31 March 2027" oninput="mbVer(\\''+c.id+'\\',\\'when\\',this.value)"></label></div></div>';
  }).join('');
  h+='<div class="u4-egs-h" style="margin-top:18px;">Executive blind spot</div>'+
    '<label class="u4-lbl" for="mb_blind_cp">The checkpoint your executive team is most likely to overlook</label>'+
    '<select class="u4-in" id="mb_blind_cp" onchange="mbBlindSet(\\'cp\\',this.value)"><option value="">&ndash; select a checkpoint &ndash;</option>'+['Arena','Boundaries','Competition','Value Proposition'].map(function(n){return '<option'+(MB.blind.cp===n?' selected':'')+'>'+n+'</option>';}).join('')+'</select>'+
    '<label class="u4-lbl" for="mb_blind_risk">The enterprise risk if it does</label>'+
    '<textarea class="u4-ta" id="mb_blind_risk" placeholder="What happens to the enterprise if this checkpoint is overlooked..." oninput="mbBlindSet(\\'risk\\',this.value)">'+u4esc(MB.blind.risk)+'</textarea>';
  return h;
}
function mbVer(id,f,val){MB.ver[id]=mbVerRow(id);MB.ver[id][f]=val;mbUnconfirm();clearTimeout(_mbPaint);_mbPaint=setTimeout(mbRefresh,350);mbQueue();}
function mbBlindSet(f,val){MB.blind[f]=val;mbUnconfirm();clearTimeout(_mbPaint);_mbPaint=setTimeout(mbRefresh,350);mbQueue();}""")
# record text and html gain 5.3
once("""function mbRecordText(){
  var lab={fn:'Functional',ex:'Experiential',co:'Consequential',bd:'Boundaries',cp:'Alternatives',rel:'Relevant',dis:'Distinctive',dlv:'Deliverable'};
  var all=mbAll(),done=all.filter(function(x){return mbKrDone(x.k);}).length;
  return (""","""function mbRecordText(){
  return mbRecordText52()+'\\n\\n5.3 · VERIFICATION OWNERSHIP\\n'+mbVerText()+'\\n\\n5.3 · EXECUTIVE BLIND SPOT\\n'+mbBlindText();
}
function mbRecordText52(){
  var lab={fn:'Functional',ex:'Experiential',co:'Consequential',bd:'Boundaries',cp:'Alternatives',rel:'Relevant',dis:'Distinctive',dlv:'Deliverable'};
  var all=mbAll(),done=all.filter(function(x){return mbKrDone(x.k);}).length;
  return (""")
once("""        return '<div class="u4-rec-c '+c.cls+'"><span class="u4-tag">'+c.name+'</span><div>'+(k[c.k].trim()?u4esc(k[c.k]):'<i>Must-Be-True to be named</i>')+'</div></div>';
      }).join('');
    }).join('');
  }).join('')+'</div>';""","""        return '<div class="u4-rec-c '+c.cls+'"><span class="u4-tag">'+c.name+'</span><div>'+(k[c.k].trim()?u4esc(k[c.k]):'<i>Must-Be-True to be named</i>')+'</div></div>';
      }).join('');
    }).join('');
  }).join('')+'<div class="u4-rec-o">5.3 &middot; Verification ownership</div><div class="u4-rec-k">'+(mbVerOwned().length?u4esc(mbVerText()).replace(/\\n/g,'<br>'):'<i>to be agreed by your group</i>')+'</div>'+
    '<div class="u4-rec-o">5.3 &middot; Executive blind spot</div><div class="u4-rec-k">'+(MB.blind.cp&&MB.blind.risk.trim()?u4esc(mbBlindText()).replace(/\\n/g,'<br>'):'<i>to be agreed by your group</i>')+'</div></div>';""")
once("When every Key Result has been taken through the four steps, select Agree. When every member has agreed, your work feeds boxes 4A to 4D of your team&rsquo;s Capstone Blueprint.",
     "When every Key Result has been taken through the four steps and 5.3 is complete, select Agree. When every member has agreed, your work feeds boxes 4A to 4F of your team&rsquo;s Capstone Blueprint.")
once("  if(o)o.innerHTML=mbOutHtml();\n}\nfunction mbRefresh(){","  if(o)o.innerHTML=mbOutHtml();\n  var v=u4el('mbVerP');if(v)v.innerHTML=mbVerHtml();\n}\nfunction mbRefresh(){")
once("  await u4save('__mbt_work',{step:MB.step,items:MB.items,cur:MB.cur});","  await u4save('__mbt_work',{step:MB.step,items:MB.items,cur:MB.cur,ver:MB.ver,blind:MB.blind});")
once("function u4TeamOut(){if(!window.S2RTeam||!S2RTeam.isScribe())return;if(!mbAll().length||mbOpen().length)return;for(var n=0;n<4;n++)S2RTeam.save(MB_KEYS[n],mbText(n));S2RTeam.save('mbt_record',mbRecordText());}",
     "function u4TeamOut(){if(!window.S2RTeam||!S2RTeam.isScribe())return;if(!mbAll().length||mbOpen().length||mbS3Open().length)return;for(var n=0;n<4;n++)S2RTeam.save(MB_KEYS[n],mbText(n));S2RTeam.save('mbt_verify',mbVerText());S2RTeam.save('mbt_blind',mbBlindText());S2RTeam.save('mbt_record',mbRecordText());}")
C_OLD="if(!mbAll().length)return 'bring in your Unit 3 Key Results';var o=mbOpen();return o.length?o.map(function(x){return 'Key Result '+mbId(x.i,x.j);}).join('; '):'';"
C_NEW="if(!mbAll().length)return 'bring in your Unit 3 Key Results';var o=mbOpen().map(function(x){return 'Key Result '+mbId(x.i,x.j);}).concat(mbS3Open());return o.length?o.join('; '):'';"
assert s.count(C_OLD)==2; s=s.replace(C_OLD,C_NEW)
once("/^(__mbt_work$|mbt_(record|arena|bound|comp|value)$)/","/^(__mbt_work$|mbt_(record|arena|bound|comp|value|verify|blind)$)/")
# print adds 5.3
once("""  }).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Unit 4 · ABCV–MBT record</title>""","""  }).join('')+'<h2>5.3 · Verification ownership</h2><p style="white-space:pre-wrap;font-family:Arial,sans-serif;font-size:13px">'+u4esc(mbVerText()||'—')+'</p><h2>5.3 · Executive blind spot</h2><p style="white-space:pre-wrap;font-family:Arial,sans-serif;font-size:13px">'+u4esc(mbBlindText())+'</p>';
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Unit 4 · ABCV–MBT record</title>""")
once("Strategy2Results® · Module 2 · Unit 4 · Part 5.2 · Capstone work","Strategy2Results® · Module 2 · Unit 4 · Parts 5.2 and 5.3 · Capstone work")
once("function mbPaint(){var k=u4el('mbOkrP'),t=u4el('mbToolP');if(k)k.innerHTML=mbPickHtml();if(t)t.innerHTML=mbToolHtml();}",
     "function mbPaint(){var k=u4el('mbOkrP'),t=u4el('mbToolP'),v=u4el('mbVerP');if(k)k.innerHTML=mbPickHtml();if(t)t.innerHTML=mbToolHtml();if(v)v.innerHTML=mbVerHtml();}")
# CSS
s=s.replace("</style>",".u4-ver{border:1px solid rgba(255,255,255,.08);border-radius:4px;padding:12px 14px;margin:0 0 12px;background:rgba(255,255,255,.02);}.u4-ver-c{font-size:13px;line-height:1.6;color:rgba(255,255,255,.8);margin-bottom:8px;}.u4-ver-c .u4-tag{display:inline-block;margin-bottom:4px;}.u4-ver-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:10px;}.u4-in{width:100%;box-sizing:border-box;background:rgba(0,0,0,.25);border:1px solid rgba(255,255,255,.15);color:#fff;border-radius:3px;padding:8px 10px;font:inherit;font-size:13px;margin-top:4px;}select.u4-in{max-width:360px;margin-bottom:12px;}\n</style>",1)
open(out,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if CR else s)
print('ok')
