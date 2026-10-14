# -*- coding: utf-8 -*-
import re
"""Unit 6 · Performance Management Setup — content from Carol's "Amended content.docx" (14 October 2026).
Two voices: facilitator ('f': all of her content, every FACILITATOR GUIDANCE block, PARTICIPANT ACTIVITY notes)
and participant ('p': the same teaching, streamlined, written to "you", no facilitator wording).
Sentences reworded for the house rules are listed in RULE_FIXES; wording that is Claude's own is marked NEW."""

ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'
SR = 'S2R® Contribution Map™'
COL = ['#8ab0e8', 'var(--teall)', '#5ecba1', '#c39de0', '#e8c96a', '#f0a070']

RULE_FIXES = [
    ('1.2 facilitator guidance', '"…not only those responsible for individual and team targets"', '"…as well as those responsible for individual and team targets"'),
    ('1.4 FACES table, C · human', '"…supported by observable evidence rather than managerial impressions"', '"…rest on observable evidence"'),
    ('3.1 sub-line', '"Different Executive Lenses, One Enterprise Result"', '"Different Executive Perspectives, One Enterprise Result" (the word "lens" is not used)'),
    ('3.1 note under the table', '"…illustrates functional perspectives rather than prescribing a particular executive structure"', '"…illustrates functional perspectives. Each organisation reads it against its own executive structure."'),
    ('4.2 worked example, F · Operations', '"…respond to reported constraints rather than allowing them to recur"', '"…respond to reported constraints so that they do not recur"'),
    ('Section 5', '"automatically added to your CESI Capstone Portfolio" / "automatically populated"', 'the confirmed record feeds the team\'s Capstone Blueprint; the Key Result and the function names are shown from the earlier step'),
]


def x(v, f, p):
    return f if v == 'f' else p


def P(t):
    return '<p>' + t + '</p>'


def H4(t):
    return '<h4>' + t + '</h4>'


def HB(t):
    return '<div class="hbox"><p>' + t + '</p></div>'


def UL(items):
    return '<ul class="u6-list">' + ''.join('<li>' + i + '</li>' for i in items) + '</ul>'


def OL(items):
    return '<ol class="u6-list">' + ''.join('<li>' + i + '</li>' for i in items) + '</ol>'


def _len(h):
    return len(re.sub(r'<[^>]+>|&[a-z]+;', ' ', h))


def ITEMS(items):
    """Long content as compact rows: the title shows, the detail opens when the row is selected."""
    return '<div class="u6-its">' + ''.join(
        '<div class="u6-it"><div class="u6-it-h" onclick="this.parentNode.classList.toggle(\'open\')"><span>' + t +
        '</span><span class="u6-it-a">&#9662;</span></div><div class="u6-it-b">' + b + '</div></div>' for t, b in items) + '</div>'


def TABLE(head, rows, cap=None):
    """Short tables stay tables. A wide or long table becomes one compact row per line of the table:
    the first column shows, the other columns open when the row is selected."""
    c = '<div class="u6t-cap">' + cap + '</div>' if cap else ''
    if len(head) >= 4 or max(_len(''.join(r)) for r in rows) > 220:
        def strong(x): return x if x.startswith('<strong>') else '<strong>' + x + '</strong>'
        return c + ITEMS([(strong(r[0]), ''.join('<p><b class="u6-it-l">' + hd + '</b>' + (cell or '<i>to complete</i>') + '</p>' for hd, cell in zip(head[1:], r[1:]))) for r in rows])
    h = ''.join('<th>' + c_ + '</th>' for c_ in head)
    b = ''.join('<tr>' + ''.join('<td>' + c_ + '</td>' for c_ in r) + '</tr>' for r in rows)
    return c + '<div class="u6t-wrap"><table class="u6t"><thead><tr>' + h + '</tr></thead><tbody>' + b + '</tbody></table></div>'


def CARDS(items, first_open=True):
    """Short cards side by side, everything visible (no arrows). Long cards become compact rows that open when selected."""
    if max(_len(it[2]) for it in items) > 200:
        return ITEMS([('<strong>' + it[0] + ' &middot; ' + it[1] + '</strong>' if it[0] != it[1] else '<strong>' + it[1] + '</strong>', it[2]) for it in items])
    out = []
    for i, it in enumerate(items):
        num, name, body = it[0], it[1], it[2]
        col = it[3] if len(it) > 3 else COL[i % len(COL)]
        out.append('<div class="u6-hc-c" style="border-top-color:%s;"><div class="u6-hc-n" style="color:%s;">%s</div><div class="u6-hc-t">%s</div><div class="u6-hc-b">%s</div></div>' % (col, col, num, name, body))
    return '<div class="u6-hc">' + ''.join(out) + '</div>'


END = '<!--end-sub-->'


def SUB(title, body):
    """A long subsection or table, collapsed until selected."""
    return ('<div class="u6-sub"><div class="u6-sub-h" onclick="this.parentNode.classList.toggle(\'open\')"><span>' + title +
            '</span><span class="u6-sub-a">&#9662;</span></div><div class="u6-sub-b">' + body + '</div></div>')


def GROUP(items):
    """Wrap every numbered subsection (h4 "N.N.N …") into SUB. A subsection runs to the next h4, the end marker,
    a reflection or activity box, or a facilitator guidance box that follows content (one that opens the subsection stays inside)."""
    out, cur, seen = [], None, False
    def close():
        if cur is not None: out.append(SUB(cur[0], '\n'.join(cur[1])))
    for it in items:
        m = re.match(r'<h4>(\d\.\d\.\d .*)</h4>$', it) or (seen and re.match(r'<h4>(.*)</h4>$', it))
        stop = it.startswith('<h4>') or it == END or it.startswith('<div class="ref-block"') or 'u6-activity' in it[:60] or \
            (it.startswith('<div class="fac-note-full"') and cur is not None and cur[1])
        if cur is not None and stop:
            close(); cur = None
        if m:
            cur = (m.group(1), []); seen = True; continue
        if it == END: continue
        if cur is not None: cur[1].append(it)
        else: out.append(it)
    close()
    return out


def FG(paras, label='FACILITATOR GUIDANCE'):
    return '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; ' + label + '</div>' + ''.join(paras) + '</div>'


def PACT(paras):
    return '<div class="fac-note-full u6-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>' + ''.join(paras) + '</div>'


def REF(rid, label, q, ph, portfolio=False):
    pf = ''
    return ('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; ' + label + '</div>' + pf +
            '<p class="ref-prompt" style="font-size:12px;color:rgba(255,255,255,.65);margin-bottom:8px;">' + q + '</p>'
            '<textarea class="ref-ta reflection-textarea" id="' + rid + '" placeholder="' + ph + '"></textarea>'
            '<div class="ref-saved reflection-saved" id="' + rid + '-saved"></div><button class="ref-save" onclick="saveTA(this)">Save Reflection</button></div>')


def PART(num, title, meta, body, open_=False):
    if isinstance(body, list): body = '\n'.join(GROUP(body))
    return ('<div class="acc' + (' open' if open_ else '') + '">\n'
            '<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">' + num + ' &mdash; ' + title + '</div><div class="acc-meta">' + meta + '</div></div>' + ARR + '</div>\n'
            '<div class="acc-b"><div class="cb">\n' + body + '\n</div></div></div>\n')


def SLO(items):
    return '<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>' + ''.join('<li>' + i + '</li>' for i in items) + '</ul></div>\n'


# ─────────────────────────── Reflections (participant) ───────────────────────────
REFS = {
    'ref13': ('Two Operating Systems',
              'Think of a recurring performance shortfall in your organisation. Does your current performance management system assess both dimensions, the Human Operating System and the Organisational Operating System, and assign accountability for addressing them?',
              'The recurring shortfall I am thinking of is…&#10;&#10;Our PM system assesses… and assigns accountability for…'),
    'ref12': ('Your Current PM System',
              'What is the current PM architecture of your organisation? Which PM system is currently being used?',
              'Our current PM architecture is… (for example: annual or continuous, rating-centric or development-centric, individual or team)&#10;&#10;The PM system we currently use is…'),
    'ref14': ('Contributions in Your Organisation',
              'Choose one enterprise Key Result in your own organisation. Which business functions must contribute to it? For one of those functions, what must its people deliver, and which Environment, Systems, Resources or Governance conditions must the organisation provide for that delivery? Where is the connection weakest today?',
              'The enterprise Key Result: …&#10;The functions that must contribute: …&#10;&#10;For [function], people must deliver… and the organisation must provide…&#10;&#10;The weakest connection today: …'),
    'ref15': ('FACES in Your Organisation',
              'For the Key Result you chose in part 1.3: which FACES function is weakest in the way your organisation manages these contributions today, for the people and for the ESRG conditions? Which one management arrangement would strengthen it?',
              'The weakest FACES function is… because…&#10;&#10;For the people: …&#10;For the ESRG conditions: …&#10;&#10;The arrangement that would strengthen it: …'),
}
REF_ORDER = ['ref13', 'ref12', 'ref14', 'ref15']


def ref_block(v, rid, part_no):
    label, q, ph = REFS[rid]
    if v == 'p':
        return REF(rid, label, q, ph, portfolio=True)
    return PACT([P('Participants write a personal reflection in their own file (Learning Portfolio): <em>' + q + '</em>')])


