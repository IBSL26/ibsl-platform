# Unit 5 three-way match — 8 October 2026

Unit 5 is "Aligning Heart & Mind": `unit3_m1_lens4_p.html` (participant), `unit3_m1_lens4_f.html` (facilitator), `Unit decks\Unit 05 - Aligning Heart & Mind.pptx` (deck). Lens id `u3m1_lens4`.

Source of the changes: `Claude outputs\Unit 5 - Three-way match (findings).md` (ten sections and Appendices A to E), applied on Carol's word "make the changes".
Source of the wording: the two pages as they stood. The fuller text of the two was taken as the shared text. No part was added that Carol did not write, except the how-to boxes, the group-work rule and the PARTICIPANT ACTIVITY notes, whose text is in the findings.

**State on 8 October:** the two pages, the three link files and the deck are written to the portal folder. Carol commits and pushes.

| File | What it does |
|---|---|
| `u5_content.py` | The content both pages share: the seven COMPASS domains, the ten role cards (facilitator voice and participant voice), the group-work rule, the reflection notes, the five-block Unit Summary. |
| `build_p.py <old participant file> <new file>` | Builds the participant file by exact replacements on the old file. Each replacement checks its own count and stops on a miss. |
| `build_f.py <old facilitator file> <new file>` | Builds the facilitator file the same way. Fails if a time or a live entry box is left. |
| `u5_p.js` | Participant tools: the read-only Unit 3 Start and Stop lists (Step 1), the Step 4 record with Confirm and Print. |
| `u5.css` | Styles added to both files. |
| `make_previews.py <p> <f> mock-s2r.js <folder>` | Stand-alone PREVIEW copies (the participant copy saves in the browser only). Never commit or upload them. |
| `mock-s2r.js` | Stand-in save for the previews, with a sample of a member's confirmed Unit 3 Start and Stop lists. |
| `patch_links.py` | The three link changes (Capstone, facilitator report, Learning Portfolio). |
| `export_deck_data.py <p> <f> <u05_data.json>` | Reads the unit content off the two written pages for the deck. Stops if the two pages disagree. |
| `final_scan.py <deck> <p> <f>` | The three-way scan. |

Input for both build scripts: `Claude outputs\Unit 5 file backups\unit3_m1_lens4_[p|f] - before three-way match (8 Oct).html`. Run the scripts from this folder. Both written pages reproduce from the backups byte for byte.

## What changed on the pages

**Both pages**
- Unit name reads "Aligning Heart & Mind" everywhere.
- Parts 1.1, 1.2, 1.5, 1.7, 2.1, 2.2, 3.1, 4.1, 4.2, 4.3 carry one shared text. Principle 2 is three cards. Principle 3 is two boxes with "Both available on demand."
- 3.1 COMPASS: seven panels, each with the full narrative, the Observable Indicators and the question.
- Unit Summary: five blocks, one for each section. The fifth is "Application".

**Participant page**
- Speaks to the participant: 16 exact replacements (list `VOICE`, Appendix D of the findings) and ten role cards in 4.2 ("As CEO, you…").
- 3.1: one rating line above the panels; reflection `ref7` opens "Write your seven ratings."
- Section 5: Steps 1 to 3 are Portfolio work, Step 4 is Capstone work. Each step opens with a how-to box.
- Step 1 shows the member's own confirmed Unit 3 Start and Stop lists, read-only.
- The Team & Executive Identity block is removed, as in Unit 4.
- Step 4: group-work rule, three group boxes, Save Synthesis, the record with Confirm and Print, then the personal 30-Day Behavioural Commitment.
- No "Save to Portfolio / Go to Submit" row. One Submit to Facilitator, at the end of the unit.

**Facilitator page**
- Preparation only. No times: 20 "Suggested time" lines, "Timing", "Allow 15 minutes", "five minutes" and "If time allows" are gone. Build notes are gone.
- 19 numbered PARTICIPANT ACTIVITY notes: one at the foot of each of the 15 parts with a reflection, and one for each of Steps 1 to 4.
- Online delivery wording ("post in the chat").

## Response keys (lens_id `u3m1_lens4`, no database change)

