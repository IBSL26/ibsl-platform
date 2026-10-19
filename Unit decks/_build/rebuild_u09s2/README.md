# Unit 9 · Section 2 rework (19 Oct 2026, PREVIEW stage)
Carol's instructions of 19 Oct 21:04–21:29; record in `Claude outputs\Review files\Unit 9\Unit 9 two views - locked amendments.md` (last section).
Wording: `u9s2_content.py`. Surgical build on the live pages (19 Oct backups: `Claude outputs\Backups\Unit 9 file backups\… - before Section 2 rework (19 Oct).html`).
```
python3 build_u09s2.py ..\..\..\unit3_m2_lens8_p.html ..\..\..\unit3_m2_lens8_f.html out\unit3_m2_lens8_p.html out\unit3_m2_lens8_f.html
python3 make_previews_u09s2.py out\unit3_m2_lens8_p.html out\unit3_m2_lens8_f.html ..\rebuild_u09\mock-s2r-u9.js out\preview
python3 test_u09s2.py out ..\..\..\unit3_m2_lens8_p.html ..\..\..\unit3_m2_lens8_f.html   (139 checks, static + node --check)
node js_u09s2.js out\unit3_m2_lens8_p.html                                              (10 checks of the 5.1 drop-downs; fails on the live page = control)
```
The device shell has no browser and no network: checks are static (bs4) plus the page script run in node with a stand-in page. Browser checks go on the live site after the push.
