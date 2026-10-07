// Unit 4 · Direction Integrity (ABCV-MBT) — facilitator deck, rebuilt October 2026 from the rebuilt Unit 4 pages.
// Run from Unit decks\_build:  node unit04.js "<output.pptx>" [logo.png]
// Then: add_reflection_slides.py (spec written by this script) and format_notes_u03.py; build_u04.sh runs all the steps.
// The reflection pictures come from shoot_reflections_u04.py. See rebuild_u04/README.md, "The deck".
//
// Format: the same design system (lib2.js) and the same slide types as the Unit 2 and Unit 3 decks.
// One slide for each part of the unit, with sub-slides (a, b…) only where a part needs them. Slide text is the page text,
// shortened; the presenter notes (u04_notes.js) carry the teaching. The data comes from u04_data.json, written by
// rebuild_u04/export_deck_data.py from u4_content.py, the content both pages are built from.
const { Deck, C, F, T, box, badge } = require('./lib2');
const fs = require('fs');
const path = require('path');
const HERE = __dirname;
const [OUT, LOGO = [path.join(HERE, '..', '..', 'logo.png'), path.join(HERE, 'logo.png')].find(x => fs.existsSync(x))] = process.argv.slice(2);
if (!OUT) { console.error('usage: node unit04.js <output.pptx> [logo.png]'); process.exit(1); }
const INS = JSON.parse(fs.readFileSync(path.join(HERE, 'enrich', 'u04_rebuild.json'), 'utf8'));
const { n, used, D, KLO, SLOS, REFL, OPENING, CLOSING_Q, ROLES, CEO, KR, q, mq } = require('./u04_notes.js')(INS);
const { DEPTHS, BOUNDARY_KINDS: BK, VP_TESTS: VP, MBT2, TRAPS, GAME: G, MINES, STEPS, WORKED_KR: W, EXAMPLES } = D;
const CP = Object.fromEntries(D.CHECKPOINTS.map(c => [c.k, c]));
const cap = s => s.charAt(0).toUpperCase() + s.slice(1);
const nodot = s => s.replace(/\.$/, '');

const SECTIONS = [
  { num: 1, name: 'Awareness', anchor: 'What', heading: 'What are the ABCV–MBT Integrity Checkpoints?' },
  { num: 2, name: 'Intelligence', anchor: 'Why', heading: 'The Industry Illusion' },
  { num: 3, name: 'Extrapolating', anchor: 'Where', heading: 'Where Does Directional Integrity Break Down?' },
  { num: 4, name: 'Integration', anchor: 'Collective', heading: 'ABCV–MBT Working Papers' },
  { num: 5, name: 'Application', anchor: 'In Practice', heading: 'Cause of Death — Match the Breakdown' }];

