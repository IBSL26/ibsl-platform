# Transfer notes — Unit 2 rework (Strategy Visioning & Success in Practice (SiP))

Prepared 5 October 2026 for a new chat. Read this first, then `STANDARDS.md`. The longer history is in `Claude outputs\Handover - Deck review.md` (sections 2 and 3 for how Carol works, 13 to 15 for how Unit 1 went, 17 and 18 for the detail of what is summarised here).

## 1. Where Unit 2 stands in one paragraph

On 5 October the participant file, the facilitator file and the deck of Unit 2 were all changed on Carol's computer and agree with each other. **Nothing of Unit 2 is committed, pushed or uploaded to Supabase.** The live portal still shows the old Unit 2. Carol has not yet reviewed the result; she called Unit 2 "a big rework" and asked for these notes, so expect her to come back with her own changes, possibly a deck she has reworked in PowerPoint.

## 2. Working with Carol (short form)

- She calls Claude "partner". Claude is the tech party: make technical decisions, do not ask her to make them.
- She is not technical. Anything she must do herself is given in grade 5 steps with the exact text to paste.
- **Claude never runs git, not even to look.** She commits in PowerShell.
- No change to a file without her approval. Find and propose everything in one pass. Back up before editing.
- British spelling. Tight, functional copy. No contrast constructions ("not X, it is Y", "rather than", "instead of"). Never "lens" in visible text. "Strategy2Results®" and "S2R®" always with ®.
- She reviews in the actual PowerPoint (View → Notes Page). She likes findings as a Word document with a code per item, and answers "yes to all" or lists codes.
- She could not find a file saved only in the folder. Send review documents into the chat as well.

## 3. Rules she set, to apply to every unit

1. **Participant file speaks to the reader: "you / your". Never "their", "each CXO", "the executive team uses".** It carries a short version written for the participant. Never paste facilitator notes into it. Exercises run by the facilitator appear in the participant file as debrief only.
2. **Journal insights sit inside the presenter notes, at the point they deepen.** No "Professional insights" block at the end. Pattern: a short title line, the insight, then "Source: Journal, <date> — Professional Insights: <category>". No "Use this with …" pointer sentences.
3. New insights must add a new point: no repeat of what the notes already say, no entry that another deck already uses. Only Strategy, Leadership and Culture professional insights; no Integration notes, DIG axioms, spiritual insights or quotes; Bible reference removed, business point kept.
4. Each section ends with a "Section N Reflections" slide showing screenshots of that section's reflection boxes from the participant page, with the part number in a gold circle.
5. No part number twice in slide titles: letter them (1.1a, 1.1b). No "Time:" line in slide notes. A numbered set never has one item alone on a slide.
6. Notes are only added to. The exceptions she approved: Claude's own pointer sentences, the end-block heading, and wording corrected to match the reviewed files.
7. **D1 (Unit 2):** the Strategic Intent Statement is the same thing as the SiP Headline and Storyline. The term is "SiP statement". "Strategic intent" as a concept (the 3W1H) stays.
8. **D2 (Unit 2):** 4.3 and 5.2 / 5.4 both stay. 5.2 and 5.4 open with one line saying they refine what was done in 4.3.

## 4. The Unit 2 files and their state

