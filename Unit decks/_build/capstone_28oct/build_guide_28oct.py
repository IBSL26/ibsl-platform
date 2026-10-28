# Capstone S2R Blueprint guide rebuilt from the live Blueprint boxes (28 Oct 2026). Usage: python3 -B build_guide_28oct.py <backup docx> <capstone_P.html> <out docx>
import sys, re, copy, json, docx
src, page, out = sys.argv[1:4]
d = docx.Document(src)
html = open(page, encoding='utf-8').read()
BP = []
for m in re.finditer(r"\{ key:'(u\d+)', unit:(\d+), title:'([^']*)', boxes:\[(.*?)\]\}", html, re.S):
    boxes = re.findall(r"\['([0-9]+[A-H])','([^']*)','([^']*)'\]", m.group(4))
    BP.append((int(m.group(2)), boxes))
assert len(BP) == 12 and sum(len(b) for _, b in BP) == 60, [len(b) for _, b in BP]
def case(t): return t.replace('[Case]’s', 'the organisation’s').replace('[Case]', 'the organisation').replace('your Capstone S2R Blueprint', 'the Capstone S2R Blueprint')
def set_runs(p, *parts):
    rs = p.runs
    for r in rs[len(parts):]: r._r.getparent().remove(r._r)
    for i, (txt, bold) in enumerate(parts):
        if i < len(rs): rs[i].text = txt; rs[i].bold = bold
        else: r = p.add_run(txt); r.bold = bold
NAMES = [('Strategy2Results® (S2R®) Capability Blueprint', 'Capstone S2R Blueprint'), ('S2R® Capability Blueprint', 'Capstone S2R Blueprint')]
def fix_names(p):
    for r in p.runs:
        for a, b in NAMES:
            if a in r.text: r.text = r.text.replace(a, b)
def all_pars():
    for p in d.paragraphs: yield p
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs: yield p
    for s in d.sections:
        for p in s.footer.paragraphs: yield p
        for p in s.header.paragraphs: yield p
P = d.paragraphs
# Section 1 · how it is built
set_runs(P[12], ('Each section fills as soon as every member of the group selects Agree on the group work in that unit (Section 5; Unit 1 part 6.2).', None))
set_runs(P[13], ('One member acts as scribe and types what the group agrees on one shared record. Participants do not edit the Capstone S2R Blueprint page itself.', None))
set_runs(P[15], ('At the capstone the group presents and defends its integrated response to the panel, as the organisation’s executive team.', None))
# Section 3 · criteria
set_runs(P[50], ('The panel (IBSL programme facilitators, an invited academic and, for a company cohort, the client company’s management) scores the team’s Capstone S2R Blueprint and each member’s individual showcase, and returns one capstone score per member out of 100.', None))
crit = {55: ('Problem Charter', ' (Unit 1 · 5%): how fully the Capstone S2R Blueprint as a whole answers the central problem and builds the capabilities the Charter names.'),
        56: ('Direction', ' (Units 2–4 · 15%): strategic intent, success definition, priorities and direction integrity.'),
        57: ('Influence', ' (Units 5–9 · 25%): alignment, performance management, expectations, measurement and unclogging.'),
        58: ('Grounding', ' (Units 10–12 · 15%): the ESRG operating environment and organisational health, leveraged through the Quarterly Three Lines of Sight and KISS to sustain strategic performance.'),
        60: ('Command', ' (each member · 20%): the member’s grasp of the whole Capstone S2R Blueprint and of their executive role within it: which Key Results, contributions, owners and measures sit with their role, and how their decisions connect across sections.'),
        61: ('Delivery', ' (each member · 20%): how clearly and credibly the member presents and defends the team’s decisions: evidence from the Capstone S2R Blueprint, consistent answers under follow-up, and a position held or revised for stated reasons.')}
for i, (a, b) in crit.items(): set_runs(P[i], (a, True), (b, None))
# Section 4 · Problem Charter in the live boxes
set_runs(P[84], ('Which challenges will we address? ', True), ('Choose the three challenges in each area the executive team will address in the programme.', None))
set_runs(P[92], ('Your group agrees its Charter on the group record in Unit 1, part 6.2. When every member selects Agree, the Charter fills Section 1 of the Capstone S2R Blueprint, one box per part.', None))
set_runs(P[98], ('Before your group selects Agree on the Problem Charter, check that:', None))
for i in (97, 96, 95, 94, 93):  # "How to complete 1H" (sources of experience) is no longer a box
    P[i]._p.getparent().remove(P[i]._p)
# Area table
T = d.tables
T[1].rows[3].cells[3].paragraphs[0].runs[0].text = 'Alignment, performance management, expectations, measurement and unclogging'
set_runs(T[1].rows[3].cells[3].paragraphs[0], ('Alignment, performance management, expectations, measurement and unclogging', None))
set_runs(T[1].rows[4].cells[3].paragraphs[0], ('Operating conditions, organisational health and sustained performance', None))
def fill(table, rows):
    while len(table.rows) - 1 < len(rows): table._tbl.append(copy.deepcopy(table.rows[-1]._tr))
    while len(table.rows) - 1 > len(rows): table._tbl.remove(table.rows[-1]._tr)
    for r, vals in zip(table.rows[1:], rows):
        for c, v in zip(r.cells, vals): set_runs(c.paragraphs[0], (v, True if c is r.cells[0] else None))
for k, (unit, boxes) in enumerate(BP):
    fill(T[2 + k], [(b, n, case(t)) for b, n, t in boxes])
u1 = BP[0][1]
fill(T[17], [('Group details', '—', 'Group number, members and their executive roles, date.')] + [(n, b, case(t)) for b, n, t in u1])
for p in all_pars(): fix_names(p)
d.save(out)
print('saved', out, [len(b) for _, b in BP])
