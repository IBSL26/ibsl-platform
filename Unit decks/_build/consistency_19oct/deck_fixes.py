# -*- coding: utf-8 -*-
"""Consistency review 19 Oct: deck fixes on Carol's decks (findings D1, D2, D5, D6, D7, D8, E1, E2, E3, E4, G1, G2).
Usage: python3 deck_fixes.py <decks in> <decks out> <pics folder> <pages folder>"""
import sys, os, re, glob, copy, html, io
from pptx import Presentation
from pptx.util import Pt, Emu
from PIL import Image
IN, OUT, PICS, PAGES = sys.argv[1:5]; os.makedirs(OUT, exist_ok=True); LOG = []
def deck(u): return glob.glob(os.path.join(IN, f'Unit {u:02d}*.pptx'))[0]
def ptext(p): return ''.join(r.text for r in p.runs)
def set_ptext(p, t):
    rs = p.runs
    rs[0].text = t
    for r in rs[1:]: r._r.getparent().remove(r._r)
def paras(s, notes=True, slide=True):
    out = []
    if slide:
        for sh in s.shapes:
            if sh.has_text_frame: out += list(sh.text_frame.paragraphs)
    if notes and s.has_notes_slide: out += list(s.notes_slide.notes_text_frame.paragraphs)
    return out
def rep(prs, u, i, old, new, where='N', whole=False, n=1):
    """Replace text in paragraphs of slide i (1-based). whole=True: the paragraph equals old exactly. new=None deletes it."""
    s = prs.slides[i - 1]; c = 0
    for p in paras(s, notes='N' in where, slide='S' in where):
        t = ptext(p)
        if (t == old) if whole else (old in t):
            c += 1
            if new is None: p._p.getparent().remove(p._p)
            else:
                rr = [r for r in p.runs if old in r.text]
                if rr and not whole: rr[0].text = rr[0].text.replace(old, new)
                else: set_ptext(p, t.replace(old, new) if not whole else new)
            LOG.append((u, i, where, t, None if new is None else (new if whole else t.replace(old, new))))
    assert c == n, (u, i, old[:60], c)

# ---------- Unit 2: online wording, slide titles ----------
p = Presentation(deck(2))
rep(p, 2, 6, '5. Leave one question in the room.', '5. Leave one question with the group.', whole=True)
rep(p, 2, 12, '3. Leave one question in the room.', '3. Leave one question with the group.', whole=True)
rep(p, 2, 8, 'say what the pattern in the room is.', 'say what pattern the group shows.')
rep(p, 2, 16, 'say what the pattern in the room is.', 'say what pattern the group shows.')
rep(p, 2, 7, '1.1· Building', '1.1 · Building', 'S')
rep(p, 2, 9, 'Defining the Success In Practice', 'Defining the Success in Practice', 'S')
rep(p, 2, 31, '4.3 Step 3', '4.3 · Step 3', 'S')
rep(p, 2, 34, '5.1 Role Contribution', '5.1 · Role Contribution', 'S')
p.save(os.path.join(OUT, os.path.basename(deck(2))))

# ---------- Unit 3: group work, contrast, online wording, slide text size ----------
p = Presentation(deck(3))
rep(p, 3, 33, 'as the team debates placements, listen for disagreements about what constitutes high impact and high effort. These disagreements are where collective intelligence is built. Hold back from a quick consensus: the quality of the debate is as valuable as',
    'the group discusses each placement until it agrees what counts as high impact and high effort for its strategy. These discussions are where collective intelligence is built, so the group takes the time it needs: the quality of the discussion is as valuable as')
rep(p, 3, 6, 'initiatives that do not yet exist but will be necessary', 'initiatives the organisation will need')
rep(p, 3, 10, 'We are testing its strategic impact against the effort required, not simply whether it is a good idea.', 'We are testing its strategic impact against the effort it requires.')
rep(p, 3, 8, 'the most useful tool in the room.', 'the most useful tool in the session.')
rep(p, 3, 13, 'say what the pattern in the room is.', 'say what pattern the group shows.')
rep(p, 3, 23, 'before it plays out in the room."', 'before it plays out in the group’s own work."')
rep(p, 3, 28, '3. Start the thinking in the room.', '3. Start the thinking with the group.', whole=True)
p.save(os.path.join(OUT, os.path.basename(deck(3))))

