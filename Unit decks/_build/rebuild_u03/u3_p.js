// ── UNIT 3 · PARTICIPANT PAGE ───────────────────────────────────────────────────────────────────
var LENS='u2m1_lens2';
var SUMMARY=[
  {arc:"Awareness — What",title:"The KISS Framework as Reflective Filter",body:"You saw that KISS (Keep, Improve, Start, Stop) functions as a reflective filter between strategic vision and execution commitments. Before defining Objectives and Key Results, you examine the organisation's current operating reality in relation to its Success in Practice. This step prevents the common strategic mistake of layering new ambitions on top of an unchanged operational system. Five steps then carry the KISS output into enterprise OKRs."},
  {arc:"Intelligence — Why",title:"Most OKR Failures are Reflection Failures",body:"When organisations move directly from vision to targets, legacy routines remain in place, resources remain misaligned, and teams attempt to pursue transformational goals while still carrying the weight of outdated priorities. The KISS-to-OKR sequence resolves this tension: SiP defines the future, KISS identifies the changes required, and OKRs translate those changes into measurable progress. The worked example showed the full sequence in practice."},
  {arc:"Extrapolating — Where",title:"Functional Bias Creates OKR Hot Zones",body:"Each leader naturally emphasises different SiP domains. Unexamined, these perspectives produce functional OKRs where enterprise OKRs are needed. You matched each leadership role to its typical hot zone and its alignment question. Recognising these patterns allows your group to integrate perspectives into a balanced execution system that reflects the full enterprise."},
  {arc:"Integration — Collective",title:"Individual Expertise into Collective Intelligence",body:"With your group you translated your Success in Practice into a confirmed KISS map across the four SiP domains, then into enterprise priorities and enterprise OKRs through the five steps. Each member began with insights from a functional domain, and the final outcome reflects the success of the enterprise as a whole. The Prioritisation Matrix concentrated execution energy on the priorities that will most accelerate progress toward the SiP. Your confirmed outputs feed your team's Capstone Blueprint."},
  {arc:"Application — In Practice",title:"From Strategic Imagination to Operational Clearance",body:"In Strategy Airport you applied the same translation on your own to a new case. You decided what the company must keep, improve, start and stop, then converted one KISS theme into an Objective and two Key Results with contributing roles. KISS is the evidence base for deciding what the Objective should be and what Key Results will prove progress."}
];
var U3={v:{},conf:[]};
function u3v(k){var x=U3.v[k];return (x===undefined||x===null)?'':String(x);}
function u3el(id){return document.getElementById(id);}
function u3msg(id,text,cls){var m=u3el(id);if(!m)return;m.textContent=text||'';m.className='u3-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u3save(k,val){
  if(!window.S2R){console.warn('[unit2_m1_lens2_p] S2R helper not loaded');return false;}
  return await S2R.save(LENS,k,val);
}
async function u3put(k,val){U3.v[k]=val;u3Mirrors();return await u3save(k,val);}
function isConf(name){return U3.conf.indexOf(name)>=0;}
async function setConfMany(names,on){
  var changed=false;
  names.forEach(function(name){
    var i=U3.conf.indexOf(name);
    if(on&&i<0){U3.conf.push(name);changed=true;}else if(!on&&i>=0){U3.conf.splice(i,1);changed=true;}
  });
  if(changed)await u3save('confirmed_items',U3.conf);
}
function u3Mirrors(){
  document.querySelectorAll('[data-mirror]').forEach(function(m){
    var v=u3v(m.getAttribute('data-mirror')).trim();
    if(v){m.textContent=v;m.classList.remove('empty');}
    else{m.textContent=m.getAttribute('data-empty')||'';m.classList.add('empty');}
  });
}

// ── Teaching content rendered from the shared data ──────────────────────────────────────────────
function renderKissGuideP(){var el=u3el('kissGuideP');if(el)el.innerHTML=kissGuideHtml('kgp_','u3ToggleDomain');}
function renderSummaryP(){
  document.getElementById("summaryP").innerHTML=SUMMARY.map(function(s,i){
    return "<div class=\"sum-block\" id=\"sump_"+i+"\">"+
      "<div class=\"sum-h\" onclick=\"document.getElementById('sump_"+i+"').classList.toggle('open')\">"+
        "<span class=\"sum-arc\">"+s.arc+"</span>"+
        "<span class=\"sum-title\">"+s.title+"</span>"+
        "<span class=\"sum-arr\">▾</span></div>"+
      "<div class=\"sum-body\"><p>"+s.body+"</p></div></div>";
  }).join("");
}

