// Unit 2 presenter notes, part 2: Section 2 (Intelligence) and Section 3 (Extrapolating).
// Structure of every page (see u02_notes.js): HEADING, then numbered steps in class order. Every card, insight and
// line of manuscript detail sits inside the step where the facilitator uses it.
module.exports = function (ctx) {
  const { u, up, H, S, page, say, ask, noq, IN, pick, portal, n, lead, gd, head, refl, reflFor, clean, data } = ctx;
  const { ARCH, DIMS, FLAMS } = data;

  // ════════════════════════════════════════════════════════════════════════ SECTION 2
  const l2 = lead(2, 0);
  const intent2 = pick(l2, 'Section intent: ', true);
  pick(l2, 'Explain that once leaders have established a shared strategic ambition and defined what success looks like in practice, those two outputs become common reference points across the organisation.');
  pick(l2, 'They serve three important functions:');
  const fnLines = ['Strategic Alignment — ', 'Decision Filter — ', 'Execution Coherence — '].map(p => pick(l2, p));
  n.s2 = ctx.divider(2, `1. 2.1 overview: the three functions the Strategy Intent and SiP serve within the Strategy2Results® architecture.
2. 2.1.1 Strategic Alignment, 2.1.2 Decision Filter and 2.1.3 Execution Coherence: one slide each. Every function is taught in three parts: Why It Matters, what the Strategy Intent does, and what SiP does.
3. The Section 2 Reflections slide: the reflection participants write on the portal after the teaching.`, [
    S('Link from Section 1.',
      say('Section 1 defined the three building blocks. This section asks what the Strategy Intent and SiP do for a leadership team once they exist.')),
    S('State the section intent.',
      say(intent2),
      say('Once leaders have established a shared strategic ambition and defined what success looks like in practice, those two outputs become common reference points across the organisation.')),
    S('Read the two section learning outcomes from the slide.'),
    S('Bridge to 2.1.', say('The Strategy Intent and SiP serve three important functions. The next slide names them.')),
  ]);

  const g21 = gd(2, 0);
  pick(g21, 'Walk participants through each function and demonstrate how Strategy Intent and SiP work together. The Intent anchors the ambition and strategic choices; SiP anchors the organisational reality those choices are intended to produce.');
  pick(g21, 'As you move through the three functions, invite participants to consider: "What happens in an organisation when this function is weak or absent?"');
  pick(g21, 'Use the Decision Filter to make the application particularly practical. Ask: "When a new initiative, investment or opportunity appears, what tells us whether it belongs in our strategy?"');
  const tests = pick(g21, 'The Strategy Intent provides the test of strategic fit.');
  n.fn = page(head(2, 0), [
    S('Introduce the three functions.',
      say('Strategy Intent and SiP serve three functions within the Strategy2Results® architecture.'),
      'Name each function from the slide:', ...fnLines.map(l => '- ' + l.replace(' — ', ': '))),
    S('Name the pairing that runs through all three.',
      say('The Intent anchors the ambition and strategic choices; SiP anchors the organisational reality those choices are intended to produce.'),
      'Listen for: participants who treat the Strategy Intent and SiP as communication tools. Say: "The two outputs are there to govern alignment, choices and execution."'),
    S('Leave one question in the room.',
      say('As we move through the three functions, consider: What happens in an organisation when this function is weak or absent?')),
    S('Bridge to the next slide.',
      say('The next three slides take one function each: why it matters, what the Strategy Intent does, and what SiP does.')),
  ]);

  const lc = t => t.charAt(0).toLowerCase() + t.slice(1);
  const SI = a => say('The Strategy Intent ' + lc(clean(a.si))), SP = a => say('SiP ' + lc(clean(a.sip)));
  const weakQ = 'What happens in an organisation when this function is weak or absent?';
  const fnSteps = {
    '2.1.1': a => [
      S('Say why it matters.', say(clean(a.why))),
      S('Give the role of the Strategy Intent.', SI(a), IN('shared_understanding')),
      S('Give the role of SiP.', SP(a), IN('shared_meaning_shared_action')),
      S('Test alignment against the opening exercise.',
        say('When this session opened, we heard several definitions of strategy in one room.'),
        ask('If each member of your leadership team described your organisation’s strategic ambition in one sentence, how many versions would you hear?')),
      S('Ask what happens when the function is weak.',
        ask(weakQ),
        'Listen for: leaders and functions interpreting the ambition differently; each executive pursuing a personal interpretation of the scope and its differentiating logic; each function describing its own version of the future operating state.'),
      S('Bridge to the Decision Filter.',
        say('Alignment gives us one reference point. The next function puts that reference point to work on choices.')),
    ],
    '2.1.2': a => [
      S('Say why it matters.', say(clean(a.why)), IN('the_one_thing')),
      S('Make it practical.',
        ask('When a new initiative, investment or opportunity appears, what tells us whether it belongs in our strategy?'),
        'Take three answers before you give the two tests.'),
      S('Give the two tests on the slide.',
        say(tests),
        'The test of strategic fit:', SI(a),
        'The test of strategic contribution:', SP(a)),
      S('Run both tests on a real case.',
        'Ask one participant to name a real initiative that is competing for resources in their organisation today. Run both tests aloud against that organisation’s current strategic ambition and its current picture of success.',
        say('Use the same two tests each time a new initiative, investment or opportunity appears.')),
      S('Deepen: the filter is how daily decisions are made.', IN('operating_logic', 'Say')),
      S('Deepen: name the governing reference points.', IN('governing_reference_points', 'Say', { then: 'Ask participants to name' })),
      S('Ask what happens when the function is weak.',
        ask(weakQ),
        'Listen for: priorities shaped by urgency, by functional interests, or by whoever has the strongest influence in the room; an initiative that passes the test of fit while nobody asks what it contributes to the defined success.'),
      S('Bridge to Execution Coherence.',
        say('The filter governs single choices. The next function asks whether the work of all the functions adds up.')),
    ],
    '2.1.3': a => [
      S('Say why it matters.', say(clean(a.why))),
      S('Give the role of the Strategy Intent.', SI(a)),
      S('Give the role of SiP.', SP(a)),
      S('Make it real.',
        ask('Where in your organisation does every function meet its own targets while the enterprise outcome falls short?'),
        'Take two or three answers.'),
      S('Deepen.', IN('the_common_centre', 'Say')),
      S('Ask what happens when the function is weak.',
        ask(weakQ),
        'Listen for: each function performing well against its own measures while the enterprise outcome is missed; functions losing sight of the organisational outcome they collectively enable; contributions that do not connect at the boundaries between functions.'),
      S('Point forward and bridge.',
        say('Section 5 puts this function to work: each of you defines what one executive role must contribute so that the agreed Success in Practice becomes real.'),
        say('Before we move to Section 3, look at the reflection for this section.')),
    ],
  };
  ARCH.forEach((a, k) => {
    n['fn' + (k + 1)] = page(H(`${a.n} — ${up(a.fn)}`), fnSteps[a.n](a),
      k === 2 ? portal(`Participants write the 2.1 reflection: "${refl(2, 0)}"`) : []);
  });

  n.ref2 = ctx.reflection(2, [
    S('Show the slide and read the prompt aloud.', `2.1 Reflection — Three Functions: "${refl(2, 0)}"`),
    reflFor(false),
    S('Set the standard.',
      say('Name one function only: Strategic Alignment, Decision Filter or Execution Coherence. Describe a real situation in which the weakness showed: a decision, a meeting, a hand-off between functions. Then give the result for the organisation.')),
    S('Read the room.', 'Take a show of hands for each function and say what the pattern in the room is.'),
    S('Bridge to Section 3.',
      say('We know what the Strategy Intent and SiP are for. Section 3 looks closely at the SiP itself: what success looks like inside each domain, and what happens when one domain dominates the picture.')),
  ], 'Participants write the reflection in Section 2 of the participant file: 2.1 Reflection — Three Functions.');

  // ════════════════════════════════════════════════════════════════════════ SECTION 3
  const l3 = lead(3, 0);
  const i3 = pick(l3, 'Section intent: ', true);
  const l3b = pick(l3, 'Each of the four SiP domains covers an important part of organisational reality.'),
    l3c = pick(l3, 'This is where observable indicators become useful.'),
    l3d = pick(l3, 'There is also a second discipline: balance across the four domains.'),
    l3e = pick(l3, 'This section therefore develops two disciplines:'),
    l3f = pick(l3, 'We begin by examining the observable indicators within each domain.');
  n.s3 = ctx.divider(3, `1. 3.1 overview: the four SiP domains and their observable indicators.
2. 3.1 domain by domain, D1 to D4: one slide each. Every indicator is taught in two positions: When Working and Signal of Absence.
3. 3.2 overview: the SiP Flammables as the balance test.
4. 3.2 pattern by pattern: one slide each, with the indicators that reveal the pattern and the strategic risk if it is not balanced.
5. The Section 3 Reflections slide: the 3.1 reflection participants write on the portal after the teaching.`, [
    S('State the section intent.', say(i3.replace(/"/g, ''))),
    S('Say why broad statements fall short.', say(l3b)),
    S('Introduce the observable indicators.', say(l3c)),
    S('Introduce the second discipline: balance.', say(l3d)),
    S('Name the two disciplines.',
      say(l3e),
      'Tell participants: both disciplines return in 4.3, where each group tests its own Success in Practice.'),
    S('Read the two section learning outcomes from the slide.'),
    S('Say how the section runs.', say(l3f)),
  ]);

  const g31 = gd(3, 0);
  const g31a = pick(g31, 'Each SiP domain is examined through a set of observable indicators.'),
    g31w = pick(g31, 'When Working describes'), g31s = pick(g31, 'Signal of Absence describes'),
    g31u = pick(g31, 'Use both positions to deepen the discussion.'), g31p = pick(g31, 'The indicators sit alongside the organisation');
  pick(g31, 'For every indicator, examine two positions:');
  const short = ['D1 · Customer Experience & Value', 'D2 · Operational Capability', 'D3 · People & Culture', 'D4 · Enterprise Value'];
  n.ind = page(head(3, 0), [
    S('Say what an observable indicator is for.', say(g31a)),
    S('Explain the two positions.',
      say('For every indicator, we examine two positions.'),
      say(g31w), say(g31s)),
    S('Say how the two positions are used.', say(g31u)),
    S('Place the indicators correctly.',
      say(g31p),
      'Tell participants: each group writes its own SiP statements in Section 4. The indicators deepen that work.'),
    S('Name the four domains and their indicators.',
      'The slide shows the indicators in short form. Give the full names:',
      ...DIMS.map((d, k) => `- ${short[k]}: ${d.inds.map(i => i.name).join(' · ')}`),
      say('No domain is a single metric.')),
    S('Bridge to the next slide.',
      say('The next four slides take one domain each. For every indicator we look at When Working, then at the Signal of Absence.')),
  ]);

  // Per indicator: manuscript detail for each position (w = When Working, m = Signal of Absence), a question for the
  // room, where to stay longest, and the insight it carries.
  const X = [
    { 'C — Connection Value': { w: 'Customers trust that the care extends beyond the transaction.' },
      'A — Access Value': { ins: 'structured_into_the_rhythm' },
      'E — Effort Value': { w: 'No complexity is passed to the customer.',
        stay: 'Stay longest here. Effort Value asks who carries the complexity: the customer or the organisation.',
        q: 'Where does your customer carry effort or complexity that the organisation should absorb?' } },
    { 'Priority Clarity': { q: 'Could each leader in your executive team state the top priorities without checking a document? Would the answers match?',
        stay: 'Stay longest on Priority Clarity and Decision Flow. A leader can test both in their own team by putting one question to each member separately.' },
      'Decision Flow': { w: 'The organisation does not bottleneck at the top.', m: 'It is the leaders below CXO level who feel they cannot act without approval.',
        q: 'Where do decisions queue in your organisation, and who is waiting for them?' },
      'Cross-Functional Coordination': { m: 'Execution friction that is silently absorbed goes unmanaged.', q: 'Which hand-off between two functions leaks the most value today?' },
      'Delivery Rhythm': { w: 'The cadence is weekly signal scanning, monthly performance reads, and quarterly strategic review.',
        m: 'Review has not become a disciplined organisational habit, and delivery is variable and unpredictable.', ins: 'daily_tending' } },
    { 'Cross-Boundary Collaboration': { w: 'Information is shared proactively.', m: 'Information is hoarded or filtered.',
        q: 'Which problem in your organisation belongs to no single function today? Who is carrying it?' },
      'Ownership Culture': { w: 'People step in without being required to. Accountability is cultural before it is structural.', m: 'When something fails at a boundary, no one steps forward.' },
      'Strategic Alignment': { w: 'Leaders can trace what they are doing to both the strategic intent and the SiP.', m: 'Teams act on what the function has always done.',
        q: 'When your teams are asked why they are doing something, can they trace it to the strategic intent?' },
      'Dialogue Quality': { w: 'Leaders can say they do not know something without losing credibility.', m: 'Fast, pattern-based thinking dominates and no deliberate, analytical thinking checks it.',
        stay: 'Stay longest here. Honest challenge is the condition for an honest discussion of the other three indicators.',
        q: 'Where are the most important concerns raised: in the meeting, or in the corridor afterwards?', ins: 'values_at_the_edges' } },
    { 'Growth Trajectory': { w: 'Growth is deliberate.', m: 'Growth may be happening in arenas that were not part of the intended WHAT.',
        q: 'Can you trace your growth to specific strategic choices, or does the market explain it?' },
      'Profitability Quality': { w: 'The premium is earned because the organisation has chosen arenas where its differentiation commands it.' },
      'Market Position': { w: 'The stakeholders in question are customers, partners, analysts and employees.', m: 'The strategy exists on paper only.',
        q: 'Do stakeholders describe your organisation in the words you would use yourselves?' },
      'Value Durability': { w: 'The organisation is building moats.', m: 'Short-term results also cost the relationships that make future success possible.',
        stay: 'Stay longest here. Value Durability is the SUSTAINS layer of the Value Triad, the layer most organisations under-invest in.',
        q: 'Which condition of your future success are you reinvesting in least?', ins: 'surviving_success' } },
  ];
  // The opening line of each domain, made speakable. The text of the page is checked first.
  const introSrc = [
    'Customers encounter the organisation through People · Processes · Products · Platforms and experience four forms of value (the CARE Model):',
    'How the organisation operates internally when its strategy is translating into results — observable through four execution indicators:',
    'Observable behavioural patterns when the organisation is at its best — when culture is actively reinforcing the strategic direction:',
    'The commercial and strategic outcomes confirming the strategy is producing durable enterprise value:'];
  const introSay = [
    ['This domain is Customer Experience & Value. Customers encounter the organisation through People, Processes, Products and Platforms, and experience four forms of value: the CARE Model.',
      'Each of the four is the source of one form of value. People: Connection Value. Platforms: Access Value. Products: Results Value. Processes: Effort Value.'],
    ['This domain is Operational Capability & Execution Rhythm. It shows how the organisation operates internally when its strategy is translating into results. It is observable through four execution indicators.'],
    ['This domain is People & Culture Dynamics. It shows the observable behavioural patterns when the organisation is at its best, when culture is actively reinforcing the strategic direction.'],
    ['This domain is Enterprise Value Creation. It shows the commercial and strategic outcomes confirming the strategy is producing durable enterprise value.']];
  const intro = k => d => { if (d.intro !== introSrc[k]) throw new Error('3.1 domain intro changed: D' + (k + 1)); return introSay[k].map((t, j) => say(t, j ? 'Add' : 'Say')); };
  const close = [
    ['Which of the four forms of value would your customers say they receive from you most reliably? Which would they name last?', 'Which of these signals of absence do you already hear in your customers’ complaints?'],
    ['Which Signal of Absence in this domain do you recognise in your own organisation?'],
    ['Which Signal of Absence in this domain do you recognise in your own organisation?'],
    ['Which Signal of Absence in this domain do you recognise in your own organisation?'],
  ];
  const link = [
    ['Customer Experience & Value', 'If the intent succeeds, what should customers and other value recipients see and experience?'],
    ['Operational Capability & Execution Rhythm', 'If the intent succeeds, what should be visible in how the organisation operates and executes?'],
    ['People & Culture Dynamics', 'If the intent succeeds, what should be visible in how people understand, decide and behave?'],
    ['Enterprise Value Creation', 'If the intent succeeds, how should the organisation benefit across its success metrics?'],
  ];
  const next3 = ['Next: D2, how the organisation operates and executes.', 'Next: D3, how people understand, decide and behave.', 'Next: D4, how the organisation benefits.',
    'We have looked at depth within each domain. Next we look at balance across all four.'];
  DIMS.forEach((d, k) => {
    const sipd = data.SIPD[k];
    if (sipd.t !== link[k][0] || sipd.lead !== link[k][1]) throw new Error('4.3 lead question changed for D' + (k + 1));
    Object.keys(X[k]).forEach(name => { if (!d.inds.some(i => i.name === name)) throw new Error('indicator renamed: ' + name); });
    n['d' + (k + 1)] = page(H(`3.1 — SiP OBSERVABLE INDICATORS · ${up(short[k])}`), [
      S('Introduce the domain.', intro(k)(d), 'The slide shows the When Working position of each indicator. Give the Signal of Absence from these notes.'),
      ...d.inds.map(ind => {
        const x = X[k][ind.name] || {};
        return S(`${ind.name}.`,
          say(ind.good, 'When Working, say'), x.w ? say(x.w, 'Add') : '',
          say(ind.miss, 'Signal of Absence, say'), x.m ? say(x.m, 'Add') : '',
          x.stay || '', x.q ? ask(x.q) : '', x.ins ? IN(x.ins) : '');
      }),
      S('Ask the room what it recognises.',
        ...close[k].map(ask),
        'Take two or three answers. Keep the discussion on what can be observed: what a customer, an employee or a board member would see or hear.'),
      S('Link the domain to Section 4.',
        say(`In Section 4 your group writes one ${link[k][0]} statement. The lead question is: ${link[k][1]} These indicators deepen that discussion. The statement itself stays focused on your own Strategy Intent.`)),
      S(k < 3 ? 'Bridge to the next domain.' : 'Bridge to 3.2.', say(next3[k])),
    ], k === 3 ? portal(`Participants write the 3.1 reflection: "${refl(3, 0)}"`) : []);
  });

  const g32 = gd(3, 1);
  const f1 = pick(g32, 'The four SiP domains are designed to describe one organisational reality.'),
    f2 = pick(g32, 'In practice, leadership teams naturally bring different perspectives into the conversation.'),
    f3 = pick(g32, 'Each perspective contributes something important.'),
    f4 = pick(g32, 'The strategic risk emerges when one perspective becomes so dominant'),
    f5 = pick(g32, 'This is what the SiP Flammables are designed to expose.'),
    f6 = pick(g32, 'They provide a balance test for the SiP.');
  n.flam = page(head(3, 1), [
    S('Start from one reality.', say(f1)),
    S('Start from legitimacy.', say(f2 + ' ' + f3), IN('a_common_baseline')),
    S('Name the risk.', say(f4), IN('the_single_measure')),
    S('Say what the Flammables are for.', say(f5 + ' ' + f6), IN('partial_formation')),
    S('Name the four patterns on the slide.',
      ...FLAMS.map(f => `- ${f.dim}: ${f.what.split(': ')[0]}.`)),
    S('Ask the room where it stands.',
      ask('Which of these four patterns is your own function most likely to produce?'),
      'Take two or three answers.'),
    S('Set the tone and bridge.',
      say('Every pattern grows from a legitimate perspective. We are here to see dominance early, while the SiP is still being written. The next four slides take one pattern each.')),
  ]);

  const fins = [[['the_task_and_its_conditions', 'Deepen, say']], [['signal_to_watch_for', 'Name the signal to watch for, say'], ['process_as_an_end_in_itself', 'Deepen, say']],
    [['budget_and_recognition', 'Deepen, say']], [['metrics_that_flatter', 'Deepen, say'], ['enduring_value', 'Close the point, say']]];
  const fask = [
    'Where has your organisation promised customers an experience before it had the capability to deliver it?',
    'Which of your efficiency measures has no customer in it?',
    'Which of your culture commitments could you defend to the board with a result?',
    'Which of your targets was met last year in a way that weakened next year?'];
  const fbal = [
    ['Operational capability: "Which capability, decision right and delivery rhythm produce this customer experience?"',
      'People and culture: "What must our people understand, decide and do for customers to experience this?"',
      'Enterprise value: "What does this experience cost to serve, and how does the organisation benefit?"'],
    ['Customer experience: "Who benefits from this efficiency, and what do they experience?"',
      'People and culture: "Which behaviour and ownership keep this system adapting when the market moves?"',
      'Enterprise value: "Which enterprise outcome is this efficiency meant to serve?"'],
    ['Customer experience: "Which customer result does this culture produce?"',
      'Operational capability: "Which mechanism turns this behaviour into operational capability?"',
      'Enterprise value: "Which commercial result would show, within the time horizon, that this is working?"'],
    ['Customer experience: "What must customers experience for this number to be earned?"',
      'Operational capability: "Which capability produces this result?"',
      'People and culture: "Which behaviour produces this result, and is it being built or spent?"']];
  const fnext = ['Next: the same test, with operations as the dominant perspective.', 'Next: people and culture as the dominant perspective.',
    'Next: enterprise value as the dominant perspective.', 'Before we move to Section 4, look at the reflection for this section.'];
  FLAMS.forEach((f, k) => {
    n['f' + (k + 1)] = page(H(`3.2 — SiP FLAMMABLES · ${up(f.dim)}`), [
      S('Say what the pattern creates.', say(f.what)),
      S('Take the three indicators on the slide.',
        ...f.signs.map(s => '- ' + s),
        say('Your group can apply these three tests to its own four SiP statements.')),
      S('Give the strategic risk, slowly.',
        say(f.risk),
        ask('Where would this risk show first in your organisation?')),
      S('Make it real.', ask(fask[k]), 'Take two or three answers.', ...fins[k].map(([id, cue]) => IN(id, cue))),
      S('Name the legitimate perspective behind the pattern.',
        ask('Which perspective in a leadership team tends to produce this pattern, and what does that perspective rightly protect?')),
      S('Give three questions that bring the other domains back.',
        say('Each of these questions brings another domain back into the picture.'),
        ...fbal[k].map(x => '- ' + x)),
      S(k < 3 ? 'Bridge to the next pattern.' : 'Bridge to the reflection.', say(fnext[k])),
    ]);
  });

  n.ref3 = ctx.reflection(3, [
    S('Show the slide and read the prompt aloud.', `3.1 Reflection — SiP Indicators: "${refl(3, 0)}"`),
    reflFor(false, ', from your assigned executive leader role'),
    S('Set the standard.',
      say('Name one SiP domain. Point to the indicators that show the gap: which Signal of Absence did you recognise? Then give one primary cause.'),
      'Listen for: a condition given as a cause, such as "we are under-resourced". Ask: "Which decision, structure or habit produces the gap?"'),
    S('Say why naming the gap matters.', IN('naming_the_gap', 'Say')),
    S('Read the room.',
      'Take one first answer for each domain if the room offers them. Note which domain is named most often. Tell the groups: test that domain hardest when you write your SiP in Section 4.'),
    S('Bridge to Section 4.',
      say('We now have two tests for any Success in Practice: depth within each domain and balance across all four. In Section 4 each group builds its own outputs and applies both tests to its Success in Practice.')),
  ], 'Participants write the reflection in Section 3 of the participant file: 3.1 Reflection — SiP Indicators.');
};
