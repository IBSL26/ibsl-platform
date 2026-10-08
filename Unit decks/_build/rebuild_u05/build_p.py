# -*- coding: utf-8 -*-
"""Unit 5 three-way match (October 2026) — participant file, on Carol's word of 8 October 2026 ("make the changes").
Usage: python3 build_p.py <participant file as it stood before the work> <new file>
Run it from this folder: it reads u5_content.py, u5.css and u5_p.js.
Every change is an exact replacement that must match the number of times given, or the build stops. Line endings (CRLF) and UTF-8 are kept.
No id, lens_id, link, lock logic or database call is changed. New: the saved key confirmed_items (Step 4 confirmation)."""
import sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5_content as C
src, out = sys.argv[1], sys.argv[2]
def read(name): return open(os.path.join(HERE, name), 'rb').read().decode('utf-8').replace('\r\n', '\n')
h = open(src, 'rb').read().decode('utf-8')
assert h.count('\r\n') == h.count('\n'), 'expected CRLF line endings'
h = h.replace('\r\n', '\n')
h0 = h

def rep(old, new, count=1):
    global h
    n = h.count(old)
    assert n == count, 'expected %d match(es), found %d: %s' % (count, n, old[:110])
    h = h.replace(old, new)
def how(title, steps, close=''):
    return ('<div class="u5-how"><div class="u5-how-h">' + title + '</div><ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>' +
            ('<p>' + close + '</p>' if close else '') + '</div>\n')

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + '\n:root{--u5:#22a08a;--u5-bg:rgba(26,122,106,.08);--u5-bd:rgba(26,122,106,.3);}' + read('u5.css') + h[i:]

# ── 1. Header ─────────────────────────────────────────────────────────────────────────────────────
rep('It equips leaders to lead people through the changes the strategy requires.</p>', 'It equips you to lead people through the changes the strategy requires.</p>')

# ── 2. Section 1 · the older cards take the fuller wording of the facilitator page (one shared text) ──
# 1.1
rep('Whether strategy produces clarity or confusion, commitment or compliance. <strong style="color:#fff;">Execution begins inside the human system.</strong>',
    'Whether strategy produces clarity or confusion, commitment or compliance, momentum or hesitation. <strong style="color:#fff;">Execution begins inside the human system.</strong>')
rep('The Functional Bias Problem reveals that when perspectives diverge, even highly capable executives can unintentionally pull the organisation in different directions.</p></div>',
    'The Functional Bias Problem reveals that organisations do not interpret strategy as a single, shared reality. When perspectives diverge, even highly capable executives can unintentionally pull the organisation in different directions.</p></div>')
# 1.2 · Principle 1
rep('        <p>Cognitive alignment focuses on making biases visible so they can be managed deliberately. Emotional alignment requires naming the current state through which strategy is being experienced. Leaders operating from Joy, Commitment, and Confidence invest very differently from those operating from Fear, Uncertainty, or Disengagement.</p>\n',
    '        <p>Cognitive alignment focuses on making biases visible so they can be managed deliberately. In practice: identify dominant decision biases at executive level, name how those biases shape the S2R&reg; process, establish shared decision principles that counter predictable distortions.</p>\n'
    '        <p>Emotional alignment requires naming the current emotional state through which strategy is being experienced. Leaders operate from a dominant state of being (Joy, Sadness, Anger, Fear, Disgust, Surprise). Each state influences engagement energy, morale drain, friction load, psychological safety, and values alignment.</p>\n')
