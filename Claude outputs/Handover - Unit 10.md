# Handover — Module 4 · Grounding, starting with Unit 10 (ESRG Alignment)

Written 27 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party": it makes the technical and database decisions and carries out technical steps itself (Storage uploads through Claude in Chrome included). Her instruction is final: never answer an instruction with options or a question on the same point. When she asks for a change, apply it everywhere (both pages, deck slides and notes, reflection pictures, Capstone, report labels, upload copy, reader folder) without being told. Apply every point of an amendment message in one pass.

**WAIT FOR HER INSTRUCTIONS.** Units 10–12 are reviewed unit by unit under her guidance: do not propose or build content until she gives direction.

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 1. Carol's direction for Module 4 · Grounding (27 Oct 2026)

The two sides of performance added through Units 6–9 (people performance and organisational performance) now shape Module 4:

- **Unit 10 · Grounding for organisational performance.** ESRG Alignment: whether the organisational conditions (Environment, Systems, Resources, Governance) support the execution of the individuals' tasks.
- **Unit 11 · Grounding for people performance.** The page is currently titled "Culture Reinforcement & Organisational Health" and is framed on organisational health; under the new direction it becomes the grounding for people performance. Carol directs how.
- **Unit 12 · Sustaining performance in both areas** (people and organisational).

Unit 10 is first. Carol gives the direction for each unit before anything is proposed.

