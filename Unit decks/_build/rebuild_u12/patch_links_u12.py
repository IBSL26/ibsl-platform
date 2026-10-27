# -*- coding: utf-8 -*-
"""Unit 12 links: Capstone boxes 12A-12D and PULL.u12 (capstone_P.html), report labels (dashboard_F.html), Learning Portfolio keys (build_collection.js).
Usage: python3 -B patch_links_u12.py <portal folder> <out folder>   (CRLF kept as found)"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from u12_content import CAP, NAMES, KEYS
src, out = sys.argv[1:3]
def rd(p):
    b = open(os.path.join(src, p), 'rb').read().decode('utf-8'); crlf = '\r\n' in b
    return b.replace('\r\n', '\n'), crlf
def wr(p, t, crlf):
    os.makedirs(out, exist_ok=True); open(os.path.join(out, p), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
def sub1(t, pat, rep):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=re.S); assert n == 1, pat[:60]; return t2

t, c = rd('capstone_P.html')
t = sub1(t, r"\{ key:'u12', unit:12, title:'Sustaining Performance', boxes:\[.*?\]\}",
         "{ key:'u12', unit:12, title:'Sustaining Performance', boxes:[\n" + ',\n'.join("      ['%s','%s','%s']" % x for x in CAP) + "\n    ]}")
m = re.search(r"    u11: \{ lens:'u4m1_lens10', rows:\[.*?\]\}\n  \};", t, re.S); assert m
u12 = "    u12: { lens:'u4m2_lens11', rows:[\n" + ',\n'.join("      ['12%s','%s','%s']" % ('ABCD'[i], k, NAMES[i]) for i, k in enumerate(KEYS)) + "\n    ]}\n  };"
t = t[:m.end() - len('\n  };')] + ',\n' + u12 + t[m.end():]
wr('capstone_P.html', t, c)

t, c = rd('dashboard_F.html')
t = sub1(t, r"    u4m2_lens11: \{\n      ref1: 'The Navigation Premise',.*?app_nav_commit: 'Navigation Commitment · KISS Decision'\n    \}", """    u4m2_lens11: {
      ref11: 'The Line of Sight We Read Least',
      ref12: 'A Drifting Practice and the KISS Decision That Holds It',
      ref13: 'Where Drift Shows First in My Role',
      qs_strategic: 'Quarterly Lines of Sight · Strategic — agreed',
      qs_operational: 'Quarterly Lines of Sight · Operational — agreed',
      qs_behavioural: 'Quarterly Lines of Sight · Behavioural — agreed',
      qs_kiss: 'Quarterly Lines of Sight · KISS for Next Quarter — agreed'
    }""")
t = sub1(t, r'      u4m2_lens11: \{1:"The Navigation Premise"[^\n]*\}',
         '      u4m2_lens11: {11:"The Line of Sight We Read Least",12:"A Drifting Practice and the KISS Decision That Holds It",13:"Where Drift Shows First in My Role"}')
t = sub1(t, r"      \{ name: 'Navigation Commitment',    test: function \(k\) \{ return /\^app_nav_/i\.test\(k\); \} \}",
         "      { name: 'Navigation Commitment',    test: function (k) { return /^app_nav_/i.test(k); } },\n"
         "      { name: 'Quarterly Three Lines of Sight', test: function (k, lensId) { return /^qs_(strategic|operational|behavioural|kiss)$/i.test(k) && lensId === 'u4m2_lens11'; } }")
wr('dashboard_F.html', t, c)

t, c = rd('build_collection.js')
t = sub1(t, r"u4m1_lens10:/\^\(oh_\(func\|cons\|rrr\|resp\|coc\)\$\|confirmed_items\$\)/i \};",
         "u4m1_lens10:/^(oh_(func|cons|rrr|resp|coc)$|confirmed_items$)/i, u4m2_lens11:/^(qs_(strategic|operational|behavioural|kiss)$|confirmed_items$)/i };")
wr('build_collection.js', t, c)
print('links written to', out)
