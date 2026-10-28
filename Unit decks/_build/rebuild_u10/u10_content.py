# -*- coding: utf-8 -*-
"""Unit 10 content as Carol gave it (27 Oct). Section 1 and the Facilitator Guide."""
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'

GROUNDING = [
 'Grounding establishes the organisational capabilities and healthy operating status required to anchor and sustain strategic performance. It considers how the enterprise is configured to deliver results, the organisational health that sustains performance, and how both are leveraged over time.',
 'The Grounding learning journey progresses from Unit 10 — ESRG Alignment (organisational operating environment), to Unit 11 — Culture Reinforcement &amp; Organisational Health (culture), and then to Unit 12 — Sustaining Performance, which leverages both to sustain high performance.',
]
MODULE_LO = [
 'Configure organisational operating conditions to support strategic priorities and enable consistent enterprise performance.',
 'Shape organisational culture by establishing and embedding the conditions and practices that strengthen organisational health.',
 'Integrate organisational capabilities and cultural practices into a coherent operating environment that supports sustained high performance.',
 'Institutionalise organisational performance sustainability through mechanisms that preserve strategic alignment, strengthen adaptability and maintain performance continuity.',
]
UNIT_LO = [
 'Design an ESRG-aligned organisational operating environment by establishing the Environment, Systems, Resources and Governance requirements necessary to deliver strategic commitments.',
 'Develop targeted organisational alignment interventions that address operating constraints and strengthen the organisation’s capacity for consistent strategic delivery.',
]
ORIENTATION = 'Anchor the discussion in one strategic commitment from the participants’ existing capstone work. The emphasis is on whether the enterprise operating environment can carry the demands of that commitment. Move from required condition, to observed evidence, to the organisational adjustment needed. Avoid building a general-purpose audit of every ESRG component.'
KEY_Q = [
 'What must be operationally true for this strategic commitment to be delivered consistently?',
 'Which condition is essential, and what evidence would demonstrate that it is fit for the required demand?',
 'Where is the visible delay or shortfall, and which operating condition is producing it?',
 'Which function experiences the effect, and which function can change the condition?',
 'What specific organisational adjustment would most improve the strategic result?',
]
PACING = 'Keep Awareness focused on establishing the operating requirements. Reserve deeper evidence testing, causal diagnosis, cross-functional reconciliation and intervention design for the later sections. Reuse the same capstone commitment throughout the unit.'

S1_TITLE = 'What operating conditions must support strategic delivery?'
S1_LO = [
 'Specify the essential organisational operating requirements associated with a selected strategic commitment.',
 'Assign each requirement to the appropriate ESRG domain and component, explaining its direct contribution to the intended result.',
]
S1_GUIDE = 'Begin with one strategic commitment from the capstone. Ask: “What must be in place within the organisation for this result to be delivered?” Recall the four ESRG domains and their three components each from Unit 6. Ask participants to identify only the operating requirements that materially affect their chosen commitment. At this stage, the task is to define and locate requirements; detailed evidence testing follows in Intelligence.'
GQ_TITLE = 'ESRG Alignment — The Grounding Question'
GQ_P = 'A strategy places demands on the organisation’s operating environment. You met ESRG in Unit 6 as the organisational operating system: Environment (FIT), Systems (SIP), Resources (AIR) and Governance (PAR), each with three components. Unit 10 uses ESRG to develop the organisational capability that grounds performance. Section 1 starts with one strategic commitment from your capstone work: which components its delivery depends on, and what each of those components must provide for the result to be delivered.'
GQ_F = 'A strategy places demands on the organisation’s operating environment. Participants met ESRG in Unit 6 as the organisational operating system: Environment (FIT), Systems (SIP), Resources (AIR) and Governance (PAR), each with three components. Unit 10 uses ESRG to develop the organisational capability that grounds performance. Section 1 starts with one strategic commitment from the group’s capstone work: which components its delivery depends on, and what each of those components must provide for the result to be delivered.'
HERO_P = 'Specifying the organisational capability one strategic commitment requires, domain by domain.'