# 1.2 · Principle 2
rep('        <p>When interpretation and emotional experience diverge, effort begins to <strong>fragment</strong>. The three most visible consequences: Chinese Whispers (intent mutates downward), Clarification Debt (leadership time consumed by re-explanation), Silent Disengagement (compliance without commitment).</p>\n'
    '        <div class="hbox red"><p><strong>Data:</strong> Low-alignment organisations experience 41% lower productivity and 48% higher turnover (Gallup; PMI). This drift is gradual, rationalised, and expensive.</p></div>\n',
    '        <p><strong>The cost of ignoring the human system.</strong> When interpretation and emotional experience are not aligned, effort begins to <strong>fragment</strong>. Everyone remains active, yet the organisation moves with split effort.</p>\n'
    '        <div class="tri-grid">\n'
    '          <div class="tri-card" style="border-top:2px solid #e74c3c;"><div style="font-size:9px;font-weight:700;text-transform:uppercase;color:#e74c3c;margin-bottom:6px;letter-spacing:1px;">Chinese Whispers</div><p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.6;margin:0;">Intent mutates as it travels downward. Frontline execution bears little resemblance to boardroom intent.</p></div>\n'
    '          <div class="tri-card" style="border-top:2px solid #e74c3c;"><div style="font-size:9px;font-weight:700;text-transform:uppercase;color:#e74c3c;margin-bottom:6px;letter-spacing:1px;">Clarification Debt</div><p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.6;margin:0;">60&ndash;80% of leadership time spent re-explaining, correcting, realigning. Leaders are patching.</p></div>\n'
    '          <div class="tri-card" style="border-top:2px solid #e74c3c;"><div style="font-size:9px;font-weight:700;text-transform:uppercase;color:#e74c3c;margin-bottom:6px;letter-spacing:1px;">Silent Disengagement</div><p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.6;margin:0;">People comply outwardly but withdraw inwardly. Looks like cooperation. Feels like exhaustion.</p></div>\n'
    '        </div>\n'
    '        <div class="hbox red" style="margin-top:12px;"><p><strong>Data:</strong> Low-alignment organisations experience 41% lower productivity and 48% higher turnover. This drift is dangerous because it is gradual, rationalised, and expensive (Gallup; PMI).</p></div>\n')
# 1.2 · Principle 3 (the two tools stay "available on demand", as the participant page already said)
rep('        <p>Alignment rarely emerges naturally. It must be intentionally designed. Two diagnostic assessments support this: the <strong>OCEAVL Assessment</strong> (surfaces psychological tendencies influencing decision-making) and the <strong>Emotional Climate Assessment</strong> (identifies the prevailing state of being through which strategy is currently being experienced). Both available on demand.</p>\n',
    '        <p><strong>Alignment rarely emerges naturally.</strong> It must be intentionally designed through structured interventions that make interpretation and emotional climate visible. Two diagnostic assessments support this design:</p>\n'
    '        <div class="u5-u3-grid" style="margin:12px 0;">\n'
    '          <div style="background:#121e1c;border-radius:3px;padding:14px;">\n'
    '            <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--teall);margin-bottom:8px;">OCEAVL Assessment</div>\n'
    '            <p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.65;margin:0;">Surfaces psychological tendencies influencing executive decision-making. Dimensions: Openness, Conscientiousness, Extraversion, Agreeableness, Emotional Stability, Values Alignment, Learning Orientation.</p>\n'
    '          </div>\n'
    '          <div style="background:#121e1c;border-radius:3px;padding:14px;">\n'
    '            <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--teall);margin-bottom:8px;">Emotional Climate Assessment</div>\n'
    '            <p style="font-size:12px;color:rgba(255,255,255,.6);line-height:1.65;margin:0;">Identifies the prevailing state of being across six core emotional categories: Joy, Sadness, Anger, Fear, Disgust, Surprise. Allows leaders to stabilise engagement before demanding execution.</p>\n'
    '          </div>\n'
    '        </div>\n'
    '        <p>Both available on demand.</p>\n')
# 1.2 · Principle 4
rep('        <p>Reactions to strategic change follow predictable psychological patterns. The SCARF Model explains five social conditions that trigger emotional responses during change.',
    '        <p><strong>Reactions to strategic change follow predictable psychological patterns.</strong> The SCARF Model (David Rock) explains five social conditions that trigger emotional responses during change.')
rep('is evaluated <em>emotionally</em> before it is evaluated rationally.</p>\n        <div class="p-insight">&#10148; Insight: When you can name',
    'is evaluated <em>emotionally</em> before it is evaluated rationally.</p>\n        <p>The five SCARF triggers are explored in detail in section 1.5.</p>\n        <div class="p-insight">&#10148; Insight: When you can name')
