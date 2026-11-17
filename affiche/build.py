import json,io,base64,sys,subprocess,os
import qrcode
from qrcode.constants import ERROR_CORRECT_M
COLS,ROWS=(int(sys.argv[1]),int(sys.argv[2])) if len(sys.argv)>2 else (3,2)
GAME='https://dagreensayaman-lab.github.io/revue-vaudoise-game/#public'
sp=json.load(open('sprites.json')); so=json.load(open('socials.json'))
ART=[('jenny','JENNY LORENT','ARTISTE'),('keumart','KEUMART','ARTISTE'),('lea','LÉA GAMBA','ARTISTE'),('pierre','PIERRE AUCAIGNE','ARTISTE'),('david','DAVID CHARLES','ARTISTE'),('olivier','OLIVIER DELALOYE','ARTISTE'),('karim','KARIM SLAMA','ARTISTE'),('catherine','CATHERINE GUGGISBERG','ARTISTE'),('veronique','VÉRONIQUE MATTANA','ARTISTE')]
def qr(url):
    q=qrcode.QRCode(error_correction=ERROR_CORRECT_M,border=1,box_size=10);q.add_data(url);q.make(fit=True)
    im=q.make_image(fill_color='#140c18',back_color='white');b=io.BytesIO();im.save(b,'PNG')
    return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
PW,PH=210*COLS,297*ROWS  # mm
cards=''
for id,n,r in ART:
    u=(so.get(id) or '').strip()
    q=f'<img class="qr" src="{qr(u)}">' if u else '<div class="qr empty">LIEN<br>À AJOUTER</div>'
    img=f'<img class="sp" src="{sp[id]}">' if id in sp else '<div class="sp"></div>'
    cards+=f'<div class="card">{img}<div class="nm">{n}</div><div class="ro">{r}</div>{q}<div class="sc">SCANNE ET SUIS-MOI</div></div>'
html=f'''<!doctype html><meta charset=utf8><style>
@font-face{{font-family:'Press Start 2P';src:url('ps2p.woff2') format('woff2')}}
*{{box-sizing:border-box;margin:0}}
body{{width:{PW}mm;height:{PH}mm;background:radial-gradient(circle at 50% 0%,#7a1424 0,#3a0a18 55%,#140c18 100%);font-family:'Press Start 2P',monospace;color:#f6e9c8;position:relative;overflow:hidden}}
.head{{display:flex;align-items:center;justify-content:center;gap:{PW*0.05}mm;padding-top:{PH*0.022}mm}}
.top{{text-align:left}}
.t1{{font-size:{PW*0.065}mm;color:#f2c14e;text-shadow:0 .8mm 0 #6a1020;line-height:1.25}}
.t2{{font-size:{PW*0.02}mm;line-height:1.7;margin-top:{PH*0.02}mm;letter-spacing:.3mm;color:#f6e9c8}}
.game{{margin:0;width:{PW*0.27}mm;background:#f2c14e;border:{PW*0.006}mm solid #140c18;padding:{PW*0.02}mm;text-align:center;box-shadow:0 {PW*0.006}mm 0 #6a1020}}
.game .g1{{font-size:{PW*0.02}mm;color:#140c18}}
.game img{{width:{PW*0.19}mm;display:block;margin:{PW*0.012}mm auto;border:{PW*0.004}mm solid #140c18}}
.game .g2{{font-size:{PW*0.0115}mm;color:#6a1020;line-height:1.6}}
.sub{{text-align:center;font-size:{PW*0.02}mm;color:#f2c14e;margin:{PH*0.022}mm 0 {PH*0.01}mm}}
.grid{{display:flex;flex-wrap:wrap;justify-content:center;gap:{PW*0.012}mm;padding:0 {PW*0.03}mm}}
.card{{width:{PW*0.175}mm;background:#1f1230;border:{PW*0.003}mm solid #f2c14e;padding:{PW*0.008}mm;text-align:center;display:flex;flex-direction:column;align-items:center}}
.sp{{width:{PW*0.07}mm;height:{PW*0.07}mm;image-rendering:pixelated}}
.nm{{font-size:{PW*0.0095}mm;margin-top:{PW*0.005}mm;line-height:1.4;min-height:{PW*0.026}mm}}
.ro{{font-size:{PW*0.0085}mm;color:#f2c14e;margin:{PW*0.003}mm 0 {PW*0.006}mm}}
.qr{{width:{PW*0.07}mm;height:{PW*0.07}mm;background:#fff;image-rendering:pixelated}}
.qr.empty{{display:flex;align-items:center;justify-content:center;font-size:{PW*0.01}mm;color:#9a8fb8;border:{PW*0.002}mm dashed #9a8fb8;background:transparent}}
.sc{{font-size:{PW*0.0075}mm;color:#9a8fb8;margin-top:{PW*0.004}mm}}
.foot{{position:absolute;bottom:{PH*0.015}mm;left:0;right:0;text-align:center;font-size:{PW*0.011}mm;color:#9a8fb8;line-height:1.8}}
</style><body>
<div class=head><div class=top><div class=t1>LA REVUE<br>VAUDOISE</div><div class=t2>8E EDITION<br>MAGIC MIRROR<br>TERRITET-MONTREUX</div></div>
<div class=game><div class=g1>JOUE AU JEU !</div><img src="{qr(GAME)}"><div class=g2>SCANNE ET CHOISIS<br>TON ARTISTE</div></div></div>
<div class=sub>LES ARTISTES - SUIS-LES !</div>
<div class=grid>{cards}</div>
<div class=foot>JEU CRÉÉ PAR KEUMART - TU PEUX LE SOUTENIR DANS LE JEU</div>
</body>'''
open('affiche.html','w').write(html)
open('conf.json','w').write(json.dumps({'cols':COLS,'rows':ROWS,'pw':PW,'ph':PH}))