- Reflections: `ref1` to `ref15`, unchanged.
- Step 1, Change Transition Map: `ctm1_*` and `ctm2_*` (`change, group, mind, heart, hands, habit, weakest, owner`), unchanged.
- Step 2, Role Connections: `wp_self_*`, `wp_a_*`, `wp_b_*`, unchanged.
- Step 3, Exchange & Dialogue: `exch_affirmed`, `exch_other_compass`, `exch_disagreement`, `exch_checks`, unchanged.
- Step 4, Plenary Synthesis: `syn_missing_compass`, `syn_strong_compass`, `syn_sequence` (group, Capstone work), `syn_30day` (personal, Portfolio work), unchanged.
- New: `confirmed_items`, with the names "Synthesis · Underactivated COMPASS Domain(s)", "Synthesis · Where Alignment Is Strong", "Synthesis · Agreed Sequence". An edit of any of the three group boxes after Confirm removes the names.
- Step 1 bring-in reads the member's own Unit 3 page (`u2m1_lens2`): `kiss_start`, `kiss_stop`, shown only when `confirmed_items` holds "KISS · Start" and "KISS · Stop".
- No longer written by the page (old answers stay in the database): `team_name`, `exec_name`, `exec_role`.

## Links

- `capstone_P.html`: `PULL.u5` brings box 5C in from `syn_missing_compass`, checked against `confirmed_items`. Boxes 5A, 5B, 5D and 5E are typed by the team.
- `dashboard_F.html`: label "Confirmed by the group" for `confirmed_items` of `u3m1_lens4`.
- `build_collection.js`: `CAPSTONE_KEYS.u3m1_lens4` leaves the group work out of the Learning Portfolio (`syn_missing_compass`, `syn_strong_compass`, `syn_sequence`, `confirmed_items`, and the old `team_name`, `exec_*`). `collection.html` rebuilt with `node build_collection.js`: 5 arc segments, 48 prompts, 0 fallbacks.
- Files before: `Claude outputs\Unit 5 file backups\[capstone_P|dashboard_F|build_collection|collection] - before Unit 5 links (8 Oct)`.

## The deck