# 1.2 · Principle 5
rep('        <p>Without observable behaviour, alignment remains theoretical. The <strong>ACE-IT Framework</strong> defines five universally desired behaviours: Accountability, Commitment, Engagement, Integrity, Transparency &mdash; independent of an organisation&rsquo;s stated values. They represent the minimum behavioural standard for any leadership team serious about execution.</p>\n',
    '        <p><strong>Strategic alignment ultimately becomes visible through behaviour.</strong> Without observable behaviour, alignment remains theoretical. With behavioural standards, alignment becomes visible, measurable, and sustainable.</p>\n'
    '        <p>The <strong>ACE-IT Framework</strong> defines five universally desired behaviours: Accountability, Commitment, Engagement, Integrity, Transparency. These behaviours are <em>independent</em> of an organisation&rsquo;s stated values &mdash; they represent the minimum behavioural standard for any leadership team serious about execution. Explored in detail in section 1.7.</p>\n')
# 1.5
rep('  <p><strong>SCARF is the Heart check.</strong> When a trigger fires, a person who understands the change still withholds their energy from it.</p>\n  <div class="scarf-grid">',
    '  <p><strong>SCARF is the Heart check.</strong> When a trigger fires, a person who understands the change still withholds their energy from it.</p>\n'
    '  <p style="margin-bottom:14px;">Expand each trigger to explore what activates it, how it shows up in behaviour, its execution impact, and the counter-strategy that addresses it.</p>\n  <div class="scarf-grid">')
rep('Involve senior leaders in co-designing new structures.</div>', 'Involve senior leaders in co-designing new structures &mdash; status is protected when people have agency in the change.</div>')
rep('Create visible milestones early. Give the brain enough structure to move without removing all ambiguity.</div>', 'Create visible milestones early. The brain seeks pattern &mdash; give it enough structure to move without removing all ambiguity.</div>')
rep('Create visible connection rituals during transitions. People share resources only when they feel part of the tribe.</div>',
    'Create visible connection rituals during transitions. People need to feel part of the tribe before they will share resources or risk vulnerability.</div>')
rep('Uneven workload &bull; Selective enforcement &bull; Inconsistent rewards', 'Uneven workload &bull; Selective enforcement of rules &bull; Inconsistent rewards')
rep('&#10148; Counter: Explain rationale behind asymmetric decisions proactively. Transparency about trade-offs is perceived as fairness.</div>',
    '&#10148; Counter: Proactively explain rationale behind decisions &mdash; especially asymmetric ones. Transparency about trade-offs is perceived as fairness even when outcomes differ.</div>')
# 1.7
rep('Acting consistently with values, facts, and truth &mdash; even when inconvenient.</div></div>', 'Acting consistently with values, facts, and truth &mdash; even when inconvenient. Declaring conflicts of interest early.</div></div>')

# ── 3. Section 2 ──────────────────────────────────────────────────────────────────────────────────
rep('&mdash; movement, execution, and results &mdash; human action must occur.</p>', '&mdash; movement, execution, and results &mdash; human action must occur. No system executes itself.</p>')
rep('Aligning Hearts and Minds activates the human energy required to convert intention into action.</p></div>\n',
    'Aligning Heart &amp; Mind activates the human energy required to convert intention into action. This is the ignition point.</p></div>\n'
    '  <p>Without this ignition point, strategy remains defined but not delivered. With it, the organisation shifts from <strong>supervised effort to self-driven momentum</strong> &mdash; the strategic payoff that makes alignment the highest-leverage leadership intervention available.</p>\n')
rep('For it to become kinetic energy, a human decision must activate it. Every day that decision is not made is a day strategic potential sits unused. <strong style="color:#fff;">The organisation does not move until people decide to move it.</strong></p>',
    'For it to become kinetic energy (movement, execution, results), a human decision must activate it. The alignment of heart and mind is precisely the conversion mechanism. Every day that decision is not made is a day strategic potential sits unused. <strong style="color:#fff;">The organisation does not move until people decide to move it.</strong> Leadership cannot shortcut this decision &mdash; it can only create the conditions for it.</p>')
