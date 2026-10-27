# Handover — after Unit 11 (Module 4 · Grounding)

Written 27 October 2026, 22:12, for a new chat. Carol (Dr Carol Hachandi Lupiya, IBSL founder) is not technical: every step she does herself is explained in grade 5 terms, one click at a time. She calls Claude "partner". Claude is the "tech party": it makes the technical and database decisions and carries out technical steps itself. Her instruction is final: never answer an instruction with options or a question on the same point. When she asks for a change, apply it everywhere without being told. Apply every point of an amendment message in one pass. Nothing is left pending or unattended: when a step cannot finish (for example the computer link drops), finish it as soon as it can and say so.

**WAIT FOR HER INSTRUCTIONS.** She works section by section: she sends each section as a Word file, Claude applies it to both pages as PREVIEW, she corrects, then "build live files". Decks are done right at the end for all units (do not touch decks until she says).

Folder: `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`). Live site ibslportal.netlify.app (Netlify deploys from `main`). Database: Supabase "S2R Portal Production" (ref tayrxqbrttlrdowrzobm).

## 1. Read first, in this order
1. This file.
2. `Claude outputs\Handover - Unit 11.md` (all of it; section 8 = how Unit 11 was rebuilt).
3. `Claude outputs\Review files\Unit 11\Unit 11 - decisions and locks.md` (every Unit 11 decision and standing-rule rewording).
4. `Claude outputs\Handover - Unit 10.md` sections 8-10 and `Review files\Unit 10\Unit 10 - decisions and locks.md` (the same method for Unit 10).
5. `Unit decks\_build\rebuild_u11\` — the method to copy for Unit 12 (build script from backups, one content module per section, PREVIEW maker + mock, links patch).

## 2. State at 22:12 (checked)
- Git `main` = `origin/main` = `02ccecd9…` "Unit 11 rebuilt" (pushed by Carol 22:11). Before it: `64eae8b4…` (ESRG alignment of Units 6-9).
- Unit 11 live: `unit4_m1_lens10_p.html` 24aa88a2…, `_f.html` 7427fb60…, `capstone_P.html` 9b3f9ddd…, `dashboard_F.html` 5461e494…, `build_collection.js` 7d4cc0f5…, `collection.html` bef1096f…. Live participant page read with WebFetch: Section 5 is "The Cross-CXO Organisational Health Clinic", the Section 4 reflection is there, the old ACE-IT section is gone.
- Carol ran `Claude outputs\unit11_health_clinic.sql`. Checked by Claude 22:16 (read-only, SQL editor): box counts 8,6,6,6,3,3,5,5,5,4,4,5 (u11 = 4).
- Not committed yet: this file (Carol may not have run the 22:16 push block; check `.git\refs` and include it in the next `git add` either way).
- Live cohort: Unit 11 is complete and working live (pages, Capstone 11A-11D, box count, report labels, Learning Portfolio). Nothing for the live cohort is waiting.

## 3. Unit 11 in brief (title unchanged: "Culture Reinforcement & Organisational Health", lens id u4m1_lens10)
- Header in the Unit 10 format (Grounding · Pillar 3 of DIG, Module and Key learning outcomes). Guide: Unit Intent, Learning Journey, Facilitation Emphasis.
- Sections 1-3 are teaching (read-only on the participant page; prompts as "Reflect:" lines). Section 4 ends with "Individual Reflection: My Functional Health Accountability" (key ref7, five fields) for facilitator feedback; Carol: it does not feed Section 5.
- Section 5 "The Cross-CXO Organisational Health Clinic": group Capstone work on the shared group record (`s2r-team.js`), using her 10-function reference figures; the group ticks its CXO roles (pre-ticked from the agreed Problem Charter executive team, matched by CEO/CFO/COO/CHRO/CTO-CIO/CMO/CCO/CPO/CRO/CSO). Keys __oh_work, oh_func, oh_cons, oh_rrr, oh_resp = Capstone 11A-11D. Unit Summary removed (as Unit 10).

## 4. Next steps
1. (Done 22:16) Box counts checked.
2. FIRST TASK for the new chat: test account run of Unit 11 on the live portal (Test Participant, team Alpha, Alpha Client Services, one member) in Chrome with the test account signed in by Carol (never sign in for her): Section 4 reflection (ref7) with realistic content; Section 5: choose scribe, tick the role(s) from its Problem Charter (its executive team decides which), fill every card, Tasks 4-6, Review/Realign/Restore, one Task 7 response (lowest trait), Agree; check the Capstone page shows Unit 11 AGREED with 11A-11D filled. Before starting, check the signed-in badge on the Unit 11 page: at 22:16 Chrome was signed in as Carol (Facilitator). If so, ask her in grade-5 steps to sign out and sign in as Test Participant, then do the whole run yourself. Tell Carol to sign back in with her own account afterwards. Then give her one push block for this file's update.
3. Unit 12 · Sustaining Performance (`unit4_m2_lens11_p.html` / `_f.html`) when Carol sends her direction / Word files: same method; align its "ESRG Scanner" card (led by COO, CTO/CIO, CHRO, CFO) to Unit 10's ESRG (FIT · SIP · AIR · PAR). Capstone u12 currently 5 boxes.
4. Decks for all units at the end (Units 6-11 need the new content and ESRG wording), then Storage uploads.

## 5. Technical rules (unchanged)
- Never run git in her folder; check pushes by reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main`. The device shell cannot delete: move files to `Claude outputs\_to_delete`. Pages are UTF-8, CRLF. Keep device_bash commands under ~12 KB.
- Changing the live database from Claude is blocked: SQL goes to Carol in a chat code block with grade-5 steps (tested first in pglite). Never read the dashboard token from localStorage.
- Push: one PowerShell block starting `cd C:\Users\Carol\ibsl-platform`, every file named in `git add`, commit message ending with the new session's attribution lines, then `git push`.
- Tests: Playwright in the cloud workspace on PREVIEW pages staged with `device_stage_files` (serve with `python3 -m http.server`).
- If the link to her computer drops, the device tools come back by themselves while the Claude app stays open; finish any unwritten step as soon as they return.

