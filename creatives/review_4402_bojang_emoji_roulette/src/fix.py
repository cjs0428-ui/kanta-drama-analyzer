import numpy as np,subprocess,cv2,sys
from PIL import Image,ImageDraw,ImageFont
V,DY=sys.argv[1],int(sys.argv[2]); SC=float(sys.argv[3]) if len(sys.argv)>3 else 1.0; W,H=1080,1920
fr=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V+'.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout,np.uint8).reshape(-1,H,W,3)
N=fr.shape[0]
dis=np.array(Image.open('dis.png').convert('RGBA')).astype(np.float32)
end=np.array(Image.open('endcard.png').convert('RGB')).astype(np.float32)
def over(img,o,x,y):
    h,w=o.shape[:2]; a=o[...,3:4]/255; img[y:y+h,x:x+w]=img[y:y+h,x:x+w]*(1-a)+o[...,:3]*a
# phone screen replacement (emoji only) with regenerated high-res screen
if V=='em':
    P2=np.array(Image.open('pe1_aligned_2x.png').convert('RGB')).astype(np.float32)  # 900x1600 = crop(450x800) at 2x
    mk=np.zeros((1600,900),np.float32); mk[24:-24,24:-24]=1; mk=cv2.GaussianBlur(mk,(0,0),10)
    T=fr[120,1180:1420,560:920]
def phone_fix(img,i):
    if i>=36: s,tx,ty=1.0,560,1180
    else:
        best=(-1,)
        g=fr[i][1050:1550,420:1060]
        for s_ in np.arange(0.80,1.12,0.01):
            t=cv2.resize(T,None,fx=s_,fy=s_)
            if t.shape[0]>g.shape[0] or t.shape[1]>g.shape[1]: continue
            r=cv2.matchTemplate(g,t,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(r)
            if mx>best[0]: best=(mx,s_,loc)
        _,s,loc=best; tx,ty=loc[0]+420,loc[1]+1050
    # patch pixel (U,V) at 2x -> crop (U/2,V/2) -> frame120 (525+U/2,750+V/2) -> frame i
    M=np.float32([[s/2,0,(525-560)*s+tx],[0,s/2,(750-1180)*s+ty]])
    wp=cv2.warpAffine(P2,M,(W,H),flags=cv2.INTER_AREA if s<1 else cv2.INTER_LINEAR)
    wm=cv2.warpAffine(mk,M,(W,H))[...,None]
    core=wm[...,0]>0.95
    if i<36 and core.sum()>100:
        gain=np.median(img[core],0)/np.maximum(np.median(wp[core],0),1); wp=wp*gain[None,None,:]
    return img*(1-wm)+wp*wm
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-i',V+'.mp4','-map','0:v','-map','1:a','-c:v','libx264','-crf','16','-pix_fmt','yuv420p','-c:a','copy','-shortest',V+'_fix.mp4'],stdin=subprocess.PIPE)
FS,FE=180,189
last_scene=None
for i in range(N):
    if i<FS:
        img=fr[i].astype(np.float32)
        if V=='em': img=phone_fix(img,i)
        img[0:118]=253
        if SC!=1.0:
            M=np.float32([[SC,0,(1-SC)*540],[0,SC,(1-SC)*H]]); sh=cv2.warpAffine(img,M,(W,H),borderMode=cv2.BORDER_REPLICATE,flags=cv2.INTER_AREA)
            sh[:int((1-SC)*H)+2]=253
        else:
            sh=np.empty_like(img); sh[DY:]=img[:H-DY]; sh[:DY]=img[0:1]
        over(sh,dis,0,0); last_scene=sh; out=sh
    elif i<FE:
        a=(i-FS+1)/(FE-FS+1); out=last_scene*(1-a)+end*a
    else: out=end
    enc.stdin.write(np.clip(out,0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print(V,'done',N)
