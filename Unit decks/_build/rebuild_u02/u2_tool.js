// ══════════════════════════════════════════════════════════════════════════════
// UNIT 2 · STRATEGY INTENT DESIGN (Section 4)
// Strategy Architecture (14 elements) → Strategy Intent Statement → Success in Practice.
// Step 1 follows Carol's S2R Strategy Architect tool (v15, "Define Strategy" mode). Steps 2 and 3 are written by the
// group itself: the page does not draft the Intent or the SiP statements. Answers save to the
// portal database through S2R.save; every key is listed in Unit decks/_build/rebuild_u02/README.md.
// ══════════════════════════════════════════════════════════════════════════════
var EL=__ELEMENTS__;
var ARCH_GROUPS=__GROUPS__;
var SIPD=__SIPD__;
var DIM4=[
  ['WHAT','Scope & Definition','The value chosen and field of play.'],
  ['WHY','Purpose & Rationale','The rationale for the choices and why they matter.'],
  ['HOW','Mechanism & Model','The operating model, capabilities and mechanisms through which the value will be delivered.'],
  ['WHEN','Timing & Sequencing','The timing, sequencing and strategic moves through which the ambition will be pursued.']
];
var U2={v:{},conf:[],cur:0,refine:{}};
var N_ARCH='Strategy Architecture',N_INTENT='Strategy Intent Statement',N_SIP='Success in Practice';

function pad2(n){return (n<10?'0':'')+n;}
function qk(i,j){return 'arch_e'+pad2(i+1)+'_q'+(j+1);}
function rk(i){return 'arch_e'+pad2(i+1)+'_rs';}
function cn(i){return 'Element '+(i+1)+' · '+EL[i].n;}
function sqk(d,j){return 'sip_d'+(d+1)+'_q'+(j+1);}
function ssk(d){return 'sip_d'+(d+1)+'_st';}
function scn(d){return 'SiP · '+SIPD[d].t;}
function u2v(k){var x=U2.v[k];return (x===undefined||x===null)?'':String(x);}
function u2esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u2el(id){return document.getElementById(id);}
function u2msg(id,text){var m=u2el(id);if(!m)return;m.textContent=text;m.style.display=text?'block':'none';}
async function u2put(k,val){
  U2.v[k]=val;refreshMirrors();
  if(!window.S2R){console.warn('[unit2_m1_lens1_p] S2R helper not loaded');return false;}
  return await S2R.save('u2m1_lens1',k,val);
}
function isConf(name){return U2.conf.indexOf(name)>=0;}
async function setConf(name,on){
  var i=U2.conf.indexOf(name);
  if(on&&i<0)U2.conf.push(name);else if(!on&&i>=0)U2.conf.splice(i,1);else return;
  if(window.S2R)await S2R.save('u2m1_lens1','confirmed_items',U2.conf);
}

// ── Step 1 · the 14 elements ──────────────────────────────────────────────────
function elAnswers(i){return EL[i].qs.map(function(_,j){return u2v(qk(i,j)).replace(/\s+/g,' ').trim();}).filter(Boolean);}
function elAuto(i){
  return 'Based on your inputs, your '+EL[i].n+' position is currently saying:\n\n'+
    elAnswers(i).map(function(a){return '• '+a;}).join('\n')+
    '\n\nThis is the position that now needs to be tested against the other elements of the strategy.';
}
function elRefined(i){var p=u2v(rk(i)).trim();return !!p&&p.indexOf('Based on your inputs, your ')!==0;}
function confirmedCount(){var n=0;EL.forEach(function(_,i){if(isConf(cn(i)))n++;});return n;}
function allElConf(){return confirmedCount()===EL.length;}

