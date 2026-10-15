# Unit 8 · the two performance views — 15 October 2026 (PREVIEW stage)

Source: Carol's section-by-section locks, recorded in `Claude outputs\Review files\Unit 8\Unit 8 two views - locked amendments.md`.
Backups: `Claude outputs\Backups\Unit 8 file backups\… - before two performance views (15 Oct)` (p 010c3abf…, f f38984cd…, capstone_P f0c01984…) and `Unit 8 deck backups\Unit 08 - before two performance views (15 Oct).pptx` (e3408c4a…).

```
python3 build_u08pv.py <live p> <live f> out/unit3_m2_lens7_p.html out/unit3_m2_lens7_f.html
python3 ..\rebuild_u08\make_previews_u08.py out\unit3_m2_lens7_p.html out\unit3_m2_lens7_f.html ..\rebuild_u08\mock-s2r.js "<Review files>\Unit 8"
python3 test_u08pv.py "<Review files>\Unit 8"          (53 checks)
python3 shoot_refs.py   (pictures r11, r21, r32 from the participant PREVIEW)
python3 deck_u08pv.py "<her deck e3408c4a>" pics "<Unit decks>\Unit 08 - Performance Measurement.pptx"
```

What changed: header sentence; S1 human/organisation cards (1.1 ×2, 1.2 ×4, 1.3 ×3) + R3 lines; S2 deep two-side cards in the four consequences; S3 implications in the four gaps; 3.2 map removed, new Portfolio reflection ref9; 4.2 rebuilt (open role play in threes + new CFO / Credit Control Manager case, GROW reworded); S5 How box, per-tab steps, labels "Individuals" / "Organisational conditions", examples reframed; facilitator guidance S1–S5 summarised (detail in slide notes); Unit Summary both pages.
Keys: ref9 added to KEYS. Section 5 keys unchanged (u8_c1_dp1 … u8_c4_dp2, rd_*), Capstone stays four boxes, no SQL.

Go-live (after her word): live pages; capstone_P.html 8A–8D descriptions ("For [consequence]: the potential gap and the decision point for recovery, for the performance of individuals and for the organisational conditions."); dashboard_F.html label for ref9 (3.2 · The Fracture You Are Most Prone To); node build_collection.js; e2e with control; deck reader folder from the final deck + Deck upload\Module-3\unit-08.pptx; check_standards.

## Live (15 October 2026, 20:08) — Carol: "build live files"
- Written: unit3_m2_lens7_p.html 4d5b51fb…, unit3_m2_lens7_f.html e5eee294…, capstone_P.html 1bafa5c6… (8A–8D descriptions; PULL.u8 unchanged), dashboard_F.html d6915376… (ref9 label, numbered map 9, four 4.2 labels reworded), collection.html a3b4ed98… (node build_collection.js; Unit 8: 21 prompts, 0 fallbacks). build_collection.js unchanged.
- Deck: Unit decks and Deck upload\Module-3\unit-08.pptx identical (a14238ce…, 24 slides); unit-08 folder: s01–s24 + manifest.json remade (same count, nothing surplus).
- Tests: test_u08pv.py 53/53 on previews; e2e_u08pv.py 25/25 on the real pages with rebuild_u06\fake-supabase.js (two controls). check_standards: no Unit 8 breach.
- Database: no SQL (Unit 8 keeps 4 boxes).
