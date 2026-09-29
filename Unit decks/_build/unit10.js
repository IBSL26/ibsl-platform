// Unit 10 · ESRG Alignment — facilitator deck with detailed presenter notes.
// Run: node unit10.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u10.json'), FH = R('unit4_m1_lens9_f.html'), PH = R('unit4_m1_lens9_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const slice = (lines, a, b) => { const i = lines.findIndex(l => l.startsWith(a)); const j = b ? lines.findIndex((l, k) => k > i && l.startsWith(b)) : -1; return lines.slice(i, j < 0 ? lines.length : j).join('\n'); };
const NOTIME = 'Time: the facilitator file gives no minute timing for this section (see the Timing watch point in the Session Overview).';
const SEP = '\n\n———\n\n';

(async () => {
  const d = new Deck({ unit: 10, module: 4, moduleName: 'Grounding', title: 'ESRG Alignment' });
  const G = u.guide();
  const X52 = u.part(5, 1).content;

  await d.cover({ logo: LOGO, subtitle: 'Is the organisation itself built to sustain this performance over time?',
    notes: N('UNIT 10 · ESRG ALIGNMENT\nModule 4 · Grounding · Unit 10', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Grounding asks a harder question: whether the organisation itself is built to sustain this performance over time. ESRG Alignment is the discipline of ensuring that Environment, Systems, Resources, and Governance are fully equipped to support consistent delivery.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time: the facilitator file times only the Application exercise (55 minutes: 5 minutes choose the set, 35 minutes build the COC, 15 minutes COC Challenge). Awareness and Intelligence can move at pace; Extrapolating benefits from brief cross-functional discussion.', G[1], G[2]) });

  // ── Section 1
  await div(d, 1, NOTIME);
  await d.prompt({ icon: 'FaMountain', label: '1.1 · The Grounding question', text: 'Is the organisation itself built to sustain this performance over time?',
    foot: 'Most strategies that survive the first quarter fail by the third.', notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · The four ESRG domains', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaBuilding', title: 'E · Environment', text: 'Physical and behavioural conditions of work.' },
    { icon: 'FaCogs', title: 'S · Systems', text: 'The operational infrastructure of execution.' },
    { icon: 'FaUserFriends', title: 'R · Resources', text: 'The capability capacity of the organisation.' },
    { icon: 'FaGavel', title: 'G · Governance', text: 'Accountability and decision discipline.' }],
    notes: u.partNotes(1, 1) });
  await d.prompt({ icon: 'FaPuzzlePiece', label: '1.3 · ESRG synthesis: the interdependence principle', text: 'A weakness in any one domain creates friction that the other three cannot fully compensate for.',
    foot: 'Sustained execution capacity depends on the synchronisation of all four domains.', notes: u.partNotes(1, 2) });

  // ── Section 2
  await div(d, 2, NOTIME);
  await d.cards({ title: '2.1 · The ESRG ignition point', cols: 4, titleSize: 24, items: [
    { icon: 'FaBuilding', title: 'E · Enable the Work', text: 'Physical and behavioural conditions both active' },
    { icon: 'FaStream', title: 'S · Streamline the Flow', text: 'Execution made visible' },
    { icon: 'FaCoins', title: 'R · Resource the Strategy', text: 'Resource the people who carry it' },
    { icon: 'FaDrum', title: 'G · Govern the Rhythm', dark: true, text: 'A steady cadence of accountability' }],
    band: '“When all four operate together, the operating system reinforces the work itself.”',
    notes: u.partNotes(2, 0) });
  await d.list({ title: '2.2 · The IBSL Cultural Operating Code', fontSize: 24, rows: [
    { icon: 'FaBullseye', label: 'AIM', text: 'Intentionality' },
    { icon: 'FaComment', label: 'SAY', text: 'Integrity' },
    { icon: 'FaHandsHelping', label: 'ONE', text: 'Collaboration' },
    { icon: 'FaUserCheck', label: 'OAR', text: 'Accountability' },
    { icon: 'FaStar', label: 'SET', text: 'Excellence' },
    { icon: 'FaHeart', gold: true, label: 'SEE', text: 'Human-Centricity' }],
    notes: u.partNotes(2, 1) });
  await d.list({ title: '2.3 · Worked example: the ESRG Execution Scanner', fontSize: 26, rows: [
    { icon: 'FaUsers', label: 'Six executives,', text: 'one ESRG issue each, scanned independently' },
    { icon: 'FaProjectDiagram', label: 'O · Organisational Alignment', text: 'flagged by 4 of 6' },
    { icon: 'FaClipboardCheck', label: 'M · Management Discipline', text: 'flagged by 3 of 6' },
    { icon: 'FaUserFriends', label: 'P · People & Capability', text: 'flagged by 3 of 6' },
    { icon: 'FaExclamationCircle', gold: true, label: 'Overall: RED', text: 'critical friction detected' }],
    notes: u.partNotes(2, 2) });

  // ── Section 3
  await div(d, 3, NOTIME);
  await d.cards({ title: '3.1–3.4 · ESRG friction zones', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaBuilding', title: 'E · Environment', text: 'Values misalignment; psychological safety failures.' },
    { icon: 'FaCogs', title: 'S · Systems', text: 'Workarounds; data fragmentation.' },
    { icon: 'FaUserFriends', title: 'R · Resources', text: 'Capability gaps; unsustainable workloads.' },
    { icon: 'FaGavel', title: 'G · Governance', text: 'Selective accountability; absent leadership.' }],
    notes: [0, 1, 2, 3].map(j => u.partNotes(3, j)).join(SEP) });
  await d.list({ title: '3.5 · Friction as organisational intelligence', fontSize: 24, rows: [
    { icon: 'FaBuilding', label: 'Values misalignment', text: 'gap between cultural aspiration and reality' },
    { icon: 'FaCogs', label: 'Systems fragmentation', text: 'infrastructure built for a different era' },
    { icon: 'FaUserFriends', label: 'Capacity constraints', text: 'resources behind strategic ambition' },
    { icon: 'FaGavel', gold: true, label: 'Governance inconsistency', text: 'leadership below the standard required' }],
    notes: u.partNotes(3, 4) });

  // ── Section 4
  await div(d, 4, NOTIME);
  await d.prompt({ icon: 'FaMountain', label: '4.1 · The Execution Muscle Scan', text: 'Are the organisational conditions still supporting our ability to continue the climb?',
    foot: 'Conducted quarterly, immediately after performance has been examined.', notes: u.partNotes(4, 0) });
  await d.cards({ title: '4.2 · The four reflections', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaBuilding', title: 'E · Enabling the Work', text: 'Easy to collaborate, speak honestly and advance the work?' },
    { icon: 'FaStream', title: 'S · Streamlining the Flow', text: 'Work, data and decisions moving smoothly and visibly?' },
    { icon: 'FaCoins', title: 'R · Resourcing the Strategy', text: 'Capability, capacity and sustainability over time?' },
    { icon: 'FaDrum', title: 'G · Maintaining the Rhythm', text: 'Decisions, accountability and ethics at the pace required?' }],
    notes: u.partNotes(4, 1) });
  await d.list({ title: '4.3 · The COMPASS-ESRG connection', fontSize: 24, rows: [
    { icon: 'FaCompass', label: 'C · Clarity of Direction', text: '→ Governance' },
    { icon: 'FaProjectDiagram', label: 'O · Organisational Alignment', text: '→ Environment' },
    { icon: 'FaClipboardCheck', label: 'M · Management Discipline', text: '→ Governance' },
    { icon: 'FaUserFriends', label: 'P · People & Capability', text: '→ Resources' },
    { icon: 'FaCoins', label: 'A · Allocation of Resources', text: '→ Resources' },
    { icon: 'FaCogs', label: 'S1 · Systems & Execution', text: '→ Systems' },
    { icon: 'FaSatelliteDish', gold: true, label: 'S2 · Sensing & Adaptation', text: '→ Environment + Systems' }],
    notes: u.partNotes(4, 2) });
  await d.prompt({ icon: 'FaLayerGroup', label: '4.4–4.5 · The Enterprise ESRG Alignment Agenda', text: 'Individual observation becomes collective intelligence.',
    foot: 'Each leader contributes one ESRG friction observation to a shared, structured agenda.',
    notes: [3, 4].map(j => u.partNotes(4, j)).join(SEP) });

  // ── Section 5
  await div(d, 5, 'Time: 55 minutes — Part 1 · 5 minutes choose your set; Part 2 · 35 minutes build the COC; Part 3 · 15 minutes COC Challenge (full group). Protect all 55 minutes.');
  await d.cards({ title: '5.1 · The three value sets: choose one', cols: 3, items: [
    { icon: 'FaGavel', title: 'A · Governance-Led', text: 'Transparency, Courage, Service, Resilience, Innovation, Stewardship' },
    { icon: 'FaChartLine', title: 'B · Performance-Led', text: 'Trust, Agility, Quality, Ownership, Growth, Inclusion' },
    { icon: 'FaCompass', title: 'C · Purpose-Led', dark: true, text: 'Purpose, Integrity, Ubuntu, Excellence, Boldness, Care' }],
    notes: u.partNotes(5, 0, { prompts: false }) });
  await d.list({ title: '5.2 · Build the COC: three steps per value', fontSize: 26, rows: [
    { icon: 'FaEye', label: 'Step 1', text: 'Define the behaviour' },
    { icon: 'FaFont', label: 'Step 2', text: 'Build the acronym from three action words' },
    { icon: 'FaPenFancy', gold: true, label: 'Step 3', text: 'Write the norm statement' }],
    notes: u.partNotes(5, 1, { content: false, extra: 'Content:\n' + slice(X52, 'Part 1', 'The COC Challenge') }) });
  await d.list({ title: 'The COC Challenge: three tests', fontSize: 26, rows: [
    { icon: 'FaUserPlus', label: 'Test 1', text: 'The New Employee Test' },
    { icon: 'FaCompressArrowsAlt', label: 'Test 2', text: 'The Pressure Test' },
    { icon: 'FaUserCircle', gold: true, label: 'Test 3', text: 'The Mirror Test' }],
    notes: N('THE COC CHALLENGE (15 minutes, full group)', 'Content:\n' + slice(X52, 'The COC Challenge'),
      'Guidance (5.3): During the presentations, capture the strongest norm from each value set on a shared board. Close by asking the group which patterns appear across the sets.',
      'FACILITATOR REFERENCE · COMPLETE COC FOR ALL THREE SETS (facilitator use only; stays with the facilitator; do not show or distribute before teams have completed their own translation work):\n' + u.part(5, 3).content.join('\n')) });
  await d.cards({ title: '5.3 · Exercise output', cols: 3, items: [
    { icon: 'FaListOl', title: 'Three draft norms', text: 'Named, acronym-based, observable' },
    { icon: 'FaComments', title: 'One test commitment', text: 'The norm for your next difficult conversation' },
    { icon: 'FaCalendarCheck', title: 'A review date', dark: true, text: 'Take the draft COC to your team' }],
    notes: u.partNotes(5, 2) });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing', text: 'Name one ESRG condition that has been misaligned for more than two quarters.',
    foot: '“What has that misalignment actually cost in strategic momentum? And what is the real reason it has not been restored?”',
    notes: u.partNotes(5, 4) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