function renderElNav(){
  var nav=u2el('elNavP');if(!nav)return;
  nav.innerHTML=EL.map(function(e,i){
    var done=isConf(cn(i));
    return '<button type="button" class="u2-chip'+(i===U2.cur?' active':'')+(done?' done':'')+'" onclick="elGo('+i+')"><span class="u2-chip-n">'+(done?'✓':(i+1))+'</span>'+u2esc(e.n)+'</button>';
  }).join('');
  var n=confirmedCount();
  var pct=u2el('elPctP');if(pct)pct.textContent=n+' of '+EL.length+' confirmed';
  var bar=u2el('elBarP');if(bar)bar.style.width=Math.round(n/EL.length*100)+'%';
}
function renderEl(){
  var host=u2el('elWorkP');if(!host)return;
  var i=U2.cur,e=EL[i],pos=u2v(rk(i)),done=isConf(cn(i));
  var qs=e.qs.map(function(q,j){
    return '<label class="u2-q" for="elAns_'+j+'">'+(j+1)+'. '+u2esc(q)+'</label>'+
      '<textarea class="port-ta u2-ans" id="elAns_'+j+'" placeholder="Enter the strategic decision, reasoning or evidence..." oninput="elInput('+j+',this.value)" onchange="elChange('+j+')">'+u2esc(u2v(qk(i,j)))+'</textarea>';
  }).join('');
  var gen='';
  if(pos){
    gen='<div class="u2-gen" id="elGenBox">'+
      '<div class="u2-gen-lbl">Generated strategic interpretation'+(done?'<span class="u2-pill">Confirmed</span>':'')+'</div>'+
      '<div class="u2-gen-h">Is this what you mean?</div>'+
      '<p class="u2-gen-txt">'+u2esc(pos)+'</p>'+
      '<div class="u2-btnrow">'+
        '<button type="button" class="u2-b'+(done?' ok':'')+'" onclick="elConfirm()">✓ Yes, confirm</button>'+
        '<button type="button" class="u2-b" onclick="elRefineOpen()">No, refine</button>'+
        '<button type="button" class="u2-b" onclick="elGenerate()">Regenerate</button>'+
      '</div>'+
      (U2.refine[i]?'<textarea class="u2-ref-ta" id="'+'elRefTa'+'" placeholder="State what the strategic position should say...">'+u2esc(elRefined(i)?pos:'')+'</textarea>'+
        '<div class="u2-btnrow"><button type="button" class="u2-b" onclick="elRefineApply()">Apply refinement</button></div>':'')+
    '</div>';
  }
  host.innerHTML='<div class="port-block u2-el">'+
    '<div class="port-head"><div class="port-lbl">Element '+(i+1)+' of '+EL.length+'</div>'+
      '<div class="u2-el-name">'+u2esc(e.n)+'</div><div class="u2-el-tag">'+u2esc(e.tag)+'</div>'+
      '<div class="port-desc">'+u2esc(e.guide)+'</div></div>'+
    '<div class="u2-el-body">'+qs+
      '<div class="u2-btnrow"><button type="button" class="sip-save-btn" style="margin-top:0;" onclick="elGenerate()">Generate what this is saying</button></div>'+
      '<div class="u2-note" id="elMsg" style="display:none;"></div>'+gen+
    '</div></div>'+
    '<div class="u2-elnav"><button type="button" class="btn" onclick="elMove(-1)"'+(i===0?' disabled':'')+'>← Previous element</button>'+
    '<button type="button" class="btn" onclick="elMove(1)">'+(i===EL.length-1?'Save':'Save and continue →')+'</button></div>';
}
function renderStep1(){renderElNav();renderEl();renderArch();}
// Typing in an answer changes what the element is saying, so the generated position and its confirmation are cleared.
function elInput(j,val){
  var i=U2.cur;U2.v[qk(i,j)]=val;
  if(u2v(rk(i))||isConf(cn(i))){
    U2.v[rk(i)]='';U2._stale=U2._stale||{};U2._stale[i]=true;
    var k=U2.conf.indexOf(cn(i));if(k>=0)U2.conf.splice(k,1);
    var box=u2el('elGenBox');if(box)box.style.display='none';
    renderElNav();
  }
}
async function elChange(j){
  var i=U2.cur;await u2put(qk(i,j),u2v(qk(i,j)));renderIntentCards();
  if(U2._stale&&U2._stale[i]){
    U2._stale[i]=false;
    await u2put(rk(i),'');
    if(window.S2R)await S2R.save('u2m1_lens1','confirmed_items',U2.conf);
    renderArch();
  }
}
async function elFlush(i){
  for(var j=0;j<EL[i].qs.length;j++){var ta=u2el('elAns_'+j);if(ta&&i===U2.cur)await u2put(qk(i,j),ta.value);}
  renderIntentCards();
}
async function elGenerate(){
  var i=U2.cur;await elFlush(i);
  if(!elAnswers(i).length){u2msg('elMsg','Answer the questions for this element first.');return;}
  await u2put(rk(i),elAuto(i));await setConf(cn(i),false);U2.refine[i]=false;renderStep1();
}
async function elConfirm(){var i=U2.cur;await setConf(cn(i),true);U2.refine[i]=false;renderStep1();}
function elRefineOpen(){U2.refine[U2.cur]=true;renderEl();var ta=u2el('elRefTa');if(ta)ta.focus();}
async function elRefineApply(){
  var i=U2.cur,ta=u2el('elRefTa'),v=ta?ta.value.trim():'';
  if(!v){u2msg('elMsg','State what the strategic position should say, then apply.');return;}
  await u2put(rk(i),v);await setConf(cn(i),true);U2.refine[i]=false;renderStep1();
}
function elGo(i){elFlush(U2.cur);U2.cur=i;renderElNav();renderEl();}
async function elMove(d){
  await elFlush(U2.cur);
  U2.cur=Math.max(0,Math.min(EL.length-1,U2.cur+d));renderElNav();renderEl();
  var nav=u2el('elNavP');if(nav&&nav.scrollIntoView)nav.scrollIntoView({behavior:'smooth',block:'start'});
}

