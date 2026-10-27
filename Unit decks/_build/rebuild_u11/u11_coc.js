
/* ── Unit 11 · part 5.8 Build Your Cultural Operating Code (27 Oct 2026, Carol 22:37) ──
   Part of the same group record: U11W.coc = {vals:[{v,m}], norms:[{value,beh,acr,acts,stmt}], test:{norm,newemp,pressure,mirror}}; Capstone 11E = oh_coc. */
var U11_NF=[["beh","Observable behaviour"],["acr","Acronym"],["acts","The three actions"],["stmt","Norm statement"]];
var U11_TF=[["newemp","The New Employee Test"],["pressure","The Pressure Test"],["mirror","The Mirror Test"]];
function u11CocBlank(){var v=[];for(var i=0;i<6;i++)v.push({v:"",m:""});return {vals:v,norms:[u11NormBlank(),u11NormBlank(),u11NormBlank()],test:{norm:"",newemp:"",pressure:"",mirror:""}};}
function u11NormBlank(){return {value:"",beh:"",acr:"",acts:"",stmt:""};}
function u11CocNorm(c){
  var b=u11CocBlank();if(!c||typeof c!=="object")return b;
  if(Array.isArray(c.vals))for(var i=0;i<6;i++){var x=c.vals[i]||{};b.vals[i]={v:u11Str(x.v),m:u11Str(x.m)};}
  if(Array.isArray(c.norms)&&c.norms.length)b.norms=c.norms.slice(0,6).map(function(n){var x=u11NormBlank();Object.keys(x).forEach(function(k){x[k]=u11Str(n&&n[k]);});return x;});
  if(c.test)Object.keys(b.test).forEach(function(k){b.test[k]=u11Str(c.test[k]);});
  return b;
}
function u11CocVals(){return U11W.coc.vals.map(function(x){return x.v.trim();}).filter(Boolean);}
function u11CocNormLabel(n){return (n.acr.trim()||"Norm")+(n.value?" · "+n.value:"");}
function u11CocValOpts(cur){var vs=u11CocVals(),h='<option value="">Select a value</option>';if(cur&&vs.indexOf(cur)<0)vs.push(cur);
  vs.forEach(function(v){h+='<option'+(v===cur?' selected':'')+'>'+u11esc(v)+'</option>';});return h;}
function u11CocTestOpts(cur){var h='<option value="">Select your strongest norm</option>',seen=false;
  U11W.coc.norms.forEach(function(n){var l=u11CocNormLabel(n);if(!n.acr.trim()&&!n.value)return;if(l===cur)seen=true;h+='<option'+(l===cur?' selected':'')+'>'+u11esc(l)+'</option>';});
  if(cur&&!seen)h+='<option selected>'+u11esc(cur)+'</option>';return h;}
