# -*- coding: utf-8 -*-
"""Unit 4 rebuild (October 2026): the content both pages share.
Source of the flow: Carol's brief of 7 October 2026. Source of the wording: her Unit 4 manuscript, her Industry Illusion concept,
the pages as they stood (marked 'page'), and new example conditions written for her review (marked 'new')."""
import html as _h

def esc(s):
    return _h.escape(s, quote=False)

# ── The four checkpoints (manuscript table, word for word; contrast sentences reworded as on the facilitator page) ──
CHECKPOINTS = [
    dict(k='a', cls='arena', name='Arena', tag='Customer End Game', icon='&#127919;',
         logic='Strategy starts with a shift in perspective: we compete for a customer need. If we define our arena by our products, we miss the forest for the trees.',
         anchor='What is the customer actually trying to achieve? What functional, emotional, or social &lsquo;job&rsquo; are they hiring us to do?',
         mbt='What must remain true about that functional, experiential or consequential need for this Key Result to stay relevant?',
         mbt_eg='Say which depth the condition rests on. Example (experiential): &ldquo;Clients must continue to value a response inside four hours.&rdquo;'),
    dict(k='b', cls='boundaries', name='Boundaries', tag='Friction Architecture', icon='&#128679;',
         logic='Every arena has invisible walls: operational limits, regulations, or simple human resistance to change. A strategy that ignores friction is a wish.',
         anchor='What is going to push back against us? What internal or external friction could slow this Key Result down or stop it entirely?',
         mbt='What must remain true operationally or regulatorily for us to actually deliver this without breaking?',
         mbt_eg='If your Key Result relies on a new tech stack, then &ldquo;Our infrastructure must handle 10x load&rdquo; is your MBT.'),
    dict(k='c', cls='competition', name='Competition', tag='The True Landscape', icon='&#128269;',
         logic='Once you define the Arena by the customer&rsquo;s need, your &lsquo;competitors&rsquo; change. You are fighting anyone who solves that same problem in a different way, peers included.',
         anchor='Who else is solving this problem, even if they look nothing like us? Who is the &lsquo;alternative&rsquo; the customer might choose?',
         mbt='What must remain true about our specific advantage compared to these other options?',
         mbt_eg=''),
    dict(k='v', cls='valueprop', name='Value Proposition', tag='Coherent Advantage', icon='&#128142;',
         logic='Strategy wins when you are distinct. Every Key Result should make your unique DNA stronger. If a goal dilutes your brand or confuses your value, it is a distraction.',
         anchor='How does this goal make us more &lsquo;us&rsquo;? Does this Key Result sharpen our distinctive edge or just add noise?',
         mbt='What must remain true about our value architecture for this Key Result to stay coherent and profitable?',
         mbt_eg=''),
]
CP = {c['k']: c for c in CHECKPOINTS}

# ── Teaching content for 1.1 to 1.4: Carol's ABCV–MBT content of 7 October (evening), word for word except "lens" → "checkpoint",
#    the author's asides, and the pointer to the Industry Illusion (it is taught after ABCV, in Section 2). ──
ARENA_QUOTE = 'The Industry tells you who you think you are competing with. The Arena tells you who you are actually competing with.'
SMARTPHONE = 'Think about the smartphone. Inside the &ldquo;telecommunications industry&rdquo;, Nokia and Motorola were making phones. The smartphone became a camera, a map, a bank and a personal assistant. It moved into multiple Arenas simultaneously.'
HEAD_Q = {
    'a': 'What is the customer ultimately trying to achieve?',
    'b': 'What could constrain our ability to deliver within this Arena?',
    'c': 'Who or what else can satisfy the same Customer End Game?',
    'v': 'Why should the customer choose the value we create?',
}
OVERVIEW_Q = [('a', 'A &mdash; Arena', 'Are we anchored in the right customer end game?'), ('b', 'B &mdash; Boundaries', 'What conditions could constrain our ability to deliver?'),
              ('c', 'C &mdash; Competition', 'Who or what else can satisfy that end game?'), ('v', 'V &mdash; Value Proposition', 'Why should the customer choose the value we create?')]
LOGIC = ['Define the Arena', 'Understand the Boundaries', 'See the Competition', 'Establish the Value Proposition', 'Name what Must Be True']
DEPTHS = [
    dict(n=1, name='Functional', q='What are they trying to achieve?',
         body=['This identifies the immediate practical outcome.'],
         ask='What needs to get done, solved, accessed, changed or achieved?',
         egs=['A learner wants to develop relevant capability.', 'A bank customer wants to move and manage money.', 'A manufacturer wants to keep critical equipment operating.',
              'A logistics customer wants to move goods reliably from one point to another.'],
         close=['Functional analysis prevents leaders from confusing what the organisation sells with what the customer needs accomplished.',
                'A university sells programmes and qualifications. The learner may be trying to build capability. Those are related, but they are not the same thing.']),
    dict(n=2, name='Experiential', q='What matters about how they achieve it?',
         body=['The outcome alone may not fully explain customer choice.', 'Customers may care about the conditions under which the outcome is achieved:'],
         chips=['Speed', 'Convenience', 'Reliability', 'Safety', 'Flexibility', 'Simplicity', 'Confidence', 'Accessibility', 'Effort'],
         ask='What matters to the customer about the experience of achieving the functional outcome?',
         egs=['For a working professional, developing capability may need to be flexible, accessible and compatible with employment.',
              'For someone transferring money: fast, secure and convenient.',
              'For an industrial customer purchasing equipment: reliable, predictable and minimally disruptive to operations.'],
         close=['The experiential dimension matters strategically because two organisations may solve the same functional problem while creating very different customer experiences.']),
    dict(n=3, name='Consequential', q='What does achieving it ultimately enable?',
         body=['This pushes the analysis beyond the immediate transaction.', 'Customers often pursue a functional outcome because of what that outcome makes possible afterwards.'],
         ask='What becomes possible, better or different for the customer once this outcome has been achieved?',
         egs=['A learner develops capability &rarr; to progress professionally, access opportunity or improve earning potential.',
              'A business secures reliable logistics &rarr; to maintain customer commitments and protect revenue.',
              'A mine acquires reliable equipment &rarr; to sustain production and avoid costly downtime.',
              'A customer manages money effectively &rarr; to maintain financial control and meet personal or business obligations.'],
         close=['The consequential dimension is especially important because it helps leaders see the result behind the result.']),
]
BOUNDARY_KINDS = [('Regulatory', 'laws, licences, standards, accreditation.'), ('Operational', 'processes, infrastructure, capacity, supply chains.'),
                  ('Technological', 'systems, data, interoperability, technical capability.'), ('Structural', 'governance, decision rights, organisational dependencies.'),
                  ('Financial', 'capital, affordability, economics, funding.'), ('Behavioural', 'capability, incentives, resistance, habits, adoption.')]
