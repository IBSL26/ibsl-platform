# S2R Portal Standards

Agreed rules for every file, deck and change in this folder. Read this before any work.
Run `node check_standards.js` before every commit: it tests rules 1–8, 11, 12 and 16 and lists every breach.

## Structure and labels (all 24 unit files, participant and facilitator)

1. Units are "units". Never "lens" or "lenses" to mean a unit — in any file, deck or message.
2. Section tabs read "Section N / Name / Anchor"; headings read "Section N · Name — Anchor":
   Awareness — What · Intelligence — Why · Extrapolating — Where · Integration — Collective · Application — In Practice.
   Unit 1 adds "Orientation — Overview" as Section 1. "Integration Zone" and "Integrating" are not used.
3. Next and back buttons read "Section N — Name →" and "← Section N — Name".
4. Every facilitator file opens with a Facilitator Guide tab (Unit Intent, Key Facilitation Questions, Tone & Watch Points); Section 1 has "← Facilitator Guide".
5. Top bar: "Module N · Name" first, then "Unit N · Title — Participant / Facilitator". The line above the title reads "Module N · Name · Unit N". The badge reads "Participant View" / "Facilitator View".
6. Every unit closes with "Unit Summary". "Unit Close" and "Micro-Climb Summary" are not used.
7. Facilitator guidance labels read "FACILITATOR GUIDANCE".
8. Portfolio blocks are named "Portfolio Artefact".
9. Participant and facilitator files carry identical section and part numbering.
10. Facilitator files are preparation-only: no entry fields, nothing saved. Where an activity was removed, a "Participant activity" note appears.

## Wording

11. British spelling throughout.
12. The brand is "Strategy2Results®".
13. No "not X — it is Y" constructions. Tight, functional copy.
14. Key learning outcomes are action-verb capability statements; they never name the tool or how the concept is delivered.
15. Two learning outcomes per section, aligned with the unit's Key learning outcomes and faithful to what the section teaches.

## Unit decks (folder "Unit decks")

16. Minimum 24pt for every piece of text on a slide.
17. IBSL forest green and gold, with the IBSL seal on the title slide.
18. Section labels on slides match the portal; facilitator guidance goes in the speaker notes.

## Working rules

19. No change without Carol's approval; find and propose all changes in one pass.
20. Claude never runs git. Carol commits in PowerShell.
21. Preserve file format (CRLF line endings, UTF-8); back up before editing.
22. Never change IDs, lens_id / data-lens-id values, links, lock logic, scoring or database calls unless the build requires it and Carol has approved.
23. After every change, verify: counts of id / onclick / href / lens_id against the backup, `<div>` balance, syntax check of every inline script, a browser run, a phone screenshot.

## Open decision

- Units 2 and 4 call the four ABCV elements (Arena, Boundaries, Competition, Value Proposition) "lenses". Decide whether rule 1 also covers this, with "checkpoint" as the replacement. Until decided, the check script reports these separately and does not count them as breaches.
