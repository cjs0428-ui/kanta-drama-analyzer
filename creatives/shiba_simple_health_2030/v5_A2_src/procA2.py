import cv2,numpy as np,os
from PIL import Image
os.makedirs('kB',exist_ok=True)
def rgba(f): return np.asarray(Image.open(f).convert('RGBA')).astype(float)
def L(i): return cv2.imread(f'f/{i:04d}.png').astype(float)
def over(a,P):  # P RGBA (RGB order) -> a BGR
    al=P[...,3:4]/255;return a*(1-al)+P[...,2::-1]*al
# caption
O=np.asarray(Image.open('old_t.png').convert('RGBA'));NC=rgba('newA2_t.png')
cmask=cv2.dilate((O[...,3]>12).astype(np.uint8)*255,np.ones((9,9),np.uint8))
def inpaint_rect(a,m,X0,X1,Y0,Y1,r=6):
    crop=a[Y0:Y1,X0:X1].astype(np.uint8);mm=m[Y0:Y1,X0:X1]
    sm=cv2.resize(crop,None,fx=.5,fy=.5,interpolation=cv2.INTER_AREA);ms=cv2.resize(mm,None,fx=.5,fy=.5,interpolation=cv2.INTER_NEAREST)
    up=cv2.GaussianBlur(cv2.resize(cv2.inpaint(sm,ms,r,cv2.INPAINT_TELEA),(X1-X0,Y1-Y0),interpolation=cv2.INTER_CUBIC),(0,0),2).astype(float)
    mf=cv2.GaussianBlur(mm.astype(float)/255,(0,0),3)[...,None];a[Y0:Y1,X0:X1]=a[Y0:Y1,X0:X1]*(1-mf)+up*mf;return a
# search states
UI={k:rgba(f'ui_{k}.png') for k in ['S0','S1','S2','S3','S4','S5']}
def st(i): return 'S0' if i==99 else 'S1' if i<=107 else 'S2' if i<=114 else 'S3' if i<=122 else 'S4' if i<=129 else 'S5'
REF200=L(200);B211=L(211)
R=(slice(360,1320),slice(240,840))
# cards & pill
def patched(ref,fill,P):
    p=ref.copy();y0,y1,x0,x1=fill;p[y0:y1,x0:x1]=255;return over(p,P)
C1R=L(330);C1P=patched(C1R,(380,560,160,920),rgba('t_c1.png'))
B1=L(318);B2=L(323);C2R=L(338);C2P=patched(C2R,(1080,1260,160,920),rgba('t_c2.png'))
PR=L(385);PP=patched(PR,(595,676,318,762),rgba('t_pill.png'));B366=L(366)
def affrep(a,ref,pat,T,fe=6):
    y0,y1,x0,x1=T;x=ref[y0:y1,x0:x1].reshape(-1);y=a[y0:y1,x0:x1].reshape(-1)
    A=np.vstack([x,np.ones_like(x)]).T;(k,c),*_=np.linalg.lstsq(A,y,rcond=None)
    res=np.sqrt(((y-(k*x+c))**2).mean())
    if k<0.05 or res>14: return a,round(float(k),2),round(float(res),1)
    new=k*pat[y0:y1,x0:x1]+c
    h,w=y1-y0,x1-x0;m=np.ones((h,w))
    for t in range(fe): v=(t+1)/(fe+1);m[t,:]=np.minimum(m[t,:],v);m[-1-t,:]=np.minimum(m[-1-t,:],v);m[:,t]=np.minimum(m[:,t],v);m[:,-1-t]=np.minimum(m[:,-1-t],v)
    a[y0:y1,x0:x1]=a[y0:y1,x0:x1]*(1-m[...,None])+new*m[...,None];return a,round(float(k),2),round(float(res),1)
def homo(a,ref,pat,T):
    y0,y1,x0,x1=T;Y0,Y1,X0,X1=y0-120,y1+120,60,1020
    g1=cv2.cvtColor(ref[y0:y1,x0:x1].astype(np.uint8),cv2.COLOR_BGR2GRAY);g2=cv2.cvtColor(a[Y0:Y1,X0:X1].astype(np.uint8),cv2.COLOR_BGR2GRAY)
    orb=cv2.ORB_create(3000);k1,d1=orb.detectAndCompute(g1,None);k2,d2=orb.detectAndCompute(g2,None)
    if d1 is None or d2 is None or len(k1)<20 or len(k2)<20: return a,False
    ms=sorted(cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True).match(d1,d2),key=lambda m:m.distance)[:300]
    if len(ms)<15: return a,False
    p1=np.float32([k1[m.queryIdx].pt for m in ms]);p2=np.float32([k2[m.trainIdx].pt for m in ms])
    H,inl=cv2.findHomography(p1,p2,cv2.RANSAC,4.0)
    if H is None or inl.sum()<60: return a,False
    diff=(pat[y0:y1,x0:x1]-ref[y0:y1,x0:x1]).astype(np.float32)
    w=cv2.warpPerspective(diff,H,(X1-X0,Y1-Y0));mk=cv2.warpPerspective(np.ones((y1-y0,x1-x0),np.float32),H,(X1-X0,Y1-Y0))
    a[Y0:Y1,X0:X1]+=w*mk[...,None];return a,int(inl.sum())
