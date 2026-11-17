from render import *
import numpy as np
def frame(fig):
    fig.canvas.draw(); a=np.asarray(fig.canvas.buffer_rgba())[...,:3].astype(int); return a
base=None
for nm,sched in (("main",MAIN),("ex",EX),("cred",CRED)):
    for i,(t0,t1,fn,kw) in enumerate(sched):
        T=t1-t0; fig=plt.figure(figsize=(W,H),dpi=40); up=fn(fig,T,**kw); out=[]
        for tt in np.arange(0.4,T,1.0):
            up(tt); a=frame(fig); body=a[30:,:]   # skip header band
            lum=body.max(axis=2); n=(lum>70).sum()/lum.size*100
            out.append((round(float(tt),1),round(n,2)))
        plt.close(fig)
        sparse=[o for o in out if o[1]<0.25]
        if sparse: print(nm,i,fn.__name__,f"T={T:.0f}","sparse:",sparse[:12])
