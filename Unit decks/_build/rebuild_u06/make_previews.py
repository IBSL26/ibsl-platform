# -*- coding: utf-8 -*-
"""Stand-alone PREVIEW copies of the two Unit 6 files, for opening by double-click.
Usage: python3 make_previews.py <participant file> <facilitator file> <mock-s2r.js> <output folder>
The previews are never committed or uploaded: the participant copy saves in the browser only, and both skip the sign-in checks."""
import sys, os, re
p_src, f_src, mock, out = sys.argv[1:5]
def read(x): return open(x, 'rb').read().decode('utf-8')
def once(t, s):
    assert t.count(s) == 1, 'expected once: ' + s[:70]; return t
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · not the live portal%s</div>')
CLEAR = (' &nbsp; <button type="button" onclick="if(confirm(\'Clear everything you typed in this preview and start again?\'))__clearPreview()" '
         'style="font:700 11px Arial,sans-serif;padding:3px 10px;border:1px solid #111811;background:transparent;border-radius:3px;cursor:pointer;">Start again</button>')
os.makedirs(out, exist_ok=True)
if p_src != '-':
    p = read(p_src)
    ext = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\r\n<script src="/s2r-save.js"></script>'
    once(p, ext)
    p = p.replace(ext, '<script>\r\n' + read(mock).replace('\r\n', '\n').replace('\n', '\r\n') + '</script>')
    p, n = re.subn(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 6 — Participant</title>', p, count=1); assert n == 1
    i = p.rindex('</body>'); p = p[:i] + (BAR % ('Unit 6 participant page · your entries stay in this browser only · the Unit 3 Key Results shown in Section 5 are samples', CLEAR)) + '\r\n' + p[i:]
    open(os.path.join(out, 'PREVIEW - Unit 6 Participant.html'), 'wb').write(p.encode('utf-8'))
if f_src != '-':
    f = read(f_src)
    m = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r\n<script>\r\n\(function\(\)\{[\s\S]*?\}\)\(\);\r\n</script>\r\n', f)
    assert m and 'can_facilitate_lens' in m.group(0)
    f = f[:m.start()] + f[m.end():]
    f = re.sub(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 6 — Facilitator</title>', f, count=1)
    i = f.rindex('</body>'); f = f[:i] + (BAR % ('Unit 6 facilitator page', '')) + '\r\n' + f[i:]
    open(os.path.join(out, 'PREVIEW - Unit 6 Facilitator.html'), 'wb').write(f.encode('utf-8'))
print('previews written to', out)
