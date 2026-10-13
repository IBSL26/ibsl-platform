# -*- coding: utf-8 -*-
"""Unit 8 amendments of 13 October 2026: dashboard_F.html labels for the reworked answers.
ref5 is reframed (the conversation type most difficult for the participant and their team); ref8 is new (the velocity gap, part 2.1);
the four 4.2 answers keep their keys and are relabelled for the GROW analysis. Then run on the device: node build_collection.js
Usage: python3 patch_links_u08_r5.py <dashboard_F.html> <out>"""
import sys
src, out = sys.argv[1:3]
raw = open(src, 'rb').read().decode('utf-8'); crlf = '\r\n' in raw; t = raw.replace('\r\n', '\n')
P = [("      ref5: 'Your Progress Signal',\n      ref6: 'Your Early Warning Signal',\n      ref7: 'Your Execution Learning',\n",
      "      ref5: 'The Conversation Type Most Difficult for Your Team',\n      ref6: 'Your Early Warning Signal',\n      ref7: 'Your Execution Learning',\n      ref8: 'Where You Have Seen the Velocity Gap',\n"),
     ("      app_rootcause: 'Accountability Loop Case · Realign: the root cause and the clues',\n      app_corrective: 'Accountability Loop Case · Restore: actions, follow-up and alignment score',\n",
      "      app_rootcause: 'Accountability Loop Case · Realign: the root cause evident and the lines that show it',\n      app_corrective: 'Accountability Loop Case · Restore with GROW: resolving the root cause, alignment close to 10',\n"),
     ("      rp_review: 'Accountability Loop Case · Review: the evidence used',\n      rp_judge: 'Accountability Loop Case · Your judgement against the three criteria',\n",
      "      rp_review: 'Accountability Loop Case · Review: the evidence and the alignment score',\n      rp_judge: 'Accountability Loop Case · Your judgement against the GROW model',\n"),
     ('5:"Your Progress Signal",6:"Your Early Warning Signal",7:"Your Execution Learning"},',
      '5:"The Conversation Type Most Difficult for Your Team",6:"Your Early Warning Signal",7:"Your Execution Learning",8:"Where You Have Seen the Velocity Gap"},')]
for a, b in P:
    assert t.count(a) == 1, a[:80]; t = t.replace(a, b)
open(out, 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8')); print('dashboard_F.html written,', len(P), 'changes')
