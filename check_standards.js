#!/usr/bin/env node
'use strict';
/*
 * check_standards.js — tests the portal files and unit decks against STANDARDS.md.
 * Usage (from this folder):  node check_standards.js
 * Checks rules 1–8, 11, 12 and 16. Rules 9–10, 13–15 and 17–23 need a human read.
 * Exit code 1 when any breach is found.
 */
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT = __dirname;
const breaches = [], notes = [];
const add = (rule, file, msg) => breaches.push(`[Rule ${rule}] ${file}: ${msg}`);

const UNITS = fs.readdirSync(ROOT).filter(f => /^unit.*\.html$/i.test(f)).sort();
const PAGES = ['index.html', 'dashboard_F.html', 'dashboard_A.html', 'capstone_P.html', 'certificate.html'].filter(f => fs.existsSync(path.join(ROOT, f)));
const isFac = f => /_f\.html$/i.test(f) || /_F\.html$/.test(f);
const STD = { 1: ['Awareness', 'What'], 2: ['Intelligence', 'Why'], 3: ['Extrapolating', 'Where'], 4: ['Integration', 'Collective'], 5: ['Application', 'In Practice'] };
const U1 = { 1: ['Orientation', 'Overview'], 2: ['Awareness', 'What'], 3: ['Intelligence', 'Why'], 4: ['Extrapolating', 'Where'], 5: ['Integration', 'Collective'], 6: ['Application', 'In Practice'] };

