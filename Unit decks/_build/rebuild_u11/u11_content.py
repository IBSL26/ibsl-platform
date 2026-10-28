# -*- coding: utf-8 -*-
"""Unit 11 content as Carol gave it (27 Oct 20:10). Facilitator Guide and Section 1 · Awareness."""
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
 'Diagnose organisational health by evaluating how organisational values and cultural norms influence collective behaviour and strategic performance.',
 'Shape and reinforce organisational culture by establishing behavioural standards and embedding cultural operating norms that strengthen organisational health.',
]
INTENT = 'Develop executive capability to assess how organisational values become lived culture and how that culture shapes organisational health, then establish the practices required to reinforce healthy organisational behaviour.'
JOURNEY = [
 ('1 · Awareness — What', 'Organisational values, culture and health; the Cultural Operating Code; the Five Observable Health Traits; the Organisational Health Pyramid.'),
 ('2 · Intelligence — Why', 'Organisational health as a performance multiplier; execution velocity; the price of poor health; health and sustained performance.'),
 ('3 · Extrapolating — Where', 'Organisational health signals and the thermometer; CXO functional bias and debiasing; personal health profile.'),
 ('4 · Integration — Collective', 'The Cross-CXO Health Architecture: the thermometer, functional scores, loss quantification and the enterprise position; from values to a Cultural Operating Code; individual reflection.'),
 ('5 · Application — In Practice', 'The Cross-CXO Organisational Health Clinic: functional assessments, consolidation, Review–Realign–Restore, the Organisational Health Response and the group’s Cultural Operating Code.'),
]
EMPHASIS = 'Keep the central progression explicit: values establish behavioural principles; culture reflects how these principles are lived; organisational health reflects the resulting collective condition. Use participant organisations as reference points. The executive team presentation takes place only at the final programme panel assessment.'

S1_TITLE = 'Values, Culture &amp; Organisational Health'
HERO_P = 'How organisational values become lived culture, and how that culture shows in the condition of organisational health.'
S1_LO = [
 'Evaluate how organisational values translate into cultural norms and practices that shape organisational health.',
 'Diagnose organisational health strengths and vulnerabilities across observable behaviour and its underlying conditions.',
]

VALUES = [('Integrity','Act honestly, communicate transparently and uphold ethical commitments.'),
 ('Accountability','Take ownership of responsibilities, honour commitments and report progress accurately.'),
 ('Respect','Treat others fairly, listen constructively and recognise different perspectives.'),
 ('Excellence','Maintain high standards, address performance gaps and pursue continuous improvement.'),
 ('Collaboration','Share information, coordinate efforts and contribute to collective outcomes.')]
TRAITS = [('1. Minimal Politics','Employees collaborate openly, with limited personal agendas, territorial behaviour and internal competition.'),
 ('2. Minimal Confusion','People understand organisational direction, priorities, responsibilities and performance expectations.'),
 ('3. High Morale','Employees demonstrate commitment, motivation and confidence in their working environment.'),
 ('4. High Productivity','Collective effort is coordinated effectively and translates into meaningful performance outcomes.'),
 ('5. Low Turnover','The organisation retains capable employees through a working environment that supports commitment and contribution.')]
PYRAMID = [
 ('Trust','The Foundation',
  ['Trust forms the foundation of organisational health. It develops through consistent leadership behaviour, including keeping commitments, communicating transparently, acknowledging mistakes and treating people fairly.',
   'When trust is established, employees develop confidence in their leaders and colleagues. They become more willing to communicate openly, raise concerns and contribute to collective objectives.'],
  'Organisational health begins with the trust established through consistent leadership conduct.'),
 ('Experiences','Shaped by Trust',
  ['Employees experience organisational culture through everyday interactions, meetings, performance conversations, leadership decisions and recognition practices.',
   'These experiences communicate what the organisation genuinely values and the behaviours it considers acceptable. For example, the way leaders respond to mistakes influences whether employees experience the organisation as supportive of learning or inclined towards blame.'],
  'Everyday organisational experiences reinforce or weaken the values leadership seeks to establish.'),
 ('Beliefs','Formed by Experiences',
  ['Through repeated experiences, employees develop beliefs about how the organisation operates. They form assumptions about whether leaders listen, whether commitments matter, whether effort is recognised and whether honest communication is encouraged.',
   'Over time, these beliefs influence how employees interpret organisational expectations and their own responsibilities.'],
  'Repeated organisational experiences establish the beliefs that influence collective behaviour.'),
 ('Actions','Driven by Beliefs',
  ['Employees’ beliefs influence how they behave and contribute to organisational performance. When employees believe their contributions are valued, they are more likely to share ideas, collaborate and take initiative.',
   'When they believe accountability is consistently reinforced, they are more likely to take ownership of responsibilities and honour commitments.'],
  'The beliefs established through organisational culture influence the behaviours employees demonstrate.'),
 ('Results','The Visible Traits',
  ['The actions employees consistently demonstrate produce collective organisational outcomes. These outcomes become visible through the Five Observable Health Traits: Minimal Politics, Minimal Confusion, High Morale, High Productivity and Low Turnover.',
   'At the apex of the pyramid, organisational results reflect the cumulative influence of trust, experiences, beliefs and actions. A commitment to continuous improvement helps sustain these results as the organisation evolves.'],
  'The visible condition of organisational health reflects the underlying cultural experiences and behaviours established throughout the organisation.'),
]
CLOSING = 'Values establish the principles that guide organisational behaviour. Culture reflects how those principles become established ways of working. Organisational health reveals how effectively those values are lived through the culture that has developed.'

