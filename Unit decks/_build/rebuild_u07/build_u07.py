# -*- coding: utf-8 -*-
"""Unit 7 · Establishing Performance Expectations — builds the amended participant and facilitator pages (Carol's amendments of 11 October 2026).
Usage: python3 build_u07.py <participant page before> <facilitator page before> <participant out> <facilitator out>
Input: Claude outputs\\Backups\\Unit 7 file backups\\unit3_m1_lens6_[p|f] - before amendments (11 Oct).html
Every part is taken from the old pages or built from u7_content.py. Each cut and each replacement checks that it finds its place exactly once and stops on a miss.
Line endings stay CRLF, encoding UTF-8. The reflection answers ref1 to ref8 and the lens id are unchanged (ref8 moves to 1.4 with its teaching)."""
import sys, re, json, html, os
import u7_content as C
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'
def read(p): return open(p, encoding='utf-8', newline='').read()
def crlf(s): return s.replace('\r\n', '\n').replace('\n', '\r\n')
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:110]); return t.replace(a, b)
NEXT = re.compile(r'\r\n<div class="acc(?: open)?"(?: id="[^"]*")?(?: style="[^"]*")?>\r\n|<div class="mod-nav"|<!-- APPLICATION REFLECTION|<!-- MICRO-CLIMB|<!-- C1:')
ACC_OPEN = re.compile(r'<div class="acc(?: open)?"(?: id="[^"]*")?(?: style="[^"]*")?>\r\n')
def acc_start(t, i):
    last = None
    for m in ACC_OPEN.finditer(t, max(0, i - 400), i): last = m
    assert last is not None, 'no part opening before position %d' % i
    return last.start()
def blk(t, title):
    key = 'class="acc-t">' + title
    assert t.count(key) == 1, 'part title not found once: ' + title
    i = t.index(key); s = acc_start(t, i); m = NEXT.search(t, i)
    return t[s:m.start()].rstrip('\r\n')
def esc(s): return html.escape(s, quote=True)
def tag(s): return re.sub(r'<[^>]+>', '', s)
def acc(title, meta, body, after='', open_=False):
    return ('<div class="acc%s">' % (' open' if open_ else '') + NL +
            '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">%s</div></div>%s</div>' % (title, meta, ARR) + NL +
            '<div class="acc-b"><div class="cb">' + NL + body + NL + '</div>' + ((NL + after + NL) if after else '') + '</div></div>')
def guide(*ps, label='FACILITATOR GUIDANCE'):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>' % label + NL + NL.join(p if p.startswith('<p') else '<p>%s</p>' % p for p in ps) + NL + '</div>'
def activity(p):
    return '<div class="fac-note-full u7-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + NL + '<p>%s</p>' % p + NL + '</div>'
def keep_reflection(block, rid):
    """A reflection block of the old participant page, with the question marked ref-prompt (the Learning Portfolio prints the question above the answer)."""
    m = re.search(r'<div class="ref-block">(?:(?!<div class="ref-block">).)*?id="%s"(?:(?!<div class="ref-block">).)*?</button></div>' % rid, block, re.S)
    assert m, 'reflection not found: ' + rid
    a = '<p style="font-size:12px;color:rgba(255,255,255,.45);margin-bottom:8px;">'
    return once(m.group(0), a, a.replace('<p ', '<p class="ref-prompt" '))
def fguide(block):
    """The paragraphs of the FACILITATOR GUIDANCE box that closes a part of the old facilitator page."""
    m = re.search(r'<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div>\r\n(.*?)\r\n</div></div></div>$', block, re.S)
    assert m, 'guidance not found: ' + block[:120]
    return m.group(1)
def fbody(block):
    """The teaching content of a part of the old facilitator page (inside the .cb box)."""
    a = '<div class="acc-b"><div class="cb">\r\n'; i = block.index(a) + len(a)
    j = block.rindex('\r\n</div>\r\n<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div>')
    return block[i:j]
PCARD = re.compile(r'<div class="p-card(?: open)?" onclick="toggleP\(this\)"><div class="p-head"><div class="p-meta">(<div class="p-num"[^>]*>.*?</div>)<div class="p-name">(.*?)</div></div><div class="p-arr">&#9660;</div></div><div class="p-body">(.*?)</div></div>\r\n', re.S)
def pcard(i, num, name, body):
    return '<div class="p-card%s" onclick="toggleP(this)"><div class="p-head"><div class="p-meta">%s<div class="p-name">%s</div></div><div class="p-arr">&#9660;</div></div><div class="p-body">%s</div></div>' % (' open' if i == 0 else '', num, name, body)
def stack(cards): return '<div class="principle-stack">' + NL + NL.join(cards) + NL + '</div>'
TH = '<th style="padding:10px 14px;text-align:left;font-size:9px;letter-spacing:2px;text-transform:uppercase;border-bottom:1px solid rgba(255,255,255,.1);color:%s;">%s</th>'
TD0 = '<td style="padding:10px 14px;color:rgba(255,255,255,.35);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;">%s</td>'
TD = '<td style="padding:10px 14px;color:rgba(255,255,255,.7);">%s</td>'
def table3(heads, rows):
    cols = ['rgba(255,255,255,.35)', '#f08080', '#5ecba1']
    h = '<table style="width:100%;border-collapse:collapse;font-size:13px;margin:16px 0;">' + NL + '<thead><tr>' + NL + NL.join(TH % (cols[i], x) for i, x in enumerate(heads)) + NL + '</tr></thead>' + NL + '<tbody>' + NL
    for i, r in enumerate(rows):
        h += ('<tr>' if i == len(rows) - 1 else '<tr style="border-bottom:1px solid rgba(255,255,255,.05);">') + TD0 % r[0] + TD % r[1] + TD % r[2] + '</tr>' + NL
    return h + '</tbody></table>'
