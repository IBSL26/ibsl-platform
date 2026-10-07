# Unit 3 rebuild — 6 October 2026

Source of the content: Carol's document "unit 3 Amendments.docx" and her game file "Strategy_Airport_Game_Medical_Health (8).html" (both in `Claude outputs`).

| File | What it does |
|---|---|
| `build_p.py <old participant file> <new file>` | Builds the participant file ("you" voice). Unchanged blocks are cut from the old file byte for byte. |
| `build_f.py <old facilitator file> <new file>` | Builds the facilitator file. Fails if a time, a whiteboard or an entry box is left. |
| `u3_shared.js` | In both files: the four SiP domains and KISS questions, the ten hot zone cards, the Prioritisation Matrix, the worked example of 2.2, the Strategy Airport game. |
| `u3_p.js` | Participant tools: matching exercise (3.1), SiP statements and KISS map (4.1), six steps (4.2), saving of the game (5.1), Unit Summary. |
| `u3_f.js` | Facilitator page: answer-key cards and Unit Summary. |
| `u3.css` | Styles added to both files. |
| `patch_links.py <dashboard_F.html> <capstone_P.html> <folder>` | Report labels for the new answers; Capstone bring-in for boxes 3A to 3F. |
| `make_previews.py <p> <f> mock-s2r.js <folder>` | Stand-alone PREVIEW copies (participant copy saves in the browser only). Never commit or upload them. |

Input for both build scripts is the file as it stood before the rebuild:
`Claude outputs\Unit 3 file backups\unit2_m1_lens2_[p|f] - before rebuild (6 Oct).html`. Run the scripts from this folder.
The scripts are a record. Later edits to the two files are made directly, with exact replacements.

## Structure after the rebuild (both files)

- Section 1: 1.1 (participant reflection removed; incomplete sentence removed from the facilitator file) · 1.2 · 1.3 "Four SiP Domains" · 1.4 · 1.5 "Six Steps: From KISS Output to Enterprise OKRs" (Find Themes, Inspiring Objectives, Define Key Results, Alignment Test, Enterprise Priority, Priority Matrix).
- Section 2: 2.1 · 2.2 "Turning Intent into Action: The Strategy2Results® Sequence" with the worked example of the six steps (old 2.2 removed; old 2.3 is now 2.2).
- Section 3: one part, 3.1 "Natural OKR Emphasis Across Leadership Functions": fused narrative and the matching exercise (individual work).
- Section 4: group work for the Capstone. 4.1 "Translating SiP to KISS" · 4.2 "Translating KISS to OKRs: The Six Steps".
- Section 5: 5.1 "Strategy Airport" (played with the room from the facilitator file; individual work in the participant file) · Unit Summary (five blocks).
- Removed because the amendments do not carry them: old 4.2 Breaking the Biases (de-labelling), the old Section 5 tasks and worked example, the Portfolio Artefact.

## Response keys (lens_id `u2m1_lens2`, no database change)

- Reflections: `ref2` (1.4), `ref3` (2.2), `ref4` (3.1).
- 3.1 matching: `hz_match` (readable result with attempts), `__hz_match` (working state).
- 4.1: `sip_d1_st` … `sip_d4_st` (the group's SiP statements, brought in from the member's Unit 2 page while the boxes are empty, editable), `kex_<cx|op|pc|ev>_<keep|improve|start|stop>` (16 entries, same keys as before), `kiss_keep`, `kiss_improve`, `kiss_start`, `kiss_stop` (written on Confirm).
- 4.2: `__okr_work` (working state of the six steps), `okr_drafts` (readable working copy), `ent_priorities`, `ent_okrs` (written on Confirm).
- `confirmed_items`: "KISS · Keep", "KISS · Improve", "KISS · Start", "KISS · Stop", "Enterprise priorities", "Enterprise OKRs". Editing an entry removes its confirmation.
- 5.1 game: `__game` (working state), `game_kiss`, `game_flight_plan`, `game_round`.
- Keys that begin with `__` are hidden in the facilitator report.
- No longer written by the page (old answers stay in the database and keep their labels): `ref1`, `ref5`, `port1` … `port3`, `okr_o1` … `okr_o4`.

## Capstone

`capstone_P.html`, `PULL.u3`: boxes 3A Keep, 3B Improve, 3C Start, 3D Stop, 3E Enterprise priorities, 3F Enterprise OKRs are read from the member's own Unit 3 answers and checked against `confirmed_items`, exactly as for Unit 2. The Unit 3 section already expects six boxes: no database step.

