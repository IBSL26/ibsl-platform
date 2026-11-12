#!/usr/bin/env node
'use strict';
/*
 * build_collection.js — Workstream 3 Phase 1 (printable portfolio builder)
 *
 * Re-runnable. Generates collection.html (repo root) from:
 *   - dashboard_F.html : the response-rendering JS pipeline + its report CSS (ported verbatim,
 *                        with ONE documented deviation — lensId threaded through renderValue).
 *   - the 12 participant files : Micro-Climb `var SUMMARY=[...]` arrays + per-key question prompts.
 *
 * collection.html itself fetches lens_catalog / submissions / profiles at RUNTIME in the
 * facilitator's authenticated Supabase session. Nothing here touches the DB.
 *
 * Usage:  node build_collection.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const OUT  = path.join(ROOT, 'collection.html');

// lens_id -> participant file. (chapter ORDER + TITLES come from lens_catalog at runtime.)
const LENS_FILES = {
  u1_foundations: 'unit1_P.html',
  u2m1_lens1:     'unit2_m1_lens1_p.html',
  u2m1_lens2:     'unit2_m1_lens2_p.html',
  u2m1_lens3:     'unit2_m1_lens3_p.html',
  u3m1_lens4:     'unit3_m1_lens4_p.html',
  u3m1_lens5:     'unit3_m1_lens5_p.html',
  u3m1_lens6:     'unit3_m1_lens6_p.html',
  u3m2_lens7:     'unit3_m2_lens7_p.html',
  u3m2_lens8:     'unit3_m2_lens8_p.html',
  u4m1_lens9:     'unit4_m1_lens9_p.html',
  u4m1_lens10:    'unit4_m1_lens10_p.html',
  u4m2_lens11:    'unit4_m2_lens11_p.html'
};

const SB_URL  = 'https://tayrxqbrttlrdowrzobm.supabase.co';
const SB_ANON = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRheXJ4cWJydHRscmRvd3J6b2JtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY3ODAyOTUsImV4cCI6MjA5MjM1NjI5NX0.8eaQauK1GPI3OXyHLdRAfbSwLfaYLB3_amHt6FhZxG0';

let FAIL = false;
const REPORT = [];
function note(m){ REPORT.push(m); }
function assert(cond, msg){ if(!cond){ FAIL = true; console.error('ASSERT FAIL: ' + msg); throw new Error(msg); } }
function read(f){ return fs.readFileSync(path.join(ROOT, f), 'utf8'); }
function lineOf(src, marker){ const i = src.indexOf(marker); return i < 0 ? -1 : src.slice(0, i).split('\n').length; }

// ── 1. Extract the JS pipeline from dashboard_F.html by function-name boundaries ──
function sliceBetween(src, startMarker, endMarker, label){
  const a = src.indexOf(startMarker);
  assert(a >= 0, 'pipeline start marker not found (' + label + '): ' + startMarker);
  const b = src.indexOf(endMarker, a + startMarker.length);
  assert(b > a, 'pipeline end marker not found (' + label + '): ' + endMarker);
  return src.slice(a, b);
}
// Deviation already applied upstream in dashboard_F.html -> accept it as-is instead of failing.
function replaceOnceOrApplied(s, find, repl, label){
  if (s.split(find).length - 1 === 0 && s.split(repl).length - 1 === 1) { note('Already upstream: ' + label); return s; }
  return replaceOnce(s, find, repl, label);
}
function replaceOnce(s, find, repl, label){
  const n = s.split(find).length - 1;
  assert(n === 1, 'expected exactly 1 occurrence of [' + label + '] in span, found ' + n);
  return s.split(find).join(repl);
}

const dash = read('dashboard_F.html');

// Span A: formatSubmittedAt + RESPONSE_OVERRIDES (stops before buildCompletionBar — SKIPPED per spec).
// Span B: renderResponses ... renderFiveCommitmentsPanel (stops before renderReviewAccessDenied).
// statusPillData (before A) and buildCompletionBar (between A and B) are excluded per spec.
const A_START = 'function formatSubmittedAt(iso) {';
const A_END   = 'function buildCompletionBar(payload, lens) {';
const B_START = 'function renderResponses(payload, lensId) {';
const B_END   = 'function renderReviewAccessDenied(';

let spanA = sliceBetween(dash, A_START, A_END, 'spanA');
let spanB = sliceBetween(dash, B_START, B_END, 'spanB');

const SRC = {
  spanA: [lineOf(dash, A_START), lineOf(dash, A_END) - 1],
  spanB: [lineOf(dash, B_START), lineOf(dash, B_END) - 1]
};

// Sanity: the kept functions must be present; the skipped ones must NOT be in the spans.
['function renderResponses', 'function renderGenericResponses', 'function renderAssessmentCard',
 'function fieldHasContent', 'function renderFieldEntry', 'function renderValue',
 'function humanizeFieldName', 'function detectFiveCommitments', 'function renderFiveCommitmentsPanel'
].forEach(function(fn){ assert(spanB.indexOf(fn) >= 0, 'expected ported function missing from spanB: ' + fn); });
assert(spanA.indexOf('function formatSubmittedAt') >= 0, 'formatSubmittedAt missing from spanA');
assert(spanA.indexOf('RESPONSE_OVERRIDES') >= 0, 'RESPONSE_OVERRIDES missing from spanA');
assert(spanA.indexOf('function buildCompletionBar') < 0 && spanB.indexOf('function buildCompletionBar') < 0, 'buildCompletionBar leaked into a span (should be skipped)');
assert(spanA.indexOf('function statusPillData') < 0 && spanB.indexOf('function statusPillData') < 0, 'statusPillData leaked into a span (should be skipped)');
assert(spanB.indexOf('function renderReviewAccessDenied') < 0, 'renderReviewAccessDenied leaked into spanB');

// ── 1b. The ONE documented deviation: thread lensId through renderValue (prevents ReferenceError;
//        behaviour-identical for all real nested data). Plus the prompt-primary label hook. ──
spanB = replaceOnceOrApplied(spanB, 'function renderValue(value, depth) {', 'function renderValue(value, depth, lensId) {', 'renderValue signature');
spanB = replaceOnceOrApplied(spanB, 'const valueEl = renderValue(value, depth);', 'const valueEl = renderValue(value, depth, lensId);', 'renderFieldEntry->renderValue');
spanB = replaceOnceOrApplied(spanB, 'li.appendChild(renderValue(item, depth + 1));', 'li.appendChild(renderValue(item, depth + 1, lensId));', 'array-item renderValue');
spanB = replaceOnceOrApplied(spanB, 'body.appendChild(renderValue(val, 0));', 'body.appendChild(renderValue(val, 0, lensId));', 'sip_data renderValue');
// prompt-primary hook: renderFieldEntry uses labelFor() (defined in collection.html) which prefers an
// extracted question prompt and falls back to the verbatim humanizeFieldName.
spanB = replaceOnceOrApplied(spanB, 'label.textContent = humanizeFieldName(fieldName, lensId);', 'label.textContent = labelFor(fieldName, lensId);', 'labelFor hook');

const PIPELINE = '  // ── Ported verbatim from dashboard_F.html lines ' + SRC.spanA[0] + '-' + SRC.spanA[1] +
  ' and ' + SRC.spanB[0] + '-' + SRC.spanB[1] + ' (build_collection.js).\n' +
  '  // Deviations: lensId threaded through renderValue; renderFieldEntry label via labelFor() hook.\n' +
  spanA + '\n' + spanB;

note('Pipeline ported: spanA lines ' + SRC.spanA.join('-') + ', spanB lines ' + SRC.spanB.join('-') + '.');

// ── 2. Extract CSS rules by selector prefix (brace-balanced; handles @media blocks whole) ──
function styleBlocks(html){
  const out = [];
  const re = /<style[^>]*>([\s\S]*?)<\/style>/gi;
  let m; while ((m = re.exec(html)) !== null) out.push(m[1]);
  return out.join('\n');
}
function topLevelRules(css){
  css = css.replace(/\/\*[\s\S]*?\*\//g, ''); // strip comments
  const rules = []; let i = 0; const n = css.length;
  while (i < n){
    while (i < n && /\s/.test(css[i])) i++;
    if (i >= n) break;
    const start = i;
    while (i < n && css[i] !== '{') i++;
    if (i >= n) break;
    const sel = css.slice(start, i).trim();
    let depth = 0;
    do { if (css[i] === '{') depth++; else if (css[i] === '}') depth--; i++; } while (i < n && depth > 0);
    rules.push({ sel: sel, block: css.slice(start, i).trim() });
  }
  return rules;
}
function extractCss(html, prefixes, label){
  const rules = topLevelRules(styleBlocks(html));
  const re = new RegExp('(^|[^a-z0-9_-])(' + prefixes.map(function(p){ return p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|') + ')', 'i');
  const kept = rules.filter(function(r){ return re.test(r.sel) || (/^@/.test(r.sel) && re.test(r.block)); });
  note(label + ': kept ' + kept.length + ' CSS rules of ' + rules.length + ' scanned.');
  assert(kept.length >= 8, label + ' captured too few CSS rules (' + kept.length + ') — extraction likely broken.');
  return kept.map(function(r){ return r.block; }).join('\n');
}

const REPORT_CSS = extractCss(dash, ['.review-completion', '.response-', '.assessment-', '.fc-', '.access-denied', '.error-card'], 'report CSS');

// ── 3. Per-participant extraction: Micro-Climb SUMMARY + question prompts ──
function extractSummary(html, lensId){
  const a = html.indexOf('var SUMMARY=[');
  if (a < 0){ note('Micro-Climb: ' + lensId + ' → none (no SUMMARY array).'); return null; }
  let i = html.indexOf('[', a); let depth = 0; const start = i;
  for (; i < html.length; i++){ if (html[i] === '[') depth++; else if (html[i] === ']'){ depth--; if (depth === 0){ i++; break; } } }
  const arrText = html.slice(start, i);
  let arr;
  try { arr = (new Function('return (' + arrText + ');'))(); }
  catch (e){ note('Micro-Climb: ' + lensId + ' → PARSE FAILED (' + e.message + ').'); return null; }
  assert(Array.isArray(arr), 'SUMMARY for ' + lensId + ' did not eval to an array');
  note('Micro-Climb: ' + lensId + ' → ' + arr.length + ' arc segments.');
  return arr;
}

function stripTags(s){
  return s.replace(/<[^>]*>/g, ' ')
          .replace(/&mdash;/g, '—').replace(/&ndash;/g, '–').replace(/&amp;/g, '&')
          .replace(/&rsquo;/g, '’').replace(/&lsquo;/g, '‘').replace(/&hellip;/g, '…')
          .replace(/&nbsp;/g, ' ').replace(/&rarr;/g, '→').replace(/&#39;/g, '’').replace(/&#x270E;|✎/gi, '').replace(/&#?[a-z0-9]+;/gi, ' ')
          .replace(/\s+/g, ' ').trim();
}
// Heuristic: for each persisted key, find the nearest preceding question/label text.
function extractPrompts(html, lensId){
  const prompts = {}; const keys = {};
  let m;
  const idRe = /<(?:textarea|input|select)\b[^>]*\bid="([a-z0-9_]+)"/gi;
  while ((m = idRe.exec(html)) !== null) keys[m[1]] = (keys[m[1]] === undefined ? m.index : keys[m[1]]);
  const dkRe = /\bdata-key="([a-z0-9_]+)"/gi;
  while ((m = dkRe.exec(html)) !== null) if (keys[m[1]] === undefined) keys[m[1]] = m.index;

  const labelRe = /<(?:div|p|label|span|h[2-6])\b[^>]*class="[^"]*(?:ref-label|score-notes-lbl|field-label|prompt|q-label|reflection-prompt|port-desc|u12-q)[^"]*"[^>]*>([\s\S]*?)<\/(?:div|p|label|span|h[2-6])>/gi;
  const forRe = function(key){ return new RegExp('<label\\b[^>]*\\bfor="' + key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '"[^>]*>([\\s\\S]*?)<\\/label>', 'i'); };

  let found = 0; const missed = [];
  Object.keys(keys).forEach(function(key){
    const pos = keys[key];
    // 1) explicit <label for="key">
    let fm = forRe(key).exec(html);
    if (fm){ const t = stripTags(fm[1]); if (t){ prompts[key] = t; found++; return; } }
    // 1b) table row: <td>Question</td><td><textarea id="key"> — use the question cell
    { const rowWin = html.slice(Math.max(0, pos - 800), pos);
      const tm = /<td\b[^>]*>([^<]{5,300})<\/td>\s*<td\b[^>]*>\s*$/i.exec(rowWin);
      if (tm){ const t = stripTags(tm[1]); if (t){ prompts[key] = t; found++; return; } } }
    // 2) nearest preceding label-ish element within a 2500-char window
    const winStart = Math.max(0, pos - 2500);
    const window = html.slice(winStart, pos);
    let best = null, lm;
    labelRe.lastIndex = 0;
    while ((lm = labelRe.exec(window)) !== null) best = lm[1];
    if (best){ const t = stripTags(best).replace(/^Reflection\s*[–—-]\s*/i, ''); if (t){ prompts[key] = t; found++; return; } }
    missed.push(key);
  });
  note('Prompts: ' + lensId + ' → ' + found + ' extracted, ' + missed.length + ' fell back to humanizeFieldName' +
       (missed.length ? ' [' + missed.join(', ') + ']' : '') + '.');
  return prompts;
}

