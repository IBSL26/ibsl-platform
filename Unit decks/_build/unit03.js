// Unit 3 · SiP KISS Mapping & OKR Definition — facilitator deck, rebuilt October 2026 from the rebuilt Unit 3 pages.
// Run from Unit decks\_build:  node unit03.js "<output.pptx>" [logo.png]
// Then: add_reflection_slides.py (spec written by this script) and format_notes_u03.py; build_u03.sh runs all the steps.
// The reflection pictures come from shoot_reflections_u03.py. See rebuild_u03/README.md, "The deck".
//
// One slide for each part of the unit, with sub-slides (a, b, c…) only where a part needs them. Slide text is the page text,
// shortened; the presenter notes (u03_notes.js) carry the teaching. The data comes from rebuild_u03/u3_shared.js, the same
// arrays the participant and facilitator pages use, so the deck and the pages cannot drift apart.
const { Deck, C, F, T, box, badge } = require('./lib2');
const fs = require('fs');
const path = require('path');
const HERE = __dirname;
const [OUT, LOGO = [path.join(HERE, '..', '..', 'logo.png'), path.join(HERE, 'logo.png')].find(x => fs.existsSync(x))] = process.argv.slice(2);
if (!OUT) { console.error('usage: node unit03.js <output.pptx> [logo.png]'); process.exit(1); }
const INS = JSON.parse(fs.readFileSync(path.join(HERE, 'enrich', 'u03_rebuild.json'), 'utf8'));
const { n, used, D, KLO, SLOS, REFL, OPENING_Q, TEST4 } = require('./u03_notes.js')(INS);
const { KISS_DOMAINS: KD, HOT_ZONES: HZ, PM_CATS: PM, WORKED: WK } = D;

const SECTIONS = [
  { num: 1, name: 'Awareness', anchor: 'What', heading: 'What is KISS Framing & OKR Definition?' },
  { num: 2, name: 'Intelligence', anchor: 'Why', heading: 'Why the KISS-to-OKR Sequence Matters' },
  { num: 3, name: 'Extrapolating', anchor: 'Where', heading: 'Where do OKR Hot Zones Appear?' },
  { num: 4, name: 'Integration', anchor: 'Collective', heading: 'Building Collective Intelligence: From SiP to KISS to Enterprise OKRs' },
  { num: 5, name: 'Application', anchor: 'In Practice', heading: 'Strategy Airport: From Strategic Imagination to Operational Clearance' }];

