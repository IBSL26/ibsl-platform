# -*- coding: utf-8 -*-
"""PREVIEW copies of the Unit 11 pages (never committed).
Usage: python3 -B make_previews_u11.py <participant> <facilitator> <mock> <out folder> [s2r-team.js]"""
import sys, os, re
p_src, f_src, mock, out = sys.argv[1:5]
team = sys.argv[5] if len(sys.argv) > 5 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 's2r-team.js')
rd = lambda x: open(x, 'rb').read().decode('utf-8')
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · not the live portal</div>')
os.makedirs(out, exist_ok=True)
p = rd(p_src)
mx = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script src="/s2r-save\.js"></script>\r?\n<script src="/s2r-team\.js"></script>', p); assert mx
p = p[:mx.start()] + '<script>\n' + rd(mock) + '</script>\n<script>\n' + rd(team) + '</script>' + p[mx.end():]
p, n = re.subn(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 11 — Participant</title>', p, count=1); assert n == 1
i = p.rindex('</body>'); p = p[:i] + (BAR % 'Unit 11 participant page · entries stay in this browser · Section 5 shows a sample group of four') + '\n' + p[i:]
open(os.path.join(out, 'PREVIEW - Unit 11 Participant.html'), 'wb').write(p.encode('utf-8'))
f = rd(f_src)
mm = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script>\r?\n\(function\(\)\{[\s\S]*?\}\)\(\);\r?\n</script>\r?\n', f)
assert mm and 'can_facilitate_lens' in mm.group(0)
f = f[:mm.start()] + f[mm.end():]
f = re.sub(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 11 — Facilitator</title>', f, count=1)
i = f.rindex('</body>'); f = f[:i] + (BAR % 'Unit 11 facilitator page') + '\n' + f[i:]
open(os.path.join(out, 'PREVIEW - Unit 11 Facilitator.html'), 'wb').write(f.encode('utf-8'))
print('previews written to', out)
