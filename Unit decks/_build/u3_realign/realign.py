import sys,copy
sys.path.insert(0,sys.path[0])
from lib import *
src,out=sys.argv[1],sys.argv[2]
p=Presentation(src)
S=list(p.slides)
lay=S[35].slide_layout
def new():return p.slides.add_slide(lay)
def N(i):return S[i-1]
def setn(s,t):
    ns=s.notes_slide
    if ns.notes_text_frame is None:
        src=S[35].notes_slide.notes_placeholder._element
        ns.shapes._spTree.append(copy.deepcopy(src))
    ns.notes_text_frame.text=t
def getn(s):return s.notes_slide.notes_text_frame.text
def retitle(s,old,newt):
    for sh in s.shapes:
        if sh.has_text_frame:
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if old in r.text:r.text=r.text.replace(old,newt);return True
    raise SystemExit('title not found '+old)

# ---------- 1.3: readable domain cards in place of the small screenshot ----------
s8=N(8)
for sh in list(s8.shapes):
    if sh.shape_type==13: sh._element.getparent().remove(sh._element)
D=[('Customer Experience & Value','If our SiP statement is true, what should customers consistently experience?'),
   ('Operational Capability & Execution Rhythm','If the SiP becomes reality, how will the organisation operate differently?'),
   ('People & Culture Dynamics','If the SiP is realised, how will leaders and teams work together?'),
   ('Enterprise Value Creation','If the SiP succeeds, what financial reality should we see?')]
