# Handover — Unit 4 · Direction Integrity (ABCV-MBT): three-way match and clean-up

Written 7 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms. She calls Claude "partner"; Claude is the "tech party" and makes the technical decisions.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only).
3. `Claude outputs\Handover - Unit 3.md`, sections 16 and 17 only (the final state of Unit 3: this is the model for Unit 4).
4. `Unit decks\_build\rebuild_u03\README.md` (how the Unit 3 pages are built and tested; reuse the method and the scripts).
5. `Claude outputs\Unit 3 - Three-way match (findings).md` (the format of a findings report she has already accepted).

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`).

## 1. The task

Carol's words: "handover notes to a new chat for unit 4 threeway match and cleanup".

- **Three-way match:** the participant file, the facilitator file and the deck must say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, prompts, cases and activities.
- **Clean-up:** bring Unit 4 to the standard Units 2 and 3 now hold (section 3 below), and remove everything that breaks her rules (section 2).
- **Order that worked for Unit 3:** read-only scan of the three files, one findings report with proposed text in the chat, her decisions, then pages, then deck, then slide pictures, then one final scan, then her commit.

## 2. Working rules that stay in force

- **Claude never runs git in the repository folder, not even to look.** Carol commits in PowerShell. Give her the lines one at a time, each in its own code block, starting with `cd C:\Users\Carol\ibsl-platform`, with what she should see after each. Database changes go to her as SQL for Supabase.
- Back up before editing: `Claude outputs\Unit 4 file backups\` and `Claude outputs\Unit 4 deck backups\` (create them). Edits are surgical. Do not change IDs, `lens_id`, links, lock logic or database calls unless required.
- Keep each unit file's encoding and line endings exactly as found. The two Unit 4 files are UTF-8 with LF line endings today (Unit 3's were CRLF). Check before writing.
- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of"). Never "lens" in visible text. "Strategy2Results®" and "S2R®" always with ®. "SiP", never "SIP". The four SiP areas are "SiP domains".
- No times anywhere. No pre-work. Nothing on pages or in notes says that anything is automated.
- Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. Online delivery: "post in the chat".
- Participant file speaks to "you / your / your group". Facilitator file speaks of "participants / the group", is preparation only (no entry boxes) and gives precise, numbered PARTICIPANT ACTIVITY instructions.
- Learning outcomes: "Key learning outcomes" for the unit; two outcomes per section, led by action verbs, faithful to what the section teaches, aligned to the unit outcomes. They name no tool and no step.
- Slide text is 24pt or larger (Rule 16). Once Carol edits a deck, her file is the master. Check for a `~$` lock file before saving a deck.
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`. PREVIEW html files are never committed or uploaded.
- Do not spawn subagents.

**How to work with Carol (lessons of Unit 3; these cost her tokens when ignored)**

- Her instruction is final. When she says "everywhere", change the pages, the deck, the notes and the slide pictures in the same round. Do not keep an alternative and flag it for her.
- When a rule is set for one unit and the same case exists in another unit, apply it there in the same round and report it.
- Send one short "what I understand" message, then do the work. Short replies. No repeated explanations.
- She reviews wording in the chat before a build. Give previews as HTML files and pictures.
- When she asks for commit lines, give the complete current block and the Supabase steps.

## 3. The standard Units 2 and 3 now hold (apply to Unit 4)

