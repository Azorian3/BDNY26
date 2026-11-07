import base64,os,asyncio,io,qrcode,pikepdf
from playwright.async_api import async_playwright
S=os.path.dirname(os.path.abspath(__file__));A=os.path.join(S,'assets');OUT='/home/ubuntu/bdny/print'
b64=lambda f:base64.b64encode(open(os.path.join(A,f),'rb').read()).decode()
URL='https://azorian3-bdny.netlify.app'
def qr(dark,light):
    q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,border=2,box_size=12);q.add_data(URL);q.make()
    im=q.make_image(fill_color='#000000',back_color='#FFFFFF').convert('RGB');b=io.BytesIO();im.save(b,'PNG');return base64.b64encode(b.getvalue()).decode()
THEMES={
 'dark':dict(bg='#0B0D10',p1='#11151B',line='#232A33',line2='#2E3745',tx='#E8ECF1',tx2='#C7CFDA',mu='#8A94A3',dim='#5C6673',cy='#5FE3FF',li='#C7F23C',rd='#FF5C5C',am='#E8C76A',onbtn='#0B0D10',logo=b64('lockup.png'),qrd='#0B0D10',qrl='#F4F4F2'),
 'light':dict(bg='#F5F3EE',p1='#FFFFFF',line='#E3DFD6',line2='#CDC7BB',tx='#15181C',tx2='#2B3139',mu='#5B626D',dim='#8A9099',cy='#0E7FA3',li='#4F7F00',rd='#C9352F',am='#B07D0A',onbtn='#FFFFFF',logo=b64('lockup_ink.png'),qrd='#15181C',qrl='#FFFFFF')}
