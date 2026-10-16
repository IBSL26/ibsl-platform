# -*- coding: utf-8 -*-
"""Pictures for the "Section N Reflections" slides of the Unit 9 deck, from the PREVIEW participant page (label and question of each reflection).
Usage: python3 shoot_refs_u09.py <PREVIEW participant page> <out folder>"""
import asyncio, sys, os, pathlib
from playwright.async_api import async_playwright
PAGE, OUT = sys.argv[1], sys.argv[2]
REFL = [('1.1', 'ref1'), ('1.2', 'ref2'), ('2.1', 'ref3'), ('2.3', 'ref4'), ('3.1', 'ref7'), ('4', 'ref8')]
CSS = ('.mod{display:block!important}.acc-b{display:block!important;max-height:none!important}'
       'body>div[style*="position:fixed"]{display:none!important}*{font-family:Carlito,Arial,sans-serif!important}')
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        ctx = await b.new_context(viewport={'width': 860, 'height': 1200}, device_scale_factor=3)
        page = await ctx.new_page()
        await page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
        await page.goto(pathlib.Path(PAGE).resolve().as_uri()); await page.wait_for_timeout(800)
        await page.add_style_tag(content=CSS)
        await page.evaluate("document.querySelectorAll('.acc').forEach(function(a){a.classList.add('open');})"); await page.wait_for_timeout(300)
        os.makedirs(OUT, exist_ok=True)
        for part, rid in REFL:
            box = await page.evaluate("""(id)=>{var ta=document.getElementById(id);var blk=ta.closest('.ref-block');var b=blk.getBoundingClientRect();
                var q=blk.querySelector('p.ref-prompt'),p=q.getBoundingClientRect();
                return {x:b.left+window.scrollX,y:b.top+window.scrollY,width:b.width,height:p.bottom-b.top+10}}""", rid)
            name = 'ref_%s.png' % part
            await page.screenshot(path=os.path.join(OUT, name), clip=box, full_page=True)
            print(name, round(box['width']), 'x', round(box['height']))
        await b.close()
asyncio.run(main())
