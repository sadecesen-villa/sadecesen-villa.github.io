# (Pattern from build_2026-11-17.py) Builds /workspace/tv-pages/days/2026-11-18.json (hourly sets 09:00-02:00). Wednesday: fractal coasts, painters of nature, chance, knowing & seeing, garden nooks, motion illusions, outward scale, nature's engineers, calm evening (undersea, lost cities, Earth from above, mountains, water), campfire night.
import json,os
DATE='2026-11-18'; REV=69; NEXT='2026-11-19'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-18.json')))
FIX={'Audubon, John James':'John James Audubon','Unknown author':'Narodowe Archiwum Cyfrowe (NAC)','Russo Francesco':'Francesco Russo','NASA and the European Space Agency':'NASA / ESA','NASA/JPL/Space Science Institute':'NASA / JPL / Space Science Institute','NASA/JPL/NIMA':'NASA / JPL / NIMA','NASA/JPL-Caltech':'NASA / JPL-Caltech','NASA/Bill Anders':'NASA / Bill Anders','Roy Egloff':'Roy Egloff','CopyrightFreePhotos':'CopyrightFreePhotos','Grand Canyon NPS':'Grand Canyon National Park (NPS)','Clarisse Meyer':'Clarisse Meyer','Bernard DUPONT':'Bernard Dupont','Bob Henricks':'Bob Henricks','Forest Wander':'Forest Wander','Credits to Mourad Ben Abdallah':'Mourad Ben Abdallah','NASA image courtesy of the DSCOVR':'NASA / DSCOVR EPIC','blgrssby from St. Louis':'blgrssby','al-Jazari':'el-Cezerî · al-Jazari (1315 kopyası · copy, The Met)','Ala ad-Din Mansur-Shirazi':'Alaeddin Mansur · Ala ad-Din Mansur-Shirazi (Şehinşahname, 1581)','NOIRLab/NSF/AURA':'NOIRLab / NSF / AURA','卓珺 黄':'Zhuojun Huang','none (Landsat)':'NASA / USGS Landsat','Kritzolina':'Claude Monet (detay · detail; foto · photo: Kritzolina)','Dale Cruse':'Dale Cruse'}
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
    it=dict(k='hzphoto',d=d,f='m/h18-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
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
    it=dict(k='hzguess',d=d,f='m/h18-%s.jpg'%k,lb='Bil Bakalım · Can You Guess? — '+REAL+' · '+where,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr=cr(k))
    if hint: it['hint']=hint
    return it
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=[i for i in items if i])
TE='Düşünce Deneyi · Thought Experiment'; CT='Zekice Düşünce · Clever Thinking'
sets=[
S(9,10,'Çarşamba Sabahı · Wednesday Morning',[
  photo('ataturkkosk','Atatürk Köşkü, Soğuksu · Trabzon','Atatürk Köşkü — Soğuksu’da, ağaçların arasında beyaz bir yazlık köşk','The Atatürk Pavilion — a white summer mansion among the trees of Soğuksu','Atatürk 1937’deki Trabzon ziyaretinde burada kaldı; köşk bugün müze olarak gezilebiliyor','Atatürk stayed here on his 1937 visit to Trabzon — today the mansion is a museum',d=42),
  q('Kapı ardına kadar açıkken|neden hapiste kalıyorsun?','Why do you stay in prison when the door is so wide open?','sea',d=44),
  photo('seragolu','Sera Gölü, Akçaabat · Trabzon','Sera Gölü — Trabzon’un hemen batısında, ormanla çevrili sakin bir göl','Sera Lake — a calm lake ringed by forest just west of Trabzon','Göl, bir heyelanın vadiyi kapatmasıyla oluşmuş bir “set gölü”','It is a landslide-dammed lake — a landslide blocked the valley and the water collected behind it',d=40),
  fact('Çarşamba','“Çarşamba” Farsça “çehâr-şenbe”den gelir: “cumartesiden sonraki dördüncü gün”','“Çarşamba” (Wednesday) comes from Persian chahār-shanbe — “the fourth day after Saturday”','Pazartesi = pazar ertesi; Çarşamba = dördüncü gün · Each weekday name hides a count','#1c2c2e','#050808',d=30),
  rid('Her şeyi yer ama hiç doymaz; su içerse ölür. Nedir?','It eats everything but is never full — if it drinks water, it dies. What is it?','Ateş!','Fire!',sec=16,c1='#2a2418',c2='#080604'),
]),
S(10,11,'Yaşayan Sanat: Fraktal Kıyılar · Living Art: Fractal Coasts',[
  g('hzmandel',d=84),
  photo('norwaycoast','Norveç, uzaydan · Norway from space — uydu · satellite','Norveç kıyısı uzaydan: fiyortlar ve adalarla dantel gibi bir kıyı; açıktaki turkuaz girdaplar bir plankton patlaması','The coast of Norway from space — a lace of fjords and islands; the turquoise swirls offshore are a plankton bloom','1967’de Benoit Mandelbrot sordu: “Britanya’nın kıyısı ne kadar uzun?” Cetvel küçüldükçe ölçülen kıyı uzuyor','In 1967 Benoit Mandelbrot asked: “How long is the coast of Britain?” The smaller the ruler, the longer the coast',fit='contain',d=44),
  steps('Zekice Düşünce · Clever Thinking','Kıyı paradoksu: bir kıyının uzunluğu kaç kilometre?','The coastline paradox: how many kilometres long is a coast?',
    [['100 km’lik bir cetvelle ölç: koyların çoğunu atlarsın','Measure with a 100 km ruler — you skip most of the bays','📏'],['10 km’lik cetvel koylara girer: kıyı uzar','A 10 km ruler dips into the bays — the coast gets longer',''],['1 metrelik cetvel her kayanın etrafından dolanır: daha da uzar','A 1 m ruler goes round every rock — longer still',''],['Cetvel küçüldükçe uzunluk büyümeye devam eder','The smaller the ruler, the more the length keeps growing','']],
    'Kıyının tek bir “gerçek” uzunluğu yok; sonuç ölçeğe bağlı — fraktalların imzası','A coast has no single “true” length — it depends on the scale, the signature of a fractal','#0f3a40','#061a1d',gap=7,d=54),
  photo('oaktree','Çıplak meşe · Bare oak','Yapraklarını dökmüş bir meşe: her dal, ağacın küçük bir kopyası gibi','An oak without its leaves — every branch looks like a small copy of the tree','Aynı dallanma deseni nehirlerde, akciğerlerdeki hava yollarında ve şimşekte de görülür','The same branching pattern appears in rivers, in the airways of our lungs and in lightning',d=40),
]),
S(11,12,'Galeri: Doğanın Ressamları · Gallery: Painters of Nature',[
  art('hare','Genç Tavşan — Albrecht Dürer, 1502','Young Hare — Albrecht Dürer, 1502','Suluboya ve guaş; tavşanın gözünde atölyenin penceresinin yansıması seçilir','Watercolour and gouache — look closely and a studio window is reflected in the hare’s eye'),
  art('turf','Büyük Çim Parçası — Albrecht Dürer, 1503','The Large Piece of Turf — Albrecht Dürer, 1503','Karahindiba, sinirotu ve çayır otları: sıradan bir çim parçası, başlı başına bir konu oluyor','Dandelions, plantain and meadow grasses — an ordinary patch of turf becomes the whole subject'),
  art('audubon','Karolina Papağanı — John James Audubon, “Amerika’nın Kuşları”, 1827–1838','Carolina Parakeet — John James Audubon, “The Birds of America”, 1827–1838','Bu tür artık yok: bilinen son Karolina papağanı 1918’de Cincinnati Hayvanat Bahçesi’nde öldü','The species is gone — the last known Carolina parakeet died at Cincinnati Zoo in 1918'),
  art('merian','Muz çiçeği ve meyvesi — Maria Sibylla Merian, 1705','Banana flower and fruit — Maria Sibylla Merian, 1705','Merian 52 yaşında Surinam’a gitti; bitkileri ve böcekleri yaşam döngüleriyle birlikte çizdi','At 52 Merian sailed to Suriname and drew plants and insects together with their life cycles'),
  art('ruysch','Vazoda Yaz Çiçekleri — Rachel Ruysch','Summer Flowers in a Vase — Rachel Ruysch','Ruysch altmış yılı aşkın resim yaptı ve döneminin en çok kazanan ressamları arasındaydı','Ruysch painted for more than sixty years and was among the best-paid painters of her time'),
]),
S(12,13,'Zekice Düşünce: Rastlantının Gücü · Clever Thinking: The Power of Chance',[
  g('hzbuffon',d=70),
  photo('buffon','Comte de Buffon','Buffon — 18. yüzyılın doğa bilimcisi; iğne problemini ortaya attı','Buffon — the 18th-century naturalist who posed the needle problem','Portre · Portrait: François-Hubert Drouais','Portrait by François-Hubert Drouais',fit='contain',d=32),
  steps(CT,'Eratosthenes, Dünya’nın çevresini bir çubuk ve bir gölgeyle nasıl ölçtü?','How did Eratosthenes measure the Earth with a stick and a shadow?',
    [['Yaz gündönümünde öğlen, Syene’de (Asvan) Güneş tam tepedeydi: gölge yok','At noon on the summer solstice the Sun stood straight overhead at Syene (Aswan) — no shadow','☀'],['Aynı anda İskenderiye’de bir çubuk gölge veriyordu: yaklaşık 7,2°','At the same moment a stick in Alexandria cast a shadow — about 7.2°',''],['7,2° bir dairenin 1/50’si demek','7.2° is one fiftieth of a full circle',''],['İki şehir arası yaklaşık 5.000 stadyon × 50','The cities were about 5,000 stadia apart — times 50','']],
    'Sonuç: yaklaşık 250.000 stadyon — MÖ 3. yüzyılda, gerçek değere şaşırtıcı derecede yakın','About 250,000 stadia — astonishingly close to the true value, in the 3rd century BC','#2a2418','#080604',gap=7,d=56),
  steps(CT,'Hayatta kalan yanılgısı: uçağın neresine zırh koymalı?','Survivorship bias: where should a plane get extra armour?',
    [['II. Dünya Savaşı: dönen uçaklarda kurşun delikleri sayılıyor','World War II: bullet holes are counted on the planes that come back','✈'],['Delikler en çok kanatlarda ve gövdede','Most holes are on the wings and fuselage',''],['İlk fikir: zırhı deliklerin olduğu yere koy','First idea: armour where the holes are',''],['İstatistikçi Abraham Wald: delik olmayan yerlere bakın — oradan vurulanlar geri dönemedi','Statistician Abraham Wald: look where there are no holes — planes hit there never came back','']],
    'Ders: yalnızca “hayatta kalanlara” bakarsan, eksik veriyi görmezsin','Lesson: if you only study the survivors, you miss the data that matters most','#16202e','#04070b',gap=7,d=54),
  rid('Bir zar attın, 6 geldi. Hemen bir daha atarsan 6 gelme şansı azalır mı?','You roll a die and get a 6. If you roll again right away, is a 6 less likely now?','Hayır! Yine 1/6 — zarın hafızası yoktur','No — it is still 1 in 6. Dice have no memory (the gambler’s fallacy)',sec=18,c1='#1d2f3c',c2='#05080c'),
  fact('3,14','14 Mart, Amerikan tarih yazımıyla 3/14 olduğu için dünyada “Pi Günü” olarak kutlanıyor','14 March is written 3/14 in the US — so it is celebrated around the world as “Pi Day”','Buffon’un iğnesi: rastlantıdan bile π çıkıyor · Even chance points to π','#16202e','#04070b',d=28),
]),
S(13,14,'Düşünce Deneyleri: Bilmek ve Görmek · Thought Experiments: Knowing & Seeing',[
  steps(TE,'Mary’nin Odası: renk hakkında her şeyi bilen biri, kırmızıyı ilk kez görünce yeni bir şey öğrenir mi?','Mary’s Room: if someone knows everything about colour, does she learn something new when she first sees red?',
    [['Mary bir bilim insanı; siyah-beyaz bir odada büyüyor','Mary is a scientist who grows up in a black-and-white room','🔬'],['Işık, göz ve beyin hakkında fiziksel olarak bilinen her şeyi öğreniyor','She learns every physical fact about light, eyes and the brain',''],['Bir gün kapı açılıyor ve kırmızı bir elma görüyor','One day the door opens and she sees a red apple','🍎']],
    'Yeni bir şey öğrendi mi? Öğrendiyse, bilgi yalnızca fizikten mi ibaret? (Frank Jackson, 1982)','Did she learn something new? If so, is knowledge more than physical facts? (Frank Jackson, 1982)','#2a1f3a','#080510',gap=7.5,d=54),
  photo('schrodinger','Erwin Schrödinger','Erwin Schrödinger — 1935’te kuantum fiziğinin tuhaflığını göstermek için bir kedi düşünce deneyi önerdi','Erwin Schrödinger — in 1935 he proposed a cat thought experiment to show how strange quantum physics is','1933 Nobel Fizik Ödülü’nü Paul Dirac ile paylaştı','He shared the 1933 Nobel Prize in Physics with Paul Dirac',fit='contain',d=34),
  steps(TE,'Schrödinger’in Kedisi: kutudaki kedi hem canlı hem ölü olabilir mi?','Schrödinger’s Cat: can a cat in a box be both alive and dead?',
    [['Kapalı bir kutuda bir kedi ve tek bir radyoaktif atom var (yalnızca düşüncede!)','A closed box holds a cat and a single radioactive atom (only in thought!)','📦'],['Atom bir saat içinde %50 ihtimalle bozunur; bozunursa bir mekanizma çalışır','The atom has a 50 % chance to decay within an hour — if it does, a device is triggered',''],['Kuantum fiziğine göre atom, ölçülene kadar iki durumun “üst üste binmesi”nde','Quantum physics says the atom is in a “superposition” of both states until measured',''],['O zaman kedi de kutu açılana kadar hem canlı hem ölü mü?','Then is the cat both alive and dead until the box is opened?','']],
    'Schrödinger bunu bir eleştiri olarak, sonucun ne kadar tuhaf olduğunu göstermek için önerdi','Schrödinger meant it as a critique — to show how absurd the conclusion seems','#14202e','#04080e',gap=7,d=56),
  q('Hayatını ateşe ver;|alevini körükleyenleri ara','Set your life on fire — seek those who fan your flames','clay',d=44),
  steps(TE,'Molyneux’nün sorusu: doğuştan görmeyen biri görmeye başlasa, küpü ve küreyi gözüyle ayırabilir mi?','Molyneux’s question: if a person born blind gains sight, can they tell a cube from a sphere by sight alone?',
    [['William Molyneux bu soruyu 1688’de filozof John Locke’a yazdı','William Molyneux sent this question to the philosopher John Locke in 1688','✉'],['Kişi küpü ve küreyi dokunarak çok iyi tanıyor','The person knows a cube and a sphere perfectly by touch',''],['Gözleri açılınca, dokunmadan hangisinin hangisi olduğunu bilebilir mi?','Once they can see, can they tell which is which without touching?','']],
    '2011’de yeni görmeye başlayan çocuklarla yapılan bir çalışma: ilk anda hayır — ama birkaç gün içinde öğrendiler','A 2011 study with newly sighted children: not at first — but they learned within days','#22301f','#050805',gap=7.5,d=52),
  rid('Bir horoz çatının tam tepesinde yumurtlarsa, yumurta hangi tarafa düşer?','If a rooster lays an egg right on the ridge of a roof, which side does the egg roll down?','Hiçbir tarafa — horoz yumurtlamaz!','Neither — roosters don’t lay eggs!',sec=16,c1='#2a2418',c2='#080604'),
]),
S(14,15,'Villa Fikirleri: Bahçe ve Köşeler · Villa Ideas: Garden & Nooks',[
  villa('firepit','bahçe ateşi · fire pit','Bahçede bir ateş çukuru: serin Karadeniz akşamlarında dostlarla oturmak için','A garden fire pit — for sitting with friends on cool Black Sea evenings','Taş ya da çelik bir ateş çukuru, binaya ve ağaçlara güvenli mesafede kurulmalı','A stone or steel fire pit should sit at a safe distance from the house and trees'),
  villa('pizzaoven','ekmek fırını · bread oven, Grand Canyon','Bahçede kerpiçten bir ekmek fırını yapılıyor: köy fırını geleneği, misafirlerle pişen pide ve ekmek','A clay bread oven being built in a garden — village tradition, pide and bread baked together with guests','Odun fırını ısıyı duvarlarında saklar; ateş söndükten sonra da saatlerce pişirmeye devam eder','A wood-fired oven stores heat in its walls and keeps baking for hours after the fire dies down'),
  villa('herbgarden','ot bahçesi · herb garden','Ot bahçesinde yaşlı bir zeytin ağacı (Polis, Kıbrıs)','An old olive tree in a herb garden (Polis, Cyprus)','Biberiye ve kekik güneşli, kuru toprağı sever; nane ve maydanoz nemli, yarı gölge yerleri','Rosemary and thyme love sunny, dry soil; mint and parsley prefer moist, half-shaded spots'),
  villa('hammock','hamak · hammock','Ağaçların arasında bir hamak: bahçenin en sakin köşesi','A hammock between trees — the quietest corner of the garden','“Hamak” kelimesi Karayipler’deki Taíno dilinden gelir; Avrupa’ya İspanyol gemicilerle ulaştı','The word “hammock” comes from the Taíno language of the Caribbean, brought to Europe by Spanish sailors'),
  rid('Karnı ateşle dolar ama hiç yanmaz; içine giren hamur ekmek olur. Nedir?','Its belly fills with fire but it never burns — dough goes in and comes out as bread. What is it?','Fırın!','An oven!',sec=16,c1='#2a2418',c2='#080604'),
]),
S(15,16,'Göz Oyunları: Hareket ve Kenar · Tricks of the Eye: Motion & Edges',[
  g('hzouchi',d=50),
  g('hzbarber',d=56),
  photo('beuchet','Beuchet sandalyesi · Beuchet chair','Beuchet sandalyesi: tek bir delikten bakınca parçalar tek bir sandalye gibi birleşiyor','The Beuchet chair — seen through one peephole, separate pieces merge into one chair','Parçalar aslında farklı uzaklıklarda duruyor; tek gözle tek noktadan bakınca beyin derinliği yanlış okuyor','The pieces actually stand at different distances — from one viewpoint, with one eye, the brain misreads depth',fit='contain',d=38),
  g('hzmach',d=50),
  photo('hollowmask','İçi oyuk maske · Hollow mask','İçi oyuk bir maske: içeriden bakınca bile yüz dışa doğru çıkıyormuş gibi görünür','A hollow mask — even from the inside, the face seems to bulge outwards','Beyin yüzleri hep dışbükey görmeye öyle alışkın ki, ışık ve gölge ipuçlarını göz ardı eder','The brain is so used to faces being convex that it overrides the light-and-shadow clues',fit='contain',d=36),
  fact('Mach','Ses hızı birimi “Mach” da, Mach bantlarını 1865’te tanımlayan aynı Avusturyalı bilim insanının adını taşır: Ernst Mach','The speed-of-sound unit “Mach” is named after the same Austrian scientist who described Mach bands in 1865 — Ernst Mach','Bir göz yanılsaması ve bir hız birimi, tek isim · One illusion, one speed unit, one name','#16202e','#04070b',d=30),
]),
S(16,17,'Ölçek Yolculuğu: Dışarı Doğru · Scale Journey: Outward',[
  photo('earthrise','Dünya Doğuşu · Earthrise — Apollo 8','Dünya Doğuşu — Apollo 8, 24 Aralık 1968: Ay’ın ufkundan yükselen Dünya','Earthrise — Apollo 8, 24 December 1968: the Earth rising over the Moon’s horizon','Astronot Bill Anders’ın çektiği bu kare, Ay yörüngesinden insan eliyle çekilen ilk renkli Dünya fotoğraflarından','Taken by astronaut Bill Anders, it is one of the first colour photos of Earth taken by a person from lunar orbit',fit='contain',d=42),
  steps('Ölçek Yolculuğu · Scale Journey','Işık hızıyla yolculuk: saniyede yaklaşık 300.000 km','Travelling at the speed of light — about 300,000 km every second',
    [['Ay’a: 1,3 saniye','To the Moon: 1.3 seconds','🌙'],['Güneş’e: 8 dakika 20 saniye','To the Sun: 8 minutes 20 seconds','☀'],['En yakın yıldız Proxima Centauri’ye: 4,2 yıl','To the nearest star, Proxima Centauri: 4.2 years','✦'],['Samanyolu’nun bir ucundan öbürüne: yaklaşık 100.000 yıl','Across the Milky Way: about 100,000 years',''],['Andromeda Galaksisi’ne: yaklaşık 2,5 milyon yıl','To the Andromeda Galaxy: about 2.5 million years','']],
    'Evrende en hızlı yolcu bile çoğu yere varamaz — uzaklık, zamana dönüşür','Even the fastest traveller in the universe never reaches most places — distance turns into time','#0e1624','#020306',gap=6.5,d=58,bg='stars'),
  photo('palebluedot','Soluk Mavi Nokta · Pale Blue Dot — Voyager 1','Soluk Mavi Nokta: Voyager 1’in 1990’da yaklaşık 6 milyar km uzaktan çektiği Dünya — ışık huzmesindeki minik nokta','The Pale Blue Dot — Earth seen by Voyager 1 in 1990 from about 6 billion km: the tiny speck in the sunbeam','Fotoğrafı Carl Sagan önerdi; bu sürüm NASA’nın 2020’de yenilediği görüntü','Carl Sagan suggested taking it — this is NASA’s 2020 reprocessed version',fit='contain',d=42),
  photo('hudf','Hubble Ultra Derin Alan · Hubble Ultra Deep Field','Hubble Ultra Derin Alan: dolunayın onda birinden küçük bir gökyüzü parçasında yaklaşık 10.000 galaksi','The Hubble Ultra Deep Field — about 10,000 galaxies in a patch of sky smaller than a tenth of the full Moon','Her ışık noktası bir yıldız değil, milyarlarca yıldızlı bir galaksi','Almost every speck here is not a star but a galaxy of billions of stars',fit='contain',d=42),
  photo('andromeda','Andromeda Galaksisi · Andromeda Galaxy','Andromeda — çıplak gözle görülebilen en uzak nesnelerden, yaklaşık 2,5 milyon ışık yılı uzakta','Andromeda — one of the most distant things visible to the naked eye, about 2.5 million light years away','Bu gece gördüğün Andromeda ışığı yola çıktığında Dünya’da henüz modern insan yoktu','When the Andromeda light you see tonight set out, there were no modern humans on Earth yet',d=42),
  rid('Ay ile Dünya arasına yan yana kaç Dünya sığar? 3 mü, 30 mu, 300 mü?','How many Earths fit side by side between the Earth and the Moon? 3, 30 or 300?','Yaklaşık 30!','About 30!',hint='Ay yaklaşık 384.000 km uzakta, Dünya’nın çapı yaklaşık 12.700 km · The Moon is ~384,000 km away; Earth is ~12,700 km wide',sec=20,c1='#14202e',c2='#04080e'),
]),
S(17,18,'Doğanın Mühendisleri · Nature’s Engineers',[
  photo('beaver','Kunduz barajı, Polonya · Beaver dam, Poland','Kunduz barajı: dallar, çamur ve taşla yapılmış bir set','A beaver dam — a barrier of branches, mud and stones','Kunduzlar suyu biriktirip yuvalarının girişini su altında tutar; böylece avcılardan korunurlar','Beavers pool the water so their lodge entrance stays underwater, safe from predators',d=40),
  steps('Doğanın Mühendisleri · Nature’s Engineers','Bir kunduz barajı nasıl kurulur?','How does a beaver build a dam?',
    [['Akan suyun sesi kunduzu harekete geçirir','The sound of running water spurs the beaver into action','🦫'],['Dişleriyle ağaç ve dal keser, dere yatağına dizer','It cuts trees and branches with its teeth and lays them across the stream',''],['Sızıntıları çamur ve taşla kapatır','It plugs the leaks with mud and stones',''],['Arkada bir gölet oluşur; yuva girişi suyun altında kalır','A pond forms behind — the lodge entrance ends up underwater','']],
    'Bir kunduz ailesi bütün bir vadinin su düzenini değiştirebilir','A single beaver family can reshape the water of an entire valley','#22301f','#050805',gap=7,d=52),
  photo('termite','Termit tepesi · Termite mound','Termit tepesi: içindeki tüneller havalandırma kanalı gibi çalışıyor','A termite mound — its tunnels work like ventilation ducts','Zimbabve’nin başkenti Harare’deki Eastgate Center, termit tepelerinden ilham alan doğal havalandırmasıyla bilinir','The Eastgate Centre in Harare, Zimbabwe, is known for natural ventilation inspired by termite mounds',d=40),
  photo('spiderweb','Örümcek ağı · Spider web','Çiy damlalarıyla süslenmiş bir örümcek ağı','A spider web beaded with dew','Örümcek ipeği, ağırlığına oranla çelikten daha sağlamdır','Weight for weight, spider silk is stronger than steel',d=40),
  photo('caddis','Su güvesi larvası · Caddisfly larva','Su güvesi larvası: minik taşlardan kendine taşınabilir bir ev yapıyor','A caddisfly larva — building itself a portable house of tiny stones','Larva, taş ve kum tanelerini kendi ürettiği ipeksi bir salgıyla suyun altında yapıştırır','Underwater, the larva glues grains of sand and stone together with silk it makes itself',d=40),
  rid('Evini sırtında taşır, hiç acele etmez; yağmurdan sonra ortaya çıkar. Nedir?','It carries its house on its back, never hurries, and comes out after the rain. What is it?','Salyangoz!','A snail!',sec=16,c1='#22301f',c2='#050805'),
]),
S(18,19,'Deniz Altında Sessizlik · Quiet Under the Sea',[
  photo('reef','Kızıldeniz, Şarm El-Şeyh · Red Sea, Sharm el-Sheikh','Kızıldeniz’de bir Acropora mercanı: binlerce minik polipten oluşan bir koloni','An Acropora coral in the Red Sea — a colony of thousands of tiny polyps','Mercan resifleri okyanus tabanının %1’inden azını kaplar ama deniz canlılarının yaklaşık dörtte birine ev sahipliği yapar','Coral reefs cover less than 1 % of the ocean floor yet are home to about a quarter of marine species',d=48),
  photo('turtle','Yeşil deniz kaplumbağası · Green sea turtle','Galápagos’ta süzülen bir yeşil deniz kaplumbağası','A green sea turtle gliding in the Galápagos','Dişi deniz kaplumbağaları yumurtlamak için çoğu kez doğdukları kumsala geri döner','Female sea turtles often return to the very beach where they hatched to lay their eggs',d=48),
  photo('manta','Dev manta vatozu · Giant manta ray','Mavinin içinde kanat çırpar gibi yüzen bir dev manta','A giant manta ray “flying” through the blue','Kanat açıklığı 7 metreye yaklaşabilir; beyni, vücuduna oranla balıklar arasında en büyüklerden','Its wingspan can approach 7 metres — and its brain is among the largest of any fish for its body size',d=48),
  photo('kelp','Kelp ormanı · Kelp forest','Su altında bir kelp ormanı: ışık, yaprakların arasından süzülüyor','An underwater kelp forest — light filtering down through the fronds','Dev kelp uygun koşullarda günde yaklaşık 60 cm uzayabilir','In good conditions, giant kelp can grow about 60 cm in a single day',d=48),
  photo('seahorse','Denizatı · Seahorse','Bir yosuna kuyruğuyla tutunmuş denizatı','A seahorse holding on to seaweed with its tail','Denizatlarında yavruları erkek taşır ve doğurur','In seahorses it is the male that carries the young and gives birth',fit='contain',d=48),
]),
S(19,20,'Kayıp Kentler · Lost Cities',[
  photo('ani','Ani, Kars','Ani — Arpaçay kıyısında “bin bir kilise” kenti; Ani Katedrali','Ani — the “city of a thousand and one churches” on the Arpaçay river; Ani Cathedral','Katedral 1001 yılında tamamlandı; Ani 2016’da UNESCO Dünya Mirası listesine girdi','The cathedral was completed in 1001 — Ani joined the UNESCO World Heritage list in 2016',d=46),
  photo('sagalassos','Sagalassos, Burdur','Sagalassos — Toros Dağları’nda yüksekte bir antik kent; Antoninler Çeşmesi','Sagalassos — an ancient city high in the Taurus Mountains; the Antonine Nymphaeum','Çeşme kazılardan sonra parça parça yeniden ayağa kaldırıldı ve yeniden su akmaya başladı','The fountain was rebuilt piece by piece after excavation — and water flows through it again',fit='contain',d=46),
  photo('hattusa','Hattuşa, Çorum','Hattuşa — Hititlerin başkenti; Aslanlı Kapı','Hattusa — capital of the Hittites; the Lion Gate','Burada bulunan Kadeş Antlaşması tabletleri, bilinen en eski yazılı barış antlaşmalarından; Hattuşa 1986’dan beri UNESCO listesinde','The Kadesh treaty tablets found here are among the oldest known written peace treaties — Hattusa has been on the UNESCO list since 1986',d=46),
  photo('afrodisias','Afrodisias, Aydın','Afrodisias — Tetrapylon, kentin anıtsal kapısı','Aphrodisias — the Tetrapylon, the city’s monumental gateway','Antik çağda mermer heykel atölyeleriyle ünlüydü; 2017’de UNESCO listesine girdi','In antiquity it was famous for its marble sculptors — it joined the UNESCO list in 2017',d=46),
  steps('Kayıp Kentler · Lost Cities','Arkeologlar toprağın altındaki bir kenti nasıl bulur?','How do archaeologists find a city under the ground?',
    [['Tarlada yüzeye çıkmış çanak çömlek kırıklarını haritalarlar','They map pottery shards that have surfaced in the fields','🏺'],['Havadan bakınca bitkilerin farklı büyüdüğü çizgiler duvarları ele verir','From the air, lines where crops grow differently give away buried walls',''],['Lazer taramayla (LIDAR) ormanın altındaki yapılar bile görülebilir','Laser scanning (LIDAR) can reveal structures even under forest',''],['Kazıda her toprak katmanı, bir zaman sayfası gibi okunur','When digging, every soil layer is read like a page of time','']],
    'Bir kent kaybolabilir; ama bıraktığı izler toprakta bekler','A city can be lost — but its traces wait in the soil','#2a2418','#080604',gap=7.5,d=56),
]),
S(20,21,'Kuşbakışı Dünya · Earth from Above',[
  photo('richat','Richat Yapısı, Moritanya · Richat Structure, Mauritania','Richat Yapısı — Sahra’nın “gözü”, yaklaşık 40 km çapında halkalar','The Richat Structure — the “Eye of the Sahara”, rings about 40 km across','Uzun süre bir göktaşı kraterine benzetildi; bugün aşınmış bir kubbe yapısı olduğu düşünülüyor','Long thought to be an impact crater, it is now seen as an eroded geological dome',fit='contain',d=46),
  photo('namib','Namib Çölü, uydudan · Namib Desert from space','Namib Çölü uydudan: Atlas Okyanusu’na kadar uzanan kum denizi','The Namib Desert from space — a sea of sand running down to the Atlantic','Namib, dünyanın en eski çöllerinden biri sayılır','The Namib is considered one of the oldest deserts on Earth',fit='contain',d=46),
  photo('istanbulnight','İstanbul, uzaydan · Istanbul from space','Uzaydan gece İstanbul: Boğaz’ın karanlık çizgisi ışıkları ikiye ayırıyor','Istanbul at night from space — the dark line of the Bosphorus splits the lights in two','Uluslararası Uzay İstasyonu yaklaşık 400 km yükseklikte, Dünya’nın çevresini yaklaşık 90 dakikada dolaşır','The International Space Station orbits about 400 km up and circles the Earth in about 90 minutes',d=46),
  fact('Genel Bakış','Astronotların uzaydan Dünya’yı görünce yaşadığı derin hayranlık ve bağlılık duygusuna “genel bakış etkisi” denir','The deep awe and sense of connection astronauts feel when they see Earth from space is called the “overview effect”','Terimi yazar Frank White 1987’de kullandı · Coined by author Frank White in 1987','#0e1624','#020306',d=32),
]),
S(21,22,'Dağların Sessizliği · Quiet Mountains',[
  photo('erciyes','Erciyes Dağı, Kayseri · Mount Erciyes','Erciyes Dağı ve önünde Kayseri’den bir cami','Mount Erciyes, with a Kayseri mosque in front','3.917 metre; Kapadokya’nın peribacalarını oluşturan tüfler bu bölgedeki volkanların küllerinden','3,917 m — the tuff that forms Cappadocia’s fairy chimneys came from the ash of volcanoes like this one',d=46),
  photo('aladaglar','Demirkazık, Aladağlar · Niğde','Demirkazık Dağı, Aladağlar — kireçtaşından keskin zirveler','Mount Demirkazık in the Aladağlar — sharp limestone peaks','Demirkazık yaklaşık 3.756 metre; Aladağlar Türkiye’nin en sevilen tırmanış bölgelerinden','Demirkazık is about 3,756 m — the Aladağlar are among Turkey’s favourite climbing ranges',d=46),
  photo('matterhorn','Matterhorn, İsviçre · Switzerland','Matterhorn ve bir dağ gölündeki yansıması','The Matterhorn and its reflection in a mountain lake','4.478 metre; zirvesine ilk kez 1865’te çıkıldı','4,478 m — first climbed in 1865',d=46),
  photo('everest','Everest, Himalayalar · Himalayas','Everest — dünyanın en yüksek zirvesi','Everest — the highest summit on Earth','2020’deki ortak Çin–Nepal ölçümüne göre 8.848,86 metre','8,848.86 m according to the joint China–Nepal survey of 2020',d=46),
  q('Dağ dağa kavuşmaz,|insan insana kavuşur','Mountains never meet, but people do','night',d=44,lb='Atasözü · Turkish Proverb',by='Türk atasözü · Turkish proverb'),
]),
S(22,23,'Su Sesi · The Sound of Water (sakin · calm)',[
  photo('tortum','Tortum Şelalesi, Erzurum','Tortum Şelalesi — Türkiye’nin en yüksek şelalelerinden','Tortum Waterfall — one of the highest waterfalls in Turkey','Su yaklaşık 48 metre yüksekten dökülür; en coşkulu hâli ilkbaharda kar suları erirken','The water falls about 48 m — at its fullest in spring, when the snow melts',fit='contain',d=46),
  photo('kapuzbasi','Kapuzbaşı Şelaleleri, Kayseri','Kapuzbaşı Şelaleleri — kayalığın içinden fışkıran kaynak suları','Kapuzbaşı Waterfalls — spring water bursting out of the cliff face','Aladağlar’ın eteklerinde, Zamantı Irmağı vadisinde','At the foot of the Aladağlar, in the valley of the Zamantı river',d=46),
  photo('mossstream','Yosunlu kayalar · Mossy rocks','Yosunlu kayaların arasında yavaşça dönen bir su birikintisi','A pool turning slowly among mossy rocks','Akan suyun sesi birçok farklı frekansı birden taşır; pek çok insan onu bu yüzden sakinleştirici bulur','The sound of flowing water carries many frequencies at once — which is why so many people find it soothing',d=46),
  steps('Sakin Düşünce · Calm Thought','Gözlerini kapat: dört sesi bul','Close your eyes and find four sounds',
    [['En uzaktaki sesi bul','Find the farthest sound','☾'],['Sonra en yakındakini','Then the nearest one',''],['Odanın içindeki küçük bir sesi','A small sound inside the room',''],['Ve seslerin arasındaki sessizliği','And the silence between the sounds','']],
    'Dinlemek de bir dinlenmedir','Listening is a kind of rest','#0e1624','#020306',gap=8,d=48,bg='stars'),
]),
S(23,26,'Kamp Ateşi ve Yıldızlar · Campfire & Stars (sakin · calm)',[
  g('hzember',d=84),
  photo('startrail','Yıldız izleri · Star trails','Uzun pozlamada yıldız izleri: kamera Dünya’nın dönüşünü kaydediyor','Star trails in a long exposure — the camera records the Earth turning','Kutup Yıldızı gök kutbuna çok yakın olduğu için neredeyse kımıldamaz; diğer yıldızlar onun çevresinde daire çizer','Polaris sits so close to the celestial pole that it barely moves — other stars circle around it',d=44),
  photo('moon','Dolunay · Full Moon','Dolunay — kraterler ve karanlık “denizler”','The full Moon — craters and dark “seas”','Ay her yıl Dünya’dan yaklaşık 3,8 cm uzaklaşıyor','The Moon drifts about 3.8 cm farther from Earth every year',fit='contain',d=44),
  photo('saturn','Satürn, Cassini · Saturn, Cassini','Arkadan aydınlanan Satürn: Cassini uzay aracı gezegenin gölgesinden bakıyor','Saturn lit from behind — the Cassini spacecraft looking back from the planet’s shadow','Halkalar yüz binlerce kilometre genişliğinde, ama çoğu yerde yalnızca onlarca metre kalınlığında','The rings are hundreds of thousands of kilometres wide, but in most places only tens of metres thick',fit='contain',d=44),
  photo('nightvillage','Göl ve dağlar · Lake and mountains','Dağların ardında son ışık; göle sakin bir akşam iniyor','The last light behind the mountains — a calm evening settles on the lake','Gökyüzü gün batımından sonra da bir süre aydınlık kalır: buna alacakaranlık denir','The sky stays bright for a while after sunset — that glow is twilight',d=44),
  q('Gönül ne kahve ister ne kahvehane;|gönül sohbet ister, kahve bahane','The heart wants neither coffee nor a coffeehouse — it wants company; coffee is the excuse','night',d=46,lb='Türk Sözü · Turkish Saying',by='Türk sözü · Turkish saying'),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-18.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
