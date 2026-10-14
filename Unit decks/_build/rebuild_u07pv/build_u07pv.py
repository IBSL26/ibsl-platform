# -*- coding: utf-8 -*-
"""Unit 7 · the two performance views (Carol's "Unit 7 Amended content.docx", 14 October 2026).
Usage: python3 build_u07pv.py <p before> <f before> <p out> <f out>
Input: the live pages (backups "… - before two performance views (14 Oct)").
Every replacement checks that it finds its place exactly once. CRLF and UTF-8 are kept."""
import sys, re, json, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u7pv_content as C
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'


def rd(p): return open(p, encoding='utf-8', newline='').read()
def crlf(s): return s.replace('\r\n', '\n').replace('\n', '\r\n')


def once(t, a, b):
    n = t.count(a)
    assert n == 1, 'expected once (%d): %s' % (n, a[:120])
    return t.replace(a, b)


def esc(s): return html.escape(s, quote=True)


def hc(cards, col=None):
    cols = ['#8ab0e8', '#5ecba1', '#c39de0']
    return '<div class="u7v-hc">' + ''.join(
        '<div class="u7v-hc-c" style="border-top-color:%s;"><div class="u7v-hc-n" style="color:%s;">%s</div><div class="u7v-hc-t">%s</div><div class="u7v-hc-b">%s</div></div>'
        % (cols[i % 3], cols[i % 3], c[0], c[1], c[2]) for i, c in enumerate(cards)) + '</div>'


def acc_block(t, title_start):
    """The whole <div class="acc…"> … part whose title begins with title_start, up to the next part or the section nav."""
    key = 'class="acc-t">' + title_start
    assert t.count(key) == 1, 'part not found once: ' + title_start
    i = t.index(key)
    s = max(t.rfind('<div class="acc">', 0, i), t.rfind('<div class="acc open">', 0, i))
    m = re.compile(r'\r\n\r\n<div class="acc(?: open)?">|\r\n<div class="mod-nav"').search(t, i)
    return t[s:m.start()]


