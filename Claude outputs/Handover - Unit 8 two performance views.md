# Handover — Unit 8 · Performance Measurement: the two performance views

Written 15 October 2026 for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party" and makes the technical and database decisions.

Her words (15 October, 16:35): "Give me transfer notes to a new chat for unit 8. What we are doing is adding the addition layer that speaks to the two performance aspects - the human operating system and the organisation operating system. Read unit 5,6,7 to see how this has been embedded and suggest how we can add relevant content to bring in the new layer."

**The task:** do for Unit 8 what was done for Unit 6 (14 Oct) and Unit 7 (14 Oct): bring in the **Human Operating System** (what individuals and teams deliver: KPIs, OKRs, behaviours) and the **Organisational Operating System** (the conditions the organisation provides, through **ESRG**: Environment, Systems, Resources, Governance). Section 4 holds her corrections of 15 October, which govern; she guides the changes herself. Her instructions, or her own amended content document (`Claude outputs\Amended Unit Content\Unit 8 Amended content.docx` if she writes one), are the source. Her words on Unit 7 apply: "there are minor changes which just include the reference to the human and organisation performance, the rest remains pretty much the same - make sure it is coherent do not just add". If her document arrives, re-read it just before building: on 14 October she saved a new version of the Unit 7 document while the build ran.

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules and the unit standard; they apply word for word).
3. `Unit decks\_build\rebuild_u07pv\README.md` (the Unit 7 two-view rework, 14 Oct: method, scripts, tests, live write). Reuse the method: `build_u07pv.py` (surgical edits on the live pages, every replacement found once), `deck_u07pv.py` (surgical edits on her deck), `e2e_u07pv.py` (end to end on the real pages with `rebuild_u06\fake-supabase.js`).
4. `Unit decks\_build\rebuild_u06cm\README.md` (the Unit 6 rework: layout helpers SUB, ITEMS, TABLE, CARDS; notes check `check_notes_cover.py`).
5. The live Unit 6 and Unit 7 pages (`unit3_m1_lens5_p/_f.html`, `unit3_m1_lens6_p/_f.html`) and the current Unit 8 pages (`unit3_m2_lens7_p/_f.html`).
6. `Unit decks\_build\rebuild_u08\README.md` (how Unit 8 was built on 12 October).

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app. Database: Supabase "S2R Portal Production".

## 1. Units in play (talk in units, never in file names)

| Unit | Pages (Claude only) | Deck |
|---|---|---|
| Unit 5 · Aligning Heart & Mind | `unit3_m1_lens4_p/_f.html` | `Unit decks\Unit 05 - Aligning Heart & Mind.pptx` |
| Unit 6 · Performance Management Setup | `unit3_m1_lens5_p/_f.html` (`u3m1_lens5`) | `Unit decks\Unit 06 - Performance Management Setup.pptx` (33 slides) |
| Unit 7 · Establishing Performance Expectations | `unit3_m1_lens6_p/_f.html` (`u3m1_lens6`) | `Unit decks\Unit 07 - Establishing Performance Expectations.pptx` (23 slides) |
| **Unit 8 · Performance Measurement** | `unit3_m2_lens7_p/_f.html` (`u3m2_lens7`) | `Unit decks\Unit 08 - Performance Measurement.pptx` (24 slides) |
| Unit 9 · Strategic Unclogging | `unit3_m2_lens8_p/_f.html` | |
| Unit 10 · ESRG Alignment | `unit4_m1_lens9_p/_f.html` | |

## 2. State on 15 October (read-only)

- Git: `main` = `origin/main` = `c943681d94fa13e4e180f72031ec989d88e990fb` (Unit 7 two views). Units 6 and 7 are live (checked in the browser pane, 15 Oct 06:05; the fetch tool showed an old cached copy for a while: check with the browser pane, `fetch(url,{cache:'no-store'})`).
- Unit 8 md5: participant 010c3abf…, facilitator f38984cd…, deck e3408c4a… (= `Deck upload\Module-3\unit-08.pptx`, 24 slides). capstone_P.html f0c01984…, dashboard_F.html 37705aa8…, build_collection.js cf1208ff…, collection.html 497c03b8….
- Capstone Unit 8: boxes 8A–8D (database count 4), `PULL.u8` from `rd_warning`, `rd_accountability`, `rd_learning`, `rd_credibility`.

