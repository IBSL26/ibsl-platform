# -*- coding: utf-8 -*-
"""Unit 8 deck, round 2 (Carol's amendments of 12 October 2026, 13:10). Carol's own deck is the master (she reworked the notes of slides 3 to 7 herself).
Usage: python3 carol_deck_u08_r2.py <Carol's deck> <participant page> <facilitator page> <pictures folder> <out.pptx>
Her slides and notes stay as she saved them, except:
  - slide titles of the renamed parts (1.1, 1.3), the 1.2 card "Enables Timely Correction" (she wrote "Intime"), the 1.3 stage lines, the notes headings of renamed parts;
  - new or rebuilt slides with notes in the Unit 2 to 7 format: 1.4 The Accountability Loop, Section 1/3/4 Reflections, 3.2 The CXO performance gap contributors,
    4.2 The Accountability Loop role play and its evaluation criteria (criterion 02 removed), the Section 2/3/4/5 openers, 5.1 Decision points;
  - slides that leave: 2.1 Execution discipline, 2.3 Three progress signals, 4.1 The Collective Intelligence principle, 4.3 The Synthesis Layer,
    The Collective Intelligence Board, Unit Summary · Closing (it asked for the five-day commitment).
No times. No review wording on the group work of Section 5."""
import sys, re, copy, html, json, os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.oxml.ns import qn
from lxml import etree
from PIL import Image
import u8_content as C
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
def on(s, where='pf'):
    s = tx(s)
    for w in where: assert s in (vp if w == 'p' else vf), ('not on the %s page: ' % w) + s
    return s
