# -*- coding: utf-8 -*-
"""Unit 5 amendments (8 October 2026, evening): the Capstone, the Learning Portfolio and the facilitator report follow the amended unit.
Usage: python3 patch_links_b.py <dashboard_F.html> <capstone_P.html> <build_collection.js> <output folder>
Run it from this folder (it reads u5b_content.py and oceavl.json) on the files as patch_links.py left them.
Byte-exact: every edit must match exactly once or nothing is written. Line endings are kept. Then run `node build_collection.js`.
The team OCEAVL profile needs the database function in `Claude outputs\\capstone_unit5_oceavl.sql` (Carol runs it in Supabase)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import u5b_content as B
dash, cap, bc, out = sys.argv[1:5]
def patch(path, edits, NL):
    b = open(path, 'rb').read().decode('utf-8')
    for old, new in edits:
        old, new = old.replace('\n', NL), new.replace('\n', NL)
        n = b.count(old)
        assert n == 1, 'expected 1 match, found %d in %s: %s' % (n, os.path.basename(path), old[:80])
        b = b.replace(old, new)
    open(os.path.join(out, os.path.basename(path)), 'wb').write(b.encode('utf-8'))
    print('written', os.path.basename(path), len(b))

# ── dashboard_F.html: headings and labels for the new saved answers (the Learning Portfolio takes its labels from here) ──
patch(dash, [
    ("      { name: 'Working Papers',           test: function (k) { return /^syn_(themes|disagree|top5)$/i.test(k)",
     "      { name: 'OCEAVL Assessment',        test: function (k) { return /^oceavl_(scores|profile)$/i.test(k); } },\n"
     "      { name: 'Alignment Toolkit',        test: function (k) { return /^kit_(me|team|mind|heart|hands|habit)$/i.test(k); } },\n"
     "      { name: 'Working Papers',           test: function (k) { return /^syn_(themes|disagree|top5)$/i.test(k)"),
    ("      ref15: 'One Voice · Change Load',\n",
     "      ref15: 'One Voice · Change Load',\n"
     "      ref16: 'OCEAVL · Own Level With the Highest Risk',\n"
     "      oceavl_scores: 'OCEAVL · own scores, 1 to 5',\n"
     "      oceavl_profile: 'OCEAVL · own profile (portfolio work)',\n"
     "      kit_me: 'Alignment Toolkit · Your Watch List (portfolio work)',\n"
     "      kit_team: 'Team Alignment Plan — record while the group works',\n"
     "      kit_mind: 'Team Alignment Plan · Mind (3S) — confirmed',\n"
     "      kit_heart: 'Team Alignment Plan · Heart (SCARF) — confirmed',\n"
     "      kit_hands: 'Team Alignment Plan · Hands (STAT) — confirmed',\n"
     "      kit_habit: 'Team Alignment Plan · Habit (ACE-IT) — confirmed',\n"),
    ("      syn_30day: 'Synthesis · 30-Day Behavioural Commitment',\n      confirmed_items: 'Confirmed by the group'\n    },\n",
     "      syn_30day: '30-Day Behavioural Commitment',\n      confirmed_items: 'Submitted and confirmed (OCEAVL scores, Team Alignment Plan)'\n    },\n"),
    ('      u3m1_lens4: {7:"COMPASS Diagnostic"},\n', '      u3m1_lens4: {7:"COMPASS Diagnostic",16:"OCEAVL · Own Level With the Highest Risk"},\n'),
], '\r\n')

# ── capstone_P.html: Unit 5 section. 5A is typed by the team under the team OCEAVL profile; 5B to 5E come from the confirmed Team Alignment Plan. ──
plan = lambda tool: 'State the %s triggers most likely to surface as [Case] implements its strategy: where each will surface, what the executive team will do and the leader who owns it.' % tool
OC = json.dumps([{'n': d['name'], 'lv': {l['level']: [l['dna'], l['risk'], l['resp'], l['rout']] for l in d['levels']}} for d in B.OCEAVL], ensure_ascii=False, separators=(',', ':'))
JS = r'''  // === Unit 5 · the team's OCEAVL profile (personal scores, read together once every member has submitted) ===
  var OCEAVL = %s;
  function loadTeamOc(){
    if (!S.bp || !S.bp.team || S.ocBusy) return;
    S.ocBusy = true;
    sb.rpc('get_capstone_team_oceavl', { p_team_id: S.bp.team.id }).then(function(res){
      S.ocBusy = false;
      if (res.error){ console.warn('[capstone] get_capstone_team_oceavl:', res.error); S.oc = { error:true }; }
      else S.oc = res.data || { error:true };
      var host = document.getElementById('ocTeam'); if (host) host.innerHTML = ocTeamHtml();
    });
  }
  function ocTeamHtml(){
    var o = S.oc, h = '<div class="box-l">Team OCEAVL profile</div>';
    if (!o) return h + '<div class="box-i">Loading your team’s profile…</div>';
    if (o.error) return h + '<div class="box-i">Your team’s profile is not available yet.</div>';
    if (!o.dims) return h + '<div class="box-i">Your team’s profile appears here once every member has submitted their OCEAVL scores in Unit 5, part 3.1. Submitted so far: ' +
      esc(String(o.submitted || 0)) + ' of ' + esc(String(o.members || 0)) + ' members.</div>';
    h += '<div class="box-i">The level held by most members is the team’s level. ' + esc(String(o.members)) + ' members submitted. No names and no single scores are shown.</div>';
    OCEAVL.forEach(function(d, i){
      var c = o.dims[i] || [0,0,0], H = c[0], Bn = c[1], L = c[2];
      var lv = (H >= Bn && H >= L) ? 'High' : ((L >= Bn && L >= H) ? 'Low' : 'Balanced'), g = d.lv[lv];
      h += '<div class="oc-row"><div class="oc-h"><strong>' + esc(d.n) + '</strong><span class="oc-lv">' + lv + '</span><span class="oc-c">High ' + H + ' · Balanced ' + Bn + ' · Low ' + L + '</span></div>' +
        '<div class="oc-t">' + esc(g[0]) + '</div><div class="oc-t"><strong>Risk:</strong> ' + esc(g[1]) + '</div><div class="oc-t"><strong>Response:</strong> ' + esc(g[2]) + '</div><div class="oc-t"><strong>Routines:</strong> ' + esc(g[3]) + '</div></div>';
    });
    return h;
  }

  // === Render ===
  function render(){''' % OC
patch(cap, [
    ("""      ['5A','Interpretation risks','Identify how functional expertise, cognitive bias and emotion across the executive team could distort how [Case]’s strategy is interpreted.'],
      ['5B','Emotional climate','Name the dominant emotion [Case]’s people carry into this strategy, and its effect on commitment.'],
      ['5C','Alignment hot zones','Name the COMPASS zones most at risk in [Case], and the warning signals that show alignment escalating into crisis.'],
      ['5D','Shared enterprise interpretation','State how each executive role connects to the others to support coordinated action on the strategy.'],
      ['5E','Leadership behaviour commitment','State the behavioural change the executive team commits to model, and how it will be observed.']
