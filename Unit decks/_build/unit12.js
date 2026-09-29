// Unit 12 · Sustaining Performance — facilitator deck with detailed presenter notes.
// Run: node unit12.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u12.json'), FH = R('unit4_m2_lens11_f.html'), PH = R('unit4_m2_lens11_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const slice = (lines, a, b) => { const i = lines.findIndex(l => l.startsWith(a)); const j = b ? lines.findIndex((l, k) => k > i && l.startsWith(b)) : -1; return lines.slice(i, j < 0 ? lines.length : j).join('\n'); };
const NOTIME = 'Time: the facilitator file gives no minute timings for this unit.';
const SEP = '\n\n———\n\n';
const gl = b => b.map(l => l.replace(/^◆ /, '')).join('\n');

(async () => {
  const d = new Deck({ unit: 12, module: 4, moduleName: 'Grounding', title: 'Sustaining Performance' });
  const G = u.guide(), S4 = u.sec(4);
  const X51 = u.part(5, 0).content;

  await d.cover({ logo: LOGO, subtitle: 'Sustained performance is the continuous navigation of five forces that never stop moving',
    notes: N('UNIT 12 · SUSTAINING PERFORMANCE\nModule 4 · Grounding · Unit 12 · The final unit of the S2R® programme', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Sustained performance is the continuous navigation of five forces that never stop moving. This unit gives leaders the causal understanding and the navigation architecture to sustain performance — across industries, in daily execution, permanently.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW', NOTIME, 'Session structure (facilitator file):\n' + u.part(0, 0).content.join('\n'), G[1], G[2]) });

  // ── Section 1
  await div(d, 1);
  await d.prompt({ icon: 'FaCompass', label: '1.1 · The navigation premise', text: 'The forces in your operating environment never stop moving.',
    foot: 'Performance Gravity is what happens when forces move and the organisation does not move with them.', notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · Three mechanisms of Performance Gravity', cols: 3, items: [
    { icon: 'FaForward', title: 'Momentum Illusion', text: 'Competitive + Disruptive forces' },
    { icon: 'FaLayerGroup', title: 'Complexity Creep', text: 'Macro-environmental forces' },
    { icon: 'FaUndo', title: 'Execution Regression', dark: true, text: 'Internal forces' }],
    band: 'Each mechanism is the consequence of a force category going unnavigated.',
    notes: u.partNotes(1, 1) });
  await d.list({ title: '1.3 · KISS: the four navigation disciplines', fontSize: 26, rows: [
    { icon: 'FaShieldAlt', label: 'K · Keep', text: 'what is working and must be protected' },
    { icon: 'FaSlidersH', label: 'I · Improve', text: 'what has shifted and needs recalibration' },
    { icon: 'FaStopCircle', label: 'S · Stop', text: 'what is harming performance' },
    { icon: 'FaPlayCircle', gold: true, label: 'S · Start', text: 'what the next level of performance requires' }],
    notes: u.partNotes(1, 2) });

  // ── Section 2
  await div(d, 2);
  await d.list({ title: '2.1 · The five forces, unnavigated', fontSize: 24, rows: [
    { icon: 'FaChessKnight', label: 'Competitive + Disruptive', text: '→ Momentum Illusion' },
    { icon: 'FaGlobeAfrica', label: 'Macro-Environmental', text: '→ Complexity Creep' },
    { icon: 'FaUsers', label: 'Social + Environmental', text: '→ Legitimacy Erosion' },
    { icon: 'FaBuilding', label: 'Internal', text: '→ Execution Regression' },
    { icon: 'FaExclamationCircle', gold: true, label: 'All five unnavigated', text: '→ Success Inertia' }],
    notes: u.partNotes(2, 0) });
  await d.prompt({ icon: 'FaProjectDiagram', label: '2.2 · The causal map', text: 'Which row describes your organisation’s most urgent navigation challenge right now?',
    foot: 'Success Inertia: the organisation is positioned for an environment that no longer exists.', notes: u.partNotes(2, 1) });

  // ── Section 3
  await div(d, 3);
  {
    const { C, F, T, box } = require('./lib2');
    const s = d.slide(); d.title(s, '3.1 · The Alignment Brigade: ten domains');
    const roles = [['CEO', 'Strategic Coherence'], ['CFO', 'Capital Discipline'], ['COO', 'Execution Cadence'], ['CHRO', 'Organisational Health'], ['CTO/CIO', 'Technology Enablement'],
      ['CMO', 'Market Intelligence'], ['CCO', 'Revenue Conversion'], ['CPO', 'Supply Resilience'], ['CRO', 'Risk Intelligence'], ['CSO', 'Strategy Translation']];
    roles.forEach(([r, c], i) => {
      const x = 0.6 + (i % 2) * 6.15, y = 1.7 + Math.floor(i / 2) * 1.05;
      box(s, x, y, 5.95, 0.9, C.tint);
      T(s, [{ text: r + '   ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: c }], { x: x + 0.25, y, w: 5.5, h: 0.9, fontSize: 26, valign: 'middle' });
    });
    s.addNotes(u.partNotes(3, 0));
  }
  await d.cards({ title: '3.2 · ABCV as the navigation diagnostic', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaBullseye', title: 'A · Arena', text: 'Has the customer end-game shifted?' },
    { icon: 'FaBorderAll', title: 'B · Boundaries', text: 'Have the constraints changed?' },
    { icon: 'FaChessKnight', title: 'C · Competition', text: 'Has the alternative set changed?' },
    { icon: 'FaGem', title: 'V · Value Proposition', text: 'Is the edge still holding?' }],
    notes: u.partNotes(3, 1) });
  await d.list({ title: '3.3 · The navigation chain', fontSize: 26, rows: [
    { icon: 'FaSatelliteDish', label: '1', text: 'Detect the force movement' },
    { icon: 'FaSearch', label: '2', text: 'Run the ABCV diagnostic' },
    { icon: 'FaUnlink', label: '3', text: 'Identify the invalidated assumption' },
    { icon: 'FaSlidersH', gold: true, label: '4', text: 'Activate KISS' }],
    notes: u.partNotes(3, 2, { extra: 'Guidance (Section 3): Walk through the chain once as a group using a real example from the room before the Application exercise.' }) });

  // ── Section 4
  await d.section({ num: 4, name: 'Integration', anchor: 'Collective', heading: S4.h2, outcomes: S4.slo,
    notes: N('SECTION 4 · INTEGRATION — COLLECTIVE\n' + S4.h2 + '\n' + S4.sub, 'Section learning outcomes:\n' + S4.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'), S4.lead.guidance.map(gl),
      'The four instruments are in the notes of the next slide.') });
  await d.cards({ title: 'The S2R® Collective Intelligence Review', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaCogs', title: 'ESRG Scanner', text: 'Diagnose the operating conditions' },
    { icon: 'FaCompass', title: 'Enterprise COMPASS', text: 'Align the enterprise' },
    { icon: 'FaSlidersH', title: 'KISS Reflection', text: 'Reinforce the navigation discipline' },
    { icon: 'FaThermometerHalf', title: 'Health Thermometer', text: 'Monitor the behavioural climate' }],
    band: 'Name a date, a lead for each conversation and a format for the output.',
    notes: N('THE S2R® COLLECTIVE INTELLIGENCE REVIEW (select each instrument in the file)', 'Content:\n' + S4.lead.content.join('\n'),
      'Guidance (Section 4): The quarterly commitment is the output of this section. Before leaving the Integration section, the group should name a date, a lead for each of the four conversations, and a format for capturing and acting on the output. If no date is named, the Review will not happen.') });

  // ── Section 5
  await div(d, 5);
  await d.cards({ title: '5.1 · The navigation chain scenarios', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaUndo', title: '1 · The COO’s Execution Rhythm', text: 'Internal · Execution Regression' },
    { icon: 'FaLayerGroup', title: '2 · The CFO’s Legacy Budget', text: 'Macro-Environmental · Complexity Creep' },
    { icon: 'FaForward', title: '3 · The CMO’s Comfortable Intelligence', text: 'Competitive + Disruptive · Momentum Illusion' },
    { icon: 'FaBalanceScale', title: '4 · The CRO’s Legitimacy Gap', text: 'Social + Environmental · Legitimacy Erosion' }],
    notes: N('5.1 — PART 1 · THE NAVIGATION CHAIN SCENARIOS (choose the closest to your reality)',
      'Guidance (Application): Push back if a leader jumps to KISS: “Before you name the KISS response — which MBT condition has been invalidated? Which ABCV letter?” Let leaders choose the scenario on the basis of recognition.',
      'Content:\n' + X51.join('\n')) });
  await d.list({ title: '5.2 · The navigation commitment', fontSize: 26, rows: [
    { icon: 'FaSatelliteDish', label: 'Q1', text: 'Which force is moving, producing which mechanism?' },
    { icon: 'FaSearch', label: 'Q2', text: 'Which ABCV MBT condition is most under threat?' },
    { icon: 'FaCalendarCheck', gold: true, label: 'Q3', text: 'One KISS decision, named and dated, in thirty days' }],
    notes: u.partNotes(5, 1) });
  await d.prompt({ icon: 'FaMountain', label: 'Unit Summary · Programme close', text: 'You came into this programme with a strategy. You leave with a navigation discipline.',
    foot: 'Keep climbing.', notes: u.partNotes(5, 2) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
