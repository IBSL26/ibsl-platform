# Handover — Unit 3 · SiP KISS Mapping & OKR Definition

Written 6 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms. She calls Claude "partner"; Claude is the "tech party" and makes the technical decisions.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root (27 rules).
3. `Claude outputs\Unit 2 deck - notes as Carol approved them (format model).txt`: the notes of her final Unit 2 deck. This is the model for Unit 3.
4. `Claude outputs\Handover - Unit 2 rework.md`, sections 20, 22, 23 and 25 only (teaching first; notes as a classroom conversation; her final decisions; the fifth question).

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`).

## 1. What Carol asked for (her words, 6 October)

"Ok let us move to unit 3. Please get unit 2 PPT as the format for depth, structure, format of facilitator notes. Then scan the participant and facilitator files for the three way match — remember the wording on participant must be in first person."

- **Format model:** her own reviewed Unit 2 deck, `Claude outputs\Deck upload\Module-2\unit-02.pptx` (36 slides, saved by her on 6 October). Use this file. The 48-slide copy in `Unit decks\` is Claude's earlier build and is NOT the model.
- **Three-way match:** participant file, facilitator file and deck must say the same thing: same section and part numbers, same titles and sub-lines, same cards, questions, prompts and activities. The facilitator file is preparation only (no entry boxes) with PARTICIPANT ACTIVITY notes. The deck carries only what the two files carry today.
- **"First person" on the participant file:** in Unit 2 this was applied as direct address: "you / your / your group" on the participant page, "participants / the group" on the facilitator page. Confirm with her at the first review that this is what she means (and that she does not mean "I / my / we").

## 2. Working rules that stay in force

- **Claude never runs git, not even to look.** Carol commits in PowerShell. She must first type `cd C:\Users\Carol\ibsl-platform` (she forgot the `cd` once). Give the lines one at a time.
- No change without her approval. Find and propose everything in one pass. She reviews text in the chat before anything is built. Back up before editing (`Claude outputs\Unit 3 file backups\`, `Unit 3 deck backups\`). Edits are surgical. When she says "fix", fix every instance of the same kind and report it.
- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of"). Never "lens" in visible text. "Strategy2Results®" and "S2R®" always with ®.
- No times anywhere. No pre-work. The four SiP areas are "domains"; WHAT / WHY / HOW / WHEN are "dimensions".
- Unit files: CRLF + UTF-8. Do not change IDs, `lens_id`, links, lock logic or database calls unless required. Database changes go to her as SQL for Supabase.
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`.
- PREVIEW html files are never committed or uploaded. She wants HTML previews and pictures in the chat, not PDF.
- If she edits a deck herself, her file is the master. Check for a `~$` lock file before saving a deck.
- Do not mention on pages or in notes that anything is automated.

## 3. The Unit 2 deck as the model (read the notes dump before writing a line)

Facts: 36 slides, about 15,500 words of notes. Typical depth: content slide 250 to 1,000 words (the nine-concepts slide has 1,600); section slide 80 to 450; reflection slide 220 to 330.

**Structure of every notes page**

1. HEADING in capitals and bold (part number and title).
2. **HOW TO TEACH IT:** (HOW TO USE THIS SLIDE on reflection slides; HOW TO OPEN THE SECTION on section slides, with HOW THIS SECTION RUNS above it).
3. Numbered steps in class order, each with a short bold title. Under it: `Say: "…"`, `Ask: "…"`, what to do, `Listen for: …`. One sentence per line inside a long Say.
4. Everything sits inside a step: the facilitator script, the card text (`What it means, say:`, `When Working, say:`), manuscript detail (`Add:`), each journal insight (`Deepen, say: "…"` then `(Insight: Title. Source: Journal, date — …)`).
5. Last blocks only: **ON THE PORTAL, AFTER THE TEACHING:** and, for group work, **LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:**.
6. Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. No step sends participants to the portal while teaching.

**What Carol changed in her own review (follow these)**

- **Fewer slides.** She cut the deck from 48 to 36: one slide per part. She removed the detail slides Claude had added (the four Flammable patterns, the four element groups, the output, confirm and test, writing the contribution, 5.2) and folded the essentials into the part's own slide. She kept one slide per SiP domain (3.1b to 3.1e) and one per function (2.1.1 to 2.1.3). Do not split a part across several slides unless she asks.
- **Examples.** She added **EXAMPLE** blocks under concepts: a worked statement, and a real case (Kodak) with the questions it raises. Propose one concrete example for each key concept, in the chat, for her approval.
- **Online delivery.** She wrote "paste in the chat" and "post in the chat" and removed the whiteboard lines. Ask her once whether Unit 3 is taught online.
- **Ask more, tell less.** She turned "Signal of Absence, say" into "Signal of Absence, ask and listen for", and added direct cues such as "You ask this" and "Ask who are these".
- **She cut:** many "Listen for" lines, the facilitator exercises hidden inside insights, counts and scoring devices, thin LATER blocks, and long insights down to their core sentence.
- **Section slides:** the two learning outcomes are read inside the steps.
- **Slide titles are hers.** She retitled several slides. Propose titles; do not assume.

