/* s2r-rectable.js · Group record display standard (20 Nov 2026).
 * Display only: draws a unit's "Your group's record" as one standard layout in every unit
 * (heading with the agreement badge, each part opening and closing, a clean table inside).
 * It reads text the unit already builds; it saves nothing and does not touch the scribe/Agree process. */
(function(){
  var CSS='.s2r-rt{width:100%;border-collapse:collapse;margin:10px 0 8px;font-size:12.5px;line-height:1.6;}'+
  '.s2r-rt th,.s2r-rt td{padding:8px 12px;border:1px solid rgba(255,255,255,.09);vertical-align:top;text-align:left;}'+
  '.s2r-rt .rt-k{width:32%;font-weight:600;color:rgba(255,255,255,.88);background:rgba(255,255,255,.03);}'+
  '.s2r-rt .rt-v{color:rgba(255,255,255,.8);white-space:pre-wrap;overflow-wrap:anywhere;}'+
  '.s2r-rt i{color:rgba(255,255,255,.35);}'+
  '.s2r-rt tr.rt-s th,.s2r-rt tr.rt-s td{background:rgba(94,203,161,.10);color:#fff;font-weight:700;white-space:pre-wrap;}'+
  '.s2r-rt tr.rt-s th{width:32%;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.75);}.s2r-rt tr.rt-s th[colspan]{width:auto;}'+
  '.s2r-rec-out{border:1px solid rgba(255,255,255,.1);border-radius:4px;padding:14px 16px;margin:18px 0 14px;}'+
  '.s2r-rec-h{font-size:10px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:rgba(255,255,255,.55);margin:0 0 8px;}'+
  '.s2r-conf{display:inline-block;font-size:9px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;border-radius:2px;padding:3px 8px;margin-left:8px;}'+
  '.s2r-conf.yes{background:rgba(39,174,96,.15);color:#5ecba1;}.s2r-conf.no{background:rgba(255,255,255,.07);color:rgba(255,255,255,.5);}'+
  '.s2r-recd{border-top:1px solid rgba(255,255,255,.07);padding:8px 0;}'+
  '.s2r-recd summary{cursor:pointer;font-size:12.5px;font-weight:700;color:#fff;line-height:1.6;}'+
  '.s2r-recd summary span{font-weight:400;color:rgba(255,255,255,.55);margin-left:8px;}'+
  '@media(max-width:640px){.s2r-rt .rt-k{width:40%;}}';
  function addCss(){if(document.getElementById('s2r-rt-css'))return;var s=document.createElement('style');s.id='s2r-rt-css';s.textContent=CSS;(document.head||document.documentElement).appendChild(s);}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',addCss);else addCss();
  function esc(t){return String(t==null?'':t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
  var EMPTY='<i>to be agreed by your group</i>';
  function row(k,v){return '<tr><td class="rt-k">'+esc(k)+'</td><td class="rt-v">'+(String(v||'').trim()?esc(v):EMPTY)+'</td></tr>';}
  function band(k,v){return v==null?'<tr class="rt-s"><th colspan="2">'+esc(k)+'</th></tr>':'<tr class="rt-s"><th>'+esc(k)+'</th><td>'+(String(v).trim()?esc(v):EMPTY)+'</td></tr>';}
  /* Text of "Label: answer" lines becomes table rows. A line with no label that opens a block becomes a band;
     one that follows an answer continues that answer. opts.band(label,line) marks other band lines. */
  function table(text,opts){
    opts=opts||{};var rows=[],start=true;
    String(text||'').replace(/\r/g,'').split('\n').forEach(function(l){
      if(!l.trim()){start=true;return;}
      var i=l.indexOf(': '),k=i<0?l.trim():l.slice(0,i).trim(),v=i<0?null:l.slice(i+2);
      if(opts.band&&opts.band(k,l)){rows.push({b:1,k:k,v:v});start=false;return;}
      if(i<0){if(start||!rows.length)rows.push({b:1,k:k,v:null});else{var r=rows[rows.length-1];r.v=(r.v?r.v+'\n':'')+l;}start=false;return;}
      rows.push({k:k,v:v});start=false;
    });
    if(!rows.length)return '<table class="s2r-rt"><tbody><tr><td class="rt-v" colspan="2">'+EMPTY+'</td></tr></tbody></table>';
    return '<table class="s2r-rt"><tbody>'+rows.map(function(r){return r.b?band(r.k,r.v):row(r.k,r.v);}).join('')+'</tbody></table>';
  }
  function rows(list){return '<table class="s2r-rt"><tbody>'+list.map(function(r){return r[2]?band(r[0],r[1]):row(r[0],r[1]);}).join('')+'</tbody></table>';}
  function part(title,inner,note){return '<details class="s2r-recd"><summary>'+esc(title)+(note?'<span>'+esc(note)+'</span>':'')+'</summary>'+inner+'</details>';}
  function head(conf,title){return '<div class="s2r-rec-h">'+(title===false?'':esc(title||'Your group’s record'))+(conf?'<span class="s2r-conf yes">Agreed by every member &middot; into your Capstone</span>':'<span class="s2r-conf no">Not yet agreed by every member</span>')+'</div>';}
  /* Keeps open parts open when the record redraws. */
  function set(host,html){
    if(!host)return;if(host.__rt===html)return;
    var open=[].slice.call(host.querySelectorAll('details.s2r-recd')).map(function(d){return d.open;});
    host.innerHTML=html;host.__rt=html;
    [].slice.call(host.querySelectorAll('details.s2r-recd')).forEach(function(d,i){if(open[i])d.open=true;});
  }
  window.S2RRec={esc:esc,table:table,rows:rows,part:part,head:head,set:set};
})();
