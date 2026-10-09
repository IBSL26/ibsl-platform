# Unit 6 amendments — 9 October 2026

Unit 6 is "Performance Management Setup": `unit3_m1_lens5_p.html` (participant), `unit3_m1_lens5_f.html` (facilitator), `Unit decks\Unit 06 - Performance Management Setup.pptx` (deck). Lens id `u3m1_lens5`.

Source of the changes: Carol's amendments of 9 October (after `Claude outputs\Unit 6 - Three-way match (findings).md`), in her words in `Claude outputs\Handover - Unit 6.md`, section 9.

**State on 9 October (evening):** Carol gave her word ("build live pages"). The two pages, the three link files, `collection.html` and the SQL file are written to the portal folder (see "Written to the portal folder" at the foot). The deck with the new Section 5 slides is in `Claude outputs\Deck upload\Module-3`; it is not yet in `Unit decks` because her deck was open in PowerPoint. Carol commits, pushes and runs the SQL.

| File | What it does |
|---|---|
| `u6_content.py` | The content: Carol's text for 1.4, 1.5, 2.2, 4.1 and Section 5, the PPT-notes detail she asked for (2.1, 2.2, 2.3, 3.1), the two voices (participant "you", facilitator "participants"), the Section 5 entries, the Unit Summary. Lines marked NEW are Claude's wording. |
| `build_u06.py <p before> <f before> <p out> <f out>` | Builds both pages from the files before the amendments. Each cut and replacement checks that it finds its place once and stops on a miss. |
| `u6_p.js` | Participant tool for Section 5: four steps, the record, Confirm and Print, the Unit 3 Enterprise OKRs read only. Written into the participant page by the build. |
| `u6.css` | Styles added to both pages. |
| `make_previews.py <p> <f> mock-s2r.js <folder>` | Stand-alone PREVIEW copies (the participant copy saves in the browser only). Never commit or upload them. |
| `mock-s2r.js` | Stand-in save for the previews, with a sample of a member's confirmed Unit 3 Enterprise OKRs (the Unit 3 worked example). |
| `test_u06.py <preview folder> [<screenshot folder>]` | Browser checks (Playwright): 100 checks, all pass. |

Input for the build: `Claude outputs\Backups\Unit 6 file backups\unit3_m1_lens5_[p|f] - before amendments (9 Oct).html` (md5 62d58d3a… and dca86076…). Run from this folder:

```
python3 build_u06.py "<backup p>" "<backup f>" out_p.html out_f.html
python3 make_previews.py out_p.html out_f.html mock-s2r.js "<Review files>"
```

## The unit as the review files show it

