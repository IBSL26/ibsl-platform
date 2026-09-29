// IBSL unit-deck design system v2: every piece of slide text is 24pt or larger.
const pptxgen = require('pptxgenjs');
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const sharp = require('sharp');
const fa = require('react-icons/fa');
const gi = require('react-icons/gi');

const C = { forest: '1A5C2C', deep: '0F3B1C', gold: 'C6A24C', goldLight: 'E6D3A0', tint: 'EEF4EF', white: 'FFFFFF', ink: '1F2A22', muted: '4E5E53', line: 'D5DED7', paleText: 'DDE8DF' };
const F = { head: 'Cambria', body: 'Calibri' };
const W = 13.333, H = 7.5, MIN = 24;

const cache = {};
async function icon(name, color) {
  const k = name + color; if (cache[k]) return cache[k];
  const Comp = fa[name] || gi[name]; if (!Comp) throw new Error('icon ' + name);
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: '#' + color, size: '256' }));
  return (cache[k] = 'image/png;base64,' + (await sharp(Buffer.from(svg)).png().toBuffer()).toString('base64'));
}
async function badge(s, name, x, y, d, circle, fg) {
  s.addShape('ellipse', { x, y, w: d, h: d, fill: { color: circle }, line: { color: circle } });
  const p = d * 0.25; s.addImage({ data: await icon(name, fg), x: x + p, y: y + p, w: d - 2 * p, h: d - 2 * p });
}
function T(s, text, o) {
  const check = v => { if (v !== undefined && v < MIN) throw new Error('font below 24: ' + v + ' in ' + JSON.stringify(text).slice(0, 60)); };
  check(o.fontSize);
  if (Array.isArray(text)) text.forEach(r => r.options && check(r.options.fontSize));
  if (o.fontSize === undefined) throw new Error('fontSize required');
  const plain = Array.isArray(text) ? text.map(r => r.text + (r.options && r.options.breakLine ? '\n' : '')).join('') : String(text);
  const fs = o.fontSize, cpl = Math.max(1, (o.w * 72) / (fs * (o.fontFace === F.head ? 0.47 : 0.45)));
  const lines = plain.split('\n').reduce((a, p) => a + Math.max(1, Math.ceil(p.length / cpl)), 0);
  const longest = plain.split(/\s+/).reduce((m, w) => Math.max(m, w.length), 0);
  if (longest > cpl * 0.95) console.warn('WORD SPLIT? ' + longest + ' chars > ' + cpl.toFixed(1) + ' per line: ' + plain.slice(0, 50));
  if (lines * fs * 1.17 / 72 > o.h + 0.1) console.warn('OVERFLOW? ' + lines + ' lines @' + fs + 'pt in h=' + o.h.toFixed(2) + ': ' + plain.slice(0, 70).replace(/\n/g, ' / '));
  s.addText(text, Object.assign({ isTextBox: true, fontFace: F.body, color: C.ink, margin: 0, valign: 'top' }, o));
}
function box(s, x, y, w, h, color) { s.addShape('roundRect', { x, y, w, h, fill: { color }, line: { color }, rectRadius: 0.1 }); }

class Deck {
  constructor(m) { this.m = m; this.p = new pptxgen(); this.p.layout = 'LAYOUT_WIDE'; this.p.author = 'Institute of Behavioural Strategy & Leadership'; this.p.company = 'IBSL'; this.p.title = `Unit ${m.unit} · ${m.title}`; }
  slide(dark) { const s = this.p.addSlide(); s.background = { color: dark ? C.deep : C.white }; return s; }
  title(s, t, dark) { T(s, t, { x: 0.6, y: 0.45, w: 12.1, h: 0.95, fontSize: 36, fontFace: F.head, bold: true, color: dark ? C.white : C.forest, valign: 'middle' }); }