## 2. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 9 continuation.md` sections 3 (rules), 6 and 7 (Capstone read-only, shared group record, simulation, deck and Storage method).
3. `Claude outputs\Handover - Unit 9 two performance views.md` sections 3 and 4 (people performance / organisational performance rules: "organisational conditions" wording, ESRG, "leaders" for those responsible for the conditions, "individuals" for those delivering KPIs; Units 9–12 teach the environment).
4. `Claude outputs\Handover - Unit 1 Charter and Unit 2 capstone.md` sections 1, 5 and 6 (shared group record, SQL and Storage rules).
5. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules and the unit standard).
6. Patterns to copy for a group Section 5 that feeds the Capstone: Unit 6 Activity 3 / Unit 8 part 5.2 (WARD, `Unit decks\_build\ward_20oct\`), Unit 9 (`Unit decks\_build\rebuild_u09s2\`), Unit 4 5.3 (`Unit decks\_build\capstone_readonly_19oct\patch_u4.py`). Tests run in the cloud workspace with Playwright: `cap_chain2.py`, `ward_e2e.py`, `fake-supabase-team2.js` (copies in `Unit decks\_build\capstone_readonly_19oct\` and `ward_20oct\`). The device shell has no browser.

## 3. State on 27 October (checked)

- Git: `main` = `origin/main` = `8ca107e4…` (WARD in Units 6 and 8, 20 Oct). Nothing pushed since.
- Capstone page is read-only for participants; each section fills from the agreed unit Section 5 through `capstone_sync_section`. Units 1–9 feed it. DB box counts: u1 8, u2 6, u3 6, u4 6, u5 3, u6 3, u7 5, u8 5, u9 5, u10 6, u11 5, u12 5.
- Test account (Test Participant, team Alpha, one member, company "Alpha Client Services"): Capstone u1–u9 all Agreed, every box filled (6C and 8E included). Its enterprise Key Result: reduce average response time from 12 hours to 4 hours by 30 June 2027.
- WARD (20 Oct): Unit 6 Activity 3 "WARD · Your Key Result's Vital Check-up" (Waypoints, Alert, Recovery, Decider; box 6C `cm_ward`); Unit 8 part 5.2 "Testing Your WARD" (box 8E `rd_ward`). Recovery covers the individuals and the organisational conditions, so Units 10–12 can refer back to it.

## 4. Module 4 pages and decks now (none rebuilt yet; none on the shared group record; none feed the Capstone)

**Unit 10 · ESRG Alignment** — `unit4_m1_lens9_p.html` (md5 5515ad5c…) / `_f.html` (7918b418…), lens id `u4m1_lens9`. Deck `Unit decks\Unit 10 - ESRG Alignment.pptx`, 25 slides (fbacf885…), same as `Deck upload\Module-4\unit-10.pptx`.
- Section 1 Awareness: 1.1 ESRG Alignment: The Grounding Question · 1.2 The Four ESRG Domains · 1.3 ESRG Synthesis.
- Section 2 Intelligence: 2.1 The ESRG Ignition Point · 2.2 Worked Example 1: The IBSL Cultural Operating Code · 2.3 Worked Example 2: The ESRG Execution Scanner.
- Section 3 Extrapolating: 3.1–3.4 E/S/R/G Friction · 3.5 Seeing Friction as Organisational Intelligence.
- Section 4 Integration: 4.1 The Execution Muscle Scan · 4.2 The Four Reflections · 4.3 The COMPASS-ESRG Connection · 4.4 Collective Signal Intelligence & The Outcome · 4.5 Enterprise ESRG Alignment Agenda: Your Contribution.
- Section 5 Application "Build the Cultural Operating Code": 5.1 The Three Value Sets · 5.2 The Exercise (55 minutes, minute timings per part) · 5.3 Exercise Output; individual Draft COC boxes and "My Commitment". Individual work on generic value sets; it does not use the group's Capstone organisation and feeds nothing.
- Capstone u10 boxes (BLUEPRINT in `capstone_P.html`): 10A Environment · 10B Systems · 10C Resources · 10D Governance (each: whether [Case]'s conditions support its priorities, and the intervention required) · 10E Cultural Operating Code · 10F Enterprise ESRG agenda. No `PULL.u10` yet.

**Unit 11 · Culture Reinforcement & Organisational Health** — `unit4_m1_lens10_p.html` / `_f.html`, lens id `u4m1_lens10`. Deck `Unit decks\Unit 11 - Culture Reinforcement & Organisational Health.pptx`.
- Sections: 1.1 What is Organisational Health? · 1.2 The Five Observable Traits · 1.3 The Organisational Health Pyramid · 1.4 Connecting the Two Models · 2.1–2.3 Signals, Conditions and Price of Poor Health · 3.1 The Organisational Health Thermometer · 3.2 Reading Your Temperature · 3.3 ACE-IT Guardrail Priorities by Temperature · Section 4 · Section 5: Choose Your Scenario, The ACE-IT Coaching Protocol, The Exercise (40 minutes).
- Capstone u11 boxes: 11A Health reading · 11B Health foundations · 11C Cost of poor health · 11D Health stewardship · 11E Guardrails and coaching. These follow the current organisational-health framing; they change with Carol's people-performance direction.

**Unit 12 · Sustaining Performance** — `unit4_m2_lens11_p.html` / `_f.html`, lens id `u4m2_lens11`. Deck `Unit decks\Unit 12 - Sustaining Performance.pptx`.
- Sections: 1.1 The Navigation Premise · 1.2 The Three Mechanisms of Performance Gravity · 1.3 KISS: The Four Navigation Disciplines · 2.1 The Five Forces · 2.2 The Causal Map · 3.1 The Collective Intelligence for Execution Discipline · 3.2 ABCV as the Navigation Diagnostic · 3.3 The Navigation Chain · Section 4 · Section 5: Navigation Chain Scenarios, Navigation Commitment.
- Capstone u12 boxes: 12A Performance gravity · 12B Force detection · 12C Navigation diagnostic · 12D KISS navigation response · 12E Navigation commitment. Under the new direction Unit 12 sustains both people and organisational performance; the boxes change with her direction.

## 5. How each Module 4 unit is rebuilt, once Carol gives the content (same chain as Units 4–9)

1. Her direction → proposal in chat (short) → her corrections → "lock". Review files (PREVIEW pages) when she asks to see the format.
2. Both pages: participant "you / your group", facilitator "participants / the group"; no times; no review wording on group work; British spelling; no contrast constructions; never "lens" in visible text; two section learning outcomes each, impact-led.
3. Section 5 as group Capstone work on the shared group record (group bar after the worked example; scribe types; every member selects Agree); the work uses the group's own Capstone organisation and brings in earlier unit work where it applies (Unit 3 OKRs, Unit 6 Contribution Map and WARD, Unit 9 clogs).
4. Save keys and Capstone names; `PULL.uNN` and BLUEPRINT boxes in `capstone_P.html`; SQL for `capstone_section_box_count` if the box count changes (give Carol SQL in a chat code block; the loop must keep every other unit's count); `CAPSTONE_KEYS` in `build_collection.js` then `node build_collection.js`; `dashboard_F.html` labels; `node check_standards.js`.
5. Tests in the cloud workspace (stage the files; site copy, fake Supabase, cap_chain extended to the unit).
6. Deck: backup first; her deck is the base; Section slides and notes in her approved notes format (numbered steps, teach first then ask); 24pt minimum; render with `reader_assets.py` (TMPDIR set) and look at every new slide; Deck upload copy + reader folder (old folder to `Claude outputs\_to_delete`).
7. Carol's PowerShell push (full grade-5 walk-through, one block starting `cd C:\Users\Carol\ibsl-platform`, every file in `git add`, commit message ending with the new session's attribution lines); check refs and the live pages; Storage (she deletes `Module-4/unit-NN.pptx` and folder `unit-NN`; Claude uploads through Claude in Chrome; SQL duplicate check).
8. Simulate the unit for the test account on the live portal so its Capstone section is Agreed with realistic content (Alpha Client Services).

## 6. Technical rules

- Never run git in her folder (check pushes by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`). Never read the dashboard token from localStorage. Never sign in for her.
- The device shell cannot delete: move files to `Claude outputs\_to_delete`.
- Pages use CRLF: patch scripts normalise to \n and restore CRLF on write.
- Supabase SQL editor tabs left with unsaved text block Chrome tab closing ("Leave site?"); navigate with force or ask Carol to close them.

