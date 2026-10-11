# Unit 7 amendments — 11 October 2026

Unit 7 is "Establishing Performance Expectations": `unit3_m1_lens6_p.html` (participant), `unit3_m1_lens6_f.html` (facilitator), `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` (deck). Lens id `u3m1_lens6`.

Source of the changes: Carol's amendments of 11 October in three rounds (10:39, 12:20 and 12:57), in her words in `Claude outputs\Handover - Unit 7.md`, sections 9, 10 and 11.

**State on 11 October (13:30):** Carol gave her word ("Am happy for us to commit now"). The two pages, the three link files and `collection.html` are written to the portal folder (see "Written to the portal folder" at the foot). No database change is needed. The deck in `Unit decks` and the copy in `Claude outputs\Deck upload\Module-3` are identical (24 slides). Carol commits, pushes and uploads the deck to Storage.

| File | What it does |
|---|---|
| `u7_content.py` | The content in two voices (participant "you", facilitator "the leader / participants"). Lines marked NEW are Claude's wording. |
| `build_u07.py <p before> <f before> <p out> <f out>` | Builds both pages from the files before the amendments. Each cut and replacement checks that it finds its place once and stops on a miss. |
| `u7_p.js` | Participant tool: Section 5 (5.1 four steps on two Objectives, 5.2 the alignment dialogue with the board chair, drop-down lists, the record, Confirm and Print) and the Key Result list of part 4.2. Written into the participant page by the build. |
| `u7.css` | Styles added to both pages. |
| `make_previews.py <p> <f> mock-s2r.js <folder>` | Stand-alone PREVIEW copies (the participant copy saves in the browser only). Never commit or upload them. |
| `mock-s2r.js` | Stand-in save for the previews, with samples of a member's confirmed Unit 3 Enterprise OKRs and Unit 2 SiP statements. |
| `test_u07.py <preview folder> [<screenshot folder>]` | Browser checks (Playwright): 130 checks, all pass. |
| `shoot_reflections_u07.py <PREVIEW participant page> <folder>` | Pictures for the reflection slides (`ref_3.1.png`, `ref_4.1.png`, `ref_4.2.png`, `reflections.json`); kept in `Unit decks\_build\reflections\u07`. |
| `carol_deck_u07_r3.py <Carol's deck> <p page> <f page> <pictures folder> <out.pptx>` | Round 3, the script in use. Works on top of her own 24-slide deck of 12:56 (md5 1e56c277…, kept in `Backups\Unit 7 deck backups`): the 4.2 picture on "Section 4 Reflections", the Section 5 opener notes, slide 5.1, a new slide 5.2, and the Unit Summary slide leaves. Every sentence quoted from the pages is checked against the built pages. |
| `patch_links_u07.py <folder> <out>` | The three link changes (`capstone_P.html`, `dashboard_F.html`, `build_collection.js`) from the files in `Claude outputs\Backups\Unit 7 file backups\… - before Unit 7 links (11 Oct)`. Then `node build_collection.js` in the portal folder. |
| `e2e_u07.py <site folder> <fake-supabase.js> [<shots>]` | End to end on the real pages with a stand-in database (`fake-supabase.js` of `rebuild_u06`): 37 checks, all pass. |
| `final_scan_u07.py <deck> <p> <f>` | The last three-way scan of deck and pages. Reports only. |
| `carol_deck_u07.py` | Round 2 script, kept as the record of how the 25-slide deck of 12:36 was built on her 23-slide file. It no longer runs against the round 3 content. |

Input for the build: `Claude outputs\Backups\Unit 7 file backups\unit3_m1_lens6_[p|f] - before amendments (11 Oct).html` (md5 2d913573… and 460f7395…). Run from this folder:

```
python3 build_u07.py "<backup p>" "<backup f>" out_p.html out_f.html
python3 make_previews.py out_p.html out_f.html mock-s2r.js "<Review files>"
python3 shoot_reflections_u07.py "<Review files>/PREVIEW - Unit 7 Participant.html" ../reflections/u07
python3 carol_deck_u07_r3.py "<Carol's 24-slide deck of 12:56>" out_p.html out_f.html ../reflections/u07 "<out.pptx>"
```

## The unit as the review files show it

