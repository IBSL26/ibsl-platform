# -*- coding: utf-8 -*-
"""Reads Carol's four Unit 9 texts (docx turned to markdown by pandoc -t markdown-smart) and writes u9pv_text.json:
the seven clog cards (part 1.2) and the ten executive role cards (part 3.1). The locked wording edits are applied here."""
import re, json, html
def inline(s):
    s = s.strip().replace('\\|', '|').replace('\\.', '.').replace("\\'", '’')
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = s.replace('—', '&mdash;').replace('–', '&ndash;')
    return s
EDITS = [('Employees focus on measurable volume rather than quality or value', 'Employees focus on measurable volume at the expense of quality or value'),
         ('Teams continue escalating customer problems rather than resolving them.', 'Teams continue to escalate customer problems they could resolve themselves.'),
         ('Governance and review forums become reporting rituals rather than mechanisms for resolving the conditions obstructing performance.', 'Governance and review forums become reporting rituals that leave the conditions obstructing performance unresolved.')]
t = open('s1.md', encoding='utf-8').read()
for a, b in EDITS:
    assert t.count(a) == 1, a; t = t.replace(a, b)
clogs = []
for blk in re.split(r'\n### Clog ', t)[1:]:
    blk = blk.split('\n## ')[0]
    head, rest = blk.split('\n', 1)
    num, name = re.match(r'(\d+) — (.+)', head).groups()
    c = {'num': num, 'name': inline(name)}
    c['abcv'] = re.search(r'ABCV element: (.+)', rest).group(1).strip()
    def para(lbl):
        m = re.search(r'\*\*' + re.escape(lbl) + r'\*\* (.+)', rest); assert m, (name, lbl); return inline(m.group(1))
    c['org'] = para('Organisational performance — System reality.')
    c['ppl'] = para('People performance — Contribution reality.')
    c['impact'] = para('Strategic impact.'); c['question'] = para('Diagnostic question.'); c['example'] = para('Worked example.')
    def lst(lbl):
        m = re.search(re.escape(lbl) + r'\n\n((?:-   .+\n\n?)+)', rest); assert m, (name, lbl)
        return [inline(x) for x in re.findall(r'-   (.+)', m.group(1))]
    c['patterns'] = lst('Observable performance patterns:'); c['warnings'] = lst('Early warning signals:')
    clogs.append(c)
assert len(clogs) == 7 and all(len(c['patterns']) == 5 and len(c['warnings']) == 4 for c in clogs)
t3 = open('s3.md', encoding='utf-8').read()
roles = []
for blk in re.split(r'\n### ', t3.split('## 3.1')[1].split('## Participant Reflection')[0])[1:]:
    head, rest = blk.split('\n', 1)
    m = re.match(r'(CEO|CFO|COO|CHRO|CTO/CIO|CMO|CCO|CPO|CRO|CSO) (.+)', head.strip()); assert m, head
    r = {'role': m.group(1), 'remit': inline(m.group(2))}
    def para(lbl):
        mm = re.search(r'\*\*' + re.escape(lbl) + r'\*\* (.+)', rest); assert mm, (head, lbl); return inline(mm.group(1))
    r['decision'] = para('Executive decision or practice.')
    r['los1'] = para('Line of Sight 1 — Performance Outcome.'); r['los2'] = para('Line of Sight 2 — Performance Behaviour.')
    c3 = para('Line of Sight 3 — Performance Condition.')
    r['clog'], r['los3'] = re.match(r'(.+?)\. (.+)', c3).groups()
    r['question'] = para('Question for participants.')
    roles.append(r)
assert len(roles) == 10, len(roles)
json.dump({'clogs': clogs, 'roles': roles}, open('u9pv_text.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('clogs', [c['name'] for c in clogs]); print('roles', [(r['role'], r['clog']) for r in roles])
