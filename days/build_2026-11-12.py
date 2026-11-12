# Builds /workspace/tv-pages/days/2026-11-12.json (hourly sets 09:00-02:00). Pattern from build_2026-11-11.py.
import json,os
DATE='2026-11-12'; REV=59; NEXT='2026-11-13'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-12.json')))
FIX={'NASA/Apollo 17 crew; taken by either Harrison Schmitt or Ron Evans':'NASA / Apollo 17','Image by NASA, modifications by Seddon':'NASA','Surmene at en.wikipedia':'Surmene (en.wikipedia)','Garst, Warren, 1922-2016, photographer':'Warren Garst','https://www.flickr.com/photos/clpmag/':'clpmag (Flickr)','Original: Tambako The Jaguar':'Tambako The Jaguar / Niabot','Al_Khazneh_Petra.jpg: Graham Racher':'Graham Racher / MrPanyGoff','Unknown authorUnknown author':'bilinmeyen fotoğrafçı · unknown photographer','Dartmouth Electron Microscope Facility':'Dartmouth Electron Microscope Facility','shankar s. from Dubai':'shankar s.','Rosa Cabecinhas and Alcino Cunha':'Rosa Cabecinhas & Alcino Cunha'}
def artist(k):
    a=C[k]['artist'].split('(')[0].strip().rstrip('.')
    for f,t in FIX.items():
        if a.startswith(f[:20]): return t
    if a.startswith('NASA / Johns Hopkins'): return 'NASA / JHUAPL / SwRI'
    return a
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38):
    it=dict(k='hzphoto',d=d,f='m/h12-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    return it
def villa(k,where,tr,en,fact,facte,fit=None):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=40)
    it['lb']='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where
    return it
def art(k,tr,en,fact,facte,who):
    it=photo(k,'',tr,en,fact,facte,fit='contain',d=44)
    it['lb']='Gerçek Eser · Real Artwork'
    it['cr']='Eser · Artwork: %s · kamu malı · public domain · Wikimedia Commons'%who
    return it
