# -*- coding: utf-8 -*-
"""Section 1 addition (Carol approved 27 Oct 18:19): ESRG Alignment and Strategic Unclogging, when to use each."""
TITLE = 'ESRG Alignment and Strategic Unclogging: When to Use Each'
P1_P = 'In Unit 9 you used Strategic Unclogging to clear clogs: blockages that slow a Key Result already in execution. You read each clog through its performance outcome, the behaviour around it and the condition behind it, across people performance and organisational performance. You cleared it with a Strategic Unclogging Lever and the Review–Realign–Restore cycle.'
P1_F = 'In Unit 9 participants used Strategic Unclogging to clear clogs: blockages that slow a Key Result already in execution. They read each clog through its performance outcome, the behaviour around it and the condition behind it, across people performance and organisational performance. They cleared it with a Strategic Unclogging Lever and the Review–Realign–Restore cycle.'
P2 = 'ESRG Alignment works on the organisational operating conditions themselves. It starts from a strategic commitment and the demand that commitment places on the Environment, Systems, Resources and Governance. Its purpose is to build the organisational capability that carries the strategy. Leaders specify the conditions before demand arrives, score them on a fixed schedule and strengthen them through targeted organisational alignment interventions.'
ROWS = [('Use it when','A Key Result is slowing and friction signals show in results or behaviour','A strategic commitment is approved, launched or scaled, and at each annual baseline and quarterly recalibration'),
        ('Question it answers','What is blocking this result, and how do we clear it?','Can our operating conditions carry this commitment, and where must we build capability?'),
        ('What it covers','People performance and organisational performance','Organisational operating conditions (ESRG)'),
        ('Leaders’ response','Select an Unclogging Lever and run Review–Realign–Restore','Coordinate, reconcile or align, and design targeted organisational alignment interventions')]
FEED = 'The two disciplines feed each other in three ways:'
FEED_L = ['A clog traced to an organisational condition becomes an ESRG component to score and strengthen.',
          'Recurring clogs in the same component show a capability gap the next annual baseline must address.',
          'A component that scores low at a quarterly recalibration shows leaders where clogs are likely to form, so they can act before Key Results slow.']
ILL = 'A service team’s response-time Key Result slips for three weeks because cases wait between the sales and operations platforms. Strategic Unclogging clears the backlog: leaders realign the handover and restore the response time. At the next recalibration, ESRG Alignment shows the same low Integration score in three functions. The executive team then agrees a shared integration requirement so the clog does not return.'

def block(fac):
    from u10_content import acc
    t = ('<table class="u10-tbl u10-when"><thead><tr><th></th><th>Strategic Unclogging</th><th>ESRG Alignment</th></tr></thead><tbody>\n'
         + '\n'.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in ROWS) + '\n</tbody></table>')
    body = '\n'.join(['<p>%s</p>' % (P1_F if fac else P1_P), '<p>%s</p>' % P2, '<div class="u10-scroll">%s</div>' % t.replace('<table class="u10-tbl', '<table style="min-width:620px" class="u10-tbl', 1),
                      '<p>%s</p><ul class="u10-ul">%s</ul>' % (FEED, ''.join('<li>%s</li>' % x for x in FEED_L)),
                      '<p><strong>Illustration:</strong> %s</p>' % ILL])
    return acc(TITLE, body, False)
CSS = '.u10-when td:first-child{width:20%;}\n.u10-ul{margin:0 0 12px 20px;}\n.u10-ul li{font-size:14px;line-height:1.85;color:rgba(255,255,255,.72);margin-bottom:4px;}\n'
