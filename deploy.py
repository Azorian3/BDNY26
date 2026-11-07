import os,json,hashlib,urllib.request,sys
TOK=open('/home/ubuntu/.netlify_tok').read().strip();H={'Authorization':'Bearer '+TOK,'Content-Type':'application/json'}
API='https://api.netlify.com/api/v1'
def req(method,path,data=None,raw=None,ctype=None):
    body=raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    h=dict(H)
    if ctype:h['Content-Type']=ctype
    r=urllib.request.Request(API+path,data=body,method=method,headers=h)
    try:
        with urllib.request.urlopen(r) as resp:return json.loads(resp.read() or b'null')
    except urllib.error.HTTPError as e:print(method,path,e.code,e.read()[:300]);raise
NAME=sys.argv[1] if len(sys.argv)>1 else 'azorian3-bdny'
sites=req('GET','/sites?per_page=200');site=next((s for s in sites if s['name']==NAME),None)
if not site:
    site=req('POST','/sites',{'name':NAME});print('created',site['ssl_url'])
else:print('existing',site['ssl_url'])
D=sys.argv[2] if len(sys.argv)>2 else '/home/ubuntu/bdny/dist';files={}
for fn in os.listdir(D):
    p=os.path.join(D,fn);files['/'+fn]=hashlib.sha1(open(p,'rb').read()).hexdigest()
dep=req('POST',f"/sites/{site['id']}/deploys",{'files':files})
for sha in dep.get('required',[]):
    fn=next(k for k,v in files.items() if v==sha)
    req('PUT',f"/deploys/{dep['id']}/files{fn}",raw=open(D+fn,'rb').read(),ctype='application/octet-stream');print('uploaded',fn)
import time
for _ in range(30):
    d=req('GET',f"/deploys/{dep['id']}")
    if d['state']=='ready':break
    time.sleep(2)
print('state',d['state'],site['ssl_url'])
