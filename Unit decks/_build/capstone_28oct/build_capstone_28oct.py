# -*- coding: utf-8 -*-
"""Capstone S2R Blueprint fixes (28 Oct 2026): fill on Agree (admin back-up button), naming,
assessment criteria card, print for the panel. Builds from the backups, never from the live files.
Usage: python3 -B build_capstone_28oct.py <backup capstone_P.html> <backup dashboard_A.html> <out folder>"""
import sys, os, re
src_p, src_a, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
rd = lambda x: open(x, 'rb').read().decode('utf-8')
P = rd(src_p)
CRLF = '\r\n' in P
P = P.replace('\r\n', '\n')

def rep(s, old, new, n=1):
    c = s.count(old)
    assert c == n, (c, n, old[:120])
    return s.replace(old, new)

# ---------- 1. Naming ----------
P = rep(P, '<title>IBSL | Capstone — Blueprint Showcase</title>', '<title>IBSL | Capstone S2R Blueprint</title>')
P = rep(P, 'onclick="window.print()" style="display:none;">Print Blueprint</button>',
           'onclick="window.print()" style="display:none;">Print Capstone S2R Blueprint</button>')
P, _n = re.subn(r'<h1 class="unit-title">[^<]*</h1>', '<h1 class="unit-title">Capstone S2R Blueprint</h1>', P, count=1); assert _n == 1
P = rep(P, 'Your team is the executive leadership team of your simulated company. This Blueprint records the decisions your team agrees as you progress through the programme. Each section opens once every member of the team has completed its unit. It fills from the Section 5 work your group agrees on each unit page.',
           'Your team is the executive leadership team of your simulated company. The Capstone S2R Blueprint records the decisions your team agrees as you progress through the programme. Each section fills as soon as every member of your group selects Agree on the group work in that unit.')
P = rep(P, "'. This Blueprint records the decisions your team agrees for ' + esc(S.caseName) + ' as you progress through the programme. Each section opens once every member of the team has completed its unit. It fills from the Section 5 work your group agrees on each unit page.';",
           "'. The Capstone S2R Blueprint records the decisions your team agrees for ' + esc(S.caseName) + ' as you progress through the programme. Each section fills as soon as every member of your group selects Agree on the group work in that unit.';")
P = rep(P, "fatal('Could not load', 'This team’s Blueprint could not be loaded.')", "fatal('Could not load', 'This team’s Capstone S2R Blueprint could not be loaded.')")
P = rep(P, "'The submission deadline has passed. The Blueprint is read-only. Contact IBSL to reopen it.'",
           "'The submission deadline has passed. The Capstone S2R Blueprint is read-only. Contact IBSL to reopen it.'")
P = rep(P, '<div class="banner">The submission deadline has passed. The Blueprint is read-only. Contact IBSL to reopen it.</div>',
           '<div class="banner">The submission deadline has passed. The Capstone S2R Blueprint is read-only. Contact IBSL to reopen it.</div>')
P = rep(P, "Pending — scored by IBSL after the Blueprint Showcase", "Pending — scored by IBSL after the showcase")
P = rep(P, "res.error ? 'Could not update the Blueprint.' : (on ? 'Blueprint reopened.' : 'Blueprint locked.')",
           "res.error ? 'Could not update the Capstone S2R Blueprint.' : (on ? 'Capstone S2R Blueprint reopened.' : 'Capstone S2R Blueprint locked.')")
P = rep(P, '// Print: open every section so the full Blueprint prints.', '// Print: open every section so the full Capstone S2R Blueprint prints.')

P = rep(P, "It is used throughout your Blueprint.'],", "It is used throughout your Capstone S2R Blueprint.'],")

