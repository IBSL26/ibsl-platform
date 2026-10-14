# Unit 7 · the two performance views — 14 October 2026 (PREVIEW stage)

Source: `Claude outputs\Amended Unit Content\Unit 7 Amended content.docx` (her save of 21:37) and her words (21:39): "minor changes which just include the reference to the human and organisation performance, the rest remains pretty much the same - make sure it is coherent do not just add".

Inputs: the live pages (backups `Claude outputs\Backups\Unit 7 file backups\… - before two performance views (14 Oct)`) and her deck (backup `Unit 7 deck backups\Unit 07 - before two performance views (14 Oct).pptx`, md5 f4814297…).

```
python3 build_u07pv.py <live p> <live f> out_p.html out_f.html
python3 make_previews.py out_p.html out_f.html mock-s2r.js "<Review files>/Unit 7"   (the mock-s2r.js of THIS folder: it holds a Unit 6 Contribution Map sample)
python3 deck_u07pv.py "<her deck>" "<Unit decks>/Unit 07 - Establishing Performance Expectations.pptx"
```

What changed: header (Unit purpose, four Key learning outcomes, facilitator sub-title); section outcomes (two each; S4 outcome 1 = coaching outcome, S5 without tool name); 1.1 two-view paragraph + cards + table row "Enabling conditions"; 1.2 her rewritten part (three condition cards across both operating systems, Key principle); 1.3 Upline/Downline/Crossline with "What must be established", Critical Distinction; External → Crossline everywhere (3.1 role chains: new Crossline lists); 1.4, 2.1, 2.3, 3.1 two-view sentences; old 4.1 (four-step architecture, ref7) removed — 4.2 is now 4.1; KEYS without ref7; Section 5 · 5.1 on two contributions of the group's Unit 6 Contribution Map (reads u3m1_lens5 `__cm_work` once confirmed_items holds "Enterprise PM System · Contribution Map"); Step 2 people + ESRG boxes; Step 3 Crossline; 5.2 unchanged. Summary cards 1, 4, 5 (participant), 5 (facilitator).

Keys (u3m1_lens6): `__ex_work` per contribution `o1_`/`o2_`: fn, obj, kr (from the map), sipst, owner, sip, frame, what, when, std, evid, beh, env, sys, res, gov, up, up_r, down, down_r, cross, cross_r, coord, score, concern, act, score2; dg_*. Confirm writes ex_future, ex_delivery, ex_chain, ex_ownership, ex_dialogue (unchanged names; Capstone 7A–7E stays 5 boxes, no SQL).

Deck: 23 slides (old slide 19 "4.1 four-step" removed); slide texts changed only on 1, 2, section slides, 6 (1.2 cards), 7 (Crossline), 20 (4.1), 21 (Section 4 · Portfolio work), 23 (5.1); notes keep her wording with the two-view content added; 1.2, 1.3, 21, 23 notes rebuilt from the pages.

Go-live (after her word): live pages; capstone_P.html PULL.u7 labels (Objective → Contribution), dashboard_F.html labels for the new keys and ref7 gone, build_collection.js check, e2e test, deck reader folder (s19 removed, pictures renumber), check_standards.

## Live (14 October 2026, 22:10) — Carol: "Happy for us to commit to live files"
- Written: unit3_m1_lens6_p.html 01e70358…, unit3_m1_lens6_f.html 0edc101c…, capstone_P.html f0c01984… (7A–7D descriptions: two contributions, people + ESRG, Crossline, owner and review date; PULL.u7 unchanged), collection.html 497c03b8… (node build_collection.js; Unit 7: 67 prompts, 0 fallbacks). dashboard_F.html and build_collection.js unchanged (keys unchanged; old ref7 label kept for old answers).
- Deck: Unit decks and Deck upload\Module-3\unit-07.pptx identical (97687ee7…, 23 slides); unit-07 folder: s01–s23 + manifest.json; old s24.jpg moved to Claude outputs\_to_delete\unit-07 old.
- Tests: e2e_u07pv.py 39/39 on the real pages with rebuild_u06\fake-supabase.js (two controls). check_standards: no Unit 7 breach.
- Database: no SQL (Unit 7 keeps 5 boxes).
- For Carol: commit and push; Storage: replace unit-07.pptx, upload s01–s23 and manifest.json into unit-07, delete s24.jpg there.
