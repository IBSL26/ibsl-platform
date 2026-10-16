/* ════════════ UNIT 9 · SECTION 5 · THE STRATEGIC UNCLOGGING CLINIC (group work, Capstone work) ════════════
   One original work-based challenge, taken through parts 5.1 to 5.4. Part 5.1 shows the group's Unit 7 Key Results for reference
   (u3m1_lens6, __ex_work o1_kr/o1_owner/o2_kr/o2_owner). Answers save as the participant types (__uc_work, uc_record).
   Confirm writes uc_challenge, uc_clog, uc_lever, uc_review_realign, uc_restore (Capstone boxes 9A to 9E) and the five
   "Unclogging · …" names into confirmed_items. An edit after confirmation takes the names out again. */
var U9_LENS='u3m2_lens8';
var U9F=/*FIELDS*/[];
var U9P=/*PARTS*/[];
var U9={conf:[],w:{},ready:false};
var U9_NAMES=U9P.map(function(p){return p[2];});
function u9el(id){return document.getElementById(id);}
function u9esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u9msg(id,text,cls){var m=u9el(id);if(!m)return;m.textContent=text||'';m.className='u9-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u9save(k,val){
  if(!window.S2R){console.warn('[unit3_m2_lens8_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U9_LENS,k,val);}catch(e){console.error('[unit3_m2_lens8_p] save failed for '+k,e);return false;}
}
var _u9t={};
function u9later(name,fn,ms){clearTimeout(_u9t[name]);_u9t[name]=setTimeout(fn,ms||700);}
function u9has(){return U9_NAMES.every(function(nm){return U9.conf.indexOf(nm)>=0;});}
function u9drop(){var ch=false;U9_NAMES.forEach(function(nm){var i=U9.conf.indexOf(nm);if(i>=0){U9.conf.splice(i,1);ch=true;}});return ch;}
function u9norm(w){var o={};U9F.forEach(function(f){o[f[0]]=(w&&typeof w[f[0]]==='string')?w[f[0]]:'';});return o;}
function u9val(id){return String(U9.w[id]||'').trim();}
function u9Step(i){
  var root=u9el('u9S5');if(!root)return;
  var tabs=root.querySelectorAll('.step-tab'),panels=root.querySelectorAll('.step-panel');
  tabs.forEach(function(t,j){t.classList.toggle('active',j===i);});panels.forEach(function(p,j){p.classList.toggle('active',j===i);});
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
function u9bad(f){return !f[3]&&!u9val(f[0]);}
/* The text of one step, as it is written into the Capstone. Optional entries left empty are left out. */
function u9Text(part){return U9F.filter(function(f){return f[2]===part&&(!f[3]||u9val(f[0]));}).map(function(f){return f[1]+': '+u9val(f[0]);}).join('\n');}
function u9Record(){return U9P.map(function(p){return p[4].toUpperCase()+'\n'+u9Text(p[0]);}).join('\n\n');}
function u9Fill(){U9F.forEach(function(f){var el=u9el('u9_'+f[0]);if(el)el.value=U9.w[f[0]]||'';});}
function u9In(id,val){
  U9.w[id]=String(val===undefined||val===null?'':val);
  if(u9drop())u9later('conf',function(){u9save('confirmed_items',U9.conf);},600);
  u9msg('u9Msg','');
  u9later('rec',u9RecDraw,300);
  u9later('save',async function(){await u9save('__uc_work',U9.w);await u9save('uc_record',u9Record());},800);
}
function u9Open(){
  var open=[];
  U9P.forEach(function(p){
    var n=U9F.filter(function(f){return f[2]===p[0]&&u9bad(f);}).length;
    if(n)open.push(p[4]+' ('+n+(n===1?' entry':' entries')+' still open)');
  });
  return open;
}
function u9RecDraw(){
  var host=u9el('u9Rec');if(!host)return;
  var conf=u9has(),msg=u9el('u9Msg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u9-out"><div class="u9-out-h">Your group&rsquo;s record'+(conf?'<span class="u9-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u9-conf no">Not yet confirmed</span>')+'</div>'+
    U9P.map(function(p){
      var fs=U9F.filter(function(f){return f[2]===p[0]&&!f[3];}),done=fs.filter(function(f){return !u9bad(f);}).length;
      var lines=U9F.filter(function(f){return f[2]===p[0]&&(!f[3]||u9val(f[0]));}).map(function(f){
        var b=u9val(f[0]);
        return '<div class="u9-rec-t"><strong>'+u9esc(f[1])+':</strong> '+(b?u9esc(b):'<i>to be agreed by your group</i>')+'</div>';
      }).join('');
      return '<details class="u9-rec"><summary>'+u9esc(p[4])+'<span>'+done+' of '+fs.length+' entries</span></summary>'+lines+'</details>';
    }).join('')+
    '<div class="u9-btnrow"><button type="button" class="u9-b ok" id="u9ConfBtn" onclick="u9Confirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u9-b" onclick="u9Print()">Print</button></div>'+
    '<div class="u9-note" id="u9Msg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u9el('u9Msg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function u9Confirm(){
  var open=u9Open();
  if(open.length){u9RecDraw();u9msg('u9Msg','Before you confirm, complete: '+open.join('; ')+'.');return;}
  clearTimeout(_u9t.save);clearTimeout(_u9t.conf);
  var ok=await u9save('__uc_work',U9.w);
  ok=ok&&(await u9save('uc_record',u9Record()));
  for(var i=0;i<U9P.length&&ok;i++)ok=await u9save(U9P[i][3],u9Text(U9P[i][0]));
  if(!ok){u9msg('u9Msg','Not saved. Check your connection, then select Confirm again.');return;}
  U9_NAMES.forEach(function(nm){if(U9.conf.indexOf(nm)<0)U9.conf.push(nm);});
  if(!(await u9save('confirmed_items',U9.conf))){u9drop();u9RecDraw();u9msg('u9Msg','Not saved. Check your connection, then select Confirm again.');return;}
  u9RecDraw();u9msg('u9Msg','✓ Confirmed. Your record is ready for your team’s Capstone Blueprint.','ok');
}
function u9Print(){
  var body=U9P.map(function(p){
    return '<h2>'+u9esc(p[4])+'</h2>'+u9Text(p[0]).split('\n').map(function(l){
      if(!l)return '';
      var i=l.indexOf(': ');return '<p><strong>'+u9esc(i>=0?l.slice(0,i):l)+':</strong> '+(i>=0&&l.slice(i+2).trim()?u9esc(l.slice(i+2)):'—')+'</p>';
    }).join('');
  }).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our Strategic Unclogging Clinic</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}p{font-size:13px;margin:4px 0;white-space:pre-wrap}</style></head><body>'+
    '<h1>Our Strategic Unclogging Clinic</h1><p class="sub">Strategy2Results® · Module 3 · Unit 9 · Section 5 · Capstone work · '+(u9has()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
/* The group's Unit 7 Key Results, read only, for reference in part 5.1. */
async function u9Earlier(){
  var kr=u9el('u9Krs');
  if(!window.S2R||!kr)return;
  try{
    var u7=await S2R.loadAll('u3m1_lens6')||{},c7=Array.isArray(u7.confirmed_items)?u7.confirmed_items:[],w7=u7.__ex_work||{};
    if(c7.indexOf('Expectations · Start With the Future')>=0&&(w7.o1_kr||w7.o2_kr)){
      kr.innerHTML=[1,2].map(function(n){
        return '<div class="u9-kr"><div class="u9-kr-n">Key Result '+n+'</div><div class="u9-kr-t">'+u9esc(w7['o'+n+'_kr']||'')+'</div>'+(w7['o'+n+'_owner']?'<div class="u9-kr-o">Owner: '+u9esc(w7['o'+n+'_owner'])+'</div>':'')+'</div>';
      }).join('');
    }else kr.innerHTML='<p class="u9-wait">Your group&rsquo;s two Key Results appear here once your group has confirmed its Unit 7 record (Section 5 of Unit 7).</p>';
  }catch(e){console.warn('[unit3_m2_lens8_p] earlier units not loaded',e);}
}
function u9Init(responses){
  responses=responses||{};
  U9.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U9.w=u9norm(responses.__uc_work);
  U9.ready=true;
  u9Fill();u9RecDraw();u9Earlier();
}
document.addEventListener('DOMContentLoaded',function(){
  U9.w=u9norm(null);
  var root=u9el('u9S5');
  if(root){
    root.addEventListener('input',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u9');if(id&&ev.target.tagName!=='SELECT')u9In(id,ev.target.value);});
    root.addEventListener('change',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u9');if(id&&ev.target.tagName==='SELECT')u9In(id,ev.target.value);});
  }
  u9Fill();u9RecDraw();
});
