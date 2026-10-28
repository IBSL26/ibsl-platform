# -*- coding: utf-8 -*-
"""Hygiene of 12 October 2026 (Carol), the decks. Works on Carol's own decks in Unit decks.
Units 3 and 4 (Unit 2 keeps its order): the Section 4 slides and the Section 5 slides change places, as on the pages. The section slide of each place keeps
its number and arc ("4 · Section 4 · Integration — Collective", "5 · Section 5 · Application — In Practice"); every slide title and note
that names a part of this unit (4.x, 5.x, Section 4, Section 5) changes with its content. The unit journey slide keeps its five lines;
its notes list the sections in the new order. Unit 2: the reflection picture of the moved section is taken again from the new page.
Units 6 and 7: the notes that point to "Unit 3, part 4.2" now say 5.2.
Usage: python3 hygiene_decks.py <Unit decks folder> <out folder> <Unit 2 reflection picture or ->"""
import sys, os, re, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from swap45 import swap_numbers
from pptx import Presentation
src, out, pic2 = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
LOG = []

def map_frame(tf, fn, where):
    for p in tf.paragraphs:
        old = ''.join(r.text for r in p.runs)
        new = fn(old)
        if new == old: continue
        for r in p.runs: r.text = fn(r.text)
        if ''.join(r.text for r in p.runs) != new:            # a number split over two runs: whole text into the first run
            p.runs[0].text = new
            for r in p.runs[1:]: r.text = ''
            LOG.append('   joined runs at %s: %s' % (where, new[:70]))

def texts(s): return [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]

def order_lists(notes):
    """In a note, lines that list the sections in order ("- Section 5 · …" then "- Section 4 · …") are put back in order."""
    lines = notes.split('\n')
    for i in range(len(lines) - 1):
        a, b = lines[i], lines[i + 1]
        if re.match(r'^(- )?Section 5 (·|—)', a) and re.match(r'^(- )?Section 4 (·|—)', b):
            lines[i], lines[i + 1] = b, a
    return '\n'.join(lines)

def set_notes_text(s, text):
    tf = s.notes_slide.notes_text_frame
    paras = text.split('\n')
    # keep runs: the notes of these decks hold one paragraph per line
    if len(tf.paragraphs) == len(paras):
        for p, t in zip(tf.paragraphs, paras):
            if ''.join(r.text for r in p.runs) != t:
                if p.runs:
                    p.runs[0].text = t
                    for r in p.runs[1:]: r.text = ''
                else:
                    p.text = t
    else:
        raise SystemExit('notes paragraphs differ')

