// ── UNIT 3 · PARTICIPANT PAGE ───────────────────────────────────────────────────────────────────
var LENS='u2m1_lens2';
var SUMMARY=[
  {arc:"Awareness — What",title:"The KISS Framework as Reflective Filter",body:"You saw that KISS (Keep, Improve, Start, Stop) functions as a reflective filter between strategic vision and execution commitments. Before defining Objectives and Key Results, you examine the organisation's current operating reality in relation to its Success in Practice. This step prevents the common strategic mistake of layering new ambitions on top of an unchanged operational system. Six steps then carry the KISS output into enterprise OKRs."},
  {arc:"Intelligence — Why",title:"Most OKR Failures are Reflection Failures",body:"When organisations move directly from vision to targets, legacy routines remain in place, resources remain misaligned, and teams attempt to pursue transformational goals while still carrying the weight of outdated priorities. The KISS-to-OKR sequence resolves this tension: SiP defines the future, KISS identifies the changes required, and OKRs translate those changes into measurable progress. The worked example showed the full sequence in practice."},
  {arc:"Extrapolating — Where",title:"Functional Bias Creates OKR Hot Zones",body:"Each leader naturally emphasises different SiP domains. Unexamined, these perspectives produce functional OKRs where enterprise OKRs are needed. You matched each leadership role to its typical hot zone and its alignment question. Recognising these patterns allows your group to integrate perspectives into a balanced execution system that reflects the full enterprise."},
  {arc:"Integration — Collective",title:"Individual Expertise into Collective Intelligence",body:"With your group you translated your Success in Practice into a confirmed KISS map across the four SiP domains, then into enterprise priorities and enterprise OKRs through the six steps. Each member began with insights from a functional domain, and the final outcome reflects the success of the enterprise as a whole. The Prioritisation Matrix concentrated execution energy on the priorities that will most accelerate progress toward the SiP. Your confirmed outputs feed your team's Capstone Blueprint."},
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

// ── 3.1 · Matching exercise: Typical Hot Zone and Alignment Question to each role (individual work) ──
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
    (all?'<div class="hbox teal"><p><strong>All ten roles matched.</strong> Select any role above to review its full card. Your matches reach your facilitator when you submit the unit.</p></div>':'')+
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

// ── 4.2 · The six steps: themes → Objectives → Key Results → alignment test → enterprise priority → matrix ──
var N_PRI='Enterprise priorities',N_OKR='Enterprise OKRs';
var OKR_STEPS=['Find Themes','Inspiring Objectives','Define Key Results','Alignment Test','Enterprise Priority','Priority Matrix'];
var OKR_TEST=['Does this truly get the organisation closer to the shared SiP vision?','Would fellow leaders see this as a win for the whole organisation — or just for one function?','Does it visibly improve culture, operations, or value creation?','Is there clear accountability for delivering this outcome?'];
function okrBlankItem(){return {theme:'',obj:'',krs:[{t:'',r:''},{t:'',r:''},{t:'',r:''}],al:[false,false,false,false],pri:false,im:'',ef:''};}
var OK={step:0,items:[]};
(function(){for(var i=0;i<6;i++)OK.items.push(okrBlankItem());})();
function okrLoad(s){
  if(!s||typeof s!=='object'||!Array.isArray(s.items))return;
  for(var i=0;i<6;i++){
    var a=s.items[i]||{},b=okrBlankItem();
    b.theme=String(a.theme||'');b.obj=String(a.obj||'');
    for(var j=0;j<3;j++){var kr=(a.krs&&a.krs[j])||{};b.krs[j]={t:String(kr.t||''),r:String(kr.r||'')};}
    for(var q=0;q<4;q++)b.al[q]=!!(a.al&&a.al[q]);
    b.pri=!!a.pri;b.im=String(a.im||'');b.ef=String(a.ef||'');
    OK.items[i]=b;
  }
  OK.step=(s.step>=0&&s.step<6)?s.step:0;
}
function okrHas(i,f){return OK.items[i][f].trim()!=='';}
function okrWithObj(){var out=[];OK.items.forEach(function(o,i){if(o.theme.trim()&&o.obj.trim())out.push(i);});return out;}
function okrPris(){return okrWithObj().filter(function(i){return OK.items[i].pri;});}
function okrKrOk(t){return /from\s+\w/i.test(t)&&/to\s+\w/i.test(t)&&/q[1-4]|fy|20\d\d|by/i.test(t);}
function okrKrCheck(t){
  if(!t.trim())return '';
  return okrKrOk(t)?'<span style="color:rgba(100,210,140,.8);">✓ Formula looks complete</span>':'<span style="color:rgba(255,180,80,.7);">⚠ Add From X → Y baseline+target and a deadline</span>';
}
function okrAlCount(i){return OK.items[i].al.filter(Boolean).length;}
function okrKrCount(i){return OK.items[i].krs.filter(function(k){return k.t.trim();}).length;}
function okrConfirmed(){return isConf(N_PRI)&&isConf(N_OKR);}
function okrMirrorHtml(){
  if(!kissConfirmed())return '<div class="u3-locked">Your KISS map appears here once your group has confirmed it in 4.1.</div>';
  return '<div class="u3-out"><div class="u3-out-h">Your confirmed KISS map</div>'+KISS_EL.map(function(k,x){
    return '<div class="u3-final"><div class="u3-final-h '+k[0]+'">'+k[1]+'</div><div class="u3-final-t">'+u3esc(u3v(KISS_OUT[x]))+'</div></div>';
  }).join('')+'</div>';
}
function okrRefreshMirror(){var m=u3el('okrKissMirror');if(m)m.innerHTML=okrMirrorHtml();}
function okrNav(){
  var s=OK.step;
  return '<div class="u3-elnav"><button type="button" class="btn" onclick="okrStep('+(s-1)+')"'+(s===0?' disabled':'')+'>← Previous step</button><button type="button" class="btn" onclick="okrStep('+(s+1)+')"'+(s===5?' disabled':'')+'>Next step →</button></div>';
}
function okrNeed(text){return '<div class="u3-locked">'+text+'</div>';}
function okrPanelHtml(){
  var s=OK.step,h='';
  if(s===0){
    h='<h5 class="u3-gq">Guiding Question: What insights emerged from the SiP and KISS reflections?</h5>'+
      '<p>Each member first writes down the 2–3 big shifts they see in the KISS map. Share them, then agree your group\'s themes. A theme names one shift the organisation must make to reach the SiP.</p>'+
      '<div id="okrKissMirror">'+okrMirrorHtml()+'</div>'+
      OK.items.map(function(o,i){return '<label class="u3-inlbl" for="okrTheme_'+i+'">Theme '+(i+1)+'</label><input type="text" class="u3-in" id="okrTheme_'+i+'" value="'+u3esc(o.theme)+'" placeholder="'+(i===0?'E.g. Customer responsiveness':'')+'" oninput="okrSet('+i+',\'theme\',this.value)" onchange="okrChanged()">';}).join('')+
      '<p class="u3-small">Record up to six themes. In Step 5 your group selects no more than four as enterprise priorities.</p>';
  }else if(s===1){
    h='<h5 class="u3-gq">Guiding Question: If we get this theme right, what will we be known for?</h5>'+
      '<p>Translate each theme into a bold, qualitative statement that expresses strategic ambition. Start with a verb and describe the desired transformation. Make it ambitious, keep it qualitative and keep it memorable.</p>';
    var th=[];OK.items.forEach(function(o,i){if(o.theme.trim())th.push(i);});
    h+=th.length?th.map(function(i){return '<label class="u3-inlbl" for="okrObj_'+i+'">Theme '+(i+1)+' · '+u3esc(OK.items[i].theme)+'</label><textarea class="u3-ta" id="okrObj_'+i+'" placeholder="Objective: start with a verb..." oninput="okrSet('+i+',\'obj\',this.value)" onchange="okrChanged()">'+u3esc(OK.items[i].obj)+'</textarea>';}).join(''):okrNeed('Record your themes in Step 1 first.');
  }else if(s===2){
    h='<h5 class="u3-gq">Guiding Question: What measurable outcomes will prove the Objective is being achieved?</h5>'+
      '<div class="okr-hint"><strong>Formula:</strong> Verb of Change + Metric + From X → Y + By Deadline &nbsp;|&nbsp; <strong>Test:</strong> Can this be checked off a list? If yes, it is a task.</div>';
    var ob=okrWithObj();
    h+=ob.length?ob.map(function(i){
      var o=OK.items[i];
      return '<div class="okr-obj open"><div class="okr-obj-head" style="cursor:default;"><span class="okr-obj-num">OBJ '+(i+1)+'</span><span class="okr-obj-title">'+u3esc(o.obj)+'</span></div><div class="okr-obj-body">'+
        o.krs.map(function(k,j){
          return '<div class="okr-kr"><label for="okrKr_'+i+'_'+j+'">Key Result '+(j+1)+(j===2?' (optional)':'')+'</label>'+
            '<textarea class="okr-ta" id="okrKr_'+i+'_'+j+'" placeholder="'+(j===0?'E.g. Reduce customer response time from 12 hours to 4 hours by Q3 2027...':'')+'" oninput="okrKr('+i+','+j+',\'t\',this.value)" onchange="okrChanged()">'+u3esc(k.t)+'</textarea>'+
            '<div class="okr-check" id="okrChk_'+i+'_'+j+'">'+okrKrCheck(k.t)+'</div>'+
            '<label for="okrRole_'+i+'_'+j+'" style="margin-top:10px;">Contributing roles</label>'+
            '<input type="text" class="u3-in" id="okrRole_'+i+'_'+j+'" value="'+u3esc(k.r)+'" placeholder="'+(j===0?'E.g. Operations, Commercial, Technology':'')+'" oninput="okrKr('+i+','+j+',\'r\',this.value)" onchange="okrChanged()"></div>';
        }).join('')+'</div></div>';
    }).join(''):okrNeed('Write your Objectives in Step 2 first.');
  }else if(s===3){
    h='<p>Before an OKR goes forward, test it against four questions. Tick each question your group answers with a clear yes. An OKR that cannot earn all four ticks goes back to Step 2 or Step 3.</p>';
    var ob3=okrWithObj();
    h+=ob3.length?ob3.map(function(i){
      var o=OK.items[i],n=okrAlCount(i);
      return '<div class="u3-test"><div class="u3-test-h"><span class="okr-obj-num">OBJ '+(i+1)+'</span><span>'+u3esc(o.obj)+'</span>'+(n===4?'<span class="u3-pill">Passed</span>':'')+'</div>'+
        OKR_TEST.map(function(q,x){return '<label class="u3-tick"><input type="checkbox"'+(o.al[x]?' checked':'')+' onchange="okrAl('+i+','+x+',this.checked)"><span>'+u3esc(q)+'</span></label>';}).join('')+'</div>';
    }).join(''):okrNeed('Write your Objectives in Step 2 first.');
  }else if(s===4){
    var sel=okrPris().length;
    h='<p>Your group now determines which Objectives deserve enterprise focus now. Strategy execution fails when too many priorities are pursued simultaneously.</p>'+
      '<div class="hbox teal"><p><strong>The Less is More Rule:</strong> No more than <strong>4 Enterprise Objectives</strong>. No more than <strong>3 Key Results per Objective</strong>. This constraint forces explicit trade-offs and concentrates execution energy on what matters most.</p></div>';
    var ob4=okrWithObj();
    h+=ob4.length?'<div class="u3-progress-top" style="margin:14px 0 6px;"><span>Enterprise priorities selected</span><b>'+sel+' of 4</b></div>'+ob4.map(function(i){
      var o=OK.items[i];
      return '<label class="u3-tick u3-pri'+(o.pri?' on':'')+'"><input type="checkbox"'+(o.pri?' checked':'')+' onchange="okrPri('+i+',this)"><span><strong>Objective '+(i+1)+' · '+u3esc(o.obj)+'</strong><em>Theme: '+u3esc(o.theme)+' · Alignment test: '+okrAlCount(i)+' of 4 · Key Results: '+okrKrCount(i)+'</em></span></label>';
    }).join('')+'<div class="u3-note" id="okrPriMsg" style="display:none;"></div>':okrNeed('Write your Objectives in Step 2 first.');
  }else{
    h='<p>Place each enterprise priority on the Prioritisation Matrix. <strong>Impact</strong> is the strategic value delivered if the Objective is achieved. <strong>Effort</strong> is the time, resources, coordination and organisational change required. Agree what high impact and high effort mean for your organisation before you place the first one.</p>';
    var pr=okrPris();
    if(!pr.length)h+=okrNeed('Select your enterprise priorities in Step 5 first.');
    else{
      h+=pr.map(function(i){
        var o=OK.items[i],c=pmFind(o.im,o.ef);
        var selH=function(f,opts,val,lab){return '<label class="u3-inlbl" for="okrMx_'+f+'_'+i+'">'+lab+'</label><select class="u3-in" id="okrMx_'+f+'_'+i+'" onchange="okrMx('+i+',\''+f+'\',this.value)"><option value="">Select…</option>'+opts.map(function(v){return '<option'+(val===v?' selected':'')+'>'+v+'</option>';}).join('')+'</select>';};
        return '<div class="u3-test"><div class="u3-test-h"><span class="okr-obj-num">OBJ '+(i+1)+'</span><span>'+u3esc(o.obj)+'</span></div>'+
          '<div class="u3-meta"><div>'+selH('im',['High','Medium','Low'],o.im,'Impact')+'</div><div>'+selH('ef',['Low','Medium','High'],o.ef,'Effort')+'</div></div>'+
          (c?'<div class="u3-pos" style="border-left-color:'+c.c+';"><strong style="color:'+c.c+';">'+c.l+'</strong> '+u3esc(c.d)+'</div>':'')+'</div>';
      }).join('');
      h+='<div class="u3-mx"><div class="u3-mx-corner">Impact ↓ &nbsp; Effort →</div><div class="u3-mx-ax">Low effort</div><div class="u3-mx-ax">Medium effort</div><div class="u3-mx-ax">High effort</div>'+
        ['High','Medium','Low'].map(function(im){
          return '<div class="u3-mx-ax u3-mx-row">'+im+' impact</div>'+['Low','Medium','High'].map(function(ef){
            var c=pmFind(im,ef),here=pr.filter(function(i){return OK.items[i].im===im&&OK.items[i].ef===ef;}).map(function(i){return '<span class="u3-mx-tag">Objective '+(i+1)+'</span>';});
            return '<div class="u3-mx-cell" style="border-color:'+c.c+';"><div class="u3-mx-name" style="color:'+c.c+';">'+c.l+'</div>'+here.join('')+'</div>';
          }).join('');
        }).join('')+'</div>';
    }
  }
  return h+okrNav();
}
function okrPriText(){
  return okrPris().map(function(i,n){var o=OK.items[i],c=pmFind(o.im,o.ef);return (n+1)+'. '+o.theme.trim()+(c?' — '+c.l+' ('+o.im+' impact, '+o.ef+' effort)':'');}).join('\n');
}
function okrOkrText(){
  return okrPris().map(function(i,n){
    var o=OK.items[i],j=0;
    return 'Objective '+(n+1)+': '+o.obj.trim()+'\n'+o.krs.filter(function(k){return k.t.trim();}).map(function(k){j++;return '   Key Result '+j+': '+k.t.trim()+(k.r.trim()?' (Contributing roles: '+k.r.trim()+')':'');}).join('\n');
  }).join('\n\n');
}
function okrDraftText(){
  var out=[];
  OK.items.forEach(function(o,i){
    if(!o.theme.trim())return;
    var lines=['Theme '+(i+1)+': '+o.theme.trim()];
    if(o.obj.trim())lines.push('Objective: '+o.obj.trim());
    o.krs.forEach(function(k,j){if(k.t.trim())lines.push('Key Result '+(j+1)+': '+k.t.trim()+(k.r.trim()?' (Contributing roles: '+k.r.trim()+')':''));});
    if(o.obj.trim())lines.push('Alignment test: '+okrAlCount(i)+' of 4 · Enterprise priority: '+(o.pri?'yes':'no'));
    out.push(lines.join('\n'));
  });
  return out.join('\n\n');
}
function okrProblems(){
  var p=[],pr=okrPris();
  if(!pr.length)return ['Select your enterprise priorities in Step 5.'];
  pr.forEach(function(i){
    var o=OK.items[i],n=i+1,filled=o.krs.filter(function(k){return k.t.trim();});
    if(filled.length<2)p.push('Objective '+n+' needs at least two Key Results (Step 3).');
    if(filled.some(function(k){return !okrKrOk(k.t);}))p.push('Each Key Result of Objective '+n+' needs a metric, From X to Y and a deadline (Step 3).');
    if(filled.some(function(k){return !k.r.trim();}))p.push('Name the contributing roles for each Key Result of Objective '+n+' (Step 3).');
    if(okrAlCount(i)<4)p.push('Complete the alignment test for Objective '+n+' (Step 4).');
    if(!pmFind(o.im,o.ef))p.push('Place Objective '+n+' on the Prioritisation Matrix (Step 6).');
  });
  return p;
}
// The output block is built once; later calls only refresh its text, so a click on Confirm is never lost to a redraw.
function renderOkrOut(){
  var host=u3el('okrOutP');if(!host)return;
  if(!u3el('okrPriOut')){
    host.innerHTML='<div class="u3-out"><div class="u3-out-h">Your Enterprise Priorities<span class="u3-pill" id="okrPillA" style="display:none;">Confirmed</span></div><div class="u3-final-t" id="okrPriOut"></div></div>'+
      '<div class="u3-out"><div class="u3-out-h">Your Enterprise OKRs<span class="u3-pill" id="okrPillB" style="display:none;">Confirmed</span></div><div class="u3-final-t" id="okrOkrOut"></div></div>'+
      '<div class="u3-btnrow"><button type="button" class="u3-b" id="okrConfirmBtn" onclick="okrConfirm()">✓ Confirm Enterprise Priorities and OKRs</button></div>'+
      '<div class="u3-note" id="okrMsg" style="display:none;"></div>';
  }
  var done=okrConfirmed(),pri=okrPriText(),okr=okrOkrText();
  var a=u3el('okrPriOut'),b=u3el('okrOkrOut');
  a.textContent=pri||'Your enterprise priorities appear here as you complete Steps 5 and 6.';a.classList.toggle('empty',!pri);
  b.textContent=okr||'Your enterprise OKRs appear here as you complete Steps 2, 3 and 5.';b.classList.toggle('empty',!okr);
  u3el('okrPillA').style.display=done?'':'none';u3el('okrPillB').style.display=done?'':'none';
  u3el('okrConfirmBtn').classList.toggle('ok',done);
  if(done)u3msg('okrMsg','');
}
function renderOkrTool(){
  var host=u3el('okrToolP');if(!host)return;
  host.innerHTML='<div class="step-tabs" id="okrSTabs">'+OKR_STEPS.map(function(n,i){
    return '<div class="step-tab'+(i===OK.step?' active':'')+'" onclick="okrStep('+i+')"><div class="step-num">Step '+(i+1)+'</div><div class="step-name">'+n+'</div></div>';
  }).join('')+'</div><div class="step-panel active" id="okrPanel">'+okrPanelHtml()+'</div>';
  renderOkrOut();
}
function okrStep(i){
  if(i<0||i>5)return;
  OK.step=i;renderOkrTool();okrQueue();
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
  await u3save('okr_drafts',okrDraftText());
  if(U3._odirty){U3._odirty=false;await u3save('confirmed_items',U3.conf);}
}
function okrSet(i,f,val){OK.items[i][f]=val;okrTouch();}
function okrKr(i,j,f,val){
  OK.items[i].krs[j][f]=val;
  if(f==='t'){var c=u3el('okrChk_'+i+'_'+j);if(c)c.innerHTML=okrKrCheck(val);}
  okrTouch();
}
function okrChanged(){renderOkrOut();}
function okrAl(i,q,on){OK.items[i].al[q]=!!on;okrTouch();u3el('okrPanel').innerHTML=okrPanelHtml();}
function okrPri(i,box){
  if(box.checked&&okrPris().length>=4){box.checked=false;u3msg('okrPriMsg','The Less is More Rule: no more than four Enterprise Objectives. Release one before you add another.');return;}
  OK.items[i].pri=box.checked;okrTouch();u3el('okrPanel').innerHTML=okrPanelHtml();renderOkrOut();
}
function okrMx(i,f,val){OK.items[i][f]=val;okrTouch();u3el('okrPanel').innerHTML=okrPanelHtml();renderOkrOut();}
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

function toggleDomain(id){u3ToggleDomain(id);}
