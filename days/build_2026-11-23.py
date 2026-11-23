# (Pattern from build_2026-11-22.py) Builds /workspace/tv-pages/days/2026-11-23.json (hourly sets 09:00-02:00). Monday: Zilkale, Gülbahar Hatun, hamsi, slime mould networks, waterfalls, poetry in wood, Vermeer, comets, Delboeuf & wagon-wheel illusions, prisoner's dilemma tournament, tea & coffee time, Black Sea kemençe & horon, setting the table, wisdom of crowds, an atlas of clouds, Aivazovsky's night seas, around the Pole Star.
import json,os
DATE='2026-11-23'; REV=77; NEXT='2026-11-24'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-23.json')))
FIX={'Feel free to use my photos':'Friedrich Böhringer','Unknown authorUnknown':'bilinmeyen · unknown','Courtesy of NOAA/Institute':'NOAA / IFE / URI','CTIO/NOIRLab':'CTIO / NOIRLab / DOE / NSF / AURA (T.A. Rector, M. Zamani)','Credit: Big Ear':'Big Ear Radio Observatory / NAAPO','Sheba_Also':'Sheba_Also','Emmanuel.boutet':'Emmanuel Boutet (Bohemeria)','User:Zenit':'Zenit','Pavel Kirillov':'Pavel Kirillov','Gide et J. Baudry':'Gide et J. Baudry (1853)','Mike Vecchione':'Mike Vecchione, NOAA','Katsushika Hokusai':'Katsushika Hokusai','Photo by and (C)2007 Derek Ramsey':'Derek Ramsey (düzenleme · edit: Papa Lima Whiskey)','bgv23':'bgv23','Unknown author':'bilinmeyen fotoğrafçı · unknown photographer','NASA/JPL-Caltech/Malin':'NASA / JPL-Caltech / MSSS','Mars Science Laboratory':'NASA / JPL-Caltech / MSSS / Texas A&M Univ.','NASA/Johns Hopkins':'NASA / JHUAPL / SwRI','NASA/JPL-Caltech/SwRI':'NASA / JPL-Caltech / SwRI / MSSS / Gerald Eichstädt / Seán Doran','Harvey Barrison':'Harvey Barrison','Benh LIEU SONG':'Benh LIEU SONG','Nevit Dilmen':'Nevit Dilmen','Audubon, John James':'John James Audubon','Russo Francesco':'Francesco Russo','NASA and the European Space Agency':'NASA / ESA','NASA/JPL/Space Science Institute':'NASA / JPL / Space Science Institute','NASA/JPL/NIMA':'NASA / JPL / NIMA','NASA/JPL-Caltech':'NASA / JPL-Caltech','NASA/Bill Anders':'NASA / Bill Anders','Roy Egloff':'Roy Egloff','CopyrightFreePhotos':'CopyrightFreePhotos','Grand Canyon NPS':'Grand Canyon National Park (NPS)','Clarisse Meyer':'Clarisse Meyer','Bernard DUPONT':'Bernard Dupont','Bob Henricks':'Bob Henricks','Forest Wander':'Forest Wander','Credits to Mourad Ben Abdallah':'Mourad Ben Abdallah','NASA image courtesy of the DSCOVR':'NASA / DSCOVR EPIC','blgrssby from St. Louis':'blgrssby','al-Jazari':'el-Cezerî · al-Jazari (1315 kopyası · copy, The Met)','Ala ad-Din Mansur-Shirazi':'Alaeddin Mansur · Ala ad-Din Mansur-Shirazi (Şehinşahname, 1581)','NOIRLab/NSF/AURA':'NOIRLab / NSF / AURA','卓珺 黄':'Zhuojun Huang','none (Landsat)':'NASA / USGS Landsat','Kritzolina':'Claude Monet (detay · detail; foto · photo: Kritzolina)','Dale Cruse':'Dale Cruse'}
FIX21={'Martin Koitmäe':'Martin Koitmäe','Image: National Aeronautics':'NASA / ESA / CSA / STScI','ESO/Y.Beletsky':'ESO / Y. Beletsky','ESO/B. Tafreshi':'ESO / B. Tafreshi (twanight.org)','NASA/JPL-Caltech/Univ. of Ariz':'NASA / JPL-Caltech / Univ. of Arizona','K.-M. Hansche':'K.-M. Hansche (düzenleme · edit: Arad)','Earth Science and Remote Sensing':'NASA / ISS Expedition 47 (Earth Science and Remote Sensing Unit, JSC)','Unknown author':'bilinmeyen katip · unknown scribe','David Stanley':'David Stanley','daryl_mitchell':'daryl_mitchell','Quentin Lowagie':'Quentin Lowagie / Klow','Rembrandt':'Rembrandt van Rijn','Thomas Allom':'Thomas Allom (1838)','NASA and European Space Agency':'NASA / ESA'}
FIX22={'Didier Descouens':'Joaquín Sorolla (foto · photo: Didier Descouens)','Ángel M. Felicísimo':'Joaquín Sorolla (foto · photo: Ángel M. Felicísimo)','Estec GmbH':'Estec GmbH','USFWSAlaska':'USFWS Alaska','Robert Cahalan':'Robert Cahalan, NASA / GSFC (Landsat 7)','NASA/Goddard/SDO':'NASA / Goddard / SDO AIA','NASA/SDO, AIA':'NASA / SDO / AIA','Barbarossa':'Barbarossa'}
FIX23={'Unknown authorUnknown':'bilinmeyen · unknown','ESA/Rosetta/NAVCAM':'ESA / Rosetta / NAVCAM','E. Kolmhofer':'E. Kolmhofer, H. Raab (Johannes Kepler Gözlemevi · Observatory, Linz)','President (1981-1989':'Beyaz Saray Fotoğraf Ofisi · White House Photographic Office','User:Rachel Dalby':'Rachel Dalby','NASA/W. Liller':'NASA / W. Liller','S. Deiries/ESO':'S. Deiries / ESO','Ximonic':'Ximonic (Simo Räsänen)','Johannes Vermeer':'Johannes Vermeer','Ivan Aivazovsky':'İvan Ayvazovski · Ivan Aivazovsky'}
FIX22={**FIX23,**{a:b for a,b in FIX22.items() if a not in FIX23}}
FIX21={**FIX22,**{a:b for a,b in FIX21.items() if a not in FIX22}}
FIX={**FIX21,**{a:b for a,b in FIX.items() if a not in FIX21}}
def artist(k):
    a=C[k]['artist']
    if not a.strip(): return 'The Metropolitan Museum of Art'
    for f,t in FIX.items():
        if a.startswith(f): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace(' rs','').replace('3.0 at','3.0 AT').replace('3.0 igo','3.0 IGO')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,pos=None):
    if k not in C: print('SKIP missing photo',k); return None
    it=dict(k='hzphoto',d=d,f='m/h23-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it
def villa(k,where,tr,en,fact,facte,fit=None,d=42):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=d)
    if it is None: return None
    it['lb']='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where
    return it