# ---------- 2. Assessment criteria card (weights; wording as the Panel Assessment Guide and Unit 12) ----------
old_crit = P[P.index('  function criteriaCard(){'):P.index('  function blueprintCard(){')]
new_crit = '''  function criteriaCard(){
    function crit(name, scope, w, text){ return '<p class="crit"><strong>' + name + '</strong> (' + scope + ' · ' + w + '): ' + text + '</p>'; }
    return '<div class="card no-print"><div class="card-label">Assessment criteria</div>' +
      '<p class="muted">The panel (IBSL programme facilitators, an invited academic and, for a company cohort, the client company’s management) scores your team’s Capstone S2R Blueprint and each member’s individual showcase, and returns one capstone score per member out of 100. Each of the twelve sections carries 5%.</p>' +
      '<div class="crit-group"><div class="crit-head">Capstone S2R Blueprint · 60%</div>' +
        crit('Problem Charter', 'Unit 1', '5%', 'how fully the Capstone S2R Blueprint as a whole answers the central problem and builds the capabilities the Charter names.') +
        crit('Direction', 'Units 2–4', '15%', 'strategic intent, success definition, priorities and direction integrity.') +
        crit('Influence', 'Units 5–9', '25%', 'alignment, performance management, expectations, measurement and unclogging.') +
        crit('Grounding', 'Units 10–12', '15%', 'the ESRG operating environment and organisational health, leveraged through the Quarterly Three Lines of Sight and KISS to sustain strategic performance.') +
      '</div>' +
      '<div class="crit-group"><div class="crit-head">Individual showcase · 40%</div>' +
        crit('Command', 'each member', '20%', 'the member’s grasp of the whole Capstone S2R Blueprint and of their executive role within it: which Key Results, contributions, owners and measures sit with their role, and how their decisions connect across sections.') +
        crit('Delivery', 'each member', '20%', 'how clearly and credibly the member presents and defends the team’s decisions: evidence from the Capstone S2R Blueprint, consistent answers under follow-up, and a position held or revised for stated reasons.') +
      '</div></div>';
  }

'''
P = P.replace(old_crit, new_crit)

# ---------- 3. Blueprint card: name, admin "Bring in agreed work", section states ----------
P = rep(P, '''    var h = '<div class="card"><div class="card-label">The Blueprint</div>';''',
           '''    var h = printCover() + '<div class="card bp-card"><div class="card-label">Capstone S2R Blueprint</div>';''')
P = rep(P, '''    h += '<p class="muted" style="margin-bottom:16px;">' + agreed + ' of 12 sections agreed.</p>';''',
           '''    h += '<p class="muted no-print" style="margin-bottom:16px;">' + agreed + ' of 12 sections agreed.</p>';''')
P = rep(P, '''      h += '<div class="admin-bar">' +
        (S.bp.team && S.bp.team.reopened
          ? '<button class="btn" onclick="capAdminReopenAll(false)">Lock Blueprint</button><span class="muted">Reopened: the team can edit after the deadline.</span>'
          : '<button class="btn" onclick="capAdminReopenAll(true)">Reopen Blueprint</button><span class="muted">Lets the team edit after the deadline.</span>') +
        '</div><div class="msg" id="msg_admin"></div>';''',
           '''      h += '<div class="admin-bar">' +
        '<button class="btn primary" id="capBringBtn" onclick="capAdminBringIn()">Bring in agreed work</button><span class="muted">Fills every section whose group work all members have agreed.</span>' +
        '</div><div class="admin-bar">' +
        (S.bp.team && S.bp.team.reopened
          ? '<button class="btn" onclick="capAdminReopenAll(false)">Lock Capstone S2R Blueprint</button><span class="muted">Reopened: the team can edit after the deadline.</span>'
          : '<button class="btn" onclick="capAdminReopenAll(true)">Reopen Capstone S2R Blueprint</button><span class="muted">Lets the team edit after the deadline.</span>') +
        '</div><div class="msg" id="msg_admin"></div>';''')

# An agreed section shows even before every member has marked the unit complete (it fills on Agree).
P = rep(P, '''  function statusOf(sec){
    if (!sec.open) return 'locked';''', '''  function statusOf(sec){
    if (sec.status === 'agreed') return 'agreed';
    if (!sec.open) return 'locked';''')
