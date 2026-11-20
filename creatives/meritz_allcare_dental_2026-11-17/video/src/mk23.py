import subprocess,numpy as np,cv2
from PIL import Image
W,H=1080,1920
nt=np.array(Image.open('nt.png').convert('RGBA')).astype(np.float32); na=nt[...,3:4]/255.; nc=nt[...,:3]
rw=np.array(Image.open('row3.png').convert('RGBA')).astype(np.float32); R3Y=848
inc=[(b-59)/(246-59) for b in [74,127,166,196,218,231,240,244,246]]
outc=[(b-89)/(246-89) for b in [239,221,180,131,103,91,89]]
def row_alpha(i):
    if i<512: return 0
    if i<512+len(inc): return inc[i-512]
    if i<552: return 1
    if i<552+len(outc): return max(0,outc[i-552])
    return 0
A,F=491,10
ys=np.arange(H,dtype=np.float32)
def ss(x): x=np.clip(x,0,1); return x*x*(3-2*x)
g=ss((ys-1540)/135)[:,None,None]
def dark(i):
    if i<553: return 0.5
    if i<=561: return 0.5+(0.28-0.5)*(i-553)/8
    return 0.28
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def outk(i): return 1.0 if i<=656 else max(0.0,(663-i)/7)
d16=subprocess.Popen(['ffmpeg','-loglevel','error','-i','v16.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
d21=subprocess.Popen(['ffmpeg','-loglevel','error','-i','v21c.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-i','v16.mp4','-map','0:v','-map','1:a','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','medium','-c:a','copy','-shortest','v23.mp4'],stdin=subprocess.PIPE)
i=0
while True:
    b=d16.stdout.read(W*H*3); c=d21.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    if i<486 or i>663:
        enc.stdin.write(c); i+=1; continue
    f=np.frombuffer(b,np.uint8).reshape(H,W,3).copy()
    a=row_alpha(i)
    if a>0:
        off=int(round(12*(1-a))); r=np.zeros_like(rw); r[:,off:]=rw[:,:W-off] if off else rw
        al=r[...,3:4]/255.*a; f[R3Y:R3Y+142]=(f[R3Y:R3Y+142]*(1-al)+r[...,:3]*al).astype(np.uint8)
    reg=f[1700:1850]; lum=reg.mean(axis=2).astype(np.uint8); bg=cv2.medianBlur(lum,41)
    mm=((lum.astype(int)-bg.astype(int))>6).astype(np.uint8)*255
    if mm.any():
        m=np.zeros((H,W),np.uint8); m[1700:1850]=mm
        f=cv2.inpaint(f,cv2.dilate(m,np.ones((11,11),np.uint8)),7,cv2.INPAINT_TELEA)
    orig=f.copy()
    if i>=A:
        k=ease((i-A+1)/F); d=dark(i)*k
        sub=f[1450:].astype(np.float32)*(1-d*g[1450:])
        sub=sub*(1-na[1450:]*k)+nc[1450:]*na[1450:]*k
        f[1450:]=np.clip(sub,0,255).astype(np.uint8)
    o=outk(i)
    if o<1: f=(orig*(1-o)+f*o).astype(np.uint8)
    enc.stdin.write(f.tobytes()); i+=1
enc.stdin.close(); enc.wait(); print('frames',i)
