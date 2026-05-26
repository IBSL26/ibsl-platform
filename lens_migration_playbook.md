# Lens Migration Playbook — v2
*Canonical process for migrating an IBSL/S2R "CESI" lens. v1 was derived from Unit 2 · Module 1 · Lens 1. v2 folds in everything standardised through the Lens 3 migration (schema design, the submission cluster, the Submit button, accordion collapse, navigation, the team/executive identity pattern, and the build/verify method). Read this with the handover notes before touching files.*

---

## 0. Canonical references & environment
- **Standard participant reference:** any migrated `unit2_m1_lens<N>_p.html` (L1, L2, L3 all now carry the same submission cluster + Submit button). Lens 3 is the most complete worked example, including a from-scratch schema and a group exercise.
- **Standard facilitator reference:** `unit2_m1_lens<N>_f.html` (Migration Lite).
- **Dashboard:** `dashboard_F.html` (~7,100+ lines; one dashboard reviews every lens).
- **Repo / live / backend:** `github.com/IBSL26/ibsl-platform` · `ibslportal.netlify.app` (Netlify, GitHub CD) · Supabase `https://tayrxqbrttlrdowrzobm.supabase.co`.
- **Build/verify env:** bash is `/bin/sh` (NO `<(...)` process substitution — use temp files). The filesystem resets between sessions, so re-copy from `/mnt/user-data/uploads` and `/mnt/user-data/outputs` at the start of each chat. Verify JS by extracting inline `<script>` blocks and running `node --check`.

---

## 1. What is shared — VERIFY, do not rebuild
These are one-time, lens-agnostic pieces. For a new lens you only confirm they still exist; you never rebuild them.
- `mark_lens_submitted` trigger — fires on every `submissions` insert, cohort-scoped. **It only advances a `lens_progress` row already at `unlocked`/`in_progress`/`submitted`. A row still at `locked` STAYS `locked` (grey on the dashboard) — a participant submit does NOT unlock a lens.**
- **UNLOCK CHAIN (critical — how a lens goes `locked` → `unlocked`):** the NEXT lens unlocks only when the predecessor's submission is **REVIEWED by a facilitator** (`review_submission` with `unlock_next`), **not** on participant submit. Two consequences: (a) the new lens's `lens_catalog` row must exist **before** a participant submits its predecessor (else the unlock has no target and the row is later seeded `locked`); (b) during testing you must **complete the facilitator review of the predecessor** to unlock the next lens. **Never edit `mark_lens_submitted` or the unlock/review functions to force this — flag it.**
- `review_submission` — cohort-scoped; shared by all lenses; **this is what unlocks the next lens.**
- `return_for_revision` — shared; writes `facilitator_feedback`, leaves the lens at `submitted`.
- `dashboard_F.html` — one dashboard reviews every lens. The committed-feedback prefill, blank-commit guard, and admin auth-guard fix already protect all lenses.
- `s2r-save.js` (served at `/s2r-save.js`) — provides `S2R.save`, `S2R.submit`, `S2R.loadAll`, `S2R.context`, `S2R._client`. **It IS in the repo working copy** (correcting an earlier note) — `S2R.save` upserts `lens_responses` on `(profile_id,lens_id,response_key)`; `S2R.submit` is a plain `INSERT` into `submissions` (`review_status:'submitted'`) with **no unlock logic** — all advancement/unlock is DB-side. Identical for every lens.

So per-lens **database** work is minimal: a `lens_catalog` row + the unlock chain (Phase 4).

---

## 2. THE STANDARDS (what "consistent across lenses" means concretely)

### 2.1 `lens_id`
- Convention: **`u<unit>m<module>_lens<N>`** (e.g. `u2m1_lens3`, `u3m1_lens5`) — the prefix matches the file's unit/module. It must match between every query in the files and the DB.
- It lives in the DB as `submissions.lens_id` (the dashboard reads `r.lens_id` straight from the DB). **The `lens_catalog` primary-key column is `id`, NOT `lens_id`** — `submissions.lens_id` references `lens_catalog.id`. **Confirm the exact string with the user** before building.

### 2.2 Response-key schema (the part v1 didn't cover)
Lenses do **not** all arrive with persistable fields. A lens may ship with cosmetic "Save" buttons (flash "Saved ✓", persist nothing), no `id`s, and an old access-code gate. When that happens you must **design the response-key schema from scratch**. These keys become **permanent DB keys** — renaming later orphans existing submissions (see gotchas). Decide deliberately, then never rename.

