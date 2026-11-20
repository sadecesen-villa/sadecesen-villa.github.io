# Rebuilds 11:00–14:00 of days/2026-11-20.json as a guest-worthy set.
# M is in the living room alone and someone may drop in; the TV should look stunning.
# Math/quiz (sieve, thought experiments) moved off these hours; 17:00 still has hzhalve.
# New photos: m/h74-*.jpg
import json, os
DATE='2026-11-20'; REV=74
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,'credits-2026-11-20e.json')))

FIX={
    'Bilinmeyen (kamu malı) · Unknown (public domain)':'',
    'Lviatour':'Luc Viatour',
    'xiquinhosilva':'Xiquinho Silva',
    'SCIENCE: NASA, ESA, CSA, STScI; IMAGE PROCESSING: Joseph DePasquale (STScI), Ant':'NASA, ESA, CSA, STScI',
    'NASA, ESA, M. Robberto (Space Telescope Science Institute/ESA) and the Hubble Sp':'NASA, ESA, M. Robberto / Hubble',
    'Giovanni Antonio Canal':'Canaletto',
    'NASA/ESA/Hubble Heritage Team':'NASA, ESA, Hubble Heritage Team',
    'NASA/SDO (AIA)':'NASA / SDO',
    'Ximonic (Simo Räsänen)':'Simo Räsänen',
}
def artist(k):
    a=C[k].get('artist','')
    for f,t in FIX.items():
        if a.startswith(f) or a==f: return t
    # also prefix match already handled; trim
    if a.startswith('SCIENCE: NASA'): return 'NASA, ESA, CSA, STScI'
    if a.startswith('NASA, ESA, M. Robberto'): return 'NASA, ESA, M. Robberto / Hubble'
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
    it=dict(k='hzphoto', d=d, f='m/h74-%s.jpg'%k, lb=(lb or (REAL+((' · '+tag) if tag else ''))), tr=tr, en=en, cr=cr(k))
    if fact: it.update(fact=fact, facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it

def artwork(k, tag, tr, en, fact=None, facte=None, fit='contain', d=46, pos=None):
    a=artist(k)
    crd='Eser · Artwork: %s · %s · Wikimedia Commons'%(a, lic(k)) if a else 'kamu malı · public domain · Wikimedia Commons'
    lb='Gerçek Eser · Real Artwork'+((' · '+tag) if tag else '')
    it=dict(k='hzphoto', d=d, f='m/h74-%s.jpg'%k, lb=lb, tr=tr, en=en, cr=crd)
    if fact: it.update(fact=fact, facte=facte)
    if fit: it['fit']=fit
    if pos: it['pos']=pos
    return it

def q(tr, en, pal, d=42, lb=None, by=None):
    it=dict(k='hzquote', d=d, tr=tr, en=en, pal=pal)
    if lb: it.update(lb=lb, by=by)
    return it

def S(frm, until, sid, name, items):
    return dict(id=sid, name=name, **{'from':frm,'until':until}, items=items)

# ---- 11:00 Breathtaking places ----
H11=[
    photo('uyuni', 'Uyuni Tuz Çölü, Bolivya · Uyuni Salt Flat, Bolivia',
        'Uyuni Tuz Çölü’nde gün doğumu: dağ, sığ suda tersten duruyor',
        'Sunrise on the Uyuni Salt Flat: a mountain standing upside down in the shallow water',
        'Dünyanın en büyük tuz düzlüğü: yaklaşık 10.500 kilometrekare',
        'The world’s largest salt flat: about 10,500 square kilometres',
        d=50, pos='50% 55%'),
    photo('dolomites', 'Tre Cime di Lavaredo, İtalya',
        'Dolomitler’de Tre Cime: üç kule gibi yükselen kayalık zirveler',
        'The Tre Cime in the Dolomites: three peaks rising like stone towers',
        d=48, pos='50% 45%'),
    photo('iguazu', 'Iguazú Şelaleleri · Iguazú Falls',
        'Iguazú Şelaleleri: ormanın içinden yan yana dökülen onlarca su perdesi',
        'Iguazú Falls: dozens of curtains of water falling side by side through the forest',
        'Şelale hattı yaklaşık üç kilometre; su 80 metreye kadar düşer',
        'The falls stretch for about three kilometres, dropping as much as 80 metres',
        d=48, pos='50% 62%'),
    photo('paine', 'Torres del Paine, Şili',
        'Paine’nin Boynuzları: turkuaz Pehoé Gölü’nün üstünde, rüzgârın yonttuğu zirveler',
        'The Horns of Paine: wind-carved peaks above the turquoise of Lake Pehoé',
        d=48, pos='50% 45%'),
    photo('zhangjiajie', 'Zhangjiajie, Çin',
        'Zhangjiajie’nin taş ormanı: incelip yükselen kulelerin üstünü orman tutmuş',
        'The stone forest of Zhangjiajie: slender pillars crowned with forest',
        d=48, pos='50% 50%'),
    q('Akıllılığını sat,|hayret satın al',
      'Sell your cleverness and buy bewilderment',
      'sea'),
]

# ---- 12:00 Architecture ----
H12=[
    photo('taj', 'Tac Mahal, Agra',
        'Tac Mahal: yapının kendisi ve sudaki ikizi, aynı sessizlikte',
        'The Taj Mahal: the building and its twin in the water, equally still',
        'Beyaz mermer, günün ışığına göre renk değiştirir: şafakta pembe, öğleyin parlak, akşamüstü sıcak',
        'The white marble changes with the light: pink at dawn, bright at noon, warm in the evening',
        d=50, pos='50% 50%'),
    photo('alhambra', 'Elhamra, Granada',
        'Elhamra’da Mersin Avlusu: uzun bir havuz, işlemeli kemerler ve sakin bir yansıma',
        'The Court of the Myrtles in the Alhambra: a long pool, carved arches, and a calm reflection',
        d=48, pos='50% 50%'),
    photo('angkor', 'Angkor Wat, Kamboçya',
        'Angkor Wat’ta gün doğumu: kuleler ve palmiyeler, havuzda tersine dönmüş',
        'Sunrise at Angkor Wat: towers and palms turned upside down in the pool',
        d=48, pos='50% 45%'),
    photo('sagrada', 'Sagrada Família, Barselona',
        'Sagrada Família: renkli camların ışığı taşı bir ormana çeviriyor',
        'The Sagrada Família: light from stained glass turns the stone into a forest',
        'Antoni Gaudí’nin tasarladığı bu kilisenin inşası 1882’de başladı; hâlâ sürüyor',
        'Antoni Gaudí began this church in 1882 — and it is still being finished',
        d=50, pos='50% 40%'),
    photo('montst', 'Mont-Saint-Michel, Fransa',
        'Mont-Saint-Michel: günün ilk ışığında, gelgitin üstünde yükselen bir ada',
        'Mont-Saint-Michel: an island rising from the tidal flats in the first light',
        'Su çekilince adaya yürüyerek gidilir; gelgit gelince yeniden deniz onu çevreler',
        'When the tide goes out you can walk to the island; when it returns, the sea surrounds it again',
        d=50, pos='50% 45%'),
]

# ---- 13:00 Great masters ----
H13=[
    artwork('shalott', '',
        'Shalott Leydisi — John William Waterhouse, 1888',
        'The Lady of Shalott — John William Waterhouse, 1888',
        'Tablo, Tennyson’ın şiirindeki kadını, kaderini beklerken bir kayıkta gösterir',
        'The painting shows the woman from Tennyson’s poem, waiting for her fate in a boat',
        d=48),
    artwork('canaletto', '',
        'Büyük Kanal’ın Girişi, Venedik — Canaletto, yaklaşık 1730',
        'The Entrance to the Grand Canal, Venice — Canaletto, about 1730',
        d=46),
    artwork('cotopaxi', '',
        'Cotopaxi — Frederic Edwin Church, 1862',
        'Cotopaxi — Frederic Edwin Church, 1862',
        'Church, Ekvador’daki bu yanardağı yerinde gördükten sonra bu geniş manzarayı yaptı',
        'Church painted this wide view after seeing the volcano in Ecuador for himself',
        d=48),
    artwork('athens', '',
        'Atina Okulu — Raphael, 1509–1511',
        'The School of Athens — Raphael, 1509–1511',
        'Vatikan’daki bu duvar resminin ortasında Platon ve Aristoteles yan yana yürür',
        'At the centre of this Vatican fresco, Plato and Aristotle walk side by side',
        d=48),
    artwork('oxbow', '',
        'Oxbow, Fırtına Sonrası — Thomas Cole, 1836',
        'The Oxbow, After a Thunderstorm — Thomas Cole, 1836',
        d=46),
    q('Ne kadar sessizleşirsen,|o kadar çok duyarsın',
      'The quieter you become, the more you can hear',
      'ink'),
]

# ---- 14:00 Wonders of the sky ----
# Space images: label real photo vs representative/filter/infrared/EUV colour
H14=[
    photo('eclipse', '12 Ağustos 2026',
        'Tam güneş tutulması: Ay’ın arkasından görünen taç, korona',
        'A total solar eclipse: the corona, seen around the Moon',
        'Korona, Güneş’in milyonlarca derece sıcaklıktaki dış atmosferidir; normal günde görünmez',
        'The corona is the Sun’s outer atmosphere, millions of degrees hot; on an ordinary day it is invisible',
        fit='contain', d=50, pos='50% 50%'),
    photo('pillars', 'Kartal Bulutsusu · Eagle Nebula',
        'Yaratılış Sütunları — James Webb’in kızılötesi fotoğrafı (renkler temsili)',
        'The Pillars of Creation — a James Webb infrared photograph (colours are representative)',
        'Kartal Bulutsusu’nda, yaklaşık 7.000 ışık yılı ötede',
        'In the Eagle Nebula, about 7,000 light-years away',
        fit='contain', d=50),
    photo('orion', 'Orion Bulutsusu · Orion Nebula',
        'Orion Bulutsusu — Hubble’ın binlerce kareden birleştirdiği mozaik (filtre renkleri)',
        'The Orion Nebula — a Hubble mosaic of thousands of frames (filter colours)',
        fit='contain', d=48),
    photo('horsehead', 'Atbaşı Bulutsusu · Horsehead Nebula',
        'Atbaşı Bulutsusu — Hubble’ın kızılötesi fotoğrafı (renkler temsili)',
        'The Horsehead Nebula — a Hubble infrared photograph (colours are representative)',
        fit='contain', d=48),
    photo('sun', '',
        'Güneş — NASA’nın SDO uydusu, aşırı morötesi ışıkta (renkler temsili)',
        'The Sun — NASA’s SDO satellite, in extreme ultraviolet (colours are representative)',
        fit='contain', d=50),
]

replacements=[
    S('%sT11:00'%DATE, '%sT12:00'%DATE, 'h-11-20-11',
      'Nefes Kesen Yerler · Breathtaking Places', H11),
    S('%sT12:00'%DATE, '%sT13:00'%DATE, 'h-11-20-12',
      'Taşın Şiiri · Poetry in Stone', H12),
    S('%sT13:00'%DATE, '%sT14:00'%DATE, 'h-11-20-13',
      'Büyük Ustalardan · From the Great Masters', H13),
    S('%sT14:00'%DATE, '%sT15:00'%DATE, 'h-11-20-14',
      'Gökyüzünün Harikaları · Wonders of the Sky', H14),
]

ONLY=os.environ.get('ONLY','11,12,13,14')
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
day['_note']='Hourly sets for the villa TV. 09:00–10:00 and 15:00–02:00 from days/build_2026-11-20.py; 11:00–14:00 rebuilt by days/build_2026-11-20_afternoon.py (rev 74, guest-worthy: breathtaking places, architecture, great masters, wonders of the sky). Sieve of Eratosthenes and afternoon thought experiments moved off 12:00–13:00 and not rescheduled, to keep later hours intact; 17:00 still has the 20-questions / binary search set. Content log: used-content.md'
out=os.path.join(HERE,'%s.json'%DATE)
json.dump(day,open(out,'w'),ensure_ascii=False,indent=1)
print('sets',len(day['sets']),'rev',day['rev'])
for s in day['sets']:
    hh=s['from'][11:13]
    mark=' *' if hh in want else ''
    tot=sum(i.get('d',0) for i in s['items'])
    print(s['id'], s['from'][11:16], len(s['items']), '%ss'%tot, s['name']+mark)
