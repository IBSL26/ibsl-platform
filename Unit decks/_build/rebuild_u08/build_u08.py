# -*- coding: utf-8 -*-
"""Unit 8 · Performance Measurement — builds the amended participant and facilitator pages (findings report of 12 October 2026, approved by Carol: "Happy with your suggestions").
Usage: python3 build_u08.py <participant page before> <facilitator page before> <participant out> <facilitator out>
Input: Claude outputs\\Backups\\Unit 8 file backups\\unit3_m2_lens7_[p|f] - before amendments (12 Oct).html
The five sections are rebuilt from u8_content.py; the page shell (header, tabs, sign-in checks, submission cluster, scripts) stays as it was.
Each cut and replacement checks that it finds its place exactly once. Line endings stay CRLF, encoding UTF-8, lens id u3m2_lens7 unchanged."""
import sys, re, json, os
import u8_content as C
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'
def read(p): return open(p, encoding='utf-8', newline='').read()
def crlf(s): return s.replace('\r\n', '\n').replace('\n', '\r\n')
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:110]); return t.replace(a, b)
def tag(s): return re.sub(r'<[^>]+>', '', s)
ACC_OPEN = re.compile(r'<div class="acc(?: open)?"(?: id="[^"]*")?(?: style="[^"]*")?>\r\n')
def acc_start(t, i):
    last = None
    for m in ACC_OPEN.finditer(t, max(0, i - 400), i): last = m
    assert last is not None; return last.start()

def section5(v):
    FL = C.fields(); you = v == 'p'
    def ta(f): return '<label class="wp-label" for="u8_%s">%s</label><textarea class="wp-ta" id="u8_%s" data-u8="%s" placeholder="%s" style="min-height:80px;"></textarea>' % (f[0], f[1], f[0], f[0], C.esc_ph(f[5]))
    def how(title, steps, lead=None, tail=None, cls='Capstone work &middot; How to complete '):
        tails = ''.join('<p>%s</p>' % x for x in (tail or []))
        return '<div class="u8-how"><div class="u8-how-h">%s%s</div>%s<ol>%s</ol>%s</div>' % (cls, title, ('<p>%s</p>' % lead) if lead else '', ''.join('<li>%s</li>' % s for s in steps), tails)
    def lesson(i): return '<div class="u8-s5-g">' + ''.join('<p><b>%s</b>%s</p>' % (a, b) for a, b in C.lesson5(i)) + '</div>'
    def lst(items): return '<ul class="u8-list">' + ''.join('<li>%s</li>' % x for x in items) + '</ul>'
    tabs = '<div class="step-tabs">' + NL + NL.join('  <div class="step-tab%s" onclick="u8Step(%d)"><div class="step-num">Consequence %d</div><div class="step-name">%s</div></div>' % (' active' if i == 0 else '', i, i + 1, c[1]) for i, c in enumerate(C.CONSEQ)) + NL + '</div>'
    lead, steps_, tail = C.HOW_S5[v]
    works = how('', steps_, lead=lead, tail=tail, cls='How Section 5 works')
    if you:
        group = '<div class="u8-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>'
        def panel(i):
            fs = [f for f in FL if f[2] == 'c%d' % (i + 1)]
            return ('<div class="step-panel%s" id="u8sp%d">' % (' active' if i == 0 else '', i + 1) + NL + how('Consequence %d &middot; %s' % (i + 1, C.CONSEQ[i][1]), C.how_step_p(i)) + NL +
                    '<div class="u8-h">The lesson for this consequence</div>' + NL + lesson(i) + NL +
                    '<div class="u8-s5">' + NL + '  <div class="u8-s5-h"><span class="u8-s5-n">Your two decision points</span></div>' + NL + '  ' + ''.join(ta(f) for f in fs) + NL + '</div>' + NL + '</div>')
        a51 = C.acc(C.T51, C.M51, group + NL + '<div id="u8S5">' + NL + tabs + NL + NL.join(panel(i) for i in range(4)) + NL + '</div>', open_=True)
        body = works + NL + a51 + NL + '<div id="u8Rec"></div>' + NL
        ids = re.findall(r'data-u8="([^"]+)"', body); assert sorted(ids) == sorted(f[0] for f in FL)
    else:
        def panel(i):
            return ('<div class="step-panel%s" id="u8sp%d">' % (' active' if i == 0 else '', i + 1) + NL +
                    '<div class="u8-h">The lesson participants see for consequence %d</div>' % (i + 1) + NL + lesson(i) + NL +
                    '<div class="u8-h">What each group completes for consequence %d</div>' % (i + 1) + NL + lst(C.COMPLETES_F[i]) + NL + '</div>')
        a51 = C.acc(C.T51, C.M51, '<div id="u8S5">' + NL + tabs + NL + NL.join(panel(i) for i in range(4)) + NL + '</div>', C.activity(C.ACT_S5_F), open_=True)
        body = C.guide('FACILITATOR GUIDANCE — Application', *C.GUIDE_S5_F) + NL + works + NL + a51 + NL
        assert '<textarea' not in body and '<input' not in body and '<select' not in body
        for bad in ('Listen for', 'Challenge any', 'Watch for', 'Check that', 'Push back', 'Probe', 'Redirect'): assert bad not in tag(body), bad
    h = C.hero('Section 5 · Application — In Practice', C.S5_TITLE, C.S5_LEAD[v])
    return h + NL + '<div class="mod-body">' + NL + C.slo(*C.SLO5) + NL + NL + body