## Choices made by Claude (reverse on Carol's word)

- The fourth domain is named "Enterprise Value Creation" as in Unit 2 and the Capstone; its five questions are unchanged.
- Hot zone cards carry the full domain names; the COO and CCO cards use the fuller manuscript wording.
- 3.1 list: financial leaders emphasise "Enterprise Value Creation and Operational Capability & Execution Rhythm" ("Operational Discipline" is not a domain).
- Participant game: "Use Example" and "Build Example OKR" show in the facilitator's lesson round only. One option reworded for the standards check ("Reporting activity in place of patient outcomes"). The closing learning point reads "KISS is the evidence base for …".
- KISS map: all sixteen boxes must hold an entry before Confirm. Six steps: up to six themes; Confirm asks for two Key Results in the formula with contributing roles, four alignment ticks and a matrix position for each enterprise priority.
- The facilitator file holds a playable game (nothing saved). This is the one place where the preparation-only rule is set aside, on Carol's instruction.

## The deck (built 6 October 2026, after the two pages)

`Unit decks\Unit 03 - SiP KISS Mapping & OKR Definition.pptx`: 34 slides, presenter notes in the form of Carol's Unit 2 deck. Files in `Unit decks\_build`:

| File | What it does |
|---|---|
| `unit03.js <out.pptx>` | The slides. Reads `rebuild_u03/u3_shared.js` and `rebuild_u03/u3_f.js`, the same data the two pages use. Writes `reflections/u03/spec.json`. |
| `u03_notes.js` | The presenter notes, one entry for each slide. A line that starts with § is a heading or step title. |
| `enrich/u03_rebuild.json` | The 18 journal insights. Each is used once. |
| `shoot_reflections_u03.py <site> reflections/u03` | Pictures of the three reflection boxes (1.4, 2.2, 3.1) from the participant page. |
| `add_reflection_slides.py` | Adds the three Section Reflections slides (shared script). |
| `format_notes_u03.py <in> <out>` | One paragraph for each notes line; § lines become bold. |
| `check_u03.py <deck> <p.html> <f.html>` | No text under 24pt, every notes page opens with a bold heading, outcomes and titles word for word on the pages. |
| `build_u03.sh <folder>` | Runs the steps in order, then `lint_notes.py`. |
| `reader_assets.py` | Remakes `Claude outputs\Deck upload\Module-2\unit-03` (shared script). |

Needs node (pptxgenjs, react-icons, sharp), python-pptx, Playwright and LibreOffice: run in the cloud workspace, then save the results back.
If Carol edits the deck herself, her file is the master: later changes are made in her file, and this script is a record.

## Change of 7 October 2026: 2.2 becomes a working example (facilitator) and an individual exercise (participant)

Carol: "the intelligence enterprise priority has to be a working example flowing from step 4 in the facilitator file. In the participant file this is an exercise that they complete from step 1 to step 6 and they submit as individuals."

- `u3_shared.js` now holds only the case: `WORKED.sip`, `WORKED.kiss` and `renderCase(hostId)`. Both pages show it.
- `u3_f.js` holds the worked answers: `WORKED_MODEL` (five themes, Objectives and OKRs; the alignment-test result; the failed draft; the vote; the trade-off; the matrix positions) and `renderWorked('workedF')`. The participant file carries none of it.
- Each step takes its input from the step before: five OKRs pass Step 4, one draft is returned; in Step 5 seven leaders vote for three each (7, 6, 4, 3, 1), four become enterprise priorities and Objective 5 is released with the trade-off stated; Step 6 places the four.
- `u3_p.js`, block "2.2 · Six-step exercise on the case": tool `CX` (functions `cx…`, element ids `cx…`), hosts `caseP`, `caseToolP`, `caseOutP`. Step 5 lists only the OKRs that earned 4 of 4 in Step 4. "Mark the exercise complete" asks for: at least three themes with an Objective; at least one and at most four enterprise priorities; for each priority two Key Results in the formula with contributing roles and a matrix position; the trade-off when an Objective is left out. An edit after completion sets the exercise back to "In progress".
- New response keys (lens `u2m1_lens2`, no database change): `__case_work` (working state, hidden in the report), `case_six_steps` (readable copy), `case_status`.
- `patch_links.py`: report heading "Six-Step Exercise" and labels for the two readable keys. `collection.html` rebuilt with `node build_collection.js`.
- Sub-line of 2.2 on both pages: "Case · 6 Steps" (was "Worked Example").
- Deck: 36 slides. The worked example runs on seven slides (SiP statement, KISS table, Steps 1 and 2, Step 3, Step 4, Step 5, Step 6). `u03_notes.js` reads the worked answers from `u3_f.js`.
- Files as they stood before this change: `Claude outputs\Unit 3 file backups\… - before 2.2 exercise (7 Oct).html` and `Claude outputs\Unit 3 deck backups\… - before 2.2 rework (7 Oct).pptx`.

