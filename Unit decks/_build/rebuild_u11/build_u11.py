# -*- coding: utf-8 -*-
"""Unit 11 rework, applied section by section on the pages backed up before the Module 4 rework.
Usage: python3 -B build_u11.py <participant in> <facilitator in> <out folder>
Pages are CRLF: normalised to \\n here, CRLF restored on write."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u11_content as C
import u11_s2 as S2
import u11_s3 as S3
import u11_s4 as S4
import u11_s5 as S5
p_in, f_in, out = sys.argv[1:4]
def read(x): return open(x, 'rb').read().decode('utf-8').replace('\r\n', '\n')
def write(x, t): open(x, 'wb').write(t.replace('\n', '\r\n').encode('utf-8'))
def sub1(t, pat, rep, flags=re.S):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=flags); assert n == 1, 'no match: ' + pat[:80]; return t2
def once(t, a, b):
    assert t.count(a) == 1, 'expected once: ' + a[:80]; return t.replace(a, b)

def common(t, fac):
    t = sub1(t, r'    <div class="unit-sub">Grounding</div>\n.*?<div class="klo-bar">.*?</div>', C.header())
    i = t.index('</style>'); t = t[:i] + C.css(fac) + S2.css(fac) + S3.css(fac) + S4.css(fac) + S5.css(fac) + __import__('u11_coc').css(fac) + t[i:]
    return t

HERO_OLD = r'<h2>What is Organisational Health\?</h2><p>[^<]*</p>'
HERO_NEW = '<h2>%s</h2><p>%s</p>' % (C.S1_TITLE, C.HERO_P)

# ---- participant
p = common(read(p_in), False)
p = sub1(p, HERO_OLD, HERO_NEW)
a = p.index('<div class="slo-box">', p.index('id="mod0"'))
b = p.index('<div class="mod-nav"><button class="btn" onclick="showMod(1)">', a)
p = p[:a] + C.section1(False) + p[b:]
assert 'id="ref1"' not in p and 'id="ref2"' not in p and 'id="ref3"' not in p
p = once(p, '"team_name","exec_role","ref1","ref2","ref3","ref4"', '"team_name","exec_role","ref4"')
p = once(p, '["ref2","ref3","ref4","ref5","ref6","app_commit"].forEach(hydrateField);', '["ref4","ref5","ref6","app_commit"].forEach(hydrateField);')
p = sub1(p, r'  ref2:\[[^\n]*\],\n  ref3:\[[^\n]*\],\n', '')

# ---- participant Section 2
m = p.index('id="mod1"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S2.TITLE, S2.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(0)">', a)
p = p[:a] + S2.section2(False) + p[b:]
assert 'id="ref4"' not in p
p = once(p, '"team_name","exec_role","ref4"', '"team_name","exec_role"')
p = once(p, '["ref4","ref5","ref6","app_commit"].forEach(hydrateField);', '["ref5","ref6","app_commit"].forEach(hydrateField);')
p = sub1(p, r'  ref4:\[[^\n]*\],\n', '')

# ---- participant Section 3
m = p.index('id="mod2"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S3.TITLE, S3.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(1)">', a)
p = p[:a] + S3.section3(False) + p[b:]
assert 'id="ref5"' not in p and 'id="app_thermo"' not in p
p = once(p, '"team_name","exec_role","ref5","ref6","app_thermo",', '"team_name","exec_role","ref6",')
p = once(p, '["ref5","ref6","app_commit"].forEach(hydrateField);', '["ref6","app_commit"].forEach(hydrateField);')
p = sub1(p, r'  ref5:\[[^\n]*\],?\n', '')

# ---- participant Section 4
m = p.index('id="mod3"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S4.TITLE, S4.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(2)">', a)
p = p[:a] + S4.section4(False) + p[b:]
assert 'id="ref6"' not in p and 'id="team_name"' not in p
p = once(p, 'var KEYS=["team_name","exec_role","ref6",', 'var KEYS=["ref7",')
p = once(p, '["ref6","app_commit"].forEach(hydrateField);', '["ref7","app_commit"].forEach(hydrateField);')
p = sub1(p, r'  ref6:\[[^\n]*\],?\n', S4.FIELD_SPEC)
assert p.count('id="ref7"') == 1

# ---- participant Section 5 (group Capstone work on the shared group record); Unit Summary removed (as Unit 10)
m = p.index('id="mod4"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S5.TITLE, S5.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<!-- C1: FACILITATOR FEEDBACK', a)
p = p[:a] + S5.section5(False) + '\n' + p[b:]
p = once(p, '<script src="/s2r-save.js"></script>', '<script src="/s2r-save.js"></script>\n<script src="/s2r-team.js"></script>')
p = sub1(p, r'var KEYS=\[[^\]]*\]', 'var KEYS=["ref7"]')
p = once(p, '["ref7","app_commit"].forEach(hydrateField);\n    hydrateScenario();\n    hydrateThermo();\n    loadSubmissionFeedback();', '["ref7"].forEach(hydrateField);\n    loadSubmissionFeedback();\n    u11S5Start(responses);')
a = p.rfind('\n', 0, p.index('MICRO-CLIMB SUMMARY (locked arc summaries')) + 1
z = p.index('\n}\n', p.index('function renderSummaryP(){')) + 3
p = p[:a] + p[z:]
p = once(p, 'renderSummaryP();\n', '')
p = once(p, '/* \u2500\u2500 Init \u2500\u2500 */', S5.js() + '\n/* \u2500\u2500 Init \u2500\u2500 */')
assert 'summaryP' not in p and 'var SUMMARY' not in p

# ---- facilitator
f = common(read(f_in), True)
f = once(f, '<p>Orientation, facilitation questions, tone guidance, and session timing for the full unit.</p>', '<p>Unit intent, learning journey and facilitation emphasis for the full unit.</p>')
a = f.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>')
b = f.index('<div class="mod-nav"><button class="btn" onclick="showMod(1)">Section 1', a)
f = f[:a] + C.guide() + f[b:]
f = sub1(f, HERO_OLD, HERO_NEW)
a = f.index('<div class="slo-box">', f.index('id="mod1"'))
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(0)">', a)
f = f[:a] + C.section1(True) + f[b:]

# ---- facilitator Section 2
m = f.index('id="mod2"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S2.TITLE, S2.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(1)">', a)
f = f[:a] + S2.section2(True) + f[b:]

# ---- facilitator Section 3
m = f.index('id="mod3"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S3.TITLE, S3.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(2)">', a)
f = f[:a] + S3.section3(True) + f[b:]

# ---- facilitator Section 4
m = f.index('id="mod4"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S4.TITLE, S4.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(3)">', a)
f = f[:a] + S4.section4(True) + f[b:]

# ---- facilitator Section 5; Unit Summary removed (as Unit 10)
m = f.index('id="mod5"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S5.TITLE, S5.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(4)">', a)
f = f[:a] + S5.section5(True) + f[b:]
assert 'Unit 11 synthesis' not in f

for t in (p, f):
    vis = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>', ' ', t)
    assert not re.search(r'\blens\b', vis, re.I), 'lens in visible text'
os.makedirs(out, exist_ok=True)
write(os.path.join(out, 'unit4_m1_lens10_p.html'), p)
write(os.path.join(out, 'unit4_m1_lens10_f.html'), f)
print('built', out)
