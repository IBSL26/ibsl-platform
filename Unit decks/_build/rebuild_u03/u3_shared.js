// ── UNIT 3 · SHARED DATA (same in the participant and facilitator files) ─────────────────────────
var KISS_DOMAINS=[
  {id:'cx',cls:'cx',label:'Customer Experience & Value',anchor:'If our SiP statement is true, what should customers consistently experience?',
   keep:'Which aspects of the current customer experience already move us toward the SiP and should be protected?',
   improve:'Where do we see good customer outcomes but recurring friction that weakens reliability or responsiveness?',
   start:'What new practices or capabilities must begin for customers to experience the organisation as described in the SiP?',
   stop:'Which processes or behaviours create customer friction and contradict the SiP experience we described?'},
  {id:'op',cls:'op',label:'Operational Capability & Execution Rhythm',anchor:'If the SiP becomes reality, how will the organisation operate differently?',
   keep:'Which operational routines already support the execution rhythm described in the SiP?',
   improve:'Where do we see operational capability but delays, coordination gaps, or decision bottlenecks?',
   start:'What new execution rhythms, coordination practices, or decision frameworks must be introduced?',
   stop:'Which processes, reporting routines, or meetings consume effort without strengthening execution?'},
  {id:'pc',cls:'pc',label:'People & Culture Dynamics',anchor:'If the SiP is realised, how will leaders and teams work together?',
   keep:'Which leadership behaviours and collaboration patterns already reinforce the culture described in the SiP?',
   improve:'Where do we see positive teamwork but inconsistent accountability or unclear ownership?',
   start:'What new leadership habits or collaboration norms must be introduced?',
   stop:'Which behaviours, informal norms, or leadership practices undermine alignment or trust?'},
  {id:'ev',cls:'ev',label:'Enterprise Value Creation',anchor:'If the SiP succeeds, what financial reality should we see?',
   keep:'Which business activities or revenue streams already support the value creation described in the SiP?',
   improve:'Where do we see positive results but margin pressure or inefficient resource use?',
   start:'What new investments, capabilities, or revenue engines must be introduced?',
   stop:'Which initiatives or commitments consume resources without contributing to the value creation described in the SiP?'}
];
var KISS_EL=[['keep','KEEP'],['improve','IMPROVE'],['start','START'],['stop','STOP']];

var HOT_ZONES=[
  {role:'CEO',title:'Chief Executive Officer',top2:'Enterprise Value Creation · Customer Experience & Value',emphasis:'Strategic ambition and market positioning',hot:'Objectives become visionary but insufficiently grounded in operational capability',align:'Do our OKRs translate ambition into outcomes the organisation can reliably deliver?'},
  {role:'CFO',title:'Chief Financial Officer',top2:'Enterprise Value Creation · Operational Capability & Execution Rhythm',emphasis:'Financial performance and efficiency',hot:'Key Results become overly financial, ignoring customer or capability drivers',align:'Are we measuring the drivers of value creation as well as the financial outcomes?'},
  {role:'COO',title:'Chief Operating Officer',top2:'Operational Capability & Execution Rhythm · Enterprise Value Creation',emphasis:'Operational reliability and execution efficiency',hot:'Objectives drift toward operational optimisation and away from strategic transformation',align:'Are our OKRs reinforcing strategic movement, beyond operational performance?'},
  {role:'CHRO',title:'Chief People & Culture Officer',top2:'People & Culture Dynamics · Operational Capability & Execution Rhythm',emphasis:'Capability development and organisational health',hot:'Objectives emphasise culture initiatives without clear connection to enterprise results',align:'Do our people objectives clearly support strategic outcomes?'},
  {role:'CTO/CIO',title:'Chief Technology / Information Officer',top2:'Operational Capability & Execution Rhythm · Customer Experience & Value',emphasis:'Technology capability and digital infrastructure',hot:'Key Results become technology delivery milestones with no line of sight to business outcomes',align:'Are we measuring the impact technology creates for customers and the enterprise?'},
  {role:'CMO',title:'Chief Marketing Officer',top2:'Customer Experience & Value · Enterprise Value Creation',emphasis:'Market positioning and brand strength',hot:'Objectives emphasise perception beyond what the organisation can consistently deliver',align:'Do our OKRs balance customer promise with operational capability?'},
  {role:'CCO',title:'Chief Commercial Officer',top2:'Enterprise Value Creation · Customer Experience & Value',emphasis:'Revenue growth and commercial expansion',hot:'Key Results prioritise sales outcomes without strengthening the customer experience system',align:'Are we building repeatable value creation, beyond short-term revenue?'},
  {role:'CPO',title:'Chief Procurement Officer',top2:'Operational Capability & Execution Rhythm · Enterprise Value Creation',emphasis:'Supply chain efficiency and cost discipline',hot:'Objectives prioritise cost optimisation at the expense of strategic capability development',align:'Are we balancing efficiency with long-term strategic capability?'},
  {role:'CRO',title:'Chief Risk Officer',top2:'Enterprise Value Creation · Operational Capability & Execution Rhythm',emphasis:'Risk control and regulatory protection',hot:'Key Results become defensive safeguards that slow strategic movement',align:'Are we enabling responsible risk-taking while protecting the organisation?'},
  {role:'CSO',title:'Chief Strategy Officer',top2:'Enterprise Value Creation · Operational Capability & Execution Rhythm',emphasis:'Strategic planning coherence',hot:'Objectives become conceptually strong but disconnected from operational ownership',align:'Are our OKRs grounded in clear accountability and execution ownership?'}
];

