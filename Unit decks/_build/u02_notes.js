// Unit 2 · presenter notes for the rebuilt deck (October 2026).
//
// STRUCTURE OF EVERY NOTES PAGE (Carol, 5 October 2026, on the worked slides 6 and 7: "the slide 6 and 7 format you gave
// me is what you must do"; "the notes must flow as a conversation that the facilitator [has] during the class"):
//   1. HEADING in capitals.
//   2. HOW TO TEACH IT (HOW TO USE THIS SLIDE on reflection slides; HOW THIS SECTION RUNS, SECTION LEARNING OUTCOMES and
//      HOW TO OPEN THE SECTION on section slides): numbered steps in the order they happen in class. Every step has a title
//      and, under it, what the facilitator says ("Say:"), asks ("Ask:"), does, or listens for ("Listen for:").
//   3. Nothing sits loose after the steps. The facilitator script, the content of the cards, each journal insight and each
//      line of manuscript detail sit INSIDE the step where they are used. An insight is spoken ("Deepen, say:") and is
//      followed by its reference line: (Insight: Title. Source: Journal, …).
//   4. Last: ON THE PORTAL, AFTER THE TEACHING (what participants complete once the teaching is over) and, in Sections 4
//      and 5, LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL (coaching for the portal work).
// A line that starts with § is a heading or a step title: format_notes.py removes the mark and makes the line bold.
//
// ALIGNMENT: the notes carry only what the facilitator and participant files carry today. Removed on 5 October because
// the files no longer have them: the private 1-to-5 rating in 1.2, the "Critical Insight" lines, and the probing
// questions that came from the old maturity assessment. check_alignment.py tests the notes against the facilitator file.
//
// TEACHING FLOW: the deck is the teaching material. The facilitator teaches the whole unit from the deck first;
// participants go to the portal afterwards. No note steers participants through the portal while the facilitator teaches.
// Carol's rules: no timings, no pre-work, no contrast constructions, "domains" for the four SiP areas,
// "dimensions" for WHAT / WHY / HOW / WHEN.
// Slides 1 to 4 carry Carol's own notes (carol_notes_1_4.json); the final deck keeps them exactly as she wrote them.
const fs = require('fs');
const path = require('path');
const { N } = require('./kit');

