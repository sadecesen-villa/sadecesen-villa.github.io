# Rebuilds 15:00–18:00 of days/2026-11-23.json as a fresh, unexpected set.
# M is in the living room and asked for new things and new ideas, different today.
# New photos: m/h78-*.jpg. New calm night scene: hzglowworm in hourly.js v78.
import json, os
DATE='2026-11-23'; REV=78
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-23e.json')))

FIX={
    'Hannes Grobe (talk)':'Hannes Grobe',
    'NOAA/Monterey Bay Aquarium Research Institute':'NOAA / MBARI',
    'Annick MONNIER':'Annick Monnier',
    'moments in nature by Antje Schultner':'Antje Schultner',
    'User:Ggia':'Ggia',
    'Steve FUNG':'Steve Fung',
    'Fernando Flores from Caracas, Venezuela':'Fernando Flores',
    'P. Horálek/ESO':'P. Horálek / ESO',
}
def artist(k):
    a=C[k].get('artist','')
    for f,t in FIX.items():
        if a.startswith(f) or a==f: return t
    return a.split('(')[0].strip().rstrip('.')
def lic(k):
    return C[k]['lic'].replace('Public domain','kamu malı · public domain').replace('CC0','CC0 · kamu malı · public domain')
def cr(k):
    a=artist(k)
    if a:
        return 'Foto · Photo: %s · %s · Wikimedia Commons'%(a, lic(k))
    return 'kamu malı · public domain · Wikimedia Commons'
REAL='Gerçek Fotoğraf · Real Photo'

