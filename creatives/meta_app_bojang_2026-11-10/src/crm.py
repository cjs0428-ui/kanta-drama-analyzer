CSS='''
@font-face{font-family:P;src:url(fontp/Pretendard-Black.otf);font-weight:900}
@font-face{font-family:P;src:url(fontp/Pretendard-ExtraBold.otf);font-weight:800}
@font-face{font-family:P;src:url(fontp/Pretendard-Bold.otf);font-weight:700}
@font-face{font-family:P;src:url(fontp/Pretendard-SemiBold.otf);font-weight:600}
@font-face{font-family:P;src:url(fontp/Pretendard-Medium.otf);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
#a{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:P}
.ap{width:64px;height:64px;border-radius:16px;background:#E0242F;color:#fff;font-weight:900;font-size:34px;display:flex;align-items:center;justify-content:center;flex:none}
'''
SIM='준법감시인 심의필 제OOOO-광고-OOOO호 (OOOO.OO.OO~OOOO.OO.OO)'
def notif(top,title,body,time,op=1,scale=1,hl=False):
    return f'''<div style="position:absolute;left:{60+(1-scale)*480}px;right:{60+(1-scale)*480}px;top:{top}px;opacity:{op};background:rgba(255,255,255,{.92 if hl else .55});backdrop-filter:blur(20px);border-radius:36px;padding:26px 30px;display:flex;gap:22px;box-shadow:0 14px 40px rgba(40,70,120,{.22 if hl else .08})">
<div class="ap">M</div><div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;font-size:26px;color:#6b7690;font-weight:600"><span>메리츠화재 보장분석</span><span>{time}</span></div>
<div style="font-size:36px;font-weight:800;color:#141B2D;margin-top:6px;white-space:nowrap">{title}</div><div style="font-size:28px;font-weight:500;color:#4a5570;margin-top:6px;white-space:nowrap">{body}</div></div></div>'''
def chk(ok,label):
    box=('<div style="width:40px;height:40px;border-radius:10px;background:#2D5BD8;display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 26 26"><path d="M5 13l5 5 11-12" stroke="#fff" stroke-width="4.5" fill="none" stroke-linecap="round"/></svg></div>' if ok else
         '<div style="width:40px;height:40px;border-radius:10px;border:4px dashed #E0242F;background:#fff"></div>')
    lab=f'<span style="font-size:32px;font-weight:{700 if ok else 900};color:{"#141B2D" if ok else "#E0242F"}">{label}</span>'
    tail='' if ok else '<span style="margin-left:auto;background:#FFE3E5;color:#E0242F;font-weight:800;font-size:24px;padding:6px 16px;border-radius:999px">확인 필요</span>'
    return f'<div style="display:flex;align-items:center;gap:20px;padding:16px 0;border-bottom:2px solid #EEF1F7">{box}{lab}{tail}</div>'
