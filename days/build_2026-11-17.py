# (Pattern from build_2026-11-16.py) Builds /workspace/tv-pages/days/2026-11-17.json (hourly sets 09:00-02:00). Tuesday: flow, autumn gallery, thinking, sound, animals, colour, geometry, migration, first snow.
import json,os
DATE='2026-11-17'; REV=68; NEXT='2026-11-18'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-17.json')))
FIX={'Credits to Mourad Ben Abdallah':'Mourad Ben Abdallah','NASA image courtesy of the DSCOVR':'NASA / DSCOVR EPIC','blgrssby from St. Louis':'blgrssby','al-Jazari':'el-Cezerî · al-Jazari (1315 kopyası · copy, The Met)','Ala ad-Din Mansur-Shirazi':'Alaeddin Mansur · Ala ad-Din Mansur-Shirazi (Şehinşahname, 1581)','NOIRLab/NSF/AURA':'NOIRLab / NSF / AURA','卓珺 黄':'Zhuojun Huang','none (Landsat)':'NASA / USGS Landsat','Kritzolina':'Claude Monet (detay · detail; foto · photo: Kritzolina)','Dale Cruse':'Dale Cruse'}
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
    it=dict(k='hzphoto',d=d,f='m/h17-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it
def villa(k,where,tr,en,fact,facte,fit=None,d=42):
    it=photo(k,'',tr,en,fact,facte,fit=fit,d=d)
    it['lb']='Villa Fikri · Villa Idea — ilham · inspiration (gerçek foto · real photo · %s)'%where
    return it
def art(k,tr,en,fact,facte,d=44):
    it=photo(k,'',tr,en,fact,facte,fit='contain',d=d)
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
    it=dict(k='hzguess',d=d,f='m/h17-%s.jpg'%k,lb='Bil Bakalım · Can You Guess? — '+REAL+' · '+where,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr=cr(k))
    if hint: it['hint']=hint
    return it
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
TE='Düşünce Deneyi · Thought Experiment'; CT='Zekice Düşünce · Clever Thinking'
sets=[
S(9,10,'Salı Sabahı · Tuesday Morning',[
  photo('sumela','Sümela, Maçka · Trabzon','Sümela Manastırı — sisin içinden yükselen kayalar ve ormanlar','Sümela Monastery — rocks and forest rising out of the mist','Manastır, vadinin yüzlerce metre üzerinde, kayalığa oyulmuş gibi duruyor; efsaneye göre kuruluşu MS 4. yüzyıla uzanır','The monastery clings to the cliff hundreds of metres above the valley — legend dates its founding to the 4th century AD',d=42),
  q('Dün akıllıydım, dünyayı değiştirmek istedim;|bugün bilgeyim, kendimi değiştiriyorum','Yesterday I was clever and wanted to change the world; today I am wise and am changing myself','night',d=46),
  photo('altindere','Altındere Vadisi · Trabzon','Altındere Vadisi — Sümela’ya giden yolun yeşil dağları','Altındere Valley — the green mountains on the way to Sümela','Vadi, nadir bitki ve hayvan türleri için milli park olarak korunuyor','The valley is protected as a national park for its rare plants and animals',fit='contain',d=40),
  fact('Salı','“Salı” kelimesi Arapçada “üçüncü” anlamına gelen bir kelimeden gelir; haftanın üçüncü günü','“Salı” (Tuesday) comes from an Arabic word meaning “third” — the third day of the week','Eski haftada sayım pazardan başlardı · The old week counted from Sunday','#1c2c2e','#050808',d=30),
  rid('Karanlık bir odaya girdin. Bir mum, bir gaz lambası ve bir şömine var, ama elinde tek kibrit. İlk önce neyi yakarsın?','You enter a dark room with a candle, a gas lamp and a fireplace — but only one match. What do you light first?','Kibriti!','The match!',sec=16,c1='#2a2418',c2='#080604'),
]),
S(10,11,'Yaşayan Sanat: Akış · Living Art: Flow',[
  g('hzflow',d=64),
  photo('lena','Sibirya · Siberia — uydu · satellite','Lena Deltası — nehrin binlerce kolu, uzaydan bir ağaç gibi','The Lena Delta — a river’s thousand arms, a tree seen from space','Sibirya’daki bu delta yaklaşık 30.000 km²; kış boyunca donuyor, yaz aylarında bin kadar adaya bölünüyor','This Siberian delta covers about 30,000 km² — frozen all winter, split into around a thousand islands in summer',d=44),
  photo('romanesco','Romanesko karnabahar','Romanesko — her tomurcuk bütünün küçük bir kopyası','Romanesco — every bud is a small copy of the whole','Spiral sayıları hep Fibonacci sayıları çıkar; doğada fraktal yapı çok sevilen bir hile','The spirals always count out as Fibonacci numbers — nature loves a fractal trick',d=40),
  photo('jelly','Ay denizanası · Moon jelly','Aurelia: ışıkta cam gibi yüzen bir denizanası','Aurelia — a jellyfish drifting like glass in the light','Kalbi ve beyni yok; vücudunun yaklaşık %95’i su, yine de yüz milyonlarca yıldır akıntıyla yaşıyor','No heart, no brain, about 95 % water — yet its kind has ridden the currents for hundreds of millions of years',d=40),
  rid('Bir kutuda 3 elma var. Sen 2 tanesini aldın. Kaç elman var?','There are 3 apples in a box. You take 2. How many apples do you have?','2 elma! Aldığın elmalar sende','2 apples — the ones you took',sec=14,c1='#16202e',c2='#04070b'),
]),
S(11,12,'Galeri: Sonbahar ve Yağmur · Gallery: Autumn & Rain',[
  art('friedrich','Sis Denizinin Üzerinde Gezgin — Caspar David Friedrich, yaklaşık 1818','Wanderer above the Sea of Fog — Caspar David Friedrich, c. 1818','Romantik çağın en tanınmış sahnesi: bir adam, kayalar ve aşağıda sis','The best-known scene of Romanticism: one man, rocks and a sea of fog below'),
  art('shishkin','Çam Ormanında Sabah — Ivan Shishkin, 1889','Morning in a Pine Forest — Ivan Shishkin, 1889','Ormanı Shishkin çizdi; ayıları arkadaşı Konstantin Savitsky ekledi','Shishkin painted the forest — his friend Konstantin Savitsky added the bears'),
  art('poplars','Epte Nehri Kıyısında Kavaklar — Claude Monet, 1891','Poplars on the Epte — Claude Monet, 1891','Monet aynı kavak sırasını sabah, öğle ve akşam ışığında defalarca resmetti','Monet painted the same row of poplars again and again in morning, noon and evening light'),
  art('hiroshige','Şin-Ohaşi Köprüsü’nde Ani Sağanak — Utagawa Hiroshige, 1857','Sudden Shower over Shin-Ōhashi Bridge — Utagawa Hiroshige, 1857','Van Gogh 1887’de bu baskıyı tuvale kopyaladı; yağmuru ince çizgilerle gösteren bir usta','Van Gogh copied this print onto canvas in 1887 — a master of showing rain with fine lines'),
  art('lily','Nilüfer Havuzu (detay) — Claude Monet','The Water-Lily Pond (detail) — Claude Monet','Monet, Giverny’deki bahçesinde yaklaşık 250 nilüfer tablosu yaptı','In his garden at Giverny, Monet painted around 250 water-lily pictures'),
  fact('1857','Hiroshige’nin “Edo’nun 100 Ünlü Manzarası” dizisi, yağmuru ve karı çizgiyle anlatmanın en güzel örneklerinden','Hiroshige’s “One Hundred Famous Views of Edo” still shows how rain and snow can be drawn with just lines','Sanatçı: yağmuru çizmek için yağmur yağmasını beklemedi, hafızasından çizdi · Many of them were drawn from memory','#1c2c2e','#050808',d=30),
]),
S(12,13,'Zekice Düşünce: Örüntüyü Gör · Clever Thinking: See the Pattern',[
  g('hzrule',d=60),
  photo('gauss','Carl Friedrich Gauss','Gauss — okulda “1’den 100’e kadar topla” denince birkaç saniyede cevabı buldu (efsaneye göre)','Gauss — told to add 1 to 100, he found the answer in seconds (so the story goes)','Portre, 1840, Christian Albrecht Jensen','Portrait, 1840, Christian Albrecht Jensen',fit='contain',d=34),
  steps(CT,'1’den 100’e kadar olan sayıları toplamanın kısa yolu','The shortcut for adding the numbers from 1 to 100',
    [['1 + 100 = 101','1 + 100 = 101','1'],['2 + 99 = 101','2 + 99 = 101',''],['3 + 98 = 101 … hep aynı toplam!','3 + 98 = 101 … always the same!',''],['Bu şekilde 50 çift var: 50 × 101','There are 50 such pairs: 50 × 101','']],
    '= 5050. Toplamadan, örüntüyü görerek','= 5050 — by seeing the pattern instead of adding','#16202e','#04070b',gap=6.5,d=48),
  steps(CT,'Doğum günü paradoksu: bir sınıfta iki kişinin doğum günü aynı olur mu?','The birthday paradox: do two people in a room share a birthday?',
    [['Sınıfta 23 kişi olsun','Say there are 23 people in a room','👥'],['Her iki kişiyi eşleştir: 253 farklı çift var','Pair everyone up: there are 253 different pairs',''],['Her çiftin tutma şansı küçük ama 253 şansın var','Each pair has a small chance — but you have 253 chances','']],
    'Sonuç: ihtimal %50’yi geçiyor; 57 kişide %99','The chance is already over 50 % — and 99 % with 57 people','#22301f','#050805',gap=7,d=46),
  rid('Bir gölde nilüfer her gün iki katına çıkıyor. 48 günde bütün gölü kaplıyor. Gölün yarısını kaçıncı günde kaplamıştır?','Water lilies on a pond double in size every day. They cover the whole pond in 48 days. When did they cover half of it?','47. gün! Ertesi gün iki katına çıkar','Day 47 — the next day they double',sec=18,c1='#1d2f3c',c2='#05080c'),
  fact('256','Bu tür tek sıralı hücresel otomat için tam 256 kural var; çoğu sıkıcı, yalnızca birkaçı — 30, 90, 110 — şaşırtıcı','There are exactly 256 rules for this kind of one-row automaton — most are dull, only a few (30, 90, 110) are astonishing','Basit kural, karmaşık sonuç · Simple rule, complex result','#16202e','#04070b',d=32),
]),
S(13,14,'Düşünce Deneyleri: Kimlik ve Sonsuzluk · Thought Experiments: Identity & Infinity',[
  steps(TE,'Theseus’un Gemisi: bütün tahtaları değişen gemi hâlâ aynı gemi midir?','The Ship of Theseus: if every plank is replaced, is it still the same ship?',
    [['Atinalılar, efsanevi kahraman Theseus’un gemisini yıllarca saklıyor','The Athenians keep the legendary ship of Theseus for years','⛵'],['Çürüyen her tahta yenisiyle değiştiriliyor','Each rotting plank is replaced by a new one',''],['Sonunda gemideki tüm tahtalar yeni','In the end, every plank is new',''],['Eski tahtalarla başka biri bir gemi kursa, hangisi Theseus’un gemisi?','If someone rebuilds a ship from the old planks — which is Theseus’s ship?','']],
    'Kimlik, parçalarda mı yoksa süreklilikte mi?','Is identity in the parts — or in the continuity?','#0f3a40','#061a1d',gap=7,d=58),
  photo('hilbertpic','Otel koridoru · Hotel corridor','Sonsuz uzun bir otel koridoru düşün — odaların sonu yok','Imagine an endless hotel corridor — the rooms never end','Bu fotoğraf gerçek bir otel koridoru; sonsuz otel yalnızca bir düşünce deneyi','This is a real hotel corridor; the infinite hotel is only a thought experiment',d=36),
  steps(TE,'Hilbert’in Oteli: odaları sonsuz ve hepsi dolu bir otelde yeni misafire yer var mı?','Hilbert’s Hotel: in a fully booked hotel with infinite rooms, is there space for a new guest?',
    [['Sonsuz odalı otel, tüm odalar dolu','An infinite hotel, every room taken','🏨'],['Yeni bir misafir geliyor: herkes bir yan odaya geçer (n → n+1)','A new guest arrives: everyone moves one room along (n → n+1)',''],['1 numaralı oda boşalır','Room 1 is free',''],['Peki sonsuz sayıda misafir gelirse? Herkes numarasının iki katına geçer (n → 2n)','What if infinitely many guests arrive? Everyone moves to double their room number (n → 2n)','']],
    'Tek numaralı odalar boş kalır: sonsuzlukta “dolu”, “yer yok” demek değil','All the odd rooms are free: with infinity, “full” doesn’t mean “no room”','#14202e','#04080e',gap=7,d=58),
  q('Gel, her ne olursan ol yine gel;|bizim kapımız umutsuzluk kapısı değildir','Come, whoever you are, come again — ours is not a door of despair','sea',d=46),
  steps(TE,'Çin Odası: sembolleri doğru döndürmek, anlamak mıdır?','The Chinese Room: is shuffling symbols correctly the same as understanding?',
    [['Kapalı bir odadasın ve Çince bilmiyorsun','You are in a closed room and know no Chinese','📕'],['Elinde yalnızca sembollerle dolu kalın bir kural kitabı var','You have only a thick book of rules for symbols',''],['Kapıdan Çince sorular giriyor; kitaba bakıp doğru sembolleri geri veriyorsun','Chinese questions come in; you look up the rules and send the right symbols back',''],['Dışarıdaki kişi senin Çince bildiğini sanıyor','The person outside thinks you understand Chinese','']],
    'Cevap vermek, anlamakla aynı şey mi? (John Searle, 1980)','Is answering the same as understanding? (John Searle, 1980)','#2a2418','#080604',gap=7,d=56),
  rid('Dört duvarı da güneye bakan bir ev yaptın. Bahçeye bir ayı geliyor. Ayı ne renk?','You build a house with all four walls facing south. A bear walks into the garden. What colour is the bear?','Beyaz! Böyle bir ev yalnızca Kuzey Kutbu’nda olabilir','White — such a house can only stand at the North Pole',sec=18,c1='#2a2418',c2='#080604'),
]),
S(14,15,'Villa Fikirleri: Butik Otel Ayrıntıları · Villa Ideas: Boutique-Hotel Details',[
  villa('fire','şömineli salon · a room with a fireplace','Beyaz mermer şömine ve yüksek pencereler: oda ısınmadan önce bile sıcak görünüyor','A white marble fireplace and tall windows — the room looks warm before it is warmed','Butik otellerde şömine genellikle odanın “sahnesi” olur: koltuklar ona dönük dizilir','In boutique hotels the fireplace is the room’s “stage” — the chairs all face it',fit='contain'),
  villa('library','kütüphane köşesi · a library nook','Zemin kattan tavana kadar kitap rafları: ev bir anda sakin bir çalışma salonuna dönüşüyor','Shelves from floor to ceiling — the house becomes a calm reading room','Raflar duvar boyunca değil de pencere kenarında ve merdiven altında da kullanılabilir','Shelves can also line a window or sit under the stairs')    ,
  villa('pergola','asma yaprağı gölgeli yol · a vine-shaded path','Asmalı bir ahşap çardak: yazın gölge, sonbaharda yaprakların rengi','A wooden pergola with vines — shade in summer, colour in autumn','Asma Karadeniz iklimini sever; bahçede hem gölge hem üzüm demektir','Vines like the Black Sea climate — shade and grapes in one',fit='contain'),
  villa('sadirvan','şadırvan · a courtyard fountain','Şadırvan: ortasında su sesi olan taş bir avlu pavyonu','A şadırvan — a stone courtyard pavilion with the sound of water at its centre','Suyun sesi şehir gürültüsünü örter; küçük bir çeşme bile bahçeye ses katar','The sound of water masks noise — even a small fountain gives a garden a voice',d=42),
  villa('lantern','göl kenarında yürüyüş yolu · a lakeside path','Bahçe gölü, taş yol ve ağaçlar: ışıkları akşam yakınca aynı yer başka bir hikâye anlatır','A garden pond, a stone path and trees — light it at dusk and the same place tells a different story','Yola yerleştirilen alçak ışıklar, gözü ışığa değil yola yönlendirir','Low lights along a path guide the eye to the way, not to the lamp'),
  rid('Başı var ama saçı yok; dişi var ama ağzı yok. Nedir?','It has a head but no hair, and teeth but no mouth. What is it?','Sarımsak!','Garlic!',sec=16,c1='#22301f',c2='#050805'),
]),
S(15,16,'Göz Oyunları: Beynin Hileleri · Tricks of the Eye: The Brain’s Shortcuts',[
  g('hzchecker',d=44),
  g('hzscint',d=34),
  photo('ames','Ames Odası · Ames room','Ames Odası: aynı boydaki iki kişi biri dev, biri minik görünür','The Ames room — two people of the same height look like a giant and a dwarf','Oda aslında yamuk; ama tek gözle bakınca düz bir küp gibi görünür','The room is actually lopsided — from one eye’s view it looks like a normal box',fit='contain',d=40),
  photo('pisa','Borromini Galerisi, Roma · Rome','Zorlamalı perspektif: kısa bir koridor çok daha uzun görünüyor','Forced perspective — a short corridor that looks far longer','Roma’daki Palazzo Spada’da bu galeri yaklaşık 8 m; sütunlar ve zemin kademeli küçültülmüş, uzun gösteriyor','At Palazzo Spada in Rome the gallery is only about 8 m long — columns and floor shrink step by step to fake the depth',d=42),
  rid('Aynada sağ ile sol yer değiştirir ama yukarı ile aşağı değişmez. Neden?','A mirror swaps left and right but not up and down. Why?','Aslında ayna sağ-solu değil, ön-arkayı çevirir; sağ-sol dönüşünü biz kendimizi çevirirken yaratıyoruz','A mirror really flips front and back — the left-right swap comes from how we imagine turning around',sec=22,c1='#1d2f3c',c2='#05080c'),
  fact('1995','Edward Adelson’ın gölgeli dama tahtası illüzyonu 1995’te yayımlandı; beyin, ışığı ve gölgeyi birbirinden ayırıp “kâğıdın gerçek rengini” bulmaya çalışır','Edward Adelson published his checker-shadow illusion in 1995 — the brain separates light from shadow to guess a surface’s “true colour”','Görme bir kamera değil, bir tahmin makinesi · Vision is not a camera but a guessing machine','#2a2418','#080604',d=32),
]),
S(16,17,'Ölçek Yolculuğu: İçeri Doğru · Scale Journey: Inward',[
  steps('Ölçek Yolculuğu · Scale Journey','Her adımda 10 kat küçülelim: bir kum tanesinden atoma','Shrinking ten times at each step: from a grain of sand to an atom',
    [['1 mm: bir kum tanesi gözle görünür','1 mm: a grain of sand — visible to the eye','🔍'],['100 µm: bir çiçek tozu tanesi','100 µm: a grain of pollen',''],['10 µm: tek bir hücre','10 µm: a single cell',''],['1 µm: bir bakteri','1 µm: a bacterium',''],['100 nm: bir virüs','100 nm: a virus',''],['2 nm: DNA sarmalının genişliği','2 nm: the width of the DNA helix',''],['0,1 nm: tek bir atom','0.1 nm: a single atom','']],
    'Kum tanesinden atoma sadece 7 adım — her biri 10 kat','Just seven steps from a grain of sand to an atom — ten times each','#14202e','#04080e',gap=6,d=62),
  photo('pollen','Çiçek tozları · Pollen grains','Renklendirilmiş elektron mikroskobu: çiçek tozu taneleri bir şeker dükkânı gibi','Colourised electron microscope: pollen grains like a sweet shop','Her bitki türünün polen tanesi farklıdır; bilim insanları geçmiş iklimleri polenlerden okur','Every plant species has its own pollen shape — scientists read past climates from it',d=42),
  photo('diatom','Diyatomlar · Diatoms','Mikroskopta cam gibi parlayan diyatomlar: tek hücreli, silikadan kabuklu','Diatoms glowing like glass under the microscope — single cells in silica shells','Okyanuslarda yaşayan bu canlılar Dünya’nın oksijeninin yaklaşık beşte birini üretir','These tiny sea dwellers make about a fifth of the oxygen we breathe',d=42),
  photo('butterflywing','Kelebek kanadı · Butterfly wing','Bir kelebek kanadının pulları: kiremit gibi dizilmiş renkli küçük levhalar','Scales on a butterfly wing — tiny coloured tiles laid like a roof','Her pul yaklaşık 0,1 mm; bazı renkler boyadan değil, ışığı kıran mikroskobik yapıdan gelir','Each scale is about 0.1 mm — some colours come from light-bending structure, not pigment',fit='contain',d=40),
  rid('Sağ elinle asla tutamayacağın, ama sol elinle kolayca tutabileceğin şey nedir?','What can you easily hold in your left hand but never in your right hand?','Sağ dirsek!','Your right elbow!',sec=16,c1='#2a2418',c2='#080604'),
  q('Damlaya damlaya|göl olur','Drop by drop, a lake is made','sea',d=40,lb='Atasözü · Turkish Proverb',by='Türk atasözü · Turkish proverb'),
]),
S(17,18,'Ses ve Müzik: Titreşimin Sanatı · Sound & Music: The Art of Vibration',[
  g('hzlissa',d=64),
  photo('kanun','Kanun · Qanun','Kanun: yatay duran, parmak halkalarıyla çalınan bir tel sarayı','The kanun — a horizontal zither played with plectra on the fingertips','Türk kanununda genellikle her nota için üç tel vardır; küçük mandallarla çeyrek ses ince ayarı yapılır','A Turkish kanun usually has three strings per note — small levers fine-tune the quarter tones',d=44),
  steps('Sesin Matematiği · The Maths of Sound','Bir telin yarısını tutunca ne olur?','What happens when you stop a string halfway?',
    [['Bir tel çalıyorsun: bir nota duyulur','You pluck a string: one note','🎻'],['Telin tam yarısını tut: nota iki kat sık titreşir — bir oktav yukarı','Stop it at the middle: it vibrates twice as fast — an octave higher',''],['Üçte ikisini tut: ilk notayla en uyumlu ikinci ses — beşli aralık','Stop it at two-thirds: the most harmonious partner note — a fifth','']],
    'Kulağımız basit oranları “güzel” duyar; müzik saklı bir matematiktir','Our ears hear simple ratios as “beautiful” — music is hidden mathematics','#22301f','#050805',gap=7.5,d=46),
  photo('sema','Mevlevi Sema · Whirling ceremony','Sema: sağ eli göğe, sol eli yere açık dönen bir dua','Sema — a prayer that turns, right hand open to the sky, left to the earth','Mevlevi Sema Töreni 2008’de UNESCO İnsanlığın Somut Olmayan Kültürel Mirası listesine alındı','The Mevlevi Sema ceremony joined UNESCO’s Intangible Cultural Heritage list in 2008',fit='contain',d=44),
  q('Gelin tanış olalım,|işi kolay kılalım;|sevelim sevilelim,|dünya kimseye kalmaz','Let us get to know each other, make things easy, love and be loved — the world stays with no one','clay',d=56,lb='Yunus Emre',by='Yunus Emre (13.–14. yy)'),
  fact('1857','Fransız fizikçi Jules Lissajous, 1857’de bir diyapazona ayna yapıştırıp ışık huzmesiyle ses titreşimini görünür hâle getirdi','In 1857 French physicist Jules Lissajous glued a mirror to a tuning fork and made sound vibrations visible with a beam of light','Ses, görülebilen bir şekil de olabilir · Sound can be a shape you can see','#14202e','#04080e',d=32),
  rid('Elim yok ayağım yok; ama kapıyı çalarım, bulutları iterim. Kimim?','I have no hands or feet, yet I knock at doors and push the clouds. Who am I?','Rüzgâr!','The wind!',sec=16,c1='#0f3a40',c2='#061a1d'),
]),
S(18,19,'Hayvanların Zekâsı · Animal Minds',[
  photo('octopus','Ahtapot · Octopus','Bir ahtapot: üç kalbi, mavi kanı ve kollarında ayrı “mini beyinleri” var','An octopus — three hearts, blue blood and “mini-brains” in its arms','Kollarındaki sinir hücreleri, merkez beyin kadar çok; her kol bir ölçüde kendi başına karar verebilir','Its arms hold more neurons than its central brain — each arm can decide partly on its own',d=42),
  photo('dolphin','Karadeniz yunusu · Black Sea dolphin','Karadeniz’de yüzen bir yunus: Karadeniz’de üç yunus türü yaşıyor','A dolphin swimming in the Black Sea — three dolphin species live here','Yunuslar birbirini kendine özgü bir “imza ıslığı”yla çağırır; bu, isim gibi çalışır','Dolphins call each other with a personal “signature whistle” — it works like a name',d=42),
  steps('Hayvan Zekâsı · Animal Minds','Zekâyı ölçmenin üç yolu','Three ways to look at animal intelligence',
    [['Alet kullanmak: bazı ahtapotlar hindistan cevizi kabuklarını taşıyıp sığınak yapar','Using tools: some octopuses carry coconut shells to build shelters','🥥'],['Aynada kendini tanımak: yunuslar, filler, saksağanlar','Recognising yourself in a mirror: dolphins, elephants, magpies',''],['Kendine isim verip çağırmak: yunuslar, papağanlar','Calling each other by name: dolphins, parrots','']],
    'Zekâ tek bir ölçü değil; her tür kendi dünyasında akıllı','Intelligence is not one scale — every species is clever in its own world','#0f3a40','#061a1d',gap=7.5,d=46),
  photo('bowerbird','Saten çardak kuşu · Satin bowerbird','Mavi eşyalarla süslediği çardağın içindeki erkek çardak kuşu','A male satin bowerbird in the bower he decorated with blue objects','Dişiyi etkilemek için haftalarca çardak yapar, mavi nesneleri bulur ve renklerini düzenler','He spends weeks building his bower, finding blue things and arranging them to impress a mate',d=42),
  photo('kangal','Kangal köpeği · Kangal dog','Anadolu’nun sessiz bekçisi: bir Kangal köpeği','Anatolia’s quiet guardian — a Kangal dog','Namibya’da çiftçiler çitalları korumak için Kangal ve Anadolu çoban köpekleri kullanıyor','In Namibia, farmers use Anatolian shepherd dogs to guard livestock and protect cheetahs',d=40),
  rid('İki baba ve iki oğul balığa gitti. Üç balık tuttular ve her biri birer balık aldı. Nasıl?','Two fathers and two sons went fishing. They caught three fish and each took one. How?','Üç kişiydiler: dede, baba ve oğul!','There were only three: grandfather, father and son!',sec=18,c1='#22301f',c2='#050805'),
]),
S(19,20,'Renklerin Hikâyesi · The Story of Colours',[
  photo('indigo','Çivit mavisi · Indigo','Çivit (indigo) boyası bir kumaşı mavi yapan eski bir sır','Indigo — an ancient secret for turning cloth blue','Kot pantolonun mavisi hâlâ çivitten gelir; boya havayla temas edince yeşilden maviye döner','The blue of jeans still comes from indigo — in air the dye turns from green to blue',fit='contain',d=40),
  art('ultramarine','İnci Küpeli Kız — Johannes Vermeer, yaklaşık 1665','Girl with a Pearl Earring — Johannes Vermeer, c. 1665','Başlığın mavisi lacivert taşından yapılan ultramarin; çağının en pahalı boyalarından biri','The blue of the turban is ultramarine, made from lapis lazuli — one of the costliest paints of its day'),
  steps('Renklerin Hikâyesi · The Story of Colours','Mavi neden bu kadar pahalıydı?','Why was blue so expensive?',
    [['Mavi, doğada boya olarak nadir bulunur','Blue is rare as a pigment in nature','🎨'],['Lacivert taşı (lapis lazuli) Afganistan dağlarından geliyordu','Lapis lazuli came from the mountains of Afghanistan',''],['“Ultramarin” “denizin ötesinden” demek','“Ultramarine” means “from beyond the sea”',''],['Ressamlar onu yalnızca en önemli işlerinde kullanırdı','Painters saved it for the most important parts of their work','']],
    'Bir renk, bir yolculuğun adı olabilir','A colour can carry the name of a journey','#14202e','#04080e',gap=7,d=52),
  photo('madder','Kökboya · Madder','Kökboya bitkisi: kökünden Anadolu halılarının kırmızısı çıkar','The madder plant — the red of Anatolian carpets comes from its root','Türkçedeki “kökboya” adı tam olarak bu bitkiyi anlatır: boyası kökünden çıkan bitki','The Turkish name “kökboya” (“root dye”) describes it exactly',fit='contain',d=40),
  photo('murex','Murex deniz salyangozları · Murex shells','Murex kabukları: Antik çağda mor renk bu salyangozlardan elde edilirdi','Murex shells — in the ancient world, purple dye came from these snails','Bir gram boya için binlerce salyangoz gerekirdi; mor bu yüzden krallara ve imparatorlara aitti','Thousands of snails made a single gram of dye — which is why purple belonged to kings and emperors',d=42),
  fact('Mor','Antik Roma’da “Tyrus moru” giymek ayrıcalıktı; rengin adı, bugünkü Lübnan’daki Sur (Tyre) şehrinden gelir','In ancient Rome wearing “Tyrian purple” was a privilege — the colour is named after the city of Tyre in today’s Lebanon','Bir renk, tarihin bir parçası · A colour is a piece of history','#2a1f3a','#080510',d=30),
]),
S(20,21,'Taşta Geometri · Geometry in Stone',[
  photo('muqarnas','Mukarnas · Muqarnas','Mukarnas: yüzlerce küçük nişin üst üste dizildiği bal peteği tavan','Muqarnas — a honeycomb vault of hundreds of tiny niches','Bu süsleme, kare duvardan yuvarlak kubbeye geçişi gözü yormadan sağlıyor','This ornament lets a square wall flow into a round dome without a visible seam',fit='contain',d=42),
  photo('divrigi','Divriği Ulu Camii · Divriği Great Mosque','Divriği Ulu Camii ve Darüşşifası’nın taş kapısı','The stone portal of the Divriği Great Mosque and Hospital','1228–29’da yapıldı; kapılarındaki taş işçiliği UNESCO Dünya Mirası listesine 1985’te girdi','Built in 1228–29, its stone carving made the UNESCO World Heritage list in 1985',d=42),
  photo('selimiye','Selimiye Camii, Edirne · Edirne','Selimiye Camii’nin kubbe içi: sekiz fil ayağı üzerinde yükselen dev bir gökyüzü','Inside the Selimiye dome — a vast sky lifted on eight great piers','Mimar Sinan: “Şehzade’ye çıraklık, Süleymaniye’ye kalfalık, Selimiye’ye ustalık eserim”','Architect Sinan called Şehzade his apprenticeship, Süleymaniye his journeyman work, and Selimiye his masterpiece',d=44),
  photo('geometry','Girih deseni · Girih pattern','Girih: yıldızlar ve çokgenlerle dolu, tekrar etmeyen çini desenleri','Girih — tile patterns of stars and polygons that never exactly repeat','2007’de fizikçi Peter Lu, 1453 tarihli bir İran yapısındaki desenin “yarı kristal” matematiğiyle çalıştığını gösterdi','In 2007 physicist Peter Lu showed that a 1453 Iranian shrine used “quasi-crystal” mathematics',d=44),
  steps('Taşta Geometri · Geometry in Stone','Bir zemini boşluksuz kaplamak','Covering a floor without any gaps',
    [['Kare, eşkenar üçgen ve altıgen zemini boşluksuz kaplar','Squares, triangles and hexagons tile a floor without gaps','▦'],['Beşgen kaplamaz — ama başka şekillerle birlikte olursa?','Pentagons do not — but together with other shapes?',''],['Girih’te yalnızca beş tür parça var; hepsinin kenarı aynı uzunlukta','Girih uses only five tile types — all with the same edge length',''],['Parçalar bir araya gelince sonsuz çeşitlilikte desen kuruyor','Put together, they build endless varieties of patterns','']],
    'Mimar için geometri, taşa yazılmış bir şiir','For the architect, geometry is a poem written in stone','#2a2418','#080604',gap=7,d=56),
  q('Eline, beline, diline|sahip ol','Be master of your hands, your loins and your tongue','ink',d=44,lb='Hacı Bektaş-ı Veli',by='Hacı Bektaş-ı Veli (13. yy)'),
]),
S(21,22,'Göç Yolları: Kasım Gökyüzü · Migration Routes: The November Sky',[
  photo('crane','Turnalar · Common cranes','Turnalar güneye gidiyor: gökyüzünde yazılmış bir “V” mektubu','Cranes heading south — a “V” letter written across the sky','V biçiminde uçmak, arkadaki kuşların enerji tasarruf etmesini sağlar','Flying in a V helps the birds behind save energy',d=42),
  photo('stork','Leylekler · White storks','Yükselen sıcak hava akımlarında süzülen leylek sürüsü','A flock of storks soaring on rising warm air','Leylekler, kanat çırpmadan süzülebilmek için denizin üzerinden değil, kara köprüleri üzerinden göç eder','Storks avoid long sea crossings — they take land bridges where warm air lets them glide',d=42),
  photo('flamingo','Flamingolar · Flamingos','Uçarken uzun boyunlarıyla düz bir çizgi oluşturan flamingolar','Flamingos in flight, long necks stretched into a straight line','Flamingolar çoğu zaman geceleri uçar; yön bulmak için yıldızlardan ve manyetik alandan yararlanır','Flamingos often fly at night, steering by stars and the magnetic field',d=40),
  photo('tern','Kuzey kutbu sumrusu · Arctic tern','Arktik sumru: yılda yaklaşık 70.000 km uçan kutuptan kutba yolcu','The Arctic tern — flying roughly 70,000 km a year, pole to pole','Yaşamı boyunca Ay’a gidip dönmeye yakın bir mesafe kat edebilir','Over a lifetime it can fly a distance close to a round trip to the Moon',d=42),
  steps('Göç Yolları · Migration Routes','Kuşlar yollarını nasıl buluyor?','How do birds find their way?',
    [['Güneşi ve yıldızları pusula gibi kullanırlar','They use the sun and stars like a compass','☀'],['Dünya’nın manyetik alanını “hissederler”','They can sense the Earth’s magnetic field',''],['Kıyıları, nehirleri ve dağları hafızalarına yerleştirirler','They memorise coastlines, rivers and mountains',''],['Genç kuşlar yolu yaşlılardan öğrenir','Young birds learn the route from older ones','']],
    'Her sonbahar, Karadeniz’in doğu ucundaki dar geçitten yüz binlerce yırtıcı kuş güneye iner','Every autumn, hundreds of thousands of raptors funnel south through a narrow gap at the Black Sea’s eastern end','#14202e','#04080e',gap=7,d=56),
  rid('Kış gelince çıplak kalır, yaz gelince giyinir; kökü yerin altında, kolları göğe uzanır. Nedir?','It stands bare in winter and dressed in summer; its roots are underground, its arms reach to the sky. What is it?','Ağaç!','A tree!',sec=14,c1='#22301f',c2='#050805'),
]),
S(22,23,'İlk Kar: Sessiz Beyaz · First Snow: Quiet White (sakin · calm)',[
  photo('snowmount','Türkiye, uzaydan · Turkey from space','Uzaydan Türkiye: dağlara düşen ilk karın beyazı','Turkey from space — the first white of snow on the mountains','Uydu görüntüsü: kar, Türkiye’nin yüksek dağlarında ve yaylalarda en erken kasımda belirir','Satellite view — snow first appears on Turkey’s high mountains and plateaus around November',d=44),
  photo('snowflake','Kar tanesi · Snowflake','Bir kar tanesinin yakından görüntüsü: altı kollu, her biri başka','A snowflake close up — six arms, every one different','Kar taneleri her zaman altı yönlüdür; çünkü su molekülleri buzda altıgen kristal oluşturur','Snowflakes are always six-sided because water molecules build hexagonal crystals in ice',d=44),
  photo('frost','Kırağı · Frost','Yapraklarda kırağı: soğuk gecenin bıraktığı ince bir işlemeli kenar','Frost on leaves — a fine lace left by the cold night','Kırağı, havadaki su buharının doğrudan buza dönüşmesiyle oluşur','Frost forms when water vapour turns directly into ice',d=42),
  photo('snowvillage','Kar altında Shirakawa · Shirakawa','Karla kaplı bir köy: kış, sesleri örter','A snow-covered village — winter muffles every sound','Kar sesi emer; bu yüzden karlı bir gün çok sessiz hissedilir','Snow absorbs sound — which is why a snowy day feels so quiet',d=40),
  q('Sabreden derviş|muradına ermiş','He who is patient reaches his goal','night',d=44,lb='Atasözü · Turkish Proverb',by='Türk atasözü · Turkish proverb'),
  steps('Sakin Düşünce · Calm Thought','Kar yağarken dört sessiz an','Four quiet moments while snow falls',
    [['Pencerenin kenarına otur','Sit by the window','❄'],['Bir yudum sıcak bir şey iç','Take a sip of something warm',''],['Kar tanelerinin birbirinden ne kadar yavaş düştüğünü izle','Watch how slowly the flakes fall',''],['Sessizliği dinle','Listen to the silence','']],
    'Dünya yavaşlıyor; sen de yavaşlayabilirsin','The world slows down — so can you','#0e1624','#020306',gap=7.5,d=48,bg='stars'),
]),
S(23,26,'Gece Kandilleri · Night Lanterns (sakin · calm)',[
  g('hzlantern',d=80),
  photo('paperlantern','Kâğıt fenerler · Paper lanterns','Mavi saatte asılı yıldız biçimli fenerler','Star-shaped lanterns hanging at the blue hour','Gün batımından sonra gökyüzü kısa süre derin maviye döner; fotoğrafçılar buna “mavi saat” der','Shortly after sunset the sky turns a deep blue — photographers call it the “blue hour”',d=44),
  photo('candle','Mum alevi · Candle','Karanlıkta tek bir mum alevi','A single candle flame in the dark','Alevin parlayan kısmı, küçük kurum parçacıklarının ısıdan akkor hâle gelmesinden çıkar','The glow of a flame comes from tiny soot particles heated until they shine',fit='contain',d=40),
  photo('moonrise','Alacakaranlıkta hilal · Crescent moon','Alacakaranlıkta batan güneşin yanında ince bir hilal','A thin crescent beside the setting sun','Hilalde karanlık kısım da hafif görünür: buna “kül ışığı” denir, Dünya’dan yansıyan ışıktır','The dark part of a crescent glows faintly — “earthshine”, light reflected from our Earth',fit='contain',d=42),
  photo('milky','Samanyolu · The Milky Way','Samanyolu ve bir gözlemevi — şili’deki Paranal’dan ESO fotoğrafı','The Milky Way over an observatory — ESO photo from Paranal in Chile','Gözümüzün gördüğü her yıldız Samanyolu’nun içinde; galaksimizde yüz milyarlarca yıldız var','Every star we see belongs to the Milky Way — our galaxy holds hundreds of billions',d=44),
  q('Her gecenin|bir sabahı vardır','Every night has its morning','sea',d=46,lb='Atasözü · Turkish Proverb',by='Türk atasözü · Turkish proverb'),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: bugünün üç iyi anı','Before sleep: the three good moments of today',
    [['Bugün seni gülümseten bir şeyi hatırla','Remember one thing that made you smile today','☾'],['Bugün öğrendiğin küçük bir şeyi düşün','Think of one small thing you learned',''],['Yarın için sevdiğin tek bir şey seç','Choose one thing to look forward to tomorrow','']],
    'İyi geceler','Good night','#0e1624','#020306',gap=8,d=46,bg='stars'),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-17.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
