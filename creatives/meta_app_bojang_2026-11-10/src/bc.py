CSS='''
@font-face{font-family:P;src:url(fontp/Pretendard-Black.otf);font-weight:900}
@font-face{font-family:P;src:url(fontp/Pretendard-ExtraBold.otf);font-weight:800}
@font-face{font-family:P;src:url(fontp/Pretendard-Bold.otf);font-weight:700}
@font-face{font-family:P;src:url(fontp/Pretendard-SemiBold.otf);font-weight:600}
@font-face{font-family:P;src:url(fontp/Pretendard-Medium.otf);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
#a{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:P;background:linear-gradient(120deg,#B52D4A 0%,#8E2A5E 50%,#5E2770 100%)}
.hd{position:absolute;left:52px;top:46px;display:flex;align-items:center;gap:14px;font-size:30px;font-weight:600;color:#fff}
.hd .m{font-weight:900;font-size:46px;letter-spacing:-2px}
.dots{position:absolute;left:0;right:0;top:128px;text-align:center;color:#FFE9A6;font-size:40px;letter-spacing:70px;padding-left:70px}
.h1{position:absolute;left:0;right:0;text-align:center;font-weight:900;color:#FFF0A0;letter-spacing:-5px}
.h2{position:absolute;left:0;right:0;text-align:center;font-weight:800;color:#fff;letter-spacing:-2px}
.ring1{position:absolute;left:290px;top:400px;width:500px;height:500px;border-radius:50%;border:3px solid rgba(255,255,255,.35)}
.ring2{position:absolute;left:330px;top:440px;width:420px;height:420px;border-radius:50%;border:5px solid #fff}
.core{position:absolute;left:375px;top:485px;width:330px;height:330px;border-radius:50%;background:#D9D9DE;display:flex;align-items:center;justify-content:center}
.badge{position:absolute;width:104px;height:104px;border-radius:52px;background:#E8202A;color:#fff;font-weight:900;font-size:62px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(0,0,0,.3)}
.sim{position:absolute;left:36px;bottom:112px;font-size:21px;color:rgba(255,255,255,.85)}
.cta{position:absolute;left:0;right:0;bottom:0;height:96px;background:#4A1A50;color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center}
'''
HD='<div class="hd"><span class="m">meritz</span><span>메리츠화재</span><span style="width:3px;height:30px;background:rgba(255,255,255,.6)"></span><span>보장분석</span></div>'
SIM='<div class="sim">준법감시인 심의필 제OOOO-광고-OOOO호 (OOOO.OO.OO~OOOO.OO.OO)</div>'
CTA='<div class="cta">앱에서 1분 확인하기 ›</div>'
# B: checklist with one empty row
def CHK(ok,y):
    fill='#8E8E96' if ok else '#fff'
    stroke='none' if ok else '#E8202A'
    dash='' if ok else 'stroke-dasharray="6 5"'
    tick='<path d="M8 17l7 7 12-14" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if ok else ''
    bar='#A6A6AE' if ok else '#F3B6BA'
    return f'<g transform="translate(0,{y})"><rect x="0" y="0" width="34" height="34" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="4" {dash}/>{tick}<rect x="52" y="9" width="120" height="16" rx="8" fill="{bar}"/></g>'
B_ICON='<svg width="200" height="230" viewBox="0 0 200 230"><rect x="10" y="10" width="180" height="210" rx="20" fill="#fff"/><rect x="62" y="0" width="76" height="26" rx="10" fill="#8E8E96"/><g transform="translate(30,50)">'+CHK(True,0)+CHK(True,44)+CHK(False,88)+CHK(True,132)+'</g></svg>'
B=f'''<div id="a">{HD}<div class="dots">• • •</div>
<div class="h1" style="top:160px;font-size:124px">보장 공백</div>
<div class="h2" style="top:300px;font-size:64px">확인이 필요합니다</div>
<div class="ring1"></div><div class="ring2"></div><div class="core">{B_ICON}</div>
<div class="badge" style="left:660px;top:470px">!</div>{SIM}{CTA}</div>'''
# C: me vs peers bars
C_ICON='''<svg width="230" height="200" viewBox="0 0 230 200"><line x1="10" y1="170" x2="220" y2="170" stroke="#9A9AA2" stroke-width="5"/>
<rect x="40" y="60" width="62" height="110" rx="8" fill="#fff" stroke="#E8202A" stroke-width="5" stroke-dasharray="10 7"/>
<rect x="132" y="30" width="62" height="140" rx="8" fill="#8E8E96"/>
<text x="71" y="128" text-anchor="middle" font-family="P" font-weight="900" font-size="48" fill="#E8202A">?</text>
<text x="71" y="198" text-anchor="middle" font-family="P" font-weight="800" font-size="24" fill="#E8202A">나</text>
<text x="163" y="198" text-anchor="middle" font-family="P" font-weight="800" font-size="24" fill="#6E6E76">또래</text></svg>'''
C=f'''<div id="a">{HD}<div class="dots">• • •</div>
<div class="h1" style="top:160px;font-size:118px">내 보장,</div>
<div class="h2" style="top:296px;font-size:68px">또래보다 부족할까?</div>
<div class="ring1"></div><div class="ring2"></div><div class="core">{C_ICON}</div>
<div class="badge" style="left:660px;top:470px">?</div>{SIM}{CTA}</div>'''
for k,b in [('B',B),('C',C)]: open(f'{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}</body></html>')
