/*
 * s2r-breakmusic.js: break music for the admin and facilitator dashboards.
 * The music is generated in the browser, so there are no audio files and no
 * third-party recordings. Loaded by dashboard_A.html and dashboard_F.html only.
 */
(function () {
  'use strict';

  var TRACKS = {
    calm:   { label: 'Calm',   chord: 10, wave: 'sine',     cutoff: 900,  bells: 2, chords: [[50,57,62,66],[47,54,59,62],[43,50,55,59],[45,52,57,61]], scale: [74,76,78,81,83,86] },
    warm:   { label: 'Warm',   chord: 8,  wave: 'triangle', cutoff: 1000, bells: 3, chords: [[48,55,60,64],[45,52,57,60],[41,48,53,57],[43,50,55,59]], scale: [72,74,76,79,81,84] },
    bright: { label: 'Bright', chord: 6,  wave: 'triangle', cutoff: 1400, bells: 4, chords: [[50,57,62,66],[43,50,59,62],[47,54,59,62],[45,52,57,64]], scale: [74,76,78,81,83,86,88] }
  };
  var MAX_LEVEL = 0.8, FADE_END = 6, KEY = 's2r_breakmusic';

  var hz = function (m) { return 440 * Math.pow(2, (m - 69) / 12); };

  // Graph shared by live playback and the offline test.
  function buildGraph(ac, output) {
    var pad = ac.createBiquadFilter(); pad.type = 'lowpass'; pad.frequency.value = 1000; pad.Q.value = 0.3;
    var dry = ac.createGain(); dry.gain.value = 0.75;
    var wet = ac.createGain(); wet.gain.value = 0.55;
    var verb = ac.createConvolver();
    var len = Math.floor(ac.sampleRate * 4), ir = ac.createBuffer(2, len, ac.sampleRate);
    for (var c = 0; c < 2; c++) {
      var d = ir.getChannelData(c);
      for (var i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 3);
    }
    verb.buffer = ir;
    var limit = ac.createDynamicsCompressor();
    limit.threshold.value = -12; limit.ratio.value = 12; limit.attack.value = 0.01; limit.release.value = 0.3;
    pad.connect(dry); dry.connect(limit);
    pad.connect(wet); wet.connect(verb); verb.connect(limit);
    limit.connect(output);
    return { pad: pad, bell: wet, dryOut: dry };
  }

  function padNote(ac, g, midi, t, dur, wave, level) {
    var env = ac.createGain();
    env.gain.setValueAtTime(0, t);
    env.gain.linearRampToValueAtTime(level, t + 2.5);
    env.gain.setValueAtTime(level, t + dur - 0.5);
    env.gain.linearRampToValueAtTime(0, t + dur + 2.5);
    env.connect(g.pad);
    [-4, 4].forEach(function (cents) {
      var o = ac.createOscillator();
      o.type = wave; o.frequency.value = hz(midi); o.detune.value = cents;
      o.connect(env); o.start(t); o.stop(t + dur + 2.6);
    });
  }

  function bellNote(ac, g, midi, t) {
    var env = ac.createGain();
    env.gain.setValueAtTime(0, t);
    env.gain.linearRampToValueAtTime(0.09, t + 0.02);
    env.gain.exponentialRampToValueAtTime(0.0005, t + 3.5);
    env.connect(g.bell); env.connect(g.dryOut);
    var o = ac.createOscillator();
    o.type = 'sine'; o.frequency.value = hz(midi);
    o.connect(env); o.start(t); o.stop(t + 3.6);
  }

  // Schedules one chord and its bell notes. Returns the next chord index.
  function playChord(ac, g, tr, idx, t, walk) {
    var notes = tr.chords[idx % tr.chords.length];
    g.pad.frequency.setValueAtTime(tr.cutoff, t);
    notes.forEach(function (m, n) { padNote(ac, g, m, t, tr.chord, tr.wave, n === 0 ? 0.075 : 0.055); });
    var step = tr.chord / tr.bells;
    for (var b = 0; b < tr.bells; b++) {
      if (Math.random() < 0.35) continue;
      walk.pos = Math.max(0, Math.min(tr.scale.length - 1, walk.pos + Math.floor(Math.random() * 5) - 2));
      bellNote(ac, g, tr.scale[walk.pos], t + b * step + Math.random() * 0.4);
    }
    return idx + 1;
  }

  // ---- Live playback ----
  var st = load(), ctx = null, master = null, graph = null, sched = null, tick = null;
  var playing = false, endAt = 0, nextT = 0, idx = 0, walk = { pos: 2 }, ui = {};

  function load() {
    var d = { track: 'calm', mins: 10, vol: 60 };
    try { var s = JSON.parse(localStorage.getItem(KEY) || '{}'); for (var k in d) if (s[k] !== undefined) d[k] = s[k]; } catch (e) {}
    if (!TRACKS[d.track]) d.track = 'calm';
    return d;
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} }
  function level() { return (st.vol / 100) * MAX_LEVEL; }

  function start() {
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) { ui.note.textContent = 'This browser cannot play the music. Use Chrome or Edge.'; return; }
    ctx = new AC();
    if (ctx.state === 'suspended') ctx.resume();
    master = ctx.createGain();
    master.gain.setValueAtTime(0, ctx.currentTime);
    master.gain.linearRampToValueAtTime(level(), ctx.currentTime + 2);
    master.connect(ctx.destination);
    graph = buildGraph(ctx, master);
    playing = true; idx = 0; nextT = ctx.currentTime + 0.1;
    pump(); sched = setInterval(pump, 1000);
    setTimer(); tick = setInterval(update, 500);
    update();
  }

  function pump() {
    while (nextT < ctx.currentTime + 6) {
      var tr = TRACKS[st.track];
      idx = playChord(ctx, graph, tr, idx, nextT, walk);
      nextT += tr.chord;
    }
  }

  function stop(fade) {
    if (!playing) return;
    playing = false;
    clearInterval(sched); clearInterval(tick);
    var c = ctx, m = master, f = fade || 1.5;
    m.gain.cancelScheduledValues(c.currentTime);
    m.gain.setValueAtTime(m.gain.value, c.currentTime);
    m.gain.linearRampToValueAtTime(0, c.currentTime + f);
    setTimeout(function () { try { c.close(); } catch (e) {} }, (f + 0.5) * 1000);
    ctx = master = graph = null;
    update();
  }

  function setTimer() { endAt = st.mins ? Date.now() + st.mins * 60000 : 0; }
  function clock(ms) {
    var s = Math.max(0, Math.ceil(ms / 1000)), m = Math.floor(s / 60);
    return m + ':' + (s % 60 < 10 ? '0' : '') + (s % 60);
  }

  function update() {
    if (playing && endAt && Date.now() >= endAt) { stop(FADE_END); return; }
    var left = playing && endAt ? clock(endAt - Date.now()) : '';
    ui.open.textContent = playing ? '♪ ' + (left || 'Playing') : '♪ Break music';
    ui.play.textContent = playing ? 'Stop' : 'Play';
    ui.status.textContent = playing ? (left ? 'Ends in ' + left : 'Playing until you stop it') : 'Stopped';
  }

  // ---- Interface ----
  function choiceRow(parent, opts, current, onPick) {
    var row = el('div', 'bm-row', parent), btns = [];
    opts.forEach(function (o) {
      var b = el('button', 'bm-choice', row); b.type = 'button'; b.textContent = o.label;
      var mark = function () { btns.forEach(function (x) { x.b.classList.toggle('on', x.v === current); }); };
      btns.push({ b: b, v: o.value });
      b.addEventListener('click', function () { current = o.value; mark(); onPick(o.value); });
      mark();
    });
  }
  function el(tag, cls, parent) { var e = document.createElement(tag); if (cls) e.className = cls; if (parent) parent.appendChild(e); return e; }

  function init() {
    var ref = document.getElementById('chpwBtn');
    if (!ref || document.getElementById('bmOpen')) return;

    var css = el('style'); css.textContent =
      '.bm-panel{position:fixed;top:80px;right:16px;width:280px;max-width:calc(100vw - 32px);background:#fff;color:#1c1c1c;border-top:3px solid #c9a84c;border-radius:4px;box-shadow:0 10px 30px rgba(0,0,0,.28);padding:16px;z-index:9000;font-size:13px;box-sizing:border-box;display:none}' +
      '.bm-panel.open{display:block}' +
      '.bm-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}' +
      '.bm-title{font-weight:700;color:#1a3a2a;font-size:15px}' +
      '.bm-x{background:none;border:0;font-size:20px;line-height:1;cursor:pointer;color:#6b7280;padding:0 4px}' +
      '.bm-label{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:#6b7280;margin:10px 0 5px}' +
      '.bm-row{display:flex;gap:6px}' +
      '.bm-choice{flex:1;padding:7px 2px;border:1px solid #d1d5db;background:#fff;color:#1c1c1c;border-radius:3px;cursor:pointer;font:inherit;font-size:12px;white-space:nowrap}' +
      '.bm-choice.on{background:#1a3a2a;border-color:#1a3a2a;color:#fff}' +
      '.bm-vol{width:100%;accent-color:#1a3a2a;margin:0}' +
      '.bm-play{width:100%;margin-top:14px;padding:10px;background:#c9a84c;color:#0f2419;border:0;border-radius:3px;font:inherit;font-weight:700;cursor:pointer}' +
      '.bm-status{text-align:center;margin-top:8px;font-weight:600;color:#1a3a2a}' +
      '.bm-note{margin-top:8px;font-size:11.5px;line-height:1.45;color:#6b7280}' +
      '@media (max-width:640px){#bmOpen{position:fixed;right:16px;bottom:16px;z-index:8999;background:#1a3a2a;color:#fff;border-color:#c9a84c}.bm-panel{top:auto;bottom:64px}}';
    document.head.appendChild(css);

    ui.open = el('button'); ui.open.id = 'bmOpen'; ui.open.type = 'button'; ui.open.className = ref.className;
    ui.open.style.whiteSpace = 'nowrap';
    ref.parentNode.insertBefore(ui.open, ref);

    var p = el('div', 'bm-panel', document.body); p.id = 'bmPanel';
    var head = el('div', 'bm-head', p);
    el('div', 'bm-title', head).textContent = 'Break music';
    var x = el('button', 'bm-x', head); x.type = 'button'; x.textContent = '×'; x.setAttribute('aria-label', 'Close');

    el('div', 'bm-label', p).textContent = 'Music';
    choiceRow(p, Object.keys(TRACKS).map(function (k) { return { label: TRACKS[k].label, value: k }; }), st.track, function (v) { st.track = v; save(); });

    el('div', 'bm-label', p).textContent = 'Break length';
    choiceRow(p, [{ label: '5 min', value: 5 }, { label: '10 min', value: 10 }, { label: '15 min', value: 15 }, { label: 'No limit', value: 0 }], st.mins, function (v) {
      st.mins = v; save(); if (playing) { setTimer(); update(); }
    });

    el('div', 'bm-label', p).textContent = 'Volume';
    var vol = el('input', 'bm-vol', p); vol.type = 'range'; vol.min = 0; vol.max = 100; vol.value = st.vol; vol.setAttribute('aria-label', 'Volume');
    vol.addEventListener('input', function () {
      st.vol = +vol.value; save();
      if (playing) master.gain.setTargetAtTime(level(), ctx.currentTime, 0.1);
    });

    ui.play = el('button', 'bm-play', p); ui.play.type = 'button';
    ui.status = el('div', 'bm-status', p);
    ui.note = el('div', 'bm-note', p);
    ui.note.textContent = 'Keep this page open while the music plays. To let the class hear it in Teams, share with computer sound on.';

    ui.open.addEventListener('click', function () { p.classList.toggle('open'); });
    x.addEventListener('click', function () { p.classList.remove('open'); });
    ui.play.addEventListener('click', function () { playing ? stop() : start(); });
    window.addEventListener('pagehide', function () { if (playing) stop(0.1); });
    update();
  }

  window.S2RBreakMusic = { tracks: TRACKS, buildGraph: buildGraph, playChord: playChord };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
