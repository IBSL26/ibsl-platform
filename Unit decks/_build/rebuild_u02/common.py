# -*- coding: utf-8 -*-
"""Shared content and helpers for the Unit 2 rebuild (5 Oct 2026)."""
import json, re

def read(path):
    raw = open(path, 'rb').read().decode('utf-8')
    assert raw.count('\r\n') == raw.count('\n'), 'mixed line endings in ' + path
    return raw.replace('\r\n', '\n')

def write(path, text):
    assert '\r' not in text
    open(path, 'wb').write(text.replace('\n', '\r\n').encode('utf-8'))

def once(text, needle):
    n = text.count(needle)
    assert n == 1, 'expected 1 occurrence, found %d: %r' % (n, needle[:90])
    return text.index(needle)

def cut(text, start, end, inc_end=True):
    """Verbatim slice from start marker to end marker (both must be unique after start)."""
    i = once(text, start)
    j = text.index(end, i + len(start))
    return text[i:j + (len(end) if inc_end else 0)]

def line_with(text, needle):
    i = once(text, needle)
    a = text.rfind('\n', 0, i) + 1
    b = text.find('\n', i)
    return text[a:b]

def rep(text, old, new):
    once(text, old)
    return text.replace(old, new)

def js(obj):
    return json.dumps(obj, ensure_ascii=False)

ARROW = '<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div>'

def acc(title, meta, body, is_open=False, comment=None):
    out = ''
    if comment:
        out += '<!-- %s -->\n' % comment
    out += '<div class="acc%s">\n' % (' open' if is_open else '')
    out += '<div class="acc-h" onclick="tA(this)">\n'
    out += '  <span class="acc-t">%s</span>\n' % title
    out += '  <div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">%s</span>%s</div>\n' % (meta, ARROW)
    out += '</div>\n<div class="acc-b cb">\n' + body.strip('\n') + '\n</div>\n</div>\n'
    return out

# ── The four SiP domains ─────────────────────────────────────────────────────
DOM_COL = ['#8ab0e8', 'var(--gold)', '#5ecba1', '#c39de0']
DOM = ['Customer Experience &amp; Value', 'Operational Capability &amp; Execution Rhythm',
       'People &amp; Culture Dynamics', 'Enterprise Value Creation']
DOM_PLAIN = [d.replace('&amp;', '&') for d in DOM]

# ── The four dimensions of the Strategy Intent Statement ─────────────────────
W = ['WHAT', 'WHY', 'HOW', 'WHEN']