// ── Step 1 · Strategy Architecture output ─────────────────────────────────────
function elIndex(name){for(var i=0;i<EL.length;i++){if(EL[i].n===name)return i;}return -1;}
// A refined position replaces the raw answers for that element.
function elText(name){var i=elIndex(name);if(i<0)return '';return elRefined(i)?u2v(rk(i)).replace(/\s+/g,' ').trim():elAnswers(i).join(' ');}
function archSeed(){
  return ARCH_GROUPS.map(function(g){
    return g[0]+'\n'+g[1].map(function(n){var t=elText(n);return t?n+': '+t:'';}).filter(Boolean).join('\n');
  }).join('\n\n');
}
function u2locked(text){return '<div class="u2-locked">'+text+'</div>';}
function renderArch(){
  var host=u2el('archStageP');if(!host)return;
  var out=u2v('arch_output'),done=isConf(N_ARCH),html='';
  if(!allElConf()&&!out){
    html=u2locked('Complete and confirm all 14 elements to unlock the Strategy Architecture output. '+confirmedCount()+' of '+EL.length+' confirmed.');
  }else if(!out){
    html='<div class="u2-ok">✓ 14 of 14 elements confirmed.</div><div class="u2-btnrow"><button type="button" class="sip-save-btn" style="margin-top:0;" onclick="archBuild()">Build Strategy Architecture Output</button></div>';
  }else{
    html=(allElConf()?'<div class="u2-ok">✓ 14 of 14 elements confirmed.</div>':'<div class="u2-note">'+confirmedCount()+' of '+EL.length+' elements confirmed. Confirm the outstanding elements, then rebuild.</div>')+
      '<div class="port-block" style="margin-top:10px;">'+
      '<div class="port-head"><div class="port-lbl">Strategy Architecture Output<span class="u2-pill" id="archPill"'+(done?'':' style="display:none;"')+'>Confirmed</span></div>'+
      '<div class="port-desc">Review the integrated output from the 14 elements. Refine it until it accurately represents your organisation\'s strategic architecture.</div></div>'+
      '<textarea class="port-ta" id="'+'arch_output'+'" style="min-height:260px;" oninput="archInput(this.value)" onchange="archChange()">'+u2esc(out)+'</textarea>'+
      '<div class="u2-btnrow u2-pad">'+
        '<button type="button" id="archBtn" class="u2-b'+(done?' ok':'')+'" onclick="archConfirm()">✓ Confirm Strategy Architecture</button>'+
        '<button type="button" class="u2-b" onclick="archBuild(true)">Rebuild from 14 elements</button>'+
        (done?'<button type="button" class="u2-b" onclick="u2Print(\'arch\')">Print Architecture Output</button>':'')+
      '</div></div>';
  }
  host.innerHTML=html;
}
async function archBuild(rebuild){
  if(!allElConf()){renderArch();return;}
  var cur=u2v('arch_output').trim(),seed=archSeed();
  if(rebuild&&cur&&cur!==seed.trim()&&!confirm('Replace the current text with a fresh build from the 14 elements?'))return;
  await u2put('arch_output',seed);await setConf(N_ARCH,false);renderArch();
}
// Editing a confirmed output removes its confirmation at once, without redrawing the box the group is typing in.
function archInput(val){
  U2.v['arch_output']=val;refreshMirrors();
  if(isConf(N_ARCH)){
    U2.conf.splice(U2.conf.indexOf(N_ARCH),1);U2._adirty=true;
    var pill=u2el('archPill');if(pill)pill.style.display='none';
    var btn=u2el('archBtn');if(btn)btn.classList.remove('ok');
  }
}
async function archChange(){
  await u2put('arch_output',u2v('arch_output'));
  if(U2._adirty){U2._adirty=false;if(window.S2R)await S2R.save('u2m1_lens1','confirmed_items',U2.conf);}
}
async function archConfirm(){
  var ta=u2el('arch_output');if(ta)await u2put('arch_output',ta.value);
  if(!u2v('arch_output').trim())return;
  await setConf(N_ARCH,true);renderArch();
}