def art(k,tr,en,fact,facte,d=44):
    it=photo(k,'',tr,en,fact,facte,fit='contain',d=d)
    if it is None: return None
    it['lb']='Gerçek Eser · Real Artwork'
    it['cr']='Eser · Artwork: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
    return it
def q(tr,en,pal,d=44,lb=None,by=None):
    it=dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
    if lb: it.update(lb=lb,by=by)
    return it
def rid(qq,qe,a,ae,hint=None,sec=18,d=34,c1=None,c2=None):
    it=dict(k='hzriddle',d=d,q=qq,qe=qe,a=a,ae=ae,sec=sec)
    if hint: it['hint']=hint
    if c1: it.update(c1=c1,c2=c2)
    return it
def fact(big,tr,en,src,c1,c2,d=30): return dict(k='hzfact',d=d,big=big,tr=tr,en=en,src=src,c1=c1,c2=c2)
def steps(lb,qq,e,st,fin,fine,c1,c2,gap=6,d=56,bg=None):
    it=dict(k='hzsteps',d=d,lb=lb,q=qq,e=e,c1=c1,c2=c2,gap=gap,steps=st,fin=fin,fine=fine)
    if bg: it['bg']=bg
    return it
def guess(k,where,qq,qe,a,ae,hint=None,sec=20,d=38):
    it=dict(k='hzguess',d=d,f='m/h23-%s.jpg'%k,lb='Bil Bakalım · Can You Guess? — '+REAL+' · '+where,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr=cr(k))
    if hint: it['hint']=hint
    return it
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=[i for i in items if i])
TE='Düşünce Deneyi · Thought Experiment'; CT='Zekice Düşünce · Clever Thinking'
sets=[
S(9,10,'Pazartesi Sabahı · Monday Morning',[
  photo('zilkale','Zilkale · Çamlıhemşin, Rize','Zilkale: Fırtına Vadisi’nin ormanları arasında, kayalık bir tepenin üstünde bir kale','Zilkale — a castle on a rocky hilltop among the forests of the Fırtına Valley','Yaklaşık 750 metrede, derenin 100 metreyi aşkın yukarısında; adının, vadide yankılanan su sesinden ya da bir çandan geldiği anlatılır','About 750 m up, more than 100 m above the stream — its name (“bell castle”) is said to come from the echoing water or a bell',d=40),
  q('Aradığın şey|seni arıyor','What you are seeking is seeking you','sea',d=44),
  photo('gulbahar','Gülbahar Hatun Camii · Trabzon','Gülbahar Hatun Camii’nin içinden: mermer minber ve sade beyaz duvarlar','Inside the Gülbahar Hatun Mosque — a marble minbar and plain white walls','Yavuz Sultan Selim, annesi Gülbahar Hatun için yaptırdı; 1514’te tamamlandı. Selim gençlik yıllarını Trabzon’da sancakbeyi olarak geçirmişti','Built by Sultan Selim I for his mother Gülbahar Hatun, completed in 1514 — Selim had spent his youth in Trabzon as its governor',fit='contain',d=40),
  photo('hamsi','Kadıköy balık pazarı · Kadıköy fish market, İstanbul','Tezgâhta pırıl pırıl Karadeniz hamsisi','Gleaming Black Sea anchovies (hamsi) on the counter','Hamsi sezonu eylülde açılır; kış soğudukça balık yağlanır ve en lezzetli hâline gelir','The hamsi season opens in September — the colder the winter gets, the richer and tastier the fish become',d=38),
  fact('%90','Karadeniz’in suyunun yaklaşık %90’ı oksijensiz: 150–200 metrenin altında neredeyse hiç canlı yok','About 90% of the Black Sea’s water has no oxygen — below 150–200 m almost nothing lives','Bu yüzden dipte 2.400 yıllık bir Yunan gemisi neredeyse bozulmadan bulundu (2018) · That is why a 2,400-year-old Greek ship was found almost intact on the seabed (2018)','#13242c','#04080a',d=32),
  rid('Ne kadar çok olursa,|o kadar az görürsün. Nedir?','The more of it there is, the less you see. What is it?','Karanlık!','Darkness!',sec=16,c1='#22303a',c2='#06090c'),
]),
S(10,11,'Yaşayan Sanat: Balçık Mantarının Ağları · Living Art: Slime Mould Networks',[
  g('hzphysarum',d=96),
  steps(CT,'Bir balçık mantarı Tokyo’nun demiryolunu nasıl çizdi?','How did a slime mould draw Tokyo’s railway?',
    [['2010’da Japon bilim insanları yulaf tanelerini Tokyo çevresindeki şehirlerin yerlerine dizdi','In 2010 Japanese scientists placed oat flakes where the cities around Tokyo lie','🌾'],['Ortaya, Tokyo’nun yerine, bir parça Physarum koydular','In the middle, where Tokyo is, they put a piece of Physarum',''],['Bir günde mantar bütün tanelere uzandı, sonra gereksiz kolları kendiliğinden geri çekti','Within a day it reached every flake, then pulled back the branches it did not need',''],['Kalan ağ, mühendislerin yıllarca uğraşıp kurduğu demiryolu ağına şaşırtıcı derecede benziyordu','The network that remained looked strikingly like the rail system engineers had spent years designing','']],
    'Sık kullanılan yollar kalınlaşır, boş kalanlar kaybolur: tek kural bu','Busy paths thicken, idle ones disappear — that is the whole rule','#162a2c','#04090a',gap=8,d=58),
  fact('1 hücre','Balçık mantarı aslında tek bir dev hücre: binlerce çekirdeği var ve bir masa büyüklüğüne kadar yayılabilir','A slime mould is really one giant cell — it has thousands of nuclei and can spread as wide as a table','Physarum polycephalum; ne bitki ne hayvan ne de gerçek bir mantar · neither plant, animal nor true fungus','#162a2c','#04090a',d=30),
  rid('Ağzı yok ama konuşur, kulağı yok ama cevap verir.|Nedir?','It has no mouth but speaks, no ears but answers. What is it?','Yankı!','An echo!',sec=18,c1='#22303a',c2='#06090c'),
]),
S(11,12,'Nefes Kesen Yerler: Şelaleler · Breathtaking Places: Waterfalls',[
  photo('plitvice','Plitvice Gölleri, Hırvatistan · Plitvice Lakes, Croatia','Plitvice: ormanın içinden basamak basamak inen göller ve şelaleler','Plitvice — lakes and waterfalls stepping down through the forest','16 göl, sudaki kirecin yavaş yavaş biriktirdiği doğal setlerle birbirinden ayrılır; bu setler hâlâ büyüyor','Sixteen lakes are separated by natural dams of limestone that the water slowly builds — and the dams are still growing',fit='contain',d=40),
  photo('skogafoss','Skógafoss, İzlanda · Iceland','Skógafoss: 60 metreden dökülen bembeyaz bir perde','Skógafoss — a white curtain falling 60 metres','Efsaneye göre bir Viking, hazine sandığını şelalenin arkasındaki mağaraya sakladı; güneşli günlerde önünde çoğu zaman gökkuşağı oluşur','Legend says a Viking hid his treasure chest in a cave behind the falls — on sunny days a rainbow often hangs in front of it',d=40),
  photo('victoria','Victoria Şelalesi, Zimbabve–Zambiya · Victoria Falls, Zimbabwe–Zambia','Victoria Şelalesi: yerel adıyla “Gürleyen Duman”','Victoria Falls — known locally as “the Smoke that Thunders”','Yaklaşık 1,7 kilometre genişliğinde ve 108 metre yüksekliğinde; su tozu kilometrelerce öteden görülebilir','About 1.7 km wide and 108 m high — its spray can be seen from many kilometres away',d=40),
  photo('kirkjufell','Kirkjufell, Snæfellsnes, İzlanda · Iceland','Kirkjufell Dağı ve önündeki küçük şelale','Kirkjufell mountain and the little waterfall in front of it','463 metrelik dağ, şekli yüzünden “kilise dağı” anlamına gelen adını almış; İzlanda’nın en çok fotoğraflanan yerlerinden','The 463 m mountain is named “church mountain” for its shape — one of the most photographed places in Iceland',d=40),
  photo('angel','Angel Şelalesi, Venezuela · Angel Falls, Venezuela','Angel Şelalesi: dünyanın kesintisiz akan en yüksek şelalesi','Angel Falls — the world’s highest uninterrupted waterfall','979 metre: suyun bir kısmı daha yere ulaşmadan sise dönüşür. Adını 1933’te üzerinden uçan pilot Jimmie Angel’dan alır','979 metres — some of the water turns to mist before it reaches the ground. Named after pilot Jimmie Angel, who flew over it in 1933',fit='contain',d=40),
]),
S(12,13,'Ahşabın Şiiri · Poetry in Wood',[
  photo('borgund','Borgund, Norveç · Norway','Borgund ahşap kilisesi: katman katman çatılar ve ejderha başları','Borgund stave church — layer upon layer of roofs, and dragon heads','Yaklaşık 1180’de yapıldı; 800 yılı aşkın süredir ayakta. Kirişler çivi yerine ahşap kamalarla birbirine tutturulmuş','Built around 1180 and standing for more than 800 years — its beams are joined with wooden pegs rather than nails',fit='contain',d=40),
  photo('kizhi','Kiji Adası, Rusya · Kizhi Island, Russia','Kiji’deki Başkalaşım Kilisesi: tamamen ahşaptan 22 kubbe','The Church of the Transfiguration on Kizhi — 22 domes, all of wood','1714’te yapıldı, 37 metre yüksekliğinde. Efsaneye göre ustası tek bir çivi kullanmadı ve bitirince baltasını göle attı','Built in 1714 and 37 m tall — legend says its master builder used not a single nail, then threw his axe into the lake',d=40),
  photo('horyuji','Hōryū-ji, Nara, Japonya · Japan','Hōryū-ji’nin beş katlı ahşap pagodası','The five-storey wooden pagoda of Hōryū-ji','Dünyanın ayakta duran en eski ahşap yapılarından; merkez direk için ağacın 594 yılında kesildiği hesaplandı','Among the oldest standing wooden buildings in the world — the tree for its central pillar was felled in the year 594',d=40),
  photo('shirakawa','Shirakawa-gō, Japonya · Japan','Shirakawa-gō’nun “dua eden eller” gibi dik saman çatılı evleri','The steep thatched “praying hands” houses of Shirakawa-gō','Dik çatılar ağır karı taşır. Bir çatının samanı yaklaşık 30 yılda bir yenilenir ve bunu bütün köy birlikte, bir günde yapar','The steep roofs carry heavy snow — a roof is re-thatched about every 30 years, by the whole village together in a single day',d=40),
  photo('serender2','Arhavi, Artvin','Bir Karadeniz serenderi: ahşap direkler üstünde bir tahıl ambarı','A Black Sea serender — a grain store on wooden stilts','Direklerin tepesindeki geniş ahşap tablalar farelerin yukarı tırmanmasını engeller; altından esen rüzgâr ürünü kuru tutar','The wide wooden discs on top of the posts stop mice from climbing up — and the breeze underneath keeps the harvest dry',fit='contain',d=40),
  photo('safranbolu2','Safranbolu, Karabük','Safranbolu’nun yamaçlara yayılmış ahşap ve kerpiç konakları','The timber-and-adobe mansions of Safranbolu spread over the slopes','1994’ten beri UNESCO Dünya Mirası. Rivayete göre evler birbirinin manzarasını kapatmayacak şekilde dizildi','A UNESCO World Heritage Site since 1994 — the story goes that the houses were placed so that none blocks another’s view',d=40),
]),
S(13,14,'Büyük Ustalardan: Vermeer’in Sessiz Işığı · From the Great Masters: Vermeer’s Quiet Light',[
  art('ver1','Sütçü Kız — Johannes Vermeer, y. 1658','The Milkmaid — Johannes Vermeer, c. 1658','Önlüğündeki mavi, o dönem altından pahalı olan lapis lazuli taşından yapılmış ultramarin boya','The blue of her apron is ultramarine, made from lapis lazuli — then more costly than gold'),
  art('ver2','Delft Manzarası — Johannes Vermeer, y. 1660–61','View of Delft — Johannes Vermeer, c. 1660–61','Yazar Marcel Proust buna “dünyanın en güzel resmi” dedi','The writer Marcel Proust called it “the most beautiful painting in the world”'),
  art('ver3','Küçük Sokak — Johannes Vermeer, y. 1658','The Little Street — Johannes Vermeer, c. 1658','2015’te araştırmacılar eski vergi kayıtlarından bu evlerin Delft’te tam olarak nerede durduğunu buldu','In 2015 researchers used old tax records to find exactly where in Delft these houses stood'),
  art('ver4','Mavili, Mektup Okuyan Kadın — Johannes Vermeer, y. 1663','Woman in Blue Reading a Letter — Johannes Vermeer, c. 1663','Mektupta ne yazdığını hiç bilmiyoruz: Vermeer hikâyeyi değil, o sessiz anı resmetti','We never learn what the letter says — Vermeer painted not the story but the quiet moment'),
  art('ver5','İnci Küpeli Kız — Johannes Vermeer, y. 1665','Girl with a Pearl Earring — Johannes Vermeer, c. 1665','Gerçek bir kişinin portresi değil, hayal edilmiş bir “tip” resmi; Vermeer’e ait bilinen yalnızca 35 kadar tablo var','Not a portrait of a real person but an imagined “type” — only about 35 paintings by Vermeer are known'),
  q('Her sürtünmede incinirsen,|aynan nasıl parlar?','If you are hurt by every rub, how will your mirror ever be polished?','clay',d=42),
]),
S(14,15,'Gökyüzünün Harikaları: Kuyruklu Yıldızlar · Wonders of the Sky: Comets',[
  photo('halebopp','Avusturya, 1997 · Austria, 1997','Hale–Bopp kuyruklu yıldızı: mavi gaz kuyruğu ve beyaz toz kuyruğu','Comet Hale–Bopp — a blue gas tail and a white dust tail','1997’de rekor sayılacak kadar uzun, yaklaşık 18 ay çıplak gözle görüldü; çekirdeği 40–60 km genişliğinde','In 1997 it stayed visible to the naked eye for a record of about 18 months — its nucleus is 40–60 km across',fit='contain',d=40),
  photo('neowise','Temmuz 2020 · July 2020','NEOWISE kuyruklu yıldızı ve onu izleyen bir gözlemci','Comet NEOWISE and a stargazer watching it','Bir daha yaklaşık 6.800 yıl sonra gelecek','It will not be back for roughly 6,800 years',d=40),
  photo('mcnaught','Paranal, Şili, 2007 · Chile, 2007','McNaught kuyruklu yıldızı: güney gökyüzüne yelpaze gibi açılan kuyruk','Comet McNaught — a tail fanning across the southern sky','2007’de son 40 yılın en parlak kuyruklu yıldızıydı; gündüz bile görülebildi','In 2007 it was the brightest comet in 40 years — it could even be seen in daylight',d=40),
  photo('comet67p','Rosetta uzay aracı, 2014 · Rosetta spacecraft, 2014','67P kuyruklu yıldızının yakından görünüşü','Comet 67P seen up close','Yaklaşık 4 km boyunda, oyuncak ördeğe benzeyen bir buz ve toz yığını. Kasım 2014’te Philae robotu yüzeyine indi','About 4 km long, a rubber-duck-shaped heap of ice and dust — in November 2014 the Philae robot landed on it',fit='contain',d=40),
  photo('halley','1986','Halley kuyruklu yıldızının 1986’daki ziyareti','Halley’s Comet on its 1986 visit','Mark Twain, Halley’in geldiği 1835’te doğdu ve bir sonraki gelişinde, 1910’da öldü — tam da öngördüğü gibi','Mark Twain was born when Halley came in 1835 and died on its next visit in 1910 — just as he had predicted',d=40),
  fact('2061','Halley kuyruklu yıldızı bir sonraki sefer 2061 yazında görünecek','Halley’s Comet will be back in the summer of 2061','Yaklaşık her 76 yılda bir döner · It returns about every 76 years','#141c30','#04060c',d=30),
]),
S(15,16,'Göz Oyunları: Boyut ve Hız · Tricks of the Eye: Size & Speed',[
  g('hzdelboeuf',d=52),
  g('hzwagon',d=96),
  fact('24','Sinema filmleri saniyede 24 kare çekilir: hareket ettiğini sandığın şey, art arda gösterilen durgun resimler','Films are shot at 24 frames a second — what looks like motion is a run of still pictures','Araba tekerleklerinin filmlerde geri dönüyor gibi görünmesi bundandır · That is why wagon wheels seem to spin backwards in films','#1c2430','#05070b',d=30),
  rid('Hep yukarı çıkar,|ama asla aşağı inmez. Nedir?','It always goes up but never comes down. What is it?','Yaşımız!','Our age!',sec=16,c1='#22303a',c2='#06090c'),
]),
S(16,17,'Zekice Düşünce: İyilik Kazanır mı? · Clever Thinking: Does Kindness Win?',[
  g('hzaxelrod',d=72),
  steps(CT,'Kısasa Kısas neden bu kadar iyi?','Why is Tit for Tat so good?',
    [['İyi niyetli: ilk kötülüğü asla o yapmaz','Nice — it is never the first to cheat','🤝'],['Karşılık verir: kazıklanırsa hemen bir kez karşılık verir','It hits back — cheated once, it answers once, straight away',''],['Affeder: karşı taraf düzelince o da hemen düzelir','It forgives — as soon as the other side behaves, so does it',''],['Açıktır: ne yapacağı belli olduğu için güven verir','It is clear — because it is predictable, others learn to trust it','']],
    'Axelrod’un özeti: kıskanma, ilk kötülüğü sen yapma, iyiliğe de kötülüğe de karşılık ver, fazla akıllı olmaya çalışma','Axelrod’s summary: don’t be envious, don’t be the first to cheat, return both kindness and cheating, don’t try to be too clever','#1b2430','#05070b',gap=8,d=58),
  photo('cleaner','Kızıldeniz · Red Sea','Bir temizlikçi balık, kendinden çok büyük bir balığın parazitlerini topluyor','A cleaner fish picking parasites off a fish many times its size','Doğada da iş birliği var: büyük balıklar, avcılar bile, “temizlik istasyonlarında” sıraya girer ve temizlikçiyi yemez','Cooperation exists in nature too — big fish, even predators, queue at “cleaning stations” and never eat the cleaner',d=40),
  rid('İki kişi beş oyun satranç oynadı.|Beraberlik yok, ikisi de beşer oyun kazandı. Nasıl?','Two people played five games of chess. No draws, yet each won five games. How?','Birbirleriyle değil, başka rakiplerle oynadılar!','They were not playing each other — they had other opponents!',sec=24,d=36,c1='#22303a',c2='#06090c'),
  fact('1980','Axelrod’un ilk turnuvasına 14 program katıldı; kazanan, aralarındaki en kısa programdı','Axelrod’s first tournament had 14 programs — the winner was the shortest of them all','Kısasa Kısas’ı Anatol Rapoport yazdı; 62 programlı ikinci turnuvayı da kazandı · Tit for Tat was written by Anatol Rapoport and also won the second tournament of 62 programs','#1b2430','#05070b',d=30),
]),
S(17,18,'Çay ve Kahve Saati · Tea & Coffee Time',[
  photo('teaglass','İnce belli bardak · Tulip glass','İnce belli bardakta tavşan kanı bir çay','A “rabbit’s blood” deep-red tea in a tulip glass','İnce bel çayı elde tutmayı kolaylaştırır; geniş ağız ise üstteki çayın daha çabuk soğumasını sağlar','The narrow waist makes the glass easy to hold, while the wide rim lets the top of the tea cool a little faster',d=40),
  photo('semaver','Semaverde çay · Tea from the samovar','Bahçede kaynayan semaverler','Samovars bubbling away in a garden','Semaverin ortasındaki boruda odun ya da kömür yanar; su saatlerce sıcak kalır, çay hiç bitmez','Wood or charcoal burns in the samovar’s central pipe — the water stays hot for hours and the tea never runs out',d=40),
  photo('kahve','Bir fincan kahve · A cup of coffee','Küçük bir fincan, koyu bir kahve','A small cup, a dark coffee','Türk kahvesi kültürü ve geleneği 2013’te UNESCO Somut Olmayan Kültürel Miras listesine alındı','Turkish coffee culture and tradition was added to UNESCO’s Intangible Cultural Heritage list in 2013',d=38),
  photo('minttea','Fas · Morocco','Fas’ta naneli çay: yüksekten dökülür','Moroccan mint tea — always poured from up high','Yüksekten dökmek çayı köpürtür ve biraz soğutur; misafire üç bardak ikram etmek gelenektir','Pouring from a height makes the tea froth and cool a little — offering a guest three glasses is the custom',fit='contain',d=40),
  photo('teaceremony','Japon çay töreni · Japanese tea ceremony','Japon çay töreninde yeşil matcha hazırlanıyor','Green matcha being prepared in a Japanese tea ceremony','Törenin özü “ichigo ichie”: bu buluşma bir kez yaşanır, aynısı bir daha olmaz','The heart of the ceremony is “ichigo ichie” — this meeting happens only once and will never come again',d=40),
  fact('3 kg','Türkiye kişi başına çay tüketiminde dünyada birinci: yılda yaklaşık 3 kilogram kuru çay','Turkey drinks the most tea per person in the world — about 3 kg of dry tea a year','Bu, günde birkaç ince belli bardak demek · That means several tulip glasses a day','#2a1e1c','#0a0605',d=30),
  q('Bir fincan kahvenin|kırk yıl hatırı vardır','A single cup of coffee is remembered for forty years','clay',d=42,lb='Atasözü · Proverb',by='Türk atasözü · Turkish proverb'),
]),
S(18,19,'Akşam Müziği: Karadeniz’in Sesi · Evening Music: The Sound of the Black Sea',[
  photo('kemence','Karadeniz kemençesi · Black Sea kemençe','Karadeniz kemençeleri: dizde tutulan, yayla çalınan üç telli küçük bir saz','Black Sea kemençes — small three-stringed fiddles held on the knee and played with a bow','Kemençeci çoğu zaman iki teli birden çalar; bu yüzden tek bir saz bile kalabalık bir ses çıkarır','The player usually bows two strings at once — so even a single kemençe sounds full',fit='contain',d=40),
  photo('horon3','Sis Dağı Horon Şenliği · Trabzon','Sis Dağı’nda yaylada horon: el ele tutuşmuş uzun bir halka','Horon on the Sis Dağı highland — a long ring of dancers hand in hand','Her yaz Trabzon’un yaylalarında yapılan şenliklerde kemençe çalar, halka büyüdükçe büyür; kemençe hızlandıkça adımlar küçülür, omuzlar titrer','At summer festivals on Trabzon’s highlands the kemençe plays and the ring keeps growing — as the music speeds up, steps shrink and shoulders shimmy',d=40),
  steps('Ritim · Rhythm','Aksak ritim nedir? Birlikte sayalım','What is an “aksak” (limping) rhythm? Let’s count together',
    [['Çoğu batı şarkısı dörde ya da ikiye bölünür: bir-iki, bir-iki','Most Western songs split into fours or twos — one-two, one-two','🎻'],['Horon ise çoğu zaman yediye bölünür: bir-iki, bir-iki, bir-iki-üç','Horon often splits into seven — one-two, one-two, one-two-three',''],['O son “üç” ritmi bir an topallatır; dansa o heyecanlı sıçrayışı veren budur','That last “three” makes the rhythm limp for a moment — and gives the dance its thrilling bounce',''],['Şimdi sen de elinle masaya vur: 2 + 2 + 3','Now tap it on the table yourself: 2 + 2 + 3','']],
    'Kulağına tuhaf gelirse normal: birkaç turdan sonra ayakların kendiliğinden uyar','If it feels odd at first, that’s normal — after a few rounds your feet just follow','#1a2430','#05070b',gap=8,d=56),
  fact('7/16','Horon çoğu zaman 7/16 gibi “aksak” ölçülerle çalınır: çok hızlı yedi vuruşluk bir döngü','Horon is often played in “aksak” meters like 7/16 — a very fast seven-beat cycle','Karadeniz müziği · Black Sea folk music','#1a2430','#05070b',d=30),
  rid('Telleri var ama gitar değil,|yayı var ama ok atmaz. Nedir?','It has strings but it is no guitar; it has a bow but shoots no arrows. What is it?','Kemençe (ya da keman)!','A kemençe (or a violin)!',sec=18,c1='#22303a',c2='#06090c'),
  q('Biz her şeyin|müzik olduğu bir yere düştük','We have fallen into the place where everything is music','night',d=42),
]),
S(19,20,'Villa Fikirleri: Sofra Kurmak · Villa Ideas: Setting the Table',[
  villa('table1','Berlin','Uzun bir masa, beyaz örtü ve sıra sıra mumlar','A long table, white linen and rows of candles','Aynı hizada dizilmiş alçak mumlar, tavandaki tek bir lambadan çok daha sıcak ve samimi bir ışık verir','Low candles in a row give a far warmer, more intimate light than a single lamp overhead'),
  villa('table3','Lyon','Bir Lyon lokantasında özenle kurulmuş sofra: kumaş peçeteler ve sade tabaklar','A carefully set table in a Lyon restaurant — cloth napkins and simple plates','Kumaş peçete ve sade beyaz tabak, misafire “sizin için hazırlandı” duygusunu en az masrafla verir','Cloth napkins and plain white plates tell guests “this was prepared for you” — for very little cost'),
  steps('Villa Fikri · Villa Idea','Misafir sofrası için dört küçük sır','Four small secrets for a guest table',
    [['Masa ortasındaki çiçek ya da mum göz hizasının altında kalsın: herkes birbirini görsün','Keep flowers and candles below eye level so everyone can see each other','🕯'],['Sofrada kokusuz mum: yemeğin kokusu ön planda kalsın','Unscented candles at the table — let the food’s aroma lead',''],['Sıcak beyaz ışık (2700 K) ve kısık lambalar: yüzler de yemekler de güzel görünür','Warm white light (2700 K) and dimmed lamps — faces and food both look their best',''],['Küçük tabak: Delboeuf yanılsamasını hatırla, porsiyon cömert görünür','Smaller plates — remember the Delboeuf illusion: portions look generous','']],
    'Butik otellerin sırrı: pahalı eşya değil, düşünülmüş ayrıntı','The boutique-hotel secret: not expensive things, but thoughtful details','#2a221c','#0a0705',gap=8,d=56),
  rid('Dört ayağı var ama yürüyemez;|sofrayı taşır ama yemek yiyemez. Nedir?','It has four legs but cannot walk; it carries the meal but cannot eat. What is it?','Masa!','A table!',sec=16,c1='#2a221c',c2='#0a0705'),
  q('Misafir umduğunu değil,|bulduğunu yer','A guest eats not what he hoped for, but what he finds','clay',d=42,lb='Atasözü · Proverb',by='Türk atasözü · Turkish proverb'),
]),
S(20,21,'Zekice Düşünce: Kalabalığın Bilgeliği · Clever Thinking: The Wisdom of Crowds',[
  g('hzcrowd',d=72),
  steps(CT,'Kalabalık ne zaman akıllıdır?','When is a crowd wise?',
    [['Herkes kendi bilgisiyle tahmin etmeli','Everyone guesses with their own knowledge','👥'],['Tahminler birbirinden bağımsız olmalı: kimse diğerinin cevabını duymamalı','Guesses must be independent — nobody should hear anyone else’s answer',''],['Farklı insanlar olmalı: hepsi aynı yönde yanılmasın','The people should be different, so they don’t all err the same way',''],['Sonra ortanca değer alınır: aşırı uçlar sonucu bozamaz','Then take the middle value — the wild extremes cannot spoil it','']],
    'Toplantılarda önce herkes cevabını kâğıda yazsın, sonra konuşulsun','In meetings, let everyone write their answer down first — then talk','#1f2a30','#05080a',gap=8,d=56),
  photo('jellybeans','Washington, 1980’ler · 1980s','Bir başkan ve en sevdiği şey: bir kavanoz jelibon','A president and his favourite thing — a jar of jelly beans','Ronald Reagan masasında hep bir kavanoz jelibon tutardı; yaban mersini aromalı jelibon, kırmızı-beyaz-mavi olsun diye onun için üretildi','Ronald Reagan always kept a jar of jelly beans on his desk — the blueberry flavour was created for him so the beans could be red, white and blue',d=40),
  rid('Bir çobanın 17 koyunu var.|9’u hariç hepsi kaçtı. Kaç koyunu kaldı?','A shepherd has 17 sheep. All but 9 run away. How many are left?','9 koyun!','9 sheep!',hint='Soruyu yavaş oku · Read the question slowly',sec=20,c1='#22303a',c2='#06090c'),
  fact('1.207','1906’da 787 kişi bir öküzün ağırlığını tahmin etti: tahminlerin ortancası 1.207 libre, gerçek ağırlık 1.198 libreydi','In 1906, 787 people guessed the weight of an ox — the middle guess was 1,207 lb, the true weight 1,198 lb','Francis Galton, “Vox Populi”, Nature, 1907','#1f2a30','#05080a',d=32),
]),
S(21,22,'Bulutların Atlası · An Atlas of Clouds',[
  photo('mammatus','Tulsa, ABD, 1973 · USA, 1973','Mammatus bulutları: gökyüzünden sarkan keseler','Mammatus clouds — pouches hanging from the sky','Çoğu bulut yukarı doğru kabarır; mammatus ise soğuk havanın aşağı çöktüğü yerlerde ters yöne, aşağıya doğru kabarır','Most clouds billow upwards — mammatus bulge downwards, where cold air sinks out of a storm’s underside',d=40),
  photo('lenticular','Rainier Dağı, ABD · Mount Rainier, USA','Mercimek bulutu: dağın üstünde duran bir “uçan daire”','A lenticular cloud — a “flying saucer” parked over the mountain','Rüzgâr esse de bulut yerinde durur: hava dağın üstünden dalga gibi geçer ve hep aynı noktada yoğuşur','It stays put even in strong wind — air flows over the mountain in a wave and condenses at the same spot',d=40),
  photo('shelf','Estonya · Estonia','Raf bulutu: yaklaşan bir fırtınanın önünde uzanan duvar','A shelf cloud — a wall leading an approaching storm','Fırtınanın soğuk hava akımı, önündeki sıcak havayı kaldırıp bu uzun rafı oluşturur; birkaç dakika içinde rüzgâr ve yağmur gelir','The storm’s cold outflow lifts the warm air ahead into this long shelf — wind and rain follow within minutes',d=40),
  photo('kelvin','Kelvin–Helmholtz bulutları · clouds','Gökyüzünde kırılan dalgalar: Kelvin–Helmholtz bulutları','Breaking waves in the sky — Kelvin–Helmholtz clouds','İki hava katmanı farklı hızlarda kayınca, rüzgârın denizde dalga yapması gibi gökyüzünde de dalgalar oluşur','When two layers of air slide past at different speeds, waves form in the sky just as wind makes waves on the sea',d=40),
  photo('asperitas','Türkiye · Turkey','Asperitas: altından bakınca çalkantılı bir deniz yüzeyine benzeyen bulut','Asperitas — a cloud that looks like a rough sea seen from below','Adı Latincede “pürüzlülük” demek; dünyanın dört bir yanındaki amatör fotoğrafçıların gönderdiği resimlerle tanındı','Its name is Latin for “roughness” — it was recognised thanks to photos sent in by amateur cloud-watchers all over the world',d=40),
  fact('2017','Asperitas 2017’de Uluslararası Bulut Atlası’na eklendi: 1951’den beri eklenen ilk yeni bulut biçimi','Asperitas was added to the International Cloud Atlas in 2017 — the first new cloud form added since 1951','Dünya Meteoroloji Örgütü · World Meteorological Organization','#1a2430','#05070b',d=30),
  q('Bulut ağlamazsa|çimen nasıl güler?','If the cloud does not weep, how will the meadow smile?','sea',d=42),
]),
S(22,23,'Galeri: Ayvazovski’nin Gece Denizleri · Gallery: Aivazovsky’s Night Seas (sakin · calm)',[
  art('aiv1','Mehtaplı Gece — İvan Ayvazovski','Moonlit Night — Ivan Aivazovsky','Ayvazovski denizi açık havada değil, atölyesinde hafızasından boyardı; bir tabloyu çoğu zaman tek oturuşta bitirirdi','Aivazovsky painted the sea not outdoors but from memory in his studio — often finishing a painting in a single sitting',d=46),
  art('aiv6','Karadeniz — İvan Ayvazovski, 1881','The Black Sea — Ivan Aivazovsky, 1881','Kırım’daki Feodosya’da, Karadeniz kıyısında doğdu; bu tabloda yalnızca su ve gökyüzü var, başka hiçbir şey','He was born in Feodosia on the Black Sea coast of Crimea — this painting holds nothing but water and sky',d=46),
  art('aiv5','Mehtaplı Gecede Bir Vapur — İvan Ayvazovski','A Steamship on a Moonlit Night — Ivan Aivazovsky','Sultan Abdülaziz için İstanbul’un ve Boğaz’ın onlarca resmini yaptı; bir kısmı bugün Dolmabahçe Sarayı’nda','He painted dozens of views of İstanbul and the Bosphorus for Sultan Abdülaziz — some hang in Dolmabahçe Palace today',d=46),
  fact('6.000','Ayvazovski uzun hayatında 6.000’e yakın resim yaptı: çoğu deniz','Over his long life Aivazovsky made close to 6,000 paintings — most of them of the sea','1817–1900','#121a26','#03050a',d=30),
  q('Sessizlik|Tanrı’nın dilidir','Silence is the language of God','night',d=44),
]),
S(23,26,'Kutup Yıldızı Etrafında · Around the Pole Star (sakin · calm)',[
  g('hzstartrail',d=100),
  photo('hedgehog','Avrupa kirpisi · European hedgehog','Kuru yaprakların arasında bir kirpi','A hedgehog among dry leaves','Kasım’da kirpiler kış uykusuna hazırlanır: uykuda kalp atışı dakikada yaklaşık 190’dan 20’ye kadar iner','In November hedgehogs settle in to hibernate — asleep, the heart slows from about 190 beats a minute to around 20',d=46),
  fact('≈430','Kutup Yıldızı yaklaşık 430 ışık yılı uzakta: bu gece gördüğün ışık 1590’larda yola çıktı','The Pole Star is about 430 light years away — the light you see tonight set off in the 1590s','Polaris, Küçükayı takımyıldızı · Polaris, Ursa Minor','#121a26','#03050a',d=32),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: üç küçük teşekkür','Before sleep: three small thank-yous',
    [['Bugün sana iyilik eden biri','Someone who was kind to you today','☾'],['Bugün işini kolaylaştıran bir şey','Something that made your day easier',''],['Yarın teşekkür etmek istediğin biri','Someone you’d like to thank tomorrow','']],
    'Yıldızlar gibi düşünceler de yavaşça dönüp yerine oturur','Like the stars, thoughts slowly turn and settle into place','#121a26','#03050a',gap=9,d=50,bg='stars'),
  q('Gece ne kadar karanlıksa|yıldızlar o kadar parlak','The darker the night, the brighter the stars','night',d=44,lb='Gece Sözü · Night Saying',by='Apollon Maykov, 1878'),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-23.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
