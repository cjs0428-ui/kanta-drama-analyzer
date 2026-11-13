import cv2,numpy as np
Q={'b':[[126,420],[451,363],[538,906],[206,963]],'c':[[98,487],[352,419],[467,884],[198,956]]}
for k in 'bc':
    im=cv2.imread('p'+k+'.png'); H,W=im.shape[:2]; oy=H//2
    s=cv2.imread('scr'+k.upper()+'.png'); h,w=s.shape[:2]
    dst=np.float32(Q[k]); dst[:,1]+=oy
    M=cv2.getPerspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]),dst)
    warp=cv2.warpPerspective(s,M,(W,H),flags=cv2.INTER_AREA)
    m=np.zeros((H,W),np.float32); m[oy:,:W//2]=np.load('mask'+k+'.npy')/255.
    m=cv2.dilate(m,np.ones((9,9),np.uint8)); m=cv2.GaussianBlur(m,(5,5),0)[...,None]
    out=(warp*m+im*(1-m)).astype(np.uint8); cv2.imwrite('pa'+k+'.png',out)
    cv2.imwrite('z'+k+'.png',out[oy:,:W//2])
