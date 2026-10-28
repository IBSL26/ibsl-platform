// Unit 10 · ESRG Alignment — facilitator deck rebuilt from the live unit pages (deck clean-up, 28 Oct 2026).
// Run from this folder: node build_u10.js "<out.pptx>" <logo.png>
// Then: python3 bold_notes.py "<out.pptx>"  (turns § headings, step titles and Say:/Ask: labels bold)
const path = require('path');
const { Deck, C, F, T, box, badge } = require(path.join(__dirname, '..', '..', 'lib2'));
const A = require('./notes_u10a'), B = require('./notes_u10b');
const [OUT = 'u10.pptx', LOGO = path.join(__dirname, '..', '..', '..', '..', 'logo.png')] = process.argv.slice(2);

async function table(d, o) {
  const s = d.slide(); d.title(s, o.title);
  const rows = [o.head.map((h, i) => ({ text: h, options: { bold: true, color: C.white, fill: { color: C.forest }, fontFace: i ? F.body : F.head, align: i ? 'center' : 'left' } }))]
    .concat(o.rows.map(r => r.map((c, i) => ({ text: c, options: { color: C.ink, fill: { color: i === 0 ? C.tint : (r.low && r.low.includes(i) ? 'F5E6C4' : C.white) }, bold: i === 0, align: i ? 'center' : 'left' } }))));
  s.addTable(rows, { x: 0.6, y: o.y || 1.6, w: 12.13, colW: o.colW, rowH: o.rowH, fontSize: 24, fontFace: F.body, border: { type: 'solid', color: C.line, pt: 1 }, valign: 'middle', margin: 0.05 });
  if (o.band) { box(s, 0.6, 6.25, 12.13, 0.8, C.deep); T(s, o.band, { x: 0.9, y: 6.25, w: 11.6, h: 0.8, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); }
  s.addNotes(o.notes);
}

(async () => {
  const d = new Deck({ unit: 10, module: 4, moduleName: 'Grounding', title: 'ESRG Alignment' });

  await d.cover({ logo: LOGO, subtitle: 'Can our operating conditions carry this commitment, and where must we build capability?', notes: A.cover });
  await d.list({ title: 'Key learning outcomes', fontSize: 26, rows: [
    { icon: 'FaDraftingCompass', text: 'Design an ESRG-aligned organisational operating environment by establishing the Environment, Systems, Resources and Governance requirements necessary to deliver strategic commitments.' },
    { icon: 'FaTools', gold: true, text: 'Develop targeted organisational alignment interventions that address operating constraints and strengthen the organisation’s capacity for consistent strategic delivery.' }], notes: A.klo });
  await d.list({ title: 'The unit journey', fontSize: 24, rows: [
    { icon: 'FaEye', label: '1 · Awareness — What', text: 'the capability one commitment requires' },
    { icon: 'FaLightbulb', label: '2 · Intelligence — Why', text: 'four enabling capabilities and the scanner' },
    { icon: 'FaMapMarkedAlt', label: '3 · Extrapolating — Where', text: 'executive biases that distort ESRG' },
    { icon: 'FaUsers', label: '4 · Integration — Collective', text: 'one executive view across functions' },
    { icon: 'FaClipboardCheck', gold: true, label: '5 · Application — In Practice', text: 'the Enterprise ESRG Alignment Clinic' }], notes: A.journey });

  // ── Section 1
  await d.section({ num: 1, name: 'Awareness', anchor: 'What', heading: 'What operating conditions must support strategic delivery?', outcomes: [
    'Specify the essential organisational operating requirements associated with a selected strategic commitment.',
    'Assign each requirement to the appropriate ESRG domain and component, explaining its direct contribution to the intended result.'], notes: A.s1 });
  await d.prompt({ icon: 'FaMountain', label: 'The Grounding question', text: 'What must be in place within the organisation for this result to be delivered?',
    foot: 'Environment · FIT   Systems · SIP   Resources · AIR   Governance · PAR', notes: A.grounding });
  await d.compare({ title: 'ESRG Alignment and Strategic Unclogging', cols: [
    { icon: 'FaFilter', title: 'Strategic Unclogging', sub: 'Unit 9 · clears a clog', points: ['A Key Result is slowing', 'What is blocking this result?', 'People and organisational performance', 'Unclogging Lever · Review–Realign–Restore'] },
    { icon: 'FaLayerGroup', title: 'ESRG Alignment', sub: 'Unit 10 · builds capability', points: ['A commitment is approved, launched or scaled', 'Can our conditions carry it?', 'Organisational operating conditions', 'Coordinate · Reconcile · Align'] }],
    band: 'Clogs point to components to strengthen; low scores show where clogs will form.', notes: A.unclog });
  const dom = (title, items, band, notes) => d.cards({ title, cols: 3, titleSize: 28, items, band, notes });
  await dom('1.1 · Environment | FIT', [
    { icon: 'FaBuilding', title: 'Facilities', text: 'Functional and suited to the planned activity' },
    { icon: 'FaPlug', title: 'Infrastructure', text: 'Utilities and connectivity carry the demand' },
    { icon: 'FaLaptop', title: 'Technology', text: 'Available, reliable and fit for the activity', dark: true }],
    'Are our facilities, infrastructure and technology fit for the strategic requirement?', A.fit);
  await dom('1.2 · Systems | SIP', [
    { icon: 'FaListOl', title: 'Standardisation', text: 'Processes clearly defined and consistently applied' },
    { icon: 'FaLink', title: 'Integration', text: 'Handoffs connect across functions without breaks' },
    { icon: 'FaStream', title: 'Process Efficiency', text: 'Output without unneeded steps, delay or waste', dark: true }],
    'Are our operational processes standardised, integrated and efficient?', A.sip);
  await dom('1.3 · Resources | AIR', [
    { icon: 'FaTruck', title: 'Asset Availability', text: 'Enough productive assets for the output' },
    { icon: 'FaCoins', title: 'Investment', text: 'Financial provision adequate for the commitment' },
    { icon: 'FaBalanceScale', title: 'Resource Utilisation', text: 'Assets and funding used productively', dark: true }],
    'Are our assets and financial resources sufficient and effectively utilised?', A.air);
  await dom('1.4 · Governance | PAR', [
    { icon: 'FaBook', title: 'Policies & Procedures', text: 'Established and suitable for the decisions' },
    { icon: 'FaStamp', title: 'Authority', text: 'Decision rights and approvals support timely decisions' },
    { icon: 'FaShieldAlt', title: 'Risk Management', text: 'Material risks assessed, mitigated, monitored', dark: true }],
    'Is our organisational governance up to PAR?', A.par);

  // ── Section 2
  await d.section({ num: 2, name: 'Intelligence', anchor: 'Why', heading: 'The ESRG Ignition Point: how each domain enables execution', outcomes: [
    'Translate strategic performance requirements into functional operating capabilities through the four ESRG execution enablers.',
    'Build and maintain an evidence-based functional ESRG performance profile to identify operating strengths, constraints and changes in alignment over time.'], notes: A.s2 });
  await d.cards({ title: '2.1 · The ESRG Ignition Point', cols: 2, titleBeside: true, titleSize: 26, iconSize: 0.6, items: [
    { icon: 'FaBuilding', title: 'Operational Readiness', text: 'Environment · FIT: a dependable operating setting' },
    { icon: 'FaStream', title: 'Operational Flow', text: 'Systems · SIP: work flows predictably to completion' },
    { icon: 'FaCoins', title: 'Delivery Capacity', text: 'Resources · AIR: the required scale of delivery' },
    { icon: 'FaGavel', title: 'Decision Responsiveness', text: 'Governance · PAR: action with clarity and control', dark: true }],
    band: 'Conditions must meet the demands of the commitment they carry.', notes: A.ignition });
  await d.list({ title: '2.2a · The scanner’s scoring guide', fontSize: 24, rows: [
    { icon: 'FaTimesCircle', label: '1 · Critical constraint', text: 'materially prevents required performance' },
    { icon: 'FaExclamationTriangle', label: '2 · Significant gap', text: 'regularly disrupts or limits performance' },
    { icon: 'FaAdjust', label: '3 · Partially effective', text: 'basic operations, not strategic demand' },
    { icon: 'FaCheck', label: '4 · Effective', text: 'reliably supports current requirements' },
    { icon: 'FaCheckDouble', gold: true, label: '5 · Fully aligned', text: 'also meets anticipated strategic demand' }], notes: A.scale });
  await d.list({ title: '2.2b · Twelve components, one scale', fontSize: 24, rows: [
    { icon: 'FaBuilding', label: 'FIT · Operational Readiness', text: 'Facilities · Infrastructure · Technology' },
    { icon: 'FaStream', label: 'SIP · Operational Flow', text: 'Standardisation · Integration · Process Efficiency' },
    { icon: 'FaCoins', label: 'AIR · Delivery Capacity', text: 'Asset Availability · Investment · Resource Utilisation' },
    { icon: 'FaGavel', label: 'PAR · Decision Responsiveness', text: 'Policies & Procedures · Authority · Risk Management' },
    { icon: 'FaCalendarAlt', gold: true, label: 'Scored 1–5', text: 'annual baseline, then Q1 · Q2 · Q3 · Q4' }], notes: A.statements });
  await d.cards({ title: '2.3 · Reading the ESRG performance profile', cols: 4, titleSize: 26, items: [
    { icon: 'FaCheckDouble', title: 'Aligned', text: '4.0 – 5.0' },
    { icon: 'FaWrench', title: 'Improvement required', text: '3.0 – 3.9' },
    { icon: 'FaExclamationTriangle', title: 'Significant constraint', text: '2.0 – 2.9' },
    { icon: 'FaTimesCircle', title: 'Critical constraint', text: '1.0 – 1.9', dark: true }],
    band: 'Read every component score: a strong average can conceal a critical constraint.', notes: A.profile });
  await d.stat({ title: '2.4 · Making sense of the results', big: '2.0', caption: 'Operational Flow: the constraint in an illustrative customer service profile', rows: [
    { icon: 'FaBuilding', label: 'Operational Readiness', text: '4.3' },
    { icon: 'FaStream', label: 'Operational Flow', text: '2.0' },
    { icon: 'FaCoins', label: 'Delivery Capacity', text: '4.0' },
    { icon: 'FaGavel', label: 'Decision Responsiveness', text: '3.7' }], notes: A.results });
  await d.list({ title: 'Section 2 Reflections', fontSize: 24, rows: [
    { icon: 'FaPen', label: '2.1', text: 'Which of the four capabilities is most critical to your function’s current strategic commitment, and what would happen if it were unable to meet the required demand?' },
    { icon: 'FaPen', label: '2.4', text: 'Which component has the lowest score? What evidence supports that rating? Has the score changed since the previous review? Which strategic commitment is most exposed?' }], notes: A.ref2 });

  // ── Section 3
  await d.section({ num: 3, name: 'Extrapolating', anchor: 'Where', heading: 'Where do executive biases distort ESRG operating capabilities?', outcomes: [
    'Diagnose executive decision biases that distort specific ESRG components and weaken the organisational capabilities required for strategic execution.',
    'Develop evidence-based debiasing techniques that strengthen executive decision-making and prevent cross-functional operating constraints.'], notes: B.s3 });
  await d.list({ title: '3.1a · CXO ESRG bias contributors: Cards 1 to 5', fontSize: 24, rows: [
    { icon: 'FaCompass', label: 'CEO · Strategic Optimism', text: 'Infrastructure · Investment' },
    { icon: 'FaCoins', label: 'CFO · Short-Term Cost Preference', text: 'Asset Availability · Investment' },
    { icon: 'FaCogs', label: 'COO · Standardisation Fixation', text: 'Standardisation · Process Efficiency' },
    { icon: 'FaUserFriends', label: 'CHRO · People-Centred Attribution', text: 'Integration · Technology' },
    { icon: 'FaServer', label: 'CTO/CIO · Legacy Loyalty', text: 'Technology · Investment' }], notes: B.cxo1 });
  await d.list({ title: '3.1b · CXO ESRG bias contributors: Cards 6 to 10', fontSize: 24, rows: [
    { icon: 'FaBullhorn', label: 'CMO · Brand-Led Investment', text: 'Facilities · Process Efficiency' },
    { icon: 'FaHandshake', label: 'CCO · Revenue Prioritisation', text: 'Process Efficiency · Resource Utilisation' },
    { icon: 'FaBoxes', label: 'CPO · Consolidation Efficiency', text: 'Asset Availability · Risk Management' },
    { icon: 'FaShieldAlt', label: 'CRO · Compliance Framing', text: 'Risk Management · Infrastructure' },
    { icon: 'FaRoute', label: 'CSO · Planning Optimism', text: 'Investment · Integration' }], notes: B.cxo2 });
  await d.list({ title: '3.2 · My Executive ESRG Bias Reflection', fontSize: 24, rows: [
    { icon: 'FaMousePointer', label: 'Component', text: 'one per domain · CFO: Resources · Investment' },
    { icon: 'FaBrain', label: 'My potential bias', text: 'immediate cost cuts over long-term reliability' },
    { icon: 'FaExclamationTriangle', label: 'Execution consequence', text: 'essential investment delayed, capacity reduced' },
    { icon: 'FaBalanceScale', gold: true, label: 'My debiasing technique', text: 'test the investment against strategic delivery' }], notes: B.bias });

  // ── Section 4
  await d.section({ num: 4, name: 'Integration', anchor: 'Collective', heading: 'How does the executive team create collective intelligence for ESRG alignment?', outcomes: [
    'Integrate functional ESRG assessments into a collective intelligence view by identifying convergence, divergence and dependency across organisational operating capabilities.',
    'Formulate collective intelligence responses that coordinate shared conditions, reconcile functional differences and align operating dependencies affecting strategic commitments.'], notes: B.s4 });
  await d.cards({ title: '4.1 · Three dimensions of collective intelligence', cols: 3, titleSize: 26, items: [
    { icon: 'FaCompressArrowsAlt', title: 'Convergence', text: 'Functional Intelligence → Coordinate' },
    { icon: 'FaExpandArrowsAlt', title: 'Divergence', text: 'Cross-Functional Intelligence → Reconcile' },
    { icon: 'FaProjectDiagram', title: 'Dependency', text: 'Enterprise Intelligence → Align', dark: true }],
    band: 'What we share → Where we differ → How we depend on one another', notes: B.dims });
  await table(d, { title: '4.2 · Enterprise ESRG Scanner: summary view', y: 1.55,
    head: ['Capability', 'Finance', 'Operations', 'Commercial', 'HR', 'Technology', 'Average'],
    colW: [2.6, 1.45, 1.75, 1.95, 0.93, 1.85, 1.6], rowH: [0.62, 0.86, 0.86, 0.86, 0.86],
    rows: [
      Object.assign(['Operational Readiness', '4.00', '2.67', '4.00', '4.00', '3.33', '3.60'], { low: [2] }),
      Object.assign(['Operational Flow', '3.33', '2.67', '3.00', '3.67', '2.67', '3.07'], { low: [2, 5] }),
      Object.assign(['Delivery Capacity', '4.00', '2.67', '3.67', '4.00', '3.00', '3.47'], { low: [2] }),
      ['Decision Responsiveness', '4.00', '3.33', '3.67', '4.00', '3.67', '3.73']],
    band: 'Illustrative scores. Read the component view alongside the summary.', notes: B.scanner });
  await d.cards({ title: '4.3 · Interpreting the prepopulated scanner', cols: 3, titleSize: 26, items: [
    { icon: 'FaCompressArrowsAlt', title: 'Convergence', text: 'Integration scores 2 in four functions' },
    { icon: 'FaExpandArrowsAlt', title: 'Divergence', text: 'Infrastructure: Operations 2, four functions 4' },
    { icon: 'FaProjectDiagram', title: 'Dependency', text: 'Commercial growth relies on Operations', dark: true }],
    band: 'Every finding is a hypothesis to validate through evidence and dialogue.', notes: B.interpret });
  await d.list({ title: '4.4 · Collective Intelligence Response', fontSize: 24, rows: [
    { icon: 'FaCompressArrowsAlt', label: 'COORDINATE · Integration', text: 'four functions score 2' },
    { icon: 'FaExpandArrowsAlt', label: 'RECONCILE · Technology', text: 'Technology 2, other functions 4' },
    { icon: 'FaProjectDiagram', gold: true, label: 'ALIGN · Infrastructure', text: 'Operations 2 carries commercial growth' }], notes: B.response });
  await d.list({ title: '4.5 · My Capstone Functional ESRG Assessment', fontSize: 24, rows: [
    { icon: 'FaUserTie', label: 'Role and problem', text: 'your capstone role, function and stated problem' },
    { icon: 'FaSlidersH', label: 'Score 12 components', text: '1–5, or N/A where genuinely not applicable' },
    { icon: 'FaCalendarCheck', label: 'Annual baseline', text: 'your scores save as you work' },
    { icon: 'FaUsers', gold: true, label: 'Feeds your team', text: 'the Enterprise ESRG Scanner in Section 5' }], notes: B.capscan });
  await d.list({ title: 'Section 4 Reflections', fontSize: 24, rows: [
    { icon: 'FaCompressArrowsAlt', label: 'Convergence', text: 'Which functions report similar conditions, and do those ratings reflect a shared cause?' },
    { icon: 'FaExpandArrowsAlt', label: 'Divergence', text: 'What explains the differences in scores, requirements or operating experience?' },
    { icon: 'FaProjectDiagram', label: 'Dependency', text: 'Which strategic commitment depends on these conditions, and which functions must act together?' },
    { icon: 'FaPen', gold: true, label: 'Each response', text: 'What does the evidence establish, and which decision needs collective agreement?' }], notes: B.ref4 });

  // ── Section 5
  await d.section({ num: 5, name: 'Application', anchor: 'In Practice', heading: 'The Enterprise ESRG Alignment Clinic', outcomes: [
    'Consolidate and interpret functional ESRG assessments to establish an evidence-based enterprise view of the operating capabilities required for strategic delivery.',
    'Develop and operationalise collective ESRG alignment interventions that address operating constraints and strengthen cross-functional delivery of strategic commitments.'], notes: B.s5 });
  await d.list({ title: 'The Clinic: how it runs', fontSize: 24, rows: [
    { icon: 'FaKeyboard', label: 'Group record', text: 'the scribe types what your group agrees' },
    { icon: 'FaLayerGroup', label: '5.1 Consolidate', text: 'every member’s 4.5 baseline, no rescoring' },
    { icon: 'FaSearch', label: '5.2 Interpret', text: 'each capability, findings with evidence' },
    { icon: 'FaTable', label: '5.3 Respond', text: 'the Collective Intelligence Response Table' },
    { icon: 'FaTasks', label: '5.4 Plan', text: 'the ESRG Alignment Intervention Plan' },
    { icon: 'FaCheckDouble', gold: true, label: 'Agree', text: 'boxes 10A to 10D of your Blueprint' }], notes: B.clinic });
  await d.list({ title: '5.1 · Consolidate individual functional scores', fontSize: 24, rows: [
    { icon: 'FaClipboardCheck', label: 'Step 1 · Verify', text: 'one complete assessment per function' },
    { icon: 'FaTable', label: 'Step 2 · Component view', text: 'scores come from each member’s scanner' },
    { icon: 'FaCalculator', label: 'Step 3 · Capability summary', text: 'means per function, enterprise average' },
    { icon: 'FaBan', gold: true, label: 'Non-negotiable', text: 'corrections are made in 4.5, at source' }], notes: B.consolidate });
  await d.cards({ title: '5.2 · Interpret by execution capability', cols: 2, titleBeside: true, titleSize: 26, iconSize: 0.6, items: [
    { icon: 'FaBuilding', title: 'Operational Readiness', text: 'Facilities · Infrastructure · Technology' },
    { icon: 'FaStream', title: 'Operational Flow', text: 'Standardisation · Integration · Process Efficiency' },
    { icon: 'FaCoins', title: 'Delivery Capacity', text: 'Asset Availability · Investment · Resource Utilisation' },
    { icon: 'FaGavel', title: 'Decision Responsiveness', text: 'Policies & Procedures · Authority · Risk Management', dark: true }],
    band: 'For each: Convergence → Divergence → Dependency, with evidence.', notes: B.interpret5 });
  await d.list({ title: '5.3 · Collective Intelligence Response Table', fontSize: 24, rows: [
    { icon: 'FaPuzzlePiece', label: 'Component', text: 'domain, capability and component' },
    { icon: 'FaSearch', label: 'Collective finding', text: 'what the evidence shows' },
    { icon: 'FaBullseye', label: 'Commitment affected', text: 'the strategic commitment at risk' },
    { icon: 'FaHandsHelping', label: 'Collective response', text: 'Coordinate · Reconcile · Align' },
    { icon: 'FaUsers', gold: true, label: 'Functions involved', text: 'the executives who must act' }], notes: B.table53 });
  await d.list({ title: '5.4 · ESRG Alignment Intervention Plan', fontSize: 24, rows: [
    { icon: 'FaArrowRight', label: 'Agreed response', text: 'copied from 5.3' },
    { icon: 'FaTasks', label: 'Implementation actions', text: 'what will be done' },
    { icon: 'FaUserTie', label: 'Accountable executive', text: 'one owner' },
    { icon: 'FaUsers', label: 'Contributing functions', text: 'who else acts' },
    { icon: 'FaCalendarAlt', label: 'Target date', text: 'when' },
    { icon: 'FaChartLine', gold: true, label: 'Evidence of improvement', text: 'the condition has changed' }], notes: B.plan54 });

  await d.list({ title: 'Unit Summary · Closing', fontSize: 24, rows: [
    { icon: 'FaEye', label: 'Awareness', text: 'ESRG names the capabilities a commitment needs' },
    { icon: 'FaLightbulb', label: 'Intelligence', text: 'a profile shows where conditions enable or constrain' },
    { icon: 'FaMapMarkedAlt', label: 'Extrapolating', text: 'executive decisions shape operating conditions' },
    { icon: 'FaUsers', label: 'Integration', text: 'coordinate, reconcile and align across functions' },
    { icon: 'FaClipboardCheck', gold: true, label: 'Application', text: 'the response says what; the plan says how' }], notes: B.summary });

  await d.save(OUT);
  console.log('saved', OUT);
})().catch(e => { console.error(e); process.exit(1); });
