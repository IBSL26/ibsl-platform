const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType, HeadingLevel, LevelFormat, Footer, PageNumber } = require('docx');
const GREEN = '1A5C2C', GOLD = 'C6A24C', CREAM = 'F6F1E3', GREY = '555555';
const W = 9638; // A4 with 2 cm margins
const run = (t, o = {}) => new TextRun(Object.assign({ text: t, font: 'Calibri', size: 21 }, o));
function rich(text, base = {}) { // **bold** segments
  return text.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(s => s.startsWith('**') ? run(s.slice(2, -2), Object.assign({}, base, { bold: true })) : run(s, base));
}
const P = (t, o = {}) => new Paragraph(Object.assign({ spacing: { after: 110, line: 276 }, children: rich(t, o.run || {}) }, o.p || {}));
const H1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 120 }, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 4 } }, children: [run(t, { bold: true, size: 28, color: GREEN })] });
const H2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 80 }, children: [run(t, { bold: true, size: 23, color: GREEN })] });
const B = t => new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 60, line: 264 }, children: rich(t) });
const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(t, w, o = {}) {
  const paras = (Array.isArray(t) ? t : [t]).map(x => new Paragraph({ spacing: { after: 40, line: 252 }, children: rich(x, { size: 19, bold: !!o.head, color: o.head ? 'FFFFFF' : (o.color || '000000') }) }));
  return new TableCell({ width: { size: w, type: WidthType.DXA }, borders, margins: { top: 60, bottom: 60, left: 100, right: 100 },
    shading: o.head ? { type: ShadingType.CLEAR, fill: GREEN, color: 'auto' } : (o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: 'auto' } : undefined), children: paras });
}
function table(widths, head, rows, opt = {}) {
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: head.map((h, i) => cell(h, widths[i], { head: true })) })].concat(
      rows.map(r => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i], { fill: i === 0 && opt.codeCol ? CREAM : undefined })) }))) });
}
const gap = () => new Paragraph({ spacing: { after: 60 }, children: [] });