// ── Step 2 · Strategy Intent Statement (the group deduces it and writes it in) ─────────────
function intentCardsHtml(){
  return DIM4.map(function(d){
    var i=elIndex(d[0]),a=i<0?[]:elAnswers(i);
    return '<div class="u2-card"><div class="u2-card-h">'+d[0]+' — '+u2esc(d[1])+'</div><p>'+u2esc(d[2])+'</p>'+
      '<div class="u2-mirror-lbl">From your Strategy Architecture</div>'+
      (a.length?'<ul class="u2-src">'+a.map(function(x){return '<li>'+u2esc(x)+'</li>';}).join('')+'</ul>':'<div class="u2-mirror empty">Appears here once this element is answered in 4.1.</div>')+'</div>';
  }).join('');
}
// The four cards follow the answers in 4.1. They are redrawn on their own, so the statement box is never disturbed.
function renderIntentCards(){var c=u2el('intentCardsP');if(c)c.innerHTML=intentCardsHtml();}
function renderIntent(){
  var host=u2el('intentStageP');if(!host)return;
  var done=isConf(N_INTENT);
  host.innerHTML='<div class="u2-grid" id="intentCardsP">'+intentCardsHtml()+'</div>'+
    '<div class="port-block">'+
      '<div class="port-head"><div class="port-lbl">Strategy Intent Statement<span class="u2-pill" id="intentPill"'+(done?'':' style="display:none;"')+'>Confirmed</span></div>'+
      '<div class="port-desc">Review the four dimensions together and write one crisp statement of strategic ambition. The Architecture holds the detail; the Intent establishes the ambition.</div></div>'+
      '<textarea class="port-ta" id="'+'intent_statement'+'" style="min-height:130px;" placeholder="Write your group\'s Strategy Intent Statement here..." oninput="intentInput(this.value)" onchange="intentChange()">'+u2esc(u2v('intent_statement'))+'</textarea>'+
      '<div class="u2-btnrow u2-pad">'+
        '<button type="button" id="intentBtn" class="u2-b'+(done?' ok':'')+'" onclick="intentConfirm()">✓ Confirm Strategy Intent</button>'+
        (done?'<button type="button" class="u2-b" onclick="u2Print(\'intent\')">Print Intent Output</button>':'')+
      '</div><div class="u2-note u2-pad" id="intentMsg" style="display:none;"></div></div>';
}
function intentInput(val){
  U2.v['intent_statement']=val;refreshMirrors();
  if(isConf(N_INTENT)){
    U2.conf.splice(U2.conf.indexOf(N_INTENT),1);U2._idirty=true;
    var pill=u2el('intentPill');if(pill)pill.style.display='none';
    var btn=u2el('intentBtn');if(btn)btn.classList.remove('ok');
  }
}
async function intentChange(){
  await u2put('intent_statement',u2v('intent_statement'));
  if(U2._idirty){U2._idirty=false;if(window.S2R)await S2R.save('u2m1_lens1','confirmed_items',U2.conf);}
}
async function intentConfirm(){
  var ta=u2el('intent_statement');if(ta)await u2put('intent_statement',ta.value);
  if(!u2v('intent_statement').trim()){u2msg('intentMsg','Write your Strategy Intent Statement first.');return;}
  await setConf(N_INTENT,true);renderIntent();
}

