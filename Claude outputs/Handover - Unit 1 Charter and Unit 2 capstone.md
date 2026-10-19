# Handover — Unit 1 Problem Charter (done) and Unit 2 capstone rework (next)

Written 19 October 2026, 18:25, for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms. She calls Claude "partner". Claude is the "tech party": it makes the technical decisions and carries out technical steps itself (Storage uploads through Claude in Chrome included). Her instruction is final: never answer an instruction with options or a question on the same point. When she asks for a change, apply it everywhere (both pages, deck, notes, slide pictures, capstone, report labels) without being told.

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 0. Read first

1. This file.
2. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules and the unit standard; they apply word for word).
3. `Claude outputs\Handover - Units 2 to 9 consistency review.md` (state of Units 2–9 on 19 October; another chat worked on it the same day).
4. `Unit decks\_build\problem_charter_19oct\README.md` and the scripts beside it.

## 1. Working rules learnt today

- **Database:** Claude may run read-only checks in the Supabase SQL editor (Claude in Chrome: set the Monaco editor text with `window.monaco.editor.getModels()[0].setValue(...)`, click Run, read the grid with `find`/`read_page`). Changing the live database from Claude is blocked by the safety check: give Carol the SQL **in a chat code block** (she clicks the copy button, pastes into the SQL Editor, Run). Never give her a file path to paste: she pasted the file name once. Test SQL first in pglite (`npm i @electric-sql/pglite` in the cloud workspace; stub tables as in `/home/claude/pgt/t.mjs` style).
- **Do not** read the dashboard auth token from localStorage or call the Supabase management API with it (blocked as credential exploration).
- **Storage upload:** Carol deletes the old `unit-NN.pptx` and `unit-NN` folder; Claude stages the files from her folder (`device_stage_files`), then in Chrome opens Storage → facilitator_decks → Module-N, `file_upload` the pptx to the hidden file input (found with `find` "file input type=file"), Create folder `unit-NN` (type name, Enter), then `file_upload` all pictures and manifest.json (max 10 MB per call). Only staged paths under `/mnt/user-data/uploads/...` are accepted by `file_upload`.
- **device_commit_files caching:** committing a second time from the same staged path name can silently write the OLD content. Always use a new staged file name for a re-commit, and check the md5 on her computer after every commit.
- Push blocks: one PowerShell block starting `cd C:\Users\Carol\ibsl-platform`, every file named in `git add`, commit message with `-m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_019DYvUucpyQo7gJYkxUNRPp"`, then `git push`. Check a push by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`.
- Wording rules as in the Unit 8 handover (British spelling, no contrast constructions, no times, participant "you / your group", facilitator "participants / the group", no review wording on group work).

## 2. Done today (all live; last push `2117fcd0`, Storage re-uploaded 18:20)

- **Unit 1 part 6.1** renamed "Self Reflection Bias Assessment" (was The Five Commitments); the five parts are "Area 1–5", tabs A1–A5; 6.1 now opens with a narrative (what it does, the five areas with one-line meanings, what the results show) on both pages.
- **Unit 1 Section 6** now: 6.1, 6.2 The Problem Charter, Unit Summary. The Distortion Lab is removed from both pages and the deck; the Unit Closing Reflection — Portfolio Artefact is removed from the participant page (old `port_1..3` answers stay in the database).
- **Unit 1 part 6.2 · The Problem Charter** (group work, Capstone work), Carol's final design:
  - Step 1 · Company: simulated company name, simulated executive team (up to 10 rows: role CEO, CFO, COO, CHRO, CTO, CMO, CCO, CPO, CRO, CSO + member name; each role once), sector, approximate size, main activity.
  - Step 2 · Shared reality: (1) challenges experienced, at least four (room for six) in each of strategy design, strategy execution, sustaining performance; (2) how these challenges manifested: at least two scenarios each for observable behaviours, management practices, organisational conditions; (3) consequences for results, one box per area, each with its own "How have…" guiding question.
  - Step 3 · Central problem: (1) three drop-down lists per area, each listing that area's challenges from Step 2, choose three different ones; (2) the central organisational problem.
  - Charter record: checks, Confirm, Print.
  - Keys (lens `u1_foundations`): `__pc_work`, `pc_record`; on Confirm `pc_company`, `pc_team`, `pc_org`, `pc_challenges`, `pc_manifest`, `pc_consequences`, `pc_address`, `pc_problem` and eight "Problem Charter · …" names in `confirmed_items`.
- **Capstone** (`capstone_P.html`): new Section 1 · Problem Charter, boxes 1A Simulated company, 1B Simulated executive team, 1C Our organisation, 1D Challenges experienced, 1E How they manifested, 1F Consequences for results, 1G The challenges we will address, 1H Our central organisational problem (`PULL.u1`). Box 1A replaces the cohort case name as [Case] on the whole Blueprint. 12 sections. Assessment criteria add the Problem Charter line. The capstone opens when Unit 1 opens.
- **Database (run by Carol):** section key `u1` allowed; `capstone_section_lens('u1') = 'u1_foundations'`; `capstone_section_box_count('u1') = 8`; `get_capstone_blueprint` lists u1 first; `get_my_capstone` opens on Unit 1; `capstone_brief.case_name` nullable and `admin_set_capstone_brief` no longer needs a case. File: `Claude outputs\capstone_unit1_charter.sql`.
- **Admin Console** (`dashboard_A.html`): Case field removed from the cohort brief; "of 12 agreed".
- **Facilitator report** (`dashboard_F.html`): labels for the `pc_*` keys and a "The Problem Charter" family. **Learning Portfolio** (`build_collection.js`): `CAPSTONE_KEYS.u1_foundations = /^(pc_|confirmed_items$)/`; `collection.html` rebuilt.
- **Unit 1 deck** (`Unit decks\Unit 01 - Behavioural Strategy Fundamentals.pptx`, 35 slides, md5 34aff41c…, identical to `Claude outputs\Deck upload\Module-1\unit-01.pptx`): Distortion Lab slides removed; slide 33 subtitle "The Self Reflection Bias Assessment and the Problem Charter"; slide 34 "Section 6 · On the Portal" with pictures of 6.1 and 6.2 and notes for both. Reader folder `unit-01` (35 pictures + manifest) made with `reader_assets.py` on a copy with Aptos→Carlito and Georgia→Caladea. Old pictures s36–s38 moved to `Claude outputs\_to_delete\unit-01 old pictures 19 Oct`.
- Tests: `Unit decks\_build\problem_charter_19oct\e2e_pc.py` (35 of 35 pass, with `rebuild_u06\fake-supabase.js`). Backups: `Claude outputs\Backups\Problem Charter 19 Oct`, `…\Problem Charter refinement 19 Oct`, `…\Unit 1 Section 6 refinement 19 Oct`.

## 3. Next: Unit 2 capstone rework (Carol's decisions, 19 October)

- Each group defines **its own simulated company's** strategy (the company from its Problem Charter, box 1A). All capstone sections must be amended to match this (decision 1: "So we will have to amend all capstone to match").
- **Section 4 (Integration) becomes one full worked example**; **Section 5 (Application) is the capstone build** of the same, in order: Strategy Architecture → Strategy Intent Statement → Success in Practice (SiP). Unit 2 keeps its section order (Carol reverted a swap on 12 Oct).
- The S2R Strategy Architect HTML tool she showed (14 elements: Iterative; Thinking & Logic; Process; What; Why; How; When; Creates Value; Delivers Value; Sustains Value; Stakeholders; Navigating; The Forces; Operating Environment; four guiding questions each) is **for consulting clients: look at how it is built, do not replicate it**. The portal must never automate the Strategy Intent Statement or the SiP; participants deduce and type them (her standing rule).
- The current Unit 2 page (`unit2_m1_lens1_p.html` / `_f.html`) already has the 14-element architecture in 4.1, the Intent in 4.2, SiP in 4.3 (`arch_*`, `intent_statement`, `sip_d1_st`…`sip_d4_st`, pulled into capstone 2A–2F), and Section 5 holds 5.1 Role Contribution to SiP and 5.2 SiP Statement Collective Application.
- **Group work records (Carol, 19 Oct, decided in the Charter chat and confirmed at 18:29–18:37):** one shared team record. The group picks its scribe for each assignment (drop-down of members, can change at any time, scribes alternate); only that assignment's scribe types; every member sees the entries on their own unit page; each member selects Agree, and the work goes into the Capstone only when every member has agreed (an edit after agreement clears the agreements). This replaces the old rule that every member retypes the scribe's entries. It applies to ALL Capstone group work: Unit 1 Problem Charter, Unit 2 Section 5 and the Section 5 group work of Units 3 to 9. Only test participants exist, so no old entries are carried over.
- Unit 2 Section 5: 5.1 Role Contribution to SiP and 5.2 SiP Statement Collective Application come off both pages and the deck (Carol, 18:35). Section 5 is Strategy Architecture, then Strategy Intent Statement, then SiP, for the group's Problem Charter company. "Generate what this is saying" is not carried into the portal (her Architect tool is reference only).
- Section 4 worked example case: the client-service organisation of the Unit 3 worked example, so one case runs Unit 2 to Unit 4.
- Later: show the group's central problem (1H) and chosen challenges (1G) read-only at the top of each unit's capstone section, Units 2 to 12 (proposed 13 Oct, not yet ordered).

## 4. Not committed yet

Add `"Claude outputs/Handover - Unit 1 Charter and Unit 2 capstone.md"` to the next `git add` line.


## 5. Built on 19 October, evening (not pushed yet)

- **Database:** `Claude outputs\team_work_shared_record.sql` (tables `team_work`, `team_work_agreement`; functions `team_work_status`, `team_work_set_scribe`, `team_work_write`, `team_work_agree`). Read-only check run by Claude in the SQL editor first. Tested in pglite 20 of 20, control fails. Carol runs it before the push: without it the group boxes stay closed.
- **`s2r-team.js`** (new, repo root): the group record bar (scribe drop-down, members, Agree), closes the group boxes for non-scribes, sends the scribe's entries to every member's page (`team_work_write` writes the same keys into every member's `lens_responses`), Agree per member; when all have agreed the server adds the names to every member's `confirmed_items`, so the Capstone `PULL`, Unit 3 (SiP), Unit 6/7/9 drop-downs and the report work unchanged.
- **Units 1, 3–9 pages** moved to it (`Unit decks\_build\team_record_19oct\team_patch.py`), wording "scribe for this work … select Agree" on both pages; tests `e2e_team_units.py` 73 of 73 (control fails). Decks of Units 1, 3–9: notes only (`deck_team_notes.py`), copies in Deck upload identical, `manifest.json` notes updated (pictures unchanged). Storage: re-upload those 8 pptx + manifest.json.
- **Unit 2** (`build_u02cap.py`, `we_content.py`, `u2b_tool.js`): Section 4 worked example (Kestrel Point Services), Section 5 · 5.1 Your Company's Strategy on the shared record; 5.1/5.2 old removed; test `e2e_u2cap.py` 32 of 32. NOT yet in the repo: review files in `Review files\Unit 2 capstone` wait for Carol. After her word: write the two pages, rebuild Unit 2 deck Sections 4–5 (slides 25–35, notes), reader folder, then SQL → push → Storage.
- Backups: `Backups\Shared group record 19 Oct\pages` and `\decks`.
- Add to the next `git add`: `s2r-team.js`, the 16 unit pages of Units 1, 3–9, `Claude outputs/team_work_shared_record.sql`, the two Unit 2 pages, `Unit decks/_build/team_record_19oct/*`, this file.

## 6. Unit 2 live files (19 Oct, 19:48 "Ok build live documents")

- Carol's amendments first: the 1.2 reflection (ref2) removed; the 1.2 WHAT/WHY/HOW/WHEN tabs fixed (container id `w1hPTabs`).
- Unit 2 pages written to the repo; Unit 2 deck rebuilt on her deck (`deck_u02cap.py`, `notes_new.py`): slide 10 without the 1.2 picture; slides 25–32 teach the Kestrel Point worked example; 33 "Build Your Company's Strategy"; 34 "5.1 · Your Company's Strategy" with a picture of the group record bar; 35 reflection 5.1; notes of 1, 8, 36 updated. Deck upload copy identical; reader folder unit-02 remade (36 pictures + manifest).
- `collection.html` rebuilt.
- Go-live order: Carol runs `team_work_shared_record.sql` → push → Storage: delete and re-upload unit-01..09 pptx and manifest.json (unit-02: the whole folder).
