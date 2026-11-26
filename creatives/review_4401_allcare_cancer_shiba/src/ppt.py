import copy
from pptx import Presentation
from pptx.oxml.ns import qn
from lxml import etree
p=Presentation('src.pptx')
def set_text(sh, lines):
    tb=sh.text_frame._txBody; ps=tb.findall(qn('a:p')); proto=ps[0]
    for x in ps: tb.remove(x)
    for ln in lines:
        np_=copy.deepcopy(proto); rs=np_.findall(qn('a:r'))
        for r in rs[1:]: np_.remove(r)
        for br in np_.findall(qn('a:br')): np_.remove(br)
        if rs: rs[0].find(qn('a:t')).text=ln
        else:
            r=etree.SubElement(np_,qn('a:r')); t=etree.SubElement(r,qn('a:t')); t.text=ln
        tb.append(np_)
def shp(s,name,left=None):
    c=[x for x in s.shapes if x.name==name]
    if left is not None: c=[x for x in c if (x.left<6000000)==(left=='L')]
    return c[0]
def replace_pics(s,side,img):
    pics=[x for x in s.shapes if x.shape_type==13 and ((x.left<6000000)==(side=='L'))]
    x0=min(x.left for x in pics); y0=min(x.top for x in pics); x1=max(x.left+x.width for x in pics); y1=max(x.top+x.height for x in pics)
    for x in pics: x._element.getparent().remove(x._element)
    h=y1-y0; w=int(h*1080/1920); left=x0+((x1-x0)-w)//2
    s.shapes.add_picture(img,left,y0,w,h)
S=p.slides
# slide 10: S#5 (L), S#6 (R)
s=S[9]
set_text(shp(s,'Google Shape;112;p4'),['통합암 진단비는 전이암까지 포함!','[기본계약] 갱신형 통합암진단비(전이포함)','※ 유사암 제외 / 암보장개시일(가입일부터 90일이 지난 다음날) 이후 진단 확정 시 각 최초 1회한 지급 / 특정소액암은 1년 이내 20% 지급'])
set_text(shp(s,'Google Shape;119;p4'),['통합암 주요치료비는 10년간 연 1회 한도로 보장','[선택계약(특약)] 갱신형 암통합치료비(실속형)','※ 암 통합치료보장개시일 이후 진단 확정 후 주요치료 시 통합치료항목별 연간 1회한 지급(수술은 1회당) / 항목별 지급금액 상이'])
set_text(shp(s,'Google Shape;114;p4'),['돋보기, 인체 모형 통해 암을 찾는 듯한 모션 적용','하단에 기본계약 표기 및 지급제한사항 병기'])
set_text(shp(s,'Google Shape;121;p4'),['약이 쌓여 있는 배경, 기뻐하는 표정 통해 연 1회 한도로 보장해줌을 시각적 어필','하단에 계약 구분(선택계약·특약) 및 지급제한사항 병기'])
replace_pics(s,'L','pp_13.jpg'); replace_pics(s,'R','pp_16.jpg')
# slide 11: S#7 (L), S#8 (R)
s=S[10]
set_text(shp(s,'Google Shape;112;p4'),['항암 중입자 방사선 치료비도 특약으로 챙길 수 있어요','[선택계약(특약)] 갱신형 항암중입자방사선치료비','※ 암보장개시일 이후 암(유사암 제외) 진단 확정 후 항암중입자방사선치료 시 최초 1회한 지급 / 1년 이내 50% 지급'])
set_text(shp(s,'Google Shape;114;p4'),['항암 중입자 방사선 치료 시각적 삽입, ‘특약’ 도장 효과','하단에 지급제한사항 병기'])
set_text(shp(s,'Google Shape;121;p4'),['서류 더미 시각자료 삽입','(서류·영수증 내 금액, 원화·달러 기호 미노출)'])
replace_pics(s,'L','pp_20.jpg'); replace_pics(s,'R','pp_23.jpg')
# slide 12: S#10 (R)
s=S[11]
set_text(shp(s,'Google Shape;119;p4'),['올케어 암보험, 내 보험료는 얼마?','간편하게 확인해 보세요!'])
replace_pics(s,'R','pp_29.3.jpg')
# slide 13: S#11
s=S[12]
sh=shp(s,'Google Shape;119;p4'); hit=0
for para in sh.text_frame.paragraphs:
    for r in para.runs:
        if '지금 바로 계산해보세요' in r.text: r.text=r.text.replace('지금 바로 계산해보세요','간편하게 확인해 보세요'); hit+=1
        if '지금 바로 계산해 보세요' in r.text: r.text=r.text.replace('지금 바로 계산해 보세요','간편하게 확인해 보세요'); hit+=1
print('S11 replaced runs',hit, repr(sh.text_frame.paragraphs[0].text[:60]))
replace_pics(s,'L','pp_32.jpg')
# leftovers
for i,sl in enumerate(S):
    for x in sl.shapes:
        if x.has_text_frame and ('지금 바로' in x.text_frame.text or '계산해' in x.text_frame.text): print('LEFT',i+1,x.name,x.text_frame.text[:80].replace('\n','|'))
p.save('out.pptx')
