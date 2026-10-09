# -*- coding: utf-8 -*-
"""Unit 6 · Performance Management Setup — builds the amended participant and facilitator pages (Carol's amendments of 9 October 2026).
Usage: python3 build_u06.py <participant page before> <facilitator page before> <participant out> <facilitator out>
Input: Claude outputs\\Backups\\Unit 6 file backups\\unit3_m1_lens5_[p|f] - before amendments (9 Oct).html
Every part is taken from the old page or built from u6_content.py. Each cut and each replacement checks that it finds its place exactly once and stops on a miss.
Line endings stay CRLF, encoding UTF-8. IDs of the answers that remain (ref1, ref2, ref3, ref4, ref6, ref7) and the lens id are unchanged."""
import sys, re, json, html, os
import u6_content as C
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'
def read(p): return open(p, encoding='utf-8', newline='').read()
def crlf(s): return s.replace('\r\n', '\n').replace('\n', '\r\n')
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:90]); return t.replace(a, b)
NEXT = re.compile(r'\r\n<div class="acc(?: open)?"(?: id="[^"]*")?(?: style="[^"]*")?>\r\n|<div class="mod-nav"|<!-- APPLICATION REFLECTION|<!-- MICRO-CLIMB|<!-- C1:')
ACC_OPEN = re.compile(r'<div class="acc(?: open)?"(?: id="[^"]*")?(?: style="[^"]*")?>\r\n')
def acc_start(t, i):
    """Start of the <div class="acc"> that holds the part title at position i."""
    last = None
    for m in ACC_OPEN.finditer(t, max(0, i - 400), i): last = m
    assert last is not None, 'no part opening before position %d' % i
    return last.start()
def blk(t, title):
    """One part of the old page, from its opening <div class="acc"> to the start of whatever follows it."""
    key = 'class="acc-t">' + title
    assert t.count(key) == 1, 'part title not found once: ' + title
    i = t.index(key); s = acc_start(t, i); m = NEXT.search(t, i)
    return t[s:m.start()].rstrip('\r\n')
def esc(s): return html.escape(s, quote=True)
def paras(items):
    out = []
    for kind, x in items:
        if kind == 'p': out.append('<p>%s</p>' % x)
        elif kind == 'h': out.append('<div class="hbox"><p>%s</p></div>' % x)
        elif kind == 'ul': out.append('<ul>' + ''.join('<li>%s</li>' % li for li in x) + '</ul>')
    return NL.join(out)
def acc(title, meta, body, after='', open_=False):
    return ('<div class="acc%s">' % (' open' if open_ else '') + NL +
            '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">%s</div></div>%s</div>' % (title, meta, ARR) + NL +
            '<div class="acc-b"><div class="cb">' + NL + body + NL + '</div>' + ((NL + after) if after else '') + '</div></div>')
def guide(*ps, label='FACILITATOR GUIDANCE'):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>' % label + NL + NL.join('<p>%s</p>' % p for p in ps) + NL + '</div>'
def activity(p, steps=None, tail=None):
    h = '<div class="fac-note-full u6-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + NL + '<p>%s</p>' % p
    if steps: h += NL + '<ol>' + ''.join('<li>%s</li>' % s for s in steps) + '</ol>'
    if tail: h += NL + '<p>%s</p>' % tail
    return h + NL + '</div>'
REF = 'Participants write a reflection in their own file: '
def reflection(rid, label, q, ph):
    return ('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; %s</div><p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">%s</p>'
            '<textarea class="ref-ta reflection-textarea" id="%s" placeholder="%s"></textarea><div class="ref-saved reflection-saved" id="%s-saved"></div>'
            '<button class="ref-save" onclick="saveTA(this)">Save Reflection</button></div>') % (label, q, rid, esc(ph).replace('\n', '&#10;'), rid)
def keep_reflection(block, rid):
    """A reflection block of the old participant page, with the question marked ref-prompt (the Learning Portfolio prints the question above the answer)."""
    m = re.search(r'<div class="ref-block">(?:(?!<div class="ref-block">).)*?id="%s"(?:(?!<div class="ref-block">).)*?</button></div>' % rid, block, re.S)
    assert m, 'reflection not found: ' + rid
    r = m.group(0); a = '<p style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">'
    return once(r, a, a.replace('<p ', '<p class="ref-prompt" '))
def tag(s): return re.sub(r'<[^>]+>', '', s)
def add_after(block, extra):
    """Facilitator page: place a note after the last guidance box of a part (inside the part, outside the teaching text)."""
    end = '\r\n</div></div></div>'
    assert block.endswith(end), block[-60:]
    return block[:-len('</div></div>')] + NL + extra + '</div></div>'

