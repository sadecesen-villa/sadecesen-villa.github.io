# Builds /workspace/tv-pages/days/2026-11-13.json (hourly sets 09:00-02:00). Pattern from build_2026-11-12.py.
import json,os
DATE='2026-11-13'; REV=60; NEXT='2026-11-14'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-13.json')))
FIX={'Image: National Aeronautics and Space Ad':'NASA / ESA / CSA / STScI','Photograph by Mike Peel':'Mike Peel','Photograph by Greg O':'Greg O’Beirne','Richard Leeming from London':'Richard Leeming','NASA/Apollo 17 crew; taken by either Harrison Schmitt or Ron Evans':'NASA / Apollo 17','Image by NASA, modifications by Seddon':'NASA','Surmene at en.wikipedia':'Surmene (en.wikipedia)','Garst, Warren, 1922-2016, photographer':'Warren Garst','https://www.flickr.com/photos/clpmag/':'clpmag (Flickr)','Original: Tambako The Jaguar':'Tambako The Jaguar / Niabot','Al_Khazneh_Petra.jpg: Graham Racher':'Graham Racher / MrPanyGoff','Unknown authorUnknown author':'bilinmeyen fotoğrafçı · unknown photographer','Dartmouth Electron Microscope Facility':'Dartmouth Electron Microscope Facility','shankar s. from Dubai':'shankar s.','Rosa Cabecinhas and Alcino Cunha':'Rosa Cabecinhas & Alcino Cunha'}
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
    it=dict(k='hzphoto',d=d,f='m/h13-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    return it
def villa(k,where,tr,en,fact,facte,fit=None):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=40)
    it['lb']='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where
    return it