| What | Where | State |
|---|---|---|
| Participant file | `unit2_m1_lens1_p.html` | 22 approved changes applied |
| Facilitator file | `unit2_m1_lens1_f.html` | 35 approved changes applied |
| Collection page | `collection.html` | rebuilt with `node build_collection.js` (Unit Summary now has five blocks) |
| Deck (the one to review and edit) | `Unit decks\Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx` | 36 slides; titles lettered; notes match the facilitator file; 55 insights inside the notes on 20 slides (25 moved, 30 new) |
| Upload copy of the deck | `Claude outputs\Deck upload\Module-2\unit-02.pptx` | identical to the deck above |
| Reader pictures and notes | `Claude outputs\Deck upload\Module-2\unit-02\` | 36 pictures + `manifest.json`, in step with the deck |
| Backups of the two files and the collection page | `Claude outputs\Unit 2 file backups\` | state before 5 October |
| Backups of the deck | `Claude outputs\Unit 2 deck backups\` | 31 slides (original); 36 slides before titles and notes |
| Review record | `Claude outputs\Unit 2 - Review notes and proposed text.docx` | codes D1, D2, B1–B10, C1–C13, W1–W8, E1–E5 |
| Guide to the insights | `Claude outputs\Unit 2 - Insights in the notes (guide for review).docx` | the 30 new insights and the line each follows |
| Pictures | `Claude outputs\Unit 2 deck - new reflection slides.png`, `… - corrected slide titles.png` | |

`node check_standards.js` reports only the 82 known rule 16 lines of the Unit 01 deck (Carol's own small text; her decision).

## 5. Tools built for Unit 2 (all under `Unit decks\_build\`)

| Script | What it does |
|---|---|
| `edits\apply_u02_review.py <folder> [--write]` | The 57 exact replacements in the two HTML files. A model for the next unit: every edit must match once or nothing is written; CRLF kept. |
| `deck_text_edits.py <in> <edits.json> <out>` | Exact corrections to slide titles and notes. Unit 2 list: `edits\u02_deck_text.json`. |
| `embed_insights.py <in> <spec.json> <out> [report.json]` | Places insights inside the notes. Handles insights already in the notes (`find`) and new ones (`text`, `source`). Stops if any other line of the notes would change. Unit 2 spec: `enrich\u02_embedded.json`. |
| `add_reflection_slides.py <in> reflections/u02/spec.json <out>` | Adds the "Section N Reflections" slides. Run once per deck. Pictures in `reflections\u02\`. |
| `reader_assets.py <out_dir> <deck>` | Pictures and manifest for the portal reader. It deletes old pictures, which the device shell refuses: run it into a scratch folder and copy the files over the old ones. |

**The Unit 2 deck is now edited directly with python-pptx. Never rebuild it with `unit02.js`, and never run `source_notes.py` or `enrich.py` on it:** their specs are keyed to the old 31-slide numbering and `enrich.py` deletes text.

## 6. If Carol brings her own reworked deck (as she did for Unit 1)

1. Her deck is the master. Back it up into `Claude outputs\Unit 2 deck backups\` before touching it. Check for a `~$` lock file; ask her to close PowerPoint before any save.
2. Compare it with the current deck, slide by slide (titles, slide text, notes), so that her changes are listed and none is lost.
3. Direction of work: **the deck leads, the two portal files follow.** The facilitator file takes the full wording; the participant file takes a short "you" version.
4. Type up her notebook notes, check each against the deck and both files, and give her one coded review document. Edit only after her yes.
5. Insights already sit inside her notes. Add or move with `embed_insights.py` (it never deletes her lines). Check anchors against her new wording first; the script names any anchor it cannot find.
6. If a reflection prompt changes in the participant file, retake that picture (section 7) and replace it on the reflection slide.
7. If her slides use Aptos or Georgia, render the reader pictures from a copy with those typefaces swapped for Carlito and Caladea (the deck itself untouched).
8. Then re-sync: deck → `Deck upload\Module-2\unit-02.pptx` → reader folder and manifest → `node build_collection.js` if the Unit Summary or prompts changed → `node check_standards.js`.

## 7. How the checks and pictures were made

- **Reading the two files side by side:** `extract.load()` from `extract.py` gives the visible text per section and part. The card content sits in script arrays (CONCEPTS, W1H, ENGINE, ARCH, DIMS, FLAMS, CXO, ASSESS, SUMMARY): cut each array out, evaluate it with node, compare field by field.
- **After any HTML edit:** counts of `id=`, `onclick`, `href`, `u2m1_lens1`, `<textarea`, `saveRef(`, `saveApp(` against the backup; `<div>` / `</div>` balance; `node --check` on every inline script; CRLF only.
- **Browser run and screenshots:** Playwright with Chromium in the cloud workspace. Stage the HTML plus `style.css`, `s2r-save.js`, `supabase.umd.js`, `logo.png`. Block network requests. Add CSS that hides `#p-lock-overlay`, shows every `.mod-panel`, opens every `.acc-b` and `.sub-acc-b`, and sets the font to Carlito. Reflection pictures: 860px viewport, scale 3, clip from the top of `.ref-head` to the bottom of `.ref-prompt`.
- The facilitator page logs "supabase is not defined" in this test because it loads Supabase from the internet. The untouched original does the same. It is not a fault of the edits.
- Phone width: the unit pages are wider than a phone screen. This was there before any of this work; raise it with Carol before changing it.

## 8. Open items for Unit 2

1. **Carol's review.** She has not said "Done". Offer stands: pictures of every changed part of the two pages (so the old Unit 2 stays live until she approves), or commit first and review on the live portal. She has not chosen.
2. **Capstone.** `capstone_P.html` line 158 still lists Blueprint item 2A "Strategic Intent Statement — State what [Case] pursues, why, how and by when, in a single agreed statement." This conflicts with D1. Not touched (it is tied to the database blueprint). Needs her word.
3. **September journal.** She attached nine journals (January to August, October). September was missing, so no new September insights. The journals stay out of the folder; a new chat needs them attached again.
4. **Manuscript lines reworded for D1** in the notes of slides 4, 13, 21 and 36. Slide 36 is the one she should read closely.
5. **Left as they are:** the unnumbered question slides 5, 10 and 33; the faint 3.2 answer box on slide 20 (faint on the portal page itself; offered to raise the contrast and retake); slide 1 subtitle "Building a shared Strategic Intent and a Success in Practice narrative".
6. **Unit 1.** She was given the commit line and the Supabase steps for the notes change. Ask once whether both were done and whether the live reader shows the insight "Same evidence, different conclusions." inside the notes of slide 10.

## 9. When Carol says "Done" for Unit 2

PowerShell, one line at a time (close the deck in PowerPoint first):

```
cd C:\Users\Carol\ibsl-platform
git add "Unit decks" unit2_m1_lens1_p.html unit2_m1_lens1_f.html collection.html "Claude outputs/Handover - Deck review.md" "Claude outputs/Handover - Unit 2 rework.md"
git commit -m "Unit 2: files aligned, SiP statement wording, deck with reflection slides and insights inside the notes"; git push
```

Supabase: Storage → `facilitator_decks` → open `Module-2` → tick `unit-02.pptx` and the folder `unit-02` → Delete → drag `unit-02.pptx` and the folder `unit-02` from `Claude outputs\Deck upload\Module-2` into the window. Delete first; Supabase does not overwrite.

Then ask her to open Unit 2 on the live portal as a participant and as a facilitator, and the deck reader.

## 10. Traps met in this chat

- The link to Carol's computer can drop for a minute in the middle of a job. Check the state on her computer before continuing; do not assume the last step ran.
- The device shell cannot delete. Move a stray file into `Claude outputs\_to_delete\` and tell her.
- Only files inside the connected folder can be brought into the cloud workspace. Files in the device shell's own scratch space cannot.
- Files written from the cloud workspace to her computer: text files arrive byte for byte; pictures are re-encoded (same pixels, different checksum). Use a new folder for every transfer.
- Device shell heredocs over about 20 KB fail. Write long scripts in the cloud workspace and transfer them.
- With python-pptx, read slide text from the XML. Asking a shape for `text_frame` adds an empty text body to shapes that have none and so changes the slide.
- Work on a copy in the device shell's scratch space, verify, then copy over the real file.

## 11. After Unit 2: Units 3 and 4 (rest of Module 2)

Same four steps Carol asked for on Unit 2: (1) check that the two files match in content flow; (2) check the wording of each file; (3) add reflection slides; (4) insights inside the notes, with new ones from the journals. Decks: `Unit 03 - SiP KISS Mapping & OKR Definition.pptx`, `Unit 04 - Direction Integrity (ABCV-MBT).pptx`. Files: `unit2_m1_lens2_p/_f.html`, `unit2_m1_lens3_p/_f.html`. Units 3 and 4 name things defined in Unit 2: use "SiP statement" there as well and check each mention of "Strategic Intent Statement".

## 12. To start the new chat

Connect the folder `C:\Users\Carol\ibsl-platform`, then say: "Read `Claude outputs\Handover - Unit 2 rework.md` and `STANDARDS.md`. We are continuing the Unit 2 rework." Attach the reworked deck if there is one, the notebook pages, and the journals if new insights are wanted.

## 13. REBUILD on 5 October, afternoon (read this before sections 1 to 9: it replaces them where they differ)

Carol attached "Unit 2 Rebuild _2026_10_05.docx" and said: build the facilitator and participant files first, the deck after. Follow the existing structure (collapsible, interactive), reframed for each file. When asked about parts absent from her document she answered "I gave instructions please follow": anything her document does not carry is removed.

**Her decisions:** name = "Strategy Intent Statement" (this reverses D1 of section 3: the statement is again its own output, separate from the SiP). Section 2 keeps only the three functions. The Strategy Maturity Assessment and Corrective Actions left Unit 2. The four SiP areas are "domains"; "dimensions" means WHAT, WHY, HOW, WHEN.

**State:** `unit2_m1_lens1_f.html` and `unit2_m1_lens1_p.html` are rebuilt and on her computer. `dashboard_F.html` has new report labels for Unit 2. `collection.html` is rebuilt. `node check_standards.js`: only the 82 known Unit 01 deck lines. **Nothing committed. The deck is NOT yet rebuilt and still follows the old unit.** She has not yet answered the review notes.

**New Unit 2:** 1.1 Define the Strategy Architecture · 1.2 Defining the Strategy Intent Statement · 1.3 SiP: From Intent to Future Reality · 2.1 Role of Strategy Intent & SiP (2.1.1 to 2.1.3) · 3.1 SiP Observable Indicators · 3.2 SiP Flammables · 4.1 Step 1 Build the Strategy Architecture (14 elements) · 4.2 Step 2 Derive the Strategy Intent Statement · 4.3 Step 3 Build Success in Practice · Integration Synthesis · 5.1 Role Contribution to SiP · 5.2 SiP Statement Collective Application · Portfolio Artefact · Unit Summary.

**Where things are:**
- Review notes with codes (A1 to A13 her wording adjusted, B1 to B19 choices made, C1 to C3 needs her word): `Claude outputs\Unit 2 rebuild - Review notes.docx`. She answers "yes to all" or lists codes.
- Both pages with every part and tab open: `Claude outputs\Unit 2 rebuild - Participant page (all parts open).pdf` and `… Facilitator page (all parts open).pdf`. Remake them with `page_pdfs.py` after any change to the files.
- Backups before the rebuild: `Claude outputs\Unit 2 file backups\… - before rebuild (5 Oct afternoon).html` (both files, collection, dashboard_F).
- Scripts and the list of response keys: `Unit decks\_build\rebuild_u02\` (see its README). The build scripts are a record; later edits are exact replacements in the two files.

**Open, needs Carol:** C1 Capstone Blueprint Unit 2 boxes (2A name, 2B depends on the removed assessment, 2G and 2H Headline and Storyline removed, no box for Strategy Architecture; `capstone_P.html` untouched). C2 whether a cohort is inside Unit 2 on the live portal. C3 the deck.

**Next:** apply her answer to the codes (exact replacements, then re-run `node build_collection.js`, `node check_standards.js`, remake the PDFs). Then rebuild the deck from the two files: slide titles and text, presenter notes from the facilitator file, new reflection pictures (ref1, ref2, ref6, ref4 and the four Flammable boxes, ref7, app_ref_final), journal insights inside the notes. Many of the 55 insights sit on slides whose parts no longer exist: re-place or drop each one with her.

**Commit line when she says "Done" (replaces section 9):**

```
git add "Unit decks" unit2_m1_lens1_p.html unit2_m1_lens1_f.html dashboard_F.html collection.html "Claude outputs/Handover - Deck review.md" "Claude outputs/Handover - Unit 2 rework.md"
git commit -m "Unit 2 rebuilt: Strategy Architecture, Strategy Intent Statement, Success in Practice"; git push
```

Do not give her the Supabase deck steps until the deck is rebuilt.

## 14. Section 4 rebuilt from Carol's S2R Strategy Architect tool (5 October, later the same afternoon)

After section 13, Carol attached her Impactis tool `S2R_Strategy_Architect_v15_Professional_Reports.html`, a "Strategy Intent Design" PDF from it, and two Word files of Impactis test inputs, and said "see what you can get from this". She then asked for HTML files, not PDFs, to review.

**What changed in the two files:** Section 4 now follows the tool ("Define Strategy" mode). The 14 elements are hers, in her order: ITERATIVE, THINKING & LOGIC, PROCESS, WHAT, WHY, HOW, WHEN, CREATES VALUE, DELIVERS VALUE, SUSTAINS VALUE, STAKEHOLDERS, NAVIGATING, THE FORCES, OPERATING ENVIRONMENT (OUTPUT is the result; the reading in section 13 and review code B4 of version 1 was wrong). Each element: tag, guide, four questions, "Generate what this is saying", "Is this what you mean?", confirm or refine. Then the Strategy Architecture output (five headings), the Strategy Intent Statement (derived draft), Success in Practice (three questions per domain, generated statement, confirm), and four printed outputs in her v15 layout with IBSL green and gold. Stages unlock in order. The facilitator file lists the elements and the SiP questions as collapsible preparation views.

**Where the code is:** `Unit decks\_build\rebuild_u02\u2_tool.js` (the tool), `sec4_p.py` (fixed wording), `common.py` (her elements and questions). The README there lists every response key and the deliberate differences from her tool.

**For her review:** `Claude outputs\PREVIEW - Unit 2 Participant.html` and `PREVIEW - Unit 2 Facilitator.html` open by double-click (no sign-in; the participant copy saves in the browser only). Remake them with `make_previews.py` after any change. **Never commit or upload the PREVIEW files.** The PDFs of section 13 are outdated and sit in `Claude outputs\_to_delete\`. Review notes are now version 2 (codes A, B, T, D, F, C).

**Tested:** the whole flow with her Impactis inputs in a headless browser; the Architecture and the four SiP statements match her PDF word for word; reload restores everything. `dashboard_F.html` was re-patched from the pre-rebuild backup with labels for all new keys; `collection.html` rebuilt; standards check clean apart from the 82 Unit 01 deck lines.

**Open, needs Carol (review notes part 5):** C1 Capstone boxes, C2 cohort in Unit 2, C3 the deck, C4 a tenth concept card in 1.1 for OPERATING ENVIRONMENT, C5 whether to correct the six tool defects (F1 to F6) in her Impactis file. The commit line in section 13 still applies.

**Trap:** the link to her computer dropped mid-transfer in this chat and a commit completed without its result coming back. Check checksums on her computer before repeating a transfer.

## 15. Carol's review of the participant preview (5 October, evening): six changes, applied to both files

She reviewed only the participant file and said: "These are the only changes." Applied and matched in the facilitator file:

1. **3.2 SiP Flammables is teaching content only.** The participant question box ("Does this pattern appear in your organisation?") is gone. Each pattern now has a fuller "What It Creates", three "Indicators" and a fuller "Strategic Risk if Not Balanced" (wording in `common.py`, `FLAMS`; my wording, she has not yet read it).
2. **No automation of the Strategy Intent Statement.** The group sees its WHAT, WHY, HOW, WHEN answers, deduces the statement and writes it in. **Do not put any automation back, and do not mention on the pages that automation exists: she said the automation is for consulting clients and this is for Claude to know only.**
3. **No automation of the SiP.** Per domain: three questions, then one statement written by the group, then confirm. The four confirmed statements show together, numbered. Keys `sip_d1_st` … `sip_d4_st`; `sip_integrated` is no longer used.
4. **Integration Synthesis part removed** from both files (repetition). Printing stays: Architecture, Intent, SiP and the full Strategy Intent Design report, from 4.1, 4.2 and 4.3. Her closing guidance for Section 4 now ends the 4.3 facilitator guidance. The Section 4 reflection (`ref7`) went with it.
5. **5.1 group SiP statements** are pulled from 4.3 (already the case; her screenshot showed the empty state).
6. **Portfolio Artefact removed** from the participant file (`port1` to `port3` no longer written).

Step 1 (14 elements, "Generate what this is saying", confirm or refine, Architecture output) is unchanged: she did not object to it.

**Deployment (she asked Claude to think about it; proposal given in chat, nothing built):** the unit page saves per participant, and Section 4 is group work. The Capstone already has shared team records (`capstone_team`, `get_my_capstone`, `capstone_save_section`). Proposal: one scribe per group works on a shared screen in the Teams breakout; the group's agreed outputs go into the team's Capstone Blueprint (which needs boxes for the three outputs: open item C1); a later build can let the unit page read the team's statements. Also raised: the hard locks stop a non-scribe member from entering the group's statements, and 56 answers in 30 to 35 minutes needs pre-work. Wait for her answer before building any of it.

## 16. Carol's decisions on how the unit is used, and three more changes (5 October, late evening)

Her words: "Group work each member will type on their portal what the scribe has typed. We are not locking 4.2 since they are typing it manually, remove all times. Where are you seeing Team's capstone? There is no prework before session. Work is done in session or after session."

**Settled, do not reopen:**

- **Group work:** the group agrees each entry, one member acts as scribe, and every member then types the agreed entries into their own portal page, in the session or after it. No shared-team mechanism is needed. The Capstone-sharing proposal in section 15 is withdrawn.
- **No pre-work before a session.** Work is done in the session or after it. Never write pre-work into either file or the deck.
- **No times in the facilitator file.** All removed (every "Suggested time", "Suggested section time", the minutes in the Section 4 and 5 lists, "Allow 3–4 minutes"). `build_f.py` now fails if a time is left. Carry this into the deck notes: no timings.

**Changed in the two files:**

1. **4.2 has no lock.** The Strategy Intent Statement box is open from the start. The four cards (WHAT, WHY, HOW, WHEN) fill as the elements are answered in 4.1.
2. **4.3 has no lock either.** Claude extended her 4.2 reasoning (typed by hand) to 4.3 and told her; put the lock back only if she asks (`renderSip()` in `u2_tool.js`).
3. The **Strategy Architecture output** still waits for 14 of 14 confirmed elements, because it is built from them.
4. **"Working as a group" box** added to 4.1 of the participant file; the facilitator activity notes for 4.1, 4.2 and 4.3 say the same and no longer speak of unlocking.

**Checked:** both files rebuilt and tested (typing in 4.2 and 4.3 before 4.1 is finished saves and survives a reload; full flow with the Impactis inputs still passes); `collection.html` rebuilt; standards check clean apart from the 82 Unit 01 deck lines; PREVIEW files and review notes (version 4: B15, T4, T5, T9) remade; build scripts in `Unit decks\_build\rebuild_u02\` updated. Backups: `Claude outputs\Unit 2 file backups\… - before lock and times change (5 Oct evening).html`.

**Her question "Where are you seeing Team's capstone?":** it is the portal's existing Capstone feature (page `capstone_P.html`, "Strategy2Results® Blueprint Showcase"; admin dashboard menu "Capstone" → "Capstone Teams"; participant home page "CAPSTONE" card). Nothing in it was touched. Open item C1 stands on its own: its Unit 2 boxes (2A to 2H) still name items that left the unit.

**Rule slip, told to Carol:** one device command in this chat included a read-only `git log` on `capstone_P.html`. No lock file was left and the index was untouched. The rule stands: Claude never runs git, not even to look.

**Still open with Carol:** "yes" on the two files (she has not yet read the new 3.2 wording); C1 to C5. Then the deck.

## 17. Carol's yes on the two files, the Section 2 title, and the Capstone aligned with Unit 2 (5 October, night)

Her words: "Yes partner. You were right on the capstone. We must align it with the new flow of the SIP. So that what we have there the strategy architecture, Strategy Intent Statement, the SIP Statement. Remove the headlines. We will be building the capstone as we build the units. Let us change the title from Why Strategy Intent Must Precede Success Definition to just the importance and relevance of SIP. … let us bring your suggestion back for capstone page. So they complete in the unit then the approved three go into the capstone right?" (She then confirmed she saw 4.2 and 4.3 unlocked.)

**Settled:**

- **The two Unit 2 files are approved** ("Yes partner"). Next step is the deck (section 13 commit line still applies, now with `capstone_P.html` added).
- **Section 2 title:** "The Importance and Relevance of SiP" in both files.
- **Capstone is built unit by unit.** Each time a unit is rebuilt, its Blueprint section is aligned in the same pass. Only Unit 2 is aligned so far; sections 3 to 12 are untouched.
- **Flow:** participants complete and confirm in the unit; the three confirmed outputs go into the team's Capstone Blueprint.

**What was built in `capstone_P.html`:**

1. Unit 2 boxes: 2A Strategy Architecture · 2B Strategy Intent Statement · 2C SiP · Customer Experience & Value · 2D SiP · Operational Capability & Execution Rhythm · 2E SiP · People & Culture Dynamics · 2F SiP · Enterprise Value Creation. Removed: maturity gaps and corrective actions, SiP Headline, SiP Storyline. The instruction line under each box is Claude's wording (review notes K2); she has not yet read it.
2. Bring-in. The section still opens when every team member has completed Unit 2. On the first opening of an empty draft by a member whose page has all six texts confirmed, the page reads that member's own `lens_responses` (`u2m1_lens1`: `arch_output`, `intent_statement`, `sip_d1_st` … `sip_d4_st`, checked against `confirmed_items`), fills the boxes and saves the team draft. A button "Bring in from my Unit 2 page" repeats it on demand (asks before replacing different text; names any output not yet confirmed). Boxes stay editable in Draft. Send, confirm and request-a-change are unchanged.
3. `PULL` in the page lists what each section brings in; add a row set per unit as units are rebuilt.

**Database step Carol must run (not yet run):** `Claude outputs\capstone_unit2_boxes.sql`, Block 1 (function `capstone_section_box_count`: Unit 2 from 8 to 6). Run it on the day the new page goes live; without it "Send for team confirmation" answers "Complete every box". Block 2 is a check for any team text already saved in the old Unit 2 boxes (old 2A held the intent, old 2B the maturity gaps); if above 0, handle before go-live. `capstone_blueprint.sql` (the record) now shows 6 in Block 12.

**Also changed:** one paragraph on the Capstone in 4.3 of each unit file. `collection.html` rebuilt. Standards check clean apart from the 82 Unit 01 deck lines. Review notes are version 5 (B3, K1 to K7; C1 closed). `PREVIEW - Capstone.html` added (sample team, sample text). Backups: `Claude outputs\Unit 2 file backups\… (5 Oct night)`.

**Tested** against a stand-in database (`mock-supabase-capstone.js`): full set brought in and saved; sent for confirmation; one output unconfirmed; draft with other text; section locked; nothing on the unit page; database still expecting 8 boxes. The real database functions were not run from here.

**Commit line when the deck is done:** `git add "Unit decks" unit2_m1_lens1_p.html unit2_m1_lens1_f.html capstone_P.html dashboard_F.html collection.html "Claude outputs/Handover - Deck review.md" "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/capstone_blueprint.sql" "Claude outputs/capstone_unit2_boxes.sql"` (Carol runs it; Claude never runs git). Never add the PREVIEW files.

**Still open with Carol:** K2 wording; C2 to C5; the deck (the old deck was open in PowerPoint on 5 October: it must be closed before the new one is written).

## 18. Go-live before the deck (5 October, night)

Carol: "Can we close this already - One step for you later and let us commit the new unit file to the portal then we do the PPT." Claude gave her, in this order: (1) Block 1 of `capstone_unit2_boxes.sql` to paste into the Supabase SQL editor, then the Block 2 check; (2) the PowerShell lines below. The deck folder is left out of this commit because the old deck was still open in PowerPoint (its lock file would be picked up) and the new deck is not built yet.

```
cd C:\Users\Carol\ibsl-platform
git add unit2_m1_lens1_p.html unit2_m1_lens1_f.html capstone_P.html dashboard_F.html collection.html "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/capstone_blueprint.sql" "Claude outputs/capstone_unit2_boxes.sql"
git commit -m "Unit 2 rebuilt: Strategy Architecture, Strategy Intent Statement, Success in Practice; Capstone Unit 2 section aligned"; git push
```

Until she confirms both steps ran, treat the live portal as still on the old Unit 2. The portal keeps serving the old Unit 2 deck until the new one is built and uploaded. `Unit decks\_build\rebuild_u02\` goes in with the deck commit.

## 19. The Unit 2 deck is rebuilt (5 October, night) — waiting for Carol's review in PowerPoint

Carol said "Done" to section 18 (the database step and the commit of the unit files and `capstone_P.html` both ran; the live portal now carries the new Unit 2). She then asked for the deck: "Please ensure that you beef up the presenter notes properly."

**The deck:** `Unit decks\Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx`, 48 slides, about 24,600 words of presenter notes (the old deck had 36 slides and about 15,200). No text under 24pt. The pptx validator passes. `node check_standards.js`: only the 82 known Unit 01 deck lines. The same file is at `Claude outputs\Deck upload\Module-2\unit-02.pptx`, and `Deck upload\Module-2\unit-02\` holds 48 pictures and the new `manifest.json` (made with `reader_assets.py` into a scratch folder, then copied over). Backups of the old deck and old build inputs: `Claude outputs\Unit 2 deck backups\`.

**Slide map:** 1 cover · 2 Key learning outcomes · 3 The unit journey · 4 Section 1 · 5 Opening the session · 6 1.1a definition · 7 1.1b nine concepts · 8 1.2 · 9 1.3 · 10 Section 1 Reflections · 11 Section 2 · 12 2.1 overview · 13–15 2.1.1 to 2.1.3 · 16 Section 2 Reflections · 17 Section 3 · 18 3.1a overview · 19–22 3.1b to 3.1e (one SiP domain each) · 23 3.2a overview · 24–27 3.2b to 3.2e (one Flammable each) · 28 Section 3 Reflections · 29 Section 4 · 30 4.1a how the group works · 31 4.1b how each element works · 32 4.1c the 14 elements · 33–36 4.1d to 4.1g (elements 1–3, 4–7, 8–11, 12–14) · 37 4.1h Architecture output · 38 4.1i six checks · 39 4.2 · 40–42 4.3a to 4.3c · 43 Section 5 · 44 5.1a · 45 5.1b · 46 5.2 · 47 Section 5 Reflections · 48 Unit Summary. Section 4 has no reflection slide because the unit has no Section 4 reflection.

**How the notes are built (every content slide):**
1. FACILITATOR GUIDANCE and PARTICIPANT ACTIVITY blocks, word for word from the facilitator file (read through `outlines\u02.json`, so they cannot drift), the card content from the files' data arrays, and the participant prompts.
2. "Source detail (S2R® manuscript)" and "Further detail / Probing question (S2R® manuscript)": the manuscript wording kept from the old deck where it still applies. The open-response questions of the old maturity assessment are reused as one probing question for each of the 14 elements in 4.1. Manuscript lines were adapted to her new terms ("domains", "Strategy Intent"). Headline, Storyline, maturity scoring and co-creation lines were left out with the content they belonged to.
3. The 55 journal insights of the old deck, all re-placed inside the notes at the point they deepen (`enrich\u02_rebuild.json`; the build stops if one is unused or used twice). Eight had no title line and were given one. **No new insights were added: the journals were not attached in this chat.**
4. Facilitation blocks written by Claude for this deck from her material: "How to run it", "Listen for", "Questions to ask", "Watch for", "Bridge", "What a strong reflection contains", the rebalancing questions on the Flammable slides, the six verbs on 5.1b. **She has not yet read these.**
No timings anywhere. Nothing is asked of participants before the session. The notes never say that the page writes the Strategy Intent Statement or the SiP statements.

**Build (cloud workspace; needs pptxgenjs, sharp, react-icons):**
```
python3 extract.py unit2_m1_lens1 outlines/u02        (only when the two HTML files change; they sit under src\)
node unit02.js "<deck>.pptx" <logo.png> outlines/u02.json <F.html> <P.html>     (44 slides; writes reflections\u02\spec.json)
python3 shoot_reflections.py <site folder> reflections/u02                        (only when a reflection prompt changes)
python3 add_reflection_slides.py "<deck>.pptx" reflections/u02/spec.json "<final>.pptx"   (adds the four reflection slides: 48)
```
Notes live in `u02_notes.js` (helpers, front, Section 1), `u02_notes_b.js` (Sections 2 and 3), `u02_notes_c.js` (Sections 4 and 5, Unit Summary). Slide text and layout live in `unit02.js`. **Do not run `source_notes.py`, `enrich.py`, `embed_insights.py` or `deck_text_edits.py` on this deck**, and ignore `source\u02.json`, `enrich\u02.json`, `enrich\u02_embedded.json` and `edits\u02_deck_text.json`: they describe the old deck. Sections 5 and 6 of this handover (edit the old deck directly with python-pptx) no longer apply; the deck is rebuilt from the scripts above until Carol edits it herself in PowerPoint. If she does, her file becomes the master (section 6 rules).

**Review guide for Carol:** `Claude outputs\Unit 2 deck - Guide for review.docx` (codes N1 to N8, slide map with the insights per slide; made with `rebuild_u02\make_deck_guide.js`). Sent into the chat with the deck.

**Checked:** every slide rendered and looked at; an independent read of all 48 notes against the facilitator file (no guidance missing; its findings on sequence, repetition and wording were fixed); wording rules scanned (no contrast constructions, no "lens", ® present, no timings, no pre-work).

**Found, not changed (needs her word):** the facilitator page gives WHEN two wordings: the 1.2 tab says "…through which the direction will be pursued", 4.2 says "…through which the ambition will be pursued". The participant page says "ambition" in both places. One word to change in `unit2_m1_lens1_f.html` (array `W1H`, `def` of WHEN) if she agrees.

**Next, on her "Done" for the deck:** commit line `git add "Unit decks" "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/Handover - Deck review.md"` then `git commit -m "Unit 2 deck rebuilt: 48 slides, full presenter notes"; git push`; then Supabase: Storage → `facilitator_decks` → `Module-2` → tick `unit-02.pptx` and folder `unit-02` → Delete → drag both from `Claude outputs\Deck upload\Module-2`. If she edits the deck in PowerPoint, copy her file over `Deck upload\Module-2\unit-02.pptx` and remake the pictures and manifest first. Then Units 3 and 4 (they name things defined in Unit 2: check every mention of the SiP Headline, Storyline, maturity assessment and "Strategic Intent Statement").

## 20. Teaching first, portal after; the opening definition on both pages (5 October, late night)

Carol on the deck: "We need to add the define strategy in the participant file for this: Write your definition of strategy in one sentence — right now, without consulting anyone. And to the facilitator as well. The PPT is the teaching material. The logic is that the facilitator runs through the whole unit first and then allows the participants to go to the portal. So the speaking notes must not be written as if the facilitator is pointing the participants to the portal while teaching."

**Rule for every unit from now on (apply to Units 3 to 12 and their decks):** the deck is the teaching material. The facilitator teaches the whole unit from the deck first. Participants go to the portal afterwards and complete their own page, in the session or after it. Presenter notes never ask participants to open, expand, select or type on the portal while the facilitator teaches. Facilitator-page guidance follows the same rule.

**Changed (all on her computer; NOT yet committed, so the live portal still has the version of section 18):**

1. `unit2_m1_lens1_p.html`: a box at the top of Section 1, "Opening the Session — Your Definition of Strategy", her sentence word for word, saved as response key `strategy_definition` (in `U2_FIELDS`; no database change). One helper line under the box is Claude's wording ("Enter the sentence you wrote when the session opened, exactly as you wrote it. You return to it at the Unit Summary."); she has not yet read it.
2. `unit2_m1_lens1_f.html`: her sentence as a quote in Section 1 with a PARTICIPANT ACTIVITY note; one line added to Unit Intent ("How the unit runs: …"); six guidance lines reworded so that the facilitator teaches and does not steer participants through the page (1.1 "Taking participants through the 9 concepts", 1.2 "Before presenting the four dimensions" / "Taking participants through the 4 dimensions" / "HOW" / "WHEN", Unit Summary "Read each of the five summary blocks aloud", 5.1 "Each participant enters their own responses in their participant file"). Old and new wording are in the review guide, code N10.
3. `dashboard_F.html`: family 'Opening — Definition of Strategy' and the label for `strategy_definition` (two exact insertions, CRLF kept; all inline scripts parse).
4. `collection.html` rebuilt (Unit 2 now has 12 prompts).
5. The deck (48 slides, same slides, about 25,650 words of notes): every "How to run it" block is now "How to teach it" and speaks from the slide; what participants do on the portal sits under "On the portal, after the teaching" and "PARTICIPANT ACTIVITY (on the portal, after the teaching)"; coaching for Sections 4 and 5 sits under "When the groups do the work" / "When the groups share"; the Unit Summary notes end with "Handing over to the portal". `Deck upload\Module-2\unit-02.pptx`, the 48 pictures and `manifest.json` are refreshed.
6. Build scripts updated: `rebuild_u02\build_f.py`, `build_p.py`; `_build\u02_notes.js`, `u02_notes_b.js`, `u02_notes_c.js`, `outlines\u02.json`. Review guide is version 2 (`Claude outputs\Unit 2 deck - Guide for review.docx`, codes N0 to N10). Backups: `Unit 2 file backups\… (5 Oct late).html`, `Unit 2 deck backups\unit-02 - 48 slides, before teaching-first notes (5 Oct late).pptx`.

Checked: both pages verified (tag balance, scripts, no duplicate ids), the new box saves and comes back after a reload, the Section 4 flow test still passes, standards check clean apart from the 82 Unit 01 deck lines, deck validator passes, no text under 24pt, notes scanned for wording rules and for any remaining portal-pointing phrase.

**On her "Done":** one commit for everything: `git add "Unit decks" unit2_m1_lens1_p.html unit2_m1_lens1_f.html dashboard_F.html collection.html "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/Handover - Deck review.md"` then `git commit -m "Unit 2: deck rebuilt with teaching-first notes; opening definition of strategy on both pages"; git push`; then the Supabase replacement of `unit-02.pptx` and folder `unit-02` in `Module-2` (section 19). Check for a `~$` lock file before any further save of the deck.

**Still open with her:** N8 ("direction" or "ambition" in the 1.2 WHEN tab of the facilitator page), the helper line under the new box (N9), new journal insights (journals not attached), C2 to C5 of the earlier review notes.

## 21. Notes restructured on Carol's model; clear opening part on the facilitator page (5 October, late night)

Carol sent back her own copy of the deck (she had cleaned the notes of slides 1 to 4) with four instructions: (a) remove the helper line under the opening-definition box on the participant page ("unnecessary"); (b) the facilitator page needs "a clear part for where they ask participant to define strategy in their own words properly", in place of the quote box and Claude's activity note; (c) she sees no relevance in Key Facilitation Questions and Tone & Watch Points in the slide notes ("otherwise we remove it completely or reword it"); (d) "For the PPT the guidance on how to use the slide must come up before the actual content notes… Write the notes properly: start with how to run the teaching content on the slide, then notes and insights on the slide content. Right now the notes are confusing. See how I have cleaned the first 4 slides. Follow that structure."

**Rule for the notes of every deck from now on (apply to Units 3 to 12):**

1. HEADING in capitals (part number and title).
2. HOW TO TEACH IT first (HOW TO USE THIS SLIDE on reflection slides, HOW THIS SECTION RUNS on section slides): numbered steps. LISTEN FOR / QUESTIONS TO ASK follow straight after where they help.
3. Then the notes on the slide content: FACILITATOR GUIDANCE (word for word, in one piece), CONTENT, the journal insights (after the guidance block or the card they deepen, never in the middle of a guidance block), SOURCE DETAIL (S2R® MANUSCRIPT).
4. Last: ON THE PORTAL, AFTER THE TEACHING, and for group work WHEN THE GROUPS DO THE WORK.
5. Every block heading in capitals and bold; one paragraph per line. Section slides carry only: heading, how the section runs, the section learning outcomes, the guidance with SECTION INTENT, and at most one short block. No Key Facilitation Questions or Tone & Watch Points block in slide notes.
6. No repetition between the steps and the guidance, no bridges floating on their own: a bridge is the last step of HOW TO TEACH IT / HOW TO USE THIS SLIDE.

**Her deck is now the master.** The deck in `Unit decks\` is her copy (her slides; her notes on slides 1 to 4, word for word) with the notes of slides 5 to 48 replaced. One correction inside her notes: slide 3 "using the list above" → "using the list below". Her copy as she sent it is kept in `Unit 2 deck backups\unit-02 - Carol's edited copy, slides 1 to 4 notes cleaned (5 Oct).pptx`.

**How the deck is built now** (in `Unit decks\_build`, cloud needs `NODE_PATH=$(npm root -g)`):
`node unit02.js build1.pptx <logo> outlines/u02.json <F html> <P html>` → `python3 add_reflection_slides.py build1.pptx reflections/u02/spec.json build2.pptx` → `python3 format_notes.py "<current deck in Unit decks>" build2.pptx "<deck out>"` (keeps the slides and the notes of slides 1 to 4 of the current deck; replaces notes from slide 5; a line starting with § in the generated notes is a heading and becomes bold; stops if the slide text of the two decks differs) → `python3 lint_notes.py "<deck out>" 5` (contrast constructions, "lens", timings, pre-work, portal-steering, ®, leftover §) → `python3 dump_notes.py "<deck out>" notes.txt` to read the notes → `reader_assets.py` into scratch, then copy over `Claude outputs\Deck upload\Module-2\unit-02\`. In the notes scripts, `H()` marks a heading, `GB()` prints a guidance block of the facilitator page under its own label, `ctx.divider()` and `ctx.reflection()` build section and reflection pages, `weave()` keeps a guidance block whole and puts its insights after it. `carol_notes_1_4.json` holds her notes for slides 1 to 4 (reference only: the deck itself is the source).

**Changed in this round (on her computer, NOT yet committed):**

1. `unit2_m1_lens1_p.html`: helper line under the opening box removed. The box and its key `strategy_definition` are unchanged.
2. `unit2_m1_lens1_f.html`: at the top of Section 1 a guidance part "Opening the Session · Defining Strategy in Your Own Words" with Ask / Collect / Keep, and a one-line PARTICIPANT ACTIVITY note. The quote box and the earlier activity note are gone; the duplicate "Opening the session" paragraph in the Section 1 guidance is removed.
3. Deck: notes of slides 5 to 48 rewritten in the structure above (about 25,500 words; all 55 insights placed once). `Deck upload\Module-2\unit-02.pptx`, the 48 pictures and `manifest.json` refreshed.
4. `collection.html` rebuilt. Standards check: only the 82 Unit 01 deck lines.
5. Review guide is version 3 (codes N0 to N11). Previews regenerated (`PREVIEW - Unit 2 Participant.html`, `PREVIEW - Unit 2 Facilitator.html`; never commit or upload them).
6. Backups: `Unit 2 file backups\… (5 Oct, notes restructure).html`, `Unit 2 deck backups\unit-02 - 48 slides, before notes restructure (5 Oct).pptx` and `notes scripts before restructure (5 Oct)\`.

**Open with her:**
- N11a: step 4 of her slide 3 notes still says "Keep the four Key Facilitation Questions in front of you", although she deleted the block. Remove the step?
- N11b: Key Facilitation Questions and Tone & Watch Points still sit in the Facilitator Guide tab of `unit2_m1_lens1_f.html` (STANDARDS rule 4 puts them in every facilitator file). Remove, reword or leave? If she says remove for all units, the standard itself must change with her approval.
- N8: "direction" or "ambition" in the 1.2 WHEN tab of the facilitator page.
- New journal insights (journals not attached); C2 to C5 of the earlier review notes.

**On her "Done":** `git add "Unit decks" unit2_m1_lens1_p.html unit2_m1_lens1_f.html dashboard_F.html collection.html "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/Handover - Deck review.md"` then `git commit -m "Unit 2: deck notes restructured (how to teach first); opening definition of strategy on both pages"; git push`; then Supabase: Storage → `facilitator_decks` → `Module-2` → delete `unit-02.pptx` and folder `unit-02` → drag both from `Claude outputs\Deck upload\Module-2`. If she edits the deck again in PowerPoint, her file is the master: copy it over `Unit decks\` and `Deck upload\Module-2\unit-02.pptx`, and remake the pictures and manifest. Then Units 3 and 4.

## 22. Notes rewritten as one classroom conversation; deck aligned with the two files (5 October, late night)

Carol rejected the section 21 version: "After the script how is the facilitator supposed to use it? … The notes must flow as a conversation that the facilitator [has] during the class. Go through all the slides and arrange the notes properly." She asked for worked slides 6, 7 and 8 in the chat first, then approved: "the slide 6 and 7 format you gave me is what you must do". She also found the private 1-to-5 rating of 1.2 in the notes although it is no longer part of the unit: "Please align the PPT with the actual content on the facilitator and participant files … give me amended PPT with proper notes and relevant insights per notes."

**This replaces rule 3 of section 21 for every deck (Units 3 to 12 too):**

1. HEADING in capitals, then HOW TO TEACH IT (HOW TO USE THIS SLIDE on reflection slides).
2. Numbered steps in class order. Each step has a short bold title. Under it: `Say: "…"`, `Ask: "…"`, what to do, `Listen for: …`.
3. Nothing sits loose after the steps. The facilitator script, the card text (`What it means, say:` and so on), manuscript detail (`Add:`) and each journal insight (`Deepen, say:` then `(Insight: Title. Source: …)`) sit inside the step where they are used. No block headed CONTENT, FACILITATOR GUIDANCE, FACILITATOR SCRIPT or SOURCE DETAIL.
4. Spoken lines speak to participants ("you", "your group"). Guidance of the facilitator page written about "participants" or "the group" is turned into speech; the cards are spoken word for word.
5. Section slides: HOW THIS SECTION RUNS, SECTION LEARNING OUTCOMES (Carol's slide 4 model), then HOW TO OPEN THE SECTION as steps.
6. Last blocks only: ON THE PORTAL, AFTER THE TEACHING, and LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL (coaching). Every bridge is the last step.
7. The notes carry only what the facilitator and participant files carry today. Nothing that reads like an activity may be invented (no ratings, counts, private tasks, things "written down" that the page has no box for). Manuscript detail is allowed where it deepens content still on the pages. Ask her before adding any exercise.
8. Read every notes page from first line to last before sending, then have an independent reader check the notes against the two files (done here with a second agent; its findings were applied).

**Removed for alignment:** the 1.2 rating (also removed from `unit2_m1_lens1_f.html`: the guidance line "Before presenting the four dimensions: Ask participants to rate …" is gone; `build_f.py` updated), the "Critical Insight" manuscript lines, the probing questions of 4.1 (old maturity assessment), the "quick count" for the Flammables (4.3b), the private task in 3.2a, "written down with the name of the person who must decide it" (six checks), "each group applies the two tests in Section 4" (2.1.2). The three questions per Flammable are kept as facilitator questions ("questions that bring the other domains back"), with no claim that they return in Section 4.

**Insights:** all 55 placed once, each spoken inside a step. Moved: the_one_thing → 2.1.2; destination_and_route → 1.2 HOW; shared_meaning_shared_action → 2.1.1; an_honest_baseline → Section 1 reflections; values_at_the_edges → 3.1d Dialogue Quality; a_common_baseline → 3.2a; signal_to_watch_for → 3.2c; top_down_cultures → 4.1a; right_destination_right_design → close of 4.1e; seeing_the_larger_system → 5.1b.

**Tools (in `Unit decks\_build`):** `u02_notes.js`, `u02_notes_b.js`, `u02_notes_c.js` (helpers `S()` step, `page()`, `say()`, `ask()`, `IN()` insight, `pick()` takes one guidance line of the facilitator page and stops the build if the page changed, `divider()`, `reflection()`, `reflFor()`); `format_notes.py` (unchanged: Carol's deck is the base, her notes on slides 1 to 4 kept); `lint_notes.py` (now also flags removed content and loose blocks); `check_alignment.py <deck> outlines/u02.json outlines/u02_arrays.txt` (lists every sentence of the facilitator guidance and every card text that is not in the notes word for word: card text must show only the re-voiced domain intros and THE FORCES list; guidance sentences listed there are the ones turned into speech, read them).

**State (on her computer, NOT committed):** `unit2_m1_lens1_f.html` (rating line removed; md5 9699929f…), `unit2_m1_lens1_p.html` (unchanged since section 21), deck in `Unit decks\` (48 slides, about 23,600 words of notes), `Deck upload\Module-2\unit-02.pptx` + 48 pictures + `manifest.json` refreshed, facilitator PREVIEW regenerated, review guide version 4 (N0 to N14). Backups: `Unit 2 file backups\unit2_m1_lens1_f - before rating line removed (5 Oct, conversation notes).html`, `Unit 2 deck backups\unit-02 - 48 slides, before conversation-style notes (5 Oct).pptx` and `notes scripts before conversation style (5 Oct)\`.

**Open with her:** N14 (Unit Summary speaks of the group work as done although it is read before the portal work; her wording kept); N11a (step 4 of her slide 3 notes still names the Key Facilitation Questions); N11b (Key Facilitation Questions and Tone & Watch Points in the Facilitator Guide tab of the facilitator page); N8 ("direction" in the 1.2 WHEN tab, "ambition" in 4.2: both pages have both wordings).

**On her "Done":** same commit line and Supabase steps as section 21 (commit message: "Unit 2: deck notes as a classroom conversation; rating removed; opening definition of strategy on both pages").

## 23. Carol's three final decisions applied; Unit 2 ready to commit (5 October, late night)

Carol on the section 22 deck: "Otherwise the PPT notes look good. So give me the final versions and we commit the revised versions." Her three answers:

1. **Slide 3, step 4 removed** ("Keep the four Key Facilitation Questions in front of you…"). `format_notes.py` now makes this cut each time it runs on her copy (it stops if the text is no longer where it was); `carol_notes_1_4.json` updated.
2. **Facilitator Guide tab reworded** ("Reword them accordingly"), in `unit2_m1_lens1_f.html` and `build_f.py`. Key Facilitation Questions now opens with "Four questions anchor the unit. Ask each one where it belongs as you teach from the deck." and each question carries where it is used (Sections 1 and 4 · Strategy Architecture; 1.3, Section 3 and 4.3 · Success in Practice; Section 2 · Decision Filter; Section 5 · Role contribution). Tone & Watch Points now opens with "These four points apply when the groups do the work on the portal, after the teaching." and each point carries its part (4.2 · Strategy Intent Statement; 4.3 · Success in Practice; 4.3 · Balance; 5.1 · Role contribution) with a Say or Ask. The questions and watch points themselves are unchanged. She has seen this wording in the chat reply only: change it if she comments.
3. **"ambition" in the 1.2 WHEN line** on both pages (`W1H`, `def` of WHEN) and in the deck notes (slide 8). `build_f.py` and `build_p.py` updated. 1.2 and 4.2 now read the same.

N14 (Unit Summary speaks of the group work as done) was not answered: her wording stays.

**Final state on her computer (md5):** `unit2_m1_lens1_f.html` 5d5958c0…, `unit2_m1_lens1_p.html` 845ace53…, deck `Unit decks\Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx` ac09cc13… (same file as `Deck upload\Module-2\unit-02.pptx`; 48 pictures and `manifest.json` refreshed), `collection.html` rebuilt, standards check clean apart from the 82 Unit 01 deck lines, both PREVIEW files regenerated. Backups: `Unit 2 file backups\… (5 Oct, final).html`, `Unit 2 deck backups\unit-02 - 48 slides, before her three final decisions (5 Oct).pptx`. The review guide docx is version 4 and still lists N8 and N11 as open: they are closed by this section.

**Given to her for the commit (she runs it herself in PowerShell; Claude never runs git):**
`git add "Unit decks" unit2_m1_lens1_p.html unit2_m1_lens1_f.html dashboard_F.html collection.html "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/Handover - Deck review.md"` · `git commit -m "Unit 2: deck notes as a classroom conversation; rating removed; opening definition of strategy; guide tab reworded"` · `git push`. Then Supabase: Storage → `facilitator_decks` → `Module-2` → delete `unit-02.pptx` and folder `unit-02` → drag both in from `Claude outputs\Deck upload\Module-2`.

**Next:** Units 3 and 4, with the teaching-first rule (section 20) and the conversation format for notes (section 22). Check every mention of the SiP Headline, Storyline, maturity assessment and "Strategic Intent Statement", and that nothing in a deck refers to content the two files no longer carry.

## 24. Unit 2 closed (5 October, late night)

Carol: "Done." She ran the commit and push of section 23 and replaced `unit-02.pptx` and the folder `unit-02` in Supabase (`facilitator_decks` → `Module-2`). Unit 2 is live: both pages, the Capstone section and the deck. Nothing is waiting for her on Unit 2. This section itself is not yet committed: it goes with the next commit.

**Next (her words: "We will move to unit 3 tomorrow"):** Unit 3, in a new chat. Start from sections 20, 22 and 23 of this file (teaching first; notes as a classroom conversation; deck aligned with what the two files carry), and attach the journals again if new insights are wanted.

## 25. Fifth question for element 13 · THE FORCES: internal forces (6 October)

Carol noticed that 1.1 teaches five force categories while element 13 in 4.1 asked about four. Her instruction: "Add the internal forces as fifth question on the files — participant and facilitator. Do not amend PPT … just amend 4.1 to add the culture and update the report if necessary."

**Changed (on her computer, NOT yet committed):**

1. `unit2_m1_lens1_p.html` and `unit2_m1_lens1_f.html`, element 13 only. Guide: "Competitive, macro, disruptive, social and environmental, and internal forces shape strategic viability: rivals, substitutes, regulation, economics, technology, business models, ESG, demographic shifts, culture and legacy identity." Fifth question: "Which internal forces (culture, behaviour patterns, institutional habits, legacy identity) work for or against the strategy?" New response key `arch_e13_q5` (no database change). Element 13 is the only element with five questions.
2. Three wordings that said "four questions": participant 4.1 "Answer the questions of each element with actual strategic choices"; facilitator 4.1 activity "It answers the questions of the element"; facilitator element 13 heading "The five questions" (the other 13 elements keep "The four questions").
3. The report needed no code change: the tool reads every question an element has, so the fifth answer flows into "what this is saying", the Strategy Architecture output and the printed report (tested end to end with `forces_test.py` in the cloud workspace: saved, reloaded, generated, built, printed).
4. `dashboard_F.html`: label for `arch_e13_q5` added after `arch_e13_q4` (exact insertion, CRLF kept, inline scripts parse). `collection.html` rebuilt. Standards check: only the 82 Unit 01 deck lines.
5. Build scripts: `rebuild_u02\common.py` (ELEMENTS), `build_f.py`, `sec4_p.py`. Backups: `Unit 2 file backups\… before fifth forces question (6 Oct).html`. Both PREVIEW files regenerated.

**The deck was NOT touched, on her instruction.** She has reviewed the deck herself and saved her copy as `Claude outputs\Deck upload\Module-2\unit-02.pptx` on 6 October: **36 slides** (the build had 48). Her copy is the master. Things that follow from that, all waiting for her word:
- `Deck upload\Module-2\unit-02\` (48 pictures + `manifest.json`) still comes from the 48-slide build, so the portal deck reader does not match her 36-slide file until the pictures and manifest are remade from her copy (`reader_assets.py` into scratch, copy over; the 12 surplus pictures must go to `_to_delete`).
- `Unit decks\Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx` is still the 48-slide build. Her copy should replace it so that git holds the master.
- Her deck's notes for element 13 may still list four questions and say every element has four. Do not change her deck unless she asks.
- `unit02.js`, the notes scripts and `format_notes.py` no longer describe her deck (slide count differs). Do not rebuild Unit 2 from them without her say; edit her file directly if she asks for changes.

**Commit line given to her:** `git add unit2_m1_lens1_p.html unit2_m1_lens1_f.html dashboard_F.html collection.html "Unit decks" "Claude outputs/Handover - Unit 2 rework.md" "Claude outputs/Handover - Deck review.md"` · `git commit -m "Unit 2: internal forces added as fifth question of element 13"` · `git push`.

**Next:** Unit 3.

## 26. Moving to Unit 3 (6 October)

Carol moved to Unit 3 and asked for handover notes for a new chat. They are in `Claude outputs\Handover - Unit 3.md`: read that file first. It holds her instruction, the Unit 2 deck as the format model (her own 36-slide copy; notes dumped to `Unit 2 deck - notes as Carol approved them (format model).txt`), a first scan of the Unit 3 files, the questions to put to her and the Unit 2 items still open.


## 27. Reader folder and `Unit decks` copy brought in line with Carol's 36-slide deck (7 October 2026)

Carol's own Unit 2 deck (36 slides, saved 6 October 12:59, md5 a5006150…) was in `Claude outputs\Deck upload\Module-2\unit-02.pptx`, but the reader folder `unit-02` still held the 48 pictures and manifest of the earlier generated deck, and `Unit decks\` still held the 48-slide deck. On her "go":

- `Deck upload\Module-2\unit-02\` now holds `s01.jpg`-`s36.jpg` and `manifest.json`, made with `reader_assets.py` from her deck. Her PPT was not changed.
- `Unit decks\Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx` is now a copy of her 36-slide deck (same md5).
- Kept: `Unit 2 deck backups\Unit 02 - 48 slides, replaced by Carol's 36-slide deck (7 Oct).pptx` and `unit-02 manifest - 48-slide deck (7 Oct).json`. The 48 old pictures are in `Claude outputs\_to_delete\unit-02 old pictures (48-slide deck)\` for her to delete.
- Her deck is the master. `_build\unit02.js` and the `u02_notes*.js` files build the 48-slide deck and are now only a record. The slide map in section 22 describes the 48-slide deck.
- Seen in her deck, not changed: slides 28 and 29 both carry the label "4.1c"; slide 32 is "4.3c" while slide 31 is "4.3".
- Supabase (she does it): Storage, `facilitator_decks`, `Module-2`: replace `unit-02.pptx` and the whole folder `unit-02` (delete the old folder first, it holds 48 pictures).
