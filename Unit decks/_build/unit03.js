// Unit 3 · SiP KISS Mapping & OKR Definition — facilitator deck with detailed presenter notes.
// Run: node unit03.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N, divider, portfolio } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u03.json'), FH = R('unit2_m1_lens2_f.html'), PH = R('unit2_m1_lens2_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);

(async () => {
  const d = new Deck({ unit: 3, module: 2, moduleName: 'Direction', title: 'SiP KISS Mapping & OKR Definition' });
  const KD = u.js('KISS_DOMAINS'), HZ = u.js('HOT_ZONES'), AK = u.js('APP_KISS'), AO = u.js('APP_OBJECTIVES'), PM = u.js('PM_CELLS'), BI = u.js('BIASES'), SUM = u.js('SUMMARY');
  const G = u.guide();

  await d.cover({ logo: LOGO, subtitle: 'From Success in Practice to a focused, measurable execution architecture',
    notes: N('UNIT 3 · SiP KISS MAPPING & OKR DEFINITION\nModule 2 · Direction · Unit 3', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): This unit guides the leadership team from the Success in Practice narrative into a focused, measurable execution architecture — through KISS reflection, OKR construction, and collective prioritisation.',
      'Time: section timings in the facilitator file add up to 145–190 minutes (about 2.5 to 3 hours), plus breaks.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time by section (from the facilitator file):\n- Section 1 · Awareness — What: 30–40 minutes\n- Section 2 · Intelligence — Why: 15–20 minutes\n- Section 3 · Extrapolating — Where: 20–25 minutes\n- Section 4 · Integration — Collective: 25–35 minutes\n- Section 5 · Application — In Practice: 55–70 minutes', G[1], G[2]) });

  // ── Section 1
  await div(d, 1);
  await d.prompt({ icon: 'FaQuoteLeft', label: '1.1 · Translating Success in Practice into action', text: 'If the Success in Practice we described is the future organisation, what must change in the organisation today to make that future possible?',
    notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · KISS: four reflective filters', cols: 4, titleSize: 30, textSize: 24, items: [
    { icon: 'FaShieldAlt', title: 'KEEP', text: 'Protect what is already working' },
    { icon: 'FaArrowUp', title: 'IMPROVE', text: 'Strengthen what is partially working' },
    { icon: 'FaPlay', title: 'START', text: 'Introduce what does not yet exist' },
    { icon: 'FaStop', title: 'STOP', dark: true, text: 'Eliminate what contradicts the SiP' }],
    band: 'Every KISS reflection must be anchored to the Success in Practice statement.',
    notes: u.partNotes(1, 1) });
  await d.cards({ title: '1.3 · The KISS reflection table: four domains', cols: 2, titleBeside: true, titleSize: 24, textSize: 24, iconSize: 0.6, items: KD.map((k, i) => ({ icon: ['FaSmile', 'FaCogs', 'FaUsers', 'FaChartLine'][i], title: k.label.replace(' & Execution Rhythm', '').replace(' Dynamics', ''), text: k.anchor })),
    notes: N(u.partNotes(1, 2),
      'The four domains, SiP anchor questions and KISS prompts:\n\n' + KD.map(k => `${k.label.toUpperCase()}\nSiP anchor: ${k.anchor}\nKEEP: ${k.keep}\nIMPROVE: ${k.improve}\nSTART: ${k.start}\nSTOP: ${k.stop}`).join('\n\n')) });
  await d.compare({ title: '1.4 · OKR anatomy', cols: [
    { icon: 'FaFlag', title: 'Objectives', sub: 'Define strategic ambition', points: ['Qualitative and ambitious', 'Action-oriented and inspirational', 'Memorable: the T-shirt test'] },
    { icon: 'FaRuler', title: 'Key Results', sub: 'Define measurable progress', points: ['Verb of Change + Metric', 'From X to Y + By Deadline', '2–3 per Objective'] }],
    band: 'Can you check it off a task list? If yes, it is a task.',
    notes: u.partNotes(1, 3) });
  await d.list({ title: '1.4 · The Key Result formula', fontSize: 26, rows: [
    { icon: 'FaArrowUp', label: 'Verb of Change', text: 'Increase, Reduce, Achieve, Improve, Maintain' },
    { icon: 'FaChartBar', label: 'Metric', text: 'a clear and measurable indicator' },
    { icon: 'FaExchangeAlt', label: 'From X to Y', text: 'baseline and target: from 40% to 75%' },
    { icon: 'FaCalendarAlt', label: 'Deadline', text: 'By Q4 2026, by end of FY' }],
    notes: N('1.4 · KEY RESULT CONSTRUCTION GUIDE — 4 ELEMENTS (sub-accordion)',
      'Content:\nVerb of Change: Indicates the direction of improvement. E.g.: Increase, Reduce, Achieve, Improve, Maintain.\nMetric: A clear and measurable indicator. E.g.: Customer satisfaction score, cycle time, adoption rate.\nFrom X to Y: Defines the baseline and target. E.g.: From 40% to 75%. Always establish a starting point.\nDeadline: Specifies when the result must be achieved. E.g.: By Q4 2026, By end of FY.\nExample: Increase digital transaction completion rate from 40% to 75% by Q4 2026.',
      'Guidance: Expand the sub-accordion and walk through all four elements with participants. Then give a live example — ask a participant to state a goal they are working toward, and workshop it through the formula in real time. One concrete example does more than ten theoretical ones.') });
  await d.list({ title: '1.5 · From KISS output to OKRs', fontSize: 26, rows: [
    { icon: 'FaLayerGroup', label: 'Step 1 · Identify Strategic Themes', text: 'What insights emerged from the SiP and KISS reflections?' },
    { icon: 'FaFlag', label: 'Step 2 · Define the Objective', text: 'If we get this theme right, what will we be known for?' },
    { icon: 'FaRuler', label: 'Step 3 · Define Key Results', text: 'What measurable outcomes will prove the Objective is being achieved?' }],
    notes: u.partNotes(1, 4) });

  // ── Section 2
  await div(d, 2);
  await d.cards({ title: '2.1 · The danger of moving too fast', cols: 3, items: [
    { icon: 'FaBullseye', title: 'Disconnected Targets', text: 'Numbers set without acknowledging the hurdles.' },
    { icon: 'FaRandom', title: 'Fragmented Efforts', text: 'Functions row in different directions.' },
    { icon: 'FaRunning', title: 'The Activity Trap', text: 'Busyness measured in place of outcomes.' }],
    band: 'The organisation starts measuring the finish line before it has mapped the terrain.',
    notes: u.partNotes(2, 0) });
  await d.list({ title: '2.2 · KISS: the missing bridge', fontSize: 26, rows: [
    { icon: 'FaShieldAlt', text: 'The strengths to protect and lean into.' },
    { icon: 'FaCompressArrowsAlt', text: 'The friction points that are quietly draining energy.' },
    { icon: 'FaSearch', text: 'The gaps where genuine support or investment is needed.' },
    { icon: 'FaHistory', text: 'The old habits to finally let go of.' }],
    notes: u.partNotes(2, 1) });
  await d.cards({ title: '2.3 · The Strategy2Results® sequence', cols: 3, items: [
    { icon: 'FaMountain', title: 'Success in Practice', text: 'The dream of where the organisation wants to be.' },
    { icon: 'FaFilter', title: 'KISS', text: 'The honest look at the changes required to get there.' },
    { icon: 'FaCompass', title: 'OKRs', dark: true, text: 'The execution compass.' }],
    band: 'At which point in this sequence does our organisation typically enter?',
    notes: u.partNotes(2, 2) });

  // ── Section 3
  await div(d, 3);
  await d.list({ title: '3.1 · Natural OKR emphasis across functions', fontSize: 26, rows: [
    { icon: 'FaHandshake', label: 'Commercial leaders:', text: 'Customer Experience and Enterprise Value Creation' },
    { icon: 'FaCogs', label: 'Operational leaders:', text: 'Operational Capability and Enterprise Value Creation' },
    { icon: 'FaUsers', label: 'People leaders:', text: 'People & Culture and Operational Capability' },
    { icon: 'FaCoins', label: 'Financial leaders:', text: 'Enterprise Value Creation and Operational Discipline' }],
    notes: u.partNotes(3, 0) });
  {
    const s = d.slide(); d.title(s, '3.2 · Leadership team hot zone cards');
    box(s, 0.6, 1.65, 12.13, 1.9, C.forest);
    T(s, 'Each role: dominant future realities, natural OKR emphasis, typical hot zone and its alignment question.', { x: 0.9, y: 1.65, w: 11.6, h: 1.9, fontSize: 28, color: C.white, valign: 'middle' });
    HZ.forEach((h, i) => {
      const x = 0.6 + (i % 5) * 2.465, y = 4.0 + Math.floor(i / 5) * 1.2;
      box(s, x, y, 2.2, 0.95, C.tint);
      T(s, h.role, { x, y, w: 2.2, h: 0.95, fontSize: 28, bold: true, color: C.forest, align: 'center', valign: 'middle' });
    });
    s.addNotes(N(u.partNotes(3, 1),
      'The ten hot zone cards:\n\n' + HZ.map(h => `${h.role} — ${h.title}\nDominant future realities: ${h.top2}\nNatural OKR emphasis: ${h.emphasis}\nTypical hot zone: ${h.hot}\nAlignment question: ${h.align}`).join('\n\n')));
  }
  await d.list({ title: '3.3 · The Alignment Brigade: four execution risks', fontSize: 26, rows: [
    { icon: 'FaRandom', text: 'Competing definitions of success across functions' },
    { icon: 'FaPuzzlePiece', text: 'Fragmented measurement systems that cannot be integrated' },
    { icon: 'FaCog', text: 'Functional optimisation in place of enterprise progress' },
    { icon: 'FaHourglassHalf', text: 'Slow decision-making due to misaligned incentives' }],
    notes: u.partNotes(3, 2) });

  // ── Section 4
  await div(d, 4);
  await d.list({ title: '4.1 · The six-step path to synthesis', fontSize: 26, rows: [
    { icon: 'FaLayerGroup', label: '1 · Find Themes', text: '2–3 big shifts, written first' },
    { icon: 'FaFlag', label: '2 · Inspiring Objectives', text: 'a transformation to be known for' },
    { icon: 'FaRuler', label: '3 · Define Key Results', text: 'Verb + Metric + From X to Y + Deadline' },
    { icon: 'FaCheckDouble', label: '4 · Alignment Test', text: 'four questions, run publicly' },
    { icon: 'FaCompress', label: '5 · Panoramic Priority', text: 'the Less is More Rule' },
    { icon: 'FaTh', label: '6 · Priority Matrix', text: 'impact versus effort' }],
    notes: u.partNotes(4, 0) });
  {
    const s = d.slide(); d.title(s, '4.1 · The Prioritisation Matrix: impact × effort');
    T(s, 'Impact ↓   Effort →', { x: 0.6, y: 1.55, w: 3.0, h: 0.5, fontSize: 24, bold: true, color: C.muted });
    ['Low', 'Medium', 'High'].forEach((e, k) => T(s, e, { x: 2.5 + k * 3.45, y: 1.55, w: 3.3, h: 0.5, fontSize: 24, bold: true, color: C.forest, align: 'center' }));
    ['High', 'Medium', 'Low'].forEach((im, r) => {
      T(s, im, { x: 0.6, y: 2.15 + r * 1.62, w: 1.8, h: 1.45, fontSize: 24, bold: true, color: C.forest, valign: 'middle' });
      ['Low', 'Medium', 'High'].forEach((e, k) => {
        const c = PM.find(p => p.impact === im && p.effort === e), hot = im === 'High' && e !== 'High' || (im === 'High' && e === 'High');
        box(s, 2.5 + k * 3.45, 2.15 + r * 1.62, 3.3, 1.45, hot ? C.forest : C.tint);
        T(s, c.label, { x: 2.65 + k * 3.45, y: 2.15 + r * 1.62, w: 3.0, h: 1.45, fontSize: 24, bold: true, color: hot ? C.white : C.forest, align: 'center', valign: 'middle' });
      });
    });
    s.addNotes(N('4.1 · STEPS 5 AND 6: PANORAMIC PRIORITY AND THE PRIORITISATION MATRIX',
      'Content:\nPanoramic Enterprise OKR Prioritisation: Once initial OKRs have been drafted, the leadership team determines which Objectives deserve enterprise focus now. Strategy execution fails when too many priorities are pursued simultaneously.\nEach team member reviews proposed Objectives and votes on which represent the most critical strategic movements at this moment.\nThe Less is More Rule: No more than 4 Enterprise Objectives. No more than 3 Key Results per Objective. This constraint forces explicit trade-offs, ensuring execution energy is concentrated.\nThe Prioritisation Matrix: Impact versus Effort. The matrix evaluates initiatives along two dimensions: Impact — the degree of strategic value delivered if achieved — and Effort — the time, resources, coordination, and organisational change required.\nThe leadership team must pay particular attention to initiatives in Strategic Catalysts, Accelerated Enablers, and Core Strategic Drivers — these represent the highest leverage execution signals.',
      'The nine cells (Impact / Effort):\n' + PM.map(p => `- ${p.impact} impact / ${p.effort} effort: ${p.label}`).join('\n'),
      'Guidance: Step 5 — Panoramic Priority: Enforce the Less is More Rule — maximum 4 Enterprise Objectives, maximum 3 Key Results per Objective. This constraint is non-negotiable. The discomfort of trade-offs is the work.\nStep 6 — Priority Matrix: Walk through the matrix structure before the group places any items. The debate about what constitutes high impact versus high effort is often more valuable than the final placements.'));
  }
  await d.list({ title: '4.2 · Breaking the biases through de-labelling', fontSize: 24, rows: BI.map((b, k) => ({ icon: ['FaUsers', 'FaFilter', 'FaCommentSlash', 'FaAnchor', 'FaGlobe'][k], label: b.title, text: '· ' + b.sub })),
    notes: N(u.partNotes(4, 1),
      'The five bias patterns:\n\n' + BI.map(b => `${b.title} (${b.sub})\n${b.body}`).join('\n\n')) });

  // ── Section 5
  await div(d, 5);
  await d.list({ title: 'Worked example: KISS themes to Objectives', fontSize: 24, rows: AO.map((o, k) => ({ icon: ['FaSmile', 'FaBolt', 'FaUsers', 'FaChartLine'][k], label: o.theme + ':', text: o.obj })),
    notes: N(u.partNotes(5, 0),
      'Worked example — KISS reflection by domain (facilitator reference case):\n\n' + AK.map(a => `${a.domain}\nKEEP: ${a.keep}\nIMPROVE: ${a.improve}\nSTART: ${a.start}\nSTOP: ${a.stop}`).join('\n\n'),
      'Strategic Themes → Enterprise Objectives:\n' + AO.map(o => `${o.n}. ${o.theme} → ${o.obj}`).join('\n')) });
  await d.list({ title: 'Task 1 · Group KISS reflection', fontSize: 26, rows: [
    { icon: 'FaAnchor', label: 'Anchor every item', text: 'to the SiP' },
    { icon: 'FaPenFancy', label: '2–3 minutes per domain:', text: 'write your own inputs first' },
    { icon: 'FaUsers', label: 'Then share:', text: 'the facilitator captures agreed items' },
    { icon: 'FaLayerGroup', gold: true, label: 'Patterns:', text: 'the 2–3 themes that anchor the Objectives' }],
    notes: u.partNotes(5, 1) });
  await d.list({ title: 'Task 2 · Key Results and the de-labelled landscape', fontSize: 26, rows: [
    { icon: 'FaPenFancy', label: '3–4 minutes per Objective:', text: 'individual Key Result drafting' },
    { icon: 'FaCheckDouble', label: 'Alignment test:', text: 'does this move the whole enterprise forward?' },
    { icon: 'FaEyeSlash', label: 'De-label:', text: 'judge each Key Result without its role name' },
    { icon: 'FaCompress', gold: true, label: 'Less is More:', text: 'maximum 4 Objectives, 3 Key Results each' }],
    notes: u.partNotes(5, 2) });
  await d.list({ title: 'Task 3 · The Prioritisation Matrix', fontSize: 26, rows: [
    { icon: 'FaBook', label: 'Shared definitions first:', text: 'what “high impact” and “high effort” mean here' },
    { icon: 'FaTh', label: 'One OKR at a time:', text: 'the group calls out its placement' },
    { icon: 'FaComments', label: 'Disagreements are the data:', text: 'do not rush to consensus' },
    { icon: 'FaCalendarCheck', gold: true, label: 'Close:', text: 'what must start in the first 90 days?' }],
    notes: u.partNotes(5, 3) });
  await portfolio(d, u, [
    { icon: 'FaPenFancy', title: 'What Has Shifted', text: 'Your key insight on how execution is planned.' },
    { icon: 'FaFlagCheckered', title: 'Commitment to Action', text: 'How you will contribute to the enterprise OKRs.' },
    { icon: 'FaBullseye', title: 'Development Priority', text: 'The capability or habit that would most strengthen you.' }], 3);
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Return to the opening question', text: 'Looking at the OKRs we have just built — have we answered the question? Where are the remaining gaps?',
    foot: 'The one thing I am committing to before our next session to make these OKRs real is…',
    notes: N(u.partNotes(5, 4, { content: false }),
      'Unit Summary (read aloud):\n\n' + SUM.map(s => `${s.arc} · ${s.title}\n${s.body}`).join('\n\n')) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
