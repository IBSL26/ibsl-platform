// TEST MOCK of the Supabase client (never deployed)
window.supabase={createClient:function(){
  var M=window.__MOCK;
  function q(table){
    var f={};
    var o={select:function(){return o;},eq:function(k,v){f[k]=v;return o;},in:function(k,a){f['in_'+k]=a;return o;},order:function(){return o;},
      maybeSingle:function(){return Promise.resolve({data:{role:'participant'}});},
      then:function(a,b){return Promise.resolve(run()).then(a,b);}};
    function run(){
      if(table==='cohort_memberships')return {data:[{cohort_id:'c1',role_in_cohort:'participant',joined_at:'2026-01-01'}]};
      if(table==='lens_responses'){M.log.push('lens_responses '+JSON.stringify(f));
        return {data:Object.keys(M.lr).filter(function(k){return f.in_response_key.indexOf(k)>=0;}).map(function(k){return {response_key:k,value:M.lr[k]};})};}
      return {data:[]};
    }
    return o;
  }
  function bp(){
    var keys=['u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12'];
    return {team:{id:'t1',name:'Team Baobab',reopened:false},locked:false,
      members:[{profile_id:'me',full_name:'Carol Lupiya'},{profile_id:'m2',full_name:'Brian Lupiya'}],
      sections:keys.map(function(k){ if(k!=='u2')return {key:k,open:false,status:'draft',content:{}};
        return {key:'u2',open:M.open,status:M.sec.status,content:M.sec.content,updated_at:M.sec.updated_at,updated_by_name:M.sec.updated_at?'Carol Lupiya':null,
                confirmations:M.sec.conf,sent_by_name:'Carol Lupiya',sent_at:M.sec.updated_at};})};
  }
  return {auth:{getSession:function(){return Promise.resolve({data:{session:{user:{id:'me'}}}});}},from:q,
    rpc:function(fn,a){M.log.push('rpc '+fn);
      if(fn==='get_my_capstone')return Promise.resolve({data:{access_open:true,brief:{case_name:'Impactis Consulting',brief_text:'Case brief text.'},blueprint:bp(),score:null}});
      if(fn==='capstone_save_section'){
        if((a.p_expected_updated_at||null)!==(M.sec.updated_at||null))return Promise.resolve({data:{ok:false,error:'stale',updated_at:M.sec.updated_at}});
        M.sec.content=a.p_content;M.sec.updated_at='2026-10-05T19:0'+(M.n++)+':00Z';return Promise.resolve({data:{ok:true,updated_at:M.sec.updated_at}});}
      if(fn==='capstone_send_for_confirmation'){
        var filled=Object.keys(M.sec.content).filter(function(k){return String(M.sec.content[k]).trim()!=='';}).length;
        if(filled<M.boxCount)return Promise.resolve({data:{ok:false,error:'incomplete'}});
        M.sec.status='awaiting';M.sec.conf=[{profile_id:'me',confirmed_at:'2026-10-05T19:30:00Z'}];return Promise.resolve({data:{ok:true,status:'awaiting'}});}
      return Promise.resolve({data:{ok:false}});
    }};
}};