// The nine positions of the Prioritisation Matrix: impact, effort, name, colour, meaning.
var PM_CATS=[
  {i:'High',e:'Low',l:'Strategic Catalysts',c:'rgba(39,174,96,.7)',d:'Quick breakthroughs that accelerate strategic momentum.'},
  {i:'High',e:'Medium',l:'Accelerated Enablers',c:'rgba(52,152,219,.7)',d:'Important initiatives requiring coordination but delivering strong value.'},
  {i:'High',e:'High',l:'Core Strategic Drivers',c:'rgba(155,89,182,.7)',d:'Major transformation initiatives essential to achieving the SiP.'},
  {i:'Medium',e:'Low',l:'Quick Efficiency Plays',c:'rgba(243,156,18,.7)',d:'Improvements that enhance performance with minimal effort.'},
  {i:'Medium',e:'Medium',l:'Targeted Growth Projects',c:'rgba(201,168,76,.7)',d:'Initiatives contributing to strategic progress but not immediate priorities.'},
  {i:'Medium',e:'High',l:'Heavy Investment Candidates',c:'rgba(230,126,34,.7)',d:'Initiatives requiring significant resources and careful timing.'},
  {i:'Low',e:'Low',l:'Supportive Enablers',c:'rgba(149,165,166,.6)',d:'Helpful but non-critical initiatives.'},
  {i:'Low',e:'Medium',l:'Marginal Utility Tasks',c:'rgba(149,165,166,.5)',d:'Limited strategic return relative to effort.'},
  {i:'Low',e:'High',l:'Resource Pitfalls',c:'rgba(231,76,60,.7)',d:'Consume significant energy without meaningful strategic value.'}
];
function pmFind(impact,effort){for(var k=0;k<PM_CATS.length;k++){if(PM_CATS[k].i===impact&&PM_CATS[k].e===effort)return PM_CATS[k];}return null;}
function u3esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
// Step tabs: tabs sit in #<prefix>Tabs, panels carry ids <prefix>_0, <prefix>_1 …
function u3Tab(prefix,i){
  document.querySelectorAll('#'+prefix+'Tabs .step-tab').forEach(function(t,x){t.classList.toggle('active',x===i);});
  document.querySelectorAll('[id^="'+prefix+'_"]').forEach(function(p,x){p.classList.toggle('active',x===i);});
}
function renderPMCards(hostId){
  var el=document.getElementById(hostId);if(!el)return;
  el.innerHTML='<div class="u3-pm">'+PM_CATS.map(function(c){
    return '<div class="u3-pm-card" style="border-left:2px solid '+c.c+';"><div class="u3-pm-h" style="color:'+c.c+';">'+c.l+'</div><p>'+c.i+' Impact – '+c.e+' Effort: '+c.d+'</p></div>';
  }).join('')+'</div>';
}
function kissGuideHtml(prefix,toggleFn){
  return KISS_DOMAINS.map(function(d){
    return '<div class="kiss-domain" id="'+prefix+d.id+'">'+
      '<div class="kiss-domain-h" onclick="'+toggleFn+'(\''+prefix+d.id+'\')">'+
        '<div class="kiss-accent kiss-domain-accent '+d.cls+'"></div>'+
        '<div class="kiss-domain-info"><div class="kiss-domain-title">'+u3esc(d.label)+'</div>'+
        '<div class="kiss-domain-anchor">SiP Anchor: '+u3esc(d.anchor)+'</div></div>'+
        '<span class="kiss-domain-arr">▾</span></div>'+
      '<div class="kiss-domain-body" style="display:none;padding:0 18px 18px;">'+
        '<div class="u3-kgrid">'+KISS_EL.map(function(k){
          return '<div class="u3-kcell"><div class="kiss-el-head '+k[0]+'-h '+k[0]+'">◆ '+k[1]+'</div><div class="kiss-q kiss-el-prompt">'+u3esc(d[k[0]])+'</div></div>';
        }).join('')+'</div></div></div>';
  }).join('');
}
function u3ToggleDomain(id){
  var el=document.getElementById(id);if(!el)return;
  var body=el.querySelector('.kiss-domain-body'),arr=el.querySelector('.kiss-domain-arr');if(!body)return;
  var open=body.style.display!=='none'&&body.style.display!=='';
  body.style.display=open?'none':'block';
  if(arr)arr.style.transform=open?'':'rotate(180deg)';
}

