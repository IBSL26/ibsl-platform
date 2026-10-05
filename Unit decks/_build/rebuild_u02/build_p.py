# -*- coding: utf-8 -*-
"""Rebuild of unit2_m1_lens1_p.html from Carol's 'Unit 2 Rebuild _2026_10_05.docx' (participant, "you" voice)."""
import sys, re
from common import *

SRC, OUT = sys.argv[1], sys.argv[2]
o = read(SRC)

def P(*paras): return ''.join('  <p>%s</p>\n' % p for p in paras)
def ref(id_, topic, prompt, cls='ref-ta reflection-textarea', save='saveRef', style=' style="margin-top:14px;"', ph='Write your reflection here...'):
    return ('  <div class="ref-block"%s>\n'
            '    <div class="ref-head"><span class="ref-icon">✍</span><span class="ref-label">&#x270E; Reflection &mdash; %s</span></div>\n'
            '    <div class="ref-prompt">%s</div>\n'
            '    <textarea class="%s" id="%s" placeholder="%s"></textarea>\n'
            '    <button class="ref-save" onclick="%s(\'%s\')">Save Reflection</button>\n'
            '    <div class="ref-saved" id="%s-saved">✓ Saved</div>\n'
            '  </div>\n') % (style, topic, prompt, cls, id_, ph, save, id_, id_)
def field(id_, lbl, desc, ph, color=None, min_h=None, ind='  '):
    s = ind + '<div class="port-block">\n'
    s += ind + '  <div class="port-head"><div class="port-lbl"%s>%s</div><div class="port-desc">%s</div></div>\n' % (' style="color:%s;"' % color if color else '', lbl, desc)
    s += ind + '  <textarea class="port-ta" id="%s" placeholder="%s"%s></textarea>\n' % (id_, ph, ' style="min-height:%dpx;"' % min_h if min_h else '')
    s += ind + '  <button class="port-save" onclick="saveField(\'%s\')">Save</button>\n' % id_
    s += ind + '  <div class="port-msg" id="%s-msg">✓ Saved</div>\n' % id_
    s += ind + '</div>\n'
    return s
def mirror(key, empty):
    return '<div class="u2-mirror empty" data-mirror="%s" data-empty="%s">%s</div>' % (key, empty, empty)

# ════════ HEAD ════════
head = o[:once(o, '<div class="mod-panel active" id="mod0">')]
head = rep(head, OLD_KLO1, '<span class="klo">%s</span>' % KLO1)
head = rep(head,
    '<p class="unit-desc">This unit builds the master definition of strategy and the 3W1H framework, and produces a Success in Practice (SiP) statement — a Headline and a Storyline — through collective executive co-creation.</p>',
    '<p class="unit-desc">This unit helps you to determine your organisation&rsquo;s strategy architecture, articulate its strategic intent and define the Success in Practice (SiP) of the chosen Strategy Intent.</p>')
