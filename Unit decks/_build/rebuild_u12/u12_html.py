# -*- coding: utf-8 -*-
"""Unit 12 · HTML for the header, Facilitator Guide and Sections 1-5 (facilitator and participant)."""
import os
from u12_content import *

def acc(title, body, open_=False, meta=''):
    m = '<div class="acc-meta">%s</div>' % meta if meta else ''
    return ('<div class="acc%s">\n<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div>%s</div>%s</div>\n'
            '<div class="acc-b"><div class="cb">\n%s\n</div></div></div>' % (' open' if open_ else '', title, m, ARR, body))

def det(title, body, open_=False):
    return '<details class="u12-det"%s><summary>%s</summary><div class="u12-det-b">\n%s\n</div></details>' % (' open' if open_ else '', title, body)

def tbl(head, rows, cls='', first_bold=True):
    h = ''.join('<th>%s</th>' % x for x in head) if head else ''
    body = '\n'.join('<tr>%s</tr>' % ''.join(('<td><strong>%s</strong></td>' if (k == 0 and first_bold) else '<td>%s</td>') % c for k, c in enumerate(r)) for r in rows)
    return ('<div class="u12-scroll"><table class="u12-tbl %s">%s<tbody>\n%s\n</tbody></table></div>'
            % (cls, '<thead><tr>%s</tr></thead>' % h if h else '', body))

def slo(lo):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in lo)

def guidance(name, paras):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; %s</div>\n%s\n</div>' % (name, '\n'.join('<p>%s</p>' % p for p in paras))

def reflect_f(label, q):
    return '<div class="u12-refl"><div class="u12-refl-h">&#x270E; %s</div><p>%s</p></div>' % (label, q)

def reflect_p(key, q):
    return ('<div class="ref-block"><div class="ref-label">&#x270E; Reflection</div><p class="u12-q">%s</p>'
            '<textarea class="ref-ta reflection-textarea" id="%s" placeholder="Write your reflection"></textarea>'
            '<div class="ref-saved reflection-saved" id="%s-saved"></div><button class="ref-save" onclick="saveTA(this)">Save Reflection</button></div>') % (q, key, key)

def header(i='    '):
    out = [i + '<div class="unit-sub">Grounding · Pillar 3 of DIG</div>']
    out += [i + '<p class="unit-desc">%s</p>' % p for p in GROUNDING]
    out += [i + '<div class="klo-bar">', i + '  <span class="klo-label">Module learning outcomes</span>']
    out += [i + '  <span class="klo">%s</span>' % x for x in MODULE_LO]
    out += [i + '</div>', i + '<div class="klo-bar">', i + '  <span class="klo-label">Key learning outcomes</span>']
    out += [i + '  <span class="klo">%s</span>' % x for x in UNIT_LO]
    out += [i + '</div>']
    return '\n'.join(out)

def guide():
    rows = '\n'.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in JOURNEY)
    return ('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>\n%s\n'
            '<p>Each section carries both concepts one step further:</p>\n'
            '<div class="u12-scroll"><table class="u12-tbl"><thead><tr><th>Section</th><th>Three Lines of Sight</th><th>KISS</th></tr></thead><tbody>\n%s\n</tbody></table></div>\n</div>\n'
            '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Key Facilitation Questions</div>\n<ul class="u12-ul">%s</ul>\n</div>\n'
            '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Tone &amp; Watch Points</div>\n<ul class="u12-ul">%s</ul>\n</div>\n') % (
        '\n'.join('<p>%s</p>' % p for p in INTENT), rows,
        ''.join('<li>%s</li>' % q for q in KFQ),
        ''.join('<li><strong>%s</strong> %s</li>' % t for t in TONE))

