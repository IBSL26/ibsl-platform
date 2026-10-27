// Logic checks of Section 5 (device shell has no browser): parsing, averages, N/A, missing, open items, Capstone texts, scribe saving.
const fs=require('fs'),vm=require('vm');
const saved={};let scribe=true;
const ctx={console,document:{getElementById:()=>null,querySelectorAll:()=>[],querySelector:()=>null,activeElement:null},
  window:{},confirm:()=>true,setTimeout};
ctx.window.S2RTeam={isScribe:()=>scribe,save:(k,v)=>{if(!scribe)return false;saved[k]=v;return true;},status:()=>null};
ctx.S2RTeam=ctx.window.S2RTeam;
vm.createContext(ctx);vm.runInContext(fs.readFileSync('u10_s5.js','utf8')+';this.T={get M(){return U10M},set M(v){U10M=v},get W(){return U10W},set W(v){U10W=v},set L(v){U10Loaded=v},u10Parse,u10Cap,u10Ent,u10Count,u10Open,u10Texts,u10Out,u10Norm,u10Missing};',ctx);
const T=ctx.T;let ok=0,bad=0;function chk(n,c){if(c)ok++;else{bad++;console.log('FAIL',n);}}
const EL=["Facilities","Infrastructure","Technology","Standardisation","Integration","Process Efficiency","Asset Availability","Investment","Resource Utilisation","Policies & Procedures","Authority","Risk Management"];
function scan(vals,per){return EL.map((e,i)=>e+' · '+(per||'Annual')+': '+(vals[i]==null?'':vals[i])).join('\n');}
function mem(name,role,fn,vals){return {id:name,name,role,fn,map:T.u10Parse(scan(vals))};}
// her illustrative columns: Finance, Operations, Commercial, HR, Technology
const fin=[4,4,4,4,2,4,4,4,4,4,4,4],ops=[3,2,3,3,2,3,2,3,3,4,2,4],com=[4,4,4,4,2,3,4,4,3,4,3,4],hr=[4,4,4,4,3,4,4,4,4,4,4,4],tec=[4,4,2,3,2,3,3,3,3,4,3,4];
T.M=[mem('A','CFO · A','Finance',fin),mem('B','COO · B','Operations',ops),mem('C','CCO · C','Commercial',com),mem('D','CHRO · D','HR',hr),mem('E','CIO · E','Technology',tec)];
T.L=true;
const caps=[0,1,2,3].map(d=>T.M.map(m=>T.u10Cap(m,d,0).toFixed(2)));
chk('Operations readiness 2.67',caps[0][1]==='2.67');chk('Technology readiness 3.33',caps[0][4]==='3.33');chk('Finance flow 3.33',caps[1][0]==='3.33');
chk('Enterprise readiness 3.60',T.u10Ent(0,0).toFixed(2)==='3.60');chk('Enterprise flow 3.07',T.u10Ent(1,0).toFixed(2)==='3.07');
chk('Enterprise capacity 3.47',T.u10Ent(2,0).toFixed(2)==='3.47');chk('Enterprise governance 3.73',T.u10Ent(3,0).toFixed(2)==='3.73');
// missing member: blank stays blank, enterprise average over assessed functions only
const part=fin.slice();part[1]=null;T.M=T.M.concat([mem('F','CMO · F','Marketing',part)]);
chk('incomplete member capability is null',T.u10Cap(T.M[5],0,0)===null);chk('blank not counted as zero',T.u10Ent(0,0).toFixed(2)==='3.60');
chk('missing listed',T.u10Missing().length===1&&T.u10Count(T.M[5],0)===11);
// N/A excluded from average
const na=hr.slice();na[0]='N/A';const g=mem('G','CSO · G','Strategy',na);chk('N/A excluded',T.u10Cap(g,0,0)===4);
const allna=hr.slice();allna[0]=allna[1]=allna[2]='N/A';chk('all N/A domain',T.u10Cap(mem('H','x','y',allna),0,0)==='na');
// open items and saving
T.W=T.u10Norm(null);let o=T.u10Open();chk('open lists gaps, findings, response, plan',o.length===4&&/missing submissions/.test(o[0])&&/0 of 12/.test(o[1]));
T.u10Out();chk('working record saved, texts not yet',saved.__es_work&&!saved.es_scanner);
const W=T.W;W.gaps='CMO has not scored Infrastructure.';W.interp=W.interp.map(r=>r.map((x,k)=>'Finding '+k));
Object.assign(W.resp[0],{dom:'Systems',comp:'Integration',finding:'f',commit:'c',response:'Agree a connected workflow',functions:'COO, CCO',actions:'a',owner:'COO · B',contrib:'CCO',date:'2027-03-31',evidence:'e'});
chk('complete',T.u10Open().length===0);T.u10Out();
chk('four Capstone texts saved',['es_scanner','es_interp','es_resp','es_plan'].every(k=>typeof saved[k]==='string'&&saved[k].length>10));
chk('scanner text has enterprise avg',/Operational Readiness \(Environment\):.*Enterprise avg\. 3\.60/.test(saved.es_scanner));
chk('scanner text has gaps',/Missing submissions or evidence gaps: CMO/.test(saved.es_scanner));
chk('resp text',/Response 1: Systems · Operational Flow · Integration/.test(saved.es_resp));
chk('plan traces response',/Intervention 1 \(from Response 1\): Agree a connected workflow/.test(saved.es_plan)&&/Target date: 2027-03-31/.test(saved.es_plan));
// unchanged record is not saved again
for(const k in saved)delete saved[k];T.u10Out();chk('no repeat save when unchanged',Object.keys(saved).length===0);
// a member's score change reaches the scanner text
T.M[1].map['Infrastructure · Annual']='4';T.u10Out();chk('member change re-saves scanner only',saved.es_scanner&&!saved.es_interp);
// non-scribe never saves
for(const k in saved)delete saved[k];scribe=false;W.gaps='x';T.u10Out();chk('non-scribe saves nothing',Object.keys(saved).length===0);
// incomplete response blocks
scribe=true;W.resp.push(T.u10Norm(null).resp[0]);chk('second empty response blocks',T.u10Open().some(x=>/Response 2/.test(x))&&T.u10Open().some(x=>/Intervention 2/.test(x)));
console.log(ok+' passed, '+bad+' failed');process.exit(bad?1:0);
