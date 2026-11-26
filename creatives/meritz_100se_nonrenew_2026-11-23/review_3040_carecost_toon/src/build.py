import copy, sys
from pptx import Presentation
from lxml import etree
from pptx.oxml.ns import qn
SRC='/home/user/kanta-drama-analyzer/creatives/meritz_simple_health_2026-11-24/2030_recheck_washing/심의안_메타_보험료확인_수정.pptx'
OUT=sys.argv[1]
V='/tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/v3040/'
p=Presentation(SRC)

def set_text(sh, lines):
    tf=sh.text_frame; txBody=tf._txBody
    ps=txBody.findall(qn('a:p')); proto=ps[0]
    for x in ps: txBody.remove(x)
    for ln in lines:
        np_=copy.deepcopy(proto)
        rs=np_.findall(qn('a:r'))
        for r in rs[1:]: np_.remove(r)
        for br in np_.findall(qn('a:br')): np_.remove(br)
        if rs:
            rs[0].find(qn('a:t')).text=ln
        else:
            r=etree.SubElement(np_,qn('a:r')); t=etree.SubElement(r,qn('a:t')); t.text=ln
            end=np_.find(qn('a:endParaRPr'))
            if end is not None: np_.remove(end); np_.append(end)
        txBody.append(np_)

def set_pic(slide, pic, path):
    _, rId = slide.part.get_or_add_image_part(path)
    pic._element.blipFill.find(qn('a:blip')).set(qn('r:embed'), rId)

def rep_all(sh, a, b):
    for para in sh.text_frame.paragraphs:
        for r in para.runs:
            if a in r.text: r.text=r.text.replace(a,b)

PROD='올바른 100세 건강보험'
# slide 1
for sh in p.slides[0].shapes:
    if sh.has_text_frame and '간편보험' in sh.text_frame.text: set_text(sh,[PROD])
# slide 5 ad preview
s=p.slides[4]
COPY=['우리 엄마 간병비, 나라가 내준다길래 안심했는데 지원은 일부래요😯',
      '암·뇌졸중·심장질환 같은 큰 병은 비갱신형으로 보장받을 수 있어요🙌',
      '⭐메리츠화재 올바른 100세 건강보험⭐',
      '나와 부모님 보험료, 한 번에 확인해보세요!',
      '(※ 비갱신형은 갱신형 대비 초기 보험료가 높을 수 있음)']
for sh in s.shapes:
    if not sh.has_text_frame: 
        if sh.shape_type==13: set_pic(s,sh,V+'k_1.5.png')
        continue
    t=sh.text_frame.text
    if t.startswith('건강검진에서'): set_text(sh,COPY)
    elif t=='1분 간편 보험료 확인하기': set_text(sh,['가족 보험료 확인하기'])
# slide 6 table
for sh in p.slides[5].shapes:
    if sh.has_table:
        rows=sh.table.rows
        vals=['메타(페이스북·인스타그램) 지면 광고에 노출되는 유저',
              '암·뇌졸중·심장질환 같은 큰 병을 비갱신형으로 보장받을 수 있는 올바른 100세 건강보험, 나와 부모님 보험료를 한 번에 확인',
              '부모님 간병비 국가 지원이 일부에 그친다는 사실을 알게 된 딸의 1인칭 공감 스토리를 웹툰 일러스트로 보여주고, 큰 병을 비갱신형으로 보장받을 수 있는 올바른 100세 건강보험을 소개해 가족 보험료 확인으로 유도']
        for r,v in zip(list(rows)[1:],vals):
            c=r.cells[1]; ps=c.text_frame.paragraphs
            ps[0].runs[0].text=v
            for rr in ps[0].runs[1:]: rr.text=''
            for extra in ps[1:]: extra._p.getparent().remove(extra._p)

