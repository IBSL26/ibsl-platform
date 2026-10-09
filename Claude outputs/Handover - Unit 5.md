# Handover — Unit 5 · Aligning Heart & Mind: three-way match

Written 8 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms. She calls Claude "partner"; Claude is the "tech party" and makes the technical decisions.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only).
3. `Claude outputs\Handover - Unit 4.md`, section 9 only (final state of Unit 4: the latest model).
4. `Unit decks\_build\rebuild_u04\README.md` (how the Unit 4 pages and deck are built, checked and tested; reuse the method and the scripts).
5. `Claude outputs\Unit 3 - Three-way match (findings).md` (the format of a findings report Carol has accepted).
6. `Claude outputs\Handover - Deck enrichment.md`, section 12 (change management was added inside Unit 5 on 2 October).

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`).

## 1. The task

Carol's words (8 October): "hand over notes to new chat for threeway check for unit 5".

- **Three-way match:** the participant file, the facilitator file and the deck say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, cases and activities.
- **Clean-up:** bring Unit 5 to the standard Units 2 to 4 now hold (section 3), and remove what breaks her rules (section 2).
- **Order that works:** read-only scan of the three files, then ONE findings report in the chat with the proposed text, then her decisions, then pages, then deck, then slide pictures, then one final scan, then her commit.

## 2. Working rules (all still in force)

- **Claude never runs git in the repository folder, not even to look.** Carol commits in PowerShell. Give her the lines one at a time, each in its own code block, starting with `cd C:\Users\Carol\ibsl-platform`, and say what she should see after each. Name every file in `git add`; never `git add .` (her folder holds many working files that stay off the portal). Database changes go to her as SQL for Supabase.
- On 8 October her pages were not pushed because she ran only the deck lines. When giving page lines and deck lines, give them as ONE block, or say clearly that both blocks must be run.
- Back up before editing: `Claude outputs\Unit 5 file backups\` and `Claude outputs\Unit 5 deck backups\` (create them). Edits are surgical. Do not change IDs, `lens_id`, links, lock logic or database calls unless required.
- Keep encoding and line endings as found. Both Unit 5 files are UTF-8 with CRLF (checked 8 October).
- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of", "in place of"). Never "lens" in visible text or notes. "Strategy2Results®" and "S2R®" always with ®. "SiP", never "SIP". The four SiP areas are "SiP domains".
- No times anywhere. No pre-work. Nothing says anything is automated.
- Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. Online delivery: "post in the chat".
- **Participant file speaks to the participant throughout** ("you / your / your group"): no facilitator cues ("Ask", "Say", "Now ask:", "Tell participants", "Facilitation move") and no third-person framing of the reader (Carol, 8 October). Role cards address the reader in the role ("As COO, you…"). Facilitator file speaks of "participants / the group", is preparation only (no entry boxes) and gives precise, numbered PARTICIPANT ACTIVITY instructions.
- Learning outcomes: "Key learning outcomes" for the unit; two outcomes per section, led by action verbs, faithful to what the section teaches. They name no tool and no step. Carol rewords them herself; propose only when asked.
- Slide text 24pt or larger (Rule 16). Once Carol edits a deck, her file is the master: later changes go into her file, and the build script is a record.
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`. PREVIEW html files are never committed or uploaded.
- Do not spawn subagents.

**How to work with Carol (lessons; these cost her tokens when ignored)**

- Her instruction is final. A question of hers that states what must happen ("should not the submit be at the end?") IS the instruction: do it. Never answer an instruction with options.
- Do not add parts she did not write. Do not replace her wording with yours unless she asks.
- When she says "everywhere", change the pages, the deck, the notes and the slide pictures in the same round. When a rule is set for one unit and the same case exists in another, apply it there too and report it.
- Short replies. One short "what I understand" line, then the work. She reviews wording as review files (PREVIEW pages in the real format) and pictures.
- Report facts that need her word in one line each, with no menu of options.

## 3. The standard Units 2 to 4 now hold (apply to Unit 5)