rep('People act because authority requires it. Produces visible output short-term. Requires continuous supervision. Creates hidden costs: leadership time consumed by follow-ups, decision-making slows as control increases.',
    'People act because authority requires it, rules enforce it, or systems monitor it. Produces visible output short-term. Requires continuous supervision. Creates hidden costs: leadership time consumed by follow-ups, teams dependent on instruction, decision-making slows as control increases.')
rep('People act because they understand intent, believe the direction is meaningful, and feel personal ownership. Generates <strong style="color:#5ecba1;">discretionary effort, adaptive problem-solving, resilience when conditions change.</strong> Execution continues when leaders are not present.</p>',
    'People act because they understand strategic intent, believe the direction is meaningful, and feel personal ownership. Generates behaviours compliance cannot sustain: <strong style="color:#5ecba1;">discretionary effort, adaptive problem-solving, resilience when conditions change.</strong> Execution continues even when leaders are not present.</p>')
rep('and leaders spend less time correcting and more time advancing strategy. <strong style="color:#fff;">Aligning Hearts and Minds is the mechanical conversion point where strategic potential becomes strategic movement.</strong></p>',
    'and leaders spend less time correcting and more time advancing strategy. This shift <strong style="color:#fff;">reduces rework, lowers escalation, and preserves leadership capacity</strong> for decisions that truly require executive attention. Aligning Heart &amp; Mind is the mechanical conversion point where strategic potential becomes strategic movement.</p>')
# The unit name reads "Aligning Heart & Mind" everywhere
rep('Aligning Hearts and Minds functions as the ignition point of execution', 'Aligning Heart &amp; Mind functions as the ignition point of execution')
assert 'Aligning Hearts' not in h

# ── 4. Section 3 · 3.1 ────────────────────────────────────────────────────────────────────────────
rep('  <p style="margin-bottom:14px;">Click each COMPASS domain to explore the signal narrative and the facilitation question that drives early intervention.</p>\n',
    '  <p class="u5-rate">Rate your organisation in each domain from 1 (strong alignment) to 5 (severe misalignment). Write your seven ratings in the reflection below.</p>\n'
    '  <p style="margin-bottom:14px;">Click each COMPASS domain to explore the signal narrative, how it appears when lit, and the reflection question that drives early intervention.</p>\n')
a = h.index('  <div id="cm0" class="cm-detail">'); b = h.index('  <div class="ref-block" style="margin-top:18px;"><div class="ref-label">&#x270E; Reflection &mdash; COMPASS Diagnostic</div>')
old = h[a:b]
assert old.count('class="cm-detail"') == 7 and old.count('Rate your organisation in this domain') == 7 and old.count('\n') == 7
h = h[:a] + ''.join(C.compass_detail(n, 'p') for n in range(7)) + h[b:]
assert 'Rate your organisation in this domain' not in h
rep('for="ref7">Which domain did you rate highest risk?', 'for="ref7">Write your seven ratings. Which domain did you rate highest risk?')

# ── 5. Section 4 ──────────────────────────────────────────────────────────────────────────────────
rep('  <p>The executive team enters the Converging Zone, where individual functional perspectives integrate into a shared leadership interpretation. The leadership team begins operating as a single leadership system, stabilising all seven COMPASS domains.</p>',
    '  <p>Your leadership team enters the Converging Zone, where individual functional perspectives integrate into a shared leadership interpretation. Your team begins operating as a single leadership system, stabilising all seven COMPASS domains.</p>')
