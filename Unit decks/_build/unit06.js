// Unit 6 · Performance Management Setup — facilitator deck with detailed presenter notes.
// Run: node unit06.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u06.json'), FH = R('unit3_m1_lens5_f.html'), PH = R('unit3_m1_lens5_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const NOTIME = 'Time: the facilitator file gives no suggested time for this section.';

(async () => {
  const d = new Deck({ unit: 6, module: 3, moduleName: 'Influence', title: 'Performance Management Setup' });
  const G = u.guide();

  await d.cover({ logo: LOGO, subtitle: 'Building the architecture of execution accountability',
    notes: N('UNIT 6 · PERFORMANCE MANAGEMENT SETUP\nModule 3 · Influence · Unit 6', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): A performance management system is an execution architecture. This unit equips leaders to design systems that translate strategy into individual accountability, calibrate progress rhythms, and sustain collective ownership across the enterprise.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time: the facilitator file gives suggested timing only for the Section 5 simulation: individual work 15 min → table discussion 15 min → group debrief 15 min.', G[1], G[2]) });

  // ── Section 1
  await div(d, 1, NOTIME);
  await d.compare({ title: '1.1 · Measurement and management', cols: [
    { icon: 'FaChartBar', title: 'Measurement', sub: 'What happened?', points: ['An input', 'Data, results, scores', 'Dashboards and reports'] },
    { icon: 'FaCompass', title: 'Management', sub: 'What do we do about it?', points: ['The leadership response', 'Decisions and actions', 'Accountability'] }],
    band: 'A management system converts reports into movement.',
    notes: u.partNotes(1, 0, { content: false, extra: 'Content:\n' + u.part(1, 0).content.slice(0, u.part(1, 0).content.indexOf('The Correct Sequence')).join('\n') }) });
  await d.list({ title: '1.1 · The correct sequence', fontSize: 26, rows: [
    { icon: 'FaFlag', label: '1 · Define Success', text: 'what, by when, at what level' },
    { icon: 'FaSitemap', label: '2 · Design the Management System', text: 'conversations, owners, decisions' },
    { icon: 'FaRuler', label: '3 · Design the Measurement Infrastructure', text: 'data that serves the conversations' },
    { icon: 'FaSyncAlt', gold: true, label: '4 · Manage Using Data', text: 'where most organisations start' }],
    notes: N('1.1 · THE CORRECT SEQUENCE', 'Content:\n' + u.part(1, 0).content.slice(u.part(1, 0).content.indexOf('The Correct Sequence')).join('\n')) });
  await d.list({ title: '1.2 · The FACES framework', fontSize: 26, rows: [
    { icon: 'FaTrophy', label: 'F', text: 'Foster a Results Culture' }, { icon: 'FaStream', label: 'A', text: 'Align Individual Performance' },
    { icon: 'FaEye', label: 'C', text: 'Create Measurement Transparency' }, { icon: 'FaUsers', label: 'E', text: 'Embed Shared Accountability' },
    { icon: 'FaSeedling', label: 'S', text: 'Support Continuous Development' }],
    notes: u.partNotes(1, 1) });
  await d.cards({ title: '1.3 · The Three Sights of Progress', cols: 3, items: [
    { icon: 'FaChessKnight', title: 'Sight 1 · Strategy', text: 'Strategic OKRs · typically 30–50% at senior levels' },
    { icon: 'FaCogs', title: 'Sight 2 · Operational', text: 'Departmental KPIs · typically 30–50%' },
    { icon: 'FaHandshake', title: 'Sight 3 · Behavioural & Values', text: '360° feedback · typically 20–40%' }],
    notes: u.partNotes(1, 2) });
  await d.list({ title: '1.4 · The 1–5 rating scale', fontSize: 24, rows: [
    { icon: 'FaExclamationTriangle', label: '1 · Poor', text: 'immediate PIP within 30 days' },
    { icon: 'FaTools', label: '2 · Needs Improvement', text: 'structured development plan' },
    { icon: 'FaMedal', gold: true, label: '3 · Meets Expectations: SOLID GOLD', text: 'recognition and retention' },
    { icon: 'FaArrowUp', label: '4 · Exceeds Expectations', text: 'stretch opportunities; retention investment' },
    { icon: 'FaStar', label: '5 · Outstanding', text: 'mandatory structural follow-through' }],
    notes: u.partNotes(1, 3) });

  // ── Section 2
  await div(d, 2, NOTIME);
  await d.list({ title: '2.1 · PM as the execution bridge', fontSize: 26, rows: [
    { icon: 'FaSitemap', label: 'Bridge 1', text: 'Decomposing the Big Picture' },
    { icon: 'FaBullseye', label: 'Bridge 2', text: 'Defining the Logic of Success' },
    { icon: 'FaHeartbeat', label: 'Bridge 3', text: 'Calibrating the Rhythm' },
    { icon: 'FaComments', label: 'Bridge 4', text: 'Structuring the Dialogue' },
    { icon: 'FaCalculator', gold: true, label: 'Progress per Period =', text: '(End Target − Baseline) ÷ Number of Periods' }],
    notes: u.partNotes(2, 0) });
  await d.compare({ title: '2.2 · Compliance and commitment architecture', cols: [
    { icon: 'FaGavel', title: 'Compliance', sub: 'Done to the individual', points: ['Leader holds accountability', 'Assessment and judgement', 'Consequence and control'] },
    { icon: 'FaHandsHelping', title: 'Commitment', sub: 'Done with the individual', points: ['Team co-owns accountability', 'Inquiry and problem-solving', 'Root cause; co-designed recovery'] }],
    notes: u.partNotes(2, 1) });
  await d.compare({ title: '2.3 · Rules of the game', cols: [
    { icon: 'FaClipboardList', title: 'Step 1', sub: 'Prepare the Foundation', points: ['Rating Scale', 'Performance Thresholds', 'Evidence Standards', 'Review Routine'] },
    { icon: 'FaStream', title: 'Step 2', sub: 'The Cascade', points: ['Verify the Data', 'Assign Ownership', 'Focus on Learning'] }],
    notes: u.partNotes(2, 2) });
  await d.compare({ title: '2.4 · Leader and team: a critical distinction', cols: [
    { icon: 'FaUsers', title: 'The team', sub: 'is measured on', points: ['Activities, outputs, behaviours', 'The current period', 'Monthly / quarterly review'] },
    { icon: 'FaUserTie', title: 'The leader', sub: 'is measured on', points: ['Cumulative outcome trajectory', 'End of cycle', 'Quarterly / bi-annual review'] }],
    notes: u.partNotes(2, 3) });

  // ── Section 3
  await div(d, 3, NOTIME);
  await d.prompt({ icon: 'FaUsers', label: '3.1 · The Alignment Brigade', text: 'When we look at the same performance data, do we interpret it from the same perspective — or from the perspective of our function?',
    foot: 'At enterprise level, the performance management system sits in the executive team.',
    notes: u.partNotes(3, 0) });
  {
    const s = d.slide(); d.title(s, '3.2 · CXO hot zones');
    const roles = [['CEO', 'Enterprise Visibility'], ['CFO', 'Financial Signals'], ['COO', 'Execution Rhythm'], ['CHRO', 'Capability & Behaviour'], ['CTO/CIO', 'System Enablement'],
      ['CMO', 'Market Signal'], ['CCO', 'Revenue Velocity'], ['CPO', 'Supply Reliability'], ['CRO', 'Risk & Governance'], ['CSO', 'Strategic Coherence']];
    roles.forEach(([r, c], i) => {
      const x = 0.6 + (i % 2) * 6.15, y = 1.7 + Math.floor(i / 2) * 1.05;
      box(s, x, y, 5.95, 0.9, C.tint);
      T(s, [{ text: r + '   ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: c }], { x: x + 0.25, y, w: 5.5, h: 0.9, fontSize: 26, valign: 'middle' });
    });
    s.addNotes(u.partNotes(3, 1));
  }
  await d.cards({ title: '3.3 · The Three Execution Gaps', cols: 3, items: [
    { icon: 'FaRandom', title: 'Gap 1', text: 'Competing Definitions of Progress' },
    { icon: 'FaEyeSlash', title: 'Gap 2', text: 'Measurement Blind Spots' },
    { icon: 'FaCoins', title: 'Gap 3', dark: true, text: 'Incentive Misalignment' }],
    band: 'When incentives and strategy diverge, strategy loses.',
    notes: u.partNotes(3, 2) });
  await d.stat({ title: '3.4 · The continuous PM shift', big: '41%', caption: 'of organisations have moved to real-time or near-real-time feedback',
    rows: [{ icon: 'FaSyncAlt', label: 'Trend 1', text: 'From Annual to Continuous' }, { icon: 'FaSeedling', label: 'Trend 2', text: 'From Rating-Centric to Development-Centric' }, { icon: 'FaUsers', label: 'Trend 3', text: 'From Individual to Team Performance' }],
    notes: u.partNotes(3, 3) });

  // ── Section 4
  await div(d, 4, NOTIME);
  await d.cards({ title: '4.1 · The Collective Progress Signal', cols: 3, items: [
    { icon: 'FaTachometerAlt', title: 'Execution Traction', text: 'Are our activities generating the progress we expected?' },
    { icon: 'FaBalanceScale', title: 'Execution Balance', text: 'Are resources in the right proportions?' },
    { icon: 'FaHandPaper', title: 'Execution Intervention', dark: true, text: 'Where must we intervene?' }],
    notes: u.partNotes(4, 0) });
  await d.cards({ title: '4.2 · Three elements of enterprise PM design', cols: 3, items: [
    { icon: 'FaCalendarAlt', title: 'Reporting Cadence', text: 'When' },
    { icon: 'FaChartBar', title: 'Periodic Measures', text: 'What now' },
    { icon: 'FaRoute', title: 'Cumulative Progress', dark: true, text: 'How far' }],
    band: 'Cumulative Progress % = (Baseline − Current) ÷ (Baseline − Target) × 100',
    notes: u.partNotes(4, 1) });
  await d.list({ title: '4.3 · The EXECUTION framework', fontSize: 24, rows: [
    ['E', 'Enterprise: Strategy First'], ['X', 'eXecution: Line-of-Sight'], ['E', 'Evidence: Evidence-Based Measurement'], ['C', 'Collective: Collective Ownership'], ['U', 'Understand: Outcomes First'],
    ['T', 'Transparent: Measurement Logic'], ['I', 'Incentive: Incentive Alignment'], ['O', 'Ongoing: Review Rhythm'], ['N', 'Navigate: Collective Insight']].map(([l, t]) => ({ icon: 'FaCheck', label: l, text: t })),
    notes: u.partNotes(4, 2) });

  // ── Section 5
  await div(d, 5);
  await d.cards({ title: '5.1 · Case: MyHealth Live Portal', cols: 3, items: [
    { icon: 'FaClock', title: 'Outcome 1', text: 'Complaint resolution: 48 hrs → 12 hrs' },
    { icon: 'FaUserMd', title: 'Outcome 2', text: 'Referral decision: 10 days → 3 days' },
    { icon: 'FaHospital', title: 'Outcome 3', text: 'Cross-facility collaboration: 30% → 70%' }],
    band: 'A hospital chain: 12 facilities, three regions, an 18-month priority.',
    notes: u.partNotes(5, 0) });
  await d.list({ title: 'The six design tasks', fontSize: 24, rows: [
    { icon: 'FaColumns', label: 'Task 1', text: 'PM Scorecard Architecture (for the COO)' },
    { icon: 'FaSortNumericUp', label: 'Task 2', text: 'Scoring Logic Design (Outcome 1)' },
    { icon: 'FaCalculator', label: 'Task 3', text: 'Baseline Simulation' },
    { icon: 'FaCalendarAlt', label: 'Task 4', text: 'Reporting Cadence Design' },
    { icon: 'FaChartBar', label: 'Task 5', text: 'Periodic Measures Selection' },
    { icon: 'FaDesktop', label: 'Task 6', text: 'Reporting Tool Design' }],
    notes: N('SECTION 5 · THE SIX DESIGN TASKS', 'Participant activity: participants write each design in their own file, in the box beneath each task.',
      [1, 2, 4, 5, 6].map(j => u.partNotes(5, j, { head: false })).join('\n\n———\n\n')) });
  await d.cards({ title: 'Task 3 · Baseline simulation at month 6 of 18', cols: 3, items: [
    { icon: 'FaClock', title: 'Outcome 1', text: 'Current 40 hrs · baseline 48 · target 12' },
    { icon: 'FaUserMd', title: 'Outcome 2', text: 'Current 8 days · baseline 10 · target 3' },
    { icon: 'FaHospital', title: 'Outcome 3', text: 'Current 42% · baseline 30% · target 70%' }],
    band: 'Expected progress at month 6 of an 18-month cycle = 33%.',
    notes: N(u.partNotes(5, 3),
      'Worked calculation for the facilitator (applying the file’s formula):\n- Outcome 1: (48 − 40) ÷ (48 − 12) × 100 = 22%\n- Outcome 2: (10 − 8) ÷ (10 − 3) × 100 = 29%\n- Outcome 3: (30 − 42) ÷ (30 − 70) × 100 = 30%\nAgainst an expected 33%, Outcome 1 is furthest behind its trajectory.') });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing', text: 'Name one design change you will make to your current PM system within the next 30 days.',
    foot: 'Which FACES function, which EXECUTION principle, which of the Three Sights — and what, specifically, will change?',
    notes: u.partNotes(5, 7) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
