// Unit 5 · Aligning Heart & Mind — facilitator deck, rebuilt October 2026 after the three-way match of the Unit 5 pages,
// and amended on 8 October 2026 (evening) with the pages: Principle 1, parts 1.3.1 to 1.3.4, OCEAVL in Section 3, alignment hot zones in 4.2, the Alignment Toolkit in Section 5.
// Run from Unit decks\_build:  node unit05.js "<output.pptx>" [logo.png]
// Then: add_reflection_slides.py (spec written by this script) and format_notes_u03.py; build_u05.sh runs all the steps.
// The reflection pictures come from shoot_reflections_u05.py. See rebuild_u05/README.md, "The deck".
//
// Format: the same design system (lib2.js) and the same slide types as the Unit 2, Unit 3 and Unit 4 decks.
// One slide for each part of the unit. 1.2 has an overview slide and one slide for each principle; 1.3 and 3.1 run over two slides (a, b).
// Section 5 slides are titled by step. Slide text is page text, shortened; the presenter notes (u05_notes.js) carry the teaching.
// Titles, outcomes and reflection questions come from u05_data.json, written by rebuild_u05/export_deck_data.py from the two pages.
const { Deck, C, F, T, box, badge } = require('./lib2');
const fs = require('fs');
const path = require('path');
const HERE = __dirname;
const [OUT, LOGO = [path.join(HERE, '..', '..', 'logo.png'), path.join(HERE, 'logo.png')].find(x => fs.existsSync(x))] = process.argv.slice(2);
if (!OUT) { console.error('usage: node unit05.js <output.pptx> [logo.png]'); process.exit(1); }
const INS = JSON.parse(fs.readFileSync(path.join(HERE, 'enrich', 'u05_rebuild.json'), 'utf8'));
const { n, used, D } = require('./u05_notes.js')(INS);
const { KLO, SECTIONS, PARTS, REFL, STEPS, CLOSING_Q } = D;
const pt = (k, suffix = '') => `${k}${suffix} · ${PARTS[k].title}`;

