cd /tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/unkv/site && cp ../../end19/endcard_final.png endcard.png && python3 - <<'EOF'
s=open('index.html').read()
def R(a,b):
    global s
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
R("html,body{width:1080px;height:1080px;","html,body{width:1080px;height:1920px;")
R("#bg2{position:absolute;inset:0;background:radial-gradient(circle at 50% 56%,","#bg2{position:absolute;inset:0;background:radial-gradient(circle at 50% 52%,")
R("#hd{position:absolute;left:46px;top:40px;","#hd{position:absolute;left:56px;top:70px;")
R(".ttl{position:absolute;left:0;right:0;top:120px;",".ttl{position:absolute;left:0;right:0;top:300px;")
R("#dots{position:absolute;left:0;right:0;top:122px;","#dots{position:absolute;left:0;right:0;top:250px;")
R('<div class="ttl" id="T0" style="top:170px">','<div class="ttl" id="T0" style="top:300px">')
R("#ctr{position:absolute;left:540px;top:620px;","#ctr{position:absolute;left:540px;top:1060px;")
R("#sim{position:absolute;left:28px;top:930px;","#sim{position:absolute;left:0;right:0;text-align:center;top:1700px;")
R("#bar{position:absolute;left:0;right:0;bottom:0;height:98px;","#bar{position:absolute;left:0;right:0;bottom:0;height:130px;")
R("#end{position:absolute;inset:0;width:1080px;height:1080px;","#end{position:absolute;inset:0;width:1080px;height:1920px;")
# bigger avatar & panels
R("#av{position:absolute;left:-158px;top:-158px;width:316px;height:316px;","#av{position:absolute;left:-200px;top:-200px;width:400px;height:400px;")
R("#av .hd2{position:absolute;left:105px;top:68px;width:106px;height:106px;","#av .hd2{position:absolute;left:133px;top:86px;width:134px;height:134px;")
R("#av .bd{position:absolute;left:52px;top:185px;width:212px;height:200px;","#av .bd{position:absolute;left:66px;top:234px;width:268px;height:254px;")
R("#bdg{position:absolute;left:62px;top:-170px;width:104px;height:104px;","#bdg{position:absolute;left:84px;top:-214px;width:124px;height:124px;")
R("font-weight:700;font-size:60px;line-height:90px;","font-weight:700;font-size:72px;line-height:110px;")
R("#scan{position:absolute;left:-330px;top:-210px;width:660px;height:420px;","#scan{position:absolute;left:-400px;top:-260px;width:800px;height:520px;")
R("#res{position:absolute;left:-330px;top:-230px;width:660px;height:460px;","#res{position:absolute;left:-400px;top:-280px;width:800px;height:560px;")
# stamp instead of card
R('''#free{position:absolute;left:-250px;top:-130px;width:500px;height:260px;border-radius:40px;background:#FFF3A3;color:#5B2B70;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;box-shadow:0 18px 40px rgba(0,0,0,.25)}''',
 '''#free{position:absolute;left:-330px;top:-170px;width:660px;height:340px;border:16px solid #FF3B3B;border-radius:36px;outline:6px solid #FF3B3B;outline-offset:10px;color:#FF3B3B;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;filter:url(#grunge);background:rgba(255,255,255,.04)}
.ob{position:absolute;opacity:0;will-change:transform}''')
R('<div id="free"><div style="font-size:40px;font-weight:700">보장분석</div><div style="font-size:120px;font-weight:800;letter-spacing:-4px;line-height:1">무료</div></div>',
  '<div id="free"><div style="font-size:66px;font-weight:800;letter-spacing:2px">보장분석</div><div style="font-size:190px;font-weight:800;letter-spacing:-6px;line-height:1">무료</div></div>')
