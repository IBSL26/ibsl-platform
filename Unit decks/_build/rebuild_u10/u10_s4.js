
/* Unit 10 · part 4.5 My Capstone Functional ESRG Assessment (annual baseline): keys esrg_scan_head and esrg_scan.
   The role and the stated problem come from the group's agreed Problem Charter (Unit 1). */
FIELD_SPECS.esrg_scan_head=[{l:"Capstone executive role",k:"select"},{l:"Business function",k:"text"},{l:"Stated problem",k:"select"}];
FIELD_SPECS.esrg_scan=["Facilities","Infrastructure","Technology","Standardisation","Integration","Process Efficiency","Asset Availability","Investment","Resource Utilisation","Policies & Procedures","Authority","Risk Management"].map(function(e){return {l:e+" · Annual",k:"select"};});
var _u10Charter=null;
/* The group's agreed Problem Charter: company, executive team and stated problems (central problem, then the challenges the group will address). */
async function u10Charter(){
  if(_u10Charter)return _u10Charter;
  var r={};try{r=window.S2R?(await S2R.loadAll("u1_foundations")||{}):{};}catch(e){r={};}
  var conf=Array.isArray(r.confirmed_items)?r.confirmed_items:[];
  function g(k,n){return conf.indexOf(n)>=0&&typeof r[k]==="string"?r[k].trim():"";}
  var team=g("pc_team","Problem Charter · Executive Team"),groups=[],central=g("pc_problem","Problem Charter · Central Organisational Problem");
  if(central)groups.push(["Our central organisational problem",[central]]);
  if(conf.indexOf("Problem Charter · Challenges We Will Address")>=0){var w=r.__pc_work||{};
    [["design","Strategy design"],["execution","Strategy execution"],["sustain","Sustaining performance"]].forEach(function(a){
      var list=(w.ch&&Array.isArray(w.ch[a[0]])?w.ch[a[0]]:[]).map(function(x){return String(x||"").trim();}).filter(Boolean),out=[];
      (w.pick&&Array.isArray(w.pick[a[0]])?w.pick[a[0]]:[]).forEach(function(x){x=String(x||"").trim();if(x&&list.indexOf(x)>=0&&out.indexOf(x)<0)out.push(x);});
      if(out.length)groups.push(["Challenges we will address · "+a[1],out]);});}
  _u10Charter={company:g("pc_company","Problem Charter · Simulated Company"),roles:team?team.split(/\r?\n/).map(function(x){return x.replace(/^[\s\-•\d.]+/,"").trim();}).filter(Boolean):[],problems:groups};
  return _u10Charter;
}
function u10ProblemOpts(sel,cur,ph){
  var c=_u10Charter||{problems:[]},h='<option value="">'+(ph||"Select the stated problem")+'</option>',all=[];
  function e(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/"/g,"&quot;");}
  c.problems.forEach(function(g){h+='<optgroup label="'+e(g[0])+'">'+g[1].map(function(x){all.push(x);return '<option value="'+e(x)+'"'+(x===cur?' selected':'')+'>'+e(x)+'</option>';}).join("")+'</optgroup>';});
  if(cur&&all.indexOf(cur)<0)h+='<option value="'+e(cur)+'" selected>'+e(cur)+'</option>';
  if(sel)sel.innerHTML=h;return h;
}
async function u10LoadRoles(){
  var sel=document.getElementById("u10RoleSel");if(!sel)return;
  var c=await u10Charter();
  var coEl=document.getElementById("u10CoName");if(coEl)coEl.textContent=c.company?"Capstone organisation: "+c.company:"";
  var note=document.getElementById("u10RoleNote");if(note)note.style.display=c.roles.length?"none":"block";
  var pn=document.getElementById("u10ProbNote");if(pn)pn.style.display=c.problems.length?"none":"block";
  var saved=document.getElementById("esrg_scan_head"),lines=((saved&&saved.value)||"").split("\n");
  function cur(lbl){var l=lines.filter(function(x){return x.indexOf(lbl+":")===0;})[0];return l?l.slice(lbl.length+1).trim():"";}
  var roles=c.roles.slice(),cr=cur("Capstone executive role");if(cr&&roles.indexOf(cr)<0)roles.push(cr);
  roles.forEach(function(x){var o=document.createElement("option");o.value=x;o.textContent=x;sel.appendChild(o);});
  u10ProblemOpts(document.getElementById("u10ProbSel"),cur("Stated problem"));
  hydrateField("esrg_scan_head");
}
