# Unit 1 part 6.2 · The Problem Charter (19 October 2026)

Carol (16:01): "each group will have its own simulated company name. Add a space for simulated executive teams for upto 10 but can be less. Build the problem charter".

- `build_pc.py <in> <out>`: builds unit1_P.html, unit1_F.html, capstone_P.html, dashboard_A.html, dashboard_F.html, build_collection.js from the files before (backups in `Claude outputs\Backups\Problem Charter 19 Oct`).
- `pc_p.js`, `pc.css`, `pc_f.css`: the participant tool and styles written into the pages.
- `e2e_pc.py <site> <fake-supabase.js> [shots]`: end-to-end test with `rebuild_u06\fake-supabase.js` (30 of 30 pass; the control with the old capstone page fails).
- Database: `Claude outputs\capstone_unit1_charter.sql` (Blocks 0 to 9, tested in pglite).

Keys (lens `u1_foundations`): `__pc_work`, `pc_record` while the group works; on Confirm `pc_company`, `pc_team`, `pc_org`, `pc_reality`, `pc_challenges`, `pc_manifest`, `pc_consequences`, `pc_capabilities`, `pc_shared`, `pc_problem`, `pc_sources` and eleven "Problem Charter · …" names in `confirmed_items`. Capstone section `u1`, boxes 1A to 1K; box 1A (the simulated company name) replaces the cohort case name as [Case] everywhere on the Capstone page. The cohort brief no longer has a Case field.

Not done yet: Unit 1 deck slide for 6.2; read-only Charter line in Units 2 to 12; Unit 2 rework (Section 4 worked example, Section 5 capstone build).
