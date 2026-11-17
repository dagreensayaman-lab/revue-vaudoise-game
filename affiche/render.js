const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const c=JSON.parse(fs.readFileSync('conf.json'));const dpi=200,k=dpi/96;
const mmpx=mm=>mm/25.4*96;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:Math.round(mmpx(c.pw)),height:Math.round(mmpx(c.ph))},deviceScaleFactor:k});
await p.goto('file://'+process.cwd()+'/affiche.html');await p.waitForTimeout(2500);
await p.screenshot({path:'affiche_complete.png'});await b.close()})();