// ── 3.1 · Matching exercise: Typical Hot Zone and Alignment Question to each role (portfolio work) ──
var HZ_ORDER={hot:[6,2,9,0,4,7,1,8,3,5],al:[3,8,1,5,9,0,6,2,7,4]};
var HZ={cur:0,m:[],note:null};
function hzBlank(){return HOT_ZONES.map(function(){return {hot:false,al:false,ht:0,at:0};});}
HZ.m=hzBlank();
function hzDone(i){return HZ.m[i].hot&&HZ.m[i].al;}
function hzCount(){var n=0;HOT_ZONES.forEach(function(_,i){if(hzDone(i))n++;});return n;}
function hzOptions(kind){
  var i=HZ.cur,field=kind==='hot'?'hot':'align',done=HZ.m[i][kind];
  if(done)return '<div class="u3-matched '+kind+'"><span class="u3-pill">Matched</span>'+u3esc(HOT_ZONES[i][field])+'</div>';
  return '<div class="u3-opts">'+HZ_ORDER[kind].map(function(j){
    if(HZ.m[j][kind])return '<div class="u3-opt used"><span>'+u3esc(HOT_ZONES[j][field])+'</span><em>Matched · '+u3esc(HOT_ZONES[j].role)+'</em></div>';
    return '<button type="button" class="u3-opt" onclick="hzPick(\''+kind+'\','+j+')">'+u3esc(HOT_ZONES[j][field])+'</button>';
  }).join('')+'</div>';
}
function hzNote(kind){
  if(!HZ.note||HZ.note.kind!==kind||HZ.note.role!==HZ.cur)return '';
  return '<div class="u3-flash '+(HZ.note.ok?'ok':'bad')+'">'+u3esc(HZ.note.text)+'</div>';
}
function renderMatch(){
  var host=u3el('hzMatchP');if(!host)return;
  var n=hzCount(),i=HZ.cur,h=HOT_ZONES[i],all=n===HOT_ZONES.length;
  var chips=HOT_ZONES.map(function(r,x){
    return '<button type="button" class="u3-chip'+(x===i?' active':'')+(hzDone(x)?' done':'')+'" onclick="hzGo('+x+')"><span class="u3-chip-n">'+(hzDone(x)?'✓':(x+1))+'</span>'+u3esc(r.role)+'</button>';
  }).join('');
  var next='';
  if(hzDone(i)&&!all)next='<div class="u3-btnrow"><button type="button" class="u3-b ok" onclick="hzNext()">Next role →</button></div>';
  host.innerHTML='<div class="u3-progress"><div class="u3-progress-top"><span>Roles matched</span><b>'+n+' of '+HOT_ZONES.length+'</b></div><div class="u3-bar"><span style="width:'+Math.round(n/HOT_ZONES.length*100)+'%"></span></div></div>'+
    '<div class="u3-chips">'+chips+'</div>'+
    (all?'<div class="hbox teal"><p><strong>All ten roles matched.</strong> Select any role above to review its full card. Select Save to Portfolio below.</p></div>':'')+
    '<div class="u3-role"><div class="u3-role-h"><div class="u3-role-n">'+u3esc(h.role)+'</div><div class="u3-role-t">'+u3esc(h.title)+'</div></div>'+
      '<div class="u3-role-given"><div><h5>Dominant Future Realities <span>suggested</span></h5><p>'+u3esc(h.top2)+'</p></div><div><h5>Natural OKR Emphasis <span>suggested</span></h5><p>'+u3esc(h.emphasis)+'</p></div></div>'+
      '<div class="u3-role-q"><h5>Typical Hot Zone</h5><p class="u3-small">Which hot zone does this emphasis create?</p>'+hzOptions('hot')+hzNote('hot')+'</div>'+
      '<div class="u3-role-q"><h5>Alignment Question</h5><p class="u3-small">Which question brings this role back to enterprise thinking?</p>'+hzOptions('al')+hzNote('al')+'</div>'+
      next+'</div>';
}
function hzGo(i){HZ.cur=i;HZ.note=null;renderMatch();}
function hzNext(){
  for(var k=1;k<=HOT_ZONES.length;k++){var j=(HZ.cur+k)%HOT_ZONES.length;if(!hzDone(j)){hzGo(j);return;}}
}
function hzText(){
  var first=0;HZ.m.forEach(function(x){if(x.hot&&x.ht===1)first++;if(x.al&&x.at===1)first++;});
  var one=function(ok,tries){return (ok?'matched':'not yet matched')+(tries?' ('+tries+(tries===1?' attempt':' attempts')+')':'');};
  return hzCount()+' of '+HOT_ZONES.length+' roles matched · '+first+' of '+(HOT_ZONES.length*2)+' matches at the first attempt\n'+
    HOT_ZONES.map(function(h,i){var x=HZ.m[i];return h.role+' — Typical Hot Zone: '+one(x.hot,x.ht)+' · Alignment Question: '+one(x.al,x.at);}).join('\n');
}
async function hzPick(kind,j){
  var i=HZ.cur,x=HZ.m[i];
  if(kind==='hot')x.ht++;else x.at++;
  if(j===i){x[kind]=true;HZ.note={kind:kind,role:i,ok:true,text:'Green light: matched.'};}
  else HZ.note={kind:kind,role:i,ok:false,text:'Red alert: this one belongs to another role. Read the emphasis of this role again, then choose again.'};
  renderMatch();
  await u3save('__hz_match',{cur:HZ.cur,m:HZ.m});
  await u3save('hz_match',hzText());
}

// ── 4.1 · Your group's four SiP statements (brought in from your Unit 2 page) and the KISS form ──
function sipKey(d){return 'sip_d'+(d+1)+'_st';}
function renderSipCapture(){
  var host=u3el('sipCaptureP');if(!host)return;
  host.innerHTML=KISS_DOMAINS.map(function(x,d){
    return '<div class="u3-sipbox"><label class="u3-inlbl" for="'+sipKey(d)+'">D'+(d+1)+' · '+u3esc(x.label)+'</label>'+
      '<textarea class="u3-ta" id="'+sipKey(d)+'" placeholder="Your group\'s SiP statement for this domain..." oninput="sipCapInput('+d+',this.value)" onchange="sipCapChange('+d+')">'+u3esc(u3v(sipKey(d)))+'</textarea></div>';
  }).join('')+'<div class="u3-btnrow"><button type="button" class="u3-b" onclick="sipBring(true)">Bring in from my Unit 2 page</button></div><div class="u3-note" id="sipCapMsg" style="display:none;"></div>';
}
function sipCapInput(d,val){U3.v[sipKey(d)]=val;u3Mirrors();}
async function sipCapChange(d){await u3save(sipKey(d),u3v(sipKey(d)));}
async function sipBring(manual){
  if(!window.S2R){if(manual)u3msg('sipCapMsg','The save system is not ready. Reload the page and try again.');return;}
  var u2={};try{u2=await S2R.loadAll('u2m1_lens1');}catch(e){u2={};}
  var found=[];
  for(var d=0;d<4;d++){var t=u2?u2[sipKey(d)]:null;found.push(typeof t==='string'?t.trim():'');}
  if(!found.some(Boolean)){if(manual)u3msg('sipCapMsg','No SiP statements were found on your Unit 2 page. Type your group\'s four statements in the boxes above.');return;}
  var replaces=found.some(function(t,d){var cur=u3v(sipKey(d)).trim();return t&&cur&&cur!==t;});
  if(manual&&replaces&&!window.confirm('Replace the text in these boxes with the SiP statements from your Unit 2 page?'))return;
  if(!manual&&replaces)return;
  var n=0;
  for(var k=0;k<4;k++){
    if(found[k]&&u3v(sipKey(k)).trim()!==found[k]){U3.v[sipKey(k)]=found[k];var ta=u3el(sipKey(k));if(ta)ta.value=found[k];await u3save(sipKey(k),found[k]);n++;}
  }
  u3Mirrors();
  if(manual)u3msg('sipCapMsg',n?'Brought in from your Unit 2 page.':'The boxes already match your Unit 2 page.','ok');
}

