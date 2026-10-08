# -*- coding: utf-8 -*-
"""Writes the Unit 5 page content the deck needs word for word: Key learning outcomes, section headings and outcomes, part titles and
sub-lines, and the fifteen reflection questions. Usage: python3 export_deck_data.py <participant page> <facilitator page> <u05_data.json>
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
    d['PARTS'] = {x.split(' — ')[0]: dict(title=x.split(' — ', 1)[1], meta=metas[i]) for i, x in enumerate(titles) if re.match(r'\d\.\d — ', x)}
    d['STEPS'] = [clean(x) for x in re.findall(r'<div class="step-name">(.*?)</div>', t)]
    return d
p, f = read(P), read(F)
dp, df = grab(p), grab(f)
assert dp == df, [k for k in dp if dp[k] != df[k]]
assert len(dp['KLO']) == 4 and len(dp['SECTIONS']) == 5 and len(dp['PARTS']) == 16 and len(dp['STEPS']) == 4
refl = {}
for m in re.finditer(r'<div class="ref-block"[^>]*><div class="ref-label">(.*?)</div>\s*<label class="wp-label"[^>]*for="(ref\d+)">(.*?)</label>', p):
    part = max(dp['PARTS'], key=lambda j: p.rfind('<span class="acc-t">' + j + ' &mdash;', 0, m.start()))
    refl[part] = dict(id=m.group(2), label=clean(m.group(1)).replace('✎ ', ''), prompt=clean(m.group(3)))
assert len(refl) == 15, len(refl)
dp['REFL'] = refl
m = re.search(r'Close with one pointed question: <em>&ldquo;(.*?)&rdquo;</em>', f); dp['CLOSING_Q'] = clean(m.group(1))
json.dump(dp, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', OUT, '· parts', len(dp['PARTS']), '· reflections', len(refl))
