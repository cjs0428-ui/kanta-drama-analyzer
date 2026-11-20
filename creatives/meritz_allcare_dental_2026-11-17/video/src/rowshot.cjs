const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:400}});
const [L,R,out,f,ls,fw,rs]=process.argv.slice(2);
fs.writeFileSync('row.html',`<html><head><meta charset="utf-8"><style>@font-face{font-family:P;src:url(fontp/Pretendard-${fw}.otf)}@font-face{font-family:Q;src:url(fontp/Pretendard-Medium.otf)}*{margin:0;padding:0}body{background:transparent}
#r{position:relative;width:1080px;height:142px}#c{position:absolute;left:70px;top:0;width:939px;height:142px;background:rgb(249,249,249)}#c i{position:absolute;left:0;top:0;bottom:0;width:16px;background:rgb(234,35,44)}
#l{position:absolute;left:62px;top:4px;height:142px;display:flex;align-items:center;font-family:P;font-size:${f}px;letter-spacing:${ls}px;color:#111}
#s{position:absolute;right:45px;top:4px;height:142px;display:flex;align-items:center;font-family:Q;font-size:${rs}px;color:rgb(105,105,105)}</style></head><body><div id="r"><div id="c"><i></i><div id="l">${L}</div><div id="s">${R}</div></div></div></body></html>`);
await p.goto('file://'+process.cwd()+'/row.html');await p.waitForTimeout(500);await (await p.$('#r')).screenshot({path:out,omitBackground:true});await b.close()})()
