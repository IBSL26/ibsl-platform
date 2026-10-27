# -*- coding: utf-8 -*-
"""Unit 11 · Cultural Operating Code (Carol, 27 Oct 22:37): Section 4 part 4.7 teaches building a Cultural Operating Code from values,
with the IBSL worked example (AIM, SAY, ONE, OAR, SET, SEE, from the Unit 10 backup); Section 5 part 5.8: the group builds its Code
from its organisation's values (shared group record, Capstone 11E)."""
from u11_content import acc, det

T47 = '4.7 &mdash; From Values to a Cultural Operating Code'
P47 = [
 'Organisational health reflects the behaviours that have become normal in each function. Stated values shape those behaviours only when people can see what each value requires of them, practise it and be held to it. A Cultural Operating Code makes this explicit: for each organisational value, it names one norm built from three observable actions that every leader and employee can recognise, use and be assessed against.',
 'The Code connects the health architecture to daily leadership practice. When executives model, recognise and correct behaviour against the same norms, the conditions the Organisational Health Thermometer measures begin to change: shared accountability reduces politics, explicit expectations reduce confusion, and consistent consequences protect morale.',
]
STEPS_H = 'How a value becomes a norm'
STEPS = [('Define the behaviour', 'Describe what a leader who genuinely lives the value does differently from one who only states it. Write the answer as a specific, observable behaviour.'),
         ('Build the acronym', 'Take the first letters of three action words that capture the behaviour. Each word is an action a person performs. The acronym is short enough to use in a corridor conversation.'),
         ('Write the norm statement', 'One sentence explaining what the value means in daily practice, specific enough that a new employee reading it on the first day knows which behaviour will be recognised and which will be corrected.')]
EMBED_H = 'What makes the Code real'
EMBED = ['<strong>Demonstrable:</strong> every value is translated into observable, specific behaviours.',
         '<strong>Assessed:</strong> the norms appear in 360-degree feedback, so how results are achieved is assessed alongside what is achieved.',
         '<strong>Enforced:</strong> consequences apply consistently regardless of seniority.',
         '<strong>Maintained:</strong> norms are explicit, modelled by executives, reinforced in reviews and revisited periodically.']
TESTS_H = 'Three tests for every norm'
TESTS = [('The New Employee Test', 'Would a new employee reading this norm on the first day know exactly which behaviour will be recognised and which will be corrected?'),
         ('The Pressure Test', 'Does the norm hold when a senior leader breaches it, when a high performer contradicts it, and when telling the truth is costly?'),
         ('The Mirror Test', 'Would every executive be comfortable being assessed against this norm in their own 360-degree feedback?')]
WE_H = 'Worked example · The IBSL Cultural Operating Code'
WE_INTRO = 'IBSL’s values: <strong>Intentionality · Integrity · Collaboration · Accountability · Excellence · Human-Centricity</strong>. Each value carries one acronym-based norm.'
IBSL = [('Intentionality', 'Leading with purpose, clarity and discipline', 'AIM', 'Act with purpose · Interrogate assumptions · Maintain the discipline',
         'Intentionality is the discipline of knowing exactly why you are doing what you are doing, and holding that line when conditions make it inconvenient.',
         'Before your last three major commitments, could you state the strategic purpose, the assumption you were making and the standard you held yourself to?'),
        ('Integrity', 'Consistency between words, behaviour and outcomes', 'SAY', 'Say what you mean · Act on what you say · Yield the truth regardless of consequence',
         'Integrity is consistency between word, behaviour and outcome, including when telling the truth is uncomfortable. What we say and what we do are the same thing.',
         'In your last performance review, did you name what was promised, what was delivered and what the gap cost before being asked?'),
        ('Collaboration', 'Leveraging diversity of thought and collective intelligence', 'ONE', 'Own a shared outcome · Navigate difference with respect · Execute as a unified force',
         'Collaboration is the decision to produce together what no single function could produce alone. The result belongs to the team.',
         'In your last cross-functional review, did you present the shared outcome alongside your function’s contribution?'),
        ('Accountability', 'Owning results and reinforcing transparency', 'OAR', 'Own it · Act on it · Report it',
         'Accountability begins the moment a commitment is made. We report the truth and fix the gap.',
         'When did you last surface a gap before being asked, with the cause, the impact and the recovery action already identified?'),
        ('Excellence', 'Upholding rigour, learning and measurable impact', 'SET', 'Set the standard · Earn the evidence · Transform through learning',
         'Excellence is a daily discipline: being better than last quarter, and proving it with evidence.',
         'At your last review, could you answer: what standard did we set, what evidence do we have, and what have we changed as a result?'),
        ('Human-Centricity', 'Placing people at the core of leadership and execution', 'SEE', 'See the person behind the role · Enable growth deliberately · Ensure dignity in every interaction',
         'Leadership serves people. We invest in growth and protect dignity, and we never reduce a person to their output.',
         'In your last performance conversation, did you open with the person before moving to the result?')]