VP_TESTS = [('Relevance', 'Does it matter?', 'Does the value proposition address something important in the Customer End Game? If the customer does not materially value it, it is not an advantage.'),
            ('Distinctiveness', 'Does it differentiate?', 'Is there something meaningfully different about the value created, or can credible alternatives make essentially the same claim?'),
            ('Deliverability', 'Can we consistently produce it?', 'A promise becomes strategically valuable only when the organisation possesses the capability and system to deliver it repeatedly.')]
MBT2 = {   # the Must-Be-True question at each checkpoint, with Carol's example
    'a': ('Once Arena has been defined, ask:', 'What must remain true about customer need, behaviour or demand for this Arena to remain strategically relevant?',
          'Working professionals must continue to value externally validated capability strongly enough to invest time and money in acquiring it.', 'That is an assumption leadership can now monitor.'),
    'b': ('Now ask:', 'What must remain true operationally, structurally or regulatorily for this strategic direction to be deliverable?',
          'We must be able to approve and deploy new learning products within the timeframe demanded by the market.', 'Now the boundary is connected directly to strategic viability.'),
    'c': ('Once the competitive landscape has been established, ask:', 'What must remain true about our advantage relative to the customer&rsquo;s alternatives?',
          'Employers and learners must continue to perceive our credential and learning experience as sufficiently valuable to justify its additional time and cost relative to alternative capability pathways.',
          'That assumption can be monitored. If it begins to weaken, the strategy receives an early-warning signal.'),
    'v': ('Finally ask:', 'What must remain true about our value architecture for this proposition to remain relevant, distinctive and economically sustainable?',
          'Customers and employers must continue to place sufficient value on applied workplace integration to prefer Apex over lower-cost content-based alternatives.',
          'Again, the hidden assumption has become visible.'),
}
KR_ANCHOR = {'a': 'Which part of the Customer End Game does this Key Result serve: the functional outcome, the experience of achieving it, or what achieving it enables?'}   # Arena: the functional, emotional, social sentence is removed with the block Carol took out

