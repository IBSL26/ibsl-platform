// Unit 11 deck (28 Oct 2026 clean-up): slides follow the live pages unit4_m1_lens10_f/p.html.
// Run: node slides.js <out.pptx> <logo.png>
const { Deck, C, F, T, box, badge } = require('./lib2');
const N = require('./notes');
const [OUT, LOGO] = process.argv.slice(2);

// table: rows of cells; first row header
function table(d, s, rows, o) {
  const hdr = rows[0].map(t => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.forest }, fontFace: F.head } }));
  const body = rows.slice(1).map((r, i) => r.map((t, j) => ({ text: t, options: { color: C.ink, bold: j === 0 && o.boldFirst !== false, fill: { color: i % 2 ? C.white : C.tint } } })));
  s.addTable([hdr, ...body], Object.assign({ x: 0.6, y: 1.65, w: 12.13, fontSize: 24, fontFace: F.body, border: { type: 'solid', pt: 1, color: C.line }, valign: 'middle', margin: 0.08 }, o.t));
}
async function tslide(d, title, rows, notes, o = {}) {
  const s = d.slide(); d.title(s, title); table(d, s, rows, o);
  if (o.band) { box(s, 0.6, 6.15, 12.13, 0.85, C.deep); T(s, o.band, { x: 0.9, y: 6.15, w: 11.6, h: 0.85, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); }
  s.addNotes(notes);
}

(async () => {
  const d = new Deck({ unit: 11, module: 4, moduleName: 'Grounding', title: 'Culture Reinforcement & Organisational Health' });
  await d.cover({ logo: LOGO, subtitle: 'How organisational values become lived culture, and how that culture shows in organisational health', notes: N.s1 });
  await d.list({ title: 'Key learning outcomes', fontSize: 26, rows: [
    { icon: 'FaCheck', text: 'Diagnose organisational health by evaluating how organisational values and cultural norms influence collective behaviour and strategic performance.' },
    { icon: 'FaCheck', text: 'Shape and reinforce organisational culture by establishing behavioural standards and embedding cultural operating norms that strengthen organisational health.' }], notes: N.s2 });
  await d.list({ title: 'The unit journey', fontSize: 24, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness — What', text: 'Values, culture and organisational health' },
    { icon: 'FaLightbulb', label: 'Section 2 · Intelligence — Why', text: 'Health as a performance multiplier' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating — Where', text: 'Health signals and functional bias' },
    { icon: 'FaUsers', label: 'Section 4 · Integration — Collective', text: 'The Cross-CXO Health Architecture' },
    { icon: 'FaClipboardCheck', gold: true, label: 'Section 5 · Application — In Practice', text: 'The Organisational Health Clinic' }], notes: N.s3 });

  // Section 1
  await d.section({ num: 1, name: 'Awareness', anchor: 'What', heading: 'Values, Culture & Organisational Health', outcomes: [
    'Evaluate how organisational values translate into cultural norms and practices that shape organisational health.',
    'Diagnose organisational health strengths and vulnerabilities across observable behaviour and its underlying conditions.'], notes: N.s4 });
  await d.cards({ title: '1.1a · Organisational values: what we stand for', cols: 2, items: [
    { icon: 'FaUserCheck', title: 'Establish behavioural expectations', text: 'Values define the standards of conduct expected across the organisation.' },
    { icon: 'FaBalanceScale', title: 'Provide a basis for accountability', text: 'Leaders evaluate how results are achieved, alongside the results themselves.', dark: true }],
    band: 'Values are the principles that guide how an organisation conducts itself.', notes: N.s5 });
  await tslide(d, '1.1b · Values into behavioural standards', [
    ['Value', 'Expected behavioural standard'],
    ['Integrity', 'Act honestly, communicate transparently, uphold ethical commitments'],
    ['Accountability', 'Take ownership, honour commitments, report progress accurately'],
    ['Respect', 'Treat others fairly, listen constructively, recognise perspectives'],
    ['Excellence', 'Maintain high standards, address gaps, keep improving'],
    ['Collaboration', 'Share information, coordinate efforts, contribute to collective outcomes']], N.s6, { t: { colW: [2.9, 9.23], rowH: 0.72 } });
  await d.compare({ title: '1.2 · Organisational culture: how we do things', cols: [
    { icon: 'FaUsers', title: 'Culture', sub: 'Shared behavioural norms', points: ['Values become behavioural expectations', 'Behaviours repeat in daily work', '“The way we do things around here”'] },
    { icon: 'FaCode', title: 'Cultural Operating Code', sub: 'Values made explicit as norms', points: ['How people work together', 'How accountability is exercised', 'How people communicate and contribute'] }], notes: N.s7 });
  await d.list({ title: '1.3a · The Five Observable Health Traits', fontSize: 24, rows: [
    { icon: 'FaHandshake', label: 'Minimal Politics', text: 'open collaboration, limited personal agendas' },
    { icon: 'FaCompass', label: 'Minimal Confusion', text: 'direction, priorities and responsibilities understood' },
    { icon: 'FaSmile', label: 'High Morale', text: 'commitment, motivation and confidence' },
    { icon: 'FaCogs', label: 'High Productivity', text: 'coordinated effort that produces outcomes' },
    { icon: 'FaUserFriends', gold: true, label: 'Low Turnover', text: 'capable employees choose to stay' }], notes: N.s8 });
  await d.list({ title: '1.3b · The Organisational Health Pyramid', fontSize: 26, rows: [
    { icon: 'FaShieldAlt', label: '1 · Trust', text: 'the foundation' },
    { icon: 'FaComments', label: '2 · Experiences', text: 'shaped by trust' },
    { icon: 'FaBrain', label: '3 · Beliefs', text: 'formed by experiences' },
    { icon: 'FaRunning', label: '4 · Actions', text: 'driven by beliefs' },
    { icon: 'FaChartLine', gold: true, label: '5 · Results', text: 'the visible traits' }], notes: N.s9 });
  await d.compare({ title: '1.3c · Connecting the traits and the pyramid', band: 'When trust deteriorates, the visible traits weaken over time.', cols: [
    { icon: 'FaEye', title: 'The Five Traits', sub: 'What we see', points: ['The visible condition of organisational health'] },
    { icon: 'FaLayerGroup', title: 'The Pyramid', sub: 'How it develops', points: ['Trust, experiences, beliefs and actions beneath the results'] }], notes: N.s10 });

  // Section 2
  await d.section({ num: 2, name: 'Intelligence', anchor: 'Why', heading: 'Why Organisational Health Determines Execution Performance', outcomes: [
    'Determine how organisational health can be leveraged to strengthen strategy execution capability and sustain enterprise performance.',
    'Quantify the enterprise cost of poor organisational health to direct leadership attention to its performance implications.'], notes: N.s11 });
  await d.list({ title: '2.1 · Health as a performance multiplier', fontSize: 24, rows: [
    { icon: 'FaCompass', label: 'Strategic Direction', text: 'shared commitment strengthens alignment' },
    { icon: 'FaUserCheck', label: 'Execution Accountability', text: 'trust and ownership support delivery' },
    { icon: 'FaChartLine', label: 'Performance Management', text: 'openness enables corrective action' },
    { icon: 'FaUsers', label: 'Enterprise Collaboration', text: 'shared responsibility strengthens coordination' },
    { icon: 'FaSync', gold: true, label: 'Organisational Adaptability', text: 'confidence supports responsiveness' }], notes: N.s12 });
  await d.list({ title: '2.2 · Organisational health and execution velocity', fontSize: 24, rows: [
    { icon: 'FaBullhorn', text: 'Performance concerns are raised and addressed early.' },
    { icon: 'FaCheckDouble', text: 'Decisions and commitments are followed through.' },
    { icon: 'FaExchangeAlt', text: 'Information moves effectively across functions.' },
    { icon: 'FaPuzzlePiece', text: 'Teams coordinate contributions towards shared priorities.' },
    { icon: 'FaFire', gold: true, text: 'Employees remain engaged in delivering objectives.' }], notes: N.s13 });
  await d.list({ title: '2.3a · The price of poor organisational health', fontSize: 24, rows: [
    { icon: 'FaClock', label: 'Lost Time', text: 'reduced productivity and slower execution' },
    { icon: 'FaUserSlash', label: 'Employee Disengagement', text: 'lower contribution, weaker momentum' },
    { icon: 'FaUnlink', label: 'Declining Trust', text: 'reduced collaboration, slower resolution' },
    { icon: 'FaBed', label: 'Emotional Fatigue', text: 'reduced morale, commitment, effectiveness' },
    { icon: 'FaDoorOpen', gold: true, label: 'Talent Loss', text: 'lost knowledge, capability, continuity' }], notes: N.s14 });
  await tslide(d, '2.3b · How the hidden costs accumulate', [
    ['Hidden cost', 'Illustrative annual cost'],
    ['Lost Time', 'R644,000'], ['Employee Disengagement', 'R414,000'], ['Declining Trust', 'R172,800'],
    ['Emotional Fatigue', 'R100,000'], ['Talent Loss', 'R340,000']], N.s15,
    { t: { colW: [6.5, 5.63], rowH: 0.62 }, band: 'Small, recurring losses accumulate into a material annual cost.' });
  await d.list({ title: '2.4 · Health and sustained performance', fontSize: 24, rows: [
    { icon: 'FaRedo', text: 'Consistent execution of organisational priorities' },
    { icon: 'FaUserCheck', text: 'Constructive performance accountability' },
    { icon: 'FaUsers', text: 'Effective collaboration across functions' },
    { icon: 'FaHeart', text: 'Employee commitment and capability retention' },
    { icon: 'FaGraduationCap', gold: true, text: 'Organisational learning and continuous improvement' }], notes: N.s16 });
  await d.list({ title: '2.5 · Executive reflection', fontSize: 24, rows: [
    { icon: 'FaPlus', text: 'Where is organisational health strengthening execution performance?' },
    { icon: 'FaSearch', text: 'Which hidden costs of poor organisational health are most evident?' },
    { icon: 'FaCalculator', text: 'What is the estimated annual cost of the most significant loss?' },
    { icon: 'FaRoute', gold: true, text: 'Which leadership response would reduce it, and how would its financial impact be tracked?' }], notes: N.s17 });

  // Section 3
  await d.section({ num: 3, name: 'Extrapolating', anchor: 'Where', heading: 'Where Are the Organisational Health Signals?', outcomes: [
    'Diagnose people-performance vulnerabilities to establish how organisational culture shapes employee behaviour and contribution.',
    'Apply debiasing techniques to challenge functional assumptions and establish evidence-based assessments of organisational health.'], notes: N.s18 });
  await tslide(d, '3.1a · Health signals: strong and vulnerable', [
    ['Trait', 'Strong signal', 'Vulnerable signal'],
    ['Minimal Politics', 'Information is shared', 'Territorial behaviour'],
    ['Minimal Confusion', 'Expectations understood', 'Conflicting instructions'],
    ['High Morale', 'Initiative and confidence', 'Withdrawal'],
    ['High Productivity', 'Commitments fulfilled', 'Missed commitments'],
    ['Low Turnover', 'Capable people stay', 'Rising departures']], N.s19, { t: { colW: [3.6, 4.27, 4.26], rowH: 0.75 } });
  await d.cards({ title: '3.1b · Reading the Health Thermometer', cols: 3, items: [
    { icon: 'FaCheckCircle', title: 'Strong', text: 'Positive behaviours are consistently observed.' },
    { icon: 'FaAdjust', title: 'Vulnerable', text: 'Negative signals are emerging or uneven.' },
    { icon: 'FaExclamationTriangle', title: 'Poor', text: 'Negative signals are persistent or widespread.', dark: true }],
    band: 'Ratings must be supported by evidence.', notes: N.s20 });
  await d.list({ title: '3.2 · CXO functional bias in health diagnosis', fontSize: 24, rows: [
    { icon: 'FaUserTie', label: 'CEO', text: 'Test across levels · Examine employee experiences' },
    { icon: 'FaCoins', label: 'CFO', text: 'Separate effort from conditions · Examine retention quality' },
    { icon: 'FaUsers', label: 'CHRO', text: 'Test lived expectations · Triangulate · Challenge the assumption' },
    { icon: 'FaCogs', label: 'COO', text: 'Examine reinforced norms · Trace expectations and experiences' },
    { icon: 'FaChess', gold: true, label: 'CSO', text: 'Verify understanding' }], notes: N.s21 });
  await d.list({ title: '3.3 · Self-reflection: my health profile', fontSize: 24, rows: [
    { icon: 'FaPlus', text: 'Which trait do I strengthen through my everyday conduct?' },
    { icon: 'FaMinus', text: 'Which trait may my own habits or practices weaken?' },
    { icon: 'FaGlasses', text: 'What assumptions or functional biases do I bring?' },
    { icon: 'FaUserEdit', gold: true, text: 'What change in my behaviour would model our values more consistently?' }], notes: N.s22 });

  // Section 4
  await d.section({ num: 4, name: 'Integration', anchor: 'Collective', heading: 'Cross-CXO Health Architecture', outcomes: [
    'Establish a functional organisational health accountability discipline that enables executives to interpret team-generated health assessments and quantify associated people-performance losses.',
    'Embed cultural operating norms that leaders model, recognise and correct, so that organisational health strengthens across functions.'], notes: N.s23 });
  await d.compare({ title: '4.1 · Two levels of leadership accountability', cols: [
    { icon: 'FaUserTie', title: 'Functional', sub: 'The CXO', points: ['Interprets the team’s consolidated score', 'Investigates vulnerabilities', 'Quantifies evidenced losses'] },
    { icon: 'FaUsers', title: 'Enterprise', sub: 'EXCO', points: ['Consolidates functional results', 'Examines shared vulnerabilities', 'Agrees enterprise priorities'] }],
    band: 'Employees assess; the executive interprets and is accountable.', notes: N.s24 });
  await d.cards({ title: '4.2a · The Organisational Health Thermometer', cols: 3, items: [
    { icon: 'FaListOl', title: '20 statements', text: 'Four for each of the five traits' },
    { icon: 'FaSlidersH', title: 'Rated 1 to 5', text: 'Never, Rarely, Sometimes, Usually, Always' },
    { icon: 'FaThermometerHalf', title: 'Scored out of 100', text: 'Each trait out of 20', dark: true }],
    band: 'Employees rate independently and confidentially.', notes: N.s25 });
  await d.list({ title: '4.2b · Reading your temperature', fontSize: 26, rows: [
    { icon: 'FaCheckCircle', label: '80–100', text: 'Healthy & Thriving' },
    { icon: 'FaAdjust', label: '60–79', text: 'Stable but Uneven' },
    { icon: 'FaExclamationTriangle', label: '40–59', text: 'Caution Zone' },
    { icon: 'FaExclamationCircle', gold: true, label: '20–39', text: 'Unhealthy' }], notes: N.s26 });
  await d.stat({ title: '4.3 · From assessments to functional scores', big: '80 → 52', bigSize: 66, caption: 'Operations, Q1 to Q2: from Healthy & Thriving to the Caution Zone', rows: [
    { icon: 'FaHandshake', label: 'Minimal Politics', text: '16 → 8' },
    { icon: 'FaCompass', label: 'Minimal Confusion', text: '16 → 12' },
    { icon: 'FaSmile', label: 'High Morale', text: '16 → 8' },
    { icon: 'FaCogs', label: 'High Productivity', text: '16 → 12' },
    { icon: 'FaUserFriends', label: 'Low Turnover', text: '16 → 12' }], notes: N.s27 });
  await d.stat({ title: '4.4 · Quantifying the people-performance losses', big: 'R346,500', bigSize: 54, caption: 'Operations: illustrative gross exposure for one quarter', rows: [
    { icon: 'FaClock', label: 'Lost Time', text: 'R120,000' },
    { icon: 'FaUserSlash', label: 'Disengagement', text: 'R90,000' },
    { icon: 'FaUnlink', label: 'Declining Trust', text: 'R24,000' },
    { icon: 'FaBed', label: 'Emotional Fatigue', text: 'R22,500' },
    { icon: 'FaDoorOpen', label: 'Talent Loss', text: 'R90,000' }], notes: N.s28 });
  await tslide(d, '4.5 · Consolidating into an enterprise position', [
    ['Function', 'Q1', 'Q2', 'Change', 'Q2 exposure'],
    ['Corporate · CEO', '84', '82', '−2', 'R25,000'], ['Finance · CFO', '78', '72', '−6', 'R70,000'],
    ['HR · CHRO', '82', '80', '−2', 'R30,000'], ['Operations · COO', '80', '52', '−28', 'R346,500'],
    ['Strategy · CSO', '78', '70', '−8', 'R95,000'], ['Enterprise · EXCO', '79.8', '65.3', '−14.5', 'R566,500']], N.s29,
    { t: { colW: [4.1, 1.6, 1.6, 1.9, 2.93], rowH: 0.62 } });
  await d.list({ title: '4.6 · Sustaining the Cross-CXO Health Architecture', fontSize: 24, rows: [
    { icon: 'FaPaperPlane', label: 'Each quarter', text: 'employees in each function complete the thermometer' },
    { icon: 'FaLock', label: 'Confidential', text: 'responses are consolidated by function' },
    { icon: 'FaSearch', label: 'Each CXO', text: 'interprets, investigates and quantifies losses' },
    { icon: 'FaUsers', gold: true, label: 'EXCO', text: 'consolidates into enterprise health and priorities' }], notes: N.s30 });
  await d.list({ title: '4.7a · From values to a Cultural Operating Code', fontSize: 26, rows: [
    { icon: 'FaEye', label: '1 · Define the behaviour', text: 'what a leader who lives the value does' },
    { icon: 'FaFont', label: '2 · Build the acronym', text: 'three action words' },
    { icon: 'FaPenNib', gold: true, label: '3 · Write the norm statement', text: 'one sentence for daily practice' }], notes: N.s31 });
  await d.cards({ title: '4.7b · What makes the Code real', cols: 2, items: [
    { icon: 'FaEye', title: 'Demonstrable', text: 'Observable, specific behaviours' },
    { icon: 'FaClipboardCheck', title: 'Assessed', text: 'In 360-degree feedback' },
    { icon: 'FaGavel', title: 'Enforced', text: 'Consequences regardless of seniority' },
    { icon: 'FaSync', title: 'Maintained', text: 'Modelled, reinforced, revisited', dark: true }], titleBeside: true, textSize: 24, iconSize: 0.6, notes: N.s32 });
  await d.cards({ title: '4.7c · Three tests for every norm', cols: 3, items: [
    { icon: 'FaUserPlus', title: 'New Employee Test', text: 'Is the behaviour clear on day one?' },
    { icon: 'FaCompressArrowsAlt', title: 'Pressure Test', text: 'Does it hold under pressure?' },
    { icon: 'FaUserCircle', title: 'Mirror Test', text: 'Would every executive accept it in their own 360?', dark: true }], notes: N.s33 });
  await tslide(d, '4.7d · The IBSL Cultural Operating Code (1)', [
    ['Value', 'Code', 'The three actions'],
    ['Intentionality', 'AIM', 'Act with purpose · Interrogate assumptions · Maintain the discipline'],
    ['Integrity', 'SAY', 'Say what you mean · Act on what you say · Yield the truth regardless of consequence'],
    ['Collaboration', 'ONE', 'Own a shared outcome · Navigate difference with respect · Execute as a unified force']], N.s34, { t: { colW: [2.75, 1.1, 8.28], rowH: 0.9 }, band: 'AIM · SAY · ONE · OAR · SET · SEE' });
  await tslide(d, '4.7e · The IBSL Cultural Operating Code (2)', [
    ['Value', 'Code', 'The three actions'],
    ['Accountability', 'OAR', 'Own it · Act on it · Report it'],
    ['Excellence', 'SET', 'Set the standard · Earn the evidence · Transform through learning'],
    ['Human-Centricity', 'SEE', 'See the person behind the role · Enable growth deliberately · Ensure dignity in every interaction']], N.s34b, { t: { colW: [2.75, 1.1, 8.28], rowH: 0.9 }, band: 'AIM · SAY · ONE · OAR · SET · SEE' });
  await d.list({ title: 'Section 4 Reflection', fontSize: 24, rows: [
    { icon: 'FaThermometerHalf', text: 'Which trait would my employees rate lowest, and what evidence do I see?' },
    { icon: 'FaCoins', text: 'Which hidden cost is that vulnerability most likely creating?' },
    { icon: 'FaCalculator', text: 'What is the estimated quarterly loss exposure, and how did I calculate it?' },
    { icon: 'FaBalanceScale', text: 'Which part is observed loss, which is assumption, and where could it overlap?' },
    { icon: 'FaRoute', gold: true, text: 'What action will I take, and how will I track the value recovered?' }], notes: N.s35 });

  // Section 5
  await d.section({ num: 5, name: 'Application', anchor: 'In Practice', heading: 'The Cross-CXO Organisational Health Clinic', outcomes: [
    'Consolidate functional organisational health assessments and quantify enterprise-level people-performance losses to establish an evidence-based organisational health position.',
    'Commit the executive team to coordinated remedial actions and shared behavioural norms that restore people performance and strengthen organisational health.'], notes: N.s36 });
  await d.list({ title: '5.1 · The Clinic: four pieces of group work', fontSize: 24, rows: [
    { icon: 'FaSearch', label: 'Interpret', text: 'the functional assessments of your CXO roles' },
    { icon: 'FaLayerGroup', label: 'Consolidate', text: 'scores and losses for the represented functions' },
    { icon: 'FaSync', label: 'Review–Realign–Restore', text: 'determine the remedial actions' },
    { icon: 'FaCode', gold: true, label: 'Build', text: 'your organisation’s Cultural Operating Code' }], notes: N.s37 });
  await d.compare({ title: '5.2–5.3 · Tasks 1 and 2: each function', cols: [
    { icon: 'FaThermometerHalf', title: 'Task 1', sub: 'Functional health position', points: ['Score and classification', 'Two weakest traits', 'Evidence to investigate'] },
    { icon: 'FaCoins', title: 'Task 2', sub: 'The functional losses', points: ['Largest hidden cost', 'Links to the weakest traits', 'Overlaps and double counting'] }], notes: N.s38 });
  await d.compare({ title: '5.4–5.5 · Tasks 3 to 6: the group position', cols: [
    { icon: 'FaCalculator', title: 'Tasks 3 and 4', sub: 'Consolidated health score', points: ['Weighted by valid responses', 'Classification and weakest traits', 'Functions contributing most'] },
    { icon: 'FaCoins', title: 'Tasks 5 and 6', sub: 'Gross quarterly exposure', points: ['Sum for represented roles only', 'Two largest cost categories', 'Estimates to verify'] }], notes: N.s39 });
  await d.cards({ title: '5.6 · Review–Realign–Restore', cols: 3, items: [
    { icon: 'FaSearch', title: 'Review', text: 'A prioritised organisational health diagnosis' },
    { icon: 'FaSync', title: 'Realign', text: 'Cultural reinforcement actions with named accountability' },
    { icon: 'FaChartLine', title: 'Restore', text: 'Measurable health and performance commitments', dark: true }], notes: N.s40 });
  await d.list({ title: '5.7 · Task 7: the Organisational Health Response', fontSize: 24, rows: [
    { icon: 'FaArrowDown', label: 'Priority trait', text: 'the lowest-scoring health trait' },
    { icon: 'FaSync', label: 'Action', text: 'from Review–Realign–Restore' },
    { icon: 'FaUserTie', label: 'Accountable CXO(s)', text: 'named executive ownership' },
    { icon: 'FaBullseye', label: 'Health target', text: 'the improvement expected' },
    { icon: 'FaCoins', gold: true, label: 'Financial target', text: 'current → target (reduction)' }], notes: N.s41 });
  await d.list({ title: '5.8 · Task 8: build your Cultural Operating Code', fontSize: 26, rows: [
    { icon: 'FaListUl', label: 'Step 1', text: 'list your organisation’s values' },
    { icon: 'FaExchangeAlt', label: 'Step 2', text: 'translate at least three into norms' },
    { icon: 'FaCheckDouble', gold: true, label: 'Step 3', text: 'test your strongest norm' }], notes: N.s42 });
  await d.list({ title: '5.9 · Capstone assessment output', fontSize: 24, rows: [
    { icon: 'FaThermometerHalf', label: '11A', text: 'Functional health assessments' },
    { icon: 'FaLayerGroup', label: '11B', text: 'Consolidated health position' },
    { icon: 'FaSync', label: '11C', text: 'Review–Realign–Restore' },
    { icon: 'FaFileAlt', label: '11D', text: 'Organisational Health Response' },
    { icon: 'FaCode', gold: true, label: '11E', text: 'Cultural Operating Code' }], notes: N.s43 });
  await d.prompt({ icon: 'FaRedo', label: 'Closing · Transition to Unit 12', text: 'Read health from evidence, price what poor health costs, act on the lowest-scoring conditions and model the norms of your Code.',
    foot: 'Unit 12 brings ESRG alignment and organisational health together to sustain performance.', notes: N.s44 });
  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
