import json,io,base64,sys,subprocess,os
import qrcode
from qrcode.constants import ERROR_CORRECT_M
COLS,ROWS=(int(sys.argv[1]),int(sys.argv[2])) if len(sys.argv)>2 else (3,2)
GAME='https://dagreensayaman-lab.github.io/revue-vaudoise-game/#public'
sp=json.load(open('sprites.json')); so=json.load(open('socials.json'))
H={'jenny':'@jennylorant','keumart':'@keumartdagreensayaman','lea':'@gambalae','pierre':'@pierreaucaigne','david':'@davidcharles_mcroger','olivier':'@olivier_delaloye','karim':'@monsieurkarimslama','catherine':'@catguggi','veronique':'@larevuevaudoise'}
F={'jenny':'jenny-lorent','keumart':'keumart','lea':'lea-gamba','pierre':'pierre-aucaigne','david':'david-charles','olivier':'olivier-delaloye','karim':'karim-slama','catherine':'catherine-guggisberg','veronique':'veronique-mattana'}
from PIL import Image
def qf(id):
    im=Image.open('qr/'+F[id]+'.png').convert('RGB').resize((600,600),Image.NEAREST);b=io.BytesIO();im.save(b,'PNG');return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
ART=[('jenny','JENNY LORENT','ARTISTE'),('keumart','KEUMART','ARTISTE'),('lea','LÉA GAMBA','ARTISTE'),('pierre','PIERRE AUCAIGNE','ARTISTE'),('david','DAVID CHARLES','ARTISTE'),('olivier','OLIVIER DELALOYE','ARTISTE'),('karim','KARIM SLAMA','ARTISTE'),('catherine','CATHERINE GUGGISBERG','ARTISTE'),('veronique','VÉRONIQUE MATTANA','ARTISTE')]
def qr(url):
    q=qrcode.QRCode(error_correction=ERROR_CORRECT_M,border=1,box_size=10);q.add_data(url);q.make(fit=True)
    im=q.make_image(fill_color='#140c18',back_color='white');b=io.BytesIO();im.save(b,'PNG')
    return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()


PW,PH=594,841.0
ICON='data:image/png;base64,'+base64.b64encode(open('../icons/icon-barbezat-180.png','rb').read()).decode()
def artist(id,n):
    nm=n.split(' ',1); first=nm[0]; last=nm[1] if len(nm)>1 else ''
    return f'<div class="card"><div class="stage"><img class="sp" src="{sp[id]}"></div><div class="info"><div class="fn">{first}</div><div class="ln">{last or "&nbsp;"}</div><div class="qrw"><img class="qr" src="{qf(id)}"></div><div class="hd">{H[id]}</div></div></div>'
A={i:(i,n) for i,n,r in ART}
LOGO='data:image/png;base64,'+base64.b64encode(open('logo-revue.png','rb').read()).decode()
order=['jenny','keumart','lea','pierre','david','olivier','karim','catherine','veronique']
cards=''.join(artist(*A[i]) for i in order[:8])
cards+=artist(*A['veronique']).replace('<div class="card">','<div class="card" style="grid-column-start:2">',1)
cards+=f'<div class="card"><div class="stage txt"><img class="logo" src="{LOGO}"></div><div class="info"><div class="fn">INSTAGRAM</div><div class="ln">LE SPECTACLE</div><div class="qrw"><img class="qr" src="{qf("veronique")}"></div><div class="hd">@larevuevaudoise</div></div></div>'
back=['pierre','olivier','karim','catherine']; front=['jenny','lea','keumart','david','veronique']
SZ=112
lineup=''
import math
def fy(x,base,amp): return base+amp*math.sqrt(max(0,1-((x-297)/220)**2))
for k,i in enumerate(back):
    x=202+63.5*k; lineup+=f'<img class="ls" style="left:{x-SZ/2}mm;top:{fy(x,304,22)-0.9*SZ}mm" src="{sp[i]}">'
for k,i in enumerate(front):
    x=170+63.5*k; lineup+=f'<img class="ls" style="left:{x-SZ/2}mm;top:{fy(x,336,40)-0.9*SZ}mm" src="{sp[i]}">'