PARTS = [
 ('1.1', 'Environment', 'FIT',
  'Environment concerns the suitability and reliability of the physical and technological setting in which organisational operations take place.',
  [('F','Facilities','Whether operating locations and physical facilities are functional and suited to the planned activity.'),
   ('I','Infrastructure','Whether essential utilities, connectivity and supporting infrastructure can reliably carry operational demand.'),
   ('T','Technology','Whether the technological operating environment is available, reliable and fit for the required activity.')],
  'Are our facilities, infrastructure and technology fit for the strategic requirement?',
  'A production expansion depends on stable electrical supply. Repeated outages prevent the additional production capacity from being used consistently.'),
 ('1.2', 'Systems', 'SIP',
  'Systems concerns how operational work is defined, connected and performed efficiently across the enterprise.',
  [('S','Standardisation','Whether recurring operational processes are clearly defined and consistently applied.'),
   ('I','Integration','Whether systems and process handoffs connect across functions without avoidable breaks.'),
   ('P','Process Efficiency','Whether the required output can be delivered without unnecessary steps, delay, duplication or waste.')],
  'Are our operational processes standardised, integrated and efficient?',
  'Customer onboarding follows a documented process, but disconnected sales and finance platforms require repeated manual entry, slowing completion.'),
 ('1.3', 'Resources', 'AIR',
  'Resources concerns the availability, funding and productive deployment of the organisation’s operational assets.',
  [('A','Asset Availability','Whether sufficient productive equipment and other operating assets are available for the required output.'),
   ('I','Investment','Whether financial provision is adequate for the strategic and operational commitment.'),
   ('R','Resource Utilisation','Whether existing assets and funding are allocated and used productively against priorities.')],
  'Are our assets and financial resources sufficient and effectively utilised?',
  'A logistics operation has enough vehicles, but uneven deployment leaves some idle while others are overused, reducing delivery reliability.'),
 ('1.4', 'Governance', 'PAR',
  'Governance concerns the institutional arrangements through which operational decisions are guided, authorised and exposed risks managed.',
  [('P','Policies &amp; Procedures','Whether the necessary institutional policies and procedures are established and suitable for the decisions and operations required.'),
   ('A','Authority','Whether decision rights, delegated authority and approval pathways support timely decisions.'),
   ('R','Risk Management','Whether material risks to the strategic commitment are identified, assessed, mitigated and monitored.')],
  'Is our organisational governance up to PAR?',
  'Funding for expansion has been approved, yet avoidable approval levels delay the release of expenditure and postpone implementation.'),
]

def header(sub_indent='    '):
    i = sub_indent
    out = [i + '<div class="unit-sub">Grounding · Pillar 3 of DIG</div>']
    out += [i + '<p class="unit-desc">%s</p>' % p for p in GROUNDING]
    out += [i + '<div class="klo-bar">', i + '  <span class="klo-label">Module learning outcomes</span>']
    out += [i + '  <span class="klo">%s</span>' % x for x in MODULE_LO]
    out += [i + '</div>', i + '<div class="klo-bar">', i + '  <span class="klo-label">Key learning outcomes</span>']
    out += [i + '  <span class="klo">%s</span>' % x for x in UNIT_LO]
    out += [i + '</div>']
    return '\n'.join(out)

def acc(title, body, open_=False, meta=''):
    m = '<div class="acc-meta">%s</div>' % meta if meta else ''
    return ('<div class="acc%s">\n<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div>%s</div>%s</div>\n'
            '<div class="acc-b"><div class="cb">\n%s\n</div></div></div>' % (' open' if open_ else '', title, m, ARR, body))

def section1(facilitator):
    out = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in S1_LO)]
    if facilitator:
        out.append('\n<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Awareness</div>\n<p>%s</p>\n</div>\n' % S1_GUIDE)
    out.append(acc(GQ_TITLE, '<p>%s</p>' % (GQ_F if facilitator else GQ_P), True))
    import u10_s1b
    out.append(u10_s1b.block(facilitator))
    for num, dom, acr, intro, rows, dq, ill in PARTS:
        tbl = ('<table class="esrg-tbl"><thead><tr><th>%s</th><th>Component</th><th>What to establish for strategic delivery</th></tr></thead><tbody>\n' % acr
               + '\n'.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in rows) + '\n</tbody></table>')
        body = '<p>%s</p>\n%s\n<div class="hbox"><p><strong>Diagnostic question:</strong> %s</p></div>\n<p><strong>Illustration:</strong> %s</p>' % (intro, tbl, dq, ill)
        out.append(acc('%s &mdash; %s | %s' % (num, dom, acr), body, num == '1.1'))
    return '\n'.join(out) + '\n'

def css(facilitator):
    if facilitator:
        th_bg, col, bd = '#1a2a1e', 'var(--gold)', 'rgba(201,168,76,.2)'
    else:
        th_bg, col, bd = '#162e28', 'var(--teall)', 'rgba(26,122,106,.2)'
    return ('.esrg-tbl{width:100%%;border-collapse:collapse;margin:14px 0;font-size:13px;}\n'
            '.esrg-tbl th{background:%s;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;padding:10px 14px;text-align:left;border-bottom:1px solid %s;}\n'
            '.esrg-tbl td{padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05);color:rgba(255,255,255,.65);line-height:1.65;vertical-align:top;}\n'
            '.esrg-tbl td:first-child{color:%s;font-weight:700;width:8%%;letter-spacing:2px;}\n'
            '.esrg-tbl td:nth-child(2){color:rgba(255,255,255,.85);font-weight:600;width:24%%;}\n'
            '@media (max-width:600px){.esrg-tbl th,.esrg-tbl td{padding:8px;}}\n') % (th_bg, col, bd, col)

def guide():
    return ('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitation Orientation</div>\n<p>%s</p>\n</div>\n'
            '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Key Facilitation Questions</div><ul>\n%s\n</ul></div>\n'
            '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitation Pacing</div>\n<p>%s</p>\n</div>\n') % (
            ORIENTATION, '\n'.join('<li>%s</li>' % q for q in KEY_Q), PACING)
