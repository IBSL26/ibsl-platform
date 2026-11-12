/* S2R Portal · Our company overview in Section 5 of Units 3 to 12 (12 Nov 2026).
   Shows, read-only, what the group agreed in its Problem Charter (Unit 1): the company,
   the strategy redesign trigger, the three problems and the central problem statement,
   so that every unit's Capstone work is done for the same company and problem.
   Placed just above the group record bar. Nothing is saved and no work is changed.
   © 2026 IBSLeadership. All rights reserved. S2R® and Strategy2Results® are registered trademarks. */
(function(){
  var BARS=['twBar','u10TwBar','u11TwBar','u12TwBar'];
  var AREAS=['Strategy design','Strategy execution','Sustaining performance'];
  var CSS='.s2c{border:1px solid rgba(201,168,76,.3);border-left:3px solid var(--gold,#c9a84c);border-radius:4px;background:#151c15;margin:16px 0 18px;}'+
    '.s2c-h{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:14px 16px;cursor:pointer;}'+
    '.s2c-t{font-size:10px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--gold,#c9a84c);}'+
    '.s2c-a{font-size:11px;color:rgba(255,255,255,.45);transition:transform .2s;}'+
    '.s2c.open .s2c-a{transform:rotate(180deg);}'+
    '.s2c-b{display:none;padding:0 16px 14px;}.s2c.open .s2c-b{display:block;}'+
    '.s2c-note{font-size:13px;font-style:italic;color:rgba(255,255,255,.65);margin:0 0 10px;}'+
    '.s2c-l{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold,#c9a84c);margin:14px 0 6px;}'+
    '.s2c-tb{width:100%;border-collapse:collapse;font-size:13px;}'+
    '.s2c-tb th,.s2c-tb td{text-align:left;vertical-align:top;padding:6px 8px;border-bottom:1px solid rgba(255,255,255,.07);line-height:1.55;}'+
    '.s2c-tb th{width:32%;font-size:11px;font-weight:600;color:rgba(255,255,255,.55);}'+
    '.s2c-tb td{color:rgba(255,255,255,.88);}'+
    '.s2c-p{font-size:13.5px;line-height:1.75;color:rgba(255,255,255,.9);margin:0;white-space:pre-wrap;border-left:3px solid var(--gold,#c9a84c);background:rgba(201,168,76,.05);padding:10px 12px;}'+
    '.s2c-wait{font-size:13px;color:rgba(255,255,255,.6);margin:0;}'+
    '@media print{.s2c{display:none;}}';
  function esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
  function tbl(rows){return '<table class="s2c-tb"><tbody>'+rows.map(function(r){return '<tr><th>'+esc(r[0])+'</th><td>'+esc(r[1])+'</td></tr>';}).join('')+'</tbody></table>';}
  function lines(t){return String(t||'').split('\n').map(function(l){var m=/^\s*([^:]{1,30}):\s*(.*)$/.exec(l);return m&&m[2].trim()?[m[1].trim(),m[2].trim()]:null;}).filter(Boolean);}
  /* The three problems, one per area, from the Charter's "problems we will address" entry. */
  function problems(addr){
    var o={};String(addr||'').split(/\n\s*\n/).forEach(function(b){
      var m=/^\s*(Strategy design|Strategy execution|Sustaining performance):[ \t]*(.+)$/m.exec(b),w=/^\s*Why this matters now:[ \t]*(.+)$/m.exec(b);
      if(m&&m[2].trim())o[m[1]]={p:m[2].trim(),w:w?w[1].trim():''};
    });
    return o;
  }
  function host(){
    var bar=null;for(var i=0;i<BARS.length&&!bar;i++)bar=document.getElementById(BARS[i]);
    if(!bar)return null;
    var h=document.getElementById('s2cOverview');
    if(!h){h=document.createElement('div');h.id='s2cOverview';h.className='s2c';bar.parentNode.insertBefore(h,bar);}
    return h;
  }
  function draw(h,c){
    var body;
    if(!c||!c.company){
      body='<p class="s2c-wait">Your group’s company appears here once every member of your group has agreed your Problem Charter in Unit 1.</p>';
    } else {
      var org=[['Company',c.company]].concat(lines(c.org));
      body='<p class="s2c-note">This is information from our Problem Charter. Every part of this unit’s Capstone work is done for this company and its central problem.</p>'+
        '<div class="s2c-l">Our company</div>'+tbl(org)+
        (c.trigger?'<div class="s2c-l">Our strategy redesign trigger</div>'+tbl(lines(c.trigger)):'')+
        (AREAS.some(function(a){return c.probs[a];})?'<div class="s2c-l">Our three problems</div>'+tbl(AREAS.filter(function(a){return c.probs[a];}).map(function(a){return [a,c.probs[a].p+(c.probs[a].w?'\nWhy this matters now: '+c.probs[a].w:'')];})).replace(/\n/g,'<br>'):'')+
        (c.problem?'<div class="s2c-l">Our central organisational problem</div><p class="s2c-p">'+esc(c.problem)+'</p>':'');
    }
    h.innerHTML='<div class="s2c-h" onclick="this.parentNode.classList.toggle(\'open\')"><span class="s2c-t">Our company overview</span><span class="s2c-a">▼</span></div><div class="s2c-b">'+body+'</div>';
  }
  async function load(){
    var r={};try{r=await window.S2R.loadAll('u1_foundations')||{};}catch(e){r={};}
    var conf=Array.isArray(r.confirmed_items)?r.confirmed_items:[];
    function g(k,n){return conf.indexOf(n)>=0&&typeof r[k]==='string'?r[k].trim():'';}
    return {company:g('pc_company','Problem Charter · Simulated Company'),org:g('pc_org','Problem Charter · Our Organisation'),
            trigger:g('pc_trigger','Problem Charter · Strategy Redesign Trigger'),
            probs:problems(g('pc_address','Problem Charter · Challenges We Will Address')),
            problem:g('pc_problem','Problem Charter · Central Organisational Problem')};
  }
  var tries=0;
  async function start(){
    var h=host();
    if(!h||!window.S2R||!window.S2R.loadAll){if(++tries<60)setTimeout(start,500);return;}
    if(!document.getElementById('s2c-css')){var s=document.createElement('style');s.id='s2c-css';s.textContent=CSS;document.head.appendChild(s);}
    var ctx=null;try{ctx=window.S2R.context?await window.S2R.context():true;}catch(e){ctx=null;}
    if(!ctx){if(++tries<60)setTimeout(start,1000);return;}
    draw(h,await load());
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
})();