var KISS_NAMES=['KISS · Keep','KISS · Improve','KISS · Start','KISS · Stop'];
var KISS_OUT=['kiss_keep','kiss_improve','kiss_start','kiss_stop'];
function kexKey(d,k){return 'kex_'+d.id+'_'+k;}
function kissFilled(){var n=0;KISS_DOMAINS.forEach(function(d){KISS_EL.forEach(function(k){if(u3v(kexKey(d,k[0])).trim())n++;});});return n;}
function kissConfirmed(){return KISS_NAMES.every(isConf);}
function kissCompose(k){
  return KISS_DOMAINS.map(function(d){return d.label+': '+u3v(kexKey(d,k)).trim().replace(/\s*\n+\s*/g,'; ');}).join('\n');
}
function renderKissForm(){
  var host=u3el('kissFormP');if(!host)return;
  host.innerHTML=KISS_DOMAINS.map(function(d,x){
    return '<div class="kiss-domain" id="kex_'+d.id+'">'+
      '<div class="kiss-domain-h" onclick="u3ToggleDomain(\'kex_'+d.id+'\')">'+
        '<div class="kiss-accent '+d.cls+'"></div>'+
        '<div class="kiss-domain-info"><div class="kiss-domain-title">'+u3esc(d.label)+'</div>'+
        '<div class="kiss-domain-anchor">SiP Anchor: '+u3esc(d.anchor)+'</div></div>'+
        '<span class="kiss-domain-arr"'+(x===0?' style="transform:rotate(180deg)"':'')+'>▾</span></div>'+
      '<div class="kiss-domain-body" style="display:'+(x===0?'block':'none')+';padding:0 18px 18px;">'+
        '<div class="u3-mirror-lbl">Your group\'s SiP statement for this domain</div>'+
        '<div class="u3-mirror empty" data-mirror="'+sipKey(x)+'" data-empty="Capture this SiP statement in the boxes above."></div>'+
        '<div class="u3-kgrid" style="margin-top:12px;">'+KISS_EL.map(function(k){
          var kid=kexKey(d,k[0]);
          return '<div class="kiss-el"><div class="kiss-el-head '+k[0]+'-h">◆ '+k[1]+'</div>'+
            '<div class="kiss-q">'+u3esc(d[k[0]])+'</div>'+
            '<textarea class="kiss-ta" id="'+kid+'" oninput="kexInput(\''+kid+'\',this.value)" onchange="kexChange(\''+kid+'\')" placeholder="Your group\'s agreed entry...">'+u3esc(u3v(kid))+'</textarea>'+
            '<div class="u3-saved" id="'+kid+'-s"></div></div>';
        }).join('')+'</div></div></div>';
  }).join('');
  renderKissConfirm();u3Mirrors();
}
function renderKissConfirm(){
  var host=u3el('kissConfirmP');if(!host)return;
  if(!u3el('kissBtn')){
    host.innerHTML='<div class="u3-progress"><div class="u3-progress-top"><span>KISS entries complete</span><b id="kissCount"></b></div><div class="u3-bar"><span id="kissBar"></span></div></div>'+
      '<div class="u3-btnrow"><button type="button" class="u3-b" id="kissBtn" onclick="kissConfirm()">✓ Confirm KISS map</button><span class="u3-pill" id="kissPill" style="display:none;">Confirmed</span></div>'+
      '<div class="u3-note" id="kissMsg" style="display:none;"></div><div id="kissOut"></div>';
  }
  var done=kissConfirmed(),n=kissFilled();
  u3el('kissCount').textContent=n+' of 16';u3el('kissBar').style.width=Math.round(n/16*100)+'%';
  u3el('kissBtn').classList.toggle('ok',done);u3el('kissPill').style.display=done?'':'none';
  if(done)u3msg('kissMsg','');
  u3el('kissOut').innerHTML=done?'<div class="u3-out"><div class="u3-out-h">Your confirmed KISS map</div>'+KISS_EL.map(function(k,x){
      return '<div class="u3-final"><div class="u3-final-h '+k[0]+'">'+k[1]+'</div><div class="u3-final-t">'+u3esc(u3v(KISS_OUT[x]))+'</div></div>';
    }).join('')+'</div>':'';
}
var _kexTimers={};
function kexInput(kid,val){
  U3.v[kid]=val;
  if(kissConfirmed()){KISS_NAMES.forEach(function(nm){var i=U3.conf.indexOf(nm);if(i>=0)U3.conf.splice(i,1);});U3._kdirty=true;renderKissConfirm();okrRefreshMirror();}
  clearTimeout(_kexTimers[kid]);_kexTimers[kid]=setTimeout(function(){kexChange(kid);},900);
}
async function kexChange(kid){
  clearTimeout(_kexTimers[kid]);
  var ok=await u3save(kid,u3v(kid));
  var s=u3el(kid+'-s');
  if(s){s.textContent=ok?'✓ Saved':'⚠ Save failed — try again';s.style.display='block';if(ok)setTimeout(function(){s.style.display='none';},2000);}
  if(U3._kdirty){U3._kdirty=false;await u3save('confirmed_items',U3.conf);}
  renderKissConfirm();
}
async function kissConfirm(){
  if(kissFilled()<16){u3msg('kissMsg','Complete all sixteen boxes first. Where your group finds nothing for a box, record "None identified".');return;}
  for(var x=0;x<KISS_EL.length;x++){var t=kissCompose(KISS_EL[x][0]);U3.v[KISS_OUT[x]]=t;await u3save(KISS_OUT[x],t);}
  await setConfMany(KISS_NAMES,true);
  renderKissConfirm();okrRefreshMirror();
}

