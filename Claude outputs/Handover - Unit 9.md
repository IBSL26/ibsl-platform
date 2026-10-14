# Handover — Unit 9 · Strategic Unclogging

Written 13 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party" and makes the technical and database decisions.

Her words (13 October, 17:43): "Give me tranfer notes for unit 9 to a new chat". Take the exact task from her first message in the new chat. Section 1 gives the task Units 2 to 8 went through, which is the expected one.

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 8.md`, sections 2 and 3: the working rules and the standard Units 2 to 8 hold. They apply to Unit 9 word for word. This file does not repeat them.
3. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only).
4. `Unit decks\_build\rebuild_u08\README.md` and the scripts beside it: the latest method (build from the backups, PREVIEW pages, browser checks, end-to-end test, deck script on top of Carol's deck, reflection pictures, reader folder). Reuse and adapt them for Unit 9.
5. The live Unit 8 pages `unit3_m2_lens7_p.html` and `unit3_m2_lens7_f.html`: the latest model Carol approved (Section 5 tool, 4.2 Portfolio case, reflection pictures in the deck).
6. Section 5 of this file: what Unit 8 taught about working with Carol.

Folder on her computer: `C:\Users\Carol\ibsl-platform` (in the device shell `$HOME/mnt/ibsl-platform`). Live site: ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase project "S2R Portal Production".

## 1. The task (as done for Units 2 to 8)

- **Three-way match:** the participant file, the facilitator file and the deck say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, cases and activities.
- **Clean-up:** bring Unit 9 to the standard of Units 2 to 8, and remove what breaks her rules.
- **Order that works:** read-only scan of the three files, then ONE findings report (`Claude outputs\Unit 9 - Three-way match (findings).md`) with the proposed text, then her decisions, then review files (PREVIEW pages in `Claude outputs\Review files\Unit 9`), then her amendments in rounds, then her approval, then live pages, Capstone link, report labels and Learning Portfolio, then the end-to-end test, then the deck, then the reflection pictures and reader folder, then one final scan, then her push, SQL and Storage upload.

## 2. Unit 9: the files (checked 13 October, read-only)

| What | Where | State |
|---|---|---|
| Participant file | `unit3_m2_lens8_p.html` | 121,359 bytes; md5 d41da670a2a24bcbff7d977922d50d34; `LENS_ID="u3m2_lens8"`; UTF-8, no BOM, CRLF |
| Facilitator file | `unit3_m2_lens8_f.html` | 95,267 bytes; md5 b65a81baa2d0333f0ce807ce7ff027ae; UTF-8, no BOM, CRLF; no entry boxes |
| Deck | `Unit decks\Unit 09 - Strategic Unclogging.pptx` | 25 slides; md5 bc4df3b9c26e68c79d10158e6254426d; identical to `Claude outputs\Deck upload\Module-3\unit-09.pptx`; reader folder `unit-09` holds 25 pictures and the manifest (all uploaded to Storage on 13 October) |
| Deck lock | `Unit decks\~$Unit 09 …` | none on 13 October. Check the md5 again before any deck work; if it differs, she has edited the deck and her file is the master |
| Deck generator | `Unit decks\_build\unit09.js` and the `outlines`, `source`, `enrich` json of the 1 October build | no `rebuild_u09` folder yet |
| Capstone | `capstone_P.html` (md5 9c244e49…) | five boxes, all for the team's own case: 9A Friction signals, 9B Clog diagnosis, 9C Unclogging levers, 9D Unclogging rhythm, 9E Unclogging agenda. `PULL` has no `u9` row. The database box count for `u9` is 5 (`capstone_section_box_count`) |
| Report labels | `dashboard_F.html` (md5 eacaeaab…), `u3m2_lens8` | labels for `ref1` to `ref6`, `app_prep`, `app_clog`, `app_lever`, `app_followup`; numbered map 1 to 6; no `FAMILY_DEFS` heading for Unit 9 |
| Learning Portfolio | `build_collection.js` (md5 7911dbc5…) | `CAPSTONE_KEYS` has no `u3m2_lens8` entry |

Backups go in `Claude outputs\Backups\Unit 9 file backups\` and `Claude outputs\Backups\Unit 9 deck backups\` (create them). Copies of the Unit 9 pages and deck as they stood before the wording change of 13 October are in `Claude outputs\Backups\Brigade wording backups (13 Oct)`.

**Section outcomes (same on both pages):**
- Section 1: Recognise the systemic blockages that widen the gap between strategic intent and execution. · Identify the observable symptoms of friction in execution.
- Section 2: Explain why execution friction is a predictable consequence of strategy stretching the operating system. · Recognise the leadership disciplines that detect and resolve friction early.
- Section 3: Evaluate where interdependent conditions are causing friction to accumulate across the enterprise. · Distinguish visible symptoms from their underlying organisational causes.
- Section 4: Recognise why restoring execution momentum requires collective leadership stewardship. · Establish a shared leadership rhythm for surfacing and resolving friction.
- Section 5: Diagnose the root cause of a stalled priority in their current portfolio. · Determine a targeted response with a named owner, action and completion date.

Read the Key learning outcomes from both pages and the deck slide 2 during the scan.

**Structure (part titles, same on both pages):** 1.1 What is a Strategic Clog? · 1.2 Three Observable Friction Signals · 1.3 The 7-Clog Diagnostic Map · 2.1 Clogs Are Design Signals · 2.2 Three Disciplines of Execution Engineering · 2.3 The 7 Strategic Unclogging Levers · 3.1 The 7 COMPASS High-Flammability Zones · 3.2 The 4-Step Unclogging Activation · 4.1 Normalising the Unclog: From Crisis to Habit · 4.2 The "See Something, Say Something" Principle · 4.3 Enterprise Unclogging Agenda (participant: "Your Contribution"; facilitator: "Collective Capture") · 5.1 The Clog Clinic: Exercise Structure · 5.2 Observer Evaluation Criteria · 5.3 Exercise Output: Participant Commitments · Unit Summary.

**Section titles:** 1 What is a Strategic Clog? · 2 Why Clogs Are Predictable Features of Execution · 3 Where Are the Highest-Flammability Clog Zones? · 4 Cross-Leadership Clog Ownership · 5 The Clog Clinic. The facilitator page also has "Unit 9 — Session Overview".

**Saved answers (participant page, `KEYS`):** `team_name`, `ref1` to `ref6`, `app_prep`, `app_clog`, `app_lever`, `app_followup`. The page has no Confirm and no `confirmed_items`: Section 5 is individual triad work today, with nothing feeding the Capstone.

**Deck slides:** 1 title · 2 Key learning outcomes · 3 The unit journey · 4 Section 1 · 5 1.1 · 6 1.2 · 7 1.3 · 8 Section 2 · 9 2.1 · 10 2.2 · 11 2.3 · 12 Section 3 · 13 3.1 · 14 3.2 · 15 Section 4 · 16 4.1 · 17 4.2 · 18 4.3 · 19 Section 5 · 20 "The Clog Clinic: three parts · 45 minutes" · 21 "Four questions, in sequence, without skipping" · 22 "Part 3 · The Collective Intelligence Challenge" · 23 5.2 Observer evaluation criteria · 24 5.3 Participant commitments · 25 Unit Summary · Closing. No slide text under 24pt. No Section Reflections slides.

## 3. What the scan should find (seen on 13 October; confirm in the full scan)

- **Times:** slide 20 title says "45 minutes"; the deck notes hold 20 "minutes", 6 "Time:" and 6 "Timing"; the facilitator page holds 10 "minutes" and 2 "Timing" (the Clog Clinic); the participant page holds one. Her rule: no times anywhere.
- **Group work as Capstone work:** Section 5 (the Clog Clinic, triads, "Participant Commitments") is individual work with an individual commitment. By the standard of Units 5 to 8, Section 5 is the group's Capstone work on the team's own strategy, with one record, Confirm and Print, feeding Capstone boxes 9A to 9E through a new `PULL.u9` row, left out of the Learning Portfolio, with no closing commitment. Expect Carol to decide how the Clog Clinic becomes that. 4.3 "Enterprise Unclogging Agenda" also reads as collective capture.
- **Facilitator review of group work:** the facilitator page has 6 "Watch for" and the deck notes 7. These must go from group work (they may stay only on class practice with nothing entered on the portal).
- **Wording:** "KR/KPI" appears (participant 2, facilitator 1, deck notes 2); write "Key Result or KPI". "lens" appears once in the participant page's visible text. "commitment" appears in the facilitator page and the deck notes.
- **Reflections:** check each reflection has `class="ref-prompt"`, an `id` in `KEYS` and a label in `dashboard_F.html`; add the "Section N Reflections" slides with pictures taken from the participant page (Unit 8 model: `shoot_reflections_u08.py`, `refill()` in `carol_deck_u08_r5.py`).
- **The wording "Alignment Brigade"** was replaced in Units 3 to 7, 9 and 12 on 13 October (pages, decks, notes, reader folders; pushed and uploaded). Unit 9 now says "The leadership team, acting as the collective intelligence for execution discipline, …" and the exercise is "The Collective Intelligence Challenge" (part 3 of the Clog Clinic). Never bring "Alignment Brigade" back. Script: `Unit decks\_build\brigade_wording\`.

## 4. State of the portal at handover (13 October, 17:40)

- `main` on GitHub = `0a7236567da6f2cac7990aba86a55c35bb7ee857` ("Alignment Brigade replaced …"). Everything built for Unit 8 and the wording change is pushed and live; Storage uploads done for Units 6, 7, 8, 9 and 12.
- Unit 8 (`u3m2_lens7`) is finished: Capstone four boxes 8A to 8D (database set to 4), report labels and Learning Portfolio updated, deck 24 slides.
- Not committed yet: this file. Add `"Claude outputs/Handover - Unit 9.md"` to the next `git add` line.

## 5. What Unit 8 taught (13 October)

- **Read all of her message and all of the notes before building.** She sends several changes in one message; list each one and tick it off in the reply. She stopped work twice to say an instruction was missed ("Do not forget the brigade wording. Please read all the notes").
- **When she says "replace all areas", search every unit page, every deck (slides, tables and notes) and the reader folders**, then report every unit touched with the right unit numbers. Lens numbers are not unit numbers: `u2m1_lens2` is Unit 3, `u3m2_lens8` is Unit 9, `u4m2_lens11` is Unit 12 (unit = lens number + 1).
- **Class practice and individual Portfolio work use different cases with different root causes.** In Unit 8 the class role play is the complaint resolution case (lack of skill, with a private team member brief) and the 4.2 Portfolio case is on-time delivery (lack of accountability). The Portfolio question asks what the participant deduces from the conversation ("How was the GROW model used…"), never what they would do.
- **Storage upload steps:** she finds swapping single files inside the reader folders confusing. Tell her to replace the whole set: in the Module folder replace `unit-NN.pptx`; open the folder `unit-NN`, delete everything inside, upload every file from `Claude outputs\Deck upload\Module-N\unit-NN`, and give the number of files to expect.
- **Red text in PowerShell after `git push` is normal.** Check the push by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`, then fetch the live page (use `https://main--ibslportal.netlify.app/<file>?v=1` when the first fetch returns an old copy).
- Never run git in her folder, not even `git --version`.
