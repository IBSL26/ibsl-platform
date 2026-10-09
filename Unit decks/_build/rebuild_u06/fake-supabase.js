/* Stand-in for the Supabase library, for testing only. One small database kept in this browser (localStorage),
   shared by every page of the test site, so that what one page saves the next page reads. Values go through JSON, as jsonb does. */
(function(){
  var KEY='fakedb';
  function db(){var d;try{d=JSON.parse(localStorage.getItem(KEY)||'null');}catch(e){d=null;}return d||{};}
  function put(d){localStorage.setItem(KEY,JSON.stringify(d));}
  function uid(){return localStorage.getItem('fake_uid')||'';}
  function log(x){var l=[];try{l=JSON.parse(localStorage.getItem('fake_log')||'[]');}catch(e){}l.push(x);localStorage.setItem('fake_log',JSON.stringify(l));}
  function Q(table){this.t=table;this.f=[];this.o=null;this.n=null;this.one=false;}
  Q.prototype.select=function(){return this;};
  Q.prototype.eq=function(c,v){this.f.push(function(r){return r[c]===v;});return this;};
  Q.prototype.in=function(c,a){this.f.push(function(r){return a.indexOf(r[c])!==-1;});return this;};
  Q.prototype.order=function(c,o){this.o=[c,!o||o.ascending!==false];return this;};
  Q.prototype.limit=function(n){this.n=n;return this;};
  Q.prototype.maybeSingle=function(){this.one=true;return this;};
  Q.prototype.single=function(){this.one=true;return this;};
  Q.prototype.run=function(){
    var rows=(db()[this.t]||[]).filter(function(r){return this.f.every(function(f){return f(r);});},this);
    if(this.o){var c=this.o[0],asc=this.o[1];rows.sort(function(a,b){return (a[c]<b[c]?-1:a[c]>b[c]?1:0)*(asc?1:-1);});}
    if(this.n!==null)rows=rows.slice(0,this.n);
    log({read:this.t,rows:rows.length});
    return {data:this.one?(rows[0]||null):rows,error:null};
  };
  Q.prototype.then=function(a,b){return Promise.resolve(this.run()).then(a,b);};
  Q.prototype.upsert=function(row,opt){
    var d=db(),t=d[this.t]=d[this.t]||[],keys=String((opt&&opt.onConflict)||'id').split(',');
    row=JSON.parse(JSON.stringify(row));
    var i=t.findIndex(function(r){return keys.every(function(k){return r[k]===row[k];});});
    if(i>=0)t[i]=Object.assign(t[i],row);else t.push(row);
    put(d);log({write:this.t,key:row.response_key});return Promise.resolve({data:null,error:null});
  };
  Q.prototype.insert=function(row){
    var d=db(),t=d[this.t]=d[this.t]||[];row=JSON.parse(JSON.stringify(row));
    row.id=row.id||('id-'+(t.length+1));if(this.t==='submissions'&&!row.submitted_at)row.submitted_at=new Date().toISOString();
    t.push(row);put(d);log({write:this.t});return Promise.resolve({data:null,error:null});
  };
  function boxes(key){var d=db();return (d.box_count&&d.box_count[key])||5;}
  function name(id){var p=(db().profiles||[]).find(function(r){return r.id===id;});return p?p.full_name:'';}
  var RPC={
    get_my_capstone:function(){var c=db().capstone;return JSON.parse(JSON.stringify({access_open:true,brief:c.brief,cohort:c.cohort,score:null,blueprint:{team:c.team,locked:false,members:c.members,sections:c.sections}}));},
    get_capstone_team_oceavl:function(){return {members:2,submitted:0};},
    capstone_save_section:function(a){
      var d=db(),s=d.capstone.sections.find(function(x){return x.key===a.p_key;});
      if(!s||!s.open)return {ok:false,error:'section_closed'};
      if((s.status||'draft')!=='draft')return {ok:false,error:'not_draft'};
      if(s.updated_at&&a.p_expected_updated_at!==s.updated_at)return {ok:false,error:'stale',updated_at:s.updated_at};
      s.content=JSON.parse(JSON.stringify(a.p_content||{}));s.updated_at=new Date().toISOString();s.updated_by_name=name(uid());
      put(d);log({rpc:'capstone_save_section',key:a.p_key,boxes:Object.keys(s.content)});return {ok:true};
    },
    capstone_send_for_confirmation:function(a){
      var d=db(),s=d.capstone.sections.find(function(x){return x.key===a.p_key;});
      var filled=Object.keys(s.content||{}).filter(function(k){return String(s.content[k]||'').trim()!=='';}).length;
      if(filled<boxes(a.p_key))return {ok:false,error:'incomplete'};
      s.status='awaiting';s.sent_by_name=name(uid());s.sent_at=new Date().toISOString();s.confirmations=[{profile_id:uid(),confirmed_at:s.sent_at}];
      put(d);return {ok:true,status:'awaiting'};
    },
    capstone_confirm_section:function(a){
      var d=db(),s=d.capstone.sections.find(function(x){return x.key===a.p_key;});
      if(s.status!=='awaiting')return {ok:false,error:'not_awaiting'};
      if(!s.confirmations.some(function(c){return c.profile_id===uid();}))s.confirmations.push({profile_id:uid(),confirmed_at:new Date().toISOString()});
      if(s.confirmations.length>=d.capstone.members.length){s.status='agreed';s.agreed_at=new Date().toISOString();}
      put(d);return {ok:true,status:s.status};
    }
  };
  var client={
    auth:{getSession:function(){var u=uid();return Promise.resolve({data:{session:u?{user:{id:u}}:null},error:null});},
          onAuthStateChange:function(){return {data:{subscription:{unsubscribe:function(){}}}};}},
    from:function(t){return new Q(t);},
    rpc:function(n,a){var r=RPC[n]?RPC[n](a||{}):[];return Promise.resolve({data:r,error:null});},
    storage:{from:function(){return {upload:function(){return Promise.resolve({error:{message:'test'}});},remove:function(){return Promise.resolve({});}};}}
  };
  window.supabase={createClient:function(){return client;}};
})();