- **Section outcomes:** Section 1 in Carol's words. Section 2 unchanged. Section 3 second, Section 4 second and both Section 5 outcomes reworded by Claude to the content (`SLO_EDITS`).
- **Section 1:** 1.1 opens with the manuscript lines from Unit 6 and carries the fuller six-row table · 1.2 the fuller three conditions · 1.3 definition, examples and key question for each chain · **1.4 The Alignment Dialogue now carries all the teaching of the dialogue**: its introduction, Score → Evaluate → Resolve, the GROW coaching model, and the reflection "Practise the Resolve Question" (`ref8`).
- **Section 2:** 2.1 six rows on both pages · 2.2 and 2.3 in the fuller wording.
- **Section 3:** 3.1 each role card gives the typical tendency, the expectation gap, the likely Expectations Chain and a question.
- **Section 4:** 4.1 the four steps in the participant card format on both pages; on the facilitator page "How to explain the four steps" comes before the cards and the cards carry no "How to explain it" row · **4.2 Practising the Alignment Dialogue**: on the facilitator page the role play in class, between any two roles the facilitator chooses (three decisions, seven steps, two example briefs, watch points) and a numbered PARTICIPANT ACTIVITY note; on the participant page Portfolio work: the participant chooses a Key Result from a drop-down list, reads the scenario (the board chair has disagreed with the current metric and timeframe and gives a 5) and writes the dialogue under Goal, Reality, Options and Will to move the chair to a 10.
- **Section 5 · Establishing Delivery Expectations:** group work, Capstone work, two exercises. **5.1 Building the Expectation Architecture:** four steps on two Objectives with one Key Result each; Objective, Key Result and Success in Practice statement are chosen from drop-down lists; 42 entries. **5.2 Conducting the Alignment Dialogue with the Board Chair:** the group chooses one Key Result from a drop-down list, reads the scenario of part 4.2 and writes its side of the dialogue under Goal, Reality, Options and Will to move the chair to a 10; 5 entries. One record for both exercises, Confirm and Print.
- **Facilitator wording on group work:** the facilitator guides how the work is completed. Capstone work is reviewed independently at graduation, so Section 5 carries no "listen for", "challenge", "watch for" or "check" (the build stops if one appears).
- **Text boxes:** every guidance box holds short paragraphs or a list, never loose text (`guide()` in the build; the test checks it).
- **No times** on either page or on the changed slides.
- **Facilitator page:** preparation only, no entry box, 11 PARTICIPANT ACTIVITY notes (eight reflections, part 4.2, part 5.1, part 5.2).

## Response keys (lens `u3m1_lens6`, no database change for the pages)

- Reflections `ref1` to `ref8` unchanged (`ref8` now sits in 1.4). Each question carries `class="ref-prompt"`.
- Part 4.2, Portfolio work: `ad_kr`, `ad_goal`, `ad_reality`, `ad_options`, `ad_will`. They save as the participant works and go with Submit to Facilitator. Each has a `<label for=…>` so the Learning Portfolio prints the label above the answer.
- Section 5: `__ex_work` (the 47 entries: `o1_…` and `o2_…` for 5.1; `dg_kr`, `dg_goal`, `dg_reality`, `dg_options`, `dg_will` for 5.2), `ex_record` while the group works; on Confirm `ex_future`, `ex_delivery`, `ex_chain`, `ex_ownership`, `ex_dialogue` and `confirmed_items` names "Expectations · Start With the Future", "· Delivery Expectation", "· Expectations Chain", "· Ownership", "· Alignment Dialogue". An edit after Confirm removes the names.
- The drop-down lists read the member's own Unit 3 page (`u2m1_lens2`: `__okr_work`, `confirmed_items` holding "Enterprise OKRs") and Unit 2 page (`u2m1_lens1`: `sip_d1_st` to `sip_d4_st`, where `confirmed_items` holds the SiP name).
- The three follow-up entries of Step 4 are needed only when the first score is below 9.
- No longer written (old answers stay in the database): the eleven `app_…` keys.

## The deck (24 slides)

Built on Carol's own 24-slide file of 12:56 (the 25-slide deck of round 2 less the "Two Objectives" slide she removed). Her slides 1 to 20 are untouched, shape and note (checked by comparing the XML). Changed in round 3: slide 21 "Section 4 Reflections" (the 4.2 picture now shows the title and the four instructions only) · slide 22 Section 5 opener (notes: two exercises, how the group works, where the work goes) · slide 23 "5.1 · Building the Expectation Architecture" (notes guide how each step is completed) · slide 24 "5.2 · The Alignment Dialogue with the Board Chair" (new: Goal, Reality, Options, Will) · the "Unit Summary · Closing" slide has left. Notes: heading, HOW TO TEACH IT, numbered steps with Say, ON THE PORTAL, AFTER THE TEACHING; no times; no review wording on the group work.

