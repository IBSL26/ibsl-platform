/* Offline stand-in for the portal's save helper: keeps answers in this browser only (localStorage). Used by the PREVIEW copies only. */
(function(){
  var KEY='u9_preview_store';
  var store={};try{store=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
  // Samples of what a member's Unit 7, Unit 6 and Unit 8 pages hold after the group has confirmed its records, so that Section 5 can show them.
  var U7_SAMPLE={
    __ex_work:{o1_obj:'Sample (preview only): Deliver consistently fast and effortless service experiences for customers',o1_kr:'Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027',o1_owner:'Chief Operating Officer',o1_what:'Average response time of 4 hours across all service channels',o1_when:'30 June 2027',o1_std:'Measured monthly, every channel included',o1_evid:'The monthly service report shows an average of 4 hours or less for three months in a row',o1_score:'7',o1_score2:'9',
      o2_obj:'Sample (preview only): Strengthen enterprise performance through scalable and efficient operations',o2_kr:'Improve operating margin from 14% to 18% by 31 December 2027',o2_owner:'Chief Financial Officer',o2_what:'Operating margin of 18%',o2_when:'31 December 2027',o2_std:'Audited annual accounts',o2_evid:'The audited accounts for 2027 show an operating margin of 18% or more',o2_score:'9',o2_score2:''},
    confirmed_items:['Expectations · Start With the Future','Expectations · Delivery Expectation','Expectations · Expectations Chain','Expectations · Ownership','Expectations · Alignment Dialogue']
  };
  var U6_SAMPLE={
    __pm_work:{cad_what:'Sample (preview only): monthly Key Result reviews with each owner; a quarterly executive review across functions',cad_why:'Monthly catches early warnings while recovery is still possible; quarterly lets the executive team see the enterprise pattern.'},
    confirmed_items:['PM Architecture · Scoring Logic','PM Architecture · FACES','PM Architecture · EXECUTION','PM Architecture · Scorecards']
  };
  var U8_SAMPLE={
    rd_warning:'Decision point 1: If a Key Result shows no movement at two monthly reviews in a row, then the owner presents a recovery plan at the next executive review, taken by the CEO.\nDecision point 2: If evidence is missing from a review submission, then the review is held back one week, taken by the Key Result owner. (sample, preview only)',
    rd_accountability:'Decision point 1: If two functions report the same Key Result as on track while the enterprise result falls behind, then one owner is named, taken by the CEO. (sample, preview only)',
    rd_learning:'Decision point 1: If a review closes with no lesson recorded, then the next review opens with the lesson, taken by the COO. (sample, preview only)',
    rd_credibility:'Decision point 1: If a priority is reset twice in a quarter, then the executive team restates the trade-off to the organisation, taken by the CEO. (sample, preview only)',
    confirmed_items:['Review Discipline · Early Warning Signals','Review Discipline · Accountability','Review Discipline · Organisational Learning','Review Discipline · Leadership Credibility']
  };
  function bag(lens){if(!store[lens])store[lens]=(lens==='u3m1_lens6'?JSON.parse(JSON.stringify(U7_SAMPLE)):(lens==='u3m1_lens5'?JSON.parse(JSON.stringify(U6_SAMPLE)):(lens==='u3m2_lens7'?JSON.parse(JSON.stringify(U8_SAMPLE)):{})));return store[lens];}
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