FACES_ROWS = [
    ['<strong>F &mdash; Foster a Results Culture</strong>',
     'Establish a culture of individual and team performance ownership. Employees understand their targets, take responsibility for commitments and demonstrate expected behaviours. Leaders reinforce performance through regular feedback, recognition of dependable contributors and consistent responses to underperformance. Achieving results through behaviours that undermine colleagues, customers or organisational values is not acceptable performance.',
     'Establish organisational responsibility for enabling results. Leaders must demonstrate the same commitment to maintaining effective operating conditions that they expect employees to demonstrate towards their targets. Recurring system failures, inadequate resources or governance delays cannot be continually tolerated while employees are held accountable for missed results. A results culture requires leaders to address ESRG constraints that repeatedly undermine delivery.'],
    ['<strong>A &mdash; Align Performance</strong>',
     'Connect individual and team performance to enterprise strategic outcomes. Strategic priorities must translate into meaningful KPIs, OKRs and behavioural expectations. Employees should understand how their work contributes to broader organisational results. Alignment also includes collaboration where successful delivery depends on contributions across departments.',
     'Align ESRG with enterprise strategic requirements. The working environment, systems, resources and governance arrangements must be configured to support the results the organisation intends to achieve. For example, a strategic commitment to faster customer service must be supported by efficient workflows, sufficient capacity and timely decision-making. Targets become difficult to achieve when organisational capability is misaligned with strategic ambition.'],
    ['<strong>C &mdash; Create Measurement Transparency</strong>',
     'Make performance expectations and assessment criteria clear and credible. Employees must understand their KPIs, targets, weightings, behavioural standards and rating criteria. Performance assessments should rest on observable evidence. Transparency allows employees to understand their progress and builds confidence in the fairness of performance evaluations.',
     'Make organisational performance conditions measurable and visible. Leaders need evidence of whether ESRG is supporting or constraining delivery. This includes system availability, process efficiency, capacity against demand, cross-functional coordination and decision turnaround times. A missed departmental target reveals a performance gap; ESRG evidence helps establish why that gap exists and where intervention is required.'],
    ['<strong>E &mdash; Embed Shared Accountability</strong>',
     'Clarify responsibility for individual contributions and collective results. Individuals remain accountable for their KPIs, OKRs and behaviours. Managers are accountable for setting expectations, providing feedback and addressing performance concerns. Where results require teamwork, each person&rsquo;s contribution and responsibilities must be clear. Shared accountability should strengthen ownership without making responsibility ambiguous.',
     'Assign accountability for organisational enablement and constraint resolution. Responsibility for ESRG must sit with the appropriate owners. Operations may own process efficiency, IT may own system reliability, resource owners may own capacity, and executives may own governance decisions. Where one function&rsquo;s performance depends on another, the dependency, accountable owner and escalation arrangements must be explicit. This forms part of the foundation for the ' + SR + '.'],
    ['<strong>S &mdash; Support Continuous Development</strong>',
     'Use performance evidence to strengthen individual and team capability. Reviews should identify development needs linked to actual performance requirements. These may include technical skills, planning, decision-making, leadership, collaboration or behavioural improvement. Development actions should have clear objectives and follow-up reviews to determine whether performance has improved.',
     'Use performance evidence to strengthen organisational operating capability. Recurring ESRG constraints should trigger improvements to workflows, technologies, resource allocation, operating conditions or governance arrangements. For example, repeated approval delays may require redesigned decision rights, while persistent capacity shortages may require resource reallocation. Organisational improvement must be monitored to establish whether the intervention strengthens delivery.']]

# ─────────────────────────── SECTION 1 ───────────────────────────
S1_TITLE = 'Foundations of Enterprise Performance Management System Design'
S1_HERO = 'What performance management must manage: the contribution of people and the conditions the organisation provides, connected to enterprise results.'  # NEW
S1_SLO = ['Distinguish performance measurement from the management system that converts evidence into decisions and action.', 'Explain how human contribution and organisational operating conditions interact to produce enterprise results, and why both must be managed together.']


