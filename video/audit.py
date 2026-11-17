from render import *
import matplotlib.text as mt
bad=[]
for nm,sched in (("main",MAIN),("ex",EX),("cred",CRED)):
    for i,(t0,t1,fn,kw) in enumerate(sched):
        T=t1-t0; fig=plt.figure(figsize=(W,H),dpi=DPI); up=fn(fig,T,**kw)
        for tt in (0.0, T*0.5, T-0.05): up(tt)
        r=fig.canvas.get_renderer()
        for t in fig.findobj(mt.Text):
            if not t.get_text().strip() or not t.get_visible() or (t.get_alpha() is not None and t.get_alpha()<0.05): continue
            b=t.get_window_extent(r)
            if b.x0<50 or b.x1>1230 or b.y0<34 or b.y1>686: bad.append((nm,i,fn.__name__,t.get_text()[:40].replace("\n"," "),int(b.x0),int(b.x1),int(b.y0),int(b.y1)))
        plt.close(fig)
for b in bad: print(b)
print("n",len(bad))
