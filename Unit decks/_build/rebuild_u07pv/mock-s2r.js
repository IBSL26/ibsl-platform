/* Offline stand-in for the portal's save helper: keeps answers in this browser only (localStorage). Used by the PREVIEW copies only. */
(function(){
  var KEY='u7_preview_store';
  var store={};try{store=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
  // Samples of what a member's Unit 3 and Unit 2 pages hold after the group has confirmed its Enterprise OKRs and its SiP statements, so that Section 5 can show them.
  var U3_SAMPLE={
    __okr_work:{items:[
      {theme:'Customer responsiveness',obj:'Sample (preview only): Deliver consistently fast and effortless service experiences for customers',krs:[{t:'Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027'},{t:'Increase customer requests resolved at first contact from 60% to 85% by 30 September 2027'}],al:[1,1,1,1]},
      {theme:'Execution speed',obj:'Sample (preview only): Build a high-speed execution engine that moves quickly from insight to action',krs:[{t:'Reduce cross-functional decision time from 5 days to 1 day by 30 June 2027'},{t:'Reduce recurring management reports from 24 to 10 by 31 March 2027'}],al:[1,1,1,1]},
      {theme:'Collaboration culture',obj:'Sample (preview only): Create a culture of shared ownership across functions for strategic priorities',krs:[{t:'Increase enterprise priorities with a named cross-functional owner from 40% to 100% by 31 March 2027'},{t:'Reduce issues escalated to the executive team from 30 to 10 per quarter by 30 September 2027'}],al:[1,1,1,1]},
      {theme:'Value creation',obj:'Sample (preview only): Strengthen enterprise performance through scalable and efficient operations',krs:[{t:'Improve operating margin from 14% to 18% by 31 December 2027'},{t:'Reduce leadership time spent on low-value projects from 25% to 10% by 30 June 2027'}],al:[1,1,1,1]}
    ]},
    confirmed_items:['Enterprise priorities','Enterprise OKRs']
  };
  var U2_SAMPLE={
    sip_d1_st:'Sample (preview only): Customers get a fast, effortless answer the first time they contact us, on any channel.',
    sip_d2_st:'Sample (preview only): Decisions are taken close to the customer and work moves across functions without waiting.',
    sip_d3_st:'Sample (preview only): People own enterprise priorities together and raise problems early.',
    sip_d4_st:'Sample (preview only): Growth comes from loyal customers and efficient, scalable operations.',
    confirmed_items:['Strategy Architecture','Strategy Intent Statement','SiP · Customer Experience & Value','SiP · Operational Capability & Execution Rhythm','SiP · People & Culture Dynamics','SiP · Enterprise Value Creation']
  };
  function bag(lens){if(!store[lens])store[lens]=(lens==='u2m1_lens2'?JSON.parse(JSON.stringify(U3_SAMPLE)):(lens==='u2m1_lens1'?JSON.parse(JSON.stringify(U2_SAMPLE)):{}));return store[lens];}
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
