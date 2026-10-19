# -*- coding: utf-8 -*-
"""Unit 9 · Section 2 rework (19 Oct 2026) on Carol's deck 7f3fd5b2…
python3 deck_u09s2.py <her deck> <facilitator page> <out deck>
Old 2.1 slide becomes 1.2; 1.2 -> 1.3; 1.2.2 -> 1.4; new 1.5 (copy of 1.4); Section 1 Reflections gets 1.2; Section 2 cover, 2.1, 2.2, Reflections;
4.2-4.4 become the three slides of 4.2 The Unclogging Cycle; 4.5 -> 4.3; 5.1, 5.4 and Section 5 notes; Unit Summary notes."""
import sys, os, re, copy, html, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lxml import etree
from pptx import Presentation
from pptx.oxml.ns import qn
from u9s2_content import SUM_F, S2_OPEN, S2_GUIDE_P2_NEW, S2_GUIDE_P3_NEW, S2_H2, S2_SUB
SRC, FPAGE, OUT = sys.argv[1:4]
prs = Presentation(SRC); S = list(prs.slides); O = {i + 1: s for i, s in enumerate(S)}
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
FT = open(FPAGE, encoding='utf-8').read()
U = lambda h: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', h))).strip()
def plain_lines(h):
    h = re.sub(r'<script.*?</script>|<style.*?</style>', '', h, flags=re.S)
    h = re.sub(r'<(br|/p|/div|/li|/h\d|/tr|/summary|/label)[^>]*>', '\n', h); h = re.sub(r'</t[dh]>', ' · ', h)
    t = html.unescape(re.sub(r'<[^>]+>', '', h))
    return [re.sub(r'\s+', ' ', l).strip(' ·') for l in t.split('\n') if l.strip(' ·\r\t ')]
def div_end(t, i):
    d = 0
    for m in re.compile(r'<div\b|</div>').finditer(t, i):
        d += 1 if m.group(0) == '<div' else -1
        if d == 0: return m.end()
def part(title_start):
    k = FT.index('<div class="acc-t">' + title_start); s = FT.index('<div class="acc-b"><div class="cb">', k)
    body = FT[s:div_end(FT, s)]
    body = re.sub(r'<div class="fac-note-full[^"]*">.*?</div>\s*</div>', '', body, flags=re.S)
    return plain_lines(body)
def det(summary):
    k = FT.index('<summary class="u9-sub">' + summary); e = FT.index('</details>', k)
    return plain_lines(FT[k:e])[1:]
BAD = re.compile(r'\b(COMPASS|minutes?|mins?|Timing|triads?|Clog Clinic|KR/KPI|Listen for|Challenge any|Check that|Push back|Watch for|lens)\b|before CESI|pre-CESI|rather than')
def ntext(n): return O[n].notes_slide.notes_text_frame.text.replace('\x0b', '\n')
def tail_of(n):
    t = ntext(n); i = [x for x in (t.find('Source detail (S2R® manuscript):'), t.find('Professional insights:')) if x >= 0]
    return ([''] + [l for l in t[min(i):].split('\n')]) if i else []
def set_notes(slide, lines):
    for l in lines: assert not BAD.search(l), l
    body = slide.notes_slide.notes_text_frame._txBody
    for p in body.findall(qn('a:p')): body.remove(p)
    for line in lines:
        p = etree.SubElement(body, '{%s}p' % A)
        if not line.strip():
            e = etree.SubElement(p, '{%s}endParaRPr' % A); e.set('lang', 'en-GB'); continue
        r = etree.SubElement(p, '{%s}r' % A); rp = etree.SubElement(r, '{%s}rPr' % A); rp.set('lang', 'en-GB')
        etree.SubElement(r, '{%s}t' % A).text = line
def notes(slide, heading, teach, content, does=None, tail=()):
    L = [heading, '', 'TEACHING NOTES:'] + teach + ['', 'Content:'] + content
    if does: L += ['', 'Participant file — what participants complete:'] + ['- ' + d for d in does]
    set_notes(slide, L + list(tail))
def sub_notes(slide, pairs):
    L = slide.notes_slide.notes_text_frame.text.replace('\x0b', '\n').split('\n')
    t = '\n'.join(L)
    for a, b in pairs:
        assert a in t, (a[:60]); t = t.replace(a, b)
    set_notes(slide, [l for l in t.split('\n') if not re.search(r'^Time: the facilitator file gives no minute timing', l)])
