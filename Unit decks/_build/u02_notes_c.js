// Unit 2 presenter notes, part 3: Section 4 (Integration), Section 5 (Application) and the Unit Summary.
// Structure of every page (see u02_notes.js): HEADING, then numbered steps in class order. The facilitator explains
// every step of the group work from the slides; the coaching for the moment the groups do that work on the portal
// sits at the end of the page, under LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL.
module.exports = function (ctx) {
  const { u, H, S, page, say, ask, noq, IN, pick, portal, later, n, lead, gd, head, refl, reflFor, data } = ctx;
  const { EL, SIPD, ROLES, APP_DIMS, GROUPS, SUMMARY } = data;

  // ════════════════════════════════════════════════════════════════════════ SECTION 4
  const l4 = lead(4, 0);
  const i4 = pick(l4, 'Section intent: ', true), l4b = pick(l4, 'The work happens collectively'),
    st = ['4.1 — Build the Strategy Architecture: ', '4.2 — Derive the Strategy Intent Statement: ', '4.3 — Build Success in Practice: '].map(p => pick(l4, p)),
    l4q = pick(l4, 'The quality of the final SiP therefore depends'), l4g = pick(l4, 'Working in groups: ', true), l4o = pick(l4, 'The objective is collective construction of one enterprise position.');
  pick(l4, 'Each group will work through three connected stages:');
  pick(l4, 'Emphasise the sequence. Each output provides the foundation for the next: Strategy Architecture → Strategy Intent → Success in Practice');
  n.s4 = ctx.divider(4, `1. 4.1a: how the group works. One scribe, agreed entries, every member's own page.
2. 4.1b to 4.1i, Step 1: the routine for one element, the 14 elements in four groups, the Strategy Architecture output and its six checks.
3. 4.2, Step 2: the Strategy Intent Statement, derived from the group's own WHAT, WHY, HOW and WHEN.
4. 4.3a to 4.3c, Step 3: Success in Practice, one statement for each of the four SiP domains, confirmed and then read as one.
You explain all three steps from the slides. The groups do the work itself on the portal after the teaching, in the session or after it.`, [
    S('State the section intent.', say(i4.replace('Participants now apply', 'You now apply'))),
    S('Say why the work is collective.', say(l4b), IN('willing_commitment')),
    S('Give the three connected stages.',
      say('Each group will work through three connected stages.'), ...st.map(x => '- ' + x)),
    S('Emphasise the sequence.',
      say('Each output provides the foundation for the next: Strategy Architecture, then Strategy Intent, then Success in Practice. ' + l4q)),
    S('Say how the groups work.',
      say(l4g.replace('Participants work in their assigned groups throughout the exercise. Encourage groups to surface differences before resolving them.', 'You work in your assigned groups throughout the exercise. Surface your differences before you resolve them.') + ' ' + l4o)),
    S('Read the two section learning outcomes from the slide.'),
    S('Say how this section runs in class.',
      say('I explain all three steps from the slides now, so that everyone knows what the group will do and what a good answer looks like. Your group does the work on the portal after the teaching.')),
  ], later('You move from teaching to coaching. The groups do the thinking. You hold the sequence, ask the questions that test their answers, and keep each group honest about what it has actually decided. The coaching notes for that stage sit at the end of the notes of the slides in this section, under headings that begin with LATER.'));

  const g41 = gd(4, 0, 0), a41 = gd(4, 0, 1);
  const agree = pick(a41, 'The group agrees each entry and one member acts as scribe.');
  n.group = page(head(4, 0, 'HOW THE GROUP WORKS'), [
    S('Explain how the group works, using the four lines on the slide.',
      say('Your group agrees each entry. One member acts as scribe and types the agreed wording. Every member then types the agreed entries into their own page, in the session or after it.')),
    S('Say why every member’s page matters.',
      say('Your own page is what I review. It is also where your team’s Capstone Blueprint later takes the three confirmed outputs from.')),
    S('Ask for every voice.',
      say('The scribe types what the whole group has agreed. Every member speaks before an entry is typed.'),
      IN('top_down_cultures')),
    S('Tell participants about the two boxes at the top of 4.1.',
      say('At the top of 4.1 there are two boxes: Organisation and Strategy period. Every member enters the same two entries. They print at the top of your group’s reports.')),
    S('Explain confirmation.',
      say('Your group confirms each element, each statement and each output once it says what your group means.')),
    S('Confirm the groups.', 'Confirm who is in each group, and ask each group to name its scribe before the work begins.'),
  ], portal(agree),
  later('- Move between the groups. Listen to a group before you speak to it.',
    '- Ask for choices. When a group offers a broad aspiration, ask: "What has the organisation decided?"',
    '- Protect the sequence. A group that writes its Strategy Intent Statement before its Architecture is confirmed is working without its source.',
    '- Hold every group to one enterprise position. A set of functional positions placed side by side falls short of collective construction.'));

  const g1 = pick(g41, 'This is the foundation of the exercise.'), g2 = pick(g41, 'Each group works through the 14 elements'),
    g3 = pick(g41, 'Remind participants that the elements are interconnected.'), g6 = pick(g41, 'The purpose of confirmation is');
  pick(g41, 'Encourage participants to capture actual strategic choices and to leave broad organisational aspirations out.');
  pick(g41, 'As each element is completed, the group should review what it has written and confirm: "Is this what we mean?"');
  n.a41 = page(head(4, 0, 'HOW EACH ELEMENT WORKS'), [
    S('State the purpose.', say(g1 + ' ' + g2)),
    S('Walk the routine for one element, using the lines on the slide.',
      say('For each element your group answers its four questions. You then select Generate what this is saying, and one member reads the result aloud. Your group asks: Is this what we mean? You confirm, or you refine and state what the position should say.')),
    S('Set the standard for an answer.',
      say('Capture actual strategic choices and leave broad organisational aspirations out. A strategic choice names what the organisation will do and what it leaves out.')),
    S('Explain confirmation.', say(g6.replace("the group's thinking", 'your group’s thinking')), IN('silence_is_a_decision')),
    S('Explain the count.',
      say('Your group confirms the elements one by one. At 14 of 14 the Strategy Architecture output opens.')),
    S('Say that the elements test one another.',
      say(g3.replace('Remind participants that the elements are interconnected.', 'The elements are interconnected.')),
      say('When that happens, return to the earlier element and revise it. An element that is edited after confirmation must be confirmed again.')),
    S('Bridge to the next slide.', say('The next slide shows the 14 elements as one list.')),
  ], portal(a41.slice(2, 7)),
  later('- Listen for confirmation without reading. Ask one member to read the generated position aloud before the group confirms it.',
    '- Listen for one voice answering for the group. Ask a quieter member: "Is this what you mean?"',
    '- Listen for answers written to sound complete. Ask: "What have we actually decided here?"'));

  const grp = name => (GROUPS.find(g => g[1].includes(name)) || [''])[0];
  const c41 = u.part(4, 0).content[0].replace(' Click each element to expand.', '');
  n.a41b = page(head(4, 0, 'THE 14 ELEMENTS'), [
    S('Show the 14 elements as one list.', say(c41)),
    S('Link back to 1.1.',
      say('In 1.1 we met nine concepts. Here the same definition is worked as 14 elements. WHAT, WHY, HOW and WHEN are four elements. CREATES, DELIVERS and SUSTAINS VALUE are three. OPERATING ENVIRONMENT has an element of its own.')),
    S('Say what each element gives the group.',
      say('Each element comes with a short guide and four questions.')),
    S('If a participant asks where an element goes in the Strategy Architecture output, use this list.',
      ...EL.map((e, k) => `${k + 1} · ${e.n} — ${e.tag} → ${grp(e.n)}`)),
    S('Bridge to the next slide.', say('The next four slides take the elements in four groups.')),
  ]);

  // What a strong answer contains (said in class) and what to watch for when the groups do the work (coaching).
  const strong = {
    'ITERATIVE': 'A strong answer names the hypotheses the strategy depends on, the evidence that would trigger refinement, and the point at which choices are revisited.',
    'THINKING & LOGIC': 'A strong answer names the alternatives that were explored and what must be true for the strategy to work.',
    'PROCESS': 'A strong answer says who could run the next strategy cycle, and where decisions and their rationale are recorded.',
    'WHAT': 'A strong answer has a boundary: it names something the organisation has deliberately chosen to leave out.',
    'WHY': 'A strong answer gives a reason that no competitor could claim unchanged, and it speaks to stakeholders as well as customers.',
    'HOW': 'A strong answer names the mechanism: the capabilities, the processes, the structures and the partnerships that make the strategy work.',
    'WHEN': 'A strong answer says what must happen first, and which dependency sets the order.',
    'CREATES VALUE': 'A strong answer names the value itself and says how you will know that genuine value has been created.',
    'DELIVERS VALUE': 'A strong answer describes the experience recipients must have, and faces the fourth question: what could prevent value from reaching them?',
    'SUSTAINS VALUE': 'A strong answer names what must be continually invested in or renewed. Expect this to be the hardest of the 14: most organisations invest in creating and delivering value and leave its durability unfunded.',
    'STAKEHOLDERS': 'A strong answer names every group with a material stake, shows where their interests conflict, and says whose interests this strategy could overlook.',
    'NAVIGATING': 'A strong answer says how a signal from the environment becomes a deliberate change of course, and who makes that call.',
    'THE FORCES': 'A strong answer names the few forces that materially shape this strategy.',
    'OPERATING ENVIRONMENT': 'A strong answer defines the context and faces the fourth question: where would this strategy stop making sense if the context changed?',
  };
  const watch = {
    'ITERATIVE': 'answers that describe an annual planning cycle.',
    'THINKING & LOGIC': 'a list of data sources and analyses, with no alternative explored.',
    'PROCESS': 'a process that lives in one person’s head.',
    'WHAT': 'a WHAT with no boundary. The fourth question needs a real answer.',
    'WHY': 'a WHY that any competitor could claim unchanged, and a WHY written for customers only.',
    'HOW': 'a HOW stated as an aspiration with no mechanism named, and an operating model that predates the current direction.',
    'WHEN': 'every move running in parallel.',
    'CREATES VALUE': 'a list of activities with no value named.',
    'DELIVERS VALUE': 'channels named with no account of the experience recipients must have.',
    'SUSTAINS VALUE': 'the thinnest answers of the 14.',
    'STAKEHOLDERS': 'customers named as the only stakeholders, and no conflict between stakeholder interests acknowledged.',
    'NAVIGATING': 'sensing with no route into decisions.',
    'THE FORCES': 'a generic list of forces. The 1.1 concept THE FORCES (slide 7) also names internal forces: culture, behaviour patterns, institutional habits and legacy identity. Ask where these appear in the group’s answers.',
    'OPERATING ENVIRONMENT': 'a context left undefined.',
  };
  const eins = {
    'ITERATIVE': ['move_on_directional_clarity', 'last_season_s_framework'], 'THINKING & LOGIC': ['inherited_boundaries'], 'PROCESS': ['succession_of_story'],
    'WHY': ['benchmarking_as_strategy'], 'HOW': ['symbol_or_substance'],
    'SUSTAINS VALUE': ['short_term_relief_long_term_cost'], 'STAKEHOLDERS': ['the_party_with_no_leverage'], 'NAVIGATING': ['adapt_the_method_keep_the_purpose'],
  };
  // The question of each element that is put to the room (number within the element's four questions).
  const roomQ = { 'ITERATIVE': 3, 'THINKING & LOGIC': 3, 'PROCESS': 4, 'WHAT': 4, 'WHY': 2, 'HOW': 1, 'WHEN': 1, 'CREATES VALUE': 4, 'DELIVERS VALUE': 4,
    'SUSTAINS VALUE': 2, 'STAKEHOLDERS': 4, 'NAVIGATING': 2, 'THE FORCES': 3, 'OPERATING ENVIRONMENT': 4 };
  const elStep = k => {
    const e = EL[k], rq = roomQ[e.n];
    return S(`Element ${k + 1} · ${e.n} — ${e.tag}.`,
      say(e.guide.replace(/ → /g, ', ').replace(/ = /g, ' is '), 'Guide, say'),
      'Name the four questions the group answers:', ...e.qs.map((q, j) => `${j + 1}. ${q}`),
      `Put question ${rq} to one or two participants, for their own organisation, and take a short answer.`,
      say(strong[e.n], 'Set the standard, say'),
      (eins[e.n] || []).map((id, j) => IN(id, j ? 'Then say' : 'Deepen, say')));
  };
  const groupNotes = (title, from, to, est, hold, bridge, coach) => {
    const ks = Array.from({ length: to - from + 1 }, (_, x) => from - 1 + x);
    return page(head(4, 0, title), [
      S('Say what this group of elements establishes.', say(est)),
      ...ks.map(elStep),
      S('Give the groups two things to hold on to.', hold),
      S('Bridge to the next slide.', say(bridge)),
    ], later(...ks.map(k => `- ${k + 1} · ${EL[k].n}: watch for ${watch[EL[k].n]}`), ...coach.map(c => '- ' + c)));
  };

  n.e1 = groupNotes('ELEMENTS 1–3 · STRATEGY DISCIPLINE', 1, 3,
    'Strategy Discipline is how the organisation produces, tests and renews its strategy. ITERATIVE keeps the strategy open to evidence. THINKING & LOGIC is the quality of the reasoning. PROCESS is the container that makes the reasoning repeatable. In the Strategy Architecture output these three sit under the last heading, Strategy Discipline. Your group works them first because they follow the order of the definition.',
    [say('These three elements ask how the strategy is made. Answer the question asked: how we produce, test and renew the strategy.'),
      say('Hold THINKING & LOGIC and PROCESS apart. Most organisations have a process and neglect the quality of the thinking inside it.')],
    'Next: elements 4 to 7, the Strategic Position and the Strategic Model.',
    ['Groups often answer with what the strategy is. Bring them back to how it is made.',
      'Ask for one real example for each element: the last revision, the last challenged assumption, the last decision that was recorded with its rationale.']);

  n.e2 = groupNotes('ELEMENTS 4–7 · POSITION AND MODEL', 4, 7,
    'WHAT and WHY form the Strategic Position: the value the organisation has chosen to create, its field of play, and the rationale that makes the choices coherent. HOW and WHEN form the Strategic Model: the mechanism through which the value is delivered and the timing and sequencing of the moves. These are the four dimensions your group brings forward in 4.2 to derive its Strategy Intent Statement. The quality of these four elements sets the quality of that statement.',
    [say('Test the four against one another. HOW without WHY is activity without logic. WHAT and WHY without HOW and WHEN is vision without execution. WHEN without WHAT is urgency without direction.'),
      IN('right_destination_right_design'),
      say('Your answers to these four elements appear again in 4.2, word for word. Loose wording here becomes a loose Intent.')],
    'Next: elements 8 to 11, the Value Architecture.',
    ['Give HOW and WHEN the most attention. They typically reveal the most significant gaps.']);

  n.e3 = groupNotes('ELEMENTS 8–11 · VALUE ARCHITECTURE', 8, 11,
    'The Value Architecture is the full account of value: how it comes into existence, CREATES VALUE; how it reaches its intended recipients, DELIVERS VALUE; what keeps it durable, SUSTAINS VALUE; and who receives or contributes it, STAKEHOLDERS. All three layers of the Value Triad must be explicitly designed and invested in.',
    [say('Compare your three value answers side by side. Is the answer on SUSTAINS as strong as the answers on CREATES and DELIVERS?'),
      say('Check CREATES VALUE against HOW. The value the organisation intends to create must be supported by the mechanism described in element 6.')],
    'Next: elements 12 to 14, Strategic Navigation.',
    ['Ask: "Where is the investment in sustainability of value?"',
      'Put the STAKEHOLDERS question about conflict directly: "Where do stakeholder interests reinforce or conflict?" A group that finds no conflict has usually looked at one stakeholder only.']);

  n.e4 = groupNotes('ELEMENTS 12–14 · STRATEGIC NAVIGATION', 12, 14,
    'Strategic Navigation is how the organisation reads and moves through its environment. NAVIGATING is the skill: sensing, interpreting and making deliberate moves. THE FORCES are what must be navigated. OPERATING ENVIRONMENT is the bounded context within which the strategy makes sense. The forces in the operating environment do not pause when the strategy is set.',
    [say('Check SUSTAINS VALUE against THE FORCES. The approach to sustaining value must respond to the forces within the operating environment.'),
      say('Check WHEN against these three elements. Timing and sequencing must reflect the realities of the organisation’s capability and environment.')],
    'When element 14 is confirmed, the count reads 14 of 14 and the Strategy Architecture output opens. The next slide shows that output.',
    ['Ask where a force can be used to advantage. The third NAVIGATING question treats external forces as something the organisation can put to use.']);

  const gOut1 = pick(g41, 'Producing the Strategy Architecture: ', true), gOut2 = pick(g41, 'They should then write out their Strategy Architecture output.');
  const outSay = gOut1.replace(' Ask groups to consider: "What is this architecture collectively saying about the organisation\'s strategy?"', '');
  if (outSay === gOut1) throw new Error('4.1 guidance changed: Producing the Strategy Architecture');
  const c41all = u.part(4, 0).content, oi = c41all.indexOf('The Strategy Architecture Output');
  if (oi < 0) throw new Error('4.1 content changed: The Strategy Architecture Output');
  n.out = page(head(4, 0, 'THE STRATEGY ARCHITECTURE OUTPUT'), [
    S('Say what happens at 14 of 14.',
      say(outSay.replace('the group should step back', 'your group steps back').replace('examine them', 'examines them'))),
    S('Give the question the group asks itself, from the foot of the slide.',
      say('Your group then asks itself: What is this architecture collectively saying about the organisation’s strategy?')),
    S('Show the five headings on the slide.',
      say(c41all[oi + 1].replace('The page brings', 'The output brings').replace('The group refines', 'Your group refines')),
      ...GROUPS.map(g => `- ${g[0]}: ${g[1].join(' · ')}`)),
    S('Say what the output must do.',
      say(gOut2.replace('They should then write out their Strategy Architecture output. ', '')),
      IN('personality_dependent_strategy')),
    S('Bridge to the next slide.', say('Before the output is confirmed, your group runs six checks. They are on the next slide.')),
  ], later('- When a group reaches 14 of 14, ask it to stop writing. One member reads the confirmed positions aloud from first to last, with no editing.',
    '- Ask: "What is this architecture collectively saying about the organisation’s strategy?" Let two or three members answer in their own words.',
    '- Listen for an output that reads as 14 separate answers. Ask which choices depend on one another and have the connection written in.',
    '- Listen for detail stripped out to make the output shorter. Say: "The Architecture is the place for depth. The Strategy Intent Statement is the place for clarity."'));

  const ci = g41.indexOf('Before finalising, ask groups to check:');
  const checks = g41.slice(ci + 1, ci + 7), source2 = pick(g41, 'The completed Strategy Architecture becomes the source for Step 2.');
  if (ci < 0 || !checks[5].startsWith('Does the architecture represent')) throw new Error('4.1 guidance changed: the six checks');
  const where = [
    'Read the Strategic Position (WHAT, WHY) against the Strategic Model (HOW, WHEN).',
    'Each of you names one. Resolve it in the element concerned before you confirm.',
    'Read element 6 against elements 4 and 8.',
    'Read element 7 against elements 6, 13 and 14.',
    'Read elements 8, 9 and 10 side by side. Look hardest at element 10.',
    'Each of you answers yes or no aloud.'];
  n.checks = page(head(4, 0, 'SIX CHECKS BEFORE FINALISING'), [
    S('Introduce the checks.', say('Before finalising your Strategy Architecture output, your group checks six things.')),
    ...checks.map((c, k) => S(`Check ${k + 1}.`, `Read from the slide: "${noq(c)}"`, say(where[k], 'Say how the group checks'))),
    S('Say what a group does when a check fails.',
      say('Return to the element concerned, revise it and confirm it again. Then carry the change into the text of the output.')),
    S('Bridge to 4.2.',
      say(source2 + ' The Architecture holds the logic. Step 2 takes four of its elements, WHAT, WHY, HOW and WHEN, and crystallises them into one statement.')),
  ], later('- Put the six checks to the group one at a time, as questions. One member answers aloud for the group and the others agree or object.',
    '- When all six checks hold, the group confirms its Strategy Architecture output. It can then be printed. Every member’s page carries the same text.',
    '- Listen for contradictions left standing because resolving them is uncomfortable. Name the contradiction and ask who in the organisation would have to decide it.',
    '- Listen for a yes given quickly to the sixth check. Ask the member who has spoken least.'));

  const g42 = gd(4, 1, 0), c42 = u.part(4, 1).content;
  const w42 = ['WHAT — ', 'WHY — ', 'HOW — ', 'WHEN — '].map(p => pick(g42, p));
  const p42 = s => pick(g42, s);
  const g42a = p42('With the Strategy Architecture established'), g42b = p42('The Architecture contains the depth.'),
    g42e = p42('Facilitator emphasis: '), g42f = p42('The Strategy Intent Statement crystallises the ambition.'), g42g = p42('A strong Intent should allow a leader'),
    g42i = p42('Where the statement exposes a contradiction'), g42j = p42('The confirmed Strategy Intent becomes the source for Step 3.');
  p42('Bring forward the four dimensions already established through the architecture:');
  p42('Ask groups to review these four dimensions together and derive one crisp Strategy Intent Statement.');
  p42('Once drafted, have the group read the statement against its completed Architecture and confirm: "Does this statement faithfully express the strategic ambition contained in our Architecture?"');
  if (!g42e.includes('Protect the Intent from becoming overloaded.')) throw new Error('4.2 guidance changed');
  n.a42 = page(head(4, 1), [
    S('State the step.', say(g42a.replace('groups now crystallise', 'each group now crystallises') + ' ' + g42b)),
    S('Bring forward the four dimensions on the slide.',
      say('These are the four dimensions already established through your architecture. They are your group’s own answers to elements 4 to 7.'),
      ...w42.map(x => '- ' + x)),
    S('Give the task.', say('Review these four dimensions together and derive one crisp Strategy Intent Statement.')),
    S('Protect the Intent from becoming overloaded.',
      say('You may want to carry every important point from the Architecture into the statement. The Architecture already holds that detail. ' + g42f)),
    S('Set the standard.',
      say(g42g),
      say('A strong statement carries all four dimensions: the value chosen and the field of play, the rationale, the mechanism and the timing. It is crisp, directional and easy to express.', 'Add'),
      IN('strategy_carried_by_people')),
    S('Give the confirmation question, from the foot of the slide.',
      say('Once the statement is drafted, read it against your completed Architecture and confirm: Does this statement faithfully express the strategic ambition contained in our Architecture?')),
    S('Say what a group does when the statement exposes a contradiction.', say(g42i.replace('resolve the underlying', 'resolve the underlying'))),
    S('Bridge to 4.3.', say(g42j)),
  ], portal(gd(4, 1, 1).slice(1)),
  later('- One member reads the group’s four answers aloud as one passage.',
    '- A useful way in: each member proposes a version of the statement aloud, and the group builds from the strongest.',
    '- Ask: "Which words in this statement could go back into the Architecture with nothing lost?"',
    '- Test the statement. Ask one member to read it to you with no explanation. Say back the strategic position you understood. The group hears at once whether the statement carries it.',
    '- Listen for a statement that names WHAT and WHY and is silent on HOW and WHEN.',
    '- Listen for wording chosen because it sounds impressive. Ask what the phrase commits the organisation to.'));

  const g43 = gd(4, 2, 0), a43 = gd(4, 2, 1);
  const p43 = (s, cut) => pick(g43, s, cut);
  const g43a = p43('The Strategy Intent Statement establishes the ambition.');
  p43('Position the group inside the future described by its Strategy Intent. Use one central question: "If our Strategy Intent is successful, what should we see in practice?"');
  p43('The group works through the four SiP domains:');
  const dg = ['1. Customer Experience & Value — ', '2. Operational Capability & Execution Rhythm — ', '3. People & Culture Dynamics — ', '4. Enterprise Value Creation — '].map(p => pick(g43, p, true));
  n.a43a = page(head(4, 2, 'THE FOUR DOMAINS'), [
    S('Link the step to the one before it.', say(g43a.replace('The group now defines', 'Each group now defines'))),
    S('Position the group inside the future.',
      say('Stand inside the future described by your Strategy Intent. One central question guides the work: If our Strategy Intent is successful, what should we see in practice?'),
      IN('credible_promise_honest_facts')),
    S('Explain the method.',
      say('Your group works through the four SiP domains. In each domain you answer three input questions, then derive one statement for the domain from your answers. The statement describes what is happening when the Strategy Intent is working.')),
    ...SIPD.map((d, k) => S(`D${k + 1} · ${d.t}.`,
      say(dg[k].replace("keep the group's final output focused on its specific Strategy Intent", 'keep your group’s final output focused on your own Strategy Intent').replace('The group produces one', 'Your group produces one')),
      `Give the lead question (the slide shows it in short form): "${noq(d.lead)}"`,
      'Name the three input questions the group answers:', ...d.qs.map((q, j) => `${j + 1}. ${q}`))),
    S('Bridge to the next slide.', say('Four statements, one for each domain. The next slide shows how your group confirms and tests them.')),
  ], portal(a43.slice(1, 6)),
  later('- One member reads the group’s confirmed Strategy Intent Statement aloud before the group starts.',
    '- Listen for initiatives, projects and activities written as success. Ask: "When that has worked, what do we see?"',
    '- Listen for a third input question left thin. Observable evidence is what makes a statement testable.',
    '- Listen for a domain statement written by the member whose function owns that domain. Every statement belongs to the whole group.'));

  const g43c = p43('Confirming each SiP domain: '), g43i = p43('This is important.'), g43r = p43('Once all four statements are confirmed'),
    g43d = p43('Depth: '), g43b = p43('Balance: '), g43f = p43('Use the SiP Flammables as the final balance check.'), g43o = p43('The four confirmed statements together become');
  p43('Test the SiP: Use the two quality checks from Section 3.');
  if (!g43c.includes('"Is this what success in this domain should look like if our Strategy Intent is realised?"')) throw new Error('4.3 guidance changed: confirmation question');
  n.a43b = page(head(4, 2, 'CONFIRM AND TEST THE SiP'), [
    S('Give the confirmation question for each domain, the first line on the slide.',
      say('After drafting each statement, pause and ask: Is this what success in this domain should look like if our Strategy Intent is realised? Refine the statement until your group confirms it.')),
    S('Say why this matters.',
      say(g43i.replace('the group\'s own', 'your group’s own')),
      IN('formula_or_practice')),
    S('Read the four statements as one.', say(g43r)),
    S('Give the two tests from Section 3.',
      say('We use the two quality checks from Section 3.'), '- ' + g43d, '- ' + g43b),
    S('Name the final check.',
      say(g43f),
      say('Read your four statements against the four patterns of 3.2 and the indicators of each.')),
    S('Close the step.', say(g43o)),
    S('Bridge to the next slide.', say('The last slide of Section 4 brings the three outputs together.')),
  ], later('- After each domain statement, the group pauses and asks the confirmation question.',
    '- When all four statements are confirmed, one member reads the four aloud as one Success in Practice. The group applies the test for depth, then the test for balance.',
    '- Ask the group which of the four Flammables its SiP is closest to, and have it apply the three indicators of that pattern to its statements.',
    '- Where a pattern shows, use the three questions in the notes of that pattern (slides 3.2b to 3.2e). They bring the other domains back.',
    '- Listen for quick confirmation of the fourth domain, late in the exercise. The fourth statement deserves the same test as the first.'));

  const g43x = p43('Closing Section 4: ', true), g43y = p43('Then reinforce the connection: ', true), g43z = p43('These three outputs become the strategic foundation');
  if (!g43x.startsWith('Each group now holds three connected outputs: its Strategy Architecture, its Strategy Intent Statement and its Success in Practice.')) throw new Error('4.3 guidance changed: Closing Section 4');
  const cap = pick(a43, 'Into the Capstone: ', true);
  n.a43c = page(head(4, 2, 'THREE CONNECTED OUTPUTS'), [
    S('Show the three outputs side by side.',
      say('When the work is done, each group holds three connected outputs: its Strategy Architecture, its Strategy Intent Statement and its Success in Practice.')),
    S('Reinforce the connection, using the three lines on the slide.', say(g43y)),
    S('Say how the three are displayed.',
      say('Each group displays or prints the three together, as one report: the Strategy Intent Design.')),
    S('Say where the outputs go.', say(g43z)),
    S('Say how the outputs reach the Capstone.',
      say('Your three confirmed outputs feed your team’s Capstone Blueprint. Its Unit 2 section opens once every member of your team has completed Unit 2, and brings the three outputs in from a member’s page. Your team reads them together and confirms them there.')),
    S('Bridge to Section 5.',
      say('Once your group has confirmed its Success in Practice, success is defined. Section 5 applies it: from your executive role, what must you contribute for this Success in Practice to become real?')),
  ], H('LATER, WHEN THE GROUPS HAVE DONE THE WORK:') + '\n' + ['- Each group displays or prints its three outputs together.',
    '- Invite each group to read its Strategy Intent Statement to the room.',
    '- After each group, ask the room: "Could you recognise this organisation if you walked into it?"',
    '- Remind every member to complete their own page with the group’s agreed entries, in the session or after it, and to confirm each output on that page.'].join('\n'));

  // ════════════════════════════════════════════════════════════════════════ SECTION 5
  const l5 = lead(5, 0);
  const i5 = pick(l5, 'Section intent: ', true), l5e = pick(l5, 'The Application section helps the group see'),
    l5a = pick(l5, '5.1 — Role Contribution to SiP: '), l5b = pick(l5, '5.2 — SiP Statement Collective Application: ');
  pick(l5, 'Success is already defined. The work in this section is to apply it.');
  pick(l5, 'Each participant now asks: "From my executive role, what must I contribute for this Success in Practice to become real?"');
  n.s5 = ctx.divider(5, `1. 5.1a and 5.1b: the role contribution table, and how to write a contribution.
2. 5.2: the group sharing, and the four headings participants observe under.
3. The Section 5 Reflections slide: the reflection participants write on the portal.
The role rows are written on the portal after the teaching. The group sharing in 5.2 takes place once the rows are complete.`, [
    S('State the section intent.', say(i5.replace('moves the group from', 'moves you from'))),
    S('Say what Section 4 leaves in place.',
      say('By the time you reach Section 5, your group has produced the Strategy Architecture, the Strategy Intent and Success in Practice. Success is already defined. The work in this section is to apply it.')),
    S('Give the question of the section.',
      say('Each of you now asks: From my executive role, what must I contribute for this Success in Practice to become real?')),
    S('Name the shift.',
      say('Section 4 is collective: one group, one position. Section 5 is individual: one role, one contribution.')),
    S('Say what the section shows.', say(l5e.replace('helps the group see', 'helps your group see'))),
    S('Read the two section learning outcomes from the slide.'),
    S('Give the two activities in order.', say('There are two activities, in this order.'), '- ' + l5a, '- ' + l5b),
  ]);

  const g51 = gd(5, 0, 0);
  const p51 = s => pick(g51, s);
  const purpose51 = pick(g51, 'Purpose: ', true), back51 = p51('Ask participants to return to the four SiP statements produced in Section 4: ');
  p51('Each participant now completes the table from the perspective of their assigned executive role. Use this central question: "From this role, what must be contributed so that the agreed Success in Practice becomes real?"');
  n.r51a = page(head(5, 0), [
    S('State the purpose.', say(purpose51)),
    S('Return to the four SiP statements.',
      say('Return to the four SiP statements your group produces in Section 4: ' + back51.split('Section 4: ')[1]),
      'Tell participants: these four statements are the reference for every entry in the table.'),
    S('Put the central question on the slide to the room.',
      say('Each of you completes the table from the perspective of your assigned executive role. The central question: From this role, what must be contributed so that the agreed Success in Practice becomes real?')),
    S('Confirm the assigned executive role of each participant, using the ten roles on the slide.',
      ROLES.join(' · '),
      say('You select your assigned role and write one row: four entries, one for each SiP domain.')),
    S('Take the four domains of the table.',
      ...APP_DIMS.map((d, k) => `- D${k + 1} · ${d.label}: ${d.prompt.replace(/your SiP/g, 'the SiP')}`)),
    S('Give the rule for an entry.',
      say('The role sets the perspective and the SiP sets the target. Every entry answers one question: what does this role contribute to that domain statement?'),
      IN('the_mission_in_daily_practice')),
    S('Bridge to the next slide.', say('The next slide shows how to write a contribution.')),
  ], portal(gd(5, 0, 1).slice(1)));
  pick(g51, 'Recording: Each participant enters their own responses in their participant file.');

  const ex = g51.slice(g51.findIndex(l => l.startsWith('Participants should write in the present tense of the future')) + 1).slice(0, 4);
  const gen = g51.slice(g51.findIndex(l => l.startsWith('Encourage practical and role-specific responses.')) + 1).slice(0, 4);
  if (ex[3] !== '"The organisation creates value through…"' || gen[3] !== '"Drive performance"') throw new Error('5.1 guidance changed: examples');
  p51('Ask in response: "What does this role specifically decide, enable, coordinate, resource, protect or change?"');
  p51('After completing the row, each participant should check whether their contribution strengthens all four SiP domains or only reflects the priorities of their own function.');
  n.r51b = page(head(5, 0, 'WRITING THE CONTRIBUTION'), [
    S('Give the voice to write in: the left column of the slide.',
      say('Write in the present tense of the future, as if the strategy is already working.'),
      'Read the four examples from the slide: ' + ex.join(' · '),
      IN('declare_the_outcome_first')),
    S('Name the general statements to push back on: the right column of the slide.',
      say('Be practical and role-specific. General statements such as these four say too little.'),
      'Read the four general statements from the slide: ' + gen.join(' · ')),
    S('Give the test for any general statement, from the foot of the slide.',
      say('The test for any general statement is this question: What does this role specifically decide, enable, coordinate, resource, protect or change?')),
    S('Take the six verbs one at a time.',
      '- Decide: which decision does this role own that the SiP depends on?',
      '- Enable: what does this role make possible for another function?',
      '- Coordinate: which hand-off between functions does this role hold together?',
      '- Resource: what does this role fund, staff or equip?',
      '- Protect: what does this role defend when short-term pressure rises?',
      '- Change: what does this role stop, start or redesign?',
      IN('substitution', 'On Change, say')),
    S('Give the check for a finished row.',
      say('After completing your row, check whether your contribution strengthens all four SiP domains or only reflects the priorities of your own function.'),
      IN('seeing_the_larger_system')),
    S('Bridge to 5.2.', say('Once every row is written, the groups share. The next slide shows how.')),
  ], H('LATER, WHEN YOU REVIEW THE ROWS:') + '\n' + [
    '- Look for a row in which one domain is rich and three are thin. This is the role’s own Flammable. Ask the participant to name it.',
    '- Look for contributions that describe what the role already does today. Ask what changes because of this Strategy Intent.',
    '- Look for contributions that depend on another role with no mention of it. Note them: they are the material for 5.2.'].join('\n'));

  const g52 = gd(5, 1, 0), c52 = u.part(5, 1).content;
  const purpose52 = pick(g52, 'Purpose: ', true), g52b = pick(g52, 'After all CXO rows have been completed'), g52d = pick(g52, 'The focus is on whether the agreed SiP');
  pick(g52, 'As groups share, listen for alignment, gaps, tensions and areas where the SiP statement may need clearer execution ownership.');
  const heads52 = []; for (let k = 1; k < 9; k += 2) heads52.push(`- ${c52[k]}: ${c52[k + 1]}`);
  if (c52[1] !== 'Alignment' || c52[7] !== 'Execution Ownership') throw new Error('5.2 content changed');
  n.c52 = page(head(5, 1), [
    S('State the purpose.', say(purpose52)),
    S('Explain the activity.',
      say(g52b.replace('After all CXO rows have been completed, invite each group to share its SiP statement and explain', 'After all CXO rows have been completed, each group shares its SiP statement and explains'))),
    S('Give the four headings on the slide.',
      say('As each group shares, everyone else listens under four headings.'), ...heads52),
    S('Say what the activity tests.', say(g52d)),
    S('Set the tone for the observations.', IN('honest_assessment_open_invitation', 'Say')),
    S('Say what execution ownership sounds like.', IN('i_made_this_decision', 'Say')),
    S('Bridge to the reflection.', say('The section closes with one reflection. It is on the next slide.')),
  ], portal(gd(5, 1, 1).slice(1),
    'The four boxes in 5.2:',
    '- Alignment: Where do the role contributions support the SiP statement and one another?',
    '- Gaps: Which part of the SiP statement has no role contributing to it?',
    '- Tensions: Where do role contributions pull against one another?',
    '- Execution Ownership: Where does the SiP statement need clearer execution ownership?'),
  H('LATER, WHEN THE GROUPS SHARE:') + '\n' + [
    '- Invite the first group to share its SiP statement, one domain at a time. For each domain, two or three roles say what they contribute to it: the role, the verb and the contribution. Every role speaks at least once across the four domains.',
    '- After each group, ask the room for one observation under each heading. Then say plainly what you heard, and invite the group to work on it.',
    '- For each part of the SiP statement with no role contributing to it, ask: "Which role owns this?" A part of the SiP that no role owns will not be delivered.',
    '- Listen for two roles claiming the same contribution, and for a contribution that no role claims.',
    '- Listen for tensions described politely and left unresolved. A tension named in this room can be worked on here.',
    '- When a group wants to reword a SiP statement, record the change. The group agrees it and every member updates their own page.'].join('\n'));

  n.ref5 = ctx.reflection(5, [
    S('Show the slide and read the prompt aloud.', `5.2 Reflection — Application: "${refl(5, 1)}"`),
    reflFor(false, ', once the application exercise is complete'),
    S('Set the standard.',
      say('Name one shift only. Name it as a change in a decision, a capability or a behaviour. Say which gap it closes between your current strategic capability and the SiP your group described, and what your own role must do first.'),
      'Listen for: a list of five shifts. It is a sign that the participant has yet to choose.'),
    S('Say why the shift must reach behaviour.', IN('rebuilding_without_correcting', 'Say')),
    S('Bridge to the Unit Summary.', say('We close the unit by returning to where we started.')),
  ], 'Participants write the reflection in Section 5 of the participant file: 5.2 Reflection — Application.');

  const gs = gd(5, 2, 0);
  const closing = pick(gs, 'Closing the unit: ', true), back = pick(gs, 'Return to the opening question: ', true),
    commit = pick(gs, 'Closing commitment: ', true), trans = pick(gs, 'Transition to Unit 3: ', true);
  const ti = gs.findIndex(l => l.startsWith('Tangible outputs check: ')), outs = gs.slice(ti + 1, ti + 5);
  if (ti < 0 || !outs[3].startsWith('A role contribution row')) throw new Error('Unit Summary guidance changed: outputs check');
  const q = s => { const m = s.match(/"([^"]+)"/); if (!m) throw new Error('quote not found: ' + s.slice(0, 50)); return m[1]; };
  if (!back.endsWith('The difference between their opening answer and their closing answer is the measure of what Unit 2 produced.') || !commit.endsWith('These become the accountability anchors for Unit 3.')) throw new Error('Unit Summary guidance changed');
  n.summary = page(head(5, 2), [
    S('Read the five summary blocks aloud.',
      'Read each block aloud from these notes. The summary is deliberately concise: its role is to crystallise the arc of the unit. The blocks describe the whole unit, including the work the groups complete on the portal.',
      ...SUMMARY.map(s => `- ${s.arc} · ${s.t}: ${s.body}`)),
    S('Return to the opening question, on the slide.',
      'Go back to the definitions participants wrote when the session opened. The differences you noted on the whiteboard are still in view. Ask two or three participants:',
      `"${noq(q(back))}"`,
      say('The difference between your opening answer and your closing answer is the measure of what Unit 2 produced.')),
    S('Run the tangible outputs check.',
      'Before closing, confirm with the group that the following have been produced or are in progress:', ...outs.map(o => '- ' + o)),
    S('Ask for the closing commitment, on the slide.',
      'Ask each participant to complete this sentence privately:',
      `"${noq(q(commit))}"`,
      'Invite two or three to share. These become the accountability anchors for Unit 3.'),
    S('Give the transition to Unit 3.', say(q(trans))),
    S('Hand over to the portal.',
      say('The teaching ends here. You now go to the portal and complete your own page, in the session or after it.'),
      '- Section 1: the opening definition of strategy, and the reflections for 1.1 and 1.2.',
      '- Section 2: the 2.1 reflection.',
      '- Section 3: the 3.1 reflection.',
      '- Section 4, with the group: the 14 elements and the Strategy Architecture output, the Strategy Intent Statement, and the four SiP statements. The group agrees each entry, one member acts as scribe, and every member types the agreed entries into their own page.',
      '- Section 5: the role contribution row in 5.1, the four observation boxes in 5.2 and the 5.2 reflection.',
      'Participants then submit Unit 2 to the facilitator from their page.',
      'Where the portal work is done in the session, bring the room back together once it is complete, for the reading of the three outputs (4.3c) and the group sharing (5.2).'),
  ], H('AFTER THE SESSION:') + '\n' + [
    '- Review each participant’s submission from the facilitator dashboard. The three outputs appear under their own headings: Strategy Architecture, Strategy Intent Statement and Success in Practice (SiP).',
    '- Note the groups whose members hold different versions of an output. Ask them to agree one version and update their pages before the team opens its Capstone Blueprint.'].join('\n'));
};
