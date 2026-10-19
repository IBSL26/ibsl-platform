# -*- coding: utf-8 -*-
"""Unit 2 capstone rework (19 October 2026).
Section 4 becomes one full worked example (read-only, both pages).
Section 5 becomes the capstone build: the group builds its simulated company's Strategy Architecture,
Strategy Intent Statement and SiP on one shared group record (scribe per assignment, every member agrees).
5.1 Role Contribution and 5.2 Collective Application come off both pages.

usage: python3 build_u02cap.py <p in> <f in> <p out> <f out>
"""
import sys, re, html, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import we_content as W

HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape

def rd(p):
    return open(p, encoding='utf-8', newline='').read().replace('\r\n', '\n')

def wr(p, s):
    open(p, 'w', encoding='utf-8', newline='').write(s.replace('\n', '\r\n'))

def cut(s, start, end, new, inclusive_end=False):
    i = s.index(start)
    j = s.index(end, i)
    if inclusive_end:
        j += len(end)
    return s[:i] + new + s[j:]

def once(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:90])
    return s.replace(old, new)

# Element questions, read from the participant page so the example uses the live wording.
def element_questions(p):
    m = re.search(r'var EL=\[(.*?)\n\];', p, re.S)
    import json
    els = json.loads('[' + m.group(1) + ']')
    return els

def sip_domains(p):
    m = re.search(r'var SIPD=\[(.*?)\n\];', p, re.S)
    import json
    return json.loads('[' + m.group(1) + ']')

# ───────────────────────────── CSS ─────────────────────────────
CSS = '''
/* Unit 2 · Section 4 worked example and Section 5 group build (19 Oct 2026) */
.u2w-how{background:rgba(26,122,106,.07);border:1px solid rgba(26,122,106,.25);border-left:3px solid var(--teal);border-radius:0 3px 3px 0;padding:14px 18px 10px;margin:0 0 16px;}
.u2w-how-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#5ecba1;margin:0 0 6px;}
.u2w-how ol{margin:6px 0 8px;padding-left:20px;}
.u2w-how li{font-size:13px;color:rgba(255,255,255,.8);line-height:1.75;margin-bottom:4px;}
.u2w-how p{font-size:13px;line-height:1.7;color:rgba(255,255,255,.8);margin:8px 0 0;}
.u2b-co{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;margin:12px 0 16px;}
.u2b-co-c{background:#151c15;border:1px solid rgba(201,168,76,.2);border-radius:3px;padding:12px 14px;}
.u2b-co-c b{display:block;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:4px;}
.u2b-co-c span{font-size:13px;line-height:1.65;color:rgba(255,255,255,.82);white-space:pre-wrap;}
.u2b-wide{grid-column:1/-1;}
details.u2w-det{border:1px solid rgba(255,255,255,.08);border-radius:3px;margin:8px 0;background:#141d15;}
details.u2w-det>summary{cursor:pointer;padding:12px 16px;font-size:12.5px;font-weight:700;color:rgba(255,255,255,.85);list-style:none;}
details.u2w-det>summary::-webkit-details-marker{display:none;}
details.u2w-det>summary::after{content:'▼';float:right;font-size:10px;color:rgba(255,255,255,.35);}
details.u2w-det[open]>summary::after{content:'▲';color:var(--gold);}
details.u2w-det>summary small{font-weight:400;color:rgba(255,255,255,.45);margin-left:8px;}
.u2w-body{padding:2px 16px 14px;}
.u2w-qa{margin:0 0 10px;}
.u2w-q{font-size:11.5px;font-weight:600;color:rgba(255,255,255,.55);line-height:1.5;}
.u2w-a{font-size:13px;color:rgba(255,255,255,.85);line-height:1.65;}
.u2w-say{background:rgba(201,168,76,.07);border-left:3px solid var(--gold);border-radius:0 3px 3px 0;padding:10px 14px;margin-top:10px;}
.u2w-say b{display:block;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:3px;}
.u2w-say span{font-size:13px;color:#fff;line-height:1.65;}
.u2w-grp{margin:0 0 14px;}
.u2w-grp-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#5ecba1;margin:0 0 6px;padding-bottom:4px;border-bottom:1px solid rgba(255,255,255,.08);}
.u2w-row{display:grid;grid-template-columns:150px 1fr;gap:12px;margin:0 0 8px;}
.u2w-row b{font-size:10px;font-weight:700;letter-spacing:1px;color:rgba(255,255,255,.6);text-transform:uppercase;}
.u2w-row span{font-size:12.5px;color:rgba(255,255,255,.82);line-height:1.6;}
.u2w-intent{border-left:4px solid var(--gold);background:rgba(201,168,76,.06);padding:16px 18px;margin:14px 0;font-family:'Cormorant Garamond',serif;font-size:1.2rem;line-height:1.6;color:#fff;}
.u2w-list{margin:6px 0 12px;padding-left:20px;}
.u2w-list li{font-size:13px;color:rgba(255,255,255,.78);line-height:1.7;margin-bottom:4px;}
.u2b-grid{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:16px;align-items:start;margin:10px 0;}
.u2b-lesson{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:3px;padding:14px 16px;}
.u2b-lesson-h{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#5ecba1;margin-bottom:8px;}
.u2b-lesson p{font-size:12.5px;line-height:1.7;color:rgba(255,255,255,.75);margin:0 0 8px;}
.u2b-lesson p b{color:#fff;}
.u2b-entry .u2-q{margin-top:10px;}
.u2b-ta{background:#0a1a0d!important;border:1px solid rgba(26,122,106,.25)!important;border-radius:3px;min-height:64px;}
.u2b-say{color:var(--gold)!important;}
.u2b-count{font-size:11px;color:rgba(255,255,255,.6);}
.u2b-count b{color:var(--gold);}
.u2b-lead{font-size:12.5px;color:rgba(255,255,255,.6);font-style:italic;margin:0 0 4px;padding:0 16px;}
details.u2b-det{border:1px solid rgba(255,255,255,.08);border-radius:3px;margin:8px 0;padding-bottom:10px;background:#141d15;}
details.u2b-det>summary{cursor:pointer;padding:12px 16px;font-size:12.5px;font-weight:700;color:rgba(255,255,255,.85);}
details.u2b-det .u2-q,details.u2b-det textarea{margin-left:16px;margin-right:16px;width:calc(100% - 32px);}
.step-tabs{display:flex;gap:4px;margin:16px 0 0;flex-wrap:wrap;}
.step-tab{flex:1;min-width:80px;padding:10px 8px;text-align:center;background:#121e1c;border:1px solid rgba(255,255,255,.07);border-radius:3px 3px 0 0;cursor:pointer;transition:all .2s;}
.step-tab.active{background:#1a2e28;border-color:var(--teal);border-bottom-color:#1a2e28;}
.step-num{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(26,122,106,.8);margin-bottom:4px;}
.step-name{font-family:"Cormorant Garamond",serif;font-size:.9rem;color:rgba(255,255,255,.6);}
.step-tab.active .step-name{color:#fff;}
.step-panel{display:none;background:#0d1a17;border:1px solid rgba(26,122,106,.15);border-top:none;border-radius:0 0 4px 4px;padding:20px;margin-bottom:14px;}
.step-panel.active{display:block;}
.u7-rec{border-top:1px solid rgba(255,255,255,.07);padding:8px 0;}
.u7-rec-s{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.45);margin:10px 0 3px;}
.u7-rec-t{font-size:12.5px;line-height:1.65;color:rgba(255,255,255,.78);white-space:pre-wrap;}
.u7-rec-t i{color:rgba(255,255,255,.3);}
.u2b-period{max-width:320px;margin:4px 0 12px;}
@media (max-width:760px){.u2b-grid{grid-template-columns:1fr;}.u2w-row{grid-template-columns:1fr;gap:2px;}}
'''

