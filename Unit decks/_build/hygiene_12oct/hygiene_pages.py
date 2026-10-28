# -*- coding: utf-8 -*-
"""Hygiene of 12 October 2026 (Carol), the pages.
1. Back to Platform / Back to Dashboard in Units 1, 2 and 3 sits at the left of the header, as in Units 4 onwards
   (back link, thin divider, then the module and unit title; the badges move to the right).
2. Units 3 and 4 (Unit 2 keeps its order, Carol 12 October 10:38): Section 4 and Section 5 change places, so that the last section is the Application section with the Capstone work
   (swap45.py). Arc names that point to the moved group work are renamed; the Unit 4 facilitator recap follows the new order.
3. Units 4 to 7 point to "Unit 3, part 4.x": now "Unit 3, part 5.x".
Usage: python3 hygiene_pages.py <portal folder> <out folder>. Every change is an exact replacement that must match; line endings kept."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import swap45
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
LOG = []

def load(name):
    raw = open(os.path.join(src, name), 'rb').read()
    return raw.decode('utf-8').replace('\r\n', '\n'), b'\r\n' in raw
def save(name, t, crlf):
    open(os.path.join(out, name), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
def once(t, a, b, name):
    n = t.count(a); assert n == 1, (name, n, a[:80]); return t.replace(a, b)

DIV = '<div style="width:1px;height:24px;background:rgba(255,255,255,.1);"></div>'
def header(t, name):
    a = t.index('<nav class="unit-nav">'); b = t.index('</nav>', a) + 6
    nav = t[a:b]
    back = re.search(r'<(a|button)\b[^>]*class="nav-back"[^>]*>.*?</\1>', nav, re.S).group(0)
    left = re.search(r'<div class="nav-left">(.*?)\n  </div>', nav, re.S).group(1)
    logo = re.search(r'<img\b[^>]*class="nav-logo"[^>]*/?>', left)
    brand = re.search(r'<div class="nav-brand">.*?</div>', left, re.S).group(0)
    badges = (re.sub(r'<div class="nav-left">.*?\n  </div>', '', nav, flags=re.S).replace(back, ''))
    inner_badges = re.findall(r'<(?:span|div) class="nav-badge[^"]*"[^>]*>.*?</(?:span|div)>', left + badges, re.S)
    assert inner_badges, name
    new = ('<nav class="unit-nav">\n  <div class="nav-left">\n    ' + back + '\n    ' + DIV + '\n    ' +
           (logo.group(0) + '\n    ' if logo else '') + brand + '\n  </div>\n  ' + ''.join(inner_badges) + '\n</nav>')
    t = t[:a] + new + t[b:]
    m = re.search(r'\.nav-back\{([^}]*)\}', t)
    css = m.group(1)
    for k, v in (('background', 'none'), ('border', 'none'), ('cursor', 'pointer'), ('font-family', '"Montserrat",sans-serif'), ('padding', '0'), ('text-decoration', 'none')):
        if not re.search(r'(^|;)' + k + ':', css): css += k + ':' + v + ';'
    t = t[:m.start()] + '.nav-back{' + css + '}' + t[m.end():]
    LOG.append('%s: back link at the left of the header' % name)
    return t

# ── 1 · headers of Units 1, 2 and 3 ──
for name in ('unit1_P.html', 'unit1_F.html'):
    t, c = load(name); save(name, header(t, name), c)

# ── 2 · Units 2, 3 and 4: the two sections change places ──
FIX = {
    'unit2_m1_lens1_p.html': [('Reflection &mdash; Application', 'Reflection &mdash; Integration')],
    'unit2_m1_lens1_f.html': [('<p>The Application section helps the group see whether the agreed strategy', '<p>The Integration section helps the group see whether the agreed strategy')],
    'unit2_m1_lens2_f.html': [('the psychological readiness to work differently in the Integration section.', 'the psychological readiness to work differently in the Application section.'),
                              ('This is the conversation the Integration section is designed to produce.', 'This is the conversation the Application section is designed to produce.'),
                              ('The Integration section is where we use that awareness to build something', 'The Application section is where we use that awareness to build something')],
}
def recap_u4f(t, name):
    """Unit 4 facilitator recap: the place keeps its number, arc and colour; title and text move with their section."""
    rx = re.compile(r'(<div style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#c39de0;margin-bottom:8px;">4 &mdash; Integration: )(Stress-Testing the Key Results)(</div>\n  )(<p>.*?</p>)(\n</div>\n<div style="border-left:3px solid #f0a070;[^>]*>\n  <div style="[^"]*">5 &mdash; Application: )(Diagnosing the Breakdown)(</div>\n  )(<p>.*?</p>)', re.S)
    m = rx.search(t); assert m, name
    g = m.groups()
    return t[:m.start()] + g[0] + g[5] + g[2] + g[7] + g[4] + g[1] + g[6] + g[3] + t[m.end():]

# Unit 2 keeps its order (Carol, 12 October 10:38: "Unit 2 is messed up ... Please take it back"): header only.
for name in ('unit2_m1_lens1_p.html', 'unit2_m1_lens1_f.html'):
    t, c = load(name); save(name, header(t, name), c)

for name in ('unit2_m1_lens2_p.html', 'unit2_m1_lens2_f.html', 'unit2_m1_lens3_p.html', 'unit2_m1_lens3_f.html'):
    t, c = load(name)
    if name.startswith('unit2_m1_lens2'): t = header(t, name)
    log = []
    t = swap45.masked_apply(t, lambda x: swap45.swap_numbers(x))
    t = swap45.swap_summary(t, log)
    ms = swap45.mods(t)
    ia = [i for i, (s, mid) in enumerate(ms) if re.search(r'Section 5 (·|&middot;) Application', t[s:s + 600])]   # after the number swap the old Section 4 carries the Section 5 label
    assert len(ia) == 1, (name, ia)
    t = swap45.swap_page(t, ia[0], log)
    for a, b in FIX.get(name, []): t = once(t, a, b, name)
    if name == 'unit2_m1_lens3_f.html': t = recap_u4f(t, name)
    # checks: the labels read 4 then 5 in page order, and parts follow the labels
    labs = re.findall(r'Section ([45]) (?:·|&middot;) (Integration|Application) (?:—|&mdash;) (Collective|In Practice)', t)
    assert labs[-2:] == [('4', 'Integration', 'Collective'), ('5', 'Application', 'In Practice')], (name, labs)
    parts = [p[0] for p in re.findall(r'class="acc-t">(\d)\.\d', t)]
    assert parts == sorted(parts), (name, parts)
    save(name, t, c)
    LOG.append('%s: %s' % (name, '; '.join(log)))

# ── 3 · pointers to Unit 3, part 4.x in Units 5 to 7 ──
for name in ('unit3_m1_lens4_p.html', 'unit3_m1_lens5_p.html', 'unit3_m1_lens5_f.html', 'unit3_m1_lens6_p.html', 'unit3_m1_lens6_f.html'):
    t, c = load(name)
    n = len(re.findall(r'Unit 3, part 4\.(\d)', t)); assert n >= 1, name
    t = re.sub(r'Unit 3, part 4\.(\d)', r'Unit 3, part 5.\1', t)
    save(name, t, c); LOG.append('%s: %d pointer(s) to Unit 3, part 4.x now 5.x' % (name, n))

print('\n'.join(LOG))
