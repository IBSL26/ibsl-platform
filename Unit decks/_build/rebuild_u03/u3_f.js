// ── UNIT 3 · FACILITATOR PAGE (preparation only: nothing is entered or saved) ───────────────────
var SUMMARY=[
  {arc:'Awareness — What',title:'The KISS Framework as Reflective Filter',body:'Leaders recognise that KISS (Keep, Improve, Start, Stop) functions as a reflective filter between strategic vision and execution commitments. Before defining Objectives and Key Results, the leadership team must examine the organisation\'s current operating reality in relation to its Success in Practice. This step prevents the common strategic mistake of layering new ambitions on top of an unchanged operational system. Six steps then carry the KISS output into enterprise OKRs.'},
  {arc:'Intelligence — Why',title:'Most OKR Failures are Reflection Failures',body:'When organisations move directly from vision to targets, legacy routines remain in place, resources remain misaligned, and teams attempt to pursue transformational goals while still carrying the weight of outdated priorities. The KISS-to-OKR sequence resolves this tension: SiP defines the future, KISS identifies the changes required, and OKRs translate those changes into measurable progress. The worked example shows the full sequence in practice, and each participant then takes the same case through the six steps as individual work.'},
  {arc:'Extrapolating — Where',title:'Functional Bias Creates OKR Hot Zones',body:'Each leader naturally emphasises different SiP domains. Unexamined, these perspectives produce functional OKRs where enterprise OKRs are needed. Participants match each leadership role to its typical hot zone and its alignment question. Recognising these patterns allows the leadership team to integrate perspectives into a balanced execution system that reflects the full enterprise.'},
  {arc:'Integration — Collective',title:'Individual Expertise into Collective Intelligence',body:'Each group translates its Success in Practice into a confirmed KISS map across the four SiP domains, then into enterprise priorities and enterprise OKRs through the six steps. Each leader begins with insights from a functional domain, and the final outcome reflects the success of the enterprise as a whole. The Prioritisation Matrix concentrates execution energy on the priorities that will most accelerate progress toward the SiP. The confirmed outputs feed the team\'s Capstone Blueprint.'},
  {arc:'Application — In Practice',title:'From Strategic Imagination to Operational Clearance',body:'In Strategy Airport each participant applies the same translation alone to a new case: what the company must keep, improve, start and stop, then one KISS theme converted into an Objective and two Key Results with contributing roles. KISS is the evidence base for deciding what the Objective should be and what Key Results will prove progress.'}
];
// ── 2.2 · WORKED EXAMPLE: the case of u3_shared.js taken through the six steps (facilitator file only) ──
// Each step uses what the step before it produced: five themes, five Objectives, five OKRs, five pass the
// alignment test (one further draft is returned), the vote selects four (one is released), four are placed on the matrix.
var WORKED_MODEL={
  items:[
    {theme:'Customer responsiveness',shift:'Deliver faster and more reliable customer responsiveness.',obj:'Deliver consistently fast and effortless service experiences for customers',
     krs:['Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027','Increase customer requests resolved at first contact from 60% to 85% by 30 September 2027'],
     roles:'Commercial, Operations, Customer Service, Technology',votes:7,pri:true,impact:'High',effort:'Medium'},
    {theme:'Execution speed',shift:'Strengthen cross-functional execution speed.',obj:'Build a high-speed execution engine that moves quickly from insight to action',
     krs:['Reduce cross-functional decision time from 5 days to 1 day by 30 June 2027','Reduce recurring management reports from 24 to 10 by 31 March 2027'],
     roles:'Operations, Finance, Strategy',votes:6,pri:true,impact:'High',effort:'Low'},
    {theme:'Collaboration culture',shift:'Build enterprise-wide ownership of strategic priorities.',obj:'Create a culture of shared ownership across functions for strategic priorities',
     krs:['Increase enterprise priorities with a named cross-functional owner from 40% to 100% by 31 March 2027','Reduce issues escalated to the executive team from 30 to 10 per quarter by 30 September 2027'],
     roles:'People & Culture, all functional heads',votes:4,pri:true,impact:'High',effort:'High'},
    {theme:'Value creation',shift:'Improve operational efficiency to strengthen value creation.',obj:'Strengthen enterprise performance through scalable and efficient operations',
     krs:['Improve operating margin from 14% to 18% by 31 December 2027','Reduce leadership time spent on low-value projects from 25% to 10% by 30 June 2027'],
     roles:'Finance, Operations, Commercial',votes:3,pri:true,impact:'Medium',effort:'High'},
    {theme:'Key account growth',shift:'Deepen the relationships with the key accounts that anchor revenue.',obj:'Become the partner our key accounts turn to for every new requirement',
     krs:['Increase key accounts using three or more service lines from 8 to 14 by 30 September 2027','Increase revenue from key accounts from 45% to 55% of total revenue by 31 December 2027'],
     roles:'Commercial, Customer Service, Finance',votes:1,pri:false,impact:'',effort:''}
  ],
  test:[
    ['Does this truly get the organisation closer to the shared SiP vision?','Yes. Fast, consistent and effortless service is the first line of the SiP statement.'],
    ['Would fellow leaders see this as a win for the whole organisation — or just for one function?','The whole organisation. It needs Commercial, Operations, Customer Service and Technology, and no single function can deliver it alone.'],
    ['Does it visibly improve culture, operations, or value creation?','Yes. Handovers improve in operations, and client retention strengthens value creation.'],
    ['Is there clear accountability for delivering this outcome?','Yes. One executive owns the Objective and the contributing roles are named for each Key Result.']
  ],
  failed:{draft:'Launch the new CRM platform by June',score:1,why:'It can be checked off a list, so it is a task, and it serves one function.'},
  voters:7,votesEach:3,
  tradeoff:'Objective 5 passed the alignment test and is released for this cycle. Key accounts are a strength the organisation already holds: they appear under KEEP and stay protected through current account management. Their growth depends on the faster and more reliable service that Objectives 1 and 2 build. The team returns to Objective 5 in its next planning cycle.',
  signal:'execution speed moves first, customer responsiveness follows, shared ownership is the long transformation, and the investment in scalable operations is timed with care.'
};
var curHZ=null;