# ───────────────────── Section 4 · the worked example ─────────────────────
def company_cards():
    c = W.COMPANY
    return ('<div class="u2b-co">'
            '<div class="u2b-co-c"><b>Company</b><span>%s</span></div>'
            '<div class="u2b-co-c"><b>Sector</b><span>%s</span></div>'
            '<div class="u2b-co-c"><b>Size</b><span>%s</span></div>'
            '<div class="u2b-co-c"><b>Strategy period</b><span>%s</span></div>'
            '<div class="u2b-co-c u2b-wide"><b>Its central organisational problem</b><span>%s</span></div>'
            '</div>') % (E(c['name']), E(c['sector']), E(c['size']), E(c['period']), E(c['problem']))

def elements_html(els):
    out = []
    by = {e['n']: e for e in els}
    for n, (name, answers, saying) in enumerate(W.ELEMENTS, 1):
        e = by[name]
        assert len(e['qs']) == len(answers), name
        qa = ''.join('<div class="u2w-qa"><div class="u2w-q">%s</div><div class="u2w-a">%s</div></div>' % (E(q), E(a))
                     for q, a in zip(e['qs'], answers))
        out.append('<details class="u2w-det"><summary>%d · %s<small>%s</small></summary><div class="u2w-body">%s'
                   '<div class="u2w-say"><b>What this element is saying</b><span>%s</span></div></div></details>'
                   % (n, E(name), E(e['tag']), qa, E(saying)))
    return '\n'.join(out)

GROUPS = [["Strategic Position", ["WHAT", "WHY"]], ["Strategic Model", ["HOW", "WHEN"]],
          ["Value Architecture", ["CREATES VALUE", "DELIVERS VALUE", "SUSTAINS VALUE", "STAKEHOLDERS"]],
          ["Strategic Navigation", ["NAVIGATING", "THE FORCES", "OPERATING ENVIRONMENT"]],
          ["Strategy Discipline", ["ITERATIVE", "THINKING & LOGIC", "PROCESS"]]]

def architecture_html():
    say = {n: s for n, _, s in W.ELEMENTS}
    return ''.join('<div class="u2w-grp"><div class="u2w-grp-h">%s</div>%s</div>' % (
        E(g), ''.join('<div class="u2w-row"><b>%s</b><span>%s</span></div>' % (E(n), E(say[n])) for n in names))
        for g, names in GROUPS)

def intent_cards():
    say = {n: s for n, _, s in W.ELEMENTS}
    dims = [('WHAT', 'Scope & Definition'), ('WHY', 'Purpose & Rationale'), ('HOW', 'Mechanism & Model'), ('WHEN', 'Timing & Sequencing')]
    return '<div class="u2-grid">' + ''.join(
        '<div class="u2-card"><div class="u2-card-h">%s — %s</div><p>%s</p></div>' % (d, E(t), E(say[d])) for d, t in dims) + '</div>'

def sip_html(sipd):
    out = []
    for d, ((answers, st), dom) in enumerate(zip(W.SIP, sipd), 1):
        qa = ''.join('<div class="u2w-qa"><div class="u2w-q">%s</div><div class="u2w-a">%s</div></div>' % (E(q), E(a))
                     for q, a in zip(dom['qs'], answers))
        out.append('<details class="u2w-det"%s><summary>D%d · %s</summary><div class="u2w-body"><p class="u2w-q" style="font-style:italic;margin-bottom:8px;">%s</p>%s'
                   '<div class="u2w-say"><b>SiP statement %d</b><span>%s</span></div></div></details>'
                   % (' open' if d == 1 else '', d, E(dom['t']), E(dom['lead']), qa, d, E(st)))
    return '\n'.join(out)