def s1(v):
    o = []
    # 1.1
    b = [P('Performance management (PM) and performance measurement are distinct disciplines. <strong>Measurement</strong> answers: <em>What happened?</em> It provides data, results, scores and dashboards. <strong>Management</strong> answers: <em>What do we do about it?</em> It establishes the conversations, decisions, actions and accountability through which leaders respond to that evidence.'),
         P(x(v, 'An organisation can measure a missed service target accurately without managing the cause. A dashboard may show that customer requests take twelve days against a standard of five. Effective management asks whether the delay reflects unclear individual expectations, insufficient capacity, a broken hand-off, slow approval rights, or a combination. Each explanation calls for a different response.',
               'Your organisation can measure a missed service target accurately without managing its cause. A dashboard may show that customer requests take twelve days against a standard of five. Effective management asks whether the delay comes from unclear individual expectations, insufficient capacity, a broken hand-off, slow approval rights, or a combination. Each explanation calls for a different response.')),
         H4('The design sequence'),
         P('The design sequence is deliberate:'),
         CARDS([('Step 1', 'Define success', P('Agree the result the organisation must achieve.')),
                ('Step 2', 'Design how performance will be managed', P('Agree the conversations, decisions, actions and accountability that will respond to the evidence.')),
                ('Step 3', 'Identify the evidence that management decisions require', P('Collect the data the management decisions need.')),
                ('Step 4', 'Use the evidence', P('Recognise contribution, correct constraints and improve delivery.'))]),
         HB('Reports become useful because the organisation has decided who will act on them and how.')]
    if v == 'f':
        b.append(FG([P('Ask: <em>&ldquo;If your organisation stopped producing its performance reports tomorrow, which decisions would leaders no longer be able to make?&rdquo;</em> Follow with: <em>&ldquo;When a target is missed, how do you distinguish an individual contribution problem from an organisational delivery problem?&rdquo;</em>')]))
    o.append(PART('1.1', 'Measurement vs Management', 'The core distinction', b, True))

    # 1.2
    b = [P('Enterprise performance is the combined result of individual and collective contributions, supported by the organisational conditions required to deliver those results.'),
         P(x(v, 'An organisation may have capable employees who consistently work towards their targets, yet still struggle to achieve its strategic outcomes. Equally, an organisation may have strong systems, sufficient resources and well-designed processes, but fail to achieve results because individuals are not delivering the contributions expected of them.',
               'An organisation may have capable employees who work towards their targets and still struggle to achieve its strategic outcomes. Equally, it may have strong systems, sufficient resources and well-designed processes, and still fail because individuals are not delivering the contributions expected of them.')),
         P('This distinction is fundamental to Enterprise Performance Management (EPM). A complete performance management system must evaluate what people contribute and whether the organisation provides the conditions necessary for those contributions to produce the intended results. We refer to these as two interconnected operating systems.'),
         H4('1.2.1 The Human Operating System'),
         P('<em>What individuals and teams contribute to organisational results.</em>'),
         P('The Human Operating System concerns the measurable performance of people within the organisation. It examines whether individuals and teams deliver the results expected of them and demonstrate the behaviours required to achieve those results. Human performance has two primary dimensions.'),
         CARDS([('Dimension 1', 'Performance against KPIs and objectives',
                 P('These establish what an individual or team is expected to deliver. They may include strategic contributions expressed through OKRs, operational outputs measured through key performance indicators (KPIs), and specific performance commitments.') +
                 P('For example, a customer service employee may be expected to resolve 90% of enquiries within an agreed turnaround time, while a sales manager may be accountable for achieving a quarterly revenue target.') +
                 P('The performance management system must establish clear targets, evidence of achievement and a consistent basis for evaluating actual performance.')),
                ('Dimension 2', 'Performance against behavioural expectations',
                 P('These establish how individuals are expected to perform their responsibilities. They include observable behaviours such as collaboration, accountability, adherence to organisational values, responsiveness, ethical conduct and leadership effectiveness.') +
                 P('For example, a manager may achieve departmental targets while consistently withholding information from other departments, undermining collaboration and delaying enterprise-wide delivery.') +
                 P('A complete assessment must therefore consider both the results achieved and the behaviours demonstrated.'), COL[1], True)]),
         HB('The Human Operating System answers: <strong>Are individuals and teams delivering their expected results and demonstrating the behaviours required for sustained organisational performance?</strong>'),
         H4('1.2.2 The Organisational Operating System'),
         P('<em>Whether the organisation is equipped and configured to deliver its intended results.</em>'),
         P('The Organisational Operating System concerns the conditions that enable or constrain performance. Within S2R®, these conditions are examined through ESRG: Environment, Systems, Resources and Governance. ESRG provides the structure for evaluating whether the organisation has the operating capability necessary to support its strategic ambition.'),
         CARDS([('E', 'Environment', P('The conditions within which people and organisational processes operate. These include the working environment, organisational climate, cross-functional relationships and external operating conditions that influence delivery.') +
                 P('<strong>Example:</strong> a customer service team may have clear targets, but persistent conflict between departments prevents timely resolution of customer enquiries.') +
                 P('<strong>Performance management consideration:</strong> Are the operating conditions supporting or obstructing the achievement of expected results?')),
                ('S', 'Systems', P('The processes, workflows, technologies and operating mechanisms through which work is performed. Systems determine how efficiently and reliably the organisation converts effort and resources into outputs.') +
                 P('<strong>Example:</strong> employees may be expected to process 100 applications daily, but an unreliable processing system limits actual throughput to 60 applications.') +
                 P('<strong>Performance management consideration:</strong> Are the systems and processes capable of supporting the required performance standards?')),
                ('R', 'Resources', P('The people, skills, capacity, funding, equipment, information and other resources required to deliver results. Resource adequacy must be evaluated against the level of performance the organisation expects.') +
                 P('<strong>Example:</strong> a department may be required to double its service output while operating with the same capacity and equipment.') +
                 P('<strong>Performance management consideration:</strong> Does the organisation have sufficient and appropriately deployed resources to achieve its targets?')),
                ('G', 'Governance', P('The decision rights, accountability arrangements, policies, controls and escalation mechanisms that guide organisational execution. Governance determines whether decisions can be made at the appropriate level and whether constraints can be resolved in time.') +
                 P('<strong>Example:</strong> a department may have the resources to complete a project, but repeated approval delays prevent it from meeting agreed milestones.') +
                 P('<strong>Performance management consideration:</strong> Do governance arrangements enable timely decisions, clear accountability and effective resolution of performance constraints?'))]),
         HB('The Organisational Operating System answers: <strong>Does the organisation have the environment, systems, resources and governance necessary to deliver its expected results consistently?</strong>'),
         H4('1.2.3 How the Two Operating Systems Interact'),
         P('The two systems are interdependent. Human performance measures what individuals and teams contribute. Organisational performance examines whether ESRG provides the conditions required for those contributions to produce enterprise results.'),
         P('Consider a customer service department with a target of resolving 90% of enquiries within 48 hours. At the end of the month, the department achieves only 65%. A conventional performance review may conclude that the employees are underperforming. An integrated EPM system examines both operating systems before determining the appropriate management response.'),
         TABLE(['Human Operating System', 'Organisational Operating System — ESRG'],
               [['Are employees meeting their individual resolution targets?', '<strong>Environment:</strong> Are cross-functional working conditions supporting timely resolution?'],
                ['Are employees following the required service procedures?', '<strong>Systems:</strong> Is the customer management system functioning reliably?'],
                ['Are employees demonstrating accountability and responsiveness?', '<strong>Resources:</strong> Is staffing capacity sufficient for the volume of enquiries?'],
                ['Are team leaders meeting their supervisory commitments?', '<strong>Governance:</strong> Are decisions and escalations being resolved within the required time?']]),
         P('The evidence may reveal that employees are performing their responsibilities correctly, but system failures and approval delays are preventing the department from achieving its targets. Alternatively, ESRG conditions may be adequate, while employees are consistently failing to meet agreed performance expectations.'),
         P('Both situations produce disappointing results, but they require different management responses. This is why an enterprise performance management system must distinguish between human performance shortfalls and organisational operating constraints. It enables leaders to establish accountability fairly, direct interventions appropriately and avoid repeatedly holding individuals responsible for conditions outside their control.'),
         H4('The Enterprise Performance Principle'),
         HB('Organisational performance emerges from the interaction between what individuals and teams contribute and how effectively the organisation&rsquo;s Environment, Systems, Resources and Governance enable those contributions to produce results.'),
         P('An integrated EPM system must therefore establish two connected lines of performance accountability:'),
         UL(['<strong>Human Performance:</strong> individual and team KPIs, OKRs and behavioural expectations.',
             '<strong>Organisational Performance:</strong> ESRG effectiveness in enabling the achievement of enterprise outcomes.']),
         P('Both must be visible, measured, reviewed and managed.')]
    if v == 'f':
        b.append(FG([P('Begin by asking participants: <em>&ldquo;When an employee or department misses a performance target, how does your organisation determine whether the problem is with individual performance or the conditions under which the work is performed?&rdquo;</em>'),
                     P('Use the customer service example to demonstrate that a missed target is evidence of a performance gap, but does not automatically establish its cause.'),
                     P('Emphasise that leaders must examine both the contribution expected from people and the ESRG conditions required to enable delivery.'),
                     P('The central teaching point is that performance accountability must extend to those responsible for organisational operating conditions as well as those responsible for individual and team targets.')]))
    b.append(ref_block(v, 'ref13', '1.2'))
    o.append(PART('1.2', 'Two Operating Systems Behind Enterprise Performance', 'Understanding what people deliver and what the organisation enables', b))

    # 1.3
    b = []
    if v == 'f':
        b.append(FG([P('Introduce the Contribution Map using the customer service example. Begin with the enterprise key result of improving 48-hour customer enquiry resolution from 65% to 90%.'),
                     P('Explain that achieving this outcome requires contributions from several functions, each with different responsibilities. Walk participants through the map, showing how Customer Service, IT, Operations and Workforce Planning contribute to the same enterprise result.'),
                     P('Emphasise three teaching points:'),
                     OL(['<strong>Functional KPIs must have a clear connection to enterprise outcomes.</strong> A department can perform well against its own measures without making the contribution the enterprise requires.',
                         '<strong>Functional contributions are interdependent.</strong> A weakness in one function can undermine the results of several others.',
                         '<strong>Accountability must follow the contribution.</strong> Each function must be accountable for the performance commitments it controls, while collective enterprise results remain a shared leadership responsibility.'])]))
    b += [H4('1.3.1 What Is the ' + SR + '?'),
          P('<em>Integrated human and organisational contributions.</em>'),
          P('The ' + SR + ' is a strategy-to-execution tool that identifies the interconnected contributions required from business functions, individuals and teams, and organisational operating conditions to achieve an enterprise strategic outcome.'),
          P('It establishes a clear line of sight between the organisation&rsquo;s strategic intent and the contributions required across its two operating systems:'),
          UL(['<strong>Human Operating System:</strong> the results and behaviours individuals and teams must deliver.',
              '<strong>Organisational Operating System:</strong> the Environment, Systems, Resources and Governance (ESRG) necessary to enable those contributions.']),
          P('The map identifies the relationships and dependencies between functions, making visible how their combined contributions support enterprise results. Where appropriate, it also establishes measurable performance commitments or evidence that the required organisational conditions are in place.'),
          HB('The central principle: enterprise results are achieved through connected human and organisational contributions, supported by clear functional accountability.'),
          H4('1.3.2 Why the Contribution Map Matters'),
          P('An organisation achieves its strategic results through the combined contributions of its business functions. Each function performs different activities, possesses different capabilities and carries different responsibilities. However, these contributions must ultimately support the same enterprise strategic outcomes.'),
          P('A common weakness in performance management is that departments establish their own KPIs and measure their performance independently. Finance measures financial performance, HR measures people-related outcomes, IT measures technology performance, and Operations measures operational efficiency. Each department may report satisfactory performance while the organisation continues to miss its strategic targets. This happens when functional performance is managed without sufficient clarity about how the contributions connect to enterprise results.'),
          P('For example, an organisation may have an enterprise objective to improve customer service. Customer Service may focus on resolving enquiries, IT on maintaining system availability, Operations on processing requests, and HR on ensuring adequate staffing. All four functions may have relevant KPIs. However, unless their contributions are connected to the enterprise objective, leaders may struggle to establish whether the combined performance of these functions is sufficient to achieve the intended result.'),
          HB('The ' + SR + ' provides that connection.'),
          H4('1.3.3 The Logic of the Contribution Map'),
          P('The map follows three connected steps.'),
          CARDS([('Step 1', 'Enterprise OKR &mdash; What must the organisation achieve?', P('Identify the agreed enterprise strategic objective and its measurable key result. This establishes the collective outcome towards which the organisation is working.')),
                 ('Step 2', 'Required Functional Contributions &mdash; What must each function deliver?', P('Identify the specific contribution each business function must make towards achieving the enterprise outcome. These contributions must reflect the interdependencies between functions.')),
                 ('Step 3', 'Human and Organisational Contributions &mdash; What is required to deliver each functional contribution?', P('For each function, identify:') +
                  UL(['<strong>Human Operating System:</strong> the results and behaviours required from individuals and teams, together with measurable performance commitments wherever practical.',
                      '<strong>Organisational Operating System:</strong> the specific ESRG conditions necessary to enable delivery, together with appropriate performance measures or evidence that those conditions are established and functioning.']) +
                  P('Only the ESRG elements relevant to the required contribution are included. Not every ESRG requirement needs a numerical metric.'))]),
          H4('1.3.4 How the Contribution Map Connects to the Two Operating Systems'),
          P('The ' + SR + ' integrates the two operating systems into the design of enterprise performance. For every required functional contribution, the map identifies two interconnected dimensions.'),
          CARDS([('Human Performance', 'What must people deliver?', P('The map establishes the expected results and behaviours of individuals and teams, supported by measurable performance commitments wherever practical.')),
                 ('Organisational Performance', 'What must the organisation enable?', P('The map identifies the specific Environment, Systems, Resources and Governance (ESRG) requirements necessary for people to deliver their contributions. These requirements may be expressed through numerical performance standards or other evidence of organisational readiness and effectiveness.'), COL[1], True)]),
          P('For example, maintaining reliable customer management systems requires IT employees to monitor and resolve incidents promptly. It also requires reliable infrastructure and sufficient technical support capacity. The human contribution can be assessed through incident-resolution performance. Organisational capability can be assessed through system availability and evidence of adequate technical support arrangements.'),
          P('The two dimensions are connected but require distinct management attention. The Contribution Map therefore establishes what must be delivered by people, what must be enabled by the organisation, and how both contribute to the enterprise result.'),
          H4('From the Contribution Map to FACES')] + ([
          P('The ' + SR + ' establishes what each function must contribute, what people must deliver and which organisational conditions must support their performance. It also identifies the measures and evidence required to assess these contributions.'),
          P('The next challenge is to ensure that these commitments are consistently delivered and that performance gaps trigger appropriate management action. The FACES Framework establishes the five management functions required to achieve this across the Human and Organisational Operating Systems.')] if v == 'f' else [
          P('The map sets out what must be delivered and enabled, with the measures and evidence for each. FACES, in part 1.4, sets out the five management functions that keep those commitments delivered and make performance gaps trigger action.')])
    b.append(ref_block(v, 'ref14', '1.3'))
    o.append(PART('1.3', 'The ' + SR, 'Connecting enterprise strategic outcomes to functional contributions', b))

    # 1.4
    b = [H4('1.4.1 The FACES Framework'),
         P('The FACES Framework defines five interconnected functions that an effective Enterprise Performance Management (EPM) system must fulfil. Each function applies to both operating systems:'),
         UL(['<strong>Human Performance:</strong> what individuals and teams deliver through their KPIs, OKRs and demonstrated behaviours.',
             '<strong>Organisational Performance:</strong> how effectively the organisation&rsquo;s Environment, Systems, Resources and Governance (ESRG) enable the achievement of intended results.']),
         TABLE(['FACES Function', 'Human Performance &mdash; KPIs, OKRs &amp; Behaviours', 'Organisational Performance &mdash; ESRG'], FACES_ROWS, 'FACES &mdash; comparing human and organisational performance'),
         H4('1.4.2 How FACES Works When the Enterprise Result Falls Short'),
         P('Assume the organisation reviews its performance and finds that only 65% of customer enquiries are being resolved within 48 hours, against the year-end target of 90%. The review reveals different performance conditions across the four functions.'),
         TABLE(['Function', 'Performance Evidence', 'How FACES Is Applied'],
               [['<strong>Customer Service</strong>', 'Follow-through on outstanding enquiries is below the agreed standard.', 'Outstanding cases are reviewed against assigned responsibilities. Employees receive feedback on missed commitments, recurring obstacles are escalated, and subsequent follow-through results establish whether performance is improving.'],
                ['<strong>IT</strong>', 'Incident-response commitments are being achieved, but system availability remains below the required standard.', 'Incident-response performance and system availability are examined separately. IT leadership investigates recurring outages, assigns responsibility for correcting the underlying infrastructure problems and reviews subsequent availability results.'],
                ['<strong>Operations</strong>', 'Processing performance is affected by approval delays and some employee processing gaps.', 'Processing records distinguish employee-related delays from approval bottlenecks. Employees receive support where performance gaps are identified, while the appropriate decision owners review approval arrangements that are slowing delivery.'],
                ['<strong>HR / Workforce Planning</strong>', 'Staffing schedules are completed as required, but actual staffing coverage remains insufficient.', 'Completed schedules are compared with actual staffing requirements. Workforce Planning coordinates available staffing adjustments, while unresolved capacity requirements are submitted to the appropriate resource decision-makers.']]), END]
    if v == 'f':
        b.append(FG([P('Walk participants through the four functions, showing how the same FACES principles are applied differently according to the contributions required.'),
                     P('Draw attention to the distinction between human performance accountability and organisational enablement accountability.'),
                     P('Conclude by reinforcing the connection:'),
                     HB('The ' + SR + ' establishes the contributions, performance measures and enabling conditions required for enterprise results. FACES establishes the management disciplines through which those contributions are aligned, evaluated, acted upon and continuously strengthened.')]))
    else:
        b.append(HB('The ' + SR + ' establishes the contributions, performance measures and enabling conditions required for enterprise results. FACES establishes the management disciplines through which those contributions are aligned, evaluated, acted upon and continuously strengthened.'))
    b.append(ref_block(v, 'ref15', '1.4'))
    o.append(PART('1.4', 'The FACES Framework', 'Five functions of an integrated Enterprise Performance Management system', b))
    return o


