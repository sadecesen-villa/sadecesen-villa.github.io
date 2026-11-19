# (Pattern from build_2026-11-18.py) Builds /workspace/tv-pages/days/2026-11-19.json (hourly sets 09:00-02:00). Thursday: times tables on a circle, Hokusai, probability traps, mind & prediction, arrival & welcome, curvature/Pinna illusions, witnesses of time, shortest path, ancient engineering, eyes of spacecraft, strange creatures, notebooks of genius, calm shore evening, night fishermen.
import json,os
DATE='2026-11-19'; REV=71; NEXT='2026-11-20'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-19.json')))
FIX={'Katsushika Hokusai':'Katsushika Hokusai','Photo by and (C)2007 Derek Ramsey':'Derek Ramsey (düzenleme · edit: Papa Lima Whiskey)','bgv23':'bgv23','Unknown author':'bilinmeyen fotoğrafçı · unknown photographer','NASA/JPL-Caltech/Malin':'NASA / JPL-Caltech / MSSS','Mars Science Laboratory':'NASA / JPL-Caltech / MSSS / Texas A&M Univ.','NASA/Johns Hopkins':'NASA / JHUAPL / SwRI','NASA/JPL-Caltech/SwRI':'NASA / JPL-Caltech / SwRI / MSSS / Gerald Eichstädt / Seán Doran','Harvey Barrison':'Harvey Barrison','Benh LIEU SONG':'Benh LIEU SONG','Nevit Dilmen':'Nevit Dilmen','Audubon, John James':'John James Audubon','Russo Francesco':'Francesco Russo','NASA and the European Space Agency':'NASA / ESA','NASA/JPL/Space Science Institute':'NASA / JPL / Space Science Institute','NASA/JPL/NIMA':'NASA / JPL / NIMA','NASA/JPL-Caltech':'NASA / JPL-Caltech','NASA/Bill Anders':'NASA / Bill Anders','Roy Egloff':'Roy Egloff','CopyrightFreePhotos':'CopyrightFreePhotos','Grand Canyon NPS':'Grand Canyon National Park (NPS)','Clarisse Meyer':'Clarisse Meyer','Bernard DUPONT':'Bernard Dupont','Bob Henricks':'Bob Henricks','Forest Wander':'Forest Wander','Credits to Mourad Ben Abdallah':'Mourad Ben Abdallah','NASA image courtesy of the DSCOVR':'NASA / DSCOVR EPIC','blgrssby from St. Louis':'blgrssby','al-Jazari':'el-Cezerî · al-Jazari (1315 kopyası · copy, The Met)','Ala ad-Din Mansur-Shirazi':'Alaeddin Mansur · Ala ad-Din Mansur-Shirazi (Şehinşahname, 1581)','NOIRLab/NSF/AURA':'NOIRLab / NSF / AURA','卓珺 黄':'Zhuojun Huang','none (Landsat)':'NASA / USGS Landsat','Kritzolina':'Claude Monet (detay · detail; foto · photo: Kritzolina)','Dale Cruse':'Dale Cruse'}
def artist(k):
    a=C[k]['artist']
    if not a.strip(): return 'The Metropolitan Museum of Art'
    for f,t in FIX.items():
        if a.startswith(f): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace(' rs','')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,pos=None):
    if k not in C: print('SKIP missing photo',k); return None
    it=dict(k='hzphoto',d=d,f='m/h19-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
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
    it=dict(k='hzguess',d=d,f='m/h19-%s.jpg'%k,lb='Bil Bakalım · Can You Guess? — '+REAL+' · '+where,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr=cr(k))
    if hint: it['hint']=hint
    return it
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=[i for i in items if i])
TE='Düşünce Deneyi · Thought Experiment'; CT='Zekice Düşünce · Clever Thinking'
sets=[
S(9,10,'Perşembe Sabahı · Thursday Morning',[
  photo('caykara','Çaykara · Trabzon','Çaykara yakınlarında bir yamaç köyü: dağınık evler, yeşil çayırlar ve sis','A hillside village near Çaykara — scattered houses, green meadows and mist','Doğu Karadeniz’de evler genellikle bir arada değil, yamaçlara dağınık kurulur: herkes kendi tarlasının yanında yaşar','In the Eastern Black Sea, houses are usually scattered over the slopes rather than clustered — each family lives beside its own fields',d=42),
  q('Cömertlikte akarsu gibi ol;|hoşgörüde deniz gibi ol','In generosity be like a river; in tolerance be like the sea','sea',d=44),
  photo('akcaabat','Ak Camii, Akçaabat · Trabzon','Akçaabat’ta beyaz taş bir cami ve ince minaresi, açık bir gökyüzü altında','A white stone mosque and its slender minaret in Akçaabat, under an open sky','Akçaabat, Trabzon’un hemen batısında; köftesi ve horon oyunuyla Türkiye’nin her yerinde tanınır','Akçaabat lies just west of Trabzon — famous all over Türkiye for its köfte and its horon dance',d=40),
  fact('Perşembe','“Perşembe” Farsça “penc-şenbe”den gelir: “cumartesiden sonraki beşinci gün”','“Perşembe” (Thursday) comes from Persian panj-shanbe — “the fifth day after Saturday”','İngilizce Thursday ise “Thor’un günü” · The English Thursday is “Thor’s day”','#1c2a30','#050809',d=30),
  rid('Ne kadar çok kurularsa, o kadar ıslanır. Nedir?','The more it dries, the wetter it gets. What is it?','Havlu!','A towel!',sec=16,c1='#22303a',c2='#06090c'),
]),
S(10,11,'Yaşayan Sanat: Çemberde Çarpım Tablosu · Living Art: Times Tables on a Circle',[
  g('hztimes',d=90),
  steps('Zekice Düşünce · Clever Thinking','Basit bir kural neden bu kadar güzel şekiller çiziyor?','Why does such a simple rule draw such beautiful shapes?',
    [['Her çizgi, bir noktayı kendisinin k katına bağlıyor','Each line joins a point to k times itself','✏️'],['Tek bir çizgi sıkıcı; ama yüzlercesi üst üste binince bir “zarf” oluşur','One line is dull — but hundreds together trace an “envelope”',''],['Zarfın şekli yalnızca k’ya bağlı: k=2 kardioid, k=3 nefroid','The envelope depends only on k — k=2 a cardioid, k=3 a nephroid',''],['Aynı kardioid bir çay bardağının dibinde, ışığın yansımasında da belirir','The same cardioid appears as reflected light at the bottom of a tea glass','']],
    'Bir dahaki çayında bardağın dibine bak: güneş ışığı orada kalp çiziyor olabilir','Next time you have tea, look at the bottom of the glass — sunlight may be drawing a heart there','#1b2a3a','#060a10',gap=8,d=60),
  photo('ginkgo','Ginkgo yaprağı · Ginkgo leaf','Karanlığın içinde tek bir ginkgo yaprağı: yelpaze gibi açılan damarlar','A single ginkgo leaf against the dark — veins opening like a fan','Ginkgo’nun damarları hiç birleşmeden hep ikiye ayrılır: doğanın en basit kurallarından biri','Ginkgo veins only ever split in two and never rejoin — one of nature’s simplest rules',fit='contain',d=40),
]),
S(11,12,'Galeri: Hokusai’nin Dünyası · Gallery: The World of Hokusai',[
  art('greatwave','Kanagawa Açıklarında Büyük Dalga — Katsushika Hokusai, yaklaşık 1831','The Great Wave off Kanagawa — Katsushika Hokusai, about 1831','Dalganın ardında küçücük kalan dağ Fuji; üç kayıktaki kürekçiler dalganın altında eğilmiş','The tiny mountain behind the wave is Fuji — the rowers in three boats are bent low beneath the crest'),
  art('redfuji','Güney Rüzgârı, Açık Sabah (“Kızıl Fuji”) — Hokusai, yaklaşık 1831','Fine Wind, Clear Morning (“Red Fuji”) — Hokusai, about 1831','Yaz sonu sabahlarında güneşin ilk ışığı dağı birkaç dakikalığına kızıla boyar','On late-summer mornings the first sunlight paints the mountain red for just a few minutes'),
  art('kajikazawa','Kai Eyaletinde Kajikazawa — Hokusai, yaklaşık 1831','Kajikazawa in Kai Province — Hokusai, about 1831','Bir kayanın ucunda ağ atan balıkçı, ipleri ve köpükle neredeyse bir üçgen çiziyor','A fisherman casting his net from a rock — his lines and the spray form an almost perfect triangle'),
  art('ejiri','Suruga Eyaletinde Ejiri — Hokusai, yaklaşık 1832','Ejiri in Suruga Province — Hokusai, about 1832','Ani bir rüzgâr şapkaları ve kâğıtları havaya savuruyor; Fuji ise yalnızca tek bir çizgi','A sudden gust sends hats and papers flying — while Fuji is just a single line'),
  art('kirifuri','Kurokami Dağı’nda Kirifuri Şelalesi — Hokusai, yaklaşık 1832','Kirifuri Waterfall at Mount Kurokami — Hokusai, about 1832','Hokusai suyu düz bir perde gibi değil, parmaklar gibi ayrılan kollar olarak çizdi','Hokusai drew the water not as a sheet, but as strands parting like fingers'),
  q('Güzel ve hoş yaratılan her şey,|onu gören göz içindir','Everything made beautiful and fair is made for the eye of one who sees','ink',d=42),
]),
S(12,13,'Zekice Düşünce: Olasılığın Tuzakları · Clever Thinking: Traps of Probability',[
  g('hzmonty',d=80),
  steps(CT,'Test pozitif çıktı. Gerçekten hasta olma ihtimalin ne?','The test came back positive. What are the chances you are really ill?',
    [['Bir hastalık 1.000 kişiden 1’inde var','A disease affects 1 person in 1,000','🧪'],['Test hastaların hepsini yakalıyor ama sağlamların %5’ine de “pozitif” diyor','The test catches every case — but also says “positive” for 5% of healthy people',''],['1.000 kişiyi test et: 1 gerçek hasta + yaklaşık 50 yanlış alarm','Test 1,000 people: 1 real case + about 50 false alarms',''],['Pozitiflerden yalnızca 51’de 1’i gerçekten hasta','Only 1 in 51 positives is actually ill','']],
    'Yaklaşık %2! Nadir şeylerde, “kaç kişide var?” sorusu testin kendisi kadar önemli','About 2%! With rare things, “how many people have it?” matters as much as the test itself','#1e2c34','#070b0e',gap=7,d=60),
  rid('Bir ailenin iki çocuğu var ve en az biri kız. İkisinin de kız olma olasılığı nedir?','A family has two children, and at least one is a girl. What is the chance both are girls?','1/3! Olası eşit durumlar: KK, KE, EK — yalnızca biri KK','1/3! The equally likely cases are GG, GB, BG — only one is GG',sec=22,d=38,c1='#24303a',c2='#070a0d'),
  fact('½','Yazı tura beş kez üst üste tura geldi. Altıncı atışta tura gelme olasılığı? Yine yarı yarıya','A coin lands heads five times in a row. The chance of heads on the sixth toss? Still one half','Paranın hafızası yok; “artık yazı gelmeli” hissine kumarbaz yanılgısı denir · The coin has no memory — the “tails is due” feeling is the gambler’s fallacy','#2a2420','#0a0806',d=32),
]),
S(13,14,'Düşünce Deneyleri: Kader, Kimlik ve Renk · Thought Experiments: Fate, Identity & Colour',[
  steps(TE,'Laplace’ın Cini: her atomun yerini ve hızını bilen bir zihin geleceği görebilir mi?','Laplace’s demon: could a mind that knows every atom’s place and speed see the future?',
    [['1814’te Laplace hayal etti: evrendeki her şeyin şu anki durumunu bilen bir zihin','In 1814 Laplace imagined a mind that knows the present state of everything','🔭'],['Fizik yasalarıyla ileri hesaplarsa, geleceği geçmiş kadar net görür','Calculating forward with the laws of physics, it would see the future as clearly as the past',''],['Ama kaos: en küçük ölçüm hatası zamanla dev farklara büyür','But chaos: the smallest measuring error grows into huge differences over time',''],['Ve kuantum fiziği, bazı olayların özünde rastlantısal olduğunu söylüyor','And quantum physics says some events are random at their core','']],
    'Gelecek belki yazılı değil — ya da yazılı ama hiçbir zihin okuyamaz','Perhaps the future is not written — or it is, but no mind can read it','#1b2433','#05080d',gap=8,d=58),
  art('laplace','Pierre-Simon Laplace (1749–1827) — gravür, 1873','Pierre-Simon Laplace (1749–1827) — engraving, 1873','Laplace, Güneş Sistemi’nin kararlılığını hesapladı; 1796’da ışığın bile kaçamayacağı “karanlık yıldızları”, yani kara delik fikrini ilk düşünenlerden biriydi','Laplace calculated the stability of the Solar System — and in 1796 he was among the first to imagine “dark stars” that not even light could escape: black holes',d=40),
  steps(TE,'Işınlanma makinesi: seni burada tarar, Mars’ta yeniden kurar. Varan kişi sen misin?','The teleporter: it scans you here and rebuilds you on Mars. Is the one who arrives you?',
    [['Makine her atomunun kaydını alır ve buradaki bedeni siler','The machine records every atom of you and erases the body here','✨'],['Mars’ta aynı atomlar aynı düzenle yeniden kurulur: aynı anılar, aynı huy','On Mars the same pattern is rebuilt — same memories, same character',''],['Peki makine buradaki bedeni silmeyi unutursa? Artık iki “sen” var','But what if the machine forgets to erase the original? Now there are two “yous”',''],['Hangisi gerçek sen? İkisi de “benim” diyor','Which is the real you? Both say “me”','']],
    'Derek Parfit’e göre önemli olan “aynı kişi” olmak değil, anıların ve bağların devam etmesi','For Derek Parfit, what matters is not being “the same person” but the continuity of memories and bonds','#241c30','#08060d',gap=8,d=58),
  q('Bu dünya bir dağdır, yaptıklarımız ses;|seslerin yankısı yine bize döner','This world is a mountain, and our deeds are the shout — the echo always comes back to us','clay',d=44),
  steps(TE,'Senin gördüğün kırmızı, benim gördüğüm kırmızıyla aynı mı?','Is the red you see the same as the red I see?',
    [['İkimiz de domatese “kırmızı”, çimene “yeşil” diyoruz','We both call a tomato “red” and grass “green”','🍅'],['Ama ya benim zihnimde kırmızı, senin yeşil dediğin his gibi görünüyorsa?','But what if, in my mind, red looks the way your green feels?',''],['Kelimelerimiz hep uyar; hiçbir test farkı gösteremez','Our words always match — no test could reveal the difference',''],['Bu soruya “ters çevrilmiş renk tayfı” denir','Philosophers call it the “inverted spectrum”','']],
    'Bir başkasının içini tam olarak hiç göremeyiz — belki de bu yüzden anlatmak bu kadar değerli','We can never fully see inside another mind — perhaps that is why telling each other matters so much','#301c1c','#0d0606',gap=8,d=56),
]),
S(14,15,'Villa Fikirleri: Varış ve Karşılama · Villa Ideas: Arrival & Welcome',[
  villa('olive','Norveç · Norway','Büyük bir küpte yaşlı bir zeytin ağacı: girişe ya da terasa tek başına bir heykel gibi','An old olive tree in a large jar — standing alone like a sculpture at the entrance or on the terrace','Zeytin saksıda yıllarca yaşar; geniş, ağır bir küp kökleri serin tutar ve rüzgârda devrilmeyi önler','Olives live for years in containers — a wide, heavy jar keeps the roots cool and stops it tipping in the wind',fit='contain'),
  villa('frontdoor','Winchester, İngiltere · England','Taş bir kemerin içinde koyu renk ahşap bir kapı: eve giriş başlı başına bir an olur','A dark wooden door set in a stone arch — arriving becomes a moment of its own','Butik otellerde kapı, misafirin ilk dokunduğu şeydir: ağır bir kol ve iyi bir menteşe sessizce “kalite” der','In boutique hotels the door is the first thing a guest touches — a heavy handle and a good hinge quietly say “quality”',fit='contain'),
  villa('stonesteps','Dawyck Bahçesi, İskoçya · Scotland','Bitkilerle çevrili alçak taş basamaklar: yürüyüşü yavaşlatan, bahçeyi gösteren bir yol','Low stone steps edged with planting — a path that slows you down and shows off the garden','Alçak ve geniş basamaklar (yaklaşık 12–15 cm) bahçede yürümeyi rahat ve keyifli yapar','Low, deep steps (about 12–15 cm high) make walking through a garden easy and pleasant'),
  villa('acequia','Generalife, Elhamra · Alhambra, Granada','Uzun bir su kanalı, iki yanında kemerli fıskiyeler ve çiçek tarhları','A long water channel lined with arching fountains and flower beds','Bu bahçe 700 yılı aşkın süredir aynı fikirle yaşıyor: suyun sesi avluyu serinletir ve sakinleştirir','This garden has lived by the same idea for more than 700 years — the sound of water cools and calms the courtyard'),
  villa('pathlights','Longwood Gardens, ABD · USA','Kış gecesi ışıklandırılmış ağaçlar: bahçe karanlıkta bambaşka bir oda olur','Trees lit on a winter night — in the dark the garden becomes a different room','Ağaçları alttan aydınlatmak (uplight) ya da dallara ince ışık sarmak, villayı yoldan bile davetkâr gösterir','Lighting trees from below, or wrapping branches in fine lights, makes a house look welcoming even from the road'),
  rid('Bir bahçıvan dört ağacı, her biri diğer üçüne tam olarak eşit uzaklıkta olacak şekilde dikmek istiyor. Nasıl?','A gardener wants to plant four trees so that each is exactly the same distance from the other three. How?','Üçünü eşkenar üçgen olarak diz, dördüncüyü ortadaki bir tepeye dik: bir üçgen piramit!','Plant three in an equilateral triangle and the fourth on a mound in the middle — a triangular pyramid!',hint='İpucu: düz zeminde olmaz · Hint: not on flat ground',sec=24,d=40,c1='#1d2c24',c2='#060a08'),
]),
S(15,16,'Göz Oyunları: Eğri, Köşe ve Dönüş · Tricks of the Eye: Curves, Corners & Spin',[
  g('hzcurve',d=60),
  g('hzpinna',d=60),
  steps('Göz ve Beyin · Eye & Brain','Neden aldanıyoruz?','Why are we fooled?',
    [['Gözden beyne saniyede çok fazla bilgi gelir; hepsini incelemeye vakit yoktur','Far too much information reaches the brain every second to examine it all','👁️'],['Beyin kısayollar kullanır: “ani renk değişimi = köşe”, “eğik kenar = hareket”','So it uses shortcuts — “sudden colour change = corner”, “tilted edge = motion”',''],['Bu kısayollar gerçek dünyada neredeyse hep doğrudur','These shortcuts are right almost all the time in the real world',''],['Yanılsamalar, kısayolların yanıldığı nadir anları yakalar','Illusions catch the rare moments when the shortcuts go wrong','']],
    'Yanılsama bir kusur değil; beynin ne kadar hızlı tahmin yaptığının kanıtı','An illusion is not a flaw — it is proof of how fast the brain predicts','#24242c','#08080b',gap=7,d=54),
  fact('80 ms','Gördüğün şey, aslında yaklaşık 80 milisaniye önce olmuştu; beyin bu gecikmeyi tahminle kapatır','What you see happened about 80 milliseconds ago — the brain covers the delay by predicting','Bu yüzden hızlı giden bir topu “olduğu yerde” değil, “olacağı yerde” görürüz · That is why we see a fast ball where it will be, not where it is','#1f2830','#06090c',d=32),
]),
S(16,17,'Zamanın Tanıkları · Witnesses of Time',[
  photo('bristlecone','Ak Dağlar, Kaliforniya · White Mountains, California','Büyük Havza kıl çamı: rüzgârın yonttuğu, yarısı ölü, yarısı yaşayan bir gövde','A Great Basin bristlecone pine — a trunk carved by wind, half dead, half alive','Bu türden bilinen en yaşlı ağaç yaklaşık 4.800 yaşında: filizlendiğinde Mısır piramitleri henüz yapılmamıştı','The oldest known tree of this kind is about 4,800 years old — when it sprouted, the Egyptian pyramids had not yet been built',d=42),
  photo('horseshoecrab','Atlantik nal yengeci · Atlantic horseshoe crab','Nal yengeci: adı yengeç ama aslında örümceklerin ve akreplerin uzak akrabası','The horseshoe crab — called a crab, but really a distant cousin of spiders and scorpions','Atalarına benzeyen canlılar 400 milyon yıldan uzun süredir denizde; kanı mavidir ve ilaç testlerinde kullanılır','Creatures like it have lived in the sea for over 400 million years — its blood is blue and is used to test medicines for safety',d=42),
  steps('Ölçek Yolculuğu · Scale Journey','Bir yaşam ne kadar uzun?','How long is a life?',
    [['Bir mayıs sineğinin yetişkin hayatı: bir gün kadar','A mayfly’s adult life — about a day','🕐'],['Bir insan: yaklaşık 80 yıl','A human — about 80 years',''],['Grönland köpekbalığı: 270 yıldan fazla olabilir','A Greenland shark — possibly more than 270 years',''],['Kıl çamı: 4.800 yıl; bazı süngerler ve klonal ormanlar daha da uzun','A bristlecone pine — 4,800 years; some sponges and clonal forests even longer','']],
    'Hepsi aynı Güneş’in altında, kendi saatiyle yaşıyor','All of them live under the same Sun, each by its own clock','#1d2a22','#060a07',gap=8,d=56),
  q('Hayatına gelen değişimlere direnme;|bırak hayat senin içinden yaşasın','Do not resist the changes that come your way — let life live through you','sea',d=44),
  rid('Hep ileri gider, asla geri dönmez; görünmez ama her şeyi değiştirir. Nedir?','It always goes forward and never comes back; it is invisible but changes everything. What is it?','Zaman!','Time!',sec=16,c1='#28241c',c2='#090806'),
]),
S(17,18,'Zekice Düşünce: En Kısa Yol · Clever Thinking: The Shortest Path',[
  g('hztsp',d=80),
  steps(CT,'Königsberg’in yedi köprüsü: hepsinden birer kez geçip başladığın yere dönebilir misin?','The seven bridges of Königsberg: can you cross each exactly once and return to the start?',
    [['Kentin ortasında bir nehir, iki ada ve yedi köprü vardı','The city had a river, two islands and seven bridges','🌉'],['Halk yıllarca denedi; kimse başaramadı','People tried for years — nobody managed it',''],['1736’da Euler haritayı noktalara ve çizgilere indirdi','In 1736 Euler reduced the map to dots and lines',''],['Kural: her noktaya çift sayıda köprü değmeli. Königsberg’de dördü de tekti','The rule: every dot needs an even number of bridges. In Königsberg all four were odd','']],
    'İmkânsız! Ve bu sorudan bugünün ağ biliminin temeli olan “çizge kuramı” doğdu','Impossible! And from this puzzle grew graph theory — the basis of today’s network science','#1b2a33','#060a0d',gap=8,d=58),
  photo('physarum','Physarum polycephalum','Sarı bir balçık mantarı: beyni yok, ama yiyecekleri birbirine bağlayan en verimli yolları buluyor','A yellow slime mould — it has no brain, yet it finds efficient routes linking its food','2010’da Japon bilim insanları yulafları Tokyo çevresindeki kentlere göre dizdi; balçığın ağı demiryolu ağına çok benzedi','In 2010 Japanese scientists placed oat flakes like the cities around Tokyo — the slime’s network closely matched the railway map',d=44),
  rid('Bir kurbağa merdivenin dibinde. Her zıplayışta 1 ya da 2 basamak çıkabiliyor. İlk 3 basamağa kaç farklı yoldan çıkar?','A frog at the foot of a staircase can hop up 1 or 2 steps at a time. In how many different ways can it climb 3 steps?','3 yol: 1+1+1, 1+2, 2+1. (4 basamak için 5, 5 için 8: Fibonacci!)','3 ways: 1+1+1, 1+2, 2+1. (4 steps give 5, 5 give 8 — Fibonacci!)',sec=24,d=38,c1='#1f2a1c',c2='#070a06'),
]),
S(18,19,'Antik Mühendislik · Ancient Engineering',[
  photo('pontdugard','Pont du Gard, Fransa · France','Pont du Gard: Roma su kemerinin üç katlı taş köprüsü, harç kullanılmadan oturtulmuş bloklar','The Pont du Gard — a three-tier Roman aqueduct bridge of blocks laid without mortar','Kemer 50 km boyunca her kilometrede yalnızca yaklaşık 25 cm alçalıyordu: su yalnızca yerçekimiyle Nîmes’e akıyordu','The aqueduct fell only about 25 cm per kilometre over 50 km — water reached Nîmes by gravity alone',fit='contain',d=44),
  photo('cistern','Yerebatan Sarnıcı · Basilica Cistern, İstanbul','Yerebatan Sarnıcı: suyun üstünde yükselen yüzlerce sütun ve loş ışık','The Basilica Cistern — hundreds of columns rising from the water in dim light','6. yüzyılda yapıldı; 80.000 metreküpten fazla su tutabilir ve 336 sütunu vardır','Built in the 6th century, it can hold more than 80,000 cubic metres of water and has 336 columns',d=42),
  photo('antikythera','Antikythera Mekanizması · Antikythera Mechanism, Atina','Antikythera Mekanizması: bir batıktan çıkan, dişlilerle dolu bronz parçalar','The Antikythera mechanism — bronze fragments full of gears, recovered from a shipwreck','Yaklaşık 2.100 yıl önce yapıldı; Ay’ın evrelerini ve tutulmaları hesaplayan bir “analog bilgisayar”','Made about 2,100 years ago, it is an “analogue computer” that predicted the Moon’s phases and eclipses',fit='contain',d=44),
  photo('yazd','Dolat Abad Bahçesi, Yezd · Yazd, İran','Yezd’de Dolat Abad köşkü ve 33 metrelik rüzgâr kulesi (badgir)','The Dolat Abad pavilion in Yazd and its 33-metre windcatcher (badgir)','Kule, esintiyi yakalayıp içeri indirir; sıcak hava yukarıdan çıkar. Elektriksiz bir klima','The tower catches the breeze and draws it down inside while hot air escapes above — air conditioning without electricity',d=42),
  steps(CT,'Elektrik yokken suyu şehre nasıl getirirsin?','How do you bring water to a city without electricity?',
    [['Kaynağı şehirden biraz daha yüksekte bul','Find a spring a little higher than the city','⛰️'],['Kanalı çok hafif bir eğimle döşe: su kendiliğinden aksın','Lay a channel with a very gentle slope so the water flows by itself',''],['Vadileri kemerlerle, tepeleri tünellerle geç','Cross valleys on arches and hills through tunnels',''],['Şehirde büyük sarnıçlarda depola','Store it in great cisterns in the city','']],
    'Roma’nın ve Bizans’ın kentleri, pompasız yalnızca yerçekimiyle yaşadı','The cities of Rome and Byzantium lived on gravity alone — no pumps','#2a241c','#0a0806',gap=7,d=54),
]),
S(19,20,'Uzay Araçlarının Gözünden · Through the Eyes of Spacecraft',[
  photo('marsselfie','Curiosity, Mars','Curiosity gezgininin Mars’taki “özçekimi”: birçok kareden birleştirilmiş, kolu görüntüden silinmiş','Curiosity rover’s “selfie” on Mars — stitched from many frames, with its arm removed from view','Curiosity bir arabadan büyük; 2012’den beri Gale Krateri’nde 30 km’den fazla yol aldı','Curiosity is bigger than a car — since 2012 it has driven more than 30 km in Gale Crater',fit='contain',d=42),
  photo('marssunset','Mars’ta gün batımı · Sunset on Mars','Mars’ta gün batımı: Güneş’in çevresindeki ışık mavi','Sunset on Mars — the glow around the Sun is blue','Dünya’da gün batımı kızıldır; Mars’ta tersine mavidir, çünkü ince toz mavi ışığı Güneş’in yönünde saçar','On Earth sunsets are red; on Mars they turn blue, because fine dust scatters blue light towards the Sun’s direction',fit='contain',d=42),
  photo('juno','Jüpiter, Juno','Juno uzay aracından Jüpiter’in bulutları: girdaplar ve mavi akıntılar (renkler güçlendirilmiş)','Jupiter’s clouds from the Juno spacecraft — swirls and blue currents (colours enhanced)','Bu fotoğraflar amatörler tarafından işlendi: NASA, Juno’nun ham görüntülerini herkesin kullanımına açıyor','These images were processed by amateurs — NASA releases Juno’s raw pictures for anyone to use',fit='contain',d=42),
  photo('pluto','Plüton, New Horizons','Plüton’un gerçek renkleri: güneyindeki açık renkli kalp biçimli buz ovası','Pluto in true colour — the pale, heart-shaped plain of ice in its south','New Horizons, 9,5 yıllık yolculuktan sonra 2015’te Plüton’un yanından geçti; bu fotoğrafın Dünya’ya ulaşması günler sürdü','New Horizons flew past Pluto in 2015 after a 9.5-year journey — sending this picture home took days',fit='contain',d=42),
  steps('Ölçek Yolculuğu · Scale Journey','Uzaydan gelen bir fotoğraf eve ne kadar sürede ulaşır?','How long does a picture from space take to reach home?',
    [['Ay’dan: yaklaşık 1,3 saniye','From the Moon — about 1.3 seconds','🌙'],['Mars’tan: 3 ile 22 dakika arası','From Mars — between 3 and 22 minutes',''],['Jüpiter’den: 35 ile 52 dakika','From Jupiter — 35 to 52 minutes',''],['Plüton’dan: yaklaşık 4,5 saat','From Pluto — about 4.5 hours','']],
    'Mars’taki bir gezgine “dur” dersen, sözün ulaştığında çoktan çukura düşmüş olabilir — bu yüzden kendi kendine sürmeyi bilir','Tell a Mars rover to “stop” and by the time the word arrives it could already be in a ditch — so it knows how to drive itself','#1c1f2e','#05060c',gap=8,d=58),
]),
S(20,21,'Gezegenin Tuhaf Canlıları · The Planet’s Strangest Creatures',[
  photo('axolotl','Aksolotl · Axolotl','Aksolotl: hep gülümsüyor gibi duran, kafasında tüylü solungaçlar taşıyan bir semender','The axolotl — a salamander with feathery gills that always seems to be smiling','Kopan bacağını, hatta kalbinin ve beyninin bazı bölümlerini yeniden büyütebilir','It can regrow a lost leg — even parts of its heart and brain',d=40),
  photo('seadragon','Yapraklı deniz ejderi · Leafy seadragon','Yapraklı deniz ejderi: yosun gibi görünen yapraklarla süslü, denizatının akrabası','The leafy seadragon — a seahorse relative dressed in leaf-like fins that look like seaweed','Yalnızca Avustralya’nın güney kıyılarında yaşar; yavruları baba taşır','It lives only off southern Australia — and it is the father who carries the eggs',fit='contain',d=40),
  photo('glassfrog','Cam kurbağası · Glass frog','Cam kurbağası bir yaprağın üstünde, yanında yumurtaları','A glass frog on a leaf beside its eggs','Karnının derisi saydamdır: altından kalbinin attığını görebilirsin. Uyurken kanını karaciğerinde saklayıp neredeyse görünmez olur','The skin of its belly is transparent — you can watch its heart beat. Asleep, it hides its blood in its liver and almost vanishes',d=40),
  photo('mantisshrimp','Palyaço peygamberdevesi karidesi · Peacock mantis shrimp','Palyaço peygamberdevesi karidesi: gökkuşağı renkli bir avcı','The peacock mantis shrimp — a rainbow-coloured hunter','Kıskaçlarını bir mermi hızıyla savurur: darbesi akvaryum camını kırabilir. Gözlerinde 12–16 tür renk alıcısı var','It swings its clubs as fast as a bullet — a blow can crack aquarium glass. Its eyes have 12–16 kinds of colour receptors',d=40),
  photo('shoebill','Pabuçgaga · Shoebill','Pabuçgaga: tahta pabuca benzeyen gagasıyla dinozor bakışlı bir kuş','The shoebill — a bird with a clog-shaped bill and a dinosaur stare','Saatlerce kıpırdamadan bekleyebilir; sonra tek hamlede bir balığı yakalar','It can stand still for hours — then catch a fish in a single lunge',d=40),
  fact('3,5 milyar','Dünya’da yaşam yaklaşık 3,5 milyar yıldır var; bugün yaşayan türlerin çoğuna henüz bir ad bile verilmedi','Life on Earth is about 3.5 billion years old — most of today’s species have not even been named yet','Tahminlere göre türlerin yalnızca küçük bir kısmı bilimsel olarak tanımlandı · Only a small share of species is thought to be described by science','#1c2a24','#060a08',d=32),
]),
S(21,22,'Dahilerin Defterleri · Notebooks of Genius',[
  art('vitruvian','Vitruvius Adamı — Leonardo da Vinci, yaklaşık 1490','Vitruvian Man — Leonardo da Vinci, about 1490','Kol açıklığı boya eşit: Leonardo, insan bedeninin oranlarını bir kare ve bir çemberle ölçtü','Arm span equals height — Leonardo measured the body’s proportions with a square and a circle'),
  art('leoflying','Uçan makine çizimi — Leonardo da Vinci','Drawing of a flying machine — Leonardo da Vinci','Leonardo notlarını ayna yazısıyla, sağdan sola yazardı; defterleri yaklaşık 7.000 sayfa olarak günümüze ulaştı','Leonardo wrote his notes in mirror script, right to left — about 7,000 pages of his notebooks survive'),
  art('darwin','“I think” — Charles Darwin’in defteri, 1837','“I think” — Charles Darwin’s notebook, 1837','Bu karalama, bir türün dallanarak yeni türlere ayrıldığını gösteren ilk “yaşam ağacı” çizimi','This scribble is his first “tree of life” — showing one species branching into new ones'),
  art('lovelace','Ada Lovelace — Alfred Edward Chalon, yaklaşık 1840','Ada Lovelace — Alfred Edward Chalon, about 1840','1843’te henüz yapılmamış bir makine için ilk algoritmayı yazdı ve makinelerin bir gün müzik besteleyebileceğini öngördü','In 1843 she wrote the first algorithm for a machine not yet built — and foresaw that machines might one day compose music'),
  photo('ramanujan','Srinivasa Ramanujan (1887–1920)','Srinivasa Ramanujan: neredeyse kendi kendine öğrenmiş Hint matematikçi','Srinivasa Ramanujan — the almost self-taught Indian mathematician','Yaklaşık 3.900 sonuç bıraktı; defterlerindeki bazı formüller ancak onlarca yıl sonra kanıtlanabildi','He left about 3,900 results — some formulas in his notebooks were only proven decades later',fit='contain',d=40),
  q('Söz ola kese savaşı, söz ola kestire başı;|söz ola ağulu aşı bal ile yağ ede bir söz','A word can end a war, a word can cost a head — a word can turn a poisoned meal to honey and butter','ink',d=46,lb='Yunus Emre',by='Yunus Emre, 13.–14. yüzyıl · 13th–14th century'),
]),
S(22,23,'Kıyıda Akşam · Evening by the Shore (sakin · calm)',[
  photo('altincamp','Altınkum, Burhaniye · Ege kıyısı · Aegean coast','Sakin bir denizin üstünde batan güneş ve suda uzanan sıcak turuncu bir yol','The sun setting over a calm sea, a warm orange path stretching across the water','Güneş battıktan sonra yaklaşık yarım saat boyunca gökyüzü aydınlık kalır; denizciler buna “sivil alacakaranlık” der','For about half an hour after sunset the sky stays light — sailors call it civil twilight',d=46),
  photo('nightport','Trabzon, Meydan’dan gece · Trabzon at night','Gece Trabzon: Meydan’dan sokak ışıkları ve şehrin sıcak pencereleri','Trabzon at night — street lights and the warm windows of the city seen from Meydan','Meydan Parkı yüzyıllardır şehrin buluşma yeri; bugün de akşam çayı için en çok tercih edilen köşelerden','Meydan Park has been the city’s meeting place for centuries — still a favourite corner for evening tea',d=46),
  steps('Sakin Düşünce · Calm Thought','Bugünden üç güzel an','Three good moments from today',
    [['Bugün seni gülümseten küçük bir şeyi hatırla','Remember a small thing that made you smile today','☾'],['Bugün tattığın güzel bir şeyi','Something good you tasted today',''],['Ve yarın için beklediğin tek bir şeyi','And one thing you are looking forward to tomorrow','']],
    'Günü güzel anlarıyla kapatmak, uykuyu da yumuşatır','Closing the day with its good moments softens sleep too','#121a26','#03050a',gap=9,d=50,bg='stars'),
  q('Sana verilen zorluğu kabul ettiğin an,|kapı açılır','The moment you accept what troubles you have been given, the door opens','night',d=46),
]),
S(23,26,'Gece Balıkçıları · Night Fishermen (sakin · calm)',[
  g('hzbalikci',d=90),
  photo('fishnight','Limanda gece · Harbour at night — Pattaya, Tayland · Thailand','Sessiz bir limanda gece dinlenen balıkçı tekneleri ve suya düşen ışıklar','Fishing boats resting in a quiet harbour at night, their lights falling on the water','Durgun su bir ayna gibidir: ışığın yansıması, dalga ne kadar küçükse o kadar keskin görünür','Still water is a mirror — the smaller the ripples, the sharper the reflection of the lights',d=46),
  q('Sabır acıdır,|meyvesi tatlıdır','Patience is bitter, but its fruit is sweet','night',d=44,lb='Türk Atasözü · Turkish Proverb',by='atasözü · proverb'),
  fact('4°C','Kışın gölün dibi en soğuk değil: su en yoğun hâline 4 °C’de ulaşır ve dibe çöker; buz üstte kalır','In winter the bottom of a lake is not the coldest place — water is densest at 4 °C and sinks, while ice stays on top','Bu yüzden balıklar donmuş göllerin altında kışı geçirebilir · That is why fish survive winter under frozen lakes','#121c2a','#03060a',d=34),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-19.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
