# -*- coding: utf-8 -*-
"""Unit 9 · go-live wiring (16 Oct 2026): Capstone boxes 9A–9E and PULL.u9, report labels, Learning Portfolio filter.
Usage: python3 golive_u09pv.py <capstone_P.html> <dashboard_F.html> <build_collection.js> <out folder>"""
import sys, os
cap, dash, coll, out = sys.argv[1:5]
def rd(p): return open(p, encoding='utf-8', newline='').read()
def once(t, a, b):
    assert t.count(a) == 1, (t.count(a), a[:90]); return t.replace(a, b)
def nl(t): return '\r\n' if '\r\n' in t else '\n'
# ── Capstone
t = rd(cap); N = nl(t)
old = t[t.index("    { key:'u9', unit:9, title:'Strategic Unclogging', boxes:["):t.index("    { key:'u10', unit:10,")]
new = N.join(["    { key:'u9', unit:9, title:'Strategic Unclogging', boxes:[",
 "      ['9A','Original challenge','The original work-based challenge selected for [Case], and the strategic Objective and Key Result or KPI it affects.'],",
 "      ['9B','Performance clog','The Seven Performance Clog that best explains the challenge, and the observations behind the diagnosis.'],",
 "      ['9C','Unclogging lever','The Strategic Unclogging Lever selected for the clog, and how it addresses it.'],",
 "      ['9D','Review and Realign','The performance reality across the three lines of sight and the diagnosis check; the collective response for people performance and organisational performance, with executive ownership.'],",
 "      ['9E','Restore','The intervention through the selected lever, the action and completion date, the evidence of recovery for people and organisational performance, and the review commitment.']",
 "    ]},", ""])
t = t.replace(old, new)
t = once(t, "      ['8D','rd_credibility','Review Discipline · Leadership Credibility']" + N + "    ]}" + N + "  };",
         "      ['8D','rd_credibility','Review Discipline · Leadership Credibility']" + N + "    ]}," + N +
         "    u9: { lens:'u3m2_lens8', rows:[" + N +
         "      ['9A','uc_challenge','Unclogging · Original Challenge']," + N +
         "      ['9B','uc_clog','Unclogging · Performance Clog']," + N +
         "      ['9C','uc_lever','Unclogging · Unclogging Lever']," + N +
         "      ['9D','uc_review_realign','Unclogging · Review and Realign']," + N +
         "      ['9E','uc_restore','Unclogging · Restore']" + N + "    ]}" + N + "  };")
open(os.path.join(out, 'capstone_P.html'), 'w', encoding='utf-8', newline='').write(t)
# ── Facilitator report
t = rd(dash); N = nl(t)
t = once(t, "      app_followup: 'Follow-Up Review Date'" + N + "    },",
         "      app_followup: 'Follow-Up Review Date'," + N +
         "      ref7: 'My Executive Contribution to Performance'," + N +
         "      ref8: 'My Leadership Contribution to Strategic Unclogging'," + N +
         "      uc_record: 'Strategic Unclogging Clinic — record while the group works'," + N +
         "      uc_challenge: 'Strategic Unclogging Clinic · 5.1 Original Work-Based Challenge — confirmed'," + N +
         "      uc_clog: 'Strategic Unclogging Clinic · 5.2 Performance Clog — confirmed'," + N +
         "      uc_lever: 'Strategic Unclogging Clinic · 5.3 Strategic Unclogging Lever — confirmed'," + N +
         "      uc_review_realign: 'Strategic Unclogging Clinic · 5.4 Review and Realign — confirmed'," + N +
         "      uc_restore: 'Strategic Unclogging Clinic · 5.4 Restore — confirmed'," + N +
         "      confirmed_items: 'Confirmed by the group'" + N + "    },")
t = once(t, '6:"Your Contribution to the Enterprise Unclogging Agenda"},', '6:"Your Contribution to the Enterprise Unclogging Agenda",7:"My Executive Contribution to Performance",8:"My Leadership Contribution to Strategic Unclogging"},')
t = once(t, "      { name: 'Working Papers',", "      { name: 'The Strategic Unclogging Clinic', test: function (k) { return /^uc_(record|challenge|clog|lever|review_realign|restore)$/i.test(k); } }," + N + "      { name: 'Working Papers',")
open(os.path.join(out, 'dashboard_F.html'), 'w', encoding='utf-8', newline='').write(t)
# ── Learning Portfolio: group work stays out
t = rd(coll)
t = once(t, "u3m2_lens7:/^(rd_(record|warning|accountability|learning|credibility)$|confirmed_items$)/i };", "u3m2_lens7:/^(rd_(record|warning|accountability|learning|credibility)$|confirmed_items$)/i, u3m2_lens8:/^(uc_(record|challenge|clog|lever|review_realign|restore)$|confirmed_items$)/i };")
open(os.path.join(out, 'build_collection.js'), 'w', encoding='utf-8', newline='').write(t)
print('written to', out)
