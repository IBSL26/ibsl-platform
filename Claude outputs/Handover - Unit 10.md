# Handover — Unit 10 · ESRG Alignment (Section 5 rebuild onto the Capstone)

Written 20 October 2026, 11:10, for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party": it makes the technical and database decisions and carries out technical steps itself (Storage uploads through Claude in Chrome included). Her instruction is final: never answer an instruction with options or a question on the same point. When she asks for a change, apply it everywhere (both pages, deck slides and notes, reflection pictures, Capstone, report labels, upload copy, reader folder) without being told. Apply every point of an amendment message in one pass. WAIT FOR HER INSTRUCTIONS before proposing or building Unit 10 content.

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 9 continuation.md` sections 3 (rules), 6 and 7 (Capstone read-only, group record, simulation, deck and Storage method).
3. `Claude outputs\Handover - Unit 9 two performance views.md` sections 3 and 4 (people performance / organisational performance rules; Units 9–12 teach the environment).
4. `Claude outputs\Handover - Unit 1 Charter and Unit 2 capstone.md` sections 1, 5 and 6 (shared group record, SQL and Storage rules).
5. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules and the unit standard).
6. Pattern to copy for a group Section 5 that feeds the Capstone: Unit 9 `unit3_m2_lens8_p.html` / `_f.html` (built by `Unit decks\_build\rebuild_u09s2\`), Unit 4 5.3 (`Unit decks\_build\capstone_readonly_19oct\patch_u4.py`), Unit 5 (`patch_u5.py`). Tests: `capstone_readonly_19oct\cap_chain2.py`, `e2e_team_units2.py`, `fake-supabase-team2.js` (cloud workspace Playwright; the device shell has no browser).

## 1. State on 20 October, 11:10 (checked)

- Git: `main` = `origin/main` = `890692d4` (Unit 4 and Unit 5 deck updates, reader folders, handovers). Everything below is live.
- Capstone page is read-only for participants; each section fills from the agreed unit Section 5 through `capstone_sync_section` (live). Units 1–9 feed it. Test account (Test Participant, team Alpha, company "Alpha Client Services"): Capstone u1–u9 all Agreed, every box filled.
- Unit 10 pages: participant `unit4_m1_lens9_p.html` (md5 5515ad5c…), facilitator `unit4_m1_lens9_f.html` (7918b418…), lens id `u4m1_lens9`. Not yet on the shared group record (no `#twBar`, no `s2r-team.js`), no `confirmed_items`, no Capstone outputs.
- Unit 10 deck: `Unit decks\Unit 10 - ESRG Alignment.pptx`, 25 slides, md5 fbacf885…, identical to `Claude outputs\Deck upload\Module-4\unit-10.pptx`. Storage: facilitator_decks / Module-4 / unit-10.pptx and folder unit-10.

## 2. Unit 10 page structure now

- Section 1 · Awareness: 1.1 ESRG Alignment: The Grounding Question · 1.2 The Four ESRG Domains · 1.3 ESRG Synthesis.
- Section 2 · Intelligence: 2.1 The ESRG Ignition Point · 2.2 Worked Example 1: The IBSL Cultural Operating Code · 2.3 Worked Example 2: The ESRG Execution Scanner.
- Section 3 · Extrapolating: 3.1–3.4 E/S/R/G Friction · 3.5 Seeing Friction as Organisational Intelligence.
- Section 4 · Integration: 4.1 The Execution Muscle Scan · 4.2 The Four Reflections · 4.3 The COMPASS-ESRG Connection · 4.4 Collective Signal Intelligence & The Outcome · 4.5 Enterprise ESRG Alignment Agenda: Your Contribution.
- Section 5 · Application ("Build the Cultural Operating Code"): 5.1 The Three Value Sets: Choose One (A Governance-Led, B Performance-Led, C Purpose-Led) · 5.2 The Exercise (55 minutes; Part 1 · 5 min Choose, Part 2 · 35 min Build, Part 3 · 15 min Challenge; three tests: New Employee, Pressure, Mirror) · 5.3 Exercise Output · individual "Draft COC — Value 1–3" boxes (Value, Behaviour, Acronym, Statement) and "My Commitment". Individual work, minute timings, generic value sets: it does not use the group's Capstone organisation and feeds nothing.