# ── Section 1
def section1(fac):
    o = [slo(S1_LO)]
    if fac: o.append(guidance('Awareness', S1_GUIDE))
    o.append(acc('1.1 &mdash; Performance Gravity', '\n'.join('<p>%s</p>' % p for p in P11), True))
    b = ['<p>%s</p>' % P12A, tbl(['Line of sight', 'The question each quarter', 'The result it reads'], LINES),
         '<h4 class="u12-h">Filtering each line through WARD</h4>', '<p>%s</p>' % P12B,
         tbl(['WARD', 'Strategic', 'Operational', 'Behavioural'], WARD_GRID, 'u12-wide'), '<p>%s</p>' % P12C]
    b.append(reflect_f('Participant reflection', R12_Q) if fac else reflect_p('ref11', R12_Q))
    o.append(acc('1.2 &mdash; The Three Lines of Sight', '\n'.join(b), meta='Strategic · Operational · Behavioural'))
    cards = ''.join('<div class="u12-card"><div class="u12-card-l">%s</div><div class="u12-card-n">%s</div><p>%s</p></div>' % k for k in KISS)
    o.append(acc('1.3 &mdash; KISS: The Four Sustaining Decisions', '<p>%s</p>\n<div class="u12-cards">%s</div>' % (P13, cards), meta='Keep · Improve · Stop · Start'))
    return '\n'.join(o) + '\n'

# ── Section 2
def section2(fac):
    o = [slo(S2_LO)]
    if fac: o.append(guidance('Intelligence', S2_GUIDE))
    b = ['<p>%s</p>' % P21]
    for k, (line, mech, txt, shows) in enumerate(MECH):
        b.append(det('%s &middot; %s' % (line, mech), '<p>%s</p><p><strong>How it shows:</strong> %s</p>' % (txt, shows), k == 0))
    b.append('<div class="hbox"><p>%s</p></div>' % P21_END)
    o.append(acc('2.1 &mdash; Why Performance Drifts', '\n'.join(b), True, meta='Select each line to open it'))
    b = ['<p>%s</p>' % P22, tbl(['Line of sight', 'Drift on this line', 'KISS decisions that counter it'], COUNTER), '<p>%s</p>' % P22_END]
    b.append(reflect_f('Participant reflection', R22_Q) if fac else reflect_p('ref12', R22_Q))
    o.append(acc('2.2 &mdash; Why KISS Holds Performance', '\n'.join(b)))
    return '\n'.join(o) + '\n'

# ── Section 3
def section3(fac):
    o = [slo(S3_LO)]
    if fac: o.append(guidance('Extrapolating', S3_GUIDE))
    b = ['<p>%s</p>' % P31]
    for k, (role, dom, line, where, ks) in enumerate(ROLES):
        b.append(det('%s &middot; %s' % (role, dom),
                     '<table class="u12-tbl u12-kv"><tbody><tr><td>Line it reads first</td><td>%s</td></tr><tr><td>Where drift shows first</td><td>%s</td></tr><tr><td>KISS decision it usually leads</td><td>%s</td></tr></tbody></table>' % (line, where, ks), k == 0))
    if fac:
        b.append(reflect_f('Participant reflection (Learning Portfolio)', 'Fields for the participant: <strong>%s</strong>.' % ' · '.join(R31_F)))
    else:
        f = ''.join('<label class="fld-label">%s</label><textarea class="ref-ta" style="min-height:46px;" data-fkey="ref13" data-fidx="%d" oninput="syncFieldDebounced(\'ref13\')"></textarea>' % (x, i) for i, x in enumerate(R31_F))
        b.append('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; Your role</div>%s'
                 '<textarea id="ref13" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="ref13-saved"></div>'
                 '<button class="ref-save" onclick="fldSaveBtn(this,\'ref13\')">Save</button></div>' % f)
    o.append(acc('3.1 &mdash; Where Drift Shows First', '\n'.join(b), True, meta='Select each role to open it'))
    return '\n'.join(o) + '\n'

# ── Section 4
def worked_example():
    b = ['<p>%s</p>' % P42, tbl(None, EX_HEAD, 'u12-kv'),
         tbl(EX_COLS, EX_ROWS, 'u12-wide'), '<p class="u12-src">%s</p>' % EX_SOURCES,
         '<h4 class="u12-h">KISS for Quarter 3</h4>', tbl(['Decision', 'Practice', 'Line of sight', 'Owner'], EX_KISS, 'u12-wide')]
    return '\n'.join(b)

