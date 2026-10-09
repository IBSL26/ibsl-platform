
/* ════════════ UNIT 6 · SECTION 5 · DESIGNING THE PM ARCHITECTURE (group work, Capstone work) ════════════
   Four steps: scoring logic, FACES, EXECUTION, PM scorecards for the CEO and the CFO on two of the group's Key Results.
   Answers save as the participant types (__pm_work, pm_record). Confirm writes pm_scoring, pm_faces, pm_execution and pm_scorecards
   and the four "PM Architecture · …" names into confirmed_items. An edit after confirmation takes the names out again.
   The group's Enterprise OKRs are read from the member's own Unit 3 page (read only; nothing is typed again). */
var U6_LENS='u3m1_lens5',U6_U3_LENS='u2m1_lens2';
var U6F=/*FIELDS*/[];
var U6P=/*PARTS*/[];
var U6={conf:[],w:{},okrs:[],ready:false};
var U6_NAMES=U6P.map(function(p){return p[2];});
function u6el(id){return document.getElementById(id);}
function u6esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u6msg(id,text,cls){var m=u6el(id);if(!m)return;m.textContent=text||'';m.className='u6-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u6save(k,val){
  if(!window.S2R){console.warn('[unit3_m1_lens5_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U6_LENS,k,val);}catch(e){console.error('[unit3_m1_lens5_p] save failed for '+k,e);return false;}
}
var _u6t={};
function u6later(name,fn,ms){clearTimeout(_u6t[name]);_u6t[name]=setTimeout(fn,ms||700);}
function u6has(){return U6_NAMES.every(function(nm){return U6.conf.indexOf(nm)>=0;});}
function u6drop(){var ch=false;U6_NAMES.forEach(function(nm){var i=U6.conf.indexOf(nm);if(i>=0){U6.conf.splice(i,1);ch=true;}});return ch;}
function u6norm(w){var o={};U6F.forEach(function(f){o[f[0]]=(w&&typeof w[f[0]]==='string')?w[f[0]]:'';});return o;}
function u6val(id){return String(U6.w[id]||'').trim();}
function u6Step(i){
  var tabs=document.querySelectorAll('#mod4 .step-tab'),panels=document.querySelectorAll('#mod4 .step-panel');
  tabs.forEach(function(t,j){t.classList.toggle('active',j===i);});panels.forEach(function(p,j){p.classList.toggle('active',j===i);});
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
/* The text of one part, as it is written into the Capstone: sub-heading, then one line for each entry. */
function u6Text(part){
  var out=[],last=null;
  U6F.filter(function(f){return f[2]===part;}).forEach(function(f){
    if(f[3]!==last){out.push((out.length?'\n':'')+f[3]);last=f[3];}
    out.push(f[1]+': '+(u6val(f[0])+(f[4]==='n'&&u6val(f[0])?'%':'')));
  });
  return out.join('\n');
}
function u6Fill(){
  U6F.forEach(function(f){var el=u6el('u6_'+f[0]);if(!el||f[4]==='k')return;el.value=U6.w[f[0]]||'';});
  u6KrDraw();u6TotDraw();
}
function u6In(id,val){
  U6.w[id]=String(val===undefined||val===null?'':val);
  if(u6drop())u6later('conf',function(){u6save('confirmed_items',U6.conf);},600);
  u6msg('u6Msg','');
  if(/^kr[12]$/.test(id))u6KrDraw();
  if(/_w$/.test(id))u6TotDraw();
  u6later('rec',u6RecDraw,300);
  u6later('save',async function(){await u6save('__pm_work',U6.w);await u6save('pm_record',U6P.map(function(p){return p[1].toUpperCase()+'\n'+u6Text(p[0]);}).join('\n\n'));},800);
}
/* Step 4: the two Key Results the group chose, shown on each scorecard row. */
function u6KrDraw(){
  [1,2].forEach(function(n){
    var v=u6val('kr'+n),sel=u6el('u6_kr'+n);
    if(sel){
      var opts=['<option value="">Choose a Key Result…</option>'],seen=false;
      U6.okrs.forEach(function(o){opts.push('<optgroup label="'+u6esc(o.obj)+'">'+o.krs.map(function(k){if(k===v)seen=true;return '<option value="'+u6esc(k)+'"'+(k===v?' selected':'')+'>'+u6esc(k)+'</option>';}).join('')+'</optgroup>');});
      if(v&&!seen)opts.push('<option value="'+u6esc(v)+'" selected>'+u6esc(v)+'</option>');
      sel.innerHTML=opts.join('');sel.disabled=!(U6.okrs.length||v);
    }
    document.querySelectorAll('.u6-kr'+n+'-t').forEach(function(el){el.textContent=v||'Choose Key Result '+n+' above.';});
  });
}
function u6Sum(role){var s=0,all=true;['kr1','kr2','op','bv'].forEach(function(k){var v=u6val(role+'_'+k+'_w');if(v===''||isNaN(Number(v)))all=false;else s+=Number(v);});return {sum:s,all:all};}
function u6TotDraw(){
  ['ceo','cfo'].forEach(function(role){var el=u6el('u6_tot_'+role);if(!el)return;var t=u6Sum(role);
    el.textContent='Total weight: '+t.sum+'%'+(t.all&&t.sum===100?' ✓':' · the four weights add up to 100%');el.className='u6-tot '+(t.all&&t.sum===100?'ok':'no');});
}
function u6Open(){
  var open=[];
  U6P.forEach(function(p,i){
    var n=U6F.filter(function(f){if(f[2]!==p[0])return false;var v=u6val(f[0]);return !v||(f[4]==='n'&&(isNaN(Number(v))||Number(v)<0||Number(v)>100));}).length;
    if(n)open.push('Step '+(i+1)+' · '+p[1]+' ('+n+(n===1?' entry':' entries')+' still open)');
  });
  if(u6val('kr1')&&u6val('kr1')===u6val('kr2'))open.push('two different Key Results in Step 4');
  ['ceo','cfo'].forEach(function(role){var t=u6Sum(role);if(t.all&&t.sum!==100)open.push('the '+role.toUpperCase()+' weights add up to 100% (now '+t.sum+'%)');});
  return open;
}
function u6RecDraw(){
  var host=u6el('u6Rec');if(!host)return;
  var conf=u6has(),msg=u6el('u6Msg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u6-out"><div class="u6-out-h">Your group&rsquo;s record'+(conf?'<span class="u6-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u6-conf no">Not yet confirmed</span>')+'</div>'+
    U6P.map(function(p,i){
      var fs=U6F.filter(function(f){return f[2]===p[0];}),done=fs.filter(function(f){return u6val(f[0]);}).length,last=null;
      return '<details class="u6-rec"><summary>Step '+(i+1)+' &middot; '+u6esc(p[1])+'<span>'+done+' of '+fs.length+' entries</span></summary>'+fs.map(function(f){
        var v=u6val(f[0]),h=(f[3]!==last)?'<div class="u6-rec-s">'+u6esc(f[3])+'</div>':'';last=f[3];
        return h+'<div class="u6-rec-t"><strong>'+u6esc(f[1])+':</strong> '+(v?u6esc(v)+(f[4]==='n'?'%':''):'<i>to be agreed by your group</i>')+'</div>';
      }).join('')+'</details>';
    }).join('')+
    '<div class="u6-btnrow"><button type="button" class="u6-b ok" id="u6ConfBtn" onclick="u6Confirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u6-b" onclick="u6Print()">Print</button></div>'+
    '<div class="u6-note" id="u6Msg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u6el('u6Msg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function u6Confirm(){
  var open=u6Open();
  if(open.length){u6RecDraw();u6msg('u6Msg','Before you confirm, complete: '+open.join('; ')+'.');return;}
  clearTimeout(_u6t.save);clearTimeout(_u6t.conf);
  var ok=await u6save('__pm_work',U6.w);
  ok=ok&&(await u6save('pm_record',U6P.map(function(p){return p[1].toUpperCase()+'\n'+u6Text(p[0]);}).join('\n\n')));
  for(var i=0;i<U6P.length&&ok;i++)ok=await u6save(U6P[i][3],u6Text(U6P[i][0]));
  if(!ok){u6msg('u6Msg','Not saved. Check your connection, then select Confirm again.');return;}
  U6_NAMES.forEach(function(nm){if(U6.conf.indexOf(nm)<0)U6.conf.push(nm);});
  if(!(await u6save('confirmed_items',U6.conf))){u6drop();u6RecDraw();u6msg('u6Msg','Not saved. Check your connection, then select Confirm again.');return;}
  u6RecDraw();u6msg('u6Msg','✓ Confirmed. Your record is ready for your team’s Capstone Blueprint.','ok');
}
function u6Print(){
  var body=U6P.map(function(p,i){var last=null;return '<h2>Step '+(i+1)+' · '+u6esc(p[1])+'</h2>'+U6F.filter(function(f){return f[2]===p[0];}).map(function(f){
    var v=u6val(f[0]),h=(f[3]!==last)?'<h3>'+u6esc(f[3])+'</h3>':'';last=f[3];
    return h+'<p><strong>'+u6esc(f[1])+':</strong> '+(v?u6esc(v).replace(/\n/g,'<br>')+(f[4]==='n'?'%':''):'—')+'</p>';}).join('');}).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our PM architecture</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}h3{font-size:13px;margin:14px 0 2px}p{font-size:13px;margin:4px 0}</style></head><body>'+
    '<h1>Our PM architecture</h1><p class="sub">Strategy2Results® · Module 3 · Unit 6 · Section 5 · Capstone work · '+(u6has()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
/* Step 4 · the group's confirmed Enterprise OKRs from Unit 3 (read only). */
function u6OkrHtml(){
  if(!U6.okrs.length)return '<div class="u6-from"><i>Your group&rsquo;s confirmed Enterprise OKRs appear here.</i></div>';
  return U6.okrs.map(function(o){return '<div class="u6-from"><b>Objective</b>'+u6esc(o.obj)+'<ul>'+o.krs.map(function(k){return '<li>'+u6esc(k)+'</li>';}).join('')+'</ul></div>';}).join('');
}
async function u6Bring(manual){
  var host=u6el('u6Okrs');if(!host)return;
  if(!window.S2R){if(manual)u6msg('u6BringMsg','The save system is not ready. Reload the page and try again.');return;}
  var u3={};try{u3=await S2R.loadAll(U6_U3_LENS);}catch(e){u3={};}
  var w=u3&&u3.__okr_work,conf=(u3&&Array.isArray(u3.confirmed_items))?u3.confirmed_items:[],found=[];
  if(w&&Array.isArray(w.items))w.items.forEach(function(o){
    if(!o||!String(o.obj||'').trim())return;
    var krs=(o.krs||[]).map(function(k){return k&&String(k.t||'').trim();}).filter(function(k){return !!k;});
    if(krs.length)found.push({obj:String(o.obj).trim(),krs:krs});
  });
  if(!found.length||conf.indexOf('Enterprise OKRs')<0){
    U6.okrs=[];host.innerHTML=u6OkrHtml();u6KrDraw();
    u6msg('u6BringMsg','No confirmed Enterprise OKRs were found on your Unit 3 page. Confirm your group’s Enterprise OKRs in Unit 3, part 4.2, then select Bring in from my Unit 3 page.');
    return;
  }
  U6.okrs=found;host.innerHTML=u6OkrHtml();u6KrDraw();
  u6msg('u6BringMsg',manual?'Brought in from your Unit 3 page.':'',manual?'ok':'');
}
function u6Init(responses){
  responses=responses||{};
  U6.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U6.w=u6norm(responses.__pm_work);
  U6.ready=true;
  u6Fill();u6RecDraw();u6Bring(false);
}
document.addEventListener('DOMContentLoaded',function(){
  U6.w=u6norm(null);
  var mod=u6el('mod4');
  if(mod){
    mod.addEventListener('input',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u6');if(id&&ev.target.tagName!=='SELECT')u6In(id,ev.target.value);});
    mod.addEventListener('change',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u6');if(id&&ev.target.tagName==='SELECT')u6In(id,ev.target.value);});
  }
  var h=u6el('u6Okrs');if(h)h.innerHTML=u6OkrHtml();
  u6Fill();u6RecDraw();
});
