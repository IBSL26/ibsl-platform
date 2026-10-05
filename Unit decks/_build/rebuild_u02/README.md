# Unit 2 rebuild — 5 October 2026

Source of the content: Carol's document "Unit 2 Rebuild _2026_10_05.docx".

| File | What it does |
|---|---|
| `common.py` | Shared wording: titles, section learning outcomes, the 14 elements and the SiP questions (from the S2R Strategy Architect tool v15), the four SiP domains, new CSS. |
| `build_f.py <old facilitator file> <new file>` | Builds the facilitator file. Unchanged blocks are cut from the old file byte for byte. |
| `build_p.py <old participant file> <new file>` | Builds the participant file ("you" voice). Run it from this folder: it reads `sec4_p.py` and `u2_tool.js`. |
| `sec4_p.py` | The fixed wording of participant Section 4. |
| `u2_tool.js` | The Section 4 tool: 14 elements (answer, generate, confirm or refine), Strategy Architecture output, Strategy Intent Statement, Success in Practice, printed reports. |
| `patch_dashboard_labels.py <dashboard_F.html> [--write]` | Adds report labels for the new response keys. Run it on the pre-rebuild dashboard file. |
| `make_previews.py <p> <f> mock-s2r.js <folder>` | Stand-alone PREVIEW copies that open by double-click (participant copy saves in the browser only). Never commit or upload them. |
| `page_pdfs.py`, `review_notes_make.js` | Earlier review aids (PDF pages, first review notes). |

Input for both build scripts is the file as it stood before the rebuild:
`Claude outputs\Unit 2 file backups\unit2_m1_lens1_[f|p] - before rebuild (5 Oct afternoon).html`.
The scripts are a record. Later edits to the two files are made directly, with exact replacements.

Response keys (lens_id `u2m1_lens1`, no database change needed):
- Section 4, Step 1: `arch_e01_q1` … `arch_e14_q4` (answers), `arch_e01_rs` … `arch_e14_rs` (what the element is saying; a refined position replaces the generated text), `arch_output`, `org_name`, `strategy_period`.
- Step 2: `intent_statement` (typed by the group). Step 3: `sip_d1_q1` … `sip_d4_q3` (answers), `sip_d1_st` … `sip_d4_st` (domain statements written by the group).
- `confirmed_items`: list of confirmed names ("Element 4 · WHAT", "Strategy Architecture", "Strategy Intent Statement", "SiP · <domain>", "Success in Practice").
- Section 5: `appSIP_<ROLE>_d1` … `d4`, `col_alignment`, `col_gaps`, `col_tensions`, `col_ownership`, `app_app_ref_final`.
- Reflections: `ref1`, `ref2`, `ref6`, `ref4`. (3.2 Flammables is teaching content only; the Portfolio Artefact and the Integration Synthesis part were removed on Carol's instruction.)
- No longer written by the page (old answers stay in the database and keep their labels): `ref3`, `ref5`, `ref7`, `flam_0` … `flam_3`, `port1` … `port3`, `sip_integrated`, `assessment`, `sip_data`, `app_app_cor_d1` … `d4`, `app_app_headline`, `app_app_storyline`, `app_app_convergence`, `app_app_tension`, `app_app_missing`, `app_app_bias`.

Differences from the Strategy Architect tool, on purpose: Define mode only (no Stress-Test mode); "Element n of 14"; a refined position flows into the Strategy Architecture output; **no automation of the Strategy Intent Statement or the SiP statements (Carol, 5 Oct: participants deduce and write them; do not mention the automation on the pages)**; the four-statement SiP shows the confirmed statements; the printed Architecture follows the group's edited text; organisation and period print on the reports; IBSL green and gold.

Carol's instructions of 5 October (evening), all built in:
- **Group work:** the group agrees each entry and one member acts as scribe; every member then types the agreed entries into their own portal page, in the session or after it. No shared-team mechanism. No pre-work before a session.
- **Locks:** only the Strategy Architecture output waits (14 of 14 confirmed). 4.2 and 4.3 are open from the start. 4.3 was unlocked by extension of her 4.2 instruction; reverse it if she says so (`renderSip()` in `u2_tool.js`).
- **Times:** none anywhere in the facilitator file. `T()` returns nothing and `build_f.py` strips the time lines carried over from the old file, then fails the build if a time is left.

Carol's instructions of 5 October (night):
- **Section 2 title** is "The Importance and Relevance of SiP" (`common.py`, `HERO`).
- **Capstone Blueprint aligned with Unit 2.** `patch_capstone.py <capstone_P.html of 28 Sept> <new file>` rewrites the Unit 2 boxes (2A Strategy Architecture, 2B Strategy Intent Statement, 2C to 2F the four SiP statements; maturity gaps, SiP Headline and SiP Storyline removed) and adds the bring-in: the confirmed outputs are read from the member's own Unit 2 answers (`arch_output`, `intent_statement`, `sip_d1_st` … `sip_d4_st`, checked against `confirmed_items`). The `PULL` table in the page takes further units as they are rebuilt. Input: `Claude outputs\Unit 2 file backups\capstone_P - before Unit 2 alignment (5 Oct night).html`.
- **Database step:** `Claude outputs\capstone_unit2_boxes.sql` (box count for Unit 2: 8 to 6). Without it, "Send for team confirmation" answers "Complete every box".
- `make_cap_preview.py <capstone_P.html> mock-supabase-capstone.js <output>` makes `PREVIEW - Capstone.html` (sample team, sample text, nothing saved). Never commit or upload it.
- 4.3 of both unit files carries one paragraph on the Capstone (`sec4_p.py`, `build_f.py`).
