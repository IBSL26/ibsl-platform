# -*- coding: utf-8 -*-
"""Unit 11 links: Capstone boxes 11A-11D and PULL.u11 (capstone_P.html), report labels (dashboard_F.html), Learning Portfolio keys (build_collection.js).
Usage: python3 -B patch_links_u11.py <portal folder> <out folder>   (CRLF kept as found)"""
import sys, os, re
src, out = sys.argv[1:3]
def rd(p):
    b = open(os.path.join(src, p), 'rb').read().decode('utf-8'); crlf = '\r\n' in b
    return b.replace('\r\n', '\n'), crlf
def wr(p, t, crlf):
    os.makedirs(out, exist_ok=True); open(os.path.join(out, p), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
def sub1(t, pat, rep):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=re.S); assert n == 1, pat[:60]; return t2
NAMES = ['Health Clinic · Functional Health Assessments','Health Clinic · Consolidated Health Position','Health Clinic · Review–Realign–Restore','Health Clinic · Organisational Health Response']
KEYS = ['oh_func','oh_cons','oh_rrr','oh_resp']
t, c = rd('capstone_P.html')
t = sub1(t, r"\{ key:'u11', unit:11, title:'Culture Reinforcement & Organisational Health', boxes:\[.*?\]\},", """{ key:'u11', unit:11, title:'Culture Reinforcement & Organisational Health', boxes:[
      ['11A','Functional health assessments','For each CXO function represented in [Case]’s executive team: the functional health score and classification, the two weakest traits, cultural vulnerabilities, evidence to investigate, and the largest hidden cost with the evidence needed to validate it.'],
      ['11B','Consolidated health position','The response-weighted health score and classification for the represented functions, the weakest traits, gross quarterly exposure by hidden cost, and the EXCO diagnosis.'],
      ['11C','Review–Realign–Restore','The prioritised organisational health diagnosis, the cultural reinforcement actions with named executive accountability, and the measurable health and performance commitments.'],
      ['11D','Organisational Health Response','For the lowest-scoring health trait: the Review–Realign–Restore action, accountable CXO(s), health improvement target, associated hidden cost and financial reduction target.']
    ]},""")
m = re.search(r"    u10: \{ lens:'u4m1_lens9', rows:\[.*?\]\}\n  \};", t, re.S); assert m
u11 = "    u11: { lens:'u4m1_lens10', rows:[\n" + ',\n'.join("      ['11%s','%s','%s']" % ('ABCD'[i], k, NAMES[i]) for i, k in enumerate(KEYS)) + "\n    ]}\n  };"
t = t[:m.end() - len('\n  };')] + ',\n' + u11 + t[m.end():]
wr('capstone_P.html', t, c)
t, c = rd('dashboard_F.html')
t = sub1(t, r"    u4m1_lens10: \{\n      ref1: 'The Best Team Environment',.*?app_commit: 'Coaching Commitment'\n    \},", """    u4m1_lens10: {
      ref7: 'My Functional Health Accountability',
      oh_func: 'Health Clinic · Functional Health Assessments — agreed',
      oh_cons: 'Health Clinic · Consolidated Health Position — agreed',
      oh_rrr: 'Health Clinic · Review–Realign–Restore — agreed',
      oh_resp: 'Health Clinic · Organisational Health Response — agreed'
    },""")
t = sub1(t, r'      u4m1_lens10: \{1:"The Best Team Environment"[^\n]*\},\n', '      u4m1_lens10: {7:"My Functional Health Accountability"},\n')
t = sub1(t, r"      \{ name: 'Health Thermometer',       test: function \(k\) \{ return /\^app_thermo\$/i\.test\(k\); \} \},\n",
 "      { name: 'Health Thermometer',       test: function (k) { return /^app_thermo$/i.test(k); } },\n"
 "      { name: 'Cross-CXO Organisational Health Clinic', test: function (k, lensId) { return /^oh_(func|cons|rrr|resp)$/i.test(k) && lensId === 'u4m1_lens10'; } },\n")
wr('dashboard_F.html', t, c)
t, c = rd('build_collection.js')
t = sub1(t, r"u4m1_lens9:/\^\(es_\(scanner\|interp\|resp\|plan\)\$\|confirmed_items\$\)/i \};",
 "u4m1_lens9:/^(es_(scanner|interp|resp|plan)$|confirmed_items$)/i, u4m1_lens10:/^(oh_(func|cons|rrr|resp)$|confirmed_items$)/i };")
wr('build_collection.js', t, c)
print('links written to', out)