def acc(title, meta, body, open_=False):
    return ('<div class="acc%s">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">%s</span>\n'
            '  <div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">%s</span><div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div>\n'
            '</div>\n<div class="acc-b cb">\n%s\n</div>\n</div>\n') % (' open' if open_ else '', title, meta, body)

def fnote(label, body):
    return '<div class="fac-note-full"><div class="fac-note-full-label">%s</div>%s</div>' % (label, body)

SLO4 = '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>Integrate the elements of Strategy Architecture into a coherent enterprise strategy.</li><li>Synthesise diverse leadership perspectives into an agreed enterprise position.</li></ul></div>'
SLO5 = '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>Translate Success in Practice into clear executive contribution expectations.</li><li>Coordinate leadership contributions required to realise strategic intent.</li></ul></div>'

def section4(els, sipd, fac):
    c = W.COMPANY['name']
    if fac:
        hero_p = 'One worked example takes Kestrel Point Services through the three connected outputs: Strategy Architecture → Strategy Intent → Success in Practice.'
        how = ('<div class="u2w-how"><div class="u2w-how-h">How the worked example is used</div><ol>'
               '<li>The example introduces Kestrel Point Services and its central organisational problem.</li>'
               '<li>4.1 shows each of the 14 elements answered, what each element is saying and the Strategy Architecture under its five headings.</li>'
               '<li>4.2 shows how WHAT, WHY, HOW and WHEN became one Strategy Intent Statement.</li>'
               '<li>4.3 shows the four SiP domains answered and the four statements, tested for depth and balance.</li></ol>'
               '<p>The example is read-only on both pages. In Section 5 each group builds the same three outputs for its own simulated company.</p></div>')
    else:
        hero_p = 'Follow one company through the three connected outputs: Strategy Architecture → Strategy Intent → Success in Practice. In Section 5 your group builds the same three outputs for its own company.'
        how = ('<div class="u2w-how"><div class="u2w-how-h">How to read the worked example</div><ol>'
               '<li>Meet the company and its central organisational problem.</li>'
               '<li>4.1 shows each of the 14 elements answered, what each element is saying and the Strategy Architecture under its five headings.</li>'
               '<li>4.2 shows how WHAT, WHY, HOW and WHEN became one Strategy Intent Statement.</li>'
               '<li>4.3 shows the four SiP domains answered and the four statements, tested for depth and balance.</li></ol>'
               '<p>Open each part in turn. Refer to it when your group builds its own three outputs in Section 5.</p></div>')

    g4 = ''
    if fac:
        g4 = fnote('&#9670; FACILITATOR GUIDANCE — Section 4 · Integration',
                   '<p><strong>Section intent:</strong> Section 4 shows the whole Strategy Intent Design completed once, for one company, before the groups build their own in Section 5. Teach it from the deck: take participants through the three outputs in order and show how each one becomes the source of the next.</p>'
                   '<p>Strategy Architecture → Strategy Intent → Success in Practice</p>'
                   '<p>The quality of the SiP depends on the quality of the Intent, and the quality of the Intent depends on the thinking captured in the Architecture. The example makes that chain visible: the client promise named in WHAT returns in the Intent and again in the first SiP statement.</p>'
                   '<p><strong>The case:</strong> Kestrel Point Services is the same company that appears in the Unit 3 worked example. Its four SiP statements lead into the SiP statement used there, and from there into the Key Results tested in Unit 4.</p>')

    intro = company_cards()

    b41 = ''
    if fac:
        b41 += fnote('&#9670; FACILITATOR GUIDANCE — Section 4.1',
                     '<p>Open two or three elements in full, starting with WHAT, then show the Strategy Architecture under its five headings.</p>'
                     '<p>Point out how the elements depend on one another in the example: WHAT chooses responsiveness; HOW supplies the mechanism through integrated client teams and one operating rhythm; WHEN puts the request system in place before decision rights move to the hubs; SUSTAINS VALUE and THE FORCES both name silos as the main threat.</p>'
                     '<p>Show how each "What this element is saying" is written: one or two sentences, in the company\'s own words, carrying the actual strategic choice.</p>')
    b41 += ('<p>The elements are interconnected: a strong answer to one element can expose a weakness or contradiction in another. The value an organisation intends to create must be supported by its HOW. Its WHEN must reflect the capabilities it needs to build. Its approach to sustaining value must respond to the forces within its operating environment.</p>'
            '<div class="hbox teal"><p><strong>How each element works.</strong> Each element has four questions (THE FORCES has five). They are answered with actual strategic choices. Then one or two sentences state <strong>what the element is saying</strong>. Open each element to read it.</p></div>')
    b41 += elements_html(els)
    b41 += '<h4>The Strategy Architecture</h4><p>When all 14 elements say what they mean, they come together under five headings and are read as one strategic system:</p><div class="quote"><p>"What is this architecture collectively saying about our organisation\'s strategy?"</p></div>'
    b41 += '<details class="u2w-det" open><summary>Kestrel Point Services · Strategy Architecture<small>%s</small></summary><div class="u2w-body">%s</div></details>' % (E(W.COMPANY['period']), architecture_html())
    b41 += '<p>Read as one system, the choices reinforce one another: the client promise in WHAT is carried by the mechanism in HOW, sequenced in WHEN and protected by naming the internal forces that work against it.</p>'

    b42 = ''
    if fac:
        b42 += fnote('&#9670; FACILITATOR GUIDANCE — Section 4.2',
                     '<p>Show the four cards first, then the statement. Take participants through how each dimension found its place in the statement, using the four lines under the cards.</p>'
                     '<p>Draw attention to what the statement leaves out: the request system, the hub decision rights and the subcontractor standards stay in the Architecture. The statement carries the ambition.</p>')
    b42 += '<p>The Architecture holds the depth. The Strategy Intent Statement gives the clarity. These are the four dimensions Kestrel Point brought forward from its Architecture:</p>'
    b42 += intent_cards()
    b42 += '<h4>How the statement was deduced</h4><ul class="u2w-list">' + ''.join('<li>%s</li>' % E(x) for x in W.INTENT_HOW) + '</ul>'
    b42 += '<div class="u2w-intent">%s</div>' % E(W.INTENT)
    b42 += '<div class="quote"><p>"Does this statement faithfully express the strategic ambition contained in our Architecture?"</p></div><p>Read against the Architecture, the statement carries the ambition and leaves the detail to the Architecture.</p>'

    b43 = ''
    if fac:
        b43 += fnote('&#9670; FACILITATOR GUIDANCE — Section 4.3',
                     '<p>Ask participants to stand inside the future the Intent describes. Open D1, read the three answers, then the statement written from them. Repeat for the other three domains.</p>'
                     '<p>Close with the two tests from Section 3, depth and balance, as the example applies them, then show the three outputs together.</p>')
    b43 += '<p>Standing inside the future its Strategy Intent describes, Kestrel Point asked one central question:</p><div class="quote"><p>"If our Strategy Intent is successful, what should we see in practice?"</p></div>'
    b43 += sip_html(sipd)
    b43 += '<h4>Testing the SiP</h4><div class="u2-grid">' + ''.join('<div class="u2-card"><div class="u2-card-h">%s</div><p>%s</p></div>' % (E(t), E(x)) for t, x in W.SIP_TEST) + '</div>'
    b43 += ('<h4>The three outputs together</h4><div class="u2-chain"><div class="u2-chain-box"><small>Strategy Architecture</small>Provides the logic</div><div class="u2-chain-arr">→</div>'
            '<div class="u2-chain-box"><small>Strategy Intent</small>Crystallises the ambition</div><div class="u2-chain-arr">→</div>'
            '<div class="u2-chain-box"><small>Success in Practice</small>Makes the ambition observable</div></div>')
    b43 += ('<p>In Section 5 each group builds these three outputs for its own simulated company.</p>' if fac else
            '<p>In Section 5 your group builds these three outputs for its own simulated company.</p>')

    sub = 'Worked Example'
    body = (SLO4 + '\n' + g4 + '\n' + how + '\n' + intro + '\n' +
            acc('4.1 — Step 1: The Strategy Architecture', '14 Elements · One Integrated Architecture · ' + sub, b41, True) +
            acc('4.2 — Step 2: The Strategy Intent Statement', 'WHAT · WHY · HOW · WHEN → One Strategic Ambition · ' + sub, b42) +
            acc('4.3 — Step 3: Success in Practice', '4 Domains · 4 Statements · One SiP · ' + sub, b43))
    hero = ('<div class="mod-hero">\n  <p class="mod-hero-label">Section 4 · Integration — Collective</p>\n'
            '  <h2>One Worked Example: Architecture · Intent · Success in Practice</h2>\n  <p>%s</p>\n</div>\n') % E(hero_p)
    return hero, body

