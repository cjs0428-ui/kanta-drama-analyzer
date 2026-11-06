import json
STATES={
'S0':{'q':'혈','rows':[],'cards':0},
'S1':{'q':'혈압','rows':[('혈압 ','재검 소견'),('혈압 ','소견 보험 가입'),('혈압 ','재검 기준'),('혈압 ','정상 수치'),('혈압 ','유병자 보험')],'cards':0},
'S2':{'q':'혈압 재검 소','rows':[('혈압 재검 소','견 보험 가입'),('혈압 재검 소','견 보험 거절'),('혈압 재검 소','견 실비'),('혈압 재검 소','견 보험 고지')],'cards':0},
'S3':{'q':'혈압 재검 소견 보험','rows':[('혈압 재검 소견 보험 ',x) for x in ['가입 못 하나요','거절','포기','고지해야 하나요','조건']],'cards':1},
'S4':{'q':'혈압 재검 소견 보험','rows':[('혈압 재검 소견 보험 ',x) for x in ['가입 못 하나요','거절','포기','고지해야 하나요','조건']],'cards':2},
'S5':{'q':'혈압 재검 소견 보험','rows':[('혈압 재검 소견 보험 ',x) for x in ['가입 못 하나요','거절','포기','고지해야 하나요','조건']],'cards':3},
}
CARDS=[('혈압 재검 소견, 보험 가입 불가?','소견만 나와도 가입이 어렵다는데…'),('재검 소견, 보험 거절되나요?','고지하면 무조건 거절이라는 얘기가…'),('유병자 보험 가입 후기 모음','조건이 다 다르다는데 뭐가 뭔지…')]
CSS='''html,body{margin:0;background:transparent}#c{position:relative;width:1080px;height:1920px}
#s{position:absolute;left:240px;top:360px;width:600px;height:960px;background:#fff;font-family:'Noto Sans KR'}
.q{position:absolute;left:20px;top:14px;width:554px;height:84px;border:3px solid #3B6FD8;border-radius:46px;box-sizing:border-box}
.q span{position:absolute;left:37px;top:14px;font-size:34px;font-weight:400;color:#111}
.q i{display:inline-block;width:3px;height:38px;background:#3B6FD8;vertical-align:-6px;margin-left:2px}
.r{position:absolute;left:20px;width:560px;height:64px;border-bottom:1px solid #ececec;box-sizing:border-box}
.r svg{position:absolute;left:14px;top:22px}
.r span{position:absolute;left:56px;top:12px;font-size:29px;color:#9a9a9a;white-space:nowrap}
.r b{color:#111;font-weight:700}
.h{position:absolute;left:36px;top:470px;font-size:24px;color:#777}
.cd{position:absolute;left:20px;width:560px;height:126px;background:#EEEFF6;border-radius:24px}
.cd .t{position:absolute;left:24px;top:18px;font-size:31px;font-weight:700;color:#1B2A9A;white-space:nowrap}
.cd .u{position:absolute;left:24px;top:70px;font-size:25px;color:#666;white-space:nowrap}
'''
ICON='<svg width="22" height="22" viewBox="0 0 22 22"><circle cx="9" cy="9" r="7" stroke="#9a9a9a" stroke-width="2.5" fill="none"/><line x1="14" y1="14" x2="20" y2="20" stroke="#9a9a9a" stroke-width="2.5"/></svg>'
for k,s in STATES.items():
    h=f'<div class="q"><span>{s["q"]}<i></i></span></div>'
    for j,(g,b) in enumerate(s['rows']): h+=f'<div class="r" style="top:{122+64*j}px">{ICON}<span>{g}<b>{b}</b></span></div>'
    if s['cards']:
        h+='<div class="h">관련 게시물</div>'
        for j in range(s['cards']):
            t,u=CARDS[j];h+=f'<div class="cd" style="top:{516+144*j}px"><div class="t">{t}</div><div class="u">{u}</div></div>'
    open(f'ui_{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fns/package/400.css"><link rel="stylesheet" href="fns/package/700.css"><style>{CSS}</style></head><body><div id="c"><div id="s">{h}</div></div></body></html>')