module.exports = function (u, INS) {
  const used = new Set();
  const H = t => '§' + t;
  const up = t => t.toUpperCase().replace(/\bSIP\b/g, 'SiP');
  const noq = s => { if (/"/.test(s)) throw new Error('straight quote inside a spoken line: ' + s.slice(0, 80)); return s; };
  const say = (s, cue = 'Say') => `${cue}: "${noq(s)}"`;
  const ask = s => `Ask: "${noq(s)}"`;
  // A journal insight inside a step: the words to say, then the reference line.
  // opt.then: text from which the insight is an instruction to the facilitator (printed as a plain line, unspoken).
  const IN = (id, cue = 'Deepen, say', opt = {}) => {
    const x = INS[id]; if (!x) throw new Error('unknown insight ' + id);
    if (used.has(id)) throw new Error('insight used twice: ' + id); used.add(id);
    const ref = `(Insight: ${x.title.replace(/\.$/, '')}. Source: ${x.source})`;
    const t = x.text; const out = [];
    if (opt.then) {
      const k = t.indexOf(opt.then); if (k < 0) throw new Error(`insight ${id}: "${opt.then}" not found`);
      out.push(say(t.slice(0, k).trim(), cue), 'Then: ' + t.slice(k).trim());
    } else {
      const m = t.match(/^([\s\S]*?)\s*Ask: “([^”]+)”\s*([\s\S]*)$/);
      if (m) { out.push(say(m[1], cue), ask(m[2])); if (m[3]) out.push(say(m[3], 'Then say')); }
      else out.push(say(t, cue));
    }
    return [...out, ref];
  };
  const strip = l => l.replace(/^◆ /, '').replace(/^📋 /, '');
  const lead = (i, k) => u.sec(i).lead.guidance[k].map(strip);
  const gd = (i, j, k = 0) => u.part(i, j).guidance[k].map(strip);
  // One line of a guidance block of the facilitator page, found by how it starts (stops the build if the page changes).
  // With cut = true the label ("Explain: ") is removed.
  const pick = (lines, start, cut = false) => {
    const hit = lines.filter(l => l.startsWith(start));
    if (hit.length !== 1) throw new Error(`guidance line "${start}" found ${hit.length} times`);
    return cut ? hit[0].slice(start.length).trim() : hit[0];
  };
  const meta = m => m.replace(/ · Click (to expand each|indicators to expand)/, '');   // the page's own instruction is left out
  const head = (i, j, tail = '') => { const p = u.part(i, j); return H(tail ? up(p.title) + ' · ' + tail : up(p.title + (p.meta ? ' (' + meta(p.meta) + ')' : ''))); };
  const PORTAL = 'ON THE PORTAL, AFTER THE TEACHING:';
  const LATER = 'LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:';
  const portal = (...lines) => H(PORTAL) + '\n' + lines.flat().join('\n');
  const later = (...lines) => H(LATER) + '\n' + lines.flat().join('\n');
  // One step: [title, line, line, …]. Arrays are flattened, empty entries dropped.
  const S = (title, ...lines) => [title, ...lines.flat(Infinity).filter(x => x !== '' && x !== null && x !== undefined && x !== false)];
  const steps = items => items.filter(Boolean).map((it, k) => H(`${k + 1}. ${it[0]}`) + (it.length > 1 ? '\n' + it.slice(1).join('\n') : ''));
  // A content slide: heading, HOW TO TEACH IT, the steps, then the closing blocks.
  const page = (heading, items, ...tail) => N(heading, H('HOW TO TEACH IT:'), steps(items), tail);
  // The reflection prompt of a part, from the participant page.
  const refl = (i, j) => {
    const pr = u.ppart(i, j).prompts.map(x => x.replace(/^✍/, '')).filter(x => /^✎ Reflection — /.test(x));
    if (pr.length !== 1) throw new Error(`reflection prompt of ${i}.${j + 1}: found ${pr.length}`);
    // the label of the box and the grey hint inside the box are left out
    return pr[0].replace(/^✎ Reflection — (Strategy Architecture|Strategy Intent|Three Functions|SiP Indicators|Application) /, '').replace(/ — (Write|Record|Describe|Note|Type|Enter)\b[^?]*$/, '').trim();
  };
  const G = u.guide();
  const CONCEPTS = u.js('CONCEPTS'), W1H = u.js('W1H'), ARCH = u.js('ARCH'), DIMS = u.js('DIMS'), FLAMS = u.js('FLAMS'), SUMMARY = u.js('SUMMARY');
  const EL = u.js('EL', 'P'), SIPD = u.js('SIPD', 'P'), ROLES = u.js('APP_ROLES', 'P'), APP_DIMS = u.js('APP_DIMS', 'P'), GROUPS = u.js('ARCH_GROUPS', 'P');
  const clean = s => String(s).replace(/<[^>]+>/g, '');
  // Section slide, on the model Carol gave slide 4 (heading, how the section runs, the two outcomes), followed by the
  // steps for opening the section, so that every line of the section guidance is something the facilitator says or does.
  const divider = (i, runs, items, ...tail) => {
    const s = u.sec(i);
    return N(H(up(s.label)),
      H('HOW THIS SECTION RUNS:') + '\n' + runs,
      H('SECTION LEARNING OUTCOMES:') + '\n' + s.slo.map((o, k) => `${k + 1}. ${o}`).join('\n'),
      H('HOW TO OPEN THE SECTION:'), steps(items), tail);
  };
  // Reflection slide. Carol's two lines from her Unit 1 deck open the notes.
  const reflection = (num, items, where) => N(H(`SECTION ${num} REFLECTIONS`), H('HOW TO USE THIS SLIDE:'), steps(items), portal(where));
  // Carol's two lines from her Unit 1 deck, word for word, as the step that says what the reflections are for.
  const reflFor = (plural, extra = '') => S(plural ? 'Say what the reflections are for.' : 'Say what the reflection is for.',
    'Point learners to the portal section that they will be required to complete with as much depth as possible. The reflections build the learning portfolio they receive at the end of the programme.',
    say(`You write ${plural ? 'these reflections' : 'this reflection'} on the portal after the teaching${extra}, with as much depth as you can.`));
  const n = {};
  const CAROL = JSON.parse(fs.readFileSync(path.join(__dirname, 'carol_notes_1_4.json'), 'utf8'));

  // ════════════════════════════════════════════════════════════════════════ FRONT (Carol's own notes)
  n.cover = CAROL['1']; n.klo = CAROL['2']; n.journey = CAROL['3']; n.s1 = CAROL['4'];

  // ════════════════════════════════════════════════════════════════════════ SECTION 1
  const op = lead(1, 1), script = lead(1, 3);
  const opAsk = pick(op, 'Ask: ', true), opCollect = pick(op, 'Collect: ', true);
  pick(op, 'Keep: Ask every participant to keep their definition. The Unit Summary returns to it.');
  if (!opAsk.includes('"Write your definition of strategy in one sentence — right now, without consulting anyone."')) throw new Error('opening sentence changed on the facilitator page');
  if (opCollect !== 'Collect 3–4 responses. Note the differences on a whiteboard. This gap between answers is exactly the problem this unit solves. Use it as the opening provocation.') throw new Error('Collect line changed');
  n.open = page(H('OPENING THE SESSION'), [
    S('Ask for the definition.',
      'Before showing any content, put this slide up and ask each participant to define strategy in their own words.',
      say('Write your definition of strategy in one sentence — right now, without consulting anyone.'),
      'Participants write on paper, without conferring.'),
    S('Collect three or four responses.',
      'Ask three or four participants to read their sentence aloud, word for word. Note the differences on a whiteboard.'),
    S('Ask the room what it hears.',
      ask('What do these definitions have in common? Where do they differ?'),
      'Listen for: definitions that describe a plan ("the steps we take to…"), definitions that stop at ambition ("where we want to be in five years"), and definitions with no mention of value, stakeholders or the operating environment.',
      'Hold back from correcting any definition. The differences on the whiteboard are the material.'),
    S('Name what you see.',
      say('Some of our definitions describe a plan. Some describe an ambition. Some describe a competitive intention.')),
    S('Use the gap as the opening provocation.',
      say('This gap between our answers is exactly the problem this unit solves. This unit gives us one precise definition of strategy and the architecture that sits underneath it.')),
    S('Keep the definitions.',
      say('Keep your sentence. We return to it at the Unit Summary.'),
      'Leave the differences on the whiteboard: you return to them at the Unit Summary.'),
  ], portal(lead(1, 2).slice(1)));

  // 1.1a · the definition. The facilitator script of the page is spoken across steps 2, 4, 5, 7, 8 and 9, words unchanged.
  const explain = pick(script, 'Explain: ', true).replace(/^"|"$/g, '');
  const bridgeDef = pick(script, 'Bridge to the definition: ', true).replace(/^"|"$/g, '');
  const bd = ['We are now going to unpack the Strategy2Results® definition of strategy.', 'Each concept in the definition represents part of the architecture.', 'Once we understand the parts and how they connect, we can begin constructing a coherent strategic position.'];
  if (bridgeDef !== bd.join(' ')) throw new Error('facilitator script changed: Bridge to the definition');
  pick(script, 'Set the frame: Before defining strategy, introduce Strategy Architecture as the underlying logic that gives a strategy its structure.');
  pick(script, 'Emphasise that the purpose of this section is to unpack the architecture before trying to produce a strategy statement. A strategy can sound compelling while important parts of its underlying logic remain weak, disconnected or undefined.');
  pick(script, 'As participants work through the concepts, ask them to consider: "How well defined is each part of our strategy architecture today?"');
  const definition = u.part(1, 0).content[0].replace(/^"|"$/g, '');
  n.def = page(head(1, 0), [
    S('Link to the opening exercise.',
      say('We have just heard several definitions of strategy in this room. Strategy is frequently used but rarely precisely defined. In most organisations it functions as shorthand for ambition, planning, or competitive intention, with each executive leader carrying a slightly different version of the word. In the Strategy2Results® framework, strategy has a specific applied definition.')),
    S('Set the frame.',
      'Before defining strategy, introduce Strategy Architecture as the underlying logic that gives a strategy its structure.',
      say(explain)),
    S('Say why architecture comes first.', IN('bringing_order', 'Say')),
    S('Explain the purpose of this section.',
      say('The purpose of this section is to unpack the architecture before trying to produce a strategy statement. A strategy can sound compelling while important parts of its underlying logic remain weak, disconnected or undefined.')),
    S('Read the definition.',
      say(bd[0]),
      'Read the definition on the slide aloud once, slowly:',
      `"${noq(definition)}"`,
      'Ask one participant to read it a second time.',
      say('Every word carries strategic weight.', 'Then say')),
    S('Compare it with the definitions of the room.',
      ask('Which words in this definition are missing from ours?'),
      'Take two or three answers. Listen for: value, stakeholders, the forces, the operating environment. These are the words most opening definitions leave out.'),
    S('Name the parts.',
      'Point to each part of the definition as you name it: the output · iterative thinking, logic and process · what, why, how and when · creates, delivers and sustains value · stakeholders · navigating the forces · the operating environment.',
      say(bd[1])),
    S('Leave one question in the room.',
      say('As we work through the concepts, consider: How well defined is each part of our strategy architecture today?')),
    S('Bridge to the next slide.',
      say(bd[2] + ' For each concept we look at three things: what it means, what it implies for execution, and what breaks when it is absent.')),
  ]);

  // 1.1b · the nine concepts. Card text comes from the page (CONCEPTS); "Add" lines are S2R® manuscript detail.
  const g11 = gd(1, 0);
  pick(g11, 'Taking participants through the 9 concepts: Take the concepts one at a time: what each one means, its strategic implication and what fails when it is missing. Then ask: "Which of these nine concepts is least visible in how your organisation currently talks about strategy?"');
  pick(g11, 'Key concept to linger on: The distinction between Thinking & Logic (the cognitive engine) and Process (the structured container). Most organisations have process but neglect thinking quality');
  pick(g11, 'The Value Triad (Creates · Delivers · Sustains): Draw explicit attention to this concept. Ask: "Is your current strategy as strong on Sustains as it is on Creates and Delivers? Where is the investment in sustainability of value?" This often surfaces an uncomfortable silence.');
  const cx = {
    'OUTPUT': [say('The decided position is distinct from a plan, a meeting, the process of strategising, the presentation deck, and the off-site discussion.', 'Add'),
      'Listen for: "our strategy is the five-year plan". Ask: "What position did that plan decide?"'],
    'ITERATIVE': [say('This rules out strategy as an annual ritual and rules in strategy as a living organisational capability.', 'Add')],
    'THINKING & LOGIC': [say('Strategy needs reasoning as well as inspiration.', 'Add'), IN('rigid_mental_models')],
    'PROCESS': [say('With process, strategy stops being a personality-dependent event. Process is the scaffolding that makes thinking transferable.', 'Add'), IN('the_mission_larger_than_the_contributor')],
    'WHAT · WHY · HOW · WHEN': [say('Together the four dimensions constitute a complete strategic position. WHEN without WHAT is urgency without direction.', 'Add'),
      'Tell participants: the next slide takes these four dimensions in detail.'],
    'CREATES · DELIVERS · SUSTAINS': ['Draw explicit attention to this concept.',
      ask('Is your current strategy as strong on Sustains as it is on Creates and Delivers? Where is the investment in sustainability of value?'),
      'This often surfaces an uncomfortable silence. Let the silence stand before you take an answer.',
      IN('value_for_whom', 'Lead into the next concept, say')],
    'STAKEHOLDERS': [say('The blind spots are specific: employees who deliver value, investors who fund it, regulators who permit it.', 'Add'),
      'Listen for: stakeholders answered as "customers". Ask: "Who else has a stake in what this organisation does?"'],
  };
  const card = c => {
    let what;
    if (c.badge === 'THE FORCES') {          // the five categories are read as a list
      const p = c.what.split(/\s*\(\d\)\s*/);
      if (p.length !== 6) throw new Error('THE FORCES card changed');
      what = [say(p[0].replace(/:$/, '.'), 'What it means, say'), 'Name the five categories, one at a time:', ...p.slice(1).map((x, k) => `${k + 1}. ${x.replace(/[;.]$/, '').replace(' — ', ': ')}.`)];
    } else what = [say(c.what.replace(/ → /g, ', '), 'What it means, say')];
    return S(`${c.badge} — ${c.name}.`, what, say(c.impl, 'Strategic implication, say'), say(c.fail, 'Failure if missing, say'), cx[c.badge] || []);
  };
  const linger = S('Linger on Thinking & Logic and Process.',
    say('Thinking & Logic is the cognitive engine. Process is the structured container. Most organisations have process but neglect thinking quality. The definition forces us to see this gap.'),
    ask('Where does your organisation invest more: in the quality of the thinking, or in the process that contains it?'),
    'Take two or three answers. Listen for: a strategy process with no named place for uncomfortable questions.');
  const cards = [];
  CONCEPTS.forEach(c => { cards.push(card(c)); if (c.badge === 'PROCESS') cards.push(linger); });
  n.concepts = page(head(1, 0, 'THE NINE CONCEPTS'), [
    S('Open.', say('We take the nine concepts one at a time. For each one: what it means, its strategic implication, and what fails when it is missing.')),
    ...cards,
    S('Bring the nine together.',
      ask('Which of these nine concepts is least visible in how your organisation currently talks about strategy?'),
      'Take three or four answers and note them. They show where each group will need to work hardest in Section 4.'),
    S('Bridge to 1.2.',
      say('OUTPUT is what the other concepts produce: the Strategy Architecture. In Section 4 each group works this definition as 14 elements. Next, we look at how the four dimensions, WHAT, WHY, HOW and WHEN, are brought forward into one statement.')),
  ], portal(`Participants write the 1.1 reflection: "${refl(1, 0)}"`));

  // 1.2 · the Strategy Intent Statement
  const g12 = gd(1, 1), c12 = u.part(1, 1).content;
  if (g12.some(l => /rate their organisation|1–5/.test(l))) throw new Error('the 1.2 rating is back on the facilitator page');
  pick(g12, 'Positioning the statement: The Strategy Architecture holds the depth and the supporting logic. The Strategy Intent Statement is crisp, directional and easy to express. Participants derive their own statement in Section 4; here they learn what it brings forward.');
  pick(g12, 'Taking participants through the 4 dimensions: Walk through WHAT, WHY, HOW, WHEN one at a time as a group. For each, ask one diagnostic question from the content and take 2–3 responses. HOW and WHEN typically reveal the most significant gaps');
  const howQ = pick(g12, 'HOW — key facilitation moment: Ask: ', true), whenQ = pick(g12, 'WHEN: Ask: ', true);
  if (!howQ.endsWith('This often opens the most honest conversation of the entire Awareness section.')) throw new Error('HOW guidance changed');
  const lc = t => t.charAt(0).toLowerCase() + t.slice(1);
  const qs = arr => arr.map(q => `"${noq(q)}"`).join(' · ');
  const howKey = howQ.replace(' This often opens the most honest conversation of the entire Awareness section.', '');
  if (W1H[2].diag[0] !== 'Does our operating model match our strategy?' || W1H[3].diag[0] !== 'Have we mapped the sequence of moves needed to achieve the strategy?') throw new Error('1.2 diagnostic questions changed');
  const wx = {
    WHAT: w => ['Ask one diagnostic question and take two or three responses: ' + qs(w.diag), 'Listen for: a WHAT with no boundary.', IN('capability_without_intent')],
    WHY: w => ['Ask one diagnostic question and take two or three responses: ' + qs(w.diag), IN('why_before_how')],
    HOW: w => ['Key facilitation moment. Ask: ' + howKey,
      'Stay here. This often opens the most honest conversation of the entire Awareness section.',
      'Further diagnostic questions, if the room needs them: ' + qs(w.diag.slice(1)),
      'Listen for: a HOW with no operating model, capability or mechanism named.',
      IN('destination_and_route')],
    WHEN: w => ['Ask: ' + whenQ,
      'Further diagnostic questions, if the room needs them: ' + qs(w.diag.slice(1)),
      IN('timing_failures')],
  };
  const dim = w => S(`${w.name} — ${w.sub}.`,
    say(`${w.name} brings forward ${lc(w.def)} It governs ${lc(w.governs)}`),
    wx[w.name](w));
  n.intent = page(head(1, 1), [
    S('Position the statement.',
      say(c12[0] + ' ' + c12[1].replace(' Select each one.', '')),
      say('The Strategy Architecture holds the depth and the supporting logic. The Strategy Intent Statement is crisp, directional and easy to express.'),
      'Tell participants: they derive their own statement in Section 4. Here they learn what it brings forward.'),
    S('Say why the statement must be crisp.', IN('sound_and_communicable', 'Say')),
    S('Take the four dimensions one at a time.',
      say('We walk through WHAT, WHY, HOW and WHEN one at a time, as a group.'),
      'For each dimension, ask one diagnostic question and take two or three responses. Stay longest on HOW and WHEN: they typically reveal the most significant gaps.'),
    ...W1H.map(dim),
    S('Read the room.',
      ask('Which of the four dimensions is least clearly defined in your organisation today?'),
      'Take a show of hands for each dimension and say what the pattern in the room is. Participants answer the same question in their 1.2 reflection.'),
    S('Show that the four hold together.',
      say('The four dimensions are interdependent. Answering only two or three creates a structurally incomplete strategy. A well-formed strategic intent answers all four at once: What value are we creating? Why will stakeholders choose us? How will we deliver this value? When will we act?')),
    S('Say what is at stake.',
      say('Without a clear strategic intent, every investment becomes a negotiation without a shared reference point. Every performance review becomes a contest between competing definitions of success.')),
    S('Close and bridge to 1.3.',
      say(c12.slice(-3).join(' ')),
      say('The Intent sets the ambition. Next we ask what we should see in practice when that ambition is realised.')),
  ], portal(`Participants write the 1.2 reflection: "${refl(1, 1)}"`));

  // 1.3 · Success in Practice
  const g13 = gd(1, 2), c13 = u.part(1, 2).content;
  const g13a = g13[1], g13d = pick(g13, 'Facilitator emphasis: ', true);
  pick(g13, 'Position participants inside the future created by the Strategy Intent. Ask them to imagine that the intent has been successfully realised and describe the observable organisational reality.');
  pick(g13, 'The central question: "If our Strategy Intent is successful, what should we see in practice?"');
  if (!g13a.startsWith('The Strategy Intent Statement establishes the ambition.') || !g13d.startsWith('Keep participants focused on observable reality.')) throw new Error('1.3 guidance changed');
  const s13 = g13a.split('. ').map((x, k, a) => (k < a.length - 1 ? x + '.' : x));     // three sentences
  if (s13.length !== 3) throw new Error('1.3 guidance, first paragraph: expected three sentences');
  const doms13 = []; for (let k = 2; k < 10; k += 2) doms13.push(`${c13[k]}: ${c13[k + 1]}`);
  if (doms13.length !== 4 || !c13[2].startsWith('D1 · ')) throw new Error('1.3 content changed');
  n.sip = page(head(1, 2), [
    S('Connect the two outputs.',
      say(s13[0] + ' ' + s13[1]),
      say('Once the organisation has answered WHAT, WHY, HOW and WHEN, the next step is to translate that clarity into an observable future reality.', 'Add')),
    S('Say what Success in Practice is.',
      say('Success in Practice, SiP, translates strategic intent into a clear picture of the future operating reality of the organisation. It answers a question that most strategy processes fail to address clearly.'),
      'Read the central question from the foot of the slide:',
      `"${noq(c13[0].replace(/^"|"$/g, ''))}"`),
    S('Position participants inside the future.',
      say('For this first look, use the strategic ambition of your own organisation as it stands today. Assume the strategy has worked. From here, we are observing.'),
      'Ask participants to describe the observable organisational reality. Each group writes its own Strategy Intent Statement in Section 4.'),
    S('Take the four domains.',
      say(c13[1].replace(/:$/, '.')),
      'Name each domain from the slide and say what it covers:', ...doms13.map(x => '- ' + x),
      'Take one observation from the room for each domain, D1 to D4.',
      say('Anchoring the description in four observable domains keeps us out of vague storytelling.', 'Add')),
    S('Keep the room on observable reality.',
      say('The SiP describes what is happening when the strategy is working. Initiatives, projects and activities stay out of it.'),
      'Each time a participant offers an initiative, a project or an activity ("we will launch…", "we will implement…"), ask: "And when that has worked, what do we see?"',
      'Listen for: success described in one domain only. Note which domain each participant reaches for first. The pattern returns in 3.2, the SiP Flammables.'),
    S('Say why success is defined before anything is built.', IN('built_to_a_specification', 'Say')),
    S('Say what a shared picture gives a leadership team.',
      say(s13[2]),
      say('The aim is shared construction: we should leave with a common understanding of what success looks like across the organisation.'),
      'Name the four effects for an executive team:',
      '- It removes ambiguity about what the strategy is actually aiming to produce.',
      '- It creates a shared mental model of the future state across all functions.',
      '- It provides a decision filter: every initiative, investment and priority can be tested against it.',
      '- It enables recognition of progress: leaders can see alignment and momentum during execution.'),
    S('Close and bridge.',
      say(c13[c13.length - 1]),
      say('Before we move to Section 2, look at the two reflections for this section.')),
  ]);

  n.ref1 = reflection(1, [
    S('Show the slide and read the two prompts aloud.',
      `1.1 Reflection — Strategy Architecture: "${refl(1, 0)}"`,
      `1.2 Reflection — Strategy Intent: "${refl(1, 1)}"`),
    reflFor(true),
    S('Set the standard for 1.1.',
      say('Name one concept from the nine, give evidence from your own organisation, and name one consequence you have seen: what the gap costs, slows down or leaves undecided.'),
      IN('an_honest_baseline')),
    S('Set the standard for 1.2.',
      say('Answer from your assigned executive leader perspective. Name one dimension, and say what clarifying it would change.'),
      'Tell participants: they can start from the dimension they named in the show of hands.'),
    S('Take one or two first thoughts aloud.', 'This lets participants hear the depth you are asking for.'),
    S('Bridge to Section 2.',
      say('We now have the three building blocks: the architecture, the intent and the picture of success. Section 2 asks why the Strategy Intent and SiP matter once they are defined.')),
  ], 'Participants write the two reflections in Section 1 of the participant file: 1.1 Reflection — Strategy Architecture and 1.2 Reflection — Strategy Intent.');

  return { u, up, H, N, S, steps, page, say, ask, noq, IN, pick, PORTAL, LATER, portal, later, divider, reflection, reflFor, refl, n, used, lead, gd, head, G, clean,
    data: { CONCEPTS, W1H, ARCH, DIMS, FLAMS, SUMMARY, EL, SIPD, ROLES, APP_DIMS, GROUPS } };
};
