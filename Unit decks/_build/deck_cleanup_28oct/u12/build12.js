// Unit 12 · Sustaining Performance — facilitator deck, rebuilt from the live unit pages (28 Oct 2026).
// Run: node build12.js "<out.pptx>" <logo.png>
const { Deck, C, F, T, box, badge } = require('./lib2');
const N = require('./notes12');
const [OUT, LOGO = 'logo.png'] = process.argv.slice(2);

// Estimated lines of text in a cell (conservative, Calibri 24pt).
const lines = (t, w, fs) => String(t).split('\n').reduce((a, p) => a + Math.max(1, Math.ceil(p.length / ((w * 72) / (fs * 0.47)))), 0);

// Grid table: cols [{w, head}], rows [[cells]], first column bold label.
async function table(d, o) {
  const s = d.slide(); d.title(s, o.title);
  const fs = o.fs || 24, pad = 0.09, lh = fs * 1.17 / 72, gap = 0.06;
  let y = o.top || 1.6;
  if (o.band0) { box(s, 0.6, y, 12.13, o.band0h || 0.9, C.deep); T(s, o.band0, { x: 0.85, y, w: 11.7, h: o.band0h || 0.9, fontSize: 24, color: C.white, valign: 'middle' }); y += (o.band0h || 0.9) + 0.15; }
  // header
  let x = 0.6; const hh = Math.max(...o.cols.map(c => lines(c.head, c.w - 2 * pad, fs))) * lh + 2 * pad;
  if (!o.noHead) { for (const c of o.cols) { box(s, x, y, c.w - gap, hh, C.forest); T(s, c.head, { x: x + pad, y, w: c.w - gap - 2 * pad, h: hh, fontSize: fs, bold: true, fontFace: F.head, color: C.white, valign: 'middle' }); x += c.w; }
  y += hh + gap; }
  for (const r of o.rows) {
    const span = r.length === 2 && o.cols.length > 2; // label + one merged cell
    const ws = span ? [o.cols[0].w, o.cols.slice(1).reduce((a, c) => a + c.w, 0)] : o.cols.map(c => c.w);
    const rh = Math.max(...r.map((t, i) => lines(t, ws[i] - 2 * pad, fs))) * lh + 2 * pad;
    x = 0.6;
    r.forEach((t, i) => {
      box(s, x, y, ws[i] - gap, rh, i === 0 ? C.goldLight : C.tint);
      T(s, t, { x: x + pad, y, w: ws[i] - gap - 2 * pad, h: rh, fontSize: fs, bold: i === 0, fontFace: i === 0 ? F.head : F.body, color: i === 0 ? C.deep : C.ink, valign: 'middle' });
      x += ws[i];
    });
    y += rh + gap;
  }
  if (o.band) { const bh = 0.85; box(s, 0.6, 7.0 - bh, 12.13, bh, C.deep); T(s, o.band, { x: 0.9, y: 7.0 - bh, w: 11.6, h: bh, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); if (y > 7.0 - bh) console.warn('TABLE OVER BAND', o.title, y.toFixed(2)); }
  else if (y > 7.15) console.warn('TABLE OVERFLOW', o.title, y.toFixed(2));
  else console.log('table', o.title, 'ends at', y.toFixed(2));
  s.addNotes(o.notes);
}

async function reflection(d, o) {
  const s = d.slide(true);
  await badge(s, 'FaPenFancy', 0.8, 1.0, 1.1, C.gold, C.deep);
  T(s, o.label, { x: 2.2, y: 1.0, w: 10.4, h: 0.6, fontSize: 32, bold: true, fontFace: F.head, color: C.white });
  T(s, o.part, { x: 2.2, y: 1.6, w: 10.4, h: 0.5, fontSize: 24, bold: true, color: C.gold });
  if (o.text) T(s, o.text, { x: 2.2, y: 2.4, w: 10.4, h: 3.6, fontSize: 34, fontFace: F.head, italic: true, color: C.white });
  if (o.fields) {
    let y = 2.45;
    for (const f of o.fields) { await badge(s, 'FaArrowRight', 2.2, y + 0.1, 0.45, C.gold, C.deep); T(s, f, { x: 2.85, y, w: 9.8, h: 0.75, fontSize: 30, fontFace: F.head, italic: true, color: C.white, valign: 'middle' }); y += 0.95; }
  }
  T(s, 'Personal reflection · Learning Portfolio', { x: 2.2, y: 6.3, w: 10.4, h: 0.5, fontSize: 24, color: C.paleText });
  s.addNotes(o.notes);
}

async function pageDiagram(d) {
  const s = d.slide(); d.title(s, '4.1 · The Quarterly Three Lines of Sight page');
  box(s, 0.6, 1.6, 12.13, 0.7, C.deep);
  T(s, [{ text: 'Header  ', options: { bold: true, color: C.gold } }, { text: 'Enterprise Key Result · Quarter · Decider', options: { color: C.white } }], { x: 0.9, y: 1.6, w: 11.6, h: 0.7, fontSize: 26, valign: 'middle' });
  const L = [['Strategic line', 'Key Result and WARD', 'FaBullseye'], ['Operational line', 'ESRG scan', 'FaCogs'], ['Behavioural line', 'Health Thermometer', 'FaHeartbeat']];
  for (let i = 0; i < 3; i++) {
    const x = 0.6 + i * 4.11, w = 3.91;
    box(s, x, 2.45, w, 1.45, C.forest);
    await badge(s, L[i][2], x + 0.2, 2.6, 0.6, C.gold, C.deep);
    T(s, L[i][0], { x: x + 0.95, y: 2.55, w: w - 1.1, h: 0.6, fontSize: 26, bold: true, fontFace: F.head, color: C.white, valign: 'middle' });
    T(s, L[i][1], { x: x + 0.2, y: 3.15, w: w - 0.35, h: 0.7, fontSize: 24, color: C.paleText, valign: 'top' });
  }
  box(s, 0.6, 4.05, 12.13, 1.6, C.tint);
  T(s, 'On each line', { x: 0.9, y: 4.12, w: 4, h: 0.5, fontSize: 24, bold: true, fontFace: F.head, color: C.forest });
  T(s, 'Result this quarter · Waypoint · Alert', { x: 0.9, y: 4.62, w: 11.6, h: 0.45, fontSize: 24 });
  T(s, 'Alert raised · Recovery and owner · Decider checks', { x: 0.9, y: 5.1, w: 11.6, h: 0.45, fontSize: 24 });
  box(s, 0.6, 5.8, 12.13, 1.2, C.deep);
  T(s, [{ text: 'KISS for next quarter  ', options: { bold: true, color: C.gold, breakLine: true } }, { text: 'Keep · Improve · Stop · Start, each with its practice, line of sight and owner', options: { color: C.white } }], { x: 0.9, y: 5.85, w: 11.6, h: 1.1, fontSize: 24, valign: 'middle' });
  s.addNotes(N.p41);
}

(async () => {
  const d = new Deck({ unit: 12, module: 4, moduleName: 'Grounding', title: 'Sustaining Performance' });

  await d.cover({ logo: LOGO, subtitle: 'Holding results once they are achieved: the Three Lines of Sight and KISS', notes: N.cover });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: [
    'Distinguish short-term performance attainment from sustained institutional capability.',
    'Maintain continuous sight of strategic, operational and behavioural performance across the enterprise’s contributions.',
    'Recognise the sources of performance drift and the early erosion of strategic coherence.',
    'Exercise forward-looking executive judgement that protects organisational value and long-term performance.'].map(t => ({ icon: 'FaCheck', text: t })), notes: N.klo });
  await d.list({ title: 'The unit journey', fontSize: 24, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness — What', text: 'the three lines of sight · what KISS means' },
    { icon: 'FaLightbulb', label: 'Section 2 · Intelligence — Why', text: 'why performance drifts · why KISS holds it' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating — Where', text: 'where drift shows first · where each KISS decision sits' },
    { icon: 'FaUsers', label: 'Section 4 · Integration — Collective', text: 'the leadership team completes the quarterly page' },
    { icon: 'FaClipboardCheck', gold: true, label: 'Section 5 · Application — In Practice', text: 'your group completes the page for its Capstone organisation' }], notes: N.journey });

  // ── Section 1
  await d.section({ num: 1, name: 'Awareness', anchor: 'What', heading: 'What Sustains Performance', outcomes: [
    'Recognise the force that pulls achieved results back towards average.',
    'Identify the leadership decisions that hold performance against that pull.'], notes: N.s1 });
  await d.prompt({ icon: 'FaArrowDown', label: '1.1 · Performance Gravity', text: 'Achieving a result and holding it are two separate leadership tasks.',
    foot: 'Performance Gravity: the steady pull of achieved results back towards the historical average.', notes: N.p11 });
  await d.cards({ title: '1.2 · The Three Lines of Sight', cols: 3, items: [
    { icon: 'FaBullseye', title: 'Strategic', text: 'Is the Key Result still moving towards its Success in Practice?\n\nReads: the Key Result against its WARD waypoint (Unit 6)' },
    { icon: 'FaCogs', title: 'Operational', text: 'Are the conditions still enabling the people’s tasks?\n\nReads: the ESRG scan (Unit 10)' },
    { icon: 'FaHeartbeat', title: 'Behavioural', dark: true, text: 'Are people still delivering the agreed behaviours?\n\nReads: the Health Thermometer (Unit 11)' }], notes: N.p12a });
  await table(d, { title: '1.2 · Filtering each line through WARD', cols: [{ w: 2.2, head: 'WARD' }, { w: 3.31, head: 'Strategic' }, { w: 3.31, head: 'Operational' }, { w: 3.31, head: 'Behavioural' }], rows: [
    ['W · Waypoint', 'The Key Result level for this quarter', 'Each capability Aligned (4.0–5.0)', 'Health 80–100, Healthy & Thriving'],
    ['A · Alert', 'More than the agreed margin below', 'A capability below 3.0', 'Health below 60'],
    ['R · Recovery', 'For individuals and conditions', 'The condition’s owner restores it', 'The executive restores the weakest traits'],
    ['D · Decider', 'The same Decider on all three lines: decides on the recovery and sees it through']], notes: N.p12b });
  await d.cards({ title: '1.3 · KISS: the four sustaining decisions', cols: 4, iconSize: 0.6, items: [
    { icon: 'FaShieldAlt', title: 'Keep', text: 'Name and protect what produces reliable results' },
    { icon: 'FaSlidersH', title: 'Improve', text: 'Recalibrate what is beginning to work less well' },
    { icon: 'FaStopCircle', title: 'Stop', text: 'End what consumes energy without commensurate value' },
    { icon: 'FaPlayCircle', title: 'Start', dark: true, text: 'Build what the next level of performance needs' }],
    band: 'Four decisions at the close of every quarter.', notes: N.p13 });
  await reflection(d, { label: 'Section 1 Reflections', part: '1.2 · The Three Lines of Sight', text: 'Which of the three lines of sight does your leadership team read least, and what has that cost your organisation?', notes: N.r1 });

  // ── Section 2
  await d.section({ num: 2, name: 'Intelligence', anchor: 'Why', heading: 'Why Performance Drifts, and Why KISS Holds It', outcomes: [
    'Explain why achieved performance drifts back towards average across strategy, operations and behaviour.',
    'Counter drift before it reaches the enterprise result.'], notes: N.s2 });
  await d.cards({ title: '2.1 · Why performance drifts', cols: 3, items: [
    { icon: 'FaForward', title: 'Momentum Illusion', text: 'Strategic line\nThe market moves on; momentum carries the results for a while.' },
    { icon: 'FaLayerGroup', title: 'Complexity Creep', text: 'Operational line\nEach sensible response adds weight; together they slow delivery.' },
    { icon: 'FaUndo', title: 'Execution Regression', dark: true, text: 'Behavioural line\nOld habits pull behaviour back once attention moves.' }],
    band: 'The routines that detect drift are the first to loosen.', notes: N.p21 });
  await table(d, { title: '2.2 · Why KISS holds performance', cols: [{ w: 2.5, head: 'Line of sight' }, { w: 3.1, head: 'Drift' }, { w: 6.53, head: 'KISS decisions that counter it' }], rows: [
    ['Strategic', 'Momentum Illusion', 'Keep what still earns the result · Start what the moved market requires'],
    ['Operational', 'Complexity Creep', 'Stop outdated structures · Improve conditions that constrain delivery'],
    ['Behavioural', 'Execution Regression', 'Keep the agreed behaviours protected · Improve behaviours that slip']],
    band: 'Each KISS decision answers a specific form of drift.', notes: N.p22 });
  await reflection(d, { label: 'Section 2 Reflections', part: '2.2 · Why KISS Holds Performance', text: 'Name one practice in your organisation that is drifting on one of the three lines. Which KISS decision would hold it, and who would need to make that decision?', notes: N.r2 });

  // ── Section 3
  await d.section({ num: 3, name: 'Extrapolating', anchor: 'Where', heading: 'Where Drift Shows First, and Where Each KISS Decision Sits', outcomes: [
    'Locate where drift appears first in each executive domain.',
    'Assign executive ownership for holding performance in each domain.'], notes: N.s3 });
  await d.cards({ title: '3.1a · The line each role reads first', cols: 3, items: [
    { icon: 'FaBullseye', title: 'Strategic', text: 'CEO · CMO · CRO\n\nAlso: CCO and CSO' },
    { icon: 'FaCogs', title: 'Operational', text: 'CFO · CTO / CIO · CPO\n\nAlso: COO and CSO' },
    { icon: 'FaHeartbeat', title: 'Behavioural', dark: true, text: 'CHRO\n\nAlso: COO, CCO and CSO' }],
    band: 'Drift surfaces first in the executive domain closest to it.', notes: N.p31a });
  const kc = [{ w: 3.7, head: 'Role' }, { w: 8.43, head: 'KISS decision it usually leads' }];
  await table(d, { title: '3.1b · The KISS decision each role leads', noHead: true, cols: kc, rows: [
    ['CEO · Strategic Coherence', 'Keep the strategic priorities clear · Stop initiatives that compete with them'],
    ['CFO · Capital Discipline', 'Stop legacy spending · Start funding for the strategic initiatives'],
    ['COO · Execution Cadence', 'Keep the review rhythm · Improve escalation discipline'],
    ['CHRO · Organisational Health', 'Keep the agreed behaviours · Improve how they are recognised and reinforced'],
    ['CTO / CIO · Technology', 'Improve the systems that constrain delivery · Start capability the strategy will need']], notes: N.p31b });
  await table(d, { title: '3.1c · The KISS decision each role leads', noHead: true, cols: kc, rows: [
    ['CMO · Market Intelligence', 'Start renewed customer intelligence · Stop campaigns built on the old customer view'],
    ['CCO · Revenue Conversion', 'Improve conversion practices · Keep commercial discipline'],
    ['CPO · Supply Resilience', 'Improve supplier arrangements · Stop cost-only sourcing decisions'],
    ['CRO · Risk Intelligence', 'Start risk input into strategic decisions · Improve risk reporting'],
    ['CSO · Strategy Translation', 'Keep the line from strategy to OKRs · Improve how the three lines are read in reviews']], notes: N.p31c });
  await reflection(d, { label: 'Section 3 Reflections', part: '3.1 · Your role', fields: ['My role', 'The line of sight I read first', 'The drift signal present in my organisation today', 'The KISS decision I would lead'], notes: N.r3 });

  // ── Section 4
  await d.section({ num: 4, name: 'Integration', anchor: 'Collective', heading: 'The Quarterly Three Lines of Sight', outcomes: [
    'Establish a collective leadership rhythm that sustains performance across every contribution.',
    'Coordinate the enterprise response to drift before it reaches the result.'], notes: N.s4 });
  await pageDiagram(d);
  const lc = [{ w: 2.6, head: 'Quarter 2' }, { w: 3.17, head: 'Strategic' }, { w: 3.18, head: 'Operational' }, { w: 3.18, head: 'Behavioural' }];
  await table(d, { title: '4.2a · Worked example: results against WARD', band0: 'Enquiries resolved within 48 hours: 65% to 90% by year-end · Quarter 2', band0h: 0.6, cols: [{ w: 2.6, head: 'WARD' }].concat(lc.slice(1)), rows: [
    ['Result this quarter', '74% within 48 hours', 'Readiness 4.3\nFlow 2.0\nCapacity 4.0\nResponsiveness 3.7', '52/100 (Q1: 80)\nPolitics 8 · Morale 8'],
    ['W · Waypoint', '80% by end of June', 'Each capability 4.0 or above', '80/100 or above'],
    ['A · Alert', 'More than 3 points below', 'Any capability below 3.0', 'Below 60/100']], notes: N.p42a });
  await table(d, { title: '4.2b · Worked example: alerts and recoveries', cols: lc, rows: [
    ['Alert raised', 'Yes · six points below', 'Yes · Flow at 2.0', 'Yes · Caution Zone'],
    ['R · Recovery', 'Team leaders review open enquiries with each owner every morning', 'IT restores system availability; Customer Service and Operations examine Flow', 'The COO strengthens collaboration, trust and commitment'],
    ['D · Decider checks', 'End of July', 'End of July', 'Quarter 3 thermometer']],
    notes: N.p42b });
  const kq = [{ w: 1.9, head: 'Decision' }, { w: 5.5, head: 'Practice' }, { w: 2.1, head: 'Line' }, { w: 2.63, head: 'Owner' }];
  await table(d, { title: '4.2c · KISS for Quarter 3: Keep and Improve', cols: kq, rows: [
    ['Keep', 'Morning review of open enquiries with each owner', 'Behavioural', 'Team leaders'],
    ['Keep', 'Conditions behind Readiness (4.3) and Capacity (4.0)', 'Operational', 'IT and Operations'],
    ['Improve', 'Cross-functional handoffs: 40% of delays need another department', 'Operational', 'Customer Service with Operations'],
    ['Improve', 'Collaboration and morale in Operations', 'Behavioural', 'COO']], notes: N.p42c });
  await table(d, { title: '4.2d · KISS for Quarter 3: Stop and Start', cols: kq, rows: [
    ['Stop', 'Senior-management approval of routine refunds', 'Operational', 'Operations'],
    ['Stop', 'Scorecards counting enquiries processed in place of resolved', 'Behavioural', 'Customer Service Executive'],
    ['Start', 'Case tracking after escalation, through to resolution', 'Strategic', 'IT with Customer Service']],
    band: 'Each decision names its practice, its line of sight and its owner.', notes: N.p42d });

  // ── Section 5
  await d.section({ num: 5, name: 'Application', anchor: 'In Practice', heading: 'Our Quarterly Three Lines of Sight', outcomes: [
    'Exercise forward-looking judgement that holds performance gains across people and organisation.',
    'Design a leadership rhythm that sustains the enterprise result quarter after quarter.'], notes: N.s5 });
  await d.cards({ title: '5.1 · Brought into your page', cols: 3, items: [
    { icon: 'FaBullseye', title: 'Unit 6', text: 'The enterprise Key Result and its WARD' },
    { icon: 'FaCogs', title: 'Unit 10 · 10A', text: 'The ESRG scan' },
    { icon: 'FaHeartbeat', title: 'Unit 11 · 11B', dark: true, text: 'The consolidated health position' }],
    band: 'Your reference: the worked example in 4.2.', notes: N.p51 });
  await d.list({ title: '5.2 to 5.4 · Your page, in order', fontSize: 24, rows: [
    { icon: 'FaDownload', label: '5.2 · Your results for the quarter', text: 'brought in; the scribe chooses the quarter and corrects any changed value' },
    { icon: 'FaStream', label: '5.3 · The three lines of sight', text: 'each line filtered through WARD, with its recovery, owner and check' },
    { icon: 'FaTasks', gold: true, label: '5.4 · KISS for next quarter', text: 'at least one Keep, one Improve, one Stop and one Start' }], notes: N.p52 });
  await d.cards({ title: '5.5 · Capstone output', cols: 4, iconSize: 0.6, items: [
    { icon: 'FaBullseye', title: '12A', text: 'Strategic line' },
    { icon: 'FaCogs', title: '12B', text: 'Operational line' },
    { icon: 'FaHeartbeat', title: '12C', text: 'Behavioural line' },
    { icon: 'FaTasks', title: '12D', dark: true, text: 'KISS for next quarter' }],
    band: 'Once every member agrees, the page goes into your Capstone S2R® Blueprint.', notes: N.p55 });

  await d.list({ title: 'Unit Summary · S2R® programme close', fontSize: 24, rows: [
    { icon: 'FaArrowDown', text: 'Achieved results come under Performance Gravity, a pull back towards average.' },
    { icon: 'FaEye', text: 'The pull shows first on one of three lines: strategic, operational or behavioural.' },
    { icon: 'FaFilter', text: 'Each line reads a result you already produce. WARD filters all three.' },
    { icon: 'FaRandom', text: 'Each line drifts through its own mechanism. KISS answers each one.' },
    { icon: 'FaCalendarCheck', gold: true, text: 'Each quarter, one page brings the three lines together and closes with KISS.' }], notes: N.summary });

  await d.save(OUT);
  console.log('saved', OUT);
})().catch(e => { console.error(e); process.exit(1); });
