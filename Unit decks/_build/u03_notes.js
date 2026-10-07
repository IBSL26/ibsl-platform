// Unit 3 · presenter notes for the rebuilt deck (October 2026), written on the model of Carol's own Unit 2 deck
// (Deck upload\Module-2\unit-02.pptx; her notes are dumped in "Claude outputs\Unit 2 deck - notes as Carol approved them (format model).txt").
//
// STRUCTURE OF EVERY NOTES PAGE
//   1. HEADING in capitals.
//   2. HOW TO TEACH IT (HOW TO USE THIS SLIDE on reflection slides; HOW THIS SECTION RUNS, SECTION LEARNING OUTCOMES and
//      HOW TO OPEN THE SECTION on section slides): numbered steps in class order. Under each step title: what the facilitator
//      says ("Say:"), asks ("Ask:"), does, or listens for ("Listen for:").
//   3. Nothing sits loose after the steps. Card text, manuscript detail ("Add:"), EXAMPLE blocks and each journal insight
//      ("Deepen, say:" then "(Insight: Title. Source: …)") sit inside the step where they are used.
//   4. Last blocks only: ON THE PORTAL, AFTER THE TEACHING and LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL.
// A line that starts with § is a heading or a step title: format_notes_u03.py removes the mark and makes the line bold.
//
// ALIGNMENT: the notes carry only what the Unit 3 facilitator and participant files carry (rebuilt 6 October 2026 from
// Carol's amendments), plus manuscript detail that deepens content still on the pages. No exercise is invented.
// TEACHING FLOW: the facilitator teaches the whole unit from the deck first, including one Strategy Airport learning round
// played with the room; participants go to the portal afterwards. No note steers participants through the portal while teaching.
// Carol's rules: no timings, no pre-work, no contrast constructions, "SiP domains", British spelling, "post in the chat".
const fs = require('fs');
const path = require('path');
const vm = require('vm');

