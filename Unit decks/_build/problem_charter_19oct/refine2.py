# -*- coding: utf-8 -*-
"""Unit 1 · 19 Oct refinement 2: Distortion Lab out of both pages, Portfolio Artefact out of the participant page,
   a narrative for 6.1 on both pages. Runs on the pages build_pc.py wrote. Usage: python3 refine2.py <folder>"""
import sys, os, re
D = sys.argv[1]
def rd(n):
    t = open(os.path.join(D, n), encoding='utf-8', newline='').read(); return t.replace('\r\n', '\n'), ('\r\n' in t)
def wr(n, t, crlf):
    open(os.path.join(D, n), 'w', encoding='utf-8', newline='').write(t.replace('\n', '\r\n') if crlf else t)
def rep(t, a, b, label):
    n = t.count(a)
    if n != 1: raise SystemExit('STOP · %s · %d' % (label, n))
    return t.replace(a, b)
def cut(t, start, end, label):
    """Remove from the line that starts with `start` up to (not including) the first later occurrence of `end`."""
    i = t.find(start)
    if i < 0 or t.count(start) != 1: raise SystemExit('STOP · cut start · ' + label)
    j = t.find(end, i + len(start))
    if j < 0: raise SystemExit('STOP · cut end · ' + label)
    return t[:i] + t[j:]

P61 = ('<p>Sections 1 to 5 showed how bias shapes the way leaders think, decide and behave, and how the thinking environment a leader creates protects or weakens judgement. '
       'The Self Reflection Bias Assessment turns that learning on you. It shows how consistently your own leadership practice holds the behavioural conditions for sound strategic judgement today.</p>'
       '<p>The assessment covers five areas, with four statements in each:</p>'
       '<ul><li><strong>A1 · I Know My Biases:</strong> recognising the patterns in your own thinking that may not serve the organisation.</li>'
       '<li><strong>A2 · I Manage My Emotional Impact:</strong> the climate your emotional state sets for how others think and speak up.</li>'
       '<li><strong>A3 · I Build Psychological Safety:</strong> the conditions in which honest challenge is expected and protected.</li>'
       '<li><strong>A4 · I Use Process to Protect Quality:</strong> the structured approaches that protect your judgement.</li>'
       '<li><strong>A5 · I Treat People as the Strategy:</strong> the attention you give to the quality of your team&rsquo;s thinking.</li></ul>'
       '<p>Your results give an overall score out of 100, a score for each area and the area where you are most exposed. That area is your development priority: the place where deliberate practice will most improve your strategic judgement as you lead your simulated executive team through CESI.</p>\n')
F61 = ('<p><strong>What 6.1 does:</strong> Sections 1 to 5 showed how bias shapes the way leaders think, decide and behave, and how the thinking environment a leader creates protects or weakens judgement. '
       'The Self Reflection Bias Assessment turns that learning on each participant. It shows how consistently their own leadership practice holds the behavioural conditions for sound strategic judgement today.</p>'
       '<p>The assessment covers five areas, with four statements in each: A1 · I Know My Biases; A2 · I Manage My Emotional Impact; A3 · I Build Psychological Safety; A4 · I Use Process to Protect Quality; A5 · I Treat People as the Strategy. '
       'The results give an overall score out of 100, a score for each area and the area where the participant is most exposed: their development priority as they lead their simulated executive team through CESI.</p>\n')

# ── participant ──
p, pc = rd('unit1_P.html')
p = rep(p, '<p>The Self Reflection Bias Assessment, the Problem Charter and Portfolio Artefact</p>', '<p>The Self Reflection Bias Assessment and the Problem Charter</p>', 'P hero')
p = cut(p, '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">The Distortion Lab: The Growth Decision</span>',
        '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">6.1 — Self Reflection Bias Assessment</span>', 'P lab')
p = cut(p, '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Closing Reflection — Portfolio Artefact</span>',
        '<div class="acc">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Summary</span>', 'P portfolio')
p = rep(p, '<span class="acc-t">6.1 — Self Reflection Bias Assessment</span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">Interactive Scoring Tool</span><div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div></div>\n<div class="acc-b cb">\n',
        '<span class="acc-t">6.1 — Self Reflection Bias Assessment</span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">Interactive Scoring Tool</span><div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div></div>\n<div class="acc-b cb">\n' + P61, 'P 6.1 narrative')
p = rep(p, "Unit 1 · Behavioural Strategy Fundamentals complete. Your portfolio artefact has been saved. Proceed to Module 2: Direction when ready.",
        "Unit 1 · Behavioural Strategy Fundamentals complete. Proceed to Module 2: Direction when ready.", 'P alert')
p = rep(p, 'Your reflections throughout this unit form your Unit 1 portfolio artefact.', 'Your reflections throughout this unit go into your Learning Portfolio.', 'P unit desc')
wr('unit1_P.html', p, pc)

# ── facilitator ──
f, fc = rd('unit1_F.html')
f = rep(f, '<p>The Distortion Lab, the Self Reflection Bias Assessment and the Problem Charter</p>', '<p>The Self Reflection Bias Assessment and the Problem Charter</p>', 'F hero')
i = f.find('<div class="fac-note"><div class="fac-note-label">&#9670; FACILITATOR GUIDANCE — Section 6 · Application</div>'); j = f.find('</div>\n', i)
if i < 0: raise SystemExit('STOP · F section note')
f = f[:i] + ('<div class="fac-note"><div class="fac-note-label">&#9670; FACILITATOR GUIDANCE — Section 6 · Application</div>'
             '<p><strong>Section intent:</strong> This is the application section. Participants first turn the unit&rsquo;s learning on themselves in the Self Reflection Bias Assessment (Section 6.1). Each group then creates its simulated company and writes its Problem Charter (Section 6.2), which opens the Capstone.</p>') + f[j:]
f = cut(f, '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Facilitator · The Distortion Lab: The Growth Decision</span>',
        '<div class="acc">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">6.1 — Self Reflection Bias Assessment</span>', 'F lab')
f = rep(f, '<div class="acc">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">6.1 — Self Reflection Bias Assessment</span>', '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">6.1 — Self Reflection Bias Assessment</span>', 'F 6.1 open')
f = rep(f, '<div class="fac-note"><div class="fac-note-label">&#9670; FACILITATOR GUIDANCE — Section 6.1</div>', F61 + '<div class="fac-note"><div class="fac-note-label">&#9670; FACILITATOR GUIDANCE — Section 6.1</div>', 'F 6.1 narrative')
f = rep(f, 'Direct participants to click the "Summary" tab.', 'Direct participants to the "Results" tab.', 'F results tab')
f = rep(f, ' Allow 10–12 minutes for completion without interruption.', ' Allow completion without interruption.', 'F 6.1 time')
f = rep(f, 'culminating in a simulation exercise and a self reflection bias assessment across five areas.', 'culminating in a self reflection bias assessment across five areas and each group&rsquo;s Problem Charter.', 'F summary')
f = rep(f, ' This becomes the anchor for their personal portfolio artefact at the end of Unit 1.', '', 'F portfolio anchor')
wr('unit1_F.html', f, fc)
print('refine2 done')
