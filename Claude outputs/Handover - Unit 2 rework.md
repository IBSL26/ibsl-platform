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