def header(i='    '):
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

def det(title, body, open_=False):
    return '<details class="u11-det"%s><summary>%s</summary><div class="u11-det-b">\n%s\n</div></details>' % (' open' if open_ else '', title, body)

def tbl(h1, h2, rows):
    return ('<table class="u11-tbl"><thead><tr><th>%s</th><th>%s</th></tr></thead><tbody>\n' % (h1, h2)
            + '\n'.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in rows) + '\n</tbody></table>')

def section1(facilitator):
    out = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in S1_LO)]
    b11 = ('<p>Organisational values are the fundamental principles that guide how an organisation conducts itself in pursuit of its purpose and strategic objectives.</p>\n'
           '<p>They establish the standards of behaviour expected of leaders and employees, influencing how people are treated, responsibilities are fulfilled and performance is achieved.</p>\n'
           '<p>Values serve two important organisational purposes:</p>\n'
           '<div class="u11-purp"><p><strong>1. Establish Behavioural Expectations.</strong> Values define the standards of conduct expected across the organisation. They guide how people interact, exercise authority, fulfil responsibilities and collaborate in delivering strategic priorities.</p>\n'
           '<p><strong>2. Provide a Basis for Accountability.</strong> Values establish the principles against which organisational conduct can be assessed. They enable leaders to evaluate how results are achieved, alongside the results themselves.</p></div>\n'
           '<h4 class="u11-h">Translating Values into Behavioural Standards</h4>\n'
           '<p>For values to influence organisational conduct, they must be expressed through observable behaviours.</p>\n'
           + tbl('Organisational Value', 'Expected Behavioural Standard', VALUES) + '\n'
           '<p>These behavioural standards clarify what organisational values mean in practice. However, the existence of values and behavioural standards does not guarantee their consistent application.</p>\n'
           '<p>Their influence depends on whether leaders and employees repeatedly demonstrate, reinforce and uphold them through everyday organisational practices. It is through this consistent application that organisational values become embedded in organisational culture.</p>')
    out.append(acc('1.1 &mdash; Organisational Values: What We Stand For', b11, True))
    b12 = ('<p>Organisational culture is the system of shared behavioural norms that determines how people conduct themselves and work together.</p>\n'
           '<p>Culture develops as organisational values are translated into behavioural expectations and repeatedly demonstrated through everyday interactions and ways of working.</p>\n'
           '<p>Over time, these behaviours become accepted as “the way we do things around here”. The organisation’s actual culture therefore reflects the behaviours that have become normal, regardless of its stated values.</p>\n'
           '<h4 class="u11-h">The Cultural Operating Code</h4>\n'
           '<p>The deliberate translation of organisational values into shared cultural norms forms the foundation of a Cultural Operating Code, which establishes how organisational values are consistently lived and reinforced.</p>\n'
           '<p>A Cultural Operating Code makes explicit the behavioural expectations that govern how people work together, exercise accountability, communicate and contribute to organisational priorities.</p>\n'
           '<p>When consistently practised and reinforced, these norms become embedded in the organisation’s culture. The culture established through these shared norms and everyday practices determines how organisational values are experienced and reflected in organisational health.</p>')
    out.append(acc('1.2 &mdash; Organisational Culture: How We Do Things', b12))
    traits = ('<p>The Five Observable Health Traits provide visible indicators of the condition of organisational health.</p>\n'
              + tbl('Health Trait', 'Observable Organisational Condition', TRAITS) + '\n'
              '<p>These traits describe what organisational health looks like when it is strong. However, the traits are only the visible surface of organisational health. To understand how they are produced, we examine the underlying conditions through the Organisational Health Pyramid.</p>')
    tabs = ''.join('<div class="step-tab%s" onclick="showStep(%d,this)"><div class="step-num">%d. %s</div><div class="step-name">%s</div></div>' % (' active' if k == 0 else '', k, k + 1, a, b) for k, (a, b, c, d) in enumerate(PYRAMID))
    panels = ''.join('<div class="step-panel%s"><h5>%d. %s &mdash; %s</h5>%s<p class="u11-impl"><strong>Leadership implication:</strong> %s</p></div>' % (' active' if k == 0 else '', k + 1, a, b, ''.join('<p>%s</p>' % x for x in c), d) for k, (a, b, c, d) in enumerate(PYRAMID))
    pyr = ('<p>The Organisational Health Pyramid explains how organisational health develops from the inside outward. It illustrates how trust influences employees’ experiences, how those experiences shape beliefs, how beliefs influence actions and how actions produce organisational results.</p>\n'
           '<div class="hbox"><p style="text-align:center;font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;letter-spacing:1px;">Trust &rarr; Experiences &rarr; Beliefs &rarr; Actions &rarr; Results</p></div>\n'
           '<div class="step-group"><div class="step-tabs">%s</div>%s</div>' % (tabs, panels))
    conn = ('<p><strong>The Five Observable Health Traits describe what we see.</strong> They indicate the visible condition of organisational health.</p>\n'
            '<p><strong>The Organisational Health Pyramid explains how that condition develops.</strong> It examines the underlying trust, experiences, beliefs and actions that influence organisational results.</p>\n'
            '<p>When trust deteriorates, employees’ experiences may create scepticism, their beliefs may become defensive and their actions may shift towards self-protection. Over time, these patterns can weaken the visible traits of organisational health.</p>\n'
            '<p>Strengthening organisational health therefore requires leadership attention to the underlying cultural conditions that shape everyday employee experiences.</p>')
    b13 = ('<p>Organisational health reflects how effectively organisational values are lived out within the culture that has been established.</p>\n'
           '<p>It is evident in the quality of collective working relationships, clarity of expectations, employee commitment, accountability and the organisation’s ability to function effectively in pursuit of strategic objectives.</p>\n'
           '<p>Patrick Lencioni describes a healthy organisation as one that is whole, consistent and complete, with its management, operations, strategy and culture working together coherently.</p>\n'
           '<p>Within Strategy2Results®, organisational health provides an indication of how effectively organisational values have become embedded in the culture experienced by employees.</p>\n'
           + det('The Five Observable Health Traits', traits, True) + '\n'
           + det('The Organisational Health Pyramid', pyr) + '\n'
           + det('Connecting the Five Traits and the Pyramid', conn))
    out.append(acc('1.3 &mdash; Organisational Health: The Resulting Condition', b13, meta='Select each part to open it'))
    out.append('<div class="hbox"><div class="u11-ci">Section Closing Insight</div><p>%s</p></div>' % CLOSING)
    return '\n'.join(out) + '\n'

