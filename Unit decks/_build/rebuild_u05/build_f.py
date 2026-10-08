# -*- coding: utf-8 -*-
"""Unit 5 three-way match (October 2026) — facilitator file, on Carol's word of 8 October 2026 ("make the changes").
Usage: python3 build_f.py <facilitator file as it stood before the work> <new file>
Run it from this folder: it reads u5_content.py and u5.css.
Every change is an exact replacement that must match the number of times given, or the build stops. Line endings (CRLF) and UTF-8 are kept.
The page stays preparation-only: the build fails if a time, an entry box or a save button is left."""
import sys, os, re
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
def activity(lead, steps=None, close=''):
    return ('  <div class="fac-note-full u5-activity"><div class="fac-note-full-label">&#9670; PARTICIPANT ACTIVITY</div>\n    <p>' + lead + '</p>\n' +
            ('    <ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>\n' if steps else '') +
            ('    <p>' + close + '</p>\n' if close else '') + '  </div>\n')

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + '\n:root{--u5:#c9a84c;--u5-bg:rgba(201,168,76,.07);--u5-bd:rgba(201,168,76,.28);}' + read('u5.css') + h[i:]

# ── 1. No times anywhere ──────────────────────────────────────────────────────────────────────────
h, n = re.subn(r' <em>Suggested (?:section )?time: \d+&ndash;\d+ minutes\.</em>', '', h); assert n == 20, n
rep('<p><strong>Timing:</strong> Step 1 is individual &mdash; 15 minutes. Step 2 is individual &mdash; 12&ndash;15 minutes. Step 3 is paired exchange &mdash; 15&ndash;20 minutes. Step 4 is plenary synthesis &mdash; 20&ndash;25 minutes. Do not rush Steps 1&ndash;3.',
    '<p><strong>Order:</strong> Steps 1 and 2 are individual. Step 3 is a paired exchange. Step 4 is the plenary synthesis. Do not rush Steps 1&ndash;3.')
rep('Each person works independently and completes the map once for each change. Allow 15 minutes. Leaders use the change', 'Each person works independently and completes the map once for each change. Leaders use the change')
rep('Reserve the final five minutes for one pointed question:', 'Close with one pointed question:')
rep('<p><strong>On one message:</strong> If time allows, repeat the 3S test from 1.4 with the whole team on one enterprise-wide change. Post the versions side by side.</p>',
    '<p><strong>On one message:</strong> Repeat the 3S test from 1.4 with the whole team on one enterprise-wide change. Participants post their versions in the chat.</p>')

# ── 2. Guidance: build notes out; teaching first (the facilitator teaches, participants go to their page afterwards); online delivery ──
rep('<p><strong>Pacing:</strong> Open each principle card and read the insight aloud before inviting reflection. Do not let the group race through.',
    '<p><strong>Pacing:</strong> Teach one principle at a time and give its insight before inviting reflection. Do not let the group race through.')
rep('for the same change, without conferring, and read them aloud.', 'for the same change, without conferring, and post them in the chat.')
rep('<p><strong>Framing:</strong> Open by naming SCARF as the Heart check. The trigger cards are taught as they are today.</p>', '<p><strong>Framing:</strong> Open by naming SCARF as the Heart check.</p>')
rep('<p><strong>On pacing:</strong> Open each SCARF card and read the trigger question aloud. Then pause:', '<p><strong>On pacing:</strong> Give each trigger with its question. Then pause:')
rep('<p><strong>Framing:</strong> Open by naming ACE-IT as the Habit check. The behaviour cards are taught as they are today.</p>', '<p><strong>Framing:</strong> Open by naming ACE-IT as the Habit check.</p>')
rep('<p><strong>Diagnostic exercise:</strong> Before revealing the COMPASS narratives, ask participants to independently rate their organisation on each domain (1 = strong alignment, 5 = severe misalignment). Then compare ratings across the leadership team. Divergent ratings are themselves diagnostic.</p>',
    '<p><strong>Diagnostic exercise:</strong> Before teaching the COMPASS narratives, ask participants to rate their organisation on each domain on their own (1 = strong alignment, 5 = severe misalignment) and post the seven ratings in the chat. Then compare the ratings across the group. Divergent ratings are themselves diagnostic.</p>')
rep('<p><strong>On the COMPASS cards:</strong> Invite leaders to click the domain they rated highest risk first. Then ask the group:',
    '<p><strong>On the COMPASS domains:</strong> Start with the domain most participants rated highest risk. Then ask the group:')
