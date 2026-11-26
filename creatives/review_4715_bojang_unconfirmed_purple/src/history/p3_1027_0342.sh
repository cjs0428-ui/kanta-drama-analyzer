cd /tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/unkv3/site && python3 - <<'EOF'
s=open('index.html').read()
def R(a,b):
    global s
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
R('''  <div class="cd" id="c0"><b>실손보험</b><s>2014년 가입</s><em>미확인</em></div>
  <div class="cd" id="c1"><b>암보험</b><s>2017년 가입</s><em>미확인</em></div>
  <div class="cd" id="c2"><b>운전자보험</b><s>2019년 가입</s><em>미확인</em></div>
''','')
R('<div id="sparks"></div>','''<div id="sparks"></div>
<style>.nt{position:absolute;left:70px;width:940px;height:150px;border-radius:38px;background:rgba(255,255,255,.95);box-shadow:0 18px 40px rgba(40,0,40,.3);display:flex;align-items:center;padding:0 34px;gap:26px;color:#222;opacity:0;z-index:8}
.nt .ic{width:92px;height:92px;border-radius:24px;background:linear-gradient(135deg,#E8312A,#B32A46);display:flex;align-items:center;justify-content:center;font-size:52px;flex:none}
.nt .tx{flex:1}.nt b{display:block;font-size:38px;font-weight:800;letter-spacing:-1px}.nt b em{font-style:normal;color:#E8312A}.nt s{display:block;text-decoration:none;font-size:30px;color:#777;margin-top:4px}
.nt i{font-style:normal;font-size:26px;color:#999;align-self:flex-start;margin-top:30px}</style>
<div class="nt" id="n0" style="top:640px"><div class="ic">🔔</div><div class="tx"><b><em>미확인</em> 보험 발견</b><s>실손보험 · 2014년 가입</s></div><i>방금</i></div>
<div class="nt" id="n1" style="top:820px"><div class="ic">🔔</div><div class="tx"><b><em>미확인</em> 보험 발견</b><s>암보험 · 2017년 가입</s></div><i>방금</i></div>
<div class="nt" id="n2" style="top:1000px"><div class="ic">🔔</div><div class="tx"><b><em>미확인</em> 보험 발견</b><s>운전자보험 · 2019년 가입</s></div><i>방금</i></div>
<img class="ob" id="o_mdoc" src="m_doc.png" style="left:-20px;top:1260px;width:400px;z-index:9">
<img class="ob" id="o_mw" src="m_wink.png" style="left:-10px;top:1240px;width:470px;z-index:9">''')
R('''  [0,1,2].forEach(i=>{const a=SC[1]+0.4+i*0.35,p=eo(seg(t,a,a+.45)),q=seg(t,SC[2]-.25,SC[2]+.1);const ang=[-1,0,1][i];
    const c=$('c'+i);c.style.opacity=p*(1-q);c.style.transform=`translate(${ang*330*p}px,${(ang?-30:-220)*p+(1-p)*40}px) rotate(${ang*8*p}deg) scale(${(0.5+0.5*p)*(1-q*.3)})`;c.style.zIndex=i==1?3:2;
    c.querySelector('em').style.transform=`rotate(-8deg) scale(${cl(back(seg(t,a+.4,a+.65)),0,1.3)})`});''',
'''  [0.2,1.2,1.6].forEach((d,i)=>{const a=SC[1]+d,p=seg(t,a,a+.35),q=seg(t,SC[2]-.25,SC[2]);const n=$('n'+i);n.style.opacity=cl(p*3)*(1-q);
    n.style.transform=`translateY(${(1-cl(back(p),0,1.1))*-140-q*40}px) scale(${0.96+0.04*cl(p*2)})`});
  {const dim=seg(t,SC[1],SC[1]+.3)*(1-seg(t,SC[2]-.3,SC[2]));['av','bdg'].forEach(id=>{$(id).style.filter=`brightness(${1-0.35*dim}) blur(${dim*3}px)`})}''')
R('''#free{position:absolute;left:-330px;top:-170px;width:660px;height:340px;border:16px solid #FF3B3B;border-radius:36px;outline:6px solid #FF3B3B;outline-offset:10px;color:#FF3B3B;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;filter:url(#grunge);background:rgba(255,255,255,.04)}''',
'''#free{position:absolute;left:-400px;top:-270px;width:800px;height:auto;opacity:0;filter:drop-shadow(0 10px 18px rgba(0,0,0,.35))}''')
R('<div id="free"><div style="font-size:66px;font-weight:800;letter-spacing:2px">보장분석</div><div style="font-size:190px;font-weight:800;letter-spacing:-6px;line-height:1">무료</div></div>','<img id="free" src="free.png">')
R("$('free').style.transform=`rotate(-9deg) scale(${2.4-1.4*eo(p)})`","$('free').style.transform=`rotate(-12deg) scale(${p<1?3.2-2.2*eo(p):1+0.06*Math.exp(-(t-a-.16)*9)*Math.cos((t-a)*40)})`")
R("  F('o_holo',SC[4]+0.6,END,(p,k)=>`scale(${cl(back(p),0,1.25)}) translateY(${Math.sin(k*3)*10}px)`);",
"""  F('o_holo',SC[4]+0.6,END,(p,k)=>`scale(${cl(back(p),0,1.25)}) translateY(${Math.sin(k*3)*10}px)`);
  F('o_mdoc',SC[2]+0.5,SC[3],(p,k)=>`translateY(${(1-eo(p))*300+Math.sin(k*4)*8}px) rotate(${Math.sin(k*3)*3}deg)`);
  F('o_mw',SC[4]+0.45,END,(p,k)=>`translate(${(1-eo(p))*-300}px,${Math.sin(k*4)*8}px) rotate(${Math.sin(k*3)*3}deg) scale(${cl(back(p),0,1.15)})`);""")
open('index.html','w').write(s)
EOF
cd ../.. && W=1080 H=1920 TS=3.4,4.8,7.5,13.0,13.25,13.6,14.8 node render.cjs unkv3/site stills unkv3/st && python3 -c "
from PIL import Image
f=['3.4','4.8','7.5','13.0','13.25','13.6','14.8']
s=Image.new('RGB',(270*7,480))
for i,x in enumerate(f): s.paste(Image.open(f'unkv3/st/t{x}.png').convert('RGB').resize((270,480)),(i*270,0))
s.save('unkv3/sheet.jpg')"