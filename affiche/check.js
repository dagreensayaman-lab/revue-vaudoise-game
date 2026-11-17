const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2245,height:3179}});
await p.goto('file://'+process.cwd()+'/affiche.html');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const k=594/document.body.getBoundingClientRect().width;const f=594/ 594; // px->css mm in 594 units
const u=594/document.body.getBoundingClientRect().width*(840/594);
return [...document.querySelectorAll('.qr,.card')].map(e=>{const q=e.getBoundingClientRect();return {c:e.className,x0:q.left*u,x1:q.right*u,y0:q.top*u,y1:q.bottom*u}})});
const X=[210,420,630],Y=[297,594,891]; // A0 mm: tile 210x297
let bad=0;r.forEach(q=>{X.forEach(x=>{if(q.x0<x&&q.x1>x){bad++;console.log('X cut',q.c,q.x0,q.x1)}});Y.forEach(y=>{if(q.y0<y&&q.y1>y){bad++;console.log('Y cut',q.c,Math.round(q.y0),Math.round(q.y1),y)}})});
console.log('elements',r.length,'cuts',bad);await b.close()})();
