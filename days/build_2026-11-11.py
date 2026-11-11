# Builds /workspace/tv-pages/days/2026-11-11.json (hourly sets 09:00-02:00). Pattern from build_2026-11-10.py.
import json,os
DATE='2026-11-11'; REV=58; NEXT='2026-11-12'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-11.json')))
FIX={'NASA/Apollo 17 crew; taken by either Harrison Schmitt or Ron Evans':'NASA / Apollo 17','Image by NASA, modifications by Seddon':'NASA','Surmene at en.wikipedia':'Surmene (en.wikipedia)','Garst, Warren, 1922-2016, photographer':'Warren Garst'}
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
    it=dict(k='hzphoto',d=d,f='m/h11-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
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
S(9,10,'Bulutların Üstünde · Above the Clouds',[
  photo('sultanmurat','Trabzon','Sultan Murat Yaylası yolu — bulut denizinin üstünde','The road to the Sultan Murat plateau — above a sea of clouds','Sabah serinliğinde vadilere çöken sis, yukarıdan bakınca deniz gibi görünür','In the cool morning, mist settles in the valleys and looks like a sea from above'),
  q('Güneş gibi ol|şefkat ve merhamette','Be like the sun in compassion and mercy','clay'),
  photo('memisaga','Sürmene, Trabzon','Memişağa Konağı — gece ışıklarıyla tarihî bir Karadeniz konağı','The Memişağa Mansion — a historic Black Sea mansion lit at night','Sürmene’nin tarihî konaklarından biri: taş ve ahşap bir arada','One of Sürmene’s historic mansions, where stone meets wood'),
  fact('1204–1461','Trabzon, 257 yıl boyunca Trabzon İmparatorluğu’nun başkentiydi','For 257 years Trabzon was the capital of the Empire of Trebizond','Fatih Sultan Mehmet şehri 1461’de aldı · Mehmed II took the city in 1461','#1f2a30','#05080a'),
  photo('dolphin','Yunus · Dolphins','Dalgaların üstünden atlayan bir yunus sürüsü','A pod of common dolphins leaping above the waves','Karadeniz’de üç tür yaşar: tırtak, mutur ve afalina','Three species live in the Black Sea: harbour porpoise, common dolphin and bottlenose dolphin'),
  rid('Yürür ama ayağı yok,<br>ağlar ama gözü yok.<br>Nedir?','It walks without feet and weeps without eyes. What is it?','Bulut!','A cloud — it drifts along and rains.',sec=16,c1='#22303a',c2='#05080a'),
]),
S(10,11,'Ses ve Şekil · Sound & Shape',[
  g('hzchladni',d=68),
  photo('seaorgan','Zadar, Hırvatistan · Croatia','Deniz Orgu — dalgalar basamakların altındaki borularda müzik çalıyor','The Sea Organ — waves play music through pipes under the steps','Mimar Nikola Bašić, 2005: her dalga farklı bir akor çıkarır','Architect Nikola Bašić, 2005: every wave plays a different chord'),
  fact('×4','Ses suda, havadakinden yaklaşık 4 kat hızlı yayılır','Sound travels about four times faster in water than in air','Havada ≈343 m/s, suda ≈1.480 m/s · Air ≈343 m/s, water ≈1,480 m/s','#14283a','#03060a'),
  steps('Akıllı Açıklama · Clever Explainer','Keman ve ney aynı notayı çalsa bile neden farklı duyulur?','Why do a violin and a ney sound different even on the same note?',
    [['Her notanın bir ana titreşimi vardır','Every note has a main vibration','temel · fundamental'],['Üstüne daha hızlı, daha sessiz titreşimler biner','Faster, quieter vibrations ride on top','armonikler · overtones'],['Her çalgı bunları farklı karıştırır','Each instrument mixes them differently',''],['Beynin bu karışımı “ses rengi” olarak tanır','Your brain hears the mix as a “tone colour”','tını · timbre']],
    'Aynı nota, farklı parmak izi','Same note, different fingerprint','#2a2030','#070508',gap=5.5),
  rid('Adını söylediğin an<br>bozulur.<br>Nedir?','Say its name and it is gone. What is it?','Sessizlik!','Silence.',sec=16,c1='#1e2430',c2='#050608'),
]),
S(11,12,'Akıllı Algoritmalar · Clever Algorithms',[
  g('hzsort',d=70),
  fact('el-Hârizmî','“Algoritma” sözcüğü, 9. yüzyılda Bağdat’ta çalışan matematikçi el-Hârizmî’nin adından gelir','The word “algorithm” comes from al-Khwarizmi, a 9th-century mathematician in Baghdad','“Cebir” (algebra) sözcüğü de onun kitabından gelir · “Algebra” comes from his book too','#2a2416','#060503',d=32),
  photo('jacquard','İskoçya Ulusal Müzesi · National Museum of Scotland','Jakar tezgâhı: desenleri delikli kartlar “programlıyor”','A Jacquard loom: punched cards “program” the pattern','Joseph Marie Jacquard, 1804 — delikli kart fikri ilk bilgisayarlara ilham verdi','Joseph Marie Jacquard, 1804 — punched cards later inspired early computers'),
  steps('Zihin Modeli · Mental Model','Aramayı ne zaman bırakmalı? %37 kuralı','When should you stop searching? The 37% rule',
    [['10 ev göreceksin; geri dönmek yok','You will view 10 houses, with no going back',''],['İlk %37’sine (≈4 ev) sadece bak, seçme','Just look at the first 37% (≈4 houses) — don’t choose',''],['Sonra, şimdiye kadarkilerin hepsinden iyi olan ilk evi al','Then take the first one better than all you’ve seen','✓'],['En iyisini bulma şansın ≈%37 — rastgele seçimin 3–4 katı','Your chance of getting the very best ≈37% — 3–4× better than random','']],
    'Optimal durma problemi · The optimal stopping problem','The “secretary problem” of mathematics','#1d2a36','#04070a',gap=6.5,d=60),
  photo('enigma','Kristiansand, Norveç · Norway','Bir Enigma şifre makinesi (1936)','An Enigma cipher machine (1936)','Alan Turing ve ekibi şifresini çözmek için elektromekanik makineler kurdu','Alan Turing and his team built electromechanical machines to break its code',fit='contain'),
  rid('İki fitilin her biri tam 1 saatte yanıyor<br>ama düzensiz. Yalnızca bunlarla<br>45 dakikayı nasıl ölçersin?','Two fuses each burn in exactly 1 hour, but unevenly. How do you measure 45 minutes?','A’yı iki ucundan, B’yi tek ucundan yak!','When A burns out (30 min), light B’s other end — it finishes 15 minutes later.',hint='Bir fitili iki ucundan yakarsan ne olur? · What if you light a fuse at both ends?',sec=26,d=44,c1='#2e2418',c2='#070504'),
]),
S(12,13,'Karadeniz Sofrası · Black Sea Table',[
  photo('muhlama','Çamlıhemşin, Rize','Muhlama (kuymak): mısır unu, tereyağı ve uzayan peynir','Muhlama (kuymak): cornmeal, butter and stretchy cheese','Peynir ne kadar uzarsa o kadar iyi olmuş demektir','The more the cheese stretches, the better it is'),
  photo('persimmon','Trabzon hurması · Persimmon','Yapraklar döküldükten sonra dalda kalan turuncu meyveler','Orange fruit still hanging after the leaves have fallen','Kasım tam mevsimi — Karadeniz’de bu meyveye “Trabzon hurması” denir','November is its season — around the Black Sea it is called the “Trabzon date”',fit='contain'),
  q('Akarsu gibi ol|cömertlik ve yardımda','Be like a flowing river in generosity and help','sea'),
  photo('lazboregi','Laz böreği','Laz böreği — ince yufka ve muhallebiyle yapılan bir Karadeniz tatlısı','Laz böreği — a Black Sea pastry of thin layers and custard','Adı börek ama tatlıdır','It is called a börek, yet it is a dessert'),
  steps('Akıllı Açıklama · Clever Explainer','Ekmek hamuru neden kabarır?','Why does bread dough rise?',
    [['Maya aslında minik, canlı mantarlardır','Yeast is really tiny living fungi',''],['Undaki şekerleri yerler','They eat the sugars in the flour',''],['Karbondioksit gazı çıkarırlar','They give off carbon dioxide gas','CO₂'],['Glüten ağı bu gazı balon gibi hapseder','The gluten network traps the gas like balloons',''],['Fırında gaz genleşir, maya ölür, delikler kalır','In the oven the gas expands, the yeast dies, the holes remain','']],
    'Her dilim ekmek, milyarlarca mayanın son eseri','Every slice is the last work of billions of yeast cells','#2e2618','#080604',gap=5.5),
  rid('Dışı yeşil, içi kırmızı,<br>çekirdeği siyah.<br>Nedir?','Green outside, red inside, black seeds. What is it?','Karpuz!','A watermelon.',sec=14,c1='#1e2c1c',c2='#050804'),
]),
S(13,14,'Taşın Ustaları · Masters of Stone',[
  photo('suleymaniye','İstanbul','Süleymaniye Camii’nin kubbesi — Mimar Sinan, 1557','The dome of the Süleymaniye Mosque — Mimar Sinan, 1557','Sinan’ın kandillerin isini toplayan bir oda yaptığı ve bu isten mürekkep elde edildiği anlatılır','Sinan is said to have built a room to collect lamp soot, which was made into ink',fit='contain'),
  photo('divrigi','Sivas','Divriği Ulu Camii’nin taş kapısı — UNESCO Dünya Mirası','The carved stone portal of the Divriği Great Mosque — UNESCO World Heritage','Yaklaşık 800 yıllık (1228–29); taş oymaları dantel gibi','About 800 years old (1228–29); its stone carving looks like lace'),
  steps('Akıllı Açıklama · Clever Explainer','Taş kemer neden çökmez?','Why doesn’t a stone arch fall down?',
    [['Her taş tek başına düşmek ister','Each stone on its own wants to fall',''],['Kemer biçimi her taşı komşusuna bastırır','The arch shape presses every stone against its neighbours',''],['Ağırlık eğri boyunca yanlara ve aşağı akar','The weight flows sideways and down along the curve','→'],['Tepedeki kilit taşı hepsini kilitler','The keystone at the top locks them all','kilit taşı · keystone']],
    'Harç olmadan bile binlerce yıl ayakta kalabilir','Even without mortar, an arch can stand for thousands of years','#2a2622','#070605',gap=6),
  photo('pantheon','Roma · Rome','Pantheon’un tavanındaki 8 metrelik açıklık: “göz” (oculus)','The 8-metre opening in the Pantheon’s ceiling: the oculus','Yaklaşık 1.900 yıllık bu kubbe hâlâ dünyanın en büyük donatısız beton kubbesi','Nearly 1,900 years old, it is still the world’s largest unreinforced concrete dome'),
  rid('Ne kadar çok kurularsa<br>o kadar ıslanır.<br>Nedir?','The more it dries, the wetter it gets. What is it?','Havlu!','A towel.',sec=15,c1='#2a2620',c2='#070605'),
]),
S(14,15,'Butik Otel Fikirleri · Boutique Hotel Ideas',[
  villa('olivepot','Washington','Büyük saksıda bir zeytin ağacı: avluya Akdeniz ruhu','An olive tree in a big pot: a Mediterranean soul for the courtyard','Zeytin rüzgâra ve kuraklığa dayanıklıdır; büyük saksıda yıllarca yaşar — kışın sert soğuktan korumak yeter','Olives shrug off wind and drought and live for years in a big pot — just shelter them from hard frost',fit='contain'),
  villa('courtyard','Elhamra, Granada · Alhambra','Uzun, durgun bir su aynası avluyu iki kat büyük gösterir','A long, still reflecting pool makes a courtyard feel twice as big','Durgun su gökyüzünü ve cepheyi yansıtır; hafif şırıltısı da dinlendirir','Still water mirrors the sky and the façade, and its soft trickle calms'),
  steps('Villa Fikri · Villa Idea','Beş duyuyla karşılama: misafir kapıdan girdiğinde…','A five-sense welcome: as a guest walks in…',
    [['Görme: yumuşak, sıcak ışık','Sight: soft, warm light',''],['Koku: taze demlenmiş Rize çayı','Smell: freshly brewed Rize tea',''],['Ses: alçak sesle kanun ya da dalga sesi','Sound: soft kanun music or the waves',''],['Dokunma: serin limon kolonyası, sıcak bir havlu','Touch: cool lemon cologne, a warm towel',''],['Tat: bir parça fındık ezmesi','Taste: a bite of hazelnut paste','']],
    'İlk dakikalar, konaklamanın havasını belirler','The first minutes set the mood of the whole stay','#26302a','#060807',gap=5.5,d=58),
  villa('cavehotel','Kapadokya · Cappadocia','Kapadokya’nın kaya otelleri: her odanın bir hikâyesi var','Cappadocia’s cave hotels: every room has a story','Fikir: beş süitin her birine bir Karadeniz adı ve kısa bir hikâye — misafir onu hatırlar','Idea: give each of the five suites a Black Sea name and a short story — guests remember it'),
  fact('Koku','Kokunun uyandırdığı anılar, diğer duyulara göre daha duygusal ve canlı olur','Memories triggered by scent tend to feel more emotional and vivid than those from other senses','Fikir: villaya özel bir imza koku — çay, fındık, ıhlamur · Idea: a signature villa scent — tea, hazelnut, linden','#2a2620','#070605',d=32),
]),
S(15,16,'Bitkilerin Zekâsı · Plant Intelligence',[
  photo('vouves','Girit · Crete','Vouves zeytin ağacı — hâlâ zeytin veriyor','The olive tree of Vouves — still bearing olives','Yaşının en az 2.000, belki 3.000 yıl olduğu tahmin ediliyor','Estimated to be at least 2,000 and perhaps 3,000 years old'),
  photo('mimosa','Küstüm otu · Mimosa pudica','Küstüm otu: dokununca yapraklarını kapatır','The sensitive plant folds its leaves when touched','Saniyeler içinde kapanır, birkaç dakika sonra yeniden açılır','It closes in seconds and reopens a few minutes later'),
  q('Toprak gibi ol|tevazuda','Be like the earth in humility','clay'),
  photo('flytrap','Venüs sinekkapanı · Venus flytrap','Tuzağın içindeki tetik tüyleri','The trigger hairs inside the trap','Kapanması için kısa sürede iki kez dokunulmalı — yani bitki “sayıyor”','A hair must be touched twice within a short time before it shuts — the plant “counts”',fit='contain'),
  photo('sherman','Kaliforniya · California','General Sherman: hacimce dünyanın en büyük tek gövdeli ağacı','General Sherman: the largest single-stem tree on Earth by volume','Yaklaşık 84 m boyunda; 2.000 yaşından büyük olduğu düşünülüyor','About 84 m tall and thought to be more than 2,000 years old',fit='contain'),
  rid('Ağzı yok ama su içer,<br>ayağı yok ama büyür.<br>Nedir?','No mouth, yet it drinks; no feet, yet it grows. What is it?','Ağaç!','A tree — it drinks through its roots.',sec=15,c1='#1c2c1e',c2='#040805'),
]),
S(16,17,'Göz ve Beyin · Eye & Brain',[
  g('hzzoll',d=42),
  photo('chameleon','Madagaskar · Madagascar','Panter bukalemun: iki gözü ayrı yönlere bakabilir','A panther chameleon: each eye can look a different way','Avı görünce iki gözünü aynı noktaya kilitler','When it spots prey, it locks both eyes onto it'),
  steps('Kısa Deney · Try It Now','Kör noktanı bul — şimdi dene!','Find your blind spot — try it now!',
    [['Sol gözünü kapat','Close your left eye',''],['Sağ gözünle ekranda tek bir noktaya bak','With your right eye, stare at one spot on the screen',''],['Parmağını yana doğru yavaşça kaydır','Slowly slide a finger out to the side',''],['Bir yerde parmak ucun kaybolur!','At one point your fingertip vanishes!','!']],
    'Görme sinirinin çıktığı yerde algılayıcı yok — beynin boşluğu doldurur','Where the optic nerve leaves the eye there are no sensors — your brain fills the gap','#1c2430','#040608',gap=7),
  g('hzmoire',d=55),
  photo('ames','Ames odası · Ames room','Ames odası: aynı boydaki insanlar dev ya da cüce görünür','An Ames room: people of the same height look like giants or dwarfs','Oda aslında çarpık; tek bir noktadan bakınca normal görünür','The room is actually skewed; from one viewpoint it looks normal'),
  rid('Gözü var<br>ama göremez.<br>Nedir?','It has an eye but cannot see. What is it?','İğne!','A needle.',sec=14,c1='#24202c',c2='#060508'),
]),
S(17,18,'Büyük Yolculuklar · Great Journeys',[
  photo('storks','Ak leylek · White stork','Göç eden ak leylekler','White storks on migration','Her sonbahar Avrupa’dan Afrika’ya binlerce kilometre uçarlar; birçoğu İstanbul Boğazı’ndan geçer','Each autumn they fly thousands of kilometres from Europe to Africa; many pass over the Bosphorus'),
  fact('1.000.000+','Her sonbahar Batum üzerinden bir milyondan fazla yırtıcı kuş göç eder','Every autumn more than a million birds of prey migrate past Batumi','Karadeniz’in doğu ucu dünyanın en büyük kuş göçü geçitlerinden biri · The eastern Black Sea is one of the world’s great migration bottlenecks','#1e2a30','#05070a',d=32),
  photo('wildebeest','Doğu Afrika · East Africa','Mara Nehri’ni geçen yaban öküzleri','Wildebeest crossing the Mara River','Her yıl bir milyondan fazla yaban öküzü taze otun peşinde dev bir daire çizer','Every year over a million wildebeest walk a huge loop following fresh grass'),
  photo('humpback','Kosta Rika · Costa Rica','Sudan fırlayan bir kambur balina','A humpback whale breaching','Bazı kambur balinalar bir yılda 8.000 km’den fazla göç eder','Some humpback whales migrate more than 8,000 km in a year'),
  photo('salmon','New York','Şelaleye atlayan bir somon','A salmon leaping up a waterfall','Somonlar doğdukları dereyi kokusundan bulur','Salmon find their way back to the stream they hatched in by its smell'),
  rid('Bir yerden bir yere gider<br>ama hiç kıpırdamaz.<br>Nedir?','It goes from place to place but never moves. What is it?','Yol!','A road.',sec=15,c1='#2a2a1e',c2='#070705'),
]),
S(18,19,'Akşam Oyunları · Evening Games',[
  g('hzspiro',d=70),
  rid('3 tavuk 3 günde 3 yumurta yumurtluyor.<br>6 tavuk 6 günde<br>kaç yumurta yumurtlar?','If 3 hens lay 3 eggs in 3 days, how many eggs do 6 hens lay in 6 days?','12!','Each hen lays 1 egg every 3 days, so 6 hens × 2 eggs = 12.',hint='“6” cevabı tuzak… · “6” is the trap…',sec=24,d=40,c1='#2e2618',c2='#080604'),
  photo('rubik','Rubik Küpü · Rubik’s Cube','43 kentilyondan fazla farklı dizilişi olan bir oyuncak','A toy with more than 43 quintillion possible positions','Ama her diziliş en fazla 20 hamlede çözülebilir — 2010’da kanıtlandı','Yet every position can be solved in 20 moves or fewer — proved in 2010',fit='contain'),
  steps('Mantık Bulmacası · Logic Puzzle','Doğrucu ve Yalancı','The Truth-teller and the Liar',
    [['Yol ikiye ayrılıyor: biri köye, biri ormana','The road splits: one way to the village, one to the forest',''],['İki kardeş var: biri hep doğru, biri hep yalan söyler','Two brothers stand there: one always tells the truth, one always lies',''],['Hangisi hangisi bilmiyorsun; tek soru hakkın var','You don’t know which is which, and you get one question','?'],['Sor: “Kardeşin bana köy yolu olarak hangisini gösterirdi?”','Ask: “Which way would your brother say leads to the village?”',''],['Gösterilen yolun tersine git!','Take the other road!','✓']],
    'Cevap her durumda yalancıdan bir kez geçer — hep yanlış yolu gösterir','Either way the answer passes through the liar once, so it always points the wrong way','#2a2030','#070508',gap=6.5,d=62),
  fact('52!','İyi karıştırılmış bir iskambil destesi, büyük ihtimalle tarihte hiç var olmamış bir sıralamadadır','A well-shuffled deck of cards is almost certainly in an order that has never existed before','52! ≈ 8×10⁶⁷ olası sıralama · ≈8×10⁶⁷ possible orders','#1a2a24','#040806'),
  rid('Hangisi daha ağır:<br>bir kilo pamuk mu,<br>bir kilo demir mi?','Which is heavier: a kilo of cotton or a kilo of iron?','İkisi de bir kilo!','They both weigh one kilo.',sec=14,c1='#24242c',c2='#060608'),
]),
S(19,20,'Gezegen Dansı · Dance of the Planets',[
  g('hzrose',d=62),
  photo('bluemarble','Apollo 17, 1972','“Mavi Bilye”: Apollo 17’den bütün Dünya','“The Blue Marble”: the whole Earth from Apollo 17','Tarihte en çok çoğaltılan fotoğraflardan biri; Afrika ve Antarktika görülüyor','One of the most reproduced photos in history — Africa and Antarctica are visible',fit='contain'),
  fact('%99,8','Güneş Sistemi’ndeki tüm kütlenin %99,8’i Güneş’tedir','The Sun holds 99.8% of all the mass in the Solar System','Bütün gezegenler geri kalan %0,2’yi paylaşıyor · All the planets share the remaining 0.2%','#2a2014','#070503'),
  photo('olympus','Mars','Olympus Mons: Güneş Sistemi’nin en büyük yanardağlarından biri','Olympus Mons: one of the largest volcanoes in the Solar System','Yaklaşık 22 km yüksekliğinde — Everest’in 2,5 katı','About 22 km high — two and a half times Everest',fit='contain'),
  steps('Ölçek Yolculuğu · Scale Journey','Güneş bir futbol topu olsaydı…','If the Sun were a football…',
    [['Dünya: 2 mm’lik bir toplu iğne başı','Earth: a 2 mm pinhead','24 m ötede'],['Jüpiter: bir bilye','Jupiter: a marble','120 m ötede'],['Neptün: bir mercimek tanesi','Neptune: a lentil','700 m ötede'],['En yakın yıldız: başka bir futbol topu…','The nearest star: another football…','6.400 km ötede']],
    'Uzay neredeyse tamamen boşluktur','Space is almost entirely empty','#101828','#020306',gap=6.5,bg='stars'),
  photo('pluto','Plüton · Pluto','Plüton ve buzdan “kalbi” — New Horizons, 2015','Pluto and its icy “heart” — New Horizons, 2015','Kalbin sol yarısı donmuş azottan oluşan dev bir ovadır','The left half of the heart is a vast plain of frozen nitrogen',fit='contain'),
  rid('Nereye gidersen git<br>peşinden gelir gibi görünür;<br>geceleri parlar. Nedir?','Wherever you go it seems to follow you, and it shines at night. What is it?','Ay!','The Moon — it is so far away that it seems to travel with you.',sec=16,c1='#141a2c',c2='#030407'),
]),
S(20,21,'Dünyayı Değiştiren Fikirler · Ideas That Changed the World',[
  photo('piri','Topkapı Sarayı · Topkapı Palace','Piri Reis haritası, 1513 — Amerika kıyılarını gösteren en eski haritalardan biri','The Piri Reis map, 1513 — one of the oldest surviving maps to show the Americas','Ceylan derisine çizildi; 1929’da Topkapı Sarayı’nda yeniden bulundu','Drawn on gazelle-skin parchment; rediscovered in Topkapı Palace in 1929',fit='contain',d=42),
  photo('gutenberg','New York','Gutenberg İncili — hareketli metal harflerle basılan ilk büyük kitap (1450’ler)','The Gutenberg Bible — the first major book printed with movable metal type (1450s)','Matbaadan önce tek bir kitabın elle kopyalanması aylar sürebiliyordu','Before printing, copying a single book by hand could take months'),
  fact('38 μs','Einstein’ın görelilik kuramı hesaba katılmasa GPS her gün yaklaşık 10 km sapardı','Without Einstein’s relativity, GPS would drift by about 10 km every day','Uydu saatleri günde ≈38 mikrosaniye hızlı işler · Satellite clocks run ≈38 microseconds a day fast','#1c2430','#040608',d=32),
  photo('wright','Kitty Hawk, 1903','Wright kardeşlerin ilk motorlu uçuşu','The Wright brothers’ first powered flight','12 saniye, 37 metre — 66 yıl sonra insanlar Ay’da yürüdü','12 seconds, 37 metres — 66 years later people walked on the Moon'),
  steps('Akıllı Açıklama · Clever Explainer','Buzdolabı nasıl soğutur?','How does a fridge make things cold?',
    [['Aslında soğuk üretmez — ısıyı dışarı taşır','It doesn’t make cold — it carries heat out',''],['Özel bir sıvı içeride buharlaşır ve ısıyı emer','A special fluid evaporates inside and soaks up heat',''],['Kompresör onu sıkıştırıp ısıtır','The compressor squeezes it and heats it up',''],['Arkadaki borular bu ısıyı odaya bırakır','The coils at the back release that heat into the room','→ sıcak · warm'],['Döngü yeniden başlar','The cycle starts again','↺']],
    'Elini buzdolabının arkasına yaklaştır — içeriden alınan ısıyı hissedersin','Hold your hand near the back of the fridge — you’ll feel the heat taken from inside','#182a30','#03070a',gap=5.5),
  rid('Anahtarlarım var<br>ama hiçbir kapıyı açamam.<br>Ben neyim?','I have keys but open no doors. What am I?','Klavye — ya da piyano!','A keyboard — or a piano.',sec=16,c1='#22222c',c2='#060608'),
]),
S(21,22,'Sessiz Galeri · Quiet Gallery',[
  art('wave','Kanagawa’da Büyük Dalga — Katsushika Hokusai, yaklaşık 1831','The Great Wave off Kanagawa — Katsushika Hokusai, c. 1831','Bir ahşap baskı; binlerce kopya basıldı — dalganın ardında minicik Fuji Dağı','A woodblock print made in thousands of copies — tiny Mount Fuji sits behind the wave','Katsushika Hokusai'),
  q('Deniz gibi ol|hoşgörüde','Be like the sea in tolerance','night'),
  art('tortoise','Kaplumbağa Terbiyecisi — Osman Hamdi Bey, 1906','The Tortoise Trainer — Osman Hamdi Bey, 1906','Ağır kaplumbağaları eğitmeye çalışan bir adam: sabır mı, ince bir mizah mı? Bugün İstanbul’da, Pera Müzesi’nde','A man trying to train slow tortoises: patience, or gentle satire? Today it hangs in Istanbul’s Pera Museum','Osman Hamdi Bey'),
  art('starry','Rhône Üzerinde Yıldızlı Gece — Vincent van Gogh, 1888','Starry Night Over the Rhône — Vincent van Gogh, 1888','Arles’da, nehir kıyısında, gaz lambalarının ışığı suya yansırken boyandı','Painted on the riverbank in Arles, with gas lamps reflected in the water','Vincent van Gogh'),
  art('lilies','Nilüferler — Claude Monet','Water Lilies — Claude Monet','Monet, Giverny’deki bahçesinin havuzunu yaklaşık 250 kez boyadı','Monet painted the pond in his Giverny garden about 250 times','Claude Monet'),
]),
S(22,23,'Uykudan Önce · Before Sleep',[
  q('Gece gibi ol|başkalarının kusurlarını örtmede','Be like the night in covering the faults of others','night',d=46),
  photo('lighthouse','Kuzey Karolina · North Carolina','Ocracoke Feneri ve Samanyolu','Ocracoke Lighthouse beneath the Milky Way','Karanlık bir gecede çıplak gözle birkaç bin yıldız görülebilir','On a dark night the naked eye can see a few thousand stars',d=42),
  steps('Sakin Açıklama · Calm Explainer','Ay’ın neden hep aynı yüzünü görürüz?','Why do we always see the same side of the Moon?',
    [['Ay kendi çevresinde bir tur dönerken…','The Moon turns once on its axis…',''],['…Dünya’nın çevresinde de bir tur atar','…in the same time it takes to circle Earth','≈27,3 gün'],['Bu yüzden hep aynı yüzü bize dönük kalır','So the same face always points at us',''],['Arka yüzü ilk kez 1959’da bir uzay aracıyla fotoğraflandı','Its far side was first photographed by a spacecraft in 1959','Luna 3']],
    'Buna kütleçekimsel kilitlenme denir','This is called tidal locking','#0c1222','#010206',gap=6.5,bg='stars'),
  fact('1.000.000','Bir yağmur damlası, yaklaşık bir milyon minik bulut damlacığının birleşmesiyle oluşur','One raindrop forms from roughly a million tiny cloud droplets joining together','Yağmur sesine iyi uykular · Sleep well to the sound of rain','#121a28','#020306',d=32),
  rid('Gün boyu peşinden gelir,<br>gece olunca kaybolur.<br>Nedir?','It follows you all day and disappears at night. What is it?','Gölgen!','Your shadow.',sec=15,c1='#10162a',c2='#020307'),
]),
S(23,26,'Gece Havuzu · Night Pond (sakin · calm)',[
  g('hzkoi',d=75),
  fact('⅓','Hayatımızın yaklaşık üçte birini uyuyarak geçiririz','We spend about a third of our lives asleep','90 yılın yaklaşık 30’u · About 30 of every 90 years','#121a24','#020305',d=32),
  steps('Sakin Yolculuk · Calm Journey','Bir yağmur damlasının yolculuğu','The journey of a raindrop',
    [['Karadeniz’den buharlaşır','It evaporates from the Black Sea',''],['Yükselir, soğur, bir buluta katılır','It rises, cools and joins a cloud',''],['Bulut Kaçkarlar’a çarpınca yağmur bırakır','When the cloud meets the Kaçkar Mountains, it lets go of rain',''],['Dereler onu yeniden denize taşır','Streams carry it back to the sea','↺']],
    'Bu gece yağan yağmur, belki dün denizdeydi','Tonight’s rain may have been in the sea yesterday','#0e1824','#020306',gap=7,d=52),
  fact('270°','Baykuşlar başlarını yaklaşık 270 derece çevirebilir','Owls can turn their heads about 270 degrees','Gecenin sessiz avcıları · The silent hunters of the night','#141a20','#030405',d=32),
  rid('Hep geliyor<br>ama hiç varmıyor.<br>Nedir?','It is always coming but never arrives. What is it?','Yarın!','Tomorrow.',sec=16,c1='#0e1424',c2='#020306'),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-11.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
