// Unit 8 · Performance Measurement — facilitator deck with detailed presenter notes.
// Run: node unit08.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u08.json'), FH = R('unit3_m2_lens7_f.html'), PH = R('unit3_m2_lens7_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const gl = b => b.map(l => l.replace(/^◆ /, '')).join('\n');
const slice = (lines, a, b) => { const i = lines.findIndex(l => l.startsWith(a)); const j = b ? lines.findIndex((l, k) => k > i && l.startsWith(b)) : -1; return lines.slice(i, j < 0 ? lines.length : j).join('\n'); };

(async () => {
  const d = new Deck({ unit: 8, module: 3, moduleName: 'Influence', title: 'Performance Measurement' });
  const G = u.guide(), S3 = u.sec(3);

  await d.cover({ logo: LOGO, subtitle: 'Making execution visible, correctable and continuous',
    notes: N('UNIT 8 · PERFORMANCE MEASUREMENT\nModule 3 · Influence · Unit 8', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Strategy fails when progress is not consistently examined. This unit establishes the review discipline that keeps strategy execution visible, surfaces early warning signals, and converts performance data into organisational intelligence through the Review–Realign–Restore cycle.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW', 'Time: the facilitator file gives no minute timings for this unit; see the Timing watch point below.', G[1], G[2]) });

  // ── Section 1
  await div(d, 1);
  await d.prompt({ icon: 'FaEye', label: '1.1 · From activity to progress', text: 'Are we actually moving closer to our Success in Practice?',
    foot: 'From “What work was done?” to “What changed because of the work?”', notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · Four strategic purposes of measurement', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaEye', title: '01 · Creates Visibility', text: 'Where momentum is gained and where it stalls.' },
    { icon: 'FaUserCheck', title: '02 · Establishes Accountability', text: 'KPIs linked to enterprise OKRs make ownership visible.' },
    { icon: 'FaLightbulb', title: '03 · Enables Learning', text: 'Patterns in how work actually unfolds.' },
    { icon: 'FaRoute', title: '04 · Enables Course Correction', text: 'Intervene while progress is recoverable.' }],
    notes: u.partNotes(1, 1) });
  await d.cards({ title: '1.3 · The Review–Realign–Restore cycle', cols: 3, items: [
    { icon: 'FaSearch', title: 'Review', text: 'Establishing evidence-based visibility.' },
    { icon: 'FaStethoscope', title: 'Realign', text: 'Diagnosing the source of performance gaps.' },
    { icon: 'FaRedo', title: 'Restore', dark: true, text: 'Rebuilding momentum.' }],
    notes: u.partNotes(1, 2) });
  await d.cards({ title: '1.3 · The Accountability Loop: three root causes', cols: 3, items: [
    { icon: 'FaHeart', title: 'Lack of accountability', text: 'Reconnect purpose and ownership.' },
    { icon: 'FaTools', title: 'Lack of skill', text: 'Coaching, peer support, training, timeline.' },
    { icon: 'FaPuzzlePiece', title: 'Misfit or structural constraint', text: 'Structural alignment discussion.' }],
    band: 'Keep the performance conversation separate from the role conversation.',
    notes: N('1.3 · REALIGN — THE ACCOUNTABILITY LOOP', 'Content:\n' + slice(u.part(1, 2).content, 'Diagnosing the Source', 'Rebuilding Momentum'),
      'Guidance (Section 1): The key facilitation moment is when leaders understand that most performance gaps have a diagnosable cause — and that the three root causes (accountability, skill, structural misfit) require fundamentally different responses.') });

  // ── Section 2
  await div(d, 2);
  await d.prompt({ icon: 'FaTachometerAlt', label: '2.1 · Execution discipline: the real differentiator', text: 'Are we actually progressing?',
    foot: 'Examine progress, confront evidence honestly, adjust before small deviations become systemic failures.', notes: u.partNotes(2, 0) });
  await d.list({ title: '2.2 · Four consequences of weak review discipline', fontSize: 26, rows: [
    { icon: 'FaBellSlash', label: '01', text: 'Early Warning Signals Are Missed' },
    { icon: 'FaUserSlash', label: '02', text: 'Gradual Diffusion of Accountability' },
    { icon: 'FaBookDead', label: '03', text: 'Loss of Organisational Learning' },
    { icon: 'FaUserTie', label: '04', text: 'Erodes Leadership Credibility' }],
    notes: u.partNotes(2, 1) });
  await d.cards({ title: '2.3 · Three progress signals', cols: 3, items: [
    { icon: 'FaCheckCircle', title: 'Progress Confirmation', text: 'Reinforce what generated the progress.' },
    { icon: 'FaExclamationTriangle', title: 'Early Warning', text: 'Intervene while recovery is possible.' },
    { icon: 'FaExclamationCircle', title: 'Significant Gap', dark: true, text: 'Activate the Accountability Loop.' }],
    notes: u.partNotes(2, 2) });

  // ── Section 3
  await d.section({ num: 3, name: 'Extrapolating', anchor: 'Where', heading: S3.h2, outcomes: S3.slo,
    notes: N('SECTION 3 · EXTRAPOLATING — WHERE\n' + S3.h2 + '\n' + S3.sub, 'Section learning outcomes:\n' + S3.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'), S3.lead.guidance.map(gl)) });
  await d.cards({ title: 'Four fractures in performance measurement', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaArrowsAltH', title: 'Gap 01 · Horizontal Coordination', text: 'Reviews happen inside functions.' },
    { icon: 'FaBalanceScale', title: 'Gap 02 · Evidence Quality', text: 'Narrative replaces verifiable indicators.' },
    { icon: 'FaHeartbeat', title: 'Gap 03 · Review Rhythm Breakdown', text: 'Reviews become irregular.' },
    { icon: 'FaBrain', title: 'Gap 04 · Learning Suppression', text: 'Reviews focus only on evaluation.' }],
    notes: N('SECTION 3 · THE FOUR GAPS (select each gap in the file)', 'Content:\n' + S3.lead.content.join('\n')) });

  // ── Section 4
  await div(d, 4);
  await d.prompt({ icon: 'FaLink', label: '4.1 · The Collective Intelligence principle', text: 'Is the chain of execution across our functions holding together?',
    foot: 'Shifting from: “Is my function achieving its KPI/KR?”', notes: u.partNotes(4, 0) });
  await d.cards({ title: '4.2 · The Collective Intelligence Circle', cols: 3, items: [
    { icon: 'FaChartLine', title: 'Round 1', text: 'Collective Trajectory: % progress, evidence, momentum' },
    { icon: 'FaExclamationTriangle', title: 'Round 2', text: 'Early Warnings: one or two evidence-based signals' },
    { icon: 'FaLightbulb', title: 'Round 3', dark: true, text: 'Execution Learning: one key learning' }],
    band: 'Every contribution must be evidence-based.',
    notes: u.partNotes(4, 1) });
  await d.list({ title: '4.3 · The Synthesis Layer', fontSize: 26, rows: [
    { icon: 'FaStream', text: 'What execution pattern is emerging?' },
    { icon: 'FaRedo', text: 'Where are warning signals repeating?' },
    { icon: 'FaUnlink', text: 'Where are cross-functional dependencies breaking down?' },
    { icon: 'FaLink', text: 'Where is the expectations chain weakest?' },
    { icon: 'FaGavel', gold: true, text: 'What decision must we take now?' }],
    notes: u.partNotes(4, 2) });

  // ── Section 5
  await div(d, 5);
  await d.cards({ title: 'The Collective Intelligence Board', cols: 3, items: [
    { icon: 'FaChartLine', title: 'Zone 1', text: 'Collective Trajectory: “Where are we on execution?”' },
    { icon: 'FaExclamationTriangle', title: 'Zone 2', text: 'Early Warning Signals: “What is starting to break?”' },
    { icon: 'FaLightbulb', title: 'Zone 3', dark: true, text: 'Execution Learning: “What is execution teaching us?”' }],
    band: '“This board is where we make the system visible.”',
    notes: u.partNotes(5, 0) });
  await d.prompt({ icon: 'FaTheaterMasks', label: '5.1 · The Accountability Loop role play', text: 'Complaint resolution is still averaging 36 hours against a 12-hour target, six weeks from the deadline.',
    foot: 'Three roles: CXO · Report · Observer. Diagnose before prescribing.',
    notes: u.partNotes(5, 1, { content: false, extra: 'Content:\n' + slice(u.part(5, 1).content, '► Scenario', 'Accountability Loop Diagnosis') }) });
  await d.list({ title: 'Observer evaluation criteria', fontSize: 26, rows: [
    { icon: 'FaClipboardCheck', label: '01', text: 'Evidence was used in the discussion' },
    { icon: 'FaHandPeace', label: '02', text: 'Leader avoided blame and focused on diagnosis' },
    { icon: 'FaStethoscope', label: '03', text: 'Root cause was correctly identified' },
    { icon: 'FaFlagCheckered', label: '04', text: 'Clear corrective actions were agreed' }],
    notes: N('ACCOUNTABILITY LOOP DIAGNOSIS AND OBSERVER CRITERIA', 'Content:\n' + slice(u.part(5, 1).content, 'Accountability Loop Diagnosis'),
      'Participant file (5.1) — what participants record after the role play:\n' + (u.ppart(5, 1).prompts || []).map(x => '- ' + x).join('\n')) });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing', text: 'Name one KPI you own that has been consistently reviewed — and one that has been allowed to drift.',
    foot: 'Schedule its next review within five working days, with evidence submitted before the conversation.',
    notes: u.partNotes(5, 2) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
