// Runs the participant page script in node with a small stand-in page, and tests the 5.1 drop-downs. Usage: node js_u09s2.js <participant page>
const fs=require('fs'),vm=require('vm');
const src=fs.readFileSync(process.argv[2],'utf8');
const code=[...src.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]).find(c=>c.includes("var U9_LENS="));
let ok=0,bad=0;const check=(c,m)=>{if(c)ok++;else{bad++;console.log('FAIL',m);}};
function mkSel(){const el={tagName:'SELECT',options:[],_v:'',
  set innerHTML(h){this._h=h;this.options=[...h.matchAll(/<option value="([^"]*)">([^<]*)<\/option>/g)].map(m=>({value:m[1].replace(/&amp;/g,'&').replace(/&quot;/g,'"'),textContent:m[2]}));this.groups=[...h.matchAll(/<optgroup label="([^"]*)">/g)].map(m=>m[1]);this._v='';},
  get innerHTML(){return this._h;},appendChild(o){this.options.push(o);},
  set value(v){this._v=this.options.some(o=>o.value===v)?v:'';},get value(){return this._v;}};return el;}
function run(u1,u7,saved){
  const els={u9_ch_challenge:mkSel(),u9_ch_link:mkSel(),u9ChNote:{style:{}},u9KrNote:{style:{}}};
  const document={getElementById:id=>els[id]||null,querySelectorAll:()=>[],addEventListener:()=>{},readyState:'complete',createElement:()=>({})};
  const window={addEventListener:()=>{},S2R:{loadAll:l=>Promise.resolve(JSON.parse(JSON.stringify(l==='u1_foundations'?u1:l==='u3m1_lens6'?u7:{})))}};
  const ctx={document,window,console,setTimeout:()=>0,clearTimeout:()=>0,Promise,S2R:window.S2R,localStorage:{getItem:()=>null,setItem:()=>{}},alert:()=>{},confirm:()=>true};
  vm.createContext(ctx);vm.runInContext(code,ctx);
  vm.runInContext('U9.w=u9norm('+JSON.stringify(saved||{})+');',ctx);
  return vm.runInContext('u9Earlier()',ctx).then(()=>els);
}
const U1={__pc_work:{ch:{design:['A','B','C'],execution:['D','E'],sustain:['F']},pick:{design:['B','A','X'],execution:['E'],sustain:[]}},confirmed_items:['Problem Charter · Challenges We Will Address']};
const U7={__ex_work:{o1_obj:'Obj one',o1_kr:'KR one',o2_obj:'Obj two',o2_kr:'KR two'},confirmed_items:['Expectations · Start With the Future']};
(async()=>{
  let e=await run(U1,U7,{ch_challenge:'A',ch_link:'Objective: Obj two · Key Result: KR two'});
  const ch=e.u9_ch_challenge;
  check(ch.options.length===4,'challenge options '+JSON.stringify(ch.options));
  check(ch.groups.join('|')==='Strategy design|Strategy execution','groups '+ch.groups);
  check(ch.options[1].textContent==='1. B'&&ch.options[2].value==='A'&&ch.options[3].textContent==='1. E','numbering');
  check(ch.value==='A','saved challenge selected');
  check(e.u9_ch_link.options.length===3&&e.u9_ch_link.value==='Objective: Obj two · Key Result: KR two','KR options and saved value');
  check(!e.u9ChNote.textContent&&e.u9ChNote.style.display==='none','no note when charter agreed');
  e=await run({__pc_work:U1.__pc_work,confirmed_items:[]},{},{ch_challenge:'Old typed text'});
  check(e.u9_ch_challenge.options.length===2&&e.u9_ch_challenge.value==='Old typed text','unconfirmed charter keeps saved text as an option');
  check(/Problem Charter/.test(e.u9ChNote.textContent)&&e.u9ChNote.style.display==='block','note when charter not agreed');
  check(e.u9_ch_link.options.length===1&&/Unit 7/.test(e.u9KrNote.textContent),'KR note when Unit 7 not agreed');
  e=await run(U1,{__ex_work:{o1_kr:'Only KR'},confirmed_items:['Expectations · Start With the Future']},{});
  check(e.u9_ch_link.options[1].value==='Key Result: Only KR','KR without objective');
  console.log(ok+' passed, '+bad+' failed');
})();
