import subprocess,os,sys
from render import MAIN, EX
from paths import BUILD, NARRATION_MAIN, NARRATION_EX, need
OUT=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else str(BUILD/"base.mp4")
NM=need(NARRATION_MAIN); NE=need(NARRATION_EX)
BUILD.mkdir(parents=True,exist_ok=True); os.chdir(BUILD)  # all intermediate files live in BUILD
def run(a): subprocess.run(a,check=True)
def cat(prefix,n,out):
    open("l.txt","w").write("".join(f"file 'seg/{prefix}{i:03d}.mp4'\n" for i in range(n)))
    run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i","l.txt","-c","copy",out])
cat("main",len(MAIN),"main_visual.mp4"); cat("ex",len(EX),"ex_visual.mp4")
A=["-c:a","aac","-ar","44100","-ac","1","-b:a","128k"]
MUTE="volume='clip(max((234.62-t)/0.04\,(t-236.5)/0.04)\,0\,1)*clip(max((423.34-t)/0.04\,(t-424.12)/0.04)\,0\,1)':eval=frame"
run(["ffmpeg","-v","error","-y","-i","main_visual.mp4","-i",NM,"-map","0:v","-map","1:a","-c:v","copy","-af",MUTE]+A+["-shortest","main_av.mp4"])
run(["ffmpeg","-v","error","-y","-i","ex_visual.mp4","-i",NE,"-map","0:v","-map","1:a","-c:v","copy"]+A+["-t","262.9","ex_av.mp4"])
enc=["-c:v","libx264","-preset","veryfast","-crf","19","-pix_fmt","yuv420p","-r","24"]+A
C=lambda n:need(f"clips/clip{n:02d}.mp4")
cuts=[(69.13,C(1)),(143.27,C(2)),(164.13,C(3)),(174.68,C(4)),(185.09,C(5)),(380.95,"ex_av.mp4"),(393.17,C(6)),(470.09,C(7)),(495.67,C(8)),(560.83,C(9)),(655.66,C(10))]
os.makedirs("finB",exist_ok=True);parts=[];prev=0;F=0.5
for k,(c,ins) in enumerate(cuts):
    d=c-prev;p=f"finB/m{k:02d}.mp4"
    vf=f"fade=t=out:st={d-F}:d={F}:color=0x101418"+(f",fade=t=in:d={F}:color=0x101418" if k else "")
    run(["ffmpeg","-v","error","-y","-ss",str(prev),"-t",str(d),"-i","main_av.mp4","-vf",vf]+enc+[p]);parts.append(p)
    q=f"finB/i{k:02d}.mp4"
    if ins=="ex_av.mp4":
        D=262.9;run(["ffmpeg","-v","error","-y","-i",ins,"-vf",f"fade=t=in:d=1.0:color=0x101418,fade=t=out:st={D-1.0}:d=1.0:color=0x101418","-af",f"afade=t=in:d=0.3,afade=t=out:st={D-0.5}:d=0.5"]+enc+[q])
    else: run(["ffmpeg","-v","error","-y","-i",ins]+enc+[q])
    parts.append(q);prev=c
d=737.0-prev;p="finB/m11.mp4";run(["ffmpeg","-v","error","-y","-ss",str(prev),"-t",str(d),"-i","main_av.mp4","-vf",f"fade=t=in:d={F}:color=0x101418,fade=t=out:st={d-1.2}:d=1.2:color=0x101418","-af",f"afade=t=out:st={d-0.3}:d=0.3"]+enc+[p]);parts.append(p)
p="finB/cred.mp4";run(["ffmpeg","-v","error","-y","-i","seg/cred000.mp4","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-vf","fade=t=in:d=1.0:color=0x101418,fade=t=out:st=14.5:d=1.5:color=0x101418","-shortest"]+enc+[p]);parts.append(p)
open("finB/list.txt","w").write("".join(f"file '{os.path.basename(x)}'\n" for x in parts))
run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i","finB/list.txt","-c","copy","finB/tmp.mp4"])
run(["ffmpeg","-v","error","-y","-i","finB/tmp.mp4","-c:v","libx264","-preset","veryfast","-crf","24","-maxrate","2000k","-bufsize","4000k","-pix_fmt","yuv420p","-af","loudnorm=I=-16:TP=-1.5:LRA=11","-c:a","aac","-b:a","128k","-ar","44100","-movflags","+faststart","finB/out_tmp.mp4"])
os.replace("finB/out_tmp.mp4",OUT)