def shp(s, name):
    m = [sh for sh in s.shapes if sh.name == name]; assert len(m) == 1, name; return m[0]
def put(s, name, *runs):
    tf = shp(s, name).text_frame
    for p in tf.paragraphs[1:]: p._p.getparent().remove(p._p)
    rs = tf.paragraphs[0].runs; assert len(rs) >= len(runs), (name, [r.text for r in rs])
    for r, t in zip(rs, runs): r.text = t
    for r in rs[len(runs):]: r._r.getparent().remove(r._r)
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
    return dst
G = lambda *names: [U(re.search(r'<li>%s[^<]*</li>' % re.escape(n), FT).group(0)) for n in names]

# ── 1.2 (old 2.1 slide) ──
s = O[10]
put(s, 'Text 1', '1.2 · Where performance becomes constrained')
put(s, 'Text 3', 'Clogs form where the strategy stretches today’s organisation beyond what it was designed to carry.')
notes(s, '1.2 — UNDERSTANDING WHERE PERFORMANCE BECOMES CONSTRAINED (Why clogs form · Two dimensions of performance)',
      G('1.2 ·'), part('1.2 &mdash; Understanding'),
      ['✎ Reflection — Where Is Your System Not Yet Ready? — the element of their operating system most likely to create friction under their current strategic direction, and why this is predictable given their strategy.'],
      tail_of(10))
# ── 1.3 (old 1.2) ──
s = O[6]
put(s, [sh.name for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.startswith('1.2 · The 7-Clog')][0], '1.3 · The Seven Performance Clogs')
notes(s, '1.3 — THE SEVEN PERFORMANCE CLOGS (ABCV-aligned · Select each clog to explore)', G('1.3 ·'), part('1.3 &mdash;'), None, tail_of(6))
# ── 1.4 (old 1.2.2) ──
s = O[7]
put(s, 'Text 0', '1.4 · Three performance lines of sight')
notes(s, '1.4 — THE THREE PERFORMANCE LINES OF SIGHT FROM THE SEVEN CLOGS (From the result to its cause)', G('1.4 ·'), part('1.4 &mdash;'), None, tail_of(7))
# ── 1.5 new (copy of 1.4) ──
n15 = duplicate(O[7])
put(n15, 'Text 0', '1.5 · Worked example: improving customer service')
put(n15, 'Text 2', '1  Performance outcome  ', '65% of enquiries resolved within 48 hours, against 90%.')
put(n15, 'Text 4', '2  Performance behaviour  ', 'Cases pass between departments; routine refunds wait for approval.')
put(n15, 'Text 6', '3  Performance condition  ', 'Structural Misfit, Decision Bottlenecks, Misaligned Metrics, Technology Lag.')
notes(n15, '1.5 — WORKED DIAGNOSTIC EXAMPLE: IMPROVING CUSTOMER SERVICE (Tracing the three lines of sight)', G('1.5 ·'), part('1.5 &mdash;'),
      ['✎ Reflection — Which Clogs Are Active? — a rating of each of the seven clogs, and the clog most active in their organisation with the organisational condition it sits in.'])
# ── Section 1 Reflections ──
s8, s13 = O[8], O[13]
p11, p12, p21, p23 = shp(s8, 'Reflection 1.1'), shp(s8, 'Reflection 1.2'), shp(s13, 'Reflection 2.1'), shp(s13, 'Reflection 2.3')
blob21, w21, h21 = p21.image.blob, p21.width, p21.height
gap = 274320; top = p11.top
pic = s8.shapes.add_picture(io.BytesIO(blob21), p11.left, 0, width=w21, height=h21); pic.name = 'Reflection 1.2 new'
ov12 = shp(s8, 'Part 1.2'); ov12.text_frame.paragraphs[0].runs[0].text = '1.5'; ov12.name = 'Part 1.5'; p12.name = 'Reflection 1.5'
ov11 = shp(s8, 'Part 1.1')
ov_new = copy.deepcopy(ov12._element); s8.shapes._spTree.append(ov_new); ovn = s8.shapes[-1]
ovn.text_frame.paragraphs[0].runs[0].text = '1.2'; ovn.name = 'Part 1.2'; pic.name = 'Reflection 1.2'
nid = max(int(e.get('id')) for e in s8._element.iter(qn('p:cNvPr'))); ov_new.find('.//' + qn('p:cNvPr')).set('id', str(nid + 1))
y = top
for p_, o_ in ((p11, ov11), (pic, ovn), (p12, shp(s8, 'Part 1.5'))):
    p_.top = y; o_.top = int(y + (p_.height - o_.height) / 2); y += p_.height + gap
