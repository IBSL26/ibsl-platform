# -*- coding: utf-8 -*-
"""Carol's own Unit 5 deck of 9 October 2026 (35 slides) is the master. This script brings it in line with the live Unit 5 pages
and changes nothing else. Usage: python3 carol_deck_align.py <Carol's deck> <the 38-slide deck built on 9 October> <u05_data.json> <out.pptx>
What it changes (each change is checked; the script stops if her deck is not as expected):
  slides 1-3   notes: the 9 October notes (hers were untouched and still described the watch list, the 30-day commitment and 4.3)
  slide 25     notes: the line that said 3.1 runs over two slides
  slide 26     notes: the registered mark on Strategy2Results® and S2R® (two places); nothing else of hers is touched
  slide 28     notes: the list of parts in Section 4
  slide 29     notes: "4.3" -> "4.1" in the heading and in the reflection line
  slide 30     notes: the ten role blocks take the wording of the live role cards (her framing and her step titles stay)
  slide 31     the reflection that has left the page goes; the One Voice reflection is 4.1; notes from the 9 October deck
  slide 32     Section 5 learning outcome 1 (her wording of 9 October), on the slide and in the notes
  slide 35     the closing question and the notes of the Unit Summary (hers were untouched and described the old Section 5)"""
import sys, copy, json, html, re, os
from pptx import Presentation
from pptx.util import Pt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import u5b_content as B
import u5d_content as E
src, new, data, out = sys.argv[1:5]
C = Presentation(src); N = Presentation(new); D = json.load(open(data, encoding='utf-8'))
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
def tf(P, i): return P.slides[i - 1].notes_slide.notes_text_frame
def ntext(P, i): return tf(P, i).text
def first_text(P, i):
    for sh in P.slides[i - 1].shapes:
        if sh.has_text_frame and sh.text_frame.text.strip(): return sh.text_frame.text.strip()
def copy_notes(i_c, i_n):
    """Carol's slide takes the notes of the 9 October deck, paragraph by paragraph, with their formatting."""
    a, b = tf(C, i_c)._txBody, tf(N, i_n)._txBody
    for p in a.findall(A + 'p'): a.remove(p)
    for p in b.findall(A + 'p'): a.append(copy.deepcopy(p))
def para(i, startswith, count=1):
    ps = [p for p in tf(C, i).paragraphs if p.text.startswith(startswith)]
    assert len(ps) == count, (i, startswith, len(ps)); return ps[0]
def set_text(p, text):
    assert p.runs, 'no run'
    p.runs[0].text = text
    for r in p.runs[1:]: r._r.getparent().remove(r._r)
def add_after(p, text):
    q = copy.deepcopy(p._p); p._p.addnext(q)
    from pptx.text.text import _Paragraph
    q2 = _Paragraph(q, p._parent); set_text(q2, text); return q2
def drop(p): p._p.getparent().remove(p._p)
un = lambda t: html.unescape(re.sub(r'<[^>]+>', '', t))

assert len(C.slides) == 35 and len(N.slides) == 38
# ── slides 1 to 3: front notes ──────────────────────────────────────────────────────────────────
for i in (1, 2, 3):
    assert first_text(C, i) == first_text(N, i)
    assert 'watch list' in ntext(C, i) or 'Alignment Toolkit' in ntext(C, i) or 'Team Alignment Plan' in ntext(C, i), i
    copy_notes(i, i)
# ── slide 25: Section 3 opener ──────────────────────────────────────────────────────────────────
set_text(para(25, '1. 3.1: the OCEAVL Assessment, on two slides'), '1. 3.1: the OCEAVL Assessment and its seven dimensions.')
# ── slide 26: her own notes; the registered mark only (her standing rule: Strategy2Results® and S2R® carry the ®) ───
def mark(i, old, new):
    hits = [r for p in tf(C, i).paragraphs for r in p.runs if old in r.text]
    assert len(hits) == 1, (i, old, len(hits)); hits[0].text = hits[0].text.replace(old, new)