(async () => {
  const d = new Deck({ unit: 3, module: 2, moduleName: 'Direction', title: 'SiP KISS Mapping & OKR Definition' });
  const div = k => d.section(Object.assign({}, SECTIONS[k - 1], { outcomes: SLOS[k], notes: n['s' + k] }));
  const band = (s, text) => { box(s, 0.6, 6.15, 12.13, 0.85, C.deep); T(s, text, { x: 0.9, y: 6.15, w: 11.6, h: 0.85, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); };

  // A list with an optional band at the foot (lib2's list has no band).
  async function rows(o) {
    const s = d.slide(); d.title(s, o.title);
    const k = o.rows.length, top = 1.65, avail = (o.band ? 4.35 : 5.35), rh = avail / k, ib = Math.min(0.7, rh * 0.7);
    for (let i = 0; i < k; i++) {
      const r = o.rows[i], y = top + i * rh;
      await badge(s, r.icon, 0.6, y + (rh - ib) / 2, ib, r.gold ? C.gold : C.forest, C.white);
      T(s, r.label ? [{ text: r.label + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: r.text || '' }] : r.text,
        { x: 0.6 + ib + 0.35, y, w: 12.13 - ib - 0.35, h: rh, fontSize: o.fontSize || 26, valign: 'middle' });
    }
    if (o.band) band(s, o.band);
    s.addNotes(o.notes);
  }

  // The Prioritisation Matrix (Impact × Effort). placed: {'High|Low': 2, …} puts an Objective number in a cell.
  function matrix(o) {
    const s = d.slide(); d.title(s, o.title);
    const X0 = 2.0, CW = 3.45, PX = 3.6, Y0 = 2.12, CH = o.legend ? 1.17 : 1.45, PY = o.legend ? 1.28 : 1.62;
        T(s, 'Impact', { x: 0.6, y: 1.55, w: 1.3, h: 0.5, fontSize: 24, bold: true, color: C.muted });
    ['Low effort', 'Medium effort', 'High effort'].forEach((e, k) => T(s, e, { x: X0 + k * PX, y: 1.55, w: CW, h: 0.5, fontSize: 24, bold: true, color: C.forest, align: 'center' }));
    ['High', 'Medium', 'Low'].forEach((im, r) => {
      T(s, im, { x: 0.6, y: Y0 + r * PY, w: 1.3, h: CH, fontSize: 24, bold: true, color: C.forest, valign: 'middle' });
      ['Low', 'Medium', 'High'].forEach((e, k) => {
        const c = PM.find(p => p.i === im && p.e === e), hot = im === 'High', x = X0 + k * PX, y = Y0 + r * PY, num = o.placed && o.placed[im + '|' + e];
        box(s, x, y, CW, CH, hot ? C.forest : C.tint);
        T(s, c.l, { x: x + 0.15, y, w: num ? CW - 0.95 : CW - 0.3, h: CH, fontSize: 24, bold: true, color: hot ? C.white : C.forest, align: num ? 'left' : 'center', valign: 'middle' });
        if (num) {
          s.addShape('ellipse', { x: x + CW - 0.7, y: y + (CH - 0.58) / 2, w: 0.58, h: 0.58, fill: { color: C.gold }, line: { color: C.gold } });
          T(s, String(num), { x: x + CW - 0.7, y: y + (CH - 0.58) / 2, w: 0.58, h: 0.58, fontSize: 24, bold: true, color: C.deep, align: 'center', valign: 'middle' });
        }
      });
    });
    if (o.legend) {
      box(s, 0.6, 6.02, 12.13, 0.98, C.deep);
      T(s, o.legend.map((t, k) => ({ text: t, options: { breakLine: k < o.legend.length - 1 } })), { x: 0.9, y: 6.02, w: 11.6, h: 0.98, fontSize: 24, italic: true, color: C.white, valign: 'middle' });
    }
    s.addNotes(o.notes);
  }

  // ── Front
  await d.cover({ logo: LOGO, subtitle: 'From Success in Practice to a focused, measurable execution architecture', notes: n.cover });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: KLO.map(t => ({ icon: 'FaCheck', text: t })), notes: n.klo });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: SECTIONS.map((x, k) => ({ icon: ['FaEye', 'FaLightbulb', 'FaMapMarkedAlt', 'FaUsers', 'FaClipboardCheck'][k], label: `Section ${x.num} · ${x.name}`, text: '— ' + x.anchor })), notes: n.journey });

  // ── Section 1 · Awareness — What
  await div(1);
  await d.prompt({ icon: 'FaQuoteLeft', label: '1.1 · Translating Success in Practice into Action', text: OPENING_Q, notes: n.p11 });
  await d.cards({ title: '1.2 · KISS: Keep · Improve · Start · Stop', cols: 4, titleSize: 30, textSize: 24, items: [
    { icon: 'FaShieldAlt', title: 'KEEP', text: 'Protect what is already working' },
    { icon: 'FaArrowUp', title: 'IMPROVE', text: 'Strengthen what is partially working' },
    { icon: 'FaPlay', title: 'START', text: 'Introduce what does not yet exist' },
    { icon: 'FaStop', title: 'STOP', dark: true, text: 'Eliminate what contradicts the SiP' }],
    band: 'Every KISS reflection must be anchored to the Success in Practice statements.', notes: n.p12 });
  await d.cards({ title: '1.3 · The KISS Reflection Table: Four SiP Domains', cols: 2, titleBeside: true, titleSize: 24, textSize: 24, iconSize: 0.6,
    items: KD.map((k, i) => ({ icon: ['FaSmile', 'FaCogs', 'FaUsers', 'FaChartLine'][i], title: k.label, text: k.anchor })), notes: n.p13 });
  await d.compare({ title: '1.4 · OKR Anatomy: Objectives & Key Results', cols: [
    { icon: 'FaFlag', title: 'Objectives', sub: 'Define strategic ambition', points: ['Qualitative and ambitious', 'Action-oriented and inspirational', 'Memorable: the T-shirt test'] },
    { icon: 'FaRuler', title: 'Key Results', sub: 'Define measurable progress', points: ['Verb of Change + Metric', 'From X to Y + By Deadline', '2–3 for each Objective'] }],
    band: 'Can you check it off a task list? If yes, it is a task.', notes: n.p14 });
  await d.list({ title: '1.5 · Six Steps: From KISS to Enterprise OKRs', fontSize: 26, rows: [
    { icon: 'FaLayerGroup', label: 'Step 1 · Find Themes', text: 'the 2–3 big shifts across the four SiP domains' },
    { icon: 'FaFlag', label: 'Step 2 · Inspiring Objectives', text: 'what will we be known for?' },
    { icon: 'FaRuler', label: 'Step 3 · Define Key Results', text: 'Verb + Metric + From X to Y + Deadline' },
    { icon: 'FaCheckDouble', label: 'Step 4 · Alignment Test', text: 'four questions before sharing' },
    { icon: 'FaCompress', label: 'Step 5 · Enterprise Priority', text: 'the Less is More Rule' },
    { icon: 'FaTh', label: 'Step 6 · Priority Matrix', text: 'Impact and Effort' }], notes: n.p15a });
  matrix({ title: '1.5 · Step 6: the Prioritisation Matrix', notes: n.p15b });

  // ── Section 2 · Intelligence — Why
  await div(2);
  await d.cards({ title: '2.1 · The Danger of Moving Too Fast', cols: 3, items: [
    { icon: 'FaBullseye', title: 'Disconnected Targets', text: 'Numbers are set while the hurdles go unacknowledged.' },
    { icon: 'FaRandom', title: 'Fragmented Efforts', text: 'Functions row in different directions.' },
    { icon: 'FaRunning', title: 'The Activity Trap', text: 'Busyness is measured because outcomes are hard to prove.' }],
    band: 'The organisation starts measuring the finish line before it has mapped the terrain.', notes: n.p21 });
  await d.cards({ title: '2.2 · The Strategy2Results® Sequence', cols: 3, items: [
    { icon: 'FaMountain', title: 'Success in Practice', text: 'The dream of where the organisation wants to be.' },
    { icon: 'FaFilter', title: 'KISS', text: 'The honest look at the changes required to get there.' },
    { icon: 'FaCompass', title: 'OKRs', dark: true, text: 'The execution compass.' }],
    band: 'At which point in this sequence does our organisation typically enter?', notes: n.p22a });
  {
    const s = d.slide(true);
    await badge(s, 'FaQuoteLeft', 0.8, 1.0, 1.2, C.gold, C.deep);
    T(s, '2.2 · Worked Example: the SiP Statement', { x: 2.3, y: 1.2, w: 10, h: 0.7, fontSize: 26, bold: true, color: C.gold });
    T(s, WK.sip, { x: 2.3, y: 2.05, w: 10.3, h: 4.1, fontSize: 28, fontFace: F.head, italic: true, color: C.white, valign: 'top' });
    T(s, 'A client services company', { x: 2.3, y: 6.3, w: 10.3, h: 0.6, fontSize: 24, color: C.paleText });
    s.addNotes(n.p22b);
  }
  await d.cards({ title: '2.2 · Worked Example: the KISS Table', cols: 4, titleSize: 30, textSize: 24, items: [
    { icon: 'FaShieldAlt', title: 'KEEP', text: WK.kiss[0].keep },
    { icon: 'FaArrowUp', title: 'IMPROVE', text: WK.kiss[0].improve },
    { icon: 'FaPlay', title: 'START', text: WK.kiss[0].start },
    { icon: 'FaStop', title: 'STOP', dark: true, text: WK.kiss[0].stop }],
    band: 'SiP domain shown: Customer Experience & Value.', notes: n.p22k });
  await d.list({ title: '2.2 · Worked Example: Steps 1 and 2', fontSize: 24,
    rows: WK.items.map((o, k) => ({ icon: ['FaSmile', 'FaBolt', 'FaUsers', 'FaChartLine', 'FaHandshake'][k], label: `${k + 1} · ${o.theme}:`, text: o.obj })), notes: n.p22c });
  await d.compare({ title: '2.2 · Worked Example: Step 3', cols: [0, 1].map(k => (
    { icon: 'FaRuler', title: 'Objective ' + (k + 1), sub: WK.items[k].theme, points: [WK.items[k].krs[0], WK.items[k].krs[1], 'Roles: ' + WK.items[k].roles] })),
    notes: n.p22d });
  await d.compare({ title: '2.2 · Worked Example: Step 4', cols: [
    { icon: 'FaCheckDouble', title: 'Alignment Test', sub: 'Four questions', points: ['Closer to the shared SiP vision?', 'A win for the whole organisation?', 'Visibly improves culture, operations or value creation?', 'Clear accountability?'] },
    { icon: 'FaFlag', title: 'Result', sub: 'Output of Step 4', points: [`Objectives 1 to ${WK.items.length}: 4 of 4`, `${WK.items.length} OKRs go forward to Step 5`, `One draft from one function: ${WK.failed.score} of 4`, 'The draft returns to Step 2'] }],
    notes: n.p22t });
  await rows({ title: '2.2 · Worked Example: Step 5', fontSize: 24,
    rows: WK.items.map((o, k) => ({ icon: o.pri ? 'FaCheck' : 'FaHourglassHalf', gold: !o.pri, label: `${k + 1} · ${o.theme}`, text: `${o.votes} ${o.votes === 1 ? 'vote' : 'votes'} · ${o.pri ? 'enterprise priority' : 'released for this cycle'}` })),
    band: 'No more than 4 Enterprise Objectives: five passed Step 4, four go forward to Step 6.', notes: n.p22v });
  matrix({ title: '2.2 · Worked Example: Step 6', notes: n.p22e,
    placed: Object.fromEntries(WK.items.map((o, k) => [o.impact + '|' + o.effort, k + 1]).filter((_, k) => WK.items[k].pri)),
    legend: ['1 Customer responsiveness · 2 Execution speed', '3 Collaboration culture · 4 Value creation'] });

  // ── Section 3 · Extrapolating — Where
  await div(3);
  await rows({ title: '3.1a · Natural OKR Emphasis: four tendencies', fontSize: 24, rows: [
    { icon: 'FaHandshake', label: 'Commercial leaders', text: 'Customer Experience & Value · Enterprise Value Creation' },
    { icon: 'FaCogs', label: 'Operational leaders', text: 'Operational Capability & Execution Rhythm · Enterprise Value Creation' },
    { icon: 'FaUsers', label: 'People leaders', text: 'People & Culture Dynamics · Operational Capability & Execution Rhythm' },
    { icon: 'FaCoins', label: 'Financial leaders', text: 'Enterprise Value Creation · Operational Capability & Execution Rhythm' }],
    band: 'Unexamined, these perspectives turn OKRs into functional scorecards.', notes: n.p31a });
  await rows({ title: '3.1b · Natural OKR Emphasis: four execution risks', fontSize: 26, rows: [
    { icon: 'FaRandom', text: 'Competing definitions of success across functions' },
    { icon: 'FaPuzzlePiece', text: 'Fragmented measurement systems that cannot be integrated' },
    { icon: 'FaCog', text: 'Functional optimisation that stalls enterprise progress' },
    { icon: 'FaHourglassHalf', text: 'Slow decision-making due to misaligned incentives' }],
    band: 'Recognising these patterns lets the team build a balanced execution system.', notes: n.p31b });
  {
    const h = HZ.find(x => x.role === 'CEO');
    await d.cards({ title: '3.1c · A Hot Zone Card: the CEO', cols: 2, titleBeside: true, titleSize: 24, textSize: 24, iconSize: 0.6, items: [
      { icon: 'FaEye', title: 'Dominant Future Realities', text: h.top2 },
      { icon: 'FaBullseye', title: 'Natural OKR Emphasis', text: h.emphasis },
      { icon: 'FaFire', title: 'Typical Hot Zone', dark: true, text: h.hot },
      { icon: 'FaQuestion', title: 'Alignment Question', dark: true, text: h.align }], notes: n.p31c });
  }
  {
    const s = d.slide(); d.title(s, '3.1d · The Matching Exercise');
    box(s, 0.6, 1.65, 12.13, 1.9, C.forest);
    T(s, 'For each role, match its Typical Hot Zone and its Alignment Question.', { x: 0.9, y: 1.65, w: 11.6, h: 1.9, fontSize: 28, italic: true, color: C.white, valign: 'middle' });
    HZ.forEach((h, i) => {
      const x = 0.6 + (i % 5) * 2.465, y = 4.0 + Math.floor(i / 5) * 1.2;
      box(s, x, y, 2.2, 0.95, C.tint);
      T(s, h.role, { x, y, w: 2.2, h: 0.95, fontSize: 28, bold: true, color: C.forest, align: 'center', valign: 'middle' });
    });
    T(s, 'Individual work', { x: 0.6, y: 6.45, w: 12.13, h: 0.5, fontSize: 24, bold: true, color: C.muted });
    s.addNotes(n.p31d);
  }

  // ── Section 4 · Integration — Collective
  await div(4);
  await d.list({ title: '4.1a · Translating SiP to KISS: how the group works', fontSize: 26, rows: [
    { icon: 'FaUsers', label: 'Agree:', text: 'the group agrees each entry' },
    { icon: 'FaPenFancy', label: 'Scribe:', text: 'one member types the agreed wording' },
    { icon: 'FaLaptop', label: 'Own page:', text: 'every member types the agreed entries, in the session or after it' },
    { icon: 'FaCheck', gold: true, label: 'Confirm:', text: 'each output, once it says what the group means' }], notes: n.p41a });
  await d.list({ title: '4.1b · Translating SiP to KISS', fontSize: 26, rows: [
    { icon: 'FaBookOpen', label: 'Read', text: 'your group’s four SiP statements' },
    { icon: 'FaFilter', label: 'Answer', text: 'the four KISS questions for each SiP domain' },
    { icon: 'FaAnchor', label: 'Anchor', text: 'every entry to the SiP' },
    { icon: 'FaCompress', label: 'Select', text: '3–4 items for each KISS element' },
    { icon: 'FaCheck', gold: true, label: 'Confirm', text: 'the KISS map' }], notes: n.p41b });
  await d.list({ title: '4.2a · Translating KISS to OKRs: The Six Steps', fontSize: 26, rows: [
    { icon: 'FaLayerGroup', label: '1 · Find Themes', text: 'up to six, from the confirmed KISS map' },
    { icon: 'FaFlag', label: '2 · Inspiring Objectives', text: 'one Objective for each theme' },
    { icon: 'FaRuler', label: '3 · Define Key Results', text: 'two or three, with the contributing roles' },
    { icon: 'FaCheckDouble', label: '4 · Alignment Test', text: 'four questions, answered aloud' },
    { icon: 'FaCompress', label: '5 · Enterprise Priority', text: 'no more than four Objectives' },
    { icon: 'FaTh', label: '6 · Priority Matrix', text: 'each priority placed by Impact and Effort' }], notes: n.p42a });
  await d.cards({ title: '4.2b · Three Confirmed Outputs', cols: 3, items: [
    { icon: 'FaMap', title: 'KISS Map', text: 'Provides the evidence' },
    { icon: 'FaCompress', title: 'Enterprise Priorities', text: 'Concentrate the energy' },
    { icon: 'FaCompass', title: 'Enterprise OKRs', dark: true, text: 'Make progress measurable' }],
    band: 'The three confirmed outputs feed the team’s Capstone Blueprint.', notes: n.p42b });

  // ── Section 5 · Application — In Practice
  await div(5);
  await d.cards({ title: '5.1 · Strategy Airport', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, items: [
    { icon: 'FaSuitcase', title: 'Gate 1 · Baggage Check', text: 'KISS mapping: what must the company keep, improve, start and stop?' },
    { icon: 'FaPlaneDeparture', title: 'Gate 2 · Flight Plan', dark: true, text: 'OKR construction: one KISS theme becomes an Objective and two Key Results.' }],
    band: 'The case: a medical health company. One learning round.', notes: n.p51 });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Return to the opening question', text: OPENING_Q,
    foot: 'The one thing I am committing to before our next session to make these OKRs real is…', notes: n.summary });

  if (used.size !== Object.keys(INS).length) throw new Error('insights not all used: ' + Object.keys(INS).filter(k => !used.has(k)).join(', '));
  await d.save(OUT);

  // Spec for add_reflection_slides.py: one "Section N Reflections" slide after the last content slide of Sections 1, 2 and 3.
  const spec = { title_model: 'Key learning outcomes', slides: [
    { title: 'Section 1 Reflections', after: '1.5 · Step 6', notes: n.ref1, pictures: [{ part: '1.4', file: 'ref_1.4.png', alt: 'Reflection 1.4: ' + REFL['1.4'] }] },
    { title: 'Section 2 Reflections', after: '2.2 · Worked Example: Step 6', notes: n.ref2, pictures: [{ part: '2.2', file: 'ref_2.2.png', alt: 'Reflection 2.2: ' + REFL['2.2'] }] },
    { title: 'Section 3 Reflections', after: '3.1d', notes: n.ref3, pictures: [{ part: '3.1', file: 'ref_3.1.png', alt: 'Reflection 3.1: ' + REFL['3.1'] }] }] };
  fs.mkdirSync(path.join(HERE, 'reflections', 'u03'), { recursive: true });
  fs.writeFileSync(path.join(HERE, 'reflections', 'u03', 'spec.json'), JSON.stringify(spec, null, 1));
  console.log('saved', OUT, '· insights used:', used.size, '· TEST4 questions:', TEST4.length);
})().catch(e => { console.error(e); process.exit(1); });
