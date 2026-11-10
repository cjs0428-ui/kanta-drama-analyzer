CSS='''
@font-face{font-family:P;src:url(fontp/Pretendard-Black.otf);font-weight:900}
@font-face{font-family:P;src:url(fontp/Pretendard-ExtraBold.otf);font-weight:800}
@font-face{font-family:P;src:url(fontp/Pretendard-Bold.otf);font-weight:700}
@font-face{font-family:P;src:url(fontp/Pretendard-SemiBold.otf);font-weight:600}
@font-face{font-family:P;src:url(fontp/Pretendard-Medium.otf);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
#a{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:P}
.hd{position:absolute;left:52px;top:44px;display:flex;align-items:center;gap:14px;font-size:30px;font-weight:600}
.hd .m{font-weight:900;font-size:46px;letter-spacing:-2px}
.hd .bar{width:3px;height:30px}
.sim{position:absolute;font-size:22px;font-weight:500}
'''
SIM='준법감시인 심의필 제OOOO-광고-OOOO호 (OOOO.OO.OO~OOOO.OO.OO)'
def hd(color,mcolor,barc): return f'<div class="hd" style="color:{color}"><span class="m" style="color:{mcolor}">meritz</span><span>메리츠화재</span><span class="bar" style="background:{barc}"></span><span>보장분석</span></div>'
# icons
def card(x,y,rot,label,icon,col):
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:220px;height:290px;background:#fff;border-radius:26px;box-shadow:0 18px 40px rgba(20,30,70,.2);transform:rotate({rot}deg)">
<div style="position:absolute;left:22px;top:26px;width:100px;height:100px;border-radius:50px;background:{col}1f;display:flex;align-items:center;justify-content:center;transform:scale(.85)">{icon}</div>
<div style="position:absolute;left:24px;top:146px;font-size:38px;font-weight:900;color:#1b2340;white-space:nowrap">{label}</div><div style="position:absolute;left:24px;top:198px;font-size:24px;font-weight:600;color:#9aa3b8">보장 ???</div></div>'''
I_CROSS='<svg width="64" height="64" viewBox="0 0 64 64"><rect x="24" y="6" width="16" height="52" rx="4" fill="#E0242F"/><rect x="6" y="24" width="52" height="16" rx="4" fill="#E0242F"/></svg>'
I_RIB='<svg width="64" height="70" viewBox="0 0 64 70"><path d="M32 6c-9 0-15 7-15 15 0 9 6 18 15 30 9-12 15-21 15-30 0-8-6-15-15-15z" fill="none" stroke="#F06292" stroke-width="9"/><path d="M20 46 8 64M44 46l12 18" stroke="#F06292" stroke-width="9" stroke-linecap="round"/></svg>'
I_BED='<svg width="76" height="56" viewBox="0 0 76 56"><rect x="2" y="4" width="8" height="50" rx="3" fill="#3B6FD8"/><circle cx="22" cy="22" r="9" fill="#3B6FD8"/><rect x="34" y="14" width="34" height="16" rx="6" fill="#3B6FD8"/><rect x="2" y="32" width="72" height="9" rx="3" fill="#3B6FD8"/><rect x="66" y="26" width="8" height="28" rx="3" fill="#3B6FD8"/></svg>'
I_CAR='<svg width="76" height="56" viewBox="0 0 76 56"><path d="M10 30l8-18c2-4 5-6 10-6h20c5 0 8 2 10 6l8 18v16H10z" fill="#13A37A"/><circle cx="22" cy="46" r="7" fill="#fff" stroke="#13A37A" stroke-width="5"/><circle cx="54" cy="46" r="7" fill="#fff" stroke="#13A37A" stroke-width="5"/><rect x="22" y="12" width="32" height="14" rx="3" fill="#fff" opacity=".8"/></svg>'
A=f'''<div id="a" style="background:linear-gradient(160deg,#F6F8FD,#E6ECF8)">{hd('#1b2340','#E0242F','#c3cadb')}
<div style="position:absolute;left:52px;top:150px;font-weight:900;font-size:96px;line-height:1.12;letter-spacing:-4px;color:#1b2340">내 보험,<br><span style="color:#E0242F">몇 개</span> 가입돼<br>있을까?</div>
<div style="position:absolute;left:56px;top:500px;font-size:34px;font-weight:600;color:#5b6480;line-height:1.45">흩어진 내 보험,<br>한 번에 모아 보여드려요</div>
{card(420,520,-12,'실손',I_CROSS,'#E0242F')}{card(560,480,-4,'암',I_RIB,'#F06292')}{card(700,470,4,'수술',I_BED,'#3B6FD8')}{card(830,500,12,'운전자',I_CAR,'#13A37A')}
<div style="position:absolute;left:900px;top:395px;width:120px;height:120px;border-radius:65px;background:#E0242F;color:#fff;font-weight:900;font-size:84px;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 30px rgba(224,36,47,.45)">?</div>
<div style="position:absolute;left:52px;top:880px;background:#E0242F;color:#fff;font-weight:800;font-size:42px;padding:22px 46px;border-radius:999px;box-shadow:0 12px 28px rgba(224,36,47,.35)">앱에서 1분 확인하기 ›</div>
<div class="sim" style="left:56px;bottom:30px;color:#8a92a8">{SIM}</div></div>'''
B=f'''<div id="a" style="background:radial-gradient(circle at 50% 35%,#24438C,#0D1A3E 75%)">{hd('#fff','#fff','rgba(255,255,255,.5)')}
<div style="position:absolute;left:0;right:0;top:150px;text-align:center;font-weight:900;font-size:64px;color:#fff;letter-spacing:-2px">내 보장,</div>
<div style="position:absolute;left:0;right:0;top:225px;text-align:center;font-weight:900;font-size:112px;color:#FFE14A;letter-spacing:-5px">또래보다 부족할까?</div>
<div style="position:absolute;left:190px;top:410px;width:700px;height:440px;background:#fff;border-radius:36px;box-shadow:0 24px 60px rgba(0,0,0,.35)">
 <div style="position:absolute;left:44px;top:34px;font-size:30px;font-weight:800;color:#1b2340">보장 비교</div>
 <div style="position:absolute;left:44px;right:44px;top:360px;height:3px;background:#e3e7f0"></div>
 <div style="position:absolute;left:150px;top:150px;width:140px;height:210px;border-radius:18px 18px 0 0;background:repeating-linear-gradient(45deg,#d9dde8,#d9dde8 14px,#e9ecf3 14px,#e9ecf3 28px)"></div>
 <div style="position:absolute;left:170px;top:70px;width:100px;height:100px;border-radius:50px;background:#E0242F;color:#fff;font-weight:900;font-size:64px;display:flex;align-items:center;justify-content:center">?</div>
 <div style="position:absolute;left:410px;top:110px;width:140px;height:250px;border-radius:18px 18px 0 0;background:linear-gradient(#5B8CFF,#2D5BD8)"></div>
 <div style="position:absolute;left:150px;top:376px;width:140px;text-align:center;font-size:32px;font-weight:800;color:#E0242F">나</div>
 <div style="position:absolute;left:410px;top:376px;width:140px;text-align:center;font-size:32px;font-weight:800;color:#2D5BD8">또래</div>
