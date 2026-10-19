# -*- coding: utf-8 -*-
"""Carol's capability learning outcomes (19 Oct 2026, her document CESI_Units_2_to_9_Capability_Learning_Outcomes.docx).
Replaces every Key and section learning outcome of Units 2-9 on both pages and in the decks (slides and notes), in place.
Usage: python3 -B apply_outcomes.py <portal folder>"""
import json, re, glob, os, sys, html
from pptx import Presentation
from pptx.oxml.ns import qn
R = sys.argv[1]
P = json.load(open(os.path.join(R, 'Unit decks/_build/consistency_19oct/outcomes_locked_19oct.json'), encoding='utf-8'))
F = {2:'unit2_m1_lens1',3:'unit2_m1_lens2',4:'unit2_m1_lens3',5:'unit3_m1_lens4',6:'unit3_m1_lens5',7:'unit3_m1_lens6',8:'unit3_m2_lens7',9:'unit3_m2_lens8'}
ENT = [('&', '&amp;'), ('’', '&rsquo;'), ('—', '&mdash;'), ('–', '&ndash;'), ('·', '&middot;')]
def variants(s):
    v = {s}; e = s
    for a, b in ENT[1:]: e = e.replace(a, b)
    v.add(e); v.add(e.replace('&', '&amp;') if '&' in s and '&amp;' not in e else e)
    return v
log = []
for u, f in F.items():
    pairs = sorted([p for p in P if p['unit'] == u], key=lambda p: -len(p['now']))
    for s in 'pf':
        fn = os.path.join(R, f'{f}_{s}.html'); raw = open(fn, 'rb').read(); crlf = b'\r\n' in raw
        t = raw.decode('utf-8').replace('\r\n', '\n'); toks = []
        for p in pairs:
            n = 0
            for v in variants(p['now']):
                c = t.count(v)
                if c: toks.append(p['new']); t = t.replace(v, '\x00%d\x00' % (len(toks) - 1)); n += c
            assert n >= 1, (u, s, p['key'])
            log.append((u, s, p['key'], n))
        t = re.sub('\x00(\\d+)\x00', lambda m: toks[int(m.group(1))], t)
        open(fn, 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
    dk = glob.glob(os.path.join(R, 'Unit decks', f'Unit {u:02d}*.pptx'))[0]; prs = Presentation(dk); cnt = {p['key']: 0 for p in pairs}
    for sl in prs.slides:
        roots = [sl.shapes._spTree] + ([sl.notes_slide.notes_text_frame._txBody] if sl.has_notes_slide else [])
        for root in roots:
            for para in root.iter(qn('a:p')):
                runs = list(para.iter(qn('a:t'))); full = ''.join(r.text or '' for r in runs)
                new = full
                for p in pairs:
                    if p['now'] in new: new = new.replace(p['now'], p['new']); cnt[p['key']] += 1
                if new != full:
                    hit = [r for r in runs if any(p['now'] in (r.text or '') for p in pairs)]
                    if len(hit) == 1 and ''.join(r.text or '' for r in runs).count(hit[0].text) == 1 and new == full.replace(hit[0].text, [p['new'] for p in pairs if p['now'] in hit[0].text][0] if False else hit[0].text):
                        pass
                    # put the whole paragraph text in the first run that carries text, keep its formatting
                    runs[0].text = new
                    for r in runs[1:]: r.text = ''
    assert all(v >= 1 for v in cnt.values()), (u, [k for k, v in cnt.items() if v == 0])
    prs.save(dk); log.append((u, 'deck', sum(cnt.values())))
print('\n'.join(str(x) for x in log if x[1] == 'deck'))
print('page replacements:', sum(x[3] for x in log if x[1] in 'pf'))
