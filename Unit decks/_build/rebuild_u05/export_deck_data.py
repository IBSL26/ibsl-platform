# -*- coding: utf-8 -*-
"""Writes the Unit 5 page content the deck needs word for word: Key learning outcomes, section headings and outcomes, part titles and
sub-lines, and the thirteen reflection questions (pages as amended on 9 October 2026). Usage: python3 export_deck_data.py <participant page> <facilitator page> <u05_data.json>
The two pages must agree on every item or the script stops."""
import sys, re, json, html
P, F, OUT = sys.argv[1:4]
def clean(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
def read(p): return open(p, encoding='utf-8').read().replace('\r\n', '\n')
def grab(t):
    d = {}
    d['KLO'] = [clean(x) for x in re.findall(r'<span class="klo">(.*?)</span>', t)]
    d['SECTIONS'] = []
    for m in re.finditer(r'<div class="mod-hero-label">(Section (\d) · (\S+) — ([^<]+))</div>\s*<h2>(.*?)</h2>', t):
        a = t.index('<div class="slo-box">', m.end()); b = t.index('</ul>', a)
        d['SECTIONS'].append(dict(num=int(m.group(2)), name=m.group(3), anchor=m.group(4).strip(), heading=clean(m.group(5)), outcomes=[clean(x) for x in re.findall(r'<li>(.*?)</li>', t[a:b])]))
    titles = [clean(x) for x in re.findall(r'<span class="acc-t">(.*?)</span>', t)]
    metas = [clean(x) for x in re.findall(r'<span class="acc-meta">(.*?)</span>', t)]
    d['PARTS'] = {x.split(' — ')[0]: dict(title=x.split(' — ', 1)[1], meta=metas[i]) for i, x in enumerate(titles) if re.match(r'\d\.\d(\.\d)? — ', x)}
    d['STEPS'] = [clean(x) for x in re.findall(r'<div class="step-name">(.*?)</div>', t)]
    return d
p, f = read(P), read(F)
dp, df = grab(p), grab(f)
assert dp == df, [k for k in dp if dp[k] != df[k]]
assert len(dp['KLO']) == 4 and len(dp['SECTIONS']) == 5 and len(dp['PARTS']) == 13 and len(dp['STEPS']) == 2, (len(dp['PARTS']), dp['STEPS'])
refl = {}
for m in re.finditer(r'<div class="ref-block"[^>]*><div class="ref-label">(.*?)</div>\s*<label class="wp-label"[^>]*for="(ref\d+)">(.*?)</label>', p):
    part = max(dp['PARTS'], key=lambda j: p.rfind('<span class="acc-t">' + j + ' &mdash;', 0, m.start()))
    refl[part] = dict(id=m.group(2), label=clean(m.group(1)).replace('✎ ', ''), prompt=clean(m.group(3)))
assert len(refl) == 13, len(refl)
dp['REFL'] = refl
m = re.search(r'Close with one pointed question: <em>&ldquo;(.*?)&rdquo;</em>', f); dp['CLOSING_Q'] = clean(m.group(1))
# The content both pages are built from (u5b_content.py, u5c_content.py, u5d_content.py), for the slides and notes of 3.1, Section 4 and Section 5.
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u5b_content as B
import u5c_content as D
import u5d_content as E
un = lambda t: html.unescape(re.sub(r'<[^>]+>', '', t))
vis_p, vis_f = (html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>', ' ', x, flags=re.S))) for x in (p, f))
def on(page, t):
    assert re.sub(r'\s+', ' ', un(t)) in re.sub(r'\s+', ' ', page), 'not on the page: ' + un(t)[:90]
    return un(t)
dp['OCEAVL'] = D.OCEAVL2
dp['OC_STEPS_F'] = [on(vis_f, x) for x in D.OC_STEPS_F]; dp['OC_STEPS_P'] = [on(vis_p, x) for x in D.OC_STEPS_P]; dp['OC_EVERY'] = D.OC_EVERY
_K = {k[0]: k for k in B.KIT}
dp['HOT'] = [dict(role=h[0], el=h[1], tag=un(D.hot_tag2(n)), need=on(vis_f, D.NEED[h[1]]), why=on(vis_f, h[3]),
                  trig=on(vis_f, D.STORY[h[1]][0]), cues=on(vis_f, D.STORY[h[1]][1]), cost=on(vis_f, D.STORY[h[1]][2])) for n, h in enumerate(D.HOT2)]
dp['TERMS'] = dict(teach=on(vis_f, D.TEACH_F), czc=on(vis_f, D.CZC_F), ahz=on(vis_f, D.AHZ_F), why=on(vis_f, D.WHY_F).replace('Why the two are shown together. ', '', 1),
                   lines=[on(vis_f, x) for x in D.HOT_LINES_F], close=on(vis_f, D.READ_CLOSE_F), one=on(vis_f, D.ONE_P),
                   czc_p=on(vis_p, D.CZC_P), ahz_p=on(vis_p, D.AHZ_P))
dp['G3'] = [{k: un(v) for k, v in g.items()} for g in E.guide_3s(f)]
dp['GA'] = [{k: un(v) for k, v in g.items()} for g in E.guide_ace(f)]
dp['ASK'] = {k: on(vis_p, v) for k, v in E.ASK.items()}; dp['ACE_ASK'] = on(vis_p, E.ACE_ASK)
dp['STEP1_ACT_F'] = [on(vis_f, x) for x in E.STEP1_ACT_F]; dp['STEP2_ACT_F'] = [on(vis_f, x) for x in E.STEP2_ACT_F]
dp['STEP1_GUIDE_F'] = [on(vis_f, x) for x in E.STEP1_GUIDE_F]; dp['STEP2_GUIDE_F'] = [on(vis_f, x) for x in E.STEP2_GUIDE_F]
dp['CHAIN'] = [list(c) for c in B.CHAIN]; dp['CHAIN_QUOTE'] = B.CHAIN_QUOTE
json.dump(dp, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', OUT, '· parts', len(dp['PARTS']), '· reflections', len(refl))
