/* ── SECTION 5 · YOUR COMPANY'S STRATEGY (group work, Capstone work, one group record) ──
   Built 19 October 2026. The group's scribe types; the entries appear on every member's page
   (S2RTeam, s2r-team.js). Each member selects Agree; when every member has agreed, the names
   below go into each member's confirmed list and the Capstone Blueprint brings the outputs in.
   Keys (lens u2m1_lens1): strategy_period, arch_eNN_qN, arch_eNN_rs (what the element is saying),
   arch_output, intent_statement, sip_dN_qN, sip_dN_st. The page writes no statement for the group. */
var U2={v:{},cur:0,step:0,pc:{}};
var N_ARCH='Strategy Architecture',N_INTENT='Strategy Intent Statement',N_SIP='Success in Practice';
var U2_LENS='u2m1_lens1';
function pad2(n){return (n<10?'0':'')+n;}
function qk(i,j){return 'arch_e'+pad2(i+1)+'_q'+(j+1);}
function rk(i){return 'arch_e'+pad2(i+1)+'_rs';}
function sqk(d,j){return 'sip_d'+(d+1)+'_q'+(j+1);}
function ssk(d){return 'sip_d'+(d+1)+'_st';}
function scn(d){return 'SiP · '+SIPD[d].t;}
function u2Names(){return [N_ARCH,N_INTENT].concat(SIPD.map(function(_,d){return scn(d);})).concat([N_SIP]);}
function u2v(k){var x=U2.v[k];return (x===undefined||x===null)?'':String(x);}
function u2t(k){return u2v(k).replace(/\s+/g,' ').trim();}
function u2esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u2el(id){return document.getElementById(id);}
function u2Key(k){return /^(strategy_period$|arch_e\d\d_(q\d|rs)$|arch_output$|intent_statement$|sip_d[1-4]_(q[1-3]|st)$)/.test(k);}
function u2In(k,val){U2.v[k]=val;if(window.S2RTeam)S2RTeam.save(k,val);u2Live(k);}
function elIndex(name){for(var i=0;i<EL.length;i++){if(EL[i].n===name)return i;}return -1;}
function elDone(i){return !!u2t(rk(i));}
function elDoneCount(){var n=0;EL.forEach(function(_,i){if(elDone(i))n++;});return n;}
function u2Company(){return String(U2.pc.company||'').trim();}

/* What is still missing before the group can agree ('' when complete). */
function u2Missing(){
  var out=[],n=EL.length-elDoneCount();
  if(n)out.push(n+' of the 14 elements still need what the element is saying');
  if(!u2t('arch_output'))out.push('the Strategy Architecture');
  if(!u2t('intent_statement'))out.push('the Strategy Intent Statement');
  var s=SIPD.filter(function(_,d){return !u2t(ssk(d));}).length;
  if(s)out.push(s+' of the 4 SiP statements');
  return out.join('; ');
}

/* Small live updates that keep the scribe's cursor in place. */
function u2Live(k){
  if(/_rs$/.test(k)){u2Chips();var b=u2el('u2bArchBtn');if(b)b.disabled=elDoneCount()<EL.length;var c=u2el('u2bCount');if(c)c.textContent=elDoneCount()+' of 14';}
  if(k==='intent_statement'){var m=u2el('u2bIntentMirror');if(m)m.textContent=u2t('intent_statement')||'Your Strategy Intent Statement appears here once your group writes it in Step 2.';}
  if(window.S2RTeam)S2RTeam.redraw();
}

/* The group's Problem Charter company, read-only. */
async function u2LoadCharter(){
  var r={};try{r=await S2R.loadAll('u1_foundations');}catch(e){r={};}
  var conf=Array.isArray(r.confirmed_items)?r.confirmed_items:[];
  function g(k,n){return conf.indexOf(n)>=0&&typeof r[k]==='string'?r[k].trim():'';}
  U2.pc={company:g('pc_company','Problem Charter · Simulated Company'),team:g('pc_team','Problem Charter · Executive Team'),
         org:g('pc_org','Problem Charter · Our Organisation'),problem:g('pc_problem','Problem Charter · Central Organisational Problem')};
  u2Charter();
}
function u2Charter(){
  var host=u2el('u2bCharter');if(!host)return;
  var p=U2.pc;
  if(!p.company){host.innerHTML='<div class="u2-locked">Your group\'s company appears here once every member of your group has agreed your Problem Charter in Unit 1, part 6.2.</div>';return;}
  host.innerHTML='<div class="u2b-co">'+
    '<div class="u2b-co-c"><b>Your simulated company</b><span>'+u2esc(p.company)+'</span></div>'+
    (p.org?'<div class="u2b-co-c"><b>Our organisation</b><span>'+u2esc(p.org)+'</span></div>':'')+
    (p.team?'<div class="u2b-co-c"><b>Your executive team</b><span>'+u2esc(p.team)+'</span></div>':'')+
    (p.problem?'<div class="u2b-co-c u2b-wide"><b>Your central organisational problem</b><span>'+u2esc(p.problem)+'</span></div>':'')+
  '</div>';
}

