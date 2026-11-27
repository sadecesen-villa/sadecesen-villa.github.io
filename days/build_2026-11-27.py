# Builds /workspace/tv-pages/days/2026-11-27.json (hourly sets 09:00-02:00). Friday.
# 09 Trabzon & Rize morning · 10 living art: when waves meet (NEW hzslit) · 11 terraced landscapes · 12 tiles · 13 Hiroshige · 14 Jupiter
# 15 illusions: ambiguous figures (NEW hzrubin, hznecker, hzkoffka) · 16 Königsberg bridges (NEW hzeuler) · 17-19 DJ Taş Act 1 Jazz House Lounge (Lisbon; villa open-air cinema)
# 19-22 Act 2 Sunset (Bosphorus, savanna, Indian Ocean) · 22-02 Act 3 Night (Japan in snow; Lapland + NEW hzbuz), stills only, no video.
# Photos m/h27-* (/workspace/hourly/dl27*.py + q27*.json), credits days/credits-2026-11-27.json.
import json,os
DATE='2026-11-27'; REV=86; NEXT='2026-11-28'
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-27.json')))
ART={'alhambratile':'Museo de la Alhambra (anonim · anonymous)','delfttile':'TxllxT','hiro2':'Utagawa Hiroshige','hiro4':'Utagawa Hiroshige','hiro5':'Utagawa Hiroshige','tyoung':'Thomas Lawrence’dan kopya · after Thomas Lawrence','jupiterhst':'NASA, ESA, A. Simon (NASA Goddard)','lemorne':'dronepicr','rizetea':'Wikimol','masaimara':'Richard Probst','kenrokuen':'tab2_dawa','ginzan':'Eiji Kikuta','gionnight':'Takeshi Kuboki','zanzibar':'Rod Waddington','junopole':'NASA / JPL / SwRI / MSSS, Kevin M. Gill','redspot':'NASA / SwRI / MSSS / Gerald Eichstädt / Seán Doran','lappcabin':'Vincent Guth','popcorn':'Alex Munsell','mucangchai':'Doan Tuan','tykky':'Simo Räsänen (Ximonic)'}
def artist(k): return ART.get(k) or C[k]['artist'].split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace('CC0','CC0 · kamu malı · public domain').replace('3.0 at','3.0 AT')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
A1='DJ Taş · 1. Perde · Act 1 — Caz House Lounge · Jazz House Lounge'
A2='DJ Taş · 2. Perde · Act 2 — Gün Batımı · Sunset'
A3='DJ Taş · 3. Perde · Act 3 — Gece · Night'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,pos=None,act=None,quiet=None):
    assert k in C,k
    lb=REAL+' · '+tag if not act else '%s · %s · %s'%(act,REAL,tag)
    it=dict(k='hzphoto',d=d,f='m/h27-%s.jpg'%k,lb=lb,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    if quiet: it['quiet']=1
    return it
def villa(k,where,tr,en,fact,facte,fit=None,d=42,act=None):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=d)
    it['lb']=(act+' · ' if act else '')+'Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where
    return it
def art(k,title,tr,en,fact,facte,d=46):
    it=photo(k,'',tr,en,fact,facte,fit='contain',d=d)
    it['lb']='Gerçek Eser · Real Artwork · '+title
    it['cr']='Eser · Artwork: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
    return it
def card(k,lb,lines,tr,en,d=30,pos=None):
    it=dict(k='hzwelcome',d=d,f='m/h27-%s.jpg'%k,lb=lb,lines=lines,tr=tr,en=en,cr=cr(k))
    if pos: it['pos']=pos
    return it
def q(tr,en,pal,d=44,lb=None,by=None):
    it=dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
    if lb: it.update(lb=lb,by=by)
    return it
def rid(qq,qe,a,ae,hint=None,sec=18,d=34,c1='#22303a',c2='#06090c'):
    it=dict(k='hzriddle',d=d,q=qq,qe=qe,a=a,ae=ae,sec=sec,c1=c1,c2=c2)
    if hint: it['hint']=hint
    return it
def fact(big,tr,en,src,c1,c2,d=32): return dict(k='hzfact',d=d,big=big,tr=tr,en=en,src=src,c1=c1,c2=c2)
def steps(lb,qq,e,st,fin,fine,c1,c2,gap=7,d=58): return dict(k='hzsteps',d=d,lb=lb,q=qq,e=e,c1=c1,c2=c2,gap=gap,steps=st,fin=fin,fine=fine)
def g(k,d=60,**kw): it=dict(k=k,d=d); it.update(kw); return it
def S(h1,h2,name,items,pre='h'):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='%s-%s-%02d'%(pre,DATE[5:],h1),name=name,**{'from':f,'until':u},items=[i for i in items if i])
CT='Zekice Düşünce · Clever Thinking'; SJ='Ölçek Yolculuğu · Scale Journey'