rep('Divergence in the room is itself a signal &mdash; name it explicitly.', 'Divergence in the group is itself a signal &mdash; name it explicitly.')
rep('&ldquo;Can every person in this room describe the top three strategic priorities', '&ldquo;Can every person in this group describe the top three strategic priorities')
rep('<p><strong>Process:</strong> Leaders rate their own change individually and in silence, using the rating guide. Then pair leaders who share an affected group and compare their ratings.</p>',
    '<p><strong>Process:</strong> Participants rate their own change on their own, using the rating guide. Then pair participants who share an affected group to compare their ratings.</p>')
rep('<p><strong>On the role grid:</strong> Ask each leader to click their own role card first. Then:', '<p><strong>On the role grid:</strong> Ask each participant to find their own role first. Then:')
rep('Then invite leaders to look at each other&rsquo;s cards. This is particularly powerful when the full CXO team is in the room.',
    'Then ask them to read the roles closest to their own. This is particularly powerful when the full CXO team attends.')
rep('<p><strong>Change load count:</strong> Choose one named group and list on one sheet every change the leadership team is asking of it this quarter.',
    '<p><strong>Change load count:</strong> Choose one named group and list in the chat every change the leadership team is asking of it this quarter.')
rep('Return the room to the group that has to absorb them.', 'Return the discussion to the group that has to absorb them.')
rep('The &ldquo;How We Create Collective Intelligence&rdquo; column', 'The &ldquo;How I Create Collective Intelligence&rdquo; column')
rep('&ldquo;Looking at all the tables in the room &mdash; which COMPASS domain', '&ldquo;Looking across all the tables &mdash; which COMPASS domain')
rep('Make these visible &mdash; write them on the board or capture them centrally.', 'Make these visible: each participant posts the commitment in the chat.')
rep('Available on demand &mdash; excel or HTML format', 'Available on demand &mdash; Excel or HTML format')

# ── 3. The unit name reads "Aligning Heart & Mind" everywhere ─────────────────────────────────────────
rep('Aligning Hearts and Minds', 'Aligning Heart &amp; Mind', 3)
rep('Aligning Hearts &amp; Minds treated execution', 'Aligning Heart &amp; Mind treated execution')
assert 'Aligning Hearts' not in h

