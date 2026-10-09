/* ── Section 5 · the 3S Check and ACE-IT for the group's strategy (group work, Capstone work) ─────
   The group states its Shift, Stake and Step, then the behaviour it expects from the leadership team under each ACE-IT behaviour.
   Answers save as the participant types (__align_work, kit_team). Confirm writes kit_mind (the 3S Check) and kit_habit (ACE-IT) and the two
   "Alignment Plan · …" names into confirmed_items. An edit after confirmation takes the names out again. */
var S5=/*FIELDS*/[];
var S5_NAMES=/*NAMES*/[];
var S5_REC=/*REC*/{};
function s5Norm(w){var o={};S5.forEach(function(f){o[f[0]]=(w&&typeof w[f[0]]==='string')?w[f[0]]:'';});return o;}
function s5Text(part){return S5.filter(function(f){return f[2]===part;}).map(function(f){return f[1]+': '+String(U5.s5[f[0]]||'').trim();}).join('\n\n');}
function s5Fill(){S5.forEach(function(f){var el=u5el('s5_'+f[0]);if(el)el.value=U5.s5[f[0]]||'';});}
function s5Open(){return S5.filter(function(f){return !String(U5.s5[f[0]]||'').trim();}).map(function(f){return f[1];});}
function u5Step(i){var t=document.querySelectorAll('#mod4 .step-tab');if(t[i]){t[i].click();t[i].scrollIntoView({behavior:'smooth',block:'start'});}}
function s5In(id,val){
  U5.s5[id]=String(val||'');
  if(u5drop(S5_NAMES)){u5later('conf',function(){u5save('confirmed_items',U5.conf);},600);u5msg('kitMsg','');}
  u5later('s5Rec',s5RecDraw,300);
  u5later('s5Save',async function(){await u5save('__align_work',U5.s5);await u5save('kit_team',s5Text('mind')+'\n\n'+s5Text('habit'));},800);
}
function s5RecDraw(){
  var host=u5el('kitOutP');if(!host)return;
  var conf=u5has(S5_NAMES),msg=u5el('kitMsg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u5-out">'+u5recHead('Your group&rsquo;s record',S5_NAMES)+'<div class="u5-rec">'+['mind','habit'].map(function(part){
    return '<div class="u5-rec-s">'+u5esc(S5_REC[part])+'</div>'+S5.filter(function(f){return f[2]===part;}).map(function(f){
      var v=String(U5.s5[f[0]]||'').trim();
      return '<div class="u5-rec-t"><strong>'+u5esc(f[1])+':</strong> '+(v?u5esc(v):'<i>to be agreed by your group</i>')+'</div>';
    }).join('');
  }).join('')+'</div><div class="u5-btnrow"><button type="button" class="u5-b ok" id="kitConfBtn" onclick="s5Confirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u5-b" onclick="s5Print()">Print</button></div>'+
    '<div class="u5-note" id="kitMsg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u5el('kitMsg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function s5Confirm(){
  var open=s5Open();
  if(open.length){s5RecDraw();u5msg('kitMsg','Before you confirm, complete: '+open.join(', ')+'.');return;}
  clearTimeout(_u5t.s5Save);clearTimeout(_u5t.conf);
  var ok=(await u5save('__align_work',U5.s5))&&(await u5save('kit_team',s5Text('mind')+'\n\n'+s5Text('habit')))&&(await u5save('kit_mind',s5Text('mind')))&&(await u5save('kit_habit',s5Text('habit')));
  if(!ok){u5msg('kitMsg','Not saved. Check your connection, then select Confirm again.');return;}
  S5_NAMES.forEach(function(nm){if(U5.conf.indexOf(nm)<0)U5.conf.push(nm);});
  if(!(await u5save('confirmed_items',U5.conf))){u5drop(S5_NAMES);s5RecDraw();u5msg('kitMsg','Not saved. Check your connection, then select Confirm again.');return;}
  s5RecDraw();u5msg('kitMsg','✓ Confirmed. Your record is ready for your team’s Capstone Blueprint.','ok');
}
function s5Print(){
  var body=['mind','habit'].map(function(part){return '<h2>'+u5esc(S5_REC[part])+'</h2>'+S5.filter(function(f){return f[2]===part;}).map(function(f){
    var v=String(U5.s5[f[0]]||'').trim();return '<h3>'+u5esc(f[1])+'</h3><p>'+(v?u5esc(v).replace(/\n/g,'<br>'):'—')+'</p>';}).join('');}).join('');
  u5print('The 3S Check and ACE-IT for our strategy','Strategy2Results® · Module 3 · Unit 5 · Section 5 · Capstone work · '+(u5has(S5_NAMES)?'confirmed':'not yet confirmed'),body);
}

/* ── Step 2 · the team's OCEAVL profile, read only. The same figures the Capstone shows: counts for each level, with no names. ── */
var TEAM_OC_WAIT=/*WAIT*/'',TEAM_OC_NONE=/*NONE*/'';
async function u5TeamOc(manual){
  var host=u5el('u5TeamOc');if(!host)return;
  var note=function(t){host.innerHTML='<div class="u5-from"><i>'+u5esc(t)+'</i></div>';};
  if(!window.S2R||!S2R._client||!S2R.context){note(TEAM_OC_NONE);return;}
  if(manual)note('Reading your team’s profile…');
  try{
    var ctx=await S2R.context();if(!ctx||!ctx.cohortId){note(TEAM_OC_NONE);return;}
    var r=await S2R._client.rpc('get_my_capstone',{p_cohort_id:ctx.cohortId});
    var team=r&&!r.error&&r.data&&r.data.blueprint&&r.data.blueprint.team;if(!team||!team.id){note(TEAM_OC_NONE);return;}
    var q=await S2R._client.rpc('get_capstone_team_oceavl',{p_team_id:team.id});
    var o=q&&!q.error&&q.data;if(!o||typeof o!=='object'){note(TEAM_OC_NONE);return;}
    if(!Array.isArray(o.dims)){note(TEAM_OC_WAIT+' Submitted so far: '+(o.submitted||0)+' of '+(o.members||0)+' members.');return;}
    host.innerHTML='<div class="u5-from" style="white-space:normal;margin-bottom:8px;">The level held by most members is the team’s level. '+u5esc(String(o.members))+' members submitted. No names and no single scores are shown.</div>'+OC.map(function(d,i){
      var c=o.dims[i]||[0,0,0],H=c[0],Bn=c[1],L=c[2],lv=(H>=Bn&&H>=L)?'High':((L>=Bn&&L>=H)?'Low':'Balanced'),g=d.levels.filter(function(x){return x.level===lv;})[0];
      return '<div class="u5-lv" style="border:1px solid rgba(255,255,255,.08);border-radius:4px;margin:0 0 8px;"><span class="u5-lv-n">'+u5esc(d.name)+'</span><span class="u5-lv-h">'+lv+'</span>'+
        '<span class="u5-lv-c">High '+H+' · Balanced '+Bn+' · Low '+L+'</span>'+
        '<div class="u5-lv-g u5-lv-g2" style="margin-top:8px;"><div><b>Risk</b>'+u5esc(g.risk)+'</div><div><b>Response</b>'+u5esc(g.resp)+'</div></div></div>';
    }).join('');
  }catch(e){console.warn('[unit3_m1_lens4_p] team OCEAVL profile not read',e);note(TEAM_OC_NONE);}
}

/* ── Start: draw the tools empty, then fill them from the saved answers ───────────────────────── */
function u5DrawAll(){ocGridDraw();ocProfileDraw();s5Fill();s5RecDraw();}
function u5Init(responses){
  responses=responses||{};
  U5.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U5.oc=ocNorm(responses.__oceavl_work);
  U5.s5=s5Norm(responses.__align_work);
  U5.ready=true;
  u5DrawAll();
  u5Bring(false);
  u5TeamOc(false);
}
document.addEventListener('DOMContentLoaded',function(){
  U5.oc=ocBlank();U5.s5=s5Norm(null);
  var k=u5el('u5KissP');if(k)k.innerHTML=u5KissHtml('','');
  u5DrawAll();
});
