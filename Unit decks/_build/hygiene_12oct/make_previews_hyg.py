# -*- coding: utf-8 -*-
"""PREVIEW copies of pages, for opening by double-click (no sign-in; answers stay in this browser). Never committed or uploaded.
Usage: python3 make_previews_hyg.py <fake-supabase.js> <s2r-save.js> <out folder> <page> [<page> ...]"""
import sys, os, re, json
fake, save, out = sys.argv[1:4]; pages = sys.argv[4:]
os.makedirs(out, exist_ok=True)
F = open(fake, encoding='utf-8').read().replace("var RPC={", "var RPC={can_facilitate_lens:function(){return true;},is_facilitator:function(){return true;},")
SV = open(save, encoding='utf-8').read()
TITLE = {'unit1': 'Unit 1', 'unit2_m1_lens1': 'Unit 2', 'unit2_m1_lens2': 'Unit 3', 'unit2_m1_lens3': 'Unit 4', 'unit3_m1_lens4': 'Unit 5', 'unit3_m1_lens5': 'Unit 6', 'unit3_m1_lens6': 'Unit 7'}
LENS = {'unit1': 'u1_foundations', 'unit2_m1_lens1': 'u2m1_lens1', 'unit2_m1_lens2': 'u2m1_lens2', 'unit2_m1_lens3': 'u2m1_lens3', 'unit3_m1_lens4': 'u3m1_lens4', 'unit3_m1_lens5': 'u3m1_lens5', 'unit3_m1_lens6': 'u3m1_lens6'}
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · not the live portal</div>')
for pth in pages:
    name = os.path.basename(pth); key = [k for k in TITLE if name.startswith(k)][0]; fac = name.lower().endswith('_f.html')
    t = open(pth, 'rb').read().decode('utf-8')
    seed = {'profiles': [{'id': 'u-1', 'role': 'facilitator' if fac else 'participant', 'full_name': 'Preview'}],
            'cohort_memberships': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'role_in_cohort': 'participant', 'joined_at': '2026-09-01'}],
            'lens_progress': [{'profile_id': 'u-1', 'cohort_id': 'c-1', 'lens_id': LENS[key], 'status': 'unlocked'}],
            'lens_responses': [], 'submissions': [], 'lens_catalog': []}
    boot = ("<script>\n(function(){try{var d=JSON.parse(localStorage.getItem('fakedb')||'null');if(!d||!d.profiles||d.profiles[0].role!=='%s'){localStorage.setItem('fakedb',%s);}"
            "localStorage.setItem('fake_uid','u-1');}catch(e){}})();\n" % ('facilitator' if fac else 'participant', json.dumps(json.dumps(seed))) + F + '</script>')
    t, n = re.subn(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>', lambda m: boot, t, count=1); assert n == 1, name
    t = re.sub(r'<script src="/?s2r-save\.js"></script>', lambda m: '<script>\n' + SV + '</script>', t, count=1)
    t = re.sub(r'<title>[^<]*</title>', '<title>PREVIEW · %s — %s</title>' % (TITLE[key], 'Facilitator' if fac else 'Participant'), t, count=1)
    i = t.rindex('</body>'); t = t[:i] + BAR % ('%s %s page' % (TITLE[key], 'facilitator' if fac else 'participant')) + '\n' + t[i:]
    nm = 'PREVIEW - %s %s.html' % (TITLE[key], 'Facilitator' if fac else 'Participant')
    open(os.path.join(out, nm), 'wb').write(t.encode('utf-8')); print(nm)
