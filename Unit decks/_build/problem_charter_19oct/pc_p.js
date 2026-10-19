/* ════════════ UNIT 1 · PART 6.2 · THE PROBLEM CHARTER (group work, Capstone work) ════════════
   The group creates its simulated company, records its simulated executive team and writes its Problem Charter.
   Answers save as the participant types (__pc_work, pc_record). Confirm writes pc_company, pc_team, pc_org, pc_reality,
   pc_challenges, pc_manifest, pc_consequences, pc_capabilities, pc_shared, pc_problem, pc_sources (Capstone boxes 1A to 1K)
   and the eleven "Problem Charter · …" names into confirmed_items. An edit after confirmation takes the names out again. */
var PC_LENS='u1_foundations';
var PC_ROLES=['CEO','CFO','COO','CHRO','CTO','CMO','CCO','CPO','CRO','CSO'];
var PC_ROWS=10;
/* [id, label, step] */
var PCF=[['company','Simulated company name','s1'],['sector','Sector or industry','s1'],['size','Approximate size','s1'],['activity','Main activity or service','s1'],['results','Our strategy-to-results reality','s1'],
  ['challenges','1 · Challenges experienced','s2'],['manifest','2 · How these challenges manifest','s2'],['consequences','3 · Consequences for results and culture','s2'],['capabilities','4 · Capabilities to strengthen','s2'],
  ['design','Strategy design','s3'],['execution','Strategy execution','s3'],['sustain','Sustaining performance','s3'],
  ['problem','Our central organisational problem','s4'],['sources','Our sources of experience','s4']];
