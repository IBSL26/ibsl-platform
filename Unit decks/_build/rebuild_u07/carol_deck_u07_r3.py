# -*- coding: utf-8 -*-
"""Unit 7 deck, round 3 (Carol, 11 October 2026, 12:57). Carol's own deck is the master: the 24-slide file she saved at 12:56 (the round 2 deck, with one slide she removed).
Usage: python3 carol_deck_u07_r3.py <Carol's 24-slide deck> <participant page> <facilitator page> <pictures folder> <out.pptx>
Changed, and nothing else:
  - "Section 4 Reflections": the 4.2 picture is replaced (the closing "This is Portfolio work…" lines are out of the picture);
  - the Section 5 opener: notes for the two exercises;
  - "Section 5 · The four steps" becomes "5.1 · Building the Expectation Architecture", with notes that guide how the work is completed;
  - a copy of that slide becomes "5.2 · Conducting the Alignment Dialogue with the Board Chair";
  - the "Unit Summary · Closing" slide leaves the deck.
The facilitator does not review group work: the Section 5 notes carry no "listen for", "check", "challenge" or "watch for". No times."""
import sys, re, copy, html, json, os
from pptx import Presentation
from pptx.util import Inches
from pptx.oxml.ns import qn
from lxml import etree
from PIL import Image
import u7_content as C
deck, P, F, PICS, out = sys.argv[1:6]
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def plain(path):
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'<style.*?</style>|<script.*?</script>|<!--.*?-->', ' ', t, flags=re.S)
    t = re.sub(r'</?(?:em|strong|b|i)\b[^>]*>', '', t)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