R('<div id="bg"></div><div id="bg2"></div>','''<div id="bg"></div><div id="bg2"></div>
<svg width="0" height="0" style="position:absolute"><filter id="grunge"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.35" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter></svg>
<div id="sparks"></div>
<img class="ob" id="o_bell" src="bell.png" style="left:650px;top:640px;width:250px">
<img class="ob" id="o_ph" src="phone_n.png" style="left:90px;top:1260px;width:270px">
<img class="ob" id="o_docs" src="docs.png" style="left:640px;top:1300px;width:340px">
<img class="ob" id="o_mag" src="mag.png" style="left:0;top:0;width:300px;z-index:9">
<img class="ob" id="o_alert" src="alert.png" style="left:770px;top:690px;width:220px;z-index:9">
<img class="ob" id="o_holo" src="holo.png" style="left:760px;top:1290px;width:250px;z-index:9">''')
# cards bigger spread
R(".cd{position:absolute;left:-150px;top:-95px;width:300px;height:190px;",".cd{position:absolute;left:-165px;top:-105px;width:330px;height:210px;")
R("c.style.transform=`translate(${ang*330*p}px,${(ang?40:-10)*p+(1-p)*40}px)","c.style.transform=`translate(${ang*330*p}px,${(ang?-30:-220)*p+(1-p)*40}px)")
# CTA tap position
R("tp.style.left=(640+120*(1-mv))+'px';tp.style.top=(1000+120*(1-mv)+(press?8:0))+'px';","tp.style.left=(660+120*(1-mv))+'px';tp.style.top=(1820+120*(1-mv)+(press?8:0))+'px';")
# stamp motion: slam
R("{const a=SC[4],p=seg(t,a+.1,a+.45);$('free').style.opacity=cl(p*3)*(1-seg(t,END-.1,END));$('free').style.transform=`rotate(-6deg) scale(${cl(back(p),0,1.3)+0.03*Math.sin(t*6)*(t>a+.5)})`}",
  "{const a=SC[4]+.15,p=seg(t,a,a+.16);$('free').style.opacity=t>=a?(1-seg(t,END-.1,END)):0;$('free').style.transform=`rotate(-9deg) scale(${2.4-1.4*eo(p)})`;document.body.style.transform=t>=a+.16&&t<a+.32?`translate(${Math.sin(t*120)*6}px,${Math.cos(t*100)*5}px)`:'none'}")
# objects motions appended before end-card line
R("  $('end').style.opacity=eo(seg(t,END,END+.35));",
"""  const F=(id,a,z,fn)=>{const e=$(id);const p=seg(t,a,a+.35),q=seg(t,z-.2,z);e.style.opacity=cl(p*2)*(1-q);e.style.transform=fn(p,t-a)};
  F('o_bell',0.9,SC[1],(p,k)=>`scale(${cl(back(p),0,1.25)}) rotate(${Math.sin(k*14)*14*Math.max(0,1-k/2.2)}deg)`);
  F('o_ph',1.3,SC[1],(p,k)=>`translateY(${(1-eo(p))*80+Math.sin(k*3)*10}px) rotate(-8deg)`);
  F('o_docs',SC[1]+0.2,SC[2],(p,k)=>`translate(${(1-eo(p))*200}px,${Math.sin(k*2.5)*12}px) rotate(${6+Math.sin(k*2)*4}deg)`);
  {const a=SC[2]+0.8,z=SC[3],e=$('o_mag');const p=seg(t,a,a+.3),q=seg(t,z-.2,z);e.style.opacity=cl(p*2)*(1-q);const k=t-a;e.style.left=(560+Math.sin(k*2.2)*170)+'px';e.style.top=(1060+Math.cos(k*1.7)*60)+'px';e.style.transform=`scale(${cl(back(p),0,1.2)})`}
  F('o_alert',SC[3]+1.2,SC[4],(p,k)=>`scale(${cl(back(p),0,1.3)*(1+0.05*Math.sin(k*8))}) rotate(${Math.sin(k*10)*6}deg)`);
  F('o_holo',SC[4]+0.6,END,(p,k)=>`scale(${cl(back(p),0,1.25)}) translateY(${Math.sin(k*3)*10}px)`);
  // sparkles burst on stamp
  {const a=SC[4]+0.31,k=t-a,box=$('sparks');if(k>0&&k<1.2){let h='';for(let i=0;i<14;i++){const ang=i/14*6.283,r=120+eo(k/0.6)*360,x=540+Math.cos(ang)*r*1.2,y=1060+Math.sin(ang)*r;h+=`<div style="position:absolute;left:${x}px;top:${y}px;width:22px;height:22px;border-radius:50%;background:${i%2?'#FFF3A3':'#fff'};opacity:${1-k/1.2};z-index:8"></div>`}box.innerHTML=h}else box.innerHTML=''}
  $('end').style.opacity=eo(seg(t,END,END+.35));""")
open('index.html','w').write(s)
EOF
grep -c "SC\[4\]" index.html