from PIL import Image,ImageDraw,ImageFont
import numpy as np,os
W='/tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/w/'
P=W+'font/package/dist/public/static/Pretendard-'
J=W+'fj/jua/files/jua-korean-400-normal.woff'
SRC=W+'cf/';OUT=W+'chk2/out/';os.makedirs(OUT,exist_ok=True)
rng=np.random.default_rng(5)
def feather(h,w,r):
    m=np.ones((h,w))
    for k in range(r):
        v=(k+1)/(r+1);m[k,:]=np.minimum(m[k,:],v);m[-1-k,:]=np.minimum(m[-1-k,:],v);m[:,k]=np.minimum(m[:,k],v);m[:,-1-k]=np.minimum(m[:,-1-k],v)
    return m[...,None]
def paste(img,src,x,y,r=10):
    h,w=src.shape[:2];m=feather(h,w,r);img[y:y+h,x:x+w]=img[y:y+h,x:x+w]*(1-m)+src*m
def chalk_layer(parts,size,y,cx=540):
    f=ImageFont.truetype(J,size);tw=sum(f.getlength(t) for t,_ in parts)
    L=Image.new('RGBA',(1080,1920),(0,0,0,0));d=ImageDraw.Draw(L);x=cx-tw/2
    for t,c in parts: d.text((x,y),t,font=f,fill=c+(255,));x+=f.getlength(t)
    a=np.asarray(L).astype(float);g=np.clip(rng.normal(0.92,0.16,a.shape[:2]),0.45,1)
    a[...,3]*=g;return a
WH=(245,243,235);YE=(251,225,115)
LA=chalk_layer([('정답은, 한 살이라도',WH)],64,170)
LB=chalk_layer([('젊을 ',WH),('때!',YE)],160,262)
def comp(img,L,al,scale=1.0):
    if al<=0: return img
    a=L
    if scale!=1.0:
        im=Image.fromarray(a.astype(np.uint8),'RGBA');w,h=im.size;ys,xs=np.where(a[...,3]>0);cx,cy=(xs.min()+xs.max())/2,(ys.min()+ys.max())/2
        im2=im.resize((int(w*scale),int(h*scale)));big=Image.new('RGBA',(w,h),(0,0,0,0));big.paste(im2,(int(cx-cx*scale),int(cy-cy*scale)));a=np.asarray(big).astype(float)
    m=a[...,3:4]/255*al;return img*(1-m)+a[...,:3]*m
# calendar card patch built from frame 140
fJ=lambda s:ImageFont.truetype(J,s)
base=np.asarray(Image.open(SRC+'0140.png').convert('RGB')).astype(float)
card=base.copy()
RED=(229,47,43);CREAM=tuple(int(v) for v in np.median(base[1060:1070,262:272].reshape(-1,3),0))
im=Image.fromarray(card.astype(np.uint8));d=ImageDraw.Draw(im)
d.rectangle((285,918,735,1003),fill=RED)
t='정답은!';f=fJ(50);d.text((498-f.getlength(t)/2,930),t,font=f,fill=(255,255,255))
d.rectangle((250,1030,690,1300),fill=CREAM);d.rectangle((690,1030,760,1185),fill=CREAM)
t='젊을 때';f=fJ(124);d.text((498-f.getlength(t)/2,1062),t,font=f,fill=RED)
t='한 살이라도';f=ImageFont.truetype(P+'Bold.otf',40);d.text((498-f.getlength(t)/2,1222),t,font=f,fill=(120,120,120))
card=np.asarray(im).astype(float)
CARD_REG=(slice(880,1350),slice(220,880))
fS=ImageFont.truetype(P+'Bold.otf',44)
def subbox(img,text):
    tw=fS.getlength(text);bw=int(tw+62);x0=int(540-bw/2);y0,y1=1397,1482
    im=Image.fromarray(np.clip(img,0,255).astype(np.uint8));d=ImageDraw.Draw(im)
    d.rounded_rectangle((x0,y0,x0+bw,y1),radius=14,fill=(20,20,20),outline=(235,235,235),width=3)
    d.text((540-tw/2,1414),text,font=fS,fill=(255,255,255))
    return np.asarray(im).astype(float)
fN=ImageFont.truetype(P+'SemiBold.otf',50)
NL=Image.new('L',(1080,1920),0);ImageDraw.Draw(NL).text((112,1262),'※ 담보별 지급조건 상이',font=fN,fill=255)
NL=np.asarray(NL).astype(float)/255*np.clip(rng.normal(0.9,0.12,(1920,1080)),0.55,1);NC=np.array([238,236,228],float)
for i in range(1,913):
    img=np.asarray(Image.open(SRC+f'{i:04d}.png').convert('RGB')).astype(float)
    if 123<=i<=188:
        paste(img,img[540:735,190:900].copy(),190,245,10)      # erase headline
        paste(img,img[560:656,240:840].copy(),240,452,10)       # erase subhead
        paste(img,img[560:640,250:830].copy(),250,160,8)        # clean line-A zone
        img=comp(img,LA,min(1,max(0,(i-127)/6)))
        if i>=156:
            t=min(1,(i-156)/6);img=comp(img,LB,t,1.25-0.25*t)
        if i>=136:
            cur=img[CARD_REG];ref=base[CARD_REG];new=card[CARD_REG]
            same=(np.abs(cur-ref).sum(2)<24).astype(float)
            from PIL import ImageFilter
            same=np.asarray(Image.fromarray((same*255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))).astype(float)/255
            img[CARD_REG]=cur*(1-same[...,None])+new*same[...,None]
        paste(img,img[560:670,195:885].copy(),195,1385,8)
        img=subbox(img,'정답은, 한 살이라도 젊을 때예요.')
    if 369<=i<=619:
        al=min(1,(i-368)/6)*NL[...,None];img=img*(1-al)+NC*al
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(OUT+f'{i:04d}.jpg',quality=95)
print('done')
