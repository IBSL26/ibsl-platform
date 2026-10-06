# -*- coding: utf-8 -*-
"""Rebuild of unit2_m1_lens1_f.html from Carol's 'Unit 2 Rebuild _2026_10_05.docx'."""
import sys, re
from common import *

SRC, OUT = sys.argv[1], sys.argv[2]
o = read(SRC)

def fg(label, html, top=False):
    st = ' style="margin-top:22px;"' if top else ''
    return '<div class="fac-note-full"%s><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — %s</div>%s</div>' % (st, label, html)
def activity(html):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#128203; PARTICIPANT ACTIVITY</div>%s</div>' % html
def P(*paras): return ''.join('<p>%s</p>' % p for p in paras if p)
def UL(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def Q(s): return '<em>"%s"</em>' % s
def T(mins): return ''   # Carol, 5 Oct: no times anywhere in the facilitator file

# ════════ HEAD ════════
head = o[:once(o, '<div class="mod-panel active" id="mod0">')]
head = rep(head, OLD_KLO1, '<span class="klo">%s</span>' % KLO1)
head = rep(head,
    '<p class="unit-desc">This unit builds the master definition of strategy and the 3W1H framework, and produces a Success in Practice (SiP) statement — a Headline and a Storyline — through collective executive co-creation.</p>',
    '<p class="unit-desc">This unit helps leaders to determine the organisation&rsquo;s strategy architecture, articulate its strategic intent and define the Success in Practice (SiP) of the chosen Strategy Intent.</p>')
i = head.index('</style>')
head = head[:i] + NEW_CSS.replace('var(--ACC)', 'var(--gold)') + head[i:]
head = rep(head, '<!-- ═══ TAB 1: AWARENESS ═══ -->\n', '<!-- ═══ FACILITATOR GUIDE ═══ -->\n')

# ════════ GUIDE TAB ════════
g_old = cut(o, '<div class="mod-panel active" id="mod0">', '<div class="mod-panel" id="mod1">', inc_end=False)
g_head = g_old[:g_old.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>')]
g_tail = g_old[g_old.index('<div class="mod-nav"><button class="btn" onclick="showMod(1)">'):]
guide = g_head + '''<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>
<p>Before the organisation can define where it is going, leaders must agree on what strategy actually means, in the precise, strategic sense, translated to operational reality, that makes every subsequent decision coherent.</p>
<p>Three connected outputs carry the unit: the Strategy Architecture, the Strategy Intent Statement and Success in Practice. Protect the time in Section 4 for each group to build them in that order.</p>
<p><strong>How the unit runs:</strong> Teach the whole unit from the deck first. Participants then go to the portal and complete their own page, in the session or after it.</p>
</div>
<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Key Facilitation Questions</div>
<p>Four questions anchor the unit. Ask each one where it belongs as you teach from the deck.</p>
<ul>
<li><strong>Sections 1 and 4 &middot; Strategy Architecture:</strong> <em>&ldquo;How well defined is each part of our strategy architecture today?&rdquo;</em></li>
<li><strong>1.3, Section 3 and 4.3 &middot; Success in Practice:</strong> <em>&ldquo;If our Strategy Intent is successful, what should we see in practice?&rdquo;</em></li>
<li><strong>Section 2 &middot; Decision Filter:</strong> <em>&ldquo;When a new initiative, investment or opportunity appears, what tells us whether it belongs in our strategy?&rdquo;</em></li>
<li><strong>Section 5 &middot; Role contribution:</strong> <em>&ldquo;From my executive role, what must I contribute for this Success in Practice to become real?&rdquo;</em></li>
</ul></div>
<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Tone &amp; Watch Points</div>
<p>These four points apply when the groups do the work on the portal, after the teaching.</p>
<p><strong>4.2 &middot; Strategy Intent Statement. Watch for:</strong> a statement that carries every point from the Architecture. Say: <em>&ldquo;The Architecture contains the depth. The Intent must provide the clarity.&rdquo;</em></p>
<p><strong>4.3 &middot; Success in Practice. Watch for:</strong> statements that list initiatives, projects or activities. Bring the group back to observable reality. Ask: <em>&ldquo;What is happening when the strategy is working?&rdquo;</em></p>
<p><strong>4.3 &middot; Balance. Watch for:</strong> one perspective defining success for the whole organisation. Use the SiP Flammables as the balance check.</p>
<p><strong>5.1 &middot; Role contribution. Watch for:</strong> general statements such as &ldquo;Support the strategy&rdquo;. Ask: <em>&ldquo;What does this role specifically decide, enable, coordinate, resource, protect or change?&rdquo;</em></p>
</div>
''' + g_tail

# ════════ SECTION 1 ════════
s1_guid = line_with(o, 'FACILITATOR GUIDANCE — Section 1 · Awareness</div>')
s1_guid = rep(s1_guid, 'its three building blocks: the master definition, the 3W1H framework, and Success in Practice.',
                       'its three building blocks: the Strategy Architecture, the Strategy Intent Statement and Success in Practice.')
s1_guid = rep(s1_guid, 'Every word in the master definition has strategic consequence.', 'Every word in the definition has strategic consequence.')
OPEN_OLD = '<p><strong>Opening the session:</strong> Before showing any content, ask participants — <em>"Write your definition of strategy in one sentence — right now, without consulting anyone."</em> Collect 3–4 responses. Note the differences on a whiteboard. This gap between answers is exactly the problem this unit solves. Use it as the opening provocation.</p>'
s1_guid = rep(s1_guid, OPEN_OLD, '')

script = '''<div class="fac-note" style="margin-top:22px;">
  <div class="fac-label">Facilitator Script</div>
  <p><strong>Set the frame:</strong> Before defining strategy, introduce Strategy Architecture as the underlying logic that gives a strategy its structure.</p>
  <p style="margin-top:8px;"><strong>Explain:</strong> "Before we can express strategy clearly, we need to understand what sits underneath it. We call this the Strategy Architecture — the interconnected choices and logic that determine what the organisation will do, why, how and when; how it will create, deliver and sustain value; for whom; and within what environment."</p>
  <p style="margin-top:8px;">Emphasise that the purpose of this section is to unpack the architecture before trying to produce a strategy statement. A strategy can sound compelling while important parts of its underlying logic remain weak, disconnected or undefined.</p>
  <p style="margin-top:8px;">As participants work through the concepts, ask them to consider: "How well defined is each part of our strategy architecture today?"</p>
  <p style="margin-top:8px;"><strong>Bridge to the definition:</strong> "We are now going to unpack the Strategy2Results® definition of strategy. Each concept in the definition represents part of the architecture. Once we understand the parts and how they connect, we can begin constructing a coherent strategic position."</p>
</div>
'''

b11 = cut(o, '  <div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Section 1.1</div>', '<div id="conceptList"></div>')

g12 = line_with(o, 'FACILITATOR GUIDANCE — Section 1.2</div>')
g12 = rep(g12,
    '<p><strong>Before opening the tabs:</strong> Draw attention to the Critical Insight box — <em>"Most strategies fail because HOW and WHEN are underdeveloped."</em> Ask participants',
    '<p><strong>Positioning the statement:</strong> The Strategy Architecture holds the depth and the supporting logic. The Strategy Intent Statement is crisp, directional and easy to express. Participants derive their own statement in Section 4; here they learn what it brings forward.</p><p><strong>Before opening the tabs:</strong> Ask participants')
w1h_tabs = cut(o, '  <div class="ph-tabs" id="w1hTabs">', '<div id="w1hPanels"></div>')
b12 = g12 + '''
  <p>The Strategy Architecture provides the foundation from which the Strategy Intent Statement is derived. It has established the organisation's strategic choices and the logic connecting them.</p>
  <p>The Strategy Intent Statement brings forward four dimensions from that architecture. Select each one.</p>
''' + w1h_tabs + '''
  <p style="margin-top:16px;">These four dimensions are then crystallised into one clear Strategy Intent Statement.</p>
  <p>The strength of the statement comes from the architecture beneath it. It should therefore be crisp, directional and easy to express, while the Strategy Architecture holds the depth and supporting logic.</p>
  <div class="hbox"><p>The resulting Strategy Intent becomes the organisation's directional anchor for strategic choices, alignment and execution.</p></div>'''

DOM_DESC_13 = ['What customers and other value recipients experience when the strategic intent is working.',
               'How the organisation operates, coordinates, delivers and adapts when the capabilities required by the intent are functioning effectively.',
               'How people understand the strategic intent, make decisions, collaborate, take ownership and behave when the intent is embedded in the organisation.',
               'How the organisation benefits across its measures of enterprise success.']
def dom_grid(descs):
    return '  <div class="u2-grid">\n' + ''.join(
        '    <div class="u2-card"><div class="u2-card-h" style="color:%s;">D%d · %s</div><p>%s</p></div>\n' % (DOM_COL[i], i + 1, DOM[i], descs[i])
        for i in range(4)) + '  </div>'

b13 = '  ' + fg('Section 1.3', P(
    'The Strategy Intent Statement establishes the ambition. Success in Practice defines what must be seen, experienced and executed for that ambition to become reality within a given time horizon. <strong>Defining this together creates a shared picture of success, reducing the risk of different functions interpreting the same strategic intent differently.</strong>',
    'Position participants inside the future created by the Strategy Intent. Ask them to imagine that the intent has been successfully realised and describe the observable organisational reality.',
    '<strong>The central question:</strong> ' + Q('If our Strategy Intent is successful, what should we see in practice?'),
    '<strong>Facilitator emphasis:</strong> Keep participants focused on <strong>observable reality</strong>. The SiP describes what is happening when the strategy is working. Initiatives, projects and activities stay out of it. <strong>The aim is shared construction: leaders should leave with a common understanding of what success looks like across the organisation.</strong>',
    T('8–10'))) + '''
  <div class="quote"><p>"If our Strategy Intent is successful, what should we see in practice?"</p></div>
  <p>Success is considered across four observable domains:</p>
''' + dom_grid(DOM_DESC_13) + '''
  <p>Together, the four domains create a shared organisational picture of success against which decisions, trade-offs and execution can be aligned.</p>'''

# Carol, 5 Oct (night): the opening exercise shows on the facilitator page as well
OPENING_F = (fg('Opening the Session · Defining Strategy in Your Own Words', P(
    '<strong>Ask:</strong> Before showing any content, ask each participant to define strategy in their own words: ' + Q('Write your definition of strategy in one sentence — right now, without consulting anyone.'),
    '<strong>Collect:</strong> Collect 3–4 responses. Note the differences on a whiteboard. This gap between answers is exactly the problem this unit solves. Use it as the opening provocation.',
    '<strong>Keep:</strong> Ask every participant to keep their definition. The Unit Summary returns to it.'))
    + '\n' + activity(P('Each participant enters their definition of strategy in the box at the top of Section 1 of the participant file: "Opening the Session — Your Definition of Strategy".')) + '\n')
sec1 = ('<div class="mod-panel" id="mod1">\n' + hero(1) + '<div class="mod-body">\n' + slo(1) + '\n\n' + s1_guid + '\n\n' + OPENING_F + '\n' + script + '\n'
        + acc(*TITLES['1.1'], b11, True, 'STRATEGY ARCHITECTURE') + '\n'
        + acc(*TITLES['1.2'], b12, False, 'STRATEGY INTENT STATEMENT') + '\n'
        + acc(*TITLES['1.3'], b13, False, 'SiP') + '\n'
        + '<div class="mod-nav"><button class="btn" onclick="showMod(0)">← Facilitator Guide</button><button class="btn" onclick="showMod(2)">Section 2 — Intelligence →</button></div>\n</div>\n</div>\n')

# ════════ SECTION 2 ════════
s2_guid = fg('Section 2 · Intelligence', P(
    '<strong>Section intent:</strong> The Strategy Intent and SiP become useful when they begin to shape how the organisation <strong>aligns, makes choices and executes</strong>.',
    'Explain that once leaders have established a shared strategic ambition and defined what success looks like in practice, those two outputs become common reference points across the organisation.',
    'They serve three important functions:') + UL([
    '<strong>Strategic Alignment</strong> — keeping people and functions oriented around the same ambition and picture of success.',
    '<strong>Decision Filter</strong> — providing a basis for determining which choices, opportunities and investments support the strategy.',
    '<strong>Execution Coherence</strong> — helping different functions understand how their individual contributions must connect to produce the enterprise outcome.']), top=True)
g21 = fg('Section 2.1', P(
    'Walk participants through each function and demonstrate how <strong>Strategy Intent and SiP work together</strong>. The Intent anchors the ambition and strategic choices; SiP anchors the organisational reality those choices are intended to produce.',
    'As you move through the three functions, invite participants to consider: ' + Q('What happens in an organisation when this function is weak or absent?'),
    'Use the <strong>Decision Filter</strong> to make the application particularly practical. Ask: ' + Q('When a new initiative, investment or opportunity appears, what tells us whether it belongs in our strategy?'),
    'The Strategy Intent provides the test of <strong>strategic fit</strong>. SiP provides the test of <strong>strategic contribution</strong>: whether the choice moves the organisation closer to the success it has defined.',
    T('15–20')))
sec2 = ('<!-- ═══ TAB 2: INTELLIGENCE ═══ -->\n<div class="mod-panel" id="mod2">\n' + hero(2) + '<div class="mod-body">\n' + slo(2) + '\n\n' + s2_guid + '\n\n\n'
        + acc(*TITLES['2.1'], '  ' + g21 + '<div id="archList"></div>', True) + '\n'
        + '<div class="mod-nav">\n  <button class="btn" onclick="showMod(1)">← Section 1 — Awareness</button>\n  <button class="btn" onclick="showMod(3)">Section 3 — Extrapolating →</button>\n</div>\n</div>\n</div>\n')

# ════════ SECTION 3 ════════
s3_guid = fg('Section 3 · Extrapolating', P(
    '<strong>Section intent:</strong> We have established that Success in Practice answers a central question: ' + Q('If our Strategy Intent is successful, what should we see in practice?') + ' This section takes that question deeper.',
    'Each of the four SiP domains covers an important part of organisational reality. Broad statements about customer experience, operational capability, people and culture, or enterprise value fall short. Leaders need to be able to recognise <strong>what success would actually look like when it begins to show up in practice</strong>.',
    'This is where <strong>observable indicators</strong> become useful. The indicators help us examine each SiP domain more deeply. They show the kinds of conditions we would expect to observe when that aspect of the Strategy Intent is working, as well as the signals that may indicate something is missing.',
    'There is also a second discipline: <strong>balance across the four domains</strong>. A leadership team can develop a strong picture of customer success while overlooking the operational capability required to deliver it. It can describe an enabling culture without connecting that culture to enterprise value. It can define strong financial outcomes without describing the customer, operational and people conditions required to produce them.',
    'This section therefore develops two disciplines: <strong>Depth within each SiP domain. Balance across all four SiP domains.</strong>',
    'We begin by examining the observable indicators within each domain. We then examine what happens when one domain becomes dominant and begins to distort the organisation\'s overall picture of success.',
    ''), top=True)
g31 = fg('Section 3.1', P(
    'Each SiP domain is examined through a set of <strong>observable indicators</strong>. These indicators help leaders move from a broad description of success to the specific conditions through which that success would become visible in the organisation.',
    'For every indicator, examine two positions:',
    '<strong>When Working</strong> describes what we would expect to observe when that aspect of the SiP is functioning effectively.',
    '<strong>Signal of Absence</strong> describes what may become visible when that condition is weak, missing or disconnected from the Strategy Intent.',
    'Use both positions to deepen the discussion. Sometimes the absence of a condition provides the clearest evidence of why it matters.',
    'The indicators sit alongside the organisation\'s SiP. They help leaders <strong>test, deepen and make observable the success they have defined.</strong>',
    T('12–14')))
dim_tabs = cut(o, '  <div class="dim-tabs" id="dimTabsF">', '<div id="dimPanels"></div>')
b31 = '  ' + g31 + '''
  <p>Each SiP domain is examined through a set of observable indicators. Every indicator has two positions: <strong>When Working</strong> and <strong>Signal of Absence</strong>.</p>
''' + dim_tabs
g32 = fg('Section 3.2', P(
    'The four SiP domains are designed to describe <strong>one organisational reality</strong>.',
    'In practice, leadership teams naturally bring different perspectives into the conversation. A commercial leader may see success primarily through customers and growth. An operations leader may emphasise efficiency, process and delivery. A people leader may focus on culture and capability. A finance leader may foreground financial and enterprise outcomes.',
    'Each perspective contributes something important.',
    'The strategic risk emerges when <strong>one perspective becomes so dominant that it begins to define success for the entire organisation</strong>.',
    'This is what the <strong>SiP Flammables</strong> are designed to expose.',
    'They provide a balance test for the SiP. They help leaders recognise when a legitimate dimension of success has become disproportionately influential and the enterprise picture has started to narrow into a functional one.',
    T('6–8')))
b32 = '  ' + g32 + '''
  <p>The four SiP domains describe one organisational reality. When one perspective becomes dominant, the enterprise picture narrows into a functional one. Expand each pattern to see what it creates, the indicators that reveal it and the strategic risk if it is not balanced.</p>
  <div id="flamList"></div>'''
sec3 = ('<!-- ═══ TAB 3: EXTRAPOLATING ═══ -->\n<div class="mod-panel" id="mod3">\n' + hero(3) + '<div class="mod-body">\n' + slo(3) + '\n\n' + s3_guid + '\n\n\n'
        + acc(*TITLES['3.1'], b31, True) + '\n' + acc(*TITLES['3.2'], b32) + '\n'
        + '<div class="mod-nav">\n  <button class="btn" onclick="showMod(2)">← Section 2 — Intelligence</button>\n  <button class="btn" onclick="showMod(4)">Section 4 — Integration →</button>\n</div>\n</div>\n</div>\n')

# ════════ SECTION 4 ════════
s4_guid = fg('Section 4 · Integration', P(
    '<strong>Section intent:</strong> This is the production section of the unit. Participants now apply the concepts developed through Awareness, Intelligence and Extrapolating to construct the organisation\'s Strategy Intent Design.',
    'The work happens collectively because strategy requires more than agreement with a finished statement. Leaders need to contribute to the thinking, surface different interpretations, work through tensions and arrive at a position they can collectively own.',
    'Each group will work through <strong>three connected stages</strong>:') + UL([
    '<strong>4.1</strong> — Build the Strategy Architecture: Work through the 14 elements, then write the group\'s Strategy Architecture output.',
    '<strong>4.2</strong> — Derive the Strategy Intent Statement: Use the completed architecture to crystallise WHAT, WHY, HOW and WHEN into one clear statement of strategic ambition.',
    '<strong>4.3</strong> — Build Success in Practice: Define what must be seen, experienced and executed across the four SiP domains, confirm each domain statement, and bring the four together into the group\'s SiP.']) + P(
    'Emphasise the sequence. Each output provides the foundation for the next: <strong>Strategy Architecture → Strategy Intent → Success in Practice</strong>',
    'The quality of the final SiP therefore depends on the quality of the Intent, and the quality of the Intent depends on the thinking captured in the Architecture.',
    '<strong>Working in groups:</strong> Participants work in their assigned groups throughout the exercise. Encourage groups to surface differences before resolving them. Different interpretations are useful because they expose assumptions, trade-offs and areas where the organisation\'s strategic thinking is not yet coherent.',
    'The objective is <strong>collective construction of one enterprise position</strong>.',
    ''), top=True)

g41 = fg('Section 4.1', P(
    'This is the foundation of the exercise.',
    'Each group works through the <strong>14 elements of the Strategy2Results® Strategy Definition</strong>. The purpose is to establish the thinking and logic underneath the organisation\'s strategic position before attempting to express that position concisely.',
    'Remind participants that the elements are interconnected. A strong answer to one element can expose a weakness or contradiction in another. For example, the value the organisation intends to create must be supported by its HOW; its WHEN must reflect the capabilities that need to be built; and its approach to sustaining value must respond to the forces within its operating environment.',
    'Encourage participants to capture <strong>actual strategic choices</strong> and to leave broad organisational aspirations out.',
    'As each element is completed, the group should review what it has written and confirm: ' + Q('Is this what we mean?'),
    'The purpose of confirmation is to ensure that the written position represents the group\'s thinking before it becomes part of the architecture.',
    '<strong>Producing the Strategy Architecture:</strong> Once all 14 elements have been completed, the group should step back from the individual responses and examine them as <strong>one strategic system</strong>. Ask groups to consider: ' + Q('What is this architecture collectively saying about the organisation\'s strategy?'),
    'They should then write out their <strong>Strategy Architecture output</strong>. The output should bring together the major strategic choices and logic revealed through the 14 elements. It should be sufficiently detailed to preserve the thinking underneath the strategy while showing how the different choices connect.',
    'Before finalising, ask groups to check:') + UL(SIX_CHECKS) + P(
    'The completed Strategy Architecture becomes the source for Step 2.', T('30–35')))
el_list = ''
for n, (nm, tag, el_guide, qs) in enumerate(ELEMENTS, 1):
    el_list += ('  <div class="sub-acc"><div class="sub-acc-h" onclick="tSA(this)"><span><strong style="color:var(--gold);margin-right:8px;">%d · %s</strong>%s</span><span class="sub-arr">▼</span></div>'
                '<div class="sub-acc-b cols2"><div class="u2-why"><p class="u2-lbl" style="color:rgba(255,255,255,.4);">Guide shown to participants</p><p class="u2-txt">%s</p></div>'
                '<div class="u2-why"><p class="u2-lbl" style="color:rgba(201,168,76,.6);">The %s questions</p><ol class="u2-ql">%s</ol></div></div></div>\n'
                ) % (n, amp(nm), amp(tag), el_guide, {4: 'four', 5: 'five'}[len(qs)], ''.join('<li>%s</li>' % q for q in qs))
out_heads = ''.join('    <div class="u2-card"><div class="u2-card-h">%s</div><p>%s</p></div>\n' % (amp(g), amp(' · '.join(names))) for g, names in ARCH_GROUPS)
b41 = ('  ' + g41 + '\n  ' + activity(
    P('The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page of the participant file, in the session or after it.',
      'Each group works in 4.1 of the participant file, one element at a time:') + UL([
        'It answers the questions of the element and selects <strong>Generate what this is saying</strong>.',
        'The page shows what the group\'s inputs are saying and asks: <em>"Is this what you mean?"</em>',
        'The group selects <strong>Yes, confirm</strong>, or <strong>No, refine</strong> and states what the position should say.',
        'A progress bar counts the confirmed elements. When all 14 are confirmed, the Strategy Architecture output unlocks. The group reviews it, refines it and confirms it. It can then be printed.']) +
    P('The elements, guides and questions below are for your preparation.'))
    + '\n  <p>The 14 elements follow the Strategy2Results® definition of strategy. OUTPUT, the first concept in 1.1, is what the 14 elements produce: the Strategy Architecture. Click each element to expand.</p>\n'
    + el_list
    + '  <h4>The Strategy Architecture Output</h4>\n'
    + '  <p>The page brings the 14 confirmed elements together under five headings. The group refines the text until it accurately represents the organisation\'s strategic architecture.</p>\n'
    + '  <div class="u2-grid">\n' + out_heads + '  </div>')

W_DEF = ['The value the organisation has chosen to create and its field of play.',
         'The rationale for those choices and why they matter.',
         'The operating model, capabilities and mechanisms through which the value will be delivered.',
         'The timing, sequencing and strategic moves through which the ambition will be pursued.']
g42 = fg('Section 4.2', P(
    'With the Strategy Architecture established, groups now crystallise that thinking into a <strong>Strategy Intent Statement</strong>.',
    'The Architecture contains the depth. The Intent must provide the clarity.',
    'Bring forward the four dimensions already established through the architecture:',
    '<strong>WHAT</strong> — the value the organisation has chosen to create and its field of play.',
    '<strong>WHY</strong> — the rationale for those choices and why they matter.',
    '<strong>HOW</strong> — the operating model, capabilities and mechanisms through which the value will be delivered.',
    '<strong>WHEN</strong> — the timing, sequencing and strategic moves through which the ambition will be pursued.',
    'Ask groups to review these four dimensions together and derive <strong>one crisp Strategy Intent Statement</strong>.',
    '<strong>Facilitator emphasis:</strong> Protect the Intent from becoming overloaded. Participants may try to carry every important point from the Architecture into the statement. Remind them that the Architecture already holds that detail.',
    'The Strategy Intent Statement <strong>crystallises the ambition</strong>. The Architecture keeps the detail.',
    'A strong Intent should allow a leader to understand the organisation\'s strategic position without needing a paragraph of explanation.',
    'Once drafted, have the group read the statement against its completed Architecture and confirm: ' + Q('Does this statement faithfully express the strategic ambition contained in our Architecture?'),
    'Where the statement exposes a contradiction in the Architecture, resolve the underlying contradiction before finalising the Intent.',
    'The confirmed Strategy Intent becomes the source for Step 3.', T('10–15')))
b42 = '  ' + g42 + '\n  ' + activity(P('In 4.2 of the participant file each group sees its own answers for WHAT, WHY, HOW and WHEN, deduces one crisp Strategy Intent Statement from them and types it in. The group confirms the statement. It can then be printed. Every member types the agreed statement into their own page.')) + '''
  <p>The four dimensions brought forward from the architecture:</p>
  <div class="u2-grid">
''' + ''.join('    <div class="u2-card"><div class="u2-card-h">%s</div><p>%s</p></div>\n' % (W[i], W_DEF[i]) for i in range(4)) + '''  </div>
  <div class="quote"><p>"Does this statement faithfully express the strategic ambition contained in our Architecture?"</p></div>'''

DOM_43 = [('Describe what customers and other value recipients experience when the Strategy Intent is working.',
           'Use the observable indicators explored in Section 3 to deepen the discussion where useful, but keep the group\'s final output focused on its <strong>specific Strategy Intent</strong>.'),
          ('Describe how the organisation operates, coordinates, delivers and adapts when the capabilities required by the Strategy Intent are functioning effectively.', ''),
          ('Describe how people understand the Strategy Intent, make decisions, collaborate, take ownership and behave when the intent is embedded in organisational practice.', ''),
          ('Describe how the organisation is benefiting across the measures of enterprise success that matter to this Strategy Intent.', '')]
g43 = fg('Section 4.3', P(
    'The Strategy Intent Statement establishes the ambition. The group now defines what must be <strong>seen, experienced and executed</strong> for that ambition to become reality within the agreed time horizon.',
    'Position the group inside the future described by its Strategy Intent. Use one central question: ' + Q('If our Strategy Intent is successful, what should we see in practice?'),
    'The group works through the four SiP domains:') + ''.join(
    P('<strong>%d. %s</strong> — %s%s The group produces <strong>one %s statement</strong>.' % (i + 1, DOM[i], DOM_43[i][0], (' ' + DOM_43[i][1]) if DOM_43[i][1] else '', DOM[i])) for i in range(4)) + P(
    '<strong>Confirming each SiP domain:</strong> After drafting each statement, pause and ask: ' + Q('Is this what success in this domain should look like if our Strategy Intent is realised?') + ' Refine the statement until the group confirms it.',
    'This is important. The SiP should emerge from the group\'s own definition of success. Generic descriptions of a successful organisation have no place in it.',
    'Once all four statements are confirmed, place them together and read them as <strong>one Success in Practice</strong>.',
    '<strong>Test the SiP:</strong> Use the two quality checks from Section 3.',
    '<strong>Depth:</strong> Is each statement specific enough that we could recognise the condition if we saw it in practice?',
    '<strong>Balance:</strong> Do the four statements collectively describe enterprise success, or has one perspective become dominant?',
    'Use the <strong>SiP Flammables</strong> as the final balance check.',
    'The four confirmed statements together become the organisation\'s <strong>Success in Practice</strong>.',
    '<strong>Closing Section 4:</strong> Each group now holds three connected outputs: its Strategy Architecture, its Strategy Intent Statement and its Success in Practice. Close the exercise by having each group display or print the three together: <strong>Strategy Architecture → Strategy Intent → Success in Practice</strong>',
    'Then reinforce the connection: <strong>The Architecture provides the logic. The Intent crystallises the ambition. Success in Practice makes the ambition observable.</strong>',
    'These three outputs become the strategic foundation that subsequent S2R® work will carry into alignment, execution and performance.', T('20–25')))
sip_list = ''
for i, (title, lead, qs) in enumerate(SIP_DOMAINS):
    sip_list += ('  <div class="sub-acc"><div class="sub-acc-h" onclick="tSA(this)"><span><strong style="color:%s;margin-right:8px;">D%d · %s</strong></span><span class="sub-arr">▼</span></div>'
                 '<div class="sub-acc-b cols2"><div class="u2-why"><p class="u2-lbl" style="color:rgba(255,255,255,.4);">Lead question</p><p class="u2-txt">%s</p></div>'
                 '<div class="u2-why"><p class="u2-lbl" style="color:rgba(201,168,76,.6);">The three input questions</p><ol class="u2-ql">%s</ol></div></div></div>\n'
                 ) % (DOM_COL[i], i + 1, amp(title), lead, ''.join('<li>%s</li>' % q for q in qs))
b43 = ('  ' + g43 + '\n  ' + activity(
    P('In 4.3 of the participant file, for each SiP domain the group:') + UL([
        'answers the three input questions;',
        'derives one statement for the domain from those answers and types it in;',
        'confirms the statement.']) +
    P('The group writes every statement, and every member types the agreed entries into their own page. When all four statements are confirmed, they appear together, numbered 1 to 4, as the group\'s Success in Practice. The group confirms it. It can then print its three outputs as one report: the Strategy Intent Design.',
      '<strong>Into the Capstone:</strong> the three confirmed outputs feed the team\'s Capstone Blueprint. Its Unit 2 section opens once every member of the team has completed Unit 2, and brings the three outputs in from the member\'s page. The team reads them together and confirms them there.'))
    + '\n  <div class="quote"><p>"If our Strategy Intent is successful, what should we see in practice?"</p></div>\n'
    + '  <p>Click each domain to see its lead question and input questions.</p>\n'
    + sip_list)

sec4 = ('<!-- ═══ TAB 4: INTEGRATION ═══ -->\n<div class="mod-panel" id="mod4">\n'
        + hero(4, 'Collective Intelligence of Execution · Strategy Architecture → Strategy Intent → Success in Practice')
        + '<div class="mod-body">\n' + slo(4) + '\n\n' + s4_guid + '\n\n\n'
        + acc(*TITLES['4.1'], b41, True, 'STEP 1: STRATEGY ARCHITECTURE') + '\n'
        + acc(*TITLES['4.2'], b42, False, 'STEP 2: STRATEGY INTENT STATEMENT') + '\n'
        + acc(*TITLES['4.3'], b43, False, 'STEP 3: SUCCESS IN PRACTICE') + '\n'
        + '<div class="mod-nav"><button class="btn" onclick="showMod(3)">← Section 3 — Extrapolating</button><button class="btn" onclick="showMod(5)">Section 5 — Application →</button></div>\n</div>\n</div>\n')

# ════════ SECTION 5 ════════
s5_guid = fg('Section 5 · Application', P(
    '<strong>Section intent:</strong> This section moves the group from the agreed <strong>Success in Practice</strong> into practical executive contribution.',
    'In Section 4, the group has already produced: <strong>Strategy Architecture → Strategy Intent → Success in Practice</strong>',
    'Success is already defined. The work in this section is to apply it.',
    'Each participant now asks: ' + Q('From my executive role, what must I contribute for this Success in Practice to become real?'),
    'The Application section helps the group see whether the agreed strategy is supported by clear leadership contribution, cross-functional ownership and shared accountability.',
    '<strong>Sequencing the two activities:</strong>') + UL([
    '<strong>5.1</strong> — Role Contribution to SiP: Each participant completes the table from an assigned executive role',
    '<strong>5.2</strong> — SiP Statement Collective Application: Each group shares its SiP statement and explains how the role contributions support it']), top=True)
g51 = fg('Section 5.1', P(
    '<strong>Purpose:</strong> This table captures how each executive role contributes to the agreed Success in Practice.',
    'Ask participants to return to the four SiP statements produced in Section 4: Customer Experience &amp; Value · Operational Capability &amp; Execution Rhythm · People &amp; Culture Dynamics · Enterprise Value Creation.',
    'Each participant now completes the table from the perspective of their assigned executive role. Use this central question: ' + Q('From this role, what must be contributed so that the agreed Success in Practice becomes real?'),
    'Participants should write in the <strong>present tense of the future</strong>, as if the strategy is already working. For example:') + UL([
    '"Customers experience…"', '"Operations are able to…"', '"People consistently…"', '"The organisation creates value through…"']) + P(
    'Encourage practical and role-specific responses. Push back on general statements such as:') + UL([
    '"Support the strategy"', '"Improve communication"', '"Collaborate better"', '"Drive performance"']) + P(
    'Ask in response: ' + Q('What does this role specifically decide, enable, coordinate, resource, protect or change?'),
    'After completing the row, each participant should check whether their contribution strengthens all four SiP domains or only reflects the priorities of their own function.',
    '<strong>Recording:</strong> Each participant enters their own responses in their participant file.', T('20–30')))
DOM_51 = ['What this role contributes so that customers and other value recipients experience what the SiP describes.',
          'What this role contributes so that the organisation operates, coordinates, delivers and adapts as the SiP describes.',
          'What this role contributes so that people understand the Strategy Intent, decide, collaborate, take ownership and behave as the SiP describes.',
          'What this role contributes so that the organisation benefits across its measures of enterprise success.']
b51 = '  ' + g51 + '\n  ' + activity(P('Each participant selects the assigned executive role in 5.1 of the participant file and completes the four domains of the table from that role. The group\'s four SiP statements from Section 4 are shown above the table.')) + '''
  <div class="quote"><p>"From this role, what must be contributed so that the agreed Success in Practice becomes real?"</p></div>
''' + dom_grid(DOM_51)
g52 = fg('Section 5.2', P(
    '<strong>Purpose:</strong> This activity allows each group to apply its agreed SiP statement to the executive roles and examine how the strategy becomes practical through leadership contribution.',
    'After all CXO rows have been completed, invite each group to share its SiP statement and explain how the different role contributions support it.',
    'As groups share, listen for alignment, gaps, tensions and areas where the SiP statement may need clearer execution ownership.',
    'The focus is on whether the agreed SiP can be supported by practical leadership contribution across the executive team.', T('15–20')))
LISTEN = [('Alignment', 'Where the role contributions support the SiP statement and one another.'),
          ('Gaps', 'Which part of the SiP statement has no role contributing to it.'),
          ('Tensions', 'Where role contributions pull against one another.'),
          ('Execution Ownership', 'Where the SiP statement needs clearer execution ownership.')]
b52 = '  ' + g52 + '\n  ' + activity(P('As groups share, participants record what they observe under four headings in 5.2 of the participant file. They then write their Section 5 reflection.')) + '''
  <p>What to listen for as each group shares:</p>
  <div class="u2-grid">
''' + ''.join('    <div class="u2-card"><div class="u2-card-h" style="color:%s;">%s</div><p>%s</p></div>\n' % (DOM_COL[i], LISTEN[i][0], LISTEN[i][1]) for i in range(4)) + '  </div>'

us_old = cut(o, '<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">Unit Summary</span>', '<div id="summaryList"></div>\n</div>\n</div>\n')
us = rep(us_old,
    '<ul><li>A collective Strategy Maturity Assessment score (with the lowest group identified)</li><li>Individual SiP contributions from all assigned executive roles</li><li>A working draft of the collective SiP (Headline + Storyline)</li></ul>',
    '<ul><li>A Strategy Architecture output from each group</li><li>A confirmed Strategy Intent Statement from each group</li><li>Four confirmed SiP statements from each group</li><li>A role contribution row from each participant</li></ul>')
us = rep(us, 'What we built today is the strategic destination. Unit 3 maps that destination',
             'What we built today is the strategic foundation: the Architecture, the Intent and the Success in Practice. Unit 3 maps that Success in Practice')

sec5 = ('\n\n<div class="mod-panel" id="mod5">\n'
        + hero(5, 'Each participant applies the agreed Success in Practice to an executive role and defines what that role must contribute to make the Strategy Intent real.')
        + '<div class="mod-body">\n' + slo(5) + '\n\n' + s5_guid + '\n\n'
        + acc(*TITLES['5.1'], b51, True, 'ROLE CONTRIBUTION') + '\n'
        + acc(*TITLES['5.2'], b52, False, 'COLLECTIVE APPLICATION') + '\n'
        + us + '\n'
        + '<div class="mod-nav">\n  <button class="btn" onclick="showMod(4)">← Section 4 — Integration</button>\n</div>\n</div>\n</div>\n\n\n</div><!-- /main -->\n\n')

# ════════ SCRIPT ════════
sc = o[once(o, '<script>\n// ── DATA ──'):]
concepts = cut(sc, 'var CONCEPTS=[', '\n];\n')
w1h = cut(sc, 'var W1H=[', '\n];\n')
for nm, d in zip(W, W_DEF[:3] + ['The timing, sequencing and strategic moves through which the ambition will be pursued.']):
    w1h, k = re.subn(r"(\{name:'%s',sub:'[^']*',)q:'(?:[^'\\]|\\.)*'," % nm, lambda m: m.group(1) + 'def:' + js(d) + ',', w1h)
    assert k == 1, nm
dims = cut(sc, 'var DIMS=[', '\n];\n')
flams = flam_js('')
ARCH = [
    {'n': '2.1.1', 'fn': 'Strategic Alignment',
     'why': "Strategy fragments when leaders and functions interpret the organisation's ambition differently. Alignment creates a common strategic reference point while allowing different parts of the organisation to make the contributions required of them.",
     'si': "Creates shared understanding of the organisation's strategic ambition and the choices that define it. Leaders are anchored to the same WHAT, WHY, HOW and WHEN.",
     'sip': 'Creates a shared picture of what successful realisation of that ambition looks like. Functions may contribute differently, but they are working towards the same organisational reality.'},
    {'n': '2.1.2', 'fn': 'Decision Filter',
     'why': 'Organisations continuously face competing opportunities, investments, initiatives and demands. Without a common strategic filter, priorities can become shaped by urgency, functional interests or whoever has the strongest influence in the room.',
     'si': "Provides the reference point for determining whether a choice is consistent with the organisation's strategic ambition and the choices already made.",
     'sip': 'Tests whether that choice contributes to the conditions of success the organisation has defined. It connects individual decisions to the future reality they are expected to help create.'},
    {'n': '2.1.3', 'fn': 'Execution Coherence',
     'why': 'Strategy is delivered through many functions, teams and decisions acting together. Each part can perform well individually while the organisation still fails to produce the intended enterprise outcome. Coherence ensures those contributions connect.',
     'si': 'Provides the common strategic anchor that enables functions to interpret their mandates and choices in relation to the enterprise ambition.',
     'sip': 'Shows what those combined contributions must produce across <strong>customer value, operational capability, people and culture, and enterprise value</strong>. It allows functions to see beyond their individual outputs to the organisational outcome they collectively enable.'},
]
SUMMARY = [
    {'arc': 'Awareness — What', 't': 'What Was Established', 'body': 'Strategy was defined precisely: the output of iterative thinking, logic and process to determine what, why, how and when an organisation creates, delivers and sustains value to its stakeholders while navigating the forces within its operating environment. Each concept in the definition is part of the Strategy Architecture: the interconnected choices and logic that sit underneath a strategy. The Strategy Intent Statement brings forward four dimensions from that architecture (WHAT, WHY, HOW and WHEN) and crystallises them into one clear statement. Success in Practice (SiP) defines what must be seen, experienced and executed for that ambition to become reality, across four observable domains: Customer Experience & Value, Operational Capability & Execution Rhythm, People & Culture Dynamics, and Enterprise Value Creation.'},
    {'arc': 'Intelligence — Why', 't': 'Why It Matters', 'body': 'The Strategy Intent and SiP become useful when they shape how the organisation aligns, makes choices and executes. They serve three functions. Strategic Alignment keeps people and functions oriented around the same ambition and picture of success. The Decision Filter gives a basis for determining which choices, opportunities and investments support the strategy: the Strategy Intent tests strategic fit and SiP tests strategic contribution. Execution Coherence helps functions understand how their individual contributions connect to produce the enterprise outcome.'},
    {'arc': 'Extrapolating — Where', 't': 'Where Success Shows Up', 'body': 'Each SiP domain was examined through observable indicators in two positions: When Working and Signal of Absence. The indicators help leaders test, deepen and make observable the success they have defined. The SiP Flammables provide the balance test: they show when one legitimate perspective has become so dominant that the enterprise picture narrows into a functional one. Two disciplines result: depth within each SiP domain and balance across all four.'},
    {'arc': 'Integration — Collective', 't': 'What Was Built', 'body': 'Each group built three connected outputs in sequence. The Strategy Architecture: the integrated strategic logic constructed from the 14 elements. The Strategy Intent Statement: the crisp expression of the organisation\'s strategic ambition derived from WHAT, WHY, HOW and WHEN. Success in Practice: four confirmed statements describing what successful realisation of that ambition looks like across the organisation. The Architecture provides the logic. The Intent crystallises the ambition. Success in Practice makes the ambition observable.'},
    {'arc': 'Application — In Practice', 't': 'What Was Applied', 'body': 'Each participant applied the agreed Success in Practice to an assigned executive role and defined, in the present tense of the future, what that role must contribute across the four SiP domains. Each group then shared its SiP statement and explained how the role contributions support it. The group examined alignment, gaps, tensions and the areas where the SiP statement needs clearer execution ownership. The three outputs are the strategic foundation that later S2R® work carries into alignment, execution and performance.'},
]
def js_arr(name, arr):
    return 'var %s=[\n' % name + ',\n'.join('  ' + js(x) for x in arr) + '\n];\n'

r_concepts = cut(sc, 'function renderConcepts(){', '\n}\n')
r_w1h = rep(cut(sc, 'function renderW1H(){', '\n}\n'), "<h5>Core Question</h5><p>'+w.q+'</p>", "<h5>What It Brings Forward</h5><p>'+w.def+'</p>")
r_dims = cut(sc, 'function renderDims(){', '\n}\n')
r_flam = flam_render('renderFlam', 'flamList', 'flam_', ' cols2')
r_sum = cut(sc, 'function renderSummary(){', '\n}\n')
helpers = cut(sc, '// ── GENERIC HELPERS ──', "window.scrollTo({top:0,behavior:'smooth'});\n}\n")
r_arch = '''function renderArch(){
  var el=document.getElementById('archList');if(!el)return;
  el.innerHTML='<p>Strategy Intent and SiP serve three functions within the Strategy2Results® architecture. Click each to expand.</p>'+
  ARCH.map(function(a,i){
    return '<div class="sub-acc" id="arch_'+i+'">'+
      '<div class="sub-acc-h" onclick="tSA(this)">'+
        '<span style="font-family:\\'Cormorant Garamond\\',serif;font-size:1.1rem;font-weight:400;color:#fff;">'+a.n+' — '+a.fn+'</span>'+
        '<span class="sub-arr">▼</span>'+
      '</div>'+
      '<div class="sub-acc-b cols2">'+
        '<div class="u2-why">'+
          '<p class="u2-lbl" style="color:rgba(255,255,255,.4);">Why It Matters</p>'+
          '<p class="u2-txt">'+a.why+'</p>'+
        '</div>'+
        '<div>'+
          '<p class="u2-lbl" style="color:rgba(201,168,76,.6);">Strategy Intent</p>'+
          '<p class="u2-txt">'+a.si+'</p>'+
        '</div>'+
        '<div>'+
          '<p class="u2-lbl" style="color:rgba(46,168,122,.6);">Success in Practice (SiP)</p>'+
          '<p class="u2-txt">'+a.sip+'</p>'+
        '</div>'+
      '</div>'+
    '</div>';
  }).join('');
}
'''
footer = sc[once(sc, '<footer class="ibsl-legal"'):]
script_new = ('<script>\n// ── DATA ──────────────────────────────────────────────────────────────────────\n'
    + concepts + '\n' + w1h + '\n' + js_arr('ARCH', ARCH) + '\n' + dims + '\n' + flams + '\n' + js_arr('SUMMARY', SUMMARY) + '\n'
    + '// ── RENDER ────────────────────────────────────────────────────────────────────\n'
    + r_concepts + '\n' + r_w1h + '\n' + r_arch + '\n' + r_dims + '\n' + r_flam + '\n' + r_sum + '\n'
    + helpers + '\n'
    + "document.body.style.overflow='';\nrenderConcepts();renderW1H();renderArch();renderDims();renderFlam();\nrenderSummary();\n\n</script>\n" + footer)

new = head + guide + sec1 + '\n' + sec2 + '\n' + sec3 + '\n' + sec4 + sec5 + script_new
# Carol, 5 Oct: no times anywhere in the facilitator file (these three sit inside blocks carried over from the old file)
n0 = len(new)
new, k1 = re.subn(r'<p><em>Suggested (?:section |total section )?time: [^<]*</em></p>', '', new)
new, k2 = re.subn(r' Allow 3–4 minutes of individual reading\.', '', new)
assert k1 == 4 and k2 == 1, (k1, k2)
assert not re.search(r'(?i)suggested (section |total section )?time|\bminutes?\b|\bmin\)', re.sub(r'<script.*?</script>|<style.*?</style>', '', new, flags=re.S)), 'a time is still in the file'
# Carol, 5 Oct (night): the facilitator teaches the whole unit from the deck first; participants go to the portal afterwards.
# Guidance lines that had the facilitator steer participants through the page while teaching are reworded.
for a, b in [
    ('<strong>Directing participants through the 9 concepts:</strong> Ask participants to expand each concept card individually and read it before moving to the next. Then ask:',
     '<strong>Taking participants through the 9 concepts:</strong> Take the concepts one at a time: what each one means, its strategic implication and what fails when it is missing. Then ask:'),
    ('<strong>Before opening the tabs:</strong> Ask participants to rate their organisation on each dimension privately (1–5) before exploring the content.',
     '<strong>Before presenting the four dimensions:</strong> Ask participants to rate their organisation on each dimension privately (1–5) before exploring the content.'),
    ('<strong>Directing through the 4 dimension tabs:</strong> Walk through WHAT, WHY, HOW, WHEN one at a time as a group. For each, ask one diagnostic question from the content and take 2–3 responses. The HOW and WHEN tabs typically reveal the most significant gaps — give them additional time.',
     '<strong>Taking participants through the 4 dimensions:</strong> Walk through WHAT, WHY, HOW, WHEN one at a time as a group. For each, ask one diagnostic question from the content and take 2–3 responses. HOW and WHEN typically reveal the most significant gaps — give them additional time.'),
    ('<strong>HOW tab — key facilitation moment:</strong>', '<strong>HOW — key facilitation moment:</strong>'),
    ('<strong>WHEN tab:</strong>', '<strong>WHEN:</strong>'),
    ('<strong>Closing the unit:</strong> Expand the summary accordion and read each of the five blocks aloud, or ask participants to read them in turn.',
     '<strong>Closing the unit:</strong> Read each of the five summary blocks aloud, or ask participants to read them in turn.'),
]:
    assert new.count(a) == 1, (a[:60], new.count(a))
    new = new.replace(a, b)
# Carol, 5 Oct (late night): the private 1-to-5 rating is no longer part of the unit ("We have removed it from the files").
# The participant file has no rating; this guidance line was the last trace of it.
RATING = '<p><strong>Before presenting the four dimensions:</strong> Ask participants to rate their organisation on each dimension privately (1–5) before exploring the content. This creates a diagnostic baseline.</p>'
assert new.count(RATING) == 1, new.count(RATING)
new = new.replace(RATING, '')
assert not re.search(r'(?i)\brate their\b|\(1–5\)|diagnostic baseline', new)
write(OUT, new)
print('facilitator file written:', len(new), 'chars')
