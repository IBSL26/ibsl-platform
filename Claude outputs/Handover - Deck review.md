# Handover — Review of the unit decks against the portal files

Prepared 4 October 2026 for a new chat. Read this first, then `STANDARDS.md` in the portal folder. Older handovers with the full history: `Claude outputs\Handover - Unit decks.md` and `Claude outputs\Handover - Deck enrichment.md` (sections 8 to 12).

## 1. The job in the new chat

Carol is reviewing the 12 facilitator PowerPoint decks and verifying each one against that unit's facilitator and participant files. She will raise what she finds, deck by deck. The new chat's job is to check each point against the files, fix it properly, and hand back a deck that is ready to upload.

The decks are in `C:\Users\Carol\ibsl-platform\Unit decks\`. The portal files are in `C:\Users\Carol\ibsl-platform\`.

## 2. Who and how to work with her

- Carol (Dr Carol Hachandi Lupiya, IBSL). She calls Claude "partner" and treats Claude as the tech party: make technical decisions yourself.
- She is not technical. Every task she must do herself is explained in grade 5 terms, one small step at a time, with exact text to paste.
- **Claude never runs git, not even read-only.** Give her PowerShell commands.
- No change to a file without her approval. Back up before editing. Give SQL for her to run herself.
- She reviews text in chat before a build. When she says "fix", fix every instance of the same kind and report it.
- British spelling. Tight, functional copy. No contrast constructions ("not X, it is Y", "rather than", "instead of", "— not …"). Never the word "lens" in visible text. "Strategy2Results®" and "S2R®" always with ®. Official unit titles only.
- Restate plainly and briefly when she says she is lost. Do not force wording to fit an idea. Think about coherence and flow before answering; she will ask "are you feeling lazy to think?" when an answer is patched together.

## 3. What she taught us in the last session (deck rules)

1. **No part number twice in slide titles.** She rejected two slides both titled "1.2 · …".
2. **No unnumbered content slide between numbered ones.** Removing the number from the second slide confused her more.
3. **A principle (or any item of a numbered set) never stands alone.** If a part teaches five principles, the overview slide carries the part number and every principle gets its own slide, in the order of the original content. A slide showing only "Principle 2" made her ask whether slides were lost.
4. Where a part needs two slides for two different ideas, letter them: 1.3a, 1.3b.
5. Exercise slides in Section 5 are titled by step: "Step 1 · …", "Steps 2–4 · …".
6. **Check the flow against the original content before proposing a fix.** The answer to the Principle 2 question was in the manuscript's own structure.
7. Notes are only ever added to, never deleted.

Only Unit 5 has been corrected to rules 1 to 5 so far. See section 7.

## 4. Unit file map

| Unit | Module | Deck (in `Unit decks\`) | Participant file | Facilitator file | lens_id |
|---|---|---|---|---|---|
| 1 | 1 | Unit 01 - Behavioural Strategy Fundamentals.pptx | unit1_P.html | unit1_F.html | u1_foundations |
| 2 | 2 | Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx | unit2_m1_lens1_p.html | unit2_m1_lens1_f.html | u2m1_lens1 |
| 3 | 2 | Unit 03 - SiP KISS Mapping & OKR Definition.pptx | unit2_m1_lens2_p.html | unit2_m1_lens2_f.html | u2m1_lens2 |
| 4 | 2 | Unit 04 - Direction Integrity (ABCV-MBT).pptx | unit2_m1_lens3_p.html | unit2_m1_lens3_f.html | u2m1_lens3 |
| 5 | 3 | Unit 05 - Aligning Heart & Mind.pptx | unit3_m1_lens4_p.html | unit3_m1_lens4_f.html | u3m1_lens4 |
| 6 | 3 | Unit 06 - Performance Management Setup.pptx | unit3_m1_lens5_p.html | unit3_m1_lens5_f.html | u3m1_lens5 |
| 7 | 3 | Unit 07 - Establishing Performance Expectations.pptx | unit3_m1_lens6_p.html | unit3_m1_lens6_f.html | u3m1_lens6 |
| 8 | 3 | Unit 08 - Performance Measurement.pptx | unit3_m2_lens7_p.html | unit3_m2_lens7_f.html | u3m2_lens7 |
| 9 | 3 | Unit 09 - Strategic Unclogging.pptx | unit3_m2_lens8_p.html | unit3_m2_lens8_f.html | u3m2_lens8 |
| 10 | 4 | Unit 10 - ESRG Alignment.pptx | unit4_m1_lens9_p.html | unit4_m1_lens9_f.html | u4m1_lens9 |
| 11 | 4 | Unit 11 - Culture Reinforcement & Organisational Health.pptx | unit4_m1_lens10_p.html | unit4_m1_lens10_f.html | u4m1_lens10 |
| 12 | 4 | Unit 12 - Sustaining Performance.pptx | unit4_m2_lens11_p.html | unit4_m2_lens11_f.html | u4m2_lens11 |

Much portal content sits in JavaScript data arrays inside the HTML (role cards, bias families, cases), not only in visible HTML. Check both.

## 5. State of the decks (checked on Carol's computer, 4 October 2026)

All 12 decks were last written on 2 October 2026 and have not changed since. Every deck passes the pptx validator, has no text under 24pt, and `node check_standards.js` says "No breaches found".

| Unit | Slides | Words of notes | Slides with source detail | Slides with journal insights |
|---|---|---|---|---|
| 1 | 40 | 18,303 | 18 | 16 |
| 2 | 31 | 15,247 | 16 | 14 |
| 3 | 29 | 12,237 | 19 | 12 |
| 4 | 18 | 8,332 | 14 | 5 |
| 5 | 33 | 19,233 | 21 | 10 |
| 6 | 28 | 15,213 | 25 | 9 |
| 7 | 22 | 10,450 | 18 | 10 |
| 8 | 23 | 10,770 | 16 | 13 |
| 9 | 25 | 9,733 | 18 | 14 |
| 10 | 25 | 17,770 | 22 | 12 |
| 11 | 23 | 8,827 | 15 | 14 |
| 12 | 20 | 18,844 | 15 | 11 |

### How the presenter notes on a slide are built (three layers, in this order)

1. **Portal notes.** Heading, FACILITATOR GUIDANCE blocks from the facilitator file, "Content:" from the facilitator file, and participant prompts from the participant file. Built by `unitNN.js` from `outlines\uNN.json`. Unit 1's are hand-written inside `unit01.js`.
2. **"Source detail (S2R® manuscript):"** Content from Carol's original manuscript (`S2R_Final_Version.docx`, all 12 units) that the portal notes did not already carry, with her writing rules applied. Held in `source\uNN.json`.
3. **"Professional insights:"** Entries from Carol's journal, each with its source line. Held in `enrich\uNN.json`.

Slide text comes only from the portal files. The manuscript feeds notes only.

## 6. Head start for the review: part numbers on slides against the portal

Portal part numbers are the `acc-t` titles ("1.1 — …"). The participant and facilitator files have identical part numbers in all 12 units.

| Unit | Portal parts with no slide carrying their number | Slide numbers that are not portal parts | Part numbers repeated on slides |
|---|---|---|---|
| 1 | none | 4.2, 4.3, 4.4 | 2.1, 2.3, 2.4, 3.1, 4.1, 5.2, 6.1 |
| 2 | none | none | 1.1, 4.2, 4.3 |
| 3 | 5.1, 5.2 | none | 1.4, 4.1 |
| 4 | none | none | none |
| 5 | none | none | none |
| 6 | 5.2 to 5.7 | none | 1.1 |
| 7 | 5.1 to 5.7 | none | none |
| 8 | none | none | 1.3 |
| 9 | 5.1 | none | none |
| 10 | 3.1 to 3.4, 4.4, 4.5 | none | none |
| 11 | 2.1, 2.2 | none | none |
| 12 | none | none | none |

Reading the table:

- "No slide carrying their number" does not prove the content is missing. Most are Section 5 exercise slides titled by task or step, and some parts are covered on a slide titled another way. Each one still needs a look: is the content there, and should the title carry the number?
- Unit 1's slides numbered 4.2, 4.3 and 4.4 have no matching portal part. Check what they cover and how the portal numbers that content.
- The repeated numbers (14 places in Units 1, 2, 3, 6 and 8) break rule 1 in section 3. Carol was asked twice whether to fix them and has not answered. Raise it once at the start of the review; do not fix without her word.

## 7. Open items

- **Rules 1 to 5 in the other 11 decks.** Only Unit 5 is corrected. The others also need the "set never stands alone" check: look for a slide that details one item of a set while the other items have no slide.
- **Unit 5, six observed results.** The manuscript lists six results of fragmented effort; the portal files and slide 8 carry three (Chinese Whispers, Clarification Debt, Silent Disengagement). All six are in the notes of slide 8. Carol declined to add the other three to the files and the slide.
- **Manuscript and deck disagree** (all labelled in the notes, portal version is the one to run): Unit 4 "Cause of Death" is a card game in the manuscript; Unit 12 scenarios and commitment questions differ; Unit 12 manuscript says "Leadership Drift" where the deck says "Execution Regression"; Unit 3 manuscript says two Key Results per objective, deck says 2–3; Unit 2 manuscript has no assessment rows for areas 16–18.
- **Not confirmed by Carol:** that the Unit 5 pages show correctly on the live site (she pushed on 2 October; the first push carried the unit files); that the commit for all 12 decks and the Supabase upload of all four modules were done. Ask before assuming.
- **Sessions feature (Teams link, calendar invite, recordings):** built and handed over; the live test (one real email arriving, Secrets names) is still unconfirmed.
- **Phone layout:** unit pages are slightly wider than a phone screen. This was there before the Unit 5 work. Raise with Carol before changing.
- The folder `Claude outputs\Unit 5 deck upload` is superseded by `Claude outputs\Deck upload`.

## 8. How to verify a deck against its files

For each unit, compare in this order:

1. **Cover and top bar:** module, unit number, official title.
2. **Key learning outcomes slide:** word for word against the `klo` items in both files.
3. **Section dividers:** label "Section N · Name — Anchor", heading, and the two section outcomes against the `slo-box` of each section.
4. **Each part:** slide title number and name against the `acc-t`; slide text against the part's content (cards, lists, data arrays); the order of slides against the order of parts.
5. **Sets:** every numbered or lettered set in a part (principles, steps, forces, checkpoints) is either all on one slide or one slide each.
6. **Notes:** guidance blocks match the facilitator file; timings match; participant prompts match the participant file's reflection and working-paper questions; Section 5 steps and timings match.
7. **Unit Summary slide:** against the facilitator Unit Summary and the participant `SUMMARY` array.
8. Scan slide text and notes for "lens", contrast constructions, US spelling and missing ®.

Reading a deck on Carol's computer (python-pptx is installed in the device shell):

```
python3 - <<'EOF'
from pptx import Presentation
p = Presentation("Unit decks/Unit 05 - Aligning Heart & Mind.pptx")
for i, s in enumerate(p.slides, 1):
    texts = [sh.text_frame.text for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
    print(i, "|", " | ".join(texts)[:160])
    # print(s.notes_slide.notes_text_frame.text)   # the notes
EOF
```

## 9. Where to make each kind of fix

| What is wrong | File to change (all under `Unit decks\_build\` unless stated) |
|---|---|
| Slide title, slide text, slide order, a slide added or removed | `unitNN.js` |
| Portal notes wrong because the portal file is wrong | the unit's HTML file in the portal folder, then re-extract the outline |
| Portal notes wrong but the portal file is right | `unitNN.js` (how it picks content) or re-extract `outlines\uNN.json` |
| Source detail (manuscript) wording or placement | `source\uNN.json` |
| Journal insight wording or placement | `enrich\uNN.json` |

`source\uNN.json` and `enrich\uNN.json` are keyed by **slide number**, each with a `_check` of the slide's opening text. When slides are added, removed or moved, renumber the keys and update `_check`, or the scripts stop with "Slide N does not match".

### Build order after any change

1. `python3 extract.py <base> outlines/uNN` only when a portal file changed (it expects the two HTML files under `src\`; base is the file name without `_p.html`, for example `unit3_m1_lens4`).
2. `node unitNN.js "<out.pptx>" <logo.png> outlines/uNN.json <F.html> <P.html>` builds the deck with layer 1 notes. Watch for "OVERFLOW?" and "WORD SPLIT?" warnings and look at those slides.
3. `python3 source_notes.py "<deck.pptx>" source/uNN.json` adds layer 2. Safe to re-run in any order.
4. `python3 enrich.py "<deck.pptx>" enrich/uNN.json` adds layer 3.
5. Validate with the pptx skill's `scripts/office/validate.py`; render with `soffice --headless --convert-to pdf` then `pdftoppm` and look at every changed slide.
6. `python3 reader_assets.py "<out_dir>" "<deck.pptx>"` builds `Module-<m>/unit-<NN>/` (slide pictures and `manifest.json`, which holds the notes the portal reader shows).
7. Copy the deck to `Claude outputs\Deck upload\Module-<m>\unit-<NN>.pptx` and the folder beside it.
8. `node check_standards.js` in the portal folder must say "No breaches found".

A notes-only fix needs steps 3 to 8 only, applied to the existing deck. A rebuilt deck (step 2) loses layers 2 and 3 until steps 3 and 4 are run again.

Tools: Carol's computer shell (device shell) has node, python-pptx, soffice, pdftoppm and the Carlito and Caladea fonts, so steps 3 to 8 run there in place. Step 2 needs `pptxgenjs react react-dom react-icons sharp`, which are in the cloud workspace (`NODE_PATH` set to the global npm folder); stage the kit and the unit's two HTML files there, build, and write the deck back.

## 10. Handing a corrected deck to Carol

PowerShell, one line at a time:

```
cd C:\Users\Carol\ibsl-platform
git add "Unit decks" "Claude outputs/Handover - Deck review.md"
git commit -m "Unit NN deck: review corrections"; git push
```

Add the unit's HTML files and `collection.html` to the `git add` line when a portal file changed. Rebuild `collection.html` with `node build_collection.js` when a participant file's `SUMMARY` array or prompts changed.

Supabase, for each module that changed: Storage → `facilitator_decks` → open `Module-N` → tick the changed unit's file and folder → Delete → drag `unit-NN.pptx` and the folder `unit-NN` from `Claude outputs\Deck upload\Module-N` into the window. Delete first; the dashboard does not overwrite.

## 11. Things that cost time last session

- **A deck open in PowerPoint is locked.** Writing to it fails with "open and locked in another application". Carol reviews with the deck open, so ask her to close it before saving, and check for a `~$` file beside it.
- The device shell cannot reach the live site, and the cloud workspace cannot either. Carol has to look at the live portal herself.
- Device shell heredocs over about 20 KB fail (E2BIG). Write long files in the cloud workspace and commit them.
- Slide pictures differ byte for byte on every render even when the slide is unchanged. Compare slides by their XML, not by picture checksum.
- `dashboard_F.html` has mixed line endings. Edit it in binary mode with exact byte strings.
- Portal HTML files are CRLF and UTF-8. Keep both. After any portal edit: counts of ids, onclick, href and lens_id against the backup, `<div>` balance, `node --check` on every inline script, a browser run with a mocked database, a phone screenshot.
- Backups made in the device shell's home folder disappear when the session ends. Git history is the lasting copy.

## 12. To start the new chat

Connect the folder `C:\Users\Carol\ibsl-platform`, then say: "Read `Claude outputs\Handover - Deck review.md` and `STANDARDS.md`. I am reviewing the Unit N deck against its facilitator and participant files." Then give the first finding.

## 13. Unit 1 review — state at the end of 4 October 2026

**The Unit 1 deck master is Carol's own edited deck:** `Claude outputs\Deck upload\Module-1\unit-01.pptx` (38 slides). She rebuilt it in PowerPoint. The copy in `Unit decks\` and `_build\unit01.js` are the old 40-slide deck and no longer match. **Never rebuild Unit 1 from the kit.** Deck fixes are made directly in her deck with python-pptx (text runs only), after a backup into `Claude outputs\Unit 1 deck backups\`.

For Unit 1 the direction of the review was: the deck leads, the portal files follow.

Records of the review: `Claude outputs\Unit 1 - Review notes.docx` (her 16 notebook notes) and `Claude outputs\Unit 1 - Proposed text.docx` (changes C1 to C15, decisions D1 to D8). Carol answered "yes to all".

**Done in `unit1_P.html` and `unit1_F.html` (backups in `Claude outputs\Unit 1 file backups\`):**

- Section 1: "Why strategies fail in delivery" (60–90%, Direction, Influence, Grounding). F guidance carries the five causes. The "one assumption" opening and closing question is removed from F; the closing question is now "What has shifted in your understanding of how you think and make decisions as a leader?"
- P section learning outcomes say "your". Section 2 second outcome is new in both files.
- 2.1: new question ("…what will shape how people respond and act?"), three cards How we think / How we decide / How we behave, S2R® definition, F guidance rewritten.
- 2.2 and 2.4: F guidance rewritten from the slide notes. 2.4 adds the definition of cognitive bias in both files.
- 2.3: functional bias definition and closing line; F debrief questions from the slide notes.
- 3.1: White Space paragraph as open text; three-point check in the deck wording.
- 4.1: both files carry the slide-notes wording of the four phases; P now has the titled Scanner Questions and the same phase tab sub-lines as F.
- 4.2 is now "4.2 — The Emotional Dimension of Strategy" with 4.2.1, 4.2.2 (a: five factors, b: seven signals) and 4.2.3, in both files, with the newer climate and principle wording. No ids were changed; `r_m4_climate` sits in 4.2.1 and `r_m4_principles` in 4.2.3.
- 5.2 tabs read 5.2.1 and 5.2.2.
- Section 6: Distortion Lab rewritten (Round 1 — The Functional View, The Enterprise Task; 5-minute break-out).
- P `SUMMARY` arc 1 updated; `collection.html` rebuilt.
- `node check_standards.js`: no breaches. Counts of id, href, lens_id, textarea, saveRef unchanged; one more `tSA` onclick in P (the new 4.2.2 drop-down). Browser run with a mocked database: no script errors.

**Done in the deck:** 2.1a / 2.1b, MyHealth, "your" in the outcomes, "team members", "lens" replaced (perspective / focus), "programme", notes of slide 20 renumbered.

**Open for Unit 1:**

- Seven "rather than / instead of" sentences in the slide notes (slides 5, 13 ×2, 18, 22, 24 ×2). Rewordings were shown to Carol; apply only on her yes.
- Slides 24, 34 and 36 hold text far under 24pt (down to 11pt) and render with overlapping text in the deck-reader pictures (LibreOffice). Slides 14, 19, 26 and 32 have 20pt text. Carol to decide how these slides are reworked.
- The deck-reader folder `Deck upload\Module-1\unit-01\` still holds the old 40 pictures. Regenerate it with `reader_assets.py` once the deck is final. The device shell cannot delete files: build into the shell's home folder, copy the new files over the old ones, and move the two spare pictures (s39, s40) into a `_to_delete` folder for Carol.
- Carol has not yet committed the Unit 1 portal files or uploaded the deck.
- SEET: added to Section 1 of both files on Carol's instruction ("The Executive Leadership Perspective Simulation", before "Why strategies fail in delivery"; P in direct address, F in the slide 4 wording, plus one F guidance paragraph).
- Carol's instruction: "Remove times from the slides." Five "Time:" lines are in the notes of slides 1, 3, 4, 7 and 34. Not yet removed: the deck was open in PowerPoint. The step durations inside the Distortion Lab running order (slide 34) and the Challenge Clock (slide 29) are instructions, left in unless Carol says otherwise. The F file keeps its "Suggested time" lines.
- Phone layout is as before (pages wider than a phone screen); the new blocks stack correctly.
- Lesson from 4 October: `device_commit_files` wrote the earlier content when the same staged path was used a second time. Use a new staged folder for every commit and check the md5 on Carol's computer afterwards.