// ── Step 3 · Success in Practice (three questions and one written statement per domain) ────
var SIP_COL=['#8ab0e8','var(--gold)','#5ecba1','#c39de0'];
function sipAllConf(){for(var d=0;d<SIPD.length;d++){if(!isConf(scn(d)))return false;}return true;}
function sipFinalHtml(){
  if(!sipAllConf())return '';
  var done=isConf(N_SIP);
  return '<div class="port-block" style="margin-top:16px;"><div class="port-head"><div class="port-lbl">Success in Practice'+(done?'<span class="u2-pill">Confirmed</span>':'')+'</div>'+
    '<div class="port-desc">Read the four statements as one enterprise picture. Each statement captures the critical success condition from its SiP domain; the supporting detail stays in the domain answers above.</div></div>'+
    '<div class="u2-el-body">'+SIPD.map(function(x,d){
      return '<div class="u2-final"><div class="u2-final-h" style="color:'+SIP_COL[d]+';">'+(d+1)+' · '+u2esc(x.t)+'</div><div class="u2-final-t">'+u2esc(u2v(ssk(d)).trim())+'</div></div>';
    }).join('')+'</div>'+
    '<div class="u2-btnrow u2-pad"><button type="button" class="u2-b'+(done?' ok':'')+'" onclick="sipConfirmAll()">✓ Confirm Success in Practice</button>'+
    (done?'<button type="button" class="u2-b" onclick="u2Print(\'sip\')">Print SiP Output</button><button type="button" class="u2-b ok" onclick="u2Print(\'full\')">Print Strategy Intent Design Report</button>':'')+
    '</div></div>';
}
function renderSip(){
  var host=u2el('sipStageP');if(!host)return;
  var cards=SIPD.map(function(x,d){
    var inputs=x.qs.map(function(q,j){
      return '<label class="u2-q" for="sipIn_'+d+'_'+j+'">'+u2esc(q)+'</label>'+
        '<textarea class="sip-ta u2-sipin" id="sipIn_'+d+'_'+j+'" oninput="sipInput('+d+','+j+',this.value)" onchange="sipChange('+d+','+j+')">'+u2esc(u2v(sqk(d,j)))+'</textarea>';
    }).join('');
    var done=isConf(scn(d));
    return '<div class="port-block u2-sipd"><div class="port-head"><div class="port-lbl" style="color:'+SIP_COL[d]+';">D'+(d+1)+' · '+u2esc(x.t)+'</div><div class="port-desc">'+u2esc(x.lead)+'</div></div>'+
      '<div class="u2-el-body">'+inputs+'</div>'+
      '<div class="u2-gen"><div class="u2-gen-lbl">Your group\'s statement for this domain<span class="u2-pill" id="sipPill_'+d+'"'+(done?'':' style="display:none;"')+'>Confirmed</span></div>'+
        '<textarea class="u2-ref-ta" id="sipSt_'+d+'" placeholder="From your three answers, write one statement of what success looks like in this domain..." oninput="sipStInput('+d+',this.value)" onchange="sipStChange('+d+')">'+u2esc(u2v(ssk(d)))+'</textarea>'+
        '<div class="u2-btnrow"><button type="button" id="sipBtn_'+d+'" class="u2-b'+(done?' ok':'')+'" onclick="sipConfirm('+d+')">✓ Confirm statement</button></div>'+
        '<div class="u2-note" id="sipMsg_'+d+'" style="display:none;"></div></div></div>';
  }).join('');
  host.innerHTML='<div class="u2-grid u2-sipgrid">'+cards+'</div><div id="sipFinalP">'+sipFinalHtml()+'</div>';
}
function sipInput(d,j,val){U2.v[sqk(d,j)]=val;}
async function sipChange(d,j){await u2put(sqk(d,j),u2v(sqk(d,j)));}
// Editing a confirmed statement removes its confirmation at once, without redrawing the boxes the group is typing in.
function sipStInput(d,val){
  U2.v[ssk(d)]=val;refreshMirrors();
  if(isConf(scn(d))||isConf(N_SIP)){
    [scn(d),N_SIP].forEach(function(n){var k=U2.conf.indexOf(n);if(k>=0)U2.conf.splice(k,1);});
    U2._sdirty=true;
    var pill=u2el('sipPill_'+d);if(pill)pill.style.display='none';
    var btn=u2el('sipBtn_'+d);if(btn)btn.classList.remove('ok');
    var fin=u2el('sipFinalP');if(fin)fin.innerHTML='';
  }
}
async function sipStChange(d){
  await u2put(ssk(d),u2v(ssk(d)));
  if(U2._sdirty){U2._sdirty=false;if(window.S2R)await S2R.save('u2m1_lens1','confirmed_items',U2.conf);}
}
async function sipConfirm(d){
  var ta=u2el('sipSt_'+d);if(ta)await u2put(ssk(d),ta.value);
  if(!u2v(ssk(d)).trim()){u2msg('sipMsg_'+d,'Write your statement for this domain first.');return;}
  await setConf(scn(d),true);renderSip();
}
async function sipConfirmAll(){
  if(!sipAllConf())return;
  await setConf(N_SIP,true);renderSip();
}