# ───────────────────── Section 5 · the capstone build ─────────────────────
HOW5_P = ('<div class="u2w-how"><div class="u2w-how-h">How Section 5 works</div>'
          '<p>This is group work and Capstone work. Your group builds three outputs for the simulated company of its Problem Charter, in order:</p><ol>'
          '<li><strong>Step 1 · Strategy Architecture.</strong> Answer the questions of the 14 elements and write what each element is saying. The scribe then brings the elements together under five headings, and your group edits the text until it says what your group intends.</li>'
          '<li><strong>Step 2 · Strategy Intent Statement.</strong> Deduce one crisp statement from WHAT, WHY, HOW and WHEN.</li>'
          '<li><strong>Step 3 · Success in Practice.</strong> Answer the three questions of each SiP domain and write one statement for each domain.</li></ol>'
          '<p>Your group chooses its scribe for this work in the group record bar. The scribe types what your group agrees, and the entries appear on every member\'s page. Your group can change the scribe at any time.</p>'
          '<p>In the Group record tab, each member reads the record and selects Agree. When every member has agreed, the three outputs go into your team\'s Capstone Blueprint. Section 4 shows each step completed for Kestrel Point Services.</p></div>')

def step_box(title, items):
    return '<div class="u2w-how"><div class="u2w-how-h">Capstone work &middot; How to complete %s</div><ol>%s</ol></div>' % (title, ''.join('<li>%s</li>' % x for x in items))

