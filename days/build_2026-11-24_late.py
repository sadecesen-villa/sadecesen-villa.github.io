# Rev 82: late-night TV 22:45–02:00 synced with the hand-sequenced HomePod DJ set
# 22:45–23:30 Monaco After Dark lounge jazz house; 23:30–00:00 deeper organic/melodic house;
# 00:00–02:00 soft wind-down. Photoreal stills (m/h82-*, quiet, no zoom) + muted 4K YouTube (hzvideo).
import json, os
DATE='2026-11-24'; REV=82
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-24n2.json')))
ART={
 'monaco':'FromMorningToMidnight','hercule':'Renek78','nice':'Miguel Mendez',
 'cannes':'Thomas Bonte','yacht':'Nicolas Völcker','hk':'Benh LIEU SONG',
 'sougia':'Aggelospallikarakis','waves':'Daniel Lepoittevin','wadirum':'Faraheed',
 'fire':'Minja Klarić','moonsea':'Giuseppe Milo','rain':'Defi22','starsfjord':'W. Carter',
}
def artist(k): return ART.get(k) or C[k]['artist'].split('(')[0].strip().rstrip('.')
def lic(k):
    L=C[k]['lic']
    if L in ('CC0','Public domain'): return 'CC0 · kamu malı · public domain' if L=='CC0' else 'kamu malı · public domain'
    return L
def cr(k):
    assert k in C,k
    return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
def photo(k,tr,en,d=44,pos=None):
    assert k in C,k
    it=dict(k='hzphoto',d=d,f='m/h82-%s.jpg'%k,tr=tr,en=en,cr=cr(k),quiet=1)
    if pos: it['pos']=pos
    return it
def video(yt,start,poster,tr,en,vcr,d=80):
    it=dict(k='hzvideo',d=d,yt=yt,start=start,f='m/h82-%s.jpg'%poster,tr=tr,en=en,cr=vcr,quiet=1)
    return it

A1='22:45–23:30'
new=[
dict(id='dj-11-24-2245', name='Monaco After Dark · Lounge Jazz House',
     **{'from':'2026-11-24T22:45','until':'2026-11-24T23:30'},
     items=[
        video('ISaZ91muY_0', 20, 'monaco',
              'Monaco gecesi: şehir ışıkları ve liman','Monaco at night: city lights and the harbour',
              'Görüntü · Footage: Paulo Leal 4K, YouTube', d=85),
        photo('monaco','Monte-Carlo limanı gece','Monte Carlo harbour at night', d=44),
        photo('hercule','Port Hercule’de yatlar, Monaco','Yachts in Port Hercule, Monaco', d=44),
        photo('nice','Promenade des Anglais, Nice, gece','The Promenade des Anglais in Nice at night', d=44),
        photo('cannes','Cannes limanı gece','Cannes harbour at night', d=44),
        photo('yacht','Gece denizde bir yat, Lipari','A yacht on the water at night, Lipari', d=46),
        photo('hk','Hong Kong limanı, yağmurlu bir gece','Hong Kong harbour on a rainy night', d=44),
     ]),
dict(id='dj-11-24-2330', name='Derin House · Deeper House',
     **{'from':'2026-11-24T23:30','until':'2026-11-25T00:00'},
     items=[
        video('qO7dPPqwQ_w', 45, 'sougia',
              'Gece sahilinde bir ateş','A fire on the beach at night',
              'Görüntü · Footage: Nature Soundscapes, YouTube', d=85),
        photo('sougia','Sougia, Girit: ay ışığında sahil','Sougia, Crete: the beach in moonlight', d=46),
        photo('waves','Akdeniz’de gece dalgaları, Grau d’Agde','Night waves on the Mediterranean at Grau d’Agde', d=46),
        video('1T1to3DU9pg', 40, 'wadirum',
              'Çölde ateş','A fire in the desert',
              'Görüntü · Footage: Beautiful Relaxation, YouTube', d=85),
        photo('wadirum','Vadi Rum’da Samanyolu','The Milky Way over Wadi Rum', d=48),
        photo('fire','Ateş ışığı','Firelight', d=44, pos='50% 40%'),
     ]),
dict(id='dj-11-25-0000', name='Sakinlik · Wind-down',
     **{'from':'2026-11-25T00:00','until':'2026-11-25T02:00'},
     items=[
        photo('moonsea','Ayın denize düşen yolu','The moon’s path on the sea', d=50),
        video('iLs04Z6uBqU', 45, 'rain',
              'Cama vuran yağmur','Rain on the window',
              'Görüntü · Footage: Relaxation Windows 4K Nature, YouTube', d=90),
        photo('rain','Camdaki yağmur ve şehir ışıkları','Rain on the glass and city lights', d=48),
        photo('starsfjord','Fiyort üzerinde yıldızlar, Åbyfjorden','Stars over the Åby fjord', d=52),
     ]),
]

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
keep=[s for s in day['sets'] if s['from'] < '2026-11-24T22:45']
# also drop any leftover 22:00 or 23:00 night sets if from is earlier but until overlaps
keep=[s for s in keep if not (s.get('until','') > '2026-11-24T22:45' and s['from'] >= '2026-11-24T22:00')]
day['sets']=keep+new
day['rev']=REV
day['_note']='Hourly sets for the villa TV. 09:00–17:00 from the morning/afternoon builds; 17:00–22:00 = DJ Taş evening (rev 81); 22:45–02:00 = rev 82 late-night DJ set matching the HomePod arc (Monaco After Dark → deeper house → wind-down). Photoreal stills m/h82-* and muted YouTube (hzvideo).'
json.dump(day,open(os.path.join(HERE,'%s.json'%DATE),'w'),ensure_ascii=False,indent=1)
for s in day['sets']:
    print(s['id'], s['from'][11:], s['until'][5:], len(s['items']), s['name'])
