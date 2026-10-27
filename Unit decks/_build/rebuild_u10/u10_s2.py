# -*- coding: utf-8 -*-
"""Unit 10 Section 2 · Intelligence, as Carol gave it (27 Oct, 16:56)."""
from u10_content import acc

TITLE = 'The ESRG Ignition Point: How Each Domain Enables Execution'
HERO_P = 'The four execution-enabling capabilities, and a scanner that profiles how well your function’s operating conditions support its strategic commitments.'
HERO_F = 'The four execution-enabling capabilities, and a scanner that profiles how well a function’s operating conditions support its strategic commitments.'
LO = ['Translate strategic performance requirements into functional operating capabilities through the four ESRG execution enablers.',
      'Build and maintain an evidence-based functional ESRG performance profile to identify operating strengths, constraints and changes in alignment over time.']
GUIDE = 'In Awareness, participants specified the operating conditions their strategic commitments require and located them within FIT, SIP, AIR and PAR. Intelligence now asks whether those conditions enable the level of performance demanded. Introduce the four execution-enabling capabilities, then have participants score their own function. Use the same scanner for the annual baseline and quarterly recalibration; detailed root-cause diagnosis belongs in Extrapolating.'

CAPS = [
 ('Environment · FIT', 'Operational Readiness', 'Provides a dependable operating setting: facilities accommodate planned activity; essential infrastructure sustains continuity; and technology has the functionality, reliability and capacity to handle strategic demand. This reduces interruptions and protects service or production availability.'),
 ('Systems · SIP', 'Operational Flow', 'Enables work to progress predictably from initiation to completion: standardised processes create consistency, integrated workflows support handovers across functions, and efficient process design removes avoidable steps, duplication and waiting time. This improves throughput and turnaround time.'),
 ('Resources · AIR', 'Delivery Capacity', 'Makes the required scale of delivery achievable: productive assets are available when needed, financial investment supports strategic priorities, and existing resources are deployed where demand is greatest. This prevents capacity shortages and avoidable underutilisation.'),
 ('Governance · PAR', 'Decision Responsiveness', 'Allows organisational action to proceed with clarity and control: policies and procedures guide consistent operations, authority arrangements enable decisions at the right level and time, and risks are identified and managed. This reduces approval bottlenecks while protecting sound decisions.'),
]
IGN_INTRO = 'The ESRG Ignition Point is reached when organisational operating conditions are sufficiently aligned to support the performance demands of the strategy. The four domains make distinct, interdependent contributions to execution:'
PRINCIPLE = 'A strategic commitment can be delivered consistently only when the operating conditions it depends upon can meet its performance demands.'
ILL = 'A customer service function has reliable technology and adequate assets, but disconnected handovers delay case resolution. Its constraint is Operational Flow (SIP). Additional equipment would not directly resolve the delay.'
PROMPT = 'Which of the four capabilities is most critical to your function’s current strategic commitment, and what would happen if it were unable to meet the required demand?'

# standing-rule rewording ("rather than" removed)
PURPOSE = 'Evaluate how effectively the current operating conditions of a business function support its strategic performance commitments. Score actual operating performance from the available evidence of how policies, systems and plans perform in practice.'
SCALE = [('1','Critical constraint','Condition materially prevents required performance.'),
         ('2','Significant gap','Condition regularly disrupts or limits performance.'),
         ('3','Partially effective','Supports basic operations but does not consistently meet strategic demand.'),
         ('4','Effective','Reliably supports current strategic performance requirements.'),
         ('5','Fully aligned','Reliably supports requirements and anticipated strategic demand.')]
SCALE_NOTE = 'Use one consistent 1–5 scale for the annual baseline and each quarterly recalibration. Enter a score for every component at each review point.'
DOMS = [
 ('FIT', 'Operational Readiness', [('Facilities','Our facilities are suitable and functional for our strategic commitments.'),
                                   ('Infrastructure','Essential infrastructure reliably supports our required operations.'),
                                   ('Technology','Our technology supports our performance requirements reliably.')]),
 ('SIP', 'Operational Flow', [('Standardisation','Our core operational processes are clearly defined and consistently applied.'),
                              ('Integration','Our processes and systems connect effectively across functions.'),
                              ('Process Efficiency','Our processes deliver required outputs without unnecessary delays, duplication or waste.')]),
 ('AIR', 'Delivery Capacity', [('Asset Availability','We have access to the productive assets required for delivery.'),
                               ('Investment','Adequate financial provision supports our strategic priorities.'),
                               ('Resource Utilisation','Available assets and financial resources are allocated and utilised effectively.')]),
 ('PAR', 'Decision Responsiveness', [('Policies &amp; Procedures','Our policies and procedures support consistent organisational decisions and operations.'),
                                     ('Authority','Decision rights and approval arrangements enable timely decisions.'),
                                     ('Risk Management','Material organisational risks are identified, assessed, mitigated and monitored.')]),
]
PERIODS = ['Annual','Q1','Q2','Q3','Q4']
HEAD = ['Business function','Functional leader','Strategic commitment / key result']