P_CSS = NEW_CSS.replace('var(--ACC)', 'var(--teal)') + '''.u2-mirror{background:#0a1a0d;border:1px dashed rgba(26,122,106,.4);border-radius:3px;padding:10px 14px;margin-top:6px;font-size:12px;color:rgba(255,255,255,.78);line-height:1.65;white-space:pre-wrap;}
.u2-mirror.empty{color:rgba(255,255,255,.3);font-style:italic;}
.u2-mirror-lbl{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.35);margin-top:12px;}
.u2-out{margin:12px 0;padding:14px 16px;background:#151c15;border:1px solid rgba(26,122,106,.2);border-radius:3px;}
.u2-out-h{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--teal);margin-bottom:2px;}
.u2-out-d{font-size:11px;color:rgba(255,255,255,.45);line-height:1.6;}
.u2-meta{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:16px 0 6px;}
.u2-inlbl{display:block;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--teal);margin-bottom:6px;}
.u2-in{width:100%;background:#0a1a0d;border:1px solid rgba(26,122,106,.25);border-radius:3px;padding:10px 12px;color:rgba(255,255,255,.8);font-size:13px;font-family:'Montserrat',sans-serif;outline:none;}
.u2-in::placeholder{color:rgba(255,255,255,.2);}
.u2-progress{margin:16px 0 10px;}
.u2-progress-top{display:flex;justify-content:space-between;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.45);margin-bottom:6px;}
.u2-progress-top b{color:var(--gold);}
.u2-bar{height:5px;background:rgba(255,255,255,.08);border-radius:5px;overflow:hidden;}
.u2-bar span{display:block;height:100%;width:0;background:var(--gold);transition:width .3s;}
.u2-chips{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0 14px;}
.u2-chip{display:flex;align-items:center;gap:7px;padding:6px 11px 6px 6px;border-radius:16px;border:1px solid rgba(255,255,255,.1);background:transparent;color:rgba(255,255,255,.5);font-family:'Montserrat',sans-serif;font-size:10px;font-weight:700;letter-spacing:.5px;cursor:pointer;transition:all .15s;}
.u2-chip:hover{border-color:rgba(26,122,106,.5);color:#fff;}
.u2-chip.active{border-color:var(--gold);color:#fff;background:rgba(201,168,76,.08);}
.u2-chip-n{width:20px;height:20px;border-radius:50%;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;font-size:10px;}
.u2-chip.done .u2-chip-n{background:#1a7a6a;color:#fff;}
.u2-el-name{font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:#fff;margin:2px 0 0;}
.u2-el-tag{font-size:12px;font-weight:700;color:var(--gold);margin-bottom:8px;}
.u2-el-body{padding:6px 16px 14px;}
.u2-q{display:block;font-size:12px;font-weight:600;color:rgba(255,255,255,.8);margin:14px 0 6px;line-height:1.5;}
.u2-ans,.u2-sipin{border:1px solid rgba(26,122,106,.2)!important;border-radius:3px;background:#111811!important;}
.u2-sipin{min-height:64px;}
.u2-btnrow{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;}
.u2-btnrow.u2-pad{padding:0 16px 14px;}
.u2-b{padding:8px 14px;border-radius:2px;border:1px solid rgba(255,255,255,.18);background:transparent;color:rgba(255,255,255,.75);font-family:'Montserrat',sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;transition:all .15s;}
.u2-b:hover{border-color:var(--gold);color:var(--gold);}
.u2-b.ok{background:#1a7a6a;border-color:#1a7a6a;color:#fff;}
.u2-gen{background:rgba(201,168,76,.07);border:1px solid rgba(201,168,76,.25);border-left:4px solid var(--gold);border-radius:3px;padding:16px 18px;margin-top:16px;}
.u2-sipd .u2-gen{margin:0 16px 14px;}
.u2-sipd .u2-ref-ta{min-height:130px;}
.u2-gen-lbl{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);}
.u2-gen-h{font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:#fff;margin:6px 0 8px;}
.u2-gen-txt{font-size:13px;color:rgba(255,255,255,.8);line-height:1.7;white-space:pre-line;margin:0;}
.u2-pill{font-size:8px;letter-spacing:1.5px;padding:3px 8px;border-radius:10px;background:#1a7a6a;color:#fff;margin-left:8px;vertical-align:middle;}
.u2-ref-ta{width:100%;min-height:84px;margin-top:10px;background:#111811;border:1px solid rgba(201,168,76,.3);border-radius:3px;padding:10px 12px;color:rgba(255,255,255,.85);font-size:13px;line-height:1.6;font-family:'Montserrat',sans-serif;resize:vertical;outline:none;}
.u2-locked{border:1px dashed rgba(255,255,255,.2);background:rgba(255,255,255,.03);border-radius:3px;padding:14px 16px;font-size:12px;color:rgba(255,255,255,.5);margin:12px 0;}
.u2-ok{font-size:12px;font-weight:700;color:#5ecba1;margin:12px 0 0;}
.u2-note{font-size:12px;color:var(--gold);margin-top:10px;}
.u2-elnav{display:flex;justify-content:space-between;margin:12px 0 6px;}
.u2-elnav .btn[disabled]{opacity:.35;cursor:default;}
.u2-src{margin:6px 0 0;padding-left:18px;}
.u2-src li{font-size:12px;color:rgba(255,255,255,.75);line-height:1.6;margin-bottom:5px;}
.u2-sipgrid{align-items:start;}
.u2-final{padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06);}
.u2-final:last-child{border-bottom:none;}
.u2-final-h{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:5px;}
.u2-final-t{font-size:13px;color:rgba(255,255,255,.82);line-height:1.7;white-space:pre-wrap;}
.u2-pad.u2-note{padding:0 16px 12px;margin-top:0;}
@media(max-width:700px){.u2-meta{grid-template-columns:1fr;}}
'''
i = head.index('</style>')
head = head[:i] + P_CSS + head[i:]

