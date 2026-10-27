# -*- coding: utf-8 -*-
"""Unit 12 rework from Carol's approved Word document (27 Oct 2026), applied on the pages backed up before the Module 4 rework.
Usage: python3 -B build_u12.py <participant in> <facilitator in> <out folder>
Pages are CRLF: normalised to \\n here, CRLF restored on write."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u12_html as H
from u12_content import *
p_in, f_in, out = sys.argv[1:4]
def read(x): return open(x, 'rb').read().decode('utf-8').replace('\r\n', '\n')
def write(x, t): open(x, 'wb').write(t.replace('\n', '\r\n').encode('utf-8'))
def sub1(t, pat, rep, flags=re.S):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=flags); assert n == 1, 'no match: ' + pat[:80]; return t2
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:80]); return t.replace(a, b)
def hero(t, mod, title, sub):
    m = t.index('id="%s"' % mod)
    return t[:m] + sub1(t[m:], r'<h2>.*?</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (title, sub))
def body(t, mod, end, html):
    m = t.index('id="%s"' % mod)
    a = t.index('<div class="slo-box">', m); b = t.index(end, a)
    return t[:a] + html + t[b:]

def common(t, fac):
    t = sub1(t, r'    <div class="unit-sub">.*?<div class="klo-bar">.*?</div>', H.header())
    i = t.index('</style>'); t = t[:i] + H.css(fac) + t[i:]
    return t

NAV = lambda k, prev: '<div class="mod-nav"><button class="btn%s" onclick="showMod(%d)">' % (' prev' if prev else '', k)

# ---- participant
p = common(read(p_in), False)
SECS = [(S1_TITLE, S1_HERO, H.section1), (S2_TITLE, S2_HERO, H.section2), (S3_TITLE, S3_HERO, H.section3), (S4_TITLE, S4_HERO, H.section4)]
for k, (title, sub, fn) in enumerate(SECS):
    p = hero(p, 'mod%d' % k, title, sub)
    p = body(p, 'mod%d' % k, NAV(1, False) if k == 0 else NAV(k - 1, True), fn(False))
p = hero(p, 'mod4', S5_TITLE, S5_HERO)
p = body(p, 'mod4', '<!-- MICRO-CLIMB SUMMARY', H.section5(False))
p = once(p, '<script src="/s2r-save.js"></script>', '<script src="/s2r-save.js"></script>\n<script src="/s2r-team.js"></script>')
p = sub1(p, r'var KEYS=\["team_name","ref1",[^\]]*\];', 'var KEYS=["ref11","ref12","ref13"];')
p = once(p, '["ref2","ref7","ref8","ref9","ref10","app_nav_force","app_nav_abcv","app_nav_commit"].forEach(hydrateField);\n    hydrateScenario();\n    loadSubmissionFeedback();',
         '["ref13"].forEach(hydrateField);\n    loadSubmissionFeedback();\n    u12S5Start(responses);')
p = sub1(p, r'var FIELD_SPECS=\{\n.*?\n\};', 'var FIELD_SPECS={\n  ref13:[%s]\n};' % ','.join('{l:"%s",k:"text"}' % x for x in R31_F))
p = sub1(p, r'var SUMMARY=\[\n.*?\n\];', H.summary_js())
p = once(p, '/* ── Init ── */', H.js() + '\n/* ── Init ── */')
for k in ['ref1', 'ref2', 'ref7', 'ref8', 'ref9', 'ref10', 'app_nav_force', 'team_name', 'app_kiss_keep']:
    assert 'id="%s"' % k not in p, k
for k in ['ref11', 'ref12', 'ref13']:
    assert p.count('id="%s"' % k) == 1, k

# ---- facilitator
f = common(read(f_in), True)
f = once(f, '<h2>Session Overview</h2><p>The final unit of the S2R&reg; programme. Orientation, facilitation questions, tone guidance, and session structure.</p>',
         '<h2>Session Overview</h2><p>%s</p>' % GUIDE_HERO)
a = f.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>')
b = f.index(NAV(1, False) + 'Section 1', a)
f = f[:a] + H.guide() + f[b:]
SECF = SECS + [(S5_TITLE, S5_HERO_F, None)]
for k, (title, sub, fn) in enumerate(SECF):
    mod = 'mod%d' % (k + 1)
    f = hero(f, mod, title, sub)
    if fn:
        f = body(f, mod, NAV(k, True), fn(True))
    else:
        f = body(f, mod, NAV(4, True), H.section5(True) + H.summary_f())
assert f.count('Unit 12 synthesis') == 1

for t in (p, f):
    vis = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>', ' ', t)
    assert not re.search(r'\blens\b', vis, re.I), 'lens in visible text'
    for w in ['ABCV', 'Navigation Chain', 'Five Forces', 'COMPASS', 'thirty days', 'Keep climbing']:
        assert w not in vis, w
os.makedirs(out, exist_ok=True)
write(os.path.join(out, 'unit4_m2_lens11_p.html'), p)
write(os.path.join(out, 'unit4_m2_lens11_f.html'), f)
print('built', out)