Naming conventions established so far (reuse them; the dashboard already understands some):
| Field kind | Key pattern | Example | Dashboard label |
|---|---|---|---|
| Reflection / commitment textareas | `ref1`, `ref2`, … | `ref5` | "Reflection N" *(auto — already mapped)* |
| Portfolio notes | `port1`, `port2`, … | `port3` | "Portfolio note N" *(auto)* |
| Grouped conceptual set | `<prefix>_<member>` (flat) | `mbt_arena`, `mbt_bound`, `mbt_comp`, `mbt_value` | per-key label + a family |
| Working-paper / synthesis | `syn_*`, `own_*` | `syn_themes`, `own_timeline` | per-key label + "Working Papers" family |
| Team / executive identity | `team_name`, `exec_name`, `exec_role` | — | "Team & Executive Identity" family |

**Persisted vs local-only.** Persist the fields the facilitator needs to review (reflections, synthesis outputs, identity/attribution). Leave genuine in-room working scaffolds **local-only** (e.g. dynamically-added objective cards, scored self-check games) unless the user wants them captured — capturing variable-length dynamic rows means serialising them into a single JSON key, a larger change to flag explicitly. Document which is which.

### 2.3 Save mechanism (every persisted field)
Each persisted field gets three things:
1. a stable `id`,
2. the `reflection-textarea` class (this is what the autosave listener keys on), and
3. a sibling status div: `<div class="ref-saved reflection-saved" id="<id>-saved"></div>`.

Wiring (copy verbatim; broadened to cover `<input>` and `<select>`, e.g. an executive-role dropdown):
```js
document.querySelectorAll("textarea.reflection-textarea, input.reflection-textarea, select.reflection-textarea")
  .forEach(function(el){
    if(!el.id)return;
    el.addEventListener("input",function(){draftRef(el.id);});
    if(el.tagName==="SELECT")el.addEventListener("change",function(){saveRef(el.id);});
  });
```
- `draftRef(id)` debounces (~1.2s) → `saveRef(id)` → real `S2R.save('<lens_id>', id, value)` with the true "Saved to your portfolio" / retry-on-failure status. **Autosave must actually persist** — never a visual-only "Draft saved".
- Manual "Save" / "Save Notes" buttons call `saveTA(btn)`, which group-saves every reflection field inside the button's container (`.ref-block` / `.step-panel`):
```js
function saveTA(btn){
  var box=btn.closest(".ref-block")||btn.closest(".step-panel")||btn.parentElement;
  var fields=box?box.querySelectorAll("textarea.reflection-textarea[id], input.reflection-textarea[id], select.reflection-textarea[id]"):[];
  fields.forEach(function(ta){saveRef(ta.id);});
  /* … 2s "Saved ✓" affordance … */
}
```
- On load, restore via `S2R.loadAll('<lens_id>')` into a `KEYS` array that **lists every persisted id**, then call `loadSubmissionFeedback()`.
- **Labelled score grids / dropdowns (e.g. a FACES or EXECUTION 1–5 self-score) must be UI-only and serialise into the SAME existing key.** Never give the per-row controls a persisted `id` or the `reflection-textarea` class (that mints new keys). Keep one hidden canonical `<textarea id="<key>" class="reflection-textarea">` holding the serialised string; a `syncScores`/`hydrateScores` pair writes it via the existing `saveRef` and re-populates on load (preserving any prior free-text value via an old-format fallback). Do **not** touch `S2R.save`/`submit`/`lens_id`/`KEYS`. Verify with a serialise↔hydrate **round-trip + old-format hydrate** check before deploy.

### 2.4 The submission cluster (the "interaction format" — IDENTICAL on every lens)
At the end of the **final Application tab**, in this exact order:

> application reflection → **Micro-Climb Summary** → **Facilitator Feedback** → **Messages** → **Supporting Documents** → **Submit to Facilitator** button → tab nav

Rules:
- The Micro-Climb Summary accordion is the participant's standardised closing summary (container `#summaryP`, rendered by `renderSummaryP()`).
- Facilitator Feedback / Messages / Supporting Documents are the C1 / C5 / C6 accordions (hidden until a submission exists; revealed by `loadSubmissionFeedback`). The feedback loader is **always-visible state** + `.limit(20)` + the "· revision resubmitted" flag.
- **No submitted field may be buried inside a collapsed accordion.** If a closing-commitment / reflection field sits inside a collapsible recap, lift it OUT to an always-visible block before the Micro-Climb Summary. (This bit us on Lens 3 — `ref5` was hidden inside the Chapter Summary.)