# ── 4. PARTICIPANT ACTIVITY notes for the fifteen reflections, at the foot of each part ────────────────
def close_of(start):
    """Index of the </div> that closes the <div ...> opening at `start`."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', h[start:]):
        depth += 1 if m.group(0) != '</div>' else -1
        if depth == 0: return start + m.start()
    raise AssertionError('no close')
for part, text in C.REFLECTION_NOTES:
    t = '<span class="acc-t">%s &mdash; ' % part
    assert h.count(t) == 1, part
    a = h.index('<div class="acc-b cb">', h.index(t)); b = close_of(a)
    assert h[b - 1] == '\n'
    h = h[:b] + activity('Participants write a reflection in their own file: ' + text) + h[b:]
assert h.count('PARTICIPANT ACTIVITY') == 15

# ── 5. Section 5 · Portfolio work (Steps 1 to 3) and Capstone work (Step 4) ─────────────────────────
rep('The exercise starts from two real changes your strategy requires.</p>\n</div>\n<div class="mod-body">\n<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>Formulate',
    'The exercise starts from two real changes your strategy requires. Steps 1 to 3 are Portfolio work. Step 4 is Capstone work: the group&rsquo;s confirmed outputs feed each team&rsquo;s Capstone Blueprint.</p>\n</div>\n<div class="mod-body">\n<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul><li>Formulate')
rep('<p>Work independently. Choose two changes your strategy requires of people: one practice they must start and one they must stop. Draw them from your KISS table where you have one. Run the 4 Checks and complete the map once for each change.</p>\n', '')
rep('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div><p>Participants complete the Change Transition Map in their own file, once for each change. Circulate and check that each map names a specific group, a specific practice and one person as owner.</p></div>\n',
    activity('After the lesson, each participant completes the Change Transition Map alone in Step 1 of their own file, as portfolio work:', [
        'They choose two changes the strategy requires of people: one practice people must start and one they must stop, taken from the Start and Stop lists the group confirmed in Unit 3. Their page shows the two lists.',
        'They read the worked example.',
        'They complete the eight fields for each change: the change, who is most affected, Mind &middot; 3S, Heart &middot; SCARF, Hands &middot; STAT, Habit &middot; ACE-IT, the weakest check and the leader who owns it.'],
        'The maps become part of the participant&rsquo;s Learning Portfolio. They reach you when the participant selects Submit to Facilitator at the end of the unit. Check that each map names a specific group, a specific practice and one person as owner.'))
rep('<p>Work independently. For the two changes you mapped, complete the table for your own role and for the two roles you depend on most. Focus on the alignment mechanism.</p>\n', '')
rep('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div><p>Participants complete the table for their own role and the two roles they depend on most. Circulate and check that each row names a specific COMPASS domain and a concrete collaboration behaviour.</p></div>\n',
    activity('Each participant completes the table alone in Step 2 of their own file, as portfolio work: their own role first, then the two roles they depend on most. Each row names the role, the two COMPASS domains it most directly activates and one statement on alignment.',
             None, 'The table becomes part of the participant&rsquo;s Learning Portfolio. Check that each row names a specific COMPASS domain and a concrete collaboration behaviour.'))
rep('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div><p>Pair participants from closely related roles. Allow five minutes per person, then ask each pair where their interpretations diverged. Treat divergence as diagnostic and leave it unresolved.</p></div>\n',
    activity('Participants work in pairs from closely related roles, as portfolio work. Each shares the map and the table, the pair works through the four exchange questions, and each participant types their own notes in their own file.',
             None, 'Then ask each pair where their interpretations diverged. Treat divergence as diagnostic and leave it unresolved.'))
rep('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE</div><p>Facilitate the group synthesis: the most underactivated COMPASS domain, shared strengths, connectivity gaps and the sequence for changes landing on the same group. Close by asking each participant to read one 30-day behavioural commitment aloud.</p></div>\n',
    activity('Participants work as a group, in Step 4 of their own file. This is Capstone work. ' + C.GROUP_RULE_F, [
        'The group agrees the COMPASS domain, or domains, most often underactivated.',
        'The group agrees where alignment is already strong.',
        'The group agrees which group of people appears on the most maps, and the order and pace for the changes landing on it.',
        'Each participant reads the record and selects Confirm. Print gives a copy of the record.'],
        'The confirmed work feeds the team&rsquo;s Capstone Blueprint. Each participant then writes one 30-day behavioural commitment in their own file, as portfolio work. Close by asking each participant to post that commitment in the chat.'))
assert h.count('PARTICIPANT ACTIVITY') == 19 and '&#9670; FACILITATOR GUIDANCE</div><p>' not in h

# ── 6. Unit Summary: block 4 named for its section; a block for Section 5 ────────────────────────────
rep('4 &mdash; Converging Zone: Collective Intelligence</div>', '4 &mdash; Integration: Collective Intelligence in the Converging Zone</div>')
rep('<!-- Change management -->\n',
    '<!-- Stage 5 -->\n<div style="border-left:3px solid #7fd1c4;padding:16px 20px;background:rgba(127,209,196,.06);border-radius:0 4px 4px 0;margin-bottom:14px;">\n'
    '  <div style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#7fd1c4;margin-bottom:8px;">5 &mdash; Application: Mapping the Transition</div>\n'
    '  <p>Each participant mapped the transition for two changes the strategy requires, set out how their role connects to the two roles they depend on most, and tested both with a colleague. '
    'The group then agreed the COMPASS domain most often underactivated, where alignment is already strong, and the sequence for the changes landing on the same group. '
    'The confirmed work feeds each team&rsquo;s Capstone Blueprint.</p>\n</div>\n\n<!-- Change management -->\n')

# ── 7. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<script') == h.count('</script>') == h0.count('<script')
assert h.count('<div') == h.count('</div>') + h.count('<\\/div>'), 'div balance %d / %d' % (h.count('<div'), h.count('</div>'))
assert set(re.findall(r'\bid="([^"]+)"', h0)) == set(re.findall(r'\bid="([^"]+)"', h))
for k in ('lens_id', 'u3m1_lens4', 'href=', 'showMod(', 'showSP(', 'onclick='):
    assert h.count(k) == h0.count(k), (k, h0.count(k), h.count(k))
assert all(C.compass_detail(n, 'f').replace('in this room', 'in this group') in h for n in range(7)) and all(C.role_detail(n, 'f') in h for n in range(10))
vis = re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>', ' ', re.sub(r'<style.*?</style>', ' ', h, flags=re.S), flags=re.S))
for bad in (r'\blens(es)?\b', r'\b\d+\s*(–|-|&ndash;)?\s*\d*\s*(minutes|mins?)\b', r'[Ss]uggested (section )?time', r'five minutes', r'time allows', r'as they are today', r'in th(e|is) room',
            r'on the board', r'whiteboard', r'flip chart', r'one sheet', r'[Cc]irculate', r'aloud', r'in silence', r'pre-?work', r'automat', r'KISS table', r'Save to Portfolio'):
    assert not re.search(bad, vis), 'found on the page: ' + bad
for tag in ('<textarea', '<input', '<select', 'onclick="saveTA(', 'S2R.save'):   # an unused saveTA function sits in the page script as it did before; no button calls it
    assert tag not in h, 'the facilitator page is preparation-only: ' + tag
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('facilitator file written:', out, len(h))
