# -*- coding: utf-8 -*-
"""Unit 10 links: Capstone boxes 10A-10D and PULL.u10 (capstone_P.html), report labels (dashboard_F.html), Learning Portfolio keys (build_collection.js).
Usage: python3 -B patch_links_u10.py <portal folder> <out folder>   (CRLF kept as found)"""
import sys, os, re
src, out = sys.argv[1:3]
def rd(p):
    b = open(os.path.join(src, p), 'rb').read().decode('utf-8'); crlf = '\r\n' in b
    return b.replace('\r\n', '\n'), crlf
def wr(p, t, crlf):
    os.makedirs(out, exist_ok=True); open(os.path.join(out, p), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
def sub1(t, pat, rep):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=re.S); assert n == 1, pat[:60]; return t2
NAMES = ['ESRG Clinic · Enterprise Scanner','ESRG Clinic · Collective Findings','ESRG Clinic · Collective Intelligence Response','ESRG Clinic · Intervention Plan']
# capstone
t, c = rd('capstone_P.html')
t = sub1(t, r"\{ key:'u10', unit:10, title:'ESRG Alignment', boxes:\[.*?\]\},", """{ key:'u10', unit:10, title:'ESRG Alignment', boxes:[
      ['10A','Enterprise ESRG Scanner','The capability profile of [Case]’s executive functions for the assessment period, consolidated from each function’s ESRG scanner, with any missing submissions or evidence gaps.'],
      ['10B','Collective findings','The convergence, divergence and dependency findings for each execution-enabling capability, with the evidence behind them.'],
      ['10C','Collective Intelligence Response','The agreed responses: ESRG component, collective finding, strategic commitment affected, response and functions involved.'],
      ['10D','ESRG Alignment Intervention Plan','For each agreed response: implementation actions, accountable executive, contributing functions, target date and evidence of improvement.']
    ]},""")
m = re.search(r"    u9: \{ lens:'u3m2_lens8', rows:\[.*?\]\}\n  \};", t, re.S); assert m
u10 = "    u10: { lens:'u4m1_lens9', rows:[\n" + ',\n'.join("      ['10%s','%s','%s']" % ('ABCD'[i], k, NAMES[i]) for i, k in enumerate(['es_scanner','es_interp','es_resp','es_plan'])) + "\n    ]}\n  };"
t = t[:m.end() - len('\n  };')] + ',\n' + u10 + t[m.end():]
wr('capstone_P.html', t, c)
# dashboard labels
t, c = rd('dashboard_F.html')
t = sub1(t, r"    u4m1_lens9: \{\n      ref1: 'The Grounding Question',.*?app_commit: 'COC Commitment'\n    \},", """    u4m1_lens9: {
      bias_e: 'My Executive ESRG Bias · Environment',
      bias_s: 'My Executive ESRG Bias · Systems',
      bias_r: 'My Executive ESRG Bias · Resources',
      bias_g: 'My Executive ESRG Bias · Governance',
      esrg_scan_head: 'My Capstone Function (4.5)',
      esrg_scan: 'My Functional ESRG Performance Scanner (4.5)',
      es_scanner: 'ESRG Clinic · 5.1 Enterprise ESRG Scanner — agreed',
      es_interp: 'ESRG Clinic · 5.2 Collective Findings — agreed',
      es_resp: 'ESRG Clinic · 5.3 Collective Intelligence Response — agreed',
      es_plan: 'ESRG Clinic · 5.4 ESRG Alignment Intervention Plan — agreed'
    },""")
t = sub1(t, r'      u4m1_lens9: \{1:"The Grounding Question"[^\n]*\},\n', '      u4m1_lens9: {},\n')
t = sub1(t, r"      \{ name: 'ESRG Alignment Agenda',    test: function \(k\) \{ return /\^esrg_/i\.test\(k\); \} \},",
 "      { name: 'My Executive ESRG Bias',   test: function (k, lensId) { return /^bias_[esrg]$/i.test(k) && lensId === 'u4m1_lens9'; } },\n"
 "      { name: 'Functional ESRG Assessment', test: function (k) { return /^esrg_/i.test(k); } },\n"
 "      { name: 'Enterprise ESRG Alignment Clinic', test: function (k, lensId) { return /^es_(scanner|interp|resp|plan)$/i.test(k) && lensId === 'u4m1_lens9'; } },")
wr('dashboard_F.html', t, c)
# Learning Portfolio: group work stays out
t, c = rd('build_collection.js')
t = sub1(t, r"u3m2_lens8:/\^\(uc_\(record\|challenge\|clog\|lever\|review_realign\|restore\)\$\|confirmed_items\$\)/i \};",
 "u3m2_lens8:/^(uc_(record|challenge|clog|lever|review_realign|restore)$|confirmed_items$)/i, u4m1_lens9:/^(es_(scanner|interp|resp|plan)$|confirmed_items$)/i };")
wr('build_collection.js', t, c)
print('links written to', out)