# ════════ SECTION 1 ════════
quote_def = line_with(o, '<div class="quote"><p>"Strategy is the output of iterative thinking, logic and process')
b11 = P('Before you can express strategy clearly, you need to understand what sits underneath it. This is the <strong>Strategy Architecture</strong>: the interconnected choices and logic that determine what your organisation will do, why, how and when; how it will create, deliver and sustain value; for whom; and within what environment.',
        'A strategy can sound compelling while important parts of its underlying logic remain weak, disconnected or undefined. In the S2R® framework, strategy has a specific applied definition. Every word carries strategic weight, and each concept in it is part of the architecture.') \
    + quote_def + '\n' \
    + P('As you work through the concepts, consider how well defined each part of your organisation\'s strategy architecture is today.') \
    + '  <div id="conceptListP"></div>\n' \
    + ref('ref1', 'Strategy Architecture', 'Which part of your organisation\'s strategy architecture is least well defined today? What is the consequence?', style=' style="margin-top:18px;"')

w1h_tabs = cut(o, '  <div class="ph-tabs" id="w1hTabsP">', '<div id="w1hPanelsP"></div>')
ref2_prompt = cut(o, '<div class="ref-prompt">From your assigned executive leader perspective: which dimension', '</div>')
ref2_prompt = ref2_prompt[len('<div class="ref-prompt">'):-len('</div>')]
b12 = P('Your Strategy Architecture is the foundation from which the Strategy Intent Statement is derived. It establishes your organisation\'s strategic choices and the logic connecting them.',
        'The Strategy Intent Statement brings forward four dimensions from that architecture. Select each one.') \
    + w1h_tabs + '\n' \
    + '  <p style="margin-top:16px;">You then crystallise these four dimensions into one clear Strategy Intent Statement.</p>\n' \
    + P('The strength of the statement comes from the architecture beneath it. Keep it crisp, directional and easy to express. Your Strategy Architecture holds the depth and the supporting logic.') \
    + '  <div class="hbox teal"><p>The resulting Strategy Intent becomes your organisation\'s directional anchor for strategic choices, alignment and execution.</p></div>\n' \
    + ref('ref2', 'Strategy Intent', ref2_prompt)

def dom_grid(descs, extra=None):
    return '  <div class="u2-grid">\n' + ''.join(
        '    <div class="u2-card"><div class="u2-card-h" style="color:%s;">D%d · %s</div><p>%s</p>%s</div>\n' % (DOM_COL[i], i + 1, DOM[i], descs[i], extra(i) if extra else '')
        for i in range(4)) + '  </div>\n'
b13 = P('Your Strategy Intent Statement establishes the ambition. Success in Practice defines what must be seen, experienced and executed for that ambition to become reality within a given time horizon. Defining this together gives you and your leadership team a shared picture of success, and reduces the risk of different functions interpreting the same strategic intent differently.',
        'Stand inside the future created by your Strategy Intent. Imagine that the intent has been successfully realised and describe the organisational reality you can observe.') \
    + '  <div class="quote"><p>"If our Strategy Intent is successful, what should we see in practice?"</p></div>\n' \
    + P('Success is considered across four observable domains:') \
    + dom_grid(['What your customers and other value recipients experience when the strategic intent is working.',
                'How your organisation operates, coordinates, delivers and adapts when the capabilities required by the intent are functioning effectively.',
                'How people understand the strategic intent, make decisions, collaborate, take ownership and behave when the intent is embedded in your organisation.',
                'How your organisation benefits across its measures of enterprise success.']) \
    + P('Together, the four domains give you a shared organisational picture of success against which you align decisions, trade-offs and execution.') \
    + '  <div class="hbox teal"><p><strong>Stay with observable reality.</strong> Your SiP describes what is happening when the strategy is working. Initiatives, projects and activities stay out of it.</p></div>\n'

# Carol, 5 Oct (night): the opening exercise has a box on the participant page. Her sentence, word for word.
OPENING_P = ('<div class="port-block" style="margin:0 0 22px;">\n'
    '  <div class="port-head"><div class="port-lbl">Opening the Session — Your Definition of Strategy</div>'
    '<div class="port-desc">Write your definition of strategy in one sentence — right now, without consulting anyone.</div></div>\n'
    '  <textarea class="port-ta" id="strategy_definition" placeholder="Write your one-sentence definition here..."></textarea>\n'
    '  <button class="port-save" onclick="saveField(\'strategy_definition\')">Save</button>\n'
    '  <div class="port-msg" id="strategy_definition-msg">✓ Saved</div>\n'
    '</div>\n')
sec1 = ('<div class="mod-panel active" id="mod0">\n' + hero(1) + '<div class="mod-body">\n' + slo(1) + '\n\n' + OPENING_P + '\n'
        + acc(*TITLES['1.1'], b11, True) + '\n' + acc(*TITLES['1.2'], b12) + '\n' + acc(*TITLES['1.3'], b13) + '\n'
        + '<div class="mod-nav"><button class="btn" onclick="showMod(1)">Section 2 — Intelligence →</button></div>\n</div>\n</div>\n')