const decode = s => s.replace(/&middot;/g, '·').replace(/&mdash;/g, '—').replace(/&rarr;|&#8594;/g, '→').replace(/&larr;|&#8592;/g, '←')
  .replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ').replace(/&rsquo;|&#39;/g, "'").replace(/&ldquo;|&rdquo;|&quot;/g, '"').replace(/&reg;/g, '®');
function visible(html) {   // text a user can see (no scripts, styles or comments)
  return decode(html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>|<!--[\s\S]*?-->/g, ' ').replace(/<[^>]+>/g, '\n'));
}
function scriptStrings(html) {   // human-readable strings inside inline scripts
  const out = [];
  html.replace(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g, (m, js) => {
    js.replace(/(['"`])((?:(?!\1)[^\\\n]|\\.){3,400}?)\1/g, (mm, q, s) => { s = s.replace(/<[^>]*>/g, ' '); if (/\s/.test(s)) out.push(decode(s)); });   // drop tags and their style/class attributes
  });
  return out.join('\n');
}
const ctx = (t, i, n = 45) => t.slice(Math.max(0, i - n), i + n).replace(/\s+/g, ' ').trim();

// Rule 1: "lens" meaning a unit
const LENS_UNIT = /\b(the|this|each|next|final|full|entire|every|subsequent|previous|one)\s+(lens|lenses)\b|\blens\s+(content|intent|in practice)\b|\blenses of this programme\b/gi;
let abcv = 0;
function checkLens(file, text) {
  let m;
  while ((m = LENS_UNIT.exec(text))) {
    const c = ctx(text, m.index, 70);
    const wide = ctx(text, m.index, 600);
    if (/\bABCV\b/.test(wide)) { abcv++; continue; }   // ABCV lenses: open decision, not a unit
    if (/ABCV|ABCV–MBT|Arena|Boundaries|Competition|Value Proposition|MBT/i.test(c) || /the lens (of|through)|through the (same )?lens|same lens/i.test(c)) { if (/ABCV|MBT|Arena|Boundaries|Competition|Value Proposition/i.test(c)) abcv++; continue; }
    add(1, file, `"${m[0]}" … ${c}`);
  }
}

for (const f of UNITS) {
  const html = fs.readFileSync(path.join(ROOT, f), 'utf8');
  const vis = visible(html), js = scriptStrings(html);
  const names = /^unit1_/i.test(f) ? U1 : STD;
  checkLens(f, vis); checkLens(f, js);

  // Rule 2: headings and tabs
  html.replace(/class="(?:mod-hero-label|mod-badge)"[^>]*>([^<]*)</g, (m, t) => {
    t = decode(t).trim(); const s = t.match(/^Section (\d)/);
    if (!s) return;
    const [n, a] = names[+s[1]] || [];
    if (t !== `Section ${s[1]} · ${n} — ${a}`) add(2, f, `heading "${t}" should be "Section ${s[1]} · ${n} — ${a}"`);
  });
  html.replace(/<div class="(?:mod-tab|tab-btn)[^"]*" onclick="showMod\([^)]*\)"[^>]*>([\s\S]*?)<\/div>/g, (m, inner) => {
    const t = decode(inner.replace(/<br\s*\/?>/g, ' / ').replace(/<[^>]+>/g, ' / ')).replace(/(\s*\/\s*)+/g, ' / ').replace(/^ \/ | \/ $/g, '').trim();
    if (/Guide/.test(t)) { if (t !== 'Facilitator / Guide / Overview') add(2, f, `guide tab "${t}"`); return; }
    const s = t.match(/^Section (\d)/); if (!s) { add(2, f, `tab "${t}"`); return; }
    const [n, a] = names[+s[1]] || [];
    if (t !== `Section ${s[1]} / ${n} / ${a}`) add(2, f, `tab "${t}" should be "Section ${s[1]} / ${n} / ${a}"`);
  });
  let m; const iz = /Integration Zone|\bIntegrating\b/g;
  while ((m = iz.exec(vis))) add(2, f, `"${m[0]}" … ${ctx(vis, m.index)}`);

  // Rule 3: next / back buttons
  html.replace(/<button class="btn[^"]*" onclick="showMod\([^)]*\)"[^>]*>([^<]*)<\/button>/g, (mm, t) => {
    t = decode(t).trim();
    if (!/[←→]/.test(t) || /Assessment/.test(t)) return;
    if (!/^(Section \d — [A-Za-z]+ →|← Section \d — [A-Za-z]+|← Facilitator Guide)$/.test(t)) add(3, f, `button "${t}"`);
  });

  // Rule 4: Facilitator Guide tab
  if (isFac(f)) {
    if (!/class="mod-hero-label">Facilitator Guide</.test(html)) add(4, f, 'no Facilitator Guide tab');
    if (!/← Facilitator Guide|&larr; Facilitator Guide/.test(html)) add(4, f, 'Section 1 has no "← Facilitator Guide" button');
  }

  // Rule 5: top bar, line above the title, badge
  const brand = (html.match(/<div class="nav-brand">([\s\S]*?)<\/div>/) || [])[1] || '';
  if (!/^<strong>Module \d · [A-Za-z]+<\/strong>Unit \d+ · .+ — (Participant|Facilitator)$/.test(decode(brand))) add(5, f, `top bar "${decode(brand).replace(/<[^>]+>/g, ' / ')}"`);
  const eb = decode(((html.match(/class="eyebrow">([^<]*)</) || [])[1] || '').trim());
  if (!/^Module \d · [A-Za-z]+ · Unit \d+$/.test(eb)) add(5, f, `line above title "${eb}"`);
  const badge = decode(((html.match(/class="nav-badge">([^<]*)</) || [])[1] || '').trim());
  if (badge !== (isFac(f) ? 'Facilitator View' : 'Participant View')) add(5, f, `badge "${badge}"`);

  // Rule 6, 7, 8
  const closers = /Unit Close|Micro-Climb Summary/g;
  while ((m = closers.exec(vis))) add(6, f, `"${m[0]}" … ${ctx(vis, m.index)}`);
  if (isFac(f)) { const fn = /FACILITATOR NOTE|Facilitator Note/g; while ((m = fn.exec(vis))) add(7, f, `"${m[0]}" … ${ctx(vis, m.index)}`); }
  html.replace(/class="(?:portfolio-label|acc-t)">(Portfolio[^<]*)</g, (mm, t) => { if (decode(t).trim() !== 'Portfolio Artefact') add(8, f, `portfolio block "${decode(t)}"`); });
}

