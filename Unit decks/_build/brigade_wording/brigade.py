# -*- coding: utf-8 -*-
"""Carol, 13 October 2026: replace "the Alignment Brigade" with "the collective intelligence for execution discipline" (of the leadership team), as done in Unit 8.
Rules, applied in this order; every occurrence must be caught (the script stops if one is left).
  Names and headings  -> "The Collective Intelligence for Execution Discipline"
  "Alignment Brigade Challenge" (Unit 9 exercise) -> "Collective Intelligence Challenge"
  "escalate to (the) Alignment Brigade" -> "escalate to the leadership team"
  The Brigade as the one who acts -> "the leadership team, acting as the collective intelligence for execution discipline,"
"""
import re
CI = 'the collective intelligence for execution discipline'
T = 'The Collective Intelligence for Execution Discipline'
ACT = 'the leadership team, acting as %s,' % CI
RULES = [
    (r'The Alignment Brigade Challenge', 'The Collective Intelligence Challenge'),
    (r'Alignment Brigade Challenge', 'Collective Intelligence Challenge'),
    (r'(?<!Alignment )(?<!The )Brigade Challenge', 'Collective Intelligence Challenge'),
    (r'THE ALIGNMENT BRIGADE CHALLENGE', 'THE COLLECTIVE INTELLIGENCE CHALLENGE'),
    (r'THE ALIGNMENT BRIGADE', T.upper()),
    (r'escalate to (?:the )?Alignment Brigade', 'escalate to the leadership team'),
    (r'a direct measure of Alignment Brigade dysfunction', 'a direct measure of dysfunction in %s of the leadership team' % CI),
    (r'<strong>The Alignment Brigade</strong>, more than', '<strong>%s</strong>, more than' % CI),
    (r'<strong>Alignment Brigade</strong> concept', '<strong>%s</strong> concept' % CI[4:]),
    (r'The Alignment Brigade concept', 'The %s concept' % CI[4:]),
    (r'The Alignment Brigade (·|&middot;) ', T + r' \1 '),
    (r'(&mdash;|—|·) The Alignment Brigade(?=[:<\s—&)]|$)', r'\1 ' + T),
    (r'<h2>The Alignment Brigade &mdash;', '<h2>%s &mdash;' % T),
    (r'<h2>Alignment Brigade &mdash;', '<h2>%s &mdash;' % T),
    (r'^The Alignment Brigade — ABCV', T + ' — ABCV'),
    (r'\(the Alignment Brigade across', '(%s across' % CI),
    (r'The Alignment Brigade (shows|maps) ', r'The %s \1 ' % CI[4:]),
    (r'On the Alignment Brigade:', 'On %s:' % CI),
    (r'operates as an Alignment Brigade', 'operates as %s' % CI),
    (r'the entire Alignment Brigade operates', 'the entire leadership team, acting as %s, operates' % CI),
    (r'The Alignment Brigade ', ACT[0].upper() + ACT[1:] + ' '),
    (r'the Alignment Brigade ', ACT + ' '),
    (r'the Alignment Brigade\.', 'the leadership team.'),
]
def fix(s):
    for a, b in RULES: s = re.sub(a, b, s, flags=re.M)
    return s
