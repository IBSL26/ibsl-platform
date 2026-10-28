import sys, os, json, mimetypes, re
from playwright.sync_api import sync_playwright
site, names, shots = sys.argv[1], sys.argv[2].split(','), sys.argv[3]
FAKE='/mnt/user-data/uploads/ibsl-platform/Unit decks/_build/rebuild_u06/fake-supabase.js'
LENS={'unit1':'u1_foundations','unit2_m1_lens1':'u2m1_lens1','unit2_m1_lens2':'u2m1_lens2','unit2_m1_lens3':'u2m1_lens3','unit3_m1_lens4':'u3m1_lens4','unit3_m1_lens5':'u3m1_lens5','unit3_m1_lens6':'u3m1_lens6'}
O='http://portal.test'
os.makedirs(shots, exist_ok=True)
res={}
with sync_playwright() as p:
    b=p.chromium.launch()
    for name in names:
        ctx=b.new_context(viewport={'width':1300,'height':900})
        def route(r):
            u=r.request.url
            if 'supabase-js' in u: return r.fulfill(path=FAKE, content_type='application/javascript')
            if u.startswith(O+'/'):
                f=os.path.join(site,u[len(O)+1:].split('?')[0])
                if u.endswith('blank.html'): return r.fulfill(body='<html></html>',content_type='text/html')
                if os.path.isfile(f): return r.fulfill(path=f, content_type=(mimetypes.guess_type(f)[0] or 'text/html')+'; charset=utf-8')
                f2=os.path.join('/mnt/user-data/uploads/ibsl-platform',u[len(O)+1:].split('?')[0])
                if os.path.isfile(f2): return r.fulfill(path=f2, content_type=(mimetypes.guess_type(f2)[0] or 'text/html')+'; charset=utf-8')
                return r.fulfill(status=404,body='')
            return r.abort()
        ctx.route('**/*',route)
        pg=ctx.new_page(); errs=[]
        pg.on('pageerror',lambda e: errs.append(str(e)[:200]))
        pg.on('dialog',lambda d: d.dismiss())
        pg.goto(O+'/blank.html')
        lens=[v for k,v in LENS.items() if name.startswith(k)][0]
        seed={'profiles':[{'id':'u-1','role':'facilitator' if name.lower().endswith('_f.html') else 'participant','full_name':'Test'}],
              'cohort_memberships':[{'profile_id':'u-1','cohort_id':'c-1','role_in_cohort':'participant','joined_at':'2026-09-01'}],
              'lens_progress':[{'profile_id':'u-1','cohort_id':'c-1','lens_id':lens,'status':'unlocked'}],'lens_responses':[],'submissions':[],'lens_catalog':[]}
        pg.evaluate("(s)=>{localStorage.clear();localStorage.setItem('fakedb',JSON.stringify(s));localStorage.setItem('fake_uid','u-1');}",seed)
        pg.goto(O+'/'+name); pg.wait_for_timeout(1500)
        pg.evaluate("document.querySelectorAll('[id$=lock-overlay]').forEach(e=>e.style.display='none')")
        pg.screenshot(path=os.path.join(shots,name.replace('.html','')+'_hdr.png'),clip={'x':0,'y':0,'width':1300,'height':90})
        tabs=pg.evaluate("[...document.querySelectorAll('.mod-tab,.tab-btn')].map(e=>e.innerText.replace(/\\s+/g,' ').trim())")
        panels=pg.evaluate("[...document.querySelectorAll('.mod-panel,.mod')].length")
        secs=[]
        for i in range(panels):
            pg.evaluate("showMod(%d)"%i); pg.wait_for_timeout(120)
            info=pg.evaluate("""(()=>{const m=[...document.querySelectorAll('.mod-panel,.mod')].find(x=>x.classList.contains('active'));if(!m)return null;
              const lab=(m.querySelector('.mod-hero-label,.mod-badge')||{}).innerText||'';const h2=(m.querySelector('.mod-hero h2,.mod-title')||{}).innerText||'';
              const parts=[...m.querySelectorAll('.acc-t')].map(e=>e.innerText.trim().slice(0,40));
              const nav=[...m.querySelectorAll('.mod-nav button')].map(b=>b.innerText.trim()+' >'+(b.getAttribute('onclick')||''));
              const slo=[...m.querySelectorAll('.slo-box li')].map(e=>e.innerText.slice(0,40));
              return {id:m.id,lab,h2:h2.slice(0,60),parts,nav,slo}})()""")
            secs.append(info)
        # nav buttons go where they say
        bad=[]
        for i,s in enumerate(secs):
            for n in s['nav']:
                m=re.match(r'.*Section (\d).*>showMod\((\d)\)',n)
                if m:
                    tgt=int(m.group(2)); lab=secs[tgt]['lab']
                    if ('Section '+m.group(1)) not in lab: bad.append((s['id'],n,lab))
        res[name]={'errs':errs,'tabs':tabs,'secs':secs,'navbad':bad}
        ctx.close()
    b.close()
print(json.dumps(res,ensure_ascii=False,indent=0)[:200000])