// Rules 1, 11, 12 on every file (units + portal pages)
const US = /\b(organization|organizations|organizational|behavior|behaviors|behavioral|color|colors|center|centered|analyze|analyzed|prioritize|prioritized|optimize|optimized|realize|realized|recognize|recognized|recognizes|utilize|favor|favorite|honor|labor|defense|catalog|program|\w+i[sz]ation|paralyzed|paralyze|\w{3,}izes?|\w{3,}ized|\w{3,}izing)\b/gi;
const NOT_US = /^(size[sd]?|sizing|prize[sd]?|seize[sd]?|seizing|capsize[sd]?|outsized?|\w*isation|\w*isations)$/i;
for (const f of [...UNITS, ...PAGES]) {
  const html = fs.readFileSync(path.join(ROOT, f), 'utf8');
  const vis = visible(html), js = scriptStrings(html);
  if (!/^unit/i.test(f)) { checkLens(f, vis); checkLens(f, js); }
  for (const text of [vis, js]) {
    let m;
    while ((m = US.exec(text))) {
      const c = ctx(text, m.index);
      if (/BEHAVIORAL STRATEGY & LEADERSHIP/i.test(c)) continue;   // logo text
      if (NOT_US.test(m[0])) continue;
      const pre = text.slice(Math.max(0, m.index - 2), m.index), post = text[m.index + m[0].length] || '';
      if (/[-_.#:]$/.test(pre) || /:\s$/.test(pre) || /[-_=(]/.test(post) || (post === ':' && (/^(color|center)$/i.test(m[0]) || /[;{]/.test(text.slice(m.index, m.index + 40))))) continue;   // CSS or code (text-align:center, color:#fff, lens_catalog)
      add(11, f, `US spelling "${m[0]}" … ${c}`);
    }
    const typo = /Strategy2Result®|Strategy2Result(?!s)\b/g;
    while ((m = typo.exec(text))) add(12, f, `"${m[0]}" … ${ctx(text, m.index)}`);
  }
}

// Rule 16: unit decks, minimum 24pt
function unzip(buf) {   // minimal zip reader (central directory)
  const files = {}; let e = buf.length - 22;
  while (e >= 0 && buf.readUInt32LE(e) !== 0x06054b50) e--;
  if (e < 0) return files;
  let p = buf.readUInt32LE(e + 16); const n = buf.readUInt16LE(e + 10);
  for (let i = 0; i < n; i++) {
    const method = buf.readUInt16LE(p + 10), csize = buf.readUInt32LE(p + 20), nl = buf.readUInt16LE(p + 28), xl = buf.readUInt16LE(p + 30), cl = buf.readUInt16LE(p + 32), off = buf.readUInt32LE(p + 42);
    const name = buf.slice(p + 46, p + 46 + nl).toString();
    const lnl = buf.readUInt16LE(off + 26), lxl = buf.readUInt16LE(off + 28), data = buf.slice(off + 30 + lnl + lxl, off + 30 + lnl + lxl + csize);
    files[name] = () => (method === 8 ? zlib.inflateRawSync(data) : data).toString('utf8');
    p += 46 + nl + xl + cl;
  }
  return files;
}
const DECKS = path.join(ROOT, 'Unit decks');
if (fs.existsSync(DECKS)) {
  for (const d of fs.readdirSync(DECKS).filter(x => /\.pptx$/i.test(x) && !x.startsWith('~$'))) {
    const z = unzip(fs.readFileSync(path.join(DECKS, d)));
    for (const name of Object.keys(z).filter(k => /^ppt\/slides\/slide\d+\.xml$/.test(k))) {
      const xml = z[name](); let m; const re = /\bsz="(\d+)"/g;
      while ((m = re.exec(xml))) if (+m[1] < 2400) add(16, 'Unit decks/' + d, `${name.replace(/.*\//, '')} has ${+m[1] / 100}pt text`);
      xml.replace(/<a:t>([^<]*)<\/a:t>/g, (mm, t) => { if (/\blens(es)?\b/i.test(t)) add(1, 'Unit decks/' + d, `"${t}"`); if (/Strategy2Result(?!s)/.test(t)) add(12, 'Unit decks/' + d, `"${t}"`); });
    }
  }
}

// Report
const byRule = {};
for (const b of breaches) { const r = b.match(/^\[Rule (\d+)\]/)[1]; (byRule[r] = byRule[r] || []).push(b); }
console.log('S2R standards check — ' + new Date().toISOString().slice(0, 10));
console.log(`Files checked: ${UNITS.length} unit files, ${PAGES.length} portal pages` + (fs.existsSync(DECKS) ? ', Unit decks' : ''));
if (!breaches.length) console.log('\nNo breaches found for rules 1–8, 11, 12 and 16.');
else { console.log(`\n${breaches.length} breach(es):`); Object.keys(byRule).sort((a, b) => a - b).forEach(r => { console.log(`\nRule ${r} (${byRule[r].length})`); byRule[r].forEach(b => console.log('  ' + b.replace(/^\[Rule \d+\] /, ''))); }); }
if (abcv) console.log(`\nOpen decision: ${abcv} ABCV "lens" mention(s) in Units 2 and 4 (see STANDARDS.md). Not counted as breaches.`);
console.log('\nHuman read still needed: rules 9, 10, 13, 14, 15, 17–23.');
process.exit(breaches.length ? 1 : 0);
