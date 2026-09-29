// Unit 11 · Culture Reinforcement & Organisational Health — facilitator deck with detailed presenter notes.
// Run: node unit11.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u11.json'), FH = R('unit4_m1_lens10_f.html'), PH = R('unit4_m1_lens10_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const slice = (lines, a, b) => { const i = lines.findIndex(l => l.startsWith(a)); const j = b ? lines.findIndex((l, k) => k > i && l.startsWith(b)) : -1; return lines.slice(i, j < 0 ? lines.length : j).join('\n'); };
const NOTIME = 'Time: the facilitator file gives no minute timing for this section.';
const SEP = '\n\n———\n\n';
const gl = b => b.map(l => l.replace(/^◆ /, '')).join('\n');

(async () => {
  const d = new Deck({ unit: 11, module: 4, moduleName: 'Grounding', title: 'Culture Reinforcement & Organisational Health' });
  const G = u.guide(), S4 = u.sec(4);
  const X53 = u.part(5, 2).content;

  await d.cover({ logo: LOGO, subtitle: 'The internal condition that determines whether strategy can actually be executed',
    notes: N('UNIT 11 · CULTURE REINFORCEMENT & ORGANISATIONAL HEALTH\nModule 4 · Grounding · Unit 11', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Organisational health is the internal condition that determines whether strategy can actually be executed. This unit builds leaders’ ability to recognise, diagnose, and actively maintain the health of the organisation as the foundation upon which all performance is built.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time: the facilitator file gives two timings: 8–10 minutes of silent individual scoring for the Health Thermometer (Section 3), and 40 minutes for the Application exercise (10 minutes choose and prepare, 20 minutes coaching in pairs, 10 minutes debrief).', G[1], G[2]) });

  // ── Section 1
  await div(d, 1, NOTIME);
  await d.prompt({ icon: 'FaHeartbeat', label: '1.1 · What is organisational health?', text: 'Think of the best team environment you have ever been part of. What made it feel different?',
    foot: 'That difference is what Lencioni calls organisational health.', notes: u.partNotes(1, 0) });
  await d.list({ title: '1.2 · The five observable traits', fontSize: 26, rows: [
    { icon: 'FaHandshake', label: 'Trait 1 · Minimal Politics', text: 'issues surface and are addressed directly' },
    { icon: 'FaCompass', label: 'Trait 2 · Minimal Confusion', text: 'clear direction, ownership, authority' },
    { icon: 'FaSmile', label: 'Trait 3 · High Morale', text: 'purpose and recognition' },
    { icon: 'FaCogs', label: 'Trait 4 · High Productivity', text: 'effort converts into results' },
    { icon: 'FaUserFriends', gold: true, label: 'Trait 5 · Low Turnover', text: 'people choose to stay' }],
    notes: u.partNotes(1, 1) });
  await d.list({ title: '1.3 · The Organisational Health Pyramid', fontSize: 26, rows: [
    { icon: 'FaShieldAlt', label: 'Trust', text: 'the foundation' },
    { icon: 'FaComments', label: 'Experiences', text: 'shaped by trust' },
    { icon: 'FaBrain', label: 'Beliefs', text: 'formed by experiences' },
    { icon: 'FaRunning', label: 'Actions', text: 'driven by beliefs' },
    { icon: 'FaChartLine', gold: true, label: 'Results', text: 'the visible traits' }],
    notes: u.partNotes(1, 2) });
  await d.list({ title: '1.4 · When trust erodes', fontSize: 26, rows: [
    { icon: 'FaUserSecret', label: 'Politics increase', text: 'as people stop trusting shared decisions' },
    { icon: 'FaQuestion', label: 'Confusion spreads', text: 'as communication stops being clear' },
    { icon: 'FaFrown', label: 'Morale declines', text: 'as effort stops seeming to matter' },
    { icon: 'FaBatteryQuarter', label: 'Productivity drops', text: 'as energy goes to internal friction' },
    { icon: 'FaDoorOpen', gold: true, label: 'Turnover rises', text: 'as the organisation stops seeming worth staying in' }],
    notes: u.partNotes(1, 3, { extra: 'Guidance (Section 1) closing statement: The pyramid explains the traits. The traits tell you what to look for. The pyramid tells you where to look when they are missing.' }) });

  // ── Section 2
  await div(d, 2, NOTIME);
  await d.compare({ title: '2.1–2.2 · Signals and conditions of health', cols: [
    { icon: 'FaEye', title: 'What we see', sub: 'The signals of health', points: ['Low politics', 'High clarity', 'Strong morale', 'Productive collaboration', 'Stable teams'] },
    { icon: 'FaSeedling', title: 'What we create', sub: 'The conditions of health', points: ['Trust', 'Experiences', 'Shared beliefs', 'Behaviour'] }],
    notes: [0, 1].map(j => u.partNotes(2, j)).join(SEP) });
  await d.list({ title: '2.3 · The price of poor health', fontSize: 26, rows: [
    { icon: 'FaClock', label: 'Time lost', text: 'through unclear communication and repeated work' },
    { icon: 'FaUserSlash', label: 'Quiet disengagement', text: 'from capable employees' },
    { icon: 'FaUnlink', label: 'Declining trust', text: 'as focus shifts to protecting turf' },
    { icon: 'FaBed', gold: true, label: 'Emotional fatigue', text: 'as contribution turns to self-preservation' }],
    notes: u.partNotes(2, 2, { extra: 'Guidance (Section 2): Pause after each cost and ask: “Where do you see this in your organisation right now?”' }) });

  // ── Section 3
  await div(d, 3, 'Time: 8–10 minutes for participants to complete the thermometer individually and in silence (no discussion while scoring).');
  await d.prompt({ icon: 'FaThermometerHalf', label: '3.1 · The Organisational Health Thermometer', text: 'Rate each of the 20 statements honestly, 1 to 5. Complete it individually and in silence.',
    foot: 'Five traits · four statements each · a total out of 100.', notes: u.partNotes(3, 0, { prompts: false }) });
  await d.list({ title: '3.2 · Reading your temperature', fontSize: 26, rows: [
    { icon: 'FaCheckCircle', label: '80–100', text: 'Healthy & Thriving' },
    { icon: 'FaAdjust', label: '60–79', text: 'Stable but Uneven' },
    { icon: 'FaExclamationTriangle', label: '40–59', text: 'Caution Zone' },
    { icon: 'FaExclamationCircle', gold: true, label: '20–39', text: 'Unhealthy' }],
    notes: u.partNotes(3, 1) });
  await d.list({ title: '3.3 · ACE-IT guardrail priorities by temperature', fontSize: 24, rows: [
    { icon: 'FaCheckCircle', label: 'Healthy & Thriving', text: 'Commitment + Transparency' },
    { icon: 'FaAdjust', label: 'Stable but Uneven', text: 'Engagement + Accountability' },
    { icon: 'FaExclamationTriangle', label: 'Caution Zone', text: 'Integrity + Engagement + Transparency' },
    { icon: 'FaExclamationCircle', gold: true, label: 'Unhealthy', text: 'all five; begin with Accountability' }],
    notes: u.partNotes(3, 2) });

  // ── Section 4
  await d.section({ num: 4, name: 'Integration', anchor: 'Collective', heading: S4.h2, outcomes: S4.slo,
    notes: N('SECTION 4 · INTEGRATION — COLLECTIVE\n' + S4.h2 + '\n' + S4.sub, 'Section learning outcomes:\n' + S4.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'), S4.lead.guidance.map(gl),
      NOTIME, 'The CXO Health Architecture content is in the notes of the next slide.') });
  {
    const s = d.slide(); d.title(s, 'The CXO Health Architecture');
    const roles = [['CEO', 'Clarity of direction'], ['CFO', 'Resource fairness'], ['COO', 'Operational clarity'], ['CHRO', 'Psychological safety'], ['CTO/CIO', 'Productive technology'],
      ['CMO', 'Purpose and meaning'], ['CCO', 'Commercial team health'], ['CPO', 'Operational fairness'], ['CRO', 'Safety to raise risks'], ['CSO', 'Strategic coherence']];
    roles.forEach(([r, c], i) => {
      const x = 0.6 + (i % 2) * 6.15, y = 1.7 + Math.floor(i / 2) * 1.05;
      box(s, x, y, 5.95, 0.9, C.tint);
      T(s, [{ text: r + '   ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: c }], { x: x + 0.25, y, w: 5.5, h: 0.9, fontSize: 26, valign: 'middle' });
    });
    s.addNotes(N('THE CXO HEALTH ARCHITECTURE (select each role in the file)', 'Content:\n' + S4.lead.content.join('\n'),
      'Guidance (Section 4): Open by revealing the team average and temperature. Ask each leader to name their own domain first — before commenting on others.'));
  }

  // ── Section 5
  await div(d, 5, 'Time: 40 minutes — Part 1 · 10 minutes choose and prepare; Part 2 · 20 minutes coach in pairs (ten minutes each direction); Part 3 · 10 minutes debrief. Protect the full 40 minutes.');
  await d.cards({ title: '5.1 · Choose your scenario', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaComments', title: '1 · The Corridor Consensus', text: 'David · Minimal Politics, Minimal Confusion' },
    { icon: 'FaRandom', title: '2 · The Confusion Spiral', text: 'Priya · Minimal Confusion, High Productivity' },
    { icon: 'FaDoorOpen', title: '3 · The Quiet Exit', text: 'James · High Morale, Low Turnover' },
    { icon: 'FaAnchor', title: '4 · The Execution Drag', text: 'Fatima · High Productivity, Minimal Politics' }],
    notes: u.partNotes(5, 0, { prompts: false }) });
  await d.list({ title: '5.2 · The ACE-IT Coaching Protocol', fontSize: 24, rows: [
    { icon: 'FaUserCheck', label: 'A · Accountability', text: 'own the conversation first' },
    { icon: 'FaHandshake', label: 'C · Commitment', text: 'ask for something real' },
    { icon: 'FaComments', label: 'E · Engagement', text: 'create the conditions for honesty' },
    { icon: 'FaBalanceScale', label: 'I · Integrity', text: 'say the honest thing' },
    { icon: 'FaLightbulb', gold: true, label: 'T · Transparency', text: 'share your context' }],
    notes: u.partNotes(5, 1) });
  await d.cards({ title: '5.3 · The exercise: 40 minutes', cols: 3, items: [
    { icon: 'FaUserEdit', title: 'Part 1 · 10 min', text: 'Choose and prepare' },
    { icon: 'FaUsers', title: 'Part 2 · 20 min', text: 'Coach in pairs' },
    { icon: 'FaComments', title: 'Part 3 · 10 min', dark: true, text: 'Debrief in the room' }],
    band: 'Did you say the honest thing? Go again and say it without softening.',
    notes: u.partNotes(5, 2, { content: false, extra: 'Content:\n' + slice(X53, 'Part 1', 'Debrief in the Room') }) });
  await d.prompt({ icon: 'FaComments', label: 'Debrief in the room', text: '“Which ACE-IT behaviour did you find easiest to apply — and which did you abandon or soften?”',
    foot: '“The conversation I am committing to have is with [role], about [topic], before [date].”',
    notes: N('DEBRIEF IN THE ROOM (Part 3 · 10 minutes)', 'Content:\n' + slice(X53, 'Debrief in the Room'),
      'Guidance (Application): For the debrief question, expect most leaders to name Integrity or Transparency. These are the behaviours that require the most personal exposure. The value of naming them publicly is that the room holds each other accountable from that moment forward.\nClose with the commitment statement: each leader names the person, the topic, and the date. Write them on a visible surface. These commitments are the output of the unit.') });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing', text: 'Organisational health is where the entire S2R® programme finds its human foundation.',
    foot: 'Direction without health produces strategies that no one believes in.',
    notes: u.partNotes(5, 3) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
