# Builds /workspace/tv-pages/days/2026-11-16.json (hourly sets 09:00-02:00). Pattern from build_2026-11-15.py. Monday: fresh-start, clever thinking, light & art.
import json,os
DATE='2026-11-16'; REV=66; NEXT='2026-11-17'
C=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'credits-2026-11-16.json')))
FIX={'Credits to Mourad Ben Abdallah':'Mourad Ben Abdallah','NASA image courtesy of the DSCOVR':'NASA / DSCOVR EPIC','blgrssby from St. Louis':'blgrssby','al-Jazari':'el-Cezerî · al-Jazari (1315 kopyası · copy, The Met)','Ala ad-Din Mansur-Shirazi':'Alaeddin Mansur · Ala ad-Din Mansur-Shirazi (Şehinşahname, 1581)','NOIRLab/NSF/AURA':'NOIRLab / NSF / AURA','卓珺 黄':'Zhuojun Huang'}
def artist(k):
    a=C[k]['artist']
    for f,t in FIX.items():
        if a.startswith(f): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace(' rs','')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=38,pos=None):
    it=dict(k='hzphoto',d=d,f='m/h16-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
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
    it=dict(k='hzguess',d=d,f='m/h16-%s.jpg'%k,lb='Bil Bakalım · Can You Guess? — '+REAL+' · '+where,q=qq,qe=qe,a=a,ae=ae,sec=sec,cr=cr(k))
    if hint: it['hint']=hint
    return it
def g(k,d=60): return dict(k=k,d=d)
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)
TE='Düşünce Deneyi · Thought Experiment'; CT='Zekice Düşünce · Clever Thinking'
sets=[
S(9,10,'Pazartesi Sabahı · Monday Morning',[
  photo('inceburun','İnceburun, Sinop','İnceburun Feneri — Türkiye’nin en kuzey ucunda yeni bir haftanın sabahı','İnceburun Lighthouse — a new week’s morning at the northern tip of Türkiye','Anadolu’nun en kuzey noktası, yaklaşık 42° kuzey enleminde; fener 19. yüzyıldan beri gemilere yol gösteriyor','The northernmost point of Anatolia, at about 42° north — the lighthouse has guided ships since the 19th century',fit='contain',d=40),
  q('Sabah rüzgârının sana söyleyecek|sırları var; uykuya geri dönme','The breeze at dawn has secrets to tell you — don’t go back to sleep','sea',d=44),
  photo('mahakampos','Çaykara, Trabzon','Mahakampos Yaylası — bulutların hemen üstünde ahşap yayla evleri','Mahakampos plateau — wooden highland houses just above the clouds','Bu evlerin çoğu yalnızca yazın açılır; kışın yayla karın altında sessizce bekler','Most of these houses open only in summer — in winter the plateau waits quietly under the snow',d=40),
  fact('Pazartesi','“Pazartesi” kelimesi “pazar ertesi”nden gelir: pazar gününden sonraki gün','“Pazartesi” (Monday) comes from “pazar ertesi” — the day after market day','Cumartesi de aynı mantıkla: “cuma ertesi” · Saturday too: “cuma ertesi”, the day after Friday','#22301f','#050805',d=30),
  photo('palovit','Çamlıhemşin, Rize','Palovit Şelalesi — ormanın içinden dökülen beyaz bir perde','Palovit Waterfall — a white curtain falling through the forest','Aynı adı taşıyan Palovit Yaylası’na giden yolun üzerinde; yürüyüşçülerin sevdiği bir mola yeri','On the road up to the Palovit plateau of the same name — a favourite stop for walkers',fit='contain',d=38),
  rid('Sözlükte her zaman<br>“yanlış” yazılan kelime hangisi?','Which word is always spelled “wrong” in the dictionary?','“Yanlış” kelimesi!','The word “wrong”!',sec=16,c1='#2a2418',c2='#080604'),
]),
S(10,11,'Yaşayan Sanat: Doğanın Formülleri · Living Art: Nature’s Formulas',[
  g('hzfern',d=75),
  photo('fiddlehead','Eğreltiotu sürgünü · Fern fiddlehead','Açılmaya hazırlanan bir eğreltiotu sürgünü — doğanın sarmalı','A fern fiddlehead about to unfurl — nature’s spiral','Eğreltiotları dinozorlardan çok önce de vardı: yaklaşık 360 milyon yıldır yeryüzündeler','Ferns were here long before the dinosaurs — they have been on Earth for about 360 million years',d=38),
  photo('nautilus','Nautilus kabuğu · Nautilus shell','İçinden kesilmiş bir nautilus kabuğu: her oda bir öncekinden biraz büyük','A nautilus shell cut open — each chamber a little larger than the last','Hayvan büyüdükçe yeni bir odaya taşınır ve arkasını kapatır. Sık söylenenin aksine bu sarmal “altın oran” değildir — daha sıkıdır','As the animal grows it moves into a new chamber and seals the old one. Despite the popular claim, the spiral is not the golden ratio — it is tighter',fit='contain',d=40),
  rid('Kökleri ve dalları var;<br>ama ne gölgesi var ne meyvesi.<br>Nedir?','It has roots and branches, but no shade and no fruit. What is it?','Soy ağacı!','A family tree.',sec=16,c1='#1f2a1c',c2='#050705'),
]),
S(11,12,'Galeri: Bahçede · Gallery: In the Garden',[
  art('sargent','Karanfil, Zambak, Zambak, Gül — John Singer Sargent, 1885–86','Carnation, Lily, Lily, Rose — John Singer Sargent, 1885–86','Sargent bu tabloyu iki yaz boyunca, yalnızca alacakaranlıkta birkaç dakika süren mor ışıkta boyadı — her akşam yaklaşık 20 dakika','Sargent painted it over two summers, only in the few minutes of violet dusk light — about 20 minutes each evening'),
  art('irises','Süsenler — Vincent van Gogh, 1889','Irises — Vincent van Gogh, 1889','Saint-Rémy’deki hastanenin bahçesinde, oraya vardığı ilk hafta yaptı; kalabalığın içinde tek bir beyaz süsen dikkat çekiyor','Painted in the asylum garden at Saint-Rémy in his first week there — one white iris stands out in the crowd'),
  art('vetheuil','Sainte-Adresse’de Teras — Claude Monet, 1867','Garden at Sainte-Adresse — Claude Monet, 1867','Monet sahneyi Japon baskılarından esinlenerek üç yatay bant halinde kurdu: bahçe, deniz, gökyüzü. Hasır şapkalı oturan, ressamın babası','Inspired by Japanese prints, Monet built the scene in three bands — garden, sea, sky. The seated man in the hat is the painter’s father'),
  art('orangetrees','Portakal Ağaçları — Gustave Caillebotte, 1878','The Orange Trees — Gustave Caillebotte, 1878','Ressamın kardeşi Martial ve kuzeni, Yerres’teki aile bahçesinde; büyük saksılardaki portakal ağaçları kışı seralarda geçirirdi','The painter’s brother Martial and their cousin in the family garden at Yerres — orange trees in big tubs spent the winter indoors'),
  art('klimtgarden','Ayçiçekli Köy Bahçesi — Gustav Klimt, yaklaşık 1907','Farm Garden with Sunflowers — Gustav Klimt, c. 1907','Klimt manzaralarının çoğunu kare tuvallere yaptı; bu tabloda gökyüzü hiç yok — yalnızca çiçekler','Klimt painted most of his landscapes on square canvases — this one has no sky at all, only flowers'),
  q('Doğru ve yanlış fikirlerinin ötesinde|bir çayır var; seninle orada buluşacağım','Out beyond ideas of wrongdoing and rightdoing there is a field — I’ll meet you there','clay',d=44),
]),
S(12,13,'Zekice Düşünce · Clever Thinking',[
  g('hzhilbert',d=62),
  steps(CT,'Fermi tahmini: Bir insan hayatı boyunca kaç kez göz kırpar?','A Fermi estimate: how many times does a person blink in a lifetime?',
    [['Dakikada yaklaşık 15 kez göz kırparız','We blink about 15 times a minute','👁'],['Günde yaklaşık 16 saat uyanığız: 960 dakika','We are awake about 16 hours a day — 960 minutes',''],['960 × 15 ≈ günde 14.400 kez','960 × 15 ≈ 14,400 blinks a day',''],['Bir yılda ≈ 5 milyon; 80 yılda ≈ 420 milyon','≈ 5 million a year; ≈ 420 million in 80 years','≈']],
    'Enrico Fermi öğrencilerine böyle sorular sorardı: kaba ama akıllı tahminler çoğu zaman gerçeğe şaşırtıcı derecede yakın çıkar','Enrico Fermi loved asking his students questions like this — rough but clever estimates often land surprisingly close to the truth','#1c2430','#04060a',gap=6.5,d=52),
  photo('soroban','Soroban · Japon abaküsü · Japanese abacus','Soroban: elektriksiz bir hesap makinesi','The soroban — a calculator that needs no electricity','Ustaları zamanla boncukları yalnızca zihinlerinde hayal ederek, abaküs olmadan büyük sayıları saniyeler içinde toplayabiliyor (anzan)','Experts learn to picture the beads in their minds and add huge numbers in seconds without any abacus at all (anzan)',fit='contain',d=38),
  steps(CT,'Ockham’ın Usturası: iki açıklama da uyuyorsa hangisini seçersin?','Ockham’s razor: when two explanations both fit, which do you choose?',
    [['Mutfakta yerde kırık bir bardak; kedi masanın yanında oturuyor','A broken glass on the kitchen floor; the cat sits next to the table','🐈'],['Açıklama A: kedi masaya atladı, bardağı devirdi','Explanation A: the cat jumped up and knocked it over',''],['Açıklama B: küçük bir deprem oldu ama başka hiçbir şey kıpırdamadı','Explanation B: a tiny earthquake struck, but nothing else moved',''],['Daha az varsayım isteyen açıklama genellikle doğruya daha yakındır','The explanation needing fewer assumptions is usually closer to the truth','✂']],
    '14. yüzyıl İngiliz düşünürü Ockhamlı William’a atfedilir. Kesin bir kural değil — ama iyi bir başlangıç noktası','Attributed to the 14th-century English thinker William of Ockham — not a strict rule, but a good place to start','#2a2420','#070605',gap=6.5,d=50),
  rid('Bir saatin akrebi ile yelkovanı<br>bir günde kaç kez üst üste gelir?','How many times a day do the hour and minute hands of a clock overlap?','22 kez! 24 değil: 11 ile 1 arasında yalnızca bir kez, saat 12’de buluşurlar','22 times, not 24 — between 11 and 1 they meet only once, at 12',sec=22,d=38,c1='#1c2a30',c2='#040708'),
  fact('10¹⁰⁰','Google adını “googol”dan aldı: 1’in ardından 100 sıfır','Google took its name from the “googol” — a 1 followed by 100 zeros','Kelimeyi 1920 civarında 9 yaşındaki Milton Sirotta uydurdu · The word was coined around 1920 by 9-year-old Milton Sirotta','#1b2230','#05070b',d=30),
]),
S(13,14,'Düşünce Deneyleri · Thought Experiments',[
  steps(TE,'Platon’un Mağarası: hayatı boyunca yalnızca gölgeleri gören insanlar…','Plato’s Cave: people who have only ever seen shadows…',
    [['İnsanlar bir mağarada, sırtları girişe dönük oturuyor','People sit in a cave with their backs to the entrance','🕯'],['Arkalarındaki ateşin önünden geçen nesnelerin yalnızca gölgelerini görüyorlar','They see only the shadows of objects carried past a fire behind them',''],['Onlar için gerçek bu: duvardaki gölgeler','For them, reality is the shadows on the wall',''],['Biri dışarı çıkıyor: güneş, renkler, gerçek dünya!','One of them walks outside — sunlight, colour, the real world!',''],['Geri dönüp anlattığında kimse ona inanmıyor','When he comes back and tells them, nobody believes him','?']],
    'Platon, Devlet, yaklaşık MÖ 375. Bugün bizim “gölgelerimiz” neler olabilir — ekranlar, alışkanlıklar, önyargılar?','Plato, The Republic, around 375 BC. What might our “shadows” be today — screens, habits, assumptions?','#2c2418','#080604',gap=6.5,d=56),
  photo('karagoz','Karagöz gölge oyunu · Shadow play','Karagöz, Hacivat ve Tiryaki — perdenin arkasında ışıkla canlanan deri tasvirler','Karagöz, Hacivat and Tiryaki — leather figures brought to life by light behind a screen','Tasvirler deve derisinden kesilip boyanır ve ışık geçsin diye inceltilir; seyirci yalnızca perdedeki renkli gölgeleri görür — tıpkı Platon’un mağarasındaki gibi','The figures are cut from camel hide, dyed and scraped thin so light shines through — the audience sees only coloured shadows, just like in Plato’s cave',fit='contain',d=40),
  steps(TE,'Deneyim Makinesi: istediğin her hayatı yaşatan bir makineye bağlanır mıydın?','The Experience Machine: would you plug into a machine that lets you live any life you want?',
    [['Bağlandığında istediğin hayatı yaşıyormuş gibi hissediyorsun','Once plugged in, you feel you are living whatever life you wish','🎧'],['Dünya turu, büyük başarılar, kusursuz günler — hepsi gerçek gibi','World travel, great achievements, perfect days — all feel real',''],['Ama hiçbiri gerçekten olmuyor; sen bir koltukta uzanıyorsun','But none of it is really happening — you are lying in a chair',''],['Ömür boyu bağlanır mıydın?','Would you plug in for life?','?']],
    'Robert Nozick, 1974: çoğu insan “hayır” diyor. Demek ki yalnızca iyi hissetmek değil, gerçekten yaşamak ve yapmak istiyoruz','Robert Nozick, 1974: most people say “no” — so we want not just to feel good, but to really live and do things','#1c2430','#04060a',gap=6.5,d=54),
  photo('catbox','Kutudaki kediler · Cats in boxes','Kutuya sığmayı seven kediler','Cats who love to squeeze into boxes','Bir araştırmaya göre barınaktaki kediler, saklanabilecekleri bir kutu verildiğinde yeni ortama çok daha çabuk alışıyor (Utrecht Üniversitesi, 2014)','One study found shelter cats given a box to hide in settled into their new home much faster (Utrecht University, 2014)',d=38),
  steps(TE,'Sonsuz Tekrar: bugünü sonsuza dek yeniden yaşayacak olsaydın…','Eternal recurrence: if you had to live today again, forever…',
    [['Biri sana şöyle diyor:','Someone tells you:',''],['“Bu hayatı, her ayrıntısıyla, sayısız kez yeniden yaşayacaksın”','“You will live this life again, in every detail, countless times”',''],['Bu haber seni sevindirir mi, korkutur mu?','Would that news delight you or frighten you?',''],['Cevabın, bugün neyi değiştirmek istediğini söyler','Your answer tells you what you would like to change today','↻']],
    'Friedrich Nietzsche, 1882. Aynı fikir 1993’te “Bugün Aslında Dündü” (Groundhog Day) filminde de oynanır','Friedrich Nietzsche, 1882 — the same idea plays out in the 1993 film Groundhog Day','#22301f','#050805',gap=6.5,d=50),
  rid('Bir adam bir fotoğrafa bakıp diyor:<br>“Kardeşim yok; ama bu adamın babası<br>babamın oğlu.” Fotoğraftaki kim?','A man looks at a photo and says: “I have no brothers, but this man’s father is my father’s son.” Who is in the photo?','Kendi oğlu! “Babamın oğlu” kendisi','His own son — “my father’s son” is himself',sec=24,d=40,c1='#2a2420',c2='#070605'),
]),
S(14,15,'Villa Fikirleri: Butik Otel Ayrıntıları · Villa Ideas: Boutique-Hotel Details',[
  villa('stepping','Portland Japon Bahçesi, ABD · Portland Japanese Garden, USA','Yosunun üstünde basamak taşları ve bir taş fener: insanı yavaşlatan bir yol','Stepping stones on moss and a stone lantern — a path that slows you down','Japon bahçelerinde basamak taşları (tobi-ishi) bilerek biraz düzensiz dizilir: misafir adımına bakar, yavaşlar, etrafı görür. Villa için: kapıdan terasa birkaç büyük, düz taş yeter','In Japanese gardens stepping stones (tobi-ishi) are set slightly irregular on purpose — guests watch their step, slow down and look around. For the villa: a few large flat stones from the door to the terrace are enough',fit='contain'),
  villa('bathtub','Amantaka, Luang Prabang, Laos','Pencerelerin önünde duran ayaklı bir küvet — bir butik otel süitinden','A freestanding tub in front of the windows — from a boutique-hotel suite','Butik otellerin sevilen ayrıntısı: küveti duvara gömmek yerine ışığın ve manzaranın önüne koymak. Villada deniz tarafındaki bir süite çok yakışır','A favourite boutique-hotel touch: set the tub in front of the light and the view instead of against a wall. It would suit a sea-facing suite at the villa'),
  villa('porchswing','St. Louis, ABD · USA','Verandada bir salıncak: akşam çayının en sevilen köşesi','A porch swing — the favourite spot for evening tea','Tavana asılı ahşap bir salıncak terasın en çok kullanılan yeri olur. Trabzon kışında minderleri ve battaniyeyi içeri almak yeter','A wooden swing hung from the ceiling becomes the most-used spot on a terrace — in Trabzon winters just bring the cushions and blankets inside'),
  steps('Villa Fikri · Villa Idea','Akşam hizmeti (turndown): misafir odasına döndüğünde…','Turndown service — when guests return to their room…',
    [['Perdeler kapanmış, yalnızca başucu lambası yanıyor','Curtains drawn, only the bedside lamp on','🛏'],['Yastığın yanında küçük bir lokum ya da fındık ezmesi','A little lokum or hazelnut treat beside the pillow',''],['Ertesi günün havasını ve gün doğumu saatini yazan el yazısı bir kart','A handwritten card with tomorrow’s weather and sunrise time','✎'],['Yatağın yanında bir sürahi su ve terlikler','A carafe of water and slippers by the bed','']],
    'Pahalı değil — ama misafirin “beni düşünmüşler” dediği küçük bir ritüel','Not expensive — but a small ritual that makes guests feel “they thought of me”','#2a2418','#080604',gap=7,d=50),
  fact('1984','“Butik otel” deyimi, 1984’te New York’ta açılan Morgans Hotel için kullanıldı: dev bir zincir değil, küçük, kişisel ve özenle tasarlanmış','The phrase “boutique hotel” was coined for the Morgans Hotel, opened in New York in 1984 — not a giant chain, but small, personal and carefully designed','Kurucuları Steve Rubell ve Ian Schrager: “büyük mağaza değil, bir butik gibi” · Founders Steve Rubell & Ian Schrager: “like a boutique, not a department store”','#173032','#030809',d=30),
]),
S(15,16,'Göz Oyunları · Tricks of the Eye',[
  g('hzshepard',d=52),
  guess('wingscales','Makro · Macro','Bu ne? Çok, çok yakından çekildi…','What is this? It was photographed very, very close up…','Bir tavus kelebeğinin kanadındaki “göz” deseni! Kiremit gibi dizilmiş minicik pullardan oluşuyor; kuşları korkutmak için bir baykuş gözünü andırır','The “eyespot” on a peacock butterfly’s wing — made of tiny scales laid like roof tiles. It looks like an owl’s eye to scare off birds',hint='İpucu: uçar · Hint: it flies',sec=22),
  g('hzbezold',d=50),
  fact('≈1 milyon','İnsan gözü tahminen bir milyon kadar renk tonunu ayırt edebilir — hem de yalnızca üç tür koni hücresiyle','The human eye can tell apart roughly a million shades of colour — with just three kinds of cone cells','Kırmızıya, yeşile ve maviye duyarlı koniler · Cones tuned to red, green and blue light','#2a1f2a','#070507',d=30),
  rid('Gözlerin kapalıyken bile<br>görebildiğin şey nedir?','What can you see even with your eyes closed?','Rüya!','A dream.',sec=16,c1='#1c2434',c2='#04060a'),
]),
S(16,17,'Ölçek Yolculuğu: Uzay ve Zaman · Scale Journey: Space & Time',[
  g('hzorrery',d=60),
  steps('Ölçek Yolculuğu · Scale Journey','Bir milyon, bir milyar, bir trilyon… saniye olarak ne kadar?','A million, a billion, a trillion… how long in seconds?',
    [['1 milyon saniye ≈ 11,5 gün','1 million seconds ≈ 11.5 days','⏱'],['1 milyar saniye ≈ 31,7 yıl','1 billion seconds ≈ 31.7 years',''],['1 trilyon saniye ≈ 31.700 yıl — en eski mağara resimleri kadar geriye','1 trillion seconds ≈ 31,700 years — back to the age of the oldest cave paintings','∞']],
    'Milyon ile milyar arasındaki fark, iki hafta ile bir ömrün yarısı arasındaki fark kadar','The gap between a million and a billion is the gap between two weeks and half a lifetime','#141c2a','#03050a',gap=7,d=46),
  photo('sdo','NASA SDO · 31 Ağustos 2012','Güneş’ten fırlayan dev bir plazma bulutu (koronal kütle atımı)','A giant cloud of plasma erupting from the Sun (a coronal mass ejection)','Bu bulut uzaya saniyede 1.400 km’den hızlı fırladı; üç gün sonra Dünya’da kutup ışıklarına yol açtı','It shot into space at more than 1,400 km per second — three days later it set off auroras on Earth',d=38),
  photo('dscovr','NASA DSCOVR · Temmuz 2015','Ay, Dünya’nın önünden geçerken — bize hiç göstermediği yüzüyle','The Moon crossing in front of the Earth — showing the face we never see','1,5 milyon km uzaktaki DSCOVR uydusu çekti. Ay’ın uzak yüzünde, bize bakan yüzündeki koyu “denizler” neredeyse hiç yok','Taken by the DSCOVR satellite 1.5 million km away — the far side of the Moon has almost none of the dark “seas” of the side we know',fit='contain',d=40),
  fact('1','Neptün 1846’da keşfedildi ve Güneş’in çevresindeki ilk tam turunu ancak 2011’de tamamladı','Neptune was discovered in 1846 and finished its first full orbit since then only in 2011','Bir Neptün yılı ≈ 165 Dünya yılı · One Neptune year ≈ 165 Earth years','#131c32','#03050b',d=30),
]),
S(17,18,'Işığın Oyunları · Tricks of Light',[
  photo('sundog','Brofjorden, İsveç · Sweden','Güneşin yanında ikinci bir “güneş”: güneş köpeği (parhelion)','A second “sun” beside the Sun: a sun dog (parhelion)','Havadaki altıgen, yassı buz kristalleri ışığı yaklaşık 22° kırar; güneşin iki yanında parlak lekeler belirir','Flat hexagonal ice crystals in the air bend sunlight by about 22° — bright spots appear on either side of the Sun',d=38),
  photo('halo','22° hale · 22° halo','Güneşin çevresinde kusursuz bir halka: 22 derecelik hale','A perfect ring around the Sun: the 22° halo','Kolunu uzatıp elini açınca serçe parmağından başparmağına kadar yaklaşık 22° eder — halenin yarıçapı tam o kadar','Stretch out your arm and spread your hand: thumb to little finger is about 22° — exactly the halo’s radius',fit='contain',d=38),
  photo('glory','Golden Gate, San Francisco','Kendi gölgenin çevresinde renkli bir halka: Brocken tayfı ve “glory”','A coloured ring around your own shadow: the Brocken spectre and glory','Arkanda güneş, önünde sis varken gölgen sise düşer ve başının çevresinde renkli halkalar belirir. Yanındaki kişi yalnızca kendi halkasını görür','With the Sun behind you and fog ahead, your shadow falls on the fog with coloured rings round your head — the person next to you sees only their own',fit='contain',d=40),
  photo('greenflash','Yeşil şimşek · Green flash','Güneş batarken son anda beliren yeşil ışık — kare kare','The green light that appears at the very last moment of sunset — frame by frame','Atmosfer bir prizma gibi davranır: Güneş’in son kenarı bir iki saniyeliğine yeşil görünür. Karadeniz’in açık ufkunda, berrak bir akşamda yakalanabilir','The atmosphere acts like a prism — the Sun’s last sliver turns green for a second or two. Watch for it over the open Black Sea horizon on a clear evening',fit='contain',d=40),
  photo('pillars','Stockholm, İsveç · Sweden','Soğuk bir kış gecesinde gökyüzüne yükselen ışık sütunları','Pillars of light rising into the sky on a cold winter night','Havada asılı yassı buz kristalleri yerdeki lambaların ışığını küçük aynalar gibi yansıtıp dikey sütunlar çizer','Flat ice crystals floating in the air reflect street lights like tiny mirrors, drawing tall vertical columns',d=38),
  photo('circumhorizontal','Rennes, Fransa · France','Bulutta yatay bir gökkuşağı: ufka paralel yay','A horizontal rainbow in a cloud: the circumhorizontal arc','Yalnızca Güneş ufkun 58° üzerine çıktığında oluşur; Trabzon’un enleminde bu ancak ilkbahar ve yaz öğlelerinde olur','It forms only when the Sun is more than 58° high — at Trabzon’s latitude that happens only around midday in spring and summer',fit='contain',d=38),
]),
S(18,19,'Trabzon’un Hikâyeleri · Stories of Trabzon',[
  photo('kostaki','Ortahisar, Trabzon','Kostaki Konağı — bugün Trabzon Müzesi','The Kostaki Mansion — today the Trabzon Museum','20. yüzyılın başında banker Kostaki Teofilaktos için yapıldı; Atatürk 1924’teki Trabzon ziyaretinde bu konakta kaldı','Built in the early 20th century for the banker Kostaki Theophylaktos — Atatürk stayed here on his 1924 visit to Trabzon',d=40),
  photo('gulbahar','Ortahisar, Trabzon','Gülbahar Hatun Camii’nin içi — 1514','Inside the Gülbahar Hatun Mosque — 1514','Trabzon’da şehzadeyken yaşayan Yavuz Sultan Selim, annesi Gülbahar Hatun’un anısına yaptırdı','Built by Selim I, who lived in Trabzon as a young prince, in memory of his mother Gülbahar Hatun',fit='contain',d=38),
  photo('zagnos','Ortahisar, Trabzon','Zağnos Köprüsü ve vadisi — eski surların dibinde bir park','The Zağnos bridge and valley — a park at the foot of the old walls','Vadi bir zamanlar surların doğal hendeğiydi; bugün yürüyüş yolları ve çay bahçeleriyle bir şehir parkı','The valley was once the walls’ natural moat — today it is a city park with walking paths and tea gardens',d=38),
  photo('theoskepastos','Boztepe yamacı, Trabzon','Kızlar Manastırı — kayaya yaslanan 14. yüzyıldan bir manastır','Kızlar Monastery — a 14th-century monastery leaning on the rock','Eski adı Panagia Theoskepastos: “Tanrı’nın örttüğü Meryem”. Bir mağara kilisenin çevresine kurulmuş','Its old name is Panagia Theoskepastos, “the Virgin sheltered by God” — built around a cave church',d=38),
  fact('Tebriz','19. yüzyılda İran’ın Avrupa ile ticaretinin büyük bölümü Trabzon limanından, Zigana Geçidi üzerinden Tebriz’e giden kervan yolundan geçerdi','In the 19th century much of Iran’s trade with Europe passed through Trabzon harbour, on the caravan road over the Zigana Pass to Tabriz','Trabzon–Erzurum–Tebriz yolu · The Trabzon–Erzurum–Tabriz road','#2a2418','#080604',d=30),
]),
S(19,20,'Galeri: Aynı Yer, Farklı Işık · Gallery: Same Place, Different Light',[
  art('haystack1','Saman Yığınları, Yaz Sonu — Claude Monet, 1891','Haystacks, End of Summer — Claude Monet, 1891','Monet evinin yakınındaki tarlada aynı saman yığınlarını 25’ten fazla kez boyadı; asıl konusu yığınlar değil, ışıktı','Monet painted the same haystacks near his house more than 25 times — his real subject was not the stacks but the light'),
  art('haystack2','Saman Yığınları, Kar Etkisi — Claude Monet, 1891','Haystacks, Snow Effect — Claude Monet, 1891','Işık o kadar hızlı değişiyordu ki tarlaya birçok tuval taşır, güneş döndükçe tuval değiştirirdi','The light changed so fast that he carried several canvases into the field and switched as the sun moved'),
  art('rouen1','Rouen Katedrali, Batı Cephesi, Güneş Işığı — Claude Monet, 1894','Rouen Cathedral, West Façade, Sunlight — Claude Monet, 1894','Katedralin tam karşısında bir oda kiralayıp aynı cepheyi 30’dan fazla kez boyadı','He rented a room right opposite the cathedral and painted the same façade more than 30 times'),
  art('rouen2','Rouen Katedrali, Sabah Etkisi — Claude Monet, 1894','Rouen Cathedral, Morning Effect — Claude Monet, 1894','Aynı taş: sabah serin bir mavi, öğleden sonra sıcak ve parlak — ışık taşı bambaşka bir malzemeye çeviriyor','The same stone — cool blue in the morning, warm and bright in the afternoon. Light turns it into a different material'),
  art('parliament','Londra Parlamentosu, Gün Batımı — Claude Monet, 1903','The Houses of Parliament, Sunset — Claude Monet, 1903','Monet Londra sisini çok severdi; Thames’in karşı kıyısındaki St Thomas Hastanesi’nin terasından boyadı','Monet loved London fog — he painted this from a terrace of St Thomas’ Hospital across the Thames'),
  steps('Küçük Meydan Okuma · Little Challenge','Monet gibi bak: yarın pencereden aynı manzaraya üç kez bak','Look like Monet: tomorrow, look at the same view from a window three times',
    [['Sabah: renkler serin mi, sıcak mı?','Morning: are the colours cool or warm?','☀'],['Öğle: gölgeler nerede kısalıyor?','Noon: where do the shadows get short?',''],['Akşam: deniz hangi renge dönüyor?','Evening: what colour does the sea turn?','☾']],
    'Aynı yerden üç fotoğraf çekip yan yana koy — aynı manzara, üç farklı tablo','Take three photos from the same spot and put them side by side — one view, three different paintings','#262019','#070605',gap=8,d=46),
]),
S(20,21,'Anadolu’dan Dâhiler · Genius Machines',[
  art('elephantclock','Fil Saati — el-Cezerî’nin kitabından bir sayfa','The Elephant Clock — a page from al-Jazari’s book','Adını doğduğu Cizre’den alan Cezerî, 1206’da Diyarbakır’daki Artuklu sarayında “Olağanüstü Mekanik Araçların Bilgisi” kitabını tamamladı; fil saatinde farklı kültürlerden figürler bir arada','Named after his birthplace Cizre, al-Jazari finished his “Book of Knowledge of Ingenious Mechanical Devices” in 1206 at the Artuqid court in Diyarbakır — the elephant clock combines figures from many cultures'),
  steps(CT,'Fil saati nasıl çalışır? Suyla ölçülen yarım saat','How does the elephant clock work? Half an hour measured by water',
    [['Filin karnındaki su tankında, dibi delik bir kâse yüzer','Inside the elephant’s belly a bowl with a small hole floats in a tank of water','💧'],['Kâse yavaş yavaş dolar ve yarım saatte batar','It slowly fills and sinks in half an hour',''],['Batarken iplere asılı düzeneği çeker: bir top düşer, kuş öter, davul çalar','As it sinks it pulls cords — a ball drops, a bird whistles, a drum beats',''],['Kâse yeniden yukarı çekilir ve her şey baştan başlar','The bowl is pulled back up and it all begins again','↻']],
    'Kendi kendini yeniden kuran bu düzenek, bugünkü otomasyonun 800 yıllık atalarından biri','A machine that resets itself — one of the 800-year-old ancestors of today’s automation','#173032','#030809',gap=6.5,d=52),
  art('takiyuddin','Takiyüddin ve gökbilimciler, İstanbul Rasathanesi — Şehinşahname minyatürü, 1581','Taqi al-Din and his astronomers at the Istanbul Observatory — miniature from the Shahanshahnama, 1581','1577’de Galata’da kurulan rasathane, zamanının en gelişmiş gözlemevlerinden biriydi; Takiyüddin gözlemlerde mekanik saat kullanan ilk gökbilimcilerdendi','Founded in Galata in 1577, it was one of the most advanced observatories of its day — Taqi al-Din was among the first astronomers to use mechanical clocks for observations'),
  fact('Robot','“Robot” kelimesi 1920’de Çek yazar Karel Čapek’in bir tiyatro oyununda doğdu; Çekçe “robota”, yani angarya, zorunlu iş','The word “robot” was born in 1920 in a play by Czech writer Karel Čapek — from the Czech “robota”, forced labour','Oyunun adı: R.U.R. · The play: R.U.R.','#1c2026','#040506',d=30),
  rid('Kumdan yapılır, kumla çalışır<br>ve zamanı söyler. Nedir?','It is made from sand, runs on sand and tells the time. What is it?','Kum saati! Camı da kumdan yapılır','An hourglass — even its glass is made from sand',sec=16,c1='#2a2420',c2='#070605'),
]),
S(21,22,'Kelimelerin Yolculuğu · Journeys of Words',[
  photo('bagdatkosku','Topkapı Sarayı, İstanbul','Bağdat Köşkü — İngilizcedeki “kiosk” kelimesi Türkçe “köşk”ten geliyor','The Baghdad Kiosk — the English word “kiosk” comes from the Turkish “köşk”','Kelime Farsçadan Türkçeye, oradan Fransızcaya ve İngilizceye geçti: önce bahçe köşkü, sonra gazete büfesi. Bağdat Köşkü 1639’da Bağdat seferinin anısına yapıldı','The word travelled from Persian to Turkish, then to French and English — first a garden pavilion, later a newsstand. The Baghdad Kiosk was built in 1639 to mark the Baghdad campaign',d=40),
  photo('yogurt','Cacık','Yoğurtla yapılan cacık — “yoğurt” bugün onlarca dilde neredeyse aynı söyleniyor','Cacık, made with yoghurt — “yoğurt” sounds almost the same in dozens of languages today','Kelime Türkçe “yoğurmak” ile ilgili: koyulaştırmak. İngilizcede yogurt, Fransızcada yaourt','The word is linked to the Turkish “yoğurmak”, to thicken — yogurt in English, yaourt in French',d=36),
  steps('Kelimelerin Yolculuğu · Journeys of Words','“Divan” kelimesinin şaşırtıcı yolculuğu','The surprising journey of the word “divan”',
    [['Farsça “dīvān”: kayıt defteri, liste','Persian “dīvān”: a register, a list','📜'],['Sonra devlet meclisi: Divan-ı Hümayun','Then a council of state: the Imperial Divan',''],['Meclis odasındaki duvar boyu minderli sedirler → Avrupa’da “divan”: kanepe','The long cushioned benches of that council room → the “divan” sofa in Europe','🛋'],['Gümrük de buradan gelir: Fransızca douane, İtalyanca dogana','Customs comes from it too: French douane, Italian dogana','']],
    'Bir şiir kitabına da “divan” denir — tek kelime, dört ayrı dünya','A book of poems is also a “divan” — one word, four different worlds','#2a2418','#080604',gap=6.5,d=50),
  fact('Ordu','İngilizcedeki “horde” (kalabalık, sürü) kelimesi Türkçe “ordu”dan gelir; Lehçe “horda” üzerinden geçti','The English word “horde” comes from the Turkic “ordu” (army, camp) — by way of the Polish “horda”','Kelimeler de göç eder · Words migrate too','#1c2430','#04060a',d=30),
  rid('Hangisi tersten okununca da aynıdır:<br>“kabak” mı, “kavun” mu?','Which Turkish word reads the same backwards: “kabak” (courgette) or “kavun” (melon)?','Kabak! Böyle kelimelere palindrom denir','Kabak — words like that are called palindromes',sec=16,c1='#22301f',c2='#050805'),
  q('Kendini küçük görme;|sen coşkuyla dönen bir evrensin','Stop acting so small — you are the universe in ecstatic motion','night',d=44),
]),
S(22,23,'Kasım Gecesi: Leonidler · November Night: The Leonids (sakin · calm)',[
  photo('meteor','Gece gökyüzü · Night sky','Gecenin içinde aynı anda iki yıldız kayması','Two shooting stars at the same moment','Bu gece ve yarın gece (17–18 Kasım) Leonid yağmurunun en yoğun zamanı; ışıklardan uzakta, gece yarısından sonra doğuya bak','Tonight and tomorrow night (17–18 November) the Leonid shower peaks — away from lights, look east after midnight',fit='contain',d=42),
  q('Herkes belli bir iş için yaratıldı;|o işin arzusu her kalbe konuldu','Everyone has been made for some particular work, and the desire for that work has been put in every heart','night',d=46),
  photo('leonids','Kitt Peak, ABD · USA · 1966','1966 Leonid fırtınası: dört fotoğraf karesinde yağan yıldızlar','The 1966 Leonid storm — shooting stars raining across four frames','Leonidler, 33 yılda bir dönen Tempel–Tuttle kuyruklu yıldızının bıraktığı tozdan gelir. 1966’da saatte 100.000’den fazla yıldız kaydığı tahmin ediliyor','The Leonids come from dust left by comet Tempel–Tuttle, which returns every 33 years — in 1966 more than 100,000 meteors an hour are thought to have fallen',fit='contain',d=42),
  fact('71 km/s','Leonid meteorları atmosfere saniyede yaklaşık 71 km hızla girer — en hızlı yıldız kaymalarından','Leonid meteors hit the atmosphere at about 71 km per second — among the fastest shooting stars','Tanelerin çoğu bir kum tanesinden küçüktür · Most grains are smaller than a grain of sand','#10202a','#020507',d=32),
  steps('Sakin Düşünce · Calm Thought','Yıldız kayması izlemek için dört sakin adım','Four calm steps for watching shooting stars',
    [['Sıcak giyin, bir battaniye al','Dress warm and bring a blanket','🧣'],['Işıkları söndür, ekrana bakma','Turn off the lights, keep away from screens',''],['Gözlerin karanlığa alışsın: yaklaşık 20 dakika','Let your eyes adjust to the dark — about 20 minutes',''],['Tek bir noktaya değil, gökyüzünün genişliğine bak','Look at the whole wide sky, not one spot','✧']],
    'Ve bir dilek tutmayı unutma','And don’t forget to make a wish','#0e1624','#020306',gap=7.5,d=48,bg='stars'),
]),
S(23,26,'Fener Işığı · Lighthouse Light (sakin · calm)',[
  g('hzfener',d=80),
  q('Gün doğmadan|neler doğar','Before the sun rises, so much is born','sea',d=46,lb='Atasözü · Turkish Proverb',by='Türk atasözü · Turkish proverb'),
  photo('dormouse','Fındık faresi · Hazel dormouse','Kış uykusuna hazırlanan bir fındık faresi','A hazel dormouse getting ready for its winter sleep','Adını fındığa olan düşkünlüğünden alır; ekimden nisana kadar, yılın yarısından fazlasını uyuyarak geçirebilir','Named for its love of hazelnuts — it can sleep from October to April, more than half the year',d=42),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: yarına küçük bir hediye','Before sleep: a small gift for tomorrow',
    [['Yarın seni gülümsetecek tek bir küçük şey seç','Choose one small thing that will make you smile tomorrow','☾'],['Sabahın ilk çayını nerede içeceğini düşün','Think where you will drink the first tea of the morning',''],['Bugünden teşekkür ettiğin bir anı hatırla','Remember one moment from today you are grateful for','']],
    'İyi geceler','Good night','#0e1624','#020306',gap=8,d=46,bg='stars'),
  fact('MÖ 3. yy','Dünyanın en ünlü ilk deniz feneri İskenderiye Feneri’ydi; yüksekliğinin 100 metreyi aştığı düşünülüyor','The world’s first famous lighthouse was the Pharos of Alexandria — thought to have stood more than 100 m tall','Antik dünyanın yedi harikasından biri · One of the Seven Wonders of the Ancient World','#0c1a26','#020406',d=32),
]),
]
json.dump(dict(date=DATE,rev=REV,_note='Hourly sets for the villa TV. Built by days/build_2026-11-16.py. Content log: used-content.md',sets=sets),open('/workspace/tv-pages/days/%s.json'%DATE,'w'),ensure_ascii=False,indent=1)
print(len(sets),sum(len(s['items']) for s in sets))
for s in sets: print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name'])