# ── The worked example: the client services company of Unit 3, part 2.2 (Objectives and Key Results unchanged) ──
# Conditions: new, written for Carol's review.
WORKED = [
    dict(theme='Customer responsiveness', obj='Deliver consistently fast and effortless service experiences for customers', krs=[
        dict(id='1a', t='Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027',
             a='<strong>Experiential.</strong> Clients continue to rank speed of response among their top three reasons for choosing a service partner.',
             b='Handovers between Commercial, Operations and Customer Service are completed inside four hours.',
             c='A four-hour response remains faster than rival firms and clients&rsquo; in-house options provide.',
             v='Faster response is delivered with no loss in the quality of the answer the client receives.'),
        dict(id='1b', t='Increase customer requests resolved at first contact from 60% to 85% by 30 September 2027',
             a='Clients continue to value a request settled in a single contact.',
             b='Front-line staff hold the authority, the client information and the system access to resolve requests without referral.',
             c='Resolution at first contact remains something clients cannot obtain faster from a self-service alternative.',
             v='Requests closed at first contact stay closed; repeat contacts on the same request do not rise.'),
    ]),
    dict(theme='Execution speed', obj='Build a high-speed execution engine that moves quickly from insight to action', krs=[
        dict(id='2a', t='Reduce cross-functional decision time from 5 days to 1 day by 30 June 2027',
             a='Faster internal decisions shorten the time clients wait for an answer or a change.',
             b='Decision rights are delegated to the cross-functional forum, and governance and contract-approval rules allow a one-day decision.',
             c='Speed of decision remains an advantage clients notice when they compare the company with larger providers.',
             v='One-day decisions stay consistent with enterprise priorities, so that speed produces no conflicting commitments to clients.'),
        dict(id='2b', t='Reduce recurring management reports from 24 to 10 by 31 March 2027',
             a='No report removed carries information that account teams rely on to serve key accounts.',
             b='The ten remaining reports meet every regulatory, audit and board reporting obligation.',
             c='Leaner reporting keeps the company faster from insight to action than the larger providers its clients compare it with.',
             v='The ten reports give leaders the evidence needed to keep service consistent across teams.'),
    ]),
    dict(theme='Collaboration culture', obj='Create a culture of shared ownership across functions for strategic priorities', krs=[
        dict(id='3a', t='Increase enterprise priorities with a named cross-functional owner from 40% to 100% by 31 March 2027',
             a='The priorities being assigned are the ones that carry the client outcomes in the SiP statement.',
             b='Each named owner has the mandate and the capacity to lead across functions, and reporting lines and incentives support it.',
             c='Joined-up ownership remains an advantage clients do not find at larger, siloed providers.',
             v='Shared ownership strengthens one joined-up service, and accountability for each key account remains clear to the client.'),
        dict(id='3b', t='Reduce issues escalated to the executive team from 30 to 10 per quarter by 30 September 2027',
             a='Client-affecting issues are resolved faster at the level where they arise.',
             b='Managers below executive level hold the decision authority and the information to resolve issues, and escalation rules for regulatory matters stay intact.',
             c='Issues resolved below executive level are resolved at least as fast as clients expect from an alternative provider.',
             v='A lower count reflects issues resolved; no unresolved issue is held back from the executive team.'),
    ]),
    dict(theme='Value creation', obj='Strengthen enterprise performance through scalable and efficient operations', krs=[
        dict(id='4a', t='Improve operating margin from 14% to 18% by 31 December 2027',
             a='<strong>Consequential.</strong> Fast, consistent service continues to protect clients&rsquo; own operations, so they keep paying current price levels for it.',
             b='Salary, input and regulatory costs stay within the planning range.',
             c='Competitors and lower-cost alternatives force no price reduction in the core client segments.',
             v='No saving reduces the service quality clients choose the company for.'),
        dict(id='4b', t='Reduce leadership time spent on low-value projects from 25% to 10% by 30 June 2027',
             a='The projects classed as low-value are low-value to clients as well as to the company.',
             b='The company can exit or decline those projects within existing contract terms.',
             c='Declining low-value work gives competitors no entry point into key accounts.',
             v='The leadership time released is invested in fast, consistent and effortless service for the clients who rely on the company first.'),
    ]),
]
WORKED_SIP = 'We will be the service partner our clients rely on first, by ensuring every client experiences fast, consistent and effortless service.'
# One Key Result of the Unit 3 company, taken across the four steps. New, for Carol's review.
WORKED_KR = dict(
    obj='Deliver consistently fast and effortless service experiences for customers',
    kr='Reduce average response time to customer requests from 12 hours to 4 hours by 30 June 2027',
    fn='Have a service request answered and resolved.',
    ex='Fast and effortless: one contact, no chasing.',
    co='Keep their own operations running and their commitments to their own customers met.',
    a='Experiential: clients continue to rank speed of response among their top three reasons for choosing a service partner.',
    bounds=[('Requests that cross Commercial, Operations and Customer Service wait at each handover.', 'Operational', 'Created ourselves'),
            ('Front-line staff lack the authority and the client information to answer alone.', 'Behavioural', 'Created ourselves'),
            ('Each function records requests in its own system, with no shared view.', 'Technological', 'Created ourselves'),
            ('Request volumes peak at month-end.', 'Operational', 'Must accept')],
    b='Handovers between Commercial, Operations and Customer Service are completed inside four hours.',
    comp=['Rival client services firms.', 'Larger providers with round-the-clock service desks.', 'The client&rsquo;s own in-house team.',
          'Self-service tools that answer simple requests at once.', 'Doing nothing: the client lives with a slower answer.'],
    c='A four-hour response remains faster than rival firms and clients&rsquo; in-house options provide.',
    rel='Speed of response is among the main reasons clients choose a service partner.',
    dis='One joined-up team answers the request. Larger providers pass it between departments.',
    dlv='Cross-functional execution routines and named owners make a four-hour response repeatable.',
    v='Faster response is delivered with no loss in the quality of the answer the client receives.',
)
STEPS = [('Step 1', 'Define the Arena'), ('Step 2', 'Understand the Boundaries'), ('Step 3', 'See the Competition'), ('Step 4', 'Establish the Value Proposition')]
# The question of each step and its Must-Be-True question. {kr} is replaced by the Key Result, word for word (Carol, 7 Oct, round 4).
STEP_Q = ['Which customer need does {kr} serve: functional, experiential or consequential?',
          'Which conditions could materially slow, restrict or prevent us from delivering {kr}?',
          'Who or what else can give the customer what {kr} delivers?',
          'What about {kr} will make customers choose us?']
STEP_MBT = ['What must remain true about that functional, experiential or consequential need for {kr} to stay relevant?',
            'What must remain true operationally or regulatorily for us to deliver {kr} without breaking?',
            'What must remain true about the advantage {kr} gives us compared to these other options?',
            'What must remain true about our value architecture for {kr} to stay coherent and profitable?']
def kr_span(text):
    return '<span class="u4-krq">&ldquo;%s&rdquo;</span>' % text.strip().rstrip('.')
EXAMPLE_KRS = ['1a', '4a']   # the two Key Results carried through 1.1 to 1.4

def kr_by_id(i):
    for o in WORKED:
        for k in o['krs']:
            if k['id'] == i:
                return k
    raise KeyError(i)

