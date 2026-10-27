# -*- coding: utf-8 -*-
"""PREVIEW copies of the Unit 6, 8 and 9 pages after the ESRG alignment (never committed).
Usage: python3 -B make_previews_esrg.py <folder with the built pages> <s2r-team.js> <mock> <out folder>"""
import sys, os, re
src, team, mock, out = sys.argv[1:5]
rd = lambda x: open(x, 'rb').read().decode('utf-8')
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · ESRG alignment 27 Oct · not the live portal</div>')
os.makedirs(out, exist_ok=True)
for f, name in [('unit3_m1_lens5', 'Unit 6'), ('unit3_m1_lens6', 'Unit 7'), ('unit3_m2_lens7', 'Unit 8'), ('unit3_m2_lens8', 'Unit 9')]:
    p = rd(os.path.join(src, f + '_p.html'))
    mx = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script src="/s2r-save\.js"></script>\r?\n<script src="/s2r-team\.js"></script>', p); assert mx, f
    p = p[:mx.start()] + '<script>\n' + rd(mock) + '</script>\n<script>\n' + rd(team) + '</script>' + p[mx.end():]
    i = p.rindex('</body>'); p = p[:i] + BAR % (name + ' participant page') + '\n' + p[i:]
    open(os.path.join(out, 'PREVIEW - %s Participant.html' % name), 'wb').write(p.encode('utf-8'))
    fz = rd(os.path.join(src, f + '_f.html'))
    mm = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script>\r?\n\(function\(\)\{[\s\S]*?\}\)\(\);\r?\n</script>\r?\n', fz)
    assert mm and 'can_facilitate_lens' in mm.group(0), f
    fz = fz[:mm.start()] + fz[mm.end():]
    i = fz.rindex('</body>'); fz = fz[:i] + BAR % (name + ' facilitator page') + '\n' + fz[i:]
    open(os.path.join(out, 'PREVIEW - %s Facilitator.html' % name), 'wb').write(fz.encode('utf-8'))
print('previews written to', out)