  async cover(d) {
    const s = this.slide(true);
    s.addImage({ path: d.logo, x: W - 4.3, y: 1.45, w: 3.4, h: 3.3 });
    T(s, `Module ${this.m.module} · ${this.m.moduleName} · Unit ${this.m.unit}`, { x: 0.8, y: 1.3, w: 8, h: 0.5, fontSize: 24, bold: true, color: C.gold });
    T(s, this.m.title, { x: 0.8, y: 1.95, w: 7.9, h: 2.2, fontSize: 48, fontFace: F.head, bold: true, color: C.white, valign: 'middle' });
    T(s, d.subtitle, { x: 0.8, y: 4.35, w: 7.9, h: 1.3, fontSize: 24, italic: true, color: C.paleText });
    T(s, 'Strategy2Results® · Facilitator deck', { x: 0.8, y: 6.2, w: 8, h: 0.5, fontSize: 24, color: C.goldLight });
    s.addNotes(d.notes);
  }
  // numbered / icon list rows
  async list(d) {
    const s = this.slide(); this.title(s, d.title);
    const n = d.rows.length, top = 1.65, avail = 5.35, rh = avail / n, ib = Math.min(0.7, rh * 0.7);
    for (let i = 0; i < n; i++) {
      const r = d.rows[i], y = top + i * rh;
      await badge(s, r.icon, 0.6, y + (rh - ib) / 2, ib, r.gold ? C.gold : C.forest, C.white);
      T(s, r.label ? [{ text: r.label + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: r.text || '' }] : r.text,
        { x: 0.6 + ib + 0.35, y, w: 12.13 - ib - 0.35, h: rh, fontSize: d.fontSize || 26, valign: 'middle' });
    }
    s.addNotes(d.notes);
  }
  async section(d) {
    const s = this.slide(); s.background = { color: C.forest };
    T(s, String(d.num), { x: 0.5, y: 0.9, w: 2.3, h: 2.4, fontSize: 150, fontFace: F.head, bold: true, color: C.gold });
    T(s, `Section ${d.num}`, { x: 3.0, y: 1.0, w: 9, h: 0.5, fontSize: 24, bold: true, color: C.goldLight });
    T(s, `${d.name} — ${d.anchor}`, { x: 3.0, y: 1.5, w: 9.8, h: 0.95, fontSize: 44, fontFace: F.head, bold: true, color: C.white });
    T(s, d.heading, { x: 3.0, y: 2.45, w: 9.8, h: 0.95, fontSize: 26, italic: true, color: C.paleText });
    T(s, 'Section learning outcomes', { x: 3.0, y: 3.55, w: 9, h: 0.5, fontSize: 24, bold: true, color: C.gold });
    let y = 4.1;
    for (const o of d.outcomes) {
      await badge(s, 'FaArrowRight', 3.0, y + 0.08, 0.42, C.gold, C.deep);
      T(s, o, { x: 3.6, y, w: 9.2, h: 1.2, fontSize: 24, color: C.white });
      y += 1.3;
    }
    s.addNotes(d.notes);
  }
  async prompt(d) {
    const s = this.slide(true);
    await badge(s, d.icon || 'FaQuestion', 0.8, 1.2, 1.2, C.gold, C.deep);
    T(s, d.label, { x: 2.3, y: 1.4, w: 10, h: 0.7, fontSize: 26, bold: true, color: C.gold });
    T(s, d.text, { x: 2.3, y: 2.3, w: 10.3, h: 3.8, fontSize: 36, fontFace: F.head, italic: true, color: C.white, valign: 'top' });
    if (d.foot) T(s, d.foot, { x: 2.3, y: 6.1, w: 10.3, h: 0.9, fontSize: 24, color: C.paleText });
    s.addNotes(d.notes);
  }
  // cards: items {icon,title,text,dark}; cols
  async cards(d) {
    const s = this.slide(); this.title(s, d.title);
    const cols = d.cols || d.items.length, rows = Math.ceil(d.items.length / cols), gap = 0.3;
    const top = 1.65, bottom = d.band ? 5.95 : 6.95;
    const cw = (12.13 - gap * (cols - 1)) / cols, ch = (bottom - top - gap * (rows - 1)) / rows, ib = d.iconSize || 0.7;
    for (let i = 0; i < d.items.length; i++) {
      const it = d.items[i], x = 0.6 + (i % cols) * (cw + gap), y = top + Math.floor(i / cols) * (ch + gap);
      box(s, x, y, cw, ch, it.dark ? C.forest : C.tint);
      await badge(s, it.icon, x + 0.25, y + 0.25, ib, it.dark ? C.gold : C.forest, it.dark ? C.deep : C.white);
      if (d.titleBeside) {
        const ts = d.titleSize || 26, tw = cw - ib - 0.7, lines = Math.ceil((it.title.length * ts * 0.0075) / tw), th = Math.max(ib + 0.1, lines * ts * 0.0175 + 0.1);
        T(s, it.title, { x: x + 0.25 + ib + 0.2, y: y + 0.2, w: tw, h: th, fontSize: ts, bold: true, fontFace: F.head, color: it.dark ? C.white : C.forest, valign: 'middle' });
        if (it.text) T(s, it.text, { x: x + 0.25, y: y + 0.35 + th, w: cw - 0.5, h: ch - th - 0.5, fontSize: d.textSize || 24, color: it.dark ? C.white : C.ink });
      } else {
        const ts = d.titleSize || 26, lines = Math.ceil((it.title.length * ts * 0.0075) / (cw - 0.5)), th = lines * ts * 0.0175 + 0.1;
        T(s, it.title, { x: x + 0.25, y: y + ib + 0.4, w: cw - 0.5, h: th, fontSize: ts, bold: true, fontFace: F.head, color: it.dark ? C.white : C.forest });
        if (it.text) T(s, it.text, { x: x + 0.25, y: y + ib + 0.55 + th, w: cw - 0.5, h: ch - ib - 0.7 - th, fontSize: d.textSize || 24, color: it.dark ? C.white : C.ink });
      }
    }
    if (d.band) { box(s, 0.6, 6.15, 12.13, 0.85, C.deep); T(s, d.band, { x: 0.9, y: 6.15, w: 11.6, h: 0.85, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); }
    s.addNotes(d.notes);
  }
  // Big statistic left, rows right
  async stat(d) {
    const s = this.slide(); this.title(s, d.title);
    box(s, 0.6, 1.65, 4.0, 5.3, C.forest);
    T(s, d.big, { x: 0.7, y: 1.9, w: 3.8, h: 1.6, fontSize: 80, bold: true, fontFace: F.head, color: C.gold, align: 'center', valign: 'middle' });
    T(s, d.caption, { x: 0.85, y: 3.6, w: 3.5, h: 3.2, fontSize: 24, color: C.white, align: 'center' });
    const n = d.rows.length, rh = 5.3 / n;
    for (let i = 0; i < n; i++) {
      const r = d.rows[i], y = 1.65 + i * rh;
      await badge(s, r.icon, 4.95, y + (rh - 0.62) / 2, 0.62, C.forest, C.white);
      T(s, r.label ? [{ text: r.label + '  ', options: { bold: true, color: C.forest, fontFace: F.head } }, { text: r.text || '', options: { color: C.muted } }] : r.text,
        { x: 5.8, y, w: 6.93, h: rh, fontSize: 24, valign: 'middle' });
    }
    s.addNotes(d.notes);
  }
  async compare(d) {
    const s = this.slide(); this.title(s, d.title);
    for (let i = 0; i < 2; i++) {
      const c = d.cols[i], x = 0.6 + i * 6.23, dark = i === 1;
      box(s, x, 1.65, 5.9, d.band ? 4.3 : 5.3, dark ? C.forest : C.tint);
      await badge(s, c.icon, x + 0.3, 1.9, 0.8, dark ? C.gold : C.forest, dark ? C.deep : C.white);
      T(s, c.title, { x: x + 1.3, y: 1.85, w: 4.45, h: 0.55, fontSize: 28, bold: true, fontFace: F.head, color: dark ? C.white : C.forest });
      T(s, c.sub, { x: x + 1.3, y: 2.4, w: 4.45, h: 0.5, fontSize: 24, italic: true, color: dark ? C.goldLight : C.muted });
      T(s, c.points.map((p, j) => ({ text: p, options: { bullet: true, breakLine: j < c.points.length - 1 } })),
        { x: x + 0.35, y: 3.1, w: 5.3, h: (d.band ? 5.85 : 6.85) - 3.1, fontSize: 24, color: dark ? C.white : C.ink, paraSpaceAfter: 6 });
    }
    if (d.band) { box(s, 0.6, 6.15, 12.13, 0.85, C.deep); T(s, d.band, { x: 0.9, y: 6.15, w: 11.6, h: 0.85, fontSize: 24, italic: true, color: C.white, valign: 'middle' }); }
    s.addNotes(d.notes);
  }
  async save(f) { await this.p.writeFile({ fileName: f }); }
}
module.exports = { Deck, C, F, W, H, T, box, badge };