def cells(table):
    heads = re.findall(r'<th\s[^>]*>(.*?)</th>', table, re.S)
    rows = [re.findall(r'<td[^>]*>(.*?)</td>', r, re.S) for r in re.findall(r'<tr[^>]*>(<td.*?)</tr>', table, re.S)]
    return heads, rows
def sc_card(i, colour, trigger, name, rows):
    return ('<div class="sc-card%s" onclick="toggleSC(this)" style="cursor:pointer;"><div class="sc-head"><div class="sc-trigger" style="color:%s;">%s</div><div class="sc-q">%s</div></div><div class="sc-bar" style="background:%s;"></div><div class="sc-body">%s</div></div>'
            % (' open' if i == 0 else '', colour, trigger, name, colour, ''.join('<div class="sc-row"><div class="sc-rl%s">%s</div><div class="sc-rt">%s</div></div>' % (' u7-howx' if l == 'How to explain it' else '', l, x) for l, x in rows)))

def build(v, src, other):
    P, F = (src, other) if v == 'p' else (other, src)
    you = v == 'p'
    accent = 'var(--teall)' if you else 'var(--gold)'
    t = src
    B = lambda page, n: blk(page, n + ' &mdash;')

    # ═══ Section 1 ═══════════════════════════════════════════════════════════════════════════════════════
    # 1.1 · opening from the manuscript, the fuller table on both pages
    f11 = B(F, '1.1'); p11 = B(P, '1.1')
    lead11 = re.search(r'<p>The difference between setting expectations and establishing expectations.*?</p>', f11).group(0)
    quote11 = re.search(r'<div class="hbox"><p style="font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;line-height:1.8;"><em>.*?</em></p></div>', (p11 if you else f11)).group(0)
    heads, rows = cells(re.search(r'<table.*?</table>', f11, re.S).group(0)); assert len(rows) == 6 and len(heads) == 3
    rows = [[c.replace(C.KPI_OLD, C.KPI_NEW) for c in r] for r in rows]; assert sum(C.KPI_NEW in c for r in rows for c in r) == 1
    body11 = '<p>%s</p>' % C.OPEN_11[v] + NL + lead11 + NL + quote11 + NL + table3(heads, rows)
    if you: n11 = acc('1.1 &mdash; Setting vs Establishing Expectations', 'The defining distinction', body11 + NL + keep_reflection(p11, 'ref1'), open_=True)
    else: n11 = acc('1.1 &mdash; Setting vs Establishing Expectations', 'The defining distinction', body11, guide(fguide(f11)) + NL + activity(C.REF + C.ACT['1.1']), open_=True)
    # 1.2 · the three conditions in the fuller wording
    f12 = B(F, '1.2'); p12 = B(P, '1.2')
    fc = PCARD.findall(f12); pc = PCARD.findall(p12); assert len(fc) == 3 and len(pc) == 3
    lead12 = re.search(r'<p>When expectations are properly established, three conditions.*?</p>', f12).group(0)
    cards = []
    for i in range(3):
        assert fc[i][1] == pc[i][1], (fc[i][1], pc[i][1])
        body = fc[i][2]
        if i == 0:
            m = re.search(r'<div class="p-insight">Facilitation test: .*?</div>', body); assert m
            body = body.replace(m.group(0), '<div class="p-insight">%s</div>' % C.TEST_12)
        cards.append(pcard(i, (pc if you else fc)[i][0], fc[i][1], body))
    body12 = lead12 + NL + stack(cards)
    if you: n12 = acc('1.2 &mdash; The Three Conditions of Established Expectations', 'Clarity &middot; Capability &middot; Commitment', body12 + NL + keep_reflection(p12, 'ref2'))
    else: n12 = acc('1.2 &mdash; The Three Conditions of Established Expectations', 'Clarity &middot; Capability &middot; Commitment', body12, guide(fguide(f12)) + NL + activity(C.REF + C.ACT['1.2']))
    # 1.3 · the three chains: definition, examples, key question on both pages
    f13 = B(F, '1.3'); p13 = B(P, '1.3')
    lead13 = re.search(r'<p>Very few delivery goals are achieved by a single person acting alone\..*?</p>\r\n<div class="hbox"><p>.*?</p></div>', f13, re.S).group(0)
    assert f13.count('ai-card') and p13.count('sc-card')
    if you:
        cols = ['#8ab0e8', 'var(--teall)', '#5ecba1']
        grid = '<div class="scarf-grid" style="grid-template-columns:repeat(3,1fr);">' + NL + NL.join(
            '<div class="sc-card%s" onclick="toggleSC(this)"><div class="sc-head"><div class="sc-trigger" style="color:%s;">%s %s</div><div class="sc-q">%s</div></div><div class="sc-bar" style="background:%s;"></div><div class="sc-body">'
            '<div class="sc-row"><div class="sc-rl">Examples</div><div class="sc-rt">%s</div></div><div class="sc-row"><div class="sc-rl">Key question</div><div class="sc-rt"><em>%s</em></div></div></div></div>'
            % (' open' if i == 0 else '', cols[i], a, nm, wp, cols[i], ex, q) for i, (a, nm, wf, wp, ex, q) in enumerate(C.CHAINS)) + NL + '</div>'
        for (a, nm, wf, wp, ex, q) in C.CHAINS: assert ex in p13 and q in p13, nm
        n13 = acc('1.3 &mdash; The Expectations Chain', 'Mapping who else influences the outcome', lead13 + NL + grid + NL + keep_reflection(p13, 'ref3'))
    else:
        grid = re.search(r'<div class="aceit-grid".*?\r\n</div>', f13, re.S).group(0)
        for (a, nm, wf, wp, ex, q) in C.CHAINS: assert wf in grid and ex in grid and q in grid, nm
        n13 = acc('1.3 &mdash; The Expectations Chain', 'Mapping who else influences the outcome', lead13 + NL + grid, guide(C.GUIDE_13_F) + NL + activity(C.REF + C.ACT['1.3']))
    # 1.4 · The Alignment Dialogue: its introduction, Score → Evaluate → Resolve and the GROW coaching model (the teaching moved here from 4.2: Carol, 11 October)
    f14 = B(F, '1.4'); assert 'A 10 means go.' in f14 and 'OKR/KPI' in f14 and 'OKR/KPI' in B(P, '1.4')
    f42 = B(F, '4.2'); p42 = B(P, '4.2')
    panels = re.findall(r'<div class="step-panel(?: active)?" id="sg1sp\d">\r\n(.*?)\r\n</div>\r\n(?=<div class="step-panel|</div>\r\n</div>)', f42, re.S); assert len(panels) == 3, len(panels)
    growcards = []
    for i, (letter, name, mean, in_p, in_f, qs) in enumerate(C.GROW):
        growcards.append(sc_card(i, C.STEP_COL[i] or accent, letter, name, [
            (C.GROW_ROWS[v][0], mean), (C.GROW_ROWS[v][1], in_p if you else in_f),
            (C.GROW_ROWS[v][2], '<ul>' + ''.join('<li><em>%s</em></li>' % q for q in qs) + '</ul>')]))
    grow = ('<h4>%s</h4>' % C.GROW_HEAD + NL + '<p>%s</p>' % C.GROW_INTRO[v][0] + NL + '<div class="hbox"><p>%s</p></div>' % C.GROW_INTRO[v][1] + NL +
            '<div class="scarf-grid u7-grow" style="grid-template-columns:1fr 1fr;gap:10px;">' + NL + NL.join(growcards) + NL + '</div>' + NL + '<div class="hbox"><p>%s</p></div>' % C.GROW_MAP[v])
    body14 = '<p>%s</p>' % C.P14[v][0] + NL + '<div class="hbox"><p>%s</p></div>' % C.P14[v][1] + NL + '<p>%s</p>' % C.P14[v][2] + NL + '<h4>%s</h4>' % C.SER_HEAD + NL
    if you:
        pc = PCARD.findall(p42); assert len(pc) == 3
        joined = '\x00'.join(panels)
        th_old = C.VOICE_42[0][0]; joined = once(joined, th_old, th_old.replace('Leader action', 'Your action'))
        for a, b in C.VOICE_42[1:]: joined = once(joined, a, b)
        joined = once(joined, 'color:var(--gold);font-weight:700;', 'color:var(--teall);font-weight:700;')
        assert 'the leader' not in tag(joined).lower().replace('leader action', ''), [x for x in re.findall(r'.{40}the leader.{40}', tag(joined))]
        pp = joined.split('\x00')
        for i in range(3): assert C.CARD_42_NAMES[i][0] in pc[i][0]
        cards = [pcard(i, pc[i][0], C.CARD_42_NAMES[i][1], NL + pp[i] + NL) for i in range(3)]
        body14 += '<p>%s</p>' % C.INTRO_42_P + NL + stack(cards) + NL + grow + NL + keep_reflection(p42, 'ref8')
        n14 = acc('1.4 &mdash; The Alignment Dialogue', 'Testing whether the expectation is owned', body14)
    else:
        ser = fbody(f42); assert ser.startswith('<p>When the alignment score is below 9, the leader treats the number as data') and ser.count('class="step-panel') == 3
        n14 = acc('1.4 &mdash; The Alignment Dialogue', 'Testing whether the expectation is owned', body14 + ser + NL + grow,
                  guide(C.GUIDE_14_F, C.GUIDE_14B_F) + NL + activity(C.REF + C.ACT['1.4']))
    sec1 = [n11, n12, n13, n14]

    # ═══ Section 2 ═══════════════════════════════════════════════════════════════════════════════════════
    f21 = B(F, '2.1'); p21 = B(P, '2.1')
    lead21 = re.search(r'<p>Strategy is ultimately delivered through human commitment\..*?</p>', f21).group(0)
    heads, rows = cells(re.search(r'<table.*?</table>', f21, re.S).group(0)); assert len(rows) == 5
    heads = [h.replace('&#9651; ', '').replace('△ ', '') for h in heads]; assert heads == ['Dimension', 'Compliance-Driven', 'Commitment-Driven'], heads
    ph, pr = cells(re.search(r'<table.*?</table>', p21, re.S).group(0)); assert pr[-1][0] == 'How it sounds'
    rows.append(list(pr[-1]))
    body21 = lead21 + NL + table3(heads, rows)
    if you: n21 = acc('2.1 &mdash; Compliance vs Commitment: The Execution Dynamic', 'Ignition point', body21 + NL + keep_reflection(p21, 'ref4'), open_=True)
    else: n21 = acc('2.1 &mdash; Compliance vs Commitment: The Execution Dynamic', 'Ignition point', body21, guide(fguide(f21)) + NL + activity(C.REF + C.ACT['2.1']), open_=True)
    f22 = B(F, '2.2'); p22 = B(P, '2.2')
    fc = PCARD.findall(f22); pc = PCARD.findall(p22); assert len(fc) == 5 and len(pc) == 5
    for i in range(5): assert fc[i][1] == pc[i][1]
    body22 = stack([pcard(i, (pc if you else fc)[i][0], fc[i][1], fc[i][2]) for i in range(5)])
    if you: n22 = acc('2.2 &mdash; Five Mechanisms: Why Expectation Alignment Determines Outcomes', 'The behavioural logic', body22 + NL + keep_reflection(p22, 'ref5'))
    else: n22 = acc('2.2 &mdash; Five Mechanisms: Why Expectation Alignment Determines Outcomes', 'The behavioural logic', body22, guide(fguide(f22)) + NL + activity(C.REF + C.ACT['2.2']))
    f23 = B(F, '2.3'); p23 = blk(P, '2.3 &mdash;')
    fc = PCARD.findall(f23); pc = PCARD.findall(p23); assert len(fc) == 2 and len(pc) == 2
    lead23 = re.search(r'<p>When expectations are set without being established, two organisational conditions.*?</p>', f23).group(0)
    body23 = lead23 + NL + stack([pcard(i, (pc if you else fc)[i][0], fc[i][1], fc[i][2]) for i in range(2)])
    n23 = acc('2.3 &mdash; Engagement &amp; Accountability: The Two Casualties', 'What breaks down when expectations are only set', body23, '' if you else guide(fguide(f23)))
    sec2 = [n21, n22, n23]

    # ═══ Section 3 · tendency, gap and likely Expectations Chain for each role ═══════════════════════════
    f31 = B(F, '3.1'); p31 = B(P, '3.1')
    fdet = re.findall(r'<div id="ex(\d)" class="cxo-detail" style="([^"]*)"><div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;"><div><h5 style="([^"]*)">Typical Tendency</h5><p style="([^"]*)">(.*?)</p></div><div><h5 style="([^"]*)">Expectation Gap</h5><p style="[^"]*">(.*?)</p></div></div></div>', f31, re.S)
    pdet = re.findall(r'<div id="px(\d)" class="cm-detail"><div class="cm-col"><h5>Typical Tendency</h5><p>(.*?)</p></div><div class="cm-col"><h5>The Expectation Gap</h5><p>(.*?)</p><div class="cm-q">Reflection: (.*?)</div></div></div>', p31, re.S)
    assert len(fdet) == 10 and len(pdet) == 10
    pgrid = re.search(r'<div class="compass-grid".*?\r\n</div>', (p31 if you else f31), re.S).group(0); assert pgrid.count('showCXO(') == 10
    for i, r in enumerate(C.ROLES): assert '>%s</div>' % r in pgrid, r
    details = []
    for i, role in enumerate(C.ROLES):
        tend_f, gap_f, q = fdet[i][4], fdet[i][6], pdet[i][3]
        if role == 'CSO': q = once(q, C.CSO_Q_OLD, C.CSO_Q_NEW)
        up, down, ext = C.ROLE_CHAIN[role]
        chain = ('<div class="u7-chain"><h5%s>%s</h5><div class="u7-chain-g"><div><b>&#8593; Upline</b>%s</div><div><b>&#8595; Downline</b>%s</div><div><b>&#8596; External</b>%s</div></div><p class="u7-chain-n">%s</p></div>'
                 % ('' if you else ' style="color:#8ab0e8;"', C.CHAIN_HEAD[v], up, down, ext, C.CHAIN_NOTE[v]))
        if you:
            m = re.match(r'(Often|Frequently|Commonly) sets ', tend_f); assert m, tend_f[:40]
            tend = 'As %s, you %s set ' % (C.AS_ROLE.get(role, role), m.group(1).lower()) + tend_f[m.end():]
            if role == 'CHRO': tend = once(tend, 'The dialogue is typically strong', 'Your dialogue is typically strong')
            gap = C.CEO_GAP_P if role == 'CEO' else gap_f
            if role == 'CEO': assert 'is the CEO&rsquo;s most common expectation gap' in gap_f
            details.append('<div id="px%d" class="cm-detail"><div class="cm-col"><h5>Typical Tendency</h5><p>%s</p></div><div class="cm-col"><h5>The Expectation Gap</h5><p>%s</p></div>%s<div class="cm-q u7-ask">Ask yourself: %s</div></div>' % (i, tend, gap, chain, q))
        else:
            details.append('<div id="ex%d" class="cxo-detail" style="%s"><div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;"><div><h5 style="%s">Typical Tendency</h5><p style="%s">%s</p></div><div><h5 style="%s">Expectation Gap</h5><p style="%s">%s</p></div></div>%s<div class="u7-fask"><b>Ask</b>%s</div></div>'
                           % (i, fdet[i][1], fdet[i][2], fdet[i][3], tend_f, fdet[i][5], fdet[i][3], gap_f, chain, q))
    if you:
        ref6 = once(keep_reflection(p31, 'ref6'), C.REF6_OLD, C.REF6_NEW)
        body31 = '<p>%s</p>' % C.INTRO_31['p'] + NL + pgrid + NL + NL.join(details) + NL + ref6
        n31 = acc('3.1 &mdash; The Alignment Brigade: CXO Expectation Tendencies &amp; Gaps', '10 executive roles', body31, open_=True)
    else:
        lead31 = re.search(r'<p>Each CXO role naturally focuses on the mechanisms it controls:.*?</p>', f31).group(0)
        lead31 = once(lead31, C.INTRO_31['f_old'], C.INTRO_31['f_new'])
        body31 = lead31 + NL + pgrid + NL + NL.join(details)
        n31 = acc('3.1 &mdash; The Alignment Brigade: CXO Expectation Tendencies &amp; Gaps', '10 executive roles', body31, guide(C.GUIDE_31_F) + NL + activity(C.REF + C.ACT['3.1']), open_=True)
    sec3 = [n31]

    # ═══ Section 4 ═══════════════════════════════════════════════════════════════════════════════════════
    # 4.1 · the four steps in the participant card format on both pages; on the facilitator page "How to explain the four steps" comes before the cards
    f41 = B(F, '4.1'); p41 = B(P, '4.1')
    assert f41.count('onclick="showStep(') == 4 and p41.count('class="sc-card') == 4
    cards = []
    for i, (name, rows, how) in enumerate(C.STEPS_41):
        rr = [(l, (C.P_41.get((i, l), x) if you else x)) for l, x in rows]
        cards.append(sc_card(i, C.STEP_COL[i] or accent, 'Step %d' % (i + 1), name, rr))
    grid41 = '<div class="scarf-grid" style="grid-template-columns:1fr 1fr;gap:10px;">' + NL + NL.join(cards) + NL + '</div>'
    if you:
        body41 = '<p>%s</p>' % C.INTRO_41[v] + NL + grid41
        n41 = acc('4.1 &mdash; The Four-Step Expectation Architecture', 'A shared leadership practice', body41 + NL + keep_reflection(p41, 'ref7'), open_=True)
    else:
        how = '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; How to explain the four steps</div>' + NL + '<ol>' + ''.join('<li>%s</li>' % x for x in C.HOW_41_F) + '</ol>' + NL + '</div>'
        body41 = '<p>%s</p>' % C.INTRO_41[v] + NL + how + NL + grid41
        n41 = acc('4.1 &mdash; The Four-Step Expectation Architecture', 'A shared leadership practice', body41, activity(C.REF + C.ACT['4.1']), open_=True)
    # 4.2 · Practising the Alignment Dialogue: Portfolio work on the participant page, role play in class on the facilitator page
    def glesson(i): return '<div class="u7-s5-g"><p><b>From part 1.4 &middot; %s</b>%s %s</p></div>' % (C.GROW[i][1], C.GROW[i][2], C.GROW[i][3 if you else 4])
    if you:
        howbox = ('<div class="u7-how"><div class="u7-how-h">Portfolio work &middot; How to complete the Alignment Dialogue</div><ol>' + ''.join('<li>%s</li>' % s for s in C.HOW_42_P) + '</ol><p>%s</p></div>' % C.HOW_42_TAIL)
        pick = ('<div class="u7-s5">' + NL + '  <div class="u7-s5-h"><span class="u7-s5-n">Your Key Result</span></div>' + NL +
                '  <label class="wp-label" for="ad_kr">%s</label><select class="u7-sel" id="ad_kr"></select><div class="u7-note" id="u7AdMsg" style="display:none;"></div>' % C.AD_KR_LABEL + NL + '</div>')
        boxes = []
        for i, (key, label, ph) in enumerate(C.AD_FIELDS):
            boxes.append('<div class="u7-s5">' + NL + '  <div class="u7-s5-h"><span class="u7-s5-n">%s &middot; %s</span></div>' % (C.GROW[i][0], C.GROW[i][1]) + NL + '  ' + glesson(i) + NL +
                         '  <label class="wp-label" for="%s">%s</label><textarea class="wp-ta reflection-textarea" id="%s" style="min-height:120px;" placeholder="%s"></textarea><div class="reflection-saved" id="%s-saved"></div>' % (key, label, key, esc(ph).replace('\n', '&#10;'), key) + NL + '</div>')
        body42 = '<p>%s</p>' % C.INTRO_42['p'] + NL + howbox + NL + pick + NL + '<div class="hbox"><p>%s</p></div>' % C.SCENARIO['p'] + NL + NL.join(boxes)
        n42 = acc(C.T42, C.M42, body42)
    else:
        R = C.ROLEPLAY
        role = ('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>' % C.ROLEPLAY_LABEL + NL + '<p>%s</p>' % R['purpose'] + NL +
                '<p>%s</p>' % R['decide_lead'] + NL + '<ol>' + ''.join('<li>%s</li>' % s for s in R['decide']) + '</ol>' + NL +
                '<p>%s</p>' % R['run_lead'] + NL + '<ol>' + ''.join('<li>%s</li>' % s for s in R['steps']) + '</ol>' + NL +
                ''.join('<div class="u7-brief"><b>%s</b><span>%s</span></div>' % b for b in R['briefs']) + NL +
                '<p><strong>Watch for:</strong></p>' + NL + '<ul>' + ''.join('<li>%s</li>' % w for w in R['watch']) + '</ul>' + NL + '</div>')
        act = ('<div class="fac-note-full u7-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + NL + '<p>%s</p>' % C.ACT_42_LEAD + NL +
               '<ol>' + ''.join('<li>%s</li>' % s for s in C.ACT_42_STEPS) + '</ol>' + NL + '<p>%s</p>' % C.ACT_42_TAIL + NL + '</div>')
        body42 = ('<p>%s</p>' % C.INTRO_42['f'] + NL + role + NL + '<div class="hbox"><p>%s</p></div>' % C.SCENARIO['f'] + NL +
                  '<div class="u7-h">What each participant completes on the portal</div>' + NL + '<ul class="u7-list">' + ''.join('<li>%s</li>' % x for x in C.COMPLETES_42_F) + '</ul>')
        n42 = acc(C.T42, C.M42, body42, act)
    sec4 = [n41, n42]

    # ═══ Section 5 · two exercises: 5.1 the four steps on two Objectives, 5.2 the alignment dialogue with the board chair (group work, Capstone work) ═══
    FL = C.fields(); lab = {f[0]: f[1] for f in FL}
    def ta(fid, big=False, label=None, ph=None):
        if ph is None: ph = C.PH[fid.split('_', 1)[1]]
        return '<label class="wp-label" for="u7_%s">%s</label><textarea class="wp-ta" id="u7_%s" data-u7="%s" placeholder="%s"%s></textarea>' % (fid, label or lab[fid], fid, fid, esc(ph).replace('\n', '&#10;'), ' style="min-height:96px;"' if big else '')
    def num(fid): return '<label class="wp-label" for="u7_%s">%s</label><input type="number" min="1" max="10" step="1" class="u7-num" id="u7_%s" data-u7="%s" placeholder="1&ndash;10">' % (fid, lab[fid], fid, fid)
    def how(title, steps, lead=None, tail=None, cls='Capstone work &middot; How to complete '):
        tails = ''.join('<p>%s</p>' % x for x in (tail if isinstance(tail, list) else [tail])) if tail else ''
        return '<div class="u7-how"><div class="u7-how-h">%s%s</div>%s<ol>%s</ol>%s</div>' % (cls, title, ('<p>%s</p>' % lead) if lead else '', ''.join('<li>%s</li>' % s for s in steps), tails)
    def lesson(i): return '<div class="u7-s5-g">' + ''.join('<p><b>%s</b>%s</p>' % (a, b) for a, b in C.LESSON[i]) + '</div>'
    def chosen(n): return '<div class="u7-okr"><div><b>Objective</b><span class="u7-o%d-obj"></span></div><div><b>Key Result</b><span class="u7-o%d-kr"></span></div></div>' % (n, n)
    def card(n, inner): return '<div class="u7-s5">' + NL + '  <div class="u7-s5-h"><span class="u7-s5-n">Objective %d</span></div>' % n + NL + '  ' + inner + NL + '</div>'
    def lst(items): return '<ul class="u7-list">' + ''.join('<li>%s</li>' % x for x in items) + '</ul>'
    tabs = '<div class="step-tabs">' + NL + NL.join('  <div class="step-tab%s" onclick="u7Step(%d)"><div class="step-num">Step %d</div><div class="step-name">%s</div></div>' % (' active' if i == 0 else '', i, i + 1, p[1]) for i, p in enumerate(C.PARTS[:4])) + NL + '</div>'
    H = C.HOW_S5[v]
    works = how('', H['steps'], lead=H['lead'], tail=H['tail'], cls='How Section 5 works')
    if you:
        def panel(i, inner):
            return ('<div class="step-panel%s" id="u7sp%d">' % (' active' if i == 0 else '', i + 1) + NL + how('Step %d &middot; %s' % (i + 1, C.PARTS[i][1]), C.HOW_STEP_P[i]) + NL + inner + NL + '</div>')
        s1 = ('<div class="u7-btnrow" style="margin:0 0 4px;"><button type="button" class="u7-b" onclick="u7Bring(true)">Reload the drop-down lists</button></div><div class="u7-note" id="u7BringMsg" style="display:none;"></div>' + NL +
              '<div class="u7-h">The lesson for this step</div>' + NL + lesson(0) + NL +
              NL.join(card(n, '<div class="u7-pick"><div><label class="wp-label" for="u7_o%d_obj">Objective %d</label><select class="u7-sel" id="u7_o%d_obj" data-u7="o%d_obj"></select></div>'
                              '<div><label class="wp-label" for="u7_o%d_kr">One Key Result of this Objective</label><select class="u7-sel" id="u7_o%d_kr" data-u7="o%d_kr"></select></div></div>' % (n, n, n, n, n, n, n) + NL + '  ' +
                              '<label class="wp-label" for="u7_o%d_sipst">The Success in Practice statement it serves</label><select class="u7-sel" id="u7_o%d_sipst" data-u7="o%d_sipst"></select>' % (n, n, n) + NL + '  ' +
                              ta('o%d_owner' % n) + ta('o%d_sip' % n) + ta('o%d_frame' % n, big=True)) for n in (1, 2)))
        s2 = ('<div class="u7-h">The lesson for this step</div>' + NL + lesson(1) + NL +
              NL.join(card(n, chosen(n) + ta('o%d_what' % n) + '<div class="u7-g3"><div>' + ta('o%d_when' % n) + '</div><div>' + ta('o%d_std' % n) + '</div><div>' + ta('o%d_evid' % n) + '</div></div>') for n in (1, 2)))
        def crow(n, k, a, b): return '<div class="u7-chainrow"><div>' + ta('o%d_%s' % (n, k), label=a) + '</div><div>' + ta('o%d_%s_r' % (n, k), label=b) + '</div></div>'
        s3 = ('<div class="u7-h">The lesson for this step</div>' + NL + lesson(2) + NL +
              NL.join(card(n, chosen(n) + crow(n, 'up', '&#8593; Upline &middot; who must approve or resource this outcome', 'What the outcome needs from them') +
                              crow(n, 'down', '&#8595; Downline &middot; who must deliver specific activities', 'What the outcome needs from them') +
                              crow(n, 'ext', '&#8596; External &middot; which external actors influence delivery', 'What the outcome needs from them') + ta('o%d_coord' % n)) for n in (1, 2)))
        s4 = ('<div class="u7-h">The lesson for this step</div>' + NL + lesson(3) + NL +
              NL.join(card(n, chosen(n) + num('o%d_score' % n) + ta('o%d_concern' % n) + ta('o%d_act' % n) + num('o%d_score2' % n)) for n in (1, 2)))
        a51 = acc(C.T51, C.M51, tabs + NL + NL.join(panel(i, s) for i, s in enumerate([s1, s2, s3, s4])), open_=True)
        pick = ('<div class="u7-s5">' + NL + '  <div class="u7-s5-h"><span class="u7-s5-n">Your group&rsquo;s Key Result</span></div>' + NL +
                '  <label class="wp-label" for="u7_dg_kr">%s</label><select class="u7-sel" id="u7_dg_kr" data-u7="dg_kr"></select>' % C.DG_KR_LABEL + NL + '</div>')
        boxes = []
        for i, (key, short, label, ph) in enumerate(C.DG_FIELDS):
            boxes.append('<div class="u7-s5">' + NL + '  <div class="u7-s5-h"><span class="u7-s5-n">%s &middot; %s</span></div>' % (C.GROW[i][0], C.GROW[i][1]) + NL + '  ' + glesson(i) + NL + '  ' + ta(key, big=True, label=label, ph=ph) + NL + '</div>')
        a52 = acc(C.T52, C.M52, '<p>%s</p>' % C.INTRO_52['p'] + NL + how('the Alignment Dialogue with your board chair', C.HOW_52_P) + NL + pick + NL + '<div class="hbox"><p>%s</p></div>' % C.SCENARIO['p'] + NL + NL.join(boxes))
        body5 = works + NL + a51 + NL + NL + a52 + NL + '<div id="u7Rec"></div>' + NL
        ids = re.findall(r'data-u7="([^"]+)"', body5); assert sorted(ids) == sorted(f[0] for f in FL), set(f[0] for f in FL) ^ set(ids)
        assert all(body5.count('id="u7_%s"' % f[0]) == 1 for f in FL)
    else:
        def panel(i):
            return ('<div class="step-panel%s" id="u7sp%d">' % (' active' if i == 0 else '', i + 1) + NL +
                    '<div class="u7-h">The lesson participants see in Step %d</div>' % (i + 1) + NL + lesson(i) + NL +
                    '<div class="u7-h">What each group completes in Step %d</div>' % (i + 1) + NL + lst(C.COMPLETES_F[i]) + NL + '</div>')
        a51 = acc(C.T51, C.M51, tabs + NL + NL.join(panel(i) for i in range(4)), activity(C.ACT_S5_F % '5.1'), open_=True)
        a52 = acc(C.T52, C.M52, '<p>%s</p>' % C.INTRO_52['f'] + NL + '<div class="hbox"><p>%s</p></div>' % C.SCENARIO['f'] + NL +
                  '<div class="u7-h">What each group completes</div>' + NL + lst(C.COMPLETES_52G_F), activity(C.ACT_S5_F % '5.2'))
        body5 = guide(*C.GUIDE_S5_F, label='FACILITATOR GUIDANCE &mdash; Section 5 &middot; Application') + NL + works + NL + a51 + NL + NL + a52 + NL
        assert '<textarea' not in body5 and '<input' not in body5 and '<select' not in body5
        vis5 = tag(body5)
        for bad in ('Listen for', 'Challenge any', 'Watch for', 'Check that', 'Push back', 'Probe', 'coach the'): assert bad not in vis5, bad

    # ═══ put the page together ═══════════════════════════════════════════════════════════════════════════
    mods = {'p': ['mod0', 'mod1', 'mod2', 'mod3', 'mod4'], 'f': ['mod1', 'mod2', 'mod3', 'mod4', 'mod5']}[v]
    def nav_after(t, mod): return t.index('<div class="mod-nav"', t.index('id="%s"' % mod))
    for first, sec, mod in (('1.1 &mdash;', sec1, mods[0]), ('2.1 &mdash;', sec2, mods[1]), ('3.1 &mdash;', sec3, mods[2]), ('4.1 &mdash;', sec4, mods[3])):
        i = t.index('class="acc-t">' + first); s = acc_start(t, i); e = nav_after(t, mod)
        t = t[:s] + (NL + NL).join(sec) + NL + t[e:]
    i = t.index('id="%s"' % mods[4])
    if you:
        s = t.index('<div class="hbox" style="margin:22px 0;"><div style="font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--teall);margin-bottom:12px;">Case Context</div>', i)
        e = t.index('<!-- MICRO-CLIMB SUMMARY', s)
        assert t[s:e].count('class="acc-t">5.') == 7 and 'app_reflection' in t[s:e]
        t = t[:s] + body5 + NL + NL + t[e:]
    else:
        s = t.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; Role Play Setup</div>', i)
        e = acc_start(t, t.index('class="acc-t">Unit Summary'))
        assert t[s:e].count('class="acc-t">5.') == 7
        t = t[:s] + body5 + NL + t[e:]
    # Section 5 opening
    old5 = re.search(r'<h2>Role Play &mdash; Establishing Delivery Expectations</h2><p>You are a CXO establishing delivery expectations with a team member or Head of Department\..*?</p>', t); assert old5
    t = t[:old5.start()] + '<h2>%s</h2><p>%s</p>' % (C.S5_TITLE, C.S5_LEAD[v]) + t[old5.end():]
    # section learning outcomes, amended to the content (Carol, 11 October)
    for old, new in C.SLO_EDITS: t = once(t, '<li>%s</li>' % old, '<li>%s</li>' % new)
    # styles
    root = ':root{--u7:#22a08a;--u7-bg:rgba(26,122,106,.08);--u7-bd:rgba(26,122,106,.3);}' if you else ':root{--u7:#c9a84c;--u7-bg:rgba(201,168,76,.07);--u7-bd:rgba(201,168,76,.3);}'
    k = t.index('</style>'); t = t[:k] + crlf(root + read(os.path.join(HERE, 'u7.css'))) + t[k:]
    if you:
        t = once(t, C.DESC_P_OLD, C.DESC_P_NEW)
        # Unit Summary: the page's own four blocks with the voice and contrast fixes, and the Application block
        m = re.search(r'var SUMMARY=\[\r\n(.*?)\r\n\];\r\n(?=function renderSummaryP)', t, re.S); assert m
        summ = m.group(1)
        for a, b in C.SUM_P_EDITS:
            a2 = json.dumps(a, ensure_ascii=True)[1:-1]; b2 = json.dumps(b, ensure_ascii=True)[1:-1]
            summ = once(summ, a2, b2)
        summ += ',' + NL + '{arc:%s,title:%s,body:%s}' % tuple(json.dumps(C.SUM_P_5[k], ensure_ascii=True) for k in ('arc', 'title', 'body'))
        t = t[:m.start()] + 'var SUMMARY=[' + NL + summ + NL + '];' + NL + t[m.end():]
        t = once(t, 'var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref7","ref8","app_role","app_future","app_outcome","app_success","app_coord","app_concerns","app_resolve","app_rating","app_primary","app_action","app_reflection"];',
                 'var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref7","ref8","ad_goal","ad_reality","ad_options","ad_will"];')
        a = 'KEYS.forEach(function(id){var ta=document.getElementById(id);if(ta&&responses[id]!=null)ta.value=responses[id];});'
        t = once(t, a, a + NL + '    u7Init(responses);')
        js = read(os.path.join(HERE, 'u7_p.js'))
        js = once(js, '/*FIELDS*/[]', json.dumps([list(f) for f in FL], ensure_ascii=False))
        js = once(js, '/*PARTS*/[]', json.dumps([list(p) for p in C.PARTS], ensure_ascii=False))
        t = once(t, '/* \\u2500\\u2500 Init \\u2500\\u2500 */', crlf(js.strip('\n')) + NL + NL + '/* \\u2500\\u2500 Init \\u2500\\u2500 */')
        assert 'app_' not in t and '5-Day' not in t and '5 working days' not in t
    else:
        m = re.search(r'<p>Unit 7 addresses the single most common reason strategy fails at the human level:.*?</p>\r\n<p>This unit is highly experiential\..*?</p>', t, re.S); assert m
        t = t[:m.start()] + '<p>%s</p>' % C.INTENT_F + t[m.end():]
        m = re.search(r'<p><strong>Application:</strong> Run the role-play with real expectations.*?</p>', t); assert m
        t = t[:m.start()] + '<p>%s</p>' % C.WATCH_APP_F + t[m.end():]
        t = once(t, C.SUM_F_4_OLD, C.SUM_F_4_NEW)
        last = re.search(r'(<div style="flex:1;min-width:180px;background:#151c15;border:1px solid rgba\(255,255,255,\.07\);border-radius:4px;padding:16px 18px;"><div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:)#c39de0(;margin-bottom:8px;">)Integration — Collective(</div><p style="[^"]*">).*?</p></div>\r\n', t); assert last
        t = t[:last.end()] + last.group(1) + '#f0a070' + last.group(2) + C.SUM_F_5[0] + last.group(3) + C.SUM_F_5[1] + '</p></div>' + NL + t[last.end():]
        m = re.search(r'<p>Close by asking each leader to name one expectation they have set but not yet established.*?</p>', t); assert m
        t = t[:m.start()] + '<p>%s</p>' % C.CLOSE_F + t[m.end():]
        t = once(t, "function toggleAI(c){c.classList.toggle('open');}", "function toggleAI(c){c.classList.toggle('open');}" + NL + "function toggleSC(c){c.classList.toggle('open');}" + NL +
                 "function u7Step(i){var tabs=document.querySelectorAll('#mod5 .step-tab'),panels=document.querySelectorAll('#mod5 .step-panel');tabs.forEach(function(x,j){x.classList.toggle('active',j===i);});panels.forEach(function(x,j){x.classList.toggle('active',j===i);});}")
        vis = tag(re.sub(r'<(script|style)\b.*?</\1>', '', t, flags=re.S))
        for bad in ('15 min', '3 minutes', 'Protect the time', 'five working days', 'five-day', 'Pairs or triads', 'plenary', 'In pairs', 'on the spot', 'Click a role', 'HoD', 'A 10 means go'):
            assert bad not in vis, bad
    assert '\n' not in t.replace('\r\n', ''), 'bare line feed in the page'
    return t

if __name__ == '__main__':
    p_in, f_in, p_out, f_out = sys.argv[1:5]
    P, F = read(p_in), read(f_in)
    for v, src, other, out in (('p', P, F, p_out), ('f', F, P, f_out)):
        t = build(v, src, other)
        open(out, 'w', encoding='utf-8', newline='').write(t)
        print(v, len(src), '->', len(t), out)
