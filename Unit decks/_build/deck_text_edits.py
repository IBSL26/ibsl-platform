"""Apply exact text corrections to a unit deck: slide titles and presenter notes.

Usage: python3 deck_text_edits.py <deck_in.pptx> <edits.json> <deck_out.pptx>

edits.json: {"titles": [[slide, old, new], ...], "notes": [[slide, old, new], ...]}
A title edit must equal the whole text of one text run on that slide. A notes edit must occur
exactly once in the notes of that slide, inside one text run. The script stops, writing nothing,
if any edit does not match. Nothing else in the deck is touched.
"""
import json, sys
from pptx import Presentation
from pptx.oxml.ns import qn

def main(deck, spec, out):
    d = json.load(open(spec, encoding="utf-8"))
    prs = Presentation(deck)
    slides = list(prs.slides)
    for n, old, new in d.get("titles", []):
        ts = [t for t in slides[n - 1]._element.iter(qn("a:t")) if (t.text or "") == old]
        if len(ts) != 1:
            sys.exit(f"Slide {n} title: expected 1 run equal to {old!r}, found {len(ts)}")
        ts[0].text = new
    for n, old, new in d.get("notes", []):
        ts = [t for t in slides[n - 1].notes_slide._element.iter(qn("a:t")) if old in (t.text or "")]
        total = sum((t.text or "").count(old) for t in ts)
        if total != 1:
            sys.exit(f"Slide {n} notes: expected 1 match, found {total}: {old[:80]!r}")
        ts[0].text = ts[0].text.replace(old, new)
    prs.save(out)
    print(f"{len(d.get('titles', []))} title edits and {len(d.get('notes', []))} notes edits -> {out}")

if __name__ == "__main__":
    main(*sys.argv[1:4])
