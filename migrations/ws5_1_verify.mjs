// WS5.1 Phase-6 verification harness (no external deps).
// Extracts the REAL buildFeedbackSection() from dashboard_F.html and runs it in
// a minimal DOM stub with real synthetic events. Also runs the verbatim
// commitReview score-extraction logic. No network/DB — RPCs are mocked and
// asserted on payload (true DB write is prod-only).

import fs from 'node:fs';

let pass = 0, fail = 0;
function check(name, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  console.log((ok ? 'PASS' : 'FAIL') + '  ' + name + '  -> ' + JSON.stringify(got) +
              (ok ? '' : '  (want ' + JSON.stringify(want) + ')'));
  ok ? pass++ : fail++;
}

// ── DOM stub ─────────────────────────────────────────────────────────────────
function makeEl(tag) {
  const el = {
    tagName: tag, children: [], _h: {}, style: {}, dataset: {},
    className: '', id: '', textContent: '', value: '', disabled: false,
    placeholder: '', _classes: new Set(),
    classList: {
      add: c => el._classes.add(c),
      remove: c => el._classes.delete(c),
      contains: c => el._classes.has(c),
    },
    setAttribute(k, v) { el['_attr_' + k] = v; },
    appendChild(c) { el.children.push(c); return c; },
    addEventListener(t, fn) { (el._h[t] = el._h[t] || []).push(fn); },
    dispatch(t, ev) { (el._h[t] || []).forEach(fn => fn(ev || { stopPropagation() {} })); },
    focus() { el._focused = true; },
  };
  return el;
}
function walk(el, acc) { acc.push(el); (el.children || []).forEach(c => walk(c, acc)); return acc; }
function classesOf(el) {
  const fromStr = (el.className || '').split(/\s+/).filter(Boolean);
  return new Set([...fromStr, ...el._classes]);
}
const byClass = (root, c) => walk(root, []).filter(el => classesOf(el).has(c));
const byId    = (root, id) => walk(root, []).filter(el => el.id === id);
const byText  = (root, t) => walk(root, []).filter(el => (el.textContent || '') === t);

// ── Extract the REAL buildFeedbackSection from the shipped file ───────────────
const file = fs.readFileSync(new URL('../dashboard_F.html', import.meta.url), 'utf8');
const startTok = 'function buildFeedbackSection(';
const endTok   = 'function wireFeedbackAutosave(';
const s = file.indexOf(startTok);
const e = file.indexOf(endTok, s);
if (s < 0 || e < 0) { console.error('Could not locate buildFeedbackSection'); process.exit(2); }
const src = file.slice(s, e);   // whole function (ends just before wireFeedbackAutosave)

// Mocked dependencies + capture handle for amend_submission_score.
let rpcCalls = [];
const supabaseClient = {
  rpc: (name, params) => {
    rpcCalls.push({ name, params });
    if (name === 'amend_submission_score') {
      return Promise.resolve({ data: { ok: true, old_score: 60, new_score: params.p_score }, error: null });
    }
    return Promise.resolve({ data: { ok: true }, error: null });
  },
};
const document = { createElement: makeEl, getElementById: () => null };
const noop = () => {};
const factory = new Function(
  'document', 'supabaseClient', 'formatReviewedAt', 'getSubmissionChain',
  'showSaveIndicator', 'wireFeedbackAutosave', 'wireCommitActions', 'wireRevisionAction', 'escapeHtml',
  src + '\nreturn buildFeedbackSection;'
);
const buildFeedbackSection = factory(
  document, supabaseClient,
  () => 'Reviewed on 1 Jan', async () => [], noop, noop, noop, noop, x => x
);

// ── TEST (a): Foundations pending review — no score input, not gated ─────────
console.log('\n── TEST (a): Foundations pending — no score input, commit not gated ──');
rpcCalls = [];
const fWrap = buildFeedbackSection(
  { review_status: 'submitted', facilitator_feedback: 'ok' },
  'sub-F', 'Pat', 'Foundations Manual', 1
);
check('(a) no #scoreInputBox rendered', byId(fWrap, 'scoreInputBox').length, 0);
check('(a) no .score-input-box rendered', byClass(fWrap, 'score-input-box').length, 0);
const fPrimary = byId(fWrap, 'commitPrimaryBtn')[0];
check('(a) commit button exists', !!fPrimary, true);
check('(a) commit button NOT score-gated (enabled)', fPrimary.disabled, false);

