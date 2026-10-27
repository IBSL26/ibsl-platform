# -*- coding: utf-8 -*-
"""PREVIEW copies of the Unit 10 pages (never committed). Participant: offline save helper + sample group of four + the real s2r-team.js inline.
Usage: python3 -B make_previews_u10.py <participant> <facilitator> <s2r-team.js> <mock> <out folder>"""
import sys, os, re
p_src, f_src, team, mock, out = sys.argv[1:6]
rd = lambda x: open(x, 'rb').read().decode('utf-8')
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · not the live portal%s</div>')
CLEAR = (' &nbsp; <button type="button" onclick="if(confirm(\'Clear everything you typed in this preview and start again?\'))__clearPreview()" '
         'style="font:700 11px Arial,sans-serif;padding:3px 10px;border:1px solid #111811;background:transparent;border-radius:3px;cursor:pointer;">Start again</button>')
os.makedirs(out, exist_ok=True)
p = rd(p_src)
mx = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script src="/s2r-save\.js"></script>\r?\n<script src="/s2r-team\.js"></script>', p); assert mx
p = p[:mx.start()] + '<script>\n' + rd(mock) + '</script>\n<script>\n' + rd(team) + '</script>' + p[mx.end():]
p, n = re.subn(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 10 — Participant</title>', p, count=1); assert n == 1
i = p.rindex('</body>'); p = p[:i] + (BAR % ('Unit 10 participant page · entries stay in this browser · Section 5 shows a sample group of four', CLEAR)) + '\n' + p[i:]
open(os.path.join(out, 'PREVIEW - Unit 10 Participant.html'), 'wb').write(p.encode('utf-8'))
f = rd(f_src)
mm = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script>\r?\n\(function\(\)\{[\s\S]*?\}\)\(\);\r?\n</script>\r?\n', f)
assert mm and 'can_facilitate_lens' in mm.group(0)
f = f[:mm.start()] + f[mm.end():]
f = re.sub(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 10 — Facilitator</title>', f, count=1)
i = f.rindex('</body>'); f = f[:i] + (BAR % ('Unit 10 facilitator page', '')) + '\n' + f[i:]
open(os.path.join(out, 'PREVIEW - Unit 10 Facilitator.html'), 'wb').write(f.encode('utf-8'))
print('previews written to', out)
