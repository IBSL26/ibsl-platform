/* S2R Portal · Section 5 task counts (12 Nov 2026).
   At the top of each Capstone step or part, a box states what the participant completes in it,
   so that no entry is missed. One list per unit page; nothing is saved and no work is changed.
   A step is found by its "How to complete" heading (how), a part by its number (part). */
(function(){
  var B=function(lead,rest){return '<strong>'+lead+'</strong>'+(rest?' '+rest:'');};
  var T={
    lens1:[ // Unit 2
      {how:'How to complete Step 1',t:B('In this step you complete your strategy period and the 14 elements.','For each element, answer its questions, then write what the element is saying. The scribe then brings the 14 elements together and your group reads the Architecture as one system.')},
      {how:'How to complete Step 2',t:B('In this step you complete 1 entry:','your Strategy Intent Statement.')},
      {how:'How to complete Step 3',t:B('In this step you complete 5 statements:','for each of the four SiP domains, answer its three questions and write its SiP statement; then write your one Success in Practice statement.')},
      {how:'How to complete the Group record',t:B('In this step you complete 1 task:','read your group record, then select Agree.')}],
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
  var m=/lens(\d+)_p/i.exec(location.pathname||'');if(!m)return;
  var L=T['lens'+m[1]];if(!L)return;
  function box(html){var d=document.createElement('div');d.className='s2r-task';d.innerHTML=html;return d;}
  function norm(s){return String(s||'').replace(/\s+/g,' ').trim();}
  function run(){
    if(!document.getElementById('s2rTaskCss')){var st=document.createElement('style');st.id='s2rTaskCss';
      st.textContent='.s2r-task{border:1px solid rgba(201,168,76,.35);background:rgba(201,168,76,.06);border-radius:3px;padding:9px 12px;margin:0 0 14px;font-size:12.5px;line-height:1.6;color:rgba(255,255,255,.85);}.s2r-task strong{color:#c9a84c;}@media print{.s2r-task{display:none!important;}}';
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