def photo(k, tag, tr, en, fact=None, facte=None, fit=None, d=48, pos=None, lb=None):
    it=dict(k='hzphoto', d=d, f='m/h78-%s.jpg'%k, lb=(lb or (REAL+((' · '+tag) if tag else ''))), tr=tr, en=en, cr=cr(k))
    if fact: it.update(fact=fact, facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it

def fact(big, tr, en, src, c1, c2, d=30):
    return dict(k='hzfact', d=d, big=big, tr=tr, en=en, src=src, c1=c1, c2=c2)

def g(k, d=60):
    return dict(k=k, d=d)

def S(frm, until, sid, name, items):
    return dict(id=sid, name=name, **{'from':frm,'until':until}, items=items)

# ---- 15:00 Nature’s Hidden Architecture ----
H15=[
    photo('radio', 'Elektron mikroskobu · Electron microscope',
        'Bir radyolaryanın iskeleti: denizdeki görünmez bir canlının camdan sarayı',
        'The skeleton of a radiolarian: a glass palace belonging to a creature too small to see',
        'Radyolaryalar, iskeletlerini kumun ve camın da yapıldığı silikadan örer; çoğu bir milimetreden küçüktür',
        'Radiolarians weave their skeletons from silica, the same mineral as sand and glass — most are smaller than a millimetre',
        fit='contain', d=50),
    photo('sponge', 'Venüs’ün Çiçek Sepeti · Venus’s flower basket',
        'Derin denizin cam süngeri: ipek gibi duran, aslında cam ipliklerden örülmüş bir sepet',
        'A glass sponge of the deep sea: a basket that looks like silk, but is woven from threads of glass',
        'Japonya’da bu sünger düğün hediyesi olur: içinde çoğu zaman bir çift karides büyür ve bir daha dışarı çıkamaz',
        'In Japan this sponge is given as a wedding gift: a pair of shrimp often grow up inside and can never leave',
        d=50, pos='50% 50%'),
    photo('frost', 'Kırağı kristalleri · Hoar-frost crystals',
        'Kırağının bir gecede kurduğu buz bahçesi: her dal, incecik bir kristal kule',
        'A garden of ice, built by hoar frost in a single night: every branch is a slender crystal tower',
        d=48, pos='45% 45%'),
    photo('soap', 'Sabun zarı · Soap film',
        'Bir sabun zarının üstünde dans eden renkler: yağ adacıkları ve ışığın girişimi',
        'Colours dancing on a soap film: lipid islands and the interference of light',
        'Renkler boya değil: zarın kalınlığı değiştikçe ışık kendi kendine bu halkaları çizer',
        'The colours are not paint — as the film’s thickness changes, light draws these rings by itself',
        fit='contain', d=48),
    photo('webdew', 'Çiy ve ipek · Dew and silk',
        'Örümcek ağında çiy taneleri: ipek üzerine dizilmiş bir inci perdesi',
        'Dew on a spider’s web: a curtain of pearls strung on silk',
        d=48, pos='50% 50%'),
]

# ---- 16:00 Wonder Machines ----
H16=[
    photo('falkirk', 'Falkirk Çarkı, İskoçya · The Falkirk Wheel, Scotland',
        'Falkirk Çarkı: tekneleri bir kanaldan ötekine, dev bir tekerlek gibi döndürerek taşıyor',
        'The Falkirk Wheel: it carries boats from one canal to the other by turning like a giant wheel',
        'Tek bir dönüş yaklaşık beş dakika sürer ve tekneleri 24 metre yükseltir',
        'A single half-turn takes about five minutes and lifts the boats 24 metres',
        d=50, pos='46% 48%'),
    photo('sacsay', 'Saksaywaman, Peru · Sacsayhuamán, Peru',
        'Saksaywaman: harç yok, kilit yok; yüz tonluk taşlar yine de bıçak sığmayan bir hassaslıkla oturuyor',
        'Sacsayhuamán: no mortar, no clamps — and yet stones of a hundred tonnes sit so tightly a knife will not fit',
        d=48, pos='50% 42%'),
    photo('yakhchal', 'Yakhchal, Meybod, İran',
        'Yakhchal: çölün ortasında, yalnızca rüzgâr ve gölgeyle buzu yaz boyu saklayan bir kule',
        'A yakhchal: a tower in the desert that kept ice through the summer, using only wind and shade',
        'Kalın kerpiç duvarlar ve bir yeraltı havuzu, içeriye sıcaklığı neredeyse hiç bırakmaz',
        'Thick mud-brick walls and an underground chamber let almost no heat inside',
        d=50, pos='50% 42%'),
    photo('noria', 'Hama su dolapları, Suriye · Norias of Hama, Syria',
        'Hama’nın su dolabı: nehir onu çevirir, ahşap kutu kutu suyu yukarı taşır',
        'A noria of Hama: the river turns it, and wooden boxes carry the water up',
        'Bazıları 20 metreyi aşar; asırlarca aynı işi görmüşlerdir',
        'Some stand more than 20 metres high, and have done the same work for centuries',
        d=48, pos='55% 48%'),
    fact('24 m',
        'Falkirk Çarkı, iki kanal arasındaki 24 metrelik kot farkını merdiven merdiven kilitle değil, tek bir yarım turla aşıyor',
        'The Falkirk Wheel crosses the 24-metre drop between two canals in a single half-turn — not by a flight of locks',
        'Aynı işi eski yöntemle yapmak için yaklaşık 11 kilit gerekir · Doing the same job the old way would take about 11 locks',
        '#1a2430','#05070b', d=32),
]

# ---- 17:00 Secret Craft ----
H17=[
    photo('millefiori', 'Millefiori cam çubukları · Millefiori glass canes',
        'Millefiori: her küçük cam dilimi, içine gizlenmiş bir çiçek',
        'Millefiori: every little slice of glass hides a flower inside',
        'İtalyanca adı “bin çiçek” demek; çubuklar üst üste eritilir, sonra ince ince kesilir',
        'The Italian name means “a thousand flowers” — the canes are fused, then sliced thin',
        d=48, pos='50% 50%'),
    photo('lace', 'Mekikli dantel · Bobbin lace',
        'Mekikli dantel: yüzlerce iğne, onlarca makara, ve ipliğin ağır ağır ördüğü bir dantel bahçesi',
        'Bobbin lace: hundreds of pins, dozens of bobbins, and a garden of lace the thread slowly weaves',
        d=48, pos='50% 46%'),
    photo('maras', 'Maras tuz tarlaları, Peru · Salt pans of Maras, Peru',
        'Maras tuz tarlaları: vadinin yamacına basamak basamak oyulmuş yüzlerce sığ havuz',
        'The salt pans of Maras: hundreds of shallow pools stepped into the side of the valley',
        'İnka döneminden beri el ile işlenir; dağdan gelen tuzlu su burada güneşte kristalleşir',
        'They have been worked by hand since Inca times — salty water from the mountain crystallises here in the sun',
        d=50, pos='50% 58%'),
    photo('pag', 'Pag Adası, Hırvatistan · The island of Pag, Croatia',
        'Havadan bakınca tuz tarlaları: denizin kenarına çizilmiş geometrik bir bahçe',
        'Salt pans from the air: a geometric garden drawn along the edge of the sea',
        d=48, pos='50% 45%'),
    fact('bin çiçek',
        'Millefiori çubuğunun içindeki çiçek, aslında renkli camların milimetre milimetre üst üste eritilmesiyle doğar',
        'The flower inside a millefiori cane is born by fusing coloured glasses together, millimetre by millimetre',
        'Kesildiğinde her dilim, aynı çiçeğin yeni bir yüzünü gösterir · Each slice shows a new face of the same flower',
        '#1a2430','#05070b', d=32),
]

# ---- 18:00 Night phenomena ----
H18=[
    photo('biowave', 'Norderney, Kuzey Denizi · Norderney, North Sea',
        'Yakamoz: dalgalar kıyıya vurunca, minik planktonlar mavi bir ışık saçıyor',
        'Sea sparkle: as the waves reach the shore, tiny plankton give off a blue light',
        'Bu ışığı çoğu zaman Noctiluca adlı tek hücreli canlılar yapar; adı Latince “geceyi aydınlatan” demek',
        'The light is often made by a single-celled creature called Noctiluca — the name means “night-shining” in Latin',
        d=50, pos='50% 58%'),
    photo('catatumbo', 'Maracaibo Gölü, Venezuela · Lake Maracaibo, Venezuela',
        'Catatumbo şimşekleri: gölün üstünde, neredeyse her akşam tekrar eden bir şimşek yağmuru',
        'The lightning of Catatumbo: a rain of bolts over the lake, returning on almost every evening',
        'Burası dünyanın “şimşek başkenti” sayılır: bazı yıllarda saatte 200’den fazla çarpma ölçülmüştür',
        'This place is often called the world’s lightning capital — in some years more than 200 strokes an hour have been counted',
        d=50, pos='52% 48%'),
    photo('sprites', 'Paranal Gözlemevi, Şili · Paranal Observatory, Chile',
        'Kırmızı hayaletler: fırtınanın çok üstünde, bir anlığına gökyüzüne yükselen kırmızı ışık sütunları',
        'Red sprites: columns of red light that leap into the sky for an instant, far above the storm',
        'Bir sprite yalnızca birkaç milisaniye sürer ve 80–90 kilometre yüksekliğe kadar çıkabilir',
        'A sprite lasts only a few milliseconds, and can climb as high as 80–90 kilometres',
        d=50, pos='58% 42%'),
    g('hzglowworm', d=70),
    fact('90 km',
        'Kırmızı hayaletler o kadar kısadır ki göz çoğu zaman onları kaçırır; kamera, 90 kilometreye yükselen o kırmızı sütunları yakalar',
        'Red sprites are so brief that the eye often misses them — the camera catches those red columns as they climb 90 kilometres',
        '1990’lara kadar çoğu bilim insanı onların gerçekten var olduğundan emin değildi · Until the 1990s most scientists were not sure they were real',
        '#121a26','#03050a', d=32),
]

replacements=[
    S('%sT15:00'%DATE, '%sT16:00'%DATE, 'h-11-23-15',
      'Doğanın Gizli Mimarisi · Nature’s Hidden Architecture', H15),
    S('%sT16:00'%DATE, '%sT17:00'%DATE, 'h-11-23-16',
      'Harika Makineler · Wonder Machines', H16),
    S('%sT17:00'%DATE, '%sT18:00'%DATE, 'h-11-23-17',
      'Gizli Zanaat, Maddenin Sihri · Secret Craft & the Magic of Materials', H17),
    S('%sT18:00'%DATE, '%sT19:00'%DATE, 'h-11-23-18',
      'Gecenin Fenomenleri · Phenomena of the Night', H18),
]

ONLY=os.environ.get('ONLY','15,16,17,18')
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
day['_note']='Hourly sets for the villa TV. 09:00–14:00 and 19:00–02:00 from days/build_2026-11-23.py; 15:00–18:00 rebuilt by days/build_2026-11-23_afternoon.py (rev 78, fresh unexpected hours: nature’s hidden architecture, wonder machines, secret craft, phenomena of the night + hzglowworm). Content log: used-content.md'
out=os.path.join(HERE,'%s.json'%DATE)
json.dump(day,open(out,'w'),ensure_ascii=False,indent=1)
print('sets',len(day['sets']),'rev',day['rev'])
for s in day['sets']:
    hh=s['from'][11:13]
    mark=' *' if hh in want else ''
    tot=sum(i.get('d',0) for i in s['items'])
    print(s['id'], s['from'][11:16], len(s['items']), '%ss'%tot, s['name']+mark)
