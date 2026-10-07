/* Offline stand-in for the portal's save helper: keeps answers in this browser only (localStorage). Used by the PREVIEW copies only. */
(function(){
  var KEY='u4_preview_store';
  var store={};try{store=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
  // Sample of what a member's Unit 3 page holds after the group has confirmed its Enterprise OKRs, so that 4.2 can show the bring-in.
  function okr(theme,obj,krs){return {theme:theme,obj:obj,krs:krs.map(function(t){return {t:t,r:''};}).concat([{t:'',r:''},{t:'',r:''}]).slice(0,2),al:[true,true,true,true],im:'High',ef:'Medium'};}
  var U3_SAMPLE={
    __okr_work:{step:4,items:[
      okr('Sample theme','Sample (preview only): Become the easiest lender for small businesses to deal with',['Reduce loan decision time from 10 days to 2 days by 30 June 2027','Increase applications completed online from 35% to 80% by 30 September 2027']),
      okr('Sample theme','Sample (preview only): Grow a loan book that performs through the cycle',['Reduce loans in arrears from 9% to 5% by 31 December 2027']),
      {theme:'',obj:'',krs:[{t:'',r:''},{t:'',r:''}],al:[false,false,false,false],im:'',ef:''},
      {theme:'',obj:'',krs:[{t:'',r:''},{t:'',r:''}],al:[false,false,false,false],im:'',ef:''}]},
    confirmed_items:['KISS · Keep','KISS · Improve','KISS · Start','KISS · Stop','Enterprise priorities','Enterprise OKRs']
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
