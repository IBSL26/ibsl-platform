# Handover — Unit 6 · Performance Management Setup

Written 9 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms. She calls Claude "partner"; Claude is the "tech party" and makes the technical and database decisions.

Her words (9 October): "Give me hand over notes to a new chat for unit 6". Take the exact task from her first message in the new chat. Section 1 gives the task Units 2 to 5 went through, which is the expected one.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only).
3. `Claude outputs\Handover - Unit 5.md`: sections 10 to 14 (folder layout, how the review rounds ran, final state of Unit 5).
4. `Unit decks\_build\rebuild_u05\README.md` (how the Unit 5 pages and deck were built, checked and tested; reuse the method and the scripts).
5. `Claude outputs\Unit 5 - Three-way match (findings).md` (the format of a findings report Carol has accepted).
6. The live Unit 5 pages `unit3_m1_lens4_p.html` and `unit3_m1_lens4_f.html`: the latest model of what Carol approves, Section 5 above all.

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`). Live site: ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase project "S2R Portal Production".

## 1. The task (as done for Units 2 to 5)

- **Three-way match:** the participant file, the facilitator file and the deck say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, cases and activities.
- **Clean-up:** bring Unit 6 to the standard Units 2 to 5 now hold (section 3), and remove what breaks her rules (section 2).
- **Order that works:** read-only scan of the three files, then ONE findings report in the chat with the proposed text, then her decisions, then review files (PREVIEW pages in the real format), then her amendments in rounds, then her approval, then live pages, then deck, then slide pictures, then one final scan, then her commit, SQL and Storage upload.

## 2. Working rules (all in force)

**Git, database, files**

- **Claude never runs git in the repository folder, not even to look.** Carol commits in PowerShell. Give her ONE code block that starts with `cd C:\Users\Carol\ibsl-platform`, names every file in `git add` (never `git add .`; her folder holds many working files that stay off the portal), and ends with `git push`. Say what she should see: the last line ends with `main -> main`. Pages and deck lines go in the same block.
- To check a push without git: read `.git\refs\heads\main` and `.git\refs\remotes\origin\main` as files (same value = pushed), and compare the blob hash of each file with the tree of the head commit using Python. Git stores the pages with LF, so hash the LF form.
- Checking the live site: the fetch tool keeps a copy of a URL. If a page looks old, fetch `https://main--ibslportal.netlify.app/<file>` or the address without `.html`.
- Database changes go to her as SQL for the Supabase SQL editor, one block at a time, a read-only check first, and she pastes back each result. Test the SQL in a local stand-in database (pglite) first.
- Back up before editing: `Claude outputs\Backups\Unit 6 file backups\` and `Claude outputs\Backups\Unit 6 deck backups\` (create them). Edits are surgical. Do not change IDs, `lens_id`, links, lock logic or database calls unless required.
- Keep encoding and line endings as found. Both Unit 6 files are UTF-8, no BOM, CRLF (checked 9 October).
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`. Python leaves `__pycache__` beside build scripts: move it there before the commit lines are given.
- PREVIEW html files are never committed or uploaded.
- Do not spawn subagents.
- Device tools load through ToolSearch. Never run a staging copy and `device_commit_files` in the same parallel tool block: stage first, commit in a later call, then check md5 on her computer.

**Folder layout (her rule of 9 October: one working folder, no version confusion)**

- She reviews decks only in `Unit decks` (one deck per unit, always the current one). Her saved file there is the master.
- She uploads to Supabase only from `Claude outputs\Deck upload`. Claude fills it after her review.
- `Claude outputs\Backups`: every backup. `Claude outputs\Review files`: PREVIEW pages, review notes, screenshots.
- Handover `.md` files and `.sql` files stay loose in `Claude outputs` (they are in git). This file is not yet committed: add `"Claude outputs/Handover - Unit 6.md"` and `"Claude outputs/Handover - Unit 5.md"` to the next `git add` line.

**Wording**

- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of", "in place of"). Never "lens" in visible text or notes. "Strategy2Results®" and "S2R®" always with ®. "SiP", never "SIP".
- No times anywhere. No pre-work. Nothing says anything is automated.
- Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. Online delivery: "post in the chat" (no "at the table", no "in the room").
- **Participant file speaks to the participant throughout** ("you / your / your group"): no facilitator cues ("Ask", "Say", "Tell participants") and no third-person framing of the reader. Role cards address the reader in the role ("As COO, you…"). Facilitator file speaks of "participants / the group", is preparation only (no entry boxes) and gives precise, numbered PARTICIPANT ACTIVITY instructions.
- Learning outcomes: "Key learning outcomes" for the unit; two outcomes per section, led by action verbs, faithful to what the section teaches. They name no tool and no step. Carol rewords them herself; propose only when asked.
- Plain words (her feedback on Unit 5): every named term is explained where it first appears; every list of named items carries a meaning for each item ("people won't know what these are"); every exercise has a box that says how it works, step by step.
- Slide text 24pt or larger (Rule 16). Once Carol edits a deck, her file is the master: later changes go into her file by hand or by a small script on top of it.

**How to work with Carol (these cost her usage when ignored)**

- Her instruction is final. A question of hers that states what must happen IS the instruction: do it. Never answer an instruction with options or a question on the same point.
- Do not add parts she did not write. Do not replace her wording with yours unless she asks.
- When she says "everywhere", change the pages, the deck, the notes and the slide pictures in the same round.
- Short replies. One short "what I understand" line, then the work. She reviews wording as review files and pictures, in rounds; each round she sees more and amends again. Expect several rounds before "build the live files".
- Report facts that need her word in one line each, in plain words, with no menu of options. Jargon in that list confuses her: say what the page shows today and what does not match.
- She may rework a deck herself while Claude builds. Before any deck work, compare the md5 of `Unit decks\<deck>` with the `Deck upload` copy and look for a `~$` lock file (the deck is open in PowerPoint and cannot be replaced).

## 3. The standard Units 2 to 5 now hold (apply to Unit 6)

- **Group work is Capstone work.** The page says so, the group confirms its outputs, the confirmed outputs feed the team's Capstone Blueprint through `PULL` in `capstone_P.html`, and the group work is left out of the Learning Portfolio through `CAPSTONE_KEYS` in `build_collection.js` (then `node build_collection.js` rebuilds `collection.html`). The facilitator report in `dashboard_F.html` shows everything, with labels in `LENS_LABELS` and headings in `FAMILY_DEFS`.
- **Group-work rule:** the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page.
- **Individual exercises are Portfolio work.** Sub-line "… · Portfolio Work" and a "Portfolio work · How to complete …" numbered box. No "Save to Portfolio / Go to Submit" row: the exercises save as the participant works.
- **One Submit to Facilitator per unit**, at the end.
- **Worked examples are read-only on both pages.** Group tools keep one record and end with Confirm and Print.
- **Reflection questions** carry `class="ref-prompt"` so the Learning Portfolio prints the question above each answer.
- **Application section, as Carol shaped it in Unit 5:** the groups work on their own strategy; each step brings back the guiding lesson from the teaching section beside the entry box; a "How Section 5 works" box opens the section; earlier units' outputs the group needs are shown on the page (Unit 5 shows the Unit 3 Start and Stop lists and the team OCEAVL profile through the existing database functions, with no new database object).
- **Capstone boxes follow the unit.** When the unit's group outputs changed, the Capstone boxes for that unit were renamed and their number changed (Unit 5 went from five boxes to three; `Claude outputs\capstone_unit5_boxes.sql` shows how the count is changed while every other unit keeps its live value).
- **Deck:** format of Carol's Unit 2 to 5 decks (design system `Unit decks\_build\lib2.js`; slide types as in `unit05.js`): one slide per part; section slides carry the two outcomes; a "Section N Reflections" slide where a section has reflections; notes as HEADING, HOW TO TEACH IT, numbered steps with Say / Ask, then ON THE PORTAL, AFTER THE TEACHING (`format_notes_u03.py`, `lint_notes.py`). Model: `Claude outputs\Review files\Unit 2 deck - notes as Carol approved them (format model).txt` and her final Unit 3, 4 and 5 decks.
- **Deck reader:** after every deck change remake the reader folder (pictures `s01.jpg` … and `manifest.json`) from the final deck, keep `Unit decks\<deck>` identical to the upload copy, and move surplus pictures to `_to_delete`. Unit 6 is Module 3: `Claude outputs\Deck upload\Module-3\unit-06.pptx` and folder `unit-06`. She uploads both to Supabase (Storage, `facilitator_decks`, `Module-3`) and deletes surplus pictures there. Run `reader_assets.py` in the cloud workspace and write the folder back.
- **Three-way scan:** adapt `Unit decks\_build\rebuild_u05\final_scan.py`.

