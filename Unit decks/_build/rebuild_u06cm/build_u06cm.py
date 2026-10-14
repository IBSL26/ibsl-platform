# -*- coding: utf-8 -*-
"""Unit 6 rework of 14 October 2026 (Carol's "Amended content.docx"): builds both pages from the live pages.
Usage: python3 build_u06cm.py <p before> <f before> <p out> <f out>
Keeps the page shell (header, tabs, lock, save, submit, feedback, messages, documents); replaces the five sections,
the Facilitator Guide, the Unit Summary texts and the Section 5 tool. Every cut checks that it finds its place once."""
import sys, re, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u6cm_content as C

HERE = os.path.dirname(os.path.abspath(__file__))
p_src, f_src, p_out, f_out = sys.argv[1:5]


def rd(x):
    return open(x, 'rb').read().decode('utf-8')


def once(t, s, label=''):
    n = t.count(s)
    assert n == 1, 'expected once (%d): %s %s' % (n, label, s[:90])
    return t.index(s)


def between(t, a, b, new, keep_a=False, keep_b=True):
    i = once(t, a, 'start')
    j = t.index(b, i + len(a))
    return t[:i] + (a if keep_a else '') + new + (b if keep_b else '') + t[j + len(b):] if not keep_b else t[:i] + (a if keep_a else '') + new + t[j:]


def crlf(s):
    return s.replace('\r\n', '\n').replace('\n', '\r\n')


CSS = rd(os.path.join(HERE, 'u6cm.css'))
JS = rd(os.path.join(HERE, 'u6cm_p.js'))

SECTIONS = [  # (label, title, hero_f, hero_p, slo, builder)
    ('Section 1 · Awareness — What', C.S1_TITLE, C.S1_HERO, C.S1_HERO, C.S1_SLO, C.s1),
    ('Section 2 · Intelligence — Why', C.S2_TITLE, C.S2_HERO, C.S2_HERO, C.S2_SLO, C.s2),
    ('Section 3 · Extrapolating — Where', C.S3_TITLE, C.S3_HERO, C.S3_HERO, C.S3_SLO, C.s3),
    ('Section 4 · Integration — Collective', C.S4_TITLE, C.S4_HERO, C.S4_HERO, C.S4_SLO, C.s4),
]


def navs(t, cls):
    return re.findall(r'<div class="mod-nav">.*?</div>', t[:t.index('<div class="mod%s" id="mod%d">' % (cls, 4 if cls == '' else 5))])


# ───────────────────────── participant ─────────────────────────
p = rd(p_src)
assert p.count('\r\n') > 1000
nav_p = re.findall(r'<div class="mod-nav"><button[^\n]*</div>', p)
assert len(nav_p) == 4, nav_p
mods = []
for i, (lab, title, hf, hp, slo, fn) in enumerate(SECTIONS):
    mods.append('<div class="mod%s" id="mod%d">\n<div class="mod-hero"><div class="mod-hero-label">%s</div><h2>%s</h2><p>%s</p></div>\n<div class="mod-body">\n%s\n%s%s\n</div></div>\n'
                % (' active' if i == 0 else '', i, lab, title, hp, C.SLO(slo), '\n'.join(fn('p')), nav_p[i]))
mods.append('<div class="mod" id="mod4">\n<div class="mod-hero"><div class="mod-hero-label">Section 5 · Application — In Practice</div><h2>%s</h2><p>%s</p></div>\n<div class="mod-body">\n%s\n%s\n'
            % (C.S5_TITLE, C.S5_HERO_P, C.SLO(C.S5_SLO), C.s5_p()))
