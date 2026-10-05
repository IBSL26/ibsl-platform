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

const rows = JSON.parse(fs.readFileSync('deck_rows.json', 'utf8'));
const DIV = { 4: 'Section 1 · Awareness — What', 11: 'Section 2 · Intelligence — Why', 17: 'Section 3 · Extrapolating — Where', 29: 'Section 4 · Integration — Collective', 43: 'Section 5 · Application — In Practice' };
const map = rows.map(r => [String(r.n), DIV[r.n] || (r.n === 1 ? 'Cover' : r.title), r.ins.length ? r.ins.map(x => x.replace(/\.$/, '')).join(' · ') : '—']);
const N_ = [
  ['N0', '**Every notes page is now one conversation, in class order (the slide 6 and 7 format you approved).** Each page is a list of numbered steps. Under each step: what the facilitator says (Say), asks (Ask), does, or listens for. Your script, the card text, each insight and each manuscript line sit inside the step where they are used. Nothing is left after the steps except two clearly marked blocks: ON THE PORTAL, AFTER THE TEACHING and LATER, WHEN THE GROUPS DO THE WORK. Slides 1 to 4 are your own notes, untouched.'],
  ['N12', '**Aligned with the two files (your instruction).** Taken out because the files no longer carry them: the private 1-to-5 rating in 1.2 (it was still in one guidance line of the facilitator page; that line is now removed from the page too); the "Critical Insight" lines; the "probing questions" in 4.1, which came from the old maturity assessment. Also taken out because they were my own additions and read like activities: the "quick count" for the Flammables in 4.3, the private note-taking task in 3.2, and the line about writing down who must settle a tension in the six checks. Each element in 4.1 is now taught with your guide and your four questions, and one of those four is put to the room.'],
  ['N13', '**Insights placed where they are used.** All 55 are still in the deck, each spoken inside a step. Ten moved to a better home: "The one thing" to 2.1.2 Decision Filter; "Destination and route" to HOW in 1.2; "Shared meaning, shared action" to 2.1.1; "An honest baseline" to the Section 1 reflections; "Values at the edges" to Dialogue Quality in 3.1d; "A common baseline" to 3.2a; "Signal to watch for" to 3.2c; "Top-down cultures" to 4.1a; "Right destination, right design" to the close of 4.1e; "Seeing the larger system" to 5.1b. Tell me if you want any of them moved or dropped.'],
  ['N14', '**Unit Summary, for your decision.** The five summary blocks and the outputs check speak of the group work as done ("Each group built three connected outputs"). In the teach-first order, the facilitator reads them before the groups go to the portal. I kept your wording and added one line to the notes saying the blocks describe the whole unit, including the portal work. Shall I leave it so, or reword the summary?'],
  ['N1', '**The facilitation blocks are my wording.** On each content slide, The step titles, the questions marked Ask that are not on your pages, and the Listen for lines are my wording. They are built from your guidance, your cards and your manuscript. Your guidance blocks themselves are word for word from the facilitator page. Please read my blocks as you would a draft.'],
  ['N2', '**48 slides, up from 36.** The three functions (2.1.1 to 2.1.3), the four SiP domains (3.1b to 3.1e), the four Flammables (3.2b to 3.2e) and the element groups of 4.1 (4.1d to 4.1g) each have their own slide, so that the notes sit where the facilitator needs them. Say the word and I merge any of them back.'],
  ['N3', '**Lettering in 4.1.** Step 1 runs from 4.1a to 4.1i: how the group works, how each element works, the 14 elements, four slides of elements, the output, the six checks.'],
  ['N4', '**No Section 4 Reflections slide.** The unit has no reflection in Section 4. Sections 1, 2, 3 and 5 each close with their Reflections slide.'],
  ['N5', '**Journal insights.** All 55 insights of the old deck are kept and moved to the slide and line they now deepen (see the last column of the table). Eight had no title line; I gave them one: "Operating logic", "The one thing", "Governing reference points", "The task and its conditions", "Process as an end in itself", "Budget and recognition", "Metrics that flatter", "Declare the outcome first". No new insight is added: the journals were not attached in this chat. Attach them and I add new ones.'],
  ['N6', '**Manuscript detail.** Kept where it still applies. It is spoken inside the steps, under the cue Add. Lines about the Headline, the Storyline and maturity scoring left with that content. Two manuscript lines were adjusted to your new terms ("domains", "Strategy Intent").'],
  ['N7', '**Cover line.** It now reads "Strategy Architecture · Strategy Intent Statement · Success in Practice".'],
  ['N9', '**Opening definition of strategy (changed as you asked).** Participant page: the box "Opening the Session — Your Definition of Strategy" stays, with your sentence word for word. My extra line under the box is removed. Facilitator page: the quote box and my activity note are replaced by one clear part at the top of Section 1, headed **Opening the Session · Defining Strategy in Your Own Words**, with three steps: **Ask** (your sentence), **Collect** (3–4 responses, differences on a whiteboard) and **Keep** (the Unit Summary returns to it). One line under it says where participants enter the definition on the portal.'],
  ['N10', '**Facilitator page: lines reworded so that the facilitator teaches and does not steer participants through the page.** 1.1: "Directing participants through the 9 concepts: Ask participants to expand each concept card individually and read it before moving to the next." now reads "Taking participants through the 9 concepts: Take the concepts one at a time: what each one means, its strategic implication and what fails when it is missing." · 1.2: "Before opening the tabs" now reads "Before presenting the four dimensions"; "Directing through the 4 dimension tabs" now reads "Taking participants through the 4 dimensions"; "HOW tab" and "WHEN tab" now read "HOW" and "WHEN". · Unit Summary: "Expand the summary accordion and read each of the five blocks aloud" now reads "Read each of the five summary blocks aloud". · 5.1: "Participants enter their own responses from their screens." now reads "Each participant enters their own responses in their participant file." · Facilitator Guide, Unit Intent, one line added: "How the unit runs: Teach the whole unit from the deck first. Participants then go to the portal and complete their own page, in the session or after it."'],
  ['N11', '**Key Facilitation Questions and Tone & Watch Points.** They are out of the slide 3 notes, as in your copy. Two things for your word. (a) Step 4 of your slide 3 notes still says "Keep the four Key Facilitation Questions in front of you". Shall I remove that step? (b) The two blocks still sit in the Facilitator Guide tab of the facilitator page, where every unit has them. Shall I remove them there, reword them, or leave them? On slide 3, I changed "using the list above" to "using the list below", because your list of the five sections now sits under the steps.'],
  ['N8', '**One word on the facilitator page, for your decision.** In 1.2 the WHEN tab says "…through which the **direction** will be pursued". In 4.2 it says "…through which the **ambition** will be pursued". The participant page says "ambition" in both places. Shall I change the 1.2 tab to "ambition"?'],
];
const doc = new Document({
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 250 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [run('Unit 2 deck · Guide for review v4 · 5 October 2026 · page ', { size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], font: 'Calibri', size: 16, color: GREY })] })] }) },
    children: [
      new Paragraph({ spacing: { after: 40 }, children: [run('Unit 2 · Strategy Visioning & Success in Practice (SiP)', { size: 20, color: GOLD, bold: true })] }),
      new Paragraph({ spacing: { after: 160 }, children: [run('The rebuilt deck: guide for your review', { size: 40, bold: true, color: GREEN })] }),
      P('The deck is rebuilt from the approved facilitator and participant pages. It has 48 slides and about 23,600 words of presenter notes. It is saved as **Unit decks\\\\Unit 02 - Strategy Visioning & Success in Practice (SiP).pptx** and was sent into the chat.'.replace(/\\\\/g, '\\')),
      P('**To review:** open the deck in PowerPoint and choose View, then Notes Page. Each page shows the slide with its notes underneath.'),
      P('**How to answer:** "Done", or the slide number and what to change. Items N0 to N14 below are the points I would like your eye on. **This is version 4 of the guide:** N0, N12, N13 and N14 are new. N8, N11 and N14 need your answer.'),
      H1('1. How the notes of each slide are laid out'),
      P('Every page from slide 5 on follows the format of slides 6 and 7 that you approved:'),
      B('**HEADING** in capitals, then **HOW TO TEACH IT** (HOW TO USE THIS SLIDE on the reflection slides).'),
      B('**Numbered steps, in class order.** Each step has a short title in bold. Under it: **Say** (the words to speak), **Ask** (the question to put to the room), what to do, and **Listen for**.'),
      B('**Your content sits inside the steps:** the facilitator script, the card text ("What it means, say"), the manuscript detail ("Add") and the journal insights ("Deepen, say", followed by the Insight and Source line).'),
      B('**Section slides** keep the model of your slide 4 (how the section runs, the two outcomes), followed by the steps for opening the section.'),
      B('**ON THE PORTAL, AFTER THE TEACHING:** what participants complete for that part once the teaching is over.'),
      B('**LATER, WHEN THE GROUPS DO THE WORK** (Sections 4 and 5): coaching for the portal work, kept apart from the teaching steps.'),
      P('No timings appear anywhere. Nothing is asked of participants before the session.'),
      H1('2. For your word'),
      table([700, 8938], ['Code', 'Point'], N_, { codeCol: true }),
      H1('3. The 48 slides and where the insights sit'),
      table([650, 4100, 4888], ['Slide', 'Title', 'Journal insights in the notes'], map),
      H1('4. Checks done'),
      B('The slides are your own copy of the deck, unchanged. Only the notes of slides 5 to 48 were replaced.'),
      B('Every card of the two pages is in the notes word for word, every guidance line of the facilitator page is spoken or acted on in a step, and all 55 journal insights are placed once.'),
      B('I read all 44 notes pages from first line to last, and a second, independent reader checked them against the two files.'),
      B('The wording rules were scanned: no contrast constructions, no timings, ® on every Strategy2Results and S2R.'),
      B('The pictures and notes for the portal deck reader are ready in Claude outputs\\Deck upload\\Module-2. They go to Supabase after your "Done".'),
    ]
  }]
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('Unit 2 deck - Guide for review.docx', b); console.log('ok', b.length); });
