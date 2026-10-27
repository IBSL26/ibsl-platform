/* ── Unit 12 · Section 5 · Our Quarterly Three Lines of Sight (27 Oct 2026) ──
   Group Capstone work on the shared group record (s2r-team.js): the scribe types, every member selects Agree.
   Brought in from the member's own pages: Unit 6 WARD (__cm_work), Unit 10 ESRG scan (es_scanner), Unit 11 consolidated health (oh_cons).
   Saved for the group: __qs_work (the working record) and, once complete, qs_strategic, qs_operational, qs_behavioural, qs_kiss (Capstone 12A-12D). */
var U12_LENS="u4m2_lens11";
var U12_NAMES=["Quarterly Lines of Sight · Strategic","Quarterly Lines of Sight · Operational","Quarterly Lines of Sight · Behavioural","Quarterly Lines of Sight · KISS for Next Quarter"];
var U12_KEYS=["qs_strategic","qs_operational","qs_behavioural","qs_kiss"];
var U12_CAP=["Operational Readiness · FIT","Operational Flow · SIP","Delivery Capacity · AIR","Decision Responsiveness · PAR"];
var U12_CAPN=["Operational Readiness","Operational Flow","Delivery Capacity","Decision Responsiveness"];
var U12_DEC=["Keep","Improve","Stop","Start"];
var U12_LINES=["Strategic","Operational","Behavioural"];
var U12W=u12Blank(),_u12Last={},U12Ready=false;
function u12Blank(){return {quarter:"",src:{kr:"",wp:"",alert:"",rec_i:"",rec_o:"",dec:"",es:["","","",""],h_score:"",h_weak:""},
  s:{result:"",wp:"",raised:"",rec:"",check:""},o:{raised:"",rec:"",owner:"",check:""},b:{raised:"",rec:"",owner:"",check:""},
  kiss:U12_DEC.map(function(d){return {d:d,practice:"",line:"",owner:""};})};}
