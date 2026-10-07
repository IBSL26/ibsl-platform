"""Shoot the reflection boxes of the Unit 4 participant page for the "Section N Reflections" slides.
Usage (cloud workspace): python3 shoot_reflections_u04.py <stand-alone participant page> <out folder>
The page is the PREVIEW copy made by rebuild_u04/make_previews.py (it needs no sign-in). Network is blocked."""
import asyncio, sys, os, pathlib
from playwright.async_api import async_playwright
PAGE, OUT = sys.argv[1], sys.argv[2]
SHOTS = {'ref1': 'ref_ov.png', 'ref2': 'ref_together.png', 'ref4': 'ref_3.1.png', 'ref5': 'ref_close.png'}
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
        for tid, name in SHOTS.items():
            box = await page.evaluate("""(id)=>{var ta=document.getElementById(id);var blk=ta.closest('.ref-block');var b=blk.getBoundingClientRect();
                var p=blk.querySelector('.ref-prompt').getBoundingClientRect();
                return {x:b.left+window.scrollX,y:b.top+window.scrollY,width:b.width,height:p.bottom-b.top+10,label:blk.querySelector('.ref-block-label').innerText,prompt:blk.querySelector('.ref-prompt').innerText}}""", tid)
            await page.screenshot(path=os.path.join(OUT, name), clip={k: box[k] for k in ('x', 'y', 'width', 'height')}, full_page=True)
            print(name, '|', box['label'], '|', box['prompt'][:70], '|', round(box['width']), 'x', round(box['height']))
        await b.close()
asyncio.run(main())
