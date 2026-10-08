/* Offline stand-in for the portal's save helper: keeps answers in this browser only (localStorage). Used by the PREVIEW copies only. */
(function(){
  var KEY='u5_preview_store';
  var store={};try{store=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
  // Sample of what a member's Unit 3 page holds after the group has confirmed its KISS map, so that Step 1 can show the Start and Stop lists.
  var U3_SAMPLE={
    kiss_start:'Customer Experience & Value: Sample (preview only): resolve complaints at first contact\nOperational Capability & Execution Rhythm: Sample (preview only): a weekly review of open cases\nPeople & Culture Dynamics: Sample (preview only): decision limits for front-line agents\nEnterprise Value Creation: Sample (preview only): tracking the cost of repeat contacts',
    kiss_stop:'Customer Experience & Value: Sample (preview only): passing every complaint to the back office\nOperational Capability & Execution Rhythm: Sample (preview only): approvals by three managers for small refunds\nPeople & Culture Dynamics: Sample (preview only): rewarding call volume alone\nEnterprise Value Creation: Sample (preview only): reporting complaints closed in place of complaints resolved',
    confirmed_items:['KISS · Keep','KISS · Improve','KISS · Start','KISS · Stop']
  };
  function bag(lens){if(!store[lens])store[lens]=(lens==='u2m1_lens2'?JSON.parse(JSON.stringify(U3_SAMPLE)):{});return store[lens];}
  function chain(){var one={data:{status:'unlocked',full_name:'Preview participant'},error:null},many={data:[],error:null};
    var p={select:function(){return p;},eq:function(){return p;},order:function(){return p;},limit:function(){return p;},in:function(){return p;},
      maybeSingle:function(){return Promise.resolve(one);},single:function(){return Promise.resolve(one);},then:function(r,j){return Promise.resolve(many).then(r,j);}};return p;}
  window.__store=store;
  window.__clearPreview=function(){try{localStorage.removeItem(KEY);}catch(e){}location.reload();};
  window.S2R={
    context:function(){return Promise.resolve({profileId:'preview',cohortId:'preview',role:'participant'});},
    save:function(lens,key,val){bag(lens)[key]=JSON.parse(JSON.stringify(val));try{localStorage.setItem(KEY,JSON.stringify(store));}catch(e){}return Promise.resolve(true);},
    loadAll:function(lens){return Promise.resolve(JSON.parse(JSON.stringify(bag(lens))));},
    submit:function(){return Promise.resolve({ok:true,message:'Preview copy: nothing was sent.'});},
    _client:{from:function(){return chain();},rpc:function(){return Promise.resolve({data:[],error:null});},storage:{from:function(){return {upload:function(){return Promise.resolve({error:{message:'preview'}});},remove:function(){}};}}}
  };
})();
