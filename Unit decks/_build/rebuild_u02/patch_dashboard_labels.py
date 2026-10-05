# -*- coding: utf-8 -*-
"""Unit 2 rebuild (5 Oct 2026): labels for the new Unit 2 response keys in the facilitator report.
Usage:  python3 patch_dashboard_labels.py <dashboard_F.html as it stood before the rebuild> [--write]
Run it on the pre-rebuild file ('dashboard_F - before rebuild (5 Oct afternoon).html' copied over dashboard_F.html).
Byte-exact: every edit must match exactly once or nothing is written. Line endings are kept."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ELEMENTS, SIP_DOMAINS, el_q, el_rs, sip_q, sip_st
path = sys.argv[1]; write = '--write' in sys.argv
b = open(path, 'rb').read(); orig = b
def rep(old, new):
    global b
    n = b.count(old.encode('utf-8'))
    assert n == 1, 'expected 1 match, found %d: %s' % (n, old[:80])
    b = b.replace(old.encode('utf-8'), new.encode('utf-8'))
NL = '\r\n'
q = lambda s: json.dumps(s, ensure_ascii=False)
# 1. Families (collapsible headings in the report)
anchor = "      { name: 'Strategic Intent (SiP)',   test: function (k) { return /^sip_data$/i.test(k); } }," + NL
rep(anchor, anchor +
    "      { name: 'Strategy Architecture',    test: function (k) { return /^arch_(e\\d+_(q\\d|rs)|output)$/i.test(k) || /^(org_name|strategy_period)$/i.test(k); } }," + NL +
    "      { name: 'Strategy Intent Statement', test: function (k) { return /^intent_statement$/i.test(k); } }," + NL +
    "      { name: 'Success in Practice (SiP)', test: function (k) { return /^sip_(d[1-4]_(q\\d|st)|integrated)$/i.test(k); } }," + NL +
    "      { name: 'Confirmed by the Group',   test: function (k) { return /^confirmed_items$/i.test(k); } }," + NL +
    "      { name: 'Collective Application',   test: function (k) { return /^col_(alignment|gaps|tensions|ownership)$/i.test(k); } }," + NL)
rep("{ name: 'Section 1.5 · CXO SiP Application', test:", "{ name: 'Role Contribution to SiP', test:")
# 2. Keep each element's questions and position together, in element order
anchor = "        if (fam.name === 'KISS Navigation Response') {" + NL
rep(anchor,
    "        if (fam.name === 'Strategy Architecture' || fam.name === 'Success in Practice (SiP)') {" + NL +
    "          famEntries = famEntries.slice().sort(function (a, b) { return a.fieldName < b.fieldName ? -1 : (a.fieldName > b.fieldName ? 1 : 0); });" + NL +
    "        }" + NL + anchor)
# 3. Per-key labels
new = ''
for i, (name, tag, guide, qs) in enumerate(ELEMENTS, 1):
    for j, question in enumerate(qs, 1):
        new += "      %s: %s," % (el_q(i, j), q('%d · %s — %s' % (i, name, question))) + NL
    new += "      %s: %s," % (el_rs(i), q('%d · %s — What this is saying (confirmed position)' % (i, name))) + NL
new += "      arch_output: 'Strategy Architecture Output'," + NL + "      org_name: 'Organisation'," + NL + "      strategy_period: 'Strategy Period'," + NL
new += "      intent_statement: 'Strategy Intent Statement'," + NL
for d, (title, lead, qs) in enumerate(SIP_DOMAINS, 1):
    for j, question in enumerate(qs, 1):
        new += "      %s: %s," % (sip_q(d, j), q('D%d · %s' % (d, question))) + NL
    new += "      %s: %s," % (sip_st(d), q('D%d · %s — Confirmed statement' % (d, title))) + NL
new += "      sip_integrated: 'Success in Practice — the four statements together'," + NL
new += "      confirmed_items: 'Confirmed by the group'," + NL
new += "      col_alignment: 'Alignment'," + NL + "      col_gaps: 'Gaps'," + NL + "      col_tensions: 'Tensions'," + NL + "      col_ownership: 'Execution Ownership'," + NL
new += "      ref6: 'Three Functions'," + NL + "      ref7: 'Integration'," + NL
anchor2 = "    u2m1_lens1: {" + NL + "      ref1: 'The Definition'," + NL + "      ref2: 'Strategic Intent'," + NL
rep(anchor2, "    u2m1_lens1: {" + NL + new + "      ref1: 'Strategy Architecture'," + NL + "      ref2: 'Strategy Intent'," + NL)
rep('u2m1_lens1: {1:"The Definition",2:"Strategic Intent",3:"Co-Creation",4:"SiP Indicators",5:"Maturity Assessment"},',
    'u2m1_lens1: {1:"Strategy Architecture",2:"Strategy Intent",3:"Co-Creation",4:"SiP Indicators",5:"Maturity Assessment",6:"Three Functions",7:"Integration"},')
print('edits ready: %d -> %d bytes' % (len(orig), len(b)))
if write:
    open(path, 'wb').write(b); print('written')
else:
    print('dry run (add --write to save)')
