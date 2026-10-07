"""Surgical edits to Carol's final Unit 3 deck (7 October 2026), on her word: five steps everywhere, four Objectives in the
worked example, Section 2 outcomes, and the notes wording that follows from these. Nothing else is touched.
Usage: python3 -I edit_deck.py <carol_deck.pptx> <out.pptx>"""
import sys, copy
from pptx import Presentation
from pptx.util import Inches
src, out = sys.argv[1:3]
prs = Presentation(src); S = list(prs.slides); log = []

def set_text(par, new):
    """Replace the text of a paragraph, keeping the formatting of its first run."""
    runs = par.runs
    runs[0].text = new
    for r in runs[1:]: r._r.getparent().remove(r._r)

def sub(pars, old, new, n=1):
    hits = 0
    for p in pars:
        if old not in p.text: continue
        done = False
        for r in p.runs:
            if old in r.text: r.text = r.text.replace(old, new); done = True
        if not done: set_text(p, p.text.replace(old, new))
        hits += 1
    assert hits == n, f'expected {n} paragraph(s) with {old!r}, found {hits}'
    log.append(f'{old!r} -> {new!r}')

def notes(i): return S[i - 1].notes_slide.notes_text_frame.paragraphs
def nsub(i, old, new, n=1): sub(notes(i), old, new, n); log[-1] = f'slide {i} notes: ' + log[-1]
def ndel(i, first, until):
    """Delete notes paragraphs from the one that contains `first` up to (not including) the one that contains `until`."""
    ps = notes(i); a = next(k for k, p in enumerate(ps) if first in p.text); b = next(k for k, p in enumerate(ps) if until in p.text and k > a)
    for p in ps[a:b]: p._p.getparent().remove(p._p)
    log.append(f'slide {i} notes: removed {b - a} paragraphs from {first!r}')
def shape_text(i, old, new):
    for sh in S[i - 1].shapes:
        if sh.has_text_frame and old in sh.text_frame.text:
            sub(sh.text_frame.paragraphs, old, new); log[-1] = f'slide {i}: ' + log[-1]; return
    raise AssertionError(f'slide {i}: {old!r} not found')
def drop(i, idxs):
    shapes = list(S[i - 1].shapes)
    for k in idxs: shapes[k]._element.getparent().remove(shapes[k]._element)
    log.append(f'slide {i}: removed {len(idxs)} shapes')

# ── Slide 7: "SiP" as written everywhere else
shape_text(7, 'KISS Application Across SIP Domains', 'KISS Application Across SiP Domains')
nsub(7, 'Position the SIP Domains.', 'Position the SiP Domains.')

# ── Slide 9: five steps
shape_text(9, '1.5 · Six Steps: From KISS to Enterprise OKRs', '1.5 · Five Steps: From KISS to Enterprise OKRs')
sh = list(S[8].shapes)
assert 'Step 5 · Enterprise Priority' in sh[15].text_frame.text and 'Step 6 · Priority Matrix' in sh[18].text_frame.text
sub(sh[18].text_frame.paragraphs, 'Step 6 · Priority Matrix', 'Step 5 · Priority Matrix')
rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (16, 17, 18)]
pitch = 5.35 / 5
for r, (b, im, tx) in enumerate(rows):
    y = 1.65 + r * pitch
    sh[tx].top = Inches(y); sh[tx].height = Inches(pitch)
    sh[b].top = Inches(y + (pitch - 0.62) / 2); sh[im].top = Inches(y + (pitch - 0.62) / 2 + 0.155)