// ── 4.2 · THE FIVE STEPS: themes → Objectives → Key Results → alignment test → Priority Matrix (group work) ──
// Each step shows what the steps before it produced: the theme is carried into Step 2, theme and Objective into
// Step 3, theme, Objective and Key Results into Step 4, and the aligned OKR into Step 5.
// Above the steps one record builds from Step 1 onwards; it is saved with the page and can be printed.
// Limits (Carol's deck, 4.2): up to four themes, one Objective for each theme, up to two Key Results for each Objective.
var N_PRI='Enterprise priorities',N_OKR='Enterprise OKRs';
var OKR_STEPS=FIVE_STEPS;
var OKR_TEST=['Does this truly get the organisation closer to the shared SiP vision?','Would fellow leaders see this as a win for the whole organisation — or just for one function?','Does it visibly improve culture, operations, or value creation?','Is there clear accountability for delivering this outcome?'];
var SX_THEMES=4,SX_KRS=2;
function sxBlank(){var k=[];for(var j=0;j<SX_KRS;j++)k.push({t:'',r:''});return {theme:'',obj:'',krs:k,al:[false,false,false,false],im:'',ef:''};}
function sxState(){var s={step:0,items:[]};for(var i=0;i<SX_THEMES;i++)s.items.push(sxBlank());return s;}
function sxLoadInto(S,s){
  if(!s||typeof s!=='object'||!Array.isArray(s.items))return;
  for(var i=0;i<SX_THEMES;i++){
    var a=s.items[i]||{},b=sxBlank();
    b.theme=String(a.theme||'');b.obj=String(a.obj||'');
    for(var j=0;j<SX_KRS;j++){var kr=(a.krs&&a.krs[j])||{};b.krs[j]={t:String(kr.t||''),r:String(kr.r||'')};}
    for(var q=0;q<4;q++)b.al[q]=!!(a.al&&a.al[q]);
    b.im=String(a.im||'');b.ef=String(a.ef||'');
    S.items[i]=b;
  }
  S.step=(s.step>=0&&s.step<OKR_STEPS.length)?s.step:0;
}
function okrKrOk(t){return /from\s+\w/i.test(t)&&/to\s+\w/i.test(t)&&/q[1-4]|fy|20\d\d|by/i.test(t);}
function okrKrCheck(t){
  if(!t.trim())return '';
  return okrKrOk(t)?'<span style="color:rgba(100,210,140,.8);">✓ Formula looks complete</span>':'<span style="color:rgba(255,180,80,.7);">⚠ Add From X → Y baseline+target and a deadline</span>';
}
function sxAl(o){return o.al.filter(Boolean).length;}
function sxKrs(o){return o.krs.filter(function(k){return k.t.trim();});}
function sxReady(o){return sxKrs(o).length>=1;}                 // an OKR is tested once it holds a Key Result
function sxThemes(S){var out=[];S.items.forEach(function(o,i){if(o.theme.trim())out.push(i);});return out;}
function sxWithObj(S){return sxThemes(S).filter(function(i){return S.items[i].obj.trim();});}
function sxPassed(S){return sxWithObj(S).filter(function(i){var o=S.items[i];return sxReady(o)&&sxAl(o)===4;});}
function sxNeed(text){return '<div class="u3-locked">'+text+'</div>';}
function sxPlace(o){var c=pmFind(o.im,o.ef);return c?c.l+' ('+o.im+' impact, '+o.ef+' effort)':'';}
// What one theme carries so far. upto: 1 theme · 2 Objective · 3 Key Results · 4 alignment test · 5 matrix.
// rec=true (the record): a row appears once it holds something. rec=false (inside a step): the rows the step works from.
function sxChain(S,i,upto,rec){
  var o=S.items[i],r=[['Theme '+(i+1),u3esc(o.theme)]],k=sxKrs(o),n=sxAl(o),passed=sxReady(o)&&n===4;
  if(upto>=2&&(o.obj.trim()||!rec))r.push(['Objective '+(i+1),o.obj.trim()?u3esc(o.obj):'<em>Not written yet</em>']);
  if(upto>=3&&(k.length||!rec))r.push(['Key Results',k.length?'<ol>'+k.map(function(x){return '<li>'+u3esc(x.t)+(x.r.trim()?'<span class="u3-chain-roles">Contributing roles: '+u3esc(x.r)+'</span>':'')+'</li>';}).join('')+'</ol>':'<em>Not written yet</em>']);
  if(upto>=4&&((k.length&&(n>0||!rec))||(!rec&&upto>4)))r.push(['Alignment test',n+' of 4'+(passed?' · aligned':'')]);
  if(upto>=5&&passed&&sxPlace(o))r.push(['Priority Matrix',u3esc(sxPlace(o))]);
  return '<div class="u3-chain">'+r.map(function(x){return '<div class="u3-chain-row"><div class="u3-chain-l">'+x[0]+'</div><div class="u3-chain-v">'+x[1]+'</div></div>';}).join('')+'</div>';
}
function sxFrom(n){return '<div class="u3-from">From Step'+(n===1?' 1':n===2?'s 1 and 2':'s 1 to '+n)+'</div>';}
function sxNav(T){
  var s=T.S.step,p="'"+T.p+"'",last=OKR_STEPS.length-1;
  return '<div class="u3-elnav"><button type="button" class="btn" onclick="sxStep('+p+','+(s-1)+')"'+(s===0?' disabled':'')+'>← Previous step</button><button type="button" class="btn" onclick="sxStep('+p+','+(s+1)+')"'+(s===last?' disabled':'')+'>Next step →</button></div>';
}
function sxPanel(T){
  var S=T.S,P=T.p,q="'"+P+"'",s=S.step,x=T.t,h='';
  if(s===0){
    h='<h5 class="u3-gq">Guiding Question: What insights emerged from the SiP and KISS reflections?</h5><p>'+x.s1+'</p>'+(T.mirror?'<div id="'+P+'KissMirror">'+T.mirror()+'</div>':'')+
      S.items.map(function(o,i){return '<label class="u3-inlbl" for="'+P+'Theme_'+i+'">Theme '+(i+1)+'</label><input type="text" class="u3-in" id="'+P+'Theme_'+i+'" value="'+u3esc(o.theme)+'" oninput="sxSet('+q+','+i+',\'theme\',this.value)" onchange="sxChanged('+q+')">';}).join('')+
      '<p class="u3-small">'+x.s1small+'</p>';
  }else if(s===1){
    h='<h5 class="u3-gq">Guiding Question: If we get this theme right, what will we be known for?</h5><p>'+x.s2+'</p>';
    var th=sxThemes(S);
    h+=th.length?th.map(function(i){
      return '<div class="u3-test">'+sxFrom(1)+sxChain(S,i,1)+'<label class="u3-inlbl" for="'+P+'Obj_'+i+'">Objective '+(i+1)+' · for this theme</label><textarea class="u3-ta" id="'+P+'Obj_'+i+'" placeholder="Objective: start with a verb..." oninput="sxSet('+q+','+i+',\'obj\',this.value)" onchange="sxChanged('+q+')">'+u3esc(S.items[i].obj)+'</textarea></div>';
    }).join(''):sxNeed('Record your themes in Step 1 first.');
  }else if(s===2){
    h='<h5 class="u3-gq">Guiding Question: What measurable outcomes will prove the Objective is being achieved?</h5><p>'+x.s3+'</p>'+
      '<div class="okr-hint"><strong>Formula:</strong> Verb of Change + Metric + From X → Y + By Deadline &nbsp;|&nbsp; <strong>Test:</strong> Can this be checked off a list? If yes, it is a task.</div>';
    var ob=sxWithObj(S),wait=sxThemes(S).filter(function(i){return !S.items[i].obj.trim();});
    h+=ob.length?ob.map(function(i){
      var o=S.items[i];
      return '<div class="u3-test">'+sxFrom(2)+sxChain(S,i,2)+o.krs.map(function(k,j){
          return '<div class="okr-kr"><label class="u3-inlbl" style="margin-top:0;" for="'+P+'Kr_'+i+'_'+j+'">Key Result '+(j+1)+' · for Objective '+(i+1)+(j>0?' (optional)':'')+'</label>'+
            '<textarea class="u3-ta" id="'+P+'Kr_'+i+'_'+j+'" placeholder="Verb of Change + Metric + From X to Y + By Deadline" oninput="sxKr('+q+','+i+','+j+',\'t\',this.value)" onchange="sxChanged('+q+')">'+u3esc(k.t)+'</textarea>'+
            '<div class="okr-check" id="'+P+'Chk_'+i+'_'+j+'">'+okrKrCheck(k.t)+'</div>'+
            '<label class="u3-inlbl" for="'+P+'Role_'+i+'_'+j+'">Contributing roles · for Key Result '+(j+1)+'</label>'+
            '<textarea class="u3-ta u3-roles" id="'+P+'Role_'+i+'_'+j+'" placeholder="Name the roles that must contribute to this Key Result. E.g. Operations, Commercial, Technology" oninput="sxKr('+q+','+i+','+j+',\'r\',this.value)" onchange="sxChanged('+q+')">'+u3esc(k.r)+'</textarea></div>';
        }).join('')+'</div>';
    }).join('')+(wait.length?'<p class="u3-small">Still in Step 2, without an Objective: '+wait.map(function(i){return 'Theme '+(i+1);}).join(' · ')+'.</p>':''):sxNeed('Write your Objectives in Step 2 first.');
  }else if(s===3){
    h='<p>'+x.s4+'</p>';
    var ob3=sxWithObj(S);
    h+=ob3.length?ob3.map(function(i){
      var o=S.items[i],n=sxAl(o),ready=sxReady(o);
      return '<div class="u3-test">'+sxFrom(3)+(ready&&n===4?'<span class="u3-pill u3-pill-r">Aligned</span>':'')+sxChain(S,i,3)+
        (ready?OKR_TEST.map(function(t,y){return '<label class="u3-tick"><input type="checkbox"'+(o.al[y]?' checked':'')+' onchange="sxTick('+q+','+i+','+y+',this.checked)"><span>'+u3esc(t)+'</span></label>';}).join('')
              :sxNeed('Write a Key Result for Objective '+(i+1)+' in Step 3 before you test it.'))+'</div>';
    }).join('')+'<div class="hbox teal"><p><strong>Output of Step 4:</strong> '+sxPassed(S).length+' of your '+ob3.length+' OKRs are aligned and go forward to Step 5.</p></div>':sxNeed('Write your Objectives in Step 2 first.');
  }else{
    h='<p>'+x.s5+'</p>';
    var pr=sxPassed(S),all=sxWithObj(S);
    if(!all.length)h+=sxNeed('Write your Objectives in Step 2 first.');
    else if(!pr.length)h+=sxNeed('No OKR is aligned yet. Complete the alignment test in Step 4 first.');
    else{
      h+=pr.map(function(i){
        var o=S.items[i],c=pmFind(o.im,o.ef);
        var selH=function(f,opts,val,lab){return '<label class="u3-inlbl" for="'+P+'Mx_'+f+'_'+i+'">'+lab+'</label><select class="u3-in" id="'+P+'Mx_'+f+'_'+i+'" onchange="sxMx('+q+','+i+',\''+f+'\',this.value)"><option value="">Select…</option>'+opts.map(function(v){return '<option'+(val===v?' selected':'')+'>'+v+'</option>';}).join('')+'</select>';};
        return '<div class="u3-test">'+sxFrom(4)+sxChain(S,i,4)+
          '<div class="u3-meta"><div>'+selH('im',['High','Medium','Low'],o.im,'Impact')+'</div><div>'+selH('ef',['Low','Medium','High'],o.ef,'Effort')+'</div></div>'+
          (c?'<div class="u3-pos" style="border-left-color:'+c.c+';"><strong style="color:'+c.c+';">'+c.l+'</strong> '+u3esc(c.d)+'</div>':'')+'</div>';
      }).join('');
      var back=all.filter(function(i){return pr.indexOf(i)<0;});
      if(back.length)h+='<p class="u3-small">Still in Step 3 or Step 4: '+back.map(function(i){return 'Objective '+(i+1)+' ('+sxAl(S.items[i])+' of 4)';}).join(' · ')+'.</p>';
      h+='<div class="u3-mx"><div class="u3-mx-corner">Impact ↓ &nbsp; Effort →</div><div class="u3-mx-ax">Low effort</div><div class="u3-mx-ax">Medium effort</div><div class="u3-mx-ax">High effort</div>'+
        ['High','Medium','Low'].map(function(im){
          return '<div class="u3-mx-ax u3-mx-row">'+im+' impact</div>'+['Low','Medium','High'].map(function(ef){
            var c=pmFind(im,ef),here=pr.filter(function(i){return S.items[i].im===im&&S.items[i].ef===ef;}).map(function(i){return '<span class="u3-mx-tag">Objective '+(i+1)+' · '+u3esc(S.items[i].theme)+'</span>';});
            return '<div class="u3-mx-cell" style="border-color:'+c.c+';"><div class="u3-mx-name" style="color:'+c.c+';">'+c.l+'</div>'+here.join('')+'</div>';
          }).join('');
        }).join('')+'</div>';
    }
  }
  return h+sxNav(T);
}
// The record: every theme with all it carries so far, in step order.
function sxRecord(S){
  return sxThemes(S).map(function(i){return '<div class="u3-rec-item">'+sxChain(S,i,5,true)+'</div>';}).join('');
}
// Readable copy of the record, saved for the facilitator's report. Group work feeds the Capstone and is left out of the Learning Portfolio.
function sxText(S){
  var out=[];
  sxThemes(S).forEach(function(i){
    var o=S.items[i],lines=['Theme '+(i+1)+': '+o.theme.trim()];
    if(o.obj.trim())lines.push('Objective '+(i+1)+': '+o.obj.trim());
    o.krs.forEach(function(k,j){if(k.t.trim())lines.push('Key Result '+(j+1)+': '+k.t.trim()+(k.r.trim()?' (Contributing roles: '+k.r.trim()+')':''));});
    if(o.obj.trim()){
      var n=sxAl(o),ok=(sxReady(o)&&n===4);
      lines.push('Alignment test: '+n+' of 4'+(ok?' · aligned':'')+(ok&&sxPlace(o)?' · Matrix: '+sxPlace(o):''));
    }
    out.push(lines.join('\n'));
  });
  return out.join('\n\n');
}
// The record sits above the steps. When it grows or shrinks, the steps would move on the screen while someone is
// typing or about to click; the page is scrolled by the same amount, so the steps stay exactly where they are.
function sxSetRec(el,html,anchorId){
  if(!el||el.__h===html)return;
  var a=u3el(anchorId),on=a&&a.offsetParent!==null,t0=on?a.getBoundingClientRect().top:0;
  el.innerHTML=html;el.__h=html;
  if(on&&t0<window.innerHeight){
    var d=a.getBoundingClientRect().top-t0;
    if(d){try{window.scrollBy({top:d,left:0,behavior:'instant'});}catch(e){window.scrollBy(0,d);}}
  }
}
var SX_EMPTY='<div class="u3-final-t empty">Your record starts with the themes of Step 1. Each step adds to it: the Objective, the Key Results, the alignment test and the matrix position.</div>';
// Print: the record on a plain page in a new window.
function sxPrint(title,sub,S,headHtml,tailHtml){
  var rows=sxThemes(S).map(function(i){
    var o=S.items[i],k=sxKrs(o),n=sxAl(o),passed=sxReady(o)&&n===4,r=[];
    if(o.obj.trim())r.push(['Objective '+(i+1),u3esc(o.obj)]);
    if(k.length)r.push(['Key Results','<ol>'+k.map(function(x){return '<li>'+u3esc(x.t)+(x.r.trim()?'<br><span class="s">Contributing roles: '+u3esc(x.r)+'</span>':'')+'</li>';}).join('')+'</ol>']);
    if(o.obj.trim())r.push(['Alignment test',n+' of 4'+(passed?' · aligned':'')]);
    if(passed&&sxPlace(o))r.push(['Priority Matrix',u3esc(sxPlace(o))]);
    return '<h2>Theme '+(i+1)+' · '+u3esc(o.theme)+'</h2>'+(r.length?'<table>'+r.map(function(x){return '<tr><th>'+x[0]+'</th><td>'+x[1]+'</td></tr>';}).join('')+'</table>':'');
  }).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>'+u3esc(title)+'</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:16px;margin:24px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px;page-break-after:avoid}h3{color:#071b4d;font-size:15px;margin:22px 0 6px}table{width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:13px;page-break-inside:avoid}th{width:150px;text-align:left;vertical-align:top;color:#043f2f;padding:6px 10px 6px 0;border-bottom:1px solid #e5e7eb}td{padding:6px 0;border-bottom:1px solid #e5e7eb;vertical-align:top}ol{margin:0;padding-left:18px}li{margin-bottom:4px}.s{color:#666;font-size:12px}p,pre{font-family:Arial,sans-serif;font-size:13px}pre{white-space:pre-wrap}</style></head><body><h1>'+u3esc(title)+'</h1><p class="sub">'+u3esc(sub)+'</p>'+(headHtml||'')+(rows||'<p>Nothing has been recorded yet.</p>')+(tailHtml||'')+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}

// ── Handlers ──
var SX={};
function sxRenderTool(T){
  var host=u3el(T.host);if(!host)return;
  host.innerHTML='<div class="step-tabs" id="'+T.p+'STabs">'+OKR_STEPS.map(function(n,i){
    return '<div class="step-tab'+(i===T.S.step?' active':'')+'" onclick="sxStep(\''+T.p+'\','+i+')"><div class="step-num">Step '+(i+1)+'</div><div class="step-name">'+n+'</div></div>';
  }).join('')+'</div><div class="step-panel active" id="'+T.p+'Panel">'+sxPanel(T)+'</div>';
  T.out();
}
function sxRepaint(T){var p=u3el(T.p+'Panel');if(p)p.innerHTML=sxPanel(T);T.out();}
function sxStep(p,i){var T=SX[p];if(i<0||i>=OKR_STEPS.length)return;T.S.step=i;sxRenderTool(T);T.queue();}
function sxTouch(T){T.touch();clearTimeout(T._o);T._o=setTimeout(T.out,500);}
function sxSet(p,i,f,val){var T=SX[p];T.S.items[i][f]=val;sxTouch(T);}
function sxKr(p,i,j,f,val){
  var T=SX[p];T.S.items[i].krs[j][f]=val;
  if(f==='t'){var c=u3el(p+'Chk_'+i+'_'+j);if(c)c.innerHTML=okrKrCheck(val);}
  sxTouch(T);
}
function sxChanged(p){SX[p].out();}
function sxTick(p,i,y,on){var T=SX[p];T.S.items[i].al[y]=!!on;T.touch();sxRepaint(T);}
function sxMx(p,i,f,val){var T=SX[p];T.S.items[i][f]=val;T.touch();sxRepaint(T);}

var OK=sxState();
function okrLoad(s){sxLoadInto(OK,s);}
function okrConfirmed(){return isConf(N_PRI)&&isConf(N_OKR);}
function okrMirrorHtml(){
  if(!kissConfirmed())return '<div class="u3-locked">Your KISS map appears here once your group has confirmed it in 4.1.</div>';
  return '<div class="u3-out"><div class="u3-out-h">Your confirmed KISS map</div>'+KISS_EL.map(function(k,x){
    return '<div class="u3-final"><div class="u3-final-h '+k[0]+'">'+k[1]+'</div><div class="u3-final-t">'+u3esc(u3v(KISS_OUT[x]))+'</div></div>';
  }).join('')+'</div>';
}
function okrRefreshMirror(){var m=u3el('okrKissMirror');if(m)m.innerHTML=okrMirrorHtml();}
// The enterprise priorities are the aligned Objectives, each with its position on the matrix.
function okrPriText(){
  return sxPassed(OK).map(function(i,n){var o=OK.items[i];return (n+1)+'. '+o.theme.trim()+(sxPlace(o)?' — '+sxPlace(o):'');}).join('\n');
}
function okrOkrText(){
  return sxPassed(OK).map(function(i,n){
    var o=OK.items[i],j=0;
    return 'Objective '+(n+1)+': '+o.obj.trim()+'\n'+sxKrs(o).map(function(k){j++;return '   Key Result '+j+': '+k.t.trim()+(k.r.trim()?' (Contributing roles: '+k.r.trim()+')':'');}).join('\n');
  }).join('\n\n');
}
function okrProblems(){
  var p=[],pr=sxPassed(OK);
  if(!pr.length)return ['Complete Steps 1 to 4 first: at least one OKR must be aligned.'];
  pr.forEach(function(i){
    var o=OK.items[i],n=i+1,filled=sxKrs(o);
    if(filled.some(function(k){return !okrKrOk(k.t);}))p.push('Each Key Result of Objective '+n+' needs a metric, From X to Y and a deadline (Step 3).');
    if(filled.some(function(k){return !k.r.trim();}))p.push('Name the contributing roles for each Key Result of Objective '+n+' (Step 3).');
    if(!pmFind(o.im,o.ef))p.push('Place Objective '+n+' on the Prioritisation Matrix (Step 5).');
  });
  return p;
}
// The blocks are built once; later calls only refresh what changed, so a click on a button is never lost to a redraw.
function renderOkrOut(){
  var host=u3el('okrOutP'),rh=u3el('okrRecP');if(!host||!rh)return;
  if(!u3el('okrRec')){
    rh.innerHTML='<div class="u3-out"><div class="u3-rec" id="okrRec"></div></div>';
    host.innerHTML='<div id="okrFinal" style="display:none;">'+
      '<div class="u3-out"><div class="u3-out-h">Your Enterprise Priorities<span class="u3-pill" id="okrPillA" style="display:none;">Confirmed</span></div><div class="u3-final-t" id="okrPriOut"></div></div>'+
      '<div class="u3-out"><div class="u3-out-h">Your Enterprise OKRs<span class="u3-pill" id="okrPillB" style="display:none;">Confirmed</span></div><div class="u3-final-t" id="okrOkrOut"></div></div></div>'+
      '<div class="u3-btnrow"><button type="button" class="u3-b" id="okrConfirmBtn" onclick="okrConfirm()">✓ Confirm Enterprise Priorities and OKRs</button><button type="button" class="u3-b" onclick="okrPrint()">Print the five-step record</button></div>'+
      '<div class="u3-note" id="okrMsg" style="display:none;"></div>';
  }
  var done=okrConfirmed(),pri=okrPriText(),okr=okrOkrText();
  sxSetRec(u3el('okrRec'),sxRecord(OK)||SX_EMPTY,'okrToolP');
  u3el('okrFinal').style.display=pri?'':'none';
  u3el('okrPriOut').textContent=pri;u3el('okrOkrOut').textContent=okr;
  u3el('okrPillA').style.display=done?'':'none';u3el('okrPillB').style.display=done?'':'none';
  u3el('okrConfirmBtn').classList.toggle('ok',done);
  if(done)u3msg('okrMsg','');
}
var _okrTimer=null;
function okrTouch(){
  if(okrConfirmed()){[N_PRI,N_OKR].forEach(function(nm){var i=U3.conf.indexOf(nm);if(i>=0)U3.conf.splice(i,1);});U3._odirty=true;renderOkrOut();}
  okrQueue();
}
function okrQueue(){clearTimeout(_okrTimer);_okrTimer=setTimeout(okrSaveNow,900);}
async function okrSaveNow(){
  clearTimeout(_okrTimer);
  await u3save('__okr_work',OK);
  await u3save('okr_drafts',sxText(OK));
  if(U3._odirty){U3._odirty=false;await u3save('confirmed_items',U3.conf);}
}
async function okrConfirm(){
  var p=okrProblems();
  if(p.length){u3msg('okrMsg',p.slice(0,4).join(' '));return;}
  await okrSaveNow();
  var a=okrPriText(),b=okrOkrText();
  U3.v.ent_priorities=a;U3.v.ent_okrs=b;
  await u3save('ent_priorities',a);await u3save('ent_okrs',b);
  await setConfMany([N_PRI,N_OKR],true);
  renderOkrOut();
}
function okrPrint(){
  var pri=okrPriText(),okr=okrOkrText();
  sxPrint('Unit 3 · Translating KISS to OKRs: Five-Step Record','Strategy2Results® · Module 2 · Unit 3 · Part 4.2 · Group work',OK,'',
    pri?'<h3>Enterprise Priorities'+(okrConfirmed()?' · confirmed':' · not yet confirmed')+'</h3><pre>'+u3esc(pri)+'</pre><h3>Enterprise OKRs'+(okrConfirmed()?' · confirmed':' · not yet confirmed')+'</h3><pre>'+u3esc(okr)+'</pre>':'');
}
var OKT=SX.okr={S:OK,p:'okr',host:'okrToolP',mirror:okrMirrorHtml,touch:okrTouch,queue:okrQueue,out:renderOkrOut,t:{
  s1:'Each member first writes down the 2–3 big shifts they see in the KISS map. Share them, then agree your group\'s themes. A theme names one shift the organisation must make to reach the SiP.',
  s1small:'Record up to four themes. Each theme you record is carried into Step 2, where your group turns it into an Objective.',
  s2:'Each theme from Step 1 is shown below. Translate it into a bold, qualitative statement that expresses strategic ambition. Start with a verb and describe the desired transformation. Make it ambitious, keep it qualitative and keep it memorable.',
  s3:'Each Objective from Step 2 is shown below with its theme. Write up to two Key Results for it and name the contributing roles for each one.',
  s4:'Each OKR from Step 3 is shown below: the theme, the Objective and its Key Results. Test it against the four questions. Tick each question your group answers with a clear yes. An OKR that earns all four ticks is aligned and goes forward to Step 5. An OKR that cannot earn all four goes back to Step 2 or Step 3.',
  s5:'Each aligned OKR from Step 4 is shown below. Place it on the Prioritisation Matrix. <strong>Impact</strong> is the strategic value delivered if the Objective is achieved. <strong>Effort</strong> is the time, resources, coordination and organisational change required. Agree what high impact and high effort mean for your organisation before you place the first one.'}};
function renderOkrTool(){sxRenderTool(OKT);}

// ── 5.1 · Strategy Airport: the participant's own learning round is saved and submitted ──────────
var _gameTimer=null;
function gameChanged(){
  clearTimeout(_gameTimer);
  _gameTimer=setTimeout(async function(){
    var st=SA.state;
    await u3save('__game',st);
    await u3save('game_kiss',saKissText());
    await u3save('game_flight_plan',saPlanText());
    await u3save('game_round',st.step===3?'Learning round complete':st.step===2?'In progress · Gate 2: Flight Plan':'In progress · Gate 1: Baggage Check');
  },700);
}

// ── Portfolio work (3.1 and 5.1): Save to Portfolio, and the way to Submit to Facilitator ──────────
async function pfSave(kind){
  var id='pf_'+kind+'_msg',ok=false,done=false;
  u3msg(id,'Saving…','');
  try{
    if(kind==='hz'){
      var a=await u3save('__hz_match',{cur:HZ.cur,m:HZ.m}),b=await u3save('hz_match',hzText());
      ok=!!(a&&b);done=hzCount()===HOT_ZONES.length;
    }else{
      clearTimeout(_gameTimer);
      var st=SA.state,r=[await u3save('__game',st),await u3save('game_kiss',saKissText()),await u3save('game_flight_plan',saPlanText()),
        await u3save('game_round',st.step===3?'Learning round complete':st.step===2?'In progress · Gate 2: Flight Plan':'In progress · Gate 1: Baggage Check')];
      ok=r.every(function(x){return !!x;});done=st.step===3;
    }
  }catch(e){ok=false;}
  if(!ok){u3msg(id,'Not saved. Check your connection, then select Save to Portfolio again.','');return;}
  if(kind==='hz')u3msg(id,done?'✓ Saved to your portfolio. Ten of ten roles matched. Select Go to Submit to Facilitator when your unit is complete.':'✓ Saved to your portfolio. '+hzCount()+' of '+HOT_ZONES.length+' roles matched. Match the remaining roles, then save again.','ok');
  else u3msg(id,done?'✓ Saved to your portfolio. Learning round complete. Select Go to Submit to Facilitator to send your unit.':'✓ Saved to your portfolio. Finish the learning round, then save again.','ok');
}
function pfGoSubmit(){
  var b=document.querySelector('.send-btn');if(!b)return;
  var panel=b.closest('.mod-panel'),panels=document.querySelectorAll('.mod-panel');
  if(panel){panels.forEach(function(p,x){var on=p===panel;p.classList.toggle('active',on);var t=document.querySelectorAll('.mod-tab')[x];if(t)t.classList.toggle('active',on);});}
  setTimeout(function(){b.scrollIntoView({behavior:'smooth',block:'center'});try{b.focus({preventScroll:true});}catch(e){}},60);
}

function toggleDomain(id){u3ToggleDomain(id);}