- **Group work is Capstone work.** The page says so ("Into your Capstone"), the group confirms its outputs, the confirmed outputs feed the team's Capstone Blueprint through `PULL` in `capstone_P.html`, and the group work is left out of the Learning Portfolio through `CAPSTONE_KEYS` in `build_collection.js` (then `node build_collection.js` rebuilds `collection.html`). The facilitator report in `dashboard_F.html` still shows everything.
- **Group-work rule:** the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page.
- **Individual exercises and games are Portfolio work.** Sub-line "… · Portfolio Work"; a "Portfolio work · How to complete …" numbered box above the exercise; a "Portfolio work · Save and submit" row under it with **Save to Portfolio** (confirmation line) and **Go to Submit to Facilitator** (takes the participant to the unit's Submit button). See `pfSave` / `pfGoSubmit` in `rebuild_u03\u3_p.js` and `.u3-pf` in `u3.css`.
- **One Submit to Facilitator per unit** (each submit sends a snapshot of the whole unit).
- **Worked examples are read-only on both pages.**
- **Step tools:** each step shows what the earlier steps produced; one record above the steps; Confirm and Print below.
- **Deck:** one slide per part; section slides carry the two outcomes; a reflections slide per section that has reflections; notes structured as HEADING, HOW TO TEACH IT, numbered steps with Say / Ask, then ON THE PORTAL, AFTER THE TEACHING. Model: `Claude outputs\Unit 2 deck - notes as Carol approved them (format model).txt` and her final Unit 3 deck.
- **Deck reader:** after every deck change remake `Claude outputs\Deck upload\Module-2\unit-04\` (`s01.jpg` … and `manifest.json`) with `Unit decks\_build\reader_assets.py`, and keep `Deck upload\Module-2\unit-04.pptx` identical to the copy in `Unit decks\`. She uploads both to Supabase (Storage, `facilitator_decks`, `Module-2`).

## 4. Unit 4: the files

| What | Where | State on 7 October |
|---|---|---|
| Participant file | `unit2_m1_lens3_p.html` | last changed 29 September; lens `u2m1_lens3` |
| Facilitator file | `unit2_m1_lens3_f.html` | last changed 29 September |
| Deck | `Unit decks\Unit 04 - Direction Integrity (ABCV-MBT).pptx` | 18 slides, built by Claude on 2 October from `Unit decks\_build\unit04.js`; Carol has not reviewed it |
| Deck for upload | `Claude outputs\Deck upload\Module-2\unit-04.pptx` + folder `unit-04` | identical to the deck above; 18 pictures and manifest |
| Capstone | `capstone_P.html` | Blueprint boxes 4A to 4F exist; `PULL` has `u2` and `u3` only |
| Report labels | `dashboard_F.html`, `u2m1_lens3` | labels for `ref1`–`ref5`, `mbt_*`, `syn_*`, `own_*` |

Response keys on the participant page: `ref1`–`ref5`, `mbt_arena`, `mbt_bound`, `mbt_comp`, `mbt_value`, `syn_themes`, `syn_disagree`, `syn_top5`, `own_internal`, `own_external`, `own_timeline`.

## 5. First scan of Unit 4 (read-only; nothing was changed; the full line-by-line match is still to do)

**Structure, same on both pages:** 1.1 The Problem with Well-Written OKRs · 1.2 The Four ABCV Integrity Checkpoints · 2.1 The Industry Illusion & the Arena Shift · 2.2 Naming the Must-Be-Trues · 3.1 The Executive Hot Zone: Role-Based Blind Spots · Section 4 ABCV–MBT Working Papers (shared case: Meridian Health Group; Step 1 individual working paper, Steps 2 to 4 collective) · Section 5 Cause of Death — Match the Breakdown (four cases; answer key on the facilitator file only) · Unit Summary.

**Section outcomes:** two per section, identical on both pages. Compare them with the deck's section slides.

**Found so far**

1. Facilitator file: 17 time references ("Suggested time: 10–12 minutes", "Suggested section time", "Pacing: Step 1 … takes 15–20 minutes", "the final five minutes"). They break the no-times rule. Check the deck notes for the same.
2. Neither page says which work is Capstone work and which is Portfolio work. "Capstone" and "Portfolio" do not appear on either page.
3. Section 4 looks like group work (candidate for Capstone work): `mbt_*` → 4A to 4D, `own_*` → 4E; 4F (executive blind spots) has no obvious source key. There is no confirm step, no `PULL` rows for Unit 4 and no `CAPSTONE_KEYS` entry. Propose the mapping to Carol; do not assume it.
4. Section 5 "Cause of Death" looks like an individual exercise (candidate for Portfolio work, like the Unit 3 matching exercise). Check whether its answers are saved at all: no save key for it was found in the quick scan.
5. Unit 3 now ends with confirmed Enterprise OKRs (`ent_okrs`, lens `u2m1_lens2`). Unit 4 Step 1 asks for "up to three objectives". Check whether Unit 4 should bring the group's Unit 3 OKRs in, the way Unit 3 brings in the Unit 2 SiP statements (`sipBring` in `u3_p.js`).
6. The deck has 18 slides and about 8,350 words of notes; the Unit 2 and Unit 3 decks are much deeper. It has no reflection slides, while the participant page has `ref1`–`ref5`. Slide 14 packs the four Working Paper steps into one slide with 1,500 words of notes. Smallest slide text is 24pt.
7. "Dimension" appears five times for the three Arena dimensions (functional, emotional, social) and once in a Section 3 outcome ("dimensions of strategic integrity"). The four SiP areas are "domains"; check each use against that rule.
8. The participant page is built differently from the facilitator page (a quick search found six section panels on the facilitator file and none of the same kind on the participant file). Read its structure before planning edits.
9. The pages do not mention Unit 2 or Unit 3 by name. Check every reference to OKRs, SiP and KISS against the final Unit 2 and Unit 3 wording (five steps; SiP domains; Strategy Intent Statement).

`node check_standards.js` on 7 October: 228 lines, all Rule 16, all in the Unit 01 deck (82) and Carol's own Unit 03 slides (146). None for Unit 4.

## 6. Tools already on her computer

- `Unit decks\_build\rebuild_u03\`: `build_p.py`, `build_f.py` (pages rebuilt from the original files by exact replacements with checks), `u3_shared.js`, `u3_p.js`, `u3_f.js`, `u3.css`, `make_previews.py` + `mock-s2r.js` (stand-alone PREVIEW pages), `edit_deck.py` (surgical text edits in a deck with python-pptx), `final_scan.py <deck> <participant> <facilitator>` (the final three-way comparison). Copy the method into `rebuild_u04`.
- `Unit decks\_build\reader_assets.py`: slide pictures and `manifest.json` for the deck reader.
- `build_collection.js` (Learning Portfolio page) and `check_standards.js` in the repository root.
- The cloud workspace of a new chat starts empty. Stage what a step needs, build and test there (Playwright with the stand-in save), and write the results back. Carol's decks use Georgia and Aptos: for clean pictures install Gelasio and Carlito and alias Georgia → Gelasio, Aptos / Calibri → Carlito, Cambria → Caladea.
- Pictures written to her folder gain a small metadata block, so their checksum differs from the cloud copy. The picture is identical.

## 7. State of Units 2 and 3

Carol reported "Done" on 7 October after the final commit lines and the Supabase steps for Units 2 and 3. Claude cannot check git. Both units are closed unless she reopens them.

Seen and left alone, for her word only: her Unit 2 deck has two slides labelled "4.1c" (28 and 29); her Unit 3 slides 16–21, 27 and 30 have text below 24pt; `Claude outputs\Deck upload\Module-2\Unit 03.pptx` (capital U) is her older copy; `Claude outputs\_to_delete\` holds old pictures she can delete.

## 8. Questions for Carol, in one pass after the full scan

1. Is Section 4 (ABCV–MBT Working Papers) Capstone work, with the mapping to Blueprint boxes 4A to 4F proposed in the findings?
2. Is Section 5 (Cause of Death) Portfolio work?
3. Should Unit 4 bring in the group's confirmed Unit 3 Enterprise OKRs as the objectives to test?
4. Does she want to review the 18-slide deck first, or have Claude rebuild its notes to the Unit 2 / Unit 3 model after the pages are settled?

## 9. STATE AT THE END OF 7 OCTOBER 2026 (night) — this replaces sections 1, 4, 5 and 8 above

Carol stopped the three-way match and asked for a content rebuild. Her brief is word for word in `Claude outputs\Unit 4 - Proposed content (for review).md`, with her four rounds of review. Read that file and `Unit decks\_build\rebuild_u04\README.md` before touching Unit 4.

**What Unit 4 is now**
- Section 1: overview (flow from Unit 3 to Unit 4), then 1.1 Arena, 1.2 Boundaries, 1.3 Competition, 1.4 Value Proposition, then Bringing ABCV Together. Arena is read at three depths: Functional, Experiential, Consequential.
- Section 2: 2.1 The Industry Illusion (Familiarity, Exclusion, Complacency); 2.2 the Industry Illusion game (Apex University), portfolio work.
- Section 3: as it stood.
- Section 4: Capstone work. 4.1 one worked Key Result across four steps; 4.2 the group takes each Unit 3 Key Result through the same four steps. Every step question and every Must-Be-True question names the Key Result word for word. There is no Step 5.
- Section 5: Cause of Death. Each scenario: find the illusion, then the ABCV checkpoint where it sits. Portfolio work.

**Rules set in this round (they change section 3 above)**
- No "Portfolio work · Save and submit" row in any unit. The exercises save as the participant works. Submit to Facilitator sits once, at the end of the unit. The row was removed from Unit 3 and Unit 4 on 7 October.
- When Carol's question already states what must happen, do it. Do not answer with options.
- Questions applied to a Key Result name that Key Result word for word.

**Files written on 7 October (Carol commits and pushes herself)**
- Pages: `unit2_m1_lens3_p.html`, `unit2_m1_lens3_f.html` (Unit 4); `unit2_m1_lens2_p.html`, `unit2_m1_lens2_f.html` (Unit 3, row removed).
- Links: `dashboard_F.html` (report headings and labels), `capstone_P.html` (`PULL.u4`, boxes 4A to 4D; 4A reads functional, experiential and consequential), `build_collection.js` and `collection.html` (Unit 4 group work left out of the Learning Portfolio).
- Deck: `Unit decks\Unit 04 - Direction Integrity (ABCV-MBT).pptx`, 38 slides, identical to `Claude outputs\Deck upload\Module-2\unit-04.pptx`; reader folder `unit-04` holds `s01.jpg` to `s38.jpg` and `manifest.json`.
- Checks: `check_standards.js` no breaches on the two pages and the deck; `rebuild_u04\final_scan.py` 0 problems; page tests clean.
- Backups: `Claude outputs\Unit 4 file backups\` and `Claude outputs\Unit 4 deck backups\`; Unit 3 pages in `Unit 3 file backups\... - before portfolio row removed (7 Oct).html`.

**Commit lines given to Carol** (pages first, then the deck): `git add` of the four unit pages, `capstone_P.html`, `dashboard_F.html`, `collection.html`, `build_collection.js`, `"Unit decks"`, `"Claude outputs/Unit 4 - Proposed content (for review).md"`, `"Claude outputs/Handover - Unit 4.md"`; then Supabase: Storage, `facilitator_decks`, `Module-2`: replace `unit-04.pptx` and the whole folder `unit-04` (38 pictures and the manifest). Claude cannot see git: ask Carol whether both pushes are done.

**Seen, not changed (facts for Carol, no decision asked)**
- Her lesson game file `Claude outputs\Deck upload\Module-2\industry_illusion_unit 4 game.html` is not inside the facilitator page. The facilitator page carries the lesson game as six step panels in 2.2, and the deck notes of 2.2a send the facilitator there. Her file's Arena screen still says Functional, Emotional, Social.
- Section 3 (as it stood) still says "functional, emotional, social" on the CTO card.
- Capstone boxes 4E and 4F are written by the team; the unit no longer produces verification ownership.
- Section outcomes are the ones on the pages on 7 October; Section 2 (second) and Section 4 (second) no longer match their sections exactly. Carol rejected Claude's rewording once; change only on her wording.
