/* Offline stand-in for the portal database (Capstone S2R Blueprint PREVIEW only; never deployed).
   Sample team of four. Add ?admin=1 to the address to see the admin view with "Bring in agreed work". */
(function(){
  var ME = 'p-you', ADMIN = /[?&]admin=1/.test(location.search);
  if (ADMIN && !/[?&]teamId=/.test(location.search)) history.replaceState(null, '', location.pathname + '?admin=1&teamId=t-sample');
  var members = [{profile_id:'p-amara',full_name:'Amara Banda'},{profile_id:'p-peter',full_name:'Peter Mwale'},{profile_id:'p-thandi',full_name:'Thandi Nkosi'},{profile_id:ME,full_name:'You (sample)'}];
  function S(t){ return t + ' (sample text)'; }
  var content = {
    u1:{'1A':'Alpha Client Services','1B':'CEO · You (sample)\nCOO · Thandi Nkosi\nCFO · Peter Mwale\nCIO · Amara Banda','1C':S('Business services, about 1,200 staff, client onboarding and account servicing'),
        '1D':S('Strategy design: priorities change every quarter.\nStrategy execution: handovers between functions delay client requests.\nSustaining performance: improvements fade after launch.'),
        '1E':S('Leaders escalate routine decisions; teams wait for approval.'),'1F':S('Client retention fell from 91% to 84% in two years.'),
        '1G':S('Design: one set of annual priorities. Execution: clear handovers. Sustaining: quarterly reviews that hold.'),
        '1H':S('Client requests wait too long because work stalls between sales, operations and technology.')},
    u2:{'2A':S('Strategic Position · Strategic Model · Value Architecture · Strategic Navigation · Strategy Discipline'),'2B':S('Alpha resolves every client request within 48 hours by 2028, through one joined-up service team.'),
        '2C':S('Clients receive one answer, first time.'),'2D':S('Work moves between teams without waiting.'),'2E':S('People decide at the point of contact.'),'2F':S('Retention back above 90%.')},
    u12:{'12A':S('Key Result: average response time 10.5 h against a 9 h waypoint; alert raised; recovery run by the COO.'),'12B':S('ESRG: Operational Flow 2.33; alert raised; recovery owned by the CIO.'),
         '12C':S('Health 82.0, Healthy & Thriving; no alert.'),'12D':S('Keep: daily huddle (COO). Improve: handover checklist (CIO). Stop: double sign-off (CFO). Start: client panel (CEO).')}
  };
  var waitingKeys = ['u3'];   // agreed in the unit, brought in by the admin button in this preview
  function sections(){
    return ['u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12'].map(function(k){
      var c = content[k];
      return { key:k, open: !!c || k === 'u3', status: c ? 'agreed' : 'draft', content: c || {}, agreed_at: c ? '2026-10-27T18:30:00Z' : null,
               updated_at: c ? '2026-10-27T18:30:00Z' : null, updated_by_name: c ? 'Thandi Nkosi' : null,
               confirmations: c ? members.map(function(m){ return { profile_id:m.profile_id, confirmed_at:'2026-10-27T18:30:00Z' }; }) : [] };
    });
  }
  function bp(){ return { team:{ id:'t-sample', name:'Group 1 · Financial Services (sample)', reopened:false }, cohort:{ id:'c-sample', name:'CESI · November 2026 (sample)' },
    brief:{ brief_text:'Sample brief: your team leads its simulated company through the twelve units and presents its Capstone S2R Blueprint at the showcase.', submission_due:'2027-03-15T15:00:00Z', showcase_at:'2027-03-25T08:00:00Z', showcase_venue:'Lusaka (sample)' },
    locked:false, members:members, sections:sections() }; }
  function Q(table){
    var q = { _t:table, select:function(){return q;}, eq:function(){return q;}, order:function(){return q;}, in:function(){return q;},
      maybeSingle:function(){ return Promise.resolve({ data: table === 'profiles' ? { role: ADMIN ? 'admin' : 'participant' } : null, error:null }); },
      then:function(res, rej){
        var d = [];
        if (table === 'cohort_memberships') d = [{ cohort_id:'c-sample', role_in_cohort:'participant', joined_at:'2026-10-01' }];
        return Promise.resolve({ data:d, error:null }).then(res, rej);
      } };
    return q;
  }
  function rpc(name, args){
    var d = null;
    if (name === 'get_my_capstone') d = { me:ME, access_open:true, cohort:{ id:'c-sample', name:'CESI · November 2026 (sample)' }, brief:bp().brief, blueprint:bp(),
                                          score:{ capstone_pending:true, final_pct:null, certified:false }, certificate:null };
    else if (name === 'get_capstone_blueprint') d = bp();
    else if (name === 'get_capstone_team_oceavl') d = { members:4, submitted:2 };
    else if (name === 'capstone_sync_section') d = { ok:true, changed:false };
    else if (name === 'admin_capstone_bring_in'){
      var filled = [];
      waitingKeys.forEach(function(k){ if (!content[k]){ content[k] = { '3A':S('Keep: daily huddle'), '3B':S('Improve: handover checklist'), '3C':S('Start: client panel'), '3D':S('Stop: double sign-off'), '3E':S('One joined-up service team'), '3F':S('Objective: faster client service. KR: reduce response time from 20 h to 9 h by June 2027 (COO, CIO).') }; filled.push(k); } });
      d = { ok:true, filled:filled, unchanged:Object.keys(content).filter(function(k){ return filled.indexOf(k) < 0; }),
            waiting:['u4','u5','u6','u7','u8','u9','u10','u11'] };
    }
    else d = { ok:true };
    return Promise.resolve({ data:d, error:null });
  }
  window.supabase = { createClient:function(){ return {
    auth:{ getSession:function(){ return Promise.resolve({ data:{ session:{ user:{ id: ADMIN ? 'p-admin' : ME } } } }); } },
    from:Q, rpc:rpc }; } };
})();
