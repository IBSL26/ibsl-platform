# -*- coding: utf-8 -*-
"""Unit 11 Section 5 · The Cross-CXO Organisational Health Clinic (HTML). Text in u11_s5a.py; group record logic in u11_s5.js."""
import os, json
from u11_content import acc, det
from u11_s4 import tbln, formula, ci
from u11_s5a import *

def rnd(n): return 'R{:,}'.format(n)
def box(lbl, txt): return '<div class="hbox"><p><strong>%s:</strong> %s</p></div>' % (lbl, txt)
def ta(path, label): return '<label class="fld-label">%s</label><textarea class="fld-input u11-ta" data-u11="%s"></textarea>' % (label, path)
def kv_empty(h1, h2, rows): return tbln([h1, h2], [(r, '') for r in rows])

def section5(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    b = ['<p>%s</p>' % OV1, '<p>%s</p>' % (OV2_F if fac else OV2_P), box('Capstone instruction', (CAP_F if fac else CAP_P).replace('ONLY', '<strong>only</strong>'))]
    if not fac:
        b.append('<div class="u11-how"><div class="u11-how-h">Capstone work &middot; How Section 5 works</div><ol>%s</ol></div>' % ''.join('<li>%s</li>' % x for x in HOW))
    o.append(acc('5.1 &mdash; Application Overview', '\n'.join(b), True))
    if not fac:
        o.append('<div id="u11TwBar"></div>')
    # 5.2
    ref = [list(r) for r in ROLES] + [['SELECTED ROLES', 'Group consolidation'] + ['—'] * 8]
    b = ['<p>%s</p>' % S52]
    if fac:
        b.append(tbln(['CXO','Function','Staff','No. of Responses','Politics','Confusion','Morale','Productivity','Turnover','Total'], [[str(x) for x in r] for r in ref]))
    else:
        b += ['<div class="u11-sub">Your group’s CXO roles</div><div id="u11Roles" class="u11-roles"></div>', '<div id="u11Ref52"></div>']
    b.append('<h4 class="u11-h">Task 1 &mdash; Interpret the Functional Health Position</h4><p>%s</p>' % T1)
    b.append(tbln(['Score', 'Health classification'], BANDS))
    if fac:
        b.append(kv_empty('Functional assessment', 'CXO finding', T1_ROWS))
    else:
        b.append('<p>Each function your group ticked has its own card below, for Task 1 here and Task 2 in part 5.3.</p><div id="u11Fns"></div>')
    o.append(acc('5.2 &mdash; Functional Organisational Health Assessment', '\n'.join(b), meta='Tasks 1 and 2'))
    # 5.3
    b = ['<p>%s</p>' % S53]
    if fac:
        rows = [[c] + [rnd(x) for x in LOSSES[c]] + [rnd(sum(LOSSES[c]))] for c, *_ in ROLES] + [['SELECTED ROLES', 'Calculate', '—', '—', '—', '—', '—']]
        b.append(tbln(['CXO'] + COSTS + ['Gross Total'], rows))
    else:
        b.append('<div id="u11Ref53"></div>')
    b.append('<h4 class="u11-h">Task 2 &mdash; Interpret Functional Losses</h4><p>%s</p>' % T2)
    if not fac:
        b.append('<p class="u11-note">Complete Task 2 in each function’s card in part 5.2.</p>')
    o.append(acc('5.3 &mdash; Quantifying Functional People-Performance Losses', '\n'.join(b)))
    # 5.4
    b = ['<p>%s</p>' % S54, formula(*F54), '<h4 class="u11-h">Task 3 &mdash; Calculate the Consolidated Health Score</h4>']
    if fac:
        b.append(kv_empty('Organisational health trait', 'Enterprise score /20', TRAITS + ['Enterprise Health Score /100']))
    else:
        b.append('<div id="u11T3"></div>')
    b.append('<h4 class="u11-h">Task 4 &mdash; Interpret the Consolidated Health Position</h4><p>%s</p>' % T4)
    if not fac:
        b.append('<table class="u11-tbl u11-kv"><tbody><tr><td>Consolidated score and classification</td><td id="u11T4s">—</td></tr><tr><td>Two weakest traits</td><td id="u11T4w">—</td></tr></tbody></table>'
                 + ta('t4-contrib', 'Functions contributing most to those weaknesses') + ta('t4-xvuln', 'Vulnerabilities requiring cross-functional leadership attention'))
    o.append(acc('5.4 &mdash; Consolidating the Capstone Group Health Position', '\n'.join(b), meta='Tasks 3 and 4'))
    # 5.5
    b = ['<h4 class="u11-h">Task 5 &mdash; Calculate Gross Quarterly Exposure for the Selected Functions</h4><p>%s</p>' % T5]
    if fac:
        b.append(kv_empty('Hidden cost', 'Enterprise quarterly exposure', COST_NAMES + ['Total Gross Quarterly Exposure']))
    else:
        b += ['<div id="u11T5"></div>', ta('t5-overlap', 'Possible overlaps flagged before presenting gross exposure')]
    b.append('<h4 class="u11-h">Task 6 &mdash; Establish the Consolidated Health Diagnosis</h4><p>%s</p>' % T6)
    if fac:
        b.append(kv_empty('Enterprise assessment dimension', 'EXCO finding', T6_ROWS))
    else:
        b.append('<table class="u11-tbl u11-kv"><thead><tr><th>Enterprise assessment dimension</th><th>EXCO finding</th></tr></thead><tbody>'
                 '<tr><td>%s</td><td id="u11T6s">—</td></tr><tr><td>%s</td><td id="u11T6w">—</td></tr><tr><td>%s</td><td id="u11T6g">—</td></tr><tr><td>%s</td><td id="u11T6c">—</td></tr></tbody></table>' % (T6_ROWS[0], T6_ROWS[1], T6_ROWS[3], T6_ROWS[4])
                 + ta('t6-funcs', T6_ROWS[2]) + ta('t6-cult', T6_ROWS[5]) + ta('t6-people', T6_ROWS[6]))
    o.append(acc('5.5 &mdash; Quantifying Losses Across the Selected Functions', '\n'.join(b), meta='Tasks 5 and 6'))
    # 5.6
    b = []
    for k, (w, sub, txt, out) in enumerate(RRR):
        blk = '<p>%s</p><p><strong>Output:</strong> %s</p>' % (txt, out)
        if not fac:
            blk += ta('rrr-' + w.lower(), out[:-1])
        b.append(det('%s &mdash; %s' % (w, sub), blk, k == 0))
    o.append(acc('5.6 &mdash; Determine Remedial Actions Through Review–Realign–Restore', '\n'.join(b)))
    # 5.7
    b = ['<h4 class="u11-h">Task 7 &mdash; Complete the Simplified Organisational Health Response</h4>']
    if fac:
        b.append(tbln(T7_H, [['', '', '', '', '', '']] * 3))
        b += ['<p>%s</p>' % T7A, '<p>%s</p>' % T7B]
    else:
        b += ['<p>%s</p>' % T7A, '<p>%s</p>' % T7B, '<div class="hbox"><p id="u11Low"></p></div>', '<div id="u11Resp"></div>',
              '<button type="button" class="ref-save u11-add" onclick="u11AddResp()">+ Add a response</button>']
    o.append(acc('5.7 &mdash; Consolidated Organisational Health Response', '\n'.join(b), meta='Task 7'))
    # 5.8 Cultural Operating Code (Carol 22:37), then the output as 5.9
    import u11_coc
    o.append(u11_coc.part58(fac))
    b = ['<p>%s</p>' % OUT58, '<p><strong>%s</strong></p>' % OUT58B]
    if not fac:
        b.append('<div class="u11-rec"><div id="u11RecMsg" class="u11-note2"></div>'
                 '<button type="button" class="ref-save" data-team-free onclick="u11Agree()">Agree</button> '
                 '<button type="button" class="ref-save" data-team-free onclick="u11Print()">Print our clinic record</button></div>')
    o.append(acc('5.9 &mdash; Capstone Assessment Output', '\n'.join(b)))
    return '\n'.join(o) + '\n'

def css(fac):
    c = 'var(--gold)' if fac else 'var(--teall)'
    return ('.u11-how{border:1px solid rgba(255,255,255,.12);border-radius:3px;padding:12px 16px;margin:14px 0;background:rgba(255,255,255,.03);}\n'
            '.u11-how-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:6px;}\n.u11-how ol{padding-left:20px;}\n.u11-how li{font-size:13px;line-height:1.7;color:rgba(255,255,255,.75);margin:4px 0;}\n'
            '.u11-sub{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin:14px 0 6px;}\n'
            '.u11-roles{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:6px 12px;margin-bottom:8px;}\n'
            '.u11-chk{font-size:12.5px;color:rgba(255,255,255,.7);display:flex;gap:8px;align-items:flex-start;padding:6px 8px;border:1px solid rgba(255,255,255,.08);border-radius:3px;cursor:pointer;line-height:1.5;}\n.u11-chk.on{border-color:%s;color:#fff;}\n.u11-chk input{margin-top:3px;}\n'
            '.u11-note2{font-size:12.5px;color:rgba(255,255,255,.55);line-height:1.6;margin:6px 0;grid-column:1/-1;}\n'
            '.u11-ref .u11-sel td{background:rgba(26,122,106,.16);color:#fff;}\n.u11-kv td:first-child{width:42%%;}\n'
            '.u11-ta{min-height:58px;resize:vertical;line-height:1.6;}\n.u11-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0 12px;}\n'
            '.u11-ro{font-size:13px;color:rgba(255,255,255,.8);line-height:1.6;padding:8px 0;}\n.u11-ok{color:#5ecba1;font-weight:700;}\n.u11-rec{margin-top:10px;}\n.u11-add{margin:6px 0 10px;}\n'
            '#mod4 .u11-tbln.u11-ref{min-width:760px;}\n') % (c, c, c)

def js():
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'u11_s5.js'), encoding='utf-8').read() + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'u11_coc.js'), encoding='utf-8').read()
    data = ('var U11_ROLES=%s;\nvar U11_LOSS=%s;\nvar U11_CS=%s;\nvar U11_CN=%s;\nvar U11_NAMES=%s;\nvar U11_KEYS=%s;' % (
        json.dumps([[r[0], r[1].replace('&amp;', '&amp;')] + list(r[2:]) for r in ROLES], ensure_ascii=False), json.dumps(LOSSES, ensure_ascii=False),
        json.dumps(COSTS), json.dumps(COST_NAMES), json.dumps(NAMES, ensure_ascii=False), json.dumps(KEYS)))
    return src.replace('/*DATA*/', data)