# ── The 14 elements of the Strategy2Results® Strategy Definition ─────────────
# Source: Carol's S2R Strategy Architect tool (v15), "Define Strategy" mode. Order, tags, guides and questions are hers.
# One wording change for standards rule 13: NAVIGATING guide ("using forces rather than merely fighting them").
ELEMENTS = [
    ("ITERATIVE", "Continuously refined",
     "Strategy is never finished in one pass. It is a hypothesis that loops: form → test against reality → revise → repeat. This rules out strategy as an annual ritual and rules in strategy as a living capability.",
     ["What core hypotheses does the strategy depend on?", "How will reality test those hypotheses?", "What evidence would trigger refinement?", "How and when will strategic choices be revisited?"]),
    ("THINKING & LOGIC", "The cognitive engine",
     "Thinking = divergent, exploratory, hypothesis-generating. Logic = convergent, analytical, assumption-testing. Both are required in sequence.",
     ["What alternative possibilities were explored?", "What assumptions underpin the preferred direction?", "What must be true for this strategy to work?", "What evidence supports or challenges the logic?"]),
    ("PROCESS", "Structured container",
     "Process turns ad hoc thinking into a repeatable, auditable, scalable method. It defines who is involved, what inputs are needed, what tools are used, and what decisions get made at each stage.",
     ["Who must participate in shaping the strategy?", "What inputs and evidence are required?", "What decision stages will be used?", "How will decisions and rationale be recorded?"]),
    ("WHAT", "Scope & definition",
     "What value are we creating? What business are we actually in? What do we offer and deliberately not offer? This sets the boundary of the organisation's field of play.",
     ["What business are we actually in?", "What value are we choosing to create?", "What will we offer?", "What will we deliberately not offer or pursue?"]),
    ("WHY", "Purpose & rationale",
     "Why does this organisation exist? Why would stakeholders choose us? The North Star that makes all other decisions coherent and gives the strategy its internal logic.",
     ["Why does the organisation exist?", "Why should stakeholders choose or support us?", "Why are these strategic choices appropriate?", "What unifying rationale makes the choices coherent?"]),
    ("HOW", "Mechanism & model",
     "How do we actually deliver the value? What capabilities, processes, structures and partnerships make it possible? This is where strategy meets the operating model.",
     ["What operating mechanism makes the strategy work?", "Which capabilities are essential?", "Which processes and structures must support it?", "Which partnerships or ecosystem relationships are required?"]),
    ("WHEN", "Timing & sequencing",
     "When do we move? When do we hold? When do we exit? Timing determines whether the right move wins or fails. Sequencing determines whether capability is built in the right order.",
     ["What must happen first, next and later?", "What determines when we move, hold or exit?", "Which dependencies shape the sequence?", "What timing assumptions could change the strategy?"]),
    ("CREATES VALUE", "Origination layer",
     "Value comes into existence through creation: product/service development, innovation, capability building, IP, brand equity — activities that generate new or improved worth.",
     ["What new or improved value will come into existence?", "Through which activities is that value created?", "What capabilities or assets enable creation?", "How will we know that genuine value has been created?"]),
    ("DELIVERS VALUE", "Distribution & access layer",
     "Creating value means nothing if it does not reach intended recipients. Delivery is the full system of transmission: channels, distribution, customer experience, partnerships and pricing.",
     ["How will created value reach each intended recipient?", "Which channels and access mechanisms matter?", "What experience must recipients have?", "What could prevent value from reaching them?"]),
    ("SUSTAINS VALUE", "Durability & compounding layer",
     "Sustaining requires investment in the conditions that make value possible: relationships, infrastructure, culture, financial health and continued relevance.",
     ["What makes this value durable over time?", "What must be continually invested in or renewed?", "What could erode the value?", "How will relevance and viability be sustained?"]),
    ("STAKEHOLDERS", "Full universe of value recipients",
     "Broader than customers: everyone with a stake in the organisation's actions, including employees, investors, communities, regulators, partners and future generations.",
     ["Who has a material stake in our actions?", "What value does each stakeholder group receive or contribute?", "Where do stakeholder interests reinforce or conflict?", "Whose interests could be overlooked by this strategy?"]),
    ("NAVIGATING", "Active, skilful movement",
     "Navigation implies agency, skill and continuous course correction. Read the environment, interpret it and make deliberate moves through it — putting the forces to use.",
     ["How will the organisation sense changes in its environment?", "How will signals be interpreted and translated into decisions?", "Where can external forces be used to advantage?", "What enables deliberate course correction?"]),
    ("THE FORCES", "What must be navigated",
     "Competitive, macro, disruptive, social and environmental forces shape strategic viability: rivals, substitutes, regulation, economics, technology, business models, ESG and demographic shifts.",
     ["Which competitive forces materially shape the strategy?", "Which macro and regulatory forces matter most?", "Which disruptive forces could alter the model?", "Which social or environmental forces create risk or opportunity?"]),
    ("OPERATING ENVIRONMENT", "The bounded context",
     "The full system within which the organisation exists: industry, economy, regulation, technology, social context and physical environment. Strategy only makes sense within a defined environment.",
     ["What is the defined operating context for this strategy?", "Which industry and market conditions shape it?", "Which regulatory, technological and social conditions matter?", "Where would this strategy stop making sense if the context changed?"]),
]
# The five headings of the Strategy Architecture output (tool: architectureSeed / architecturePrintBody)
ARCH_GROUPS = [
    ("Strategic Position", ["WHAT", "WHY"]),
    ("Strategic Model", ["HOW", "WHEN"]),
    ("Value Architecture", ["CREATES VALUE", "DELIVERS VALUE", "SUSTAINS VALUE", "STAKEHOLDERS"]),
    ("Strategic Navigation", ["NAVIGATING", "THE FORCES", "OPERATING ENVIRONMENT"]),
    ("Strategy Discipline", ["ITERATIVE", "THINKING & LOGIC", "PROCESS"]),
]
# Success in Practice: lead question and three input questions per domain (tool: SIP_DOMAINS)
SIP_DOMAINS = [
    ("Customer Experience & Value", "If the intent succeeds, what should customers and other value recipients see and experience?",
     ["What will customers or value recipients experience differently?", "What value or result will they consistently receive?", "What observable evidence will tell us this is true?"]),
    ("Operational Capability & Execution Rhythm", "If the intent succeeds, what should be visible in how the organisation operates and executes?",
     ["What capabilities and operating conditions will be functioning effectively?", "How will priorities, decisions, coordination and delivery work in practice?", "What observable evidence will show that execution is working?"]),
    ("People & Culture Dynamics", "If the intent succeeds, what should be visible in how people understand, decide and behave?",
     ["What will people understand about the strategic intent and their contribution?", "How will people decide, collaborate, take ownership and behave?", "What observable evidence will show that these conditions are embedded?"]),
    ("Enterprise Value Creation", "If the intent succeeds, how should the organisation benefit across its success metrics?",
     ["What enterprise outcomes should improve as a result of the strategy?", "What strategic or market position should the organisation achieve?", "What evidence will show that value is being sustained within the time horizon?"]),
]
def amp(t): return t.replace('&', '&amp;')
def el_q(i, j): return 'arch_e%02d_q%d' % (i, j)      # i = 1..14, j = 1..4  (answer)
def el_rs(i): return 'arch_e%02d_rs' % i              # confirmed position ("what this is saying")
def el_conf(i): return 'Element %d · %s' % (i, ELEMENTS[i - 1][0])
def sip_q(d, j): return 'sip_d%d_q%d' % (d, j)        # d = 1..4, j = 1..3
def sip_st(d): return 'sip_d%d_st' % d                # confirmed domain statement

