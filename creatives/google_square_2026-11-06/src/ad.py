import json,sys
CSS='''
@font-face{font-family:P;src:url(fontp/Pretendard-Black.otf);font-weight:900}
@font-face{font-family:P;src:url(fontp/Pretendard-ExtraBold.otf);font-weight:800}
@font-face{font-family:P;src:url(fontp/Pretendard-Bold.otf);font-weight:700}
@font-face{font-family:P;src:url(fontp/Pretendard-SemiBold.otf);font-weight:600}
@font-face{font-family:P;src:url(fontp/Pretendard-Medium.otf);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
#a{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:P;color:#151515}
#a>img{position:absolute;inset:0;width:100%;height:100%}
.brand{position:absolute;right:40px;top:34px;font-weight:900;font-size:34px;color:#E0242F;letter-spacing:-1px;text-shadow:0 0 12px rgba(255,255,255,.9)}
.chip{position:absolute;left:56px;top:40px;background:#E0242F;color:#fff;font-weight:800;font-size:30px;padding:8px 20px;border-radius:999px;transform:rotate(-3deg);box-shadow:0 6px 16px rgba(0,0,0,.25)}
.hl{position:absolute;left:56px;font-weight:900;letter-spacing:-3px;line-height:1.12}
.hl em{font-style:normal;color:#E0242F}
.hl.w{color:#fff;text-shadow:0 4px 18px rgba(0,0,0,.55)}
.hl.w em{color:#FFE14A}
.hl.k{text-shadow:0 0 18px rgba(255,255,255,.95),0 0 36px rgba(255,255,255,.8)}
.sub{position:absolute;left:56px;font-weight:700;font-size:34px;letter-spacing:-1px;background:rgba(255,255,255,.92);padding:8px 16px;border-radius:12px;box-shadow:0 6px 16px rgba(0,0,0,.18)}
.band{position:absolute;left:0;right:0;bottom:0;height:250px;background:linear-gradient(rgba(0,0,0,0),rgba(0,0,0,.72) 38%,rgba(0,0,0,.82))}
.cta{position:absolute;left:56px;bottom:112px;background:#E0242F;color:#fff;font-weight:800;font-size:36px;padding:14px 34px;border-radius:999px;box-shadow:0 8px 20px rgba(224,36,47,.45)}
.pts{position:absolute;left:56px;right:40px;color:#fff;font-weight:700;font-size:31px;line-height:1.45}
.pts b{color:#FFE14A;font-weight:800}
.disc{position:absolute;left:56px;right:40px;bottom:22px;color:rgba(255,255,255,.92);font-weight:500;font-size:28px;line-height:1.3;letter-spacing:-.5px}
.card{position:absolute;font-weight:900;color:#1a1a1a;text-align:center;line-height:1.18;letter-spacing:-1.5px}
'''
def page(body,img):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="a"><img src="{img}">{body}</div></body></html>'
DISC='※ 상품 및 심사 결과에 따라 가입이 제한되거나 조건이 붙을 수 있습니다.<br>준법감시인 심의필 제OOOO호(2026.00.00~2027.00.00)'
DISC2='※ 간편보험은 일반심사 상품보다 보험료가 높을 수 있으며, 심사 결과에 따라<br>가입이 제한될 수 있습니다. 준법감시인 심의필 제OOOO호'
ads={
'g1a':('g1a_1080.jpg',f'''<div class="brand">메리츠화재</div><div class="chip">3040 자녀라면</div>
<div class="hl k" style="top:104px;font-size:70px">엄마 아빠 보험,<br>마지막으로 본 게<br><em>언제</em>예요?</div>
<div class="band" style="height:300px"></div><div class="pts" style="bottom:190px">자녀가 대신 확인하는 <b>부모님 보장분석</b></div><div class="cta">부모님 보장분석 1분 ›</div><div class="disc">{DISC}</div>'''),
'g1b':('g1b_1080.jpg',f'''<div class="brand">메리츠화재</div><div class="chip">3040 자녀라면</div>
<div class="hl k" style="top:104px;font-size:66px">부모님 보험,<br><em>'알아서 하셨겠지'</em><br>하고 넘기셨나요?</div>
<div class="band" style="height:300px"></div><div class="pts" style="bottom:190px">자녀가 대신 확인하는 <b>부모님 보장분석</b></div><div class="cta">부모님 보장분석 1분 ›</div><div class="disc">{DISC}</div>'''),
'g2a':('g2a_1080.jpg',f'''<div class="brand" style="text-shadow:none;color:#fff">메리츠화재</div>
<div class="hl w" style="left:auto;right:44px;top:96px;font-size:84px;text-align:right">이거 다<br><em>오해</em>예요!</div>
<div class="card" style="left:72px;top:290px;width:236px;font-size:33px;transform:rotate(7deg)">병력 있으면<br>가입 자체가<br>안 된다?</div>
<div class="card" style="left:296px;top:422px;width:200px;font-size:29px;transform:rotate(9deg)">한 번 아프면<br>건강체 가입은<br>끝?</div>
<div class="band" style="height:330px"></div>
<div class="pts" style="bottom:190px">✔ 병력이 있어도 <b>간편심사</b>로 가입 검토 가능<br>✔ 치료·경과에 따라 <b>일반심사(건강체)</b>도 검토 가능</div>
<div class="cta" style="bottom:104px;font-size:32px;padding:12px 30px">1분 보장분석 ›</div><div class="disc" style="font-size:27px">{DISC2}</div>'''),
'g2b':('g2b_1080.jpg',f'''<div class="brand">메리츠화재</div>
<div class="hl k" style="top:70px;font-size:76px">약 먹으면 보험 끝?<br>그거 <em>오해</em>예요!</div>
<div class="band" style="height:330px"></div>
<div class="pts" style="bottom:190px">✔ 병력이 있어도 <b>간편심사</b>로 가입 검토 가능<br>✔ 치료·경과에 따라 <b>일반심사(건강체)</b>도 검토 가능</div>
<div class="cta" style="bottom:104px;font-size:32px;padding:12px 30px">1분 보장분석 ›</div><div class="disc" style="font-size:27px">{DISC2}</div>'''),
}
for k,(img,body) in ads.items(): open(f'{k}.html','w').write(page(body,img))
