# Handover — Review of Units 6, 7 and 8 (Performance Management)

Written 14 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party" and makes the technical and database decisions.

Her words (14 October, 09:23): "Give me hand over notes for review of units 6,7,8 in a new chat. There is a component of Performance Management that I want us to explore." Take the exact task from her first message in the new chat. She has not yet named the component. Read and wait for her words before proposing anything.

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 8.md`, sections 2 and 3: the working rules and the standard the units hold. They apply word for word. This file does not repeat them.
3. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only). On 14 October it reports only the known 310 lines of small text in the Unit 06 deck (slide 14).
4. The three live participant pages and their facilitator pages (section 2), then the three decks in `Unit decks`.
5. The build folders `Unit decks\_build\rebuild_u06\`, `rebuild_u07\`, `rebuild_u08\` (README in each): how each unit was last built. Any change is made on top of the live page with a small script, after a backup.
6. Section 5 of this file: what the session of 13 October taught.

Folder on her computer: `C:\Users\Carol\ibsl-platform` (in the device shell `$HOME/mnt/ibsl-platform`). Live site: ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase project "S2R Portal Production".

## 1. The three units (Module 3 · Influence)

Lens numbers are not unit numbers: unit = lens number + 1.

| Unit | Title | Lens id | Participant / facilitator page | Deck |
|---|---|---|---|---|
| 6 | Performance Management Setup | `u3m1_lens5` | `unit3_m1_lens5_p.html` / `_f.html` | `Unit decks\Unit 06 - Performance Management Setup.pptx` |
| 7 | Establishing Performance Expectations | `u3m1_lens6` | `unit3_m1_lens6_p.html` / `_f.html` | `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` |
| 8 | Performance Measurement | `u3m2_lens7` | `unit3_m2_lens7_p.html` / `_f.html` | `Unit decks\Unit 08 - Performance Measurement.pptx` |

**Unit 6 · Performance Management Setup.** Sections: 1 Foundations of Performance Management · 2 PM as an Execution Bridge · 3 PM in the Executive Context · 4 Designing for Enterprise Performance · 5 Designing the PM Architecture. Parts: 1.1 Measurement vs Management · 1.2 The FACES Framework · 1.3 The Three Sights of Progress · 1.4 Leader's Response · 1.5 The Impact of a Calibrated System · 2.1 PM as the Execution Bridge · 2.2 Compliance vs Commitment Architecture · 2.3 Leader vs Team: A Critical Distinction · 3.1 Unity in Diversity · 3.2 The Three Execution Gaps · 3.3 The Continuous PM Shift · 4.1 The EXECUTION Framework · Section 5 group work in four steps (Scoring Logic, FACES, EXECUTION, PM Scorecards for the CEO and CFO on two of the team's Key Results). Saved answers: `ref1`–`ref4`, `ref6`, `ref7`, `ref11`, `ref12`; Section 5 `__pm_work` and, on Confirm, `pm_scoring`, `pm_faces`, `pm_execution`, `pm_scorecards`. Capstone boxes 6A–6D.

**Unit 7 · Establishing Performance Expectations.** Sections: 1 What is Establishing Performance Expectations? · 2 Why Establishing Expectations Determines Execution Outcomes · 3 Where Does the Expectations Gap Emerge? · 4 Cross-Leadership Expectation Architecture · 5 Establishing Delivery Expectations. Parts: 1.1 Setting vs Establishing Expectations · 1.2 The Three Conditions of Established Expectations · 1.3 The Expectations Chain · 1.4 The Alignment Dialogue · 2.1 Compliance vs Commitment: The Execution Dynamic · 2.2 Five Mechanisms · 2.3 Engagement & Accountability: The Two Casualties · 3.1 CXO Expectation Tendencies & Gaps · 4.1 The Four-Step Expectation Architecture · 4.2 Practising the Alignment Dialogue (Portfolio work: `ad_goal`, `ad_reality`, `ad_options`, `ad_will`) · 5.1 Building the Expectation Architecture · 5.2 Conducting the Alignment Dialogue with the Board Chair. Reflections `ref1`–`ref8`. Section 5 `__ex_work` (two Objectives, one Key Result each: `o1_obj`, `o1_kr`, `o1_owner` …) and, on Confirm, `ex_future`, `ex_delivery`, `ex_chain`, `ex_ownership`, `ex_dialogue`. Capstone boxes 7A–7E.

**Unit 8 · Performance Measurement.** Sections: 1 What is Performance Measurement? · 2 Why Performance Measurement Determines Execution Velocity · 3 Where Does Performance Measurement Break Down Across Functions? · 4 Cross-Leadership Performance Intelligence · 5 Applying the Four Consequences of Weak Review Discipline. Parts: 1.1 The Execution Visibility Infrastructure · 1.2 The Four Strategic Purposes · 1.3 From Performance Measurement to Execution Recovery · 1.4 The Accountability Loop · 2.1 Four Consequences of Weak Review Discipline · 3.1 Four Fractures in Performance Measurement · 3.2 The CXO Performance Gap Contributors · 4.1 EPIC · 4.2 The Accountability Loop Role Play (Portfolio work: `rp_review`, `app_rootcause`, `app_corrective`, `rp_judge`) · 5.1 Decision Points Against the Four Consequences. Reflections `ref1`, `ref2`, `ref4`–`ref8`. Section 5 `__rd_work`, `rd_record` and, on Confirm, `rd_warning`, `rd_accountability`, `rd_learning`, `rd_credibility`. Capstone boxes 8A–8D (database count 4).

The units chain: Unit 6 sets the scoring logic and review cadence; Unit 7 establishes two Key Results with owners and alignment scores; Unit 8 sets the review decision points; Unit 9 (in review) diagnoses friction on the same two Key Results and shows the Unit 8 decision points. A change to the PM content of one unit may touch the others and the Capstone boxes.

## 2. State of the files (14 October, 09:30, read-only)

| File | md5 |
|---|---|
| `unit3_m1_lens5_p.html` / `_f.html` | 2c32a4c9… / 3be28b68… |
| `unit3_m1_lens6_p.html` / `_f.html` | 8f45a80b… / 48fbf693… |
| `unit3_m2_lens7_p.html` / `_f.html` | 010c3abf… / f38984cd… |
| Deck Unit 06 | 19c48b04… (identical to `Claude outputs\Deck upload\Module-3\unit-06.pptx`) |
| Deck Unit 07 | f4814297… (identical to `unit-07.pptx`) |
| Deck Unit 08 | e3408c4a… (identical to `unit-08.pptx`) |
| `capstone_P.html` | 9c244e49… |
| `dashboard_F.html` | eacaeaab… |
| `build_collection.js` | 7911dbc5… |

No lock file on the Unit 6, 7 or 8 decks. A lock file `Unit decks\~$Unit 09 - Strategic Unclogging.pptx` exists: Carol has the Unit 9 deck open. Check the md5 again before any deck work; if it differs, she has edited the deck and her file is the master.

Git: `main` = `origin/main` = `0a7236567da6f2cac7990aba86a55c35bb7ee857` ("Alignment Brigade replaced …"). Everything for Units 2 to 8 is pushed and live.

## 3. Other work in flight (do not lose it)

**Unit 9 · Strategic Unclogging (`u3m2_lens8`): in Carol's review.** She said on 14 October, 09:23: "I am reviewing unit 9. I will give review notes." Her notes may arrive in the new chat.
- Findings: `Claude outputs\Unit 9 - Three-way match (findings).md`.
- Review files: `Claude outputs\Review files\Unit 9\PREVIEW - Unit 9 Participant.html` and `PREVIEW - Unit 9 Facilitator.html` (built 13 October; 28 browser checks pass).
- Build: `Unit decks\_build\rebuild_u09\` (`build_u09.py`, `u9_content.py`, `u9_p.js`, `u9.css`, `make_previews_u09.py`, `mock-s2r-u9.js`, `test_u09.py`). Usage: `python3 build_u09.py <p backup> <f backup> <p out> <f out>`, then `make_previews_u09.py`, then `test_u09.py`. Her amendments go into `u9_content.py`.
- Backups: `Claude outputs\Backups\Unit 9 file backups\` (pages md5 d41da670…, b65a81ba…; also `capstone_P`, `dashboard_F`, `build_collection` before Unit 9) and `Claude outputs\Backups\Unit 9 deck backups\`.
- What it holds: Section 5 is the group's Clog Clinic on its two Unit 7 Key Results in five steps feeding Capstone 9A–9E (`__uc_work`, `uc_record`; on Confirm `uc_signals`, `uc_diagnosis`, `uc_levers`, `uc_rhythm`, `uc_agenda` and five "Unclogging · …" names). New part 4.4 Diagnostic Triads (Portfolio work `tc_prep`, `tc_diag`, `tc_lever`). Old keys `team_name`, `ref6`, `app_*` no longer written.
- Not yet done for Unit 9: live pages, `PULL.u9` in `capstone_P.html`, report labels and `FAMILY_DEFS` in `dashboard_F.html`, `CAPSTONE_KEYS.u3m2_lens8` in `build_collection.js`, end-to-end test, deck, reflection pictures, reader folder.
- Waiting for her word: the two Section 5 outcomes ("in their current portfolio"); "the social grease of execution"; "superpower / we've got this".

**Capstone: the S2R® Capability Blueprint (decided 13 October, parked until the three-way checks are done).**
- New brief: each CESI group of seven draws on its members' experience to create one fictional organisation and its Problem Charter during orientation (Unit 1), then builds the Blueprint unit by unit. Guide: `Claude outputs\Capstone\CESI_S2R_Problem_Charter_Participant_Guide.docx`. Fit check: `Claude outputs\Capstone\Capstone - Problem Charter fit (findings).md`.
- Her decisions: the name is **S2R® Capability Blueprint** (replaces "Capstone Blueprint" everywhere when the Capstone is built). The Problem Charter becomes Section 1 with boxes 1A–1H. Assessment: each of the 12 sections carries 5% (Problem Charter 5%, Direction 15%, Influence 25%, Grounding 15% = 60%); Command 20% and Delivery 20% = 40%; she added the Problem Charter criterion. Her instruction of 14 October: the brief states that each group, as a collective executive team, designs a Strategy2Results® (S2R®) Capability Blueprint for its organisation (added to the document in section 1, its build steps and the guide; the Capstone page intro and brief card carry the same line when the Capstone is built). Her approved document: `Claude outputs\Capstone\S2R Capability Blueprint - Framework, Charter and Guide.docx` (md5 316190e9…; build script `build.js` in the cloud workspace only).
- Agreed build (later): Section 1 Problem Charter on the Capstone page and as Unit 1 group work; each team's organisation name from 1A replaces the cohort-wide case name (`capstone_brief.case_name`); Capstone opens with Unit 1; each unit's Capstone section shows the group's central problem (1G) and capabilities (1F) read only; the assessment card carries the weights.

## 4. Not committed yet

Add to the next `git add` line (with every changed file named; never `git add .`):
- `"Claude outputs/Handover - Unit 9.md"`
- `"Claude outputs/Unit 9 - Three-way match (findings).md"`
- `"Claude outputs/Capstone/Capstone - Problem Charter fit (findings).md"`
- `"Claude outputs/Handover - Units 6 to 8 review.md"` (this file)
- the files of `"Unit decks/_build/rebuild_u09/"` by name

PREVIEW files, `Backups`, `Review files` and `Deck upload` are never committed. Ask Carol whether the Capstone guide and the Blueprint `.docx` belong in git before naming them.

## 5. What 13 October taught

- **State proposals as what will be done.** A "For your word" list of eight points confused her ("Am not sure what you are asking"). Write: what the page does today, what Claude will change, and only the points that are hers (learning outcomes, her own phrases) as "kept as they are, for your word".
- **When she says "rework", build the PREVIEW files straight after the findings.** She reviews files, not reports: "I want to look after you have made the changes."
- **She works on several threads at once** (Capstone brief, Unit 9, now Units 6 to 8). Park a thread with a short note in the handover and come back to it when she says.
- **Word documents she opens lock the file.** Before writing over a file in her folder, check for a lock (Word refuses the write). Ask her to close it, then compare her copy with Claude's before replacing it.
- **Text drawn by script is invisible to a plain text scan.** The participant Unit Summary blocks live in `var SUMMARY` in the page script; read the script as well as the page text.
- Never run git in her folder, not even `git --version`. Check a push by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`.
