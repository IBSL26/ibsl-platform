# -*- coding: utf-8 -*-
"""Unit 3 rebuild (October 2026): the facilitator report and the Capstone follow the new Unit 3 answers.
Usage: python3 patch_links.py <dashboard_F.html> <capstone_P.html> <output folder>
Byte-exact: every edit must match exactly once or nothing is written. Line endings are kept."""
import sys, os
dash, cap, out = sys.argv[1:4]
NL = '\r\n'
def patch(path, edits):
    b = open(path, 'rb').read().decode('utf-8')
    for old, new in edits:
        n = b.count(old)
        assert n == 1, 'expected 1 match, found %d in %s: %s' % (n, os.path.basename(path), old[:80])
        b = b.replace(old, new)
    open(os.path.join(out, os.path.basename(path)), 'wb').write(b.encode('utf-8'))
    print('written', os.path.basename(path), len(b))
# ── dashboard_F.html ──
fam = "      { name: 'KISS Mapping',             test: function (k) { return /^kex_/i.test(k); } }," + NL
lab = "      okr_o4: 'OKR · Value Creation'" + NL + "    }," + NL
patch(dash, [
    (fam, "      { name: 'Hot Zone Matching',        test: function (k) { return /^hz_match$/i.test(k); } }," + NL + fam +
          "      { name: 'KISS Map — Confirmed',     test: function (k) { return /^kiss_(keep|improve|start|stop)$/i.test(k); } }," + NL +
          "      { name: 'Enterprise Priorities & OKRs', test: function (k) { return /^(okr_drafts|ent_priorities|ent_okrs)$/i.test(k); } }," + NL +
          "      { name: 'Strategy Airport',         test: function (k) { return /^game_(kiss|flight_plan|round)$/i.test(k); } }," + NL),
    (lab, "      okr_o4: 'OKR · Value Creation'," + NL +
          "      hz_match: 'Typical Hot Zone and Alignment Question matched to each role (portfolio work)'," + NL +
          "      sip_d1_st: 'D1 · Customer Experience & Value — SiP statement used for the KISS map'," + NL +
          "      sip_d2_st: 'D2 · Operational Capability & Execution Rhythm — SiP statement used for the KISS map'," + NL +
          "      sip_d3_st: 'D3 · People & Culture Dynamics — SiP statement used for the KISS map'," + NL +
          "      sip_d4_st: 'D4 · Enterprise Value Creation — SiP statement used for the KISS map'," + NL +
          "      kiss_keep: 'Keep — confirmed'," + NL +
          "      kiss_improve: 'Improve — confirmed'," + NL +
          "      kiss_start: 'Start — confirmed'," + NL +
          "      kiss_stop: 'Stop — confirmed'," + NL +
          "      okr_drafts: 'Five-step record — themes, Objectives, Key Results, alignment test and matrix'," + NL +
          "      ent_priorities: 'Enterprise Priorities — confirmed'," + NL +
          "      ent_okrs: 'Enterprise OKRs — confirmed'," + NL +
          "      confirmed_items: 'Confirmed by the group'," + NL +
          "      game_kiss: 'Gate 1 · Baggage Check — KISS choices (portfolio work)'," + NL +
          "      game_flight_plan: 'Gate 2 · Flight Plan — Objective, Key Results and contributing roles (portfolio work)'," + NL +
          "      game_round: 'Learning round'" + NL + "    }," + NL),
    ("    ev: 'Financial Performance & Value Creation'" + NL, "    ev: 'Enterprise Value Creation'" + NL),
])
# ── capstone_P.html: bring the confirmed Unit 3 outputs in from the member's own Unit 3 page ──
old = "      ['2F','sip_d4_st','SiP · Enterprise Value Creation']" + NL + "    ]}" + NL + "  };" + NL
patch(cap, [(old, "      ['2F','sip_d4_st','SiP · Enterprise Value Creation']" + NL + "    ]}," + NL +
    "    u3: { lens:'u2m1_lens2', rows:[" + NL +
    "      ['3A','kiss_keep','KISS · Keep']," + NL +
    "      ['3B','kiss_improve','KISS · Improve']," + NL +
    "      ['3C','kiss_start','KISS · Start']," + NL +
    "      ['3D','kiss_stop','KISS · Stop']," + NL +
    "      ['3E','ent_priorities','Enterprise priorities']," + NL +
    "      ['3F','ent_okrs','Enterprise OKRs']" + NL +
    "    ]}" + NL + "  };" + NL)])
