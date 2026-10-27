# -*- coding: utf-8 -*-
"""Unit 10 rework, applied section by section on the live pages.
Usage: python3 -B build_u10.py <participant in> <facilitator in> <out folder>
Pages are CRLF: normalised to \\n here, CRLF restored on write."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u10_content as C
import u10_s2 as S2
import u10_s3 as S3
import u10_s4 as S4
import u10_s5 as S5
p_in, f_in, out = sys.argv[1:4]
def read(x): return open(x, 'rb').read().decode('utf-8').replace('\r\n', '\n')
def write(x, t): open(x, 'wb').write(t.replace('\n', '\r\n').encode('utf-8'))
def sub1(t, pat, rep, flags=re.S):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=flags); assert n == 1, 'no match: ' + pat[:80]; return t2
def once(t, a, b):
    assert t.count(a) == 1, 'expected once: ' + a[:80]; return t.replace(a, b)

def common(t, fac):
    # header: Grounding text, Module learning outcomes, Key learning outcomes
    t = sub1(t, r'    <div class="unit-sub">Grounding</div>\n.*?<div class="klo-bar">.*?</div>', C.header())
    # CSS for the domain tables
    i = t.index('</style>'); t = t[:i] + C.css(fac) + S2.css(fac) + S3.css(fac) + S4.css(fac) + S5.css(fac) + __import__('u10_s1b').CSS + t[i:]
    return t

# ---- participant
p = common(read(p_in), False)
p = sub1(p, r'<h2>What is ESRG Alignment\?</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (C.S1_TITLE, C.HERO_P))
a = p.index('<div class="slo-box">', p.index('id="mod0"'))
b = p.index('<div class="mod-nav"><button class="btn" onclick="showMod(1,null)">', a)
p = p[:a] + C.section1(False) + p[b:]
p = once(p, '"team_name","exec_role","ref1","ref2","ref3"', '"team_name","exec_role"')
assert 'id="ref1"' not in p and 'id="ref2"' not in p

# ---- participant Section 2
p = sub1(p, r'<h2>Why ESRG Alignment Drives Sustained Execution</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S2.TITLE, S2.HERO_P))
a = p.index('<div class="slo-box">', p.index('id="mod1"'))
b = p.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(0,null)">', a)
p = p[:a] + S2.section2(False) + p[b:]

# ---- participant Section 3
m = p.index('id="mod2"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (S3.TITLE, S3.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(1,null)">', a)
p = p[:a] + S3.section3(False) + p[b:]
p = once(p, '"team_name","exec_role","ref4","ref5","ref6","ref7","ref8"', '"team_name","exec_role","bias_e","bias_s","bias_r","bias_g"')
p = once(p, '["coc1","coc2","coc3","app_commit"].forEach(hydrateField);', '["coc1","coc2","coc3","app_commit","bias_e","bias_s","bias_r","bias_g"].forEach(hydrateField);')
p = once(p, '/* \\u2500\\u2500 Init \\u2500\\u2500 */', S3.JS + '/* \\u2500\\u2500 Init \\u2500\\u2500 */')

# ---- participant Section 4
m = p.index('id="mod3"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (S4.TITLE, S4.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(2,null)">', a)
p = p[:a] + S4.section4(False) + p[b:]
p = sub1(p, r'var KEYS=\[[^\]]*\]', 'var KEYS=["bias_e","bias_s","bias_r","bias_g","esrg_scan_head","esrg_scan","coc_valueset","coc1","coc2","coc3","app_commit"]')
p = once(p, '"bias_e","bias_s","bias_r","bias_g"].forEach(hydrateField);', '"bias_e","bias_s","bias_r","bias_g","esrg_scan"].forEach(hydrateField);u10Profile();u10LoadRoles();')
p = once(p, '/* \\u2500\\u2500 Init \\u2500\\u2500 */', S4.JS + '/* \\u2500\\u2500 Init \\u2500\\u2500 */')

# ---- participant Section 5 (group Capstone work on the shared group record)
m = p.index('id="mod4"')
p = p[:m] + sub1(p[m:], r'<h2>[^<]*</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (S5.TITLE, S5.HERO))
a = p.index('<div class="slo-box">', m)
b = p.index('<!-- MICRO-CLIMB SUMMARY (standard #summaryP) -->', a)
p = p[:a] + S5.section5(False) + '\n' + p[b:]
p = once(p, '<script src="/s2r-save.js"></script>', '<script src="/s2r-save.js"></script>\n<script src="/s2r-team.js"></script>')
p = sub1(p, r'var KEYS=\[[^\]]*\]', 'var KEYS=["bias_e","bias_s","bias_r","bias_g","esrg_scan_head","esrg_scan"]')
p = sub1(p, r'\["coc1","coc2","coc3","app_commit",("bias_e".*?)\]\.forEach\(hydrateField\);u10Profile\(\);u10LoadRoles\(\);\n\s*\["coc1","coc2","coc3"\]\.forEach\(cocRevealIfFilled\);\n\s*hydrateValueSet\(\);',
         '["bias_e","bias_s","bias_r","bias_g","esrg_scan"].forEach(hydrateField);u10LoadRoles();\n    u10S5Start(responses);')
p = once(p, '/* \\u2500\\u2500 Init \\u2500\\u2500 */', S5.JS + '/* \\u2500\\u2500 Init \\u2500\\u2500 */')

# ---- facilitator
f = common(read(f_in), True)
f = once(f, '<p>Orientation, facilitation questions, tone guidance, and watch points for the full unit.</p>', '<p>Orientation, key facilitation questions and pacing for the full unit.</p>')
a = f.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>')
b = f.index('<div class="mod-nav"><button class="btn" onclick="showMod(1)">Section 1', a)
f = f[:a] + C.guide() + f[b:]
f = sub1(f, r'<h2>What is ESRG Alignment\?</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (C.S1_TITLE, C.HERO_P))
a = f.index('<div class="slo-box">', f.index('id="mod1"'))
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(0)">', a)
f = f[:a] + C.section1(True) + f[b:]

# ---- facilitator Section 2
f = sub1(f, r'<h2>Why ESRG Alignment Drives Sustained Execution</h2><p>.*?</p>', '<h2>%s</h2><p>%s</p>' % (S2.TITLE, S2.HERO_F))
a = f.index('<div class="slo-box">', f.index('id="mod2"'))
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(1)">', a)
f = f[:a] + S2.section2(True) + f[b:]

# ---- facilitator Section 3
m = f.index('id="mod3"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (S3.TITLE, S3.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(2)">', a)
f = f[:a] + S3.section3(True) + f[b:]

# ---- facilitator Section 4
m = f.index('id="mod4"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (S4.TITLE, S4.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<div class="mod-nav"><button class="btn prev" onclick="showMod(3)">', a)
f = f[:a] + S4.section4(True) + f[b:]

# ---- facilitator Section 5
m = f.index('id="mod5"')
f = f[:m] + sub1(f[m:], r'<h2>[^<]*</h2><p>[^<]*</p>', '<h2>%s</h2><p>%s</p>' % (S5.TITLE, S5.HERO))
a = f.index('<div class="slo-box">', m)
b = f.index('<!-- MICRO-CLIMB SUMMARY -->', a)
f = f[:a] + S5.section5(True) + '\n' + f[b:]

# ---- Unit Summary removed from both pages (Carol, 27 Oct 18:44)
a = p.index('<!-- MICRO-CLIMB SUMMARY (standard #summaryP) -->'); z = p.index('<!-- C1: FACILITATOR FEEDBACK', a)
p = p[:a] + p[z:]
a = p.index('/* \\u2550'); a = p.rfind('\n', 0, p.index('MICRO-CLIMB SUMMARY (locked arc summaries)')) + 1
z = p.index('\n}\n', p.index('function renderSummaryP(){')) + 3
p = p[:a] + p[z:]
p = once(p, 'renderSummaryP();\n', '')
assert 'summaryP' not in p and 'var SUMMARY' not in p
a = f.index('<!-- MICRO-CLIMB SUMMARY -->'); z = f.index('<div class="mod-nav">', a)
f = f[:a] + f[z:]
assert 'Unit 10 synthesis' not in f

for t in (p, f):
    vis = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>', ' ', t)
    assert not re.search(r'\blens\b', vis, re.I), 'lens in visible text'
os.makedirs(out, exist_ok=True)
write(os.path.join(out, 'unit4_m1_lens9_p.html'), p)
write(os.path.join(out, 'unit4_m1_lens9_f.html'), f)
print('built', out)