BRIDGES = [
    ['<strong>1. Decomposing the Big Picture</strong>',
     'Enterprise strategy must remain connected to the contributions through which it is delivered. As priorities and operating demands change, the relationship between functional performance and enterprise outcomes must remain clear.',
     'Maintains the line of sight between enterprise objectives and individual or team expectations. Employees understand how their contributions support the intended result, including where delivery depends on other functions.',
     'Maintains alignment between strategic requirements and the organisational conditions needed to support them. Systems, resources, workflows and decision arrangements must remain appropriate to the demands of execution.',
     'Functions become increasingly focused on their own activities and targets. Individual performance may appear satisfactory while the collective contribution to enterprise results weakens.'],
    ['<strong>2. Defining the Logic of Success</strong>',
     'Performance must be evaluated against a shared understanding of successful delivery. Completing an activity or achieving an isolated target does not necessarily establish that the intended contribution has been achieved.',
     'Establishes clear expectations for results, performance standards, behaviours and evidence of achievement. Employees and managers have a credible basis for evaluating contribution.',
     'Establishes how effective organisational enablement will be recognised. Relevant ESRG conditions are assessed through appropriate measures or qualitative evidence of their effectiveness.',
     'Different functions interpret success differently. Human performance may be rated positively while organisational constraints remain unresolved, creating a misleading picture of execution readiness and achievement.'],
    ['<strong>3. Calibrating the Rhythm</strong>',
     'Execution unfolds over time. Changes in performance, demand and operating conditions must become visible early enough for leaders to influence the outcome.',
     'Provides regular visibility of individual and team progress, emerging performance gaps and development needs. Review frequency reflects the nature of the contribution and its effect on results.',
     'Provides visibility of changing organisational conditions, such as system reliability, staffing capacity, process efficiency and decision delays. Monitoring frequency reflects the nature and significance of each condition.',
     'Performance deterioration is recognised too late. Employees continue working against targets while emerging organisational constraints accumulate, leaving limited opportunity for recovery.'],
    ['<strong>4. Structuring the Dialogue</strong>',
     'Performance evidence creates value when it informs decisions and action. Reviews must establish what is influencing results, who is responsible and what response is required.',
     'Enables evidence-based conversations about contribution, achievement, behaviour, performance gaps and improvement. Employees and managers establish appropriate responses and follow-through.',
     'Enables leaders to examine ESRG constraints, determine their effect on delivery and assign decisions or interventions to the appropriate organisational owners. Cross-functional dependencies are addressed collectively.',
     'Performance meetings become reporting exercises. The same gaps recur because evidence does not consistently lead to decisions, coordinated interventions and accountable follow-through.']]

# ─────────────────────────── SECTION 2 ───────────────────────────
S2_TITLE = 'Performance Management as the Execution Bridge'
S2_HERO = 'Understanding why enterprise performance depends on connecting strategic outcomes, human contributions and organisational operating capability through an integrated management system.'
S2_SLO = ['Determine the disciplines that keep strategy connected to performance throughout delivery.', 'Assess the compliance and commitment characteristics of a performance management system.']


def s2(v):
    o = []
    b = [P('The ' + SR + ' establishes the contributions required to achieve enterprise results. FACES defines the five functions through which human and organisational performance are managed. The next challenge is sustaining the connection between these contributions and the intended results throughout execution.'),
         P('Strategy is delivered over time. Performance expectations must remain clear, progress must be visible, and emerging gaps must lead to timely management responses. Without these disciplines, the connection between strategic intent and actual delivery gradually weakens.'),
         HB('This is why performance management serves as an execution bridge: it provides the disciplines that keep strategy connected to performance throughout delivery.'),
         P('Four interconnected bridges make this possible:'),
         CARDS([('Bridge 1', 'Decomposing the Big Picture', P('Connecting strategic outcomes to actionable performance expectations.')),
                ('Bridge 2', 'Defining the Logic of Success', P('Establishing how successful performance is understood and evaluated.')),
                ('Bridge 3', 'Calibrating the Rhythm', P('Maintaining visibility of progress throughout the execution period.')),
                ('Bridge 4', 'Structuring the Dialogue', P('Converting performance evidence into decisions and action.'))]),
         P('Together, these bridges explain why performance management is essential to sustaining the connection between strategy, human contribution, organisational capability and enterprise results.'),
         H4('2.1.1 How the Four Execution Bridges Work Together'),
         P('The four bridges work together to sustain the connection between strategy and results. Each addresses a particular risk that can weaken execution across the Human and Organisational Operating Systems.'),
         TABLE(['Execution Bridge', 'Why It Matters', 'Human Operating System &mdash; KPIs, OKRs &amp; Behaviours', 'Organisational Operating System &mdash; ESRG', 'What Happens When the Bridge Weakens'], BRIDGES)]
    if v == 'f':
        b.append(FG([P('Take the bridges one at a time through the table: why each matters, what it sustains for the people, what it sustains for the ESRG conditions, and what happens when it weakens.'),  # NEW
                     P('Ask: <em>&ldquo;Which of the four bridges is weakest in your organisation, and what do you see happening as a result?&rdquo;</em>')]))  # NEW
    o.append(PART('2.1', 'Performance Management as the Execution Bridge', 'Four execution bridges', b, True))

    b = [P('The four execution bridges establish the disciplines required to sustain the connection between strategy and results. However, their effectiveness is influenced by the way an organisation approaches performance expectations, accountability and performance conversations.'),
         P('This introduces an important distinction between compliance-driven and commitment-driven performance management architectures.'),
         '<div class="u6-two"><div class="u6-two-c red"><div class="u6-two-h">Compliance-driven architecture</div><p>Emphasises adherence to prescribed expectations, monitoring performance and correcting deviations.</p></div>'
         '<div class="u6-two-c green"><div class="u6-two-h">Commitment-driven architecture</div><p>Emphasises shared understanding of expected results, ownership of contributions, constructive performance dialogue and collective responsibility for improvement.</p></div></div>',
         P('Both approaches recognise the importance of standards and accountability. Their differences become visible in how performance is experienced and how the organisation responds when results fall short.'),
         H4('2.2.1 Four Dimensions of Compliance and Commitment'),
         TABLE(['Dimension', 'Compliance-Driven Architecture', 'Commitment-Driven Architecture'],
               [['<strong>Purpose</strong>', 'Ensure minimum standards are met and deviations corrected.', 'Generate shared ownership of results and continuous improvement.'],
                ['<strong>Ownership</strong>', 'Leader holds accountability; team is subject to it.', 'Team co-owns accountability; leader facilitates.'],
                ['<strong>Tone</strong>', 'Assessment and judgement; hierarchical.', 'Inquiry and problem-solving; collaborative.'],
                ['<strong>PM Experience</strong>', 'Anxiety-producing; done to the individual.', 'Energy-generating; done with the individual.']]),
         H4('2.2.2 Accountability Across the Two Operating Systems'),
         P('The distinction between compliance and commitment applies to both human and organisational performance.'),
         CARDS([('Human', 'Human Operating System', P('A compliance-driven approach tends to emphasise whether employees have met prescribed KPIs, OKRs and behavioural standards.') +
                 P('A commitment-driven approach maintains these expectations while strengthening employees&rsquo; understanding of their contribution, ownership of results and participation in performance improvement.')),
                ('ESRG', 'Organisational Operating System', P('A compliance-driven approach may establish requirements for systems, resources, processes and governance, but concentrate primarily on whether prescribed arrangements have been followed.') +
                 P('A commitment-driven approach also examines whether those arrangements are effective in supporting the intended results and whether emerging constraints are being addressed.'), COL[1], True)]),
         P('This distinction becomes particularly important when performance falls short. An employee may miss a target because of inadequate follow-through, an organisational constraint or a combination of both. A credible performance management system distinguishes between these causes before determining the appropriate response.'),
         HB('Commitment strengthens accountability when employees remain responsible for their contributions and organisational leaders remain equally responsible for the enabling conditions within their authority.')]
    if v == 'f':
        b.append(FG([P('Teach the two architectures first, then the four dimensions, then how each applies to the people and to the ESRG conditions.'),  # NEW
                     P('Ask: <em>&ldquo;When a target is missed in your organisation, which of the two architectures does the review conversation sound like?&rdquo;</em>')]))  # NEW
    o.append(PART('2.2', 'Compliance vs Commitment Architecture', 'The design choice that shapes performance behaviour', b))
    return o


# ─────────────────────────── SECTION 3 ───────────────────────────
def CXO():
    cards, det = [], []
    for i, r in enumerate(HOTZ):
        ab, full = r[0].split(' &mdash; ')
        col = COL[i % len(COL)]
        cards.append('<div class="u6-cx" onclick="u6Cxo(this,%d)" style="border-top-color:%s;"><div class="u6-cx-a" style="color:%s;">%s</div><div class="u6-cx-f">%s</div></div>' % (i, col, col, ab, full))
        det.append('<div class="u6-cxd" id="u6cxd%d"><div class="u6-cxd-h" style="color:%s;">%s &middot; %s</div>%s%s%s</div>' % (
            i, col, ab, full, P('<strong>Natural performance focus:</strong> ' + r[1]), P('<strong>Potential performance blind spot:</strong> ' + r[2]), P('<strong>Enterprise integration requirement:</strong> ' + r[3])))
    return ('<div class="u6t-cap">Select a role to see its performance focus, blind spot and integration requirement</div>'
            '<div class="u6-cxg">' + ''.join(cards) + '</div>' + ''.join(det))



S3_TITLE = 'Executive Performance Integration and the Evolution of Performance Management'
S3_HERO = 'Where does enterprise performance management become vulnerable? How executive performance perspectives and the evolution of performance management practice shape what leaders see and how they respond.'  # NEW (from her section question)
S3_SLO = ['Diagnose executive performance blind spots that affect enterprise results.', 'Assess where current performance management practice sits on the shift to continuous, development-centred and team-based performance.']

HOTZ = [
    ['CEO &mdash; Chief Executive Officer', 'Enterprise results, strategic priorities, organisational performance and long-term sustainability.', 'Accepting positive functional performance reports without establishing whether their combined contributions are producing the intended enterprise outcomes.', 'Integrate functional performance evidence into a coherent view of strategic progress. Identify where collective performance is weakening and coordinate executive responses.'],
    ['CFO &mdash; Chief Financial Officer', 'Financial performance, profitability, cost efficiency, cash flow and returns on investment.', 'Interpreting cost containment or favourable financial variances as success when resource constraints are weakening delivery capability.', 'Establish whether financial decisions and resource allocations sustain the organisational capability required to achieve strategic results.'],
    ['COO &mdash; Chief Operating Officer', 'Operational efficiency, productivity, throughput, quality and delivery reliability.', 'Concentrating on operational efficiency and output targets without establishing whether these outputs are producing the intended customer or enterprise outcomes.', 'Connect operational performance to strategic outcomes and examine dependencies affecting delivery across functions.'],
    ['CHRO &mdash; Chief Human Resources Officer', 'Employee performance, workforce capability, leadership effectiveness, engagement and organisational culture.', 'Concentrating on individual performance achievement, employee development or HR process completion while organisational conditions continue to constrain delivery.', 'Interpret human performance evidence alongside relevant ESRG conditions. Establish whether workforce capability and organisational arrangements support the results expected from people.'],
    ['CIO/CTO &mdash; Chief Information/Technology Officer', 'System reliability, technology performance, digital capability, cybersecurity and information infrastructure.', 'Reporting satisfactory technical performance without establishing whether technology is effectively enabling business processes and strategic delivery requirements.', 'Connect technology measures to the operating requirements of dependent functions and the enterprise outcomes those functions support.'],
    ['CMO &mdash; Chief Marketing Officer', 'Market positioning, brand performance, customer engagement, acquisition and market response.', 'Interpreting strong campaign results, engagement or customer acquisition as success without establishing whether the organisation can deliver and sustain the value promised.', 'Connect market performance to customer experience, operational delivery capability and the organisation&rsquo;s strategic value proposition.'],
    ['CCO &mdash; Chief Commercial Officer', 'Revenue growth, sales conversion, commercial pipeline, customer retention and commercial relationships.', 'Prioritising sales volumes or revenue targets without adequately considering delivery capacity, profitability or the organisation&rsquo;s ability to fulfil commitments.', 'Connect commercial performance to financial sustainability, operational capability and customer value delivery.'],
    ['CPO &mdash; Chief Procurement Officer', 'Procurement efficiency, supplier performance, purchasing costs, supply reliability and contract management.', 'Prioritising purchasing savings or procurement compliance while overlooking the effects of supplier quality, availability or lead times on operational delivery.', 'Establish whether procurement decisions and supplier arrangements support the quality, reliability and timing required for enterprise performance.'],
    ['CRO &mdash; Chief Risk Officer', 'Risk exposure, regulatory compliance, internal controls and governance effectiveness.', 'Concentrating on control compliance or risk avoidance without adequately examining whether governance arrangements are enabling timely and effective execution.', 'Balance risk management requirements with the decision rights, controls and escalation arrangements necessary for reliable delivery.'],
    ['CSO &mdash; Chief Strategy Officer', 'Strategic alignment, strategic initiatives, portfolio priorities and long-term organisational direction.', 'Concentrating on strategic milestones, initiative completion or reported alignment without establishing whether execution is producing the intended strategic outcomes.', 'Connect strategic progress reporting to actual enterprise results, functional contributions and the organisational conditions influencing delivery.']]