# ════════ SECTION 2 ════════
FUNCS = [
    ('2.1.1', 'Strategic Alignment',
     'Strategy fragments when you and other leaders interpret the organisation\'s ambition differently. Alignment creates a common strategic reference point while allowing each part of the organisation to make the contribution required of it.',
     'Creates shared understanding of your organisation\'s strategic ambition and the choices that define it. You and your fellow leaders are anchored to the same WHAT, WHY, HOW and WHEN.',
     'Creates a shared picture of what successful realisation of that ambition looks like. Functions may contribute differently, but you are all working towards the same organisational reality.'),
    ('2.1.2', 'Decision Filter',
     'Your organisation continuously faces competing opportunities, investments, initiatives and demands. Without a common strategic filter, priorities become shaped by urgency, functional interests or whoever has the strongest influence in the room.',
     'Gives you the reference point for determining whether a choice is consistent with your organisation\'s strategic ambition and the choices already made.',
     'Tests whether that choice contributes to the conditions of success you have defined. It connects each decision to the future reality it is expected to help create.'),
    ('2.1.3', 'Execution Coherence',
     'Strategy is delivered through many functions, teams and decisions acting together. Your function can perform well on its own while the organisation still fails to produce the intended enterprise outcome. Coherence ensures the contributions connect.',
     'Gives you the common strategic anchor for interpreting your mandate and your choices in relation to the enterprise ambition.',
     'Shows what the combined contributions must produce across <strong>customer value, operational capability, people and culture, and enterprise value</strong>. It lets you see beyond your own outputs to the organisational outcome you collectively enable.'),
]
funcs_html = ''
for n, fn, why, si, sip in FUNCS:
    funcs_html += ('  <div class="sub-acc"><div class="sub-acc-h" onclick="tSA(this)"><span style="font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;font-weight:400;color:#fff;">%s — %s</span><span class="sub-arr">▼</span></div>'
                   '<div class="sub-acc-b cols2">'
                   '<div class="u2-why"><p class="u2-lbl" style="color:rgba(255,255,255,.4);">Why It Matters</p><p class="u2-txt">%s</p></div>'
                   '<div><p class="u2-lbl" style="color:rgba(201,168,76,.6);">Strategy Intent</p><p class="u2-txt">%s</p></div>'
                   '<div><p class="u2-lbl" style="color:rgba(46,168,122,.6);">Success in Practice (SiP)</p><p class="u2-txt">%s</p></div>'
                   '</div></div>\n') % (n, fn, why, si, sip)
b21 = P('Your Strategy Intent and your SiP become useful when they begin to shape how your organisation <strong>aligns, makes choices and executes</strong>.',
        'Once you and your leadership team have established a shared strategic ambition and defined what success looks like in practice, those two outputs become common reference points across the organisation. They serve three functions within the Strategy2Results® architecture. Click each to expand.') \
    + funcs_html \
    + '  <div class="hbox teal"><p><strong>How they work together:</strong> The Intent anchors the ambition and the strategic choices. SiP anchors the organisational reality those choices are intended to produce. When a new initiative, investment or opportunity appears, the Strategy Intent gives you the test of <strong>strategic fit</strong> and SiP gives you the test of <strong>strategic contribution</strong>: whether the choice moves your organisation closer to the success it has defined.</p></div>\n' \
    + ref('ref6', 'Three Functions', 'Which of the three functions is weakest in your organisation today? What happens as a result?', style='')
sec2 = ('<!-- ═══ TAB 2: INTELLIGENCE ═══ -->\n<div class="mod-panel" id="mod1">\n' + hero(2) + '<div class="mod-body">\n' + slo(2) + '\n\n'
        + acc(*TITLES['2.1'], b21, True) + '\n'
        + '<div class="mod-nav">\n  <button class="btn" onclick="showMod(0)">← Section 1 — Awareness</button>\n  <button class="btn" onclick="showMod(2)">Section 3 — Extrapolating →</button>\n</div>\n</div>\n</div>\n')

# ════════ SECTION 3 ════════
dim_tabs = cut(o, '  <div class="dim-tabs" id="dimTabsP">', '<div id="dimPanelsP"></div>')
b31 = P('Each SiP domain is examined through a set of <strong>observable indicators</strong>. They help you move from a broad description of success to the specific conditions through which that success becomes visible in your organisation.',
        'For every indicator, examine two positions. <strong>When Working</strong> describes what you expect to observe when that aspect of the SiP is functioning effectively. <strong>Signal of Absence</strong> describes what may become visible when that condition is weak, missing or disconnected from the Strategy Intent.',
        'Use both positions. Sometimes the absence of a condition gives you the clearest evidence of why it matters.') \
    + dim_tabs + '\n' \
    + ref('ref4', 'SiP Indicators', 'From your assigned executive leader role: which SiP domain shows the most significant gaps in your organisation right now? What is the primary cause?')
