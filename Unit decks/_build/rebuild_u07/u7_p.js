/* ════════════ UNIT 7 · SECTION 5 · ESTABLISHING DELIVERY EXPECTATIONS (group work, Capstone work) ════════════
   5.1 · four steps (Start With the Future, Clarify the Delivery Expectation, Identify the Expectations Chain, Confirm Ownership),
   applied to two Objectives with one related Key Result each. The Objectives and Key Results are chosen from drop-down lists
   of the group's confirmed Unit 3 Enterprise OKRs; the SiP statement each one serves is chosen from a drop-down list of the
   group's confirmed Unit 2 SiP statements. Part 4.2 (Portfolio work) takes its Key Result from the same Unit 3 list (ad_kr).
   5.2 · the group's alignment dialogue with the board chair on one Key Result (dg_kr, dg_goal, dg_reality, dg_options, dg_will).
   Answers save as the participant types (__ex_work, ex_record). Confirm writes ex_future, ex_delivery, ex_chain, ex_ownership and ex_dialogue
   and the five "Expectations · …" names into confirmed_items. An edit after confirmation takes the names out again. */
var U7_LENS='u3m1_lens6',U7_U3_LENS='u2m1_lens2',U7_U2_LENS='u2m1_lens1';
var U7F=/*FIELDS*/[];
var U7P=/*PARTS*/[];
var U7_SIP=[['sip_d1_st','SiP · Customer Experience & Value'],['sip_d2_st','SiP · Operational Capability & Execution Rhythm'],['sip_d3_st','SiP · People & Culture Dynamics'],['sip_d4_st','SiP · Enterprise Value Creation']];
var U7={conf:[],w:{},okrs:[],sip:[],ad:'',ready:false};
var U7_NAMES=U7P.map(function(p){return p[2];});
function u7el(id){return document.getElementById(id);}
function u7esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u7msg(id,text,cls){var m=u7el(id);if(!m)return;m.textContent=text||'';m.className='u7-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u7save(k,val){
  if(!window.S2R){console.warn('[unit3_m1_lens6_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U7_LENS,k,val);}catch(e){console.error('[unit3_m1_lens6_p] save failed for '+k,e);return false;}
}
var _u7t={};
function u7later(name,fn,ms){clearTimeout(_u7t[name]);_u7t[name]=setTimeout(fn,ms||700);}
function u7has(){return U7_NAMES.every(function(nm){return U7.conf.indexOf(nm)>=0;});}
function u7drop(){var ch=false;U7_NAMES.forEach(function(nm){var i=U7.conf.indexOf(nm);if(i>=0){U7.conf.splice(i,1);ch=true;}});return ch;}
function u7norm(w){var o={};U7F.forEach(function(f){o[f[0]]=(w&&typeof w[f[0]]==='string')?w[f[0]]:'';});return o;}
function u7val(id){return String(U7.w[id]||'').trim();}
function u7score(id){var v=u7val(id);if(!/^\d{1,2}$/.test(v))return null;var n=Number(v);return (n>=1&&n<=10)?n:null;}
function u7Step(i){
  var tabs=document.querySelectorAll('#mod4 .step-tab'),panels=document.querySelectorAll('#mod4 .step-panel');
  tabs.forEach(function(t,j){t.classList.toggle('active',j===i);});panels.forEach(function(p,j){p.classList.toggle('active',j===i);});
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
/* An entry counts as open when it is empty, or when a score is outside 1 to 10. The three follow-up entries are needed only when the first score is below 9. */
function u7needs(f){
  if(f[4]==='o'||f[4]==='m'){var s=u7score(f[3]==='Objective 1'?'o1_score':'o2_score');return s!==null&&s<9;}
  return true;
}
function u7bad(f){
  var v=u7val(f[0]);
  if(!u7needs(f))return false;
  if(f[4]==='n'||f[4]==='m')return u7score(f[0])===null;
  return !v;
}
/* The text of one part, as it is written into the Capstone: for each Objective, the Objective and Key Result, then one line for each entry. */
function u7Text(part){
  var out=[];
  if(part==='dialogue'){
    out.push('Key Result: '+u7val('dg_kr'));
    U7F.filter(function(f){return f[2]===part&&f[4]!=='k';}).forEach(function(f){out.push(f[1]+': '+u7val(f[0]));});
    return out.join('\n');
  }
  [1,2].forEach(function(n){
    if(out.length)out.push('');
    out.push('OBJECTIVE '+n+': '+u7val('o'+n+'_obj'));
    out.push('Key Result: '+u7val('o'+n+'_kr'));
    U7F.filter(function(f){return f[2]===part&&f[3]==='Objective '+n;}).forEach(function(f){
      var v=u7val(f[0]);if(!v&&!u7needs(f))return;
      out.push(f[1]+': '+v);
    });
  });
  return out.join('\n');
}
function u7Record(){return U7P.map(function(p){return p[4].toUpperCase()+'\n'+u7Text(p[0]);}).join('\n\n');}
function u7Fill(){
  U7F.forEach(function(f){var el=u7el('u7_'+f[0]);if(!el||f[4]==='k')return;el.value=U7.w[f[0]]||'';});
  u7SelDraw();
}
function u7In(id,val){
  U7.w[id]=String(val===undefined||val===null?'':val);
  var m=/^o([12])_obj$/.exec(id);
  if(m){var o=U7.okrs.filter(function(x){return x.obj===U7.w[id];})[0];if(!o||o.krs.indexOf(U7.w['o'+m[1]+'_kr'])<0)U7.w['o'+m[1]+'_kr']='';}
  if(u7drop())u7later('conf',function(){u7save('confirmed_items',U7.conf);},600);
  u7msg('u7Msg','');
  if(/^(o[12]_(obj|kr|sipst)|dg_kr)$/.test(id))u7SelDraw();
  u7later('rec',u7RecDraw,300);
  u7later('save',async function(){await u7save('__ex_work',U7.w);await u7save('ex_record',u7Record());},800);
}
/* The two Objectives and their Key Results: the choosers in Step 1, and the same text shown at the head of each Objective in every step. */
function u7SelDraw(){
  var dv=u7val('dg_kr'),ds=u7el('u7_dg_kr');
  if(ds){
    var dopts=['<option value="">Choose a Key Result…</option>'],dseen=false;
    U7.okrs.forEach(function(o){dopts.push('<optgroup label="'+u7esc(o.obj)+'">'+o.krs.map(function(k){if(k===dv)dseen=true;return '<option value="'+u7esc(k)+'"'+(k===dv?' selected':'')+'>'+u7esc(k)+'</option>';}).join('')+'</optgroup>');});
    if(dv&&!dseen)dopts.push('<option value="'+u7esc(dv)+'" selected>'+u7esc(dv)+'</option>');
    ds.innerHTML=dopts.join('');ds.disabled=!(U7.okrs.length||dv);
  }
  [1,2].forEach(function(n){
    var ov=u7val('o'+n+'_obj'),kv=u7val('o'+n+'_kr'),os=u7el('u7_o'+n+'_obj'),ks=u7el('u7_o'+n+'_kr'),seen=false,cur=null;
    if(os){
      var opts=['<option value="">Choose an Objective…</option>'];
      U7.okrs.forEach(function(o){if(o.obj===ov){seen=true;cur=o;}opts.push('<option value="'+u7esc(o.obj)+'"'+(o.obj===ov?' selected':'')+'>'+u7esc(o.obj)+'</option>');});
      if(ov&&!seen)opts.push('<option value="'+u7esc(ov)+'" selected>'+u7esc(ov)+'</option>');
      os.innerHTML=opts.join('');os.disabled=!(U7.okrs.length||ov);
    }
    if(ks){
      var kopts=['<option value="">Choose a Key Result of this Objective…</option>'],kseen=false;
      if(cur)cur.krs.forEach(function(k){if(k===kv)kseen=true;kopts.push('<option value="'+u7esc(k)+'"'+(k===kv?' selected':'')+'>'+u7esc(k)+'</option>');});
      if(kv&&!kseen)kopts.push('<option value="'+u7esc(kv)+'" selected>'+u7esc(kv)+'</option>');
      ks.innerHTML=kopts.join('');ks.disabled=!(cur||kv);
    }
    var sv=u7val('o'+n+'_sipst'),ss=u7el('u7_o'+n+'_sipst');
    if(ss){
      var sopts=['<option value="">Choose a Success in Practice statement…</option>'],sseen=false;
      U7.sip.forEach(function(x){var val=x[0].replace(/^SiP · /,'')+': '+x[1];if(val===sv)sseen=true;sopts.push('<option value="'+u7esc(val)+'"'+(val===sv?' selected':'')+'>'+u7esc(val)+'</option>');});
      if(sv&&!sseen)sopts.push('<option value="'+u7esc(sv)+'" selected>'+u7esc(sv)+'</option>');
      ss.innerHTML=sopts.join('');ss.disabled=!(U7.sip.length||sv);
    }
    document.querySelectorAll('.u7-o'+n+'-obj').forEach(function(el){el.textContent=ov||'Choose Objective '+n+' in Step 1.';});
    document.querySelectorAll('.u7-o'+n+'-kr').forEach(function(el){el.textContent=kv||'Choose its Key Result in Step 1.';});
  });
}
function u7Open(){
  var open=[];
  [1,2].forEach(function(n){if(!u7val('o'+n+'_obj')||!u7val('o'+n+'_kr'))open.push('Objective '+n+' and its Key Result in Step 1');});
  if(u7val('o1_obj')&&u7val('o1_obj')===u7val('o2_obj'))open.push('two different Objectives in Step 1');
  U7P.forEach(function(p,i){
    var n=U7F.filter(function(f){return f[2]===p[0]&&u7bad(f);}).length;
    if(n)open.push(p[4]+' ('+n+(n===1?' entry':' entries')+' still open)');
  });
  return open;
}
function u7RecDraw(){
  var host=u7el('u7Rec');if(!host)return;
  var conf=u7has(),msg=u7el('u7Msg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u7-out"><div class="u7-out-h">Your group&rsquo;s record'+(conf?'<span class="u7-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u7-conf no">Not yet confirmed</span>')+'</div>'+
    U7P.map(function(p,i){
      var fs=U7F.filter(function(f){return f[2]===p[0]&&u7needs(f);}),done=fs.filter(function(f){return !u7bad(f);}).length;
      if(p[0]==='dialogue')return '<details class="u7-rec"><summary>'+u7esc(p[4])+'<span>'+done+' of '+fs.length+' entries</span></summary>'+fs.map(function(f){var v=u7val(f[0]);
        return '<div class="u7-rec-t"><strong>'+u7esc(f[1])+':</strong> '+(v?u7esc(v):'<i>to be agreed by your group</i>')+'</div>';}).join('')+'</details>';
      return '<details class="u7-rec"><summary>'+u7esc(p[4])+'<span>'+done+' of '+fs.length+' entries</span></summary>'+[1,2].map(function(n){
        return '<div class="u7-rec-s">Objective '+n+'</div>'+
          '<div class="u7-rec-t"><strong>Objective:</strong> '+(u7val('o'+n+'_obj')?u7esc(u7val('o'+n+'_obj')):'<i>to be chosen in Step 1</i>')+'</div>'+
          '<div class="u7-rec-t"><strong>Key Result:</strong> '+(u7val('o'+n+'_kr')?u7esc(u7val('o'+n+'_kr')):'<i>to be chosen in Step 1</i>')+'</div>'+
          fs.filter(function(f){return f[3]==='Objective '+n;}).map(function(f){var v=u7val(f[0]);
            return '<div class="u7-rec-t"><strong>'+u7esc(f[1])+':</strong> '+(v?u7esc(v):'<i>to be agreed by your group</i>')+'</div>';}).join('');
      }).join('')+'</details>';
    }).join('')+
    '<div class="u7-btnrow"><button type="button" class="u7-b ok" id="u7ConfBtn" onclick="u7Confirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u7-b" onclick="u7Print()">Print</button></div>'+
    '<div class="u7-note" id="u7Msg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u7el('u7Msg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function u7Confirm(){
  var open=u7Open();
  if(open.length){u7RecDraw();u7msg('u7Msg','Before you confirm, complete: '+open.join('; ')+'.');return;}
  clearTimeout(_u7t.save);clearTimeout(_u7t.conf);
  var ok=await u7save('__ex_work',U7.w);
  ok=ok&&(await u7save('ex_record',u7Record()));
  for(var i=0;i<U7P.length&&ok;i++)ok=await u7save(U7P[i][3],u7Text(U7P[i][0]));
  if(!ok){u7msg('u7Msg','Not saved. Check your connection, then select Confirm again.');return;}
  U7_NAMES.forEach(function(nm){if(U7.conf.indexOf(nm)<0)U7.conf.push(nm);});
  if(!(await u7save('confirmed_items',U7.conf))){u7drop();u7RecDraw();u7msg('u7Msg','Not saved. Check your connection, then select Confirm again.');return;}
  u7RecDraw();u7msg('u7Msg','✓ Confirmed. Your record is ready for your team’s Capstone Blueprint.','ok');
}
function u7Print(){
  var body=U7P.map(function(p,i){
    if(p[0]==='dialogue')return '<h2>'+u7esc(p[4])+'</h2>'+U7F.filter(function(f){return f[2]===p[0];}).map(function(f){var v=u7val(f[0]);
      return '<p><strong>'+u7esc(f[1])+':</strong> '+(v?u7esc(v).replace(/\n/g,'<br>'):'—')+'</p>';}).join('');
    return '<h2>'+u7esc(p[4])+'</h2>'+[1,2].map(function(n){
    return '<h3>Objective '+n+': '+(u7esc(u7val('o'+n+'_obj'))||'—')+'</h3><p><strong>Key Result:</strong> '+(u7esc(u7val('o'+n+'_kr'))||'—')+'</p>'+
      U7F.filter(function(f){return f[2]===p[0]&&f[3]==='Objective '+n&&(u7val(f[0])||u7needs(f));}).map(function(f){var v=u7val(f[0]);
        return '<p><strong>'+u7esc(f[1])+':</strong> '+(v?u7esc(v).replace(/\n/g,'<br>'):'—')+'</p>';}).join('');}).join('');}).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our delivery expectations</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}h3{font-size:13px;margin:14px 0 2px}p{font-size:13px;margin:4px 0}</style></head><body>'+
    '<h1>Our delivery expectations</h1><p class="sub">Strategy2Results® · Module 3 · Unit 7 · Section 5 · Capstone work · '+(u7has()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
/* Part 4.2 · Portfolio work: the Key Result for the alignment dialogue with the board chair (ad_kr), chosen from the Unit 3 list. */
function u7AdDraw(){
  var sel=u7el('ad_kr');if(!sel)return;
  var v=String(U7.ad||''),opts=['<option value="">Choose a Key Result…</option>'],seen=false;
  U7.okrs.forEach(function(o){opts.push('<optgroup label="'+u7esc(o.obj)+'">'+o.krs.map(function(k){if(k===v)seen=true;return '<option value="'+u7esc(k)+'"'+(k===v?' selected':'')+'>'+u7esc(k)+'</option>';}).join('')+'</optgroup>');});
  if(v&&!seen)opts.push('<option value="'+u7esc(v)+'" selected>'+u7esc(v)+'</option>');
  sel.innerHTML=opts.join('');sel.disabled=!(U7.okrs.length||v);
  if(!U7.ready)return;
  u7msg('u7AdMsg',U7.okrs.length||v?'':'No confirmed Enterprise OKRs were found on your Unit 3 page. Confirm your group’s Enterprise OKRs in Unit 3, part 4.2, then reload this page.');
}
async function u7AdSave(v){
  U7.ad=String(v||'');
  var ok=await u7save('ad_kr',U7.ad);
  u7msg('u7AdMsg',ok?'✓ Saved to your portfolio':'Not saved. Check your connection, then choose the Key Result again.',ok?'ok':'');
}
/* The drop-down lists: the group's confirmed Enterprise OKRs (Unit 3) and its confirmed SiP statements (Unit 2), read from the member's own pages. */
async function u7Bring(manual){
  if(!window.S2R){if(manual)u7msg('u7BringMsg','The save system is not ready. Reload the page and try again.');return;}
  var u3={},u2={};
  try{u3=await S2R.loadAll(U7_U3_LENS);}catch(e){u3={};}
  try{u2=await S2R.loadAll(U7_U2_LENS);}catch(e){u2={};}
  var c2=(u2&&Array.isArray(u2.confirmed_items))?u2.confirmed_items:[];
  U7.sip=U7_SIP.filter(function(r){return c2.indexOf(r[1])>=0&&String((u2||{})[r[0]]||'').trim();}).map(function(r){return [r[1],String(u2[r[0]]).trim()];});
  var w=u3&&u3.__okr_work,conf=(u3&&Array.isArray(u3.confirmed_items))?u3.confirmed_items:[],found=[];
  if(w&&Array.isArray(w.items)&&conf.indexOf('Enterprise OKRs')>=0)w.items.forEach(function(o){
    if(!o||!String(o.obj||'').trim())return;
    var krs=(o.krs||[]).map(function(k){return k&&String(k.t||'').trim();}).filter(function(k){return !!k;});
    if(krs.length)found.push({obj:String(o.obj).trim(),krs:krs});
  });
  U7.okrs=found;u7SelDraw();u7AdDraw();
  var miss=[];
  if(!found.length)miss.push('No confirmed Enterprise OKRs were found on your Unit 3 page. Confirm your group’s Enterprise OKRs in Unit 3, part 4.2.');
  if(!U7.sip.length)miss.push('No confirmed Success in Practice statements were found on your Unit 2 page. Confirm your group’s SiP statements in Unit 2.');
  if(miss.length){u7msg('u7BringMsg',miss.join(' ')+' Then select Reload the drop-down lists.');return;}
  u7msg('u7BringMsg',manual?'The drop-down lists are up to date.':'',manual?'ok':'');
}
function u7Init(responses){
  responses=responses||{};
  U7.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U7.w=u7norm(responses.__ex_work);
  U7.ad=typeof responses.ad_kr==='string'?responses.ad_kr:'';
  U7.ready=true;
  u7Fill();u7RecDraw();u7AdDraw();u7Bring(false);
}
document.addEventListener('DOMContentLoaded',function(){
  U7.w=u7norm(null);
  var mod=u7el('mod4');
  if(mod){
    mod.addEventListener('input',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u7');if(id&&ev.target.tagName!=='SELECT')u7In(id,ev.target.value);});
    mod.addEventListener('change',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u7');if(id&&ev.target.tagName==='SELECT')u7In(id,ev.target.value);});
  }
  var ad=u7el('ad_kr');if(ad)ad.addEventListener('change',function(){u7AdSave(ad.value);});
  u7Fill();u7RecDraw();u7AdDraw();
});
