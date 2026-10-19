# -*- coding: utf-8 -*-
"""Consistency review 19 Oct: rule fixes on the pages (findings A3, D1, D3, D4, D5, D6, D10, E3, E4).
Usage: python3 -B fixes_pages.py <portal folder> <out folder>. Each pair must match exactly n times."""
import sys, os, json
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True); LOG = []
F = {
'unit2_m1_lens1_f.html': [
 ("<p>These four points apply when the groups do the work on the portal, after the teaching.</p>", "<p>These four points guide how the groups complete the work on the portal, after the teaching.</p>", 1),
 ("<p><strong>4.2 &middot; Strategy Intent Statement. Watch for:</strong> a statement that carries every point from the Architecture. Say:", "<p><strong>4.2 &middot; Strategy Intent Statement.</strong> The group condenses the Architecture into one clear statement. Say:", 1),
 ("<p><strong>4.3 &middot; Success in Practice. Watch for:</strong> statements that list initiatives, projects or activities. Bring the group back to observable reality. Ask:", "<p><strong>4.3 &middot; Success in Practice.</strong> The group describes observable reality: what people see and experience when the strategy works. Ask:", 1),
 ("<p><strong>4.3 &middot; Balance. Watch for:</strong> one perspective defining success for the whole organisation. Use the SiP Flammables as the balance check.</p>", "<p><strong>4.3 &middot; Balance.</strong> The group gives each SiP domain its place in the picture of success and uses the SiP Flammables as the balance check.</p>", 1),
 ("<p><strong>5.1 &middot; Role contribution. Watch for:</strong> general statements such as &ldquo;Support the strategy&rdquo;. Ask:", "<p><strong>5.1 &middot; Role contribution.</strong> Each contribution names what the role does for the Success in Practice. Ask:", 1),
 ("<p>As groups share, listen for alignment, gaps, tensions and areas where the SiP statement may need clearer execution ownership.</p>", "<p>As groups share, participants note alignment, gaps, tensions and areas where the SiP statement needs clearer execution ownership.</p>", 1),
 ("<p>What to listen for as each group shares:</p>", "<p>What participants note as each group shares:</p>", 1),
],
'unit2_m1_lens2_p.html': [("<p>Integrator Zone · With your group", "<p>With your group", 1)],
'unit2_m1_lens2_f.html': [
 ("<p>Integrator Zone · The groups", "<p>The groups", 1),
 ("<p>As the team debates placements, listen for disagreements about what constitutes \"high impact\" versus \"high effort.\" These disagreements are where collective intelligence is built. Do not rush to consensus — the quality of the debate is as valuable as the final placement.</p>",
  "<p>The group discusses each placement until it agrees what counts as high impact and high effort for its strategy. These discussions are where collective intelligence is built, so the group takes the time it needs before it agrees each placement.</p>", 1),
 ("This single test is the most useful tool in the room.", "This single test is the most useful tool in the session.", 1),
 ("before it plays out in the room.", "before it plays out in the group's own work.", 1),
],
'unit2_m1_lens3_p.html': [("Where Does This Show Up in Your Role?", "Where Does Directional Integrity Break Down?", None)],
'unit2_m1_lens3_f.html': [
 ("<p><strong>Watch for:</strong> Must-Be-True conditions written as risks or concerns. Each must be a condition that is either true or false.</p>\n<p><strong>Watch for:</strong> competition defined as industry rivals only. Push for every alternative the customer can choose, including doing nothing.</p>",
  "<p><strong>Teach:</strong> a Must-Be-True condition is written so that it is either true or false. A risk or a concern becomes a condition once it is stated as what must hold.</p>\n<p><strong>Teach:</strong> competition covers every alternative the customer can choose, including doing nothing.</p>", 1),
 ("Vague conditions (&ldquo;the market must support us&rdquo;) are not sufficient. Push for precision.", "A general statement such as &ldquo;the market must support us&rdquo; becomes a condition once it names what must be true, for whom and by when.", 1),
 ("<p><strong>Watch for:</strong> Groups that struggle to name a condition. This is a signal that the Key Result itself may not be sufficiently grounded. Use it as productive friction: <em>&ldquo;If you cannot name a Must-Be-True, what does that tell you about this Key Result?&rdquo;</em></p>",
  "<p><strong>Where a group cannot name a condition:</strong> the Key Result itself may not be sufficiently grounded. The group asks itself: <em>&ldquo;If we cannot name a Must-Be-True, what does that tell us about this Key Result?&rdquo;</em></p>", 1),
 ("<p><strong>Watch for:</strong> conditions written as risks or concerns. Each must be a condition that is either true or false.</p>", "<p><strong>How each condition is written:</strong> as a statement that is either true or false. The group restates a risk or a concern as the condition that must hold.</p>", 1),
 ("Who is leaving this room responsible for that verification?", "Who is responsible for that verification?", 1),
],
'unit3_m1_lens4_p.html': [("you need to have with a closely adjacent role in the next 30 days?", "you need to have next with a closely adjacent role?", 1)],
'unit3_m1_lens4_f.html': [
 ("you need to have with that role in the next 30 days?", "you need to have next with that role?", 1),
 ("the most important alignment conversation with a closely adjacent role in the next 30 days.", "the most important alignment conversation they need to have next with a closely adjacent role.", 1),
 ("<p><strong>Watch for:</strong> a Shift written as a direction. Ask what stops, what starts, for whom and from when.</p>", "<p><strong>The Shift:</strong> the group states what stops, what starts, for whom and from when.</p>", 1),
 ("<p><strong>Watch for:</strong> a Stake that gives the gain only. Ask what the organisation loses if it stays as it is.</p>", "<p><strong>The Stake:</strong> the group states the gain and what the organisation loses if it stays as it is.</p>", 1),
 ("<p><strong>Watch for:</strong> a Step written for the organisation. Ask each member to say their own part in the first person.</p>", "<p><strong>The Step:</strong> each member states their own part in the first person.</p>", 1),
 ("<p><strong>Watch for:</strong> a value written where a behaviour is asked for, such as &ldquo;we will be accountable&rdquo;. Ask what a colleague would see the leadership team do.</p>", "<p><strong>Each behaviour:</strong> the group writes what a colleague would see the leadership team do. A value such as &ldquo;we will be accountable&rdquo; becomes a behaviour once it is stated that way.</p>", 1),
 ("<p><strong>Watch for:</strong> behaviours expected of staff. The five boxes are for the leadership team&rsquo;s own behaviour.</p>", "<p><strong>Whose behaviour:</strong> the five boxes hold the leadership team&rsquo;s own behaviour.</p>", 1),
],
'unit3_m1_lens6_p.html': [("What the individual wants to reach.", "What the leader aims to achieve in the conversation.", None)],
'unit3_m1_lens6_f.html': [("What the individual wants to reach.", "What the leader aims to achieve in the conversation.", None)],
'unit3_m2_lens8_p.html': [
 ('<div class="acc-t">Participant Activity &mdash; Collective Strategic Unclogging</div>', '<div class="acc-t">My Leadership Contribution to Strategic Unclogging</div>', 1),
 ("RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery.</p>", "RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery.</p>\n<p>Review–Realign–Restore is the cycle every performance review follows. Here the executive team applies it together to a clog that crosses executive portfolios.</p>", 1),
],
'unit3_m2_lens8_f.html': [
 ("FACILITATOR GUIDANCE &mdash; The Clog Clinic", "FACILITATOR GUIDANCE &mdash; The Strategic Unclogging Clinic", 1),
 ("RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery.</p>", "RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery.</p>\n<p>Review–Realign–Restore is the cycle every performance review follows. Here the executive team applies it together to a clog that crosses executive portfolios.</p>", 1),
],
}
for name, pairs in F.items():
    raw = open(os.path.join(src, name), 'rb').read(); crlf = b'\r\n' in raw
    t = raw.decode('utf-8').replace('\r\n', '\n')
    for a, b, n in pairs:
        c = t.count(a)
        assert (c == n) if n else c >= 1, (name, c, n, a[:90])
        t = t.replace(a, b); LOG.append(dict(file=name, count=c, before=a, after=b))
    open(os.path.join(out, name), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
json.dump(LOG, open(os.path.join(out, 'fixes_log.json'), 'w'), ensure_ascii=False, indent=1)
print('pages:', len(F), 'replacements:', len(LOG))