def s3(v):
    o = []
    intro = ([] if v == 'p' else [P('Section 2 established the four execution bridges that sustain the connection between strategy and results. It also examined how compliance-driven and commitment-driven approaches influence accountability, performance behaviour and management responses.')]) + [
             P('Section 3 examines where enterprise performance management becomes vulnerable, through two areas:'),
             UL(['<strong>Unity in Diversity:</strong> how executive performance perspectives influence what leaders notice, prioritise and interpret.',
                 '<strong>The Continuous Performance Management Shift:</strong> how performance management practices are evolving to strengthen timely feedback, development and collective performance.'])]
    hot_cards = []
    for i, r in enumerate(HOTZ):
        role = r[0]
        hot_cards.append((role.split(' &mdash; ')[0], role.split(' &mdash; ')[1],
                          P('<strong>Natural performance focus:</strong> ' + r[1]) + P('<strong>Potential performance blind spot:</strong> ' + r[2]) + P('<strong>Enterprise integration requirement:</strong> ' + r[3]),
                          COL[i % len(COL)]))
    b = intro + [
        P('Enterprise performance management depends on the collective contribution of executive leaders who hold different responsibilities. Each executive function develops a particular understanding of performance based on its mandate, expertise, operating priorities and the evidence it routinely examines. These perspectives are necessary because enterprise performance is multidimensional.'),
        P('This reflects the principle of functional bias, introduced earlier in CESI: leaders may interpret organisational situations primarily through the priorities and assumptions associated with their professional responsibilities. Within enterprise performance management, functional bias can influence:'),
        UL(['<strong>What executives notice:</strong> the performance indicators and developments that attract their attention.',
            '<strong>What executives prioritise:</strong> the results, risks and improvements they consider most important.',
            '<strong>How executives interpret evidence:</strong> the conclusions they draw about organisational performance and its underlying causes.']),
        P('The challenge for executive teams is to bring these perspectives together so that functional performance information supports a coherent understanding of enterprise results.'),
        HB('<strong>Unity in Diversity</strong> means integrating different executive performance perspectives into one collective understanding of enterprise progress.'),
        H4('3.1.1 The Ten Executive Performance Hot Zones'),
        P('The ten executive performance perspectives below show the blind spots each may create and the integration required to support enterprise results. The executive team must establish whether the performance reported by individual functions is sufficient to produce the intended collective outcome. This requires attention to both operating systems.'),
        CARDS([('Human', 'Human Operating System', P('Executives examine whether individuals and teams are delivering their agreed KPIs, OKRs and behavioural expectations. They also consider whether the required contributions are being coordinated effectively across functions.')),
               ('ESRG', 'Organisational Operating System', P('Executives examine whether the relevant Environment, Systems, Resources and Governance conditions are enabling those contributions. Where organisational constraints affect delivery, the appropriate executive owners must take responsibility for resolving them.'), COL[1], True),
               ('Enterprise', 'Enterprise Integration', P('The executive team brings the evidence together to determine:') +
                UL(['whether functional performance is supporting the intended enterprise result;', 'where human contribution or organisational capability is weakening delivery;', 'which executive decisions or coordinated interventions are required.']), COL[2], True)]),
        P('The ' + SR + ' provides the established relationships between contributions. The four execution bridges provide the disciplines for sustaining those relationships. Executive integration ensures that the resulting performance evidence is interpreted and acted upon collectively.'),
        HB('<strong>Key insight:</strong> executive performance integration requires leaders to recognise the limits of their functional perspectives and use collective performance evidence to make decisions in the interests of enterprise results.'),
        CXO(),
        P('<em>Executive titles and responsibilities vary between organisations. The table illustrates functional perspectives. Each organisation reads it against its own executive structure.</em>')]
    if v == 'f':
        b.append(FG([P('Teach functional bias first: what executives notice, prioritise and interpret. Then open the role cards, starting with the CEO, and read the natural focus, the blind spot and the integration requirement of each.'),  # NEW
                     P('Ask: <em>&ldquo;Which blind spot do you recognise in your own executive team, and what does it cost the enterprise result?&rdquo;</em>')]))  # NEW
    o.append(PART('3.1', 'Unity in Diversity: Executive Performance Perspectives', 'Different executive perspectives, one enterprise result', b, True))

    b = [P('Organisations are increasingly recognising the limitations of performance management systems built primarily around periodic assessments and individual ratings. Three important shifts are influencing how performance management is approached.'),
         H4('3.2.1 Three Shifts in Performance Management Practice'),
         TABLE(['Performance Management Shift', 'Traditional Orientation', 'Evolving Orientation', 'Implication for the Two Operating Systems'],
               [['<strong>1. From Annual to Continuous</strong>', 'Performance is formally evaluated at annual or biannual intervals.', 'Regular check-ins, periodic reviews and timely feedback support performance throughout execution.', 'Human contributions and relevant ESRG conditions are reviewed frequently enough to identify emerging gaps and influence results.'],
                ['<strong>2. From Rating-Centric to Development-Centric</strong>', 'Performance conversations concentrate heavily on ratings and historical achievement.', 'Performance evidence informs development, capability strengthening and future improvement.', 'Individual development is considered alongside improvements to organisational processes, systems, resources and governance arrangements.'],
                ['<strong>3. From Individual to Team Performance</strong>', 'Performance assessment concentrates primarily on individual achievement.', 'Individual accountability is complemented by attention to team and cross-functional contributions.', 'Human collaboration and organisational dependencies become more visible within the performance management system.']]), END,
         P('These developments reinforce the importance of managing performance while execution is unfolding. They also broaden the performance management conversation:'),
         UL(['Employee development remains important, but organisations must also improve the operating conditions that influence performance.',
             'Individual accountability remains necessary, but enterprise results often require coordinated contributions across teams and functions.',
             'Periodic assessments remain relevant, but they must be supported by timely performance conversations that allow leaders to respond to emerging challenges.']),
         HB('<strong>Key insight:</strong> continuous performance management strengthens the organisation&rsquo;s ability to recognise, interpret and respond to performance conditions while there is still an opportunity to influence results.')]
    if v == 'f':
        b.append(FG([P('Walk through the three shifts, then the implication of each for the two operating systems.'),  # NEW
                     P('Ask: <em>&ldquo;Where does your organisation sit on each of the three shifts today?&rdquo;</em>')]))  # NEW
    b.append(ref_block(v, 'ref12', '3.2'))
    o.append(PART('3.2', 'The Continuous Performance Management Shift', 'How performance management practices are evolving', b))
    return o


# ─────────────────────────── SECTION 4 ───────────────────────────
S4_TITLE = 'Integration of Human and Organisational Performance'
S4_HERO = 'One worked example brings the unit together: the contributions an enterprise Key Result requires, mapped across four functions, and how FACES manages them.'  # NEW
S4_SLO = ['Map enterprise performance requirements across functional, human and organisational contributions.', 'Determine how those contributions are managed across business functions towards an enterprise result.']

MAP_ROWS = [
    ['<strong>Customer Service</strong>', 'Resolve customer enquiries accurately and within 48 hours.', 'Employees resolve assigned enquiries, follow up on outstanding cases and escalate delays requiring support from other functions.',
     '<strong>Resolution:</strong> &ge;90% of enquiries within employees&rsquo; control resolved within 48 hours.<br><strong>Follow-through:</strong> &ge;95% of outstanding enquiries followed up within the agreed period.',
     '<strong>Systems:</strong> An enquiry management system that records ownership, progress and resolution times.<br><strong>Governance:</strong> Clear escalation authority for enquiries requiring decisions outside Customer Service.',
     '<strong>Systems:</strong> Enquiry records provide complete timestamps and assigned ownership.<br><strong>Governance:</strong> Documented escalation routes and named decision owners.'],
    ['<strong>IT</strong>', 'Maintain reliable customer management systems to support uninterrupted enquiry processing.', 'IT employees monitor system performance, respond to incidents and restore disrupted services.',
     '<strong>Incident resolution:</strong> &ge;95% of critical incidents resolved within two hours.<br><strong>Communication:</strong> &ge;95% of confirmed critical incidents communicated to affected departments within 15 minutes.',
     '<strong>Systems:</strong> Reliable infrastructure and monitoring capability to maintain system availability.<br><strong>Resources:</strong> Sufficient technical support coverage during service hours.',
     '<strong>Systems:</strong> &ge;99% customer management system availability during service hours.<br><strong>Resources:</strong> Approved technical support roster covering required service hours.'],
    ['<strong>Operations</strong>', 'Complete internal processing and approvals within the turnaround required for customer resolution.', 'Employees process assigned requests accurately and escalate exceptions that could delay customer resolution.',
     '<strong>Turnaround:</strong> &ge;95% of assigned requests completed within eight working hours.<br><strong>Accuracy:</strong> &ge;98% processing accuracy.',
     '<strong>Governance:</strong> Approval authority must be assigned at the appropriate level to prevent avoidable delays.<br><strong>Systems:</strong> Processing workflows must support timely handovers between Operations and Customer Service.',
     '<strong>Governance:</strong> Documented approval limits and designated decision owners.<br><strong>Systems:</strong> &ge;95% of internal processing requests completed within the agreed turnaround time.'],
    ['<strong>HR / Workforce Planning</strong>', 'Ensure customer-facing operations have sufficient staffing capacity and capabilities to meet enquiry demand.', 'Workforce Planning employees forecast staffing requirements, prepare schedules and coordinate responses to identified capacity gaps.',
     '<strong>Planning:</strong> 100% of staffing schedules completed before the agreed deadline.<br><strong>Responsiveness:</strong> &ge;95% of identified staffing gaps addressed within the agreed response period.',
     '<strong>Resources:</strong> Sufficient qualified staff available to meet forecast customer enquiry volumes.<br><strong>Governance:</strong> Authority to approve staffing adjustments when demand exceeds available capacity.',
     '<strong>Resources:</strong> &ge;95% staffing coverage against demand-based requirements.<br><strong>Governance:</strong> Agreed staffing adjustment authority and escalation arrangements.']]
