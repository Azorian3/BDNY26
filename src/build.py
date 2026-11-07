import base64,os,re,json
S=os.path.dirname(os.path.abspath(__file__));A=os.path.join(S,'assets');D=os.path.join(S,'..','dist')
b64=lambda p:base64.b64encode(open(os.path.join(A,p),'rb').read()).decode()
css=open(os.path.join(S,'style.css')).read().replace('{{SYNE}}',b64('syne_normal.woff2')).replace('{{DMSANS}}',b64('dmsans_normal.woff2')).replace('{{DMSANSI}}',b64('dmsans_italic.woff2')).replace('{{ISERIF}}',b64('iserif_normal.woff2')).replace('{{ISERIFI}}',b64('iserif_italic.woff2'))
def page(src,out,extra=None):
    h=open(os.path.join(S,src)).read()
    h=h.replace('{{CSS}}',css).replace('{{LOCKUP}}',b64('lockup.png')).replace('{{MARK}}',b64('mark.png')).replace('{{LOCKUPD}}',b64('lockup_ink.png')).replace('{{LOCKUPSVG}}',open(os.path.join(S,'assets','lockup_inline.svg')).read())
    for k,v in (extra or {}).items(): h=h.replace('{{'+k+'}}',v)
    open(os.path.join(D,out),'w').write(h);print(out,len(h)//1024,'KB')
os.makedirs(D,exist_ok=True)
page('index.html','index.html',{'JS':open(os.path.join(S,'app.js')).read()})
if os.path.exists(os.path.join(S,'walk.html')):
    page('walk.html','walk.html',{'JS':open(os.path.join(S,'walk.js')).read(),'DATA':open(os.path.join(S,'walk_data.json')).read()})
open(os.path.join(D,'_headers'),'w').write('/*\n  Content-Type: text/html; charset=UTF-8\n  X-Frame-Options: SAMEORIGIN\n')