def build(v, t):
    you = v == 'p'
    mods = ['mod0', 'mod1', 'mod2', 'mod3', 'mod4'] if you else ['mod1', 'mod2', 'mod3', 'mod4', 'mod5']
    secs = [C.sec1(v), C.sec2(v), C.sec3(v), C.sec4(v)]
    for mod, sec in zip(mods[:4], secs):
        i = t.index('id="%s"' % mod); s = t.index('<div class="mod-hero">', i); e = t.index('<div class="mod-nav"', i)
        t = t[:s] + sec + NL + t[e:]
    i = t.index('id="%s"' % mods[4]); s = t.index('<div class="mod-hero">', i)
    if you:
        e = t.index('<!-- MICRO-CLIMB SUMMARY', s)
        assert 'app_loop_reflection' in t[s:e] and '5.1 &mdash; The Accountability Loop Role Play' in t[s:e]
        t = t[:s] + section5(v) + NL + t[e:]
        t = once(t, '<!-- MICRO-CLIMB SUMMARY (standard #summaryP) -->', '<!-- UNIT SUMMARY (standard #summaryP) -->')
    else:
        e = acc_start(t, t.index('class="acc-t">Unit Summary'))
        assert 'Facilitator Capture' in t[s:e] and 'board-zone' in t[s:e]
        t = t[:s] + section5(v) + NL + t[e:]
    root = ':root{--u8:#22a08a;--u8-bg:rgba(26,122,106,.08);--u8-bd:rgba(26,122,106,.3);}' if you else ':root{--u8:#c9a84c;--u8-bg:rgba(201,168,76,.07);--u8-bd:rgba(201,168,76,.3);}'
    k = t.index('</style>'); t = t[:k] + crlf(root + NL + read(os.path.join(HERE, 'u8.css'))) + t[k:]
    if you:
        t = once(t, C.DESC_OLD['p'], C.DESC_NEW)
        m = re.search(r'var SUMMARY=\[\r\n(.*?)\r\n\];\r\n(?=function renderSummaryP)', t, re.S); assert m
        summ = (',' + NL).join('{arc:%s,title:%s,body:%s}' % tuple(json.dumps(x, ensure_ascii=True) for x in s) for s in C.SUM_P)
        t = t[:m.start()] + 'var SUMMARY=[' + NL + summ + NL + '];' + NL + t[m.end():]
        t = once(t, 'var KEYS=["team_name","ref1","ref2","ref3","ref4","ref5","ref6","ref7","app_syn_pattern","app_syn_repeat","app_syn_depend","app_syn_chain","app_syn_decision","app_rootcause","app_corrective","app_loop_reflection"];',
                 'var KEYS=["ref1","ref2","ref4","ref5","ref6","ref7","rp_review","app_rootcause","app_corrective","rp_judge"];')
        a = 'hydrateScores("ref4");'
        t = once(t, a, a + NL + '    u8Init(responses);')
        FL = C.fields()
        js = read(os.path.join(HERE, 'u8_p.js'))
        js = once(js, '/*FIELDS*/[]', json.dumps(FL, ensure_ascii=False))
        js = once(js, '/*PARTS*/[]', json.dumps(C.PARTS, ensure_ascii=False))
        t = once(t, '/* \\u2500\\u2500 Init \\u2500\\u2500 */', crlf(js.strip('\n')) + NL + NL + '/* \\u2500\\u2500 Init \\u2500\\u2500 */')
        for bad in ('team_name', 'app_syn_', 'app_loop_reflection', '5-Day', '5-day', 'Save Commitment', 'Report Role', 'id="ref3"', 'rp_score'): assert bad not in t, bad
    else:
        for a, b in C.GUIDE_EDITS: t = once(t, a, b)
        for a in C.GUIDE_DROP:
            i = t.index(a); j = t.index('</p>', i) + 4
            assert t[j:j + 2] == '\r\n'; t = t[:i] + t[j + 2:]
        a = '<p><strong>Watch for:</strong> leaders who treat the Accountability Loop as a confrontation tool.'
        i = t.index(a); j = t.index('</p>', i) + 4; t = t[:j] + NL + C.GUIDE_ADD + t[j:]
        m = re.search(r'(<div style="display:flex;flex-wrap:wrap;gap:8px;margin:18px 0;">\r\n)((?:<div style="flex:1;min-width:180px;.*?</p></div>\r\n){4})(</div>)', t, re.S); assert m
        blk = ''.join('<div style="flex:1;min-width:180px;background:#151c15;border:1px solid rgba(255,255,255,.07);border-radius:4px;padding:16px 18px;"><div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:8px;">%s</div><p style="font-size:13px;color:rgba(255,255,255,.65);line-height:1.7;">%s</p></div>' % (c, a, b) + NL for a, c, b in C.SUM_F)
        t = t[:m.start(2)] + blk + t[m.end(2):]
        m = re.search(r'<p>Close by asking each leader to name one performance KPI they own.*?</p>', t); assert m
        t = t[:m.start()] + '<p>%s</p>' % C.CLOSE_F + t[m.end():]
        t = once(t, 'function toggleGap(c){c.classList.toggle(\'open\');}', 'function toggleGap(c){c.classList.toggle(\'open\');}' + NL +
                 "function showU8Cxo(card,id){document.querySelectorAll('.u8-cx-card').forEach(function(c){c.classList.toggle('active',c===card);});document.querySelectorAll('.u8-cx-detail').forEach(function(d){d.classList.toggle('visible',d.id===id);});}" + NL +
                 "function u8Step(i){var r=document.getElementById('u8S5');if(!r)return;var tabs=r.querySelectorAll('.step-tab'),panels=r.querySelectorAll('.step-panel');tabs.forEach(function(x,j){x.classList.toggle('active',j===i);});panels.forEach(function(x,j){x.classList.toggle('active',j===i);});}")
        vis = tag(re.sub(r'<(script|style)\b.*?</\1>', '', t, flags=re.S))
        for bad in ('Timing', 'Spend time', 'Protect time', 'adequate time', 'five working days', 'five-day', 'non-negotiable', 'physical or digital', 'Collective Intelligence Board', 'Report Role', 'session runs short'):
            assert bad not in vis, bad
    vis = tag(re.sub(r'<(script|style)\b.*?</\1>', '', t, flags=re.S))
    for bad in ('Collective Intelligence Circle', 'Collective Intelligence Principle', 'Synthesis Layer', 'Execution Discipline: The Real', 'Three Progress Signals', 'Enables Learning', 'Course Correction', 'Visibility Shift', 'Leader Avoided Blame', 'KR/KPI', 'KPI/KR', 'ROI', 'lens', 'rather than', 'instead of', 'in place of', 'fundamentally different', 'four criteria'):
        assert bad not in vis, (v, bad)
    assert '\n' not in t.replace('\r\n', ''), 'bare line feed in the page'
    return t

if __name__ == '__main__':
    p_in, f_in, p_out, f_out = sys.argv[1:5]
    for v, src, out in (('p', p_in, p_out), ('f', f_in, f_out)):
        open(out, 'w', encoding='utf-8', newline='').write(build(v, read(src)))
    print('built', p_out, f_out)
