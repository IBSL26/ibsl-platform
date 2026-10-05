// Unit 2 · Strategy Visioning & Success in Practice (SiP) — facilitator deck, REBUILT October 2026
// from the rebuilt unit files (Strategy Architecture · Strategy Intent Statement · Success in Practice).
//
// Run:  node unit02.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
// Then: python3 add_reflection_slides.py "<output.pptx>" reflections/u02/spec.json "<final.pptx>"
//       (this script writes reflections/u02/spec.json; the pictures ref_*.png are shot from the participant page)
//
// Presenter notes come from u02_notes.js, u02_notes_b.js and u02_notes_c.js. The journal insights sit inside the notes
// (enrich/u02_rebuild.json). Do NOT run source_notes.py, enrich.py or embed_insights.py on this deck: the manuscript
// detail and the insights are already in place, and those scripts are keyed to the old slide numbers.
// LAST STEP (October 2026): after add_reflection_slides.py, run format_notes.py. It takes Carol's own copy of the deck as
// the master (her slides, and her notes on slides 1 to 4), and puts the generated notes into slides 5 onwards with
// bold headings:  python3 format_notes.py "<the deck in Unit decks>" build2.pptx "<deck out>"
// Then python3 lint_notes.py "<deck out>" 5 (checks the notes against Carol's standing rules).
const fs = require('fs');
const path = require('path');
const { Deck, C, F, T, box, badge } = require('./lib2');
const { Unit, N } = require('./kit');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u02.json'), FH = R('unit2_m1_lens1_f.html'), PH = R('unit2_m1_lens1_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);
const INS = JSON.parse(fs.readFileSync(path.join(__dirname, 'enrich', 'u02_rebuild.json'), 'utf8'));
const ctx = require('./u02_notes')(u, INS);
require('./u02_notes_b')(ctx);
require('./u02_notes_c')(ctx);
const n = ctx.n;
const { CONCEPTS, W1H, ARCH, DIMS, FLAMS, EL, SIPD, ROLES, GROUPS } = ctx.data;

async function divider(d, i, notes) {
  const s = u.sec(i), m = /Section (\d+) · (\S+) — (.+)/.exec(s.label);
  await d.section({ num: +m[1], name: m[2], anchor: m[3], heading: s.h2, outcomes: s.slo, notes });
}
// list rows in the upper area with a quotation band underneath
async function listBand(d, o) {
  const s = d.slide(); d.title(s, o.title);
  const rows = o.rows, top = 1.65, avail = 4.3, rh = avail / rows.length, ib = Math.min(0.7, rh * 0.7);
  for (let i = 0; i < rows.length; i++) {
    const r = rows[i], y = top + i * rh;
    await badge(s, r.icon, 0.6, y + (rh - ib) / 2, ib, r.gold ? C.gold : C.forest, C.white);
    T(s, [{ text: r.label + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: r.text || '' }],
      { x: 0.6 + ib + 0.35, y, w: 12.13 - ib - 0.35, h: rh, fontSize: o.fontSize || 24, valign: 'middle' });
  }
  box(s, 0.6, 6.15, 12.13, 0.85, C.deep);
  T(s, o.band, { x: 0.9, y: 6.15, w: 11.6, h: 0.85, fontSize: 24, italic: true, color: C.white, valign: 'middle' });
  s.addNotes(o.notes);
}

