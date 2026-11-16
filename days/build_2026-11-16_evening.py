# Rebuilds evening sets of days/2026-11-16.json for a calm movie-background mode.
# M is watching Project Hail Mary on his iPhone; the villa TV is only ambient
# background until about 21:30. Keeps morning/afternoon (09:00-18:00) and the
# already-calm 22:00-02:00 sets from the 08:00 build.
import json, os
DATE='2026-11-16'; REV=67; NEXT='2026-11-17'
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-16.json')))

def lic(k):
    return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace(' rs','')
def artist(k):
    return C[k]['artist']
def cr(k):
    return 'Gerçek fotoğraf · Real photo · Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k), lic(k))

def soft(k, tr, en, d=240, dim=0.7, pos=None, capop=0.32):
    it=dict(k='hzphoto', quiet=1, d=d, f='m/h16-%s.jpg'%k, tr=tr, en=en, cr=cr(k), dim=dim, capop=capop)
    if pos: it['pos']=pos
    return it

# Long dwell, tiny bilingual caption, no facts / quotes / games.
# Dim values tuned to the source brightness of each still.
ITEMS=[
  soft('mb-aftersunset','Gün batımından sonra','After sunset', dim=0.55, d=240),
  soft('mb-agvadusk','Karadeniz alacakaranlığı','Black Sea dusk', dim=0.48, pos='50% 38%', d=240),
  soft('mb-paranal','Yıldızların altında','Under the stars', dim=0.72, d=260),
  soft('mb-pleiades','Ülker','The Pleiades', dim=0.62, d=240),
  soft('mb-witchhead','Soluk mavi bir bulutsu','A faint blue nebula', dim=0.68, pos='50% 45%', d=240),
  soft('mb-barnard68','Karanlık bir toz bulutu','A dark dust cloud', dim=0.74, d=240),
  soft('mb-ngc891','Kenardan görünen bir galaksi','A galaxy seen edge-on', dim=0.95, d=260),
  soft('mb-airglow','Dünya’nın kenarı','The edge of the Earth', dim=0.56, d=240),
]

def S(frm, until, sid, name, items):
    return dict(id=sid, name=name, **{'from':frm,'until':until}, items=items)

evening=[
  S('%sT18:00'%DATE, '%sT21:30'%DATE, 'h-11-16-mb',
    'Sakin Fon · Quiet Background', ITEMS),
  S('%sT21:30'%DATE, '%sT22:00'%DATE, 'h-11-16-2130',
    'Sakin Fon · Quiet Background', ITEMS),
]

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
# keep 09-17 and 22-23 (22 and 23 start at 22 and 23)
keep=[]
for s in day['sets']:
    hh=int(s['from'][11:13])
    mm=int(s['from'][14:16])
    if (hh<18) or (hh>=22):
        keep.append(s)
assert [s['from'][11:16] for s in keep]==['09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','22:00','23:00'], [s['from'] for s in keep]
# order: morning, evening override, then 22/23
morn=[s for s in keep if int(s['from'][11:13])<18]
late=[s for s in keep if int(s['from'][11:13])>=22]
day['sets']=morn+evening+late
day['rev']=REV
day['_note']='Hourly sets for the villa TV. Morning from days/build_2026-11-16.py; 18:00–22:00 rebuilt by days/build_2026-11-16_evening.py (rev 67, calm movie background until 21:30, quiet continuation until 22:00). Content log: used-content.md'
out=os.path.join(HERE,'%s.json'%DATE)
json.dump(day,open(out,'w'),ensure_ascii=False,indent=1)
print('sets',len(day['sets']),'evening scenes',sum(len(s['items']) for s in evening))
for s in day['sets']:
    hh=int(s['from'][11:13])
    mark=' *' if 18<=hh<22 or s['from'][11:16]=='21:30' else ''
    print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name']+mark)
