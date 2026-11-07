// WS5.4 Phase 6 verification — exercises the compact on-row cert-summary
// renderer + the lazy per-row fetch wiring against sample FLAT-shape RPC JSON.
// Mirrors the exact logic added to dashboard_F.html (no DOM/network needed).

// ── copied verbatim from dashboard_F.html ─────────────────────────────────
function escapeHtml(s) {
  if (s === null || s === undefined) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function renderRowCertSummary(mountEl, d) {
  const hasPct = d && d.final_pct !== null && d.final_pct !== undefined;
  if (!hasPct) {
    mountEl.innerHTML = '<span class="rcs-pct rcs-unscored">Not yet scored</span>';
    mountEl.style.fontFamily = 'inherit';
    return;
  }
  const certified = d.certified === true;
  mountEl.innerHTML =
    '<span class="rcs-pct">' + escapeHtml(String(d.final_pct)) + '%</span>' +
    '<span class="rcs-cert ' + (certified ? 'is-certified' : 'not-certified') + '">' +
      (certified ? 'Certified' : 'Not yet') + '</span>';
  mountEl.style.fontFamily = 'inherit';
}

// stub mount element
const mk = () => ({ innerHTML: '', style: {} });

let pass = 0, fail = 0;
const check = (name, cond, detail) => {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + (detail ? '  → ' + detail : '')); }
};

// ── (a) scored participant: final % + certified badge, no expansion ────────
console.log('\n(a) scored + certified (flat shape):');
let el = mk();
renderRowCertSummary(el, {
  unit2_avg: 88, unit3_avg: 91, unit4_avg: 84, capstone_avg: null,
  capstone_pending: true, final_pct: 87, certified: true, unscored_lens_count: 0
});
console.log('   →', el.innerHTML);
check('shows final %', el.innerHTML.includes('87%'));
check('shows Certified badge', el.innerHTML.includes('is-certified') && el.innerHTML.includes('Certified'));
check('inherits page font', el.style.fontFamily === 'inherit');

console.log('\n(a2) scored + NOT yet certified:');
el = mk();
renderRowCertSummary(el, { final_pct: 62, certified: false, unscored_lens_count: 2 });
console.log('   →', el.innerHTML);
check('shows final %', el.innerHTML.includes('62%'));
check('shows Not yet badge', el.innerHTML.includes('not-certified') && el.innerHTML.includes('Not yet'));
check('does NOT claim certified', !el.innerHTML.includes('is-certified'));

console.log('\n(a3) final_pct = 0 (boundary — still a real score, not unscored):');
el = mk();
renderRowCertSummary(el, { final_pct: 0, certified: false });
console.log('   →', el.innerHTML);
check('renders 0% (not treated as unscored)', el.innerHTML.includes('0%') && !el.innerHTML.includes('Not yet scored'));

// ── (b) unscored: quiet "Not yet scored", never an error ───────────────────
console.log('\n(b) unscored participant (final_pct null / undefined / missing):');
[ { final_pct: null, certified: false },
  { final_pct: undefined, certified: false },
  { certified: false }
].forEach((d, i) => {
  el = mk();
  renderRowCertSummary(el, d);
  console.log('   case', i, '→', el.innerHTML);
  check('case ' + i + ': quiet "Not yet scored"', el.innerHTML.includes('Not yet scored') && el.innerHTML.includes('rcs-unscored'));
  check('case ' + i + ': no badge / no error text', !el.innerHTML.includes('rcs-cert') && !/error/i.test(el.innerHTML));
});

// ── (d) one RPC per row with correct (profile_id, cohort_id) ───────────────
console.log('\n(d) one RPC per row, correct (p_profile_id, p_cohort_id):');
const rpcCalls = [];
const supabaseClient = {
  rpc: async (fn, params) => {
    rpcCalls.push({ fn, params });
    return { data: { final_pct: 75, certified: false }, error: null };
  }
};
// mirror of loadParticipantFinalScore (4-arg form)
async function loadParticipantFinalScore(profileId, cohortId, mountEl, renderer) {
  if (!mountEl || !profileId || !cohortId) return;
  try {
    const res = await supabaseClient.rpc('get_participant_final_score', {
      p_profile_id: profileId, p_cohort_id: cohortId
    });
    if (res.error || !res.data || typeof res.data !== 'object') return;
    const d = Array.isArray(res.data) ? res.data[0] : res.data;
    (renderer || renderRowCertSummary)(mountEl, d);
  } catch (e) {}
}

const roster = [
  { participant_id: 'prof-AAA', cohortId: 'coh-1' },
  { participant_id: 'prof-BBB', cohortId: 'coh-1' },
  { participant_id: 'prof-CCC', cohortId: 'coh-1' },
];
for (const r of roster) {
  await loadParticipantFinalScore(r.participant_id, r.cohortId, mk(), renderRowCertSummary);
}
check('one RPC per row', rpcCalls.length === roster.length, 'got ' + rpcCalls.length);
check('all hit get_participant_final_score', rpcCalls.every(c => c.fn === 'get_participant_final_score'));
check('correct profile_id per row', rpcCalls.every((c, i) => c.params.p_profile_id === roster[i].participant_id));
check('correct cohort_id per row', rpcCalls.every((c, i) => c.params.p_cohort_id === roster[i].cohortId));
console.log('   calls:', JSON.stringify(rpcCalls.map(c => c.params)));

// missing cohortId → skip gracefully (no RPC, no throw)
console.log('\n(d2) row with no cohortId skips gracefully:');
const before = rpcCalls.length;
await loadParticipantFinalScore('prof-DDD', null, mk(), renderRowCertSummary);
check('no RPC fired when cohortId missing', rpcCalls.length === before);

console.log('\n──────────────────────────────');
console.log('PASS: ' + pass + '   FAIL: ' + fail);
process.exit(fail ? 1 : 0);
