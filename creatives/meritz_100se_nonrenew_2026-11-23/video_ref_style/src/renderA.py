import subprocess,numpy as np,json
from PIL import Image
W,H,F=1080,1920,30
SC=[0,4.17,8.46,11.06,14.59,18.84,22.57,26.2,30.0,35.0]
cap=json.load(open('capA.json'))
def L(p): return np.array(Image.open(p).convert('RGBA')).astype(np.float32)
CA=[L(f'ca{i:02d}.png') for i in range(len(cap))]
NA=[L(f'na{k}.png') for k in range(1,10)]; NK=[L(f'nk{k}.png') for k in range(1,10)]
legal=np.array(Image.open('legal.png').convert('RGB').resize((W,H)))
def over(img,o,k=1.0):
    a=o[...,3:4]/255.*k; return img*(1-a)+o[...,:3]*a
enc=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','va.mp4'],stdin=subprocess.PIPE)
for s in range(9):
    a,b=SC[s],SC[s+1]; d=b-a; n=int(round(d*F)); rate=min(1.0,5.0/d)
    vf=f"setpts=PTS/{rate:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30"
    dec=subprocess.Popen(['ffmpeg','-loglevel','quiet','-i',f'ka{s+1}.mp4','-vf',vf,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    last=None
    for i in range(n):
        buf=dec.stdout.read(W*H*3)
        f=np.frombuffer(buf,np.uint8).reshape(H,W,3).astype(np.float32) if len(buf)==W*H*3 else last
        last=f; t=a+i/F; lf=i
        img=over(f,NA[s],min(1,lf/6+0.2))
        kk=NK[s]
        if s==3: img=over(img,kk,min(1,max(0,(t-13.63)/0.15)))
        else: img=over(img,kk,min(1,lf/6))
        ci=[j for j,(x,y) in enumerate(cap) if x-0.05<=t<y+0.05]
        if ci: j=ci[0]; img=over(img,CA[j],min(1,(t-cap[j][0])/0.12+0.3))
        enc.stdin.write(np.clip(img,0,255).astype(np.uint8).tobytes())
    dec.terminate()
for i in range(int(2.5*F)): enc.stdin.write(legal.tobytes())
enc.stdin.close(); enc.wait()
