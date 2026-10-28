# -*- coding: utf-8 -*-
"""Units 2, 3 and 4 (12 October 2026, Carol): the Capstone section becomes the last section.
Section 4 (Integration — Collective) and Section 5 (Application — In Practice) change places.
The content of each section moves as it is; the place keeps its label: the 4th section is "Section 4 · Integration — Collective",
the 5th "Section 5 · Application — In Practice". Every number that names a section or part of this unit (4.x and 5.x) changes with its content.
The Unit Summary, the submission cluster and Submit to Facilitator stay at the end of the last section.
Usage: python3 swap45.py <page in> <page out> <log out>"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blocks import children, mods

A_LABEL = {'4': ('Integration', 'Collective'), '5': ('Application', 'In Practice')}

def swap_numbers(s, log=None, where=''):
    """Swap every 4.x <-> 5.x and Section 4 <-> Section 5 in a piece of text, with the arc names that go with them."""
    P = []
    def keep(x):
        P.append(x); return '\x00%d\x00' % (len(P) - 1)
    # whole labels first: the arc name travels with the number
    for sep in (' · ', ' &middot; ', ' — ', ' &mdash; ', ' – ', ': '):
        for up in (False, True):
            a4 = 'Section 4' + sep + 'Integration'; a5 = 'Section 5' + sep + 'Application'
            if up: a4, a5 = a4.upper(), a5.upper()
            for tail4, tail5 in ((sep_t + 'Collective', sep_t + 'In Practice') for sep_t in (' — ', ' &mdash; ', ' · ', ' &middot; ', ' – ')):
                if up: tail4, tail5 = tail4.upper(), tail5.upper()
                s = s.replace(a4 + tail4, keep(a5 + tail5)).replace(a5 + tail5, keep(a4 + tail4))
            s = s.replace(a4, keep(a5)).replace(a5, keep(a4))
    def sec(m):
        n = m.group(2); return keep(m.group(1) + ('5' if n == '4' else '4'))
    s = re.sub(r'((?:Section|SECTION|section|Sections|Part|PART|part|parts)\s+)([45])(?![\d])', sec, s)
    s = re.sub(r'((?:Sections|sections) [1-3] and )([45])(?!\d)', sec, s)
    def part(m):
        return keep(('5' if m.group(1) == '4' else '4') + '.' + m.group(2))
    s = re.sub(r'(?<![\w.,/#&;:\-])([45])\.(\d{1,2})(?![\d%]|px|em|rem|vh|vw|deg|s\b)', part, s)
    while '\x00' in s:
        s = re.sub(r'\x00(\d+)\x00', lambda m: P[int(m.group(1))], s)
    return s

def masked_apply(t, fn):
    """Apply fn to t outside <style>, <svg>, style="...", data: URIs, the section tab strip, the mod-nav bars and the arc words of SUMMARY."""
    keep = []
    def k(m): keep.append(m.group(0)); return '\x01%d\x01' % (len(keep) - 1)
    pats = [r'<style\b.*?</style>', r'<svg\b.*?</svg>', r'\sstyle="[^"]*"', r'data:[a-z]+/[^"\')\s]+',
            r'<div class="mod-tab[^"]*"[^>]*>.*?</div>', r'<button class="tab-btn[^"]*"[^>]*>.*?</button>',
            r'<div class="mod-nav">.*?</div>', r'<div class="tab-btn[^"]*"[^>]*>.*?</div>']
    for p in pats: t = re.sub(p, k, t, flags=re.S)
    t = fn(t)
    while '\x01' in t:
        t = re.sub(r'\x01(\d+)\x01', lambda m: keep[int(m.group(1))], t)
    return t

def section_parts(t, start):
    """For one section block: (hero span, list of content child spans, tail start or None, nav span)."""
    end, kids = children(t, start)
    hero = [x for x in kids if 'mod-hero' in t[x[0]:x[0] + 60]][0]
    body = [x for x in kids if 'mod-body' in t[x[0]:x[0] + 60]][0]
    _, bk = children(t, body[0])
    nav = [x for x in bk if t.startswith('<div class="mod-nav"', x[0])]
    assert len(nav) == 1, 'mod-nav'
    nav = nav[0]
    content = [x for x in bk if x[1] <= nav[0]]
    tail = None
    for i, x in enumerate(content):
        if re.match(r'<div class="acc"[^>]*>\s*<div class="acc-h"[^>]*>\s*<span class="acc-t">Unit Summary<', t[x[0]:x[0] + 300]):
            j = i - 1 if (i > 0 and t[content[i - 1][0]:content[i - 1][0] + 4] == '<!--') else i
            tail = content[j][0]; content = content[:j]; break
    return hero, content, tail, nav

def swap_page(t, ia, log):
    ms = mods(t)
    (sa, ida), (sb, idb) = ms[ia], ms[ia + 1]
    ha, ca, ta, na = section_parts(t, sa)
    hb, cb, tb, nb = section_parts(t, sb)
    assert ta is None, 'tail in the 4th section'
    hero_a, hero_b = t[ha[0]:ha[1]], t[hb[0]:hb[1]]
    cont_a = t[ca[0][0]:ca[-1][1]]; cont_b = t[cb[0][0]:cb[-1][1]]
    # rebuild: 4th place gets B, 5th place gets A
    new = (t[:ha[0]] + hero_b + t[ha[1]:ca[0][0]] + cont_b + t[ca[-1][1]:hb[0]] +
           hero_a + t[hb[1]:cb[0][0]] + cont_a + t[cb[-1][1]:])
    log.append('moved: 4th place now holds %d chars of the old Section 5; 5th place %d chars of the old Section 4; tail kept at the end: %s' % (len(cont_b), len(cont_a), tb is not None))
    return new

def swap_summary(t, log):
    """Unit Summary blocks: the arc word stays with the place, the text moves with its section."""
    for q in ('"', "'"):
        rx = re.compile(r'(\{\s*%(q)sarc%(q)s\s*:\s*%(q)s)(Integration — Collective)(%(q)s\s*,)(.*?)(\}\s*,\s*\{\s*%(q)sarc%(q)s\s*:\s*%(q)s)(Application — In Practice)(%(q)s\s*,)(.*?)(\})' % {'q': q}, re.S)
        rx2 = re.compile(r'(\{\s*arc\s*:\s*%(q)s)(Integration — Collective)(%(q)s\s*,)(.*?)(\}\s*,\s*\{\s*arc\s*:\s*%(q)s)(Application — In Practice)(%(q)s\s*,)(.*?)(\})' % {'q': q}, re.S)
        for r in (rx, rx2):
            m = r.search(t)
            if m:
                g = m.groups()
                t = t[:m.start()] + g[0] + g[1] + g[2] + g[7] + g[4] + g[5] + g[6] + g[3] + g[8] + t[m.end():]
                log.append('summary: the two blocks changed texts')
    return t

if __name__ == '__main__':
    src, out, logf = sys.argv[1:4]
    raw = open(src, 'rb').read(); t = raw.decode('utf-8'); crlf = b'\r\n' in raw
    t = t.replace('\r\n', '\n')
    ms = mods(t)
    ia = [i for i, (s, mid) in enumerate(ms) if re.search(r'Section 4 (·|&middot;) Integration', t[s:s + 600])]
    assert len(ia) == 1, ia
    log = []
    before = t
    t = masked_apply(t, lambda x: swap_numbers(x))
    # report every changed word, with its context (before the sections move)
    import difflib
    ta = re.split(r'(\s+|<[^>]+>)', before); tb = re.split(r'(\s+|<[^>]+>)', t)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            ctx = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', ''.join(ta[max(0, i1 - 30):i1])))[-90:]
            post = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', ''.join(ta[i2:i2 + 20])))[:60]
            log.append('%s [%s => %s] %s' % (ctx, ''.join(ta[i1:i2]), ''.join(tb[j1:j2]), post))
    t = swap_summary(t, log)
    t = swap_page(t, ia[0], log)
    open(out, 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
    open(logf, 'w', encoding='utf-8').write('\n'.join(log))
    print(src, '->', out, len(log), 'log lines')
