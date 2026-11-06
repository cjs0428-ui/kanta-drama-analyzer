import cv2,numpy as np
from PIL import Image
S1=np.asarray(Image.open('new_sub1.png').convert('RGBA')).astype(float);S2=np.asarray(Image.open('new_sub2.png').convert('RGBA')).astype(float)
for i in range(10,99):
    src=f'k/{i:04d}.png' if 16<=i<=98 else f'f/{i:04d}.png'
    a=cv2.imread(src);o=cv2.imread(f'f/{i:04d}.png').astype(int)
    dk=(o.sum(2)<40).astype(np.uint8);reg=dk[1480:1620]
    rows=np.where(reg[:,100:980].sum(1)>200)[0]
    if len(rows)==0: continue
    y0,y1=rows.min()+1480,rows.max()+1480;cs=np.where(dk[(y0+y1)//2])[0];x0,x1=cs.min(),cs.max()
    S=S1 if i<=43 else S2
    newm=(S[...,3]>10)
    m=np.zeros(a.shape[:2],np.uint8);m[y0-8:y1+9,x0-10:x1+11]=255
    if m.any():
        X0,X1,Y0,Y1=max(0,x0-80),min(1080,x1+80),y0-60,y1+60
        crop=a[Y0:Y1,X0:X1];mm=m[Y0:Y1,X0:X1]
        sm=cv2.resize(crop,None,fx=.5,fy=.5,interpolation=cv2.INTER_AREA);ms=cv2.resize(mm,None,fx=.5,fy=.5,interpolation=cv2.INTER_NEAREST)
        ms=cv2.dilate(ms,np.ones((3,3),np.uint8))
        up=cv2.resize(cv2.inpaint(sm,ms,5,cv2.INPAINT_TELEA),(X1-X0,Y1-Y0),interpolation=cv2.INTER_CUBIC)
        mf=(mm>0)[...,None].astype(float);crop=crop*(1-mf)+up*mf;a=a.astype(float);a[Y0:Y1,X0:X1]=crop
    a=a.astype(float);al=S[...,3:4]/255;a=a*(1-al)+S[...,2::-1]*al
    cv2.imwrite(f'k/{i:04d}.png',np.clip(a,0,255).astype(np.uint8))
print('ok')
