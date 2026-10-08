/* ════════════ UNIT 5 THREE-WAY MATCH (October 2026) · PARTICIPANT TOOLS ════════════
   Section 5 · Step 1: the group's confirmed Start and Stop lists, read from the member's own Unit 3 page (read only; nothing is saved here).
   Section 5 · Step 4: the group's three agreed entries are Capstone work. Confirm writes the three names into confirmed_items;
   an edit after confirmation takes them out again. Print gives a copy of the record. No other saving is changed. */
var U5_LENS='u3m1_lens4',U5_U3_LENS='u2m1_lens2';
var U5={conf:[],ready:false};
var SYN_KEYS=['syn_missing_compass','syn_strong_compass','syn_sequence'];
var SYN_NAMES=['Synthesis · Underactivated COMPASS Domain(s)','Synthesis · Where Alignment Is Strong','Synthesis · Agreed Sequence'];
var SYN_LABELS=['Most Frequently Underactivated COMPASS Domain(s)','Shared Patterns — Where Alignment Is Already Strong','Changes Landing on the Same Group, and the Sequence the Team Agrees'];
function u5el(id){return document.getElementById(id);}
function u5esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function u5msg(id,text,cls){var m=u5el(id);if(!m)return;m.textContent=text||'';m.className='u5-note'+(cls?' '+cls:'');m.style.display=text?'block':'none';}
async function u5save(k,val){
  if(!window.S2R){console.warn('[unit3_m1_lens4_p] S2R helper not loaded');return false;}
  try{return await S2R.save(U5_LENS,k,val);}catch(e){console.error('[unit3_m1_lens4_p] save failed for '+k,e);return false;}
}

/* ── Step 1 · the group's confirmed Start and Stop lists from Unit 3 ──────────────────────────── */
function u5KissHtml(start,stop){
  var box=function(label,val){return '<div class="u5-from"><b>'+label+'</b>'+(String(val||'').trim()?u5esc(val):'<i>Your group&rsquo;s confirmed list appears here.</i>')+'</div>';};
  return '<div class="u5-u3-grid">'+box('Start &middot; practices to introduce',start)+box('Stop &middot; practices to end',stop)+'</div>';
}
async function u5Bring(manual){
  var host=u5el('u5KissP');if(!host)return;
  if(!window.S2R){if(manual)u5msg('u5BringMsg','The save system is not ready. Reload the page and try again.');return;}
  var u3={};try{u3=await S2R.loadAll(U5_U3_LENS);}catch(e){u3={};}
  var conf=(u3&&Array.isArray(u3.confirmed_items))?u3.confirmed_items:[];
  var start=(u3&&typeof u3.kiss_start==='string')?u3.kiss_start:'',stop=(u3&&typeof u3.kiss_stop==='string')?u3.kiss_stop:'';
  if(conf.indexOf('KISS · Start')<0||conf.indexOf('KISS · Stop')<0||!start.trim()||!stop.trim()){
    host.innerHTML=u5KissHtml('','');
    u5msg('u5BringMsg','No confirmed KISS map was found on your Unit 3 page. Confirm your group’s KISS map in Unit 3, part 4.1, then select Bring in from my Unit 3 page.');
    return;
  }
  host.innerHTML=u5KissHtml(start,stop);
  u5msg('u5BringMsg',manual?'Brought in from your Unit 3 page.':'',manual?'ok':'');
}

