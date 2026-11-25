# Builds /workspace/tv-pages/days/2026-11-25.json (hourly sets 09:00-02:00). Wednesday.
# 09 morning Trabzon · 10 Brownian motion (NEW hzbrown) · 11 canyons · 12 glass · 13 Turner · 14 the Moon · 15 illusions (NEW hzehren)
# 16 Pólya's urn (NEW hzpolya) · 17-19 DJ Taş Act 1 Jazz House Lounge (NEW hzplak) · 19-22 Act 2 Sunset · 22-02 Act 3 Night (NEW hzbulut), stills only, no video.
# Photos m/h25-* (dl25.py/q25.json, dl25b.py/q25b.json), credits days/credits-2026-11-25.json.
import json,os
DATE='2026-11-25'; REV=84; NEXT='2026-11-26'
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-25.json')))
ART={'einstein1905':'Lucien Chavan','chartres':'Ludwig Schneider','footprint':'NASA (Buzz Aldrin)','tycho':'NASA / GSFC / Arizona State Univ. (LRO)',
 'bloodmoon':'Friedrich Böhringer','amasra':'Bertilvidet','bookbar':'bilinmeyen fotoğrafçı · unknown photographer (DPLA)','pollen':'Dartmouth Electron Microscope Facility',
 'positano':'Kent Wang','amalfi':'Nan Palmero','fireplace':'Warren LeMay','horseshoe':'Luca Galuzzi','rainsteam':'J. M. W. Turner','norham':'J. M. W. Turner','snowstorm':'J. M. W. Turner','fishermen':'J. M. W. Turner'}
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
    it=dict(k='hzphoto',d=d,f='m/h25-%s.jpg'%k,lb=lb,tr=tr,en=en,cr=cr(k))
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
    it=dict(k='hzwelcome',d=d,f='m/h25-%s.jpg'%k,lb=lb,lines=lines,tr=tr,en=en,cr=cr(k))
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
S(9,10,'Çarşamba Sabahı · Wednesday Morning',[
  photo('meydan','Atatürk Alanı · Trabzon','Trabzon’un kalbi: güne başlayan Atatürk Alanı','The heart of Trabzon: Atatürk Square starting its day','Trabzonlular burayı kısaca “Meydan” diye anar; şehirde buluşma sözü çoğu zaman burada verilir','Locals simply call it “Meydan” (the Square) — in Trabzon, “let’s meet” usually means here',d=40),
  q('Kalbin yolu bilir;|o yöne koş','Your heart knows the way — run in that direction','sea',d=40),
  photo('macka','Altındere Vadisi Milli Parkı · Maçka','Maçka’da Altındere Vadisi: ormanla kaplı yamaçlar','The Altındere Valley at Maçka: slopes covered in forest','Sümela Manastırı bu vadide, deniz seviyesinden yaklaşık 1.200 metre yükseklikte bir kayalığın yüzüne kurulu','Sümela Monastery stands in this valley, built into a cliff face about 1,200 m above sea level',d=40),
  fact('41°','Trabzon kuzey yarımkürede 41. enlemde: İstanbul, Roma ve New York ile hemen hemen aynı çizgide','Trabzon lies at about 41° north — almost on the same line as Istanbul, Rome and New York','Haritada bir çizgi · One line on the map','#13242c','#04080a',d=32),
  photo('akcaabat','Akçaabat · Trabzon','Akçaabat’ta Ak Camii ve yamaca yaslanan evler','The Ak Mosque in Akçaabat and the houses leaning on the hillside','Akçaabat, adını taşıyan köftesiyle Türkiye’nin dört bir yanında bilinir','Akçaabat is known all over Turkey for the meatballs that carry its name',d=38),
  rid('Ne kadar çok kurularsa,|o kadar ıslanır. Nedir?','The more it dries, the wetter it gets. What is it?','Havlu!','A towel!',sec=16),
]),
S(10,11,'Yaşayan Sanat: Görünmeyenin İzi — Brown Hareketi · Living Art: Traces of the Invisible — Brownian Motion',[
  g('hzbrown',d=96),
  photo('pollen','Polen taneleri · Pollen grains (elektron mikroskobu, renklendirilmiş · electron microscope, colourised)','Ayçiçeği, gündüzsefası, gülhatmi ve zambak polenleri, binlerce kez büyütülmüş','Pollen of sunflower, morning glory, hollyhock and lily, magnified thousands of times','Bir polen tanesi genelde 0,01–0,1 mm. Robert Brown’un 1827’de titrerken gördüğü tanecikler, polenin içinden çıkan çok daha küçük parçacıklardı','A pollen grain is usually 0.01–0.1 mm. The particles Robert Brown saw jiggling in 1827 were far smaller specks released from inside pollen',fit='contain',d=40),
  steps(CT,'Atomların var olduğunu nasıl kanıtladık?','How did we prove that atoms exist?',
    [['1827: Robert Brown, sudaki minik taneciklerin durmadan titrediğini gördü; önce canlı sandı','1827: Robert Brown saw tiny particles in water jiggling non-stop — at first he thought they were alive','🔬'],['Sonra taş tozuyla denedi: o da titriyordu. Demek ki canlılıkla ilgisi yoktu','Then he tried dust from rock — it jiggled too. So life had nothing to do with it',''],['1905: Einstein hesapladı: su moleküllerden oluşuyorsa, tanecik zamanın kareköküyle orantılı uzaklaşmalı','1905: Einstein calculated that if water is made of molecules, a particle should drift away in proportion to the square root of time',''],['1908: Jean Perrin mikroskopla ölçtü, tahmin tuttu; molekül sayısını bile hesapladı. 1926’da Nobel aldı','1908: Jean Perrin measured it under the microscope — the prediction held, and he even counted the molecules. He won the Nobel Prize in 1926','']],
    'Görünmeyeni, bıraktığı izden ölçebilirsin','You can measure the invisible from the traces it leaves','#16222c','#04080a',gap=8,d=58),
  photo('einstein1905','Bern · Patent Ofisi · Patent Office','Einstein, Bern’deki patent ofisinde, 1904 dolaylarında','Einstein at the patent office in Bern, around 1904','1905’te, hâlâ patent memuruyken dört çığır açan makale yayımladı; biri Brown hareketini açıklıyordu','In 1905, while still a patent clerk, he published four groundbreaking papers — one of them explained Brownian motion',fit='contain',d=38),
  fact('8 × 10²⁴','Bir su bardağında (250 ml) yaklaşık 8 × 10²⁴ su molekülü var: Dünya’daki bütün kumsallardaki kum tanelerinden kat kat fazla','A 250 ml glass holds about 8 × 10²⁴ water molecules — many times more than all the grains of sand on all the world’s beaches','Bir bardak su · One glass of water','#14202a','#04070a',d=32),
  rid('Suya bir damla mürekkep damlatırsan,|karıştırmasan da neden yayılır?','Drop ink into water — why does it spread even if you don’t stir?','Moleküller durmadan çarpışıyor: yine Brown hareketi. Sıcak suda daha hızlı yayılır','The molecules never stop colliding — Brownian motion again. It spreads faster in warm water',sec=20),
]),
S(11,12,'Nefes Kesen Yerler: Kanyonlar · Breathtaking Places: Canyons',[
  photo('antelope','Antelope Kanyonu, Arizona · Antelope Canyon','Dar kanyonun tepesindeki yarıktan inen bir ışık sütunu','A beam of light falling through the slot at the top of the narrow canyon','Kanyonu ani sel suları kumtaşını oyarak açtı; ışık sütunları en çok ilkbahar ve yaz öğlelerinde görülür','Flash floods carved this canyon out of sandstone — the light beams appear mostly around noon in spring and summer',d=42),
  photo('horseshoe','Horseshoe Bend, Arizona','Colorado Nehri burada kayayı at nalı biçiminde dolanıyor','Here the Colorado River loops around the rock in the shape of a horseshoe','Kayalığın kenarından nehre yaklaşık 300 metre','From the cliff edge down to the river is about 300 m',d=40),
  photo('saklikent','Saklıkent Kanyonu · Fethiye, Muğla','Saklıkent’in oyulmuş kayaları','The carved rock walls of Saklıkent','Yaklaşık 18 km uzunluğunda; yaz ortasında bile içinden akan su buz gibidir','About 18 km long — even in midsummer the water running through it is icy cold',d=40),
  photo('fishriver','Fish River Kanyonu, Namibya · Fish River Canyon','Namibya çölünde kıvrılan Fish River Kanyonu','The Fish River Canyon winding through the Namibian desert','Afrika’nın en büyük kanyonu: yaklaşık 160 km uzunluğunda, yer yer 550 metre derinliğinde','Africa’s largest canyon — about 160 km long and up to 550 m deep',d=40),
  photo('verdon','Verdon Vadisi, Fransa · Gorges du Verdon','Verdon’un kayalıklarında bir dağ keçisi; aşağıda derin vadi','A goat on the cliffs of the Verdon, the deep gorge below','Yer yer 700 metreye varan derinliğiyle Avrupa’nın en etkileyici kanyonlarından biri','Up to about 700 m deep in places — one of Europe’s most dramatic canyons',d=38),
  dict(k='hzchoose',d=40,q='Bir kanyonu nasıl yaşamak isterdin?',qe='How would you rather experience a canyon?',a=dict(f='m/h25-horseshoe.jpg',t='Tepeden bakmak',e='Looking down from the top',tag='Horseshoe Bend, Arizona'),b=dict(f='m/h25-saklikent.jpg',t='Dibinde, suyun içinde',e='Down at the bottom, in the water',tag='Saklıkent, Muğla'),p='Herkes birini seçsin, sonra nedenini söylesin',pe='Everyone picks one — then says why',cr='Fotoğraflar · Photos: %s · %s; %s · %s · Wikimedia Commons'%(artist('horseshoe'),lic('horseshoe'),artist('saklikent'),lic('saklikent'))),
]),
S(12,13,'Camın Şiiri · Poetry in Glass',[
  photo('chartres','Chartres Katedrali, Fransa · Chartres Cathedral','Güney gül penceresi: renkli camdan bir çiçek','The south rose window — a flower made of coloured glass','Chartres’ın vitraylarının çoğu 13. yüzyıldan kalma; derin maviler “Chartres mavisi” diye ünlüdür','Most of Chartres’ stained glass dates from the 13th century — its deep blues are famous as “Chartres blue”',fit='contain',d=42),
  photo('nasir','Nasırülmülk Camii, Şiraz · Nasir al-Mulk Mosque, Shiraz','Sabah güneşi renkli camlardan geçip halıların üstüne düşüyor','Morning sun pours through coloured glass onto the carpets','1888’de tamamlandı; renkler en güzel sabah erken saatte görünür. Pembe çinileri yüzünden “Pembe Cami” de denir','Completed in 1888, its colours are best early in the morning — its pink tiles earned it the name “Pink Mosque”',d=42),
  photo('sainte','Sainte-Chapelle, Paris','Üst şapelin duvarları neredeyse tamamen camdan','The walls of the upper chapel are almost entirely glass','1248’de kutsandı; 15 büyük pencerede 1.113 sahne anlatılır','Consecrated in 1248 — its 15 great windows tell 1,113 scenes',d=40),
  photo('murano','Venedik · Venice','Venedik’te ateşin başında çalışan bir cam ustası','A glassmaker working at the flame in Venice','1291’de Venedik, yangın tehlikesi yüzünden cam ocaklarını Murano adasına taşıdı; ada bugün hâlâ camıyla ünlü','In 1291 Venice moved its glass furnaces to the island of Murano because of the fire risk — the island is still famous for glass',d=38),
  photo('millefiori','Millefiori · cam ağırlık · glass paperweight','Bin çiçek: ince renkli cam çubuklardan dilimlerle yapılmış bir desen','A thousand flowers: a pattern made from slices of thin coloured glass canes','“Millefiori” İtalyanca “bin çiçek” demek. Renkli cam çubuk çekilip incelir, sonra dilimlenir: desen çubuğun boydan boya içindedir','“Millefiori” is Italian for “a thousand flowers”. A coloured glass rod is pulled thin, then sliced — the pattern runs all the way through it',fit='contain',d=38),
  photo('beykoz','Bursa Türk İslam Eserleri Müzesi · Museum of Turkish and Islamic Art, Bursa','Müzede burgu desenli cam eserler','Glass pieces with twisted patterns in the museum','Beyaz ve renkli şeritlerin burgulandığı bu desen, 19. yüzyılda İstanbul’da yapılan “çeşm-i bülbül” (bülbül gözü) camlarını hatırlatır','This twist of white and coloured threads recalls the “çeşm-i bülbül” (nightingale’s eye) glass made in 19th-century Istanbul',d=38),
  rid('Cam aslında neyden yapılır?','What is glass actually made from?','Kumdan! Çoğunlukla kuvars kumu, soda ve kireç; yaklaşık 1.500 °C’de eritilir','Sand! Mostly quartz sand with soda and lime, melted at about 1,500 °C',sec=18),
]),
S(13,14,'Büyük Ustalardan: Turner’ın Işığı ve Fırtınası · From the Great Masters: Turner’s Light & Storm',[
  art('rainsteam','J. M. W. Turner, 1844','Yağmur, Buhar ve Hız — Great Western Demiryolu','Rain, Steam and Speed — The Great Western Railway','Maidenhead köprüsünde bir tren sisin içinden geliyor. İyi bak: rayların üstünde trenin önünden kaçan küçük bir tavşan saklı','A train comes through the mist on the Maidenhead bridge. Look closely: a small hare is running ahead of it on the tracks'),
  art('fishermen','J. M. W. Turner, 1796','Denizde Balıkçılar','Fishermen at Sea','Turner’ın Kraliyet Akademisi’nde sergilenen ilk yağlı boya tablosu; o sırada 21 yaşındaydı','Turner’s first oil painting shown at the Royal Academy — he was 21'),
  q('Sanki renkli buharla boyuyor','He seems to paint with tinted steam','clay',d=36,lb='Ressamın Sözü · A Painter’s Words',by='John Constable, Turner için · on Turner'),
  art('snowstorm','J. M. W. Turner, 1842','Kar Fırtınası — Liman Ağzında Bir Buharlı Gemi','Snow Storm — Steam-Boat off a Harbour’s Mouth','Turner, fırtınayı görmek için kendini dört saat geminin direğine bağlattığını anlatırdı; hikâye bugün tartışmalı','Turner claimed he had himself tied to a ship’s mast for four hours to watch the storm — the story is debated today'),
  art('norham','J. M. W. Turner, yaklaşık · about 1845','Norham Kalesi, Gün Doğumu','Norham Castle, Sunrise','Turner bu kaleyi ilk kez 1797’de çizdi; neredeyse 50 yıl sonra onu yalnızca ışık ve renkle yeniden boyadı','Turner first drew this castle in 1797 — almost 50 years later he painted it again with nothing but light and colour'),
  fact('30.000','Turner öldüğünde ardında yaklaşık 300 yağlı boya ve 30.000 kadar çizim ve suluboya bıraktı; hepsini İngiliz ulusuna vasiyet etti','When Turner died he left about 300 oil paintings and some 30,000 sketches and watercolours — all bequeathed to the British nation','Turner Vasiyeti · The Turner Bequest','#2a2420','#0a0806',d=32),
]),
S(14,15,'Gökyüzünün Harikaları: Ay · Wonders of the Sky: The Moon',[
  photo('fullmoon','Dolunay · Full Moon','Dolunay: koyu lekeler, eski lav düzlükleri olan “denizler”','The full Moon — the dark patches are “seas” of ancient lava','Ay bize hep aynı yüzünü gösterir: kendi çevresinde bir tur dönmesi, Dünya’nın çevresinde bir tur dolaşması kadar sürer','The Moon always shows us the same face — it takes exactly as long to spin once as to circle the Earth once',fit='contain',d=40),
  photo('footprint','Apollo 11, 1969','Buzz Aldrin’in Ay tozundaki bot izi','Buzz Aldrin’s bootprint in the lunar dust','Ay’da rüzgâr ve yağmur olmadığı için bu izler milyonlarca yıl yerinde kalabilir','With no wind or rain on the Moon, these prints can last for millions of years',d=40),
  steps(SJ,'Ay ne kadar uzakta?','How far away is the Moon?',
    [['Ortalama 384.400 km','On average 384,400 km','🌕'],['Işık bu yolu yaklaşık 1,3 saniyede alır','Light covers it in about 1.3 seconds',''],['Saatte 100 km giden bir arabayla, hiç durmadan yaklaşık 160 gün','By car at 100 km/h, without stopping: about 160 days',''],['Ay her yıl yaklaşık 3,8 cm uzaklaşıyor; Apollo’nun bıraktığı aynalara lazer atılarak ölçülüyor','Each year the Moon drifts about 3.8 cm farther — measured by bouncing lasers off mirrors left by Apollo','']],
    'Kolunu uzat: serçe parmağının tırnağı dolunayı tamamen kapatır','Hold out your arm — your little fingernail covers the whole full Moon','#141c2a','#04060a',d=56),
  photo('tycho','Tycho Krateri · Tycho Crater (LRO)','Ay yörüngesindeki LRO’nun gözünden Tycho kraterinin merkez tepesi','The central peak of Tycho crater, seen by the Lunar Reconnaissance Orbiter','Tycho yaklaşık 108 milyon yaşında, Ay’ın genç büyük kraterlerinden; dolunayda ondan yayılan parlak ışınlar dürbünle görülür','Tycho is about 108 million years old, one of the Moon’s young large craters — at full Moon its bright rays can be seen with binoculars',fit='contain',d=38),
  photo('bloodmoon','Tam Ay tutulması · Total lunar eclipse, 28.09.2015','Bir Ay tutulmasının evreleri: Ay kızıla dönüyor','The stages of a lunar eclipse — the Moon turning red','Kızıl renk, Dünya atmosferinden süzülen ışık: o an Dünya’nın çevresindeki bütün gün doğumları ve batımları Ay’ı aydınlatır','The red is light filtered through Earth’s air — at that moment all the sunrises and sunsets around the Earth are lighting the Moon',fit='contain',d=40),
  rid('Ay ufka yakınken|neden daha büyük görünür?','Why does the Moon look bigger near the horizon?','Aslında büyümez! Fotoğrafta ölçünce boyu aynı: beyin ufuktaki şeyleri daha uzak sanıp büyütüyor','It doesn’t actually grow — measure it in a photo and it’s the same size. The brain thinks things on the horizon are farther away and enlarges them',sec=20),
]),
S(15,16,'Göz Oyunları: Beynin Eklediği Işık · Tricks of the Eye: Light the Brain Adds',[
  g('hzehren',d=50),
  g('hzcorn',d=44),
  fact('Kör nokta','Her gözde, görme sinirinin çıktığı yerde ışık algılayıcısı olmayan bir nokta var. Hiç fark etmeyiz: beyin o boşluğu çevreden tahminle doldurur','Each eye has a spot with no light receptors, where the optic nerve leaves. We never notice — the brain fills the gap with a guess from the surroundings','Gözün sırrı · A secret of the eye','#1c2228','#06080a',d=34),
  g('hzwhite',d=44),
  g('hzhermann',d=40),
  rid('İki gözünü de açıkken|kör noktanı neden görmezsin?','With both eyes open, why don’t you see your blind spot?','Çünkü iki gözün kör noktaları farklı yerlere düşer: biri ötekinin eksiğini kapatır','Because the two blind spots fall in different places — each eye covers for the other',sec=18),
]),
S(16,17,'Zekice Düşünce: Şansın Kartopu · Clever Thinking: The Snowball of Luck',[
  g('hzpolya',d=96),
  steps(CT,'Bir şarkı neden birden herkesin şarkısı olur?','Why does one song suddenly become everyone’s song?',
    [['2006: Columbia Üniversitesi’nde 14.000’i aşkın kişi, bilinmeyen 48 şarkıyı dinleyip indirebildi','2006: at Columbia University more than 14,000 people could listen to and download 48 unknown songs','🎧'],['Katılımcılar gizlice 8 ayrı “dünyaya” bölündü; her dünyada yalnızca o dünyanın indirme sayıları görünüyordu','Participants were secretly split into 8 separate “worlds” — each saw only its own download counts',''],['Sonuç: her dünyanın hit listesi farklı çıktı. Erken şanslı indirmeler kartopu gibi büyüdü','The result: every world ended up with a different hit list. Early lucky downloads snowballed',''],['İyi şarkılar nadiren dibe düştü, kötüler nadiren zirveye çıktı; aradaki her şeyi şans belirledi','Good songs rarely sank, bad ones rarely topped the chart — luck decided everything in between','']],
    'Kalite kapıyı açar; şans kimin önce gireceğine karar verir','Quality opens the door — luck decides who gets in first','#1a2228','#05080a',d=58),
  fact('Matta etkisi','Sosyolog Robert Merton 1968’de fark etti: aynı işi yapan iki bilim insanından ünlü olan daha çok övgü alıyor. Adını “kimde varsa ona daha çok verilecek” sözünden aldı','Sociologist Robert Merton noticed in 1968 that of two scientists doing the same work, the famous one gets more credit — named after the saying “to everyone who has, more will be given”','The Matthew effect','#1e2228','#06080a',d=36),
  rid('Bir zarı 6 kez atarsan,|en az bir kez 6 gelme olasılığı kaç?','Roll a die 6 times — what are the chances of at least one six?','Yaklaşık %66,5 — kesin değil! 1 − (5/6)⁶','About 66.5% — not certain! 1 − (5/6)⁶',hint='%100 değil · not 100%',sec=22),
  q('Şans, hazırlıklı zihinlerden yanadır','Chance favours only the prepared mind','ink',d=36,lb='Bilim Sözü · Science Saying',by='Louis Pasteur, 1854'),
]),
S(17,18,'DJ Taş · Caz House Lounge · Jazz House Lounge — Riviera gecesi · a Riviera night',[
  card('rooftop','DJ Taş · Sadece Sen — '+REAL+' · bir lounge bar · a lounge bar',[['DJ Taş',7.2],['Bu akşam · Tonight',3.4]],
   'Üç perdelik bir akşam: Caz House Lounge → Gün Batımı (19:00) → Gece (22:00). Müzik HomePod’da','An evening in three acts: Jazz House Lounge → Sunset (19:00) → Night (22:00). Music on the HomePod',d=32),
  g('hzplak',d=64),
  photo('bass','Kontrbas · Double bass','Bir kontrbasçı: caz house’un sıcak bas çizgisinin kökü','A double bass player — the root of jazz house’s warm basslines','Kontrbas, keman ailesinin en büyüğü; cazda çoğunlukla yayla değil parmakla çalınır (pizzicato)','The double bass is the largest of the violin family — in jazz it is mostly plucked with the fingers (pizzicato), not bowed',d=40,pos='50% 35%',act=A1),
  photo('rhodes','Fender Rhodes','Caz house’un yumuşak akorlarının sesi: bir Rhodes elektrikli piyanosu','The sound of jazz house’s soft chords: a Rhodes electric piano','Rhodes’da tel yok: çekiçler ince metal çubuklara vurur, titreşimi manyetik bir mikrofon toplar','A Rhodes has no strings — hammers strike thin metal tines and a magnetic pickup catches the vibration',d=40,act=A1),
  g('hzlissa',d=56),
  photo('eze','Èze, Fransız Rivierası · French Riviera','Kayalığın tepesindeki Èze köyü ve uzakta Cap Ferrat','The village of Èze on its rock, Cap Ferrat beyond','Èze, denizden yaklaşık 430 metre yükseklikte bir kayanın üstüne kurulmuş “kartal yuvası” köylerinden','Èze is one of the “eagle’s nest” villages, perched on a rock about 430 m above the sea',d=40,act=A1),
  fact('118–125','Deep ve caz house çoğunlukla dakikada 118–125 vuruş arasında çalınır: dans etmeye yeter, sohbeti bölmez','Deep and jazz house usually run at 118–125 beats per minute — enough to dance to, never loud enough to stop a conversation','Bu akşamın temposu · Tonight’s tempo','#24181a','#080506',d=30),
],pre='dj'),
S(18,19,'Caz House Lounge · Jazz House Lounge — Villa Fikri: Akşam Köşeleri · Villa Idea: Evening Corners',[
  photo('villefranche','Villefranche-sur-Mer, Riviera','Riviera’da sakin bir koy ve demirli yelkenliler','A quiet Riviera bay with sailboats at anchor',d=38,act=A1),
  villa('speakeasy','Mind Palace Bar','Alt katta küçük bir speakeasy köşesi: koyu ahşap, yeşil kadife tabureler, arkadan ışıklı raflar','A small speakeasy corner downstairs: dark wood, green velvet stools, back-lit shelves','“Speakeasy” adı ABD’deki içki yasağı yıllarından (1920–33) gelir: içeride sesini alçaltarak, “speak easy” konuşurdun','“Speakeasy” comes from the US Prohibition years (1920–33) — inside you kept your voice down and “spoke easy”',act=A1),
  q('Kalbinde tutuşmaya hazır|bir mum var','There is a candle in your heart, ready to be kindled','clay',d=40),
  villa('bookbar','Whid-Isle Inn, Washington, 1925 dolayları · about 1925','Şöminenin önünde koltuklar, raflarda kitaplar: misafirlerin akşam toplandığı bir oda','Armchairs by the fire, books on the shelves — a room where guests gather in the evening','Fikir: taş duvarın önüne kitap rafı ve iki deri koltuk — Sadece Sen misafirleri için akşamları bir “kütüphane bar”','Idea: a bookshelf and two leather armchairs against the stone wall — a “library bar” for Sadece Sen guests in the evening',act=A1),
  g('hzflow',d=56),
  fact('Negroni','Söylenceye göre 1919’da Floransa’da Kont Camillo Negroni, Americano’sundaki soda yerine cin istedi; doğan kokteyle onun adı verildi','Legend has it that in 1919 in Florence, Count Camillo Negroni asked for gin instead of soda in his Americano — the new cocktail took his name','Bir kokteylin hikâyesi · The story of a cocktail','#2a1416','#0a0506',d=30),
],pre='dj'),
S(19,20,'Gün Batımı · Sunset — Karadeniz kıyıları · Black Sea shores',[
  card('amasra','DJ Taş · 2. Perde · Act 2 — '+REAL+' · Amasra, Bartın',[['Gün Batımı',6.4],['Sunset',3.6]],
   'Liste değişti: şimdi “Sadece Sen Sunset” çalıyor','The playlist has changed — now playing “Sadece Sen Sunset”',d=30),
  photo('giresunisland','Giresun Adası · Giresun Island','Akşamüstü Karadeniz’de Giresun Adası','Giresun Island on the Black Sea in the late afternoon','Doğu Karadeniz kıyısımızdaki tek ada; mitolojide Argonotların uğradığı Aretias adası olduğu düşünülür','The only island off Turkey’s eastern Black Sea coast — thought to be Aretias, where the Argonauts landed in myth',d=40,act=A2),
  g('hzmoire',d=56),
  photo('sile','Şile Feneri · Şile Lighthouse, İstanbul','Şile’nin siyah-beyaz çizgili deniz feneri','Şile’s black-and-white striped lighthouse','1859’da yapıldı; bugün de Karadeniz’den Boğaz’a gelen gemilere yol gösteriyor','Built in 1859, it still guides ships coming from the Black Sea towards the Bosphorus',d=38,act=A2),
  photo('kefken','Kefken Adası · Kefken Island, Kocaeli','Kefken Adası, yukarıdan: turkuaz suyla çevrili küçük bir ada','Kefken Island from above — a small island ringed by turquoise water',d=38,act=A2),
  photo('amasra','Amasra, Bartın','Amasra’da güneş kayalıkların arasından denize iniyor','The sun sinking into the sea between the rocks at Amasra','Amasra’nın iki limanını Bizans ve Ceneviz dönemlerinden kalma kale surları çevreler','Amasra’s two harbours are framed by castle walls from the Byzantine and Genoese eras',d=40,act=A2),
],pre='dj'),
S(20,21,'Gün Batımı · Sunset — Ege ve Adriyatik · Aegean & Adriatic',[
  photo('ayvalik','Şeytan Sofrası, Ayvalık','Şeytan Sofrası’ndan adalara inen akşam','Evening settling over the islands from Şeytan Sofrası','Ayvalık’ın önünde 20’den fazla ada var; en büyüğü Cunda','More than 20 islands lie off Ayvalık — the largest is Cunda',d=42,act=A2),
  g('hzfourier',d=56),
  photo('bozcaada','Bozcaada','Bozcaada’da gün batımı','Sunset on Bozcaada','Ada bağlarıyla ve rüzgârıyla bilinir; Polente Feneri’nde güneşi batırmak adanın akşam ritüelidir','The island is known for its vineyards and wind — watching the sun go down at Polente Lighthouse is its evening ritual',d=40,act=A2),
  photo('datca','Datça','Datça’da koylara inen güneş','The sun going down over the coves of Datça','Datça Yarımadası, Ege ile Akdeniz’in buluştuğu yerde uzanır','The Datça peninsula stretches out where the Aegean meets the Mediterranean',d=40,act=A2),
  fact('Mavi saat','Güneş ufkun birkaç derece altına inince gökyüzü kısa bir süre derin maviye döner; fotoğrafçıların sevdiği bu ana “mavi saat” denir','When the sun sinks a few degrees below the horizon, the sky turns deep blue for a short while — photographers call it the “blue hour”','Blue hour · Akşamın rengi · The colour of evening','#14203a','#04060c',d=30),
  photo('kotor','Kotor Körfezi, Karadağ · Bay of Kotor, Montenegro','Kotor Körfezi’nde dağların ardında son ışık','The last light behind the mountains of the Bay of Kotor','Çoğu kişi fiyort sanır ama aslında deniz basmış eski bir nehir kanyonudur','Many people take it for a fjord, but it is really an old river canyon flooded by the sea',d=40,act=A2),
],pre='dj'),
S(21,22,'Gün Batımı · Sunset — Anadolu’da son ışık · last light in Anatolia',[
  photo('cappadocia','Kapadokya · Cappadocia','Kapadokya’da batan güneşe karşı balonlar ve bir at','Balloons and a horse against the setting sun in Cappadocia','Peri bacaları, Erciyes, Hasandağı ve Göllüdağ’ın püskürttüğü küllerin sertleşip aşınmasıyla oluştu','The fairy chimneys formed as ash from Erciyes, Hasandağı and Göllüdağ hardened and wore away',d=42,act=A2),
  g('hzphyllo',d=56),
  photo('pamukkale','Pamukkale, Denizli','Pamukkale travertenlerinde pastel bir akşam','A pastel evening on the travertine terraces of Pamukkale','Beyaz teraslar, yaklaşık 35 °C’lik kaynak suyundaki kirecin çökelmesiyle oluşur','The white terraces form as lime settles out of spring water at about 35 °C',d=40,act=A2),
  q('Nerede yıkıntı varsa,|orada bir hazine umudu vardır','Where there is ruin, there is hope for a treasure','clay',d=40),
  photo('nemrutdagi','Nemrut Dağı, Adıyaman · Mount Nemrut','Nemrut Dağı’nda karların içinde Apollon’un taş başı','The stone head of Apollo in the snow on Mount Nemrut','Kommagene Kralı I. Antiochos’un MÖ 1. yüzyılda 2.134 metrede yaptırdığı tümülüs; buradan gün batımı efsanevidir','The tomb-mound King Antiochus I of Commagene built at 2,134 m in the 1st century BC — sunsets here are legendary',d=40,act=A2),
],pre='dj'),
S(22,23,'Gece · Night — Akdeniz kıyısında ışıklar · lights on the Mediterranean (sakin · calm)',[
  card('amalfi','DJ Taş · 3. Perde · Act 3 — '+REAL+' · Amalfi kıyısı · Amalfi Coast',[['Gece',6.6],['Night',3.6]],
   'Şimdi “Sadece Sen Night” çalıyor: daha yumuşak, daha sakin','Now playing “Sadece Sen Night” — softer and calmer',d=30),
  photo('positano','Positano, İtalya · Italy','Positano’da akşam: kayalıklara yaslanan ışıklar ve sakin deniz','Evening at Positano: lights against the cliffs and a calm sea',d=44,act=A3,quiet=1),
  photo('dubrovnik','Dubrovnik, Hırvatistan · Croatia','Dubrovnik eski şehrinde gece: sokak lambası altında taş merdivenler','Night in Dubrovnik’s old town — stone steps under a street lamp',d=44,act=A3,quiet=1),
  g('hzlantern',d=70),
  photo('venicenight','Venedik · Venice','Akşam San Marco’da: kemerlerin ışıkları yanıyor','Evening at San Marco — the lights in the arcades coming on',d=44,act=A3,quiet=1),
  photo('amalfi','Amalfi kıyısı · Amalfi Coast','Amalfi kıyısında yamaçlara serpilmiş ışıklar','Lights scattered across the slopes of the Amalfi Coast',d=44,act=A3,quiet=1),
],pre='dj'),
S(23,26,'Gece · Night — ay, bulut ve göl · moon, clouds and lake (sakin · calm)',[
  g('hzbulut',d=110),
  photo('moonclouds','Ay ve bulut · Moon and clouds','İnce bir bulut tülünün ardında ay','The moon behind a thin veil of cloud',d=46,act=A3,quiet=1),
  photo('bellagio','Bellagio, Como Gölü · Lake Como','Gece Como Gölü kıyısında Bellagio','Bellagio by Lake Como at night',d=46,act=A3,quiet=1),
  g('hzfener',d=80),
  photo('hallstatt','Hallstatt, Avusturya · Austria','Hallstatt’ın ışıkları göle düşüyor','The lights of Hallstatt falling on the lake',d=46,act=A3,quiet=1),
  photo('fullmoon','Dolunay · Full Moon','İyi geceler · Good night','Good night',d=46,fit='contain',act=A3,quiet=1),
],pre='dj'),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-25.py. 17:00–02:00 = DJ Taş evening (Jazz House Lounge → Sunset 19:00 → Night 22:00, synced with the HomePod playlists; stills only at night, no video). Content log: used-content.md',sets=sets),open(os.path.join(HERE,'%s.json'%DATE),'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'][:60])