drop(9, [13, 14, 15])
nsub(9, '1.5 — SIX STEPS: FROM KISS OUTPUT TO ENTERPRISE OKRs (6 STEPS)', '1.5 — FIVE STEPS: FROM KISS OUTPUT TO ENTERPRISE OKRs (5 STEPS)')
nsub(9, 'Six steps carry the KISS output into enterprise OKRs.', 'Five steps carry the KISS output into enterprise OKRs.')
ndel(9, '6. Step 5 — Enterprise Priority.', '7. Step 6 — Priority Matrix.')
nsub(9, '7. Step 6 — Priority Matrix.', '6. Step 5 — Priority Matrix.')
nsub(9, 'The last step places each enterprise priority on the Prioritisation Matrix', 'The last step places each aligned OKR on the Prioritisation Matrix')
nsub(9, '8. Show how the steps chain.', '7. Show how the steps chain.')
nsub(9, 'Steps 4 to 6 test, select and place what Steps 1 to 3 produce.', 'Steps 4 and 5 test and place what Steps 1 to 3 produce.')
nsub(9, '9. Bridge to the matrix.', '8. Bridge to the matrix.')
nsub(9, 'We now look at Step 6 in detail.', 'We now look at Step 5 in detail.')

# ── Slide 10
shape_text(10, '1.5 · Step 6: the Prioritisation Matrix', '1.5 · Step 5: the Prioritisation Matrix')
nsub(10, '1.5 — STEP 6: THE PRIORITISATION MATRIX (IMPACT × EFFORT)', '1.5 — STEP 5: THE PRIORITISATION MATRIX (IMPACT × EFFORT)')
nsub(10, 'and the six-step path to connect them.', 'and the five-step path to connect them.')

# ── Slide 12: Section 2 outcomes (Carol's wording)
O = ('Explain why an honest review of current practice must precede the setting of priorities.', 'Recognise the cost of setting targets before the path to the future state is understood.')
N = ('Recognise the benefits of mapping the terrain before setting goals.', 'Practise the translation of SiP into OKRs.')
for o, n_ in zip(O, N): shape_text(12, o, n_); nsub(12, o, n_)
nsub(12, 'then one worked example on five slides: the SiP statement, its KISS table, Steps 1 and 2, Steps 3 and 4, Steps 5 and 6.', 'then one worked example on seven slides: the SiP statement, its KISS table, then Steps 1 to 5 on one slide each.')

# ── Slides 17 and 18: four themes, four Objectives
sh = list(S[16].shapes); assert sh[27].text_frame.text == 'Key account growth' and sh[25].text_frame.text == '05'
shape_text(17, 'five recurring strategic themes emerge', 'four recurring strategic themes emerge')
for r in range(4):
    for k in range(8 + 4 * r, 12 + 4 * r): sh[k].top = sh[k].top + Inches(0.21 * r)
drop(17, [24, 25, 26, 27])
sh = list(S[17].shapes); assert sh[21].text_frame.text == 'Key account growth' and sh[22].text_frame.text.startswith('5: ')
for r in range(4):
    for k in range(8 + 3 * r, 11 + 3 * r): sh[k].top = sh[k].top + Inches(0.21 * r)
drop(18, [20, 21, 22])

# ── Slide 21: Step 5 is the matrix
nsub(21, '2.2 — WORKED EXAMPLE · STEPS 5 AND 6: ENTERPRISE PRIORITY AND THE MATRIX', '2.2 — WORKED EXAMPLE · STEP 5: THE PRIORITISATION MATRIX')
nsub(21, 'Step 6 — Priority Matrix.', 'Step 5 — Priority Matrix.')
nsub(21, 'Each enterprise Objective is placed on the Prioritisation Matrix by Impact and Effort.', 'Each aligned Objective is placed on the Prioritisation Matrix by Impact and Effort.')