B=f'''<div id="a" style="background:linear-gradient(170deg,#DCEBFF 0%,#EAF2FF 45%,#F6F9FF 100%)">
<div style="position:absolute;left:0;right:0;top:70px;text-align:center;font-size:34px;font-weight:600;color:#4a5570">11월 12일 수요일</div>
<div style="position:absolute;left:0;right:0;top:110px;text-align:center;font-size:190px;font-weight:800;color:#141B2D;letter-spacing:-6px;line-height:1">9:41</div>
<div style="position:absolute;left:0;right:0;top:335px;text-align:center;font-size:66px;font-weight:900;color:#141B2D;letter-spacing:-3px">내 보장에 <span style="color:#E0242F">빈칸</span> 있다는 알림?</div>
{notif(470,'보장 공백 확인이 필요해요 🔔','가입한 보험 중 비어 있는 보장을 확인해 보세요','지금',1,1,True)}
<div style="position:absolute;left:60px;right:60px;top:640px;background:#fff;border-radius:36px;padding:26px 40px;box-shadow:0 14px 40px rgba(40,70,120,.15)">
<div style="font-size:28px;font-weight:700;color:#6b7690;margin-bottom:6px">내 보장 체크리스트</div>
{chk(True,'실손 의료비')}{chk(True,'암 진단비')}{chk(False,'뇌·심장 진단비')}{chk(True,'수술비')}</div>
{notif(1000,'보험료 납입 안내','이번 달 보험료가 정상 납입되었어요','1시간 전',.6,.94)}
<div style="position:absolute;left:50%;transform:translateX(-50%);top:1196px;background:#141B2D;color:#fff;font-weight:800;font-size:40px;padding:22px 54px;border-radius:999px;white-space:nowrap;box-shadow:0 12px 30px rgba(20,27,45,.3)">앱에서 1분 확인하기 ›</div>
<div style="position:absolute;left:0;right:0;bottom:22px;text-align:center;font-size:20px;color:#7d8699">※ 예시 화면입니다. {SIM}</div></div>'''
C=f'''<div id="a" style="background:#FBF6EE">
<div style="position:absolute;left:-120px;top:-160px;width:620px;height:620px;border-radius:50%;background:#FFE7C7"></div>
<div style="position:absolute;right:-180px;bottom:120px;width:560px;height:560px;border-radius:50%;background:#FFEFD9"></div>
<div style="position:absolute;left:70px;top:90px;display:flex;align-items:center;gap:14px;font-size:30px;font-weight:700;color:#3a2f25"><span style="font-weight:900;font-size:44px;color:#E0242F;letter-spacing:-2px">meritz</span>메리츠화재 · 보장분석</div>
<div style="position:absolute;left:70px;top:190px;font-size:96px;font-weight:900;line-height:1.12;letter-spacing:-5px;color:#2B2118">또래랑 비교한<br>내 보장 <span style="color:#E0242F">리포트</span>가<br>도착했어요</div>
<div style="position:absolute;left:70px;right:70px;top:540px;background:#fff;border-radius:44px;box-shadow:0 24px 60px rgba(120,80,30,.16);overflow:hidden">
 <div style="background:#2B2118;color:#fff;padding:28px 40px;display:flex;align-items:center;gap:18px;font-size:32px;font-weight:800"><span style="font-size:36px">✉</span>보장 비교 리포트<span style="margin-left:auto;background:#E0242F;border-radius:999px;font-size:24px;padding:6px 16px">NEW</span></div>
 <div style="padding:34px 44px 40px">
  <div style="font-size:36px;font-weight:800;color:#2B2118;line-height:1.4">내 보장, <span style="color:#E0242F">또래보다 부족할까?</span><br><span style="font-size:28px;font-weight:600;color:#7a6a5a">항목별 비교 결과가 준비됐어요</span></div>
  <div style="position:relative;height:220px;margin-top:20px;border-bottom:4px solid #E9DFD2">
   <div style="position:absolute;left:150px;bottom:0;width:150px;height:130px;border:5px dashed #E0242F;border-bottom:none;border-radius:20px 20px 0 0;background:#FFF5F5;display:flex;align-items:center;justify-content:center;font-size:70px;font-weight:900;color:#E0242F">?</div>
   <div style="position:absolute;left:470px;bottom:0;width:150px;height:200px;border-radius:20px 20px 0 0;background:linear-gradient(#FFB45C,#F08A24)"></div>
  </div>
  <div style="position:relative;height:56px;font-size:32px;font-weight:800"><span style="position:absolute;left:150px;width:150px;text-align:center;color:#E0242F;top:10px">나</span><span style="position:absolute;left:470px;width:150px;text-align:center;color:#B8691C;top:10px">또래</span></div>
  <div style="margin-top:22px;background:#E0242F;color:#fff;text-align:center;font-weight:900;font-size:40px;padding:24px;border-radius:24px">앱에서 결과 보기 ›</div>
 </div></div>
<div style="position:absolute;left:0;right:0;bottom:22px;text-align:center;font-size:20px;line-height:1.45;color:#9a8a78">※ 예시 화면이며, 또래 기준은 보장분석 이용자 연령대 기준입니다.<br>{SIM}</div></div>'''
for k,b in [('B2',B),('C2',C)]: open(f'{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}</body></html>')