PROFILE_INTRO = 'Calculate each domain score as the average of its three component scores. The overall ESRG score is the average of the four domain scores. Review individual component scores as well: a strong average can conceal a critical constraint.'
BANDS = 'Score interpretation: 4.0–5.0 Aligned &nbsp;|&nbsp; 3.0–3.9 Improvement required &nbsp;|&nbsp; 2.0–2.9 Significant constraint &nbsp;|&nbsp; 1.0–1.9 Critical constraint.'
# standing-rule rewording ("not a substitute for" removed)
PROFILE_END = 'Annual review establishes the baseline. Quarterly recalibration repeats the same 12 statements using the same scale, allowing leaders to see where operating capability has strengthened, weakened or remained stable. Scores are directional management judgements, read together with the operational evidence behind them.'
ILL_PROFILE = 'A customer service function scores Operational Readiness 4.3, Operational Flow 2.0, Delivery Capacity 4.0 and Decision Responsiveness 3.7. Operational Flow is the lowest-rated execution-enabling capability. Leaders should examine its Standardisation, Integration and Process Efficiency scores, together with supporting evidence, before identifying which operating condition is restricting case resolution.'
QUESTIONS = ['Which component has the lowest score?','What evidence supports that rating?','Has the score changed since the previous review?','Which strategic commitment is most exposed?']
OUTPUT_F = 'A completed Functional ESRG Performance Scanner with annual baseline and quarterly review columns, plus a four-capability performance profile. Carry the material low-scoring or deteriorating conditions into Section 3 — Extrapolating for deeper diagnosis and prioritisation.'
OUTPUT_P = 'Your completed Functional ESRG Performance Scanner with annual baseline and quarterly review columns, plus your four-capability performance profile. Carry the material low-scoring or deteriorating conditions into Section 3 — Extrapolating for deeper diagnosis and prioritisation.'
HOW = ['Enter your business function, its functional leader and the strategic commitment or key result you are scoring against.',
       'Read the scoring guide, then score each of the 12 components from 1 to 5 from the evidence you have.',
       'Enter the annual baseline now. At each quarterly review, return to this page and enter Q1, Q2, Q3 or Q4 on the same scale.',
       'Read your profile in part 2.3 and answer the questions in part 2.4.']
ACT_F = ['Participants enter their business function, its functional leader and the strategic commitment or key result they are scoring against.',
         'Participants score each of the 12 components from 1 to 5 against the scoring guide, from the evidence they have.',
         'Participants enter the annual baseline now and return to the page at each quarterly review to enter Q1 to Q4 on the same scale.',
         'Participants read their profile in part 2.3 and answer the questions in part 2.4.']

def tbl(cls, head, rows):
    return ('<table class="%s"><thead><tr>%s</tr></thead><tbody>\n' % (cls, ''.join('<th>%s</th>' % h for h in head))
            + '\n'.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows) + '\n</tbody></table>')

def scale_tbl():
    return tbl('u10-tbl u10-scale', ['Score','Rating','Meaning'], SCALE)

def scanner(fac):
    """fac=True: teaching view, Annual and Q1-Q4 with dashes. fac=False: the participant's part 4.5 annual baseline (one drop-down per component)."""
    pers = PERIODS if fac else ['Annual baseline']
    head = ['ESRG domain / capability','Element','Functional assessment statement'] + pers
    out = ['<div class="u10-scroll"><table class="u10-tbl u10-scan"%s><thead><tr>%s</tr></thead><tbody>' % ('' if fac else ' style="min-width:560px"', ''.join('<th>%s</th>' % h for h in head))]
    i = 0
    for acr, cap, comps in DOMS:
        for j, (el, st) in enumerate(comps):
            first = '<td rowspan="3" class="u10-dom">%s · %s</td>' % (acr, cap) if j == 0 else ''
            if fac:
                cells = ['<td class="u10-sc">—</td>'] * 5
            else:
                cells = ['<td class="u10-sc"><select class="u10-sel" aria-label="%s · Annual" data-fkey="esrg_scan" data-fidx="%d" onchange="syncFieldDebounced(\'esrg_scan\')"><option value=""></option>%s</select></td>'
                         % (el.replace('&amp;','&'), i, ''.join('<option>%d</option>' % n for n in range(1, 6)) + '<option>N/A</option>')]
            out.append('<tr%s>%s<td class="u10-el">%s</td><td>%s</td>%s</tr>' % (' class="u10-dstart"' if j == 0 else '', first, el, st, ''.join(cells)))
            i += 1
    out.append('</tbody></table></div>')
    return '\n'.join(out)

