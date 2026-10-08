# Handover — Unit 5 · Aligning Heart & Mind: three-way match

Written 8 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she must do herself is explained in grade 5 terms. She calls Claude "partner"; Claude is the "tech party" and makes the technical decisions.

## 0. Read first, in this order

1. This file.
2. `STANDARDS.md` in the repository root, then run `node check_standards.js` (read-only).
3. `Claude outputs\Handover - Unit 4.md`, section 9 only (final state of Unit 4: the latest model).
4. `Unit decks\_build\rebuild_u04\README.md` (how the Unit 4 pages and deck are built, checked and tested; reuse the method and the scripts).
5. `Claude outputs\Unit 3 - Three-way match (findings).md` (the format of a findings report Carol has accepted).
6. `Claude outputs\Handover - Deck enrichment.md`, section 12 (change management was added inside Unit 5 on 2 October).

Folder on her computer: `C:\Users\Carol\ibsl-platform` (connected folder; in the device shell `$HOME/mnt/ibsl-platform`).

## 1. The task

Carol's words (8 October): "hand over notes to new chat for threeway check for unit 5".

- **Three-way match:** the participant file, the facilitator file and the deck say the same thing: same Key learning outcomes, same two outcomes per section, same section and part numbers, same titles and sub-lines, same cards, questions, cases and activities.
- **Clean-up:** bring Unit 5 to the standard Units 2 to 4 now hold (section 3), and remove what breaks her rules (section 2).
- **Order that works:** read-only scan of the three files, then ONE findings report in the chat with the proposed text, then her decisions, then pages, then deck, then slide pictures, then one final scan, then her commit.

## 2. Working rules (all still in force)

