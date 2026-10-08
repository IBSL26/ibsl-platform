# -*- coding: utf-8 -*-
"""Unit 5 three-way match (October 2026): the Capstone, the Learning Portfolio and the facilitator report follow the Unit 5 group work.
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

# ── dashboard_F.html: the report names the Step 4 confirmation ──
patch(dash, [
    ("      syn_sequence: 'Synthesis · Changes on the Same Group and Agreed Sequence',\n      syn_30day: 'Synthesis · 30-Day Behavioural Commitment'\n    },\n",
     "      syn_sequence: 'Synthesis · Changes on the Same Group and Agreed Sequence',\n      syn_30day: 'Synthesis · 30-Day Behavioural Commitment',\n      confirmed_items: 'Confirmed by the group'\n    },\n"),
], '\r\n')

# ── capstone_P.html: bring the confirmed Unit 5 output in from the member's own Unit 5 page (box 5C). Boxes 5A, 5B, 5D and 5E are written by the team. ──
patch(cap, [
    ("""      ['4D','mbt_value','MBT · Value Proposition']
    ]}
  };
""", """      ['4D','mbt_value','MBT · Value Proposition']
    ]},
    u5: { lens:'u3m1_lens4', rows:[
      ['5C','syn_missing_compass','Synthesis · Underactivated COMPASS Domain(s)']
    ]}
  };
"""),
], '\r\n')

# ── build_collection.js: the Unit 5 group work feeds the Capstone and is left out of the Learning Portfolio ──
patch(bc, [
    ("|team_name$|exec_(name|role)$|confirmed_items$)/i };',",
     "|team_name$|exec_(name|role)$|confirmed_items$)/i, u3m1_lens4:/^(syn_(missing_compass|strong_compass|sequence)$|team_name$|exec_(name|role)$|confirmed_items$)/i };',"),
], '\n')
