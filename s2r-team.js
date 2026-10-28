/**
 * S2R Team Record — shared group work (19 October 2026)
 *
 * Group work in each unit is one record per team. The group chooses its scribe for the
 * work; only the scribe types; the entries appear on every member's page; each member
 * selects Agree. When every member has agreed, the work's names go into every member's
 * confirmed list and the Capstone S2R® Blueprint brings it in.
 *
 * Needs s2r-save.js (window.S2R) loaded first. Database: team_work_* functions
 * (Claude outputs/team_work_shared_record.sql).
 *
 * Usage on a unit page:
 *   S2RTeam.attach({
 *     lens: 'u2m1_lens1',                 // the unit's lens id
 *     mount: 'teamBarP',                  // element the group bar is drawn into
 *     lock: ['u2bTool'],                  // elements whose entry boxes only the scribe may use
 *     names: [...],                       // the confirmed names the Capstone checks
 *     complete: function(){ return '' },  // '' when complete, otherwise what is still missing
 *     onRemote: async function(responses){ ... }, // redraw the tool from the group record
 *     stand: { mount:'twStand', hint:'...' }      // optional: the group's Our Position statement (28 Oct 2026)
 *   });
 *   S2RTeam.save(key, value);             // the scribe's entries (batched)
 *
 * © 2026 IBSLeadership. All rights reserved. S2R® and Strategy2Results® are registered trademarks.
 */