# ── 3.2 SiP Flammables: teaching content only (5 Oct, Carol: more substance; no participant question) ──
FLAMS = [
    {"dim": "D1 Dominant — Customer Only",
     "what": "The SiP reads as a marketing aspiration: vivid about the customer experience, silent on how the organisation will build and sustain it. The customer statement is rich and specific. The operational, people and enterprise statements are thin, or repeat the customer promise in other words. Leaders can describe what customers will feel and cannot describe the capability, the behaviour or the economics that produce it.",
     "signs": ["Every domain statement begins and ends with the customer.",
               "No statement names a capability, a decision right or a delivery rhythm.",
               "The enterprise statement assumes that growth follows from satisfaction, with no account of cost to serve."],
     "risk": "Execution capacity is underestimated. The customer promise is made without accounting for the operational and cultural conditions required to deliver it. The organisation commits publicly to an experience it cannot yet produce at scale, so delivery teams absorb the gap through workarounds and overtime. Service becomes inconsistent, cost to serve rises faster than revenue, and the promise that was meant to differentiate the organisation becomes the source of customer disappointment."},
    {"dim": "D2 Dominant — Operations Only",
     "what": "The SiP reads as a process optimisation plan: efficient and measurable, and stripped of the customer meaning and cultural texture that make execution energising. Success is described in throughput, cycle time, cost and compliance. The customer appears as a recipient of efficiency. People appear as resources inside the process.",
     "signs": ["Statements describe how work flows and say little about who benefits.",
               "Every measure of success is internal: speed, cost, error rates.",
               "The people statement lists roles and procedures, with no behaviour or ownership."],
     "risk": "The organisation improves its machine while losing sight of what the machine is for. Execution becomes an end in itself. The efficiency gains are real, and the value they were meant to serve drifts: the organisation becomes faster at delivering what customers value less. People comply with the process without owning the outcome, so the system stops adapting when the market moves."},
    {"dim": "D3 Dominant — People Only",
     "what": "The SiP reads as an organisational development narrative: rich in values, commercially unanchored, difficult to measure and easy to dismiss. Success is described through engagement, collaboration, trust and leadership behaviour. The customer outcome and the enterprise outcome are implied and never stated.",
     "signs": ["Statements describe how people feel and behave, with no link to a customer result or a commercial result.",
               "No statement could be tested against evidence within the time horizon.",
               "Operational capability is described as culture, with no mechanism behind it."],
     "risk": "Culture work becomes disconnected from commercial outcomes. The strategy describes who the organisation wants to be and leaves what it intends to achieve undefined. Investment in people and culture cannot be defended when results come under pressure, so it is the first budget to be cut. Leaders outside the people function disengage from the SiP, and culture becomes one function's project."},
    {"dim": "D4 Dominant — Value Only",
     "what": "The SiP reads as a financial target: measurable and motivationally thin, describing the score without describing the game. Success is expressed in revenue, margin, market share and return. The statements say what the organisation will gain and say little about what customers, operations and people must look like to produce it.",
     "signs": ["Every statement resolves into a number.",
               "The customer statement is a sales target or a share target.",
               "No statement describes a capability or a behaviour that produces the result."],
     "risk": "Leaders optimise for metrics without creating the conditions that produce them. Short-termism disguises itself as strategic clarity. Targets are met through cost cutting, price moves and deferred investment, which weakens the capabilities and relationships that future results depend on. Functions compete for the numbers they are measured on, and the enterprise outcome erodes while each scorecard stays green."},
]
def flam_js(accent_risk_label):
    import json
    return 'var FLAMS=[\n' + ',\n'.join('  ' + json.dumps(x, ensure_ascii=False) for x in FLAMS) + '\n];\n'