def section4(fac):
    o = [slo(S4_LO)]
    if fac: o.append(guidance('Integration', S4_GUIDE))
    o.append(acc('4.1 &mdash; The Quarterly Three Lines of Sight Page',
                 '<p>%s</p>\n%s\n<p>%s</p>' % (P41, tbl(['Part of the page', 'What the leadership team enters'], PAGE_PARTS), P41_END), True))
    o.append(acc('4.2 &mdash; Worked Example: Quarter 2, Customer Service', worked_example(), meta='Every figure from earlier worked examples'))
    return '\n'.join(o) + '\n'

# ── Section 5
def fld(path, label, kind='ta', opts=None, ph=''):
    return '<div class="u12-f">%s</div>' % _fld(path, label, kind, opts, ph)

def _fld(path, label, kind='ta', opts=None, ph=''):
    if kind == 'ta':
        return '<label class="fld-label">%s</label><textarea class="fld-input u12-ta" data-u12="%s" placeholder="%s"></textarea>' % (label, path, ph)
    if kind == 'in':
        return '<label class="fld-label">%s</label><input class="fld-input" type="text" data-u12="%s" placeholder="%s">' % (label, path, ph)
    if kind == 'num':
        return '<label class="fld-label">%s</label><input class="fld-input" type="number" step="0.01" data-u12="%s" placeholder="%s">' % (label, path, ph)
    return '<label class="fld-label">%s</label><select class="fld-input" data-u12="%s"><option value="">Choose…</option>%s</select>' % (label, path, ''.join('<option>%s</option>' % x for x in opts))