function u12esc(s){return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function u12el(id){return document.getElementById(id);}
function u12Str(v){return v==null?"":String(v);}
function u12Norm(w){
  var b=u12Blank();if(!w||typeof w!=="object")return b;
  b.quarter=u12Str(w.quarter);
  if(w.src&&typeof w.src==="object")Object.keys(b.src).forEach(function(k){if(k==="es"){if(Array.isArray(w.src.es))for(var i=0;i<4;i++)b.src.es[i]=u12Str(w.src.es[i]);}else b.src[k]=u12Str(w.src[k]);});
  ["s","o","b"].forEach(function(g){Object.keys(b[g]).forEach(function(k){b[g][k]=u12Str(w[g]&&w[g][k]);});});
  if(Array.isArray(w.kiss)&&w.kiss.length)b.kiss=w.kiss.map(function(r){return {d:u12Str(r&&r.d),practice:u12Str(r&&r.practice),line:u12Str(r&&r.line),owner:u12Str(r&&r.owner)};});
  return b;
}
function u12Num(v){var n=parseFloat(String(v).replace(",","."));return isNaN(n)?null:n;}
function u12Band(x){return x>=80?"Healthy & Thriving":x>=60?"Stable but Uneven":x>=40?"Caution Zone":"Unhealthy";}
function u12EsBand(x){return x>=4?"Aligned":x>=3?"Improvement required":x>=2?"Significant constraint":"Critical constraint";}
function u12Low(){var lo=null;U12W.src.es.forEach(function(v,i){var n=u12Num(v);if(n!==null&&(lo===null||n<lo.n))lo={i:i,n:n};});return lo;}
function u12LowText(){var lo=u12Low();if(!lo)return "";return U12_CAPN[lo.i]+" "+lo.n.toFixed(2)+" ("+u12EsBand(lo.n)+")";}
function u12HText(){var h=u12Num(U12W.src.h_score);if(h===null)return "";return h.toFixed(1)+" /100 · "+u12Band(h)+(U12W.src.h_weak.trim()?" · weakest traits: "+U12W.src.h_weak.trim():"");}

/* ── Drawing ── */
function u12Fill(){
  var root=u12el("mod4");if(!root)return;
  root.querySelectorAll("[data-u12]").forEach(function(f){var p=f.getAttribute("data-u12");if(/^kiss\./.test(p))return;var v=u12Get(p);if(f.value!==v)f.value=v;});
  u12DrawKiss();u12DrawChecks();
}
function u12Get(p){var a=p.split("."),o=U12W;for(var i=0;i<a.length;i++){if(o==null)return "";o=o[a[i]];}return u12Str(o);}
function u12Set(p,v){var a=p.split("."),o=U12W;for(var i=0;i<a.length-1;i++){o=o[a[i]];if(o==null)return;}o[a[a.length-1]]=v;}
function u12DrawChecks(){
  var s=u12el("u12SAlert"),o=u12el("u12OLow"),b=u12el("u12BLow");
  if(s)s.innerHTML=U12W.src.alert.trim()?"<strong>A · Alert:</strong> "+u12esc(U12W.src.alert.trim()):"<strong>A · Alert:</strong> bring in your WARD in part 5.2.";
  if(o){var lo=u12Low();o.innerHTML=lo?"<strong>Lowest capability:</strong> "+u12esc(u12LowText())+". Waypoint 4.0 or above; alert below 3.0 · "+(lo.n<3?'<span class="u12-warn">the band raises the alert</span>':'<span class="u12-ok">the band does not raise the alert</span>'):"<strong>Lowest capability:</strong> bring in your ESRG scan in part 5.2.";}
  if(b){var h=u12Num(U12W.src.h_score);b.innerHTML=h!==null?"<strong>Health position:</strong> "+u12esc(u12HText())+". Waypoint 80 or above; alert below 60 · "+(h<60?'<span class="u12-warn">the band raises the alert</span>':'<span class="u12-ok">the band does not raise the alert</span>'):"<strong>Health position:</strong> bring in your consolidated health position in part 5.2.";}
}
function u12DrawKiss(){
  var host=u12el("u12Kiss");if(!host)return;
  host.innerHTML=U12W.kiss.map(function(r,i){
    var dOpt='<option value="">Choose…</option>'+U12_DEC.map(function(d){return '<option'+(r.d===d?' selected':'')+'>'+d+'</option>';}).join("");
    var lOpt='<option value="">Choose…</option>'+U12_LINES.map(function(d){return '<option'+(r.line===d?' selected':'')+'>'+d+'</option>';}).join("");
    return '<div class="u12-krow"><div class="u12-krow-h"><span>Decision '+(i+1)+(r.d?" · "+u12esc(r.d):"")+'</span>'+(U12W.kiss.length>4?'<button type="button" class="u12-del" onclick="u12DelKiss('+i+')">Remove</button>':'')+'</div>'+
      '<div class="u12-grid"><div><label class="fld-label">Decision</label><select class="fld-input" data-u12="kiss.'+i+'.d">'+dOpt+'</select></div>'+
      '<div><label class="fld-label">Line of sight it comes from</label><select class="fld-input" data-u12="kiss.'+i+'.line">'+lOpt+'</select></div></div>'+
      '<label class="fld-label">Practice</label><textarea class="fld-input u12-ta" data-u12="kiss.'+i+'.practice">'+u12esc(r.practice)+'</textarea>'+
      '<label class="fld-label">Owner</label><input class="fld-input" type="text" data-u12="kiss.'+i+'.owner" value="'+u12esc(r.owner)+'"></div>';
  }).join("");
  if(window.S2RTeam&&S2RTeam.redraw)S2RTeam.redraw();
}
function u12AddKiss(){if(window.S2RTeam&&!S2RTeam.isScribe())return;U12W.kiss.push({d:"",practice:"",line:"",owner:""});u12DrawKiss();u12Out();u12RecDraw();}
function u12DelKiss(i){if(window.S2RTeam&&!S2RTeam.isScribe())return;if(U12W.kiss.length<5)return;if(!confirm("Remove Decision "+(i+1)+"?"))return;U12W.kiss.splice(i,1);u12DrawKiss();u12Out();u12RecDraw();}
function u12OnInput(ev){
  var t=ev.target,p=t&&t.getAttribute&&t.getAttribute("data-u12");if(!p)return;
  var a=p.split(".");
  if(a[0]==="kiss"){var r=U12W.kiss[+a[1]];if(!r)return;r[a[2]]=t.value;
    if(a[2]==="d"){var h=t.closest(".u12-krow");var s=h&&h.querySelector(".u12-krow-h span");if(s)s.textContent="Decision "+(+a[1]+1)+(t.value?" · "+t.value:"");}}
  else u12Set(p,t.value);
  if(a[0]==="src")u12DrawChecks();
  u12Out();u12RecDraw();
}

/* ── Bring in from the member's own Unit 6, 10 and 11 pages ── */
function u12Lines(t){var m={};String(t||"").split(/\r?\n/).forEach(function(l){var i=l.indexOf(": ");if(i>0)m[l.slice(0,i).trim()]=l.slice(i+2).trim();});return m;}
async function u12Bring(manual){
  if(window.S2RTeam&&!S2RTeam.isScribe()){if(manual)u12Msg("Only the scribe brings the results onto your group’s page.","warn");return;}
  if(!window.S2R)return;
  var got=[],miss=[];
  var r6={},r10={},r11={};
  try{r6=await S2R.loadAll("u3m1_lens5")||{};}catch(e){r6={};}
  try{r10=await S2R.loadAll("u4m1_lens9")||{};}catch(e){r10={};}
  try{r11=await S2R.loadAll("u4m1_lens10")||{};}catch(e){r11={};}
  var w=r6.__cm_work;if(typeof w==="string"){try{w=JSON.parse(w);}catch(e){w=null;}}
  if(w&&typeof w==="object"&&(w.kr||w.wd_alert||w.wd_dec)){
    var S=U12W.src;S.kr=u12Str(w.kr);
    S.wp=[1,2,3].map(function(n){var d=u12Str(w["wd_w"+n+"d"]).trim(),l=u12Str(w["wd_w"+n+"l"]).trim();return (d||l)?(l+(d?" by "+d:"")):"";}).filter(Boolean).join("\n");
    S.alert=u12Str(w.wd_alert);S.rec_i=u12Str(w.wd_rec_i);S.rec_o=u12Str(w.wd_rec_o);S.dec=u12Str(w.wd_dec);got.push("Unit 6 WARD");
  }else miss.push("Unit 6 WARD");
  if(typeof r10.es_scanner==="string"&&r10.es_scanner.trim()){
    var n=0;String(r10.es_scanner).split(/\r?\n/).forEach(function(l){U12_CAPN.forEach(function(c,i){if(l.indexOf(c+" (")===0){var m=l.match(/Enterprise avg\.\s*([0-9]+(?:\.[0-9]+)?)/);if(m){U12W.src.es[i]=(Math.round(parseFloat(m[1])*100)/100).toFixed(2);n++;}}});});
    if(n)got.push("Unit 10 ESRG scan");else miss.push("Unit 10 ESRG scan");
  }else miss.push("Unit 10 ESRG scan");
  if(typeof r11.oh_cons==="string"&&r11.oh_cons.trim()){
    var L=u12Lines(r11.oh_cons),sc=String(L["Consolidated health score"]||"").match(/([0-9]+(?:\.[0-9]+)?)/);
    if(sc){U12W.src.h_score=sc[1];U12W.src.h_weak=u12Str(L["Two weakest traits"]);got.push("Unit 11 health position");}else miss.push("Unit 11 health position");
  }else miss.push("Unit 11 health position");
  if(!U12W.s.wp.trim()&&U12W.src.wp.trim())U12W.s.wp=U12W.src.wp.split("\n")[0];
  u12Fill();u12Out();u12RecDraw();
  if(manual||got.length)u12Msg((got.length?"Brought in: "+got.join(", ")+". ":"")+(miss.length?"Not found yet: "+miss.join(", ")+" (agreed group work in that unit is needed). The scribe can type these values.":""),miss.length?"warn":"ok");
}
function u12Msg(t,c){var m=u12el("u12BringMsg");if(!m)return;m.textContent=t||"";m.className="u12-note"+(c?" "+c:"");}

/* ── What is still open before the group can agree ── */
function u12Open(){
  var o=[],S=U12W.src;
  if(!U12W.quarter)o.push("the quarter in part 5.2");
  if(!S.kr.trim()||!S.alert.trim()||!S.dec.trim())o.push("the Key Result, alert and Decider in part 5.2");
  if(!u12Low())o.push("the ESRG scores in part 5.2");
  if(u12Num(S.h_score)===null||!S.h_weak.trim())o.push("the health score and two weakest traits in part 5.2");
  if(["result","wp","raised","rec","check"].some(function(k){return !U12W.s[k].trim();}))o.push("every field of the strategic line");
  if(["raised","rec","owner","check"].some(function(k){return !U12W.o[k].trim();}))o.push("every field of the operational line");
  if(["raised","rec","owner","check"].some(function(k){return !U12W.b[k].trim();}))o.push("every field of the behavioural line");
  U12W.kiss.forEach(function(r,i){if(!r.d||!r.line||!r.practice.trim()||!r.owner.trim())o.push("every field of Decision "+(i+1));});
  var miss=U12_DEC.filter(function(d){return !U12W.kiss.some(function(r){return r.d===d;});});
  if(miss.length)o.push("at least one "+miss.join(", one ")+" decision");
  return o;
}
function u12Texts(){
  var S=U12W.src,q=U12W.quarter;
  var A=["Quarter: "+q,"Enterprise Key Result: "+S.kr.trim(),"Result this quarter: "+U12W.s.result.trim(),"W · Waypoint: "+U12W.s.wp.trim(),"A · Alert: "+S.alert.trim(),
    "Alert raised: "+U12W.s.raised,"R · Recovery: "+U12W.s.rec.trim(),"D · Decider: "+S.dec.trim(),"Decider checks: "+U12W.s.check.trim()].join("\n");
  var B=["Quarter: "+q,"ESRG scan: "+U12_CAPN.map(function(c,i){var n=u12Num(S.es[i]);return c+" "+(n===null?"—":n.toFixed(2));}).join(" · "),"Lowest capability: "+u12LowText(),
    "W · Waypoint: each capability at 4.0 or above","A · Alert: any capability below 3.0","Alert raised: "+U12W.o.raised,"R · Recovery: "+U12W.o.rec.trim(),"Owner: "+U12W.o.owner.trim(),
    "D · Decider: "+S.dec.trim(),"Checked: "+U12W.o.check.trim()].join("\n");
  var C=["Quarter: "+q,"Health position: "+u12HText(),"W · Waypoint: 80/100 or above","A · Alert: below 60/100","Alert raised: "+U12W.b.raised,"R · Recovery: "+U12W.b.rec.trim(),
    "Owner: "+U12W.b.owner.trim(),"D · Decider: "+S.dec.trim(),"Checked: "+U12W.b.check.trim()].join("\n");
  var D=U12_DEC.map(function(d){return U12W.kiss.filter(function(r){return r.d===d;}).map(function(r){return d+": "+r.practice.trim()+" · Line of sight: "+r.line+" · Owner: "+r.owner.trim();}).join("\n");}).filter(Boolean).join("\n");
  return {qs_strategic:A,qs_operational:B,qs_behavioural:C,qs_kiss:"Quarter: "+q+" · decisions for the next quarter\n"+D};
}
/* The scribe's page saves the working record, and the four Capstone texts once the record is complete. */
function u12Out(){
  if(!window.S2RTeam||!S2RTeam.isScribe()||!U12Ready)return;
  var w=JSON.stringify(U12W);if(_u12Last.__qs_work!==w){_u12Last.__qs_work=w;S2RTeam.save("__qs_work",JSON.parse(w));}
  if(u12Open().length)return;
  var t=u12Texts();U12_KEYS.forEach(function(k){if(_u12Last[k]!==t[k]){_u12Last[k]=t[k];S2RTeam.save(k,t[k]);}});
}
function u12RecDraw(){
  var m=u12el("u12RecMsg");if(!m)return;var o=u12Open(),st=window.S2RTeam&&S2RTeam.status();
  if(st&&st.all_agreed)m.innerHTML='<span class="u12-ok">✓ Every member has agreed. Your group’s quarterly page goes into your team’s Capstone S2R Blueprint.</span>';
  else if(o.length)m.textContent="Still to complete before your group can agree: "+o.join("; ")+".";
  else m.textContent="Your record is complete. Each member reads it and selects Agree.";
}
async function u12Agree(){var o=u12Open();if(o.length){u12RecDraw();return;}if(!window.S2RTeam)return;
  if(S2RTeam.isScribe()){u12Out();await S2RTeam.flush();}await S2RTeam.agree();u12RecDraw();}
function u12Print(){
  var t=u12Texts(),T=["Strategic line","Operational line","Behavioural line","KISS for next quarter"];
  var body=U12_KEYS.map(function(k,i){return '<h2>'+T[i]+'</h2><pre>'+u12esc(t[k])+'</pre>';}).join("");
  var doc='<!doctype html><html><head><meta charset="utf-8"><title>Our Quarterly Three Lines of Sight</title><style>body{font-family:Arial,sans-serif;margin:32px;color:#111;}h1{font-size:20px;}h2{font-size:14px;margin-top:22px;}pre{white-space:pre-wrap;font-family:inherit;font-size:12.5px;line-height:1.6;}.sub{color:#666;font-size:12px;}</style></head><body>'+
    '<h1>Our Quarterly Three Lines of Sight</h1><p class="sub">Strategy2Results® · Module 4 · Unit 12 · Section 5 · Capstone work</p>'+body+'</body></html>';
  var w=window.open("","_blank");if(!w){window.print();return;}w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
function u12Init(r){
  r=r||{};var w=r.__qs_work;if(typeof w==="string"){try{w=JSON.parse(w);}catch(e){w=null;}}
  U12W=u12Norm(w);_u12Last={__qs_work:JSON.stringify(U12W)};U12_KEYS.forEach(function(k){if(typeof r[k]==="string")_u12Last[k]=r[k];});
  u12Fill();
}
var _u12On=false;
async function u12S5Start(responses){
  if(_u12On)return;_u12On=true;
  var root=u12el("mod4");if(root){root.addEventListener("input",u12OnInput);root.addEventListener("change",u12OnInput);}
  u12Init(responses);U12Ready=true;
  if(window.S2RTeam){try{await S2RTeam.attach({lens:U12_LENS,mount:"u12TwBar",lock:["mod4"],names:U12_NAMES,
    complete:function(){var o=u12Open();return o.length?o.join("; "):"";},
    onRemote:function(r){u12Init(r);}});}catch(e){}}
  var S=U12W.src;if(!S.kr&&!S.alert&&!u12Low()&&!S.h_score&&window.S2RTeam&&S2RTeam.isScribe())await u12Bring(false);
  u12RecDraw();
}