def swap_deck(name, unit):
    prs = Presentation(os.path.join(src, name)); S = list(prs.slides)
    div = {}
    for i, s in enumerate(S):
        t = [sh.text_frame.text.strip() for sh in texts(s)]
        if len(t) > 2 and t[0] in ('4', '5') and t[1] == 'Section ' + t[0]: div[t[0]] = i
    d4, d5 = div['4'], div['5']
    end = len(S) - 1
    assert 'Unit Summary' in texts(S[end])[0].text_frame.text, name
    assert d4 < d5 < end
    journey = 2
    assert texts(S[journey])[0].text_frame.text == 'The unit journey'
    # 1 · text of every slide and note, except the five fixed lines of the journey slide
    for i, s in enumerate(S):
        if i != journey:
            for sh in texts(s): map_frame(sh.text_frame, swap_numbers, '%s slide %d' % (name, i + 1))
        if s.has_notes_slide and i == journey:
            nt = s.notes_slide.notes_text_frame
            r4 = [r for q in nt.paragraphs for r in q.runs if '— Collective:' in r.text]
            r5 = [r for q in nt.paragraphs for r in q.runs if '— In Practice:' in r.text]
            assert len(r4) == 1 and len(r5) == 1, (name, len(r4), len(r5))
            h4, d4_ = r4[0].text.split('— Collective:', 1); h5, d5_ = r5[0].text.split('— In Practice:', 1)
            skip = {id(r4[0]), id(r5[0])}
            for q in nt.paragraphs:
                for r in q.runs:
                    if r is not r4[0] and r is not r5[0] and r.text != swap_numbers(r.text) and not re.search(r'Section [45] · (Integration|Application) $', r.text):
                        r.text = swap_numbers(r.text)
            r4[0].text = h4 + '— Collective:' + swap_numbers(d5_); r5[0].text = h5 + '— In Practice:' + swap_numbers(d4_)
            LOG.append('   %s: journey notes: the two section lines keep their place, their descriptions changed places' % name)
        elif s.has_notes_slide:
            nt = s.notes_slide.notes_text_frame
            map_frame(nt, lambda x: order_lists(swap_numbers(x)), '%s notes %d' % (name, i + 1))
            ps = nt.paragraphs
            for k in range(len(ps) - 1):       # a list written one paragraph per line
                a_, b_ = ps[k].text, ps[k + 1].text
                if re.match(r'^(- )?Section 5 (·|—)', a_) and re.match(r'^(- )?Section 4 (·|—)', b_):
                    e1, e2 = ps[k]._p, ps[k + 1]._p; e1.addprevious(e2); ps = nt.paragraphs
    # 2 · the section slides keep the number and arc of their place
    for i, n in ((d4, '5'), (d5, '4')):            # d4 moves to place 5, d5 to place 4
        sh = texts(S[i])
        sh[0].text_frame.paragraphs[0].runs[0].text = n
        assert sh[1].text_frame.text == 'Section ' + n, sh[1].text_frame.text
        sh[2].text_frame.paragraphs[0].runs[0].text = 'Integration — Collective' if n == '4' else 'Application — In Practice'
    # 3 · reflection slides of the moved sections: their part label follows the section
    for i in range(d4, end):
        t = texts(S[i])
        if t and re.match(r'Section [45] Reflections$', t[0].text_frame.text):
            for sh in t[1:]:
                if sh.text_frame.text.strip() in ('4', '5'):
                    r = sh.text_frame.paragraphs[0].runs[0]; r.text = '5' if r.text.strip() == '4' else '4'
            if unit == 2 and pic2 != '-':
                pics = [p for p in S[i].shapes if p.shape_type == 13]
                assert len(pics) == 1, len(pics)
                old = pics[0]; name_p = old.name.replace('5.2', '4.2'); left, top, width = old.left, old.top, old.width
                el = old._element; pos = list(S[i].shapes._spTree).index(el); S[i].shapes._spTree.remove(el)
                new = S[i].shapes.add_picture(pic2, left, top, width=width); new.name = name_p
                S[i].shapes._spTree.remove(new._element); S[i].shapes._spTree.insert(pos, new._element)
                LOG.append('   %s: reflection picture taken again from the new page (%s)' % (name, name_p))
    # 4 · the slides change places
    lst = prs.slides._sldIdLst; ids = list(lst)
    order = ids[:d4] + ids[d5:end] + ids[d4:d5] + ids[end:]
    for e in ids: lst.remove(e)
    for e in order: lst.append(e)
    prs.save(os.path.join(out, name))
    LOG.append('%s: Section 4 slides %d-%d and Section 5 slides %d-%d changed places' % (name, d4 + 1, d5, d5 + 1, end))

# Unit 2 keeps its order (Carol, 12 October 10:38).
swap_deck('Unit 03 - SiP KISS Mapping & OKR Definition.pptx', 3)
swap_deck('Unit 04 - Direction Integrity (ABCV-MBT).pptx', 4)

for name in ('Unit 06 - Performance Management Setup.pptx', 'Unit 07 - Establishing Performance Expectations.pptx'):
    prs = Presentation(os.path.join(src, name)); n = 0
    for s in prs.slides:
        if not s.has_notes_slide: continue
        old = s.notes_slide.notes_text_frame.text
        new = re.sub(r'Unit 3, part 4\.(\d)', r'Unit 3, part 5.\1', old)
        if new != old: map_frame(s.notes_slide.notes_text_frame, lambda x: re.sub(r'Unit 3, part 4\.(\d)', r'Unit 3, part 5.\1', x), name); n += 1
    assert n >= 1, name
    prs.save(os.path.join(out, name)); LOG.append('%s: %d note(s) now point to Unit 3, part 5.2' % (name, n))
print('\n'.join(LOG))
