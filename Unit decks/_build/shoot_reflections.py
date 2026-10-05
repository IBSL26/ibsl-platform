"""Shoot the reflection boxes of the Unit 2 participant page for the "Section N Reflections" slides.
Usage (cloud workspace, from the folder that holds site/): python3 shoot_reflections.py <site folder> <out folder>
The site folder holds unit2_m1_lens1_p.html, style.css, logo.png and a stand-in s2r-save.js (mock-s2r.js). Network is blocked."""
import asyncio, sys, subprocess, time, os
from playwright.async_api import async_playwright
SITE, OUT = sys.argv[1], sys.argv[2]
PORT = 8781
SHOTS = {'ref1': 'ref_1.1.png', 'ref2': 'ref_1.2.png', 'ref6': 'ref_2.1.png', 'ref4': 'ref_3.1.png', 'app_ref_final': 'ref_5.2.png'}
CSS = ('#p-lock-overlay{display:none!important}.mod-panel{display:block!important}.acc-b,.sub-acc-b{display:block!important;max-height:none!important}'
       '*{font-family:Carlito,Arial,sans-serif!important}')
async def main():
    srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(PORT), '--directory', SITE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    try:
        async with async_playwright() as pw:
            b = await pw.chromium.launch()
            ctx = await b.new_context(viewport={'width': 860, 'height': 1200}, device_scale_factor=3)
            page = await ctx.new_page()
            async def route(r):
                u = r.request.url
                if u.startswith('http://localhost:%d/' % PORT):
                    if u.endswith('/s2r-save.js'): await r.fulfill(path=os.path.join(SITE, 'mock-s2r.js'), content_type='application/javascript')
                    else: await r.continue_()
                else: await r.abort()
            await page.route('**/*', route)
            await page.goto('http://localhost:%d/unit2_m1_lens1_p.html' % PORT); await page.wait_for_timeout(800)
            await page.add_style_tag(content=CSS); await page.wait_for_timeout(300)
            os.makedirs(OUT, exist_ok=True)
            for tid, name in SHOTS.items():
                box = await page.evaluate("""(id)=>{var ta=document.getElementById(id);var blk=ta.closest('.ref-block');var h=blk.querySelector('.ref-head').getBoundingClientRect();
                    var p=blk.querySelector('.ref-prompt').getBoundingClientRect();return {x:h.left+window.scrollX,y:h.top+window.scrollY,width:h.width,height:p.bottom-h.top,label:blk.querySelector('.ref-label').innerText,prompt:blk.querySelector('.ref-prompt').innerText}}""", tid)
                await page.screenshot(path=os.path.join(OUT, name), clip={k: box[k] for k in ('x', 'y', 'width', 'height')}, full_page=True)
                print(name, '|', box['label'], '|', box['prompt'][:70], '|', round(box['width']), 'x', round(box['height']))
            await b.close()
    finally: srv.terminate()
asyncio.run(main())
