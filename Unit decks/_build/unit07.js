// Unit 7 · Establishing Performance Expectations — facilitator deck with detailed presenter notes.
// Run: node unit07.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u07.json'), FH = R('unit3_m1_lens6_f.html'), PH = R('unit3_m1_lens6_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const NOTIME = 'Time: the facilitator file gives no suggested time for this section.';

(async () => {
  const d = new Deck({ unit: 7, module: 3, moduleName: 'Influence', title: 'Establishing Performance Expectations' });
  const G = u.guide();

  await d.cover({ logo: LOGO, subtitle: 'Turning delivery goals into genuine ownership',
    notes: N('UNIT 7 · ESTABLISHING PERFORMANCE EXPECTATIONS\nModule 3 · Influence · Unit 7', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Execution begins when the people responsible for those goals internalise the expectation and accept ownership of the result. This unit equips leaders to close the gap between a well-designed performance management system and genuine human commitment to deliver it.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time: the facilitator file gives suggested timing only for the Section 5 role play: 15 minutes per round, two rounds minimum, then a plenary debrief.', G[1], G[2]) });

  // ── Section 1
  await div(d, 1, NOTIME);
  await d.compare({ title: '1.1 · Setting and establishing expectations', cols: [
    { icon: 'FaBullhorn', title: 'Setting', sub: 'Top-down declaration', points: ['Clarity of instruction', 'KPI as a metric to monitor', 'Conditional, defensive ownership'] },
    { icon: 'FaHandshake', title: 'Establishing', sub: 'Leadership alignment', points: ['Mutual readiness for execution', 'KPI as a personal leadership promise', 'Personal, proactive ownership'] }],
    notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · Three conditions of established expectations', cols: 3, items: [
    { icon: 'FaBullseye', title: 'Clarity', text: 'The individual understands exactly what success looks like.' },
    { icon: 'FaCogs', title: 'Capability', text: 'The system can realistically support delivery.' },
    { icon: 'FaHandshake', title: 'Commitment', dark: true, text: 'The person consciously accepts ownership of the outcome.' }],
    band: 'An alignment score below 9 means Commitment is not yet established.',
    notes: u.partNotes(1, 1) });
  await d.cards({ title: '1.3 · The Expectations Chain', cols: 3, items: [
    { icon: 'FaArrowUp', title: 'Upline', text: 'Who must approve or resource this outcome?' },
    { icon: 'FaArrowDown', title: 'Downline', text: 'Who must deliver specific activities?' },
    { icon: 'FaExchangeAlt', title: 'External', text: 'Which external actors influence delivery?' }],
    notes: u.partNotes(1, 2) });
  await d.prompt({ icon: 'FaSlidersH', label: '1.4 · The Alignment Dialogue', text: '“On a scale of 1–10, how aligned are you with the expectation for you to deliver this outcome?”',
    foot: '9 or 10: genuine ownership. Anything lower: Score → Evaluate → Resolve.',
    notes: u.partNotes(1, 3) });

  // ── Section 2
  await div(d, 2, NOTIME);
  await d.compare({ title: '2.1 · The execution dynamic', cols: [
    { icon: 'FaClipboardList', title: 'Compliance-driven', sub: 'Acknowledged', points: ['Wait for direction', 'Escalate problems upward', 'Activity ownership'] },
    { icon: 'FaFire', title: 'Commitment-driven', sub: 'Owned', points: ['Anticipate risks earlier', 'Take initiative, surface issues', 'Outcome ownership'] }],
    notes: u.partNotes(2, 0) });
  await d.list({ title: '2.2 · Five mechanisms', fontSize: 26, rows: [
    { icon: 'FaHandshake', label: '1', text: 'From Instruction to Ownership' },
    { icon: 'FaBullseye', label: '2', text: 'Reducing Interpretation Ambiguity' },
    { icon: 'FaSearch', label: '3', text: 'Surfacing Constraints Before Execution Begins' },
    { icon: 'FaUserCheck', label: '4', text: 'Strengthening Accountability' },
    { icon: 'FaLayerGroup', label: '5', text: 'Building the Behavioural Foundation' }],
    notes: u.partNotes(2, 1) });
  await d.compare({ title: '2.3 · The two casualties', cols: [
    { icon: 'FaBatteryQuarter', title: 'Engagement weakens', sub: 'Observable but subtle', points: ['Only what is assigned gets done', 'People wait for direction', 'Engagement becomes transactional'] },
    { icon: 'FaUserSlash', title: 'Accountability dilutes', sub: 'The deeper cost', points: ['Explanations replace ownership', 'Dependencies cause delay', 'Everyone partly responsible'] }],
    band: 'Ownership of the outcome was assigned without being secured.',
    notes: u.partNotes(2, 2) });

  // ── Section 3
  await div(d, 3, NOTIME);
  {
    const s = d.slide(); d.title(s, '3.1 · CXO expectation tendencies');
    const roles = [['CEO', 'Enterprise Ambition'], ['CFO', 'Financial Precision'], ['COO', 'Operational Discipline'], ['CHRO', 'Cultural Alignment'], ['CTO/CIO', 'Technical Milestones'],
      ['CMO', 'Market Performance'], ['CCO', 'Commercial Ambition'], ['CPO', 'Procurement Discipline'], ['CRO', 'Risk Governance'], ['CSO', 'Strategic Planning']];
    roles.forEach(([r, c], i) => {
      const x = 0.6 + (i % 2) * 6.15, y = 1.7 + Math.floor(i / 2) * 1.05;
      box(s, x, y, 5.95, 0.9, C.tint);
      T(s, [{ text: r + '   ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: c }], { x: x + 0.25, y, w: 5.5, h: 0.9, fontSize: 26, valign: 'middle' });
    });
    s.addNotes(u.partNotes(3, 0));
  }

  // ── Section 4
  await div(d, 4, NOTIME);
  await d.list({ title: '4.1 · The four-step Expectation Architecture', fontSize: 26, rows: [
    { icon: 'FaMountain', label: '1 · Start With the Future', text: 'why the expectation matters' },
    { icon: 'FaBullseye', label: '2 · Clarify the Delivery Expectation', text: 'in outcome terms' },
    { icon: 'FaLink', label: '3 · Identify the Expectations Chain', text: 'who else must contribute' },
    { icon: 'FaHandshake', gold: true, label: '4 · Confirm Ownership', text: 'ask the Alignment Question' }],
    notes: u.partNotes(4, 0) });
  await d.list({ title: '4.2 · Score → Evaluate → Resolve', fontSize: 26, rows: [
    { icon: 'FaCheckCircle', label: '9–10', text: 'clear ownership: proceed and document' },
    { icon: 'FaAdjust', label: '7–8', text: 'partial alignment: Evaluate' },
    { icon: 'FaExclamationCircle', label: '5–6', text: 'significant concerns: Evaluate' },
    { icon: 'FaTimesCircle', gold: true, label: 'Below 5', text: 'redesign the expectation' }],
    notes: u.partNotes(4, 1) });
  await d.prompt({ icon: 'FaKey', label: 'The Resolve question', text: '“What would help move your alignment from where it is now to a 9 or 10?”',
    notes: N('THE RESOLVE QUESTION', 'Guidance (4.2): The Resolve question — “What would move you to a 9 or 10?” — is the most important question in the whole architecture. It keeps the leader in the right posture: solving for the person’s ability to own it. Have leaders practise asking it aloud before the Application section. It sounds simple and feels unfamiliar the first time.',
      'Participant reflection (participant file, 4.2 · ✎ Reflection — Practise the Resolve Question): “Write the Resolve question in your own words. Then apply it to a real expectation alignment scenario you are currently facing.”') });

  // ── Section 5
  await div(d, 5);
  await d.prompt({ icon: 'FaTheaterMasks', label: 'Role play · Case context', text: 'Key Result: cut customer complaint resolution time from 48 hours to 12 hours by Q3 2026.',
    foot: 'SiP: “The most responsive and trusted partner in our market…”',
    notes: N('ROLE PLAY — ESTABLISHING DELIVERY EXPECTATIONS', 'You are a CXO establishing delivery expectations with a team member or Head of Department. Your goal is to ensure that the expectation moves beyond communication into clear ownership of delivery.',
      'Case Context:\n' + u.sec(5).lead.content.slice(1).join('\n')) });
  await d.list({ title: 'Role play: seven steps', fontSize: 24, rows: [
    { icon: 'FaUser', label: '1', text: 'Identify who you are establishing expectations with' },
    { icon: 'FaMountain', label: '2', text: 'Start with the Future' },
    { icon: 'FaBullseye', label: '3', text: 'Clarify the delivery expectation' },
    { icon: 'FaLink', label: '4', text: 'Identify the Expectations Chain' },
    { icon: 'FaHandshake', label: '5', text: 'Confirm ownership of the result' },
    { icon: 'FaSyncAlt', label: '6', text: 'Below 9: Score → Evaluate → Resolve' },
    { icon: 'FaPenFancy', label: '7', text: 'Leader reflection and commitment record' }],
    notes: N('ROLE PLAY · THE SEVEN STEPS (participants record each step in their own file)', [0, 1, 2, 3, 4, 5, 6].map(j => u.partNotes(5, j)).join('\n\n———\n\n')) });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing', text: 'Name one expectation you have set but not yet established, with a specific person in your expectations chain.',
    foot: 'Commit to that alignment dialogue within five working days: the score, the primary concern and the action for elevation.',
    notes: u.partNotes(5, 7) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
