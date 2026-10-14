# -*- coding: utf-8 -*-
"""Unit 9 · Strategic Unclogging — builds the amended participant and facilitator pages (three-way match of 13 October 2026;
Carol, 13 October 20:21: "rework the current exercise to fit that", Section 5 as the application for Capstone building).
Usage: python3 build_u09.py <participant page before> <facilitator page before> <participant out> <facilitator out>
Input: Claude outputs\\Backups\\Unit 9 file backups\\unit3_m2_lens8_[p|f] - before amendments (13 Oct).html (md5 d41da670…, b65a81ba…)
Sections 1 to 4 keep the facilitator page's teaching text (one shared text), with the wording fixes of the findings report;
part 4.4 (diagnostic triads, Portfolio work) and Section 5 (the Clog Clinic on the group's two Key Results, Capstone work) are new.
The page shell (header, tabs, sign-in checks, submission cluster, scripts) stays as it was. Each cut checks that it finds its place
exactly once. Line endings stay CRLF, encoding UTF-8, lens id u3m2_lens8 unchanged."""
import sys, re, json, os
import u9_content as C
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'
def read(p): return open(p, encoding='utf-8', newline='').read()
def crlf(s): return s.replace('\r\n', '\n').replace('\n', '\r\n')
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:110]); return t.replace(a, b)
def tag(s): return re.sub(r'<[^>]+>', '', s)
def div_end(t, i):
    """Index just past the </div> that closes the <div at position i."""
    depth = 0
    for m in re.compile(r'<div\b|</div>').finditer(t, i):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0: return m.end()
    raise AssertionError('unbalanced div')
def strip_fac(body):
    while True:
        i = body.find('<div class="fac-note-full"')
        if i < 0: return body
        j = div_end(body, i)
        a = i - 2 if body[i - 2:i] == NL else i
        body = body[:a] + body[j:]
def accs(t):
    out = {}
    for m in re.finditer(r'<div class="acc(?: open)?"[^>]*>\r\n<div class="acc-h"[^\r]*?<div class="acc-t">(.*?)</div>', t):
        s = t.index('<div class="acc-b"><div class="cb">\r\n', m.end()) + len('<div class="acc-b"><div class="cb">\r\n')
        out[m.group(1)] = t[s:t.index('\r\n</div></div></div>', s)]
    return out
def get(A, prefix):
    k = [x for x in A if x.startswith(prefix)]; assert len(k) == 1, prefix; return A[k[0]]

P0 = F0 = FA = PA = None
def guide_box(mod, label):
    i = F0.index('id="%s"' % mod); j = F0.index('&#9670; ' + label, i)
    s = F0.rindex('<div class="fac-note-full">', i, j); return F0[s:div_end(F0, s)]

def sec_head(v, n, title):
    names = {1: 'Awareness — What', 2: 'Intelligence — Why', 3: 'Extrapolating — Where', 4: 'Integration — Collective'}
    return [C.hero('Section %d · %s' % (n, names[n]), title, C.LEAD[n]), '<div class="mod-body">', C.slo(*C.SLO[n]), '']
def fguide(n, label):
    g = guide_box('mod%d' % n, 'FACILITATOR GUIDANCE — ' + label)
    for a, b in C.GUIDE_S.get(n, []): g = once(g, a, b)
    return C.fix(g)

