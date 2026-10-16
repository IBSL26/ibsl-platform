# -*- coding: utf-8 -*-
"""Unit 9 · the two performance views (16 October 2026) — page text for build_u09pv.py.
Source: Carol's locks in Claude outputs\\Review files\\Unit 9\\Unit 9 two views - locked amendments.md and her four texts
(Unit 9 part 1.2 - Seven Clog Map; Section 3 - CXO Performance Clogs; Section 4 - Integration R3 and levers;
Section 5 - Strategic Unclogging Clinic), with the wording edits recorded there. The seven clog cards and the ten
executive role cards come from u9pv_text.json (gen_text.py)."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
NL = '\r\n'
T = json.load(open(os.path.join(HERE, 'u9pv_text.json'), encoding='utf-8'))
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'

def ent(s):
    for a, b in (('’', '&rsquo;'), ('‘', '&lsquo;'), ('“', '&ldquo;'), ('”', '&rdquo;'), ('—', '&mdash;'), ('–', '&ndash;'), ('→', '&rarr;'), ('®', '&reg;')):
        s = s.replace(a, b)
    return s
def esc_ph(s): return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('\n', '&#10;')
def P(*ps): return NL.join('<p>%s</p>' % ent(p) for p in ps)
def acc(title, meta, body, after='', open_=False):
    return ('<div class="acc%s">' % (' open' if open_ else '') + NL +
            '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">%s</div></div>%s</div>' % (ent(title), ent(meta), ARR) + NL +
            '<div class="acc-b"><div class="cb">' + NL + body + NL + '</div>' + ((NL + after + NL) if after else '') + '</div></div>')
def guide(label, *ps):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>' % ent(label) + NL + NL.join(ent(p) if p.startswith('<') else '<p>%s</p>' % ent(p) for p in ps) + NL + '</div>'
def activity(text):
    return '<div class="fac-note-full u9-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + NL + '<p>%s</p>' % ent(text) + NL + '</div>'
def hero(label, title, lead):
    return '<div class="mod-hero"><div class="mod-hero-label">%s</div><h2>%s</h2><p>%s</p></div>' % (label, ent(title), ent(lead))
def slo(a, b):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>%s</li><li>%s</li></ul></div>' % (ent(a), ent(b))
def sub(t): return '<div class="u9-sub">%s</div>' % ent(t)
FOLD, END = '\x00FOLD:', '\x00END'
def fsub(t): return FOLD + t
def fold(items):
    """Each fsub(title) opens a collapsible sub-part (closed) holding the items after it, up to the next fsub, an END or the end."""
    out, cur = [], None
    for x in items:
        if x.startswith(FOLD) or x == END:
            if cur: out.append('<details class="u9-det"><summary class="u9-sub">%s</summary><div class="u9-det-b">' % ent(cur[0]) + NL + NL.join(cur[1]) + NL + '</div></details>')
            cur = [x[len(FOLD):], []] if x.startswith(FOLD) else None
        elif cur: cur[1].append(x)
        else: out.append(x)
    if cur: out.append('<details class="u9-det"><summary class="u9-sub">%s</summary><div class="u9-det-b">' % ent(cur[0]) + NL + NL.join(cur[1]) + NL + '</div></details>')
    return out
def hc(a_lab, a_txt, b_lab, b_txt, a_cls='u8v-hu', b_cls='u8v-or'):
    """Two-side cards: blue top border for the human / people side (u8v-hu), green for the organisation side (u8v-or)."""
    return ('<div class="u8v-hc" onclick="event.stopPropagation()"><div class="u8v-c %s"><div class="u8v-n">%s</div><p>%s</p></div>'
            '<div class="u8v-c %s"><div class="u8v-n">%s</div><p>%s</p></div></div>') % (a_cls, ent(a_lab), ent(a_txt), b_cls, ent(b_lab), ent(b_txt))
def table(head, rows, cls='u9-tbl'):
    h = '<div class="u9-tw"><table class="%s"><thead><tr>%s</tr></thead><tbody>' % (cls, ''.join('<th>%s</th>' % ent(x) for x in head))
    return h + ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % ent(c) for c in r) for r in rows) + '</tbody></table></div>'
def ol(items, cls='u9-ol'): return '<ol class="%s">%s</ol>' % (cls, ''.join('<li>%s</li>' % ent(x) for x in items))
def ul(items, cls='u9-ul'): return '<ul class="%s">%s</ul>' % (cls, ''.join('<li>%s</li>' % ent(x) for x in items))
PROMPT = '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">%s</p>'
CLOGS = ['Structural Misfit', 'Capability Gaps', 'Decision Bottlenecks', 'Misaligned Metrics & Incentives', 'Cultural Resistance', 'Technology / Infrastructure Lag', 'Leadership Avoidance']
LEVERS = ['01 · Standardise', '02 · Streamline', '03 · Clarify', '04 · Upgrade', '05 · Reinforce', '06 · Realign', '07 · Rebuild Trust']
ABCV_CLS = {'Arena': 'abcv-arena', 'Boundaries': 'abcv-boundaries', 'Competition': 'abcv-competition', 'Value Proposition': 'abcv-value', 'Arena + Boundaries': 'abcv-mixed'}

# ═══ Section learning outcomes (Carol's texts) ═══
SLO = {
    3: ('Reveal how executive decisions and practices can create or reinforce performance clogs.', 'Examine how decisions within one executive function affect contributions and performance across the organisation.'),
    4: ('Mobilise leaders across functions to restore performance momentum together.', 'Establish a shared leadership rhythm for surfacing and resolving friction across people and organisational performance.'),
    5: ('Classify an original organisational challenge using the Seven Performance Clogs and select an appropriate established Unclogging Lever.', 'Develop a collective executive response through Review–Realign–Restore, addressing people performance and organisational performance.'),
}

# ═══ Facilitator Guide (overview tab) — locked 15 Oct 20:24 and 16 Oct 09:58 ═══
REFRAME_OLD = '<p>The central reframe is powerful and must land clearly: <strong>a clog is a signal.</strong> It indicates where the organisation&rsquo;s current operating system has not yet adapted to the new strategic direction. Leaders who understand this stop asking &ldquo;Why are we failing?&rdquo; and start asking &ldquo;Where is the system not yet designed to carry the strategy?&rdquo;</p>'
REFRAME_NEW = ent('<p><strong>A clog is a signal.</strong> It indicates where the organisation has not yet adapted to the new strategic direction, in the performance of individuals and teams and in the organisational conditions that support the execution of their tasks. Leaders who understand this stop asking “Why are we failing?” and start asking “Where are our people and our organisational conditions not yet ready to carry the strategy?”</p>' + NL +
                  '<p>A clog shows from two sides. From the human side, individuals and teams stall on their KPIs: decisions wait, effort pulls in different directions, and tasks are completed while the Key Result does not move. From the organisation side, the organisational conditions do not support the execution of the individuals’ tasks. The diagnosis of every clog examines both sides before a lever is selected.</p>')
CLINIC_OLD = '<p>The Clog Clinic in Application is the centrepiece: each group diagnoses the friction on its own Key Results and builds its Enterprise Unclogging Agenda. The diagnostic triads of part 4.4 prepare it, on each participant&rsquo;s own stalled KPI. The quality of the diagnostic conversation is the measure of this unit.</p>'
CLINIC_NEW = ent('<p>The Strategic Unclogging Clinic in Application is the centrepiece: each group returns to an original work-based challenge, identifies the clog, selects the lever and applies Review–Realign–Restore within its Capstone organisation. The quality of the diagnostic conversation is the measure of this unit.</p>')
KFQ_ADD = ent('<li><em>“Where a KPI has stalled, what is happening in the individuals’ performance, and do the organisational conditions support the execution of their tasks?”</em></li>' + NL +
              '<li><em>“Which leader is responsible for the organisational condition behind this clog, and when was it last reviewed?”</em></li>')
TONE_ADD = ent('<p><strong>Teach both sides of every clog.</strong> Leaders tend to read a stalled KPI as a people problem, because individuals’ performance is reviewed every month and the organisational conditions seldom are. For each clog, take them to the second question: do the organisational conditions support the execution of the individuals’ tasks?</p>')

# ═══ Section 1 · Awareness ═══
GUIDE_S1 = ['<ul class="u9-ul">' +
            '<li>Open with the scenario: the strategy is clear, objectives are defined, performance expectations are in motion, and then the gears begin grinding. Teach the shift from “failure of strategy” to “failure of flow”.</li>'
            '<li>1.1 · Teach what a Strategic Clog is and the four ABCV elements it distorts. Then teach where clogs form, from the human side and the organisation side.</li>'
            '<li>1.2 · Teach the two dimensions of performance, then the seven clogs one card at a time, the ABCV connection, the three lines of sight and the worked example. Participants complete the self-assessment in their own file.</li></ul>']
OPEN_11 = {
    'p': ('<p>At this point, your strategy is clear. Your objectives are defined. Your performance expectations are in motion. Then the gears begin grinding.</p>',
          '<p>At this point, your strategy is clear. Your objectives are defined. Your performance expectations are in motion. Each Key Result has been translated into KPIs that individuals and teams deliver. Leaders have agreed the organisational conditions that support the execution of those individuals’ tasks. A rhythm of review tracks the progress of both.</p>'),
    'f': ('<p>At this point, the strategy is clear. Objectives are defined. Performance expectations are in motion. Then the gears begin grinding.</p>',
          '<p>At this point, the strategy is clear. Objectives are defined. Performance expectations are in motion. Each Key Result has been translated into KPIs that individuals and teams deliver. Leaders have agreed the organisational conditions that support the execution of those individuals’ tasks. A rhythm of review tracks the progress of both.</p>'),
}
OPEN_11_TAIL = ('<p>Then the gears begin grinding.</p>' + NL +
                '<p>Progress slows on a Key Result that everyone supports. Reviews record effort, explanations and revised dates, and the result does not move. The plan still stands. What holds it back is a Strategic Clog.</p>')
WHERE_FORM = (sub('Where clogs form') + NL +
              P('Strategic intent reaches the Key Result through the tasks that individuals and teams execute. Those tasks depend on the organisational conditions around them. These conditions are the Environment, Systems, Resources and Governance (ESRG): the environment people work in, the systems they rely on, the resources they are given and the governance that guides decisions. A clog can form in either, and it usually acts on both.') + NL +
              hc('From the human side', 'A clog shows in the performance of individuals and teams. Decisions wait, effort pulls in different directions, and tasks are completed while the KPI holds still. This is the side the review sees first, because the individuals’ numbers are reviewed.',
                 'From the organisation side', 'A clog shows when the organisational conditions no longer support the execution of the individuals’ tasks, as the strategy places new weight on them. This side seldom carries a number of its own, so it stays unseen until leaders ask for it.'))
REF1_ADD = ' Which organisational condition did the individuals’ tasks depend on, and did it support their execution?'
ACT_11 = 'Participants write a reflection in their own file: a strategy initiative that stalled in their organisation, the blockage behind it, whether it could have been named earlier, and the organisational condition the individuals’ tasks depended on.'
REF2_PROMPT = 'Rate each clog in your current strategy portfolio (1 = absent, 5 = active). Then name the clog most active in your organisation, and the organisational condition it sits in.'
REF2_FIELD = 'The clog most active in my organisation, and the organisational condition it sits in'
ACT_12 = 'Participants write a reflection in their own file: a rating of each of the seven clogs in their current strategy portfolio, from 1 (absent) to 5 (active), and the clog most active in their organisation, with the organisational condition it sits in.'
T12, M12 = '1.2 — The 7-Clog Diagnostic Map', 'ABCV-aligned · Select each clog to explore'

def clog_card(c):
    lst = lambda lab, xs: '<div class="u9-lst"><div class="clog-rl">%s</div>%s</div>' % (lab, ul(xs))
    return ('<div class="clog-card" onclick="toggleClog(this)">' + NL +
            '  <div class="clog-head"><div class="clog-meta"><div class="clog-num">Clog %s</div><div class="clog-name">%s</div></div><span class="abcv-badge %s">%s</span><div class="clog-arr">&#9660;</div></div>' % (c['num'], c['name'], ABCV_CLS[c['abcv']], c['abcv']) + NL +
            '  <div class="clog-body" onclick="event.stopPropagation()">' + NL +
            '    ' + hc('Organisational performance · System reality', c['org'], 'People performance · Contribution reality', c['ppl'], 'u8v-or', 'u8v-hu') + NL +
            '    <div class="u9-cols">%s%s</div>' % (lst('Observable performance patterns', c['patterns']), lst('Early warning signals', c['warnings'])) + NL +
            '    <div class="clog-impact"><strong>Strategic impact:</strong> %s</div>' % c['impact'] + NL +
            '    <div class="p-reflect"><strong>Diagnostic question:</strong> %s</div>' % c['question'] + NL +
            '    <div class="u9-ex"><div class="u9-ex-h">Worked example</div><p>%s</p></div>' % c['example'] + NL +
            '  </div>' + NL + '</div>')

def map12():
    out = [fsub('Understanding Where Performance Becomes Constrained'),
           P('Strategy depends on the organisation’s ability to convert its strategic intent into coordinated contributions and measurable results. This requires two connected dimensions of performance:'),
           hc('Organisational performance', 'The enterprise’s ability to create, deliver and sustain value. It reflects how effectively structures, processes, resources, capabilities, governance and operating systems work together to produce strategic outcomes.',
              'People performance', 'How effectively individuals and teams understand expectations, make decisions, exercise judgement, apply capabilities, collaborate and deliver their contributions to organisational results.', 'u8v-or', 'u8v-hu'),
           P('Both dimensions operate within the same enterprise system. When organisational conditions are weak, even capable and committed people may struggle to perform. They experience delays, conflicting priorities, unclear responsibilities, resource shortages and barriers beyond their authority to resolve.',
             'When people performance is weak, the organisation may have adequate resources and well-designed processes but still experience poor judgement, inconsistent behaviours, weak collaboration, limited ownership and unreliable delivery.',
             'These conditions often reinforce one another. For example, unclear decision rights create hesitation among managers. Repeated hesitation then encourages senior leaders to centralise decisions further, increasing the original bottleneck.',
             'The 7-Clog Diagnostic Map identifies seven recurring conditions that constrain the organisation’s capacity to deliver its strategy. The diagnostic examines both the condition of the organisational system and the performance patterns emerging within it.'),
           fsub('The Seven Performance Clogs'),
           P('Select each clog to examine its organisational conditions, effects on people, observable patterns, early warnings and strategic consequences.'),
           '<div class="clog-stack">' + NL + NL.join(clog_card(c) for c in T['clogs']) + NL + '</div>',
           fsub('1.2.1 — The ABCV Diagnostic Connection'),
           P('The ABCV framework helps locate the strategic dimension being distorted by a performance clog.'),
           table(['ABCV element', 'Strategic concern', 'Related clogs'], [
               ['<span class="abcv-badge abcv-arena">Arena</span>', 'Does the organisation have the capability and focus to operate successfully in its chosen strategic space?', 'Capability Gaps; Leadership Avoidance'],
               ['<span class="abcv-badge abcv-boundaries">Boundaries</span>', 'Do organisational arrangements, decision rights and governance enable disciplined, coordinated delivery?', 'Structural Misfit; Decision Bottlenecks; Leadership Avoidance'],
               ['<span class="abcv-badge abcv-competition">Competition</span>', 'Can the enterprise respond and perform at the speed, reliability and standard required in its competitive environment?', 'Technology / Infrastructure Lag'],
               ['<span class="abcv-badge abcv-value">Value Proposition</span>', 'Do organisational behaviours, measures and contributions produce the value promised to stakeholders?', 'Misaligned Metrics &amp; Incentives; Cultural Resistance']]),
           P('These are primary diagnostic associations. A clog may affect several ABCV elements simultaneously. For example, inadequate technology may primarily affect competitive responsiveness but also prevent the organisation from delivering its value proposition. Similarly, a structural misfit may originate in organisational boundaries while undermining the chosen strategic arena.',
             'ABCV helps identify where strategic intent is being distorted; the 7-Clog Diagnostic Map helps explain the conditions producing that distortion.'),
           fsub('1.2.2 — The Three Performance Lines of Sight from the Seven Clogs'),
           P('The central discipline is to distinguish three levels of performance evidence. Each line of sight reveals a different part of the performance problem and helps leaders move from symptoms to causes.'),
           '<div class="u9-los">' + ''.join('<div class="u9-los-c"><div class="u9-los-n">%s</div><div class="u9-los-t">%s</div><p>%s</p></div>' % (n, ent(a), ent(b)) for n, a, b in (
               ('1', 'Performance outcome', 'What result is falling short? Establish the intended strategic outcome, the actual result and the size or nature of the gap.'),
               ('2', 'Performance behaviour', 'What are people or teams doing, or unable to do, that contributes to the gap? Observe specific decisions, actions, omissions, collaboration patterns and delivery practices.'),
               ('3', 'Performance condition', 'What organisational arrangements, capabilities, incentives or leadership practices are causing or reinforcing that behaviour? Test the seven clogs to explain why the pattern persists.'))) + '</div>',
           P('This distinction helps leaders avoid treating every disappointing result as an individual performance failure. It also keeps people accountable for actions within their control while recognising the organisation’s responsibility for enabling conditions.',
             'A single performance outcome can reflect several interacting clogs. The following example traces the three lines of sight before identifying the organisational conditions that require attention.'),
           fsub('1.2.3 — Worked Diagnostic Example: Improving Customer Service'),
           '<div class="u9-okr"><p><strong>Enterprise Objective.</strong> Deliver a reliable and responsive customer service experience.</p><p><strong>Enterprise Key Result.</strong> Increase customer enquiries resolved within 48 hours from 65% to 90% by year-end.</p><p class="u9-small">Performance figures are illustrative.</p></div>',
           '<div class="u9-step"><div class="u9-step-h">Line of Sight 1 &mdash; Performance Outcome</div>' + P('Only 65% of customer enquiries are resolved within 48 hours against a target of 90%. The enterprise is falling short of its intended customer responsiveness and service reliability.') + '</div>',
           '<div class="u9-step"><div class="u9-step-h">Line of Sight 2 &mdash; Performance Behaviour</div>' + P('Service agents process enquiries and escalate cases requiring other departments. Cases are frequently transferred without end-to-end ownership, managers wait for approval on routine refunds, and staff spend their time requesting updates while customer problems wait. Employees may be achieving their activity targets while the collective resolution outcome remains weak.') + '</div>',
           '<div class="u9-step"><div class="u9-step-h">Line of Sight 3 &mdash; Performance Condition</div>' + P('The diagnostic identifies the organisational conditions that help explain the behaviour:') +
           table(['Evidence', 'Clog', 'How it constrains performance'], [
               ['40% of delayed cases require another department.', 'Structural Misfit', 'Fragmented ownership and weak cross-functional handoffs delay resolution.'],
               ['Routine refunds require senior-management approval.', 'Decision Bottlenecks', 'People closest to the enquiry lack sufficient authority to resolve it.'],
               ['Employee scorecards emphasise enquiries processed.', 'Misaligned Metrics &amp; Incentives', 'Volume is reinforced more strongly than complete and timely resolution.'],
               ['Employees cannot track cases after escalation.', 'Technology / Infrastructure Lag', 'Fragmented information prevents timely follow-through.']]) + '</div>',
           '<div class="u9-int">' +
           '<div class="u9-int-c u9-or"><div class="u9-int-h">Organisational performance interpretation</div><p>%s</p></div>' % ent('The coordination processes, decision rights, measures and information systems are not sufficiently aligned to the customer-resolution outcome. These conditions create recurring delays across the service chain.') +
           '<div class="u9-int-c u9-hu"><div class="u9-int-h">People performance interpretation</div><p>%s</p></div>' % ent('Customer service employees may complete assigned tasks but still lack the authority, information and cross-functional support needed to resolve cases. Any individual capability or behavioural gaps must be assessed against these conditions and the standards within each person’s control.') +
           '<div class="u9-int-c u9-go"><div class="u9-int-h">Strategic interpretation</div><p>%s</p></div>' % ent('The customer value proposition promises responsive service, but operating arrangements do not consistently enable its delivery. The principal ABCV distortion concerns the Value Proposition, with contributing constraints in Boundaries and Competition.') +
           '<div class="u9-int-c"><div class="u9-int-h">Required management response</div><p>%s</p></div>' % ent('Clarify end-to-end resolution ownership, adjust routine decision authority, align measures to resolution outcomes and improve case visibility across departments. Provide coaching or accountability interventions where evidence confirms individual capability or behavioural gaps.') +
           '</div>',
           END,
           '<div class="hbox" style="margin-top:16px;"><div class="u9-ex-h">Closing Diagnostic Principle</div>' + P('Performance is produced through people operating within an organisational system. A sound diagnosis examines the result, the behaviours shaping contributions and the organisational conditions that enable or constrain them.',
             'The 7-Clog Diagnostic Map helps leaders identify where these relationships have become misaligned, which ABCV elements are affected and what must change to restore performance.') + '</div>']
    return NL.join(fold(out))

# ═══ Section 2 · Intelligence — guidance question brought into line with the Section 1 lock ═══
S2_Q_OLD = '<em>&ldquo;Where is the system not yet designed to carry the strategy?&rdquo;</em>'
S2_Q_NEW = '<em>&ldquo;Where are our people and our organisational conditions not yet ready to carry the strategy?&rdquo;</em>'

# ═══ Section 3 · Extrapolating (Carol, locked 16 Oct 12:56) ═══
S3_TITLE = 'Where Do Executive Decisions and Practices Contribute to Performance Clogs?'
S3_LEAD = 'Examining how decisions and management practices within executive functions influence people performance, organisational conditions and strategic results.'
GUIDE_S3 = ['Connect this section to the seven clogs and Three Performance Lines of Sight introduced in Section 1 (part 1.2.2). Explain that every executive function shapes the conditions in which other teams work. Decisions in finance, operations, people management, technology and commercial functions can affect performance beyond their own portfolios.',
            'Use the CXO cards to illustrate a decision or practice, the organisational result affected, how people respond and the clog that can follow. Begin with participants’ own roles, then invite them to explore two closely connected functions. Participants use the final reflection to examine a decision or practice from their own organisation.']
T31, M31 = '3.1 — The CXO Performance Clog Contributors', 'Select each executive role to explore'
S31_INTRO = ('Executive roles carry responsibility for different parts of the organisation’s operating system. Through their decisions, executives determine how resources are allocated, work is organised, people are managed, performance is measured and risks are controlled. These decisions shape the conditions in which individuals and teams contribute to strategic results.',
             'A performance clog can form when a decision or management practice in one executive function creates difficulties for people working elsewhere. Select an executive role to examine a realistic decision and its consequences through the Three Performance Lines of Sight.')
def roles(v):
    tabs = '<div class="u9-roles">' + ''.join('<button type="button" class="u9-role-b%s" onclick="u9Role(this,%d)"><b>%s</b><span>%s</span></button>' % (' on' if i == 0 else '', i, r['role'], r['remit']) for i, r in enumerate(T['roles'])) + '</div>'
    qlab = 'Your question' if v == 'p' else 'Question for participants'
    panels = ''.join(('<div class="u9-role%s">' % (' on' if i == 0 else '')) +
                     '<div class="u9-role-h">%s &middot; %s</div>' % (r['role'], r['remit']) +
                     '<div class="u9-dec"><div class="clog-rl">Executive decision or practice</div><p>%s</p></div>' % r['decision'] +
                     '<div class="u9-step"><div class="u9-step-h">Line of Sight 1 &mdash; Performance Outcome</div><p>%s</p></div>' % r['los1'] +
                     '<div class="u9-step"><div class="u9-step-h">Line of Sight 2 &mdash; Performance Behaviour</div><p>%s</p></div>' % r['los2'] +
                     '<div class="u9-step"><div class="u9-step-h">Line of Sight 3 &mdash; Performance Condition</div><p><strong>%s.</strong> %s</p></div>' % (r['clog'], r['los3']) +
                     '<div class="p-reflect"><strong>%s:</strong> %s</div>' % (qlab, r['question']) + '</div>' for i, r in enumerate(T['roles']))
    return tabs + NL + '<div class="u9-role-panels">' + panels + '</div>'
REF7 = ('ref7', 'My Executive Contribution to Performance',
        'Think about one decision, policy or management practice within your own executive function that may be affecting the performance of another team or function. Examine its consequences through the Three Performance Lines of Sight.',
        [(None, 'My executive function', 'Identify your executive function.', None),
         (None, 'Decision or management practice', 'What one decision, policy or practice within your function may be affecting another function?', None),
         (None, '1 · Performance Outcome', 'Which organisational result is affected?', None),
         (None, '2 · Performance Behaviour', 'What are people doing, delaying or unable to do because of this decision?', None),
         (None, '3 · Performance Condition', 'Which of the seven clogs does the decision or practice create or reinforce?', None)])
HOW_REF7 = ['Read the card for your own executive role, then the cards for two closely connected functions.',
            'Choose one decision, policy or management practice within your own function that may be affecting another team or function.',
            'Trace it through the Three Performance Lines of Sight and name the clog it creates or reinforces.',
            'This is personal work. Your answers save as you type and go to your facilitator when you select Submit to Facilitator.']
ACT_31 = 'Participants write a reflection in their own file, as Portfolio work: one decision, policy or management practice within their own executive function that may be affecting another team or function, traced through the Three Performance Lines of Sight to the clog it creates or reinforces.'
S3_CLOSE = ('Executive decisions shape the conditions in which people and teams perform. The Three Performance Lines of Sight help leaders recognise how decisions within their own functions may influence results elsewhere in the organisation.',
            'Section 4 — Integration will focus on how executive leaders work collectively to remove performance clogs and restore strategic coherence and performance momentum.')

# ═══ Section 4 · Integration (Carol, locked 16 Oct 13:45) ═══
S4_TITLE = 'Cross Leadership Clog Ownership'
S4_LEAD = 'Building the collective discipline of normalising the unclog, where detecting and clearing performance friction becomes a shared leadership habit.'
GUIDE_S4 = ['The central shift is from “my clog” to “our clog”. A performance blockage may surface in one function while the organisational condition sustaining it sits in another. The leadership team, acting as the collective intelligence for execution discipline, must own the diagnostic conversation and response together.',
            'Emphasise the “see something, say something” principle: surfacing friction in another executive domain can feel politically risky, yet early identification is an act of shared leadership stewardship. Use Review–Realign–Restore as the established S2R® discipline for acting on what leaders surface. REALIGN must explicitly consider the implications for both people performance and organisational performance.',
            'Work through the manufacturing example and then guide participants to apply the same process to their Capstone organisation. Keep the Seven Unclogging Levers as the intervention mechanism within RESTORE.']
LEVER_ROWS = [['01 — Standardise', 'Ensure Consistency', 'Structural Misfit; Misaligned Metrics &amp; Incentives; Technology / Infrastructure Lag'],
              ['02 — Streamline', 'Increase Speed', 'Decision Bottlenecks; Structural Misfit'],
              ['03 — Clarify', 'Eliminate Confusion', 'Decision Bottlenecks; Structural Misfit; Leadership Avoidance'],
              ['04 — Upgrade', 'Remove Bottlenecks', 'Technology / Infrastructure Lag; Capability Gaps'],
              ['05 — Reinforce', 'Strengthen Behaviour', 'Capability Gaps; Cultural Resistance'],
              ['06 — Realign', 'Focus on Results', 'Misaligned Metrics &amp; Incentives'],
              ['07 — Rebuild Trust', 'Restore Credibility', 'Cultural Resistance; Leadership Avoidance']]
def s4_parts(v):
    a = []
    a.append(acc('4.1 — Normalising the Unclog: From Crisis to Habit', 'The collective discipline', NL.join([
        P('Performance friction is a normal feature of organisational life. Strategic priorities shift, resources become constrained, dependencies increase and existing operating arrangements may no longer support the required results. Without a shared leadership discipline, these problems are discussed informally, addressed within silos or left unresolved across successive performance reviews.',
          'Normalising the unclog means making the early detection and removal of performance constraints part of how the executive team operates. Leaders raise concerns through evidence, examine the contributing conditions together and agree on an accountable response. Surfacing friction is treated as a contribution to organisational learning and performance, including when the condition involves another executive portfolio.'),
        P('The leadership team follows a consistent path: REVIEW the performance evidence and confirm the clog; REALIGN executive ownership and the changes required across people and organisational performance; RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery.'),
        '<div class="hbox"><p>%s</p></div>' % ent('<strong>Collective leadership principle.</strong> Every executive is responsible for making emerging friction visible. The leaders who control the contributing conditions must act together to remove it, with clear individual ownership for each agreed commitment.')]), open_=True))
    a.append(acc('4.2 — REVIEW: Establish the Performance Reality', 'Review', NL.join([
        P('REVIEW establishes a shared, evidence-based understanding of the result falling short and the organisational condition contributing to it. Leaders use the Three Performance Lines of Sight to distinguish the outcome from the behaviours observed and the conditions causing or reinforcing them.'),
        ol(['<strong>Performance Outcome</strong> — Confirm the Key Result or KPI that is underperforming and establish the actual gap.',
            '<strong>Performance Behaviour</strong> — Identify what individuals or teams are doing, delaying or unable to do that contributes to the gap.',
            '<strong>Performance Condition</strong> — Test the evidence against the Seven Clogs and identify the condition sustaining the behaviour.']),
        P('The review conversation must allow leaders to surface performance friction across functional boundaries. Concerns should be examined through observable evidence, including where the condition may sit within another executive portfolio.'),
        '<div class="u9-done">%s</div>' % ent('<strong>REVIEW is complete when</strong> the executive team agrees on the performance gap, the supporting evidence and the clog requiring intervention.')])))
    a.append(acc('4.3 — REALIGN: Establish Collective Executive Ownership', 'Realign', NL.join([
        P('Once a performance clog has been confirmed, the executive team must determine which organisational condition needs to change and which leaders have the authority and responsibility to act. A clog may be experienced in one function but sustained by a decision or operating arrangement in another.'),
        sub('Three Leadership Decisions'),
        ol(['<strong>What must change?</strong> Identify the specific organisational arrangement, practice or decision sustaining the clog.',
            '<strong>Who must act together?</strong> Appoint one coordinating executive owner and name the contributing executives needed to resolve the condition.',
            '<strong>What must be agreed?</strong> Establish the decisions, responsibilities, resources and timelines required for the intervention.']),
        P('Before finalising the response, leaders consider the implications for both dimensions of performance:'),
        hc('People performance', 'What must change in expectations, authority, capabilities, behaviours or support so individuals and teams can deliver their contributions?',
           'Organisational performance', 'What must change in structures, processes, systems, resources, decision rights or governance so the enterprise can produce the intended result?'),
        P('The agreed intervention should address the confirmed organisational condition while enabling the people responsible for delivery to perform effectively.',
          'Every executive has a responsibility to recognise and surface performance friction. Collective ownership is supported by clear individual accountability: one leader coordinates the resolution, while other executives remain accountable for their agreed contributions.'),
        '<div class="u9-done">%s</div>' % ent('<strong>REALIGN is complete when</strong> the relevant leaders have agreed what must change, who will act and what each executive must deliver.')])))
    a.append(acc('4.4 — RESTORE: Activate the Seven Unclogging Levers', 'Restore', NL.join([
        P('RESTORE converts the agreed leadership response into organisational action. The Seven Unclogging Levers provide the established S2R® interventions for addressing the conditions represented by the Seven Performance Clogs. The executive team selects the relevant lever, implements the agreed changes and reviews evidence of recovery.'),
        table(['Established lever', 'Purpose', 'Best applied to'], LEVER_ROWS),
        P('These are the established Seven Strategic Unclogging Levers introduced in Section 2. The executive team chooses a lever according to the confirmed condition and the specific obstruction to be removed. The S2R® REALIGN stage is the collective decision and ownership step; Lever 06 — Realign is the distinct intervention used to adjust metrics and rewards.'),
        ol(['<strong>Select the relevant Unclogging Lever.</strong> Choose the intervention that addresses the confirmed clog.',
            '<strong>Activate the intervention.</strong> Implement the decisions and changes agreed during REALIGN.',
            '<strong>Verify performance recovery.</strong> Confirm that the obstruction is reducing and that the affected performance measures are moving in the intended direction.']),
        P('Removing a clog requires evidence that the organisational condition has changed. Sustained improvement is verified through the normal performance review rhythm.')])))
    ex = [
        '<div class="u9-okr"><p><strong>Enterprise Objective.</strong> Improve production reliability and on-time customer delivery.</p><p><strong>Enterprise Key Result.</strong> Increase customer orders delivered on time from 72% to 95% by year-end.</p><p class="u9-small">Performance figures are illustrative. The executive team notices that production interruptions are contributing to late deliveries.</p></div>',
        fsub('Step 1 — REVIEW: Confirm the Performance Clog'),
        table(['Line of sight', 'Diagnostic finding'], [
            ['Performance Outcome', 'Only 72% of customer orders are delivered on time, against the 95% target.'],
            ['Performance Behaviour', 'Maintenance managers wait for approval before ordering routine replacement parts. Equipment repairs and production schedules are delayed.'],
            ['Performance Condition', 'Financial approval requirements place routine maintenance decisions at senior management level, slowing necessary purchases.']]),
        P('<strong>Identified clog.</strong> Decision Bottlenecks.', 'The team confirms that avoidable approval delays contribute to maintenance downtime and late customer deliveries.'),
        fsub('Step 2 — REALIGN: Agree on Collective Ownership'),
        P('The CFO and COO agree that routine maintenance decisions must be faster while appropriate financial controls remain in place.'),
        table(['Leadership decision', 'Agreed response'], [
            ['What must change?', 'Approval authority for routine maintenance expenditure.'],
            ['Who coordinates?', 'CFO — revise financial approval arrangements.'],
            ['Who contributes?', 'COO — define operational requirements and ensure adoption.'],
            ['What must be agreed?', 'Delegated thresholds, control requirements, responsibilities and an implementation date.']]),
        hc('People performance implication', 'Maintenance managers gain clear authority to purchase approved routine replacement parts and can act promptly within defined controls.',
           'Organisational performance implication', 'The approval system preserves financial oversight while enabling reliable equipment maintenance and uninterrupted production flow.'),
        fsub('Step 3 — RESTORE: Activate the Unclogging Lever'),
        P('<strong>Selected lever.</strong> Lever 02 — Streamline | Increase Speed.',
          'Streamline simplifies workflows and removes approval layers that add no value to execution. It is appropriate because the confirmed clog is Decision Bottlenecks, and routine maintenance purchases are delayed by unnecessary approval steps.',
          '<strong>Activation.</strong> The CFO and COO implement the following changes:'),
        ol(['Identify approval steps that cause avoidable delays to routine maintenance purchases.',
            'Remove redundant approvals and simplify the routine purchase workflow.',
            'Retain appropriate controls and senior approval for exceptional or higher-risk expenditure.',
            'Communicate and implement the streamlined process with maintenance and operational teams.']),
        hc('People performance after Streamline', 'Maintenance managers can obtain routine replacement parts promptly and fulfil their responsibilities within clear approval limits, without repeated unnecessary escalation.',
           'Organisational performance after Streamline', 'Reduced approval time lowers maintenance downtime, supports production continuity and helps restore on-time customer delivery while preserving financial control.'),
        P('<strong>Verification.</strong> At the agreed executive review, examine:'),
        ul(['Routine maintenance approval turnaround time.', 'Equipment downtime caused by delayed replacement parts.', 'On-time customer delivery performance.', 'Compliance with the revised financial controls.']),
        P('The intervention is working when maintenance managers can exercise the revised authority confidently, routine decisions are made faster, approval-related downtime falls and customer delivery performance begins to recover without weakening financial control.'),
        fsub('Completed Unclogging Record'),
        table(['S2R® discipline', 'Leadership record'], [
            ['REVIEW', 'Decision Bottlenecks are contributing to maintenance and production delays.'],
            ['REALIGN', 'CFO coordinates; COO contributes. Both agree on revised approval authority and controls.'],
            ['RESTORE', 'Activate Lever 02 — Streamline and verify improvement through approval time, downtime, delivery and financial-control evidence.']])]
    a.append(acc('4.5 — Worked Example: Review–Realign–Restore', 'A manufacturing case', NL.join(fold(ex))))
    return a
REF8 = ('ref8', 'My Leadership Contribution to Strategic Unclogging',
        'Reflect on how your leadership decisions and practices may enable or constrain people and organisational performance. Think about a performance clog you have observed in your organisation, particularly one that may have been created, reinforced or left unresolved through decisions within your area of responsibility.',
        [('1 · REVIEW — Recognise the Clog', 'The clog', 'What performance clog have I observed or allowed to persist?', None),
         (None, 'Effect on people’s performance', 'How is this clog affecting people’s performance?', None),
         (None, 'Effect on organisational performance', 'How is this clog affecting organisational performance?', None),
         ('2 · REALIGN — Examine My Leadership Responsibility', 'My contribution to the clog', 'What decision, practice or behaviour within my control may be contributing to this clog?', None),
         (None, 'What I must change, and the leaders I need to engage', 'What must I change, and which other leaders do I need to engage?', None),
         ('3 · RESTORE — Commit to Action', 'The Unclogging Lever', 'Which of the Seven Strategic Unclogging Levers is most appropriate?', LEVERS),
         (None, 'My action and the evidence of improvement', 'What specific action will I take, and what evidence will demonstrate improvement?', None)])
HOW_REF8 = ['Think about a performance clog you have observed in your organisation, particularly one linked to decisions within your area of responsibility.',
            'Work through REVIEW, REALIGN and RESTORE, answering each question below.',
            'This is personal work. Your answers save as you type and go to your facilitator when you select Submit to Facilitator.']
T46, M46 = 'Participant Activity — Collective Strategic Unclogging', 'Personal reflection · Portfolio Work'
ACT_46 = 'Participants write a personal reflection in their own file, as Portfolio work: a performance clog they have observed or allowed to persist and its effect on people and organisational performance, their own leadership contribution to it and the leaders they need to engage, and the Unclogging Lever, action and evidence of improvement they commit to.'
CLOSE_S4 = ['Close by reinforcing both the shared leadership habit and the established S2R® discipline. Leaders must make emerging friction visible and respond collectively. REVIEW establishes the performance reality. REALIGN establishes collective leadership responsibility and the changes required for people and organisational performance. RESTORE activates the relevant intervention and verifies recovery.',
            'The goal is to make the removal of performance clogs a consistent part of executive review, decision-making and follow-through. Section 5 applies this integrated discipline to the participants’ strategic results.']

# ═══ Section 5 · Application (Carol, locked 16 Oct 13:59) ═══
S5_TITLE = 'The Strategic Unclogging Clinic'
S5_LEAD = 'Returning to an original work-based challenge, identifying the performance clog, selecting the corresponding Strategic Unclogging Lever and applying Review–Realign–Restore within the Capstone organisation.'
GUIDE_S5 = ['At the beginning of CESI, each group identified recurring work-based organisational challenges drawn from its members’ professional experiences. These challenges informed the simulated Capstone organisation. Participants must now return to that original list, select one challenge and apply the S2R® diagnostic and intervention tools they have learned.',
            'Teach the sequence clearly: original challenge → identify the clog → select the lever → Review–Realign–Restore. The initial classification is a working diagnosis; REVIEW checks it against performance evidence before the team commits to action. If REVIEW reveals a different underlying condition, the team must correct the clog and lever selection.',
            'Teach the group to support its diagnosis: the group explains why its selected clog fits the observed behaviours and organisational conditions. During REALIGN, the group sets out the implications for both people and organisational performance. During RESTORE, the group specifies the application of the selected lever, named executive ownership, completion timing and evidence of recovery.']
HOW_S5 = {
    'p': ['Your group selects one challenge from the list it documented before CESI began and links it to a strategic result (5.1).',
          'Your group identifies the performance clog (5.2) and selects the Strategic Unclogging Lever (5.3).',
          'Your group applies Review–Realign–Restore (5.4), then tests its response against the Diagnostic Quality Check (5.5).',
          'Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
          'In part 5.6 you read your group’s record and select Confirm. Your confirmed record feeds your team’s Capstone Blueprint.'],
    'f': ['Each group selects one challenge from the list it documented before CESI began and links it to a strategic result (5.1).',
          'The group identifies the performance clog (5.2) and selects the Strategic Unclogging Lever (5.3).',
          'The group applies Review–Realign–Restore (5.4), then tests its response against the Diagnostic Quality Check (5.5).',
          'The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.',
          'In part 5.6 each member reads the group’s record and selects Confirm. The confirmed record feeds the team’s Capstone Blueprint.']}
ACT_S5 = 'Participants work as a group in Section 5 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page and selects Confirm in part 5.6.'
# Section 5 entries: [id, record label, part, optional, type, options or placeholder, question shown above the box]
def fields():
    t = lambda i, lab, part, q, ph: [i, lab, part, False, 't', ph, q]
    return [
        t('ch_challenge', 'Selected original challenge', 'p1', 'State the challenge as your group originally understood it.', 'The challenge, as your group first described it...'),
        t('ch_link', 'Strategic connection', 'p1', 'Which strategic Objective and Key Result or KPI developed during CESI does this challenge affect?', 'The Objective, and the Key Result or KPI it affects...'),
        ['cl_clog', 'Selected clog', 'p2', False, 's', CLOGS, 'Which single category best explains the current challenge?'],
        t('cl_why', 'Reason for selection', 'p2', 'What specific observations make this the most likely clog?', 'The observations that point to this clog...'),
        ['lv_lever', 'Selected lever', 'p3', False, 's', LEVERS, 'Which of the seven levers will the group use?'],
        t('lv_why', 'Reason for selection', 'p3', 'How does this lever address the identified clog?', 'How the lever removes or reduces the clog...'),
        t('rv_outcome', 'REVIEW · Line of sight 1 · Performance Outcome', 'p4', 'State the affected Key Result or KPI, its current result and target.', 'The Key Result or KPI, its current result and its target...'),
        t('rv_behaviour', 'REVIEW · Line of sight 2 · Performance Behaviour', 'p4', 'Describe what individuals and teams are doing, delaying or unable to do.', 'What individuals and teams are doing, delaying or unable to do...'),
        t('rv_condition', 'REVIEW · Line of sight 3 · Performance Condition', 'p4', 'Identify the organisational condition causing or reinforcing those behaviours.', 'The organisational condition behind those behaviours...'),
        t('rv_check', 'REVIEW · Diagnosis check', 'p4', 'Does this evidence confirm the clog selected in 5.2? If not, revise both the clog and the lever before proceeding.', 'Confirmed, or revised: the clog and lever your group now holds...'),
        t('ra_people', 'REALIGN · People performance', 'p4', 'What must change in expectations, decision authority, capability, behaviours or support so people can fulfil their contributions?', 'What must change for the people delivering the result...'),
        t('ra_org', 'REALIGN · Organisational performance', 'p4', 'What must change in structures, systems, processes, resources or governance so the enterprise can achieve the intended result?', 'What must change in the organisational conditions...'),
        t('ra_owner', 'REALIGN · Coordinating executive owner', 'p4', 'Coordinating executive owner', 'The executive who coordinates the resolution...'),
        t('ra_contrib', 'REALIGN · Contributing executive functions', 'p4', 'Contributing executive functions', 'The executive functions that contribute...'),
        t('ra_change', 'REALIGN · Agreed organisational change', 'p4', 'Agreed organisational change', 'The organisational change the executives agree...'),
        t('ra_each', 'REALIGN · Each executive’s contribution', 'p4', 'Each executive’s contribution', 'What each executive will deliver...'),
        t('rs_intervention', 'RESTORE · Intervention', 'p5', 'What precisely will change through the selected lever?', 'What the lever changes, precisely...'),
        t('rs_action', 'RESTORE · Action and completion', 'p5', 'What will the coordinating and contributing executives implement, and by when?', 'Who implements what, and by when...'),
        t('rs_people', 'RESTORE · People performance evidence', 'p5', 'What improvement in capability, decisions, behaviours or contribution will show that employees and teams are better enabled?', 'The evidence that people are better enabled...'),
        t('rs_org', 'RESTORE · Organisational performance evidence', 'p5', 'What improvement in the relevant operating condition and strategic Key Result or KPI will demonstrate recovery?', 'The evidence that the condition and the Key Result or KPI are recovering...'),
        t('rs_review', 'RESTORE · Review commitment', 'p5', 'When will the executive team check progress and decide whether further action is necessary?', 'When the executive team will check progress...'),
    ]
# key, name, Capstone name (confirmed_items), confirm key, record heading, Capstone box
PARTS = [('p1', 'Original Challenge', 'Unclogging · Original Challenge', 'uc_challenge', '5.1 · Original Work-Based Challenge', '9A'),
         ('p2', 'Performance Clog', 'Unclogging · Performance Clog', 'uc_clog', '5.2 · Performance Clog', '9B'),
         ('p3', 'Unclogging Lever', 'Unclogging · Unclogging Lever', 'uc_lever', '5.3 · Strategic Unclogging Lever', '9C'),
         ('p4', 'Review and Realign', 'Unclogging · Review and Realign', 'uc_review_realign', '5.4 · Review and Realign', '9D'),
         ('p5', 'Restore', 'Unclogging · Restore', 'uc_restore', '5.4 · Restore', '9E')]
CLOG_ROWS = [['01 — Structural Misfit', 'Roles, reporting, ownership and coordination arrangements'],
             ['02 — Capability Gaps', 'Skills, resources, tools or capacity required for delivery'],
             ['03 — Decision Bottlenecks', 'Decision authority, approvals and escalation'],
             ['04 — Misaligned Metrics &amp; Incentives', 'Measures and rewards reinforcing the wrong contributions'],
             ['05 — Cultural Resistance', 'Established beliefs, norms and habits obstructing change'],
             ['06 — Technology / Infrastructure Lag', 'Systems, information and infrastructure limiting delivery'],
             ['07 — Leadership Avoidance', 'Unresolved leadership decisions, trade-offs and accountability']]
QUALITY = ['The original challenge is linked to a specific strategic result and supported by realistic performance evidence.',
           'The selected clog names the underlying organisational condition behind the symptom.',
           'The lever addresses the confirmed clog, and REALIGN considers both people and organisational performance.',
           'The RESTORE intervention is specific, owned, time-bound and supported by evidence that will show whether performance is recovering.']
OUTPUT = ['The original work-based challenge selected from its pre-CESI preparation.',
          'The identified Seven Performance Clog and reason for the diagnosis.',
          'The selected Seven Strategic Unclogging Lever and its intended purpose.',
          'The completed REVIEW, REALIGN and RESTORE responses, with executive ownership and evidence of recovery.']
CLOSE_S5 = ['Invite each group to explain briefly: the original challenge, the confirmed clog, the selected lever and the collective leadership response. Ask: “How has your understanding of this challenge changed since you first identified it before CESI?”',
            'Close by reinforcing the integrated discipline: recognise the challenge, identify the clog, select the suitable lever, and apply Review–Realign–Restore to confirm the diagnosis, coordinate leadership decisions and verify recovery across people and organisational performance.']

# ═══ Unit Summary ═══
SUM_P = [
    ('Awareness — What', 'What Was Established', 'You saw that a Strategic Clog is an internal blockage that prevents strategic intent from flowing into execution. Performance has two connected dimensions, organisational performance and people performance. The 7-Clog Diagnostic Map, aligned to ABCV Directional Integrity, examines both, and the Three Performance Lines of Sight trace a result from its outcome to the behaviours and the conditions behind it.'),
    ('Intelligence — Why', 'Why It Matters', 'You saw that clogs are design signals. Where strategy stretches the operating system beyond its current capacity, friction appears predictably. The 7 levers restore the structural, behavioural and operational conditions that allow strategy to flow at the intended speed.'),
    ('Extrapolating — Where', 'Where Clogs Begin', 'You saw that every executive function shapes the conditions in which other teams work. Traced through the Three Performance Lines of Sight, a decision or practice in one function can create or reinforce a clog in another.'),
    ('Integration — Collective', 'What Was Built', 'You saw that clogs rarely stay in one lane. The leadership team removes them together through Review–Realign–Restore: REVIEW confirms the clog, REALIGN agrees collective ownership and the changes for people and organisational performance, and RESTORE activates the Unclogging Lever and verifies recovery.'),
    ('Application — In Practice', 'What You Applied', 'Your group returned to an original work-based challenge, identified the clog, selected the lever and applied Review–Realign–Restore within your Capstone organisation.'),
]
SUM_F = [
    ('Awareness — What', 'A Strategic Clog is an internal blockage that prevents strategic intent from flowing into execution. Performance has two connected dimensions, organisational performance and people performance. The 7-Clog Diagnostic Map, aligned to ABCV Directional Integrity, examines both, and the Three Performance Lines of Sight trace a result from its outcome to the behaviours and the conditions behind it.'),
    ('Intelligence — Why', None),
    ('Extrapolating — Where', 'Every executive function shapes the conditions in which other teams work. Traced through the Three Performance Lines of Sight, a decision or practice in one function can create or reinforce a clog in another.'),
    ('Integration — Collective', 'Clogs rarely stay in one lane. The leadership team removes them together through Review–Realign–Restore: REVIEW confirms the clog, REALIGN agrees collective ownership and the changes for people and organisational performance, and RESTORE activates the Unclogging Lever and verifies recovery.'),
    ('Application — In Practice', 'Each group returned to an original work-based challenge, identified the clog, selected the lever and applied Review–Realign–Restore within its Capstone organisation. The confirmed record feeds the team’s Capstone Blueprint.'),
]

# ═══ Voice (Carol, 16 Oct 14:13: "Use appropriate language for facilitator and participant files") ═══
# Participant page speaks to the participant and "your group"; facilitator page speaks of "participants" and "the group".
VOICE = {
    'p': [('If the group has not established a current result, agree on a realistic illustrative figure consistent with its organisational scenario.', 'If your group has not established a current result, agree on a realistic illustrative figure consistent with your organisational scenario.'),
          ('Treat this as the initial diagnosis. The group will test it during REVIEW.', 'Treat this as the initial diagnosis. Your group will test it during REVIEW.'),
          ('Which of the seven levers will the group use?', 'Which of the seven levers will your group use?'),
          ('<p>Before the group finalises its response, test it against four criteria:</p>', '<p>Before your group finalises its response, test it against four criteria:</p>'),
          ('<p>The group submits one Strategic Unclogging Clinic Record containing:</p>', '<p>Your group submits one Strategic Unclogging Clinic Record containing:</p>'),
          ('<p>The completed record is incorporated into the existing Capstone portfolio.</p>', '<p>Your completed record is incorporated into your existing Capstone portfolio.</p>')],
    'f': [('Select each clog to examine its organisational conditions, effects on people, observable patterns, early warnings and strategic consequences.', 'Participants select each clog to examine its organisational conditions, effects on people, observable patterns, early warnings and strategic consequences.'),
          ('Select an executive role to examine a realistic decision and its consequences through the Three Performance Lines of Sight.', 'Participants select an executive role to examine a realistic decision and its consequences through the Three Performance Lines of Sight.'),
          ('<p>Think about one decision, policy or management practice within your own executive function that may be affecting the performance of another team or function. Examine its consequences through the Three Performance Lines of Sight.</p>', '<p>Participants think about one decision, policy or management practice within their own executive function that may be affecting the performance of another team or function, and examine its consequences through the Three Performance Lines of Sight.</p>'),
          ('<p>Reflect on how your leadership decisions and practices may enable or constrain people and organisational performance. Think about a performance clog you have observed in your organisation, particularly one that may have been created, reinforced or left unresolved through decisions within your area of responsibility.</p>', '<p>Participants reflect on how their leadership decisions and practices may enable or constrain people and organisational performance. Each thinks about a performance clog they have observed in their organisation, particularly one that may have been created, reinforced or left unresolved through decisions within their area of responsibility. They answer the questions below in the first person.</p>'),
          ('<p>Review the organisational challenges your group documented before CESI began. Select one challenge that remains relevant to your Capstone organisation and has a clear connection to disappointing organisational results.</p>', '<p>Each group reviews the organisational challenges it documented before CESI began and selects one challenge that remains relevant to its Capstone organisation and has a clear connection to disappointing organisational results.</p>'),
          ('State the challenge as your group originally understood it.', 'State the challenge as the group originally understood it.'),
          ('<p>Examine the selected challenge and identify which of the Seven Performance Clogs best explains the difficulty.', '<p>The group examines the selected challenge and identifies which of the Seven Performance Clogs best explains the difficulty.'),
          ('<p>Now select the established Strategic Unclogging Lever most appropriate for removing the identified obstruction. One clog may have more than one suitable lever; select the primary lever that best addresses the specific condition in your case.</p>', '<p>The group now selects the established Strategic Unclogging Lever most appropriate for removing the identified obstruction. One clog may have more than one suitable lever; the group selects the primary lever that best addresses the specific condition in its case.</p>'),
          ('<p>Use the Three Performance Lines of Sight to test the initial diagnosis and establish the evidence for intervention.</p>', '<p>The group uses the Three Performance Lines of Sight to test the initial diagnosis and establish the evidence for intervention.</p>'),
          ('<p>As the simulated executive team, determine what must change and identify who has the authority and responsibility to act. Explicitly consider both dimensions of performance.</p>', '<p>As the simulated executive team, the group determines what must change and identifies who has the authority and responsibility to act. It explicitly considers both dimensions of performance.</p>'),
          ('<p>Specify how the confirmed Strategic Unclogging Lever will be applied.', '<p>The group specifies how the confirmed Strategic Unclogging Lever will be applied.'),
          ('<p>Before the group finalises its response, test it against four criteria:</p>', '<p>Before the group finalises its response, it tests the response against four criteria:</p>'),
          ('<p>If any criterion is not met, return to the relevant step and refine the response.</p>', '<p>If any criterion is not met, the group returns to the relevant step and refines the response.</p>')],
}