### 2.5 The Submit button (byte-identical on every lens)
**Standard = full-width inline `.send-btn`. NOT a floating action button (`send-fab`).** L1 originally shipped a FAB; it was converted. Verify each new lens uses exactly this:
```html
<div style="padding:20px 0 10px;">
  <button class="send-btn" onclick="sendToFacilitator()">
    <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
    Submit to Facilitator
  </button>
</div>
```
```css
.send-btn{width:100%;padding:14px;background:rgba(26,122,106,.1);border:1px solid rgba(26,122,106,.3);border-radius:3px;color:var(--teal);font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px;}
.send-btn:hover{background:rgba(26,122,106,.2);}
.send-btn svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2;}
```
`sendToFacilitator()` confirms → `S2R.submit('<lens_id>')` → on success re-runs `loadSubmissionFeedback()`. Remove any FAB markup/CSS and any caption that points to a "bottom-right" button.

### 2.6 Accordion collapse (display-based — the robust standard)
Use **display-based** collapse, not a `max-height` transition. The `max-height:9000px` slide lags badly on tall content (clicking close does nothing for ~⅓ s, then snaps, leaving content bleeding mid-animation).
```css
.acc-b{display:none;overflow:hidden;}
.acc.open .acc-b{display:block;}
```
Keep `.cb{padding:…}` for inner padding and the chevron rotate on `.acc.open .arr svg`.

### 2.7 Navigation uniformity (start = end)
The top-nav back control and the final-tab back control must be uniform within a lens:
- **Participant:** "← Back to Platform", `goBack()` → `index.html`.
- **Facilitator:** "← Back to Dashboard", `goBack()` → `dashboard_F.html`.

### 2.8 Group / collective-intelligence exercises (when a lens has one)
If a lens contains a team/consensus exercise:
- Frame it explicitly as a **team exercise** for collective intelligence (individual work first, then consolidate as a team).
- Provide a **shared case study** so everyone analyses the same scenario (a concise default is fine; mark it clearly so the user can paste their canonical case).
- Capture **team + executive identity** for facilitator attribution: `team_name`, `exec_name`, `exec_role` (role = a C-suite `<select>`).
- **Remove participant-inappropriate prompts** — anything a single participant cannot answer alone (e.g. "Which conditions appear in multiple participants' papers?").

---

## 3. THE MIGRATION PROCESS (follow in order for each upcoming lens)

### Phase 0 — Pre-flight
- [ ] Confirm **which lens** and its exact **`lens_id`** (`u2m1_lens<N>`) with the user.
- [ ] Get the lens's `_p.html` + `_f.html` (and ideally a sample submission).
- [ ] Note the **tab structure**: number of module tabs and which is the final Application/doing tab. Count the content **arcs** (exclude any intro tab and the final Application tab) — that's the number of Micro-Climb summary blocks (L1/L2/L3 = 4).
- [ ] Inspect the participant file: does it already persist fields, or ship cosmetic saves + an old gate? Decide whether you're doing a mechanism-copy or a from-scratch schema (§2.2).

### Phase 1 — Summaries (the real human work)
- [ ] Read the actual teaching content of each arc; write a summary per arc (~600–950 chars), naming only the **real frameworks** from the lens.
- [ ] Title pattern: "What Was Established / Why It Matters / Where … Appears / What Was Built", arc labels "Awareness — What / Intelligence — Why / Extrapolating — Where / Integration — Collective".
- [ ] Same content goes in both files (participant `renderSummaryP`/`#summaryP`; facilitator keeps its own Chapter Summary if it already has complete recap content).

### Phase 2 — Participant page (~90% of the work)
- [ ] **Schema:** assign permanent keys to every persisted field (§2.2); give each `id` + `reflection-textarea` class + `-saved` sibling.
- [ ] **Head:** add `@supabase/supabase-js@2` + `/s2r-save.js`.
- [ ] **Save mechanism (§2.3):** S2R `SUMMARY` + `renderSummaryP`, the autosave chain, `saveTA` group-save, `loadAll` restore (`KEYS` lists every id), `loadSubmissionFeedback`/`showFeedbackState`/`renderSubmissionFeedback`, the generic messages + documents block (port verbatim; only the log prefix changes), `renderSignedInBadge`, `sendToFacilitator`.
- [ ] **Cluster (§2.4):** place application reflection → Micro-Climb → Feedback → Messages → Documents → Submit → nav, in that order; lift any submitted field out of collapsibles.
- [ ] **Submit button (§2.5), accordion collapse (§2.6), nav (§2.7).**
- [ ] **Group exercise (§2.8)** if applicable.
- [ ] Remove the old access-code gate, `localStorage` drafts, scroll-lock, and any `mailto`/FAB.
- [ ] Add the signed-in badge `<span id="signedInBadge">` to the participant nav.