def section5(fac):
    o = [slo(S5_LO)]
    if fac: o.append(guidance('Application', S5_GUIDE))
    b = ['<p>%s</p>' % (P51_F if fac else P51_P),
         '<h4 class="u12-h">Brought into the page from earlier units</h4><ul class="u12-ul">%s</ul>' % ''.join('<li>%s</li>' % x for x in BROUGHT),
         ]
    if fac:
        b.append('<h4 class="u12-h">Exercise fields</h4><ol class="u12-ul">%s</ol>' % ''.join('<li>%s</li>' % x for x in FIELDS))
    if not fac:
        b.append('<div class="u12-how"><div class="u12-how-h">Capstone work &middot; How Section 5 works</div><ol>%s</ol></div>' % ''.join('<li>%s</li>' % x for x in HOW))
        b.append(det('Worked example reference &middot; Quarter 2, Customer Service (part 4.2)', worked_example()))
    o.append(acc('5.1 &mdash; Application Overview', '\n'.join(b), True))
    if fac:
        o.append(acc('5.2 &mdash; Your Results for the Quarter',
                     '<p>The portal brings each group’s confirmed results onto its page: the enterprise Key Result and its WARD (Unit 6), the ESRG scan (Unit 10) and the consolidated health position (Unit 11). The scribe chooses the quarter and can correct any value that has changed.</p>\n'
                     + tbl(None, [('Enterprise Key Result', ''), ('Quarter', ''), ('Decider', '')], 'u12-kv'), True))
        tmpl = [(w, '', '', '') for w in ['Result this quarter', 'W · Waypoint', 'A · Alert', 'Alert raised', 'R · Recovery and owner', 'D · Decider checks']]
        o.append(acc('5.3 &mdash; The Three Lines of Sight',
                     '<p>Each group completes each line from its results in part 5.2, filtered through WARD.</p>\n'
                     + tbl(['WARD', 'Strategic · Key Result', 'Operational · ESRG scan', 'Behavioural · Health Thermometer'], tmpl, 'u12-wide')))
        o.append(acc('5.4 &mdash; KISS for Next Quarter',
                     '<p>Each group records the decisions its leadership team makes at the close of the quarter, with at least one Keep, one Improve, one Stop and one Start.</p>\n'
                     + tbl(['Decision', 'Practice', 'Line of sight', 'Owner'], [('Keep', '', '', ''), ('Improve', '', '', ''), ('Stop', '', '', ''), ('Start', '', '', '')], 'u12-wide')))
        o.append(acc('5.5 &mdash; Capstone Output', '<p>When every member has agreed, the group’s page goes into its team’s Capstone S2R® Blueprint:</p>\n' + tbl(['Item', 'Title', 'Content'], CAP)))
        return '\n'.join(o) + '\n'
    o.append('<div id="u12TwBar"></div>')
    # 5.2 brought in
    b = ['<p>The scribe selects “Bring in” to bring your group’s confirmed results onto the page. Each value can be corrected by the scribe if your group’s records have changed.</p>',
         '<div class="u12-btnrow"><button type="button" class="ref-save" onclick="u12Bring(true)">Bring in from my earlier units</button></div>',
         '<div class="u12-note" id="u12BringMsg"></div>',
         '<div class="u12-grid">' + fld('quarter', 'Quarter', 'sel', ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']) + '</div>',
         '<div class="u12-sub">Unit 6 &middot; Enterprise Key Result and WARD</div>',
         fld('src.kr', 'Enterprise Key Result', 'ta'),
         '<div class="u12-grid">' + fld('src.wp', 'W · Waypoints', 'ta') + fld('src.alert', 'A · Alert', 'ta') + '</div>',
         '<div class="u12-grid">' + fld('src.rec_i', 'R · Recovery · individuals', 'ta') + fld('src.rec_o', 'R · Recovery · organisational conditions', 'ta') + '</div>',
         '<div class="u12-grid">' + fld('src.dec', 'D · Decider', 'in') + '</div>',
         '<div class="u12-sub">Unit 10 &middot; ESRG scan (enterprise average, 1 to 5)</div>',
         '<div class="u12-grid4">' + fld('src.es.0', 'Operational Readiness · FIT', 'num') + fld('src.es.1', 'Operational Flow · SIP', 'num')
         + fld('src.es.2', 'Delivery Capacity · AIR', 'num') + fld('src.es.3', 'Decision Responsiveness · PAR', 'num') + '</div>',
         '<div class="u12-sub">Unit 11 &middot; Consolidated health position</div>',
         '<div class="u12-grid">' + fld('src.h_score', 'Consolidated health score (out of 100)', 'num') + fld('src.h_weak', 'Two weakest traits', 'in') + '</div>']
    o.append(acc('5.2 &mdash; Your Results for the Quarter', '\n'.join(b), True, meta='Brought in from Units 6, 10 and 11'))
    # 5.3 three lines
    s = ('<div class="u12-line"><div class="u12-line-h">Strategic line &middot; Key Result</div>'
         + '<div class="u12-grid">' + fld('s.result', 'Result this quarter', 'in') + fld('s.wp', 'W · Waypoint for this quarter', 'in') + '</div>'
         + '<p class="u12-ro" id="u12SAlert"></p>'
         + '<div class="u12-grid">' + fld('s.raised', 'Alert raised', 'sel', ['Yes', 'No']) + fld('s.check', 'When the Decider checks it', 'in') + '</div>'
         + fld('s.rec', 'R · Recovery (for individuals and for the organisational conditions)', 'ta') + '</div>')
    op = ('<div class="u12-line"><div class="u12-line-h">Operational line &middot; ESRG scan</div>'
          + '<p class="u12-ro" id="u12OLow"></p>'
          + '<div class="u12-grid">' + fld('o.raised', 'Alert raised', 'sel', ['Yes', 'No']) + fld('o.owner', 'Owner of the recovery', 'in') + '</div>'
          + fld('o.rec', 'R · Recovery (the owner of the condition restores it)', 'ta')
          + '<div class="u12-grid">' + fld('o.check', 'When it is checked', 'in') + '</div></div>')
    be = ('<div class="u12-line"><div class="u12-line-h">Behavioural line &middot; Health Thermometer</div>'
          + '<p class="u12-ro" id="u12BLow"></p>'
          + '<div class="u12-grid">' + fld('b.raised', 'Alert raised', 'sel', ['Yes', 'No']) + fld('b.owner', 'Owner of the recovery', 'in') + '</div>'
          + fld('b.rec', 'R · Recovery (the accountable executive restores the weakest traits)', 'ta')
          + '<div class="u12-grid">' + fld('b.check', 'When it is checked', 'in') + '</div></div>')
    o.append(acc('5.3 &mdash; The Three Lines of Sight', '<p>Complete each line from the results in part 5.2, filtered through WARD.</p>\n' + s + '\n' + op + '\n' + be))
    # 5.4 KISS
    o.append(acc('5.4 &mdash; KISS for Next Quarter',
                 '<p>Record the decisions your leadership team makes at the close of the quarter. Each decision names the practice, the line of sight it comes from and its owner. Your group needs at least one Keep, one Improve, one Stop and one Start.</p>\n'
                 '<div id="u12Kiss"></div><button type="button" class="ref-save u12-add" onclick="u12AddKiss()">+ Add a decision</button>'))
    # 5.5 output
    o.append(acc('5.5 &mdash; Capstone Output',
                 '<p>When every member has agreed, your group’s page goes into your team’s Capstone S2R® Blueprint:</p>\n' + tbl(['Item', 'Title', 'Content'], CAP) + '\n'
                 '<div class="u12-rec"><div id="u12RecMsg" class="u12-note"></div>'
                 '<button type="button" class="ref-save" data-team-free onclick="u12Agree()">Agree</button> '
                 '<button type="button" class="ref-save" data-team-free onclick="u12Print()">Print our quarterly page</button></div>'))
    return '\n'.join(o) + '\n'

def summary_f():
    return ('<div class="acc"><div class="acc-h" onclick="tA(this)"><div><div class="acc-t">Unit Summary</div><div class="acc-meta">Unit 12 synthesis &middot; S2R&reg; Programme Close</div></div>%s</div>\n'
            '<div class="acc-b"><div class="cb">\n<ul class="u12-ul">%s</ul>\n</div></div></div>\n') % (ARR, ''.join('<li>%s</li>' % x for x in SUMMARY_F))

def summary_js():
    import json
    return 'var SUMMARY=[\n' + ',\n'.join('{arc:%s,title:%s,body:%s}' % (json.dumps(a, ensure_ascii=False), json.dumps(t, ensure_ascii=False), json.dumps(b, ensure_ascii=False)) for a, t, b in SUMMARY_P) + '\n];'

def css(fac):
    th_bg, col, bd = ('#1a2a1e', 'var(--gold)', 'rgba(201,168,76,.2)') if fac else ('#162e28', 'var(--teall)', 'rgba(26,122,106,.2)')
    return ('/* Unit 12 · Sustaining Performance (27 Oct 2026) */\n'
            '.u12-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:14px 0;}\n'
            '.u12-tbl{width:100%%;border-collapse:collapse;font-size:13px;}\n'
            '.u12-tbl th{background:%s;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;padding:10px 14px;text-align:left;border-bottom:1px solid %s;}\n'
            '.u12-tbl td{padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05);color:rgba(255,255,255,.68);line-height:1.65;vertical-align:top;}\n'
            '.u12-tbl td strong{color:rgba(255,255,255,.9);}\n'
            '.u12-kv td:first-child{width:34%%;color:rgba(255,255,255,.85);font-weight:600;}\n'
            '.u12-wide{min-width:640px;}\n'
            '.u12-h{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin:20px 0 8px;}\n'
            '.u12-sub{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin:16px 0 4px;}\n'
            '.u12-ul{padding-left:20px;margin:8px 0;}\n.u12-ul li{font-size:13.5px;line-height:1.75;color:rgba(255,255,255,.75);margin:5px 0;}\n'
            '.u12-q{font-size:13.5px;line-height:1.7;color:rgba(255,255,255,.8);margin:4px 0 8px;}\n'
            '.u12-src{font-size:12px;color:rgba(255,255,255,.55);line-height:1.6;}\n'
            '.u12-refl{border:1px solid %s;border-radius:3px;padding:12px 16px;margin:14px 0;background:rgba(255,255,255,.02);}\n'
            '.u12-refl-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:6px;}\n'
            '.u12-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:14px 0;}\n'
            '.u12-card{border:1px solid rgba(255,255,255,.1);border-top:2px solid %s;border-radius:3px;padding:14px;background:rgba(255,255,255,.02);}\n'
            '.u12-card-l{font-family:\'Cormorant Garamond\',serif;font-size:1.6rem;color:%s;line-height:1;}\n'
            '.u12-card-n{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.85);margin:6px 0 8px;}\n'
            '.u12-card p{font-size:12.5px;line-height:1.65;color:rgba(255,255,255,.68);margin:0;}\n'
            '.u12-det{border:1px solid rgba(255,255,255,.1);border-radius:3px;margin:10px 0;background:rgba(255,255,255,.02);}\n'
            '.u12-det>summary{cursor:pointer;list-style:none;padding:11px 14px;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.82);display:flex;justify-content:space-between;align-items:center;gap:10px;}\n'
            '.u12-det>summary::-webkit-details-marker{display:none;}\n'
            '.u12-det>summary::after{content:"\\25BE";font-size:13px;opacity:.6;transition:transform .2s;}\n'
            '.u12-det[open]>summary::after{transform:rotate(180deg);}\n'
            '.u12-det-b{padding:2px 14px 12px;}\n'
            '.u12-how{border:1px solid rgba(255,255,255,.12);border-radius:3px;padding:12px 16px;margin:14px 0;background:rgba(255,255,255,.03);}\n'
            '.u12-how-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:6px;}\n.u12-how ol{padding-left:20px;}\n.u12-how li{font-size:13px;line-height:1.7;color:rgba(255,255,255,.75);margin:4px 0;}\n'
            '.u12-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0 12px;}\n'
            '.u12-grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:0 12px;}\n'
            '.u12-f{min-width:0;}\n.u12-f .fld-input{width:100%%;box-sizing:border-box;}\n.u12-ta{min-height:58px;resize:vertical;line-height:1.6;}\n'
            '.u12-line{border:1px solid rgba(255,255,255,.1);border-left:2px solid %s;border-radius:3px;padding:12px 16px;margin:14px 0;background:rgba(255,255,255,.02);}\n'
            '.u12-line-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:4px;}\n'
            '.u12-ro{font-size:13px;color:rgba(255,255,255,.8);line-height:1.6;margin:8px 0;}\n'
            '.u12-note{font-size:12.5px;color:rgba(255,255,255,.6);line-height:1.6;margin:8px 0;}\n.u12-note.ok{color:#5ecba1;}.u12-note.warn{color:#f0c060;}\n'
            '.u12-ok{color:#5ecba1;font-weight:700;}\n.u12-warn{color:#f0c060;font-weight:700;}\n'
            '.u12-btnrow{margin:10px 0;}\n.u12-rec{margin-top:12px;}\n.u12-add{margin:6px 0 10px;}\n'
            '.u12-krow{border:1px solid rgba(255,255,255,.1);border-radius:3px;padding:10px 14px;margin:10px 0;}\n'
            '.u12-krow-h{display:flex;justify-content:space-between;align-items:center;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;}\n'
            '.u12-del{background:none;border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.6);font-size:10px;padding:4px 10px;border-radius:2px;cursor:pointer;letter-spacing:1px;}\n'
            '@media (max-width:600px){.u12-tbl th,.u12-tbl td{padding:8px;}}\n') % (th_bg, col, bd, col, col, bd, col, col, col, col, col, col, col)

def js():
    return open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'u12_s5.js'), encoding='utf-8').read()
