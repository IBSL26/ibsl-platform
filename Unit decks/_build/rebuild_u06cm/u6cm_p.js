/* ════════════ UNIT 6 · SECTION 5 · BUILDING YOUR ENTERPRISE PERFORMANCE MANAGEMENT SYSTEM (group work, Capstone work) ════════════
   Activity 1: the S2R® Contribution Map™ for one enterprise Key Result chosen from the group's Unit 3 Enterprise OKRs (three or four functions, six fields each).
   Activity 2: FACES applied to each function named in Activity 1.
   Answers save as the participant types (__cm_work, cm_record). Confirm writes cm_map and cm_faces and the two
   "Enterprise PM System · …" names into confirmed_items. An edit after confirmation takes the names out again.
   The group's Enterprise OKRs are read from the member's own Unit 3 page (read only; nothing is typed again). */
var U6_LENS='u3m1_lens5',U6_U3_LENS='u2m1_lens2';
var U6_MAPF=[['contrib','Required functional contribution'],['hos','Human Operating System · required contribution'],['hosm','Human Operating System · performance measure'],['esrg','Required ESRG contribution'],['esrgm','ESRG measure or evidence']];
var U6_FACES=[['F','Foster a Results Culture'],['A','Align Performance'],['C','Create Measurement Transparency'],['E','Embed Shared Accountability'],['S','Support Continuous Development']];
var U6P=[['map','S2R® Contribution Map™','Enterprise PM System · Contribution Map','cm_map'],['faces','FACES Application','Enterprise PM System · FACES Application','cm_faces']];
var U6_IDS=(function(){var a=['kr','kr_obj'];for(var n=1;n<=4;n++){a.push('f'+n+'_name');U6_MAPF.forEach(function(f){a.push('f'+n+'_'+f[0]);});U6_FACES.forEach(function(f){a.push('f'+n+'_'+f[0]);});}return a;})();
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
function u6norm(w){var o={};U6_IDS.forEach(function(id){o[id]=(w&&typeof w[id]==='string')?w[id]:'';});return o;}
function u6val(id){return String(U6.w[id]||'').trim();}
function u6Step(i){
  var tabs=document.querySelectorAll('#mod4 .step-tab'),panels=document.querySelectorAll('#mod4 .step-panel');
  tabs.forEach(function(t,j){t.classList.toggle('active',j===i);});panels.forEach(function(p,j){p.classList.toggle('active',j===i);});
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
/* Function 4 is optional: it counts once any of its Activity 1 entries holds text. */
function u6fnUsed(n){if(n<4)return true;if(u6val('f4_name'))return true;return U6_MAPF.some(function(f){return !!u6val('f4_'+f[0]);});}
function u6fnName(n){return u6val('f'+n+'_name')||('Function '+n);}
/* The Capstone text of one part. */
function u6Text(part){
  var out=[];
  if(part==='map'){if(u6val('kr_obj'))out.push('Enterprise Objective: '+u6val('kr_obj'));}
  out.push('Enterprise Key Result: '+u6val('kr'));
  for(var n=1;n<=4;n++){
    if(!u6fnUsed(n))continue;
    out.push('');out.push('Function '+n+' · '+u6val('f'+n+'_name'));
    if(part==='map')U6_MAPF.forEach(function(f){out.push(f[1]+': '+u6val('f'+n+'_'+f[0]));});
    else U6_FACES.forEach(function(f){out.push(f[0]+' · '+f[1]+': '+u6val('f'+n+'_'+f[0]));});
  }
  return out.join('\n');
}
function u6RecordText(){return U6P.map(function(p){return p[1].toUpperCase()+'\n'+u6Text(p[0]);}).join('\n\n');}
function u6Fill(){
  U6_IDS.forEach(function(id){var el=u6el('u6_'+id);if(!el||el.tagName==='SELECT')return;el.value=U6.w[id]||'';});
  u6KrDraw();u6NamesDraw();
}
function u6In(id,val){
  U6.w[id]=String(val===undefined||val===null?'':val);
  if(id==='kr_obj'){var ob=null;U6.okrs.forEach(function(x){if(x.obj===U6.w.kr_obj)ob=x;});if(!ob||ob.krs.indexOf(U6.w.kr)<0)U6.w.kr='';}
  if(id==='kr'&&U6.w.kr&&!U6.w.kr_obj){var o=null;U6.okrs.forEach(function(x){if(x.krs.indexOf(U6.w.kr)>=0)o=x;});U6.w.kr_obj=o?o.obj:'';}
  if(u6drop())u6later('conf',function(){u6save('confirmed_items',U6.conf);},600);
  u6msg('u6Msg','');
  if(id==='kr'||id==='kr_obj')u6KrDraw();
  if(/^f\d_/.test(id))u6NamesDraw();
  u6later('rec',u6RecDraw,300);
  u6later('save',async function(){await u6save('__cm_work',U6.w);await u6save('cm_record',u6RecordText());},800);
}
/* Step 1: the Key Result the group chose, shown above Step 2 and in Activity 2. */
function u6KrDraw(){
  var ob=u6val('kr_obj'),v=u6val('kr'),os=u6el('u6_obj'),ks=u6el('u6_kr'),cur=null;
  U6.okrs.forEach(function(o){if(o.obj===ob)cur=o;});
  if(os){
    var oo=['<option value="">Choose an Objective…</option>'],seen=false;
    U6.okrs.forEach(function(o){if(o.obj===ob)seen=true;oo.push('<option value="'+u6esc(o.obj)+'"'+(o.obj===ob?' selected':'')+'>'+u6esc(o.obj)+'</option>');});
    if(ob&&!seen)oo.push('<option value="'+u6esc(ob)+'" selected>'+u6esc(ob)+'</option>');
    os.innerHTML=oo.join('');os.disabled=!(U6.okrs.length||ob);
  }
  if(ks){
    var ko=['<option value="">'+(ob?'Choose a Key Result…':'Choose an Objective first…')+'</option>'],kseen=false;
    (cur?cur.krs:[]).forEach(function(k){if(k===v)kseen=true;ko.push('<option value="'+u6esc(k)+'"'+(k===v?' selected':'')+'>'+u6esc(k)+'</option>');});
    if(v&&!kseen)ko.push('<option value="'+u6esc(v)+'" selected>'+u6esc(v)+'</option>');
    ks.innerHTML=ko.join('');ks.disabled=!(cur||v);
  }
  var html=v?((ob?'<b>Enterprise Objective</b>'+u6esc(ob)+'<br><br>':'')+'<b>Enterprise Key Result</b>'+u6esc(v)):'<b>Enterprise Key Result</b><i>Choose your Objective and Key Result in Activity 1, Step 1.</i>';
  ['u6KrShow','u6KrShow2'].forEach(function(id){var el=u6el(id);if(el)el.innerHTML=html;});
}
/* Activity 2 shows the function names given in Activity 1; Function 4 appears only when it is used. */
function u6NamesDraw(){
  for(var n=1;n<=4;n++){
    var nm=u6val('f'+n+'_name');
    document.querySelectorAll('.u6-fn'+n+'-t').forEach(function(el){el.textContent=nm?'· '+nm:'';});
  }
  var fx=u6el('u6fx4');if(fx)fx.style.display=u6fnUsed(4)?'':'none';
}
function u6Open(){
  var open=[];
  if(!u6val('kr_obj'))open.push('Step 1 · the Objective');
  if(!u6val('kr'))open.push('Step 1 · the enterprise Key Result');
  for(var n=1;n<=4;n++){
    if(!u6fnUsed(n))continue;
    var m=(u6val('f'+n+'_name')?0:1)+U6_MAPF.filter(function(f){return !u6val('f'+n+'_'+f[0]);}).length;
    if(m)open.push('Activity 1 · Function '+n+' ('+m+(m===1?' field':' fields')+' still open)');
  }
  for(var k=1;k<=4;k++){
    if(!u6fnUsed(k))continue;
    var q=U6_FACES.filter(function(f){return !u6val('f'+k+'_'+f[0]);}).length;
    if(q)open.push('Activity 2 · '+u6fnName(k)+' ('+q+(q===1?' FACES box':' FACES boxes')+' still open)');
  }
  return open;
}
function u6RecDraw(){
  var host=u6el('u6Rec');if(!host)return;
  var conf=u6has(),msg=u6el('u6Msg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u6-out"><div class="u6-out-h">Your group&rsquo;s record'+(conf?'<span class="u6-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u6-conf no">Not yet confirmed</span>')+'</div>'+
    U6P.map(function(p,i){
      var rows=[],done=0,total=0;
      rows.push('<div class="u6-rec-t"><strong>Enterprise Key Result:</strong> '+(u6val('kr')?u6esc(u6val('kr')):'<i>to be agreed by your group</i>')+'</div>');
      for(var n=1;n<=4;n++){
        if(!u6fnUsed(n))continue;
        rows.push('<div class="u6-rec-s">Function '+n+(u6val('f'+n+'_name')?' &middot; '+u6esc(u6val('f'+n+'_name')):'')+'</div>');
        (p[0]==='map'?U6_MAPF:U6_FACES).forEach(function(f){
          var v=u6val('f'+n+'_'+f[0]);total++;if(v)done++;
          rows.push('<div class="u6-rec-t"><strong>'+u6esc(p[0]==='map'?f[1]:f[0]+' · '+f[1])+':</strong> '+(v?u6esc(v):'<i>to be agreed by your group</i>')+'</div>');
        });
      }
      return '<details class="u6-rec"><summary>5.'+(i+1)+' &middot; '+u6esc(p[1])+'<span>'+done+' of '+total+' entries</span></summary>'+rows.join('')+'</details>';
    }).join('')+
    '<div class="u6-btnrow"><button type="button" class="u6-b ok" id="u6ConfBtn" onclick="u6Confirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u6-b" onclick="u6Print()">Print</button></div>'+
    '<div class="u6-note" id="u6Msg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u6el('u6Msg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function u6Confirm(){
  var open=u6Open();
  if(open.length){u6RecDraw();u6msg('u6Msg','Before you confirm, complete: '+open.join('; ')+'.');return;}
  clearTimeout(_u6t.save);clearTimeout(_u6t.conf);
  var ok=await u6save('__cm_work',U6.w);
  ok=ok&&(await u6save('cm_record',u6RecordText()));
  for(var i=0;i<U6P.length&&ok;i++)ok=await u6save(U6P[i][3],u6Text(U6P[i][0]));
  if(!ok){u6msg('u6Msg','Not saved. Check your connection, then select Confirm again.');return;}
  U6_NAMES.forEach(function(nm){if(U6.conf.indexOf(nm)<0)U6.conf.push(nm);});
  if(!(await u6save('confirmed_items',U6.conf))){u6drop();u6RecDraw();u6msg('u6Msg','Not saved. Check your connection, then select Confirm again.');return;}
  u6RecDraw();u6msg('u6Msg','✓ Confirmed. Your record is ready for your team’s Capstone Blueprint.','ok');
}
function u6Print(){
  var body=U6P.map(function(p,i){return '<h2>5.'+(i+1)+' · '+u6esc(p[1])+'</h2>'+u6Text(p[0]).split('\n').map(function(l){
    if(!l)return '';var m=l.match(/^(Function \d · .*)$/);if(m)return '<h3>'+u6esc(m[1])+'</h3>';
    var c=l.indexOf(': ');return c>0?'<p><strong>'+u6esc(l.slice(0,c))+':</strong> '+(u6esc(l.slice(c+2))||'—')+'</p>':'<p>'+u6esc(l)+'</p>';}).join('');}).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our Enterprise Performance Management System</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}h3{font-size:13px;margin:14px 0 2px}p{font-size:13px;margin:4px 0}</style></head><body>'+
    '<h1>Our Enterprise Performance Management System</h1><p class="sub">Strategy2Results® · Module 3 · Unit 6 · Section 5 · Capstone work · '+(u6has()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
/* Step 1 · the group's confirmed Enterprise OKRs from Unit 3 (read only). */
function u6OkrHtml(){
  if(!U6.okrs.length)return '<div class="u6-from"><i>Your group&rsquo;s confirmed Enterprise OKRs appear here.</i></div>';
  return U6.okrs.map(function(o){return '<div class="u6-from"><b>Objective</b>'+u6esc(o.obj)+'<ul>'+o.krs.map(function(k){return '<li>'+u6esc(k)+'</li>';}).join('')+'</ul></div>';}).join('');
}
async function u6Bring(manual){
  var host=u6el('u6Okrs');
  if(!window.S2R){if(manual)u6msg('u6BringMsg','The save system is not ready. Reload the page and try again.');return;}
  var u3={};try{u3=await S2R.loadAll(U6_U3_LENS);}catch(e){u3={};}
  var w=u3&&u3.__okr_work,conf=(u3&&Array.isArray(u3.confirmed_items))?u3.confirmed_items:[],found=[];
  if(w&&Array.isArray(w.items))w.items.forEach(function(o){
    if(!o||!String(o.obj||'').trim())return;
    var krs=(o.krs||[]).map(function(k){return k&&String(k.t||'').trim();}).filter(function(k){return !!k;});
    if(krs.length)found.push({obj:String(o.obj).trim(),krs:krs});
  });
  if(!found.length||conf.indexOf('Enterprise OKRs')<0){
    U6.okrs=[];if(host)host.innerHTML=u6OkrHtml();u6KrDraw();
    u6msg('u6BringMsg','No confirmed Enterprise OKRs were found on your Unit 3 page. Confirm your group’s Enterprise OKRs in Unit 3, part 4.2, then select Bring in from my Unit 3 page.');
    return;
  }
  U6.okrs=found;if(host)host.innerHTML=u6OkrHtml();u6KrDraw();
  u6msg('u6BringMsg',manual?'Brought in from your Unit 3 page.':'',manual?'ok':'');
}
function u6Init(responses){
  responses=responses||{};
  U6.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U6.w=u6norm(responses.__cm_work);
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

/* Section 3 · part 3.1.1: select a role card to show its detail; select it again to close it. */
function u6Cxo(card,i){
  var d=document.getElementById('u6cxd'+i),was=card.classList.contains('on');
  document.querySelectorAll('.u6-cx').forEach(function(c){c.classList.remove('on');});
  document.querySelectorAll('.u6-cxd').forEach(function(x){x.classList.remove('on');});
  if(!was){card.classList.add('on');if(d)d.classList.add('on');}
}
