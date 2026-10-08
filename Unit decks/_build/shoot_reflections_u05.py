"""Shoot the reflection boxes of the Unit 5 participant page for the "Section N Reflections" slides.
Usage (cloud workspace): python3 shoot_reflections_u05.py <stand-alone participant page> <u05_data.json> <out folder>
The page is the PREVIEW copy made by rebuild_u05/make_previews.py (it needs no sign-in). Network is blocked.
Each picture shows the reflection label and its question, as on the portal; the file is named after the part (ref_1.1.png …)."""
import asyncio, sys, os, json, pathlib
from playwright.async_api import async_playwright
PAGE, DATA, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
REFL = json.load(open(DATA, encoding='utf-8'))['REFL']
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
        for part, r in REFL.items():
            box = await page.evaluate("""(id)=>{var ta=document.getElementById(id);var blk=ta.closest('.ref-block');var b=blk.getBoundingClientRect();
                var q=blk.querySelector('label[for="'+id+'"]'),p=q.getBoundingClientRect();
                return {x:b.left+window.scrollX,y:b.top+window.scrollY,width:b.width,height:p.bottom-b.top+6,label:blk.querySelector('.ref-label').innerText,prompt:q.textContent}}""", r['id'])
            assert box['prompt'].strip() == r['prompt'], (part, box['prompt'])
            name = 'ref_%s.png' % part
            await page.screenshot(path=os.path.join(OUT, name), clip={k: box[k] for k in ('x', 'y', 'width', 'height')}, full_page=True)
            print(name, '|', box['label'].strip(), '|', box['prompt'][:60], '|', round(box['width']), 'x', round(box['height']))
        await b.close()
asyncio.run(main())