module.exports = function (INS) {
  const used = new Set();
  const N = (...parts) => parts.flat(Infinity).filter(p => p !== null && p !== undefined && p !== false && String(p).trim() !== '').join('\n\n').replace(/\n{3,}/g, '\n\n');
  const H = t => '§' + t;
  const noq = s => { if (/"/.test(s)) throw new Error('straight quote inside a spoken line: ' + s.slice(0, 80)); return s; };
  // A long spoken line is set one sentence to a line, as in Carol's deck.
  const brk = s => s.length < 150 ? s : s.replace(/([.?!])\s+(?=[A-Z“‘])/g, '$1\n');
  const say = (s, cue = 'Say') => `${cue}: "${brk(noq(s))}"`;
  const ask = s => `Ask: "${noq(s)}"`;
  const IN = (id, cue = 'Deepen, say') => {
    const x = INS[id]; if (!x) throw new Error('unknown insight ' + id);
    if (used.has(id)) throw new Error('insight used twice: ' + id); used.add(id);
    return [say(x.text, cue), `(Insight: ${x.title.replace(/\.$/, '')}. Source: ${x.source})`];
  };
  const S = (title, ...lines) => [title, ...lines.flat(Infinity).filter(x => x !== null && x !== undefined && x !== false)];
  const steps = items => items.filter(Boolean).map((it, k) => H(`${k + 1}. ${it[0]}`) + (it.length > 1 ? '\n' + it.slice(1).join('\n') : ''));
  const page = (heading, items, ...tail) => N(H(heading), H('HOW TO TEACH IT:'), steps(items), tail);
  const block = (title, ...lines) => H(title) + '\n' + lines.flat(Infinity).join('\n');
  const portal = (...lines) => block('ON THE PORTAL, AFTER THE TEACHING:', ...lines);
  const later = (...lines) => block('LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:', ...lines);
  const EX = (...lines) => ['', H('EXAMPLE'), ...lines, ''];
  const divider = (label, runs, slo, items, ...tail) => N(H(label),
    H('HOW THIS SECTION RUNS:') + '\n' + runs.join('\n'),
    H('HOW TO OPEN THE SECTION:'), steps(items), tail);
  const SLO = slo => [H('SECTION LEARNING OUTCOMES:'), ...slo.map((o, k) => `${k + 1}. ${o}`)];
  const reflection = (num, items, where) => N(H(`SECTION ${num} REFLECTIONS`), H('HOW TO USE THIS SLIDE:'), steps(items), portal(where));
  // Carol's two lines from her own decks, word for word, as the step that says what the reflection is for.
  const reflFor = () => S('Say what the reflection is for.',
    'Point learners to the portal section that they will be required to complete with as much depth as possible.',
    'The reflections build the learning portfolio they receive at the end of the programme.', '',
    say('You write this reflection on the portal after the teaching, with as much depth as you can.'));

  // ── Data: the same arrays the two pages use (rebuild_u03/u3_shared.js) and the facilitator Unit Summary (u3_f.js) ──
  // On Carol's computer the two files sit in rebuild_u03 (the page build folder); in a scratch build they may sit beside this file.
  const src = f => [path.join(__dirname, 'rebuild_u03', f), path.join(__dirname, f)].find(x => fs.existsSync(x));
  const box = {};
  const stub = { getElementById: () => null, querySelectorAll: () => [] };
  vm.runInNewContext(fs.readFileSync(src('u3_shared.js'), 'utf8') + '\nthis.D={KISS_DOMAINS,HOT_ZONES,PM_CATS,WORKED,SA_SIP,SA_CARDS,SA_OPTIONS};', Object.assign(box, { document: stub, window: {} }));
  const D = box.D;
  vm.runInNewContext(fs.readFileSync(src('u3_f.js'), 'utf8').split('var curHZ')[0] + '\nthis.SUMMARY=SUMMARY;this.WORKED_MODEL=WORKED_MODEL;', box);
  D.SUMMARY = box.SUMMARY;
  D.WORKED = Object.assign({}, D.WORKED, box.WORKED_MODEL);   // the case (SiP, KISS) plus the worked answers of the six steps
  const { KISS_DOMAINS: KD, HOT_ZONES: HZ, PM_CATS: PM, WORKED: W } = D;
  const hz = role => HZ.find(h => h.role === role);

  const KLO = [
    'Distinguish the organisational practices that reinforce strategic progress from those that constrain it.',
    'Determine the enterprise priorities required to advance from the current position to the intended future state.',
    'Formulate clear and measurable outcomes that express the strategic priorities of the organisation.',
    'Establish a clear relationship between strategic ambition, organisational contribution and evidence of progress.'];
  const SLOS = {
    1: ['Distinguish the current practices that reinforce strategic progress from those that constrain it.', 'Translate strategic intent into measurable results.'],
    2: ['Recognise the benefits of mapping the terrain before setting goals.', 'Practise the translation of SiP into OKRs.'],
    3: ['Recognise how each leadership function’s emphasis shapes the priorities it proposes.', 'Distinguish functional contributions from the enterprise priorities they serve.'],
    4: ['Apply the translation of SiP into OKRs as a group.', 'Gain collective intelligence for the strategic trajectory.'],
    5: ['Reinforce strategy translation capability.', 'Establish individual capability to set a strategic trajectory.']};
  const REFL = {
    '1.4': 'Think of a goal your team set in the last 12 months. Was it an Objective, a Key Result, or a task disguised as one of these? What would a proper Key Result look like using the formula?',
    '2.2': 'At which point in the SiP → KISS → OKR sequence does your organisation typically enter? What is the consequence of skipping the KISS stage?',
    '3.1': 'Which hot zone description most accurately reflects how you instinctively approach OKR definition? What would you need to do differently to write an enterprise-level Key Result?'};
  const OPENING_Q = 'If the Success in Practice we described is the future organisation, what must change in the organisation today to make that future possible?';
  const TEST4 = ['Does this truly get the organisation closer to the shared SiP vision?', 'Would fellow leaders see this as a win for the whole organisation — or just for one function?',
    'Does it visibly improve culture, operations, or value creation?', 'Is there clear accountability for delivering this outcome?'];
  const n = {};

  // ════════════════════════════════════════════════════════════════ FRONT
  n.cover = N(H('UNIT 3 · SiP KISS MAPPING & OKR DEFINITION') + '\nModule 2 · Direction · Unit 3',
    block('UNIT INTENT',
      'Unit overview (facilitator file): This unit guides the leadership team from Success in Practice into a focused, measurable execution architecture — through KISS reflection, OKR construction, and collective prioritisation.', '',
      'Unit 3 converts Success in Practice into a measurable execution architecture. The KISS reflection examines current practice honestly before any target is set; OKRs then express the enterprise priorities that reflection reveals.', '',
      'The six-step path is the core of the unit. It moves executives from functional objectives to enterprise priorities judged on strategic merit.'),
    block('WHAT THE UNIT PRODUCES:',
      'Each group builds three connected outputs, in this order.',
      '1. The KISS map: what the organisation must keep, improve, start and stop to reach its Success in Practice, across the four SiP domains.',
      '2. The Enterprise Priorities: no more than four, each placed on the Prioritisation Matrix.',
      '3. The Enterprise OKRs: one Objective for each priority, with its Key Results and the contributing roles.',
      'The KISS map provides the evidence. The Enterprise Priorities concentrate the energy. The Enterprise OKRs make progress measurable.',
      'Each participant also produces three pieces of individual work: the six-step exercise of Section 2, the matching exercise of Section 3 and one Strategy Airport learning round in Section 5.'),
    block('HOW THE UNIT RUNS:',
      '1. You teach the whole unit from this deck first, from Section 1 to the Unit Summary. The deck is the teaching material. The teaching includes one learning round of the Strategy Airport game, played with the room.',
      '2. Participants then go to the portal and complete their own page, in the session or after it: the reflections, the six-step exercise, the matching exercise, the group work of Section 4 and their own Strategy Airport learning round.',
      '3. Section 4 on the portal is group work for the Capstone. The group agrees each entry and one member acts as scribe.',
      'Every member then types the agreed entries into their own page.',
      '4. The six-step exercise in Section 2, the matching exercise in Section 3 and the game in Section 5 are individual work.'),
    'Each slide’s notes end with a block headed "On the portal, after the teaching" wherever participants have something to complete for that part.',
    'Your preparation as facilitator:\n- Read the Facilitator Guide tab and every section of the facilitator file.\n- Have the facilitator file ready in your browser at Section 5, so that the Strategy Airport game can be shared when you reach it.',
    'Where the outputs go next:\n- The confirmed KISS map, Enterprise Priorities and Enterprise OKRs feed the team’s Capstone Blueprint.');

  n.klo = N(H('KEY LEARNING OUTCOMES'),
    block('HOW TO USE THIS SLIDE:',
      'Read the four outcomes aloud and say where the unit delivers each one.',
      '- Outcome 1 is built in 1.2 and 1.3 (the four KISS filters and the four SiP domains) and produced in 4.1 (the group’s KISS map).',
      '- Outcome 2 is built in 1.5 (the six steps and the Prioritisation Matrix) and in Section 3 (the natural emphasis of each leadership role), and produced in 4.2 (the Enterprise Priorities).',
      '- Outcome 3 is built in 1.4 (Objectives and Key Results) and produced in 4.2 (the Enterprise OKRs) and in 5.1 (the Strategy Airport flight plan).',
      '- Outcome 4 is shown in 2.2 (the worked example, from one SiP statement to its OKRs) and produced in 4.2, where every Key Result names its contributing roles.'),
    'Each section slide carries that section’s two learning outcomes.',
    block('QUESTION TO ASK:', '"Which of these four outcomes would make the largest difference to how your leadership team works today?"'),
    'Take two or three answers. They tell you where the room expects the most from the unit.');

  n.journey = N(H('FACILITATOR GUIDE · SESSION OVERVIEW'),
    block('HOW TO USE THIS SLIDE:',
      '1. Walk the five sections in one sentence each, using the list below.',
      '2. Say plainly that Sections 1 to 3 prepare the thinking, Section 4 is where each group produces its outputs for the Capstone, and Section 5 is a game: played first with the room, then by each participant alone.',
      '3. Tell participants how the unit runs: you teach all five sections from the deck first, and they then complete the unit on the portal, in the session or after it.'),
    block('THE FIVE SECTIONS:',
      '- Section 1 · Awareness — What: KISS (Keep, Improve, Start, Stop), the four SiP domains it is applied to, the anatomy of Objectives and Key Results, and the six steps from KISS output to enterprise OKRs.', '',
      '- Section 2 · Intelligence — Why: why the reflection must come before the targets, and one worked example that follows a SiP statement through KISS and the six steps. Each participant then takes the same case through the six steps alone.', '',
      '- Section 3 · Extrapolating — Where: the natural OKR emphasis of each leadership role, its typical hot zone and its alignment question.', '',
      '- Section 4 · Integration — Collective: each group translates its Success in Practice into a KISS map, then into Enterprise Priorities and Enterprise OKRs.', '',
      '- Section 5 · Application — In Practice: the Strategy Airport game, played with the room in the lesson and then by each participant alone.'));

  // ════════════════════════════════════════════════════════════════ SECTION 1
  n.s1 = divider('SECTION 1 · AWARENESS — WHAT', [
    '1. 1.1: the question that carries the unit, from Success in Practice to action.',
    '2. 1.2 and 1.3: the four KISS filters, and the four SiP domains they are applied to.',
    '3. 1.4: the anatomy of Objectives and Key Results.',
    '4. 1.5: the six steps from KISS output to enterprise OKRs, then Step 6 in detail: the Prioritisation Matrix.',
    '5. The Section 1 Reflections slide: the reflection participants write on the portal after the teaching.'], SLOS[1], [
    S('Link from Unit 2.',
      say('In Unit 2, we built our Strategy Intent Statement and our Success in Practice. Today we answer the harder question: what must actually change in this organisation to make that future real?')),
    S('Read the two section learning outcomes from the slide.', SLO(SLOS[1])),
    S('State the section intent.',
      say('This section establishes the full conceptual architecture of Unit 3: the KISS framework, the OKR anatomy, and the six-step path from KISS output to enterprise OKRs. You need to understand all three before you can do the work.')),
    S('Frame the unit.',
      say('This unit is the bridge between the SiP your group has built and the execution reality you must now create. The KISS reflection is a direct examination of the organisation against the specific future you have described.'),
      'Add: "KISS is a practical act of honesty."'),
    S('Bridge to 1.1.', say('We start with one question.'))]);

  n.p11 = page('1.1 — TRANSLATING SUCCESS IN PRACTICE INTO ACTION (FOUNDATION)', [
    S('Say where each group stands.',
      say('Your group has produced a Strategy Intent Statement and four Success in Practice statements, one for each SiP domain. Together they provide a vivid and shared description of the future organisation: how customers experience the enterprise, how operations function, how people collaborate, and what value the organisation consistently creates.')),
    S('Read the question on the slide aloud.',
      `"${OPENING_Q}"`,
      'Ask participants to sit with it for a moment.'),
    S('Ask for the first answers.',
      ask('What is the one thing that most needs to change in your area to close that gap?'),
      'Take three or four responses. Ask participants to post them in the chat.',
      'Hold back from evaluating any response. Note them: they resurface when the groups build their KISS map in Section 4, and you return to them at the Unit Summary.'),
    S('Say what comes before the targets.',
      say('The next step is to move from this future description to a practical execution agenda. Before defining Objectives and Key Results, the organisation must first examine its current operating reality in relation to the SiP.'), '',
      IN('feed_or_fight')),
    S('Frame the purpose of KISS.',
      say('KISS is a targeted filter applied against the specific future your group has described. Generality is the enemy of this exercise. We push for the operating reality.'),
      EX('A SiP statement says: “Clients receive a response within four hours.”',
        'The operating reality today: response time to customer requests varies across teams, and internal handovers are slow.',
        'The change is specific and it can be acted on: the handovers, and the response standard every team works to.',
        'A general answer such as “we must be more customer-focused” gives the organisation nothing to change.')),
    S('Bridge to 1.2.', say('The Strategy2Results® process gives us a simple filter for this examination. It has four parts.'))]);

  n.p12 = page('1.2 — KISS: KEEP · IMPROVE · START · STOP (4 REFLECTIVE FILTERS)', [
    S('Introduce the filter.',
      say('The Strategy2Results® process introduces a reflective step designed to answer this question. The SiP statements are passed through a simple but powerful filter called KISS: Keep, Improve, Start, Stop. Each element asks you to examine the organisation in relation to the future state described in the SiP.'),
      'Tell participants: we take the four filters one at a time. For each one, they give a live example from their own function, anchored to the SiP.'),
    S('KEEP — Protect what is already working.',
      say('KEEP identifies the practices, capabilities, and behaviours that are already moving the organisation toward the SiP and should therefore be protected and reinforced. These are strategic assets that must not be disrupted in the pursuit of change.'),
      ask('What is already working in your function that the SiP depends on?'),
      'Take two examples.', '',
      IN('keep')),
    S('IMPROVE — Strengthen what is partially working.',
      say('IMPROVE highlights areas where the organisation is already moving in the right direction but where performance, coordination, or capability must strengthen to support the SiP more fully. These are often the highest-leverage interventions.'),
      ask('Where is your function moving in the right direction, with results that are still unreliable?'),
      'Take two examples.'),
    S('START — Introduce what does not yet exist.',
      say('START identifies new practices, capabilities, or initiatives that do not yet exist but will be necessary for the organisation to operate in the way described in the SiP. These represent genuine strategic gaps.'),
      ask('What does the SiP describe that nobody in your organisation is doing yet?'),
      'Take two examples.'),
    S('STOP — Eliminate what contradicts the SiP.',
      say('STOP surfaces activities, routines, or commitments that consume energy and resources but do not contribute to the future organisation described in the SiP. Stopping is often harder than starting — and more strategically valuable.'),
      'STOP is the hardest filter. Stay here longer.',
      ask('What is one thing your function is currently doing that actively contradicts the future we described? What would it take to stop it?'),
      'Silence after this question is productive. Let it run.', '',
      IN('strategic_shelf')),
    S('Pair START with STOP.',
      IN('start_and_stop', 'Say')),
    S('Read the critical principle from the foot of the slide.',
      say('Every KISS reflection must be anchored to the Success in Practice statements. You evaluate the organisation against the future organisation you have collectively described.'),
      'Add: "By grounding the KISS reflection in the SiP, the organisation ensures that its execution agenda is directly aligned with the future it intends to build."'),
    S('Set the standard of specificity.',
      say('When you generate KISS items, be specific. Push for the operating reality.'),
      EX('Too general to act on: “Improve communication.”',
        'A KISS item: “Improve cross-functional handover time from 72 hours to 24 hours.”',
        'The second names what changes, by how much, and where to look for it.'),
      'Tell participants: this is the standard for every entry their group makes in Section 4.'),
    S('Bridge to 1.3.', say('KISS gives us four filters. Next we see where we apply them: the four SiP domains.'))]);

  n.p13 = page('1.3 — THE KISS REFLECTION TABLE: FOUR SiP DOMAINS (4 DOMAINS)', [
    S('Position the table.',
      say('The KISS reflection is structured across the four SiP domains. These are the same four domains in which your group wrote its SiP statements in Unit 2. Each domain has a SiP anchor question to ground the reflection, and one guiding question for each KISS filter.'),
      'Tell participants: this is the preparation for the KISS map their group builds in Section 4.'),
    S('Say how you take the domains.',
      'For each domain, read the SiP anchor question from the slide, then ask:',
      ask('What does your organisation currently look like in this domain — and how far is that from the SiP you described?'),
      'Take one or two answers, then give the four guiding questions of the domain.'),
    ...KD.map(d => S(d.label + '.',
      `SiP anchor, say: "${d.anchor}"`,
      `KEEP, say: "${d.keep}"`,
      `IMPROVE, say: "${d.improve}"`,
      `START, say: "${d.start}"`,
      `STOP, say: "${d.stop}"`)),
    S('Keep the items domain-specific.',
      say('KISS items must be domain-specific. A STOP item in the Customer Experience & Value domain looks different from a STOP item in People & Culture Dynamics. Keeping them separate prevents the vague cross-functional generalisations that make KISS useless.'),
      EX('The same organisation, two domains, two different STOP items.',
        'Customer Experience & Value: “Slow internal handovers that delay customer responses.”',
        'People & Culture Dynamics: “Functional silos and escalation behaviours.”',
        'Each one can be traced to its own SiP statement.')),
    S('Bridge to 1.4.', say('KISS tells us what must change. We now need a way to express that change as measurable progress.'))]);

  n.p14 = page('1.4 — OKR ANATOMY: OBJECTIVES & KEY RESULTS (STRUCTURE & FORMULA)', [
    S('Position OKRs.',
      say('Objective Key Results, OKRs, translate the changes identified in the KISS reflection into measurable progress.'),
      'Add: "The discipline of OKRs lies in their simplicity. Objectives express the strategic ambition. Key Results define what success looks like and by when."'),
    S('Start from the room.',
      ask('Think of a goal your team set in the last 12 months. Was it an Objective, a Key Result, or a task disguised as one of these?'),
      'Take two or three answers. Keep one of them for step 6.'),
    S('Objectives, on the left of the slide.',
      say('Objectives define strategic ambition. An Objective must be qualitative, ambitious, action-oriented, inspirational and memorable. If you cannot wear it on a T-shirt, it is not worth pursuing.'),
      EX('An Objective: “Deliver consistently fast and effortless service experiences for customers.”',
        'It starts with a verb, it describes a transformation, and it carries no number.')),
    S('Key Results, on the right of the slide.',
      say('Key Results define measurable progress. The formula has four elements: Verb of Change, Metric, From X to Y, By Deadline.'),
      'Take the four elements one at a time:',
      '- Verb of Change: indicates the direction of improvement. E.g.: Increase, Reduce, Achieve, Improve, Maintain.',
      '- Metric: a clear and measurable indicator. E.g.: customer satisfaction score, cycle time, adoption rate.',
      '- From X to Y: defines the baseline and target. E.g.: from 40% to 75%. Always establish a starting point.',
      '- Deadline: specifies when the result must be achieved. E.g.: by Q4 2026, by end of FY.',
      EX('A Key Result: “Increase digital transaction completion rate from 40% to 75% of total transactions by Q4 2026.”',
        'Verb of Change: Increase. Metric: digital transaction completion rate. From X to Y: from 40% to 75% of total transactions. Deadline: by Q4 2026.'),
      IN('testable_objectives')),
    S('Land the critical distinction, at the foot of the slide.',
      say('OKRs define outcomes. If a statement can be checked off a task list, such as ‘launch new platform’ or ‘run customer survey’, it is a task. Those are activities that support the Key Result. Key Results describe the impact those activities must produce.'),
      ask('Can you check it off a task list? If yes, it is a task.'),
      'This single test is the most useful tool in the room. Return to it every time a task appears dressed as a Key Result.'),
    S('Work one live example through the formula.',
      'Ask one participant to state a goal they are working toward. Use the goal you kept from step 2 if the room is slow to offer one.',
      'Work it through the four elements with the room: the verb of change, the metric, the baseline and the target, the deadline.',
      'One concrete example does more than ten theoretical ones.', '',
      IN('specific_enough')),
    S('Bridge to 1.5.', say('We have the filter and we have the building blocks. Six steps connect them.'))],
    portal(`Participants write the 1.4 reflection: "${REFL['1.4']}"`));

  n.p15a = page('1.5 — SIX STEPS: FROM KISS OUTPUT TO ENTERPRISE OKRs (6 STEPS)', [
    S('Open.',
      say('Six steps carry the KISS output into enterprise OKRs. We take them in order. Each step builds on the one before it and prepares the next.'),
      'Tell participants: for each step, apply the guiding question mentally to your own area.'),
    S('Step 1 — Find Themes.',
      'Read the guiding question: "What insights emerged from the SiP and KISS reflections?"',
      say('Each leader reviews their KISS reflection. What are the 2–3 big shifts that will contribute to moving the whole organisation forward? The real question is: If the organisation is going to reach the future it has described, what is the one thing my area can change that would make the biggest difference for everyone?'),
      say('Then review the patterns that surfaced across the four SiP domains. Identify the strategic themes that repeatedly appeared in the KEEP, IMPROVE, START, and STOP reflections. These themes represent the most important shifts required to move the organisation toward the SiP.'),
      ask('When you review the KISS reflections across all four domains, what is the pattern? What themes keep appearing?'),
      'Add: "Themes are the connective tissue between scattered KISS observations and purposeful OKRs."',
      'Output produced: a small set of strategic themes that reflect the organisation’s priority execution shifts.'),
    S('Step 2 — Inspiring Objectives.',
      'Read the guiding question: "If we get this theme right, what will we be known for?"',
      say('Each leader gives their themes a voice. Translate each theme into a bold, qualitative statement that expresses strategic ambition. Start with a verb and describe the desired transformation. An Objective should look like a transformation.'),
      ask('If the organisation actually pulls this off, what will customers and competitors say it is known for?'),
      'Give the three standards:',
      '- Make it ambitious: stretch the team.',
      '- Keep it qualitative: describe the destination.',
      '- Keep it memorable: if you cannot say it in a hallway conversation, it is too complex.',
      say('This is the T-shirt test. Try stating an Objective in one sentence before you write it.'),
      'Add: "An Objective should look like a transformation and never like a line in a budget."',
      'Give the room a test for every Objective:',
      say('After each Objective is proposed, ask: Is this statement something we could announce publicly with pride? If the answer is no, it lacks ambition or clarity. Objectives that describe activities, such as ‘Implement new CRM’, are tasks disguised as goals.'),
      'Output produced: a clear Objective that expresses the strategic ambition.'),
    S('Step 3 — Define Key Results.',
      'Read the guiding question: "What measurable outcomes will prove the Objective is being achieved?"',
      say('For every Objective, identify 2–3 measurable results that demonstrate progress toward it. Each Key Result must describe a meaningful shift in performance and must follow the Key Result formula: Verb, Metric, From X to Y, Deadline.'),
      EX('“Shift response time from 12 hours (frustrating) to 4 hours (exceptional) by Q3.”',
        'Use it as the benchmark. Hold each Key Result to the same standard.'),
      say('Quick check: if the team can simply check it off a list, it is a task. Key Results describe outcomes: the actual change in the world that proves the Objective is being achieved.'),
      'Output produced: measurable Key Results that define progress toward the Objective.'),
    S('Step 4 — Alignment Test.',
      say('Before sharing, every leader tests their OKR against four questions.'),
      'Read the four questions aloud:',
      ...TEST4.map((q, k) => `${k + 1}. ${q}`),
      say('The four questions show whether an OKR is enterprise-level or functionally disguised.'), '',
      IN('listening_before_acting')),
    S('Step 5 — Enterprise Priority.',
      say('Once initial OKRs have been drafted, the leadership team determines which Objectives deserve enterprise focus now. Strategy execution fails when too many priorities are pursued simultaneously.'),
      say('Each team member reviews the proposed Objectives and votes on which represent the most critical strategic movements at this moment.'),
      'Give the Less is More Rule:',
      say('No more than 4 Enterprise Objectives. No more than 3 Key Results per Objective. This constraint forces explicit trade-offs and concentrates execution energy on what matters most.'),
      'Add: "This constraint is non-negotiable. The discomfort of trade-offs is the work."',
      'Add: "The Less is More Rule keeps leaders’ energy focused and keeps teams from burning out."', '',
      IN('capacity_for_distinction')),
    S('Step 6 — Priority Matrix.',
      say('The last step places each enterprise priority on the Prioritisation Matrix, by Impact and Effort. The next slide shows the matrix.')),
    S('Show how the steps chain.',
      say('Step 2 defines the Objective from the themes of Step 1. Step 3 defines the Key Results from the Objective of Step 2. Steps 4 to 6 test, select and place what Steps 1 to 3 produce.')),
    S('Bridge to the matrix.', say('We now look at Step 6 in detail.'))]);

  const pmRow = im => PM.filter(c => c.i === im).map(c => `- ${c.l} (${c.i.toLowerCase()} impact, ${c.e.toLowerCase()} effort): ${c.d}`);
  n.p15b = page('1.5 — STEP 6: THE PRIORITISATION MATRIX (IMPACT × EFFORT)', [
    S('Give the two dimensions.',
      say('The Prioritisation Matrix evaluates each initiative against two dimensions. Impact is the degree of strategic value delivered if it is achieved. Effort is the time, resources, coordination, and organisational change required.'),
      say('This structured approach helps distinguish initiatives that accelerate strategic movement from those that consume resources without meaningful progress.')),
    S('Give the question the matrix asks.',
      say('The matrix asks the leadership team to answer a difficult question together: Which of these initiatives will most accelerate our movement toward the Success in Practice?')),
    S('Walk the nine positions on the slide, row by row.',
      'High impact:', ...pmRow('High'), '',
      'Medium impact:', ...pmRow('Medium'), '',
      'Low impact:', ...pmRow('Low')),
    S('Point to the three positions that carry the execution signal.',
      say('Pay particular attention to initiatives in Strategic Catalysts, Accelerated Enablers, and Core Strategic Drivers. These represent the highest leverage execution signals.'),
      'Add: "When the leadership team agrees on what belongs in these three positions, the organisation knows what must move first, what must follow, what must wait and what should stop."'),
    S('Give the guiding questions for placing an initiative.',
      'Impact, ask: "If this initiative succeeds, how strongly will it move us toward our Success in Practice? Will customers feel the difference? Will execution speed improve? Will collaboration improve? Will enterprise value strengthen?"',
      'Effort, ask: "How much organisational coordination is required? How many functions must collaborate? What capability or system changes are required? How much leadership attention is needed?"', '',
      IN('second_cost')),
    S('Say what the low-impact row is for.',
      say('The bottom row matters as much as the top row. It shows where energy is leaking.'),
      IN('protecting_attention')),
    S('Say what the debate is for.',
      say('The debate about what constitutes high impact versus high effort is often more valuable than the final placements. As a team debates a placement, it shows how each function interprets impact, how each function perceives effort, and where assumptions about capability, coordination and resources differ.')),
    S('Close Awareness.',
      say('We now have the full toolkit: KISS as the honest diagnostic, OKR anatomy as the building structure, and the six-step path to connect them. The next two sections explain why this sequence matters and where it typically fails.'))]);

  n.ref1 = reflection(1, [
    S('Show the slide and read the prompt aloud.', `1.4 Reflection: "${REFL['1.4']}"`),
    reflFor(),
    S('Set the standard.',
      say('Name one real goal. Say which of the three it was: an Objective, a Key Result, or a task. Then rewrite it as a Key Result with all four elements: the verb of change, the metric, from X to Y, and the deadline.'),
      'Listen for: a rewritten Key Result with no baseline. Ask: "From what, to what?"'),
    S('Bridge to Section 2.', say('We have the toolkit. Section 2 asks why the sequence matters.'))],
    'Participants write the reflection in Section 1 of the participant file: 1.4 Reflection.');

  // ════════════════════════════════════════════════════════════════ SECTION 2
  n.s2 = divider('SECTION 2 · INTELLIGENCE — WHY', [
    '1. 2.1: the danger of moving straight from vision to targets, and the three human problems it creates.',
    '2. 2.2: the Strategy2Results® sequence (Success in Practice, KISS, OKRs), then one worked example on seven slides: the SiP statement, its KISS table, Steps 1 and 2, then Steps 3, 4, 5 and 6 on one slide each.',
    '3. The Section 2 Reflections slide: the reflection participants write on the portal after the teaching.',
    '4. After the teaching, each participant takes the same case through the six steps alone on the portal, as individual work.'], SLOS[2], [
    S('Ask before you show any content.',
      ask('Has your organisation ever set goals that felt disconnected from the reality of what was actually happening on the ground? Where Key Results became a to-do list that nobody believed in?'),
      'Take three or four answers. Ask participants to post them in the chat.',
      'Use the responses to anchor why the sequence matters before the content begins.'),
    S('Read the two section learning outcomes from the slide.', SLO(SLOS[2])),
    S('State the section intent.',
      say('This section answers the question you may be quietly asking: why can we not just write the OKRs directly? The answer: OKRs without KISS become disconnected targets, fragmented efforts, and activity traps.'),
      'Add: "Most OKR failures are reflection failures. Most of the time, the OKR framework itself is sound."'),
    S('Bridge to 2.1.', say('We start with what goes wrong when an organisation moves too fast.'))]);

  n.p21 = page('2.1 — THE DANGER OF MOVING TOO FAST (3 HUMAN PROBLEMS)', [
    S('Describe the pattern.',
      say('Many organisations dive into OKRs with energy, but that enthusiasm often sours into frustration. Teams end up with vague goals and Key Results that feel like yet another to-do list.')),
    S('Name the usual cause.',
      say('The usual cause of OKR frustration: organisations try to measure progress before they have had an honest conversation about where they are actually standing. When leadership moves straight from a big vision to hard targets, they unintentionally skip the reality check. This creates predictable human problems.')),
    S('Take the three problems on the slide.',
      'Disconnected Targets, say: "People are asked to hit numbers without anyone acknowledging the hurdles that make those numbers nearly impossible."',
      'Fragmented Efforts, say: "Different functions row in different directions because they have not agreed on what success looks like in the trenches."',
      'The Activity Trap, say: "People default to measuring busyness because they are not sure how to prove they are achieving real outcomes."',
      EX('A leadership team sets a target: “Grow client revenue by 20% this year.”',
        'Sales pursues new accounts. Operations is measured on cost and reduces service cover. Nobody has said that response time to existing clients already varies across teams.',
        'All three problems are present: a target disconnected from the hurdle, functions rowing in different directions, and busyness reported as progress.')),
    S('Ask the room to recognise itself.',
      ask('Which of these three describes your organisation’s most recent goal-setting cycle most accurately?'),
      'Take a show of hands for each problem, or quick responses in the chat, and say what the pattern in the room is.',
      'The near-universal recognition of at least one pattern is itself the lesson.'),
    S('Say what the skipped reality check costs.', IN('stopping_at_convenient')),
    S('Read the closing line from the foot of the slide.',
      say('Essentially, the organisation starts measuring the finish line before it has mapped the terrain.'),
      ask('What does ‘mapping the terrain’ mean practically — and what does KISS give us that we do not currently have?'), '',
      IN('claiming_early')),
    S('Bridge to 2.2.', say('KISS is the map of the terrain. The next slide shows where it sits in the sequence.'))]);

  n.p22a = page('2.2 — TURNING INTENT INTO ACTION: THE STRATEGY2RESULTS® SEQUENCE (3-PART LOGIC)', [
    S('Introduce the sequence.',
      say('Once these patterns are visible, strategy stops being a deck of slides and starts being a shared journey. The Strategy2Results® sequence makes the path forward clear and respectful of the people walking it.')),
    S('Success in Practice.',
      say('Success in Practice is the dream of where the organisation wants to be: the vivid future state across the four SiP domains.')),
    S('KISS.',
      say('KISS is the honest look at the changes required to get there. It is the bridge between the future and the present reality.'), '',
      IN('know_what_you_have')),
    S('OKRs.',
      say('OKRs are the manageable, measurable steps taken to prove the organisation is moving. They are the execution compass.')),
    S('Locate the room in the sequence.',
      ask('Which stage is your organisation at in its current strategic cycle: Success in Practice, KISS or OKRs?'),
      'Take one answer from each group. This gives a live picture of where the room’s execution journey currently sits.'),
    S('Put the question at the foot of the slide to the room.',
      ask('At which point in this sequence does our organisation typically enter? Do we skip the KISS reality check and jump straight to targets?'),
      'The honest answer often unlocks the conversation about why previous goal-setting cycles felt frustrating.'),
    S('Say what the sequence gives.',
      say('When this sequence is respected, OKRs become a way for the organisation to learn, breathe, and align. Strategy transforms from a statement of intent into a living system that actually helps people succeed.'), '',
      IN('sequenced_execution')),
    S('Bridge to the worked example.',
      say('We now follow one simple SiP statement through the whole sequence: first through the KISS filters, then through the six steps.'))]);

  n.p22b = page('2.2 — WORKED EXAMPLE · THE SiP STATEMENT', [
    S('Introduce the example.',
      say('This is a client services company. It has written one simple SiP statement. We follow it through the whole sequence.'),
      'Tell participants: the same SiP statement and KISS table are in 2.2 of their own page. After the teaching, each of them takes this case through the six steps alone.'),
    S('Read the SiP statement from the slide.',
      `"${W.sip}"`,
      ask('Which words in this statement belong to each of the four SiP domains?'),
      'Listen for: fast, consistent and effortless service (Customer Experience & Value); insight to action across functions (Operational Capability & Execution Rhythm); shared ownership of enterprise priorities (People & Culture Dynamics); scalable, efficient operations and enterprise performance (Enterprise Value Creation).'),
    S('Bridge to the KISS table.', say('The statement describes the future. The leadership team now examines the organisation of today against it.'))]);

  n.p22k = page('2.2 — WORKED EXAMPLE · THE KISS TABLE', [
    S('Pass the statement through KISS, one SiP domain at a time.',
      say('The leadership team passes the SiP statement through the four KISS filters, one SiP domain at a time.')),
    S('Read the first domain from the slide: Customer Experience & Value.',
      ...[W.kiss[0]].flatMap(d => [`- KEEP: ${d.keep}`, `- IMPROVE: ${d.improve}`, `- START: ${d.start}`, `- STOP: ${d.stop}`]),
      ask('Which words of the SiP statement do these four entries answer to?'),
      'Listen for: fast, consistent and effortless service.'),
    S('Give the other three domains aloud.',
      'The same four filters are applied to each of the other three SiP domains:',
      ...W.kiss.slice(1).flatMap(d => ['', d.domain, `- KEEP: ${d.keep}`, `- IMPROVE: ${d.improve}`, `- START: ${d.start}`, `- STOP: ${d.stop}`])),
    S('Test the entries against the standard of 1.2.',
      ask('Which of these entries is specific enough to act on? Which one would you send back for more detail?'),
      'Listen for: “Clear strategic priorities already exist” named as too general. Ask: "What would make it specific?"'),
    S('Bridge to the six steps.', say('This KISS table is the evidence. The six steps now turn it into enterprise OKRs.'))]);

  const NUM = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven'];
  const nI = W.items.length, PRI = W.items.filter(o => o.pri), OUT = W.items.filter(o => !o.pri);
  n.p22c = page('2.2 — WORKED EXAMPLE · STEPS 1 AND 2: FROM THEMES TO OBJECTIVES', [
    S('Step 1 — Find Themes.',
      say(`Reading across the four domains of the KISS table, the leadership team finds ${NUM[nI]} patterns that keep appearing. Each becomes a strategic theme.`),
      `Name the ${NUM[nI]} themes and the shift each one carries:`,
      ...W.items.map((o, k) => `${k + 1}. ${o.theme}: ${o.shift}`)),
    S('Trace one theme back to the table.',
      say('Take the first theme. Response time to customer requests varies across teams: that was the IMPROVE entry. Slow internal handovers: that was the STOP entry. A proactive customer engagement model: that was the START entry. Three entries, one theme: customer responsiveness.')),
    S('Step 2 — Inspiring Objectives.',
      say('Each theme from Step 1 is translated into a bold, qualitative statement that starts with a verb and describes the transformation.'),
      `Read the ${NUM[nI]} Objectives from the slide:`,
      ...W.items.map((o, k) => `${k + 1}. ${o.theme} → ${o.obj}`),
      say('Notice how the KISS item maps directly to the Objective. There is no gap. The Objective is the direct consequence of what the KISS reflection surfaced.')),
    S('Apply the T-shirt test.',
      ask(`Which of these ${NUM[nI]} Objectives would you wear on a T-shirt? Which one is hardest to say in a hallway conversation?`),
      say('Each Objective is qualitative, ambitious, action-oriented and memorable. If you cannot wear it on your T-shirt, it is not worth pursuing.')),
    S('Bridge to Step 3.', say('An Objective carries no number. The numbers come next.'))]);

  const o1 = W.items[0], o2 = W.items[1];
  n.p22d = page('2.2 — WORKED EXAMPLE · STEP 3: KEY RESULTS', [
    S('Step 3 — Define Key Results.',
      say('Each Objective from Step 2 receives two Key Results in the form Verb, Metric, From X to Y, Deadline, with the contributing roles named.'),
      'Read the two OKRs on the slide:',
      `Objective 1 · ${o1.obj}`, ...o1.krs.map(k => `- ${k}`), `- Contributing roles: ${o1.roles}`, '',
      `Objective 2 · ${o2.obj}`, ...o2.krs.map(k => `- ${k}`), `- Contributing roles: ${o2.roles}`),
    S('Check the formula with the room.',
      ask('In the first Key Result of Objective 1, what is the verb of change? The metric? The baseline and the target? The deadline?'),
      'Listen for: Reduce · average response time to customer requests · from 12 hours to 4 hours · by 30 June 2027.'),
    S(`Give the Key Results of the other ${NUM[nI - 2]} Objectives.`,
      ...W.items.slice(2).flatMap((o, k) => ['', `Objective ${k + 3} · ${o.obj}`, ...o.krs.map(x => `- ${x}`), `- Contributing roles: ${o.roles}`])),
    S('Say why the contributing roles are named.',
      say('Every Key Result names the roles that must contribute to it. This is the link between each outcome, its contributing roles and the evidence of progress.')),
    S('Bridge to Step 4.', say(`${NUM[nI][0].toUpperCase() + NUM[nI].slice(1)} OKRs are drafted. Before they go forward, each one is tested.`))]);

  n.p22t = page('2.2 — WORKED EXAMPLE · STEP 4: THE ALIGNMENT TEST', [
    S('Step 4 — Alignment Test.',
      say('Before the OKRs of Step 3 go forward, each one is tested against the four questions on the slide.'),
      'Take the four questions and the answers the team gave for Objective 1:',
      ...W.test.flatMap(t => [`- ${t[0]}`, `  ${t[1]}`])),
    S('Read the result of the test from the slide.',
      ...W.items.map((o, k) => `- Objective ${k + 1} · ${o.theme}: 4 of 4. Goes forward to Step 5.`),
      `- Draft from one function · “${W.failed.draft}”: ${W.failed.score} of 4. Returned to Step 2.`),
    S('Show why the draft failed.',
      say(`One further draft came from one function: ‘${W.failed.draft}.’ It earned one of four. ${W.failed.why} It returns to Step 2.`),
      ask('What outcome would that platform have to produce to earn a place as a Key Result?')),
    S('Say what Step 4 hands to Step 5.',
      say(`The output of Step 4 is the input of Step 5: ${NUM[nI]} OKRs that the whole enterprise can stand behind.`)),
    S('Bridge to Step 5.', say(`${NUM[nI][0].toUpperCase() + NUM[nI].slice(1)} OKRs have passed. The Less is More Rule allows four.`))]);

  n.p22v = page('2.2 — WORKED EXAMPLE · STEP 5: ENTERPRISE PRIORITY', [
    S('State what Step 5 decides.',
      say(`${NUM[nI][0].toUpperCase() + NUM[nI].slice(1)} OKRs passed the alignment test in Step 4. The Less is More Rule allows no more than 4 Enterprise Objectives. The leadership team must decide which four deserve enterprise focus now.`)),
    S('Ask the room before you read the vote.',
      ask('Which Objective would you release, and what would that decision cost?'),
      'Take two or three answers. Ask participants to post their choice in the chat.'),
    S('Read the vote from the slide.',
      say(`Each of the ${NUM[W.voters]} members of the leadership team votes for the ${NUM[W.votesEach]} Objectives that represent the most critical strategic movements at this moment.`),
      ...W.items.map((o, k) => `- Objective ${k + 1} · ${o.theme}: ${o.votes} ${o.votes === 1 ? 'vote' : 'votes'}. ${o.pri ? 'Enterprise priority.' : 'Released for this cycle.'}`)),
    S('Read the trade-off.',
      say(W.tradeoff),
      'The team names what it releases and why.', '',
      IN('open_door')),
    S('Run the Less is More check.',
      say(`${PRI.length} Enterprise Objectives: the maximum is 4. Two Key Results for each Objective: the maximum is 3.`),
      'Add: "The discomfort of trade-offs is the work."'),
    S('Bridge to Step 6.', say(`The ${NUM[PRI.length]} enterprise priorities go forward to Step 6.`))]);

  const place = o => { const c = PM.find(p => p.i === o.impact && p.e === o.effort); return `${c.l} (${o.impact.toLowerCase()} impact, ${o.effort.toLowerCase()} effort)`; };
  const order = [1, 0, 2, 3];
  n.p22e = N(page('2.2 — WORKED EXAMPLE · STEP 6: THE PRIORITISATION MATRIX', [
    S('Step 6 — Priority Matrix.',
      say(`The ${NUM[PRI.length]} enterprise priorities confirmed in Step 5 are placed on the Prioritisation Matrix by Impact and Effort.`),
      `Read the ${NUM[PRI.length]} placements from the slide:`,
      ...order.map(i => `- Objective ${i + 1} · ${W.items[i].theme}: ${place(W.items[i])}.`)),
    S('Test one placement with the room.',
      ask('Why is execution speed placed at low effort, while collaboration culture is placed at high effort?'),
      'Listen for: execution speed begins with stopping reporting cycles and opening faster decision forums; shared ownership asks leaders in every function to change how they behave.'),
    S('Read the execution signal.',
      say('The execution signal: ' + W.signal)),
    S('Set the standard for the room.',
      ask('At this level of specificity, could you trace every OKR back to a specific KISS observation?'),
      say('That is the standard we are working toward.')),
    S('Hand the case to the participants.',
      say('After the teaching, each of you takes this same case through the six steps alone, in 2.2 of your own page. Your page gives you the SiP statement and the KISS table. The themes, the Objectives, the Key Results, the alignment test, the enterprise priorities and the matrix positions are yours to work out, from Step 1 to Step 6. Each step shows what you recorded in the steps before it, and your six-step record builds above the steps. Your answers may differ from this example and still be sound, provided each one can be traced to the KISS table. This is individual work. It is saved on your page and reaches me when you submit the unit.')),
    S('Close Intelligence.',
      say('Now we know why the sequence matters. The next section maps where it most commonly breaks down — and which leadership role is most responsible for each break point.'))]),
    portal('Each participant completes the six-step exercise in 2.2 of the participant file, as individual work: the case gives the SiP statement and the KISS table, and the participant completes Step 1 to Step 6, marks the exercise complete and can print the six-step record.',
      'They then write the 2.2 reflection.'),
    block('AFTER THE SESSION:',
      'Each participant’s exercise reaches you with the submission, under the heading Six-Step Exercise.',
      'The worked example in 2.2 of the facilitator file is your reference. A participant’s themes and Objectives may differ from it and still be sound, provided each one can be traced to the KISS table, each Key Result follows the formula, and no more than four enterprise priorities are selected.'));

  n.ref2 = reflection(2, [
    S('Show the slide and read the prompt aloud.', `2.2 Reflection: "${REFL['2.2']}"`),
    reflFor(),
    S('Set the standard.',
      say('Name the point of entry: Success in Practice, KISS or OKRs. Give one piece of evidence from your organisation’s last planning cycle. Then name one consequence you have seen when the KISS stage was skipped.'),
      'Listen for: a consequence stated as a feeling, such as “people were frustrated”. Ask: "What did it cost, slow down or leave undecided?"'),
    S('Bridge to Section 3.', say('We know the sequence and why it matters. Section 3 asks where it breaks down.'))],
    'Participants write the reflection in Section 2 of the participant file: 2.2 Reflection.');

  // ════════════════════════════════════════════════════════════════ SECTION 3
  n.s3 = divider('SECTION 3 · EXTRAPOLATING — WHERE', [
    '1. 3.1a: the natural OKR emphasis of commercial, operational, people and financial leaders.',
    '2. 3.1b: the four execution risks when that emphasis stays unexamined.',
    '3. 3.1c: one hot zone card in full, as the pattern for all ten leadership roles.',
    '4. 3.1d: the matching exercise that each participant completes alone on the portal after the teaching.',
    '5. The Section 3 Reflections slide.'], SLOS[3], [
    S('Frame the section.',
      say('Before we start writing OKRs together, it helps to know the natural biases each of us brings to the table. This section maps those patterns so the team can compensate for them collectively.')),
    S('Read the two section learning outcomes from the slide.', SLO(SLOS[3])),
    S('State the section intent.',
      say('This section does for OKR definition what Unit 2’s Extrapolating section did for the SiP: it maps where the process predictably breaks down, and who is responsible for each break. The hot zone cards are the diagnostic instrument. The goal is to make the systemic pattern visible before it plays out in the room.')),
    S('Bridge to 3.1.', say('We begin with four tendencies that every leadership team carries.'))]);

  n.p31a = page('3.1 — NATURAL OKR EMPHASIS ACROSS LEADERSHIP FUNCTIONS · THE FOUR TENDENCIES', [
    S('Give the starting point.',
      say('Every leadership role tends to emphasise some of the four SiP domains more strongly than others. Each role carries responsibility for specific organisational outcomes, so leaders instinctively prioritise the realities that sit closest to their domain.'),
      'Recall the four SiP domains in one line each:',
      '- Customer Experience & Value: how customers experience the organisation.',
      '- Operational Capability & Execution Rhythm: how the enterprise operates internally.',
      '- People & Culture Dynamics: how leaders and teams collaborate.',
      '- Enterprise Value Creation: the outcomes that confirm success.'),
    S('Read the four tendencies from the slide.',
      say('This creates a natural imbalance in how OKRs are proposed and evaluated.'),
      '- Commercial leaders emphasise Customer Experience & Value and Enterprise Value Creation.',
      '- Operational leaders emphasise Operational Capability & Execution Rhythm and Enterprise Value Creation.',
      '- People leaders emphasise People & Culture Dynamics and Operational Capability & Execution Rhythm.',
      '- Financial leaders emphasise Enterprise Value Creation and Operational Capability & Execution Rhythm.'),
    S('Ask each participant to place themselves.',
      'Ask each participant to identify privately which category their natural OKR emphasis falls into. Then ask three or four to share.',
      ask('Which SiP domain do your own objectives most often leave out?')),
    S('Reinforce the key point.',
      say('Each perspective reflects an important dimension of strategy execution, and each one is valid. The problem arises when these perspectives remain unexamined and unchallenged.'),
      say('The purpose of this part is to make the invisible visible before OKR writing begins, so that your group can consciously compensate.'), '',
      IN('differentiated_strategy')),
    S('Read the line at the foot of the slide and bridge.',
      say('When these perspectives remain unexamined, OKRs gradually drift into functional scorecards, and the organisation accumulates functional OKRs where enterprise OKRs are needed. The next slide names the risks.'))]);

  n.p31b = page('3.1 — NATURAL OKR EMPHASIS ACROSS LEADERSHIP FUNCTIONS · THE FOUR EXECUTION RISKS', [
    S('Read each risk aloud, one at a time.',
      'After each one, ask for a show of hands:',
      ask('Have you personally experienced this in a previous goal-setting cycle?'),
      '1. Competing definitions of success across functions',
      '2. Fragmented measurement systems that cannot be integrated',
      '3. Functional optimisation that stalls enterprise progress',
      '4. Slow decision-making due to misaligned incentives',
      'The near-universal recognition creates the readiness to work differently in the Integration section.'),
    S('Deepen the first risk.',
      IN('no_governing_centre'),
      EX('One organisation, one quarter. Sales reports record revenue. Operations reports record cost savings. Client complaints rise in the same quarter.',
        'Each function has met its own definition of success. Nobody owns the client’s experience of all three.')),
    S('Name the shift.',
      say('When the leadership team names its natural biases explicitly, the conversation shifts from functional interpretation of success to collective definition of success.'),
      ask('What is the difference between a functional interpretation of success and a collective definition of success? What does that difference look like in a room full of leaders with different mandates?'),
      'This is the conversation the Integration section is designed to produce.'),
    S('Read the line at the foot of the slide.',
      say('Recognising these patterns allows the leadership team to integrate perspectives into a balanced execution system that reflects the full enterprise.')),
    S('Bridge to the hot zone card.', say('Each leadership role has a typical hot zone and an alignment question. We look at one role in full.'))]);

  const ceo = hz('CEO');
  const card = h => [`- Dominant Future Realities: ${h.top2}`, `- Natural OKR Emphasis: ${h.emphasis}`, `- Typical Hot Zone: ${h.hot}`, `- Alignment Question: ${h.align}`];
  n.p31c = page('3.1 — NATURAL OKR EMPHASIS ACROSS LEADERSHIP FUNCTIONS · A HOT ZONE CARD', [
    S('Define the two terms.',
      say('Each leadership role has a typical hot zone: the point where its natural emphasis distorts the OKRs it proposes. Each role also has an alignment question that challenges it toward enterprise thinking.')),
    S('Read the card on the slide: the Chief Executive Officer.',
      ...card(ceo),
      say('Read the card from top to bottom. The emphasis is a strength. The hot zone is the same strength left unexamined. The alignment question brings the role back to the enterprise.')),
    S('Ask how the hot zone follows from the emphasis.',
      ask('How does the hot zone follow from the emphasis?'),
      'Listen for: a role whose ambition runs ahead of what operations can deliver, because operational capability sits with other functions.'),
    S('Hold the other roles back.',
      `There are ten roles: ${HZ.map(h => h.role).join(', ')}. Teach this one card only.`,
      'Participants match all ten in the exercise on the next slide. The ten complete cards are in 3.1 of the facilitator file for your own preparation.'),
    S('Ask the room to look ahead.',
      ask('If all ten of these hot zones operated simultaneously in our OKR work — what would our final OKR landscape look like? Which domains would be over-represented, and which would be left out?')),
    S('Give each participant something to carry.',
      say('The matching exercise shows you the alignment question of your own role. Keep it in front of you throughout the group work in Section 4. It is your personal quality check on every OKR you propose.')),
    S('Give the groups one move to use.',
      say('After a leader describes an OKR perspective, ask the room: Which hot zone does this perspective risk creating? Name the imbalance explicitly.'),
      'Add: "This builds collective intelligence by surfacing what each function cannot see about itself."')]);

  n.p31d = N(page('3.1 — NATURAL OKR EMPHASIS ACROSS LEADERSHIP FUNCTIONS · THE MATCHING EXERCISE', [
    S('Say what the exercise is.',
      say('After the teaching, each of you works through the ten leadership roles on the slide. For each role, the Dominant Future Realities and the Natural OKR Emphasis are suggested. You match the Typical Hot Zone and the Alignment Question that belong to that role.')),
    S('Say how the page answers.',
      say('The page shows a green light for a match and a red alert when your choice belongs to another role. You then choose again.')),
    S('Say that it is individual work.',
      say('This is individual work. Complete it on your own. Your matches are saved on your page and reach me when you submit the unit.')),
    S('Give the method.',
      say('Read the emphasis first. Ask what that strength produces when nobody examines it: that is the hot zone. Then ask which question would bring the role back to the enterprise: that is the alignment question.')),
    S('Close Extrapolating.',
      say('We now know what biases we each bring into the room. The Integration section is where we use that awareness to build something none of us could build alone.'))],
    portal('Each participant completes the matching exercise in 3.1 of the participant file, as individual work: ten roles, with the Typical Hot Zone and the Alignment Question matched to each one.',
      'They then write the 3.1 reflection.')),
    block('AFTER THE SESSION:',
      'Each participant’s matches reach you with the submission, with the number of attempts for each role.',
      'The ten complete cards in 3.1 of the facilitator file are your answer key.'));

  n.ref3 = reflection(3, [
    S('Show the slide and read the prompt aloud.', `3.1 Reflection: "${REFL['3.1']}"`),
    reflFor(),
    S('Start the thinking in the room.',
      ask('Which of these descriptions resonates most with how you instinctively write Key Results?'),
      'Take two answers.'),
    S('Set the standard.',
      say('Name one hot zone description. Give one objective or Key Result you have written that shows it. Then say what you would do differently: which SiP domain you would add, and which role you would consult.')),
    S('Bridge to Section 4.', say('We know the filter, the building blocks, the steps and our own biases. Section 4 is where your group builds.'))],
    'Participants write the reflection in Section 3 of the participant file: 3.1 Reflection.');

  // ════════════════════════════════════════════════════════════════ SECTION 4
  n.s4 = divider('SECTION 4 · INTEGRATION — COLLECTIVE', [
    '1. 4.1a: how the group works. One scribe, agreed entries, every member’s own page.',
    '2. 4.1b: Translating SiP to KISS. The group’s four SiP statements, the sixteen entries of the KISS map, and its confirmation.',
    '3. 4.2a: Translating KISS to OKRs through the six steps.',
    '4. 4.2b: the three confirmed outputs, and how they reach the Capstone.',
    'You explain both steps from the slides. The groups do the work itself on the portal after the teaching, in the session or after it.'], SLOS[4], [
    S('State the section intent.',
      say('This is the production section of the unit, and it is Capstone work. Everything in Awareness, Intelligence, and Extrapolating has been preparation for this.')),
    S('Read the two section learning outcomes from the slide.', SLO(SLOS[4])),
    S('Give the two connected stages.',
      say('Your group works through two connected stages.'),
      '- 4.1 — Translating SiP to KISS: pass each of your four SiP statements through the four KISS filters and confirm your KISS map.', '',
      '- 4.2 — Translating KISS to OKRs: The Six Steps: convert the confirmed KISS map into Enterprise Priorities and Enterprise OKRs.', '',
      say('Each output is the foundation for the next: Success in Practice, then KISS, then OKRs.')),
    S('Frame the goal.',
      say('The goal of this section is to find the few, vital Enterprise OKRs that will shift the needle for the entire organisation. Departments contribute the insight. The enterprise owns the results.'),
      'Add: "When the focus is on departments, the organisation just gets better silos. When the focus is on the enterprise, it actually executes its strategy."'),
    S('Say why the work is collective.',
      say('Each of you starts from the perspective of your own role. That is your expertise, and it is why you are at the table. The work now is to move beyond functional goals.'))]);

  n.p41a = page('4.1 — TRANSLATING SiP TO KISS · HOW THE GROUP WORKS', [
    S('Explain how the group works, using the four lines on the slide.',
      say('Your group agrees each entry. One member acts as scribe and types the agreed wording. Every member then types the agreed entries into their own page, in the session or after it.')),
    S('Say why every member’s page matters.',
      say('Your own page is what I review. It is also where your team’s Capstone Blueprint later takes the confirmed outputs from.')),
    S('Ask for individual thinking first.',
      say('For each SiP domain, write your own inputs first. Then share them and agree your group’s entries. This prevents the first speaker from dominating the KISS landscape.')),
    S('Ask for every voice.',
      say('The scribe types what the whole group has agreed. Every member speaks before an entry is typed.'),
      IN('seniority_and_challenge')),
    S('Explain confirmation.',
      say('Your group confirms each output once it says what your group means. An entry that is edited after confirmation must be confirmed again.')),
    S('Confirm the groups.',
      'Confirm who is in each group, and ask each group to name its scribe before the work begins. Each group continues with the Success in Practice it built in Unit 2.')],
    portal('The group agrees each entry and one member acts as scribe.',
      'Every member then types the agreed entries into their own page of the participant file, in the session or after it.'),
    later('- Move between the groups. Listen to a group before you speak to it.',
      '- Protect the sequence. A group that writes Objectives before its KISS map is confirmed is working without its evidence.',
      '- Hold every group to one enterprise position. A set of functional lists placed side by side falls short of collective construction.'));

  n.p41b = page('4.1 — TRANSLATING SiP TO KISS (4 DOMAINS · GROUP WORK)', [
    S('State the purpose.',
      say('Your group’s four SiP statements describe the future organisation. In this step you pass each statement through the four KISS filters and record what the organisation must keep, improve, start and stop to reach it.')),
    S('Say where the SiP statements come from.',
      say('At the top of 4.1 you find your group’s four SiP statements, brought in from your Unit 2 page. Read each one with your group. Where your team has since refined a statement in the Capstone Blueprint, type the confirmed wording in the box.')),
    S('Explain the KISS map, using the lines on the slide.',
      say('Take one SiP domain at a time. Read the domain’s SiP statement, then answer the four guiding questions with your group: Keep, Improve, Start, Stop. These are the guiding questions of 1.3. Four domains, four filters: sixteen entries.')),
    S('Set the anchor.',
      say('Every item you enter must be anchored to the SiP.'),
      EX('“We should improve cross-functional handover time from 72 to 24 hours because the SiP describes seamless execution rhythm.”',
        'The entry names the change and the SiP statement that asks for it.')),
    S('Ask for selection.',
      say('Aim for 3–4 items per KISS element per domain. More than 5 items per element means the group has not prioritised.')),
    S('Explain confirmation.',
      say('When all sixteen boxes are complete, read the map across the four domains as a group and confirm it. Your confirmed KISS map is the source for 4.2.')),
    S('Say where the map goes.',
      say('Your confirmed Keep, Improve, Start and Stop feed your team’s Capstone Blueprint.')),
    S('Bridge to 4.2.',
      say('After all four domains are captured, look across them. The patterns that keep appearing become the themes of 4.2.'))],
    portal('In 4.1 of the participant file, the group:',
      'reads its four SiP statements at the top of the part, brought in from each member’s Unit 2 page;',
      'answers the four KISS guiding questions for each SiP domain: sixteen entries;',
      'confirms its KISS map.',
      'The group agrees each entry, and every member types the agreed entries into their own page.'),
    later('- Insist on specificity. When a group offers “improve communication”, ask: "Improve what, from what, to what?"',
      '- Push for selection when a box holds more than five items.',
      '- When all four domains are captured, ask the group: "Look across all four domains. What are the 2–3 patterns that keep appearing? What does the organisation most consistently need to START, STOP, or IMPROVE relative to the SiP?"',
      '- A group whose SiP boxes are empty types its four SiP statements from Unit 2 into them before it starts.'));

  n.p42a = page('4.2 — TRANSLATING KISS TO OKRs: THE SIX STEPS (6 STEPS · GROUP WORK)', [
    S('Link the step to the one before it.',
      say('With your KISS map confirmed, your group converts it into enterprise OKRs through the six steps of 1.5. Work through the steps in order. Each step shows what your group recorded in the steps before it, so you always see what you are working on.')),
    S('Step 1 — Find Themes.',
      say('Each member first writes down the 2–3 big shifts they see in the KISS map. Share them, then agree your group’s themes. A theme names one shift the organisation must make to reach the SiP. Your group records up to six themes.'),
      'Add: "Written themes prevent the anchoring bias where the first speaker dominates the room."'),
    S('Step 2 — Inspiring Objectives.',
      say('Each theme from Step 1 is shown in Step 2. Your group writes one Objective under each theme. Draft your Objective privately first, then agree the group’s wording. The T-shirt test applies: if you cannot say it in a hallway conversation, simplify it.')),
    S('Step 3 — Define Key Results.',
      say('Each Objective is shown in Step 3 with its theme. Under each Objective, your group writes two or three Key Results in the formula, and names the contributing roles for each Key Result. Every Key Result carries a baseline, a target and a deadline.'),
      say('Hold each Key Result to the benchmark: shift response time from 12 hours to 4 hours by Q3.')),
    S('Step 4 — Alignment Test.',
      say('Each OKR is shown in Step 4 in full: the theme, the Objective and its Key Results. An Objective needs two Key Results before it is tested. Run the four-question test publicly. One member reads the OKR and the group answers the four questions aloud. Tick a question only when the answer is a clear yes. An OKR that cannot earn all four ticks goes back to Step 2 or Step 3.')),
    S('Step 5 — Enterprise Priority.',
      say('The OKRs that passed the alignment test are shown in Step 5 in full. Your group decides which of them deserve enterprise focus now. The Less is More Rule applies: no more than four Enterprise Objectives.'),
      say('The discomfort of trade-offs is the work.')),
    S('Step 6 — Priority Matrix.',
      say('Each enterprise priority you selected is shown in Step 6. Place it on the matrix by its Impact and its Effort. Before you place the first one, agree what high impact and high effort mean for your organisation: time, money, change management, or all three.')),
    S('Explain the six-step record.',
      say('Above the steps your six-step record builds from Step 1, theme by theme: the theme, its Objective, its Key Results, the alignment test, the enterprise priority and the matrix position. It is saved on your page. When the six steps are complete, read the record together, confirm your Enterprise Priorities and your Enterprise OKRs, then print the record.'))],
    portal('In 4.2 of the participant file, the group works through the six steps:',
      'records up to six themes from its confirmed KISS map;',
      'writes one Objective under each theme;',
      'writes two or three Key Results under each Objective, with the contributing roles;',
      'applies the four-question alignment test to each OKR, shown with its theme, Objective and Key Results;',
      'chooses no more than four of the OKRs that passed as enterprise priorities;',
      'places each priority on the Prioritisation Matrix;',
      'reads its six-step record, confirms its Enterprise Priorities and its Enterprise OKRs, and prints the record.',
      'The group agrees each entry, and every member types the agreed entries into their own page.'),
    later('- Step 1: collect all themes before any discussion begins.',
      '- Step 3: apply the four-part formula rigorously. When a Key Result reads as an activity, ask: "Can you check it off a task list?"',
      '- Step 4: ask each leader to read their OKR and answer the four questions aloud. The room quickly shows whether the OKR is enterprise-level or functionally disguised.',
      '- Step 5: enforce the Less is More Rule: maximum 4 Enterprise Objectives, maximum 3 Key Results per Objective. This constraint is non-negotiable.',
      '- Step 6: as the team debates placements, listen for disagreements about what constitutes high impact and high effort. These disagreements are where collective intelligence is built. Hold back from a quick consensus: the quality of the debate is as valuable as the final placement.',
      '- Use the hot zones. After a leader describes an OKR, ask the room: "Which hot zone does this perspective risk creating?"'));

  n.p42b = N(page('4.2 — TRANSLATING KISS TO OKRs · THE THREE CONFIRMED OUTPUTS', [
    S('Show the three outputs side by side.',
      say('When the work is done, each group holds three confirmed outputs: its KISS map, its Enterprise Priorities and its Enterprise OKRs.')),
    S('Reinforce the connection, using the three lines on the slide.',
      say('The KISS map provides the evidence. The Enterprise Priorities concentrate the energy. The Enterprise OKRs make progress measurable.')),
    S('Say whose OKRs these are.',
      say('These OKRs belong to the entire enterprise. They are the collective outcomes that, as a leadership system, you commit to delivering together.'),
      'Add: "If the Success in Practice is the organisation’s destination and the KISS reflection is the reality check, these Enterprise OKRs are the organisation’s compass."'),
    S('Say how the outputs reach the Capstone.',
      say('Your confirmed outputs feed your team’s Capstone Blueprint. Its Unit 3 section opens once every member of your team has completed Unit 3, and brings the confirmed outputs in from a member’s page: Keep, Improve, Start, Stop, Enterprise Priorities and Enterprise OKRs. Your team reads them together and confirms them there.')),
    S('Bridge to Section 5.',
      say('Section 4 is collective: one group, one KISS map, one set of OKRs. Section 5 is individual, and it is a game.'))]),
    block('LATER, WHEN THE GROUPS HAVE DONE THE WORK:',
      '- Invite each group to read one Enterprise OKR to the room: the Objective, its Key Results and the contributing roles.',
      '- After each group, ask the room: "Could you trace this OKR back to a specific KISS observation?"',
      '- Remind every member to complete their own page with the group’s agreed entries, in the session or after it, and to confirm each output on that page.'));

  // ════════════════════════════════════════════════════════════════ SECTION 5
  n.s5 = divider('SECTION 5 · APPLICATION — IN PRACTICE', [
    '1. 5.1: the Strategy Airport game. You play one learning round with the room, from the facilitator file.',
    '2. After the teaching, each participant plays the same game alone on the portal and submits it with the unit.',
    '3. The Unit Summary.'], SLOS[5], [
    S('State the section intent.',
      say('This is the application section. You have seen the full path from Success in Practice to KISS to OKRs. Strategy Airport lets you apply it to a case you have not met: first together in this lesson, then on your own.')),
    S('Read the two section learning outcomes from the slide.', SLO(SLOS[5])),
    S('Name the shift.',
      say('Section 4 is collective: one group, one position. Section 5 is individual: one participant, one learning round.'))]);

  const opt = (k, i) => D.SA_OPTIONS[k][i];
  n.p51 = N(page('5.1 — STRATEGY AIRPORT (2 GATES · LEARNING ROUND)', [
    S('Share the game.',
      'Stop sharing the deck and share the browser window that holds the facilitator file, at Section 5. Have that page ready before the lesson begins.',
      'Return to the deck when the learning round is complete.'),
    S('Introduce the game.',
      say('This is Strategy Airport. We move from strategic imagination to operational clearance. The case is a medical health company. There are two gates: Baggage Check, which is KISS mapping, and Flight Plan, which is OKR construction.')),
    S('Read the Success in Practice statement of the case aloud.',
      `"${D.SA_SIP}"`),
    S('Gate 1 — Baggage Check.',
      'Take KEEP, IMPROVE, START and STOP in turn. For each filter, read the question on the card and the options under it:',
      ...D.SA_CARDS.map(c => `- ${c[1]}: ${c[2]}`),
      'Game rule: let participants choose first. Ask them to post their choice in the chat. Then choose that option on the screen: the answer is revealed only after selection.',
      'On a green light, read the reason aloud.',
      'On a red alert, ask: "Why does this option fail the SiP?"',
      'Collect at least two items for each filter, then move to the Flight Plan.',
      EX(`Under KEEP, one option reads: “${opt('keep', 7)[0]}.” ${opt('keep', 7)[2]}`,
        `Under START, one option reads: “${opt('start', 6)[0]}.” ${opt('start', 6)[2]}`,
        'Each red alert names the reason the option fails the SiP. Ask the room for the reason before you read it.')),
    S('Gate 2 — Flight Plan.',
      say('The KISS choices have now become your OKR themes.'),
      'Ask the group to pick one theme and choose it on the screen. A draft Objective, two Key Results and the contributing roles appear.',
      'Read the draft aloud and test it with the room:',
      ask('Is the Objective enterprise-level? Does each Key Result show a metric, a movement from X to Y and a deadline?'),
      'Edit the draft with the group’s corrections, then add the flight plan.'),
    S('Finish the learning round.',
      'Finish the learning round and read the summary on the screen: the KISS themes captured, and the OKR built from one theme.'),
    S('Land the learning point.',
      say('KISS is the evidence base for deciding what the Objective should be and what Key Results will prove progress.')),
    S('Hand the game to the participants.',
      say('After the teaching, each of you plays one learning round alone, in 5.1 of your own page. Clear both gates: at least two items for each KISS filter, then at least one OKR flight plan with one Objective, two Key Results and the contributing roles. This is individual work. Your learning round is saved on your page and reaches me when you submit the unit.'))],
    portal('Each participant plays one Strategy Airport learning round alone in 5.1 of the participant file and clears both gates.')),
    block('AFTER THE SESSION:', 'Each participant’s KISS choices and flight plans reach you with the submission, under the heading Strategy Airport.'));

  n.summary = N(page('UNIT SUMMARY (UNIT 3 SYNTHESIS)', [
    S('Return to the opening question, on the slide.',
      'Go back to the question you asked at the start of Awareness:',
      `"${OPENING_Q}"`,
      'Recall the answers participants posted in the chat in 1.1. Ask two or three participants:',
      ask('With the full path in front of you, where do you expect your own organisation to find its largest gap?'),
      'When the groups have confirmed their Enterprise OKRs on the portal, put the closing question of the facilitator file to them:',
      ask('Looking at the OKRs we have just built — have we answered that question? Where are the remaining gaps?')),
    S('Read the five summary blocks aloud.',
      'The summary is intentionally concise: it crystallises the arc of the unit without adding new content.',
      'The blocks describe the whole unit, including the work participants complete on the portal.',
      ...D.SUMMARY.flatMap(s => ['', H(`${s.arc} · ${s.title}:`), ...s.body.replace(/([.?!])\s+(?=[A-Z])/g, '$1\n').split('\n')])),
    S('Name the tangible outputs.',
      'Tell participants what the unit produces once the portal work is complete:',
      '- The six-step exercise from each participant (2.2)',
      '- The matching exercise from each participant (3.1)',
      '- A confirmed KISS map from each group (4.1)',
      '- Confirmed Enterprise Priorities and Enterprise OKRs from each group: maximum 4 Objectives, maximum 3 Key Results each (4.2)',
      '- A completed Strategy Airport learning round from each participant (5.1)'),
    S('Ask for the closing commitment, on the slide.',
      'Ask each participant to complete this sentence privately:',
      '"The one thing I am committing to before our next session to make these OKRs real is…"',
      'Post in the chat. These are the accountability anchors between now and Unit 4.'),
    S('Give the transition to Unit 4.',
      say('We have built our Strategy Intent Statement, described our future state through SiP, and now defined how we will measure our progress through OKRs. Unit 4 tests the integrity of that direction through ABCV: the conditions that must hold true for the journey toward the organisation we have described.')),
    S('Hand over to the portal.',
      say('The teaching ends here. You now go to the portal and complete your own page, in the session or after it.'),
      '- Section 1: the 1.4 reflection.',
      '- Section 2: the six-step exercise, as individual work, and the 2.2 reflection.',
      '- Section 3: the matching exercise and the 3.1 reflection, as individual work.',
      '- Section 4, with the group: the KISS map in 4.1, then the six steps in 4.2. The group agrees each entry, one member acts as scribe, and every member types the agreed entries into their own page.',
      '- Section 5: one Strategy Airport learning round, as individual work.',
      'Participants then submit Unit 3 to the facilitator from their page.',
      'Where the portal work is done in the session, bring the room back together once it is complete, for each group to read one Enterprise OKR to the room (4.2b).')]),
    block('AFTER THE SESSION:',
      '- Review each participant’s submission from the facilitator dashboard. The work appears under its own headings: Six-Step Exercise, Hot Zone Matching, KISS Mapping, KISS Map — Confirmed, Enterprise Priorities & OKRs and Strategy Airport.',
      '- Note the groups whose members hold different versions of an output. Ask them to agree one version and update their pages before the team opens its Capstone Blueprint.'));

  return { n, used, D, KLO, SLOS, REFL, OPENING_Q, TEST4 };
};
