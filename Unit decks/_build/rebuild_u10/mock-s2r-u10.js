/* Offline stand-in for the portal's save helper and the shared group record (Unit 10 PREVIEW only):
   answers stay in this browser. The group has four members: you and three sample members whose part 4.5 scanners are filled. */
(function(){
  var KEY='u10_preview_store';
  var st={};try{st=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
  st.lens=st.lens||{};st.team=st.team||{scribe_id:null,version:0,names:[],agree:{}};
  st.lens.u1_foundations={pc_company:'Alpha Client Services (sample)',pc_team:'CEO · You\nCOO · Thandi (sample)\nCFO · Peter (sample)\nCIO · Amara (sample)',
    pc_problem:'Customer requests wait too long because work stalls between sales, operations and technology (sample).',
    __pc_work:{ch:{design:['Priorities change every quarter (sample)'],execution:['Handovers between functions delay customer requests (sample)','Decisions wait for executive approval (sample)'],sustain:['Improvements fade after launch (sample)']},
               pick:{design:['Priorities change every quarter (sample)'],execution:['Handovers between functions delay customer requests (sample)','Decisions wait for executive approval (sample)'],sustain:['Improvements fade after launch (sample)']}},
    confirmed_items:['Problem Charter · Simulated Company','Problem Charter · Executive Team','Problem Charter · Central Organisational Problem','Problem Charter · Challenges We Will Address']};
  function put(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(e){}}
  function L(l){return st.lens[l]=st.lens[l]||{};}
  var ME='preview';
  var EL=['Facilities','Infrastructure','Technology','Standardisation','Integration','Process Efficiency','Asset Availability','Investment','Resource Utilisation','Policies & Procedures','Authority','Risk Management'];
  function scan(v){return EL.map(function(e,i){return ['Annual','Q1','Q2','Q3','Q4'].map(function(p,k){return e+' · '+p+': '+(k===0?v[i]:'');}).join('\n');}).join('\n');}
  var SAMPLE=[{profile_id:'m2',full_name:'Thandi (sample)',head:'Capstone executive role: COO · Thandi (sample)\nBusiness function: Operations\nStated problem: Handovers between functions delay customer requests (sample)',scan:scan([3,2,3,3,2,3,2,3,3,4,2,4])},
              {profile_id:'m3',full_name:'Peter (sample)',head:'Capstone executive role: CFO · Peter (sample)\nBusiness function: Finance\nStated problem: Decisions wait for executive approval (sample)',scan:scan([4,4,4,4,2,4,4,4,4,4,4,4])},
              {profile_id:'m4',full_name:'Amara (sample)',head:'Capstone executive role: CIO · Amara (sample)\nBusiness function: Technology\nStated problem: Customer requests wait too long because work stalls between sales, operations and technology (sample).',scan:scan([4,4,2,3,2,3,3,3,3,4,3,4])}];
  function members(){var t=st.team;return [{profile_id:ME,full_name:'You (preview)'}].concat(SAMPLE.map(function(m){return {profile_id:m.profile_id,full_name:m.full_name};})).map(function(m){m.agreed=t.version>0&&t.agree[m.profile_id]===t.version;return m;});}
  var RPC={
    team_work_status:function(a){var t=st.team,m=members();return {team_id:'preview-team',team_name:'Preview group',me:ME,scribe_id:t.scribe_id,version:t.version,names:t.names,all_agreed:t.version>0&&m.every(function(x){return x.agreed;}),members:m};},
    team_work_set_scribe:function(a){st.team.scribe_id=a.p_scribe_id;put();return {ok:true};},
    team_work_write:function(a){var t=st.team;if(t.scribe_id!==ME)return {ok:false,error:'not_scribe'};var l=L(a.p_lens_id);
      Object.keys(a.p_items).forEach(function(k){l[k]=a.p_items[k];});
      var drop=(t.names||[]).concat(a.p_names||[]);if(Array.isArray(l.confirmed_items))l.confirmed_items=l.confirmed_items.filter(function(n){return drop.indexOf(n)<0;});
      t.version++;t.names=a.p_names;t.agree={};put();return {ok:true,version:t.version};},
    team_work_agree:function(a){var t=st.team;if(t.version!==a.p_version)return {ok:false,error:'changed'};t.agree[ME]=t.version;put();return {ok:true,all_agreed:false};},
    team_esrg_scans:function(){var me=L('u4m1_lens9');return [{profile_id:ME,full_name:'You (preview)',head:me.esrg_scan_head||null,scan:me.esrg_scan||null}].concat(SAMPLE);}
  };
  function chain(){var one={data:{status:'unlocked',full_name:'Preview participant'},error:null},many={data:[],error:null};
    var p={select:function(){return p;},eq:function(){return p;},order:function(){return p;},limit:function(){return p;},in:function(){return p;},
      maybeSingle:function(){return Promise.resolve(one);},single:function(){return Promise.resolve(one);},then:function(r,j){return Promise.resolve(many).then(r,j);}};return p;}
  window.__clearPreview=function(){try{localStorage.removeItem(KEY);}catch(e){}location.reload();};
  window.S2R={
    context:function(){return Promise.resolve({profileId:ME,cohortId:'preview',role:'participant'});},
    save:function(lens,key,val){L(lens)[key]=val;put();return Promise.resolve(true);},
    loadAll:function(lens){return Promise.resolve(JSON.parse(JSON.stringify(L(lens))));},
    submit:function(){return Promise.resolve({ok:true,message:'Preview copy: nothing was sent.'});},
    _client:{from:function(){return chain();},rpc:function(n,a){var r=RPC[n]?RPC[n](a||{}):[];return Promise.resolve({data:r,error:null});},
      storage:{from:function(){return {upload:function(){return Promise.resolve({error:{message:'preview'}});},remove:function(){},list:function(){return Promise.resolve({data:[],error:null});}};}}}
  };
})();
