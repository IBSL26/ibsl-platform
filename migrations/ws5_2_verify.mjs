// WS5.2 Phase-6 verification (no external deps).
// The RPC needs an auth session (can't run headless), so we extract the REAL
// render functions from dashboard_A.html and collection.html and feed them
// RPC-shaped sample objects, asserting the required scenarios.

import fs from 'node:fs';

let pass = 0, fail = 0;
function check(name, cond, extra) {
  console.log((cond ? 'PASS' : 'FAIL') + '  ' + name + (cond ? '' : '   ' + (extra || '')));
  cond ? pass++ : fail++;
}
function slice(file, startTok, endTok) {
  const s = file.indexOf(startTok); const e = file.indexOf(endTok, s + 1);
  if (s < 0 || e < 0) throw new Error('cannot slice ' + startTok);
  return file.slice(s, e);
}

// ── dashboard_A.html: certScoreMarkup(d, variant) ────────────────────────────
const aFile = fs.readFileSync(new URL('../dashboard_A.html', import.meta.url), 'utf8');
const certScoreMarkup = new Function('escapeHtml',
  slice(aFile, 'function certScoreMarkup(', 'function hydrateCertScores(') + '\nreturn certScoreMarkup;'
)(x => x);

console.log('\n── A/B (dashboard_A): certScoreMarkup ──');
// (a) fully scored, full variant
const aFull = certScoreMarkup(
  { unit2_avg: 85, unit3_avg: 90, unit4_avg: 100, capstone_avg: null, capstone_pending: true,
    final_pct: 68.75, certified: false, unscored_lens_count: 0 }, 'full');
check('(a) three unit averages shown',
      aFull.includes('85 / 100') && aFull.includes('90 / 100') && aFull.includes('100 / 100'), aFull);
check('(a) final % shown', aFull.includes('68.75%'));
check('(a) full variant has heading', aFull.includes('Certification score'));
check('(a) no "in progress" when fully scored', !aFull.includes('in progress'));
check('(d) capstone Pending + not-yet-certified', aFull.includes('Pending') && aFull.includes('Not yet certified') && aFull.includes('cert-badge--no'));

// (b) partial: units 3 & 4 null, unscored note present
const aPartial = certScoreMarkup(
  { unit2_avg: 80, unit3_avg: null, unit4_avg: null, capstone_avg: null, capstone_pending: true,
    final_pct: 20, certified: false, unscored_lens_count: 2 }, 'full');
check('(b) null unit avgs render "in progress"', (aPartial.match(/in progress/g) || []).length === 2, aPartial);
check('(b) scored unit still shows number', aPartial.includes('80 / 100'));
check('(b) unscored-count note shown', aPartial.includes('2 reviewed lenses not yet scored'));

// certified-true sample proves the yes-badge path (RPC keeps it false today)
const aCert = certScoreMarkup({ unit2_avg: 95, unit3_avg: 95, unit4_avg: 95, capstone_pending: true,
  final_pct: 90, certified: true, unscored_lens_count: 0 }, 'full');
check('badge flips to Certified when certified:true', aCert.includes('cert-badge--yes') && aCert.includes('>Certified<'));

// compact variant: no heading, badge + final present
const aCompact = certScoreMarkup({ unit2_avg: 50, unit3_avg: null, unit4_avg: null, capstone_pending: true,
  final_pct: 12.5, certified: false, unscored_lens_count: 1 }, 'compact');
check('compact variant omits heading', !aCompact.includes('Certification score') && aCompact.includes('cert-score--compact'));
check('compact still has final % + badge', aCompact.includes('12.5%') && aCompact.includes('Not yet certified'));

// ── collection.html: renderCert + fillCertSection ────────────────────────────
const cFile = fs.readFileSync(new URL('../collection.html', import.meta.url), 'utf8');
function makeNode(tag, cls, txt) {
  return { tag: tag || 'div', className: cls || '', textContent: (txt != null ? String(txt) : ''),
           children: [], innerHTML: '', appendChild(c) { this.children.push(c); return c; } };
}
const el = (tag, cls, txt) => makeNode(tag, cls, txt);
function textOf(n) { let t = n.textContent || ''; (n.children || []).forEach(c => { t += ' ' + textOf(c); }); return t; }

const renderCert = new Function('el',
  slice(cFile, 'function renderCert(', 'function boot(') + '\nreturn renderCert;'
)(el);

let rpcCalled = 0;
const supabaseClient = { rpc: () => { rpcCalled++; return Promise.resolve({ data: null, error: null }); } };
const fillCertSection = new Function('el', 'supabaseClient', 'participantId', 'renderCert',
  slice(cFile, 'function fillCertSection(', 'function renderCert(') + '\nreturn fillCertSection;'
)(el, supabaseClient, 'pid-1', renderCert);

console.log('\n── C (collection): renderCert / fillCertSection ──');
const UNIT_TOTAL = { 2: 3, 3: 5, 4: 3 };

// (a) fully scored
const bodyFull = makeNode('div');
renderCert(bodyFull, { unit2_avg: 85, unit3_avg: 88, unit4_avg: 100, capstone_pending: true,
  final_pct: 68.25, certified: false, unscored_lens_count: 0 },
  u => ({ scored: UNIT_TOTAL[u], total: UNIT_TOTAL[u] }));
const tFull = textOf(bodyFull);
check('(a) collection fully-scored shows averages', tFull.includes('85 / 100') && tFull.includes('88 / 100') && tFull.includes('100 / 100'), tFull);
check('(a) collection shows Final % + Pending + Not yet certified',
      tFull.includes('68.25%') && tFull.includes('Pending') && tFull.includes('Not yet certified'));
check('(a) collection no "in progress" when fully scored', !tFull.includes('in progress'));

// (b) partial: unit2 1/3, unit3 0/5, unit4 3/3 scored
const bodyPartial = makeNode('div');
renderCert(bodyPartial, { unit2_avg: 70, unit3_avg: null, unit4_avg: 90, capstone_pending: true,
  final_pct: 22.5, certified: false, unscored_lens_count: 4 },
  u => ({ 2: { scored: 1, total: 3 }, 3: { scored: 0, total: 5 }, 4: { scored: 3, total: 3 } }[u]));
const tPartial = textOf(bodyPartial);
check('(b) partial unit labelled "in progress — N of M lenses scored"',
      tPartial.includes('in progress — 1 of 3 lenses scored') && tPartial.includes('in progress — 0 of 5 lenses scored'), tPartial);
check('(b) partial unit does NOT leak the bare partial number 70', !tPartial.includes('70 / 100'));
check('(b) fully-scored unit (4) still shows its average', tPartial.includes('90 / 100'));
check('(b) unscored-count note shown', tPartial.includes('4 reviewed lenses not yet scored'));

// (c) null cohortId -> "No scores yet", no throw, no rpc
rpcCalled = 0;
const sectionC = { _body: makeNode('div') };
let threw = false;
try { fillCertSection(sectionC, null, [], {}); } catch (e) { threw = true; }
check('(c) null cohortId does not throw', !threw);
check('(c) null cohortId shows "No scores yet"', textOf(sectionC._body).includes('No scores yet'));
check('(c) null cohortId skips the RPC entirely', rpcCalled === 0);

// (d) capstone always Pending / certified false reflected
check('(d) Pending shown in both collection renders', tFull.includes('Pending') && tPartial.includes('Pending'));

console.log('\n──────────────────────────────────────────────');
console.log('TOTAL: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
