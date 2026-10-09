# -*- coding: utf-8 -*-
"""Unit 6 amendments of 9 October 2026: the files linked to the two unit pages.
Usage: python3 patch_links_u06.py <folder with capstone_P.html, dashboard_F.html and build_collection.js> <output folder>
capstone_P.html      Unit 6 has four boxes (was five): 6A performance scoring logic, 6B FACES, 6C EXECUTION, 6D PM scorecards for the CEO and the CFO.
                     All four are filled from the unit page's confirmed record (pm_scoring, pm_faces, pm_execution, pm_scorecards).
                     The database counts the boxes of a section: run Claude outputs\\capstone_unit6_boxes.sql in Supabase.
dashboard_F.html     labels for the two new reflections (ref11, ref12) and for the Section 5 record; heading "Designing the PM Architecture". Labels of old answers stay.
build_collection.js  the group work of Section 5 is left out of the Learning Portfolio. Then run: node build_collection.js
Every change is an exact replacement that must match once. Line endings and UTF-8 are kept as found."""
import sys, os
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

OLD_BOXES = """      ['6A','Performance scorecard','Set the weighting across the three sights (Strategy OKRs, Operational KPIs, Behavioural & Values Alignment) for each leadership level in [Case].'],
      ['6B','Leader and team accountability','Define which outcomes executives are measured on and which are measured at team level.'],
      ['6C','Scoring logic','State how performance is rated on the 1–5 scale, and the leadership response each rating requires.'],
      ['6D','Collective Progress Signal','Define the single enterprise signal of progress for [Case], and the executive questions it anchors.'],
      ['6E','Reporting cadence and tools','Set the review rhythm, the forums and the reports through which [Case]’s performance is managed.']
"""
NEW_BOXES = """      ['6A','Performance scoring logic','State how performance is rated in [Case]: the performance level that earns each rating, the evidence required to confirm it, the leadership response it triggers in the monthly review, the contextual factors, the lines of sight of progress and the review cadence.'],
      ['6B','FACES of the PM architecture','Describe how the PM architecture of [Case] serves each of the five FACES functions.'],
      ['6C','EXECUTION of the PM architecture','Describe how each of the nine EXECUTION principles is designed into the PM architecture of [Case].'],
      ['6D','PM scorecards · CEO and CFO','Set out the PM scorecard for the CEO and for the CFO of [Case] on two of the team’s Key Results: what each role is measured on across the three sights, with the weights.']
"""
OLD_PULL = """      ['5B','kit_mind','Alignment Plan · Mind'],
      ['5C','kit_habit','Alignment Plan · Habit']
    ]}
  };
"""
NEW_PULL = """      ['5B','kit_mind','Alignment Plan · Mind'],
      ['5C','kit_habit','Alignment Plan · Habit']
    ]},
    u6: { lens:'u3m1_lens5', rows:[
      ['6A','pm_scoring','PM Architecture · Scoring Logic'],
      ['6B','pm_faces','PM Architecture · FACES'],
      ['6C','pm_execution','PM Architecture · EXECUTION'],
      ['6D','pm_scorecards','PM Architecture · Scorecards']
    ]}
  };
"""
patch('capstone_P.html', [(OLD_BOXES, NEW_BOXES), (OLD_PULL, NEW_PULL)])
patch('dashboard_F.html', [
    ("      { name: 'Leading with Clarity',     test: function (k) { return /^kit_(me|team|mind|heart|hands|habit)$/i.test(k); } },\n",
     "      { name: 'Leading with Clarity',     test: function (k) { return /^kit_(me|team|mind|heart|hands|habit)$/i.test(k); } },\n"
     "      { name: 'Designing the PM Architecture', test: function (k) { return /^pm_(record|scoring|faces|execution|scorecards)$/i.test(k); } },\n"),
    ("      ref10: 'My 30-Day Commitment',\n      app_scorecard: 'PM Scorecard Architecture',\n",
     "      ref10: 'My 30-Day Commitment',\n      ref11: 'Team and Leader in Your PM System',\n      ref12: 'Your Current PM System',\n"
     "      pm_record: 'Designing the PM Architecture — record while the group works',\n"
     "      pm_scoring: 'PM Architecture · Step 1 · Scoring Logic — confirmed',\n"
     "      pm_faces: 'PM Architecture · Step 2 · FACES — confirmed',\n"
     "      pm_execution: 'PM Architecture · Step 3 · EXECUTION — confirmed',\n"
     "      pm_scorecards: 'PM Architecture · Step 4 · PM Scorecards for the CEO and the CFO — confirmed',\n"
     "      confirmed_items: 'Confirmed by the group',\n      app_scorecard: 'PM Scorecard Architecture',\n"),
    ('9:"EXECUTION Self-Score",10:"My 30-Day Commitment"},', '9:"EXECUTION Self-Score",10:"My 30-Day Commitment",11:"Team and Leader in Your PM System",12:"Your Current PM System"},'),
])
patch('build_collection.js', [
    ("oceavl_scores$|team_name$|exec_(name|role)$|confirmed_items$)/i };',",
     "oceavl_scores$|team_name$|exec_(name|role)$|confirmed_items$)/i, u3m1_lens5:/^(pm_(record|scoring|faces|execution|scorecards)$|confirmed_items$)/i };',"),
])