def sec1(v):
    out = sec_head(v, 1, 'What is a Strategic Clog?')
    if v == 'f': out += [fguide(1, 'Awareness'), '']
    b = once(C.fix(get(FA, '1.1')), C.OPEN_11['f'], C.OPEN_11[v])
    if v == 'p':
        q = C.Q['ref1']; out.append(C.acc('1.1 &mdash; What is a Strategic Clog?', 'Core concept', b + NL + C.reflection('ref1', q[0], q[1], q[2]), open_=True))
    else:
        out.append(C.acc('1.1 &mdash; What is a Strategic Clog?', 'Core concept', b, C.activity(C.ACT['1.1']), open_=True))
    out.append('')
    b = C.fix(get(FA, '1.2'))
    if v == 'p':
        b = once(strip_fac(b), 'Three patterns signal that a clog is forming.</p>', 'Three patterns signal that a clog is forming. Which do you recognise most immediately in your organisation?</p>')
    else:
        b = once(b, C.PROMPT_12_OLD, C.PROMPT_12_NEW)
    out.append(C.acc('1.2 &mdash; Three Observable Friction Signals', 'How clogs first appear', b)); out.append('')
    b = C.fix(get(FA, '1.3'))
    if v == 'p':
        b = strip_fac(b)
        b = once(b, 'Select each to examine the structural reality, observable patterns, early warning signals, and strategic impact.</p>',
                 'Select each to examine the structural reality, observable patterns, early warning signals, and strategic impact, and ask yourself which clogs are currently present in your organisation.</p>')
        asks = re.findall(r'<div class="p-reflect">Reflect: (.*?)</div>', get(PA, '1.3')); assert len(asks) == 7
        parts = re.split(r'(<div class="clog-impact">.*?</div>)', b); assert len(parts) == 15
        b = ''.join(x + ((NL + '      <div class="p-reflect">Ask yourself: %s</div>' % C.fix(asks[k // 2])) if k % 2 == 1 else '') for k, x in enumerate(parts))
        pb = get(PA, '1.3'); s = pb.index('<div class="ref-block"><div class="ref-label">&#x270E; Your Self-Assessment'); blk = pb[s:]
        blk = once(blk, '<div class="ref-label">&#x270E; Your Self-Assessment — Which Clogs Are Active?</div><p style="font-size:12px;color:rgba(255,255,255,.6);margin-bottom:6px;">Rate each clog in your current strategy portfolio (1 = absent, 5 = active).</p>',
                   '<div class="ref-label">&#x270E; Reflection &mdash; Which Clogs Are Active?</div>' + C.PROMPT % 'Rate each clog in your current strategy portfolio (1 = absent, 5 = active). Then name the clog you will bring to the diagnostic triads in part 4.4.')
        blk = once(blk, '<label class="fld-label">The clog I will bring to the Clog Clinic</label>', '<label class="fld-label">The clog I will bring to the diagnostic triads (4.4)</label>')
        out.append(C.acc('1.3 &mdash; The 7-Clog Diagnostic Map', 'ABCV-aligned · Select each clog to explore', b + NL + blk))
    else:
        out.append(C.acc('1.3 &mdash; The 7-Clog Diagnostic Map', 'ABCV-aligned · Select each clog to explore', b, C.activity(C.ACT['1.3'])))
    out.append('')
    return NL.join(out)

def sec2(v):
    out = sec_head(v, 2, 'Why Clogs Are Predictable Features of Execution')
    if v == 'f': out += [fguide(2, 'Intelligence'), '']
    b = C.fix(get(FA, '2.1'))
    if v == 'p':
        q = C.Q['ref3']; out.append(C.acc('2.1 &mdash; Clogs Are Design Signals', 'The core argument', b + NL + C.reflection('ref3', q[0], q[1], q[2]), open_=True))
    else:
        out.append(C.acc('2.1 &mdash; Clogs Are Design Signals', 'The core argument', b, C.activity(C.ACT['2.1']), open_=True))
    out.append('')
    out.append(C.acc('2.2 &mdash; Three Disciplines of Execution Engineering', 'Step through each', C.fix(get(FA, '2.2')))); out.append('')
    b = C.fix(get(FA, '2.3'))
    whens = re.findall(r'<div class="lever-reflect">(Apply when: .*?) Best for:', get(PA, '2.3')); assert len(whens) == 7
    parts = b.split(' Best applied to:'); assert len(parts) == 8
    b = parts[0] + ''.join(' %s Best applied to:%s' % (whens[k], parts[k + 1]) for k in range(7))
    if v == 'p':
        q = C.Q['ref4']; out.append(C.acc('2.3 &mdash; The 7 Strategic Unclogging Levers', 'Select each lever to explore', strip_fac(b) + NL + C.reflection('ref4', q[0], q[1], q[2])))
    else:
        out.append(C.acc('2.3 &mdash; The 7 Strategic Unclogging Levers', 'Select each lever to explore', b, C.activity(C.ACT['2.3'])))
    out.append('')
    return NL.join(out)

def sec3(v):
    out = sec_head(v, 3, 'Where Are the Highest-Flammability Clog Zones?')
    if v == 'f': out += [fguide(3, 'Extrapolating'), '']
    out.append(C.acc('3.1 &mdash; The 7 COMPASS High-Flammability Zones', 'Select each zone to explore', C.fix(get(FA, '3.1')), open_=True)); out.append('')
    out.append(C.acc('3.2 &mdash; The 4-Step Unclogging Activation', 'Step through each stage', C.fix(get(FA, '3.2')))); out.append('')
    return NL.join(out)

def pf_block(key, label, flds):
    h = '<div class="ref-block u9-pf"><div class="ref-label">%s</div>' % label
    for i, (lab, opts) in enumerate(flds):
        h += '<label class="fld-label">%s</label>' % lab
        if opts:
            h += '<select class="fld-isel" data-fkey="%s" data-fidx="%d" onchange="syncField(\'%s\')"><option value="">&ndash;</option>%s</select>' % (key, i, key, ''.join('<option>%s</option>' % o.replace('&', '&amp;') for o in opts))
        else:
            h += '<input class="fld-input" type="text" data-fkey="%s" data-fidx="%d" oninput="syncFieldDebounced(\'%s\')">' % (key, i, key)
        h += NL
    return h + '<textarea id="%s" class="reflection-textarea" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="%s-saved"></div><button class="ref-save" onclick="fldSaveBtn(this,\'%s\')">Save</button></div>' % (key, key, key)

def part44(v):
    you = v == 'p'
    how = '<div class="u9-how"><div class="u9-how-h">Portfolio work &middot; How to complete the diagnostic triads</div><ol>%s</ol></div>' % ''.join('<li>%s</li>' % s for s in C.HOW44[v])
    roles = '<div class="role-row">' + NL + NL.join('  <div class="role-card"><div class="role-card-title">&#128100; %s</div><p>%s</p></div>' % r for r in C.ROLES) + NL + '</div>'
    qs = '<p style="margin-top:14px;"><strong>Four Questions &mdash; in sequence, without skipping:</strong></p>' + NL + '<div class="obs-stack">' + NL + NL.join('  <div class="obs-item"><div class="obs-label">%s</div><p>%s</p></div>' % q for q in C.QUESTIONS) + NL + '</div>'
    crit = '<p style="margin-top:14px;"><strong>The four observer criteria:</strong></p>' + NL + '<div class="obs-stack">' + NL + NL.join('  <div class="obs-item"><div class="obs-label">%s</div><p>%s</p></div>' % c for c in C.CRITERIA) + NL + '</div>'
    ch = ('<p style="margin-top:14px;"><strong>The Collective Intelligence Challenge.</strong> Each triad nominates one diagnosis, ideally the one it found most difficult to crack, and posts it in the chat:</p>' + NL +
          '<div class="hbox" style="margin:12px 0;"><p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;">%s</p></div>' % C.CHALLENGE_SENTENCE + NL +
          '<p>The full group then challenges it:</p>' + NL + C.ul(C.CHALLENGE_QS))
    if not you:
        ch += NL + '<p>The facilitator closes each challenge with:</p>' + NL + '<div class="hbox" style="margin:12px 0;"><p style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;font-style:italic;">%s</p></div>' % C.CLOSE_Q
    body = NL.join([how, roles, qs, crit, ch])
    if you:
        body += NL + '<div class="u9-h">Your Portfolio work</div>' + NL + NL.join(pf_block(*x) for x in C.PF)
        return C.acc(C.T44, C.M44, body)
    return C.acc(C.T44, C.M44, C.guide('FACILITATOR GUIDANCE — Diagnostic Triads', *C.GUIDE_44) + NL + body, C.activity(C.ACT['4.4']))

def sec4(v):
    out = sec_head(v, 4, 'Cross-Leadership Clog Ownership')
    if v == 'f': out += [fguide(4, 'Integration'), '']
    out.append(C.acc('4.1 &mdash; Normalising the Unclog: From Crisis to Habit', 'The collective discipline', C.fix(get(FA, '4.1')), open_=True)); out.append('')
    b = C.fix(get(FA, '4.2'))
    if v == 'p':
        pb = get(PA, '4.1'); s = pb.index('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; Clog Outside Your Function</div>'); blk = pb[s:]
        blk = once(blk, '<p style="font-size:12px;color:rgba(255,255,255,.6);margin-bottom:2px;">The clog I suspect is forming outside my function:</p>',
                   C.PROMPT % 'Name a clog you suspect is forming outside your function: its category, COMPASS zone and the signal you observe, why you have not raised it yet, and the consequence of not raising it.')
        out.append(C.acc('4.2 &mdash; The &ldquo;See Something, Say Something&rdquo; Principle', 'Shared stewardship of execution', strip_fac(b) + NL + blk))
    else:
        b = once(b, C.EX_42_OLD, C.EX_42_NEW)
        out.append(C.acc('4.2 &mdash; The &ldquo;See Something, Say Something&rdquo; Principle', 'Shared stewardship of execution', b, C.activity(C.ACT['4.2'])))
    out.append('')
    if v == 'p':
        out.append(C.acc('4.3 &mdash; Enterprise Unclogging Agenda', 'Build the shared priority list', C.AGENDA_43 + NL + C.AGENDA_43_P))
    else:
        fb = get(FA, '4.3'); s = fb.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator Closing Note'); closing = fb[s:div_end(fb, s)]
        out.append(C.acc('4.3 &mdash; Enterprise Unclogging Agenda', 'Build the shared priority list', C.AGENDA_43 + NL + C.guide('FACILITATOR GUIDANCE', C.AGENDA_43_F_GUIDE) + NL + closing))
    out.append('')
    out.append(part44(v)); out.append('')
    return NL.join(out)

def section5(v):
    you = v == 'p'; FL = C.fields()
    def how(title, steps, lead=None, tail=None, cls='Capstone work &middot; How to complete '):
        return '<div class="u9-how"><div class="u9-how-h">%s%s</div>%s<ol>%s</ol>%s</div>' % (cls, title, ('<p>%s</p>' % lead) if lead else '', ''.join('<li>%s</li>' % s for s in steps), ''.join('<p>%s</p>' % x for x in (tail or [])))
    def lesson(i): return '<div class="u9-s5-g">' + ''.join('<p><b>%s</b>%s</p>' % ab for ab in C.LESSON[i]) + '</div>'
    def ctrl(f):
        if f[4] == 's':
            return '<label class="wp-label" for="u9_%s">%s</label><select class="u9-sel" id="u9_%s" data-u9="%s"><option value="">&ndash; select &ndash;</option>%s</select>' % (f[0], f[1], f[0], f[0], ''.join('<option>%s</option>' % o.replace('&', '&amp;') for o in f[5]))
        return '<label class="wp-label" for="u9_%s">%s</label><textarea class="wp-ta" id="u9_%s" data-u9="%s" placeholder="%s" style="min-height:70px;"></textarea>' % (f[0], f[1], f[0], f[0], C.esc_ph(f[5]))
    tabs = '<div class="step-tabs">' + NL + NL.join('  <div class="step-tab%s" onclick="u9Step(%d)"><div class="step-num">Step %d</div><div class="step-name">%s</div></div>' % (' active' if i == 0 else '', i, i + 1, s[1]) for i, s in enumerate(C.STEPS)) + NL + '</div>'
    lead, steps_, tail = C.HOW_S5[v]
    works = how('', steps_, lead=lead, tail=tail, cls='How Section 5 works')
    if you:
        group = '<div class="u9-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>'
        krs = '<div class="u9-h">Your group&rsquo;s two Key Results (Unit 7)</div>' + NL + '<div id="u9Krs"><p class="u9-wait">Loading your group&rsquo;s Key Results&hellip;</p></div>'
        def boxes(i):
            part = C.STEPS[i][0]; fs = [f for f in FL if f[2] == part]
            groups = []
            for f in fs:
                g = f[1].split(' · ')[0] if (' · ' in f[1] and i != 3) else 'Your group&rsquo;s rhythm'
                if i == 4: g = ' · '.join(f[1].split(' · ')[:2])
                if not groups or groups[-1][0] != g: groups.append([g, []])
                groups[-1][1].append(f)
            def lab(f):
                if i == 3: return f
                n = f[1].split(' · '); k = 2 if i == 4 else 1
                return [f[0], ' · '.join(n[k:]), f[2], f[3], f[4], f[5]]
            return NL.join('<div class="u9-s5">' + NL + '  <div class="u9-s5-h"><span class="u9-s5-n">%s</span></div>' % g + NL + '  ' + ''.join(ctrl(lab(f)) for f in fl) + NL + '</div>' for g, fl in groups)
        def panel(i):
            extra = (NL + '<div class="u9-h">Your group&rsquo;s Unit 8 decision points</div>' + NL + '<div id="u9Rd"><p class="u9-wait">Loading your group&rsquo;s decision points&hellip;</p></div>') if i == 3 else ''
            return ('<div class="step-panel%s" id="u9sp%d">' % (' active' if i == 0 else '', i + 1) + NL + how('Step %d &middot; %s' % (i + 1, C.STEPS[i][1]), C.HOW_STEP[i]) + NL +
                    '<div class="u9-h">The lesson for this step</div>' + NL + lesson(i) + extra + NL + boxes(i) + NL + '</div>')
        a51 = C.acc(C.T51, C.M51, group + NL + krs + NL + '<div id="u9S5">' + NL + tabs + NL + NL.join(panel(i) for i in range(5)) + NL + '</div>', open_=True)
        body = works + NL + a51 + NL + '<div id="u9Rec"></div>' + NL
        ids = re.findall(r'data-u9="([^"]+)"', body); assert sorted(ids) == sorted(f[0] for f in FL)
    else:
        def panel(i):
            return ('<div class="step-panel%s" id="u9sp%d">' % (' active' if i == 0 else '', i + 1) + NL +
                    '<div class="u9-h">The lesson participants see in Step %d</div>' % (i + 1) + NL + lesson(i) + NL +
                    '<div class="u9-h">What each group completes in Step %d</div>' % (i + 1) + NL + '<ul class="u9-list">' + ''.join('<li>%s</li>' % x for x in C.COMPLETES_F[i]) + '</ul>' + NL + '</div>')
        a51 = C.acc(C.T51F, C.M51, '<div id="u9S5">' + NL + tabs + NL + NL.join(panel(i) for i in range(5)) + NL + '</div>', C.activity(C.ACT_S5_F), open_=True)
        body = C.guide('FACILITATOR GUIDANCE — Application', *C.GUIDE_S5_F) + NL + works + NL + a51 + NL
        assert '<textarea' not in body and '<input' not in body and '<select' not in body
    h = C.hero('Section 5 · Application — In Practice', C.S5_TITLE, C.S5_LEAD[v])
    return h + NL + '<div class="mod-body">' + NL + C.slo(*C.SLO[5]) + NL + NL + body

def build(v, t):
    global P0, F0, FA, PA
    you = v == 'p'
    mods = ['mod0', 'mod1', 'mod2', 'mod3', 'mod4'] if you else ['mod1', 'mod2', 'mod3', 'mod4', 'mod5']
    secs = [sec1(v), sec2(v), sec3(v), sec4(v)]
    for mod, sec in zip(mods[:4], secs):
        i = t.index('id="%s"' % mod); s = t.index('<div class="mod-hero">', i); e = t.index('<div class="mod-nav"', i)
        t = t[:s] + sec + NL + t[e:]
    i = t.index('id="%s"' % mods[4]); s = t.index('<div class="mod-hero">', i)
    if you:
        e = t.index('<!-- MICRO-CLIMB SUMMARY', s)
        assert 'app_followup' in t[s:e] and 'Strategic Unclogging Tool' in t[s:e]
        t = t[:s] + section5(v) + NL + t[e:]
        t = once(t, '<!-- MICRO-CLIMB SUMMARY (standard #summaryP) -->', '<!-- UNIT SUMMARY (standard #summaryP) -->')
    else:
        a = t.index('<div class="acc-t">Unit Summary</div>', s); e = t.rindex('<div class="acc">', s, a)
        assert 'Strategic Unclogging Tool' in t[s:e] and '5.3 &mdash; Exercise Output' in t[s:e]
        t = t[:s] + section5(v) + NL + t[e:]
    root = ':root{--u9:#22a08a;--u9-bg:rgba(26,122,106,.08);--u9-bd:rgba(26,122,106,.3);}' if you else ':root{--u9:#c9a84c;--u9-bg:rgba(201,168,76,.07);--u9-bd:rgba(201,168,76,.3);}'
    k = t.index('</style>'); t = t[:k] + crlf(root + NL + read(os.path.join(HERE, 'u9.css'))) + t[k:]
    q_old = 'You stop just managing a plan and start engineering flow.'
    t = once(t, q_old, 'You start engineering flow.')
    if you:
        t = once(t, C.DESC_OLD['p'], C.DESC_NEW)
        m = re.search(r'var SUMMARY=\[\r\n(.*?)\r\n\];\r\n(?=function renderSummaryP)', t, re.S); assert m
        summ = (',' + NL).join('{arc:%s,title:%s,body:%s}' % tuple(json.dumps(x, ensure_ascii=True) for x in s) for s in C.SUM_P)
        t = t[:m.start()] + 'var SUMMARY=[' + NL + summ + NL + '];' + NL + t[m.end():]
        t = once(t, 'var KEYS=["team_name","ref1","ref2","ref3","ref4","ref5","ref6","app_prep","app_clog","app_lever","app_followup"];',
                 'var KEYS=["ref1","ref2","ref3","ref4","ref5","tc_prep","tc_diag","tc_lever"];')
        t = once(t, '["ref2","ref5","ref6","app_prep","app_clog","app_lever","app_followup"].forEach(hydrateField);',
                 '["ref2","ref5","tc_prep","tc_diag","tc_lever"].forEach(hydrateField);' + NL + '    u9Init(responses);')
        m = re.search(r'var FIELD_SPECS=\{\r\n(.*?)\r\n\};', t, re.S); assert m
        old = m.group(1).split('\r\n')
        keep = [x for x in old if x.lstrip().startswith(('ref2:', 'ref5:'))]; assert len(keep) == 2
        keep[0] = once(keep[0], '{l:"The clog I will bring to the Clog Clinic",k:"text"}', '{l:"The clog I will bring to the diagnostic triads (4.4)",k:"text"}')
        keep = [x.rstrip(',') for x in keep]
        new = keep + ['  %s:[%s]' % (key, ','.join('{l:%s,k:"text"}' % json.dumps(tag(lab).replace('&amp;', '&')) for lab, _ in flds)) for key, _, flds in C.PF]
        t = t[:m.start(1)] + (',' + NL).join(new) + t[m.end(1):]
        js = read(os.path.join(HERE, 'u9_p.js'))
        js = once(js, '/*FIELDS*/[]', json.dumps(C.fields(), ensure_ascii=False))
        js = once(js, '/*PARTS*/[]', json.dumps(C.PARTS, ensure_ascii=False))
        t = once(t, '/* \\u2500\\u2500 Init \\u2500\\u2500 */', crlf(js.strip('\n')) + NL + NL + '/* \\u2500\\u2500 Init \\u2500\\u2500 */')
        for bad in ('team_name', 'app_prep', 'app_clog', 'app_lever', 'app_followup', 'id="ref6"', 'Leave With These Three', 'Unclogging Tool'): assert bad not in t, bad
    else:
        for a, b in C.GUIDE_EDITS: t = once(t, a, b)
        for a in C.GUIDE_DROP:
            i = t.index(a); j = t.index('</p>', i) + 4
            assert t[j:j + 2] == '\r\n'; t = t[:i] + t[j + 2:]
        a = t.index('<div class="acc-t">Unit Summary</div>')
        m = re.compile(r'(<div style="display:flex;flex-wrap:wrap;gap:8px;margin:18px 0;">\r\n(?:<div style="flex:1;min-width:180px;.*?</p></div>\r\n){4})(</div>)', re.S).search(t, a); assert m
        blk = '<div style="flex:1;min-width:180px;background:#151c15;border:1px solid rgba(255,255,255,.07);border-radius:4px;padding:16px 18px;"><div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#22a08a;margin-bottom:8px;">%s</div><p style="font-size:13px;color:rgba(255,255,255,.65);line-height:1.7;">%s</p></div>' % C.SUM_F_5 + NL
        t = t[:m.end(1)] + blk + t[m.end(1):]
        t = once(t, '<strong>That conversation is the beginning of genuine execution engineering.</strong></p>', '<strong>That conversation is the beginning of genuine execution engineering.</strong>' + C.CLOSE_F_ADD + '</p>')
        t = once(t, 'function showStep(', "function u9Step(i){var r=document.getElementById('u9S5');if(!r)return;var tabs=r.querySelectorAll('.step-tab'),panels=r.querySelectorAll('.step-panel');tabs.forEach(function(x,j){x.classList.toggle('active',j===i);});panels.forEach(function(x,j){x.classList.toggle('active',j===i);});}" + NL + 'function showStep(')
        vis = tag(re.sub(r'<(script|style)\b.*?</\1>', '', t, flags=re.S))
        for bad in ('Timing', 'Spend time', 'Do not rush', '45 minutes', 'minutes', 'working days', 'non-negotiable', 'Raise your hand', 'show of hands', 'shared board', 'in front of colleagues', 'Unclogging Tool', 'auto-diagnose', 'Push every group', 'Push until'):
            assert bad not in vis, (bad, re.findall('.{60}'+re.escape(bad)+'.{20}', vis)[:3])
        assert vis.count('Watch for') == 3, vis.count('Watch for')  # the three watch points of the diagnostic triads (class practice)
        i5 = t.index('id="mod5"'); assert 'Watch for' not in tag(t[i5:])
    vis = tag(re.sub(r'<(script|style)\b.*?</\1>', '', t, flags=re.S))
    for bad in ('KR/KPI', 'lens', 'rather than', 'instead of', 'in place of', 'fundamentally different diagnostic', 'Brigade', 'is only the start', 'only half the work', 'no longer seen', 'progress is not', 'advancement is not', 'stop just', 'Clog Clinic: Exercise Structure', 'Participant Commitments', 'Your Contribution', 'Collective Capture', '5 min', '30 min', '10 min', '90 seconds', 'three minutes'):
        assert bad not in vis, (v, bad)
    assert '&mdash; or ' not in t and '— or ' not in vis, v
    assert '\n' not in t.replace('\r\n', ''), 'bare line feed in the page'
    return t

if __name__ == '__main__':
    p_in, f_in, p_out, f_out = sys.argv[1:5]
    P0, F0 = read(p_in), read(f_in); FA, PA = accs(F0), accs(P0)
    for v, src, out in (('p', P0, p_out), ('f', F0, f_out)):
        open(out, 'w', encoding='utf-8', newline='').write(build(v, src))
    print('built', p_out, f_out)
