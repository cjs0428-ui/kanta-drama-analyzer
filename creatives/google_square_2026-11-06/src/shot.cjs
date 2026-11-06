const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080},deviceScaleFactor:1});
for(const k of ['g1a','g1b','g2a','g2b']){await p.goto('file://'+process.cwd()+'/'+k+'.html');await p.waitForTimeout(700);await (await p.$('#a')).screenshot({path:k+'_ad.png'})}await b.close()})()