def build(v, t):
    you = v == 'p'
    # ═══ Header ═══
    if not you:
        t = once(t, '<div class="unit-sub">Turning Delivery Goals into Genuine Ownership</div>', '<div class="unit-sub">%s</div>' % C.SUB_F)
    m = re.search(r'<p class="unit-desc">.*?</p>', t); assert m
    t = t[:m.start()] + '<p class="unit-desc">%s</p>' % C.DESC[v] + t[m.end():]
    m = re.search(r'(<span class="klo-label">Key learning outcomes</span>\r\n)((?:      <span class="klo">.*?</span>\r\n){4})', t); assert m
    t = t[:m.start(2)] + ''.join('      <span class="klo">%s</span>\r\n' % k for k in C.KLO) + t[m.end(2):]
    # ═══ Section outcomes ═══
    slos = list(re.finditer(r'<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>.*?</ul></div>', t))
    assert len(slos) == 5, len(slos)
    for k, mm in reversed(list(enumerate(slos))):
        t = t[:mm.start()] + '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>' + ''.join('<li>%s</li>' % s for s in C.SLO[k]) + '</ul></div>' + t[mm.end():]
    # ═══ Facilitator Guide ═══
    if not you:
        a = 'genuine human commitment to deliver it.</p></div>'
        t = once(t, a, 'genuine human commitment to deliver it.</p>' + NL + '<p>%s</p></div>' % C.INTENT_ADD)
        t = once(t, C.APP_OLD, C.APP_NEW)
    # ═══ 1.1 ═══
    views = '<p>%s</p>' % C.V11[v] + NL + hc(C.V11_CARDS) + NL + '<p><strong>%s</strong></p>' % C.V11_TAIL
    if you:
        a = 'accept ownership of the result.</em></p></div>\r\n<table'
        t = once(t, a, 'accept ownership of the result.</em></p></div>' + NL + views + NL + '<table')
    else:
        a = '<p>The performance management and accountability frameworks and structures have been established. The delivery goals have been defined. The targets have been set.</p>\r\n'
        t = once(t, a, a + views + NL)
    TD0 = '<td style="padding:10px 14px;color:rgba(255,255,255,.35);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;">%s</td>'
    TD = '<td style="padding:10px 14px;color:rgba(255,255,255,.7);">%s</td>'
    row = '<tr style="border-bottom:1px solid rgba(255,255,255,.05);">' + TD0 % C.ROW11[0] + TD % C.ROW11[1] + TD % C.ROW11[2] + '</tr>' + NL
    a = '<tr><td style="padding:10px 14px;color:rgba(255,255,255,.35);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;">Accountability</td>'
    t = once(t, a, row + a)
    # ═══ 1.2 ═══
    b12 = acc_block(t, '1.2 &mdash;')
    i = b12.index('<p>When expectations are properly established'); j = b12.index('</div>\r\n</div>', b12.index('<div class="principle-stack">'))
    nums = re.findall(r'<div class="p-num" style="color:[^"]+;">Condition \d</div>', b12); assert len(nums) == 3
    intro, systems, lead, conds, principle = C.P12(v)
    cards = []
    for k, (nm, q, body) in enumerate(conds):
        cards.append('<div class="p-card%s" onclick="toggleP(this)"><div class="p-head"><div class="p-meta">%s<div class="p-name">%s &mdash; %s</div></div><div class="p-arr">&#9660;</div></div><div class="p-body">%s</div></div>'
                     % (' open' if k == 0 else '', nums[k], nm, q, body))
    new12 = (NL.join('<p>%s</p>' % s for s in intro) + NL + hc([(n_, '', d_) for n_, d_ in systems]).replace('<div class="u7v-hc-t"></div>', '') + NL +
             '<p>%s</p>' % lead + NL + '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>' + NL + '<div class="hbox"><p>%s</p></div>' % principle)
    nb12 = b12[:i] + new12 + b12[j + len('</div>\r\n</div>'):]
    t = once(t, b12, nb12)
    # ═══ 1.3 ═══
    b13 = acc_block(t, '1.3 &mdash;')
    cols = ['#8ab0e8', 'var(--teall)' if you else 'var(--gold)', '#5ecba1']
    gcls = 'scarf-grid' if you else 'aceit-grid'
    gi = b13.index('<div class="%s"' % gcls); gj = b13.index('\r\n</div>', b13.rindex('<div class="%s' % ('sc-card' if you else 'ai-card'))) + len('\r\n</div>')
    if you:
        grid = '<div class="scarf-grid" style="grid-template-columns:repeat(3,1fr);">' + NL + NL.join(
            '<div class="sc-card%s" onclick="toggleSC(this)"><div class="sc-head"><div class="sc-trigger" style="color:%s;">%s %s</div><div class="sc-q">%s</div></div><div class="sc-bar" style="background:%s;"></div><div class="sc-body">'
            '<div class="sc-row"><div class="sc-rl">What must be established</div><div class="sc-rt">%s</div></div><div class="sc-row"><div class="sc-rl">Examples</div><div class="sc-rt">%s</div></div><div class="sc-row"><div class="sc-rl">Key question</div><div class="sc-rt"><em>%s</em></div></div></div></div>'
            % (' open' if k == 0 else '', cols[k], a_, nm, who, cols[k], est, ex, q) for k, (a_, nm, who, est, ex, q) in enumerate(C.CHAINS)) + NL + '</div>'
    else:
        bars = ['<div class="ai-bar" style="background:rgba(107,143,204,.4);"></div>', '<div class="ai-bar"></div>', '<div class="ai-bar"></div>']
        grid = '<div class="aceit-grid" style="grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0;">' + NL + NL.join(
            '<div class="ai-card%s" onclick="toggleAI(this)"><div class="ai-head"><div><div class="ai-letter" style="color:%s;font-size:1.5rem;">%s</div><div class="ai-name">%s</div></div><div class="ai-arr">&#9660;</div></div>%s<div class="ai-body">'
            '<div class="ai-row"><div class="ai-rl">Who</div><div class="ai-rt">%s</div></div><div class="ai-row"><div class="ai-rl">What must be established</div><div class="ai-rt">%s</div></div>'
            '<div class="ai-row"><div class="ai-rl">Examples</div><div class="ai-rt">%s</div></div><div class="ai-row"><div class="ai-rl">Key question</div><div class="ai-rt"><em>%s</em></div></div></div></div>'
            % (' open' if k == 0 else '', cols[k], a_, nm, bars[k], who, est, ex, q) for k, (a_, nm, who, est, ex, q) in enumerate(C.CHAINS)) + NL + '</div>'
    dist = '<h4>The Critical Distinction</h4>' + NL + hc([(n_, ex_, '<p>' + tail_ + '</p>') for n_, ex_, tail_ in C.DIST_13]).replace('<div class="u7v-hc-t">', '<div class="u7v-hc-t u7v-q">')
    new13 = ('<div class="hbox"><p>%s</p></div>' % C.CENTRAL_13 + NL + '<p>%s</p>' % C.USES_13[v] + NL + grid + NL + '<p>%s</p>' % C.OUTPUT_13 + NL + dist)
    nb13 = b13[:gi] + new13 + b13[gj:]
    if you:
        nb13 = once(nb13, '&#10;External: ...', '&#10;Crossline: ...')
    else:
        nb13 = once(nb13, 'one contributor from each chain: Upline, Downline and External.', 'one contributor from each direction: Upline, Downline and Crossline.')
    t = once(t, b13, nb13)
    # ═══ 1.4 ═══
    a = ('the leader conducts' if not you else 'you conduct') + ' an Alignment Dialogue with the individuals responsible for delivering the Key Result or KPI. This is a structured conversation designed to test whether the expectation has moved from instruction to commitment.</p>\r\n'
    t = once(t, a, a + NL.join('<p>%s</p>' % s for s in C.V14[v]) + NL)
    if not you:
        t = once(t, 'Participants practise it in the role play of part 4.2.', 'Participants practise it in the role play of part 4.1.')
    # ═══ 2.1 · 2.3 ═══
    m = re.search(r'<p>Strategy is ultimately delivered through human commitment\..*?</p>\r\n', t); assert m and t.count('<p>Strategy is ultimately delivered') == 1
    t = t[:m.end()] + '<p>%s</p>' % C.V21 + NL + t[m.end():]
    a = '<p>When expectations are set without being established, two organisational conditions degrade in a predictable sequence.</p>\r\n'
    t = once(t, a, a + '<div class="hbox"><p>%s</p></div>' % C.V23[v] + NL)
    # ═══ 3.1 ═══
    if you:
        m = re.search(r'<p>Each executive function communicates expectations through the mechanisms it controls\..*?</p>\r\n', t)
        assert m; t = t[:m.end()] + '<p>%s</p>' % C.V31['p'] + NL + '<div class="hbox"><p>%s</p></div>' % C.Q31_P + NL + t[m.end():]
    else:
        m = re.search(r'<p>Each CXO role naturally focuses on the mechanisms it controls:.*?</p>\r\n', t)
        assert m; t = t[:m.end()] + '<p>%s</p>' % C.V31['f'] + NL + t[m.end():]
        a = '<p>Teach each participant’s own role first, then the two roles closest to it.'
        t = once(t, a, '<p>%s</p>' % C.Q31_F + NL + a)
    chains = re.findall(r'<div><b>&#8596; External</b>([^<]*)</div>', t)
    assert len(chains) == 10, len(chains)
    roles = list(C.CROSSLINE.keys())
    for k, old in enumerate(chains):
        t = once(t, '<div><b>&#8596; External</b>%s</div>' % old, '<div><b>&#8596; Crossline</b>%s</div>' % C.CROSSLINE[roles[k]])
    # ═══ Section 4 ═══
    m = re.search(r'(<div class="mod-hero-label">Section 4 · Integration — Collective</div><h2>[^<]*</h2><p>)(.*?)(</p>)', t); assert m
    t = t[:m.start(2)] + C.S4_HERO[v] + t[m.end(2):]
    b41 = acc_block(t, '4.1 &mdash;')
    t = once(t, b41 + '\r\n\r\n', '')
    t = once(t, '<div class="acc">\r\n<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">4.2 &mdash; Practising the Alignment Dialogue',
             '<div class="acc open">\r\n<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">4.1 &mdash; Practising the Alignment Dialogue')
    if you:
        t = once(t, 'In part 4.2 you prepared this dialogue on your own.', 'In part 4.1 you prepared this dialogue on your own.')
        m = re.search(r'<p>This is Portfolio work\. Your entries save as you type\. They become part of your Learning Portfolio[^<]*</p>', t)
        if m: t = t[:m.start()] + t[m.end():]
    else:
        t = once(t, 'Use the example of part 4.1, <em>“Reduce complaint resolution time from 48 hours to 12 hours”</em>,', 'Use the example <em>“Reduce complaint resolution time from 48 hours to 12 hours”</em>,')
        t = once(t, 'Two briefs for the part 4.1 example are below.', 'Two briefs for this example are below.')
        t = once(t, 'On the portal, in part 4.2, you prepare', 'On the portal, in part 4.1, you prepare')
        t = once(t, 'Each participant completes part 4.2 of their own file alone', 'Each participant completes part 4.1 of their own file alone')
        t = once(t, 'In part 4.2 each participant prepared this dialogue alone.', 'In part 4.1 each participant prepared this dialogue alone.')
    # ═══ Section 5 ═══
    m = re.search(r'(<div class="mod-hero-label">Section 5 · Application — In Practice</div><h2>[^<]*</h2><p>)(.*?)(</p>)', t); assert m
    t = t[:m.start(2)] + C.S5_HERO[v] + t[m.end(2):]
    m = re.search(r'<li><strong>5\.1 · Building the Expectation Architecture\.</strong>.*?</li>', t); assert m
    t = t[:m.start()] + '<li>%s</li>' % C.HOW_S5_STEP1[v] + t[m.end():]
    b51 = acc_block(t, '5.1 &mdash;')
    t = once(t, b51, s51_p() if you else s51_f(b51))
    if not you:
        m = re.search(r'<p><strong>Before the group starts:</strong>.*?</p>', t); assert m
        t = t[:m.start()] + '<p>%s</p>' % C.GUIDE_BEFORE + t[m.end():]
        a = '<p><strong>To finish:</strong>'
        t = once(t, a, '<p>%s</p>' % C.GUIDE_DONE + NL + a)
    # ═══ Summary ═══
    if you:
        m = re.search(r'var SUMMARY=\[\r?\n(.*?)\r?\n\];', t, re.S); assert m
        items = re.findall(r'\{arc:"(.*?)",title:"(.*?)",body:"(.*?)"\}', m.group(1)); assert len(items) == 5
        dec = lambda s: json.loads('"' + s + '"')
        items = [[dec(a_), dec(b_), dec(c_)] for a_, b_, c_ in items]
        for old, new in C.SUM_P[0]:
            assert items[0][2].count(old) == 1, old; items[0][2] = items[0][2].replace(old, new)
        items[3][1] = C.SUM_P_4_TITLE; items[3][2] = C.SUM_P_4
        items[4][2] = C.SUM_P_5
        body = ',\n'.join('{arc:%s,title:%s,body:%s}' % (json.dumps(a_), json.dumps(b_), json.dumps(c_)) for a_, b_, c_ in items)
        t = t[:m.start(1)] + crlf(body) + t[m.end(1):]
        t = once(t, 'var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref7","ref8",', 'var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref8",')
    else:
        t = once(t, C.SUM_F_5_OLD, C.SUM_F_5_NEW)
    # ═══ CSS, JS ═══
    k = t.index('</style>')
    t = t[:k] + crlf(rd(os.path.join(HERE, 'u7pv.css'))) + t[k:]
    if you:
        i = t.index('/* ════════════ UNIT 7 · SECTION 5 · ESTABLISHING DELIVERY EXPECTATIONS')
        end = "  u7Fill();u7RecDraw();u7AdDraw();\r\n});\r\n"
        j = t.index(end, i) + len(end)
        js = rd(os.path.join(HERE, 'u7pv_p.js'))
        js = js.replace('/*FIELDS*/[]', json.dumps(fields(), ensure_ascii=False)).replace('/*PARTS*/[]', json.dumps(PARTS, ensure_ascii=False))
        t = t[:i] + crlf(js) + t[j:]
    return t