def build(v, src, other):
    """v = 'p' or 'f'. src = that page before the amendments. other = the other page (some shared wording is read from it)."""
    P, F = (src, other) if v == 'p' else (other, src)
    you = v == 'p'
    t = src
    num_colour = {'p': ['#8ab0e8', 'var(--teall)', '#5ecba1', '#c39de0'], 'f': ['#8ab0e8', 'var(--gold)', '#5ecba1', '#c39de0']}[v]

    # ═══ Section 1 ═══════════════════════════════════════════════════════════════════════════════
    b11 = blk(src, '1.1 &mdash;'); b12 = blk(src, '1.2 &mdash;'); b13 = blk(src, '1.3 &mdash;'); b14 = blk(src, '1.4 &mdash;')
    b11 = once(b11, '<p>Performance management and performance measurement are distinct disciplines.', '<p>Performance management (PM) and performance measurement are distinct disciplines.')
    if you:
        b12 = once(b12, keep_reflection(b12, 'ref1').replace(' class="ref-prompt"', ''), keep_reflection(b12, 'ref1'))
    else:
        cue = '<div class="p-insight">Facilitation cue: &ldquo;What does your PM system reward? Does it reward activity or results? Compliance or commitment?&rdquo;</div>'
        b12 = once(b12, cue, '')
        b12 = once(b12, '<p>Ask participants to rate their current PM system against each FACES dimension (1&ndash;5).',
                   '<p>Ask: <em>&ldquo;What does your PM system reward? Does it reward activity or results? Compliance or commitment?&rdquo;</em></p>' + NL + '<p>Ask participants to rate their current PM system against each FACES dimension (1&ndash;5).')
        b12 = add_after(b12, activity(REF + 'their rating of their current PM system from 1 to 5 against each of the five FACES functions, the biggest gap and what closing it would change.'))
    # 1.4 · Leader's Response: Carol's introduction, then the five rating cards in the fuller wording of the facilitator page
    f14 = blk(F, '1.4 &mdash;'); p14 = blk(P, '1.4 &mdash;')
    fcards = re.findall(r'<div class="p-card(?: open)?" onclick="toggleP\(this\)"><div class="p-head"><div class="p-meta"><div class="p-num"[^>]*>(.*?)</div><div class="p-name">(.*?)</div></div><div class="p-arr">&#9660;</div></div><div class="p-body">(.*?)</div></div>\r\n', f14, re.S)
    pnums = re.findall(r'<div class="p-card(?: open)?" onclick="toggleP\(this\)"><div class="p-head"><div class="p-meta">(<div class="p-num"[^>]*>.*?</div>)<div class="p-name">', (p14 if you else f14), re.S)
    assert len(fcards) == 5 and len(pnums) == 5
    cards = []
    for i, (_, name, body) in enumerate(fcards):
        name = name.replace('Immediate PIP within 30 days', 'Immediate performance improvement plan within 30 days')
        cards.append('<div class="p-card%s" onclick="toggleP(this)"><div class="p-head"><div class="p-meta">%s<div class="p-name">%s</div></div><div class="p-arr">&#9660;</div></div><div class="p-body">%s</div></div>' % (' open' if i == 2 else '', pnums[i], name, body))
    stack14 = '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>'
    assert 'PIP' not in tag(stack14)
    RATING_GUIDE = []   # for Section 5, Step 1: the definition of each rating, as taught in 1.4
    for (_, name, body) in fcards:
        d = re.search(r'<p><strong>Definition:</strong> (.*?)</p>', body, re.S).group(1)
        RATING_GUIDE.append((html.unescape(tag(d)), html.unescape(tag(name)).replace('Leadership response: ', '').replace('Immediate PIP within 30 days', 'Immediate performance improvement plan within 30 days')))
    if you:
        body14 = paras(C.INTRO_14_P) + NL + stack14 + NL + keep_reflection(p14, 'ref2')
        n14 = acc('1.4 &mdash; Leader&rsquo;s Response', 'Ratings &amp; leadership responses', body14)
    else:
        g = re.search(r'<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div>\r\n(.*?)\r\n</div></div></div>', f14, re.S).group(1)
        n14 = acc('1.4 &mdash; Leader&rsquo;s Response', 'Ratings &amp; leadership responses', paras(C.INTRO_14_F) + NL + stack14,
                  '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div>' + NL + g + NL + '</div>' + NL +
                  activity(REF + 'the rating that best reflects the performance standard they measure toward, and what the leadership response to that rating looks like in practice.'))
    # 1.5 · The Impact of a Calibrated System (new)
    cal = C.CAL[v]
    shifts = '<div class="principle-stack">' + NL + NL.join(
        '<div class="p-card open" onclick="toggleP(this)"><div class="p-head"><div class="p-meta"><div class="p-num" style="color:%s;">Shift %d</div><div class="p-name">%s</div></div><div class="p-arr">&#9660;</div></div><div class="p-body"><p>%s</p></div></div>' % (num_colour[i], i + 1, n, x)
        for i, (n, x) in enumerate(cal['shifts'])) + NL + '</div>'
    body15 = NL.join('<p>%s</p>' % x for x in cal['intro']) + NL + shifts + NL + '<div class="hbox"><p>%s</p></div>' % cal['close']
    n15 = acc('1.5 &mdash; The Impact of a Calibrated System', 'Three shifts', body15, '' if you else guide(C.CAL_GUIDE_F))
    sec1 = [b11, b12, b13, n14, n15]

    # ═══ Section 2 ═══════════════════════════════════════════════════════════════════════════════
    b21 = blk(src, '2.1 &mdash;'); b22 = blk(src, '2.2 &mdash;'); b24 = blk(src, '2.4 &mdash;'); blk(src, '2.3 &mdash;')   # 2.3 Rules of the Game is left out
    # 2.1 · the bridges, beefed up from the PPT notes
    a21 = '<p>A performance management system performs four critical bridging functions between strategy and execution.'
    b21 = once(b21, a21, NL.join('<p>%s</p>' % x for x in C.BRIDGE_INTRO[v]) + NL + '<div class="hbox"><p>%s</p></div>' % C.BRIDGE_LOS[v] + NL + a21)
    ends = re.findall(r'</p>(?:<div class="hbox"[^>]*>.*?</div>)?</div></div>\r\n', b21, re.S)
    assert len(ends) == 4, len(ends)
    pos = 0
    for i in range(4):
        j = b21.index(ends[i], pos)
        ins = '</p><p><strong>In practice:</strong> %s</p>' % C.BRIDGE_PRACTICE[v][i]
        b21 = b21[:j] + ins + b21[j + 4:]; pos = j + len(ins)
    if you: b21 = once(b21, keep_reflection(b21, 'ref3').replace(' class="ref-prompt"', ''), keep_reflection(b21, 'ref3'))
    else: b21 = add_after(b21, activity(REF + 'the bridge function most underdeveloped in their organisation, and where their strategy most often leaks.'))
    # 2.2 · Carol's opening order, then the six dimensions in the fuller wording
    f22 = blk(F, '2.2 &mdash;')
    table22 = re.search(r'<table.*?</table>', b22, re.S).group(0)
    if you:
        ft = re.search(r'<table.*?</table>', f22, re.S).group(0)
        fr = re.findall(r'<td[^>]*>(.*?)</td>', ft, re.S); pr = re.findall(r'<td[^>]*>(.*?)</td>', table22, re.S)
        assert len(fr) == len(pr) == 18
        for a, b in zip(pr, fr):
            if a != b: table22 = once(table22, '>' + a + '</td>', '>' + b + '</td>')
    two = ('<div class="u6-two"><div class="u6-two-c red"><div class="u6-two-h">Compliance</div><p>%s</p><ul>%s</ul></div><div class="u6-two-c green"><div class="u6-two-h">Commitment</div><p>%s</p><ul>%s</ul></div></div>'
           % (C.COMPLIANCE[0], ''.join('<li>%s</li>' % x for x in C.COMPLIANCE[1]), C.COMMITMENT[0], ''.join('<li>%s</li>' % x for x in C.COMMITMENT[1])))
    body22 = ('<p>Every PM system is built on one of two architectural orientations: compliance or commitment.</p>' + NL + '<p>%s</p>' % C.S2R_POSITION + NL + two + NL +
              '<p>The choice is rarely made explicitly &mdash; but it is always made. The six dimensions below reveal which architecture is currently operating%s.</p>' % (' in your organisation' if you else '') + NL + table22)
    if you:
        n22 = acc('2.2 &mdash; Compliance vs Commitment Architecture', 'The design choice', body22 + NL + keep_reflection(b22, 'ref4'))
    else:
        g = re.search(r'(<div class="fac-note-full">.*?\r\n</div>)</div></div>', f22, re.S).group(1)
        n22 = acc('2.2 &mdash; Compliance vs Commitment Architecture', 'The design choice', body22,
                  g + NL + activity(REF + 'where their current PM system sits between compliance and commitment, and the one structural change that would shift it most.'))
    # 2.3 (was 2.4) · Leader vs Team, in the fuller wording, with the one-line distinction and the example from the PPT notes
    f24 = blk(F, '2.4 &mdash;')
    table24 = re.search(r'<table.*?</table>', b24, re.S).group(0)
    if you:
        ft = re.search(r'<table.*?</table>', f24, re.S).group(0)
        for rx in (r'<td[^>]*>(.*?)</td>', r'<th[^>]*>(.*?)</th>'):
            fr = re.findall(rx, ft, re.S); pr = re.findall(rx, table24, re.S); assert len(fr) == len(pr)
            for a, b in zip(pr, fr):
                if a != b: table24 = once(table24, '>' + a + '</t', '>' + b + '</t')
    intro24 = re.search(r'<div class="acc-b"><div class="cb">\r\n(<p>.*?</p>)\r\n<table', f24, re.S).group(1)
    hbox24 = re.search(r'<div class="hbox"><p><strong>The practical implication:</strong>.*?</p></div>', f24, re.S).group(0)
    body23 = intro24 + NL + '<p><strong>%s</strong></p>' % C.LVT_ONE_LINE + NL + table24 + NL + hbox24 + NL + '<p>%s</p>' % C.LVT_EXAMPLE
    if you:
        n23 = acc('2.3 &mdash; Leader vs Team: A Critical Distinction', 'Who is measured on what', body23 + NL + reflection('ref11', 'Team and Leader in Your PM System', C.REF11_Q, C.REF11_PH))
    else:
        g = re.search(r'(<div class="fac-note-full">.*?\r\n</div>)</div></div>', f24, re.S).group(1)
        n23 = acc('2.3 &mdash; Leader vs Team: A Critical Distinction', 'Who is measured on what', body23,
                  g + NL + activity(REF + 'whether their current PM system evaluates the team member on execution progress and the leader on progress towards the strategic outcome or Key Result, and their own contribution to closing the gap.'))
    sec2 = [b21, n22, n23]

    # ═══ Section 3 ═══════════════════════════════════════════════════════════════════════════════
    p31 = blk(P, '3.1 &mdash;'); f31 = blk(F, '3.1 &mdash;'); p32 = blk(P, '3.2 &mdash;'); f32 = blk(F, '3.2 &mdash;')
    b33 = blk(src, '3.3 &mdash;'); b34 = blk(src, '3.4 &mdash;')
    f31p = re.findall(r'\r\n(<p>.*?</p>|<div class="hbox">.*?</div>)(?=\r\n)', f31.split('<div class="fac-note-full">')[0], re.S)
    assert len(f31p) == 3 and f31p[1].startswith('<div class="hbox">'), f31p
    lead, hb, crit = f31p
    if you:
        crit = once(crit, 'The critical question for any executive team:', 'The critical question for your executive team:')
    # the ten role cards: facilitator narrative and "when absent" line from the facilitator page; PM contribution lead and tags from the participant page
    fdet = re.findall(r'<div id="cxo(\d)" class="cxo-detail"[^>]*><p[^>]*><strong[^>]*>(.*?) &mdash; (.*?):</strong> (.*?)</p></div>', f32, re.S)
    pdet = re.findall(r'<div id="cx(\d)" class="cm-detail"><div class="cm-col"><h5>Hot Zone: (.*?)</h5><p>(.*?)</p></div><div class="cm-col"><h5>PM Contribution</h5><p>(.*?) <em>When this is absent:</em> (.*?)</p>((?:<div class="d-tag">.*?</div>)+)</div></div>', p32, re.S)
    assert len(fdet) == 10 and len(pdet) == 10
    details = []
    for i, R in enumerate(C.ROLES):
        role, zone, bias, ac_f, ac_p, narr_p, absent_p = R
        assert html.unescape(fdet[i][1]) == role and html.unescape(fdet[i][2]) == zone and html.unescape(pdet[i][1]) == zone, (role, fdet[i][1:3])
        ftxt = fdet[i][3]; k = ftxt.rindex(' When '); narr_f, absent_f = ftxt[:k], ftxt[k + 1:]
        lead_pm, tags = pdet[i][3], pdet[i][5]
        if you:
            det = ('<div id="cx%d" class="cm-detail"><div class="cm-col"><h5>Hot Zone: %s</h5><p class="u6-bias"><b>Your natural bias</b>%s</p><p>%s</p></div>'
                   '<div class="cm-col"><h5>PM Contribution</h5><p>%s %s</p><h5 style="margin-top:16px;">Alignment Contribution</h5><p>%s</p>%s</div></div>'
                   % (i, esc(zone), bias[0].upper() + bias[1:] + '.', narr_p.replace('—', '&mdash;'), lead_pm, absent_p, ac_p, tags))
        else:
            det = ('<div id="cxo%d" class="cxo-detail" style="display:none;background:#0a1a0d;border:1px solid rgba(201,168,76,.15);border-radius:4px;margin-top:8px;padding:22px 26px;"><div class="u6-cx2">'
                   '<div><h5>%s &mdash; Hot Zone: %s</h5><p class="u6-bias"><b>Natural bias</b>%s</p><p>%s</p></div>'
                   '<div><h5>PM Contribution</h5><p>%s %s</p><h5 style="margin-top:16px;">Alignment Contribution</h5><p>%s</p>%s</div></div></div>'
                   % (i, role, esc(zone), bias[0].upper() + bias[1:] + '.', narr_f, lead_pm, absent_f, ac_f, tags))
        details.append(det)
    grid = re.search(r'<div class="compass-grid".*?(?=\r\n<div id="cx)', (p32 if you else f32), re.S).group(0)
    assert grid.count('showCXO(') == 10
    grid_intro = ('<p>Each executive function owns a distinct hot zone in the enterprise PM architecture. Explore your own role first, then the roles most adjacent to yours. Each card gives your natural bias, your hot zone, your PM contribution and your alignment contribution.</p>' if you else
                  '<p>Each executive function owns a distinct hot zone in the enterprise PM architecture. Each role card gives the role&rsquo;s natural bias, its hot zone, its PM contribution and its alignment contribution.</p>')
    body31 = lead + NL + '<p>%s</p>' % C.BRIGADE_IMAGE[v] + NL + hb + NL + crit + NL + '<h4>CXO Hot Zones</h4>' + NL + grid_intro + NL + grid + NL + NL.join(details)
    if you:
        n31 = acc('3.1 &mdash; Unity in Diversity', '10 executive PM contributions', body31 + NL + keep_reflection(p32, 'ref6'), open_=True)
    else:
        g = guide('Ask participants to write down the top three enterprise performance priorities right now, on their own, and post them in the chat. Then compare the answers. The degree of divergence is a direct measure of Alignment Brigade dysfunction. <em>&ldquo;If your executive team cannot agree on the top three, how does the organisation below you know where to focus?&rdquo;</em>',
                  'Teach each participant&rsquo;s own role first, then the two roles closest to it. For each role, set the natural bias beside the alignment contribution: the bias is the diversity, the contribution is the unity. Key question: <em>&ldquo;In your last executive performance review, were all ten hot zones represented? What does the absence of a hot zone from the executive PM conversation produce in the organisation below?&rdquo;</em>')
        n31 = acc('3.1 &mdash; Unity in Diversity', '10 executive PM contributions', body31,
                  g + NL + activity(REF + 'the most important alignment conversation with an adjacent function in the next 30 days.'), open_=True)
    # 3.2 (was 3.3) and 3.3 (was 3.4)
    b33 = once(b33, '3.3 &mdash; The Three Execution Gaps', '3.2 &mdash; The Three Execution Gaps')
    b34 = once(b34, '3.4 &mdash; The Continuous PM Shift', '3.3 &mdash; The Continuous PM Shift')
    if you:
        b33 = once(b33, keep_reflection(b33, 'ref7').replace(' class="ref-prompt"', ''), keep_reflection(b33, 'ref7'))
        b34 = once(b34, '</div>\r\n</div></div></div>', '</div>' + NL + reflection('ref12', 'Your Current PM System', C.REF12_Q, C.REF12_PH) + NL + '</div></div></div>')
    else:
        b33 = once(b33, 'Ask the group to vote (anonymously if needed) on which Execution Gap is most present in their organisation.', 'Ask participants to post in the chat the Execution Gap most present in their organisation.')
        b33 = add_after(b33, activity(REF + 'the Execution Gap most present in their organisation, and why it persists.'))
        b34 = add_after(b34, activity(REF + 'the current PM architecture of their organisation, and the PM system currently in use.'))
    sec3 = [n31, b33, b34]

    # ═══ Section 4 · EXECUTION only ══════════════════════════════════════════════════════════════
    blk(src, '4.1 &mdash;'); blk(src, '4.2 &mdash;'); p43 = blk(P, '4.3 &mdash;'); f43 = blk(F, '4.3 &mdash;')
    fx = re.findall(r'<div class="ai-body"><p>(.*?)</p></div></div>', f43, re.S)
    px = re.findall(r'<div class="ai-ev">Self-check: (.*?)</div>', p43, re.S)
    assert len(fx) == 9 and len(px) == 9
    for i, (l, word, name, princ, check) in enumerate(C.EXEC):
        want = html.unescape(fx[i]) + (' ' + C.EXEC_O_ADDED if l == 'O' else '')
        assert want == princ, (l, want, princ)
        assert html.unescape(px[i]) == check, (l, px[i])
    ex_cards = []
    for i, (l, word, name, princ, check) in enumerate(C.EXEC):
        if you:
            ex_cards.append('<div class="ai-card" onclick="toggleAI(this)"><div class="ai-head"><div><div class="ai-letter" style="color:var(--teall);">%s</div><div class="ai-name">%s &mdash; %s</div></div><div class="ai-arr">&#9660;</div></div><div class="ai-bar"></div><div class="ai-body"><div class="ai-row"><div class="ai-rl">Principle</div><div class="ai-rt">%s</div></div><div class="ai-ev">Self-check: %s</div></div></div>' % (l, word, name, princ.replace('—', '&mdash;'), check))
        else:
            ex_cards.append('<div class="ai-card" onclick="toggleP(this)" style="cursor:pointer;"><div class="ai-head" style="padding:14px 16px;display:flex;align-items:center;gap:10px;"><span style="font-family:\'Cormorant Garamond\',serif;font-size:1.8rem;color:var(--gold);line-height:1;">%s</span><div><div style="font-size:9px;font-weight:700;letter-spacing:2px;color:rgba(255,255,255,.3);margin-bottom:2px;">%s</div><div style="font-size:12px;color:rgba(255,255,255,.7);">%s</div></div></div><div class="ai-body"><p>%s</p><div class="ai-ev">Self-check: %s</div></div></div>' % (l, word, name, princ.replace('—', '&mdash;'), check))
    gridx = ('<div class="aceit-grid" style="grid-template-columns:repeat(3,1fr);">' if you else '<div class="aceit-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:18px 0;">') + NL + NL.join(ex_cards) + NL + '</div>'
    two41 = '<div class="u6-two"><div class="u6-two-c"><div class="u6-two-h">FACES &middot; the function test</div><p>%s</p></div><div class="u6-two-c"><div class="u6-two-h">EXECUTION &middot; the design quality test</div><p>%s</p></div></div>' % (C.FACES_TEST, C.EXEC_TEST)
    body41 = ('<p>The EXECUTION framework synthesises the nine design principles of a high-quality enterprise PM system. Each letter represents a principle that, when absent, creates a specific and predictable PM failure mode.</p>' + NL +
              '<h4>FACES and EXECUTION</h4>' + NL + two41 + NL + '<div class="hbox"><p>%s</p></div>' % C.FACES_EXEC_CLOSE + NL + '<h4>The Nine Design Principles</h4>' + NL + gridx)
    g41 = guide('Teach the distinction first: FACES is what the PM system must deliver, and EXECUTION is what must be designed into the system for it to deliver. Then teach each principle with its self-check question. <em>&ldquo;Which principle is weakest in your current PM system? What is the cost of that gap? What is the one change that would address it?&rdquo;</em> This becomes the bridge into the Application section, where each group designs the FACES and the EXECUTION of its own PM architecture.')
    n41 = acc('4.1 &mdash; The EXECUTION Framework', 'Nine design principles', body41, '' if you else g41, open_=True)
    sec4 = [n41]

    # ═══ Section 5 · Designing the PM Architecture ═══════════════════════════════════════════════
    FL = C.fields(); lab = {f[0]: f[1] for f in FL}
    faces_body = re.findall(r'<div class="p-body"><p>(.*?)</p>', blk(src, '1.2 &mdash;'), re.S); assert len(faces_body) == 5
    sight_body = re.findall(r'<div class="sc-rl">What it measures</div><div class="sc-rt">(.*?)</div>', b13, re.S); assert len(sight_body) == 3
    def ta(fid, label, ph, big=False):
        return '<label class="wp-label" for="u6_%s">%s</label><textarea class="wp-ta" id="u6_%s" data-u6="%s" placeholder="%s"%s></textarea>' % (fid, label, fid, fid, esc(ph), ' style="min-height:96px;"' if big else '')
    def card(name, q, guide_html, inner):
        return '<div class="u6-s5">' + NL + '  <div class="u6-s5-h"><span class="u6-s5-n">%s</span>%s</div>' % (name, ('<span class="u6-s5-q">%s</span>' % q) if q else '') + NL + (('  <div class="u6-s5-g">%s</div>' % guide_html + NL) if guide_html else '') + '  ' + inner + NL + '</div>'
    def how(title, steps, lead=None, tail=None, cls='Capstone work &middot; How to complete '):
        return '<div class="u6-how"><div class="u6-how-h">%s%s</div>%s<ol>%s</ol>%s</div>' % (cls, title, ('<p>%s</p>' % lead) if lead else '', ''.join('<li>%s</li>' % s for s in steps), ('<p>%s</p>' % tail) if tail else '')
    tabs = '<div class="step-tabs">' + NL + NL.join('  <div class="step-tab%s" onclick="u6Step(%d)"><div class="step-num">Step %d</div><div class="step-name">%s</div></div>' % (' active' if i == 0 else '', i, i + 1, p[1]) for i, p in enumerate(C.PARTS)) + NL + '</div>'
    if you:
        works = how('', ['<strong>Step 1 &middot; Scoring Logic.</strong> Your group sets what each rating means, the evidence that confirms it and the leadership response it triggers in the monthly review. It then states the factors that may legitimately affect a rating, the lines of sight of progress it uses and its review cadence. The lessons from parts 1.3 and 1.4 sit above the boxes.',
                         '<strong>Step 2 &middot; FACES.</strong> Your group describes how its PM architecture will serve each of the five FACES functions. The lesson from part 1.2 sits above each box.',
                         '<strong>Step 3 &middot; EXECUTION.</strong> Your group describes how each of the nine EXECUTION principles is designed into its PM architecture. The lesson from part 4.1 sits above each box.',
                         '<strong>Step 4 &middot; PM Scorecards.</strong> Your group designs a PM scorecard for the CEO and one for the CFO. It uses two of the Key Results it confirmed in Unit 3 as the basis for measurement.'],
                    lead='This is group work. Your group designs the PM architecture for the strategy in your Capstone Blueprint, in four steps:',
                    tail='You then read your group&rsquo;s record at the foot of this section and select Confirm. This is Capstone work, and your confirmed record feeds your team&rsquo;s Capstone Blueprint.', cls='How Section 5 works')
        grp = '<div class="u6-group">%s</div>' % C.GROUP_RULE
        # Step 1
        s1 = [grp, how('Step 1 &middot; Scoring Logic', ['For each rating from 1 to 5, agree the performance level that earns it, the evidence required to confirm it and the leadership response it should trigger in the monthly review. The lesson from part 1.4 sits above the three boxes.',
                                                           'Agree the contextual factors that might legitimately affect a rating.',
                                                           'Describe the lines of sight of progress your PM architecture uses. The lesson from part 1.3 sits above each box.',
                                                           'Describe your review cadence and why your group chose it.']),
              '<div class="u6-h">1 &middot; The rating scale</div>']
        for i, (n, name) in enumerate(C.RATINGS):
            d, resp = RATING_GUIDE[i]
            g3 = '<div class="u6-g3"><div>%s</div><div>%s</div><div>%s</div></div>' % (
                ta('r%d_level' % n, 'Performance level that earns this rating', 'What a person at this rating delivers, in terms your organisation can see or count...'),
                ta('r%d_evid' % n, 'Evidence required to confirm it', 'The data, reports or feedback that confirm the rating...'),
                ta('r%d_resp' % n, 'Leadership response in the monthly review', 'What the leader does when this rating is given...'))
            s1.append(card('Rating %d &middot; %s' % (n, esc(name)), '', '<p><b>From part 1.4</b>%s</p><p><b>Leadership response taught</b>%s</p>' % (esc(d), esc(resp)), g3))
        s1.append('<div class="u6-h">2 &middot; Contextual factors</div>')
        s1.append(card('Contextual factors', '&ldquo;What might legitimately affect a rating?&rdquo;', '', ta('ctx', 'Contextual factors that might legitimately affect a rating', 'For example: the size of the unit, the volume of work, a change outside the person’s control...', True)))
        s1.append('<div class="u6-h">3 &middot; Lines of sight of progress</div>')
        for i, (s, name) in enumerate(C.SIGHTS, 1):
            s1.append(card('%s &middot; %s' % (s, esc(name)), '', '<p><b>From part 1.3 &middot; What it measures</b>%s</p>' % sight_body[i - 1], ta('sight%d' % i, 'How your PM architecture uses this sight', 'What your organisation tracks under this sight, and how much it counts...')))
        s1.append('<div class="u6-h">4 &middot; Review cadence</div>')
        s1.append(card('Review cadence', '&ldquo;How often is performance reviewed, and why?&rdquo;', '<p><b>From part 4.1 &middot; Ongoing &mdash; Review Rhythm</b>%s</p>' % C.EXEC_O_ADDED,
                       '<div class="u6-g2"><div>%s</div><div>%s</div></div>' % (ta('cad_what', 'Our review cadence', 'What is reviewed, how often and by whom...', True), ta('cad_why', 'Why this cadence', 'Why this rhythm suits your strategy and your organisation...', True))))
        s1.append('<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Step(1)">Go to Step 2 &middot; FACES &rarr;</button></div>')
        # Step 2
        s2 = [grp, how('Step 2 &middot; FACES', ['Read the guide in each card. It is the lesson from part 1.2.', 'For each of the five functions, describe how your PM architecture will serve it: the rule, the routine, the report or the owner that makes it happen.'])]
        for i, (l, name) in enumerate(C.FACES, 1):
            s2.append(card('%s &middot; %s' % (l, name), '', '<p><b>From part 1.2</b>%s</p>' % faces_body[i - 1], ta('faces%d' % i, 'How your PM architecture will ' + name[0].lower() + name[1:], 'In our PM architecture, this function is served by...', True)))
        s2.append('<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Step(2)">Go to Step 3 &middot; EXECUTION &rarr;</button></div>')
        # Step 3
        s3 = [grp, how('Step 3 &middot; EXECUTION', ['Read the guide in each card. It is the lesson from part 4.1.', 'For each of the nine principles, describe how it is designed into your PM architecture.'],
                       lead='Step 2 states what your PM architecture must deliver. Step 3 states what your group designs into it so that it delivers.')]
        for i, (l, word, name, princ, check) in enumerate(C.EXEC, 1):
            s3.append(card('%s &middot; %s &mdash; %s' % (l, word, name), '&ldquo;%s&rdquo;' % check, '<p><b>From part 4.1 &middot; Principle</b>%s</p>' % princ.replace('—', '&mdash;'), ta('exec%d' % i, 'How this principle is designed into your PM architecture', 'In our PM architecture, this principle is built in through...', True)))
        s3.append('<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Step(3)">Go to Step 4 &middot; PM Scorecards &rarr;</button></div>')
        # Step 4
        s4 = [grp, how('Step 4 &middot; PM Scorecards', ['Read your group&rsquo;s Enterprise OKRs, shown below. They are the Objectives and Key Results your group confirmed in Unit 3.',
                                                           'Choose two of your Key Results as the basis for measurement.',
                                                           'Design the PM scorecard for the CEO. For each Key Result, state what the CEO is measured on and give it a weight. Then add the operational measures and the behavioural and values measures, each with a weight. The four weights add up to 100%.',
                                                           'Design the PM scorecard for the CFO in the same way.',
                                                           'Read your group&rsquo;s record below, then select Confirm. Select Print for a copy.']),
              '<div class="u6-h" style="margin-top:6px;">From Unit 3 &middot; your group&rsquo;s confirmed Enterprise OKRs</div>', '<div id="u6Okrs"></div>',
              '<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Bring(true)">Bring in from my Unit 3 page</button></div>', '<div class="u6-note" id="u6BringMsg" style="display:none;"></div>',
              '<div class="u6-h">The two Key Results your group will measure</div>',
              '<div class="u6-g2" style="margin-bottom:18px;"><div><label class="wp-label" for="u6_kr1">Key Result 1</label><select class="u6-sel" id="u6_kr1" data-u6="kr1"></select></div><div><label class="wp-label" for="u6_kr2">Key Result 2</label><select class="u6-sel" id="u6_kr2" data-u6="kr2"></select></div></div>']
        for ri, role in ((0, 'CEO'), (1, 'CFO')):
            R = C.ROLES[ri]; k = role.lower()
            def row(head, sub, mid, mlabel, ph):
                return ('<div class="u6-row"><div class="u6-row-h">%s%s</div><div>%s</div><div><label class="wp-label" for="u6_%s_w">Weight (%%)</label><input class="u6-num" type="number" min="0" max="100" step="1" id="u6_%s_w" data-u6="%s_w" placeholder="%%"></div></div>'
                        % (head, sub, ta(k + '_' + mid + '_m', mlabel, ph), k + '_' + mid, k + '_' + mid, k + '_' + mid))
            rows = (row('Sight 1 &middot; Strategy &middot; Key Result 1', '<span class="u6-kr1-t"></span>', 'kr1', 'What the %s is measured on for this Key Result' % role, 'The cumulative outcome the %s answers for on this Key Result...' % role) +
                    row('Sight 1 &middot; Strategy &middot; Key Result 2', '<span class="u6-kr2-t"></span>', 'kr2', 'What the %s is measured on for this Key Result' % role, 'The cumulative outcome the %s answers for on this Key Result...' % role) +
                    row('Sight 2 &middot; Operational', '', 'op', 'Operational measures (KPIs) for the %s' % role, 'The operational measures that show the engine behind the two Key Results is performing...') +
                    row('Sight 3 &middot; Behavioural &amp; Values Alignment', '', 'bv', 'Behaviours and values measured for the %s' % role, 'The leadership behaviours and values assessed, and how...') +
                    '<div class="u6-tot" id="u6_tot_%s"></div>' % k)
            gh = ('<p><b>From part 3.1 &middot; %s &middot; %s</b>%s Natural bias: %s.</p><p><b>From part 2.3</b>%s</p><p><b>From part 1.3 &middot; Typical weighting</b>Strategy 30&ndash;50%% at senior levels &middot; Operational 30&ndash;50%% &middot; Behavioural &amp; Values 20&ndash;40%%.</p>'
                  % (role, esc(R[1]), R[5].replace('—', '&mdash;').replace('As %s, you' % role, 'The %s' % role).split('. ')[0].replace('The CEO hold ', 'The CEO holds ').replace('The CFO interpret ', 'The CFO interprets ') + '.', R[2], C.LVT_ONE_LINE))
            s4.append(card('PM scorecard &middot; ' + role, '', gh, rows))
        panels = [s1, s2, s3, s4]
        body5 = (works + NL + NL + tabs + NL + NL + (NL + NL).join('<div class="step-panel%s" id="u6sp%d">' % (' active' if i == 0 else '', i + 1) + NL + NL.join(x) + NL + '</div>' for i, x in enumerate(panels)) + NL + NL + '<div id="u6Rec"></div>' + NL)
    else:
        works = how('', ['<strong>Step 1 &middot; Scoring Logic.</strong> The group sets what each rating means, the evidence that confirms it and the leadership response it triggers in the monthly review. It then states the factors that may legitimately affect a rating, the lines of sight of progress it uses and its review cadence. The lessons from parts 1.3 and 1.4 sit above the boxes.',
                         '<strong>Step 2 &middot; FACES.</strong> The group describes how its PM architecture will serve each of the five FACES functions. The lesson from part 1.2 sits above each box.',
                         '<strong>Step 3 &middot; EXECUTION.</strong> The group describes how each of the nine EXECUTION principles is designed into its PM architecture. The lesson from part 4.1 sits above each box.',
                         '<strong>Step 4 &middot; PM Scorecards.</strong> The group designs a PM scorecard for the CEO and one for the CFO. It uses two of the Key Results it confirmed in Unit 3 as the basis for measurement.'],
                    lead='This is group work. Each group designs the PM architecture for the strategy in its Capstone Blueprint, in four steps:',
                    tail='Each participant then reads the group&rsquo;s record and selects Confirm. This is Capstone work, and the confirmed record feeds the team&rsquo;s Capstone Blueprint.', cls='How Section 5 works')
        top = guide('<strong>Order:</strong> All four steps are group work. Step 4 needs the group&rsquo;s Enterprise OKRs, so each group confirms them in Unit 3, part 4.2, first.',
                    '<strong>Facilitation principle:</strong> Test each entry against its guide. An entry that could be said of any organisation has not yet been designed for this strategy.',
                    label='FACILITATOR GUIDANCE &mdash; Section 5 &middot; Application')
        def lst(items): return '<ul class="u6-list">' + ''.join('<li>%s</li>' % x for x in items) + '</ul>'
        f1 = [guide('<strong>Briefing:</strong> Each group sets its rating scale first. For each rating from 1 to 5 it agrees the performance level, the evidence and the leadership response in the monthly review. It then states the contextual factors, the lines of sight of progress and the review cadence.',
                    '<strong>Watch for:</strong> a performance level with no measure in it. Ask what a manager would see or count.',
                    '<strong>Watch for:</strong> one leadership response given for two ratings. Ask what changes for the person at each rating.', label='FACILITATOR GUIDANCE &mdash; Step 1'),
              '<div class="u6-h">What each group completes in Step 1</div>',
              lst(['<strong>The rating scale:</strong> for each of Rating 1 &middot; Poor, Rating 2 &middot; Needs Improvement, Rating 3 &middot; Meets Expectations &middot; Solid Gold, Rating 4 &middot; Exceeds Expectations and Rating 5 &middot; Outstanding, three boxes: Performance level that earns this rating &middot; Evidence required to confirm it &middot; Leadership response in the monthly review. The definition from part 1.4 sits above the three boxes.',
                   '<strong>Contextual factors:</strong> one box: Contextual factors that might legitimately affect a rating.',
                   '<strong>Lines of sight of progress:</strong> one box for each of Sight 1 &middot; Strategy, Sight 2 &middot; Operational and Sight 3 &middot; Behavioural &amp; Values Alignment. The lesson from part 1.3 sits above each box.',
                   '<strong>Review cadence:</strong> two boxes: Our review cadence &middot; Why this cadence.']),
              activity(C.GROUP_RULE_F % 1, ['For each rating from 1 to 5, the group agrees the performance level that earns it, the evidence required to confirm it and the leadership response it should trigger in the monthly review.',
                                            'The group agrees the contextual factors that might legitimately affect a rating.', 'The group describes the lines of sight of progress its PM architecture uses.', 'The group describes its review cadence and why it chose it.'])]
        f2 = [guide('<strong>Briefing:</strong> Each group describes how its PM architecture will serve each of the five FACES functions.',
                    '<strong>Watch for:</strong> a function restated in other words. Ask what in the architecture makes it happen: a rule, a routine, a report or an owner.', label='FACILITATOR GUIDANCE &mdash; Step 2'),
              '<div class="u6-h">What each group completes in Step 2</div>',
              lst(['One box for each function: ' + ' &middot; '.join('%s %s' % x for x in C.FACES) + '. The lesson from part 1.2 sits above each box.']),
              activity(C.GROUP_RULE_F % 2, ['The group reads the guide in each card. It is the lesson from part 1.2.', 'For each of the five functions, the group describes how its PM architecture will serve it.'])]
        f3 = [guide('<strong>Briefing:</strong> Each group describes how each of the nine EXECUTION principles is designed into its PM architecture. Recall the distinction taught in part 4.1: FACES is what the PM system must deliver, and EXECUTION is what must be designed into it.',
                    '<strong>Watch for:</strong> an entry that repeats the Step 2 answer. Step 2 says what the system delivers. Step 3 says how it is built.', label='FACILITATOR GUIDANCE &mdash; Step 3'),
              '<div class="u6-h">What each group completes in Step 3</div>',
              lst(['One box for each principle: ' + ' &middot; '.join('%s %s' % (x[0], x[2]) for x in C.EXEC) + '. The principle and its self-check question from part 4.1 sit above each box.']),
              activity(C.GROUP_RULE_F % 3, ['The group reads the guide in each card. It is the lesson from part 4.1.', 'For each of the nine principles, the group describes how it is designed into its PM architecture.'])]
        f4 = [guide('<strong>Briefing:</strong> Each group chooses two of the Key Results it confirmed in Unit 3 as the basis for measurement. It then designs a PM scorecard for the CEO and one for the CFO.',
                    '<strong>Watch for:</strong> the same measure on both scorecards. Ask what each role is best placed to track (part 3.1) and what a leader is measured on (part 2.3).',
                    '<strong>Watch for:</strong> weights that leave out a sight. Each scorecard carries all three sights of part 1.3, and its four weights add up to 100%.', label='FACILITATOR GUIDANCE &mdash; Step 4'),
              '<div class="u6-h">What each group completes in Step 4</div>',
              lst(['<strong>The two Key Results:</strong> chosen from the group&rsquo;s Enterprise OKRs, which each page shows from the member&rsquo;s own Unit 3 page.',
                   '<strong>PM scorecard &middot; CEO:</strong> four rows, each with a measure and a weight: Sight 1 &middot; Strategy &middot; Key Result 1 &middot; Sight 1 &middot; Strategy &middot; Key Result 2 &middot; Sight 2 &middot; Operational &middot; Sight 3 &middot; Behavioural &amp; Values Alignment.',
                   '<strong>PM scorecard &middot; CFO:</strong> the same four rows.']),
              activity(C.GROUP_RULE_F % 4, ['The group reads its Enterprise OKRs from Unit 3, shown on each page.', 'The group chooses two of its Key Results as the basis for measurement.',
                                            'For the CEO, the group states what the role is measured on for each Key Result, then the operational measures and the behavioural and values measures, each with a weight.',
                                            'The group designs the PM scorecard for the CFO in the same way.', 'Each participant reads the record and selects Confirm. Print gives a copy.'],
                       tail='The confirmed record feeds the team&rsquo;s Capstone Blueprint.')]
        body5 = (top + NL + NL + works + NL + NL + tabs + NL + NL + (NL + NL).join('<div class="step-panel%s" id="u6sp%d">' % (' active' if i == 0 else '', i + 1) + NL + NL.join(x) + NL + '</div>' for i, x in enumerate([f1, f2, f3, f4])) + NL)

    # ═══ put the page together ═══════════════════════════════════════════════════════════════════
    def swap(t, first_title, stop, new_html):
        """Replace everything from the opening of the part titled first_title up to stop (not included)."""
        i = t.index('class="acc-t">' + first_title); s = acc_start(t, i); e = t.index(stop, s)
        return t[:s] + new_html + t[e:]
    mods = {'p': ['mod0', 'mod1', 'mod2', 'mod3', 'mod4'], 'f': ['mod1', 'mod2', 'mod3', 'mod4', 'mod5']}[v]
    def nav_after(t, mod):  # the mod-nav that closes this section
        return t.index('<div class="mod-nav"', t.index('id="%s"' % mod))
    for first, sec, mod in (('1.1 &mdash;', sec1, mods[0]), ('2.1 &mdash;', sec2, mods[1]), ('3.1 &mdash;', sec3, mods[2]), ('4.1 &mdash;', sec4, mods[3])):
        i = t.index('class="acc-t">' + first); s = acc_start(t, i); e = nav_after(t, mod)
        t = t[:s] + (NL + NL).join(sec) + NL + t[e:]
    # Section 5: from the first old part up to the Unit Summary
    i = t.index('id="%s"' % mods[4])
    if you:
        s = t.index('<div class="acc open">', i); e = t.index('<!-- MICRO-CLIMB SUMMARY', s)
        t = t[:s] + body5 + NL + t[e:]
    else:
        s = t.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; Simulation Setup</div>', i)
        e = acc_start(t, t.index('class="acc-t">Unit Summary'))
        t = t[:s] + body5 + NL + t[e:]
    # section openings
    t = once(t, '<h2>MyHealth Live Portal &mdash; PM Design Simulation</h2><p>Applying the full unit to a realistic case: designing the performance management architecture for a hospital chain launching a digital patient engagement portal.</p>',
             '<h2>%s</h2><p>%s</p>' % (C.S5_TITLE, 'Your group designs the performance management architecture for the strategy in your team&rsquo;s Capstone Blueprint: the scoring logic, the FACES, the EXECUTION and the PM scorecards for the CEO and the CFO.' if you else
                                       'Application &middot; Each group designs the performance management architecture for the strategy in its Capstone Blueprint: the scoring logic, the FACES, the EXECUTION and the PM scorecards for the CEO and the CFO.'))
    t = once(t, 'an integrated enterprise PM design: the collective progress signal, the three elements of enterprise PM, and the EXECUTION framework.' if you else 'an integrated enterprise PM design: the collective progress signal, three elements of enterprise PM, and the EXECUTION framework.',
             'an integrated enterprise PM design: the EXECUTION framework.')
    # styles
    root = ':root{--u6:#22a08a;--u6-bg:rgba(26,122,106,.08);--u6-bd:rgba(26,122,106,.3);}' if you else ':root{--u6:#c9a84c;--u6-bg:rgba(201,168,76,.07);--u6-bd:rgba(201,168,76,.3);}'
    k = t.index('</style>'); t = t[:k] + crlf(root + read(os.path.join(HERE, 'u6.css'))) + t[k:]
    if you:
        # Unit Summary, saved answers and the Section 5 script
        m = re.search(r'var SUMMARY=\[\r\n.*?\r\n\];\r\n(?=function renderSummaryP)', t, re.S); assert m
        t = t[:m.start()] + 'var SUMMARY=' + json.dumps(C.SUM_P, ensure_ascii=False) + ';' + NL + t[m.end():]
        m = re.search(r',\r\n  ref9:\{notesLabel:.*?\]\}\r\n\};', t, re.S); assert m
        t = t[:m.start()] + NL + '};' + t[m.end():]
        t = once(t, 'var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref7","ref8","ref9","ref10","app_scorecard","app_scoring","app_baseline","app_cadence","app_measures","app_tool"];',
                 'var KEYS=["ref1","ref2","ref3","ref4","ref6","ref7","ref11","ref12"];')
        t = once(t, 'hydrateScores("ref1");hydrateScores("ref9");', 'hydrateScores("ref1");u6Init(responses);')
        js = read(os.path.join(HERE, 'u6_p.js'))
        js = once(js, '/*FIELDS*/[]', json.dumps([list(f) for f in FL], ensure_ascii=False))
        js = once(js, '/*PARTS*/[]', json.dumps([list(p) for p in C.PARTS], ensure_ascii=False))
        t = once(t, '/* ── Init ── */', crlf(js.strip('\n')) + NL + NL + '/* ── Init ── */')
    else:
        t = once(t, 'It contains purpose, timing, tone, and key facilitation questions for the full unit.', 'It contains the purpose, the tone and the key facilitation questions for the full unit.')
        t = once(t, 'The Collective Progress Signal anchors three executive question types: Traction, Balance, Intervention. Cumulative Progress calculation reveals whether the trajectory will reach target.', C.SUM_F_4)
        t = once(t, 'The MyHealth Live Portal simulation applies PM design across scorecard architecture, scoring logic, baseline calculation, cadence design, periodic measures, and reporting tool structure &mdash; integrating all unit content into a live design challenge.', C.SUM_F_5)
        m = re.search(r'<p>Close by asking each participant to name one design change.*?</p>', t, re.S); assert m
        t = t[:m.start()] + '<p>%s</p>' % C.CLOSE_F + t[m.end():]
        t = once(t, 'function goBack(){window.location.href=\'dashboard_F.html\';}', 'function goBack(){window.location.href=\'dashboard_F.html\';}' + NL +
                 "function u6Step(i){var tabs=document.querySelectorAll('#mod5 .step-tab'),panels=document.querySelectorAll('#mod5 .step-panel');tabs.forEach(function(x,j){x.classList.toggle('active',j===i);});panels.forEach(function(x,j){x.classList.toggle('active',j===i);});}")
    assert '\n' not in t.replace('\r\n', ''), 'bare line feed in the page'
    return t

if __name__ == '__main__':
    p_in, f_in, p_out, f_out = sys.argv[1:5]
    P, F = read(p_in), read(f_in)
    for v, src, other, out in (('p', P, F, p_out), ('f', F, P, f_out)):
        t = build(v, src, other)
        open(out, 'w', encoding='utf-8', newline='').write(t)
        print(v, len(src), '->', len(t), out)
