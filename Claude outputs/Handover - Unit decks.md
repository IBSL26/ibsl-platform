# Handover — S2R® Unit Decks (facilitator PowerPoint decks)

Prepared 29 September 2026 for a new chat; updated at the close of the deck build the same day. Read this first, then `STANDARDS.md` in the portal folder.

## 1. Who and where

- Carol (Dr Carol Hachandi Lupiya), IBSL. She calls Claude "partner" and treats Claude as the tech party: make technical decisions yourself.
- Portal folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder). Static HTML portal, Netlify auto-deploys from GitHub `IBSL26/ibsl-platform` (main).
- Decks go in `C:\Users\Carol\ibsl-platform\Unit decks\`.
- Build kit (scripts) is in `Unit decks\_build\` — see section 6.

## 2. Working rules (non-negotiable)

1. No change to any file without Carol's approval. Find and propose everything in one pass; she dislikes being handed lists of things Claude found but did not fix. When she approves a batch, fix all of it and re-check before saying "done". When she says "fix everything", that covers every instance of the same kind of problem you find, including ones outside the list you showed her; fix them and report them.
2. Claude never runs git, not even read-only. Carol commits in PowerShell. Give her the commands.
3. Preserve CRLF line endings and UTF-8 in HTML files. Back up before editing. Verify after every change (ids / onclick / href / lens_id counts, `<div>` balance, `node --check` of every inline script, a browser run).
4. Never change IDs, lens_id / data-lens-id values, links, lock logic, scoring or database calls without approval. Give SQL for Carol to run herself.
5. Run `node check_standards.js` in the portal folder before saying anything is complete. It must say "No breaches found".
6. Carol's writing rules: British spelling; tight, functional copy; no fluff; no "not X — it is Y" or other contrast constructions; no "founding cohort" language. Learning outcomes are action-verb capability statements that never name the tool or how it is delivered.
7. The word "lens" is never used in visible text: a unit is a "unit"; the four ABCV elements are "checkpoints"; a role's point of view is a "perspective". (Code names such as lens_id and file names such as unit2_m1_lens1_p.html stay as they are.)

## 3. The deck brief (agreed with Carol)

- Audience: the facilitator, delivering the unit live. One deck per unit, 12 units.
- Source: the unit's participant and facilitator HTML files. Nothing invented.
- **Minimum font size 24pt for every piece of text on a slide.** `lib2.js` throws an error if anything is smaller.
- IBSL forest green and gold, IBSL seal (`logo.png` in the portal root) on the title slide. Icons (react-icons) on content slides.
- Section labels match the portal exactly: "Section N · Name — Anchor" (Awareness — What · Intelligence — Why · Extrapolating — Where · Integration — Collective · Application — In Practice). Unit 1 adds Section 1 "Orientation — Overview".
- Official unit titles (use exactly):
  1 Behavioural Strategy Fundamentals · 2 Strategy Visioning & Success in Practice (SiP) · 3 SiP KISS Mapping & OKR Definition · 4 Direction Integrity (ABCV-MBT) · 5 Aligning Heart & Mind · 6 Performance Management Setup · 7 Establishing Performance Expectations · 8 Performance Measurement · 9 Strategic Unclogging · 10 ESRG Alignment · 11 Culture Reinforcement & Organisational Health · 12 Sustaining Performance.
- File name pattern: `Unit 01 - Behavioural Strategy Fundamentals.pptx`, `Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx`, etc. (replace characters Windows disallows, if any).

### NEW requirement (Carol, 29 Sept): detailed presenter notes

"I want the presenter notes to be detailed — get all the details from the content files."

For every slide, the speaker notes carry everything the facilitator needs to deliver that slide without opening the portal:
- The full teaching content behind the slide, from the participant file (definitions, explanations, examples, case facts, figures, all items of any framework, table or card set on that slide).
- Every FACILITATOR GUIDANCE block for that part, from the facilitator file, in full: purpose, key facilitation points, questions to ask (verbatim), expected responses, watch-points, cautions, transitions.
- The Facilitator Guide tab content (Unit Intent, Key Facilitation Questions, Tone & Watch Points) on the opening slides.
- Suggested timings per part and per section, as given in the files.
- Participant activities: what participants do, where in their file (section/part number), how long, and how to debrief.
- Section learning outcomes (two per section) on each section divider; Key learning outcomes on the outcomes slide.
- The Unit Summary synthesis on the closing slides.
- Notes are plain text organised with short labels ("Content:", "Ask:", "Watch for:", "Time:", "Transition:"). Apply Carol's writing rules to the notes too (British spelling, no "not X — it is Y", no "lens").

Slide text stays short and at 24pt or larger; the detail lives in the notes.

## 4. Unit file map

| Unit | Participant file | Facilitator file | lens_id (database) |
|---|---|---|---|
| 1 | unit1_P.html | unit1_F.html | u1_foundations |
| 2 | unit2_m1_lens1_p.html | unit2_m1_lens1_f.html | u2m1_lens1 |
| 3 | unit2_m1_lens2_p.html | unit2_m1_lens2_f.html | u2m1_lens2 |
| 4 | unit2_m1_lens3_p.html | unit2_m1_lens3_f.html | u2m1_lens3 |
| 5 | unit3_m1_lens4_p.html | unit3_m1_lens4_f.html | u3m1_lens4 |
| 6 | unit3_m1_lens5_p.html | unit3_m1_lens5_f.html | u3m1_lens5 |
| 7 | unit3_m1_lens6_p.html | unit3_m1_lens6_f.html | u3m1_lens6 |
| 8 | unit3_m2_lens7_p.html | unit3_m2_lens7_f.html | u3m2_lens7 |
| 9 | unit3_m2_lens8_p.html | unit3_m2_lens8_f.html | u3m2_lens8 |
| 10 | unit4_m1_lens9_p.html | unit4_m1_lens9_f.html | u4m1_lens9 |
| 11 | unit4_m1_lens10_p.html | unit4_m1_lens10_f.html | u4m1_lens10 |
| 12 | unit4_m2_lens11_p.html | unit4_m2_lens11_f.html | u4m2_lens11 |

Much of the content (role cards, bias families, cases, frameworks) sits in JavaScript data arrays inside the HTML files, not only in visible HTML. Extract from both. Module line on each deck's cover follows the file's top bar ("Module N · Name · Unit N").

## 5. Status (end of 29 September 2026)

- **All 12 decks are built and committed** in `Unit decks\`, with the official file names. Unit 1 was reviewed and approved by Carol; Units 2–12 follow the same pattern. Every deck passes the pptx validator, has no text under 24pt and no "lens", and every slide carries detailed presenter notes (content, facilitator guidance, questions word for word, watch-points, timings, participant activities, transitions).
- Where a unit file gives no timings, the notes say so; nothing is invented. Unit 10's complete worked Cultural Operating Code for all three value sets sits only in the speaker notes of the COC Challenge slide (the file says not to distribute it before teams finish).
- **Portal fixes made during the deck build, all committed and logged** in `Claude outputs\Rule 13 rewrites - pass 2.md`:
  - rows 479–545: further "not X — it is Y" sentences found while building;
  - rows 546–750: every "rather than" / "instead of" contrast and teaching pair removed from the unit files; Unit 2 → Unit 3 transition corrected; Unit 5 forward references now point to Unit 6 (Performance Management Setup); the Meridian Health Group case study copied into the Unit 4 facilitator file; Unit 12 force tabs renumbered to count five (Forces 1–2 Competitive + Disruptive, 3 Macro-Environmental, 4 Social + Environmental, 5 Internal);
  - row 751: Unit 3 → Unit 4 transition corrected (it now names ABCV, the subject of Unit 4).
- `check_standards.js` was widened: rule 13 now also flags "rather than", "instead of", fragments opening "Not a…/Never…", "— not…" and "… is not." pairs, in visible text and script strings (code comments ignored). It reports "No breaches found".
- `collection.html` was rebuilt with `node build_collection.js` after the participant summaries changed. Rebuild it again whenever a participant file's SUMMARY array changes.
- Left deliberately (Carol has not asked for these): short state descriptions such as "Energy is high; progress is not." and "Organisations that are not explain each shift as temporary noise". Raise them with her before changing.
- Known expected difference in the integrity check: unit1_P.html onclick count 140 → 143 (the Distortion Lab option cards Carol approved).

## 6. Build kit and QA (in `Unit decks\_build\`)

- `lib2.js` — design system: colours (forest 1A5C2C, deep 0F3B1C, gold C6A24C), fonts (Cambria headings, Calibri body), layouts: `cover`, `list`, `section`, `prompt`, `cards`, `stat`, `compare`. `T()` refuses any font under 24pt and prints "OVERFLOW?" / "WORD SPLIT?" warnings (check those slides by eye; most are false alarms).
- `extract.py` — reads a unit's F and P files and writes an outline JSON (sections, parts, content, facilitator guidance, participant prompts including textarea placeholders). Run: `python3 extract.py <base> <out>` with base such as `unit3_m2_lens8` (or `unit1`); it expects the HTML under `src/`.
- `outlines\u01.json` … `u12.json` — current outlines.
- `kit.js` — `Unit` class over an outline plus the HTML files: `sec()`, `part()`, `ppart()` (matching participant part), `guide()`, `secNotes()`, `partNotes()` (builds notes from content, guidance and participant prompts); `divider()` for section slides; `js(name)` evaluates a JavaScript data array from the HTML.
- `unit01.js` … `unit12.js` — one script per deck. Unit 1 has hand-written notes: `node unit01.js "<out.pptx>" <logo.png> <unit1_F.html>`. Units 2–12: `node unitNN.js "<out.pptx>" [logo.png] [outline.json] [F.html] [P.html]`; defaults point at the portal folder.
- Dependencies (cloud workspace): `npm i pptxgenjs react react-dom react-icons sharp`; python `beautifulsoup4`, `python-pptx`.
- QA per deck: run the pptx skill validator; convert with `soffice --headless --convert-to pdf`, then `pdftoppm -r 40 -jpeg` and look at every slide; scan notes for "lens", contrast constructions and US spelling; then `node check_standards.js` in the portal folder.
- After any change to a unit file: re-extract that unit's outline, rebuild its deck, copy it into `Unit decks\`. Unit 1's notes are hand-written in `unit01.js`, so apply the same wording change there too.

## 7. Open items for Carol

- Nothing outstanding on the decks or the portal.
