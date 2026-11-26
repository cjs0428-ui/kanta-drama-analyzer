cd /tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/unkv3/site && ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='0.5*sin(2*PI*1318*t)*exp(-4*t)*lt(t,0.42)+0.5*sin(2*PI*1046*(t-0.38))*exp(-3*(t-0.38))*gt(t,0.38)+0.15*sin(2*PI*2636*t)*exp(-8*t)':s=48000:d=1.4" -af "afade=t=in:d=0.005,afade=t=out:st=1.1:d=0.3" dingdong.wav && python3 - <<'EOF'
import re
s=open('index.html').read()
old=re.search(r'const N=\[[^\]]*\],SC=\[[^\]]*\];const END=[0-9.]+;window.DURATION=[0-9.]+;',s).group(0)
D=0.36
new=f"const N=[0.6,{3.15-D:.2f},{6.05-D:.2f},{10.3-D:.2f},{12.95-D:.2f}],SC=[0,{3.0-D:.2f},{5.9-D:.2f},{10.15-D:.2f},{12.8-D:.2f},{15.6-D:.2f}];const END={15.6-D:.2f};window.DURATION={18.0-D:.2f};"
s=s.replace(old,new)
for a,b in [("ttl('T0',0.3,SC[1],t);","ttl('T0',0.55,SC[1],t);"),("const b=seg(t,0.7,1.0);$('bdg')","const b=seg(t,0.15,0.45);$('bdg')")]:
    assert s.count(a)==1,a; s=s.replace(a,b)
open('index.html','w').write(s);print(new)
import subprocess
N=[0.6,3.15-D,6.05-D,10.3-D,12.95-D];SC=[0,3.0-D,5.9-D,10.15-D,12.8-D,15.6-D];END=15.6-D;TOT=18.0-D
ev=[(f'n{i+1}.wav',N[i],1.0) for i in range(5)]+[('dingdong.wav',0.03,0.55),('click3.wav',SC[1]+0.2,0.35),('click3.wav',SC[1]+1.2,0.35),('click3.wav',SC[1]+1.6,0.35)]+[('whoosh.wav',s-0.06,0.12) for s in SC[1:5]]+[('beep.wav',SC[3]+1.2,0.55),('click3.wav',SC[4]+0.31,0.8),('click3.wav',END-0.75,0.85)]
inp=[];fl=[];vo=[];fx=[]
for j,(f,t,v) in enumerate(ev):
    inp+=['-i',f];ms=int(t*1000);fl.append(f'[{j}]aformat=sample_rates=48000:channel_layouts=stereo,volume={v},adelay={ms}|{ms}[a{j}]');(vo if f[0]=='n' else fx).append(f'[a{j}]')
n=len(ev);inp+=['-i','bgm.m4a']
fl.append(''.join(vo)+f'amix=inputs={len(vo)}:normalize=0,apad,atrim=0:{TOT},asplit[v1][v2]')
fl.append(''.join(fx)+f'amix=inputs={len(fx)}:normalize=0,apad,atrim=0:{TOT}[fx]')
fl.append(f'[{n}]aformat=sample_rates=48000:channel_layouts=stereo,apad,atrim=0:{TOT},volume=0.45,afade=t=out:st={TOT-1.5}:d=1.5[bg]')
fl.append('[bg][v2]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=300[bgd]')
fl.append('[bgd][v1][fx]amix=inputs=3:normalize=0:duration=first,apad,atrim=0:%s,loudnorm=I=-14:TP=-1.5[out]'%TOT)
subprocess.run(['ffmpeg','-y','-loglevel','error',*inp,'-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','mix5.wav'],check=True);print(TOT)
EOF
cd ../.. && rm -rf unkv3/fr && W=1080 H=1920 node render.cjs unkv3/site frames unkv3/fr && ffmpeg -y -loglevel error -framerate 30 -i unkv3/fr/f%05d.jpg -i unkv3/site/mix5.wav -af apad -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -t 17.64 meritz_bojang_unconfirmed_motion_9x16_v6.mp4 && ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 meritz_bojang_unconfirmed_motion_9x16_v6.mp4 && ffmpeg -v error -i meritz_bojang_unconfirmed_motion_9x16_v6.mp4 -f null - 2>&1 | wc -l