assert y - gap <= prs.slide_height
set_notes(s8, ['SECTION 1 REFLECTIONS', '', 'Participants complete these reflections in their own file after the teaching.',
 '1.1 · Strategic Clog in Your Organisation: a strategy initiative that stalled, the blockage behind it, whether it could have been named earlier, and the organisational condition the individuals’ tasks depended on.',
 '1.2 · Where Is Your System Not Yet Ready?: the element of their operating system most likely to create friction under their current strategic direction, and why.',
 '1.5 · Which Clogs Are Active?: a rating of each of the seven clogs, and the clog most active in their organisation with the organisational condition it sits in.'])
# ── Section 4 notes and Section 2 ──
s = O[9]
put(s, 'Text 3', S2_H2)
t9 = ntext(9)
sub_notes(s, [('Why Clogs Are Predictable Features of Execution', S2_H2),
 ('Understanding why execution friction is the inevitable consequence of system misalignment — and introducing the 7 Strategic Unclogging Levers as the leadership toolkit for restoring execution flow.', S2_SUB),
 (t9[t9.index('Spend time on the pressure point examples'):t9.index('For the 7 levers')], U(S2_GUIDE_P2_NEW) + '\n'),
 (t9[t9.index('For the 7 levers'):t9.index('\n', t9.index('For the 7 levers'))], U(S2_GUIDE_P3_NEW) + '\n\nSection opening (on the page):\n' + '\n'.join(plain_lines(S2_OPEN)))])
s = O[11]
put(s, 'Text 0', '2.1 · Three disciplines of execution engineering')
notes(s, '2.1 — THREE DISCIPLINES OF EXECUTION ENGINEERING (Step through each)',
      ['Teach the three disciplines one at a time. For each, teach the discipline, then what it means in people performance and in organisational performance, using the examples on the page.'],
      part('2.1 &mdash; Three'), None, tail_of(11))
s = O[12]
put(s, [sh.name for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.startswith('2.3 · ')][0], '2.2 · The 7 Strategic Unclogging Levers')
notes(s, '2.2 — THE 7 STRATEGIC UNCLOGGING LEVERS (Select each lever to explore)',
      ['Open the levers one at a time: what the lever does, how it works, and what it changes in people performance and in organisational performance. Rarely does a single lever clear a clog alone: ask which lever combination addresses the root cause.'],
      part('2.2 &mdash; The 7'),
      ['✎ Reflection — Your Lever — the primary lever and the second lever they would pull for the clog they identified in Awareness, and why this combination.'],
      tail_of(12))
for nm in ('Reflection 2.1', 'Part 2.1'): shp(s13, nm)._element.getparent().remove(shp(s13, nm)._element)
o23 = shp(s13, 'Part 2.3'); p23.top = top; o23.top = int(top + (p23.height - o23.height) / 2)
o23.text_frame.paragraphs[0].runs[0].text = '2.2'; o23.name = 'Part 2.2'; p23.name = 'Reflection 2.2'
set_notes(s13, ['SECTION 2 REFLECTIONS', '', 'Participants complete this reflection in their own file after the teaching.',
 '2.2 · Your Lever: the primary lever and the second lever they would pull for the clog they identified in Awareness, and why this combination.'])
# ── Section 4 ──
sub_notes(O[17], [('Use Review–Realign–Restore as the established', 'Use the Unclogging Cycle, Review–Realign–Restore, as the established')] if 'Use Review–Realign–Restore as the established' in ntext(17) else [])
sub_notes(O[18], [('Here the executive team applies it together to a clog', 'Here the executive team applies it together, as the Unclogging Cycle, to a clog')])
intro = plain_lines(FT[FT.index('<p>The Unclogging Cycle is the S2R'):FT.index('</p>', FT.index('<p>The Unclogging Cycle is the S2R'))])
for n, stage, sm in ((19, 'REVIEW', 'REVIEW &mdash; Establish'), (20, 'REALIGN', 'REALIGN &mdash; Establish'), (21, 'RESTORE', 'RESTORE &mdash; Activate the Seven')):
    s = O[n]; tshape = [sh.name for sh in s.shapes if sh.has_text_frame and re.match(r'4\.[234] · ', sh.text_frame.text)][0]
    put(s, tshape, '4.2 · The Unclogging Cycle: ' + stage)
    content = (intro if stage == 'REVIEW' else []) + det(sm) + (det('The Unclogging Record') if stage == 'RESTORE' else [])
    notes(s, '4.2 — THE UNCLOGGING CYCLE: REVIEW–REALIGN–RESTORE · ' + stage,
          ['Teach %s as one stage of the Unclogging Cycle: what the stage establishes, what it means in people performance and in organisational performance, and what it adds to the Unclogging Record.' % stage],
          content, None, tail_of(n))
