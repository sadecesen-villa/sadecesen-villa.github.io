# Builds /workspace/tv-pages/days/2026-11-09.json (hourly sets). Template for future daily builds: copy, change DATE + content.
import json
DATE='2026-11-09'; REV=55
import os
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-09.json')))
def cr(k):
    c=C[k]; lic=c['lic'].replace('Public domain','kamu malı · public domain')
    a=c['artist'].split('(')[0].strip().rstrip('.')
    return 'Foto · Photo: %s · %s · Wikimedia Commons'%(a,lic)
REAL='Gerçek Fotoğraf · Real Photo'; IM='Villa Fikri · Villa Idea — hayal ürünü · imagined (AI)'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,cp=None):
    it=dict(k='hzphoto',d=d,f='m/h9-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if cp: it['cp']=cp
    return it
def idea(k,tr,en,fact,facte,d=36):
    return dict(k='hzphoto',d=d,f='m/h9-idea-%s.jpg'%k,lb=IM,tr=tr,en=en,fact=fact,facte=facte,cr='Sadece Sen için üretilmiş fikir görseli · Concept image made for Sadece Sen',cp='top')
def q(tr,en,pal,d=42): return dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
def rid(qq,qe,a,ae,hint=None,sec=18,d=34,c1=None,c2=None):
    it=dict(k='hzriddle',d=d,q=qq,qe=qe,a=a,ae=ae,sec=sec)
    if hint: it['hint']=hint
    if c1: it.update(c1=c1,c2=c2)
    return it
def g(k,d=55,**kw): it=dict(k=k,d=d); it.update(kw); return it
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '2026-11-10T%02d:00'%(h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
sets=[
S(14,16,'Merak · Curiosity',[
  photo('earthrise','Apollo 8','Ay’ın ufkundan doğan Dünya, 24 Aralık 1968','Earth rising over the Moon’s horizon, 24 December 1968','Astronotlar Ay’ı keşfetmeye gitti, en çok Dünya’yı keşfettiler','They went to explore the Moon — and discovered the Earth',fit='contain'),
  g('hzcafe',d=40),
  g('hzsteps',d=50,lb='Düşünce Deneyi · Thought Experiment',q='Dünya’nın çevresine sıkıca bir ip sar. İpi sadece 1 metre uzatırsan…',e='Wrap a rope tightly around the Earth. Add just 1 metre…',bg='stars',
    steps=[['İp her yerden eşit havaya kalkar','The rope lifts evenly all round',''],['Sence kaç cm boşluk oluşur?','How big is the gap?',''],['Cevap','Answer','≈ 16 cm'],['Bir kedi altından geçebilir!','A cat could walk under it!','']],
    fin='Boşluk = 1 m ÷ 2π — Dünya’nın büyüklüğü hiç fark etmez',fine='Gap = 1 m ÷ 2π — the size of the Earth doesn’t matter at all',gap=6),
  q('Kanatlarla doğdun;|neden sürünmeyi seçesin?','You were born with wings — why choose to crawl?','ink'),
  idea('cinema','Çimde açık hava sineması: battaniye, fener, deniz manzarası','An open-air cinema on the lawn: blankets, lanterns, a sea view','Yaz akşamları misafirlere “film gecesi” — sadece beyaz bir perde ve projektör yeter','Summer “movie night” for guests — a white screen and a projector are all it takes'),
  g('hzpend',d=55),
  photo('sera','Akçaabat','Sera Gölü, Akçaabat — Trabzon’a 15 dakika','Sera Lake, Akçaabat — 15 minutes from Trabzon','Bir heyelanın dereyi kapatmasıyla oluştuğu anlatılır','It is said to have formed when a landslide dammed a stream'),
]),
S(16,17,'Desen · Patterns',[
  photo('paleblue','Voyager 1, 1990','Işık huzmesindeki o soluk mavi nokta: Dünya','That pale blue dot in the sunbeam: Earth','6 milyar km uzaktan — herkesin yaşadığı her şey o noktada','From 6 billion km away — everything anyone ever lived is on that dot',fit='contain'),
  g('hzebb',d=40),
  g('hzgalton',d=60),
  q('Aradığın şey|de seni arıyor','What you seek is seeking you','sea'),
  idea('oven','Bahçede taş fırın: misafirlerle birlikte pide akşamı','A stone oven in the garden: a pide evening with guests','Hamuru misafirler açsın, fırını villa yaksın — tatilin en çok anlatılan anı olur','Guests roll the dough, the villa fires the oven — the story they’ll tell most'),
  rid('Göldeki nilüferler her gün iki katına çıkıyor.<br>Göl 48 günde tamamen doluyor.<br>Göl yarıya kaçıncı günde dolar?','Water lilies double every day. The lake is full on day 48. On which day is it half full?','47. gün!','Day 47 — just one day before the end.',hint='Çoğu kişi “24” der… · Most people say “24”…'),
  photo('cal','Düzköy','Çal Mağarası, Düzköy — Trabzon’un yeraltındaki nehri','Çal Cave, Düzköy — Trabzon’s underground river','İçinden bir dere akar; uzunluğunun 8 km kadar olduğu söylenir','A stream runs through it; it is said to be about 8 km long'),
]),
S(17,18,'Doğa Zekâsı · Nature’s Genius',[
  photo('giresun','Giresun','Giresun Adası — Doğu Karadeniz’in tek adası','Giresun Island — the only island in the eastern Black Sea','Efsaneye göre Argonotlar Altın Post yolculuğunda buraya uğradı','Legend says the Argonauts stopped here on their quest for the Golden Fleece'),
  g('hzkaniz',d=40),
  g('hzboids',d=60),
  photo('murmur','Sığırcıklar · Starlings','Gerçek bir sığırcık sürüsü: binlerce kuş, tek bir bulut','A real starling murmuration: thousands of birds, one cloud','Bazı sürüler 100.000 kuşu geçer','Some murmurations number over 100,000 birds'),
  g('hzsteps',d=55,lb='Düşünce Deneyi · Thought Experiment — Otel Fikri',q='Hilbert’in Oteli: sonsuz oda var ve hepsi dolu',e='Hilbert’s Hotel: infinitely many rooms, all full',c1='#2a2238',c2='#06050a',
    steps=[['Yeni bir misafir geliyor…','A new guest arrives…',''],['Herkes bir sonraki odaya geçiyor: 1→2, 2→3…','Everyone moves up one room',''],['1 numaralı oda boşaldı!','Room 1 is now free!','✓'],['Sonsuz bir otobüs dolusu misafir gelirse?','An infinite busload arrives?',''],['Herkes oda numarasının 2 katına geçer','Everyone moves to double their number','n → 2n']],
    fin='Tüm tek numaralı odalar boşalır — sonsuzluk da dolmaz',fine='All the odd rooms are free — infinity never fills up',gap=6),
  idea('bikes','Kapıda iki bisiklet ve hazır piknik sepeti','Two bicycles at the door with picnic baskets ready','Misafir sabah haritayı alır, sepeti kapar ve sahile pedal çevirir','In the morning guests grab the map and the basket, and ride to the coast'),
  q('Dünle beraber gitti cancağızım,|ne kadar söz varsa düne ait;|şimdi yeni şeyler söylemek lazım','Gone with yesterday, my dear, are all of yesterday’s words — now it’s time to say new things','clay',d=48),
]),
S(18,19,'Akşamüstü Kıvılcımı · Evening Spark',[
  photo('hamsilos','Sinop','Hamsilos, Sinop — Türkiye’nin tek doğal fiyordu olarak anılır','Hamsilos, Sinop — known as Turkey’s only natural fjord','Deniz burada karaya derin bir kol gibi sokulur','Here the sea slips inland like a long, deep arm'),
  g('hzlilac',d=45),
  g('hzsteps',d=52,lb='Akıllı Düşünce · Clever Thinking',q='Doğum Günü Paradoksu',e='The Birthday Paradox',c1='#14303a',c2='#03080b',
    steps=[['Bir odada 2 kişi','2 people in a room','%0,3'],['10 kişi','10 people','%12'],['23 kişi','23 people','%50'],['50 kişi','50 people','%97'],['70 kişi','70 people','%99,9']],
    fin='Sadece 23 kişide iki kişinin aynı gün doğmuş olma şansı yarı yarıya!',fine='With just 23 people, it’s a coin flip that two share a birthday!'),
  photo('lightning','Fırtına · Storm','Gece denizin üzerinde çakan şimşekler','Lightning over the sea at night','Bir şimşek Güneş’in yüzeyinden yaklaşık 5 kat sıcaktır (~30.000 °C)','A lightning bolt is about 5× hotter than the Sun’s surface (~30,000 °C)'),
  g('hzfourier',d=50),
  rid('Ne kadar çok alırsan,<br>o kadar çok geride bırakırsın.<br>Ben neyim?','The more you take, the more you leave behind. What am I?','Ayak izleri · Adımlar','Footsteps.',c1='#2b2016',c2='#070504'),
  photo('dew','Doğa · Nature','Sabah çiyi tutmuş bir örümcek ağı','A spider web holding the morning dew','Örümcek ipeği, ağırlığına göre çelikten daha güçlüdür','Spider silk is stronger than steel, weight for weight'),
]),
S(19,20,'Küçük ve Büyük · Small & Large',[
  photo('amasra','Bartın','Amasra koyları — Karadeniz’in mavi incisi','The bays of Amasra — blue pearl of the Black Sea','Fatih Sultan Mehmet’in burayı görünce “Çeşm-i cihan bu mu?” dediği anlatılır','Mehmed the Conqueror is said to have asked: “Is this the eye of the world?”'),
  g('hzafter',d=46,f='m/h9-zigana.jpg',cr=cr('zigana'),place='Zigana, Trabzon–Gümüşhane'),
  g('hzsteps',d=60,lb='Ölçek Yolculuğu · Scale Journey',q='Her adımda 10 kat küçül…',e='Shrink 10× with every step…',bg='stars',c1='#0f1d2e',c2='#020408',gap=4.5,
    steps=[['Sen','You','1,7 m'],['Bir karınca','An ant','5 mm'],['Bir saç teli kalınlığı','A hair’s width','0,07 mm'],['Bir bakteri','A bacterium','0,002 mm'],['Bir virüs','A virus','100 nm'],['DNA sarmalı','A DNA helix','2 nm'],['Bir atom','An atom','0,1 nm']],
    fin='Atomu bir stadyum kadar büyütsen, çekirdeği ortada bir bezelye olurdu',fine='Blow an atom up to a stadium, and its nucleus would be a pea in the middle'),
  rid('Bir babanın 5 kızı var.<br>Her kızın bir erkek kardeşi var.<br>Babanın kaç çocuğu var?','A father has 5 daughters. Each daughter has one brother. How many children?','6 çocuk!','Six — all five sisters share the same brother.',hint='“10” demeden önce bir daha düşün… · Think twice before saying “10”…'),
  idea('herbs','Mutfak kapısında misafir bostanı: nane, fesleğen, kekik','A guest herb garden by the kitchen door: mint, basil, thyme','Misafir makasla kendi çayına nane, salatasına fesleğen keser','Guests snip their own mint for tea and basil for salad'),
  g('hzripple',d=55),
  photo('causeway','Kuzey İrlanda · N. Ireland','Dev Geçidi: 40.000 altıgen bazalt sütun','The Giant’s Causeway: 40,000 hexagonal basalt columns','Kimse oymadı — soğuyan lav kendi kendine altıgen çatladı','No one carved them — cooling lava cracked into hexagons by itself'),
]),
S(20,21,'Uzay ve Zaman · Space & Time',[
  photo('saturn','Cassini, 2012','Güneş, Satürn’ün tam arkasında: ışığı halkalardan süzülüyor','The Sun hidden right behind Saturn, its light glowing through the rings','Satürn sudan hafiftir — dev bir küvet bulsan yüzerdi','Saturn is less dense than water — in a giant bathtub it would float'),
  g('hzstep',d=40),
  g('hzsteps',d=55,lb='Düşünce Deneyi · Thought Experiment',q='İkiz Paradoksu: biri uzaya gidiyor, biri evde kalıyor',e='The Twin Paradox: one twin flies off, one stays home',bg='stars',c1='#101a33',c2='#02030a',
    steps=[['Işık hızının %99,5’iyle yolculuk','Travelling at 99.5% of light speed',''],['Gemide geçen süre','Time on the ship','1 yıl'],['Dünya’da geçen süre','Time on Earth','10 yıl'],['Eve dönen ikiz…','The returning twin is…','9 yaş genç!']],
    fin='Einstein (1905): hız arttıkça zaman yavaşlar — GPS uyduları bunu her gün düzeltir',fine='Einstein (1905): the faster you go, the slower time runs — GPS satellites correct for it daily',gap=6),
  q('Ne kadar bilirsen bil,|söylediklerin karşındakinin|anlayabildiği kadardır','However much you know, what you say is only as much as the other can understand','night',d=48),
  idea('hammock','Ağaçların arasında hamak köşesi ve iki ince belli çay','A hammock corner between the trees, with two tulip glasses of tea','Telefonsuz bir öğleden sonra için en iyi davet','The best invitation to a phone-free afternoon'),
  g('hzmonte',d=55),
  photo('pillars','Hubble, 2014','Yaratılış Sütunları: yıldızların doğduğu gaz bulutları','The Pillars of Creation: gas clouds where stars are born','En uzun sütun yaklaşık 4 ışık yılı boyunda','The tallest pillar is about 4 light-years long',fit='contain'),
]),
S(21,22,'Gece Merakı · Night Curiosity',[
  photo('mevlana','Konya','Mevlânâ Müzesi ve yeşil kubbesi, Konya','The Mevlânâ Museum and its green dome, Konya','Mevlânâ 1273’te Konya’da vefat etti; her yıl 17 Aralık’ta Şeb-i Arûs’ta anılır','Rumi died in Konya in 1273; he is remembered every 17 December, Şeb-i Arûs'),
  g('hzhermann',d=36),
  photo('udf','Hubble Ultra Derin Alan','Bu karanlık bir boşluk değil: yaklaşık 10.000 galaksi','This isn’t empty darkness: about 10,000 galaxies','Gökyüzünün kol boyu uzaklıktaki bir kum tanesi kadar küçük bir parçası','A patch of sky the size of a grain of sand held at arm’s length',fit='contain'),
  rid('Kullanmadan önce kırman gereken şey nedir?','What has to be broken before you can use it?','Yumurta!','An egg!',c1='#20283a',c2='#05060a',sec=15),
  g('hzulam',d=55),
  g('hzfact',d=30,big='3 ❤',tr='Ahtapotun üç kalbi ve mavi kanı vardır',en='An octopus has three hearts and blue blood',src='Kanındaki bakır yüzünden mavidir · Blue from the copper in its blood',c1='#10283a',c2='#02070c'),
  idea('firering','Taş avluda ateş halkası: post minderler, demlik ve uzakta sahil ışıkları','A fire ring in the stone courtyard: sheepskins, a teapot and distant coast lights','Gece misafirlerle hikâye saati — ateş, çay ve sessizlik','A storytelling hour with guests — fire, tea and quiet'),
]),
S(22,23,'Yatmadan Önce · Before Bed',[
  photo('istnight','Uzay İstasyonu · ISS','Uzaydan gece İstanbul: Boğaz’ın iki yakası ışık içinde','Istanbul at night from space: both shores of the Bosphorus aglow','Fotoğraf Uluslararası Uzay İstasyonu’ndan çekildi','Taken from the International Space Station',fit='contain',d=40),
  q('Sessizlik Tanrı’nın dilidir;|geri kalan her şey|kötü bir çeviridir','Silence is the language of God; all else is poor translation','night',d=48),
  g('hzfirefly',d=70),
  photo('snowflake','Wilson Bentley','İlk kar tanesi fotoğrafları — Wilson Bentley, 1885’ten itibaren','The first photographs of snowflakes — Wilson Bentley, from 1885','5.000’den fazla kar tanesi çekti; ikisinin aynı olduğunu hiç görmedi','He photographed over 5,000 and never found two alike',fit='contain',d=40),
  g('hzfact',d=32,big='Fe',tr='Kanındaki demir, milyarlarca yıl önce patlayan yıldızlarda oluştu',en='The iron in your blood was made in stars that exploded billions of years ago',src='Sen de yıldız tozundan yapıldın · You are made of stardust',c1='#1a1830',c2='#030308'),
  g('hzharmono',d=60),
]),
S(23,26,'Gece · Night (calm)',[
  photo('bsswirl','NASA uydusu · satellite','Uzaydan Karadeniz: planktonların turkuaz girdapları','The Black Sea from space: turquoise swirls of plankton','Bu renkler milyarlarca minicik canlıdan geliyor','These colours come from billions of tiny living things',fit='contain',d=45),
  g('hzphyllo',d=55),
  photo('walls1890','Trabzon, 19. yy sonu · late 1800s','Bir asırdan uzun süre önce Trabzon surları','The walls of Trabzon, more than a century ago','Fotoğrafçı Dmitri Yermakov’un objektifinden','Through the lens of photographer Dmitri Ermakov',fit='contain',d=40),
  g('hzsleep',d=70),
  photo('ataturk','Trabzon','Atatürk Köşkü, Soğuksu — çam ağaçları arasında beyaz bir köşk','The Atatürk Pavilion, Soğuksu — a white mansion among the pines','Atatürk 1937’de burada kaldı ve vasiyetini burada hazırladı','Atatürk stayed here in 1937 and prepared his will here',d=40),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by hourly/build_day.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']))