def flam_render(fn, host_id, prefix, cols_class):
    return """function %s(){
  var el=document.getElementById('%s');if(!el)return;
  el.innerHTML=FLAMS.map(function(f,i){
    return '<div class="sub-acc" id="%s'+i+'">'+
      '<div class="sub-acc-h" onclick="tSA(this)" style="border-left:3px solid rgba(231,76,60,.4);padding-left:14px;">'+
        '<span style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(231,100,80,.9);">'+f.dim+'</span>'+
        '<span class="sub-arr">▼</span>'+
      '</div>'+
      '<div class="sub-acc-b%s" style="padding-top:12px;">'+
        '<div>'+
          '<p class="u2-lbl" style="color:rgba(255,255,255,.4);">What It Creates</p>'+
          '<p class="u2-txt">'+f.what+'</p>'+
          '<p class="u2-lbl" style="color:rgba(255,255,255,.4);margin-top:14px;">Indicators</p>'+
          '<ul class="u2-signs">'+f.signs.map(function(s){return '<li>'+s+'</li>';}).join('')+'</ul>'+
        '</div>'+
        '<div>'+
          '<p class="u2-lbl" style="color:rgba(231,76,60,.65);">Strategic Risk if Not Balanced</p>'+
          '<p class="u2-txt" style="color:rgba(231,120,100,.9);">'+f.risk+'</p>'+
        '</div>'+
      '</div>'+
    '</div>';
  }).join('');
}
""" % (fn, host_id, prefix, cols_class)

CHAIN = ('<div class="u2-chain">'
         '<div class="u2-chain-box"><small>Output 1</small>Strategy Architecture</div><div class="u2-chain-arr">→</div>'
         '<div class="u2-chain-box"><small>Output 2</small>Strategy Intent</div><div class="u2-chain-arr">→</div>'
         '<div class="u2-chain-box"><small>Output 3</small>Success in Practice</div></div>')

SIX_CHECKS = ['Do our choices reinforce one another?',
              'Where are there contradictions or unresolved tensions?',
              'Does our HOW support what we have chosen to achieve?',
              'Does our timing and sequencing reflect the realities of our capability and environment?',
              'Have we addressed how value will be created, delivered <strong>and sustained</strong>?',
              'Does the architecture represent the strategic position we collectively intend?']

KLO1 = 'Define strategy architecture and articulate strategic intent in relation to the organisation&rsquo;s purpose, long-term value and stakeholder relevance.'
OLD_KLO1 = '<span class="klo">Articulate strategic intent in relation to the organisation&rsquo;s purpose, long-term value and stakeholder relevance.</span>'

SLO = {
    1: ['Redefine strategy to create a robust understanding of strategy architecture.',
        'Distinguish the direction an organisation sets from the future position that defines its success.'],
    2: ['Explain how a shared strategic ambition and a shared picture of success keep leaders and functions aligned.',
        'Recognise how a shared direction filters decisions throughout execution.'],
    3: ['Use observable indicators to examine what success looks like within each of the four SiP domains.',
        'Distinguish between conditions that demonstrate success and signals that those conditions are absent.'],
    4: ['Build a coherent Strategy Architecture.',
        'Integrate different leadership perspectives into one shared enterprise position.'],
    5: ['Apply the agreed Success in Practice to specific executive roles.',
        'Define what each leadership role must contribute to make the Strategy Intent real.'],
}
def slo(n):
    return ('<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>' +
            ''.join('<li>%s</li>' % x for x in SLO[n]) + '</ul></div>')

