# Builds /workspace/tv-pages/days/2026-11-10.json (hourly sets). Copied from build_2026-11-09.py.
import json,os,sys
DATE='2026-11-10'; REV=int(os.environ.get('REV','56')); UPTO=int(os.environ.get('UPTO','99'))
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
    it['lb']='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo)'
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
S(12,13,'Karadeniz Yolları · Black Sea Roads',[
  photo('yason','Ordu','Yason Burnu, Perşembe — denize uzanan kayalık burun','Cape Yason, Perşembe — a rocky cape reaching into the sea','Burunda 19. yüzyıldan kalma küçük bir taş kilise bulunur','A small 19th-century stone church stands on the cape'),
  g('hzfact',d=30,big='½+',tr='Dünyadaki fındığın yarısından fazlası Türkiye’de yetişir — çoğu da Karadeniz’de',en='More than half of the world’s hazelnuts grow in Turkey — most of them along the Black Sea',src='Ordu, Giresun ve Trabzon yamaçları · The slopes of Ordu, Giresun and Trabzon',c1='#2a2416',c2='#060503'),
  photo('kemer','Rize','Fırtına Deresi üzerinde taş kemer köprü, Çamlıhemşin','A stone arch bridge over the Fırtına stream, Çamlıhemşin','Vadide bunun gibi pek çok tarihî taş köprü olduğu anlatılır','The valley is said to hold many historic stone bridges like this'),
  rid('Aç karnına<br>kaç tane yumurta yiyebilirsin?','How many eggs can you eat on an empty stomach?','Sadece bir tane!','Just one — after that your stomach isn’t empty any more.',sec=16,c1='#2b2a1a',c2='#070704'),
  photo('tonya','Trabzon','Tonya — tereyağıyla ünlü, bulutların arasındaki dağ ilçesi','Tonya — a mountain town in the clouds, famous for its butter','Sahilden kısa bir yolculukla denizden bulutların arasına çıkılır','A short drive from the coast takes you from the sea up into the clouds'),
  photo('rizetea','Rize','Rize’nin çay bahçeleri — yamaçlarda yeşil teraslar','Rize’s tea gardens — green terraces on the slopes','Kişi başına çay tüketiminde Türkiye dünyanın en önlerinde','Turkey is among the world’s top tea drinkers per person'),
]),
S(13,14,'Sonsuz Desenler · Endless Patterns',[
  photo('romanesco','Romanesko · Romanesco','Kendini tekrar eden bir sebze','A vegetable that repeats itself','Her tomurcuk, bütünün küçük bir kopyası — doğal bir fraktal','Every bud is a small copy of the whole — a natural fractal'),
  g('hzkoch',d=50),
  dict(photo('mandel','',
   'Mandelbrot kümesi: kısa bir formülden sonsuz detay','The Mandelbrot set: endless detail from one short formula','z → z² + c — ne kadar yakınlaşırsan yakınlaş, yeni desenler çıkar','z → z² + c — however far you zoom, new patterns appear',fit='contain'),lb='Matematik Görseli · Maths Image — bilgisayar çizimi · computer rendering'),
  g('hzsteps',d=54,lb='Düşünce Deneyi · Thought Experiment',q='Karadeniz kıyısı kaç kilometre?',e='How long is the Black Sea coastline?',c1='#0f2c3a',c2='#03080b',gap=5.5,
    steps=[['100 km’lik bir cetvelle ölç','Measure with a 100 km ruler','kısa'],['10 km’lik cetvelle ölç','Use a 10 km ruler','daha uzun'],['1 metrelik cetvelle ölç','Use a 1 metre ruler','çok daha uzun'],['Her koyu, her kayayı saydıkça…','Count every cove and rock…','↑']],
    fin='Kıyı Şeridi Paradoksu: cetvel küçüldükçe kıyı uzar (Mandelbrot, 1967)',fine='The Coastline Paradox: the smaller the ruler, the longer the coast (Mandelbrot, 1967)'),
  rid('Dişleri var<br>ama hiç ısırmaz.<br>Nedir?','It has teeth but never bites. What is it?','Tarak!','A comb.',sec=15,c1='#1f2a33',c2='#050709'),
]),
S(14,15,'Butik Otel Fikirleri · Boutique Hotel Ideas',[
  villa('trulli','Konik taş çatılı evler — Alberobello, İtalya','Cone-roofed stone houses — Alberobello, Italy','Fikir: bahçede bal rengi taştan, kubbeli küçük bir okuma kulübesi','Idea: a small domed reading hut in the garden, built of honey-coloured stone',where='İtalya · Italy'),
  g('hzsteps',d=58,lb='Düşünce Deneyi · Thought Experiment — Villa',q='Cehalet Peçesi: villa kurallarını sen yazıyorsun…',e='The Veil of Ignorance: you write the villa’s house rules…',c1='#2a2a24',c2='#070706',gap=5.5,
    steps=[['…ama hangi misafir olacağını bilmiyorsun','…but you don’t know which guest you’ll be',''],['Erken kalkan mı, geç yatan mı?','The early riser or the night owl?','?'],['Çocuklu bir aile mi, balayı çifti mi?','A family with kids or honeymooners?','?'],['Herkese adil kurallar yazarsın','You end up writing rules fair to all','✓']],
    fin='John Rawls (1971): kim olacağını bilmeden tasarla — adil olur',fine='John Rawls (1971): design without knowing who you’ll be — and it turns out fair'),
  villa('wisteria','Mor salkım pergolası','A wisteria pergola','Fikir: taş terasın üstünde mor salkım — birkaç yılda doğal bir gölgelik olur','Idea: wisteria over the stone terrace — in a few years it becomes a natural canopy',where='Japonya · Japan'),
  g('hzfact',d=32,lb='Misafir Psikolojisi · Guest Psychology',big='Zirve + Son',tr='Misafirler bir tatili en güzel anı ve son anıyla hatırlar',en='Guests remember a stay by its best moment and its final moment',src='Kahneman’ın Zirve-Son Kuralı · Fikir: ayrılırken ev yapımı reçel ve el yazısı bir not · Idea: homemade jam and a handwritten note at departure',c1='#22302a',c2='#050806'),
  villa('lavender','Lavanta sıraları','Rows of lavender','Fikir: güneşli, süzek toprağı olan bir yamaçta lavanta — misafir kapıya kokuyla gelir','Idea: lavender on a sunny, well-drained slope — guests arrive at the door through its scent',where='Fransa · France'),
  villa('infinity','Ufka karışan havuz','A pool that melts into the horizon','Fikir: deniz manzarasına bakan sonsuzluk kenarlı bir havuz — su ile deniz tek çizgi olur','Idea: an infinity-edge pool facing the sea — water and sea become one line',cp='top'),
]),
S(15,16,'Hayvan Dâhileri · Animal Geniuses',[
  photo('tern','İzlanda · Iceland','Kutup deniz kırlangıcı','The Arctic tern','Her yıl Kuzey Kutbu’ndan Antarktika’ya gidip gelir; ömrü boyunca Ay’a üç kez gidip gelecek kadar uçtuğu hesaplanmış','It flies from the Arctic to the Antarctic and back every year — over a lifetime, about three round trips to the Moon, researchers estimate'),
  g('hzlangton',d=56),
  photo('monarch','Kral kelebeği · Monarch','Kral kelebeği, çarkıfelek çiçeğinde','A monarch butterfly on a passionflower','Kuzey Amerika’dan Meksika’ya binlerce km göç eder; yolculuğu birkaç kuşak birlikte tamamlar','It migrates thousands of km from North America to Mexico — a journey completed over several generations'),
  rid('Bir çiftlikte 15 koyun var.<br>9 tanesi hariç hepsi kaçtı.<br>Kaç koyun kaldı?','A farmer has 15 sheep. All but 9 run away. How many are left?','9 koyun!','Nine — “all but 9” ran away.',hint='Çıkarma yapma… · Don’t subtract…',sec=16,c1='#22301c',c2='#060805'),
  photo('tardigrade','Mikroskop · Microscope','Su ayısı (tardigrad): yarım milimetrelik bir hayatta kalma ustası','The water bear (tardigrade): a half-millimetre survival master','Kuruyup yıllarca bekleyebilir, suyla yeniden canlanır; 2007’de uzay boşluğunda bile hayatta kaldı','It can dry out for years and revive with water — in 2007 it even survived open space',fit='contain'),
  g('hzfact',d=30,big='450 › 385',tr='Köpekbalıkları ağaçlardan daha eskidir',en='Sharks are older than trees',src='İlk köpekbalıkları ~450 milyon, ilk ağaçlar ~385 milyon yıl önce · First sharks ~450 million years ago, first trees ~385 million',c1='#0f2a36',c2='#02070a'),
]),
S(16,17,'Göz Oyunları · Eye Tricks',[
  g('hzcheck',d=40),
  photo('owl','Kar baykuşu · Snowy owl','Kar baykuşu, kumulların arasında','A snowy owl among the dunes','Baykuşlar gözlerini oynatamaz — bunun yerine başlarını 270° kadar çevirebilir','Owls can’t move their eyes — instead they can turn their heads up to about 270°'),
  rid('Kapalı bir odada 1 lamba, dışarıda 3 düğme var.<br>Odaya yalnızca bir kez girebilirsin.<br>Lambayı hangi düğme yakıyor?','A closed room has one bulb; outside are 3 switches. You may enter only once. Which switch lights the bulb?','1’i 5 dk aç, kapat; 2’yi aç, gir.','Yanıyorsa 2 · sıcaksa 1 · soğuksa 3 — Lit: 2 · warm: 1 · cold: 3',hint='İpucu: ampul ısınır · Hint: bulbs get warm',sec=24,d=42,c1='#2e2a1e',c2='#070605'),
  g('hzdrift',d=40),
  g('hzfact',d=30,big='↕',tr='Gözünün arkasına düşen görüntü baş aşağıdır — beynin onu çevirir',en='The image on the back of your eye is upside down — your brain flips it',src='Merceği olan her göz böyle çalışır · Every eye with a lens works this way',c1='#1c2236',c2='#04050a'),
  photo('kumbet','Giresun','Kümbet Yaylası — yeşil çayırlar ve dağ havası','Kümbet plateau — green meadows and mountain air','Yaz aylarında yayla şenlikleriyle bilinir','Known for its summer highland festivals'),
]),
S(17,18,'Zaman ve Sabır · Time & Patience',[
  g('hzsteps',d=56,lb='Düşünce Deneyi · Thought Experiment',q='Aşil ile Kaplumbağa',e='Achilles and the Tortoise',c1='#2c2418',c2='#070504',gap=5.5,
    steps=[['Aşil kaplumbağaya 100 m avans veriyor','Achilles gives the tortoise a 100 m head start',''],['Aşil 100 m koşunca kaplumbağa 10 m ilerlemiş','When he runs 100 m, it has gone 10 m',''],['10 m koşunca kaplumbağa 1 m önde','He runs 10 m — it is 1 m ahead',''],['Sonsuz adım… hiç yakalayamaz mı?','Infinite steps… can he never catch up?','?'],['100 + 10 + 1 + 0,1 + …','100 + 10 + 1 + 0.1 + …','= 111,1… m']],
    fin='Zenon (MÖ 5. yy): sonsuz sayıda adım, sonlu bir mesafeye sığabilir',fine='Zeno (5th c. BC): infinitely many steps can fit into a finite distance'),
  photo('vazelon','Maçka, Trabzon','Vazelon Manastırı — ormanda kayaya yaslanmış','Vazelon Monastery — leaning against a cliff in the forest','Rivayete göre kökleri MS 3. yüzyıla kadar uzanır','Legend says its roots go back to the 3rd century AD'),
  q('Sabır,|ferahlığın anahtarıdır','Patience is the key to relief','sea'),
  g('hzmaze',d=58),
  rid('Hep önünde durur<br>ama onu asla göremezsin.<br>Nedir?','It is always in front of you, but you can never see it. What is it?','Gelecek!','The future.',sec=16,c1='#1d2836',c2='#05070a'),
  photo('teadrop','Rize','Yağmur damlası tutmuş çay yaprakları','Tea leaves holding raindrops','Çay bitkisinin iyi bakılırsa onlarca yıl verim verdiği anlatılır','A well-tended tea bush is said to keep giving leaves for decades',fit='contain'),
]),
S(18,19,'Akşam Oyunları · Evening Games',[
  g('hzchaos',d=55),
  g('hzsteps',d=58,lb='Akıllı Düşünce · Clever Thinking',q='Mahkûm İkilemi',e='The Prisoner’s Dilemma',c1='#2a1e24',c2='#070506',gap=5.5,
    steps=[['İki şüpheli, ayrı odalarda sorgulanıyor','Two suspects, questioned in separate rooms',''],['İkisi de susarsa','Both stay silent','1’er yıl'],['Biri öter, diğeri susarsa','One talks, one stays silent','0 / 10 yıl'],['İkisi de öterse','Both talk','5’er yıl'],['Bencil “mantık”: ikisi de öter','Selfish “logic”: both talk','5 + 5']],
    fin='Birbirine güvenen ikisi kazanırdı — oyun teorisi, 1950',fine='If they had trusted each other, both would have won — game theory, 1950'),
  photo('reef','Avustralya · Australia','Büyük Set Resifi’nde bir mercan kümesi','A coral outcrop on the Great Barrier Reef','Uzaydan görülebilen en büyük canlı yapı olarak anılır','It is described as the largest living structure visible from space'),
  rid('Şehirlerim var ama evim yok,<br>ormanlarım var ama ağacım yok,<br>denizlerim var ama suyum yok.<br>Ben neyim?','I have cities but no houses, forests but no trees, seas but no water. What am I?','Harita!','A map.',sec=18,c1='#1a2c30',c2='#040809'),
  g('hzfact',d=32,big='2.500 › 2.000',tr='Kleopatra, Büyük Piramit’e göre Ay’a ayak basılmasına daha yakın bir zamanda yaşadı',en='Cleopatra lived closer in time to the Moon landing than to the building of the Great Pyramid',src='Piramitten ~2.500 yıl sonra, Ay’a inişten ~2.000 yıl önce · ~2,500 years after the pyramid, ~2,000 years before the Moon landing',c1='#2c2618',c2='#070604'),
]),
S(19,20,'Derinlere · Into the Deep',[
  g('hzsteps',d=60,lb='Ölçek Yolculuğu · Scale Journey',q='Denizin dibine doğru dalıyoruz…',e='Diving down towards the sea floor…',c1='#0a2a3a',c2='#010509',gap=5,
    steps=[['Kırmızı renk ilk kaybolur','Red is the first colour to vanish','10 m'],['Güneş ışığı burada biter','Sunlight ends here','200 m'],['Zifiri karanlık; ışığını kendi yapan canlılar','Pitch dark; creatures make their own light','1.000 m'],['Karadeniz’in en derin yeri','The deepest point of the Black Sea','≈2.200 m'],['Titanik’in enkazı','The wreck of the Titanic','≈3.800 m'],['Mariana Çukuru — Challenger Derinliği','The Mariana Trench — Challenger Deep','≈10.900 m']],
    fin='Everest’i oraya koysan, zirvesi 2 km’den fazla su altında kalırdı',fine='Put Everest there and its summit would still be over 2 km under water'),
  g('hzfact',d=32,big='%90',tr='Karadeniz’in sularının yaklaşık %90’ı oksijensizdir',en='About 90% of the Black Sea’s water has no oxygen',src='Bu yüzden derinlerdeki eski batıklar şaşırtıcı derecede sağlam kalır · That’s why ancient shipwrecks in its depths stay remarkably intact',c1='#0b2430',c2='#020609'),
  rid('Bir geminin merdiveni suya sarkıyor.<br>Su her saat 10 cm yükseliyor.<br>3 saat sonra kaç basamak daha su altında?','A ship’s ladder hangs into the sea. The water rises 10 cm an hour. After 3 hours, how many more rungs are under water?','Hiçbiri!','None — the ship rises with the water.',hint='Gemi ne yapıyor? · What does the ship do?',sec=20,c1='#12283a',c2='#03060a'),
  photo('otters','Su samurları · Sea otters','El ele uyuyan su samurları','Sea otters sleeping hand in hand','Uyurken akıntıya kapılmamak için birbirlerine tutundukları anlatılır','They are said to hold on to each other so they don’t drift apart while sleeping'),
  g('hzpwave',d=62),
]),
S(20,21,'Gökyüzü · The Sky',[
  photo('jupiter','Hubble, 2014','Jüpiter ve Büyük Kırmızı Leke','Jupiter and its Great Red Spot','Leke, Dünya’dan büyük bir fırtına; yüzyıllardır esiyor ama küçülüyor','The spot is a storm bigger than Earth — raging for centuries, but shrinking',fit='contain'),
  g('hzfact',d=30,big='243 › 225',tr='Venüs’te bir gün, bir yıldan uzundur',en='On Venus, a day is longer than a year',src='Kendi çevresinde 243, Güneş çevresinde 225 Dünya gününde döner · It spins once in 243 Earth days but orbits the Sun in 225',c1='#2c2016',c2='#070504'),
  g('hzsteps',d=56,lb='Düşünce Deneyi · Thought Experiment',q='Evren bu kadar büyükse… herkes nerede?',e='If the universe is so big… where is everybody?',bg='stars',c1='#0c1426',c2='#020308',gap=5.5,
    steps=[['Samanyolu’nda yüz milyarlarca yıldız','Hundreds of billions of stars in the Milky Way',''],['Çoğunun çevresinde gezegen var','Most of them have planets',''],['Bazıları milyarlarca yıl önce oluştu','Some formed billions of years ago',''],['Yine de kimseden tek bir sinyal yok','Yet not a single signal from anyone','?']],
    fin='Enrico Fermi, 1950: “Herkes nerede?” — Fermi Paradoksu',fine='Enrico Fermi, 1950: “Where is everybody?” — the Fermi Paradox'),
  photo('andromeda','Andromeda · M31','Andromeda Galaksisi — çıplak gözle görülebilen en uzak şeylerden biri','The Andromeda Galaxy — one of the most distant things visible to the naked eye','Samanyolu ile yaklaşık 4,5 milyar yıl sonra birleşmesi bekleniyor','It is expected to merge with the Milky Way in about 4.5 billion years',fit='contain'),
  rid('Ne kadar çok olursa,<br>o kadar az görürsün.<br>Nedir?','The more of it there is, the less you see. What is it?','Karanlık!','Darkness.',sec=16,c1='#141a2c',c2='#030407'),
]),
S(21,22,'Sessiz Merak · Quiet Wonder',[
  q('Dinle, bu ney nasıl şikâyet ediyor;|ayrılıkları nasıl anlatıyor','Listen to the reed, how it tells its tale, complaining of separations','night',d=48,fs=90),
  g('hzsteps',d=56,lb='Düşünce Deneyi · Thought Experiment',q='Mary’nin Odası',e='Mary’s Room',c1='#1c1c2a',c2='#040408',gap=6,
    steps=[['Mary renkler hakkında her şeyi bilen bir bilim insanı','Mary is a scientist who knows everything about colour',''],['Ama hayatı boyunca siyah-beyaz bir odada yaşadı','But she has lived all her life in a black-and-white room',''],['Bir gün dışarı çıkıp ilk kez kırmızı bir gül görüyor','One day she steps out and sees a red rose for the first time',''],['Yeni bir şey öğrendi mi?','Did she learn something new?','?']],
    fin='Frank Jackson, 1982: bilmek ile yaşamak aynı şey mi?',fine='Frank Jackson, 1982: is knowing the same as experiencing?'),
  photo('karagol','Artvin','Karagöl, Şavşat — ladin ormanının aynası','Karagöl, Şavşat — a mirror for the spruce forest','Durgun günlerde göl, ormanı neredeyse kusursuz yansıtır','On still days the lake reflects the forest almost perfectly'),
  rid('Ona hiç dokunmadan<br>kırabileceğin şey nedir?','What can you break without ever touching it?','Söz!','A promise.',sec=15,c1='#1e1a2a',c2='#050407'),
  g('hzfact',d=30,big='1096 · 1325',tr='Oxford Üniversitesi, Aztek başkenti Tenochtitlan’dan daha eskidir',en='Oxford University is older than the Aztec capital Tenochtitlan',src='Oxford’da eğitim 1096’ya, Tenochtitlan 1325’e uzanır · Teaching at Oxford dates to 1096; Tenochtitlan was founded in 1325',c1='#1a2030',c2='#040508'),
]),
S(22,23,'Uykudan Önce · Before Sleep',[
  q('Sevgiyle|acılar tatlılaşır','Through love, bitter things become sweet','night',d=46),
  g('hzsteps',d=58,lb='Ölçek Yolculuğu · Scale Journey — sakin · calm',q='Gece gökyüzünde gördüğün ışık ne kadar yaşlı?',e='How old is the light you see in the night sky?',bg='stars',c1='#0a1020',c2='#010206',gap=6,
    steps=[['Ay','The Moon','≈1,3 saniye'],['Jüpiter','Jupiter','≈35–50 dakika'],['Sirius (Akyıldız)','Sirius','≈8,6 yıl'],['Vega','Vega','≈25 yıl'],['Ülker yıldız kümesi','The Pleiades','≈440 yıl']],
    fin='Gökyüzüne bakmak, geçmişe bakmaktır',fine='Looking at the sky is looking into the past'),
  photo('pokut','Rize','Pokut Yaylası’nda ay ışığında çadırlar','Tents under moonlight on the Pokut plateau','Şehir ışıklarından uzakta yıldızlar çok daha parlak görünür','Far from city lights, the stars shine much brighter',d=40),
  g('hzfact',d=32,big='Zzz',tr='Sen uyurken beynin günün anılarını düzenler ve kaydeder',en='While you sleep, your brain sorts and stores the day’s memories',src='İyi uyku, iyi hafıza demektir · Good sleep means good memory',c1='#141a2e',c2='#030408'),
  rid('Gece gelir, gündüz kaybolur;<br>saymakla bitmez.<br>Nedir?','They come at night and vanish by day, and you can never count them all. What are they?','Yıldızlar!','The stars.',sec=16,c1='#10162a',c2='#020307'),
]),
S(23,26,'Gece Işıkları · Night Lights (sakin · calm)',[
  g('hzaurora',d=70),
  photo('dino','Biyolüminesans · Bioluminescence','Gece dalgalarında mavi ışık','Blue light in the night waves','Dalga sarstığında milyonlarca minik plankton ışık saçar','Millions of tiny plankton glow when the waves stir them',d=42),
  g('hzfact',d=34,big='3,8 cm',tr='Ay her yıl Dünya’dan yaklaşık 3,8 cm uzaklaşıyor',en='The Moon drifts about 3.8 cm farther from Earth every year',src='Tırnaklarının uzama hızı kadar · About as fast as your fingernails grow',c1='#0e1424',c2='#020306'),
  g('hzsteps',d=50,lb='Küçük Alışkanlık · Tiny Habit',q='Gözlerini kapatmadan önce düşün…',e='Before you close your eyes, think of…',bg='stars',c1='#0b1120',c2='#010205',gap=7,
    steps=[['Bugün seni gülümseten bir an','One moment that made you smile today',''],['Bugün öğrendiğin yeni bir şey','One new thing you learned today',''],['Yarın için küçük bir heves','One small thing to look forward to tomorrow','']],
    fin='İyi geceler',fine='Good night'),
  g('hzfact',d=32,big='20 sa',tr='Koalalar günde 20 saate kadar uyuyabilir',en='Koalas can sleep up to 20 hours a day',src='Okaliptüs yaprağı çok az enerji verir — o yüzden bol bol dinlenirler · Eucalyptus leaves give very little energy, so they rest a lot',c1='#16201c',c2='#030504'),
]),
]
sets=[s for s in sets if int(s['id'][-2:])<UPTO]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-10.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),s['name'])
