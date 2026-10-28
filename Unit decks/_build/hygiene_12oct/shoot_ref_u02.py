# -*- coding: utf-8 -*-
"""Unit 2 deck, "Section 4 Reflections": picture of the reflection of part 4.2 (label "Reflection — Integration"), from the participant page.
Usage: python3 shoot_ref_u02.py <participant page> <out.png>"""
import asyncio, sys, pathlib
from playwright.async_api import async_playwright
PAGE, OUT = sys.argv[1], sys.argv[2]
CSS = ('.mod-panel{display:block!important}.acc-b{display:block!important;max-height:none!important}'
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
        box = await page.evaluate("""()=>{var blk=[...document.querySelectorAll('.ref-block')].find(function(b){return /Reflection\\s*—\\s*Integration/i.test(b.innerText);});
            var b=blk.getBoundingClientRect(),q=blk.querySelector('.ref-prompt').getBoundingClientRect();
            return {x:b.left+window.scrollX,y:b.top+window.scrollY,width:b.width,height:q.bottom-b.top+10,label:blk.innerText.slice(0,60)}}""")
        await page.screenshot(path=OUT, clip={k: box[k] for k in ('x', 'y', 'width', 'height')}, full_page=True)
        print(OUT, box)
        await b.close()
asyncio.run(main())
