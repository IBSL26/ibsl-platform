// Unit 4 · Direction Integrity (ABCV-MBT) — facilitator deck with detailed presenter notes.
// Run: node unit04.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N, divider } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u04.json'), FH = R('unit2_m1_lens3_f.html'), PH = R('unit2_m1_lens3_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const div = (d, i, x) => divider(d, u, i, x);
const gl = b => b.map(l => l.replace(/^◆ /, '')).join('\n');

(async () => {
  const d = new Deck({ unit: 4, module: 2, moduleName: 'Direction', title: 'Direction Integrity (ABCV-MBT)' });
  const G = u.guide();
  const S4 = u.sec(4), S5 = u.sec(5), P4 = u.P.sections[3], P5 = u.P.sections[4];

  await d.cover({ logo: LOGO, subtitle: 'Testing whether the chosen direction is strategically sound before execution begins',
    notes: N('UNIT 4 · DIRECTION INTEGRITY (ABCV-MBT)\nModule 2 · Direction · Unit 4', G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): Ensuring OKRs are anchored in customer reality, resilient to operational friction, and coherent with your organisation’s unique value before execution begins.',
      'Time: section timings in the facilitator file add up to 120–150 minutes (about 2 to 2.5 hours), plus breaks.') });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' }, { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' }, { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time by section (from the facilitator file):\n- Section 1 · Awareness — What: 20–25 minutes\n- Section 2 · Intelligence — Why: 20–25 minutes\n- Section 3 · Extrapolating — Where: 20–25 minutes\n- Section 4 · Integration — Collective: 40–50 minutes\n- Section 5 · Application — In Practice: 20–25 minutes', G[1], G[2]) });

  // ── Section 1
  await div(d, 1);
  await d.prompt({ label: '1.1 · The problem with well-written OKRs', text: 'Our OKRs look great on paper. Are they strategically sound?',
    foot: 'Most strategies fail because of unnamed conditions.',
    notes: u.partNotes(1, 0) });
  await d.cards({ title: '1.2 · The four ABCV integrity checkpoints', cols: 4, titleSize: 28, textSize: 24, items: [
    { icon: 'FaBullseye', title: 'Arena', text: 'Customer End Game' },
    { icon: 'FaRoad', title: 'Boundaries', text: 'Friction Architecture' },
    { icon: 'FaSearch', title: 'Competition', text: 'The True Landscape' },
    { icon: 'FaGem', title: 'Value Proposition', dark: true, text: 'Coherent Advantage' }],
    band: 'For every checkpoint, name the Must-Be-True condition.',
    notes: u.partNotes(1, 1) });

  // ── Section 2
  await div(d, 2);
  await d.cards({ title: '2.1 · The industry illusion and the arena shift', cols: 3, items: [
    { icon: 'FaTools', title: 'Functional', text: 'The actual task they need to finish.' },
    { icon: 'FaHeart', title: 'Emotional', text: 'How they want to feel while doing it.' },
    { icon: 'FaUsers', title: 'Social', text: 'How they want others to see them.' }],
    band: 'Industry categories were made for administrators.',
    notes: u.partNotes(2, 0) });
  await d.list({ title: '2.2 · Naming the Must-Be-Trues', fontSize: 26, rows: [
    { icon: 'FaBullseye', label: 'Arena:', text: 'a real customer end-game, or just pushing a product?' },
    { icon: 'FaRoad', label: 'Boundaries:', text: 'what regulations or internal frictions will push back?' },
    { icon: 'FaSearch', label: 'Competition:', text: 'who else is solving this problem?' },
    { icon: 'FaGem', label: 'Value Proposition:', text: 'does this goal make us more distinct?' }],
    notes: u.partNotes(2, 1) });

  // ── Section 3
  await div(d, 3);
  {
    const s = d.slide(); d.title(s, '3.1 · The executive hot zone: role-based blind spots');
    const roles = [['CEO', 'Boundaries'], ['CFO', 'Arena'], ['COO', 'Competition'], ['CHRO', 'Competition'], ['CTO', 'Arena'], ['CMO', 'Boundaries'], ['CCO', 'Value Prop'], ['CPO', 'Arena'], ['CSO', 'Boundaries']];
    T(s, 'What each role most often overlooks', { x: 0.6, y: 1.55, w: 12, h: 0.5, fontSize: 24, italic: true, color: C.muted });
    roles.forEach(([r, c], i) => {
      const x = 0.6 + (i % 3) * 4.1, y = 2.2 + Math.floor(i / 3) * 1.6;
      box(s, x, y, 3.85, 1.35, i % 2 ? C.tint : C.tint);
      T(s, [{ text: r, options: { bold: true, color: C.forest, fontFace: F.head, breakLine: true } }, { text: c }], { x: x + 0.25, y, w: 3.4, h: 1.35, fontSize: 26, valign: 'middle' });
    });
    s.addNotes(u.partNotes(3, 0));
  }

  // ── Section 4
  await d.section({ num: 4, name: 'Integration', anchor: 'Collective', heading: S4.h2, outcomes: S4.slo,
    notes: N('SECTION 4 · INTEGRATION — COLLECTIVE\n' + S4.h2 + '\n' + S4.sub, 'Section learning outcomes:\n' + S4.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'), gl(S4.lead.guidance[0])) });
  await d.prompt({ icon: 'FaHospital', label: 'Shared case study · Meridian Health Group', text: 'A premium specialist hospital group launches a digital-first virtual-care platform. Stress-test the direction before execution begins.',
    notes: N('SHARED CASE STUDY (participant file, Section 4 · ABCV–MBT Working Papers)',
      'Participant file introduction: ' + P4.lead.content.slice(0, 2).join(' '),
      'Team identity: participants enter a Team Name, their Executive Name and an Executive Role. “Adopt one C-suite role for the duration of this exercise. Your facilitator uses this to attribute your contribution consistently across the leadership team.”',
      'Case (read aloud): Meridian Health Group. A regional private-hospital group built its reputation on premium, in-person specialist care. Under margin pressure and the rapid rise of tele-health, the board has approved a strategy to launch a digital-first virtual-care platform aimed at younger, lower-acuity patients — while sustaining the premium specialist business that defines the brand. Leadership is confident in the financial model and the technology. As the executive team, your task is to stress-test this strategic direction through the four ABCV checkpoints before execution begins, and to name the Must-Be-True conditions the strategy is silently assuming.',
      'Note: the case study text sits in the participant file only.') });
  await d.list({ title: 'ABCV–MBT Working Papers: four steps', fontSize: 26, rows: [
    { icon: 'FaUser', label: 'Step 1 · Individual Working Paper:', text: 'up to three objectives, all four checkpoints' },
    { icon: 'FaUsers', label: 'Step 2 · Consensus & Synthesis:', text: 'top five priority MBT conditions' },
    { icon: 'FaUserCheck', label: 'Step 3 · Leadership Ownership:', text: 'a named owner for every condition' },
    { icon: 'FaHandsHelping', gold: true, label: 'Step 4 · Supporting Partners:', text: 'evidence, sources and timeline' }],
    notes: N('ABCV–MBT WORKING PAPERS · STEPS 1–4\nTime: Step 1 is individual and takes 15–20 minutes. Steps 2–4 are collective and take 20–30 minutes together.',
      S4.lead.guidance.slice(1).map(gl),
      'Participant file instructions by step:\nStep 1: Working from the shared case study above and in your executive role, select up to three of the organisation’s strategic objectives and apply all four ABCV checkpoints to each. Name one Must-Be-True condition per checkpoint — make it specific enough that someone could verify it. Work individually here; you will consolidate as a team in the next steps.\nStep 2: As a team, share one MBT condition from each checkpoint. Look for patterns together: which checkpoint recurs as the most challenging across the group? (Fields: Shared Themes · Areas of Disagreement · Top 5 Priority MBT Conditions (Team Consensus))\nStep 3: As a team, assign clear leadership ownership to each priority MBT condition. Every condition must have a named owner — shared ownership is no ownership.\nStep 4: As a team, identify the internal and external support needed to verify your priority MBT conditions, and agree a verification timeline. (Fields: Internal Partners Required · External Data or Partners Required · Verification Timeline)') });

  // ── Section 5
  await d.section({ num: 5, name: 'Application', anchor: 'In Practice', heading: S5.h2, outcomes: S5.slo,
    notes: N('SECTION 5 · APPLICATION — IN PRACTICE\n' + S5.h2 + '\n' + S5.sub, 'Section learning outcomes:\n' + S5.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'), S5.lead.guidance.map(gl)) });
  await d.cards({ title: 'Cause of Death: four mines', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaShip', title: 'Mine 1 · The Ghost Ship', text: 'Retention collapsed; the product never changed.' },
    { icon: 'FaCar', title: 'Mine 2 · The Ferrari in the Mud', text: 'Excellent system; under 30% consistent use.' },
    { icon: 'FaMobileAlt', title: 'Mine 3 · The Invisible Disruption', text: '#1 in satisfaction; revenue declining.' },
    { icon: 'FaMask', title: 'Mine 4 · The Identity Crisis', text: 'More work won; distinctiveness lost.' }],
    notes: N('CAUSE OF DEATH — MATCH THE BREAKDOWN\nScoring: 2 points per mine, maximum 8.',
      'Participant activity (participant file, Section 5): Each scenario below describes a real-world strategy that failed. Your task: identify the investigation question that would have exposed the failure, and the ABCV checkpoint it belongs to. Choose carefully — wrong answers detonate.',
      'Mine 1 — The Ghost Ship: ' + 'A SaaS platform achieved 85% retention in year one. By year three, churn reached 70%. Nothing in the product changed. Support tickets were low. The platform worked exactly as designed. Post-exit interviews revealed: customers had changed what they were trying to achieve — and the platform never followed.',
      'Mine 2 — The Ferrari in the Mud: A leading logistics firm invested R120m in a new digital operations platform. Eighteen months in, less than 30% of staff were using it consistently. Field teams had developed workarounds. Middle management had quietly reverted to spreadsheets. The system was technically excellent. The organisation was not designed to absorb it.',
      'Mine 3 — The Invisible Disruption: A financial advisory firm was ranked #1 in client satisfaction for four consecutive years. Then revenue began declining. No competitor had taken their clients. No scandal. No service failure. The problem: a fintech app was letting clients self-manage what the firm had always managed for them — and clients preferred it for 60% of use cases.',
      'Mine 4 — The Identity Crisis: A boutique consulting firm built its reputation on deep-sector expertise and bespoke strategy work. Under revenue pressure, they began accepting large implementation contracts — work that paid well but required different skills, different team profiles, and a different culture. Within two years, they won more work but lost their most experienced strategists and their distinctiveness with clients who valued exactly what they had been.',
      'The investigation questions participants choose from (each mine):\nQ1: What functional, emotional, and social outcome is the customer truly pursuing — and has it shifted?\nQ2: What internal or external friction is preventing strategy from delivering at scale?\nQ3: Who else is solving this problem — including those who don’t look like competitors?\nQ4: Does our distinctive value architecture still create coherent, defensible advantage?\nCheckpoint options: Arena · Boundaries · Competition · Value Proposition.',
      'Push participants to articulate their reasoning before selecting an answer.') });
  await d.list({ title: 'Answer key (facilitator only)', fontSize: 26, rows: [
    { icon: 'FaShip', label: 'Ghost Ship:', text: 'Q1 · Arena' },
    { icon: 'FaCar', label: 'Ferrari in the Mud:', text: 'Q2 · Boundaries' },
    { icon: 'FaMobileAlt', label: 'Invisible Disruption:', text: 'Q3 · Competition' },
    { icon: 'FaMask', label: 'Identity Crisis:', text: 'Q4 · Value Proposition' }],
    notes: u.partNotes(5, 0) });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Closing commitment', text: 'What is the one MBT condition your team is most likely to avoid naming? Why? And what will you do about it before the next strategic review?',
    notes: N(u.partNotes(5, 1),
      'Participant file (Section 5 · ✍ Closing Commitment): “What is one MBT condition your organisation is currently avoiding naming? Why? What will you do about it before your next strategic review?”',
      'Output (Facilitator Guide): a named owner and date.') });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
