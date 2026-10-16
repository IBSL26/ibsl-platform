# -*- coding: utf-8 -*-
"""Unit 9 · Strategic Unclogging — the two performance views (16 October 2026).
Builds the participant and facilitator pages from the 13 October rework (rebuild_u09\\build_u09.py output, the pages behind the
13 October PREVIEW copies) with every amendment Carol locked on 15 and 16 October:
Facilitator Guide · Section 1 (1.1 additions; old 1.2 removed; new 1.2 Seven Clog Map) · Section 2 guidance question ·
Section 3 (CXO Performance Clog Contributors) · Section 4 (Review–Realign–Restore and the levers) ·
Section 5 (The Strategic Unclogging Clinic, Capstone work 9A–9E) · COMPASS removed · Unit Summary.
Usage: python3 build_u09pv.py <participant 13 Oct> <facilitator 13 Oct> <participant out> <facilitator out>
Each cut checks that it finds its place exactly once. CRLF, UTF-8, lens id u3m2_lens8 unchanged."""
import sys, re, json, os
import u9pv_content as C
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'
ent = C.ent
def read(p): return open(p, encoding='utf-8', newline='').read()
def crlf(s): return s.replace('\r\n', '\n').replace('\n', '\r\n')
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:120]); return t.replace(a, b)
def tag(s): return re.sub(r'<[^>]+>', '', s)
def div_end(t, i):
    depth = 0
    for m in re.compile(r'<div\b|</div>').finditer(t, i):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0: return m.end()
    raise AssertionError('unbalanced div')
def acc_span(t, title_start, after=0):
    """(start, end) of the <div class="acc…"> whose title begins with title_start."""
    k = t.index('<div class="acc-t">' + title_start, after)
    s = max(t.rfind('<div class="acc">', 0, k), t.rfind('<div class="acc open">', 0, k)); assert s >= 0
    return s, div_end(t, s)

# ── Portfolio reflections made of several boxes (one key, "Label: value" lines, as the page's FIELD_SPECS) ──
def pf_block(spec, v):
    key, label, prompt, flds = spec
    if v == 'f':
        lead = '<p class="u9-q">The questions participants answer in their own file:</p>'
        staged = any(g for g, l, q, o in flds)
        rows, cur = [], ''
        for g, l, q, o in flds:
            if g: cur = g
            rows.append(([cur] if staged else []) + [l, '&ldquo;%s&rdquo;' % q])
        if staged:  # one stage cell per stage
            body = ''
            for i, r in enumerate(rows):
                n = sum(1 for x in rows if x[0] == r[0]); first = i == 0 or rows[i - 1][0] != r[0]
                body += '<tr>' + ('<td rowspan="%d" class="u9-stage">%s</td>' % (n, ent(r[0])) if first else '') + '<td>%s</td><td><em>%s</em></td></tr>' % (ent(r[1]), ent(r[2]))
            head = ['Stage', 'What participants record', 'The question they answer']
        else:
            body = ''.join('<tr><td>%s</td><td><em>%s</em></td></tr>' % (ent(r[0]), ent(r[1])) for r in rows)
            head = ['What participants record', 'The question they answer']
        return ('<div class="u9-fq">' + lead + '<div class="u9-tw"><table class="u9-tbl u9-rrr"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></div>' % (''.join('<th>%s</th>' % h for h in head), body))
    h = ('<div class="ref-block u9-pf"><div class="ref-label">&#x270E; Reflection &mdash; %s</div>' % ent(label) + C.PROMPT % ent(prompt) +
         '<textarea id="%s" class="reflection-textarea" style="display:none;"></textarea>' % key + NL)  # next to its question, for the Learning Portfolio
    for i, (g, lab, q, opts) in enumerate(flds):
        if g: h += '<div class="u9-sub2">%s</div>' % ent(g)
        h += '<label class="wp-label">%s</label><div class="u9-q">%s</div>' % (ent(lab), ent(q))
        if opts:
            h += '<select class="u9-sel" data-fkey="%s" data-fidx="%d" onchange="syncField(\'%s\')"><option value="">&ndash; select &ndash;</option>%s</select>' % (key, i, key, ''.join('<option>%s</option>' % o.replace('&', '&amp;') for o in opts))
        else:
            h += '<textarea class="wp-ta" data-fkey="%s" data-fidx="%d" oninput="syncFieldDebounced(\'%s\')"></textarea>' % (key, i, key)
        h += NL
    return h + '<div class="ref-saved reflection-saved" id="%s-saved"></div><button class="ref-save" onclick="fldSaveBtn(this,\'%s\')">Save</button></div>' % (key, key)
