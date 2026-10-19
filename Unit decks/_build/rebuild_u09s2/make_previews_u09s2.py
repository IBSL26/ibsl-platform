# -*- coding: utf-8 -*-
"""Stand-alone PREVIEW copies (double-click to open). Never committed or uploaded.
Usage: python3 make_previews_u09s2.py <p> <f> <mock js> <out folder>"""
import sys, os, re
p_src, f_src, mock, out = sys.argv[1:5]
rd = lambda x: open(x, encoding='utf-8', newline='').read()
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · not the live portal%s</div>')
CLEAR = (' &nbsp; <button type="button" onclick="if(confirm(\'Clear everything you typed in this preview and start again?\'))__clearPreview()" '
         'style="font:700 11px Arial,sans-serif;padding:3px 10px;border:1px solid #111811;background:transparent;border-radius:3px;cursor:pointer;">Start again</button>')
U1 = r"""
  var U1_SAMPLE={__pc_work:{ch:{design:['Sample (preview only): strategy is set by the executive team without the people who must deliver it','Sample: priorities change every quarter','Sample: plans are not costed'],
    execution:['Sample: decisions wait weeks for head-office approval','Sample: functions work to their own targets','Sample: data from different systems does not agree'],
    sustain:['Sample: improvements fade after the first review','Sample: the same problems return each year','Sample: strong performers leave']},
    pick:{design:['Sample (preview only): strategy is set by the executive team without the people who must deliver it','Sample: priorities change every quarter'],
    execution:['Sample: decisions wait weeks for head-office approval','Sample: functions work to their own targets','Sample: data from different systems does not agree'],
    sustain:['Sample: improvements fade after the first review','Sample: the same problems return each year']}},
    confirmed_items:['Problem Charter \u00b7 Challenges We Will Address']};
"""
m = rd(mock).replace('  function bag(lens){if(!store[lens])store[lens]=(', U1 + "  function bag(lens){if(!store[lens])store[lens]=(lens==='u1_foundations'?JSON.parse(JSON.stringify(U1_SAMPLE)):", 1)
assert "U1_SAMPLE))" in m
os.makedirs(out, exist_ok=True)
p = rd(p_src)
mx = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script src="/s2r-save\.js"></script>\r?\n<script src="/s2r-team\.js"></script>', p)
assert mx
p = p[:mx.start()] + '<script>\n' + m + '</script>' + p[mx.end():]
p, n = re.subn(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 9 — Participant</title>', p, count=1); assert n == 1
i = p.rindex('</body>'); p = p[:i] + (BAR % ('Unit 9 participant page · your entries stay in this browser only · nothing is sent', CLEAR)) + '\n' + p[i:]
open(os.path.join(out, 'PREVIEW - Unit 9 Participant.html'), 'w', encoding='utf-8', newline='').write(p)
f = rd(f_src)
mm = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r?\n<script>\r?\n\(function\(\)\{[\s\S]*?\}\)\(\);\r?\n</script>\r?\n', f)
assert mm and 'can_facilitate_lens' in mm.group(0)
f = f[:mm.start()] + f[mm.end():]
f = re.sub(r'<title>[^<]*</title>', '<title>PREVIEW · Unit 9 — Facilitator</title>', f, count=1)
i = f.rindex('</body>'); f = f[:i] + (BAR % ('Unit 9 facilitator page', '')) + '\n' + f[i:]
open(os.path.join(out, 'PREVIEW - Unit 9 Facilitator.html'), 'w', encoding='utf-8', newline='').write(f)
print('previews written to', out)