def diffrep(a,ref,pat,rect,tol=30):
    y0,y1,x0,x1=rect;cur=a[y0:y1,x0:x1];d=np.abs(cur-ref[y0:y1,x0:x1]).sum(2)
    m=(d<tol).astype(np.uint8);m=cv2.erode(m,np.ones((3,3),np.uint8));mf=cv2.GaussianBlur(m.astype(float),(0,0),1)[...,None]
    a[y0:y1,x0:x1]=cur*(1-mf)+pat[y0:y1,x0:x1]*mf;return a
SUBS=[(10,38,'A2_L0a.png'),(39,98,'A2_L0b.png'),(99,173,'A2_L1a.png'),(208,256,'A2_L2a.png'),(257,303,'A2_L2b.png'),(369,390,'A2_L4a.png'),(391,396,'A2_L4b.png')]
SUBP={f:rgba(f) for _,_,f in SUBS}
LOG=open('cardlog.txt','w')
import sys
RANGE=range(int(sys.argv[1]),int(sys.argv[2])+1) if len(sys.argv)>2 else range(1,996)
for i in RANGE:
    a=L(i);o=a.copy();ch=False
    if 16<=i<=98:
        a=inpaint_rect(a,cmask,120,960,560,960);a=over(a,NC*np.array([1,1,1,0.5 if i==16 else 1.0]));ch=True
    if 99<=i<=200:
        a[R]=over(a[R],UI[st(i)][R]);ch=True
    if 201<=i<=210:
        rr=a[R];al=(np.median(rr)-np.median(B211[R]))/(np.median(REF200[R])-np.median(B211[R]));al=float(np.clip(al,0,1))
        pred=al*REF200[R]+(1-al)*B211[R];m=(np.abs(rr-pred).sum(2)<45).astype(float)[...,None]
        new=over(REF200[R].copy(),UI['S5'][R]);a[R]=rr+m*al*(new-REF200[R]);ch=True
    if 316<=i<=345:
        for (ref,pat,T,B,rng) in [(C1R,C1P,(384,552,170,910),B1,(319,339)),(C2R,C2P,(1084,1252,170,910),B2,(324,343))]:
            if not(rng[0]<=i<=rng[1]): continue
            a2,k,r=affrep(a.copy(),ref,pat,T)
            if r<=6: a=a2;LOG.write(f'{i} aff {k} {r}\n');continue
            y0,y1,x0,x1=T;f=a[y0:y1,x0:x1];bb=B[y0:y1,x0:x1];rr=ref[y0:y1,x0:x1]
            al=((f-bb)*(rr-bb)).sum()/max(((rr-bb)**2).sum(),1);res=np.sqrt(((f-(bb+al*(rr-bb)))**2).mean())
            if 0.03<al<1.1 and res<14:
                a[y0:y1,x0:x1]=f+al*(pat[y0:y1,x0:x1]-rr);LOG.write(f'{i} fade {al:.2f} {res:.1f}\n');continue
            a,ok=homo(a,ref,pat,T);LOG.write(f'{i} homo {ok}\n')
    if 373<=i<=460: a=diffrep(a,PR,PP,(560,700,290,790),tol=40);ch=True
    if 367<=i<=372:
        y0,y1,x0,x1=595,676,318,762;al=(a[y0:y1,x0:x1].mean()-B366[y0:y1,x0:x1].mean())/(PR[y0:y1,x0:x1].mean()-B366[y0:y1,x0:x1].mean());al=float(np.clip(al,0,1))
        a[560:700,290:790]+=al*(PP[560:700,290:790]-PR[560:700,290:790]);ch=True
    for s0,s1,f in SUBS:
        if s0<=i<=s1:
            dk=(o.sum(2)<120).astype(np.uint8);rows=np.where(dk[1480:1620,100:980].sum(1)>200)[0]
            if len(rows):
                y0,y1=rows.min()+1480,rows.max()+1480;cs=np.where(dk[(y0+y1)//2])[0];x0,x1=cs.min(),cs.max()
                m=np.zeros(a.shape[:2],np.uint8);m[y0-8:y1+9,max(0,x0-10):min(1080,x1+11)]=255
                a=inpaint_rect(a,m,max(0,x0-80),min(1080,x1+80),y0-60,y1+60,5)
            a=over(a,SUBP[f]);ch=True
    cv2.imwrite(f'kB/{i:04d}.png',np.clip(a,0,255).astype(np.uint8))
print('done')