html=f"""<!doctype html><meta charset=utf8><style>
@font-face{{font-family:'Press Start 2P';src:url('ps2p.woff2') format('woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--gold:#f2c14e;--cream:#f6e9c8;--ink:#0e0814}}
body{{width:594mm;height:841mm;position:relative;overflow:hidden;font-family:'Press Start 2P',monospace;color:var(--cream);background:#2a0612}}
.bg{{position:absolute;left:0;top:-72mm;width:594mm;height:1056mm;image-rendering:pixelated}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,6,20,.5) 0,rgba(8,6,20,.1) 22%,rgba(8,6,20,0) 40%,rgba(8,6,20,.35) 62%,rgba(8,6,20,.75) 100%)}}
.frame{{position:absolute;inset:8mm;border:1.4mm solid var(--gold);box-shadow:inset 0 0 0 1.6mm rgba(14,8,20,.8)}}
.head{{position:absolute;top:44mm;left:0;right:0;text-align:center}}
.eyebrow{{font-size:5.6mm;letter-spacing:1.4mm;color:var(--gold);text-shadow:0 .6mm 0 var(--ink)}}
.t1{{font-size:30mm;line-height:1.08;color:var(--gold);text-shadow:0 2.2mm 0 #5a0c1a,0 3.6mm 0 var(--ink);margin-top:7mm}}
.t2{{font-size:7mm;letter-spacing:.8mm;margin-top:11mm;text-shadow:0 .6mm 0 var(--ink)}}
.msg{{position:absolute;top:426mm;left:0;right:0;text-align:center;font-size:4.8mm;line-height:1.6;color:var(--gold);letter-spacing:.5mm;text-shadow:0 .7mm 0 var(--ink),0 0 3mm var(--ink)}}
.grid{{position:absolute;top:441mm;left:0;right:0;display:grid;grid-template-columns:repeat(4,148.5mm);grid-auto-rows:90mm;row-gap:6mm}}
.card{{margin:0 11mm 0 11mm;display:flex;align-items:center;gap:2mm;background:rgba(14,8,20,.58);border:.5mm solid rgba(242,193,78,.4);padding:3mm 4mm 3mm 2mm;height:90mm}}
.stage{{width:58mm;height:100%;flex:none;display:flex;align-items:flex-end;justify-content:center;background:radial-gradient(ellipse at 50% 100%,rgba(255,210,120,.4),transparent 70%);overflow:visible}}
.sp{{width:88mm;height:88mm;max-width:none;image-rendering:pixelated;margin-bottom:-4mm}}
.info{{flex:1;min-width:0;display:flex;flex-direction:column;align-items:flex-start}}
.fn{{font-size:5mm;color:var(--cream)}}
.ln{{font-size:3.1mm;margin-top:1.4mm;color:var(--gold);min-height:4mm}}
.qrw{{background:#fff;padding:1.4mm;margin-top:3mm}}
.qr{{display:block;width:50mm;height:50mm;image-rendering:pixelated}}
.hd{{font-size:2.6mm;margin-top:2.6mm;color:#c9bfe6;white-space:nowrap}}
.logo{{width:57mm;height:auto;display:block}}
.txt{{align-items:center}}.big{{font-size:6.6mm;line-height:1.5;color:var(--gold);text-align:center;text-shadow:0 .5mm 0 var(--ink)}}
.ic{{width:46mm;height:46mm;image-rendering:pixelated;align-self:center}}
.note{{justify-content:center;border-style:dashed}}.nt{{font-size:7.4mm;line-height:1.7;color:var(--gold);text-align:center}}
.ls{{position:absolute;width:112mm;height:112mm;image-rendering:pixelated;filter:drop-shadow(0 1.5mm 1mm rgba(0,0,0,.55))}}
.bonus{{position:absolute;left:456mm;top:24mm;width:118mm;text-align:center;background:rgba(14,8,20,.62);border:.5mm solid rgba(242,193,78,.55);padding:5mm 3mm 4mm}}
.bonus .b1{{font-size:4.6mm;color:var(--gold);line-height:1.5}}
.bonus .q{{display:block;width:64mm;height:64mm;background:#fff;padding:1.6mm;margin:3.5mm auto 3mm;image-rendering:pixelated}}
.bonus .b2{{font-size:3.2mm;line-height:1.6}}
.bonus .b3{{font-size:2.3mm;color:#9a90c0;margin-top:2.6mm}}
.credit{{position:absolute;top:782mm;left:0;right:0;text-align:center;font-size:4.2mm;color:#c9bfe6;letter-spacing:.8mm;line-height:2}}
</style><body>
<img class=bg src="fond-interieur.png"><div class=shade></div><div class=frame></div>
<div class=head><div class=eyebrow>MAGIC MIRROR - TERRITET</div><div class=t1>LA REVUE<br>VAUDOISE</div><div class=t2>8E EDITION</div></div>
<div class=msg>SUIVEZ LES ARTISTES EN SCANNANT LEUR QR CODE</div>
{lineup}
<div class=bonus><div class=b1>BONUS<br>A SCANNER</div><img class=q src="{qr(GAME)}"><div class=b2>LE JEU DE LA REVUE</div><div class=b3>JEU CRÉÉ PAR KEUMART</div></div>
<div class=grid>{cards}</div>
<div class=credit>MAGIC MIRROR - TERRITET - 2026</div>
</body>"""
open('affiche.html','w').write(html)
open('conf.json','w').write(json.dumps({'pw':PW,'ph':PH}))
