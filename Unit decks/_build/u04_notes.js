// Unit 4 · presenter notes for the rebuilt deck (October 2026), on the model of Carol's Unit 2 and Unit 3 decks
// ("Claude outputs\Unit 2 deck - notes as Carol approved them (format model).txt" and her final Unit 3 deck).
//
// STRUCTURE OF EVERY NOTES PAGE
//   1. HEADING in capitals.
//   2. HOW TO TEACH IT (HOW TO USE THIS SLIDE on reflection slides; HOW THIS SECTION RUNS, SECTION LEARNING OUTCOMES and
//      HOW TO OPEN THE SECTION on section slides): numbered steps in class order. Under each step title: what the facilitator
//      says ("Say:"), asks ("Ask:"), does, or listens for ("Listen for:").
//   3. Nothing sits loose after the steps. EXAMPLE blocks and each journal insight ("Deepen, say:" then "(Insight: … Source: …)")
//      sit inside the step where they are used.
//   4. Last blocks only: ON THE PORTAL, AFTER THE TEACHING and AFTER THE SESSION.
// A line that starts with § is a heading or a step title: format_notes_u03.py removes the mark and makes the line bold.
//
// ALIGNMENT: the notes carry only what the Unit 4 facilitator and participant files carry (rebuilt 7 October 2026 on Carol's brief).
// The data comes from u04_data.json, written by rebuild_u04/export_deck_data.py from u4_content.py, the content both pages are built from.
// TEACHING FLOW: the facilitator teaches the whole unit from the deck first, including the Industry Illusion game played with the
// room; participants go to the portal afterwards.
// Carol's rules: no timings, no pre-work, no contrast constructions, never "lens", British spelling, "post in the chat".
const fs = require('fs');
const path = require('path');