P = rep(P, "var chipText = { locked:'Locked', draft:'Draft', awaiting:'Awaiting confirmation', agreed:'Agreed' }[st];",
           "var chipText = { locked:'Not yet agreed', draft:'Not yet agreed', awaiting:'Awaiting confirmation', agreed:'Agreed' }[st];")
P = rep(P, '''        '<span class="sec-t">Unit ' + def.unit + ' · ' + esc(def.title) + '</span>' +''',
           '''        '<span class="sec-t"><span class="print-only">Section ' + def.unit + ' · </span>Unit ' + def.unit + ' · ' + esc(def.title) + '</span>' +''')
P = rep(P, '''    if (st === 'locked') h += '<p class="sec-note">Opens when every team member has completed Unit ' + def.unit + '.' + (PULL[sec.key] ? ' Your confirmed outputs from Unit ' + def.unit + ' are then brought in.' : '') + '</p>';
    if (isMember && st !== 'locked' && st !== 'agreed') h += '<p class="sec-note">This section fills from Section 5 of your Unit ' + def.unit + ' page once every member of your group has agreed the work there.</p>';''',
           '''    if (st === 'locked' || st === 'draft') h += '<p class="sec-note">Fills as soon as every member of ' + (isMember ? 'your group' : 'the group') + ' selects Agree on the group work in ' + groupPart(def.unit) + ' of the Unit ' + def.unit + ' page.</p>';''')
P = rep(P, '''      } else if (st !== 'locked'){
        h += '<div class="box-v' + (val ? '' : ' empty') + '">' + (val ? esc(val) : 'Not yet entered') + '</div>';
      }''', '''      } else if (st !== 'locked'){
        h += '<div class="box-v' + (val ? '' : ' empty') + '">' + (val ? esc(val) : 'Not yet entered') + '</div>';
      } else {
        h += '<div class="box-v empty print-only">Not agreed by the team</div>';
      }''')
P = rep(P, "if (S.mode === 'participant') html += resultCard();", "if (S.mode === 'participant') html += resultCard();   // the result card never prints (no-print)")
P = rep(P, '''    var h = '<div class="card"><div class="card-label">Your result</div>';''', '''    var h = '<div class="card no-print"><div class="card-label">Your result</div>';''')
P = rep(P, '''    var h = '<div class="card"><div class="card-label">The brief</div>';''', '''    var h = '<div class="card no-print"><div class="card-label">The brief</div>';''')
P = rep(P, '''    var h = '<div class="card"><div class="card-label">' + (S.mode === 'admin' ? 'Team' : 'Your team') + '</div>';''',
           '''    var h = '<div class="card no-print"><div class="card-label">' + (S.mode === 'admin' ? 'Team' : 'Your team') + '</div>';''')

