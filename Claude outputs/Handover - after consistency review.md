# Handover — after the consistency review of Units 1–11 (28 Oct 2026)

Carol (Dr Carol Hachandi Lupiya) is not technical: grade 5 steps for anything she does. Claude is the tech party. Her instruction is final; apply every change everywhere it appears. Folder `C:\Users\Carol\ibsl-platform` (device shell `$HOME/mnt/ibsl-platform`); live site ibslportal.netlify.app, deployed from `main`.

## 0. How to write the next brief (Carol, 28 Oct: "you are the one giving me the briefs")
A brief for a new chat is written from this file's section 1 at the moment it is written, after reading `.git\refs\heads\main` and `.git\refs\remotes\origin\main` and the newest handover sections. The 28 Oct brief said Unit 12 was not built and gave head 8f06a53; three pushes had followed (Unit 11 Cultural Operating Code, Unit 12 build, Unit 12 live check). Every handover now ends with a dated "State now" line, and older handovers carry a "Superseded" note.

## 1. State now (28 Oct 2026, before Carol's push)
- Git head before this work: `main` = `origin/main` = `3f7577e` "Unit 12 live check and test account run recorded".
- Units 1–12 are built and live. Unit 11 has 4.7 and 5.8 (Cultural Operating Code) and Capstone 11E (5 boxes). Unit 12 · Sustaining Performance is live (12A–12D). Box counts 8,6,6,6,3,3,5,5,5,4,5,4.
- Her folder holds uncommitted work from earlier sessions (deck files in `Claude outputs\Deck upload`, two handovers, `lens_migration_playbook.md` showing as deleted, many backup folders). Push blocks name only the files of the current work.
- Files on her Windows checkout are CRLF and git stores LF: the device shell's `git diff` shows whole files changed; `git diff --ignore-cr-at-eol` shows the real change.

## 2. What changed (consistency review, applied 28 Oct; backups in `Claude outputs\Backups\Consistency review 28 Oct`)
- Line under each unit title: Unit 1 "Foundation · Behavioural Strategy"; Units 2–4 "Direction · Pillar 1 of DIG"; Units 5–9 "Influence · Pillar 2 of DIG" (Units 10–12 unchanged).
- Facilitator intros of Units 1 and 4 now match the participant paragraph (Unit 1 said "five sections").
- Reflections: Unit 11 label "✎ Reflection — My Functional Health Accountability"; Save buttons of Unit 9 (ref2, ref7, ref8) and Unit 11 (ref7) read "Save Reflection"; one confirmation everywhere, "✓ Saved to your portfolio" (Units 2 and 3 placeholders, Units 5, 6, 11 button flash); Unit 2 and 3 double reflection icon removed.
- Section 5: box label "Capstone work · How Section 5 works" (Units 2–9; Units 3 and 4 in the "Working as a group" box; Unit 1 "Capstone work · How 6.2 works"); each unit names the boxes its record fills (2A–2F, 3A–3F, 4A–4F, 5A and 5B–5C, 6A–6C, 7A–7E, 8A–8E, 9A–9E, 10A–10D, 11A–11E); group print button "Print our group record" (Units 1, 3–11); Unit 2 gains Agree beside Print in its group record.
- Unit 2 lock message names "Unit 1 — Behavioural Strategy Fundamentals" (was "Foundations"). Facilitator back button "← Back to Dashboard" in Units 4–12; Unit 1 facilitator gate "Checking access…".
- Unit 11: transitions to Sections 4 and 5 rewritten to match Section 4 content and part 5.8; five section learning outcomes reworded (S1b, S2b, S3a, S4b, S5b) to drop tool names and task wording and to cover the Cultural Operating Code.
- Module 4 line (Units 10, 11, 12): "Unit 11 — Culture Reinforcement & Organisational Health (culture), and then to Unit 12 — Sustaining Performance…".
- Capstone page: Unit 1 section headed "Behavioural Strategy Fundamentals"; page heading "Capstone S2R® Blueprint Showcase".
- "Capstone S2R® Blueprint" with ® everywhere (100 places in pages, Learning Portfolio, s2r-team.js, dashboards); Unit 1 "S2R® Capability Blueprint" renamed.
- Copy: "toward" → "towards" (71); Unit 4 contrast sentence and Unit 6 Unit Summary quote reworded; "automatically" removed from 15 teaching sentences.
- Build scripts of Units 10, 11, 12 carry the same text so a rebuild keeps it. STANDARDS.md rules 4, 5, 6, 25 updated and rules 28, 29 added; `check_standards.js` skips Rule 27 for Units 10 and 11. Checker: only deck slide sizes remain (Rule 16, decks done at the end).
- Checks: id / href / lens / div / script counts equal to the backups (Unit 2 one more onclick = the new Agree); every inline script passes `node --check`; `node build_collection.js` rebuilt the Learning Portfolio.

## 3. Left, and why
- Confirmed names of Units 4 and 5 ("MBT · Executive Blind Spot", "Alignment Plan · …"): the Capstone page fills boxes by matching these exact names against what teams already agreed; renaming would empty agreed boxes. Box labels already read correctly.
- Reminder emails (`supabase/functions/send-reminders`) still say "Capstone S2R Blueprint" without ®: an Edge Function deploy is needed; fold into the next function deploy.
- Locked learning outcomes flagged, unchanged: Unit 10 (tool names, task wording), Unit 1 (three Key outcomes; two task-led section outcomes), Units 2, 3, 9 tool names; Key outcome counts 3 / 4 / 2.
- Unit 10 Facilitator Guide headings (Carol's locked text).
- Waiting for Carol's review in chat (drafts): Module paragraphs and Module learning outcomes for Modules 1–3 (sent 28 Oct), section closing insights and transitions for Units 1–10 (Unit 11: Section 1 transition and Section 5 closing insight), Unit 1–3 section sub-lines, Learning Journey tables for Units 1–10, unit-to-unit hand-off boxes.

## 4. Push status
- 28 Oct: push block given to Carol (files listed in it). After "pushed": read `.git\refs`, read the live pages with WebFetch, update this line.

## State now (28 Oct 2026)
Fixes applied in her folder; waiting for her push; drafts waiting for her review.
