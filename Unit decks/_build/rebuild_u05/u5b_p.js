/* ════════════ UNIT 5 (October 2026) · PARTICIPANT TOOLS ════════════
   Section 3 · 3.1: the OCEAVL Assessment (personal). Scores save as the participant works; Submit writes "OCEAVL · My Scores" into confirmed_items.
   The team's profile is shown in the Capstone once every member has submitted.
   Section 5 · Step 2: Your Watch List (individual, Portfolio work). Saves as the participant works.
   Section 5 · Step 3: Team Alignment Plan (group, Capstone work). Confirm writes the four "Alignment Plan · …" names into confirmed_items.
   An edit after confirmation takes the names out again. The Unit 3 Start and Stop lists are read only. */
var U5_LENS='u3m1_lens4',U5_U3_LENS='u2m1_lens2';
var U5={conf:[],ready:false,oc:[],me:{},team:{}};
var OC=/*OCEAVL*/[];
var CHECKS=/*CHECKS*/[];
var KIT=/*KIT*/[];
var OC_NAME='OCEAVL · My Scores';
var KIT_NAMES=CHECKS.map(function(c){return 'Alignment Plan · '+c.name;});
var KIT_KEYS=CHECKS.map(function(c){return 'kit_'+c.id;});
function u5el(id){return document.getElementById(id);}
function u5esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u5msg(id,text,cls){var m=u5el(id);if(!m)return;m.textContent=text||'';m.className='u5-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u5save(k,val){
  if(!window.S2R){console.warn('[unit3_m1_lens4_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U5_LENS,k,val);}catch(e){console.error('[unit3_m1_lens4_p] save failed for '+k,e);return false;}
}
function u5has(names){return names.every(function(nm){return U5.conf.indexOf(nm)>=0;});}
function u5drop(names){var ch=false;names.forEach(function(nm){var i=U5.conf.indexOf(nm);if(i>=0){U5.conf.splice(i,1);ch=true;}});return ch;}
var _u5t={};
function u5later(name,fn,ms){clearTimeout(_u5t[name]);_u5t[name]=setTimeout(fn,ms||700);}
function u5print(title,sub,body){
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>'+u5esc(title)+'</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}h3{font-size:13px;margin:14px 0 2px}p{font-size:13px;margin:4px 0}</style></head><body>'+
    '<h1>'+u5esc(title)+'</h1><p class="sub">'+u5esc(sub)+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
function u5recHead(title,names){
  var conf=u5has(names);
  return '<div class="u5-out-h">'+title+(conf?'<span class="u5-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u5-conf no">Not yet confirmed</span>')+'</div>';
}

/* ── Unit 3 · the group's confirmed Start and Stop lists (read only) ─────────────────────────── */
function u5KissHtml(start,stop){
  var box=function(label,val){return '<div class="u5-from"><b>'+label+'</b>'+(String(val||'').trim()?u5esc(val):'<i>Your group&rsquo;s confirmed list appears here.</i>')+'</div>';};
  return '<div class="u5-u3-grid">'+box('Start &middot; practices to introduce',start)+box('Stop &middot; practices to end',stop)+'</div>';
}
async function u5Bring(manual){
  var host=u5el('u5KissP');if(!host)return;
  if(!window.S2R){if(manual)u5msg('u5BringMsg','The save system is not ready. Reload the page and try again.');return;}
  var u3={};try{u3=await S2R.loadAll(U5_U3_LENS);}catch(e){u3={};}
  var conf=(u3&&Array.isArray(u3.confirmed_items))?u3.confirmed_items:[];
  var start=(u3&&typeof u3.kiss_start==='string')?u3.kiss_start:'',stop=(u3&&typeof u3.kiss_stop==='string')?u3.kiss_stop:'';
  if(conf.indexOf('KISS · Start')<0||conf.indexOf('KISS · Stop')<0||!start.trim()||!stop.trim()){
    host.innerHTML=u5KissHtml('','');
    u5msg('u5BringMsg','No confirmed KISS map was found on your Unit 3 page. Confirm your group’s KISS map in Unit 3, part 4.1, then select Bring in from my Unit 3 page.');
    return;
  }
  host.innerHTML=u5KissHtml(start,stop);
  u5msg('u5BringMsg',manual?'Brought in from your Unit 3 page.':'',manual?'ok':'');
}

/* ── 3.1 · OCEAVL Assessment: a personal assessment. Each participant scores themselves. The team's profile is shown in the Capstone. ── */
function ocBlank(){return OC.map(function(){return 0;});}
function ocNorm(w){var a=ocBlank();if(w&&Array.isArray(w.s))OC.forEach(function(d,j){var v=parseInt(w.s[j],10);a[j]=(v>=1&&v<=5)?v:0;});return a;}
function ocDone(){return U5.oc.every(function(v){return v>0;});}
function ocLevel(v){return v>=4?'High':(v<=2?'Low':'Balanced');}
function ocMine(){return OC.map(function(d,j){var v=U5.oc[j];if(!v)return null;var lv=ocLevel(v);return {d:d,v:v,lv:lv,g:d.levels.filter(function(x){return x.level===lv;})[0]};});}
function ocGridDraw(){
  var host=u5el('ocGrid');if(!host)return;
  host.innerHTML='<div class="u5-oc"><div class="u5-oc-row"><div class="u5-oc-g">'+OC.map(function(d,j){
    return '<div><label for="oc_s_'+j+'">'+u5esc(d.name)+'</label><select class="u5-sel" id="oc_s_'+j+'" onchange="ocIn('+j+',this.value)">'+
      '<option value="0">&mdash;</option>'+[1,2,3,4,5].map(function(v){return '<option value="'+v+'"'+(U5.oc[j]===v?' selected':'')+'>'+v+'</option>';}).join('')+'</select></div>';
  }).join('')+'</div></div></div>';
}
function ocScoresText(){return OC.map(function(d,j){return d.name+' '+(U5.oc[j]||'—');}).join(' · ');}
function ocProfileText(){
  return ocMine().filter(function(x){return x;}).map(function(x){
    return x.d.name+': '+x.lv+' (score '+x.v+')\n'+x.g.dna+'\nRisk: '+x.g.risk+'\nResponse: '+x.g.resp+'\nRoutines: '+x.g.rout;
  }).join('\n\n');
}
function ocProfileDraw(){
  var host=u5el('ocProfile');if(host){
    var P=ocMine().filter(function(x){return x;});
    host.innerHTML='<div class="chg-h">Your own profile</div>'+(P.length?P.map(function(x){
      return '<div class="u5-lv" style="border:1px solid rgba(255,255,255,.08);border-radius:4px;margin:0 0 8px;"><span class="u5-lv-n">'+u5esc(x.d.name)+'</span><span class="u5-lv-h">'+x.lv+'</span>'+
        '<span class="u5-lv-c">Your score: '+x.v+'</span><p class="u5-lv-dna">'+u5esc(x.g.dna)+'</p>'+
        '<div class="u5-lv-g"><div><b>Risk</b>'+u5esc(x.g.risk)+'</div><div><b>Response</b>'+u5esc(x.g.resp)+'</div><div><b>Routines</b>'+u5esc(x.g.rout)+'</div></div></div>';
    }).join(''):'<div class="u5-from"><i>Your profile appears here as you score each dimension.</i></div>');
  }
  var c=u5el('ocConf');if(c){
    var conf=u5has([OC_NAME]),msg=u5el('ocMsg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
    c.innerHTML='<div class="u5-out"><div class="u5-out-h">Your scores'+(conf?'<span class="u5-conf yes">Submitted &middot; in your team&rsquo;s profile</span>':'<span class="u5-conf no">Not yet submitted</span>')+'</div>'+
      '<div class="u5-rec-t">Your team&rsquo;s profile appears in your team&rsquo;s Capstone Blueprint once every member has submitted. It shows the team&rsquo;s level on each dimension, with no names.</div>'+
      '<div class="u5-btnrow"><button type="button" class="u5-b ok" id="ocConfBtn" onclick="ocConfirm()">'+(conf?'Submitted &#10003;':'Submit to My Team&rsquo;s Capstone')+'</button><button type="button" class="u5-b" onclick="ocPrint()">Print</button></div>'+
      '<div class="u5-note" id="ocMsg" style="display:none;"></div></div>';
    if(keep&&keep[0]){var m=u5el('ocMsg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
  }
}
function ocEdited(){
  if(u5drop([OC_NAME])){u5later('conf',function(){u5save('confirmed_items',U5.conf);},600);u5msg('ocMsg','');}
  u5later('ocDraw',ocProfileDraw,300);
}
function ocIn(j,val){
  var v=parseInt(val,10);U5.oc[j]=(v>=1&&v<=5)?v:0;
  ocEdited();
  u5later('ocSave',async function(){await u5save('__oceavl_work',{s:U5.oc});await u5save('oceavl_scores',ocScoresText());await u5save('oceavl_profile',ocProfileText());},800);
}
async function ocConfirm(){
  if(!ocDone()){ocProfileDraw();u5msg('ocMsg','Score all seven dimensions before you submit.');return;}
  clearTimeout(_u5t.ocSave);clearTimeout(_u5t.conf);
  var ok=(await u5save('__oceavl_work',{s:U5.oc}))&&(await u5save('oceavl_scores',ocScoresText()))&&(await u5save('oceavl_profile',ocProfileText()));
  if(!ok){u5msg('ocMsg','Not saved. Check your connection, then select Submit again.');return;}
  if(U5.conf.indexOf(OC_NAME)<0)U5.conf.push(OC_NAME);
  if(!(await u5save('confirmed_items',U5.conf))){u5drop([OC_NAME]);ocProfileDraw();u5msg('ocMsg','Not saved. Check your connection, then select Submit again.');return;}
  ocProfileDraw();u5msg('ocMsg','✓ Submitted. Your scores are in your team’s profile.','ok');
}
function ocPrint(){
  var P=ocMine().filter(function(x){return x;});
  var body=P.length?P.map(function(x){return '<h2>'+u5esc(x.d.name)+' · '+x.lv+' (score '+x.v+')</h2><p>'+u5esc(x.g.dna)+'</p><p><b>Risk:</b> '+u5esc(x.g.risk)+'</p><p><b>Response:</b> '+u5esc(x.g.resp)+'</p><p><b>Routines:</b> '+u5esc(x.g.rout)+'</p>';}).join(''):'<p>—</p>';
  u5print('My OCEAVL Profile','Strategy2Results® · Module 3 · Unit 5 · Section 3 · 3.1 · '+(u5has([OC_NAME])?'submitted to my team’s Capstone':'not yet submitted'),body);
}

/* ── Section 5 · the Alignment Toolkit: Your Watch List (me) and Team Alignment Plan (team) ───── */
var KIT_F={me:[['t','What I will do','The action you will take on this trigger in your own area...']],
           team:[['w','Where it will surface','The change and the group it affects...'],['d','What we will do','The action your team agrees on this trigger...'],['o','Leader who owns it','One named leader...']]};
function kitGet(mode,id){var s=U5[mode];if(!s[id])s[id]={on:false};return s[id];}
function kitNorm(w){var o={};if(w&&typeof w==='object'){KIT.forEach(function(k){var x=w[k.id];if(x&&typeof x==='object'){o[k.id]={on:!!x.on};['t','w','d','o'].forEach(function(f){if(typeof x[f]==='string')o[k.id][f]=x[f];});}});}return o;}
var KIT_PICK={me:'Likely to surface in my area',team:'Likely to surface for our strategy'};
function kitDraw(mode){
  var host=u5el(mode==='me'?'kitMe':'kitTeam');if(!host)return;
  host.innerHTML=CHECKS.map(function(c,ci){
    return '<div class="u5-kh"><span class="u5-kh-c">'+u5esc(c.name+' · '+c.tool)+'</span><span class="u5-kh-l">'+u5esc(c.line)+'</span><span class="u5-kc" id="kc_'+mode+'_'+ci+'"></span></div>'+
      KIT.filter(function(k){return k.c===ci;}).map(function(k){
        var st=kitGet(mode,k.id),pre='kit_'+mode+'_'+k.id;
        return '<div class="u5-ke'+(st.on?' on':'')+'" id="'+pre+'"><div class="u5-ke-top"><div class="u5-ke-n">'+u5esc(k.n)+'</div>'+
          '<p class="u5-ke-t"><b>Likely trigger</b>'+u5esc(k.trig)+'</p><p class="u5-ke-t"><b>Look out for</b>'+u5esc(k.cues[0])+' '+u5esc(k.cues[1])+'</p>'+
          '<button type="button" class="u5-ke-h" aria-pressed="'+(st.on?'true':'false')+'" onclick="kitToggle(\''+mode+'\',\''+k.id+'\')"><span class="u5-ke-box">'+(st.on?'&#10003;':'')+'</span>'+
          '<span>'+KIT_PICK[mode]+'</span></button></div>'+
          '<div class="u5-ke-b">'+
          KIT_F[mode].map(function(f){
            var fid=pre+'_'+f[0];
            return '<label class="wp-label" for="'+fid+'">'+f[1]+'</label>'+(f[0]==='o'?
              '<input type="text" class="u5-in" id="'+fid+'" maxlength="120" placeholder="'+f[2]+'" value="'+u5esc(st[f[0]]||'')+'" oninput="kitIn(\''+mode+'\',\''+k.id+'\',\''+f[0]+'\',this.value)">':
              '<textarea class="wp-ta" id="'+fid+'" placeholder="'+f[2]+'" oninput="kitIn(\''+mode+'\',\''+k.id+'\',\''+f[0]+'\',this.value)">'+u5esc(st[f[0]]||'')+'</textarea>');
          }).join('')+'</div></div>';
      }).join('');
  }).join('')+(mode==='me'?'<div class="u5-note" id="kitMeMsg" style="display:none;"></div>':'');
  kitCounts(mode);
}
function kitCounts(mode){
  CHECKS.forEach(function(c,ci){
    var el=u5el('kc_'+mode+'_'+ci);if(!el)return;
    var n=KIT.filter(function(k){return k.c===ci&&kitGet(mode,k.id).on;}).length;
    el.textContent=n?(n+' selected'):'None selected yet';el.className='u5-kc'+(n?' ok':'');
  });
}
function u5Step(i){var t=document.querySelectorAll('#mod4 .step-tab');if(t[i]){t[i].click();t[i].scrollIntoView({behavior:'smooth',block:'start'});}}
function kitText(mode,ci){
  return KIT.filter(function(k){return (ci===undefined||k.c===ci)&&kitGet(mode,k.id).on;}).map(function(k){
    var st=kitGet(mode,k.id),c=CHECKS[k.c];
    return (ci===undefined?c.name+' · '+c.tool+' · ':'')+k.n+'\nCues: '+k.cues[0]+' '+k.cues[1]+'\nTrigger: '+k.trig+'\n'+
      KIT_F[mode].map(function(f){return f[1]+': '+String(st[f[0]]||'').trim();}).join('\n');
  }).join('\n\n');
}
function kitSaveSoon(mode){
  if(mode==='me'){u5later('kitMe',async function(){var ok=(await u5save('__kit_me',U5.me))&&(await u5save('kit_me',kitText('me')));u5msg('kitMeMsg',ok?'✓ Saved to your portfolio':'Not saved. Check your connection.',ok?'ok':'');},800);}
  else{u5later('kitTeam',async function(){await u5save('__kit_team',U5.team);await u5save('kit_team',kitText('team'));},800);}
}
function kitEdited(mode){
  if(mode==='team'){
    if(u5drop(KIT_NAMES)){u5later('conf',function(){u5save('confirmed_items',U5.conf);},600);u5msg('kitMsg','');}
    u5later('kitRec',kitRecDraw,300);
  }
  kitSaveSoon(mode);
}
function kitToggle(mode,id){
  var st=kitGet(mode,id);st.on=!st.on;
  var el=u5el('kit_'+mode+'_'+id);
  if(el){el.className='u5-ke'+(st.on?' on':'');var b=el.querySelector('.u5-ke-h');b.setAttribute('aria-pressed',st.on?'true':'false');el.querySelector('.u5-ke-box').innerHTML=st.on?'&#10003;':'';}
  kitCounts(mode);kitEdited(mode);
}
function kitIn(mode,id,f,val){kitGet(mode,id)[f]=String(val||'');kitEdited(mode);}
function kitOpen(){
  var open=[];
  CHECKS.forEach(function(c,ci){
    var sel=KIT.filter(function(k){return k.c===ci&&kitGet('team',k.id).on;});
    if(!sel.length){open.push('select a trigger under '+c.name);return;}
    sel.forEach(function(k){var st=kitGet('team',k.id);if(KIT_F.team.some(function(f){return !String(st[f[0]]||'').trim();}))open.push('complete '+k.n);});
  });
  return open;
}
function kitRecDraw(){
  var host=u5el('kitOutP');if(!host)return;
  var conf=u5has(KIT_NAMES),msg=u5el('kitMsg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u5-out">'+u5recHead('Your group&rsquo;s Team Alignment Plan',KIT_NAMES)+'<div class="u5-rec">'+CHECKS.map(function(c,ci){
    var t=kitText('team',ci);
    return '<div class="u5-rec-s">'+u5esc(c.name+' · '+c.tool)+'</div><div class="u5-rec-t">'+(t?u5esc(t):'<i>to be agreed by your group</i>')+'</div>';
  }).join('')+'</div><div class="u5-btnrow"><button type="button" class="u5-b ok" id="kitConfBtn" onclick="kitConfirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u5-b" onclick="kitPrint()">Print</button></div>'+
    '<div class="u5-note" id="kitMsg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u5el('kitMsg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function kitConfirm(){
  var open=kitOpen();
  if(open.length){kitRecDraw();u5msg('kitMsg','Before you confirm: '+open.join('; ')+'.');return;}
  clearTimeout(_u5t.kitTeam);clearTimeout(_u5t.conf);
  var ok=(await u5save('__kit_team',U5.team))&&(await u5save('kit_team',kitText('team')));
  for(var i=0;i<CHECKS.length;i++){ok=ok&&(await u5save(KIT_KEYS[i],kitText('team',i)));}
  if(!ok){u5msg('kitMsg','Not saved. Check your connection, then select Confirm again.');return;}
  KIT_NAMES.forEach(function(nm){if(U5.conf.indexOf(nm)<0)U5.conf.push(nm);});
  if(!(await u5save('confirmed_items',U5.conf))){u5drop(KIT_NAMES);kitRecDraw();u5msg('kitMsg','Not saved. Check your connection, then select Confirm again.');return;}
  kitRecDraw();u5msg('kitMsg','✓ Confirmed. Your Team Alignment Plan is ready for your team’s Capstone Blueprint.','ok');
}
function kitPrint(){
  var body=CHECKS.map(function(c,ci){var t=kitText('team',ci);return '<h2>'+u5esc(c.name+' · '+c.tool)+'</h2><p>'+(t?u5esc(t).replace(/\n/g,'<br>'):'—')+'</p>';}).join('');
  u5print('Team Alignment Plan','Strategy2Results® · Module 3 · Unit 5 · Section 5 · Step 3 · Capstone work · '+(u5has(KIT_NAMES)?'confirmed':'not yet confirmed'),body);
}

/* ── Start: draw the tools empty, then fill them from the saved answers ───────────────────────── */
function u5DrawAll(){ocGridDraw();ocProfileDraw();kitDraw('me');kitDraw('team');kitRecDraw();}
function u5Init(responses){
  responses=responses||{};
  U5.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U5.oc=ocNorm(responses.__oceavl_work);
  U5.me=kitNorm(responses.__kit_me);
  U5.team=kitNorm(responses.__kit_team);
  U5.ready=true;
  u5DrawAll();
  u5Bring(false);
}
document.addEventListener('DOMContentLoaded',function(){
  U5.oc=ocBlank();
  var k=u5el('u5KissP');if(k)k.innerHTML=u5KissHtml('','');
  u5DrawAll();
});
