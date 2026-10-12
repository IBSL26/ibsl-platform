# -*- coding: utf-8 -*-
"""Unit 8 amendments of 12 October 2026: the files linked to the two unit pages.
Usage: python3 patch_links_u08.py <folder with capstone_P.html, dashboard_F.html and build_collection.js> <output folder>
capstone_P.html      Unit 8 has four boxes (was five): 8A to 8D, one per consequence of weak review discipline, each filled from the
                     confirmed Section 5 record of the unit page (rd_warning, rd_accountability, rd_learning, rd_credibility) through PULL.u8.
                     The database must count four boxes for Unit 8: capstone_unit8_boxes.sql.
dashboard_F.html     labels for the new answers (rp_review, rp_judge, rd_*, confirmed_items) and the renamed reflections; two headings. Labels of old answers stay.
build_collection.js  the group work of Section 5 is left out of the Learning Portfolio; the Portfolio work of part 4.2 stays in. Then run: node build_collection.js
Every change is an exact replacement that must match once. Line endings and UTF-8 are kept as found."""
import sys, os
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
def patch(name, pairs):
    raw = open(os.path.join(src, name), 'rb').read().decode('utf-8')
    crlf = '\r\n' in raw
    t = raw.replace('\r\n', '\n')
    for a, b in pairs:
        assert t.count(a) == 1, (name, t.count(a), a[:90])
        t = t.replace(a, b)
    assert t.count('<script') == raw.count('<script') and t.count('</script>') == raw.count('</script>')
    open(os.path.join(out, name), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
    print(name, 'written,', len(pairs), 'changes')

OLD_BOXES = """      ['8A','Review discipline','Set [Case]’s review–realign–restore rhythm: the forums, their frequency and who attends.'],
      ['8B','Progress signals and responses','For [Case]’s priority Key Results, define what counts as progress confirmation, early warning and a significant gap, and the leadership response each requires.'],
      ['8C','Breakdown risk','Identify where the review and interpretation of performance evidence are most likely to break down in [Case].'],
      ['8D','Enterprise performance intelligence','Record the collective trajectory, early warnings and execution learning from a simulated executive review, and the decisions taken.'],
      ['8E','Accountability loop','State how the executive team responds when a Key Result falls below expectation: root cause, action and follow-up.']
"""
NEW_BOXES = """      ['8A','Early warning signals','Set two decision points that stop [Case]’s executive team from missing early warning signals: for each, the signal, the decision taken when it appears and who takes it.'],
      ['8B','Accountability','Set two decision points that stop accountability for [Case]’s Key Results from gradually diffusing: for each, the signal, the decision taken when it appears and who takes it.'],
      ['8C','Organisational learning','Set two decision points that stop [Case] losing the learning in its performance reviews: for each, the signal, the decision taken when it appears and who takes it.'],
      ['8D','Leadership credibility','Set two decision points that protect the credibility of [Case]’s leadership on its strategic priorities: for each, the signal, the decision taken when it appears and who takes it.']
"""
OLD_PULL = """      ['7E','ex_dialogue','Expectations · Alignment Dialogue']
    ]}
  };
"""
NEW_PULL = """      ['7E','ex_dialogue','Expectations · Alignment Dialogue']
    ]},
    u8: { lens:'u3m2_lens7', rows:[
      ['8A','rd_warning','Review Discipline · Early Warning Signals'],
      ['8B','rd_accountability','Review Discipline · Accountability'],
      ['8C','rd_learning','Review Discipline · Organisational Learning'],
      ['8D','rd_credibility','Review Discipline · Leadership Credibility']
    ]}
  };
"""
patch('capstone_P.html', [(OLD_BOXES, NEW_BOXES), (OLD_PULL, NEW_PULL)])
patch('dashboard_F.html', [
    ("      { name: 'Establishing Delivery Expectations', test: function (k) { return /^ex_(record|future|delivery|chain|ownership|dialogue)$/i.test(k); } },\n",
     "      { name: 'Establishing Delivery Expectations', test: function (k) { return /^ex_(record|future|delivery|chain|ownership|dialogue)$/i.test(k); } },\n"
     "      { name: 'The Accountability Loop Case', test: function (k) { return /^rp_(review|judge)$/i.test(k) || /^app_(rootcause|corrective)$/i.test(k); } },\n"
     "      { name: 'Decision Points Against the Four Consequences', test: function (k) { return /^rd_(record|warning|accountability|learning|credibility)$/i.test(k); } },\n"),
    ("      app_rootcause: 'Root Cause Diagnosed',\n      app_corrective: 'Corrective Actions (Restore)',\n      app_loop_reflection: 'Overall Reflection & 5-Day Commitment'\n    },\n    u3m2_lens8: {",
     "      app_rootcause: 'Accountability Loop Case · Realign: the root cause and the clues',\n"
     "      app_corrective: 'Accountability Loop Case · Restore: actions, follow-up and alignment score',\n"
     "      app_loop_reflection: 'Overall Reflection & 5-Day Commitment',\n"
     "      rp_review: 'Accountability Loop Case · Review: the evidence used',\n"
     "      rp_judge: 'Accountability Loop Case · Your judgement against the three criteria',\n"
     "      rd_record: 'Decision Points — record while the group works',\n"
     "      rd_warning: 'Decision Points · Early Warning Signals Are Missed — confirmed',\n"
     "      rd_accountability: 'Decision Points · Gradual Diffusion of Accountability — confirmed',\n"
     "      rd_learning: 'Decision Points · Loss of Organisational Learning — confirmed',\n"
     "      rd_credibility: 'Decision Points · Erodes Leadership Credibility — confirmed',\n"
     "      confirmed_items: 'Confirmed by the group'\n    },\n    u3m2_lens8: {"),
    ("      ref2: 'R3 Cycle in Your Organisation',\n", "      ref2: 'The Cycle and the Loop in Your Organisation',\n"),
    ("      ref5: 'Round 1 Contribution — Collective Trajectory',\n      ref6: 'Round 2 Contribution — Early Warnings',\n      ref7: 'Round 3 Contribution — Execution Learning',\n",
     "      ref5: 'Your Progress Signal',\n      ref6: 'Your Early Warning Signal',\n      ref7: 'Your Execution Learning',\n"),
    ('      u3m2_lens7: {1:"Activity vs Progress",2:"R3 Cycle in Your Organisation",3:"Which Signal Are You Seeing?",4:"Which Gap Is Most Prevalent?",5:"Round 1 Contribution — Collective Trajectory",6:"Round 2 Contribution — Early Warnings",7:"Round 3 Contribution — Execution Learning"},',
     '      u3m2_lens7: {1:"Activity vs Progress",2:"The Cycle and the Loop in Your Organisation",3:"Which Signal Are You Seeing?",4:"Which Gap Is Most Prevalent?",5:"Your Progress Signal",6:"Your Early Warning Signal",7:"Your Execution Learning"},'),
])
patch('build_collection.js', [
    (", u3m1_lens6:/^(ex_(record|future|delivery|chain|ownership|dialogue)$|confirmed_items$)/i };',",
     ", u3m1_lens6:/^(ex_(record|future|delivery|chain|ownership|dialogue)$|confirmed_items$)/i, u3m2_lens7:/^(rd_(record|warning|accountability|learning|credibility)$|confirmed_items$)/i };',"),
])