function u2Step(i){
  U2.step=i;
  document.querySelectorAll('#u2bTool .step-tab').forEach(function(t,x){t.classList.toggle('active',x===i);});
  document.querySelectorAll('#u2bTool .step-panel').forEach(function(p,x){p.classList.toggle('active',x===i);});
  u2RenderStep(i);
}
function u2RenderStep(i){if(i===0)u2RenderArch();else if(i===1)u2RenderIntent();else if(i===2)u2RenderSip();else u2RenderRecord();if(window.S2RTeam)S2RTeam.redraw();}
function u2RenderAll(){u2Charter();u2RenderStep(U2.step);}

function u2Chips(){
  var host=u2el('u2bChips');if(!host)return;
  host.innerHTML=EL.map(function(e,i){
    return '<button type="button" class="u2-chip'+(i===U2.cur?' active':'')+(elDone(i)?' done':'')+'" data-team-free onclick="u2Go('+i+')"><span class="u2-chip-n">'+(elDone(i)?'✓':(i+1))+'</span>'+u2esc(e.n)+'</button>';
  }).join('');
}
function u2Go(i){U2.cur=Math.max(0,Math.min(EL.length-1,i));u2RenderEl();u2Chips();}
function u2RenderEl(){
  var host=u2el('u2bEl');if(!host)return;
  var i=U2.cur,e=EL[i];
  host.innerHTML='<div class="u2b-grid"><div class="u2b-lesson"><div class="u2b-lesson-h">The lesson for this element</div>'+
      '<div class="u2-el-name">'+(i+1)+' · '+u2esc(e.n)+'</div><div class="u2-el-tag">'+u2esc(e.tag)+'</div><p>'+u2esc(e.guide)+'</p></div>'+
    '<div class="u2b-entry">'+
      e.qs.map(function(q,j){var k=qk(i,j);return '<label class="u2-q" for="'+k+'">'+u2esc(q)+'</label><textarea class="port-ta u2b-ta" id="'+k+'" oninput="u2In(\''+k+'\',this.value)" placeholder="Your group\'s answer…">'+u2esc(u2v(k))+'</textarea>';}).join('')+
      '<label class="u2-q u2b-say" for="'+rk(i)+'">What this element is saying</label>'+
      '<textarea class="port-ta u2b-ta" id="'+rk(i)+'" oninput="u2In(\''+rk(i)+'\',this.value)" placeholder="In one or two sentences, what your answers say about your strategy…">'+u2esc(u2v(rk(i)))+'</textarea>'+
    '</div></div>'+
    '<div class="u2-elnav"><button type="button" class="btn" data-team-free onclick="u2Go('+(i-1)+')"'+(i===0?' disabled':'')+'>← Previous element</button><button type="button" class="btn" data-team-free onclick="u2Go('+(i+1)+')"'+(i===EL.length-1?' disabled':'')+'>Next element →</button></div>';
}
function u2RenderArch(){
  u2Chips();u2RenderEl();
  var host=u2el('u2bArch');if(!host)return;
  host.innerHTML='<div class="u2b-grid"><div class="u2b-lesson"><div class="u2b-lesson-h">The lesson for the Strategy Architecture</div>'+
      '<p>Step back from the single elements and read them as one strategic system: <em>"What is this architecture collectively saying about our organisation\'s strategy?"</em></p>'+
      '<p>Check together: Do our choices reinforce one another? Where are there contradictions or unresolved tensions? Does our HOW support what we have chosen to achieve? Does our timing and sequencing reflect the realities of our capability and environment? Have we addressed how value will be created, delivered and sustained? Does the architecture represent the strategic position we collectively intend?</p></div>'+
    '<div class="u2b-entry"><div class="u2b-count">Elements with what they are saying: <b id="u2bCount">'+elDoneCount()+' of 14</b></div>'+
      '<div class="u2-btnrow tw-scribe-only"><button type="button" class="u2-b" id="u2bArchBtn" onclick="u2ArchBring()"'+(elDoneCount()<EL.length?' disabled':'')+'>Bring the 14 elements together</button></div>'+
      '<label class="u2-q" for="arch_output">Your Strategy Architecture, under its five headings</label>'+
      '<textarea class="port-ta u2b-ta" id="arch_output" style="min-height:280px;" oninput="u2In(\'arch_output\',this.value)" placeholder="When all 14 elements say what they mean, the scribe brings them together here under the five headings. Your group then edits the text until it says what your group intends.">'+u2esc(u2v('arch_output'))+'</textarea>'+
    '</div></div>';
}
function u2ArchBring(){
  if(elDoneCount()<EL.length)return;
  if(u2t('arch_output')&&!window.confirm('Replace the text in the box with the 14 elements as they stand now?'))return;
  var txt=ARCH_GROUPS.map(function(g){return g[0]+'\n'+g[1].map(function(n){var i=elIndex(n);return n+': '+u2t(rk(i));}).join('\n');}).join('\n\n');
  var ta=u2el('arch_output');if(ta)ta.value=txt;u2In('arch_output',txt);
}
function u2RenderIntent(){
  var host=u2el('u2bIntent');if(!host)return;
  host.innerHTML='<div class="u2b-grid"><div class="u2b-lesson"><div class="u2b-lesson-h">The lesson for this step</div>'+
      '<p>The Architecture holds the depth. The Intent gives the clarity: one crisp statement of strategic ambition that carries WHAT, WHY, HOW and WHEN.</p>'+
      '<p><b>Protect the Intent from overload.</b> Leave the detail in the Architecture. A strong Intent lets a leader understand your strategic position without a paragraph of explanation.</p>'+
      '<p>Read your statement against your Architecture: <em>"Does this statement faithfully express the strategic ambition contained in our Architecture?"</em> Where it exposes a contradiction, resolve the contradiction in the Architecture first.</p></div>'+
    '<div class="u2b-entry"><div class="u2-grid">'+DIM4.map(function(d){var i=elIndex(d[0]),t=i<0?'':u2t(rk(i));
        return '<div class="u2-card"><div class="u2-card-h">'+d[0]+' — '+u2esc(d[1])+'</div><p>'+u2esc(d[2])+'</p><div class="u2-mirror-lbl">What your element is saying</div>'+
          (t?'<div class="u2-mirror">'+u2esc(t)+'</div>':'<div class="u2-mirror empty">Appears here once your group writes it in Step 1.</div>')+'</div>';}).join('')+'</div>'+
      '<label class="u2-q" for="intent_statement">Your Strategy Intent Statement</label>'+
      '<textarea class="port-ta u2b-ta" id="intent_statement" style="min-height:110px;" oninput="u2In(\'intent_statement\',this.value)" placeholder="One crisp statement your group deduces from WHAT, WHY, HOW and WHEN…">'+u2esc(u2v('intent_statement'))+'</textarea>'+
    '</div></div>';
}
function u2RenderSip(){
  var host=u2el('u2bSip');if(!host)return;
  var it=u2t('intent_statement');
  host.innerHTML='<div class="u2b-grid"><div class="u2b-lesson"><div class="u2b-lesson-h">The lesson for this step</div>'+
      '<p>Stand inside the future your Strategy Intent describes and ask: <em>"If our Strategy Intent is successful, what should we see in practice?"</em></p>'+
      '<p>For each domain, answer the three questions, then write one statement for the domain from your answers. Use the observable indicators from Section 3 to deepen the discussion.</p>'+
      '<p><b>Depth.</b> Could you recognise each condition if you saw it in practice?</p>'+
      '<p><b>Balance.</b> Do the four statements together describe enterprise success? Use the SiP Flammables from 3.2 as the final balance check.</p></div>'+
    '<div class="u2b-entry"><div class="u2-out"><div class="u2-out-h">Your Strategy Intent Statement</div><div class="u2-mirror'+(it?'':' empty')+'" id="u2bIntentMirror">'+u2esc(it||'Your Strategy Intent Statement appears here once your group writes it in Step 2.')+'</div></div>'+
      SIPD.map(function(x,d){
        return '<details class="u2b-det"'+(d===0?' open':'')+'><summary>D'+(d+1)+' · '+u2esc(x.t)+'</summary><p class="u2b-lead">'+u2esc(x.lead)+'</p>'+
          x.qs.map(function(q,j){var k=sqk(d,j);return '<label class="u2-q" for="'+k+'">'+u2esc(q)+'</label><textarea class="port-ta u2b-ta" id="'+k+'" oninput="u2In(\''+k+'\',this.value)" placeholder="Your group\'s answer…">'+u2esc(u2v(k))+'</textarea>';}).join('')+
          '<label class="u2-q u2b-say" for="'+ssk(d)+'">Your SiP statement · '+u2esc(x.t)+'</label><textarea class="port-ta u2b-ta" id="'+ssk(d)+'" oninput="u2In(\''+ssk(d)+'\',this.value)" placeholder="One statement for this domain, written from your answers…">'+u2esc(u2v(ssk(d)))+'</textarea></details>';
      }).join('')+
    '</div></div>';
}
function u2RecRow(label,text){return '<div class="u7-rec"><div class="u7-rec-s">'+u2esc(label)+'</div><div class="u7-rec-t">'+(text?u2esc(text):'<i>Not written yet.</i>')+'</div></div>';}
function u2RenderRecord(){
  var host=u2el('u2bRecord');if(!host)return;
  var miss=u2Missing();
  host.innerHTML=(miss?'<div class="u2-note">Still to complete: '+u2esc(miss)+'.</div>':'<div class="u2-ok">✓ Every part of the record is written. Each member reads it and selects Agree in the group record bar above.</div>')+
    u2RecRow('Company',u2Company())+u2RecRow('Strategy period',u2t('strategy_period'))+
    u2RecRow('Strategy Architecture',u2v('arch_output').trim())+u2RecRow('Strategy Intent Statement',u2t('intent_statement'))+
    SIPD.map(function(x,d){return u2RecRow('SiP '+(d+1)+' · '+x.t,u2t(ssk(d)));}).join('')+
    '<div class="u2-btnrow"><button type="button" class="u2-b" data-team-free onclick="u2Print(\'all\')"'+(miss?' disabled':'')+'>Print the three outputs</button></div>';
}