// Units 10 and 11 have no Unit Summary on their pages (removed 27 Oct); the Learning Portfolio carries these.
const PORTFOLIO_SUMMARY = {
  u4m1_lens9: [
    {arc:"Awareness — What",title:"What Was Established",body:"Every strategic commitment places specific demands on the organisation’s operating conditions. ESRG names those conditions: Environment (FIT), Systems (SIP), Resources (AIR) and Governance (PAR). You specified what each component must provide for one commitment to be delivered, and you learnt when to use ESRG Alignment and when to use Strategic Unclogging."},
    {arc:"Intelligence — Why",title:"Why It Matters",body:"The ESRG Ignition Point is reached when operating conditions can meet the performance demands of the strategy. Each domain enables execution through one capability: Operational Readiness, Operational Flow, Delivery Capacity and Decision Responsiveness. A functional ESRG profile shows where conditions enable a commitment and where they constrain it."},
    {arc:"Extrapolating — Where",title:"Where Bias Distorts Capability",body:"Executive decisions shape operating conditions through the priorities and assumptions of each portfolio. The CXO ESRG Bias Contributors show the approval, investment, sourcing or design choice where a bias enters, the ESRG component it weakens and the debiasing action that protects it."},
    {arc:"Integration — Collective",title:"What Was Built",body:"Functional assessments become collective intelligence through three dimensions: Convergence shows what functions have in common and calls for Coordinate; Divergence shows where they differ and calls for Reconcile; Dependency shows how they rely on one another and calls for Align. You completed your function’s annual ESRG baseline."},
    {arc:"Application — In Practice",title:"What You Applied",body:"In the Enterprise ESRG Alignment Clinic your group consolidated every member’s baseline into the Enterprise Scanner, interpreted it by capability, agreed its Collective Intelligence Responses and completed an ESRG Alignment Intervention Plan for each. The response determines what must change; the plan establishes how the executive team will make that change happen."}
  ],
  u4m1_lens10: [
    {arc:"Awareness — What",title:"What Was Established",body:"Values set the principles that guide behaviour. Culture is how those principles become established ways of working, expressed through the Cultural Operating Code. Organisational health reveals how effectively values are lived, and it shows in the Five Observable Health Traits and the Organisational Health Pyramid."},
    {arc:"Intelligence — Why",title:"Why It Matters",body:"Organisational health multiplies strategy execution capability and determines execution velocity. When health deteriorates, execution friction increases, performance systems lose effectiveness and the cost of delivering strategy rises. That cost can be quantified, which directs leadership attention to its performance implications."},
    {arc:"Extrapolating — Where",title:"Where the Signals Show",body:"The Organisational Health Thermometer reads each of the Five Observable Health Traits as strong, vulnerable or poor, using observable employee behaviour and supporting evidence. A credible assessment also requires awareness of functional bias and personal accountability for the behaviours leaders reinforce."},
    {arc:"Integration — Collective",title:"What Was Built",body:"The Cross-CXO Health Architecture connects functional accountability with collective responsibility. Employees complete the Thermometer independently; each CXO interprets the consolidated score, investigates vulnerabilities and quantifies people-performance losses; and the executive team addresses what affects the enterprise on a quarterly rhythm."},
    {arc:"Application — In Practice",title:"What You Applied",body:"In the Cross-CXO Organisational Health Clinic your group interpreted functional assessments, consolidated scores and losses into an enterprise position, determined remedial actions through Review–Realign–Restore and built its own Cultural Operating Code. Health improves when the executive team reads it from evidence, prices what poor health costs, acts with named accountability and models its norms."}
  ]
};
function decodeSummaryText(s){
  return String(s == null ? '' : s).replace(/&mdash;/g, '—').replace(/&ndash;/g, '–').replace(/&rsquo;/g, '’').replace(/&lsquo;/g, '‘')
    .replace(/&ldquo;/g, '“').replace(/&rdquo;/g, '”').replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ').replace(/&middot;/g, '·');
}
const MICRO_CLIMB = {};
const PROMPTS = {};
Object.keys(LENS_FILES).forEach(function(lensId){
  const f = LENS_FILES[lensId];
  assert(fs.existsSync(path.join(ROOT, f)), 'participant file missing: ' + f);
  const html = read(f);
  const summary = extractSummary(html, lensId) || PORTFOLIO_SUMMARY[lensId] || null;
  MICRO_CLIMB[lensId] = summary && summary.map(function(b){ return Object.assign({}, b, { arc: decodeSummaryText(b.arc), title: decodeSummaryText(b.title || b.t), body: decodeSummaryText(b.body) }); });
  PROMPTS[lensId] = extractPrompts(html, lensId);
});