# ── Section 2: the Industry Illusion (Carol's concept, word for word) ──
II_INTRO = [
    'Industry knowledge is essential to strategy. Over time, leaders build a deep understanding of how their industry works: its customers, competitors, economics, regulations, technologies and established ways of creating value.',
    'That knowledge also creates a frame through which leaders interpret their environment.',
    'The Industry Illusion occurs when that frame becomes so familiar that leaders begin to treat it as the boundary of what is strategically relevant.',
]
TRAPS = [
    dict(n=1, name='Familiarity', line='We know this industry.',
         body=['Experience creates confidence in our understanding of how the industry works. We know the established players, customer patterns, sources of value and indicators we normally monitor.',
               'The trap occurs when what we know becomes what we expect to continue seeing.'],
         risk='We interpret the future through patterns established by the past.'),
    dict(n=2, name='Exclusion', line='We discount what doesn&rsquo;t fit it.',
         body=['Once we have a familiar picture of the industry, developments that fit that picture receive our attention.',
               'Signals that sit outside it can appear less relevant because they do not resemble the customers, competitors, technologies or business models we associate with our industry.',
               'The trap is that we may see the signal but exclude it from serious strategic consideration.'],
         risk='What does not fit our industry frame gets underestimated.'),
    dict(n=3, name='Complacency', line='We become confident in the world we can see.',
         body=['When the organisation continues to perform, our established view of the industry appears to be validated.',
               'Market position, reputation, customer demand or past success can reinforce the belief that we understand what matters.',
               'The trap occurs when evidence of current success becomes reassurance about future relevance.'],
         risk='We continue looking in the same places because nothing has yet forced us to look elsewhere.'),
]
II_BOUNDARY = 'The industry we understand becomes the boundary of the world we examine.'

GAME = dict(
    title='The Future of a University',
    brief_lead='Apex University is an established private university.',
    brief_has=['18,000 students', 'Strong undergraduate and postgraduate programmes', 'Recognised accreditation', 'A respected business school',
               'Growing online delivery', 'Strong relationships with employers', 'Good graduate employment outcomes', 'Stable enrolment'],
    brief_board='The Board is beginning development of the university&rsquo;s 2032 Strategy.',
    brief_task='Your task is to advise the Board on where it should focus its strategic attention.',
    r1_title='Where would you look?',
    r1_prompt='You have been asked to understand how Apex University&rsquo;s environment is changing. Where would you look for intelligence?',
    r1_do='Select FOUR that you would prioritise.',
    sources=[('A', 'Enrolment trends across universities'), ('B', 'New programmes being introduced by competing universities'),
             ('C', 'Changes in university rankings and reputation'), ('D', 'Higher-education regulation and accreditation changes'),
             ('E', 'Changes in how major employers assess and recruit talent'), ('F', 'Growth in professional and industry credentials'),
             ('G', 'How working adults are building new capabilities outside formal education'),
             ('H', 'Changes in how employers recognise demonstrated skills versus qualifications')],
    r2_title='What deserves attention?',
    r2_prompt='Your strategy team has brought six developments to the executive committee. You only have capacity to investigate THREE in depth.',
    r2_q1='Which THREE warrant immediate strategic investigation?', r2_q2='Which THREE would you deprioritise?',
    signals=['A competing university has launched a new Executive MBA.',
             'Applications to universities in your region are projected to grow by 8%.',
             'Several major employers are removing degree requirements from selected roles and introducing capability assessments.',
             'Working professionals are increasingly combining short courses, professional certifications and workplace experience in place of longer qualifications.',
             'A leading university has reduced fees for several postgraduate programmes.',
             'Employers are increasingly using portfolios, simulations and demonstrated capability to evaluate candidates.'],
    r3_title='Should we be worried?',
    r3_report_title='Apex University: current position',
    report=[('Enrolment', '+5%'), ('Revenue', '+7%'), ('Graduate employment', '86%'), ('Accreditation', 'Strong'), ('Student satisfaction', '82%'),
            ('Market position', 'Top 3 private university'), ('Online enrolment', '+12%')],
    r3_prompt='The Board asks whether the university needs to reconsider its fundamental strategic direction.',
    choices=[('A', 'No major change', 'Our position remains strong. Continue executing the current strategy.'),
             ('B', 'Adjust', 'Our strategy remains sound, but some areas need strengthening.'),
             ('C', 'Re-examine', 'Current performance is strong, but we should question whether the assumptions underlying our future position remain valid.')],
    reveal=[dict(round='Round 1', ask='Where did you look?', trap='Familiarity', line='We know this industry.',
                 q='How much of your attention went toward the world you already recognised as higher education?'),
            dict(round='Round 2', ask='What did you exclude?', trap='Exclusion', line='We discount what doesn&rsquo;t fit it.',
                 q='Which signals did you deprioritise because they appeared to sit outside the conventional higher-education environment?'),
            dict(round='Round 3', ask='What reassured you?', trap='Complacency', line='We become confident in the world we can see.',
                 q='Did strong current performance influence how urgently you believed the university needed to question its future?')],
    insight='Apex did not lack information. The question is what its industry frame caused leaders to notice, dismiss and trust.',
    arena_q='What is the Apex learner actually trying to achieve?',
    arena=[('Functional', 'What are they trying to achieve?'), ('Experiential', 'What matters about how they achieve it?'),
           ('Consequential', 'What does achieving it ultimately enable?')],
    final='Now look again at everything you deprioritised in Rounds 1 and 2. Does defining the Arena around the customer&rsquo;s end game change what you consider strategically relevant?',
    tests=['Familiarity. Do participants gravitate toward A to D because these are recognisably higher-education indicators?',
           'Exclusion. Are signals 3, 4 and 6 discounted because they do not initially look like developments inside higher education?',
           'Complacency. Does strong current performance reassure participants that the university understands its future? Choice A is a reasonable answer on the page: the numbers genuinely look good.'],
)

