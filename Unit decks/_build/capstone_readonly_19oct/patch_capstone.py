# -*- coding: utf-8 -*-
"""Capstone page read-only for participants; sections fill from the agreed unit work (capstone_sync_section). 19 Oct 2026."""
import sys
src,out=sys.argv[1:3]
s=open(src,encoding='utf-8',newline='').read()
CR='\r\n' in s
s=s.replace('\r\n','\n')
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
once("""      ['4D','mbt_value','MBT · Value Proposition']
    ]},""","""      ['4D','mbt_value','MBT · Value Proposition'],
      ['4E','mbt_verify','MBT · Verification Ownership'],
      ['4F','mbt_blind','MBT · Executive Blind Spot']
    ]},""")
once("""    u5: { lens:'u3m1_lens4', rows:[
      ['5B','kit_mind','Alignment Plan · Mind'],""","""    u5: { lens:'u3m1_lens4', rows:[
      ['5A','kit_profile','Alignment Plan · Team Profile'],
      ['5B','kit_mind','Alignment Plan · Mind'],""")
once("    var editable = isMember && st === 'draft' && !S.bp.locked;","    var editable = false;   // participants read the Blueprint; it fills from the agreed unit work")
old="""    if (editable && PULL[sec.key]) h += '<div class="pull no-print"><p class="sec-note">Your confirmed outputs from Unit ' + def.unit + ' are brought in from your Unit ' + def.unit + ' page. Read them as a team, then send for team confirmation.</p>' +
      '<button class="btn" onclick="capPull(\\'' + sec.key + '\\')">Bring in from my Unit ' + def.unit + ' page</button></div>';"""
new="""    if (isMember && st !== 'locked' && st !== 'agreed') h += '<p class="sec-note">This section fills from Section 5 of your Unit ' + def.unit + ' page once every member of your group has agreed the work there.</p>';"""
once(old,new)
once("""    if (st === 'awaiting') h += '<p class="sec-note">Awaiting confirmation""","""    if (st === 'awaiting' && !isMember) h += '<p class="sec-note">Awaiting confirmation""")
once("""    if (st === 'agreed') h += '<p class="sec-note">Agreed · ' + esc(fmtDateTime(sec.agreed_at)) + '</p>';""",
     """    if (st === 'agreed') h += '<p class="sec-note">' + (isMember ? 'Agreed by every member in Unit ' + def.unit + ' · ' : 'Agreed · ') + esc(fmtDateTime(sec.agreed_at)) + '</p>';""")
once("""    if (st !== 'locked' && sec.updated_by_name) h += '<div class="meta">Last saved by""","""    if (st !== 'locked' && sec.updated_by_name && !isMember) h += '<div class="meta">Last saved by""")
once("""    if (st === 'awaiting' || st === 'agreed'){
      h += '<div class="confirms">';""","""    if (!isMember && (st === 'awaiting' || st === 'agreed')){
      h += '<div class="confirms">';""")
old2="""    if (isMember && !S.bp.locked){
      if (st === 'draft'){"""
new2="""    if (false){
      if (st === 'draft'){"""
once(old2,new2)
# replace autoPull with autoSync
i=s.find('  // First opening of an empty Draft: bring the full confirmed set in and save it as the team\'s draft.')
j=s.find('  // The button: bring in again from this member\'s unit page.')
assert 0<i<j
s=s[:i]+"""  // Each open section fills from the unit work the whole group has agreed (database function capstone_sync_section).
  function contentEqual(a, b){ a = a || {}; b = b || {}; var ka = Object.keys(a).filter(function(k){ return String(a[k]||'').trim(); }), kb = Object.keys(b); if (ka.length !== kb.length) return false; return kb.every(function(k){ return String(a[k]||'').trim() === String(b[k]||'').trim(); }); }
  function autoPull(){
    if (S.mode !== 'participant' || !S.bp || S.bp.locked || S.syncing) return;
    var todo = (S.bp.sections || []).filter(function(sec){ return PULL[sec.key] && statusOf(sec) !== 'locked' && !S.pulled[sec.key]; });
    if (!todo.length) return;
    S.syncing = true;
    var changed = false;
    var run = todo.reduce(function(p, sec){
      return p.then(function(){
        var key = sec.key; S.pulled[key] = true;
        return readUnitOutputs(key).then(function(o){
          if (!o || o.missing.length) return;
          var want = {}; o.ready.forEach(function(x){ want[x.box] = x.text; });
          if (statusOf(sec) === 'agreed' && contentEqual(sec.content, want)) return;
          var map = {}; PULL[key].rows.forEach(function(r){ map[r[0]] = r[1]; });
          return sb.rpc('capstone_sync_section', { p_team_id: S.bp.team.id, p_key: key, p_map: map }).then(function(res){
            var d = res.error ? { ok:false, error:'rpc' } : (res.data || { ok:false });
            if (res.error) console.warn('[capstone] sync ' + key + ':', res.error);
            if (d.ok && d.changed) changed = true;
          });
        });
      });
    }, Promise.resolve());
    run.then(function(){ S.syncing = false; if (changed) reload(); });
  }

"""+s[j:]
open(out,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if CR else s)
print('ok')
# (19 Oct) intro text
s2=open(out,encoding='utf-8',newline='').read()
a='Agree the content together, enter it, and confirm it as a team.'
if s2.count(a)==2: s2=s2.replace(a,'It fills from the Section 5 work your group agrees on each unit page.'); open(out,'w',encoding='utf-8',newline='').write(s2)