def art(k,tr,en,fact,facte,who,fit=None):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=44)
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
S(9,10,'Karadeniz Kıyıları · Black Sea Shores',[
  photo('giresunadasi','Giresun','Giresun Adası — Türkiye’nin Karadeniz kıyısındaki en büyük ada','Giresun Island — the largest island on Türkiye’s Black Sea coast','Antik çağda Aretias diye anılırdı; efsaneye göre Amazonlar burada bir tapınak kurmuştu','In antiquity it was called Aretias; legend says the Amazons built a temple here'),
  q('Dünle beraber gitti cancağızım|ne kadar söz varsa düne ait;|şimdi yeni şeyler söylemek lazım','All the words that belonged to yesterday went with yesterday, dear soul — now it is time to say new things','sea',d=46),
  photo('hamsilos','Sinop','Hamsilos Koyu — “Türkiye’nin tek fiyordu” diye anılan sakin bir koy','Hamsilos Bay — a calm cove often called “Türkiye’s only fjord”','Sinop’ta Türkiye’nin en kuzey ucu da var: İnceburun','Sinop also holds Türkiye’s northernmost point, İnceburun'),
  fact('½','Karadeniz’in yüzey suyu, okyanusların yalnızca yarısı kadar tuzludur','The Black Sea’s surface water is only about half as salty as the ocean','Tuna, Dinyeper ve Don gibi büyük nehirler onu tatlı suyla besler · Great rivers like the Danube, Dnieper and Don pour in fresh water','#14303a','#03080b',d=32),
  photo('cal','Düzköy, Trabzon','Çal Mağarası — içinden yer altı deresi akan bir mağara','Çal Cave — a cave with an underground stream running through it','İçeride şelaleler ve dereler var; mağara yazın bile serin kalır','Inside are waterfalls and streams — the cave stays cool even in summer'),
  photo('horon','Sis Dağı, Trabzon','Sis Dağı’nda horon şenliği — yayla çayırında omuz omuza','A horon festival on Sis Mountain — shoulder to shoulder on the highland meadow','Horon kemençenin hızlı ritmiyle oynanır; omuzların titreyişi denizde çırpınan hamsiye benzetilir','The horon is danced to the fast beat of the kemençe — the shimmy of the shoulders is likened to anchovies flickering in the sea',d=40),
]),
S(10,11,'Kristallerin Büyümesi · How Crystals Grow',[
  g('hzdla',d=75),
  photo('lichtenberg','Lichtenberg figürü · Lichtenberg figure','Akrilik bir blokta “donmuş şimşek”: yüksek gerilimin açtığı dallar','“Frozen lightning” in an acrylic block: branches cut by a high-voltage discharge','Elektrik, plastiğin içinden en kolay yolu ararken ağaç gibi dallanır','The electricity forks like a tree as it searches for the easiest path through the plastic',fit='contain'),
  photo('naica','Naica, Meksika · Mexico','Kristaller Mağarası — insandan kat kat büyük alçıtaşı kristalleri','The Cave of Crystals — selenite crystals many times taller than a person','En büyüğü yaklaşık 12 m boyunda ve 55 ton; sıcak suyun içinde yarım milyon yılda büyüdü','The largest is about 12 m long and weighs 55 tonnes — it grew in hot water over about half a million years',d=40),
  photo('dendrite','Maden dendritleri · Mineral dendrites','Taş üstünde manganez dendritleri — bitki fosili değil, kristal','Manganese dendrites on stone — not fossil plants, but crystals','Mineralli su taşın çatlağına sızar ve az önce gördüğün simülasyondaki gibi dallanarak çöker','Mineral-rich water seeps into a crack and branches out just like the simulation you saw'),
  photo('geode','Ametist jeodu · Amethyst geode','İçi kristal dolu bir taş: ametist jeodu','A stone full of crystals: an amethyst geode','Volkanik kayadaki bir gaz boşluğu, milyonlarca yıl boyunca sızan sudan kristal büyütür','A gas bubble in volcanic rock slowly grows crystals from seeping water over millions of years',fit='contain'),
  fact('6 yüz','Kuvars kristalleri her zaman altı yüzlü bir prizma olarak büyür','Quartz crystals always grow as six-sided prisms','Atomların içerideki diziliş düzeni dış şekle yansır · The order of the atoms inside shows in the outer shape','#22202c','#060508',d=30),
]),
S(11,12,'Sonsuzluk Paradoksları · Paradoxes of Infinity',[
  steps('Düşünce Deneyi · Thought Experiment','Hilbert’in Oteli: sonsuz sayıda odası var ve hepsi dolu…','Hilbert’s Hotel: infinitely many rooms, and every one is full…',
    [['Yeni bir misafir geliyor. Resepsiyon: “Yerimiz var!”','A new guest arrives. Reception says: “We have room!”',''],['Herkes bir sonraki odaya geçiyor: 1→2, 2→3, 3→4…','Everyone moves up one room: 1→2, 2→3, 3→4…',''],['1 numaralı oda boşaldı','Room 1 is now free','✓'],['Sonsuz kişilik bir otobüs gelirse? Herkes oda numarasının iki katına geçer','What if an infinite coach arrives? Everyone moves to double their room number','n → 2n'],['Sonsuz sayıda tek numaralı oda boşalır','Infinitely many odd-numbered rooms are freed','∞']],
    'Sonsuzlukta “dolu” demek “yer yok” demek değildir — David Hilbert, 1924','With infinity, “full” does not mean “no room” — David Hilbert, 1924','#1e2430','#040508',gap=6.5,d=60),
  photo('penrose','East Perth, Avustralya · Australia','İmkânsız Üçgen heykeli — doğru noktadan bakınca kapalı bir üçgen gibi görünür','The Impossible Triangle sculpture — from the right spot it looks like a closed triangle','Gerçek bir Penrose üçgeni var olamaz; heykel aslında açık uçlu ve yalnızca tek bir noktadan “kapanır”','A true Penrose triangle cannot exist — the sculpture is open-ended and only “closes” from one viewpoint',d=40),
  fact('∞ > ∞','Bazı sonsuzluklar ötekilerden büyüktür: 0 ile 1 arasındaki sayılar, bütün sayma sayılarından daha çoktur','Some infinities are bigger than others: there are more numbers between 0 and 1 than there are counting numbers','Georg Cantor, 1874–1891','#262030','#060508',d=32),
  steps('Akıllı Tahmin · Clever Estimate','Türkiye’de bir günde kaç bardak çay içilir? Bilmeden tahmin edelim…','How many glasses of tea are drunk in Türkiye in a day? Let’s estimate without knowing…',
    [['Nüfus yaklaşık 85 milyon','Population about 85 million','85 M'],['Çay içenler: belki üçte ikisi','Tea drinkers: maybe two thirds','≈ 57 M'],['Kişi başı günde ortalama 4 bardak','On average about 4 glasses each per day','× 4'],['Sonuç · Result','','≈ 230 milyon bardak · glasses']],
    'Fermi tahmini: kaba ama akıllı adımlar şaşırtıcı derecede yakın sonuç verir — Türkiye, kişi başı çay tüketiminde dünyada ilk sıralarda','A Fermi estimate: rough but clever steps get surprisingly close — Türkiye is among the world’s top tea drinkers per person','#2a2018','#070504',gap=6,d=54),
  rid('Hep yukarı çıkar,<br>ama hiç aşağı inmez.<br>Nedir?','It always goes up but never comes down. What is it?','Yaşın!','Your age.',sec=16,c1='#22262c',c2='#050607'),
]),
S(12,13,'Kuşların Mimarları · Bird Architects',[
  dict(cp='top',pos='50% 90%',**photo('weaver','Dokumacı kuş · Weaver bird','Erkek dokumacı kuş, otları düğümleyerek asılı bir yuva örüyor','A male weaver knots blades of grass into a hanging nest','Dişi yuvayı beğenmezse erkek söküp baştan örer','If the female doesn’t like it, the male tears it down and starts again')),
  photo('bower','Saten çardak kuşu · Satin bowerbird, Avustralya · Australia','Saten çardak kuşu ve mavi süslerle bezediği çardağı','A satin bowerbird with the bower he has decorated in blue','Dişiyi etkilemek için yalnızca mavi şeyler toplar: tüyler, çiçekler, hatta şişe kapakları','To impress a female he collects only blue things — feathers, flowers, even bottle caps'),
  fact('2 ton','Kayıtlardaki en büyük kel kartal yuvası 2 tondan ağırdı','The largest bald eagle nest on record weighed more than 2 tonnes','Kartallar aynı yuvayı yıllarca kullanır ve her yıl biraz daha büyütür · Eagles reuse the same nest for years, adding to it every season','#1e2a22','#040705',d=30),
  photo('sociable','Kalahari','Ortak dokumacı kuşların bir akasya ağacındaki dev ortak yuvası','A giant communal nest of sociable weavers in an acacia tree','Yüzlerce kuş birlikte yaşar; bazı yuvalar 100 yıldan uzun kullanılır','Hundreds of birds live together — some nests are used for more than 100 years',d=40),
  photo('hornero','Uruguay','Fırıncı kuşu, çamurdan yaptığı fırın biçimli yuvasının üstünde','A rufous hornero on its oven-shaped mud nest','Adını eski toprak fırınlara benzeyen yuvasından alır; Arjantin’in ulusal kuşudur','It is named for its nest, shaped like an old clay oven — and it is Argentina’s national bird'),
]),
S(13,14,'Kendiliğinden Düzen · Order Without a Plan',[
  g('hzsandpile',d=72),
  photo('murmuration','Galashiels, İskoçya · Scotland','Binlerce sığırcık gökyüzünde tek bir canlı gibi dalgalanıyor','Thousands of starlings ripple across the sky like a single creature','Lider yok: her kuş yalnızca en yakın yedi komşusunu izler','There is no leader — each bird simply follows its seven nearest neighbours'),
  steps('Akıllı Açıklama · Clever Explainer','Karıncalar en kısa yolu nasıl bulur? Hiçbiri haritaya bakmadan…','How do ants find the shortest path — without any of them reading a map?',
    [['Her karınca yürürken yere koku (feromon) bırakır','Every ant leaves a scent trail (pheromone) as it walks',''],['Kısa yoldan gidenler yuvaya daha çabuk döner','Ants on the short route get back to the nest sooner',''],['Kısa yolda koku daha hızlı birikir','So scent builds up faster on the short route',''],['Yeni karıncalar en güçlü kokuyu izler','New ants follow the strongest scent',''],['Uzun yolun kokusu uçup gider','The long route’s scent fades away','✓']],
    'Bu fikir bugün kargo rotalarını ve internet trafiğini planlayan algoritmalara ilham veriyor','This idea now inspires algorithms that plan delivery routes and internet traffic','#24301c','#050803',gap=5.5,d=54),
  photo('pamukkale','Denizli','Pamukkale travertenleri — sıcak sudan çöken kireçle oluşan beyaz teraslar','The travertines of Pamukkale — white terraces built from lime left by hot springs','Kimse tasarlamadı: su her kenarda biraz kireç bırakır ve teraslar kendiliğinden yükselir · UNESCO Dünya Mirası','Nobody designed them: the water leaves a little lime at every rim and the terraces rise by themselves · UNESCO World Heritage',d=40),
  photo('ripples','Fuerteventura, İspanya · Spain','Rüzgârın kumda çizdiği dalgacıklar','Ripples drawn in the sand by the wind','Dalgacıkların aralığı, rüzgârın kum tanelerini zıplattığı mesafeye göre kendiliğinden ayarlanır','Their spacing sets itself — matched to how far the wind makes the grains hop'),
]),
S(14,15,'Villa Fikirleri: Sessiz Bahçeler · Villa Ideas: Quiet Gardens',[
  villa('ryoanji','Kyoto','Ryōan-ji’nin kuru bahçesi: tırmıklanmış çakıl ve 15 taş','The dry garden of Ryōan-ji: raked gravel and 15 stones','Verandanın hiçbir noktasından 15 taşın hepsi birden görünmez','From no spot on the veranda can you see all 15 stones at once'),
  q('Dünyanın bahçesinin sınırı yoktur;|sınır yalnızca zihnindedir','The garden of the world has no limits, except in your mind','ink'),
  villa('vertical','CaixaForum, Madrid','Yaşayan duvar: binlerce bitkiden oluşan dikey bir bahçe','A living wall: a vertical garden of thousands of plants','Toprak yok: bitkiler keçe katmanlarında damla sulamayla büyür — taş bir avlu duvarı için güzel bir fikir','No soil — the plants grow in layers of felt with drip irrigation: a lovely idea for a stone courtyard wall'),
  villa('kew','Kew, Londra · London','Büyük bir cam serada palmiyeler ve eğrelti otları arasında yürüyüş yolu','A walkway among palms and ferns inside a great glasshouse','Kışın bile yeşil: camlı bir kış bahçesi, yağmurlu Karadeniz günlerinde kahvaltı için harika bir köşe olur','Green even in winter: a glass winter garden makes a wonderful breakfast spot on rainy Black Sea days'),
  steps('Villa Fikri · Villa Idea','Kendi kuru bahçeni kur: taş, çakıl ve sessizlik','Make your own dry garden: stone, gravel and silence',
    [['Sessiz bir köşe seç: bir pencerenin ya da çay köşesinin önü','Choose a quiet corner — in front of a window or the tea nook',''],['Açık gri çakıl ser, 5–7 cm kalınlığında','Spread pale grey gravel, 5–7 cm deep',''],['Tek sayıda iri taş yerleştir: 3, 5 ya da 7','Place an odd number of large stones: 3, 5 or 7',''],['Çakılı tırmıkla dalgalandır — her sabah yeniden','Rake the gravel into waves — afresh each morning','≋'],['Biraz yosun ve tek bir küçük akçaağaç yeter','A little moss and a single small maple are enough','']],
    'Karadeniz yeşilinin yanında sakin, gri bir ada: misafirler orada yavaşlar','A calm grey island beside the Black Sea green — where guests slow down','#262a26','#060706',gap=6,d=54),
]),
S(15,16,'Sonbaharın Renkleri · Colours of Autumn',[
  photo('yedigoller','Bolu','Yedigöller Milli Parkı — göle yansıyan sonbahar renkleri','Yedigöller National Park — autumn colours mirrored in the lake','Yedi gölü birbirine dereler ve yer altı kanalları bağlar','Its seven lakes are linked by streams and underground channels'),
  steps('Akıllı Açıklama · Clever Explainer','Yapraklar sonbaharda neden sararıp kızarır?','Why do leaves turn yellow and red in autumn?',
    [['Yaz boyunca yeşil klorofil öteki renkleri örter','All summer, green chlorophyll hides the other colours',''],['Günler kısalınca ağaç klorofil üretmeyi bırakır','As the days shorten, the tree stops making chlorophyll',''],['Hep orada olan sarı ve turuncular ortaya çıkar','The yellows and oranges that were there all along appear','karotenoid · carotenoids'],['Kızıl renk ise yeni üretilir — soğuk, güneşli günlerden sonra daha parlak','Reds are newly made — brightest after cold, sunny days','antosiyanin · anthocyanins']],
    'Yani sarı yaprak yeni bir renk giymiyor; maskesini çıkarıyor','So a yellow leaf isn’t putting on a new colour — it is taking off its mask','#2e2016','#080503',gap=6.5,d=52),
  photo('tofukuji','Kyoto','Tōfuku-ji’de gece ışıklandırılan kızıl akçaağaçlar','Crimson maples lit up at night at Tōfuku-ji','Tōfuku-ji’nin akçaağaç vadisi Kyoto’nun en ünlü sonbahar manzaralarından biridir','Tōfuku-ji’s maple valley is one of Kyoto’s most famous autumn sights'),
  q('Bir ağaç gibi ol;|kuru yaprakların düşmesine izin ver','Be like a tree and let the dead leaves drop','clay'),
  photo('mapleleaf','Québec, Kanada · Canada','Sonbahar ışığına tutulmuş bir akçaağaç yaprağı','A maple leaf held up to the autumn light','Akçaağaç yaprağı 1965’ten beri Kanada bayrağında','The maple leaf has been on Canada’s flag since 1965'),
  photo('beech','Steckenroth, Almanya · Germany','Sonbaharda bir kayın ormanından geçen patika','A path through a beech forest in autumn','Karadeniz’in doğu kayını ormanları da kasımda bakır rengine döner','The oriental beech forests of the Black Sea turn copper-red in November too',d=40),
]),
S(16,17,'Derinlik Yanılgıları · Tricks of Depth',[
  g('hzponzo',d=48),
  photo('rays','Tan ışınları · Crepuscular rays','Ağaçların arasından süzülen ışık huzmeleri','Shafts of light streaming between the trees','Bu ışınlar aslında birbirine paralel; bir noktadan yayılıyor gibi görünmeleri bir perspektif oyunu — tıpkı demiryolu rayları gibi','These rays are really parallel — they only seem to fan out from one point because of perspective, just like railway tracks',d=40),
  g('hzhering',d=48),
  photo('moonrise','Paranal, Şili · Chile','Paranal Gözlemevi’nde bir teleskobun yanında doğan kızıl Ay','A reddish Moon rising beside a telescope at Paranal Observatory','Ufuktaki Ay daha büyük görünür ama değildir: fotoğrafta tepedeki Ay’la aynı boydadır — buna “Ay yanılgısı” denir','The Moon looks bigger near the horizon, but it isn’t — in photos it is the same size as high in the sky: the “Moon illusion”',d=40),
  steps('Akıllı Açıklama · Clever Explainer','Uzaktaki dağlar neden mavi görünür?','Why do distant mountains look blue?',
    [['Gözünle dağ arasında kilometrelerce hava var','Between your eye and the mountain lie kilometres of air',''],['Hava, mavi ışığı en çok saçar','Air scatters blue light the most',''],['Mesafe arttıkça bu mavi perde kalınlaşır','The farther away, the thicker this blue veil',''],['Beyin bunu “uzak” diye okur','Your brain reads it as “far away”','✓']],
    'Ressamlar buna “hava perspektifi” der: Leonardo da Vinci uzak tepeleri bilerek mavi boyadı','Painters call it “aerial perspective” — Leonardo da Vinci painted distant hills blue on purpose','#18243a','#03050a',gap=6,d=50),
]),
S(17,18,'Ateş Dağları · Fire Mountains',[
  photo('ararat','Ağrı','Ağrı Dağı — 5.137 metreyle Türkiye’nin en yüksek dağı','Mount Ararat — at 5,137 m, the highest mountain in Türkiye','Sönmüş değil, uykuda bir yanardağ; zirvesi yıl boyu buzulla kaplı','A dormant — not extinct — volcano, its summit capped with ice all year'),
  photo('kilauea','Hawaii','Pāhoehoe lavası Büyük Okyanus’la buluşuyor','Pāhoehoe lava meets the Pacific Ocean','Hawaii adalarının hepsi deniz tabanından yükselen lavlarla oluştu — yeni kara hâlâ doğuyor','All the Hawaiian islands were built by lava rising from the seafloor — new land is still being born'),
  steps('Akıllı Açıklama · Clever Explainer','Bir yanardağ neden patlar?','Why does a volcano erupt?',
    [['Derinlerde kaya erir: magma','Deep down, rock melts into magma',''],['Magma çevresindeki kayadan hafiftir, yukarı yükselir','Magma is lighter than the rock around it, so it rises',''],['İçindeki gazlar, gazozdaki kabarcıklar gibi sıkışık durur','Gases are trapped inside, like the bubbles in a fizzy drink',''],['Yüzeye yaklaşınca basınç düşer, gazlar genişler','Near the surface the pressure drops and the gases expand',''],['Kapak açılır: patlama!','The cap pops — eruption!','🌋']],
    'Akışkan magma (Hawaii) sakin akar; yapışkan magma (Vezüv) patlar','Runny magma (Hawaii) flows calmly; sticky magma (Vesuvius) explodes','#2e1a14','#080403',gap=5.5,d=52),
  photo('peri','Kapadokya, Nevşehir','Kapadokya’nın peri bacaları','The fairy chimneys of Cappadocia','Erciyes, Hasandağı ve Göllüdağ’ın milyonlarca yıl önceki küllerinden oluştular; sert şapkalar altlarındaki yumuşak tüfü korur','They formed from ash thrown out millions of years ago by Erciyes, Hasandağı and Göllüdağ — the hard caps shield the soft tuff below',d=40),
  photo('fuji','Kawaguchi Gölü, Japonya · Japan','Kawaguchi Gölü’nden Fuji Dağı','Mount Fuji from Lake Kawaguchi','Son kez 1707’de patladı; neredeyse kusursuz koni şekli, üst üste yığılan patlamalarla oluştu','It last erupted in 1707 — its near-perfect cone was built eruption upon eruption'),
  rid('Bir adam yağmurda şapkasız, şemsiyesiz yürüdü;<br>saçının tek teli bile ıslanmadı.<br>Nasıl?','A man walked in the rain with no hat and no umbrella, yet not one hair got wet. How?','Adam keldi!','He was bald.',sec=18,c1='#2a201c',c2='#070505'),
]),
S(18,19,'Buz Dünyaları · Ice Worlds',[
  photo('perito','Patagonya, Arjantin · Argentina','Perito Moreno Buzulu — yaklaşık 70 metre yüksekliğinde bir buz duvarı','Perito Moreno Glacier — a wall of ice about 70 m high','Küçülmeyen az sayıdaki buzuldan biri; zaman zaman dev buz blokları göle düşer','One of the few glaciers that isn’t shrinking — now and then huge blocks of ice crash into the lake'),
  photo('penguins','Antarktika · Antarctica','Sudan buzun üstüne fırlayan bir imparator penguen','An emperor penguin leaping out of the water onto the ice','Tüylerinden bıraktığı hava kabarcıkları onu bir an için çok hızlandırır — fırlayışın sırrı bu','Air bubbles released from its feathers make it much faster for a moment — the secret of the leap'),
  photo('iceberg','Buzdağı · Iceberg','Dalgaların yonttuğu bir buzdağı parçası','A piece of iceberg sculpted by the waves','Bir buzdağının yaklaşık %90’ı suyun altında kalır','About 90% of an iceberg stays hidden under water'),
  fact('%70','Dünyadaki tatlı suyun yaklaşık %70’i Antarktika’nın buzunda saklı','About 70% of the world’s fresh water is locked in Antarctica’s ice','Hepsi erirse deniz seviyesi yaklaşık 58 m yükselirdi · If it all melted, sea level would rise by about 58 m','#16263a','#03060a',d=30),
  photo('icecave','İzlanda · Iceland','İzlanda’da bir buzul mağarası — mavi ışığın içinde bir kâşif','An ice cave in Iceland — an explorer in the blue light','Buzul buzu o kadar sıkışmıştır ki kırmızı ışığı yutar, yalnızca maviyi geçirir','Glacier ice is so dense it swallows red light and lets only the blue through',d=40),
]),
S(19,20,'Galaksiler · Galaxies',[
  g('hzgalaxy',d=72),
  photo('m51','Hubble','Girdap Galaksisi (M51) ve küçük komşusu','The Whirlpool Galaxy (M51) and its small companion','Yaklaşık 30 milyon ışık yılı uzakta; komşusunun çekimi sarmal kollarını belirginleştiriyor','About 30 million light-years away — its neighbour’s pull sharpens its spiral arms'),
  photo('sombrero','Hubble','Sombrero Galaksisi (M104) — yandan gördüğümüz bir galaksi ve koyu toz halkası','The Sombrero Galaxy (M104) — seen edge-on, with its dark ring of dust','Merkezinde Güneş’ten yaklaşık 1 milyar kat ağır bir kara delik var','At its heart sits a black hole about a billion times the mass of the Sun'),
  fact('≈ 0','İki galaksi çarpıştığında yıldızlar neredeyse hiç birbirine değmez — aralarındaki boşluk o kadar büyüktür','When two galaxies collide, their stars almost never touch — the gaps between them are that huge','Güneş bir kum tanesi olsaydı, en yakın yıldız ≈6 km ötede olurdu · If the Sun were a grain of sand, the nearest star would be ≈6 km away','#141a30','#020308',d=32),
  photo('cliffs','James Webb','Karina Bulutsusu’nun “Kozmik Uçurumları” — James Webb Uzay Teleskobu','The “Cosmic Cliffs” of the Carina Nebula — James Webb Space Telescope','En yüksek “tepeler” yaklaşık 7 ışık yılı boyunda; içlerinde yeni yıldızlar doğuyor','The tallest “peaks” are about 7 light-years high — new stars are being born inside them',d=40),
]),
S(20,21,'Akıllı Mühendislik · Clever Engineering',[
  photo('falkirk','Falkirk, İskoçya · Scotland','Falkirk Çarkı — tekneleri bir kanaldan ötekine döndürerek taşıyan dev çark','The Falkirk Wheel — a giant wheel that turns boats from one canal to another','İki kol hep dengede: tekne girince tam kendi ağırlığı kadar su taşar. Yarım tur, yaklaşık 8 su ısıtıcısı kaynatacak kadar enerji harcar','The two arms always balance: a boat pushes out exactly its own weight in water. Half a turn uses about the energy of boiling eight kettles',d=40),
  steps('Akıllı Açıklama · Clever Explainer','Binlerce tonluk çelik bir gemi neden batmaz?','Why doesn’t a steel ship weighing thousands of tonnes sink?',
    [['Su, içine giren her şeyi yukarı iter','Water pushes up on anything that enters it',''],['Bu itme = yerinden çıkan suyun ağırlığı','That push equals the weight of the water pushed aside','Arşimet · Archimedes'],['Dolu bir çelik blok az su iter: batar','A solid steel block pushes aside little water — it sinks',''],['Aynı çelik içi boş bir gövde olunca çok su iter','Shape the same steel into a hollow hull and it pushes aside a lot of water',''],['Gemi, kendi ağırlığı kadar su ittiği yerde yüzer','The ship floats once it has pushed aside its own weight in water','⚓']],
    'Rivayete göre Arşimet bunu yıkanırken fark etti ve “Eureka — buldum!” diye bağırdı','Legend says Archimedes realised this in the bath and shouted “Eureka — I’ve found it!”','#16263a','#03060a',gap=5.5,d=54),
  photo('millau','Millau, Fransa · France','Millau Viyadüğü — vadinin çok üstünden geçen bir köprü','The Millau Viaduct — a bridge running high above the valley','En yüksek direği 343 m: Eyfel Kulesi’nden daha uzun','Its tallest mast reaches 343 m — taller than the Eiffel Tower'),
  photo('canakkale','Çanakkale','1915 Çanakkale Köprüsü — Avrupa ile Asya’yı Çanakkale Boğazı üzerinden bağlıyor','The 1915 Çanakkale Bridge — linking Europe and Asia across the Dardanelles','2.023 metrelik orta açıklığıyla dünyanın en uzun asma köprüsü; bu sayı Cumhuriyet’in 100. yılını anıyor','With a 2,023 m main span it is the world’s longest suspension bridge — the number honours the Republic’s centenary',d=40),
  rid('Sepette 5 elma var. 5 arkadaşına birer elma verdin,<br>ama sepette yine bir elma kaldı.<br>Nasıl?','There are 5 apples in a basket. You give one to each of 5 friends, yet one apple stays in the basket. How?','Sonuncusuna elmayı sepetiyle verdin!','You gave the last friend the apple still inside the basket.',sec=22,d=38,c1='#24282c',c2='#050607'),
]),
S(21,22,'Işığın Ressamları · Painters of Light',[
  art('impression','İzlenim, Gün Doğumu — Claude Monet, 1872','Impression, Sunrise — Claude Monet, 1872','Bu tablo bir akıma adını verdi: bir eleştirmen alay ederek bu ressamlara “izlenimciler” dedi','This painting named a movement — a critic mockingly called these painters “Impressionists”','Claude Monet'),
  q('Sevdiğin şeyin güzelliği|yaptığın şey olsun','Let the beauty of what you love be what you do','night'),
  art('temeraire','Savaşan Temeraire — J. M. W. Turner, 1839','The Fighting Temeraire — J. M. W. Turner, 1839','Eski bir yelkenli savaş gemisi, buharlı bir römorkörle son yolculuğuna çekiliyor; Turner bu tabloyu hiç satmadı, ona “sevgilim” derdi','An old sailing warship is towed to its last berth by a steam tug — Turner never sold it and called it his “darling”','J. M. W. Turner'),
  art('hiroshige','Shin-Ōhashi Köprüsü’nde Ani Sağanak — Utagawa Hiroshige, 1857','Sudden Shower over Shin-Ōhashi Bridge — Utagawa Hiroshige, 1857','Van Gogh bu baskıya öyle hayran kaldı ki 1887’de yağlıboyayla kopyasını yaptı','Van Gogh admired this print so much that he copied it in oils in 1887','Utagawa Hiroshige'),
  art('almond','Badem Çiçekleri — Vincent van Gogh, 1890','Almond Blossom — Vincent van Gogh, 1890','Yeğeninin doğumu için yaptı: bahar dalları yeni bir hayatın simgesi','He painted it for his newborn nephew — spring branches as a sign of new life','Vincent van Gogh'),
  art('sorolla','Deniz Kıyısında Gezinti — Joaquín Sorolla, 1909','Strolling along the Seashore — Joaquín Sorolla, 1909','Sorolla’ya “ışığın ressamı” denir; tablolarını çoğu zaman sahilde, açık havada boyadı','Sorolla is called “the painter of light” — he often painted right on the beach, in the open air','Joaquín Sorolla'),
]),
S(22,23,'Sakin Sular · Still Waters',[
  q('Nerede olursan ol,|ne yaparsan yap, sevgi içinde ol','Wherever you are, whatever you do, be in love','night',d=46),
  photo('bled','Slovenya · Slovenia','Kışın Bled Gölü — karlı ağaçlar ve pembe bir alacakaranlık','Lake Bled in winter — snowy trees and a pink dusk','Gölün ortasındaki küçük adaya, “pletna” denen geleneksel kayıklarla gidilir','The little island in the middle of the lake is reached by traditional “pletna” boats',d=42),
  photo('lotus','Lotus yaprağı · Lotus leaf','Lotus yaprağının üstünde bir su damlası — içinde minik bir kurbağa','A drop of water on a lotus leaf — with a tiny frog inside','Yaprağın yüzeyi mikroskobik tümseklerle kaplı: su tutunamaz, kirle birlikte yuvarlanıp gider — “lotus etkisi”','The leaf is covered in microscopic bumps — water can’t cling and rolls away with the dirt: the “lotus effect”',d=42),
  fact('20 dk','Doğada 20 dakika geçirmek stres hormonunu belirgin biçimde düşürür','Spending 20 minutes in nature noticeably lowers your stress hormone','Michigan Üniversitesi araştırması, 2019 · University of Michigan study, 2019','#14202a','#030507',d=32),
  photo('hallstatt','Avusturya · Austria','Hallstatt Gölü’nde kış — karlı dağlar ve durgun su','Winter on Lake Hallstatt — snowy mountains and still water','Hallstatt’ta 7.000 yıldır tuz çıkarılıyor; bilinen en eski tuz madeni burada','Salt has been mined at Hallstatt for 7,000 years — the oldest known salt mine in the world',d=42),
]),
S(23,26,'Ay Yolu · Moon Road (sakin · calm)',[
  g('hzmoonsea',d=80),
  q('Aradığın şey|seni arıyor','What you seek is seeking you','night',d=44),
  photo('hedgehog','Garching, Almanya · Germany','Kuru yapraklar arasında uyuyan bir kirpi','A hedgehog asleep among dry leaves','Kış uykusundan önce yaprak ve yosundan sıcak bir yuva yapar; kasımdan marta kadar uyur','Before hibernating it builds a warm nest of leaves and moss — and sleeps from November to March',d=42),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: bugünün üç küçük güzelliği','Before sleep: three small good things from today',
    [['Bugün seni gülümseten bir an','A moment that made you smile today',''],['Tadını çıkardığın bir şey: bir çay, bir manzara, bir ses','Something you enjoyed — a tea, a view, a sound',''],['Yarın için küçük bir merak','One small thing you are curious about for tomorrow','☾']],
    'Araştırmalar, her akşam üç güzel şeyi hatırlamanın ruh halini iyileştirdiğini gösteriyor','Studies show that recalling three good things each evening lifts your mood','#0e1624','#020306',gap=7,d=48,bg='stars'),
  fact('%12','Ay, üstüne düşen güneş ışığının yalnızca yaklaşık %12’sini yansıtır','The Moon reflects only about 12% of the sunlight that falls on it','Yani aslında eski bir asfalt kadar koyu — gece gökyüzünde parlak görünmesi karanlığın sayesinde · As dark as worn asphalt — it only looks bright against the night','#101a26','#020305',d=32),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-13.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
