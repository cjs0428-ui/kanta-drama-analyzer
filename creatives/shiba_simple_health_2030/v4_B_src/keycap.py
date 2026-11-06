import cv2,numpy as np,os
from PIL import Image
O=np.asarray(Image.open('old_t.png').convert('RGBA'))
N=np.asarray(Image.open('new_t.png').convert('RGBA')).astype(float)
mask=(O[...,3]>12).astype(np.uint8)*255
mask=cv2.dilate(mask,np.ones((9,9),np.uint8))
x0,x1,y0,y1=120,960,560,960
os.makedirs('k',exist_ok=True)
for i in range(16,99):
    a=cv2.imread(f'f/{i:04d}.png')
    crop=a[y0:y1,x0:x1];m=mask[y0:y1,x0:x1]
    small=cv2.resize(crop,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA);ms=cv2.resize(m,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
    inp=cv2.inpaint(small,ms,6,cv2.INPAINT_TELEA)
    up=cv2.resize(inp,(x1-x0,y1-y0),interpolation=cv2.INTER_CUBIC)
    up=cv2.GaussianBlur(up,(0,0),2)
    mf=cv2.GaussianBlur(m.astype(float)/255,(0,0),3)[...,None]
    crop=crop*(1-mf)+up*mf
    a=a.astype(float);a[y0:y1,x0:x1]=crop
    al=(0.5 if i==16 else 1.0)*N[...,3:4]/255
    rgb=N[...,2::-1]  # RGBA->BGR
    a=a*(1-al)+rgb*al
    cv2.imwrite(f'k/{i:04d}.png',np.clip(a,0,255).astype(np.uint8))
print('done')
