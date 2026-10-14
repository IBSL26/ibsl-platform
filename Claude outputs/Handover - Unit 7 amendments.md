# Handover — Unit 7 · Establishing Performance Expectations: the two performance views

Written 14 October 2026 (21:00) for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party" and makes the technical and database decisions.

Her words (14 October, 20:53): "Done give me transfer notes to a new chat for a similar work for unit 7 - that is incorporating the two performance views."

**The task:** do for Unit 7 what was done for Unit 6 today: bring the two performance views into the unit — the **Human Operating System** (what individuals and teams deliver: KPIs, OKRs and behaviours) and the **Organisational Operating System** (what the organisation enables, examined through **ESRG**: Environment, Systems, Resources, Governance). Take the exact task from her first message. She is likely to give amended content (a document in `Claude outputs\Amended Unit Content\` or texts in the chat): her texts are the source. If she gives no texts, read Unit 6 as live and the Unit 7 pages, then send ONE short list of where the two views enter each Unit 7 section, and build the PREVIEW pages straight after her word.

## 0. Read first, in this order

1. This file.
2. `Unit decks\_build\rebuild_u06cm\README.md`: the Unit 6 rework of today, start to live (method, scripts, keys, tests). Reuse the method and scripts.
3. The live Unit 6 pages `unit3_m1_lens5_p.html` / `_f.html` (the model Carol approved tonight) and `Claude outputs\Amended Unit Content\Amended content.docx` (her Unit 6 text: the two operating systems, ESRG, the S2R® Contribution Map™, FACES applied to both systems).
4. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules, unit standard) and `Claude outputs\Handover - Unit 7.md` (how Unit 7 was built on 11 October).
5. `STANDARDS.md`, then `node check_standards.js` (read-only).
6. `Unit decks\_build\rebuild_u07\README.md` and `u7_content.py`, `u7_p.js`.

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app. Database: Supabase "S2R Portal Production".

## 1. Talk in units, never in file names

| Unit | Pages (Claude only) | Deck |
|---|---|---|
| Unit 6 · Performance Management Setup (done tonight) | `unit3_m1_lens5_p/_f.html` (`u3m1_lens5`) | `Unit decks\Unit 06 - Performance Management Setup.pptx` (33 slides) |
| **Unit 7 · Establishing Performance Expectations** | `unit3_m1_lens6_p/_f.html` (`u3m1_lens6`) | `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` |
| Unit 8 · Performance Measurement | `unit3_m2_lens7_p/_f.html` (`u3m2_lens7`) | `Unit decks\Unit 08 - Performance Measurement.pptx` |

## 2. State on 14 October, 21:00 (read-only)

- Git: Carol pushed the Unit 6 work: `main` = `origin/main` = `5ccc7a9596e63612fb3fd7053a7ae579059165ec`. She reported SQL, push and Storage upload done ("Done").
- Unit 7 pages: participant md5 8f45a80b…, facilitator 48fbf693…; deck f4814297… (identical to `Claude outputs\Deck upload\Module-3\unit-07.pptx`). Unchanged since 11 October.
- `capstone_P.html` 2225d9bd… · `dashboard_F.html` 37705aa8… · `build_collection.js` cf1208ff… (all with the Unit 6 changes of tonight).
- Database box counts after tonight: u6 = 2 (6A S2R® Contribution Map™, 6B FACES application). Unit 7 = 5 (7A–7E). Check with the read-only block of `Claude outputs\capstone_unit6_boxes_cm.sql` if needed.

**Unit 7 today** (see `Handover - Units 6 to 8 review.md` §1 for the full list): 1.1 Setting vs Establishing Expectations · 1.2 The Three Conditions of Established Expectations · 1.3 The Expectations Chain · 1.4 The Alignment Dialogue (GROW) · 2.1 Compliance vs Commitment: The Execution Dynamic · 2.2 Five Mechanisms · 2.3 Engagement & Accountability · 3.1 CXO Expectation Tendencies & Gaps · 4.1 The Four-Step Expectation Architecture · 4.2 Practising the Alignment Dialogue (Portfolio work) · Section 5: 5.1 Building the Expectation Architecture, 5.2 Alignment Dialogue with the Board Chair (Capstone 7A–7E; `__ex_work`, `ex_future`, `ex_delivery`, `ex_chain`, `ex_ownership`, `ex_dialogue`). Section 5 reads the group's Unit 3 Objectives/Key Results and Unit 2 SiP through drop-down lists.

## 3. What Unit 6 now teaches (Unit 7 must flow from it)

- Two operating systems: Human (results against KPIs/OKRs; behavioural expectations) and Organisational (ESRG). A missed target is evidence of a gap; it does not establish its cause. Accountability extends to those who own the ESRG conditions.
- The S2R® Contribution Map™: Enterprise OKR → required functional contributions → for each function, what people must deliver (with a measure) and the ESRG conditions the organisation must provide (with a measure or evidence of readiness).
- FACES applied to both systems; four execution bridges; compliance vs commitment across both systems; ten executive hot zones across both systems; three continuous-PM shifts.
- Unit 6 Section 5 (Capstone 6A, 6B): each group built a Contribution Map for ONE enterprise Key Result (Objective then Key Result drop-downs from Unit 3) and FACES for each function. Keys on `u3m1_lens5`: `__cm_work` (`kr_obj`, `kr`, `f1_name`…`f4_name`, `fN_contrib`, `fN_hos`, `fN_hosm`, `fN_esrg`, `fN_esrgm`, `fN_F`…`fN_S`), `cm_map`, `cm_faces`, `confirmed_items` names "Enterprise PM System · Contribution Map" / "· FACES Application".
- Natural link for Unit 7: expectations are established for both systems — what people are expected to deliver, and what the owners of ESRG conditions are expected to provide. Unit 7 Section 5 could read the group's Unit 6 Contribution Map (read only) the way it reads Unit 3 and Unit 2 today. Propose; the design is hers.
- Context to keep in view: Carol said on 14 October that the environment's elements (systems, resources, governance, culture) are covered in Units 9–12 and must not be brought into Units 6–8 as full teaching; her own Unit 6 text then brought ESRG in as the second performance view. Follow her Unit 7 texts; if they are silent, keep ESRG at the level Unit 6 uses (conditions to be expected, evidenced and owned), and point to Units 9–12 for the depth.

## 4. Carol's rules from tonight (apply to Unit 7 from the first build)

- **Outcomes:** two per section, aligned to what the section teaches and to the Key learning outcomes; they never name a tool (no FACES, Contribution Map, GROW in outcomes). She asked: "align the section learning outcomes to the content and they must just be 2 per section".
- **Layout ("the idea is not to tire the eye"):** long sub-parts, long tables and long cards collapse and open when selected (both pages). Once one sub-part in a part is collapsible, every sub-part below it in that part is collapsible too. Short content (2–3 sentences per card) shows as horizontal cards with no arrows. A wide or long table becomes compact rows: the first column shows, the rest opens on selection. Unit 6 helpers: `SUB`, `GROUP`, `ITEMS`, `TABLE`, `CARDS`, `CXO` in `rebuild_u06cm\u6cm_content.py`; styles in `u6cm.css` (`.u6-sub`, `.u6-it`, `.u6-hc`, `.u6-cx`).
- **Reflections:** placed where the content is taught (she asked for 1.3 and 1.4 in Unit 6, "I did say this — you missed it"); no "Personal reflection · it goes into your Learning Portfolio…" line ("they know already").
- **Section 5 participant page:** no guidance tables ("it is just cluttering"); each box carries its own question as placeholder; Objectives and Key Results as drop-down lists (Objective first, then its Key Results).
- **Participant page streamlined** (her: "streamline content on the participant"), written to "you"; **facilitator page keeps all of her content** and every Facilitator Guidance block.
- **Deck:** built on top of her current deck; notes in the approved format (HOW TO TEACH IT, numbered Say/Ask steps, ON THE PORTAL, AFTER THE TEACHING) and **all facilitator-page content in the notes** (`check_notes_cover.py` lists facilitator sentences missing from the notes). Slide text ≥24pt (including table cells and paragraph ends). Reflection slides with pictures from the participant page.
- House wording: no "lens"; no "instead of / rather than"; "Integrating" not used (Rule 2); S2R® with ®; no times; nothing "automatic"; she reads the "she said it already" cost: apply every point of a message in one pass.
- Order she follows: her texts → PREVIEW pages in `Claude outputs\Review files\Unit 7\` + deck in `Unit decks` → her rounds → "build live files" → live pages, Capstone link (`capstone_P.html` boxes + `PULL.u7`), box count SQL if the number changes, `dashboard_F.html` labels, `CAPSTONE_KEYS.u3m1_lens6` + `node build_collection.js`, e2e test with a control, deck reader folder, `node check_standards.js`, then her one PowerShell block, SQL in grade-5 clicks, Storage upload.

## 5. Tools ready

- `Unit decks\_build\rebuild_u06cm\`: `build_u06cm.py` (rebuild sections on top of the live page shell), `u6cm_content.py` (two voices + layout helpers), `u6cm_p.js`, `u6cm.css`, `test_u06cm.py` (67 browser checks), `deck_u06cm.py` (deck on her file: duplicate her slide layouts, notes with `F()` check against the facilitator page), `shoot_reflections_u06cm.py`, `patch_links_u06cm.py`, `e2e_u06cm.py` (+ `rebuild_u06\fake-supabase.js`), `check_notes_cover.py`.
- `Unit decks\_build\rebuild_u07\` (11 October build of Unit 7) and `reader_assets.py` in `Unit decks\_build\`.
- Backups go to `Claude outputs\Backups\Unit 7 file backups\` and `Unit 7 deck backups\` (dated 14/15 Oct) before any change.

## 6. Not committed yet

Add to the next `git add` line: `"Claude outputs/Handover - Unit 7 amendments.md"` (this file) and `"Unit decks/_build/rebuild_u06cm/README.md"` if it changed after the push.
