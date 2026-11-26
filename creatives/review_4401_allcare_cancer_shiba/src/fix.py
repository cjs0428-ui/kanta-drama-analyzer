import numpy as np,subprocess,cv2
from PIL import Image
W,H=1080,1920
fr=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','src.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout,np.uint8).reshape(-1,H,W,3)
N=fr.shape[0]
L=lambda f:np.array(Image.open(f).convert('RGBA')).astype(np.float32)
n5,n6,n7=L('n5.png'),L('n6.png'),L('n7.png'); pill=L('pill.png')
s1=np.array(Image.open('s1.png').convert('RGB')).astype(np.float32); s2=np.array(Image.open('s2.png').convert('RGB')).astype(np.float32)
g=cv2.resize(np.array(Image.open('g1.png').convert('RGB')),(1080,720),interpolation=cv2.INTER_AREA).astype(np.float32)
tmpl=fr[int(29.2*30),1369:1439,400:700]
def over(img,o,x,y):
    h,w=o.shape[:2]; a=o[...,3:4]/255; img[y:y+h,x:x+w]=img[y:y+h,x:x+w]*(1-a)+o[...,:3]*a
def box(img,patch,cy0,minw):
    h,w=patch.shape[:2]; bw=max(w,minw); x0=540-bw//2
    img[cy0:cy0+70,x0:x0+bw]=255; xp=540-w//2; img[cy0:cy0+h,xp:xp+w]=patch
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p','vid_fix.mp4'],stdin=subprocess.PIPE)
capf=[]
for i in range(N):
    img=fr[i].astype(np.float32)
    if 341<=i<=420:
        img[1440:1510]=0; over(img,n5,0,1470)
    elif 421<=i<=534: over(img,n6,0,1470)
    elif 535<=i<=649: over(img,n7,0,1470)
    elif 650<=i<=718:
        k=(i-650)/68; s=1.0+0.06*k
        M=np.float32([[s,0,(1-s)*540],[0,s,(1-s)*360]]); gi=cv2.warpAffine(g,M,(1080,720),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REPLICATE)
        img[600:1297]=gi[:697]
        img[1297:1320,:270]=gi[697:720,:270]; img[1297:1320,810:]=gi[697:720,810:]
    elif 789<=i<=905:
        r=cv2.matchTemplate(fr[i,1369:1439,380:720],tmpl,cv2.TM_CCOEFF_NORMED).max()
        if r>0.8:
            capf.append(i); box(img,s1,1297,260); box(img,s2,1369,372)
    elif i>=906:
        over(img,pill,124,490)
    enc.stdin.write(np.clip(img,0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print('frames',N,'caption replaced frames',capf[:1],capf[-1:],len(capf))