""", """      ['5A','Team behavioural profile','Name the two OCEAVL dimensions on which the executive team profile of [Case] carries the highest risk for the strategy, and the response the team adopts for each.'],
      ['5B','Alignment plan · Mind (3S)','%s'],
      ['5C','Alignment plan · Heart (SCARF)','%s'],
      ['5D','Alignment plan · Hands (STAT)','%s'],
      ['5E','Alignment plan · Habit (ACE-IT)','%s']
""" % (plan('3S'), plan('SCARF'), plan('STAT'), plan('ACE-IT'))),
    ("""    u5: { lens:'u3m1_lens4', rows:[
      ['5C','syn_missing_compass','Synthesis · Underactivated COMPASS Domain(s)']
    ]}
""", """    u5: { lens:'u3m1_lens4', rows:[
      ['5B','kit_mind','Alignment Plan · Mind'],
      ['5C','kit_heart','Alignment Plan · Heart'],
      ['5D','kit_hands','Alignment Plan · Hands'],
      ['5E','kit_habit','Alignment Plan · Habit']
    ]}
"""),
    ("  // === Render ===\n  function render(){", JS),
    ("    restoreDirty();\n    autoPull();\n  }\n", "    restoreDirty();\n    autoPull();\n    loadTeamOc();\n  }\n"),
    ("    if (st === 'agreed') h += '<p class=\"sec-note\">Agreed · ' + esc(fmtDateTime(sec.agreed_at)) + '</p>';\n",
     "    if (st === 'agreed') h += '<p class=\"sec-note\">Agreed · ' + esc(fmtDateTime(sec.agreed_at)) + '</p>';\n"
     "    if (sec.key === 'u5' && st !== 'locked') h += '<div class=\"box oc-team\" id=\"ocTeam\">' + ocTeamHtml() + '</div>';\n"),
    (".state{max-width:640px;margin:80px auto;text-align:center;padding:0 24px;}\n",
     ".oc-team{border-left:2px solid var(--gold);padding:2px 0 4px 14px;}\n"
     ".oc-row{border:1px solid rgba(255,255,255,.08);border-radius:3px;padding:10px 12px;margin:0 0 8px;}\n"
     ".oc-h{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline;font-size:13px;color:#fff;margin-bottom:4px;}\n"
     ".oc-lv{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#1c1c1c;background:var(--gold);border-radius:2px;padding:2px 8px;}\n"
     ".oc-c{font-size:11px;color:rgba(255,255,255,.5);}\n"
     ".oc-t{font-size:12.5px;line-height:1.65;color:rgba(255,255,255,.78);margin-top:3px;}\n"
     ".state{max-width:640px;margin:80px auto;text-align:center;padding:0 24px;}\n"),
    ("  .box-l{color:#111;}\n", "  .box-l{color:#111;}\n  .oc-team,.oc-row{border-color:#bbb;}\n  .oc-h,.oc-t,.oc-c{color:#111 !important;}\n  .oc-lv{color:#111;background:none;border:1px solid #999;}\n  .oc-row{break-inside:avoid;}\n"),
], '\r\n')

# ── build_collection.js: the group work and the duplicate score line are left out of the Learning Portfolio ──
patch(bc, [
    ("u3m1_lens4:/^(syn_(missing_compass|strong_compass|sequence)$|team_name$|exec_(name|role)$|confirmed_items$)/i };',",
     "u3m1_lens4:/^(syn_(missing_compass|strong_compass|sequence)$|kit_(team|mind|heart|hands|habit)$|oceavl_scores$|team_name$|exec_(name|role)$|confirmed_items$)/i };',"),
], '\n')