`Unit decks\Unit 05 - Aligning Heart & Mind.pptx`: 40 slides, in the format of the Unit 2 to 4 decks (design system `lib2.js`, presenter notes in Carol's approved form). Files in `Unit decks\_build`:

| File | What it does |
|---|---|
| `unit05.js <out.pptx>` | The slides. Reads `u05_data.json` and `u05_notes.js`. Writes `reflections/u05/spec.json`. Titles size themselves from 36pt down to 26pt. |
| `u05_notes.js` | The presenter notes, one entry for each slide. A line that starts with § is a heading or a step title. |
| `u05_data.json` | Written by `rebuild_u05/export_deck_data.py`. |
| `enrich/u05_rebuild.json` | The 19 journal insights. Each is used once, inside the step where it is taught. |
| `shoot_reflections_u05.py <PREVIEW participant page> <u05_data.json> reflections/u05` | Pictures of the 15 reflection boxes. |
| `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py` | Shared scripts, unchanged. |
| `build_u05.sh <folder>` | Runs the steps in order. |
| `reader_assets.py` | Remakes `Claude outputs\Deck upload\Module-3\unit-05` (40 pictures and `manifest.json`). |

Slides: cover, Key learning outcomes, unit journey · Section 1 (1.1; 1.2 overview and Principles 1 to 5; 1.3a the event and the transition; 1.3b the 4 Checks; 1.4 to 1.7; two reflection slides, 1.1 to 1.3 and 1.4 to 1.7) · Section 2 (2.1 to 2.3; reflections) · Section 3 (3.1 to 3.3; reflections) · Section 4 (4.1 to 4.3; reflections) · Section 5 (Steps 1 to 4) · Unit Summary.

- Slide 3 (unit journey) carries KEY FACILITATION QUESTIONS and TONE AND WATCH POINTS, as slide 3 of Carol's Unit 4 deck does.
- Deck only, no match on the pages: slide titles, three taglines in 1.2 from Carol's earlier deck, and the four labels of the kind "Mind · 3S · Explain".
- `final_scan.py` on the final files: 40 slides, 0 problems (198 slide strings found on the pages; outcomes word for word; 16 part titles; 15 reflection questions in the notes; no text under 24pt; no leftovers).
- `lint_notes.py`: 1 hit, "48 hours", the wording of the worked example itself.
- Files before: `Claude outputs\Unit 5 deck backups\` (the 33-slide deck, its script and its reader folder).
- If Carol edits the deck herself, her file is the master: later changes are made in her file, and `unit05.js` is a record.

## Tests

- Participant PREVIEW, 33 checks in a real browser: all pass (save, reload, bring-in of the Unit 3 lists, Confirm, edit after Confirm, Print, lock logic, no console error).
- Phone widths before and after are the same on both pages.
- `node check_standards.js`: no Unit 5 breach.

## Still open (for Carol's word)

- Capstone boxes 5A, 5B, 5D and 5E have no feed from the unit; the team types them.
- Section 5, first outcome, says "one strategic change"; the exercise maps two. Outcomes are hers; left as written.
- Step 1 says the two changes come from the Unit 3 Start and Stop lists; the facilitator briefing keeps "Leaders use the change they carried through the unit as their first map".
- `Claude outputs\Unit 5 deck upload` is an older folder, superseded by `Claude outputs\Deck upload\Module-3`.

## Amendments of 8 October (evening): written to the portal files

Carol amended the unit the same evening and gave her word ("Happy for you to write the live pages"). **The sections above describe the unit as it stood after the three-way match. This section describes the unit as it stands now.** Her instructions are in `Claude outputs\Handover - Unit 5.md`, section 8.

**Build chain for the pages:** file before the three-way match → `build_p.py` / `build_f.py` → `amend_p.py` / `amend_f.py`. The inputs of the amend scripts are kept as `Claude outputs\Unit 5 file backups\unit3_m1_lens4_[p|f] - before amendments (8 Oct evening).html`. The live pages reproduce from them byte for byte.

| File | What it does |
|---|---|
| `u5b_content.py` | Amended content both pages share: Principle 1 (Carol's five links), the OCEAVL teaching text, the 17 toolkit elements (two cues and a trigger each), the worked example, the ten alignment hot zones, Section 5 wording, Unit Summary blocks. Lines marked NEW are Claude's wording. |
| `oceavl.json` | Carol's OCEAVL tool: seven dimensions, three levels each (behavioural DNA, risk, response, routines). Three phrases reworded for the no-contrast and no-times rules. |
| `amend_p.py <built participant page> <new file>` | Applies the amendments to the participant page. |
| `amend_f.py <built facilitator page> <new file>` | Applies them to the facilitator page. Fails if an entry box or a time is left. |
| `u5b_p.js` | Participant tools: OCEAVL personal assessment (3.1), Your Watch List and Team Alignment Plan (Section 5), the Unit 3 Start and Stop lists. It takes the place of `u5_p.js` on the page. |
| `u5b.css` | Styles added to both pages. |
| `patch_links_b.py <dashboard_F> <capstone_P> <build_collection.js> <folder>` | Capstone section 5, report labels, Learning Portfolio keys. Runs on the files as `patch_links.py` left them. |

### The unit now

- **Section 1:** 1.1 · 1.2 (Principle 1 carries Carol's five links: Interpretation, Experience, Choices, Actions, Results, and her closing line) · 1.3 Change Management · 1.3.1 3S · 1.3.2 SCARF · 1.3.3 STAT · 1.3.4 ACE-IT.
- **Section 2:** unchanged.
- **Section 3:** one part, 3.1 The OCEAVL Assessment. COMPASS, "From High Flammables to Burning Platforms" and "Change Readiness" are deleted. OCEAVL is a **personal** assessment: each participant scores themselves 1 to 5 on seven dimensions, reads their own profile and selects Submit to My Team's Capstone. The team's profile is shown in the Capstone once every member has submitted.
- **Section 4:** COMPASS removed. Each role card in 4.2 names its Alignment Hot Zone, one of the 17 toolkit elements, with that element's trigger and two cues word for word: CEO Shift · CFO Transparency · COO Time · CHRO Skill · CTO/CIO Tools · CMO Engagement · CCO Fairness · CPO Authority · CRO Autonomy · CSO Stake.
- **Section 5 · The Alignment Toolkit:** Step 1 The Toolkit (read) · Step 2 Your Watch List (individual, Portfolio work) · Step 3 Team Alignment Plan (group, Capstone work, Confirm and Print) · the 30-Day Behavioural Commitment. The Change Transition Map, Role Connections, Exchange & Dialogue and Plenary Synthesis are gone.
- COMPASS appears nowhere in Unit 5.

### Response keys (lens `u3m1_lens4`)

- Reflections: `ref1` to `ref6`, `ref8` to `ref13`, `ref15`, `ref16` (3.1). `ref7` and `ref14` are no longer written.
- OCEAVL: `__oceavl_work` (`{s:[seven scores]}`), `oceavl_scores`, `oceavl_profile` (the participant's own); `confirmed_items` name "OCEAVL · My Scores".
- Watch list: `__kit_me`, `kit_me`.
- Team plan: `__kit_team`, `kit_team` (record while the group works), `kit_mind`, `kit_heart`, `kit_hands`, `kit_habit` (written on Confirm); `confirmed_items` names "Alignment Plan · Mind", "· Heart", "· Hands", "· Habit". An edit removes the confirmation.
- Commitment: `syn_30day`.
- No longer written: `ctm1_*`, `ctm2_*`, `wp_*`, `exch_*`, `syn_missing_compass`, `syn_strong_compass`, `syn_sequence`.

### Links

- `capstone_P.html`, section Unit 5: 5A Team behavioural profile (typed by the team under the team OCEAVL profile) · 5B to 5E Alignment plan · Mind, Heart, Hands, Habit, brought in from `kit_mind` … `kit_habit` through `PULL.u5`. The team OCEAVL profile is read with the database function `get_capstone_team_oceavl(p_team_id)`.
- **Database:** `Claude outputs\capstone_unit5_oceavl.sql`, five blocks, one new function. It returns counts of High, Balanced and Low for each dimension, with no names, and only when every member of the team has submitted. Tested in a local Postgres: signed out, non-member, none, some and all submitted, odd values, admin. Carol runs it in Supabase. Until she does, the Capstone shows "Your team's profile is not available yet" and everything else works.
- `dashboard_F.html`: headings "OCEAVL Assessment" and "Alignment Toolkit", labels for the new keys.
- `build_collection.js`: `CAPSTONE_KEYS.u3m1_lens4` also leaves out `kit_team`, `kit_mind|heart|hands|habit` and `oceavl_scores`. `collection.html` rebuilt.
- Files before: `Claude outputs\Unit 5 file backups\[…] - before amendments (8 Oct evening)`.

### The deck

`Unit decks\Unit 05 - Aligning Heart & Mind.pptx`: **39 slides**. Changed: Principle 1 (five links), parts renumbered 1.3.1 to 1.3.4, Section 3 (3.1a the seven dimensions, 3.1b how the profile is read, one reflection), 4.1, 4.2 (hot zones), Section 5 (Step 1 The Toolkit, Step 1 Worked example, Step 2, Step 3), Unit Summary, notes throughout. 18 journal insights, each used once ("Listening to strain" left with the High Flammable Zones it names).

- `export_deck_data.py <p> <f> <u05_data.json>` now also writes the OCEAVL, toolkit and hot-zone content for the notes.
- `final_scan.py` on the final files: 39 slides, 0 problems (177 slide strings found on the pages, 14 part titles, 14 reflection questions, no leftovers, COMPASS included in the leftover list).
- `lint_notes.py`: 4 hits, all OCEAVL wording ("from 1 to 5", "stress causes withdrawal").
- Reader folder `Claude outputs\Deck upload\Module-3\unit-05`: 39 pictures and `manifest.json`. `s40.jpg` and five old reflection pictures are in `Claude outputs\_to_delete\unit-05 old files (8 Oct evening)`.
- Files before: `Claude outputs\Unit 5 deck backups\[…] before amendments (8 Oct evening)`.

### Tests

- PREVIEW participant page in a real browser: 38 checks, all pass (numbering, Principle 1, OCEAVL scoring, submit, edit after submit, hot zones word for word against the toolkit, watch list, team plan, Confirm, reload, no script errors). Phone widths unchanged.
- Capstone page with a stand-in database: team profile shown when all have submitted, count shown when some have, plain message when the function is missing; 5B to 5E brought in and saved.
- `node check_standards.js`: no Unit 5, Capstone or report breach.

### Still open (for Carol's word)

- The element chosen for each role in 4.2 and its linking sentence, the ACE-IT cues, the triggers for 3S, STAT and ACE-IT, the 3.1 reflection and the new guidance notes are Claude's wording.
- Section 3 outcomes still speak of misalignment escalating into crisis and of readiness; Section 5's first outcome still speaks of one strategic change and role connections. Outcomes are hers.
- Seven of the 17 elements are tied to no role.