const shape = [
  ['Facilitator Guide', 'Unit Intent, Key Facilitation Questions, Tone & Watch Points: rewritten from your document.', 'The old wording on the Headline, the 3W1H framework and the Maturity Assessment.'],
  ['Section 1 · Awareness', ['1.1 Define the Strategy Architecture (nine concept cards kept)', '1.2 Defining the Strategy Intent Statement (WHAT, WHY, HOW, WHEN tabs)', '1.3 Success in Practice (SiP): From Intent to Future Reality (four domains)'], ['1.2: the Critical Insight box and the closing line.', '1.3: the WHAT→ WHY→ HOW→ WHEN→ grid, the Headline and the Storyline.']],
  ['Section 2 · Intelligence', ['2.1 Role of Strategy Intent & SiP in the S2R® Architecture', '2.1.1 Strategic Alignment · 2.1.2 Decision Filter · 2.1.3 Execution Coherence (collapsible, each with Why It Matters, Strategy Intent, SiP)'], ['Why Intent and SiP Must Be Co-Created, with its reflection.', 'The Strategy Engine.']],
  ['Section 3 · Extrapolating', ['Title: Examining Success in Practice', '3.1 SiP Observable Indicators (content kept)', '3.2 SiP Flammables: When the Picture of Success Becomes Distorted (teaching content only: what it creates, indicators, strategic risk)'], ['The Facilitator Move note in 3.2.', 'The participant question box under each Flammable.']],
  ['Section 4 · Integration', ['Title: Build the Architecture · Derive the Intent · Define Success in Practice', '4.1 Step 1: Build the Strategy Architecture (14 elements, one at a time, then the output)', '4.2 Step 2: Derive the Strategy Intent Statement', '4.3 Step 3: Build Success in Practice (four statements written by the group, then the four read as one SiP; the three outputs print as one report)'], ['Executive Leader Perspectives (ten role cards).', 'Strategy Maturity Assessment (26 areas, score, report) with its reflection.', 'The role-by-role SiP exercise.']],
  ['Section 5 · Application', ['Title: From Success in Practice to Leadership Contribution', '5.1 Role Contribution to SiP (role selector, four domains)', '5.2 SiP Statement Collective Application', 'Unit Summary (kept, reworded)'], ['Corrective Actions.', 'SiP Headline & Storyline.', 'Integration Summary (convergence, tension, missing dimensions, dominant bias).', 'Portfolio Artefact.']],
];
const A = [
  ['A1', 'Unit intent: "…what strategy actually means. Not in the abstract — in the precise, strategic sense translated to operational reality…"', '"…leaders must agree on what strategy actually means, in the precise, strategic sense, translated to operational reality, that makes every subsequent decision coherent."'],
  ['A2', 'Section 1 outcome 1: "…to redefine the definition of strategy to create a robust understanding of strategy architecture."', '"Redefine strategy to create a robust understanding of strategy architecture."'],
  ['A3', '1.3: "…what is happening when the strategy is working—not a list of initiatives, projects or activities."', '"The SiP describes what is happening when the strategy is working. Initiatives, projects and activities stay out of it."'],
  ['A4', 'Section 3: "However, broad statements about … are not enough."', '"Broad statements about … fall short."'],
  ['A5', '3.1: "The indicators are not intended to replace the organisation\'s SiP."', '"The indicators sit alongside the organisation\'s SiP."'],
  ['A6', 'Section 4: "…surface differences rather than resolve them too quickly." and "…one enterprise position, rather than the aggregation of individual answers."', '"Encourage groups to surface differences before resolving them." and "The objective is collective construction of one enterprise position."'],
  ['A7', '4.1: "…actual strategic choices, rather than broad organisational aspirations."', '"…capture actual strategic choices and to leave broad organisational aspirations out."'],
  ['A8', '4.2: "…needs to crystallise the ambition, not reproduce the architecture."', '"The Strategy Intent Statement crystallises the ambition. The Architecture keeps the detail."'],
  ['A9', '4.3: "…emerge from the group\'s definition of success rather than from generic descriptions…"', '"The SiP should emerge from the group\'s own definition of success. Generic descriptions of a successful organisation have no place in it."'],
  ['A10', 'Section 5: "The work in this section is not to redefine success. The work is to apply it."', '"Success is already defined. The work in this section is to apply it."'],
  ['A11', '5.1: "Ask instead:"', '"Ask in response:"'],
  ['A12', 'Two names in your document.', '"Strategy Intent Statement" everywhere, as you chose. "strategic intent" in small letters stays where you wrote it as the concept (Key learning outcome 1, the four domain descriptions in 1.3).'],
  ['A13', 'Section 4 intent: "…construct the organisation\'s Strategy Intent Design."', 'Kept as written. It is the only place the term appears.'],
];
const Bc = [
  ['B1', 'Numbering in Section 2. Your document reads 2.21, 2.2.2, 2.2.3. The three functions sit under 2.1, so they are 2.1.1, 2.1.2 and 2.1.3.'],
  ['B2', 'Section 2 learning outcome 1. The old outcome was about co-creation, which left the section. New: **"Explain how a shared strategic ambition and a shared picture of success keep leaders and functions aligned."** Outcome 2 is unchanged.'],
  ['B3', 'Section 2 title, on your instruction: **"The Importance and Relevance of SiP"**. The line under it now reads: "Why do the Strategy Intent and SiP matter once they are defined? How do they shape alignment, choices and execution?"'],
  ['B4', 'The 14 elements now come from your tool, in your order: ITERATIVE, THINKING & LOGIC, PROCESS, WHAT, WHY, HOW, WHEN, CREATES VALUE, DELIVERS VALUE, SUSTAINS VALUE, STAKEHOLDERS, NAVIGATING, THE FORCES, OPERATING ENVIRONMENT. OUTPUT is what the 14 produce. My earlier reading and my own prompts are withdrawn.'],
  ['B5', 'Each element carries your tag, your guide and your four questions. Each SiP domain carries your lead question and your three questions.'],
  ['B6', '1.2 keeps the four tabs. Your definition leads each tab ("What It Brings Forward"). "What It Governs" and "Diagnostic Questions" stay beside it.'],
  ['B7', '1.2 facilitator guidance. Your document gave none, so the existing guidance stays, with a new first paragraph on positioning the statement and without the Critical Insight reference.'],
  ['B8', 'Facilitator Guide tab. Unit Intent carries your sentence plus one line naming the three outputs. The four key questions and the four watch points are taken from your own questions and emphasis notes.'],
  ['B9', 'Reflections. 1.1: "Which part of your organisation\'s strategy architecture is least well defined today? What is the consequence?" · 1.2: unchanged · 2.1 (new): "Which of the three functions is weakest in your organisation today? What happens as a result?" · 3.1: unchanged, "dimension" now "SiP domain" · 5.2: unchanged. Section 4 has no reflection since the Integration Synthesis part was removed.'],
  ['B10', 'Confirmation in Step 1 works as in your tool: "Generate what this is saying", then "Is this what you mean?", then "Yes, confirm" or "No, refine". The Strategy Architecture output, the Strategy Intent Statement, each SiP statement and the SiP as a whole each have a confirm button. Every confirmation is saved.'],
  ['B11', 'Carried forward for the participant. 4.2 shows the group\'s own WHAT, WHY, HOW, WHEN answers. 4.3 shows the Strategy Intent Statement. 5.1 shows the four SiP statements from 4.3 above the role table.'],
  ['B12', '5.2 participant boxes. Your four listening points became four boxes: Alignment, Gaps, Tensions, Execution Ownership.'],
  ['B13', '5.2 guidance. Your document has two "Purpose" paragraphs. I used the second, complete one and left the first out.'],
  ['B14', '5.1 guidance. Your text says the facilitator can record in a full table view. The facilitator file has no entry fields (your rule), so the line reads: "Recording: Participants enter their own responses from their screens."'],
  ['B15', 'Times. All times are removed from the facilitator file, in every section and part, as you instructed. The participant file carried none.'],
  ['B16', 'Portfolio Artefact removed from the participant file, on your instruction.'],
  ['B17', 'Unit Summary. The five blocks are rewritten from your document, one per section. The facilitator\'s outputs check lists the Strategy Architecture output, the confirmed Strategy Intent Statement, the four confirmed SiP statements and the role contribution row.'],
  ['B20', '3.2 Flammables wording is mine: a fuller "What It Creates", three "Indicators" and a fuller "Strategic Risk if Not Balanced" for each of the four patterns. Please read it in the preview.'],
  ['B18', '"SiP dimensions" now reads "SiP domains" in the wording around the content. "Dimensions" is kept for WHAT, WHY, HOW, WHEN. The indicator and Flammable content is untouched, as you instructed.'],
  ['B19', 'Unit description under the title. Facilitator: "This unit helps leaders to determine the organisation\'s strategy architecture, articulate its strategic intent and define the Success in Practice (SiP) of the chosen Strategy Intent." Participant: the same sentence addressed to "you".'],
];
const T = [
  ['T1', 'The 14 elements in your order, each with its tag, guide and four questions. The participant sees one element at a time, with 14 numbered chips and a progress bar.'],
  ['T2', '"Generate what this is saying" shows "Based on your inputs, your WHAT position is currently saying…" and asks "Is this what you mean?". Buttons: Yes, confirm · No, refine · Regenerate. Changing an answer clears that element\'s confirmation, as in your tool.'],
  ['T3', 'Strategy Architecture output under your five headings (Strategic Position, Strategic Model, Value Architecture, Strategic Navigation, Strategy Discipline). It unlocks at 14 of 14. The group refines it and confirms it.'],
  ['T4', 'Strategy Intent Statement. Open from the start, with no lock. Four cards show the group\'s answers for WHAT, WHY, HOW and WHEN as they are entered in 4.1. The group deduces the statement, types it in and confirms it.'],
  ['T5', 'Success in Practice. Open from the start, with no lock: it is typed by hand in the same way as 4.2, so I applied your 4.2 instruction here as well. Say the word and I put the 4.3 lock back. Each domain has your lead question and three questions. The group writes one statement per domain and confirms it. The four confirmed statements then appear numbered 1 to 4 and the group confirms the SiP.'],
  ['T6', 'Four printed outputs in your v15 layout, in IBSL green and gold: Architecture, Intent, SiP and the full Strategy Intent Design report.'],
  ['T7', 'Organisation and Strategy period boxes, printed in the report header.'],
  ['T8', 'Facilitator file: 4.1 lists the 14 elements, each collapsible, with the guide and four questions. 4.3 lists the four domains with the lead question and three questions. The activity notes describe what the group does on its page.'],
  ['T9', 'Group work. 4.1 of the participant file says: the group agrees each entry, one member acts as scribe, and every member then types the agreed entries into their own page, in the session or after it. The facilitator activity notes for 4.1, 4.2 and 4.3 say the same. Nothing is asked of participants before a session.'],
];
const D = [
  ['D1', 'Define mode only. The Stress-Test mode (ratings 1 to 5 with evidence) is left out: your Unit 2 document is about building the strategy.'],
  ['D2', 'The page says "Element 4 of 14" where the tool says "Lens 4 of 14" (your rule on the word). The definition keeps the portal\'s British spelling.'],
  ['D3', 'One guide reworded for rule 13. NAVIGATING: "using forces rather than merely fighting them" now reads "putting the forces to use".'],
  ['D4', 'Answers save to the portal under each participant\'s account. The tool saves in the browser.'],
  ['D5', 'The report header reads "Strategy2Results® · Module 2 · Unit 2" and the footer names IBSL. The name "S2R Strategy Architect™" and the Impactis branding stay with the Impactis tool.'],
];
const F = [
  ['F2', 'A position changed through "No, refine" did not reach the Strategy Architecture output. In the portal it does.'],
  ['F3', 'The printed Architecture (v15) ignores edits made in the output box. The portal prints the text the group confirmed.'],
  ['F4', 'The report shows "Organisation" in place of the organisation name, and no period. The portal prints both.'],
  ['F5', '"Rebuild from 14 Elements" does nothing once text exists. In the portal it rebuilds, after asking.'],
];
const K = [
  ['K1', 'Unit 2 boxes of the Blueprint: **2A Strategy Architecture · 2B Strategy Intent Statement · 2C SiP · Customer Experience & Value · 2D SiP · Operational Capability & Execution Rhythm · 2E SiP · People & Culture Dynamics · 2F SiP · Enterprise Value Creation**. "Maturity gaps and corrective actions", "SiP Headline" and "SiP Storyline" are removed.'],
  ['K2', 'The line under each box title is my wording, for your read. 2A: "Set out the strategy architecture of [Case] under its five headings: Strategic Position, Strategic Model, Value Architecture, Strategic Navigation and Strategy Discipline." 2B: "State the strategic ambition of [Case] in one crisp statement that carries WHAT, WHY, HOW and WHEN." 2C: "State what customers and other value recipients see and experience when the Strategy Intent of [Case] succeeds." 2D: "State what is visible in how [Case] operates and executes when its Strategy Intent succeeds." 2E: "State what is visible in how the people of [Case] understand, decide and behave when its Strategy Intent succeeds." 2F: "State how [Case] benefits across its success metrics when its Strategy Intent succeeds."'],
  ['K3', 'How the three outputs arrive. The Unit 2 section of the Blueprint opens when every team member has completed Unit 2 (unchanged). The first member to open it who has all three outputs confirmed on their Unit 2 page sees the six boxes filled from that page and saved as the team draft. The team reads the text, one member selects "Send for team confirmation", and every member confirms (unchanged).'],
  ['K4', 'The boxes stay open to edit while the section is a draft, so the team can correct a typing difference between members. A button, "Bring in from my Unit 2 page", brings the text in again from the page of the member who selects it. An output that is not confirmed on the Unit 2 page is not brought in, and the page names it.'],
  ['K5', 'One database step is needed, once: the database counts the boxes of a section before it can be sent, and Unit 2 goes from 8 boxes to 6. The step is in Claude outputs\\capstone_unit2_boxes.sql. Run it on the day the new Capstone page goes live.'],
  ['K6', 'Unit 2 pages: 4.3 of the participant file and the 4.3 facilitator activity note each carry one short paragraph saying that the three confirmed outputs feed the team\'s Capstone Blueprint.'],
  ['K7', 'The other ten sections of the Blueprint are untouched. Each one is aligned as its unit is rebuilt. The page is built so that a further unit is added in a few lines.'],
];
const C = [
  ['C2', '**Cohorts inside Unit 2.** If any participant has already saved answers in the old Unit 2, those answers stay in the database and stay visible in the facilitator report. The removed boxes no longer show on the participant\'s own page. Tell me if a cohort is in Unit 2 now.'],
  ['C3', '**The deck.** The 36-slide Unit 2 deck still follows the old unit. After your yes on the two files, I rebuild the deck from them: slides, presenter notes, reflection slides and the journal insights.'],
  ['C4', '**OPERATING ENVIRONMENT in 1.1.** 1.1 has nine concept cards. Element 14 of your tool, OPERATING ENVIRONMENT, has no card there. Say the word and I add a tenth card, using your guide text for "What it means". I would propose the "Strategic implication" and "Failure if missing" lines for your approval.'],
  ['C5', '**Your Impactis tool.** The points in part 4c apply to the v15 file. Two more sit in its drafting: the Intent draft reads "We will do this by combines…" and stops mid-sentence twice, and the four-statement SiP ignores a statement the user has edited. I can correct them in that file if you want. The second PDF you sent is the same file as the first, so I have not seen a v15 report.'],
];