/* ── Printed report: Strategy Architecture → Strategy Intent → Success in Practice ── */
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
function rptIntent(){return '<section class="section"><div class="section-title">Strategy Intent Statement</div><div class="section-rule"></div><div class="intent-panel">'+u2esc(u2t('intent_statement'))+'</div></section>';}
function rptSip(){
  return '<section class="section"><div class="section-title">Success in Practice</div><div class="section-rule"></div>'+
    SIPD.map(function(x,d){return '<div class="sip-card"><div class="sip-kicker">Statement '+(d+1)+'</div><div class="sip-title">'+u2esc(x.t)+'</div><div class="sip-text">'+u2esc(u2t(ssk(d)))+'</div></div>';}).join('')+'</section>';
}
function rptShell(title,body){
  var org=u2Company()||'Organisation',period=u2t('strategy_period');
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
function u2Print(){
  var w=window.open('','_blank');
  if(!w){alert('Please allow pop-ups for this page to print your three outputs.');return;}
  w.document.open();w.document.write(rptShell('Strategy Intent Design','<div class="summary-band">Strategy Architecture → Strategy Intent → Success in Practice</div>'+rptArch()+'<div class="report-break"></div>'+rptIntent()+rptSip()));w.document.close();
}

/* Fill the tool from saved answers (own page or the group record). */
function u2Fill(responses){
  U2.v={};
  Object.keys(responses||{}).forEach(function(k){if(u2Key(k)&&responses[k]!==null&&responses[k]!==undefined)U2.v[k]=responses[k];});
  var p=u2el('strategy_period');if(p&&document.activeElement!==p)p.value=u2v('strategy_period');
}
async function u2Attach(){
  if(!window.S2RTeam)return;
  await S2RTeam.attach({lens:U2_LENS,mount:'u2bTeam',lock:['u2bTool'],names:u2Names(),complete:u2Missing,
    onRemote:async function(r){u2Fill(r);u2RenderAll();}});
}