## 4. Unit 6: the files (checked 9 October, read-only)

| What | Where | State |
|---|---|---|
| Participant file | `unit3_m1_lens5_p.html` | 154,758 bytes; last changed 29 September; `LENS_ID="u3m1_lens5"`; UTF-8, CRLF |
| Facilitator file | `unit3_m1_lens5_f.html` | 123,979 bytes; last changed 29 September; UTF-8, CRLF; no entry boxes |
| Deck | `Unit decks\Unit 06 - Performance Management Setup.pptx` | 28 slides; last changed 2 October; md5 1bc915cb4c73a1698c285a8590f47153; identical to `Claude outputs\Deck upload\Module-3\unit-06.pptx`; reader folder `unit-06` holds 28 pictures and the manifest |
| Deck lock | `Unit decks\~$Unit 06 - Performance Management Setup.pptx` | present on 9 October: Carol had the deck open in PowerPoint. Check the md5 again before any deck work; if it differs from the value above, she has edited it and her file is the master |
| Deck generator | `Unit decks\_build\unit06.js`, `outlines\u06.json`, `source\u06.json`, `enrich\u06.json` | the 2 October build; no `u06_notes.js`, no `rebuild_u06` folder yet |
| Capstone | `capstone_P.html` | boxes 6A Performance scorecard, 6B Leader and team accountability, 6C Scoring logic, 6D Collective Progress Signal, 6E Reporting cadence and tools; `PULL` has no `u6` row; the live box count for `u6` is 5 (Carol's SQL result of 9 October) |
| Report labels | `dashboard_F.html`, `u3m1_lens5` | labels exist for the reflections ("FACES Diagnostic", "Your Rating Experience", "Your Weakest Bridge", …); check `FAMILY_DEFS` |
| Learning Portfolio | `build_collection.js` | `CAPSTONE_KEYS` has no `u3m1_lens5` entry |

**Key learning outcomes (same on both pages and on slide 2):** Evaluate whether organisational performance arrangements support the achievement of strategic priorities. · Define clear relationships between enterprise outcomes, leadership accountability and performance evidence. · Exercise consistent executive judgement on performance status and its strategic significance. · Interpret performance insight in ways that strengthen accountability, decision quality and organisational responsiveness.

**Structure (same part titles on both pages):** 1.1 Measurement vs Management · 1.2 The FACES Framework · 1.3 The Three Sights of Progress · 1.4 The 1–5 Rating Scale · 2.1 PM as the Execution Bridge · 2.2 Compliance vs Commitment Architecture · 2.3 Rules of the Game · 2.4 Leader vs Team: A Critical Distinction · 3.1 The Alignment Brigade · 3.2 CXO Hot Zones · 3.3 The Three Execution Gaps · 3.4 The Continuous PM Shift · 4.1 The Collective Progress Signal · 4.2 Three Elements of Enterprise PM Design · 4.3 The EXECUTION Framework · 5.1 Case Context: MyHealth Live Portal · 5.2 Task 1 · PM Scorecard Architecture · 5.3 Task 2 · Scoring Logic Design · 5.4 Task 3 · Baseline Simulation · 5.5 Task 4 · Reporting Cadence Design · 5.6 Task 5 · Periodic Measures Selection · 5.7 Task 6 · Reporting Tool Design · Unit Summary.

**Saved answers (participant page):** `ref1` to `ref10` (reflections) and `app_scorecard`, `app_scoring`, `app_baseline`, `app_cadence`, `app_measures`, `app_tool` (the six Section 5 tasks). The page holds 20 text boxes, 14 drop-downs and one Submit to Facilitator.

## 5. Found in the quick look (to confirm in the full scan)

1. **Section 5 is a simulation on a given case** (MyHealth Live Portal, a hospital chain), done alone and then compared. It feeds nothing: no Capstone marking, no confirm step, no `PULL.u6`, no `CAPSTONE_KEYS` entry. The five Capstone boxes 6A to 6E speak of the team's own case ("[Case]"). In Unit 5 Carol turned the application section into group work on the team's own strategy. Put this in the findings report as a fact with the proposed text; the design is hers.
2. **Times in the facilitator file** (four matches of "15 min" in the Section 5 FACILITATOR GUIDANCE, with "Suggested timing") and in the deck notes of slides 3 and 24. They break the no-times rule.
3. **In-room wording** in the facilitator file ("compare outputs at the table", "Table discussion"). Delivery is online.
4. **Neither page uses "Portfolio Work" or "Capstone"** as marking. Individual work and group work are not yet marked. The reflection status line reads "✓ Saved to your portfolio".
5. **Reflections have no `class="ref-prompt"`** (10 reflections).
6. **Deck against the standard:** no "Section N Reflections" slides; 1.1 takes two slides (5 and 6); Section 5 has one slide for all six tasks and one for Task 3 while the pages have 5.1 to 5.7; the notes open "FACILITATOR GUIDE" / "Content:" and do not follow the approved notes format (HEADING, HOW TO TEACH IT, numbered Say / Ask, ON THE PORTAL, AFTER THE TEACHING); slide titles differ from the page part titles (for example "1.1 · Measurement and management" on the slide, "1.1 — Measurement vs Management" on the pages; the same for 2.2 and 2.4). All explicit text sizes on the slides are 24pt or larger; `check_standards.js` is the authority.
7. **"Hot Zone" now has two meanings in two units that follow each other.** Unit 5 part 4.2 teaches the "Alignment Hot Zone" of each role (the alignment need the role is inclined to neglect: CEO Shift, CFO Transparency, COO Time, CHRO Skill, CTO/CIO Tools, CMO Engagement, CCO Fairness, CPO Authority, CRO Autonomy, CSO Stake). Unit 6 part 3.2 "CXO Hot Zones" uses the word for each role's performance management contribution ("Hot Zone: Enterprise Visibility", "Financial Signals", "Execution Rhythm", …). For Carol's word, one line.
8. Neither Unit 6 page nor the deck names Unit 5, OCEAVL, ACE-IT, 3S, SCARF, STAT or COMPASS. Check whether Unit 6 should refer back to what the group now leaves Unit 5 with (the 3S record and the ACE-IT behaviours) and to the Unit 3 OKRs.
9. "automatically" appears once on each page inside teaching text (a self-check question; an escalation rule). It describes the organisation, not the portal. Report it; change only on her word.
10. **A 30-day commitment closes Unit 6** (`ref10`, report label "My 30-Day Commitment"; the closing slide asks for "one design change you will make to your current PM system within…"). Carol removed the 30-Day Behavioural Commitment from Unit 5 on 9 October. For her word, one line.
11. Many "—" constructions in the teaching text (for example "This is one of the most important distinctions in strategy execution — and one most organisations get wrong"). Read every section against Rule 13.

## 6. Tools already on her computer

- `Unit decks\_build\rebuild_u05\`: `build_p.py`, `build_f.py`, `amend_*.py`, `amend2_*.py` (pages rebuilt from the backup files by exact replacements with checks, in three layers), content files (`u5*_content.py`), `make_previews.py` + `mock-s2r.js` (stand-alone PREVIEW pages), `patch_links*.py` (report, Capstone, Learning Portfolio), `final_scan.py`, `export_deck_data.py`, `carol_deck_align.py` (a small script on top of Carol's own deck), `test_am2.py` (Playwright checks). Copy the method into `rebuild_u06`.
- `Unit decks\_build\`: `lib2.js`, `kit.js`, `unit05.js` + `u05_notes.js` (deck and notes model), `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py`, `shoot_reflections_u05.py`, `reader_assets.py`, `enrich\u06.json` (journal insights for Unit 6), `unit06.js` (the present Unit 6 deck).
- `build_collection.js` and `check_standards.js` in the repository root.
- Database functions already live and usable from a unit page through `S2R._client.rpc(...)`: `get_my_capstone` (`p_cohort_id`), `get_capstone_team_oceavl` (`p_team_id`), `capstone_section_box_count` (`p_key`).
- The cloud workspace of a new chat starts empty. Stage what a step needs, build and test there (Playwright with the stand-in save; fonts Montserrat and Cormorant Garamond for page pictures; Carlito and Caladea for deck pictures), and write the results back.

## 7. State of Units 2 to 5

- Units 2, 3 and 4 are closed (see their handovers).
- **Unit 5 is closed and live (9 October).** Push confirmed (head commit `a5ba52f`, "Unit 5: Leading with Clarity, OCEAVL scores first, Section 4 merged, Capstone three boxes, deck"); the live participant and facilitator pages show the new content; the three SQL blocks ran (Unit 5 box count 3; units 2, 3, 4, 10 at 6; unit 6 at 5); Carol reported the Storage upload done (35 slides; not visible from the workspace).
- Unit 5 deck: Carol's own 35-slide file is the master; the generator no longer reproduces it.
- Unit 5, left as they are on her word (9 October, "Ok that is alright"): Section 5 outcome 2 unchanged; Section 3 outcome 2 ("Assess the readiness of the people most affected…") unchanged.
- In her git list, `lens_migration_playbook.md` shows as deleted and some older files as changed. They do not come from the unit work; leave them alone.

## 8. Lessons of the Unit 5 round

- Build the review files first and expect her to reshape the application section more than once. Keep each round as a new layer of exact replacements on top of the last, so every earlier state can be rebuilt.
- When she asks for "meanings", write one plain sentence per item and show them in the review file; she reads them there.
- Role cards: generic lines do not pass. Each role needs its own story (what sets it off, what you will see and hear, what it costs).
- Tell her in the first line when a review file is ready and where it is (`Claude outputs\Review files`).
- After "build the live files" she may still add one change. Wait for "go ahead".
- After her push, check the live pages yourself and report in plain words what the pages show.

## 9. Three-way match done; Carol's amendments of 9 October (afternoon): built as review files, NOT yet on the live pages

- Findings report: `Claude outputs\Unit 6 - Three-way match (findings).md` (read-only scan; eleven points for her word).
- She answered with her own amendments (below) in place of ticking the eleven points. Build: `Unit decks\_build\rebuild_u06\` (README there). Review files: `Claude outputs\Review files\PREVIEW - Unit 6 Participant.html` and `PREVIEW - Unit 6 Facilitator.html`. Backups: `Claude outputs\Backups\Unit 6 file backups\… - before amendments (9 Oct).html`. The live pages, the links and the deck are unchanged.

**Her instructions, 9 October (her words, shortened only where she pasted long text; the long text is in `u6_content.py`):**

1. "section 1.4 change title to Leader's response from The 1–5 Rating Scale. Add introduction narrative to beef up this" (her narrative: a good PM system reduces subjectivity … "What must we now do because of this rating?" …). "See what you can take over to the participant file to beef up the intro to this section from the above."
2. "Add this as section 1.5 in both but ensure that the framing of the words is relevant in each file. The impact of a calibrated system: …" (no-surprise event; Strategic Transparency, Shift in Dynamics, Pathways to Excellence).
3. "Get PPT notes for 2." and "Get PPT notes to beef up portal content for both facilitator and participant for the bridges. Ensure that the framing of the sentences is relevant to the facilitator or participant."
4. "Add this as beef up to opening intro of 2.2 before The choice is rarely made explicitly — but it is always made. The six dimensions below reveal which architecture is currently operating. then this moves after the narration below: A compliance driven PM depicts an environment where Leader holds accountability / Assessment and judgement / Consequence and control. A commitment driven PM depicts an environment where Team co-owns accountability / Inquiry and problem-solving / Root cause; co-designed recovery."
5. "Remove section 2.3 rules of the game from both files"
6. "Add reflection for participants after 2.4 Does our current PM provide this distinction between the team or individual evaluation and the leaders in this manner based on execution progress for the team member vs progress towards strategic outcome or key Result for the leader. If not what would be my contribution to closing this gap. (feel to polish the grammar without diluting the meaning)"
7. "Change 3.1 title from The Alignment Brigade to Unity in diversity. Then combine this section to one section between 3.1 and 3.2 - this now becomes all 3.1 then remove this reflection from participant - Your Enterprise Signal … but maintain this reflection - Your Hot Zone … right there at the end of the combined 3.1. Please check the narrative of CXO Hot Zones must be beefed up in the facilitator file too"
8. "Let us add a reflection after 3.4 for participants - What is the current PM architecture of your organisation? And what PM system is currently being used?"
9. "Section 4 remove 4.1 from both files. So EXECUTION becomes the only section. Beef up the intro to add the distinction between FACES and EXECUTION" (her text: FACES is the function test … EXECUTION is the design quality test … "FACES tells us what a PM system must deliver. EXECUTION tells us what must be designed into the system for it to deliver."). "Make this section just learning content for participants too. Currently it a scoring exercise."
10. "Let us tweak Application section 5. This becomes a group exercise where the groups develop a PM architecture using the recommended steps - make this clear to populate structurally and coherently and it goes to the blue print. 1. Design the performance Scoring Logic Design: Define what performance level earns each rating selected · Specify what evidence is required to confirm each rating · Identify any contextual factors that might legitimately affect the rating · Describe the lines of sight of progress used · Describe the review Cadence and why · Describe the leadership response each rating should trigger in the monthly review. 2. Design and describe the FACES of your PM architecture. 3. Design and describe the EXECUTION of your PM architecture. 4. Design a PM SCORE CARD for the CEO and CFO"
11. Follow-up message: "When designing the score card for the CEO and CFO, the groups use two of their Key Results as basis for measurement."

**How Claude read the points that could be read two ways (all reported to her):**

- "So EXECUTION becomes the only section": Section 4 now has one part, 4.1 The EXECUTION Framework. Both 4.1 The Collective Progress Signal and 4.2 Three Elements of Enterprise PM Design left (with the cumulative progress formula and the "Apply the Formula" reflection). If she wants 4.2 back, restore it in `build_u06.py` (keep `blk(src, '4.2 &mdash;')` in `sec4`, renumbered).
- "Get PPT notes for 2": taken as Section 2. The manuscript detail in the deck notes of slides 10, 11, 12 and 14 went into 2.1, 2.2 and 2.3.
- "Add reflection … after 2.4": her reflection takes the place of the old 2.4 reflection (which had no saved-answer name and never saved). 2.4 is now 2.3 because Rules of the Game left.
- The 30-day commitment left with the old Section 5 (her list for Section 5 has four steps and nothing else; she removed the same commitment from Unit 5).
- Parts renumbered: 3.3 → 3.2, 3.4 → 3.3; her "reflection after 3.4" sits in the new 3.3.
- Titles in title case to match the other parts: "Leader's Response", "Unity in Diversity".

**Standard fixes made in the same build** (the findings report, section "What I will put right"): times and room wording out of the facilitator page; 12 PARTICIPANT ACTIVITY notes; `ref-prompt` on every reflection; role cards speak to the participant in the role; "performance management (PM)" at first mention; "PIP" spelled out; the rebuilt parts carry one shared text in the fuller facilitator wording. Not touched: the small wording differences between the pages in 1.1, 1.2, 1.3, 3.2 and 3.3 (as before the amendments), the unit sub-title ("Influence" on the participant page), "vs" in three part titles, the CPO "product pipeline" wording.

**Checks:** build reproduces on her computer byte for byte (participant md5 5d59c4c5…, facilitator 9ade8077…); browser test 100 checks, all pass; `node check_standards.js` on a copy of the folder with the two built pages: no breach; phone widths no wider than before.

**Waiting on Carol:** her review of the two PREVIEW files, in rounds. After "build the live files": the go-live list in `rebuild_u06\README.md` (pages, Capstone four boxes and `PULL.u6`, box count SQL 5 → 4, report labels, Learning Portfolio keys, deck in the Unit 2 to 5 format, reader pictures, final scan, commit lines). The Unit 6 deck was still open in PowerPoint on her computer (lock file present); ask her to close it before the deck stage.

Add to the next `git add` line: `"Claude outputs/Unit 6 - Three-way match (findings).md"` and the files of `"Unit decks/_build/rebuild_u06/"` by name. PREVIEW files are never committed.

## 10. Live write of 9 October (evening): "Remove the 30-day commitment … and build live pages. Use the current unit 6 in Unit Decks to update just section 5 slides. I have already amended all the sections."

- The review files were approved as they stood (the 30-day commitment was already out). No change between the PREVIEW build and the live pages.
- Written to her folder and checked by md5: the two pages, `capstone_P.html`, `dashboard_F.html`, `build_collection.js`, `collection.html`, `Claude outputs\capstone_unit6_boxes.sql` (table of md5 values in `rebuild_u06\README.md`).
- Deck: her own 27-slide deck is the master. `carol_deck_s5.py` changed the Section 5 slides and the closing slide only (28 slides). The result is in `Deck upload\Module-3` with 28 pictures and the manifest. It could NOT be written to `Unit decks` (open in PowerPoint, lock file). When she says the deck is closed: re-stage her file, check the md5 (bf0490ba…), write the 28-slide file there, check both copies are identical.
- Waiting on Carol: (1) the push (one block, given to her); (2) the three SQL blocks of `capstone_unit6_boxes.sql` (expect 5, then "Success", then unit6 = 4 and unit5 = 3); (3) close the deck in PowerPoint; then the deck line and the Storage upload (`facilitator_decks`, `Module-3`: replace `unit-06.pptx`, upload the 28 pictures and `manifest.json` of `unit-06`).
- After her push: check `.git\refs\heads\main` against `.git\refs\remotes\origin\main` (before the push both held a5ba52fb…) and read the live pages at `https://main--ibslportal.netlify.app/unit3_m1_lens5_p.html`.
- For her word, still open: both Section 4 outcomes and the second Section 5 outcome describe content that has left; the points on her own slides listed in the README.


## End-to-end check (9 Oct, before the push)

Carol asked, before committing: does the Capstone work save to the group's page and do the personal reflections go to the Learning Portfolio?
Checked with `e2e_u06.py` and `fake-supabase.js` (folder `Unit decks\_build\rebuild_u06`): the real `unit3_m1_lens5_p.html`, the real `s2r-save.js`, the real `capstone_P.html` and the real rebuilt `collection.html`, in a browser, on a stand-in database. 29 of 29 checks pass. Nothing touched the live site or Supabase.

- Unit 6 page: the eight reflections save under the member. Section 5 saves while typed; Confirm saves `pm_scoring`, `pm_faces`, `pm_execution`, `pm_scorecards` and the four names in `confirmed_items`.
- Capstone page: before Confirm nothing is brought in. After Confirm, opening the Capstone fills 6A to 6D word for word and saves them on the team's Blueprint; a teammate sees the same text; with both confirmations the section is Agreed.
- The database must expect 4 boxes for Unit 6 (`capstone_unit6_boxes.sql`). While it expects 5, "Send for team confirmation" is refused with "Complete every box before sending for confirmation." The stand-in copies this rule; the real function was not read.
- Learning Portfolio: it reads the submission, so a member's reflections appear after that member selects Send to Facilitator. The Unit 6 chapter shows the eight reflections under their questions and leaves the group work out. Reflection 1.2 (FACES scores) shows under "Biggest gap & what closing it would change", as before the change.
- Control: with the Unit 6 line taken out of `collection.html` the group work shows in the Portfolio; with the Unit 6 rows taken out of `capstone_P.html` there is no bring-in. So the test does catch both.
- Not checked: the live site (no push yet) and the live database (SQL not run yet).

## Push done (9 Oct, 17:06)

- Carol pushed. Head and origin both `e431c08` (parent `a5ba52f`). Every named file in the commit equals her local file (blob check).
- Live participant and facilitator pages read: twelve part titles as built, Section 5 "Designing the PM Architecture" with four steps, no MyHealth, no 30-day commitment.
- `capstone_P.html` and `collection.html` cannot be read through the fetch tool (script only); they are in the same commit.
- Still waiting: the three SQL blocks (block 1 given to her first), then "closed" for the deck, then the deck line and the Storage upload. This note and the deck go in the next `git add`.
- 17:15: the PowerPoint lock file was gone and her deck was unchanged (md5 bf0490ba…), so the 28-slide deck was written to `Unit decks\Unit 06 - Performance Management Setup.pptx` (md5 570180bc…, same as `Deck upload\Module-3\unit-06.pptx`). Her 27-slide deck is in `Backups\Unit 6 deck backups`. Deck not yet committed.