</div>
<div class="sim" style="left:0;right:0;text-align:center;bottom:128px;color:rgba(255,255,255,.75)">{SIM}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:#FFE14A;color:#0D1A3E;font-weight:900;font-size:44px;display:flex;align-items:center;justify-content:center">앱에서 또래랑 비교하기 ›</div></div>'''
C=f'''<div id="a" style="background:linear-gradient(135deg,#FF6B5B,#FF9A44)">{hd('#fff','#fff','rgba(255,255,255,.6)')}
<div style="position:absolute;left:52px;top:160px;font-weight:900;font-size:90px;line-height:1.15;letter-spacing:-4px;color:#fff;text-shadow:0 6px 20px rgba(150,40,20,.25)">내 보험점수는<br><span style="color:#FFF3A6">몇 점</span>일까?</div>
<div style="position:absolute;left:56px;top:400px;font-size:34px;font-weight:600;color:#fff;opacity:.95;line-height:1.45">가입한 보험을 한 번에 분석해<br>점수로 알려드려요</div>
<div style="position:absolute;left:560px;top:430px;width:430px;height:820px;border-radius:64px;background:#141414;transform:rotate(12deg);box-shadow:0 30px 60px rgba(120,30,10,.4);padding:16px">
 <div style="width:100%;height:100%;border-radius:50px;background:#fff;position:relative;overflow:hidden">
  <div style="position:absolute;left:36px;top:48px;font-size:26px;font-weight:800;color:#E0242F">meritz <span style="color:#777;font-weight:600">보장분석</span></div>
  <div style="position:absolute;left:36px;top:96px;font-size:34px;font-weight:800;color:#1b1b1b">내 보험점수</div>
  <svg style="position:absolute;left:40px;top:170px" width="320" height="180" viewBox="0 0 320 180"><path d="M30 160 A130 130 0 0 1 290 160" fill="none" stroke="#eee" stroke-width="30" stroke-linecap="round"/><path d="M30 160 A130 130 0 0 1 120 38" fill="none" stroke="#E0242F" stroke-width="30" stroke-linecap="round"/></svg>
  <div style="position:absolute;left:0;right:0;top:260px;text-align:center;font-size:84px;font-weight:900;color:#1b1b1b">??<span style="font-size:36px">점</span></div>
  <div style="position:absolute;left:36px;right:36px;top:420px;height:20px;border-radius:10px;background:#f1f1f1"></div>
  <div style="position:absolute;left:36px;right:120px;top:460px;height:20px;border-radius:10px;background:#f1f1f1"></div>
 </div></div>
<div style="position:absolute;left:52px;top:780px;background:#fff;color:#E0423B;font-weight:900;font-size:42px;padding:22px 44px;border-radius:24px;box-shadow:0 14px 30px rgba(140,40,20,.3)">앱에서 내 점수 확인 ›</div>
<div class="sim" style="left:56px;bottom:30px;color:rgba(255,255,255,.9);width:470px;line-height:1.35">준법감시인 심의필 제OOOO-광고-OOOO호<br>(OOOO.OO.OO~OOOO.OO.OO)</div></div>'''
for k,b in [('A',A),('B',B),('C',C)]:
    open(f'app_{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}</body></html>')