rep('&#10003; One coherent signal across the organisation.</p>', '&#10003; One coherent signal across the organisation. COMPASS domains become leverage points for performance.</p>')
rep('&#9888; Multiple conflicting signals. Leverage zones become friction.</p>', '&#9888; Multiple conflicting signals. Leverage zones become sources of execution friction.</p>')
a = h.index('  <div id="rl0" class="rl-detail">'); b = h.index('  <div class="ref-block" style="margin-top:18px;"><div class="ref-label">&#x270E; Reflection</div>\n    <label class="wp-label" style="margin-top:0;" for="ref9">')
old = h[a:b]
assert old.count('class="rl-detail"') == 10 and old.count('\n') == 10
h = h[:a] + ''.join(C.role_detail(n, 'p') for n in range(10)) + h[b:]
rep('In the Converging Zone, the leadership team makes four commitments that no single function can make alone.', 'In the Converging Zone, your leadership team makes four commitments that no single function can make alone.')
rep('<div class="sc-rl">What The Team Does</div>', '<div class="sc-rl">What Your Team Does</div>', 4)

# ── 6. Participant voice in the change management parts (Appendix D of the findings) ─────────────────
VOICE = [
    ('A leadership team debates a change for months before announcing it. Leaders finish their own transition on the day everyone else begins theirs.',
     'Your leadership team debates a change for months before announcing it. You finish your own transition on the day everyone else begins theirs.', 1),
    ('An announcement shows that the leader has spoken.', 'An announcement shows that you have spoken.', 1),
    ('Passed when: the practice holds when the leader is absent.</div>', 'Passed when: the practice holds when you are absent.</div>', 1),
    ('that check is where the leader&rsquo;s effort belongs.', 'that check is where your effort belongs.', 1),
    ('<h4>The leader&rsquo;s four jobs</h4>', '<h4>Your four jobs as leader</h4>', 1),
    ('<th>Leader&rsquo;s job</th>', '<th>Your job</th>', 1),
    ('The practice holds through a full review period with the leader absent.</td>', 'The practice holds through a full review period with you absent.</td>', 1),
    ('the practice holds through a full review period with the leader absent.</p>', 'the practice holds through a full review period with you absent.</p>', 1),
    ('have understood the change as the leader intended it.', 'have understood the change as you intended it.', 1),
    ('<p>Leaders are poorly placed to judge this for themselves. After months inside a change, its logic feels obvious to them, and an obvious message feels like a clear one.',
     '<p>You are poorly placed to judge this for yourself. After months inside a change, its logic feels obvious to you, and an obvious message feels like a clear one.', 1),
    ('&#10148; Leader&rsquo;s move:', '&#10148; Your move:', 7),
    ('<div class="chg-job-label">The leader&rsquo;s job at this check &middot;', '<div class="chg-job-label">Your job at this check &middot;', 4),
    ('Repetition feels excessive to the leader long before the message has landed.', 'Repetition feels excessive to you long before the message has landed.', 1),
    ('The leader decides what changes and opens up how it is done.', 'You decide what changes and open up how it is done.', 1),
    ('<li>Use of the new practice falls when the leader is absent.</li>', '<li>Use of the new practice falls when you are absent.</li>', 1),
    ('<td>The practice holds when the leader is absent.</td>', '<td>The practice holds when you are absent.</td>', 1),
]
for a_, b_, n in VOICE:
    assert h.count(a_) == n, ('participant voice', h.count(a_), a_[:70])
    h = h.replace(a_, b_)

# ── 7. Section 5 · Portfolio work (Steps 1 to 3) and Capstone work (Step 4) ─────────────────────────
rep('  <p>This exercise highlights how Collective Intelligence emerges when leaders understand each other&rsquo;s alignment responsibilities. The goal: move from individual interpretations to a shared understanding of how roles jointly stabilise all seven COMPASS domains. The exercise starts from two real changes your strategy requires.</p>',
    '  <p>This exercise highlights how Collective Intelligence emerges when you and your colleagues understand each other&rsquo;s alignment responsibilities. The goal: move from individual interpretations to a shared understanding of how roles jointly stabilise all seven COMPASS domains. The exercise starts from two real changes your strategy requires. Steps 1 to 3 are Portfolio work. Step 4 is Capstone work: your group&rsquo;s confirmed outputs feed your team&rsquo;s Capstone Blueprint.</p>')
