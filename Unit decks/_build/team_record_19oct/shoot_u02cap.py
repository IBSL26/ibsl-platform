import asyncio,os
from playwright.async_api import async_playwright
P='file://'+os.path.abspath('/home/claude/w/preview/PREVIEW - Unit 2 Participant.html')
CSS='#p-lock-overlay{display:none!important}*{font-family:Carlito,Arial,sans-serif!important}'
async def m():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        ctx=await b.new_context(viewport={'width':1100,'height':1400},device_scale_factor=2)
        pg=await ctx.new_page(); await pg.goto(P); await pg.wait_for_timeout(1500)
        await pg.add_style_tag(content=CSS)
        await pg.evaluate("showMod(4)"); await pg.wait_for_timeout(400)
        await pg.select_option('#twScribe','preview'); await pg.wait_for_timeout(600)
        await pg.evaluate("""()=>{const w=document.createTreeWalker(document.getElementById('u2bTeam'),NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){n.nodeValue=n.nodeValue.replace('You (preview)','Member One').replace('Second member','Member Two').replace('Preview group','Group 1');}
            document.querySelectorAll('#twScribe option').forEach(o=>{o.textContent=o.textContent.replace('You (preview)','Member One').replace('Second member','Member Two');});}""")
        # portal picture: group bar to the step tabs
        box=await pg.evaluate("""()=>{const a=document.getElementById('u2bTeam').getBoundingClientRect();const t=document.querySelector('#u2bTool .step-tabs').getBoundingClientRect();
            return {x:a.left+scrollX,y:a.top+scrollY,width:a.width,height:t.bottom-a.top}}""")
        await pg.screenshot(path='shots/portal_5_1.png',clip=box,full_page=True); print('portal',box)
        box=await pg.evaluate("""()=>{const blk=document.getElementById('app_ref_final').closest('.ref-block');const h=blk.querySelector('.ref-head').getBoundingClientRect();const p=blk.querySelector('.ref-prompt').getBoundingClientRect();
            return {x:h.left+scrollX,y:h.top+scrollY,width:h.width,height:p.bottom-h.top,label:blk.querySelector('.ref-label').innerText}}""")
        print('ref',box)
        await pg.screenshot(path='shots/ref_5.1.png',clip={k:box[k] for k in ('x','y','width','height')},full_page=True)
        await b.close()
asyncio.run(m())
