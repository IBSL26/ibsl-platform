# -*- coding: utf-8 -*-
"""Unit 7 amendments of 11 October 2026: the files linked to the two unit pages.
Usage: python3 patch_links_u07.py <folder with capstone_P.html, dashboard_F.html and build_collection.js> <output folder>
capstone_P.html      Unit 7 keeps five boxes with new content: 7A Start With the Future, 7B Delivery expectation, 7C Expectations chain,
                     7D Ownership, 7E Alignment dialogue with the board chair. All five are filled from the unit page's confirmed record
                     (ex_future, ex_delivery, ex_chain, ex_ownership, ex_dialogue). The database already counts five boxes for Unit 7: no SQL.
dashboard_F.html     labels for the Portfolio work of part 4.2 (ad_*) and for the Section 5 record (ex_*); two headings. Labels of old answers stay.
build_collection.js  the group work of Section 5 is left out of the Learning Portfolio; the Portfolio work of part 4.2 stays in. Then run: node build_collection.js
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

OLD_BOXES = """      ['7A','Critical delivery expectation','Select one Key Result for [Case]. State what must be delivered, by when, to what standard, and how success will be recognised.'],
      ['7B','Expectations chain','Name the upline, downline and lateral contributors on whom that result depends.'],
      ['7C','Ownership readiness','Assess the owner’s clarity, capability and commitment, and state how each gap will be closed.'],
      ['7D','Commitment record','Record the commitments made by the owner and the executive team, the alignment score reached, and how any gap was resolved.'],
      ['7E','Enterprise practice','State how [Case]’s leaders will establish expectations consistently across the organisation.']
"""
NEW_BOXES = """      ['7A','Start With the Future','For two Objectives of [Case], with one Key Result each: name the owner of the Key Result, the Success in Practice statement it serves, the part of that Future it serves and the leader framing that connects the Key Result to that Future.'],
      ['7B','Delivery expectation','For each of the two Key Results of [Case]: state what must be delivered, by when, to what standard, and how success will be recognised.'],
      ['7C','Expectations chain','For each of the two Key Results of [Case]: name the Upline, Downline and External contributors, what the outcome needs from each, and the coordination they require.'],
      ['7D','Ownership','For each of the two Key Results of [Case]: record the owner’s alignment score and, where the score is below 9, what stands behind it, the actions agreed and the revised score.'],
      ['7E','Alignment dialogue with the board chair','For one Key Result of [Case]: set out the alignment dialogue that moves the board chair to a 10, under Goal, Reality, Options and Will.']
"""
OLD_PULL = """      ['6C','pm_execution','PM Architecture · EXECUTION'],
      ['6D','pm_scorecards','PM Architecture · Scorecards']
    ]}
  };
"""
NEW_PULL = """      ['6C','pm_execution','PM Architecture · EXECUTION'],
      ['6D','pm_scorecards','PM Architecture · Scorecards']
    ]},
    u7: { lens:'u3m1_lens6', rows:[
      ['7A','ex_future','Expectations · Start With the Future'],
      ['7B','ex_delivery','Expectations · Delivery Expectation'],
      ['7C','ex_chain','Expectations · Expectations Chain'],
      ['7D','ex_ownership','Expectations · Ownership'],
      ['7E','ex_dialogue','Expectations · Alignment Dialogue']
    ]}
  };
"""
patch('capstone_P.html', [(OLD_BOXES, NEW_BOXES), (OLD_PULL, NEW_PULL)])
patch('dashboard_F.html', [
    ("      { name: 'Designing the PM Architecture', test: function (k) { return /^pm_(record|scoring|faces|execution|scorecards)$/i.test(k); } },\n",
     "      { name: 'Designing the PM Architecture', test: function (k) { return /^pm_(record|scoring|faces|execution|scorecards)$/i.test(k); } },\n"
     "      { name: 'Practising the Alignment Dialogue', test: function (k) { return /^ad_(kr|goal|reality|options|will)$/i.test(k); } },\n"
     "      { name: 'Establishing Delivery Expectations', test: function (k) { return /^ex_(record|future|delivery|chain|ownership|dialogue)$/i.test(k); } },\n"),
    ("      ref8: 'Practise the Resolve Question',\n      app_role: 'Critical Role Identification',\n",
     "      ref8: 'Practise the Resolve Question',\n"
     "      ad_kr: 'Alignment Dialogue with the Board Chair · Key Result chosen',\n"
     "      ad_goal: 'Alignment Dialogue with the Board Chair · Goal',\n"
     "      ad_reality: 'Alignment Dialogue with the Board Chair · Reality',\n"
     "      ad_options: 'Alignment Dialogue with the Board Chair · Options',\n"
     "      ad_will: 'Alignment Dialogue with the Board Chair · Will',\n"
     "      ex_record: 'Establishing Delivery Expectations — record while the group works',\n"
     "      ex_future: 'Expectations · 5.1 · Step 1 · Start With the Future — confirmed',\n"
     "      ex_delivery: 'Expectations · 5.1 · Step 2 · Clarify the Delivery Expectation — confirmed',\n"
     "      ex_chain: 'Expectations · 5.1 · Step 3 · Identify the Expectations Chain — confirmed',\n"
     "      ex_ownership: 'Expectations · 5.1 · Step 4 · Confirm Ownership — confirmed',\n"
     "      ex_dialogue: 'Expectations · 5.2 · Alignment Dialogue with the Board Chair — confirmed',\n"
     "      confirmed_items: 'Confirmed by the group',\n      app_role: 'Critical Role Identification',\n"),
])
patch('build_collection.js', [
    (", u3m1_lens5:/^(pm_(record|scoring|faces|execution|scorecards)$|confirmed_items$)/i };',",
     ", u3m1_lens5:/^(pm_(record|scoring|faces|execution|scorecards)$|confirmed_items$)/i, u3m1_lens6:/^(ex_(record|future|delivery|chain|ownership|dialogue)$|confirmed_items$)/i };',"),
])
