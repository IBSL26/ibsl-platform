# -*- coding: utf-8 -*-
"""Unit 4 rebuild (October 2026): the facilitator report, the Capstone and the Learning Portfolio follow the new Unit 4 answers.
Usage: python3 patch_links.py <dashboard_F.html> <capstone_P.html> <build_collection.js> <output folder>
Byte-exact: every edit must match exactly once or nothing is written. Line endings are kept. Then run `node build_collection.js`."""
import sys, os
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

# ── dashboard_F.html: headings and labels for the facilitator report ──
mbt = "      { name: 'MBT Conditions',           test: function (k) { return /^mbt_(arena|bound|comp|value)$/i.test(k); } },\n"
wp_a = "      { name: 'Working Papers',           test: function (k) { return /^syn_(themes|disagree|top5)$/i.test(k)"
old_labels = """    u2m1_lens3: {
      ref1: 'The Problem with Well-Written OKRs',
      ref2: 'Four ABCV Integrity Checkpoints',
      ref3: 'Industry Illusion & Arena Shift',
      ref4: 'Executive Hot Zone',
      ref5: 'Closing Commitment',
      mbt_arena: 'MBT · Arena',
      mbt_bound: 'MBT · Boundaries',
      mbt_comp: 'MBT · Competition',
      mbt_value: 'MBT · Value Proposition',
"""
new_labels = """    u2m1_lens3: {
      ref1: 'From Unit 3 to Unit 4',
      ref2: 'Bringing ABCV Together',
      ref3: 'Industry Illusion & Arena Shift',
      ref4: 'Executive Hot Zone',
      ref5: 'Closing Commitment',
      ii_round1: 'Round 1 · Where would you look? (portfolio work)',
      ii_round2: 'Round 2 · What deserves attention? (portfolio work)',
      ii_round3: 'Round 3 · Should we be worried? (portfolio work)',
      ii_arena: 'Arena · the three depths and the final challenge (portfolio work)',
      ii_status: 'Game status',
      mbt_record: 'Four-step record — every Key Result, its entries and its Must-Be-True conditions',
      mbt_arena: 'Step 1 · Define the Arena — confirmed',
      mbt_bound: 'Step 2 · Understand the Boundaries — confirmed',
      mbt_comp: 'Step 3 · See the Competition — confirmed',
      mbt_value: 'Step 4 · Establish the Value Proposition — confirmed',
      confirmed_items: 'Confirmed by the group',
      mine_result: 'Cause of Death — score and attempts (portfolio work)',
"""
patch(dash, [
    (mbt, "      { name: 'Industry Illusion Game',   test: function (k) { return /^ii_(round[123]|arena|status)$/i.test(k); } },\n"
          "      { name: 'ABCV–MBT: Stress-Testing the Key Results', test: function (k) { return /^mbt_(record|arena|bound|comp|value)$/i.test(k); } },\n"
          "      { name: 'Cause of Death',           test: function (k) { return /^mine_result$/i.test(k); } },\n"),
    (old_labels, new_labels),
], '\r\n')

# ── capstone_P.html: bring the confirmed Unit 4 outputs in from the member's own Unit 4 page; Arena read at the three depths of 1.1 ──
patch(cap, [
    ("""      ['3F','ent_okrs','Enterprise OKRs']
    ]}
  };
""", """      ['3F','ent_okrs','Enterprise OKRs']
    ]},
    u4: { lens:'u2m1_lens3', rows:[
      ['4A','mbt_arena','MBT · Arena'],
      ['4B','mbt_bound','MBT · Boundaries'],
      ['4C','mbt_comp','MBT · Competition'],
      ['4D','mbt_value','MBT · Value Proposition']
    ]}
  };
"""),
    ("['4A','Arena','State the functional, emotional and social outcome [Case]’s customers pursue,", "['4A','Arena','State the functional, experiential and consequential outcome [Case]’s customers pursue,"),
], '\r\n')

# ── build_collection.js: the Unit 4 group work feeds the Capstone and is left out of the Learning Portfolio ──
patch(bc, [
    ("|okr_drafts$|ent_priorities$|ent_okrs$|confirmed_items$)/i };',",
     "|okr_drafts$|ent_priorities$|ent_okrs$|confirmed_items$)/i, u2m1_lens3:/^(mbt_(record|arena|bound|comp|value)$|syn_(themes|disagree|top5)$|own_(internal|external|timeline)$|team_name$|exec_(name|role)$|confirmed_items$)/i };',"),
], '\n')