# ── Slide 31: five steps in 4.2
shape_text(31, '4.2 Translating KISS to OKRs: The Six Steps', '4.2 Translating KISS to OKRs: The Five Steps')
nsub(31, '4.2 — TRANSLATING KISS TO OKRs: THE SIX STEPS (6 STEPS · GROUP WORK)', '4.2 — TRANSLATING KISS TO OKRs: THE FIVE STEPS (5 STEPS · GROUP WORK)')
nsub(31, 'through the six steps of 1.5.', 'through the five steps of 1.5.')
nsub(31, 'Your group records up to six themes.', 'Your group records up to four themes.')
nsub(31, 'your group writes two or three Key Results in the formula', 'your group writes up to two Key Results in the formula')
ndel(31, '6. Step 5 — Enterprise Priority.', '7. Step 6 — Priority Matrix.')
nsub(31, '7. Step 6 — Priority Matrix.', '6. Step 5 — Priority Matrix.')
nsub(31, 'Place each enterprise priority on the matrix by its Impact and its Effort.', 'Place each aligned OKR on the matrix by its Impact and its Effort.')
nsub(31, '8. Explain confirmation.', '7. Explain confirmation.')
nsub(31, 'the group works through the six steps:', 'the group works through the five steps:')
nsub(31, 'records up to six themes from its confirmed KISS map;', 'records up to four themes from its confirmed KISS map;')
nsub(31, 'writes two or three Key Results for each Objective, with the contributing roles;', 'writes up to two Key Results for each Objective, with the contributing roles;')
ndel(31, 'chooses no more than four Objectives as enterprise priorities;', 'places each priority on the Prioritisation Matrix;')
nsub(31, 'places each priority on the Prioritisation Matrix;', 'places each aligned OKR on the Prioritisation Matrix;')
ndel(31, '- Step 5: enforce the Less is More Rule', '- Step 6: as the team debates placements')
nsub(31, '- Step 6: as the team debates placements', '- Step 5: as the team debates placements')

# ── Slide 32: a stray full stop under the second outcome
for shp in S[31].shapes:
    if shp.has_text_frame and len(shp.text_frame.paragraphs) == 2 and shp.text_frame.paragraphs[1].text == '.':
        p2 = shp.text_frame.paragraphs[1]._p; p2.getparent().remove(p2); log.append('slide 32: stray "." removed under outcome 2')

# ── Other notes: five steps, portfolio work, limits
nsub(1, 'The matching exercise in Section 3 and the game in Section 5 are individual work.', 'The matching exercise in Section 3 and the game in Section 5 are portfolio work.')
nsub(1, 'The six-step path is the core of the unit.', 'The five-step path is the core of the unit.')
nsub(2, 'the six steps and the Prioritisation Matrix', 'the five steps and the Prioritisation Matrix')
nsub(3, 'and the six steps from KISS output to enterprise OKRs.', 'and the five steps from KISS output to enterprise OKRs.')
nsub(3, 'through KISS and the six steps.', 'through KISS and the five steps.')
nsub(3, 'follows the 6 steps to convert to prioritised OKRs', 'follows the five steps to convert to prioritised OKRs')
nsub(4, '1.5: the six steps from KISS output to enterprise OKRs, then Step 6 in detail', '1.5: the five steps from KISS output to enterprise OKRs, then Step 5 in detail')
nsub(8, 'Six steps connect them.', 'Five steps connect them.')
nsub(14, 'then through the six steps.', 'then through the five steps.')
nsub(16, 'Bridge to the six steps.', 'Bridge to the five steps.')
nsub(16, 'The six steps now turn it into enterprise OKRs.', 'The five steps now turn it into enterprise OKRs.')
nsub(29, 'Translating KISS to OKRs through the six steps.', 'Translating KISS to OKRs through the five steps.')
nsub(33, 'This is individual work.', 'This is portfolio work.')
nsub(34, 'Six steps then carry the KISS output into enterprise OKRs.', 'Five steps then carry the KISS output into enterprise OKRs.')
nsub(34, 'through the six steps.', 'through the five steps.')
nsub(34, 'maximum 4 Objectives, maximum 3 Key Results each (4.2)', 'maximum 4 Objectives, maximum 2 Key Results each (4.2)')

prs.save(out)
print(len(log), 'edits'); print('\n'.join(log))