- **Group work is Capstone work.** The page says so, the group confirms its outputs, the confirmed outputs feed the team's Capstone Blueprint through `PULL` in `capstone_P.html`, and the group work is left out of the Learning Portfolio through `CAPSTONE_KEYS` in `build_collection.js` (then `node build_collection.js` rebuilds `collection.html`). The facilitator report in `dashboard_F.html` shows everything, with labels in `LENS_LABELS` and headings in `FAMILY_DEFS`.
- **Group-work rule:** the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page.
- **Individual exercises and games are Portfolio work.** Sub-line "… · Portfolio Work" and a "Portfolio work · How to complete …" numbered box. **There is NO "Save to Portfolio / Go to Submit" row** (removed from Units 3 and 4 on 7 October): the exercises save as the participant works, and the how-to box ends "… reach your facilitator when you select Submit to Facilitator at the end of the unit."
- **One Submit to Facilitator per unit**, at the end.
- **Worked examples are read-only on both pages.** Group tools follow the worked example step for step, show what earlier steps produced, keep one record, and end with Confirm and Print.
- **Reflection questions** carry `class="ref-prompt"` so the Learning Portfolio prints the question above each answer.
- **Deck:** format of Carol's Unit 2, 3 and 4 decks (design system `Unit decks\_build\lib2.js`; slide types as in `unit04.js`): one slide per part; section slides carry the two outcomes; a "Section N Reflections" slide where a section has reflections (`add_reflection_slides.py`); notes as HEADING, HOW TO TEACH IT, numbered steps with Say / Ask, then ON THE PORTAL, AFTER THE TEACHING (`format_notes_u03.py`, `lint_notes.py`). Model: `Claude outputs\Unit 2 deck - notes as Carol approved them (format model).txt` and her final Unit 3 and Unit 4 decks.
- **Deck reader:** after every deck change remake the reader folder (pictures `s01.jpg` … and `manifest.json`) from the final deck, keep `Unit decks\<deck>` identical to the upload copy, and move surplus pictures to `_to_delete`. Unit 5 is Module 3: `Claude outputs\Deck upload\Module-3\unit-05.pptx` and folder `unit-05`. She uploads both to Supabase (Storage, `facilitator_decks`, `Module-3`) and deletes surplus pictures there. `reader_assets.py` hangs on bare `soffice` in the cloud workspace: convert with the pptx skill's `soffice.py`, then run its picture and manifest steps on the PDF.
- **Three-way scan:** adapt `Unit decks\_build\rebuild_u04\final_scan.py` (outcomes word for word on both pages; every slide string found on a page; no text under 24pt; notes open with a bold heading; leftovers; identical part titles and sub-lines on both pages).

## 4. Unit 5: the files (checked 8 October, read-only)

| What | Where | State |
|---|---|---|
| Participant file | `unit3_m1_lens4_p.html` | last changed 2 October; lens `u3m1_lens4`; UTF-8, CRLF |
| Facilitator file | `unit3_m1_lens4_f.html` | last changed 2 October; UTF-8, CRLF |
| Deck | `Unit decks\Unit 05 - Aligning Heart & Mind.pptx` | 33 slides (2 October, after the change-management additions); identical to `Claude outputs\Deck upload\Module-3\unit-05.pptx`; reader folder `unit-05` holds 33 pictures and the manifest |
| Older copy | `Claude outputs\Unit 5 deck upload\unit-05.pptx` | differs from the deck above; an older upload folder. Do not upload it; ask Carol only if it matters |
| Capstone | `capstone_P.html` | boxes 5A Interpretation risks, 5B Emotional climate, 5C Alignment hot zones, 5D Shared enterprise interpretation, 5E Leadership behaviour commitment; `PULL` has no `u5` row yet |
| Report labels | `dashboard_F.html`, `u3m1_lens4` | labels exist for `ref1`–`ref15`, `wp_*` and others |
| Learning Portfolio | `build_collection.js` | `CAPSTONE_KEYS` has no `u3m1_lens4` entry yet |

**Structure (the same part titles on both pages):** 1.1 The Human Terrain of Strategy Execution · 1.2 The Five Principles of Aligning Heart & Mind · 1.3 Change Management: The 4 Checks of Mind, Heart, Hands and Habit · 1.4 The 3S Check: Shift, Stake, Step · 1.5 The SCARF Model: Five Triggers of Human Resistance · 1.6 The STAT Check: Skill, Time, Authority, Tools · 1.7 ACE-IT: The Observable Behaviour Standard · 2.1 The Ignition Point of Strategy Execution · 2.2 Three Foundational Logics · 2.3 Why Change Must Be Led: Installed and Adopted · 3.1 The COMPASS Framework: Seven High Flammable Zones · 3.2 From High Flammables to Burning Platforms · 3.3 Change Readiness Across the Organisation · 4.1 The Converging Zone · 4.2 Collective Intelligence Across the Leadership Team · 4.3 Leading Change with One Voice · Section 5 (not an accordion; read its structure) · Unit Summary.

**Found in the quick look (to confirm in the full scan):**
1. Facilitator file: time references remain (for example "100 minutes", "12 minutes", "18 minutes"; about 25 matches). They break the no-times rule.
2. Neither page uses the words "Portfolio" or "Capstone". Group work and individual work are not yet marked, and there is no confirm step feeding boxes 5A to 5E.
3. The participant voice rule of 8 October has not been applied to Unit 5. Read every participant section for facilitator cues and third-person framing.
4. The change-management content (1.3, 1.4, 1.6, 2.3, 3.3, 4.3; see `Unit 5 - Change management content (draft for review).docx`) was added on 2 October. Check it against the deck word for word.
5. Unit 4 now ends with the group's ABCV–MBT record (`mbt_*`). Check whether Unit 5 refers back to Unit 4 correctly.