def how(title, steps): return '<div class="u9-how"><div class="u9-how-h">%s</div>%s</div>' % (ent(title), C.ol(steps, ''))
def spec_js(spec):
    return '  %s:[%s]' % (spec[0], ','.join('{l:%s,k:"text"}' % json.dumps(tag(ent(l)).replace('&amp;', '&').replace('&rsquo;', '’')) for g, l, q, o in spec[3]))

# ═══ Sections ═══
def head(n, label, title, lead, slo):
    return [C.hero(label, title, lead), '<div class="mod-body">', C.slo(*slo), '']

def sec1(v, old):
    """Section 1 from the 13 Oct body: guidance summarised, 1.1 additions, old 1.2 out, new 1.2 map in place of old 1.3."""
    t = old
    if v == 'f':
        i = t.index('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Awareness</div>')
        t = t[:i] + C.guide('FACILITATOR GUIDANCE — Awareness', *C.GUIDE_S1) + t[div_end(t, i):]
    a, b = C.OPEN_11[v]
    t = once(t, a, ent(b) + NL + ent(C.OPEN_11_TAIL))
    sl = '<div class="hbox blue" style="margin-top:14px;"><p><strong>System Logic:</strong>'
    i = t.index(sl); j = div_end(t, i)
    t = t[:j] + NL + C.WHERE_FORM + t[j:]
    if v == 'p':
        q = 'Could it have been named earlier?</p>'
        t = once(t, q, 'Could it have been named earlier?' + ent(C.REF1_ADD) + '</p>')
        t = once(t, 'placeholder="The initiative:&#10;The blockage:&#10;Could it have been named earlier?"', 'placeholder="The initiative:&#10;The blockage:&#10;Could it have been named earlier?&#10;The organisational condition:"')
    else:
        t = once(t, '<p>Participants write a reflection in their own file: a strategy initiative that stalled in their organisation, the blockage behind it, and whether it could have been named earlier.</p>', '<p>%s</p>' % ent(C.ACT_11))
    s, e = acc_span(t, '1.2 &mdash; Three Observable Friction Signals'); t = t[:s] + t[e:].lstrip('\r\n')
    s, e = acc_span(t, '1.3 &mdash; The 7-Clog Diagnostic Map'); old13 = t[s:e]
    if v == 'p':
        k = old13.index('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; Which Clogs Are Active?</div>'); blk = old13[k:div_end(old13, k)]
        blk = once(blk, 'Rate each clog in your current strategy portfolio (1 = absent, 5 = active). Then name the clog you will bring to the diagnostic triads in part 4.4.', ent(C.REF2_PROMPT))
        blk = once(blk, '<label class="fld-label">The clog I will bring to the diagnostic triads (4.4)</label>', '<label class="fld-label">%s</label>' % ent(C.REF2_FIELD))
        hid = '<textarea id="ref2" class="reflection-textarea" style="display:none;"></textarea>'
        blk = once(blk, hid, ''); k2 = blk.index('</p>', blk.index('class="ref-prompt"')) + 4; blk = blk[:k2] + hid + blk[k2:]
        new = C.acc(C.T12, C.M12, C.map12() + NL + blk)
    else:
        new = C.acc(C.T12, C.M12, C.map12(), C.activity(C.ACT_12))
    t = t[:s] + new + t[e:]
    return t

