# -*- coding: utf-8 -*-
"""Shoot the pictures for the "Section N Reflections" slides of the Unit 6 deck from the participant page.
Usage (cloud workspace): python3 shoot_reflections_u07.py <stand-alone participant page> <out folder>
The page is the PREVIEW copy made by make_previews.py (it needs no sign-in). Network is blocked.
ref_3.1.png and ref_4.1.png show the reflection label and its question, as on the portal; """
import asyncio, sys, os, json, pathlib
from playwright.async_api import async_playwright
PAGE, OUT = sys.argv[1], sys.argv[2]
REFL = {'1.2': 'ref13', '1.3': 'ref14', '1.4': 'ref15', '3.2': 'ref12'}
CSS = ('.mod{display:block!important}.acc-b{display:block!important;max-height:none!important}'
       'body>div[style*="position:fixed"]{display:none!important}*{font-family:Carlito,Arial,sans-serif!important}'
       '.u6-pf{display:none!important}')
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        ctx = await b.new_context(viewport={'width': 860, 'height': 1200}, device_scale_factor=3)
        page = await ctx.new_page()
        await page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
        await page.goto(pathlib.Path(PAGE).resolve().as_uri()); await page.wait_for_timeout(800)
        await page.add_style_tag(content=CSS)
        await page.evaluate("document.querySelectorAll('.acc').forEach(function(a){a.classList.add('open');})"); await page.wait_for_timeout(300)
        os.makedirs(OUT, exist_ok=True); info = {}
        for part, rid in REFL.items():
            box = await page.evaluate("""(id)=>{var ta=document.getElementById(id);var blk=ta.closest('.ref-block');var b=blk.getBoundingClientRect();
                var q=blk.querySelector('p.ref-prompt'),p=q.getBoundingClientRect();
                return {x:b.left+window.scrollX,y:b.top+window.scrollY,width:b.width,height:p.bottom-b.top+10,label:blk.querySelector('.ref-label').innerText,prompt:q.textContent}}""", rid)
            name = 'ref_%s.png' % part
            await page.screenshot(path=os.path.join(OUT, name), clip={k: box[k] for k in ('x', 'y', 'width', 'height')}, full_page=True)
            info[part] = {'file': name, 'label': box['label'].strip(), 'prompt': box['prompt'].strip()}
            print(name, '|', box['label'].strip(), '|', box['prompt'][:70], '|', round(box['width']), 'x', round(box['height']))
        json.dump(info, open(os.path.join(OUT, 'reflections.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        await b.close()
asyncio.run(main())