def profile(fac):
    head = ['Execution-enabling capability'] + PERIODS
    rows = []
    for acr, cap, _ in DOMS:
        rows.append(['%s · %s' % (cap, acr)] + (['—'] * 5 if fac else ['<span class="u10-pv" id="u10p_%s_%d">—</span>' % (acr, k) for k in range(5)]))
    rows.append(['<strong>Overall ESRG score</strong>'] + (['—'] * 5 if fac else ['<span class="u10-pv" id="u10p_ALL_%d">—</span>' % k for k in range(5)]))
    return '<div class="u10-scroll">%s</div>' % tbl('u10-tbl u10-prof', head, rows).replace('<table class="u10-tbl', '<table style="min-width:480px" class="u10-tbl', 1)

def section2(fac):
    """Teaching only on both pages (Carol, 17:10): no entry boxes; the facilitator page adds guidance, prompt and questions."""
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    if fac:
        o.append('\n<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Intelligence</div>\n<p>%s</p>\n</div>\n' % GUIDE)
    b = ['<p>%s</p>' % IGN_INTRO,
         '<div class="u10-scroll">%s</div>' % tbl('u10-tbl u10-cap', ['ESRG domain','Execution-enabling capability','What it makes possible'], CAPS).replace('<table class="u10-tbl', '<table style="min-width:620px" class="u10-tbl', 1),
         '<div class="hbox"><p><strong>Ignition principle:</strong> %s</p></div>' % PRINCIPLE,
         '<p><strong>Illustration:</strong> %s</p>' % ILL]
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator prompt</div>\n<p>%s</p>\n</div>' % PROMPT)
    else:
        b.append('<div class="p-reflect">Reflect: %s</div>' % PROMPT)
    o.append(acc('2.1 &mdash; The ESRG Ignition Point', '\n'.join(b), True))
    b = ['<p><strong>Purpose:</strong> %s</p>' % PURPOSE,
         '<table class="u10-tbl u10-headf"><tbody>%s</tbody></table>' % ''.join('<tr><td>%s</td><td>____________________</td></tr>' % h for h in HEAD),
         '<div class="u10-sub">Scoring guide</div>', scale_tbl(), '<p>%s</p>' % SCALE_NOTE,
         '<div class="u10-sub">ESRG Scanner &mdash; Annual Baseline and Quarterly Recalibration</div>', scanner(True)]
    o.append(acc('2.2 &mdash; Functional ESRG Performance Scanner', '\n'.join(b), False))
    b = ['<p>%s</p>' % PROFILE_INTRO, profile(True), '<p class="u10-bands">%s</p>' % BANDS, '<p>%s</p>' % PROFILE_END]
    o.append(acc('2.3 &mdash; Reading the ESRG Performance Profile', '\n'.join(b), False))
    b = ['<p><strong>Illustrative profile:</strong> %s</p>' % ILL_PROFILE]
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator questions</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % q for q in QUESTIONS))
        b.append('<div class="hbox"><p><strong>Section output:</strong> %s</p></div>' % OUTPUT_F)
    else:
        b.append('<div class="p-reflect">Reflect: %s</div>' % ' '.join(QUESTIONS))
    o.append(acc('2.4 &mdash; Making Sense of the Results', '\n'.join(b), False))
    return '\n'.join(o) + '\n'