SC=[
 dict(img='k_1.5.png',
  txt=['우리 엄마 간병비,','이제 나라가 내준다길래','안심했는데...','[출처] 보건복지부, 보도자료 「요양병원 의료혁신 및 간병서비스 제도화 위한 대국민 토론회 개최」(2026.07.28)','[상단 로고] meritz 메리츠화재 (전 장면 노출)'],
  nar=['우리 엄마 간병비,','이제 나라가 내준다길래 안심했는데'],
  mot=['소파에 앉아 TV를 보며 안도하는 딸 캐릭터','상단 자막 순차 등장, 자막 하단 출처 표기']),
 dict(img='k_4.8.png',
  txt=['알고 보니... 지원은 일부래!','게다가 진단비부터 목돈이잖아','[인포 카드] 일부 요양병원, 중증 환자부터','진단 내 부담 / 치료 내 부담 / 입원 내 부담 / 간병 일부 지원','[말풍선] 그럼 미리 챙겨둬야겠네..?'],
  nar=['알고 보니 지원은 일부래.','게다가 진단비부터 목돈이잖아.'],
  mot=['머리를 감싸 쥔 딸 캐릭터 위로 먹구름·번개','진단·치료·입원·간병 카드 순차 등장 후 말풍선 등장']),
 dict(img='k_8.9.png',
  txt=['그래서 엄마 보험부터 찾아봤더니','요즘 병원비 생각하면','더 챙겨야겠더라고','[말풍선] 엄마, 이거 언제 든 거야?','[말풍선] 20년 전에 든 거야~ 괜찮아!'],
  nar=['그래서 엄마 보험부터 찾아봤더니','요즘 병원비 생각하면 더 챙겨야겠더라고'],
  mot=['보험 서류를 안고 걱정하는 딸, 손 흔드는 엄마','두 사람의 말풍선 대화 순차 등장']),
 dict(img='k_13.9.png',
  txt=['요즘 건강보험은','암, 뇌졸중, 심장질환처럼 큰 병은','비갱신으로 보장받을 수 있대','[아이콘] 암 세포 / 뇌 / 심장'],
  nar=['요즘 건강보험은 암, 뇌졸중, 심장질환 같은 큰 병은','비갱신으로 보장받을 수 있대'],
  mot=['노트북을 함께 보며 이야기하는 딸과 엄마','암·뇌·심장 아이콘 순차 등장']),
 dict(img='k_18.2.png',
  txt=['그럼 얼마일까?','엄마랑 내 보험료,','한 번에 계산해 봤어','[보험 분석 화면] 김메리님의 보험 3건을 분석했어요 / 여성, 만 32세','월 납입액 148,806원 / 보험 계약 3건 / 실효, 해지 6건'],
  nar=['그럼 얼마일까?','엄마랑 내 보험료 한 번에 계산해 봤어'],
  mot=['보험 분석 화면 카드가 아래에서 위로 등장','기대하는 표정의 딸과 엄마']),
 dict(img='k_20.8.png',
  txt=['메리츠화재','올바른 100세건강보험','[CTA 버튼] 가족 보험료 계산하기 >'],
  nar=['나랑 부모님 보험료','한 번에 확인해봐'],
  mot=['어깨동무하며 손 흔드는 딸과 엄마','상품명과 CTA 버튼 등장']),
]
MID=6096000
L=dict(txt=(1905490,1780089),narL=3769663,nar=(4050000,800000),motL=4992213,mot=(5271488,1001400))
for si,slide in enumerate([p.slides[6],p.slides[7],p.slides[8]]):
    for side in (0,1):
        sc=SC[si*2+side]; n=si*2+side+1
        inside=lambda sh: (sh.left<MID-200000)==(side==0)
        for sh in slide.shapes:
            if not inside(sh): continue
            nm=sh.name
            if sh.shape_type==13: set_pic(slide,sh,V+sc['img']); continue
            if not sh.has_text_frame: continue
            t=sh.text_frame.text
            if t.startswith('S#'): set_text(sh,['S#%d'%n])
            elif '993' in nm: set_text(sh,sc['txt']); sh.top,sh.height=L['txt']
            elif '997' in nm: set_text(sh,sc['nar']); sh.top,sh.height=L['nar']
            elif '995' in nm: set_text(sh,sc['mot']); sh.top,sh.height=L['mot']
            elif t=='[영상 내 나레이션]': sh.top=L['narL']
            elif t=='[영상 내 모션 설명]': sh.top=L['motL']
# end slide (12) -> S#7
s=p.slides[11]
END=['[보호금융상품 마크] 예금보험공사 보호금융상품 1인당 최고 1억원','메리츠화재 / 올바른 100세건강보험',
'해당 상품은 비갱신형 상품으로 80세, 90세, 100세 만기 중에서 선택할 수 있습니다.',
'이 보험계약은 예금자보호법에 따라 해약환급금(또는 만기 시 보험금)에 기타지급금을 합한 금액이 1인당 "1억원까지" (본 보험회사의 여타 보호상품과 합산) 보호됩니다. 이와 별도로 본 보험회사 보호상품의 사고보험금을 합산한 금액이 1인당 "1억원까지" 보호됩니다. 다만, 보험계약자 및 보험료납부자가 법인인 보험계약의 경우에는 보호되지 않습니다.',
'기존 보험계약을 해지하고 새로운 계약 체결 시 보험인수가 거절되거나 보험료가 인상되는 등 보장내용이 달라질 수 있습니다.',
'지급한도, 면책사항 등에 따라 보험금 지급이 제한될 수 있습니다.',
'보험계약 전, 자세한 상품내용과 제한사항은 약관 및 상품설명서를 참고하시기 바랍니다.',
'메리츠화재는 해당 상품에 대해 충분히 설명할 의무가 있으며, 가입자는 가입하기 전 이에 대한 충분한 설명을 들으시기 바랍니다.',
'본 게시물의 광고 유효기간은 심의필 발급 시점으로부터 1년입니다.',
'손해보험협회 심의필 000000호(2026.00.00~2027.00.00)']
for sh in s.shapes:
    if sh.shape_type==13: set_pic(s,sh,V+'endcard.png'); continue
    if not sh.has_text_frame: continue
    t=sh.text_frame.text
    if t.startswith('S#'): set_text(sh,['S#7'])
    elif t.startswith('[보호금융상품'): set_text(sh,END)
# delete slides 10, 11 (index 9,10)
lst=p.slides._sldIdLst; ids=list(lst)
for i in (10,9):
    rid=ids[i].get(qn('r:id')); p.part.drop_rel(rid); lst.remove(ids[i])
# leftovers check
for i,sl in enumerate(p.slides):
    for sh in sl.shapes:
        if sh.has_text_frame:
            for k in ['간편','재검','시바','1분','맞춤']:
                if k in sh.text_frame.text: print('LEFT',i+1,sh.name,k,sh.text_frame.text[:60].replace('\n','|'))
p.save(OUT)