# Step 1: the how-to box, the Unit 3 lists; the Team & Executive Identity block leaves (as in Unit 4; saved answers stay in the database)
a = h.index('<p>Work independently. Choose two changes your strategy requires of people:'); b = h.index('<div class="chg-h">Worked example</div>')
old = h[a:b]
assert old.count('id="team_name"') == 1 and old.count('id="exec_name"') == 1 and old.count('id="exec_role"') == 1 and old.count('<textarea') == 0 and old.count('<div') == old.count('</div>')
step1 = ('<p>Work independently. The map turns the 4 Checks into a plan for one change: who it affects, where it will stall, what they need and who answers for it.</p>\n' +
         how('Portfolio work &middot; How to complete the Change Transition Map', [
             'Choose two changes your strategy requires of people: one practice they must start and one they must stop. Take them from the Start and Stop lists your group confirmed in Unit 3.',
             'Read the worked example.',
             'Complete the eight fields for Change 1, then for Change 2.',
             'Check each map against &ldquo;A complete map&rdquo;.'],
             'Your maps become part of your Learning Portfolio. ' + C.SUBMIT_P) +
         '<div class="u5-u3">\n<div class="chg-h" style="margin-top:6px;">From Unit 3 &middot; your group&rsquo;s confirmed Start and Stop lists</div>\n<div id="u5KissP"></div>\n'
         '<div class="u5-btnrow"><button type="button" class="u5-b" onclick="u5Bring(true)">Bring in from my Unit 3 page</button></div>\n'
         '<div class="u5-note" id="u5BringMsg" style="display:none;"></div>\n</div>\n\n')
h = h[:a] + step1 + h[b:]
for gone in ('id="team_name"', 'id="exec_name"', 'id="exec_role"', 'Team &amp; Executive Identity', 'KISS table'):
    assert gone not in h, gone
# Step 2
rep('<p>Work independently. For the two changes you mapped, complete the table for your own role and for the two roles you depend on most. Focus on the alignment mechanism.</p>\n',
    '<p>Work independently. For the two changes you mapped, complete the table for your own role and for the two roles you depend on most. Focus on the alignment mechanism.</p>\n' +
    how('Portfolio work &middot; How to complete Role Connections', [
        'Row 1: name your own role, the two COMPASS domains it most directly activates, and how you create Collective Intelligence.',
        'Row 2: name the first role you depend on, its two COMPASS domains, and why its alignment is critical to yours.',
        'Row 3: name the second role you depend on, its two COMPASS domains, and what would strengthen your alignment.'],
        'Your table becomes part of your Learning Portfolio. It reaches your facilitator when you select Submit to Facilitator at the end of the unit.'))
# Step 3
rep('<p>Share your map and your table with the colleague(s) whose role you selected. Four exchange questions to explore together:</p>\n',
    how('Portfolio work &middot; How to complete Exchange &amp; Dialogue', [
        'Share your map and your table with the colleague(s) whose role you selected.',
        'Work through the four exchange questions together.',
        'Type your own notes under each question.'],
        'Your notes become part of your Learning Portfolio. ' + C.SUBMIT_P))
# Step 4: group-work rule, how-to box, the three group entries, the record with Confirm and Print, then the personal commitment
rep('<div class="step-panel" id="sp2">\n<div style="margin:16px 0;">\n',
    '<div class="step-panel" id="sp2">\n<div class="u5-group"><strong>Working as a group.</strong> ' + C.GROUP_RULE_P + '</div>\n' +
    how('Capstone work &middot; How to complete', [
        'Agree the COMPASS domain, or domains, that appeared most often as missing or poorly understood across your tables.',
        'Agree where alignment is already strong.',
        'Agree which group appears on the most maps, and the order and pace for the changes landing on it.',
        'Read your record, then select Confirm. Select Print for a copy.']) +
    '<div style="margin:16px 0;">\n')
