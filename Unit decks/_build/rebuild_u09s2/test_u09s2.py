# -*- coding: utf-8 -*-
"""Static checks of the Section 2 rework (no browser on this computer's shell). Usage: python3 test_u09s2.py <out folder> <live p> <live f>"""
import sys, os, re, subprocess, json
from bs4 import BeautifulSoup
D, LP, LF = sys.argv[1:4]
ok = 0; bad = []
def check(c, m):
    global ok
    if c: ok += 1
    else: bad.append(m); print('FAIL', m)
for v, fn, live in (('p', 'unit3_m2_lens8_p.html', LP), ('f', 'unit3_m2_lens8_f.html', LF)):
    s = open(os.path.join(D, fn), encoding='utf-8').read()
    soup = BeautifulSoup(s, 'lxml')
    # balanced divs/details per section (html.parser count)
    for tag in ('div', 'details'):
        check(len(re.findall(r'<%s\b' % tag, s)) - len(re.findall(r'</%s>' % tag, s)) == len(re.findall(r'<%s\b' % tag, open(live, encoding='utf-8').read())) - len(re.findall(r'</%s>' % tag, open(live, encoding='utf-8').read())), '%s %s balance changed' % (v, tag))
    titles = [x.get_text() for x in soup.select('.acc-t')]
    want = ['1.1 — What is a Strategic Clog?', '1.2 — Understanding Where Performance Becomes Constrained', '1.3 — The Seven Performance Clogs',
            '1.4 — The Three Performance Lines of Sight from the Seven Clogs', '1.5 — Worked Diagnostic Example: Improving Customer Service',
            '2.1 — Three Disciplines of Execution Engineering', '2.2 — The 7 Strategic Unclogging Levers', '4.1 — Normalising the Unclog: From Crisis to Habit',
            '4.2 — The Unclogging Cycle: Review–Realign–Restore', '4.3 — Worked Example: The Unclogging Cycle', '5.4 — Simulate the Unclogging Cycle']
    for w in want: check(w in titles, '%s missing title %s' % (v, w))
    seq = [t for t in titles if re.match(r'\d\.\d', t)]
    check(seq == sorted(seq, key=lambda t: (int(t[0]), int(t[2]))), '%s part order %s' % (v, seq))
    txt = soup.get_text(' ')
    for badw in ('1.2.1', '1.2.2', '1.2.3', 'Clogs Are Design Signals', 'The 7-Clog Diagnostic Map</', '2.3 —', '4.4 —', '4.5 —', 'before CESI', 'pre-CESI',
                 'rather than', 'instead of', 'COMPASS', 'Why Clogs Are Predictable', 'Apply Review–Realign–Restore', 'part 1.2.2', 'lens'):
        check(not re.search(r'\b%s\b' % re.escape(badw), txt) if badw == 'lens' else badw not in txt, '%s still has %s' % (v, badw))
    sec = lambda a, b: txt[txt.find(a):txt.find(b, txt.find(a))]
    s1 = sec('1.2 — Understanding', '1.3 — The Seven')
    check('Clogs form where the strategy stretches' in s1, v + ' 1.2 opening')
    check(s1.find('Clogs form where') < s1.find('Strategy depends on the organisation'), v + ' 1.2 opening before Carol text')
    check(('Where Is Your System Not Yet Ready?' in s1) if v == 'p' else ('most likely to create friction' in s1), v + ' ref3 moved into 1.2')
    check('ABCV Diagnostic Connection' not in txt, v + ' ABCV connection gone')
    check(soup.select('.clog-card') != [] or 'Clog 07' in txt, v + ' clogs kept')
    s2 = sec('Section 2 · Intelligence', 'Section 3 · Extrapolating') if 'Section 3 · Extrapolating' in txt else ''
    check('Why Disciplined Intervention Clears Strategic Clogs' in txt, v + ' S2 title')
    check('A named clog still holds until leaders act on it' in txt, v + ' S2 opening')
    panels = soup.select('.step-panel')
    dpan = [p for p in panels if p.find('h5') and p.find('h5').get_text() in ('Detect Signals Before They Compound', 'Name the Clog Precisely Before Intervening', 'Pull the Right Lever with Precision')]
    check(len(dpan) == 3, v + ' three discipline panels')
    for p in dpan: check(len(p.select('.u8v-hu')) == 1 and len(p.select('.u8v-or')) == 1, v + ' discipline cards ' + p.find('h5').get_text())
    lev = soup.select('.lever-card')
    check(len(lev) == 7, v + ' seven levers %d' % len(lev))
    for c in lev: check(len(c.select('.u8v-hu')) == 1 and len(c.select('.u8v-or')) == 1 and c.select('.u9-lv-how'), v + ' lever cards ' + c.select_one('.lever-name').get_text())
    acc42 = [a for a in soup.select('.acc') if a.select_one('.acc-t') and a.select_one('.acc-t').get_text().startswith('4.2')][0]
    subs = [x.get_text() for x in acc42.select('summary')]
    check(subs == ['REVIEW — Establish the Performance Reality', 'REALIGN — Establish Collective Executive Ownership', 'RESTORE — Activate the Seven Unclogging Levers', 'The Unclogging Record'], v + ' 4.2 subtitles %s' % subs)
    dets = acc42.select('details')
    for d in dets[:3]: check(len(d.select('.u8v-hu')) == 1 and len(d.select('.u8v-or')) == 1 and 'Into the Unclogging Record' in d.get_text(), v + ' 4.2 stage cards ' + d.summary.get_text())
    check('The Unclogging Cycle' in acc42.get_text() and acc42.select('table'), v + ' 4.2 record table')
    check('Lever 06 — Realign is the distinct intervention' in acc42.get_text(), v + ' RESTORE text kept')
    check('Problem Charter' in sec('5.1 —', '5.2 —'), v + ' 5.1 Problem Charter')
    check('simulates how its executive team takes the selected challenge' in sec('5.4 —', '5.5 —'), v + ' 5.4 guidance line')
    if v == 'p':
        for i in ('u9_ch_challenge', 'u9_ch_link', 'u9_cl_clog', 'u9_lv_lever'):
            e = soup.find(id=i); check(e is not None and e.name == 'select', 'p %s is a drop-down' % i)
        opts = [o.get_text() for o in soup.find(id='u9_cl_clog').find_all('option')][1:]
        check(opts[0] == '01 · Structural Misfit' and opts[6] == '07 · Leadership Avoidance', 'p clog options numbered %s' % opts)
        check(soup.find(id='u9_cl_clog').find_all('option')[1].get('value') == 'Structural Misfit', 'p clog value kept')
        check(soup.find(id='u9Krs') is None, 'p old KR block removed')
        check(soup.find(id='ref3') is not None and soup.find(id='ref4') is not None, 'p ref3 ref4 present')
        check(len(soup.select('textarea#ref3')) == 1, 'p one ref3')
        # every KEYS id exists
        keys = json.loads(re.search(r'var KEYS=(\[[^\]]*\])', s).group(1).replace("'", '"'))
        for k in keys: check(soup.find(id=k) is not None, 'p key box ' + k)
    else:
        check('1.5 · Work through the worked example' in txt, 'f awareness guidance lines')
        check('Use the pressure point examples' not in txt, 'f old guidance gone')
        check('(part 1.4)' in txt, 'f section 3 reference')
        check('Unclogging Cycle' in sec('Unit Summary', 'When unclogging'), 'f summary')
    # JS syntax
    for n, m in enumerate(re.finditer(r'<script>([\s\S]*?)</script>', s)):
        tmp = os.path.join(D, '_chk_%s_%d.js' % (v, n)); open(tmp, 'w', encoding='utf-8').write(m.group(1))
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True); os.replace(tmp, os.path.join(D, '_last.js'))
        check(r.returncode == 0, '%s script %d syntax %s' % (v, n, r.stderr[:300]))
print('%d passed, %d failed' % (ok, len(bad)))
