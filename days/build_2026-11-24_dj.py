# Rev 81: DJ evening 17:00–02:00 for days/2026-11-24.json, synced with the HomePod playlists
# Act 1 –19:00 Jazz House Lounge (Sadece Sen · Jazz House Mix), Act 2 19–22 Sunset (Sadece Sen Sunset), Act 3 22–02 Night (Sadece Sen Night).
# Photos m/h81-* (credits-2026-11-24n.json). All visuals silent.
import json, os
DATE='2026-11-24'; REV=81
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-24n.json')))
ART={'sax':'Jimmy Baikovicius','candle':'Andrew Fogg','milkyway':'ESO/Yuri Beletsky','jazzclub':'FingerWiki','records':'ביקורת (Bikoret)'}
def artist(k): return ART.get(k) or C[k]['artist'].split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('CC0','CC0 · kamu malı · public domain')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
A1='1. Perde · Act 1 — Caz House Lounge · Jazz House Lounge'
A2='2. Perde · Act 2 — Gün Batımı · Sunset'
A3='3. Perde · Act 3 — Gece · Night'
def photo(k,act,where,tr,en,fact=None,facte=None,d=40,pos=None,fit=None,quiet=None):
    assert k in C,k
    it=dict(k='hzphoto',d=d,f='m/h81-%s.jpg'%k,lb='%s · %s · %s'%(act,REAL,where),tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if pos: it['pos']=pos
    if fit: it['fit']=fit
    if quiet: it['quiet']=1
    return it
def card(k,lb,lines,tr,en,d=30,pos=None):
    it=dict(k='hzwelcome',d=d,f='m/h81-%s.jpg'%k,lb=lb,lines=lines,tr=tr,en=en,cr=cr(k))
    if pos: it['pos']=pos
    return it
def q(tr,en,pal,lb,by,d=36): return dict(k='hzquote',d=d,tr=tr,en=en,pal=pal,lb=lb,by=by)
def fact(big,tr,en,src,c1,c2,d=30): return dict(k='hzfact',d=d,big=big,tr=tr,en=en,src=src,c1=c1,c2=c2)
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items,day2=False):
    u='%sT%02d:00'%('2026-11-25' if day2 else DATE,h2)
    return dict(id='dj-%s-%02d'%(DATE[5:],h1),name=name,**{'from':'%sT%02d:00'%(DATE,h1),'until':u},items=items)