# ── Section learning outcomes: as on the pages on 7 October (Carol has not approved any change) ──
SLO = {
    1: ('Recognise why well-formulated objectives can still lack strategic credibility.', 'Distinguish objectives that are measurable from those that are strategically coherent.'),
    2: ('Judge whether strategic priorities respond to the outcomes customers pursue.', 'Articulate the assumptions on which each strategic objective depends.'),
    4: ('Appraise the assumptions, dependencies and uncertainties behind the organisation&rsquo;s strategic objectives.', 'Demonstrate collective accountability by assigning ownership for verifying critical conditions.'),
    5: ('Evaluate realistic strategic failures to diagnose where directional integrity broke down.', 'Judge which integrity checkpoint would have protected the chosen direction.'),
}

# ── Static blocks used by both pages ──
def _ps(items): return ''.join('    <p>%s</p>\n' % x for x in items)
def _ul(items): return '    <ul>' + ''.join('<li>%s</li>' % x for x in items) + '</ul>\n'
def _chips(items): return '    <div class="u4-chips">' + ''.join('<span>%s</span>' % x for x in items) + '</div>\n'
def _ask(q): return '    <div class="u4-ask"><span>Ask</span>%s</div>\n' % q
def _mbt(k, label):
    lead, q, eg, close = MBT2[k]
    return ('    <div class="u4-mbt"><div class="u4-row-l">%s</div><p class="u4-mbt-lead">%s</p><p>%s</p>'
            '<p class="u4-mbt-eg"><strong>Example:</strong> %s</p><p class="u4-mbt-eg">%s</p></div>\n' % (label, lead, q, eg, close))
def _kr_block(c, examples_label):
    k = c['k']
    anchor = KR_ANCHOR.get(k, c['anchor'])
    rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % (kr_by_id(i)['t'], kr_by_id(i)[k]) for i in EXAMPLE_KRS)
    return ('    <div class="u4-krbox"><div class="u4-krbox-h">%s &middot; applied to a Key Result</div>\n'
            '      <p><strong>Ask of the Key Result:</strong> %s</p>\n'
            '      <p><strong>Then name the condition:</strong> %s</p>%s\n'
            '      <div class="u4-egs-h" style="margin-top:12px;">%s</div>\n'
            '      <table class="u4-tbl"><thead><tr><th>Key Result</th><th>%s &middot; Must-Be-True condition</th></tr></thead><tbody>%s</tbody></table></div>\n'
            % (c['name'], anchor, c['mbt'], ('\n      <p class="u4-mbt-eg">%s</p>' % c['mbt_eg']) if c['mbt_eg'] else '', examples_label, c['name'], rows))
def _depths():
    out = []
    for d in DEPTHS:
        out.append('    <div class="u4-trap%s" onclick="this.classList.toggle(\'open\')"><div class="u4-trap-h"><span class="u4-trap-n">%d</span>'
                   '<div><div class="u4-trap-name">%s</div><div class="u4-trap-line">%s</div></div><span class="u4-obj-a">&#9662;</span></div>\n'
                   '    <div class="u4-trap-b">%s%s<div class="u4-ask"><span>Ask</span>%s</div><div class="u4-egs-h" style="margin-top:12px;">Examples</div><ul>%s</ul>%s</div></div>\n'
                   % (' open' if d['n'] == 1 else '', d['n'], d['name'], d['q'], ''.join('<p>%s</p>' % x for x in d['body']),
                      ('<div class="u4-chips">' + ''.join('<span>%s</span>' % x for x in d['chips']) + '</div>') if d.get('chips') else '',
                      d['ask'], ''.join('<li>%s</li>' % x for x in d['egs']), ''.join('<p>%s</p>' % x for x in d['close'])))
    return ''.join(out)
def _minichain(items, end=None):
    h = ''.join('<div class="u4-chain-s"><b>%s</b><span>%s</span></div>%s' % (a, b, '<div class="u4-chain-a">&darr;</div>' if n < len(items) - 1 or end else '') for n, (a, b) in enumerate(items))
    if end: h += '<div class="u4-chain-end"><b>%s</b><span>%s</span></div>' % end
    return '    <div class="u4-chain">%s</div>\n' % h

