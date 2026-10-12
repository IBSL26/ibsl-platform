# Handover — Unit 8 · Performance Measurement

Written 12 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms, one click at a time. She calls Claude "partner"; Claude is the "tech party" and makes the technical and database decisions.

Her words (12 October, 09:53 and again at 10:52): "Give me unit 8 handover notes to a new chat" · "Ok give me handover notes for unit 8 partner. Consider all the hygiene work that you have done". Section 9 holds the hygiene work of 12 October: it is built and in review, NOT live; finish it first if she asks. Take the exact task from her first message in the new chat. Section 1 gives the task Units 2 to 7 went through, which is the expected one.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only; on 12 October it lists Rule 16 lines for the decks of other units only).
3. `Claude outputs\Handover - Unit 7.md`: sections 9 to 12 (her three rounds of Unit 7 amendments word for word, how they were read, the live write, the end-to-end check, the push).
4. `Unit decks\_build\rebuild_u07\README.md` (how the Unit 7 pages, links and deck were built, checked and tested; reuse the method and the scripts).
5. `Claude outputs\Unit 7 - Three-way match (findings).md` (the latest findings report Carol accepted).
6. The live Unit 7 pages `unit3_m1_lens6_p.html` and `unit3_m1_lens6_f.html`: the latest model of what Carol approves, Section 5 above all.
7. Section 9 of this file (hygiene of 12 October) and `Unit decks\_build\hygiene_12oct\` (the scripts).

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`). Live site: ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase project "S2R Portal Production".

## 1. The task (as done for Units 2 to 7)

- **Three-way match:** the participant file, the facilitator file and the deck say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, cases and activities.
- **Clean-up:** bring Unit 8 to the standard Units 2 to 7 now hold (section 3), and remove what breaks her rules (section 2).
- **Order that works:** read-only scan of the three files, then ONE findings report in the chat with the proposed text, then her decisions, then review files (PREVIEW pages in the real format), then her amendments in rounds, then her approval, then live pages, then the end-to-end test, then deck, then slide pictures, then one final scan, then her commit, SQL and Storage upload.

## 2. Working rules (all in force)

**Git, database, files**

