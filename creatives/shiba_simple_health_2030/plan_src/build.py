from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
C=[
('0~3.3초','c_61.jpg','오프닝 · 식탁 위 약 봉투·물컵 클로즈업\n강조 문구: "서른다섯, 혈압 재검 소견"','저 서른다섯인데, 검진에서 혈압 재검 소견이 나왔거든요.'),
('3.3~6.8초','c_151.jpg','검색 화면 · "혈압 재검 소견 보험" 타이핑\n연관검색어(가입 못 하나요/거절/포기/고지해야 하나요/조건)\n관련 게시물 3개 → 우는 이모지로 전환','이렇게 소견 나온 사람은 보험 가입 안 될 것 같아서, 아예 포기했었죠.'),
('6.8~10.1초','c_256.jpg','고민하는 시바견(직장인)\n강조 문구: "증상 없으니 괜찮겠지?"','시간 지나면 수치도 괜찮아질 테니까, 말 안 하고 가입할까 싶었고요.'),
('10.1~12.3초','c_331.jpg','노트북 POV → 오해 카드 2장\n"소견 있으면 무조건 가입 불가?" / "증상 없으면 검진 소견 말 안 해도?"\n→ 카드 뒤집힘 "✕ 오해예요" + "둘 다 오해!"','알아보니, 둘 다 틀린 생각이었어요.'),
('12.3~15.3초','c_421.jpg','밝은 자연광 배경\n"소견이 있어도" ▼ "간편심사로 가입 검토"','소견이 있어도, 간편심사를 통해 가입을 검토할 수 있고요.'),
('15.3~18.3초','c_511.jpg','일반심사 vs 간편심사 비교 카드\n일반: 건강 상태를 자세히 심사 / 간편: 정해진 질문에 답해 심사','다만 상품과 심사 유형마다 조건이 다르고,'),
('18.3~22.2초','c_646.jpg','간편심사 질문 예시\n3개월 내 재검사 소견 / 2년 내 입원·수술 / 5년 내 암 등 진단 (예·아니요)','투약이나 진단, 입원·수술 이력처럼, 질문별로 확인할 내용도 다르더라고요!'),
('22.2~25.6초','c_721.jpg','폰·노트 메모 POV\n강조 문구: "나한테 맞는 심사 방식부터!"','역시 중요한 건, 나한테 맞는 심사 방식을 확인하는 거더라고요!'),
('25.6~29.9초','c_841.jpg','메리 CTA\n"헷갈릴 땐 보장분석부터" + [1분 보장분석으로 조건 확인 ›]','헷갈릴 땐, 1분 보장분석으로 가입 조건부터 확인해 보세요.'),
('29.9~33.1초','c_960.jpg','엔드카드 · 메리츠화재 간편건강보험\n예금자보호·해약·유의사항 고지 + 심의필','(BGM)'),
]
p=Presentation();p.slide_width=Inches(13.333);p.slide_height=Inches(7.5)
RED=RGBColor(0xE0,0x24,0x2F);DK=RGBColor(0x22,0x22,0x22);GR=RGBColor(0x66,0x66,0x66)
def tb(s,x,y,w,h,text,size,bold=False,color=DK,align=PP_ALIGN.LEFT,fill=None):
    b=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=b.text_frame;tf.word_wrap=True
    if fill is not None: b.fill.solid();b.fill.fore_color.rgb=fill
    for k,line in enumerate(text.split('\n')):
        par=tf.paragraphs[0] if k==0 else tf.add_paragraph();par.alignment=align
        r=par.add_run();r.text=line;r.font.size=Pt(size);r.font.bold=bold;r.font.color.rgb=color;r.font.name='Noto Sans KR'
    return b
for page in range(2):
    s=p.slides.add_slide(p.slide_layouts[6])
    tb(s,0.4,0.25,12.5,0.5,"메리츠 간편보험 2030 · 시바견 릴스 '검진 소견' 버전 기획안 (9:16 · 33초)",20,True)
    tb(s,0.4,0.72,12.5,0.35,f"설정: 서른다섯, 건강검진에서 혈압 재검 소견 → 오해 2가지(소견 있으면 가입 불가 / 소견 말 안 해도 됨) 해소 → 1분 보장분석 CTA   ({page+1}/2)",11,False,GR)
    for j in range(5):
        n=page*5+j;t,img,scr,na=C[n];x=0.4+j*2.52
        tb(s,x,1.15,2.35,0.32,f"#{n+1}  {t}",12,True,RGBColor(255,255,255),PP_ALIGN.CENTER,RED)
        s.shapes.add_picture(img,Inches(x+0.42),Inches(1.55),Inches(1.5),Inches(2.67))
        tb(s,x,4.3,2.35,0.25,'주요 화면',10,True,RED)
        tb(s,x,4.52,2.35,1.4,scr,9,False,DK)
        tb(s,x,5.95,2.35,0.25,'나레이션',10,True,RED)
        tb(s,x,6.17,2.35,1.1,na,9.5,True,DK)
p.save('/home/user/kanta-drama-analyzer/creatives/shiba_simple_health_2030/기획안_검진소견_v6.pptx')
