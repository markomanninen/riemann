import numpy as np, soundfile as sf, subprocess, json, os, sys, glob
from paths import BUILD, SOURCES, need
SR=44100
BASE=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else str(BUILD/"base.mp4")
os.chdir(BUILD); os.makedirs("audio",exist_ok=True)  # intermediate files live in BUILD
# Music and effects from SOURCES/music, converted once to 44.1 kHz stereo WAV
STEMS={"music_1_main_theme":"Riemann 1.*","music_2_tension":"Riemann 2.*","music_3_breakthrough":"Riemann 3.*",
       "sfx_tick":"Single_soft_muted_ti*","sfx_whoosh":"Low_soft_whoosh*","sfx_bell":"Single_soft_glass_be*"}
for name,pat in STEMS.items():
    dst=f"audio/{name}_44.wav"
    if os.path.exists(dst): continue
    hits=sorted(glob.glob(str(SOURCES/"music"/pat)))
    if not hits: need(SOURCES/"music"/pat)
    subprocess.run(["ffmpeg","-v","error","-y","-i",hits[0],"-ar",str(SR),"-ac","2",dst],check=True)
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
cuts=[69.13,143.27,164.13,174.68,185.09,380.95,393.17,470.09,495.67,560.83,655.66]
clipn=[1,2,3,4,5,None,6,7,8,9,10]
PAUSE=1.2  # must match assemble.py
ins=[262.9+PAUSE if n is None else dur(need(f"clips/clip{n:02d}.mp4")) for n in clipn]
def F(t): return t+sum(d for c,d in zip(cuts,ins) if c<t-1e-6)
EX0=380.95+sum(ins[:5]); E=lambda t:EX0+PAUSE+t  # excursion narration time -> final time
TOTAL=dur(need(BASE)); N=int(TOTAL*SR)+SR
clip_iv=[(c+sum(ins[:k]),c+sum(ins[:k])+ins[k]) for k,c in enumerate(cuts) if clipn[k] is not None]
def load(p):
    x,sr=sf.read(p,dtype="float32"); assert sr==SR; return x if x.ndim==2 else np.c_[x,x]
def norm_peak(x,db): return x*(10**(db/20)/np.abs(x).max())
# The tick source is very quiet, so a higher gain would lift its noise floor with it
SFX={"tick":norm_peak(load("audio/sfx_tick_44.wav"),-27),"whoosh":norm_peak(load("audio/sfx_whoosh_44.wav"),-12),"bell":norm_peak(load("audio/sfx_bell_44.wav"),-15)}
ev=[]
A=lambda k,t,g=0: ev.append((k,t,g))
for t in (48,149,398,538,662): A("whoosh",F(t)-0.15)
A("whoosh",E(0)-1.7,-3); A("whoosh",F(381)-0.2,-3); A("whoosh",F(737)+0.3,-3)
for t in (80.5,216.5,313.5,472.8,531.3,626,712.5,728.2): A("bell",F(t))
A("bell",E(74),-3); A("bell",E(242),-3)
for i in range(10): A("tick",F(95)+i*0.5)
for i in range(0,20,2): A("tick",F(276)+i*6.5/20,-2)
for i in range(10): A("tick",F(473.6)+i*0.7,-1)
for i in range(11): A("tick",F(509.3)+i*0.45,-4); A("tick",F(515.3)+i*0.45,-4)
for t in (1,6.5,10,14.5,16.2,17.8,19.4,21): A("tick",F(561)+t,-2)
sfx=np.zeros((N,2),np.float32)
for k,t,g in ev:
    x=SFX[k]*10**(g/20); i=int(t*SR)
    if 0<=i<N-len(x): sfx[i:i+len(x)]+=x
# ---- music
def loop(x,length,xf=4.0):
    n=int(xf*SR); out=x.copy(); fo=np.linspace(1,0,n)[:,None]; fi=1-fo
    while len(out)<length:
        out=np.vstack([out[:-n],out[-n:]*fo+x[:n]*fi,x[n:]])
    return out[:length]
M=[load(f"audio/music_{n}_44.wav") for n in ("1_main_theme","2_tension","3_breakthrough")]
M[2]=M[2]*10**(-5/20)  # the breakthrough track is mastered louder than the other two
plan=[(0,F(398),0),(F(398),F(538),1),(F(538),F(662),2),(F(662),F(737)+0.5,0),(F(737)+0.5,TOTAL,2)]
# excursion uses tension track
plan=[(0,E(0),0),(E(0),E(262.9),1),(E(262.9),F(398),0)]+plan[1:]
music=np.zeros((N,2),np.float32); XF=3.0
for a,b,m in plan:
    i0=int(max(0,a-XF/2)*SR); i1=min(N,int((b+XF/2)*SR)); seg=loop(M[m],i1-i0).copy(); n=int(XF*SR)
    seg[:n]*=np.linspace(0,1,n)[:,None]; seg[-n:]*=np.linspace(1,0,n)[:,None]; music[i0:i1]+=seg
env=np.full(N,10**(-13/20),np.float32); r=int(0.8*SR)
for n,(a,b) in enumerate(clip_iv):
    i0,i1=int(a*SR),int(b*SR); env[i0:i1]=0.0 if n==0 else 10**(-19.5/20)
k=np.ones(r)/r; env=np.convolve(env,k,mode="same")
music*=env[:,None]; e=int(4*SR); music[int(TOTAL*SR)-e:int(TOTAL*SR)]*=np.linspace(1,0,e)[:,None]; music[int(TOTAL*SR):]=0
music[:int(1.5*SR)]*=np.linspace(0,1,int(1.5*SR))[:,None]
sf.write("audio/bed_music.wav",music,SR); sf.write("audio/bed_sfx.wav",sfx,SR)
json.dump({"events":ev,"plan":plan,"clips":clip_iv},open("audio/cues.json","w"))
print(len(ev),"events",round(TOTAL,1))