def cp_part_body(c, examples_label):
    """Teaching content of one checkpoint part (1.1 to 1.4), the same on both pages."""
    k = c['k']
    o = ['  <div class="u4-cp %s">\n' % c['cls'], '    <div class="u4-q">%s</div>\n' % HEAD_Q[k],
         '    <div class="u4-row"><div class="u4-row-l">Strategic Logic</div><p>%s</p></div>\n' % c['logic']]
    if k == 'a':
        o += [_ps(['Arena defines the space in which value is being sought and contested.',
                   'Organisations naturally describe themselves through what they produce or the industry in which they operate:']),
              _chips(['We are a university.', 'We are a bank.', 'We are a mine.', 'We provide insurance.']),
              _ps(['Those descriptions tell us something important about the organisation. They do not necessarily tell us what the customer is ultimately trying to accomplish.',
                   'This is where the Industry Illusion can distort strategic thinking. Familiarity with an industry can become the boundary of what leaders examine. Section 2 takes this further.',
                   SMARTPHONE]),
              '    <div class="u4-quote"><p>%s</p></div>\n' % ARENA_QUOTE,
              _ps(['Arena deliberately returns attention to the Customer End Game.', 'To understand that end game properly, interrogate it at three depths.']),
              _depths(),
              '    <h4>Reading the Three Together</h4>\n',
              _ps(['These are not three separate customer needs that must be artificially created. They are three depths of interrogation:']),
              _minichain([(d['name'], d['q']) for d in DEPTHS]),
              _ps(['Together, they help define the Customer End Game.']),
              '    <div class="u4-eg-box"><div class="u4-row-l">Example &middot; Higher Education</div>'
              '<p><strong>Functional:</strong> Build relevant and credible capability.</p><p><strong>Experiential:</strong> Do so through learning that is flexible, accessible and compatible with work.</p>'
              '<p><strong>Consequential:</strong> Translate that capability into career progression and economic opportunity.</p>'
              '<p>The Arena can therefore be expressed as:</p><p class="u4-eg-st">Enabling working professionals to build credible capability, in ways compatible with their working lives, that advances career and economic opportunity.</p>'
              '<p>Now the organisation has a much richer strategic space to interrogate than simply: &ldquo;We provide postgraduate education.&rdquo;</p></div>\n',
              _mbt('a', 'Arena MBT')]
    elif k == 'b':
        o += [_ps(['Defining the right Arena does not mean the organisation can automatically succeed within it.',
                   'Every strategic choice operates within conditions that enable, restrict or shape what can actually be delivered. These are Boundaries.']),
              '    <div class="u4-quote"><p>What could push back against our ability to achieve the intended outcome?</p></div>\n',
              _ps(['Boundaries may be:']),
              '    <div class="u4-kinds">' + ''.join('<div class="u4-kind"><b>%s</b><span>%s</span></div>' % x for x in BOUNDARY_KINDS) + '</div>\n',
              _ps(['The purpose is not to produce a long risk register.', 'We are looking for boundaries material enough to affect the strategic outcome.']),
              '    <div class="u4-eg-box"><div class="u4-row-l">Example &middot; Higher Education</div><p>Our university Arena requires flexible capability development for working professionals. But:</p>'
              '<ul><li>Programme approvals take 12 months.</li><li>Faculty contracts are designed around semesters.</li><li>Systems require fixed annual enrolment periods.</li><li>Accreditation limits how credentials can be structured.</li></ul>'
              '<p>These conditions do not invalidate the Arena. They reveal the friction architecture surrounding it.</p></div>\n',
              '    <h4>The Strategic Question</h4>\n', _ask('Which conditions could materially slow, restrict or prevent us from delivering the customer end game we have defined?'),
              _ps(['Then distinguish between:']),
              '    <div class="u4-three"><div class="u4-three-c"><div class="u4-three-h">A boundary we must accept</div><p>For example, legislation.</p></div>'
              '<div class="u4-three-c"><div class="u4-three-h">A boundary we can influence</div><p>Perhaps an industry standard.</p></div>'
              '<div class="u4-three-c"><div class="u4-three-h">A boundary we created ourselves</div><p>Perhaps an internal process, structure or policy.</p></div></div>\n',
              _ps(['That last one can generate particularly useful executive discussion.']),
              _mbt('b', 'Boundary MBT')]
    elif k == 'c':
        o += [_ps(['Competition follows Arena deliberately.',
                   'If leaders define Arena through their industry, they will probably identify competitors through their industry. If Arena is defined around the Customer End Game, the competitive field can look very different.',
                   'Competition therefore asks:']),
              '    <div class="u4-quote"><p>Who or what else can enable the customer to achieve this end game?</p></div>\n',
              _ps(['The competitor does not have to:']), _chips(['look like us', 'sell the same product', 'use the same business model', 'belong to the same industry']),
              _ps(['It only needs to offer the customer a credible alternative route to the outcome.']),
              '    <div class="u4-eg-box"><div class="u4-row-l">Example &middot; Higher Education</div><p>If we say &ldquo;We provide postgraduate qualifications&rdquo;, we will probably compare ourselves with other universities.</p>'
              '<p>But our Arena has now been defined more deeply: build credible capability &rarr; flexibly &rarr; to advance career opportunity. Now ask: who or what else can enable that? The landscape may include:</p>'
              '<ul><li>Professional bodies.</li><li>Corporate academies.</li><li>Industry certifications.</li><li>Specialist training providers.</li><li>Digital learning platforms.</li><li>Employer-led development.</li><li>Alternative credential providers.</li></ul>'
              '<p>And potentially emerging models we have not historically classified as higher education.</p></div>\n',
              _ps(['This is exactly where the Industry Illusion becomes strategically important. Something that was excluded because &ldquo;that&rsquo;s not our industry&rdquo; may become highly relevant once Arena has been correctly defined.']),
              '    <h4>Competition Is About Alternatives</h4>\n', _ps(['The critical distinction is:']),
              '    <div class="u4-versus"><div>Who sells something similar to us?</div><span>versus</span><div>What alternatives does the customer have for achieving the end game?</div></div>\n',
              _ps(['This also means competition can sometimes be:']),
              _chips(['Do it internally.', 'Do it themselves.', 'Use technology instead.', 'Postpone it.', 'Choose a completely different solution.', 'Do nothing.']),
              _ps(['The customer is choosing between routes to an outcome, not merely between organisations in a category.']),
              _mbt('c', 'Competition MBT')]
    else:
        o += [_ps(['Arena established what the customer is ultimately trying to achieve. Boundaries established the conditions within which we must deliver it. Competition revealed the alternatives available to the customer.',
                   'Value Proposition now asks:']),
              '    <div class="u4-quote"><p>Given those alternatives, why should the customer choose us?</p></div>\n',
              _ps(['This is where strategic distinctiveness enters the interrogation.', 'A Value Proposition is more than a description of what the organisation offers. Statements such as:']),
              _chips(['high quality', 'customer focused', 'innovative', 'excellent service', 'experienced people']),
              _ps(['may all be positive attributes. They do not automatically establish strategic value.', 'The real interrogation is:']),
              '    <div class="u4-quote"><p>What combination of value do we create that matters to this customer, in this Arena, relative to the alternatives available?</p></div>\n',
              '    <h4>Three Tests of the Value Proposition</h4>\n',
              '    <div class="u4-three">' + ''.join('<div class="u4-three-c"><div class="u4-three-h">%s</div><p><strong>%s</strong> %s</p></div>' % t for t in VP_TESTS) + '</div>\n',
              '    <div class="u4-formula">RELEVANT + DISTINCTIVE + DELIVERABLE = STRATEGIC VALUE</div>\n',
              '    <div class="u4-eg-box"><div class="u4-row-l">Example &middot; Higher Education</div><p>Suppose Apex says: &ldquo;We provide high-quality executive education.&rdquo; That is positive but strategically weak. Interrogate it.</p>'
              '<p><strong>Relevant?</strong> Working executives value capability that translates into workplace performance.</p>'
              '<p><strong>Distinctive?</strong> Apex integrates real organisational strategy challenges into assessed learning.</p>'
              '<p><strong>Deliverable?</strong> Its faculty, practitioner network and learning architecture consistently support applied workplace learning.</p>'
              '<p>The value proposition becomes more meaningful:</p><p class="u4-eg-st">Applied, credible executive capability development built around real organisational challenges and designed for working professionals.</p>'
              '<p>Now there is something that can actually be tested against alternatives.</p></div>\n',
              _mbt('v', 'Value Proposition MBT')]
    o += [_kr_block(c, examples_label), '  </div>']
    return ''.join(o)

