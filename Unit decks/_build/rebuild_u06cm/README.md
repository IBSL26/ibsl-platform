# Unit 6 rework — 14 October 2026 (Carol's "Amended content.docx")

Source: `Claude outputs\Amended Unit Content\Amended content.docx` and her instruction of 14 October, 19:07: change Unit 6 in both files and the PPT; notes in the approved format, carrying all facilitator content; participant streamlined; personal reflections on contributions and FACES (Learning Portfolio); Section 5 goes into the Capstone.

| File | What it does |
|---|---|
| `u6cm_content.py` | All content in two voices (facilitator 'f' keeps every word of her text and Facilitator Guidance; participant 'p' streamlined, "you"). `RULE_FIXES` lists her sentences reworded for the house rules; lines marked NEW are Claude's. |
| `build_u06cm.py <p before> <f before> <p out> <f out>` | Builds both pages from the live pages (backups `… - before Contribution Map rework (14 Oct)`). |
| `u6cm_p.js`, `u6cm.css` | Section 5 tool (Activity 1 Contribution Map, Activity 2 FACES; one record, Confirm, Print) and styles. |
| `test_u06cm.py <preview folder>` | 57 browser checks on the PREVIEW pages (make them with `rebuild_u06\make_previews.py`). |
| `shoot_reflections_u06cm.py`, `pics\` | Pictures of the four reflections for the reflection slides. |
| `deck_u06cm.py <her deck 19c48b04…> <f page> <pics> <out>` | 34-slide deck on top of her 28-slide deck; notes in the approved format. |
| `check_notes_cover.py <f page> <deck>` | Lists facilitator-page sentences not found in the notes (remaining ones are headings, labels and paraphrased lines). |

Response keys (`u3m1_lens5`): reflections `ref13` (1.2), `ref12` (3.2, kept), `ref14` (4.1), `ref15` (4.2). Section 5: `__cm_work`, `cm_record`; on Confirm `cm_map`, `cm_faces` and names "Enterprise PM System · Contribution Map", "Enterprise PM System · FACES Application". No longer written: `ref1`–`ref4`, `ref6`, `ref7`, `ref11`, `__pm_work`, `pm_*`.

Go-live, after her approval: live pages; `capstone_P.html` Unit 6 boxes become two (6A S2R® Contribution Map™, 6B FACES application) via `PULL.u6` from `cm_map`, `cm_faces`; SQL box count u6 4 → 2 (model `Claude outputs\capstone_unit6_boxes.sql`); `dashboard_F.html` labels for `ref13`–`ref15`, `cm_*`; `build_collection.js` `CAPSTONE_KEYS.u3m1_lens5`; `node build_collection.js`; end-to-end test (`rebuild_u06\e2e_u06.py` adapted); deck reader folder; upload copy; Capability Blueprint document boxes 6A–6D → 6A–6B.

## Live (14 October 2026, evening) — Carol: "OK LOOKS GOOD BUILD LIVE FILES"
- Review rounds: reflections moved to 1.3 and 1.4; long sub-parts, tables and long cards collapse and open when selected (every sub-part after a collapsed one collapses too); short cards side by side; Objective then Key Result drop-downs in Section 5; Section 5 guidance tables removed from the participant page; "Integrating" → "Integration of …" (Rule 2) and "instead of" → "against a standard of" (Rule 13).
- Written: unit3_m1_lens5_p.html 03d96230…, unit3_m1_lens5_f.html 50c7f7a4…, capstone_P.html 2225d9bd… (6A S2R® Contribution Map™, 6B FACES application, PULL.u6 from cm_map, cm_faces), dashboard_F.html 37705aa8…, build_collection.js cf1208ff…, collection.html dc2b649e…; deck 5905d5c4… (33 slides) in Unit decks and Deck upload\Module-3\unit-06.pptx with 33 pictures and manifest.json in unit-06.
- Tests: test_u06cm.py 67/67 on previews; e2e_u06cm.py 20/20 on the real pages with rebuild_u06\fake-supabase.js (control without the 6A PULL row fails 3 checks). check_standards: no Unit 6 breach.
- For Carol: SQL `Claude outputs\capstone_unit6_boxes_cm.sql` (u6 4 → 2); commit and push; Storage upload of unit-06.pptx and the unit-06 folder (5 new pictures s29–s33).
- Still to do: S2R® Capability Blueprint document lists boxes 6A–6D; update to 6A–6B when the Capstone is built.