def css(fac):
    c, bg, bd = ('var(--gold)', '#1a2a1e', 'rgba(201,168,76,.2)') if fac else ('var(--teall)', '#162e28', 'rgba(26,122,106,.2)')
    tint = 'rgba(201,168,76,.06)' if fac else 'rgba(26,122,106,.06)'
    return ('.u10-tbl{width:100%%;border-collapse:collapse;margin:14px 0;font-size:13px;}\n'
            '.u10-tbl th{background:%(bg)s;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%(c)s;padding:10px 12px;text-align:left;border-bottom:1px solid %(bd)s;}\n'
            '.u10-tbl td{padding:9px 12px;border-bottom:1px solid rgba(255,255,255,.05);color:rgba(255,255,255,.68);line-height:1.6;vertical-align:top;}\n'
            '.u10-tbl td:first-child{color:rgba(255,255,255,.88);font-weight:600;}\n'
            '.u10-cap td:nth-child(2){color:%(c)s;font-weight:700;white-space:nowrap;}\n'
            '.u10-scale td:first-child{color:%(c)s;font-weight:700;width:8%%;}\n.u10-scale td:nth-child(2){color:rgba(255,255,255,.85);width:26%%;}\n'
            '.u10-scroll{overflow-x:auto;margin:14px 0;}\n.u10-scroll .u10-tbl{margin:0;min-width:760px;}\n'
            '.u10-scan td.u10-dom{color:%(c)s;font-weight:700;background:%(tint)s;width:15%%;}\n.u10-scan td.u10-el{color:rgba(255,255,255,.88);font-weight:600;width:14%%;}\n'
            '.u10-scan tr.u10-dstart td{border-top:1px solid %(bd)s;}\n.u10-scan th:nth-child(n+4),.u10-sc{text-align:center;width:7%%;}\n'
            '.u10-sel{background:#091612;border:1px solid rgba(255,255,255,.15);border-radius:2px;color:#fff;font-size:13px;padding:4px 2px;width:54px;cursor:pointer;}\n'
            '.u10-prof td:not(:first-child),.u10-prof th:not(:first-child){text-align:center;}\n'
            '.u10-pv{font-weight:700;}\n.u10-pv.b4{color:#5ecba1;}.u10-pv.b3{color:#e8c96a;}.u10-pv.b2{color:#e8955a;}.u10-pv.b1{color:#e06666;}\n'
            '.u10-bands{font-size:13px!important;}\n'
            '.u10-sub{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%(c)s;margin:20px 0 4px;}\n'
            '.u10-how{background:%(tint)s;border:1px solid %(bd)s;border-left:3px solid %(c)s;border-radius:0 3px 3px 0;padding:14px 18px 10px;margin:0 0 16px;}\n'
            '.u10-how-h{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%(c)s;margin:0 0 6px;}\n'
            '.u10-how ol,.u10-activity ol{margin:6px 0 8px;padding-left:20px;}\n.u10-how li,.u10-activity li{font-size:13px;color:rgba(255,255,255,.8);line-height:1.75;margin-bottom:4px;}\n'
            '.u10-headf td:first-child{width:34%%;}\n') % dict(c=c, bg=bg, bd=bd, tint=tint)

JS = r'''
/* Unit 10 · part 2.2 Functional ESRG Performance Scanner: entries save under esrg_scan_head and esrg_scan; part 2.3 profile averages the scores. */
FIELD_SPECS.esrg_scan_head=[{l:"Business function",k:"text"},{l:"Functional leader",k:"text"},{l:"Strategic commitment / key result",k:"text"}];
(function(){var EL=["Facilities","Infrastructure","Technology","Standardisation","Integration","Process Efficiency","Asset Availability","Investment","Resource Utilisation","Policies & Procedures","Authority","Risk Management"],PER=["Annual","Q1","Q2","Q3","Q4"],s=[];
EL.forEach(function(e){PER.forEach(function(p){s.push({l:e+" · "+p,k:"select"});});});FIELD_SPECS.esrg_scan=s;})();
function u10Profile(){
  var DOM=["FIT","SIP","AIR","PAR"];
  function v(i,k){var el=document.querySelector('[data-fkey="esrg_scan"][data-fidx="'+(i*5+k)+'"]');var n=el?parseInt(el.value,10):NaN;return isNaN(n)?null:n;}
  function show(id,x){var el=document.getElementById(id);if(!el)return;if(x==null){el.textContent="—";el.className="u10-pv";return;}
    el.textContent=x.toFixed(1);el.className="u10-pv "+(x>=4?"b4":x>=3?"b3":x>=2?"b2":"b1");}
  for(var k=0;k<5;k++){var doms=[];
    DOM.forEach(function(d,di){var a=v(di*3,k),b=v(di*3+1,k),c=v(di*3+2,k);var avg=(a!=null&&b!=null&&c!=null)?(a+b+c)/3:null;doms.push(avg);show("u10p_"+d+"_"+k,avg);});
    var all=doms.every(function(x){return x!=null;})?(doms[0]+doms[1]+doms[2]+doms[3])/4:null;show("u10p_ALL_"+k,all);}
}
'''