prs = Presentation(deck)
S = list(prs.slides); assert len(S) == 23, len(S)
def texts(s): return [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
def first(s): t = texts(s); return t[0].text_frame.text if t else ''
EXPECT = {4: '1.1 ·', 6: '1.3 ·', 7: '1.3 · The Accountability Loop', 9: '2.1 · Execution', 10: '2.2 ·', 11: '2.3 ·', 13: 'Four fractures', 15: '4.1 · The Collective', 17: '4.3 · The Synthesis', 19: 'The Collective Intelligence Board', 22: 'Unit Summary'}
for i, a in EXPECT.items(): assert first(S[i]).startswith(a), (i, first(S[i]))
assert texts(S[16])[0].text_frame.text.startswith('4.2 · The Collective') and texts(S[20])[0].text_frame.text.startswith('5.1 · The Accountability') and first(S[21]) == 'Observer evaluation criteria'
def set_text(shape, *run_texts):
    ps = shape.text_frame.paragraphs; runs = ps[0].runs
    assert len(runs) == len(run_texts), (shape.name, [r.text for r in runs], run_texts)
    for r, t in zip(runs, run_texts): r.text = t
def find(slide, start):
    m = [sh for sh in texts(slide) if sh.text_frame.text.startswith(start)]; assert len(m) == 1, (start, [x.text_frame.text for x in texts(slide)]); return m[0]
BAD = re.compile(r'\b(minutes?|mins?|Timing|working days|five-day|Listen for|Challenge any|Check that|Push back)\b')
def set_notes(slide, lines, watch_ok=False):
    body = slide.notes_slide.notes_text_frame._txBody
    for p in body.findall(qn('a:p')): body.remove(p)
    for line in lines:
        assert not BAD.search(line), line
        if not watch_ok: assert 'Watch for' not in line, line
        p = etree.SubElement(body, '{%s}p' % A)
        bold = line.startswith('§'); text = line[1:] if bold else line
        if not text.strip():
            e = etree.SubElement(p, '{%s}endParaRPr' % A); e.set('lang', 'en-GB'); e.set('dirty', '0'); continue
        r = etree.SubElement(p, '{%s}r' % A); rp = etree.SubElement(r, '{%s}rPr' % A); rp.set('lang', 'en-GB')
        if bold: rp.set('b', '1')
        rp.set('dirty', '0'); etree.SubElement(r, '{%s}t' % A).text = text
def note_replace(slide, pairs):
    """Replace text inside Carol's own notes, paragraph by paragraph; each old text must be found."""
    found = {a: 0 for a, b in pairs}
    for p in slide.notes_slide.notes_text_frame.paragraphs:
        full = ''.join(r.text for r in p.runs)
        new = full
        for a, b in pairs:
            if a in new: new = new.replace(a, b); found[a] += 1
        if new != full:
            p.runs[0].text = new
            for r in p.runs[1:]: r.text = ''
    for a, n in found.items(): assert n, 'not in the notes: ' + a
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
def drop_shapes(slide, names):
    for sh in [s for s in slide.shapes if s.name in names]: sh._element.getparent().remove(sh._element)
OVAL = None
def oval(slide, label, left, top):
    global OVAL
    from pptx.oxml import parse_xml
    el = parse_xml(OVAL); nid = max(int(e.get('id')) for e in slide._element.iter(qn('p:cNvPr'))) + 1
    el.find('.//' + qn('p:cNvPr')).set('id', str(nid)); slide.shapes._spTree.append(el)
    sh = slide.shapes[-1]; sh.left, sh.top = left, top; sh.name = 'Part ' + label
    sh.text_frame.paragraphs[0].runs[0].text = label
    return sh
def reflection_slide(title, items, notes):
    """items: [(part label, picture file)] stacked; each with a gold oval at the left."""
    s = duplicate(S[6])  # a slide with the standard title box
    drop_shapes(s, [sh.name for sh in s.shapes if sh.name != 'Text 0'])
    set_text(texts(s)[0], title)
    left, right, top0, bottom = Inches(1.85), Inches(12.85), Inches(1.6), Inches(7.2)
    gap = Inches(0.22); width = right - left
    hs = []
    for _, f in items:
        w, h = Image.open(os.path.join(PICS, f)).size; hs.append(width * h / w)
    scale = min(1, (bottom - top0 - gap * (len(items) - 1)) / sum(hs)); print(title, 'picture scale', round(scale, 2))
    y = top0
    for (lab, f), h in zip(items, hs):
        pw = int(width * scale); ph = int(h * scale)
        pic = s.shapes.add_picture(os.path.join(PICS, f), left, int(y), width=pw); pic.name = 'Reflection ' + lab
        oval(s, lab, Inches(0.6), int(y + ph / 2 - Inches(0.475)))
        y += ph + gap
    assert y - gap <= bottom + 10
    set_notes(s, notes)
    return s

# the gold oval of the reflection slides (as in Carol's Unit 7 deck)
OVAL = ('''<p:sp xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:nvSpPr><p:cNvPr id="900" name="Part"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="868680" cy="868680"/></a:xfrm><a:prstGeom prst="ellipse"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="C6A24C"/></a:solidFill><a:ln><a:solidFill><a:srgbClr val="C6A24C"/></a:solidFill></a:ln><a:effectLst/></p:spPr><p:txBody><a:bodyPr wrap="none" lIns="0" tIns="0" rIns="0" bIns="0" rtlCol="0" anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="en-GB" sz="2400" b="1"><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:latin typeface="Calibri"/></a:rPr><a:t>1.1</a:t></a:r></a:p></p:txBody></p:sp>''')
REFS = json.load(open(os.path.join(PICS, 'reflections.json'), encoding='utf-8'))
LABELS = {'1.1': 'Reflection — Activity vs Progress', '1.4': 'Reflection — The Cycle and the Loop in Your Organisation', '3.1': 'Reflection — Which Gap Is Most Prevalent in Your Organisation?',
          '4.1a': 'Reflection — Your Progress Signal', '4.1b': 'Reflection — Your Early Warning Signal', '4.1c': 'Reflection — Your Execution Learning'}
def rq(part): return '%s %s: "%s"' % (part[:3], LABELS[part], REFS[part]['prompt'])

note_replace(S[0], [('The Accountability Loop role play in Application is non-negotiable: it is where the conceptual work becomes a leadership skill.', 'The Accountability Loop role play in part 4.2 is where the conceptual work becomes a leadership skill, and Section 5 applies the four consequences of weak review discipline to the group’s own strategy.'),
                   ('through the Collective Intelligence Circle,', 'through the Enterprise Performance Intelligence Circle (EPIC),')])
# ═══ Section 1 ═════════════════════════════════════════════════════════════════════════════════════════
note_replace(S[2], [('Running the Review–Realign–Restore Cycle', tx(C.S5_TITLE))])
set_text(texts(S[4])[0], '1.1 · The execution visibility infrastructure')
note_replace(S[4], [('1.1 — FROM ACTIVITY TO PROGRESS: THE VISIBILITY SHIFT (Core concept)', '1.1 — THE EXECUTION VISIBILITY INFRASTRUCTURE (Core concept)')])
set_text(find(S[5], '04 ·'), '04 · Enables Timely Correction')
set_text(find(S[5], 'Patterns in how work'), 'Data turned into decision insight.')
note_replace(S[5], [('Enables Intime Correction', 'Enables Timely Correction')])
set_text(texts(S[6])[0], '1.3 · From performance measurement to execution recovery')
for a, b in (('Establishing evidence-based visibility.', 'Establish execution reality.'), ('Diagnosing the source of performance gaps.', 'Diagnose and address execution gaps.'), ('Rebuilding momentum.', 'Rebuild execution momentum.')):
    set_text(find(S[6], a), b)
note_replace(S[6], [('1.3 — THE REVIEW–REALIGN–RESTORE CYCLE (3 stages)', '1.3 — FROM PERFORMANCE MEASUREMENT TO EXECUTION RECOVERY (the Review–Realign–Restore Cycle, R3)')])
# 1.4 · the Accountability Loop (Carol's slide 8, renamed)
set_text(texts(S[7])[0], '1.4 · The Accountability Loop')
CA = C.CAUSES14
set_notes(S[7], ['§1.4 — THE ACCOUNTABILITY LOOP', '', '§HOW TO TEACH IT:', '',
  '§1. Name the default response.',
  'Say: "%s"' % on('Many organisations respond to performance gaps with one default response: they push harder. More urgency is applied. More pressure is introduced. Deadlines are reinforced. Pressure alone rarely solves execution challenges because pressure does not identify the underlying cause of the problem.'),
  'Say: "When a gap is identified, the leader activates the Accountability Loop: a structured diagnostic process designed to restore traction and ownership without collapsing into unproductive performance pressure. Most performance gaps emerge from one of three underlying conditions."', '',
  '§2. Teach the three root causes, one card at a time.',
  'Lack of accountability. Say: "%s Recovery: %s"' % (on(CA[0][2]), on(CA[0][3])),
  'Lack of skill. Say: "%s Recovery: %s"' % (on(CA[1][2]), on(CA[1][3])),
  'Misfit or structural constraint. Say: "%s Recovery: %s"' % (on(CA[2][2]), on(CA[2][3])),
  'Then say: "Leaders must distinguish between team members who cannot perform and those who will not. Inability needs development, and unwillingness needs accountability." (Journal, 7 January 2026, Professional Insights: Leadership)',
  'With the third card, say: "Avoid assuming that every negative outcome proves individual failure, or that every positive outcome proves sound practice." (Journal, 18 August 2026, Professional Insights: Strategy)', '',
  '§3. Keep the two conversations separate.',
  'Say: "%s"' % on('The performance conversation must remain separate from the role conversation. Performance discussions focus on progress toward outcomes. Role alignment discussions focus on placing individuals where their capabilities can generate the greatest organisational value. By maintaining this distinction, the organisation protects both fairness and clarity.'),
  'Say: "Accountability works when it is specific and behaviour-based. Vague, general assessments of character produce no specific correction." (Journal, 8 April 2026, Professional Insights: Culture)', '',
  '§4. Ask, now that the loop is taught.',
  'Ask: "Think of a performance gap in your area. Which of the three root causes sits behind it, and what evidence tells you so?" Take two or three answers in the chat.', '',
  '§ON THE PORTAL, AFTER THE TEACHING:',
  'Participants write the reflection at the foot of part 1.4: the stage of the Review–Realign–Restore Cycle a current gap sits in, and the root cause they would most likely diagnose.'])
R1 = reflection_slide('Section 1 Reflections', [('1.1', 'ref_1.1.png'), ('1.4', 'ref_1.4.png')], ['§SECTION 1 REFLECTIONS', '', '§HOW TO USE THIS SLIDE:', '',
  '§1. Show the slide and read the two prompts aloud.', rq('1.1'), rq('1.4'), '',
  '§2. Say what the reflections are for.', 'Say: "You write these reflections on the portal after the teaching, with as much depth as you can. They build the learning portfolio you receive at the end of the programme."', '',
  '§3. Set the standard.', 'Say: "Name a real measure, a real gap and a real root cause from your own function."', '',
  '§4. Bridge to Section 2.', 'Say: "You have seen how measurement makes execution visible and how the cycle restores it. Section 2 shows what happens when the review rhythm weakens."', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants write these reflections in Section 1 of the participant file, at the foot of parts 1.1 and 1.4.'])

# ═══ Section 2 ═════════════════════════════════════════════════════════════════════════════════════════
def opener(slide, title, slo, lines):
    t = texts(slide)
    set_text(t[3], tx(title)); set_text(t[5], tx(slo[0])); set_text(t[6], tx(slo[1]))
    set_notes(slide, lines)
s2 = S[8]
opener(s2, 'Why Performance Measurement Determines Execution Velocity', C.SLO2, ['§SECTION 2 · INTELLIGENCE — WHY', 'Why Performance Measurement Determines Execution Velocity', '',
  '§SECTION LEARNING OUTCOMES:', '1. ' + on(C.SLO2[0]), '2. ' + on(C.SLO2[1]), '', '§HOW TO OPEN THE SECTION:', '',
  '§1. Name the shift.', 'Say: "This section moves from measurement as a tool to measurement as a leadership discipline. The rhythm of review conversations is itself a strategic capability."', '',
  '§2. Preview the chain.', 'Say: "When that rhythm weakens, four consequences follow, and they are cumulative. Missed early warnings lead to diffused accountability; diffused accountability suppresses learning; suppressed learning erodes leadership credibility."', '',
  '§3. Say where it goes.', 'Say: "Section 5 returns to these four consequences. There, your group sets the decision points that guard against them."'])
set_text(texts(S[10])[0], '2.1 · Four consequences of weak review discipline')
# Carol rewrote the notes of her slide 10 (execution velocity and the four consequences, 12 October evening). Slide 10 leaves with part 2.1,
# so her notes move, word for word, to the four consequences slide, now 2.1.
src_b = S[9].notes_slide.notes_text_frame._txBody; dst_b = S[10].notes_slide.notes_text_frame._txBody
assert 'velocity of the flight' in S[9].notes_slide.notes_text_frame.text
for p in dst_b.findall(qn('a:p')): dst_b.remove(p)
for p in src_b.findall(qn('a:p')): dst_b.append(copy.deepcopy(p))
note_replace(S[10], [('2.1 — EXECUTION DISCIPLINE: THE REAL DIFFERENTIATOR (Core argument)', '2.1 — FOUR CONSEQUENCES OF WEAK REVIEW DISCIPLINE')])

# ═══ Section 3 ═════════════════════════════════════════════════════════════════════════════════════════
s3 = S[12]
SLO3 = ('Identify where the review and interpretation of performance evidence break down across functions.', 'Assess which breakdown is most prevalent in their own organisation.')
set_notes(s3, ['§SECTION 3 · EXTRAPOLATING — WHERE', 'Where Does Performance Measurement Break Down Across Functions?', '',
  '§SECTION LEARNING OUTCOMES:', '1. ' + on(SLO3[0]), '2. ' + on(SLO3[1]), '', '§HOW TO OPEN THE SECTION:', '',
  '§1. Give the provocation.', 'Say: "Most modern organisations have agreed goals and KPIs, dashboards, reporting tools, and performance frameworks. The breakdown usually occurs in how leaders review and interpret the measurement together."', '',
  '§2. Say what the section holds.', 'Say: "Part 3.1 gives the four gaps. Part 3.2 shows which executive roles most often feed each gap."', '',
  '§3. Name the question that runs through it.', 'Say: "The question for this section is: Is the chain of execution across our functions holding together?"'])
set_text(texts(S[13])[0], '3.1 · Four fractures in performance measurement')
note_replace(S[13], [('SECTION 3 · THE FOUR GAPS (select each gap in the file)', '3.1 — FOUR FRACTURES IN PERFORMANCE MEASUREMENT')])
# 3.2 · a copy of the 3.1 slide: each gap with the roles that most often feed it
s32 = duplicate(S[13]); t = texts(s32)
set_text(t[0], '3.2 · The CXO performance gap contributors')
gmap = {g: [c[0] for c in C.CXO if any(x[0] == g for x in c[3])] for g in (C.G_H, C.G_E, C.G_R, C.G_L)}
for sh, g in zip((t[2], t[4], t[6], t[8]), (C.G_H, C.G_E, C.G_R, C.G_L)): set_text(sh, ' · '.join(gmap[g]))
set_notes(s32, ['§3.2 — THE CXO PERFORMANCE GAP CONTRIBUTORS', 'Is the chain of execution across our functions holding together?', '', '§HOW TO TEACH IT:', '',
  '§1. Set up the part.', 'Say: "%s"' % on('The four fractures of part 3.1 rarely begin with one leader. Each executive role reviews performance in its own meetings and with its own evidence, and the habits in those reviews open one or two of the fractures. When these habits are not seen together, the chain of execution across functions weakens without anyone noticing.'), '',
  '§2. Teach the map on the slide.'] + ['%s: %s.' % (g.replace('The ', ''), ', '.join(gmap[g])) for g in (C.G_H, C.G_E, C.G_R, C.G_L)] + ['',
  '§3. Teach each role: how it reviews performance, what it does in those reviews and what happens as a result. Take the participants\' own roles first.'] +
  ['%s. %s' % (tx(c[2][1]), ' '.join('What the %s does: %s What happens as a result: %s (%s)' % (c[0].replace('CTO/CIO', 'CTO or CIO'), tx(x[1][1]), tx(x[2]), x[0].replace('The ', '')) for x in c[3])) for c in C.CXO] + ['',
  '§4. Close the part.', 'Say: "%s"' % on('No single role opens a fracture alone. The Alignment Brigade closes the four fractures when each leader sees how the habits in their own reviews feed them, and the executive team reviews the chain of execution together.'), '',
  '§5. Ask, now that the roles are taught.', 'Ask: "What is one habit in your own reviews, and which fracture does it open?" Ask participants to post their answer in the chat.', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants read the ten role cards in part 3.2 of their own file, their own role first, and answer the question on their own card for themselves.'])
R3 = reflection_slide('Section 3 Reflections', [('3.1', 'ref_3.1.png')], ['§SECTION 3 REFLECTIONS', '', '§HOW TO USE THIS SLIDE:', '',
  '§1. Show the slide and read the prompt aloud.', rq('3.1'), '',
  '§2. Say what the reflection is for.', 'Say: "You write this reflection on the portal after the teaching. Rate each gap honestly, then name the gap you are most responsible for closing."', '',
  '§3. Bridge to Section 4.', 'Say: "You have seen where the review of performance breaks down, and which roles feed each gap. Section 4 brings the executive team together around one view of enterprise execution."', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants complete this reflection in Section 3 of the participant file, at the foot of part 3.1.'])

# ═══ Section 4 ═════════════════════════════════════════════════════════════════════════════════════════
s4 = S[14]
opener(s4, 'Cross-Leadership Performance Intelligence', C.SLO4, ['§SECTION 4 · INTEGRATION — COLLECTIVE', 'Cross-Leadership Performance Intelligence', '',
  '§SECTION LEARNING OUTCOMES:', '1. ' + on(C.SLO4[0]), '2. ' + on(C.SLO4[1]), '', '§HOW TO OPEN THE SECTION:', '',
  '§1. Name the shift.', 'Say: "This section moves from function to enterprise. The question that guides it is the question of part 3.2: Is the chain of execution across our functions holding together?"', '',
  '§2. Say what the section holds.', 'Say: "Part 4.1 teaches the Enterprise Performance Intelligence Circle, EPIC: the three signals each leader brings from their PM review sheet. Part 4.2 takes one Key Result through the Accountability Loop in a role play."'])
s41 = S[16]
set_text(texts(s41)[0], '4.1 · The Enterprise Performance Intelligence Circle (EPIC)')
for sh, (a, b) in zip([x for x in texts(s41) if x.text_frame.text.startswith('Round')], (('Round 1', 'Signal 1'), ('Round 2', 'Signal 2'), ('Round 3', 'Signal 3'))):
    assert sh.text_frame.text == a; set_text(sh, b)
ES = C.EPIC_SIGNALS
set_notes(s41, ['§4.1 — THE ENTERPRISE PERFORMANCE INTELLIGENCE CIRCLE (EPIC)', 'Select each signal', '', '§HOW TO TEACH IT:', '',
  '§1. Say what EPIC is for.',
  'Say: "%s"' % on('The Enterprise Performance Intelligence Circle (EPIC) is the executive team’s structured review of enterprise execution. The question that guides EPIC is: “Is the chain of execution across our functions holding together?”'),
  'Say: "%s"' % on('Many organisations conduct performance reviews. Few organisations convert those reviews into collective strategic intelligence. EPIC ensures that insights emerging from PM review sheets are brought together across functions in a structured conversation that allows the Alignment Brigade to observe execution as a living system.'), '',
  '§2. Say what each leader brings.',
  'Say: "%s"' % on('In EPIC, each member of the executive team brings three signals from their own PM review sheet: where their Key Results stand, what is starting to break, and what execution is teaching them. Each signal answers one question, and the three are shared in that order. Progress comes first because it gives the warnings their context and the learning a system to learn about.'), ''] +
  sum([['§%d. Signal %d · %s: "%s"' % (k + 3, k + 1, s_[0], s_[1]),
        'Say: "Each leader brings: %s"' % on(s_[2]),
        'Say: "Each leader says it like this: %s"' % on(s_[3]),
        'Example: %s' % on(s_[4][0]),
        'Say: "What the executive team sees: %s"' % on(s_[5]), ''] for k, s_ in enumerate(ES)], []) +
  ['§6. Close on what EPIC produces.'] + ['%d. %s' % (i + 1, on(x)) for i, x in enumerate(C.EPIC_PRODUCES)] +
  ['Say: "%s"' % on('Through this practice, performance measurement becomes the organisation’s radar system for strategy execution.'), '',
   'Say: "Healthy organisations create conditions in which differentiated strengths work together. The test of collective culture: when one part suffers, others respond; when one succeeds, others celebrate." (Journal, 9 September 2026, Professional Insights: Culture)', '',
   '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants write their own three signals at the foot of each tab of part 4.1, from their own Key Results and KPIs.'])
# 4.2 · the role play (Carol's slide 21 moves into Section 4)
rp = S[20]
set_text(find(rp, '5.1 ·'), '4.2 · The Accountability Loop role play')
set_text(find(rp, 'Three roles'), 'Three roles: CXO · Team member · Observer. Diagnose before prescribing.')
set_notes(rp, ['§4.2 — THE ACCOUNTABILITY LOOP ROLE PLAY (PRACTICE IN CLASS)', '', '§HOW TO TEACH IT:', '',
  '§1. Give the case.', 'Say: "' + on(C.SCENARIO2.split('</p>')[0], 'f') + ' ' + on('The latest performance review shows that progress has stalled and complaint resolution is still averaging 36 hours. The target deadline is six weeks away.') + '"', '',
  '§2. Assign the three roles.',
  'CXO: "%s"' % on(C.ROLES[0][1], 'f'), 'Team member: "%s"' % on(C.ROLES[1][1], 'f'), 'Observer: "%s"' % on(C.ROLES[2][1].replace('the four criteria', 'the three criteria'), 'f'),
  'Brief the CXO with this line: "The leader who receives honest feedback about a genuine problem and responds with honesty before justification, and action before communication, creates the conditions for real leadership." (Journal, 29 June 2026, Professional Insights: Leadership)', '',
  '§3. Run the conversation.', 'The CXO opens with the evidence and diagnoses the root cause with the team member before any corrective action is discussed.',
  'If the CXO defaults to pressure and skips diagnosis, pause and redirect: "You have identified the gap. Now diagnose the cause. Is this an accountability issue, a skill gap, or a structural constraint? What evidence do you have for that?"', '',
  '§4. Close the conversation.', 'The CXO closes with the corrective actions, the follow-up and the alignment question.',
  'Say: "Accountability without a pathway back becomes punishment. Correct firmly where necessary, and deliberately restore trust, contribution and dignity when change is evident." (Journal, 16 September 2026, Professional Insights: Leadership)', '',
  '§5. Debrief.', 'The observer posts in the chat the root cause diagnosed (accountability, skill or structural), the evidence for it and how the conversation met each criterion.',
  'Ask the CXO: "If you ran this conversation again, what would you change first?"', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants complete personal Portfolio work in part 4.2 of their own file. They read a full conversation on the same case and work out how the CXO applied the cycle and the loop: the evidence used in Review, the root cause diagnosed in Realign and how the other two were ruled out, the corrective actions and the movement of the alignment score in Restore, and their own judgement against the three criteria.'], watch_ok=True)
cr = S[21]
set_text(texts(cr)[0], '4.2 · Evaluation criteria')
drop_shapes(cr, ['Shape 3', 'Image 1', 'Text 4'])
step = Emu(1223010 + 300000)
for k, (shp, img, txt) in enumerate((('Shape 1', 'Image 0', 'Text 2'), ('Shape 5', 'Image 2', 'Text 6'), ('Shape 7', 'Image 3', 'Text 8'))):
    d = {sh.name: sh for sh in cr.shapes}
    base = Emu(1508760) + step * k
    d[txt].top = base; d[shp].top = base + (1800225 - 1508760); d[img].top = base + (1960245 - 1508760)
set_text(find(cr, '03  '), '02  ', 'Root cause was correctly identified'); set_text(find(cr, '04  '), '03  ', 'Clear corrective actions were agreed')
CR = C.CRITERIA3
set_notes(cr, ['§4.2 — EVALUATION CRITERIA', '', '§HOW TO USE THIS SLIDE:', '',
  '§1. Brief the observer before the role play.'] + ['%s · %s: "%s"' % (a, b, on(c)) for a, b, c in CR] + ['',
  '§2. Use the criteria in the debrief.', 'The observer posts how the conversation met each criterion. Ask the room which criterion was hardest to meet, and why.',
  'Say: "Leaders who either conceal failure or weaponise it prevent learning. Mature accountability names what went wrong, understands why it happened and moves people toward responsible change." (Journal, 10 August 2026, Professional Insights: Leadership)',
  'Say: "Holding people accountable for outcomes without considering intent produces a culture of blame. Intent matters." (Journal, 17 March 2026, Professional Insights)', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'In part 4.2 of their own file, participants judge the scripted conversation against these three criteria.'], watch_ok=True)
R4 = reflection_slide('Section 4 Reflections', [('4.1', 'ref_4.1a.png'), ('4.1', 'ref_4.1b.png')], ['§SECTION 4 REFLECTIONS (1 OF 2)', '', '§HOW TO USE THIS SLIDE:', '',
  '§1. Show the slide and read the two prompts aloud.', rq('4.1a'), rq('4.1b'), '',
  '§2. Say what the reflections are for.', 'Say: "In part 4.1, you write your own EPIC signals, from your own Key Results and KPIs, with the evidence behind each. These reflections build your learning portfolio."', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants write their progress signal and their early warning signal at the foot of the first two tabs of part 4.1.'])
R4b = reflection_slide('Section 4 Reflections', [('4.1', 'ref_4.1c.png'), ('4.2', 'ref_4.2.png')], ['§SECTION 4 REFLECTIONS (2 OF 2)', '', '§HOW TO USE THIS SLIDE:', '',
  '§1. Show the slide and read the prompt and the Portfolio work aloud.', rq('4.1c'), '4.2 Portfolio work: the Accountability Loop case, read and analysed alone.', '',
  '§2. Say what the work is for.', 'Say: "In 4.2, you read a full Accountability Loop conversation on the case of the role play and work out how the CXO applied the cycle: the evidence in Review, the root cause in Realign, the corrective actions and the alignment score in Restore. This is personal work, and it builds your learning portfolio."', '',
  '§3. Bridge to Section 5.', 'Say: "You have seen the enterprise view and practised the loop on one Key Result. Section 5 brings back the four consequences of weak review discipline, and your group guards its own strategy against them."', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', 'Participants write their execution learning at the foot of the third tab of part 4.1, and complete the Portfolio work of part 4.2.'])

# ═══ Section 5 ═════════════════════════════════════════════════════════════════════════════════════════
s5 = S[18]
lead, steps_, tail = C.HOW_S5['f']
opener(s5, C.S5_TITLE, C.SLO5, ['§SECTION 5 · APPLICATION — IN PRACTICE', tx(C.S5_TITLE), '',
  '§SECTION LEARNING OUTCOMES:', '1. ' + on(C.SLO5[0]), '2. ' + on(C.SLO5[1]), '',
  '§HOW THIS SECTION RUNS:', on(lead, 'f')] + [on(x, 'f') for x in steps_] + [on(x, 'f') for x in tail] + ['',
  '§HOW TO OPEN THE SECTION:', '',
  '§1. Say what the section does.', 'Say: "' + on(C.S5_LEAD['p'], 'p') + '"', '',
  '§2. Say how the group works.', 'Say: "This is group work. Your group agrees each entry. One member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it."', '',
  '§3. Say where the work goes.', 'Say: "This is Capstone work. You read your group’s record at the foot of the section and select Confirm. Your confirmed record feeds your team’s Capstone Blueprint."'])
s51 = duplicate(S[10]); t = texts(s51)
set_text(t[0], '5.1 · Decision points against the four consequences')
for sh, (n, c) in zip(t[1:], enumerate(C.CONSEQ, 1)): set_text(sh, '0%d  ' % n, c[1] + '  ·  2 decision points')
set_notes(s51, ['§5.1 — DECISION POINTS AGAINST THE FOUR CONSEQUENCES (CAPSTONE WORK)', '', '§HOW TO TEACH IT:', '',
  '§1. Recall the four consequences of part 2.1.', 'Say: "Missed early warning signals. Gradual diffusion of accountability. Loss of organisational learning. Eroded leadership credibility. Each begins with signals that can be seen early."', '',
  '§2. Say what a decision point is.', 'Say: "A decision point names the signal the executive team watches for, the decision it takes when the signal appears and who takes it. Write it as one sentence: If the signal appears, then the decision, taken by whom."', '',
  '§3. Give one example for each consequence.'] + ['%s: "%s"' % (c[1], on(C.DP_EX[i])) for i, c in enumerate(C.CONSEQ)] + ['',
  '§4. Say how the group completes it.', 'Say: "Take the four consequences one at a time. For each, agree the two signals your executive team is most likely to miss in your strategy, and write one decision point for each."', '',
  '§ON THE PORTAL, AFTER THE TEACHING:', on(C.ACT_S5_F, 'f'), 'Each group writes two decision points for each of the four consequences: for each, the signal, the decision the executive team takes when it appears and who takes it.'])

# ═══ the new order; six slides leave ═══════════════════════════════════════════════════════════════════
lst = prs.slides._sldIdLst; ids = list(lst)
allS = list(prs.slides); by = {id(s): el for s, el in zip(allS, ids)}
order = [S[0], S[1], S[2], S[3], S[4], S[5], S[6], S[7], R1, S[8], S[10], S[12], S[13], s32, R3, S[14], S[16], S[20], S[21], R4, R4b, S[18], s51]
gone = [S[9], S[11], S[15], S[17], S[19], S[22]]
for s in gone: prs.part.drop_rel(by[id(s)].get(RID + 'id'))
for el in ids: lst.remove(el)
for s in order: lst.append(by[id(s)])
prs.save(out)
print(len(prs.slides), 'slides ->', out)
