# Capstone · fit with the Problem Charter guide

Check of 13 October 2026. Read-only: no file was changed.
Read: `Claude outputs\Capstone\CESI_S2R_Problem_Charter_Participant_Guide.docx`, `capstone_P.html`, the Capstone views of `dashboard_A.html`, `Claude outputs\capstone_blueprint.sql`, and the participant pages of Units 1 to 8.

## 1. What the guide asks

1. Groups of seven, by sector (four groups listed).
2. Before CESI: each participant brings examples from their own work. No group meeting.
3. During orientation: each group creates one fictional organisation, writes its Problem Charter (sections A to E, 2–3 pages) and acts as its executive team.
4. The Capability Blueprint is then built one section at a time, as each unit is taught.
5. At the capstone the group presents and defends its integrated response as that organisation's executive team.

## 2. What already fits

- **One Blueprint section per unit.** Each section opens once every member of the team has completed its unit.
- **Group work on the group's own strategy.** Units 5 to 8 work on "the strategy in your team's Capstone Blueprint", with no set case in any group exercise. Unit 2 builds the Strategy Architecture from a blank page, with an "Organisation" box the group fills in. This works for an organisation the group invents.
- **Group rule.** The group agrees each entry, one member acts as scribe, and every member types the agreed entries into their own page. This suits a group of seven, and Capstone teams are set per cohort in the Admin Console.
- **Executive team.** Unit 1 gives each participant an executive role in the Simulated Enterprise Executive Team (SEET). The Unit 5 team behavioural profile is built from the members' own scores.
- **The three areas.** The Assessment criteria card scores Direction (Units 2–4), Influence (Units 5–9) and Grounding (Units 10–12). These are the guide's Strategy Design, Strategy Execution and Sustaining Performance.
- **Real experience stays individual.** The reflections ask about "your organisation", meaning the participant's own employer. They remain Portfolio work, which matches how the guide uses real experience.
- **Current practices come from the Charter.** Unit 3 Keep and Improve ask for "the current practices at [Case]". The Charter's "How these challenges manifest" supplies them.

## 3. What does not fit

1. **One case per cohort, set by IBSL.** The Capstone page reads the case name and brief from `capstone_brief`: one row per cohort, typed in the Admin Console under "Cohort brief" (Case: "e.g. Company X or Mining sector"). Every box shows that one name in place of [Case]. Under the guide, four groups write four organisations, but all four would see the same name. Until the brief is filled in, the page also says "IBSL will publish your cohort's brief shortly".
2. **No place for the Problem Charter.** Neither the Unit 1 pages nor the Capstone page hold sections A to E. The Blueprint has 11 sections, Units 2 to 12.
3. **The Capstone opens with Unit 2.** The Charter is written in orientation (Unit 1). Until Unit 2 opens, the page shows "The capstone opens when Unit 2 opens."
4. **Unit 1 has no group Charter exercise.** Section 1 Orientation explains the SEET. Section 6 Application is the Distortion Lab, which the facilitator runs and which feeds nothing into the Capstone.
5. **Nothing carries the Charter forward.** No unit shows the group its challenges, the results falling short or the capabilities to strengthen. The Assessment criteria do not name the Charter. The guide expects the Blueprint to answer the central problem, but the Blueprint has no link back to it.
6. **Unit 2 starts from a blank organisation.** In 4.1 the group types "Organisation" and "Strategy period". Nothing tells the group to build the strategy as its answer to the central problem.
7. **Seven members, ten roles.** The SEET lists ten roles and each group has seven members. Unit 6 asks for CEO and CFO scorecards. In Unit 2, part 5.1, each participant chooses a role from the list. Nothing records which seven roles a group holds or makes sure CEO and CFO are taken. Yet the individual showcase is scored on "their executive role".
8. **Two names.** The guide calls it the "S2R Capability Blueprint". The portal calls it the "Capstone Blueprint", and the page title is "Strategy2Results® Blueprint Showcase".
9. **Guide wording against your standards:** "S2R" appears without ® in the title, "S2R Problem Charter", "S2R Capability Blueprint" and "the detailed S2R solution". "orientation of the program" should read "programme".

## 4. Proposed

1. **The Problem Charter becomes Section 1 of the Blueprint**, with eight boxes taken from the guide's template:
   - 1A Our organisation
   - 1B Our strategy-to-results reality
   - 1C Challenges experienced
   - 1D How they manifest
   - 1E Consequences for results and culture
   - 1F Capabilities to strengthen
   - 1G Our central organisational problem
   - 1H Our sources of experience

   It uses the same send-for-confirmation and confirm steps as every other section. The database box count for Unit 1 is set to 8.
2. **Each team's [Case] is the organisation name from 1A.** The cohort brief keeps the challenge question, the deadline, the showcase date and the venue. The "Case" field leaves the Admin Console.
3. **The Capstone opens with Unit 1.** Teams must be set in the Admin Console before Unit 1 opens.
4. **Unit 1, Section 6 Application holds the Charter as group Capstone work.** The Distortion Lab stays first, as class practice. The Charter follows the guide's four steps, with one record, Confirm and Print, and feeds 1A to 1H through a new `PULL.u1` row. The same record lists the group's executive team (member and role), with CEO and CFO among the seven roles. The facilitator page gets the matching PARTICIPANT ACTIVITY notes.
5. **Every unit's Capstone section shows the group's 1F and 1G, read only, at the top.** The "How Section 5 works" box adds one line: "Your group's work here answers the central problem in your Problem Charter." This applies to Units 2 to 8 now, and to Units 9 to 12 as each is built.
6. **Unit 2, part 4.1** shows the organisation from 1A, read only, and opens: "Your group builds the strategy that answers the central problem in your Problem Charter."
7. **Assessment criteria, under Team Blueprint**, add a line: "Problem Charter: how fully the Blueprint answers the central problem and builds the capabilities the Charter names." The weightings stay as they are.

## 5. For your word

1. The Blueprint carries two names: "S2R® Capability Blueprint" in the guide and "Capstone Blueprint" on the portal.
2. Points 1 to 7 of section 4.
3. The guide wording in section 3, point 9.

## 6. Order of work after your word

SQL (Section 1 of the Blueprint, each team's organisation name, box count, Capstone opening with Unit 1) → `capstone_P.html` and `dashboard_A.html` → the Unit 1 pages and deck → the read-only Charter line in Units 2 to 8 (pages and decks) → `dashboard_F.html` labels and `build_collection.js` → end-to-end test → your push and SQL.
