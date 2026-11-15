# Rebuilds evening sets (18:00-02:00) of days/2026-11-15.json for a calm night alone.
# Keeps the morning/afternoon sets (09:00-18:00) from the 08:00 build.
import json, os
DATE='2026-11-15'; REV=65; NEXT='2026-11-16'
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-15.json')))
FIX={
    'Didier Descouens':'Jean-Baptiste-Camille Corot',
    'Dosseman':'Şeker Ahmed Paşa',
    'GlacierNPS':'Glacier National Park Service',
    'YellowstoneNPS':'Yellowstone National Park Service',
    'Jacob W. Frank, National Park Service':'Jacob W. Frank (NPS)',
    'Hamdigumus':'Hamdigumus',
    'Dreamy Pixel':'Dreamy Pixel',
    'Ahmet Gokhan Kara':'Ahmet Gökhan Kara',
    'Kadir KARA':'Kadir Kara',
    'Merve ÇELİK':'Merve Çelik',
}
def artist(k):
    a=C[k]['artist']
    for f,t in FIX.items():
        if a==f or a.startswith(f): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k): return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace(' rs','')
def cr(k): return 'Foto · Photo: %s · %s · Wikimedia Commons'%(artist(k),lic(k))
REAL='Gerçek Fotoğraf · Real Photo'
def photo(k,tag,tr,en,fact=None,facte=None,fit=None,d=40,pos=None):
    it=dict(k='hzphoto',d=d,f='m/h15-%s.jpg'%k,lb=REAL+' · '+tag,tr=tr,en=en,cr=cr(k))
    if fact: it.update(fact=fact,facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it
def art(k,tr,en,fact,facte,d=44,extra_cr=None):
    it=photo(k,'',tr,en,fact,facte,fit='contain',d=d)
    it['lb']='Gerçek Eser · Real Artwork'
    who=artist(k)
    if extra_cr:
        it['cr']=extra_cr
    else:
        it['cr']='Eser · Artwork: %s · kamu malı · public domain · Wikimedia Commons'%who
    return it
def q(tr,en,pal,d=46): return dict(k='hzquote',d=d,tr=tr,en=en,pal=pal)
def fact(big,tr,en,src,c1,c2,d=30): return dict(k='hzfact',d=d,big=big,tr=tr,en=en,src=src,c1=c1,c2=c2)
def steps(lb,qq,e,st,fin,fine,c1,c2,gap=6,d=56,bg=None):
    it=dict(k='hzsteps',d=d,lb=lb,q=qq,e=e,c1=c1,c2=c2,gap=gap,steps=st,fin=fin,fine=fine)
    if bg: it['bg']=bg
    return it
def S(h1,h2,name,items):
    f='%sT%02d:00'%(DATE,h1); u=('%sT%02d:00'%(DATE,h2)) if h2<=23 else '%sT%02d:00'%(NEXT,h2-24)
    return dict(id='h-%s-%02d'%(DATE[5:],h1),name=name,**{'from':f,'until':u},items=items)

# Şeker Ahmed Paşa: painting is PD; the museum photo is CC BY-SA 4.0 (Dosseman)
SEKER_CR='Eser · Artwork: Şeker Ahmed Paşa · kamu malı · public domain; Foto · Photo: Dosseman · CC BY-SA 4.0 · Wikimedia Commons'

evening=[
S(18,19,'Karadeniz’in Huzuru · Black Sea Peace',[
  photo('zilkale','Zilkale · Çamlıhemşin, Rize','Zilkale — Fırtına Vadisi’nin sisli yamaçlarında bir kale','Zilkale — a castle on the misty slopes of the Fırtına valley','14. ya da 15. yüzyıldan; Fırtına Deresi’ne bakan bir kayanın üstünde, yaklaşık 750 metre yükseklikte','From the 14th or 15th century — on a rock above the Fırtına river, about 750 metres up',d=42),
  q('Ben gelmedim dava için;|benim işim sevi için','I did not come to quarrel; my work is love','sea',d=46),
  photo('unyesea','Ünye, Ordu · Çamlık sahili','Sisli bir günde Karadeniz — Ünye kıyısındaki kayalıklar','The Black Sea on a misty day — the rocks of the Çamlık shore in Ünye','Kıyıdaki çamlar ve kayalar, Karadeniz’in sık sık takındığı bu yumuşak griye çok yakışır','The pines and rocks along the shore belong to this soft grey the Black Sea often wears',d=42),
  photo('cagrankaya','Çağrankaya Yaylası · Hayrat, Trabzon','Çağrankaya Yaylası — bulut denizi yaylanın hemen altında','Çağrankaya plateau — a sea of cloud just below the highland','Hayrat ilçesinde, Trabzon’un doğu yaylalarından; açık bir günde sisin altındaki vadiler ta uzağa kadar görünür','In Hayrat, among Trabzon’s eastern highlands — on a clear day the valleys below the mist run all the way to the far horizon',d=42),
  fact('Sis','Doğu Karadeniz yaylalarında, vadideki soğuk hava sıkışınca sis bir deniz gibi yaylaların altında kalır','In the eastern Black Sea highlands, when cold air sits in the valleys, the mist lies like a sea below the yaylas','Bu görüntüye “bulut denizi” denir · This is called a “sea of clouds”','#15202c','#030508',d=30),
]),
S(19,20,'Sisli Yaylalar · Misty Highlands',[
  photo('elevit','Elevit Yaylası · Çamlıhemşin, Rize','Elevit — sisin sarıp sarmaladığı ahşap yayla evleri','Elevit — wooden highland houses wrapped in mist','Çamlıhemşin’in yüksek yaylalarından; yazın yaylacılar burada kalır, sis vadiden her an yükselebilir','One of Çamlıhemşin’s high plateaus — herders stay here in summer, and the mist can rise from the valley at any moment',d=42),
  photo('cagfire','Aşağı Çağrankaya · Hayrat, Trabzon','Yayla çiçeklerinin ardından, vadiyi dolduran bir sis denizi','Beyond the highland flowers, a sea of mist filling the valley','Öndeki mor çiçekler yakıotu; yaz sonuna doğru Karadeniz yaylalarının kenarlarında açar','The purple flowers in front are fireweed — they bloom along the edges of Black Sea yaylas towards the end of summer',d=42),
  q('Kanaat, tükenmez|bir hazinedir','Contentment is a treasure that never runs out','clay',d=46),
  photo('elevitpine','Elevit Yaylası · Çamlıhemşin','Sisin içinden çıkan ladinler','Spruce trees stepping out of the mist','Yaylanın yamaçları ladin ve çam ormanıyla kaplıdır; sis evlerin hemen üstüne kadar iner','The slopes are clothed in spruce and pine — the mist comes down to just above the houses',d=42),
  photo('elevitmist','Elevit Yaylası · Çamlıhemşin','Sisin içinde tek başına duran bir yayla evi','A single highland house standing in the mist','Yağmurlu bir günde yayla sessizleşir; yalnızca çayır ve bulut kalır','On a rainy day the yayla grows quiet — only meadow and cloud are left',d=42),
  fact('Yayla','Karadeniz’de “yayla”, yazın hayvanlarla çıkılan yüksek, serin çayır demektir','In the Black Sea, a “yayla” is a high, cool meadow that people go up to in summer with their animals','Kışın evler kapanır; baharda yol yeniden açılır · In winter the houses are shut; in spring the road opens again','#1a2420','#040605',d=30),
]),
S(20,21,'Galeri: Sakin Fırçalar · Gallery: Quiet Brushes',[
  art('aivazovsky','Sakin Deniz — Ivan Aivazovsky, 1887','Calm Sea — Ivan Aivazovsky, 1887','Aivazovsky Karadeniz kıyısında, Kefe’de doğdu; denizi hayatı boyunca yüzlerce tablosunda resmetti','Aivazovsky was born in Feodosia (Kefe) on the Black Sea — he painted the sea in hundreds of pictures over his lifetime'),
  art('corot','Ville-d’Avray Göleti — Jean-Baptiste-Camille Corot','The Pond at Ville-d’Avray — Jean-Baptiste-Camille Corot','Corot bu göletlerin kıyısında yaşadı; suları ve ağaçları defalarca, hep yumuşak bir ışıkla çizdi','Corot lived beside these ponds and painted their water and trees again and again, always in a soft light'),
  q('Yaratılanı hoş gör,|Yaradan’dan ötürü','Be kind to all that is created, for the sake of the Creator','ink',d=46),
  art('sisley','Sis, Voisins — Alfred Sisley, 1874','Fog, Voisins — Alfred Sisley, 1874','Sisley bu bahçeyi neredeyse tek bir renkle, mavimsi bir gümüşle boyadı; figür sisin içinde kayboluyor','Sisley painted this garden in almost a single colour — a bluish silver — and the figure disappears into the fog'),
  art('levitan','Alacakaranlık — İsaak Levitan, 1899','Twilight — Isaac Levitan, 1899','Levitan Rusya’nın sakin akşamlarını çok severdi; bu tabloda ay, bir samanlık ve bir çit yeter','Levitan loved Russia’s quiet evenings — here a moon, a barn and a fence are enough'),
  art('sekerahmet','Ankara Manzarası — Şeker Ahmed Paşa','Landscape of Ankara — Şeker Ahmed Paşa','Şeker Ahmed Paşa (1841–1907), Paris’te yetişmiş ilk Osmanlı manzara ressamlarındandır','Şeker Ahmed Paşa (1841–1907) was among the first Ottoman landscape painters trained in Paris',extra_cr=SEKER_CR),
]),
S(21,22,'Ayna Gibi · Like a Mirror',[
  photo('mcdonald','McDonald Gölü · Glacier, Montana','Stanton ve Vaught dağları, McDonald Gölü’nde bir ayna gibi','Mount Stanton and Mount Vaught, a mirror in Lake McDonald','Göl o kadar durgundur ki, dağın her çizgisi suda ikinci kez görünür','The lake is so still that every line of the mountain appears a second time in the water',d=42),
  q('Sular durulsun;|ayı ve yıldızları kendi içinde görürsün','Let the waters settle, and you will see the moon and the stars in yourself','sea',d=46),
  photo('karagol','Borçka Karagöl · Artvin','Borçka Karagöl — ormanın durgun, yeşil bir aynası','Borçka Karagöl — a still, green mirror of the forest','Artvin’de, kayın ve ladin ormanının içinde; adı, suyun koyu renginden gelir','In Artvin, inside a forest of beech and spruce — it is named for the dark colour of the water',d=42),
  photo('bohinj','Bohinj Gölü · Slovenya','Kış sabahı Bohinj Gölü — durgun suda dağların yansıması','Lake Bohinj on a winter morning — the mountains reflected in still water','Slovenya’nın en büyük gölü; rüzgâr yokken su, cam gibi gerilir','Slovenia’s largest lake — when there is no wind the water stretches like glass',d=42),
  photo('derwent','Derwent Water · İngiltere','Sakin bir akşam: Derwent Gölü’nün durulmuş suyu','A calm evening: the settled water of Derwent Water','İngiltere’nin Göl Bölgesi’nde; taşların gölün dibinde bile göründüğü kadar duru','In England’s Lake District — so clear you can see the stones on the bed of the lake',d=42),
  fact('Ayna','Dağ göllerinde “ayna saati” çoğu zaman şafaktan hemen sonradır: rüzgâr henüz uyanmamıştır','On mountain lakes the “mirror hour” is often just after dawn, before the wind has woken','Fotoğrafçıların en sevdiği kısa aralık · Photographers’ favourite brief window','#10202a','#020507',d=32),
]),
S(22,23,'Yıldızların Altında · Under the Stars',[
  photo('starlake','Glacier Milli Parkı · Montana','Yıldızlar ve bir dağın sessiz yansıması','The stars and the quiet reflection of a mountain','Su o kadar durgundur ki, gökyüzü gölün içinde ikinci bir gece olur','The water is so still that the sky becomes a second night inside the lake',d=44),
  q('Şükrü bir örtü gibi giy;|hayatının her köşesini besler','Wear gratitude like a cloak, and it will feed every corner of your life','night',d=46),
  photo('ogwen','Ogwen Gölü · Galler, İngiltere','Ogwen Gölü’nün üstünde Samanyolu','The Milky Way over Llyn Ogwen','Küçük bir göl, küçük bir kulübe ve bütün bir gökyüzü','A small lake, a small hut, and the whole of the sky',d=44),
  photo('madera','Madera Kanyonu · Arizona','Karanlık dağların üstünde uzanan Samanyolu','The Milky Way stretching above dark mountains','Işık kirliliği olmayınca gökyüzü, gündüz unuttuğumuz kadar kalabalıktır','With no light pollution, the sky is as crowded as we forget it is by day',d=44),
  fact('Orion','Kasım ortasında, akşamları doğu ufkundan yükselen avcı Orion, kış gökyüzünün kapısını açar','In mid-November the hunter Orion rises in the eastern evening sky — opening the door to the winter heavens','Kuşağı: üç parlak yıldız, yan yana · His belt: three bright stars, side by side','#0e1624','#020306',d=32),
]),
S(23,26,'Gönül Rahatlığı · A Quiet Heart',[
  photo('cabin','Yellowstone · Wyoming','Yıldızların altında, ışığı yanan küçük bir ev','A little house with its light on, under the stars','Ormanın sessizliğinde tek bir pencere yeter','In the quiet of the forest, a single window is enough',d=44),
  q('Bir fincan kahvenin|kırk yıl hatırı vardır','A cup of coffee is remembered for forty years','clay',d=46),
  steps('Sakin Düşünce · Calm Thought','Uyumadan önce: dört sakin düşünce','Before sleep: four quiet thoughts',
    [['Bugün birine iyi gelen bir ânın','A moment today that did someone good','♡'],['Buharı tüten duru bir çay','A clear glass of tea, still steaming',''],['Dışarıda, görünmeden duran deniz','The sea outside, there even when you cannot see it',''],['Yarın terasa vuracak ilk ışık','The first light that will touch the terrace tomorrow','☾']],
    'İyi geceler — sakin uykular','Good night — sleep gently','#0e1624','#020306',gap=7.5,d=50,bg='stars'),
  fact('Yunus','Yunus Emre, 13. ve 14. yüzyılda Anadolu’da yaşadı; şiirleri yedi yüzyıldır gönülden gönüle dolaşır','Yunus Emre lived in Anatolia in the 13th and 14th centuries — his poems have travelled from heart to heart for seven hundred years','“Benim işim sevi için” · “My work is love”','#0c1a26','#020406',d=32),
]),
]

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
keep=[s for s in day['sets'] if int(s['from'][11:13])<18]
assert [s['from'][11:13] for s in keep]==['09','10','11','12','13','14','15','16','17'], [s['from'] for s in keep]
day['sets']=keep+evening
day['rev']=REV
day['_note']='Hourly sets for the villa TV. Morning from days/build_2026-11-15.py; evening 18:00-02:00 rebuilt by days/build_2026-11-15_evening.py (rev 65, calm night). Content log: used-content.md'
out=os.path.join(HERE,'%s.json'%DATE)
json.dump(day,open(out,'w'),ensure_ascii=False,indent=1)
print('sets',len(day['sets']),'evening scenes',sum(len(s['items']) for s in evening))
for s in day['sets']:
    mark=' *' if int(s['from'][11:13])>=18 else ''
    print(s['id'],s['from'],s['until'],len(s['items']),sum(i['d'] for i in s['items']),s['name']+mark)