### Phase 3 — Facilitator manual (Migration Lite)
- [ ] Add `@supabase/supabase-js@2` + a `checkAccess()` IIFE: `getSession` → no session = redirect `index.html`; read `profiles.role`; **admin passes**; non-facilitator = redirect; facilitator gated by `can_facilitate_lens(p_user_id, p_lens_id=LENS_ID)`; denial shows `#f1-gate-overlay`. Set `const LENS_ID = '<lens_id>'`.
- [ ] Nav badge → **"Facilitator View"**; back navigation → `dashboard_F.html` (§2.7).
- [ ] Remove old access-code overlay, scroll-lock, and any `exportEmail()`/`mailto`.
- [ ] **No** S2R save/submit and **no** dynamic signed-in badge (review happens in the dashboard). Keep the facilitator's existing Chapter Summary content.

### Phase 4 — Database (USER runs the SQL) — **usually DISCOVERY-ONLY**
- [ ] Catalog rows are normally **pre-created**. Run a read-only `SELECT` to confirm the row exists and is correct: `select * from lens_catalog where id in ('<new>','<predecessor>');` (PK column is **`id`**). **Do NOT insert or repoint unless the SELECT shows something actually wrong.**
- [ ] `requires_lens` points **BACKWARD to the prerequisite**: the chain is driven by the **new lens's** `requires_lens = its predecessor` (e.g. `u3m1_lens5.requires_lens = u3m1_lens4`) — and it's normally already set. Do **not** repoint the predecessor (that creates a cycle). One row per successor (two pointing at the same predecessor trips `ambiguous_successor`).
- [ ] **Facilitation is unit/cohort-scoped** via `can_facilitate_lens` — **no per-lens facilitator assignment** needed; a facilitator assigned to the unit already covers the new lens.
- [ ] No new trigger/function — they're generic. **Never edit the core DB functions to work around a problem — flag it.**
- [ ] If the new lens won't unlock, it's the **unlock chain** (§1), not a missing row: the catalog row must exist *before* the predecessor is submitted, and the predecessor must be **reviewed** to unlock the next lens.

### Phase 5 — Dashboard (`dashboard_F.html`)
- [ ] **Labels:** in `humanizeFieldName`, add `if (/^<key>$/i.test(s)) return '<Label>';` for each new key, **before** the title-case fallback. (`ref\d+`/`port\d+` are already mapped.)
- [ ] **Families:** in `FAMILY_DEFS`, add `{ name:'<Section>', test:function(k){ return /<pattern>/i.test(k); } }` for each new group. Keep the numeric-module filter `.filter(k => /^\d+$/.test(k))` intact. Families established: Reflections, Portfolio, Objectives & Key Results, KISS Mapping, SiP, Application, **MBT Conditions**, **Working Papers**, **Team & Executive Identity**.
- [ ] Deeply-nested keys (object values) → a special-case branch in the NAMED FAMILY render pass.
- [ ] **Live flag:** flip the lens in `LENS_MANUAL_MAP` to `live: true` — **only after** the facilitator manual is migrated.

### Phase 6 — Verify
- [ ] **Assistant (static):** extract inline `<script>` blocks → `node --check`; div-balance sanity (`<div` count == `</div>`); cross-file `lens_id` alignment; confirm every persisted key has `id` + `reflection-textarea` + is in `KEYS`; simulate `humanizeFieldName`/`familyOf` over the new keys; for any labelled score field, a serialise↔hydrate **round-trip + old-format hydrate** check.
- [ ] **User (live two-window loop):** facilitator (normal) + participant (incognito). Badge shows the right role and is not red. Submit → Return for revision → resubmit (feedback persists, "· revision resubmitted") → Mark reviewed & unlock. Confirm correct cohort and that new keys land under the right dashboard headings. **Note the unlock chain (§1): the NEXT lens turns from grey only after the facilitator REVIEWS the predecessor — not on submit — and only if the new lens's catalog row existed before that submit.**

### Phase 7 — Deploy (only after explicit user OK on the push)
- [ ] **`gh` is NOT installed — no pull requests.** Deploy by: `git checkout -b <branch>` → `git add <files>` → `git commit` → `git checkout main && git merge --ff-only <branch> && git push origin main` (Netlify CD builds from `main`).
- [ ] Deploy **all touched files together** + **hard-refresh (Ctrl+Shift+R)**. Confirm the live site is not **Paused** first.

---

