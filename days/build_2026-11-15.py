# Builds /workspace/tv-pages/days/2026-11-15.json (hourly sets 09:00-02:00). Pattern from build_2026-11-14.py. Sunday: relaxed & beautiful.
import json,os
DATE='2026-11-15'; REV=64; NEXT='2026-11-16'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-15.json')))
FIX={'Stephen Morris from Toronto':'Stephen Morris','Bernard DUPONT from FRANCE':'Bernard Dupont','Julia Maudlin':'Julia Maudlin','Alias 0591 from the Netherlands':'Alias 0591','Pseudopanax at English Wikipedia':'Pseudopanax (en.wikipedia)','Unknown authorUnknown author':'bilinmeyen fotoğrafçı · unknown photographer (State Library of NSW)','H. Raab (User:Vesta)':'H. Raab','Gmihail at Serbian Wikipedia':'Gmihail (sr.wikipedia)'}
def artist(k):
    a=C[k]['artist']
    for f,t in FIX.items():
        if a.startswith(f[:18]): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace(' rs','')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,pos=None):
    it=dict(k='hzphoto',d=d,f='m/h15-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it
def villa(k,where,tr,en,fact,facte,fit=None):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=42)
    it['lb']='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where
    return it
def art(k,tr,en,fact,facte,d=44):
    it=photo(k,'',tr,en,fact,facte,fit='contain',d=d)
    it['lb']='Gerçek Eser · Real Artwork'
    it['cr']='Eser · Artwork: %s · kamu malı · public domain · Wikimedia Commons'%artist(k)
    return it
