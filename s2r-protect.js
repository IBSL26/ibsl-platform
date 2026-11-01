/**
 * S2R Protect (1 Nov 2026)
 * Protects programme content on participant pages:
 *  - copy block: no selecting, copying, cutting, right-clicking or dragging of content.
 *    Answer boxes stay fully usable (typing, selecting, copying, pasting).
 *  - name watermark: the signed-in person's name and email, faintly across the page,
 *    cut away around answer boxes so the boxes stay clean.
 *  - print block: printing the page gives a notice. Printed group records and reports open in
 *    their own window, so they are unaffected. Add data-allow-print to the script tag to keep
 *    printing on a page, and the watermark then prints with it.
 * Add data-no-mark-present to the script tag to leave the watermark off the presenting window.
 * Admin accounts are exempt.
 * No website can stop a device taking a screenshot: the watermark is what covers that risk.
 *
 * © 2026 IBSLeadership. All rights reserved.
 */
(function () {
  'use strict';

  var SUPABASE_URL = 'https://tayrxqbrttlrdowrzobm.supabase.co';
  var SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRheXJ4cWJydHRscmRvd3J6b2JtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY3ODAyOTUsImV4cCI6MjA5MjM1NjI5NX0.8eaQauK1GPI3OXyHLdRAfbSwLfaYLB3_amHt6FhZxG0';
  var AUTH_KEY = 'sb-tayrxqbrttlrdowrzobm-auth-token';
  var BOXES = 'textarea,select,[contenteditable="true"],[contenteditable=""],' +
    'input:not([type=hidden]):not([type=radio]):not([type=checkbox]):not([type=button]):not([type=submit]):not([type=range])';

  var root = document.documentElement;
  var script = document.currentScript;
  var allowPrint = !!(script && script.hasAttribute('data-allow-print'));
  var noMark = !!(script && script.hasAttribute('data-no-mark-present')) && /[?&]mode=present\b/.test(location.search);
  var active = true;
  var layer = null;
  var pending = false;
  var lastClip = '';

  root.classList.add('s2r-guard');
  if (!allowPrint) root.classList.add('s2r-noprint');

  var css = document.createElement('style');
  css.textContent =
    'html.s2r-guard body{-webkit-user-select:none;user-select:none;-webkit-touch-callout:none;}' +
    'html.s2r-guard img{-webkit-user-drag:none;}' +
    'html.s2r-guard input,html.s2r-guard textarea,html.s2r-guard select,html.s2r-guard [contenteditable]{' +
      '-webkit-user-select:text;user-select:text;-webkit-touch-callout:default;}' +
    '#s2r-mark{position:fixed;top:0;left:0;width:100%;height:100%;z-index:2147483000;pointer-events:none;' +
      'background-repeat:repeat;-webkit-print-color-adjust:exact;print-color-adjust:exact;}' +
    '@media print{' +
      'html.s2r-noprint body>*{display:none!important;}' +
      'html.s2r-noprint body::before{display:block;padding:60px 40px;font:16px/1.6 Arial,sans-serif;color:#000;' +
        'content:"Programme content is the intellectual property of IBSL and cannot be printed from this page. ' +
        'To print a group record or report, use its print button and allow pop-ups for this site.";}' +
    '}';
  (document.head || root).appendChild(css);

  function editable(el) {
    if (!el || el.nodeType !== 1) el = el && el.parentElement;
    return !!(el && el.closest && el.closest('input,textarea,select,[contenteditable="true"],[contenteditable=""]'));
  }

  function block(e) {
    if (active && !editable(e.target)) e.preventDefault();
  }
  document.addEventListener('copy', block, true);
  document.addEventListener('cut', block, true);
  document.addEventListener('contextmenu', block, true);
  document.addEventListener('selectstart', block, true);
  document.addEventListener('dragstart', block, true);

  document.addEventListener('keydown', function (e) {
    if (!active || !(e.ctrlKey || e.metaKey)) return;
    var k = (e.key || '').toLowerCase();
    if (k === 's' || k === 'u' || (k === 'p' && !allowPrint)) e.preventDefault();
  }, true);

  function session() {
    try {
      var s = JSON.parse(localStorage.getItem(AUTH_KEY) || 'null');
      return s && s.user ? s : null;
    } catch (err) { return null; }
  }

  function esc(t) {
    return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function tile(name, email) {
    var lines = (name ? '<text x="0" y="-10">' + esc(name) + '</text><text x="0" y="14">' + esc(email) + '</text>'
                      : '<text x="0" y="2">' + esc(email) + '</text>');
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="320" height="200">' +
      '<g transform="translate(160 100) rotate(-28)" text-anchor="middle" font-family="Arial,sans-serif" ' +
      'font-size="15" font-weight="400" fill="#808080" fill-opacity="0.09">' + lines + '</g></svg>';
    return 'url("data:image/svg+xml,' + encodeURIComponent(svg) + '")';
  }

  function clip() {
    pending = false;
    if (!layer) return;
    var W = window.innerWidth, H = window.innerHeight;
    var d = 'M0 0H' + W + 'V' + H + 'H0Z';
    var els = document.querySelectorAll(BOXES);
    for (var i = 0; i < els.length; i++) {
      var r = els[i].getBoundingClientRect();
      if (!r.width || !r.height || r.bottom < 0 || r.top > H || r.right < 0 || r.left > W) continue;
      d += 'M' + Math.round(r.left) + ' ' + Math.round(r.top) + 'h' + Math.round(r.width) +
           'v' + Math.round(r.height) + 'h' + (-Math.round(r.width)) + 'z';
    }
    if (d === lastClip) return;
    lastClip = d;
    var v = 'path(evenodd,"' + d + '")';
    layer.style.webkitClipPath = v;
    layer.style.clipPath = v;
  }

  function schedule() {
    if (pending || !layer) return;
    pending = true;
    requestAnimationFrame(clip);
  }

  function showMark(name, email) {
    if (!email && !name) return;
    var image = tile(name, email);
    function place() {
      if (!active || !document.body) return;
      if (!layer) {
        layer = document.createElement('div');
        layer.id = 's2r-mark';
        layer.setAttribute('aria-hidden', 'true');
        lastClip = '';
      }
      layer.style.backgroundImage = image;
      if (layer.parentNode !== document.body) document.body.appendChild(layer);
    }
    place();
    clip();
    ['scroll', 'resize', 'click', 'input', 'focusin', 'transitionend', 'animationend'].forEach(function (t) {
      window.addEventListener(t, schedule, true);
    });
    new MutationObserver(schedule).observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['class', 'style', 'hidden'] });
    setInterval(function () { place(); schedule(); }, 800);
  }

  function release() {
    active = false;
    root.classList.remove('s2r-guard', 's2r-noprint');
    if (layer && layer.parentNode) layer.parentNode.removeChild(layer);
    layer = null;
  }

  function start() {
    var s = session();
    if (!s) return;
    var email = s.user.email || '';
    var meta = s.user.user_metadata || {};
    fetch(SUPABASE_URL + '/rest/v1/profiles?select=full_name,role&id=eq.' + encodeURIComponent(s.user.id), {
      headers: { apikey: SUPABASE_KEY, Authorization: 'Bearer ' + s.access_token }
    }).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; }).then(function (rows) {
      var p = rows && rows[0] || {};
      if (p.role === 'admin') { release(); return; }
      if (!noMark) showMark(p.full_name || meta.full_name || '', email);
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