const doc = new Document({
  styles: { default: { document: { run: { font: 'Calibri', size: 21 } } } },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } } } }] }] },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [run('Unit 2 rebuild · Review notes v5 · 5 October 2026 · page ', { size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], font: 'Calibri', size: 16, color: GREY })] })] }) },
    children: [
      new Paragraph({ spacing: { after: 40 }, children: [run('Unit 2 · Strategy Visioning & Success in Practice (SiP)', { size: 20, color: GOLD, bold: true })] }),
      new Paragraph({ spacing: { after: 160 }, children: [run('Rebuild: review notes', { size: 40, bold: true, color: GREEN })] }),
      P('Both Unit 2 files are rebuilt from your document "Unit 2 Rebuild _2026_10_05" and saved on your computer. Nothing is committed or uploaded, so the live portal still shows the old Unit 2.'),
      P('**Version 5 of these notes.** New in this version: the Section 2 title (B3) and the Capstone Blueprint (part 5, codes K1 to K7). Version 4 brought: 4.2 and 4.3 with no lock (T4, T5); all times removed from the facilitator file (B15); the group-work line (T9). It also includes the six changes from your review of the participant page: 3.2 is teaching content only, with fuller indicators and risks; the Intent and the SiP statements are written by the group; the Integration Synthesis part and the Portfolio Artefact are removed.'),
      P('**How to answer:** "yes to all", or the codes you want changed (for example "A3, B9"). Section C needs a separate answer.'),
      P('**To try the pages:** open the HTML preview files sent with these notes ("PREVIEW - Unit 2 Participant.html", "PREVIEW - Unit 2 Facilitator.html" and "PREVIEW - Capstone.html"). Double-click each one. The participant preview saves in your browser only.'),
      H1('1. The new shape of Unit 2'),
      table([1900, 4538, 3200], ['Section', 'Parts now', 'Left the unit, as your document instructs'], shape),
      gap(),
      P('Both files carry the same sections, part numbers, titles and sub-lines. The facilitator file holds your guidance in full and has no entry fields. The participant file speaks to "you" and holds the entry boxes.'),
      H1('2. A: your wording, adjusted'),
      P('Standards rule 13 (no contrast constructions) and the chosen name required these changes to your text. Everything else in your document is in the facilitator file as you wrote it.'),
      table([700, 4369, 4569], ['Code', 'Your document', 'In the files'], A, { codeCol: true }),
      H1('3. B: choices made where your document was silent'),
      table([700, 8938], ['Code', 'Choice'], Bc, { codeCol: true }),
      H1('4. From your S2R Strategy Architect tool (v15)'),
      P('Tested with your Impactis inputs: all 14 elements, the Architecture, the Intent and the four SiP statements. The Architecture and the SiP statements match your PDF word for word.'),
      H2('4a. Carried into Section 4'),
      table([700, 8938], ['Code', 'What the participant page now does'], T, { codeCol: true }),
      H2('4b. Different from the tool, on purpose'),
      table([700, 8938], ['Code', 'Difference'], D, { codeCol: true }),
      H2('4c. Corrected in the portal version'),
      table([700, 8938], ['Code', 'What the tool does, and what the portal does'], F, { codeCol: true }),
      H1('5. K: the Capstone Blueprint, aligned with the new Unit 2'),
      P('To try it: open "PREVIEW - Capstone.html". It shows one sample team with sample text; nothing is saved.'),
      table([700, 8938], ['Code', 'What changed'], K, { codeCol: true }),
      H1('6. C: needs your word (nothing touched)'),
      table([700, 8938], ['Code', 'Item'], C, { codeCol: true }),
      H1('7. Checks done'),
      B('Standards check: no breach in either Unit 2 file. The only lines reported are the 82 known lines of the Unit 01 deck.'),
      B('Both pages run in a browser. In the participant page the whole Section 4 flow was run with your Impactis inputs: answers, confirmations, outputs and the role table save and come back after a reload.'),
      B('The facilitator report and the printable collection show the new answers under their own headings. The two unit files need no database change. The Capstone needs one small step (K5).'),
      B('The Capstone page was run in a browser against a stand-in database: outputs brought in and saved, sent for confirmation, a missing confirmation named, an existing draft replaced only after a yes, a locked section left locked.'),
      B('Backups of the files as they stood this morning are in Claude outputs\\Unit 2 file backups.'),
    ]
  }]
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('Unit 2 rebuild - Review notes.docx', b); console.log('ok', b.length); });