## 3. What the Capstone expects from Unit 10 (`capstone_P.html` BLUEPRINT u10, DB box count 6)

- 10A Environment — whether [Case]'s physical and behavioural environment supports its priorities, and the intervention required.
- 10B Systems — processes, data and approvals.
- 10C Resources — people, funding and capacity.
- 10D Governance — decision rights, oversight and accountability.
- 10E Cultural Operating Code — [Case]'s values translated into named, observable behavioural norms.
- 10F Enterprise ESRG agenda — the enterprise actions that align [Case]'s operating conditions with its strategic priorities.
- No `PULL.u10` row yet; `capstone_section_lens('u10')` and box count already exist in the database.

## 4. The rebuild, once Carol gives the content (same chain as Units 4, 5 and 9)

1. Section 5 as group Capstone work on the shared group record: group bar after the worked example; scribe types; every member selects Agree; no minute timings; "you / your group"; the work uses the group's own Capstone organisation (bring-in from earlier units where it applies, e.g. Unit 3 OKRs, Unit 6 Contribution Map organisational conditions, Unit 9 clogs).
2. Save keys for 10A–10F, Capstone names in `confirmed_items`; `PULL.u10` in `capstone_P.html`; `CAPSTONE_KEYS` in `build_collection.js` (rebuild `collection.html`); `dashboard_F.html` labels; facilitator page to match.
3. Tests: static checks, `cap_chain2.py` extended to u10, e2e on the group record.
4. Deck: Section 5 slides and notes (backup first, 24pt rule), Deck upload copy, reader folder (`reader_assets.py`, TMPDIR set), Storage (Carol deletes Module-4/unit-10.pptx and folder unit-10; Claude uploads; SQL duplicate check).
5. Carol's PowerShell push; check refs and live pages; then simulate Unit 10 for the test account so Capstone u10 is Agreed with realistic content (Alpha Client Services).
6. Units 11 and 12 follow the same chain (boxes 11A–11E, 12A–12E).

## 5. WARD added to Units 6 and 8 (20 Oct, Carol's instruction)

- Unit 6 Section 5 Activity 3 "WARD · Your Key Result's Vital Check-up" (Waypoints, Alert, Recovery, Decider) for the enterprise Key Result chosen in Activity 1; saves cm_ward; Capstone box 6C. Unit 8 Section 5 part 5.2 "Testing Your WARD" (brings in cm_ward from the member's Unit 6 page; red flag, what explains the gap for individuals and organisational conditions, recovery); saves rd_ward; Capstone box 8E.
- Wording source: `Unit decks\_build\ward_20oct\ward_text.py` (Carol's approved opening: "Every Key Result your group set in Unit 3 has a baseline, a target and a deadline. Performance management must set out in advance when a Key Result will be checked and which result raises a red flag. Corrective action then starts early, while the gap is still small enough to close. WARD is the vital check-up that sets these points for your Key Result."). Alert reads "how far off a waypoint" (works for Key Results where lower is better).
- Patches, tests (`ward_e2e.py`, `cap_chain2.py` 46/46 in the cloud workspace), deck scripts (`deck_ward.py`, `icons.py`) in `Unit decks\_build\ward_20oct\`. SQL `Claude outputs\capstone_ward_boxes.sql` (u6 = 3 boxes, u8 = 5). Decks: Unit 6 34 slides (new 33), Unit 8 25 slides (new 25).

## 6. Not committed yet

Add `"Claude outputs/Handover - Unit 10.md"` to the next `git add` line.
