/* ════════════ UNIT 8 · SECTION 5 · APPLYING THE FOUR CONSEQUENCES OF WEAK REVIEW DISCIPLINE (group work, Capstone work) ════════════
   Two decision points against each of the four consequences of part 2.1, for the strategy in the team's Capstone Blueprint.
   Answers save as the participant types (__rd_work, rd_record). Confirm writes rd_warning, rd_accountability, rd_learning and rd_credibility
   and the four "Review Discipline · …" names into confirmed_items. An edit after confirmation takes the names out again. */
var U8_LENS='u3m2_lens7';
var U8F=/*FIELDS*/[];
var U8P=/*PARTS*/[];
var U8={conf:[],w:{},ready:false};
var U8_NAMES=U8P.map(function(p){return p[2];});
function u8el(id){return document.getElementById(id);}
function u8esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u8msg(id,text,cls){var m=u8el(id);if(!m)return;m.textContent=text||'';m.className='u8-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u8save(k,val){
  if(!window.S2R){console.warn('[unit3_m2_lens7_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U8_LENS,k,val);}catch(e){console.error('[unit3_m2_lens7_p] save failed for '+k,e);return false;}
}
var _u8t={};
function u8later(name,fn,ms){clearTimeout(_u8t[name]);_u8t[name]=setTimeout(fn,ms||700);}
function u8has(){return U8_NAMES.every(function(nm){return U8.conf.indexOf(nm)>=0;});}
function u8drop(){var ch=false;U8_NAMES.forEach(function(nm){var i=U8.conf.indexOf(nm);if(i>=0){U8.conf.splice(i,1);ch=true;}});return ch;}
function u8norm(w){var o={};U8F.forEach(function(f){o[f[0]]=(w&&typeof w[f[0]]==='string')?w[f[0]]:'';});return o;}
function u8val(id){return String(U8.w[id]||'').trim();}
function u8score(id){var v=u8val(id);if(!/^\d{1,2}$/.test(v))return null;var n=Number(v);return (n>=1&&n<=10)?n:null;}
function u8Step(i){
  var root=u8el('u8S5');if(!root)return;
  var tabs=root.querySelectorAll('.step-tab'),panels=root.querySelectorAll('.step-panel');
  tabs.forEach(function(t,j){t.classList.toggle('active',j===i);});panels.forEach(function(p,j){p.classList.toggle('active',j===i);});
  if(tabs[i])tabs[i].scrollIntoView({behavior:'smooth',block:'start'});
}
function u8bad(f){return !u8val(f[0]);}
/* The text of one part, as it is written into the Capstone. */
function u8Text(part){return U8F.filter(function(f){return f[2]===part;}).map(function(f){return f[1]+': '+u8val(f[0]);}).join('\n');}
function u8Record(){return U8P.map(function(p){return p[4].toUpperCase()+'\n'+u8Text(p[0]);}).join('\n\n');}
function u8Fill(){U8F.forEach(function(f){var el=u8el('u8_'+f[0]);if(el)el.value=U8.w[f[0]]||'';});}
function u8In(id,val){
  U8.w[id]=String(val===undefined||val===null?'':val);
  if(u8drop())u8later('conf',function(){u8save('confirmed_items',U8.conf);},600);
  u8msg('u8Msg','');
  u8later('rec',u8RecDraw,300);
  u8later('save',async function(){await u8save('__rd_work',U8.w);await u8save('rd_record',u8Record());},800);
}
function u8Open(){
  var open=[];
  U8P.forEach(function(p){
    var n=U8F.filter(function(f){return f[2]===p[0]&&u8bad(f);}).length;
    if(n)open.push(p[4]+' ('+n+(n===1?' entry':' entries')+' still open)');
  });
  return open;
}
function u8RecDraw(){
  var host=u8el('u8Rec');if(!host)return;
  var conf=u8has(),msg=u8el('u8Msg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u8-out"><div class="u8-out-h">Your group&rsquo;s record'+(conf?'<span class="u8-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u8-conf no">Not yet confirmed</span>')+'</div>'+
    U8P.map(function(p){
      var fs=U8F.filter(function(f){return f[2]===p[0];}),done=fs.filter(function(f){return !u8bad(f);}).length;
      var lines=u8Text(p[0]).split('\n').map(function(l){
        if(!l)return '<div class="u8-rec-s">&nbsp;</div>';
        var i=l.indexOf(': ');var a=i>=0?l.slice(0,i):l,b=i>=0?l.slice(i+2):'';
        return '<div class="u8-rec-t"><strong>'+u8esc(a)+':</strong> '+(b.trim()?u8esc(b):'<i>to be agreed by your group</i>')+'</div>';
      }).join('');
      var extra='';
      return '<details class="u8-rec"><summary>'+u8esc(p[4])+'<span>'+done+' of '+fs.length+' entries'+extra+'</span></summary>'+lines+'</details>';
    }).join('')+
    '<div class="u8-btnrow"><button type="button" class="u8-b ok" id="u8ConfBtn" onclick="u8Confirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u8-b" onclick="u8Print()">Print</button></div>'+
    '<div class="u8-note" id="u8Msg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u8el('u8Msg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
async function u8Confirm(){
  var open=u8Open();
  if(open.length){u8RecDraw();u8msg('u8Msg','Before you confirm, complete: '+open.join('; ')+'.');return;}
  clearTimeout(_u8t.save);clearTimeout(_u8t.conf);
  var ok=await u8save('__rd_work',U8.w);
  ok=ok&&(await u8save('rd_record',u8Record()));
  for(var i=0;i<U8P.length&&ok;i++)ok=await u8save(U8P[i][3],u8Text(U8P[i][0]));
  if(!ok){u8msg('u8Msg','Not saved. Check your connection, then select Confirm again.');return;}
  U8_NAMES.forEach(function(nm){if(U8.conf.indexOf(nm)<0)U8.conf.push(nm);});
  if(!(await u8save('confirmed_items',U8.conf))){u8drop();u8RecDraw();u8msg('u8Msg','Not saved. Check your connection, then select Confirm again.');return;}
  u8RecDraw();u8msg('u8Msg','✓ Confirmed. Your record is ready for your team’s Capstone Blueprint.','ok');
}
function u8Print(){
  var body=U8P.map(function(p){
    return '<h2>'+u8esc(p[4])+'</h2>'+u8Text(p[0]).split('\n').map(function(l){
      if(!l)return '';
      var i=l.indexOf(': ');return '<p><strong>'+u8esc(i>=0?l.slice(0,i):l)+':</strong> '+(i>=0&&l.slice(i+2).trim()?u8esc(l.slice(i+2)):'—')+'</p>';
    }).join('');
  }).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our decision points for review discipline</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px}h3{font-size:13px;margin:14px 0 2px}p{font-size:13px;margin:4px 0;white-space:pre-wrap}</style></head><body>'+
    '<h1>Our decision points for review discipline</h1><p class="sub">Strategy2Results® · Module 3 · Unit 8 · Section 5 · Capstone work · '+(u8has()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
function u8Init(responses){
  responses=responses||{};
  U8.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U8.w=u8norm(responses.__rd_work);
  U8.ready=true;
  u8Fill();u8RecDraw();
}
document.addEventListener('DOMContentLoaded',function(){
  U8.w=u8norm(null);
  var root=u8el('u8S5');
  if(root){
    root.addEventListener('input',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u8');if(id&&ev.target.tagName!=='SELECT')u8In(id,ev.target.value);});
    root.addEventListener('change',function(ev){var id=ev.target&&ev.target.getAttribute&&ev.target.getAttribute('data-u8');if(id&&ev.target.tagName==='SELECT')u8In(id,ev.target.value);});
  }
  u8Fill();u8RecDraw();
});

/* Part 3.2 · the CXO cards */
function showU8Cxo(card,id){
  document.querySelectorAll('.u8-cx-card').forEach(function(c){c.classList.toggle('active',c===card);});
  document.querySelectorAll('.u8-cx-detail').forEach(function(d){d.classList.toggle('visible',d.id===id);});
}
