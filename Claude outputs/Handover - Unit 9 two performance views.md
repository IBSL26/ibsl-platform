# Handover — Unit 9 · Strategic Unclogging: the two performance views

Written 15 October 2026 (evening) for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party" and makes the technical and database decisions.

Her words (15 October, 20:17): "give me the handover notes for unit 9 to go to the new chat". The task is the one just finished for Unit 8: add the **organisational side** of performance (the organisational conditions) to Unit 9, alongside the human side, as and when applicable. **Carol guides the changes section by section.** Wait for her instructions; take her first message in the new chat as the task.

## 0. Read first, in this order

1. This file.
2. `Claude outputs\Handover - Unit 8.md` sections 2 and 3 (working rules and the unit standard; they apply word for word).
3. `Claude outputs\Review files\Unit 8\Unit 8 two views - locked amendments.md`: what Carol locked for Unit 8, section by section. It shows the depth, wording and shape she approved.
4. `Unit decks\_build\rebuild_u08pv\README.md` and its scripts (`u8pv_content.py` content helpers and the two-side cards `u8v-hc`; `build_u08pv.py` surgical edits; `test_u08pv.py`; `e2e_u08pv.py`; `deck_u08pv.py`; `shoot_refs.py`). Reuse the method for Unit 9.
5. The live Unit 8 pages `unit3_m2_lens7_p.html` / `_f.html` (the approved look of the human side / organisation side cards).
6. `Claude outputs\Handover - Unit 9.md` (13 Oct) and `Claude outputs\Unit 9 - Three-way match (findings).md`: the Unit 9 rework that is still in Carol's review (section 2 below).
7. The live Unit 10 pages `unit4_m1_lens9_p.html` / `_f.html` (ESRG Alignment): read them for realistic organisational examples (Environment physical and behavioural, Systems, Resources, Governance and their sub-themes).

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app. Database: Supabase "S2R Portal Production".

## 1. State on 15 October, 20:17 (read-only)

- Git: `main` = `origin/main` = `32a9c85fe559f3af639cbd4ba29098c6a0c7063d` (Unit 8 two views). Unit 8 is live (checked in the browser pane), Storage upload done by Carol.
- Shared files now: capstone_P.html 1bafa5c6…, dashboard_F.html d6915376…, collection.html a3b4ed98…, build_collection.js cf1208ff….
- **Unit 9 (`u3m2_lens8`) live files are still the 13 October originals:** participant d41da670…, facilitator b65a81ba…, deck `Unit decks\Unit 09 - Strategic Unclogging.pptx` bc4df3b9… (25 slides, identical to `Deck upload\Module-3\unit-09.pptx`). Capstone Unit 9 boxes 9A–9E exist in `capstone_P.html` but there is no `PULL.u9` yet. Unit 9 pages mention the operating system in 2.1 ("Clogs emerge precisely where strategy stretches the existing operating system beyond its current design capacity"); no ESRG or organisational-conditions content yet.

## 2. Unit 9 has an earlier rework still in review

