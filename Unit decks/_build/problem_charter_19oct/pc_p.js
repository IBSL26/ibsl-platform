/* ════════════ UNIT 1 · PART 6.2 · THE PROBLEM CHARTER (group work, Capstone work) ════════════
   Step 1 the simulated company and its executive team; Step 2 the shared reality (challenges in the three areas,
   how they manifested, consequences in the three areas); Step 3 the three challenges per area the team will address
   and the central organisational problem. Answers save as the participant types (__pc_work, pc_record).
   Confirm writes pc_company, pc_team, pc_org, pc_challenges, pc_manifest, pc_consequences, pc_address, pc_problem
   (Capstone boxes 1A to 1H) and the eight "Problem Charter · …" names into confirmed_items.
   An edit after confirmation takes the names out again. */
var PC_LENS='u1_foundations';
var PC_ROWS=10, PC_CH=6, PC_CH_MIN=4, PC_SC=3, PC_SC_MIN=2, PC_PICK=3;
var PC_AREAS=[['design','Strategy design'],['execution','Strategy execution'],['sustain','Sustaining performance']];
var PC_MF=[['behaviours','Observable behaviours'],['practices','Management practices'],['conditions','Organisational conditions']];
var PC_S1=[['company','Simulated company name'],['sector','Sector or industry'],['size','Approximate size'],['activity','Main activity or service']];
var PCP=[['Problem Charter · Simulated Company','pc_company','1A'],
  ['Problem Charter · Executive Team','pc_team','1B'],
  ['Problem Charter · Our Organisation','pc_org','1C'],
  ['Problem Charter · Challenges Experienced','pc_challenges','1D'],
  ['Problem Charter · How They Manifested','pc_manifest','1E'],
  ['Problem Charter · Consequences','pc_consequences','1F'],
  ['Problem Charter · Challenges We Will Address','pc_address','1G'],
  ['Problem Charter · Central Organisational Problem','pc_problem','1H']];