**Never again (her complaints on Unit 2)**

- Content left after the steps with no instruction on how to use it.
- Anything in the deck that the two files no longer carry (a removed rating reached the deck through one leftover line of the facilitator file). Scan the facilitator file for leftovers of removed content before building.
- Invented activities. Facilitation questions are fine; exercises, counts and "write this down" need a box on the page or her approval.
- Sending notes she has to restructure herself. Read every notes page from first line to last, then have an independent reader check the notes against the two files.

## 4. Unit 3: the files

| What | File |
|---|---|
| Participant page | `unit2_m1_lens2_p.html` (title "Module 2 · Unit 3 — Participant", `lens_id` `u2m1_lens2`) |
| Facilitator page | `unit2_m1_lens2_f.html` |
| Deck | `Unit decks\Unit 03 - SiP KISS Mapping & OKR Definition.pptx` (29 slides; same file as `Deck upload\Module-2\unit-03.pptx`) |
| Old deck build | `Unit decks\_build\unit03.js`, `source\u03.json`, `enrich\u03.json`, `outlines\u03.json` (old method: do not reuse blindly) |
| Capstone | `capstone_P.html`, block `u3`: boxes 3A Keep, 3B Improve, 3C Start, 3D Stop, 3E Enterprise priorities, 3F Enterprise OKRs |

File naming: the number after "lens" is the unit number minus one (Unit 2 = lens1, Unit 3 = lens2, Unit 4 = lens3).

Sections and parts today (both pages): Section 1 Awareness (1.1 Translating SiP into Action, 1.2 KISS, 1.3 KISS Reflection Table, 1.4 OKR Anatomy, 1.5 Three Steps) · Section 2 Intelligence (2.1, 2.2, 2.3) · Section 3 Extrapolating (3.1, 3.2 Hot Zone Cards, 3.3 Alignment Brigade) · Section 4 Integration (4.1 Six-Step Path, 4.2 Breaking the Biases) · Section 5 Application (see finding A). Reflections on the participant page: 1.1, 1.4, 2.3, 3.2, 4.2.

## 5. First scan of Unit 3 (read-only; nothing was changed; the full line-by-line match is still to do)

**A. Section 5 does not match between the two pages (standards rule 9).**
- Facilitator: "Working Session: KISS Mapping, OKR Construction & Prioritisation", with an unnumbered "Facilitator · Worked Example", 5.1 "Task 1 · Group KISS Reflection Capture", 5.2 "Task 2 · Determine Key Results & De-label the OKR Landscape", an unnumbered "Facilitator · Task 3 · Prioritisation Matrix", Unit Summary.
- Participant: "Your Working Session: KISS Reflection, OKR Drafting & Portfolio", with 5.1 "Task 1 · Your Personal KISS Reflection", 5.2 "Task 2 · Your OKR Contribution", "Portfolio Artefact (3 Prompts)", Unit Summary.
- Task 3 (Prioritisation Matrix) has no place on the participant page. The Portfolio Artefact has no place on the facilitator page. In Unit 2 Carol removed the Portfolio Artefact: ask whether it stays in Unit 3.

**B. Unit 2 words that changed.** Unit 3 still says "Success in Practice narrative" (participant 3 times, facilitator 6), "four future-reality domains" and once "four future-reality dimensions of the SiP" (participant 1.3; "dimensions" is the wrong word), and "Strategic Intent" (facilitator, twice). Unit 2 now produces a Strategy Architecture, a Strategy Intent Statement and four confirmed SiP statements, one per SiP domain. Check every mention, and check that the four domain names match Unit 2 exactly: Customer Experience & Value · Operational Capability & Execution Rhythm · People & Culture Dynamics · Enterprise Value Creation.

**C. Times.** The facilitator page has 22 "Suggested time" lines and other minute counts (27 "minutes" in all), including "Give each leader 5 minutes" and a session architecture with minutes. Two slides show times on the slide itself ("2–3 minutes per domain", "3–4 minutes per Objective"). The deck notes have 33. All must go.

**D. Teaching first.** Section 5 is written as a live working session (individual drafting, then group, then the matrix). It needs the Unit 2 treatment: the facilitator explains each task from the deck; participants do the tasks on the portal afterwards. The facilitator guidance has not been read line by line yet for wording that steers participants through the page.

**E. Whiteboard and flip chart** appear once each on the facilitator page. See "online delivery" above.

**F. The deck is in the old format.** 29 slides, about 12,200 words of notes, laid out as Content / Source detail (S2R® manuscript) / Professional insights. No Say or Ask steps, no reflection slides, a Portfolio Artefact slide, 18 journal insights (keep them, each spoken inside the step where it is used; attach the journals if she wants new ones). In Unit 2 the deck was rebuilt from the two files once they were agreed.