## 6. Carol's instruction (27 Oct 22:17)
Do not leave pending issues for Carol: she is not technical and runs a live cohort. Every open item above is Claude's to carry through to live in the new chat; ask her only for the steps only she can do (signing in, running the SQL or push blocks Claude gives her).

## 7. Test account run of Unit 11 (27 Oct 2026, 22:20-22:30, live portal, Chrome signed in as Test Participant by Carol)
- Git before this: `main` = `origin/main` = `0f79fa6a…` "Handover after Unit 11" (Carol's 22:16 push).
- Section 4: Individual Reflection ref7, five fields filled (CEO, Executive Office: High Morale, lost time from board-paper rework, about R84,000 a quarter, observed vs assumed, quarterly priority list action). Saved: "Saved to your portfolio".
- Section 5: scribe = Test Participant; CEO ticked from the Problem Charter executive team ("CEO · Test Participant"). CEO card (Tasks 1-2), Tasks 4-6, Review/Realign/Restore and one Task 7 response (Minimal Confusion, lowest trait 16/20; Lost Time R12,000 -> R7,000, reduction R5,000) filled. Record complete; Agree -> all agreed; confirmed names = the four "Health Clinic · …" items.
- Capstone page: Unit 11 · Culture Reinforcement & Organisational Health AGREED; 11A-11D filled (11B: CEO, 18 valid responses, 82.0 /100 Healthy & Thriving).
- Note: the Agree button in part 5.8 sits inside a closed fold-out; the group bar Agree button records the agreement. Both call the same agree.
- Next: Unit 12 when Carol sends her direction. Decks at the end.

## 8. Unit 12 built as PREVIEW (27 Oct 2026, 23:07-23:55, from Carol's Word document)
- Carol 23:07: "USE THE DOCUMENT TO CREATE UNIT 12" (document: `Review files\Unit 12\Unit 12 Sustaining Performance - Facilitator.docx`). Every decision in `Review files\Unit 12\Unit 12 - decisions and locks.md`.
- Build: `Unit decks\_build\rebuild_u12\` (`build_u12.py` from `Backups\Unit 12 file backups\Pages before Module 4 rework (27 Oct)`; content `u12_content.py`, `u12_html.py`, `u12_s5.js`; links `patch_links_u12.py` -> `out\links`; PREVIEW `make_previews_u12.py` + `mock-s2r-u12.js`; tests `test_u12_preview.py`, 39 of 39).
- Two concepts through every section: Three Lines of Sight (read through WARD) and KISS. Section 5 = Quarterly Three Lines of Sight page on the shared group record, bringing in Unit 6 WARD, Unit 10 es_scanner and Unit 11 oh_cons; keys __qs_work, qs_strategic, qs_operational, qs_behavioural, qs_kiss = Capstone 12A-12D (4 boxes; SQL `unit12_quarterly_lines.sql`, tested in pglite: 8,6,6,6,3,3,5,5,5,4,5,4). Reflections ref11, ref12, ref13.
- PREVIEWs in `Review files\Unit 12\`. Nothing live yet. Next: Carol reviews; on "build live files" copy `out\*.html` and `out\links\*` live, `node build_collection.js`, Carol runs the SQL and the push; live check; test account run of Unit 12 Section 5; deck at the end.
- 23:26 Carol: "BUILD LIVE FILES". Live files written 23:30: unit4_m2_lens11_p.html 3cba7ee9…, unit4_m2_lens11_f.html 1425492f…, capstone_P.html 5a94b06c…, dashboard_F.html e3def8a4…, build_collection.js cf67ddd8…, collection.html b89ffd99… (node build_collection.js: u4m2_lens11 4 arc segments, 3 prompts). Backups of the four link files in Backups\Unit 12 file backups\Links before live (27 Oct). Head before the push: 34f53c19. Next: Carol runs unit12_quarterly_lines.sql and the push; live check; test account run of Unit 12 Section 5.