// ── Printed outputs: Architecture · Intent · SiP · full Strategy Intent Design report ──
function rptArch(){
  var names=EL.map(function(e){return e.n;}),groups=ARCH_GROUPS.map(function(g){return g[0];});
  var html='',open=false;
  u2v('arch_output').split(/\r?\n/).forEach(function(raw){
    var line=raw.trim();if(!line)return;
    if(groups.indexOf(line)>=0){if(open)html+='</div>';html+='<div class="group"><div class="group-title">'+u2esc(line)+'</div>';open=true;return;}
    if(!open){html+='<div class="group">';open=true;}
    var k=line.indexOf(':'),label=k>0?line.slice(0,k).trim():'';
    if(label&&names.indexOf(label)>=0)html+='<div class="arch-row"><div class="arch-label">'+u2esc(label)+'</div><div class="arch-text">'+u2esc(line.slice(k+1).trim())+'</div></div>';
    else html+='<div class="arch-row"><div class="arch-label"></div><div class="arch-text">'+u2esc(line)+'</div></div>';
  });
  if(open)html+='</div>';
  return '<section class="section"><div class="section-title">Strategy Architecture</div><div class="section-rule"></div>'+html+'</section>';
}
function rptIntent(){
  return '<section class="section"><div class="section-title">Strategy Intent Statement</div><div class="section-rule"></div><div class="intent-panel">'+u2esc(u2v('intent_statement'))+'</div></section>';
}
function rptSip(){
  return '<section class="section"><div class="section-title">Success in Practice</div><div class="section-rule"></div>'+
    SIPD.map(function(x,d){return '<div class="sip-card"><div class="sip-kicker">Statement '+(d+1)+'</div><div class="sip-title">'+u2esc(x.t)+'</div><div class="sip-text">'+u2esc(u2v(ssk(d)))+'</div></div>';}).join('')+'</section>';
}
function rptShell(title,body){
  var org=u2v('org_name').trim()||'Organisation',period=u2v('strategy_period').trim();
  return '<!doctype html><html><head><meta charset="utf-8"><title>'+u2esc(title)+'</title><style>'+
    '@page{size:A4;margin:17mm 16mm 18mm}*{box-sizing:border-box}'+
    'body{font-family:Arial,Helvetica,sans-serif;color:#1f2a24;line-height:1.52;font-size:10.2pt;margin:0}'+
    '.topline{height:5px;background:#C6A24C;margin-bottom:18px}'+
    '.brand{font-size:8.5pt;letter-spacing:.14em;font-weight:800;color:#1A5C2C;text-transform:uppercase}'+
    'h1{font-size:23pt;line-height:1.12;margin:7px 0 5px;color:#12301c}'+
    '.meta{margin:0 0 22px;color:#687482;font-size:9.5pt}.meta strong{color:#12301c}'+
    '.section{margin:0 0 26px}.section-title{font-size:16pt;font-weight:800;color:#12301c;margin:0 0 5px}'+
    '.section-rule{height:3px;width:58px;background:#C6A24C;margin:0 0 16px}'+
    '.group{margin:0 0 21px}.group-title{font-size:11.5pt;font-weight:800;color:#1A5C2C;text-transform:uppercase;letter-spacing:.04em;margin:0 0 9px;padding-bottom:5px;border-bottom:1px solid #d9e0e5;page-break-after:avoid;break-after:avoid}'+
    '.arch-row{display:grid;grid-template-columns:145px 1fr;gap:13px;margin:0 0 11px;page-break-inside:avoid}'+
    '.arch-label{font-size:9.3pt;font-weight:800;color:#12301c;text-transform:uppercase;letter-spacing:.025em}.arch-text{font-size:10pt;color:#2b3a31}'+
    '.intent-panel{border-left:5px solid #C6A24C;background:#f4f6f1;padding:18px 20px;margin-top:12px;font-size:13.2pt;line-height:1.58;color:#12301c;font-weight:600;page-break-inside:avoid;white-space:pre-wrap}'+
    '.sip-card{border:1px solid #d9e0e5;border-left:5px solid #1A5C2C;border-radius:5px;padding:14px 16px;margin:0 0 13px;page-break-inside:avoid}'+
    '.sip-kicker{font-size:8.5pt;font-weight:800;letter-spacing:.09em;color:#a8862f;text-transform:uppercase;margin-bottom:3px}'+
    '.sip-title{font-size:11.5pt;font-weight:800;color:#12301c;margin:0 0 7px}.sip-text{font-size:10.2pt;color:#2b3a31;white-space:pre-wrap}'+
    '.summary-band{background:#1A5C2C;color:#fff;padding:10px 14px;margin:22px 0 15px;font-weight:700;font-size:10pt}'+
    '.footer{margin-top:30px;padding-top:9px;border-top:1px solid #d9e0e5;font-size:8.2pt;color:#7a8490}'+
    '@media print{.report-break{page-break-before:always}}'+
    '</style></head><body><div class="topline"></div>'+
    '<div class="brand">Strategy2Results® · Module 2 · Unit 2</div><h1>'+u2esc(title)+'</h1>'+
    '<div class="meta"><strong>'+u2esc(org)+'</strong>'+(period?' &nbsp;·&nbsp; Strategy Period: '+u2esc(period):'')+'</div>'+body+
    '<div class="footer">Strategy2Results® &nbsp;·&nbsp; Institute of Behavioural Strategy &amp; Leadership</div>'+
    '<scr'+'ipt>window.onload=function(){window.print();};<\/scr'+'ipt></body></html>';
}
function u2Print(kind){
  var title,body;
  if(kind==='arch'){title='Strategy Architecture';body=rptArch();}
  else if(kind==='intent'){title='Strategy Intent';body=rptIntent();}
  else if(kind==='sip'){title='Success in Practice';body=rptSip();}
  else{title='Strategy Intent Design';body='<div class="summary-band">Strategy Architecture → Strategy Intent → Success in Practice</div>'+rptArch()+'<div class="report-break"></div>'+rptIntent()+rptSip();}
  var w=window.open('','_blank');
  if(!w){alert('Please allow pop-ups for this page to print this output.');return;}
  w.document.open();w.document.write(rptShell(title,body));w.document.close();
}

// ── Read-only copies of the group's outputs, shown where a later step builds on them ──
function refreshMirrors(){
  document.querySelectorAll('[data-mirror]').forEach(function(m){
    var v=u2v(m.getAttribute('data-mirror')).trim();
    if(v){m.textContent=v;m.classList.remove('empty');}
    else{m.textContent=m.getAttribute('data-empty')||'';m.classList.add('empty');}
  });
}
function u2RenderAll(){renderStep1();renderIntent();renderSip();refreshMirrors();}

// ── Plain boxes: organisation, strategy period, Section 5.2 observations (id = response key) ──
var U2_FIELDS=__FIELDS__;
async function saveField(id){
  var el=u2el(id);if(!el)return false;
  var ok=await u2put(id,el.value);
  var msg=u2el(id+'-msg');
  if(msg){
    msg.textContent=ok?'✓ Saved':'⚠ Save failed — try again';
    msg.style.display='block';
    setTimeout(function(){msg.style.display='none';msg.textContent='✓ Saved';},2500);
  }
  return ok;
}
U2_FIELDS.forEach(function(id){
  var el=u2el(id);if(!el)return;
  el.addEventListener('input',function(){U2.v[id]=el.value;});
  el.addEventListener('change',function(){saveField(id);});
});
