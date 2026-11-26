import subprocess,numpy as np,cv2,json,math
from PIL import Image
W,H,F=1080,1920,30
def L(p): return np.array(Image.open(p).convert('RGBA')).astype(np.float32)
def R(p): return cv2.cvtColor(cv2.imread(p),cv2.COLOR_BGR2RGB)
frame=L('B_frame.png'); NT={k:L(f'B_nt{k}.png') for k in 'DNP'}
cap=json.load(open('capB.json')); CB=[L(f'cb{i:02d}.png') for i in range(len(cap))]
src={k:R(f'nb/{k}_p.png') for k in ['feed','post','cmts','info','upd']}
src['m2']=cv2.resize(R('m2.png'),(1080,1080)); src['m3']=cv2.resize(R('m3.png'),(1080,1080)); src['m1']=cv2.resize(R('m1.png'),(1080,1080)); src['cta']=R('nb/cta.png')
legal=np.array(Image.open('legal.png').convert('RGB').resize((W,H)))
wc=np.array(Image.open('wcard.png').convert('RGB')).astype(np.float32)
prevf=None
# scene: (start,end,src,crop0,crop1,highlights[(t,x,y,w,h)],note,shake)
S=[(0,3.0,'feed',(0,0,1080),(0,150,900),[(1.0,10,364,1060,158)],'D',0),
(3.0,6.8,'post',(0,0,1080),(0,60,980),[],'D',0),
(6.8,9.9,'post',(0,480,760),(20,560,640),[(7.6,97,800,375,112)],'D',0),
(9.9,14.9,'cmts',(0,0,1080),(0,40,1000),[(10.2,20,200,1040,180),(12.3,20,383,1040,180)],'D',0),
(14.9,17.7,'cmts',(0,420,1000),(0,520,880),[(15.2,20,749,1040,180)],'D',0),
(17.7,23.0,'info',(0,0,1080),(0,120,960),[(20.9,680,428,360,250)],'N',0),
(23.0,26.0,'upd',(0,0,1080),(0,200,860),[(23.5,72,556,460,62)],'P',0),
(26.0,29.5,'m2',(0,0,1080),(90,90,900),[],'D',0),
(29.5,32.3,'m3',(0,0,1080),(60,60,960),[],'D',1),
(32.3,34.0,'cta',(0,0,1080),(20,20,1040),[],'N',0)]
def over(img,o,k=1.0):
    a=o[...,3:4]/255.*k; return img*(1-a)+o[...,:3]*a
def ease(x): x=min(1,max(0,x)); return x*x*(3-2*x)
enc=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','vb2.mp4'],stdin=subprocess.PIPE)
for i in range(int(37.0*F)):
    t=i/F
    if t>=34.0: enc.stdin.write(legal.tobytes()); continue
    if t>=32.3:
        k=min(1,(t-32.3)/0.3); fr_=wc if prevf is None else prevf*(1-k)+wc*k
        enc.stdin.write(np.clip(fr_,0,255).astype(np.uint8).tobytes()); continue
    s=[x for x in S if x[0]<=t<x[1]][0]; a,b,k,c0,c1,hl,nt,sh=s; p=ease((t-a)/(b-a))
    x=c0[0]+(c1[0]-c0[0])*p; y=c0[1]+(c1[1]-c0[1])*p; w=c0[2]+(c1[2]-c0[2])*p
    im=src[k]; sc=1080/w
    M=np.float32([[sc,0,-x*sc],[0,sc,-y*sc]])
    if sh and t-a<0.5: M[0,2]+=14*math.sin((t-a)*60)*(1-(t-a)/0.5)
    box=cv2.warpAffine(im,M,(1080,1080),borderMode=cv2.BORDER_CONSTANT,borderValue=(255,255,255)).astype(np.float32)
    for (ht,hx,hy,hw,hh) in hl:
        if t>=ht:
            k2=min(1,(t-ht)/0.15)
            p1=(int((hx-x)*sc),int((hy-y)*sc)); p2=(int((hx+hw-x)*sc),int((hy+hh-y)*sc))
            ov=box.copy(); cv2.rectangle(ov,p1,p2,(235,30,30),max(5,int(7*sc/1.2))); box=box*(1-k2)+ov*k2
    lf=(t-a)*F
    f=np.zeros((H,W,3),np.float32); f[400:1480]=box
    if lf<4 and s is not S[0]:
        pass
    f=over(f,frame); f=over(f,NT[nt])
    ci=[j for j,(u,v) in enumerate(cap) if u-0.05<=t<v+0.05]
    if ci: f=over(f,CB[ci[0]])
    prevf=f
    enc.stdin.write(np.clip(f,0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
