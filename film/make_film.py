import base64,os
A='/home/ubuntu/bdny/src/assets';b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
F=lambda f:b64(os.path.join(A,f))
HTML=r'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{font-family:'Syne';font-weight:400 800;src:url(data:font/woff2;base64,%(SYNE)s) format('woff2')}
@font-face{font-family:'DM Sans';font-weight:100 1000;src:url(data:font/woff2;base64,%(DM)s) format('woff2')}
@font-face{font-family:'Instrument Serif';font-style:italic;src:url(data:font/woff2;base64,%(SER)s) format('woff2')}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:#0B0D10;color:#E8ECF1;font-family:'DM Sans',sans-serif}
#stage{position:relative;width:1920px;height:1080px}
.sc{position:absolute;inset:0;opacity:0}
canvas{position:absolute;inset:0}
.syne{font-family:Syne;font-weight:700;letter-spacing:-.035em;line-height:.95}
.serif{font-family:'Instrument Serif';font-style:italic;font-weight:400;color:#5FE3FF}
.eyebrow{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-family:Syne;font-size:22px;letter-spacing:.42em;color:#5FE3FF;font-weight:600;white-space:nowrap}
.bl{position:absolute;left:120px;bottom:140px}
.bl div{font-size:150px}
.bl div{opacity:0;transform:translateY(40px)}
.lines{position:absolute;left:120px;top:200px}
.ln{opacity:0;transform:translateX(-30px);margin-bottom:54px}
.ln .t{font-size:60px;color:#E8ECF1;font-weight:400;letter-spacing:-.01em}
.ln .raw{margin-top:14px;font-family:'DM Mono',ui-monospace,Menlo,monospace;font-size:26px;color:#8A94A3;letter-spacing:.02em}
.ln .raw b{color:#FF5C5C;font-weight:500}
.center{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center}
.center .syne{font-size:210px}
.big2{position:absolute;left:120px;top:50%;transform:translateY(-50%);font-size:118px}
.sig{position:absolute;left:120px;bottom:120px;font-family:Syne;font-size:20px;letter-spacing:.3em;color:#C7F23C;opacity:0}
.kb{position:absolute;inset:0;overflow:hidden}
.kb img{position:absolute;left:0;top:0;width:1920px;transform-origin:50% 30%}
.kb .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,13,16,.96) 0%,rgba(11,13,16,.85) 42%,rgba(11,13,16,.25) 100%)}
.co{position:absolute;left:120px;opacity:0}
.co b{display:block;font-family:Syne;font-weight:700;font-size:170px;letter-spacing:-.04em;line-height:.9}
.co span{display:block;font-size:34px;color:#C7CFDA;margin-top:14px;letter-spacing:-.005em}
.words{position:absolute;inset:0;display:flex;justify-content:space-between;align-items:center;padding:0 110px}
.words div{font-size:92px;opacity:0;transform:scale(.9);white-space:nowrap}
.words div:nth-child(4){color:#C7F23C}
.end{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:48px}
.end img{width:720px;height:auto;display:block;margin:0 auto 54px;opacity:0}
.end .o{font-size:66px;opacity:0}
.end .o em{font-family:'Instrument Serif';font-style:italic;font-weight:400;color:#C7F23C}
.end .m{font-family:Syne;font-size:20px;letter-spacing:.3em;color:#8A94A3;opacity:0;margin-top:10px}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50%% 50%%,transparent 55%%,rgba(0,0,0,.55) 100%%);pointer-events:none}
#fade{position:absolute;inset:0;background:#000;opacity:0}
</style></head><body><div id="stage">
<canvas id="c" width="1920" height="1080"></canvas>
<div class="sc" id="s1"><div class="eyebrow">FOR THE PEOPLE WHO MAKE WHAT THE HOTELS BUY</div></div>
<div class="sc" id="s2"><div class="bl"><div class="syne">Monday.</div><div class="syne">Four files.</div><div class="syne">Zero <span class="serif">answers.</span></div></div></div>
<div class="sc" id="s3"><div class="lines">
 <div class="ln"><div class="t">The names do not match.</div><div class="raw">STUDIO MARLOWE &nbsp; <b>Marlowe Studio</b> &nbsp; Studio Marlowe LLC &nbsp; <b>S. Marlowe</b></div></div>
 <div class="ln"><div class="t">The dates are typed three ways.</div><div class="raw">3/14/26 &nbsp; <b>14-Mar-2026</b> &nbsp; March 14 &nbsp; <b>ship wk 12</b> &nbsp; TBD</div></div>
 <div class="ln"><div class="t">Half the promised ship dates are blank.</div><div class="raw">(blank) &nbsp; <b>(blank)</b> &nbsp; see email &nbsp; <b>ask Dana</b> &nbsp; (blank)</div></div>
</div></div>
<div class="sc" id="s4"><div class="center"><div class="syne">You make<br>the piece.</div></div></div>
<div class="sc" id="s5"><div class="big2 syne">We make the<br><span class="serif">numbers</span> behave.</div><div class="sig">95%% CONFIDENCE · SIGNED J. MARTINKO, COO · SECURITY J. BOYNTON, CIO</div></div>
<div class="sc" id="s6"><div class="kb"><img id="grid" src="data:image/png;base64,%(GRID)s"><div class="shade"></div></div>
 <div class="co" style="top:150px"><b>$609K</b><span>of deposit money held on orders already late</span></div>
 <div class="co" style="top:430px"><b>14</b><span>orders past promised ship, average 23 days</span></div>
 <div class="co" style="top:700px"><b>3 of 8</b><span>containers landed 12%% or more over quote</span></div>
</div>
<div class="sc" id="s7"><div class="words"><div class="syne">Clean.</div><div class="syne">Standardize.</div><div class="syne">Complete.</div><div class="syne">Sign.</div></div></div>
<div class="sc" id="s8"><div class="end"><img src="data:image/png;base64,%(LOGO)s"><div class="o syne">Fixed fee. Fixed date. <em>You</em> own the result.</div><div class="m">BDNY · JAVITS · NOVEMBER 8 AND 9 · AZORIAN3.COM</div></div></div>
<div class="vig"></div><div id="fade"></div>
</div>
<script>
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const cl=(x,a,b)=>Math.max(a,Math.min(b,x));const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;const eo=x=>1-Math.pow(1-x,3);
const win=(t,a,b,fi=.5,fo=.5)=>t<a||t>b?0:Math.min(1,(t-a)/fi,(b-t)/fo);
const prog=(t,a,d)=>cl((t-a)/d,0,1);
function fadeIn(el,t,a,d=.5,dy=40){const p=eo(prog(t,a,d));el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px)`}
/* canvas scatter -> ledger */
const POOL=[
 [['STUDIO MARLOWE','Studio Marlowe'],['Marlowe Studio','Studio Marlowe'],['Greyfield Hosp.','Greyfield Hospitality'],['GREYFIELD','Greyfield Hospitality'],['Northlight Int','Northlight Interiors'],['northlight interiors','Northlight Interiors'],['Sutton Rowe','Sutton Rowe Design'],['SRD','Sutton Rowe Design'],['Avery Lane','Avery Lane Studio'],['Castellan','Castellan Design'],['Meridian ffe','Meridian FF&E'],['Loom DH','Loom Design House'],['Brightwater Purch','Brightwater Purchasing'],['Halcyon','Halcyon Interiors']],
 [['3/14/26','2026-03-14'],['14-Mar-2026','2026-03-14'],['March 14','2026-03-14'],['TBD','2026-04-02'],['ship wk 12','2026-03-20'],['ASAP','2026-03-20'],['2/2/26','2026-02-02'],['02.02.2026','2026-02-02'],['(blank)','2026-05-06'],['late','2026-01-30'],['Q2?','2026-04-15'],['end of month','2026-03-31'],['next wk','2026-03-27'],['see email','2026-02-19']],
 [['$ 38,000','38,000'],['38000.00','38,000'],['$38k','38,000'],['see attached','18,920'],['dep 50%%','18,500'],['deposit rec’d','18,500'],['22,700','22,700'],['$2.27k','2,270'],['landed +17%%','61,900'],['brokerage tbd','61,900'],['n/a','0'],['-','0'],['(blank)','12,400*'],['12.4k','12,400']],
 [['sent?','Open · 118d'],['status: ??','Open · 118d'],['PO-1192 dup','PO-1192'],['PO 1192','PO-1192'],['Q-0417 (v2)','Q-0417'],['Q0417','Q-0417'],['ask Dana','Open · 74d'],['memo out','Memo · 61d'],['sample?','Memo · 61d'],['overdue!!','Late · 23d'],['in prod.','In production'],['hold','Not due yet'],['container ?','HLXU 118 5577'],['TGHU 902 7716','TGHU 902 7716']]];
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const ITEMS=[];const COLX=[1030,1350,1555,1705];const ROWY0=330,ROWH=38;
for(let c=0;c<4;c++)for(let r=0;r<14;r++){const [raw,clean]=POOL[c][r];ITEMS.push({raw,clean,c,r,sx:140+rnd()*1640,sy:60+rnd()*960,dx:(rnd()-.5)*40,dy:(rnd()-.5)*40,ph:rnd()*6.28,bad:/\?|blank|dup|tbd|late|overdue|ask|see|n\/a|^-$/i.test(raw)});}
const ctx=$('#c').getContext('2d');
function drawCanvas(t,alpha,resolve,drift){
 ctx.clearRect(0,0,1920,1080);if(alpha<=0)return;ctx.globalAlpha=alpha;ctx.textBaseline='middle';
 const p=ease(resolve);
 ITEMS.forEach(it=>{const sx=it.sx+Math.sin(t*.4+it.ph)*18*drift,sy=it.sy+Math.cos(t*.3+it.ph)*14*drift;const tx=COLX[it.c],ty=ROWY0+it.r*ROWH;const x=sx+(tx-sx)*p,y=sy+(ty-sy)*p;
  ctx.font=(p>.6?'500 ':'400 ')+'24px "DM Sans"';ctx.textAlign=it.c===2&&p>.6?'right':'left';const xx=it.c===2&&p>.6?x+120:x;
  const col=p<.5?(it.bad?'#FF5C5C':'#8A94A3'):(it.c===0?'#E8ECF1':'#8FB4E8');ctx.fillStyle=col;const txt=p<.5?it.raw:it.clean;ctx.globalAlpha=alpha*(p<.5?.75+.25*(1-p*2):1);ctx.fillText(txt,xx,y)});
 if(p>.7){const q=cl((p-.7)/.3,0,1);ctx.globalAlpha=alpha*q;ctx.strokeStyle='#2E3745';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(1020,ROWY0-24);ctx.lineTo(1020+860*q,ROWY0-24);ctx.stroke();ctx.beginPath();ctx.moveTo(1020,ROWY0+14*ROWH-14);ctx.lineTo(1020+860*q,ROWY0+14*ROWH-14);ctx.stroke();
  ctx.font='600 14px Syne';ctx.fillStyle='#5FE3FF';ctx.textAlign='left';['FIRM','PROMISED SHIP','DEPOSIT','STATUS'].forEach((h,i)=>{ctx.fillText(h.split('').join(String.fromCharCode(8202)),COLX[i],ROWY0-44)})}
 ctx.globalAlpha=1}
const S=$$('.sc');
window.seek=function(t){
 S.forEach(s=>s.style.opacity=0);
 // s1
 $('#s1').style.opacity=win(t,0,3.6,1.2,.5);
 // canvas presence: scenes 2,3 scatter; scene 5 resolve
 let ca=0,res=0,drift=1;
 if(t>=3.2&&t<15.2){ca=win(t,3.2,15.2,1.5,.6)*(t<9.2?.9:.45)}
 if(t>=19.6&&t<27.4){ca=win(t,19.6,27.4,.8,.7);res=prog(t,21,3.4);drift=1-res}
 drawCanvas(t,ca,res,drift);
 // s2
 $('#s2').style.opacity=win(t,3.6,9.2,.3,.5);$$('#s2 .bl div').forEach((d,i)=>fadeIn(d,t,3.9+i*1.5,.6));
 // s3
 $('#s3').style.opacity=win(t,9.2,15.2,.3,.6);$$('#s3 .ln').forEach((d,i)=>{const p=eo(prog(t,9.4+i*1.8,.6));d.style.opacity=p;d.style.transform=`translateX(${(1-p)*-30}px)`});
 // s4
 $('#s4').style.opacity=win(t,15.2,20,.5,.6);$('#s4 .syne').style.transform=`scale(${1+prog(t,15.2,4.8)*.05})`;
 // s5
 $('#s5').style.opacity=win(t,20,27.4,.5,.6);const b2=$('#s5 .big2');const p5=eo(prog(t,20.2,.8));b2.style.opacity=p5;b2.style.transform=`translateY(calc(-50%% + ${(1-p5)*50}px))`;$('#s5 .sig').style.opacity=prog(t,24.8,.6);
 // s6
 $('#s6').style.opacity=win(t,27.4,35.2,.5,.6);const k=prog(t,27.4,7.8);$('#grid').style.transform=`translate(${-60*k}px,${-80*k}px) scale(${1.02+.1*k})`;$$('#s6 .co').forEach((d,i)=>{const p=eo(prog(t,28+i*2,.55));d.style.opacity=p;d.style.transform=`translateX(${(1-p)*-40}px)`});
 // s7
 $('#s7').style.opacity=win(t,35.2,40.2,.3,.5);$$('#s7 .words div').forEach((d,i)=>{const p=eo(prog(t,35.4+i*1.05,.45));d.style.opacity=p;d.style.transform=`scale(${.9+.1*p})`});
 // s8
 $('#s8').style.opacity=win(t,40.2,46,.5,.1);const e=$('#s8');const img=e.querySelector('img');img.style.opacity=prog(t,40.6,.9);fadeIn(e.querySelector('.o'),t,41.4,.7,24);e.querySelector('.m').style.opacity=prog(t,42.4,.7);
 $('#fade').style.opacity=prog(t,44.2,.8);
};
seek(0);
</script></body></html>'''
d=dict(SYNE=F('syne_normal.woff2'),DM=F('dmsans_normal.woff2'),SER=F('iserif_italic.woff2'),LOGO=F('lockup.png'),GRID=b64('/home/ubuntu/bdny/film/cap/grid.png'))
out=HTML.replace('%%','%')
for k,v in d.items(): out=out.replace('%('+k+')s',v)
open('/home/ubuntu/bdny/film/film.html','w').write(out);print('film.html ok')