def section5_p():
    tool = ('<div id="u2bCharter"></div>\n'
            '<div id="u2bTeam"></div>\n'
            '<div id="u2bTool">\n'
            '<label class="u2-inlbl" for="strategy_period">Strategy period</label>'
            '<input class="u2-in u2b-period" type="text" id="strategy_period" placeholder="e.g. 2027–2029" oninput="u2In(\'strategy_period\',this.value)">\n'
            '<div class="step-tabs">'
            '<div class="step-tab active" onclick="u2Step(0)"><div class="step-num">Step 1</div><div class="step-name">Strategy Architecture</div></div>'
            '<div class="step-tab" onclick="u2Step(1)"><div class="step-num">Step 2</div><div class="step-name">Strategy Intent Statement</div></div>'
            '<div class="step-tab" onclick="u2Step(2)"><div class="step-num">Step 3</div><div class="step-name">Success in Practice</div></div>'
            '<div class="step-tab" onclick="u2Step(3)"><div class="step-num">Record</div><div class="step-name">Group record</div></div>'
            '</div>\n'
            '<div class="step-panel active">' +
            step_box('Step 1 &middot; Strategy Architecture', [
                'Choose an element from the row below. Read the lesson for the element beside the boxes.',
                'Answer its questions with your group\'s actual strategic choices for your company.',
                'Write <strong>what this element is saying</strong>: one or two sentences in your own words. The element shows a tick when it is written.',
                'When all 14 elements are written, the scribe selects <strong>Bring the 14 elements together</strong>. The elements appear under the five headings.',
                'Read the Architecture as one system with the checks in the lesson, and edit the text until it says what your group intends.']) +
            '<div class="u2-chips" id="u2bChips"></div><div id="u2bEl"></div><h4>Producing the Strategy Architecture</h4><div id="u2bArch"></div></div>\n'
            '<div class="step-panel">' +
            step_box('Step 2 &middot; Strategy Intent Statement', [
                'Read the four cards: what your WHAT, WHY, HOW and WHEN elements are saying.',
                'Deduce one crisp statement of your company\'s strategic ambition that carries the four, and type it in the box.',
                'Read the statement against your Architecture. Where it exposes a contradiction, resolve it in the Architecture first.']) +
            '<div id="u2bIntent"></div></div>\n'
            '<div class="step-panel">' +
            step_box('Step 3 &middot; Success in Practice', [
                'Open each of the four domains in turn.',
                'Answer the three questions of the domain for your company.',
                'Write one SiP statement for the domain from your answers.',
                'Read the four statements together and test them for depth and balance, with the SiP Flammables from 3.2 as the final balance check.']) +
            '<div id="u2bSip"></div></div>\n'
            '<div class="step-panel">' +
            step_box('the Group record', [
                'Read your group\'s full record: Strategy Architecture, Strategy Intent Statement and the four SiP statements.',
                'When it says what your group agreed, select <strong>Agree</strong> in the group record bar above. Every member agrees on their own page.',
                'When every member has agreed, the three outputs go into your team\'s Capstone Blueprint. You can print them as one report.',
                'If the scribe changes an entry after members have agreed, the agreements clear and every member agrees again.']) +
            '<div id="u2bRecord"></div></div>\n'
            '</div>\n')
    return tool

def section5_f():
    act = fnote('&#128203; PARTICIPANT ACTIVITY — 5.1',
                '<ol style="margin:6px 0 0 18px;">'
                '<li>The group works in 5.1 of its own participant pages. This is Capstone work. At the top, each member sees the group\'s simulated company, organisation, executive team and central problem from its Problem Charter (Unit 1, part 6.2).</li>'
                '<li>The group chooses its scribe for this work in the group record bar. The scribe types what the group agrees, and the entries appear on every member\'s page. The group can change the scribe at any time.</li>'
                '<li>Step 1 · Strategy Architecture: for each of the 14 elements the group answers the questions and writes what the element is saying. When all 14 are written, the scribe selects Bring the 14 elements together, and the group edits the Architecture under its five headings.</li>'
                '<li>Step 2 · Strategy Intent Statement: the group reads its WHAT, WHY, HOW and WHEN and deduces one crisp statement.</li>'
                '<li>Step 3 · Success in Practice: for each of the four domains the group answers the three questions and writes one statement.</li>'
                '<li>Group record: each member reads the full record and selects Agree. When every member has agreed, the three outputs go into the team\'s Capstone Blueprint (boxes 2A to 2F), and the group can print them as one report.</li>'
                '</ol>')
    return act

