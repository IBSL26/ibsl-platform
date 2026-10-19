# Handover — Consistency review of Units 2 to 9 (before Unit 10)

Written 19 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party": it makes the technical and database decisions and carries out technical steps itself wherever it can (Storage uploads included).

Her words (19 October, 10:20): "I want us to do a review of consistency from unit 2 to 9 before we go to polishing unit 10."

**The task:** a read-only consistency review of Units 2 to 9 (participant page, facilitator page, deck and notes, Capstone link, report labels, Learning Portfolio). Take the exact scope from her first message in the new chat. Expected order: scan → ONE findings report (`Claude outputs\Units 2 to 9 - Consistency review (findings).md`) with each finding, where it sits and the proposed fix → her decisions → changes unit by unit (backups first, surgical scripts) → tests → her push → Storage upload. Change nothing before her word.

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 8.md`, sections 2 and 3: the working rules and the unit standard. They apply word for word.
3. `Claude outputs\Handover - Unit 9 two performance views.md` sections 3 and 4 (Carol's wording rules for the two performance views) and `Claude outputs\Review files\Unit 9\Unit 9 two views - locked amendments.md` (everything she locked for Unit 9 on 15 and 16 October, and the build record).
4. The two-views handovers of the other units: `Handover - Unit 6 amendments.md`, `Handover - Unit 7 amendments.md`, `Handover - Unit 8 two performance views.md`, and the Unit 8 locks in `Review files\Unit 8\Unit 8 two views - locked amendments.md`.
5. `STANDARDS.md`, then `node check_standards.js` (read-only, in the device shell).
6. The build folders' README files: `Unit decks\_build\rebuild_u02` … `rebuild_u09pv` (each says how the unit was last built and which scripts to reuse).

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 1. The units (talk in units, never in file names; unit = lens number + 1)

| Unit | Title | Lens | Pages (Claude only) | Deck / upload copy |
|---|---|---|---|---|
| 2 | Strategy Visioning & Success in Practice (SiP) | `u2m1_lens1` | `unit2_m1_lens1_p/_f.html` | `Unit 02 - …pptx` / `Module-2\unit-02` |
| 3 | SiP KISS Mapping & OKR Definition | `u2m1_lens2` | `unit2_m1_lens2_p/_f.html` | `Unit 03 - …` / `Module-2\unit-03` |
| 4 | Direction Integrity (ABCV-MBT) | `u2m1_lens3` | `unit2_m1_lens3_p/_f.html` | `Unit 04 - …` / `Module-2\unit-04` |
| 5 | Aligning Heart & Mind | `u3m1_lens4` | `unit3_m1_lens4_p/_f.html` | `Unit 05 - …` / `Module-3\unit-05` |
| 6 | Performance Management Setup | `u3m1_lens5` | `unit3_m1_lens5_p/_f.html` | `Unit 06 - …` / `Module-3\unit-06` |
| 7 | Establishing Performance Expectations | `u3m1_lens6` | `unit3_m1_lens6_p/_f.html` | `Unit 07 - …` / `Module-3\unit-07` |
| 8 | Performance Measurement | `u3m2_lens7` | `unit3_m2_lens7_p/_f.html` | `Unit 08 - …` / `Module-3\unit-08` |
| 9 | Strategic Unclogging | `u3m2_lens8` | `unit3_m2_lens8_p/_f.html` | `Unit 09 - …` / `Module-3\unit-09` |

Unit 10 (ESRG Alignment, `u4m1_lens9`) is next for polishing and teaches the organisational conditions in depth; Units 2–9 must stay consistent with it without teaching its tools.

## 2. State on 19 October, 10:30 (checked, read-only)

- Git: `main` = `origin/main` = `662429978e3d41185066f8ce5914e76af93e6b7a` (Unit 9 two performance views, pushed 16 Oct). Everything below is live.
- Page md5 (first 8): U2 p 9e045629 / f b25f6db0 · U3 p ddec1179 / f acbc7bc4 · U4 p f063c182 / f 834260b4 · U5 p 5a24b5c3 / f 97f0d2b9 · U6 p 77cbdf46 / f 3612f2a7 · U7 p eff6a305 / f 23d72c8e · U8 p 0fc2ce6b / f 79134784 · U9 p da8d1d85 / f 7b142dcb.
- Decks: `Unit decks` identical to the `Deck upload` copies for Units 2, 3, 5, 6, 7, 8, 9. **Unit 4 differs**: `Unit decks\Unit 04 …` f27020a1 (12 Oct 08:24) vs `Deck upload\Module-2\unit-04.pptx` 4a5416cb (8 Oct 09:24): find out which is in Storage and whether the reader folder (30 files) matches; report it as a finding.
- No `~$` lock file in `Unit decks`.
- `node check_standards.js`: 243 lines, all small slide text (20pt/18pt) in the Unit 01, 03 and 05 decks (Unit 03 slide 16 the largest share; Unit 05 slide 33). No page breach for Units 2–9.
- Capstone (`capstone_P.html` 8e5ee92a): PULL rows for u2–u9; box counts in the database unchanged (Unit 9 five boxes 9A–9E). Report labels `dashboard_F.html` db4168de; Learning Portfolio `build_collection.js` 8e9f9ce9 → `collection.html` (rebuild with `node build_collection.js` after any page change).

## 3. What the review should cover (proposed checklist; Carol sets the scope)

1. **The two performance views across Units 6–9.** The wording drifted unit by unit:
   - Unit 6 and 7 (14 Oct): "Human Operating System" / "Organisational Operating System", ESRG named many times (Unit 6 page 57 mentions, Unit 7 27).
   - Unit 8 (15 Oct): "From the human side" / "From the organisation side", "organisational conditions", ESRG named once (1.1, "agreed in Unit 6").
   - Unit 9 (16 Oct): her own new terms "people performance" / "organisational performance" (1.2 and Sections 3–5) alongside the locked 1.1 "human side / organisation side" pair; ESRG named once (1.1 "Where clogs form").
   - Her standing rules (15 Oct): "organisational conditions" everywhere, ESRG named once where first defined, "leaders" for those responsible for the conditions, "individuals" for KPI deliverers, the organisational question = whether the conditions support the execution of the individuals' tasks. Units 2–5 carry neither view: ask whether they should.
   - Open from Unit 9 (never answered): 1.1 "Where clogs form" (human side / organisation side) now overlaps the 1.2 opening (organisational performance / people performance).
2. **Learning outcomes.** Key learning outcomes per unit (4) and two section outcomes per section, capability statements (15 Oct round: never "Explain", "Assess how…", "Anticipate where…"). Unit 9 Sections 3 and 5 now carry Carol's own outcomes ("Reveal…", "Examine…", "Classify…", "Develop…"): check them against the same rule and report, do not change.
3. **Unit standard** (Handover - Unit 8 §3): Section 5 = group Capstone work with one record, Confirm, Print; "How Section 5 works" box; Portfolio work boxes; one Submit at the end; reflections with `ref-prompt`, `id`, `KEYS`, report label; back link top left; three-way match of pages and deck (titles, sub-lines, outcomes, part numbers); reflection slides per section; no times; no facilitator review of group work ("Watch for", "Check that"…); voice (participant "you / your group", facilitator "participants / the group").
4. **Cross-unit chain.** Unit 7's two Key Results and owners feed Units 8 and 9 (Unit 9 5.1 shows them read-only); Unit 8 decision points; Capstone box names and descriptions follow each unit's group outputs. Check every "part N.N" and "Unit N" reference still points at something that exists (Unit 9 parts were renumbered: old 1.2/1.3, 3.1/3.2, 4.1–4.4 and Section 5 are gone).
5. **Frameworks.** COMPASS was removed from Unit 9 (16 Oct, her decision); no visible COMPASS on Units 2–8 pages today. Check decks and notes of Units 2–8 for COMPASS and for references to Unit 9's old content (friction signals, diagnostic triads, Clog Clinic, Enterprise Unclogging Agenda, 4-step activation). Also: R3 (Review–Realign–Restore) as taught in Unit 8 vs used in Unit 9 Section 4; GROW wording (Unit 7 / Unit 8 4.2); Three Performance Lines of Sight (new in Unit 9) vs Unit 6 "Three Sights of Progress".
6. **Presentation.** Collapsible sub-sections (Unit 9 uses `details.u9-det` for long sub-parts; Unit 5 has some); tables; two-side card colours (blue human/people, green organisation) used the same way in Units 8 and 9 (Unit 9 1.2 puts organisation first, as in Carol's text).
7. **Decks.** Slide text 24pt and larger (Unit 01/03/05 breaches above); notes format; reflection pictures match the current prompts; reader folders match the decks (Unit 4 above).

## 4. How to scan (read-only)

- Device shell for reading her files (python3, node and LibreOffice are there; playwright is not). Stage files into the cloud workspace for browser work (`device_stage_files`, max 50 per call) and run Playwright there (Chromium at `/opt/pw-browsers`).
- Extract visible text per page (strip script/style) and compare across units; dump deck slide texts and notes with python-pptx.
- Reusable: `Unit decks\_build\lint_notes.py` (notes rules), `rebuild_u07\final_scan_u07.py` (three-way scan), `rebuild_u09pv\test_u09pv.py` and `e2e_u09pv.py` (Unit 9 checks; e2e uses `rebuild_u06\fake-supabase.js`).

## 5. Working rules learnt in the Unit 9 round (16 Oct)

- She sends finished text as Word files ("Lock it"): save it to `Review files\Unit N\` as markdown, record the lock in the unit's locked amendments file at once, and apply the standing rules only where a sentence breaks one (say which, in one line).
- "Use appropriate language for facilitator and participant files": the shared text is voiced per page (participant "you / your group"; facilitator "participants / the group"; questions shown on the facilitator page in quotes or as a table).
- Long sub-parts collapse; facilitator lists of questions read better as tables; "what the group submits" comes before the exercise.
- Deck rebuilds go on top of her deck (backup first); new slides are copies of her own slides; check the md5 of `Unit decks\<deck>` and the lock file before writing.
- Storage: she deletes the old `unit-NN.pptx` and `unit-NN` folder (Claude may not delete); Claude uploads through Claude in Chrome (`file_upload`, staged paths under `/mnt/user-data/uploads/ibsl-platform/…`, max 10 MB per call), then checks there is no "(1)" duplicate.
- PowerShell push: whole walk-through every time; one block starting `cd C:\Users\Carol\ibsl-platform`, every file named in `git add`, commit message ending with the session's attribution lines. Never run git in her folder; check a push by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`.
- Replies short, no menus; her instruction is final.

## 6. Not committed yet

Add to the next `git add` line: `"Claude outputs/Handover - Units 2 to 9 consistency review.md"` (this file).


## 7. Done on 19 October (afternoon session)

Carol (10:44): "So address all including comitting pending work". Built, tested, not yet pushed. Method, scripts and tests: `Unit decks\_build\consistency_19oct\README.md`. What is still open: end of `Claude outputs\Units 2 to 9 - Consistency review (findings).md`. After her push: check the refs, read the live pages, then Storage upload of all eight decks and reader folders (Module-2 unit-02 to 04, Module-3 unit-05 to 09; she deletes the old ones first).
