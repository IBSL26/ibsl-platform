// Unit 2 · Strategy Visioning & Success in Practice (SiP) — facilitator deck with detailed presenter notes.
// Run: node unit02.js "<output.pptx>" [logo.png] [outline.json] [unit F html] [unit P html]
const { Deck, C, F, T, box } = require('./lib2');
const { Unit, N } = require('./kit');
const path = require('path');
const R = (...p) => path.join(__dirname, '..', '..', ...p);
const [OUT, LOGO = R('logo.png'), JSONP = path.join(__dirname, 'outlines', 'u02.json'), FH = R('unit2_m1_lens1_f.html'), PH = R('unit2_m1_lens1_p.html')] = process.argv.slice(2);
const u = new Unit(JSONP, FH, PH);

async function divider(d, i, extra) {
  const s = u.sec(i), m = /Section (\d+) · (\S+) — (.+)/.exec(s.label);
  await d.section({ num: +m[1], name: m[2], anchor: m[3], heading: s.h2, outcomes: s.slo, notes: u.secNotes(i, extra) });
}

(async () => {
  const d = new Deck({ unit: 2, module: 2, moduleName: 'Direction', title: 'Strategy Visioning & Success in Practice (SiP)' });
  const CONCEPTS = u.js('CONCEPTS'), W1H = u.js('W1H'), ENGINE = u.js('ENGINE'), ARCH = u.js('ARCH'), DIMS = u.js('DIMS'),
    FLAMS = u.js('FLAMS'), CXO = u.js('CXO'), ASSESS = u.js('ASSESS'), SIP_QS = u.js('SIP_QS'), SIP_LABELS = u.js('SIP_LABELS'), SUMMARY = u.js('SUMMARY');
  const G = u.guide();

  await d.cover({ logo: LOGO, subtitle: 'Building a shared Strategic Intent and a Success in Practice narrative',
    notes: N('UNIT 2 · STRATEGY VISIONING & SUCCESS IN PRACTICE (SiP)\nModule 2 · Direction · Unit 2',
      G[0].replace('Unit Intent', 'Unit intent (Facilitator Guide):'),
      'Unit overview (facilitator file): This unit builds the master definition of strategy, the 3W1H framework, and produces two integrated outputs — a Strategic Intent Statement and a Success in Practice narrative — through collective executive co-creation.',
      'Time: section timings in the facilitator file add up to 175–240 minutes (about 3 to 4 hours), plus breaks.') });

  await d.list({ title: 'Key learning outcomes', fontSize: 24, rows: u.F.klo.map(t => ({ icon: 'FaCheck', text: t })),
    notes: N('KEY LEARNING OUTCOMES (identical in the participant and facilitator files)', u.F.klo.map((t, k) => `${k + 1}. ${t}`).join('\n'), 'Each section slide carries that section’s two learning outcomes.') });

  await d.list({ title: 'The unit journey', fontSize: 28, rows: [
    { icon: 'FaEye', label: 'Section 1 · Awareness', text: '— What' },
    { icon: 'FaLightbulb', label: 'Section 2 · Intelligence', text: '— Why' },
    { icon: 'FaMapMarkedAlt', label: 'Section 3 · Extrapolating', text: '— Where' },
    { icon: 'FaUsers', label: 'Section 4 · Integration', text: '— Collective' },
    { icon: 'FaClipboardCheck', label: 'Section 5 · Application', text: '— In Practice' }],
    notes: N('FACILITATOR GUIDE · SESSION OVERVIEW',
      'Time by section (from the facilitator file):\n- Section 1 · Awareness — What: 25–35 minutes\n- Section 2 · Intelligence — Why: 20–25 minutes\n- Section 3 · Extrapolating — Where: 20–25 minutes\n- Section 4 · Integration — Collective: 55–75 minutes\n- Section 5 · Application — In Practice: 55–80 minutes',
      G[1], G[2]) });

  // ── Section 1
  await divider(d, 1);
  await d.prompt({ label: 'Opening the session', text: 'Write your definition of strategy in one sentence — right now, without consulting anyone.',
    notes: N('OPENING THE SESSION',
      'Before showing any content, ask participants: “Write your definition of strategy in one sentence — right now, without consulting anyone.”',
      'Collect 3–4 responses. Note the differences on a whiteboard. This gap between answers is exactly the problem this unit solves. Use it as the opening provocation.',
      'Keep these definitions: you return to them at the Unit Summary.') });
  await d.prompt({ icon: 'FaQuoteLeft', label: '1.1 · Strategy Master Definition', text: 'Strategy is the output of iterative thinking, logic and process to determine what, why, how and when an organisation creates, delivers and sustains value to its stakeholders while navigating the forces within its operating environment.',
    notes: u.partNotes(1, 0) });
  await d.list({ title: '1.1 · Every word carries strategic weight', fontSize: 24, rows: CONCEPTS.map(c => ({ icon: 'FaKey', label: c.badge, text: c.name })),
    notes: N('1.1 · THE MASTER DEFINITION CONCEPTS (expand each in the file)',
      CONCEPTS.map(c => `${c.badge} — ${c.name}\nWhat it means: ${c.what}\nStrategic implication: ${c.impl}\nFailure mode: ${c.fail}`).join('\n\n')) });
  await d.cards({ title: '1.2 · Strategic Intent: the 3W1H framework', cols: 4, titleSize: 28, textSize: 24, items: W1H.map((w, k) => ({ icon: ['FaBullseye', 'FaHeart', 'FaCogs', 'FaClock'][k], title: w.name, text: w.sub })),
    band: 'Most strategies fail because HOW and WHEN are underdeveloped.',
    notes: N(u.partNotes(1, 1),
      'The four dimensions (tabs in the file):\n\n' + W1H.map(w => `${w.name} — ${w.sub}\nCore question: ${w.q}\nGoverns: ${w.governs}\nDiagnostic questions: ${w.diag.join(' · ')}`).join('\n\n')) });
  await d.cards({ title: '1.3 · Success in Practice: four observable domains', cols: 2, titleBeside: true, titleSize: 26, iconSize: 0.6, items: SIP_LABELS.map((l, k) => ({ icon: ['FaSmile', 'FaCogs', 'FaUsers', 'FaChartLine'][k], title: `D${k + 1} · ${l}` })),
    band: 'Headline: the destination in one sentence. Storyline: the four-dimensional narrative.',
    notes: u.partNotes(1, 2) });
  await d.prompt({ label: 'Closing Awareness', text: 'What is one word that describes the gap between where your organisation currently is and the SiP you just imagined?',
    notes: N('CLOSING AWARENESS', 'After section 1.3, pause before moving to Intelligence. Ask participants: “What is one word that describes the gap between where your organisation currently is and the SiP you just imagined?”', 'Capture the words — they will resurface in the Integration section.') });

  // ── Section 2
  await divider(d, 2);
  await d.list({ title: '2.1 · Why intent and SiP must be co-created', fontSize: 26, rows: [
    { icon: 'FaHandshake', label: 'Shared destination:', text: 'leaders agree through genuine shared construction' },
    { icon: 'FaBalanceScale', label: 'Visible trade-offs:', text: 'tensions surface in the room, before execution' },
    { icon: 'FaUsers', label: 'Collective ownership:', text: 'the only ownership that sustains under execution pressure' }],
    notes: u.partNotes(2, 0) });
  await d.cards({ title: '2.2 · The Strategy Engine', cols: 3, items: ENGINE.map((e, k) => ({ icon: ['FaBrain', 'FaProjectDiagram', 'FaSyncAlt'][k], title: e.name, text: e.sub.split(' — ')[0] })),
    band: 'Most focus on Process, add some Iteration, and largely ignore Thinking Logic.',
    notes: N(u.partNotes(2, 1),
      'The three layers (tabs in the file):\n\n' + ENGINE.map(e => `${e.name} — ${e.sub}\nWhat it is: ${e.what}\nHow it works: ${e.how}\nWhere it fails: ${e.fail}`).join('\n\n')) });
  await d.cards({ title: '2.3 · Intent and SiP in the S2R® architecture', cols: 3, items: ARCH.map((a, k) => ({ icon: ['FaCompass', 'FaFilter', 'FaLink'][k], title: a.fn })),
    notes: N(u.partNotes(2, 2, { content: false }),
      'The three functions (Strategic Intent · SiP):\n\n' + ARCH.map(a => `${a.fn}\nStrategic Intent: ${a.si}\nSiP: ${a.sip}`).join('\n\n')) });

  // ── Section 3
  await divider(d, 3);
  await d.cards({ title: '3.1 · The four SiP dimensions', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: DIMS.map((x, k) => ({ icon: ['FaSmile', 'FaCogs', 'FaUsers', 'FaChartLine'][k], title: ['D1 · Customer Experience', 'D2 · Operational Capability', 'D3 · People & Culture', 'D4 · Enterprise Value'][k], text: ['CARE: Connection · Access · Results · Effort', 'Priority Clarity · Decision Flow · Coordination · Delivery Rhythm', x.inds.map(i => i.name).join(' · '), x.inds.map(i => i.name).join(' · ')][k] })),
    notes: N(u.partNotes(3, 0),
      'Observable indicators (“What good looks like” · “What’s missing”):\n\n' + DIMS.map((x, k) => `D${k + 1} · ${x.name.toUpperCase()}\n${x.intro}\n` + x.inds.map(i => `- ${i.name}\n  Good: ${i.good}\n  Missing: ${i.miss}`).join('\n')).join('\n\n')) });
  await d.cards({ title: '3.2 · SiP Flammables: where imbalance creates drift', cols: 2, titleBeside: true, titleSize: 26, iconSize: 0.6, items: FLAMS.map((f, k) => ({ icon: 'FaFire', title: f.dim })),
    notes: N(u.partNotes(3, 1),
      'The four Flammables:\n\n' + FLAMS.map(f => `${f.dim}\nWhat it looks like: ${f.what}\nRisk: ${f.risk}`).join('\n\n')) });

  // ── Section 4
  await divider(d, 4);
  {
    const s = d.slide(); d.title(s, '4.1 · Executive leader perspectives');
    box(s, 0.6, 1.65, 12.13, 1.9, C.forest);
    T(s, 'Each role naturally emphasises its domain: many partial pictures, each accurate and collectively incomplete.', { x: 0.9, y: 1.65, w: 11.6, h: 1.9, fontSize: 28, color: C.white, valign: 'middle' });
    const roles = Object.keys(CXO);
    for (let i = 0; i < roles.length; i++) {
      const x = 0.6 + (i % 5) * 2.465, y = 4.0 + Math.floor(i / 5) * 1.2;
      box(s, x, y, 2.2, 0.95, C.tint);
      T(s, roles[i], { x, y, w: 2.2, h: 0.95, fontSize: 28, bold: true, color: C.forest, align: 'center', valign: 'middle' });
    }
    s.addNotes(N(u.partNotes(4, 0),
      'The ten executive roles (natural bias · integration challenge):\n\n' + roles.map(r => `${r} — ${CXO[r].t}\nNatural bias: ${CXO[r].b}\nIntegration challenge: ${CXO[r].c}`).join('\n\n')));
  }
  await d.list({ title: '4.2 · Strategy Maturity Assessment: six groups', fontSize: 26, rows: ASSESS.map(a => ({ icon: 'FaClipboardList', label: a.lbl, text: a.desc })),
    notes: N(u.partNotes(4, 1),
      'The 26 areas (score 0 = Not addressed · 1 = Partially · 2 = Substantially · 3 = Fully embedded):\n\n' + ASSESS.map(a => `${a.lbl} — ${a.desc}\n` + a.items.map(i => `${i.n}. ${i.t}: ${i.s}\n   Question: ${i.q}`).join('\n')).join('\n\n')) });
  await d.stat({ title: '4.2 · Reading the maturity score', big: '78', caption: 'maximum score: 26 areas, each scored 0–3',
    rows: [{ icon: 'FaExclamationTriangle', label: '0–26 Foundational Gaps', text: 'strategy remains fragile and personality-dependent' },
      { icon: 'FaSeedling', label: '27–52 Developing Capability', text: 'key dimensions present; integration incomplete' },
      { icon: 'FaTrophy', label: '53–78 Strategic Maturity', text: 'strategy is embedded as organisational capability' }],
    notes: N('4.2 · SCORE INTERPRETATION AND DEBRIEF',
      'Score interpretation: 0–26 = Foundational Gaps (strategy is fragile, personality-dependent). 27–52 = Developing Capability (key dimensions present but integration incomplete). 53–78 = Strategic Maturity (strategy is embedded as organisational capability). Most first-time groups score in the 20–45 range — normalise this and focus on the direction of travel.',
      'Group debrief after scoring — use these three questions in sequence:\n1. “Which group (A–F) scored lowest across the team — and was there consensus on that?”\n2. “Where was the widest divergence in scores? What does that disagreement tell us?”\n3. “What is the single most important corrective action this score points to in the next 90 days?”',
      'Using the export function: Direct participants (or the lead facilitator) to use “Screen View” or “Save as PDF” to generate the maturity report. This becomes a baseline document for the organisation’s S2R® journey — it should be retained and revisited at the end of the programme.') });
  await d.list({ title: '4.3 · Collective SiP exercise', fontSize: 26, rows: [
    { icon: 'FaUserTie', label: 'Assigned roles:', text: 'no self-selection' },
    { icon: 'FaPenFancy', label: 'Present tense of the future:', text: '“we have…”, “customers experience…”' },
    { icon: 'FaVolumeMute', label: '10–12 minutes, in silence:', text: 'all four dimensions from your role' },
    { icon: 'FaUsers', gold: true, label: 'Then synthesise:', text: 'one working SiP, genuinely shared' }],
    notes: N(u.partNotes(4, 2),
      'The four SiP dimension prompts participants answer from their role:\n' + SIP_LABELS.map((l, k) => `- ${l}: ${SIP_QS[k]}`).join('\n')) });
  await d.list({ title: '4.3 · Running the synthesis', fontSize: 26, rows: [
    { icon: 'FaCompressArrowsAlt', label: 'Converge:', text: 'your strongest strategic signal' },
    { icon: 'FaBolt', label: 'Compete:', text: 'where trade-off decisions are needed' },
    { icon: 'FaSearch', label: 'Least described:', text: 'your white space — who owns it?' },
    { icon: 'FaBalanceScale', label: 'Dominant perspective:', text: 'how do we rebalance?' }],
    notes: N('4.3 · RUNNING THE SYNTHESIS',
      'After individual contributions are complete, use the “View All Responses” function to display contributions side by side. Facilitate the synthesis using four questions:\n1. “Where do all perspectives converge? This is your strongest strategic signal.”\n2. “Where do perspectives compete or contradict? This is where trade-off decisions are needed.”\n3. “Which SiP dimension is least well-described across all contributions? This is your white space — who owns it?”\n4. “Which functional perspective dominates the collective narrative? How do we rebalance?”',
      'Producing the collective output: The facilitator (or a nominated scribe) drafts a single integrated SiP from the synthesis discussion. This draft becomes the working SiP for the organisation — it will be tested, refined, and embedded across subsequent units. It needs to be genuinely shared today; refinement follows in later units.') });

  // ── Section 5
  await divider(d, 5);
  await d.cards({ title: '5.1 · From assessment to corrective actions', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaSmile', title: 'D1 · Customer Experience & Value', text: 'What must change to close the gap to the SiP vision?' },
    { icon: 'FaCogs', title: 'D2 · Operational Capability', text: 'What operational gaps must be closed?' },
    { icon: 'FaUsers', title: 'D3 · People & Culture Dynamics', text: 'What cultural and behavioural shifts are required?' },
    { icon: 'FaChartLine', title: 'D4 · Enterprise Value Creation', text: 'What must be strengthened for durable value?' }],
    notes: u.partNotes(5, 0) });
  await d.list({ title: '5.2 · CXO SiP Application Table', fontSize: 26, rows: [
    { icon: 'FaUserTie', label: 'Your assigned role:', text: 'all four dimensions' },
    { icon: 'FaPenFancy', label: 'Present tense of the future:', text: 'as if the strategy has already succeeded' },
    { icon: 'FaFire', gold: true, label: 'Self-audit:', text: 'which Flammable does your response risk creating?' }],
    notes: u.partNotes(5, 1) });
  await d.compare({ title: '5.3 · SiP Headline and Storyline', cols: [
    { icon: 'FaFlag', title: 'Headline', sub: 'Strategic vision anchor', points: ['One sentence', 'The strategic destination', 'Leaders repeat it everywhere'] },
    { icon: 'FaBookOpen', title: 'Storyline', sub: 'Strategic narrative', points: ['The future organisation', 'Across the four dimensions', 'Present tense of the future'] }],
    band: 'Draft the composite together: no single executive writes it alone.',
    notes: u.partNotes(5, 2) });
  await d.cards({ title: '5.4 · Integration Summary', cols: 2, titleBeside: true, titleSize: 26, textSize: 24, iconSize: 0.6, items: [
    { icon: 'FaCompressArrowsAlt', title: '1 · Points of Convergence', text: 'Where all CXO descriptions aligned.' },
    { icon: 'FaBolt', title: '2 · Points of Tension', text: 'Where perspectives contradicted or competed.' },
    { icon: 'FaSearch', title: '3 · Missing Dimensions', text: 'The collective blind spot.' },
    { icon: 'FaBalanceScale', title: '4 · Dominant Bias', text: 'Which functional perspective was over-represented.' }],
    notes: u.partNotes(5, 3) });
  await d.prompt({ label: 'Closing the Application section', text: 'Is the gap between what we described and what we currently have strategic or operational? And who in this room is accountable for closing it?',
    notes: N('CLOSING QUESTION (Section 5.4)', 'End with the question: “We have now described the organisation we intend to build. The gap between what we described and what we currently have — is that gap strategic or operational? And who in this room is accountable for closing it?”') });
  {
    const pp = u.P.sections[4].parts.find(p => /Portfolio/.test(p.title));
    await d.cards({ title: 'Portfolio Artefact', cols: 3, items: [
      { icon: 'FaPenFancy', title: 'What Has Shifted', text: 'The assumption about strategy this unit challenged.' },
      { icon: 'FaFlagCheckered', title: 'My Commitment to Action', text: 'One action within 30 days to strengthen strategic clarity.' },
      { icon: 'FaBullseye', title: 'My Development Priority', text: 'Your single most important area of the 26.' }],
      notes: N('PORTFOLIO ARTEFACT (participant file: 3 prompts · submit to facilitator)',
        'Participant activity (participant file, Section 5 · Portfolio Artefact):\n' + pp.prompts.map(x => '- ' + x).join('\n'),
        'Participants save the artefact, then submit Unit 2 to the facilitator from their file (supporting documents can be attached).') });
  }
  await d.prompt({ icon: 'FaRedo', label: 'Unit Summary · Return to the opening question', text: 'Read your original definition of strategy. What would you change in it now — and why?',
    foot: 'Based on what Unit 2 revealed, the one thing I am committed to doing differently before our next session is…',
    notes: N(u.partNotes(5, 4, { content: false }),
      'Unit Summary (read aloud, section by section):\n\n' + SUMMARY.map(s => `${s.arc} · ${s.t}\n${s.body}`).join('\n\n')) });

  await d.save(OUT); console.log('saved');
})().catch(e => { console.error(e); process.exit(1); });