- **Section 1:** 1.1 · 1.2 · 1.3 unchanged ("performance management (PM)" at first mention) · **1.4 Leader's Response** (was The 1–5 Rating Scale): Carol's introduction, in full on the facilitator page and in the participant's voice on the participant page; the five rating cards in the fuller wording on both pages, "PIP" spelled out · **1.5 The Impact of a Calibrated System** (new): the no-surprise review and the three shifts.
- **Section 2:** **2.1** beefed up from the PPT notes (slides 10 and 11): three opening paragraphs, the line of sight, an "In practice" line on each bridge · **2.2** opens in Carol's order: the two orientations, the S2R® position (PPT notes, slide 12), her compliance-driven and commitment-driven lists, then "The choice is rarely made explicitly — but it is always made…", then the six dimensions · **Rules of the Game removed** · **2.3 Leader vs Team** (was 2.4): the one-line distinction and the example from the PPT notes (slide 14), and Carol's new reflection (`ref11`).
- **Section 3:** **3.1 Unity in Diversity** (the old 3.1 The Alignment Brigade and 3.2 CXO Hot Zones as one part): the Brigade image (PPT notes, slide 16), the ten role cards with natural bias, hot zone, PM contribution and alignment contribution (PPT notes, slide 17) on both pages; the Your Enterprise Signal reflection removed; Your Hot Zone reflection (`ref6`) at the end · **3.2 The Three Execution Gaps** (was 3.3) · **3.3 The Continuous PM Shift** (was 3.4) with Carol's new reflection (`ref12`).
- **Section 4:** one part, **4.1 The EXECUTION Framework**: Carol's FACES and EXECUTION distinction, then the nine principles as learning content (principle and self-check question). No scoring. The Collective Progress Signal and Three Elements of Enterprise PM Design are removed.
- **Section 5 · Designing the PM Architecture:** group work, Capstone work, four steps: Step 1 Scoring Logic (five ratings × performance level, evidence, leadership response; contextual factors; three lines of sight; review cadence and why) · Step 2 FACES (five boxes) · Step 3 EXECUTION (nine boxes) · Step 4 PM Scorecards (two Key Results chosen from the group's Unit 3 Enterprise OKRs; a scorecard for the CEO and one for the CFO: Key Result 1, Key Result 2, operational, behavioural and values, each with a measure and a weight; the four weights add up to 100%). One record, Confirm and Print. The MyHealth Live Portal case and the 30-day commitment are gone.
- **Facilitator page:** preparation only, no entry box, no times, online wording, 17 FACILITATOR GUIDANCE boxes and 12 PARTICIPANT ACTIVITY notes (eight reflections, four steps).

## Response keys (lens `u3m1_lens5`, no database change for the pages)

- Reflections: `ref1`, `ref2`, `ref3`, `ref4`, `ref6`, `ref7` unchanged; new `ref11` (2.3) and `ref12` (3.3). Each question carries `class="ref-prompt"`.
- Section 5: `__pm_work` (the 53 entries), `pm_record` (all, as text) while the group works; on Confirm `pm_scoring`, `pm_faces`, `pm_execution`, `pm_scorecards` and `confirmed_items` names "PM Architecture · Scoring Logic", "· FACES", "· EXECUTION", "· Scorecards". An edit after Confirm removes the names.
- Step 4 reads the member's own Unit 3 page (`u2m1_lens2`): `__okr_work` and `confirmed_items` holding "Enterprise OKRs".
- No longer written (old answers stay in the database): `ref5`, `ref8`, `ref9`, `ref10`, `app_scorecard`, `app_scoring`, `app_baseline`, `app_cadence`, `app_measures`, `app_tool`.

## Go-live list (after Carol's word)

1. Write the two live pages from the build.
2. `capstone_P.html`: Unit 6 boxes become four (6A Scoring logic, 6B FACES, 6C EXECUTION, 6D PM scorecards · CEO and CFO), brought in through `PULL.u6` from `pm_scoring`, `pm_faces`, `pm_execution`, `pm_scorecards`.
3. Database: `capstone_section_box_count('u6')` from 5 to 4 (SQL for Carol, read-only check of the live function first; model `Claude outputs\capstone_unit5_boxes.sql`).
4. `dashboard_F.html`: labels for `ref11`, `ref12` and the `pm_*` keys, a heading for them in `FAMILY_DEFS`, "Confirmed by the group" for `confirmed_items`.
5. `build_collection.js`: `CAPSTONE_KEYS.u3m1_lens5` leaves the group work out of the Learning Portfolio; rebuild `collection.html`.
6. Deck: rebuild in the format of the Unit 2 to 5 decks from the approved pages; reader pictures.
7. One final scan (adapt `rebuild_u05\final_scan.py`), `node check_standards.js`, then the commit lines.

## For Carol's word (reported to her on 9 October)

- Section 4 holds EXECUTION only, as she said. That removed 4.2 Three Elements of Enterprise PM Design (the cumulative progress formula and its reflection) together with 4.1.
- Both Section 4 learning outcomes and the second Section 5 outcome describe content that has left. Outcomes are hers.
- Two of her 1.4 sentences were reworded for her no-contrast rule (`RULE13` in `u6_content.py`).
- The example in 2.3 leaves out "(the −0.42 hours of improvement per week)".
- NEW wording by Claude: the Section 5 title and opening, the how-to boxes, the placeholders, the facilitator guidance of 1.5, 4.1 and Section 5, the PARTICIPANT ACTIVITY notes, Unit Summary blocks 4 and 5, the facilitator closing question, the labels of the two new reflections.

## Written to the portal folder (9 October, evening)

| File | md5 | What changed |
|---|---|---|
| `unit3_m1_lens5_p.html` | 5d59c4c5d0b3766903b611bd084b38be | the build above |
| `unit3_m1_lens5_f.html` | 9ade80773b2807e7e0f2c2dc03f83f04 | the build above |
| `capstone_P.html` | 6f9e241ae0e2312b94e640fa4389cc08 | Unit 6 has four boxes (6A Performance scoring logic, 6B FACES of the PM architecture, 6C EXECUTION of the PM architecture, 6D PM scorecards · CEO and CFO), all brought in through `PULL.u6` |
| `dashboard_F.html` | 716fcd6e3d4a0333b65dda66e0fb87cb | heading "Designing the PM Architecture"; labels for `ref11`, `ref12`, `pm_*`, `confirmed_items` (labels of old answers stay) |
| `build_collection.js` | 9c9ba38605236ec1db681493cebdee70 | `CAPSTONE_KEYS.u3m1_lens5` |
| `collection.html` | de88dfd1cf4de00e0b280d6ebfa3652b | rebuilt with `node build_collection.js` (Unit 6: 5 arc segments, 62 prompts, 0 fallbacks) |
| `Claude outputs\capstone_unit6_boxes.sql` | d02e3d75330f2dedcf83d8e9d3f1fdde | three blocks; Unit 6 box count 5 → 4, every other unit keeps its value; tested in a local stand-in database |

`patch_links_u06.py <folder> <out>` makes the three link changes from the files in `Claude outputs\Backups\Unit 6 file backups\… - before Unit 6 links (9 Oct)`.
`node check_standards.js` on the folder: no page breach (Rule 16 lines are decks only).

## The deck: Carol's file is the master

Carol amended Sections 1 to 4 of the deck herself (27 slides, md5 bf0490ba…, kept as `Claude outputs\Backups\Unit 6 deck backups\… - Carol's own deck as saved (9 Oct 16h40).pptx`) and said: "Use the current unit 6 in Unit Decks to update just section 5 slides. I have already amended all the sections."

`carol_deck_s5.py <her deck> <p page> <f page> <out.pptx>` changes only: the Section 5 opener (title, notes) · "The six design tasks" → Step 1 · Scoring Logic · a copy of her 1.2 slide → Step 2 · FACES · a copy of her 4.1 slide → Step 3 · EXECUTION · the case slide → Step 4 · PM Scorecards · the Task 3 slide removed · the closing slide (closing question of the facilitator page; the 30-day commitment has left). Slides 1 to 22 are untouched, text and notes. Result: 28 slides, md5 570180bcc5d324eda4eed069f2a2cd3a, in `Claude outputs\Deck upload\Module-3\unit-06.pptx` with 28 pictures and `manifest.json` in `unit-06` (`reader_assets.py`).

STILL TO DO: copy that file to `Unit decks\Unit 06 - Performance Management Setup.pptx` once Carol has closed it in PowerPoint (re-stage first and check its md5 is still bf0490ba…; if she saved again, run `carol_deck_s5.py` on her newer file).

`final_scan_u06.py <deck> <p> <f>`: pages clean; Section 5 slides word for word on the pages. On Carol's own slides (reported to her, hers to decide): part numbers 3.3 and 3.4 on slides 19 and 20 (pages 3.2 and 3.3); 3.1 slide titled "The Alignment Brigade" (pages "Unity in Diversity"); reflection slides labelled "1.1" and "2.4"; slide 8 gives Sight 3 "typically 5 – 10%" (pages 20–40%); slide 14 has text under 24pt; times in the notes of slides 3, 12, 17 and 21; the Section 4 opener keeps the two outcomes.

## End-to-end check (9 Oct, before the push)

Carol asked, before committing: does the Capstone work save to the group's page and do the personal reflections go to the Learning Portfolio?
Checked with `e2e_u06.py` and `fake-supabase.js` (folder `Unit decks\_build\rebuild_u06`): the real `unit3_m1_lens5_p.html`, the real `s2r-save.js`, the real `capstone_P.html` and the real rebuilt `collection.html`, in a browser, on a stand-in database. 29 of 29 checks pass. Nothing touched the live site or Supabase.

- Unit 6 page: the eight reflections save under the member. Section 5 saves while typed; Confirm saves `pm_scoring`, `pm_faces`, `pm_execution`, `pm_scorecards` and the four names in `confirmed_items`.
- Capstone page: before Confirm nothing is brought in. After Confirm, opening the Capstone fills 6A to 6D word for word and saves them on the team's Blueprint; a teammate sees the same text; with both confirmations the section is Agreed.
- The database must expect 4 boxes for Unit 6 (`capstone_unit6_boxes.sql`). While it expects 5, "Send for team confirmation" is refused with "Complete every box before sending for confirmation." The stand-in copies this rule; the real function was not read.
- Learning Portfolio: it reads the submission, so a member's reflections appear after that member selects Send to Facilitator. The Unit 6 chapter shows the eight reflections under their questions and leaves the group work out. Reflection 1.2 (FACES scores) shows under "Biggest gap & what closing it would change", as before the change.
- Control: with the Unit 6 line taken out of `collection.html` the group work shows in the Portfolio; with the Unit 6 rows taken out of `capstone_P.html` there is no bring-in. So the test does catch both.
- Not checked: the live site (no push yet) and the live database (SQL not run yet).