- **Claude never runs git in the repository folder, not even to look.** Carol commits in PowerShell. Give her the lines one at a time, each in its own code block, starting with `cd C:\Users\Carol\ibsl-platform`, and say what she should see after each. Name every file in `git add`; never `git add .` (her folder holds many working files that stay off the portal). Database changes go to her as SQL for Supabase.
- On 8 October her pages were not pushed because she ran only the deck lines. When giving page lines and deck lines, give them as ONE block, or say clearly that both blocks must be run.
- Back up before editing: `Claude outputs\Unit 5 file backups\` and `Claude outputs\Unit 5 deck backups\` (create them). Edits are surgical. Do not change IDs, `lens_id`, links, lock logic or database calls unless required.
- Keep encoding and line endings as found. Both Unit 5 files are UTF-8 with CRLF (checked 8 October).
- British spelling. Tight, functional copy. No contrast constructions ("not X — it is Y", "rather than", "instead of", "in place of"). Never "lens" in visible text or notes. "Strategy2Results®" and "S2R®" always with ®. "SiP", never "SIP". The four SiP areas are "SiP domains".
- No times anywhere. No pre-work. Nothing says anything is automated.
- Teaching first: the facilitator teaches the whole unit from the deck; participants go to the portal afterwards. Online delivery: "post in the chat".
- **Participant file speaks to the participant throughout** ("you / your / your group"): no facilitator cues ("Ask", "Say", "Now ask:", "Tell participants", "Facilitation move") and no third-person framing of the reader (Carol, 8 October). Role cards address the reader in the role ("As COO, you…"). Facilitator file speaks of "participants / the group", is preparation only (no entry boxes) and gives precise, numbered PARTICIPANT ACTIVITY instructions.
- Learning outcomes: "Key learning outcomes" for the unit; two outcomes per section, led by action verbs, faithful to what the section teaches. They name no tool and no step. Carol rewords them herself; propose only when asked.
- Slide text 24pt or larger (Rule 16). Once Carol edits a deck, her file is the master: later changes go into her file, and the build script is a record.
- The device shell cannot delete: move stray files to `Claude outputs\_to_delete\`. PREVIEW html files are never committed or uploaded.
- Do not spawn subagents.

**How to work with Carol (lessons; these cost her tokens when ignored)**

- Her instruction is final. A question of hers that states what must happen ("should not the submit be at the end?") IS the instruction: do it. Never answer an instruction with options.
- Do not add parts she did not write. Do not replace her wording with yours unless she asks.
- When she says "everywhere", change the pages, the deck, the notes and the slide pictures in the same round. When a rule is set for one unit and the same case exists in another, apply it there too and report it.
- Short replies. One short "what I understand" line, then the work. She reviews wording as review files (PREVIEW pages in the real format) and pictures.
- Report facts that need her word in one line each, with no menu of options.

## 3. The standard Units 2 to 4 now hold (apply to Unit 5)

- **Group work is Capstone work.** The page says so, the group confirms its outputs, the confirmed outputs feed the team's Capstone Blueprint through `PULL` in `capstone_P.html`, and the group work is left out of the Learning Portfolio through `CAPSTONE_KEYS` in `build_collection.js` (then `node build_collection.js` rebuilds `collection.html`). The facilitator report in `dashboard_F.html` shows everything, with labels in `LENS_LABELS` and headings in `FAMILY_DEFS`.
- **Group-work rule:** the group agrees each entry, one member acts as scribe, every member types the agreed entries into their own page.
- **Individual exercises and games are Portfolio work.** Sub-line "… · Portfolio Work" and a "Portfolio work · How to complete …" numbered box. **There is NO "Save to Portfolio / Go to Submit" row** (removed from Units 3 and 4 on 7 October): the exercises save as the participant works, and the how-to box ends "… reach your facilitator when you select Submit to Facilitator at the end of the unit."
- **One Submit to Facilitator per unit**, at the end.
- **Worked examples are read-only on both pages.** Group tools follow the worked example step for step, show what earlier steps produced, keep one record, and end with Confirm and Print.
- **Reflection questions** carry `class="ref-prompt"` so the Learning Portfolio prints the question above each answer.
- **Deck:** format of Carol's Unit 2, 3 and 4 decks (design system `Unit decks\_build\lib2.js`; slide types as in `unit04.js`): one slide per part; section slides carry the two outcomes; a "Section N Reflections" slide where a section has reflections (`add_reflection_slides.py`); notes as HEADING, HOW TO TEACH IT, numbered steps with Say / Ask, then ON THE PORTAL, AFTER THE TEACHING (`format_notes_u03.py`, `lint_notes.py`). Model: `Claude outputs\Unit 2 deck - notes as Carol approved them (format model).txt` and her final Unit 3 and Unit 4 decks.
- **Deck reader:** after every deck change remake the reader folder (pictures `s01.jpg` … and `manifest.json`) from the final deck, keep `Unit decks\<deck>` identical to the upload copy, and move surplus pictures to `_to_delete`. Unit 5 is Module 3: `Claude outputs\Deck upload\Module-3\unit-05.pptx` and folder `unit-05`. She uploads both to Supabase (Storage, `facilitator_decks`, `Module-3`) and deletes surplus pictures there. `reader_assets.py` hangs on bare `soffice` in the cloud workspace: convert with the pptx skill's `soffice.py`, then run its picture and manifest steps on the PDF.
- **Three-way scan:** adapt `Unit decks\_build\rebuild_u04\final_scan.py` (outcomes word for word on both pages; every slide string found on a page; no text under 24pt; notes open with a bold heading; leftovers; identical part titles and sub-lines on both pages).

## 4. Unit 5: the files (checked 8 October, read-only)

| What | Where | State |
|---|---|---|
| Participant file | `unit3_m1_lens4_p.html` | last changed 2 October; lens `u3m1_lens4`; UTF-8, CRLF |
| Facilitator file | `unit3_m1_lens4_f.html` | last changed 2 October; UTF-8, CRLF |
| Deck | `Unit decks\Unit 05 - Aligning Heart & Mind.pptx` | 33 slides (2 October, after the change-management additions); identical to `Claude outputs\Deck upload\Module-3\unit-05.pptx`; reader folder `unit-05` holds 33 pictures and the manifest |
| Older copy | `Claude outputs\Unit 5 deck upload\unit-05.pptx` | differs from the deck above; an older upload folder. Do not upload it; ask Carol only if it matters |
| Capstone | `capstone_P.html` | boxes 5A Interpretation risks, 5B Emotional climate, 5C Alignment hot zones, 5D Shared enterprise interpretation, 5E Leadership behaviour commitment; `PULL` has no `u5` row yet |
| Report labels | `dashboard_F.html`, `u3m1_lens4` | labels exist for `ref1`–`ref15`, `wp_*` and others |
| Learning Portfolio | `build_collection.js` | `CAPSTONE_KEYS` has no `u3m1_lens4` entry yet |

**Structure (the same part titles on both pages):** 1.1 The Human Terrain of Strategy Execution · 1.2 The Five Principles of Aligning Heart & Mind · 1.3 Change Management: The 4 Checks of Mind, Heart, Hands and Habit · 1.4 The 3S Check: Shift, Stake, Step · 1.5 The SCARF Model: Five Triggers of Human Resistance · 1.6 The STAT Check: Skill, Time, Authority, Tools · 1.7 ACE-IT: The Observable Behaviour Standard · 2.1 The Ignition Point of Strategy Execution · 2.2 Three Foundational Logics · 2.3 Why Change Must Be Led: Installed and Adopted · 3.1 The COMPASS Framework: Seven High Flammable Zones · 3.2 From High Flammables to Burning Platforms · 3.3 Change Readiness Across the Organisation · 4.1 The Converging Zone · 4.2 Collective Intelligence Across the Leadership Team · 4.3 Leading Change with One Voice · Section 5 (not an accordion; read its structure) · Unit Summary.

**Found in the quick look (to confirm in the full scan):**
1. Facilitator file: time references remain (for example "100 minutes", "12 minutes", "18 minutes"; about 25 matches). They break the no-times rule.
2. Neither page uses the words "Portfolio" or "Capstone". Group work and individual work are not yet marked, and there is no confirm step feeding boxes 5A to 5E.
3. The participant voice rule of 8 October has not been applied to Unit 5. Read every participant section for facilitator cues and third-person framing.
4. The change-management content (1.3, 1.4, 1.6, 2.3, 3.3, 4.3; see `Unit 5 - Change management content (draft for review).docx`) was added on 2 October. Check it against the deck word for word.
5. Unit 4 now ends with the group's ABCV–MBT record (`mbt_*`). Check whether Unit 5 refers back to Unit 4 correctly.

## 5. Tools already on her computer

- `Unit decks\_build\rebuild_u04\`: `build_p.py`, `build_f.py` (pages rebuilt from the original files by exact replacements with checks), `make_previews.py` + `mock-s2r.js` (stand-alone PREVIEW pages), `patch_links.py` (report, Capstone, Learning Portfolio), `final_scan.py`, `export_deck_data.py`. Copy the method into `rebuild_u05`.
- `Unit decks\_build\`: `lib2.js`, `kit.js`, `unit04.js` + `u04_notes.js` (deck and notes model), `add_reflection_slides.py`, `format_notes_u03.py`, `lint_notes.py`, `shoot_reflections_u04.py`, `reader_assets.py`, `enrich\u05.json` (journal insights for Unit 5).
- `build_collection.js` and `check_standards.js` in the repository root.
- The cloud workspace of a new chat starts empty. Stage what a step needs, build and test there (Playwright with the stand-in save; fonts Montserrat and Cormorant Garamond for page pictures; Carlito and Caladea for deck pictures), and write the results back.

## 6. State of Units 2, 3 and 4

- Units 2 and 3 are closed. On 7 October the "Save to Portfolio" row was removed from Unit 3.
- Unit 4 was rebuilt 7 to 8 October (see `Handover - Unit 4.md`, section 9). Pages pushed on 8 October. Carol edited the deck herself (29 slides); her file is the master. Reader folder remade from her deck.
- Open Unit 4 points for Carol's word only: her slide 16 gives the CTO blind spot as Value Proposition while the pages give Arena; her slides 5 and 6 are titled "The Problem with Well-Written OKRs" and "The Four ABCV Integrity Checkpoints" while the pages call that part "Overview — From Unit 3 to Unit 4".
- In her git list, `lens_migration_playbook.md` shows as deleted and `Handover - Deck enrichment.md` as changed. Neither comes from the unit work; leave them alone.

## 7. Final state of Unit 5 (8 October 2026, after "make the changes")

Read `Unit decks\_build\rebuild_u05\README.md` first: it is the full record (files, response keys, links, deck, tests, open points). Sections 1 and 4 above describe the unit before the work.

- **Findings:** `Claude outputs\Unit 5 - Three-way match (findings).md`. Carol answered "make the changes"; everything proposed in it was applied.
- **Pages:** `unit3_m1_lens4_p.html` and `unit3_m1_lens4_f.html` are the builds of `rebuild_u05\build_p.py` and `build_f.py` on the backups in `Claude outputs\Unit 5 file backups\`. They reproduce byte for byte.
- **Group work:** Section 5, Step 4 is Capstone work. The group confirms three entries; `syn_missing_compass` feeds Capstone box 5C through `PULL.u5`. Boxes 5A, 5B, 5D and 5E are typed by the team. Steps 1 to 3 and the 30-Day Behavioural Commitment are Portfolio work.
- **Links:** `capstone_P.html` (`PULL.u5`), `dashboard_F.html` (label for `confirmed_items`), `build_collection.js` (`CAPSTONE_KEYS.u3m1_lens4`), `collection.html` rebuilt. No database change.
- **Deck:** `Unit decks\Unit 05 - Aligning Heart & Mind.pptx`, 40 slides, identical to `Claude outputs\Deck upload\Module-3\unit-05.pptx`. Reader folder `unit-05`: 40 pictures and the manifest, no surplus. Built by `Unit decks\_build\build_u05.sh`. If Carol edits the deck, her file is the master.
- **Checks on the written files:** `final_scan.py` 40 slides, 0 problems. `node check_standards.js`: no Unit 5 breach (the 228 Rule 16 lines are the Unit 01 and Unit 03 decks, as before).
- **Backups:** `Claude outputs\Unit 5 file backups\` and `Claude outputs\Unit 5 deck backups\`.
- **PREVIEW files** in `Claude outputs` are for viewing only. Never commit or upload them.

**Waiting on Carol**

1. Commit and push: the two pages, the three link files, `collection.html`, `Unit decks`, the findings and this handover (one block of lines, given in the chat of 8 October). Claude cannot see git: ask her whether the push is done.
2. Supabase, Storage, `facilitator_decks`, `Module-3`: replace `unit-05.pptx` and the folder `unit-05` (40 pictures and `manifest.json`).

**Open, for her word only (one line each, no options)**

- Capstone boxes 5A, 5B, 5D and 5E have no feed from the unit.
- Section 5, first outcome, says "one strategic change"; the exercise maps two.
- Step 1 names the Unit 3 Start and Stop lists as the source of the two changes; the facilitator briefing keeps "Leaders use the change they carried through the unit as their first map".
- Deck only, no match on the pages: three taglines in 1.2 and the four labels of the kind "Mind · 3S · Explain".
- `Claude outputs\Unit 5 deck upload` is an older folder, superseded.

**Lessons of this round**

- `reader_assets.py` ran in the cloud workspace with bare `soffice` this time. It removes old pictures first, which the device shell cannot do: run it in the cloud and write the folder back.
- Reflection pictures: four on a slide is the limit at 24pt titles. Section 1 has seven, so it takes two slides (1.1 to 1.3, 1.4 to 1.7).
- Python leaves a `__pycache__` folder beside the build scripts; move it to `_to_delete` before the commit lines are given.