b32 = P('The four SiP domains describe <strong>one organisational reality</strong>. You and your fellow leaders bring different perspectives into the conversation: a commercial leader may see success through customers and growth, an operations leader through efficiency, process and delivery, a people leader through culture and capability, a finance leader through financial and enterprise outcomes.',
        'Each perspective contributes something important. The strategic risk emerges when one perspective becomes so dominant that it begins to define success for the entire organisation.',
        'The SiP Flammables are your balance test. They help you recognise when a legitimate dimension of success has become disproportionately influential and the enterprise picture has narrowed into a functional one. Each pattern below shows what the imbalance creates, the indicators that reveal it and the strategic risk if it is left unbalanced.') \
    + '  <div id="flamListP"></div>\n'
sec3 = ('<!-- ═══ TAB 3: EXTRAPOLATING ═══ -->\n<div class="mod-panel" id="mod2">\n' + hero(3) + '<div class="mod-body">\n' + slo(3) + '\n\n'
        + acc(*TITLES['3.1'], b31, True) + '\n' + acc(*TITLES['3.2'], b32) + '\n'
        + '<div class="mod-nav">\n  <button class="btn" onclick="showMod(1)">← Section 2 — Intelligence</button>\n  <button class="btn" onclick="showMod(3)">Section 4 — Integration →</button>\n</div>\n</div>\n</div>\n')

# ════════ SECTION 4 ════════
exec(open('sec4_p.py', encoding='utf-8').read())

sec4 = ('<!-- ═══ TAB 4: INTEGRATION ═══ -->\n<div class="mod-panel" id="mod3">\n'
        + hero(4, 'Work with your group through three connected stages. Each output is the foundation for the next: Strategy Architecture → Strategy Intent → Success in Practice.')
        + '<div class="mod-body">\n' + slo(4) + '\n\n'
        + acc(*TITLES['4.1'], b41, True, 'STEP 1: STRATEGY ARCHITECTURE') + '\n'
        + acc(*TITLES['4.2'], b42, False, 'STEP 2: STRATEGY INTENT STATEMENT') + '\n'
        + acc(*TITLES['4.3'], b43, False, 'STEP 3: SUCCESS IN PRACTICE') + '\n'
        + '<div class="mod-nav"><button class="btn" onclick="showMod(2)">← Section 3 — Extrapolating</button><button class="btn" onclick="showMod(4)">Section 5 — Application →</button></div>\n</div>\n</div>\n')

# ════════ SECTION 5 ════════
role_block = cut(o, '  <div class="sip-role-wrap">\n    <div class="sip-role-label">Select Your Assigned Role</div>\n    <div class="sip-role-select" id="appRoleSelP"></div>', '<div class="sip-save-msg" id="appSaveMsgP">✓ SiP Application saved.</div>\n  </div>')
role_block = rep(role_block, 'Save My SiP Application', 'Save My Role Contribution')
role_block = rep(role_block, '✓ SiP Application saved.', '✓ Role Contribution saved.')
b51 = P('In Section 4 your group produced Strategy Architecture → Strategy Intent → Success in Practice. Success is already defined. Your work here is to apply it from your executive role.') \
    + '  <div class="quote"><p>"From my executive role, what must I contribute for this Success in Practice to become real?"</p></div>\n' \
    + '  <h4>Your Group\'s Four SiP Statements</h4>\n' + sip_mirrors() \
    + P('Select your assigned executive role and complete the table from that role\'s perspective. Write in the <strong>present tense of the future</strong>, as if the strategy is already working: "Customers experience…", "Operations are able to…", "People consistently…", "The organisation creates value through…".') \
    + '  <div class="hbox"><p><strong>Be practical and role-specific.</strong> General statements such as "Support the strategy", "Improve communication", "Collaborate better" or "Drive performance" say too little. Ask: <em>"What does this role specifically decide, enable, coordinate, resource, protect or change?"</em></p></div>\n' \
    + role_block + '\n' \
    + '  <p style="margin-top:14px;">When your row is complete, check it: does your contribution strengthen all four SiP domains, or does it reflect only the priorities of your own function?</p>\n'