# ---------- 4. Print cover, footer, helpers ----------
helpers = '''  // Where the group work sits on each unit page.
  function groupPart(unit){ return unit === 1 ? 'part 6.2' : 'Section 5'; }

  // === Print for the panel: cover page (organisation, team, members, executive roles), footer with team name and date ===
  function execRoles(){
    var l = (S.bp && S.bp.sections) || [], txt = '';
    for (var i = 0; i < l.length; i++){ if (l[i].key === 'u1' && l[i].content) txt = String(l[i].content['1B'] || ''); }
    var rows = [];
    txt.split(/\\n+/).forEach(function(line){
      line = line.trim(); if (!line) return;
      var p = line.split(' · ');
      if (p.length >= 2) rows.push({ role:p[0].trim(), name:p.slice(1).join(' · ').trim() }); else rows.push({ role:line, name:'' });
    });
    return rows;
  }
  function printDate(){ return new Date().toLocaleDateString('en-GB', { day:'numeric', month:'long', year:'numeric' }); }
  function printCover(){
    var team = (S.bp && S.bp.team && S.bp.team.name) || '';
    var cohort = (S.bp && S.bp.cohort && S.bp.cohort.name) || (S.data && S.data.cohort && S.data.cohort.name) || '';
    var members = (S.bp && S.bp.members) || [], roles = execRoles(), used = {};
    var tr = '';
    members.forEach(function(m){
      var nm = String(m.full_name || '').trim(), role = '';
      for (var i = 0; i < roles.length; i++){ if (!used[i] && roles[i].name && roles[i].name.toLowerCase() === nm.toLowerCase()){ role = roles[i].role; used[i] = true; break; } }
      tr += '<tr><td>' + esc(nm) + '</td><td>' + (role ? esc(role) : '—') + '</td></tr>';
    });
    roles.forEach(function(r, i){ if (!used[i]) tr += '<tr><td>' + (r.name ? esc(r.name) : '—') + '</td><td>' + esc(r.role) + '</td></tr>'; });
    var agreed = ((S.bp && S.bp.sections) || []).filter(function(s){ return s.status === 'agreed'; }).length;
    return '<div class="print-cover print-only">' +
      '<div class="pc-eyebrow">Strategy2Results® · CESI Capstone</div>' +
      '<div class="pc-title">Capstone S2R Blueprint</div>' +
      '<table class="pc-facts"><tbody>' +
        '<tr><th>Organisation</th><td>' + (S.caseName ? esc(S.caseName) : 'Not yet entered') + '</td></tr>' +
        '<tr><th>Team</th><td>' + esc(team) + '</td></tr>' +
        (cohort ? '<tr><th>Cohort</th><td>' + esc(cohort) + '</td></tr>' : '') +
        '<tr><th>Sections agreed</th><td>' + agreed + ' of 12</td></tr>' +
        '<tr><th>Printed</th><td>' + esc(printDate()) + '</td></tr>' +
      '</tbody></table>' +
      '<div class="pc-h">Executive team</div>' +
      '<table class="pc-team"><thead><tr><th>Member</th><th>Executive role</th></tr></thead><tbody>' + tr + '</tbody></table>' +
      '<div class="pc-foot">Institute of Behavioural Strategy &amp; Leadership</div>' +
    '</div>';
  }
  function setPrintFooter(){
    var team = (S.bp && S.bp.team && S.bp.team.name) || '';
    var text = (team ? team + ' · ' : '') + 'Capstone S2R Blueprint · ' + printDate();
    var el = document.getElementById('printFooterCss');
    if (!el){ el = document.createElement('style'); el.id = 'printFooterCss'; document.head.appendChild(el); }
    el.textContent = '@page{size:A4;margin:16mm 15mm 18mm;@bottom-left{content:' + JSON.stringify(text) + ';font-family:Montserrat,Arial,sans-serif;font-size:8pt;color:#555;}' +
      '@bottom-right{content:"Page " counter(page) " of " counter(pages);font-family:Montserrat,Arial,sans-serif;font-size:8pt;color:#555;}}';
  }

'''
P = rep(P, '  // === Render ===\n', helpers + '  // === Render ===\n')
P = rep(P, '''    restoreDirty();
    autoPull();''', '''    restoreDirty();
    setPrintFooter();
    autoPull();''')

# ---------- 5. Admin action: Bring in agreed work ----------
bring = '''  var SEC_UNIT = function(k){ return 'Unit ' + String(k).replace('u',''); };
  window.capAdminBringIn = function(){
    var btn = document.getElementById('capBringBtn'); if (btn) btn.disabled = true;
    sb.rpc('admin_capstone_bring_in', { p_team_id: S.bp.team.id }).then(function(res){
      var d = res.error ? null : res.data;
      if (res.error) console.error('[capstone] admin_capstone_bring_in:', res.error);
      reload().then(function(){
        if (!d || !d.ok){ showMsg('admin', 'Could not bring in the agreed work. Please try again.', 'err'); return; }
        var f = (d.filled || []).map(SEC_UNIT), w = (d.waiting || []).map(SEC_UNIT);
        showMsg('admin', (f.length ? 'Brought in: ' + f.join(', ') + '.' : 'Nothing new to bring in.') +
          (w.length ? ' Not yet agreed by every member: ' + w.join(', ') + '.' : ''), 'ok');
      });
    });
  };
'''
P = rep(P, '  window.capAdminReopenAll = function(on){', bring + '  window.capAdminReopenAll = function(on){')