BAND = 'AIM · SAY · ONE · OAR · SET · SEE'
G47 = ['Teach the three steps with one IBSL value before showing the full Code: start with the behaviour; the acronym only packages it.',
       'Use the three tests on one IBSL norm so participants see how a norm holds under pressure. The groups build their own Code from their organisation’s values in part 5.8.']

def part47(fac):
    b = ['<p>%s</p>' % x for x in P47]
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator guidance</div>%s</div>' % ''.join('<p>%s</p>' % x for x in G47))
    b.append('<div class="u11-sub">%s</div><ol class="u11-ol">%s</ol>' % (STEPS_H, ''.join('<li><strong>%s.</strong> %s</li>' % s for s in STEPS)))
    b.append('<div class="u11-sub">%s</div><ul class="u11-ol">%s</ul>' % (EMBED_H, ''.join('<li>%s</li>' % s for s in EMBED)))
    b.append('<div class="u11-sub">%s</div><ul class="u11-ol">%s</ul>' % (TESTS_H, ''.join('<li><strong>%s:</strong> %s</li>' % s for s in TESTS)))
    cards = []
    for i, (v, d, acr, norm, body, refl) in enumerate(IBSL):
        inner = ('<p class="u11-coc-def">%s</p><div class="u11-coc-norm"><span class="u11-coc-acr">%s</span> %s</div><p>%s</p>' % (d, acr, norm, body)
                 + ('<p class="u11-note2"><strong>Prompt:</strong> %s</p>' % refl if fac else '<div class="p-reflect">Reflect: %s</div>' % refl))
        cards.append(det('%s &middot; %s' % (v, acr), inner, i == 0))
    tbl = ('<div class="u11-scroll"><table class="u11-tbl u11-tbln"><thead><tr><th>Value</th><th>Acronym</th><th>Norm</th></tr></thead><tbody>%s</tbody></table></div>'
           % ''.join('<tr><td>%s</td><td><strong>%s</strong></td><td>%s</td></tr>' % (v, acr, norm.replace(' · ', '. ') + '.') for v, d, acr, norm, body, refl in IBSL))
    b.append('<div class="u11-sub">%s</div><p>%s</p>%s%s<div class="hbox"><p class="u11-band">%s</p></div>' % (WE_H, WE_INTRO, ''.join(cards), tbl, BAND))
    return acc(T47, '\n'.join(b), False, 'Worked example: the IBSL Code')

T58 = '5.8 &mdash; Build Your Cultural Operating Code'
P58_P = ['Your Organisational Health Response sets out what must change. Your Cultural Operating Code defines the behaviours that carry the change: it translates your organisation’s values into norms your executive team models, recognises and corrects. Build it the way part 4.7 showed with the IBSL Code.']
P58_F = ['The group’s Organisational Health Response sets out what must change. The Cultural Operating Code defines the behaviours that carry the change: it translates the capstone organisation’s values into norms the executive team models, recognises and corrects. Groups build it the way part 4.7 showed with the IBSL Code.']
G58 = ['Each group builds the Code for its capstone organisation, using that organisation’s values. Where a group has not yet stated its organisation’s values, it agrees them first as the executive team.',
       'Guide the groups to begin each norm with the behaviour and to apply the three tests from part 4.7 to their strongest norm before they agree the record.']