LISTEN = [('col_alignment', 'Alignment', 'Where do the role contributions support the SiP statement and one another?', 'Record where the contributions align...'),
          ('col_gaps', 'Gaps', 'Which part of the SiP statement has no role contributing to it?', 'Record the gaps you observe...'),
          ('col_tensions', 'Tensions', 'Where do role contributions pull against one another?', 'Record the tensions you observe...'),
          ('col_ownership', 'Execution Ownership', 'Where does the SiP statement need clearer execution ownership?', 'Record where ownership needs to be clearer...')]
ref_final_prompt = cut(o, '<div class="ref-prompt">Having completed the full application exercise', '</div>')[len('<div class="ref-prompt">'):-len('</div>')]
b52 = P('When every role has completed its row, your group shares its SiP statement and explains how the different role contributions support it. You examine how the strategy becomes practical through leadership contribution.',
        'As groups share, record what you observe under the four headings below.') \
    + '  <div class="u2-grid">\n' + ''.join(field(k, l, d, ph, color=DOM_COL[i], ind='    ') for i, (k, l, d, ph) in enumerate(LISTEN)) + '  </div>\n' \
    + '  <div class="hbox teal"><p>The focus: can the agreed SiP be supported by practical leadership contribution across the executive team?</p></div>\n' \
    + ref('app_ref_final', 'Application', ref_final_prompt, cls='ref-ta', save='saveApp', style=' style="margin-top:6px;"', ph='Write your final integration reflection here...')

tail = o[once(o, '<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">Unit Summary</span>'):once(o, '<script>\n// ── DATA (shared with fac version)')]
assert 'Portfolio Artefact' not in tail and 'port1' not in tail

sec5 = ('\n\n<div class="mod-panel" id="mod4">\n'
        + hero(5, 'Apply your group\'s agreed Success in Practice to your executive role and define what that role must contribute to make the Strategy Intent real.')
        + '<div class="mod-body">\n' + slo(5) + '\n\n'
        + acc(*TITLES['5.1'], b51, True, 'ROLE CONTRIBUTION') + '\n'
        + acc(*TITLES['5.2'], b52, False, 'COLLECTIVE APPLICATION') + '\n' + tail)

# ════════ SCRIPT ════════
sc_all = o[once(o, '<script>\n// ── DATA (shared with fac version)'):]
k = once(sc_all, '// ══════════════════════════════════════════════════════════════════════════════\n// COMPONENT 1 — FACILITATOR FEEDBACK DISPLAY')
sc, rest = sc_all[:k], sc_all[k:]

concepts = cut(sc, 'var CONCEPTS=[', '\n];\n')
w1h = cut(sc, 'var W1H=[', '\n];\n')
for nm, d in zip(W, W_DEF[:3] + ['The timing, sequencing and strategic moves through which the ambition will be pursued.']):
    w1h, n_ = re.subn(r"(\{name:'%s',sub:'[^']*',)q:'(?:[^'\\]|\\.)*'," % nm, lambda m: m.group(1) + 'def:' + js(d) + ',', w1h)
    assert n_ == 1, nm
dims = cut(sc, 'var DIMS=[', '\n];\n')
flams = flam_js('')
r_concepts = cut(sc, 'function renderConcepts(){', '\n}\n')
r_w1h = rep(cut(sc, 'function renderW1H(){', '\n}\n'), "<h5>Core Question</h5><p>'+w.q+'</p>", "<h5>What It Brings Forward</h5><p>'+w.def+'</p>")
r_dims = cut(sc, 'function renderDimsP(){', '\n}\n')
r_flam = flam_render('renderFlamP', 'flamListP', 'flamP_', '')
r_sum = cut(sc, 'function renderSummaryP(){', "function tSumP(i){document.getElementById('sumP_'+i).classList.toggle('open');}\n")
nav = cut(sc, 'function goBack(){', "window.scrollTo({top:0,behavior:'smooth'});\n}\n")
nav = rep(nav, "function showPhP(prefix,i){", "function showEl(i){\n  document.querySelectorAll('#elTabsP .ag-tab').forEach(function(t,x){t.classList.toggle('active',x===i);});\n  document.querySelectorAll('#elPanelsP .ag-panel').forEach(function(p,x){p.classList.toggle('active',x===i);});\n}\nfunction showPhP(prefix,i){")
s_ref = cut(sc, 'async function saveRef(id){', '\n}\n')
send = rep(cut(sc, 'async function sendToFacilitator(){', '\n}\n'), '  saveCurSIPP();\n', '')
app_vars = cut(sc, "var appRoleP='';", 'var appResponsesP={};\n')
s_app = cut(sc, 'async function saveApp(id){', '\n}\n')
r_roles = cut(sc, 'function renderAppRoleSel(){', '\n}\n')
r_form = cut(sc, 'function renderAppForm(){', '\n}\n')
r_form = rep(r_form, 'Select your assigned role above to begin your SiP Application.', 'Select your assigned role above to begin your Role Contribution.')
r_form = rep(r_form, 'Write in the present tense of the future — as if the strategy has already succeeded...', 'Write in the present tense of the future, as if the strategy is already working...')
s_appsip = cut(sc, 'async function saveAppSIP(){', '\n}\n')