def sec2(v, old):
    if v == 'f': old = once(old, C.S2_Q_OLD, C.S2_Q_NEW)
    return old

def sec3(v):
    out = head(3, 'Section 3 · Extrapolating — Where', C.S3_TITLE, C.S3_LEAD, C.SLO[3])
    if v == 'f': out += [C.guide('FACILITATOR GUIDANCE — Extrapolating', *C.GUIDE_S3), '']
    body = [C.P(*C.S31_INTRO), C.roles(v)]
    if v == 'p':
        body += ['<div class="u9-h">Personal reflection &middot; Portfolio Work</div>', how('Portfolio work · How to complete this reflection', C.HOW_REF7), pf_block(C.REF7, 'p')]
        out.append(C.acc(C.T31, C.M31, NL.join(body), open_=True))
    else:
        body += ['<div class="u9-h">Personal reflection &middot; Portfolio Work: %s</div>' % ent(C.REF7[1]), C.P(C.REF7[2]), pf_block(C.REF7, 'f')]
        out.append(C.acc(C.T31, C.M31, NL.join(body), C.activity(C.ACT_31), open_=True))
    out += ['', '<div class="hbox" style="margin-top:6px;"><div class="u9-ex-h">Closing Insight</div>' + C.P(*C.S3_CLOSE) + '</div>', '']
    return NL.join(out)

def sec4(v):
    out = head(4, 'Section 4 · Integration — Collective', C.S4_TITLE, C.S4_LEAD, C.SLO[4])
    if v == 'f': out += [C.guide('FACILITATOR GUIDANCE — Integration', *C.GUIDE_S4), '']
    for a in C.s4_parts(v): out += [a, '']
    if v == 'p':
        body = NL.join([how('Portfolio work · How to complete this reflection', C.HOW_REF8), pf_block(C.REF8, 'p')])
        out.append(C.acc(C.T46, C.M46, body))
    else:
        body = NL.join([C.P(C.REF8[2]), pf_block(C.REF8, 'f'), C.guide('Facilitator Closing Note — Integration', *C.CLOSE_S4)])
        out.append(C.acc(C.T46, C.M46, body, C.activity(C.ACT_46)))
    out.append('')
    return NL.join(out)

