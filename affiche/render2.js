const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const c=JSON.parse(fs.readFileSync('conf.json'));const k=Number(process.argv[2]||200)/96;const mm=x=>x/25.4*96;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:Math.round(mm(c.pw)),height:Math.round(mm(c.ph))},deviceScaleFactor:k});
await p.goto('file://'+process.cwd()+'/affiche.html');await p.waitForTimeout(2500);await p.screenshot({path:'full.png'});await b.close()})();