/* [step, record heading] */
var PCS=[['s1','Step 1 · Our simulated company'],['s2','Step 2 · The four Charter questions'],['s3','Step 3 · Our shared organisational reality'],['s4','Step 4 · Our central organisational problem']];
/* [Capstone name, response key, Capstone box, fields ('team' = the executive team)] */
var PCP=[['Problem Charter · Simulated Company','pc_company','1A',['company']],
  ['Problem Charter · Executive Team','pc_team','1B',['team']],
  ['Problem Charter · Our Organisation','pc_org','1C',['sector','size','activity']],
  ['Problem Charter · Strategy-to-Results Reality','pc_reality','1D',['results']],
  ['Problem Charter · Challenges Experienced','pc_challenges','1E',['challenges']],
  ['Problem Charter · How They Manifest','pc_manifest','1F',['manifest']],
  ['Problem Charter · Consequences','pc_consequences','1G',['consequences']],
  ['Problem Charter · Capabilities to Strengthen','pc_capabilities','1H',['capabilities']],
  ['Problem Charter · Shared Organisational Reality','pc_shared','1I',['design','execution','sustain']],
  ['Problem Charter · Central Organisational Problem','pc_problem','1J',['problem']],
  ['Problem Charter · Sources of Experience','pc_sources','1K',['sources']]];
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
function pcnorm(w){
  var o={};PCF.forEach(function(f){o[f[0]]=(w&&typeof w[f[0]]==='string')?w[f[0]]:'';});
  o.team=[];for(var i=0;i<PC_ROWS;i++){var r=(w&&Array.isArray(w.team)&&w.team[i])||{};o.team.push({role:typeof r.role==='string'?r.role:'',name:typeof r.name==='string'?r.name:''});}
  return o;
}
function pcval(id){return String(PC.w[id]||'').trim();}
function pcTeamRows(){return PC.w.team.filter(function(r){return r.role.trim()&&r.name.trim();});}
function pcLabel(id){for(var i=0;i<PCF.length;i++)if(PCF[i][0]===id)return PCF[i][1];return id;}
/* The text of one Capstone box. */
function pcText(p){
  var fs=p[3];
  if(fs[0]==='team')return pcTeamRows().map(function(r){return r.role.trim()+' · '+r.name.trim();}).join('\n');
  if(fs.length===1)return pcval(fs[0]);
  return fs.map(function(id){return pcLabel(id)+': '+pcval(id);}).join('\n');
}
function pcTeamText(){var rows=pcTeamRows();return rows.length?rows.map(function(r){return r.role.trim()+' · '+r.name.trim();}).join('\n'):'';}
function pcRecord(){
  return PCS.map(function(s){
    var lines=PCF.filter(function(f){return f[2]===s[0];}).map(function(f){return f[1]+': '+pcval(f[0]);});
    if(s[0]==='s1')lines.splice(1,0,'Simulated executive team:\n'+pcTeamText());
    return s[1].toUpperCase()+'\n'+lines.join('\n');
  }).join('\n\n');
}
function pcFill(){
  PCF.forEach(function(f){var el=pcel('pc_'+f[0]);if(el)el.value=PC.w[f[0]]||'';});
  for(var i=0;i<PC_ROWS;i++){var r=pcel('pc_role_'+i),n=pcel('pc_name_'+i);if(r)r.value=PC.w.team[i].role;if(n)n.value=PC.w.team[i].name;}
}
function pcChanged(){
  if(pcdrop())pclater('conf',function(){pcsave('confirmed_items',PC.conf);},600);
  pcmsg('');
  pclater('rec',pcRecDraw,300);
  pclater('save',async function(){await pcsave('__pc_work',PC.w);await pcsave('pc_record',pcRecord());},800);
}
function pcIn(el){
  var id=el.getAttribute('data-pc');if(!id)return;
  var m=/^(role|name)_(\d+)$/.exec(id);
  if(m)PC.w.team[+m[2]][m[1]]=String(el.value||'');
  else PC.w[id]=String(el.value||'');
  pcChanged();
}
function pcStep(i){
  var root=pcel('pcTool');if(!root)return;
  var tabs=root.querySelectorAll('.pc-tab'),panels=root.querySelectorAll('.pc-panel');
  tabs.forEach(function(t,j){t.classList.toggle('on',j===i);});panels.forEach(function(p,j){p.classList.toggle('on',j===i);});
  if(i===tabs.length-1)pcRecDraw();
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
/* What is still open before Confirm. */
function pcOpen(){
  var open=[];
  PCS.forEach(function(s){
    var n=PCF.filter(function(f){return f[2]===s[0]&&!pcval(f[0]);}).length;
    if(n)open.push(s[1]+' ('+n+(n===1?' entry':' entries')+' still open)');
  });
  var half=PC.w.team.filter(function(r){return (r.role.trim()&&!r.name.trim())||(!r.role.trim()&&r.name.trim());}).length;
  if(!pcTeamRows().length)open.push('Simulated executive team (no member recorded yet)');
  else if(half)open.push('Simulated executive team ('+half+(half===1?' row has':' rows have')+' a role without a name, or a name without a role)');
  var seen={},dup=[];pcTeamRows().forEach(function(r){var k=r.role.trim();if(seen[k]&&dup.indexOf(k)<0)dup.push(k);seen[k]=1;});
  if(dup.length)open.push('Simulated executive team (each role is held by one member: '+dup.join(', ')+' appears more than once)');
  return open;
}
function pcRecDraw(){
  var host=pcel('pcRec');if(!host)return;
  var conf=pchas(),msg=pcel('pcMsg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  var name=pcval('company');
  host.innerHTML='<div class="pc-out"><div class="pc-out-h">'+(name?pcesc(name)+' &middot; ':'')+'Your group&rsquo;s Problem Charter'+(conf?'<span class="pc-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="pc-conf no">Not yet confirmed</span>')+'</div>'+
    PCS.map(function(s){
      var fs=PCF.filter(function(f){return f[2]===s[0];}),done=fs.filter(function(f){return pcval(f[0]);}).length,total=fs.length;
      var lines=fs.map(function(f){var b=pcval(f[0]);return '<div class="pc-rec-t"><strong>'+pcesc(f[1])+':</strong> '+(b?pcesc(b):'<i>to be agreed by your group</i>')+'</div>';});
      if(s[0]==='s1'){
        var t=pcTeamText();total++;if(t)done++;
        lines.splice(1,0,'<div class="pc-rec-t"><strong>Simulated executive team:</strong>'+(t?'\n'+pcesc(t):' <i>to be agreed by your group</i>')+'</div>');
      }
      return '<details class="pc-rec"><summary>'+pcesc(s[1])+'<span>'+done+' of '+total+' entries</span></summary>'+lines.join('')+'</details>';
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
  for(var i=0;i<PCP.length&&ok;i++)ok=await pcsave(PCP[i][1],pcText(PCP[i]));
  if(!ok){pcmsg('Not saved. Check your connection, then select Confirm again.');return;}
  PC_NAMES.forEach(function(nm){if(PC.conf.indexOf(nm)<0)PC.conf.push(nm);});
  if(!(await pcsave('confirmed_items',PC.conf))){pcdrop();pcRecDraw();pcmsg('Not saved. Check your connection, then select Confirm again.');return;}
  pcRecDraw();pcmsg('✓ Confirmed. Your Problem Charter is ready for your team’s Capstone Blueprint.','ok');
}
function pcPrint(){
  var body=PCS.map(function(s){
    var ps=PCF.filter(function(f){return f[2]===s[0];}).map(function(f){var v=pcval(f[0]);return '<p><strong>'+pcesc(f[1])+':</strong> '+(v?pcesc(v):'—')+'</p>';});
    if(s[0]==='s1'){var t=pcTeamText();ps.splice(1,0,'<p><strong>Simulated executive team:</strong>'+(t?'\n'+pcesc(t):' —')+'</p>');}
    return '<h2>'+pcesc(s[1])+'</h2>'+ps.join('');
  }).join('');
  var name=pcval('company');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our Problem Charter</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}p{font-size:13px;margin:4px 0;white-space:pre-wrap}</style></head><body>'+
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
    root.addEventListener('input',function(ev){if(ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-pc')&&ev.target.tagName!=='SELECT')pcIn(ev.target);});
    root.addEventListener('change',function(ev){if(ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-pc')&&ev.target.tagName==='SELECT')pcIn(ev.target);});
  }
  pcFill();pcRecDraw();
});