def q(tr,en,pal,d=44,fs=None):
    it=dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
    if fs: it['fs']=fs
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
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
sets=[
S(9,10,'Vadilerin Sesi · Voices of the Valleys',[
  photo('zilkale','Çamlıhemşin, Rize','Zilkale — Fırtına Vadisi’nde ormanın içinden yükselen bir ortaçağ kalesi','Zilkale — a medieval castle rising out of the forest in the Fırtına Valley','Sabah sisinde kale, ağaçların üstünde yüzüyormuş gibi görünür','In the morning mist the castle seems to float above the trees'),
  q('Bir işi ruhundan yaptığında|içinde akan bir nehir hissedersin','When you do things from your soul, you feel a river moving in you — a joy','sea'),
  photo('hemsin','Hemşin, Rize','Bilen köyü — yemyeşil yamaçlara serpilmiş evler','Bilen village — houses scattered over bright green slopes','Doğu Karadeniz yılda 2.000 mm’yi aşan yağışıyla Türkiye’nin en yeşil köşesi','With over 2,000 mm of rain a year, the eastern Black Sea is Türkiye’s greenest corner'),
  fact('Kuş dili','Giresun’un Kuşköy’ünde insanlar ıslıkla konuşur: kelimeler bir vadiden ötekine ıslık olarak taşınır','In Kuşköy, Giresun, people talk by whistling — words travel from one valley to the next as whistles','UNESCO acil koruma listesinde, 2017 · On UNESCO’s urgent safeguarding list, 2017','#1e2c24','#040805',d=32),
  steps('Akıllı Açıklama · Clever Explainer','Yeşil yaprak nasıl siyah çaya dönüşür?','How does a green leaf become black tea?',
    [['Taze filizler, “iki yaprak bir tomurcuk” toplanır','Fresh shoots are picked: “two leaves and a bud”',''],['Yapraklar birkaç saat soldurulur, yumuşar','The leaves are withered for hours until soft',''],['Kıvrılıp ezilir, hücreler açılır','They are rolled and crushed, opening the cells',''],['Havayla buluşan özsu kararır','The juice meets the air and darkens','oksidasyon · oxidation'],['Kurutulur — ve demliğe hazır','Then dried — and ready for the teapot','☕']],
    'Yeşil çay da aynı yapraktan yapılır — sadece kararmasına izin verilmez','Green tea comes from the same leaf — it just isn’t allowed to darken','#22301e','#050804',gap=5.5),
  photo('boztepe','Trabzon','Boztepe’den akşam Trabzon — şehrin ışıkları ve Karadeniz','Trabzon at dusk from Boztepe — the city lights and the Black Sea','Boztepe’nin çay bahçeleri şehrin en sevilen manzara noktalarından','Boztepe’s tea gardens are among the city’s favourite viewpoints'),
  rid('Yatağı var ama hiç uyumaz,<br>ağzı var ama hiç konuşmaz.<br>Nedir?','It has a bed but never sleeps, a mouth but never speaks. What is it?','Dere — ya da nehir!','A river: it has a bed and a mouth.',sec=16,c1='#1c2c2a',c2='#040807'),
]),
S(10,11,'Turing’in Desenleri · Turing Patterns',[
  g('hzturing',d=72),
  photo('leopard','Kar leoparı · Snow leopard','Kar leoparının benekleri: kayalık dağlarda kusursuz bir kamuflaj','A snow leopard’s rosettes: perfect camouflage on rocky mountains','Kalın, uzun kuyruğunu denge için ve uyurken atkı gibi sarınmak için kullanır','It uses its long, thick tail for balance — and wraps it round like a scarf when sleeping',fit='contain'),
  fact('1952','Alan Turing son makalelerinden birinde, hayvan desenlerinin iki kimyasalın yarışından doğabileceğini yazdı','In one of his last papers, Alan Turing wrote that animal patterns could come from a race between two chemicals','“Morfogenezin Kimyasal Temeli” · “The Chemical Basis of Morphogenesis”','#28201a','#070504',d=32),
  photo('zebra','Etosha, Namibya · Namibia','Ova zebrasının gözü ve çizgileri','A plains zebra’s eye and stripes','Her zebranın çizgileri parmak izi gibi kendine özgüdür','Every zebra’s stripes are unique, like a fingerprint'),
  photo('puffer','Benekli balon balığı · Guineafowl puffer','Balon balığının sarı renk formu','The golden colour form of a guineafowl puffer','Tehlikede su yutarak kendini top gibi şişirir','In danger it gulps water and puffs up like a ball',fit='contain'),
  rid('Zebra beyaz üstüne siyah çizgili mi,<br>yoksa siyah üstüne beyaz mı?','Is a zebra black-striped on white, or white-striped on black?','Siyah üstüne beyaz!','Its skin is black underneath — the white stripes are hair without pigment.',sec=18,c1='#26262a',c2='#060607'),
]),
S(11,12,'Düşünce Deneyleri · Thought Experiments',[
  photo('pisa','Pisa, İtalya · Italy','Pisa Katedrali ve eğik kulesi, gün doğumunda','Pisa Cathedral and its leaning tower at sunrise','Galileo’nun kuleden top attığı anlatılır — muhtemelen hiç yapmadı; asıl kanıtı bir düşünce deneyiydi','Galileo is said to have dropped balls from the tower — he probably never did; his real proof was a thought experiment'),
  steps('Düşünce Deneyi · Thought Experiment','Galileo: ağır cisimler daha mı hızlı düşer?','Galileo: do heavy things fall faster?',
    [['Diyelim ki ağır taş hızlı, hafif taş yavaş düşüyor','Suppose a heavy stone falls fast and a light one slowly',''],['İkisini bir iple birbirine bağla','Tie the two together with a string',''],['Hafif taş ağırı frenlemeli: ikili daha yavaş düşer','The light one should hold the heavy one back: the pair falls slower','?'],['Ama ikili daha ağır: daha hızlı düşmeli!','But the pair is heavier, so it should fall faster!','!'],['Çelişki: demek ki hepsi aynı hızla düşer','A contradiction — so they all fall at the same rate','✓']],
    'Hava direnci olmasa tüy ile çekiç aynı anda yere iner — Apollo 15 bunu Ay’da gösterdi','Without air, a feather and a hammer land together — Apollo 15 showed it on the Moon','#1e2632','#040608',gap=6,d=60),
  q('Akıllılığını sat,|hayret satın al','Sell your cleverness and buy bewilderment','ink'),
  steps('Düşünce Deneyi · Thought Experiment','Newton’un Topu: dağın tepesinden bir top ateşle…','Newton’s Cannonball: fire a cannon from a mountaintop…',
    [['Yavaş ateşlersen top yakına düşer','Fire it slowly and it lands nearby',''],['Daha hızlı ateşle: daha uzağa düşer','Fire faster: it lands farther away',''],['Dünya yuvarlak — zemin topun altından “kaçar”','Earth is round — the ground curves away beneath it',''],['Saniyede ≈7,9 km hızla hiç yere değmez!','At ≈7.9 km per second it never touches down!','yörünge · orbit']],
    'Uydular aslında sürekli düşüyor — ama hep ıskalıyor','Satellites are really falling all the time — and always missing','#16202e','#030508',gap=6.5,bg='stars'),
  fact('16 yaş','Einstein 16 yaşındayken bir ışık huzmesinin yanında, onunla aynı hızda koştuğunu hayal etti','At 16, Einstein imagined running alongside a beam of light at the same speed','Bu hayal, on yıl sonra görelilik kuramına götürdü · Ten years later this daydream led to relativity','#202430','#050608',d=32),
  rid('Bir tuğla 1 kilo<br>artı yarım tuğla geliyor.<br>Bir tuğla kaç kilo?','A brick weighs 1 kg plus half a brick. How much does a brick weigh?','2 kilo!','If 1 kg equals half a brick, the whole brick is 2 kg.',hint='“1,5” cevabı tuzak… · “1.5” is the trap…',sec=24,d=40,c1='#2c2420',c2='#070505'),
]),
S(12,13,'Çarşı ve Zanaat · Bazaar & Craft',[
  photo('bazaar','İstanbul','Kapalıçarşı — dünyanın en eski ve en büyük kapalı çarşılarından biri','The Grand Bazaar — one of the oldest and largest covered markets in the world','1460’larda kuruldu; bugün 60’tan fazla sokak ve yaklaşık 4.000 dükkân','Founded in the 1460s; today over 60 streets and about 4,000 shops'),
  photo('ebru','Ebru · Paper marbling','Ebru sanatçısı suyun üstüne boyayla lale çiziyor','An ebru artist draws a tulip in paint on water','Her ebru tektir: aynı desen bir daha asla çıkmaz','Every ebru is one of a kind — the same pattern never appears twice'),
  steps('Akıllı Açıklama · Clever Explainer','Ebru: resim suyun üstünde nasıl durur?','Ebru: how does a picture stay on top of water?',
    [['Su, kitre bitkisinin özüyle koyulaştırılır','The water is thickened with gum tragacanth',''],['Boyalara biraz sığır ödü katılır — boya yayılır, batmaz','A little ox gall is added to the paints — they spread instead of sinking',''],['At kılı fırçalarla damla damla serpilir','Drops are flicked on with horsehair brushes',''],['Bizle desen çizilir, kâğıt yavaşça yüzeye yatırılır','Patterns are drawn with an awl, then paper is laid gently on top',''],['Kâğıt kaldırılır: resim artık kâğıttadır','The paper is lifted — and the picture is on it','✓']],
    'Türk ebru sanatı 2014’ten beri UNESCO listesinde','Turkish ebru has been on UNESCO’s list since 2014','#1e2a36','#04070a',gap=5.5),
  photo('carpet','Türkiye · Türkiye','Tezgâhta halı dokuyan bir kadın','A woman weaving a carpet on a loom','Türk düğümü (Gördes düğümü) her ilmeği iki çözgü ipine sarar — halı bu yüzden çok sağlamdır','The Turkish (Gördes) knot wraps two warp threads — that’s why the carpets are so strong',fit='contain'),
  fact('1.000.000+','Bir halıda metrekarede 1 milyondan fazla düğüm olabilir; ipek halılar yıllarca dokunur','A fine carpet can hold over a million knots per square metre; silk carpets take years to weave','Hereke halıları bunun en ünlü örnekleri · Hereke carpets are the most famous examples','#2a1e22','#070506',d=32),
  rid('Satıcı bir halıyı 100 TL’ye alıp 120’ye sattı,<br>140’a geri alıp 160’a sattı.<br>Kârı ya da zararı ne?','A seller buys a carpet for 100, sells it for 120, buys it back for 140 and sells it for 160. Profit or loss?','40 TL kâr!','Two trades, each +20: (120−100) + (160−140) = 40.',hint='İki ayrı alışveriş gibi düşün · Treat it as two separate trades',sec=26,d=42,c1='#2a2420',c2='#070605'),
]),
S(13,14,'Hücrelerin Geometrisi · Geometry of Cells',[
  g('hzvoronoi',d=66),
  photo('honeycomb','Tayvan · Taiwan','Kusursuz altıgenler: bal peteği','Perfect hexagons: a honeycomb','Altıgen, düzlemi en az duvar malzemesiyle eşit parçalara böler — 1999’da kanıtlandı','Hexagons divide a plane into equal cells with the least wall material — proved in 1999'),
  photo('giraffe','Masai zürafası · Masai giraffe','Zürafaların derisindeki lekeler','The patches on giraffes’ coats','Her zürafanın deseni benzersizdir; desenler anneden yavruya kısmen geçer','Every giraffe’s pattern is unique, and patterns are partly passed from mother to calf'),
  fact('3 × 120°','Köpükte baloncuklar hep üçerli buluşur ve aralarında 120° açı olur','In foam, bubbles always meet in threes, at 120° to each other','Plateau yasaları, 1873 · Plateau’s laws, 1873','#1c2630','#040608',d=30),
  photo('foam','Kaliforniya · California','Planktonların oluşturduğu deniz köpüğü','Sea foam created by plankton','Her baloncuk, komşularıyla en kısa sınırı paylaşmaya çalışır','Each bubble tries to share the shortest possible border with its neighbours'),
  photo('dragonfly','Yusufçuk · Dragonfly','Bir dala tünemiş yusufçuk','A dragonfly perched on a twig','Kanatlarındaki ince damarlar küçük hücrelere bölünmüştür; dört kanadını ayrı ayrı oynatabilir','Fine veins split its wings into tiny cells, and it can move all four wings independently'),
  rid('Hangi şekil zemini<br>boşluksuz kaplar:<br>düzgün beşgen mi, altıgen mi?','Which shape tiles a floor with no gaps: a regular pentagon or a hexagon?','Altıgen!','Regular pentagons leave gaps; only triangles, squares and hexagons tile perfectly.',sec=18,c1='#22282e',c2='#050607'),
]),
S(14,15,'Villa Fikirleri: Kış Ritüelleri · Villa Ideas: Winter Rituals',[
  villa('hamam','Hürrem Sultan Hamamı, İstanbul','Mermer göbek taşı ve kubbeden süzülen ışık','A marble heated stone and light falling from the dome','Mimar Sinan, 1556 — fikir: villada küçük, mermer bir buhar odası','Mimar Sinan, 1556 — idea: a small marble steam room at the villa',fit='contain'),
  q('İnsan olmak bir misafirhanedir;|her sabah yeni bir konuk gelir','This being human is a guest house — every morning a new arrival','clay'),
  villa('sauna','Vantaa, Finlandiya · Finland','Geleneksel bir duman saunasının taş sobası','The stone stove of a traditional smoke sauna','Duman saunası en eski sauna türüdür; saatlerce ısıtılır, duman çıkınca girilir','The smoke sauna is the oldest kind: heated for hours, used once the smoke has cleared',fit='contain'),
  fact('3.300.000','5,5 milyon nüfuslu Finlandiya’da yaklaşık 3,3 milyon sauna var','Finland has about 3.3 million saunas for 5.5 million people','Fikir: Karadeniz manzaralı bir çatı saunası · Idea: a rooftop sauna with a Black Sea view','#2a2420','#070605',d=32),
  villa('onsen','Akita, Japonya · Japan','Karlar içinde açık hava kaplıcası (rotenburo)','An open-air hot spring bath (rotenburo) in the snow','Fikir: bahçede sıcak bir dış havuz — kar yağarken içinde oturmak','Idea: a hot outdoor tub in the garden — sitting in it while snow falls'),
  steps('Villa Fikri · Villa Idea','Kış akşamı misafir ritüeli','A winter-evening ritual for guests',
    [['Kapıda yün terlik ve sıcak ıhlamur','Wool slippers and hot linden tea at the door',''],['Saunada 15 dakika, sonra serin bir duş','15 minutes in the sauna, then a cool shower',''],['Şöminenin yanında kestane ve mandalina','Chestnuts and tangerines by the fire',''],['Yatağın üstünde el yazısı bir “iyi geceler” kartı','A handwritten “good night” card on the bed','']],
    'Küçük ritüeller, sıradan bir geceyi hatırlanan bir geceye çevirir','Small rituals turn an ordinary night into one guests remember','#26282c','#060607',gap=6,d=54),
]),
S(15,16,'Sayıların Gizemi · Mysteries of Numbers',[
  g('hzcollatz',d=70),
  photo('ishango','Brüksel · Brussels','Ishango kemiği — üzerinde gruplar hâlinde çentikler olan bir kemik','The Ishango bone — a bone carved with groups of notches','Yaklaşık 20.000 yıllık; insanların sayı saymak için kullandığı en eski araçlardan biri olabilir','About 20,000 years old — perhaps one of the oldest counting tools ever made',fit='contain'),
  steps('Akıllı Düşünce · Clever Thinking','1’den 100’e kadar bütün sayıları hızla nasıl toplarsın?','How can you quickly add all the numbers from 1 to 100?',
    [['Öğretmen sınıfı oyalamak için bu soruyu sorar','A teacher asks this to keep the class busy',''],['Küçük Gauss baştan ve sondan eşleştirir: 1+100, 2+99…','Young Gauss pairs them from both ends: 1+100, 2+99…',''],['Her çift 101 eder ve 50 çift vardır','Every pair makes 101, and there are 50 pairs',''],['50 × 101 =','50 × 101 =','5050']],
    'Dakikalar değil, saniyeler — doğru bakış açısının gücü','Seconds, not minutes — the power of looking at it the right way','#1e2430','#040608',gap=6),
  photo('ramanujan','Srinivasa Ramanujan (1887–1920)','Kendi kendine matematik öğrenen Hintli dâhi Ramanujan','Ramanujan, the self-taught mathematical genius','Hastanede “1729 sıkıcı bir sayı” denince: “Hayır! İki küp toplamı olarak iki farklı şekilde yazılabilen en küçük sayı” dedi','Told 1729 was a dull number, he replied: “No! It is the smallest number that is the sum of two cubes in two different ways”',fit='contain'),
  fact('10¹⁰⁰','1 ve ardından 100 sıfır: “googol”. Adı 1920’de 9 yaşındaki bir çocuk koydu','1 followed by 100 zeros is a “googol” — named in 1920 by a 9-year-old boy','Google adını bu sayıdan aldı · Google took its name from it','#1a2a26','#040806',d=30),
  rid('Bir sayı düşün. 2 ile çarp, 10 ekle,<br>2’ye böl, sonra düşündüğün<br>sayıyı çıkar. Sonuç kaç?','Think of a number. Double it, add 10, halve it, then subtract the number you thought of. What do you get?','5!','Whatever you chose: (2n + 10) ÷ 2 − n = 5.',sec=28,d=42,c1='#22263a',c2='#05060a'),
]),
S(16,17,'Algı ve Gerçek · Perception & Reality',[
  g('hzwhite',d=44),
  photo('mirage','Neuwerk, Almanya · Germany','Fata Morgana: deniz ufkunda gemiler ve kıyı havada asılı gibi','Fata Morgana: ships and shoreline seem to hang above the sea','Gerçek bir görüntü ama yanlış yerde — fotoğraf makinesi de görür','A real image in the wrong place — a camera can capture it too'),
  steps('Akıllı Açıklama · Clever Explainer','Serap nasıl oluşur?','How does a mirage form?',
    [['Işık, farklı sıcaklıktaki hava katmanlarından geçerken bükülür','Light bends when it passes through layers of air at different temperatures',''],['Sıcak asfaltta ışık yukarı kıvrılır','Over hot asphalt, light curves upward',''],['Gördüğün “su birikintisi” aslında gökyüzünün yansıması','The “puddle” you see is really a reflection of the sky','!'],['Soğuk denizin üstünde ise ışık aşağı kıvrılır — uzak gemiler havada görünür','Over cold sea, light curves down — distant ships appear in the air','Fata Morgana']],
    'Beynin ışığın düz gittiğini varsayar — serap bu varsayımın faturası','Your brain assumes light travels straight — a mirage is the price of that assumption','#1e2a34','#04070a',gap=6.5),
  g('hzpogg',d=42),
  fact('%30','Beyin kabuğunun yaklaşık üçte biri görmeyle ilgili işlere ayrılır','Around a third of the brain’s cortex is involved in vision','Gördüğün şey, gözünün değil beyninin çizdiği bir resimdir · What you see is a picture painted by your brain, not your eye','#24202c','#060508',d=32),
  rid('Ne kadar yaklaşırsan<br>o kadar uzaklaşır.<br>Nedir?','The closer you get, the farther it moves away. What is it?','Ufuk — ya da serap!','The horizon — or a mirage.',sec=16,c1='#22303a',c2='#05080a'),
]),
S(17,18,'Çöllerin Sessizliği · The Silence of Deserts',[
  photo('deadvlei','Namib Çölü, Namibya · Namib Desert, Namibia','Deadvlei: turuncu kum tepelerinin önünde kurumuş ağaçlar','Deadvlei: dead trees in front of orange dunes','Ağaçlar yaklaşık 600–700 yıl önce kurudu; hava o kadar kuru ki çürümüyorlar','The trees died some 600–700 years ago — the air is so dry they do not rot'),
  photo('wadirum','Ürdün · Jordan','Wadi Rum: kızıl kumlar ve kumtaşı dağlar','Wadi Rum: red sand and sandstone mountains','Birçok filmde Mars’ın yerine geçti','It has stood in for Mars in several films'),
  fact('6.000 yıl önce','Sahra yeşildi: göller, çayırlar, zürafalar ve suaygırları vardı','The Sahara was green: lakes, grasslands, giraffes and hippos','Kayalara yüzen insan resimleri çizilmiş · People even painted swimmers on its rocks','#2a2418','#070604',d=32),
  photo('erg','Erg Chebbi, Fas · Morocco','Erg Chebbi kumulları','The dunes of Erg Chebbi','Rüzgârın taşıdığı kumdan oluşan kumullar 150 metreye kadar yükselir','Wind-blown dunes here rise up to 150 metres',fit='contain'),
  steps('Akıllı Açıklama · Clever Explainer','Deve çölde nasıl hayatta kalır?','How does a camel survive the desert?',
    [['Hörgücünde su değil, yağ depolar','Its hump stores fat, not water',''],['10 dakikada 100 litre su içebilir','It can drink 100 litres of water in ten minutes',''],['Kum fırtınasında burun deliklerini kapatır; çift sıra kirpikleri vardır','It closes its nostrils in sandstorms and has a double row of eyelashes',''],['Vücut ısısını gün içinde değiştirip terlemeden su biriktirir','It lets its body temperature swing during the day to save water instead of sweating','']],
    'Bu yüzden ona “çölün gemisi” denir','That is why it is called the “ship of the desert”','#2c2418','#070604',gap=6),
  photo('atacama','Atacama Çölü, Şili · Chile','Dünyanın en kurak çölünde, ALMA gözlemevi yakınında yaşayan bir bitki','A plant living near the ALMA observatory in the world’s driest desert','Bazı hava istasyonlarına hiç yağmur düşmedi; nadiren yağınca çöl çiçeklerle kaplanır','Some weather stations have never recorded rain; when it rarely does, the desert bursts into flower'),
  rid('Denize hiç girmez<br>ama ona gemi derler.<br>Nedir?','It never goes to sea, yet people call it a ship. What is it?','Deve!','The camel — the ship of the desert.',sec=14,c1='#2c2418',c2='#070604'),
]),
S(18,19,'Zekâ Atölyesi · Brain Workshop',[
  steps('Mantık Bulmacası · Logic Puzzle','Kurt, keçi ve lahana','The wolf, the goat and the cabbage',
    [['Kayıkla bir kurt, bir keçi ve bir lahanayı karşıya geçireceksin','You must ferry a wolf, a goat and a cabbage across a river',''],['Kayığa seninle birlikte sadece biri sığar','Only one fits in the boat with you',''],['Yalnız kalırsa kurt keçiyi, keçi lahanayı yer','Left alone, the wolf eats the goat, the goat eats the cabbage','!'],['Önce keçiyi geçir; sonra kurdu geçir ama keçiyi geri getir','Take the goat first; then the wolf — but bring the goat back',''],['Lahanayı geçir, en son keçiyi al','Take the cabbage, and finally the goat','✓']],
    'Bazen ileri gitmek için bir şeyi geri getirmek gerekir — York’lu Alcuin, yaklaşık 800','Sometimes you must bring something back to move forward — Alcuin of York, c. 800','#1e2a24','#040806',gap=6.5,d=62),
  photo('mangala','Uganda, 1965','Mankala ailesinden bir oyun tahtası (kisolo)','A board from the mancala family of games (kisolo)','Türkiye’de oynanan mangala da bu çok eski akıl oyunları ailesinden','Türkiye’s mangala belongs to this very old family of strategy games',fit='contain'),
  rid('Bir saatin 3’ü vurması 3 saniye sürüyor.<br>6’yı vurması<br>kaç saniye sürer?','A clock takes 3 seconds to strike 3. How long does it take to strike 6?','7,5 saniye!','3 strikes have 2 gaps of 1.5 s; 6 strikes have 5 gaps → 7.5 s.',hint='Vuruşları değil, aralarındaki boşlukları say · Count the gaps, not the strikes',sec=26,d=42,c1='#2a2430',c2='#070508'),
  steps('Kutunun Dışında · Outside the Box','9 nokta, 4 düz çizgi: kalemi kaldırmadan hepsini birleştir','9 dots, 4 straight lines — join them all without lifting your pen',
    [['Noktalar 3×3 bir kare oluşturuyor','The dots form a 3×3 square',''],['Çoğu insan çizgileri karenin içinde tutmaya çalışır','Most people try to keep the lines inside the square',''],['Ama kimse “karenin içinde kal” demedi!','But nobody said “stay inside the square”!','!'],['Çizgileri karenin dışına taşırınca 4 çizgi yeter','Let the lines run past the edges, and 4 are enough','✓']],
    '“Kutunun dışında düşünmek” deyiminin bu bulmacadan geldiği söylenir','The phrase “thinking outside the box” is said to come from this puzzle','#20262e','#050607',gap=6.5),
  steps('Fermi Tahmini · Fermi Estimate','Trabzon’da bir günde kaç bardak çay içiliyor?','How many glasses of tea are drunk in Trabzon in a day?',
    [['Nüfus ≈ 800.000','Population ≈ 800,000',''],['Yetişkinler ≈ %70 → ≈ 560.000 kişi','Adults ≈ 70% → ≈ 560,000 people',''],['Kişi başı günde ≈ 5 bardak','About 5 glasses each per day',''],['560.000 × 5 ≈','560,000 × 5 ≈','≈ 3 milyon · million']],
    'Kesin değil ama doğru büyüklükte — Enrico Fermi’nin sevdiği düşünme oyunu','Not exact, but the right size — Enrico Fermi’s favourite thinking game','#2a2218','#070504',gap=6.5),
  fact('197.281','Satrançta iki taraf da yalnızca ikişer hamle yaptıktan sonra 197.281 farklı oyun mümkün','After just two moves each, there are 197,281 possible chess games','Hamle sayısı arttıkça sayı, evrendeki atomlardan bile fazla olur · Soon the count exceeds the atoms in the universe','#1c2228','#040506',d=30),
]),
S(19,20,'Antik Harikalar · Ancient Wonders',[
  photo('gobekli','Şanlıurfa','Göbeklitepe — oyma taş sütunlarla dünyanın bilinen en eski tapınak alanlarından biri','Göbekli Tepe — one of the oldest known monumental sites on Earth','Yaklaşık 11.600 yıllık: Stonehenge’den 6.000 yıl daha eski; UNESCO Dünya Mirası','About 11,600 years old — 6,000 years older than Stonehenge; UNESCO World Heritage'),
  photo('petra','Ürdün · Jordan','Petra’daki el-Hazne — kumtaşı kayaya oyulmuş bir cephe','Al-Khazneh in Petra — a façade carved into sandstone','Nebatiler onu yaklaşık 2.000 yıl önce yukarıdan aşağıya doğru oydu','The Nabataeans carved it about 2,000 years ago, working from the top down',fit='contain'),
  photo('celsus','Efes, İzmir · Ephesus','Celsus Kütüphanesi’nin cephesi','The façade of the Library of Celsus','MS 117 civarında tamamlandı; yaklaşık 12.000 parşömen tomarı saklıyordu','Completed around AD 117, it held some 12,000 scrolls'),
  photo('nemrut','Adıyaman','Nemrut Dağı’nın zirvesindeki dev taş başlar','The giant stone heads on the summit of Mount Nemrut','Kommagene Kralı I. Antiokhos’un anıt mezarı, MÖ 1. yüzyıl, 2.134 m','The tomb-sanctuary of King Antiochus I of Commagene, 1st century BC, 2,134 m',fit='contain'),
  photo('machu','Peru','Machu Picchu — bulutlara yakın bir İnka kenti','Machu Picchu — an Inca city close to the clouds','Taşlar harçsız ama öyle iyi oturtulmuş ki arasına bıçak girmez','The stones use no mortar, yet fit so tightly a knife blade won’t go between them',fit='contain'),
  fact('25.000','Efes’in Büyük Tiyatrosu yaklaşık 25.000 kişi alıyordu — mikrofon olmadan','The Great Theatre of Ephesus seated about 25,000 people — with no microphones','Basamakların biçimi sesi en arka sıraya kadar taşır · The shape of the tiers carries sound to the back row','#2a2418','#070604',d=32),
  rid('Taştan yapılmış ama<br>ne ev ne köprü;<br>gölgesiyle saati söyler. Nedir?','Made of stone, yet neither house nor bridge; it tells the time with its shadow. What is it?','Güneş saati!','A sundial.',sec=16,c1='#2a2620',c2='#070605'),
]),
S(20,21,'Mikro Dünya · The Micro World',[
  art('diatom','Diyatomeler — Ernst Haeckel, “Doğadaki Sanat Biçimleri”, 1904','Diatoms — Ernst Haeckel, “Art Forms in Nature”, 1904','Camdan kabuklu bu minik algler, soluduğumuz oksijenin yaklaşık beşte birini üretir','These tiny algae with glass shells make roughly a fifth of the oxygen we breathe','Ernst Haeckel'),
  photo('pollen','Elektron mikroskobu · Electron microscope','Ayçiçeği, gündüzsefası, gambak ve zambak polenleri (renklendirilmiş)','Pollen grains of sunflower, morning glory, hollyhock and lily (colourised)','Polen kabuğu o kadar dayanıklıdır ki milyonlarca yıl bozulmadan kalabilir','A pollen wall is so tough it can survive for millions of years',fit='contain'),
  photo('leeuwenhoek','Leeuwenhoek mikroskobu · Leeuwenhoek microscope','Tek mercekli, avuç içi büyüklüğünde bir mikroskop','A palm-sized microscope with a single lens','Antonie van Leeuwenhoek 1676’da bununla bakterileri ilk gören kişi oldu','In 1676 Antonie van Leeuwenhoek became the first person to see bacteria with one like this',fit='contain'),
  art('radiolaria','Radyolaryalar — Ernst Haeckel, 1904','Radiolarians — Ernst Haeckel, 1904','Bir milimetreden küçük bu canlılar camdan, simetrik iskeletler örer','Smaller than a millimetre, these creatures build symmetrical skeletons of glass','Ernst Haeckel'),
  fact('39 trilyon','Vücudunda yaklaşık 39 trilyon bakteri yaşar — kendi hücrelerin kadar','About 39 trillion bacteria live in your body — roughly as many as your own cells','Çoğu dost: sindirime ve bağışıklığa yardım ederler · Most are friends, helping digestion and immunity','#1c2a26','#040806',d=32),
  rid('Bir insan saçının kalınlığı<br>kaç mikron?<br>1 mi, 10 mu, 70 mi?','How thick is a human hair in microns: 1, 10 or 70?','≈ 70 mikron!','About 70 micrometres — a bacterium is about 1, a pollen grain about 25.',sec=18,c1='#20262c',c2='#050607'),
]),
S(21,22,'Akşam Galerisi · Evening Gallery',[
  art('ninthwave','Dokuzuncu Dalga — İvan Ayvazovski, 1850','The Ninth Wave — Ivan Aivazovsky, 1850','Ayvazovski denizi hafızasından boyardı; ömrü boyunca 6.000’e yakın tablo yaptı','Aivazovsky painted the sea from memory, making nearly 6,000 pictures in his life','Ivan Aivazovsky'),
  q('Gerçekten sevdiğin şeyin|seni sessizce çekmesine izin ver','Let yourself be silently drawn by the strange pull of what you really love','night'),
  art('wanderer','Sis Denizinin Üzerindeki Gezgin — Caspar David Friedrich, yaklaşık 1818','Wanderer above the Sea of Fog — Caspar David Friedrich, c. 1818','Yüzünü hiç görmeyiz; böylece manzaraya onun gözleriyle bakarız','We never see his face — so we look at the view through his eyes','Caspar David Friedrich'),
  art('hammershoi','Strandgade 30’da İç Mekân — Vilhelm Hammershøi, 1900','Interior, Strandgade 30 — Vilhelm Hammershøi, 1900','“Sessizliğin ressamı”: Kopenhag’daki evinin boş odalarını ve pencere ışığını boyadı','“The painter of silence”: he painted the empty rooms and window light of his Copenhagen home','Vilhelm Hammershøi'),
  art('milkmaid','Sütçü Kız — Johannes Vermeer, yaklaşık 1658','The Milkmaid — Johannes Vermeer, c. 1658','Küçücük bir tablo (45 × 41 cm); bugün Amsterdam’daki Rijksmuseum’da','A small painting (45 × 41 cm), today in the Rijksmuseum in Amsterdam','Johannes Vermeer'),
]),
S(22,23,'Sessiz Kış Gecesi · Quiet Winter Night',[
  q('Ne kadar sessizleşirsen|o kadar çok duyarsın','The quieter you become, the more you are able to hear','night',d=46),
  photo('snowforest','Kış · Winter','Karlı ormanda ağaçların arasından süzülen ışık','Light filtering through a snowy forest','Kar örtüsü, altındaki toprağı bir battaniye gibi sıcak tutar','A blanket of snow keeps the soil beneath it warm',d=42),
  steps('Sakin Açıklama · Calm Explainer','Ayılar kış uykusunda ne yapar?','What do bears do while they hibernate?',
    [['Kaçkarlar’ın boz ayıları kasımda inine çekilir','The brown bears of the Kaçkar Mountains retreat to their dens in November',''],['Kalp atışı dakikada 40’tan 10 civarına iner','Their heart rate drops from about 40 to around 10 beats a minute',''],['Aylarca yemez, içmez — vücudu kendi yağını kullanır','For months they neither eat nor drink — the body burns its own fat',''],['Baharda uyanır; dişiler inde yavrulamış olur','They wake in spring — and the mothers have had their cubs in the den','🐻']],
    'Doğanın en uzun ve en derin dinlenmesi','Nature’s longest, deepest rest','#121a26','#020306',gap=6.5,d=52),
  photo('frost','Buz çiçekleri · Frost ferns','Soğuk bir gecede cama işlenen buz kristalleri','Ice crystals drawn on a window pane on a cold night','Havadaki su buharı soğuk camın üstünde doğrudan buza dönüşür, eğrelti otu gibi dallanır','Water vapour turns straight to ice on the cold glass and branches like ferns',d=40),
  fact('≈1 saat','Bir kar tanesinin buluttan yere düşmesi yarım saatle bir saat arasında sürebilir','A snowflake can take between half an hour and an hour to fall from its cloud to the ground','Saniyede yalnızca yaklaşık 1 metre · Only about 1 metre per second','#121a28','#020306',d=32),
  rid('Düşerken hiç ses çıkarmam,<br>ama sabah herkes beni konuşur.<br>Neyim?','I make no sound when I fall, but in the morning everyone talks about me. What am I?','Kar!','Snow.',sec=16,c1='#10162a',c2='#020307'),
]),
S(23,26,'İlk Kar · First Snow (sakin · calm)',[
  g('hzsnow',d=80),
  q('Bir mum, başka bir mumu tutuşturmakla|ışığından bir şey kaybetmez','A candle loses none of its light by lighting another candle','night',d=46),
  steps('Sakin Yolculuk · Calm Journey','Sen uyurken yaptığın yolculuk (8 saat)','The journey you make while you sleep (8 hours)',
    [['Trabzon, Dünya’nın dönüşüyle saatte ≈1.260 km hızla döner','Trabzon spins with the Earth at ≈1,260 km/h','≈10.000 km'],['Dünya, Güneş’in çevresinde saatte ≈107.000 km gider','Earth travels round the Sun at ≈107,000 km/h','≈860.000 km'],['Güneş de galaksinin çevresinde dolanır','And the Sun circles the galaxy','≈6,6 milyon km'],['Ve sen hiç kıpırdamadan dinlenirsin','And you rest without moving at all','☾']],
    'Yarın sabah, bambaşka bir uzay noktasında uyanacaksın','Tomorrow morning you will wake in a completely different spot in space','#0e1624','#020306',gap=7,d=54,bg='stars'),
  fact('½','Yunuslar beynin yarısıyla uyur; diğer yarısı nefes almak için uyanık kalır','Dolphins sleep with half their brain; the other half stays awake to breathe','Sonra iki yarım nöbet değiştirir · Then the halves take turns','#101a26','#020305',d=32),
  rid('Senindir ama<br>başkaları senden çok kullanır.<br>Nedir?','It belongs to you, but other people use it more than you do. What is it?','Adın!','Your name.',sec=16,c1='#0e1424',c2='#020306'),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-12.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