var PC={conf:[],w:{},ready:false};
var PC_NAMES=PCP.map(function(p){return p[0];});
function pcel(id){return document.getElementById(id);}
function pcesc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function pcmsg(text,cls){var m=pcel('pcMsg');if(!m)return;m.textContent=text||'';m.className='pc-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function pcsave(k,val){
  if(!window.S2R){console.warn('[unit1_P] S2R helper not loaded');return false;}
  try{return await S2R.save(PC_LENS,k,val);}catch(e){console.error('[unit1_P] save failed for '+k,e);return false;}
}
var _pct={};
function pclater(name,fn,ms){clearTimeout(_pct[name]);_pct[name]=setTimeout(fn,ms||700);}
function pchas(){return PC_NAMES.every(function(nm){return PC.conf.indexOf(nm)>=0;});}
function pcdrop(){var ch=false;PC_NAMES.forEach(function(nm){var i=PC.conf.indexOf(nm);if(i>=0){PC.conf.splice(i,1);ch=true;}});return ch;}
function pcs(v){return typeof v==='string'?v:'';}
function pcarr(a,n){var o=[];for(var i=0;i<n;i++)o.push(pcs(Array.isArray(a)?a[i]:''));return o;}
function pcnorm(w){
  w=w||{};var o={};
  PC_S1.forEach(function(f){o[f[0]]=pcs(w[f[0]]);});
  o.team=[];for(var i=0;i<PC_ROWS;i++){var r=(Array.isArray(w.team)&&w.team[i])||{};o.team.push({role:pcs(r.role),name:pcs(r.name)});}
  o.ch={};o.cq={};o.pick={};
  PC_AREAS.forEach(function(a){
    o.ch[a[0]]=pcarr(w.ch&&w.ch[a[0]],PC_CH);
    o.cq[a[0]]=pcs(w.cq&&w.cq[a[0]]);
    o.pick[a[0]]=(w.pick&&Array.isArray(w.pick[a[0]]))?w.pick[a[0]].filter(function(x){return typeof x==='string';}):[];
  });
  o.mf={};PC_MF.forEach(function(m){o.mf[m[0]]=pcarr(w.mf&&w.mf[m[0]],PC_SC);});
  o.problem=pcs(w.problem);
  return o;
}
function pct(s){return String(s||'').trim();}
function pcList(area){return PC.w.ch[area].map(pct).filter(Boolean);}
function pcScen(m){return PC.w.mf[m].map(pct).filter(Boolean);}
function pcPicked(area){var l=pcList(area);return PC.w.pick[area].filter(function(x){return l.indexOf(x)>=0;});}
function pcTeamRows(){return PC.w.team.filter(function(r){return pct(r.role)&&pct(r.name);});}
/* Capstone texts */
function pcText(key){
  if(key==='pc_company')return pct(PC.w.company);
  if(key==='pc_team')return pcTeamRows().map(function(r){return pct(r.role)+' · '+pct(r.name);}).join('\n');
  if(key==='pc_org')return 'Sector or industry: '+pct(PC.w.sector)+'\nApproximate size: '+pct(PC.w.size)+'\nMain activity or service: '+pct(PC.w.activity);
  if(key==='pc_challenges')return PC_AREAS.map(function(a){return a[1]+'\n'+pcList(a[0]).map(function(c,i){return (i+1)+'. '+c;}).join('\n');}).join('\n\n');
  if(key==='pc_manifest')return PC_MF.map(function(m){return m[1]+'\n'+pcScen(m[0]).map(function(c,i){return 'Scenario '+(i+1)+': '+c;}).join('\n');}).join('\n\n');
  if(key==='pc_consequences')return PC_AREAS.map(function(a){return a[1]+': '+pct(PC.w.cq[a[0]]);}).join('\n');
  if(key==='pc_address')return PC_AREAS.map(function(a){return a[1]+'\n'+pcPicked(a[0]).map(function(c,i){return (i+1)+'. '+c;}).join('\n');}).join('\n\n');
  if(key==='pc_problem')return pct(PC.w.problem);
  return '';
}
function pcFilled(key){
  var any=function(f){return PC_AREAS.some(function(a){return f(a[0]);});};
  if(key==='pc_company')return !!pct(PC.w.company);
  if(key==='pc_team')return pcTeamRows().length>0;
  if(key==='pc_org')return !!(pct(PC.w.sector)||pct(PC.w.size)||pct(PC.w.activity));
  if(key==='pc_challenges')return any(function(a){return pcList(a).length;});
  if(key==='pc_manifest')return PC_MF.some(function(m){return pcScen(m[0]).length;});
  if(key==='pc_consequences')return any(function(a){return pct(PC.w.cq[a]);});
  if(key==='pc_address')return any(function(a){return pcPicked(a).length;});
  return !!pct(PC.w.problem);
}
var PC_REC=[['Step 1 · Our simulated company',[['Simulated company','pc_company'],['Simulated executive team','pc_team'],['Our organisation','pc_org']]],
  ['Step 2 · Our shared reality',[['Challenges experienced','pc_challenges'],['How these challenges manifested','pc_manifest'],['Consequences','pc_consequences']]],
  ['Step 3 · Our central problem',[['The challenges we will address','pc_address'],['Our central organisational problem','pc_problem']]]];