// ── RENDER ────────────────────────────────────────────────────────────────────
function renderKissGuide(){
  var a=document.getElementById('kissGuideList');if(a)a.innerHTML=kissGuideHtml('kgd_','u3ToggleDomain');
  var b=document.getElementById('kissPrepList');if(b)b.innerHTML=kissGuideHtml('kgq_','u3ToggleDomain');
}

function renderHotZones(){
  document.getElementById('hzGrid').innerHTML=HOT_ZONES.map(function(h,i){
    return '<div class="hz-card" id="hz_'+i+'" onclick="showHZ('+i+')">'+
      '<div class="hz-top"><div class="hz-role">'+h.role+'</div><div class="hz-title">'+h.title+'</div></div>'+
      '<div class="hz-bar"></div>'+
    '</div>';
  }).join('');
}

function showHZ(i){
  var h=HOT_ZONES[i];
  document.querySelectorAll('.hz-card').forEach(function(c,x){c.classList.toggle('active',x===i);});
  var d=document.getElementById('hzDetail');
  if(curHZ===i){d.className='hz-detail';d.innerHTML='';curHZ=null;return;}
  curHZ=i;
  d.className='hz-detail visible';
  d.innerHTML='<div class="hz-col"><h5>Dominant Future Realities</h5><p>'+h.top2+'</p><h5 style="margin-top:14px;">Natural OKR Emphasis</h5><p>'+h.emphasis+'</p></div>'+
    '<div class="hz-col"><h5>Alignment Question</h5><div class="hz-align">'+h.align+'</div><h5 style="margin-top:12px;">Typical Hot Zone</h5><div class="hz-hot">'+h.hot+'</div></div>';
}

function renderSummary(){
  document.getElementById('summaryList').innerHTML=SUMMARY.map(function(s,i){
    return '<div class="sum-block" id="sum_'+i+'">'+
      '<div class="sum-h" onclick="tSum('+i+')">'+
        '<span class="sum-arc">'+s.arc+'</span>'+
        '<span class="sum-title">'+s.title+'</span>'+
        '<span class="sum-arr">▾</span>'+
      '</div>'+
      '<div class="sum-body"><p>'+s.body+'</p></div>'+
    '</div>';
  }).join('');
}

