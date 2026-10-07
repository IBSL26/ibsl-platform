#!/usr/bin/env node
'use strict';
/*
 * check_standards.js — tests the portal files and unit decks against STANDARDS.md.
 * Usage (from this folder):  node check_standards.js
 * Checks rules 1–13, 16 and 24–27. Rules 14, 15 and 17–23 need a human read.
 * Exit code 1 when any breach is found.
 */
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT = __dirname;
const breaches = [], notes = [];
const add = (rule, file, msg) => breaches.push(`[Rule ${rule}] ${file}: ${msg}`);

const UNITS = fs.readdirSync(ROOT).filter(f => /^unit.*\.html$/i.test(f)).sort();
const PAGES = fs.readdirSync(ROOT).filter(f => /\.html$/i.test(f) && !/^unit/i.test(f) && f !== 'collection.html').sort();
const isFac = f => /_f\.html$/i.test(f) || /_F\.html$/.test(f);
const STD = { 1: ['Awareness', 'What'], 2: ['Intelligence', 'Why'], 3: ['Extrapolating', 'Where'], 4: ['Integration', 'Collective'], 5: ['Application', 'In Practice'] };
const U1 = { 1: ['Orientation', 'Overview'], 2: ['Awareness', 'What'], 3: ['Intelligence', 'Why'], 4: ['Extrapolating', 'Where'], 5: ['Integration', 'Collective'], 6: ['Application', 'In Practice'] };

