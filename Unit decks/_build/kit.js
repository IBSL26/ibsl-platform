// Shared helpers for unit decks: reads extracted unit outlines (JSON) and JS data arrays from the unit HTML files.
const fs = require('fs');
const vm = require('vm');
const N = (...parts) => parts.flat().filter(p => p !== null && p !== undefined && String(p).trim() !== '').join('\n\n');
const clean = s => String(s).replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ').replace(/&mdash;/g, '—').replace(/&ndash;/g, '–')
  .replace(/&rsquo;/g, '’').replace(/&lsquo;/g, '‘').replace(/&ldquo;/g, '“').replace(/&rdquo;/g, '”').replace(/&#39;/g, "'").replace(/&quot;/g, '"')
  .replace(/&middot;/g, '·').replace(/&rarr;/g, '→').replace(/&larr;/g, '←').replace(/&times;/g, '×').replace(/&hellip;/g, '…').replace(/&reg;/g, '®').replace(/&#\d+;/g, '').replace(/\s+/g, ' ').trim();
function literalAt(src, i) {
  const open = src[i], close = open === '[' ? ']' : '}';
  let depth = 0, q = null;
  for (let k = i; k < src.length; k++) {
    const c = src[k];
    if (q) { if (c === '\\') { k++; continue; } if (c === q) q = null; continue; }
    if (c === '"' || c === "'" || c === '`') { q = c; continue; }
    if (c === '[' || c === '{') depth++;
    else if (c === ']' || c === '}') { depth--; if (depth === 0) return src.slice(i, k + 1); }
  }
  throw new Error('unbalanced literal');
}
class Unit {
  constructor(jsonPath, fHtml, pHtml) {
    const j = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    this.F = j.F; this.P = j.P;
    this.fsrc = fs.readFileSync(fHtml, 'utf8'); this.psrc = fs.readFileSync(pHtml, 'utf8');
  }
  js(name, side = 'F') {
    const src = side === 'F' ? this.fsrc : this.psrc;
    const m = new RegExp('(?:var|const|let)\\s+' + name + '\\s*=\\s*([\\[{])').exec(src);
    if (!m) throw new Error('js var not found: ' + name);
    return vm.runInNewContext('(' + literalAt(src, m.index + m[0].length - 1) + ')');
  }
  sec(i) { return this.F.sections[i]; }
  part(i, j) { return this.F.sections[i].parts[j]; }
  num(t) { const m = /^(\d+(\.\d+)?)/.exec(t.replace(/^Facilitator · /, '')); return m ? m[1] : t; }
  ppart(i, j) {
    const fp = this.part(i, j); const key = this.num(fp.title);
    for (const s of this.P.sections) for (const p of s.parts) if (this.num(p.title) === key || p.title === fp.title) return p;
    return null;
  }
  guide() {
    const g = this.F.sections[0];
    return g.lead.guidance.map(b => b.map(l => l.replace(/^◆ /, '')).join('\n'));
  }
  secNotes(i, extra = []) {
    const s = this.sec(i);
    return N(`${s.label.toUpperCase()}\n${s.h2}${s.sub ? '\n' + s.sub : ''}`,
      s.slo.length ? 'Section learning outcomes:\n' + s.slo.map((o, k) => `${k + 1}. ${o}`).join('\n') : '',
      s.lead.guidance.map(b => b.map(l => l.replace(/^◆ /, '')).join('\n')),
      s.lead.content.length ? 'Content:\n' + s.lead.content.join('\n') : '', extra);
  }
  partNotes(i, j, o = {}) {
    const p = this.part(i, j), pp = this.ppart(i, j);
    const head = `${p.title.toUpperCase()}${p.meta ? ' (' + p.meta + ')' : ''}`;
    const g = o.guidance === false ? [] : p.guidance.map(b => b.map(l => l.replace(/^◆ /, '').replace(/^📋 /, '')).join('\n'));
    const c = o.content === false || !p.content.length ? '' : 'Content:\n' + p.content.join('\n');
    const pr = o.prompts === false || !pp || !pp.prompts || !pp.prompts.length ? '' :
      `Participant file (${pp.title}) — prompts participants complete:\n` + pp.prompts.map(x => '- ' + x.replace(/^✍/, '')).join('\n');
    return N(o.head === false ? '' : head, o.before || '', g, c, o.extra || '', pr, o.after || '');
  }
}
module.exports = { Unit, N, clean };
// Deck helpers shared by unit scripts
async function divider(d, u, i, extra) {
  const s = u.sec(i), m = /Section (\d+) · (\S+) — (.+)/.exec(s.label);
  await d.section({ num: +m[1], name: m[2], anchor: m[3], heading: s.h2, outcomes: s.slo, notes: u.secNotes(i, extra) });
}
function pPortfolio(u) {
  for (const s of u.P.sections) for (const p of s.parts) if (/Portfolio/i.test(p.title)) return p;
  return null;
}
async function portfolio(d, u, items, unitNo) {
  const pp = pPortfolio(u);
  await d.cards({ title: 'Portfolio Artefact', cols: items.length, items,
    notes: N(`PORTFOLIO ARTEFACT (participant file: ${pp.title}${pp.meta ? ' · ' + pp.meta : ''})`,
      'Participant activity (participant file): participants answer each prompt in writing:\n' + pp.prompts.map(x => '- ' + x).join('\n'),
      `Participants save the artefact, then submit Unit ${unitNo} to the facilitator from their file (supporting documents can be attached).`) });
}
function mapDivider(u) { return (d, i, extra) => divider(d, u, i, extra); }
module.exports.divider = divider; module.exports.portfolio = portfolio; module.exports.mapDivider = mapDivider;