## Change of 7 October 2026 (second): the six steps flow from Step 1, with one record and a Print button

Carol: "Step 2, 3, 4, 5, 6 must flow from step 1 … all this data must be stored to be printed at the end." and "this is just for participant file. the facilitator file must just give the precise instructions."

- `u3_p.js`: the group tool of 4.2 and the individual exercise of 2.2 now run on one shared flow (functions `sx…`; tools `OKT` and `CXT` in `SX`; states `OK` and `CX`). Element ids keep their prefixes `okr…` and `cx…`.
- What each step shows (`sxChain`): Step 2 the theme; Step 3 the theme and its Objective; Step 4 the theme, Objective and Key Results; Step 5 the tested OKR in full; Step 6 the selected priority in full.
- An Objective needs two Key Results before it is tested (Step 4). Step 5 lists only OKRs with 4 of 4. A lost tick removes the priority.
- One record under the steps (`sxRecord`), built from Step 1. The two Capstone outputs (Enterprise Priorities, Enterprise OKRs) appear once a priority is selected. Print: `okrPrint()` and `cxPrint()` open the record on a plain page.
- Saved readable copy for the report: `okr_drafts` and `case_six_steps` now hold the full record, matrix position included (`sxText`). Keys are unchanged; no database change.
- `build_f.py`: no tool in the facilitator file. The Participant Activity boxes of 2.2 and 4.2 give the step-by-step instructions.
- Files before this change: `Claude outputs\Unit 3 file backups\… - before six-step flow (7 Oct).html`.

## Change of 7 October 2026 (third): the six-step record sits above the step menu