new=[
S(17,18,'DJ Taş · Caz House Lounge · Jazz House Lounge',[
 card('jazzclub','DJ Taş · Sadece Sen — '+REAL+' · bir caz kulübü · a jazz club',[['DJ Taş',7.2],['Bu akşam · Tonight',3.4]],
  'Üç perdelik bir akşam: Caz House Lounge → Gün Batımı → Gece. Müzik HomePod’da','An evening in three acts: Jazz House Lounge → Sunset → Night. Music on the HomePod',d=34,pos='50% 60%'),
 photo('turntable',A1,'Plak iğnesi · Stylus on vinyl','İğne plağın oluğunda: müzik buradan başlıyor','The needle in the groove: this is where the music begins',
  'Bir LP’nin her yüzünde tek bir spiral oluk vardır; iğne onu baştan sona yaklaşık 450 metre boyunca izler','Each side of an LP has a single spiral groove — the needle follows it for roughly 450 metres from start to finish',d=42),
 g('hzchladni',64),
 photo('sax',A1,'Punta del Este Caz Festivali, Uruguay · Jazz Festival','Sahnede bir saksafoncu: caz house’un kalbindeki ses','A saxophonist on stage — the sound at the heart of jazz house',
  'Saksafonu 1840’larda Belçikalı Adolphe Sax icat etti; pirinçten yapılsa da bir nefesli ağaç çalgı sayılır, çünkü kamışla çalınır','Adolphe Sax invented it in the 1840s — though made of metal it counts as a woodwind, because it is played with a reed',d=40,pos='50% 30%'),
 fact('Rose Rouge','St Germain’in “Rose Rouge” parçası 2000’de Blue Note’tan çıkan “Tourist” albümünde; içindeki ses Marlena Shaw’un “Woman of the Ghetto” kaydından','St Germain’s “Rose Rouge” is on “Tourist”, released by Blue Note in 2000 — the voice in it is sampled from Marlena Shaw’s “Woman of the Ghetto”','Bu akşamın listesinden · From tonight’s playlist','#2a1c14','#0a0605',d=32),
 g('hzmeta',60),
 photo('records',A1,'Bir plakçı · A record shop','Kaldırımda plak kasaları: her kapak başka bir akşamın sözü','Crates of records on the pavement — every sleeve the promise of another evening',d=38),
]),
S(18,19,'Caz House Lounge · Jazz House Lounge — altın saat · golden hour',[
 photo('cocktail',A1,'Lounge','Terasta serin bir içki ve batmaya hazırlanan güneş','A cool drink on the terrace while the sun gets ready to set',d=36),
 g('hzharmono',64),
 q('Hatalardan korkma. Hata diye bir şey yoktur.','Do not fear mistakes. There are none.','clay','Cazın Sözü · Words of Jazz','Miles Davis'),
 photo('jazzclub',A1,'Bir caz kulübü · A jazz club','Kırmızı ışıkta bekleyen piyano ve sahne: set birazdan başlıyor','A piano and stage waiting in red light — the set is about to start',
  'Deep house 1980’lerde Chicago’da doğdu; caz ve soul akorlarını house ritmiyle buluşturdu','Deep house was born in 1980s Chicago, bringing jazz and soul chords together with the house beat',d=40,pos='50% 55%'),
 g('hzkaleido',60),
 fact('33⅓','Uzunçalar plak 1948’de Columbia tarafından tanıtıldı: dakikada 33⅓ devirle her yüze yaklaşık 20 dakika müzik sığdı','The long-playing record was introduced by Columbia in 1948 — at 33⅓ turns a minute it fitted about 20 minutes of music per side','Plağın hikâyesi · The story of vinyl','#1e1a26','#07060a',d=30),
]),
S(19,20,'Gün Batımı · Sunset — Karadeniz · Black Sea',[
 card('batumi','DJ Taş · 2. Perde · Act 2 — '+REAL+' · Batum, Gürcistan · Batumi, Georgia',[['Gün Batımı',6.4],['Sunset',3.6]],
  'Liste değişti: şimdi “Sadece Sen Sunset” çalıyor','The playlist has changed — now playing “Sadece Sen Sunset”',d=30),
 photo('bssunset',A2,'Karadeniz · Black Sea','Karadeniz’de bir iskeleden güneşin son ışıkları','The last light of the sun from a jetty on the Black Sea',
  'Karadeniz’in derinlerinde neredeyse hiç oksijen yok: 150 metrenin altındaki batıklar binlerce yıl bozulmadan kalabiliyor','The deep Black Sea has almost no oxygen — wrecks below about 150 m can survive intact for thousands of years',d=42),
 g('hzripple',56),
 photo('sinop',A2,'Sinop','Sinop’ta güneş denize inerken','The sun going down into the sea at Sinop',
  'Sinop, Türkiye’nin en kuzey ucuna yakın: Karadeniz kıyısının ortasında bir yarımada','Sinop sits near Turkey’s northernmost point — a peninsula in the middle of the Black Sea coast',d=40),
 photo('batumi',A2,'Batum, Gürcistan · Batumi, Georgia','Batum’da bulutların arasından denize düşen akşam ışığı','Evening light breaking through the clouds over the sea at Batumi',d=40),
 q('Müzik olmasaydı hayat bir hata olurdu.','Without music, life would be a mistake.','sea','Müzik Üzerine · On Music','Friedrich Nietzsche'),
]),
S(20,21,'Gün Batımı · Sunset — Akdeniz ve Ege · Mediterranean & Aegean',[
 photo('oludeniz',A2,'Ölüdeniz, Fethiye','Ölüdeniz’de güneş tepelerin ardına iniyor','The sun sliding behind the hills at Ölüdeniz',d=42),
 g('hzspiro',60),
 photo('bodrum',A2,'Bodrum','Bodrum’un yel değirmeni gün batımına karşı','A Bodrum windmill against the sunset',
  'Bodrum yel değirmenleri 18. yüzyıldan kalma; bir zamanlar rüzgârla buğday öğütüyorlardı','The Bodrum windmills date from the 18th century — they once ground wheat with the wind',d=40),
 photo('sailboat',A2,'Altın deniz · Golden sea','Altın rengine dönen denizde bir yelkenli ve yüzenler','A sailboat and swimmers on a sea turning gold',d=40),
 fact('Yeşil şimşek','Güneş denize tam batarken bazen bir saniyeliğine yeşil bir ışık çakar: hava, ışığı bir prizma gibi kırar','Just as the sun disappears into the sea, a green flash sometimes appears for a second — the air bends the light like a prism','Green flash · Atmosfer optiği · Atmospheric optics','#1a2a24','#050a08',d=30),
 photo('kas',A2,'Kaş, Antalya','Kaş’ta akşam: minare, kubbe ve batan güneş','Evening in Kaş: a minaret, a dome and the setting sun',d=40),
]),
S(21,22,'Gün Batımı · Sunset — son ışık · last light',[
 photo('seagull',A2,'Batı Avustralya · Western Australia','Gün batımında kayalıkların üzerinden süzülen bir martı','A seagull gliding over the rocks at sunset',d=40),
 g('hzrose',60),
 photo('sinop',A2,'Sinop','Karadeniz’de günün son ışığı','The last light of the day on the Black Sea',d=38),
 q('Müzik, kelimelerin bittiği yerde başlar.','Where words fail, music speaks.','clay','Müzik Üzerine · On Music','Hans Christian Andersen'),
 photo('oludeniz',A2,'Ölüdeniz, Fethiye','Ölüdeniz’de günün son ışığı','The last light of the day at Ölüdeniz',d=38),
 g('hzkoi',56),
]),
S(22,23,'Gece · Night — şehir ışıkları · city lights',[
 card('ortakoy','DJ Taş · 3. Perde · Act 3 — '+REAL+' · Ortaköy, İstanbul',[['Gece',6.6],['Night',3.6]],
  'Şimdi “Sadece Sen Night” çalıyor: daha yumuşak, daha sakin','Now playing “Sadece Sen Night” — softer and calmer',d=30),
 photo('galata',A3,'Galata Kulesi, İstanbul · Galata Tower','Gece Galata Kulesi ve Haliç’in ışıkları','The Galata Tower and the lights of the Golden Horn at night',
  'Kule 1348’de Cenevizliler tarafından yapıldı; yaklaşık 67 metre yüksekliğinde','The tower was built by the Genoese in 1348 and stands about 67 m tall',d=42),
 g('hzmoonsea',70),
 photo('bridge',A3,'İstanbul Boğazı · Bosphorus','Boğaz’da gece: köprünün ve kıyının ışıkları suya düşüyor','Night on the Bosphorus: the lights of the bridge and the shore fall on the water',d=40,quiet=1),
 photo('candle',A3,'Mum ışığı · Candlelight','Karanlıkta tek bir mum: akşamın en sakin ışığı','A single candle in the dark — the calmest light of the evening',d=40,quiet=1),
 g('hzyakamoz',70),
]),
S(23,2,'Gece · Night — yıldızlar ve sakinlik · stars and calm',[
 photo('moonsea',A3,'Ay ışığı · Moonlight','Denizin üzerinde ay ışığı','Moonlight over the sea',d=44,quiet=1),
 g('hzgalaxy',70),
 photo('milkyway',A3,'ESO, Şili · Chile','Samanyolu’nun merkezine uzanan bir lazer ışını: gökbilimciler atmosferin titreşimini böyle ölçer','A laser beam reaching toward the centre of the Milky Way — astronomers use it to measure the shimmer of the air',d=44,quiet=1),
 g('hzrainwin',70),
 photo('candle',A3,'Mum ışığı · Candlelight','İyi geceler · Good night','Good night',d=40,quiet=1),
 g('hzsleep',70),
],day2=True),
]

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
keep=[s for s in day['sets'] if s['from'][11:13] < '17']
day['sets']=keep+new
day['rev']=REV
day['_note']='Hourly sets for the villa TV. 09:00–17:00 from build_2026-11-24.py / build_2026-11-24_afternoon.py; 17:00–02:00 = DJ Taş evening (rev 81, build_2026-11-24_dj.py): Jazz House Lounge → Sunset (19:00) → Night (22:00), synced with the HomePod playlists.'
json.dump(day,open(os.path.join(HERE,'%s.json'%DATE),'w'),ensure_ascii=False,indent=1)
for s in day['sets']: print(s['id'],s['from'][11:16],s['until'][5:16],len(s['items']),s['name'])
