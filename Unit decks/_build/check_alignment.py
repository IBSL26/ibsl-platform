"""Does the deck carry what the facilitator and participant files carry? Usage: python3 check_alignment.py <deck.pptx> <outline.json> <arrays.txt>
1. Every sentence of every guidance block of the facilitator page (Sections 1 to 5) is looked for in the notes of slides 5 onwards.
2. Every card text of the pages (concepts, dimensions, functions, indicators, Flammables, elements, SiP questions, summary) is looked for too.
Sentences that are not found word for word are listed: read each one and decide (some are spoken to participants as "you")."""
import json, re, sys
from pptx import Presentation
deck, outline, arrays = sys.argv[1:4]
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'[“”"‘’\'`]', '', t.replace(' → ', ', ').replace(' = ', ' is '))).strip().lower()
p = Presentation(deck)
notes = norm(' \n '.join(s.notes_slide.notes_text_frame.text for i, s in enumerate(p.slides, 1) if i >= 5))
o = json.load(open(outline, encoding='utf8'))
miss = []
def sentences(line):
    line = re.sub(r'^[◆📋]\s*', '', line)
    for s in re.split(r'(?<=[.?!])\s+(?=[A-Z"“])', line):
        s = s.strip()
        if len(s) > 12: yield s
for si, sec in enumerate(o['F']['sections']):
    if si == 0: continue
    blocks = [(f'S{si} lead', b) for b in sec['lead']['guidance']] + [(f"{pt['title'][:12]}", b) for pt in sec['parts'] for b in pt['guidance']]
    for where, b in blocks:
        for line in b[1:]:
            for s in sentences(line):
                s2 = re.sub(r'^(Ask|Collect|Keep|Explain|Set the frame|Purpose|Section intent|Facilitator emphasis|Recording|Bridge to the definition|Closing the unit|Return to the opening question|Closing commitment|Transition to Unit 3|Tangible outputs check|Working in groups|Confirming each SiP domain|Test the SiP|Closing Section 4|Then reinforce the connection|Producing the Strategy Architecture|Positioning the statement|Into the Capstone|Key concept to linger on|Taking participants through the \d concepts|Taking participants through the \d dimensions|HOW — key facilitation moment|WHEN|The central question|\d\. [A-Za-z &]+ —|The Value Triad \(Creates · Delivers · Sustains\)): ?', '', s).strip()
                if norm(s2) not in notes and norm(s) not in notes:
                    miss.append((where, s))
print(f'facilitator guidance: {len(miss)} sentence(s) not found word for word')
for w, s in miss: print(f'  [{w}] {s}')
# card text from the data arrays
txt = open(arrays, encoding='utf8').read().split('=====P SUMMARY')[0]
vals = re.findall(r'"(?:what|impl|fail|def|governs|why|si|sip|good|miss|risk|guide|lead|body|intro)": "((?:[^"\\]|\\.)*)"', txt)
cm = []
for v in set(vals):
    v = re.sub(r'<[^>]+>', '', json.loads('"' + v + '"'))
    for s in sentences(v):
        if norm(s) not in notes and norm(s.rstrip(':;')) not in notes: cm.append(s)
print(f'card text: {len(cm)} sentence(s) not found word for word')
for s in sorted(cm): print('  ', s)