## 5. Tools already on her computer

- `Unit decks\_build\rebuild_u04\`: `build_p.py`, `build_f.py` (pages rebuilt from the original files by exact replacements with checks), `make_previews.py` + `mock-s2r.js` (stand-alone PREVIEW pages), `patch_links.py` (report, Capstone, Learning Portfolio), `final_scan.py`, `export_deck_data.py`. Copy the method into `rebuild_u05`.
- `Unit decks\_build\`: `lib2.js`, `kit.js`, `unit04.js` + `u04_notes.js` (deck and notes model), `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py`, `shoot_reflections_u04.py`, `reader_assets.py`, `enrich\u05.json` (journal insights for Unit 5).
- `build_collection.js` and `check_standards.js` in the repository root.
- The cloud workspace of a new chat starts empty. Stage what a step needs, build and test there (Playwright with the stand-in save; fonts Montserrat and Cormorant Garamond for page pictures; Carlito and Caladea for deck pictures), and write the results back.

## 6. State of Units 2, 3 and 4

- Units 2 and 3 are closed. On 7 October the "Save to Portfolio" row was removed from Unit 3.
- Unit 4 was rebuilt 7 to 8 October (see `Handover - Unit 4.md`, section 9). Pages pushed on 8 October. Carol edited the deck herself (29 slides); her file is the master. Reader folder remade from her deck.
- Open Unit 4 points for Carol's word only: her slide 16 gives the CTO blind spot as Value Proposition while the pages give Arena; her slides 5 and 6 are titled "The Problem with Well-Written OKRs" and "The Four ABCV Integrity Checkpoints" while the pages call that part "Overview — From Unit 3 to Unit 4".
- In her git list, `lens_migration_playbook.md` shows as deleted and `Handover - Deck enrichment.md` as changed. Neither comes from the unit work; leave them alone.

## 7. Final state of Unit 5 (8 October 2026, after "make the changes")

Read `Unit decks\_build\rebuild_u05\README.md` first: it is the full record (files, response keys, links, deck, tests, open points). Sections 1 and 4 above describe the unit before the work.

- **Findings:** `Claude outputs\Unit 5 - Three-way match (findings).md`. Carol answered "make the changes"; everything proposed in it was applied.
- **Pages:** `unit3_m1_lens4_p.html` and `unit3_m1_lens4_f.html` are the builds of `rebuild_u05\build_p.py` and `build_f.py` on the backups in `Claude outputs\Unit 5 file backups\`. They reproduce byte for byte.
- **Group work:** Section 5, Step 4 is Capstone work. The group confirms three entries; `syn_missing_compass` feeds Capstone box 5C through `PULL.u5`. Boxes 5A, 5B, 5D and 5E are typed by the team. Steps 1 to 3 and the 30-Day Behavioural Commitment are Portfolio work.
- **Links:** `capstone_P.html` (`PULL.u5`), `dashboard_F.html` (label for `confirmed_items`), `build_collection.js` (`CAPSTONE_KEYS.u3m1_lens4`), `collection.html` rebuilt. No database change.
- **Deck:** `Unit decks\Unit 05 - Aligning Heart & Mind.pptx`, 40 slides, identical to `Claude outputs\Deck upload\Module-3\unit-05.pptx`. Reader folder `unit-05`: 40 pictures and the manifest, no surplus. Built by `Unit decks\_build\build_u05.sh`. If Carol edits the deck, her file is the master.
- **Checks on the written files:** `final_scan.py` 40 slides, 0 problems. `node check_standards.js`: no Unit 5 breach (the 228 Rule 16 lines are the Unit 01 and Unit 03 decks, as before).
- **Backups:** `Claude outputs\Unit 5 file backups\` and `Claude outputs\Unit 5 deck backups\`.
- **PREVIEW files** in `Claude outputs` are for viewing only. Never commit or upload them.

**Waiting on Carol**

1. Commit and push: the two pages, the three link files, `collection.html`, `Unit decks`, the findings and this handover (one block of lines, given in the chat of 8 October). Claude cannot see git: ask her whether the push is done.
2. Supabase, Storage, `facilitator_decks`, `Module-3`: replace `unit-05.pptx` and the folder `unit-05` (40 pictures and `manifest.json`).

**Open, for her word only (one line each, no options)**

- Capstone boxes 5A, 5B, 5D and 5E have no feed from the unit.
- Section 5, first outcome, says "one strategic change"; the exercise maps two.
- Step 1 names the Unit 3 Start and Stop lists as the source of the two changes; the facilitator briefing keeps "Leaders use the change they carried through the unit as their first map".
- Deck only, no match on the pages: three taglines in 1.2 and the four labels of the kind "Mind · 3S · Explain".
- `Claude outputs\Unit 5 deck upload` is an older folder, superseded.

**Lessons of this round**

- `reader_assets.py` ran in the cloud workspace with bare `soffice` this time. It removes old pictures first, which the device shell cannot do: run it in the cloud and write the folder back.
- Reflection pictures: four on a slide is the limit at 24pt titles. Section 1 has seven, so it takes two slides (1.1 to 1.3, 1.4 to 1.7).
- Python leaves a `__pycache__` folder beside the build scripts; move it to `_to_delete` before the commit lines are given.

## 8. Amendments of 8 October (evening): her instructions (now written, see section 9)

Carol sent amendments after section 7. They are built as review files only: `Claude outputs\PREVIEW - Unit 5 Participant.html` and `PREVIEW - Unit 5 Facilitator.html`. **The live pages, the deck, the Capstone, the facilitator report and the Learning Portfolio are unchanged.** On her word, write the pages, make the links, rebuild the deck and the reader folder, and give one block of commit lines.

Build: `rebuild_u05\amend_p.py <live participant page> <new file>` and `amend_f.py <live facilitator page> <new file>` (they run on the pages as built by `build_p.py` / `build_f.py`). Content: `u5b_content.py`, `oceavl.json`, `u5b.css`, `u5b_p.js`. Previews: `make_previews.py`. Browser test in the cloud: 39 checks, all pass.

**Her instructions, and what the previews hold**

1. 1.2, Principle 1 takes her five-link text (Interpretation, Experience, Choices, Actions, Results) and her closing line, word for word. The lead line and the insight line stay.
2. Change management is 1.3; the tools are 1.3.1 (3S), 1.3.2 (SCARF), 1.3.3 (STAT), 1.3.4 (ACE-IT). Cross-references follow.
3. Participant voice, second pass: 12 more sentences speak to "you" (list `VOICE2` in `amend_p.py`).
4. "3.2 From High Flammables to Burning Platforms" and "Change Readiness Across the Organisation" are deleted from both pages (her words: "Change readiness also must be removed from both"). Section 3 holds one part, 3.1. Reflection `ref14` leaves with it.
5. Section 3: the OCEAVL Assessment takes the place of COMPASS. Source: her own OCEAVL tool (seven dimensions, three levels each: behavioural DNA, risk, response, routines). **It is a personal assessment** (her words: "each person completes the assessment. Then the system gives them the team score after they all submit to their capstone. It would be weird to say out one's score for another person to record it"). On the page each participant scores themselves 1 to 5 on the seven dimensions, reads their own profile and selects Submit to My Team's Capstone. No member names, no scribe. The team's profile (the level held by most members, shown as levels and counts with no names) is shown in the Capstone once every member has submitted. New reflection `ref16`.
6. Section 4: COMPASS is removed. Each role card names its Alignment Hot Zone, aligned to the 17 elements of 3S, SCARF, STAT and ACE-IT (her words). Each role takes one element, and the card shows that element's trigger and two cues word for word from the toolkit: CEO Shift · CFO Transparency · COO Time · CHRO Skill · CTO/CIO Tools · CMO Engagement · CCO Fairness · CPO Authority · CRO Autonomy · CSO Stake. The choice of element for each role and the one linking sentence are Claude's, for her review. Step 2 of Section 5 tells the participant to start with the hot zone of their own role.
7. Section 5 is the Alignment Toolkit (her brief: two cues and the likely trigger for each element; then, based on the Capstone, the triggers most likely to surface and what they will do; the Capstone part goes into the Capstone). Step 1 The Toolkit (17 elements of 3S, SCARF, STAT, ACE-IT) · Step 2 Your Watch List (individual, Portfolio work) · Step 3 Team Alignment Plan (group, Capstone work, Confirm and Print) · the 30-Day Behavioural Commitment stays. The Change Transition Map, Role Connections, Exchange & Dialogue and Plenary Synthesis leave.

**New saved keys (lens `u3m1_lens4`, no database change):** `ref16`, `__oceavl_work` (`{s:[seven scores]}`), `oceavl_scores`, `oceavl_profile` (the participant's own), `__kit_me`, `kit_me`, `__kit_team`, `kit_team`, `kit_mind`, `kit_heart`, `kit_hands`, `kit_habit`; `confirmed_items` names "OCEAVL · My Scores", "Alignment Plan · Mind / Heart / Hands / Habit". No longer written: `ref7`, `ref14`, `ctm1_*`, `ctm2_*`, `wp_*`, `exch_*`, `syn_missing_compass`, `syn_strong_compass`, `syn_sequence`.

**To do on her word**

- Pages: run the two amend scripts on the live pages (back up first), write them back.
- Capstone: the team OCEAVL profile must be worked out from every member's submitted scores. A participant can read only their own `lens_responses`, so this needs a new SECURITY DEFINER function (for example `capstone_team_oceavl(p_team_id)`: for each dimension the count of High, Balanced and Low among members whose `confirmed_items` holds "OCEAVL · My Scores", plus members submitted and members in the team; no names, no single scores). Give Carol the SQL to run in Supabase, with a read-only check first. `capstone_P.html` shows the team profile in section 5 once all members have submitted; the team then types the two highest-risk dimensions and its response. Proposed boxes: 5A from the OCEAVL team profile; 5B to 5E from the Team Alignment Plan, one box for each check. The five box titles and descriptions in `capstone_P.html` need new wording; `PULL.u5` needs five rows.
- `dashboard_F.html`: labels for the new keys; `{7:"COMPASS Diagnostic"}` goes, `ref16` "OCEAVL" comes. `build_collection.js`: `CAPSTONE_KEYS.u3m1_lens4` covers `oceavl_*`, `kit_team`, `kit_mind|heart|hands|habit`, `__oceavl_work`, `__kit_team`; rebuild `collection.html`.
- Deck: Principle 1 slide, numbering 1.3.1 to 1.3.4, Section 3 (OCEAVL in; COMPASS, Burning Platforms and Change Readiness out), 4.1 and 4.2, Section 5 (three steps), Unit Summary, reflection pictures (3.1 is new), notes, reader folder.
- Section 3 and Section 5 learning outcomes still describe the old content. They are hers to reword.
- Section 5 was made clearer on her word ("it is not just clear"): a "How Section 5 works" box above the steps, each trigger shown as a card with its trigger and cues always visible and a "Likely to surface…" button, a count for each check, one example, and a "Go to Step…" button at the foot of Steps 1 and 2.
- New wording by Claude that she has not yet approved: the ACE-IT cues, the 3S / STAT / ACE-IT triggers, the element chosen for each role and its linking sentence, the 3.1 reflection, the guidance notes for 3.1 and Section 5.

## 9. Final state (8 October 2026, late evening): the amendments are written

Carol: "Happy for you to write the live pages." Everything in section 8 is now on the live files. The "To do on her word" list of section 8 is done. Full record: `Unit decks\_build\rebuild_u05\README.md`, section "Amendments of 8 October (evening): written to the portal files".

- **Pages:** `unit3_m1_lens4_p.html`, `unit3_m1_lens4_f.html` (builds of `amend_p.py` / `amend_f.py`).
- **Capstone:** `capstone_P.html`, Unit 5 section: 5A typed by the team under the team OCEAVL profile; 5B to 5E from the confirmed Team Alignment Plan.
- **Report and Learning Portfolio:** `dashboard_F.html`, `build_collection.js`, `collection.html`.
- **Deck:** 39 slides, identical in `Unit decks` and `Claude outputs\Deck upload\Module-3\unit-05.pptx`; reader folder 39 pictures and the manifest.
- **Checks on the written files:** `final_scan.py` 39 slides, 0 problems; `check_standards.js` no Unit 5 breach.
- **PREVIEW files** in `Claude outputs` match the live pages. Never commit or upload them.

**Waiting on Carol (ask her; Claude cannot see git or Supabase)**

1. Commit and push: `unit3_m1_lens4_p.html`, `unit3_m1_lens4_f.html`, `capstone_P.html`, `dashboard_F.html`, `collection.html`, `build_collection.js`, `Unit decks`, the findings, this handover and `Claude outputs/capstone_unit5_oceavl.sql`.
2. Supabase SQL editor: run the five blocks of `Claude outputs\capstone_unit5_oceavl.sql`, one at a time. Block 1 must answer `jsonb`. Block 5 must answer 0; if it is above 0, a team has saved Unit 5 Capstone text under the old box titles and that text needs a look.
3. Supabase Storage, `facilitator_decks`, `Module-3`: replace `unit-05.pptx` and the folder `unit-05` (39 pictures and `manifest.json`), and delete `s40.jpg` there.

**Open, for her word only (one line each, no options)**

- Claude's wording she has not yet approved: the element chosen for each role in 4.2 and its linking sentence; the ACE-IT cues; the triggers for 3S, STAT and ACE-IT; the 3.1 reflection; the guidance notes for 3.1 and Section 5.
- Section 3 and Section 5 learning outcomes still describe content that has left the unit.
- Seven of the 17 toolkit elements are tied to no role.

**Lessons of this round**

- She reviews in the real format. Build review files first when new wording or a new exercise is involved, and write the live files on her word.
- When she says a page "is not just clear", make the page clearer in the same round as the explanation.
- A personal assessment is never completed aloud or typed by another member. Group results from personal data come from the database, as counts with no names.

## 10. Folder layout from 9 October (Carol asked for one working folder)

- Carol reviews decks only in `Unit decks` (one deck per unit, always the current one). Her saved file there is the master.
- Carol uploads to Supabase only from `Claude outputs\Deck upload`. Claude fills it after her review.
- `Claude outputs\Backups` holds every "Unit N deck backups" and "Unit N file backups" folder, the old `Unit 5 deck upload (old copy, 2 Oct)` and the old loose Unit 01 deck copy of 29 September. New backups go here.
- `Claude outputs\Review files` holds the PREVIEW pages, review notes, screenshots and `Unit 2 deck - notes as Carol approved them (format model).txt`. New review files go here.
- The handover notes and the `.sql` files stay loose in `Claude outputs` (they are in git).
- Unit 5 deck: awaiting Carol's review in `Unit decks`. After her review, remake the reader pictures and `Deck upload\Module-3\unit-05.pptx` from her copy; then she uploads.

## 11. Amendments of 9 October (morning): built as review files, NOT yet on the live pages

Carol's instructions, 9 October: (1) 3.1: the participant scores first, the assessment comes before the seven dimensions, and the assessment instructions merge with "How the profile is read"; (2) 4.1 merges with 4.3 under the header "Leading Change with One Voice", the old 4.1 becomes notes inside it, and it is the new 4.1; (3) 4.2 in plain words: what a Converging Zone Contribution is, what an Alignment Hot Zone is, why the two are linked, with a clear narrative for each role ("we are aligning hearts and minds so it must flow and reflect that"); (4) Section 5 applies the 3S Check and ACE-IT only, explained clearly.

- Review files: `Claude outputs\Review files\PREVIEW - Unit 5 Participant.html` and `PREVIEW - Unit 5 Facilitator.html`. The live pages are unchanged (still the 8 October evening version).
- Build: `Unit decks\_build\rebuild_u05\amend2_p.py`, `amend2_f.py`, `u5c_content.py`, `u5c.css`, `test_am2.py`. Chain: file before the three-way match -> build_[p|f].py -> amend_[p|f].py -> amend2_[p|f].py. Browser test: 39 checks, all pass.
- What changed in the review files: 3.1 has one instruction block, then the scores (one row for each dimension with what it covers), own profile, submit, then the seven dimensions, then the reflection. Section 4 has two parts: 4.1 Leading Change with One Voice (with the with/without table as notes, one reflection ref15; ref8 has left) and 4.2 (the two terms explained, why they are shown together, how to read a card; each card: contribution on the left, hot zone on the right with need, why, what sets it off, what you will see and hear, what it costs). Roles keep their elements of 8 October. Section 5: eight elements (3S and ACE-IT), same three steps; the plan confirms as "Alignment Plan · Mind" and "Alignment Plan · Habit" (keys kit_mind, kit_habit; kit_heart and kit_hands are no longer written).
- Still to do after Carol approves the wording: write the two live pages; Capstone Unit 5 boxes go from five to three (5A team behavioural profile, 5B Mind (3S), 5C Habit (ACE-IT)) and `capstone_section_box_count('u5')` goes from 5 to 3 (SQL for Carol, read-only check of the live function first); `dashboard_F.html` labels; rebuild `collection.html`; deck (3.1 order, Section 4 slides merged, Section 5 slides on two tools, reflection slides) and reader pictures. Carol holds her deck review until the deck is rebuilt.
- New wording by Claude awaiting her approval: the 4.2 explanations and the ten role narratives; the "what people need" line and the "what it costs" line on each card; the "What one voice creates" note in 4.1; the Section 5 explanation box.

### Second round, 9 October (same morning), in the same review files

Carol: "let us have meanings for routine - people won't know what these are"; "We are still not clear on these in section 4, what do they actually mean" (the three lines on the role card: what sets it off, what you will see and hear, what it costs); "let us simplify the application and remove personal watch list, so that they just work as a group".

- 3.1: each of the 63 OCEAVL routines now has one plain line of meaning (`ROUT` in `u5c_content.py`; new wording by Claude, each drawn from the response the routine holds in place, in the same order). Shown in the seven dimensions, in the participant's own profile and on the printed copy. Her source instrument carries routine names only.
- 4.2: each role card now tells the role's own story in plain words (`STORY` in `u5c_content.py`): what sets it off, what is seen and heard, what it costs. They are no longer the toolkit lines word for word. "How to read a role card" says what each line is. Roles and elements are unchanged.
- Section 5: two steps (The Toolkit; Team Alignment Plan). The personal watch list has left: `kit_me` and `__kit_me` are no longer written, ids `kitMe` and `sp0` have left. The Unit 3 Start and Stop lists now sit in Step 2. The 30-Day Behavioural Commitment stays as Portfolio work.
- Browser test: 43 checks, all pass. Live pages still unchanged.
- Added to the go-live list: the Capstone team profile shows routine names, so add the meanings there too; deck Section 5 has two steps.

### Third round, 9 October (same morning), in the same review files

Carol: "Let us remove the 30 day behavioural commitment". It has left both review files: the entry box and its note on the participant page, the closing line of "How Section 5 works", the facilitator's closing-commitment guidance and activity line, and the last sentence of the Section 5 block in both Unit Summaries. Key `syn_30day` is no longer written. Section 5 now ends with the Team Alignment Plan and the Unit Outcome. Browser test: 44 checks, all pass. Live pages still unchanged.

- Fact reported to Carol: the second Section 5 learning outcome ("Demonstrate commitment through a behavioural change that strengthens collective alignment") described the commitment; it is hers to reword.
- The 4.2 reflection ("the most important alignment conversation ... in the next 30 days") is a different item and stays.
- Go-live list: deck notes and Unit Summary slide mention the commitment; `dashboard_F.html` keeps the old label for saved answers.

### Fourth round, 9 October (same morning), in the same review files: Section 5 redesigned

Carol: "for the 3 Ss let us have the groups complete it. So based on their strategy they state the shift, the stake and step. Bring back the guiding lesson from section 1. They state what is the change, what will the organisation gain, and what must be done differently. That way we help them reflect and build their case properly. We can then add the ACE-IT and ask them state what behaviours from a leadership team they will expect ... since they will have to check what the team score was on the OCEAVL."

- Section 5 is group work in two steps. Step 1 · The 3S Check: three cards (Shift, Stake, Step), each with the page's own guide from part 1.3.1 (what it is, weak, clear, the move) and one box. Step 2 · ACE-IT: the team's OCEAVL profile, then five cards (Accountability, Commitment, Engagement, Integrity, Transparency), each with the guide from part 1.3.4 (definition, what it does for a new practice, observable) and one box "The behaviour we expect from our leadership team". Record, Confirm and Print at the foot of Step 2.
- The cue-and-trigger toolkit tables and cards have left Section 5 (`toolkit_step1`, `KIT5`, `TEAM_HOW` in `u5c_content.py` are no longer used). The Section 4 role cards are unchanged.
- The team's OCEAVL profile is shown on the unit page itself (read only): `S2R.context()` -> `get_my_capstone` -> `get_capstone_team_oceavl`. Not every member submitted: "Submitted so far: k of n members." Function missing or no team: a line sends the participant to the Capstone Blueprint. No new database object is needed.
- Keys: `__align_work` (the eight answers), `kit_team` (all, as text), `kit_mind` (the 3S text) and `kit_habit` (the ACE-IT text) on Confirm; confirmed names still "Alignment Plan · Mind" and "Alignment Plan · Habit". No longer written: `__kit_team`, `__kit_me`, `kit_me`, `kit_heart`, `kit_hands`, `syn_30day`.
- Build: `u5d_content.py` (content; reads the guide text from the page at build time), `u5d_p.js` (script), `amend2_p.py`, `amend2_f.py`, `u5c.css`; `mock-s2r.js` now returns a sample team profile for the review file. Browser test: 50 checks, all pass. Live pages still unchanged.
- Go-live list now: write the two pages; Capstone Unit 5 boxes five -> three (5A team behavioural profile, 5B the 3S Check, 5C ACE-IT leadership behaviours) with reworded prompts, and `capstone_section_box_count('u5')` 5 -> 3 (read the live function first); routine meanings in the Capstone team profile; `dashboard_F.html` labels; `collection.html`; deck Sections 3, 4 and 5 and reader pictures.
- Facts reported to Carol: the section is still titled "The Alignment Toolkit"; both Section 5 learning outcomes describe content that has changed (hers to reword); the team profile in the review file is sample figures.

## 12. State after the live write of 9 October (morning)

Carol approved the review files ("Am Happy partner Please build the live files") and changed the Section 5 title to "Leading with Clarity".

Written to her computer and checked by checksum:
- `unit3_m1_lens4_p.html` (md5 ba4e92bc4c663dcd6225f12f00c3a4d4), `unit3_m1_lens4_f.html` (md5 90389c03e3ccc50429e637a7a12335c9).
- `capstone_P.html` (Unit 5: 5A team behavioural profile, 5B the change · Shift, Stake and Step, 5C leadership behaviours · ACE-IT; routine meanings in the team profile), `dashboard_F.html` (labels "Leading with Clarity"), `collection.html` (rebuilt; `build_collection.js` unchanged).
- `Claude outputs\capstone_unit5_boxes.sql` (three blocks; sets the Unit 5 box count to 3 and keeps every other unit as it is; tested in a local stand-in database).
- Deck, 38 slides: `Claude outputs\Deck upload\Module-3\unit-05.pptx` (md5 b85a2f9f32ac6de85d5907827f90abdb) with 38 pictures and `manifest.json` in `unit-05`. `s39.jpg` and `ref_4.3.png` moved to `Claude outputs\_to_delete\unit-05 old files (9 Oct)`.
- NOT yet written: `Unit decks\Unit 05 - Aligning Heart & Mind.pptx`. The file was open in PowerPoint on Carol's computer and locked. It still holds the 39-slide deck of 8 October (md5 b2b070c36fdb93b35a8fce166e474a83). When she has closed it, copy the 38-slide deck there (same file as the Deck upload copy).
- Backups: `Claude outputs\Backups\Unit 5 file backups\... - before amendments (9 Oct)` and `Unit 5 deck backups\... - before amendments (9 Oct)`.
- Checks: browser test 52 checks pass; Capstone stand-in test passes (all submitted, some submitted, function missing); `final_scan.py` 38 slides, 0 problems; `node check_standards.js` 228 Rule 16 hits, all in the Unit 01 and Unit 03 decks as before.

Waiting on Carol: (1) close the Unit 5 deck in PowerPoint and say so; (2) the push; (3) the three SQL blocks in `capstone_unit5_boxes.sql`; (4) review the deck in `Unit decks`, then the Storage upload (replace `unit-05.pptx`, upload 38 pictures and `manifest.json`, delete `s39.jpg` and `s40.jpg` in the `unit-05` folder).

Open items for her word: both Section 5 learning outcomes and the second Section 3 outcome describe content that has changed; wording by Claude not yet reviewed line by line: the 63 routine meanings, the ten role stories, the Section 5 example lines, the deck notes for the changed slides.

## 13. Carol's own deck is the master (9 October, later in the morning)

While the live files were being built, Carol reworked the Unit 5 deck herself in `Unit decks` (she took slides from the 38-slide build, wrote her own 3.1 notes, put her own pictures on 4.2 and cut the deck to 35 slides) and attached it: "Please use this one to upload to the deck upload folder. I worked on the notes."

- Her deck as attached is kept in `Claude outputs\Backups\Unit 5 deck backups\Unit 05 - Aligning Heart & Mind - Carol's own deck as attached (9 Oct).pptx` (md5 5ba38151ac2c1bad32038e1843ba8530).
- `Unit decks\_build\rebuild_u05\carol_deck_align.py` brought it in line with the live pages and changed nothing else: notes of slides 1 to 3 and of the Unit Summary (hers were untouched and described the old Section 5), the part lists on the Section 3 and Section 4 openers, "4.3" -> "4.1" on her 4.1 slide, the ten role blocks in the 4.2 notes (now the wording of the live role cards), the Section 4 Reflections slide (two reflections; the "which state" reflection has left the page), Section 5 outcome 1, the closing question, and the ® on Strategy2Results® and S2R® in her 3.1 notes.
- Result: `Unit decks\Unit 05 - Aligning Heart & Mind.pptx` = `Claude outputs\Deck upload\Module-3\unit-05.pptx` (md5 ead55464d8a8189f27a4189b9b276ad0), 35 slides, with 35 pictures and `manifest.json` in `unit-05`. The pictures of slides 36 to 38 went to `_to_delete`.
- THE GENERATOR NO LONGER REPRODUCES THE DECK. `unit05.js` and `u05_notes.js` build the 38-slide version of 9 October. Any later change to the Unit 5 deck is made in Carol's file, by hand or by a small script on top of it.
- Section 5 learning outcome 1 is now "Determine how the organisation will land the strategy agenda." (her wording; `SLO5_1_NEW` in `u5d_content.py`). Outcome 2 is unchanged. Her message ended at "Instead we must have" with nothing after it; reported to her.
- Live pages now: `unit3_m1_lens4_p.html` md5 247f098d064dc14aaafb75b73a903ad8, `unit3_m1_lens4_f.html` md5 824ee601df622a05e69dd94c773e9c7b; `collection.html` rebuilt.
- Scan of her deck against the pages: three items, all her own choices, reported to her: the 3.1 slide title ("Where Does the Leadership Team Stand?") differs from the part title on the pages; her 3.1 notes do not carry the 3.1 reflection question; her 3.1 notes carry "instead of" once and several "not X" lines. `check_standards.js` reports 15 hits of 18pt on slides 32 to 34: empty end-of-paragraph marks left by pasting, with no visible text.
- Waiting on Carol: the push; the three SQL blocks in `capstone_unit5_boxes.sql`; the Storage upload (replace `unit-05.pptx`, upload 35 pictures and `manifest.json`, delete `s36.jpg` to `s40.jpg`).

## 14. Unit 5 closed and live (9 October)

- Push confirmed without git: `.git\refs\heads\main` and `.git\refs\remotes\origin\main` both hold `a5ba52fb7be683ab307135580a4446e04b54db8f`; the five pages in the head commit match the files on her computer.
- Live check: the participant and facilitator pages on ibslportal.netlify.app show the new content (Section 5 "Leading with Clarity", parts 4.1 and 4.2, routine meanings, no watch list, no 30-day commitment). The fetch tool first returned an old stored copy of the participant page; `https://main--ibslportal.netlify.app/unit3_m1_lens4_p.html` showed the true state.
- SQL: the three blocks of `capstone_unit5_boxes.sql` ran (Unit 5 box count 3; units 2, 3, 4 and 10 at 6; unit 6 at 5).
- Storage upload: Carol reported it done (35 slides). It cannot be seen from the workspace.
- Left as they are on her word ("Ok that is alright"): Section 5 outcome 2 and Section 3 outcome 2.
- Next: Unit 6, see `Claude outputs\Handover - Unit 6.md`.
