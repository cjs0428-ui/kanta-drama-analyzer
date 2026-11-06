const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const [t,out]=process.argv.slice(2);await p.goto('file://'+process.cwd()+'/sub.html?t='+encodeURIComponent(t));await p.waitForTimeout(800);
await p.screenshot({path:out,omitBackground:true});await b.close()})()