## 4. Build method (how the assistant should actually edit)
- **Working cadence:** run read-only investigation, builds, and file edits **straight through**; **stop only for (a) data-changing SQL and (b) git push/merge** — each needs explicit user approval, and SQL is drafted for the user to run (the assistant has no DB connection). Read-only `SELECT`s and repo investigation need no permission. **Never edit core DB functions to work around a problem — flag it.**
- Prefer a **re-runnable Python builder with assertions** over fragile sequential edits: every transform asserts its anchor exists and is unique, so drift fails loudly instead of producing a broken page. Operate on a working copy; write the result to `/mnt/user-data/outputs/`.
- Port generic blocks (messages/documents) **verbatim**, changing only the log prefix and `lens_id`.
- Use the literal `·` character (not a `\u00b7` escape) in source to avoid escaping pitfalls.
- Re-copy inputs from uploads/outputs at the start of each session (filesystem resets).

## 5. What the assistant can and cannot certify
- **Can:** JS validity (`node --check`), structural well-formedness, internal consistency (save/restore/feedback/submit all bound to the same `lens_id` and ids), label/family resolution, byte-parity of standard blocks across lenses.
- **Cannot (needs the user's live test):** the actual DB round-trip; the exact `S2R.submit` payload shape (`s2r-save.js` isn't in the working copy); the `can_facilitate_lens` gate (needs the `lens_catalog` row + facilitator assignment). Division of labour: **the assistant builds the backend; the user runs the loop that validates it.**

## 6. Gotchas (v1 + new)
1. **Deploy all touched files together + hard-refresh.** Stale deploys repeatedly looked like "my code is broken" when it wasn't.
2. **Netlify "Paused":** a Paused project doesn't publish new builds (usually a usage/credit limit). Un-pause before debugging "changes not showing".
3. **Permanent keys:** once a field is named and data is saved, **never rename it** — it orphans existing submissions. Choose schema keys deliberately in Phase 2.
4. **No submitted field inside a collapsed accordion** (§2.4) — participants can't reach it.
5. **Accordion collapse must be display-based** (§2.6) — `max-height` slide lags/bleeds on tall content.
6. **Submit button is the inline `send-btn`, never a FAB** (§2.5).
7. **Resubmission creates a NEW `submissions` row;** continuity is patched client-side in the dashboard (a fully robust fix belongs at the DB/RPC layer).
8. **One successor per lens** in `requires_lens` (else `ambiguous_successor`).
9. **Login confusion** (facilitator vs participant): the participant signed-in badge flags it (red when role ≠ participant) — check it first.
10. **Draft ≠ sent:** typing feedback only autosaves a draft; the facilitator must click Return/Mark-reviewed to send it.
11. **`saveApp()` quirk (Lens 1):** prepends `app_` to ids already starting with `app_` → stored keys are `app_app_*`. Don't "fix" the names (orphans data) — map them in the report.
12. **A lens unlocks on facilitator REVIEW of its predecessor, not on participant submit** (§1). `mark_lens_submitted` won't advance a `locked` row. Ensure the new catalog row exists *before* the predecessor is submitted, and review the predecessor to unlock the next lens during testing.
13. **`lens_catalog` PK is `id`, not `lens_id`**, and rows are usually pre-created — Phase 4 is discovery-only (`SELECT` to confirm; don't insert/repoint unless something's wrong).
14. **Never edit core DB functions** (`mark_lens_submitted`, the unlock/review functions) to work around a problem — flag it.
15. **Score grids/dropdowns serialise into the existing key** — never mint new response keys; verify a round-trip + old-format hydrate before deploy (§2.3).
16. **`gh` is not installed — no PRs.** Deploy via branch → commit → `git checkout main && git merge --ff-only <branch> && git push origin main`.

## 7. Parked work (do AFTER the lens migrations, unless reprioritised)
- **Full Facilitator Cohort Report** (the main deferred feature): Phase 1 Cohort Progress matrix → Phase 2 Lens Synthesis ("one question → every participant's answer", reusing `humanizeFieldName` + `FAMILY_DEFS`) → Phase 3 Collective-Intelligence insights + exportable deliverable. Tech shape: a Supabase RPC `get_cohort_submissions(cohort_id, lens_id)` (facilitator-RLS scoped) + a "Cohort Report" button on the roster. Build Phase 1+2 first (~80% of value, mostly reuses existing code).
- **Per-lens "show the actual question prompts" in the dashboard report** — fold into a batch pass.
- **Optional:** capture group-exercise working scaffolds (dynamic objective/ownership rows) if the user wants the individual working papers reviewable — means serialising variable rows into a JSON key per lens.
- **Cosmetic parity:** L2's cluster bodies use bare `.acc-b`; L3 uses `.acc-b cb` (slightly more padding). Functionally identical; left as-is unless pixel-parity is requested.