def sec5(v):
    you = v == 'p'; FL = C.fields()
    def box(f):
        if not you:
            return '<div class="u9-brief"><b>%s</b><span>%s</span></div>' % (ent(f[1]), ent(f[6]))
        lab = f[1].split(' · ')[-1]
        q = '' if f[6] == lab else '<div class="u9-q">%s</div>' % ent(f[6])
        if f[4] == 's':
            ctl = '<select class="u9-sel" id="u9_%s" data-u9="%s"><option value="">&ndash; select &ndash;</option>%s</select>' % (f[0], f[0], ''.join('<option>%s</option>' % o.replace('&', '&amp;') for o in f[5]))
        else:
            ctl = '<textarea class="wp-ta" id="u9_%s" data-u9="%s" placeholder="%s" style="min-height:64px;"></textarea>' % (f[0], f[0], C.esc_ph(f[5]))
        return '<div class="u9-s5"><label class="wp-label" for="u9_%s">%s</label>%s%s</div>' % (f[0], ent(lab), q, ctl)
    def boxes(ids): return NL.join(box(f) for f in FL if f[0] in ids)
    tag_ = '<div class="u9-tagline">Group response</div>' if you else '<div class="u9-tagline">What each group completes</div>'
    a = []
    krs = (NL + '<div class="u9-h">Your group&rsquo;s Key Results from Unit 7, for reference</div>' + NL + '<div id="u9Krs"><p class="u9-wait">Loading your group&rsquo;s Key Results&hellip;</p></div>') if you else ''
    p51 = [C.P('Review the organisational challenges your group documented before CESI began. Select one challenge that remains relevant to your Capstone organisation and has a clear connection to disappointing organisational results.'),
           krs.lstrip('\r\n'), tag_, boxes(['ch_challenge', 'ch_link']),
           C.P('Use existing Capstone performance information where available. If the group has not established a current result, agree on a realistic illustrative figure consistent with its organisational scenario.')]
    if you:
        group = '<div class="u9-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>'
        p51 = [group] + p51
        a.append(C.acc('5.1 — Return to Your Original Work-Based Challenge', 'Capstone Work', NL.join(p51), open_=True))
    else:
        a.append(C.acc('5.1 — Return to Your Original Work-Based Challenge', 'Capstone Work', NL.join(p51), C.activity(C.ACT_S5), open_=True))
    a.append(C.acc('5.2 — Identify the Performance Clog', 'Capstone Work', NL.join([
        C.P('Examine the selected challenge and identify which of the Seven Performance Clogs best explains the difficulty. The challenge describes what has been experienced; the clog identifies the organisational condition believed to be constraining performance.'),
        C.table(['Seven Performance Clogs', 'Diagnostic focus'], C.CLOG_ROWS), tag_, boxes(['cl_clog', 'cl_why']),
        C.P('Treat this as the initial diagnosis. The group will test it during REVIEW.')])))
    a.append(C.acc('5.3 — Select the Strategic Unclogging Lever', 'Capstone Work', NL.join([
        C.P('Now select the established Strategic Unclogging Lever most appropriate for removing the identified obstruction. One clog may have more than one suitable lever; select the primary lever that best addresses the specific condition in your case.'),
        C.table(['Seven Strategic Unclogging Levers', 'Purpose', 'Common application'], C.LEVER_ROWS), tag_, boxes(['lv_lever', 'lv_why']),
        C.P('The selected lever is tested and activated through Review–Realign–Restore. Selection at this stage does not mean intervention begins before the diagnosis has been confirmed.')])))
    a.append(C.acc('5.4 — Apply Review–Realign–Restore', 'Capstone Work', NL.join(C.fold([
        C.fsub('REVIEW — Confirm the Performance Reality'),
        C.P('Use the Three Performance Lines of Sight to test the initial diagnosis and establish the evidence for intervention.'),
        tag_, boxes(['rv_outcome', 'rv_behaviour', 'rv_condition', 'rv_check']),
        C.fsub('REALIGN — Agree on the Collective Response'),
        C.P('As the simulated executive team, determine what must change and identify who has the authority and responsibility to act. Explicitly consider both dimensions of performance.'),
        tag_, boxes(['ra_people', 'ra_org']),
        '<div class="u9-sub2">Leadership agreement</div>', boxes(['ra_owner', 'ra_contrib', 'ra_change', 'ra_each']),
        C.fsub('RESTORE — Activate the Selected Lever'),
        C.P('Specify how the confirmed Strategic Unclogging Lever will be applied. The action must directly remove or reduce the identified condition and be clear enough for the responsible executive to implement.'),
        tag_, boxes(['rs_intervention', 'rs_action', 'rs_people', 'rs_org', 'rs_review'])]))))
    a.append(C.acc('5.5 — Diagnostic Quality Check', 'Before the response is finalised', NL.join([
        C.P('Before the group finalises its response, test it against four criteria:'), C.ol(C.QUALITY),
        C.P('If any criterion is not met, return to the relevant step and refine the response.')])))
    if you:
        a.append(C.acc('5.6 — The Strategic Unclogging Clinic Record', 'Read the record and Confirm', NL.join([C.P('Read your group’s record. When every entry is complete, select Confirm. Your confirmed record feeds boxes 9A to 9E of your team’s Capstone Blueprint.'), '<div id="u9Rec"></div>'])))
    else:
        a.append(C.acc('5.6 — The Strategic Unclogging Clinic Record', 'Read the record and Confirm', NL.join([C.P('Each member reads the group’s record on their own page and selects Confirm. The confirmed record feeds boxes 9A to 9E of the team’s Capstone Blueprint.'),
                C.guide('Facilitator Closing Note — Application', *C.CLOSE_S5)])))
    out = [C.hero('Section 5 · Application — In Practice', C.S5_TITLE, C.S5_LEAD), '<div class="mod-body">', C.slo(*C.SLO[5]), '']
    if not you: out += [C.guide('FACILITATOR GUIDANCE — The Clog Clinic', *C.GUIDE_S5), '']
    output = ('<div class="u9-out-box"><div class="u9-how-h">Capstone Portfolio Output</div>' + C.P('The group submits one Strategic Unclogging Clinic Record containing:') + C.ol(C.OUTPUT) +
              C.P('The completed record is incorporated into the existing Capstone portfolio.') + '</div>')
    out += [how('How Section 5 works', C.HOW_S5[v]), output, '<div id="u9S5">'] + a + ['</div>', '']
    body = NL.join(out)
    if you:
        ids = re.findall(r'data-u9="([^"]+)"', body); assert sorted(ids) == sorted(f[0] for f in FL), ids
    else:
        assert '<textarea' not in body and '<input' not in body and '<select' not in body
    return body

