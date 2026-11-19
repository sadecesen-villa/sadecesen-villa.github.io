# Rebuilds 17:00–19:00 of days/2026-11-19.json as a cozy rainy-afternoon set.
# M is in the living room alone, raining outside, loves the earth-and-rain smell.
# First pass: 17:00 (petrichor). 18:00–19:00 filled in a second pass.
# New photos: m/h72-*.jpg
import json, os
DATE='2026-11-19'; REV=72
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-19e.json')))

FIX={
    'Bilinmeyen (kamu malı) · Unknown (public domain)':'',
    'Photo by User:Wikimol':'Wikimol',
}
def artist(k):
    a=C[k].get('artist','')
    for f,t in FIX.items():
        if a.startswith(f): return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k):
    return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace('CC0','CC0 · kamu malı · public domain')
def cr(k):
    a=artist(k)
    if a:
        return 'Foto · Photo: %s · %s · Wikimedia Commons'%(a, lic(k))
    return 'kamu malı · public domain · Wikimedia Commons'
REAL='Gerçek Fotoğraf · Real Photo'

def photo(k, tag, tr, en, fact=None, facte=None, fit=None, d=46, pos=None, lb=None):
    it=dict(k='hzphoto', d=d, f='m/h72-%s.jpg'%k, lb=(lb or (REAL+((' · '+tag) if tag else ''))), tr=tr, en=en, cr=cr(k))
    if fact: it.update(fact=fact, facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it

def artwork(k, tag, tr, en, fact=None, facte=None, fit=None, d=46, pos=None):
    a=artist(k)
    crd='Eser · Artwork: %s · %s · Wikimedia Commons'%(a, lic(k)) if a else 'kamu malı · public domain · Wikimedia Commons'
    lb='Gerçek Eser · Real Artwork'+((' · '+tag) if tag else '')
    it=dict(k='hzphoto', d=d, f='m/h72-%s.jpg'%k, lb=lb, tr=tr, en=en, cr=crd)
    if fact: it.update(fact=fact, facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it

def steps(lb, q, e, st, fin, fine, c1, c2, gap=7, d=56, bg=None, start=5):
    it=dict(k='hzsteps', d=d, lb=lb, q=q, e=e, c1=c1, c2=c2, gap=gap, steps=st, fin=fin, fine=fine)
    if bg: it['bg']=bg
    if start!=5: it['start']=start
    return it

def fact(big, tr, en, src, c1, c2, d=32):
    return dict(k='hzfact', d=d, big=big, tr=tr, en=en, src=src, c1=c1, c2=c2)

def q(tr, en, pal, d=46, lb=None, by=None):
    it=dict(k='hzquote', d=d, tr=tr, en=en, pal=pal)
    if lb: it.update(lb=lb, by=by)
    return it

def S(frm, until, sid, name, items):
    return dict(id=sid, name=name, **{'from':frm,'until':until}, items=items)

# ---- 17:00 The smell of rain (petrichor) ----
H17=[
    photo('rainglass', '',
        'Camın ötesinde yağmur ve koyu ağaçlar — pencereden bakınca dünya yumuşuyor',
        'Rain and dark trees beyond the glass — looking out, the world softens',
        'Pencereyi açınca gelen o koku, ıslak toprak ve yağmurun karışımıdır',
        'The smell that comes when you open the window is wet earth mixed with rain',
        d=50, pos='50% 50%'),
    photo('rainwin', '',
        'Camdaki her damla küçük bir mercek: arkasındaki bahçeyi ters çevirip büyütüyor',
        'Each drop on the glass is a tiny lens, turning and magnifying the garden behind it',
        d=46, pos='50% 50%'),
    fact('petrichor',
        'Yağmurun toprağa düştüğü an yayılan o kokunun bilimsel adı: petrichor',
        'The scientific name for the smell that rises when rain hits the earth is petrichor',
        '1964’te Isabel Joy Bear ve Richard Thomas, Nature’da bu adı koydu · Bear and Thomas coined the word in Nature in 1964',
        '#1a2830','#05090c', d=34),
    photo('petrichor', 'yağmurun ıslattığı bir avlu · a rain-soaked courtyard',
        'Yağmur ıslak zemine çarpınca, toprakta ve taşta birikmiş yağlar havaya karışır',
        'When rain strikes the wet ground, oils held in the earth and on stone lift into the air',
        'Bu kokunun büyük kısmı geosmin’den gelir: topraktaki Streptomyces bakterilerinin yaptığı bir molekül',
        'Much of the scent is geosmin — a molecule made by Streptomyces bacteria in the soil',
        d=50, pos='50% 50%'),
    steps('Merak · Wonder',
        'Bu kokuyu neden bu kadar küçük miktarlarda bile duyarız?',
        'Why can we smell this even in the tiniest amounts?',
        [
            ['Geosmin, topraktaki bakterilerin ürettiği bir molekül', 'Geosmin is a molecule made by bacteria in the soil', ''],
            ['İnsan burnu onu trilyonda beş ila on parçada bile ayırt eder', 'The human nose can detect it at just five to ten parts per trillion', ''],
            ['Kuru dönemde bitkiler de toprağa yağ bırakır; yağmur bunları serbest bırakır', 'In dry spells plants also leave oils in the soil; rain sets them free', ''],
            ['Fırtınadan önceki keskin koku ise başka bir şeydir: yıldırımın yaptığı ozon', 'The sharp smell before a storm is something else: ozone made by lightning', ''],
        ],
        'Petrichor, yağmurun toprağa merhaba dediği andır — burnumuz buna evrimle ayarlıdır',
        'Petrichor is the moment rain greets the earth — our noses evolved to notice it',
        '#1a2830','#05090c', gap=7, d=58),
    photo('rainleaves', '',
        'Yaprakların üstünde duran damlalar neredeyse küre: onları bu biçimde tutan, yüzey gerilimidir',
        'The droplets resting on the leaves are almost spheres — surface tension holds them in that shape',
        d=46, pos='50% 45%'),
    q('Küçük, muttarid, muhteriz darbeler;|kafeslerde, camlarda pür-ihtizâz',
      'Small, steady, timid taps — trembling on the lattices and the windowpanes',
      'sea', d=46,
      lb='Tevfik Fikret, “Yağmur” · Tevfik Fikret, “Rain”',
      by='Tevfik Fikret (1867–1915)'),
]


# ---- 18:00 Black Sea rain, tea gardens, misty forest ----
H18=[
    photo('hemsin', 'Hemşin, Rize (Bilen köyü)',
        'Hemşin’in yeşil yamaçları — önde bir çay bahçesi, dağa yayılmış evler',
        'The green slopes of Hemşin — a tea garden in front, houses on the hillside',
        'Bu peyzaj, Doğu Karadeniz’e özgü: sık yağmur, yumuşak kış ve dik yamaçlarda çay',
        'This landscape belongs to the eastern Black Sea: frequent rain, mild winters and tea on steep hills',
        d=50, pos='50% 55%'),
    photo('pontic', 'Pontus Dağları · Pontic Mountains',
        'Pontus Dağları’nda çay bahçeleri: ağaçların arasında sıra sıra ekilmiş yeşil tarlalar',
        'Tea gardens in the Pontic Mountains — rows of green planted among the trees',
        d=46, pos='50% 45%'),
    photo('rize', 'Rize yakınlarında çay bahçeleri · tea gardens near Rize',
        'Rize yakınlarında çay tarlaları — yamaca basamak basamak işlenmiş yeşil',
        'Tea fields near Rize — green terraces stepped into the hillside',
        d=46, pos='50% 45%'),
    photo('mist2', 'Roruper Holz, Dülmen, Almanya · Germany',
        'Sisin içindeki bir kayın ormanı: yosunlu kökler ve ağaçların arasından süzülen ışık',
        'A beech forest in the mist — mossy roots, and light slipping between the trees',
        'Bu fotoğraf Almanya’dan; yağmurdan sonra ormanlar dünyanın her yerinde böyle nefes alır',
        'This photograph is from Germany — after rain, forests everywhere breathe like this',
        d=50, pos='50% 55%'),
    steps('Merak · Wonder',
        'Doğu Karadeniz neden bu kadar yeşil?',
        'Why is the eastern Black Sea so green?',
        [
            ['Karadeniz’den gelen nemli hava, dağların yamaçlarına çarpar', 'Moist air from the Black Sea meets the mountain slopes', ''],
            ['Hava yükseldikçe soğur; içindeki su yağmur olarak düşer', 'As the air rises it cools, and the water in it falls as rain', ''],
            ['Dağların denize bakan yüzü yıl boyunca ıslak ve yumuşak kalır', 'The seaward face of the mountains stays wet and soft all year', ''],
            ['Çay, fındık ve orman bu sisin ve yağmurun içinde büyür', 'Tea, hazelnuts and forest grow inside this mist and rain', ''],
        ],
        'Bu yeşil, bir dağın nemli havayı yukarı kaldırmasının armağanıdır',
        'This green is the gift of a mountain lifting moist air upward',
        '#1a2a22','#050a07', gap=7, d=58),
]

# ---- 19:00 Rain in art, drop physics, cozy fire ----
H19=[
    artwork('vgrain', 'Vincent van Gogh, 1889',
        'Yağmur — Vincent van Gogh, 1889: tarlaya çizgi çizgi inen sağanak',
        'Rain — Vincent van Gogh, 1889: a shower falling in lines across the field',
        'Van Gogh bunu Saint-Rémy’de yaptı; yağmuru bir perde gibi, fırça darbeleriyle yazdı',
        'Van Gogh made this in Saint-Rémy, writing the rain like a curtain, in strokes of the brush',
        d=50, pos='50% 45%'),
    artwork('shono', 'Utagawa Hiroshige, yaklaşık 1833–34',
        'Shōno’da Sağanak — Hiroshige’nin Tōkaidō dizisinden, eğik yağmurun altında yürüyen yolcular',
        'Driving Rain at Shōno — travellers walking under a slanting downpour, from Hiroshige’s Tōkaidō series',
        'Bu, iki gün önce gördüğün Shin-Ōhashi köprüsündeki sağanaktan başka bir gravürdür',
        'This is a different print from the Sudden Shower over Shin-Ōhashi you saw two days ago',
        d=50, pos='50% 48%'),
    artwork('hassam', 'Childe Hassam, 1885',
        'Yağmurlu Gün, Boston — Childe Hassam, 1885: ıslak taşlar, şemsiyeler ve at arabaları',
        'Rainy Day, Boston — Childe Hassam, 1885: wet stone, umbrellas and horse-drawn carriages',
        d=48, pos='50% 50%'),
    fact('islak sokak',
        'Islak bir sokak gökyüzünü yere indirir: izlenimciler yağmuru bu yüzden de severdi',
        'A wet street brings the sky down to the ground — one reason the Impressionists loved the rain',
        'Yansıyan ışık, bildik bir caddesini yeni bir manzaraya çevirir · Reflected light turns a familiar street into a new view',
        '#1c2430','#05080c', d=34),
    steps('Merak · Wonder',
        'Havadaki bir yağmur damlası gerçekte nasıl durur?',
        'What shape does a raindrop actually have in the air?',
        [
            ['Küçük damlalar, yüzey gerilimiyle neredeyse tam bir küredir', 'Small drops are almost perfect spheres, held by surface tension', ''],
            ['Büyüdükçe altı hava direnciyle yassılaşır: bir hamburger ekmeğine benzer', 'As they grow, air resistance flattens the bottom — like a bun', ''],
            ['Daha da irileşirse bir paraşüte döner ve parçalanır', 'Larger still, they become a parachute and then break apart', ''],
            ['Bu yüzden gökyüzünde “dev damla” uzun yaşamaz', 'That is why a “giant drop” does not last long in the sky', ''],
        ],
        'Gözyaşı biçimi bir çizim alışkanlığıdır; havadaki damla onu taklit etmez',
        'The teardrop is a habit of drawing — a drop in the air does not copy it',
        '#1a2430','#05090c', gap=7, d=58),
    photo('fire3', 'şöminede çıtırdayan ateş · a fire crackling in the hearth',
        'Dışarıda yağmur, içeride çıtırdayan bir şömine ateşi',
        'Rain outside, and a fire crackling in the hearth',
        d=50, pos='50% 60%'),
]

replacements=[
    S('%sT17:00'%DATE, '%sT18:00'%DATE, 'h-11-19-17',
      'Yağmurun Kokusu · The Smell of Rain', H17),
    S('%sT18:00'%DATE, '%sT19:00'%DATE, 'h-11-19-18',
      'Karadeniz Yağmuru · Black Sea Rain', H18),
    S('%sT19:00'%DATE, '%sT20:00'%DATE, 'h-11-19-19',
      'Yağmurun Sanatı · The Art of Rain', H19),
]

ONLY=os.environ.get('ONLY','17,18,19')
want=set(ONLY.split(','))

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
keep=[]
for s in day['sets']:
    hh=s['from'][11:13]
    if hh in want:
        continue
    keep.append(s)

newsets=[s for s in replacements if s['from'][11:13] in want]

byh={}
for s in keep:
    byh[s['from'][11:13]]=s
for s in newsets:
    byh[s['from'][11:13]]=s
order=['09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
outsets=[byh[h] for h in order]
assert len(outsets)==15, [s['from'] for s in outsets]

day['sets']=outsets
day['rev']=REV
day['_note']='Hourly sets for the villa TV. 09:00–16:00 and 20:00–02:00 from days/build_2026-11-19.py; 17:00–19:00 rebuilt by days/build_2026-11-19_evening.py (rev 72, cozy rainy afternoon: petrichor, Black Sea rain, rain in art). Content log: used-content.md'
out=os.path.join(HERE,'%s.json'%DATE)
json.dump(day,open(out,'w'),ensure_ascii=False,indent=1)
print('sets',len(day['sets']))
for s in day['sets']:
    hh=s['from'][11:13]
    mark=' *' if hh in want else ''
    tot=sum(i.get('d',0) for i in s['items'])
    print(s['id'], s['from'][11:16], len(s['items']), '%ss'%tot, s['name']+mark)
