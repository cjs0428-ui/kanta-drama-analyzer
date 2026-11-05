from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
W='/tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/w/'
F=W+'font/package/dist/public/static/Pretendard-'
BG=np.array([247,245,246],float)
RED=(228,49,41);DARK=(25,25,25)
def font(w,s): return ImageFont.truetype(F+w+'.otf',s)
def wrap(text,f,maxw,ls=0):
    words=text.split(' ');lines=[];cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if f.getlength(t)+ls*len(t)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            # hard-break long word
            while f.getlength(w)>maxw:
                k=len(w)
                while f.getlength(w[:k])>maxw: k-=1
                lines.append(w[:k]);w=w[k:]
            cur=w
    if cur: lines.append(cur)
    return lines
def draw_spaced(d,x,y,txt,f,fill,ls):
    for c in txt:
        d.text((x,y),c,font=f,fill=fill);x+=f.getlength(c)+ls
    return x