rep('  <div class="ref-saved reflection-saved" id="syn_sequence-saved"></div>\n  <label class="wp-label" for="syn_30day">Your 30-Day Behavioural Commitment</label>\n',
    '  <div class="ref-saved reflection-saved" id="syn_sequence-saved"></div>\n  <button class="wp-save" onclick="saveTA(this)">Save Synthesis</button>\n</div>\n'
    '<div id="synOutP"></div>\n'
    '<div class="u5-how"><div class="u5-how-h">Portfolio work &middot; Your 30-Day Behavioural Commitment</div>'
    '<p>Your 30-Day Behavioural Commitment is your own. It is Portfolio work and reaches your facilitator when you select Submit to Facilitator at the end of the unit.</p></div>\n'
    '<div style="margin:16px 0;">\n  <label class="wp-label" style="margin-top:0;" for="syn_30day">Your 30-Day Behavioural Commitment</label>\n')
rep('  <div class="ref-saved reflection-saved" id="syn_30day-saved"></div>\n  <button class="wp-save" onclick="saveTA(this)">Save Synthesis</button>\n',
    '  <div class="ref-saved reflection-saved" id="syn_30day-saved"></div>\n  <button class="wp-save" onclick="saveTA(this)">Save Commitment</button>\n')
rep('<strong>Unit Outcome:</strong> The organisation leaves this session with aligned leadership interpretation, emotional commitment to the strategy, clear visibility of the conditions that will enable or constrain execution, and a transition mapped for two of the changes the strategy requires &mdash;',
    '<strong>Unit Outcome:</strong> You leave this unit with an aligned leadership interpretation, emotional commitment to the strategy, clear visibility of the conditions that will enable or constrain execution, and a transition mapped for two of the changes your strategy requires &mdash;')

# ── 8. Script ─────────────────────────────────────────────────────────────────────────────────────
m = re.search(r'var SUMMARY=\[.*?\n\];\n', h, re.S); assert m and m.group(0).count('{arc:') == 4
h = h[:m.start()] + 'var SUMMARY=' + json.dumps(C.SUMMARY_P, ensure_ascii=False) + ';\n' + h[m.end():]
rep('var KEYS=["team_name","exec_name","exec_role","ref1",', 'var KEYS=["ref1",')
rep('    KEYS.forEach(function(id){var ta=document.getElementById(id);if(ta&&responses[id]!=null)ta.value=responses[id];});\n    loadSubmissionFeedback();\n',
    '    KEYS.forEach(function(id){var ta=document.getElementById(id);if(ta&&responses[id]!=null)ta.value=responses[id];});\n    u5Init(responses);\n    loadSubmissionFeedback();\n')
rep('/* ── Init ── */\nrenderSummaryP();', read('u5_p.js').strip('\n') + '\n\n/* ── Init ── */\nrenderSummaryP();')

# ── 9. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<script') == h.count('</script>') == h0.count('<script')
assert h.count('<div') == h.count('</div>') + h.count('<\\/div>'), 'div balance %d / %d' % (h.count('<div'), h.count('</div>'))
ids0 = set(re.findall(r'\bid="([^"]+)"', h0)); ids1 = set(re.findall(r'\bid="([^"]+)"', h))
lost = ids0 - ids1
assert lost == {'team_name', 'team_name-saved', 'exec_name', 'exec_name-saved', 'exec_role', 'exec_role-saved'}, lost
assert (ids1 - ids0) == {'u5KissP', 'u5BringMsg', 'synOutP', 'synMsg'}, ids1 - ids0   # synMsg is drawn by u5_p.js
for k in ('lens_id', 'u3m1_lens4', 'href=', 'showMod(', 'showSP('):
    extra = 1 if k == 'u3m1_lens4' else 0     # u5_p.js names the unit once, in U5_LENS
    assert h.count(k) == h0.count(k) + extra, (k, h0.count(k), h.count(k))
vis = re.sub(r'<script.*?</script>', ' ', re.sub(r'<style.*?</style>', ' ', h, flags=re.S), flags=re.S)
for bad in (r'\blens(es)?\b', r'Save to Portfolio', r'pre-?work', r'automat', r'\b\d+\s*(–|-|&ndash;)?\s*\d*\s*minutes\b', r'facilitation question', r'\bAsk:', r'\bSay:'):
    assert not re.search(bad, re.sub(r'<[^>]+>', ' ', vis), re.I), 'found on the page: ' + bad
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('participant file written:', out, len(h))
