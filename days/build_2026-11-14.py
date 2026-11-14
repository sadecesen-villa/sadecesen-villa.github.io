# Builds /workspace/tv-pages/days/2026-11-14.json (hourly sets 09:00-02:00). Pattern from build_2026-11-13.py.
import json,os
DATE='2026-11-14'; REV=63; NEXT='2026-11-15'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-14.json')))
FIX={'Ed Landing &amp; Markes':'Ed Landing & Markes E. Johnson','ESA/Rosetta/NAVCAM, CC BY-SA IGO 3.0':'ESA / Rosetta / NAVCAM','Benh LIEU SONG from Torcy':'Benh LIEU SONG','Raita Futo from Tokyo':'Raita Futo','E. Kolmhofer, H. Raab; Johannes':'E. Kolmhofer, H. Raab (Johannes-Kepler-Sternwarte)','Greg Lundeen':'Greg Lundeen / NWS','Image: National Aeronautics and Space Ad':'NASA / ESA / CSA / STScI','Photograph by Mike Peel':'Mike Peel','Photograph by Greg O':'Greg O’Beirne','Richard Leeming from London':'Richard Leeming','NASA/Apollo 17 crew; taken by either Harrison Schmitt or Ron Evans':'NASA / Apollo 17','Image by NASA, modifications by Seddon':'NASA','Surmene at en.wikipedia':'Surmene (en.wikipedia)','Garst, Warren, 1922-2016, photographer':'Warren Garst','https://www.flickr.com/photos/clpmag/':'clpmag (Flickr)','Original: Tambako The Jaguar':'Tambako The Jaguar / Niabot','Al_Khazneh_Petra.jpg: Graham Racher':'Graham Racher / MrPanyGoff','Unknown authorUnknown author':'bilinmeyen fotoğrafçı · unknown photographer','Dartmouth Electron Microscope Facility':'Dartmouth Electron Microscope Facility','shankar s. from Dubai':'shankar s.','Rosa Cabecinhas and Alcino Cunha':'Rosa Cabecinhas & Alcino Cunha'}
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
    it=dict(k='hzphoto',d=d,f='m/h14-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
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
WHERE='Neresi Burası? · Where Is This? — Gerçek Fotoğraf · Real Photo'
FIX2={'User:Sveter':'Petr Šmerkl','This Photo was taken by Timothy A. Gonsalves':'Timothy A. Gonsalves','Jeff Schmaltz, MODIS Land Rapid Response Team, NASA GSFC':'Jeff Schmaltz, MODIS / NASA GSFC','Fir0002 at English Wikipedia':'Fir0002','Eric Welch eric_welch':'Eric Welch'}
def art2(k):
    a=artist(k)
    for f,t in FIX2.items():
        if a.startswith(f[:25]): return t
    return a.split('. ')[0]
def crs(k): return '%s · %s'%(art2(k),lic(k))
def welcome(k,where,lines,names,tr,en,d=45):
    return dict(k='hzwelcome',d=d,f='m/h14-%s.jpg'%k,lb='Hoş Geldiniz · Welcome — '+REAL+' · '+where,lines=lines,names=names,tr=tr,en=en,cr='Foto · Photo: '+crs(k)+' · Wikimedia Commons') if names else dict(k='hzwelcome',d=d,f='m/h14-%s.jpg'%k,lb='Hoş Geldiniz · Welcome — '+REAL+' · '+where,lines=lines,tr=tr,en=en,cr='Foto · Photo: '+crs(k)+' · Wikimedia Commons')
def guess(k,where,qq,qe,a,ae,hint=None,sec=20,d=36,lb=None,tag=None,pos=None):
    it=dict(k='hzguess',d=d,f='m/h14-%s.jpg'%k,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr='Foto · Photo: '+crs(k)+' · Wikimedia Commons')
    it['lb']=lb or ('Birlikte Tahmin · Guess Together — '+(tag or REAL)+(' · '+where if where else ''))
    if hint: it['hint']=hint
    if pos: it['pos']=pos
    return it
def ask(k,where,qq,qe,d=34):
    return dict(k='hzguess',d=d,f='m/h14-%s.jpg'%k,lb='Sohbet Sorusu · Conversation Starter — '+REAL+' · '+where,q=qq,qe=qe,p='Sırayla anlatın! · Take turns!',cr='Foto · Photo: '+crs(k)+' · Wikimedia Commons')
def choose(qq,qe,A,B,p,pe,d=40):
    def side(x): return dict(f='m/h14-%s.jpg'%x[0],t=x[1],e=x[2],tag=REAL)
    return dict(k='hzchoose',d=d,q=qq,qe=qe,a=side(A),b=side(B),p=p,pe=pe,cr='Fotoğraflar · Photos: A — %s · B — %s · Wikimedia Commons'%(crs(A[0]),crs(B[0])))
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
sets=[
S(9,10,'Karadeniz’in Taş Hafızası · Stone Memory of the Black Sea',[
  photo('ayasofya','Trabzon','Trabzon Ayasofya’nın 13. yüzyıldan kalma freskleri','The 13th-century frescoes of Hagia Sophia in Trabzon','1250–1260 yıllarında Trabzon İmparatorluğu döneminde yapıldı; freskleri geç Bizans sanatının en güzel örneklerinden sayılır','Built in 1250–1260 in the days of the Empire of Trebizond — its frescoes are counted among the finest of late Byzantine art',d=40),
  q('Sen denizde bir damla değilsin;|bir damlada okyanusun tamamısın','You are not a drop in the ocean — you are the entire ocean in a drop','sea',d=46),
  photo('sumela','Maçka, Trabzon','Sümela Manastırı — Altındere Vadisi’nde sarp bir kayalığa yaslanmış','Sümela Monastery — clinging to a sheer cliff above the Altındere Valley','Rivayete göre 4. yüzyılda kuruldu; yaklaşık 1.200 metre yükseklikte, ormanın içinden bakınca kayaya oyulmuş gibi görünür','Tradition says it was founded in the 4th century — at about 1,200 m, it looks carved into the rock when seen from the forest',d=40),
  fact('%90','Karadeniz’in sularının yaklaşık %90’ında hiç oksijen yok — dünyanın en büyük oksijensiz su kütlesi','About 90% of the Black Sea’s water holds no oxygen at all — the largest oxygen-free body of water on Earth','Bu yüzden derinlerdeki batıklar çürümez: 2018’de 2.400 yıllık bir Yunan gemisi neredeyse sağlam bulundu · So deep wrecks don’t rot — in 2018 a 2,400-year-old Greek ship was found almost intact','#12303a','#03080b',d=32),
  photo('kackar','Rize','Kaçkar Dağları — 3.937 metrelik zirvesiyle Doğu Karadeniz’in çatısı','The Kaçkar Mountains — roof of the eastern Black Sea, with a 3,937 m summit','Buzul gölleri ve yaz yaylalarıyla ünlü; denizden 50 km içeride 3.900 metreyi aşan dağlar, bulutları yakalayıp kıyıyı yeşil tutar','Famous for glacial lakes and summer pastures — peaks above 3,900 m just 50 km from the sea catch the clouds and keep the coast green',d=40),
  rid('Suda doğar, suda ölür;<br>sofraya tat verir.<br>Nedir?','It is born in water and dies in water, and gives the table its taste. What is it?','Tuz!','Salt.',sec=16,c1='#1c2a30',c2='#040708'),
]),
S(10,11,'Kelebek Etkisi · The Butterfly Effect',[
  g('hzlorenz',d=78),
  steps('Gerçek Hikâye · True Story','1961: Bir meteorolog kahve molası verir ve kaos keşfedilir…','1961: a meteorologist takes a coffee break — and chaos is discovered…',
    [['Edward Lorenz bilgisayarında basit bir hava modeli çalıştırıyor','Edward Lorenz runs a simple weather model on his computer',''],['Bir hesabı yeniden başlatmak için sayıyı kısaltarak giriyor: 0,506127 yerine 0,506','To rerun a forecast he types a shortened number: 0.506 instead of 0.506127',''],['Kahvesini içip dönüyor','He goes for a coffee and comes back','☕'],['Birkaç “hafta” sonra tahmin bambaşka: güneş yerine fırtına','A few simulated “weeks” later the forecast is completely different — storm instead of sun','≠'],['Binde birlik fark, bütün havayı değiştirmişti','A difference of one part in a thousand had changed all the weather','🦋']],
    'Lorenz’in 1972 konuşmasının adı: “Brezilya’da bir kelebeğin kanat çırpışı Teksas’ta bir kasırga başlatabilir mi?”','The title of Lorenz’s 1972 talk: “Does the flap of a butterfly’s wings in Brazil set off a tornado in Texas?”','#1a2230','#040508',gap=6.5,d=58),
  photo('supercell','New Mexico, ABD · USA','Dönen dev bir fırtına bulutu: süper hücre','A giant rotating storm cloud: a supercell','Tepesi 12–15 km’ye, yolcu uçaklarının üstüne kadar yükselebilir; içindeki hava sütunu yavaşça döner','Its top can tower 12–15 km high — above airliners — while the column of air inside slowly turns',d=40),
  fact('+1 gün','Hava tahminleri her on yılda yaklaşık bir gün daha ileriyi görüyor','Weather forecasts see about one day further ahead every decade','Bugünün 5 günlük tahmini, 1980’lerin 3 günlük tahmini kadar isabetli · A 5-day forecast today is as good as a 3-day forecast in the 1980s','#18243a','#03050a',d=30),
  rid('Ne kadar çok alırsan,<br>arkanda o kadar çok bırakırsın.<br>Nedir?','The more you take, the more you leave behind. What are they?','Adımlar!','Footsteps.',sec=18,c1='#22262c',c2='#050607'),
]),
S(11,12,'Yaşam Oyunu · The Game of Life',[
  g('hzlife',d=75),
  steps('Akıllı Açıklama · Clever Explainer','Beş karelik bir “planör” nasıl yürür? Hiçbir kare kıpırdamadan…','How does a five-square “glider” walk — when no square ever moves?',
    [['Kareler yer değiştirmez; yalnızca doğar ya da ölür','Squares never move — they are only born or die',''],['Planör her adımda biçim değiştirir: dört farklı şekil','The glider changes shape at every step — four different forms',''],['4 adım sonra ilk şekline döner…','After 4 steps it is back to its first shape…',''],['…ama bir kare çapraz kaymış olarak','…but shifted one square diagonally','↘'],['Ortada hareket eden bir şey yok — ama desen yürüyor','Nothing is moving — yet the pattern walks','✓']],
    'Dalgalar da böyledir: denizde su yerinde kalır, ilerleyen şey biçimdir','Waves are like this too — the water stays put; it is the shape that travels','#16282a','#030707',gap=6,d=54),
  photo('conus','Konik salyangoz · Cone snail, Conus textile','Konik salyangoz kabuğu — üçgen desenleri bir bilgisayar programı gibi büyür','A cone snail shell — its triangle patterns grow like a computer program','Kabuğun kenarındaki hücreler komşularına bakarak boya bırakır; ortaya basit kurallı bir “hücresel otomat” deseni çıkar (bu salyangoz zehirlidir, dokunulmaz!)','Cells along the shell’s edge lay down pigment by checking their neighbours — a simple-rule “cellular automaton” pattern (this snail is venomous — never touch!)',fit='contain'),
  fact('1970','Yaşam Oyunu 1970’te bir dergi köşesinde tanıtıldı; bilgisayar azdı, insanlar kareli kâğıt ve go taşlarıyla oynadı','The Game of Life was introduced in a magazine column in 1970 — few people had computers, so they played it on graph paper and Go boards','Martin Gardner, Scientific American · Conway kendisi de go tahtası kullandı · Conway himself used a Go board','#1e2430','#040508',d=32),
  rid('1 · 11 · 21 · 1211 · 111221<br>Sıradaki ne?','1, 11, 21, 1211, 111221 — what comes next?','312211 — her sayı bir öncekini sesli okur: “üç 1, iki 2, bir 1”','312211 — each line reads the one before aloud: “three 1s, two 2s, one 1” (Conway studied this too)',hint='İpucu: sayıları yüksek sesle oku · Hint: read them aloud',sec=26,d=40,c1='#24282c',c2='#050607'),
]),
S(12,13,'Ağaçların Mimarisi · The Architecture of Trees',[
  g('hztree',d=60),
  photo('crown','Taç utangaçlığı · Crown shyness','Taç utangaçlığı: komşu ağaçların tepeleri birbirine değmez','Crown shyness: the crowns of neighbouring trees don’t touch','Nedeni tam bilinmiyor: rüzgârda sürtünmemek, böceklerin yayılmasını önlemek ya da ışığı paylaşmak olabilir','Nobody knows exactly why — perhaps to avoid rubbing in the wind, to stop insects spreading, or to share the light'),
  photo('dragontree','Sokotra, Yemen','Ejder kanı ağacı — ters dönmüş bir şemsiye gibi','The dragon’s blood tree — like an umbrella turned inside out','Şemsiye biçimi sisi ve gölgeyi yakalar; kabuğu çizilince kırmızı reçine sızar, adı buradan gelir','Its umbrella shape catches mist and makes shade — cut the bark and red resin seeps out, hence the name',fit='contain'),
  photo('baobab','Madagaskar · Madagascar','Baobab ağacı — gövdesinde binlerce litre su saklar','A baobab — storing thousands of litres of water in its trunk','Bazı baobablar 800 yıldan yaşlıdır; kurak mevsimde yapraklarını döküp suyunu korur','Some baobabs are over 800 years old — in the dry season they drop their leaves to save water',fit='contain'),
  photo('angeloak','Johns Island, ABD · USA','Melek Meşesi — dalları yere kadar uzanan yaşlı bir meşe','The Angel Oak — an ancient oak whose limbs reach down to the ground','300–400 yaşında olduğu tahmin ediliyor; gölgesi yaklaşık 1.600 m²’lik bir alanı kaplar','Thought to be 300–400 years old — its shade covers about 1,600 m²',fit='contain'),
  fact('da Vinci','Leonardo da Vinci fark etti: ağaç dallandığında dalların kalınlıkları toplamı gövdeyle aşağı yukarı aynı kalır','Leonardo da Vinci noticed that when a tree branches, the branches together are about as thick as the trunk','“Leonardo kuralı” — bugün rüzgâra dayanıklılıkla açıklanıyor · “Leonardo’s rule” — now explained by resistance to wind','#1e2a22','#040705',d=32),
]),
S(13,14,'Katlamanın Sırları · Secrets of Folding',[
  g('hzdragon',d=66),
  steps('Ölçek Yolculuğu · Scale Journey','0,1 mm kalınlığında bir kâğıdı 42 kez katlayabilseydin…','If you could fold a 0.1 mm sheet of paper 42 times…',
    [['10 katta: bir kibrit kutusu kadar, yaklaşık 10 cm','10 folds: about 10 cm — a matchbox','10 cm'],['20 katta: 30 katlı bir gökdelen boyu','20 folds: as tall as a 30-storey tower','105 m'],['30 katta: uzayın kıyısını geçer','30 folds: past the edge of space','107 km'],['42 katta: Ay’a ulaşıp geçer','42 folds: all the way to the Moon — and beyond','440.000 km']],
    'Gerçekte rekor 12 kat — 2002’de bir lise öğrencisi Britney Gallivan, 1 km’yi aşan tek bir kâğıt şeritle yaptı','The real record is 12 folds — set in 2002 by high-school student Britney Gallivan with a single strip over 1 km long','#1e2430','#040508',gap=6.5,d=54),
  photo('origami','Origami','Kâğıt turnalar — tek bir kare kâğıttan, kesmeden ve yapıştırmadan','Paper cranes — from a single square sheet, no cutting, no glue','Japon geleneğine göre bin turna katlayanın bir dileği gerçekleşir: “senbazuru”','Japanese tradition says that whoever folds a thousand cranes is granted a wish — “senbazuru”'),
  q('Başkalarının hikâyeleriyle yetinme;|kendi efsaneni aç','Don’t be satisfied with stories of how things have gone with others — unfold your own myth','ink'),
  photo('miura','Miura katlaması · Miura fold','Miura katlaması — tek bir çekişle açılıp kapanan bir desen','The Miura fold — a pattern that opens and closes with a single pull','Japon astrofizikçi Kōryō Miura buldu; 1995’te bir uydunun güneş panelleri bu desenle katlanıp uzayda açıldı','Invented by Japanese astrophysicist Kōryō Miura — in 1995 a satellite’s solar panels were folded this way and opened in space',fit='contain'),
  photo('jwst','NASA','James Webb Uzay Teleskobu’nun 18 altıgen ayna parçası, testte','The 18 hexagonal mirror segments of the James Webb Space Telescope, under test','6,5 metrelik ayna roketin içine sığmadı: teleskop origami gibi katlandı ve uzayda kendi kendine açıldı (2022)','The 6.5 m mirror didn’t fit inside the rocket — so the telescope was folded like origami and unfolded itself in space (2022)',d=40),
]),
S(14,15,'Villa Fikirleri: Işık ve Gölge · Villa Ideas: Light & Shadow',[
  villa('louvreabu','Louvre Abu Dabi · Abu Dhabi','Kubbeden süzülen “ışık yağmuru”','A “rain of light” falling through the dome','Jean Nouvel’in kubbesi 8 katmanda 7.850 yıldızdan oluşur; güneş ışığı içeri hurma yapraklarının arasından süzülür gibi damlar','Jean Nouvel’s dome is made of 7,850 stars in 8 layers — sunlight drips through as if through palm fronds'),
  q('Yara,|ışığın içine girdiği yerdir','The wound is the place where the Light enters you','clay'),
  villa('nasir','Nasırülmülk Camii, Şiraz · Nasir al-Mulk, Shiraz','Sabah güneşi renkli camlardan halılara düşüyor','Morning sun falls through stained glass onto the carpets','Doğuya bakan birkaç renkli cam, sabah kahvaltısında taş zemine ve yastıklara renk serpebilir','A few coloured panes facing east could scatter colour across a stone floor and cushions at breakfast'),
  villa('alcove','Japonya · Japan','Kâğıt sürgü kapılar (şoji) ışığı yumuşatıyor','Paper sliding screens (shoji) soften the light','Keten ya da pirinç kâğıdı perdeler sert güneşi süt beyazı bir ışığa çevirir — bir yatak odası ya da okuma köşesi için huzurlu bir fikir','Linen or rice-paper screens turn harsh sun into milky light — a calm idea for a bedroom or reading nook'),
  steps('Villa Fikri · Villa Idea','Butik otel ışığı: tavandan değil, katmanlardan','Boutique-hotel lighting: layers, not the ceiling',
    [['Genel ışık: sıcak beyaz 2700 K, kısılabilir','Ambient: warm white 2700 K, dimmable',''],['Görev ışığı: okuma koltuğu, mutfak tezgâhı','Task light: the reading chair, the kitchen counter',''],['Vurgu: bal rengi taş duvarı aşağıdan yalayan ışık dokusunu ortaya çıkarır','Accent: light grazing the honey stone walls from below brings out their texture','✦'],['Akşam: ışıklar göz hizasının altında — abajurlar, aplikler','Evening: light below eye level — lamps and low wall lights','☾']],
    'Otellerin sırrı: akşam tavandaki lambayı kapatıp alçak, sıcak ışık adacıkları bırakmak','The hotels’ secret: switch off the ceiling light in the evening and leave low, warm islands of light','#2a2420','#070605',gap=6,d=54),
  fact('2700 K','Akşam için ideal ışık rengi yaklaşık 2700 kelvin: mum ve gün batımına yakın sıcak beyaz','The ideal evening light colour is about 2700 kelvin — a warm white close to candlelight and sunset','4000 K ve üstü ofis hissi verir; yatak odasında 2200–2700 K daha dinlendiricidir · 4000 K and above feels like an office — 2200–2700 K is more restful in a bedroom','#2a2018','#070504',d=30),
]),
S(15,16,'Hoş Geldiniz! · Welcome, Murat & Şerif',[
  welcome('pokut','Pokut Yaylası, Rize',[['Hoş geldiniz',8.2],['Murat &amp; Şerif',6.6]],None,'Sadece Sen’e hoş geldiniz — çay demde, sohbet sizde!','Welcome to Sadece Sen — the tea is brewing, the conversation is all yours!',d=45),
  guess('trabzon','Trabzon','Trabzon’un antik adı “Trapezus”. Sizce ne demek?','Trabzon’s ancient name was “Trapezus”. What do you think it means?','“Masa”! Yunanca trapeza — şehrin üstündeki tepe masa gibi düz olduğu için','“Table” — Greek trapeza, after the table-flat hill above the city',hint='İpucu: şehrin üstündeki düz tepeli Boztepe’yi düşünün · Hint: think of the flat-topped hill above the city',sec=22),
  choose('Bu akşamın sofrası için tek seçim hakkınız var!','You only get one pick for tonight’s table!',('hamsitava','Hamsi tava','Fried hamsi — crispy Black Sea anchovies'),('lazboregi','Laz böreği','Laz böreği — a sweet custard pastry in syrup'),'Herkes seçsin, sebebini söylesin!','Everyone picks — and says why!'),
  guess('hazelnut','Fındık · Hazelnuts','Dünyadaki fındığın yaklaşık ne kadarı Türkiye’de yetişiyor?','About how much of the world’s hazelnuts grow in Türkiye?','Yaklaşık üçte ikisi! Başı Ordu ve Giresun çekiyor','About two thirds — led by Ordu and Giresun',hint='Tahminleri sırayla söyleyin · Take turns guessing',sec=20,pos='50% 40%'),
  guess('kemence','Trabzon’da bir kemençe ustası · A kemençe maker in Trabzon','Karadeniz kemençesinin kaç teli var?','How many strings does the Black Sea kemençe have?','Üç! Dizde dik tutulur ve yayla çalınır','Three — held upright on the knee and played with a bow',sec=16,d=32),
  guess('blacksea','NASA uydusu · NASA satellite, 2017','Karadeniz’e kaç ülkenin kıyısı var?','How many countries have a Black Sea coast?','Altı: Türkiye, Gürcistan, Rusya, Ukrayna, Romanya ve Bulgaristan','Six: Türkiye, Georgia, Russia, Ukraine, Romania and Bulgaria',hint='İpucu: bir elin parmaklarından fazla · Hint: more than the fingers on one hand',sec=20,tag='Gerçek Uydu Fotoğrafı · Real Satellite Photo'),
  photo('kayabasi','Kayabaşı Yaylası, Düzköy, Trabzon','Bulut denizinin üstünde bir Trabzon yaylası','A Trabzon highland pasture above a sea of clouds','Nemli deniz havası yamaçlara tırmanırken soğur ve bulut olur — yaylaya çıkınca bulutlar ayağınızın altında kalır','Moist sea air cools as it climbs the slopes and turns to cloud — up on the yayla, the clouds lie below your feet',d=34),
]),
S(16,17,'Neresi Burası? · Where in the World?',[
  guess('chefchaouen',None,'Bu masmavi sokaklar hangi ülkede?','Which country are these bright blue streets in?','Fas — Şefşavan (Chefchaouen), Rif Dağları’nda','Morocco — Chefchaouen, in the Rif Mountains',hint='İpucu: Afrika’da, Akdeniz’e çok yakın · Hint: in Africa, close to the Mediterranean',lb=WHERE),
  guess('fushimi',None,'Binlerce turuncu kapının arasından geçen bu yol nerede?','Where is this path through thousands of orange gates?','Japonya, Kyoto — Fuşimi İnari: dağa tırmanan binlerce torii kapısı','Kyoto, Japan — Fushimi Inari, thousands of torii gates climbing the hill',hint='İpucu: Uzak Doğu · Hint: the Far East',lb=WHERE),
  choose('Bir hafta tatil: kuzeyin fiyortları mı, Ege’nin beyaz evleri mi?','A week away: northern fjords or white Aegean houses?',('lofoten','Lofoten, Norveç','Lofoten, Norway — red fishing cabins under sharp peaks'),('santorini','Santorini, Yunanistan','Santorini, Greece — white houses and blue domes above the sea'),'Herkes elini kaldırsın: A mı, B mi?','Hands up — A or B?'),
  guess('matera',None,'Bu taş şehir hangi ülkede?','Which country is this stone city in?','İtalya — Matera: kayaya oyulmuş mağara evleri bugün otel ve restoran','Italy — Matera: its cave houses cut into the rock are now hotels and restaurants',hint='İpucu: evlerin çoğu kayaya oyulmuş mağaralar · Hint: many homes are caves cut into the rock',lb=WHERE),
  guess('plitvice',None,'Turkuaz göller ve şelaleler… Neresi?','Turquoise lakes and waterfalls — where?','Hırvatistan — Plitvice Gölleri: 16 göl birbirine şelalelerle bağlanır','Croatia — Plitvice Lakes: 16 lakes linked by waterfalls',hint='İpucu: Balkanlar · Hint: the Balkans',lb=WHERE),
  ask('manarola','Manarola, Cinque Terre, İtalya · Italy','Sıradaki tatil nereye? Herkes bir yer söylesin!','Where should the next trip be? Everyone name a place!'),
]),
S(17,18,'Çay Saati Oyunları · Tea-Time Games',[
  g('hzstroop',d=52),
  guess('hamsi','İstanbul’da bir balık tezgâhı · A fish stall in Istanbul','Hamsi en lezzetli hangi mevsimde yenir?','In which season does hamsi taste best?','Kışın — yani tam şimdi! Soğuk sularda yağlanır; av sezonu eylülde açılır','In winter — right now! It fattens in the cold water; the season opens in September',sec=18,d=32),
  choose('Çayın yanına hangisi?','Which one goes with the tea?',('simit','Simit','Simit — the sesame bread ring'),('lokum','Lokum','Lokum — Turkish delight with pistachio and rose'),'Kararsız kalan çayları tazelesin!','Whoever can’t decide refills the tea!'),
  guess('cherries','Kiraz · Cherries','Kiraza adını verdiği söylenen Karadeniz şehri hangisi?','Which Black Sea city is said to have given the cherry its name?','Giresun! Antik adı Kerasus; rivayete göre Romalı Lucullus kirazı buradan Roma’ya götürdü','Giresun — ancient Kerasus; legend says the Roman Lucullus took cherries from here to Rome',hint='İpucu: antik adı Kerasus · Hint: its ancient name was Kerasus',sec=20),
  fact('200 saat','Bir araştırmaya göre birini “yakın arkadaş” yapmak için yaklaşık 200 saat birlikte vakit geçirmek gerekiyor','One study found it takes about 200 hours together to turn someone into a “close friend”','Jeffrey Hall, Kansas Üniversitesi, 2018 · Bu akşam saatleri doldurmaya devam! · Keep adding the hours tonight!','#1e2a30','#040708',d=30),
]),
S(18,19,'Hoş Geldin İbo! · Welcome, İbo!',[
  welcome('trabzonnight','Trabzon, gece · at night',[['Hoş geldin',8.2],['İbo!',8.8]],'Mami · Şerif · Murat · İbo','Ekip tamam — şimdi akşam başlasın!','The whole crew is here — let the evening begin!',d=48),
  steps('Oyun · Party Game','İki Doğru Bir Yalan: herkes kendisi hakkında üç şey söyler — biri yalan!','Two Truths and a Lie: everyone says three things about themselves — one is a lie!',
    [['Sırayla, kendinle ilgili üç cümle söyle','Take turns saying three things about yourself',''],['İkisi doğru, biri uydurma olsun','Two are true, one is made up',''],['Diğerleri yalanı tahmin etsin','The others guess the lie','?'],['Bilen bir puan alır; kimse bilemezse puan senin','A right guess wins a point — if nobody gets it, the point is yours','★']],
    'İpucu: en iyi yalan, en sıradan görünen cümledir','Tip: the best lie is the most ordinary-sounding one','#1c2a34','#04070a',gap=6,d=52),
  choose('Kış tatili: karlı bir yayla evi mi, sıcak bir ada mı?','Winter break: a snowy mountain hut or a warm island?',('pokutsnow','Pokut Yaylası, Rize','Pokut, Rize — snow, a wood stove and silence'),('maldives','Maldivler','The Maldives — white sand and turquoise water'),'Herkes seçsin — kazanan tarafa çay ısmarlanır!','Everyone picks — the winning side gets the tea!'),
  guess('kizkulesi',None,'Bu küçük kule hangi şehirde ve adı ne?','Which city is this little tower in — and what is it called?','İstanbul — Kız Kulesi, Üsküdar açıklarında küçük bir adacıkta','Istanbul — the Maiden’s Tower, on an islet off Üsküdar',hint='Isınma sorusu: en hızlı kim? · Warm-up: who’s fastest?',sec=12,d=28,lb=WHERE),
  guess('aurora','Norveç · Norway','Kuzey ışıklarını görmek için yılın hangi zamanı en iyisi?','When is the best time of year to see the northern lights?','Eylülden marta kadar — uzun ve karanlık gecelerde','September to March — in the long, dark nights',sec=18),
]),
S(19,20,'Dünyanın Gece Işıkları · World Lights at Night',[
  guess('galataday','Galata Kulesi, İstanbul · Galata Tower, Istanbul','Bu kule kaç yaşında?','How old is this tower?','Yaklaşık 680! Bugünkü Galata Kulesi 1348’de yapıldı','About 680 years — today’s Galata Tower was built in 1348',hint='İpucu: İstanbul’un en eski kulelerinden · Hint: one of Istanbul’s oldest towers',sec=20),
  photo('prague','Prag · Prague','Prag Kalesi ve Karlov Köprüsü, gece','Prague Castle above the Charles Bridge at night','Köprünün yapımı 1357’de başladı; üstünde 30 heykel var ve gece yarısından sonra neredeyse bomboş','Building began in 1357 — it is lined with 30 statues and almost empty after midnight',d=36),
  guess('moonsea','Andaman Denizi · Andaman Sea','Ay her yıl Dünya’dan ne kadar uzaklaşıyor?','How far does the Moon drift away from Earth each year?','Yaklaşık 3,8 santim — tırnaklarımızın uzama hızı kadar','About 3.8 cm — roughly as fast as our fingernails grow',hint='İpucu: bir cetvelle ölçebilirsiniz · Hint: you could measure it with a ruler',sec=20),
  ask('stockholm','Stockholm, mavi saat · blue hour','Gece yürüyüşü için dünyada tek bir şehir seçseniz, hangisi olurdu?','If you could pick one city in the world for a night walk, which would it be?'),
  fact('⅓','İnsanlığın üçte birinden fazlası, ışık kirliliği yüzünden Samanyolu’nu evinden göremiyor','More than a third of humanity can’t see the Milky Way from home because of light pollution','Falchi ve ark., Science Advances, 2016 · Karadeniz yaylalarında hâlâ görünüyor · Still visible from the Black Sea highlands','#141a2a','#020306',d=30),
]),
S(20,21,'Hayal Rotaları · Dream Routes',[
  choose('Hayal tren yolculuğu: hangisine binerdiniz?','Dream train ride — which would you board?',('landwasser','Glacier Express, İsviçre','Glacier Express, Switzerland — over the 65 m Landwasser Viaduct'),('doguekspresi','Doğu Ekspresi, Ankara–Kars','The Doğu Express, Ankara–Kars — about a day through the snow'),'Kim kiminle aynı kompartımana?','Who shares a compartment with whom?'),
  guess('faroe',None,'Bu şelale doğrudan okyanusa dökülüyor. Neresi?','This waterfall drops straight into the ocean. Where is it?','Faroe Adaları — Gásadalur köyündeki Múlafossur Şelalesi','The Faroe Islands — Múlafossur waterfall at Gásadalur',hint='İpucu: İzlanda ile Norveç arasında küçük adalar · Hint: small islands between Iceland and Norway',lb=WHERE),
  guess('moraine','Moraine Gölü, Kanada · Moraine Lake, Canada','Bu gölün rengi neden bu kadar turkuaz?','Why is this lake so turquoise?','“Buzul unu”! Buzulların öğüttüğü ince kaya tozu suda asılı kalır ve ışığı saçar','“Glacial flour” — fine rock dust ground by glaciers hangs in the water and scatters the light',sec=22),
  photo('halong','Vietnam','Ha Long Körfezi — denizden yükselen yaklaşık 1.600 kireçtaşı ada','Ha Long Bay — about 1,600 limestone islands rising from the sea','Adı “inen ejder” demek: efsaneye göre adaları denize inen bir ejder yaptı','Its name means “descending dragon” — legend says a dragon made the islands as it came down to the sea',d=36),
  guess('trolltunga','Norveç · Norway','Norveç’teki bu ünlü kaya çıkıntısının adı sizce ne?','What do you think this famous Norwegian rock ledge is called?','Trolltunga — “Trolün Dili”! Gölün yaklaşık 700 metre üstünde','Trolltunga — “the Troll’s Tongue”, about 700 m above the lake',hint='İpucu: masallardaki dev bir yaratığın bir parçası · Hint: part of a fairy-tale giant',sec=20),
]),
S(21,22,'Türkiye Bilgi Gecesi · Türkiye Trivia Night',[
  guess('tulips','Emirgan Korusu, İstanbul','İngilizce “tulip” (lale) kelimesi hangi Türkçe kelimeden geliyor?','The English word “tulip” comes from which Turkish word?','Tülbent! Lale çiçeği başa sarılan tülbende benzetilmiş','Tülbent, a turban cloth — the flower was likened to a turban',hint='İpucu: başa sarılan bir kumaş · Hint: a cloth wrapped around the head',sec=22),
  guess('safranbolu','Safranbolu, Karabük','Safranbolu adını nereden alıyor?','Where does Safranbolu get its name?','Safrandan! Çevresinde hâlâ safran yetişiyor; eski evleri UNESCO Dünya Mirası','From saffron — it still grows nearby; the old town is a UNESCO World Heritage Site',sec=18),
  steps('Fıkra · Folk Tale','Nasreddin Hoca ve doğuran kazan','Nasreddin Hodja and the pot that gave birth',
    [['Hoca komşusundan büyük bir kazan ödünç alır','The Hodja borrows a big pot from his neighbour',''],['Geri verirken içine küçük bir tencere koyar: “Kazanın doğurdu!”','He returns it with a little pan inside: “Your pot gave birth!”',''],['Komşu sevinir, sesini çıkarmaz','The neighbour is delighted and says nothing',''],['Hoca kazanı yine ister… ama bu kez geri getirmez: “Kazanın öldü!”','The Hodja borrows it again… and this time: “Your pot died!”',''],['“Kazan ölür mü?” — “Doğurduğuna inandın da öldüğüne niye inanmıyorsun?”','“Can a pot die?” — “You believed it gave birth, so why not that it died?”','😄']],
    'Sıra sizde: bir sonraki fıkrayı kim anlatıyor?','Your turn — who tells the next joke?','#2a2420','#070605',gap=6.5,d=52),
  guess('kizilirmak','Kapıkaya Köyü','Tamamen Türkiye’de akan en uzun nehir hangisi?','What is the longest river flowing entirely within Türkiye?','Kızılırmak — 1.355 km; Bafra’da Karadeniz’e dökülür','The Kızılırmak — 1,355 km, reaching the Black Sea at Bafra',hint='İpucu: adı bir renk · Hint: its name is a colour',sec=20),
  fact('61','İlk 67 ilin plaka kodları alfabetik sırayla verildi: 01 Adana … 61 Trabzon','The first 67 provinces got their plate codes in alphabetical order: 01 Adana … 61 Trabzon','Sonradan il olanlar 68’den 81’e kadar sıralandı · Later provinces were numbered 68 to 81','#1c2434','#04060a',d=30),
]),
S(22,23,'Gece Sohbeti · Late-Night Talk',[
  ask('milkyway2','Samanyolu altında bir gözlemci · Stargazing under the Milky Way','Çocukken ne olmak istiyordunuz?','What did you want to be when you were a kid?'),
  photo('fjordstars','Åbyfjorden, İsveç · Sweden','Sakin bir fiyortun üstünde yıldızlar ve Samanyolu','Stars and the Milky Way above a still fjord','Karanlık ve açık bir gecede çıplak gözle aynı anda yaklaşık 2.500 yıldız görülebilir','On a dark, clear night the naked eye can see about 2,500 stars at once',d=40),
  ask('startrails','La Hague Feneri, Fransa · France','Bu yıl sizi en çok güldüren an neydi?','What was the moment that made you laugh most this year?'),
  fact('30 kat','Başkalarıyla birlikteyken, tek başımıza olduğumuzdan yaklaşık 30 kat daha fazla güleriz','We laugh about 30 times more when we are with others than when we are alone','Robert Provine, gülme araştırmaları · laughter research · Kahkaha bulaşıcıdır · Laughter is contagious','#141c28','#020306',d=30),
]),
S(23,26,'Yağmurlu Gece · Rainy Night (sakin · calm)',[
  g('hzrainwin',d=80),
  q('Sesini değil, sözünü yükselt;|çiçekleri yetiştiren gök gürültüsü değil,|yağmurdur','Raise your words, not your voice — it is rain that grows flowers, not thunder','night',d=46),
  photo('flamingo','Flamingo · Flamingos','Tek ayak üstünde uyuyan flamingolar','Flamingos asleep on one leg','Tek ayakta durmak onlar için daha az yorucu: eklemleri kendiliğinden kilitlenir ve vücut ısısı daha az kaybolur','Standing on one leg is less tiring for them — the joints lock by themselves and less body heat is lost',d=42),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: hayalî bir yürüyüş','Before sleep: an imagined walk',
    [['Villanın kapısından çıkıyorsun; yağmur yeni dinmiş','You step out of the villa door — the rain has just stopped',''],['Islak taşların ve toprağın kokusu','The smell of wet stone and earth',''],['Uzakta denizin ve yaprakların sesi','The sound of the sea and the leaves in the distance',''],['Geri dönüyorsun: sıcak bir oda, yumuşak bir yastık','You come back to a warm room and a soft pillow','☾']],
    'Zihin, ayrıntılı ve sakin bir sahneyi hayal ederken düşüncelerin gürültüsünden uzaklaşır','When the mind pictures a calm, detailed scene, it drifts away from the noise of its thoughts','#0e1624','#020306',gap=7.5,d=50,bg='stars'),
  fact('4,5 mm','Yağmur damlası gözyaşı biçiminde değildir: küçükken küre, büyüdükçe hamburger ekmeği gibi yassılaşır','A raindrop isn’t tear-shaped — small ones are spheres, and bigger ones flatten like a burger bun','Yaklaşık 4,5 mm’yi aşan damla paraşüt gibi açılıp küçük damlalara bölünür · A drop bigger than about 4.5 mm opens like a parachute and splits','#101a26','#020305',d=32),
]),

]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-14.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
