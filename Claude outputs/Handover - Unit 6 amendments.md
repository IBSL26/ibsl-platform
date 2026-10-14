# Handover — Unit 6 · Performance Management Setup: Carol's amended content

Written 14 October 2026 (19:00) for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party" and makes the technical and database decisions.

Her words (14 October, 18:59): "I have amended the content to add an additional layer to performance management. We are starting with Module 3 · Influence · Unit 6 Performance Management Setup. I will give you the amended texts."

Take the exact task from her first message in the new chat. She will give the amended texts. Read them in full before building anything.

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Units 6 to 8 review.md`: the three units, the state of the files, the work in flight (Unit 9 in her review; the S2R® Capability Blueprint decisions) and the lessons of 13 October. Everything in it still holds, except where this file updates it.
3. `Claude outputs\Handover - Unit 8.md`, sections 2 and 3: the working rules and the standard every unit holds.
4. `STANDARDS.md`, then `node check_standards.js` (read-only).
5. `Unit decks\_build\rebuild_u06\README.md` and `u6_content.py`: how Unit 6 was last built (9 October). Changes are made with a script on top of the live pages, after a backup.

Folder on her computer: `C:\Users\Carol\ibsl-platform` (in the device shell `$HOME/mnt/ibsl-platform`). Live site: ibslportal.netlify.app. Database: Supabase project "S2R Portal Production".

## 1. Talk in units, never in file names

On 14 October Carol thought the live Unit 6 held Unit 7 content because a GitHub file name carries a number one lower than the unit (the "lens6" file is Unit 7). Checked the same day: GitHub, her computer and the live portal all hold the right content in the right place. In every message to her, say "Unit 6", "Unit 7", "the Unit 6 deck"; never a file name or a lens id. If a file name must be given, give the full path and say which unit it is.

| Unit | Portal pages (technical names, for Claude only) | Deck |
|---|---|---|
| Unit 6 · Performance Management Setup | `unit3_m1_lens5_p.html`, `unit3_m1_lens5_f.html` (lens id `u3m1_lens5`) | `Unit decks\Unit 06 - Performance Management Setup.pptx` (28 slides) |
| Unit 7 · Establishing Performance Expectations | `unit3_m1_lens6_p.html`, `unit3_m1_lens6_f.html` (`u3m1_lens6`) | `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` |
| Unit 8 · Performance Measurement | `unit3_m2_lens7_p.html`, `unit3_m2_lens7_f.html` (`u3m2_lens7`) | `Unit decks\Unit 08 - Performance Measurement.pptx` |

## 2. State on 14 October, 19:00 (read-only)

- Unit 6 pages: participant md5 2c32a4c9…, facilitator 3be28b68…; deck 19c48b04… (identical to `Claude outputs\Deck upload\Module-3\unit-06.pptx`). Same as GitHub and live.
- `capstone_P.html` 9c244e49… · `dashboard_F.html` eacaeaab… · `build_collection.js` 7911dbc5…
- Git: `main` = `origin/main` = `0a7236567da6f2cac7990aba86a55c35bb7ee857`. Her push of the Unit 9 notes and build files (14 October) may or may not have happened; read `.git\refs\heads\main` to see.
- Lock files: `Unit decks\~$Unit 09 - Strategic Unclogging.pptx` was present this morning (her Unit 9 deck open). Check for a lock on the Unit 6 deck before any deck work.

**Live Unit 6 today:** Section 1 Foundations of Performance Management (1.1 Measurement vs Management · 1.2 The FACES Framework · 1.3 The Three Sights of Progress · 1.4 Leader's Response · 1.5 The Impact of a Calibrated System) · Section 2 PM as an Execution Bridge (2.1–2.3) · Section 3 PM in the Executive Context (3.1 Unity in Diversity · 3.2 The Three Execution Gaps · 3.3 The Continuous PM Shift) · Section 4 Designing for Enterprise Performance (4.1 The EXECUTION Framework) · Section 5 Designing the PM Architecture (group Capstone work in four steps: Scoring Logic, FACES, EXECUTION, PM Scorecards for the CEO and CFO on two Key Results; Capstone boxes 6A–6D; `__pm_work`, on Confirm `pm_scoring`, `pm_faces`, `pm_execution`, `pm_scorecards`).

Seen in the Unit 6 deck on 14 October (for the review): slides 19 and 20 are numbered 3.3 and 3.4 (pages: 3.2, 3.3); slide 16 shows reflection "2.4" (no 2.4 on the pages); slide 9 carries a time ("immediate improvement plan within 30 days").

## 3. Her amended content (found in her folder, not yet read in full)

`Claude outputs\Amended Unit Content\Amended content.docx` (saved 14 October, 16:57; 382 paragraphs, 13 tables). She may paste the texts in the chat as well; the texts she gives are the source.

What its headings show (read the whole document before acting on any of this):
- **Section 1 · Foundations of Enterprise Performance Management System Design:** 1.1 Measurement vs Management; Two Operating Systems Behind Enterprise Performance (the Human Operating System: performance against KPIs and objectives, and against behavioural expectations; the Organisational Operating System: E Environment, S Systems, R Resources, G Governance; how the two interact; the Enterprise Performance Principle; an individual reflection); the S2R Contribution Map™ (what it is, why it matters, its logic: Enterprise OKR → required functional contributions → the two operating systems); 1.4 The FACES Framework applied to both operating systems.
- **Section 2 · Performance Management as the Execution Bridge:** 2.1 the four execution bridges and how they work together; 2.2 Compliance vs Commitment Architecture (four dimensions; accountability across the two operating systems). New section outcomes.
- **Section 3 · Executive Performance Integration and the Evolution of Performance Management:** 3.1 Unity in Diversity: Executive Performance Perspectives (the ten executive performance hot zones, across both operating systems); 3.2 The Continuous Performance Management Shift (three shifts). New section outcomes.
- **Section 4 · Integrating Human and Organisational Performance:** 4.1 Mapping the Contributions Required for Enterprise Results (worked example: customer enquiries resolved within 48 hours, 65% to 90%; Customer Service, IT, Operations, Workforce Planning); 4.2 Managing the Contributions Through FACES. New section outcomes.
- **Section 5 · Building Your Enterprise Performance Management System:** Capstone application in two activities: Activity 1, build the S2R Contribution Map™ from one enterprise Key Result; Activity 2, apply FACES to the Contribution Map.

Points to check against the standard when her texts arrive (report them in one line each, then build):
- Numbering in the document is uneven (two parts numbered 1.3; 1.2.1 and 1.2.2 under 1.3; 1.3.1 to 1.3.4 under the Contribution Map). The pages need one clean numbering, the same on both pages and in the deck.
- Section 4 is headed "Integration — How"; the standard tab reads "Integration — Collective".
- Section 5 says outputs are "automatically added to your CESI Capstone Portfolio" and fields are "automatically populated": her rule is that nothing says anything is automated. Section 5 is group work and Capstone work (Units 5 to 8 standard): one record, Confirm and Print, feeding the S2R® Capability Blueprint.
- Section learning outcomes change in Sections 2, 3 and 4 (and likely 1 and 5); the unit's Key learning outcomes must still align. Outcomes are hers: use her wording.
- "S2R" carries ® in visible text ("S2R® Contribution Map™").
- What leaves the live unit: 1.3 The Three Sights of Progress, 1.4 Leader's Response, 1.5 The Impact of a Calibrated System, 2.3 Leader vs Team, 3.2 The Three Execution Gaps, 4.1 The EXECUTION Framework, and Section 5's Scoring Logic, EXECUTION and CEO/CFO scorecards. Confirm with her texts what stays.

## 4. What a change to Unit 6 touches

- **Capstone boxes 6A–6D** (Scoring logic, FACES, EXECUTION, PM scorecards) change to the new Section 5 outputs: box names and number in `capstone_P.html` (`BLUEPRINT` u6, `PULL.u6`), the database count `capstone_section_box_count` (SQL modelled on `Claude outputs\capstone_unit6_boxes.sql`), labels in `dashboard_F.html`, `CAPSTONE_KEYS.u3m1_lens5` in `build_collection.js`, then `node build_collection.js`.
- **Later units may lean on Unit 6:** a quick search on 14 October found no direct mention of "Unit 6" in the Unit 7 and Unit 8 pages. Before building, search Units 7, 8 and 9 (pages and decks) for the content that leaves (scoring logic, rating scale, three sights, EXECUTION, scorecards, review cadence) and report every hit.
- **The Unit 9 PREVIEW** (in her review) reads Unit 7 Key Results and Unit 8 decision points only; it does not read Unit 6.
- **The S2R® Capability Blueprint document** (`Claude outputs\Capstone\S2R Capability Blueprint - Framework, Charter and Guide.docx`) lists boxes 6A–6D in section 2: update it when the Unit 6 boxes change. Its build script `build.js` exists only in the earlier cloud workspace; rebuild the document from the box list in `capstone_P.html` if needed.
- **The deck:** after the pages are agreed, the Unit 6 deck is brought to the new content on top of her file, with reflection slides and the reader pictures remade.

## 5. Order of work

Read her texts in full → one short list of the points in section 3 that need her word, in plain words → backups (`Claude outputs\Backups\Unit 6 file backups\` and `Unit 6 deck backups\`, dated 14 Oct) → PREVIEW pages in `Claude outputs\Review files\Unit 6\` → her amendments in rounds → her approval → live pages, Capstone link, box count SQL, report labels, Learning Portfolio → end-to-end test → deck → reflection pictures and reader folder → final scan → her push, SQL and Storage upload.

When she says "rework" or gives texts to apply, build the PREVIEW pages straight away: she reviews files, not reports.
