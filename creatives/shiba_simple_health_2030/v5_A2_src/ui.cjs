const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const k of ['S0','S1','S2','S3','S4','S5']){await p.goto('file://'+process.cwd()+'/ui_'+k+'.html');await p.waitForTimeout(600);await p.screenshot({path:'ui_'+k+'.png',omitBackground:true})}await b.close()})()