## Written to the portal folder (11 October, 13:30)

| File | md5 | What changed |
|---|---|---|
| `unit3_m1_lens6_p.html` | 9872d13440bbb0a6f7a1bdfdf89c1097 | the build above |
| `unit3_m1_lens6_f.html` | 32fee0a2478ae4268c703ac3521f25c0 | the build above |
| `capstone_P.html` | c50453f25cf1724ffafce9dd5aa1905f | Unit 7 keeps five boxes with new content (7A Start With the Future, 7B Delivery expectation, 7C Expectations chain, 7D Ownership, 7E Alignment dialogue with the board chair), all brought in through `PULL.u7` |
| `dashboard_F.html` | 11bfb0da2958b8586759edfb1586b302 | headings "Practising the Alignment Dialogue" and "Establishing Delivery Expectations"; labels for `ad_*`, `ex_*`, `confirmed_items` (labels of old answers stay) |
| `build_collection.js` | fb7b66e56b71a06594d2c001abf71f7e | `CAPSTONE_KEYS.u3m1_lens6` |
| `collection.html` | ab4855d9483047d7ac7b10328041d55f | rebuilt with `node build_collection.js` (Unit 7: 5 arc segments, 60 prompts, 0 fallbacks) |
| `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` | a03928127f5be5aef01dde599d702330 | 24 slides; the same file is `Claude outputs\Deck upload\Module-3\unit-07.pptx`, with 24 pictures and `manifest.json` in `unit-07` (`reader_assets.py`) |

Database: the Capstone box count for Unit 7 is 5 and stays 5 (`capstone_unit6_boxes.sql` kept the value every other unit had; the function gives 5 where no other number is set). No SQL.

`node check_standards.js` on the portal folder: no page breach (the Rule 16 lines are decks of other units).

## End-to-end check (11 October, before the push)

`e2e_u07.py`: the real `unit3_m1_lens6_p.html`, the real `s2r-save.js`, the real `capstone_P.html` and the real rebuilt `collection.html`, in a browser, on a stand-in database. 37 of 37 checks pass. Nothing touched the live site or Supabase.

- Unit 7 page: the eight reflections and the Portfolio work of part 4.2 (`ad_kr` and the four GROW boxes) save under the member. Section 5 saves while typed; Confirm saves `ex_future`, `ex_delivery`, `ex_chain`, `ex_ownership`, `ex_dialogue` and the five names in `confirmed_items`.
- Capstone page: before Confirm nothing is brought in. After Confirm, opening the Capstone fills 7A to 7E word for word and saves them on the team's Blueprint; with five boxes the section goes for team confirmation; a teammate sees the same text; with both confirmations the section is Agreed.
- Learning Portfolio: it reads the submission, so a member's answers appear after that member selects Submit to Facilitator. The Unit 7 chapter has two headings: Reflections (eight answers under their questions) and Practising the Alignment Dialogue (the Key Result and the four GROW answers under their labels). The group work of Section 5 is left out. With two headings the chapter opens closed on screen; on paper every heading prints open.
- Control: with the Unit 7 line taken out of `collection.html` the group work shows in the Portfolio; with the Unit 7 rows taken out of `capstone_P.html` there is no bring-in.
- Not checked: the live site (no push yet).

## Final scan (`final_scan_u07.py`)

Pages: part titles, sub-lines, Key learning outcomes and section outcomes identical on both pages; no leftovers. Deck: 24 slides, no text under 24pt, no times, no parts that have left. On Carol's own slides (hers to decide): slide titles shorter than the part titles (1.1, 1.2, 2.1, 2.2, 2.3, 3.1); the first Section 1 outcome on slide 4 has no full stop; "Watch for" in the notes of slides 17, 20 and 21 (class teaching and role play, not group Capstone work).

## Still to do after the push

1. Carol: Storage upload (`facilitator_decks`, `Module-3`): replace `unit-07.pptx`; folder `unit-07`: the 24 pictures and `manifest.json` (the old folder held 22 pictures; none is surplus).
2. Check the push without git (`.git\refs\heads\main` against `.git\refs\remotes\origin\main`, blob check of each named file) and read the live pages.
