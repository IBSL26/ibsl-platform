import asyncio, sys, subprocess, time
from playwright.async_api import async_playwright
PORT=8766
CSS='''#p-lock-overlay,#f1-gate-overlay{display:none!important}
*{font-family:Carlito,Arial,sans-serif!important}
.unit-nav{position:static!important}
.mod-tabs{display:none!important}
.mod-panel{display:block!important;margin-bottom:26px;border-top:1px solid rgba(201,168,76,.3)!important}
.ph-panel{display:grid!important;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:6px}
.ph-tabs{display:none!important}
.ph-panel::before{content:attr(data-tab);grid-column:1/-1;font-size:11px;font-weight:700;letter-spacing:2px;color:#c9a84c}
.dim-panel,.ag-panel{display:block!important;margin-bottom:8px}
.dim-tabs,.ag-tabs{display:none!important}
.dim-panel::before,.ag-panel::before{content:attr(data-tab);display:block;font-size:11px;font-weight:700;letter-spacing:2px;color:#c9a84c;margin-bottom:10px;text-transform:uppercase}
.mod-nav,.send-btn{display:none!important}
.acc,.sub-acc,.port-block,.ref-block,.u2-card,.u2-out,.fac-note-full,.fac-note,.ind-row,.sum-block,.hbox,.quote,.s-row,.slo-box{break-inside:avoid}
.acc-h{break-after:avoid}
html,body{background:#111811!important}
.main{padding:0 6px 20px!important;max-width:none!important}.mod-body{padding:0 20px!important}.mod-hero{padding:22px 20px 16px!important}.unit-header{padding:26px 20px!important}.unit-nav{padding:10px 20px!important}.uh-inner{max-width:none!important}
'''
JS='''()=>{document.querySelectorAll('.acc,.sub-acc,.ind-row,.sum-block').forEach(e=>e.classList.add('open'));
['feedback-acc','msg-acc','upload-acc'].forEach(i=>{var e=document.getElementById(i);if(e)e.style.display='none'});
const lab=(tabsSel,panelSel)=>{document.querySelectorAll(tabsSel).forEach(tb=>{const names=[...tb.children].map(c=>c.innerText.replace(/\\n/g,' · '));let p=tb.nextElementSibling;const ps=p.matches(panelSel)?[p]:[...p.querySelectorAll(panelSel)];let all=p.matches(panelSel)?[]:ps; if(p.matches(panelSel)){let q=p;while(q&&q.matches(panelSel)){all.push(q);q=q.nextElementSibling}} all.forEach((x,i)=>x.setAttribute('data-tab','Tab: '+(names[i]||'')))})};
lab('.ph-tabs','.ph-panel');lab('.dim-tabs','.dim-panel');lab('.ag-tabs','.ag-panel');}'''
async def run(which,out):
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); ctx=await b.new_context(viewport={'width':1180,'height':900}); page=await ctx.new_page()
        async def route(r):
            u=r.request.url
            if u.startswith('http://localhost:%d/'%PORT):
                if u.endswith('/s2r-save.js'): await r.fulfill(path='site/mock-s2r.js', content_type='application/javascript')
                else: await r.continue_()
            else: await r.abort()
        await page.route('**/*', route)
        await page.goto('http://localhost:%d/unit2_m1_lens1_%s.html'%(PORT,which)); await page.wait_for_timeout(700)
        if which=='p': await page.evaluate("appRoleP='CEO';renderAppRoleSel();renderAppForm();")
        await page.add_style_tag(content=CSS); await page.evaluate(JS)
        await page.emulate_media(media='screen')
        await page.pdf(path=out, format='A4', print_background=True, scale=0.78, margin={'top':'8mm','bottom':'8mm','left':'6mm','right':'6mm'})
        await b.close()
async def main():
    srv=subprocess.Popen([sys.executable,'-m','http.server',str(PORT),'--directory','site'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    try:
        await run('p','review/Unit 2 rebuild - Participant page (all parts open).pdf')
        await run('f','review/Unit 2 rebuild - Facilitator page (all parts open).pdf')
    finally: srv.terminate()
import os; os.makedirs('review',exist_ok=True)
asyncio.run(main())