(function(){
  'use strict';
  var CSS='.tw-bar{background:rgba(201,168,76,.06);border:1px solid rgba(201,168,76,.28);border-radius:3px;padding:16px 18px;margin:16px 0;}'+
    '.tw-h{font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--gold,#c9a84c);margin-bottom:10px;}'+
    '.tw-row{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-bottom:10px;}'+
    '.tw-lbl{font-size:11px;color:rgba(255,255,255,.75);font-weight:600;}'+
    '.tw-sel{background:#0f1a12;color:#fff;border:1px solid rgba(26,122,106,.45);border-radius:2px;padding:7px 10px;font-family:inherit;font-size:12px;min-width:220px;}'+
    '.tw-you{font-size:11px;color:#5ecba1;font-weight:600;}'+
    '.tw-chips{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 10px;}'+
    '.tw-chip{font-size:11px;padding:4px 10px;border-radius:12px;border:1px solid rgba(255,255,255,.18);color:rgba(255,255,255,.6);}'+
    '.tw-chip.ok{border-color:rgba(94,203,161,.55);color:#5ecba1;background:rgba(94,203,161,.08);}'+
    '.tw-chip.sc{border-color:rgba(201,168,76,.6);color:var(--gold,#c9a84c);}'+
    '.tw-btn{padding:9px 20px;border-radius:2px;font-family:inherit;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;background:rgba(26,122,106,.15);border:1px solid rgba(26,122,106,.5);color:#5ecba1;}'+
    '.tw-btn[disabled]{opacity:.4;cursor:not-allowed;}'+
    '.tw-note{font-size:12px;line-height:1.7;color:rgba(255,255,255,.7);margin-top:8px;}'+
    '.tw-note.ok{color:#5ecba1;}.tw-note.warn{color:#f0c060;}'+
    '.tw-ro textarea[disabled],.tw-ro input[disabled],.tw-ro select[disabled]{opacity:.85;cursor:default;}'+
    '.tw-ro .tw-scribe-only{display:none!important;}'+
    '.tw-stand{border:1px solid rgba(201,168,76,.35);border-left:3px solid var(--gold,#c9a84c);background:rgba(201,168,76,.05);border-radius:3px;padding:16px 18px;margin:18px 0;}'+
    '.tw-stand-h{font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--gold,#c9a84c);margin-bottom:8px;}'+
    '.tw-stand p{font-size:13px;line-height:1.7;color:rgba(255,255,255,.75);margin:0 0 10px;}'+
    '.tw-stand textarea{width:100%;min-height:110px;background:rgba(0,0,0,.25);border:1px solid rgba(255,255,255,.14);border-radius:3px;color:#fff;font-family:inherit;font-size:13px;line-height:1.6;padding:10px 12px;resize:vertical;}'+
    '.tw-stand textarea[disabled]{opacity:.85;}';
  var T={cfg:null,st:null,ctx:null,q:{},timer:null,busy:false,poll:null,obs:null,msg:'',stand:''};
  var STAND_KEY='team_summary',STAND_NAME='Our Position';
  /* Our Position: the group's short summary statement of its position from the unit, in the unit's own terms. */
  function standDraw(){
    var c=T.cfg&&T.cfg.stand;if(!c)return;var host=el(c.mount);if(!host)return;
    if(!host.querySelector('#twStandTa')){
      host.innerHTML='<div class="tw-stand"><div class="tw-stand-h">Capstone work · Our Position</div>'+
        '<p>As a group, write a short summary statement of your team\'s position from this unit. Use the unit\'s own terms and the work your group has agreed above. It guides the assessors through your work.'+(c.hint?' '+esc(c.hint):'')+'</p>'+
        '<textarea id="twStandTa" placeholder="Our position from this unit…"></textarea></div>';
      var ta=host.querySelector('#twStandTa');
      ta.addEventListener('input',function(){T.stand=ta.value;API.save(STAND_KEY,ta.value);draw();});
    }
    var t=host.querySelector('#twStandTa');
    if(document.activeElement!==t&&t.value!==T.stand)t.value=T.stand;
    t.disabled=!isScribe();
  }
  function standSet(r){if(r&&typeof r[STAND_KEY]==='string')T.stand=r[STAND_KEY];}


  function el(id){return document.getElementById(id);}
  function esc(s){return String(s===undefined||s===null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
  function client(){return window.S2R&&window.S2R._client;}
  async function rpc(name,args){
    var c=client();if(!c)return null;
    try{var r=await c.rpc(name,args);if(r.error){console.error('[S2RTeam] '+name,r.error);return null;}return r.data;}
    catch(e){console.error('[S2RTeam] '+name,e);return null;}
  }
  function isScribe(){return !!(T.st&&T.st.team_id&&T.st.scribe_id&&T.st.scribe_id===T.st.me);}
  function meAgreed(){if(!T.st||!T.st.members)return false;var m=T.st.members.find(function(x){return x.profile_id===T.st.me;});return !!(m&&m.agreed);}
  function nameOf(id){var m=(T.st&&T.st.members||[]).find(function(x){return x.profile_id===id;});return m?(m.full_name||'A member'):'';}

  function applyLock(){
    if(!T.cfg)return;
    var ro=!isScribe();
    (T.cfg.lock||[]).forEach(function(id){
      var root=el(id);if(!root)return;
      root.classList.toggle('tw-ro',ro);
      root.querySelectorAll('textarea,input,select').forEach(function(f){
        if(f.closest('[data-team-free]')||f.classList.contains('p-thread-ta')||f.type==='file'||f.classList.contains('ref-ta')||f.classList.contains('reflection-textarea'))return;
        if(ro){if(!f.disabled){f.disabled=true;f.setAttribute('data-tw-off','1');}}
        else if(f.getAttribute('data-tw-off')){f.disabled=false;f.removeAttribute('data-tw-off');}
      });
      root.querySelectorAll('button').forEach(function(b){
        if(b.closest('[data-team-free]'))return;
        if(!/^\s*(\+|add\b|remove\b|delete\b|clear\b|bring\b|reload\b|rebuild\b|build\b|use\b)/i.test(b.textContent||''))return;
        if(ro){if(!b.disabled){b.disabled=true;b.setAttribute('data-tw-off','1');}}
        else if(b.getAttribute('data-tw-off')){b.disabled=false;b.removeAttribute('data-tw-off');}
      });
    });
  }
  function watchLock(){
    if(T.obs||!window.MutationObserver)return;
    T.obs=new MutationObserver(function(){if(!T._applying){T._applying=true;try{applyLock();}finally{T._applying=false;}}});
    (T.cfg.lock||[]).forEach(function(id){var r=el(id);if(r)T.obs.observe(r,{childList:true,subtree:true,attributes:true,attributeFilter:['disabled']});});
  }

  function draw(){
    if(!T.cfg)return;
    var host=el(T.cfg.mount);if(!host)return;
    var st=T.st;
    if(!st){host.innerHTML='<div class="tw-bar"><div class="tw-h">Group record</div><div class="tw-note">Loading your group…</div></div>';return;}
    if(!st.team_id){
      host.innerHTML='<div class="tw-bar"><div class="tw-h">Group record</div><div class="tw-note warn">You are not in a group yet. Your programme administrator sets the groups. Once you are in a group, your group\'s record appears here.</div></div>';
      return;
    }
    var opts='<option value="">Choose the scribe…</option>'+st.members.map(function(m){
      return '<option value="'+esc(m.profile_id)+'"'+(m.profile_id===st.scribe_id?' selected':'')+'>'+esc(m.full_name||'Member')+(m.profile_id===st.me?' (you)':'')+'</option>';
    }).join('');
    var chips=st.members.map(function(m){
      var cls='tw-chip'+(m.agreed?' ok':'')+(m.profile_id===st.scribe_id?' sc':'');
      return '<span class="'+cls+'">'+esc(m.full_name||'Member')+(m.profile_id===st.scribe_id?' · scribe':'')+(m.agreed?' · agreed ✓':'')+'</span>';
    }).join('');
    var missing=st.version>0?String(T.cfg.complete?T.cfg.complete()||'':''):'';
    var canAgree=st.version>0&&!missing&&!meAgreed();
    var note='';
    if(st.all_agreed)note='<div class="tw-note ok">✓ Every member has agreed. Your group\'s work goes into your team\'s Capstone S2R® Blueprint.</div>';
    else if(!st.scribe_id)note='<div class="tw-note">Choose your scribe for this work. The scribe types what your group agrees; the entries appear on every member\'s page.</div>';
    else if(isScribe())note='<div class="tw-note">You are the scribe. Type what your group agrees. Your entries save and appear on every member\'s page.</div>';
    else note='<div class="tw-note">'+esc(nameOf(st.scribe_id))+' is the scribe. The group\'s entries appear below as they are saved.</div>';
    if(st.version>0&&!st.all_agreed){
      if(missing)note+='<div class="tw-note warn">Still to complete before your group can agree: '+esc(missing)+'</div>';
      else if(meAgreed())note+='<div class="tw-note ok">✓ You have agreed. Waiting for the other members.</div>';
      else note+='<div class="tw-note">Read your group\'s record. When it says what your group agreed, select Agree.</div>';
    }
    if(T.msg)note+='<div class="tw-note warn">'+esc(T.msg)+'</div>';
    host.innerHTML='<div class="tw-bar"><div class="tw-h">Group record'+(st.team_name?' · '+esc(st.team_name):'')+'</div>'+
      '<div class="tw-row"><label class="tw-lbl" for="twScribe">Scribe for this work</label><select class="tw-sel" id="twScribe" data-team-free onchange="S2RTeam.setScribe(this.value)">'+opts+'</select></div>'+
      '<div class="tw-chips">'+chips+'</div>'+
      '<button type="button" class="tw-btn" id="twAgree" data-team-free onclick="S2RTeam.agree()"'+(canAgree?'':' disabled')+'>'+(meAgreed()?'✓ Agreed':'Agree')+'</button>'+
      note+'</div>';
  }

  async function refresh(pull){
    if(!T.ctx)return;
    var before=T.st?T.st.version:null,wasScribe=isScribe();
    var st=await rpc('team_work_status',{p_cohort_id:T.ctx.cohortId,p_lens_id:T.cfg.lens});
    if(st)T.st=st;
    var changed=T.st&&before!==null&&T.st.version!==before;
    if((pull||(changed&&!wasScribe))&&T.cfg.onRemote&&!Object.keys(T.q).length){
      var r={};try{r=await window.S2R.loadAll(T.cfg.lens);}catch(e){r={};}
      standSet(r);
      try{await T.cfg.onRemote(r);}catch(e){console.error('[S2RTeam] onRemote',e);}
    }
    draw();applyLock();standDraw();
  }

  async function flush(){
    clearTimeout(T.timer);T.timer=null;
    var keys=Object.keys(T.q);if(!keys.length||T.busy)return true;
    if(!isScribe()){T.q={};T.msg='Only the scribe can change the group\'s entries.';draw();return false;}
    var items=T.q;T.q={};T.busy=true;
    var r=await rpc('team_work_write',{p_cohort_id:T.ctx.cohortId,p_lens_id:T.cfg.lens,p_items:items,p_names:T.cfg.names||[]});
    T.busy=false;
    if(!r||!r.ok){
      Object.keys(items).forEach(function(k){if(!(k in T.q))T.q[k]=items[k];});
      T.msg=(r&&r.error==='not_scribe')?'Another member is now the scribe. Your last change was not saved.':'Not saved. Check your connection; the page will try again.';
      if(r&&r.error==='not_scribe')T.q={};
      await refresh(r&&r.error==='not_scribe');
      if(Object.keys(T.q).length)T.timer=setTimeout(flush,4000);
      return false;
    }
    T.msg='';
    if(T.st){T.st.version=r.version;T.st.all_agreed=false;(T.st.members||[]).forEach(function(m){m.agreed=false;});}
    draw();
    if(Object.keys(T.q).length)T.timer=setTimeout(flush,300);
    return true;
  }

  var API={
    attach:async function(cfg){
      if(cfg.stand){
        var base=cfg.complete;cfg=Object.assign({},cfg);
        cfg.names=(cfg.names||[]).concat([STAND_NAME]);
        cfg.complete=function(){var m=base?String(base()||''):'';var o=m?[m]:[];if(!String(T.stand||'').trim())o.push('Our Position');return o.join('; ');};
      }
      T.cfg=cfg;
      if(!document.getElementById('tw-css')){var s=document.createElement('style');s.id='tw-css';s.textContent=CSS;document.head.appendChild(s);}
      draw();
      try{T.ctx=window.S2R?await window.S2R.context():null;}catch(e){T.ctx=null;}
      if(!T.ctx){var h=el(cfg.mount);if(h)h.innerHTML='';return;}
      watchLock();
      if(cfg.stand){try{standSet(await window.S2R.loadAll(cfg.lens));}catch(e){}}
      await refresh(false);
      clearInterval(T.poll);T.poll=setInterval(function(){if(!T.busy&&!Object.keys(T.q).length)refresh(false);},8000);
      window.addEventListener('beforeunload',function(){if(Object.keys(T.q).length)flush();});
    },
    save:function(key,value){
      if(!T.cfg)return false;
      if(!isScribe())return false;
      T.q[key]=value;clearTimeout(T.timer);T.timer=setTimeout(flush,700);return true;
    },
    flush:flush,
    setScribe:async function(pid){
      if(!pid){draw();return;}
      await flush();
      var r=await rpc('team_work_set_scribe',{p_cohort_id:T.ctx.cohortId,p_lens_id:T.cfg.lens,p_scribe_id:pid});
      T.msg=(r&&r.ok)?'':'The scribe was not changed. Check your connection and try again.';
      await refresh(true);
    },
    agree:async function(){
      await flush();
      await refresh(false);
      if(!T.st||!T.st.version)return;
      var missing=T.cfg.complete?T.cfg.complete():'';
      if(missing){draw();return;}
      var r=await rpc('team_work_agree',{p_cohort_id:T.ctx.cohortId,p_lens_id:T.cfg.lens,p_version:T.st.version});
      T.msg=(r&&r.ok)?'':((r&&r.error==='changed')?'The record changed just now. Read it again, then select Agree.':'Not saved. Check your connection, then select Agree again.');
      await refresh(!!(r&&r.ok&&r.all_agreed));
    },
    isScribe:isScribe,
    status:function(){return T.st;},
    refresh:refresh,
    redraw:function(){draw();applyLock();standDraw();}
  };
  window.S2RTeam=API;
})();