# ---------- Unit 4: facilitator guide and Working Papers notes, slide titles ----------
p = Presentation(deck(4))
rep(p, 4, 3, '- Watch for Must-Be-True conditions written as risks or concerns. Each must be a condition that is either true or false.', '- Teach: a Must-Be-True condition is written so that it is either true or false. A risk or a concern becomes a condition once it is stated as what must hold.', whole=True)
rep(p, 4, 3, '- Watch for competition defined as industry rivals only. Push for every alternative the customer can choose, including doing nothing.', '- Teach: competition covers every alternative the customer can choose, including doing nothing.', whole=True)
rep(p, 4, 28, '“The market must support us” is too vague to verify.', '“The market must support us” becomes a condition once it names what must be true, for whom and by when.', whole=True)
rep(p, 4, 28, 'Push for precision."', '"', whole=True)
rep(p, 4, 28, 'Watch for: conditions written as risks or concerns. Each must be a condition that is either true or false.', 'How each condition is written: as a statement that is either true or false. The group restates a risk or a concern as the condition that must hold.', whole=True)
rep(p, 4, 28, 'Watch for: groups that struggle to name a condition. This is a signal that the Key Result itself may be insufficiently grounded. Use it as productive friction.', 'Where a group cannot name a condition: the Key Result itself may be insufficiently grounded. The group asks itself what that tells it about the Key Result.', whole=True)
rep(p, 4, 28, 'Who is leaving this room responsible for that verification?', 'Who is responsible for that verification?')
for i, a in ((7, '1.1 Arena'), (8, '1.2 Boundaries'), (9, '1.3 Competition'), (10, '1.4 Value Proposition')):
    rep(p, 4, i, a, a.replace(' ', ' · ', 1), 'S')
p.save(os.path.join(OUT, os.path.basename(deck(4))))

# ---------- Unit 5: no time, contrast ----------
p = Presentation(deck(5))
for i in (30, 31):
    rep(p, 5, i, 'you need to have with a closely adjacent role in the next 30 days?', 'you need to have next with a closely adjacent role?')
rep(p, 5, 26, 'We use it here as a strategy execution tool, not as a personality label.', 'We use it here as a strategy execution tool.')
rep(p, 5, 26, 'read it as a map, not as a judgement.', 'read it as a map of how the team tends to respond.')
rep(p, 5, 26, 'the team starts managing emotions instead of managing the strategy.', 'the team spends its energy managing emotions, and the strategy waits.')
rep(p, 5, 26, 'When they do not match, people may comply but commitment weakens.', 'When they do not match, people comply and commitment weakens.')
rep(p, 5, 26, 'That is how alignment becomes designed, not assumed.', 'That is how alignment is designed.')
p.save(os.path.join(OUT, os.path.basename(deck(5))))

# ---------- Unit 6: pointer to Unit 3 after the section swap ----------
p = Presentation(deck(6))
rep(p, 6, 30, 'from Unit 3, part 4.2.', 'from Unit 3, part 5.2.')
p.save(os.path.join(OUT, os.path.basename(deck(6))))

# ---------- Unit 7: GROW, part numbers, notes format ----------
p = Presentation(deck(7))
rep(p, 7, 10, 'what the individual wants to reach', 'what the leader aims to achieve', 'S')
rep(p, 7, 10, 'What the individual wants to reach.', 'What the leader aims to achieve in the conversation.')
rep(p, 7, 19, 'completes part 4.2 of their own file', 'completes part 4.1 of their own file')
rep(p, 7, 23, '1. Link it to part 4.2.', '1. Link it to part 4.1.', whole=True)
rep(p, 7, 23, 'In part 4.2 you prepared', 'In part 4.1 you prepared')
for i in (6, 7, 12, 14, 16):
    has = 'HOW TO TEACH IT' in p.slides[i - 1].notes_slide.notes_text_frame.text
    rep(p, 7, i, 'FACILITATOR GUIDANCE', None if has else 'HOW TO TEACH IT:', whole=True)
p.save(os.path.join(OUT, os.path.basename(deck(7))))

# ---------- Unit 8: notes format ----------
p = Presentation(deck(8))
rep(p, 8, 4, 'FACILITATOR GUIDANCE — Awareness', 'HOW TO TEACH THE SECTION:', whole=True)
p.save(os.path.join(OUT, os.path.basename(deck(8))))

# ---------- Unit 9: old Unit 9 notes on slide 31, R3 bridge, reflection oval, notes format ----------
p = Presentation(deck(9))
nt = p.slides[30].notes_slide.notes_text_frame
ps = list(nt.paragraphs); a = [k for k, q in enumerate(ps) if ptext(q).startswith('Source detail (S2R® manuscript):')][0]
b = [k for k, q in enumerate(ps) if ptext(q).startswith('Professional insights:')][0]
for q in ps[a:b]:
    LOG.append((9, 31, 'N', ptext(q), None)); q._p.getparent().remove(q._p)
rep(p, 9, 18, 'RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery.', 'RESTORE by activating the relevant Seven Unclogging Lever and verifying recovery. Review–Realign–Restore is the cycle every performance review follows. Here the executive team applies it together to a clog that crosses executive portfolios.')
ov = [sh for sh in p.slides[22].shapes if sh.has_text_frame and sh.text_frame.text.strip() == '4']
assert len(ov) == 1; set_ptext(ov[0].text_frame.paragraphs[0], '4.5'); LOG.append((9, 23, 'S', '4', '4.5'))
rep(p, 9, 9, 'FACILITATOR GUIDANCE — Intelligence', 'HOW TO TEACH THE SECTION:')
p.save(os.path.join(OUT, os.path.basename(deck(9))))
import json; json.dump(LOG, open(os.path.join(OUT, 'deck_log.json'), 'w'), ensure_ascii=False, indent=1)
print('deck changes:', len(LOG))