PARTS = [
    ('future', 'Start With the Future', 'Expectations · Start With the Future', 'ex_future', '5.1 · Step 1 · Start With the Future'),
    ('delivery', 'Clarify the Delivery Expectation', 'Expectations · Delivery Expectation', 'ex_delivery', '5.1 · Step 2 · Clarify the Delivery Expectation'),
    ('chain', 'Identify the Expectations Chain', 'Expectations · Expectations Chain', 'ex_chain', '5.1 · Step 3 · Identify the Expectations Chain'),
    ('own', 'Confirm Ownership', 'Expectations · Ownership', 'ex_ownership', '5.1 · Step 4 · Confirm Ownership'),
    ('dialogue', 'Alignment Dialogue with the Board Chair', 'Expectations · Alignment Dialogue', 'ex_dialogue', '5.2 · Alignment Dialogue with the Board Chair'),
]
DG = [('dg_goal', 'Goal'), ('dg_reality', 'Reality'), ('dg_options', 'Options'), ('dg_will', 'Will')]


def fields():
    out = []
    for n in (1, 2):
        for fid, label, part, kind, ph, grp in C.FIELD_DEFS:
            out.append(['o%d_%s' % (n, fid), label, part, 'Contribution %d' % n, kind])
    out.append(['dg_kr', 'Key Result', 'dialogue', 'Board chair', 'k'])
    for key, short in DG: out.append([key, short, 'dialogue', 'Board chair', ''])
    return out


ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'