const decode = s => s.replace(/&#x([0-9a-f]+);/gi, (m, h) => String.fromCodePoint(parseInt(h, 16))).replace(/&#(\d+);/g, (m, d) => String.fromCodePoint(+d)).replace(/&middot;/g, '·').replace(/&mdash;/g, '—').replace(/&rarr;|&#8594;/g, '→').replace(/&larr;|&#8592;/g, '←')
  .replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ').replace(/&rsquo;|&#39;/g, "'").replace(/&ldquo;|&rdquo;|&quot;/g, '"').replace(/&reg;/g, '®');
function visible(html) {   // text a user can see (no scripts, styles or comments)
  return decode(html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>|<!--[\s\S]*?-->/g, ' ').replace(/<[^>]+>/g, '\n'));
}
function scriptStrings(html) {   // human-readable strings inside inline scripts
  const out = [];
  html.replace(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g, (m, js) => {
    js.replace(/(['"`])((?:(?!\1)[^\\\n]|\\.){3,400}?)\1/g, (mm, q, s) => { s = s.replace(/<[^>]*>/g, ' '); if (/\s/.test(s) && !/^\[[A-Z0-9→ -]+\]/.test(s)) out.push(decode(s)); });   // console-log tags like [F6] are not visible   // drop tags and their style/class attributes
  });
  return out.join('\n');
}
const ctx = (t, i, n = 45) => t.slice(Math.max(0, i - n), i + n).replace(/\s+/g, ' ').trim();

// Rule 1: the word "lens" never appears in visible text (units, ABCV checkpoints, perspectives)
const LENS = /(?<![\w\-_.$#{\/])(lens|lenses)(?![\w\-_=(\[:]|\.\w)/gi;
function checkLens(file, text) {
  let m;
  while ((m = LENS.exec(text))) add(1, file, `"${m[0]}" … ${ctx(text, m.index, 60)}`);
}

// Rule 24: official unit titles
const TITLES = { 1: 'Behavioural Strategy Fundamentals', 2: 'Strategy Visioning & Success in Practice (SiP)', 3: 'SiP KISS Mapping & OKR Definition', 4: 'Direction Integrity (ABCV-MBT)', 5: 'Aligning Heart & Mind', 6: 'Performance Management Setup', 7: 'Establishing Performance Expectations', 8: 'Performance Measurement', 9: 'Strategic Unclogging', 10: 'ESRG Alignment', 11: 'Culture Reinforcement & Organisational Health', 12: 'Sustaining Performance' };
const unitNo = f => /^unit1_/i.test(f) ? 1 : +(f.match(/lens(\d+)_/i) || [0, -1])[1] + 1;
const strip = h => decode(h.replace(/<[^>]+>/g, '')).replace(/\s+/g, ' ').trim();
const metaOf = html => { const out = {}; const ts = [...html.matchAll(/class="acc-t">([\s\S]*?)<\/(?:span|div)>/g)];
  ts.forEach((m, i) => { const end = i + 1 < ts.length ? ts[i + 1].index : m.index + 600; const seg = html.slice(m.index + m[0].length, Math.min(end, m.index + m[0].length + 400));
    const mm = seg.match(/class="acc-meta">([^<]*)</); const t = strip(m[1]); const k = (t.match(/^\d+\.\d+[a-z]?/) || [t])[0]; out[k] = { t, meta: mm ? decode(mm[1]).trim() : null }; });
  return out; };

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

  // Rule 24: title in top bar and heading
  const U = unitNo(f), T = TITLES[U];
  if (!decode(brand).includes(`Unit ${U} · ${T} — `)) add(24, f, `top bar should read "Unit ${U} · ${T}"`);
  const h1 = strip((html.match(/<h1 class="unit-title">([\s\S]*?)<\/h1>/) || [, ''])[1]);
  if (h1 !== T) add(24, f, `title "${h1}" should be "${T}"`);

  // Rule 10: facilitator files are preparation-only
  if (isFac(f)) {
    // The Strategy Airport lesson game in the Unit 3 facilitator file is the one agreed exception (played with the room; nothing is saved).
    const inputs = (html.match(/<textarea(?! class="sa-ta")|<input(?! class="sa-in")(?![^>]*type=["'](?:hidden|radio|checkbox)["'])|<select|contenteditable/g) || []).length;
    if (inputs) add(10, f, `${inputs} entry field(s)`);
    const saves = (html.match(/localStorage\.setItem/g) || []).length;
    if (saves) add(10, f, `${saves} save call(s)`);
  }

  // Rule 25: reflection labels
  html.replace(/class="(?:reflection-label|ref-label|ref-block-label)"[^>]*>([^<]*)</g, (mm, t) => {
    t = decode(t).trim();
    if (/Reflection/.test(t) && /^(✍|✎)?\s*(Your )?Reflection\b/.test(t) && !/^✎ Reflection( — .+)?$/.test(t)) add(25, f, `reflection label "${t}" should read "✎ Reflection" or "✎ Reflection — [topic]"`);
  });

  // Rule 27: Unit Summary sub-line
  const us = (metaOf(html)['Unit Summary'] || {}).meta;
  const usWant = `Unit ${U} synthesis` + (isFac(f) ? (U === 12 ? ' · S2R® Programme Close' : '') : ' · Review before submitting');
  if (us !== usWant) add(27, f, `Unit Summary sub-line "${us}" should be "${usWant}"`);

  // Rule 6, 7, 8
  const closers = /Unit Close|Micro-Climb Summary/g;
  while ((m = closers.exec(vis))) add(6, f, `"${m[0]}" … ${ctx(vis, m.index)}`);
  if (isFac(f)) { const fn = /FACILITATOR NOTE|Facilitator Note/g; while ((m = fn.exec(vis))) add(7, f, `"${m[0]}" … ${ctx(vis, m.index)}`); }
  html.replace(/class="(?:portfolio-label|acc-t)">(Portfolio[^<]*)</g, (mm, t) => { if (decode(t).trim() !== 'Portfolio Artefact') add(8, f, `portfolio block "${decode(t)}"`); });
}

// Rule 26: participant sub-lines match the facilitator file (parts with the same title)
for (const p of UNITS.filter(x => !isFac(x))) {
  const fac = UNITS.find(x => isFac(x) && x.replace(/_[fF]\.html$/, '') === p.replace(/_[pP]\.html$/, ''));
  if (!fac) { add(9, p, 'no matching facilitator file'); continue; }
  const P = metaOf(fs.readFileSync(path.join(ROOT, p), 'utf8')), F = metaOf(fs.readFileSync(path.join(ROOT, fac), 'utf8'));
  for (const k of Object.keys(P)) {
    if (k === 'Unit Summary' || !F[k]) continue;
    if (P[k].t === F[k].t && F[k].meta && P[k].meta !== F[k].meta) add(26, p, `${k} sub-line "${P[k].meta}" should be "${F[k].meta}"`);
  }
  const pn = Object.keys(P).filter(k => /^\d/.test(k)).sort().join(','), fn = Object.keys(F).filter(k => /^\d/.test(k)).sort().join(',');
  if (pn !== fn) add(9, p, `part numbers differ from ${fac}`);
}

// Rule 24: titles on the portal pages
const pageText = f => fs.existsSync(path.join(ROOT, f)) ? decode(fs.readFileSync(path.join(ROOT, f), 'utf8')) : '';
const idx = pageText('index.html'), dF = pageText('dashboard_F.html'), cap = pageText('capstone_P.html');
for (const [n, t] of Object.entries(TITLES)) {
  if (idx && !idx.includes(`Unit ${n} · ${t}`)) add(24, 'index.html', `missing "Unit ${n} · ${t}"`);
  if (dF && !dF.includes(`Unit ${n} — ${t}'`)) add(24, 'dashboard_F.html', `missing "Unit ${n} — ${t}"`);
  if (cap && n > 1 && !cap.includes(`unit:${n}, title:'${t}'`)) add(24, 'capstone_P.html', `Blueprint title for Unit ${n} should be "${t}"`);
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
  // Rule 13: no "not X — it is Y" constructions
  const NOTX = /\b(?:is|are|was|were|isn't|aren't)\s+not\b[^.;:!?\n—–]{0,90}?\s*[—–;,]\s*(?:it|this|they|that|these)(?:'s|’s|\s+is|\s+are|\s+was)\b|\bnot\s+(?:just|merely|simply|about)\b[^.!?\n]{1,90}?(?:[—–;,]\s*(?:it|this|they)(?:'s|’s|\s+is|\s+are)\b|\bbut\b)|\b(?:isn't|aren't|isn’t|aren’t)\b[^.!?\n]{1,70}?[—–;,]\s*(?:it|they)(?:'s|’s|\s+is|\s+are)\b|(?:^|[.!?]\s+)Not\s+(?:because|through|in|what|about)\b[^.!?\n]{1,60}—/gm;
  let q; const visQ = vis.replace(/&mdash;/g, '—');
  while ((q = NOTX.exec(visQ))) add(13, f, `"not X — it is Y" … ${ctx(visQ, q.index, 60)}`);
  // Rule 13 (wider): "rather than" / "instead of" contrasts, fragments opening "Not …", dash-led "— not …" and "… is not." teaching pairs, in visible text and script strings
  const CONTRAST = /\b(?:rather than|instead of)\b|(?:^|[.!?"”:]\s+)(?:Not|Never)\s+(?:a|an|the|because|through|just|merely|simply|about|only|in|what)\b|[—–]\s*not\s+(?:a|an|the|just|merely|simply|about|because)\b|["”]\s+is\s+not\.|\b(?:is|are)\s+not\s+(?:fine|enough)\.|(?:^|[.!?]\s+)Instead\b/gim;
  const jsNC = scriptStrings(html.replace(/^\s*\/\/.*$/gm, ''));   // code comments are not visible
  for (const text of [visQ, jsNC]) { let c; while ((c = CONTRAST.exec(text))) add(13, f, `contrast "${c[0].trim()}" … ${ctx(text, c.index, 60)}`); }
  let r; const noReg = /\b(Strategy2Results|S2R)(?!®|\w)/g; const visR = vis.replace(/^S2R$/gm, '');   // the square S2R logo mark is exempt
  while ((r = noReg.exec(visR))) add(12, f, `"${r[1]}" without ® … ${ctx(vis, r.index)}`);
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
if (!breaches.length) console.log('\nNo breaches found for rules 1–13, 16 and 24–27.');
else { console.log(`\n${breaches.length} breach(es):`); Object.keys(byRule).sort((a, b) => a - b).forEach(r => { console.log(`\nRule ${r} (${byRule[r].length})`); byRule[r].forEach(b => console.log('  ' + b.replace(/^\[Rule \d+\] /, ''))); }); }
console.log('\nHuman read still needed: rules 14, 15, 17–23.');
process.exit(breaches.length ? 1 : 0);