(async () => {
  const d = new Deck({ unit: 2, module: 2, moduleName: 'Direction', title: 'Strategy Visioning & Success in Practice (SiP)' });

  await d.cover({ logo: LOGO, subtitle: 'Strategy Architecture · Strategy Intent Statement · Success in Practice', notes: n.cover });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })), notes: n.klo });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' },
    { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' },
    { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }], notes: n.journey });

  // ── Section 1 · Awareness — What
  await divider(d, 1, n.s1);
  await d.prompt({ label: 'Opening the session', text: 'Write your definition of strategy in one sentence — right now, without consulting anyone.', notes: n.open });
  await d.prompt({ icon: 'FaQuoteLeft', label: '1.1a · Define the Strategy Architecture',
    text: 'Strategy is the output of iterative thinking, logic and process to determine what, why, how and when an organisation creates, delivers and sustains value to its stakeholders while navigating the forces within its operating environment.', notes: n.def });
  await d.list({ title: '1.1b · Every word carries strategic weight', fontSize: 24, rows: CONCEPTS.map(c => ({ icon: 'FaKey', label: c.badge, text: c.name })), notes: n.concepts });
  await d.cards({ title: '1.2 · Defining the Strategy Intent Statement', cols: 4, titleSize: 28, textSize: 24,
    items: W1H.map((w, k) => ({ icon: ['FaBullseye', 'FaHeart', 'FaCogs', 'FaClock'][k], title: w.name, text: w.sub })),
    band: 'Four dimensions, crystallised into one clear Strategy Intent Statement.', notes: n.intent });
  await d.cards({ title: '1.3 · SiP: From Intent to Future Reality', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6,
    items: [
      { icon: 'FaSmile', title: 'D1 · Customer Experience & Value', text: 'What customers experience' },
      { icon: 'FaCogs', title: 'D2 · Operational Capability & Execution Rhythm', text: 'How the organisation operates' },
      { icon: 'FaUsers', title: 'D3 · People & Culture Dynamics', text: 'How people decide and behave' },
      { icon: 'FaChartLine', title: 'D4 · Enterprise Value Creation', text: 'How the organisation benefits' }],
    band: '“If our Strategy Intent is successful, what should we see in practice?”', notes: n.sip });

  // ── Section 2 · Intelligence — Why
  await divider(d, 2, n.s2);
  await d.cards({ title: '2.1 · Intent & SiP in the S2R® Architecture', cols: 3, items: [
    { icon: 'FaCompass', title: 'Strategic Alignment', text: 'People and functions oriented around the same ambition and picture of success' },
    { icon: 'FaFilter', title: 'Decision Filter', text: 'A basis for deciding which choices, opportunities and investments support the strategy' },
    { icon: 'FaLink', title: 'Execution Coherence', text: 'Individual contributions connect to produce the enterprise outcome' }],
    band: 'The Intent anchors the ambition. SiP anchors the reality it is intended to produce.', notes: n.fn });
  const FN = [
    { band: 'Strategy fragments when leaders interpret the ambition differently.',
      si: ['Shared understanding of the ambition and the choices that define it', 'Leaders anchored to the same WHAT, WHY, HOW and WHEN'],
      sip: ['A shared picture of what successful realisation looks like', 'Different contributions, the same organisational reality'] },
    { band: 'What tells us whether a new initiative belongs in our strategy?',
      si: ['The test of strategic fit', 'Is this choice consistent with our ambition and the choices already made?'],
      sip: ['The test of strategic contribution', 'Does this choice move us closer to the success we have defined?'] },
    { band: 'Each part can perform well while the enterprise outcome is missed.',
      si: ['The common strategic anchor', 'Each function reads its mandate in relation to the enterprise ambition'],
      sip: ['What the combined contributions must produce', 'Functions see the outcome they collectively enable'] }];
  for (let k = 0; k < 3; k++) {
    await d.compare({ title: `${ARCH[k].n} · ${ARCH[k].fn}`, cols: [
      { icon: 'FaBullseye', title: 'Strategy Intent', sub: 'Anchors the ambition', points: FN[k].si },
      { icon: 'FaEye', title: 'SiP', sub: 'Anchors the reality', points: FN[k].sip }], band: FN[k].band, notes: n['fn' + (k + 1)] });
  }

  // ── Section 3 · Extrapolating — Where
  await divider(d, 3, n.s3);
  await listBand(d, { title: '3.1a · SiP Observable Indicators', rows: [
    { icon: 'FaSmile', label: 'D1 · Customer Experience & Value', text: 'Connection · Access · Results · Effort' },
    { icon: 'FaCogs', label: 'D2 · Operational Capability', text: 'Priority Clarity · Decision Flow · Coordination · Delivery Rhythm' },
    { icon: 'FaUsers', label: 'D3 · People & Culture', text: 'Collaboration · Ownership · Alignment · Dialogue Quality' },
    { icon: 'FaChartLine', label: 'D4 · Enterprise Value', text: 'Growth · Profitability · Market Position · Value Durability' }],
    band: 'Every indicator has two positions: When Working and Signal of Absence.', notes: n.ind });
  const DOM = [
    { t: '3.1b · D1 Customer Experience & Value', icons: ['FaHandshake', 'FaDoorOpen', 'FaTrophy', 'FaFeatherAlt'],
      x: ['Customers feel understood, respected and supported.', 'Quick, easy, reliable interaction through preferred channels.', 'Solutions that solve the problem and improve outcomes.', 'Simple, predictable processes. Minimal customer effort.'] },
    { t: '3.1c · D2 Operational Capability', icons: ['FaListOl', 'FaRandom', 'FaProjectDiagram', 'FaSyncAlt'],
      x: ['Priorities are explicit, stable and understood in every function.', 'Right level, right information, right speed.', 'Smooth hand-offs. Unambiguous responsibilities.', 'A predictable cadence. Consistent, reliable delivery.'] },
    { t: '3.1d · D3 People & Culture', icons: ['FaPeopleCarry', 'FaUserCheck', 'FaCompass', 'FaComments'],
      x: ['People work across boundaries without being directed to.', 'Leaders and teams carry outcomes.', 'Daily actions connect to the enterprise strategy.', 'Honest challenge before decisions are made.'] },
    { t: '3.1e · D4 Enterprise Value', icons: ['FaChartLine', 'FaCoins', 'FaFlag', 'FaShieldAlt'],
      x: ['Growth is traceable to specific strategic choices.', 'Margin reflects deliberate value positioning.', 'The competitive position the strategic intent described.', 'The conditions of success are actively reinvested in.'] }];
  for (let k = 0; k < 4; k++) {
    await d.cards({ title: DOM[k].t, cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6,
      items: DIMS[k].inds.map((ind, j) => ({ icon: DOM[k].icons[j], title: ind.name, text: DOM[k].x[j] })), notes: n['d' + (k + 1)] });
  }
  await d.cards({ title: '3.2a · SiP Flammables: the balance test', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6,
    items: FLAMS.map((f, k) => ({ icon: 'FaFire', title: f.dim, text: ['Reads as a marketing aspiration', 'Reads as a process optimisation plan', 'Reads as an organisational development narrative', 'Reads as a financial target'][k] })), notes: n.flam });
  const FL = [
    { signs: ['Every statement begins and ends with the customer', 'No capability, decision right or delivery rhythm is named', 'Growth is assumed to follow satisfaction; cost to serve is ignored'],
      risk: ['Execution capacity is underestimated', 'The promise outruns what the organisation can deliver at scale', 'Cost to serve rises faster than revenue'] },
    { signs: ['Statements describe how work flows, with little on who benefits', 'Every measure of success is internal: speed, cost, error rates', 'People appear as roles and procedures, with no ownership'],
      risk: ['Execution becomes an end in itself', 'Faster at delivering what customers value less', 'People comply with the process without owning the outcome'] },
    { signs: ['Statements describe how people feel and behave, with no result attached', 'Nothing could be tested against evidence in the time horizon', 'Capability is described as culture, with no mechanism'],
      risk: ['Culture work disconnects from commercial outcomes', 'What the organisation intends to achieve stays undefined', 'People and culture budgets are the first to be cut'] },
    { signs: ['Every statement resolves into a number', 'The customer statement is a sales or share target', 'No capability or behaviour that produces the result'],
      risk: ['Leaders optimise metrics without building what produces them', 'Short-termism disguises itself as strategic clarity', 'Deferred investment weakens future results'] }];
  for (let k = 0; k < 4; k++) {
    await d.compare({ title: `3.2${'bcde'[k]} · ${FLAMS[k].dim}`, cols: [
      { icon: 'FaSearch', title: 'Indicators', sub: 'What reveals the pattern', points: FL[k].signs },
      { icon: 'FaExclamationTriangle', title: 'Strategic risk', sub: 'If not balanced', points: FL[k].risk }], notes: n['f' + (k + 1)] });
  }

  // ── Section 4 · Integration — Collective
  await divider(d, 4, n.s4);
  await d.list({ title: '4.1a · Step 1: how the group works', fontSize: 26, rows: [
    { icon: 'FaUsers', label: 'Agree:', text: 'the group agrees each entry' },
    { icon: 'FaPenFancy', label: 'Scribe:', text: 'one member types the agreed wording' },
    { icon: 'FaLaptop', label: 'Own page:', text: 'every member types the agreed entries, in the session or after it' },
    { icon: 'FaCheck', gold: true, label: 'Confirm:', text: 'each element, each statement, each output' }], notes: n.group });
  await d.list({ title: '4.1b · Step 1: how each element works', fontSize: 26, rows: [
    { icon: 'FaQuestion', label: 'Answer', text: 'the four questions of the element' },
    { icon: 'FaMagic', label: 'Generate', text: 'what this is saying' },
    { icon: 'FaComments', label: 'Ask', text: '“Is this what we mean?”' },
    { icon: 'FaCheck', label: 'Confirm or refine', text: 'until it says what the group means' },
    { icon: 'FaLayerGroup', gold: true, label: '14 of 14:', text: 'the Strategy Architecture output opens' }], notes: n.a41 });
  {
    const s = d.slide(); d.title(s, '4.1c · Step 1: the 14 elements');
    const top = 1.65, rh = 5.3 / 7, cw = 5.915, dia = 0.56;
    for (let k = 0; k < 14; k++) {
      const col = Math.floor(k / 7), row = k % 7, x = 0.6 + col * (cw + 0.3), y = top + row * rh;
      box(s, x, y + 0.05, cw, rh - 0.1, C.tint);
      s.addShape('ellipse', { x: x + 0.15, y: y + (rh - dia) / 2, w: dia, h: dia, fill: { color: C.forest }, line: { color: C.forest } });
      T(s, String(k + 1), { x: x + 0.15, y: y + (rh - dia) / 2, w: dia, h: dia, fontSize: 24, bold: true, color: C.white, align: 'center', valign: 'middle' });
      T(s, EL[k].n, { x: x + 0.95, y, w: cw - 1.1, h: rh, fontSize: 24, bold: true, fontFace: F.head, color: C.forest, valign: 'middle' });
    }
    s.addNotes(n.a41b);
  }
  const elCards = (from, to, icons) => EL.slice(from - 1, to).map((e, j) => ({ icon: icons[j], title: `${from + j} · ${e.n}`, text: e.tag }));
  await d.cards({ title: '4.1d · Elements 1–3: Strategy Discipline', cols: 3, items: elCards(1, 3, ['FaSyncAlt', 'FaBrain', 'FaProjectDiagram']),
    band: 'Strategy Discipline: how the strategy is produced, tested and renewed', notes: n.e1 });
  await d.cards({ title: '4.1e · Elements 4–7: Position and Model', cols: 4, titleSize: 28, textSize: 24, items: elCards(4, 7, ['FaBullseye', 'FaHeart', 'FaCogs', 'FaClock']),
    band: 'Strategic Position: WHAT · WHY      Strategic Model: HOW · WHEN', notes: n.e2 });
  await d.cards({ title: '4.1f · Elements 8–11: Value Architecture', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: elCards(8, 11, ['FaSeedling', 'FaTruck', 'FaInfinity', 'FaUsers']),
    band: 'Value Architecture: value created, delivered and sustained, and for whom', notes: n.e3 });
  await d.cards({ title: '4.1g · Elements 12–14: Strategic Navigation', cols: 3, items: elCards(12, 14, ['FaCompass', 'FaWind', 'FaGlobeAfrica']),
    band: 'Strategic Navigation: reading and moving through the environment', notes: n.e4 });
  await listBand(d, { title: '4.1h · The Strategy Architecture output', rows: GROUPS.map((g, k) => ({
    icon: ['FaBullseye', 'FaCogs', 'FaGem', 'FaCompass', 'FaSyncAlt'][k], label: g[0], text: g[1].map(x => x.replace(' VALUE', '')).join(' · ').replace('SUSTAINS', 'SUSTAINS VALUE') })),
    band: '“What is this architecture collectively saying about the organisation’s strategy?”', notes: n.out });
  await d.list({ title: '4.1i · Six checks before finalising', fontSize: 24, rows: [
    'Do our choices reinforce one another?', 'Where are there contradictions or unresolved tensions?', 'Does our HOW support what we have chosen to achieve?',
    'Does our timing and sequencing reflect the realities of our capability and environment?', 'Have we addressed how value will be created, delivered and sustained?',
    'Does the architecture represent the strategic position we collectively intend?'].map(t => ({ icon: 'FaCheck', text: t })), notes: n.checks });
  await d.cards({ title: '4.2 · Step 2: the Strategy Intent Statement', cols: 4, titleSize: 28, textSize: 24, items: [
    { icon: 'FaBullseye', title: 'WHAT', text: 'The value chosen and its field of play' },
    { icon: 'FaHeart', title: 'WHY', text: 'The rationale for the choices and why they matter' },
    { icon: 'FaCogs', title: 'HOW', text: 'The model, capabilities and mechanisms that deliver the value' },
    { icon: 'FaClock', title: 'WHEN', text: 'The timing, sequencing and strategic moves' }],
    band: '“Does this statement faithfully express the strategic ambition contained in our Architecture?”', notes: n.a42 });
  await d.cards({ title: '4.3a · Step 3: Build Success in Practice', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaSmile', title: 'D1 · Customer Experience & Value', text: 'What should customers and other value recipients see and experience?' },
    { icon: 'FaCogs', title: 'D2 · Operational Capability & Execution Rhythm', text: 'What should be visible in how the organisation operates and executes?' },
    { icon: 'FaUsers', title: 'D3 · People & Culture Dynamics', text: 'What should be visible in how people understand, decide and behave?' },
    { icon: 'FaChartLine', title: 'D4 · Enterprise Value Creation', text: 'How should the organisation benefit across its success metrics?' }], notes: n.a43a });
  await d.list({ title: '4.3b · Step 3: confirm and test the SiP', fontSize: 26, rows: [
    { icon: 'FaComments', label: 'Confirm each domain:', text: 'is this what success should look like if our Strategy Intent is realised?' },
    { icon: 'FaSearchPlus', label: 'Depth:', text: 'could we recognise the condition if we saw it in practice?' },
    { icon: 'FaBalanceScale', label: 'Balance:', text: 'enterprise success, or one dominant perspective?' },
    { icon: 'FaFire', gold: true, label: 'Final check:', text: 'the SiP Flammables' }], notes: n.a43b });
  await d.cards({ title: '4.3c · Three connected outputs', cols: 3, items: [
    { icon: 'FaSitemap', title: 'Strategy Architecture', text: 'Provides the logic' },
    { icon: 'FaBullseye', title: 'Strategy Intent', text: 'Crystallises the ambition' },
    { icon: 'FaEye', title: 'Success in Practice', text: 'Makes the ambition observable', dark: true }],
    band: 'Display or print the three together: the Strategy Intent Design.', notes: n.a43c });

  // ── Section 5 · Application — In Practice
  await divider(d, 5, n.s5);
  {
    const s = d.slide(); d.title(s, '5.1a · Role Contribution to SiP');
    box(s, 0.6, 1.65, 12.13, 1.9, C.forest);
    T(s, '“From this role, what must be contributed so that the agreed Success in Practice becomes real?”', { x: 0.9, y: 1.65, w: 11.6, h: 1.9, fontSize: 28, italic: true, color: C.white, valign: 'middle' });
    for (let i = 0; i < ROLES.length; i++) {
      const x = 0.6 + (i % 5) * 2.465, y = 4.0 + Math.floor(i / 5) * 1.2;
      box(s, x, y, 2.2, 0.95, C.tint);
      T(s, ROLES[i], { x, y, w: 2.2, h: 0.95, fontSize: 28, bold: true, color: C.forest, align: 'center', valign: 'middle' });
    }
    s.addNotes(n.r51a);
  }
  await d.compare({ title: '5.1b · Writing the contribution', cols: [
    { icon: 'FaPenFancy', title: 'Write like this', sub: 'Present tense of the future', points: ['“Customers experience…”', '“Operations are able to…”', '“People consistently…”', '“The organisation creates value through…”'] },
    { icon: 'FaHandPaper', title: 'Push back on', sub: 'General statements', points: ['“Support the strategy”', '“Improve communication”', '“Collaborate better”', '“Drive performance”'] }],
    band: 'What does this role specifically decide, enable, coordinate, resource, protect or change?', notes: n.r51b });
  await d.cards({ title: '5.2 · SiP Statement Collective Application', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaCompressArrowsAlt', title: 'Alignment', text: 'Where contributions support the SiP statement and one another' },
    { icon: 'FaSearch', title: 'Gaps', text: 'Which part of the SiP statement has no role contributing to it' },
    { icon: 'FaBolt', title: 'Tensions', text: 'Where role contributions pull against one another' },
    { icon: 'FaUserTie', title: 'Execution Ownership', text: 'Where the SiP statement needs clearer execution ownership' }], notes: n.c52 });

  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Return to the opening question', text: 'Read your original definition of strategy. What would you change in it now — and why?',
    foot: 'Based on what Unit 2 revealed, the one thing I am committed to doing differently before our next session is…', notes: n.summary });

  // every insight placed once
  const missing = Object.keys(INS).filter(k => !ctx.used.has(k));
  if (missing.length) throw new Error('insights not placed: ' + missing.join(', '));

  // reflection slides: spec for add_reflection_slides.py (pictures are shot separately)
  const spec = {
    _about: 'Unit 2 reflection slides (rebuilt deck, October 2026). Pictures are shots of the reflection boxes in unit2_m1_lens1_p.html (860px viewport, 3x). Retake them if a reflection prompt changes. Written by unit02.js.',
    title_model: 'Key learning outcomes',
    slides: [
      { title: 'Section 1 Reflections', after: '1.3 · SiP: From Intent to Future Reality', notes: n.ref1, pictures: [
        { part: '1.1', file: 'ref_1.1.png', alt: "Reflection — Strategy Architecture: Which part of your organisation's strategy architecture is least well defined today? What is the consequence?" },
        { part: '1.2', file: 'ref_1.2.png', alt: "Reflection — Strategy Intent: From your assigned executive leader perspective: which dimension (WHAT, WHY, HOW, WHEN) is least clearly defined in your organisation's current strategy? What would clarifying it change?" }] },
      { title: 'Section 2 Reflections', after: '2.1.3 · Execution Coherence', notes: n.ref2, pictures: [
        { part: '2.1', file: 'ref_2.1.png', alt: 'Reflection — Three Functions: Which of the three functions is weakest in your organisation today? What happens as a result?' }] },
      { title: 'Section 3 Reflections', after: '3.2e · ', notes: n.ref3, pictures: [
        { part: '3.1', file: 'ref_3.1.png', alt: 'Reflection — SiP Indicators: From your assigned executive leader role: which SiP domain shows the most significant gaps in your organisation right now? What is the primary cause?' }] },
      { title: 'Section 5 Reflections', after: '5.2 · SiP Statement Collective Application', notes: n.ref5, pictures: [
        { part: '5.2', file: 'ref_5.2.png', alt: 'Reflection — Application: Having completed the full application exercise — what is the single most important shift your organisation must make to close the gap between your current strategic capability and the SiP you have collectively described?' }] }],
  };
  const sp = path.join(__dirname, 'reflections', 'u02'); fs.mkdirSync(sp, { recursive: true });
  fs.writeFileSync(path.join(sp, 'spec.json'), JSON.stringify(spec, null, 1));

  await d.save(OUT); console.log('saved', OUT, '· insights placed:', ctx.used.size);
})().catch(e => { console.error(e); process.exit(1); });
