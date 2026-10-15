import os
from playwright.sync_api import sync_playwright
P='file://'+os.path.abspath('prev/PREVIEW - Unit 8 Participant.html')
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1400,'height':1000},device_scale_factor=3)
    pg.goto(P); pg.wait_for_timeout(900)
    for mod,key,name in [(0,'ref1','r11'),(1,'ref8','r21'),(2,'ref9','r32')]:
        pg.evaluate('showMod(%d,null)'%mod); pg.wait_for_timeout(200)
        pg.evaluate("(()=>{var t=document.getElementById('%s');var a=t.closest('.acc');a.classList.add('open');var r=t.closest('.ref-block');r.style.width='698px';r.style.maxWidth='698px';})()"%key)
        pg.wait_for_timeout(200)
        r=pg.locator('#%s'%key).locator('xpath=ancestor::div[contains(@class,"ref-block")]')
        bb=r.bounding_box(); tb=pg.locator('#%s'%key).bounding_box()
        r.scroll_into_view_if_needed(); bb=r.bounding_box(); tb=pg.locator('#%s'%key).bounding_box()
        pg.screenshot(path='shots/%s.png'%name, clip={'x':bb['x'],'y':bb['y'],'width':bb['width'],'height':tb['y']-bb['y']+2})
    b.close()
