# Builds /workspace/tv-pages/days/2026-11-26.json (hourly sets 09:00-02:00). Thursday.
# 09 Trabzon morning · 10 living art: patterns that make themselves (NEW hzbz, hzpiwalk) · 11 glaciers · 12 paper · 13 Caspar David Friedrich · 14 Saturn
# 15 illusions (NEW hztusi, hzflashlag) · 16 Schelling (NEW hzschelling) · 17-19 DJ Taş Act 1 Jazz House Lounge · 19-22 Act 2 Sunset · 22-02 Act 3 Night (NEW hzburc), stills only, no video.
# Photos m/h26-* (/workspace/hourly/dl26.py+q26.json, dl26b.py+q26b.json), credits days/credits-2026-11-26.json.
import json,os
DATE='2026-11-26'; REV=85; NEXT='2026-11-27'
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-26.json')))
ART={'titan':'Kevin M. Gill','pleiades':'NASA, ESA, AURA/Caltech, Palomar Observatory','cabin':'U.S. Fish and Wildlife Service Alaska','drums':'Jimmy Baikovicius','patara':'William Neuheisel',
 'monumentvalley':'Christian Mehlführer','portofino':'Gjacquenot','papercut':'Fanghong','peritomoreno':'Luca Galuzzi','aletsch':'Tobias Alt','hexagon':'NASA / JPL-Caltech / SSI / Cornell','saturnrings':'NASA / JPL / Space Science Institute',
 'ataturkkosku':'Yazar Haber','mendenhall':'Jörg Hempel','schelling':'New America'}
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
    it=dict(k='hzphoto',d=d,f='m/h26-%s.jpg'%k,lb=lb,tr=tr,en=en,cr=cr(k))
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
    it=dict(k='hzwelcome',d=d,f='m/h26-%s.jpg'%k,lb=lb,lines=lines,tr=tr,en=en,cr=cr(k))
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
S(9,10,'Perşembe Sabahı · Thursday Morning',[
  photo('sumela','Sümela Manastırı · Sumela Monastery, Maçka','Sümela Manastırı, Karadağ’ın sarp yamacına yaslanmış','Sumela Monastery clinging to the steep face of Mount Karadağ','Geleneğe göre 4. yüzyılda kuruldu; bugün gördüğün binaların çoğu 18. ve 19. yüzyıldan','By tradition it was founded in the 4th century — most of the buildings you see today date from the 18th and 19th centuries',d=40),
  q('Bütün evren|seninmiş gibi parla','Shine as if the whole universe is yours','sea',d=38),
  photo('ataturkkosku','Atatürk Köşkü · Soğuksu, Trabzon','Soğuksu’da ağaçların arasında beyaz köşk','The white mansion among the trees at Soğuksu','Atatürk Trabzon’a gelişlerinde burada kaldı; köşk bugün müze','Atatürk stayed here on his visits to Trabzon — today the mansion is a museum',d=38),
  fact('%90','Karadeniz’in suyunun yaklaşık %90’ı oksijensiz: 150–200 metrenin altında neredeyse hiç canlı yok, bu yüzden dipteki antik gemiler binlerce yıl bozulmadan kalıyor','About 90% of the Black Sea’s water has no oxygen — below 150–200 m almost nothing lives, so ancient ships on the bottom survive for thousands of years','Karadeniz’in sırrı · A Black Sea secret','#13242c','#04080a',d=34),
  photo('seragolu','Sera Gölü · Akçaabat, Trabzon','Sera Gölü’nde sakin bir sabah: ormanla çevrili su','A calm morning on Sera Lake, ringed by forest','Göl, bir heyelanın vadiyi tıkamasıyla oluştu; Trabzon merkezine yalnızca yarım saat','The lake formed when a landslide blocked the valley — only half an hour from central Trabzon',d=38),
  photo('calcave','Çal Mağarası · Düzköy, Trabzon','Mağaranın içinde kızıl ışıkta sarkıtlar','Stalactites in a reddish light inside the cave','Türkiye’nin en uzun mağaralarından biri; içinden bir yeraltı deresi akar','One of the longest caves in Turkey — an underground stream runs through it',d=38),
  rid('Ondan aldıkça büyür.|Nedir?','The more you take away from it, the bigger it gets. What is it?','Çukur!','A hole!',sec=16),
]),
S(10,11,'Yaşayan Sanat: Kendiliğinden Doğan Desenler · Living Art: Patterns That Make Themselves',[
  g('hzbz',d=90),
  photo('bzdish','Belousov–Zhabotinsky tepkimesi · BZ reaction (Steinbock laboratuvarı · Steinbock lab)','Bir petri kabında kendiliğinden halka halka yayılan kimyasal dalgalar','Chemical waves spreading in rings by themselves in a Petri dish','Karışım dakikalar içinde renk değiştirip durur; bu yüzden “kimyasal saat” denir','The mixture keeps changing colour over minutes — that is why it is called a “chemical clock”',fit='contain',d=38),
  steps(CT,'İyi bir buluş neden reddedilir?','Why does a good discovery get rejected?',
    [['1951: Sovyet kimyacı Boris Belousov, kendi kendine renk değiştirip duran bir karışım bulur','1951: Soviet chemist Boris Belousov finds a mixture that keeps changing colour by itself','🧪'],['Dergiler makaleyi geri çevirir: “Kimya bunu yapamaz, tepkimeler sonunda durulur”','Journals turn the paper down: “Chemistry can’t do that — reactions always settle down”',''],['1959’da yalnızca kısa bir özet yayımlayabilir ve konuyu bırakır','In 1959 he manages to publish only a short abstract, and gives the subject up',''],['1960’larda genç Anatol Zhabotinsky deneyi tekrarlayıp açıklar; 1980’de Lenin Ödülü verilir, Belousov ise 1970’te ölmüştür','In the 1960s young Anatol Zhabotinsky repeats and explains it; the Lenin Prize follows in 1980 — but Belousov had died in 1970','']],
    'Bir şey “imkânsız” görünüyorsa, belki yalnızca alışılmadık','If something looks “impossible”, maybe it is only unfamiliar','#16222c','#04080a',gap=8,d=58),
  g('hzpiwalk',d=84),
  fact('39 basamak','π’nin ilk 39 basamağı, gözlemlenebilir evrenin çevresini bir hidrojen atomu kadar hassas hesaplamaya yeter','The first 39 digits of π are enough to work out the circumference of the observable universe to within the width of a hydrogen atom','Ne kadar π yeter? · How much π is enough?','#14202a','#04070a',d=32),
  rid('Hangi saat günde yalnızca|iki kez doğruyu gösterir?','Which clock is right only twice a day?','Durmuş bir saat!','A stopped clock!',sec=16),
]),
S(11,12,'Nefes Kesen Yerler: Buzullar · Breathtaking Places: Glaciers',[
  photo('peritomoreno','Perito Moreno Buzulu, Arjantin · Perito Moreno Glacier, Argentina','Patagonya’da göle inen dev buz cephesi','The great ice front reaching the lake in Patagonia','Cephesi yaklaşık 5 km genişliğinde; kopan buz parçalarının gürültüsü çok uzaklardan duyulur','Its front is about 5 km wide — the roar of breaking ice can be heard from far away',d=40),
  photo('aletsch','Büyük Aletsch Buzulu, İsviçre · Great Aletsch Glacier, Switzerland','Eggishorn’dan bakınca Aletsch’in kıvrılan buz nehri','The winding ice river of the Aletsch seen from the Eggishorn','Alplerin en büyük buzulu, yaklaşık 20 km uzunluğunda; ama her yıl onlarca metre geri çekiliyor','The largest glacier in the Alps, about 20 km long — but it retreats by tens of metres every year',d=40),
  photo('jokulsarlon','Jökulsárlón, İzlanda · Iceland','Buzul gölünde yeni devrilmiş, masmavi buzdağları','Freshly rolled-over, deep-blue icebergs in the glacier lagoon','Buzdağı devrilince altındaki sıkışmış, kabarcıksız buz görünür: kırmızı ışığı yutar, maviyi yansıtır','When an iceberg rolls over, the dense, bubble-free ice from below shows — it swallows red light and gives back blue',d=40),
  photo('mendenhall','Franz Josef Buzulu, Yeni Zelanda · Franz Josef Glacier, New Zealand','Yağmur ormanına doğru inen bir buzul','A glacier sliding down towards the rainforest','Bu kadar alçakta, denize bu kadar yakın biten çok az buzul var: batıdan gelen bol kar onu besliyor','Very few glaciers end this low and this close to the sea — heavy snow from the west feeds it',d=40),
  dict(k='hzchoose',d=40,q='Hangisini kendi gözünle görmek isterdin?',qe='Which would you rather see with your own eyes?',a=dict(f='m/h26-peritomoreno.jpg',t='Buzdan kopan dev bir parça',e='A giant slab breaking off the ice',tag='Perito Moreno'),b=dict(f='m/h26-jokulsarlon.jpg',t='Sessizce yüzen buzdağları',e='Icebergs drifting in silence',tag='Jökulsárlón'),p='Herkes birini seçsin, sonra nedenini söylesin',pe='Everyone picks one, then says why',cr='Fotolar · Photos: Luca Galuzzi · CC BY-SA 2.5 / Giles Laurent · CC BY-SA 4.0 · Wikimedia Commons'),
  fact('%69','Dünyadaki tatlı suyun yaklaşık %69’u buzullarda ve buz örtülerinde donmuş hâlde duruyor','About 69% of the world’s fresh water is locked up as ice in glaciers and ice sheets','Donmuş tatlı su · Frozen fresh water','#14222e','#04080c',d=30),
]),
S(12,13,'Kâğıdın Şiiri · Poetry in Paper',[
  photo('ebru','Ebru · su üstünde boyama · marbling','Suyun üstüne damlatılan boyalardan fırçayla bir desen','A pattern brushed from paints dropped onto water','Boyalar kitreyle koyulaştırılmış suyun yüzünde yüzer; kâğıt üstüne yatırılınca desen bir kez, yalnızca bir kez aktarılır. Türk ebrusu 2014’te UNESCO listesine girdi','The paints float on water thickened with gum tragacanth; when paper is laid on top the pattern transfers once, and only once. Turkish ebru joined the UNESCO list in 2014',d=42),
  art('marbling','Nedim Sönmez','Ebru Lale','Ebru Tulip','Suyun üstünde boyayla çizilmiş bir lale. Çiçekli ebruyu 20. yüzyılın başında Necmeddin Okyay geliştirdi','A tulip drawn in paint on water. Floral ebru was developed by Necmeddin Okyay in the early 20th century',d=40),
  photo('origami','Origami turnaları · origami cranes','Tek bir kâğıttan, kesmeden katlanmış turnalar','Cranes folded from single sheets, with no cuts','Japon geleneğinde bin turna katlayanın bir dileğinin gerçekleşeceğine inanılır (senbazuru)','In Japanese tradition, whoever folds a thousand cranes is granted a wish (senbazuru)',d=38),
  photo('papercut','Çin kâğıt kesme sanatı · Chinese paper cutting','Köpek Yılı için kırmızı kâğıttan kesilmiş bir desen','A design cut from red paper for the Year of the Dog','Kâğıt kesme sanatı (jianzhi) 2009’da UNESCO listesine alındı; desenler çoğu zaman katlanmış kâğıda tek seferde kesilir','The art of paper cutting (jianzhi) joined the UNESCO list in 2009 — designs are often cut in one go into folded paper',fit='contain',d=38),
  g('hzdragon',d=56),
  fact('√2','A4 kâğıdının uzun kenarı kısa kenarının √2 katı: ikiye katlayınca aynı orana sahip iki A5 elde edersin. A0 tam 1 metrekare','The long side of an A4 sheet is √2 times the short side — fold it in half and you get two A5 sheets of exactly the same shape. A0 is exactly one square metre','ISO 216 · kâğıt boyutları · paper sizes','#1a2028','#05080b',d=32),
  rid('Bir kâğıt en fazla|kaç kez ikiye katlanabildi?','What is the most times a sheet of paper has been folded in half?','12 kez! 2002’de lise öğrencisi Britney Gallivan, yaklaşık 1,2 km uzunluğunda bir kâğıtla başardı','12 times! In 2002 high-school student Britney Gallivan did it with a strip about 1.2 km long',hint='Sık söylenen 7 değil · Not the often-quoted 7',sec=20),
  q('İşleri ruhundan yaptığında,|içinde akan bir nehir hissedersin','When you do things from your soul, you feel a river moving in you','ink',d=38),
]),
S(13,14,'Büyük Ustalardan: Caspar David Friedrich’in Sessizliği · From the Great Masters: The Silence of Caspar David Friedrich',[
  art('wanderer','Caspar David Friedrich, yaklaşık 1818','Sis Denizinin Üzerinde Gezgin','Wanderer above the Sea of Fog','Gezgini sırtından görürüz, yüzünü değil: manzaraya onun gözünden bakarız. Sırtı dönük figür (Rückenfigur) ressamın en sevdiği fikirlerden biri','We see the wanderer from behind, never his face — so we look at the view through his eyes. The figure seen from behind (Rückenfigur) is one of the painter’s favourite ideas'),
  art('monkbysea','Caspar David Friedrich, 1808–1810','Deniz Kıyısında Keşiş','The Monk by the Sea','İlk sergilendiğinde izleyiciler şaşırdı: uçsuz bucaksız gök ve deniz önünde minicik bir insan. Röntgen incelemeleri, Friedrich’in denize önce gemiler çizip sonra sildiğini gösterdi','When first shown it baffled viewers — a tiny person before endless sky and sea. X-rays revealed that Friedrich first painted ships on the sea, then painted them out'),
  art('chalkcliffs','Caspar David Friedrich, yaklaşık 1818','Rügen’deki Tebeşir Kayalıkları','Chalk Cliffs on Rügen','1818’deki evliliğinden sonraki balayı yolculuğunu anlattığı düşünülür','It is thought to recall his honeymoon trip after his marriage in 1818'),
  q('Ressam yalnızca önünde gördüğünü değil,|içinde gördüğünü de resmetmeli','The painter should paint not only what he sees before him, but also what he sees within him','night',d=38,lb='Ressamın Sözü · A Painter’s Words',by='Caspar David Friedrich'),
  art('seaofice','Caspar David Friedrich, 1823–1824','Buz Denizi','The Sea of Ice','Kırık buz tabakalarının arasında ezilmiş bir geminin kıçı görünüyor. Friedrich hayattayken alıcı bulamadı; bugün Hamburg Kunsthalle’de','The stern of a crushed ship shows between the broken slabs of ice. It found no buyer in Friedrich’s lifetime — today it hangs in the Hamburg Kunsthalle'),
  art('moonrise','Caspar David Friedrich, 1822','Denizde Ay Doğuşu','Moonrise over the Sea','Kayaların üstünde oturan üç kişi, eve dönen yelkenlilere ve doğan aya bakıyor','Three figures sitting on the rocks watch sailboats coming home and the moon rising'),
]),
S(14,15,'Gökyüzünün Harikaları: Satürn · Wonders of the Sky: Saturn',[
  photo('saturneq','Satürn · Saturn (Cassini, 2009 ekinoksu · 2009 equinox)','Ekinoksta Satürn: Güneş halkaları tam kenarından aydınlatıyor','Saturn at equinox — the Sun lights the rings exactly edge-on','Ana halkalar 270.000 km’den geniş ama çoğu yerde yalnızca onlarca metre kalın: oranı, bir futbol sahası genişliğinde bir kâğıt gibi','The main rings are more than 270,000 km across but in most places only tens of metres thick — like a sheet of paper as wide as a football pitch',fit='contain',d=40),
  photo('hexagon','Satürn’e yukarıdan · Saturn from above (Cassini, 2013)','Kuzey kutbunun üzerinden: ortada altıgen biçimli dev bir rüzgâr akıntısı','From above the north pole — a giant six-sided jet stream at the centre','Altıgenin her kenarı Dünya’nın çapından uzun. 1981’de Voyager fark etti; neden altı köşeli olduğu hâlâ tartışılıyor','Each side of the hexagon is longer than Earth is wide. Voyager spotted it in 1981 — why it has six sides is still debated',fit='contain',d=40),
  steps(SJ,'Işık hızıyla Satürn’e','To Saturn at the speed of light',
    [['1,3 saniye: Ay’ı geçtik','1.3 seconds: past the Moon','🌙'],['8 dakika 20 saniye: Güneş’in uzaklığı kadar yol aldık','8 minutes 20 seconds: as far as the Sun',''],['3–22 dakika: Mars, nerede olduğuna göre','3–22 minutes: Mars, depending on where it is',''],['33–54 dakika: Jüpiter','33–54 minutes: Jupiter',''],['67–92 dakika: Satürn! Cassini’nin her mesajı Dünya’ya bu kadar sürede ulaşıyordu','67–92 minutes: Saturn! Every message from Cassini took this long to reach Earth','🪐']],
    'Satürn’e baktığında, onun bir buçuk saat kadar önceki hâlini görüyorsun','When you look at Saturn you see it as it was about an hour and a half ago','#141c2a','#04060c',gap=8,d=56),
  photo('enceladus','Enceladus · Satürn’ün uydusu · a moon of Saturn (Cassini)','Enceladus’un güney kutbundan uzaya fışkıran su buharı ve buz','Water vapour and ice spraying into space from Enceladus’ south pole','Buz kabuğunun altında küresel bir okyanus var; Güneş Sistemi’nde yaşam aranacak yerlerin başında geliyor','Beneath its icy crust lies a global ocean — one of the top places to look for life in the Solar System',fit='contain',d=38),
  photo('titan','Titan · Satürn’ün en büyük uydusu · Saturn’s largest moon (Cassini, işlenmiş · processed)','Solda Titan’ın gerçek rengi, kalın bir sis; sağda kızılötesinde yüzeyi','Left, Titan in true colour, wrapped in thick haze — right, its surface in infrared','Titan’da metan ve etan gölleri var: Dünya dışında yüzeyinde sıvı bulunduğu bilinen tek yer. 2005’te Huygens aracı yüzeyine indi','Titan has lakes of methane and ethane — the only place besides Earth known to have liquid on its surface. The Huygens probe landed there in 2005',fit='contain',d=40),
  rid('Satürn’ü dev bir küvete|koysaydık ne olurdu?','If we put Saturn in a giant bathtub, what would happen?','Yüzerdi! Ortalama yoğunluğu sudan az: yaklaşık 0,69 g/cm³','It would float! Its average density is less than water’s — about 0.69 g/cm³',sec=18),
  fact('10,5 saat','Satürn o kadar hızlı döner ki bir günü yalnızca yaklaşık 10,5 saat sürer; bu yüzden kutuplarından basık görünür','Saturn spins so fast that its day lasts only about 10.5 hours — that is why it looks squashed at the poles','Satürn’de bir gün · A day on Saturn','#16202c','#04070c',d=30),
]),
S(15,16,'Göz Oyunları: Beynin Uydurduğu Hareket · Tricks of the Eye: Motion the Brain Makes Up',[
  g('hztusi',d=60),
  fact('1259','Nasîrüddîn Tûsî, bugünkü İran’daki Meraga’da zamanının en büyük gözlemevini kurdu; “Tusi çifti” yüzyıllar sonra Kopernik’in kitabında da benzer biçimde yer aldı','Nasir al-Din al-Tusi founded the greatest observatory of his age at Maragheh, in today’s Iran — a device like the “Tusi couple” appears centuries later in Copernicus’ book','Bilim tarihinden · From the history of science','#1a2230','#05080c',d=32),
  g('hzflashlag',d=52),
  fact('~0,1 s','Gözünün gördüğü bir şeyin bilince ulaşması yaklaşık saniyenin onda biri sürer: hep biraz geçmişi görürüz. Beyin hareketli şeyleri tahminle ileri iterek bu farkı kapatır','It takes about a tenth of a second for what your eye sees to reach awareness — we always see a little of the past. The brain closes the gap by pushing moving things ahead by prediction','Gecikmeli dünya · A delayed world','#141c24','#04070a',d=32),
  rid('Bir yarışta ikinciyi geçtin.|Şimdi kaçıncısın?','In a race you overtake the runner in second place. What place are you in now?','İkinci! Birinci değil','Second — not first!',sec=16),
]),
S(16,17,'Zekice Düşünce: Küçük Tercihler, Büyük Desenler · Clever Thinking: Small Preferences, Big Patterns',[
  g('hzschelling',d=70),
  photo('schelling','Thomas C. Schelling (1921–2016)','Ekonomist Thomas Schelling bir konuşmada','Economist Thomas Schelling giving a talk','Oyun kuramı üzerine çalışmalarıyla 2005 Nobel Ekonomi Ödülü’nü Robert Aumann ile paylaştı','He shared the 2005 Nobel Prize in Economics with Robert Aumann for his work on game theory',fit='contain',d=34),
  steps(CT,'Trafik neden sebepsiz yere durur?','Why does traffic stop for no reason?',
    [['2008: Japonya’da 22 araç, 230 metrelik dairesel bir pistte aynı hızla dönmeye başladı','2008: in Japan, 22 cars began circling a 230-metre track at the same speed','🚗'],['Ortada ne kaza vardı ne de daralan bir yol','There was no accident and no narrowing of the road',''],['Bir sürücü birazcık fren yaptı; arkasındaki biraz daha fazla, onun arkasındaki daha da fazla…','One driver braked a little; the one behind braked a bit more, the next one more still…',''],['Birkaç dakika içinde geriye doğru yürüyen bir “hayalet sıkışıklık” doğdu','Within minutes a “phantom jam” was born, travelling backwards round the track','']],
    'Kimse sıkışıklık istemedi; küçük tepkiler toplanınca kendiliğinden çıktı','Nobody wanted a jam — it emerged as small reactions added up','#1a2228','#05080a',gap=8,d=56),
  fact('⅓ → ¾','Schelling modelinde herkes yalnızca komşularının üçte birinin kendine benzemesini ister; sonunda çoğu zaman komşuların dörtte üçe yakını benzer olur','In Schelling’s model everyone wants just a third of their neighbours to be like them — and in the end, often close to three quarters are','Toplamın sürprizi · The surprise of the sum','#1a2228','#05080a',d=32),
  rid('Dışarıda 3 düğme, kapalı odada 3 lamba var.|Odaya yalnızca bir kez girebilirsin.|Hangi düğme hangi lambanın?','Three switches outside, three lamps in a closed room. You may enter only once. Which switch is which lamp?','Birini aç, birkaç dakika bekle, kapat; ikincisini aç ve gir. Yanan: ikinci. Sönük ama sıcak: birinci. Sönük ve soğuk: üçüncü','Turn one on, wait a few minutes, turn it off; turn the second on and go in. Lit: the second. Off but warm: the first. Off and cold: the third',hint='Lambanın ışıktan başka bir şeyi daha var · A lamp gives off more than light',sec=24,d=40),
]),
S(17,18,'DJ Taş · Caz House Lounge · Jazz House Lounge — Riviera’da gece · night on the Riviera',[
  card('portofino','DJ Taş · Sadece Sen — '+REAL+' · Portofino, İtalya · Italy',[['DJ Taş',7.2],['Bu akşam · Tonight',3.4]],
   'Üç perdelik bir akşam: Caz House Lounge → Gün Batımı (19:00) → Gece (22:00). Müzik HomePod’da','An evening in three acts: Jazz House Lounge → Sunset (19:00) → Night (22:00). Music on the HomePod',d=32),
  g('hzboids',d=58),
  photo('drums','Fırçalı davul · Brushes on the snare (Punta del Este Caz Festivali · Jazz Festival)','Fırçalar trampetin üstünde: cazın fısıltı gibi ritmi','Brushes on the snare — the whispering rhythm of jazz','Tel fırçalar 1920’lerde yaygınlaştı: davulcu vurmak yerine sürter, yumuşak ve sürekli bir “şşş” sesi çıkar','Wire brushes spread in the 1920s — the drummer sweeps instead of striking, for a soft, continuous “shhh”',d=38,act=A1),
  art('capri','Alfred Stevens, 19. yüzyıl · 19th century','Menton, Gece Olurken','Menton, Almost Night','Menton, Fransız Rivierası’nın İtalya sınırındaki son kasabası; her şubat limon festivaliyle ünlü','Menton is the last town on the French Riviera before the Italian border — famous for its lemon festival every February',d=40),
  g('hzmandel',d=60),
  fact('Chicago, 1980’ler','“House” adı, DJ Frankie Knuckles’ın çaldığı Chicago’daki The Warehouse kulübünden gelir. Caz house bu ritme caz akorlarını ve canlı enstrümanları katar','The name “house” comes from The Warehouse, the Chicago club where DJ Frankie Knuckles played. Jazz house adds jazz chords and live instruments to that beat','Müziğin kökleri · Roots of the music','#14202a','#04070a',d=32),
],pre='dj'),
S(18,19,'Caz House Lounge · Jazz House Lounge — Villa Fikri: Şarap ve Peynir Akşamı · Villa Idea: A Wine & Cheese Evening',[
  villa('winecellar','Château Kirwan, Bordeaux','Alt katta küçük bir şarap köşesi: serin, karanlık, birkaç raf ve tek bir sıcak ışık','A small wine corner downstairs: cool, dark, a few racks and one warm light','Şarap en iyi 12–14 °C civarında, karanlıkta, yatık ve sarsıntısız saklanır','Wine keeps best at around 12–14 °C, in the dark, lying down and undisturbed',act=A1),
  villa('cheese','bir peynir tabağı · a cheese board','Misafirlere: üç dört peynir, kuru meyve, ceviz, bal ve ince dilimlenmiş ekmek','For guests: three or four cheeses, dried fruit, walnuts, honey and thinly sliced bread','Kural: yumuşaktan serte, hafiften keskine doğru diz; peynirleri servisten yarım saat önce buzdolabından çıkar','The rule: arrange from soft to hard, mild to strong — and take the cheese out of the fridge half an hour before serving',act=A1),
  q('Nerede durursan dur,|oranın ruhu ol','Wherever you stand, be the soul of that place','clay',d=38),
  photo('redwine','Kırmızı şarap · Red wine','Kadehe dökülen kırmızı şarap','Red wine being poured into a glass','Kırmızı şarabın rengi üzüm kabuğundan gelir; üzümün suyu neredeyse her zaman renksizdir','The colour of red wine comes from the grape skins — the juice itself is almost always clear',d=36,act=A1),
  g('hzvoronoi',d=56),
  photo('vineyard','Napa Vadisi, Kaliforniya · Napa Valley, California','Sonbaharda kızıla dönen bir bağ','A vineyard turning red in autumn','Anadolu dünyanın en eski bağcılık bölgelerinden biri: Türkiye’de 600’den fazla yerli üzüm çeşidi var — Öküzgözü, Boğazkere, Kalecik Karası…','Anatolia is one of the oldest wine regions on Earth — Turkey has more than 600 native grape varieties: Öküzgözü, Boğazkere, Kalecik Karası…',d=40,act=A1),
],pre='dj'),
S(19,20,'Gün Batımı · Sunset — Likya kıyısı · the Lycian coast',[
  card('kekova','DJ Taş · 2. Perde · Act 2 — '+REAL+' · Kekova, Antalya',[['Gün Batımı',6.4],['Sunset',3.6]],
   'Liste değişti: şimdi “Sadece Sen Sunset” çalıyor','The playlist has changed — now playing “Sadece Sen Sunset”',d=30),
  photo('olympos','Çıralı, Antalya','Çıralı plajı ve Olimpos’un dağları','Çıralı beach and the mountains of Olympos','Hemen yukarıdaki Yanartaş’ta binlerce yıldır yerden çıkan doğal gaz alevleri yanıyor','On the Chimaera just above, natural gas flames have burned out of the ground for thousands of years',d=40,act=A2),
  g('hzfern',d=56),
  photo('patara','Patara, Antalya','Patara’nın kumunda ayak izleri','Footprints in the sand at Patara','Türkiye’nin en uzun kumsallarından biri; deniz kaplumbağaları (Caretta caretta) yazın buraya yumurtlar','One of Turkey’s longest beaches — loggerhead turtles (Caretta caretta) come here to nest in summer',d=40,act=A2),
  photo('kalkan','Kalkan, Kaş','Kalkan’ın beyaz evleri koyun çevresinde','Kalkan’s white houses around the bay','Bir zamanlar küçük bir liman ve balıkçı kasabasıydı; bugün terasları akşam güneşine bakar','Once a small harbour and fishing town — today its terraces face the evening sun',d=38,act=A2),
  photo('phaselis','Phaselis, Kemer','Çamların arasında antik Phaselis’in taşları','The stones of ancient Phaselis among the pines','Üç limanı olan bir Likya kenti; Büyük İskender MÖ 334–333 kışını burada geçirdi','A Lycian city with three harbours — Alexander the Great spent the winter of 334–333 BC here',d=38,act=A2),
],pre='dj'),
S(20,21,'Gün Batımı · Sunset — çöllerde akşam · evening in the deserts',[
  photo('monumentvalley','Monument Valley, ABD · USA','Batan güneşte Monument Valley’nin kumtaşı kuleleri','The sandstone buttes of Monument Valley at sunset','Navajo topraklarında; kuleler yer yer 300 metreye kadar yükselir','On Navajo land — the buttes rise up to about 300 m',d=42,act=A2),
  photo('uluru','Uluru, Avustralya · Australia','Akşam ışığında Uluru','Uluru in the evening light','Anangu halkı için kutsal; 2019’dan beri tırmanmak yasak. Güneş batarken kayanın rengi dakika dakika değişir','Sacred to the Anangu people, it has been closed to climbers since 2019. As the sun sets the rock changes colour minute by minute',d=40,act=A2),
  g('hzchaos',d=56),
  photo('atacama','Ay Vadisi, Atacama, Şili · Valle de la Luna, Chile','Atacama’da Ay Vadisi’nin rüzgârla oyulmuş kayaları','The wind-carved rocks of the Valley of the Moon in the Atacama','Atacama, kutuplar dışında dünyanın en kurak çölü; bazı istasyonlar yıllarca tek damla yağmur ölçmedi','The Atacama is the driest desert outside the poles — some stations have gone years without measuring a drop of rain',d=40,act=A2),
  photo('whitedesert','Beyaz Çöl, Mısır · White Desert, Egypt','Farafra yakınlarında rüzgârın tebeşirden yonttuğu beyaz kayalar','White rocks carved from chalk by the wind near Farafra','Bu tebeşir, milyonlarca yıl önce burayı kaplayan denizdeki minicik canlıların kabuklarından oluştu','This chalk was made from the shells of tiny sea creatures, from a sea that covered the area millions of years ago',d=40,act=A2),
  fact('30 °C','Kum ve kuru hava ısıyı tutmaz: bazı çöllerde gündüz ile gece arasındaki fark 30 °C’yi aşar. Gün batınca çöl hızla serinler','Sand and dry air don’t hold heat — in some deserts the difference between day and night is more than 30 °C. Once the sun sets, the desert cools fast','Çölde akşam · Evening in the desert','#20181a','#07050a',d=30),
],pre='dj'),
S(21,22,'Gün Batımı · Sunset — Ege köyleri · Aegean villages',[
  photo('alacati','Alaçatı, Çeşme','Alaçatı’nın taş yel değirmenleri','The stone windmills of Alaçatı','Hiç dinmeyen rüzgârı Alaçatı’yı Türkiye’nin rüzgâr sörfü merkezi yaptı','Its never-ending wind made Alaçatı Turkey’s windsurfing capital',d=40,act=A2),
  photo('sirince','Şirince, Selçuk','Zeytinliklerle çevrili Şirince köyü','Şirince village among the olive groves','Köy, meyve şaraplarıyla ve 19. yüzyıldan kalma taş evleriyle bilinir','The village is known for its fruit wines and its 19th-century stone houses',d=40,act=A2),
  g('hzkoch',d=56),
  photo('foca','Eski Foça, İzmir','Eski Foça’da ağaçların arasından denize inen güneş','The sun going down into the sea through the trees at Eski Foça','Foça kıyıları, nesli tehlikedeki Akdeniz foklarının yaşadığı az sayıdaki yerden biri','The Foça coast is one of the few places where endangered Mediterranean monk seals still live',d=40,act=A2),
  q('Batışı gördün;|doğuşu da gör','You have seen the setting — now see the rising','clay',d=38),
  rid('Neyi kırmadan|kullanamazsın?','What can’t you use until you break it?','Yumurta!','An egg!',sec=16),
],pre='dj'),
S(22,23,'Gece · Night — kış ışıklarında eski şehirler · old towns in winter lights (sakin · calm)',[
  card('bruges','DJ Taş · 3. Perde · Act 3 — '+REAL+' · Brugge, Belçika · Bruges, Belgium',[['Gece',6.6],['Night',3.6]],
   'Şimdi “Sadece Sen Night” çalıyor: daha yumuşak, daha sakin','Now playing “Sadece Sen Night” — softer and calmer',d=30),
  photo('tallinn','Tallinn, Estonya · Estonia','Tallinn’in ortaçağ surları gece ışıklarında','Tallinn’s medieval walls in the night lights',d=44,act=A3,quiet=1),
  photo('colmar','Colmar, Fransa · France','Colmar’da yarı ahşap evler ve sakin bir akşam sokağı','Half-timbered houses and a quiet evening street in Colmar',d=44,act=A3,quiet=1),
  g('hzsnow',d=70),
  photo('ljubljana','Ljubljana, Slovenya · Slovenia','Ljubljana’da nehir kıyısında kış ışıkları','Winter lights along the river in Ljubljana',d=44,act=A3,quiet=1),
  photo('stockholm','Gamla Stan, Stockholm','Stockholm’ün eski şehrinde bir kış pazarı','A winter market in Stockholm’s old town',d=44,act=A3,quiet=1),
],pre='dj'),
S(23,26,'Gece · Night — yıldızlar ve takımyıldızlar · stars and constellations (sakin · calm)',[
  g('hzburc',d=120),
  photo('pleiades','Ülker · the Pleiades','Ülker yıldız kümesi ve çevresindeki mavi toz','The Pleiades and the blue dust around them',d=46,act=A3,quiet=1),
  photo('andromeda','Andromeda Gökadası · Andromeda Galaxy','Andromeda: çıplak gözle görülen en uzak şeylerden biri, 2,5 milyon ışık yılı ötede','Andromeda — one of the farthest things the naked eye can see, 2.5 million light years away',d=46,act=A3,quiet=1),
  g('hzember',d=80),
  photo('cabin','Alaska · bir kış gecesi · a winter night','Karlı ormanda ışığı yanan bir kulübe','A cabin with its light on in the snowy forest',d=46,act=A3,quiet=1),
  q('Gözlerini kapat,|âşık ol ve orada kal','Close your eyes, fall in love, stay there','night',d=40),
  photo('crescent','Hilal · Crescent Moon','İyi geceler · Good night','Good night',d=46,fit='contain',act=A3,quiet=1),
],pre='dj'),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-26.py. 17:00–02:00 = DJ Taş evening (Jazz House Lounge → Sunset 19:00 → Night 22:00, synced with the HomePod playlists; stills only at night, no video). Content log: used-content.md',sets=sets),open(os.path.join(HERE,'%s.json'%DATE),'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'][:60])
