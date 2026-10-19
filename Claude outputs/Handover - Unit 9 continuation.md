# Handover — Unit 9 continuation (Section 2 rework and open Unit 9 items)

Written 19 October 2026, 20:50, for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party": it makes the technical and database decisions and carries out technical steps itself (Storage uploads through Claude in Chrome included). Her instruction is final: never answer an instruction with options or a question on the same point. When she asks for a change, apply it everywhere (both pages, deck slides and notes, reflection pictures, capstone, report labels, upload copy, reader folder) without being told. Apply every point of an amendment message in one pass.

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 9 two performance views.md` (16 Oct): sections 3 and 4 are Carol's rules for the two performance views; section 5 the build order; section 6 how Claude does the technical steps.
3. `Claude outputs\Review files\Unit 9\Unit 9 two views - locked amendments.md`: everything locked for Unit 9 (Facilitator Guide, Section 1, new 1.2 Seven Clog Map, COMPASS removed, Sections 3, 4, 5) and the build record. Section 2 is PARKED there with her notes.
4. The locked section texts beside it: `Unit 9 part 1.2 - Seven Clog Map (locked 16 Oct).md`, `Unit 9 Section 3 - CXO Performance Clogs (locked 16 Oct).md`, `Unit 9 Section 4 - Integration R3 and levers (locked 16 Oct).md`, `Unit 9 Section 5 - Strategic Unclogging Clinic (locked 16 Oct).md`.
5. `Claude outputs\Handover - Units 2 to 9 consistency review.md` sections 3, 5, 7, 8 and the end of `Claude outputs\Units 2 to 9 - Consistency review (findings).md` (what is still open).
6. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules and the unit standard).
7. `Claude outputs\Handover - Unit 1 Charter and Unit 2 capstone.md` sections 1, 5 and 6 (shared group record, SQL and Storage rules learnt on 19 Oct).
8. Build method: `Unit decks\_build\rebuild_u09pv\` (README, `test_u09pv.py`, `e2e_u09pv.py`, `deck_u09pv.py`; e2e uses `rebuild_u06\fake-supabase.js`) and `Unit decks\_build\team_record_19oct\` (`team_patch.py`, `e2e_team_units.py`, `test/fake-supabase-team.js` for the group record).
9. Live Unit 10 pages `unit4_m1_lens9_p.html` / `_f.html` (ESRG Alignment) for realistic organisational examples (Environment, Systems, Resources, Governance and sub-themes).

## 1. State on 19 October, 20:45 (checked)

- Git: `main` = `origin/main` = `cc2fc81ad1f1d1f47ee58efa04494f7ccf72d20e` (shared group record, Unit 2 capstone, Units 1, 3–9 on the group record). Everything below is live.
- Unit 9 pages (live): participant `unit3_m2_lens8_p.html` 641a7058…, facilitator `unit3_m2_lens8_f.html` fdce01ae… (19 Oct 17:24: the 16 Oct two-views build + Carol's 19 Oct capability outcomes + the shared group record in Section 5).
- Unit 9 deck: `Unit decks\Unit 09 - Strategic Unclogging.pptx` 7f3fd5b2…, identical to `Claude outputs\Deck upload\Module-3\unit-09.pptx`, 31 slides.
- Storage (facilitator_decks, Module-3): unit-09.pptx and folder unit-09 (31 pictures + manifest.json = 32 files) re-uploaded by Claude on 19 Oct evening; SQL check: no "(1)" duplicates.
- Database: `team_work` / `team_work_agreement` tables and the `team_work_*` functions are live (Carol ran `Claude outputs\team_work_shared_record.sql`).
- Unit 9 Section 5 is group Capstone work on the shared group record: the group picks a scribe for this assignment in the group record bar (`#twBar`, `s2r-team.js`); only the scribe types; entries appear on every member's page; each member selects Agree; the work goes into the Capstone (boxes 9A–9E, `PULL.u9`) only when all have agreed. Page wording: "Your group chooses its scribe for this work in the group record bar. The scribe types what your group agrees, and the entries appear on every member's page." and "select Agree".
- Unit 9 Section 2 outcomes on the pages now (Carol's own, 19 Oct, `consistency_19oct\outcomes_locked_19oct.json`): "Select and apply responses to strategic clogs across people and organisational performance." · "Intervene early in emerging execution friction before it compounds." These replace the 15 Oct outcome "Resolve the strategy clogs…".

## 2. What is open on Unit 9

1. **Section 2 · Intelligence rework (main task; waits for Carol's instructions).** Parked since 15 Oct 21:07 ("you are not quite landing the thinking. I will come back to it tomorrow"). Section 2 on the live pages is unchanged except the guidance question ("Where are our people and our organisational conditions not yet ready to carry the strategy?"): 2.1 Clogs Are Design Signals (+ reflection "Where Is Your System Not Yet Ready?"), 2.2 Three Disciplines of Execution Engineering (Early Identification, Accurate Classification, Targeted Intervention), 2.3 The 7 Strategic Unclogging Levers (4.4 refers back to it: keep it unless she removes it). Her notes: she removed "A new strategy stretches both, and the stretch on each side can be read before execution begins."; the 2.1 two-side pair confused her ("what are we saying"); the 2.2/2.3 pair drafts were never reviewed. Start afresh from the Section 2 outcomes above: build the argument first, then the people and organisational sides; every new paragraph connects to the one before; the seven clogs are the anchor.
2. **Wording overlap (never answered):** 1.1 "Where clogs form" uses "human side / organisation side"; 1.2 and Sections 3–5 use her terms "people performance / organisational performance". Raise once when Section 2 is discussed, since Section 2 will use one of the two pairs.
3. After Section 2 is locked: PREVIEW pages, then her "build live files": live pages, Section 2 deck slides and notes (on top of her deck, backup first), reflection picture for any changed prompt, `dashboard_F.html` label for any new reflection key, `node build_collection.js`, tests, Deck upload copy + reader folder (`Unit decks\_build\reader_assets.py`, device shell), `node check_standards.js`, her PowerShell push, Storage (she deletes unit-09.pptx and folder unit-09 first; Claude uploads; SQL count check).

## 3. Rules that govern (summary; full text in the files above)

- Wording: "organisational conditions" everywhere, ESRG named once (1.1 "Where clogs form"); "leaders" for those responsible for the conditions, "individuals" for those delivering KPIs; the organisational question is whether the organisational conditions support the execution of the individuals' tasks; the human content is not rewritten, the organisation side is added; no references to other units or parts inside examples; Units 9–12 teach the environment, Unit 9 stays consistent with Unit 10 without teaching its tools.
- Shape: two-side cards after each part's narrative (blue people, green organisation; `u8v-hc`, stacked `u8v-st`); executive-level depth, organisation examples from the Unit 10 domains with sub-themes, two or three per card, each a concrete situation (signal → effect on the tasks → why the review misses it); long sub-parts collapse (`details.u9-det`); facilitator guidance boxes short, detail in the slide notes.
- Process: propose in chat (short, no menus), she corrects, then "lock"; record each lock in the locked amendments file at once; when she asks "in full", give the whole section with existing text and **[New]** marks in page order; Word files she sends with "Lock it" are saved as markdown in `Review files\Unit 9\` and applied as written (standing rules only, say which in one line).
- Voice: participant "you / your group"; facilitator "participants / the group"; no times; no review wording on group work; British spelling; no contrast constructions; no floating generic statements; never "lens" in visible text.
- Technical: never run git in her folder (check pushes by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`); DB changes go to her as SQL in a chat code block (read-only checks by Claude in the SQL editor are fine); never read the dashboard token from localStorage; the device shell cannot delete (move to `Claude outputs\_to_delete`); re-commits use a new staged file name and an md5 check; PowerShell push with the full grade-5 walk-through, one block starting `cd C:\Users\Carol\ibsl-platform`, every file in `git add`, commit message ending with the new session's attribution lines.

## 4. Other open items (not Unit 9)

- Unit 3: split the 8 dense slides (16–21, 27, 32) to reach 24pt.
- Later (proposed 13 Oct, not ordered): show the group's central problem (1H) and chosen challenges (1G) read-only at the top of each unit's capstone section, Units 2 to 12.

## 5. Not committed yet

Add to the next `git add` line: `"Claude outputs/Handover - Unit 9 continuation.md"` and `"Claude outputs/Handover - Unit 1 Charter and Unit 2 capstone.md"` (its section 6 was written after the last push).

## 6. Section 2 rework built live (19 Oct, evening; Carol 21:49 "build live files")
- Carol's instructions and what was built: last section of `Review files\Unit 9\Unit 9 two views - locked amendments.md`. Method and tests: `Unit decks\_build\rebuild_u09s2\README.md` (static checks 139, node drop-down checks 10, page-script smoke run; this computer's shell has no browser and no network, so browser checks are done on the live site).
- The reflection "Where Is Your System Not Yet Ready?" (ref3) moved to Section 1 part 1.2 with its prompt unchanged, so the deck picture stays valid; dashboard labels are keyed by ref id, so no dashboard change.
- Pages: participant 9a…/facilitator (md5 in the push check); `collection.html` rebuilt. Deck: 32 slides (old 2.1 slide → 1.2; new 1.5; Section 1 Reflections 1.1/1.2/1.5; Section 2 Reflections 2.2; 4.2 Unclogging Cycle ×3; 4.3; 5.1, 5.4, notes), `Unit decks` = `Deck upload\Module-3\unit-09.pptx`; reader folder unit-09 remade (32 pictures + manifest). Old reader files in `_to_delete`.
- Next: Carol's push → check refs and live pages in Chrome → Storage (she deletes unit-09.pptx and folder unit-09; upload). This session has no file-staging tool, so the Storage upload may need Carol's clicks (grade-5 steps).

- DONE 19 Oct 22:35: pushed 8c55f972 (live pages checked in the browser); Storage Module-3: unit-09.pptx and folder unit-09 (33 files) uploaded by Claude through Claude in Chrome after Carol deleted the old ones; no duplicates. Add this file to the next git add.
- 19 Oct 22:55 Capstone chain check (cap_chain.py in Unit decks/_build/capstone_check_19oct, run in the cloud workspace with team_record_19oct/fake-supabase-team.js): Units 1, 3-9 42/42, control fails; Unit 2 by e2e_u2cap F (2A-2F). DB capstone_section_box_count u1-u9 = 8,6,6,6,3,2,5,4,5 (match). CAPSTONE_KEYS and report labels complete. Not linked: Units 10-12 (pages not rebuilt), boxes 4E, 4F, 5A typed on the Capstone page. Unit 3 'Bring in from my Unit 2 page' saves only for the scribe and says 'already match' when the page pre-filled the boxes on load (no Capstone effect).
