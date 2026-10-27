# Handover — Module 4 · Unit 11 (next after Unit 10)

Written 27 October 2026, 20:05, for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party": it makes the technical and database decisions and carries out technical steps itself (Storage uploads and live test runs through Claude in Chrome included). Her instruction is final: never answer an instruction with options or a question on the same point. When she asks for a change, apply it everywhere (both pages, Capstone, report labels, earlier units that use the same concept) without being told — on 27 Oct she had to ask "why have you not aligned everywhere we have ESRG?": search every page for the concept before saying a unit needs no change. Apply every point of an amendment message in one pass.

**WAIT FOR HER INSTRUCTIONS.** Unit 11 is reviewed section by section under her guidance: she sends each section as a Word file; Claude applies it to both pages as PREVIEW, she corrects, then "build live files". **Decks are done right at the end for all units** (Carol, 27 Oct 19:45) — do not touch decks until she says.

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 1. Read first, in this order
1. This file.
2. `Claude outputs\Handover - Unit 10.md` (all of it, sections 8–10 above all: how Unit 10 was rebuilt, ESRG alignment, test account run).
3. `Claude outputs\Review files\Unit 10\Unit 10 - decisions and locks.md`: every decision Carol made on 27 Oct, with the standing-rule rewordings she accepted.
4. `Unit decks\_build\rebuild_u10\` — the method to copy for Unit 11 (`build_u10.py` rebuilds both pages from backups section by section; content modules per section; `make_previews_u10.py` + `mock-s2r-u10.js` for PREVIEW pages with a sample group; tests `test\e2e_u10_preview.py` (Playwright in the cloud workspace), `test_u10_s5_logic.js`, `test\sql_test_u10.mjs` (pglite)).
5. `Claude outputs\Handover - Unit 9 continuation.md` section 3 and `Claude outputs\Handover - Unit 1 Charter and Unit 2 capstone.md` sections 1, 5, 6 (shared group record, SQL, Storage).

## 2. State on 27 October, 20:05 (checked)
- Git `main` = `origin/main` = `64eae8b4…` (ESRG alignment of Units 6–9). Before it: `6d099201…` (Unit 10 rebuilt). Not committed yet: `Claude outputs/Handover - Unit 10.md` (sections 9–10 added after the push) and this file — add both to the next `git add`.
- Unit 10 is live and complete (pages, Capstone 10A–10D, report labels, Learning Portfolio, DB function `team_esrg_scans`, box count u10 = 4). Test account: Capstone Unit 10 Agreed (20:03). Unit 10 deck not yet done (decks at the end).
- ESRG (FIT · SIP · AIR · PAR) is aligned on the pages of Units 6, 7, 8, 9, 10. Units 11 and 12 mention ESRG by name only; Unit 12's "ESRG Scanner" card (led by COO, CTO/CIO, CHRO, CFO) must match Unit 10 when Unit 12 is rebuilt. Unit 11 facilitator page says "Where Unit 10 examined the structural conditions (ESRG), Unit 11 examines the behavioural and cultural conditions": keep consistent with her direction.
- Chrome: signed in to the portal as Test Participant at the end of the session (Carol was told to sign back in with her own account).

## 3. Carol's direction for Module 4 (from 27 Oct)
- Unit 10 · ESRG Alignment = organisational operating environment (FIT, SIP, AIR, PAR); built.
- **Unit 11** · her Module 4 text (Unit 10 Facilitator Guide, locked): "The Grounding learning journey progresses from Unit 10 — ESRG Alignment (organisational operating environment), to Unit 11 — Organisational Health (culture), and then to the subsequent unit on leveraging both to sustain high performance." Her Module learning outcome 2: "Shape organisational culture by establishing and embedding the conditions and practices that strengthen organisational health." The earlier note (Unit 10 handover §1) said Unit 11 becomes the grounding for people performance; Carol directs how. People items moved out of ESRG on 27 Oct (workforce capacity, capability, psychological safety, values and consequences, employee sustainability) belong to the people side — Unit 11 is their natural home.
- Unit 12 · sustaining performance in both areas (people and organisational).

## 4. Unit 11 now (live, not rebuilt)
- Pages `unit4_m1_lens10_p.html` (md5 39e16b9f…) / `unit4_m1_lens10_f.html` (0c15a192…), lens id `u4m1_lens10`, title "Culture Reinforcement & Organisational Health". Deck `Unit decks\Unit 11 - Culture Reinforcement & Organisational Health.pptx` (50934e49…).
- Sections: 1.1 What is Organisational Health? · 1.2 The Five Observable Traits · 1.3 The Organisational Health Pyramid · 1.4 Connecting the Two Models · 2.1–2.3 Signals, Conditions and Price of Poor Health · 3.1 The Organisational Health Thermometer · 3.2 Reading Your Temperature · 3.3 ACE-IT Guardrail Priorities by Temperature · Section 4 · Section 5: Choose Your Scenario, The ACE-IT Coaching Protocol, The Exercise.
- Section 5 is individual work on a scenario; not on the shared group record; feeds nothing. Capstone u11 boxes (5): 11A Health reading · 11B Health foundations · 11C Cost of poor health · 11D Health stewardship · 11E Guardrails and coaching. No `PULL.u11`. These change with Carol's content.
- Report labels `dashboard_F.html` `u4m1_lens10` (ref1–ref6, app_thermo, app_scenario, app_prep_*, app_commit); numbered map 1–6; Learning Portfolio `CAPSTONE_KEYS` has no u4m1_lens10.

## 5. How the Unit 10 rebuild ran (repeat for Unit 11)
1. Backups first: `Claude outputs\Backups\Unit 11 file backups\… before Module 4 rework`. Build script rebuilds from the backups each time (idempotent), one content module per section.
2. Each Word file she sends: read it, apply to both pages (participant "you / your group"; facilitator "participants / the group"; facilitator-only boxes stay on the facilitator page; facilitator prompts become "Reflect:" lines on the participant page). Save her text as markdown in `Claude outputs\Review files\Unit 11\` and log each decision in `Unit 11 - decisions and locks.md`.
3. Standing rules she accepted on 27 Oct (apply silently, report in one line each): never "lens" (use "perspective"); no contrast constructions ("rather than", "not X", "instead of") — reword only that sentence; no "automatically"; "Integrating" not used in sub-lines (STANDARDS rule 2); the facilitator does not review Capstone work ("Facilitator Review Focus" became "Completion focus" / "What your completed work shows"); "Key learning outcomes" label; British spelling.
4. Her preferences shown on 27 Oct: teaching sections are read-only on the participant page ("for teaching not completing"); worked examples sit before the form; long multi-part blocks collapse (`details.u10-det`, first open); individual assessment = annual baseline only; group work pulls members' individual entries and the group's Problem Charter (roles `pc_team`, stated problems `pc_problem` + chosen challenges from `__pc_work`).
5. Section 5 = group Capstone work on the shared group record (`s2r-team.js`; scribe types, each member selects Agree; texts saved only when complete; `PULL.u11`; BLUEPRINT boxes; box count SQL keeping all other units — model `Claude outputs\unit10_esrg_clinic.sql`, tested in pglite first; give Carol SQL in a chat code block with grade-5 steps; a read-only check by Claude is fine).
6. Links: `patch_links` (capstone_P BLUEPRINT + PULL, dashboard_F labels/families/numbered map, build_collection CAPSTONE_KEYS) → `node build_collection.js` → `node check_standards.js`.
7. Tests: logic in device node; Playwright in the cloud workspace on PREVIEW pages staged with `device_stage_files` (cloud `Bash` has playwright; start `python3 -m http.server` in the same command as the test). Check page errors, phone width (390px), no "lens", saves, lock for non-scribe, reload.
8. Live: copy built pages over the repo files (check git head and live md5 first — other chats pushed twice on 27 Oct), give SQL then the PowerShell push (one block starting `cd C:\Users\Carol\ibsl-platform`, every file named in `git add`, commit message ending with the new session's attribution lines). Verify the push by reading `.git\refs` and blob hashes; read the live pages with WebFetch.
9. Live simulation for the test account (Test Participant, team Alpha, Alpha Client Services, one member) in Chrome with the test account signed in by Carol (never sign in for her), so the Capstone u11 section shows Agreed.

## 6. Technical rules
- Never run git in her folder. The device shell cannot delete: move files to `Claude outputs\_to_delete`. Pages are UTF-8, CRLF: scripts normalise to \n and restore CRLF. Keep device_bash commands under ~12 KB (a larger heredoc failed with E2BIG): write long files in parts.
- Never read the dashboard token from localStorage. Changing the live database from Claude is blocked: SQL goes to Carol.

## 7. Open list after Unit 11
- Unit 12 rebuild (her direction; align the ESRG Scanner card to Unit 10).
- Decks for all units at the end (Units 6–10 also need the ESRG wording and Unit 10's new content); Storage uploads after each deck.

## 8. Unit 11 rebuilt (27 Oct 2026, 20:10-22:04; Carol 22:04 "build live files")
- Carol's Facilitator Guide and Sections 1-5 (five Word files) applied section by section; every decision in `Review files\Unit 11\Unit 11 - decisions and locks.md`, her texts as markdown beside it. Build: `Unit decks\_build\rebuild_u11\` (`build_u11.py` from the backups in `Backups\Unit 11 file backups\Pages before Module 4 rework (27 Oct)`; content `u11_content.py`, `u11_s2.py`, `u11_s3.py`, `u11_s4a.py` + `u11_s4.py`, `u11_s5a.py` + `u11_s5.py` + `u11_s5.js`; links `patch_links_u11.py`; PREVIEW `make_previews_u11.py` + `mock-s2r-u11.js`).
- Section 4 ends with an individual reflection (ref7, five fields, "My Functional Health Accountability") for facilitator feedback; Carol: it does not feed Section 5.
- Section 5 "The Cross-CXO Organisational Health Clinic" is group Capstone work on the shared group record, using her 10-function reference figures and the group's ticked CXO roles (pre-ticked from the Problem Charter executive team). Keys __oh_work, oh_func, oh_cons, oh_rrr, oh_resp = Capstone 11A-11D (4 boxes). SQL `Claude outputs\unit11_health_clinic.sql` (box count u11 = 4).
- Unit Summary removed from both pages (as Unit 10). check_standards: Rule 12 and Rule 27 notes, same as Unit 10.
- Live files written 22:04: `unit4_m1_lens10_p.html` 24aa88a2…, `unit4_m1_lens10_f.html` 7427fb60…, `capstone_P.html` 9b3f9ddd…, `dashboard_F.html` 5461e494…, `build_collection.js` 7d4cc0f5…, `collection.html` bef1096f…. Head before the push: 64eae8b4.
- Still to do: Carol runs the SQL and the push; live check; test account simulation of Unit 11 Section 5 (Capstone u11 Agreed); Unit 12; decks at the end.