HERO = {
    1: ('Section 1 · Awareness — What', 'What is Strategy?',
        'Interrogative Anchor · What is the Strategy Architecture? What is the Strategy Intent Statement? What is Success in Practice?'),
    2: ('Section 2 · Intelligence — Why', 'The Importance and Relevance of SiP',
        'Ignition Point · Why do the Strategy Intent and SiP matter once they are defined? How do they shape alignment, choices and execution?'),
    3: ('Section 3 · Extrapolating — Where', 'Examining Success in Practice',
        'Locate Hot Zones · Depth within each SiP domain · Balance across all four SiP domains'),
    4: ('Section 4 · Integration — Collective', 'Build the Architecture · Derive the Intent · Define Success in Practice', None),
    5: ('Section 5 · Application — In Practice', 'From Success in Practice to Leadership Contribution', None),
}
def hero(n, sub=None):
    lab, h2, s = HERO[n]
    return ('<div class="mod-hero">\n  <p class="mod-hero-label">%s</p>\n  <h2>%s</h2>\n  <p>%s</p>\n</div>\n'
            % (lab, h2.replace('&', '&amp;') if '&amp;' not in h2 else h2, sub or s))

TITLES = {
    '1.1': ('1.1 — Define the Strategy Architecture', '9 Concepts · Click to expand each'),
    '1.2': ('1.2 — Defining the Strategy Intent Statement', '4 Dimensions'),
    '1.3': ('1.3 — Success in Practice (SiP): From Intent to Future Reality', '4 Observable Domains'),
    '2.1': ('2.1 — Role of Strategy Intent &amp; SiP in the S2R® Architecture', '3 Functions'),
    '3.1': ('3.1 — SiP Observable Indicators', '4 Domains · Click indicators to expand'),
    '3.2': ('3.2 — SiP Flammables: When the Picture of Success Becomes Distorted', '4 Risk Patterns'),
    '4.1': ('4.1 — Step 1: Build the Strategy Architecture', '14 Elements · One Integrated Architecture'),
    '4.2': ('4.2 — Step 2: Derive the Strategy Intent Statement', 'WHAT · WHY · HOW · WHEN → One Strategic Ambition'),
    '4.3': ('4.3 — Step 3: Build Success in Practice', '4 Domains · 4 Confirmed Statements · One SiP'),
    '4.S': ('Integration Synthesis', '3 Connected Outputs'),
    '5.1': ('5.1 — Role Contribution to SiP', '10 Roles · 4 Domains'),
    '5.2': ('5.2 — SiP Statement Collective Application', 'Share · Explain · Observe'),
}

NEW_CSS = '''/* UNIT 2 REBUILD (Oct 2026) */
.u2-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:14px 0;}
.u2-card{background:#151c15;border:1px solid rgba(255,255,255,.06);border-radius:3px;padding:14px 16px;}
.u2-card-h{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;color:var(--ACC);}
.u2-card p{font-size:12px;color:rgba(255,255,255,.6);line-height:1.65;margin:0;}
.u2-chain{display:flex;align-items:stretch;gap:8px;margin:16px 0;}
.u2-chain-box{flex:1;padding:14px 12px;text-align:center;background:#151c15;border:1px solid rgba(201,168,76,.25);border-radius:3px;font-family:'Cormorant Garamond',serif;font-size:1.05rem;color:#fff;}
.u2-chain-box small{display:block;font-family:'Montserrat',sans-serif;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:4px;}
.u2-chain-arr{display:flex;align-items:center;color:var(--gold);font-size:1.1rem;}
.u2-why{grid-column:1/-1;}
.u2-lbl{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;}
.u2-txt{font-size:13px;color:rgba(255,255,255,.7);line-height:1.75;margin:0;}
.u2-signs{margin:0;padding-left:18px;}.u2-signs li{font-size:13px;color:rgba(255,255,255,.7);line-height:1.7;margin-bottom:5px;}
.u2-ql{margin:0;padding-left:20px;}.u2-ql li{font-size:13px;color:rgba(255,255,255,.7);line-height:1.7;margin-bottom:4px;}
@media(max-width:700px){.u2-grid{grid-template-columns:1fr;}.u2-chain{flex-direction:column;}.u2-chain-arr{justify-content:center;transform:rotate(90deg);}}
'''