SUMMARY = [
    {'arc': 'Awareness — What', 't': 'What Was Established', 'body': 'Strategy was defined precisely: the output of iterative thinking, logic and process to determine what, why, how and when an organisation creates, delivers and sustains value to its stakeholders while navigating the forces within its operating environment. Each concept in the definition is part of the Strategy Architecture: the interconnected choices and logic that sit underneath a strategy. The Strategy Intent Statement brings forward four dimensions from that architecture (WHAT, WHY, HOW and WHEN) and crystallises them into one clear statement. Success in Practice (SiP) defines what must be seen, experienced and executed for that ambition to become reality, across four observable domains: Customer Experience & Value, Operational Capability & Execution Rhythm, People & Culture Dynamics, and Enterprise Value Creation.'},
    {'arc': 'Intelligence — Why', 't': 'Why It Matters', 'body': 'Your Strategy Intent and your SiP become useful when they shape how your organisation aligns, makes choices and executes. They serve three functions. Strategic Alignment keeps you and your fellow leaders oriented around the same ambition and picture of success. The Decision Filter gives you a basis for determining which choices, opportunities and investments support the strategy: the Strategy Intent tests strategic fit and SiP tests strategic contribution. Execution Coherence helps you see how your function\'s contribution connects with the others to produce the enterprise outcome.'},
    {'arc': 'Extrapolating — Where', 't': 'Where Success Shows Up', 'body': 'You examined each SiP domain through observable indicators in two positions: When Working and Signal of Absence. The indicators help you test, deepen and make observable the success you have defined. The SiP Flammables gave you the balance test: they show when one legitimate perspective has become so dominant that the enterprise picture narrows into a functional one. Two disciplines result: depth within each SiP domain and balance across all four.'},
    {'arc': 'Integration — Collective', 't': 'What Was Built', 'body': 'With your group you built three connected outputs in sequence. Your Strategy Architecture: the integrated strategic logic constructed from the 14 elements. Your Strategy Intent Statement: the crisp expression of your organisation\'s strategic ambition derived from WHAT, WHY, HOW and WHEN. Your Success in Practice: four confirmed statements describing what successful realisation of that ambition looks like across the organisation. The Architecture provides the logic. The Intent crystallises the ambition. Success in Practice makes the ambition observable.'},
    {'arc': 'Application — In Practice', 't': 'What Was Applied', 'body': 'You applied the agreed Success in Practice to your assigned executive role and defined, in the present tense of the future, what that role must contribute across the four SiP domains. Your group then shared its SiP statement and explained how the role contributions support it. You recorded the alignment, the gaps, the tensions and the areas where the SiP statement needs clearer execution ownership. Your three outputs are the strategic foundation that later S2R® work carries into alignment, execution and performance.'},
]
APP_DIMS = [
    {'id': 'd1', 'label': 'Customer Experience & Value', 'color': '#8ab0e8', 'prompt': 'What does this role contribute so that customers and other value recipients experience what your SiP describes?'},
    {'id': 'd2', 'label': 'Operational Capability & Execution Rhythm', 'color': 'var(--gold)', 'prompt': 'What does this role contribute so that the organisation operates, coordinates, delivers and adapts as your SiP describes?'},
    {'id': 'd3', 'label': 'People & Culture Dynamics', 'color': '#5ecba1', 'prompt': 'What does this role contribute so that people understand the Strategy Intent, decide, collaborate, take ownership and behave as your SiP describes?'},
    {'id': 'd4', 'label': 'Enterprise Value Creation', 'color': '#c39de0', 'prompt': 'What does this role contribute so that the organisation benefits across its measures of enterprise success?'},
]
def js_arr(name, arr):
    return 'var %s=[\n' % name + ',\n'.join('  ' + js(x) for x in arr) + '\n];\n'