function renderWorked(hostId){
  var host=document.getElementById(hostId);if(!host)return;
  var M=WORKED_MODEL,N=M.items.length,pri=M.items.filter(function(o){return o.pri;});
  var word=['','one','two','three','four','five','six','seven'];
  var tabs=['Find Themes','Inspiring Objectives','Define Key Results','Alignment Test','Enterprise Priority','Priority Matrix'].map(function(n,i){
    return '<div class="step-tab'+(i===0?' active':'')+'" onclick="u3Tab(\'wx\','+i+')"><div class="step-num">Step '+(i+1)+'</div><div class="step-name">'+n+'</div></div>';
  }).join('');
  var row3=function(a,b,c,cls){return '<div class="u3-wx-res'+(cls?' '+cls:'')+'"><div class="u3-wx-l">'+a+'</div><div class="u3-wx-n">'+b+'</div><div class="u3-wx-r">'+c+'</div></div>';};
  var s1='<p>Reading across the four domains of the KISS table, the leadership team finds '+word[N]+' patterns that keep appearing. Each becomes a strategic theme:</p>'+
    M.items.map(function(o,i){return '<div class="u3-wx-line"><div class="u3-wx-l">'+(i+1)+' · '+u3esc(o.theme)+'</div><div class="u3-wx-r">'+u3esc(o.shift)+'</div></div>';}).join('');
  var s2='<p>Each theme from Step 1 is translated into a bold, qualitative statement that starts with a verb and describes the transformation:</p>'+
    M.items.map(function(o,i){return '<div class="u3-wx-line"><div class="u3-wx-l">'+u3esc(o.theme)+'</div><div class="u3-wx-r"><strong>Objective '+(i+1)+':</strong> '+u3esc(o.obj)+'</div></div>';}).join('');
  var s3='<p>Each Objective from Step 2 receives two Key Results in the form Verb + Metric + From X to Y + Deadline, with the contributing roles named:</p>'+
    M.items.map(function(o,i){return '<div class="u3-wx-okr"><div class="u3-wx-okr-h">Objective '+(i+1)+' · '+u3esc(o.obj)+'</div><ul>'+o.krs.map(function(k){return '<li>'+u3esc(k)+'</li>';}).join('')+'</ul><div class="u3-wx-roles"><strong>Contributing roles:</strong> '+u3esc(o.roles)+'</div></div>';}).join('');
  var s4='<p>Before the OKRs of Step 3 go forward, each one is tested against the four questions. Objective 1 is shown in full:</p>'+
    M.test.map(function(t){return '<div class="u3-wx-line"><div class="u3-wx-l">'+u3esc(t[0])+'</div><div class="u3-wx-r">'+u3esc(t[1])+'</div></div>';}).join('')+
    '<h5 class="u3-gq" style="margin-top:18px;">Result of the alignment test</h5>'+
    M.items.map(function(o,i){return row3('Objective '+(i+1)+' · '+u3esc(o.theme),'4 of 4','Goes forward to Step 5');}).join('')+
    row3('Draft from one function · "'+u3esc(M.failed.draft)+'"',M.failed.score+' of 4','Returned to Step 2. '+u3esc(M.failed.why),'out')+
    '<div class="hbox teal"><p><strong>Output of Step 4:</strong> '+word[N]+' OKRs pass the alignment test and go forward to Step 5.</p></div>';
  var s5='<p>'+word[N].charAt(0).toUpperCase()+word[N].slice(1)+' OKRs passed the alignment test in Step 4. The Less is More Rule allows no more than 4 Enterprise Objectives, so the leadership team must decide which four deserve enterprise focus now.</p>'+
    '<p><strong>The vote:</strong> each of the '+word[M.voters]+' members of the leadership team votes for the '+word[M.votesEach]+' Objectives that represent the most critical strategic movements at this moment.</p>'+
    M.items.map(function(o,i){return row3('Objective '+(i+1)+' · '+u3esc(o.theme),o.votes+(o.votes===1?' vote':' votes'),o.pri?'Enterprise priority':'Released for this cycle',o.pri?'in':'out');}).join('')+
    '<div class="hbox"><p><strong>The trade-off:</strong> '+u3esc(M.tradeoff)+'</p></div>'+
    '<div class="hbox teal"><p><strong>Less is More check:</strong> '+pri.length+' Enterprise Objectives (maximum 4) · 2 Key Results for each Objective (maximum 3). <strong>Output of Step 5:</strong> the '+word[pri.length]+' enterprise priorities go forward to Step 6.</p></div>';
  var grid='<div class="u3-mx"><div class="u3-mx-corner">Impact ↓ &nbsp; Effort →</div><div class="u3-mx-ax">Low effort</div><div class="u3-mx-ax">Medium effort</div><div class="u3-mx-ax">High effort</div>'+
    ['High','Medium','Low'].map(function(im){
      return '<div class="u3-mx-ax u3-mx-row">'+im+' impact</div>'+['Low','Medium','High'].map(function(ef){
        var c=pmFind(im,ef),here=[];M.items.forEach(function(o,i){if(o.pri&&o.impact===im&&o.effort===ef)here.push('<span class="u3-mx-tag">Objective '+(i+1)+' · '+u3esc(o.theme)+'</span>');});
        return '<div class="u3-mx-cell" style="border-color:'+c.c+';"><div class="u3-mx-name" style="color:'+c.c+';">'+c.l+'</div>'+here.join('')+'</div>';
      }).join('');
    }).join('')+'</div>';
  var s6='<p>The '+word[pri.length]+' enterprise priorities confirmed in Step 5 are placed on the Prioritisation Matrix by Impact and Effort:</p>'+grid+
    '<div class="hbox teal"><p><strong>The execution signal:</strong> '+u3esc(M.signal)+'</p></div>';
  var panels=[s1,s2,s3,s4,s5,s6].map(function(h,i){return '<div id="wx_'+i+'" class="step-panel'+(i===0?' active':'')+'">'+h+'</div>';}).join('');
  host.innerHTML='<h4>From KISS to OKRs: the six steps</h4><div class="step-tabs" id="wxTabs">'+tabs+'</div>'+panels;
}