// Sum-* (Micro-Climb) CSS — shared across migrated participant files; pull from lens5.
const SUM_CSS = extractCss(read(LENS_FILES.u3m1_lens5), ['.sum-block', '.sum-h', '.sum-arc', '.sum-title', '.sum-body', '.sum-arr'], 'Micro-Climb CSS');

// ── 4. Assemble collection.html ──
const BUILD_INFO = { generated: new Date().toISOString(), pipelineSrc: SRC, lensCount: Object.keys(LENS_FILES).length };

function injectAll(s, token, value){ return s.split(token).join(value); }
const TEMPLATE = buildTemplate();
let html = TEMPLATE;
html = injectAll(html, '%%REPORT_CSS%%', REPORT_CSS);
html = injectAll(html, '%%SUM_CSS%%', SUM_CSS);
html = injectAll(html, '%%PIPELINE%%', PIPELINE);
html = injectAll(html, '%%MICRO_CLIMB%%', JSON.stringify(MICRO_CLIMB));
html = injectAll(html, '%%PROMPTS%%', JSON.stringify(PROMPTS));
html = injectAll(html, '%%BUILD_INFO%%', JSON.stringify(BUILD_INFO));
html = injectAll(html, '%%SB_URL%%', SB_URL);
html = injectAll(html, '%%SB_ANON%%', SB_ANON);