(async () => {
  const d = new Deck({ unit: 5, module: 3, moduleName: 'Influence', title: 'Aligning Heart & Mind' });
  // Titles keep the page wording in full; the size steps down (never under 26pt) so that a long part title stays on the slide.
  d.title = function (s, t, dark) {
    const size = [36, 32, 30, 28, 26].find(z => t.length <= (12.1 * 72) / (z * 0.47) * 0.93) || 26;
    T(s, t, { x: 0.6, y: 0.45, w: 12.1, h: 0.95, fontSize: size, fontFace: F.head, bold: true, color: dark ? C.white : C.forest, valign: 'middle' });
  };
  const div = k => d.section(Object.assign({}, SECTIONS[k - 1], { notes: n['s' + k] }));
  const band = (s, text, y = 6.15, h = 0.85) => { box(s, 0.6, y, 12.13, h, C.deep); T(s, text, { x: 0.9, y, w: 11.6, h, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); };

  // A list with an optional band at the foot (as in unit03.js and unit04.js). A row may carry a tagline after its text.
  async function rows(o) {
    const s = d.slide(); d.title(s, o.title);
    const bh = o.bandH || 0.85, k = o.rows.length, top = 1.65, avail = (o.band ? 5.2 - bh : 5.35), rh = avail / k, ib = Math.min(0.7, rh * 0.7);
    for (let i = 0; i < k; i++) {
      const r = o.rows[i], y = top + i * rh;
      await badge(s, r.icon, 0.6, y + (rh - ib) / 2, ib, r.gold ? C.gold : C.forest, C.white);
      const runs = [];
      if (r.label) runs.push({ text: r.label + '  ', options: { bold: true, color: C.forest, fontFace: F.head } });
      runs.push({ text: r.text || '' });
      if (r.tag) { runs.push({ text: ' · ', options: { color: C.muted } }); runs.push({ text: r.tag, options: { italic: true, color: C.muted } }); }
      T(s, runs, { x: 0.6 + ib + 0.35, y, w: 12.13 - ib - 0.35, h: rh, fontSize: o.fontSize || 26, valign: 'middle' });
    }
    if (o.band) band(s, o.band, 7.0 - bh, bh);
    s.addNotes(o.notes);
  }

  // Two columns side by side, the second dark (as Deck.compare, with room for a two-line column title and no sub-line).
  async function pair(o) {
    const s = d.slide(); d.title(s, o.title);
    const bottom = o.band ? 5.95 : 6.95;
    for (let i = 0; i < 2; i++) {
      const c = o.cols[i], x = 0.6 + i * 6.23, dark = i === 1;
      box(s, x, 1.65, 5.9, bottom - 1.65, dark ? C.forest : C.tint);
      await badge(s, c.icon, x + 0.3, 1.9, 0.8, dark ? C.gold : C.forest, dark ? C.deep : C.white);
      T(s, c.title, { x: x + 1.3, y: 1.9, w: 4.45, h: 0.8, fontSize: 26, bold: true, fontFace: F.head, color: dark ? C.white : C.forest, valign: 'middle' });
      T(s, c.points.map((p, j) => ({ text: p, options: { bullet: true, breakLine: j < c.points.length - 1 } })),
        { x: x + 0.35, y: 2.95, w: 5.3, h: bottom - 0.1 - 2.95, fontSize: 24, color: dark ? C.white : C.ink, paraSpaceAfter: 6 });
    }
    if (o.band) band(s, o.band);
    s.addNotes(o.notes);
  }

  // A grid of tinted boxes, each holding a bold name and a line of text (the ten roles of 4.2, the eight fields of the map).
  function grid(o) {
    const s = d.slide(); d.title(s, o.title);
    const cols = o.cols, rws = Math.ceil(o.items.length / cols), gap = 0.2, top = 1.65, bottom = o.band ? 5.95 : 6.95;
    const cw = (12.13 - gap * (cols - 1)) / cols, ch = (bottom - top - gap * (rws - 1)) / rws;
    o.items.forEach((it, i) => {
      const x = 0.6 + (i % cols) * (cw + gap), y = top + Math.floor(i / cols) * (ch + gap);
      box(s, x, y, cw, ch, C.tint);
      const runs = [{ text: it.name + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }];
      it.parts.forEach((p, j) => { if (j) runs.push({ text: ' · ', options: { color: C.muted } }); runs.push({ text: p }); });
      T(s, runs, { x: x + 0.25, y, w: cw - 0.5, h: ch, fontSize: 24, valign: 'middle' });
    });
    if (o.band) band(s, o.band);
    s.addNotes(o.notes);
  }

  // ── Front
  await d.cover({ logo: LOGO, subtitle: 'The human operating system that enables strategy to move from intention to execution', notes: n.cover });
  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: KLO.map(t => ({ icon: 'FaCheck', text: t })), notes: n.klo });
  await d.list({ title: 'The unit journey', fontSize: 28, rows: SECTIONS.map((x, k) => ({ icon: ['FaEye', 'FaLightbulb', 'FaMapMarkedAlt', 'FaUsers', 'FaClipboardCheck'][k], label: `Section ${x.num} · ${x.name}`, text: '— ' + x.anchor })), notes: n.journey });

  // ── Section 1 · Awareness — What
  await div(1);
  await pair({ title: pt('1.1'), cols: [
    { icon: 'FaBrain', title: 'Cognition — Mind', points: ['How individuals interpret what strategy means.', 'Shaped by professional expertise, mental shortcuts, past experience, and risk perception.'] },
    { icon: 'FaHeart', title: 'Emotion — Heart', points: ['How individuals experience the strategy.', 'Shapes engagement energy, morale, friction load, psychological safety, and values alignment.'] }],
    band: 'Execution begins inside the human system.', notes: n.p11 });

  // 1.2: the overview carries the part number; each principle then has its own slide, in order (Carol, 2 October 2026).
  // The five taglines are from Carol's original content.
  await rows({ title: pt('1.2'), fontSize: 24, rows: [
    { icon: 'FaUsers', label: 'Principle 1', text: 'Strategy Moves Through People', tag: 'the human entry point of execution' },
    { icon: 'FaUnlink', label: 'Principle 2', text: 'Misalignment Fragments Effort', tag: 'the cost of ignoring the human system' },
    { icon: 'FaDraftingCompass', label: 'Principle 3', text: 'Alignment Must Be Designed', tag: 'the tools that create alignment' },
    { icon: 'FaProjectDiagram', label: 'Principle 4', text: 'Human Reactions Are Predictable', tag: 'the behavioural dynamics that influence execution' },
    { icon: 'FaEye', label: 'Principle 5', text: 'Execution Must Be Visible in Behaviour', tag: 'the observable standard for alignment' }], notes: n.p12 });
  await rows({ title: 'Principle 1 — Strategy Moves Through People', fontSize: 24, rows: [
    { icon: 'FaBrain', label: 'Interpretation', text: 'People first make sense of the strategy.' },
    { icon: 'FaHeart', label: 'Experience', text: 'People then experience the strategy emotionally.' },
    { icon: 'FaBalanceScale', label: 'Choices', text: 'People then make choices and trade-offs.' },
    { icon: 'FaWalking', label: 'Actions', text: 'People finally act in ways that either carry the strategy forward or weaken it.' },
    { icon: 'FaChartLine', label: 'Results', text: 'Results emerge when thinking is clear, feeling is aligned, decisions are coherent, and behaviour is disciplined.' }],
    band: 'When any part of the chain is weak, execution begins to leak.', notes: n.pr1 });
  await d.cards({ title: 'Principle 2 — Misalignment Fragments Effort', cols: 3, titleSize: 26, textSize: 24, items: [
    { icon: 'FaCommentDots', title: 'Chinese Whispers', text: 'Intent mutates as it travels downward.' },
    { icon: 'FaRedo', title: 'Clarification Debt', text: '60–80% of leadership time spent re-explaining, correcting, realigning.' },
    { icon: 'FaUserSlash', title: 'Silent Disengagement', dark: true, text: 'People comply outwardly but withdraw inwardly.' }],
    band: 'Low-alignment organisations experience 41% lower productivity and 48% higher turnover.', notes: n.pr2 });
  await d.cards({ title: 'Principle 3 — Alignment Must Be Designed', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, items: [
    { icon: 'FaUserCog', title: 'OCEAVL Assessment', text: 'Surfaces psychological tendencies influencing executive decision-making.' },
    { icon: 'FaThermometerHalf', title: 'Emotional Climate Assessment', dark: true, text: 'Identifies the prevailing state of being across six core emotional categories: Joy, Sadness, Anger, Fear, Disgust, Surprise.' }],
    band: 'Alignment rarely emerges naturally.', notes: n.pr3 });
  await rows({ title: 'Principle 4 — Human Reactions Are Predictable', fontSize: 24, rows: [
    { icon: 'FaChartLine', text: 'Reactions to strategic change follow predictable psychological patterns.' },
    { icon: 'FaExclamationTriangle', text: 'The human brain processes social change using the same threat circuitry as physical danger' },
    { icon: 'FaHeartbeat', text: 'Any new goal, system, or way of working is evaluated emotionally before it is evaluated rationally' }],
    band: 'The SCARF Model (David Rock) explains five social conditions that trigger emotional responses during change.', bandH: 1.05, notes: n.pr4 });
  await rows({ title: 'Principle 5 — Execution Must Be Visible in Behaviour', fontSize: 24, rows: [
    { icon: 'FaEye', text: 'Strategic alignment ultimately becomes visible through behaviour.' },
    { icon: 'FaEyeSlash', text: 'Without observable behaviour, alignment remains theoretical.' },
    { icon: 'FaRulerCombined', text: 'With behavioural standards, alignment becomes visible, measurable, and sustainable.' }],
    band: 'Accountability, Commitment, Engagement, Integrity, Transparency', notes: n.pr5 });

  await pair({ title: '1.3a · Change Management: The Event and the Transition', cols: [
    { icon: 'FaCalendarDay', title: 'The event', points: ['A change is an event.', 'It is announced on a date, and on that date the structure, the system or the target is different.', 'The event belongs to the organisation.'] },
    { icon: 'FaWalking', title: 'The transition', points: ['Letting go of a familiar practice', 'Working out what the new one asks of them', 'Becoming able to do it', 'The transition belongs to the person.'] }],
    band: 'Change management is the leadership discipline of moving people from current practice to the practice the strategy requires.', notes: n.p13a });
  await rows({ title: pt('1.3', 'b'), fontSize: 24, rows: [
    { icon: 'FaBrain', label: 'Mind · 3S · Explain', text: 'They understand the change, why it matters and what they do differently.' },
    { icon: 'FaHeart', label: 'Heart · SCARF · Involve', text: 'They want it to succeed.' },
    { icon: 'FaHandPaper', label: 'Hands · STAT · Equip', text: 'They are able to do it.' },
    { icon: 'FaSyncAlt', label: 'Habit · ACE-IT · Reinforce', text: 'It has become the way they work.' }],
    band: 'A change stalls at the first check it fails.', notes: n.p13b });

  await d.cards({ title: pt('1.3.1'), cols: 3, titleSize: 28, textSize: 24, items: [
    { icon: 'FaExchangeAlt', title: 'Shift', text: '“What is changing?”' },
    { icon: 'FaBalanceScale', title: 'Stake', text: '“What do we gain if we change, and what do we lose if we stay as we are?”' },
    { icon: 'FaShoePrints', title: 'Step', dark: true, text: '“What do I do differently?”' }],
    band: 'Mind passes when the people affected can say three things about the change in their own words.', notes: n.p14 });
  await rows({ title: pt('1.3.2'), fontSize: 26, rows: [
    { icon: 'FaMedal', label: 'Status', text: '“Will this reduce my importance?”' },
    { icon: 'FaCompass', label: 'Certainty', text: '“Do I know what success looks like?”' },
    { icon: 'FaUnlockAlt', label: 'Autonomy', text: '“Am I losing control of my work?”' },
    { icon: 'FaHandshake', label: 'Relatedness', text: '“Do I still belong here?”' },
    { icon: 'FaBalanceScale', label: 'Fairness', text: '“Is this being applied equitably?”' }], notes: n.p15 });
  await d.cards({ title: pt('1.3.3'), cols: 2, titleBeside: true, titleSize: 28, textSize: 24, items: [
    { icon: 'FaGraduationCap', title: 'Skill', text: '“Do they know how to do it?”' },
    { icon: 'FaClock', title: 'Time', text: '“Do they have the hours to do it?”' },
    { icon: 'FaKey', title: 'Authority', dark: true, text: '“Are they allowed to decide and act?”' },
    { icon: 'FaTools', title: 'Tools', dark: true, text: '“Do they have the systems and resources?”' }],
    band: 'Hands passes when all four elements are in place.', notes: n.p16 });
  await rows({ title: pt('1.3.4'), fontSize: 24, rows: [
    { icon: 'FaUserCheck', label: 'Accountability', text: 'Taking full ownership for results.' },
    { icon: 'FaAnchor', label: 'Commitment', text: 'Staying anchored to agreed strategic intent even when pressure rises.' },
    { icon: 'FaComments', label: 'Engagement', text: 'Actively involving self and others in sense-making, dialogue, and execution.' },
    { icon: 'FaShieldAlt', label: 'Integrity', text: 'Acting consistently with values, facts, and truth — even when inconvenient.' },
    { icon: 'FaSearch', label: 'Transparency', text: 'Making reasoning, progress, and constraints visible to all stakeholders.' }],
    band: 'These five behaviours are what hold a new practice in place.', notes: n.p17 });

  // ── Section 2 · Intelligence — Why
  await div(2);
  await d.prompt({ icon: 'FaFire', label: pt('2.1'), text: '“This matters to me. I am willing to invest energy in making this succeed.”',
    foot: 'Until that moment occurs across the organisation, strategy remains theoretical.', notes: n.p21 });
  await d.cards({ title: pt('2.2'), cols: 3, titleSize: 24, textSize: 24, items: [
    { icon: 'FaBolt', title: 'I. Potential vs. Kinetic Energy Logic', text: 'The organisation does not move until people decide to move it.' },
    { icon: 'FaBalanceScale', title: 'II. Compliance vs. Commitment Logic', text: 'Execution continues even when leaders are not present.' },
    { icon: 'FaTrophy', title: 'III. The Strategic Payoff of Alignment', dark: true, text: 'Leaders spend less time correcting and more time advancing strategy.' }],
    band: 'Aligning Heart & Mind is the mechanical conversion point where strategic potential becomes strategic movement.', notes: n.p22 });
  await pair({ title: pt('2.3'), cols: [
    { icon: 'FaPlug', title: 'Installed', points: ['The new system, structure or KPI is in place, and people have been told.', 'Installation is a project outcome.', 'What it yields: cost.'] },
    { icon: 'FaCheckDouble', title: 'Adopted', points: ['People work the new way without supervision.', 'Adoption is a behavioural outcome.', 'What it yields: value.'] }],
    band: 'The time between installed and adopted is the adoption gap.', notes: n.p23 });

  // ── Section 3 · Extrapolating — Where
  await div(3);
  await rows({ title: pt('3.1', 'a'), fontSize: 24, rows: [
    { icon: 'FaLightbulb', label: 'Openness', text: 'Curiosity, creativity, adaptability to new approaches' },
    { icon: 'FaTasks', label: 'Conscientiousness', text: 'Discipline, planning, follow-through on commitments' },
    { icon: 'FaComments', label: 'Extraversion', text: 'Outward energy, communication, collaboration comfort' },
    { icon: 'FaHandshake', label: 'Agreeableness', text: 'Harmony orientation, conflict management, cooperation' },
    { icon: 'FaAnchor', label: 'Emotional Stability', text: 'Composure under pressure, emotional resilience' },
    { icon: 'FaShieldAlt', label: 'Values Alignment', text: 'Consistency between stated values and lived behaviour' },
    { icon: 'FaGraduationCap', label: 'Learning Orientation', text: 'Growth mindset, openness to feedback, skill development' }], notes: n.p31a });
  await rows({ title: '3.1b · How the profile is read', fontSize: 24, rows: [
    { icon: 'FaUser', label: '1', text: 'Each participant scores themselves from 1 to 5 on each dimension.' },
    { icon: 'FaSlidersH', label: '2', text: 'A score of 4 or 5 is High, 3 is Balanced, and 1 or 2 is Low.' },
    { icon: 'FaUsers', label: '3', text: 'The level held by most members of a team is the team’s level for that dimension.' },
    { icon: 'FaClipboardList', label: '4', text: 'Each level carries a risk, a response and three routines that hold the response in place.' }],
    band: 'Every level carries a risk.', notes: n.p31b });

  // ── Section 4 · Integration — Collective
  await div(4);
  await pair({ title: pt('4.1'), cols: [
    { icon: 'FaCheckCircle', title: 'With Collective Intelligence', points: ['Direction remains clear across all layers', 'Resources reinforce priorities', 'Systems enable execution', 'People move with coordinated effort'] },
    { icon: 'FaTimesCircle', title: 'Without Collective Intelligence', points: ['Different leaders transmit different interpretations', 'Changes stall at the first check they fail', 'Functions receive competing signals', 'Strategic instability spreads invisibly'] }],
    band: 'One coherent signal across the organisation.', notes: n.p41 });
  // 4.2: each role with its alignment hot zone, one of the 17 elements of the toolkit (the page's own tags).
  grid({ title: pt('4.2'), cols: 2, items: [
    { name: 'CEO', parts: ['Mind · 3S · Shift'] },
    { name: 'CFO', parts: ['Habit · ACE-IT · Transparency'] },
    { name: 'COO', parts: ['Hands · STAT · Time'] },
    { name: 'CHRO', parts: ['Hands · STAT · Skill'] },
    { name: 'CTO/CIO', parts: ['Hands · STAT · Tools'] },
    { name: 'CMO', parts: ['Habit · ACE-IT · Engagement'] },
    { name: 'CCO', parts: ['Heart · SCARF · Fairness'] },
    { name: 'CPO', parts: ['Hands · STAT · Authority'] },
    { name: 'CRO', parts: ['Heart · SCARF · Autonomy'] },
    { name: 'CSO', parts: ['Mind · 3S · Stake'] }], notes: n.p42 });
  {
    const s = d.slide(); d.title(s, pt('4.3'));
    const items = [
      ['FaBullhorn', 'One message', 'Protects Mind', 'Every leader gives the same Shift, Stake and Step for each change.', false],
      ['FaUserTie', 'One example', 'Protects Heart', 'Leaders show the ACE-IT behaviours the change needs before they ask for them.', false],
      ['FaSortAmountDown', 'One sequence', 'Protects Hands', 'The team then agrees the order and the pace.', true],
      ['FaUserCheck', 'One owner', 'Protects Habit', 'Each transition has one named leader who answers for adoption, through to Habit.', true]];
    const gap = 0.3, top = 1.65, bottom = 6.95, cw = (12.13 - gap) / 2, ch = (bottom - top - gap) / 2, ib = 0.6;
    for (let i = 0; i < 4; i++) {
      const [ic, name, tag, text, dark] = items[i], x = 0.6 + (i % 2) * (cw + gap), y = top + Math.floor(i / 2) * (ch + gap);
      box(s, x, y, cw, ch, dark ? C.forest : C.tint);
      await badge(s, ic, x + 0.25, y + 0.22, ib, dark ? C.gold : C.forest, dark ? C.deep : C.white);
      T(s, [{ text: name, options: { bold: true, fontFace: F.head, color: dark ? C.white : C.forest } }, { text: ' · ', options: { color: dark ? C.goldLight : C.muted } },
        { text: tag, options: { italic: true, color: dark ? C.goldLight : C.muted } }], { x: x + 0.25 + ib + 0.2, y: y + 0.2, w: cw - ib - 0.7, h: 0.65, fontSize: 24, valign: 'middle' });
      T(s, text, { x: x + 0.25, y: y + 1.0, w: cw - 0.5, h: ch - 1.15, fontSize: 24, color: dark ? C.white : C.ink });
    }
    s.addNotes(n.p43);
  }

  // ── Section 5 · Application — In Practice (slides titled by step)
  await div(5);
  await rows({ title: `Step 1 · ${STEPS[0]}`, fontSize: 24, rows: [
    { icon: 'FaBrain', label: 'Mind · 3S', text: 'They understand the change, why it matters and what they do differently.' },
    { icon: 'FaHeart', label: 'Heart · SCARF', text: 'They want it to succeed.' },
    { icon: 'FaHandPaper', label: 'Hands · STAT', text: 'They are able to do it.' },
    { icon: 'FaSyncAlt', label: 'Habit · ACE-IT', text: 'It has become the way they work.' }],
    band: 'Act on the trigger. A response aimed at the cue leaves the trigger in place.', bandH: 1.05, notes: n.st1 });
  grid({ title: 'Step 1 · Worked example: resolve complaints at first contact', cols: 2, items: [
    { name: 'Mind · Step', parts: ['People agree with the change and carry on as before.'] },
    { name: 'Heart · Status', parts: ['Withholding information or cooperation.'] },
    { name: 'Hands · Authority', parts: ['People ask permission for what the change asks them to do.'] },
    { name: 'Habit · Accountability', parts: ['A missed commitment passes without a fix.'] }], notes: n.st1x });
  await rows({ title: `Step 2 · ${STEPS[1]}`, fontSize: 24, rows: [
    { icon: 'FaIdCard', text: 'Each card is one trigger, with the two cues that show it.' },
    { icon: 'FaCheckSquare', text: 'Select “Likely to surface in my area” on the triggers you expect as these changes land.' },
    { icon: 'FaPen', text: 'In the box that opens, write what you will do.' }],
    band: 'Start with the alignment hot zone of your own role in 4.2.', notes: n.st2 });
  await rows({ title: `Step 3 · ${STEPS[2]}`, fontSize: 24, rows: [
    { icon: 'FaUsers', text: 'Compare the watch lists of your group.' },
    { icon: 'FaCheckSquare', text: 'Select “Likely to surface for our strategy” on the triggers your group agrees on, for the strategy in your Capstone Blueprint.' },
    { icon: 'FaPen', text: 'In the boxes that open, write where the trigger will surface, what your team will do and the leader who owns it.' },
    { icon: 'FaUser', gold: true, text: 'Your 30-Day Behavioural Commitment' }],
    band: 'Read your record at the foot of this step, then select Confirm.', notes: n.st3 });
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · The closing question', text: CLOSING_Q, notes: n.summary });

  if (used.size !== Object.keys(INS).length) throw new Error('insights not all used: ' + Object.keys(INS).filter(k => !used.has(k)).join(', '));
  await d.save(OUT);

  // Spec for add_reflection_slides.py: the reflection slides of Sections 1 to 4, each after the last content slide of its section.
  // Section 1 has seven reflections and takes two slides. Where two slides share an anchor, the later one is listed first
  // (the script places each straight after the anchor).
  const pic = k => ({ part: k, file: `ref_${k}.png`, alt: `${k} ${REFL[k].label}: ${REFL[k].prompt}` });
  const spec = { title_model: 'Key learning outcomes', slides: [
    { title: 'Section 1 Reflections · 1.3.1 to 1.3.4', after: pt('1.3.4'), notes: n.ref1b, pictures: ['1.3.1', '1.3.2', '1.3.3', '1.3.4'].map(pic) },
    { title: 'Section 1 Reflections · 1.1 to 1.3', after: pt('1.3.4'), notes: n.ref1a, pictures: ['1.1', '1.2', '1.3'].map(pic) },
    { title: 'Section 2 Reflections', after: pt('2.3'), notes: n.ref2, pictures: ['2.1', '2.2', '2.3'].map(pic) },
    { title: 'Section 3 Reflections', after: '3.1b · How the profile is read', notes: n.ref3, pictures: ['3.1'].map(pic) },
    { title: 'Section 4 Reflections', after: pt('4.3'), notes: n.ref4, pictures: ['4.1', '4.2', '4.3'].map(pic) }] };
  fs.mkdirSync(path.join(HERE, 'reflections', 'u05'), { recursive: true });
  fs.writeFileSync(path.join(HERE, 'reflections', 'u05', 'spec.json'), JSON.stringify(spec, null, 1));
  console.log('saved', OUT, '· insights used:', used.size);
})().catch(e => { console.error(e); process.exit(1); });
