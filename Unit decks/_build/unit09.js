// Unit 9 · Strategic Unclogging — facilitator deck with detailed presenter notes.
// Run: node unit09.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u09.json'), FH = R('unit3_m2_lens8_f.html'), PH = R('unit3_m2_lens8_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const slice = (lines, a, b) => { const i = lines.findIndex(l => l.startsWith(a)); const j = b ? lines.findIndex((l, k) => k > i && l.startsWith(b)) : -1; return lines.slice(i, j < 0 ? lines.length : j).join('\n'); };
const NOTIME = 'Time: the facilitator file gives no minute timing for this section (see the Timing watch point in the Session Overview).';

(async () => {
  const d = new Deck({ unit: 9, module: 3, moduleName: 'Influence', title: 'Strategic Unclogging' });
  const G = u.guide();
  const P51 = u.part(5, 0).content;

  await d.cover({ logo: LOGO, subtitle: 'Engineering the Flow of Execution',
    notes: N('UNIT 9 · STRATEGIC UNCLOGGING\nModule 3 · Influence · Unit 9', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): When strategy stalls, the failure usually sits in the system that carries the plan. This unit equips leaders to diagnose the blockages preventing strategic intent from flowing into real-world execution — and to intervene with precision using the 7 Strategic Unclogging Levers.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time: the facilitator file times only the Clog Clinic (45 minutes: 5 minutes silent prep, 30 minutes triads, 10 minutes Alignment Brigade Challenge). Awareness and Intelligence can move at pace; Extrapolating benefits from brief functional discussion.', G[1], G[2]) });

  // ── Section 1
  await div(d, 1, NOTIME);
  await d.prompt({ icon: 'FaFilter', label: '1.1 · What is a Strategic Clog?', text: 'Strategy sets the destination. Flow determines whether you have the power to arrive.',
    foot: 'A clog is an internal blockage that prevents strategic intent from flowing into execution.', notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · Three observable friction signals', cols: 3, items: [
    { icon: 'FaHourglassHalf', title: 'Decision Paralysis', text: 'Leaders hesitate where they should act.' },
    { icon: 'FaExchangeAlt', title: 'Kinetic Misalignment', text: 'Energy is high; progress is not.' },
    { icon: 'FaChartBar', title: 'Output–Outcome Gap', dark: true, text: 'Activity is high; advancement is not.' }],
    band: 'Which of these three signals is most visible in your organisation right now?',
    notes: u.partNotes(1, 1) });
  await d.list({ title: '1.3 · The 7-Clog Diagnostic Map', fontSize: 24, rows: [
    { icon: 'FaSitemap', label: '01 · Structural Misfit', text: '· Boundaries' },
    { icon: 'FaTools', label: '02 · Capability Gaps', text: '· Arena' },
    { icon: 'FaHourglassHalf', label: '03 · Decision Bottlenecks', text: '· Boundaries' },
    { icon: 'FaBalanceScale', label: '04 · Misaligned Metrics & Incentives', text: '· Value Proposition' },
    { icon: 'FaUsers', label: '05 · Cultural Resistance', text: '· Value Proposition' },
    { icon: 'FaServer', label: '06 · Technology / Infrastructure Lag', text: '· Competition' },
    { icon: 'FaUserSlash', gold: true, label: '07 · Leadership Avoidance', text: '· Arena + Boundaries' }],
    notes: u.partNotes(1, 2) });

  // ── Section 2
  await div(d, 2, NOTIME);
  await d.prompt({ icon: 'FaDraftingCompass', label: '2.1 · Clogs are design signals', text: 'Where is the system not yet designed to carry the strategy?',
    foot: 'Clogs emerge precisely where the strategy stretches the existing system beyond its current design capacity.', notes: u.partNotes(2, 0) });
  await d.cards({ title: '2.2 · Three disciplines of execution engineering', cols: 3, items: [
    { icon: 'FaSearch', title: 'Early Identification', text: 'Detect signals before they compound.' },
    { icon: 'FaTags', title: 'Accurate Classification', text: 'Name the clog precisely before intervening.' },
    { icon: 'FaCrosshairs', title: 'Targeted Intervention', dark: true, text: 'Pull the right lever with precision.' }],
    band: 'Identify the Clog → Select the Lever → Targeted Intervention',
    notes: u.partNotes(2, 1) });
  await d.list({ title: '2.3 · The 7 Strategic Unclogging Levers', fontSize: 24, rows: [
    { icon: 'FaRulerCombined', label: '01 · Standardise', text: 'ensure consistency' },
    { icon: 'FaForward', label: '02 · Streamline', text: 'increase speed' },
    { icon: 'FaBullseye', label: '03 · Clarify', text: 'eliminate confusion' },
    { icon: 'FaArrowCircleUp', label: '04 · Upgrade', text: 'remove bottlenecks' },
    { icon: 'FaDumbbell', label: '05 · Reinforce', text: 'strengthen behaviour' },
    { icon: 'FaSlidersH', label: '06 · Realign', text: 'focus on results' },
    { icon: 'FaHandshake', gold: true, label: '07 · Rebuild Trust', text: 'restore credibility' }],
    notes: u.partNotes(2, 2) });

  // ── Section 3
  await div(d, 3, NOTIME);
  await d.list({ title: '3.1 · The 7 COMPASS high-flammability zones', fontSize: 24, rows: [
    { icon: 'FaCompass', label: 'C', text: 'Clarity of Direction' },
    { icon: 'FaProjectDiagram', label: 'O', text: 'Organisational Alignment' },
    { icon: 'FaClipboardCheck', label: 'M', text: 'Management Discipline' },
    { icon: 'FaUserFriends', label: 'P', text: 'People & Capability' },
    { icon: 'FaCoins', label: 'A', text: 'Allocation of Resources' },
    { icon: 'FaCogs', label: 'S1', text: 'Systems & Execution' },
    { icon: 'FaSatelliteDish', gold: true, label: 'S2', text: 'Sensing & Adaptation' }],
    notes: u.partNotes(3, 0) });
  await d.list({ title: '3.2 · The 4-step Unclogging Activation', fontSize: 26, rows: [
    { icon: 'FaTags', label: '1 · Identify Clog Category', text: 'select the type of friction' },
    { icon: 'FaCompass', label: '2 · Locate in COMPASS', text: 'pinpoint where it is forming' },
    { icon: 'FaSlidersH', label: '3 · Trigger Lever', text: 'match the lever to the root cause' },
    { icon: 'FaThermometerHalf', gold: true, label: '4 · Rate Severity', text: 'Low · Medium · High' }],
    notes: u.partNotes(3, 1, { extra: 'Guidance (Section 3): Walk the four steps as a live demonstration with one stalled KPI from the group before moving to Application.' }) });

  // ── Section 4
  await div(d, 4, NOTIME);
  await d.list({ title: '4.1 · Normalising the unclog: a shared path', fontSize: 26, rows: [
    { icon: 'FaQuestionCircle', label: '1', text: 'Is there a clog?' },
    { icon: 'FaTags', label: '2', text: 'What category does it fall into?' },
    { icon: 'FaCompass', label: '3', text: 'Which part of the system is it affecting?' },
    { icon: 'FaSlidersH', gold: true, label: '4', text: 'Which lever do we pull to fix it?' }],
    notes: u.partNotes(4, 0) });
  await d.prompt({ icon: 'FaBullhorn', label: '4.2 · See something, say something', text: '“The clog I suspect is forming outside my function is [clog category] in the [COMPASS zone].”',
    foot: 'Surfacing a blockage early is an act of leadership.', notes: u.partNotes(4, 1) });
  await d.cards({ title: '4.3 · Enterprise Unclogging Agenda', cols: 3, items: [
    { icon: 'FaExclamationTriangle', title: 'KR at risk', text: 'COMPASS zone and clog category' },
    { icon: 'FaSlidersH', title: 'Recommended lever', text: 'with a named owner' },
    { icon: 'FaThermometerHalf', title: 'Severity', dark: true, text: 'and why it must be named now' }],
    band: 'Agree the top three items with named owners.',
    notes: u.partNotes(4, 2) });

  // ── Section 5
  await div(d, 5, 'Time: 45 minutes in total — 5 minutes silent prep + 30 minutes triads (10 minutes per person) + 10 minutes Alignment Brigade Challenge. Do not compress the triad rounds.');
  await d.cards({ title: 'The Clog Clinic: three parts · 45 minutes', cols: 3, items: [
    { icon: 'FaUserEdit', title: 'Part 1 · 5 min', text: 'Individual Prep' },
    { icon: 'FaUsers', title: 'Part 2 · 30 min', text: 'Diagnostic Triads: Diagnostician · Challenger · Observer' },
    { icon: 'FaGavel', title: 'Part 3 · 10 min', dark: true, text: 'Alignment Brigade Challenge' }],
    band: 'Use a real stalled KPI, visible for more than two review cycles.',
    notes: u.partNotes(5, 0, { content: false, extra: 'Content:\n' + slice(P51, 'Part 1', 'Four Questions') }) });
  await d.list({ title: 'Four questions, in sequence, without skipping', fontSize: 26, rows: [
    { icon: 'FaCompass', label: 'Q1', text: 'Where is the friction?' },
    { icon: 'FaSignal', label: 'Q2', text: 'What is the signal?' },
    { icon: 'FaFilter', label: 'Q3', text: 'What is the clog?' },
    { icon: 'FaSlidersH', gold: true, label: 'Q4', text: 'What lever would you pull?' }],
    notes: N('THE FOUR QUESTIONS (5.1 · Part 2 · Diagnostic Triads)', 'Content:\n' + slice(P51, 'Four Questions', 'The Alignment Brigade Challenge'),
      'Guidance (Section 5): Watch for the symptom-to-lever skip. If a triad jumps from symptom to lever, pause and redirect: “Wait. Before we select the lever, have we correctly classified the clog? Let’s go back to Q3.”') });
  await d.prompt({ icon: 'FaGavel', label: 'Part 3 · The Alignment Brigade Challenge', text: 'What would have to be true for that lever to actually clear the clog?',
    foot: '90-second presentation, then three minutes of challenge from the full group.',
    notes: N('PART 3 · THE ALIGNMENT BRIGADE CHALLENGE (10 minutes)', 'Content:\n' + slice(P51, 'The Alignment Brigade Challenge')) });
  await d.list({ title: '5.2 · Observer evaluation criteria', fontSize: 26, rows: [
    { icon: 'FaBrain', label: '01', text: 'The Diagnostician reasoned through it' },
    { icon: 'FaStethoscope', label: '02', text: 'The clog was distinguished from the symptom' },
    { icon: 'FaQuestion', label: '03', text: 'The Challenger used curiosity' },
    { icon: 'FaFlagCheckered', label: '04', text: 'The intervention was concrete' }],
    notes: u.partNotes(5, 1) });
  await d.cards({ title: '5.3 · Participant commitments', cols: 3, items: [
    { icon: 'FaFilter', title: 'The clog I diagnosed', text: 'Category, COMPASS zone, signal' },
    { icon: 'FaSlidersH', title: 'The lever I will pull', text: 'Action, owner, completion date' },
    { icon: 'FaCalendarCheck', title: 'My follow-up review date', dark: true, text: 'And the evidence I will look for' }],
    notes: u.partNotes(5, 2) });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing', text: 'Name one clog that has been present in your organisation for more than six months.',
    foot: '“What has it actually cost the organisation in strategic momentum? And what is the real reason it hasn’t been cleared yet?”',
    notes: u.partNotes(5, 3) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