## 3. How the two views are embedded so far

- **Unit 5** names the people side only: its header says the unit "establishes the human operating system that enables strategy to move from intention to execution". It is the root of the Human Operating System; Unit 5 was not reworked for ESRG.
- **Unit 6** teaches the two operating systems (1.2 "Two Operating Systems Behind Enterprise Performance"), the S2R® Contribution Map™ (1.3: Enterprise OKR → functional contributions → what people must deliver with a measure, and the ESRG conditions the organisation must provide with a measure or evidence of readiness), FACES applied to both systems (1.4), compliance vs commitment across both, executive hot zones across both, Section 4 "Integration of Human and Organisational Performance". Key line: a missed target is evidence of a gap; it does not establish its cause. Capstone 6A Contribution Map (one Key Result, up to four functions: `__cm_work` keys `kr`, `kr_obj`, `fN_name`, `fN_contrib`, `fN_hos`, `fN_hosm`, `fN_esrg`, `fN_esrgm`), 6B FACES.
- **Unit 7** (woven into the existing text, 14 Oct): 1.1 human expectations and organisational expectations, both explicitly agreed, table row "Enabling conditions"; 1.2 Clarity, Capability, Commitment each in both systems; mutual accountability (individuals own their commitments, organisational leaders own the conditions they undertook to provide); 1.3 Upline / Downline / Crossline (External became Crossline everywhere); 1.4 the Alignment Dialogue tests "What contribution will you deliver?" and "What must the organisation enable for you to deliver it?", and separates a clarity gap, a skill or commitment gap, and an ESRG or cross-functional constraint, with a resolution owner and review date; 2.1 compliance when people are held to results while conditions sit outside their control; 2.3 the record separates the delivery owner from the ESRG resolution owner; 3.1 each CXO role places expectations and owns ESRG commitments (finance resources, operations systems, HR capability and environment, executives governance). Section 5 (Capstone 7A–7E): two contributions from the Unit 6 map, each with the people expectation and the four ESRG conditions with owners, Crossline chain, actions with owner and review date.
- **Boundary (Carol, 14 Oct):** the environment's elements are taught in depth in Units 9–12 (Unit 10 is "ESRG Alignment"). Units 6–8 keep ESRG at the level of conditions that are expected, evidenced and owned. Unit 8 measures and reviews them; it does not teach how to fix them.

## 4. Carol's corrections (15 October, 16:43) — these govern; she will guide the Unit 8 changes herself

Her words: "unit 5 yes is just people side. we are not saying whether the agreed ESRG conditions are in place but whether they support execution of the people tasks - something like that. Review–Realign–Restore cycle is for both human and organisation not this - Realign separates a human cause from an organisational cause. The only changes that must happen are that the organiastion element is now added to the review - the human is not being infused into the organisation. ANyway I will guide you may just confuse the flow."

What this means for the new chat:
- Unit 5 is the people side only (confirmed).
- The organisational question in Unit 8 is whether the ESRG conditions **support the execution of the people's tasks**. Never word it as "whether the agreed ESRG conditions are in place".
- The Review–Realign–Restore cycle (R3) applies to both the human and the organisational performance. Do not describe Realign as separating a human cause from an organisational cause.
- The only change: the organisational element is **added to the review**. The existing human content stays as it is; the human is not infused into the organisation, and no existing human wording is rewritten into two-view wording.
- **Carol guides the Unit 8 changes.** Wait for her instructions or her document; do not propose a list of changes first. The proposal below is background only and is superseded wherever it conflicts with these lines (in particular items 2, 4 and 5).

## 4a. Proposal sent to Carol (15 October, superseded where it conflicts with section 4)

The unit's logic stays: Unit 8 reviews what Unit 7 established. Each review now examines two things for every Key Result: the progress of the people's contribution, and whether the ESRG conditions the organisation undertook to provide are in place.