MAP_HEAD = ['Business Function', 'Required Functional Contribution', 'Human Operating System (HOS) &mdash; Required Contribution', 'HOS &mdash; Performance Metric', 'Organisational Operating System &mdash; Required ESRG Contribution', 'ESRG &mdash; Measure or Evidence of Readiness']

FACES_FN_ROWS = [
    ['<strong>F &mdash; Foster a Results Culture</strong>',
     'Customer enquiries have clear ownership through to resolution. Employees discuss outstanding commitments, explain delays and recognise colleagues who consistently deliver reliable service. Managers demonstrate the same ownership by addressing obstacles raised by their teams.',
     'System incidents are openly reviewed to understand what happened, how the team responded and what must improve. Employees raise emerging reliability risks early, while IT leadership follows through on recurring infrastructure problems.',
     'Processing delays and errors are discussed openly, with attention to their consequences for customer resolution. Employees raise potential bottlenecks early, and managers respond to reported constraints so that they do not recur.',
     'Staffing gaps are discussed as performance risks requiring action. Workforce Planning and operational managers jointly examine whether available capacity can meet expected demand and raise emerging shortages before service delivery is affected.'],
    ['<strong>A &mdash; Align Performance</strong>',
     'Individual resolution and follow-through commitments are linked to the enterprise 48-hour target. The enquiry management system and escalation arrangements are checked against the requirements for timely resolution.',
     'Incident-resolution and communication commitments are linked to the required system availability. Technical support arrangements are matched to the service hours and reliability requirements established in the Contribution Map.',
     'Processing turnaround and accuracy expectations are agreed in relation to the time available for customer enquiry resolution. Workflows and approval authority are checked to ensure they support the required turnaround.',
     'Staffing forecasts and schedules are based on expected enquiry volumes and the service capacity required. Staffing coverage requirements are agreed with the operational functions that depend on them.'],
    ['<strong>C &mdash; Create Measurement Transparency</strong>',
     'Resolution and follow-through results are visible against agreed standards. Outstanding enquiries show their assigned owners, elapsed time and any unresolved dependencies on other functions.',
     'Incident-response results and system availability are reported together. The evidence distinguishes how effectively employees respond to incidents from whether the infrastructure is delivering the required reliability.',
     'Processing reports show turnaround, accuracy and the causes of delays. Approval waiting times are visible alongside employee processing performance.',
     'Staffing schedules, forecast demand and actual staffing coverage are reviewed together. The evidence shows whether scheduling commitments have been fulfilled and whether sufficient qualified employees are available.'],
    ['<strong>E &mdash; Embed Shared Accountability</strong>',
     'Each enquiry has an assigned owner responsible for follow-through. Delays requiring IT, Operations or staffing support are recorded against the responsible function, with agreed escalation and resolution arrangements.',
     'Incident owners are responsible for response and communication commitments. IT leadership is responsible for system reliability and for securing decisions or resources needed to correct infrastructure constraints.',
     'Processing responsibilities are assigned to employees and supervisors. Approval delays are referred to the managers who control the relevant decision rights, with unresolved constraints escalated to the Operations Executive.',
     'Workforce Planning is responsible for forecasts, schedules and coordinating staffing adjustments. Operational managers confirm their staffing requirements, while decisions on additional capacity are referred to the appropriate resource authority.'],
    ['<strong>S &mdash; Support Continuous Development</strong>',
     'Repeated follow-through gaps are examined using actual enquiry records. Coaching addresses employee capability gaps, while recurring problems with case tracking or escalation lead to improvements in the supporting arrangements. Subsequent results establish whether performance has improved.',
     'Incident trends identify technical skills requiring development and recurring infrastructure weaknesses requiring correction. Subsequent incident-response and availability results show whether the improvements have strengthened service reliability.',
     'Processing errors inform targeted employee development. Recurring workflow and approval delays inform process or governance improvements. Changes are evaluated against turnaround and accuracy performance.',
     'Differences between forecast and actual demand inform improvements to workforce planning. Recurring staffing shortages lead to adjustments in scheduling, deployment or capacity arrangements, with staffing coverage used to evaluate their effectiveness.']]


def s4(v):
    o = []
    b = ([P('The previous sections established the foundations of enterprise performance management, the disciplines that sustain execution and the importance of integrating executive performance perspectives. We now bring these concepts together through a worked example.'),
          P('The ' + SR + ' establishes the interconnected contributions required to achieve an enterprise result. It identifies what each function must deliver, the performance expected from individuals and teams, and the organisational conditions necessary to enable those contributions. The following example demonstrates how these requirements are connected across four business functions.')] if v == 'f' else
         [P('This worked example brings the unit together: one enterprise Key Result, mapped across four business functions. For each function, the map shows what the function must deliver, what its people must deliver and the organisational conditions that enable them.')]) + [
         H4('4.1.1 Worked Example: Improving Customer Service')]
    if v == 'f':
        b.append(FG([OL(['<strong>Establish the enterprise result.</strong> Begin with the enterprise key result: <em>&ldquo;Increase customer enquiries resolved within 48 hours from 65% to 90% by year-end.&rdquo;</em> Ask: <em>&ldquo;Which functions must contribute to achieving this result?&rdquo;</em> Draw attention to Customer Service, IT, Operations and Workforce Planning.',
                          '<strong>Walk through the Contribution Map.</strong> Use Customer Service to demonstrate the distinction between the functional contribution, human performance and organisational enablement. Emphasise that the enterprise target covers all customer enquiries, while the employee resolution measure covers enquiries within employees&rsquo; control. Then examine the remaining functions, highlighting how their contributions support the same enterprise result.',
                          '<strong>Examine the measures.</strong> Ask: <em>&ldquo;Why do we measure both employee incident-response performance and system availability in IT?&rdquo;</em> Guide participants to recognise that employees may fulfil their responsibilities while the underlying organisational capability remains inadequate.',
                          '<strong>Consolidate the learning.</strong> Say: <em>&ldquo;The Contribution Map gives us an integrated view of what must be delivered and enabled across the organisation. It establishes the performance requirements against which contributions can be assessed.&rdquo;</em>'])]))
    b += ['<div class="u6-from"><b>Enterprise Objective</b>Deliver a reliable and responsive customer service experience.</div>',
          '<div class="u6-from"><b>Enterprise Key Result</b>Increase customer enquiries resolved within 48 hours from 65% to 90% by year-end.</div>',
          TABLE(MAP_HEAD, MAP_ROWS, 'The ' + SR + ' &middot; worked example'),
          P('<em>Performance targets are illustrative. The purpose is to establish sufficient evidence to determine whether the required contribution is being delivered and whether the organisation is enabling it.</em>'),
          H4('4.1.2 Interpreting the Contribution Map'),
          P('The Contribution Map establishes the relationship between three elements.'),
          CARDS([('1', 'Functional Contribution &mdash; What must the function deliver?', P('Each function has a defined contribution to the enterprise key result.')),
                 ('2', 'Human Operating System &mdash; What must individuals and teams deliver?', P('The map identifies the results and behaviours required from people, supported by measurable performance expectations wherever practical.')),
                 ('3', 'Organisational Operating System &mdash; What conditions must the organisation provide?', P('The map identifies the relevant ESRG requirements necessary to enable the human contribution.'))]),
          P('Only the ESRG elements that materially affect delivery are included. Some require numerical performance measures, such as system availability or staffing coverage. Others require evidence that an arrangement or capability exists and is functioning, such as documented approval authority or established escalation procedures.'),
          ]
    o.append(PART('4.1', 'Mapping the Contributions Required for Enterprise Results', 'Worked example: improving customer service', b, True))

    b = ([P('The Contribution Map&trade; has established the contributions required from Customer Service, IT, Operations and Workforce Planning, including the expected human performance and the organisational conditions necessary to enable delivery. The next requirement is to manage these contributions consistently throughout execution.'),
          P('FACES provides the five management functions through which performance expectations are aligned, evidence is examined, accountability is maintained and improvement is supported. The following example demonstrates how each FACES function is achieved in practice across the four business functions.')] if v == 'f' else
         [P('The map in part 4.1 shows what Customer Service, IT, Operations and Workforce Planning must contribute. FACES shows how those contributions are managed throughout execution, function by function.')]) + [
         H4('4.2.1 Applying FACES Across the Four Functions')]
    if v == 'f':
        b.append(FG([OL(['<strong>Connect FACES to the Contribution Map.</strong> Say: <em>&ldquo;In the first part of this example, we established what each function must contribute and what the organisation must enable. We now examine how these contributions are managed. FACES provides the five management functions required to sustain delivery.&rdquo;</em>',
                          '<strong>Demonstrate how FACES operates across functions.</strong> Begin with Customer Service and work through the five FACES functions. Then select IT to demonstrate how the same management functions apply to different performance responsibilities. Emphasise that FACES applies to both employee contributions and organisational enabling conditions.',
                          '<strong>Examine shared accountability.</strong> Ask: <em>&ldquo;If Customer Service employees are meeting their performance commitments but system outages continue to delay customer resolution, who must take responsibility for the performance gap?&rdquo;</em> Guide participants to distinguish employee accountability from the organisational responsibility for system reliability.',
                          '<strong>Connect management action to improvement.</strong> Ask: <em>&ldquo;What should happen when performance reviews repeatedly identify the same approval delays or staffing shortages?&rdquo;</em> Emphasise that performance management must lead to appropriate decisions, assigned responsibilities and follow-through.',
                          '<strong>Consolidate the learning.</strong> Say: <em>&ldquo;The Contribution Map establishes the contributions, performance measures and enabling conditions required for enterprise results. FACES establishes the management disciplines through which those contributions are aligned, evaluated, acted upon and continuously strengthened.&rdquo;</em>'])]))
    b += [TABLE(['FACES Function', 'Customer Service', 'IT', 'Operations', 'HR / Workforce Planning'], FACES_FN_ROWS, 'FACES across the four functions &middot; worked example'),
          H4('4.2.2 Interpreting the Worked Example'),
          P('FACES operates through five connected disciplines:'),
          CARDS([('F', 'Foster', P('Performance commitments and delivery obstacles are discussed openly, with consistent follow-through from employees and leaders.')),
                 ('A', 'Align', P('Human contributions and organisational conditions are connected to the requirements of the enterprise key result.')),
                 ('C', 'Create Measurement Transparency', P('Performance evidence makes both employee contributions and organisational constraints visible.')),
                 ('E', 'Embed Shared Accountability', P('Responsibilities for delivering contributions and resolving constraints are assigned to the people and functions with the relevant authority.')),
                 ('S', 'Support Continuous Development', P('Performance findings lead to improvements in employee capability and organisational operating conditions, with subsequent results used to evaluate progress.'))]),
          HB('Together, these disciplines ensure that the contributions established in the ' + SR + ' are actively managed towards the enterprise result.'),
          ]
    o.append(PART('4.2', 'Managing the Contributions Through FACES', 'Applying FACES across the four functions', b))
    return o


