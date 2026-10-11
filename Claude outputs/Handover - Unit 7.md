# Handover — Unit 7 · Establishing Performance Expectations

Written 11 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms, one click at a time. She calls Claude "partner"; Claude is the "tech party" and makes the technical and database decisions.

Her words (11 October): "Give me hand over notes to unit 7". Take the exact task from her first message in the new chat. Section 1 gives the task Units 2 to 6 went through, which is the expected one.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only; on 11 October it lists Rule 16 lines for decks only).
3. `Claude outputs\Handover - Unit 6.md`: section 9 to the end (her Unit 6 amendments word for word, how they were read, the live write, the end-to-end check, the push, the SQL, the deck).
4. `Unit decks\_build\rebuild_u06\README.md` (how the Unit 6 pages and deck were built, checked and tested; reuse the method and the scripts).
5. `Claude outputs\Unit 6 - Three-way match (findings).md` (the latest findings report Carol accepted).
6. The live Unit 6 pages `unit3_m1_lens5_p.html` and `unit3_m1_lens5_f.html`: the latest model of what Carol approves, Section 5 above all.

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`). Live site: ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase project "S2R Portal Production".

## 1. The task (as done for Units 2 to 6)

- **Three-way match:** the participant file, the facilitator file and the deck say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, cases and activities.
- **Clean-up:** bring Unit 7 to the standard Units 2 to 6 now hold (section 3), and remove what breaks her rules (section 2).
- **Order that works:** read-only scan of the three files, then ONE findings report in the chat with the proposed text, then her decisions, then review files (PREVIEW pages in the real format), then her amendments in rounds, then her approval, then live pages, then the end-to-end test, then deck, then slide pictures, then one final scan, then her commit, SQL and Storage upload.

## 2. Working rules (all in force)

**Git, database, files**

- **Claude never runs git in the repository folder, not even to look.** Carol commits in PowerShell. Give her ONE code block that starts with `cd C:\Users\Carol\ibsl-platform`, names every file in `git add` (never `git add .`; her folder holds many working files that stay off the portal), and ends with `git push`. Say what she should see: the last line ends with `main -> main`.
- To check a push without git: read `.git\refs\heads\main` and `.git\refs\remotes\origin\main` as files (same value = pushed), and compare the blob hash of each file with the tree of the head commit using Python (read the loose objects with `zlib`). Git stores the pages with LF, so hash the LF form as well as the file as it is.
- Checking the live site: the fetch tool reads the unit pages. It cannot read `capstone_P.html` and `collection.html` (their content sits in script); for those two rely on the blob check. If a page looks old, fetch `https://main--ibslportal.netlify.app/<file>`. The device shell and the cloud shell have no route to the live site.
- Database changes go to her as SQL for the Supabase SQL editor, one block at a time, a read-only check first, and she pastes back each result. Test the SQL in a local stand-in database (pglite) first. With the first block, give her the clicks: supabase.com, Dashboard, project "S2R Portal Production", SQL Editor in the left column, empty the typing box, paste, green Run button, the small table underneath.
- Back up before editing: `Claude outputs\Backups\Unit 7 file backups\` and `Claude outputs\Backups\Unit 7 deck backups\` (create them). Edits are surgical. Do not change IDs, `lens_id`, links, lock logic or database calls unless required.
- Keep encoding and line endings as found. Both Unit 7 files are UTF-8, no BOM, CRLF (checked 11 October).
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`. Python leaves `__pycache__` beside build scripts: move it there before the commit lines are given. (An old `__pycache__` sits in `Unit decks\_build\`; it is never named in `git add`.)
- PREVIEW html files are never committed or uploaded. `Claude outputs\Backups`, `Review files` and `Deck upload` are not in git.
- Do not spawn subagents.
- Device tools load through ToolSearch. Never run a staging copy and `device_commit_files` in the same parallel tool block: stage first, commit in a later call, then check md5 on her computer.

**Folder layout (her rule of 9 October: one working folder, no version confusion)**

- She reviews decks only in `Unit decks` (one deck per unit, always the current one). Her saved file there is the master.
- She uploads to Supabase only from `Claude outputs\Deck upload`. Claude fills it after her review.
- `Claude outputs\Backups`: every backup. `Claude outputs\Review files`: PREVIEW pages, review notes, screenshots.
- Handover `.md` files and `.sql` files stay loose in `Claude outputs` (they are in git). Not yet committed on 11 October: this file and the last lines of `Handover - Unit 6.md`. Add `"Claude outputs/Handover - Unit 7.md"` and `"Claude outputs/Handover - Unit 6.md"` to the next `git add` line.

**Wording**

- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of", "in place of"). Never "lens" in visible text or notes. "Strategy2Results®" and "S2R®" always with ®. "SiP", never "SIP".
- No times anywhere. No pre-work. Nothing says anything is automated.
- Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. Online delivery: "post in the chat" (no "at the table", no "in the room").
- **Participant file speaks to the participant throughout** ("you / your / your group"): no facilitator cues ("Ask", "Say", "Tell participants") and no third-person framing of the reader. Role cards address the reader in the role ("As COO, you…"). Facilitator file speaks of "participants / the group", is preparation only (no entry boxes) and gives precise, numbered PARTICIPANT ACTIVITY instructions.
- Learning outcomes: "Key learning outcomes" for the unit; two outcomes per section, led by action verbs, faithful to what the section teaches. They name no tool and no step. Carol rewords them herself; propose only when asked.
- Plain words: every named term is explained where it first appears (Unit 6: "performance management (PM)", "PIP" spelled out); every list of named items carries a meaning for each item; every exercise has a box that says how it works, step by step.
- Slide text 24pt or larger (Rule 16). Once Carol edits a deck, her file is the master: later changes go into her file by a small script on top of it.

**How to work with Carol (these cost her usage when ignored)**

- Her instruction is final. A question of hers that states what must happen IS the instruction: do it. Never answer an instruction with options or a question on the same point.
- Where an instruction can be read two ways, take the plain reading, do it, and say in one line how it was read (Unit 6: "So EXECUTION becomes the only section" was read as both other parts leaving; she did not object).
- Do not add parts she did not write. Do not replace her wording with yours unless she asks; where her sentence breaks a wording rule, reword only that sentence and say so.
- When she says "everywhere", change the pages, the deck, the notes and the slide pictures in the same round.
- Short replies. Tell her in the first line when a file is ready and where it is. She reviews wording as review files and pictures, in rounds.
- Report facts that need her word in one line each, in plain words, with no menu of options. Say what the page shows today and what does not match.
- She may rework a deck herself while Claude builds. Before any deck work, compare the md5 of `Unit decks\<deck>` with the `Deck upload` copy and look for a `~$` lock file (the deck is open in PowerPoint and cannot be replaced). When the lock file is gone and her md5 is unchanged, write the deck without waiting for her to say "closed".

## 3. The standard Units 2 to 6 now hold (apply to Unit 7)

- **Group work is Capstone work.** The page says so, the group confirms its outputs, the confirmed outputs feed the team's Capstone Blueprint through `PULL` in `capstone_P.html`, and the group work is left out of the Learning Portfolio through `CAPSTONE_KEYS` in `build_collection.js` (then `node build_collection.js` on her computer rebuilds `collection.html`). The facilitator report in `dashboard_F.html` shows everything, with labels in `LENS_LABELS`, the numbered reflection map and headings in `FAMILY_DEFS`.
- **How the Capstone link works:** Confirm on the unit page saves each part as plain text under its own key and adds the part's name to the list `confirmed_items`. The Capstone page reads those keys from the member's own unit page and fills the boxes only when the name is in the list. The working entries save under a key that starts with `__` (hidden from the report and the Learning Portfolio). An edit after Confirm takes the names out again.
- **The Learning Portfolio reads the submission.** A member's reflections appear there after that member selects Submit to Facilitator.
- **Group-work rule:** the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page.
- **Individual exercises are Portfolio work.** Sub-line "… · Portfolio Work" and a "Portfolio work · How to complete …" numbered box. The exercises save as the participant works.
- **One Submit to Facilitator per unit**, at the end.
- **Worked examples are read-only on both pages.** Group tools keep one record and end with Confirm and Print.
- **Reflection questions** carry `class="ref-prompt"` so the Learning Portfolio prints the question above each answer. Every reflection box has an `id` and is in the page's `KEYS` list (Unit 6 had one that never saved).
- **Application section, as Carol shaped it in Units 5 and 6:** the groups work on their own strategy; the section runs as numbered steps, each on its own tab, each with the guiding lesson beside the entry boxes; a "How Section 5 works" box opens the section; earlier units' outputs the group needs are shown on the page read-only (Unit 6 Step 4 reads the group's confirmed Unit 3 Enterprise OKRs with `S2R.loadAll('u2m1_lens2')`: `__okr_work.items[{obj, krs:[{t}]}]`, shown only when `confirmed_items` holds "Enterprise OKRs"). No set case and no closing commitment (she removed the 30-day commitment from Units 5 and 6).
- **Capstone boxes follow the unit.** When the unit's group outputs change, the Capstone boxes for that unit are renamed and their number changes, and the database function `capstone_section_box_count` is set to the same number (`Claude outputs\capstone_unit6_boxes.sql` is the model: it keeps every other unit at its live value and can be run twice). Until the number matches, "Send for team confirmation" is refused with "Complete every box".
- **Deck:** format of Carol's Unit 2 to 6 decks (design system `Unit decks\_build\lib2.js`): one slide per part; section slides carry the two outcomes; a "Section N Reflections" slide where a section has reflections; notes as HEADING, HOW TO TEACH IT, numbered steps with Say / Ask, then ON THE PORTAL, AFTER THE TEACHING (`format_notes_u03.py`, `lint_notes.py`). Model: `Claude outputs\Review files\Unit 2 deck - notes as Carol approved them (format model).txt` and her final Unit 3 to 6 decks.
- **Deck reader:** after every deck change remake the reader folder (pictures `s01.jpg` … and `manifest.json`) from the final deck with `reader_assets.py` in the cloud workspace, keep `Unit decks\<deck>` identical to the upload copy, and move surplus pictures to `_to_delete`. Unit 7 is Module 3: `Claude outputs\Deck upload\Module-3\unit-07.pptx` and folder `unit-07`. She uploads both to Supabase (Storage, `facilitator_decks`, `Module-3`) and deletes surplus pictures there.
- **Tests before she commits:** the browser checks of the PREVIEW pages (`test_u06.py`) and the end-to-end test on the real pages with a stand-in database (`e2e_u06.py` + `fake-supabase.js`): unit page saves, Capstone brings the work in, Learning Portfolio shows the reflections and leaves the group work out. Run a control with the unit's link lines taken out, so the test is shown to catch a break.
- **Three-way scan:** adapt `Unit decks\_build\rebuild_u06\final_scan_u06.py`.

## 4. Unit 7: the files (checked 11 October, read-only)

| What | Where | State |
|---|---|---|
| Participant file | `unit3_m1_lens6_p.html` | 128,095 bytes; last changed 29 September; md5 2d913573442a141d9954cd05d2e2fe4a; `LENS_ID="u3m1_lens6"`; UTF-8, CRLF |
| Facilitator file | `unit3_m1_lens6_f.html` | 104,246 bytes; last changed 29 September; md5 460f739591f625b504a4733cd57df82a; UTF-8, CRLF; no entry boxes |
| Deck | `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` | 22 slides; last changed 2 October; md5 baf6833ec7fc640dc4aeda7d88b5fd14; identical to `Claude outputs\Deck upload\Module-3\unit-07.pptx`; reader folder `unit-07` holds 22 pictures and the manifest |
| Deck lock | `Unit decks\~$Unit 07 …` | none on 11 October. Check the md5 again before any deck work; if it differs from the value above, she has edited it and her file is the master |
| Deck generator | `Unit decks\_build\unit07.js`, `outlines\u07.json`, `source\u07.json`, `enrich\u07.json` | the 1 October build; no `rebuild_u07` folder yet |
| Capstone | `capstone_P.html` | boxes 7A Critical delivery expectation, 7B Expectations chain, 7C Ownership readiness, 7D Commitment record, 7E Enterprise practice (all written for the team's own case, "[Case]"); `PULL` has no `u7` row; the live box count for `u7` is 5 (Carol's SQL result of 9 October) |
| Report labels | `dashboard_F.html`, `u3m1_lens6` | labels exist for `ref1` to `ref8` and the `app_…` keys; numbered map 1 to 8; check `FAMILY_DEFS` |
| Learning Portfolio | `build_collection.js` | `CAPSTONE_KEYS` has no `u3m1_lens6` entry; `collection.html` prints each Unit 7 reflection under its title ("✎ Reflection — Your Honest Assessment"), because the questions carry no `ref-prompt` |

**Key learning outcomes (same on both pages; slide 2 says "identical"):** Articulate performance expectations that are clear, strategically relevant and consistent with enterprise outcomes. · Evaluate the readiness of individuals and teams to fulfil their strategic responsibilities. · Recognise the contribution relationships and dependencies that influence organisational performance. · Demonstrate shared ownership and mutual accountability for agreed results.

**Section outcomes (same on both pages):**
- Section 1: Articulate expectations that are clear, consistent with enterprise outcomes and supported by the contributors they depend on. · Evaluate whether individuals have the clarity, capability and commitment to own an expectation.
- Section 2: Explain how establishing expectations builds ownership and mutual accountability. · Recognise how engagement and accountability degrade when expectations are only communicated.
- Section 3: Identify where each executive function tends to set expectations without securing ownership. · Recognise when surface agreement masks unresolved ownership.
- Section 4: Apply a consistent leadership practice for establishing expectations across the organisation. · Interpret alignment conversations to confirm genuine commitment.
- Section 5: Establish a delivery expectation that secures personal ownership of an agreed result. · Record the commitments that make mutual accountability visible.

**Structure (same part titles on both pages):** 1.1 Setting vs Establishing Expectations · 1.2 The Three Conditions of Established Expectations · 1.3 The Expectations Chain · 1.4 The Alignment Dialogue · 2.1 Compliance vs Commitment: The Execution Dynamic · 2.2 Five Mechanisms: Why Expectation Alignment Determines Outcomes · 2.3 Engagement & Accountability: The Two Casualties · 3.1 The Alignment Brigade: CXO Expectation Tendencies & Gaps · 4.1 The Four-Step Expectation Architecture · 4.2 The Alignment Dialogue: Score → Evaluate → Resolve · 5.1 Step 1 · Identify Who You Are Establishing Expectations With · 5.2 Step 2 · Start With the Future · 5.3 Step 3 · Clarify the Delivery Expectation · 5.4 Step 4 · Identify the Expectations Chain · 5.5 Step 5 · Confirm Ownership of the Result · 5.6 Step 6 · If Alignment Is Below 9: Score → Evaluate → Resolve · 5.7 Step 7 · Leader Reflection & Commitment Record · Unit Summary. Section headings differ between the two pages in Section 4 ("The Expectation Architecture" on the participant page, "Cross-Leadership Expectation Architecture" on the facilitator page) and in the sub-lines of Sections 1 to 4.

**Saved answers (participant page):** `ref1` to `ref8` (reflections: 1.1 Your Honest Assessment, 1.2 Which Condition Is Most Often Missing?, 1.3 Map Your Chain, 2.1 Your Team Right Now, 2.2 Your Most Absent Mechanism, 3.1 Your Expectation Gap, 4.1 Which Step Do You Most Often Skip?, 4.2 Practise the Resolve Question; parts 1.4 and 2.3 have none) and `app_role`, `app_future`, `app_outcome`, `app_success`, `app_coord`, `app_concerns`, `app_resolve`, `app_rating`, `app_primary`, `app_action`, `app_reflection` (Section 5: 5.1 role, 5.2 future, 5.3 outcome and success, 5.4 coordination, 5.6 concerns and resolve, 5.7 rating, primary concern, action and reflection; 5.5 saves nothing). The page holds 19 saved text boxes, 19 Save buttons and one Submit to Facilitator.

**Deck slides:** 1 title · 2 Key learning outcomes · 3 The unit journey · 4 Section 1 · 5 "1.1 · Setting and establishing expectations" · 6 "1.2 · Three conditions of established expectations" · 7 "1.3 · The Expectations Chain" · 8 "1.4 · The Alignment Dialogue" · 9 Section 2 · 10 "2.1 · The execution dynamic" · 11 "2.2 · Five mechanisms" · 12 "2.3 · The two casualties" · 13 Section 3 · 14 "3.1 · CXO expectation tendencies" · 15 Section 4 · 16 "4.1 · The four-step Expectation Architecture" · 17 "4.2 · Score → Evaluate → Resolve" · 18 "The Resolve question" · 19 Section 5 · 20 "Role play · Case context" · 21 "Role play: seven steps" · 22 "Unit Summary · Closing".

## 5. Found in the quick look (to confirm in the full scan)

1. **Entries that never save (participant page, Section 5).** The Step 4 chain table (four rows: contributor, chain type drop-down, role in delivering the outcome; eight text entries and four drop-downs) and the Step 5 alignment score box (1 to 10) have no `id` and are in no save call. What a participant types there is lost on reload and reaches neither the facilitator nor the Learning Portfolio. Put this first in the findings report.
2. **Section 5 is a role play on a set case**, done by each participant: a given SiP ("The most responsive and trusted partner in our market…") and a given Key Result ("Cut customer complaint resolution time from 48 hours to 12 hours by Q3 2026"). It feeds nothing: no Capstone marking, no Confirm, no `PULL.u7`, no `CAPSTONE_KEYS` entry. The five Capstone boxes 7A to 7E speak of the team's own case, and 7A begins "Select one Key Result for [Case]". In Units 5 and 6 Carol turned the application section into group work on the team's own strategy, with the group's own Unit 3 Key Results shown on the page. Put this in the findings report as a fact with the proposed text; the design is hers.
3. **A commitment closes Unit 7.** Step 7 ends with "Overall Reflection & 5-Day Commitment" (`app_reflection`), and the closing slide reads "Commit to that alignment dialogue within five working days". Carol removed the closing commitment from Units 5 and 6. For her word, one line.
4. **Times.** Facilitator file: "Timing: 15 min per round (two rounds minimum)" in the Section 5 role-play guidance, and "3 minutes, three columns" in the 1.3 guidance. Deck notes: slide 3 ("15 minutes"), slide 7 ("3 minutes"), slide 19 ("15 min"). They break the no-times rule.
5. **In-room wording.** Facilitator file and notes of slides 3, 19 and 21: "Pairs or triads", "Debrief in plenary", "Rotate roles". Delivery is online; the wording needs her word on how the role play runs online.
6. **Neither page uses "Portfolio Work", "Capstone" or "your group"** as marking. Individual work and group work are not yet marked. The reflection status line reads "✓ Saved to your portfolio".
7. **Reflections have no `class="ref-prompt"`** (8 reflections).
8. **"The Alignment Brigade" is still the title of 3.1** on both pages and in the notes of slide 14. In Unit 6 Carol renamed 3.1 from "The Alignment Brigade" to "Unity in Diversity". For her word, one line.
9. **Facilitator file:** 18 FACILITATOR GUIDANCE boxes and only 2 PARTICIPANT ACTIVITY notes (the standard is one precise, numbered note wherever participants do an activity: eight reflections and seven steps on the participant page).
10. **Deck against the standard:** no "Section N Reflections" slides; slide 18 "The Resolve question" has no part of its own on the pages (it belongs to 4.2); Section 5 has two slides for seven parts; the notes open with the part title, then "FACILITATOR GUIDANCE" and "Content:", and do not follow the approved format (HOW TO TEACH IT, numbered Say / Ask, ON THE PORTAL, AFTER THE TEACHING appear on no slide); slide titles differ from the page part titles (for example "1.1 · Setting and establishing expectations" on the slide, "1.1 — Setting vs Establishing Expectations" on the pages; "3.1 · CXO expectation tendencies" against "3.1 — The Alignment Brigade: CXO Expectation Tendencies & Gaps"). All explicit text sizes on the slides are 24pt or larger; `check_standards.js` is the authority.
11. Neither page names Unit 3, Unit 5 or Unit 6 or what the group now leaves them with (Unit 3 Enterprise OKRs; Unit 5 Alignment Plan; Unit 6 PM architecture with the CEO and CFO scorecards on two Key Results). "OKR" appears twice in teaching text ("the OKR/KPI"; the CSO card). The facilitator guide opens with "If you distributed your team's scorecard right now…", which now follows directly from the Unit 6 scorecards. Check where Unit 7 should refer back.
12. "automatically" appears once on each page inside teaching text (the CEO card: "The assumption that strategic clarity cascades automatically into execution commitment…"). It describes the organisation. Report it; change only on her word.
13. Many "—" constructions in the teaching text (74 dashes on the participant page, 90 on the facilitator page; for example "Was the expectation set — or was it established?"). Read every section against Rule 13.
14. The Alignment Dialogue is taught twice (1.4 and 4.2) and practised in 5.5 and 5.6. Check the three for the same wording of the question, the scale and the threshold ("below 9").

## 6. Tools already on her computer

- `Unit decks\_build\rebuild_u06\` (all committed): `build_u06.py` (both pages rebuilt from the backup files by block-level cuts and exact replacements with checks; `acc_start()` finds the real opener of a part), `u6_content.py` (content in two voices, participant and facilitator), `u6_p.js` and `u6.css` (the Section 5 step tool: fields list, parts list, save while typing, Confirm, read of the Unit 3 Key Results), `make_previews.py` + `mock-s2r.js` (stand-alone PREVIEW pages), `test_u06.py` (100 browser checks), `patch_links_u06.py` (Capstone boxes and `PULL`, report labels, Learning Portfolio keys), `e2e_u06.py` + `fake-supabase.js` (end-to-end test on the real pages), `carol_deck_s5.py` (changes a few slides on top of Carol's own deck and keeps the rest untouched; copies the notes placeholders when a slide is duplicated), `final_scan_u06.py`, `README.md`. Copy the method into `rebuild_u07`.
- `Unit decks\_build\`: `lib2.js`, `kit.js`, `unit05.js` + `u05_notes.js` (deck and notes model), `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py`, `reader_assets.py`, `enrich\u07.json` (journal insights for Unit 7), `unit07.js` (the present Unit 7 deck).
- `build_collection.js` and `check_standards.js` in the repository root. Run `node build_collection.js` on her computer through the device shell after the pages are written.
- Database functions already live and usable from a unit page through `S2R._client.rpc(...)`: `get_my_capstone` (`p_cohort_id`), `get_capstone_team_oceavl` (`p_team_id`), `capstone_section_box_count` (`p_key`).
- The device shell has Python with python-pptx and Node; it cannot delete and has no route to the internet. The cloud workspace of a new chat starts empty: stage what a step needs, build and test there (Playwright; fonts Montserrat and Cormorant Garamond for page pictures; Carlito and Caladea for deck pictures; pglite for SQL), and write the results back.

## 7. State of Units 2 to 6

- Units 2, 3, 4 and 5 are closed (see their handovers).
- **Unit 6 is closed and live (9 October).** Head commit `5397a14` ("Unit 6 deck: Section 5 slides for the PM architecture"; parent `e431c08`, the pages). Live pages read after the push. SQL ran: unit2 6, unit3 6, unit4 6, unit5 3, unit6 4, unit7 5, unit10 6. Carol reported the Storage upload done (28 slides; not visible from the workspace).
- Unit 6 files as they stand (md5): `unit3_m1_lens5_p.html` 5d59c4c5…, `unit3_m1_lens5_f.html` 9ade8077…, `capstone_P.html` 6f9e241a…, `dashboard_F.html` 716fcd6e…, `build_collection.js` 9c9ba386…, `collection.html` de88dfd1…, deck 570180bc… (28 slides; slides 1 to 22 are Carol's own, untouched).
- Unit 6, still for Carol's word (reported to her on 9 October, no answer yet; raise only if she opens Unit 6 again): both Section 4 learning outcomes and the second Section 5 outcome describe content that has left; on her own slides, slides 19 and 20 are numbered 3.3 and 3.4 while the pages say 3.2 and 3.3, slide 18 carries "The Alignment Brigade", slide 8 gives Sight 3 as "typically 5 – 10%" while the pages say 20–40%, slide 14 has text under 24pt, and the notes of slides 3, 12, 17 and 21 carry times.
- In her git list, `lens_migration_playbook.md` shows as deleted and some older files as changed. They do not come from the unit work; leave them alone.

## 8. Lessons of the Unit 6 round

- After the findings report she sent her amendments as one long message, part by part, and one more line while the work was running. Build exactly that list; keep her sentences; report the few readings in one line each.
- She reworked the deck herself in the same days. Her file became the master, and only the Section 5 slides were changed, by a script on top of her file. Ask nothing; check the md5 and the lock file.
- Before she commits she asks whether the Capstone work and the reflections land where they should. Run the end-to-end test before the push block is given, and say plainly what was tested on real pages and what was only wired.
- Give the push block once, complete. If files are added afterwards, give the whole block again.
- Check every entry box for an `id` and a save call during the first scan (Unit 6: one reflection; Unit 7: thirteen entries, section 5 point 1).
- The stand-in database copies the box-count rule; the real database function was not read. Say so.
- After "pushed", check the two git ref files, the blob hashes and the live unit pages, and report in plain words. Then SQL, one block per message, with the clicks.
- After the Storage upload she says "Done"; it cannot be seen from the workspace. Close the unit in the handover and list what is still open for her word.

## 9. Three-way match done; Carol's amendments of 11 October: built as review files, NOT yet on the live pages

- Findings report: `Claude outputs\Unit 7 - Three-way match (findings).md` (read-only scan; twelve points for her word).
- She answered with her own amendments (below). Build: `Unit decks\_build\rebuild_u07\` (README there). Review files: `Claude outputs\Review files\PREVIEW - Unit 7 Participant.html` and `PREVIEW - Unit 7 Facilitator.html`. Backups: `Claude outputs\Backups\Unit 7 file backups\… - before amendments (11 Oct).html`. The live pages, the links and the deck are unchanged.
- Her deck: she saved `Unit decks\Unit 07 - …pptx` on 11 October at 09:47 (md5 ba16418a…; the handover table above gives the older value). Only the notes of slides 1 and 3 differ from the `Deck upload` copy. Her file is the master; a copy is in `Backups\Unit 7 deck backups`.

**Her instructions, 11 October (her words):**

1. "Remove all times."
2. "Section 3 - extrapolation - can we add likely expectations chain for each role. So instead of just having tendency and gap, we add who is likely to be in their expectations chain."
3. "Section 4. Improve facilitator section on how to explain the — The Four-Step Expectation Architecture. use the format in the participant file."
4. "4.2 Add an exercise for the facilitator for role play the alignment dialogue. Please add the GROW model as the coaching model to use when having the alignment dialogue. Which means you will add the learning content on the grow model in the participant file too."
5. "Section 5. Refine the exercise in participant profile to be included in the capstone work. So build fields to capture the information for the four steps, giving precise instruction and narrative of what information is captured. Here they apply the process to two Objectives and one related key results for each objective. So section 5 is changing to just have the participants complete the four steps. - 1. Start With the Future 2. Clarify the Delivery Expectation 3. Identify the Expectations Chain 4. Confirm Ownership. Work on these then we will work on the final PPT."
6. While the build ran: "Amend the section outcomes according to the content. I see section 1 outcome are not linked to the content", then her wording for Section 1: "Understand the distinction between setting vs establishing expectations" and "Design clarity, capability and commitment to establish expectations."
7. While the build ran: "We are not adding time to any files or PPT." (standing rule for every unit file and deck)

**How Claude read the points that could be read two ways (all reported to her):**

- "Remove all times" and "just … the four steps": the five-day window left with them (the box after Step 7, the 3.1 reflection hint, "this week" in the CSO question, the Facilitator Closing Note). "By when" in Step 2 is the delivery date of the Key Result, from her Clarity text and Capstone box 7A; it stays.
- "use the format in the participant file": facilitator 4.1 now has the four step cards of the participant page (Purpose, Leader framing, Why it matters), each with a row "How to explain it", and a closing box "How to explain the four steps".
- Step 4 is "Confirm Ownership" everywhere (her list, the facilitator tab and slide 16); the participant card read "Confirm Ownership of the Result".
- The role play is an in-session exercise on the facilitator page only (nothing entered on the portal). The participant page takes the GROW learning content.
- Section outcomes: Section 1 in her words; Section 2 kept; Section 3 second, Section 4 second and both Section 5 outcomes reworded by Claude to the content.
- Section 5: each Capstone text names the Objective and the Key Result. The owner of each Key Result is one entry in Step 1 (the old Step 1 "who").

**Standard fixes made in the same build** (the findings report, "What I will put right"): one shared text in the fuller facilitator wording for 1.1, 1.2, 1.3, 2.1, 2.2, 2.3 and 4.2; role cards speak to the participant in the role; `ref-prompt` on the eight reflections; 12 PARTICIPANT ACTIVITY notes; room wording out; the 1.4 guidance scale (9 or 10); the Resolve question in full; Unit Intent in her slide 1 wording; "Key performance indicator (KPI)" at first mention; the manuscript opening in 1.1; the tabs of facilitator 4.2 now sit side by side.

**Still for her word (reported in the findings report, no answer yet):** "The Alignment Brigade" in the 3.1 title · the Section 4 title (two versions) · "by the end of Q3 2026" in the 4.1 example · "vs" in two part titles against the deck · "automatically" in the CEO card · the unit sub-title "Influence" on the participant page.

**Checks:** browser test 116 checks, all pass; every inline script passes a syntax check; `<div>` balance and CRLF kept; phone width no wider than before the amendments.

**Waiting on Carol:** her review of the two PREVIEW files, in rounds. After her word: the go-live list in `rebuild_u07\README.md` (pages, Capstone four boxes and `PULL.u7`, box count SQL 5 → 4, report labels, Learning Portfolio keys, end-to-end test, deck on top of her file, reader pictures, final scan, commit lines).

Add to the next `git add` line: `"Claude outputs/Unit 7 - Three-way match (findings).md"`, `"Claude outputs/Handover - Unit 7.md"`, `"Claude outputs/Handover - Unit 6.md"` and the files of `"Unit decks/_build/rebuild_u07/"` by name. PREVIEW files are never committed.

## 10. Round 2 of 11 October (12:20): her review of the PREVIEW pages; built as review files and on the deck

**Her instructions (her words):**

1. "For future slides do not start with the questions on content that has not been taught. See how the uploaded PPTs have been written - this is for facilitator notes" (standing rule for every deck).
2. "Bring the teaching of the alignment dialogue from 4.2 — The Alignment Dialogue: Score → Evaluate → Resolve to Awareness section 1.4. But leave the role play in 4.2. Amend the PPT slides accordingly for this as well." Later in the same message: "The teaching for alignment dialogue moves to section 2 . in both profiles".
3. "Build a reflection slide for section 3.1 in the format of the other decks." "Add reflections slides in section 4."
4. With a picture of the "How to explain it" row: "Remove this part in the four steps in the facilitator profile." With a picture of the "How to explain the four steps" box: "This explanation must come before the cards for the four steps."
5. "Then 4.2 becomes the practice of the alignment dialogue using the grow model in class then for the participant it becomes the portofolio work for which key results they might need to have an alignment dialogue with the board chairman. They complete the ALignment to move the chair to a score of 10 using the goal model. Add a generic scenario that their board chair has disagreed with the current metrick and timeframe for the choosen key result. So the difference with the facilitator is that in class this is practiced between any roles that the facilitator chooses. Then for the participant is it a profolio work. The instruction in the facilitator must be clear."
6. "Section 5 Remove the stated objective and use the drop down instead, then remove also this SIP and add a drop down menue too. Instruction 3 changes from Read your Success in Practice below. For each Key Result, write the part of that Future it serves - to For each Key Result, write the part of that Future it serves. Be clear here in instruction 4 and add ...Write the leader framing: the sentence that you say to leader connected the Key Result to that Future. Also reframe wll participant to first person reference appropriately."
7. "Amend only the relevant PPT slides. Make these changes."

**How Claude read the points that could be read two ways (all reported to her):**

- The teaching of the dialogue (Score → Evaluate → Resolve and GROW) went to 1.4, as her first sentence says ("Awareness section 1.4"); "section 2" in the later sentence was read as the same move. The reflection "Practise the Resolve Question" (`ref8`) went to 1.4 with its teaching.
- 4.2 is retitled "Practising the Alignment Dialogue", sub-line "GROW coaching model · Portfolio Work" (NEW wording). "the goal model" was read as the GROW model.
- The scenario gives the chair's first score as 5 (NEW), so that the participant has a starting point for moving the chair to a 10.
- Section 5: the SiP drop-down list chooses the Success in Practice statement; the box "The part of that Future it serves" stays, as her instruction 3 says "write".
- "first person reference": the participant page speaks to "you" throughout; the Section 5 instructions no longer say "the leader asks" or "one member".
- Deck: "relevant slides" was read as the slides whose content changed on the pages: the two 1.4 teaching slides, the 4.2 practice slide, the two reflection slides, the second outcome on the Section 3 and Section 4 slides, the Section 5 slides and the closing slide (five-day window). Her slides 1 to 12, 14 and 17 are untouched.

**Her deck:** she saved it again at 12:19 and at 12:25 (23 slides, md5 159d0249…): her own notes on slides 3 to 12, 14, 16 and 17, a "Reflections" slide after 3.1, an empty slide after 4.2, and a picture in place of the ten role boxes on the 3.1 slide. That file is the master and is kept as `Backups\Unit 7 deck backups\Unit 07 - Carol's own deck as saved (11 Oct 12h25).pptx`. The deck written to `Unit decks` has md5 ce04640f… (25 slides). `carol_deck_u07.py` built the 25-slide deck on top of it (README in `rebuild_u07`). `Deck upload\Module-3\unit-07.pptx` and its reader pictures still hold the deck of 2 October; refresh them after her review of the deck in `Unit decks`.

**Checks:** browser test 127 checks, all pass; build reproduces on her computer; `node check_standards.js` on a copy with the two built pages: no breach; her untouched slides compare equal in XML, shapes and notes; no slide text under 24pt; no times in the notes of the deck.

**Still for her word:** the four section outcomes Claude reworded (Section 3 second, Section 4 second, both of Section 5); "The Alignment Brigade" in the 3.1 title; the Section 4 title (two versions); "by the end of Q3 2026" in the 4.1 example; slide titles that differ from the part titles on her own slides.

**Waiting on Carol:** her review of the two PREVIEW files and of the deck in `Unit decks`. Then the go-live list in `rebuild_u07\README.md`.

## 11. Round 3 of 11 October (12:57): clean text boxes, the facilitator guides (does not review) group work, Section 5 in two exercises

**Her instructions (her words):**

1. "Please clean the text boxes - do not clutter text. Check all sections."
2. "The facilitator does not review group work so the wording on the group exercise must neve be - e.g Listen for a statement that links the expectation to the SiP future. Challenge any statement that describes a task without the future it serves. Watch for: an owner named as a department. Ask which executive role answers for the Key Result. All the capstone work is independently reviewed during graduation. The facilitator must just guide hoe the work is completed." (standing rule for every unit)
3. "Add Alignment dialogue exercise for the group in section 5 application. So we have 2 exercises. 5.1 Building the expectation architecture which is the current content. Then 5.2 Conducting alignment dialogue with board chair. We repeat the exercise here for preparing to have an alignment dialogue moving the chair to a 10 but now as a group and this goes in the capstone."
4. With a picture of the last lines in the 4.2 reflection picture ("This is Portfolio work. Your entries save as you type…"): "remove this part from the reflection screenshot."
5. "Also remove unit summary slide. Amend the last section slide/s for section 5."

**What was built (review files and deck only; the live pages are unchanged):**

- **Text boxes:** the cause of the cluttered Section 5 box was a build fault (bold lead-ins were written without paragraphs). `guide()` now gives every line its own paragraph, on every box of the facilitator page; the test checks that no box holds loose text. The per-step group boxes and the per-step guidance and activity notes in Section 5 have left; each exercise has one PARTICIPANT ACTIVITY note.
- **Facilitator Section 5:** one guidance box in four short lines (Your role · Order · Before the group starts · To finish), one "How Section 5 works" box, then 5.1 (the lesson participants see and "What each group completes" for each step) and 5.2 (scenario and what each group completes). No "listen for", "challenge", "watch for" or "check"; the build stops if one appears.
- **Participant Section 5:** 5.1 Building the Expectation Architecture (the four steps as before) and 5.2 Conducting the Alignment Dialogue with the Board Chair: one drop-down list for the Key Result, the scenario of part 4.2, four boxes (Goal, Reality, Options, Will) with the part 1.4 lesson above each. One record for both exercises, Confirm and Print. New keys: `dg_kr`, `dg_goal`, `dg_reality`, `dg_options`, `dg_will` in `__ex_work`; on Confirm `ex_dialogue` and the name "Expectations · Alignment Dialogue". 47 entries in all.
- **Overview box** (Tone & watch points): the Application line now names both exercises.
- **Deck (24 slides, md5 a0392812…):** built by `carol_deck_u07_r3.py` on her own file of 12:56 (24 slides, md5 1e56c277…, kept as `Backups\Unit 7 deck backups\Unit 07 - Carol's own deck as saved (11 Oct 12h56).pptx`; she had removed the "Two Objectives" slide). Slides 1 to 20 untouched. Slide 21: the 4.2 picture shows the title and the four instructions only. Slide 22: Section 5 opener notes for two exercises. Slide 23: "5.1 · Building the Expectation Architecture". Slide 24 (new): "5.2 · The Alignment Dialogue with the Board Chair". The "Unit Summary · Closing" slide has left.

**How Claude read the points that could be read two ways:**

- "Check all sections": every guidance box on the facilitator page was looked at as a picture. The 4.2 role play box keeps its "Watch for" list: it is class practice led by the facilitator, with nothing entered on the portal and nothing in the Capstone.
- 5.2 uses the same scenario as 4.2 (the chair disagrees with the metric and timeframe and gives a 5). The Key Result is chosen afresh by the group from the drop-down list.
- The slide title for 5.2 is "5.2 · The Alignment Dialogue with the Board Chair" so that it fits one line at the size of the other titles; the page title is "5.2 — Conducting the Alignment Dialogue with the Board Chair".
- "remove unit summary slide" was read as the slide only. The Unit Summary part on the two pages stays (its wording now names both exercises).
- The Capstone keeps five Unit 7 boxes at go-live (7A to 7D the four steps, 7E the alignment dialogue), so the box count in the database stays 5.

**Checks:** browser test 130 checks, all pass; her slides 1 to 20 compare equal in XML, shapes and notes; no slide text under 24pt; no times and no review wording in the Section 5 notes.

**Still for her word:** as in section 10.

**Waiting on Carol:** her review of the two PREVIEW files and of the deck in `Unit decks`. Then the go-live list in `rebuild_u07\README.md`. Add `carol_deck_u07_r3.py` to the files named in the `git add` line.

## 12. Live write of 11 October (13:30): "Am happy for us to commit now"

- Her word was read as approval of the two PREVIEW pages and the deck, and as the instruction to go live. No change between the round 3 PREVIEW build and the live pages.
- **Written to the portal folder** (md5 in `rebuild_u07\README.md`, "Written to the portal folder"): `unit3_m1_lens6_p.html`, `unit3_m1_lens6_f.html`, `capstone_P.html` (Unit 7: five boxes with new content, 7A to 7E, brought in through `PULL.u7`), `dashboard_F.html` (two headings and the labels for `ad_*` and `ex_*`), `build_collection.js` (`CAPSTONE_KEYS.u3m1_lens6`), `collection.html` (rebuilt with `node build_collection.js` in the portal folder).
- **Backups:** `Backups\Unit 7 file backups\… - before Unit 7 links (11 Oct)` (the three link files and `collection.html`) beside the two pages "before amendments (11 Oct)". Old upload copy of the deck: `Backups\Unit 7 deck backups\Deck upload (old copy, 2 Oct)`.
- **Database:** no change. Unit 7 keeps five Capstone boxes and the box count is 5.
- **Deck:** `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` and `Claude outputs\Deck upload\Module-3\unit-07.pptx` are identical (24 slides, md5 a0392812…). Reader folder `unit-07`: 24 pictures and `manifest.json`.
- **Checks:** end-to-end test on the real pages with a stand-in database, 37 of 37 (`e2e_u07.py`); `node check_standards.js` on the portal folder, no page breach; final scan (`final_scan_u07.py`) clean on the pages and on slides 22 to 24. On her own slides, hers to decide: shorter slide titles for 1.1, 1.2, 2.1, 2.2, 2.3 and 3.1; no full stop after the first Section 1 outcome on slide 4.
- **Learning Portfolio:** the Unit 7 chapter now has two headings (Reflections; Practising the Alignment Dialogue). With two headings a chapter opens closed on screen and prints open.
- **Old Capstone text:** a team that typed into the old Unit 7 boxes before today keeps that text under the new headings until it brings in again or edits. No cohort had reached Unit 7 when this was written (not visible from the workspace).
- **Waiting on Carol:** (1) the push (one block, given to her); (2) the Storage upload (`facilitator_decks`, `Module-3`: replace `unit-07.pptx`; folder `unit-07`: the 24 pictures and `manifest.json`). Then check the push without git and read the live pages. This section is in the commit; later lines of this note go in the next `git add`.
