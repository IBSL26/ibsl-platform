# Unit 8 amendments — 12 October 2026

Unit 8 is "Performance Measurement": `unit3_m2_lens7_p.html` (participant), `unit3_m2_lens7_f.html` (facilitator), `Unit decks\Unit 08 - Performance Measurement.pptx` (deck). Lens id `u3m2_lens7`.

Source of the changes: the three-way match of 12 October (`Claude outputs\Unit 8 - Three-way match (findings).md`), approved by Carol, then her amendments at 13:10, 21:52 and 22:14. Approved at 22:49 ("Am happy with this framing. You can build the live files and the PPT").

| File | What it does |
|---|---|
| `u8_content_r1.py` + `u8_sections.py` | The content in two voices. `u8_content.py` is the two joined (`cat u8_content_r1.py u8_sections.py > u8_content.py`); later definitions replace earlier ones. |
| `build_u08.py <p before> <f before> <p out> <f out>` | Builds both pages from the backups in `Claude outputs\Backups\Unit 8 file backups` (md5 14234cb6…, 82ed5273…). |
| `u8_p.js`, `u8.css` | Section 5 tool (four tabs, two decision points each, one record, Confirm, Print) and the 3.2 role cards. |
| `make_previews_u08.py`, `mock-s2r.js`, `test_u08.py` | PREVIEW copies and browser checks (34 pass). |
| `shoot_reflections_u08.py` | Pictures for the reflection slides (`_build\reflections\u08`). |
| `carol_deck_u08_r2.py <Carol's deck> <p> <f> <pictures> <out>` | Works on top of Carol's own deck (md5 1cd2dd99…, kept in `Backups\Unit 8 deck backups`): 23 slides. Her slide 10 notes (execution velocity) move to the 2.1 slide. |
| `patch_links_u08.py` | `capstone_P.html` (Unit 8 four boxes 8A–8D, `PULL.u8`), `dashboard_F.html` (labels, two headings), `build_collection.js` (`CAPSTONE_KEYS.u3m2_lens7`). Then `node build_collection.js`. |
| `e2e_u08.py <site> <fake-supabase.js>` | End to end with a stand-in database: 25 of 25 pass. |

## The unit
1.1 The Execution Visibility Infrastructure · 1.2 The Four Strategic Purposes · 1.3 From Performance Measurement to Execution Recovery · 1.4 The Accountability Loop · 2.1 Four Consequences of Weak Review Discipline · 3.1 Four Fractures in Performance Measurement · 3.2 The CXO Performance Gap Contributors · 4.1 EPIC (three signals) · 4.2 The Accountability Loop Role Play (participant: personal analysis of a scripted conversation) · 5.1 Decision Points Against the Four Consequences (group, Capstone).

## Response keys (u3m2_lens7)
Reflections `ref1`, `ref2`, `ref4` (3.1 rating), `ref5`–`ref7` (EPIC signals) · 4.2 Portfolio work `rp_review`, `app_rootcause`, `app_corrective`, `rp_judge` · Section 5 `__rd_work`, `rd_record`; on Confirm `rd_warning`, `rd_accountability`, `rd_learning`, `rd_credibility` and the four "Review Discipline · …" names in `confirmed_items`. No longer written (old answers stay): `team_name`, `ref3`, `app_syn_*`, `app_loop_reflection`.

## Database
Unit 8 Capstone has four boxes: `Claude outputs\capstone_unit8_boxes.sql` (tested in pglite: u8 → 4, every other unit unchanged, safe to run twice).