## 7. Not committed yet

Add `"Claude outputs/Handover - Unit 10.md"` to the next `git add` line.

## 8. Unit 10 rebuilt (27 Oct 2026, evening; Carol 19:32 "write the live files")
- Carol's content for the Facilitator Guide and Sections 1–5 (five Word files) is applied; every decision is in `Claude outputs\Review files\Unit 10\Unit 10 - decisions and locks.md`. Build: `Unit decks\_build\rebuild_u10\` (`build_u10.py` rebuilds both pages from the backups in `Claude outputs\Backups\Unit 10 file backups\… before Module 4 rework (27 Oct)`; content in `u10_content.py`, `u10_s1b.py`, `u10_s2.py`–`u10_s5.py`, `u10_s4.js`, `u10_s5.js`; links `patch_links_u10.py`; PREVIEW `make_previews_u10.py` + `mock-s2r-u10.js`; tests `test_u10_s5_logic.js` (device node), `test\e2e_u10_preview.py` (cloud Playwright, 41 checks), `test\sql_test_u10.mjs` (pglite, 11 checks)).
- ESRG is FIT / SIP / AIR / PAR (Unit 10 master). Agreed follow-up: align Unit 6 part 1.2.2 (brief, new format), relabel Units 8 and 9 organisational examples (people items to the people cards), Units 8 and 9 part 1.1 ESRG sentence. Unit 7 unchanged.
- Section 5 is group Capstone work on the shared group record; it reads every member's part 4.5 annual baseline through the new function `team_esrg_scans` (`Claude outputs\unit10_esrg_clinic.sql`, also sets Capstone u10 to 4 boxes 10A–10D). Unit Summary removed from both pages (Carol 18:44).
- Live files written 27 Oct: `unit4_m1_lens9_p.html` 6f056e7a…, `unit4_m1_lens9_f.html` b81441948…, `capstone_P.html` b2ff9c93…, `dashboard_F.html` 4abf4dce…, `build_collection.js` 8ba37827…, `collection.html` 272bb3d8…. Head before the push: 55e70ae1 (two other commits landed today before this work went live).
- check_standards: Unit 10 shows Rule 27 (no Unit Summary, by Carol's decision) and Rule 12 "Capstone S2R Blueprint" (same naming as the other units).
- Still to do: deck (Carol: "we will work on the decks later"), Storage, live simulation of the test account (Capstone u10 Agreed), Units 6/8/9 ESRG alignment, Units 11 and 12.

## 9. ESRG alignment of Units 6, 7, 8 and 9 (27 Oct 2026, 19:54 "build the live files")
- Carol asked why Unit 7 was left out: Unit 7 part 1.2 (Clarity and Capability in organisational performance) and its Section 5 placeholders still carried the old domain meanings. Now aligned with Units 6, 8 and 9. Script `Unit decks\_build\esrg_align_27oct\align_esrg.py` (runs on the pre-change pages in `Claude outputs\Backups\ESRG alignment 27 Oct`); change list and PREVIEW pages in `Claude outputs\Review files\ESRG alignment Units 6 to 9`.
- Live md5: Unit 6 p 5ede4836…, f 8606bf64…; Unit 7 p eb12f356…, f 1dc1ca44…; Unit 8 p a0dc043f…, f 62f89d69…; Unit 9 p d869b363…, f 9477295d…; collection.html a409be63….
- ESRG elsewhere: Unit 11 (u4m1_lens10) and Unit 12 (u4m2_lens11) mention ESRG by name only (Unit 12 "ESRG Scanner" card: led by COO, CTO/CIO, CHRO, CFO) — align when Units 11 and 12 are rebuilt. Decks of Units 6–10 carry the old ESRG wording in slides and notes: align at the end with all decks.
