import asyncio, sys, os, json, pathlib
from playwright.async_api import async_playwright
JOBS = {'u5': ('w/unit3_m1_lens4_p.html', {'4.2': 'ref9'}),
        'u6': ('w/unit3_m1_lens5_p.html', {'1.2': 'ref13', '1.3': 'ref14', '1.4': 'ref15'}),
        'u7': ('w/unit3_m1_lens6_p.html', {'1.1': 'ref1', '1.2': 'ref2', '1.3': 'ref3', '1.4': 'ref8', '2.1': 'ref4', '2.2': 'ref5'})}
CSS = ('.mod,.mod-panel{display:block!important}.acc-b{display:block!important;max-height:none!important}'
       'body>div[style*="position:fixed"],#gate,.gate{display:none!important}*{font-family:Carlito,Arial,sans-serif!important}'
       '.u6-pf{display:none!important}')
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        for u, (page_f, refl) in JOBS.items():
            ctx = await b.new_context(viewport={'width': 860, 'height': 1200}, device_scale_factor=3)
            page = await ctx.new_page()
            await page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
            await page.goto(pathlib.Path(page_f).resolve().as_uri()); await page.wait_for_timeout(800)
            await page.add_style_tag(content=CSS)
            await page.evaluate("document.querySelectorAll('.acc').forEach(function(a){a.classList.add('open');})"); await page.wait_for_timeout(400)
            for part, rid in refl.items():
                box = await page.evaluate("""(id)=>{var ta=document.getElementById(id);var blk=ta.closest('.ref-block');var b=blk.getBoundingClientRect();var t=ta.getBoundingClientRect();
                    return {x:b.left+window.scrollX,y:b.top+window.scrollY,width:b.width,height:t.top-b.top+4,label:blk.querySelector('.ref-label').innerText}}""", rid)
                name = f'pics/{u}_ref_{part}.png'
                await page.screenshot(path=name, clip={k: box[k] for k in ('x','y','width','height')}, full_page=True)
                print(name, round(box['width']), 'x', round(box['height']), '|', box['label'])
            await ctx.close()
        await b.close()
asyncio.run(main())