**G. Group work.** Unit 2's rule: the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page; a member's page feeds the team's Capstone Blueprint. Unit 3's pages do not say how group entries are recorded, and the participant page reads only its own answers (it does not show the group's four SiP statements from Unit 2, which the KISS reflection is anchored to). Options to put to her: show the member's four confirmed SiP statements at the top of 1.3 and 5.1; have the Capstone bring 3A to 3F in from the member's page as it does for Unit 2.

**H. Small.** Carol's Unit 2 deck now ends "Unit 3 maps that Success in Practice and defines the Objective Key Results" (she removed "through KISS"); the Unit 2 facilitator page still says "through KISS and defines the OKRs".

## 6. Questions for Carol, to ask in one pass after the full scan

1. Is Unit 3 an alignment job (three-way match, teaching first, no times, new notes format) or does she have new content for it, as she had for Unit 2 (her rebuild document)?
2. Portfolio Artefact: keep or remove?
3. Task 3 · Prioritisation Matrix and the Worked Example: where do they sit on the participant page, and what does the participant record?
4. Section 5: individual work, group work, or both, and in which order after the teaching?
5. "First person": confirm "you / your".
6. Online delivery: "chat" in place of "whiteboard"?

## 7. Suggested order of work

1. Read the model notes. Do the full three-way scan of the two pages (reuse `Unit decks\_build\extract.py unit2_m1_lens2 <out>`; it reads `src/unit2_m1_lens2_f.html` and `_p.html` from the folder it is run in).
2. Send Carol one review document in the chat: every mismatch with the proposed wording, plus the questions above. Nothing is changed before her answer.
3. Apply to the two pages (backup first, CRLF kept, verify: tag balance, inline scripts parse, ids unchanged, browser run with the mock save, standards check). Send HTML previews. She commits.
4. Rebuild the deck from the agreed pages in the Unit 2 format. Give her two or three worked slides in the chat first; build the rest after her yes. Add Section Reflections slides (pictures of the reflection boxes, as in Units 1 and 2).
5. Checks before sending: `lint_notes.py` (wording rules, removed content, loose blocks), `check_alignment.py` (notes against the facilitator page), a full read, an independent reader.
6. After her "Done": commit line, then Supabase: Storage → `facilitator_decks` → `Module-2` → replace `unit-03.pptx` and folder `unit-03` (pictures and `manifest.json` made by `reader_assets.py`).
7. Unit 4 next (`unit2_m1_lens3_*`): same steps.

Tools in `Unit decks\_build`: `lib2.js` and `kit.js` (house deck kit; all slide text 24pt or larger), `u02_notes*.js` (pattern for steps: `S()`, `page()`, `say()`, `ask()`, `IN()`, `pick()`), `format_notes.py`, `lint_notes.py`, `check_alignment.py`, `dump_notes.py`, `add_reflection_slides.py`, `shoot_reflections.py`, `reader_assets.py`. On the device shell `reader_assets.py` must write into scratch first, then copy over (no deletes in the folder).

## 8. Unit 2 items still open (ask before touching)

- **Commit of the fifth question** (element 13, internal forces): the lines were given to her; whether she ran them is not confirmed.
- **Deck reader on the portal:** `Deck upload\Module-2\unit-02\` still holds the 48 pictures and notes of Claude's build, while her `unit-02.pptx` has 36 slides. The pictures and `manifest.json` must be remade from her copy (12 surplus pictures go to `_to_delete`), and she then re-uploads the folder to Supabase. She was asked and has not answered.
- **`Unit decks\Unit 02 - … .pptx`** is still the 48-slide build. Her 36-slide copy should replace it so that the repository holds the master. The Unit 2 build scripts no longer describe her deck: edit her file directly if she asks for changes.
- Her Unit 2 deck still says each element has "four questions" (element 13 now has five), and slide 9 says "four observable indicators" where the pages say "domains". Her deck: mention it, change nothing without her word.

## 9. Unit 3 rebuilt from Carol's amendments (6 October, evening) — waiting for her review of the two pages

Carol sent "unit 3 Amendments.docx" and her game file "Strategy_Airport_Game_Medical_Health (8).html" ("These are the amendments to unit 3 facilitator and participant before we build the PPT"). Copy of her document: `Claude outputs\Unit 3 - Amendments from Carol (6 Oct).docx`. Three-way match findings: `Claude outputs\Unit 3 - Three-way match (findings).md`.

**Her instructions, all built into both pages:**
1. Facilitator: the two incomplete sentences removed (1.1 and 2.1). The sentence that followed each one now names its subject ("The Strategy Intent Statement and the four Success in Practice (SiP) statements provide…"; "The usual cause of OKR frustration: …"). The participant page keeps its own complete opening sentences.
2. 1.5 aligned with the old 4.1: "1.5 — Six Steps: From KISS Output to Enterprise OKRs"; Step 5 is "Enterprise Priority" (never "Panoramic").
3. Old 2.2 (Missing Bridge) removed. Old 2.3 is now 2.2, same title, with a worked example: one simple SiP statement of a client services company, its KISS table, then the six steps. Her answer when asked: "This is the same thing 2.3 becomes 2.2 with the 6 steps".
4. 3.1, 3.2 and 3.3 fused into one 3.1 "Natural OKR Emphasis Across Leadership Functions". The cards are a matching exercise: Dominant Future Realities and Natural OKR Emphasis are given ("suggested"); the participant matches the Typical Hot Zone and the Alignment Question; green light or red alert at once; attempts counted; individual work that goes with the submission. The facilitator page holds the ten full cards as the answer key.
5. Section 4 is group work for the Capstone. 4.1 "Translating SiP to KISS": the group's four SiP statements (brought in from the member's Unit 2 page, editable), the KISS form with the domains and guiding questions of 1.3, Confirm. 4.2 "Translating KISS to OKRs: The Six Steps": themes, Objectives, Key Results with contributing roles, alignment test, enterprise priority (no more than four), Priority Matrix, Confirm. Group rule as in Unit 2 (scribe; every member types on their own page).
6. Section 5 is the Strategy Airport game: playable on the facilitator page for the lesson round (nothing saved), individual saved work on the participant page.
7. Participant: the 1.1 reflection box removed.

**Her three unanswered questions were settled by her standing rule (parts her document does not carry are removed):** old 4.2 Breaking the Biases and its reflection, the Portfolio Artefact and the old Section 5 tasks are gone. Game on the participant page: as her file, without the two example buttons.

**Also aligned (three-way match and Unit 2 wording):** SiP "narrative" → statements; "Strategic Intent" → Strategy Intent Statement; "future-reality dimensions/domains" → SiP domains; fourth domain named Enterprise Value Creation (its questions unchanged); full domain names on the hot zone cards; "your leadership team" → "your group" on the participant page; every time removed from the facilitator page; guidance labels 1.1 to 1.5 renumbered; guidance no longer steers participants through the page; whiteboard and flip chart gone; the things that never existed (capture tool, "Assemble Landscape", Session Report) gone; Unit Summary has five blocks ("you" voice on the participant page); participant 1.2, 1.4 and 2.1 now carry the same content as the facilitator page (card sub-titles, Key Result Construction Guide, closing line of 2.1).

**Files changed on her computer (NOT committed; the live portal still has the old Unit 3):** `unit2_m1_lens2_p.html`, `unit2_m1_lens2_f.html`, `dashboard_F.html` (families and labels for the new answers; KISS domain "ev" renamed), `capstone_P.html` (`PULL.u3`: 3A to 3F brought in from the member's Unit 3 page; no database step, Unit 3 already expects six boxes), `collection.html` (rebuilt), `check_standards.js` and `STANDARDS.md` (rule 10: the Strategy Airport lesson game is the one agreed exception). Backups: `Claude outputs\Unit 3 file backups\… - before rebuild (6 Oct)`. Build scripts and the list of answer keys: `Unit decks\_build\rebuild_u03\README.md`. Previews: `Claude outputs\PREVIEW - Unit 3 Participant.html` and `PREVIEW - Unit 3 Facilitator.html` (never commit or upload them).

**Checked:** standards check clean apart from the 82 Unit 01 deck lines; all inline scripts parse; no duplicate ids; lock gate, access gate, feedback, messages, documents and submit blocks byte-identical to the old files; CRLF kept; browser run with a stand-in save (matching, SiP bring-in, KISS confirm, six steps and confirm, game to the end, reload brings everything back, editing removes a confirmation); Capstone bring-in run against the stand-in database; phone width no wider than the old page. The real database was not touched.

**Her question on the game in the lesson:** a game cannot run inside a slide. The deck gets a game slide; at that slide she stops sharing the deck and shares the browser window that holds the facilitator Unit 3 page (opened before the lesson), then returns to the deck. The facilitator page says the same in 5.1.

**Open with Carol:** her review of the two previews (authored by Claude and not yet read by her: the worked example, the fused 3.1 narrative, the Section 4 wording, the Section 5 introduction, the Unit Summary). Then the commit line and the deck.

**Commit line once she approves (she runs it; Claude never runs git):**
`cd C:\Users\Carol\ibsl-platform` · `git add unit2_m1_lens2_p.html unit2_m1_lens2_f.html capstone_P.html dashboard_F.html collection.html check_standards.js STANDARDS.md "Unit decks/_build/rebuild_u03" "Claude outputs/Handover - Unit 3.md" "Claude outputs/Unit 3 - Three-way match (findings).md"` · `git commit -m "Unit 3 rebuilt: six steps, worked example, matching exercise, Capstone group work, Strategy Airport"; git push`

**Deck (next):** rebuild from the two approved pages in the Unit 2 format. New slide needs: 1.5 six steps; 2.2 worked example; 3.1 (two or three role cards only, the rest is the exercise); 4.1 and 4.2 explained from the deck; a Strategy Airport game slide with the sharing instruction; Section Reflections slides for 1.4, 2.2 and 3.1; no Portfolio slide; no times.

## 10. The deck (built 6 October 2026)

**Built from the two rebuilt pages, on the model of Carol's Unit 2 deck. Not yet reviewed by Carol: she reviews the participant page, the facilitator page and the deck together.**

- Saved as `Unit decks\Unit 03 - SiP KISS Mapping & OKR Definition.pptx` and `Claude outputs\Deck upload\Module-2\unit-03.pptx` (same file). Reader pictures `s01`–`s34` and `manifest.json` remade in `Deck upload\Module-2\unit-03`. Old deck, old `unit03.js` and old manifest are in `Claude outputs\Unit 3 deck backups`.
- 34 slides: cover · outcomes · journey · Section 1 (1.1, 1.2, 1.3, 1.4, 1.5 six steps, 1.5 matrix, Reflections) · Section 2 (2.1, 2.2 sequence, worked example on five slides, Reflections) · Section 3 (3.1a tendencies, 3.1b risks, 3.1c CEO card, 3.1d matching exercise, Reflections) · Section 4 (4.1a, 4.1b, 4.2a, 4.2b) · Section 5 (5.1 Strategy Airport) · Unit Summary.
- Notes: about 13,700 words. Heading, HOW TO TEACH IT, numbered steps with Say / Ask / Listen for / Add, EXAMPLE blocks, each of the 18 journal insights once with its source, then ON THE PORTAL, AFTER THE TEACHING and LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL.
- Game in the lesson: the notes of slide 33 tell the facilitator to stop sharing the deck, share the browser window with the facilitator page at Section 5, play one learning round, then return to the deck.
- Checks run: notes linter (only metric phrases such as "12 hours to 4 hours" and the after-teaching handover are listed), `check_u03.py` (no text under 24pt; outcomes, reflection prompts, titles and alignment-test questions word for word on both pages), every slide rendered and looked at, standards check (only the 82 Unit 01 deck lines).

**Choices made by Claude in the deck (reverse on Carol's word):**
- 3.1c teaches one hot zone card only (the CEO), so that the matching exercise keeps nine roles unseen.
- The worked example shows the KISS entries of one SiP domain on the slide (Customer Experience & Value); the other three are read from the notes.
- Unit Summary: the page's closing question ("Looking at the OKRs we have just built…") is placed after the groups have confirmed their OKRs on the portal, because the teaching comes first.
- EXAMPLE blocks written by Claude: 1.1 (four-hour response), 1.3 (two STOP items), 2.1 (20% revenue target), 3.1b (one quarter, three functions), the failed draft "Launch the new CRM platform by June" and the two released drafts in the worked example.

**Commit lines once she approves pages and deck (she runs them; Claude never runs git):**
`cd C:\Users\Carol\ibsl-platform` · `git add unit2_m1_lens2_p.html unit2_m1_lens2_f.html capstone_P.html dashboard_F.html collection.html check_standards.js STANDARDS.md "Unit decks/_build" "Unit decks/Unit 03 - SiP KISS Mapping & OKR Definition.pptx" "Claude outputs/Handover - Unit 3.md" "Claude outputs/Unit 3 - Three-way match (findings).md"` · `git commit -m "Unit 3 rebuilt: pages and facilitator deck"` · `git push`

(The `Deck upload` folder is for Supabase and is left out of the commit, as for Unit 2.)

**Supabase after the commit:** Storage → `facilitator_decks` → `Module-2` → replace `unit-03.pptx` and the folder `unit-03` with the ones in `Claude outputs\Deck upload\Module-2`. The old folder holds 29 pictures and the new one 34: upload all 34 and the manifest.

## 11. Change of 7 October 2026: 2.2 worked example and individual exercise

**Carol's instruction:** "work on the intelligence enterprise priority - it has to be a working example flowing from step 4 in the facilitator file. In the participant file this is an exercise that they complete from step 1 to step 6 and they submit as individuals."

**Done (on her computer, not committed by her yet):**
- Facilitator file, 2.2: the worked example now carries five themes, Objectives and OKRs. Step 4 ends with the result of the alignment test (five go forward, one draft from one function is returned). Step 5 shows the vote of seven leaders, four enterprise priorities, Objective 5 (Key account growth) released, the trade-off and the Less is More check. Step 6 places the four. A Participant Activity box and one guidance paragraph on Step 5 were added.
- Participant file, 2.2: the worked answers are removed. The page gives the SiP statement and the KISS table and a six-step tool for individual work, with "Mark the exercise complete". Saved under `case_six_steps` and `case_status`; reaches the facilitator with the unit submission.
- Facilitator report: heading "Six-Step Exercise". Collection page rebuilt.
- Deck: now 36 slides; worked example on seven slides; notes name three pieces of individual work (2.2 exercise, 3.1 matching, 5.1 game). Reader pictures `s01`–`s36` remade.
- Checks: browser test of the exercise (messages when incomplete, fifth priority refused, completion, reload, edit after completion), the earlier page tests, script syntax, no duplicate ids, CRLF, standards check (only the 82 Unit 01 deck lines), deck checks.

**Written by Claude and waiting for Carol's review:** the fifth theme and Objective (Key account growth) with its two Key Results; the vote numbers; the trade-off wording; the wording of the participant exercise; the guidance paragraph on Step 5.

**Point for Carol:** the facilitator teaches the worked example from the deck, then each participant does the same case alone. The pages and notes say a participant's answers may differ from the example and still be sound when each one can be traced to the KISS table.

**Commit lines (she runs them, one at a time; Claude never runs git):**
`cd C:\Users\Carol\ibsl-platform` · `git add unit2_m1_lens2_p.html unit2_m1_lens2_f.html capstone_P.html dashboard_F.html collection.html check_standards.js STANDARDS.md "Unit decks/_build/rebuild_u03" "Claude outputs/Handover - Unit 3.md" "Claude outputs/Unit 3 - Three-way match (findings).md"` · `git commit -m "Unit 3: 2.2 worked example and individual six-step exercise"` · `git push`
The deck is committed after her deck review with: `git add "Unit decks"` · `git commit -m "Unit 3 facilitator deck"` · `git push`, then the Supabase upload of `unit-03.pptx` and the folder `unit-03` (36 pictures and the manifest).

## 12. Change of 7 October 2026 (second): clean flow through the six steps, one record, Print

**Carol's instruction (with a screenshot of the two empty output boxes in 4.2):** the steps must flow from Step 1: themes pull into Step 2, Objectives into Step 3, Key Results into Step 4 and Step 5; all data stored and printable at the end. Then: "this is just for participant file. the facilitator file must just give the precise instructions."

**Done (on her computer, not committed by her yet):**
- Participant file, 4.2 (group) and 2.2 (individual exercise): each step shows what the steps before it produced. One "Your six-step record" builds under the steps from Step 1 and is saved; "Print the six-step record" prints it. The old empty boxes ("appear here as you complete Steps 5 and 6") are gone; Enterprise Priorities and Enterprise OKRs show once a priority is selected, and are confirmed as before for the Capstone.
- Facilitator file: no working boxes. The Participant Activity boxes in 2.2 and 4.2 now give numbered, step-by-step instructions. The Unit Summary outputs list names the 2.2 exercise.
- Facilitator report: `okr_drafts` and `case_six_steps` are labelled "Six-step record". Collection page rebuilt.
- Deck: slides unchanged (36). Notes of 4.2a and the 2.2 hand-over describe the same flow, the record and printing.
- Checks: browser test of both tools step by step (what each step shows, locked test until two Key Results, record, print pages, reload, un-confirm on change), earlier page tests, script syntax, no duplicate ids, CRLF, standards check (only the 82 Unit 01 deck lines).

**Commit lines are the same as in section 11** (pages now; deck after her deck review).

## 13. Change of 7 October 2026 (third): record above the step menu; section outcomes under review

- On Carol's word the "Your Six-Step Record" block now sits before the step menu in 4.2 and 2.2. Confirm / Mark complete and Print stay under the steps, under the heading "Confirm and Print" / "Complete and Print". Facilitator instructions and deck notes say "above the steps". Not committed by her yet.
- Carol then asked for the two learning outcomes of each section to be checked against the new content and the Key learning outcomes. Claude's check and proposed wording were given to her in chat for approval; nothing is changed in the files until she approves. Places to change once approved: both pages (section outcome boxes) and the deck (five section slides and their notes; `SLOS` in `u03_notes.js`).

## 14. Section learning outcomes realigned (7 October 2026, Carol's wording)

Carol gave the wording and allowed refinement without change of meaning. Written into both pages, the five section slides of the deck and `SLOS` in `u03_notes.js`. Section 3 and the four Key learning outcomes are unchanged.

| Section | Outcome 1 | Outcome 2 |
|---|---|---|
| 1 | Distinguish the current practices that reinforce strategic progress from those that constrain it. (unchanged) | Translate strategic intent into measurable results. |
| 2 | Recognise the benefits of mapping the terrain before setting goals. | Practise the translation of SiP into OKRs. |
| 3 | Recognise how each leadership function's emphasis shapes the priorities it proposes. (unchanged) | Distinguish functional contributions from the enterprise priorities they serve. (unchanged) |
| 4 | Apply the translation of SiP into OKRs as a group. | Gain collective intelligence for the strategic trajectory. |
| 5 | Reinforce strategy translation capability. | Establish individual capability to set a strategic trajectory. |

Claude's refinements of her words: "Understand" became "Recognise"; "Practice" became "Practise" (verb, British spelling); "SIp/SIP" became "SiP"; "Group application of translating SIP to OKR" became "Apply the translation of SiP into OKRs as a group"; "individual strategy trajectory setting capability" became "individual capability to set a strategic trajectory". Reverse any of these on her word.
Not committed by her yet. Commit lines as in section 11.

## 15. Carol's final deck; pages cleaned and aligned to it (7 October 2026, afternoon)

**Carol:** "DO NOT CHANGE THE PPT. THIS IS THE FINAL VERSION WHICH I HAVE SAVED IN DECK UPLOADS." Her deck: `Claude outputs\Deck upload\Module-2\unit-03.pptx`, 34 slides. No deck file was written in this change.

**Her instructions and what was done in both pages (on her computer, not committed by her yet):**
1. 2.2 is a worked example for the participant too, read-only. The exercise is removed.
2. Step 5 Enterprise Priority removed: five steps in 1.5, 2.2, 4.2, guidance and summaries.
3. Step 1 of the worked example shows the themes only.
4. A clear box for contributing roles under each Key Result in 4.2 (participant).
5. Matching exercise (3.1) and Strategy Airport (5.1) are Portfolio work, with instructions on how to complete them.
6. Section outcomes: Section 4 and Section 5 as she gave them.

**Choices made by Claude (reverse on Carol's word):**
- Section 1 outcome 2 uses the deck's wording, "Translate the intent to measurable results." Section 2 outcomes are back to the pair on her final slide 12 ("Explain why an honest review…" / "Recognise the cost of setting targets…"), because 2.2 is no longer practised and the deck is final. Her earlier pair for Section 2 ("mapping the terrain" / "Practise the translation") is therefore not on the pages.
- Worked example: five themes and Objectives as on slides 17–18; four placed on the matrix as on slide 21. To close the gap, Step 4 says Objective 5 (Key account growth) earns 3 of 4 and returns to Step 2.
- 4.2 follows slide 31: up to four themes, up to two Key Results. With Step 5 gone, every aligned OKR is an enterprise priority.
- The Less is More Rule no longer appears on the pages.

**Open with Carol:**
- Her final deck still says "six steps" in three places: slide 9 (title and the list with Step 5 Enterprise Priority and Step 6), slide 10 (title "Step 6"), slide 31 (title "The Six Steps"), and in several notes. The pages say five. She decides whether to change the slides.
- Slide 7 is titled "1.3 · KISS Application Across SIP Domains"; the pages keep "1.3 — The KISS Reflection Table: Four SiP Domains".
- The deck-reader folder `Deck upload\Module-2\unit-03` still holds the 36 pictures and manifest of the earlier generated deck. They must be remade from her final deck before upload (this does not change the PPT). `Unit decks\Unit 03 - SiP KISS Mapping & OKR Definition.pptx` is also the earlier generated deck. Both wait for her word.

**Commit lines (she runs them, one at a time):**
`cd C:\Users\Carol\ibsl-platform` · `git add unit2_m1_lens2_p.html unit2_m1_lens2_f.html capstone_P.html dashboard_F.html collection.html check_standards.js STANDARDS.md "Unit decks/_build/rebuild_u03" "Claude outputs/Handover - Unit 3.md" "Claude outputs/Unit 3 - Three-way match (findings).md"` · `git commit -m "Unit 3: five steps, worked example, portfolio work, aligned to final deck"` · `git push`


## 16. FINAL STATE (7 October 2026, evening) — ready for Carol to commit

This section replaces the "open with Carol" list at the end of section 15. All three points there are closed.

**Carol's instruction:** Section 2 outcomes as below; four Objectives only; five steps everywhere, slides included; pictures remade from her final deck; final scan; final versions for committing.

**Final files on her computer (not committed yet; she commits herself):**
- `unit2_m1_lens2_p.html` (md5 cfe5ac7a…), `unit2_m1_lens2_f.html` (md5 5ed53789…), `dashboard_F.html`, `collection.html`, `capstone_P.html`.
- Deck: `Claude outputs\Deck upload\Module-2\unit-03.pptx` and `Unit decks\Unit 03 - SiP KISS Mapping & OKR Definition.pptx` (identical, 34 slides, md5 d6b614d0…). This is Carol's final deck with the edits below. Her untouched final is in `Claude outputs\Unit 3 deck backups\unit-03 - Carol final before five-step edits (7 Oct).pptx`.
- Reader folder `Claude outputs\Deck upload\Module-2\unit-03`: `s01.jpg`-`s34.jpg` and `manifest.json`, remade from the final deck. The old `s35.jpg` and `s36.jpg` are in `Claude outputs\_to_delete`.

**What is final in the content:**
- Five steps everywhere (pages and deck): Find Themes, Inspiring Objectives, Define Key Results, Alignment Test, Priority Matrix.
- Worked example: four themes, four Objectives (Customer responsiveness, Execution speed, Collaboration culture, Value creation), two Key Results each with contributing roles; all four earn 4 of 4 and go to the matrix.
- Section 2 outcomes on both pages and slide 12: "Recognise the benefits of mapping the terrain before setting goals." / "Practise the translation of SiP into OKRs."
- Sections 1, 3, 4, 5 outcomes as in section 15.

**Edits made to Carol's deck (text only; her design is untouched):**
- Slide 7: "SIP" to "SiP" (title and notes).
- Slide 9: title "Five Steps"; the Enterprise Priority row removed and the rows re-spaced; last row is "Step 5 · Priority Matrix".
- Slide 10: title says Step 5.
- Slide 12: the two Section 2 outcomes; notes say the worked example runs on seven slides.
- Slides 17 and 18: four themes and four Objectives (Key account growth removed, rows re-spaced). Slide 18: Objective 1 "and"; Objective 3 "Create a culture of shared ownership…" with its text box widened so it sits on one line.
- Slide 21: label "4 · Value creation"; notes heading "STEP 5: THE PRIORITISATION MATRIX".
- Slide 31: title "The Five Steps"; notes say four themes and up to two Key Results.
- Slide 32: a stray full stop removed.
- Notes on slides 1, 2, 3, 4, 8, 14, 16, 29, 33, 34: six to five, "individual work" to "portfolio work", "maximum 2 Key Results each".

**Final scan (`final_scan.py`, deck against both pages):** 0 differences in KLOs, section outcomes, step names, worked example, 3.1 content and part titles; no leftover "six", "Step 6", "Less is More", "Enterprise Priority" step, "individual work", "SIP" or "Key account" in the pages, the slides or the notes. Page tests clean (five-step tabs, 2.2 read-only, portfolio boxes, 4.2 flow with record and print, matching, KISS, Strategy Airport, no console errors).

**One finding for Carol's decision (reported to her, not changed):** `check_standards.js` reports Rule 16 (slide text below 24pt) on her own designed slides: slide 16 (4 lines), 17 (10), 18 (24), 19 (10), 20 (10), 21 (50), 27 (34), 30 (4) = 146 lines, sizes 12.75pt to 20pt. This comes from her slide design. Nothing else is breached. The other 82 Rule 16 lines are the old Unit 01 ones. Do not resize her slides without her word.

**Do not upload by mistake:** `Claude outputs\Deck upload\Module-2\Unit 03.pptx` (capital U, 13:10) is an older copy Carol saved. The one to upload is `unit-03.pptx`.

**Commit lines (she runs them, one at a time, in PowerShell):**
`cd C:\Users\Carol\ibsl-platform` · `git add unit2_m1_lens2_p.html unit2_m1_lens2_f.html capstone_P.html dashboard_F.html collection.html check_standards.js STANDARDS.md "Unit decks" "Claude outputs/Handover - Unit 3.md" "Claude outputs/Unit 3 - Three-way match (findings).md"` · `git commit -m "Unit 3 final: five steps, worked example, portfolio work, final deck"` · `git push`

**After the push (Supabase, she does it):** Storage, bucket `facilitator_decks`, folder `Module-2`: replace `unit-03.pptx` and the whole folder `unit-03` (34 pictures and `manifest.json`) with the ones in `Claude outputs\Deck upload\Module-2`. The old folder in Supabase holds 36 pictures, so `s35.jpg` and `s36.jpg` must be deleted there. The `Deck upload` folder is not committed (same as Unit 2).

**Unit 2 (7 October, on Carol's "go"):** the reader folder `Deck upload\Module-2\unit-02` (36 pictures and manifest) and the `Unit decks` copy now match her 36-slide Unit 2 deck. See `Handover - Unit 2 rework.md` section 27. This closes the first two Unit 2 items in section 8.

## 17. Portfolio work: Save to Portfolio; group work to the Capstone only (7 October 2026, late)

Carol's questions on the committed-ready pages: where participants save the matching exercise and Strategy Airport to the portfolio and send them to the facilitator; whether Steps 2 to 5 take proper input per Objective; that the five-step work pulls into the Capstone and not the Learning Portfolio.

**Done:**
- 3.1 and 5.1 (participant file): a "Portfolio work · Save and submit" row under each exercise with **Save to Portfolio** (confirmation line, counts roles matched or states whether the learning round is finished) and **Go to Submit to Facilitator** (opens Section 5 at the unit's Submit to Facilitator button).
- Decision taken as tech party: one Submit to Facilitator for the unit. A submit on each exercise would send the whole unit as a new submission each time. Carol can reverse this.
- Learning Portfolio (`collection.html`, built by `build_collection.js`): for Unit 3 it now prints Reflections, Hot Zone Matching and Strategy Airport. The KISS map and the five-step outputs are left out; they feed the Capstone Blueprint (3A to 3F) and stay visible in the facilitator's report.
- Steps 2 to 5 checked with entries: one Objective box per theme; two Key Result boxes and a contributing-roles box per Objective; four questions per OKR; Impact and Effort per aligned OKR. Picture sent to Carol.
- Facilitator file: Participant Activity text of 3.1 and 5.1 updated. Deck not changed (its notes already say the work reaches the facilitator when the unit is submitted).
- Seen, not changed: Unit 2's group work still prints in the Learning Portfolio. Same rule can be added for `u2m1_lens1` in `CAPSTONE_KEYS` on Carol's word.

**Files (not committed yet):** `unit2_m1_lens2_p.html` (md5 b4501a5a…), `unit2_m1_lens2_f.html` (md5 12099399…), `collection.html`, `build_collection.js`, `Unit decks\_build\rebuild_u03\`. Commit line in section 16 now also needs `build_collection.js`.

**Unit 2 added (7 October, on Carol's word):** `CAPSTONE_KEYS` in `build_collection.js` now also covers `u2m1_lens1`. The Unit 2 group work (Strategy Architecture, Strategy Intent Statement, Success in Practice: `arch_*`, `org_name`, `strategy_period`, `intent_statement`, `sip_d*_q*`, `sip_d*_st`, `sip_integrated`, `confirmed_items`) is left out of the Learning Portfolio and feeds the Capstone (2A to 2F). The Learning Portfolio for Unit 2 prints the reflections, the opening definition, Role Contribution to SiP and Collective Application. `collection.html` rebuilt and tested with stand-in data.
