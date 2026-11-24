# Rebuilds 14:00–21:00 of days/2026-11-24.json (rev 80). M asked for new things and for everything to display right.
# New photos: m/h80-*.jpg (credits-2026-11-24e.json). New scene: hzpenrose in hourly.js v80.
# 21:00 volcanoes, 22:00 Whistler and 23:00 whales are kept from days/build_2026-11-24.py (rendered clean, not yet seen).
import json, os
DATE='2026-11-24'; REV=80
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-24e.json')))
FIX={'MareikeHeuer':'Mareike Heuer (WMDE)','Jim Peaco':'Jim Peaco, NPS','Luca Galuzzi':'Luca Galuzzi','Aleksandr Zykov':'Aleksandr Zykov',
     'Jeremy Reding':'Jeremy Reding','BriYYZ':'BriYYZ','S. Rae':'S. Rae','Pierre Blaché':'Pierre Blaché','Stephane D':'Stéphane D’Alu'}
def artist(k):
    a=C[k].get('artist','')
    for f,t in FIX.items():
        if a.startswith(f): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace('CC0','CC0 · kamu malı · public domain')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=44,pos=None,lb=None):
    assert k in C, k
    it=dict(k='hzphoto',d=d,f='m/h80-%s.jpg'%k,lb=lb or (REAL+' · '+tag),tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it
def villa(k,where,tr,en,fact,facte,fit=None,d=46,pos=None):
    return photo(k,'',tr,en,fact,facte,fit=fit,d=d,pos=pos,lb='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where)
def fact(big,tr,en,src,c1,c2,d=30): return dict(k='hzfact',d=d,big=big,tr=tr,en=en,src=src,c1=c1,c2=c2)
def rid(qq,qe,a,ae,hint=None,sec=18,d=34,c1=None,c2=None):
    it=dict(k='hzriddle',d=d,q=qq,qe=qe,a=a,ae=ae,sec=sec)
    if hint: it['hint']=hint
    if c1: it.update(c1=c1,c2=c2)
    return it
def q(tr,en,pal,d=44,lb=None,by=None):
    it=dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
    if lb: it.update(lb=lb,by=by)
    return it
def steps(lb,qq,e,st,fin,fine,c1,c2,gap=8,d=56): return dict(k='hzsteps',d=d,lb=lb,q=qq,e=e,c1=c1,c2=c2,gap=gap,steps=st,fin=fin,fine=fine)
def S(h1,h2,name,items): return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':'%sT%02d:00'%(DATE,h1),'until':'%sT%02d:00'%(DATE,h2)},items=items)

new=[
S(14,15,'Dünyanın Renkli Toprakları · Earth in Colour',[
 photo('vinicunca','Vinicunca, Peru','Vinicunca, “Gökkuşağı Dağı”: yamaçta çizgi çizgi mineral renkleri','Vinicunca, the “Rainbow Mountain”: stripes of mineral colour down the slopes',
  'Kırmızı demir oksitten, sarı kükürtlü kayaçlardan, yeşil kildeki minerallerden gelir; dağ 5.000 metrenin üzerinde','The red comes from iron oxide, the yellow from sulphur-bearing rock, the green from minerals in clay — over 5,000 m up',d=46),
 photo('prismatic','Grand Prismatic, Yellowstone, ABD · USA','Grand Prismatic Kaynağı: gökyüzünden bakınca dev bir göz','Grand Prismatic Spring: a giant eye when seen from the sky',
  'Ortası mavi, çünkü orada su bakterilere bile fazla sıcak; kenarlardaki turuncu halkalar sıcağı seven mikrop kolonileri','The centre is blue because the water there is too hot even for bacteria — the orange rings are colonies of heat-loving microbes',d=46),
 photo('dallol','Dallol, Etiyopya · Ethiopia','Dallol: tuz, kükürt ve demirin boyadığı başka bir gezegen gibi','Dallol: painted by salt, sulphur and iron like another planet',
  'Deniz seviyesinin yaklaşık 125 metre altında; yeryüzünde yıllık ortalama sıcaklığı en yüksek yerlerden biri','About 125 m below sea level — one of the places on Earth with the highest average yearly temperature',d=44),
 photo('canocristales','Caño Cristales, Kolombiya · Colombia','Caño Cristales: “beş renkli nehir”','Caño Cristales: the “river of five colours”',
  'Kırmızı renk, suyun içinde yaşayan bir bitkiden (Macarenia clavigera) gelir; en canlı hâli haziran ile kasım arası','The red comes from a plant living in the water (Macarenia clavigera) — brightest between June and November',d=44),
 photo('lagunacolorada','Laguna Colorada, Bolivya · Bolivia','Laguna Colorada: kırmızı gölde And flamingoları','Laguna Colorada: Andean flamingos on a red lake',
  'Göl yaklaşık 4.280 metrede; rengini sudaki kırmızı alglerden ve tortulardan alır','The lake lies at about 4,280 m and takes its colour from red algae and sediment in the water',d=44),
 rid('Gökkuşağında|kaç renk vardır?','How many colours are in a rainbow?','Sayısız! Renkler kesintisiz akar; Newton müzikteki yedi nota gibi olsun diye yedi saydı','Countless! The colours flow without a break — Newton counted seven to match the seven notes of music',sec=18,c1='#2a1e2c',c2='#08060a'),
]),
S(15,16,'Kuşların Mücevherleri · Feathered Jewels',[
 photo('kingfisher','Yalıçapkını · Common kingfisher','Yalıçapkını: suya dalmadan önce bir an duran mavi bir kıvılcım','A kingfisher: a blue spark pausing for a moment before the dive',
  'Türkiye’nin dere ve göl kıyılarında da yaşar; suya dalarken gözünü saydam bir üçüncü göz kapağıyla korur','It lives along Turkey’s streams and lakes too — when it dives it shields its eyes with a clear third eyelid',d=44),
 photo('mandarin','Mandarin ördeği · Mandarin duck (erkek · male)','Mandarin ördeği: turuncu “yelkenleri” olan bir erkek','A male mandarin duck with his orange “sails”',
  'Doğu Asya’da bir çift mandarin ördeği, sadık sevginin simgesi olarak düğün hediyelerinde resmedilir','In East Asia a pair of mandarin ducks is a symbol of faithful love, painted on wedding gifts',d=42),
 photo('roller','Leylak göğüslü gök kuzgunu · Lilac-breasted roller','Leylak göğüslü gök kuzgunu: neredeyse bütün gökkuşağı tek bir kuşta','A lilac-breasted roller: almost a whole rainbow on one bird',
  'İngilizce adı (roller), kur yaparken havada takla atarak dalmasından gelir','Its English name comes from the rolling, tumbling dives it makes in the air while courting',d=42),
 photo('quetzal','Ketzal · Resplendent quetzal (erkek · male)','Ketzal: kuyruğu gövdesinden uzun yeşil bir efsane','A quetzal: a green legend with a tail longer than its body',
  'Guatemala’nın ulusal kuşu; ülkenin parasının adı da “quetzal”','Guatemala’s national bird — the country’s money is called the quetzal too',d=42),
 photo('beeeater','Arı kuşu · European bee-eater','İki arı kuşu yan yana: Türkiye’nin yaz konukları','Two bee-eaters side by side: Turkey’s summer guests',
  'Baharda Afrika’dan gelirler; kumlu yamaçlara metrelerce tünel kazarak yuva yaparlar','They arrive from Africa in spring and nest in tunnels dug deep into sandy banks',d=42),
 photo('puffin','Deniz papağanı · Atlantic puffin','Deniz papağanı: renkli gagasıyla kayalıkların palyaçosu','A puffin: the clown of the sea cliffs with its colourful bill',
  'Gagasında tek seferde ondan fazla küçük balığı yan yana dizerek taşıyabilir','It can carry more than ten small fish at once, lined up crosswise in its bill',d=42,pos='50% 35%'),
 fact('Mavi','Kuşların çoğunda mavi bir boya yoktur: mavi, tüyün içindeki minicik yapıların ışığı saçmasından doğar. Mavi bir tüyü ezersen grileşir','Most birds have no blue pigment at all: the blue is made by tiny structures inside the feather scattering light. Crush a blue feather and it turns grey','Yapısal renk · Structural colour','#14263a','#050a10'),
]),
S(16,17,'Sonsuz Desenler: Selçuklu Yıldızları ve Penrose · Endless Patterns: Seljuk Stars & Penrose',[
 dict(k='hzpenrose',d=72),
 photo('divrigi','Divriği Ulu Camii · Great Mosque of Divriği, Sivas','Divriği Ulu Camii’nin taş kapısında, taşın dantel gibi oyulduğu desenler','Patterns carved like lace into the stone gateway of the Great Mosque of Divriği',
  'Cami ve darüşşifa 1228–29’da yapıldı; 1985’te UNESCO Dünya Mirası listesine girdi','The mosque and hospital were built in 1228–29 and joined the UNESCO World Heritage list in 1985',d=46),
 photo('karatay2','Karatay Medresesi · Karatay Madrasa, Konya','Karatay Medresesi’nin kubbesi: firuze ve siyah çinilerden örülmüş yıldızlar','The dome of the Karatay Madrasa: stars woven from turquoise and black tiles',
  '1251’de yapıldı; kubbenin tepesindeki açıklıktan gökyüzü görünür, altında bir havuz vardır. Bugün çini eserleri müzesi','Built in 1251 — the opening at the top of the dome shows the sky above a pool. Today it is a museum of tiles',d=46),
 photo('gokmedrese','Gök Medrese · Sivas','Sivas Gök Medrese’nin çifte minareli taç kapısı','The twin-minaret portal of the Gök Medrese in Sivas',
  '1271’de yapıldı; adını minarelerini süsleyen mavi (gök) çinilerden alır','Built in 1271 — it takes its name from the blue (“gök”) tiles on its minarets',d=44,pos='50% 40%'),
 fact('1453','İsfahan’daki Darb-ı İmam türbesinin (1453) çinilerinde, 2007’de fizikçiler Penrose döşemesine çok yakın, neredeyse hiç tekrarlamayan bir desen buldu: Batı’dan 500 yıl önce','In 2007 physicists found, in the tiles of the Darb-i Imam shrine in Isfahan (1453), a pattern very close to Penrose tiling that almost never repeats — 500 years before the West','Peter Lu & Paul Steinhardt, Science, 2007','#14282a','#050b0c'),
 rid('Eşkenar üçgen, kare ve altıgen bir zemini tek başına boşluksuz kaplar.|Peki düzgün beşgen neden kaplayamaz?','Triangles, squares and hexagons can each tile a floor with no gaps. Why can’t a regular pentagon?','İç açısı 108°: 360° bunu tam bölmez, köşede hep bir boşluk kalır','Its angle is 108° — that doesn’t divide 360° evenly, so a gap is always left at the corner',sec=22,d=38,c1='#1e2a30',c2='#06090c'),
]),
S(17,18,'Deniz Fenerleri: Kıyının Bekçileri · Lighthouses: Keepers of the Coast',[
 photo('kizkulesi','Kız Kulesi · Maiden’s Tower, İstanbul','Gece Kız Kulesi: Boğaz’ın ağzında küçük bir adada ışık','The Maiden’s Tower at night: a light on a tiny island at the mouth of the Bosphorus',
  'Uzun yıllar deniz feneri olarak da hizmet verdi; restorasyondan sonra 2023’te yeniden ziyarete açıldı','For many years it also served as a lighthouse — it reopened to visitors in 2023 after restoration',d=46),
 photo('peggys','Peggy’s Cove, Kanada · Canada','Peggy’s Cove: granit kayaların üstünde beyaz ve kırmızı bir fener','Peggy’s Cove: a white and red lighthouse on granite rocks',
  'Kanada’nın en çok fotoğraflanan fenerlerinden biri; 1915’ten beri yerinde','One of the most photographed lighthouses in Canada — it has stood here since 1915',d=44),
 photo('portlandhead','Portland Head, Maine, ABD · USA','Portland Head Feneri: Atlantik kıyısında bir sonbahar günü','Portland Head Light: an autumn day on the Atlantic coast',
  'İlk kez 1791’de yakıldı; Maine’in en eski feneri','First lit in 1791 — the oldest lighthouse in Maine',d=44),
 photo('neist','Neist Point, Skye, İskoçya · Scotland','Neist Point: Skye Adası’nın en batı ucunda bir fener','Neist Point: a lighthouse at the far western tip of the Isle of Skye',
  '1909’dan beri yanıyor; burada akşamüstü balinalar ve yunuslar görülebilir','Lit since 1909 — whales and dolphins can sometimes be seen from here in the evening',d=44),
 photo('rubjerg','Rubjerg Knude, Danimarka · Denmark','Rubjerg Knude: kumulların yutmaya çalıştığı fener','Rubjerg Knude: the lighthouse the dunes tried to swallow',
  'Denize düşmesin diye 2019’da raylar üstünde yaklaşık 70 metre içeri taşındı','In 2019 it was moved about 70 m inland on rails so it would not fall into the sea',d=44),
 fact('Pharos','İskenderiye Feneri Antik Dünya’nın Yedi Harikası’ndan biriydi; tahminen 100 metreyi aşıyordu. Fransızca “phare” ve İtalyanca “faro” adını bu adadan, Pharos’tan alır','The Lighthouse of Alexandria was one of the Seven Wonders of the Ancient World, probably over 100 m tall. The French “phare” and Italian “faro” are named after its island, Pharos','İÖ 3. yüzyıl · 3rd century BC','#18222e','#05080c'),
 rid('Gece gündüz bekler, hiç uyumaz;|gözü var ama görmez, yine de yol gösterir. Nedir?','It keeps watch day and night and never sleeps; it has an eye that cannot see, yet it shows the way. What is it?','Deniz feneri','A lighthouse',sec=16,c1='#1a2632',c2='#05080c'),
]),
S(18,19,'Akşam Müziği: Sesin Mimarisi · Evening Music: The Architecture of Sound',[
 photo('aspendos','Aspendos, Antalya','Aspendos Antik Tiyatrosu: kemerlerin arasından 1.800 yıllık sahne','The ancient theatre of Aspendos: an 1,800-year-old stage seen through its arches',
  'MS 2. yüzyılda yapıldı; dünyanın en iyi korunmuş Roma tiyatrolarından biri ve bugün hâlâ opera ve bale festivaline ev sahipliği yapıyor','Built in the 2nd century AD — one of the best-preserved Roman theatres in the world, and it still hosts an opera and ballet festival',d=46),
 photo('epidaurus','Epidavros, Yunanistan · Greece','Epidavros: en üst sıradan bakınca sahne','Epidaurus: the stage seen from the top row',
  'İÖ 4. yüzyıldan; sahnede yakılan bir kibritin sesinin en üst sıradan duyulduğu söylenir. Basamaklar alçak sesleri süzüp sesi berraklaştırır','From the 4th century BC — they say a match struck on stage can be heard from the top row. The stepped seats filter out low noise and keep voices clear',d=46),
 photo('sydneyopera','Sidney · Sydney, Avustralya · Australia','Gece Sidney Opera Binası: limanın üstünde açılmış beyaz yelkenler','The Sydney Opera House at night: white sails opened over the harbour',
  'Jørn Utzon tasarladı, 1973’te açıldı. Kabukların hepsi aynı kürenin parçalarından kesildi; böylece inşa edilebildi','Designed by Jørn Utzon, opened in 1973. Every shell was cut from pieces of the same sphere — that is what made it buildable',d=46),
 photo('elbphil','Elbphilharmonie, Hamburg','Elbphilharmonie: eski bir liman deposunun üstüne konmuş cam bir dalga','The Elbphilharmonie: a glass wave set on top of an old harbour warehouse',
  '2017’de açıldı; büyük salonun duvarlarındaki yaklaşık 10.000 alçı panelin her biri, sesi dağıtmak için bilgisayarla ayrı ayrı biçimlendirildi','Opened in 2017 — each of the roughly 10,000 panels lining the great hall was shaped individually by computer to scatter sound',d=44),
 photo('oslo','Oslo Opera Binası · Oslo Opera House','Oslo Opera Binası: üstünde yürüyebildiğin, fiyorda inen beyaz bir çatı','The Oslo Opera House: a white roof you can walk on, sloping down into the fjord',
  '2008’de açıldı; çatısı İtalyan Carrara mermeriyle kaplı','Opened in 2008 — its roof is clad in Italian Carrara marble',d=44),
 fact('≈ 2 sn · s','İyi bir senfoni salonunda son nota yaklaşık iki saniye boyunca havada asılı kalır: sesin yavaşça sönmesine yankılanma süresi denir','In a good symphony hall the last note hangs in the air for about two seconds — the slow fading of sound is called reverberation time','Akustik · Acoustics','#241a14','#090604'),
 q('Sözün tükendiği yerde müzik konuşur','Where words fail, music speaks','night',d=40,lb='Söz · Words',by='Hans Christian Andersen'),
]),
S(19,20,'Villa Fikirleri: Taş ve Çakıl Bahçeleri · Villa Ideas: Gardens of Stone & Pebble',[
 villa('ryoanji','Ryōan-ji, Kyoto','Ryōan-ji: tırmıklanmış beyaz çakıl ve on beş taş','Ryōan-ji: raked white gravel and fifteen stones',
  'Bu tür bahçelere karesansui, “kuru manzara” denir: tek damla su kullanmadan suyu anlatır','Gardens like this are called karesansui, “dry landscape” — they tell of water without using a single drop'),
 villa('ginkakuji','Ginkaku-ji, Kyoto','Ginkaku-ji: kumdan bir koni, “Ay’ı seyretme tepesi”','Ginkaku-ji: a cone of sand, the “moon-viewing platform”',
  'Kum düzenli olarak elle yeniden biçimlendirilir; ay ışığında parlayıp bahçeyi aydınlattığı söylenir','The sand is reshaped by hand again and again — they say it glows in the moonlight and lights the garden',pos='50% 50%'),
 villa('kenrokuen','Kenroku-en, Kanazawa','Kenroku-en: iki ayaklı taş fener ve gölün üstünde taş bir köprü','Kenroku-en: a two-legged stone lantern and a stone bridge over the pond',
  'Japonya’nın en güzel üç bahçesinden biri sayılır; fenerin ayakları bir telli çalgının (koto) köprüsüne benzer','It is counted among Japan’s three finest gardens — the lantern’s legs look like the bridge of a koto, a stringed instrument'),
 villa('portlandjg','Portland Japon Bahçesi · Portland Japanese Garden','Kırmızı bir Japon akçaağacı, taşların ve yosunun üstünde','A red Japanese maple above stones and moss',
  'Japon bahçelerinde tek bir akçaağaç, mevsimin değiştiğini gösteren canlı bir saat gibidir','In a Japanese garden a single maple is like a living clock that shows the season turning',pos='50% 40%'),
 steps('Villa Fikri · Villa Idea','Merdiven altındaki çakıl köşesine bir Japon bahçesinden ne alınabilir?','What could the pebble corner under the stairs borrow from a Japanese garden?',[
   ['Tırmıkla çizilmiş birkaç dalga çizgisi: beyaz çakıl suya dönüşür','A few raked wave lines — and white pebbles become water','〰'],
   ['Tek sayıda taş: üç ya da beş, aralarındaki mesafeler eşit olmasın','An odd number of stones — three or five, never evenly spaced',''],
   ['Işık taşa yandan, sıyırarak vursun: sıcak ve alçak bir ışık dokuyu ortaya çıkarır','Let light graze the stone from the side — a warm, low light brings out the texture',''],
   ['Boşluk da tasarımın parçası: Japonlar buna “ma” der','Empty space is part of the design — the Japanese call it “ma”',''],
  ],'Çakıl, taş ve tek bir ağaç: hepsi zaten merdivenin altında','Pebbles, stone and a single tree — all already under the stairs','#1e2420','#070908',d=58),
 rid('Ryōan-ji’de 15 taş var.|Bahçenin neresinden bakarsan bak, kaç tanesini aynı anda görebilirsin?','Ryōan-ji has 15 stones. From anywhere in the garden, how many can you see at once?','En fazla 14: biri hep bir başkasının arkasında saklanır','At most 14 — one always hides behind another',sec=20,d=36,c1='#22281f',c2='#070906'),
]),
S(20,21,'Yerin Altındaki Mücevherler: Kristaller · Jewels Beneath the Earth: Crystals',[
 photo('naica','Naica Mağarası · Cave of the Crystals, Meksika · Mexico','Naica’nın Kristal Mağarası: insanı cüce gösteren dev alçıtaşı kristalleri','The Cave of the Crystals at Naica: giant gypsum crystals that make people look tiny',
  'Yerin yaklaşık 300 metre altında; bazı kristaller 11 metreyi aşar. İçerisi yaklaşık 58 °C ve neredeyse yüzde 100 nemli','About 300 m underground — some crystals are over 11 m long. Inside it is about 58 °C and almost 100% humid',d=48),
 photo('amethyst','Ametist · Amethyst','İkiye ayrılmış bir ametist jeodu: taşın içinde mor bir mağara','An amethyst geode split in two: a purple cave inside a stone',
  'Eski Yunanca “amethystos”, “sarhoş olmayan” demek: bu taşın sarhoşluğu önlediğine inanılırdı','The Greek “amethystos” means “not drunk” — people believed this stone prevented drunkenness',fit='contain',d=44),
 photo('fluorite','Florit · Fluorite, İngiltere · England','Yeşil florit küpleri: kayanın içinde büyümüş camdan zarlar','Green fluorite cubes: glassy dice grown inside the rock',
  '“Floresan” kelimesi bu mineralden gelir: morötesi ışıkta parlar','The word “fluorescence” comes from this mineral — it glows under ultraviolet light',fit='contain',d=44),
 photo('azurite','Azurit · Azurite, ABD · USA','Azurit: lacivertin en derin tonu, kendiliğinden','Azurite: the deepest shade of blue, made by nature alone',
  'Orta Çağ ve Rönesans ressamlarının en önemli mavi boyalarından biriydi; zamanla yeşil malakite dönüşebilir','It was one of the most important blue paints of medieval and Renaissance painters — over time it can turn into green malachite',fit='contain',d=44),
 photo('malachite','Malakit ve atakamit · Malachite & atacamite, Avustralya · Australia','Malakit üzerinde koyu yeşil atakamit kristalleri','Dark green atacamite crystals on malachite',
  'Antik Mısır’da malakit öğütülüp yeşil göz boyası ve resim boyası yapılırdı','In ancient Egypt malachite was ground into green eye paint and painters’ pigment',fit='contain',d=42),
 photo('quartz','Dumanlı kuvars ve amazonit · Smoky quartz & amazonite, Colorado','Dumanlı kuvars ve turkuaz amazonit: dağın içinden çıkan bir ikili','Smoky quartz and turquoise amazonite: a pair from inside a mountain',
  'Kol saatlerindeki minicik kuvars kristali saniyede tam 32.768 kez titreşir; saat bunları sayarak zamanı tutar','The tiny quartz crystal in a wristwatch vibrates exactly 32,768 times a second — the watch keeps time by counting them',fit='contain',d=44),
 rid('Bir elmas ile kurşun kalemin ucu|aynı şeyden yapılmıştır. Nedir?','A diamond and the tip of a pencil are made of the same thing. What is it?','Karbon! Atomlar elmasta sıkı bir kafes, grafitte kayan katmanlar oluşturur','Carbon! In diamond the atoms form a tight lattice, in graphite sliding layers',sec=18,c1='#1c1a2c',c2='#06050a'),
]),
]

want={s['from'][11:13] for s in new}
day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
byh={s['from'][11:13]:s for s in day['sets']}
for s in new: byh[s['from'][11:13]]=s
order=['09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
day['sets']=[byh[h] for h in order]
day['rev']=REV
day['_note']='Hourly sets for the villa TV. 09:00–14:00 and 21:00–02:00 from days/build_2026-11-24.py; 14:00–21:00 rebuilt by days/build_2026-11-24_afternoon.py (rev 80: earth in colour, feathered jewels, Seljuk stars & Penrose + hzpenrose, lighthouses, architecture of sound, gardens of stone & pebble, crystals).'
json.dump(day,open(os.path.join(HERE,'%s.json'%DATE),'w'),ensure_ascii=False,indent=1)
for s in day['sets']:
    hh=s['from'][11:13]
    print(s['id'],s['from'][11:16],len(s['items']),'%ss'%sum(i.get('d',0) for i in s['items']),s['name']+(' *' if hh in want else ''))
