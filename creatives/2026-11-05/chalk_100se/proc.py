from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np,os
W='/tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/w/'
F=W+'font/package/dist/public/static/Pretendard-'
SRC=W+'cf/';OUT=W+'chk/out/';os.makedirs(OUT,exist_ok=True)
DROP=set(range(124,141))
def feather(h,w,r=14):
    m=np.ones((h,w));
    for k in range(r):
        v=(k+1)/(r+1);m[k,:]=np.minimum(m[k,:],v);m[-1-k,:]=np.minimum(m[-1-k,:],v);m[:,k]=np.minimum(m[:,k],v);m[:,-1-k]=np.minimum(m[:,-1-k],v)
    return m[...,None]
def paste(img,src,x,y,r=14):
    h,w=src.shape[:2];m=feather(h,w,r);img[y:y+h,x:x+w]=img[y:y+h,x:x+w]*(1-m)+src*m
# subtitle box
fS=ImageFont.truetype(F+'Bold.otf',44)
def subbox(img,text):
    tw=fS.getlength(text);bw=int(tw+62);x0=int(540-bw/2);y0,y1=1397,1482
    im=Image.fromarray(img.astype(np.uint8));d=ImageDraw.Draw(im)
    d.rounded_rectangle((x0,y0,x0+bw,y1),radius=14,fill=(20,20,20),outline=(235,235,235),width=3)
    d.text((540-tw/2,1414),text,font=fS,fill=(255,255,255))
    return np.asarray(im).astype(float)
fN=ImageFont.truetype(F+'SemiBold.otf',50)
rng=np.random.default_rng(3)
def note_layer():
    L=Image.new('L',(1080,1920),0);d=ImageDraw.Draw(L)
    d.text((112,1262),'※ 담보별 지급조건 상이',font=fN,fill=255)
    a=np.asarray(L).astype(float)/255
    tex=np.clip(rng.normal(0.9,0.12,a.shape),0.55,1)  # chalk grain
    return a*tex
NL=note_layer();NC=np.array([238,236,228],float)
n=0
for i in range(1,913):
    if i in DROP: continue
    img=np.asarray(Image.open(SRC+f'{i:04d}.png').convert('RGB')).astype(float)
    if 141<=i<=188:
        # erase headline with board patch from rows 560-717
        paste(img,img[540:735,190:900].copy(),190,245,10)
        og=np.asarray(Image.open(SRC+f'{i:04d}.png').convert('RGB')).astype(float)[250:428,530:826]
        al=min(1,(i-140)/5)
        h,w=og.shape[:2];m=feather(h,w,8)*al;x=540-w//2
        img[250:428,x:x+w]=img[250:428,x:x+w]*(1-m)+og*m
    if 123<=i<=188:
        paste(img,img[560:670,195:885].copy(),195,1385,8)
        img=subbox(img,'가장 젊은 날이니까요.')
    if 369<=i<=619:
        al=min(1,(i-368)/6)*NL[...,None]
        img=img*(1-al)+NC*al
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(OUT+f'{n:04d}.jpg',quality=95);n+=1
print('frames',n)
