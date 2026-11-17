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
BMC='https://buymeacoffee.com/dagreensayz'
ROLE={'keumart':'ARTISTE'}
cards=''
for id,n,r in ART:
    img=f'<img class="sp" src="{sp[id]}">'
    nm=n.split(' ',1)
    first=nm[0]; last=nm[1] if len(nm)>1 else '&nbsp;'
    cards+=f'<div class="card"><div class="stage">{img}</div><div class="fn">{first}</div><div class="ln">{last}</div><div class="qrw"><img class="qr" src="{qf(id)}"></div><div class="hd">{H[id]}</div></div>'
html=f"""<!doctype html><meta charset=utf8><style>
@font-face{{font-family:'Press Start 2P';src:url('ps2p.woff2') format('woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--gold:#f2c14e;--gold2:#c9892f;--red:#8a1426;--ink:#140c18;--cream:#f6e9c8}}
body{{width:594mm;height:841mm;position:relative;overflow:hidden;font-family:'Press Start 2P',monospace;color:var(--cream);
background:
 radial-gradient(ellipse at 50% 18%,rgba(255,200,110,.28),transparent 55%),
 repeating-linear-gradient(90deg,rgba(0,0,0,.22) 0 14mm,rgba(255,255,255,.03) 14mm 22mm,transparent 22mm 38mm),
 linear-gradient(180deg,#6d0f20 0,#4a0a18 40%,#2a0612 75%,#160a14 100%)}}
.frame{{position:absolute;inset:9mm;border:2.2mm solid var(--gold);box-shadow:inset 0 0 0 2mm var(--ink),inset 0 0 0 3.2mm var(--gold2)}}
.corner{{position:absolute;width:12mm;height:12mm;background:var(--gold);box-shadow:0 0 0 1.5mm var(--ink)}}
.corner.a{{left:3mm;top:3mm}}.corner.b{{right:3mm;top:3mm}}.corner.c{{left:3mm;bottom:3mm}}.corner.d{{right:3mm;bottom:3mm}}
.bulbs{{position:absolute;left:30mm;right:30mm;height:5mm;background:radial-gradient(circle,#ffe9a8 0 1.6mm,transparent 2mm) 0 0/9mm 5mm repeat-x}}
.bulbs.t{{top:17mm}}
.head{{position:absolute;top:30mm;left:0;right:0;text-align:center}}
.eyebrow{{font-size:6.2mm;letter-spacing:1.5mm;color:var(--gold)}}
.t1{{font-size:30mm;line-height:1.08;color:var(--gold);text-shadow:0 2.2mm 0 #5a0c1a,0 3.6mm 0 var(--ink);margin-top:7mm}}
.t2{{font-size:7.4mm;letter-spacing:.8mm;margin-top:12mm;color:var(--cream)}}
.t2 b{{color:var(--gold);font-weight:normal}}
.play{{position:absolute;top:150mm;left:34mm;right:34mm;height:128mm;background:linear-gradient(180deg,#f7d27a,#e0a63a);border:2mm solid var(--ink);box-shadow:0 3mm 0 #5a0c1a,0 0 0 5mm var(--gold2);display:flex;align-items:center;gap:10mm;padding:0 10mm;color:var(--ink)}}
.play .me{{height:92mm;width:92mm;image-rendering:pixelated;flex:none;filter:drop-shadow(0 2mm 0 rgba(90,12,26,.5))}}
.play .q{{width:100mm;height:100mm;background:#fff;border:2mm solid var(--ink);flex:none;image-rendering:pixelated}}
.play .tx{{flex:1}}
.play .h{{font-size:15mm;line-height:1.25}}
.play .l{{font-size:5.8mm;line-height:1.9;margin-top:6mm;color:#5a0c1a}}
.play .coin{{display:inline-block;margin-top:7mm;background:var(--ink);color:var(--gold);font-size:5.4mm;padding:2.6mm 5mm}}
.sect{{position:absolute;top:298mm;left:0;right:0;text-align:center;font-size:8mm;color:var(--gold);letter-spacing:1mm}}
.sect:before,.sect:after{{content:'';display:inline-block;width:60mm;height:1.2mm;background:var(--gold2);vertical-align:middle;margin:0 8mm}}
.grid{{position:absolute;top:316mm;left:30mm;right:30mm;display:grid;grid-template-columns:repeat(3,1fr);gap:7mm}}
.card{{background:linear-gradient(180deg,#26163a,#170d26);border:1.2mm solid var(--gold);box-shadow:0 0 0 1mm var(--ink);padding:3mm 3mm 4mm;text-align:center;display:flex;flex-direction:column;align-items:center}}
.stage{{width:100%;height:56mm;background:radial-gradient(ellipse at 50% 100%,rgba(255,210,120,.55),transparent 65%),linear-gradient(180deg,#0e0818,#1d1130);display:flex;align-items:flex-end;justify-content:center;border-bottom:1mm solid var(--gold2)}}
.sp{{height:54mm;width:54mm;image-rendering:pixelated}}
.fn{{font-size:6mm;margin-top:4mm;color:var(--cream)}}
.ln{{font-size:4.4mm;margin-top:1.6mm;color:var(--gold);min-height:5mm}}
.qrw{{background:#fff;padding:1.6mm;margin-top:3.5mm}}
.qr{{display:block;width:52mm;height:52mm;image-rendering:pixelated}}
.hd{{font-size:3.3mm;margin-top:3mm;color:#b3a7d6;max-width:100%;overflow:hidden}}
.foot{{position:absolute;bottom:22mm;left:34mm;right:34mm;display:flex;align-items:center;justify-content:center;gap:10mm}}
.foot .qrw{{margin:0}}.foot .qr{{width:30mm;height:30mm}}
.foot .tx{{font-size:4.4mm;line-height:1.9;color:var(--cream)}}
.foot .tx b{{color:var(--gold);font-weight:normal}}
</style><body>
<div class=frame><div class="corner a"></div><div class="corner b"></div><div class="corner c"></div><div class="corner d"></div></div>
<div class="bulbs t"></div>
<div class=head><div class=eyebrow>MAGIC MIRROR - TERRITET - MONTREUX</div><div class=t1>LA REVUE<br>VAUDOISE</div><div class=t2><b>8E EDITION</b> - LE SPECTACLE</div></div>
<div class=play><img class=q src="{qr(GAME)}"><div class=tx><div class=h>JOUE AU<br>JEU !</div><div class=l>SCANNE, CHOISIS<br>TON ARTISTE ET<br>LANCE-TOI DANS<br>LES MINI-JEUX<br>ET LE QUIZ</div><div class=coin>INSERT COIN</div></div><img class=me src="{sp['keumart']}"></div>
<div class=sect>LES ARTISTES</div>
<div class=grid>{cards}</div>
<div class=foot><div class=qrw><img class=qr src="{qr(BMC)}"></div><div class=tx>CE JEU EST GRATUIT, CRÉÉ PAR <b>KEUMART</b>.<br>UN CAFÉ POUR LE SOUTENIR ?<br>SCANNE OU CLIQUE DANS LE JEU</div></div>
</body>"""
open('affiche.html','w').write(html)
open('conf.json','w').write(json.dumps({'pw':PW,'ph':PH}))