// ── 2.2 · THE CASE: one simple SiP statement and its KISS table (client services company) ───────
// Both pages show the case. The worked answers of the six steps are in the facilitator file only (u3_f.js);
// participants take the case through the six steps themselves (u3_p.js).
var WORKED={
  sip:'We will be the service partner our clients rely on first, by ensuring every client experiences fast, consistent and effortless service. To achieve this, we will move quickly from insight to action across functions, build shared ownership of enterprise priorities and run scalable, efficient operations that strengthen enterprise performance.',
  kiss:[
    {domain:'Customer Experience & Value',cls:'cx',keep:'Strong client relationships with key accounts',improve:'Response time to customer requests varies across teams',start:'Introduce proactive customer engagement model',stop:'Slow internal handovers that delay customer responses'},
    {domain:'Operational Capability & Execution Rhythm',cls:'op',keep:'Clear strategic priorities already exist',improve:'Decision-making slows when multiple functions are involved',start:'Introduce cross-functional execution routines and faster decision forums',stop:'Excessive reporting cycles that delay action'},
    {domain:'People & Culture Dynamics',cls:'pc',keep:'Strong trust within teams',improve:'Collaboration across functions remains inconsistent',start:'Introduce shared ownership of enterprise priorities',stop:'Functional silos and escalation behaviours'},
    {domain:'Enterprise Value Creation',cls:'ev',keep:'Solid revenue base and loyal client segments',improve:'Profit margins fluctuate due to operational inefficiencies',start:'Develop scalable service delivery models',stop:'Low-value projects that absorb leadership attention'}
  ]
};
function renderCase(hostId){
  var host=document.getElementById(hostId);if(!host)return;
  var W=WORKED,col={keep:'#5ecba1',improve:'#f0c060',start:'#7ec8f0',stop:'#f08080'};
  var kiss=W.kiss.map(function(d){
    return '<div class="u3-wx-dom"><div class="u3-wx-dom-h"><span class="kiss-accent '+d.cls+'" style="display:inline-block;min-height:12px;height:12px;margin-right:8px;vertical-align:middle;"></span>'+u3esc(d.domain)+'</div><div class="u3-wx-row">'+
      KISS_EL.map(function(k){return '<div class="u3-wx-cell"><div class="u3-wx-k" style="color:'+col[k[0]]+';">'+k[1]+'</div><p>'+u3esc(d[k[0]])+'</p></div>';}).join('')+'</div></div>';
  }).join('');
  host.innerHTML='<div class="u3-wx-sip"><div class="u3-wx-sip-h">Case · Success in Practice statement of a client services company</div><p>'+u3esc(W.sip)+'</p></div>'+
    '<h4>From SiP to KISS</h4><p>The leadership team passes the SiP statement through the four KISS filters, one SiP domain at a time:</p>'+kiss;
}