def together_html():
    """Bringing ABCV Together: the integrated view after 1.4, the same on both pages."""
    items = [('A &mdash; Arena', 'What is the customer ultimately trying to achieve?<br><em>Functional &rarr; Experiential &rarr; Consequential</em>'),
             ('B &mdash; Boundaries', 'What could constrain our ability to deliver that outcome?'),
             ('C &mdash; Competition', 'Who or what else can enable the customer to achieve it?'),
             ('V &mdash; Value Proposition', 'Why should the customer choose the value we create?')]
    return (_minichain(items, ('MBT &mdash; Must Be True', 'What conditions must hold for our strategic logic to remain valid?')) +
            '    <div class="u4-quote"><p>ABCV does not ask whether an OKR is well written. It asks whether the strategic logic underneath it can survive reality.</p></div>\n')

def worked_html(prefix):
    """4.1: one Key Result taken across the four steps, read-only, the same on both pages. Each step ends with its Must-Be-True condition."""
    W = WORKED_KR
    def qa(label, text): return '<div class="u4-qa"><span>%s</span><p>%s</p></div>' % (label, text)
    KR = kr_span(W['kr'])
    def mbt(n, text): return '<div class="u4-stepout"><span>%s &middot; Must-Be-True</span><small>%s</small><p>%s</p></div>' % (CHECKPOINTS[n]['name'], STEP_MBT[n].replace('{kr}', KR), text)
    p = [qa('Functional &middot; What does the customer need done that this Key Result serves?', W['fn']) + qa('Experiential &middot; What matters to the customer about how it is done?', W['ex']) +
         qa('Consequential &middot; What does this Key Result enable for the customer?', W['co']) + mbt(0, W['a']),
         '<table class="u4-tbl u4-tbl3"><thead><tr><th>Boundary</th><th>Kind</th><th>Accept, influence or self-created</th></tr></thead><tbody>' +
         ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % x for x in W['bounds']) + '</tbody></table>' + mbt(1, W['b']),
         '<ul class="u4-plain">' + ''.join('<li>%s</li>' % x for x in W['comp']) + '</ul>' + mbt(2, W['c']),
         qa('Relevant &middot; Does this Key Result matter to the customer?', W['rel']) + qa('Distinctive &middot; What does it give the customer that the alternatives do not?', W['dis']) +
         qa('Deliverable &middot; Can we consistently produce it?', W['dlv']) + mbt(3, W['v'])]
    gid = prefix + 'Steps'
    tabs = '<div class="u4-stages">' + ''.join(
        '<div class="u4-stage%s" onclick="u4Tab(\'%s\',%d)"><small>%s</small>%s</div>' % (' active' if n == 0 else '', gid, n, a, b) for n, (a, b) in enumerate(STEPS)) + '</div>'
    panels = ''.join('<div class="u4-panel u4-wpanel%s"><h5>%s &middot; %s</h5><p class="u4-say">%s</p>%s</div>' % (' active' if n == 0 else '', STEPS[n][0], STEPS[n][1], STEP_Q[n].replace('{kr}', KR), body)
                     for n, body in enumerate(p))
    head = ('<div class="u4-okrs"><div class="u4-egs-h">From Unit 3 &middot; the Key Result being tested</div><div class="u4-okr"><b>Objective</b> %s<ul><li><span>Key Result</span>%s</li></ul></div></div>' % (W['obj'], W['kr']))
    return '  ' + head + '\n  <div class="u4-wsteps" id="%s">%s%s</div>' % (gid, tabs, panels)

def traps_html():
    out = []
    for t in TRAPS:
        out.append('  <div class="u4-trap%s" onclick="this.classList.toggle(\'open\')"><div class="u4-trap-h"><span class="u4-trap-n">%d</span>'
                   '<div><div class="u4-trap-name">%s</div><div class="u4-trap-line">%s</div></div><span class="u4-obj-a">&#9662;</span></div>\n'
                   '    <div class="u4-trap-b">%s<div class="u4-risk"><span>Strategic risk</span>%s</div></div></div>'
                   % (' open' if t['n'] == 1 else '', t['n'], t['name'], t['line'], ''.join('<p>%s</p>' % p for p in t['body']), t['risk']))
    return '\n'.join(out)