(async () => {
  const d = new Deck({ unit: 4, module: 2, moduleName: 'Direction', title: 'Direction Integrity (ABCV-MBT)' });
  const div = k => d.section(Object.assign({}, SECTIONS[k - 1], { outcomes: SLOS[k], notes: n['s' + k] }));
  const band = (s, text, y = 6.15, h = 0.85) => { box(s, 0.6, y, 12.13, h, C.deep); T(s, text, { x: 0.9, y, w: 11.6, h, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); };

  // A list with an optional band at the foot (as in unit03.js).
  async function rows(o) {
    const s = d.slide(); d.title(s, o.title);
    const bh = o.bandH || 0.85, k = o.rows.length, top = 1.65, avail = (o.band ? 5.2 - bh : 5.35), rh = avail / k, ib = Math.min(0.7, rh * 0.7);
    for (let i = 0; i < k; i++) {
      const r = o.rows[i], y = top + i * rh;
      await badge(s, r.icon, 0.6, y + (rh - ib) / 2, ib, r.gold ? C.gold : C.forest, C.white);
      T(s, r.label ? [{ text: r.label + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: r.text || '' }] : r.text,
        { x: 0.6 + ib + 0.35, y, w: 12.13 - ib - 0.35, h: rh, fontSize: o.fontSize || 26, valign: 'middle' });
    }
    if (o.band) band(s, o.band, 7.0 - bh, bh);
    s.addNotes(o.notes);
  }

  // A checkpoint's Must-Be-True slide: the question, then one Unit 3 Key Result and its condition.
  async function mbt(o) {
    const s = d.slide(); d.title(s, o.title);
    box(s, 0.6, 1.65, 12.13, 1.75, C.tint);
    await badge(s, 'FaQuestion', 0.85, 1.9, 0.7, C.forest, C.white);
    T(s, [{ text: 'Ask  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: o.ask }], { x: 1.8, y: 1.65, w: 10.7, h: 1.75, fontSize: 24, valign: 'middle' });
    box(s, 0.6, 3.6, 12.13, 3.4, C.forest);
    await badge(s, 'FaKey', 0.85, 3.85, 0.7, C.gold, C.deep);
    T(s, 'On a Key Result from Unit 3', { x: 1.8, y: 3.85, w: 10.7, h: 0.7, fontSize: 26, bold: true, fontFace: F.head, color: C.white, valign: 'middle' });
    T(s, o.kr, { x: 0.9, y: 4.7, w: 11.55, h: 0.95, fontSize: 24, italic: true, color: C.goldLight });
    T(s, [{ text: 'Must be true:  ', options: { bold: true, color: C.gold } }, { text: o.cond }], { x: 0.9, y: 5.7, w: 11.55, h: 1.2, fontSize: 24, color: C.white });
    s.addNotes(o.notes);
  }

  // One step of the worked example: the step question with the Key Result word for word, the company's answers, the condition.
  function step(o) {
    const s = d.slide(); d.title(s, o.title);
    box(s, 0.6, 1.5, 12.13, 1.45, C.tint);
    T(s, o.q, { x: 0.9, y: 1.5, w: 11.55, h: 1.45, fontSize: 24, italic: true, color: C.forest, valign: 'middle' });
    const top = 3.1, bh = o.bandH || 1.25, bot = 7.0 - bh - 0.15;
    T(s, o.lines.map((l, i) => Array.isArray(l)
      ? [{ text: l[0] + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: l[1], options: { breakLine: i < o.lines.length - 1 } }]
      : [{ text: l, options: { bullet: true, breakLine: i < o.lines.length - 1 } }]).flat(),
      { x: 0.75, y: top, w: 11.85, h: bot - top, fontSize: 24, valign: 'middle', paraSpaceAfter: o.gap === undefined ? 6 : o.gap });
    box(s, 0.6, 7.0 - bh, 12.13, bh, C.deep);
    T(s, [{ text: 'Must be true:  ', options: { bold: true, color: C.gold } }, { text: o.mbt, options: { color: C.white } }], { x: 0.9, y: 7.0 - bh, w: 11.55, h: bh, fontSize: 24, valign: 'middle' });
    s.addNotes(o.notes);
  }

  // ── Front
  d.m.title = 'Direction Integrity\n(ABCV-MBT)';   // the cover title breaks before the bracket
  await d.cover({ logo: LOGO, subtitle: 'Testing whether the chosen direction is strategically sound before execution begins', notes: n.cover });
  d.m.title = 'Direction Integrity (ABCV-MBT)';
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: KLO.map(t => ({ icon: 'FaCheck', text: t })), notes: n.klo });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: SECTIONS.map((x, k) => ({ icon: ['FaEye', 'FaLightbulb', 'FaMapMarkedAlt', 'FaUsers', 'FaClipboardCheck'][k], label: `Section ${x.num} · ${x.name}`, text: '— ' + x.anchor })), notes: n.journey });

  // ── Section 1 · Awareness — What
  await div(1);
  await d.prompt({ icon: 'FaQuoteLeft', label: 'Overview · From Unit 3 to Unit 4', text: OPENING, notes: n.ov1 });
  await rows({ title: 'Overview · The Logic', fontSize: 24,
    rows: D.OVERVIEW_Q.map((o, k) => ({ icon: ['FaBullseye', 'FaBorderAll', 'FaChessKnight', 'FaGem'][k], label: `${STEPS[k][0]} · ${STEPS[k][1]}`, text: o[2] })),
    band: 'At each step, name what Must Be True.', notes: n.ov2 });

  await d.cards({ title: '1.1a · Arena: the Customer End Game', cols: 3, titleSize: 28, textSize: 24, items:
    DEPTHS.map((x, k) => ({ icon: ['FaTasks', 'FaHandHoldingHeart', 'FaDoorOpen'][k], title: x.name, text: x.q, dark: k === 2 })),
    band: 'The Arena tells you who you are actually competing with.', notes: n.p11a });
  await mbt({ title: '1.1b · Arena: what Must Be True', ask: MBT2.a[1], kr: EXAMPLES[0].t, cond: EXAMPLES[0].a, notes: n.p11b });

  await d.cards({ title: '1.2a · Boundaries: the Friction Architecture', cols: 3, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items:
    BK.map((b, k) => ({ icon: ['FaBalanceScale', 'FaCogs', 'FaMicrochip', 'FaSitemap', 'FaCoins', 'FaUserFriends'][k], title: b[0], text: cap(nodot(b[1])) })),
    notes: n.p12a });
  await mbt({ title: '1.2b · Boundaries: what Must Be True', ask: MBT2.b[1], kr: EXAMPLES[0].t, cond: EXAMPLES[0].b, notes: n.p12b });

  await d.cards({ title: '1.3a · Competition: the True Landscape', cols: 2, titleSize: 26, textSize: 24, items: [
    { icon: 'FaStore', title: 'Who sells something similar to us?', text: 'If leaders define Arena through their industry, they will probably identify competitors through their industry.' },
    { icon: 'FaRoute', title: 'What alternatives does the customer have for achieving the end game?', dark: true, text: 'Do it internally. Do it themselves. Use technology instead. Postpone it. Choose a completely different solution. Do nothing.' }],
    notes: n.p13a });
  await mbt({ title: '1.3b · Competition: what Must Be True', ask: MBT2.c[1], kr: EXAMPLES[0].t, cond: EXAMPLES[0].c, notes: n.p13b });

  await d.cards({ title: '1.4a · Value Proposition: Coherent Advantage', cols: 3, titleSize: 28, textSize: 24, items:
    VP.map((v, k) => ({ icon: ['FaHeart', 'FaFingerprint', 'FaSyncAlt'][k], title: v[0], text: v[1], dark: k === 2 })),
    band: 'RELEVANT + DISTINCTIVE + DELIVERABLE = STRATEGIC VALUE', notes: n.p14a });
  await mbt({ title: '1.4b · Value Proposition: what Must Be True', ask: MBT2.v[1], kr: EXAMPLES[0].t, cond: EXAMPLES[0].v, notes: n.p14b });

  await rows({ title: 'Bringing ABCV Together', fontSize: 24, rows: [
    { icon: 'FaBullseye', label: 'A — Arena', text: 'What is the customer ultimately trying to achieve?' },
    { icon: 'FaBorderAll', label: 'B — Boundaries', text: 'What could constrain our ability to deliver that outcome?' },
    { icon: 'FaChessKnight', label: 'C — Competition', text: 'Who or what else can enable the customer to achieve it?' },
    { icon: 'FaGem', label: 'V — Value Proposition', text: 'Why should the customer choose the value we create?' },
    { icon: 'FaKey', gold: true, label: 'MBT — Must Be True', text: 'What conditions must hold for our strategic logic to remain valid?' }],
    band: 'ABCV does not ask whether an OKR is well written. It asks whether the strategic logic underneath it can survive reality.', bandH: 1.15, notes: n.together });

  // ── Section 2 · Intelligence — Why
  await div(2);
  await d.cards({ title: '2.1 · The Industry Illusion', cols: 3, titleSize: 28, textSize: 24, items:
    TRAPS.map((t, k) => ({ icon: ['FaGlasses', 'FaFilter', 'FaCouch'][k], title: t.name, text: t.line, dark: k === 2 })),
    band: D.II_BOUNDARY, notes: n.p21 });
  await d.cards({ title: '2.2a · The Industry Illusion Game', cols: 3, titleSize: 28, textSize: 24, items: [
    { icon: 'FaSearch', title: 'Round 1', text: G.r1_title },
    { icon: 'FaSatelliteDish', title: 'Round 2', text: G.r2_title },
    { icon: 'FaQuestion', title: 'Round 3', dark: true, text: G.r3_title }],
    band: 'The case: The Future of a University. Three rounds, then The Reveal.', notes: n.p22 });
  await d.prompt({ icon: 'FaBullseye', label: '2.2b · After The Reveal: Apply Arena', text: G.arena_q,
    foot: 'Now look again at everything you deprioritised in Rounds 1 and 2.', notes: n.p22b });

  // ── Section 3 · Extrapolating — Where
  await div(3);
  {
    const s = d.slide(); d.title(s, '3.1a · The Executive Hot Zone');
    T(s, 'Role-based blind spots: the ABCV checkpoint each role most often overlooks', { x: 0.6, y: 1.5, w: 12.1, h: 0.5, fontSize: 24, italic: true, color: C.muted });
    ROLES.forEach(([r, c], i) => {
      const x = 0.6 + (i % 3) * 4.11, y = 2.2 + Math.floor(i / 3) * 1.62;
      box(s, x, y, 3.9, 1.4, C.tint);
      T(s, [{ text: r, options: { bold: true, color: C.forest, fontFace: F.head, breakLine: true } }, { text: c }], { x: x + 0.25, y, w: 3.4, h: 1.4, fontSize: 26, valign: 'middle' });
    });
    s.addNotes(n.p31a);
  }
  await d.cards({ title: '3.1b · A Hot Zone Card: the CEO', cols: 2, titleBeside: true, titleSize: 24, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaEyeSlash', title: 'What Gets Overlooked', text: 'Boundaries' },
    { icon: 'FaExclamationTriangle', title: 'Symptom', text: `“${CEO.symptom}”` },
    { icon: 'FaSearchPlus', title: 'The Checkpoint Reveals', dark: true, text: CEO.line },
    { icon: 'FaQuestion', title: 'Right Question', dark: true, text: `“${CEO.right}”` }], notes: n.p31b });

  // ── Section 4 · Integration — Collective
  await div(4);
  {
    const s = d.slide(true);
    await badge(s, 'FaQuoteLeft', 0.8, 1.0, 1.2, C.gold, C.deep);
    T(s, '4.1 · Worked Example: Stress-Testing a Key Result', { x: 2.3, y: 1.2, w: 10.3, h: 0.7, fontSize: 26, bold: true, color: C.gold });
    T(s, W.kr, { x: 2.3, y: 2.15, w: 10.3, h: 2.6, fontSize: 36, fontFace: F.head, italic: true, color: C.white, valign: 'top' });
    T(s, 'Objective: ' + W.obj, { x: 2.3, y: 4.95, w: 10.3, h: 0.95, fontSize: 24, color: C.goldLight });
    T(s, 'A client services company · from Unit 3, part 2.2', { x: 2.3, y: 6.3, w: 10.3, h: 0.6, fontSize: 24, color: C.paleText });
    s.addNotes(n.p41);
  }
  step({ title: '4.1 · Step 1: Define the Arena', q: q(0), lines: [['Functional', W.fn], ['Experiential', W.ex], ['Consequential', W.co]], mbt: W.a, bandH: 1.3, notes: n.p41s1 });
  step({ title: '4.1 · Step 2: Understand the Boundaries', q: q(1), lines: W.bounds.map(b => b[0]), mbt: W.b, bandH: 1.0, gap: 2, notes: n.p41s2 });
  step({ title: '4.1 · Step 3: See the Competition', q: q(2), lines: W.comp, mbt: W.c, bandH: 1.0, gap: 2, notes: n.p41s3 });
  step({ title: '4.1 · Step 4: Establish the Value Proposition', q: q(3), lines: [['Relevant', W.rel], ['Distinctive', W.dis], ['Deliverable', W.dlv]], mbt: W.v, bandH: 1.0, notes: n.p41s4 });
  await rows({ title: '4.1 · Four Steps, Four Conditions', fontSize: 24, rows: [
    { icon: 'FaBullseye', label: 'Arena', text: W.a },
    { icon: 'FaBorderAll', label: 'Boundaries', text: W.b },
    { icon: 'FaChessKnight', label: 'Competition', text: W.c },
    { icon: 'FaGem', label: 'Value Proposition', text: W.v }],
    band: 'If one of them shifts or fails, the Key Result becomes fragile by design.', notes: n.p41end });

  await rows({ title: '4.2a · Stress-Testing Your Key Results', fontSize: 26, rows: [
    { icon: 'FaUsers', label: 'Agree:', text: 'the group agrees each entry' },
    { icon: 'FaPenFancy', label: 'Scribe:', text: 'one member types the agreed wording' },
    { icon: 'FaLaptop', label: 'Own page:', text: 'every member types the agreed entries, in the session or after it' },
    { icon: 'FaCheck', gold: true, label: 'Confirm:', text: 'every Key Result, through the four steps' }],
    band: 'This is Capstone work: your confirmed outputs feed your team’s Capstone Blueprint.', notes: n.p42a });
  await rows({ title: '4.2b · Your Key Results: the Four Steps', fontSize: 24, rows: [
    { icon: 'FaBullseye', label: '1 · Define the Arena', text: 'which customer need the Key Result serves' },
    { icon: 'FaBorderAll', label: '2 · Understand the Boundaries', text: 'what could slow, restrict or prevent delivery' },
    { icon: 'FaChessKnight', label: '3 · See the Competition', text: 'who or what else can give the customer what it delivers' },
    { icon: 'FaGem', label: '4 · Establish the Value Proposition', text: 'what about it will make customers choose you' }],
    band: 'At each step, name what Must Be True.', notes: n.p42b });

  // ── Section 5 · Application — In Practice
  await div(5);
  await d.cards({ title: 'Cause of Death · Match the Breakdown', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, items: [
    { icon: 'FaSearch', title: '1 · Find the illusion', text: 'Choose the investigation question the scenario answers: Familiarity, Exclusion or Complacency.' },
    { icon: 'FaMapMarkerAlt', title: '2 · Find where it sits', dark: true, text: 'Choose the ABCV checkpoint the illusion hid from leaders: Arena, Boundaries, Competition or Value Proposition.' }],
    band: 'Four failed strategies. Defuse the mine before it detonates.', notes: n.p51a });
  await d.cards({ title: 'Cause of Death · The Four Mines', cols: 2, titleBeside: true, titleSize: 24, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaShip', title: MINES[0].name, text: 'A SaaS platform' },
    { icon: 'FaCarSide', title: MINES[1].name, text: 'A leading logistics firm' },
    { icon: 'FaUserSecret', title: MINES[2].name, text: 'A financial advisory firm' },
    { icon: 'FaTheaterMasks', title: MINES[3].name, text: 'A boutique consulting firm' }], notes: n.p51b });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · The closing question', text: CLOSING_Q, notes: n.summary });

  if (used.size !== Object.keys(INS).length) throw new Error('insights not all used: ' + Object.keys(INS).filter(k => !used.has(k)).join(', '));
  await d.save(OUT);

  // Spec for add_reflection_slides.py: one "Section N Reflections" slide after the last content slide of Sections 1, 3 and 5.
  const spec = { title_model: 'Key learning outcomes', slides: [
    { title: 'Section 1 Reflections', after: 'Bringing ABCV Together', notes: n.ref1, pictures: [
      { part: '1', file: 'ref_ov.png', alt: 'Overview reflection: ' + REFL.ov }, { part: '2', file: 'ref_together.png', alt: 'Bringing ABCV Together reflection: ' + REFL.together }] },
    { title: 'Section 3 Reflections', after: '3.1b · A Hot Zone Card', notes: n.ref3, pictures: [{ part: '3.1', file: 'ref_3.1.png', alt: 'Reflection 3.1: ' + REFL['3.1'] }] },
    { title: 'Section 5 Reflections', after: 'Cause of Death · The Four Mines', notes: n.ref5, pictures: [{ part: '5', file: 'ref_close.png', alt: 'Closing Commitment: ' + REFL.close }] }] };
  fs.mkdirSync(path.join(HERE, 'reflections', 'u04'), { recursive: true });
  fs.writeFileSync(path.join(HERE, 'reflections', 'u04', 'spec.json'), JSON.stringify(spec, null, 1));
  console.log('saved', OUT, '· insights used:', used.size);
})().catch(e => { console.error(e); process.exit(1); });
