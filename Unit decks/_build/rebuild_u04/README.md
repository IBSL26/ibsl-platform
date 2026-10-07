# Unit 4 rebuild — 7 October 2026 (review stage)

Source of the flow: Carol's brief of 7 October 2026 (word for word in `Claude outputs\Unit 4 - Proposed content (for review).md`).
Source of the wording: her Unit 4 manuscript, her Industry Illusion concept, the pages as they stood, and new example conditions (marked "new" in `u4_content.py`).

**State on 7 October:** PREVIEW files only. The live files `unit2_m1_lens3_p.html` and `unit2_m1_lens3_f.html` are unchanged. Carol reviews the previews first.

| File | What it does |
|---|---|
| `u4_content.py` | The content both pages share: the four checkpoints, the worked example (Unit 3 company, 8 Key Results, 32 conditions), the Industry Illusion concept and game, section outcomes. |
| `build_p.py <old participant file> <new file>` | Builds the participant file. Section 3 and the portal plumbing are cut from the old file byte for byte. |
| `build_f.py <old facilitator file> <new file>` | Builds the facilitator file. Fails if a time, an entry box or a score is left. |
| `u4_p.js` | Participant tools: Industry Illusion game (2.2), Stress-Testing Your Key Results (4.2), saving of the Section 5 game. Both games save as the participant plays; there is no Save to Portfolio row (removed on Carol's word, 7 October, round 4). |
| `u4.css` | Styles added to both files. |
| `make_previews.py <p> <f> mock-s2r.js <folder>` | Stand-alone PREVIEW copies (participant copy saves in the browser only). Never commit or upload them. |
| `mock-s2r.js` | Stand-in save for the previews, with a sample of a member's confirmed Unit 3 OKRs. |

Input for both build scripts: `Claude outputs\Unit 4 file backups\unit2_m1_lens3_[p|f] - before rebuild (7 Oct).html`. Run the scripts from this folder.

## Structure (both files) — as changed on Carol's review of 7 October (evening)

- Section 1: Overview "From Unit 3 to Unit 4" · 1.1 Arena · 1.2 Boundaries · 1.3 Competition · 1.4 Value Proposition · Bringing ABCV Together. Teaching content: Carol's ABCV–MBT text of 7 October (evening), "lens" → "checkpoint". Arena is read at three depths: Functional, Experiential, Consequential (the Functional / Emotional / Social block and the Netflix example were removed on her word). Each part ends with a box "applied to a Key Result" and two example Key Results from the Unit 3 worked example (1a and 4a). In the Arena box the wording names the three depths (functional, experiential, consequential), on Carol's word.
- Section 2: 2.1 The Industry Illusion (three traps; the "This is why Arena matters" lines were deleted on her word) · 2.2 The Industry Illusion Game (portfolio work). The game's Arena questions use the three depths of 1.1.
- Section 3: as it stood (times removed from the facilitator file). Its CTO card still says "functional, emotional, social".
- Section 4, four steps (Define the Arena, Understand the Boundaries, See the Competition, Establish the Value Proposition); each step ends with its Must-Be-True condition. There is no Step 5 (removed on Carol's word, 7 October, late). 4.1 Worked Example: one Key Result of the Unit 3 company (1a) across the four steps, read-only · 4.2 the same four steps on each of the group's own Unit 3 Key Results (Capstone work).
- Section 5: Cause of Death, game format kept. Each scenario is tested against the Industry Illusion: the investigation question reveals the illusion (Q1 Familiarity, Q2 Exclusion, Q3 Complacency), the ABCV checkpoint is where the illusion sits. Key: Ghost Ship = Complacency / Arena · Ferrari in the Mud = Familiarity / Boundaries · Invisible Disruption = Exclusion / Competition · Identity Crisis = Complacency / Value Proposition. Scenario wording was adjusted so that each carries one clear illusion. The reminder blocks above the mines (the three illusions, where an illusion sits) were removed on Carol's word; the key stays in the facilitator's Answer Key. Unit Summary: five blocks.

## Round 4 (7 October, night), on Carol's word

- The "Portfolio work · Save and submit" row is removed from 2.2 and Section 5 (`pf()`, `pfSave`, `pfGoSubmit`, `.u4-pf` are gone). The two games save as the participant plays. Submit to Facilitator sits once, at the end of the unit. The same row is removed from Unit 3 (see `rebuild_u03/README.md`).
- Section 4, 4.1 and 4.2: every step question and every Must-Be-True question carries the Key Result word for word (`STEP_Q`, `STEP_MBT` in `u4_content.py`, with `{kr}`; `kr_span()` on the pages, `mbQ()` in `u4_p.js`; style `.u4-krq`). Step 4 asks: "What about <Key Result> will make customers choose us?"

## Response keys (lens_id `u2m1_lens3`, no database change)

- Reflections: `ref1` (overview), `ref2` (after Bringing ABCV Together), `ref4` (3.1), `ref5` (closing commitment).
- 2.2 game: `__ii_work` (working state), `ii_round1`, `ii_round2`, `ii_round3`, `ii_arena`, `ii_status` (readable).
- 4.2: `__mbt_work` (working state: step, current Key Result, and for each Key Result `fn, ex, co, a` (Step 1), `bd, b` (Step 2), `cp, c` (Step 3), `rel, dis, dlv, v` (Step 4); `a, b, c, v` are the Must-Be-True conditions), `mbt_record` (readable copy of the whole record, saved while the group works, so the facilitator report shows progress before Confirm), `mbt_arena`, `mbt_bound`, `mbt_comp`, `mbt_value` (readable, written on Confirm: per Key Result, the step's entries and its condition), `confirmed_items` ("MBT · Arena", "MBT · Boundaries", "MBT · Competition", "MBT · Value Proposition"). Confirm needs every Key Result through all four steps. An edit removes the confirmation.
- 4.2 bring-in: reads the member's own Unit 3 page (`u2m1_lens2`): `__okr_work` (aligned OKRs with a theme, an Objective and at least one Key Result) and `confirmed_items` containing "Enterprise OKRs". Conditions already typed stay with a Key Result whose text is unchanged.
- Section 5: `__mine_game` (attempts and defused mines), `mine_result` (readable). In each mine the right investigation question carries the option value `correct`, so the game code is unchanged.
- No longer written by the page (old answers stay in the database): `ref3`, `team_name`, `exec_name`, `exec_role`, `syn_*`, `own_*`.

## Written to the portal files (7 October, night, on Carol's word "happy to push these files to the portal")

- `unit2_m1_lens3_p.html` and `unit2_m1_lens3_f.html` are the builds of this folder. Files before: `Claude outputs\Unit 4 file backups\unit2_m1_lens3_[p|f] - before rebuild (7 Oct).html`.
- `patch_links.py <dashboard_F.html> <capstone_P.html> <build_collection.js> <folder>`:
  - `dashboard_F.html`: report headings "Industry Illusion Game", "ABCV–MBT: Stress-Testing the Key Results", "Cause of Death"; labels for the new keys of `u2m1_lens3`.
  - `capstone_P.html`: `PULL.u4` brings boxes 4A to 4D in from `mbt_arena`, `mbt_bound`, `mbt_comp`, `mbt_value`, checked against `confirmed_items`. Boxes 4E and 4F are written by the team. Box 4A now reads "functional, experiential and consequential" (the three depths of 1.1).
  - `build_collection.js`: `CAPSTONE_KEYS.u2m1_lens3` leaves the group work out of the Learning Portfolio (`mbt_*`, `confirmed_items`, and the old `syn_*`, `own_*`, `team_name`, `exec_*`). `collection.html` rebuilt with `node build_collection.js`.
- The four reflection questions carry `class="ref-prompt"` so the Learning Portfolio prints the question above each answer, as in Units 2 and 3.
- Files before: `Claude outputs\Unit 4 file backups\[dashboard_F|capstone_P|collection|build_collection] - before Unit 4 links (7 Oct)`.
- No database change.

## The deck (built 7 October 2026, night, after the two pages)

`Unit decks\Unit 04 - Direction Integrity (ABCV-MBT).pptx`: 38 slides, in the format of the Unit 2 and Unit 3 decks (same design system `lib2.js`, same slide types, presenter notes in Carol's approved form). Files in `Unit decks\_build`:

| File | What it does |
|---|---|
| `rebuild_u04/export_deck_data.py <u04_data.json>` | Writes the unit content from `u4_content.py` (the content both pages are built from) for the deck. |
| `unit04.js <out.pptx>` | The slides. Reads `u04_data.json` and `u04_notes.js`. Writes `reflections/u04/spec.json`. |
| `u04_notes.js` | The presenter notes, one entry for each slide. A line that starts with § is a heading or a step title. |
| `enrich/u04_rebuild.json` | The 9 journal insights. Each is used once. |
| `shoot_reflections_u04.py <PREVIEW participant page> reflections/u04` | Pictures of the four reflection boxes. |
| `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py` | Shared scripts, unchanged. |
| `build_u04.sh <folder>` | Runs the steps in order. |
| `rebuild_u04/final_scan.py <deck> <p.html> <f.html>` | The three-way scan. Result on the final files: 0 problems (129 slide strings found on the pages; outcomes word for word; no text under 24pt; no leftovers). |
| `reader_assets.py` | Remakes `Claude outputs\Deck upload\Module-2\unit-04` (38 pictures and `manifest.json`). |

Slides: cover, Key learning outcomes, unit journey · Section 1 (overview 2 slides; 1.1 to 1.4, two slides each: the checkpoint, then "what Must Be True" on a Unit 3 Key Result; Bringing ABCV Together; Section 1 Reflections) · Section 2 (2.1; 2.2a the game; 2.2b Apply Arena) · Section 3 (3.1a the nine roles; 3.1b the CEO card; Section 3 Reflections) · Section 4 (4.1 the Key Result, Steps 1 to 4, Four Steps Four Conditions; 4.2a; 4.2b) · Section 5 (Cause of Death, two slides; Section 5 Reflections; Unit Summary).

The Industry Illusion game is played in the lesson from the facilitator file, Section 2, part 2.2 (six step panels), as Strategy Airport is in Unit 3. The notes of 2.2a say so.
`lint_notes.py` reports 13 "time" hits: all are the worked Key Result itself ("from 12 hours to 4 hours").
Files before: `Claude outputs\Unit 4 deck backups\` (the 18-slide deck of 2 October, its script and its reader folder).
If Carol edits the deck herself, her file is the master: later changes are made in her file, and this script is a record.

## Still open

- Capstone box 4E (verification ownership) has no source in the unit since Step 5 was removed; the team writes 4E and 4F by hand.
- Section 3 is as it stood: its CTO card still says "functional, emotional, social".
- Section outcomes are the ones on the pages on 7 October.
- Carol's lesson game file is `Claude outputs\Deck upload\Module-2\industry_illusion_unit 4 game.html`.
