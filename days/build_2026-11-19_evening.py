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

evening17=[
    S('%sT17:00'%DATE, '%sT18:00'%DATE, 'h-11-19-17',
      'Yağmurun Kokusu · The Smell of Rain', H17),
]

ONLY=os.environ.get('ONLY','17')  # '17' or '17,18,19'
want=set(ONLY.split(','))

day=json.load(open(os.path.join(HERE,'%s.json'%DATE)))
keep=[]
for s in day['sets']:
    hh=s['from'][11:13]
    if hh in want:
        continue
    keep.append(s)

newsets=[]
if '17' in want: newsets += evening17
# 18 and 19 hooked in later

# rebuild in hour order
replaced={s['from'][11:13]:s for s in newsets}
outsets=[]
# original order from keep + replacements
# Collect all hours
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
    hh=int(s['from'][11:13])
    mark=' *' if s['from'][11:13] in want else ''
    tot=sum(i.get('d',0) for i in s['items'])
    print(s['id'], s['from'][11:16], len(s['items']), '%ss'%tot, s['name']+mark)
