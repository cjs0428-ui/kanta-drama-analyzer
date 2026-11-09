import numpy as np,os
from PIL import Image,ImageFilter
BG=np.array([247,245,246],float)
def L(i): return np.asarray(Image.open(f'f5/{i:04d}.png').convert('RGB')).astype(float)
ref=L(490);y0,y1,x0,x1=990,1468,195,895
reg=ref[y0:y1,x0:x1];d=np.abs(reg-BG).sum(2);al=np.clip((d-4)/30,0,1)
rgb=np.where(al[...,None]>0.02,(reg-BG*(1-al[...,None]))/np.maximum(al[...,None],0.02),BG)
layer=np.dstack([np.clip(rgb,0,255),al*255]).astype(np.uint8);ST=Image.fromarray(layer,'RGBA')
OC=(543-x0,1230-y0)  # stamp center in layer coords
clean=ref.copy()
L_=ref[y0:y1,x0-3:x0].mean(1);R_=ref[y0:y1,x1:x1+3].mean(1);t=np.linspace(0,1,x1-x0)[None,:,None]
clean[y0:y1,x0:x1]=L_[:,None,:]*(1-t)+R_[:,None,:]*t
NEWC=(538,1031);OLDC=(543,1230)
SC={476:2.31,477:1.99,478:1.68,479:1.37,480:1.06}
def place(base,scale,center,alpha=1.0,blur=0):
    w,h=ST.size;im=ST.resize((max(1,int(w*scale)),max(1,int(h*scale))),Image.LANCZOS)
    canvas=Image.new('RGBA',(1080,1920),(0,0,0,0));cx,cy=OC[0]*scale,OC[1]*scale
    canvas.paste(im,(int(round(center[0]-cx)),int(round(center[1]-cy))),im)
    if blur>0.3: canvas=canvas.filter(ImageFilter.GaussianBlur(blur))
    c=np.asarray(canvas).astype(float);a=c[...,3:4]/255*alpha
    return base*(1-a)+c[...,:3]*a,a
os.makedirs('f5o',exist_ok=True)
FIT={513:(4,.70),514:(10,.48),515:(15,.22)}
for i in range(1,652):
    a=L(i)
    if 476<=i<=512:
        a,_=place(clean.copy(),SC.get(i,1.0),NEWC)
    elif i in FIT:
        s,al=FIT[i]
        sc,_=place(clean.copy(),1.0,NEWC)
        sc[1460:]=BG
        b=np.asarray(Image.fromarray(np.clip(sc,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float) if s>0.3 else sc
        a[:1460]=(BG+al*(b-BG))[:1460]
    Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save(f'f5o/{i:04d}.png')
print('ok')
