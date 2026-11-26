import re,os,subprocess,shutil
RB='/tmp/claude-0/-home-user-kanta-drama-analyzer/841a2249-e19b-55c1-8188-ca8037a85c33/scratchpad/tools/rb/'
R=RB+'replay/'
shutil.rmtree(R,ignore_errors=True); os.makedirs(R+'unkv/site')
shutil.copy(RB+'w_v1.html',R+'unkv/site/index.html')
def heredocs(sh):
    return re.findall(r"<<'EOF'\n(.*?)\nEOF",open(RB+sh).read(),re.S)
def runpy(code,cwd):
    r=subprocess.run(['python3','-c',code],cwd=cwd,capture_output=True,text=True)
    print('  rc',r.returncode,r.stdout.strip()[:200],r.stderr.strip()[-300:])
    assert r.returncode==0
print('p1');runpy(heredocs('p1_1022_1047.sh')[0],R+'unkv/site')
print('p2');runpy(heredocs('p2_1022_1048.sh')[0],R)
shutil.copytree(R+'unkv',R+'unkv3')
shutil.copy(R+'unkv/site/index.html',RB+'index_v2_unkv.html')
print('p3');runpy(heredocs('p3_1027_0342.sh')[0],R+'unkv3/site')
D=R+'unkv3/site/'
print('p4 sed');subprocess.run(['sed','-i','s/html,body{width:1080px;height:1920px;overflow:hidden;/html{background:#5B2B70}html,body{width:1080px;height:1920px;overflow:hidden;/','index.html'],cwd=D,check=True)
print('  bg count',open(D+'index.html').read().count('html{background:#5B2B70}'))
shutil.copy(D+'index.html',RB+'index_v3v4.html')
print('p5');runpy(heredocs('p5_1027_0711a.sh')[0],D)
print('p6 seds')
subprocess.run(['sed','-i',"s/const b=seg(t,1.0,1.3);\\$('bdg')/const b=seg(t,0.7,1.0);\\$('bdg')/; s/F('o_bell',0.9,SC\\[1\\]/F('o_bell',0.6,SC[1]/; s/F('o_ph',1.3,SC\\[1\\]/F('o_ph',0.9,SC[1]/",'index.html'],cwd=D,check=True)
subprocess.run(['sed','-i',"s/const p=t<1.0?Math.abs(Math.sin((t\\*7)-i\\*0.9)):0;/const p=t<0.6?Math.abs(Math.sin((t*7)-i*0.9)):0;/",'index.html'],cwd=D,check=True)
s=open(D+'index.html').read()
print('  checks',s.count('seg(t,0.7,1.0)'),s.count("F('o_bell',0.6,SC[1]"),s.count("F('o_ph',0.9,SC[1]"),s.count('const p=t<0.6?Math.abs'))
shutil.copy(D+'index.html',RB+'index_v5.html')
code=heredocs('p7_1027_0718.sh')[0]
code=code.split('import subprocess')[0]
print('p7');runpy(code,D)
shutil.copy(D+'index.html',RB+'index_v6.html')