def chain_html():
    steps = ''.join('<div class="u4-chain-s"><b>%s</b><span>%s</span></div><div class="u4-chain-a">&darr;</div>' % (t['name'], t['line']) for t in TRAPS)
    return '  <div class="u4-chain">%s<div class="u4-chain-end"><b>Industry Illusion</b><span>%s</span></div></div>' % (steps, II_BOUNDARY)

def industry_illusion_teaching():
    """2.1: the concept, the same on both pages."""
    return '\n'.join(['  <p>%s</p>' % p for p in II_INTRO] + [
        '  <p>It develops through three reinforcing traps:</p>',
        traps_html(),
        '  <h4>How the Industry Illusion Forms</h4>',
        chain_html()])

def brief_html():
    g = GAME
    return ('<div class="u4-brief"><div class="u4-brief-h">Case Brief &middot; %s</div>\n'
            '    <p>%s Apex has:</p><ul>%s</ul><p>%s</p><p><strong>%s</strong></p></div>'
            % (g['title'], g['brief_lead'], ''.join('<li>%s</li>' % x for x in g['brief_has']), g['brief_board'], g['brief_task']))

def report_html():
    g = GAME
    return ('<table class="u4-tbl u4-report"><thead><tr><th colspan="2">%s</th></tr></thead><tbody>%s</tbody></table>'
            % (g['r3_report_title'], ''.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in g['report'])))

# ── Section 5: Cause of Death, tested against the Industry Illusion (Carol, 7 October, evening) ──
# The investigation question reveals the illusion at work; the ABCV checkpoint is where that illusion sits.
# Scenario wording adjusted so that each one carries one clear illusion; the pairing is new, for Carol's review.
ILLUS = [
    dict(k='fam', name='Familiarity', line='We know this industry.', q='What did leaders expect to continue seeing because it was what they already knew?'),
    dict(k='exc', name='Exclusion', line='We discount what doesn&rsquo;t fit it.', q='Which signal did leaders see and then discount because it did not fit their established picture?'),
    dict(k='com', name='Complacency', line='We become confident in the world we can see.', q='Which evidence of current success did leaders treat as reassurance about the future?'),
]
SITS = [('Arena', 'arena', 'The illusion hid a change in what the customer is trying to achieve.'),
        ('Boundaries', 'boundaries', 'The illusion hid a condition that constrains delivery.'),
        ('Competition', 'competition', 'The illusion hid an alternative open to the customer.'),
        ('Value Proposition', 'valueprop', 'The illusion hid the erosion of the reason customers choose the organisation.')]
MINES = [
    dict(name='The Ghost Ship', ill='com', cp='ARENA', cpname='Arena', col='#8ab0e8',
         scenario='A SaaS platform achieved 85% retention in year one. Support tickets were low and the platform worked exactly as designed. Leadership read these numbers as proof that customers were committed, and kept the product as it was. By year three, churn reached 70%. Post-exit interviews revealed: customers had changed what they were trying to achieve &mdash; and the platform never followed.',
         insight='Strong retention and a quiet support desk reassured leaders that customers were committed. The customer end game had shifted, and nobody was asking what customers were now trying to achieve.'),
    dict(name='The Ferrari in the Mud', ill='fam', cp='BOUNDARIES', cpname='Boundaries', col='#f0c060',
         scenario='A leading logistics firm invested R120m in a new digital operations platform. It had rolled out systems before and ran this one the way it always had: build, train once, switch over. Eighteen months in, less than 30% of staff were using it consistently. Field teams had developed workarounds. Middle management had quietly reverted to spreadsheets. The system was technically excellent. The organisation was not designed to absorb it.',
         insight='Leaders expected this roll-out to go the way earlier ones had. The behavioural and structural boundaries (habits, incentives, middle-management routines) were never mapped.'),
    dict(name='The Invisible Disruption', ill='exc', cp='COMPETITION', cpname='Competition', col='#5ecba1',
         scenario='A financial advisory firm reviewed its rival advisory firms every quarter. Two years ago its strategy team noticed a fintech app and left it out of the review: it was software, and the firm competed with advisers. Then revenue began declining. No rival firm had taken their clients. No scandal. No service failure. The app was letting clients self-manage what the firm had always managed for them &mdash; and clients preferred it for 60% of use cases.',
         insight='The firm saw the app and discounted it because it did not look like an advisory firm. Clients had an alternative route to the same outcome.'),
    dict(name='The Identity Crisis', ill='com', cp='VALUE PROPOSITION', cpname='Value Proposition', col='#c39de0',
         scenario='A boutique consulting firm built its reputation on deep-sector expertise and bespoke strategy work. Under revenue pressure, it began accepting large implementation contracts &mdash; work that paid well but required different skills, different team profiles, and a different culture. Revenue rose every quarter, and the partners took the growth as confirmation that the firm was stronger than ever. Within two years, it had won more work but lost its most experienced strategists and its distinctiveness with clients who valued exactly what it had been.',
         insight='Rising revenue reassured the partners while the work they accepted diluted what made the firm distinct.'),
]
def illus(k): return [x for x in ILLUS if x['k'] == k][0]
def illus_html():
    return '<div class="u4-illus">' + ''.join('<div><b>%s</b><span>%s</span><em>Q%d reveals it: %s</em></div>' % (x['name'], x['line'], i + 1, x['q']) for i, x in enumerate(ILLUS)) + '</div>'
def sits_html():
    return '<div class="u4-four">' + ''.join('<div class="u4-four-c %s"><b>%s</b><span>%s</span></div>' % (c, n, t) for n, c, t in SITS) + '</div>'