vp, vf = plain(P), plain(F)
def tx(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()
def on_pages(s, where='pf'):
    s = tx(s)
    for w in where: assert s in (vp if w == 'p' else vf), ('not on the %s page: ' % w) + s
    return s
prs = Presentation(deck)
S = list(prs.slides)
assert len(S) == 24, len(S)
def texts(s): return [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
def first(s): t = texts(s); return t[0].text_frame.text if t else ''
assert first(S[20]) == 'Section 4 Reflections' and texts(S[21])[3].text_frame.text == 'Establishing Delivery Expectations' and first(S[22]) == 'Section 5 · The four steps' and 'Unit Summary' in first(S[23])
def set_text(shape, *run_texts):
    ps = shape.text_frame.paragraphs; runs = ps[0].runs
    assert len(ps) == 1 or all(not p.runs for p in ps[1:]), shape.name
    assert len(runs) == len(run_texts), (shape.name, [r.text for r in runs], run_texts)
    for r, t in zip(runs, run_texts): r.text = t
BAD = re.compile(r'\b(minutes?|mins?|Timing|working days|five-day|Listen for|Challenge any|Watch for|Check that|Push back|Probe)\b')
def set_notes(slide, lines):
    body = slide.notes_slide.notes_text_frame._txBody
    for p in body.findall(qn('a:p')): body.remove(p)
    for line in lines:
        assert not BAD.search(line), line
        p = etree.SubElement(body, '{%s}p' % A)
        bold = line.startswith('§'); text = line[1:] if bold else line
        if not text.strip():
            e = etree.SubElement(p, '{%s}endParaRPr' % A); e.set('lang', 'en-GB'); e.set('dirty', '0'); continue
        r = etree.SubElement(p, '{%s}r' % A); rp = etree.SubElement(r, '{%s}rPr' % A); rp.set('lang', 'en-GB')
        if bold: rp.set('b', '1')
        rp.set('dirty', '0'); etree.SubElement(r, '{%s}t' % A).text = text
def duplicate(src):
    dst = prs.slides.add_slide(src.slide_layout)
    for sh in list(dst.shapes): sh._element.getparent().remove(sh._element)
    rid = {}
    for rel in src.part.rels.values():
        if rel.reltype.endswith('/image'): rid[rel.rId] = dst.part.relate_to(rel._target, rel.reltype)
    for sh in src.shapes: dst.shapes._spTree.append(copy.deepcopy(sh._element))
    bg = src._element.cSld.find(qn('p:bg'))
    if bg is not None and dst._element.cSld.find(qn('p:bg')) is None: dst._element.cSld.insert(0, copy.deepcopy(bg))
    for el in dst._element.iter():
        for k in (RID + 'embed', RID + 'link', RID + 'id'):
            if el.get(k) in rid: el.set(k, rid[el.get(k)])
    nt, st = dst.notes_slide._element.cSld.spTree, src.notes_slide._element.cSld.spTree
    for el in [e for e in nt if e.tag in (qn('p:sp'), qn('p:pic'))]: nt.remove(el)
    for el in [e for e in st if e.tag == qn('p:sp')]: nt.append(copy.deepcopy(el))
    assert dst.notes_slide.notes_text_frame is not None
    return dst

# ═══ Section 4 Reflections: the 4.2 picture without its closing lines ═══════════════════════════════════
r4 = S[20]; old = [sh for sh in r4.shapes if sh.name == 'Reflection 4.2']; assert len(old) == 1
left, top, width = old[0].left, old[0].top, old[0].width; descr = old[0]._element.nvPicPr.cNvPr.get('descr')
pos = list(r4.shapes._spTree).index(old[0]._element); r4.shapes._spTree.remove(old[0]._element)
new = r4.shapes.add_picture(os.path.join(PICS, 'ref_4.2.png'), left, top, width=width); new.name = 'Reflection 4.2'; new._element.nvPicPr.cNvPr.set('descr', descr or '')
r4.shapes._spTree.remove(new._element); r4.shapes._spTree.insert(pos, new._element)
assert new.top + new.height <= prs.slide_height - Inches(0.15)

# ═══ Section 5 opener ════════════════════════════════════════════════════════════════════════════════════
s5 = S[21]; t = texts(s5); slo = [on_pages(t[5].text_frame.text), on_pages(t[6].text_frame.text)]
H = C.HOW_S5['f']   # the facilitator's own wording: 'Each group …'
set_notes(s5, ['§SECTION 5 · APPLICATION — IN PRACTICE', '', '§HOW THIS SECTION RUNS:', on_pages(H['lead'], 'f')] + [on_pages(x, 'f') for x in H['steps']] + [on_pages(x, 'f') for x in H['tail']] + ['',
  '§SECTION LEARNING OUTCOMES:', '1. ' + slo[0], '2. ' + slo[1], '', '§HOW TO OPEN THE SECTION:', '',
  '§1. Say what the section does.', 'Say: "Section 5 has two exercises.', 'In 5.1 your group builds the Expectation Architecture for two of its Objectives.',
  'In 5.2 your group prepares the Alignment Dialogue with your board chair."', '',
  '§2. Say how the group works.', 'Say: "Both exercises are group work.', 'Your group agrees each entry.', 'One member acts as scribe.', 'Every member then types the agreed entries into their own page, in the session or after it."', '',
  '§3. Say where the work goes.', 'Say: "This is Capstone work. You read your group’s record at the foot of the section and select Confirm. Your confirmed record feeds your team’s Capstone Blueprint."',
  on_pages(C.GUIDE_S5_F[0], 'f').replace('Your role: ', 'Your role in this section: '), on_pages(C.GUIDE_S5_F[2], 'f').replace('Before the group starts: ', '')])

# ═══ 5.1 · Building the Expectation Architecture (the four steps slide) ══════════════════════════════════
s51 = S[22]; set_text(texts(s51)[0], '5.1 · Building the Expectation Architecture')
HS = C.HOW_STEP_P
set_notes(s51, ['§5.1 — BUILDING THE EXPECTATION ARCHITECTURE (CAPSTONE WORK)', '', '§HOW TO TEACH IT:', '',
  '§1. Say what the group does.',
  'Say: "' + tx(H['steps'][0]).split('. ', 1)[1] + '"', '',
  '§2. Step 1 · Start With the Future.',
  'Say: "' + on_pages(HS[0][0], 'p'), on_pages(HS[0][1], 'p'), on_pages(HS[0][2], 'p'),
  on_pages('Write the leader framing: the sentence that you, as the leader, say to the owner to connect the Key Result to that Future.', 'p') + '"',
  'The lists hold the Enterprise OKRs the group confirmed in Unit 3 and the Success in Practice statements it confirmed in Unit 2.', '',
  '§3. Step 2 · Clarify the Delivery Expectation.', 'Say: "' + ' '.join(on_pages(x, 'p') for x in HS[1]) + '"', '',
  '§4. Step 3 · Identify the Expectations Chain.', 'Say: "' + ' '.join(on_pages(x, 'p') for x in HS[2]) + '"', '',
  '§5. Step 4 · Confirm Ownership.', 'Say: "' + ' '.join(on_pages(x, 'p') for x in HS[3]) + '"', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', on_pages(C.ACT_S5_F % '5.1', 'f')] +
  ['Step %d: %s' % (i + 1, ' '.join(tx(x) for x in C.COMPLETES_F[i])) for i in range(4)])

# ═══ 5.2 · Conducting the Alignment Dialogue with the Board Chair (a copy of the 5.1 slide) ══════════════
s52 = duplicate(s51); t = texts(s52); set_text(t[0], '5.2 · The Alignment Dialogue with the Board Chair')
for sh, (a, b) in zip(t[1:], (('G · Goal  ', 'what a 10 looks like for your chair'), ('R · Reality  ', 'what stands behind your chair’s score'),
                             ('O · Options  ', 'what could resolve the metric and the timeframe'), ('W · Will  ', 'what you and your chair agree to do'))): set_text(sh, a, b)
HD = C.HOW_52_P
set_notes(s52, ['§5.2 — CONDUCTING THE ALIGNMENT DIALOGUE WITH THE BOARD CHAIR (CAPSTONE WORK)', '', '§HOW TO TEACH IT:', '',
  '§1. Link it to part 4.2.', 'Say: "' + on_pages(C.INTRO_52['p'], 'p') + '"', '',
  '§2. Give the scenario.', 'Say: "' + on_pages(C.SCENARIO['p'], 'p').replace('The scenario. ', '').replace('“', '‘').replace('”', '’') + '"', '',
  '§3. Say what the group writes.', 'Say: "' + on_pages(HD[0], 'p'), on_pages(HD[2], 'p'), on_pages(HD[3], 'p') + '"', '',
  '§4. Say where the work goes.', 'Say: "You read your group’s record at the foot of the section and select Confirm. Your confirmed record feeds your team’s Capstone Blueprint."', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', on_pages(C.ACT_S5_F % '5.2', 'f')] + [tx(x) for x in C.COMPLETES_52G_F])

# ═══ the Unit Summary slide leaves; 5.2 closes the deck ══════════════════════════════════════════════════
lst = prs.slides._sldIdLst; ids = list(lst); assert len(ids) == 25
by = {id(s): el for s, el in zip(list(prs.slides), ids)}
gone = by[id(S[23])]; prs.part.drop_rel(gone.get(RID + 'id'))
new_order = S[:23] + [s52]
for el in ids: lst.remove(el)
for s in new_order: lst.append(by[id(s)])
prs.save(out)
print(len(prs.slides), 'slides ->', out)
