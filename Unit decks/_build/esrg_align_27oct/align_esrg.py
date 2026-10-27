# -*- coding: utf-8 -*-
"""ESRG alignment of Units 6, 8 and 9 to Unit 10's FIT / SIP / AIR / PAR (Carol, 27 Oct 2026: "do this ESRG alignment of Units 6, 8 and 9, as agreed").
Unit 6 part 1.2.2 rewritten in the new format (brief); Units 8 and 9: organisational labels remapped to the new components,
people items moved to the people performance side of the same card, a new organisational example where a card would keep only one,
part 1.1 ESRG sentence of Unit 9. Same edits on participant and facilitator pages.
Usage: python3 -B align_esrg.py <portal folder> <out folder>"""
import sys, os, re
src, out = sys.argv[1:3]
def rd(p):
    b = open(os.path.join(src, p), 'rb').read().decode('utf-8'); return b.replace('\r\n', '\n'), '\r\n' in b
def wr(p, t, crlf):
    os.makedirs(out, exist_ok=True); open(os.path.join(out, p), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
def once(t, a, b):
    assert t.count(a) == 1, 'expected once (%d): %s' % (t.count(a), a[:90]); return t.replace(a, b)
LOG = []

# ── item tools for the two-side cards (u8v-hc) ──
def find_item(t, label, prefix):
    m = None
    for tag in ('li', 'p'):
        pat = r'<%s><strong>%s\.</strong>\s*%s.*?</%s>' % (tag, re.escape(label), re.escape(prefix), tag)
        ms = list(re.finditer(pat, t, re.S))
        if ms:
            assert len(ms) == 1, (label, prefix, len(ms)); m = (ms[0], tag); break
    assert m, ('not found', label, prefix)
    return m
def relabel(t, label, prefix, new):
    (m, tag) = find_item(t, label, prefix)
    s = m.group(0).replace('<strong>%s.</strong>' % label, '<strong>%s.</strong>' % new, 1)
    LOG.append('relabel | %s → %s | %s' % (label, new, prefix)); return t[:m.start()] + s + t[m.end():]
def to_people(t, label, prefix, people_label):
    (m, tag) = find_item(t, label, prefix)
    body = re.sub(r'^<%s><strong>[^<]*</strong>\s*' % tag, '', m.group(0))[:-len('</%s>' % tag)]
    t = t[:m.start()] + t[m.end():]
    hc = t.rfind('<div class="u8v-hc', 0, m.start()); orc = t.find('<div class="u8v-c u8v-or">', hc)
    assert 0 < hc < orc < m.start() + 5, label
    end_hu = t.rfind('</div>', hc, orc)          # the people side closes just before the organisation side opens
    t = t[:end_hu] + '<p><strong>%s.</strong> %s</p>' % (people_label, body) + t[end_hu:]
    LOG.append('to people side | %s → "%s" | %s' % (label, people_label, prefix)); return t
def add_after(t, label_new_item_after, prefix, new_label, text):
    (m, tag) = find_item(t, label_new_item_after, prefix)
    s = '<%s><strong>%s.</strong> %s</%s>' % (tag, new_label, text, tag)
    LOG.append('new organisational example | %s | %s' % (new_label, text)); return t[:m.end()] + s + t[m.end():]

def unit8(t):
    t = to_people(t, 'Resources · workforce capacity', 'A contact centre', 'Workforce capacity')
    t = to_people(t, 'Environment · psychological safety', 'In a function where raising', 'Psychological safety')
    t = relabel(t, 'Systems · data integrity', 'Sales, operations and finance each report', 'Systems · Integration')
    t = add_after(t, 'Systems · Integration', 'Sales, operations and finance each report', 'Environment · Infrastructure',
                  'Power outages at the main depot rise from one a month to one a week. Dispatch holds on backup generators until fuel costs exceed the budget; the outage log showed the trend weeks before the delivery KPI moved.')
    t = to_people(t, 'Resources · capability alignment', 'A new procurement system', 'Capability')
    t = relabel(t, 'Governance · clear accountability', 'A regional manager is accountable', 'Governance · Authority')
    t = add_after(t, 'Governance · Authority', 'A regional manager is accountable', 'Resources · Investment',
                  'The upgrade budget for the delivery fleet is approved in the plan and never released. The fleet-availability commitment is reported as on track every month until the vehicles are needed.')
    t = relabel(t, 'Systems · process clarity', 'Three functions each report delays', 'Systems · Integration')
    t = relabel(t, 'Resources · financial support', 'For two years running', 'Resources · Investment')
    t = relabel(t, 'Governance · decision authority', 'Capital requests above a set value', 'Governance · Authority')
    t = to_people(t, 'Environment · values and consequences', 'The organisation states accountability', 'Values and consequences')
    t = to_people(t, 'Environment · psychological safety', 'Leaders invite open reporting', 'Psychological safety')
    t = relabel(t, 'Governance · execution oversight', 'The executive team commits to a monthly decision forum', 'Governance · Risk Management')
    t = add_after(t, 'Governance · Risk Management', 'The executive team commits to a monthly decision forum', 'Governance · Policies &amp; Procedures',
                  'The review procedure requires evidence for every individual KPI and none for the organisational conditions, so a failed condition never reaches the agenda.')
    t = relabel(t, 'Systems · process clarity', 'The order-to-cash process', 'Systems · Integration')
    t = relabel(t, 'Governance · decision authority', 'A non-standard customer contract', 'Governance · Authority')
    t = to_people(t, 'Resources · workforce capacity', 'HR reports headcount at budget', 'Workforce capacity')
    t = relabel(t, 'Systems · workflow visibility', 'IT reports system availability', 'Environment · Technology')
    t = add_after(t, 'Environment · Technology', 'IT reports system availability', 'Resources · Asset Availability',
                  'The asset register shows every delivery vehicle in service. A third are off the road awaiting parts. The evidence that matters is how many vehicles can carry the work today.')
    t = relabel(t, 'Governance · execution oversight', 'Capital and risk decisions follow the board calendar', 'Governance · Authority')
    t = relabel(t, 'Resources · financial support', 'Budgets are reallocated only', 'Resources · Resource Utilisation')
    t = to_people(t, 'Environment · employee sustainability', 'Workload is seen through', 'Employee sustainability')
    t = to_people(t, 'Environment · psychological safety', 'A team lead knows the approval process', 'Psychological safety')
    t = relabel(t, 'Governance · consistent consequences', 'Shortfalls in individual KPIs', 'Governance · Policies &amp; Procedures')
    t = add_after(t, 'Governance · Policies &amp; Procedures', 'Shortfalls in individual KPIs', 'Governance · Risk Management',
                  'The risk register lists the approval process as a delivery risk, and no review has examined it since it was logged.')
    assert not re.search(r'<strong>(Environment|Systems|Resources|Governance) · [a-z]', t), re.findall(r'<strong>((?:Environment|Systems|Resources|Governance) · [a-z][^<]*)', t)
    return t

def unit9(t):
    t = once(t, 'These conditions are the Environment, Systems, Resources and Governance (ESRG): the environment people work in, the systems they rely on, the resources they are given and the governance that guides decisions.',
             'These conditions are the Environment, Systems, Resources and Governance (ESRG): the facilities, infrastructure and technology the work depends on, the processes that carry it across functions, the assets and funding that make delivery possible, and the policies, decision authority and risk management that guide it.')
    LOG.append('part 1.1 ESRG sentence rewritten')
    R = [('Governance · review forums', 'The same unresolved item appears', 'Governance · Authority'),
         ('Systems · data integrity', 'Two reports give different figures', 'Systems · Integration'),
         ('Governance · decision authority', 'Approvals for routine work sit', 'Governance · Authority'),
         ('Systems · process clarity', 'The hand-offs between three functions', 'Systems · Integration'),
         ('Governance · decision authority', 'Delegation limits for routine', 'Governance · Authority'),
         ('Systems · data integrity', 'One source of customer data', 'Systems · Integration'),
         ('Systems · process clarity', 'Three regions run three versions', 'Systems · Standardisation'),
         ('Governance · clear accountability', 'A named leader maintains the standard', 'Governance · Policies &amp; Procedures'),
         ('Governance · decision authority', 'Routine purchases below', 'Governance · Authority'),
         ('Systems · approvals', 'One electronic approval route', 'Systems · Process Efficiency'),
         ('Governance · clear accountability', 'One executive owns the end-to-end', 'Governance · Authority'),
         ('Governance · review forums', 'Each open trade-off', 'Governance · Authority'),
         ('Systems · data integrity', 'The customer and transport systems', 'Systems · Integration'),
         ('Environment · infrastructure', 'Field teams receive reliable', 'Environment · Infrastructure'),
         ('Resources · capability alignment', 'A development programme', 'Resources · Investment'),
         ('Governance · consistent consequences', 'Sales bonuses are paid', 'Governance · Policies &amp; Procedures'),
         ('Systems · performance data', 'Shared enterprise measures', 'Systems · Integration'),
         ('Governance · consistent consequences', 'Commitments missed at senior level', 'Governance · Policies &amp; Procedures')]
    t = to_people(t, 'Resources · workforce capacity', 'One specialist', 'Workforce capacity')
    t = to_people(t, 'Resources · capability alignment', 'Specialist capacity is added', 'Workforce capacity')
    t = to_people(t, 'Environment · values and consequences', 'Leaders', 'Values and consequences')
    t = to_people(t, 'Environment · psychological safety', 'Leaders open each review', 'Psychological safety')
    for a, p, n in R: t = relabel(t, a, p, n)
    t = add_after(t, 'Resources · Investment', 'A development programme', 'Environment · Technology',
                  'Lending officers receive the credit-assessment software the training uses, so new skills are applied on live cases from the first week.')
    t = add_after(t, 'Governance · Policies &amp; Procedures', 'Commitments missed at senior level', 'Governance · Risk Management',
                  'Delivery risks raised in a review are logged with an owner and a date, and the log is examined at the next review.')
    assert not re.search(r'<strong>(Environment|Systems|Resources|Governance) · [a-z]', t), re.findall(r'<strong>((?:Environment|Systems|Resources|Governance) · [a-z][^<]*)', t)
    return t

def it(code, name, acr, comps, defin, ex, pm):
    return ('<div class="u6-it"><div class="u6-it-h" onclick="this.parentNode.classList.toggle(\'open\')"><span><strong>%s &middot; %s &middot; %s</strong></span><span class="u6-it-a">&#9662;</span></div>'
            '<div class="u6-it-b"><p><strong>Components:</strong> %s.</p><p>%s</p><p><strong>Example:</strong> %s</p><p><strong>Performance management consideration:</strong> %s</p></div></div>') % (code, name, acr, comps, defin, ex, pm)

def unit6(t):
    old_intro = 'Within S2R®, these conditions are examined through ESRG: Environment, Systems, Resources and Governance. ESRG provides the structure for evaluating whether the organisation has the operating capability necessary to support its strategic ambition.'
    t = once(t, old_intro, 'Within S2R®, these conditions are examined through ESRG: Environment, Systems, Resources and Governance, each with three components. ESRG provides the structure for evaluating whether the organisation has the operating capability necessary to support its strategic ambition. The capacity, capability and behaviour of people sit in the Human Operating System. Unit 10 teaches how to leverage ESRG to develop the organisational capability that grounds performance.')
    a = t.index('<div class="u6-its"><div class="u6-it"><div class="u6-it-h" onclick="this.parentNode.classList.toggle(\'open\')"><span><strong>E &middot; Environment</strong>')
    z = t.index('<div class="hbox"><p>The Organisational Operating System answers', a)
    new = ('<div class="u6-its">' +
      it('E', 'Environment', 'FIT', 'Facilities · Infrastructure · Technology',
         'The physical and technological setting in which the work takes place: facilities suited to the planned activity, infrastructure that reliably carries operational demand, and technology that is available and fit for the required work.',
         'a customer service team has clear targets, but repeated outages of the customer management system leave enquiries unresolved.',
         'Are the facilities, infrastructure and technology supporting or obstructing the achievement of expected results?') +
      it('S', 'Systems', 'SIP', 'Standardisation · Integration · Process Efficiency',
         'How work is defined, connected and performed across the organisation: processes clearly defined and consistently applied, handovers that connect across functions, and process design that delivers the required output without unnecessary steps, delay or duplication.',
         'employees may be expected to process 100 applications daily, but disconnected handovers between departments limit actual throughput to 60 applications.',
         'Are the systems and processes capable of supporting the required performance standards?') +
      it('R', 'Resources', 'AIR', 'Asset Availability · Investment · Resource Utilisation',
         'The productive assets and funding required to deliver results, and how productively they are deployed against priorities. Resource adequacy must be evaluated against the level of performance the organisation expects.',
         'a department may be required to double its service output with the same equipment and no additional budget.',
         'Does the organisation have sufficient and appropriately deployed assets and funding to achieve its targets?') +
      it('G', 'Governance', 'PAR', 'Policies &amp; Procedures · Authority · Risk Management',
         'The policies and procedures, decision authority and risk management that guide organisational execution. Governance determines whether decisions can be made at the appropriate level and time, and whether risks to delivery are identified and managed.',
         'a department may have the resources to complete a project, but repeated approval delays prevent it from meeting agreed milestones.',
         'Do governance arrangements enable timely decisions, clear accountability and effective resolution of performance constraints?') +
      '</div>\n')
    t = t[:a] + new + t[z:]
    LOG.append('part 1.2.2 domain definitions rewritten (FIT, SIP, AIR, PAR)')
    t = once(t, 'Are cross-functional working conditions supporting timely resolution?', 'Are the facilities, infrastructure and technology the team relies on available and reliable?')
    t = once(t, 'Is staffing capacity sufficient for the volume of enquiries?', 'Are the equipment and funding sufficient for the volume of enquiries?')
    LOG.append('part 1.2.3 table: Environment and Resources questions')
    # Contribution Map worked example labels
    for a_, b_ in [('Systems:</strong> Reliable infrastructure and monitoring capability to maintain system availability.', 'Environment:</strong> Reliable infrastructure and monitoring technology to maintain system availability.'),
                   ('Systems:</strong> &ge;99% customer management system availability during service hours.', 'Environment:</strong> &ge;99% customer management system availability during service hours.'),
                   ('Resources:</strong> Sufficient technical support coverage during service hours.', 'Resources:</strong> A funded technical support contract covering service hours.'),
                   ('Resources:</strong> Approved technical support roster covering required service hours.', 'Resources:</strong> Approved support contract covering required service hours.'),
                   ('Resources:</strong> Sufficient qualified staff available to meet forecast customer enquiry volumes.', 'Resources:</strong> Funding approved for the staffing levels that forecast customer enquiry volumes require.'),
                   ('Resources:</strong> &ge;95% staffing coverage against demand-based requirements.', 'Resources:</strong> &ge;95% of the demand-based staffing budget approved and released.')]:
        t = once(t, a_, b_); LOG.append('Contribution Map example | ' + re.sub('<[^>]+>', '', b_))
    return t


def unit7(t):
    R = [('What working conditions, relationships or cultural practices must support delivery?', 'What facilities, infrastructure and technology must support delivery?'),
         ('What processes, technology, information and coordination mechanisms must function?', 'Which processes must be standardised, integrated across functions and efficient enough to deliver?'),
         ('What people, skills, time, funding or equipment must be available?', 'What assets and funding must be available, and how must they be deployed?'),
         ('What decisions, authority, approvals and escalation arrangements must be established?', 'What policies and procedures, decision authority and risk management must be established?'),
         ('Do working conditions and relationships support the required performance?', 'Are the facilities, infrastructure and technology fit for the required performance?'),
         ('Can existing processes, technology and information support consistent delivery?', 'Are the processes standardised, integrated and efficient enough to support consistent delivery?'),
         ('Are the required people, funding, equipment and time available?', 'Are the required assets and funding available and productively deployed?'),
         ('Are decisions, authority and escalation mechanisms sufficiently clear and responsive?', 'Are the policies and procedures, decision authority and risk management clear and responsive?'),
         ('The working conditions, relationships or practices that must support delivery, and their owner...', 'The facilities, infrastructure and technology that must support delivery, and their owner...'),
         ('The processes, technology, information or coordination that must work, and their owner...', 'The processes that must be standardised, integrated and efficient, and their owner...'),
         ('The people, skills, time, funding or equipment required, and their owner...', 'The assets and funding required, and their owner...'),
         ('The decisions, authority, approvals or escalation required, and their owner...', 'The policies and procedures, decision authority and risk management required, and their owner...')]
    for a_, b_ in R:
        n = t.count(a_)
        if n:
            t = t.replace(a_, b_); LOG.append('Unit 7 (%dx) | %s → %s' % (n, a_, b_))
    assert 'working conditions' not in t and 'people, skills, time' not in t and 'people, funding, equipment' not in t
    return t

for unit, fn, files in [('6', unit6, ['unit3_m1_lens5_p.html', 'unit3_m1_lens5_f.html']), ('8', unit8, ['unit3_m2_lens7_p.html', 'unit3_m2_lens7_f.html']), ('9', unit9, ['unit3_m2_lens8_p.html', 'unit3_m2_lens8_f.html']), ('7', unit7, ['unit3_m1_lens6_p.html', 'unit3_m1_lens6_f.html'])]:
    for f in files:
        LOG.append('== Unit %s · %s' % (unit, f)); t, c = rd(f); wr(f, fn(t), c)
open(os.path.join(out, 'change_log.txt'), 'w', encoding='utf-8').write('\n'.join(LOG) + '\n')
print('\n'.join(l for l in LOG if l.startswith('==')), '\nwritten to', out)
