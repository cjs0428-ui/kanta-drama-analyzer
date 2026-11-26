cd /tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad && python3 - <<'EOF'
p='unkv/site/index.html';s=open(p).read()
r=[('values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.35"','values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.1 1.55"'),
("#scan{position:absolute;left:-400px;top:-260px;width:800px;height:520px;","#scan{position:absolute;zoom:1.25;left:-330px;top:-210px;width:660px;height:420px;"),
("#res{position:absolute;left:-400px;top:-280px;width:800px;height:560px;","#res{position:absolute;zoom:1.25;left:-330px;top:-230px;width:660px;height:460px;")]
for a,b in r:
    assert s.count(a)==1,a; s=s.replace(a,b)
open(p,'w').write(s)
EOF
W=1080 H=1920 TS=7.8,11.8,13.4 node render.cjs unkv/site stills unkv/st2 && python3 -c "
from PIL import Image
s=Image.new('RGB',(405*3,720))
for i,x in enumerate(['7.8','11.8','13.4']): s.paste(Image.open(f'unkv/st2/t{x}.png').convert('RGB').resize((405,720)),(i*405,0))
s.save('unkv/sheet2.jpg')"