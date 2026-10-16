# Unit 9 · the two performance views — 16 October 2026 (PREVIEW stage)

Source: Carol's locks in `Claude outputs\Review files\Unit 9\Unit 9 two views - locked amendments.md` and her four texts (part 1.2 Seven Clog Map, Sections 3, 4 and 5), saved in the same folder. `s1.md`, `s3.md`, `s4.md`, `s5.md` are her docx files as markdown (pandoc -t markdown-smart); `gen_text.py` reads the clog cards and executive role cards into `u9pv_text.json`.
Base: the 13 October rework pages (`rebuild_u09\build_u09.py` on the 13 Oct backups; its PREVIEW copies match the 13 Oct PREVIEW files byte for byte).
Backups (16 Oct): `Claude outputs\Backups\Unit 9 file backups\… - before two performance views (16 Oct)` and `Unit 9 deck backups\Unit 09 - before two performance views (16 Oct).pptx` (cf941f0d…).

```
python3 ..\rebuild_u09\build_u09.py "<13 Oct backup p>" "<13 Oct backup f>" o13_p.html o13_f.html
python3 build_u09pv.py o13_p.html o13_f.html out\unit3_m2_lens8_p.html out\unit3_m2_lens8_f.html
python3 ..\rebuild_u09\make_previews_u09.py out\unit3_m2_lens8_p.html out\unit3_m2_lens8_f.html ..\rebuild_u09\mock-s2r-u9.js "<Review files>\Unit 9"
python3 test_u09pv.py "<Review files>\Unit 9"     (84 checks)
```

What changed: Facilitator Guide (reframe, two-sides paragraph, Clinic paragraph, two questions, one tone point); S1 guidance summarised, 1.1 additions + "Where clogs form", old 1.2 removed, new 1.2 Seven Clog Map (1.2.1–1.2.3, Closing Diagnostic Principle), ref2 prompt; S2 guidance question; S3 new (ten CXO cards, reflection ref7); S4 new (4.1–4.5, reflection ref8); S5 new (Strategic Unclogging Clinic 5.1–5.6, Capstone work, Confirm); COMPASS removed; Unit Summary; participant/facilitator voice.
Keys: KEYS ref1 ref2 ref3 ref4 ref7 ref8. Section 5: __uc_work, uc_record; Confirm writes uc_challenge, uc_clog, uc_lever, uc_review_realign, uc_restore and the names "Unclogging · Original Challenge / Performance Clog / Unclogging Lever / Review and Realign / Restore" (Capstone 9A–9E; five boxes as now, so no SQL).
Go-live (after her word): capstone_P.html PULL.u9 row and 9A–9E names/descriptions; dashboard_F.html labels for ref7, ref8, the uc_* keys; build_collection.js CAPSTONE_KEYS.u3m2_lens8; node build_collection.js; e2e; deck reader folder; check_standards.

## 16 Oct, afternoon — Carol's review notes, then "build live files including PPT"
- Sub-parts collapse (1.2 Understanding / Seven clogs / 1.2.1 / 1.2.2 / 1.2.3; 4.5 steps; 5.4 REVIEW / REALIGN / RESTORE).
- Facilitator page: the Section 3 and Section 4 reflection questions as tables (Section 4 by Review–Realign–Restore stage).
- Section 5: the Capstone Portfolio Output (what the group submits) moves before 5.1; 5.6 becomes "The Strategic Unclogging Clinic Record" (record + Confirm).
- Hidden reflection boxes ref2, ref7, ref8 sit next to their question so the Learning Portfolio finds it (27 prompts, 0 fallbacks).

Live (16 Oct): unit3_m2_lens8_p.html da8d1d85…, unit3_m2_lens8_f.html 7b142dcb…, capstone_P.html 8e5ee92a… (9A–9E renamed, PULL.u9), dashboard_F.html db4168de… (ref7, ref8, uc_* labels, map 7–8, family "The Strategic Unclogging Clinic"), build_collection.js 8e9f9ce9… (CAPSTONE_KEYS.u3m2_lens8), collection.html aa733af1….
python3 golive_u09pv.py <capstone_P> <dashboard_F> <build_collection.js> <out>   (from the 16 Oct backups)
Tests: test_u09pv.py 89/89; e2e_u09pv.py 24/24 on the real pages with rebuild_u06\fake-supabase.js (two controls); check_standards: no Unit 9 breach.
Deck: deck_u09pv.py on her deck cf941f0d… → 8a91b51d…, 31 slides; Unit decks and Deck upload\Module-3\unit-09.pptx identical; unit-09 reader folder: s01–s31 + manifest.json (reader_assets.py). Database: no SQL (Unit 9 keeps five boxes).