assert(html.indexOf('%%') < 0, 'unreplaced %%placeholder%% remains in output');
fs.writeFileSync(OUT, html, 'utf8');

console.log('\n=== build_collection.js report ===');
REPORT.forEach(function(r){ console.log(' - ' + r); });
console.log('Wrote ' + OUT + ' (' + html.length + ' bytes).');
if (FAIL) process.exitCode = 1;

// ── collection.html template (static skeleton; %% tokens injected above) ──
function buildTemplate(){
  return [
'<!DOCTYPE html>',
'<html lang="en">',
'<head>',
'<meta charset="utf-8">',
'<meta name="viewport" content="width=device-width, initial-scale=1">',
'<title>Learning Portfolio · IBSL</title>',
'<!-- Generated by build_collection.js — DO NOT edit by hand; re-run the builder. Build: %%BUILD_INFO%% -->',
'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">',
'<style>',
':root{--gold:#c9a84c;--teal:#1a7a6a;--forest:#1a3a2a;--ink:#0d1816;}',
'@page{size:A4;margin:16mm 14mm;}',
'*{box-sizing:border-box;}',
'html,body{margin:0;padding:0;background:#101a16;color:#1c1c1c;font-family:"Montserrat",sans-serif;}',
'.sheet{background:#fff;color:#1c1c1c;max-width:820px;margin:0 auto;}',
'.chapter{break-before:page;page-break-before:always;padding:40px 54px 60px;}',
'.chapter:first-of-type{break-before:auto;page-break-before:auto;}',
'.cover{break-after:page;page-break-after:always;min-height:90vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px;background:linear-gradient(160deg,#0d1f15,#1a3a2a 60%,#0f2419);color:#fff;}',
'.cover .wordmark{font-size:11px;letter-spacing:6px;text-transform:uppercase;color:var(--gold);margin-bottom:26px;}',
'.cover h1{font-family:"Cormorant Garamond",serif;font-weight:300;font-size:3rem;margin:0 0 8px;}',
'.cover .who{font-size:1.05rem;color:rgba(255,255,255,.85);margin-top:18px;}',
'.cover .meta{font-size:12px;letter-spacing:1px;color:rgba(255,255,255,.55);margin-top:6px;}',
'.cover .brand{margin-top:40px;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.4);}',
'.toc{break-after:page;page-break-after:always;padding:48px 54px;}',
'.toc h2{font-family:"Cormorant Garamond",serif;font-weight:400;font-size:1.8rem;color:var(--forest);border-bottom:2px solid var(--gold);padding-bottom:10px;margin:0 0 20px;}',
'.toc ol{list-style:none;counter-reset:toc;padding:0;margin:0;}',
'.toc li{counter-increment:toc;padding:9px 0;border-bottom:1px solid #eee;font-size:14px;}',
'.toc li a{color:#1c1c1c;text-decoration:none;}',
'.toc li::before{content:counter(toc) ".";color:var(--gold);font-weight:700;margin-right:12px;}',
'.chapter-head{border-bottom:2px solid var(--gold);padding-bottom:12px;margin-bottom:22px;}',
'.chapter-head h2{font-family:"Cormorant Garamond",serif;font-weight:400;font-size:1.9rem;color:var(--forest);margin:0;}',
'.chapter-head .sub{font-size:11px;letter-spacing:1px;color:#888;margin-top:6px;}',
'.chapter-head .lens-score{font-family:"Cormorant Garamond",serif;font-size:22px;font-weight:700;color:var(--forest);margin-top:4px;margin-bottom:2px;letter-spacing:0.5px;}',
'.not-submitted{color:#999;font-style:italic;padding:18px 0;}',
'.section-label{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin:26px 0 10px;}',
'.feedback-block{margin-top:24px;border-left:3px solid var(--teal);background:#f3f8f6;padding:16px 18px;border-radius:0 4px 4px 0;}',
'.feedback-block .fb-text{font-size:13px;line-height:1.7;color:#28413a;white-space:pre-wrap;}',
'.fatal{max-width:560px;margin:80px auto;background:#fff;border:1px solid #e0c9c9;border-radius:8px;padding:40px;text-align:center;}',
'.fatal h2{font-family:"Cormorant Garamond",serif;font-weight:400;color:#8a2a2a;}',
'.print-bar{position:fixed;top:14px;right:14px;z-index:50;}',
'.print-bar button{background:var(--gold);color:#1c1c1c;border:none;font-family:Montserrat,sans-serif;font-weight:700;font-size:11px;letter-spacing:1px;text-transform:uppercase;padding:10px 18px;border-radius:3px;cursor:pointer;}',
'/* ── Ported report CSS (dashboard_F.html) ── */',
'%%REPORT_CSS%%',
'/* ── Ported Micro-Climb CSS (participant files) ── */',
'%%SUM_CSS%%',
'/* dark report classes sit on a white sheet — recolour text for print legibility */',
'.sheet .response-text,.sheet .response-label,.sheet .response-module-heading,.sheet .sum-title,.sheet .sum-body p,.sheet .sum-arc{color:#1c1c1c;}',
'.sheet .response-module-heading{background:#f4f1e8;}',
'.sheet .sum-block{border:1px solid #e6e1d2;}',
'@media print{',
'  .sheet .response-text{background:#faf8f1;}',
'  .sum-block,.response-label{break-inside:avoid;}',
'  .response-label,.response-module-heading,.section-label{break-after:avoid;}',
'  html,body{background:#fff;}',
'  .print-bar{display:none!important;}',
'  /* force every collapsible fully open on paper */',
'  .response-module.collapsed .response-module-body,.response-field-collapsible.collapsed>*{display:block!important;}',
'  .response-module.collapsed .response-module-heading::after{content:""!important;}',
'  .sum-block .sum-body{display:block!important;}',
'  .response-toolbar,.response-expand-all{display:none!important;}',
'}',
'/* ── IBSL portfolio design (12 Nov 2026): brand layout for screen and print ── */',
':root{--ibsl-green:#1A5C2C;--ibsl-deep:#12401F;--ibsl-gold:#C6A24C;--ibsl-cream:#FAF6EA;--ibsl-line:#E4DCC4;--ibsl-ink:#1F2A24;}',
'@page{size:A4;margin:18mm 16mm 20mm;@bottom-left{content:"Institute of Behavioural Strategy & Leadership  \\00B7  Learning Portfolio";font-family:Montserrat,sans-serif;font-size:7.5pt;color:#6b6b6b;}@bottom-right{content:"Page " counter(page);font-family:Montserrat,sans-serif;font-size:7.5pt;font-weight:600;color:#1A5C2C;}}',
'@page :first{margin:0;@bottom-left{content:none;}@bottom-right{content:none;}}',
'.sheet{font-family:"Montserrat",sans-serif;color:var(--ibsl-ink);}',
'/* cover */',
'.cover{position:relative;min-height:297mm;padding:0;background:var(--ibsl-cream);color:var(--ibsl-ink);justify-content:flex-start;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.cover .cv-band{width:100%;height:16mm;background:var(--ibsl-green);border-bottom:2.5mm solid var(--ibsl-gold);}',
'.cover .cv-logo{width:42mm;height:auto;margin:62mm 0 12mm;}',
'.cover .wordmark{font-size:10px;font-weight:700;letter-spacing:5px;color:var(--ibsl-gold);margin:0 0 14px;}',
'.cover h1{font-family:"Cormorant Garamond",serif;font-weight:600;font-size:3.6rem;line-height:1.05;color:var(--ibsl-green);margin:0;}',
'.cover .cv-rule{width:70mm;height:0;border-top:1.5px solid var(--ibsl-gold);margin:16px auto 22px;}',
'.cover .who{font-size:1.35rem;font-weight:700;color:var(--ibsl-ink);margin:0;}',
'.cover .meta{font-size:11px;letter-spacing:.5px;color:#5b5b5b;margin-top:8px;}',
'.cover .brand{position:absolute;left:0;right:0;bottom:0;margin:0;padding:9mm 0;background:var(--ibsl-green);border-top:2.5mm solid var(--ibsl-gold);font-size:9.5px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:#fff;}',
'/* contents */',
'.toc{padding:40px 54px;}',
'.toc h2{font-family:"Montserrat",sans-serif;font-weight:700;font-size:1.5rem;letter-spacing:.5px;color:var(--ibsl-green);border-bottom:3px solid var(--ibsl-gold);padding-bottom:10px;margin:0 0 18px;}',
'.toc li{display:flex;align-items:center;padding:11px 0;border-bottom:1px solid var(--ibsl-line);font-size:13.5px;font-weight:500;}',
'.toc li::before{content:counter(toc);display:inline-flex;align-items:center;justify-content:center;flex:0 0 26px;height:26px;border-radius:50%;background:var(--ibsl-green);color:#fff;font-size:11px;font-weight:700;margin-right:14px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.toc li a{color:var(--ibsl-ink);}',
'/* chapter */',
'.chapter{padding:40px 54px 50px;}',
'.chapter-head{border:0;padding:18px 22px 16px;margin:0 0 26px;background:var(--ibsl-green);border-bottom:4px solid var(--ibsl-gold);border-radius:3px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.chapter-head .ch-kicker{font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--ibsl-gold);margin-bottom:4px;}',
'.chapter-head h2{font-family:"Cormorant Garamond",serif;font-weight:600;font-size:2rem;line-height:1.15;color:#fff;}',
'.chapter-head .ch-meta{display:flex;align-items:center;gap:12px;margin-top:10px;}',
'.chapter-head .sub{font-size:10.5px;letter-spacing:.5px;color:rgba(255,255,255,.85);margin:0;}',
'.chapter-head .lens-score{display:inline-block;font-family:"Montserrat",sans-serif;font-size:11px;font-weight:700;letter-spacing:1px;color:var(--ibsl-deep);background:var(--ibsl-gold);padding:4px 10px;border-radius:12px;margin:0;}',
'.section-label{display:block;font-size:12px;font-weight:700;letter-spacing:2.5px;color:var(--ibsl-green);margin:30px 0 14px;padding-bottom:6px;border-bottom:2px solid var(--ibsl-gold);}',
'.chapter>.section-label:first-of-type{margin-top:0;}',
'.not-submitted{color:#8a8a8a;}',
'/* reflections */',
'.sheet .response-module-heading{background:var(--ibsl-cream);color:var(--ibsl-green);border:1px solid var(--ibsl-line);border-left:4px solid var(--ibsl-green);font-size:11px;}',
'.sheet .response-field{margin-bottom:20px;}',
'.sheet .response-label{display:block;color:var(--ibsl-deep);font-size:13px;font-weight:700;letter-spacing:0;line-height:1.5;margin-bottom:8px;}',
'.sheet .response-label .rf-tag{display:inline-block;font-size:9px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;background:var(--ibsl-green);padding:3px 8px;border-radius:2px;margin:0 0 6px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.sheet .response-label .rf-tag b{color:var(--ibsl-gold);font-weight:700;}',
'.sheet .response-label .rf-q{display:block;}',
'.sheet .response-text{color:var(--ibsl-ink);background:var(--ibsl-cream);border-left:3px solid var(--ibsl-gold);font-size:12.5px;line-height:1.7;padding:12px 16px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'/* unit summary */',
'.sheet .sum-block{border:1px solid var(--ibsl-line);border-radius:3px;margin:0 0 12px;}',
'.sheet .sum-h{background:var(--ibsl-cream);border-bottom:1px solid var(--ibsl-line);padding:10px 16px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.sheet .sum-arc{width:auto;flex:0 0 auto;color:#fff;background:var(--ibsl-green);font-size:8.5px;letter-spacing:1.5px;padding:4px 8px;border-radius:2px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.sheet .sum-title{font-family:"Montserrat",sans-serif;font-size:13px;font-weight:700;color:var(--ibsl-green);}',
'.sheet .sum-arr{display:none;}',
'.sheet .sum-body{padding:12px 16px 4px;}',
'.sheet .sum-body p{font-size:12px;line-height:1.75;color:var(--ibsl-ink);margin:0 0 8px;}',
'/* facilitator feedback */',
'.feedback-block{border-left:4px solid var(--ibsl-gold);background:var(--ibsl-cream);-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.feedback-block .fb-text{color:var(--ibsl-ink);font-size:12.5px;}',
'/* competency profile */',
'.cp-sec{background:#fff;color:var(--ibsl-ink);padding:40px 54px;margin:0 auto;max-width:820px;break-before:page;page-break-before:always;}',
'.cp-sec h2{font-family:"Montserrat",sans-serif;font-weight:700;font-size:1.5rem;color:var(--ibsl-green);border-bottom:3px solid var(--ibsl-gold);padding-bottom:10px;margin:0 0 6px;}',
'.cp-sec h3{font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--ibsl-green);margin:22px 0 8px;}',
'.cp-sec table{width:100%;border-collapse:collapse;font-size:11.5px;}',
'.cp-sec th{background:var(--ibsl-green);color:#fff;font-weight:700;text-align:left;padding:8px 10px;-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'.cp-sec td{padding:8px 10px;border-bottom:1px solid var(--ibsl-line);vertical-align:top;}',
'.cp-sec tr:nth-child(even) td{background:var(--ibsl-cream);-webkit-print-color-adjust:exact;print-color-adjust:exact;}',
'@media print{',
'  .sheet{max-width:none;}',
'  .cover{min-height:0;height:297mm;}',
'  .chapter,.toc,.cp-sec{padding:0;}',
'  .sheet .response-text{background:var(--ibsl-cream);}',
'  .sheet .response-field{break-inside:avoid;}',
'  .chapter-head,.sum-h{break-after:avoid;}',
'  .cp-sec tr{break-inside:avoid;}',
'}',
'</style>',
'<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>',
'<script src="/s2r-protect.js" data-allow-print></script>',
'<script src="/s2r-key-reflections.js"></script>',
'<script src="/s2r-u1-sheet.js"></script>',
'</head>',
'<body>',
'<div class="print-bar"><button onclick="window.print()">Print / Save PDF</button></div>',
'<div id="root" class="sheet"><div class="not-submitted" style="padding:60px 54px;">Loading collection…</div></div>',
'<script>',
'(function(){',
'  "use strict";',
'  var SB_URL="%%SB_URL%%", SB_ANON="%%SB_ANON%%";',
'  if(typeof supabase==="undefined"){ document.getElementById("root").innerHTML="<div class=\\"fatal\\"><h2>Could not load</h2><p>The Supabase library failed to load. Check your connection and refresh.</p></div>"; return; }',
'  var supabaseClient=supabase.createClient(SB_URL,SB_ANON,{auth:{persistSession:true,autoRefreshToken:true,detectSessionInUrl:false}});',
'',
'  var MICRO_CLIMB=%%MICRO_CLIMB%%;',
'  var PROMPTS=%%PROMPTS%%;',
'  var BUILD_INFO=%%BUILD_INFO%%;',
'',
'  var qp=new URLSearchParams(location.search);',
'  var participantId=(qp.get("participantId")||"").trim();',
'  var feedbackOn=((qp.get("feedback")||"on").toLowerCase()!=="off");',
'  var ACCESSIBLE={unlocked:1,in_progress:1,submitted:1,reviewed:1,completed:1};',
'',
'  // ───────────────────────── ported rendering pipeline ─────────────────────────',
'%%PIPELINE%%',
'  // Group work that feeds the Capstone S2R® Blueprint is left out of the Learning Portfolio. It stays in the facilitator report (dashboard_F.html).',
'  var CAPSTONE_KEYS={ u1_foundations:/^(pc_|confirmed_items$)/i, u2m1_lens1:/^(arch_|org_name$|strategy_period$|intent_statement$|sip_d\\d_(q\\d|st)$|sip_integrated$|confirmed_items$)/i, u2m1_lens2:/^(kex_|kiss_(keep|improve|start|stop)$|sip_d\\d_st$|okr_drafts$|ent_priorities$|ent_okrs$|confirmed_items$)/i, u2m1_lens3:/^(mbt_(record|arena|bound|comp|value|verify|blind)$|syn_(themes|disagree|top5)$|own_(internal|external|timeline)$|team_name$|exec_(name|role)$|confirmed_items$)/i, u3m1_lens4:/^(syn_(missing_compass|strong_compass|sequence)$|kit_(team|mind|heart|hands|habit|profile)$|oceavl_scores$|team_name$|exec_(name|role)$|confirmed_items$)/i, u3m1_lens5:/^(pm_(record|scoring|faces|execution|scorecards)$|cm_(record|map|faces|ward)$|confirmed_items$)/i, u3m1_lens6:/^(ex_(record|future|delivery|chain|ownership|dialogue)$|confirmed_items$)/i, u3m2_lens7:/^(rd_(record|warning|accountability|learning|credibility|ward)$|confirmed_items$)/i, u3m2_lens8:/^(uc_(record|challenge|clog|lever|review_realign|restore)$|confirmed_items$)/i, u4m1_lens9:/^(es_(scanner|interp|resp|plan)$|confirmed_items$)/i, u4m1_lens10:/^(oh_(func|cons|rrr|resp|coc)$|confirmed_items$)/i, u4m2_lens11:/^(qs_(strategic|operational|behavioural|kiss)$|confirmed_items$)/i };',
'  function portfolioPayload(payload,lensId){ var rx=CAPSTONE_KEYS[lensId]; if(!rx||!payload||!payload.responses) return payload; var out={}; Object.keys(payload).forEach(function(k){ out[k]=payload[k]; }); var r={}; Object.keys(payload.responses).forEach(function(k){ if(!rx.test(k)) r[k]=payload.responses[k]; }); out.responses=r; return out; }',
'  // prompt-primary label hook (spec §: extracted question prompt, else verbatim humanizeFieldName)',
'  function labelFor(name,lensId){ var m=PROMPTS[lensId]||{}; var p=m[name]; if(!p){ Object.keys(m).some(function(k){ if(k.replace(/^r_m\\d+_/,"")===name){ p=m[k]; return true; } return false; }); } return (p&&String(p).trim())?p:humanizeFieldName(name,lensId); }',
'',
'  // ───────────────────────── helpers ─────────────────────────',
'  function el(tag,cls,txt){ var e=document.createElement(tag); if(cls)e.className=cls; if(txt!=null)e.textContent=txt; return e; }',
'  function fatal(title,msg){ document.getElementById("root").innerHTML=""; var w=el("div","fatal"); w.appendChild(el("h2",null,title)); w.appendChild(el("p",null,msg)); document.getElementById("root").appendChild(w); }',
'  function fmtDate(iso){ if(!iso) return null; var d=new Date(iso); if(isNaN(d)) return null; return d.toLocaleDateString("en-GB",{day:"numeric",month:"long",year:"numeric"}); }',
'',
'  function renderMicroClimb(arr){',
'    var wrap=el("div","micro-climb");',
'    arr.forEach(function(s){',
'      var b=el("div","sum-block open");',
'      var h=el("div","sum-h"); h.appendChild(el("span","sum-arc",s.arc||"")); h.appendChild(el("span","sum-title",s.title||s.t||"")); b.appendChild(h);',
'      var body=el("div","sum-body"); body.appendChild(el("p",null,s.body||"")); b.appendChild(body);',
'      wrap.appendChild(b);',
'    });',
'    return wrap;',
'  }',
'',
'  // Print layout: drop a lone "Reflections" heading under the label; split "Section N · Arc · Question" labels into a tag and the question.',
'  function styleResponses(node){',
'    try{',
'      var mods=node.querySelectorAll(".response-module");',
'      if(mods.length===1){ var hd=mods[0].querySelector(".response-module-heading"); if(hd && /^reflections$/i.test(hd.textContent.trim())){ hd.parentNode.removeChild(hd); mods[0].classList.remove("collapsed"); } }',
'      Array.prototype.forEach.call(node.querySelectorAll(".response-label"), function(lb){',
'        var m=/^\\s*(Section\\s+\\d+)\\s*\\u00b7\\s*([^\\u00b7]+?)\\s*\\u00b7\\s*([\\s\\S]+)$/.exec(lb.textContent||"");',
'        if(!m) return;',
'        lb.textContent="";',
'        var tag=el("span","rf-tag",m[1]+" \\u00b7 "); var arc=el("b",null,m[2]); tag.appendChild(arc);',
'        lb.appendChild(tag); lb.appendChild(el("span","rf-q",m[3]));',
'      });',
'    }catch(e){}',
'    return node;',
'  }',
'',
'  function chapterNode(cat, subs){',
'    var ch=el("div","chapter"); ch.id="ch-"+cat.id;',
'    var head=el("div","chapter-head");',
'    var seq=Number(cat.sequence);',
'    head.appendChild(el("div","ch-kicker","Unit "+(seq+1)));',
'    var h2=el("h2", null, seq===0 ? "Behavioural Strategy Fundamentals" : (cat.title||cat.id));',
'    head.appendChild(h2);',
'    var latest = subs && subs.length ? subs[0] : null;',
'    if(latest){',
'      var chMeta=el("div","ch-meta");',
'      var sub=el("div","sub"); var dt=fmtDate(latest.submitted_at);',
'      var subText = dt ? ("Submitted "+dt) : "";',
'      sub.textContent = subText;',
'      if(typeof latest.score==="number"){',
'        var scoreEl = el("div","lens-score","Score: "+latest.score+" / 100");',
'        chMeta.appendChild(scoreEl);',
'      }',
'      chMeta.appendChild(sub);',
'      head.appendChild(chMeta);',
'    }',
'    ch.appendChild(head);',
'',
'    if(!latest){',
'      ch.appendChild(el("div","not-submitted","Not yet submitted."));',
'    } else {',
'      var payload = portfolioPayload(latest.payload || {}, cat.id);',
'      ch.appendChild(el("div","section-label","Reflections"));',
'      ch.appendChild(styleResponses(renderResponses(payload, cat.id)));',
'      var fc = detectFiveCommitments(payload);',
'      if(fc) ch.appendChild(renderFiveCommitmentsPanel(fc));',
'    }',
'',
'    var mc = MICRO_CLIMB[cat.id];',
'    if(latest && mc && mc.length){ ch.appendChild(el("div","section-label","Unit Summary")); ch.appendChild(renderMicroClimb(mc)); }',
'',
'    // Unit 1 marking sheet, once the facilitator has selected Mark as reviewed.',
'    if(cat.id==="u1_foundations" && latest && String(latest.review_status||"")==="reviewed" && window.S2R_U1_SHEET){ var u1s=el("div"); ch.appendChild(u1s); window.S2R_U1_SHEET.render(supabaseClient, participantId, latest.cohort_id, u1s, { heading:"Marking Sheet", headingClass:"section-label", sub:false }); }',
'',
'    if(feedbackOn && latest && latest.facilitator_feedback && String(latest.facilitator_feedback).trim()){',
'      ch.appendChild(el("div","section-label","Facilitator Feedback"));',
'      var fb=el("div","feedback-block"); fb.appendChild(el("div","fb-text", String(latest.facilitator_feedback))); ch.appendChild(fb);',
'    }',
'    return ch;',
'  }',
'',
'  function buildCover(name, cohort){',
'    var c=el("div","cover");',
'    c.appendChild(el("div","cv-band"));',
'    var logo=el("img","cv-logo"); logo.src="/logo.png"; logo.alt="IBSL"; c.appendChild(logo);',
'    c.appendChild(el("div","wordmark","Strategy2Results\\u00ae"));',
'    c.appendChild(el("h1","","Learning Portfolio"));',
'    c.appendChild(el("div","cv-rule"));',
'    c.appendChild(el("div","who", name||"\\u2014"));',
'    var meta=el("div","meta"); meta.textContent=(cohort?("Cohort: "+cohort+"  \\u00b7  "):"")+"Generated "+new Date().toLocaleDateString("en-GB",{day:"numeric",month:"long",year:"numeric"}); c.appendChild(meta);',
'    c.appendChild(el("div","brand","Institute of Behavioural Strategy & Leadership"));',
'    return c;',
'  }',
'  function buildToc(cats){',
'    var t=el("div","toc"); t.appendChild(el("h2","","Contents"));',
'    var ol=el("ol");',
'    cats.forEach(function(cat){ var seq=Number(cat.sequence); var li=el("li"); var a=el("a"); a.href="#ch-"+cat.id; a.textContent = seq===0?"Unit 1 \\u00b7 Behavioural Strategy Fundamentals":("Unit "+(seq+1)+" \\u00b7 "+(cat.title||cat.id)); li.appendChild(a); ol.appendChild(li); });',
'    t.appendChild(ol); return t;',
'  }',
'',
'  // ───────────────────────── boot ─────────────────────────',
'  var viewerIsSelf=false;   // participant viewing their own portfolio',
'  function boot(){',
'    if(!participantId){ fatal("Missing participant","This collection link needs a ?participantId=<uuid> parameter."); return; }',
'    supabaseClient.auth.getSession().then(function(sres){',
'      var session=sres&&sres.data&&sres.data.session;',
'      if(!session){ fatal("Not signed in","Sign in to the S2R Portal, then reopen this collection."); return; }',
'      var uid=session.user.id;',
'      supabaseClient.from("profiles").select("role").eq("id",uid).maybeSingle().then(function(pr){',
'        var role=(pr&&pr.data&&pr.data.role)||"";',
'        // Participant self-view: allowed when (uid === participantId).',
'        viewerIsSelf=(uid===participantId);',
'        var allowed=(role==="facilitator"||role==="admin"||viewerIsSelf);',
'        if(!allowed){ fatal("Access restricted","This collection is viewable by its participant, facilitators and admins only."); return; }',
'        loadAndRender();',
'      }, function(){ fatal("Access check failed","Could not verify your role. Please refresh and try again."); });',
'    }, function(){ fatal("Session error","Could not read your session. Please refresh and try again."); });',
'  }',
'',
'  function loadAndRender(){',
'    var catP=supabaseClient.from("lens_catalog").select("id,unit,module,sequence,title,requires_lens").order("sequence",{ascending:true});',
'    var subP=supabaseClient.from("submissions").select("lens_id,cohort_id,payload,submitted_at,review_status,facilitator_feedback").eq("profile_id",participantId).order("submitted_at",{ascending:false});',
'    Promise.all([catP,subP]).then(function(res){',
'      var cat=res[0], sub=res[1];',
'      if(cat.error||!cat.data||!cat.data.length){ console.error("[collection] lens_catalog read:",cat.error); fatal("Could not load chapters","The lens catalogue could not be read in this session (this needs a facilitator SELECT policy on lens_catalog). "+(cat.error?cat.error.message:"")); return; }',
'      if(sub.error){ console.error("[collection] submissions read:",sub.error); fatal("Could not load submissions", sub.error.message||"Read failed."); return; }',
'      var cats=cat.data; var subs=sub.data||[];',
'      // group submissions by lens_id (already newest-first)',
'      var byLens={}; subs.forEach(function(r){ (byLens[r.lens_id]=byLens[r.lens_id]||[]).push(r); });',
'      var cohortId=null; for(var i=0;i<subs.length;i++){ if(subs[i].cohort_id){ cohortId=subs[i].cohort_id; break; } }',
'      resolveWho(cohortId).then(function(who){',
'        var root=document.getElementById("root"); root.innerHTML="";',
'        root.appendChild(buildCover(who.name, who.cohort));',
'        root.appendChild(buildToc(cats));',
'        cats.forEach(function(c){ root.appendChild(chapterNode(c, byLens[c.id]||null)); });',
'        appendCompetencyProfile(root, cohortId);',
'      });',
'    }, function(err){ console.error("[collection] load error:",err); fatal("Could not load","An unexpected error occurred. Please refresh."); });',
'  }',
'',
'  // [COMPETENCY] My Competency Profile closes the portfolio. Facilitators have no access to it, so for them nothing is added.',
'  function appendCompetencyProfile(root, cohortId){',
'    if(!cohortId) return;',
'    supabaseClient.rpc("get_competency_profile",{p_cohort_id:cohortId,p_profile_id:participantId}).then(function(r){',
'      if(!r||r.error||!r.data||!r.data.length) return;',
'      var esc=function(s){ var d=document.createElement("div"); d.textContent=s==null?"":String(s); return d.innerHTML; };',
'      var h="<h2>My Competency Profile</h2>";',
'      var area="", open=false;',
'      r.data.forEach(function(x){',
'        if(x.area!==area){ if(open) h+="</table>"; area=x.area; open=true;',
'          h+="<h3>"+esc(area)+"</h3><table><tr><th>Competency</th><th>Beginning</th><th>Progressive</th><th>Unit mark</th></tr>"; }',
'        h+="<tr><td>"+esc(x.competency)+"</td><td>"+esc(x.beginning||"")+"</td><td>"+esc(x.progressive||"")+"</td><td>"+(typeof x.unit_mark==="number"?x.unit_mark+" / 100":"")+"</td></tr>";',
'      });',
'      if(open) h+="</table>";',
'      var sec=document.createElement("section"); sec.className="cp-sec"; sec.innerHTML=h;',
'      root.appendChild(sec);',
'    },function(){ /* no access: the profile is left out */ });',
'  }',
'',
'  // Resolve participant name + cohort name via the dashboard\\u2019s RPCs (RLS-safe). Best-effort.',
'  function resolveWho(cohortId){',
'    var who={name:null,cohort:null};',
'    var jobs=[];',
'    jobs.push(supabaseClient.from("profiles").select("full_name").eq("id",participantId).maybeSingle().then(function(r){ if(r&&r.data&&r.data.full_name) who.name=r.data.full_name; },function(){}));',
'    jobs.push(supabaseClient.rpc("get_facilitator_cohorts").then(function(r){ if(r&&r.data){ for(var i=0;i<r.data.length;i++){ if(cohortId&&r.data[i].cohort_id===cohortId){ who.cohort=r.data[i].cohort_name; break; } } } },function(){}));',
'    if(cohortId){ jobs.push(supabaseClient.rpc("get_cohort_participants",{p_cohort_id:cohortId}).then(function(r){ if(r&&r.data){ for(var i=0;i<r.data.length;i++){ var p=r.data[i]; if((p.profile_id||p.id)===participantId&&p.full_name){ who.name=p.full_name; break; } } } },function(){})); }',
'    if(viewerIsSelf&&cohortId){ jobs.push(supabaseClient.rpc("get_my_capstone",{p_cohort_id:cohortId}).then(function(r){ if(r&&r.data&&r.data.cohort&&r.data.cohort.name&&!who.cohort) who.cohort=r.data.cohort.name; },function(){})); }',
'    return Promise.all(jobs).then(function(){ return who; });',
'  }',
'',
'  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",boot); else boot();',
'})();',
'</script>',
'</body>',
'</html>',
''
  ].join('\n');
}
