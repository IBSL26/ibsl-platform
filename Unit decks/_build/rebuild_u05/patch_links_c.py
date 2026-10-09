# -*- coding: utf-8 -*-
"""Unit 5 amendments of 9 October 2026: the files linked to the two unit pages.
Usage: python3 patch_links_c.py <folder with capstone_P.html and dashboard_F.html> <output folder>
capstone_P.html  Unit 5 has three boxes (was five): 5A team behavioural profile, 5B the change (Shift, Stake, Step), 5C leadership behaviours (ACE-IT).
                 5B and 5C are filled from the unit page's confirmed record (kit_mind, kit_habit). The team OCEAVL profile shows each routine with its meaning.
                 The database counts the boxes of a section: run Claude outputs\\capstone_unit5_boxes.sql in Supabase.
dashboard_F.html labels for the Section 5 record ("Leading with Clarity").
Every change is an exact replacement that must match once. Line endings and UTF-8 are kept as found."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5c_content as D
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
def patch(name, pairs):
    raw = open(os.path.join(src, name), 'rb').read().decode('utf-8')
    crlf = '\r\n' in raw
    assert (raw.count('\r\n') == raw.count('\n')) if crlf else True, name + ': mixed line endings'
    t = raw.replace('\r\n', '\n')
    for a, b in pairs:
        assert t.count(a) == 1, (name, t.count(a), a[:90])
        t = t.replace(a, b)
    assert t.count('<script') == raw.count('<script') and t.count('</script>') == raw.count('</script>')
    open(os.path.join(out, name), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
    print(name, 'written,', len(pairs), 'changes')

OLD_BOXES = """      ['5B','Alignment plan · Mind (3S)','State the 3S triggers most likely to surface as [Case] implements its strategy: where each will surface, what the executive team will do and the leader who owns it.'],
      ['5C','Alignment plan · Heart (SCARF)','State the SCARF triggers most likely to surface as [Case] implements its strategy: where each will surface, what the executive team will do and the leader who owns it.'],
      ['5D','Alignment plan · Hands (STAT)','State the STAT triggers most likely to surface as [Case] implements its strategy: where each will surface, what the executive team will do and the leader who owns it.'],
      ['5E','Alignment plan · Habit (ACE-IT)','State the ACE-IT triggers most likely to surface as [Case] implements its strategy: where each will surface, what the executive team will do and the leader who owns it.']
"""
NEW_BOXES = """      ['5B','The change · Shift, Stake and Step','State the Shift, the Stake and the Step for [Case]’s strategy: what is changing, what [Case] gains if it changes and loses if it stays as it is, and what must be done differently.'],
      ['5C','Leadership behaviours · ACE-IT','State the behaviour the executive team of [Case] will show under each ACE-IT behaviour so that the change holds: Accountability, Commitment, Engagement, Integrity and Transparency.']
"""
OLD_PULL = """      ['5B','kit_mind','Alignment Plan · Mind'],
      ['5C','kit_heart','Alignment Plan · Heart'],
      ['5D','kit_hands','Alignment Plan · Hands'],
      ['5E','kit_habit','Alignment Plan · Habit']
"""
NEW_PULL = """      ['5B','kit_mind','Alignment Plan · Mind'],
      ['5C','kit_habit','Alignment Plan · Habit']
"""
OLD_ROUT = """'</div><div class="oc-t"><strong>Routines:</strong> ' + esc(g[3]) + '</div></div>';"""
NEW_ROUT = """'</div><div class="oc-t"><strong>Routines:</strong></div>' +
        String(g[3]).split(';').map(function(r){ r = r.trim(); return '<div class="oc-t oc-r"><strong>' + esc(r) + '.</strong> ' + esc(OC_ROUT[r] || '') + '</div>'; }).join('') + '</div>';"""
OLD_FN = "  function loadTeamOc(){\n"
NEW_FN = ("  // What each routine is, in one line (the same lines as on the Unit 5 page).\n  var OC_ROUT = " +
          json.dumps(D.ROUT, ensure_ascii=False, separators=(',', ':')) + ";\n  function loadTeamOc(){\n")
patch('capstone_P.html', [(OLD_BOXES, NEW_BOXES), (OLD_PULL, NEW_PULL), (OLD_ROUT, NEW_ROUT), (OLD_FN, NEW_FN),
                          (".oc-t{font-size:12.5px;line-height:1.65;color:rgba(255,255,255,.78);margin-top:3px;}", ".oc-t{font-size:12.5px;line-height:1.65;color:rgba(255,255,255,.78);margin-top:3px;}\n.oc-r{padding-left:14px;}")])
patch('dashboard_F.html', [
    ("      { name: 'Alignment Toolkit',        test: function (k) { return /^kit_(me|team|mind|heart|hands|habit)$/i.test(k); } },",
     "      { name: 'Leading with Clarity',     test: function (k) { return /^kit_(me|team|mind|heart|hands|habit)$/i.test(k); } },"),
    ("      kit_team: 'Team Alignment Plan — record while the group works',", "      kit_team: 'Leading with Clarity — record while the group works',"),
    ("      kit_mind: 'Team Alignment Plan · Mind (3S) — confirmed',", "      kit_mind: 'Leading with Clarity · the 3S Check (Shift, Stake, Step) — confirmed',"),
    ("      kit_habit: 'Team Alignment Plan · Habit (ACE-IT) — confirmed',", "      kit_habit: 'Leading with Clarity · ACE-IT leadership behaviours — confirmed',"),
])