U2_FIELDS = ['strategy_definition', 'org_name', 'strategy_period'] + [x[0] for x in LISTEN]
u2_js = open('u2_tool.js', encoding='utf-8').read()
u2_js = u2_js.replace('__ELEMENTS__', '[\n' + ',\n'.join('  ' + js({'n': n, 'tag': t, 'guide': g, 'qs': q}) for n, t, g, q in ELEMENTS) + '\n]')
u2_js = u2_js.replace('__GROUPS__', js([[g, names] for g, names in ARCH_GROUPS]))
u2_js = u2_js.replace('__SIPD__', '[\n' + ',\n'.join('  ' + js({'t': t, 'lead': l, 'qs': q}) for t, l, q in SIP_DOMAINS) + '\n]')
u2_js = u2_js.replace('__FIELDS__', js(U2_FIELDS))
assert '__' not in u2_js.replace('__stale', '').replace('__sstale', ''), 'placeholder left'
load_js = '''// ── LOAD SAVED FROM SUPABASE ──────────────────────────────────────────────────
window.addEventListener('load',async function(){
  if(!window.S2R){console.warn('[unit2_m1_lens1_p] S2R helper not loaded');return;}
  try{
    var responses=await S2R.loadAll('u2m1_lens1');
    // Reflections
    ['ref1','ref2','ref4','ref6'].forEach(function(id){
      var ta=document.getElementById(id);
      if(ta&&responses[id]!==undefined&&responses[id]!==null)ta.value=responses[id];
    });
    // Section 4: Strategy Intent Design (14 elements, architecture, intent, SiP) and what the group has confirmed
    Object.keys(responses).forEach(function(k){
      if(/^(arch_|sip_d[1-4]_|intent_statement$)/.test(k)&&responses[k]!==null&&responses[k]!==undefined)U2.v[k]=responses[k];
    });
    if(Array.isArray(responses['confirmed_items']))U2.conf=responses['confirmed_items'].slice();
    // Organisation, strategy period and Section 5.2 observations
    U2_FIELDS.forEach(function(id){
      var el=document.getElementById(id);
      if(responses[id]!==undefined&&responses[id]!==null){U2.v[id]=responses[id];if(el)el.value=responses[id];}
    });
    u2RenderAll();
    // Section 5 single-value app_* fields
    ['app_ref_final'].forEach(function(id){
      var key='app_'+id;
      var v=responses[key];
      appResponsesP[key]=(v!==undefined&&v!==null)?v:'';
      var el=document.getElementById(id);
      if(el&&v!==undefined&&v!==null)el.value=v;
    });
    // Section 5.1 role contribution fields (appSIP_<role>_<domain>)
    Object.keys(responses).forEach(function(k){
      if(k.indexOf('appSIP_')===0)appResponsesP[k]=responses[k];
    });
    // Open the role the participant has already written for
    if(!appRoleP){
      APP_ROLES.some(function(r){
        return APP_DIMS.some(function(d){
          var v=appResponsesP['appSIP_'+r+'_'+d.id];
          if(v&&String(v).trim()){appRoleP=r;return true;}
          return false;
        });
      });
    }
    if(typeof renderAppRoleSel==='function')renderAppRoleSel();
    if(typeof renderAppForm==='function')renderAppForm();
  }catch(err){
    console.error('[unit2_m1_lens1_p] Failed to load responses:',err);
  }
  // Load facilitator feedback / messages / uploads if a submission exists
  if(window.S2R)loadSubmissionFeedback();
});
'''
script_new = ('<script>\n// ── DATA (shared with fac version) ────────────────────────────────────────────\n'
    + concepts + w1h + dims + flams + '\n'
    + '// ── RENDER ────────────────────────────────────────────────────────────────────\n'
    + r_concepts + '\n' + r_w1h + '\n' + r_dims + '\n' + r_flam + '\n'
    + js_arr('SUMMARY', SUMMARY) + '\n' + r_sum + '\n'
    + nav + s_ref + '\n' + u2_js + '\n' + send + '\n' + load_js + '\n'
    + '// ── INIT ──────────────────────────────────────────────────────────────────────\n'
    + 'renderConcepts();renderW1H();renderDimsP();renderFlamP();\nrenderSummaryP();u2RenderAll();\n\n'
    + '// ── SECTION 5.1: ROLE CONTRIBUTION TABLE ──────────────────────────────────\n'
    + "var APP_ROLES=['CEO','CFO','COO','CHRO','CTO','CMO','CCO','CPO','CRO','CSO'];\n"
    + js_arr('APP_DIMS', APP_DIMS) + app_vars + '\n' + s_app + '\n' + r_roles + '\n' + r_form + '\n' + s_appsip + '\n'
    + 'renderAppRoleSel();renderAppForm();\n\n')

new = head + sec1 + '\n' + sec2 + '\n' + sec3 + '\n' + sec4 + sec5 + script_new + rest
write(OUT, new)
print('participant file written:', len(new), 'chars')
