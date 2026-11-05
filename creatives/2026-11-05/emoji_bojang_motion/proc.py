import sys,os;sys.path.insert(0,'.')
from lib import *
SRC=W+'ef/';OUT=W+'emo/out/';os.makedirs(OUT,exist_ok=True)
bgt=tuple(int(v) for v in BG)
def arr(p): return np.asarray(Image.open(p).convert('RGB')).astype(float)
REF=arr(SRC+'0430.png');END=arr(SRC+'0620.png')
fH=font('ExtraBold',117)
def l1_canvas(num):
    im=Image.new('RGB',(1080,1920),bgt);d=ImageDraw.Draw(im)
    # measure
    tmp=Image.new('L',(1400,200),0);td=ImageDraw.Draw(tmp)
    x=draw_spaced(td,0,0,num+'만',fH,255,-3);draw_spaced(td,x,0,'명이 확인한',fH,255,-3)
    t=np.asarray(tmp);ys,xs=np.where(t>100);w=xs.max()-xs.min()
    ox=544.5-w/2-xs.min();oy=343-ys.min()
    x=draw_spaced(d,ox,oy,num+'만',fH,RED,-3);draw_spaced(d,x,oy,'명이 확인한',fH,DARK,-3)
    return np.asarray(im).astype(float)
def blur(a,s):
    if s<0.3: return a
    return np.asarray(Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)
def bgcanvas(): return np.tile(BG,(1920,1080,1))
# templates
L2=bgcanvas();L2[466:600]=REF[466:600]
L1old=bgcanvas();L1old[330:466]=REF[330:466]
Fold=bgcanvas();Fold[1486:1534]=REF[1486:1534]
Dold=bgcanvas();Dold[1592:1684]=REF[1592:1684]
# new footnote
fF=font('Regular',48)
def footnote():
    im=Image.new('RGB',(1080,1920),bgt);d=ImageDraw.Draw(im)
    for k,t in enumerate(['※ 메리츠화재 보장분석 서비스 이용자 수','(26년 9월 기준)']):
        w=fF.getlength(t);d.text(((1080-w)/2,1472+k*56),t,font=fF,fill=(108,106,107))
    return np.asarray(im).astype(float)
Fnew=footnote()
fD=font('Regular',48)
def disclaimer():
    im=Image.new('RGB',(1080,1920),bgt);d=ImageDraw.Draw(im)
    for k,t in enumerate(wrap('*상기 내용은 메리츠화재의 의견이며, 계약 체결에 따른 이익 또는 손실은 보험 계약자 등에게 귀속됩니다.',fD,965)):
        d.text((58,1598+k*62),t,font=fD,fill=(40,40,40))
    return np.asarray(im).astype(float)
Dnew=disclaimer()
# endcard
def endcard():
    e=END.copy();tex=END[1590:1890]
    rows=np.arange(540,1900);e[540:1900]=tex[(rows-540)%300]
    im=Image.fromarray(e.astype(np.uint8));d=ImageDraw.Draw(im);f=font('Regular',48)
    P=['보험계약자가 기존 보험계약을 해약하고 새로운 보험계약을 체결하는 과정에서',
       '① 질병이력, 연령증가 등으로 가입이 거절되거나 보험료가 인상될 수 있습니다.',
       '② 가입 상품에 따라 새로운 보험금 지급제한기간 적용 및 보장 제한 등 기타 불이익이 발생할 수 있습니다.',
       '지급한도, 면책사항 등에 따라 보험금 지급이 제한될 수 있습니다. 보험계약 전, 자세한 상품내용과 제한사항은 약관 및 상품설명서를 참고하시기 바랍니다. 메리츠화재는 해당 상품에 대해 충분히 설명할 의무가 있으며, 가입자는 가입하기 전 이에 대한 충분한 설명을 받으시기 바랍니다.',
       ':본 광고는 손해보험협회 광고 심의 기준을 준수하였으며 유효기간은 심의일로부터 1년입니다.',
       '손해보험협회 심의필 제OOOOO호','(2026.OO.OO~2027.OO.OO)']
    y=548;LH=61
    for p in P:
        for ln in wrap(p,f,975):
            d.text((54,y),ln,font=f,fill=(0,0,0));y+=LH
    print('endcard text bottom',y)
    return np.asarray(im).astype(float)
ENEW=endcard()
SIG=[0,1,2,3,4,6,8,10,12,15,18,22,26,30]
def fit(img,T,rows):
    best=None
    for s in SIG:
        B=blur(T,s)[rows[0]:rows[1]]-BG;R=img[rows[0]:rows[1]]-BG
        den=(B*B).sum()
        if den<1: continue
        a=(B*R).sum()/den;err=((R-a*B)**2).mean()
        if best is None or err<best[0]: best=(err,s,a)
    return best[1],max(0,min(1.05,best[2])),best[0]
# count schedule
pts=[(384,0),(390,.093),(393,.335),(394,.405),(400,.725),(419,1.0)]
def frac(i):
    if i<=pts[0][0]: return 0
    if i>=419: return 1
    for (a,fa),(b,fb) in zip(pts,pts[1:]):
        if a<=i<=b:
            t=(i-a)/(b-a)
            if a==400: t=1-(1-t)**2
            return fa+(fb-fa)*t
L1fin=l1_canvas('3,495')
log=open(W+'emo/fitlog.txt','w')
files=sorted(os.listdir(SRC))
for fn in files:
    i=int(fn[:4]);img=arr(SRC+fn)
    if 394<=i<=530:
        s2,a2,e=fit(img,L2,(480,600))
        if i<=419:
            t=(i-394)/25;n=int(round(1232+(3495-1232)*(1-(1-t)**2)))
            a1={394:.77,395:.88}.get(i,1.0)
            L1=l1_canvas(f'{n:,}')
            comp=BG+a1*(L1-BG)+a2*(blur(L2,s2)-BG)
            img[300:612]=comp[300:612]
        elif 512<=i<=516:
            comp=BG+a2*(blur(L1fin+L2-BG,s2)-BG)
            img[300:600]=comp[300:600]
        elif a2>0.02:
            img[300:612]+=a2*(blur(L1fin,s2)[300:612]-blur(L1old,s2)[300:612])
        log.write(f'{i} L2 s={s2} a={a2:.2f}\n')
    if 388<=i<=515:
        img[1430:1596]+=(Fnew[1430:1596]-BG)-(Fold[1430:1596]-BG)
    if i<=569:
        r=img[1592:1684];D=Dold[1592:1684];m=(D.sum(2)<600)
        ad=((BG-r)*(BG-D))[m].sum()/((BG-D)**2)[m].sum();ad=max(0,min(1,ad))
        img[1592:1684]-=ad*(D-BG)
        img[1560:1820]+=ad*(Dnew[1560:1820]-BG)
    if i>=560:
        r=img[1592:1684]
        w=1.0 if i>=570 else None
        if w is None:
            D=Dold[1592:1684];m=(D.sum(2)<600)
            # endcard weight from endcard dark text pixels in rows 1200-1560
            E=END[1200:1560];me=(E.sum(2)<200);R=arr(SRC+fn)[1200:1560]
            w=((BG-R)*(BG-E))[me].sum()/((BG-E)**2)[me].sum();w=max(0,min(1,w))
        img[540:1900]+=w*(ENEW[540:1900]-END[540:1900])
        log.write(f'{i} endw={w:.2f}\n')
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(OUT+fn.replace('.png','.jpg'),quality=95)
log.close()
