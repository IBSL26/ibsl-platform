
/* ── Unit 10 · Section 5 · The Enterprise ESRG Alignment Clinic (27 Oct 2026) ──
   Group Capstone work on the shared group record (s2r-team.js): the scribe types, every member selects Agree.
   Part 5.1 brings in every member's part 4.5 scanner (esrg_scan_head, esrg_scan) through rpc team_esrg_scans.
   Saved for the group: __es_work (the working record) and, once complete, es_scanner, es_interp, es_resp, es_plan (Capstone 10A-10D). */
var U10_LENS="u4m1_lens9";
var U10_NAMES=["ESRG Clinic · Enterprise Scanner","ESRG Clinic · Collective Findings","ESRG Clinic · Collective Intelligence Response","ESRG Clinic · Intervention Plan"];
var U10_KEYS=["es_scanner","es_interp","es_resp","es_plan"];
var U10_EL=["Facilities","Infrastructure","Technology","Standardisation","Integration","Process Efficiency","Asset Availability","Investment","Resource Utilisation","Policies & Procedures","Authority","Risk Management"];
var U10_PER=["Annual","Q1","Q2","Q3","Q4"];
var U10_DOM=[["Environment","Operational Readiness"],["Systems","Operational Flow"],["Resources","Delivery Capacity"],["Governance","Decision Responsiveness"]];
var U10_QL=["Functional / Convergence","Cross-functional / Divergence","Enterprise / Dependency"];
var U10_RF=[["finding","Collective finding"],["commit","Strategic commitment affected"],["response","Collective intelligence response"],["functions","Functions involved"]];
var U10_PF=[["actions","Implementation actions"],["owner","Accountable executive"],["contrib","Contributing functions"],["date","Target date"],["evidence","Evidence of improvement"]];
var U10W=u10Blank(),U10M=[],U10Roles=[],U10Loaded=false,_u10Last={},U10Fold={r:{},p:{}};
function u10Blank(){return {period:0,gaps:"",interp:[["","",""],["","",""],["","",""],["","",""]],resp:[u10BlankResp()]};}
function u10BlankResp(){return {dom:"",comp:"",finding:"",commit:"",response:"",functions:"",actions:"",owner:"",contrib:"",date:"",evidence:""};}
function u10esc(s){return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function u10el(id){return document.getElementById(id);}
function u10Norm(w){
  var b=u10Blank();if(!w||typeof w!=="object")return b;
  b.period=(w.period>=0&&w.period<=4)?(w.period|0):0;b.gaps=typeof w.gaps==="string"?w.gaps:"";
  if(Array.isArray(w.interp))for(var d=0;d<4;d++)for(var k=0;k<3;k++){var v=w.interp[d]&&w.interp[d][k];b.interp[d][k]=typeof v==="string"?v:"";}
  if(Array.isArray(w.resp)&&w.resp.length)b.resp=w.resp.map(function(r){var x=u10BlankResp();Object.keys(x).forEach(function(k){if(r&&typeof r[k]==="string")x[k]=r[k];});return x;});
  return b;
}
function u10Parse(t){var m={};String(t||"").split(/\r?\n/).forEach(function(l){var i=l.lastIndexOf(": ");if(i>0)m[l.slice(0,i).trim()]=l.slice(i+2).trim();});return m;}
function u10Col(m){return m.role||m.name;}
function u10Score(m,ci,p){var v=m.map[U10_EL[ci]+" · "+U10_PER[p]];if(v==="N/A")return "na";var n=parseInt(v,10);return isNaN(n)?null:n;}
function u10Count(m,p){var n=0;for(var i=0;i<12;i++)if(u10Score(m,i,p)!==null)n++;return n;}
function u10Cap(m,d,p){var s=[];for(var i=d*3;i<d*3+3;i++){var v=u10Score(m,i,p);if(v===null)return null;if(v!=="na")s.push(v);}
  return s.length?s.reduce(function(a,b){return a+b;},0)/s.length:"na";}
function u10Ent(d,p){var s=U10M.map(function(m){return u10Cap(m,d,p);}).filter(function(x){return typeof x==="number";});return s.length?s.reduce(function(a,b){return a+b;},0)/s.length:null;}
function u10Fmt(x,dp){return x===null?"—":x==="na"?"N/A":(typeof x==="number"?x.toFixed(dp==null?2:dp):String(x));}
function u10Band(x){return typeof x!=="number"?"":x>=4?" b4":x>=3?" b3":x>=2?" b2":" b1";}
function u10Missing(){var p=0;return U10M.filter(function(m){return u10Count(m,p)<12;});}

/* 5.1 · the scanner views, drawn from the members' part 4.5 scores */
function u10DrawScanner(){
  var p=0,v=u10el("u10Verify"),e=u10el("u10Ent"),s=u10el("u10Sum");if(!v)return;
  var sel=u10el("u10Period");if(sel&&document.activeElement!==sel)sel.value=String(p);
  if(!U10Loaded){v.innerHTML='<div class="u10-note">Loading your group’s functional scanners…</div>';e.innerHTML="";s.innerHTML="";return;}
  if(!U10M.length){v.innerHTML='<div class="u10-note">Your group’s functional scanners appear here once your group is set and members have completed part 4.5.</div>';e.innerHTML="";s.innerHTML="";return;}
  v.innerHTML='<div class="u10-scroll"><table class="u10-tbl" style="min-width:720px"><thead><tr><th>Capstone executive role</th><th>Member</th><th>Business function</th><th>Stated problem</th><th>Annual baseline · components scored</th></tr></thead><tbody>'+
    U10M.map(function(m){var n=u10Count(m,p);return '<tr><td>'+u10esc(m.role||"Not yet selected")+'</td><td>'+u10esc(m.name)+'</td><td>'+u10esc(m.fn||"—")+'</td><td>'+u10esc(m.prob||"—")+'</td><td class="'+(n===12?"u10-ok":"u10-miss")+'">'+n+' of 12'+(n===12?" ✓":" · missing")+'</td></tr>';}).join("")+'</tbody></table></div>';
  var hd='<th>ESRG domain</th><th>Execution capability</th><th>Component</th>'+U10M.map(function(m){return '<th>'+u10esc(u10Col(m))+'</th>';}).join("");
  var rows="";for(var i=0;i<12;i++){var d=Math.floor(i/3);rows+='<tr><td>'+U10_DOM[d][0]+'</td><td>'+U10_DOM[d][1]+'</td><td>'+u10esc(U10_EL[i])+'</td>'+U10M.map(function(m){var x=u10Score(m,i,p);return '<td class="'+(x===null?"u10-miss":"")+'">'+u10Fmt(x,0)+'</td>';}).join("")+'</tr>';}
  e.innerHTML='<div class="u10-scroll"><table class="u10-tbl u10-ent" style="min-width:'+(420+90*U10M.length)+'px"><thead><tr>'+hd+'</tr></thead><tbody>'+rows+'</tbody></table></div>';
  var srows=U10_DOM.map(function(dd,d){return '<tr><td>'+dd[0]+'</td><td>'+dd[1]+'</td>'+U10M.map(function(m){var x=u10Cap(m,d,p);return '<td><span class="u10-pv'+u10Band(x)+'">'+u10Fmt(x)+'</span></td>';}).join("")+'<td><span class="u10-pv'+u10Band(u10Ent(d,p))+'">'+u10Fmt(u10Ent(d,p))+'</span></td></tr>';}).join("");
  s.innerHTML='<div class="u10-scroll"><table class="u10-tbl u10-ent u10-sum" style="min-width:'+(420+90*U10M.length)+'px"><thead><tr><th>ESRG domain</th><th>Execution capability</th>'+U10M.map(function(m){return '<th>'+u10esc(u10Col(m))+'</th>';}).join("")+'<th>Enterprise avg.</th></tr></thead><tbody>'+srows+'</tbody></table></div>'+
    '<div class="u10-note">A dash (—) is a missing score: it stays blank and never counts as zero.</div>';
}
async function u10LoadTeam(){
  var c=window.S2R&&S2R._client,ctx=null;try{ctx=window.S2R?await S2R.context():null;}catch(e){ctx=null;}
  var rows=[];
  if(c&&ctx){try{var r=await c.rpc("team_esrg_scans",{p_cohort_id:ctx.cohortId});if(r&&!r.error&&Array.isArray(r.data))rows=r.data;}catch(e){}}
  U10M=rows.map(function(x){var h=u10Parse(x.head);return {id:x.profile_id,name:x.full_name||"Member",role:h["Capstone executive role"]||"",fn:h["Business function"]||"",prob:h["Stated problem"]||"",map:u10Parse(x.scan)};});
  U10Loaded=true;u10DrawScanner();u10Out();
}
async function u10LoadOwners(){
  var c=window.u10Charter?await u10Charter():{roles:[],problems:[]};
  U10Roles=c.roles.slice();u10DrawRows();
}

/* 5.2 to 5.4 · the group's entries */
function u10CompOpts(dom,cur){var d=-1;U10_DOM.forEach(function(x,i){if(x[0]===dom)d=i;});var h='<option value="">Select a component</option>';
  if(d>=0)for(var i=d*3;i<d*3+3;i++)h+='<option'+(U10_EL[i]===cur?' selected':'')+'>'+u10esc(U10_EL[i])+'</option>';return h;}
function u10Fld(path,label,val,kind){
  if(kind==="ta")return '<label class="fld-label">'+label+'</label><textarea class="fld-input u10-ta" style="min-height:56px;" data-u10="'+path+'">'+u10esc(val)+'</textarea>';
  if(kind==="date")return '<label class="fld-label">'+label+'</label><input class="fld-input" type="date" data-u10="'+path+'" value="'+u10esc(val)+'">';
  return '<label class="fld-label">'+label+'</label><input class="fld-input" type="text" data-u10="'+path+'" value="'+u10esc(val)+'">';
}
function u10DrawRows(){
  var host=u10el("u10Resp"),plan=u10el("u10Plan");if(!host)return;
  host.innerHTML=U10W.resp.map(function(r,i){
    var cap="";U10_DOM.forEach(function(x){if(x[0]===r.dom)cap=x[1];});
    return '<details class="u10-det"'+(U10Fold.r[i]!==false?' open':'')+' data-fold="r-'+i+'"><summary>Response '+(i+1)+(r.comp?' · '+u10esc(r.comp):'')+'</summary><div class="u10-det-b"><div class="u10-grid">'+
      '<div><label class="fld-label">ESRG domain</label><select class="fld-isel" data-u10="resp-'+i+'-dom"><option value="">Select a domain</option>'+U10_DOM.map(function(x){return '<option'+(x[0]===r.dom?' selected':'')+'>'+x[0]+'</option>';}).join("")+'</select></div>'+
      '<div><label class="fld-label">Execution capability</label><div class="u10-ro" id="u10Cap'+i+'">'+(cap||"—")+'</div></div>'+
      '<div><label class="fld-label">Component</label><select class="fld-isel" data-u10="resp-'+i+'-comp">'+u10CompOpts(r.dom,r.comp)+'</select></div></div>'+
      u10Fld("resp-"+i+"-finding","Collective finding",r.finding,"ta")+'<label class="fld-label">Strategic commitment affected</label><select class="fld-isel" data-u10="resp-'+i+'-commit">'+u10ProblemOpts(null,r.commit,"Select the stated problem it affects")+'</select>'+
      u10Fld("resp-"+i+"-response","Collective intelligence response",r.response,"ta")+u10Fld("resp-"+i+"-functions","Functions involved",r.functions)+
      (U10W.resp.length>1?'<button type="button" class="ref-save" onclick="u10DelResp('+i+')">Remove this response</button>':'')+'</div></details>';
  }).join("");
  if(plan)plan.innerHTML=U10W.resp.map(function(r,i){
    var owners=U10Roles.slice();if(r.owner&&owners.indexOf(r.owner)<0)owners.push(r.owner);
    var own=owners.length?'<label class="fld-label">Accountable executive</label><select class="fld-isel" data-u10="resp-'+i+'-owner"><option value="">Select the accountable executive</option>'+owners.map(function(o){return '<option'+(o===r.owner?' selected':'')+'>'+u10esc(o)+'</option>';}).join("")+'</select>':u10Fld("resp-"+i+"-owner","Accountable executive",r.owner);
    return '<details class="u10-det"'+(U10Fold.p[i]!==false?' open':'')+' data-fold="p-'+i+'"><summary>Intervention '+(i+1)+' · from Response '+(i+1)+'</summary><div class="u10-det-b">'+
      '<label class="fld-label">Agreed collective response (from 5.3)</label><div class="u10-ro" id="u10PR'+i+'">'+u10PRText(r,i)+'</div>'+
      u10Fld("resp-"+i+"-actions","Implementation actions",r.actions,"ta")+'<div class="u10-grid"><div>'+own+'</div><div>'+u10Fld("resp-"+i+"-contrib","Contributing functions",r.contrib)+'</div><div>'+u10Fld("resp-"+i+"-date","Target date",r.date,"date")+'</div></div>'+
      u10Fld("resp-"+i+"-evidence","Evidence of improvement",r.evidence,"ta")+'</div></details>';
  }).join("");
}
function u10PRText(r,i){return r.response?u10esc(r.response):'<span class="u10-miss">Write Response '+(i+1)+' in part 5.3 first.</span>';}
function u10DrawFields(){
  document.querySelectorAll('#mod4 [data-u10^="interp-"]').forEach(function(t){var a=t.getAttribute("data-u10").split("-");if(document.activeElement!==t)t.value=U10W.interp[+a[1]][+a[2]]||"";});
  var g=u10el("u10Gaps");if(g&&document.activeElement!==g)g.value=U10W.gaps;
}
function u10Draw(){u10DrawScanner();u10DrawFields();u10DrawRows();u10RecDraw();}
function u10AddResp(){if(window.S2RTeam&&!S2RTeam.isScribe())return;U10W.resp.push(u10BlankResp());u10DrawRows();u10Out();u10RecDraw();}
function u10DelResp(i){if(window.S2RTeam&&!S2RTeam.isScribe())return;if(U10W.resp.length<2)return;if(!confirm("Remove Response "+(i+1)+" and its intervention?"))return;U10W.resp.splice(i,1);U10Fold={r:{},p:{}};u10DrawRows();u10Out();u10RecDraw();}
function u10OnInput(ev){
  var t=ev.target,path=t&&t.getAttribute&&t.getAttribute("data-u10");if(!path)return;
  if(path==="period"){U10W.period=parseInt(t.value,10)||0;u10DrawScanner();}
  else if(path==="gaps")U10W.gaps=t.value;
  else{var a=path.split("-");
    if(a[0]==="interp")U10W.interp[+a[1]][+a[2]]=t.value;
    else if(a[0]==="resp"){var r=U10W.resp[+a[1]];if(!r)return;r[a[2]]=t.value;
      if(a[2]==="dom"||a[2]==="comp"){var sm=document.querySelector('#u10Resp details[data-fold="r-'+a[1]+'"]>summary');if(sm)sm.textContent="Response "+(+a[1]+1)+(a[2]==="comp"&&r.comp?" · "+r.comp:"");}
      if(a[2]==="dom"&&ev.type==="change"){r.comp="";var cs=document.querySelector('[data-u10="resp-'+a[1]+'-comp"]');if(cs)cs.innerHTML=u10CompOpts(r.dom,"");
        var cl=u10el("u10Cap"+a[1]);if(cl){var c="—";U10_DOM.forEach(function(x){if(x[0]===r.dom)c=x[1];});cl.textContent=c;}}
      if(a[2]==="response"){var pr=u10el("u10PR"+a[1]);if(pr)pr.innerHTML=u10PRText(r,+a[1]);}}}
  u10Out();u10RecDraw();
}

/* What is still open before the group can agree */
function u10Open(){
  var o=[],p=0;
  if(!U10M.some(function(m){return u10Count(m,p)===12;}))o.push("at least one complete annual baseline from part 4.5");
  if(u10Missing().length&&!U10W.gaps.trim())o.push("the missing submissions or evidence gaps in part 5.1");
  var n=0;U10W.interp.forEach(function(d){d.forEach(function(x){if(x.trim())n++;});});if(n<12)o.push("the findings in part 5.2 ("+n+" of 12 written)");
  U10W.resp.forEach(function(r,i){
    if(!r.dom||!r.comp||!r.finding.trim()||!r.commit.trim()||!r.response.trim()||!r.functions.trim())o.push("every field of Response "+(i+1)+" in part 5.3");
    if(!r.actions.trim()||!r.owner.trim()||!r.contrib.trim()||!r.date||!r.evidence.trim())o.push("every field of Intervention "+(i+1)+" in part 5.4");
  });
  return o;
}
function u10Texts(){
  var p=0,L=["Assessment: annual baseline, reviewed at Q1"];
  L.push("Functions assessed: "+(U10M.length?U10M.map(function(m){return u10Col(m)+(m.fn?" ("+m.fn+")":"")+(m.prob?", stated problem: "+m.prob:"")+", "+u10Count(m,p)+" of 12 components scored";}).join("; "):"none"));
  U10_DOM.forEach(function(d,i){L.push(d[1]+" ("+d[0]+"): "+U10M.map(function(m){return u10Col(m)+" "+u10Fmt(u10Cap(m,i,p));}).join(" · ")+" · Enterprise avg. "+u10Fmt(u10Ent(i,p)));});
  L.push("Missing submissions or evidence gaps: "+(U10W.gaps.trim()||"None"));
  var I=U10_DOM.map(function(d,i){return d[0]+" · "+d[1]+"\n"+U10_QL.map(function(q,k){return q+": "+U10W.interp[i][k].trim();}).join("\n");}).join("\n\n");
  var R=U10W.resp.map(function(r,i){var cap="";U10_DOM.forEach(function(x){if(x[0]===r.dom)cap=x[1];});
    return "Response "+(i+1)+": "+r.dom+" · "+cap+" · "+r.comp+"\n"+U10_RF.map(function(f){return f[1]+": "+r[f[0]].trim();}).join("\n");}).join("\n\n");
  var P=U10W.resp.map(function(r,i){return "Intervention "+(i+1)+" (from Response "+(i+1)+"): "+r.response.trim()+"\n"+U10_PF.map(function(f){return f[1]+": "+String(r[f[0]]).trim();}).join("\n");}).join("\n\n");
  return {es_scanner:L.join("\n"),es_interp:I,es_resp:R,es_plan:P};
}
/* The scribe's page saves the working record, and the four Capstone texts once the record is complete. */
function u10Out(){
  if(!window.S2RTeam||!S2RTeam.isScribe()||!U10Loaded)return;
  var w=JSON.stringify(U10W);if(_u10Last.__es_work!==w){_u10Last.__es_work=w;S2RTeam.save("__es_work",JSON.parse(w));}
  if(u10Open().length)return;
  var t=u10Texts();U10_KEYS.forEach(function(k){if(_u10Last[k]!==t[k]){_u10Last[k]=t[k];S2RTeam.save(k,t[k]);}});
}
function u10RecDraw(){
  var m=u10el("u10RecMsg");if(!m)return;var o=u10Open(),st=window.S2RTeam&&S2RTeam.status();
  if(st&&st.all_agreed)m.innerHTML='<span class="u10-ok">✓ Every member has agreed. Your group’s clinic record goes into your team’s Capstone S2R Blueprint.</span>';
  else if(o.length)m.textContent="Still to complete before your group can agree: "+o.join("; ")+".";
  else m.textContent="Your record is complete. Each member reads it and selects Agree.";
}
async function u10Agree(){
  var o=u10Open();if(o.length){u10RecDraw();return;}
  if(!window.S2RTeam)return;
  if(S2RTeam.isScribe()){u10Out();await S2RTeam.flush();}
  await S2RTeam.agree();u10RecDraw();
}
function u10Print(){
  var t=u10Texts(),H=["Enterprise ESRG Scanner","Collective findings","Collective Intelligence Response","ESRG Alignment Intervention Plan"];
  var body=U10_KEYS.map(function(k,i){return "<h2>"+H[i]+"</h2>"+t[k].split("\n").map(function(l){if(!l)return "";var j=l.indexOf(": ");return "<p>"+(j>0?"<strong>"+u10esc(l.slice(0,j))+":</strong> "+u10esc(l.slice(j+2)):"<strong>"+u10esc(l)+"</strong>")+"</p>";}).join("");}).join("");
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our Enterprise ESRG Alignment Clinic</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}h2{color:#043f2f;font-size:18px;margin-top:22px;border-bottom:1px solid #ccc}p{margin:4px 0}.sub{color:#555;font-size:13px}</style></head><body>'+
    '<h1>Our Enterprise ESRG Alignment Clinic</h1><p class="sub">Strategy2Results® · Module 4 · Unit 10 · Section 5 · Capstone work</p>'+body+'</body></html>';
  var w=window.open("","_blank");if(!w){window.print();return;}w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
function u10Init(r){
  r=r||{};var w=r.__es_work;if(typeof w==="string"){try{w=JSON.parse(w);}catch(e){w=null;}}
  U10W=u10Norm(w);_u10Last={__es_work:JSON.stringify(U10W)};U10_KEYS.forEach(function(k){if(typeof r[k]==="string")_u10Last[k]=r[k];});
  u10Draw();
}
var _u10On=false;
function u10S5Start(responses){
  if(_u10On)return;_u10On=true;
  var root=u10el("mod4");if(root){root.addEventListener("input",u10OnInput);root.addEventListener("change",u10OnInput);
    root.addEventListener("toggle",function(e){var d=e.target,k=d&&d.getAttribute&&d.getAttribute("data-fold");if(!k)return;var a=k.split("-");U10Fold[a[0]][+a[1]]=d.open;},true);}
  u10Init(responses);u10LoadOwners();u10LoadTeam();
  if(window.S2RTeam)S2RTeam.attach({lens:U10_LENS,mount:"u10TwBar",lock:["mod4"],names:U10_NAMES,
    complete:function(){var o=u10Open();return o.length?o.join("; "):"";},
    onRemote:function(r){u10Init(r);u10LoadTeam();}});
}
