# -*- coding: utf-8 -*-
"""Replace "Alignment Brigade" in a unit deck (slide text, tables and notes), paragraph by paragraph, with the rules of brigade.py.
Usage: python3 deck_brigade.py <deck in> <deck out>. Only paragraphs that contain the phrase change; every other part of the deck stays as saved."""
import sys, re
from pptx import Presentation
from brigade import fix
src, out = sys.argv[1:3]
prs = Presentation(src); n = 0
def paras(s):
    for sh in s.shapes:
        if sh.has_text_frame: yield from sh.text_frame.paragraphs
        if getattr(sh, 'has_table', False) and sh.has_table:
            for c in sh.table.iter_cells(): yield from c.text_frame.paragraphs
    if s.has_notes_slide: yield from s.notes_slide.notes_text_frame.paragraphs
for i, s in enumerate(prs.slides, 1):
    for p in paras(s):
        full = ''.join(r.text for r in p.runs)
        if not re.search('(?i)brigade', full): continue
        hit = [r for r in p.runs if re.search('(?i)alignment brigade', r.text)]
        if hit and all(not re.search('(?i)brigade', r.text) or r in hit for r in p.runs):
            for r in hit: r.text = fix(r.text)      # the phrase sits inside single runs: keep each run's formatting
        else:
            new = fix(full); p.runs[0].text = new   # the phrase spans runs: join the paragraph in its first run
            for r in p.runs[1:]: r.text = ''
        print('slide', i, '|', ''.join(r.text for r in p.runs)[:150]); n += 1
for s in prs.slides:
    for p in paras(s): assert not re.search('(?i)brigade', ''.join(r.text for r in p.runs)), ''.join(r.text for r in p.runs)
prs.save(out); print(n, 'paragraphs changed ->', out)