HTML=r'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{font-family:'Syne';font-weight:400 800;src:url(data:font/woff2;base64,%(SYNE)s) format('woff2')}
@font-face{font-family:'DM Sans';font-weight:100 1000;src:url(data:font/woff2;base64,%(DM)s) format('woff2')}
@font-face{font-family:'Instrument Serif';font-style:italic;src:url(data:font/woff2;base64,%(SER)s) format('woff2')}
@font-face{font-family:'Instrument Serif';font-style:normal;src:url(data:font/woff2;base64,%(SERN)s) format('woff2')}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:8.5in;height:11in;background:%(bg)s;color:%(tx)s;font-family:'DM Sans',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:8.5in;height:11in;padding:.22in .55in .26in;display:flex;flex-direction:column}
.hd{display:flex;justify-content:space-between;align-items:center;padding-bottom:.06in;border-bottom:1px solid %(line)s}
.hd img{height:1.02in;margin-left:-.08in}
.tag{font-family:Syne;font-size:8.5pt;letter-spacing:.16em;text-transform:uppercase;color:%(mu)s;border:1px solid %(line2)s;padding:4pt 8pt}
.eyebrow{font-family:Syne;font-size:7.5pt;letter-spacing:.22em;text-transform:uppercase;color:%(cy)s;font-weight:600;margin-top:.1in}
h1{font-family:'Instrument Serif';font-weight:400;font-size:34pt;line-height:.96;letter-spacing:-.01em;margin:.05in 0 .1in;max-width:7.3in}
.sw{display:grid;grid-template-columns:repeat(6,1fr);gap:.08in;margin-top:.06in}
.sw div{font-family:Syne;font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;color:%(mu)s}
.sw i{display:block;height:5pt;margin-bottom:3pt}
.sw .l{color:%(dim)s;letter-spacing:.06em;text-transform:none;font-family:'DM Sans';font-size:6.6pt;display:inline;margin-left:4pt}
h1 em{font-style:italic;color:%(cy)s}
.lede{font-size:9.6pt;line-height:1.36;color:%(tx2)s;max-width:6.6in}
.cols{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;background:%(line)s;border:1px solid %(line)s;margin-top:.08in}
.col{background:%(p1)s;padding:.12in .15in .12in}
.col .k{font-family:Syne;font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:%(dim)s;margin-bottom:6pt}
.col h3{font-family:Syne;font-size:12.5pt;font-weight:600;letter-spacing:-.01em;margin-bottom:6pt;line-height:1.15}
.col p,.col li{font-size:8.2pt;line-height:1.3;color:%(tx2)s}
.col ul{list-style:none}
.col li{padding:2.6pt 0;border-bottom:1px dotted %(line2)s;display:block}
.col li:last-child{border-bottom:0}
.col li b{font-family:Syne;font-weight:600;color:%(cy)s;font-size:7.5pt;display:block;letter-spacing:.14em;margin-bottom:1pt}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:%(line)s;border:1px solid %(line)s;border-top:0}
.steps div{background:%(p1)s;padding:.08in .15in .09in}
.steps b{font-family:Syne;font-size:9.5pt;display:block;margin-bottom:2pt}
.steps span{font-size:8pt;color:%(mu)s;line-height:1.32;display:block}
.steps i{font-family:Syne;font-style:normal;font-size:7.5pt;letter-spacing:.2em;color:%(cy)s;display:block;margin-bottom:4pt}
.band{display:grid;grid-template-columns:1.3fr 1fr;gap:.14in;margin-top:.08in}
.offer{border:1px solid %(li)s;padding:.1in .15in;display:flex;flex-direction:column}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:%(line)s;border:1px solid %(line)s;border-top:0}
.tiers div{background:%(p1)s;padding:.05in .15in .06in}
.tiers i{font-family:Syne;font-style:normal;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:%(li)s;display:block;margin-bottom:4pt}
.tiers b{font-family:Syne;font-size:9.5pt;display:block;margin-bottom:2pt}
.tiers span{font-size:7.6pt;line-height:1.3;color:%(mu)s;display:block}
.offer .k{font-family:Syne;font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:%(li)s;margin-bottom:5pt}
.offer h2{font-family:'Instrument Serif';font-size:21pt;font-weight:400;letter-spacing:-.01em;line-height:1;margin-bottom:6pt}
.offer h2 em{font-family:'Instrument Serif';font-style:italic;font-weight:400;color:%(li)s}
.offer p{font-size:8.6pt;line-height:1.36;color:%(tx2)s}
.offer .who{margin-top:8pt;padding-top:7pt;border-top:1px solid %(line)s;font-size:8.3pt;color:%(mu)s;line-height:1.4}
.offer .who b{color:%(tx)s;font-family:Syne;font-weight:600}
.qr{background:%(p1)s;border:1px solid %(line2)s;padding:.1in;display:grid;grid-template-columns:1.35in 1fr;gap:.15in;align-items:center}
.qr img{width:1.45in;height:1.45in;display:block;background:#fff}
.qr b{font-family:Syne;font-size:12pt;display:block;letter-spacing:-.01em;line-height:1.15}
.qr span{font-size:8.2pt;color:%(mu)s;line-height:1.4;display:block;margin-top:5pt}
.qr .u{font-family:Syne;color:%(cy)s;font-size:7.6pt;margin-top:6pt;display:block;letter-spacing:0;white-space:nowrap}
.team{display:grid;grid-template-columns:repeat(4,1fr);gap:.03in .12in;margin-top:auto;padding-top:.03in;border-top:1px solid %(line)s}
.team i{font-family:Syne;font-style:normal;font-size:6.5pt;letter-spacing:.18em;text-transform:uppercase;color:%(cy)s;display:block}
.team b{font-family:Syne;font-size:8.2pt;display:block}
.team span{font-size:6.9pt;color:%(mu)s;line-height:1.26;display:block}
.ft{display:flex;justify-content:space-between;align-items:center;margin-top:.07in;font-size:8pt;color:%(dim)s}
.ft b{font-family:Syne;color:%(tx)s;font-size:9.5pt;font-weight:600}
</style></head><body><div class="page">
<div class="hd"><img src="data:image/png;base64,%(logo)s"><span class="tag">BDNY 2026 · Javits Center · November 8 and 9</span></div>
<div class="eyebrow">For the people who make what the hotels buy</div>
<h1>You bring the vision.<br>We bring the <em>insight.</em></h1>
<p class="lede">Know which quotes need attention and where costs are changing. Azorian3 brings your quote log, open orders, freight invoices and sample records into one dashboard, so your team can prioritize follow up, see delivery issues and compare quoted costs with actual costs. Start with the files your team already uses.</p>
<div class="sw"><div><i style="background:linear-gradient(90deg,#6F4F17,#E6B45A 55%%,#FFF0C4)"></i>Lighting<span class="l">brass and linen</span></div><div><i style="background:linear-gradient(90deg,#3E2314,#9A6239 50%%,#EADDC8)"></i>Furniture<span class="l">walnut and boucle</span></div><div><i style="background:linear-gradient(90deg,#1B2A6B,#4457B0 50%%,#C23B3B)"></i>Rugs and textiles<span class="l">indigo and madder</span></div><div><i style="background:linear-gradient(90deg,#2F6E62,#9FD3C4 50%%,#EADFCC)"></i>Tile and stone<span class="l">travertine and verdigris</span></div><div><i style="background:linear-gradient(90deg,#4F6040,#A9B98F 50%%,#F1E8DA)"></i>Wallcovering<span class="l">sage and plaster</span></div><div><i style="background:linear-gradient(90deg,#3E1014,#8A2A30 50%%,#D9B26A)"></i>Art and accessories<span class="l">oxblood and gilt</span></div></div>
<div class="cols">
 <div class="col"><div class="k">01 · What we do</div><h3>Clean. Standardize. Complete. Sign.</h3><p>Simple, accurate and as stylish as you want it to be. We meet you where your processes already are. Start with the files your team already uses. Missing values are estimated and labeled as estimates. A person reviews the numbers before you see them.</p></div>
 <div class="col"><div class="k">02 · Three outcomes</div><ul>
  <li><b>SALES</b>See aging quotes and which accounts are converting. Samples and memos out too long.</li>
  <li><b>ORDERS</b>Identify late orders and the dollars tied to them, including deposits held on late work.</li>
  <li><b>COSTS</b>Compare quoted and actual landed cost, per container, to inform the next project.</li>
 </ul></div>
 <div class="col"><div class="k">03 · Beyond Monday</div><ul>
  <li>90 day forecast of what will book, with an honest range<b>FROM YOUR OWN HISTORY</b></li>
  <li>Best, base and worst case on every filled blank<b>PLAN ON THE LOW END</b></li>
  <li>Weekly watch, every Monday, the five changes that matter<b>SIGNED EACH WEEK</b></li>
  <li>Buyers in your market who have never asked you for a quote<b>GRADED, WITH AN OPENER</b></li>
 </ul></div>
</div>
<div class="tiers"><div><i>Sprint · fixed fee</i><b>Ledger Sprint</b><span>Your four files to a signed ledger in 10 business days. Executive readout with the top ten money moves.</span></div><div><i>Monthly</i><b>Monday Subscription</b><span>Flat monthly fee, cancel any month. Weekly refresh, forecast, best and worst case, watch list, buyer radar. Unlimited users.</span></div><div><i>Build · fixed scope</i><b>Build and Hand Over</b><span>Wired into QuickBooks and your quote log, documented, trained, 8 weeks. You own the code and the data.</span></div></div>

<div class="band">
 <div class="offer"><div class="k">Pricing</div><h2>Fixed fee. Fixed date. <em>You</em> own the result.</h2><p>Three ways to engage, above, priced on the outcome and the calendar, not billable days. Sized to your order volume, your files and your data quality. Agreed before we start. Discovery is one hour with the owner, no charge.</p>
 <div class="who"><b>Who this fits.</b> Owner led. 5 to 50 people. No data team. Showrooms, makers, rug and textile houses, tile and stone, lighting studios, galleries.</div></div>
 <div class="qr"><img src="data:image/png;base64,%(QR)s"><div><b>Scan to explore a modeled furniture example.</b><span>Pick what you make. Watch four files become one dashboard. Tap any number for the fix. Figures are modeled, not customer results.</span><span class="u">azorian3-bdny.netlify.app</span></div></div>
</div>
<div class="team">
 <div><i>Chief Executive</i><b>James F. Canfield IV</b><span>CEO. Procurement and spend data.</span></div>
 <div><i>Operations</i><b>Jacob M. Martinko</b><span>COO. Reviews and signs every ledger.</span></div>
 <div><i>Infrastructure and cyber</i><b>Justin M. Boynton</b><span>CIO. Infrastructure and security.</span></div>
 <div><i>Statistics</i><b>Lawrence Marinucci</b><span>VP of Statistics. 30 years in clinical trials.</span></div>
 <div><i>Commercial</i><b>Thaddeus Kornegay</b><span>CCO. Furniture procurement and logistics.</span></div>
 <div><i>Legal</i><b>Ahmad Seraj</b><span>General Counsel. Seraj Law PLLC.</span></div>
 <div><i>Account management</i><b>Nicole Riley</b><span>Account Manager.</span></div>
 <div><i>Account management</i><b>Dahlia Riley</b><span>Account Manager.</span></div>
</div>
<div class="ft"><b>contact@azorian3.com · azorian3.com</b><span>Azorian 3, LLC · New York · All figures shown are modeled examples, not customer results.</span></div>
</div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,t in THEMES.items():
            d=dict(t);d.update(SYNE=b64('syne_normal.woff2'),DM=b64('dmsans_normal.woff2'),SER=b64('iserif_italic.woff2'),SERN=b64('iserif_normal.woff2'),QR=qr(t['qrd'],t['qrl']))
            html=HTML%d;hp=os.path.join(OUT,f'onepager_{name}.html');open(hp,'w').write(html)
            pg=await b.new_page(viewport={'width':816,'height':1056});await pg.goto('file://'+hp);await pg.wait_for_timeout(400)
            raw=os.path.join(OUT,f'raw_{name}.pdf');await pg.pdf(path=raw,width='8.5in',height='11in',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
            await pg.screenshot(path=os.path.join(OUT,f'onepager_{name}.png'),full_page=True);print(name,'content height px:',await pg.evaluate('document.querySelector(".page").scrollHeight'),await pg.evaluate('document.documentElement.scrollHeight'))
            pdf=pikepdf.open(raw)
            with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
                m['dc:title']='Azorian3 at BDNY 2026. You bring the vision. We bring the insight.';m['dc:creator']=['James F. Canfield IV'];m['pdf:Producer']='Azorian3';m['xmp:CreatorTool']='Azorian3'
            pdf.docinfo['/Author']='James F. Canfield IV';pdf.docinfo['/Creator']='Azorian3';pdf.docinfo['/Producer']='Azorian3';pdf.docinfo['/Title']='Azorian3 at BDNY 2026'
            pdf.save(os.path.join(OUT,f'Azorian3_BDNY_OnePager_{name}.pdf'));os.remove(raw);print(name,len(pdf.pages),'page(s)')
        await b.close()
asyncio.run(main())