function pcRecord(){return PC_REC.map(function(s){return s[0].toUpperCase()+'\n'+s[1].map(function(x){return x[0]+':\n'+pcText(x[1]);}).join('\n\n');}).join('\n\n\n');}
function pcFill(){
  PC_S1.forEach(function(f){var el=pcel('pc_'+f[0]);if(el)el.value=PC.w[f[0]];});
  for(var i=0;i<PC_ROWS;i++){var r=pcel('pc_role_'+i),n=pcel('pc_name_'+i);if(r)r.value=PC.w.team[i].role;if(n)n.value=PC.w.team[i].name;}
  PC_AREAS.forEach(function(a){
    for(var j=0;j<PC_CH;j++){var e=pcel('pc_ch_'+a[0]+'_'+j);if(e)e.value=PC.w.ch[a[0]][j];}
    var q=pcel('pc_cq_'+a[0]);if(q)q.value=PC.w.cq[a[0]];
  });
  PC_MF.forEach(function(m){for(var j=0;j<PC_SC;j++){var e=pcel('pc_mf_'+m[0]+'_'+j);if(e)e.value=PC.w.mf[m[0]][j];}});
  var p=pcel('pc_problem');if(p)p.value=PC.w.problem;
  pcPickDraw();
}
function pcChanged(){
  if(pcdrop())pclater('conf',function(){pcsave('confirmed_items',PC.conf);},600);
  pcmsg('');
  pclater('rec',pcRecDraw,300);
  pclater('save',async function(){await pcsave('__pc_work',PC.w);await pcsave('pc_record',pcRecord());},800);
}
function pcIn(el){
  var id=el.getAttribute('data-pc');if(!id)return;
  var v=String(el.value||''),m;
  if((m=/^(role|name)_(\d+)$/.exec(id)))PC.w.team[+m[2]][m[1]]=v;
  else if((m=/^ch_(\w+)_(\d+)$/.exec(id))){PC.w.ch[m[1]][+m[2]]=v;pclater('pick',pcPickDraw,400);}
  else if((m=/^mf_(\w+)_(\d+)$/.exec(id)))PC.w.mf[m[1]][+m[2]]=v;
  else if((m=/^cq_(\w+)$/.exec(id)))PC.w.cq[m[1]]=v;
  else if((m=/^pick_(\w+)$/.exec(id))){
    var l=PC.w.pick[m[1]],i=l.indexOf(el.value);
    if(el.checked&&i<0){if(pcPicked(m[1]).length>=PC_PICK){el.checked=false;pcmsgPick(m[1]);return;}l.push(el.value);}
    if(!el.checked&&i>=0)l.splice(i,1);
    pcPickDraw();
  }
  else PC.w[id]=v;
  pcChanged();
}
function pcmsgPick(area){var n=pcel('pc_pickmsg_'+area);if(n){n.textContent='Choose three challenges. Untick one to choose another.';n.style.display='block';}}
/* Step 3: the three challenges per area, chosen from the lists in Step 2. */
function pcPickDraw(){
  PC_AREAS.forEach(function(a){
    var host=pcel('pc_pick_'+a[0]);if(!host)return;
    var l=pcList(a[0]),picked=pcPicked(a[0]);
    PC.w.pick[a[0]]=picked.slice();
    host.innerHTML=l.length?l.map(function(c){
      var on=picked.indexOf(c)>=0;
      return '<label class="pc-pick'+(on?' on':'')+'"><input type="checkbox" data-pc="pick_'+a[0]+'" value="'+pcesc(c)+'"'+(on?' checked':'')+'><span>'+pcesc(c)+'</span></label>';
    }).join(''):'<p class="pc-wait">Your group&rsquo;s '+pcesc(a[1].toLowerCase())+' challenges from Step 2 appear here.</p>';
    var c=pcel('pc_pickn_'+a[0]);if(c)c.textContent=picked.length+' of '+PC_PICK+' chosen';
    var n=pcel('pc_pickmsg_'+a[0]);if(n&&picked.length<PC_PICK)n.style.display='none';
  });
}
function pcStep(i){
  var root=pcel('pcTool');if(!root)return;
  var tabs=root.querySelectorAll('.pc-tab'),panels=root.querySelectorAll('.pc-panel');
  tabs.forEach(function(t,j){t.classList.toggle('on',j===i);});panels.forEach(function(p,j){p.classList.toggle('on',j===i);});
  if(i===2)pcPickDraw();
  if(i===tabs.length-1)pcRecDraw();
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
/* What is still open before Confirm. */
function pcOpen(){
  var open=[],s1=PC_S1.filter(function(f){return !pct(PC.w[f[0]]);}).map(function(f){return f[1];});
  if(s1.length)open.push('Step 1: '+s1.join(', '));
  var half=PC.w.team.filter(function(r){return (pct(r.role)&&!pct(r.name))||(!pct(r.role)&&pct(r.name));}).length;
  if(!pcTeamRows().length)open.push('Step 1: the simulated executive team (no member recorded yet)');
  else if(half)open.push('Step 1: the simulated executive team ('+half+(half===1?' row has':' rows have')+' a role without a name, or a name without a role)');
  var seen={},dup=[];pcTeamRows().forEach(function(r){var k=pct(r.role);if(seen[k]&&dup.indexOf(k)<0)dup.push(k);seen[k]=1;});
  if(dup.length)open.push('Step 1: each role is held by one member ('+dup.join(', ')+' appears more than once)');
  PC_AREAS.forEach(function(a){var n=pcList(a[0]).length;if(n<PC_CH_MIN)open.push('Step 2, question 1: at least four '+a[1].toLowerCase()+' challenges ('+n+' so far)');});
  PC_MF.forEach(function(m){var n=pcScen(m[0]).length;if(n<PC_SC_MIN)open.push('Step 2, question 2: at least two scenarios for '+m[1].toLowerCase()+' ('+n+' so far)');});
  PC_AREAS.forEach(function(a){if(!pct(PC.w.cq[a[0]]))open.push('Step 2, question 3: the consequences for '+a[1].toLowerCase());});
  PC_AREAS.forEach(function(a){var n=pcPicked(a[0]).length;if(n!==PC_PICK)open.push('Step 3: three '+a[1].toLowerCase()+' challenges to address ('+n+' chosen)');});
  if(!pct(PC.w.problem))open.push('Step 3: the central organisational problem');
  return open;
}
function pcRecDraw(){
  var host=pcel('pcRec');if(!host)return;
  var conf=pchas(),msg=pcel('pcMsg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  var name=pct(PC.w.company);
  host.innerHTML='<div class="pc-out"><div class="pc-out-h">'+(name?pcesc(name)+' &middot; ':'')+'Your group&rsquo;s Problem Charter'+(conf?'<span class="pc-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="pc-conf no">Not yet confirmed</span>')+'</div>'+
    PC_REC.map(function(s){
      return '<details class="pc-rec"><summary>'+pcesc(s[0])+'</summary>'+s[1].map(function(x){
        return '<div class="pc-rec-s">'+pcesc(x[0])+'</div><div class="pc-rec-t">'+(pcFilled(x[1])?pcesc(pcText(x[1])):'<i>to be agreed by your group</i>')+'</div>';
      }).join('')+'</details>';
    }).join('')+
    '<div class="pc-btnrow"><button type="button" class="pc-b ok" id="pcConfBtn" onclick="pcConfirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="pc-b" onclick="pcPrint()">Print</button></div>'+
    '<div class="pc-note" id="pcMsg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=pcel('pcMsg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function pcConfirm(){
  var open=pcOpen();
  if(open.length){pcRecDraw();pcmsg('Before you confirm, complete: '+open.join('; ')+'.');return;}
  clearTimeout(_pct.save);clearTimeout(_pct.conf);
  var ok=await pcsave('__pc_work',PC.w);
  ok=ok&&(await pcsave('pc_record',pcRecord()));
  for(var i=0;i<PCP.length&&ok;i++)ok=await pcsave(PCP[i][1],pcText(PCP[i][1]));
  if(!ok){pcmsg('Not saved. Check your connection, then select Confirm again.');return;}
  PC_NAMES.forEach(function(nm){if(PC.conf.indexOf(nm)<0)PC.conf.push(nm);});
  if(!(await pcsave('confirmed_items',PC.conf))){pcdrop();pcRecDraw();pcmsg('Not saved. Check your connection, then select Confirm again.');return;}
  pcRecDraw();pcmsg('✓ Confirmed. Your Problem Charter is ready for your team’s Capstone Blueprint.','ok');
}
function pcPrint(){
  var body=PC_REC.map(function(s){
    return '<h2>'+pcesc(s[0])+'</h2>'+s[1].map(function(x){var t=pcText(x[1]);return '<h3>'+pcesc(x[0])+'</h3><p>'+(t?pcesc(t):'—')+'</p>';}).join('');
  }).join('');
  var name=pct(PC.w.company);
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our Problem Charter</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:16px;margin:24px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}h3{font-size:13px;margin:12px 0 2px;color:#043f2f}p{font-size:13px;margin:4px 0;white-space:pre-wrap}</style></head><body>'+
    '<h1>'+(name?pcesc(name)+' · ':'')+'Our Problem Charter</h1><p class="sub">Strategy2Results® · Module 1 · Unit 1 · Part 6.2 · Capstone work · '+(pchas()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
function pcInit(responses){
  responses=responses||{};
  PC.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  PC.w=pcnorm(responses.__pc_work);
  PC.ready=true;
  pcFill();pcRecDraw();
}
document.addEventListener('DOMContentLoaded',function(){
  PC.w=pcnorm(null);
  var root=pcel('pcTool');
  if(root){
    root.addEventListener('input',function(ev){var t=ev.target;if(t&&t.getAttribute&&t.getAttribute('data-pc')&&t.tagName!=='SELECT'&&t.type!=='checkbox')pcIn(t);});
    root.addEventListener('change',function(ev){var t=ev.target;if(t&&t.getAttribute&&t.getAttribute('data-pc')&&(t.tagName==='SELECT'||t.type==='checkbox'))pcIn(t);});
  }
  pcFill();pcRecDraw();
});