S1_H = 'Step 1 · Your organisation’s values'
S1_P = 'List the values of your capstone organisation, three to six, each with what it means in one line. Where your organisation’s values are not yet stated, agree them now as its executive team.'
S1_F = 'The group lists the values of its capstone organisation, three to six, each with what it means in one line.'
S2_H = 'Step 2 · Translate the values into norms'
S2_P = 'Translate at least three of your values. For each: choose the value, describe the observable behaviour, build the acronym from three action words, write the three actions, and write the norm statement.'
S2_F = 'The group translates at least three of its values. For each: the value, the observable behaviour, the acronym from three action words, the three actions and the norm statement.'
S3_H = 'Step 3 · Test your strongest norm'
S3_P = 'Choose your strongest norm and record how it passes each of the three tests from part 4.7, or what your group changed so that it passes.'
S3_F = 'The group chooses its strongest norm and records how it passes each of the three tests from part 4.7, or what it changed so that it passes.'
NORM_F = [('beh', 'Observable behaviour'), ('acr', 'Acronym'), ('acts', 'The three actions'), ('stmt', 'Norm statement')]
TEST_F = [('newemp', 'The New Employee Test'), ('pressure', 'The Pressure Test'), ('mirror', 'The Mirror Test')]
OUT_COC = 'Your Cultural Operating Code forms part of the final capstone panel assessment (Capstone box 11E).'
OUT_COC_F = 'The group’s Cultural Operating Code forms part of the final capstone panel assessment (Capstone box 11E).'

def part58(fac):
    from u11_s4 import tbln
    b = ['<p>%s</p>' % x for x in (P58_F if fac else P58_P)]
    if fac:
        b.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; Facilitator guidance</div>%s</div>' % ''.join('<p>%s</p>' % x for x in G58))
        b += ['<h4 class="u11-h">%s</h4><p>%s</p>' % (S1_H, S1_F), tbln(['Value', 'What it means'], [['', '']] * 3),
              '<h4 class="u11-h">%s</h4><p>%s</p>' % (S2_H, S2_F), tbln(['Value'] + [l for k, l in NORM_F], [['', '', '', '', '']] * 3),
              '<h4 class="u11-h">%s</h4><p>%s</p>' % (S3_H, S3_F), tbln(['Test', 'How the strongest norm passes'], [[l, ''] for k, l in TEST_F]),
              '<div class="hbox"><p>%s</p></div>' % OUT_COC_F]
    else:
        b += ['<h4 class="u11-h">%s</h4><p>%s</p><div id="u11CocVals"></div>' % (S1_H, S1_P),
              '<h4 class="u11-h">%s</h4><p>%s</p><div id="u11CocNorms"></div><button type="button" class="ref-save u11-add" onclick="u11CocAdd()">+ Add a norm</button>' % (S2_H, S2_P),
              '<h4 class="u11-h">%s</h4><p>%s</p><div id="u11CocTest"></div>' % (S3_H, S3_P),
              '<div class="hbox"><p>%s</p></div>' % OUT_COC]
    return acc(T58, '\n'.join(b), False, 'Task 8')

def css(fac):
    c = 'var(--gold)' if fac else 'var(--teall)'
    return ('.u11-coc-def{font-style:italic;color:rgba(255,255,255,.6)!important;margin-bottom:6px!important;}\n'
            '.u11-coc-norm{font-size:14px;font-weight:600;color:rgba(255,255,255,.9);margin:6px 0 10px;line-height:1.6;}\n'
            '.u11-coc-acr{display:inline-block;font-weight:700;letter-spacing:3px;color:%s;border:1px solid %s;border-radius:2px;padding:1px 8px;margin-right:6px;}\n'
            '.u11-band{text-align:center;letter-spacing:3px;font-weight:700;color:%s!important;}\n'
            '.u11-cv{display:grid;grid-template-columns:minmax(140px,1fr) 2fr;gap:6px 10px;margin:6px 0;}\n'
            '@media (max-width:600px){.u11-cv{grid-template-columns:1fr;}}\n') % (c, c, c)