U9ROLE_JS = "function u9Role(b,i){var w=b.closest('.cb');w.querySelectorAll('.u9-role-b').forEach(function(x,j){x.classList.toggle('on',j===i);});w.querySelectorAll('.u9-role').forEach(function(x,j){x.classList.toggle('on',j===i);});}"

def build(v, t):
    you = v == 'p'
    mods = ['mod0', 'mod1', 'mod2', 'mod3', 'mod4'] if you else ['mod1', 'mod2', 'mod3', 'mod4', 'mod5']
    def span(mod, end_marker=None):
        i = t.index('id="%s"' % mod); s = t.index('<div class="mod-hero">', i)
        e = t.index(end_marker, s) if end_marker else t.index('<div class="mod-nav"', i)
        return s, e
    # Sections 5 to 1, from the end, so earlier offsets stay valid
    if you: s, e = span(mods[4], '<!-- UNIT SUMMARY (standard #summaryP) -->')
    else:
        s, _ = span(mods[4]); a = t.index('<div class="acc-t">Unit Summary</div>', s); e = t.rindex('<div class="acc">', s, a)
    t = t[:s] + sec5(v) + NL + t[e:]
    s, e = span(mods[3]); t = t[:s] + sec4(v) + t[e:]
    s, e = span(mods[2]); t = t[:s] + sec3(v) + t[e:]
    s, e = span(mods[1]); t = t[:s] + sec2(v, t[s:e]) + t[e:]
    s, e = span(mods[0]); t = t[:s] + sec1(v, t[s:e]) + t[e:]
    # page CSS
    css = read(os.path.join(HERE, 'u9pv.css'))
    k = t.index('</style>'); t = t[:k] + crlf(css) + t[k:]
    if you:
        m = re.search(r'var SUMMARY=\[\r\n(.*?)\r\n\];\r\n(?=function renderSummaryP)', t, re.S); assert m
        summ = (',' + NL).join('{arc:%s,title:%s,body:%s}' % tuple(json.dumps(ent(x), ensure_ascii=True) for x in s) for s in C.SUM_P)
        t = t[:m.start()] + 'var SUMMARY=[' + NL + summ + NL + '];' + NL + t[m.end():]
        t = once(t, 'var KEYS=["ref1","ref2","ref3","ref4","ref5","tc_prep","tc_diag","tc_lever"];', 'var KEYS=["ref1","ref2","ref3","ref4","ref7","ref8"];')
        t = once(t, '["ref2","ref5","tc_prep","tc_diag","tc_lever"].forEach(hydrateField);', '["ref2","ref7","ref8"].forEach(hydrateField);')
        m = re.search(r'var FIELD_SPECS=\{\r\n(.*?)\r\n\};', t, re.S); assert m
        old = m.group(1).split('\r\n'); keep = [x.rstrip(',') for x in old if x.lstrip().startswith('ref2:')]; assert len(keep) == 1
        keep[0] = once(keep[0], '{l:"The clog I will bring to the diagnostic triads (4.4)",k:"text"}', '{l:%s,k:"text"}' % json.dumps(C.REF2_FIELD))
        t = t[:m.start(1)] + (',' + NL).join(keep + [spec_js(C.REF7), spec_js(C.REF8)]) + t[m.end(1):]
        # Section 5 tool: replace the 13 Oct Clog Clinic block with the Strategic Unclogging Clinic block
        a = t.index("/* ════════════ UNIT 9 · SECTION 5 · THE CLOG CLINIC"); b = t.index('/* \\u2500\\u2500 Init \\u2500\\u2500 */', a)
        js = read(os.path.join(HERE, 'u9pv_p.js'))
        js = once(js, '/*FIELDS*/[]', json.dumps(C.fields(), ensure_ascii=False))
        js = once(js, '/*PARTS*/[]', json.dumps([list(p[:5]) for p in C.PARTS], ensure_ascii=False))
        t = t[:a] + crlf(js.strip('\n') + NL + U9ROLE_JS) + NL + NL + t[b:]
        for bad in ('tc_prep', 'tc_diag', 'tc_lever', 'id="ref5"', 'id="ref6"', 'uc_signals', 'u9Rd', 'k1_signal'): assert bad not in t, bad
    else:
        t = once(t, C.REFRAME_OLD, C.REFRAME_NEW)
        t = once(t, C.CLINIC_OLD, C.CLINIC_NEW)
        t = once(t, '<li><em>&ldquo;You&rsquo;ve selected a lever. What would have to be true for that lever to actually clear the clog?&rdquo;</em></li>' + NL + '</ul></div>',
                 '<li><em>&ldquo;You&rsquo;ve selected a lever. What would have to be true for that lever to actually clear the clog?&rdquo;</em></li>' + NL + C.KFQ_ADD + NL + '</ul></div>')
        tone = '<p><strong>Teach what a lever is.</strong>'; i = t.index(tone); j = t.index('</p>', i) + 4
        t = t[:j] + NL + C.TONE_ADD + t[j:]
        a = t.index('<div class="acc-t">Unit Summary</div>')
        blocks = list(re.compile(r'<div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:[^;]+;margin-bottom:8px;">(.*?)</div><p style="font-size:13px;color:rgba\(255,255,255,\.65\);line-height:1\.7;">(.*?)</p>').finditer(t, a))
        assert len(blocks) == 5, len(blocks)
        for m, (lab, txt) in reversed(list(zip(blocks, C.SUM_F))):
            assert tag(m.group(1)).replace('&mdash;', '—').strip() == lab or ent(lab) == m.group(1), (m.group(1), lab)
            if txt: t = t[:m.start(2)] + ent(txt) + t[m.end(2):]
        t = once(t, 'function showStep(', U9ROLE_JS + NL + 'function showStep(')
    for x, y in C.VOICE[v]:
        assert t.count(ent(x)) >= 1, x; t = t.replace(ent(x), ent(y))
    vis = tag(re.sub(r'<(script|style)\b.*?</\1>', '', t, flags=re.S))
    for bad in ('COMPASS', 'KR/KPI', 'lens', 'rather than', 'instead of', 'in place of', 'Brigade', 'Friction Signals', 'diagnostic triads', 'minutes', 'Timing', 'Suggested timing', 'Enterprise Unclogging Agenda', 'High-Flammability', 'Watch for'):
        assert bad not in vis, (v, bad, re.findall('.{60}' + re.escape(bad) + '.{30}', vis)[:2])
    assert 'S2R ' not in vis.replace('S2R®', ''), v
    assert '\n' not in t.replace('\r\n', ''), 'bare line feed in the page'
    return t

if __name__ == '__main__':
    p_in, f_in, p_out, f_out = sys.argv[1:5]
    for v, src, out in (('p', p_in, p_out), ('f', f_in, f_out)):
        open(out, 'w', encoding='utf-8', newline='').write(build(v, read(src)))
    print('built', p_out, f_out)