# ---------- 6. Print CSS ----------
css_screen_add = '''.print-only{display:none;}
'''
P = rep(P, '@media (max-width:640px){', css_screen_add + '@media (max-width:640px){')
old_print = P[P.index('@media print{'):P.index('</style>')]
new_print = '''@media print{
  body{background:#fff;color:#111;font-size:11pt;}
  .unit-nav,.unit-header,.actions,.msg,.admin-bar,.banner,.box-ta,.no-print,.confirms,.meta{display:none !important;}
  .print-only{display:block !important;}
  span.print-only{display:inline !important;}
  .main{padding:0;max-width:none;}
  .card{background:none;border:none;padding:0;margin:0;}
  .bp-card > .card-label{display:none;}
  .print-cover{break-after:page;padding-top:30mm;}
  .pc-eyebrow{font-size:9pt;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#1a7a6a;margin-bottom:10px;}
  .pc-title{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;font-weight:400;color:#111;border-bottom:2px solid #1a3a2a;padding-bottom:12px;margin-bottom:22px;}
  .pc-facts,.pc-team{width:100%;border-collapse:collapse;font-size:11pt;color:#111;}
  .pc-facts th{width:38%;text-align:left;font-weight:600;color:#444;padding:7px 10px 7px 0;border-bottom:1px solid #ddd;vertical-align:top;}
  .pc-facts td{padding:7px 0;border-bottom:1px solid #ddd;}
  .pc-h{font-size:9pt;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#1a7a6a;margin:28px 0 8px;}
  .pc-team th{text-align:left;font-size:9pt;font-weight:700;color:#444;padding:6px 8px;border-bottom:2px solid #1a3a2a;}
  .pc-team td{padding:7px 8px;border-bottom:1px solid #ddd;}
  .pc-foot{margin-top:40mm;font-size:9pt;color:#555;}
  .sec{break-before:page;border:none;background:none;margin:0;}
  .sec-h{padding:0 0 8px;border-bottom:2px solid #1a3a2a;margin-bottom:10px;cursor:default;}
  .sec-t{color:#111;font-size:16pt;}
  .sec-b{display:block !important;padding:0;}
  .box{break-inside:avoid;margin-bottom:12px;}
  .box-l{color:#111;font-size:10.5pt;}
  .box-i,.sec-note{color:#444 !important;font-size:9pt;}
  .muted,.crit{color:#222 !important;}
  .box-v,.ptext{display:block;color:#111 !important;background:none;border:1px solid #ccc;white-space:pre-wrap;padding:8px 10px;font-size:10pt;line-height:1.55;}
  .box-v.empty{color:#777 !important;font-style:italic;}
  .chip{color:#111 !important;border-color:#999 !important;}
  .oc-team,.oc-row{border-color:#bbb;}
  .oc-h,.oc-t,.oc-c{color:#111 !important;}
  .oc-lv{color:#111;background:none;border:1px solid #999;}
  .oc-row{break-inside:avoid;}
}
'''
P = P.replace(old_print, new_print)

if CRLF: P = P.replace('\n', '\r\n')
open(os.path.join(out, 'capstone_P.html'), 'wb').write(P.encode('utf-8'))