// ── 5.1 · STRATEGY AIRPORT (Carol's game, Medical Health Company case) ─────────────────────────
var SA_SIP='We will deliver reliable, accessible and patient-centred healthcare by ensuring patients experience timely support, clear communication and coordinated care across every touchpoint. To achieve this, we will strengthen operational coordination, use data to guide decisions, build shared accountability across teams and improve service reliability, efficiency, patient trust and health outcomes.';
var SA_OPTIONS={
  keep:[["Existing patient trust",1,"Green light: this is a real strength to protect."],["Committed clinical teams",1,"Green light: this supports patient-centred delivery."],["Strong referral relationships",1,"Green light: this can improve access and continuity."],["Known community presence",1,"Green light: this can support trust and accessibility."],["Functional appointment channels",1,"Green light: this is useful infrastructure for access."],["Keep all approval layers because they create control",0,"Red alert: this protects bureaucracy, not timely patient care."],["Keep department-specific patient files separate",0,"Red alert: this weakens coordinated care."],["Keep complaints informal so teams are not blamed",0,"Red alert: this hides evidence the strategy needs."]],
  improve:[["Slow patient handovers",1,"Green light: this directly affects coordinated care."],["Inconsistent patient updates",1,"Green light: this affects clear communication."],["Delayed lab or test feedback",1,"Green light: this affects timely support."],["Fragmented patient records",1,"Green light: this affects reliability and coordination."],["Long waiting times",1,"Green light: this affects accessibility."],["Improve the poster design for the strategy launch",0,"Red alert: this is communication activity, not operational reality."],["Improve executive parking arrangements",0,"Red alert: this does not support the SiP."],["Improve the wording of internal slogans",0,"Red alert: slogans are not evidence of patient-centred care."]],
  start:[["Patient journey dashboard",1,"Green light: this supports data-guided decisions."],["Weekly care coordination huddles",1,"Green light: this supports execution rhythm."],["Single patient update protocol",1,"Green light: this supports clear communication."],["Data-based service reviews",1,"Green light: this supports learning and reliability."],["Clear handover standard",1,"Green light: this supports coordinated care."],["Start a new committee for every service issue",0,"Red alert: more committees may slow execution."],["Start collecting more data without deciding how it will be used",0,"Red alert: data without decisions creates noise."],["Start sending all decisions to the CEO",0,"Red alert: this weakens shared accountability."]],
  stop:[["Asking patients for the same information repeatedly",1,"Green light: this directly reduces patient friction."],["Departments handing off without ownership",1,"Green light: this supports accountability."],["Reporting activity in place of patient outcomes",1,"Green light: this protects outcome discipline."],["Treating complaints as isolated incidents",1,"Green light: this supports system learning."],["Launching initiatives without capacity",1,"Green light: this protects execution discipline."],["Stop patient feedback because it creates pressure",0,"Red alert: this removes patient evidence."],["Stop cross-functional meetings to save time",0,"Red alert: this weakens coordination."],["Stop measuring waiting time if performance is poor",0,"Red alert: this hides reliability problems."]]
};
var SA_ORDER={keep:[5,0,6,1,3,7,2,4],improve:[0,5,2,6,1,7,3,4],start:[5,0,6,1,3,7,2,4],stop:[0,5,1,6,2,7,3,4]};
var SA_CARDS=[
  ['keep','KEEP','What must be protected because it already supports the SiP?','Existing patient trust\nCommitted clinical teams'],
  ['improve','IMPROVE','What must work better because it weakens delivery?','Slow patient handovers\nDelayed communication'],
  ['start','START','What must begin because it is missing?','Patient journey dashboard\nWeekly care coordination huddles'],
  ['stop','STOP','What must stop because it contradicts the SiP?','Duplicated patient information requests\nDepartments handing off without ownership']
];
// Wording that differs between the facilitator's lesson round ('f') and the participant's own round ('p').
var SA_TXT={
  f:{g1:'Use the SiP statement above. Ask the group to choose an option. The facilitator clicks it, and the system will then show a green light or red alert.',
     rule:'Game rule: let participants choose first. The answer is revealed only after selection.',
     g2:'The KISS choices have now become your OKR themes. Ask the group to pick one theme, then convert it into one Objective and two Key Results.',
     pick:'Choose one KISS theme above. The system will translate it into a draft OKR for the group to test and edit.',
     done:'The team has translated the medical health SiP into KISS insights, then converted one selected theme into an Objective and two Key Results.'},
  p:{g1:'Use the SiP statement above. Choose an option for each filter. The system will then show a green light or red alert.',
     rule:'Game rule: choose first. The answer is revealed only after you select.',
     g2:'Your KISS choices have now become your OKR themes. Pick one theme, then convert it into one Objective and two Key Results.',
     pick:'Choose one KISS theme above. The system will translate it into a draft OKR for you to test and edit.',
     done:'You have translated the medical health SiP into KISS insights, then converted one selected theme into an Objective and two Key Results.'}
};
var SA={mode:'f',host:null,onChange:null,state:{step:1,kiss:{keep:'',improve:'',start:'',stop:''},okrs:[]}};
function saLines(v){return String(v||'').split('\n').map(function(x){return x.trim();}).filter(Boolean);}
function saEl(id){return document.getElementById(id);}
function saChanged(){if(SA.onChange)SA.onChange(SA.state);}
function saInit(hostId,mode,onChange){
  SA.host=document.getElementById(hostId);if(!SA.host)return;
  SA.mode=mode;SA.onChange=onChange||null;
  SA.host.innerHTML='<div class="sa">'+
    '<div class="sa-head"><div><div class="sa-title">Strategy Airport</div><div class="sa-tag">Move from strategic imagination to operational clearance.</div></div><div class="sa-badge">Medical Health Company Case</div></div>'+
    '<div class="sa-sip"><div class="sa-sip-h">Success in Practice Statement</div><p>'+u3esc(SA_SIP)+'</p></div>'+
    '<div class="sa-board"><div id="saGate1" class="sa-gate"><small>Gate 1</small><div class="sa-gate-n">Baggage Check</div><p>KISS Mapping</p><span class="sa-status">Open</span></div>'+
    '<div id="saGate2" class="sa-gate"><small>Gate 2</small><div class="sa-gate-n">Flight Plan</div><p>OKR Construction</p><span class="sa-status">Locked</span></div></div>'+
    '<div class="sa-screen" id="saScreen"></div></div>';
  saRender();
}
function saLoad(state){
  if(state&&typeof state==='object'){
    var k=state.kiss||{};
    SA.state={step:state.step===2||state.step===3?state.step:1,kiss:{keep:String(k.keep||''),improve:String(k.improve||''),start:String(k.start||''),stop:String(k.stop||'')},okrs:Array.isArray(state.okrs)?state.okrs.slice(0,4):[]};
  }
  if(SA.host)saRender();
}
function saRender(){if(SA.state.step===3)saRenderDone();else if(SA.state.step===2)saRenderOkr();else saRenderKiss();}
function saGates(){
  [1,2].forEach(function(n){
    var g=saEl('saGate'+n);if(!g)return;
    g.className='sa-gate'+(n<SA.state.step?' done':n===SA.state.step?' active':' locked');
    g.querySelector('.sa-status').textContent=n<SA.state.step?'Complete':n===SA.state.step?'Open':'Locked';
  });
}
function saKissCard(c){
  var key=c[0];
  return '<div class="sa-card"><div class="sa-card-h">'+c[1]+'</div><p class="sa-hint">'+c[2]+'</p>'+
    '<textarea class="sa-ta" id="sa_'+key+'" placeholder="'+u3esc(c[3])+'" oninput="saKissInput(\''+key+'\',this.value)">'+u3esc(SA.state.kiss[key])+'</textarea>'+
    '<div class="sa-options">'+SA_ORDER[key].map(function(i){return '<span class="sa-chip" onclick="saAdd(\''+key+'\','+i+')">'+u3esc(SA_OPTIONS[key][i][0])+'</span>';}).join('')+'</div></div>';
}
function saRenderKiss(){
  saGates();var T=SA_TXT[SA.mode];
  saEl('saScreen').innerHTML='<div class="sa-st"><div><div class="sa-st-h">Gate 1: Baggage Check</div><p>'+T.g1+'</p></div>'+
    (SA.mode==='f'?'<button type="button" class="sa-btn gold" onclick="saFill()">Use Example</button>':'')+'</div>'+
    '<div class="sa-grid4">'+SA_CARDS.map(saKissCard).join('')+'</div>'+
    '<div id="saKissMsg" class="sa-msg">'+T.rule+'</div>'+
    '<div class="sa-actions"><button type="button" class="sa-btn ghost" onclick="saReset()">Reset Game</button><button type="button" class="sa-btn" onclick="saToGate2()">Proceed to Flight Plan</button></div>';
}
function saKissInput(key,val){SA.state.kiss[key]=val;saChanged();}
function saAdd(key,index){
  var opt=SA_OPTIONS[key][index],msg=saEl('saKissMsg');
  if(!opt[1]){msg.className='sa-msg danger';msg.textContent=opt[2];return;}
  var el=saEl('sa_'+key),existing=saLines(el.value);
  if(existing.indexOf(opt[0])<0){existing.push(opt[0]);el.value=existing.join('\n');SA.state.kiss[key]=el.value;saChanged();}
  msg.className='sa-msg success';msg.textContent=opt[2];
}
function saFill(){
  SA.state.kiss={keep:'Strong patient relationships\nCommitted nurses and clinical teams',improve:'Slow handovers between departments\nPatient communication is inconsistent',start:'Patient journey dashboard\nWeekly cross-functional care coordination huddles',stop:'Asking patients for the same information repeatedly\nTreating service failures as one department\'s problem'};
  saRenderKiss();saChanged();
}
function saToGate2(){
  ['keep','improve','start','stop'].forEach(function(k){var el=saEl('sa_'+k);if(el)SA.state.kiss[k]=el.value;});
  var missing=['keep','improve','start','stop'].filter(function(k){return saLines(SA.state.kiss[k]).length<2;}).map(function(k){return k.toUpperCase();});
  var msg=saEl('saKissMsg');
  if(missing.length){msg.className='sa-msg danger';msg.textContent='Not cleared: add at least two items for '+missing.join(', ')+'.';return;}
  SA.state.step=2;saRenderOkr();saChanged();
}
function saThemes(){var out=[];['keep','improve','start','stop'].forEach(function(k){saLines(SA.state.kiss[k]).forEach(function(v){out.push({type:k.toUpperCase(),text:v});});});return out;}
function saOkrFromTheme(theme){
  var t=theme.text.toLowerCase();
  if(t.indexOf('handover')>=0||t.indexOf('coordin')>=0)return {objective:'Strengthen coordinated care across patient touchpoints',kr1:'Reduce patient handover delays from 48 hours to 12 hours by 31 March 2027',kr2:'Increase complete patient handover records from 60% to 95% by 31 March 2027',roles:'Clinical Teams, Operations, Care Coordinators, IT'};
  if(t.indexOf('update')>=0||t.indexOf('communication')>=0||t.indexOf('complaint')>=0)return {objective:'Improve clarity and consistency of patient communication',kr1:'Increase patients receiving clear status updates from 50% to 90% by 31 March 2027',kr2:'Reduce communication-related complaints from 80 to 30 per quarter by 31 March 2027',roles:'Customer Support, Clinical Teams, Operations, Communications'};
  if(t.indexOf('waiting')>=0||t.indexOf('appointment')>=0||t.indexOf('access')>=0||t.indexOf('referral')>=0)return {objective:'Improve timely access to patient-centred care',kr1:'Reduce average appointment waiting time from 14 days to 7 days by 31 March 2027',kr2:'Increase same-day response to patient enquiries from 55% to 90% by 31 March 2027',roles:'Operations, Clinical Teams, Customer Support, IT'};
  if(t.indexOf('data')>=0||t.indexOf('dashboard')>=0||t.indexOf('review')>=0||t.indexOf('records')>=0)return {objective:'Use service data to improve patient outcomes and reliability',kr1:'Increase weekly review of patient service data from 0 to 4 reviews per month by 31 March 2027',kr2:'Reduce unresolved service exceptions older than 7 days from 40 to 10 by 31 March 2027',roles:'Executive Team, Operations, IT, Quality Assurance'};
  if(t.indexOf('ownership')>=0||t.indexOf('accountability')>=0||t.indexOf('capacity')>=0||t.indexOf('initiative')>=0)return {objective:'Build shared accountability for patient-centred execution',kr1:'Increase cross-functional issue closure within 5 working days from 45% to 85% by 31 March 2027',kr2:'Reduce escalations caused by unclear ownership from 50 to 15 per quarter by 31 March 2027',roles:'Executive Team, Department Leads, Operations, HR'};
  return {objective:'Improve reliability of patient-centred service delivery',kr1:'Increase on-time completion of priority patient actions from 65% to 90% by 31 March 2027',kr2:'Reduce repeat patient information requests from 35% to 10% by 31 March 2027',roles:'Operations, Clinical Teams, IT, Customer Support'};
}
function saRenderOkr(){
  saGates();var T=SA_TXT[SA.mode],themes=saThemes();
  saEl('saScreen').innerHTML='<div class="sa-st"><div><div class="sa-st-h">Gate 2: Flight Plan</div><p>'+T.g2+'</p></div>'+
    (SA.mode==='f'?'<button type="button" class="sa-btn gold" onclick="saAuto()">Build Example OKR</button>':'')+'</div>'+
    '<div class="sa-packs">'+themes.map(function(t,i){return '<button type="button" class="sa-pack" onclick="saUseTheme('+i+')"><strong>'+t.type+'</strong><span>'+u3esc(t.text)+'</span></button>';}).join('')+'</div>'+
    '<div class="sa-okr-wrap"><div class="sa-card"><div class="sa-card-h">Convert Selected Theme</div>'+
      '<label class="sa-lbl" for="saObjective">Objective</label><input class="sa-in" id="saObjective" placeholder="Select a KISS theme above">'+
      '<label class="sa-lbl" for="saKr1">Key Result 1</label><input class="sa-in" id="saKr1" placeholder="Generated from selected theme">'+
      '<label class="sa-lbl" for="saKr2">Key Result 2</label><input class="sa-in" id="saKr2" placeholder="Generated from selected theme">'+
      '<label class="sa-lbl" for="saRoles">Contributing Roles</label><input class="sa-in" id="saRoles" placeholder="Generated from selected theme">'+
      '<div id="saOkrMsg" class="sa-msg">'+T.pick+'</div>'+
      '<div style="margin-top:14px"><button type="button" class="sa-btn" onclick="saAddOkr()">Add Flight Plan</button></div></div>'+
    '<div class="sa-card"><div class="sa-card-h">Accepted Flight Plan</div><div id="saOkrList" class="sa-okr-list"></div></div></div>'+
    '<div class="sa-actions"><button type="button" class="sa-btn ghost" onclick="saBack()">Back to Baggage Check</button><button type="button" class="sa-btn" onclick="saFinish()">Finish Learning Round</button></div>';
  saRenderOkrList();
}
function saBack(){SA.state.step=1;saRenderKiss();saChanged();}
function saUseTheme(i){
  var p=saOkrFromTheme(saThemes()[i]);
  saEl('saObjective').value=p.objective;saEl('saKr1').value=p.kr1;saEl('saKr2').value=p.kr2;saEl('saRoles').value=p.roles;
  var msg=saEl('saOkrMsg');msg.className='sa-msg success';
  msg.textContent='Green light: selected KISS theme converted into a draft OKR. Now test whether the Objective is enterprise-level and the Key Results show measurable change.';
}
function saAuto(){
  saEl('saObjective').value='Improve reliability of patient-centred service delivery';
  saEl('saKr1').value='Reduce patient handover delays from 48 hours to 12 hours by 31 March 2027';
  saEl('saKr2').value='Increase patients receiving clear service updates from 50% to 90% by 31 March 2027';
  saEl('saRoles').value='Clinical Teams, Operations, IT, Customer Support, Executive Team';
}
function saKrPasses(t){return /\d/.test(t)&&/from|to|increase|reduce|improve|decrease|raise|lower/i.test(t)&&/by|march|april|may|june|july|august|september|october|november|december|2027|2026/i.test(t);}
function saAddOkr(){
  var objective=saEl('saObjective').value.trim(),kr1=saEl('saKr1').value.trim(),kr2=saEl('saKr2').value.trim(),roles=saEl('saRoles').value.trim(),msg=saEl('saOkrMsg');
  if(!objective||!kr1||!kr2||!roles){msg.className='sa-msg danger';msg.textContent='Not cleared: the flight plan has missing fields.';return;}
  if(!saKrPasses(kr1)||!saKrPasses(kr2)){msg.className='sa-msg danger';msg.textContent='This flight has weak instrument readings. Each KR needs a metric, movement and deadline.';return;}
  if(SA.state.okrs.length>=4){msg.className='sa-msg danger';msg.textContent='Too many destinations. Maximum four objectives.';return;}
  SA.state.okrs.push({objective:objective,kr1:kr1,kr2:kr2,roles:roles});
  ['saObjective','saKr1','saKr2','saRoles'].forEach(function(id){saEl(id).value='';});
  msg.className='sa-msg success';msg.textContent='Flight plan accepted.';saRenderOkrList();saChanged();
}
function saRenderOkrList(){
  var list=saEl('saOkrList');if(!list)return;
  if(!SA.state.okrs.length){list.innerHTML='<p class="sa-hint">No flight plans accepted yet.</p>';return;}
  list.innerHTML=SA.state.okrs.map(function(o,i){return '<div class="sa-okr-item"><strong>'+(i+1)+'. '+u3esc(o.objective)+'</strong><ul><li>'+u3esc(o.kr1)+'</li><li>'+u3esc(o.kr2)+'</li><li><strong>Crew:</strong> '+u3esc(o.roles)+'</li></ul></div>';}).join('');
}
function saFinish(){
  if(SA.state.okrs.length<1){var m=saEl('saOkrMsg');m.className='sa-msg danger';m.textContent='Not cleared: create one OKR flight plan.';return;}
  SA.state.step=3;saRenderDone();saChanged();
}
function saRenderDone(){
  ['saGate1','saGate2'].forEach(function(id){var g=saEl(id);if(!g)return;g.className='sa-gate done';g.querySelector('.sa-status').textContent='Complete';});
  var K=SA.state.kiss,T=SA_TXT[SA.mode];
  saEl('saScreen').innerHTML='<div class="sa-st"><div><div class="sa-st-h">Learning Round Complete</div><p>'+T.done+'</p></div><button type="button" class="sa-btn gold" onclick="saPrint()">Print Summary</button></div>'+
    '<div class="sa-summary"><div class="sa-card"><div class="sa-big">1</div><div class="sa-card-h">KISS Themes Captured</div><ul><li>Keep: '+saLines(K.keep).length+'</li><li>Improve: '+saLines(K.improve).length+'</li><li>Start: '+saLines(K.start).length+'</li><li>Stop: '+saLines(K.stop).length+'</li></ul></div>'+
    '<div class="sa-card"><div class="sa-big">2</div><div class="sa-card-h">OKR Built From One Theme</div><ul>'+SA.state.okrs.map(function(o){return '<li><strong>'+u3esc(o.objective)+'</strong><br>'+u3esc(o.kr1)+'<br>'+u3esc(o.kr2)+'</li>';}).join('')+'</ul></div></div>'+
    '<div class="sa-msg success" style="margin-top:18px">Learning point: KISS is the evidence base for deciding what the Objective should be and what Key Results will prove progress.</div>'+
    (SA.mode==='p'?'<div class="sa-msg" style="margin-top:10px">Your learning round is saved on this page. It reaches your facilitator when you submit the unit.</div>':'')+
    '<div class="sa-actions"><button type="button" class="sa-btn ghost" onclick="saReset()">Start Again</button></div>';
}
function saReset(){
  if(SA.mode==='p'&&(SA.state.okrs.length||saThemes().length)&&!window.confirm('Start the game again? Your saved KISS choices and flight plans will be cleared.'))return;
  SA.state={step:1,kiss:{keep:'',improve:'',start:'',stop:''},okrs:[]};saRenderKiss();saChanged();
}
function saKissText(){return SA_CARDS.map(function(c){var l=saLines(SA.state.kiss[c[0]]);return c[1]+': '+(l.length?l.join('; '):'—');}).join('\n');}
function saPlanText(){return SA.state.okrs.map(function(o,i){return (i+1)+'. Objective: '+o.objective+'\n   Key Result 1: '+o.kr1+'\n   Key Result 2: '+o.kr2+'\n   Contributing roles: '+o.roles;}).join('\n\n');}
function saPrint(){
  var w=window.open('','_blank');if(!w){window.print();return;}
  var body='<h1>Strategy Airport · Learning Round</h1><h2>Success in Practice Statement</h2><p>'+u3esc(SA_SIP)+'</p><h2>Gate 1 · Baggage Check (KISS Mapping)</h2><pre>'+u3esc(saKissText())+'</pre><h2>Gate 2 · Flight Plan (OKR Construction)</h2><pre>'+u3esc(saPlanText())+'</pre>';
  w.document.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Strategy Airport · Learning Round</title><style>body{font-family:Georgia,serif;color:#172033;max-width:760px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:26px}h2{color:#071b4d;font-size:17px;margin-top:22px;border-bottom:1px solid #e5e7eb;padding-bottom:4px}pre{white-space:pre-wrap;font-family:Arial,sans-serif;font-size:13px}</style></head><body>'+body+'</body></html>');
  w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