sets=[
S(9,10,'Cuma Sabahı · Friday Morning — Trabzon ve Rize · Trabzon & Rize',[
  photo('trabzonport','Trabzon Limanı · Trabzon harbour','Sabah ışığında Trabzon limanı ve Karadeniz','Trabzon harbour and the Black Sea in the morning light','Yüzyıllar boyunca İran’daki Tebriz’e giden kervan yolu burada denize ulaştı: ipek ve baharat bu limandan gemilere yüklendi','For centuries the caravan road to Tabriz in Persia reached the sea here — silk and spices were loaded onto ships at this harbour',d=40),
  q('Sevdiğin şeyin güzelliği,|yaptığın iş olsun','Let the beauty of what you love be what you do','sea',d=38),
  photo('kostaki','Kostaki Konağı · Trabzon Müzesi · Kostaki Mansion · Trabzon Museum','Trabzon Müzesi’nin bulunduğu taş konak ve bahçesi','The stone mansion that houses the Trabzon Museum, and its garden','20. yüzyılın başında bir banker için yapıldı; Atatürk 1924’te Trabzon’a geldiğinde burada kaldı','Built in the early 20th century for a banker — Atatürk stayed here when he came to Trabzon in 1924',d=38),
  photo('rizetea','Çay bahçeleri · Tea gardens, Rize','Rize’nin yamaçlarında sıra sıra çay','Rows of tea on the slopes of Rize','Türkiye’de çay tarımı 1940’larda Rize’de başladı; bugün Türkiye kişi başına dünyada en çok çay içen ülke: yılda 3 kilodan fazla','Tea farming in Turkey began in Rize in the 1940s — today Turks drink more tea per person than anyone else in the world, over 3 kg a year',d=40),
  photo('firtina','Fırtına Deresi · Fırtına Valley, Çamlıhemşin','Fırtına Deresi’nin üzerinde eski bir taş kemer köprü','An old stone arch bridge over the Fırtına stream','Vadi boyunca onlarca tarihî taş köprü var; derenin adı, yağmurdan sonra köpürerek akmasından gelir','Dozens of historic stone bridges line the valley — the stream’s name, “storm”, comes from the way it foams after rain',d=40),
  fact('≈ 1.700 km','Türkiye’nin Karadeniz kıyısı yaklaşık 1.700 km uzunluğunda: İstanbul’dan Gürcistan sınırındaki Sarp’a kadar. Bu, Londra ile Roma arasındaki uzaklıktan bile fazla','Turkey’s Black Sea coast is about 1,700 km long — from Istanbul to Sarp on the Georgian border. That is even more than the distance from London to Rome','Karadeniz kıyısı · The Black Sea coast','#13242c','#04080a',d=32),
  rid('Ne kadar çok olursa,|o kadar az görürsün.|Nedir?','The more of it there is, the less you see. What is it?','Sis! (ya da karanlık)','Fog! (or darkness)',hint='Karadeniz sabahlarını düşün · Think of Black Sea mornings',sec=16),
]),
S(10,11,'Yaşayan Sanat: Dalgalar Buluşunca · Living Art: When Waves Meet',[
  g('hzslit',d=72,ph=34),
  photo('soapfilm','Sabun köpüğü · a soap bubble (yakın çekim · close-up)','Bir sabun köpüğünün üstünde akan renkler','Colours flowing over a soap bubble','Renk boya değil: zarın ön ve arka yüzünden yansıyan ışık dalgaları üst üste biniyor. Zar inceldikçe renkler değişir; en ince yerde köpük patlamadan önce siyaha döner','The colour is not paint — light waves bouncing off the front and back of the film overlap. As the film thins the colours change, and the thinnest part turns black just before it pops',fit='contain',d=40),
  photo('tyoung','Thomas Young (1773–1829)','Thomas Young’ın portresi','A portrait of Thomas Young','Doktor, fizikçi ve dilbilimci: çift yarık deneyini yaptı ve Rosetta Taşı’ndaki hiyerogliflerin çözülmesine ilk adımları attı','A doctor, physicist and linguist — he did the double-slit experiment and took the first steps in decoding the hieroglyphs on the Rosetta Stone',fit='contain',d=34),
  steps(CT,'Işık tek tek gelse ne olur?','What if light arrives one piece at a time?',
    [['1801: Young iki yarıktan geçen ışıkla çizgili bir desen görür: ışık bir dalga gibi davranır','1801: Young sends light through two slits and sees stripes — light behaves like a wave','💡'],['1905: Einstein, ışığın aynı zamanda tanecikler (fotonlar) hâlinde geldiğini söyler','1905: Einstein says light also comes in particles — photons',''],['Deney, tek tek gönderilen parçacıklarla tekrarlanır: her biri perdede tek bir nokta bırakır','The experiment is repeated with particles sent one at a time — each leaves a single dot on the screen',''],['Binlerce nokta birikince… yine aynı çizgili desen ortaya çıkar','After thousands of dots… the same striped pattern appears again','']],
    'Her parçacık, bir dalga gibi iki yarıktan da “geçmiş” gibi davranıyor — kuantum dünyasının en büyük gizemlerinden biri','Each particle acts as if, like a wave, it went through both slits — one of the deepest mysteries of the quantum world','#14202c','#04070c',gap=8,d=58),
  g('hzpwave',d=56),
  fact('< 0,001 mm','Bir sabun köpüğünün zarı çoğu yerde milimetrenin binde birinden ince: bir saç telinden yüz kat kadar ince, aşağı yukarı ışığın dalga boyu kadar','Most of a soap bubble’s film is thinner than a thousandth of a millimetre — about a hundred times thinner than a hair, roughly the size of a wavelength of light','İnce mi ince · Thin, thinner','#14202a','#04070a',d=30),
  rid('Hangi dalga|seni hiç ıslatmaz?','Which wave never gets you wet?','El sallamak!','A wave of the hand!',sec=14),
]),
S(11,12,'Nefes Kesen Yerler: Basamaklı Topraklar · Breathtaking Places: Terraced Landscapes',[
  photo('longji','Longji pirinç terasları, Çin · Longji Rice Terraces, China','Guangxi’de dağın çevresine dolanan pirinç terasları','Rice terraces wrapping around the mountain in Guangxi','Adı “Ejderin Omurgası”: teraslar uzaktan bir ejderin pullarına benzer. Yüzyıllar boyunca elle, kuşaktan kuşağa yapıldı','Its name means “Dragon’s Backbone” — from afar the terraces look like a dragon’s scales. They were built by hand, generation after generation, over centuries',d=40),
  photo('banaue','Banaue, Filipinler · Banaue, the Philippines','Ifugao dağlarında yeşil terasların arasında köy','A village among the green terraces of the Ifugao mountains','Ifugao pirinç teraslarının yaklaşık 2.000 yıllık olduğu düşünülür; 1995’ten beri UNESCO Dünya Mirası','The Ifugao rice terraces are thought to be about 2,000 years old — a UNESCO World Heritage site since 1995',d=38),
  photo('mucangchai','Mù Cang Chải, Vietnam','Vadiye basamak basamak inen sarı-yeşil pirinç tarlaları','Rice fields stepping down into the valley','Teraslar dağın eş yükselti çizgilerini izler: su en üstten girer ve basamaktan basamağa akarak hepsini sular','The terraces follow the mountain’s contour lines — water enters at the top and flows down from step to step, watering them all',d=38),
  photo('jatiluwih','Jatiluwih, Bali, Endonezya · Indonesia','Palmiyelerin arasından Jatiluwih’in pirinç tarlaları','The rice fields of Jatiluwih seen through the palms','Bali’nin bin yıllık “subak” sulama düzeninde suyu köylülerin ve tapınakların ortak kararıyla paylaştırır; 2012’de UNESCO listesine girdi','Bali’s thousand-year-old “subak” system shares the water by joint decision of farmers and water temples — it joined the UNESCO list in 2012',d=40),
  photo('moray','Moray, Peru','Moray’de dev bir amfi tiyatro gibi iç içe dairesel teraslar','Circular terraces nested like a giant amphitheatre at Moray','İnkaların burayı bir tarım laboratuvarı olarak kullandığı düşünülür: her basamakta sıcaklık biraz farklı','The Incas are thought to have used it as a farming laboratory — each step has a slightly different temperature',d=38),
  photo('lavaux','Lavaux, İsviçre · Switzerland','Cenevre Gölü’ne inen Lavaux üzüm bağları','The Lavaux vineyards stepping down to Lake Geneva','Teraslar 12. yüzyılda keşişler tarafından kurulmaya başlandı; bağcılar “üç güneş” der: gökteki, göldeki yansıması ve ısınan taş duvarlar','Monks began building the terraces in the 12th century — winegrowers speak of “three suns”: the one in the sky, its reflection in the lake, and the warm stone walls',d=40),
  dict(k='hzchoose',d=40,q='Hangisinde bir sabah uyanmak isterdin?',qe='Which would you rather wake up in one morning?',a=dict(f='m/h27-longji.jpg',t='Sisli dağlarda pirinç terasları',e='Rice terraces in misty mountains',tag='Longji'),b=dict(f='m/h27-lavaux.jpg',t='Göle bakan üzüm bağları',e='Vineyards above a lake',tag='Lavaux'),p='Herkes birini seçsin, sonra nedenini söylesin',pe='Everyone picks one, then says why',cr='Fotolar · Photos: Rutger van der Maar · CC BY 2.0 / Lorenz Poffet · CC BY-SA 4.0 · Wikimedia Commons'),
]),
S(12,13,'Çininin Şiiri · Poetry in Tiles',[
  photo('izniktile','İznik seramiği · İznik ware (Çinili Köşk Müzesi, İstanbul · Tiled Kiosk Museum, Istanbul)','Mavi ve beyaz çiçek desenli bir İznik tabağı','An İznik plate with blue and white flowers','16. yüzyılda İznik atölyeleri Osmanlı saraylarına ve camilerine çini yaptı; parlak “domates kırmızısı”nın sırrı uzun süre çözülemedi','In the 16th century İznik’s workshops made tiles for Ottoman palaces and mosques — the secret of their bright “tomato red” long remained a mystery',fit='contain',d=40),
  photo('shahmosque','İmam (Şah) Camii, İsfahan · Shah Mosque, Isfahan','Kubbenin içi: merkeze doğru daralan çini halkaları','Inside the dome — rings of tiles narrowing towards the centre','1611–1629 arasında yapıldı; yüzeyleri yaklaşık yarım milyon çiniyle kaplı','Built between 1611 and 1629 — its surfaces are covered with around half a million tiles',fit='contain',d=40),
  photo('azulejo','São Bento Garı, Porto · São Bento Station, Porto','Gar salonunun duvarlarında mavi-beyaz azulejo panolar','Blue-and-white azulejo panels on the walls of the station hall','Ressam Jorge Colaço 1905–1916 arasında yaklaşık 20.000 çiniyle Portekiz tarihinden sahneler yaptı','Painter Jorge Colaço made scenes from Portuguese history between 1905 and 1916, using about 20,000 tiles',d=38),
  photo('zellige','Ben Youssef Medresesi, Marakeş · Ben Youssef Madrasa, Marrakesh','Elle kesilmiş küçük renkli parçalardan bir zellij yıldızı','A zellige star made of small hand-cut coloured pieces','Zellij ustaları her parçayı pişmiş çiniden çekiçle tek tek yontar; desen ancak parçalar ters çevrilip yan yana dizilince ortaya çıkar','Zellige craftsmen chip each piece from fired tile one by one with a hammer — the pattern only appears once the pieces are laid face down side by side',fit='contain',d=40),
  photo('delfttile','Menşikov Sarayı, St. Petersburg · Menshikov Palace','Tavanı ve duvarları Delft çinileriyle kaplı bir oda','A room with its ceiling and walls covered in Delft tiles','Hollanda’nın mavi Delft çinileri, Çin porselenini taklit etmek için doğdu; 18. yüzyılın başında bu saray odaları binlerce Delft çinisiyle kaplandı','Dutch blue Delft tiles were born as an imitation of Chinese porcelain — in the early 18th century these palace rooms were lined with thousands of them',d=38),
  photo('alhambratile','Elhamra Müzesi, Granada · Museo de la Alhambra','Elhamra’dan geometrik bir “alicatado” çini panosu','A geometric “alicatado” tile panel from the Alhambra','Alicatado: her renk ayrı bir çiniden kesilip mozaik gibi birleştirilir. Nasrî ustaları 14. yüzyılda bu yıldızları pergel ve cetvelle kurdu','Alicatado: each colour is cut from a separate tile and fitted together like a mosaic. Nasrid craftsmen built these stars with compass and ruler in the 14th century',fit='contain',d=38),
  fact('17','Bir düzlemi aynı desenin tekrarıyla döşemenin matematiksel olarak tam 17 simetri türü vardır (1891’de kanıtlandı). Ustalar bunların çoğunu yüzyıllar önce, kanıttan habersiz çinilere işlemişti','There are exactly 17 kinds of symmetry for covering a plane with a repeating pattern (proved in 1891). Craftsmen had used most of them in tiles centuries earlier, without any proof','Duvar kâğıdı grupları · Wallpaper groups','#142030','#04070c',d=34),
  rid('Bir zemini boşluk bırakmadan|tek bir düzgün çokgenle döşemek istiyorsun.|Kaç seçeneğin var?','You want to tile a floor with no gaps using one kind of regular polygon. How many choices do you have?','Yalnızca üç: üçgen, kare ve altıgen','Only three: triangles, squares and hexagons',hint='Köşede açılar 360°’ye tamamlanmalı · The corners must add up to 360°',sec=20,d=36),
]),
S(13,14,'Büyük Ustalardan: Hiroshige’nin Yağmuru, Karı ve Ayı · From the Great Masters: Hiroshige’s Rain, Snow & Moon',[
  art('hiro1','Utagawa Hiroshige, 1857','Shin-Ōhashi Köprüsü’nde Ani Sağanak','Sudden Shower over Shin-Ōhashi Bridge','Yağmur yüzlerce ince çizgiyle, iki farklı açıda basılmış. 1887’de Van Gogh bu baskıyı yağlıboyayla birebir kopyaladı','The rain is printed in hundreds of fine lines at two different angles. In 1887 Van Gogh copied this print in oils'),
  art('hiro2','Utagawa Hiroshige, 1857','Kameido’daki Erik Bahçesi','Plum Park in Kameido','Ön plandaki dev dal ile uzaktaki küçük insanlar: bu cesur kırpma Avrupalı ressamları çok etkiledi; Van Gogh bunu da kopyaladı','A huge branch in front, tiny people far away — this bold cropping greatly influenced European painters, and Van Gogh copied this one too'),
  art('hiro3','Utagawa Hiroshige, yaklaşık 1833–34 · about 1833–34','Kanbara’da Gece Karı','Night Snow at Kanbara','Tōkaidō Yolu’nun 53 Durağı dizisinden. İşin ilginci, Kanbara ılık bir sahil kasabası; orada böyle kar neredeyse hiç yağmaz','From the Fifty-three Stations of the Tōkaidō. Curiously, Kanbara is a mild coastal town where snow like this hardly ever falls'),
  q('Fırçamı Doğu’da bırakıp yola çıkıyorum;|Batı’nın ünlü yerlerini görmeye','I leave my brush in the East and set out on my journey, to see the famous places of the West','ink',d=40,lb='Ressamın Son Şiiri · The Painter’s Last Poem',by='Utagawa Hiroshige, 1858'),
  art('hiro4','Utagawa Hiroshige, 1858','Ryōgoku’da Havai Fişekler','Fireworks at Ryōgoku','Gece göğünde açılan tek bir havai fişek ve nehirdeki kayıklar. Whistler’ın Thames üzerindeki gece resimleri bu baskıdan izler taşır','A single firework bursting in the night sky above boats on the river — Whistler’s night paintings of the Thames carry traces of this print'),
  art('hiro5','Utagawa Hiroshige, 1857','Ueno’daki Ay Çamı','The Moon Pine at Ueno','Dalı kendi üstüne halka gibi kıvrılmış bir çam ve halkanın içinden görünen manzara: Edo’nun Yüz Ünlü Manzarası dizisinden','A pine whose branch curls into a ring, with the view seen through it — from One Hundred Famous Views of Edo'),
  fact('118','“Edo’nun Yüz Ünlü Manzarası” adına rağmen 118 baskıdan oluşur. Hiroshige diziyi bitiremeden 1858’de öldü; son baskıları öğrencisi tamamladı','Despite its name, “One Hundred Famous Views of Edo” has 118 prints. Hiroshige died in 1858 before finishing it, and his pupil completed the last ones','Bir dizinin hikâyesi · The story of a series','#1a2028','#05080b',d=32),
]),
S(14,15,'Gökyüzünün Harikaları: Jüpiter · Wonders of the Sky: Jupiter',[
  photo('jupiterhst','Jüpiter · Jupiter (Hubble Uzay Teleskobu, 2019 · Hubble Space Telescope)','Jüpiter’in renkli bulut kuşakları ve Büyük Kırmızı Leke','Jupiter’s coloured cloud belts and the Great Red Spot','Jüpiter, Güneş Sistemi’ndeki bütün öteki gezegenlerin toplamından iki buçuk kat daha ağır','Jupiter is two and a half times heavier than all the other planets in the Solar System put together',fit='contain',d=40),
  photo('redspot','Büyük Kırmızı Leke · the Great Red Spot (Juno, 2017, işlenmiş · processed)','Juno’nun yakından gördüğü dev fırtına','The giant storm seen up close by Juno','En az 190 yıldır gözlenen bir fırtına. Bugün Dünya’dan biraz geniş; yüz yıl önce içine üç Dünya sığardı','A storm watched for at least 190 years. Today it is a little wider than Earth — a century ago three Earths would have fitted inside',fit='contain',d=40),
  steps(SJ,'Dünya bir nohut olsaydı…','If Earth were a chickpea…',
    [['Dünya 1 cm’lik bir nohut olsaydı…','If Earth were a 1 cm chickpea…','🫘'],['Jüpiter 11 cm: bir greyfurt','Jupiter would be 11 cm — a grapefruit',''],['Güneş 1,1 metrelik bir top, nohuttan 117 metre ötede','The Sun would be a 1.1 m ball, 117 m from the chickpea',''],['Greyfurt Jüpiter ise Güneş’ten 611 metre uzakta dönerdi','And grapefruit Jupiter would circle 611 m from the Sun','🪐']],
    'Uzay çoğunlukla boşluktur: gezegenler bu kadar büyük bir sahnede minicik','Space is mostly empty — the planets are tiny on such a vast stage','#1a1a24','#05050a',gap=8,d=54),
  photo('junopole','Jüpiter’in güney kutbu · Jupiter’s south pole (Juno, 2017, işlenmiş · processed)','Güney kutbunun üzerinde birbirine dokunan dev kasırgalar','Giant cyclones touching each other over the south pole','Juno, kutuplarda düzenli desenler hâlinde dizilmiş kasırgalar buldu: kuzeyde sekiz, güneyde beş-altı; her biri neredeyse bir kıta büyüklüğünde','Juno found cyclones arranged in regular patterns at the poles — eight in the north, five or six in the south, each almost the size of a continent',fit='contain',d=38),
  photo('io','Io · Jüpiter’in uydusu · a moon of Jupiter (Galileo)','Kükürtle sarıya, turuncuya boyanmış Io','Io, painted yellow and orange by sulphur','Güneş Sistemi’nin volkanik olarak en etkin yeri: Jüpiter’in çekimi Io’yu sürekli sıkıp gevşetir, içini ısıtır; yüzlerce yanardağ püskürür','The most volcanically active place in the Solar System — Jupiter’s pull keeps squeezing and relaxing Io, heating it inside; hundreds of volcanoes erupt',fit='contain',d=38),
  photo('europa','Europa · Jüpiter’in uydusu · a moon of Jupiter (Galileo, gerçeğe yakın renk · near-true colour)','Çatlaklarla örülmüş buz yüzeyiyle Europa','Europa with its ice surface criss-crossed by cracks','Buzun altında tuzlu bir okyanus olduğu düşünülüyor; içindeki su, Dünya’daki bütün okyanusların iki katı olabilir','A salty ocean is thought to lie beneath the ice — it may hold twice as much water as all of Earth’s oceans',fit='contain',d=38),
  rid('1610’da Galileo teleskobunu Jüpiter’e çevirdi.|Ne gördü?','In 1610 Galileo turned his telescope to Jupiter. What did he see?','Etrafında dönen dört uydu: Io, Europa, Ganymede ve Callisto. Her şeyin Dünya’nın çevresinde dönmediğinin ilk kanıtlarından biri','Four moons circling it — Io, Europa, Ganymede and Callisto. One of the first proofs that not everything goes round the Earth',sec=18,d=36),
]),
S(15,16,'Göz Oyunları: İki Anlamlı Şekiller · Tricks of the Eye: Pictures With Two Meanings',[
  g('hzrubin',d=50),
  g('hznecker',d=50),
  fact('Şekil ve zemin · Figure & ground','Beyin bir görüntüye bakınca önce neyin “şey”, neyin “arka plan” olduğuna karar verir. Bu kararı aynı anda iki türlü veremez; bu yüzden iki anlamlı şekiller gidip gelir','When the brain looks at a picture, it first decides what is the “thing” and what is the background. It can’t make that choice both ways at once — so two-way pictures flip back and forth','Gestalt psikolojisi · Gestalt psychology','#1a1d22','#050608',d=32),
  g('hzkoffka',d=56),
  rid('Ördek mi, tavşan mı?|1892’de bir Alman dergisinde yayımlanan çizimde|hangisini gördüğünü ne belirler?','Duck or rabbit? In a drawing published in a German magazine in 1892, what decides which one you see?','Çoğu zaman beklentin! Paskalya’da çocukların çoğu önce tavşanı, ekimde ise önce ördeği görüyor','Often your expectation! At Easter most children see the rabbit first; in October, the duck',sec=20,d=38),
]),
S(16,17,'Zekice Düşünce: Königsberg’in Yedi Köprüsü · Clever Thinking: The Seven Bridges of Königsberg',[
  g('hzeuler',d=90),
  photo('konigsberg','Königsberg, 1652 (Merian gravürü · Merian engraving)','Pregel Nehri, iki ada ve yedi köprüyle Königsberg şehri','The city of Königsberg with the Pregel river, two islands and seven bridges','Şehrin halkı pazar yürüyüşlerinde her köprüden bir kez geçmeyi dener, hiç başaramazdı','On Sunday walks the townspeople would try to cross every bridge once — and never managed it',fit='contain',d=38),
  photo('euler','Leonhard Euler (1707–1783), Jakob Emanuel Handmann, 1753','İsviçreli matematikçi Leonhard Euler’in portresi','A portrait of the Swiss mathematician Leonhard Euler','Tarihin en üretken matematikçilerinden biri: neredeyse tamamen kör olduktan sonra da yazdırarak yüzlerce çalışma yaptı','One of the most productive mathematicians in history — even after going almost completely blind he kept dictating hundreds of works',fit='contain',d=36),
  steps(CT,'Bir bulmacadan bugünün haritalarına','From a puzzle to today’s maps',
    [['1736: Euler, köprü sorusunun cevabının haritada değil, bağlantılarda olduğunu görür','1736: Euler sees that the answer lies not in the map but in the connections','🌉'],['Kara parçaları nokta, köprüler çizgi olur: ilk “çizge” (graf)','Land becomes dots, bridges become lines — the first “graph”',''],['Bugün aynı fikir internetin, elektrik şebekelerinin ve sosyal ağların haritasını çıkarır','Today the same idea maps the internet, power grids and social networks',''],['Telefonundaki yol tarifi de bir çizge üzerinde en kısa yolu arar','The directions on your phone search for the shortest path on a graph too','📱']],
    'Bazen bir sorunu çözmenin yolu, gereksiz ayrıntıları silmektir','Sometimes the way to solve a problem is to erase the details that don’t matter','#17222a','#05080b',gap=8,d=56),
  fact('Kaliningrad','Königsberg bugün Rusya’da, adı Kaliningrad. Euler’in yedi köprüsünden yalnızca ikisi onun zamanından kalma; bazıları savaşta yıkıldı','Königsberg is now Kaliningrad, in Russia. Only two of Euler’s seven bridges survive from his time — some were destroyed in the war','Şehrin bugünü · The city today','#17222a','#05080b',d=30),
  rid('Kalemi kâğıttan kaldırmadan ve|hiçbir çizgiden iki kez geçmeden|açık bir zarf çizebilir misin?','Can you draw an open envelope without lifting your pen or going over any line twice?','Evet, ama yalnızca alttaki iki köşeden birinden başlarsan! Tek sayıda çizginin buluştuğu iki köşe oralar','Yes — but only if you start at one of the two bottom corners! Those are the two corners where an odd number of lines meet',hint='Euler’in kuralını hatırla · Remember Euler’s rule',sec=22,d=40),
]),
S(17,18,'DJ Taş · Caz House Lounge · Jazz House Lounge — Lizbon’da akşam · an evening in Lisbon',[
  card('miradouro','DJ Taş · Sadece Sen — '+REAL+' · Lizbon, Portekiz · Lisbon, Portugal',[['DJ Taş',7.2],['Bu akşam · Tonight',3.4]],
   'Üç perdelik bir akşam: Caz House Lounge → Gün Batımı (19:00) → Gece (22:00). Müzik HomePod’da','An evening in three acts: Jazz House Lounge → Sunset (19:00) → Night (22:00). Music on the HomePod',d=32),
  photo('lisbontram','28 numaralı tramvay · Tram 28, Alfama','Alfama’nın dar sokağında sarı tramvay','The yellow tram in a narrow Alfama street','Lizbon’un yokuşlu sokaklarında 1930’lardan kalma ahşap tramvaylar hâlâ çalışıyor','Wooden trams from the 1930s still run up and down Lisbon’s steep streets',d=38,act=A1),
  g('hzlorenz',d=60),
  photo('alfama','Alfama, Lizbon · Lisbon','Gece Alfama’da sokak lambalarının altında taş basamaklar','Stone steps under the street lamps of Alfama at night','Alfama, 1755 depreminden büyük ölçüde sağ çıkan tek eski mahalle; sokakları hâlâ ortaçağ planını izler','Alfama is the only old quarter that largely survived the 1755 earthquake — its lanes still follow the medieval plan',d=38,act=A1),
  fact('Saudade','Portekizcede “saudade”: uzaktaki, belki hiç dönmeyecek bir şeye duyulan tatlı-acı özlem. Lizbon’un fado şarkıları bu duyguyla söylenir; fado 2011’de UNESCO listesine girdi','In Portuguese, “saudade” is a bittersweet longing for something far away that may never return. Lisbon’s fado songs are sung with this feeling — fado joined the UNESCO list in 2011','Bir kelime, bir şehir · One word, one city','#14202a','#04070a',d=32),
  photo('belem','Belém Kulesi, Lizbon · Belém Tower, Lisbon','Akşam ışığında Tejo kıyısındaki Belém Kulesi','Belém Tower on the bank of the Tagus in the evening light','16. yüzyılın başında limanı korumak için yapıldı; keşif gemileri okyanusa buradan açıldı','Built in the early 16th century to guard the harbour — the ships of the age of discovery set out to sea from here',d=38,act=A1),
],pre='dj'),
S(18,19,'Caz House Lounge · Jazz House Lounge — Villa Fikri: Terasta Film Gecesi · Villa Idea: Film Night on the Terrace',[
  villa('opencinema','Agistri, Yunanistan · Greece','Yazın terasta açık hava sineması: beyaz bir perde, birkaç rahat sandalye ve battaniyeler','An open-air cinema on the terrace in summer — a white screen, a few comfy chairs and blankets','İpucu: filme hava tamamen karardıktan sonra başla, gün batımından yaklaşık 40 dakika sonra. Taş duvar yerine düz, mat beyaz bir perde görüntüyü çok daha keskin yapar','Tip: start the film once it is fully dark, about 40 minutes after sunset. A flat matte-white screen instead of the stone wall makes the picture much sharper',act=A1),
  villa('campfire','Finlandiya · Finland','Filmden önce ateş başında: kıvılcımlar, sıcak içecekler ve sohbet','Before the film, by the fire — sparks, hot drinks and conversation','Ateşi rüzgârın perdeye değil, oturanların arkasına doğru estiği tarafa kur; duman ne yüzlere ne de görüntüye gitsin','Build the fire where the wind blows away from both the screen and the guests — so the smoke goes neither into faces nor into the picture',act=A1),
  q('Gönülden gönüle|yol vardır','There is a road from heart to heart','clay',d=38,lb='Atasözü · Proverb',by='Türk atasözü · Turkish proverb'),
  villa('popcorn','ev yapımı patlamış mısır · homemade popcorn','Büyük bir kasede taze patlamış mısır','A big bowl of fresh popcorn','Mısır tanesinin içindeki az miktar su ısınınca buhara döner; basınç kabuğu yaklaşık 180 °C’de patlatır ve tane ters yüz olur','The tiny bit of water inside each kernel turns to steam — at about 180 °C the pressure bursts the hull and the kernel turns inside out',act=A1),
  g('hztimes',d=56),
  fact('24 kare · frames','Bir sinema filmi saniyede 24 kare gösterir; projektör her kareyi iki ya da üç kez yakıp söndürür ki göz titreme görmesin','A cinema film shows 24 frames a second — the projector flashes each frame two or three times so the eye sees no flicker','Sinemanın sırrı · The secret of cinema','#1a1822','#06050a',d=30),
],pre='dj'),
S(19,20,'Gün Batımı · Sunset — Boğaziçi · the Bosphorus',[
  card('maidenstower','DJ Taş · 2. Perde · Act 2 — '+REAL+' · Kız Kulesi, İstanbul · Maiden’s Tower, Istanbul',[['Gün Batımı',6.4],['Sunset',3.6]],
   'Liste değişti: şimdi “Sadece Sen Sunset” çalıyor','The playlist has changed — now playing “Sadece Sen Sunset”',d=30),
  photo('bosphorusbr','15 Temmuz Şehitler Köprüsü · the Bosphorus Bridge, from Cihangir','Batan güneşte Boğaz Köprüsü ve iki kıta','The Bosphorus Bridge and two continents at sunset','1973’te açıldığında dünyanın en uzun dördüncü asma köprüsüydü; Avrupa ile Asya’yı birbirine bağlar','When it opened in 1973 it was the fourth-longest suspension bridge in the world — it links Europe and Asia',d=38,act=A2),
  photo('rumelihisari','Rumeli Hisarı, İstanbul','Boğaz’ın kıyısında Rumeli Hisarı’nın kuleleri','The towers of Rumeli Hisarı on the shore of the Bosphorus','Fatih Sultan Mehmed 1452’de, İstanbul’un fethinden önce, yaklaşık dört ayda yaptırdı','Mehmed the Conqueror had it built in about four months in 1452, before the conquest of Istanbul',d=38,act=A2),
  g('hztree',d=56),
  photo('eminonuferry','Boğaz’da vapur · A ferry on the Bosphorus','Gün batımında Boğaz’dan geçen bir vapur','A ferry crossing the Bosphorus at sunset','Boğaz yaklaşık 31 km uzunluğunda; en dar yerinde iki kıyı arası yalnızca 700 metre kadar','The Bosphorus is about 31 km long — at its narrowest the two shores are only about 700 m apart',d=38,act=A2),
  fact('İki akıntı · Two currents','Boğaz’da yüzeydeki su Karadeniz’den Marmara’ya akar; derinde ise daha tuzlu, daha ağır su ters yöne, Karadeniz’e doğru akar','In the Bosphorus the surface water flows from the Black Sea to the Marmara — while deep down, saltier, heavier water flows the other way, into the Black Sea','Boğaz’ın sırrı · A Bosphorus secret','#20181a','#07050a',d=30),
],pre='dj'),
S(20,21,'Gün Batımı · Sunset — savanada akşam · evening on the savanna',[
  photo('serengeti','Serengeti, Tanzanya · Tanzania','Güneşin önünde tek başına bir akasya ağacı','A lone acacia tree against the sun','Her yıl yaklaşık bir buçuk milyon antilop (gnu) yağmurların peşinden Serengeti ile Masai Mara arasında daire çizerek göç eder','Every year about one and a half million wildebeest follow the rains in a great circle between the Serengeti and the Masai Mara',d=40,act=A2),
  photo('giraffes','Zürafa · Giraffe','Akşam ışığında yürüyen bir zürafa','A giraffe walking in the evening light','Zürafanın boynu iki metreyi bulur ama içinde bizimki kadar, yalnızca yedi omur vardır','A giraffe’s neck can reach two metres, yet it has just seven vertebrae — the same as ours',d=38,act=A2),
  photo('kilimanjaro','Kilimanjaro, Tanzanya · Tanzania','Gün batımında Kilimanjaro’nun karlı zirvesi','Kilimanjaro’s snowy summit at sunset','5.895 metreyle Afrika’nın en yüksek dağı ve dünyanın tek başına yükselen en yüksek dağı; ekvatora çok yakın olmasına rağmen zirvesi buzlu','At 5,895 m it is Africa’s highest mountain and the tallest free-standing mountain on Earth — its summit is icy even though it lies close to the equator',d=40,act=A2),
  photo('masaimara','Masai Mara, Kenya','Masai Mara’da kızıl bir gün batımı','A red sunset over the Masai Mara','Ekvatorda gün batımı çok hızlıdır: güneş ufka dik indiği için alacakaranlık yalnızca 20 dakika kadar sürer','Sunsets on the equator are fast — the sun drops straight down to the horizon, so twilight lasts only about 20 minutes',d=40,act=A2),
  rid('Hangi hayvan|zıplayamaz?','Which animal cannot jump?','Fil! Dört ayağından en az biri hep yerde kalır','The elephant! At least one of its four feet always stays on the ground',sec=16),
],pre='dj'),
S(21,22,'Gün Batımı · Sunset — Hint Okyanusu kıyıları · Indian Ocean shores',[
  photo('zanzibar','Zanzibar, Tanzanya · Tanzania','Gün batımında üçgen yelkenli bir dhow','A dhow with its triangular sail at sunset','Dhow’lar yüzyıllardır muson rüzgârlarıyla seyreder: kışın Arabistan’dan Afrika’ya, yazın geri','For centuries dhows have sailed with the monsoon winds — to Africa from Arabia in winter, and back in summer',d=40,act=A2),
  photo('seychelles','Anse Source d’Argent, La Digue, Seyşeller · Seychelles','Pembe granit kayalar ve sığ turkuaz su','Pink granite boulders and shallow turquoise water','Bu granitler yaklaşık 750 milyon yıllık: Seyşeller, bir zamanlar Hindistan ile Madagaskar arasında kalmış eski bir kıta parçası','These granites are about 750 million years old — the Seychelles are a fragment of an old continent once caught between India and Madagascar',d=40,act=A2),
  q('Hayat, tutunmak ile bırakmak|arasında bir dengedir','Life is a balance between holding on and letting go','sea',d=38),
  photo('maldives','Rannalhi, Maldivler · the Maldives','Maldivler’de denize inen güneş','The sun going down into the sea in the Maldives','Dünyanın en alçak ülkesi: adaların çoğu deniz seviyesinden yalnızca bir iki metre yüksekte','The lowest country in the world — most of its islands rise only a metre or two above the sea',d=38,act=A2),
  photo('lemorne','Le Morne Brabant, Morityus · Mauritius','Lagünün kıyısında yükselen Le Morne dağı','Le Morne mountain rising above the lagoon','Kaçan köleler bu sarp dağa sığındı; bugün özgürlüğün simgesi ve UNESCO Dünya Mirası','Escaped slaves took refuge on this steep mountain — today it is a symbol of freedom and a UNESCO World Heritage site',d=38,act=A2),
  rid('Suda doğar,|suda ölür.|Nedir?','It is born in water and dies in water. What is it?','Tuz!','Salt!',sec=14),
],pre='dj'),
S(22,23,'Gece · Night — kar altında Japonya · Japan under snow (sakin · calm)',[
  card('ginzan','DJ Taş · 3. Perde · Act 3 — '+REAL+' · Ginzan Onsen, Yamagata',[['Gece',6.6],['Night',3.6]],
   'Şimdi “Sadece Sen Night” çalıyor: daha yumuşak, daha sakin','Now playing “Sadece Sen Night” — softer and calmer',d=30),
  photo('kenrokuen','Kenroku-en, Kanazawa','Kenroku-en bahçesinde karla örtülü taş fener','A stone lantern under snow in Kenroku-en garden',d=44,act=A3,quiet=1),
  photo('hirosaki','Hirosaki Kalesi · Hirosaki Castle','Kar festivalinde ışıklarla aydınlanan Hirosaki Kalesi','Hirosaki Castle lit up for the snow festival',d=44,act=A3,quiet=1),
  q('Ayrılık yalnızca gözleriyle sevenler içindir;|gönülle sevenler için ayrılık yoktur','Goodbyes are only for those who love with their eyes — for those who love with heart and soul there is no separation','night',d=40),
  photo('gionnight','Gion, Kyoto','Gion’da gece yanan kâğıt fenerler','Paper lanterns glowing at night in Gion',d=44,act=A3,quiet=1),
],pre='dj'),
S(23,26,'Gece · Night — Laponya’da kış · winter in Lapland (sakin · calm)',[
  g('hzbuz',d=150),
  photo('tykky','Pallas-Yllästunturi, Laponya · Lapland','Karın ağırlığıyla heykele dönmüş ağaçlar','Trees turned into sculptures by the weight of snow',d=46,act=A3,quiet=1),
  photo('frostwindow','Camda buz kristalleri · Ice crystals on a window','Gece soğuğunda camda büyüyen buz çiçekleri','Frost flowers growing on a window in the night cold',d=44,act=A3,quiet=1),
  g('hzaurora',d=90),
  photo('reindeer','Laponya · Lapland','Karlı ormanda bir ren geyiği kızağı','A reindeer sled in the snowy forest',d=44,act=A3,quiet=1),
  photo('lappcabin','Laponya’da alacakaranlık · twilight in Lapland','İyi geceler · Good night','Good night',d=46,act=A3,quiet=1),
],pre='dj'),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-27.py. 17:00–02:00 = DJ Taş evening (Jazz House Lounge → Sunset 19:00 → Night 22:00, synced with the HomePod playlists; stills only at night, no video). Content log: used-content.md',sets=sets),open(os.path.join(HERE,'%s.json'%DATE),'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'][:60])