a = '<div class="mod active" id="mod0">'
b = '<div id="u6Rec"></div>\n'
i = once(p, a); j = once(p, '<div id="u6Rec"></div>')
p = p[:i] + crlf(''.join(mods)) + p[j + len('<div id="u6Rec"></div>'):]
# script: Section 5 tool
i = once(p, '/* ════════════ UNIT 6 · SECTION 5 · DESIGNING THE PM ARCHITECTURE')
j = once(p, '/* ── Init ── */')
p = p[:i] + crlf(JS) + '\r\n' + p[j:]
# keys
old = 'var KEYS=["ref1","ref2","ref3","ref4","ref6","ref7","ref11","ref12"];'
once(p, old); p = p.replace(old, 'var KEYS=' + json.dumps(C.REF_ORDER).replace(' ', '') + ';')
old = 'hydrateScores("ref1");u6Init(responses);'
once(p, old); p = p.replace(old, 'u6Init(responses);')
old_sf = re.search(r'var SCORE_FIELDS=\{[\s\S]*?\n\};', p)
assert old_sf
p = p[:old_sf.start()] + 'var SCORE_FIELDS={};' + p[old_sf.end():]
# summary
m = re.search(r'var SUMMARY=\[.*?\];\r\n', p)
assert m
p = p[:m.start()] + 'var SUMMARY=' + json.dumps([{'arc': a_, 'title': t_, 'body': b_} for a_, t_, b_ in C.SUMMARY], ensure_ascii=False) + ';\r\n' + p[m.end():]
# css
k = p.index('</style>')
p = p[:k] + crlf(CSS) + p[k:]
open(p_out, 'wb').write(p.encode('utf-8'))

# ───────────────────────── facilitator ─────────────────────────
f = rd(f_src)
nav_f = re.findall(r'<div class="mod-nav"><button[^\n]*</div>', f)
assert len(nav_f) == 6, len(nav_f)
# Facilitator Guide
a = '<div class="mod-body" style="padding-top:24px;padding-bottom:10px;">\r\n'
i = once(f, a) + len(a)
j = f.index(nav_f[0], i)
f = f[:i] + crlf(C.FGUIDE) + f[j:]
nav_f = re.findall(r'<div class="mod-nav"><button[^\n]*</div>', f)
mods = []
for i_, (lab, title, hf, hp, slo, fn) in enumerate(SECTIONS):
    mods.append('<div class="mod-panel" id="mod%d">\n<div class="mod-hero"><div class="mod-hero-label">%s</div><h2>%s</h2><p>%s</p></div>\n<div class="mod-body">\n%s\n%s%s\n</div></div>\n\n'
                % (i_ + 1, lab, title, hf, C.SLO(slo), '\n'.join(fn('f')), nav_f[i_ + 1]))
mods.append('<div class="mod-panel" id="mod5">\n<div class="mod-hero"><div class="mod-hero-label">Section 5 · Application — In Practice</div><h2>%s</h2><p>%s</p></div>\n<div class="mod-body">\n%s\n%s\n\n'
            % (C.S5_TITLE, C.S5_HERO_F, C.SLO(C.S5_SLO), C.s5_f()))
i = once(f, '<div class="mod-panel" id="mod1">')
j = once(f, '<div class="acc">\r\n<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">Unit Summary</div>')
f = f[:i] + crlf(''.join(mods)) + f[j:]
# Unit Summary cards
cards = re.findall(r'(<div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:[^;]+;margin-bottom:8px;">([^<]+)</div><p style="font-size:13px;color:rgba\(255,255,255,\.65\);line-height:1\.7;">)(.*?)(</p>)', f)
assert len(cards) == 5, len(cards)
bodies = [s[2] for s in C.SUMMARY[:4]] + [C.SUMMARY_F5]
for (pre, arc, body, post), nb in zip(cards, bodies):
    once(f, pre + body + post)
    f = f.replace(pre + body + post, pre + nb + post)
old = re.search(r'Close with one pointed question: <em>“[^”]*”</em>', f)
assert old
f = f[:old.start()] + 'Close with one pointed question: <em>“' + C.CLOSING_Q + '”</em>' + f[old.end():]
cx = JS[JS.index('/* Section 3 · part 3.1.1'):]
gb = "function goBack(){window.location.href='dashboard_F.html';}"
once(f, gb); f = f.replace(gb, gb + '\r\n' + crlf(cx.strip()))
k = f.index('</style>')
f = f[:k] + crlf(CSS) + f[k:]
open(f_out, 'wb').write(f.encode('utf-8'))
print('built', p_out, f_out)