function u11DrawCoc(){
  var hv=u11el("u11CocVals"),hn=u11el("u11CocNorms"),ht=u11el("u11CocTest");if(!hv)return;
  hv.innerHTML=U11W.coc.vals.map(function(x,i){return '<div class="u11-cv"><div><label class="fld-label">Value '+(i+1)+(i<3?'':' (optional)')+'</label><input class="fld-input" type="text" data-u11="cv-'+i+'-v" value="'+u11esc(x.v)+'"></div>'+
    '<div><label class="fld-label">What it means</label><input class="fld-input" type="text" data-u11="cv-'+i+'-m" value="'+u11esc(x.m)+'"></div></div>';}).join("");
  hn.innerHTML=U11W.coc.norms.map(function(n,i){return '<details class="u11-det" data-fold="n-'+i+'"'+(U11Fold.n&&U11Fold.n[i]===false?'':' open')+'><summary>Norm '+(i+1)+(n.acr.trim()?' · '+u11esc(n.acr.trim()):'')+'</summary><div class="u11-det-b">'+
    '<label class="fld-label">Value</label><select class="fld-isel" data-u11="cn-'+i+'-value">'+u11CocValOpts(n.value)+'</select>'+
    U11_NF.map(function(f){return '<label class="fld-label">'+f[1]+'</label>'+(f[0]==="acr"?'<input class="fld-input" type="text" data-u11="cn-'+i+'-acr" value="'+u11esc(n.acr)+'">':'<textarea class="fld-input u11-ta" data-u11="cn-'+i+'-'+f[0]+'">'+u11esc(n[f[0]])+'</textarea>');}).join("")+
    (U11W.coc.norms.length>3?'<button type="button" class="ref-save" onclick="u11CocDel('+i+')">Remove this norm</button>':'')+'</div></details>';}).join("");
  ht.innerHTML='<label class="fld-label">Strongest norm</label><select class="fld-isel" data-u11="ct-norm">'+u11CocTestOpts(U11W.coc.test.norm)+'</select>'+
    U11_TF.map(function(f){return '<label class="fld-label">'+f[1]+'</label><textarea class="fld-input u11-ta" data-u11="ct-'+f[0]+'">'+u11esc(U11W.coc.test[f[0]])+'</textarea>';}).join("");
}
function u11CocAdd(){if(window.S2RTeam&&!S2RTeam.isScribe())return;if(U11W.coc.norms.length>=6)return;U11W.coc.norms.push(u11NormBlank());u11DrawCoc();u11Out();u11RecDraw();}
function u11CocDel(i){if(window.S2RTeam&&!S2RTeam.isScribe())return;if(U11W.coc.norms.length<=3)return;if(!confirm("Remove Norm "+(i+1)+"?"))return;U11W.coc.norms.splice(i,1);U11Fold.n={};u11DrawCoc();u11Out();u11RecDraw();}
function u11CocInput(a,t,ev){
  if(a[0]==="cv"){var x=U11W.coc.vals[+a[1]];if(!x)return;x[a[2]]=t.value;
    if(a[2]==="v"&&ev.type==="change")document.querySelectorAll('#u11CocNorms select[data-u11$="-value"]').forEach(function(s){var i=+s.getAttribute("data-u11").split("-")[1];s.innerHTML=u11CocValOpts(U11W.coc.norms[i].value);});}
  else if(a[0]==="cn"){var n=U11W.coc.norms[+a[1]];if(!n)return;n[a[2]]=t.value;
    if(a[2]==="acr"){var sm=document.querySelector('#u11CocNorms details[data-fold="n-'+a[1]+'"]>summary');if(sm)sm.textContent="Norm "+(+a[1]+1)+(n.acr.trim()?" · "+n.acr.trim():"");}
    if((a[2]==="acr"||a[2]==="value")&&ev.type==="change"){var ts=document.querySelector('#u11CocTest select');if(ts)ts.innerHTML=u11CocTestOpts(U11W.coc.test.norm);}}
  else if(a[0]==="ct"){U11W.coc.test[a[1]]=t.value;}
}
function u11CocOpen(){
  var o=[],c=U11W.coc,vs=c.vals.filter(function(x){return x.v.trim();});
  if(vs.length<3)o.push("at least three values in part 5.8 Step 1");
  if(vs.some(function(x){return !x.m.trim();}))o.push("what each value means in part 5.8 Step 1");
  c.norms.forEach(function(n,i){if(!n.value||U11_NF.some(function(f){return !n[f[0]].trim();}))o.push("every field of Norm "+(i+1)+" in part 5.8");});
  if(!c.test.norm||U11_TF.some(function(f){return !c.test[f[0]].trim();}))o.push("the three tests of your strongest norm in part 5.8");
  return o;
}
function u11CocText(){
  var c=U11W.coc;
  return ["Our values:"].concat(c.vals.filter(function(x){return x.v.trim();}).map(function(x){return x.v.trim()+": "+x.m.trim();}))
    .concat(c.norms.map(function(n,i){return "\nNorm "+(i+1)+": "+n.value+" · "+n.acr.trim()+"\nThe three actions: "+n.acts.trim()+"\nObservable behaviour: "+n.beh.trim()+"\nNorm statement: "+n.stmt.trim();}))
    .concat(["\nStrongest norm: "+c.test.norm].concat(U11_TF.map(function(f){return f[1]+": "+c.test[f[0]].trim();}))).join("\n");
}
