import subprocess, os
from scenes_b import *
from PIL import Image, ImageDraw
from paths import INTERVIEW_CLIPS, build_dir, need
LT = build_dir("lt"); OUT = build_dir("clips")
K=("Alex Kontorovich","Professor of Mathematics\nRutgers University"); G=("Brian Greene","Physicist, Columbia University\nhost")
META={1:(1,[G,K],"Seeing the result"),2:(1,[G],"Changing the question\nabout primes"),3:(2,[G],"What the AI did,\nand did not do"),4:(2,[K],"A moment that can\nonly happen once"),5:(2,[K],"Gauss and his\ntables of primes"),
      6:(2,[K],"Riemann's 1859 paper"),7:(3,[K],"Riemann's notebooks\nand the line ½"),8:(3,[K],"Primes up to a trillion"),9:(4,[K],"The proof of 1896"),10:(4,[K],"The Lean proof checker")}
SEG={1:[(0.0,20.49)],2:[(19.15,37.62)],3:[(2.04,21.66)],4:[(3.30,9.96),(19.03,25.25)],5:[(1.62,10.12),(37.30,59.80)],6:[(25.12,39.60)],7:[(1.52,14.85),(28.65,33.81)],8:[(1.27,5.64),(36.60,52.54)],9:[(1.44,18.80)],10:[(9.78,27.65)]}
m=Image.new("L",(800,450),0);ImageDraw.Draw(m).rounded_rectangle((0,0,799,449),10,fill=255);m.save(LT / "vmask.png")
Image.new("RGBA",(800,4),(255,216,102,255)).save(LT / "bar800.png");Image.new("RGBA",(64,4),(16,20,24,255)).save(LT / "cover.png")
X=0.3;FI=0.8;
import sys
ONLY=[int(a) for a in sys.argv[1:]]
for k,segs in SEG.items():
    if ONLY and k not in ONLY: continue
    sec,people,topic=META[k];fig=plt.figure(figsize=(W,H),dpi=DPI);clip_bg(fig,sec,people,topic);fig.savefig(LT / f"bg{k:02d}.png",dpi=DPI);plt.close(fig)
    src=need(INTERVIEW_CLIPS / f"clip{k:02d}.mp4")
    if len(segs)==1:
        a,b=segs[0];D=b-a;core=f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,fps=24[cv];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS[ca];"
    else:
        (a1,b1),(a2,b2)=segs;d1=b1-a1;D=d1+(b2-a2)-X
        core=(f"[0:v]trim={a1}:{b1},setpts=PTS-STARTPTS,fps=24[v1];[0:v]trim={a2}:{b2},setpts=PTS-STARTPTS,fps=24[v2];[v1][v2]xfade=transition=fade:duration={X}:offset={d1-X}[cv];"
              f"[0:a]atrim={a1}:{b1},asetpts=PTS-STARTPTS[a1];[0:a]atrim={a2}:{b2},asetpts=PTS-STARTPTS[a2];[a1][a2]acrossfade=d={X}:c1=tri:c2=tri[ca];")
    fc=(core+("[cv]crop=iw*0.82:ih*0.82:iw*0.11:ih*0.09,scale=800:450,format=rgba[sv];" if k==1 else "[cv]scale=800:450,format=rgba[sv];")+"[2:v]format=gray[mk];[sv][mk]alphamerge[rv];[1:v][rv]overlay=64:128:shortest=1[a];"
        f"[a][3:v]overlay=x='64-800+800*t/{D}':y=606:shortest=1[b];[b][4:v]overlay=0:606:shortest=1,fade=t=in:d={FI}:color=0x101418,fade=t=out:st={D-FI}:d={FI}:color=0x101418,format=yuv420p[v];"
        f"[ca]afade=t=in:d=0.5,afade=t=out:st={D-0.6}:d=0.6[au]")
    L=lambda p:["-loop","1","-framerate","24","-i",str(p)]
    subprocess.run(["ffmpeg","-v","error","-y","-i",src]+L(LT / f"bg{k:02d}.png")+L(LT / "vmask.png")+L(LT / "bar800.png")+L(LT / "cover.png")+["-filter_complex",fc,"-map","[v]","-map","[au]","-t",f"{D:.3f}",
        "-c:v","libx264","-preset","veryfast","-crf","19","-r","24","-c:a","aac","-ar","44100","-ac","1","-b:a","128k",str(OUT / f"tmp{k:02d}.mp4")],check=True)
    os.replace(OUT / f"tmp{k:02d}.mp4", OUT / f"clip{k:02d}.mp4");print(k,flush=True)