# ─────────────────────────── SECTION 5 ───────────────────────────
S5_TITLE = 'Building Your Enterprise Performance Management System'
S5_HERO_P = 'Your group builds two connected components of the Enterprise Performance Management System for the strategy in your team&rsquo;s Capstone Blueprint: the ' + SR + ' and the FACES application.'
S5_HERO_F = 'Application &middot; Each group builds two connected components of the Enterprise Performance Management System for the strategy in its Capstone Blueprint: the ' + SR + ' and the FACES application.'
S5_SLO = ['Design the functional, human and organisational contributions an enterprise Key Result requires.', 'Establish how those contributions will be managed across business functions.']

FIELD_GUIDE = [['Business Function', 'The department or function responsible for contributing to the enterprise Key Result.'],
               ['Required Functional Contribution', 'The specific result the function must deliver.'],
               ['HOS &mdash; Required Contribution', 'The work, results or behaviours expected from individuals and teams.'],
               ['HOS &mdash; Performance Measure', 'One or two KPIs, OKRs or observable behavioural measures that demonstrate the required contribution.'],
               ['Required ESRG Contribution', 'The critical organisational conditions needed to enable performance. Identify the relevant Environment, Systems, Resources or Governance requirements.'],
               ['ESRG &mdash; Measure or Evidence', 'A measure or evidence showing whether the required organisational conditions are available and functioning effectively.']]
FACES_Q = [['F', 'Foster a Results Culture', 'What routine or leadership practice will reinforce ownership of performance commitments and delivery obstacles?', 'How will employees and leaders demonstrate ownership of results?'],
           ['A', 'Align Performance', 'How will the function&rsquo;s performance expectations and enabling conditions remain connected to the enterprise Key Result?', 'How will human contributions and organisational conditions remain aligned with the enterprise Key Result?'],
           ['C', 'Create Measurement Transparency', 'What evidence will make both human performance and organisational constraints visible?', 'How will human performance and ESRG effectiveness be made visible?'],
           ['E', 'Embed Shared Accountability', 'Who will own performance commitments, enabling conditions and decisions required to address performance gaps?', 'Who will be responsible for contributions, enabling conditions and corrective decisions?'],
           ['S', 'Support Continuous Development', 'How will performance findings be used to strengthen employee capability and organisational effectiveness?', 'How will performance findings lead to improvements in human capability and organisational conditions?']]
MAP_FIELDS = [('contrib', 'Required Functional Contribution', 'What must this function deliver?'),
              ('hos', 'Human Operating System &middot; Required Contribution', 'What must individuals or teams deliver?'),
              ('hosm', 'Human Operating System &middot; Performance Measure', 'How will their contribution be measured?'),
              ('esrg', 'Organisational Operating System &middot; Required ESRG Contribution', 'What Environment, Systems, Resources or Governance conditions are required?'),
              ('esrgm', 'Organisational Operating System &middot; ESRG Measure or Evidence', 'How will the effectiveness or readiness of these conditions be assessed?')]
CHECK1 = ['Each functional contribution supports the selected enterprise Key Result.',
          'Human performance expectations are clearly distinguished from organisational enabling conditions.',
          'Each contribution has an appropriate measure or evidence of performance.']
CHECK2 = ['All five FACES functions have been addressed for each business function.',
          'Your responses describe practical management arrangements.',
          'Your FACES application uses the contributions and performance requirements established in Activity 1.']
CLOSE = ['The ' + SR + ' establishes the contributions required to achieve an enterprise result.',
         'FACES establishes how those contributions will be managed across the organisation.',
         'Together, they connect enterprise strategy to functional performance, human contribution, organisational enablement and collective accountability.']
GROUP_P = '<div class="u6-group"><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</div>'


def s5_intro(v):
    if v == 'p':
        return ('<div class="u6-how"><div class="u6-how-h">How Section 5 works</div>'
                '<p>You have already established your capstone organisation&rsquo;s strategic direction, strategic objectives and Key Results. In this application, your group uses that work to develop two connected components of your Enterprise Performance Management System:</p>'
                '<ol><li><strong>5.1 &middot; Activity 1 &middot; ' + SR + '.</strong> Establish what each business function must contribute, what individuals and teams must deliver, and what organisational conditions must enable performance.</li>'
                '<li><strong>5.2 &middot; Activity 2 &middot; FACES Application.</strong> Establish how these contributions will be aligned, measured, managed and continuously improved.</li></ol>'
                '<p>This is group work and Capstone work. Your page saves as you type. When both activities are complete, each member reads the record and selects Confirm. The confirmed record feeds your team&rsquo;s Capstone Blueprint. Print gives a copy.</p></div>')
    return ('<div class="u6-how"><div class="u6-how-h">How Section 5 works</div>'
            '<p>Each group has already established its capstone organisation&rsquo;s strategic direction, strategic objectives and Key Results. In this application, the group uses that work to develop two connected components of its Enterprise Performance Management System:</p>'
            '<ol><li><strong>5.1 &middot; Activity 1 &middot; ' + SR + '.</strong> Establish what each business function must contribute, what individuals and teams must deliver, and what organisational conditions must enable performance.</li>'
            '<li><strong>5.2 &middot; Activity 2 &middot; FACES Application.</strong> Establish how these contributions will be aligned, measured, managed and continuously improved.</li></ol>'
            '<p>This is group work and Capstone work. The confirmed record feeds the team&rsquo;s Capstone Blueprint.</p></div>')


def tx_attr(s):
    return s.replace('&rsquo;', '’')


def ta(fid, label, ph, minh=None):
    st = ' style="min-height:%dpx;"' % minh if minh else ''
    return '<div><label class="wp-label" for="u6_%s">%s</label><textarea class="wp-ta" id="u6_%s" data-u6="%s" placeholder="%s"%s></textarea></div>' % (fid, label, fid, fid, ph, st)


def s5_p():
    o = [s5_intro('p'),
         '<div class="step-tabs">'
         '<div class="step-tab active" onclick="u6Step(0)"><div class="step-num">5.1 &middot; Activity 1</div><div class="step-name">Contribution Map</div></div>'
         '<div class="step-tab" onclick="u6Step(1)"><div class="step-num">5.2 &middot; Activity 2</div><div class="step-name">FACES Application</div></div></div>']
    # Activity 1
    a = ['<div class="step-panel active" id="u6sp1">',
         '<div class="u6-h" style="margin-top:4px;">5.1 &mdash; Activity 1: Build Your ' + SR + '</div>',
         GROUP_P,
         '<div class="u6-how"><div class="u6-how-h">Capstone work &middot; How to complete Activity 1</div><ol>'
         '<li><strong>Step 1 &middot; Select your enterprise Key Result.</strong> Choose an Objective from your group&rsquo;s Unit 3 OKRs, then one of its Key Results that requires contributions from several business functions.</li>'
         '<li><strong>Step 2 &middot; Complete your Contribution Map.</strong> Identify three or four business functions that must contribute to the selected Key Result. For each function, complete the six fields. The worked example is in part 4.1.</li>'
         '<li>Read the completion check, then go to Activity 2.</li></ol></div>',
         '<div class="u6-h">Step 1 &middot; Select your enterprise Key Result</div>',
         '<div class="u6-g2" style="margin:6px 0 10px;"><div><label class="wp-label" for="u6_obj">Objective &middot; from your group&rsquo;s Unit 3 OKRs</label><select class="u6-sel" id="u6_obj" data-u6="kr_obj"></select></div>'
         '<div><label class="wp-label" for="u6_kr">Enterprise Key Result</label><select class="u6-sel" id="u6_kr" data-u6="kr"></select></div></div>',
         '<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Bring(true)">Bring in from my Unit 3 page</button></div>',
         '<div class="u6-note" id="u6BringMsg" style="display:none;"></div>',
         '<div class="u6-h">Step 2 &middot; Complete your Contribution Map</div>']
    for n in range(1, 5):
        opt = ' (optional)' if n == 4 else ''
        a.append('<div class="u6-s5" id="u6fn%d"><div class="u6-s5-h"><span class="u6-s5-n">Function %d%s</span><span class="u6-s5-q u6-fn%d-t"></span></div>' % (n, n, opt, n))
        a.append('<div><label class="wp-label" for="u6_f%d_name">Business Function</label><input class="u6-in" type="text" id="u6_f%d_name" data-u6="f%d_name" placeholder="The department or function, for example Customer Service"></div>' % (n, n, n))
        a.append('<div class="u6-g1">' + ta('f%d_contrib' % n, MAP_FIELDS[0][1], MAP_FIELDS[0][2]) + '</div>')
        a.append('<div class="u6-h" style="margin:14px 0 6px;">Human Operating System</div><div class="u6-g2">' + ta('f%d_hos' % n, 'Required Contribution', MAP_FIELDS[1][2]) + ta('f%d_hosm' % n, 'Performance Measure', MAP_FIELDS[2][2]) + '</div>')
        a.append('<div class="u6-h" style="margin:14px 0 6px;">Organisational Operating System &middot; ESRG</div><div class="u6-g2">' + ta('f%d_esrg' % n, 'Required ESRG Contribution', MAP_FIELDS[3][2]) + ta('f%d_esrgm' % n, 'Measure or Evidence', MAP_FIELDS[4][2]) + '</div>')
        a.append('</div>')
    a += ['<div class="u6-how"><div class="u6-how-h">Completion check</div><p>Before you go on, confirm that:</p>' + OL(CHECK1) + '<p><strong>Output 1:</strong> your completed ' + SR + '.</p></div>',
          '<div class="u6-btnrow"><button type="button" class="u6-b" onclick="u6Step(1)">Continue to Activity 2 &rarr;</button></div>',
          '</div>']
    o += a
    # Activity 2
    a = ['<div class="step-panel" id="u6sp2">',
         '<div class="u6-h" style="margin-top:4px;">5.2 &mdash; Activity 2: Apply FACES to Your Contribution Map&trade;</div>',
         GROUP_P,
         '<div class="u6-how"><div class="u6-how-h">Capstone work &middot; How to complete Activity 2</div><ol>'
         '<li>You have established the contributions required to achieve your enterprise Key Result. Now apply FACES to determine how these contributions will be managed.</li>'
         '<li><strong>Step 3 &middot; Complete your FACES application.</strong> The business functions you named in Activity 1 are shown below. For each business function, describe one practical management arrangement for each FACES function. Each box carries its question; the worked example is in part 4.2.</li>'
         '<li>Read the completion check, then read your group&rsquo;s record and select Confirm.</li></ol></div>',
         '<div class="u6-from" id="u6KrShow2"></div>',
         '<div class="u6-h">Step 3 &middot; Complete your FACES application</div>']
    for n in range(1, 5):
        opt = ' (optional)' if n == 4 else ''
        a.append('<div class="u6-s5" id="u6fx%d"><div class="u6-s5-h"><span class="u6-s5-n">Function %d%s</span><span class="u6-s5-q u6-fn%d-t"></span></div>' % (n, n, opt, n))
        for q in FACES_Q:
            a.append('<div class="u6-g1">' + ta('f%d_%s' % (n, q[0]), q[0] + ' &mdash; ' + q[1], tx_attr(q[2]), 70) + '</div>')
        a.append('</div>')
    a += ['<div class="u6-how"><div class="u6-how-h">Completion check</div><p>Before you confirm, check that:</p>' + OL(CHECK2) + '</div>',
          HB('<br>'.join(CLOSE)),
          '</div>']
    o += a
    o.append('<div id="u6Rec"></div>')
    return '\n'.join(o)