def css(fac):
    th_bg, col, bd = ('#1a2a1e', 'var(--gold)', 'rgba(201,168,76,.2)') if fac else ('#162e28', 'var(--teall)', 'rgba(26,122,106,.2)')
    return ('.u11-tbl{width:100%%;border-collapse:collapse;margin:14px 0;font-size:13px;}\n'
            '.u11-tbl th{background:%s;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;padding:10px 14px;text-align:left;border-bottom:1px solid %s;}\n'
            '.u11-tbl td{padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05);color:rgba(255,255,255,.65);line-height:1.65;vertical-align:top;}\n'
            '.u11-tbl td:first-child{color:rgba(255,255,255,.85);font-weight:600;width:30%%;}\n'
            '.u11-h{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin:20px 0 8px;}\n'
            '.u11-purp{border-left:2px solid %s;padding-left:14px;margin:10px 0 14px;}\n'
            '.u11-impl{border-top:1px solid rgba(255,255,255,.08);padding-top:10px;}\n'
            '.u11-ci{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin-bottom:6px;}\n'
            '.u11-det{border:1px solid rgba(255,255,255,.1);border-radius:3px;margin:10px 0;background:rgba(255,255,255,.02);}\n'
            '.u11-det>summary{cursor:pointer;list-style:none;padding:11px 14px;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.82);display:flex;justify-content:space-between;align-items:center;}\n'
            '.u11-det>summary::-webkit-details-marker{display:none;}\n'
            '.u11-det>summary::after{content:"\\25BE";font-size:13px;opacity:.6;transition:transform .2s;}\n'
            '.u11-det[open]>summary::after{transform:rotate(180deg);}\n'
            '.u11-det-b{padding:2px 14px 12px;}\n'
            '.step-tabs{flex-wrap:wrap;}\n'
            '@media (max-width:600px){.u11-tbl th,.u11-tbl td{padding:8px;}.u11-tbl td:first-child{width:36%%;}}\n') % (th_bg, col, bd, col, col, col)

def guide():
    rows = '\n'.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in JOURNEY)
    return ('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Unit Intent</div>\n<p>%s</p>\n</div>\n'
            '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Learning Journey</div>\n'
            '<table class="u11-tbl"><thead><tr><th>Section</th><th>Focus</th></tr></thead><tbody>\n%s\n</tbody></table>\n</div>\n'
            '<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitation Emphasis</div>\n<p>%s</p>\n</div>\n') % (INTENT, rows, EMPHASIS)
