import json,re
d=json.load(open('assets/radar_data.json'));ex=json.load(open('assets/bdny_exhibitors.json'))
L={l['n']:l for l in d['leads']}
def lead(n):
    l=L[n];return {k:l.get(k) for k in ('n','s','a','h','w','d','st','note','fix','open','score','grade')}
radar=[
 dict(lead('Stone Source'),booth='2437',ex='Stone Source',match='exact'),
 dict(lead('Artistic Tile'),booth='2619',ex='Artistic Tile',match='exact'),
 dict(lead('Nemo Tile + Stone'),booth='3037',ex='Nemo Tile Co.',match='same company, trade name differs'),
 dict(lead('Matter'),booth='2679',ex='Matter Surfaces Inc',match='same word, almost certainly a different company. Verify before you pitch.'),
]
out={'bdny':d['bdny'],'radar':radar,'ex':[[e['n'],e['b']] for e in ex],'segs':d['segments'] if isinstance(d['segments'],dict) else {}}
json.dump(out,open('walk_data.json','w'),separators=(',',':'))
print(len(out['ex']),len(out['bdny']['new']),[r['n']+' '+r['booth'] for r in radar])
print(json.dumps(radar[0],indent=0)[:600])