/* ── Step 4 · Capstone work: record, Confirm, Print ───────────────────────────────────────────── */
function synVal(i){var t=u5el(SYN_KEYS[i]);return t?String(t.value||''):'';}
function synConfirmed(){return SYN_NAMES.every(function(nm){return U5.conf.indexOf(nm)>=0;});}
function synRecordHtml(){
  return '<div class="u5-rec">'+SYN_LABELS.map(function(l,i){
    var v=synVal(i).trim();
    return '<div class="u5-rec-s">'+u5esc(l)+'</div><div class="u5-rec-t">'+(v?u5esc(v):'<i>to be agreed by your group</i>')+'</div>';
  }).join('')+'</div>';
}
function renderSyn(){
  var host=u5el('synOutP');if(!host)return;
  var conf=synConfirmed(),msg=u5el('synMsg'),keep=msg?[msg.textContent,msg.className,msg.style.display]:null;
  host.innerHTML='<div class="u5-out"><div class="u5-out-h">Your group&rsquo;s record'+
    (conf?'<span class="u5-conf yes">Confirmed &middot; into your Capstone</span>':'<span class="u5-conf no">Not yet confirmed</span>')+'</div>'+
    synRecordHtml()+
    '<div class="u5-btnrow"><button type="button" class="u5-b ok" onclick="synConfirm()">'+(conf?'Confirmed &#10003;':'Confirm')+'</button><button type="button" class="u5-b" onclick="synPrint()">Print</button></div>'+
    '<div class="u5-note" id="synMsg" style="display:none;"></div></div>';
  if(keep&&keep[0]){var m=u5el('synMsg');m.textContent=keep[0];m.className=keep[1];m.style.display=keep[2];}
}
var _synPaint=null,_synConfTimer=null;
function synEdited(){
  if(synConfirmed()){
    SYN_NAMES.forEach(function(nm){var i=U5.conf.indexOf(nm);if(i>=0)U5.conf.splice(i,1);});
    clearTimeout(_synConfTimer);_synConfTimer=setTimeout(function(){u5save('confirmed_items',U5.conf);},600);
    u5msg('synMsg','');
  }
  clearTimeout(_synPaint);_synPaint=setTimeout(renderSyn,350);
}
async function synConfirm(){
  var open=SYN_LABELS.filter(function(l,i){return !synVal(i).trim();});
  if(open.length){renderSyn();u5msg('synMsg','Complete all three group entries before you confirm. Still open: '+open.join('; ')+'.');return;}
  clearTimeout(_synConfTimer);
  var ok=true;
  for(var i=0;i<SYN_KEYS.length;i++){ok=(await u5save(SYN_KEYS[i],synVal(i)))&&ok;}
  if(!ok){u5msg('synMsg','Not saved. Check your connection, then select Confirm again.');return;}
  SYN_NAMES.forEach(function(nm){if(U5.conf.indexOf(nm)<0)U5.conf.push(nm);});
  if(!(await u5save('confirmed_items',U5.conf))){
    SYN_NAMES.forEach(function(nm){var i=U5.conf.indexOf(nm);if(i>=0)U5.conf.splice(i,1);});
    renderSyn();u5msg('synMsg','Not saved. Check your connection, then select Confirm again.');return;
  }
  renderSyn();u5msg('synMsg','✓ Confirmed. Your group’s outputs are ready for your team’s Capstone Blueprint.','ok');
}
function synPrint(){
  var body=SYN_LABELS.map(function(l,i){var v=synVal(i).trim();return '<h2>'+u5esc(l)+'</h2><p>'+(v?u5esc(v).replace(/\n/g,'<br>'):'—')+'</p>';}).join('');
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Unit 5 · Plenary Synthesis record</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}.sub{color:#555;font-size:13px;margin:0 0 18px}h2{color:#043f2f;font-size:15px;margin:22px 0 6px;border-bottom:2px solid #c9a84c;padding-bottom:4px;page-break-after:avoid}p{font-family:Arial,sans-serif;font-size:13px;margin:0 0 8px}</style></head><body>'+
    '<h1>Plenary Synthesis Record</h1><p class="sub">Strategy2Results® · Module 3 · Unit 5 · Section 5 · Step 4 · Capstone work · '+(synConfirmed()?'confirmed':'not yet confirmed')+'</p>'+body+'</body></html>';
  var w=window.open('','_blank');if(!w){window.print();return;}
  w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}

/* ── Start: draw the tools empty, then fill them from the saved answers ───────────────────────── */
function u5Init(responses){
  responses=responses||{};
  U5.conf=Array.isArray(responses.confirmed_items)?responses.confirmed_items.slice():[];
  U5.ready=true;
  renderSyn();
  u5Bring(false);
}
document.addEventListener('DOMContentLoaded',function(){
  SYN_KEYS.forEach(function(k){var t=u5el(k);if(t)t.addEventListener('input',synEdited);});
  var k=u5el('u5KissP');if(k)k.innerHTML=u5KissHtml('','');
  renderSyn();
});
