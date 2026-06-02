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
spanB = replaceOnce(spanB, 'function renderValue(value, depth) {', 'function renderValue(value, depth, lensId) {', 'renderValue signature');
spanB = replaceOnce(spanB, 'const valueEl = renderValue(value, depth);', 'const valueEl = renderValue(value, depth, lensId);', 'renderFieldEntry->renderValue');
spanB = replaceOnce(spanB, 'li.appendChild(renderValue(item, depth + 1));', 'li.appendChild(renderValue(item, depth + 1, lensId));', 'array-item renderValue');
spanB = replaceOnce(spanB, 'body.appendChild(renderValue(val, 0));', 'body.appendChild(renderValue(val, 0, lensId));', 'sip_data renderValue');
// prompt-primary hook: renderFieldEntry uses labelFor() (defined in collection.html) which prefers an
// extracted question prompt and falls back to the verbatim humanizeFieldName.
spanB = replaceOnce(spanB, 'label.textContent = humanizeFieldName(fieldName, lensId);', 'label.textContent = labelFor(fieldName, lensId);', 'labelFor hook');

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
          .replace(/&nbsp;/g, ' ').replace(/&rarr;/g, '→').replace(/&[a-z]+;/gi, ' ')
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

  const labelRe = /<(?:div|p|label|span|h[2-6])\b[^>]*class="[^"]*(?:ref-label|score-notes-lbl|field-label|prompt|q-label|reflection-prompt)[^"]*"[^>]*>([\s\S]*?)<\/(?:div|p|label|span|h[2-6])>/gi;
  const forRe = function(key){ return new RegExp('<label\\b[^>]*\\bfor="' + key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '"[^>]*>([\\s\\S]*?)<\\/label>', 'i'); };

  let found = 0; const missed = [];
  Object.keys(keys).forEach(function(key){
    const pos = keys[key];
    // 1) explicit <label for="key">
    let fm = forRe(key).exec(html);
    if (fm){ const t = stripTags(fm[1]); if (t){ prompts[key] = t; found++; return; } }
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

const MICRO_CLIMB = {};
const PROMPTS = {};
Object.keys(LENS_FILES).forEach(function(lensId){
  const f = LENS_FILES[lensId];
  assert(fs.existsSync(path.join(ROOT, f)), 'participant file missing: ' + f);
  const html = read(f);
  MICRO_CLIMB[lensId] = extractSummary(html, lensId);
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
'<title>S2R Collection</title>',
'<!-- Generated by build_collection.js — DO NOT edit by hand; re-run the builder. Build: %%BUILD_INFO%% -->',
'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">',
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
'  html,body{background:#fff;}',
'  .print-bar{display:none!important;}',
'  /* force every collapsible fully open on paper */',
'  .response-module.collapsed .response-module-body,.response-field-collapsible.collapsed>*{display:block!important;}',
'  .response-module.collapsed .response-module-heading::after{content:""!important;}',
'  .sum-block .sum-body{display:block!important;}',
'  .response-toolbar,.response-expand-all{display:none!important;}',
'}',
'</style>',
'<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>',
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
'  // prompt-primary label hook (spec §: extracted question prompt, else verbatim humanizeFieldName)',
'  function labelFor(name,lensId){ var p=PROMPTS[lensId]&&PROMPTS[lensId][name]; return (p&&String(p).trim())?p:humanizeFieldName(name,lensId); }',
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
'  function chapterNode(cat, subs){',
'    var ch=el("div","chapter"); ch.id="ch-"+cat.id;',
'    var head=el("div","chapter-head");',
'    var seq=Number(cat.sequence);',
'    var h2=el("h2", null, seq===0 ? "Foundations" : ("Lens "+seq+" \\u00b7 "+(cat.title||cat.id)));',
'    head.appendChild(h2);',
'    var latest = subs && subs.length ? subs[0] : null;',
'    if(latest){',
'      var sub=el("div","sub"); var dt=fmtDate(latest.submitted_at);',
'      var subText = dt ? ("Submitted "+dt) : "";',
'      sub.textContent = subText;',
'      if(typeof latest.score==="number"){',
'        var scoreEl = el("div","lens-score","Score: "+latest.score+" / 100");',
'        head.appendChild(scoreEl);',
'      }',
'      head.appendChild(sub);',
'    }',
'    ch.appendChild(head);',
'',
'    if(!latest){',
'      ch.appendChild(el("div","not-submitted","Not yet submitted."));',
'    } else {',
'      var payload = latest.payload || {};',
'      ch.appendChild(el("div","section-label","Responses"));',
'      ch.appendChild(renderResponses(payload, cat.id));',
'      var fc = detectFiveCommitments(payload);',
'      if(fc) ch.appendChild(renderFiveCommitmentsPanel(fc));',
'    }',
'',
'    var mc = MICRO_CLIMB[cat.id];',
'    if(mc && mc.length){ ch.appendChild(el("div","section-label","Micro-Climb Summary")); ch.appendChild(renderMicroClimb(mc)); }',
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
'    c.appendChild(el("div","wordmark","Strategy2Results\\u00ae \\u00b7 Collection"));',
'    c.appendChild(el("h1","","Learning Portfolio"));',
'    c.appendChild(el("div","who", name||"\\u2014"));',
'    var meta=el("div","meta"); meta.textContent=(cohort?("Cohort: "+cohort+"  \\u00b7  "):"")+"Generated "+new Date().toLocaleDateString("en-GB",{day:"numeric",month:"long",year:"numeric"}); c.appendChild(meta);',
'    c.appendChild(el("div","brand","IBSLeadership \\u00b7 S2R\\u00ae Portal"));',
'    return c;',
'  }',
'  function buildToc(cats){',
'    var t=el("div","toc"); t.appendChild(el("h2","","Contents"));',
'    var ol=el("ol");',
'    cats.forEach(function(cat){ var seq=Number(cat.sequence); var li=el("li"); var a=el("a"); a.href="#ch-"+cat.id; a.textContent = seq===0?"Foundations":("Lens "+seq+" \\u00b7 "+(cat.title||cat.id)); li.appendChild(a); ol.appendChild(li); });',
'    t.appendChild(ol); return t;',
'  }',
'',
'  // ───────────────────────── boot ─────────────────────────',
'  function boot(){',
'    if(!participantId){ fatal("Missing participant","This collection link needs a ?participantId=<uuid> parameter."); return; }',
'    supabaseClient.auth.getSession().then(function(sres){',
'      var session=sres&&sres.data&&sres.data.session;',
'      if(!session){ fatal("Not signed in","Sign in to the S2R Portal as a facilitator, then reopen this collection."); return; }',
'      var uid=session.user.id;',
'      supabaseClient.from("profiles").select("role").eq("id",uid).maybeSingle().then(function(pr){',
'        var role=(pr&&pr.data&&pr.data.role)||"";',
'        // TODO(W3-Pn): add participant self-view — allow when (uid === participantId).',
'        var allowed=(role==="facilitator"||role==="admin");',
'        if(!allowed){ fatal("Access restricted","This collection is viewable by facilitators and admins only."); return; }',
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
'      });',
'    }, function(err){ console.error("[collection] load error:",err); fatal("Could not load","An unexpected error occurred. Please refresh."); });',
'  }',
'',
'  // Resolve participant name + cohort name via the dashboard\\u2019s RPCs (RLS-safe). Best-effort.',
'  function resolveWho(cohortId){',
'    var who={name:null,cohort:null};',
'    var jobs=[];',
'    jobs.push(supabaseClient.from("profiles").select("full_name").eq("id",participantId).maybeSingle().then(function(r){ if(r&&r.data&&r.data.full_name) who.name=r.data.full_name; },function(){}));',
'    jobs.push(supabaseClient.rpc("get_facilitator_cohorts").then(function(r){ if(r&&r.data){ for(var i=0;i<r.data.length;i++){ if(cohortId&&r.data[i].cohort_id===cohortId){ who.cohort=r.data[i].cohort_name; break; } } } },function(){}));',
'    if(cohortId){ jobs.push(supabaseClient.rpc("get_cohort_participants",{p_cohort_id:cohortId}).then(function(r){ if(r&&r.data){ for(var i=0;i<r.data.length;i++){ var p=r.data[i]; if((p.profile_id||p.id)===participantId&&p.full_name){ who.name=p.full_name; break; } } } },function(){})); }',
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
