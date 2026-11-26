cd /tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/unkv3/site && cp n1.wav n1_old.wav && cp ../vo/n1b.wav n1.wav && ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='0.45*sin(2*PI*1550*t)*(lt(t,0.17)+gt(t,0.24)*lt(t,0.62))*min(1,mod(t,10)*200)':s=48000:d=0.7" -af "afade=t=out:st=0.55:d=0.07" beep.wav && python3 - <<'EOF'
s=open('index.html').read()
def R(a,b):
    global s
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
D=0.76
R("const N=[0.35,3.15,6.05,10.3,12.95],SC=[0,3.0,5.9,10.15,12.8,15.6];const END=15.6;window.DURATION=18.0;",
  f"const N=[0.2,{3.15-D:.2f},{6.05-D:.2f},{10.3-D:.2f},{12.95-D:.2f}],SC=[0,{3.0-D:.2f},{5.9-D:.2f},{10.15-D:.2f},{12.8-D:.2f},{15.6-D:.2f}];const END={15.6-D:.2f};window.DURATION={18.0-D:.2f};")
R("ttl('T0',0.55,SC[1],t);","ttl('T0',0.3,SC[1],t);")
R('<div class="ttl" id="T4"><span class="l" style="font-size:96px">','<div class="ttl" id="T4" style="top:250px"><span class="l" style="font-size:150px">')
R("#free{position:absolute;left:-400px;top:-270px;width:800px;","#free{position:absolute;left:-500px;top:-500px;width:1000px;")
R('id="o_mw" src="m_wink.png" style="left:-10px;top:1240px;width:470px;','id="o_mw" src="m_wink.png" style="left:-30px;top:1130px;width:600px;')
R('id="o_holo" src="holo.png" style="left:760px;top:1290px;width:250px;','id="o_holo" src="holo.png" style="left:700px;top:1250px;width:330px;')
R("const ang=i/14*6.283,r=120+eo(k/0.6)*360,x=540+Math.cos(ang)*r*1.2,y=1060+Math.sin(ang)*r;","const ang=i/14*6.283,r=160+eo(k/0.6)*380,x=540+Math.cos(ang)*r*1.2,y=900+Math.sin(ang)*r;")
open('index.html','w').write(s)
EOF
grep -n "o_bell',\|o_ph',\|const b=seg(t,1.0,1.3)" index.html | cut -c1-120