def head51():
    return ('<div class="acc open">' + NL + '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">Four steps &middot; Capstone Work</div></div>%s</div>' % (C.T51, ARR) + NL +
            '<div class="acc-b"><div class="cb">' + NL + '<div class="step-tabs">' + NL +
            NL.join('  <div class="step-tab%s" onclick="u7Step(%d)"><div class="step-num">Step %d</div><div class="step-name">%s</div></div>' % (' active' if k == 0 else '', k, k + 1, s) for k, s in enumerate(C.STEPS)) + NL + '</div>' + NL)


def lesson(k):
    return '<div class="u7-s5-g">' + ''.join('<p><b>%s</b>%s</p>' % (a, b) for a, b in C.LESSON[k]) + '</div>'


FD = {f[0]: f for f in C.FIELD_DEFS}


def ta(n, fid, tall=False):
    f = FD[fid]; i = 'o%d_%s' % (n, fid)
    return '<label class="wp-label" for="u7_%s">%s</label><textarea class="wp-ta" id="u7_%s" data-u7="%s" placeholder="%s"%s></textarea>' % (i, f[1], i, i, esc(f[4]), ' style="min-height:96px;"' if tall else '')


def num(n, fid):
    f = FD[fid]; i = 'o%d_%s' % (n, fid)
    return '<label class="wp-label" for="u7_%s">%s</label><input type="number" min="1" max="10" step="1" class="u7-num" id="u7_%s" data-u7="%s" placeholder="1&ndash;10">' % (i, f[1], i, i)


