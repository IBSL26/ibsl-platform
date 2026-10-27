
/* ── Unit 11 · Section 5 · The Cross-CXO Organisational Health Clinic (27 Oct 2026) ──
   Group Capstone work on the shared group record (s2r-team.js): the scribe types, every member selects Agree.
   Uses only the reference functional scores and losses below and the group's CXO roles (Carol: the Section 4 personal reflection does not feed Section 5).
   Saved for the group: __oh_work (the working record) and, once complete, oh_func, oh_cons, oh_rrr, oh_resp (Capstone 11A-11D). */
var U11_LENS="u4m1_lens10";
/*DATA*/
var U11_TR=["Minimal Politics","Minimal Confusion","High Morale","High Productivity","Low Turnover"];
var U11_FF=[["vuln","Potential cultural vulnerabilities"],["evid","Evidence requiring investigation"],["link","Links between the largest hidden cost and the two weakest traits"],["valid","Evidence needed to validate the estimates"],["overlap","Potential overlap or double counting"],["dist","Estimated exposure and validated loss"]];
var U11_RF=[["trait","Priority health trait"],["action","Review–Realign–Restore action"],["owners","Accountable CXO(s)"],["htarget","Health improvement target"],["cost","Associated hidden cost"],["target","Financial target (R)"]];
var U11W=u11Blank(),_u11Last={},U11Fold={f:{},r:{},n:{}},U11Charter=[],U11Ready=false;
function u11Blank(){return {roles:[],fn:{},t4:{contrib:"",xvuln:""},t5:{overlap:""},t6:{funcs:"",cult:"",people:""},rrr:{review:"",realign:"",restore:""},resp:[u11BlankResp()],coc:u11CocBlank()};}
function u11BlankResp(){return {trait:"",action:"",owners:"",htarget:"",cost:"",target:""};}
function u11esc(s){return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function u11el(id){return document.getElementById(id);}
function u11Str(v){return typeof v==="string"?v:"";}
function u11Norm(w){
  var b=u11Blank();if(!w||typeof w!=="object")return b;
  if(Array.isArray(w.roles))b.roles=U11_ROLES.map(function(r){return r[0];}).filter(function(c){return w.roles.indexOf(c)>=0;});
  if(w.fn&&typeof w.fn==="object")Object.keys(w.fn).forEach(function(c){var x={};U11_FF.forEach(function(f){x[f[0]]=u11Str(w.fn[c]&&w.fn[c][f[0]]);});b.fn[c]=x;});
  ["t4","t5","t6","rrr"].forEach(function(g){Object.keys(b[g]).forEach(function(k){b[g][k]=u11Str(w[g]&&w[g][k]);});});
  b.coc=u11CocNorm(w.coc);
  if(Array.isArray(w.resp)&&w.resp.length)b.resp=w.resp.map(function(r){var x=u11BlankResp();Object.keys(x).forEach(function(k){x[k]=u11Str(r&&r[k]);});return x;});
  return b;
}
function u11Row(c){for(var i=0;i<U11_ROLES.length;i++)if(U11_ROLES[i][0]===c)return U11_ROLES[i];return null;}
function u11Fn(c){if(!U11W.fn[c]){var x={};U11_FF.forEach(function(f){x[f[0]]="";});U11W.fn[c]=x;}return U11W.fn[c];}
function u11Band(x){return x>=80?"Healthy & Thriving":x>=60?"Stable but Uneven":x>=40?"Caution Zone":"Unhealthy";}
function u11R(n){return "R"+Math.round(n).toLocaleString("en-ZA").replace(/\s| /g,",");}
function u11D(x){return (Math.round(x*10)/10).toFixed(1);}
function u11Weak(vals){var ix=[0,1,2,3,4].sort(function(a,b){return vals[a]-vals[b]||a-b;});return [ix[0],ix[1]];}
function u11FnWeak(r){var w=u11Weak(r.slice(4,9));return U11_TR[w[0]]+" ("+r[4+w[0]]+"/20) and "+U11_TR[w[1]]+" ("+r[4+w[1]]+"/20)";}
function u11FnCost(c){var l=U11_LOSS[c]||[0,0,0,0,0],m=0;for(var i=1;i<5;i++)if(l[i]>l[m])m=i;return U11_CN[m]+" ("+u11R(l[m])+")";}
function u11FnTot(c){return (U11_LOSS[c]||[]).reduce(function(a,b){return a+b;},0);}
/* The group consolidation, weighted by valid responses (Task 3) and summed by hidden cost (Task 5) */
function u11Cons(){
  var sel=U11W.roles.map(u11Row).filter(Boolean);if(!sel.length)return null;
  var n=sel.reduce(function(a,r){return a+r[3];},0),tr=[0,1,2,3,4].map(function(t){return sel.reduce(function(a,r){return a+r[4+t]*r[3];},0)/n;});
  var tot=tr.reduce(function(a,b){return a+b;},0),cost=[0,1,2,3,4].map(function(k){return sel.reduce(function(a,r){return a+U11_LOSS[r[0]][k];},0);});
  var gross=cost.reduce(function(a,b){return a+b;},0),cix=[0,1,2,3,4].sort(function(a,b){return cost[b]-cost[a]||a-b;});
  return {sel:sel,n:n,staff:sel.reduce(function(a,r){return a+r[2];},0),tr:tr,tot:tot,weak:u11Weak(tr),cost:cost,gross:gross,big:[cix[0],cix[1]]};
}
function u11ConsText(c){return u11D(c.tot)+" /100 · "+u11Band(c.tot);}
function u11Fld(path,label,val){return '<label class="fld-label">'+label+'</label><textarea class="fld-input u11-ta" data-u11="'+path+'">'+u11esc(val)+'</textarea>';}
function u11DrawRoles(){
  var h=u11el("u11Roles");if(!h)return;
  h.innerHTML=U11_ROLES.map(function(r){var on=U11W.roles.indexOf(r[0])>=0;return '<label class="u11-chk'+(on?' on':'')+'"><input type="checkbox" data-u11="role-'+r[0]+'"'+(on?' checked':'')+'> <strong>'+r[0]+'</strong> · '+r[1]+'</label>';}).join("")+
    '<div class="u11-note2">'+(U11Charter.length?'Your Problem Charter’s executive team: '+u11esc(U11Charter.join("; ")):'Your group’s Problem Charter executive team appears here once the Charter is agreed in Unit 1.')+'</div>';
}
function u11DrawRef(){
  var a=u11el("u11Ref52"),b=u11el("u11Ref53"),c=u11Cons();if(!a)return;
  a.innerHTML='<div class="u11-scroll"><table class="u11-tbl u11-tbln u11-ref"><thead><tr><th>CXO</th><th>Function</th><th>Staff</th><th>No. of Responses</th><th>Politics</th><th>Confusion</th><th>Morale</th><th>Productivity</th><th>Turnover</th><th>Total</th></tr></thead><tbody>'+
    U11_ROLES.map(function(r){return '<tr class="'+(U11W.roles.indexOf(r[0])>=0?'u11-sel':'')+'">'+r.map(function(x){return '<td>'+x+'</td>';}).join("")+'</tr>';}).join("")+
    '<tr class="u11-tot"><td>Selected roles</td><td>Group consolidation</td>'+(c?'<td>'+c.staff+'</td><td>'+c.n+'</td>'+c.tr.map(function(x){return '<td>'+u11D(x)+'</td>';}).join("")+'<td>'+u11D(c.tot)+'</td>':'<td colspan="8">Tick your group’s CXO roles above</td>')+'</tr></tbody></table></div>';
  if(b)b.innerHTML='<div class="u11-scroll"><table class="u11-tbl u11-tbln u11-ref"><thead><tr><th>CXO</th>'+U11_CS.map(function(x){return '<th>'+x+'</th>';}).join("")+'<th>Gross Total</th></tr></thead><tbody>'+
    U11_ROLES.map(function(r){var l=U11_LOSS[r[0]];return '<tr class="'+(U11W.roles.indexOf(r[0])>=0?'u11-sel':'')+'"><td>'+r[0]+'</td>'+l.map(function(x){return '<td>'+u11R(x)+'</td>';}).join("")+'<td>'+u11R(u11FnTot(r[0]))+'</td></tr>';}).join("")+
    '<tr class="u11-tot"><td>Selected roles</td>'+(c?c.cost.map(function(x){return '<td>'+u11R(x)+'</td>';}).join("")+'<td>'+u11R(c.gross)+'</td>':'<td colspan="6">Tick your group’s CXO roles in part 5.2</td>')+'</tr></tbody></table></div>';
}
function u11DrawFns(){
  var h=u11el("u11Fns");if(!h)return;
  if(!U11W.roles.length){h.innerHTML='<div class="u11-note2">Tick your group’s CXO roles above to open one interpretation card per function.</div>';return;}
  h.innerHTML=U11W.roles.map(function(c,i){var r=u11Row(c),f=u11Fn(c);
    return '<details class="u11-det"'+(U11Fold.f[c]===undefined?(i===0?' open':''):(U11Fold.f[c]?' open':''))+' data-fold="f-'+c+'"><summary>'+c+' · '+r[1]+'</summary><div class="u11-det-b">'+
      '<div class="u11-sub">Task 1 · Functional health position</div>'+
      '<table class="u11-tbl u11-kv"><tbody><tr><td>CXO role / function</td><td>'+c+' · '+r[1]+'</td></tr><tr><td>Functional score and classification</td><td>'+r[9]+' /100 · '+u11Band(r[9])+' ('+r[3]+' of '+r[2]+' staff responded)</td></tr><tr><td>Two weakest traits</td><td>'+u11FnWeak(r)+'</td></tr></tbody></table>'+
      u11Fld("fn-"+c+"-vuln",U11_FF[0][1],f.vuln)+u11Fld("fn-"+c+"-evid",U11_FF[1][1],f.evid)+
      '<div class="u11-sub">Task 2 · Functional losses</div>'+
      '<table class="u11-tbl u11-kv"><tbody><tr><td>Largest hidden cost</td><td>'+u11FnCost(c)+'</td></tr><tr><td>Gross quarterly exposure</td><td>'+u11R(u11FnTot(c))+'</td></tr></tbody></table>'+
      u11Fld("fn-"+c+"-link",U11_FF[2][1],f.link)+u11Fld("fn-"+c+"-valid",U11_FF[3][1],f.valid)+u11Fld("fn-"+c+"-overlap",U11_FF[4][1],f.overlap)+u11Fld("fn-"+c+"-dist",U11_FF[5][1],f.dist)+
      '</div></details>';}).join("");
}
function u11DrawCalc(){
  var c=u11Cons(),t3=u11el("u11T3"),t5=u11el("u11T5"),none='<div class="u11-note2">Tick your group’s CXO roles in part 5.2.</div>';
  if(t3)t3.innerHTML=c?'<table class="u11-tbl u11-kv"><thead><tr><th>Organisational health trait</th><th>Enterprise score /20</th></tr></thead><tbody>'+U11_TR.map(function(t,i){return '<tr><td>'+t+'</td><td>'+u11D(c.tr[i])+'</td></tr>';}).join("")+'<tr class="u11-tot"><td>Enterprise Health Score /100</td><td>'+u11ConsText(c)+'</td></tr></tbody></table><div class="u11-note2">Weighted by '+c.n+' valid responses across '+c.sel.length+' function'+(c.sel.length>1?'s':'')+': '+c.sel.map(function(r){return r[0];}).join(", ")+'.</div>':none;
  if(t5)t5.innerHTML=c?'<table class="u11-tbl u11-kv"><thead><tr><th>Hidden cost</th><th>Enterprise quarterly exposure</th></tr></thead><tbody>'+U11_CN.map(function(t,i){return '<tr><td>'+t+'</td><td>'+u11R(c.cost[i])+'</td></tr>';}).join("")+'<tr class="u11-tot"><td>Total Gross Quarterly Exposure</td><td>'+u11R(c.gross)+'</td></tr></tbody></table>':none;
  var set=function(id,v){var e=u11el(id);if(e)e.textContent=v;};
  set("u11T4s",c?u11ConsText(c):"—");set("u11T4w",c?U11_TR[c.weak[0]]+" ("+u11D(c.tr[c.weak[0]])+"/20) and "+U11_TR[c.weak[1]]+" ("+u11D(c.tr[c.weak[1]])+"/20)":"—");
  set("u11T6s",c?u11ConsText(c):"—");set("u11T6w",c?U11_TR[c.weak[0]]+" and "+U11_TR[c.weak[1]]:"—");
  set("u11T6g",c?u11R(c.gross)+" (gross, before overlap adjustments)":"—");set("u11T6c",c?U11_CN[c.big[0]]+" ("+u11R(c.cost[c.big[0]])+") and "+U11_CN[c.big[1]]+" ("+u11R(c.cost[c.big[1]])+")":"—");
  set("u11Low",c?"Lowest-scoring health trait in your consolidated assessment: "+U11_TR[c.weak[0]]+" ("+u11D(c.tr[c.weak[0]])+"/20).":"");
}
function u11Cur(r){var c=u11Cons(),k=U11_CN.indexOf(r.cost);return (c&&k>=0)?c.cost[k]:null;}
function u11RedText(r){var cur=u11Cur(r),t=parseFloat(String(r.target).replace(/[^\d.]/g,""));if(cur===null)return "Select the associated hidden cost";
  return "Current "+u11R(cur)+(isNaN(t)?" → target not yet set":" → target "+u11R(t)+" (reduction "+u11R(cur-t)+")");}
function u11DrawResp(){
  var h=u11el("u11Resp");if(!h)return;
  h.innerHTML=U11W.resp.map(function(r,i){
    var sel=function(k,opts,ph){return '<select class="fld-isel" data-u11="resp-'+i+'-'+k+'"><option value="">'+ph+'</option>'+opts.map(function(o){return '<option'+(o===r[k]?' selected':'')+'>'+o+'</option>';}).join("")+'</select>';};
    return '<details class="u11-det"'+(U11Fold.r[i]!==false?' open':'')+' data-fold="r-'+i+'"><summary>Response '+(i+1)+(r.trait?' · '+u11esc(r.trait):'')+'</summary><div class="u11-det-b">'+
      '<label class="fld-label">Priority health trait</label>'+sel("trait",U11_TR,"Select the priority health trait")+
      u11Fld("resp-"+i+"-action","Review–Realign–Restore action",r.action)+
      '<div class="u11-grid"><div><label class="fld-label">Accountable CXO(s)</label><input class="fld-input" type="text" data-u11="resp-'+i+'-owners" value="'+u11esc(r.owners)+'"></div>'+
      '<div><label class="fld-label">Health improvement target</label><input class="fld-input" type="text" data-u11="resp-'+i+'-htarget" value="'+u11esc(r.htarget)+'" placeholder="e.g. trait score /20 next quarter"></div></div>'+
      '<div class="u11-grid"><div><label class="fld-label">Associated hidden cost</label>'+sel("cost",U11_CN,"Select the hidden cost")+'</div>'+
      '<div><label class="fld-label">Financial target for next quarter (R)</label><input class="fld-input" type="text" inputmode="numeric" data-u11="resp-'+i+'-target" value="'+u11esc(r.target)+'"></div></div>'+
      '<div class="u11-ro" id="u11Red'+i+'">'+u11RedText(r)+'</div>'+
      (U11W.resp.length>1?'<button type="button" class="ref-save" onclick="u11DelResp('+i+')">Remove this response</button>':'')+'</div></details>';}).join("");
}
function u11DrawFields(){
  document.querySelectorAll('#mod4 [data-u11^="t4-"],#mod4 [data-u11^="t5-"],#mod4 [data-u11^="t6-"],#mod4 [data-u11^="rrr-"]').forEach(function(t){var a=t.getAttribute("data-u11").split("-");if(document.activeElement!==t)t.value=U11W[a[0]][a[1]]||"";});
}
function u11Draw(){u11DrawRoles();u11DrawRef();u11DrawFns();u11DrawCalc();u11DrawFields();u11DrawResp();u11DrawCoc();u11RecDraw();}
function u11AddResp(){if(window.S2RTeam&&!S2RTeam.isScribe())return;U11W.resp.push(u11BlankResp());u11DrawResp();u11Out();u11RecDraw();}
function u11DelResp(i){if(window.S2RTeam&&!S2RTeam.isScribe())return;if(U11W.resp.length<2)return;if(!confirm("Remove Response "+(i+1)+"?"))return;U11W.resp.splice(i,1);U11Fold.r={};u11DrawResp();u11Out();u11RecDraw();}
function u11OnInput(ev){
  var t=ev.target,path=t&&t.getAttribute&&t.getAttribute("data-u11");if(!path)return;
  var a=path.split("-");
  if(a[0]==="role"){if(ev.type!=="change")return;var c=path.slice(5),i=U11W.roles.indexOf(c);if(t.checked&&i<0)U11W.roles.push(c);if(!t.checked&&i>=0)U11W.roles.splice(i,1);
    U11W.roles=U11_ROLES.map(function(r){return r[0];}).filter(function(x){return U11W.roles.indexOf(x)>=0;});u11DrawRoles();u11DrawRef();u11DrawFns();u11DrawCalc();u11DrawResp();}
  else if(a[0]==="cv"||a[0]==="cn"||a[0]==="ct"){u11CocInput(a,t,ev);}
  else if(a[0]==="fn"){u11Fn(a[1])[a[2]]=t.value;}
  else if(a[0]==="resp"){var r=U11W.resp[+a[1]];if(!r)return;r[a[2]]=t.value;
    if(a[2]==="trait"){var sm=document.querySelector('#u11Resp details[data-fold="r-'+a[1]+'"]>summary');if(sm)sm.textContent="Response "+(+a[1]+1)+(r.trait?" · "+r.trait:"");}
    var rd=u11el("u11Red"+a[1]);if(rd)rd.textContent=u11RedText(r);}
  else if(U11W[a[0]]&&a[1] in U11W[a[0]])U11W[a[0]][a[1]]=t.value;
  u11Out();u11RecDraw();
}
/* What is still open before the group can agree */
function u11Open(){
  var o=[];if(!U11W.roles.length){o.push("your group’s CXO roles in part 5.2");return o;}
  U11W.roles.forEach(function(c){var f=u11Fn(c);if(U11_FF.some(function(x){return !f[x[0]].trim();}))o.push("every field of the "+c+" card (Tasks 1 and 2)");});
  if(!U11W.t4.contrib.trim()||!U11W.t4.xvuln.trim())o.push("Task 4 in part 5.4");
  if(!U11W.t5.overlap.trim())o.push("the possible overlaps in Task 5");
  if(!U11W.t6.funcs.trim()||!U11W.t6.cult.trim()||!U11W.t6.people.trim())o.push("the EXCO findings in Task 6");
  if(!U11W.rrr.review.trim()||!U11W.rrr.realign.trim()||!U11W.rrr.restore.trim())o.push("the Review, Realign and Restore outputs in part 5.6");
  U11W.resp.forEach(function(r,i){if(U11_RF.some(function(f){return !String(r[f[0]]).trim();})||isNaN(parseFloat(String(r.target).replace(/[^\d.]/g,""))))o.push("every field of Response "+(i+1)+" in part 5.7");});
  o=o.concat(u11CocOpen());
  return o;
}
function u11Texts(){
  var c=u11Cons()||{sel:[],tr:[0,0,0,0,0],tot:0,weak:[0,1],cost:[0,0,0,0,0],gross:0,big:[0,1],n:0};
  var F=U11W.roles.map(function(k){var r=u11Row(k),f=u11Fn(k);
    return k+" · "+r[1].replace(/&amp;/g,"&")+"\nFunctional score and classification: "+r[9]+" /100 · "+u11Band(r[9])+"\nTwo weakest traits: "+u11FnWeak(r)+"\nLargest hidden cost: "+u11FnCost(k)+"\nGross quarterly exposure: "+u11R(u11FnTot(k))+"\n"+U11_FF.map(function(x){return x[1]+": "+f[x[0]].trim();}).join("\n");}).join("\n\n");
  var C=["Functions consolidated: "+c.sel.map(function(r){return r[0];}).join(", ")+" ("+c.n+" valid responses)"]
    .concat(U11_TR.map(function(t,i){return t+": "+u11D(c.tr[i])+" /20";}))
    .concat(["Consolidated health score: "+u11ConsText(c),"Two weakest traits: "+U11_TR[c.weak[0]]+" and "+U11_TR[c.weak[1]],
      "Functions contributing most to those weaknesses: "+U11W.t4.contrib.trim(),"Vulnerabilities requiring cross-functional leadership attention: "+U11W.t4.xvuln.trim()])
    .concat(U11_CN.map(function(t,i){return t+" exposure: "+u11R(c.cost[i]);}))
    .concat(["Total gross quarterly exposure: "+u11R(c.gross),"Possible overlaps: "+U11W.t5.overlap.trim(),
      "Two largest hidden-cost categories: "+U11_CN[c.big[0]]+" and "+U11_CN[c.big[1]],"Most vulnerable functions: "+U11W.t6.funcs.trim(),
      "Priority cultural vulnerabilities: "+U11W.t6.cult.trim(),"Priority people-performance concerns: "+U11W.t6.people.trim()]).join("\n");
  var R="Review · Prioritised organisational health diagnosis: "+U11W.rrr.review.trim()+"\nRealign · Agreed cultural reinforcement actions: "+U11W.rrr.realign.trim()+"\nRestore · Measurable health and performance commitments: "+U11W.rrr.restore.trim();
  var P=U11W.resp.map(function(r,i){return "Response "+(i+1)+": "+r.trait+"\nReview–Realign–Restore action: "+r.action.trim()+"\nAccountable CXO(s): "+r.owners.trim()+"\nHealth improvement target: "+r.htarget.trim()+"\nAssociated hidden cost: "+r.cost+"\nFinancial target: "+u11RedText(r);}).join("\n\n");
  return {oh_func:F,oh_cons:C,oh_rrr:R,oh_resp:P,oh_coc:u11CocText()};
}
/* The scribe's page saves the working record, and the four Capstone texts once the record is complete. */
function u11Out(){
  if(!window.S2RTeam||!S2RTeam.isScribe()||!U11Ready)return;
  var w=JSON.stringify(U11W);if(_u11Last.__oh_work!==w){_u11Last.__oh_work=w;S2RTeam.save("__oh_work",JSON.parse(w));}
  if(u11Open().length)return;
  var t=u11Texts();U11_KEYS.forEach(function(k){if(_u11Last[k]!==t[k]){_u11Last[k]=t[k];S2RTeam.save(k,t[k]);}});
}
function u11RecDraw(){
  var m=u11el("u11RecMsg");if(!m)return;var o=u11Open(),st=window.S2RTeam&&S2RTeam.status();
  if(st&&st.all_agreed)m.innerHTML='<span class="u11-ok">✓ Every member has agreed. Your group’s clinic record goes into your team’s Capstone S2R Blueprint.</span>';
  else if(o.length)m.textContent="Still to complete before your group can agree: "+o.join("; ")+".";
  else m.textContent="Your record is complete. Each member reads it and selects Agree.";
}
async function u11Agree(){var o=u11Open();if(o.length){u11RecDraw();return;}if(!window.S2RTeam)return;
  if(S2RTeam.isScribe()){u11Out();await S2RTeam.flush();}await S2RTeam.agree();u11RecDraw();}
function u11Print(){
  var t=u11Texts(),H=["Functional health assessments","Consolidated health position","Review–Realign–Restore","Organisational Health Response","Cultural Operating Code"];
  var body=U11_KEYS.map(function(k,i){return "<h2>"+H[i]+"</h2>"+t[k].split("\n").map(function(l){if(!l)return "";var j=l.indexOf(": ");return "<p>"+(j>0?"<strong>"+u11esc(l.slice(0,j))+":</strong> "+u11esc(l.slice(j+2)):"<strong>"+u11esc(l)+"</strong>")+"</p>";}).join("");}).join("");
  var doc='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Our Cross-CXO Organisational Health Clinic</title><style>body{font-family:Georgia,serif;color:#172033;max-width:780px;margin:32px auto;padding:0 20px;line-height:1.5}h1{color:#043f2f;font-size:25px;margin-bottom:2px}h2{color:#043f2f;font-size:18px;margin-top:22px;border-bottom:1px solid #ccc}p{margin:4px 0}.sub{color:#555;font-size:13px}</style></head><body>'+
    '<h1>Our Cross-CXO Organisational Health Clinic</h1><p class="sub">Strategy2Results® · Module 4 · Unit 11 · Section 5 · Capstone work</p>'+body+'</body></html>';
  var w=window.open("","_blank");if(!w){window.print();return;}w.document.write(doc);w.document.close();w.focus();setTimeout(function(){w.print();},300);
}
/* The group's agreed Problem Charter executive team (Unit 1): roles named there are ticked for a new record. */
var U11_MATCH=[["CEO",/\bCEO\b|chief executive/i],["CFO",/\bCFO\b|chief financ/i],["COO",/\bCOO\b|chief operat/i],["CHRO",/\bCHRO\b|chief (human|people)/i],["CTO/CIO",/\bCTO\b|\bCIO\b|chief (technology|information|digital)/i],
  ["CMO",/\bCMO\b|chief marketing/i],["CCO",/\bCCO\b|chief commercial/i],["CPO",/\bCPO\b|chief procurement/i],["CRO",/\bCRO\b|chief risk/i],["CSO",/\bCSO\b|chief strateg/i]];
var _u11CharterDone=false;
async function u11LoadCharter(){
  if(!_u11CharterDone){_u11CharterDone=true;
    var r={};try{r=window.S2R?(await S2R.loadAll("u1_foundations")||{}):{};}catch(e){r={};}
    var conf=Array.isArray(r.confirmed_items)?r.confirmed_items:[];
    var team=(conf.indexOf("Problem Charter · Executive Team")>=0&&typeof r.pc_team==="string")?r.pc_team:"";
    U11Charter=team.split(/\r?\n/).map(function(x){return x.replace(/^[\s\-•\d.]+/,"").trim();}).filter(Boolean);}
  if(!U11W.roles.length&&U11Charter.length&&window.S2RTeam&&S2RTeam.isScribe()){
    U11W.roles=U11_MATCH.filter(function(m){return U11Charter.some(function(x){return m[1].test(x);});}).map(function(m){return m[0];});
    if(U11W.roles.length){u11Draw();u11Out();if(S2RTeam.redraw)S2RTeam.redraw();return;}
  }
  u11DrawRoles();if(window.S2RTeam&&S2RTeam.redraw)S2RTeam.redraw();
}
function u11Init(r){
  r=r||{};var w=r.__oh_work;if(typeof w==="string"){try{w=JSON.parse(w);}catch(e){w=null;}}
  U11W=u11Norm(w);_u11Last={__oh_work:JSON.stringify(U11W)};U11_KEYS.forEach(function(k){if(typeof r[k]==="string")_u11Last[k]=r[k];});
  u11Draw();
}
var _u11On=false;
async function u11S5Start(responses){
  if(_u11On)return;_u11On=true;
  var root=u11el("mod4");if(root){root.addEventListener("input",u11OnInput);root.addEventListener("change",u11OnInput);
    root.addEventListener("toggle",function(e){var d=e.target,k=d&&d.getAttribute&&d.getAttribute("data-fold");if(!k)return;var g=k.slice(0,1),id=k.slice(2);U11Fold[g][g==="r"?+id:id]=d.open;},true);}
  u11Init(responses);U11Ready=true;
  if(window.S2RTeam){try{await S2RTeam.attach({lens:U11_LENS,mount:"u11TwBar",lock:["mod4"],names:U11_NAMES,
    complete:function(){var o=u11Open();return o.length?o.join("; "):"";},
    onRemote:function(r){u11Init(r);return u11LoadCharter();}});}catch(e){}}
  await u11LoadCharter();u11RecDraw();
}
