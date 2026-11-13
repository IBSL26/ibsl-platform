/* S2R Portal · Section 5 task counts (12 Nov 2026).
   At the top of each Capstone step or part, a box states what the participant completes in it,
   so that no entry is missed. One list per unit page; nothing is saved and no work is changed.
   A step is found by its "How to complete" heading (how), a part by its number (part). */
(function(){
  var B=function(lead,rest){return '<strong>'+lead+'</strong>'+(rest?' '+rest:'');};
  var T={
    lens1:[ // Unit 2
      {how:'How to complete 5.1',t:B('In this step you complete 2 parts:','answer the 14 elements, one question each, against your problem statement; then the scribe brings them together under five headings and your group edits them.')},
      {how:'How to complete 5.2',t:B('In this step you complete 1 entry:','your Strategy Intent Statement, in one or two sentences.')},
      {how:'How to complete 5.3',t:B('In this step you complete 3 parts:','answer the two questions in each of the four domains; write one statement per domain; then write your one Success in Practice statement.')},
      {how:'How to complete the Group record',t:B('In this part you complete 1 task:','read your group record, then select Agree.')}],
    lens2:[ // Unit 3
      {part:'5.1',t:B('In this part you complete 4 domains (16 entries):','for each SiP domain, check its SiP statement, then write one entry each for Keep, Improve, Start and Stop.')},
      {part:'5.2',t:B('In this part you complete the five steps for each of your themes (up to four):','1. the theme; 2. its Objective; 3. its Key Results and contributing roles; 4. the alignment test; 5. its place on the Priority Matrix. Then read your record and select Agree.')}],
    lens3:[ // Unit 4
      {part:'5.1',t:B('This part is a worked example to read.','There is nothing to complete here.')},
      {part:'5.2',t:B('In this part you complete 4 steps for each of your Key Results:','Arena, Boundaries, Competition and Value Proposition. Each step ends with the condition that must remain true.')},
      {part:'5.3',t:B('In this part you complete 2 tasks:','1. for each critical Must-Be-True condition, the accountable executive, the evidence and the date of the first check; 2. your executive blind spot. Then read your record and select Agree.')}],
    lens4:[ // Unit 5
      {how:'How to complete Step 1',t:B('In this step you complete 3 entries:','the Shift, the Stake and the Step.')},
      {how:'How to complete Step 2',t:B('In this step you complete 9 entries:','your two highest-risk dimensions, each with its response (4 entries), and the behaviour you expect from the leadership team under Accountability, Commitment, Engagement, Integrity and Transparency (5 entries). Then select Agree.')}],
    lens5:[ // Unit 6
      {how:'How to complete Activity 1',t:B('In this activity you complete 2 tasks:','1. select your Objective and Key Result; 2. complete the Contribution Map for three or four business functions, filling every entry in each function’s row.')},
      {how:'How to complete Activity 2',t:B('In this activity you complete 5 entries for each business function:','one practical arrangement under each FACES function: Foster, Align, Create, Embed and Support.')},
      {how:'How to complete Activity 3',t:B('In this activity you complete 3 sets of measures, each with a weight:','Strategy, Operational and Behavioural. The weights must add up to 100%.')},
      {how:'How to complete Activity 4',t:B('In this activity you complete 4 entries:','your waypoints (two or three, each with a date and a level), the alert, the recovery for individuals and for the organisational conditions, and the decider. Then select Agree.')}],
    lens6:[ // Unit 7
      {how:'How to complete Step 1',t:B('In this step you choose 2 contributions and complete 4 entries for each (8 in total):','the SiP statement it serves, its owner, the part of that Future it serves, and the leader framing.')},
      {how:'How to complete Step 2',t:B('In this step you complete 9 entries for each contribution (18 in total):','for the people, what must be delivered, by when, to what standard, how success will be recognised and the behaviours expected; for the organisation, Environment, Systems, Resources and Governance.')},
      {how:'How to complete Step 3',t:B('In this step you complete 7 entries for each contribution (14 in total):','the Upline, Downline and Crossline, each with what must be established with them, and the coordination required.')},
      {how:'How to complete Step 4',t:B('In this step you complete up to 4 entries for each contribution:','the alignment score; where it is below 9, what stands behind it, the actions agreed and the revised score.')},
      {how:'How to complete the Alignment Dialogue',t:B('In this part you complete 5 entries:','the Key Result, then your side of the dialogue under Goal, Reality, Options and Will.')}],
    lens7:[ // Unit 8
      {how:'How to complete Consequence 1',t:B('In this step you complete 2 entries:','for individuals, the potential gap and the decision point for recovery; for the organisational conditions, the potential gap and the decision point for recovery.')},
      {how:'How to complete Consequence 2',t:B('In this step you complete 2 entries:','for individuals, the potential gap and the decision point for recovery; for the organisational conditions, the potential gap and the decision point for recovery.')},
      {how:'How to complete Consequence 3',t:B('In this step you complete 2 entries:','for individuals, the potential gap and the decision point for recovery; for the organisational conditions, the potential gap and the decision point for recovery.')},
      {how:'How to complete Consequence 4',t:B('In this step you complete 2 entries:','for individuals, the potential gap and the decision point for recovery; for the organisational conditions, the potential gap and the decision point for recovery.')},
      {how:'How to complete part 5.2',t:B('In this part you complete 4 entries:','the red flag, what explains the gap for individuals, what explains it for the organisational conditions, and the recovery. Then select Agree.')}],
    lens8:[ // Unit 9
      {part:'5.1',t:B('In this part you complete 2 entries:','the challenge you select from your Problem Charter, and its strategic connection.')},
      {part:'5.2',t:B('In this part you complete 2 entries:','the clog you select, and the reason for your selection.')},
      {part:'5.3',t:B('In this part you complete 2 entries:','the lever you select, and the reason for your selection.')},
      {part:'5.4',t:B('In this part you complete 15 entries:','4 for REVIEW, 6 for REALIGN and 5 for RESTORE.')},
      {part:'5.5',t:B('In this part you complete 1 task:','check your work against the four quality checks, and correct any entry that falls short.')},
      {part:'5.6',t:B('In this part you complete 1 task:','read your group’s record, then select Agree.')}],
    lens9:[ // Unit 10
      {part:'5.1',t:B('In this part you complete 1 entry:','any missing submissions or evidence gaps.')},
      {part:'5.2',t:B('In this part you complete 12 entries:','for each of Environment, Systems, Resources and Governance, one finding at each level: Functional (Convergence), Cross-functional (Divergence) and Enterprise (Dependency).')},
      {part:'5.3',t:B('In this part you complete one row for each response your group agrees:','the ESRG domain, execution capability, component, collective finding, strategic commitment affected, the response and the functions involved.')},
      {part:'5.4',t:B('In this part you complete one row for each response from 5.3:','the implementation actions, accountable executive, contributing functions, target date and evidence of improvement. Then select Agree.')}],
    lens10:[ // Unit 11
      {part:'5.1',t:B('Section 5 has 8 tasks across parts 5.2 to 5.8.','Each part below states what you complete in it.')},
      {part:'5.2',t:B('In this part you complete Task 1 for each function your group ticked:','tick your CXO roles, then write each function’s interpretation of its health position in its card.')},
      {part:'5.3',t:B('In this part you complete Task 2 for each function,','in the same function card in part 5.2.')},
      {part:'5.4',t:B('In this part you complete 2 entries:','the functions contributing most to the weaknesses, and the vulnerabilities requiring cross-functional leadership attention.')},
      {part:'5.5',t:B('In this part you complete 4 entries:','the overlaps flagged, the most vulnerable functions, the priority cultural vulnerabilities and the priority people-performance concerns.')},
      {part:'5.6',t:B('In this part you complete 3 entries:','the prioritised diagnosis, the cultural reinforcement actions with named executive accountability, and the measurable commitments.')},
      {part:'5.7',t:B('In this part you complete 1 response row','for your lowest-scoring health trait, and a further row only for a further priority.')},
      {part:'5.8',t:B('In this part you complete 3 steps:','1. three to six values, each with its meaning; 2. at least three values translated into norms; 3. your strongest norm tested against the three tests.')},
      {part:'5.9',t:B('In this part you complete 1 task:','read your group’s record, then select Agree.')}],
    lens11:[ // Unit 12
      {part:'5.1',t:B('Section 5 has 3 parts to complete: 5.2, 5.3 and 5.4.','Each part below states what you complete in it.')},
      {part:'5.2',t:B('In this part you complete 13 entries:','the quarter, the Key Result, your WARD, the four ESRG capabilities, the consolidated health score and the two weakest traits. Select Bring in to fill those that come from Units 6, 10 and 11, then check each one.')},
      {part:'5.3',t:B('In this part you complete 3 lines of sight (13 entries):','the strategic, operational and behavioural lines, each with its result, alert, recovery, owner and check date.')},
      {part:'5.4',t:B('In this part you complete at least 4 decisions:','one Keep, one Improve, one Stop and one Start, each with its line of sight and owner.')},
      {part:'5.5',t:B('In this part you complete 1 task:','read your group’s record, then select Agree.')}]
  };
  /* 12 Nov 2026: the Section 5 layout also runs on facilitator pages (no task boxes there). */
  var m=/lens(\d+)_([pf])/i.exec(location.pathname||'');if(!m)return;
  var isF=/f/i.test(m[2]);
  var L=isF?[]:T['lens'+m[1]];if(!L)return;
  function box(html){var d=document.createElement('div');d.className='s2r-task';d.innerHTML=html;return d;}
  function norm(s){return String(s||'').replace(/\s+/g,' ').trim();}

  /* Section 5 layout (13 Nov 2026): the Capstone work, then the Unit Summary, then the Key Reflection,
     then the Closing Insight and Transition, then feedback. Loose guidance boxes and the reflection are
     placed in collapsible sections; the Capstone parts start closed. Elements are moved, never rebuilt,
     so their saved work and handlers are kept. */
  function accWrap(title,meta,nodes){
    var a=document.createElement('div');a.className='acc s2r-wrap';
    a.innerHTML='<div class="acc-h" onclick="this.parentElement.classList.toggle(\'open\')"><span class="acc-t"></span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta"></span><div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div></div><div class="acc-b cb"></div>';
    a.querySelector('.acc-t').textContent=title;a.querySelector('.acc-meta').textContent=meta||'';
    var b=a.querySelector('.acc-b');nodes.forEach(function(n){b.appendChild(n);});return a;}
  function layout(){
    var lab=[].slice.call(document.querySelectorAll('.mod-hero-label,.mod-badge')).filter(function(e){return /^Section 5 · Application/.test(norm(e.textContent));})[0];
    var P=lab&&lab.closest('.mod-panel,.mod,[id^="mod"]');if(!P||P.getAttribute('data-s2r-layout'))return;
    var body=P.querySelector('.mod-body')||P;P.setAttribute('data-s2r-layout','1');
    var kids=[].slice.call(body.children),top=[],ref=[],cap=[],sum=[],close=[],tail=[];
    kids.forEach(function(c){
      var cls=' '+(c.className||'')+' ',id=c.id||'',tx=norm(c.textContent),at=c.querySelector(':scope > .acc-h .acc-t, :scope > .acc-h');
      var t=at?norm(at.textContent):'';
      if(/ (slo-box|lo-box) /.test(cls))top.push(c);
      else if(/ s2r-kr-acc /.test(cls))ref.push(c);
      else if(/ s2r-close-acc /.test(cls))close.push(c);
      else if(/ s2r-key-ref /.test(cls))ref.push(c);
      else if(/ acc /.test(cls)&&t.indexOf('Unit Summary')===0)sum.push(c);
      else if(/ s2r-cr /.test(cls)||(/ hbox /.test(cls)&&/^(Section Closing Insight|Transition to)/.test(tx)))close.push(c);
      else if(/^(feedback-acc|msg-acc|upload-acc)$/.test(id)||/ mod-nav /.test(cls)||(/Submit to Facilitator/.test(tx)&&tx.length<60))tail.push(c);
      else cap.push(c);
    });
    var keep=function(c){var cls=' '+(c.className||'')+' ',id=c.id||'';return c.hasAttribute('data-s2r-keep')||/ acc /.test(cls)||/twbar/i.test(id)||/ step-tabs | step-panel /.test(cls)||/Rec$/.test(id)||/S5$/.test(id)||c.tagName==='SCRIPT';};
    var capOut=[],grp=[];
    var flush=function(){if(!grp.length)return;var tx=norm(grp.map(function(g){return g.textContent;}).join(' '));
      var title=/How Section 5 works/.test(tx)?'How the Capstone project works':/FACILITATOR (GUIDANCE|GUIDE)|PARTICIPANT ACTIVITY|Facilitator Frame/i.test(tx)?'Facilitator guidance':/Capstone Portfolio Output/.test(tx)?'Capstone Portfolio Output':/Application outputs/.test(tx)?'Application outputs':'Capstone guidance';
      capOut.push(accWrap(title,'Capstone work',grp));grp=[];};
    cap.forEach(function(c){if(keep(c)){flush();if(/ acc /.test(' '+c.className+' '))c.classList.remove('open');capOut.push(c);}else grp.push(c);});flush();
    /* The group record bar leads the Capstone, above the guidance (12 Nov 2026). */
    var bars=capOut.filter(function(c){return /twbar/i.test(c.id||'')||c.id==='u2bTeam';});
    var how=capOut.filter(function(c){var t=c.querySelector(':scope > .acc-h .acc-t');return t&&t.textContent==='How the Capstone project works';});
    capOut=bars.concat(how,capOut.filter(function(c){return bars.indexOf(c)<0&&how.indexOf(c)<0;}));
    var capAcc=capOut.length?accWrap('Capstone','Capstone work',capOut):null;if(capAcc)capAcc.classList.add('s2r-cap');
    var one=function(a,k){return a.length===1&&(' '+a[0].className+' ').indexOf(' '+k+' ')>=0;};
    /* 13 Nov 2026: the Key Reflection closes each section, just before the Closing Insight. */
    var order=top.concat(capAcc?[capAcc]:[],sum,ref.length?[one(ref,'s2r-kr-acc')?ref[0]:accWrap('Key Reflection','Section 5',ref)]:[],close.length?[one(close,'s2r-close-acc')?close[0]:accWrap('Closing Insight & Transition','Unit close',close)]:[],tail);
    order.forEach(function(n){body.appendChild(n);});
  }
  function run(){
    try{layout();}catch(e){console.warn('[s2r-tasks] layout',e);}
    if(!document.getElementById('s2rTaskCss')){var st=document.createElement('style');st.id='s2rTaskCss';
      st.textContent='.s2r-cap .acc:not(.open)>.acc-b{display:none!important;}.s2r-cap .acc:not(.open)>.acc-h .arr{transform:none!important;}.s2r-task{border:1px solid rgba(201,168,76,.35);background:rgba(201,168,76,.06);border-radius:3px;padding:9px 12px;margin:0 0 14px;font-size:12.5px;line-height:1.6;color:rgba(255,255,255,.85);}.s2r-task strong{color:#c9a84c;}@media print{.s2r-task{display:none!important;}}';
      document.head.appendChild(st);}
    L.forEach(function(it,k){
      if(document.querySelector('[data-s2r-task="'+k+'"]'))return;
      var at=null,where='before';
      if(it.how){
        var hs=document.querySelectorAll('[class*="how-h"]');
        for(var i=0;i<hs.length;i++){var tx=norm(hs[i].textContent);if(tx.indexOf('Capstone work')===0&&tx.indexOf(it.how)>=0){at=hs[i].parentElement;break;}}
      }else if(it.part){
        var ts=document.querySelectorAll('.acc-t');
        for(var j=0;j<ts.length;j++){if(norm(ts[j].textContent).indexOf(it.part+' ')===0){var a=ts[j].closest('.acc');at=a&&a.querySelector('.acc-b');where='top';break;}}
      }
      if(!at)return;
      var b=box(it.t);b.setAttribute('data-s2r-task',k);
      if(where==='top'){var c=at.querySelector(':scope > .cb')||at;c.insertBefore(b,c.firstChild);}
      else at.parentNode.insertBefore(b,at);
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){run();setTimeout(run,1500);});
  else{run();setTimeout(run,1500);}
})();