def okr(n):
    return '<div class="u7-okr"><div><b>Contribution</b><span class="u7-o%d-obj"></span></div><div><b>Key Result</b><span class="u7-o%d-kr"></span></div></div>' % (n, n)


def box(n, inner):
    return '<div class="u7-s5">' + NL + '  <div class="u7-s5-h"><span class="u7-s5-n">Contribution %d</span></div>' % n + NL + '  ' + inner + NL + '</div>'


def how(k):
    return '<div class="u7-how"><div class="u7-how-h">Capstone work &middot; How to complete Step %d &middot; %s</div><ol>%s</ol></div>' % (k + 1, C.STEPS[k], ''.join('<li>%s</li>' % s for s in C.HOW_STEP_P[k]))


def s51_p():
    o = [head51()]
    # Step 1
    o.append('<div class="step-panel active" id="u7sp1">' + NL + how(0) + NL +
             '<div class="u7-btnrow" style="margin:0 0 4px;"><button type="button" class="u7-b" onclick="u7Bring(true)">Reload the drop-down lists</button></div><div class="u7-note" id="u7BringMsg" style="display:none;"></div>' + NL +
             '<div class="u7-h">The lesson for this step</div>' + NL + lesson(0))
    for n in (1, 2):
        o.append(box(n, '<label class="wp-label" for="u7_o%d_fn">Contribution %d · a function of your Contribution Map</label><select class="u7-sel" id="u7_o%d_fn" data-u7="o%d_fn"></select>' % (n, n, n, n) +
                     '<div class="u7-okr u7v-kr"><div><b>Key Result</b><span class="u7-o%d-kr"></span></div></div>' % n +
                     '<label class="wp-label" for="u7_o%d_sipst">The Success in Practice statement it serves</label><select class="u7-sel" id="u7_o%d_sipst" data-u7="o%d_sipst"></select>' % (n, n, n) +
                     ta(n, 'owner') + ta(n, 'sip') + ta(n, 'frame', True)))
    o.append('</div>')
    # Step 2
    o.append('<div class="step-panel" id="u7sp2">' + NL + how(1) + NL + '<div class="u7-h">The lesson for this step</div>' + NL + lesson(1))
    for n in (1, 2):
        o.append(box(n, okr(n) + '<div class="u7v-map" id="u7v_map%d"></div>' % n +
                     '<div class="u7v-sh">For the people &middot; Human Operating System</div>' + ta(n, 'what') +
                     '<div class="u7-g3"><div>%s</div><div>%s</div><div>%s</div></div>' % (ta(n, 'when'), ta(n, 'std'), ta(n, 'evid')) + ta(n, 'beh') +
                     '<div class="u7v-sh">For the organisation &middot; ESRG</div>' +
                     '<div class="u7-g2"><div>%s</div><div>%s</div></div><div class="u7-g2"><div>%s</div><div>%s</div></div>' % (ta(n, 'env'), ta(n, 'sys'), ta(n, 'res'), ta(n, 'gov'))))
    o.append('</div>')
    # Step 3
    o.append('<div class="step-panel" id="u7sp3">' + NL + how(2) + NL + '<div class="u7-h">The lesson for this step</div>' + NL + lesson(2))
    arrows = {'up': '&#8593; ', 'down': '&#8595; ', 'cross': '&#8596; '}
    for n in (1, 2):
        rows = ''
        for d in ('up', 'down', 'cross'):
            a_ = ta(n, d).replace('">%s</label>' % FD[d][1], '">%s%s</label>' % (arrows[d], FD[d][1].replace(' · ', ' &middot; ')))
            rows += '<div class="u7-chainrow"><div>%s</div><div>%s</div></div>' % (a_, ta(n, d + '_r'))
        o.append(box(n, okr(n) + rows + ta(n, 'coord')))
    o.append('</div>')
    # Step 4
    o.append('<div class="step-panel" id="u7sp4">' + NL + how(3) + NL + '<div class="u7-h">The lesson for this step</div>' + NL + lesson(3))
    for n in (1, 2):
        o.append(box(n, okr(n) + num(n, 'score') + ta(n, 'concern') + ta(n, 'act') + num(n, 'score2')))
    o.append('</div>')
    return NL.join(o) + NL + '</div></div></div>'


def s51_f(old):
    o = [head51()]
    for k in range(4):
        o.append('<div class="step-panel%s" id="u7sp%d">' % (' active' if k == 0 else '', k + 1) + NL +
                 '<div class="u7-h">The lesson participants see in Step %d</div>' % (k + 1) + NL + lesson(k) + NL +
                 '<div class="u7-h">What each group completes in Step %d</div>' % (k + 1) + NL +
                 '<ul class="u7-list">' + ''.join('<li>%s</li>' % s for s in C.COMPLETES_F[k]) + '</ul>' + NL + '</div>')
    o.append('</div>')
    act = re.search(r'<div class="fac-note-full u7-activity">.*?</div>\r\n', old, re.S).group(0)
    return NL.join(o) + NL + act + '</div></div>'


if __name__ == '__main__':
    p_src, f_src, p_out, f_out = sys.argv[1:5]
    p = build('p', rd(p_src)); f = build('f', rd(f_src))
    for out, s in ((p_out, p), (f_out, f)):
        assert '\n' not in s.replace('\r\n', '')
        open(out, 'w', encoding='utf-8', newline='').write(s)
    print('built', p_out, f_out)