On 13 October a three-way-match rework of Unit 9 was built as PREVIEW only (`Unit decks\_build\rebuild_u09\`, `Claude outputs\Review files\Unit 9\PREVIEW - Unit 9 Participant/Facilitator.html`; backups in `Claude outputs\Backups\Unit 9 file backups\` and `Unit 9 deck backups\`). It moved the diagnostic triads to part 4.4 and turned Section 5 (the Clog Clinic) into group Capstone work feeding 9A–9E. Carol said on 14 October: "I am reviewing unit 9. I will give review notes." Those notes have not come in. Not yet done for that rework: live pages, `PULL.u9`, report labels, `CAPSTONE_KEYS.u3m2_lens8`, e2e, deck, reflection pictures, reader folder.
Report this in one line in the first reply of the new chat (the two-views layer would build on whichever version she keeps). Do not choose for her and do not offer options; follow her instruction.

## 3. Carol's rules from the Unit 8 two-views round (15 October) — these govern

Wording
- Say **"organisational conditions"** everywhere. Name ESRG once, where the conditions are first defined: "These conditions are the Environment, Systems, Resources and Governance (ESRG)…". Never "ESRG conditions", "ESRG owner".
- **"leaders"** for those responsible for the organisational conditions; **"individuals"** for the people delivering KPIs. Never "owner", "KPI owner", "contributor" in added text (existing human wording stays as it is).
- The organisational question is whether the organisational conditions **support the execution of the individuals' tasks**. Never "whether the conditions are in place".
- The human content is not rewritten into two-view wording; the organisation side is **added**. Review–Realign–Restore applies to both sides; never word Realign as separating a human cause from an organisational cause.
- Do not refer to other units or parts inside examples ("agreed in Unit 7", "part 1.4"); give realistic references. Name things in full (the three root causes by name, not "the three root causes of part 1.4").
- People-specific content stays people-only (in Unit 8 the Accountability Loop got no organisation side).
- Boundary: Units 9–12 teach the environment in depth (Unit 10 is ESRG Alignment). Unit 9 should stay consistent with Unit 10 (read it), without teaching Unit 10's tools.

Content and shape
- Under each existing card or part, after its narrative: a **"From the human side" / "From the organisation side"** pair (Section 3 style: "Implication for human performance" / "Implication for organisational performance"). Blue top border for human, green for organisation (`u8v-hc` classes; stacked layout `u8v-st` for long content).
- She wants **executive-level depth**: mechanisms, consequences and practical scenarios. Organisation examples come from the Unit 10 domains with their sub-themes (e.g. "Resources · workforce capacity", "Governance · decision authority", "Environment · psychological safety", "Systems · data integrity"); two or three per card, never all four by rote; each example is a concrete situation (signal → effect on the tasks → why the review misses it).
- Avoid framings open to interpretation (she rejected "build up around the individual's tasks, usually before they touch the KPI").
- **Facilitator Guidance boxes are summarised** to a few lines per section; the detail moves into the slide notes.
- Role plays are **open**: give the scenario and the roles (leader, team member, observer); do not script answers. Portfolio cases carry a full written conversation. GROW is "a conversation with an end in mind": G is what the leader aims to achieve (root cause, alignment, or both).
- Group exercises: say plainly what each group completes; keep the layout she has; reframe, do not restructure, unless she says so. No examples typed into answer boxes; one example line per tab is fine where it already exists.

Process (what worked)
- She goes **section by section**: Claude proposes the added content for that section in chat, she corrects, then says "lock". Record each lock in `Claude outputs\Review files\Unit 9\Unit 9 two views - locked amendments.md` right away (she said "do not get lost").
- **Do not implement until all five sections are locked**; then build PREVIEW pages + deck in one go, then "build live files".
- Chat replies: short, no long menus, no repeating everything. When she asks "what goes on the file", give only the exact text that goes on the page.

## 4. Order (as Unit 8)

Locks → backups (`Backups\Unit 9 file backups`, `Unit 9 deck backups`, "- before two performance views (date)") → build PREVIEW pages from the live (or her chosen) pages with a surgical script → browser checks → deck on top of her deck (notes carry two-view content and the facilitator detail; slide texts only where changed; retake reflection pictures whose prompt changed) → her word "build live files" → live pages, `capstone_P.html` descriptions, `dashboard_F.html` labels for new reflection keys, `node build_collection.js`, e2e with controls, Deck upload copy + reader folder (`reader_assets.py` in the cloud), `node check_standards.js` → her PowerShell block (every file named, commit lines with the attribution) → Storage upload in grade-5 clicks → check the push (refs + blob hashes) and the live pages in the browser pane (`fetch(url,{cache:'no-store'})`).

Never run git in her folder, not even to look (one slip on 15 Oct: a `git status`; no harm, but it breaks her rule).

## 5. Not committed yet

Add to the next `git add` line: `"Claude outputs/Handover - Unit 9 two performance views.md"`.