1. **Header and Key learning outcomes:** the purpose sentence names both views; KLO 1 already says "the wider organisational context"; KLO 4 could read "…leadership action from human and organisational performance evidence" (her call).
2. **1.1 The Execution Visibility Infrastructure:** one paragraph and two short cards: measurement makes visible (a) progress of what people deliver (the KPI/OKR measures of the Contribution Map) and (b) whether the agreed ESRG conditions are in place (the ESRG measures or evidence of readiness). Reflection 1.1 adds "and one condition the organisation must provide".
3. **1.2 Four purposes:** Purpose 02 accountability covers the delivery owner and the ESRG resolution owner; Purpose 03 adds a fourth review question, "Is the obstacle in the people's contribution or in a condition the organisation must provide?"
4. **1.3 R3 cycle:** Review brings both kinds of evidence; Realign separates a human cause from an organisational cause (Unit 6 line: a missed target does not establish its cause); Restore agrees actions for both owners, each with a review date.
5. **1.4 Accountability Loop:** Root Causes A and B sit in the Human Operating System. Root Cause C is split in its wording into role misfit (people) and structural or ESRG constraint (organisation); for the second, the recovery is owned by the ESRG resolution owner named in Unit 7 and is not treated as a personal performance failure. GROW stays.
6. **2.1 Four consequences:** Consequence 01 early warnings include condition signals (system downtime, capacity shortfall, delayed decision); Consequence 02 diffusion of accountability also hits promised support that is never reviewed (links to Unit 7 2.1 compliance).
7. **3.1 Four fractures:** Evidence Quality Gap adds that reviews often hold people evidence and no evidence on conditions; Horizontal Coordination Gap names the Crossline dependencies.
8. **3.2 CXO cards:** one line per role, "The condition you own and rarely review" (finance resources, operations systems and work design, HR capability and environment, CEO governance decisions…), as in Unit 7 3.1.
9. **4.1 EPIC:** each signal is tagged people or condition; Signal 1 trajectory carries the ESRG readiness measures; Signal 2 asks "Is this a people signal or a condition signal, and who owns it?"
10. **4.2 role play (Portfolio):** the Head of Logistics case stays. The competing CEO priority (warehouse move) is a governance condition: the "Your judgement" question adds "Which part of the gap sits in the organisation's conditions, and who owns it?" No new box.
11. **Section 5 (Capstone 8A–8D):** for each consequence the two decision points become one on people's delivery and one on the organisation's conditions (labels "Decision point 1 · the people", "Decision point 2 · the conditions"); same keys, same four boxes, no SQL; Capstone box descriptions updated.
12. **Unit Summary, facilitator guidance, deck:** follow the pages; notes surgical on her deck; reflection slides only where a reflection changed.

## 5. Order (as Units 6 and 7)

Her decisions or her document → PREVIEW pages in `Claude outputs\Review files\Unit 8\` + deck in `Unit decks` (backups first: `Backups\Unit 8 file backups`, `Unit 8 deck backups`, "- before two performance views (date)") → her rounds → her word ("build live files" / "commit to live files") → live pages, `capstone_P.html` 8A–8D descriptions, `dashboard_F.html` labels if keys change, `node build_collection.js`, e2e test with a control, deck reader folder (`reader_assets.py`; move surplus pictures to `_to_delete`), `node check_standards.js`, her one PowerShell block (every file named), Storage upload in grade-5 clicks, then check the push (refs + LF blob hashes) and the live pages in the browser pane.

## 6. Not committed yet

Add to the next `git add` line: `"Claude outputs/Handover - Unit 8 two performance views.md"`.

## 7. Done on 15 October (evening)
Carol locked Sections 1–5 one at a time (record: `Claude outputs\Review files\Unit 8\Unit 8 two views - locked amendments.md`), then said "build live files" (20:08). Method, files, md5s and tests: `Unit decks\_build\rebuild_u08pv\README.md`. Live once she commits and pushes, and uploads unit-08.pptx and the unit-08 folder to Storage.