def s5_f():
    o = [FG([P('<strong>Order:</strong> both activities are group work and Capstone work. Activity 1 needs the group&rsquo;s confirmed Enterprise OKRs from Unit 3, part 4.2. Activity 2 uses the business functions the group names in Activity 1.'),  # NEW
             P('<strong>How to guide the work:</strong> brief each activity from the worked example in Section 4, then let the groups work through the steps on their own pages. One member acts as scribe; every member types the agreed entries into their own page.')],  # NEW
            'FACILITATOR GUIDANCE &mdash; Section 5 &middot; Application'),
         s5_intro('f'),
         '<div class="step-tabs">'
         '<div class="step-tab active" onclick="u6Step(0)"><div class="step-num">5.1 &middot; Activity 1</div><div class="step-name">Contribution Map</div></div>'
         '<div class="step-tab" onclick="u6Step(1)"><div class="step-num">5.2 &middot; Activity 2</div><div class="step-name">FACES Application</div></div></div>',
         '<div class="step-panel active" id="u6sp1">',
         '<div class="u6-h" style="margin-top:4px;">5.1 &mdash; Activity 1: Build Your ' + SR + '</div>',
         FG([P('<strong>Briefing:</strong> each group selects one enterprise Key Result from its Unit 3 Objectives and Key Results that requires contributions from several business functions. It then identifies three or four business functions and completes the six fields for each. Point the groups to the field guidance and to the worked example in part 4.1.')], 'FACILITATOR GUIDANCE &mdash; Activity 1'),  # NEW
         '<div class="u6-h">Step 1 &middot; Select your enterprise Key Result</div>',
         P('The group&rsquo;s Objectives and Key Results from Unit 3 are in two drop-down lists on each participant&rsquo;s page: the Objective first, then its Key Results. For the purposes of the programme, the group selects one enterprise Key Result from its capstone strategy that requires contributions from several business functions.'),
         '<div class="u6-h">Step 2 &middot; Complete your Contribution Map</div>',
         TABLE(['Field', 'What to enter'], FIELD_GUIDE, 'Guidance for completing the map'),
         P('The group identifies three or four business functions that must contribute to the selected Key Result and completes the six fields in the template for each function.'),
         TABLE(['Business Function', 'Required Functional Contribution', 'Human Operating System &mdash; Required Contribution', 'Human Operating System &mdash; Performance Measure', 'Organisational Operating System &mdash; Required ESRG Contribution', 'Organisational Operating System &mdash; ESRG Measure or Evidence'],
               [['Function 1', '<em>What must this function deliver?</em>', '<em>What must individuals or teams deliver?</em>', '<em>How will their contribution be measured?</em>', '<em>What Environment, Systems, Resources or Governance conditions are required?</em>', '<em>How will the effectiveness or readiness of these conditions be assessed?</em>'],
                ['Function 2', '', '', '', '', ''], ['Function 3', '', '', '', '', ''], ['Function 4 (optional)', '', '', '', '', '']], 'The template on each participant&rsquo;s page (Enterprise Key Result shown from Step 1)'),
         '<div class="u6-how"><div class="u6-how-h">Completion check</div><p>Before proceeding, the group confirms that:</p>' + OL(CHECK1) + '<p><strong>Output 1:</strong> the completed ' + SR + '.</p></div>',
         PACT([P('Participants work as a group, in Activity 1 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'),
               OL(['The group chooses an Objective from its Unit 3 OKRs, then one of its Key Results that requires contributions from several business functions, from the two drop-down lists on each page.',
                   'The group identifies three or four business functions that must contribute to that Key Result.',
                   'For each function, the group completes the six fields: business function, required functional contribution, Human Operating System required contribution and performance measure, required ESRG contribution and its measure or evidence.',
                   'The group reads the completion check, then goes to Activity 2.'])]),
         '</div>',
         '<div class="step-panel" id="u6sp2">',
         '<div class="u6-h" style="margin-top:4px;">5.2 &mdash; Activity 2: Apply FACES to Your Contribution Map&trade;</div>',
         FG([P('<strong>Briefing:</strong> each group applies FACES to the contributions it mapped in Activity 1. For each business function it describes one practical management arrangement for each FACES function. Point the groups to the application questions and to the worked example in part 4.2.')], 'FACILITATOR GUIDANCE &mdash; Activity 2'),  # NEW
         P('The group has established the contributions required to achieve its enterprise Key Result. It now applies FACES to determine how these contributions will be managed. The business functions named in Activity 1 are shown in the FACES template on each participant&rsquo;s page.'),
         '<div class="u6-h">Step 3 &middot; Complete your FACES application</div>',
         TABLE(['FACES Function', 'Application Question'], [['<strong>' + q[0] + ' &mdash; ' + q[1] + '</strong>', q[2]] for q in FACES_Q], 'Guidance for applying FACES'),
         TABLE(['FACES Function', 'Function 1', 'Function 2', 'Function 3', 'Function 4 (if applicable)'],
               [['<strong>' + q[0] + ' &mdash; ' + q[1] + '</strong>', '<em>' + q[3] + '</em>', '', '', ''] for q in FACES_Q], 'The template on each participant&rsquo;s page (Enterprise Key Result shown from Activity 1)'),
         '<div class="u6-how"><div class="u6-how-h">Completion check</div><p>Before confirming, the group checks that:</p>' + OL(CHECK2) + '</div>',
         HB('<br>'.join(CLOSE)),
         PACT([P('Participants work as a group, in Activity 2 of their own file. This is Capstone work. The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.'),
               OL(['For each business function named in Activity 1, the group describes one practical management arrangement for each of the five FACES functions.',
                   'The group reads the completion check.',
                   'Each participant reads the record and selects Confirm. Print gives a copy.']),
               P('The confirmed record feeds the team&rsquo;s Capstone Blueprint.')]),
         '</div>']
    return '\n'.join(o)


# ─────────────────────────── Facilitator Guide tab, Unit Summary ───────────────────────────
FGUIDE = ('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>'
          '<p>Unit 6 sets up enterprise performance management on two operating systems: what people deliver (the Human Operating System) and what the organisation enables (the Organisational Operating System, examined through ESRG). Participants learn the ' + SR + ', which connects an enterprise Key Result to the contributions of business functions, people and organisational conditions, and FACES, the five functions through which those contributions are managed. In Section 5 each group builds both for its own Capstone strategy.</p></div>\n'
          '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Key Facilitation Questions</div><ul>'
          '<li><em>&ldquo;If your organisation stopped producing its performance reports tomorrow, which decisions would leaders no longer be able to make?&rdquo;</em></li>'
          '<li><em>&ldquo;When a target is missed, how do you distinguish an individual contribution problem from an organisational delivery problem?&rdquo;</em></li>'
          '<li><em>&ldquo;Which functions must contribute to achieving this result?&rdquo;</em></li>'
          '<li><em>&ldquo;If employees are meeting their performance commitments but system outages continue to delay customer resolution, who must take responsibility for the performance gap?&rdquo;</em></li>'
          '<li><em>&ldquo;What should happen when performance reviews repeatedly identify the same approval delays or staffing shortages?&rdquo;</em></li>'
          '</ul></div>\n'
          '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Tone &amp; Watch Points</div>'
          '<p><strong>Avoid:</strong> turning the Contribution Map or FACES into a compliance checklist. They are design and management tools.</p>'
          '<p><strong>Watch for:</strong> a missed target read as proof of individual underperformance before the ESRG conditions are examined. A missed target is evidence of a performance gap; it does not establish its cause.</p>'
          '<p><strong>Watch for:</strong> leaders who equate &ldquo;we have a scorecard&rdquo; with &ldquo;we have a PM system.&rdquo; Probe: <em>&ldquo;What happens after you look at the scorecard? What changes? Who decides what?&rdquo;</em></p>'
          '</div>\n')

SUMMARY = [
    ('Awareness — What', 'What Was Established',
     'Performance measurement answers what happened; performance management decides what to do about it. Enterprise performance comes from two operating systems: the Human Operating System (results against KPIs and OKRs, and behaviours) and the Organisational Operating System (Environment, Systems, Resources and Governance, ESRG). The S2R® Contribution Map™ connects an enterprise Key Result to the contribution each function, its people and the organisation must make. FACES names the five functions that manage those contributions across both systems.'),
    ('Intelligence — Why', 'Why It Matters',
     'Performance management is the execution bridge that keeps strategy connected to performance throughout delivery. Four bridges sustain it: Decomposing the Big Picture, Defining the Logic of Success, Calibrating the Rhythm and Structuring the Dialogue. Compliance-driven and commitment-driven architectures shape how accountability works for people and for the organisation when results fall short.'),
    ('Extrapolating — Where', 'Where It Becomes Vulnerable',
     'Each executive brings a natural performance focus and a potential blind spot. Unity in Diversity integrates the ten executive performance perspectives into one view of enterprise progress. Three shifts are moving performance management from annual to continuous, from rating-centric to development-centric, and from individual to team performance.'),
    ('Integration — Collective', 'How It Comes Together',
     'The worked example mapped one enterprise Key Result across Customer Service, IT, Operations and Workforce Planning: each function&rsquo;s contribution, what its people must deliver and the ESRG conditions that enable them, each with a measure or evidence. FACES then showed how those contributions are managed in practice.'),
    ('Application — In Practice', 'What Your Group Built',
     'Your group built an S2R® Contribution Map™ for one of its own enterprise Key Results and applied FACES to manage each function&rsquo;s contribution. The confirmed record feeds your team&rsquo;s Capstone Blueprint.')]
SUMMARY_F5 = 'Each group built an S2R® Contribution Map™ for one of its own enterprise Key Results and applied FACES to manage each function&rsquo;s contribution. The confirmed record feeds the team&rsquo;s Capstone Blueprint.'
CLOSING_Q = 'Which contribution in your group&rsquo;s map was hardest to agree, and what does that tell you about the performance management system in your own organisation?'
