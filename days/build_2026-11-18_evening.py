# Rebuilds 20:00–23:00 of days/2026-11-18.json for an alone mind-spark evening.
# M is in the living room alone (asked ~19:56). 19:00 was almost over, left as-is.
# 23:00 calm night (campfire & stars) is kept. New photos: m/h70-*.jpg.
import json, os
DATE='2026-11-18'; REV=70; NEXT='2026-11-19'
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-18.json')))

FIX={
    'Bilinmeyen (kamu malı) · Unknown (public domain)':'',
    'NASA / JPL-Caltech / R. Hurt':'NASA / JPL-Caltech / R. Hurt',
    'BLM Utah (Bureau of Land Management)':'BLM Utah',
    'Jim Peaco, National Park Service':'Jim Peaco, National Park Service',
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
    it=dict(k='hzphoto', d=d, f='m/h70-%s.jpg'%k, lb=(lb or (REAL+' · '+tag)), tr=tr, en=en, cr=cr(k))
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

# ---- 20:00 Strange corners of the Earth ----
H20=[
    photo('thewave', 'The Wave, Arizona, ABD · USA',
        'The Wave — rüzgârın 190 milyon yıl önce yığdığı kum, şimdi taşa dönüşmüş bir dalga',
        'The Wave — sand piled by wind 190 million years ago, now a wave turned to stone',
        'Bu kumtaşı, bir zamanlar büyük bir çölün kumuluydu; su ve rüzgâr onu yavaşça oymuş',
        'This sandstone was once a desert dune; water and wind slowly carved it',
        d=48, pos='50% 50%'),
    photo('deadvlei', 'Deadvlei, Namibya · Namibia',
        'Deadvlei — beyaz kil tabanın üstünde, yüzyıllardır ayakta duran ölü akasya ağaçları',
        'Deadvlei — dead camel-thorn trees still standing on a white clay pan, centuries later',
        'Ağaçlar yaklaşık 600–900 yıl önce kurudu; çölün kuraklığı onları çürütmeden korudu',
        'The trees died some 600–900 years ago; the desert’s dryness kept them from rotting',
        d=48, pos='50% 55%'),
    photo('danxia', 'Zhangye Danxia, Çin · China',
        'Zhangye’nin renkli tepeleri — katman katman mineral, milyonlarca yılın kaydı',
        'The coloured hills of Zhangye — mineral layers, a record of millions of years',
        'Kırmızı demir, yeşil bakır, sarı kükürt: her şerit başka bir çağın tortusu',
        'Red iron, green copper, yellow sulphur: each stripe is the sediment of another age',
        d=48, pos='50% 45%'),
    photo('prismatic', 'Grand Prismatic Spring, Yellowstone',
        'Grand Prismatic — dünyanın en büyük sıcak su kaynaklarından, havadan bir gökkuşağı',
        'Grand Prismatic — one of the world’s largest hot springs, a rainbow from the air',
        'Halkanın renklerini ısıyı seven mikroplar verir; göbeği ise çok sıcak olduğu için steril ve mavi',
        'Heat-loving microbes paint the rings; the centre is sterile and blue because it is too hot',
        d=48, pos='50% 48%'),
    photo('socotra', 'Sokotra, Yemen · Socotra, Yemen',
        'Sokotra’nın ejderha kanı ağacı — şemsiye gibi bir taç, dünyada neredeyse yalnızca burada',
        'Socotra’s dragon’s-blood tree — an umbrella crown, found almost only on this island',
        'Adını, kırmızı reçinesinden alır; adada başka yerde görülmeyen yüzlerce tür yaşar',
        'It is named for its blood-red resin; the island is home to hundreds of species found nowhere else',
        d=48, pos='50% 50%'),
    photo('lencois', 'Lençóis Maranhenses, Brezilya · Brazil',
        'Lençóis Maranhenses — beyaz kum tepelerinin arasında yağmurun doldurduğu zümrüt göletler',
        'Lençóis Maranhenses — emerald rain-lagoons held between white sand dunes',
        '“Çarşaflar” anlamına gelir: yağmur mevsiminde kumun içi bir labirent göle dönüşür',
        'The name means “bedsheets”: in the rainy season the dunes become a labyrinth of lagoons',
        d=48, pos='50% 50%'),
    steps('Merak · Wonder',
        'Bu altı yerin ortak yanı ne?',
        'What do these six places have in common?',
        [
            ['Kimisi rüzgârla, kimisi suyla, kimisi ateşle yazıldı', 'Some were written by wind, some by water, some by fire', ''],
            ['Hiçbiri bir stüdyoda üretilmedi', 'None of them was made in a studio', ''],
            ['Çoğu, iki yüz yıl önce haritalarda bile yoktu', 'Most were not even on maps two hundred years ago', ''],
        ],
        'Hepsi gerçek — ve hepsi bu gezegende',
        'All of them are real — and all of them are on this planet',
        '#163042','#050a10', gap=7, d=52),
]

# ---- 21:00 Secrets of light ----
H21=[
    photo('aurora', 'Kuzey ışıkları, Alaska · Aurora borealis, Alaska',
        'Kuzey ışıkları — Güneş’ten gelen parçacıklar, Dünya’nın manyetik alanında bir perdesi gibi yanıyor',
        'The northern lights — particles from the Sun glowing like a curtain in Earth’s magnetic field',
        'Yeşil ve kırmızı çoğunlukla oksijenden, mor ve mavi ise azottan gelir',
        'Greens and reds mostly come from oxygen; purples and blues from nitrogen',
        d=48, pos='50% 40%'),
    photo('cristales', 'Caño Cristales, Kolombiya · Colombia',
        'Caño Cristales — “sıvı gökkuşağı”: nehir yatağındaki bitkiler, ışıkta kırmızı ve sarıya bürünür',
        'Caño Cristales — the “liquid rainbow”: plants on the riverbed turn red and yellow in the light',
        'Rengi Macarenia clavigera adlı bir su bitkisi verir; yılın yalnızca bir döneminde bu kadar parlar',
        'The colour comes from a water plant, Macarenia clavigera — it only glows like this for part of the year',
        d=48, pos='50% 50%'),
    dict(k='hzfraser', d=50),
    steps('Düşünce Deneyi · Thought Experiment',
        'Gece gökyüzü neden karanlık?',
        'Why is the night sky dark?',
        [
            ['Evren sonsuz ve yıldızlarla dolu olsaydı…', 'If the universe were endless and full of stars…', ''],
            ['Her bakış bir yıldıza rastlardı: gece, gündüz gibi parlardı', 'Every line of sight would hit a star — night would blaze like day', ''],
            ['Ama evrenin bir yaşı var; ışık her yerden henüz ulaşmadı', 'But the universe has an age: light has not yet reached us from everywhere', ''],
        ],
        'Karanlık gece, evrenin hâlâ genç olduğunun kanıtı',
        'The dark night is proof that the universe is still young',
        '#152032','#05070e', gap=7, d=56, bg='stars'),
    dict(k='hzkaniz', d=48),
    fact('8 dk 20 sn',
        'Güneş’e baktığında, 8 dakika 20 saniye önceki Güneş’i görürsün',
        'When you look at the Sun, you see it as it was 8 minutes and 20 seconds ago',
        'Işık da bir yolculuktur · Light is a journey too',
        '#1a2436','#05080e', d=32),
]

# ---- 22:00 Night thoughts (curious, a little calmer) ----
H22=[
    photo('starlake', 'Bontecou Gölü, New York · Bontecou Lake, New York',
        'Gölün üstünde Samanyolu — bakışın, binlerce yıl önce yola çıkan ışığa denk geliyor',
        'The Milky Way over a lake — your gaze meets light that set out thousands of years ago',
        'Gördüğün her yıldız, kendi zamanından bir kartpostal gibidir',
        'Every star you see is a postcard from its own time',
        fit='contain', d=52),
    q('Beni bende demen, bende değilim;|bir ben vardır bende, benden içeri',
      'Don’t say I am in myself — I am not; there is a self in me, deeper than I am',
      'night', d=48,
      lb='Yunus Emre’den · From Yunus Emre',
      by='Yunus Emre'),
    photo('milkyway', 'Samanyolu canlandırması · Milky Way illustration',
        'Dışarıdan bakınca Samanyolu böyle olabilir — bu bir fotoğraf değil, bilimsel bir canlandırma',
        'The Milky Way as it may look from outside — not a photograph, a scientific illustration',
        'Samanyolu’nu dışarıdan çeken bir uzay aracımız hiç olmadı; görüntü, verilerden çizildi',
        'No spacecraft has ever photographed the Milky Way from outside; this was drawn from data',
        fit='contain', d=52,
        lb='Sanatçı yorumu · Artist’s conception — NASA / JPL-Caltech / R. Hurt'),
    dict(k='hzfirefly', d=56),
    steps('Gece Düşüncesi · A Night Thought',
        'Elinin içindeki demir nereden geldi?',
        'Where did the iron in your hand come from?',
        [
            ['Genç evrende yalnızca en hafif elementler vardı', 'The young universe held only the lightest elements', ''],
            ['Demir, ölen yıldızların içinde pişti', 'Iron was cooked inside dying stars', ''],
            ['Bir süpernova onu uzaya saçtı; toz bu gezegene yağdı', 'A supernova scattered it — the dust fell onto this planet', ''],
        ],
        'Elini çevir: yıldızların külleri sende',
        'Turn your hand: the ashes of stars are in you',
        '#12182a','#04060c', gap=7, d=56, bg='stars'),
    fact('13,8 milyar yıl',
        'Gökyüzündeki en uzak ışık, evrenin neredeyse başlangıcından yola çıkmış olabilir',
        'The most distant light in the sky may have set out from near the beginning of the universe',
        'Gece, bir zaman makinesidir · Night is a time machine',
        '#161c2c','#04060a', d=34),
]

evening=[
    S('%sT20:00'%DATE, '%sT21:00'%DATE, 'h-11-18-20',
      'Dünyanın Tuhaf Köşeleri · Strange Corners of the Earth', H20),
    S('%sT21:00'%DATE, '%sT22:00'%DATE, 'h-11-18-21',
      'Işığın Sırları · Secrets of Light', H21),
    S('%sT22:00'%DATE, '%sT23:00'%DATE, 'h-11-18-22',
      'Geceye Kalan Sorular · Questions for the Night', H22),
]

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
keep=[]
for s in day['sets']:
    hh=int(s['from'][11:13])
    if hh<20 or hh>=23:
        keep.append(s)
assert [s['from'][11:16] for s in keep]==['09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','23:00'], [s['from'] for s in keep]
early=[s for s in keep if int(s['from'][11:13])<20]
late=[s for s in keep if int(s['from'][11:13])>=23]
day['sets']=early+evening+late
day['rev']=REV
day['_note']='Hourly sets for the villa TV. Morning–19:00 and 23:00 from days/build_2026-11-18.py; 20:00–23:00 rebuilt by days/build_2026-11-18_evening.py (rev 70, alone mind-spark: strange places, light, night thoughts). Content log: used-content.md'
out=os.path.join(HERE,'%s.json'%DATE)
json.dump(day,open(out,'w'),ensure_ascii=False,indent=1)
print('sets',len(day['sets']))
for s in day['sets']:
    hh=int(s['from'][11:13])
    mark=' *' if 20<=hh<23 else ''
    tot=sum(i.get('d',0) for i in s['items'])
    print(s['id'], s['from'][11:16], len(s['items']), '%ss'%tot, s['name']+mark)