s = O[22]; put(s, [sh.name for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.startswith('4.5 · ')][0], '4.3 · Worked example: the Unclogging Cycle')
sub_notes(s, [('4.5 — WORKED EXAMPLE: REVIEW–REALIGN–RESTORE', '4.3 — WORKED EXAMPLE: THE UNCLOGGING CYCLE')])
o4 = shp(O[23], 'Part 4'); o4.text_frame.paragraphs[0].runs[0].text = '4.3'
if '4.5' in ntext(23): sub_notes(O[23], [('4.5', '4.3')])
# ── Section 5 ──
t24 = ntext(24)
sub_notes(O[24], [('Each group selects one challenge from the list it documented before CESI began and links it to a strategic result (5.1).', 'Each group selects one challenge from its Problem Charter and links it to one of its Objectives and Key Results (5.1).'),
                  ('The group applies Review–Realign–Restore (5.4)', 'The group simulates the Unclogging Cycle, Review–Realign–Restore (5.4)')]
         + ([(t24[t24.index('At the beginning of CESI'):t24.index('select one challenge', t24.index('At the beginning of CESI'))], 'In its Problem Charter, each group recorded recurring work-based organisational challenges drawn from its members’ professional experiences and chose the challenges its executive team would address. These challenges informed the simulated Capstone organisation. Participants now return to that list, ')] if 'At the beginning of CESI' in t24 else []))
sub_notes(O[25], [('selected from its pre-CESI preparation', 'selected from its Problem Charter')])
put(O[26], 'Text 4', 'One challenge from your group’s Problem Charter.')
t26 = ntext(26)
sub_notes(O[26], [('Each group returns to the organisational challenges its members documented before CESI began, and selects one', 'Each group returns to the challenges in its Problem Charter, and selects one'),
 (t26[t26.index('\nContent:\n'):t26.index('Use existing Capstone performance')], '\nContent:\n' + '\n'.join(l for l in part('5.1 &mdash;') if not l.startswith('Use existing Capstone')) + '\n')])
s = O[29]; put(s, 'Text 0', '5.4 · Simulate the Unclogging Cycle')
t29 = ntext(29)
sub_notes(s, [('5.4 — APPLY REVIEW–REALIGN–RESTORE (Capstone Work)', '5.4 — SIMULATE THE UNCLOGGING CYCLE (Capstone Work)'),
              ('TEACHING NOTES:\n', 'TEACHING NOTES:\nThe group simulates how its executive team takes the selected challenge through the Unclogging Cycle, working through REVIEW, REALIGN and RESTORE in turn. Together they complete the group’s Strategic Unclogging Clinic Record.\n')])
t31 = ntext(31)
pairs = []
for arc, nxt in (('Intelligence — Why', 'Extrapolating — Where'), ('Integration — Collective', 'Application — In Practice'), ('Application — In Practice', '“When unclogging')):
    i = t31.index(arc + '\n') + len(arc) + 1; j = t31.index(nxt, i)
    key = arc.split(' — ')[0]
    pairs.append((t31[i:j], U(SUM_F[key]) + '\n'))
if 'Awareness — What\n' in t31:
    i = t31.index('Awareness — What\n') + len('Awareness — What\n'); j = t31.index('Intelligence — Why', i); pairs.append((t31[i:j], U(SUM_F['Awareness']) + '\n'))
sub_notes(O[31], pairs)
# ── order ──
lst = prs.slides._sldIdLst; ids = list(lst)
order = [1, 2, 3, 4, 5, 10, 6, 7, 'n15', 8, 9, 11, 12, 13] + list(range(14, 32))
by = {i + 1: ids[i] for i in range(31)}; by['n15'] = ids[31]
for el in ids: lst.remove(el)
for k in order: lst.append(by[k])
prs.save(OUT)
print('saved', OUT, len(prs.slides))