mark(26, 'In Strategy2Results, this', 'In Strategy2Results®, this')
mark(26, 'Then connect to S2R:', 'Then connect to S2R®:')
# ── slide 28: Section 4 opener ──────────────────────────────────────────────────────────────────
set_text(para(28, '1. 4.1: the Converging Zone and the two states it separates.'), '1. 4.1: leading change with one voice, and its four commitments.')
set_text(para(28, '2. 4.2: the alignment responsibility and the alignment hot zone'), '2. 4.2: the Converging Zone Contribution and the Alignment Hot Zone of each leadership role.')
set_text(para(28, '3. 4.3: the four commitments of leading change with one voice.'), '3. The Section 4 Reflections slide: the two reflections participants write on the portal after the teaching.')
drop(para(28, '4. The Section 4 Reflections slide: the three reflections'))
# ── slide 29: 4.1 ───────────────────────────────────────────────────────────────────────────────
assert first_text(C, 29) == '4.1 · Leading Change with One Voice'
set_text(para(29, '4.3 — LEADING CHANGE WITH ONE VOICE'), '4.1 — LEADING CHANGE WITH ONE VOICE (FOUR COMMITMENTS)')
set_text(para(29, 'Participants write the reflection of 4.3 in the participant file:'), 'Participants write the reflection of 4.1 in the participant file:')
assert D['REFL']['4.1']['prompt'] in ntext(C, 29)
# ── slide 30: 4.2, the ten roles ────────────────────────────────────────────────────────────────
assert first_text(C, 30) == '4.2 · Collective Intelligence Across the Leadership Team'
K = {k[0]: k for k in B.KIT}
for n, h in enumerate(D['HOT']):
    old = B.HOT[n]; k = K[old[1]]; assert old[0] == h['role']
    p_tag = para(30, '%s · %s.' % (old[0], un(B.hot_tag(n))))
    p_why = para(30, un(old[3]))
    p_trig = [p for p in tf(C, 30).paragraphs if p.text == 'Likely trigger: ' + k[5]]
    p_cues = [p for p in tf(C, 30).paragraphs if p.text == 'Look out for: ' + k[3] + ' ' + k[4]]
    assert len(p_trig) == 1 and len(p_cues) == 1, (h['role'], len(p_trig), len(p_cues))
    set_text(p_tag, '%s · %s.' % (h['role'], h['tag']))
    set_text(p_why, 'Why the role is inclined to it: ' + h['why'])
    need = add_after(p_tag, 'What people need: ' + h['need'])
    set_text(p_trig[0], 'What sets it off: ' + h['trig'])
    set_text(p_cues[0], 'What is seen and heard: ' + h['cues'])
    add_after(p_cues[0], 'What it costs: ' + h['cost'])
t30 = ntext(C, 30)
assert 'Likely trigger' not in t30 and 'Look out for' not in t30 and t30.count('What it costs: ') == 10 and t30.count('What people need: ') == 10
# ── slide 31: Section 4 Reflections ─────────────────────────────────────────────────────────────
s31, n34 = C.slides[30], N.slides[33]
assert first_text(C, 31) == 'Section 4 Reflections' and first_text(N, 34) == 'Section 4 Reflections'
sh = {x.name: x for x in s31.shapes}; nn = {x.name: x for x in n34.shapes}
assert set(sh) == {'Text 0', 'Reflection 4.1', 'Part 4.1', 'Reflection 4.2', 'Part 4.2', 'Reflection 4.3', 'Part 4.3'}
for nm in ('Reflection 4.1', 'Part 4.1'): sh[nm]._element.getparent().remove(sh[nm]._element)       # "Which state is your organisation closer to?" has left the page
for old_nm, new_nm in (('Reflection 4.3', 'Reflection 4.1'), ('Part 4.3', 'Part 4.1')):
    x = sh[old_nm]; x.left, x.top = nn[new_nm].left, nn[new_nm].top; x.name = new_nm
sh['Part 4.3'].text_frame.paragraphs[0].runs[0].text = '4.1'
copy_notes(31, 34)
# ── slide 32: Section 5 opener, learning outcome 1 ──────────────────────────────────────────────
hit = [x for x in C.slides[31].shapes if x.has_text_frame and x.text_frame.text.strip() == E.SLO5_1_OLD]
assert len(hit) == 1; r = hit[0].text_frame.paragraphs[0].runs; r[0].text = E.SLO5_1_NEW
for x in r[1:]: x._r.getparent().remove(x._r)
set_text(para(32, '1. ' + E.SLO5_1_OLD), '1. ' + E.SLO5_1_NEW)
assert D['SECTIONS'][4]['outcomes'][0] == E.SLO5_1_NEW
# ── slide 35: Unit Summary ──────────────────────────────────────────────────────────────────────
assert first_text(C, 35) is not None and 'watch list' in ntext(C, 35)
hit = [x for x in C.slides[34].shapes if x.has_text_frame and x.text_frame.text.strip().startswith('Which trigger in your team plan')]
assert len(hit) == 1; r = hit[0].text_frame.paragraphs[0].runs; r[0].text = D['CLOSING_Q']
for x in r[1:]: x._r.getparent().remove(x._r)
copy_notes(35, 38)
assert D['CLOSING_Q'] in ntext(C, 35)
C.save(out)
print('saved', out, '·', len(C.slides), 'slides')
