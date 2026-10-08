# -*- coding: utf-8 -*-
"""Writes the Unit 5 page content the deck needs word for word: Key learning outcomes, section headings and outcomes, part titles and
sub-lines, and the fourteen reflection questions. Usage: python3 export_deck_data.py <participant page> <facilitator page> <u05_data.json>
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
assert len(dp['KLO']) == 4 and len(dp['SECTIONS']) == 5 and len(dp['PARTS']) == 14 and len(dp['STEPS']) == 3
refl = {}
for m in re.finditer(r'<div class="ref-block"[^>]*><div class="ref-label">(.*?)</div>\s*<label class="wp-label"[^>]*for="(ref\d+)">(.*?)</label>', p):
    part = max(dp['PARTS'], key=lambda j: p.rfind('<span class="acc-t">' + j + ' &mdash;', 0, m.start()))
    refl[part] = dict(id=m.group(2), label=clean(m.group(1)).replace('✎ ', ''), prompt=clean(m.group(3)))
assert len(refl) == 14, len(refl)
dp['REFL'] = refl
m = re.search(r'Close with one pointed question: <em>&ldquo;(.*?)&rdquo;</em>', f); dp['CLOSING_Q'] = clean(m.group(1))
# The amended content both pages are built from (u5b_content.py), for the slides and notes of 3.1, 4.2 and Section 5.
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u5b_content as B
un = lambda t: html.unescape(t)
dp['OCEAVL'] = B.OCEAVL
dp['CHECKS'] = B.CHECKS
dp['KIT'] = [dict(id=k[0], c=k[1], n=k[2], cues=[k[3], k[4]], trig=k[5]) for k in B.KIT]
dp['KIT_EXAMPLE'] = [list(r) for r in B.KIT_EXAMPLE]
dp['HOT'] = [dict(role=h[0], el=h[1], tag=un(B.hot_tag(n)), f=h[3]) for n, h in enumerate(B.HOT)]
dp['CHAIN'] = [list(c) for c in B.CHAIN]; dp['CHAIN_QUOTE'] = B.CHAIN_QUOTE
for k in dp['KIT']:
    for t in k['cues'] + [k['trig']]: assert un(t) in html.unescape(re.sub(r'<[^>]+>', ' ', p)), t
json.dump(dp, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', OUT, '· parts', len(dp['PARTS']), '· reflections', len(refl))