module.exports = function (INS) {
  const used = new Set();
  const N = (...parts) => parts.flat(Infinity).filter(p => p !== null && p !== undefined && p !== false && String(p).trim() !== '').join('\n\n').replace(/\n{3,}/g, '\n\n');
  const H = t => '§' + t;
  const noq = s => { if (/"/.test(s)) throw new Error('straight quote inside a spoken line: ' + s.slice(0, 80)); return s; };
  const brk = s => s.length < 150 ? s : s.replace(/([.?!])\s+(?=[A-Z“‘])/g, '$1\n');
  const say = (s, cue = 'Say') => `${cue}: "${brk(noq(s))}"`;
  const ask = s => `Ask: "${noq(s)}"`;
  const IN = (id, cue = 'Deepen, say') => {
    const x = INS[id]; if (!x) throw new Error('unknown insight ' + id);
    if (used.has(id)) throw new Error('insight used twice: ' + id); used.add(id);
    return ['', say(x.text, cue), `(Insight: ${x.title.replace(/\.$/, '')}. Source: ${x.source})`];
  };
  const S = (title, ...lines) => [title, ...lines.flat(Infinity).filter(x => x !== null && x !== undefined && x !== false)];
  const steps = items => items.filter(Boolean).map((it, k) => H(`${k + 1}. ${it[0]}`) + (it.length > 1 ? '\n' + it.slice(1).join('\n') : ''));
  const page = (heading, items, ...tail) => N(H(heading), H('HOW TO TEACH IT:'), steps(items), tail);
  const block = (title, ...lines) => H(title) + '\n' + lines.flat(Infinity).join('\n');
  const portal = (...lines) => block('ON THE PORTAL, AFTER THE TEACHING:', ...lines);
  const after = (...lines) => block('AFTER THE SESSION:', ...lines);
  const EX = (...lines) => ['', H('EXAMPLE'), ...lines, ''];
  const SLO = slo => block('SECTION LEARNING OUTCOMES:', slo.map((o, k) => `${k + 1}. ${o}`));
  const divider = (label, runs, slo, items, ...tail) => N(H(label),
    block('HOW THIS SECTION RUNS:', runs), SLO(slo),
    H('HOW TO OPEN THE SECTION:'), steps(items), tail);
  const reflection = (num, items, where) => N(H(`SECTION ${num} REFLECTIONS`), H('HOW TO USE THIS SLIDE:'), steps(items), portal(where));
  // Carol's two lines from her own decks, word for word, as the step that says what the reflection is for.
  const reflFor = () => S('Say what the reflection is for.',
    'Point learners to the portal section that they will be required to complete with as much depth as possible.',
    'The reflections build the learning portfolio they receive at the end of the programme.', '',
    say('You write this reflection on the portal after the teaching, with as much depth as you can.'));

  const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'u04_data.json'), 'utf8'));
  const { DEPTHS, BOUNDARY_KINDS: BK, VP_TESTS: VP, MBT2, TRAPS, GAME: G, MINES, ILLUS, STEPS, WORKED_KR: W, EXAMPLES } = D;
  const CP = Object.fromEntries(D.CHECKPOINTS.map(c => [c.k, c]));
  const KR = '“' + W.kr + '”';
  const q = k => D.STEP_Q[k].replace('{kr}', KR);
  const mq = k => D.STEP_MBT[k].replace('{kr}', KR);
  const ill = k => ILLUS.find(x => x.k === k);

  const KLO = [
    'Critically evaluate the coherence and credibility of the organisation’s strategic direction.',
    'Appraise the assumptions, dependencies and uncertainties that influence the viability of strategic choices.',
    'Judge the extent to which strategic priorities are differentiated, internally consistent and responsive to the operating environment.',
    'Demonstrate executive confidence and collective accountability for the integrity of the chosen direction.'];
  const SLOS = { 1: D.SLO['1'], 2: D.SLO['2'],
    3: ['Identify the dimensions of strategic integrity most often overlooked in their own executive function.', 'Appraise how functional blind spots compound into enterprise-wide strategic risk.'],
    4: D.SLO['4'], 5: D.SLO['5'] };
  const REFL = {
    ov: 'Take one Key Result your group confirmed in Unit 3. What is it assuming about the world that has not yet been verified?',
    together: 'Which of the four ABCV checkpoints is your organisation least likely to examine rigorously before launching a new strategic initiative? What does that pattern cost you?',
    '3.1': 'Having explored your role’s typical blind spot: what is one MBT condition in that checkpoint that your organisation is currently assuming without confirmation? What would it take to verify it?',
    close: 'What is one MBT condition your organisation is currently avoiding naming? Why? What will you do about it before your next strategic review?' };
  const OPENING = 'Your group has defined its OKRs. Now the question is whether they are strategically sound.';
  const CLOSING_Q = 'What is the one MBT condition your team is most likely to avoid naming? Why? And what will you do about it before the next strategic review?';
  // Section 3 is as it stood on the pages: the nine roles and the checkpoint each most often overlooks; the CEO card in full.
  const ROLES = [['CEO', 'Boundaries'], ['CFO', 'Arena'], ['COO', 'Competition'], ['CHRO', 'Competition'], ['CTO', 'Arena'], ['CMO', 'Boundaries'], ['CCO', 'Value Proposition'], ['CPO', 'Arena'], ['CSO', 'Boundaries']];
  const CEO = {
    over: 'The CEO holds the vision and drives narrative — but operational friction is rarely in the chief executive\'s focus until execution stalls significantly.',
    symptom: 'Why are we not seeing the results when our strategy is clear?',
    reveal: 'The Boundaries checkpoint forces explicit naming of the regulatory, structural, and behavioural friction standing between the vision and its delivery.',
    line: 'Vision without friction-mapping is only a speech.',
    right: 'What specific conditions must remain true for execution to sustain the pace we\'ve planned for?' };
  const n = {};
  const kr1 = EXAMPLES[0], kr2 = EXAMPLES[1];
  const exKR = k => EX('Two Key Results of the client services company participants met in Unit 3, part 2.2:',
    `Key Result: ${kr1.t}`, `${CP[k].name} · Must-Be-True: ${kr1[k]}`, '',
    `Key Result: ${kr2.t}`, `${CP[k].name} · Must-Be-True: ${kr2[k]}`);
  const ownKR = k => S('Apply it to one of the room’s own Key Results.',
    'Take one of the Key Results a group confirmed in Unit 3.',
    ask(k === 'a' ? 'Which part of the Customer End Game does this Key Result serve: the functional outcome, the experience of achieving it, or what achieving it enables?' : CP[k].anchor),
    'Then ' + ask(CP[k].mbt).replace(/^Ask/, 'ask'),
    'Hold out for a condition that is either true or false.');

  // ════════════════════════════════════════════════════════════════ FRONT
  n.cover = N(H('UNIT 4 · DIRECTION INTEGRITY (ABCV-MBT)') + '\nModule 2 · Direction · Unit 4',
    block('UNIT INTENT',
      'Unit overview (facilitator file): Ensuring OKRs are anchored in customer reality, resilient to operational friction, and coherent with your organisation’s unique value before execution begins.', '',
      'Unit 4 tests whether the chosen direction is strategically sound. The four ABCV checkpoints (Arena, Boundaries, Competition and Value Proposition) and their Must-Be-True conditions turn assumptions into named, verifiable conditions.', '',
      'The Key Results tested are the ones the group confirmed in Unit 3: no new objective or metric enters the unit.'),
    block('WHAT THE UNIT PRODUCES:',
      '1. Each group produces its ABCV–MBT record: every Key Result it confirmed in Unit 3, taken through four steps, with one Must-Be-True condition named at each step. This is Capstone work.',
      '2. Each participant produces two pieces of portfolio work: the Industry Illusion game of Section 2 and the Cause of Death game of Section 5.',
      '3. Each participant writes four reflections, the last of them a closing commitment.'),
    block('HOW THE UNIT RUNS:',
      '1. You teach the whole unit from this deck first, from Section 1 to the Unit Summary. The deck is the teaching material. The teaching includes the Industry Illusion game, played with the room in groups.',
      '2. Participants then complete their own page on the portal, in the session or after it: the reflections, their own Industry Illusion game, the group work of Section 4 and the Cause of Death game.',
      '3. Section 4 on the portal is group work for the Capstone. The group agrees each entry and one member acts as scribe.',
      'Every member then types the agreed entries into their own page.',
      '4. The Industry Illusion game in Section 2 and the Cause of Death game in Section 5 are portfolio work, completed by each participant alone.'),
    'Each slide’s notes end with a block headed "On the portal, after the teaching" wherever participants have something to complete for that part.',
    'Your preparation as facilitator:\n- Read the Facilitator Guide tab and every section of the facilitator file.\n- Have the facilitator file ready in your browser at Section 2, part 2.2, so that the Industry Illusion game can be shared when you reach it.\n- Each group needs its confirmed Enterprise OKRs from Unit 3 in front of it: every exercise in this unit works on those Key Results.',
    'Where the outputs go next:\n- The confirmed Must-Be-True conditions feed boxes 4A to 4D of the team’s Capstone Blueprint.');

  n.klo = N(H('KEY LEARNING OUTCOMES'),
    block('HOW TO USE THIS SLIDE:',
      'Read the four outcomes aloud and say where the unit delivers each one.',
      '- Outcome 1 is built in Section 1 (the four ABCV checkpoints) and produced in 4.2, where each group tests its own Key Results.',
      '- Outcome 2 is built at each checkpoint, where a Must-Be-True condition is named, and shown in 4.1 (the worked example: one Key Result, four steps, four conditions).',
      '- Outcome 3 is built in 1.3 and 1.4 (Competition and Value Proposition) and in Section 2 (the Industry Illusion).',
      '- Outcome 4 is built in Section 3 (the blind spot of each executive role) and produced in 4.2, where the group confirms its conditions together.'),
    'Each section slide carries that section’s two learning outcomes.',
    block('QUESTION TO ASK:', '"What is your current strategy assuming about customers that nobody has verified?"'),
    'Take two or three answers. They tell you where the room expects the most from the unit.');

  n.journey = N(H('FACILITATOR GUIDE · SESSION OVERVIEW'),
    block('HOW TO USE THIS SLIDE:',
      '1. Walk the five sections in one sentence each, using the list below.',
      '2. Say plainly that Sections 1 to 3 prepare the thinking, Section 4 is where each group tests its own Key Results for the Capstone, and Section 5 is a diagnosis game each participant plays alone.',
      '3. Tell participants how the unit runs: you teach all five sections from the deck first, and they then complete the unit on the portal, in the session or after it.'),
    block('THE FIVE SECTIONS:',
      '- Section 1 · Awareness — What: the flow from Unit 3 to Unit 4, then the four ABCV checkpoints one at a time (Arena, Boundaries, Competition, Value Proposition), each with its Must-Be-True condition, then the four brought together.', '',
      '- Section 2 · Intelligence — Why: the Industry Illusion and its three traps (Familiarity, Exclusion, Complacency), then the Industry Illusion game on the case of a university.', '',
      '- Section 3 · Extrapolating — Where: the ABCV checkpoint each executive role most often overlooks.', '',
      '- Section 4 · Integration — Collective: one worked example, then each group takes its Unit 3 Key Results through the same four steps.', '',
      '- Section 5 · Application — In Practice: Cause of Death, four failed strategies tested against the Industry Illusion.'),
    block('KEY FACILITATION QUESTIONS:',
      '- "Who else solves your customer’s problem, including those outside your industry?"',
      '- "Which ABCV checkpoint is your executive function least likely to examine? What risk does that create for the enterprise?"',
      '- "What is the one Must-Be-True condition your team is most likely to avoid naming, and who will verify it before the next strategic review?"'),
    block('TONE AND WATCH POINTS:',
      '- Watch for Must-Be-True conditions written as risks or concerns. Each must be a condition that is either true or false.',
      '- Watch for competition defined as industry rivals only. Push for every alternative the customer can choose, including doing nothing.',
      '- Insist on specific conditions.'));

  // ════════════════════════════════════════════════════════════════ SECTION 1
  n.s1 = divider('SECTION 1 · AWARENESS — WHAT', [
    '1. The overview: the flow from Unit 3 to Unit 4 and the logic of the four steps.',
    '2. 1.1 to 1.4: the four checkpoints, one at a time. Each has two slides: the checkpoint itself, then its Must-Be-True condition.',
    '3. Bringing ABCV Together: the integrated view.',
    '4. The Section 1 Reflections slide: the two reflections participants write on the portal after the teaching.'], SLOS[1], [
    S('Open with the question that creates the need.',
      ask('How many of you have experienced a well-crafted strategy that fell apart once execution started because of assumptions we hadn’t named until they broke?'),
      'Pause. Use the silence.'),
    S('Introduce ABCV–MBT.',
      say('ABCV–MBT is the tool that names those invisible assumptions before they become expensive failures.'),
      'Section intent: leaders must feel the danger of unnamed assumptions before they can value the discipline of naming them.'),
    S('Say what each group brings into the unit.',
      say('You arrive with the Enterprise OKRs your group confirmed in Unit 3. Every exercise in this unit works on those Key Results.'))]);

  n.ov1 = page('OVERVIEW — FROM UNIT 3 TO UNIT 4 (STRATEGIC CONTEXT)', [
    S('Read the statement on the slide aloud.', `"${OPENING}"`),
    S('Say where the room stands.',
      say('In Unit 3 your group translated its Success in Practice into Enterprise OKRs. They are measurable, they are ambitious and they have deadlines. The next step is to move past well-written OKRs and ask whether they are strategically sound.')),
    S('Name the danger.',
      say('Most strategies fail because of unnamed conditions. Goals are built on a bed of invisible assumptions that are discovered only once execution begins and things start to break. By then, the cost of correction is massive.'),
      ask('Think of a goal that failed in your organisation. Was it a lack of effort, or was there an assumption that turned out to be wrong, one you didn’t name until it broke?'),
      'Take two or three answers.',
      IN('unnamed')),
    S('Bridge to the logic.',
      say('ABCV is used to interrogate whether an agreed strategic direction is sound enough to carry into execution. The next slide shows how it works.'))]);

  n.ov2 = page('OVERVIEW — THE LOGIC (4 STEPS · 1 CONDITION AT EACH)', [
    S('Walk the four steps on the slide.',
      say('ABCV forces leaders to examine the strategic logic through four checkpoints.'),
      ...D.OVERVIEW_Q.map((o, k) => `- ${STEPS[k][0]} · ${STEPS[k][1]}. ${o[2]}`)),
    S('Introduce Must-Be-True, from the foot of the slide.',
      say('For each checkpoint, MBT, Must-Be-True, makes the underlying assumption explicit. It names the load-bearing walls of the goals: the specific condition that must remain true for a Key Result to survive. If one of these conditions shifts or fails, the Key Result becomes fragile by design.')),
    S('Show the flow from Unit 3 to Unit 4.',
      'Say the three stages in order:',
      '- From Unit 3: the group’s Enterprise OKRs, the Objectives and Key Results it confirmed.',
      '- Four checkpoints: Arena, Boundaries, Competition, Value Proposition.',
      '- Must-Be-True conditions: one at each checkpoint, for each Key Result.',
      say('No new objective and no new measure enters this unit. We test the Key Results you already hold.')),
    S('Say what the test secures.',
      say('The test secures strategic priorities that are anchored in customer reality, designed to withstand operational constraints, positioned accurately against the competitive landscape, and coherent with the organisation’s core value.'),
      say('By naming these conditions early, you create an early-warning system that detects risks before a well-written ambition collapses under the weight of reality.')),
    S('Bridge to 1.1.', say('We take the four checkpoints one at a time. We start with Arena.'))],
    portal('Participants write the first reflection in Section 1 of the participant file, under the overview. It is shown on the Section 1 Reflections slide.'));

  // 1.1 Arena
  n.p11a = page('1.1 — ARENA (CUSTOMER END GAME)', [
    S('Read the question of the checkpoint.', `"${D.HEAD_Q.a}"`),
    S('Give the strategic logic.',
      say(CP.a.logic),
      say('Arena defines the space in which value is being sought and contested.'),
      say('Organisations naturally describe themselves through what they produce or the industry in which they operate: we are a university, we are a bank, we are a mine, we provide insurance. Those descriptions tell us something important about the organisation. They do not necessarily tell us what the customer is ultimately trying to accomplish.')),
    S('Use the smartphone.',
      say('Think about the smartphone. Inside the telecommunications industry, Nokia and Motorola were making phones. The smartphone became a camera, a map, a bank and a personal assistant. It moved into multiple Arenas simultaneously.'),
      ask('Who in your industry is playing a different game that you’re only just starting to notice?'),
      IN('arena')),
    S('Teach the three depths on the slide, one at a time.',
      say('Arena deliberately returns attention to the Customer End Game. To understand that end game properly, we interrogate it at three depths.'),
      ...DEPTHS.flatMap(d => ['', `${d.name} — ${d.q}`, `Ask: "${d.ask}"`, `Example: ${d.egs[0]}`])),
    S('Read the three together.',
      say('These are three depths of one interrogation. Together, they help define the Customer End Game.'),
      EX('Higher education.',
        'Functional: Build relevant and credible capability.',
        'Experiential: Do so through learning that is flexible, accessible and compatible with work.',
        'Consequential: Translate that capability into career progression and economic opportunity.',
        'The Arena can therefore be expressed as: Enabling working professionals to build credible capability, in ways compatible with their working lives, that advances career and economic opportunity.',
        'The organisation now has a much richer strategic space to interrogate than “We provide postgraduate education.”')),
    S('Ask the room to apply the three depths.',
      'Ask leaders to apply the three depths to their primary customer. Online: ask them to post one line for each depth in the chat.',
      'Listen for: the experiential and consequential depths. Most leaders find these are rarely discussed in their strategy sessions. That is the blind spot.'),
    S('Land the line at the foot of the slide.', `Read it in full: "${D.ARENA_QUOTE}"`)]);

  const mbtPage = (k, num, extraSteps = []) => page(`${num} — ${CP[k].name.toUpperCase()}: WHAT MUST BE TRUE`, [
    S('Ask the Must-Be-True question on the slide.',
      MBT2[k][0],
      `"${MBT2[k][1]}"`),
    S('Give the teaching example.',
      'Example, from higher education: ' + MBT2[k][2],
      say(MBT2[k][3])),
    S('Show the checkpoint on a Key Result.',
      'The slide shows one Key Result of the client services company from Unit 3, part 2.2, and its condition. The same two Key Results run through all four checkpoints.',
      exKR(k)),
    ownKR(k),
    ...extraSteps]);

  n.p11b = mbtPage('a', '1.1', [
    S('Say which depth the condition rests on.',
      'Each Arena condition rests on one of the three depths. Example (experiential): “Clients must continue to value a response inside four hours.”'),
    S('Bridge to 1.2.', say('Arena tells us what the customer is trying to achieve. Boundaries asks what could stop us delivering it.'))]);

  // 1.2 Boundaries
  n.p12a = page('1.2 — BOUNDARIES (FRICTION ARCHITECTURE)', [
    S('Read the question of the checkpoint.', `"${D.HEAD_Q.b}"`),
    S('Give the strategic logic.',
      say(CP.b.logic),
      say('Every strategic choice operates within conditions that enable, restrict or shape what can actually be delivered. These are Boundaries.'),
      'Key message: defining the right Arena is only the first test. The organisation must also be able to deliver within it.'),
    S('Walk the six kinds of boundary on the slide.',
      ...BK.map(b => `- ${b[0]}: ${b[1]}`),
      say('The purpose is to find the boundaries material enough to affect the strategic outcome. A long risk register is of no use here.')),
    S('Give the example.',
      EX('Higher education. The university’s Arena requires flexible capability development for working professionals. But:',
        '- Programme approvals take 12 months.',
        '- Faculty contracts are designed around semesters.',
        '- Systems require fixed annual enrolment periods.',
        '- Accreditation limits how credentials can be structured.',
        'These conditions reveal the friction architecture surrounding the Arena. The Arena itself still stands.')),
    S('Ask the strategic question.',
      ask('Which conditions could materially slow, restrict or prevent us from delivering the customer end game we have defined?'),
      IN('behind')),
    S('Sort the boundaries.',
      'Distinguish between three kinds:',
      '- A boundary we must accept. For example, legislation.',
      '- A boundary we can influence. Perhaps an industry standard.',
      '- A boundary we created ourselves. Perhaps an internal process, structure or policy.',
      ask('Which of your boundaries did your own organisation create?'),
      'Stay here. The self-created boundary generates particularly useful executive discussion.')]);

  n.p12b = mbtPage('b', '1.2', [
    S('Bridge to 1.3.', say('We know what the customer is trying to achieve and what could constrain us. Competition asks who else can give the customer the same outcome.'))]);

  // 1.3 Competition
  n.p13a = page('1.3 — COMPETITION (THE TRUE LANDSCAPE)', [
    S('Read the question of the checkpoint.', `"${D.HEAD_Q.c}"`),
    S('Give the strategic logic.',
      say(CP.c.logic),
      say('Competition follows Arena deliberately. If leaders define Arena through their industry, they will probably identify competitors through their industry. If Arena is defined around the Customer End Game, the competitive field can look very different.')),
    S('Read the two questions on the slide, left then right.',
      '- Who sells something similar to us?',
      '- What alternatives does the customer have for achieving the end game?',
      'The critical distinction is between these two questions.',
      say('The competitor does not have to look like us, sell the same product, use the same business model or belong to the same industry. It only needs to offer the customer a credible alternative route to the outcome.')),
    S('Give the example.',
      EX('Higher education. If we say “We provide postgraduate qualifications”, we will probably compare ourselves with other universities.',
        'The Arena has now been defined more deeply: build credible capability, flexibly, to advance career opportunity. Who or what else can enable that? The landscape may include:',
        '- Professional bodies.', '- Corporate academies.', '- Industry certifications.', '- Specialist training providers.',
        '- Digital learning platforms.', '- Employer-led development.', '- Alternative credential providers.',
        'And potentially emerging models we have not historically classified as higher education.')),
    S('Widen the list of alternatives, using the right-hand card.',
      say('Competition can also be: do it internally, do it themselves, use technology, postpone it, choose a completely different solution, or do nothing.'),
      ask('Who else solves your customer’s problem, including those outside your industry?'),
      'Listen for: competition defined as industry rivals only. Push for every alternative route the customer has to the outcome, including doing nothing.',
      IN('competition')),
    S('Land the point.', say('The customer is choosing between routes to an outcome.'))]);

  n.p13b = mbtPage('c', '1.3', [
    S('Say why the condition matters.', say('That assumption can be monitored. If it begins to weaken, the strategy receives an early-warning signal.')),
    S('Bridge to 1.4.', say('Given those alternatives, why should the customer choose us? That is the Value Proposition.'))]);

  // 1.4 Value Proposition
  n.p14a = page('1.4 — VALUE PROPOSITION (COHERENT ADVANTAGE)', [
    S('Read the question of the checkpoint.', `"${D.HEAD_Q.v}"`),
    S('Give the strategic logic.',
      say(CP.v.logic),
      say('Arena established what the customer is ultimately trying to achieve. Boundaries established the conditions within which we must deliver it. Competition revealed the alternatives available to the customer. Value Proposition now asks: given those alternatives, why should the customer choose us?')),
    S('Clear away the positive attributes.',
      say('A Value Proposition is more than a description of what the organisation offers. High quality, customer focused, innovative, excellent service, experienced people: all of these may be positive attributes. On their own they establish no strategic value.'),
      ask('What combination of value do we create that matters to this customer, in this Arena, relative to the alternatives available?')),
    S('Teach the three tests on the slide.',
      ...VP.flatMap(v => ['', `${v[0]} — ${v[1]}`, v[2]]),
      '', 'Read the foot of the slide: RELEVANT + DISTINCTIVE + DELIVERABLE = STRATEGIC VALUE.',
      IN('value')),
    S('Give the example.',
      EX('Higher education. Suppose Apex says: “We provide high-quality executive education.” That is positive but strategically weak. Interrogate it.',
        'Relevant? Working executives value capability that translates into workplace performance.',
        'Distinctive? Apex integrates real organisational strategy challenges into assessed learning.',
        'Deliverable? Its faculty, practitioner network and learning architecture consistently support applied workplace learning.',
        'The value proposition becomes more meaningful: Applied, credible executive capability development built around real organisational challenges and designed for working professionals.',
        'Now there is something that can actually be tested against alternatives.'))]);

  n.p14b = mbtPage('v', '1.4', [
    S('Bridge to the integrated view.', say('We have four checkpoints and a condition at each. Now we bring them together.'))]);

  n.together = page('BRINGING ABCV TOGETHER (THE INTEGRATED VIEW)', [
    S('Walk down the chain on the slide once.',
      '- A — Arena: What is the customer ultimately trying to achieve? Functional, Experiential, Consequential.',
      '- B — Boundaries: What could constrain our ability to deliver that outcome?',
      '- C — Competition: Who or what else can enable the customer to achieve it?',
      '- V — Value Proposition: Why should the customer choose the value we create?',
      '- MBT — Must Be True: What conditions must hold for our strategic logic to remain valid?'),
    S('Land the line at the foot of the slide.',
      'Read it aloud: "ABCV does not ask whether an OKR is well written. It asks whether the strategic logic underneath it can survive reality."',
      IN('known')),
    S('Ask the room.',
      ask('If you had to identify the single ABCV checkpoint your organisation most consistently overlooks when setting strategy, which would it be? And what has that cost you?'),
      'Online: ask participants to post the checkpoint in the chat.',
      'Keep the answers. They surface the role-based blind spots you return to in Section 3.')],
    portal('Participants answer the same question as a reflection in Section 1 of the participant file. It is shown on the Section 1 Reflections slide.'));

  n.ref1 = reflection(1, [
    S('Show the slide and read the two prompts aloud.',
      `1 · Overview reflection: "${REFL.ov}"`, '',
      `2 · Bringing ABCV Together reflection: "${REFL.together}"`),
    reflFor(),
    S('Set the standard.',
      say('For the first reflection, name one real Key Result of your group and one thing it assumes. For the second, name the checkpoint and one real cost.'),
      'Listen for: an assumption stated as a worry. Ask: "Written as a condition, is it true or false today?"'),
    S('Bridge to Section 2.', say('We have the four checkpoints. Section 2 asks why leaders so often fail to use them.'))],
    'Participants write the two reflections in Section 1 of the participant file: under the overview, and under Bringing ABCV Together.');

  // ════════════════════════════════════════════════════════════════ SECTION 2
  n.s2 = divider('SECTION 2 · INTELLIGENCE — WHY', [
    '1. 2.1: the Industry Illusion and its three traps.',
    '2. 2.2: the Industry Illusion game, played with the room in groups, from the facilitator file.',
    '3. 2.2, after the game: the Arena question, back on the deck.'], SLOS[2], [
    S('Say what the section does.',
      say('In this section you discover, through your own decisions, how an industry frame shapes what leaders notice, dismiss and trust.'),
      'Section intent: the game supplies the evidence. Arena supplies the test.'),
    S('Read the line under the section title.', `"${D.II_BOUNDARY}"`)]);

  n.p21 = page('2.1 — THE INDUSTRY ILLUSION (3 TRAPS)', [
    S('Start with the value of industry knowledge.',
      say('Industry knowledge is essential to strategy. Over time, leaders build a deep understanding of how their industry works: its customers, competitors, economics, regulations, technologies and established ways of creating value. That knowledge also creates a frame through which leaders interpret their environment.'),
      say('The Industry Illusion occurs when that frame becomes so familiar that leaders begin to treat it as the boundary of what is strategically relevant.')),
    ...TRAPS.map(t => S(`${t.name} — ${t.line}`,
      say(t.body.join(' ')),
      `Strategic risk: ${t.risk}`)),
    S('Show how the illusion forms.',
      'Read the three cards from left to right, then the foot of the slide:',
      '- Familiarity: We know this industry.',
      '- Exclusion: We discount what doesn’t fit it.',
      '- Complacency: We become confident in the world we can see.',
      `- Industry Illusion: ${D.II_BOUNDARY}`,
      'Each trap reinforces the next. Keep the examples general here: the game supplies the case.'),
    S('Bridge to the game.', say('You are about to make three decisions as an executive team. Make each one as you would at work.'))]);

  n.p22 = page('2.2 — THE INDUSTRY ILLUSION GAME: THE FUTURE OF A UNIVERSITY (3 ROUNDS)', [
    S('Share the game.',
      'Stop sharing the deck and share the browser window that holds the facilitator file, at Section 2, part 2.2.',
      'Have that page ready before the lesson begins.',
      'The page holds six steps in order: Case Brief, Round 1, Round 2, Round 3, The Reveal, Apply Arena.',
      'Play the game with the room in groups. Each group makes its decision and defends it.',
      'Important: do not tell participants which trap each round is testing. Do not correct their answers during the game. Capture their decisions. Reveal the traps only at the end.'),
    S('Give the case brief.',
      say('You are the executive team of Apex University, an established private university.'),
      'Read the brief on the screen: 18,000 students; strong undergraduate and postgraduate programmes; recognised accreditation; a respected business school; growing online delivery; strong relationships with employers; good graduate employment outcomes; stable enrolment.',
      say(G.brief_board + ' ' + G.brief_task)),
    S('Round 1 — Where would you look?',
      say(G.r1_prompt),
      'Show the eight intelligence sources, A to H, on the screen.',
      say('Select four that you would prioritise.'),
      'Each group posts its four letters in the chat. Record the choices.',
      'What this round tests, for you only: Familiarity. Do participants gravitate toward A to D because these are recognisably higher-education indicators? Do not reveal this.'),
    S('Round 2 — What deserves attention?',
      say('Your strategy team has brought six developments to the executive committee. You only have capacity to investigate three in depth.'),
      'Show the six signals on the screen.',
      ask('Which three warrant immediate strategic investigation?'),
      'Then ' + ask('Which three would you deprioritise?').replace(/^Ask/, 'ask'),
      'Require each group to make the decision. Capture what it excluded and, importantly, why.',
      'What this round tests, for you only: Exclusion. Are signals 3, 4 and 6 discounted because they do not initially look like developments inside higher education? Do not reveal the trap.'),
    S('Round 3 — Should we be worried?',
      'Show the Apex University performance report on the screen: enrolment +5%, revenue +7%, graduate employment 86%, accreditation strong, student satisfaction 82%, market position top 3 private university, online enrolment +12%.',
      say(G.r3_prompt),
      'Give the three choices: A, no major change; B, adjust; C, re-examine. Each group must select one and defend it.',
      'What this round tests, for you only: Complacency. Does strong current performance reassure participants that the university understands its future? Choice A is a reasonable answer on the page: the numbers genuinely look good.'),
    S('The Reveal.',
      'Now return to their decisions, round by round.',
      'Round 1, where did you look? Reveal Familiarity: We know this industry.',
      ask('How much of your attention went toward the world you already recognised as higher education?'),
      'Round 2, what did you exclude? Reveal Exclusion: We discount what doesn’t fit it.',
      ask('Which signals did you deprioritise because they appeared to sit outside the conventional higher-education environment?'),
      'Round 3, what reassured you? Reveal Complacency: We become confident in the world we can see.',
      ask('Did strong current performance influence how urgently you believed the university needed to question its future?'),
      'Then give the crucial insight.',
      say(G.insight)),
    S('Return to the deck.',
      'Stop sharing the facilitator file and return to the deck. The next slide carries the Arena question.')],
    after('Each participant’s own game reaches you with the submission, under the heading Industry Illusion Game.'));

  n.p22b = page('2.2 — AFTER THE REVEAL: APPLY ARENA (THE LEARNING MOMENT)', [
    S('Ask the question on the slide.',
      'Only after the reveal, bring the room back to ABCV.',
      `Ask: "${G.arena_q}"`,
      'Do not give the answer.'),
    S('Make the groups work through the three depths of 1.1.',
      ...DEPTHS.map(d => `- ${d.name}: ${d.q}`),
      'Each group posts one line for each depth in the chat.'),
    S('Give the final challenge, from the foot of the slide.',
      say(G.final),
      'Take answers from two or three groups.'),
    S('Land the learning moment.',
      say('The game has not told you that you suffer from the Industry Illusion. Your own choices provide the evidence. Arena is the mechanism for testing and expanding your field of strategic attention.')),
    S('Hand the game to the participants.',
      say('After the teaching, each of you plays the game alone, in 2.2 of your own page. You play Round 1, Round 2 and Round 3 in order, and each decision is locked. The Reveal then shows your own decisions beside each trap, and you answer the Arena questions and the final challenge. This is portfolio work. Your game is saved on your page and reaches me when you submit the unit.')),
    S('Bridge to Section 3.', say('The illusion works on a whole leadership team. Section 3 asks where it works on each role.'))],
    portal('Each participant completes the Industry Illusion game alone in 2.2 of the participant file: the case brief, three locked rounds, The Reveal, the Arena questions and the final challenge.'),
    after('Each participant’s decisions and Arena answers reach you with the submission, under the heading Industry Illusion Game.'));

  // ════════════════════════════════════════════════════════════════ SECTION 3
  n.s3 = divider('SECTION 3 · EXTRAPOLATING — WHERE', [
    '1. 3.1a: the nine executive roles and the checkpoint each most often overlooks.',
    '2. 3.1b: one role card in full, the CEO.',
    '3. The Section 3 Reflections slide: the reflection participants write on the portal after the teaching.'], SLOS[3], [
    S('Say what the section does.',
      say('Every executive role is trained to protect a different part of the enterprise system. These specialisations create selective attention, and predictable strategic blind spots across the leadership mandate.'),
      'Section intent: make the ABCV framework personal to each leader’s role. The aim is illumination. Leaders should finish knowing which ABCV checkpoint is most likely their organisational blind spot and why it creates specific downstream consequences.'),
    S('Return to the answers from Section 1.',
      'Recall the checkpoints the room named as most consistently overlooked at the end of Section 1. Section 3 shows where those answers come from.')]);

  n.p31a = page('3.1 — THE EXECUTIVE HOT ZONE: ROLE-BASED BLIND SPOTS (9 ROLES)', [
    S('Show the grid.',
      say('For each role the slide shows the ABCV checkpoint that typically gets overlooked.'),
      ...ROLES.map(r => `- ${r[0]}: ${r[1]}`)),
    S('Ask each leader to find their own role first.',
      ask('Does the checkpoint beside your role match what your function examines least?'),
      'Online: ask participants to post their role and one word, yes or no, in the chat.'),
    S('Read the grid as a team.',
      ask('Look at the gaps across all roles. Which checkpoint appears most frequently as an overlooked dimension?'),
      'That answer is the team’s most critical strategic vulnerability.'),
    S('Bridge to the role card.', say('Each role has a full card. We read one together: the CEO.'))]);

  n.p31b = page('3.1 — A HOT ZONE CARD: THE CEO', [
    S('Read the card from the top left.',
      'What gets overlooked: Boundaries.',
      say(CEO.over.replace(' — but ', ', and ')),
      `Symptom: “${CEO.symptom}”`),
    S('Read what the checkpoint reveals.',
      say(CEO.reveal + ' ' + CEO.line),
      `Right question: “${CEO.right}”`),
    S('Teach the key insight.',
      say('The symptom is the question leaders only ask when the underlying ABCV condition has already failed. These are late signals. ABCV–MBT creates early signals.')),
    S('Ask the room.',
      ask('Which of these symptoms have you heard in your leadership conversations in the last quarter? What does that tell you about where your blind spot sits?'),
      'Take two or three answers.'),
    S('Say where the other eight cards are.',
      say('Each of the nine roles has its own card: what gets overlooked, the symptom, what the checkpoint reveals and the right question. You read your own card on the portal after the teaching.'))],
    portal('Participants read the nine role cards in 3.1 of the participant file and write the Section 3 reflection.'));

  n.ref3 = reflection(3, [
    S('Show the slide and read the prompt aloud.', `3.1 Reflection: "${REFL['3.1']}"`),
    reflFor(),
    S('Set the standard.',
      say('Name the checkpoint of your role. Write one condition your organisation is assuming, in a form that is either true or false. Then say what evidence would verify it and who holds that evidence.'),
      'Listen for: a general concern where a condition is needed. Ask: "What exactly must remain true?"'),
    S('Bridge to Section 4.', say('We know the checkpoints and we know our blind spots. Section 4 applies both to your own Key Results.'))],
    'Participants write the reflection in Section 3 of the participant file: 3.1 Reflection.');

  // ════════════════════════════════════════════════════════════════ SECTION 4
  n.s4 = divider('SECTION 4 · INTEGRATION — COLLECTIVE', [
    '1. 4.1: the worked example. One Key Result of the client services company from Unit 3, taken through four steps, on six slides.',
    '2. 4.2: the briefing for the Capstone work. Each group takes its own Unit 3 Key Results through the same four steps.'], SLOS[4], [
    S('Say what the section does.',
      say('This is where the checkpoints are applied to your own direction. Your group brings in the Key Results it confirmed in Unit 3 and takes each one through four steps. At each step it names the condition that must remain true.'),
      'This is Capstone work: the confirmed outputs feed each team’s Capstone Blueprint.'),
    S('Say the order.',
      say('We first walk one worked example in full. Your exercise then follows the worked example step for step.'))]);

  n.p41 = page('4.1 — WORKED EXAMPLE: STRESS-TESTING A KEY RESULT (4 STEPS)', [
    S('Recall the company.',
      say('This example continues the client services company you met in Unit 3, part 2.2.'),
      `Its Success in Practice reads: “${D.WORKED_SIP}”`),
    S('Read the Key Result on the slide aloud.',
      `Objective: ${W.obj}`,
      `Key Result: ${W.kr}`),
    S('Say how the example runs.',
      say('The company takes this one Key Result through the four steps. Each step ends with the condition that must remain true for the Key Result to hold.'),
      'At the end of each step, read the Must-Be-True condition aloud and ask what it would look like if it failed. Each condition is either true or false.')]);

  const stepPage = (k, lines, mbt, askFail, extra = []) => page(`4.1 — WORKED EXAMPLE · STEP ${k + 1}: ${STEPS[k][1].toUpperCase()}`, [
    S('Read the question of the step from the slide.', `"${q(k)}"`),
    S('Read the company’s answers.', ...lines),
    S('Read the Must-Be-True condition.',
      `The question: "${mq(k)}"`,
      `The condition: ${mbt}`,
      ask(askFail)),
    ...extra]);
  n.p41s1 = stepPage(0, [
    `Functional · What does the customer need done that this Key Result serves? ${W.fn}`,
    `Experiential · What matters to the customer about how it is done? ${W.ex}`,
    `Consequential · What does this Key Result enable for the customer? ${W.co}`], W.a,
    'What would we see first if clients stopped ranking speed of response among their top three reasons?',
    [S('Point out the depth.', say('The condition rests on the experiential depth. The company says so in the first word.'))]);
  n.p41s2 = stepPage(1, [
    'The slide lists four boundaries. For each one, give its kind and say whether the company must accept it, can influence it, or created it itself:',
    ...W.bounds.map(b => `- ${b[0]} ${b[1]} · ${b[2]}.`)], W.b,
    'What would we see first if handovers took longer than four hours?',
    [S('Point out the pattern.', say('Three of the four boundaries were created by the company itself. Those are the ones it can remove.'))]);
  n.p41s3 = stepPage(2, [
    'The slide lists five alternatives:',
    ...W.comp.map(c => `- ${c}`)], W.c,
    'Which of the five alternatives would close the gap first?',
    [S('Point out the width of the list.', say('Two of the five alternatives sit outside the industry, and one is doing nothing.'))]);
  n.p41s4 = stepPage(3, [
    `Relevant · Does this Key Result matter to the customer? ${W.rel}`,
    `Distinctive · What does it give the customer that the alternatives do not? ${W.dis}`,
    `Deliverable · Can we consistently produce it? ${W.dlv}`], W.v,
    'What would clients notice first if speed came at the cost of the quality of the answer?');

  n.p41end = page('4.1 — WORKED EXAMPLE: FOUR STEPS, FOUR CONDITIONS', [
    S('Read the four conditions in order.',
      `- Arena: ${W.a}`, `- Boundaries: ${W.b}`, `- Competition: ${W.c}`, `- Value Proposition: ${W.v}`),
    S('Land the line at the foot of the slide.',
      say('Four steps, four conditions. If one of them shifts or fails, the Key Result becomes fragile by design.')),
    S('Test the standard.',
      ask('Could someone outside this company verify each of these four conditions?'),
      say('That is the standard for your own conditions: specific enough that someone else could attempt to verify them.'),
      IN('cost')),
    S('Bridge to 4.2.', say('Your exercise is this example repeated on your own Key Results: the same four steps, in the same order.'))]);

  n.p42a = page('4.2 — STRESS-TESTING YOUR KEY RESULTS · HOW THE GROUP WORKS', [
    S('Explain how the group works, using the four lines on the slide.',
      say('Your group agrees each entry. One member acts as scribe and types the agreed wording. Every member then types the agreed entries into their own page, in the session or after it.')),
    S('Say what the group works on.',
      say('Your group does for its own Key Results what the worked example did. Your confirmed Key Results from Unit 3 are already listed on your page. No new objective or measure is added.')),
    S('Say when the work is confirmed.',
      say('When every Key Result has been taken through the four steps, each of you confirms the record.'),
      'Read the foot of the slide aloud.')]);

  n.p42b = page('4.2 — STRESS-TESTING YOUR KEY RESULTS · THE FOUR STEPS (CAPSTONE WORK)', [
    S('Walk the four steps on the slide. Each one is taken for one Key Result at a time.',
      '- Step 1 · Define the Arena. The group says which customer need the Key Result serves, at three depths (functional, experiential, consequential). Then it names what must remain true about that need.',
      '- Step 2 · Understand the Boundaries. The group lists the boundaries material enough to slow, restrict or prevent delivery of the Key Result, with the kind of each and whether it must be accepted, can be influenced or was created by the organisation itself. Then it names what must remain true for delivery.',
      '- Step 3 · See the Competition. The group lists who or what else can give the customer what the Key Result delivers, including alternatives outside the industry and doing nothing. Then it names what must remain true about its advantage.',
      '- Step 4 · Establish the Value Proposition. The group says what about the Key Result will make customers choose the organisation, using the three tests (relevant, distinctive, deliverable). Then it names what must remain true about its value architecture.'),
    S('Say how the questions read on the page.',
      say('On your page every question names your own Key Result, word for word. You answer about that Key Result and no other.')),
    S('Set the standard for a condition.',
      say('The condition your group names must be specific enough that someone else could attempt to verify it. “The market must support us” is too vague to verify. Push for precision.'),
      'Watch for: conditions written as risks or concerns. Each must be a condition that is either true or false.',
      'Watch for: groups that struggle to name a condition. This is a signal that the Key Result itself may be insufficiently grounded. Use it as productive friction.',
      ask('If you cannot name a Must-Be-True, what does that tell you about this Key Result?'),
      IN('specific')),
    S('Close the section with the commitment question.',
      ask('Which one MBT condition, if left unverified, represents the greatest risk to our strategy’s integrity? Who is leaving this room responsible for that verification?'))],
    portal('Participants work in their groups in 4.2 of the participant file. This is Capstone work.',
      '1. The group’s confirmed Key Results from Unit 3 are listed in 4.2.',
      '2. The group takes one Key Result through the four steps and names the condition at each step.',
      '3. The group takes the next Key Result through the same four steps, until every Key Result is complete.',
      '4. A record shows the condition named at each step for every Key Result. Each participant confirms the record. Print gives a copy.'),
    after('The record reaches you with each participant’s submission, under the heading ABCV–MBT: Stress-Testing the Key Results.',
      'The confirmed conditions feed boxes 4A to 4D of the team’s Capstone Blueprint.'));

  // ════════════════════════════════════════════════════════════════ SECTION 5
  n.s5 = divider('SECTION 5 · APPLICATION — IN PRACTICE', [
    '1. Cause of Death: how the game is played.',
    '2. The four mines.',
    '3. The Section 5 Reflections slide: the closing commitment.',
    '4. The Unit Summary.'], SLOS[5], [
    S('Say what the section does.',
      say('You now apply ABCV diagnostic thinking under pressure. Each scenario is a real-world strategy failure in which an Industry Illusion kept leaders from seeing the breakdown.'),
      'Section intent: participants find the illusion first, then the ABCV checkpoint where that illusion sits.'),
    S('Say who plays.', say('Each of you plays this game alone, on the portal, after the teaching. It is portfolio work.'))]);

  n.p51a = page('CAUSE OF DEATH — MATCH THE BREAKDOWN (2 PARTS · PORTFOLIO WORK)', [
    S('Explain the two parts on the slide.',
      say('Each scenario is answered in two parts. First you find the illusion. Then you find where it sits.'),
      '- Find the illusion: the participant chooses the investigation question the scenario answers. Each question reveals one illusion.',
      '- Find where it sits: the participant chooses the ABCV checkpoint the illusion hid from leaders: Arena, Boundaries, Competition or Value Proposition.'),
    S('Read the three investigation questions.',
      ...ILLUS.map((x, k) => `- Question ${k + 1}: ${x.q}`),
      'Do not say which illusion each question reveals. The participants work that out.'),
    S('Explain the mine.',
      say('When both parts are right, the mine is defused. A wrong answer detonates it: you read the hint and try again. A mine defused at the first attempt earns 2 points, at a later attempt 1 point. The maximum is 8.'),
      say('The same illusion can sit behind more than one mine.')),
    S('Set the standard.',
      say('Say your reasoning to yourself before you answer. Guessing the right checkpoint for the wrong reason will surface.'))]);

  n.p51b = page('CAUSE OF DEATH — THE FOUR MINES', [
    S('Introduce the four scenarios, one line each.',
      '- Mine 1, The Ghost Ship: a SaaS platform with strong retention in year one and 70% churn by year three.',
      '- Mine 2, The Ferrari in the Mud: a logistics firm whose new digital operations platform is used consistently by less than 30% of staff.',
      '- Mine 3, The Invisible Disruption: a financial advisory firm that loses revenue while no rival firm takes its clients.',
      '- Mine 4, The Identity Crisis: a boutique consulting firm whose revenue rises while its distinctiveness is lost.',
      'Do not give the answers. The value is in the diagnostic reasoning.'),
    S('Hand the game to the participants.',
      say('After the teaching, each of you defuses all four mines in Section 5 of your own page. Your score and your attempts are saved on your page and reach me when you submit the unit.')),
    S('Debrief at the next session, or when all have played.',
      ask('Which mine was hardest to defuse? What does that tell you about your organisation’s own ABCV blind spot?'),
      EX('Answer key, for you only. It is in the facilitator file, Section 5.',
        ...MINES.map(m => `- ${m.name}: ${ill(m.ill).name}, sitting in ${m.cpname}. ${m.insight}`)))],
    portal('Each participant plays Cause of Death alone in Section 5 of the participant file and defuses all four mines.'),
    after('Each participant’s score and attempts reach you with the submission, under the heading Cause of Death.'));

  n.ref5 = reflection(5, [
    S('Show the slide and read the prompt aloud.', `Closing Commitment: "${REFL.close}"`),
    reflFor(),
    S('Set the standard.',
      say('Name one condition, in a form that is either true or false. Say why it is being avoided. Then name one action and the date of your next strategic review.'),
      IN('avoided'))],
    'Participants write the Closing Commitment at the end of Section 5 of the participant file.');

  n.summary = page('UNIT SUMMARY (UNIT 4 SYNTHESIS)', [
    S('Recap the unit, section by section.',
      say('This session was about ensuring strategic direction is structurally sound before the first move of execution is made. The ABCV–MBT framework served as our strategic integrity filter.'),
      '- 1 · Awareness: a well-written OKR can still rest on unnamed conditions. ABCV examines the strategic logic at four checkpoints, and a Must-Be-True condition at each makes the underlying assumption explicit.',
      '- 2 · Intelligence: industry knowledge becomes a frame, and three reinforcing traps (Familiarity, Exclusion and Complacency) turn that frame into the boundary of the world leaders examine.',
      '- 3 · Extrapolating: every executive role sees through a specialised perspective, and each has a checkpoint it most often overlooks.',
      '- 4 · Integration: each group takes the Key Results it confirmed in Unit 3 through four steps and names the condition that must remain true at each step.',
      '- 5 · Application: in Cause of Death each participant tests four failed strategies against the Industry Illusion.'),
    S('Ask the closing question on the slide.',
      `Ask: "${CLOSING_Q}"`,
      'Take an answer from each group.'),
    S('Close the unit.',
      say('The ABCV–MBT checkpoints turn your OKRs from polished aspirations into resilient execution signals, grounded in the hard realities of the enterprise system.')),
    S('Say what happens on the portal.',
      say('You now complete the unit on the portal: your reflections, your own Industry Illusion game, your group’s work in Section 4, Cause of Death and your closing commitment. When your page is complete, you submit the unit.'))],
    portal('Participants complete every part of the participant file and submit the unit to the facilitator from the end of Section 5.'),
    after('Each submission reaches you in the facilitator dashboard.',
      'The confirmed Must-Be-True conditions feed boxes 4A to 4D of the team’s Capstone Blueprint.'));

  return { n, used, D, KLO, SLOS, REFL, OPENING, CLOSING_Q, ROLES, CEO, KR, q, mq };
};
