# Handover — S2R® deck enrichment (new task)

Prepared 1 October 2026 for a new chat.

## 1. Read first

1. `Claude outputs\Handover - Unit decks.md` — working rules, deck brief, unit file map and build kit. Every rule there still applies.
2. `STANDARDS.md` in the portal folder.

## 2. The task

Carol wants the 12 facilitator decks in `Unit decks\` enriched with dense content. She will supply the source material. The decks as they stand carry the unit-file content in short slide text plus detailed presenter notes; the enrichment adds substance from her sources.

## 3. Settle these with Carol before building

1. **Sources:** what each source is (her own IP, published books or papers, client material) and which units it serves. Ask her to put the files in one folder, e.g. `Unit decks\_sources\`, so they can be read on her computer.
2. **Form of the density** (the 24pt minimum rules out small text):
   - more slides per section (e.g. one slide per clog, lever, role or bias, each with its definition, signals and impact);
   - diagrams and tables (pyramids, cycles, chains, matrices, comparison tables);
   - worked examples, cases and calculations on slides;
   - fuller bullets at 24pt.
3. **Scope:** one pilot unit for her review first, or all 12 at once. The pilot route has worked well: Unit 1 was approved before Units 2–12 were built.
4. **Portal alignment:** if new content goes into the decks, does it also go into the unit HTML files? Decks that teach material the portal does not hold will drift from it. Ask her.

## 4. Rules for the new content

- Use only Carol's sources and the unit files. Invent nothing; where a source is thin, say so and ask.
- Add a "Source:" line in the speaker notes of every slide that uses new material (document and page or section).
- Third-party published material: summarise in your own words; quote only short passages, with attribution.
- Where a source conflicts with a unit file, flag it to Carol and change nothing until she decides.
- Apply her writing rules to slides and notes: British spelling; tight copy; no contrast constructions of any kind ("not X — it is Y", "rather than", "instead of", "Not a…" fragments, teaching pairs); no "lens"; official unit titles; learning outcomes never name the tool.
- Show Carol the proposed slide list and two sample slides with notes in chat before building.

## 5. Current decks (baseline)

All 12 built from the unit files and committed. Slide counts: 02 · 31, 03 · 29, 04 · 18, 05 · 21, 06 · 28, 07 · 22, 08 · 23, 09 · 25, 10 · 25, 11 · 23, 12 · 20 (Unit 1 has its own hand-written script, `unit01.js`).

## 6. Technical notes

- Build kit in `Unit decks\_build\`: `lib2.js` (layouts `cover`, `list`, `section`, `prompt`, `cards`, `stat`, `compare`; `T()` refuses text under 24pt), `kit.js` (notes from the outlines), `extract.py`, `outlines\`, `unit01.js` … `unit12.js`. Run details are in the Unit decks handover, section 6.
- Dense content will likely need new layouts in `lib2.js`: a table layout, a diagram layout (drawn shapes for pyramids, cycles and chains), and a two-part "case" layout. Keep every text run at 24pt or more; a full-width box holds about six lines of 60 characters at 24pt.
- QA every deck: pptx validator, PDF → images and a look at every slide, notes scanned for "lens", contrast constructions and US spelling, then `node check_standards.js` (must report "No breaches found").
- Copy finished decks into `Unit decks\` with the official file names. Claude never runs git; give Carol the PowerShell commands.

## 7. Working style reminders

- Carol calls Claude "partner" and expects Claude to make the technical decisions.
- Find everything in one pass. When she says "fix everything", fix every instance of the same kind of problem, including ones outside the list shown to her, and report them.
- Back up before editing any portal file; verify after; say "done" only after the checks pass.

## 8. Status (end of 1 October 2026)

Carol's decisions:
- Only the presenter notes are enriched. Slide text, layouts and slide counts are unchanged; the unit HTML files are untouched.
- Source: the General Professional Insights (Strategy, Leadership, Culture) in Carol's nine devotional journals, January–September 2026. Integration insights, DIG axioms, spiritual insights and quotes are excluded.
- Each insight keeps its business point; the Bible reference is removed. The source files were attached in chat and are deliberately kept out of this repository.

Done:
- 154 slides across all 12 decks carry a "Professional insights:" block after the existing notes: a label, the insight (tightened to Carol's writing rules) and a "Source: Journal, <date> — Professional Insights: <category>" line. March entries carry no category ("Professional Insights").
- Content lives in `Unit decks\_build\enrich\u01.json` … `u12.json` (with a `_check` of each slide's opening text). `Unit decks\_build\enrich.py` applies them: `python3 enrich.py "<deck.pptx>" enrich/uNN.json`. Re-running replaces the block; slide XML is left untouched.
- After any rebuild with `unitNN.js`, run `enrich.py` on the new deck, or the insights are lost.
- QA passed: slide XML identical to the previous decks, original notes intact, pptx validator passed on all 12, notes scanned for contrast constructions, "lens" and US spelling, `node check_standards.js` reports "No breaches found".

## 9. Decks on the facilitator dashboard (1 October 2026)

- Carol's decisions: PowerPoint only; access by module (cohort_memberships.unit), since assignments are by module. Per-unit access would need a schema and admin-screen change later.
- Private Supabase bucket `facilitator_decks`, layout `Module-<1..4>/unit-<NN>.pptx` (capital M, as created in Supabase). SQL: `migrations/facilitator_decks.sql` (bucket, `can_read_facilitator_deck()` security-definer check, read policy). Facilitators read only their assigned modules; admins read all; uploads only through the Supabase dashboard.
- `dashboard_F.html`: a "⬇ Unit N deck (PPTX)" button beside each Manual link on the cohort card ([DECK] block); it creates a 5-minute signed link that downloads under the official file name.
- `_redirects` + `404.html`: block `Unit decks`, `Claude outputs`, `migrations`, `recovered-not-yet-deployed`, `.claude` and working files from the live site.
- When a deck changes: rebuild, run `enrich.py`, then re-upload it to its module folder in the bucket (overwrite).

## 10. Deck reader (1 October 2026)

- `deck_reader.html?unit=N`: in-portal reader for facilitators and admins. Slide image with full presenter notes below, Back/Next, slide jump, ⬇ PPTX button. Opened from "🖥 Read Unit N deck" on the cohort card.
- Present mode (`&mode=present`): opens a slide-only window for screen sharing; it stays in step with the reader (BroadcastChannel), arrow keys or click move both, Full screen button.
- Files: `Module-<m>/unit-<NN>/s01.jpg …` and `manifest.json` (titles + notes) in the `facilitator_decks` bucket; same module access rule. Built by `Unit decks\_build\reader_assets.py <out_dir> <deck.pptx …>` (LibreOffice render, 1600 px JPEG).
- When a deck changes: rebuild → `enrich.py` → `reader_assets.py` → re-upload the `.pptx` and the `unit-<NN>` folder.

- Carol's decision (1 October 2026): facilitators cannot download the PPTX. The storage rule refuses .pptx to facilitators; the download buttons show only to admins (dashboard admin view and the reader).

## 11. Live sessions: Teams link, calendar invite, recordings (2 October 2026)

- Carol's decisions: one entry per session (date, time, unit, Teams link); admin creates and sends; the cohort gets an email with a calendar file and a Join session button on the portal; a "will be recorded" tick; the recording link is added afterwards and is watchable by the whole cohort (participants and facilitators) and admin. The portal stores links only: Carol creates the meeting in Teams and the recording stays in OneDrive.
- Database: `migrations/cohort_sessions.sql` (table `cohort_sessions`, RLS read policy, six functions, and `log_activity` re-created with six session events added). Admin functions: `admin_save_cohort_session`, `admin_cancel_cohort_session`, `admin_delete_cohort_session` (unsent only), `admin_set_session_recording`, `admin_list_cohort_sessions`. Members: `get_my_sessions()`.
- Sending is publishing: a session shows to the cohort only once `last_sent_at` is set, which the email function does. Editing a sent session sets `changed_since_sent` and raises `ical_sequence` so the admin sends an update.
- Email: Edge Function `send-session-email` (source in `supabase/functions/send-session-email/index.ts`, deployed by pasting into Supabase). Body `{ session_id, kind }`, kind = invite | update | cancel | recording. Admin-only (checks the caller's profile). Uses the same secrets and sender as `send-invitation-email`: `RESEND_API_KEY`, `SB_SERVICE_ROLE_KEY`, `noreply@mail.ibsleadership.com`. One email per active cohort member, sent one after another; invite and update attach an `.ics` (METHOD:PUBLISH, UID = session id). Email text shows GMT+2 (`DISPLAY_OFFSET_MIN`, `DISPLAY_TZ_LABEL`); the calendar file converts for each person.
- `dashboard_A.html`: [SESSIONS] block after the 2FA modal (styles, three modals, script exposing `window.ibslSessions.mount(bundle)`), a `#cohortSessionsCard` placeholder above the danger zone in `renderCohortDetailHtml`, and one mount call in `renderCohortDetail`.
- `index.html` and `dashboard_F.html`: [SESSIONS] block before the main script (styles + `window.ibslLiveSessions.load()` / `.clear()`), a `#liveSessionsCard` (hidden until there is something to show), one call in `showPortal` / `loadFacilitatorCohorts`, and a clear on sign-out in `index.html`. Shows upcoming sessions with Join session, and recordings with Watch recording; "Recording to follow" shows for 14 days after a recorded session.
- `_redirects`: `/supabase/*` blocked from the live site.
- Tested with a mocked database in a headless browser (47 admin checks, 32 participant and facilitator checks, 29 email-function checks). Still to confirm live by Carol: the SQL run, the function deploy, one real send, and how the calendar file opens in Outlook.
- Known limits: admin "view as facilitator" shows no sessions (the admin is not a cohort member; use the cohort page). A cancellation email carries no calendar file, it asks people to remove the entry. Teams recording access for people outside the organisation has to be granted when sharing the recording.