// Control: a non-Foundations pending review DOES render + gate the input.
const nWrap = buildFeedbackSection(
  { review_status: 'submitted', facilitator_feedback: 'ok' },
  'sub-N', 'Pat', 'Lens 5', 3
);
check('(control) non-Foundations renders #scoreInputBox', byId(nWrap, 'scoreInputBox').length, 1);
check('(control) non-Foundations commit gated (disabled, empty score)',
      byId(nWrap, 'commitPrimaryBtn')[0].disabled, true);

// ── TEST commitReview extraction: Foundations forces p_score null ────────────
console.log('\n── TEST: commitReview p_score (verbatim extraction) ──');
function extractPScore(currentUnit, inputVal) {
  const _currentReviewUnit = currentUnit;
  const doc = { getElementById: id => id === 'scoreInputBox' ? { value: inputVal } : null };
  // VERBATIM from commitReview:
  let pScore = null;
  if (_currentReviewUnit !== 1) {
    const scoreEl = doc.getElementById('scoreInputBox');
    if (scoreEl && /^\d+$/.test(scoreEl.value.trim())) {
      const sv = Number(scoreEl.value.trim());
      if (sv >= 0 && sv <= 100) pScore = sv;
    }
  }
  return pScore;
}
check('Foundations(unit1) -> p_score null even if stray input present', extractPScore(1, '77'), null);
check('unit3 + "70" -> p_score 70', extractPScore(3, '70'), 70);
check('unit3 + "" -> p_score null', extractPScore(3, ''), null);

// ── TEST (b): non-Foundations reviewed — Edit score saves + updates display ──
console.log('\n── TEST (b): reviewed non-Foundations — edit score round-trip ──');
rpcCalls = [];
const rWrap = buildFeedbackSection(
  { review_status: 'reviewed', facilitator_feedback: 'good', score: 60, reviewed_at: '2026-01-01' },
  'sub-2', 'Pat', 'Lens 5', 3
);
const editBtn = byText(rWrap, 'Edit score')[0];
check('(b) "Edit score" button present', !!editBtn, true);
const committed = byClass(rWrap, 'committed-score')[0];
check('(b) committed score initially shows 60', committed.textContent, 'Score: 60 / 100');

// reveal editor (real click), then change value and Save (real async handler)
editBtn.dispatch('click');
const editInput = byClass(rWrap, 'score-edit-input')[0];
check('(b) editor prefilled with current score', editInput.value, '60');
editInput.value = '85';
const saveBtn = byText(rWrap, 'Save')[0];
// saveBtn has [stopProp, asyncSave] handlers; invoke the async one and await it.
await saveBtn._h.click[saveBtn._h.click.length - 1]({ stopPropagation() {} });
check('(b) amend_submission_score called once', rpcCalls.length, 1);
check('(b) rpc name + payload', [rpcCalls[0].name, rpcCalls[0].params],
      ['amend_submission_score', { p_submission_id: 'sub-2', p_score: 85 }]);
check('(b) displayed score updated in place (no reload)', committed.textContent, 'Score: 85 / 100');
const editor = byClass(rWrap, 'score-edit-editor')[0];
check('(b) editor hidden after save', editor.style.display, 'none');

// Foundations reviewed shows NO edit control.
const fr = buildFeedbackSection(
  { review_status: 'reviewed', facilitator_feedback: 'good', score: null, reviewed_at: '2026-01-01' },
  'sub-FR', 'Pat', 'Foundations', 1
);
check('(b) Foundations reviewed has NO Edit score button', byText(fr, 'Edit score').length, 0);

// ── TEST (c): invalid edit values rejected client-side (no rpc) ──────────────
console.log('\n── TEST (c): invalid edit values rejected client-side ──');
for (const bad of ['', '101', '-1', '3.5']) {
  const w = buildFeedbackSection(
    { review_status: 'reviewed', facilitator_feedback: 'g', score: 50, reviewed_at: '2026-01-01' },
    'sub-c', 'Pat', 'Lens 6', 3
  );
  byText(w, 'Edit score')[0].dispatch('click');
  const inp = byClass(w, 'score-edit-input')[0];
  inp.value = bad;
  rpcCalls = [];
  const sBtn = byText(w, 'Save')[0];
  await sBtn._h.click[sBtn._h.click.length - 1]({ stopPropagation() {} });
  const errEl = byClass(w, 'score-edit-error')[0];
  check("(c) '" + bad + "' -> no rpc + error shown",
        [rpcCalls.length, errEl._classes.has('shown'), byClass(w, 'committed-score')[0].textContent],
        [0, true, 'Score: 50 / 100']);
}

console.log('\n──────────────────────────────────────────────');
console.log('TOTAL: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
