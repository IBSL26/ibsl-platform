
/* ════════════ UNIT 4 REBUILD (October 2026) · PARTICIPANT TOOLS ════════════
   2.2 Industry Illusion game (portfolio work) · 4.2 Stress-Testing Your Key Results (Capstone work) · Section 5 game saved to the portfolio.
   U4D (the game data and the four checkpoints) is written into the page by build_p.py from u4_content.py. */
var U4_LENS='u2m1_lens3',U3_LENS='u2m1_lens2';
var U4={conf:[],ready:false};
function u4el(id){return document.getElementById(id);}
function u4esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u4plain(s){var d=document.createElement('div');d.innerHTML=s;return d.textContent;}
function u4msg(id,text,cls){var m=u4el(id);if(!m)return;m.textContent=text||'';m.className='u4-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u4save(k,val){
  if(!window.S2R){console.warn('[unit2_m1_lens3_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U4_LENS,k,val);}catch(e){console.error('[unit2_m1_lens3_p] save failed for '+k,e);return false;}
}
function u4isConf(name){return U4.conf.indexOf(name)>=0;}
async function u4setConf(names,on){
  var changed=false;
  names.forEach(function(name){var i=U4.conf.indexOf(name);if(on&&i<0){U4.conf.push(name);changed=true;}else if(!on&&i>=0){U4.conf.splice(i,1);changed=true;}});
  if(changed)await u4save('confirmed_items',U4.conf);
}

/* ── 2.2 · THE INDUSTRY ILLUSION GAME ─────────────────────────────────────────────────────────── */
var II={stage:0,r1:[],l1:false,r2:[],why2:'',l2:false,r3:'',why3:'',l3:false,rev:false,fn:'',em:'',so:'',fin:''};
var II_STAGES=[['Round 1','Where would you look?'],['Round 2','What deserves attention?'],['Round 3','Should we be worried?'],['The Reveal','Your decisions'],['Arena','Apply Arena']];
var II_INSIDE=['A','B','C','D'],II_OUTSIDE_SIGNALS=[2,3,5];
function iiLoad(s){
  if(!s||typeof s!=='object')return;
  var G=U4D.game,ids=G.sources.map(function(x){return x[0];});
  II.r1=(Array.isArray(s.r1)?s.r1:[]).filter(function(x){return ids.indexOf(x)>=0;}).slice(0,4);
  II.r2=(Array.isArray(s.r2)?s.r2:[]).filter(function(x){return x>=0&&x<G.signals.length;}).slice(0,3);
  II.r3=(['A','B','C'].indexOf(s.r3)>=0)?s.r3:'';
  ['why2','why3','fn','em','so','fin'].forEach(function(k){II[k]=String(s[k]||'');});
  II.l1=!!s.l1&&II.r1.length===4;II.l2=II.l1&&!!s.l2&&II.r2.length===3;II.l3=II.l2&&!!s.l3&&!!II.r3;II.rev=II.l3&&!!s.rev;
  II.stage=iiOpen(s.stage)?s.stage:(II.rev?4:II.l3?3:II.l2?2:II.l1?1:0);
}
function iiOpen(i){return i===0||(i===1&&II.l1)||(i===2&&II.l2)||(i===3&&II.l3)||(i===4&&II.rev);}
function iiDone(i){return i===0?II.l1:i===1?II.l2:i===2?II.l3:i===3?II.rev:iiArenaDone();}
function iiArenaDone(){return !!(II.fn.trim()&&II.em.trim()&&II.so.trim()&&II.fin.trim());}
function iiComplete(){return II.l1&&II.l2&&II.l3&&II.rev&&iiArenaDone();}
function iiSrc(id){var x=U4D.game.sources.filter(function(s){return s[0]===id;})[0];return x?x[1]:'';}
function iiLeft1(){return U4D.game.sources.map(function(s){return s[0];}).filter(function(id){return II.r1.indexOf(id)<0;});}
function iiLeft2(){return U4D.game.signals.map(function(_,i){return i;}).filter(function(i){return II.r2.indexOf(i)<0;});}
function iiStageNav(){
  return '<div class="u4-stages">'+II_STAGES.map(function(s,i){
    var open=iiOpen(i);
    return '<div class="u4-stage'+(i===II.stage?' active':'')+(iiDone(i)?' done':'')+(open?'':' locked')+'" onclick="iiGo('+i+')"><small>'+s[0]+'</small>'+s[1]+'</div>';
  }).join('')+'</div>';
}
function iiLockedLine(n){return '<div class="u4-lockline">&#10003; Round '+n+' locked</div>';}
function iiNext(i,label){return '<div class="u4-btnrow"><button type="button" class="u4-b ok" onclick="iiGo('+i+')">'+label+' &rarr;</button></div>';}
function iiPanel(){
  var G=U4D.game,h='';
  if(II.stage===0){
    h='<h5>Round 1 &middot; '+G.r1_title+'</h5><p class="u4-say">&ldquo;'+G.r1_prompt+'&rdquo;</p><p class="u4-do">'+G.r1_do+'</p>'+
      '<div class="u4-opts">'+G.sources.map(function(s){
        var on=II.r1.indexOf(s[0])>=0,dis=II.l1||(!on&&II.r1.length>=4);
        return '<button type="button" class="u4-opt'+(on?' on':'')+'"'+(dis?' disabled':'')+' onclick="iiPick1(\''+s[0]+'\')"><b>'+s[0]+'</b><span>'+s[1]+'</span></button>';
      }).join('')+'</div>'+
      (II.l1?iiLockedLine(1)+iiNext(1,'Go to Round 2'):
        '<div class="u4-count">Selected <b>'+II.r1.length+' of 4</b></div><div class="u4-btnrow"><button type="button" class="u4-b ok"'+(II.r1.length===4?'':' disabled')+' onclick="iiLock(1)">Lock Round 1</button></div>');
  }else if(II.stage===1){
    var left=iiLeft2();
    h='<h5>Round 2 &middot; '+G.r2_title+'</h5><p class="u4-say">&ldquo;'+G.r2_prompt+'&rdquo;</p><p class="u4-do">'+G.r2_q1+'</p>'+
      '<div class="u4-opts one">'+G.signals.map(function(s,i){
        var on=II.r2.indexOf(i)>=0,dis=II.l2||(!on&&II.r2.length>=3);
        return '<button type="button" class="u4-opt'+(on?' on':'')+'"'+(dis?' disabled':'')+' onclick="iiPick2('+i+')"><b>'+(i+1)+'</b><span><em>Signal '+(i+1)+(on?' &middot; investigate':'')+'</em>'+s+'</span></button>';
      }).join('')+'</div>'+
      (II.l2?'':'<div class="u4-count">Selected for investigation <b>'+II.r2.length+' of 3</b></div>')+
      '<p class="u4-do">'+G.r2_q2+'</p>'+
      (II.r2.length===3?'<div class="u4-rev-you">The three you have not selected are deprioritised:<ul>'+left.map(function(i){return '<li>Signal '+(i+1)+': '+G.signals[i]+'</li>';}).join('')+'</ul></div>':
        '<div class="u4-locked">The three signals you leave unselected are deprioritised. Select three for investigation first.</div>')+
      '<label class="u4-lbl" for="ii_why2">Why did you deprioritise these three?</label>'+
      '<textarea class="u4-ta" id="ii_why2" placeholder="Your reasons..."'+(II.l2?' disabled':'')+' oninput="iiText(\'why2\',this.value)">'+u4esc(II.why2)+'</textarea>'+
      (II.l2?iiLockedLine(2)+iiNext(2,'Go to Round 3'):'<div class="u4-btnrow"><button type="button" class="u4-b ok" id="ii_lock2"'+(iiCan2()?'':' disabled')+' onclick="iiLock(2)">Lock Round 2</button></div>');
  }else if(II.stage===2){
    h='<h5>Round 3 &middot; '+G.r3_title+'</h5>'+U4D.reportHtml+'<p class="u4-say">&ldquo;'+G.r3_prompt+'&rdquo;</p><p class="u4-do">Select one and defend it.</p>'+
      '<div class="u4-opts one">'+G.choices.map(function(c){
        var on=II.r3===c[0];
        return '<button type="button" class="u4-opt'+(on?' on':'')+'"'+(II.l3?' disabled':'')+' onclick="iiPick3(\''+c[0]+'\')"><b>'+c[0]+'</b><span><em>'+c[1]+'</em>'+c[2]+'</span></button>';
      }).join('')+'</div>'+
      '<label class="u4-lbl" for="ii_why3">Defend your choice</label>'+
      '<textarea class="u4-ta" id="ii_why3" placeholder="Why this choice..."'+(II.l3?' disabled':'')+' oninput="iiText(\'why3\',this.value)">'+u4esc(II.why3)+'</textarea>'+
      (II.l3?iiLockedLine(3)+iiNext(3,'Open The Reveal'):'<div class="u4-btnrow"><button type="button" class="u4-b ok" id="ii_lock3"'+(iiCan3()?'':' disabled')+' onclick="iiLock(3)">Lock Round 3</button></div>');
  }else if(II.stage===3){
    var R=G.reveal,inside=II.r1.filter(function(x){return II_INSIDE.indexOf(x)>=0;}).length;
    var out=iiLeft2().filter(function(i){return II_OUTSIDE_SIGNALS.indexOf(i)>=0;});
    var ch=G.choices.filter(function(c){return c[0]===II.r3;})[0]||['','',''];
    var you=[
      '<b>You prioritised:</b><ul>'+II.r1.slice().sort().map(function(id){return '<li>'+id+'. '+iiSrc(id)+'</li>';}).join('')+'</ul>Sources A to D are indicators from inside higher education. Sources E to H sit outside it. You chose <b>'+inside+' from inside</b> and <b>'+(4-inside)+' from outside</b>.',
      '<b>You deprioritised:</b><ul>'+iiLeft2().map(function(i){return '<li>Signal '+(i+1)+': '+G.signals[i]+'</li>';}).join('')+'</ul>Signals 3, 4 and 6 come from outside conventional higher education. You deprioritised <b>'+out.length+' of those three</b>.'+(II.why2.trim()?'<br><b>Your reasons:</b> '+u4esc(II.why2):''),
      '<b>You chose:</b> '+ch[0]+'. '+ch[1]+'. '+ch[2]+(II.why3.trim()?'<br><b>Your defence:</b> '+u4esc(II.why3):'')
    ];
    h='<h5>The Reveal</h5><p>Each round tested one trap. Your own decisions are the evidence.</p>'+R.map(function(r,i){
      return '<div class="u4-rev"><div class="u4-rev-h"><small>'+r.round+'</small><span>'+r.ask+'</span></div><div class="u4-rev-b">'+
        '<div class="u4-rev-you">'+you[i]+'</div><div class="u4-rev-trap">'+r.trap+'</div><div class="u4-rev-line">'+r.line+'</div><p class="u4-say">&ldquo;'+r.q+'&rdquo;</p></div></div>';
    }).join('')+U4D.chainHtml+'<div class="u4-quote"><p>'+G.insight+'</p></div>'+
      '<div class="u4-btnrow"><button type="button" class="u4-b ok" onclick="iiReveal()">Now apply Arena &rarr;</button></div>';
  }else{
    var keys=['fn','em','so'];
    h='<h5>Now apply Arena</h5><p class="u4-say">&ldquo;'+G.arena_q+'&rdquo;</p>'+G.arena.map(function(a,i){
      return '<label class="u4-lbl" for="ii_'+keys[i]+'">'+a[0]+': '+a[1]+'</label><textarea class="u4-ta" id="ii_'+keys[i]+'" placeholder="Your answer..." oninput="iiText(\''+keys[i]+'\',this.value)">'+u4esc(II[keys[i]])+'</textarea>';
    }).join('')+
      '<p class="u4-say" style="margin-top:18px;">&ldquo;'+G.final+'&rdquo;</p>'+
      '<div class="u4-rev-you"><b>Not prioritised in Round 1:</b><ul>'+iiLeft1().map(function(id){return '<li>'+id+'. '+iiSrc(id)+'</li>';}).join('')+'</ul>'+
      '<b>Deprioritised in Round 2:</b><ul>'+iiLeft2().map(function(i){return '<li>Signal '+(i+1)+': '+G.signals[i]+'</li>';}).join('')+'</ul></div>'+
      '<label class="u4-lbl" for="ii_fin">Your answer to the final challenge</label><textarea class="u4-ta" id="ii_fin" placeholder="Your answer..." oninput="iiText(\'fin\',this.value)">'+u4esc(II.fin)+'</textarea>';
  }
  return '<div class="u4-panel">'+h+'</div>';
}
function renderII(){var host=u4el('iiGameP');if(host)host.innerHTML=iiStageNav()+iiPanel();}
function iiGo(i){if(!iiOpen(i))return;II.stage=i;renderII();iiQueue();var host=u4el('iiGameP');if(host&&host.getBoundingClientRect().top<0)host.scrollIntoView({behavior:'smooth',block:'start'});}
function iiPick1(id){if(II.l1)return;var i=II.r1.indexOf(id);if(i>=0)II.r1.splice(i,1);else if(II.r1.length<4)II.r1.push(id);renderII();iiQueue();}
function iiPick2(i){if(II.l2)return;var x=II.r2.indexOf(i);if(x>=0)II.r2.splice(x,1);else if(II.r2.length<3)II.r2.push(i);renderII();iiQueue();}
function iiPick3(c){if(II.l3)return;II.r3=c;renderII();iiQueue();}
function iiCan2(){return II.r2.length===3&&!!II.why2.trim();}
function iiCan3(){return !!II.r3&&!!II.why3.trim();}
function iiText(k,val){
  II[k]=val;
  var b2=u4el('ii_lock2');if(b2)b2.disabled=!iiCan2();
  var b3=u4el('ii_lock3');if(b3)b3.disabled=!iiCan3();
  iiQueue();
}
function iiLock(n){
  if(n===1&&II.r1.length===4)II.l1=true;
  else if(n===2&&II.l1&&iiCan2())II.l2=true;
  else if(n===3&&II.l2&&iiCan3())II.l3=true;
  else return;
  renderII();iiSaveNow();
}
function iiReveal(){II.rev=true;II.stage=4;renderII();iiSaveNow();var host=u4el('iiGameP');if(host)host.scrollIntoView({behavior:'smooth',block:'start'});}
function iiStatus(){return iiComplete()?'Complete':II.rev?'In progress · Arena':II.l3?'In progress · The Reveal':II.l2?'In progress · Round 3':II.l1?'In progress · Round 2':'In progress · Round 1';}
function iiTexts(){
  var G=U4D.game,ch=G.choices.filter(function(c){return c[0]===II.r3;})[0];
  return {
    ii_round1:(II.l1?'Locked':'Open')+'\nPrioritised:\n'+II.r1.slice().sort().map(function(id){return '  '+id+'. '+u4plain(iiSrc(id));}).join('\n'),
    ii_round2:(II.l2?'Locked':'Open')+'\nInvestigate:\n'+II.r2.slice().sort().map(function(i){return '  Signal '+(i+1)+': '+u4plain(G.signals[i]);}).join('\n')+
      (II.r2.length===3?'\nDeprioritised:\n'+iiLeft2().map(function(i){return '  Signal '+(i+1)+': '+u4plain(G.signals[i]);}).join('\n'):'')+'\nWhy deprioritised: '+II.why2.trim(),
    ii_round3:(II.l3?'Locked':'Open')+'\nChoice: '+(ch?ch[0]+'. '+u4plain(ch[1])+'. '+u4plain(ch[2]):'')+'\nDefence: '+II.why3.trim(),
    ii_arena:G.arena.map(function(a,i){return u4plain(a[0])+': '+II[['fn','em','so'][i]].trim();}).join('\n')+'\nFinal challenge: '+II.fin.trim(),
    ii_status:iiStatus()
  };
}
var _iiTimer=null;
function iiQueue(){clearTimeout(_iiTimer);_iiTimer=setTimeout(iiSaveNow,900);}
async function iiSaveNow(){
  clearTimeout(_iiTimer);
  var ok=await u4save('__ii_work',II),t=iiTexts();
  for(var k in t){ok=(await u4save(k,t[k]))&&ok;}
  return !!ok;
}

/* ── 4.2 · STRESS-TESTING YOUR KEY RESULTS (Capstone work): each Key Result across the four steps of the worked example ── */
function u4Tab(gid,i){
  var g=u4el(gid);if(!g)return;
  g.querySelectorAll('.u4-stage').forEach(function(t,x){t.classList.toggle('active',x===i);});
  g.querySelectorAll('.u4-wpanel').forEach(function(p,x){p.classList.toggle('active',x===i);});
}
var MB={step:0,items:[],cur:[0,0]};
var MB_KEYS=['mbt_arena','mbt_bound','mbt_comp','mbt_value'];
var MB_NAMES=['MBT · Arena','MBT · Boundaries','MBT · Competition','MBT · Value Proposition'];
var MB_F=['a','b','c','v'];                                   // the Must-Be-True condition of each step
var MB_STEP_F=[['fn','ex','co','a'],['bd','b'],['cp','c'],['rel','dis','dlv','v']];
var MB_ALL=['fn','ex','co','a','bd','b','cp','c','rel','dis','dlv','v'];
var MB_FIELDS={
  fn:['Functional · What does the customer need done that this Key Result serves?','What needs to get done, solved, accessed, changed or achieved?'],
  ex:['Experiential · What matters to the customer about how it is done?','What matters to the customer about the experience of achieving the functional outcome?'],
  co:['Consequential · What does this Key Result enable for the customer?','What becomes possible, better or different for the customer once this Key Result is achieved?'],
  bd:['The boundaries','One boundary on each line. For each one, give its kind (regulatory, operational, technological, structural, financial or behavioural) and say whether you must accept it, can influence it, or created it yourselves.'],
  cp:['The alternatives','One alternative on each line: every other way the customer can get what this Key Result delivers. Include those outside your industry: doing it themselves, using technology, postponing it, doing nothing.'],
  rel:['Relevant · Does this Key Result matter to the customer?','Which customer need from Step 1 does this Key Result address?'],
  dis:['Distinctive · What does it give the customer that the alternatives do not?','Compare with the alternatives you listed in Step 3.'],
  dlv:['Deliverable · Can we consistently produce it?','Which capability and system let you deliver this Key Result repeatedly?']
};
function mbId(i,j){return (i+1)+'abcdefgh'.charAt(j);}
function mbBlankKr(t){var k={t:t};MB_ALL.forEach(function(f){k[f]='';});return k;}
function mbLoad(s){
  if(!s||typeof s!=='object')return;
  if(Array.isArray(s.items))MB.items=s.items.filter(function(o){return o&&o.obj&&Array.isArray(o.krs)&&o.krs.length;}).map(function(o){
    return {obj:String(o.obj),krs:o.krs.map(function(k){var n=mbBlankKr(String(k.t||''));MB_ALL.forEach(function(f){n[f]=String(k[f]||'');});return n;})};
  });
  var c=Array.isArray(s.cur)?s.cur:[0,0];
  MB.cur=(MB.items[c[0]]&&MB.items[c[0]].krs[c[1]])?[c[0],c[1]]:[0,0];
  MB.step=(s.step>=0&&s.step<4)?s.step:0;
}
function mbAll(){var out=[];MB.items.forEach(function(o,i){o.krs.forEach(function(k,j){out.push({i:i,j:j,o:o,k:k});});});return out;}
function mbKr(){var o=MB.items[MB.cur[0]];return o?o.krs[MB.cur[1]]:null;}
function mbStepDone(k,n){return !!k&&MB_STEP_F[n].every(function(f){return k[f].trim();});}
function mbKrDone(k){return [0,1,2,3].every(function(n){return mbStepDone(k,n);});}
function mbOpen(){return mbAll().filter(function(x){return !mbKrDone(x.k);});}
function mbConfirmed(){return MB_NAMES.every(u4isConf);}
function mbText(n){
  var lab={fn:'Functional',ex:'Experiential',co:'Consequential',bd:'Boundaries',cp:'Alternatives',rel:'Relevant',dis:'Distinctive',dlv:'Deliverable'};
  return MB.items.map(function(o,i){
    return 'Objective '+(i+1)+': '+o.obj.trim()+'\n'+o.krs.map(function(k,j){
      return '   Key Result '+mbId(i,j)+': '+k.t.trim()+'\n'+MB_STEP_F[n].slice(0,-1).map(function(f){return '   '+lab[f]+': '+k[f].trim().replace(/\n/g,'; ');}).join('\n')+'\n   Must-Be-True: '+k[MB_F[n]].trim();
    }).join('\n\n');
  }).join('\n\n');
}
/* The whole record as text, saved while the group works, so the facilitator report shows progress before Confirm. */
function mbRecordText(){
  var lab={fn:'Functional',ex:'Experiential',co:'Consequential',bd:'Boundaries',cp:'Alternatives',rel:'Relevant',dis:'Distinctive',dlv:'Deliverable'};
  var all=mbAll(),done=all.filter(function(x){return mbKrDone(x.k);}).length;
  return (mbConfirmed()?'Confirmed':'Not yet confirmed')+' · '+done+' of '+all.length+' Key Results taken through the four steps\n\n'+MB.items.map(function(o,i){
    return 'Objective '+(i+1)+': '+o.obj.trim()+'\n'+o.krs.map(function(k,j){
      return '   Key Result '+mbId(i,j)+': '+k.t.trim()+'\n'+[0,1,2,3].map(function(n){
        return '   '+U4D.steps[n][0]+' · '+U4D.steps[n][1]+'\n'+MB_STEP_F[n].slice(0,-1).map(function(f){return '      '+lab[f]+': '+k[f].trim().replace(/\n/g,'; ');}).join('\n')+'\n      Must-Be-True: '+k[MB_F[n]].trim();
      }).join('\n');
    }).join('\n\n');
  }).join('\n\n');
}
function mbRecordHtml(){
  var all=mbAll(),done=all.filter(function(x){return mbKrDone(x.k);}).length;
  var head='<div class="u4-rec-h" onclick="this.parentNode.classList.toggle(\'shut\')">Your ABCV&ndash;MBT record<span>'+(all.length?done+' of '+all.length+' Key Results tested &middot; ':'')+'select to open or close</span></div>';
  if(!all.length)return head+'<div class="u4-rec-b"><div class="u4-rec-empty">Your record starts when your Unit 3 Key Results are brought in. The Must-Be-True condition of each step is added here.</div></div>';
  return head+'<div class="u4-rec-b">'+MB.items.map(function(o,i){
    return '<div class="u4-rec-o">Objective '+(i+1)+' &middot; '+u4esc(o.obj)+'</div>'+o.krs.map(function(k,j){
      return '<div class="u4-rec-k">Key Result '+mbId(i,j)+' &middot; '+u4esc(k.t)+'</div>'+U4D.cps.map(function(c){
        return '<div class="u4-rec-c '+c.cls+'"><span class="u4-tag">'+c.name+'</span><div>'+(k[c.k].trim()?u4esc(k[c.k]):'<i>Must-Be-True to be named</i>')+'</div></div>';
      }).join('');
    }).join('');
  }).join('')+'</div>';
}
function mbPickHtml(){
  if(!MB.items.length)return '<div class="u4-okrs"><div class="u4-egs-h">From Unit 3 &middot; your group&rsquo;s Key Results</div><div class="u4-locked">No Key Results are here yet. Select Bring in from my Unit 3 page.</div></div>';
  return '<div class="u4-egs-h">From Unit 3 &middot; your group&rsquo;s Key Results &middot; select the one to test</div><div class="u4-krs">'+MB.items.map(function(o,i){
    return '<div class="u4-krs-o">Objective '+(i+1)+' &middot; '+u4esc(o.obj)+'</div>'+o.krs.map(function(k,j){
      var act=MB.cur[0]===i&&MB.cur[1]===j;
      return '<button type="button" class="u4-krb'+(act?' active':'')+(mbKrDone(k)?' done':'')+'" onclick="mbGo('+i+','+j+')"><b>'+(mbKrDone(k)?'&#10003;':mbId(i,j))+'</b><span>'+u4esc(k.t)+'</span></button>';
    }).join('');
  }).join('')+'</div>';
}
function mbField(k,f){
  var d=MB_FIELDS[f];
  return '<label class="u4-lbl" for="mb_'+f+'">'+d[0]+'</label><div class="u4-hint">'+d[1]+'</div>'+
    '<textarea class="u4-ta" id="mb_'+f+'" placeholder="Your group&rsquo;s agreed entry..." oninput="mbSet(\''+f+'\',this.value)">'+u4esc(k[f])+'</textarea>';
}
function mbQ(q,k){return q.replace('{kr}','<span class="u4-krq">&ldquo;'+u4esc(k.t.trim().replace(/\.+$/,''))+'&rdquo;</span>');}
function mbMbt(k,n){
  var c=U4D.cps[n];
  return '<div class="u4-wcp '+c.cls+'" style="margin-top:18px;"><div class="u4-wcp-n">'+c.name+' &middot; Must-Be-True</div><div class="u4-wcp-q">'+mbQ(U4D.stepMbt[n],k)+'</div>'+
    '<textarea class="u4-ta" id="mb_'+c.k+'" placeholder="The one condition your group agrees must remain true. Write it so that it is either true or false." oninput="mbSet(\''+c.k+'\',this.value)">'+u4esc(k[c.k])+'</textarea></div>';
}
function mbFrom(n,label,val){return '<div class="u4-from"><b>From Step '+n+' &middot; '+label+'</b>'+(val.trim()?u4esc(val):'<i>to be completed in Step '+n+'</i>')+'</div>';}
function mbToolHtml(){
  var k=mbKr();if(!k)return '';
  var n=MB.step,S=U4D.steps,o=MB.items[MB.cur[0]];
  var nav='<div class="u4-stages">'+S.map(function(s,i){
    return '<div class="u4-stage'+(i===n?' active':'')+(mbStepDone(k,i)?' done':'')+'" onclick="mbStepGo('+i+')"><small>'+s[0]+'</small>'+s[1]+'</div>';
  }).join('')+'</div>';
  var h='<div class="u4-work-h">Key Result '+mbId(MB.cur[0],MB.cur[1])+' &middot; '+u4esc(k.t)+'</div><div class="u4-work-o">Objective '+(MB.cur[0]+1)+' &middot; '+u4esc(o.obj)+'</div>'+
    '<h5>'+S[n][0]+' &middot; '+S[n][1]+'</h5><p class="u4-say">'+mbQ(U4D.stepQ[n],k)+'</p>';
  var end=mbFrom(1,'the customer need this Key Result serves','Functional: '+k.fn.trim()+'\nExperiential: '+k.ex.trim()+'\nConsequential: '+k.co.trim());
  if(!(k.fn.trim()||k.ex.trim()||k.co.trim()))end=mbFrom(1,'the customer need this Key Result serves','');
  if(n===0)h+='<p>Take the customer this Key Result serves. Answer at the three depths, then name what must remain true.</p>'+mbField(k,'fn')+mbField(k,'ex')+mbField(k,'co');
  else if(n===1)h+=end+'<p>List the boundaries material enough to affect this Key Result. Leave out the rest. Then name what must remain true.</p>'+mbField(k,'bd');
  else if(n===2)h+=end+'<p>List every credible alternative the customer has for getting what this Key Result delivers. Then name what must remain true.</p>'+mbField(k,'cp');
  else h+=end+mbFrom(3,'the alternatives to this Key Result',k.cp)+'<p>Apply the three tests to this Key Result. Then name what must remain true.</p>'+mbField(k,'rel')+mbField(k,'dis')+mbField(k,'dlv');
  h+=mbMbt(k,n);
  h+='<div class="u4-btnrow">'+(n>0?'<button type="button" class="u4-b" onclick="mbStepGo('+(n-1)+')">&larr; '+S[n-1][0]+'</button>':'')+
    (n<3?'<button type="button" class="u4-b ok" onclick="mbStepGo('+(n+1)+')">'+S[n+1][0]+' &middot; '+S[n+1][1]+' &rarr;</button>':
      '<button type="button" class="u4-b ok" onclick="mbKrStep(1)">Next Key Result &rarr;</button>')+'</div>';
  return nav+'<div class="u4-panel">'+h+'</div>';
}
function mbOutHtml(){
  if(!MB.items.length)return '';
  var conf=mbConfirmed();
  var badge=conf?'<span class="u4-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u4-conf no">Not yet confirmed</span>';
  return '<div class="u4-out"><div class="u4-out-h">Into your Capstone'+badge+'</div>'+
    '<p class="u4-lead" style="font-size:13px;margin-bottom:8px;">When every Key Result has been taken through the four steps, select Confirm. Your confirmed work feeds boxes 4A to 4D of your team&rsquo;s Capstone Blueprint. An edit after confirmation sets the record back to not yet confirmed.</p>'+
    '<div class="u4-btnrow"><button type="button" class="u4-b ok" onclick="mbConfirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u4-b" onclick="mbPrint()">Print</button></div>'+
    '<div class="u4-note" id="mbMsg" style="display:none;"></div></div>';
}
function renderMB(){
  var r=u4el('mbRecP'),k=u4el('mbOkrP'),t=u4el('mbToolP'),o=u4el('mbOutP');
  if(k)k.innerHTML=mbPickHtml();
  if(r){var shut=r.classList.contains('shut');r.innerHTML=mbRecordHtml();r.classList.toggle('shut',shut);}
  if(t)t.innerHTML=mbToolHtml();
  if(o)o.innerHTML=mbOutHtml();
}
function mbRefresh(){   // while typing: everything except the box being typed in
  var r=u4el('mbRecP');
  if(r){var shut=r.classList.contains('shut'),before=r.offsetHeight;r.innerHTML=mbRecordHtml();r.classList.toggle('shut',shut);var d=r.offsetHeight-before;if(d&&r.getBoundingClientRect().top<window.innerHeight)window.scrollBy(0,d);}
  var o=u4el('mbOutP');if(o)o.innerHTML=mbOutHtml();
  var k=mbKr();
  document.querySelectorAll('#mbToolP .u4-stage').forEach(function(s,n){s.classList.toggle('done',mbStepDone(k,n));});
  document.querySelectorAll('#mbOkrP .u4-krb').forEach(function(b,n){
    var x=mbAll()[n];if(!x)return;
    b.classList.toggle('done',mbKrDone(x.k));b.firstChild.innerHTML=mbKrDone(x.k)?'&#10003;':mbId(x.i,x.j);
  });
}
function mbPaint(){var k=u4el('mbOkrP'),t=u4el('mbToolP');if(k)k.innerHTML=mbPickHtml();if(t)t.innerHTML=mbToolHtml();}
function mbStepGo(n){
  if(n<0||n>3)return;MB.step=n;mbPaint();mbQueue();
  var t=u4el('mbToolP');if(t&&t.getBoundingClientRect().top<0)t.scrollIntoView({behavior:'smooth',block:'start'});
}
function mbGo(i,j){MB.cur=[i,j];MB.step=0;mbPaint();mbQueue();var t=u4el('mbToolP');if(t)t.scrollIntoView({behavior:'smooth',block:'nearest'});}
function mbKrStep(d){
  var all=mbAll(),n=0;all.forEach(function(x,q){if(x.i===MB.cur[0]&&x.j===MB.cur[1])n=q;});
  var x=all[(n+d+all.length)%all.length];if(!x)return;
  mbGo(x.i,x.j);
}
var _mbTimer=null,_mbPaint=null;
function mbUnconfirm(){if(mbConfirmed()){MB_NAMES.forEach(function(nm){var i=U4.conf.indexOf(nm);if(i>=0)U4.conf.splice(i,1);});MB._unconf=true;}}
function mbSet(f,val){
  var k=mbKr();if(!k)return;
  k[f]=val;mbUnconfirm();
  clearTimeout(_mbPaint);_mbPaint=setTimeout(mbRefresh,350);
  mbQueue();
}
function mbQueue(){clearTimeout(_mbTimer);_mbTimer=setTimeout(mbSaveNow,900);}
async function mbSaveNow(){
  clearTimeout(_mbTimer);
  await u4save('__mbt_work',{step:MB.step,items:MB.items,cur:MB.cur});
  if(MB._unconf){MB._unconf=false;await u4save('confirmed_items',U4.conf);}
  if(MB.items.length)await u4save('mbt_record',mbRecordText());
}
async function mbConfirm(){
  var open=mbOpen();
  if(!mbAll().length){u4msg('mbMsg','Bring in your Unit 3 Key Results first.');return;}
  if(open.length){
    u4msg('mbMsg','Take every Key Result through the four steps before you confirm. Still open: '+open.map(function(x){
      var st=[0,1,2,3].filter(function(n){return !mbStepDone(x.k,n);}).map(function(n){return n+1;});
      return 'Key Result '+mbId(x.i,x.j)+' (Step '+st.join(', ')+')';}).join('; ')+'.');return;
  }
  await mbSaveNow();
  var ok=true;
  for(var n=0;n<4;n++){ok=(await u4save(MB_KEYS[n],mbText(n)))&&ok;}
  if(!ok){u4msg('mbMsg','Not saved. Check your connection, then select Confirm again.');return;}
  await u4setConf(MB_NAMES,true);
  await u4save('mbt_record',mbRecordText());
  renderMB();u4msg('mbMsg','✓ Confirmed. Your work is ready for your team’s Capstone Blueprint.','ok');
}
function mbPrint(){
  var row=function(a,b){return '<tr><th>'+a+'</th><td>'+(String(b).trim()?u4esc(b).replace(/\n/g,'<br>'):'—')+'</td></tr>';};
  var body=MB.items.map(function(o,i){
    return '<h2>Objective '+(i+1)+' · '+u4esc(o.obj)+'</h2>'+o.krs.map(function(k,j){
      return '<h3>Key Result '+mbId(i,j)+' · '+u4esc(k.t)+'</h3>'+
        '<p class="kr">Step 1 · Arena</p><table>'+row('Functional',k.fn)+row('Experiential',k.ex)+row('Consequential',k.co)+row('Must-Be-True',k.a)+'</table>'+
        '<p class="kr">Step 2 · Boundaries</p><table>'+row('Boundaries',k.bd)+row('Must-Be-True',k.b)+'</table>'+
        '<p class="kr">Step 3 · Competition</p><table>'+row('Alternatives',k.cp)+row('Must-Be-True',k.c)+'</table>'+
        '<p class="kr">Step 4 · Value Proposition</p><table>'+row('Relevant',k.rel)+row('Distinctive',k.dis)+row('Deliverable',k.dlv)+row('Must-Be-True',k.v)+'</table>';
    }).join('');
  }).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Unit 4 · ABCV–MBT record</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:16px;margin:24px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px;page-break-after:avoid}h3{color:#071b4d;font-size:14px;margin:16px 0 4px;page-break-after:avoid}.kr{font-family:Arial,sans-serif;font-size:12px;font-weight:bold;margin:10px 0 4px;color:#555}table{width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:13px;page-break-inside:avoid}th{width:150px;text-align:left;vertical-align:top;padding:6px 8px;border:1px solid #ccd;background:#f3f6f4}td{padding:6px 8px;border:1px solid #ccd;vertical-align:top}</style></head><body>'+
    '<h1>ABCV–MBT Record: Stress-Testing Your Key Results</h1><p class="sub">Strategy2Results® · Module 2 · Unit 4 · Part 4.2 · Capstone work · '+(mbConfirmed()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
/* Bring in the group's confirmed Enterprise OKRs from the member's own Unit 3 page (read only; nothing is typed again). */
async function mbBring(manual){
  if(!window.S2R){if(manual)u4msg('mbBringMsg','The save system is not ready. Reload the page and try again.');return;}
  var u3={};try{u3=await S2R.loadAll(U3_LENS);}catch(e){u3={};}
  var w=u3&&u3.__okr_work,conf=(u3&&Array.isArray(u3.confirmed_items))?u3.confirmed_items:[];
  var found=[];
  if(w&&Array.isArray(w.items)){
    w.items.forEach(function(o){
      if(!o||!String(o.theme||'').trim()||!String(o.obj||'').trim())return;
      var krs=(o.krs||[]).filter(function(k){return k&&String(k.t||'').trim();});
      var al=Array.isArray(o.al)&&o.al.length===4&&o.al.every(function(x){return !!x;});
      if(krs.length&&al)found.push({obj:String(o.obj).trim(),krs:krs.map(function(k){return mbBlankKr(String(k.t).trim());})});
    });
  }
  if(!found.length||conf.indexOf('Enterprise OKRs')<0){
    if(manual||!MB.items.length)u4msg('mbBringMsg','No confirmed Enterprise OKRs were found on your Unit 3 page. Confirm your group’s OKRs in Unit 3, part 4.2, then select Bring in from my Unit 3 page.');
    return;
  }
  var old={};mbAll().forEach(function(x){old[x.k.t]=x.k;});
  var lost=mbAll().filter(function(x){return MB_ALL.some(function(f){return x.k[f].trim();})&&!found.some(function(o){return o.krs.some(function(k){return k.t===x.k.t;});});});
  var same=JSON.stringify(found.map(function(o){return [o.obj,o.krs.map(function(k){return k.t;})];}))===JSON.stringify(MB.items.map(function(o){return [o.obj,o.krs.map(function(k){return k.t;})];}));
  if(same){if(manual)u4msg('mbBringMsg','Your Key Results already match your Unit 3 page.','ok');return;}
  if(!manual&&MB.items.length)return;
  if(manual&&lost.length&&!window.confirm('Your Unit 3 page no longer holds '+lost.length+' Key Result'+(lost.length===1?'':'s')+' you have typed entries for. Bring in the current Key Results and remove those entries?'))return;
  found.forEach(function(o){o.krs.forEach(function(k){var p=old[k.t];if(p)MB_ALL.forEach(function(f){k[f]=p[f];});});});
  MB.items=found;MB.cur=[0,0];
  mbUnconfirm();
  renderMB();await mbSaveNow();
  var n=mbAll().length;
  u4msg('mbBringMsg','Brought in from your Unit 3 page: '+found.length+' Objective'+(found.length===1?'':'s')+' and '+n+' Key Result'+(n===1?'':'s')+'.','ok');
}

/* ── Section 5 · CAUSE OF DEATH: the game is unchanged; its result is now kept and saved ──────── */
var MINE_NAMES=['The Ghost Ship','The Ferrari in the Mud','The Invisible Disruption','The Identity Crisis'];
var MINE_CP=['ARENA','BOUNDARIES','COMPETITION','VALUE PROPOSITION'];
var _mineBusy=false;
function mineState(){return {attempts:mineAttempts.slice(),defused:mineDefused.slice()};}
function mineText(){
  return 'Score '+score+' of 8 · '+defused+' of 4 mines defused\n'+MINE_NAMES.map(function(nm,i){
    return 'Mine '+(i+1)+' — '+nm+': '+(mineDefused[i]?'defused at attempt '+mineAttempts[i]+' · '+(mineAttempts[i]===1?'2 points':'1 point'):(mineAttempts[i]?'not yet defused ('+mineAttempts[i]+(mineAttempts[i]===1?' attempt':' attempts')+')':'not yet attempted'));
  }).join('\n');
}
var _mineTimer=null;
function mineQueue(){if(_mineBusy)return;clearTimeout(_mineTimer);_mineTimer=setTimeout(mineSaveNow,700);}
async function mineSaveNow(){clearTimeout(_mineTimer);var a=await u4save('__mine_game',mineState()),b=await u4save('mine_result',mineText());return !!(a&&b);}
var _checkMine0=checkMine,_resetGame0=resetGame;
checkMine=function(idx,correctQ,correctL,pts){var was=mineAttempts[idx];_checkMine0(idx,correctQ,correctL,pts);if(mineAttempts[idx]!==was)mineQueue();};
resetGame=function(){_resetGame0();mineQueue();};
function mineRestore(s){
  if(!s||!Array.isArray(s.attempts)||!Array.isArray(s.defused))return;
  _mineBusy=true;
  try{
    _resetGame0();
    for(var i=0;i<4;i++){
      var n=Math.max(0,parseInt(s.attempts[i],10)||0);
      if(s.defused[i]&&n>=1){
        u4el('mine'+i+'q').value='correct';u4el('mine'+i+'l').value=MINE_CP[i];
        mineAttempts[i]=n-1;_checkMine0(i,'correct',MINE_CP[i],2);
      }else mineAttempts[i]=n;
    }
  }finally{_mineBusy=false;}
}

/* ── Start: draw the tools empty, then fill them from the saved answers ───────────────────────── */
function u4Init(responses){
  responses=responses||{};
  U4.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  iiLoad(responses.__ii_work);mbLoad(responses.__mbt_work);
  renderII();renderMB();
  mineRestore(responses.__mine_game);
  U4.ready=true;
  mbBring(false);
}
renderII();renderMB();