Carol: "Can this be before the step menu. it is confusing where it is now."
- 4.2 order: intro · Your Six-Step Record (`okrRecP`) · The Six Steps (`okrToolP`) · Confirm and Print (`okrOutP`: Enterprise Priorities, Enterprise OKRs, the two buttons).
- 2.2 order: case · Your Six-Step Record (`caseRecP`) · the six steps (`caseToolP`) · Complete and Print (`caseOutP`).
- `sxSetRec`: when the record above the steps grows or shrinks, the page is scrolled by the same amount, so the box being typed in and the button about to be clicked stay where they are (tested with and without the browser's own scroll anchoring).

## Change of 7 October 2026 (fourth): five steps, worked example on both pages, portfolio work — pages aligned to Carol's final deck

Carol's final deck is `Claude outputs\Deck upload\Module-2\unit-03.pptx` (34 slides). It is the master and is not changed by these scripts. `unit03.js` and `u03_notes.js` in `_build` are a record of the earlier generated deck only.

- Five steps everywhere: Find Themes · Inspiring Objectives · Define Key Results · Alignment Test · Priority Matrix (`FIVE_STEPS` in `u3_shared.js`). Step 5 Enterprise Priority, the vote and the Less is More Rule are gone from 1.5, 2.2, 4.2, the guidance and the summaries.
- 2.2 is a read-only worked example on both pages again: `WORKED` (case, five themes, five Objectives, Key Results, alignment test, matrix) and `renderCase` / `renderWorked` are in `u3_shared.js`. Step 1 shows the themes only. Four OKRs are aligned and placed on the matrix, as on slide 21; Objective 5 earns 3 of 4 and returns to Step 2.
- The individual 2.2 exercise is removed: no `CX` tool, no `case_*` keys, no "Six-Step Exercise" report heading.
- 4.2 group tool (slide 31): up to four themes, one Objective each, up to two Key Results with a contributing-roles box under each, alignment test, matrix. Every aligned OKR is an enterprise priority. Record and Print are named "five-step record". Keys unchanged: `__okr_work`, `okr_drafts`, `ent_priorities`, `ent_okrs`, `confirmed_items`.
- 3.1 matching exercise and 5.1 Strategy Airport are "Portfolio work" in the participant file, each with a numbered "how to complete" box. Sub-lines on both pages: "10 Roles · Portfolio Work", "2 Gates · Portfolio Work". Both already appear in the Learning Portfolio (`collection.html`) under "Hot Zone Matching" and "Strategy Airport".
- Section outcomes as on the deck's section slides (see handover section 15).
- Files before this change: `Claude outputs\Unit 3 file backups\… - before five steps (7 Oct).html`.


## Change of 7 October 2026 (fifth, final): four Objectives, Section 2 outcomes, deck edited to five steps

- `WORKED` in `u3_shared.js` now holds four items (Customer responsiveness, Execution speed, Collaboration culture, Value creation). "Key account growth" is removed. All four earn 4 of 4 at Step 4 and go to the Step 5 matrix.
- Section 2 outcomes on both pages and on slide 12: "Recognise the benefits of mapping the terrain before setting goals." / "Practise the translation of SiP into OKRs."
- Carol allowed slide changes in this round. `edit_deck.py` makes them on her final deck with python-pptx (text runs only, plus removed rows re-spaced): five steps on slides 9, 10, 31; four themes and four Objectives on slides 17, 18; Section 2 outcomes on slide 12; "SiP" on slide 7; notes aligned on slides 1-4, 8, 9, 12, 14, 16, 21, 29, 31, 33, 34. Her untouched final is in `Claude outputs\Unit 3 deck backups\unit-03 - Carol final before five-step edits (7 Oct).pptx`.
- `final_scan.py <deck> <participant page> <facilitator page>` compares the deck with both pages (KLOs, section outcomes, step names, worked example, 3.1 content, leftover terms, page-pair titles). Result on the final files: 0 differences.
- Reader pictures `s01`-`s34` and `manifest.json` are remade from the edited final deck.
- Files before this change: `Claude outputs\Unit 3 file backups\... - before final scan (7 Oct).html`.

## Change of 7 October 2026 (sixth): Save to Portfolio on the two portfolio exercises; group work left out of the Learning Portfolio

- Participant file, 3.1 and 5.1: a "Portfolio work · Save and submit" row under each exercise (`.u3-pf`, built in `build_p.py`). "Save to Portfolio" calls `pfSave('hz')` / `pfSave('game')` in `u3_p.js`, which saves the same keys as before (`__hz_match`, `hz_match`; `__game`, `game_kiss`, `game_flight_plan`, `game_round`) and reports the result in `pf_hz_msg` / `pf_game_msg`. "Go to Submit to Facilitator" calls `pfGoSubmit()`, which opens Section 5 and brings the unit's Submit to Facilitator button into view.
- One submission for the unit is kept: `S2R.submit` inserts a snapshot of the whole unit each time, so the exercises do not carry their own submit.
- `build_collection.js` (repo root): `CAPSTONE_KEYS` and `portfolioPayload()` leave the Unit 3 group work out of the Learning Portfolio (`kex_*`, `kiss_*`, `sip_d*_st`, `okr_drafts`, `ent_priorities`, `ent_okrs`, `confirmed_items`). The facilitator report in `dashboard_F.html` still shows everything. The Capstone still reads `kiss_*`, `ent_priorities`, `ent_okrs` (3A to 3F in `capstone_P.html`).
- Facilitator file: the Participant Activity text of 3.1 and 5.1 names Save to Portfolio and Submit to Facilitator.
- Files before this change: `Claude outputs\Unit 3 file backups\... - before portfolio save buttons (7 Oct).html` and `build_collection - before portfolio filter (7 Oct).js`.

**Unit 2 added (7 October, on Carol's word):** `CAPSTONE_KEYS` in `build_collection.js` now also covers `u2m1_lens1`. The Unit 2 group work (Strategy Architecture, Strategy Intent Statement, Success in Practice: `arch_*`, `org_name`, `strategy_period`, `intent_statement`, `sip_d*_q*`, `sip_d*_st`, `sip_integrated`, `confirmed_items`) is left out of the Learning Portfolio and feeds the Capstone (2A to 2F). The Learning Portfolio for Unit 2 prints the reflections, the opening definition, Role Contribution to SiP and Collective Application. `collection.html` rebuilt and tested with stand-in data.
