const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2245,height:3179}});
await p.goto('file://'+process.cwd()+'/affiche.html');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const bb=document.body.getBoundingClientRect();const ux=891/bb.width,uy=1260/bb.height;
return [...document.querySelectorAll('.qr,.card')].map(e=>{const q=e.getBoundingClientRect();return {c:e.className,x0:q.left*ux,x1:q.right*ux,y0:q.top*uy,y1:q.bottom*uy}})});
const X=[297,594],Y=[420,840];let bad=0;
r.forEach(q=>{X.forEach(x=>{if(q.x0<x&&q.x1>x){bad++;console.log('X cut',q.c,Math.round(q.x0),Math.round(q.x1),x)}});Y.forEach(y=>{if(q.y0<y&&q.y1>y){bad++;console.log('Y cut',q.c,Math.round(q.y0),Math.round(q.y1),y)}})});
console.log('elements',r.length,'cuts',bad);await b.close()})();
