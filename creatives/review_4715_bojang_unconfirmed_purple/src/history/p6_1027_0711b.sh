cd /tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/unkv3/site && sed -i "s/const b=seg(t,1.0,1.3);\$('bdg')/const b=seg(t,0.7,1.0);\$('bdg')/; s/F('o_bell',0.9,SC\[1\]/F('o_bell',0.6,SC[1]/; s/F('o_ph',1.3,SC\[1\]/F('o_ph',0.9,SC[1]/" index.html && grep -c "seg(t,0.7,1.0)" index.html && grep -n "Math.sin((t\*7)-i\*0.9)" index.html | cut -c1-80 && sed -i "s/const p=t<1.0?Math.abs(Math.sin((t\*7)-i\*0.9)):0;/const p=t<0.6?Math.abs(Math.sin((t*7)-i*0.9)):0;/" index.html && python3 - <<'EOF'
import subprocess
D=0.76;N=[0.2,3.15-D,6.05-D,10.3-D,12.95-D];SC=[0,3.0-D,5.9-D,10.15-D,12.8-D,15.6-D];END=15.6-D;TOT=18.0-D
ev=[(f'n{i+1}.wav',N[i],1.0) for i in range(5)]+[('click3.wav',SC[1]+0.2,0.35),('click3.wav',SC[1]+1.2,0.35),('click3.wav',SC[1]+1.6,0.35)]+[('whoosh.wav',s-0.06,0.12) for s in SC[1:5]]+[('beep.wav',SC[3]+1.2,0.55),('click3.wav',SC[4]+0.31,0.8),('click3.wav',END-0.75,0.85)]
inp=[];fl=[];vo=[];fx=[]
for j,(f,t,v) in enumerate(ev):
    inp+=['-i',f];ms=int(t*1000);fl.append(f'[{j}]aformat=sample_rates=48000:channel_layouts=stereo,volume={v},adelay={ms}|{ms}[a{j}]');(vo if f[0]=='n' else fx).append(f'[a{j}]')
n=len(ev);inp+=['-i','bgm.m4a']
fl.append(''.join(vo)+f'amix=inputs={len(vo)}:normalize=0,apad,atrim=0:{TOT},asplit[v1][v2]')
fl.append(''.join(fx)+f'amix=inputs={len(fx)}:normalize=0,apad,atrim=0:{TOT}[fx]')
fl.append(f'[{n}]aformat=sample_rates=48000:channel_layouts=stereo,apad,atrim=0:{TOT},volume=0.45,afade=t=out:st={TOT-1.5}:d=1.5[bg]')
fl.append('[bg][v2]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=300[bgd]')
fl.append('[bgd][v1][fx]amix=inputs=3:normalize=0:duration=first,apad,atrim=0:%s,loudnorm=I=-14:TP=-1.5[out]'%TOT)
subprocess.run(['ffmpeg','-y','-loglevel','error',*inp,'-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','mix4.wav'],check=True);print(TOT)
EOF
cd ../.. && W=1080 H=1920 TS=0.5,1.6,10.8,12.6,14.2 node render.cjs unkv3/site stills unkv3/st3 && python3 -c "
from PIL import Image
f=['0.5','1.6','10.8','12.6','14.2']
s=Image.new('RGB',(270*5,480))
for i,x in enumerate(f): s.paste(Image.open(f'unkv3/st3/t{x}.png').convert('RGB').resize((270,480)),(i*270,0))
s.save('unkv3/sheet3.jpg')"