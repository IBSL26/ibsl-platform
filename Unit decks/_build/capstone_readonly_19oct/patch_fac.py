# -*- coding: utf-8 -*-
import sys
f4,f5,o4,o5=sys.argv[1:5]
def once(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:80]); return s.replace(a,b)
ARR='<div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div>'
s=open(f4,encoding='utf-8',newline='').read(); CR4='\r\n' in s; s=s.replace('\r\n','\n')
s=once(s,"<p><strong>Closing the section:</strong> End with a commitment question: <em>&ldquo;Which one MBT condition, if left unverified, represents the greatest risk to our strategy&rsquo;s integrity? Who is responsible for that verification?&rdquo;</em></p>",
 "<p><strong>Moving to 5.3:</strong> Close 5.2 with the question 5.3 answers: <em>&ldquo;Which one MBT condition, if left unverified, represents the greatest risk to our strategy&rsquo;s integrity? Who is responsible for that verification?&rdquo;</em></p>")
s=once(s,"<li>A record shows the condition named at each step for every Key Result. When every Key Result has been taken through the four steps, each participant selects Agree. Print gives a copy of the record.</li></ol>\n    <p>The confirmed work feeds the team&rsquo;s Capstone Blueprint.</p>\n  </div>\n</div>\n</div>\n",
 "<li>A record shows the condition named at each step for every Key Result. When every Key Result has been taken through the four steps, the group goes on to 5.3.</li></ol>\n  </div>\n</div>\n</div>\n\n"
 '<div class="acc">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">5.3 &mdash; Verification Ownership and Executive Blind Spots</span>\n  <div style="display:flex;align-items:center;gap:10px;"><span class="acc-meta">Capstone Work</span>'+ARR+'</div>\n</div>\n<div class="acc-b cb">\n'
 '  <div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE &mdash; Section 5.3</div>\n'
 '    <p><strong>Briefing for participants:</strong> Each Must-Be-True condition named in 5.2 holds only while someone checks it. The group assigns each critical check to an executive and names the checkpoint its executive team is most likely to overlook.</p>\n'
 '    <p><strong>On ownership:</strong> Teach that one executive owns each check, with evidence someone else could inspect and a date. Link the blind spot to the role-based blind spots taught in Section 3.</p>\n  </div>\n'
 '  <div class="fac-note-full u4-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n'
 '    <p>Participants work in their groups, in 5.3 of their own file. This is Capstone work, typed by the group&rsquo;s scribe.</p>\n'
 '    <ol><li>The group reads its Must-Be-True conditions from 5.2, listed in 5.3.</li><li><strong>Verification ownership.</strong> For each critical condition, the group names the executive accountable for verifying it, the evidence that will confirm it still holds, and the date of the first check.</li><li><strong>Executive blind spot.</strong> The group selects the checkpoint its executive team is most likely to overlook, given the roles around its table, and states the enterprise risk if it does.</li><li>Each participant reads the record and selects Agree. Print gives a copy of the record.</li></ol>\n'
 '    <p>The agreed work feeds boxes 4A to 4F of the team&rsquo;s Capstone Blueprint.</p>\n  </div>\n</div>\n</div>\n')
open(o4,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if CR4 else s)
t=open(f5,encoding='utf-8',newline='').read(); CR5='\r\n' in t; t=t.replace('\r\n','\n')
t=once(t,"<li><strong>Step 2 · ACE-IT.</strong> The group reads its team OCEAVL profile. It then states",
 "<li><strong>Step 2 · ACE-IT.</strong> The group reads its team OCEAVL profile and names the two dimensions on which the team carries the highest risk for the strategy, with the response to each. It then states")
t=once(t,"<li>The group reads its team OCEAVL profile, shown on each page once every member of the team has submitted their scores in part 3.1.</li><li>The group reads the guide in each card.",
 "<li>The group reads its team OCEAVL profile, shown on each page once every member of the team has submitted their scores in part 3.1.</li><li>The group names the two dimensions on which its executive team carries the highest risk for the strategy, and the response it adopts for each.</li><li>The group reads the guide in each card.")
t=once(t,"<p>The agreed record feeds the team&rsquo;s Capstone Blueprint: the Shift, Stake and Step, and the five expected leadership behaviours.</p>",
 "<p>The agreed record feeds the team&rsquo;s Capstone Blueprint: the two highest-risk dimensions, the Shift, Stake and Step, and the five expected leadership behaviours.</p>")
open(o5,'w',encoding='utf-8',newline='').write(t.replace('\n','\r\n') if CR5 else t)
print('ok')