for k,(d,q) in enumerate(D):
    x=0.6+(k%2)*6.13; y=1.55+(k//2)*2.2
    dark=k in (1,2)
    box(s8,x,y,6.0,2.1,G if dark else L)
    txt(s8,x+0.3,y+0.12,5.4,0.85,d,size=26,bold=True,font='Cambria',color=W if dark else G,anchor='m')
    txt(s8,x+0.3,y+1.0,5.4,1.0,q,size=24,italic=True,color=W if dark else TX)
bar(s8,'Each domain is read through Keep, Improve, Start and Stop.')

# ---------- Section 3 ----------
setn(N(25),getn(N(25)).replace(
"3. 3.1c: one hot zone card in full, as the pattern for all ten leadership roles.\n4. 3.1d: the matching exercise that each participant completes alone on the portal after the teaching.",
"3. 3.1c: the ten leadership roles.\n4. 3.1d: the hot zone card, taught in full with the CEO, then the CFO and the COO.\n5. 3.1e: the matching exercise that each participant completes alone on the portal after the teaching.").replace("5. The Section 3 Reflections slide.","6. The Section 3 Reflection slide."))

roles=[('CEO','Chief Executive Officer'),('CFO','Chief Financial Officer'),('COO','Chief Operating Officer'),('CHRO','Chief People & Culture Officer'),('CTO/CIO','Chief Technology / Information Officer'),
       ('CMO','Chief Marketing Officer'),('CCO','Chief Commercial Officer'),('CPO','Chief Procurement Officer'),('CRO','Chief Risk Officer'),('CSO','Chief Strategy Officer')]
R=new();title(R,'3.1c · Ten Leadership Roles')
for k,(a,t) in enumerate(roles):
    x=0.6+(k%5)*2.45; y=1.4+(k//5)*2.62
    box(R,x,y,2.3,2.5,DK2,line=GD2)
    txt(R,x+0.18,y+0.15,1.95,0.55,a,size=30,bold=True,color=GD2)
    txt(R,x+0.18,y+0.72,1.98,1.75,t,size=24,color=CR)
setn(R,'''3.1c — TEN LEADERSHIP ROLES (10 ROLES)

HOW TO TEACH IT:

1. Name the ten roles.
Say: "These are the ten leadership roles we work with in this unit: CEO, CFO, COO, CHRO, CTO or CIO, CMO, CCO, CPO, CRO and CSO."

2. Give the four parts of every role card.
Say: "Each role carries four things into the OKR conversation.
Its dominant future realities: the two SiP domains it naturally emphasises.
Its natural OKR emphasis: what it instinctively wants the OKRs to measure.
Its typical hot zone: the point where that emphasis distorts the OKRs it proposes.
Its alignment question: the question that challenges it towards enterprise thinking."

3. Ask the room to place themselves.
Ask: "Which of these ten roles is closest to the one you hold, or the one you hold in your group's company?"
Take three or four answers.

4. Bridge to 3.1d.
Say: "We read one card in full, and you will see the pattern every role follows."''')

s28=N(28);retitle(s28,'3.1c','3.1d')
setn(s28,getn(s28).replace('3.1c — NATURAL OKR EMPHASIS','3.1d — NATURAL OKR EMPHASIS').replace(
'7. Bridge to the matching exercise.\nSay: "Ten roles, ten natural emphases. Let us see how well the room can match them."',
'7. Bridge to the matching exercise.\nSay: "You now know the pattern. In the exercise you complete each card yourself."'))

M=new();title(M,'3.1e · The Matching Exercise')
box(M,0.6,1.5,5.92,4.45,L)
txt(M,0.9,1.7,5.3,0.55,'On each role card',size=26,bold=True,font='Cambria',color=G)
txt(M,0.9,2.4,5.3,3.4,['Role','Dominant Future Realities','Natural OKR Emphasis'],size=24,color=TX)
box(M,6.82,1.5,5.92,4.45,G)
txt(M,7.12,1.7,5.3,0.55,'You select',size=26,bold=True,font='Cambria',color=W)
txt(M,7.12,2.4,5.3,3.4,['Typical Hot Zone','Alignment Question','Green light: a match.','Red alert: the choice belongs to another role.'],size=24,color=W)
bar(M,'Ten roles, completed alone after the teaching. Portfolio work.')
n29=getn(N(29))
port=n29[n29.index('ON THE PORTAL, AFTER THE TEACHING:'):]
setn(M,'''3.1e — MATCH THE HOT ZONE AND THE ALIGNMENT QUESTION (10 ROLES · PORTFOLIO WORK)

HOW TO TEACH IT:

1. Explain the exercise from the slide.
Say: "After the teaching you complete the matching exercise in 3.1 of your own page, on your own.
For each of the ten roles, the role, its dominant future realities and its natural OKR emphasis are given on the card.
You select the typical hot zone and the alignment question that belong to that role.
A green light confirms a match. A red alert shows a choice that belongs to another role, and you choose again.
This is portfolio work: your matches become part of your Learning Portfolio."

2. Debrief the whole picture.
Ask: "If all ten of these hot zones operated simultaneously in our OKR work, what would our final OKR landscape look like? Which domains would be over-represented, and which would be left out?"

3. Name the shift.
Ask: "What is the difference between a functional interpretation of success and a collective definition of success? What does that difference look like in a room full of leaders with different mandates?"
Say: "That is the conversation Section 5 is designed to produce."

4. Close the section.
Say: "Enterprise OKRs emerge when leaders recognise their functional emphasis and balance it across the four Success in Practice domains.
We now know what biases we each bring into the room. Section 5 is where we use that awareness to build something none of us could build alone."

ANSWER KEY (the ten complete cards, for your reference):
- CEO · Hot zone: Objectives become visionary but insufficiently grounded in operational capability. Alignment question: Do our OKRs translate ambition into outcomes the organisation can reliably deliver?
- CFO · Hot zone: Key Results become overly financial, ignoring customer or capability drivers. Alignment question: Are we measuring the drivers of value creation as well as the financial outcomes?
- COO · Hot zone: Objectives drift towards operational optimisation and away from strategic transformation. Alignment question: Are our OKRs reinforcing strategic movement, beyond operational performance?
- CHRO · Hot zone: Objectives emphasise culture initiatives without clear connection to enterprise results. Alignment question: Do our people objectives clearly support strategic outcomes?
- CTO/CIO · Hot zone: Key Results become technology delivery milestones with no line of sight to business outcomes. Alignment question: Are we measuring the impact technology creates for customers and the enterprise?
- CMO · Hot zone: Objectives emphasise perception beyond what the organisation can consistently deliver. Alignment question: Do our OKRs balance customer promise with operational capability?
- CCO · Hot zone: Key Results prioritise sales outcomes without strengthening the customer experience system. Alignment question: Are we building repeatable value creation, beyond short-term revenue?
- CPO · Hot zone: Objectives prioritise cost optimisation at the expense of strategic capability development. Alignment question: Are we balancing efficiency with long-term strategic capability?
- CRO · Hot zone: Key Results become defensive safeguards that slow strategic movement. Alignment question: Are we enabling responsible risk-taking while protecting the organisation?
- CSO · Hot zone: Objectives become conceptually strong but disconnected from operational ownership. Alignment question: Are our OKRs grounded in clear accountability and execution ownership?

'''+port)

# ---------- Section 4: the case slide ----------
n32=getn(N(32))
i3=n32.index('3. Read the Success in Practice')
head=n32[:i3]
rest=n32[i3:]
setn(N(32),head.replace('2. Introduce the game.','2. Introduce the game from this slide.')+'''3. Move to the case.
Say: "Here is the company we take through both gates."''')
import re
def renum(t):
    c=[0]
    def f(m):
        c[0]+=1;return '\n%d. '%c[0]
    return re.sub(r'\n\d+\. ', f, '\n'+t)[1:]
CASE=new();title(CASE,'4.1 · The Case: a Medical Health Company')
box(CASE,0.6,1.45,12.13,2.95,L)
txt(CASE,0.9,1.6,11.55,2.7,'“We will deliver reliable, accessible and patient-centred healthcare by ensuring patients experience timely support, clear communication and coordinated care across every touchpoint. To achieve this, we will strengthen operational coordination, use data to guide decisions, build shared accountability across teams and improve service reliability, efficiency, patient trust and health outcomes.”',size=24,italic=True,color=TX,font='Cambria',anchor='m')
box(CASE,0.6,4.55,5.92,1.45,G);txt(CASE,0.85,4.6,5.45,1.35,[[('Gate 1 · Baggage Check: ',{'bold':True})],[('at least two items for each KISS filter',{})]],size=24,color=W,anchor='m')
box(CASE,6.82,4.55,5.92,1.45,GOLD);txt(CASE,7.07,4.6,5.45,1.35,[[('Gate 2 · Flight Plan: ',{'bold':True})],[('one Objective, two Key Results, contributing roles',{})]],size=24,color=DK,anchor='m')
bar(CASE,'Choose first. The answer is revealed only after selection.')
setn(CASE,'4.1 — STRATEGY AIRPORT · THE CASE AND THE LEARNING ROUND\n\nHOW TO TEACH IT:\n\n'+renum('1. Share the game.\nOpen the facilitator page at Section 4 in your browser before the lesson: the game is built into that page. Stop sharing the deck and share that browser window. If the portal cannot be reached, open the game file Strategy_Airport_unit 3 Game.html from your folder and share that window. Return to the deck when the learning round is complete.\n\n'+rest))

# ---------- Section 5 ----------
F=new();title(F,'5.1 · Translating SiP to KISS')
steps=[('1 · Read your four SiP statements','Brought in from Unit 2. Where your team has refined a statement, type the confirmed wording.'),
       ('2 · Answer the sixteen questions','One SiP domain at a time: Keep, Improve, Start and Stop. Type the agreed answer in each box.'),
       ('3 · Generate our KISS map','When all sixteen boxes are complete. Read the map together before 5.2.')]
for k,(h,b) in enumerate(steps):
    x=0.6+k*4.1;dark=(k==1)
    box(F,x,1.5,3.93,4.45,G if dark else L)
    txt(F,x+0.25,1.7,3.45,1.0,h,size=26,bold=True,font='Cambria',color=W if dark else G)
    txt(F,x+0.25,2.85,3.45,3.0,b,size=24,color=W if dark else TX)
bar(F,'Anchor every entry to the SiP statement, and be specific.')
setn(F,'''5.1 — TRANSLATING SiP TO KISS (4 DOMAINS · GROUP WORK)

HOW TO TEACH IT:

1. Say what the group starts with.
Say: "In 5.1 your group's four SiP statements from Unit 2 appear at the top of the page, brought in from each member's Unit 2 page.
Where your team has since refined a statement in the Capstone S2R® Blueprint, type the confirmed wording in the box."

2. Give the sixteen questions.
Say: "Take one SiP domain at a time. Open the domain and read its SiP statement.
Then answer each of the four guiding questions of 1.3 with your group and type the agreed answer in its box: Keep, Improve, Start and Stop.
Four domains, four filters: sixteen entries in all. Each entry saves as it is typed."

3. Anchor every entry to the SiP.
Say: "Every item you enter must be anchored to the SiP. For example: we should improve cross-functional handover time from 72 to 24 hours because the SiP describes seamless execution rhythm."
Add: "Insist on specificity in your group. Push for the operating reality."

4. Say how the group reaches its entries.
Say: "For each domain, each member first writes their own inputs. Then the group shares them and agrees its entries.
This keeps the first speaker from dominating the KISS landscape."

5. Set the scale.
Say: "Aim for three or four items for each KISS element in each domain. More than five means the group has not yet prioritised: choose."

6. Generate the map.
Say: "When all sixteen boxes are complete, select Generate our KISS map. The next slide shows what it brings together."''')

s35=N(35)
setn(s35,'''5.1 — OUR KISS MAP (4 DOMAINS × KISS)

HOW TO TEACH IT:

1. Walk the map on the slide.
Say: "This is the shape of your KISS map: the four SiP domains against Keep, Improve, Start and Stop."
Point to each domain band as you name it: Customer Experience & Value, Operational Capability & Execution Rhythm, People & Culture Dynamics, Enterprise Value Creation.

2. Say what the map is for.
Say: "Read the map together as a group before you go on to 5.2. It is the source of your four themes.
The confirmed Keep, Improve, Start and Stop feed your team's Capstone S2R® Blueprint."

3. Bridge to 5.2.
Say: "The four themes of 5.2 open only once the map is generated."

ON THE PORTAL, AFTER THE TEACHING:
In 5.1 of the participant file the group answers the four KISS guiding questions for each SiP domain (sixteen entries) and selects Generate our KISS map. The scribe types what the group agrees, and the entries appear on every member's page.

LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:
- Ask each member to write their own inputs for a domain before the group discusses it.
- After all four domains are captured, ask the group, domain by domain: "Read this domain's Improve and Start entries together. What one shift do they point to?" These shifts become the four themes of 5.2.
Point the groups to their company overview. Say: "Your company overview, just above the group record bar, shows your company, your trigger, your three problems and your central problem statement. Every part of this work is done for that company and its central problem."''')

# 5.2 flow
T1=new();title(T1,'5.2 · Finding Your Four Themes')
fl=[('SiP statement','Read the domain’s statement',L,G,TX),('Improve + Start','What must be done better, and what must begin',G,W,W),('One theme','The one shift, in a few words',GOLD,DK,DK)]
for k,(h,b,f,hc,bc) in enumerate(fl):
    x=0.6+k*4.1
    box(T1,x,1.5,3.7,2.6,f)
    txt(T1,x+0.25,1.7,3.2,0.6,h,size=28,bold=True,font='Cambria',color=hc)
    txt(T1,x+0.25,2.45,3.2,1.5,b,size=24,color=bc)
    if k<2: txt(T1,x+3.72,2.35,0.38,0.8,'→',size=32,bold=True,color=G,align='c')
box(T1,0.6,4.3,12.13,1.65,L)
txt(T1,0.9,4.4,11.55,1.45,[[('Keep: ',{'bold':True,'color':G}),('what the organisation protects while it makes the shift.',{})],[('Stop: ',{'bold':True,'color':G}),('a once-off decision the organisation acts on directly. Neither becomes a theme.',{})]],size=24,anchor='m')
bar(T1,'Four themes only: one for each SiP domain.')
setn(T1,'''5.2 — FINDING YOUR FOUR THEMES (STEP 1 · GROUP WORK)

HOW TO TEACH IT:

1. Link 5.2 to 5.1.
Say: "With your KISS map complete, your group begins the five steps of 1.5. 5.2 is Step 1: Find Themes."

2. Walk the flow on the slide, left to right.
Say: "Take one SiP domain at a time. Read the domain's SiP statement.
Then read its Improve and Start entries together: what the organisation must do better and what it must begin.
Name the one shift they point to. That shift is the theme."

3. Say what a theme is.
Say: "A theme names one shift the organisation must make to reach the SiP, in a few words, such as Customer responsiveness or Execution speed.
It is a shift. It is not yet an Objective, and it is not a task."

4. Place Keep and Stop.
Say: "Stop entries are once-off decisions you act on directly, and Keep entries are what you protect while you make the shift. Neither becomes a theme."

5. Say how the group agrees each theme.
Say: "Each member writes down, privately, the one shift they see in the domain's Improve and Start entries. Then share, and agree one theme for the domain.
Writing first, then sharing, prevents the anchoring bias where the first speaker dominates the room."

6. Bridge to the table.
Say: "Four themes only: one for each SiP domain. The next slide shows the table they go into."

LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:
Collect every member's written shift for a domain before any discussion begins.''')

def table(s,x,y,w,colw,heads,rows,rowh=1.0,headh=0.75):
    from pptx.util import Inches,Pt
    gt=s.shapes.add_table(len(rows)+1,len(heads),Inches(x),Inches(y),Inches(w),Inches(headh+rowh*len(rows))).table
    for j,cw in enumerate(colw):gt.columns[j].width=Inches(cw)
    gt.rows[0].height=Inches(headh)
    for i in range(1,len(rows)+1):gt.rows[i].height=Inches(rowh)
    def cell(c,t,fill,col,b=False):
        c.fill.solid();c.fill.fore_color.rgb=rgb(fill);c.text_frame.text='';c.text_frame.word_wrap=True
        c.margin_left=c.margin_right=Inches(0.12);c.margin_top=c.margin_bottom=Inches(0.05)
        r=c.text_frame.paragraphs[0].add_run();r.text=t;r.font.size=Pt(24);r.font.bold=b;r.font.name='Calibri';r.font.color.rgb=rgb(col)
        c.vertical_anchor=MSO_ANCHOR.MIDDLE
    for j,h in enumerate(heads):cell(gt.cell(0,j),h,DK,GD2,True)
    for i,row in enumerate(rows,1):
        for j,t in enumerate(row):cell(gt.cell(i,j),t,L if i%2 else 'FFFFFF',G if j==0 else TX,j==0)
    tblPr=gt._tbl.tblPr;tblPr.set('firstRow','0');tblPr.set('bandRow','0')
T2=new();title(T2,'5.2 · Table: Our Four Themes')
table(T2,0.6,1.4,12.13,[4.6,2.5,2.5,2.53],['SiP domain','Improve','Start','Our theme'],
      [['Customer Experience & Value','','',''],['Operational Capability & Execution Rhythm','','',''],['People & Culture Dynamics','','',''],['Enterprise Value Creation','','','']],rowh=1.08)
setn(T2,'''5.2 — TABLE: OUR FOUR THEMES

HOW TO TEACH IT:

1. Walk the table on the slide.
Say: "When all four themes are recorded, a table shows each theme beside the Improve and Start entries it comes from: one row for each SiP domain."

2. Say how the group uses it.
Say: "Read the table together before you go on to 5.3.
Check each row: does the theme name the one shift that its Improve and Start entries point to?"

3. Bridge to 5.3.
Say: "Each theme is carried into 5.3, where your group turns it into an OKR."

ON THE PORTAL, AFTER THE TEACHING:
In 5.2 of the participant file the four SiP domains are shown one at a time, each with the group's SiP statement for the domain and its Keep, Improve, Start and Stop entries from 5.1. The group records one theme for each domain, and the table Our Four Themes shows the four themes beside the Improve and Start entries they come from.''')

# 5.3
O1=new();title(O1,'5.3 · From Themes to OKRs')
st=[('Step 2 · Inspiring Objectives','One Objective for the theme: bold, qualitative, starting with a verb.'),
    ('Step 3 · Define Key Results','Up to two Key Results: Verb + Metric + From X to Y + Deadline. Name the contributing roles for each.'),
    ('Step 4 · Alignment Test','Tick each of the four questions answered with a clear yes. Four ticks: the OKR is aligned.')]
for k,(h,b) in enumerate(st):
    x=0.6+k*4.1;dark=(k==1)
    box(O1,x,1.5,3.93,4.45,G if dark else L)
    txt(O1,x+0.25,1.7,3.45,1.0,h,size=26,bold=True,font='Cambria',color=W if dark else G)
    txt(O1,x+0.25,2.85,3.45,3.0,b,size=24,color=W if dark else TX)
bar(O1,'One theme at a time through Steps 2 to 4, then the next theme.')
setn(O1,'''5.3 — FROM THEMES TO OKRs (STEPS 2 TO 4 · GROUP WORK)

HOW TO TEACH IT:

1. Link 5.3 to 5.2.
Say: "Each theme from 5.2 becomes one OKR. Take one theme at a time through Steps 2 to 4 before you move to the next."

2. Step 2 — Inspiring Objectives.
Say: "Translate the theme into a bold, qualitative statement that expresses strategic ambition. Start with a verb and describe the desired transformation.
Make it ambitious, keep it qualitative and keep it memorable."
Say: "Draft the Objective privately first, then agree the group's wording.
The T-shirt test applies: if you cannot say it in a hallway conversation, simplify it."

3. Step 3 — Define Key Results.
Say: "For the Objective, write up to two Key Results in the form Verb + Metric + From X to Y + Deadline, and name the contributing roles for each Key Result."
Say: "Hold each Key Result to the benchmark: shift response time from 12 hours to 4 hours by Q3."

4. Step 4 — Alignment Test.
Say: "Read your OKR aloud and test it against the four questions:
Does this truly get the organisation closer to the shared SiP vision?
Would fellow leaders see this as a win for the whole organisation, or just for one function?
Does it visibly improve culture, operations or value creation?
Is there clear accountability for delivering this outcome?
Tick a question only when the answer is a clear yes.
An OKR with all four ticks is aligned and goes forward to 5.4. An OKR that cannot earn four clear yeses goes back to Step 2 or Step 3."

5. Bridge to the table.
Say: "The next slide shows the table your four OKRs go into."

LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:
- Apply the four-part formula rigorously. When a Key Result reads as an activity, ask: "Can you check it off a task list?"
- Ask the group to read each OKR and answer the four questions aloud. The room quickly shows whether the OKR serves the whole organisation or one function.
- Use the hot zones. After a leader describes an OKR, ask the room: "Which hot zone does this perspective risk creating?"''')

O2=new();title(O2,'5.3 · Table: Our OKRs')
table(O2,0.6,1.4,12.13,[2.4,3.3,4.23,2.2],['Theme','Objective','Key Results · contributing roles','Alignment test'],
      [['Theme 1','','','✓ ✓ ✓ ✓'],['Theme 2','','','✓ ✓ ✓ ✓'],['Theme 3','','','✓ ✓ ✓ ✓'],['Theme 4','','','✓ ✓ ✓ ✓']],rowh=1.08)
setn(O2,'''5.3 — TABLE: OUR OKRs

HOW TO TEACH IT:

1. Walk the table on the slide.
Say: "When all four OKRs are aligned, a table shows each theme with its Objective, its Key Results with their contributing roles, and its alignment test."

2. Say how the group uses it.
Say: "Read the table together before you go on to 5.4.
Check each row against the line of sight: theme, then Objective, then Key Results. Each Key Result should prove its own Objective."

3. Bridge to 5.4.
Say: "Four aligned OKRs now go to the Prioritisation Matrix."

ON THE PORTAL, AFTER THE TEACHING:
In 5.3 of the participant file the four themes are shown one at a time. For each theme the group writes one Objective, up to two Key Results with the contributing roles for each, and ticks the four alignment questions it answers with a clear yes. The table Our OKRs shows all four for the group to read together before 5.4.''')

# 5.4 matrix
P1=new();title(P1,'5.4 · Prioritising Your OKRs')
box(P1,0.6,1.35,12.13,0.95,L);txt(P1,0.9,1.35,11.55,0.95,'First agree what high impact and high effort mean for your company. Then set the Impact and the Effort of each OKR.',size=24,anchor='m')
cats=[['Strategic Catalysts','Accelerated Enablers','Core Strategic Drivers'],['Quick Efficiency Plays','Targeted Growth Projects','Heavy Investment Candidates'],['Supportive Enablers','Marginal Utility Tasks','Resource Pitfalls']]
txt(P1,0.6,2.45,1.7,0.45,'Impact',size=24,bold=True,color=G)
for j,e in enumerate(['Low effort','Medium effort','High effort']):txt(P1,2.35+j*3.47,2.45,3.35,0.45,e,size=24,bold=True,color=G,align='c')
for i,imp in enumerate(['High','Medium','Low']):
    y=2.95+i*1.05
    txt(P1,0.6,y,1.7,0.95,imp,size=24,bold=True,color=G,anchor='m')
    for j in range(3):
        f=G if i==0 else L
        box(P1,2.35+j*3.47,y,3.35,0.95,f)
        txt(P1,2.45+j*3.47,y,3.15,0.95,cats[i][j],size=24,bold=(i==0),color=W if i==0 else TX,anchor='m',align='c')
setn(P1,'''5.4 — PRIORITISING YOUR OKRs (STEP 5 · GROUP WORK)

HOW TO TEACH IT:

1. Link 5.4 to 5.3.
Say: "Your four aligned OKRs are placed on the Prioritisation Matrix. This is Step 5.
The matrix shows which OKRs accelerate the strategy and which consume resources for less movement, so your group can see where to move first."

2. Agree the definitions first.
Say: "Before you place the first OKR, agree what high impact and high effort mean for your company.
Impact is the strategic value delivered if the Objective is achieved.
Effort is the time, resources, coordination and organisational change required."
Ask: "What does high effort mean in your company: time, money, change management, or all three?"

3. Place each OKR.
Say: "Set the Impact and the Effort of each OKR. The matrix shows its place."

4. Read the top row.
Say: "Pay particular attention to the top row: Strategic Catalysts, Accelerated Enablers and Core Strategic Drivers. These are the highest-leverage execution signals."

5. Bridge to the group record.
Say: "Once all four OKRs are placed, your group record is complete."

LATER, WHEN THE GROUPS DO THE WORK ON THE PORTAL:
Walk through the matrix structure before the group places any OKR, and ask it to agree what counts as high impact and high effort for its strategy. These discussions are where collective intelligence is built, so the group takes the time it needs before it agrees each placement.''')

P2=new();title(P2,'5.4 · Your Group Record')
fl=[('Read','the record together'),('Agree','every member selects Agree'),('Print','the group record'),('Capstone','boxes 3A to 3F')]
for k,(h,b) in enumerate(fl):
    x=0.6+k*3.07
    f=[L,G,L,GOLD][k];hc=[G,W,G,DK][k];bc=[TX,W,TX,DK][k]
    box(P2,x,1.5,2.85,2.3,f)
    txt(P2,x+0.2,1.65,2.45,0.6,h,size=28,bold=True,font='Cambria',color=hc)
    txt(P2,x+0.2,2.35,2.45,1.35,b,size=24,color=bc)
box(P2,0.6,4.0,12.13,1.95,L)
txt(P2,0.9,4.1,11.55,1.75,[[('The record holds ',{}),('each theme',{'bold':True,'color':G}),(' with its SiP domain, Objective, Key Results and contributing roles, alignment test and place on the matrix.',{})]],size=24,anchor='m')
bar(P2,'When every member has agreed, the Objectives and Key Results feed the Capstone.')
setn(P2,'''5.4 — YOUR GROUP RECORD (GROUP WORK · CAPSTONE)

HOW TO TEACH IT:

1. Say what the record holds.
Say: "Below the matrix, your group record shows the four themes, each with its SiP domain, Objective, Key Results and contributing roles, alignment test and place on the matrix."

2. Walk the four boxes on the slide.
Say: "When all four OKRs are aligned and placed, read the record together.
Every member selects Agree. Then print the record."

3. Say where the work goes.
Say: "When every member has agreed, your Objectives and Key Results feed your team's Capstone S2R® Blueprint, together with your KISS map.
The Unit 3 section of the Blueprint opens once every member of your team has completed this unit. It brings in your confirmed Keep, Improve, Start, Stop, Objectives and Key Results, boxes 3A to 3F, and your team reads them together and confirms them."

4. Bridge to the reflection.
Say: "Before the unit closes, one reflection for Section 5."

ON THE PORTAL, AFTER THE TEACHING:
In 5.4 of the participant file the group sets the Impact and Effort of each aligned OKR and places it on Our Prioritisation Matrix, then reads the group record, selects Agree and prints it. The group agrees each entry; the scribe types it, and it appears on every member's page.''')

# ---------- order ----------
order=S[0:27]+[R,S[27],M]+S[29:32]+[CASE,S[32],S[33],F,S[34],T1,T2,O1,O2,P1,P2]+S[36:38]
lst=p.slides._sldIdLst
ids={s.slide_id:el for el in lst for s in [None] if False}
els={int(el.get('id')):el for el in lst}
keep=[s.slide_id for s in order]
for sid,el in list(els.items()):
    if sid not in keep:
        rid=el.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        lst.remove(el);p.part.drop_rel(rid)
for el in list(lst):lst.remove(el)
for sid in keep:lst.append(els[sid])
p.save(out);print('slides',len(p.slides))
