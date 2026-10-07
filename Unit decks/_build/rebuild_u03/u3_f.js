// ── UNIT 3 · FACILITATOR PAGE (preparation only: nothing is entered or saved) ───────────────────
var SUMMARY=[
  {arc:'Awareness — What',title:'The KISS Framework as Reflective Filter',body:'Leaders recognise that KISS (Keep, Improve, Start, Stop) functions as a reflective filter between strategic vision and execution commitments. Before defining Objectives and Key Results, the leadership team must examine the organisation\'s current operating reality in relation to its Success in Practice. This step prevents the common strategic mistake of layering new ambitions on top of an unchanged operational system. Six steps then carry the KISS output into enterprise OKRs.'},
  {arc:'Intelligence — Why',title:'Most OKR Failures are Reflection Failures',body:'When organisations move directly from vision to targets, legacy routines remain in place, resources remain misaligned, and teams attempt to pursue transformational goals while still carrying the weight of outdated priorities. The KISS-to-OKR sequence resolves this tension: SiP defines the future, KISS identifies the changes required, and OKRs translate those changes into measurable progress. The worked example shows the full sequence in practice.'},
  {arc:'Extrapolating — Where',title:'Functional Bias Creates OKR Hot Zones',body:'Each leader naturally emphasises different SiP domains. Unexamined, these perspectives produce functional OKRs where enterprise OKRs are needed. Participants match each leadership role to its typical hot zone and its alignment question. Recognising these patterns allows the leadership team to integrate perspectives into a balanced execution system that reflects the full enterprise.'},
  {arc:'Integration — Collective',title:'Individual Expertise into Collective Intelligence',body:'Each group translates its Success in Practice into a confirmed KISS map across the four SiP domains, then into enterprise priorities and enterprise OKRs through the six steps. Each leader begins with insights from a functional domain, and the final outcome reflects the success of the enterprise as a whole. The Prioritisation Matrix concentrates execution energy on the priorities that will most accelerate progress toward the SiP. The confirmed outputs feed the team\'s Capstone Blueprint.'},
  {arc:'Application — In Practice',title:'From Strategic Imagination to Operational Clearance',body:'In Strategy Airport each participant applies the same translation alone to a new case: what the company must keep, improve, start and stop, then one KISS theme converted into an Objective and two Key Results with contributing roles. KISS is the evidence base for deciding what the Objective should be and what Key Results will prove progress.'}
];
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