def main(pin, fin, pout, fout):
    p = rd(pin); f = rd(fin)
    els = element_questions(p); sipd = sip_domains(p)

    # ── PARTICIPANT ──
    _i = p.index('</style>'); p = p[:_i] + CSS + p[_i:]
    p = once(p, '<script src="/s2r-save.js"></script>', '<script src="/s2r-save.js"></script>\n<script src="/s2r-team.js"></script>')
    hero, body = section4(els, sipd, False)
    i = p.index('<div class="mod-panel" id="mod3">'); j = p.index('<div class="mod-nav">', i)
    p = p[:i] + '<div class="mod-panel" id="mod3">\n' + hero + '<div class="mod-body">\n' + body + '\n' + p[j:]

    i = p.index('<div class="mod-panel" id="mod4">'); j = p.index('<div class="slo-box">', i)
    p = p[:i] + ('<div class="mod-panel" id="mod4">\n<div class="mod-hero">\n  <p class="mod-hero-label">Section 5 · Application — In Practice</p>\n'
                 '  <h2>Build Your Company\'s Strategy</h2>\n  <p>With your group, build the Strategy Architecture, the Strategy Intent Statement and the Success in Practice of your simulated company.</p>\n'
                 '</div>\n<div class="mod-body">\n') + p[j:]
    i = p.index('<!-- ROLE CONTRIBUTION -->'); j = p.index('<div class="ref-block" style="margin-top:6px;">', i)
    e = p.index('id="app_ref_final-saved"', j)
    e = p.index('  </div>\n', e) + len('  </div>\n')
    ref = p[j:e]
    assert p[e:e+len('</div>\n</div>\n')] == '</div>\n</div>\n'
    k = e + len('</div>\n</div>\n')
    p = p[:i] + HOW5_P + '\n' + acc('5.1 — Your Company\'s Strategy', 'Architecture · Intent · SiP · Capstone Work', section5_p() + ref.rstrip('\n'), True) + p[k:]

    # summary
    p = re.sub(r'\{"arc": "Integration — Collective".*?\},\n', '{"arc": "Integration — Collective", "t": "What Was Shown", "body": "One worked example took Kestrel Point Services through the three connected outputs. Its Strategy Architecture: the integrated strategic logic constructed from the 14 elements, each stating what it is saying. Its Strategy Intent Statement: the crisp expression of its ambition deduced from WHAT, WHY, HOW and WHEN. Its Success in Practice: four statements describing what realising that ambition looks like across the organisation, tested for depth and balance."},\n', p, count=1, flags=re.S)
    p = re.sub(r'\{"arc": "Application — In Practice".*?\}\n\];', '{"arc": "Application — In Practice", "t": "What Was Built", "body": "With your group you built the same three outputs for your own simulated company: your Strategy Architecture, your Strategy Intent Statement and your Success in Practice. Every member agreed the group record, and the three outputs went into your team\'s Capstone Blueprint. The Architecture provides the logic. The Intent crystallises the ambition. Success in Practice makes the ambition observable. These outputs are the strategic foundation that later S2R® work carries into alignment, execution and performance."}\n];', p, count=1, flags=re.S)


    # Carol, 19 Oct 19:45: the 1.2 reflection comes off; the WHAT/WHY/HOW/WHEN tabs in 1.2 must switch with the panels
    i = p.index('  <div class="ref-block" style="margin-top:14px;">\n    <div class="ref-head"><span class="ref-icon">✍</span><span class="ref-label">&#x270E; Reflection &mdash; Strategy Intent</span></div>')
    j = p.index('<div class="ref-saved" id="ref2-saved">✓ Saved</div>\n  </div>\n', i) + len('<div class="ref-saved" id="ref2-saved">✓ Saved</div>\n  </div>\n')
    p = p[:i] + p[j:]
    p = once(p, "['ref1','ref2','ref4','ref6'].forEach(", "['ref1','ref4','ref6'].forEach(")
    p = once(p, '<div class="ph-tabs" id="w1hTabsP">', '<div class="ph-tabs" id="w1hPTabs">')

    # JS: replace the old tool and the role table with the new group build
    tool = open(os.path.join(HERE, 'u2b_tool.js'), encoding='utf-8').read()
    i = p.index('var U2={v:{},conf:[],cur:0,refine:{}};'); j = p.index('function u2RenderAll(){renderStep1();renderIntent();renderSip();refreshMirrors();}\n')
    p = p[:i] + tool + p[j + len('function u2RenderAll(){renderStep1();renderIntent();renderSip();refreshMirrors();}\n'):]
    p = once(p, 'var U2_FIELDS=["strategy_definition", "org_name", "strategy_period", "col_alignment", "col_gaps", "col_tensions", "col_ownership"];',
             'async function u2put(k,val){if(!window.S2R){console.warn(\'[unit2_m1_lens1_p] S2R helper not loaded\');return false;}return await S2R.save(\'u2m1_lens1\',k,val);}\nvar U2_FIELDS=["strategy_definition"];')
    p = once(p, '// ── Plain boxes: organisation, strategy period, Section 5.2 observations (id = response key) ──', '// ── Plain box: the opening definition of strategy (id = response key) ──')
    old_load = p[p.index('    // Section 4: Strategy Intent Design'):p.index('    if(typeof renderAppRoleSel===\'function\')renderAppRoleSel();\n    if(typeof renderAppForm===\'function\')renderAppForm();\n')]
    new_load = ('    // Section 5: the group\'s Strategy Intent Design (shared group record) and the opening definition\n'
                '    u2Fill(responses);\n'
                '    U2_FIELDS.forEach(function(id){\n'
                '      var el=document.getElementById(id);\n'
                '      if(el&&responses[id]!==undefined&&responses[id]!==null)el.value=responses[id];\n'
                '    });\n'
                '    u2RenderAll();\n'
                '    u2LoadCharter();\n'
                '    u2Attach();\n'
                '    // Section 5 reflection\n'
                '    [\'app_ref_final\'].forEach(function(id){\n'
                '      var key=\'app_\'+id;\n'
                '      var v=responses[key];\n'
                '      appResponsesP[key]=(v!==undefined&&v!==null)?v:\'\';\n'
                '      var el=document.getElementById(id);\n'
                '      if(el&&v!==undefined&&v!==null)el.value=v;\n'
                '    });\n')
    p = p.replace(old_load, new_load, 1)
    p = once(p, "    if(typeof renderAppRoleSel==='function')renderAppRoleSel();\n    if(typeof renderAppForm==='function')renderAppForm();\n", '')
    i = p.index('// ── SECTION 5.1: ROLE CONTRIBUTION TABLE ──'); j = p.index('var appRoleP=\'\';', i)
    p = p[:i] + '// ── SECTION 5 REFLECTION ──────────────────────────────────────────────────\n' + p[j:]
    i = p.index('function renderAppRoleSel(){'); j = p.index('renderAppRoleSel();renderAppForm();\n', i)
    p = p[:i] + p[j + len('renderAppRoleSel();renderAppForm();\n'):]
    p = once(p, "var appRoleP='';\nvar appStoreP={};\n", '')

    # ── FACILITATOR ──
    _i = f.index('</style>'); f = f[:_i] + CSS + f[_i:]
    hero, body = section4(els, sipd, True)
    i = f.index('<p class="mod-hero-label">Section 4 · Integration — Collective</p>'); i = f.rindex('<div class="mod-hero">', 0, i)
    j = f.index('<div class="mod-nav">', i)
    # keep the old 4.x facilitator reference blocks for Section 5
    old4 = f[i:j]
    f = f[:i] + hero + '<div class="mod-body">\n' + body + '\n' + f[j:]

    def piece(src, start, end):
        a = src.index(start); b = src.index(end, a); return src[a:b]
    elements_ref = piece(old4, '<p>The 14 elements follow the Strategy2Results® definition of strategy.', '<h4>The Strategy Architecture Output</h4>')
    arch_ref = piece(old4, '<h4>The Strategy Architecture Output</h4>', '</div>\n</div>\n\n<!-- STEP 2')
    dims_ref = piece(old4, '<p>The four dimensions brought forward from the architecture:</p>', '</div>\n</div>\n\n<!-- STEP 3')
    sip_ref = piece(old4, '<div class="quote"><p>"If our Strategy Intent is successful, what should we see in practice?"</p></div>\n  <p>Click each domain', '</div>\n</div>\n\n<div class="mod-nav">' if '</div>\n</div>\n\n<div class="mod-nav">' in old4 else '</div>\n</div>\n')
    elements_ref = elements_ref.replace('OUTPUT, the first concept in 1.1, is what the 14 elements produce: the Strategy Architecture. Click each element to expand.', 'OUTPUT, the first concept in 1.1, is what the 14 elements produce: the Strategy Architecture. Click each element to see the guide and questions participants see beside the boxes.')
    arch_ref = arch_ref.replace('The page brings the 14 confirmed elements together under five headings. The group refines the text until it accurately represents the organisation\'s strategic architecture.',
                                'When all 14 elements are written, the scribe brings them together under five headings. The group edits the text until it represents the strategic architecture it intends.')

    i = f.index('<p class="mod-hero-label">Section 5 · Application — In Practice</p>'); i = f.rindex('<div class="mod-hero">', 0, i)
    j = f.index('<div class="slo-box">', i)
    f = f[:i] + ('<div class="mod-hero">\n  <p class="mod-hero-label">Section 5 · Application — In Practice</p>\n'
                 '  <h2>Build Your Company\'s Strategy</h2>\n  <p>Each group builds the Strategy Architecture, the Strategy Intent Statement and the Success in Practice of its simulated company.</p>\n'
                 '</div>\n<div class="mod-body">\n') + f[j:]
    i = f.index('<div class="fac-note-full" style="margin-top:22px;"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Section 5 · Application</div>')
    k = f.index('<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">Unit Summary</span>', i)
    g5 = fnote('&#9670; FACILITATOR GUIDANCE — Section 5 · Application',
               '<p><strong>Section intent:</strong> This is the production section of the unit and the group\'s Capstone work. Each group now builds the Strategy Intent Design of the simulated company it created in its Problem Charter. The work happens collectively because strategy requires more than agreement with a finished statement: leaders contribute to the thinking, surface different interpretations, work through tensions and arrive at a position they can collectively own.</p>'
               '<p>Each group works through three connected steps, in order: Strategy Architecture → Strategy Intent → Success in Practice. Section 4 showed each step completed for Kestrel Point Services; groups can return to it at any point.</p>'
               '<p><strong>Working in groups:</strong> participants work in their assigned groups. Encourage groups to surface differences before resolving them: different interpretations expose assumptions, trade-offs and places where the strategic thinking is not yet coherent. The group chooses its scribe for this work, and can choose a different scribe for each assignment.</p>'
               '<p><strong>Your role:</strong> guide how the work is completed. This is Capstone work and is assessed independently at the capstone.</p>')
    how5 = ('<div class="u2w-how"><div class="u2w-how-h">How Section 5 works</div>'
            '<p>This is group work and Capstone work. Each group builds three outputs for the simulated company of its Problem Charter: Step 1 Strategy Architecture, Step 2 Strategy Intent Statement, Step 3 Success in Practice.</p>'
            '<p>The group chooses its scribe for this work. The scribe types what the group agrees, and the entries appear on every member\'s page. In the Group record tab each member reads the record and selects Agree. When every member has agreed, the three outputs go into the team\'s Capstone Blueprint.</p></div>')
    s1 = fnote('&#9670; FACILITATOR GUIDANCE — Step 1 · Strategy Architecture',
               '<p>Step 1 is the foundation. The group establishes the thinking and logic underneath its company\'s strategic position before expressing that position concisely.</p>'
               '<p>Remind participants that the elements are interconnected: the value the company intends to create must be supported by its HOW; its WHEN must reflect the capabilities that need to be built; its approach to sustaining value must respond to the forces in its operating environment.</p>'
               '<p>Encourage groups to answer with actual strategic choices and to leave broad aspirations out. After the questions of an element, the group writes what the element is saying in one or two sentences and asks: <em>"Is this what we mean?"</em></p>'
               '<p>When all 14 are written, the group reads them as one strategic system: <em>"What is this architecture collectively saying about our company\'s strategy?"</em> The six questions in the lesson beside the boxes guide that reading: whether the choices reinforce one another, where tensions remain, whether the HOW supports what has been chosen, whether timing reflects capability and environment, whether value is created, delivered and sustained, and whether the architecture represents the position the group intends.</p>')
    s2 = fnote('&#9670; FACILITATOR GUIDANCE — Step 2 · Strategy Intent Statement',
               '<p>The group crystallises its Architecture into one Strategy Intent Statement. The Architecture holds the depth. The Intent gives the clarity.</p>'
               '<p>Protect the Intent from overload: participants may try to carry every important point from the Architecture into the statement. The Architecture already holds that detail. A strong Intent lets a leader understand the company\'s strategic position without a paragraph of explanation.</p>'
               '<p>The group reads its statement against its Architecture: <em>"Does this statement faithfully express the strategic ambition contained in our Architecture?"</em> Where the statement exposes a contradiction, the group resolves it in the Architecture before finalising the Intent.</p>')
    s3 = fnote('&#9670; FACILITATOR GUIDANCE — Step 3 · Success in Practice',
               '<p>Position the group inside the future its Strategy Intent describes, with one central question: <em>"If our Strategy Intent is successful, what should we see in practice?"</em></p>'
               '<p>For each domain the group answers the three questions and writes one statement from its answers. The observable indicators from Section 3 deepen the discussion; the statement stays focused on the group\'s own Intent. Generic descriptions of a successful organisation have no place in it.</p>'
               '<p>When the four statements are written, the group reads them as one Success in Practice and tests them for depth and balance, with the SiP Flammables as the final balance check.</p>')
    s4 = fnote('&#9670; FACILITATOR GUIDANCE — Group record',
               '<p>Each member reads the full record and selects Agree on their own page. The page shows who has agreed. When every member has agreed, the three outputs go into the team\'s Capstone Blueprint, boxes 2A to 2F, and the group can print them as one report: Strategy Architecture → Strategy Intent → Success in Practice.</p>')
    b51 = (section5_f() + '\n<h4>Step 1 · Strategy Architecture</h4>\n' + s1 + '\n  ' + elements_ref + arch_ref +
           '\n<h4>Step 2 · Strategy Intent Statement</h4>\n' + s2 + '\n  ' + dims_ref +
           '\n<h4>Step 3 · Success in Practice</h4>\n' + s3 + '\n  ' + sip_ref +
           '\n<h4>Group record</h4>\n' + s4)
    f = f[:i] + g5 + '\n\n' + how5 + '\n' + acc('5.1 — Your Company\'s Strategy', 'Architecture · Intent · SiP · Capstone Work', b51, True) + '\n' + f[k:]
    f = f.replace('<li>A role contribution row from each participant</li>', '')
    f = f.replace('<li>A Strategy Architecture output from each group</li><li>A confirmed Strategy Intent Statement from each group</li><li>Four confirmed SiP statements from each group</li>',
                  '<li>A Strategy Architecture from each group</li><li>A Strategy Intent Statement from each group</li><li>Four SiP statements from each group, agreed by every member</li>')


    # Facilitator Guide tab and summary follow the new Sections 4 and 5
    F_REPL = [
        ('Protect the time in Section 4 for each group to build them in that order.', 'Section 4 shows them completed once for Kestrel Point Services. Protect the time in Section 5 for each group to build them for its own company, in that order.'),
        ('Participants derive their own statement in Section 4; here they learn what it brings forward.', 'Participants derive their own statement in Section 5; here they learn what it brings forward.'),
        ('<li><strong>Sections 1 and 4 &middot; Strategy Architecture:</strong>', '<li><strong>Sections 1, 4 and 5 &middot; Strategy Architecture:</strong>'),
        ('<li><strong>1.3, Section 3 and 4.3 &middot; Success in Practice:</strong>', '<li><strong>1.3, Section 3, 4.3 and 5.1 &middot; Success in Practice:</strong>'),
        ('<li><strong>Section 5 &middot; Role contribution:</strong> <em>&ldquo;From my executive role, what must I contribute for this Success in Practice to become real?&rdquo;</em></li>',
         '<li><strong>Section 5 &middot; Strategy Intent Statement:</strong> <em>&ldquo;Does this statement faithfully express the strategic ambition contained in our Architecture?&rdquo;</em></li>'),
        ('<p><strong>4.2 &middot; Strategy Intent Statement.</strong>', '<p><strong>5.1 Step 2 &middot; Strategy Intent Statement.</strong>'),
        ('<p><strong>4.3 &middot; Success in Practice.</strong>', '<p><strong>5.1 Step 3 &middot; Success in Practice.</strong>'),
        ('<p><strong>4.3 &middot; Balance.</strong>', '<p><strong>5.1 Step 3 &middot; Balance.</strong>'),
        ('<p><strong>5.1 &middot; Role contribution.</strong> Each contribution names what the role does for the Success in Practice. Ask: <em>&ldquo;What does this role specifically decide, enable, coordinate, resource, protect or change?&rdquo;</em></p>',
         '<p><strong>5.1 &middot; Group record.</strong> The group chooses a scribe for the work and can choose a different scribe for each assignment. Each member reads the record and selects Agree on their own page.</p>'),
    ]
    for a, b in F_REPL:
        f = once(f, a, b)
    f = re.sub(r'\{"arc": "Integration — Collective".*?\},\n', '{"arc": "Integration — Collective", "t": "What Was Shown", "body": "One worked example took Kestrel Point Services through the three connected outputs. Its Strategy Architecture: the integrated strategic logic constructed from the 14 elements, each stating what it is saying. Its Strategy Intent Statement: the crisp expression of its ambition deduced from WHAT, WHY, HOW and WHEN. Its Success in Practice: four statements describing what realising that ambition looks like across the organisation, tested for depth and balance."},\n', f, count=1, flags=re.S)
    f = re.sub(r'\{"arc": "Application — In Practice".*?\}\n\];', '{"arc": "Application — In Practice", "t": "What Was Built", "body": "Each group built the same three outputs for its own simulated company: its Strategy Architecture, its Strategy Intent Statement and its Success in Practice. Every member agreed the group record, and the three outputs went into the team\'s Capstone Blueprint. The Architecture provides the logic. The Intent crystallises the ambition. Success in Practice makes the ambition observable. These outputs are the strategic foundation that later S2R® work carries into alignment, execution and performance."}\n];', f, count=1, flags=re.S)

    wr(pout, p); wr(fout, f)

if __name__ == '__main__':
    main(*sys.argv[1:5])
