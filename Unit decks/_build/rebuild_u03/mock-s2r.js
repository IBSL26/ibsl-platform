/* Offline stand-in for the portal's save helper: keeps answers in this browser only (localStorage), one store per unit. */
(function(){
  var KEY='u3_preview_store';
  var store={};try{store=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
  // Sample of what a member's Unit 2 page holds, so that 4.1 can show the bring-in.
  var U2_SAMPLE={
    sip_d1_st:'Sample (preview only): Clients receive a response within four hours and describe us as the partner that makes their work easier.',
    sip_d2_st:'Sample (preview only): Decisions that involve several functions are taken within one day, and priorities are reviewed in one weekly forum.',
    sip_d3_st:'Sample (preview only): Leaders own enterprise priorities together, and teams raise issues early without escalation.',
    sip_d4_st:'Sample (preview only): Revenue from retained clients grows each year and margins hold as the business scales.'
  };
  function bag(lens){if(!store[lens])store[lens]=(lens==='u2m1_lens1'?JSON.parse(JSON.stringify(U2_SAMPLE)):{});return store[lens];}
  function chain(){var one={data:{status:'unlocked',full_name:'Preview participant'},error:null},many={data:[],error:null};
    var p={select:function(){return p;},eq:function(){return p;},order:function(){return p;},limit:function(){return p;},in:function(){return p;},
      maybeSingle:function(){return Promise.resolve(one);},single:function(){return Promise.resolve(one);},then:function(r,j){return Promise.resolve(many).then(r,j);}};return p;}
  window.__store=store;
  window.S2R={
    context:function(){return Promise.resolve({profileId:'preview',cohortId:'preview',role:'participant'});},
    save:function(lens,key,val){bag(lens)[key]=JSON.parse(JSON.stringify(val));try{localStorage.setItem(KEY,JSON.stringify(store));}catch(e){}return Promise.resolve(true);},
    loadAll:function(lens){return Promise.resolve(JSON.parse(JSON.stringify(bag(lens))));},
    submit:function(){return Promise.resolve({ok:true,message:'Preview copy: nothing was sent.'});},
    _client:{from:function(){return chain();},rpc:function(){return Promise.resolve({data:[],error:null});},storage:{from:function(){return {upload:function(){return Promise.resolve({error:{message:'preview'}});},remove:function(){}};}}}
  };
})();
