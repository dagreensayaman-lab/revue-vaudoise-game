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
cards=''
for id,n,r in ART:
    nm=n.split(' ',1); first=nm[0]; last=nm[1] if len(nm)>1 else ''
    cards+=f'<div class="card"><div class="stage"><img class="sp" src="{sp[id]}"></div><div class="info"><div class="fn">{first}</div><div class="ln">{last or "&nbsp;"}</div><div class="qrw"><img class="qr" src="{qf(id)}"></div><div class="hd">{H[id]}</div></div></div>'
html=f"""<!doctype html><meta charset=utf8><style>
@font-face{{font-family:'Press Start 2P';src:url('ps2p.woff2') format('woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--gold:#f2c14e;--cream:#f6e9c8;--ink:#0e0814}}
body{{width:594mm;height:841mm;position:relative;overflow:hidden;font-family:'Press Start 2P',monospace;color:var(--cream);background:#0c0a22}}
.bg{{position:absolute;left:0;top:-134mm;width:594mm;height:1056mm;image-rendering:pixelated}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,6,20,.55) 0,rgba(8,6,20,0) 24%,rgba(8,6,20,0) 52%,rgba(8,6,20,.72) 66%,rgba(8,6,20,.9) 100%)}}
.frame{{position:absolute;inset:8mm;border:1.4mm solid var(--gold);box-shadow:inset 0 0 0 1.6mm rgba(14,8,20,.8)}}
.head{{position:absolute;top:26mm;left:0;right:0;text-align:center}}
.eyebrow{{font-size:5.6mm;letter-spacing:1.4mm;color:var(--gold)}}
.t1{{font-size:30mm;line-height:1.08;color:var(--gold);text-shadow:0 2.2mm 0 #5a0c1a,0 3.6mm 0 var(--ink);margin-top:7mm}}
.t2{{font-size:7mm;letter-spacing:.8mm;margin-top:11mm}}
.badge{{position:absolute;left:34mm;top:402mm;width:112mm;text-align:center;background:rgba(14,8,20,.7);border:.8mm solid rgba(242,193,78,.7);padding:8mm 3mm;height:auto}}
.badge .b1{{font-size:7.4mm;color:var(--gold);line-height:1.5}}
.badge .b2{{font-size:4.6mm;margin-top:5mm;line-height:1.8}}
.play{{position:absolute;right:34mm;top:402mm;width:112mm;text-align:center;background:rgba(14,8,20,.7);border:.8mm solid rgba(242,193,78,.7);padding:5mm 3mm}}
.play .h{{font-size:5.4mm;color:var(--gold);line-height:1.5}}
.play .q{{width:62mm;height:62mm;background:#fff;padding:1.6mm;margin:4mm auto 3mm;display:block;image-rendering:pixelated}}
.play .l{{font-size:3.2mm;line-height:1.7}}
.sect{{position:absolute;top:512mm;left:0;right:0;text-align:center;font-size:7.5mm;color:var(--gold);letter-spacing:1.2mm}}
.grid{{position:absolute;top:520mm;left:30mm;right:30mm;display:grid;grid-template-columns:repeat(3,1fr);gap:6mm}}
.card{{display:flex;align-items:center;gap:2mm;background:rgba(14,8,20,.5);border:.5mm solid rgba(242,193,78,.4);padding:3mm 4mm 3mm 2mm;height:93mm}}
.stage{{width:68mm;height:100%;display:flex;align-items:flex-end;justify-content:center;background:radial-gradient(ellipse at 50% 100%,rgba(255,210,120,.4),transparent 70%)}}
.sp{{width:92mm;height:92mm;max-width:none;image-rendering:pixelated;margin-bottom:-4mm}}
.info{{flex:1;min-width:0;display:flex;flex-direction:column;align-items:flex-start}}
.fn{{font-size:5.2mm;color:var(--cream)}}
.ln{{font-size:3.2mm;margin-top:1.4mm;color:var(--gold);min-height:4mm}}
.qrw{{background:#fff;padding:1.4mm;margin-top:3mm}}
.qr{{display:block;width:44mm;height:44mm;image-rendering:pixelated}}
.hd{{font-size:2.6mm;margin-top:2.6mm;color:#c9bfe6;white-space:nowrap}}
.credit{{position:absolute;bottom:12.5mm;left:0;right:0;text-align:center;font-size:3.2mm;color:#9a90c0;letter-spacing:.6mm}}
</style><body>
<img class=bg src="fond-chapiteau.png"><div class=shade></div><div class=frame></div>
<div class=head><div class=eyebrow>MAGIC MIRROR - TERRITET - MONTREUX</div><div class=t1>LA REVUE<br>VAUDOISE</div><div class=t2>8E EDITION</div></div>
<div class=badge><div class=b1>SUIVEZ<br>LES ARTISTES</div><div class=b2>EN SCANNANT<br>LEUR QR CODE</div></div>
<div class=play><div class=h>ENVIE DE JOUER ?</div><img class=q src="{qr(GAME)}"><div class=l>SCANNE ET AMUSE-TOI<br>AVEC LE JEU DE LA REVUE</div></div>
<div class=grid>{cards}</div>
<div class=credit>JEU CRÉÉ PAR KEUMART</div>
</body>"""
open('affiche.html','w').write(html)
open('conf.json','w').write(json.dumps({'pw':PW,'ph':PH}))
