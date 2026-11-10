# Builds /workspace/tv-pages/days/2026-11-10.json (hourly sets). Copied from build_2026-11-09.py.
import json,os,sys
DATE='2026-11-10'; REV=int(os.environ.get('REV','55')); UPTO=int(os.environ.get('UPTO','99'))
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-10.json')))
def cr(k):
    c=C[k]; lic=c['lic'].replace('Public domain','kamu malı · public domain')
    a=c['artist'].split('(')[0].strip().rstrip('.')
    a={'Photo by User:Wikimol':'Wikimol','Created by Wolfgang Beyer with the program Ultra Fractal 3':'Wolfgang Beyer','Joe Robertson from Austin, Texas, USA':'Joe Robertson','NASA, ESA, and A. Simon':'NASA, ESA, A. Simon'}.get(a,a)
    if a.startswith('Created by Wolfgang Beyer'): a='Wolfgang Beyer'
    return 'Foto · Photo: %s · %s · Wikimedia Commons'%(a,lic)
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,cp=None,pos=None):
    it=dict(k='hzphoto',d=d,f='m/h10-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if cp: it['cp']=cp
    if pos: it['pos']=pos
    return it
def villa(k,tr,en,fact,facte,d=38,cp=None,where=''):
    it=photo(k,'',tr,en,fact,facte,d=d,cp=cp)
    it['lb']='Villa Fikri · Villa Idea — ilham için gerçek fotoğraf · real photo for inspiration'+(' · '+where if where else '')
    return it
def q(tr,en,pal,d=44,fs=None):
    it=dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
    if fs: it['fs']=fs
    return it
def rid(qq,qe,a,ae,hint=None,sec=18,d=34,c1=None,c2=None,lb=None):
    it=dict(k='hzriddle',d=d,q=qq,qe=qe,a=a,ae=ae,sec=sec)
    if hint: it['hint']=hint
    if c1: it.update(c1=c1,c2=c2)
    if lb: it['lb']=lb
    return it
def g(k,d=55,**kw): it=dict(k=k,d=d); it.update(kw); return it
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '2026-11-11T%02d:00'%(h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
sets=[
S(9,10,'Günaydın Karadeniz · Good Morning, Black Sea',[
  photo('ayder','Rize','Ayder Yaylası, Çamlıhemşin — sisin içinde ahşap evler','Ayder plateau, Çamlıhemşin — wooden houses in the mist','Kaplıcalarıyla da bilinir — Kaçkar Dağları’nın eteğinde','Also known for its hot springs — at the foot of the Kaçkar Mountains'),
  q('Her gün bir yerden göçmek ne iyi;|her gün bir yere konmak ne güzel','How good to move on from somewhere every day — how lovely to settle somewhere new every day','sea'),
  g('hzsteps',d=60,lb='Ölçek Yolculuğu · Scale Journey — Zaman · Time',q='Dünya’nın 4,5 milyar yılını tek bir güne sığdır…',e='Squeeze Earth’s 4.5 billion years into a single day…',c1='#1b2a22',c2='#040805',gap=5,
    steps=[['00:00 — Dünya doğuyor','Earth is born',''],['≈ 04:00 — ilk canlılar','First life','04:00'],['≈ 22:45 — dinozorlar geliyor','Dinosaurs arrive','22:45'],['≈ 23:39 — dinozorlar yok oluyor','Dinosaurs vanish','23:39'],['Son 6 saniye — biz, Homo sapiens','The last 6 seconds — us','23:59:54']],
    fin='Tüm yazılı tarih, son saniyenin onda birinden bile kısa',fine='All of written history is shorter than a tenth of the very last second'),
  rid('Sabah dört ayakla,<br>öğlen iki ayakla,<br>akşam üç ayakla yürüyen nedir?','Four legs in the morning, two at noon, three in the evening — what is it?','İnsan!','A human: crawling baby, walking adult, elder with a cane.',hint='Antik Yunan’daki Sfenks’in bilmecesi · The riddle of the Sphinx',c1='#2a2a1c',c2='#070705'),
  photo('bee','Bal arısı · Honey bee','Kekik çiçeğinde bir bal arısı','A honey bee on an oregano flower','Bir arının ömrü boyunca bir çay kaşığının yalnızca küçük bir kısmı kadar bal yaptığı söylenir','A single bee is said to make only a small fraction of a teaspoon of honey in its whole life'),
  photo('kaymakli','Trabzon','Kaymaklı Manastırı — şehrin içinde saklı tarihî bir manastır','Kaymaklı Monastery — a historic monastery hidden within the city','İçindeki freskolar yüzyıllardır duruyor; bugün bir çiftlik arazisinde','Its frescoes have survived for centuries; today it stands on farmland'),
]),
S(10,11,'Işık ve Renk · Light & Colour',[
  photo('rainbow','Norveç · Norway','Çift gökkuşağı — ikincisinde renkler ters sırada','A double rainbow — the second one has its colours reversed','İkisinin arasındaki koyu banda “Alexander’ın karanlık şeridi” denir','The darker sky between them is called Alexander’s dark band'),
  g('hzsteps',d=56,lb='Akıllı Açıklama · Clever Explainer',q='Gökyüzü öğlen mavi, akşam neden kızıl?',e='Why is the sky blue at noon but red at sunset?',c1='#1d3350',c2='#05080f',gap=5.5,
    steps=[['Güneş ışığı bütün renkleri taşır','Sunlight carries every colour',''],['Hava, mavi ışığı en çok saçar','Air scatters blue light the most',''],['Öğlen: ışık havada kısa yol alır','Noon: light crosses little air','→ mavi gök'],['Akşam: ışık havada çok uzun yol alır','Sunset: light crosses lots of air',''],['Mavi yolda dağılır, geriye kızıl kalır','Blue is scattered away, red remains','→ kızıl ufuk']],
    fin='Buna Rayleigh saçılması denir (Lord Rayleigh, 1871)',fine='This is called Rayleigh scattering (Lord Rayleigh, 1871)'),
  photo('morpho','Morpho kelebeği · Morpho butterfly','Bu mavi bir boya değil','This blue is not a pigment','Renk, kanat pullarındaki mikroskobik yapıların ışığı kırmasından doğar','It comes from microscopic structures on the wing scales bending the light'),
  q('Bu dünya bir dağdır;|yaptıklarımız ses gibi yine bize döner','This world is a mountain, our deeds are the shout — and the echo comes back to us','clay',d=48,fs=92),
  photo('fogbow','Estonya · Estonia','Sis yayı: beyaz bir gökkuşağı','A fogbow: a white rainbow','Sis damlaları çok küçük olduğundan renkler birbirine karışıp beyazlaşır','Fog droplets are so tiny that the colours blend into white'),
  rid('Hangi ayda<br>28 gün vardır?','Which month has 28 days?','Hepsinde!','All of them — every month has at least 28 days.',hint='Şubat demeden önce düşün… · Think before you say February…',sec=15,c1='#1b2c3d',c2='#04070b'),
]),
S(11,12,'Zihin Modelleri · Mental Models',[
  g('hzsteps',d=58,lb='Zihin Modeli · Mental Model',q='Hayatta Kalan Yanılgısı',e='Survivorship Bias',c1='#2a3036',c2='#06080a',gap=6,
    steps=[['II. Dünya Savaşı: dönen uçaklarda delikler kanat ve gövdede','WWII: returning planes had holes in wings and body',''],['Komutanlar: “Delik olan yerleri zırhlayalım”','Commanders: “Armour where the holes are”',''],['Matematikçi Abraham Wald: “Hayır — motorları”','Mathematician Abraham Wald: “No — the engines”','!'],['Motorundan vurulanlar hiç geri dönememişti','Planes hit in the engine never came back','']],
    fin='Sadece görünenleri sayma — görünmeyenleri de sor',fine='Don’t just count what you can see — ask about what’s missing'),
  q('Akıllı düşman,|cahil dosttan iyidir','A wise enemy is better than an ignorant friend','ink'),
  g('hzsteps',d=60,lb='Düşünce Deneyi · Thought Experiment',q='Monty Hall: 3 kapı, birinin arkasında araba',e='Monty Hall: 3 doors, a car behind one',c1='#33241c',c2='#080504',gap=6,
    steps=[['1 numaralı kapıyı seçiyorsun','You pick door 1',''],['Sunucu boş olan 3. kapıyı açıyor','The host opens door 3 — empty',''],['“Kapını değiştirmek ister misin?”','“Do you want to switch?”','?'],['Değiştirirsen kazanma şansı','If you switch, your chance is','2/3'],['Değiştirmezsen','If you stay','1/3']],
    fin='Sunucu boş kapıyı bilerek açtı — bu sana bilgi verir',fine='The host knew which door was empty — and that gives you information'),
  photo('antiky','Atina · Athens','Antikythera düzeneği: yaklaşık 2.000 yıllık bir “bilgisayar”','The Antikythera mechanism: a “computer” about 2,000 years old','Güneş, Ay ve tutulmaları hesaplamak için kullanıldığı düşünülüyor; 1901’de bir batıktan çıkarıldı','Thought to have computed the Sun, Moon and eclipses; recovered from a shipwreck in 1901'),
  g('hzsteps',d=50,lb='Zihin Modeli · Mental Model',q='Sabah bahçedeki çimler ıslak. Neden?',e='The lawn is wet this morning. Why?',c1='#183024',c2='#030805',gap=5.5,
    steps=[['A: Gece yağmur yağdı','A: It rained in the night','1 varsayım'],['B: Komşunun fıskiyesi açık kaldı','B: The neighbour’s sprinkler ran','2 varsayım'],['C: Uzaylılar gizlice bahçeyi suladı','C: Aliens secretly watered it','çok varsayım']],
    fin='Ockham’ın Usturası: önce en az varsayım isteyen açıklamayı dene',fine='Occam’s Razor: try the explanation that needs the fewest assumptions first'),
  rid('Bir salyangoz 10 metrelik kuyunun dibinde.<br>Gündüz 3 m tırmanıyor, gece 2 m kayıyor.<br>Kaçıncı gün kuyudan çıkar?','A snail is at the bottom of a 10 m well. It climbs 3 m by day and slips 2 m at night. On which day does it get out?','8. gün!','Day 8 — after 7 nights it is at 7 m, then climbs the last 3 m.',hint='“10” cevabı tuzak… · “10” is the trap…',sec=22,d=38,c1='#24301e',c2='#060805'),
  photo('karaca','Gümüşhane','Karaca Mağarası — Trabzon–Gümüşhane yolunda','Karaca Cave — on the Trabzon–Gümüşhane road','Sarkıtların çoğu zaman yılda bir milimetreden bile az büyüdüğü söylenir','Stalactites are said to often grow less than a millimetre a year'),
]),
]
sets=[s for s in sets if int(s['id'][-2:])<UPTO]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-10.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),s['name'])
