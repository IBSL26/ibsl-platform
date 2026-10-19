# Consistency review of Units 2 to 9 · 19 October 2026

Carol: "So address all including committing pending work" (19 Oct, 10:44). Findings: `Claude outputs\Units 2 to 9 - Consistency review (findings).md`.
Review file (every changed sentence, before and after): `Claude outputs\Review files\Units 2 to 9 - Consistency changes (review).md`.
Backups of every page, deck and upload folder before the work: `Claude outputs\Backups\Consistency review 19 Oct\`.

## Order of the build (each step on the files left by the step before)
1. **Hygiene of 12 October, written live**: `Unit decks\_build\hygiene_12oct\hygiene_pages.py` on the live pages (Units 3 and 4 swap Sections 4 and 5; back link at the top left in Units 1, 2, 3; "Unit 3, part 4.x" → "5.x" in Units 5–7). Run from a copy with its last assert relaxed (the Unit 7 facilitator page holds no pointer). Unit 1 and Unit 4 pages came out with the same md5 as on 12 October.
2. **One pair of names for the two performance views**: `vocab.py` (ordered pairs) + `apply_vocab.py <portal> <out>` → Units 6–9 pages, decks (slides and notes), `capstone_P.html`. Unit 6 part 1.2 is kept word for word plus one sentence naming the pair; Unit 9 Section 2 untouched (parked). A replacement never rewrites text another pair wrote. Log: `Review files\vocab_log.json`.
3. **Rule fixes on the pages**: `fixes_pages.py <portal> <out>` (each pair must match its count). Log: `Review files\fixes_log.json`.
4. **Decks** (cloud workspace): `deck_fixes.py` (notes and slide text), `deck_pics.py` (new reflection pictures Unit 5 s31, Unit 6 s15; Unit 7 new slides 11, 12 and 17), `deck_fonts.py` (Unit 5 slides 32–34 at 24pt; Unit 3 not changed: its dense slides overflow at 24pt and need splitting). Pictures: `shoot_reflections_19oct.py`. Log: `Review files\deck_log.json`.
5. Upload copies = `Unit decks` masters (all eight); reader folders remade with `reader_assets.py` into a scratch folder, then copied over (the device shell cannot delete; no surplus pictures).
6. `node build_collection.js`; `node check_standards.js` (Units 2–9 left: Unit 3 Rule 16 only).
7. Tests: `rebuild_u06cm\e2e_u06cm.py` 20/20; `e2e_all.py` 40/40 (every Unit 2–9 page, reflections, Submit, Learning Portfolio, facilitator tabs); control with the save helper broken fails as it should.