- **Claude never runs git in the repository folder, not even to look.** Carol commits in PowerShell. Give her ONE code block that starts with `cd C:\Users\Carol\ibsl-platform`, names every file in `git add` (never `git add .`; her folder holds many working files that stay off the portal), and ends with `git push`. Say what she should see: the last line ends with `main -> main`.
- To check a push without git: read `.git\refs\heads\main` and `.git\refs\remotes\origin\main` as files (same value = pushed), and compare the blob hash of each file with the tree of the head commit using Python (read the loose objects with `zlib`). Git stores the pages with LF, so hash the LF form as well as the file as it is.
- Checking the live site: the fetch tool reads the unit pages. It cannot read `capstone_P.html` and `collection.html` (their content sits in script); for those two rely on the blob check. If a page looks old, fetch `https://main--ibslportal.netlify.app/<file>`. The device shell and the cloud shell have no route to the live site.
- Database changes go to her as SQL for the Supabase SQL editor, one block at a time, a read-only check first, and she pastes back each result. Test the SQL in a local stand-in database (pglite) first. With the first block, give her the clicks: supabase.com, Dashboard, project "S2R Portal Production", SQL Editor in the left column, empty the typing box, paste, green Run button, the small table underneath.
- Back up before editing: `Claude outputs\Backups\Unit 8 file backups\` and `Claude outputs\Backups\Unit 8 deck backups\` (create them). Edits are surgical. Do not change IDs, `lens_id`, links, lock logic or database calls unless required.
- Keep encoding and line endings as found. Both Unit 8 files are UTF-8, no BOM, CRLF (checked 12 October).
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`. Python leaves `__pycache__` beside build scripts: move it there before the commit lines are given. (An old `__pycache__` sits in `Unit decks\_build\`; it is never named in `git add`.)
- PREVIEW html files are never committed or uploaded. `Claude outputs\Backups`, `Review files` and `Deck upload` are not in git.
- Do not spawn subagents.
- Device tools load through ToolSearch. Never run a staging copy and `device_commit_files` in the same parallel tool block: stage first, commit in a later call, then check md5 on her computer.

**Folder layout (her rule of 9 October: one working folder, no version confusion)**

- She reviews decks only in `Unit decks` (one deck per unit, always the current one). Her saved file there is the master.
- She uploads to Supabase only from `Claude outputs\Deck upload`. Claude fills it after her review.
- `Claude outputs\Backups`: every backup. `Claude outputs\Review files`: PREVIEW pages, review notes, screenshots.
- Handover `.md` files and `.sql` files stay loose in `Claude outputs` (they are in git). Not yet committed on 12 October: this file. Add `"Claude outputs/Handover - Unit 8.md"` to the next `git add` line.

**Wording**

- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of", "in place of"). Never "lens" in visible text or notes. "Strategy2Results®" and "S2R®" always with ®. "SiP", never "SIP".
- No times anywhere. No pre-work. Nothing says anything is automated.
- Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. Online delivery: "post in the chat" (no "at the table", no "in the room").
- **Participant file speaks to the participant throughout** ("you / your / your group"): no facilitator cues ("Ask", "Say", "Tell participants") and no third-person framing of the reader. Role cards address the reader in the role ("As COO, you…"). Facilitator file speaks of "participants / the group", is preparation only (no entry boxes) and gives precise, numbered PARTICIPANT ACTIVITY instructions.
- Learning outcomes: "Key learning outcomes" for the unit; two outcomes per section, led by action verbs, faithful to what the section teaches. They name no tool and no step. Carol rewords them herself; propose only when asked.
- Plain words: every named term is explained where it first appears (Unit 6: "performance management (PM)", "PIP" spelled out; Unit 7: "Key performance indicator (KPI)"); every list of named items carries a meaning for each item; every exercise has a box that says how it works, step by step.
- Slide text 24pt or larger (Rule 16). Once Carol edits a deck, her file is the master: later changes go into her file by a small script on top of it.

**Facilitator and group work (her standing rule of 11 October)**

- The facilitator does not review group work: all Capstone work is reviewed independently at graduation. Facilitator wording on a group exercise only guides how the work is completed. Never "Listen for…", "Challenge any statement…", "Watch for…", "Check that…" on group work, on the page or in the slide notes. (Class practice the facilitator leads, such as a role play with nothing entered on the portal, may keep its watch points.)
- Text boxes are clean: short paragraphs or a numbered list, never loose text run together; one PARTICIPANT ACTIVITY note per exercise.
- Deck notes start with teaching. A question in the notes only asks about content already taught (her rule of 11 October, "see how the uploaded PPTs have been written").

**How to work with Carol (these cost her usage when ignored)**

- Her instruction is final. A question of hers that states what must happen IS the instruction: do it. Never answer an instruction with options or a question on the same point.
- Where an instruction can be read two ways, take the plain reading, do it, and say in one line how it was read (Unit 6: "So EXECUTION becomes the only section" was read as both other parts leaving; she did not object).
- Do not add parts she did not write. Do not replace her wording with yours unless she asks; where her sentence breaks a wording rule, reword only that sentence and say so.
- When she says "everywhere", change the pages, the deck, the notes and the slide pictures in the same round.
- Short replies. Tell her in the first line when a file is ready and where it is. She reviews wording as review files and pictures, in rounds.
- Report facts that need her word in one line each, in plain words, with no menu of options. Say what the page shows today and what does not match.
- She may rework a deck herself while Claude builds. Before any deck work, compare the md5 of `Unit decks\<deck>` with the `Deck upload` copy and look for a `~$` lock file (the deck is open in PowerPoint and cannot be replaced). When the lock file is gone and her md5 is unchanged, write the deck without waiting for her to say "closed".

## 3. The standard Units 2 to 7 now hold (apply to Unit 8)

- **The last section is always the Application section with the Capstone work** (her rule of 12 October). Units 5, 6 and 7 hold it; Units 3 and 4 were swapped to it on 12 October (section 9); Unit 2 keeps its own order by her decision ("Unit 2 is messed up ... take it back"); Unit 1 has no Capstone and already ends on Application. In Unit 8, Section 5 must be the group Capstone work.
- **Back to Platform / Back to Dashboard sits at the top left of the header** (back link, thin divider, module and unit title; badges on the right), as in Units 4 onwards. Unit 8 already has it.
- **Group work is Capstone work.** The page says so, the group confirms its outputs, the confirmed outputs feed the team's Capstone Blueprint through `PULL` in `capstone_P.html`, and the group work is left out of the Learning Portfolio through `CAPSTONE_KEYS` in `build_collection.js` (then `node build_collection.js` on her computer rebuilds `collection.html`). The facilitator report in `dashboard_F.html` shows everything, with labels in `LENS_LABELS`, the numbered reflection map and headings in `FAMILY_DEFS`.
- **How the Capstone link works:** Confirm on the unit page saves each part as plain text under its own key and adds the part's name to the list `confirmed_items`. The Capstone page reads those keys from the member's own unit page and fills the boxes only when the name is in the list. The working entries save under a key that starts with `__` (hidden from the report and the Learning Portfolio). An edit after Confirm takes the names out again.
- **The Learning Portfolio reads the submission.** A member's reflections appear there after that member selects Submit to Facilitator.
- **Group-work rule:** the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page.
- **Individual exercises are Portfolio work.** Sub-line "… · Portfolio Work" and a "Portfolio work · How to complete …" numbered box. The exercises save as the participant works.
- **One Submit to Facilitator per unit**, at the end.
- **Worked examples are read-only on both pages.** Group tools keep one record and end with Confirm and Print.
- **Reflection questions** carry `class="ref-prompt"` so the Learning Portfolio prints the question above each answer. Every reflection box has an `id` and is in the page's `KEYS` list (Unit 6 had one that never saved).
- **Application section, as Carol shaped it in Units 5, 6 and 7:** the groups work on their own strategy; the section runs as numbered steps, each on its own tab, each with the guiding lesson beside the entry boxes; a "How Section 5 works" box opens the section; earlier units' outputs the group needs are shown on the page read-only (Unit 6 Step 4 reads the group's confirmed Unit 3 Enterprise OKRs with `S2R.loadAll('u2m1_lens2')`: `__okr_work.items[{obj, krs:[{t}]}]`, shown only when `confirmed_items` holds "Enterprise OKRs"). No set case and no closing commitment (she removed the 30-day commitment from Units 5 and 6 and the five-day commitment from Unit 7). Unit 7 model: choices are drop-down lists of the group's own confirmed outputs (Unit 3 Objectives and Key Results from `u2m1_lens2`; Unit 2 SiP statements from `u2m1_lens1`: `sip_d1_st`…`sip_d4_st`, shown when `confirmed_items` holds the SiP name); Section 5 may hold more than one exercise (Unit 7: 5.1 and 5.2), each Capstone work, one record and one Confirm for the section. An individual version of a group exercise can sit earlier in the unit as Portfolio work (Unit 7 part 4.2).
- **Capstone boxes follow the unit.** When the unit's group outputs change, the Capstone boxes for that unit are renamed and their number changes, and the database function `capstone_section_box_count` is set to the same number (`Claude outputs\capstone_unit6_boxes.sql` is the model: it keeps every other unit at its live value and can be run twice). Until the number matches, "Send for team confirmation" is refused with "Complete every box".
- **Deck:** format of Carol's Unit 2 to 6 decks (design system `Unit decks\_build\lib2.js`): one slide per part; section slides carry the two outcomes; a "Section N Reflections" slide where a section has reflections; notes as HEADING, HOW TO TEACH IT, numbered steps with Say / Ask, then ON THE PORTAL, AFTER THE TEACHING (`format_notes_u03.py`, `lint_notes.py`). Model: `Claude outputs\Review files\Unit 2 deck - notes as Carol approved them (format model).txt` and her final Unit 3 to 7 decks. Unit 7 added: reflection slides are a title, a picture of the reflection taken from the participant page and a gold oval "Part N.N" (`carol_deck_u07.py`, `shoot_reflections_u07.py`).
- **Deck reader:** after every deck change remake the reader folder (pictures `s01.jpg` … and `manifest.json`) from the final deck with `reader_assets.py` in the cloud workspace, keep `Unit decks\<deck>` identical to the upload copy, and move surplus pictures to `_to_delete`. Unit 8 is Module 3: `Claude outputs\Deck upload\Module-3\unit-08.pptx` and folder `unit-08`. She uploads both to Supabase (Storage, `facilitator_decks`, `Module-3`) and deletes surplus pictures there.
- **Tests before she commits:** the browser checks of the PREVIEW pages (`test_u07.py`) and the end-to-end test on the real pages with a stand-in database (`e2e_u07.py` + `fake-supabase.js` of `rebuild_u06`): unit page saves, Capstone brings the work in, Learning Portfolio shows the reflections and leaves the group work out. Run a control with the unit's link lines taken out, so the test is shown to catch a break.
- **Three-way scan:** adapt `Unit decks\_build\rebuild_u07\final_scan_u07.py`.

## 4. Unit 8: the files (checked 12 October, read-only)

| What | Where | State |
|---|---|---|
| Participant file | `unit3_m2_lens7_p.html` | 111,166 bytes; last changed 29 September; md5 14234cb68db65bec1390365cb13e4e92; `LENS_ID="u3m2_lens7"`; UTF-8, no BOM, CRLF |
| Facilitator file | `unit3_m2_lens7_f.html` | 94,749 bytes; last changed 29 September; md5 82ed52735fc8cdc7814b31bd5abfae22; UTF-8, no BOM, CRLF; no entry boxes |
| Deck | `Unit decks\Unit 08 - Performance Measurement.pptx` | 23 slides; last changed 2 October; md5 1baf704f9beda0b1c0a4c6827371275f; identical to `Claude outputs\Deck upload\Module-3\unit-08.pptx`; reader folder `unit-08` holds 23 pictures and the manifest |
| Deck lock | `Unit decks\~$Unit 08 …` | none on 12 October. Check the md5 again before any deck work; if it differs from the value above, she has edited it and her file is the master |
| Deck generator | `Unit decks\_build\unit08.js`, `outlines\u08.json`, `source\u08.json`, `enrich\u08.json` | the 1 October build; no `rebuild_u08` folder yet |
| Capstone | `capstone_P.html` | boxes 8A Review discipline, 8B Progress signals and responses, 8C Breakdown risk, 8D Enterprise performance intelligence, 8E Accountability loop (all written for the team's own case, "[Case]"); `PULL` has no `u8` row; the live box count for `u8` is 5 (the default) |
| Report labels | `dashboard_F.html`, `u3m2_lens7` | labels for `ref1` to `ref7` and the `app_…` keys (`app_loop_reflection` is labelled "Overall Reflection & 5-Day Commitment"); numbered map 1 to 7; `FAMILY_DEFS` has "Performance Intelligence Synthesis" (`app_syn_*`) and "Application — Accountability Loop" (`app_rootcause`, `app_corrective`, `app_loop_reflection`) |
| Learning Portfolio | `build_collection.js` | `CAPSTONE_KEYS` has no `u3m2_lens7` entry |

**Key learning outcomes (same on both pages):** Interpret performance evidence in relation to strategic objectives and the wider organisational context. · Distinguish meaningful strategic progress from activity, compliance and short-term fluctuation. · Exercise balanced executive judgement when performance differs from agreed expectations. · Derive relevant decisions, organisational learning and leadership action from performance evidence.

**Section outcomes (same on both pages):**
- Section 1: Distinguish meaningful strategic progress from activity. · Explain how performance evidence converts into realignment and corrective action.
- Section 2: Explain why review discipline determines the pace of execution. · Interpret the progress signals that emerge in performance reviews and the response each requires.
- Section 3: Identify where the review and interpretation of performance evidence break down across functions. · Assess which breakdown is most prevalent in their own organisation.
- Section 4: Interpret individual performance signals within a shared enterprise view of progress. · Derive enterprise decisions and organisational learning from collective performance evidence.
- Section 5: Exercise balanced judgement when performance differs from agreed expectations. · Determine the root cause of underperformance and the leadership action it requires.

**Structure (part titles):** 1.1 From Activity to Progress: The Visibility Shift · 1.2 The Four Strategic Purposes of Performance Measurement · 1.3 The Review–Realign–Restore Cycle · 2.1 Execution Discipline: The Real Differentiator · 2.2 Four Consequences of Weak Review Discipline · 2.3 Three Progress Signals in Healthy Review Conversations · (Section 3 has no numbered part: four gap cards, "Four fractures") · 4.1 The Collective Intelligence Principle · 4.2 The Enterprise Performance Intelligence Circle: Three Rounds · 4.3 The Synthesis Layer: Enterprise Intelligence Decisions · 5.1 The Accountability Loop Role Play · Unit Summary. The facilitator page adds a part "Facilitator · The Collective Intelligence Board" before 5.1.

**Section headings differ between the pages:** Section 3 "Where Does Performance Measurement Break Down?" (participant) and "… Break Down Across Functions?" (facilitator); Section 5 "The Accountability Loop Role Play" (participant) and "Building the Collective Intelligence Board & The Accountability Loop" (facilitator).

**Saved answers (participant page):** `team_name`; `ref1` to `ref7` (`ref4` is a 1-to-5 rating of the four gaps with a note `ref4_notes`; `ref5` to `ref7` are the three rounds of 4.2); `app_syn_pattern`, `app_syn_repeat`, `app_syn_depend`, `app_syn_chain`, `app_syn_decision` (4.3 synthesis); `app_rootcause`, `app_corrective`, `app_loop_reflection` (5.1).

**Deck slides:** 1 title · 2 Key learning outcomes · 3 The unit journey · 4 Section 1 · 5 "1.1 · From activity to progress" · 6 "1.2 · Four strategic purposes of measurement" · 7 "1.3 · The Review–Realign–Restore cycle" · 8 "1.3 · The Accountability Loop: three root causes" · 9 Section 2 · 10 "2.1 · Execution discipline" · 11 "2.2 · Four consequences of weak review discipline" · 12 "2.3 · Three progress signals" · 13 Section 3 · 14 "Four fractures in performance measurement" · 15 Section 4 · 16 "4.1 · The Collective Intelligence principle" · 17 "4.2 · The Collective Intelligence Circle" · 18 "4.3 · The Synthesis Layer" · 19 Section 5 · 20 "The Collective Intelligence Board" · 21 "5.1 · The Accountability Loop role play" · 22 "Observer evaluation criteria" · 23 "Unit Summary · Closing". No slide text under 24pt.

## 5. Found in the quick look (to confirm in the full scan)

1. **An entry that never saves.** The "Alignment Score" number box in 5.1 (under "Corrective Actions Agreed — Restore Stage") has no `id` and no save call: what is typed is lost on reload. Put it first in the findings report. (The four `ref4` rating drop-downs save through `syncScores('ref4')`; confirm.)
2. **Section 5 is a role play on a set case** ("Complaint resolution is still averaging 36 hours against a 12-hour target, six weeks from the deadline"), done by each participant, with observer criteria. It feeds nothing: no Capstone marking, no Confirm, no `PULL.u8`, no `CAPSTONE_KEYS` entry. The Capstone boxes 8A to 8E speak of the team's own case. In Units 5, 6 and 7 Carol turned the application section into group Capstone work on the team's own strategy. Report the fact with proposed text; the design is hers.
3. **4.2 and 4.3 are group-style exercises** (three rounds of an Enterprise Performance Intelligence Circle; the synthesis decisions) saved per participant as reflections and `app_syn_*`, with a `team_name` box. Capstone box 8D asks for exactly this output. Report how it maps to 8D.
4. **A closing commitment:** `app_loop_reflection` is labelled "Overall Reflection & 5-Day Commitment" in the report; the closing slide asks the participant to name a KPI that has drifted. Carol removed closing commitments from Units 5, 6 and 7. For her word, one line.
5. **Section 3 has no numbered part** on either page (four gap cards and the `ref4` rating) and the slide is titled "Four fractures in performance measurement". Every other section has numbered parts. Propose "3.1 — …".
6. **Slide 8 "1.3 · The Accountability Loop: three root causes"** has no part on the pages under 1.3 (it is taught in 5.1). Slide 20 "The Collective Intelligence Board" matches only the facilitator part. Slide 22 "Observer evaluation criteria" belongs to the role play.
7. **Times:** facilitator page "Timing: Awareness and Intelligence …"; deck notes slide 3 "Time: …". Remove.
8. **No Portfolio or Capstone marking** on either page; no `class="ref-prompt"` on the reflections; facilitator page holds 6 FACILITATOR GUIDANCE boxes and 1 PARTICIPANT ACTIVITY note.
9. **Deck notes** follow the old format ("Content:", part titles in capitals); none has HOW TO TEACH IT, numbered Say / Ask, ON THE PORTAL, AFTER THE TEACHING. No "Section N Reflections" slides. Slide titles are shorter than the part titles.
10. Many "—" constructions (55 on the participant page, 80 on the facilitator page). Read every section against Rule 13.
11. Unit 8 follows Unit 7: the Accountability Loop and the Review–Realign–Restore cycle act on the delivery expectations and alignment scores the group set in Unit 7 (Section 5), on the Unit 6 PM scorecards and on the Unit 3 Enterprise OKRs. Neither page refers back yet.

## 6. Tools already on her computer

- `Unit decks\_build\rebuild_u07\` (committed): `build_u07.py` (both pages rebuilt from the backup files by block-level cuts and exact replacements with checks; `guide()` keeps every box in paragraphs), `u7_content.py` (content in two voices), `u7_p.js` and `u7.css` (Section 5 tool: fields and parts lists, drop-down lists of the group's Unit 3 OKRs and Unit 2 SiP, save while typing, one record, Confirm and Print; part 4.2 Portfolio work), `make_previews.py` + `mock-s2r.js`, `test_u07.py` (131 browser checks), `shoot_reflections_u07.py` (pictures for reflection slides), `carol_deck_u07_r3.py` (changes a few slides on top of Carol's own deck; duplicates slides; drops a slide), `patch_links_u07.py` (Capstone boxes and `PULL`, report labels, Learning Portfolio keys), `e2e_u07.py` (end-to-end test with `rebuild_u06\fake-supabase.js`, with controls), `final_scan_u07.py`, `README.md`. Copy the method into `rebuild_u08`.
- `Unit decks\_build\rebuild_u06\`: `fake-supabase.js`, `carol_deck_s5.py`, and the Unit 6 versions of the same scripts.
- `Unit decks\_build\`: `lib2.js`, `kit.js`, `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py`, `reader_assets.py`, `enrich\u08.json`, `unit08.js` (the present Unit 8 deck).
- `build_collection.js` and `check_standards.js` in the repository root. Run `node build_collection.js` on her computer through the device shell after the pages are written.
- Database functions already live: `get_my_capstone` (`p_cohort_id`), `get_capstone_team_oceavl` (`p_team_id`), `capstone_section_box_count` (`p_key`). Box counts after 9 October: unit2 6, unit3 6, unit4 6, unit5 3, unit6 4, unit7 5, unit8 5 (default), unit10 6. Any change: SQL on the model of `Claude outputs\capstone_unit6_boxes.sql`.
- The device shell has Python with python-pptx and Node; it cannot delete and has no route to the internet. The cloud workspace of a new chat starts empty: stage what a step needs, build and test there (Playwright; Carlito for deck and reflection pictures; soffice and pdftoppm for slide pictures), and write the results back.

## 7. State of Units 2 to 7

- Units 2 to 6 are closed (see their handovers).
- **Unit 7 is closed and live (11 October).** Commit `b96be26` (pages, Capstone five boxes 7A to 7E through `PULL.u7`, report labels, Learning Portfolio keys, 24-slide deck). Pushed and checked: 28 files match, live pages read. Carol reported the Storage upload done.
- Her commit `b77bea9` "Unit 7: Section 4 title on the participant page matches the facilitator page and the deck" is pushed (head and origin both `b77bea9`, read 12 October 10:55).
- Unit 7 files as live (md5): `unit3_m1_lens6_p.html` 7e0e47c4…, `unit3_m1_lens6_f.html` 32fee0a2…, `capstone_P.html` c50453f2…, `dashboard_F.html` 11bfb0da…, `build_collection.js` fb7b66e5…, `collection.html` ab4855d9…, deck a0392812… (24 slides; the copy in `Deck upload`). The deck in `Unit decks` now differs: one note changed by the hygiene work (section 9).
- Unit 7, still for her word (none blocks; raise only if she opens Unit 7 again): the four section outcomes Claude reworded (Section 3 second, Section 4 second, both of Section 5); "The Alignment Brigade" in the 3.1 title; "by the end of Q3 2026" in the 4.1 example (Step 2 leader framing, current content; the date has passed); the wording of Capstone boxes 7A to 7E; her own slide titles shorter than the part titles.
- In her git list, `lens_migration_playbook.md` shows as deleted and some older files as changed. They do not come from the unit work; leave them alone.

## 8. Lessons of the Unit 7 round

- Three rounds of amendments came in one day (10:39, 12:20, 12:57), each with screenshots. Build each round as PREVIEW pages and as slide changes on her latest deck; she re-saved her deck four times while Claude worked, so re-stage and compare md5 before every deck write.
- She expects every text box to be clean and every section checked when she says "check all sections". Look at each box as a picture before reporting.
- She moved teaching earlier (the alignment dialogue to 1.4) and turned 4.2 into practice. Expect the same pattern: teach once, practise later, apply in Section 5.
- "Am happy for us to commit now" was her approval to go live: pages, links, end-to-end test, deck upload, push block, in one go.
- When she asks "what are these now?", answer with each open point in one line, what the page says today, and that nothing blocks.
- When she says to remove something "if it is a section that has been deleted", check first; if it is current content, keep it and say where it sits.

## 9. Hygiene of 12 October: built, in review, NOT live

**Her words (10:03):** "So before we start working on unit 8. let us do some hygiene work in the earleir units. 1. Units 1,2 and 3 if am not mistaken have the back to platform button on the right and it white, if one does not know they would miss it. So let us make all the return to platform button on the right in units 4,5...then 2. Please swamp the section 4 with sections 5 in the following units unit 1, 2, 3, 4. The last section must always be the application section with capstone work. Are these clear. Work in all three files for each unit. You are not changing content just swamping sections and renaming them accordingly." With two screenshots (the white button of Units 2–3; the Unit 4 header with the link at the left).
**10:38:** "Unit 2 is messed up. the order cannot be how we changed it now. Please take it back this is the only change." Unit 2 was put back (header change kept).
**10:46:** she asked to confirm group work goes to the Capstone and reflections to the Learning Portfolio: confirmed for Units 2 to 4 (same answer names and save code; `PULL` and `CAPSTONE_KEYS` work by name).

**How it was read (reported to her):** the back link goes to the left as in Units 4 onwards (her screenshot). Unit 1 is not swapped: its last section (Section 6 · Application) already holds the group simulation, and Unit 1 has no Capstone. A swapped section keeps its content; the place keeps its label (4th = "Section 4 · Integration — Collective", 5th = "Section 5 · Application — In Practice"); every part number moves with its content (4.x ↔ 5.x) on pages, slides and notes. Unit Summary, submission cluster and Submit to Facilitator stay at the end of the page. In the Unit Summary the text of each block moves with its section; the arc word stays with the place. In the Unit 3 facilitator file three sentences that named the group work "the Integration section" now say "the Application section". The Unit 3 Capstone section's sub-line still opens with "Integrator Zone" (kept as content).

**What is built (scripts in `Unit decks\_build\hygiene_12oct\`: `hygiene_pages.py`, `swap45.py`, `blocks.py`, `hygiene_decks.py`, `make_previews_hyg.py`, `check_pages.py`, `shoot_ref_u02.py` (now unused)):**
- Pages (built from the live files, not yet written live): header change in `unit1_P/F`, `unit2_m1_lens1_p/f`, `unit2_m1_lens2_p/f`; Sections 4 and 5 swapped in `unit2_m1_lens2_p/f` (Unit 3) and `unit2_m1_lens3_p/f` (Unit 4); "Unit 3, part 4.x" → "Unit 3, part 5.x" in `unit3_m1_lens4_p`, `unit3_m1_lens5_p/f`, `unit3_m1_lens6_p/f` (and, by the swap itself, in the Unit 4 page). Built on her computer and in the cloud with the same md5 (Unit 1 P 617b83f1…, F 06c845ef…; Unit 3 P 7a9eaedf…, F b28328ff…; Unit 4 P d22db90c…, F 7e47d984…; Units 5–7 24784182…, 2fe3e482…, 74eaf084…, 7a685371…, 13e0ebb6…; Unit 2 header-only pages P bceea871…, F 0f2578e7…). Browser check: no page error, tabs, nav buttons and part order right; same answer names and save code before and after.
- Review files: `Claude outputs\Review files\Hygiene 12 Oct\PREVIEW - Unit 1 … Unit 4 Participant/Facilitator.html` (8 files; the Unit 2 pair is the header-only version).
- Decks, written to `Unit decks` (her masters; the copies before are in `Claude outputs\Backups\Hygiene 12 Oct`): Unit 3 (md5 5c27667e…) and Unit 4 (f27020a1…): the Section 4 and Section 5 slides swapped, titles and notes renumbered, divider slides keep the number and arc of their place, the journey slide keeps its five lines and its notes describe the sections in the new order, the Unit 4 reflection oval "5" → "4". Unit 6 (a5ebe841…) and Unit 7 (4c4f4c77…): one note each now says "Unit 3, part 5.2". Unit 2 deck is back to her file (a5006150…, same as the upload copy).
- Backups of every page and deck before the hygiene work, plus `dashboard_F.html` and `collection.html`: `Claude outputs\Backups\Hygiene 12 Oct\`.

**Left to do when she says go (in this order):**
1. Re-run `python3 -B hygiene_pages.py <portal folder> <out>` on her computer from the live files (check the live md5s first; if a page changed since 12 October 10:00, rebuild on it) and write the 13 pages live.
2. `node build_collection.js` (the Unit Summary blocks of Units 3 and 4 changed places), check that only those blocks differ.
3. No report label change is needed (Unit 2 was put back, so "Reflection — Application" stays).
4. Build scripts of Units 4 to 7 (`rebuild_u04`…`rebuild_u07`) still write "Unit 3, part 4.x" and the old section order: note in their READMEs that any rebuild must be followed by `hygiene_pages.py`, or patch `u7_content.py` and `u7_p.js` (two messages and one guidance line).
5. Deck upload: copy the Unit 3, 4, 6 and 7 decks from `Unit decks` to `Claude outputs\Deck upload\Module-2\unit-03.pptx`, `unit-04.pptx`, `Module-3\unit-06.pptx`, `unit-07.pptx`, and remake the reader folders (`reader_assets.py`); Unit 3 and 4 slide order changed, so all pictures change.
6. `node check_standards.js`, then one push block naming every file: the 13 pages, `collection.html`, the four decks, the `hygiene_12oct` scripts, this handover. Then the Storage upload of the four decks with their pictures (`facilitator_decks`, `Module-2` and `Module-3`).
7. After the push: ref check, blob check, read the live Unit 3 and Unit 4 pages.