def q(tr,en,pal,d=44): return dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
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
    it=dict(k='hzguess',d=d,f='m/h15-%s.jpg'%k,lb='Bul Bakalım · Can You Spot It? — '+REAL+' · '+where,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr=cr(k))
    if hint: it['hint']=hint
    return it
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
sets=[
S(9,10,'Pazar Sabahı · Sunday Morning',[
  photo('yayla','Kadırga Yaylası · Trabzon–Giresun','Kadırga Yaylası — bulutların hemen altında bir pazar sabahı','Kadırga plateau — a Sunday morning just below the clouds','Trabzon ile Giresun’un sınırında; her temmuz iki ilin yaylacıları burada büyük bir şenlikte buluşur','On the Trabzon–Giresun border — every July highlanders from both provinces meet here for a big festival',d=40),
  q('Ruhunu heyecanlandıran|her çağrıya cevap ver','Respond to every call that excites your spirit','clay',d=44),
  photo('kuzalan','Dereli, Giresun','Kuzalan Şelalesi — ormanın içinde basamak basamak inen su','Kuzalan Waterfall — water stepping down through the forest','Dereli’de, ladin ve kayın ağaçlarının arasında; yazın serin bir mola, sonbaharda renk cümbüşü','In Dereli, among spruce and beech — a cool stop in summer, a riot of colour in autumn',fit='contain',d=40),
  fact('Pazar','Pazar gününün adı, o gün kurulan pazardan gelir','Sunday is called “Pazar” in Turkish after the market held that day','Kelime Farsça “bâzâr”dan; eskiden “bazar günü” denirdi · From the Persian “bāzār” — it used to be called “bazar günü”, market day','#2a2218','#080604',d=30),
  photo('macahel','Camili, Borçka, Artvin','Macahel (Camili) — Türkiye’nin ilk UNESCO biyosfer rezervi','Macahel (Camili) — Türkiye’s first UNESCO biosphere reserve','2005’te biyosfer rezervi oldu; ormanları el değmemiş, arıları saf Kafkas arısı olarak korunuyor','Named a biosphere reserve in 2005 — its forests are untouched and its bees are protected as pure Caucasian honeybees',d=40),
  rid('Her ayda en az<br>kaç Pazar günü vardır?','What is the smallest number of Sundays any month can have?','4! En kısa ay bile 28 gün, yani tam 4 hafta','4 — even the shortest month has 28 days: exactly four weeks',sec=16,c1='#22301f',c2='#050805'),
]),
S(10,11,'Yaşayan Sanat: Akışkanlar · Living Art: Fluids',[
  g('hzmeta',d=75),
  photo('ferrofluid','Ferroakışkan · Ferrofluid','Mıknatısın üstünde diken diken olan bir sıvı: ferroakışkan','A liquid that turns spiky over a magnet: ferrofluid','1963’te NASA’da, roket yakıtını yerçekimsiz ortamda yönlendirmek için icat edildi — lav lambasıyla aynı yıl','Invented at NASA in 1963 to steer rocket fuel in zero gravity — the same year as the lava lamp',d=38),
  photo('bubble2','Sabun Köpüğü · Soap Bubble','Bir sabun köpüğünün yüzeyinde dans eden renkler','Colours dancing on the skin of a soap bubble','Renkler zarın kalınlığından gelir; zar bir saç telinden yüzlerce kat incedir. Patlamadan hemen önce o kadar incelir ki kararır','The colours come from the film’s thickness — hundreds of times thinner than a hair. Just before it pops it gets so thin it turns dark',d=38),
  photo('bzreaction','Kimyasal Saat · Chemical Clock','Kendi kendine halkalar çizen bir karışım: Belousov–Zhabotinsky tepkimesi','A mixture that draws its own rings: the Belousov–Zhabotinsky reaction','Boris Belousov 1950’lerde keşfettiğinde dergiler “imkânsız” diyerek makalesini reddetti; bugün doğadaki desenleri anlamak için inceleniyor','When Boris Belousov found it in the 1950s, journals rejected his paper as “impossible” — today it is studied to understand patterns in nature',d=40),
  rid('Bir koşu yarışında<br>ikinciyi geçtin.<br>Kaçıncı oldun?','In a race you overtake the runner in second place. What place are you in now?','İkinci! Birinci olmak için birinciyi geçmen gerekirdi','Second — to be first you would have to pass the leader',sec=16,c1='#2a1f33',c2='#07050a'),
]),
S(11,12,'Galeri: Bir Pazar Öğleden Sonrası · Gallery: A Sunday Afternoon',[
  art('grandejatte','La Grande Jatte Adası’nda Bir Pazar Öğleden Sonrası — Georges Seurat, 1884–86','A Sunday on La Grande Jatte — Georges Seurat, 1884–86','Seurat bu tabloyu yaklaşık iki yılda, renkleri karıştırmadan yan yana koyduğu küçük noktalarla yaptı; renkleri gözümüz karıştırıyor','Seurat spent about two years on it, placing tiny dots of unmixed colour side by side — our eyes do the mixing'),
  art('boating','Kayıkçıların Öğle Yemeği — Pierre-Auguste Renoir, 1880–81','Luncheon of the Boating Party — Pierre-Auguste Renoir, 1880–81','Seine kıyısında bir terasta Renoir’ın arkadaşları; sağ altta ters sandalyede oturan genç adam ressam Gustave Caillebotte','Renoir’s friends on a terrace by the Seine — the young man astride a chair at lower right is the painter Gustave Caillebotte'),
  art('rainyday','Paris Sokağı, Yağmurlu Gün — Gustave Caillebotte, 1877','Paris Street; Rainy Day — Gustave Caillebotte, 1877','İşte Caillebotte’un kendi tablosu: şemsiyeler, ıslak kaldırım taşları ve yeni yapılmış geniş Paris caddeleri','And here is Caillebotte’s own painting — umbrellas, wet cobblestones and the newly built wide streets of Paris'),
  art('breezing','Rüzgârı Arkaya Almak — Winslow Homer, 1873–76','Breezing Up (A Fair Wind) — Winslow Homer, 1873–76','Bir baba ve üç çocuk, dolgun bir yelkenle eve dönüyor; Homer’ın en sevilen deniz tablolarından','A father and three boys heading home under a full sail — one of Homer’s best-loved sea paintings'),
  art('cassatt','Kayık Gezisi — Mary Cassatt, 1893–94','The Boating Party — Mary Cassatt, 1893–94','Cassatt bu sahneyi Fransız Rivierası’nda, Antibes’te geçirdiği bir kışta çizdi','Cassatt painted this scene during a winter spent at Antibes on the French Riviera'),
  steps('Küçük Meydan Okuma · Little Challenge','Bir tabloya “yavaş bakmayı” dene: 3 dakika, tek tablo','Try “slow looking”: three minutes, one painting',
    [['Önce uzaktan bütününe bak: ilk ne dikkatini çekiyor?','First look at the whole: what catches your eye first?','①'],['Bir kişiyi seç: şu an ne düşünüyor olabilir?','Pick one person — what might they be thinking right now?','②'],['Işık nereden geliyor? Gölgeler hangi yöne düşüyor?','Where does the light come from? Which way do the shadows fall?','③'],['Bir rengi seç ve tablonun içinde takip et','Choose one colour and follow it around the canvas','④']],
    'Müzelerde insanlar bir tabloya ortalama yalnızca 30 saniye kadar bakıyor. Üç dakika, bambaşka bir tablo gösterir','In museums people look at a painting for only about 30 seconds on average — three minutes shows you a different picture','#262019','#070605',gap=7,d=52),
]),
S(12,13,'Simetri · Symmetry',[
  g('hzkaleido',d=72),
  photo('selimiye','Edirne','Selimiye Camii’nin kubbesi — içeriden bakınca bir kaleydoskop','The dome of the Selimiye Mosque — a kaleidoscope seen from below','Mimar Sinan 80 yaşını geçmişken bitirdi (1575) ve onu “ustalık eserim” diye anlattı; kubbenin çapı yaklaşık 31 metre','Mimar Sinan finished it in his eighties (1575) and called it his masterpiece — the dome is about 31 m across',d=40),
  photo('fin','Bağ-ı Fin, Kaşan · Fin Garden, Kashan','Bağ-ı Fin köşkünün tavanı — taşa ve sıvaya işlenmiş yıldızlar','The ceiling of a pavilion in the Fin Garden — stars worked in plaster','Kaşan’daki bu bahçe, UNESCO listesindeki “İran Bahçesi” örneklerinden biri','This garden in Kashan is one of the “Persian Garden” sites on the UNESCO list',d=38),
  photo('aloe','Sarmal aloe · Spiral aloe','Kendi etrafında kusursuz bir sarmal çizen bitki: sarmal aloe','A plant that draws a perfect spiral around itself: the spiral aloe','Lesotho dağlarına özgü; yaprakları beş sıra halinde, kimi bitkide saat yönünde, kimisinde tersine döner','Native to the mountains of Lesotho — its leaves wind in five rows, clockwise on some plants and anticlockwise on others',d=38),
  photo('morpho','Mavi morfo kelebeği · Blue morpho','Mavi morfo kelebeği — kanatlar birbirinin aynası','A blue morpho butterfly — each wing a mirror of the other','Bu mavide hiç boya yok: kanattaki minicik pullar ışığı kırıp yalnızca maviyi geri yansıtıyor','There is no blue pigment here — tiny scales on the wings bend the light and reflect only blue',d=38),
  q('Evrendeki her şey senin içinde;|her şeyi kendinden iste','Everything in the universe is within you — ask all of it from yourself','ink',d=44),
]),
S(13,14,'Düşünce Deneyleri · Thought Experiments',[
  steps('Düşünce Deneyi · Thought Experiment','Kum Yığını Paradoksu: tek bir tane neyi değiştirir?','The heap paradox: what difference does one grain make?',
    [['Önünde bir kum yığını var','In front of you is a heap of sand','⛰'],['Bir tane alıyorsun: hâlâ yığın mı? Elbette','You take away one grain — still a heap? Of course',''],['Bir tane daha… bir tane daha…','Another grain… and another…',''],['Sonunda tek bir tane kalıyor: bu yığın değil','At last one grain is left — that is not a heap',''],['Peki yığın hangi tanede “yığın” olmaktan çıktı?','So which grain was the one that stopped it being a heap?','?']],
    'Milattan önce 4. yüzyılda Miletli Eubulides sordu; “uzun”, “yaşlı”, “sıcak” gibi sınırı belirsiz bütün kelimeler aynı soruyu taşır','Eubulides of Miletus asked it in the 4th century BC — every word with a fuzzy edge, like “tall”, “old” or “warm”, carries the same puzzle','#2c2418','#080604',gap=6.5,d=56),
  photo('dunes','Erg Chebbi, Fas · Morocco','Sahra’nın kenarında kum denizi: Erg Chebbi','A sea of sand at the edge of the Sahara: Erg Chebbi','Rüzgârın yığdığı kum tepeleri yer yer 150 metreye ulaşıyor — milyarlarca tanenin her biri yığının bir parçası','Wind-built dunes here reach up to about 150 m — billions of grains, each one part of the heap',d=38),
  steps('Düşünce Deneyi · Thought Experiment','Sonsuz Maymun: rastgele tuşlara basan bir maymun Hamlet’i yazabilir mi?','The infinite monkey: could a monkey hitting random keys type Hamlet?',
    [['Bir maymun, bir daktilo ve sonsuz zaman','One monkey, one typewriter and endless time','🐒'],['Her tuşa rastgele basıyor','It hits every key at random',''],['Sadece “HAMLET” kelimesi için şans: 309 milyonda 1','The chance of just the word “HAMLET”: 1 in 309 million',''],['Bütün oyun için gereken süre, evrenin yaşından trilyonlarca kat uzun','For the whole play it would take trillions of times the age of the universe',''],['Ama zaman gerçekten sonsuzsa… bir gün mutlaka yazar','But if time is truly endless… one day it will','∞']],
    'Fransız matematikçi Émile Borel 1913’te anlattı: “olası” ile “mümkün” arasındaki uçurumu gösterir','French mathematician Émile Borel described it in 1913 — it shows the gulf between “likely” and “possible”','#1c2430','#04060a',gap=6.5,d=56),
  photo('macaque','Nagano, Japonya · Japan','Kışın sıcak su kaynağında ısınan Japon makakları','Japanese macaques warming up in a hot spring in winter','Nagano’daki bu maymunlar karlı kış günlerinde sıcak suya girer; dünyanın en kuzeyde yaşayan maymunları onlar','These monkeys in Nagano slip into hot water on snowy days — they are the most northerly living monkeys on Earth',d=38),
  steps('Düşünce Deneyi · Thought Experiment','Buridan’ın Eşeği: iki eşit saman yığınının tam ortasında aç bir eşek…','Buridan’s donkey: a hungry donkey exactly halfway between two identical haystacks…',
    [['Sol yığın da sağ yığın da aynı büyüklükte','The left haystack and the right are the same size',''],['İkisi de aynı uzaklıkta, aynı güzel kokuyor','Same distance, same lovely smell',''],['Eşeğin birini seçmesi için hiçbir sebep yok','The donkey has no reason at all to choose one',''],['Karar veremiyor… ve aç kalıyor','It cannot decide… and goes hungry','🫏']],
    'Ders: Bazen hangisini seçtiğin değil, bir seçim yapman önemlidir — pazar günü ne yapacağına karar vermek gibi','The lesson: sometimes what matters is not which one you pick, but that you pick — like deciding what to do on a Sunday','#22301f','#050805',gap=6.5,d=50),
  rid('Bir odanın dört köşesinde<br>birer kedi oturuyor.<br>Her kedinin karşısında 3 kedi var.<br>Odada kaç kedi var?','A cat sits in each of the four corners of a room. Each cat sees three cats facing it. How many cats are in the room?','4 kedi!','Just 4 cats.',sec=18,c1='#2a2420',c2='#070605'),
]),
S(14,15,'Villa Fikirleri: Suyun Sesi · Villa Ideas: The Sound of Water',[
  villa('myrtles','Elhamra, Granada','Mersin Avlusu: uzun, durgun bir havuz bütün cepheyi ikiye katlıyor','The Court of the Myrtles: one long, still pool doubles the whole facade','Villa için ders: dar ve sığ bir yansıma havuzu bile, akşam ışıklarıyla evi suyun içinde ikinci kez gösterir','Lesson for the villa: even a narrow, shallow reflecting pool shows the house a second time in the water at night'),
  villa('acequia','Generalife, Granada','Generalife’in Su Arkı Avlusu: yolun iki yanından kemer çizen ince su fıskiyeleri','The Generalife’s Court of the Water Channel: thin jets arching from both sides of a path','Fıskiyeler alçak ve ince olunca su sıçramaz, sadece hafif bir şırıltı duyulur — oturma köşesinin yanına çok yakışır','Low, fine jets don’t splash — you hear only a soft murmur, perfect beside a seating corner',fit='contain'),
  villa('tsukubai2','Ryōan-ji, Kyoto','Taş bir su teknesi (tsukubai): bambu oluktan damlayan su','A stone water basin (tsukubai) fed by a bamboo spout','Ortadaki kare boşluğun çevresindeki dört işaret “Ben yalnızca yetinmeyi bilirim” diye okunur — girişe yakışacak sakin bir karşılama','The four signs around the square hole read “I only know contentment” — a calm welcome for an entrance',fit='contain'),
  steps('Villa Fikri · Villa Idea','Villa için küçük bir su köşesi: nereye, nasıl?','A small water corner for the villa — where and how?',
    [['Yer: oturma köşesine 3–5 metre — ses duyulsun ama sohbeti bastırmasın','Place: 3–5 m from the seating, so you hear it without drowning the conversation','📍'],['Ses: şelale gürlemesi değil, ince bir şırıltı','Sound: not a roaring cascade — a gentle trickle','〰'],['Pompa: suyu kendi içinde döndüren küçük bir devridaim pompası yeter','Pump: a small recirculating pump that reuses the same water is enough','♻'],['Gece: suyu yandan ya da alttan yumuşak, sıcak bir ışıkla aydınlat','Night: light the water softly and warmly from the side or below','✦']],
    'Trabzon kışı için not: soğuk gecelerden önce boruları boşaltıp pompayı içeri almak gerekir','A note for Trabzon winters: drain the pipes and bring the pump inside before the frosty nights','#14262a','#030708',gap=7,d=54),
  fact('6 km','Elhamra’nın havuzlarına su, yaklaşık 6 km yukarıdaki Darro Nehri’nden, yalnızca eğimle akan bir arkla geliyordu','The Alhambra’s pools were fed by a channel running about 6 km from the Darro River — powered by nothing but gravity','Kraliyet Arkı (Acequia Real), 13. yüzyıl · The Royal Channel, 13th century','#173032','#030809',d=30),
]),
S(15,16,'Göz Oyunları · Tricks of the Eye',[
  g('hzmib',d=60),
  guess('cuttlefish','Akvaryum · Aquarium','Bu fotoğrafta bir hayvan saklanıyor. Bulabilir misin?','An animal is hiding in this photo. Can you find it?','Ortada, kumla aynı desene bürünmüş yavru bir mürekkepbalığı!','In the middle — a baby cuttlefish wearing the exact pattern of the sand',hint='İpucu: ortaya yakın bak · Hint: look near the centre',sec=22),
  g('hzcorn',d=52),
  fact('3','Gözlerin her saniye yaklaşık 3 kez sıçrar; beyin aradaki bulanık anları siler, sen hiç fark etmezsin','Your eyes jump about 3 times every second — the brain erases the blurry moments in between, so you never notice','Bu sıçramalara “sakkad” denir · These jumps are called saccades','#1b2230','#05070b',d=30),
  rid('Doktor sana 3 hap verdi:<br>“Yarım saatte bir tane iç.”<br>Haplar kaç dakikada biter?','A doctor gives you 3 pills: “Take one every half hour.” How many minutes until they are gone?','60 dakika! İlki hemen, ikincisi 30., üçüncüsü 60. dakikada','60 minutes — the first right away, then at 30 and at 60',sec=20,c1='#1c2a30',c2='#040708'),
]),
S(16,17,'Bulut Seyri · Cloud Watching',[
  photo('lenticular','Titlis, İsviçre · Switzerland','Dağın üstünde duran mercek bulutları','Lens-shaped clouds parked over a mountain','Rüzgâr dağı aşınca dalgalanır; dalganın tepesinde bulut oluşur ve yerinden kıpırdamıyormuş gibi durur. Çoğu zaman UFO sanılır','Wind ripples as it crosses a mountain — a cloud forms on the wave crest and seems to hang still. Often mistaken for UFOs',d=38),
  photo('mammatus','Tulsa, ABD · USA · 1973','Gök kubbeden sarkan keseler: mammatus bulutları','Pouches hanging from the sky: mammatus clouds','Genellikle büyük bir fırtına bulutunun altında görülür; serin hava cepleri aşağı çöker','Usually seen beneath a big storm cloud — pockets of cool air sinking downwards',d=38),
  photo('kelvinhh','Kelvin–Helmholtz','Gökyüzünde kıvrılan dalgalar: Kelvin–Helmholtz bulutları','Waves curling across the sky: Kelvin–Helmholtz clouds','İki hava katmanı farklı hızla akınca sınırda deniz dalgası gibi kıvrımlar oluşur; çoğu birkaç dakika içinde kaybolur','When two layers of air flow at different speeds, the boundary curls like breaking sea waves — most vanish within minutes',d=38),
  photo('fallstreak','Delik bulut · Hole-punch cloud','Bulutta açılmış kocaman bir delik','A huge hole punched in a cloud','Bulutta donmadan soğumuş su damlaları vardır; bir uçak geçince bir anda buza döner ve aşağı düşerler — ortada bir pencere açılır','The cloud holds supercooled droplets — when a plane passes they suddenly freeze and fall, opening a window in the middle',d=38),
  steps('Küçük Meydan Okuma · Little Challenge','Bulut avı: bugün gökyüzüne iki dakika ayır','Cloud hunt — give the sky two minutes today',
    [['Terasa çık ya da pencereden bak','Step out on the terrace or look out of a window','☁'],['Bir bulutta bir hayvan ya da yüz bul','Find an animal or a face in a cloud',''],['Bulutlar hangi yöne gidiyor? Denizden mi, dağdan mı?','Which way are they moving — from the sea or from the mountains?',''],['Bugün öğrendiğin bulutlardan birini ara','Look for one of the clouds you just learned about','🔎']],
    'Bulutlarda yüz görmenin adı “pareidolia”: beyin rastgele şekillerde bile tanıdık şeyler arar','Seeing faces in clouds is called pareidolia — the brain looks for familiar things even in random shapes','#1c2a3a','#04070b',gap=7,d=50),
  fact('⅔','Herhangi bir anda Dünya’nın yaklaşık üçte ikisi bulutlarla örtülüdür','At any moment, about two-thirds of the Earth is covered by clouds','NASA uydu ölçümleri · NASA satellite data','#18263a','#03060b',d=28),
]),
S(17,18,'Hayvanların Dili · How Animals Talk',[
  photo('elephants','Savan filleri · Savanna elephants','Bir fil ailesi — duyamadığımız seslerle konuşuyorlar','An elephant family — talking in sounds we cannot hear','Filler insan kulağının duyamayacağı kadar pes seslerle kilometrelerce uzağa mesaj gönderir; bu titreşimleri ayaklarıyla da hissederler','Elephants send rumbles too deep for human ears over kilometres — and feel the vibrations through their feet too',d=38),
  steps('Doğa Zekâsı · Nature’s Genius','Arıların dansı: “Çiçekler şu tarafta, şu kadar uzakta!”','The honeybee dance: “Flowers that way — this far!”',
    [['Bir arı güzel çiçekler bulup kovana dönüyor','A bee finds good flowers and flies home','🐝'],['Peteğin üstünde sekiz çizerek dans ediyor','On the comb it dances in a figure of eight',''],['Ortadaki titreşimli yürüyüşün açısı: Güneş’e göre yön','The angle of the waggle run: the direction relative to the Sun',''],['Titreşimin süresi: uzaklık — uzun dans, uzak çiçek','How long it waggles: the distance — a long dance means far-away flowers',''],['Öteki arılar dansı izleyip doğrudan çiçeğe uçuyor','The others watch and fly straight to the flowers','✓']],
    'Karl von Frisch bu dili çözdüğü için 1973’te Nobel Ödülü aldı','Karl von Frisch won the 1973 Nobel Prize for decoding this language','#2c2616','#080604',gap=6.5,d=56),
  photo('prairiedog','Kara kuyruklu çayır köpeği · Black-tailed prairie dog','Nöbetteki bir çayır köpeği','A prairie dog on lookout','Araştırmalara göre uyarı sesleri yalnızca “tehlike!” demiyor: gelen hayvanın türünü, büyüklüğünü, hatta bir insanın üstündeki rengi bile anlatabiliyor','Research suggests their alarm calls say more than “danger!” — they can describe the predator’s kind, size and even the colour a person is wearing',fit='contain',d=40),
  photo('lyrebird','Victoria, Avustralya · Australia · 1935','Kuyruğunu açmış bir lir kuşu','A lyrebird with its tail spread','Dünyanın en iyi taklitçisi: öteki kuşların seslerini, fotoğraf makinesi deklanşörünü, hatta motorlu testereyi bile kusursuz taklit edebilir','The world’s greatest mimic — it can copy other birds, a camera shutter, even a chainsaw',d=38),
  photo('wolf','Kutup kurdu · Arctic wolf','Uluyan bir kurt','A wolf howling','Bir kurdun uluması açık arazide kilometrelerce öteden duyulur; her kurdun sesi farklıdır ve sürü birbirini sesinden tanır','A wolf’s howl carries for kilometres over open ground — every wolf sounds different, and the pack knows each voice',fit='contain',d=38),
  fact('Karga','Kargalar insan yüzlerini tanır, yıllarca hatırlar — ve bunu öbür kargalara da öğretir','Crows recognise human faces, remember them for years — and teach other crows about them too','Washington Üniversitesi’nin maskeli deneyleri · University of Washington mask experiments','#1c2026','#040506',d=30),
]),
S(18,19,'Bir Saniyede Dünya · The World in One Second',[
  steps('Ölçek Yolculuğu · Scale Journey','Sadece bir saniye… Bu sürede neler oluyor?','Just one second… what happens in that time?',
    [['Işık yaklaşık 300.000 km yol alır: Dünya’nın çevresini 7,5 kez dolaşır','Light travels about 300,000 km — seven and a half times around the Earth','✦'],['Dünya, Güneş’in çevresinde yaklaşık 30 km ilerler','The Earth moves about 30 km along its orbit around the Sun','🌍'],['Kalbin aşağı yukarı bir kez atar','Your heart beats about once','♥'],['Vücudun 2 milyondan fazla yeni kırmızı kan hücresi yapar','Your body makes more than 2 million new red blood cells','●']],
    'Bir saniye küçük görünür ama içine koca bir dünya sığar','A second looks small — yet a whole world fits inside it','#141c2a','#03050a',gap=6.5,d=50),
  photo('hummingbird','Sinekkuşu · Hummingbird','Havada asılı duran bir sinekkuşu','A hummingbird hanging in mid-air','Kanatlarını saniyede 50 kezden fazla çırpar; geriye doğru uçabilen tek kuş grubu','It beats its wings more than 50 times a second — the only birds that can fly backwards',fit='contain',d=38),
  photo('dropcrown','Süt tacı · Milk crown','Bir damlanın çarpıştığı an: süt tacı','The instant a drop lands: a milk crown','Bu taç bir saniyenin yüzde biri kadar bile yaşamaz; Harold Edgerton’ın 1957 fotoğrafıyla ünlendi','The crown lasts less than a hundredth of a second — made famous by Harold Edgerton’s 1957 photograph',d=38),
  photo('cheetah','Namibya · Namibia','Koşan bir çita — bir saniyede yaklaşık 30 metre','A running cheetah — about 30 metres in one second','Karadaki en hızlı hayvan: üç saniyede saatte yaklaşık 100 km hıza çıkabilir','The fastest land animal — it can reach about 100 km/h in three seconds',d=38),
  fact('≈4','Sen bu cümleyi okurken bir saniyede dünyada yaklaşık 4 bebek doğuyor','In the second it takes to read this, about 4 babies are born around the world','Yılda yaklaşık 130 milyon doğum · About 130 million births a year','#2a1f2a','#070507',d=30),
]),
S(19,20,'Yavaş Şehirler · Slow Towns (Cittaslow)',[
  photo('sigacik','Seferihisar, İzmir','Sığacık Kalesi ve limanı — Türkiye’nin ilk “yavaş şehri” Seferihisar’da','Sığacık castle and harbour — in Seferihisar, Türkiye’s first “slow town”','Seferihisar 2009’da Cittaslow ağına katıldı; pazarında yerel üreticiler, kale içinde taş evler var','Seferihisar joined the Cittaslow network in 2009 — local growers fill its market, and stone houses fill the castle',d=40),
  photo('halfeti','Halfeti, Şanlıurfa','Halfeti — Fırat’ın kıyısında, bir kısmı suların altında kalan kasaba','Halfeti — a town on the Euphrates, partly beneath the water','Baraj gölü eski mahallelerin bir bölümünü kapladı; tekne gezileri ve yalnızca burada yetişen kara gülüyle ünlü','A dam lake covered part of the old quarter — it is known for boat trips and the black rose that grows only here',fit='contain',d=40),
  photo('tarakli','Taraklı, Sakarya','Taraklı’nın ahşap konakları','The wooden mansions of Taraklı','Bu küçük kasaba da bir “yavaş şehir”; eski evleri ve tahta kaşık ustalığıyla tanınır','This small town is a “slow town” too — known for its old houses and its wooden spoon makers',d=38),
  fact('1999','Cittaslow (“yavaş şehir”) hareketi 1999’da İtalya’da doğdu: acele etmeyen, yerelini koruyan küçük kasabalar','The Cittaslow (“slow town”) movement began in Italy in 1999 — small towns that refuse to rush and protect what is local','Üye olmak için nüfusun 50.000’in altında olması gerekir · Members must have fewer than 50,000 people','#22301f','#050805',d=30),
  photo('goynuk','Göynük, Bolu','Göynük yakınlarında Çubuk Gölü — Göynük de bir “yavaş şehir”','Çubuk Lake near Göynük — Göynük is a “slow town” too','Ormanla çevrili bu göl, piknik ve sakin yürüyüşler için bölgenin sevilen durağı','Ringed by forest, the lake is the area’s favourite stop for picnics and quiet walks',d=38),
  steps('Villa Fikri · Villa Idea','Villada “yavaş bir pazar”: üç küçük kural','A “slow Sunday” at the villa — three small rules',
    [['Telefonlar bir saatliğine kapının yanındaki sepete','Phones go into a basket by the door for one hour','📵'],['Sofraya yalnızca yakından gelenler: köy peyniri, mısır ekmeği, bahçeden ne varsa','Only local food on the table — village cheese, corn bread, whatever the garden gives','🧺'],['Gün batımında acelesiz bir yürüyüş, dönüşte çay','An unhurried walk at sunset, tea when you get back','☕']],
    'Butik otellerin sırrı da bu: misafire daha çok şey değil, daha çok zaman sunmak','It is the secret of boutique hotels too — not offering guests more things, but more time','#2a2418','#080604',gap=7,d=48),
]),
S(20,21,'Galeri: Mavi Saat · Gallery: The Blue Hour',[
  art('kroyer','Skagen’in Güney Kumsalında Yaz Akşamı — Peder Severin Krøyer, 1893','Summer Evening on Skagen’s Southern Beach — Peder Severin Krøyer, 1893','Danimarka’nın en kuzey ucunda deniz ve gökyüzü, gün batımından sonra aynı maviye bürünür; Skagen ressamları bu saati çok severdi','At Denmark’s northern tip, sea and sky turn the same blue after sunset — the Skagen painters loved this hour'),
  q('Lambalar farklıdır,|ama ışık aynıdır','The lamps are different, but the light is the same','night',d=44),
  art('whistler','Nokturn: Mavi ve Gümüş, Chelsea — James McNeill Whistler, 1871','Nocturne: Blue and Silver – Chelsea — James McNeill Whistler, 1871','Whistler gece resimlerine müzik gibi “nokturn” adını verdi; bu, serinin ilklerinden','Whistler named his night paintings “nocturnes”, like music — this is one of the first'),
  art('grimshaw','Ay Işığında Liverpool Rıhtımı — John Atkinson Grimshaw, 1887','Liverpool Quay by Moonlight — John Atkinson Grimshaw, 1887','Islak kaldırımda parlayan dükkân ışıkları: Grimshaw ay ışığının ressamı olarak anılır','Shop lights glowing on wet stone — Grimshaw is remembered as the painter of moonlight'),
  art('kuindzhi','Dinyeper Üzerinde Ay Işığı — Arhip Kuinci, 1880','Moonlit Night on the Dnieper — Arkhip Kuindzhi, 1880','Tablo karanlık bir odada tek başına sergilendi; ay o kadar parlak görünüyordu ki izleyiciler arkasında lamba var mı diye baktı','It was shown alone in a darkened room — the moon looked so bright that visitors checked behind the canvas for a lamp'),
  fact('4°–6°','Mavi saat, Güneş ufkun yaklaşık 4–6 derece altındayken yaşanır: kızıllar kaybolur, gökyüzünü derin bir mavi kaplar','The blue hour comes when the Sun is about 4–6° below the horizon — the reds fade and a deep blue fills the sky','Fotoğrafçıların en sevdiği saat · Photographers’ favourite hour','#131c32','#03050b',d=30),
]),
S(21,22,'Pazar Akşamı Meydan Okumaları · Sunday-Night Challenges',[
  g('hzfraser',d=52),
  steps('Küçük Meydan Okuma · Little Challenge','Üç mini görev — hemen şimdi, oturduğun yerden','Three mini tasks — right now, from where you sit',
    [['1 dakika: odada mavi olan 5 şey bul','1 minute: find 5 blue things in the room','①'],['Gözlerini kapat: duyduğun 4 farklı sesi say','Close your eyes and count 4 different sounds you can hear','②'],['Adını öteki elinle havaya yaz','Write your name in the air with your other hand','③']],
    'Alışılmadık küçük işler beyni “otomatik pilottan” çıkarır','Small unusual tasks switch the brain off autopilot','#1c2434','#04060a',gap=8,d=46),
  rid('Sesim var ama ağzım yok;<br>sen ne dersen onu söylerim.<br>Ben neyim?','I have a voice but no mouth — I say whatever you say. What am I?','Yankı!','An echo.',sec=16,c1='#1c2430',c2='#04060a'),
  rid('Yüzü var, iki eli var;<br>ama ne gülümser ne alkışlar.<br>Nedir?','It has a face and two hands, but never smiles or claps. What is it?','Saat!','A clock.',sec=16,c1='#2a2420',c2='#070605'),
  fact('6.000','Bir araştırmaya göre insan zihninde günde 6.000’den fazla yeni düşünce başlıyor','According to one study, more than 6,000 new thoughts start in the human mind each day','Queen’s Üniversitesi, Kanada, 2020 · Queen’s University, Canada, 2020','#1b2230','#05070b',d=30),
]),
S(22,23,'Durgun Sular · Still Waters (sakin · calm)',[
  photo('abant','Bolu','Abant Gölü — kışın durgun, mavi bir ayna','Lake Abant — a still blue mirror in winter','Bir heyelanın vadiyi kapatmasıyla oluştu; yaklaşık 1.300 metre yükseklikte, çam ve kayın ormanlarıyla çevrili','Formed when a landslide blocked a valley — about 1,300 m up, ringed by pine and beech forest',d=42),
  q('Sessizlik bir okyanustur;|söz ise bir nehir','Silence is an ocean; speech is a river','sea',d=46),
  photo('matheson','Yeni Zelanda · New Zealand','Matheson Gölü’nde Aoraki (Cook) ve Tasman dağlarının yansıması','Mount Cook (Aoraki) and Mount Tasman reflected in Lake Matheson','Ormandan gelen doğal maddeler suyu koyu kahverengiye boyar; bu yüzden göl kusursuz bir ayna gibi yansıtır','Natural matter from the forest stains the water dark brown — that is why the lake reflects like a perfect mirror',d=42),
  photo('braies','Dolomitler, İtalya · Dolomites, Italy','Braies Gölü — dağların dibinde yeşil bir su','Lake Braies — green water at the foot of the mountains','Yaklaşık 1.500 metrede; sabah erken saatlerde rüzgâr yokken su neredeyse hiç kıpırdamaz','At about 1,500 m — early in the morning, with no wind, the water barely moves',d=42),
  fact('%20','Sibirya’daki Baykal Gölü, dünyadaki donmamış tatlı suyun yaklaşık beşte birini tutar','Lake Baikal in Siberia holds about a fifth of all the unfrozen fresh water on Earth','En derin yeri 1.642 metre; dünyanın en derin ve en yaşlı gölü · 1,642 m at its deepest — the world’s deepest and oldest lake','#10202a','#020507',d=32),
]),
S(23,26,'Yakamoz · Sea Sparkle (sakin · calm)',[
  g('hzyakamoz',d=80),
  q('Ay, geceden kaçmadığı için|parlak kalır','The moon stays bright because it does not run from the night','night',d=46),
  photo('biolum','San Diego, ABD · USA','Alacakaranlıkta mavi parlayan dalgalar','Waves glowing blue at dusk','Bu ışığı denizdeki tek hücreli canlılar yapar; dalga onları sarstıkça kıyı boyunca mavi bir çizgi yanıp söner','Single-celled sea creatures make this light — as the waves jostle them, a blue line flickers along the shore',d=42),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: dört sakin resim','Before sleep: four calm pictures',
    [['Uzakta yanıp sönen bir deniz feneri','A lighthouse blinking far away','✧'],['Kıyıya usulca vuran mavi dalgalar','Blue waves lapping softly at the shore',''],['Ilık bir battaniye ve sessiz bir oda','A warm blanket and a quiet room',''],['Sabaha karşı ötecek ilk kuş','The first bird that will sing before dawn','☾']],
    'İyi geceler — yarın yeni bir hafta','Good night — tomorrow a new week begins','#0e1624','#020306',gap=7.5,d=50,bg='stars'),
  fact('Noctiluca','Yakamozun en bilinen kaynağı Noctiluca adlı tek hücreli bir canlı; adı Latince “geceyi aydınlatan” demek','The best-known source of sea sparkle is a single-celled creature called Noctiluca — Latin for “night light”','Dokunulunca bir anlık mavi ışık verir · It gives a brief blue flash when disturbed','#0c1a26','#020406',d=32),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-15.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
