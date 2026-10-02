// Unit 5 · Aligning Heart & Mind — facilitator deck with detailed presenter notes.
// Run: node unit05.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u05.json'), FH = R('unit3_m1_lens4_f.html'), PH = R('unit3_m1_lens4_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const gl = b => b.map(l => l.replace(/^◆ /, '')).join('\n');
const from = (lines, a) => { const i = lines.findIndex(l => l.startsWith(a)); if (i < 0) throw new Error('marker not found: ' + a); return i; };
const between = (lines, a, b) => { const i = lines.findIndex(l => l.startsWith(a)), j = b ? lines.findIndex((l, k) => k > i && l.startsWith(b)) : lines.length; return lines.slice(i, j < 0 ? lines.length : j).join('\n'); };

(async () => {
  const d = new Deck({ unit: 5, module: 3, moduleName: 'Influence', title: 'Aligning Heart & Mind' });
  const G = u.guide(), S5 = u.sec(5);

  await d.cover({ logo: LOGO, subtitle: 'The human operating system that moves strategy from intention to execution',
    notes: N('UNIT 5 · ALIGNING HEART & MIND\nModule 3 · Influence · Unit 5', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Before strategy becomes operational activity, it must be interpreted, experienced, and accepted by the people responsible for carrying it forward. This unit establishes the human operating system that enables strategy to move from intention to execution.',
      'Time: section timings in the facilitator file add up to about 267–325 minutes (4½ to 5½ hours), plus breaks.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time by section (from the facilitator file):\n- Section 1 · Awareness — What: 80–100 minutes\n- Section 2 · Intelligence — Why: 35–40 minutes\n- Section 3 · Extrapolating — Where: 50–60 minutes\n- Section 4 · Integration — Collective: 40–50 minutes\n- Section 5 · Application — In Practice: Step 1 15 min · Step 2 12–15 min · Step 3 15–20 min · Step 4 20–25 min', G[1], G[2]) });

  // ── Section 1
  await div(d, 1);
  await d.compare({ title: '1.1 · The human terrain of strategy execution', cols: [
    { icon: 'FaBrain', title: 'Cognition — Mind', sub: 'How strategy is interpreted', points: ['Professional expertise', 'Mental shortcuts and past experience', 'Risk perception'] },
    { icon: 'FaHeart', title: 'Emotion — Heart', sub: 'How strategy is experienced', points: ['Engagement energy and morale', 'Friction load', 'Psychological safety and values'] }],
    band: 'Execution begins inside the human system.',
    notes: u.partNotes(1, 0) });
  await d.list({ title: '1.2 · Five principles of aligning heart and mind', fontSize: 26, rows: [
    { icon: 'FaUsers', label: '1', text: 'Strategy Moves Through People' },
    { icon: 'FaRandom', label: '2', text: 'Misalignment Fragments Effort' },
    { icon: 'FaDraftingCompass', label: '3', text: 'Alignment Must Be Designed' },
    { icon: 'FaBrain', label: '4', text: 'Human Reactions Are Predictable' },
    { icon: 'FaEye', label: '5', text: 'Execution Must Be Visible in Behaviour' }],
    notes: u.partNotes(1, 1) });
  await d.cards({ title: '1.2 · Principle 2: the cost of misalignment', cols: 3, items: [
    { icon: 'FaCommentDots', title: 'Chinese Whispers', text: 'Intent mutates as it travels downward.' },
    { icon: 'FaRedo', title: 'Clarification Debt', text: '60–80% of leadership time spent re-explaining.' },
    { icon: 'FaUserSlash', title: 'Silent Disengagement', text: 'Outward compliance, inward withdrawal.' }],
    band: 'Low alignment: 41% lower productivity, 48% higher turnover (Gallup; PMI).',
    notes: N('1.2 · PRINCIPLE 2 — MISALIGNMENT FRAGMENTS EFFORT', 'Content:\n' + between(u.part(1, 1).content, 'Principle 2', 'Principle 3'),
      'Guidance: Principle 2 (Misalignment Fragments Effort) generates the most immediate recognition — use it as a pivot.') });
  {
    const p13 = u.part(1, 2), cut = from(p13.content, 'The 4 Checks of Mind, Heart, Hands and Habit');
    const g13 = p13.guidance[0].filter(l => /^(Key facilitation question|Watch for):/.test(l)).join('\n');
    await d.compare({ title: '1.3 · Change management: event and transition', cols: [
      { icon: 'FaCalendarCheck', title: 'The event', sub: 'Belongs to the organisation', points: ['Announced on a date', 'The structure, system or target is different', 'Leaders have finished their own transition'] },
      { icon: 'FaRoute', title: 'The transition', sub: 'Belongs to the person', points: ['Letting go of a familiar practice', 'Working out what the new one asks', 'Becoming able to do it'] }],
      band: 'Moving people from current practice to the practice the strategy requires.',
      notes: u.partNotes(1, 2, { content: false, extra: 'Content:\n' + p13.content.slice(0, cut).join('\n') }) });
    await d.list({ title: '1.3 · The 4 Checks of Mind, Heart, Hands and Habit', fontSize: 24, rows: [
      { icon: 'FaBrain', label: 'Mind · 3S · Explain', text: 'They understand the change, why it matters and what they do differently.' },
      { icon: 'FaHeart', label: 'Heart · SCARF · Involve', text: 'They want it to succeed.' },
      { icon: 'FaHandsHelping', label: 'Hands · STAT · Equip', text: 'They are able to do it.' },
      { icon: 'FaSyncAlt', label: 'Habit · ACE-IT · Reinforce', text: 'It has become the way they work.' },
      { icon: 'FaFlag', gold: true, text: 'A change stalls at the first check it fails.' }],
      notes: N('1.3 · THE 4 CHECKS OF MIND, HEART, HANDS AND HABIT', 'Guidance:\n' + g13, 'Content:\n' + p13.content.slice(cut).join('\n')) });
  }
  await d.cards({ title: '1.4 · The 3S Check: Shift, Stake, Step', cols: 3, items: [
    { icon: 'FaExchangeAlt', title: 'Shift', text: '“What is changing?”' },
    { icon: 'FaBalanceScale', title: 'Stake', text: '“What do we gain if we change, and what do we lose if we stay as we are?”' },
    { icon: 'FaShoePrints', title: 'Step', text: '“What do I do differently?”' }],
    band: 'Mind passes when three people give the same Shift, Stake and Step.',
    notes: u.partNotes(1, 3) });
  await d.list({ title: '1.5 · SCARF: five triggers of human resistance', fontSize: 26, rows: [
    { icon: 'FaCrown', label: 'Status', text: '“Will this reduce my importance?”' },
    { icon: 'FaQuestionCircle', label: 'Certainty', text: '“Do I know what success looks like?”' },
    { icon: 'FaUnlock', label: 'Autonomy', text: '“Am I losing control of my work?”' },
    { icon: 'FaUserFriends', label: 'Relatedness', text: '“Do I still belong here?”' },
    { icon: 'FaBalanceScale', label: 'Fairness', text: '“Is this being applied equitably?”' }],
    notes: u.partNotes(1, 4) });
  await d.cards({ title: '1.6 · The STAT Check: Skill, Time, Authority, Tools', cols: 2, titleBeside: true, items: [
    { icon: 'FaGraduationCap', title: 'Skill', text: '“Do they know how to do it?”' },
    { icon: 'FaClock', title: 'Time', text: '“Do they have the hours to do it?”' },
    { icon: 'FaKey', title: 'Authority', text: '“Are they allowed to decide and act?”' },
    { icon: 'FaTools', title: 'Tools', text: '“Do they have the systems and resources?”' }],
    notes: u.partNotes(1, 5) });
  await d.list({ title: '1.7 · ACE-IT: the observable behaviour standard', fontSize: 26, rows: [
    { icon: 'FaUserCheck', label: 'A · Accountability', text: 'full ownership for results' },
    { icon: 'FaAnchor', label: 'C · Commitment', text: 'anchored to agreed strategic intent' },
    { icon: 'FaComments', label: 'E · Engagement', text: 'listening to understand' },
    { icon: 'FaGem', label: 'I · Integrity', text: 'consistent with values, facts and truth' },
    { icon: 'FaEye', label: 'T · Transparency', text: 'reasoning, progress and constraints visible' }],
    notes: u.partNotes(1, 6) });

  // ── Section 2
  await div(d, 2);
  await d.prompt({ icon: 'FaBolt', label: '2.1 · The ignition point of strategy execution', text: '“This matters to me. I am willing to invest energy in making this succeed.”',
    foot: 'Until that moment occurs across the organisation, strategy remains theoretical.',
    notes: u.partNotes(2, 0) });
  await d.compare({ title: '2.2 · Compliance and commitment', cols: [
    { icon: 'FaClipboardList', title: 'Compliance', sub: 'Mind only', points: ['Authority, rules or monitoring', 'Continuous supervision', 'Mechanical'] },
    { icon: 'FaHeart', title: 'Commitment', sub: 'Mind and heart', points: ['Understanding, belief, ownership', 'Discretionary effort', 'Resilient when leaders are absent'] }],
    band: 'Alignment is the conversion point where strategic potential becomes movement.',
    notes: u.partNotes(2, 1) });
  await d.compare({ title: '2.3 · Installed and adopted', cols: [
    { icon: 'FaPlug', title: 'Installed', sub: 'A project outcome', points: ['System, structure or KPI is in place', 'People have been told', 'Yields cost'] },
    { icon: 'FaCheckDouble', title: 'Adopted', sub: 'A behavioural outcome', points: ['People work the new way unsupervised', 'The change has passed all four checks', 'Yields value'] }],
    band: 'The time between installed and adopted is the adoption gap.',
    notes: u.partNotes(2, 2) });

  // ── Section 3
  await div(d, 3);
  await d.list({ title: '3.1 · COMPASS: seven High Flammable Zones', fontSize: 24, rows: [
    ['C', 'Clarity of Strategic Direction'], ['O', 'Organisational Alignment'], ['M', 'Management Discipline'], ['P', 'People & Capability'],
    ['A', 'Allocation of Resources'], ['S', 'Sensing & Adaptation'], ['S', 'Systems & Execution']].map(([l, t]) => ({ icon: 'FaFire', label: l, text: t })),
    notes: u.partNotes(3, 0) });
  await d.compare({ title: '3.2 · From High Flammable to Burning Platform', cols: [
    { icon: 'FaFire', title: 'High Flammable Zone', sub: 'A leverage point', points: ['Strong alignment: compounding momentum', 'Weak alignment: multiplying friction', 'Early intervention stabilises it'] },
    { icon: 'FaExclamationTriangle', title: 'Burning Platform', sub: 'Past the escalation threshold', points: ['Breakdown visible and costly', 'Reactive fixes cost far more', 'Requires systemic rebuilding'] }],
    notes: u.partNotes(3, 1) });
  await d.list({ title: '3.3 · Change readiness: the scan', fontSize: 26, rows: [
    { icon: 'FaListUl', label: '1', text: 'Name one change and list the groups it affects.' },
    { icon: 'FaTasks', label: '2', text: 'Rate each group on the 4 Checks: 1 (fully in place) to 5 (missing).' },
    { icon: 'FaFlag', label: '3', text: 'Start at each group’s first check that scores 4 or 5.' },
    { icon: 'FaFire', gold: true, text: 'Low readiness inside a High Flammable Zone comes first.' }],
    notes: u.partNotes(3, 2) });

  // ── Section 4
  await div(d, 4);
  await d.compare({ title: '4.1 · The Converging Zone', cols: [
    { icon: 'FaRandom', title: 'Without', sub: 'Collective Intelligence', points: ['Different interpretations transmitted', 'COMPASS domains drift', 'Competing signals'] },
    { icon: 'FaCompressArrowsAlt', title: 'With', sub: 'Collective Intelligence', points: ['Direction clear across all layers', 'Resources reinforce priorities', 'One coherent signal'] }],
    notes: u.partNotes(4, 0) });
  {
    const s = d.slide(); d.title(s, '4.2 · Collective intelligence by role');
    const roles = [['CEO', 'Clarity · Alignment'], ['CFO', 'Resources · Discipline'], ['COO', 'Systems · Discipline'], ['CHRO', 'People · Alignment'], ['CTO/CIO', 'Systems · Sensing'],
      ['CMO', 'Clarity · Sensing'], ['CCO', 'Resources · Alignment'], ['CPO', 'Systems · Resources'], ['CRO', 'Discipline · Systems'], ['CSO', 'Clarity · Sensing']];
    T(s, 'Primary COMPASS activation by role', { x: 0.6, y: 1.55, w: 12, h: 0.5, fontSize: 24, italic: true, color: C.muted });
    roles.forEach(([r, c], i) => {
      const x = 0.6 + (i % 2) * 6.15, y = 2.15 + Math.floor(i / 2) * 0.98;
      box(s, x, y, 5.95, 0.85, C.tint);
      T(s, [{ text: r + '   ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: c }], { x: x + 0.25, y, w: 5.5, h: 0.85, fontSize: 24, valign: 'middle' });
    });
    s.addNotes(u.partNotes(4, 1));
  }
  await d.cards({ title: '4.3 · Leading change with one voice', cols: 2, titleBeside: true, items: [
    { icon: 'FaBullhorn', title: 'One message', text: 'Protects Mind: every leader gives the same Shift, Stake and Step.' },
    { icon: 'FaUserCheck', title: 'One example', text: 'Protects Heart: leaders show the behaviours before they ask for them.' },
    { icon: 'FaListOl', title: 'One sequence', text: 'Protects Hands: the team agrees the order and pace of its changes.' },
    { icon: 'FaUserTie', title: 'One owner', text: 'Protects Habit: one named leader answers for adoption.' }],
    notes: u.partNotes(4, 2) });

  // ── Section 5
  await d.section({ num: 5, name: 'Application', anchor: 'In Practice', heading: S5.h2, outcomes: S5.slo,
    notes: N('SECTION 5 · APPLICATION — IN PRACTICE\n' + S5.h2 + '\n' + S5.sub, 'Section learning outcomes:\n' + S5.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'), gl(S5.lead.guidance[0])) });
  {
    const fc = S5.lead.content, pc = u.P.sections[4].lead.content, G5 = S5.lead.guidance.map(gl);
    const fMap = from(fc, 'Work independently. Choose two changes'), fRole = from(fc, 'Work independently. For the two changes');
    const pMap = from(pc, 'Work independently. Choose two changes'), pRole = from(pc, 'Work independently. For the two changes');
    await d.list({ title: 'Step 1 · The Change Transition Map', fontSize: 26, rows: [
      { icon: 'FaExchangeAlt', label: 'Two changes (15 min):', text: 'one practice to start, one to stop' },
      { icon: 'FaTasks', label: 'Run the 4 Checks:', text: 'Mind · 3S, Heart · SCARF, Hands · STAT, Habit · ACE-IT' },
      { icon: 'FaSearch', label: 'Weakest check:', text: 'the first check that fails, and what the group needs' },
      { icon: 'FaUserTie', gold: true, label: 'Owner:', text: 'one named leader who answers for adoption' }],
      notes: N('APPLICATION EXERCISE · STEP 1 — THE CHANGE TRANSITION MAP', G5.slice(1, 3), 'Content:\n' + fc.slice(fMap, fRole).join('\n'),
        'Participant file (Section 5, Step 1) — what participants complete:\n' + pc.slice(pMap, pRole).join('\n')) });
    await d.list({ title: 'Mapping how our roles connect', fontSize: 26, rows: [
      { icon: 'FaUser', label: 'Step 2 · Role Connections (12–15 min):', text: 'your role and the two you depend on most' },
      { icon: 'FaExchangeAlt', label: 'Step 3 · Exchange & Dialogue (15–20 min):', text: 'test each other’s maps and tables' },
      { icon: 'FaUsers', label: 'Step 4 · Plenary Synthesis (20–25 min):', text: 'the weakest domain and the change sequence' },
      { icon: 'FaFlagCheckered', gold: true, label: '30-day commitment:', text: 'one behaviour, tied to a mapped change' }],
      notes: N('APPLICATION EXERCISE · STEPS 2–4', G5.slice(3), 'Content:\n' + fc.slice(fRole).join('\n'),
        'Participant file (Section 5, Steps 2–4) — what participants complete:\n' + pc.slice(pRole).join('\n')) });
  }
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing question', text: 'Which COMPASS domain is this team most likely rating too generously — and which executive role has quietly stopped carrying its alignment responsibility there?',
    notes: u.partNotes(5, 0) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
