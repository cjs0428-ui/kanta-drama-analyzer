const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080},deviceScaleFactor:1});
for(const k of ['A','B','C']){await p.goto('file://'+process.cwd()+'/app_'+k+'.html');await p.waitForTimeout(700);await (await p.$('#a')).screenshot({path:'app_'+k+'.png'})}await b.close()})()
