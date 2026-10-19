// Runs every script of a page in node with a permissive stand-in page and fires DOMContentLoaded and load; reports any error. Usage: node smoke_u09s2.js <page>
const fs=require('fs'),vm=require('vm');
const src=fs.readFileSync(process.argv[2],'utf8');
const scripts=[...src.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
function el(){const t={};return new Proxy(function(){},{get(_,k){if(k in t)return t[k];if(k==='style'||k==='dataset')return t[k]={};if(k==='classList')return {add(){},remove(){},toggle(){},contains(){return false}};if(k==='options'||k==='children')return [];if(k==='value'||k==='textContent'||k==='innerHTML')return '';if(k==='tagName')return 'DIV';if(k===Symbol.toPrimitive)return ()=>'';return (...a)=>el();},set(_,k,v){t[k]=v;return true;},apply(){return el();}});}
const L={};const add=(k,f)=>{(L[k]=L[k]||[]).push(f)};
const document={getElementById:()=>el(),querySelector:()=>el(),querySelectorAll:()=>[],addEventListener:add,readyState:'loading',createElement:()=>el(),body:el()};
const store={};
const window={addEventListener:add,open:()=>null,scrollTo(){},print(){}};
const ctx={document,window,console,setTimeout:(f)=>0,clearTimeout(){},Promise,JSON,localStorage:{getItem:()=>null,setItem(){},removeItem(){}},alert(){},confirm:()=>true,location:{reload(){},href:''}};
Object.assign(ctx,window);ctx.window=ctx;vm.createContext(ctx);
let err=0;
for(const [i,c] of scripts.entries()){try{vm.runInContext(c,ctx);}catch(e){err++;console.log('script',i,'ERROR',e.message);}}
(async()=>{for(const k of ['DOMContentLoaded','load'])for(const f of (L[k]||[])){try{await f({});}catch(e){err++;console.log(k,'ERROR',e.message);}}
console.log('errors:',err);})();
