import numpy as np,subprocess,cv2,sys
from PIL import Image,ImageDraw,ImageFont
V,DY=sys.argv[1],int(sys.argv[2]); SC=float(sys.argv[3]) if len(sys.argv)>3 else 1.0; W,H=1080,1920
fr=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V+'.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout,np.uint8).reshape(-1,H,W,3)
N=fr.shape[0]
dis=np.array(Image.open('dis.png').convert('RGBA')).astype(np.float32)
end=np.array(Image.open('endcard.png').convert('RGB')).astype(np.float32)
def over(img,o,x,y):
    h,w=o.shape[:2]; a=o[...,3:4]/255; img[y:y+h,x:x+w]=img[y:y+h,x:x+w]*(1-a)+o[...,:3]*a
# phone label fix (emoji only)
if V=='em':
    base=fr[120].copy(); fixed=Image.fromarray(base); d=ImageDraw.Draw(fixed)
    d.rectangle((674,1287,798,1315),fill=(251,251,252))
    d.rectangle((729,1215,747,1229),fill=(249,243,241))
    d.line([(732,1222),(736,1227),(745,1216)],fill=(226,72,72),width=3)
    f=ImageFont.truetype('fontp/Pretendard-Medium.otf',24); t='주요 보장'; tw=f.getlength(t)
    d.text((735.5-tw/2,1287),t,font=f,fill=(100,100,104))
    fixed=np.array(fixed)
    R=(660,1205,820,1320)  # x0,y0,x1,y1
    P=fixed[R[1]:R[3],R[0]:R[2]].astype(np.float32)
    T=fr[120,1180:1420,560:920]
def phone_fix(img,i):
    if i>=36: s,dx,dy=1.0,0,0
    else:
        best=(-1,)
        g=fr[i][1050:1550,420:1060]
        for s in np.arange(0.80,1.12,0.01):
            t=cv2.resize(T,None,fx=s,fy=s)
            if t.shape[0]>g.shape[0] or t.shape[1]>g.shape[1]: continue
            r=cv2.matchTemplate(g,t,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(r)
            if mx>best[0]: best=(mx,s,loc)
        mx,s,loc=best
        # template top-left in frame coords
        tx,ty=loc[0]+420,loc[1]+1050
    if i>=36: tx,ty=560,1180
    tf=lambda x,y:((x-560)*s+tx,(y-1180)*s+ty)
    im=Image.fromarray(np.clip(img,0,255).astype(np.uint8)); d=ImageDraw.Draw(im)
    def fillrect(x0,y0,x1,y1):
        X0,Y0=tf(x0,y0);X1,Y1=tf(x1,y1); X0,Y0,X1,Y1=int(X0),int(Y0),int(np.ceil(X1)),int(np.ceil(Y1))
        ring=np.concatenate([img[Y0-3:Y0,X0:X1].reshape(-1,3),img[Y1:Y1+3,X0:X1].reshape(-1,3),img[Y0:Y1,X0-3:X0].reshape(-1,3),img[Y0:Y1,X1:X1+3].reshape(-1,3)])
        c=tuple(int(v) for v in np.median(ring,0)); d.rectangle((X0,Y0,X1,Y1),fill=c); return c
    fillrect(676,1289,796,1314)
    fillrect(729,1215,747,1229)
    p=[tf(732,1222),tf(736,1227),tf(745,1216)]; d.line(p,fill=(226,72,72),width=max(2,int(round(3*s))))
    f=ImageFont.truetype('fontp/Pretendard-Medium.otf',max(8,int(round(24*s)))); t='주요 보장'; tw=f.getlength(t)
    cx,cy=tf(735.5,1287); d.text((cx-tw/2,cy),t,font=f,fill=(100,100,104))
    return np.asarray(im).astype(np.float32)
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