# ================= Admin Console (dashboard_A.html) =================
A = rd(src_a)
ACRLF = '\r\n' in A
A = A.replace('\r\n', '\n')
A = rep(A, "/* Capstone build: cohort brief panel + Blueprint progress per team */", "/* Capstone build: cohort brief panel + Capstone S2R Blueprint progress per team */")
A = rep(A, "// Capstone build: Blueprint progress per team (sections agreed).", "// Capstone build: Capstone S2R Blueprint progress per team (sections agreed).")
A = rep(A, """              '<span class="capstone-bp">Blueprint: ' + ((capstoneState.agreedByTeam && capstoneState.agreedByTeam[t.id]) || 0) + ' of 12 agreed</span>' +
              '<a class="capstone-cert-view" href="capstone_P.html?teamId=' + encodeURIComponent(t.id) + '" target="_blank" rel="noopener">Open Blueprint</a>' +""",
"""              '<span class="capstone-bp">Capstone S2R Blueprint: ' + ((capstoneState.agreedByTeam && capstoneState.agreedByTeam[t.id]) || 0) + ' of 12 agreed</span>' +
              '<a class="capstone-cert-view" href="capstone_P.html?teamId=' + encodeURIComponent(t.id) + '" target="_blank" rel="noopener">Open Capstone S2R Blueprint</a>' +
              '<button type="button" class="btn--ghost capstone-bring-btn" data-team-id="' + capstoneEsc(t.id) + '" data-team-name="' + capstoneEsc(t.team_name) + '">Bring in agreed work</button>' +""")
A = rep(A, "              <div class=\"view-header__sub\">Create capstone teams for a cohort and manage their members.</div>",
           "              <div class=\"view-header__sub\">Create capstone teams for a cohort, manage their members and open each team’s Capstone S2R Blueprint.</div>")
A = rep(A, "  .capstone-bp { font-size: 11px;", "  .capstone-bring-btn { font-size: 11px; padding: 5px 12px; }\n  .capstone-bp { font-size: 11px;")
bring_a = """    // Back-up: bring every agreed group record into the team's Capstone S2R Blueprint (admin_capstone_bring_in).
    let _capstoneBringBound = false;
    function bindCapstoneBringHandler() {
      if (_capstoneBringBound) return;
      _capstoneBringBound = true;
      document.addEventListener('click', function(e) {
        const btn = e.target.closest('.capstone-bring-btn');
        if (!btn) return;
        const teamId = btn.getAttribute('data-team-id');
        const teamName = btn.getAttribute('data-team-name') || 'the team';
        btn.disabled = true; const orig = btn.textContent; btn.textContent = 'Bringing in…';
        sb.rpc('admin_capstone_bring_in', { p_team_id: teamId }).then(function(res) {
          btn.disabled = false; btn.textContent = orig;
          const d = res && !res.error ? res.data : null;
          if (!d || !d.ok) { window.showToast('Could not bring in the agreed work for ' + teamName + '. Please try again.', 5000); return; }
          const units = function(a) { return (a || []).map(function(k) { return 'Unit ' + String(k).replace('u', ''); }); };
          const f = units(d.filled), w = units(d.waiting);
          window.showToast(teamName + ': ' + (f.length ? 'brought in ' + f.join(', ') + '.' : 'nothing new to bring in.') +
            (w.length ? ' Not yet agreed by every member: ' + w.join(', ') + '.' : ''), 7000);
          loadCapstoneTeams();
        }).catch(function() { btn.disabled = false; btn.textContent = orig; window.showToast('Network error. Please try again.', 5000); });
      });
    }

    function renderCapstoneTeams() {"""
A = rep(A, "    function renderCapstoneTeams() {", bring_a)
A = rep(A, """      bindCapstoneScoreHandler();
      bindCapstoneCertHandler();
      const teams = capstoneState.teams;""", """      bindCapstoneScoreHandler();
      bindCapstoneCertHandler();
      bindCapstoneBringHandler();
      const teams = capstoneState.teams;""")
if ACRLF: A = A.replace('\n', '\r\n')
open(os.path.join(out, 'dashboard_A.html'), 'wb').write(A.encode('utf-8'))
print('built', out)
