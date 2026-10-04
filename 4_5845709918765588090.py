import datetime

# Sizin verdiğiniz ham metinden ayıklanan veriler
hasta_verisi = {
    'boy': '...',      # Bilgi verilmemiş
    'kilo': '...',     # Bilgi verilmemiş
    'sikayet': 'Halsizlik, yorgunluk, kilo verememe şikayeti ile başvuruyor.',
    'ozgecmis': 'Bilinen PCOS ve Diyabet tanıları mevcut.',
    'soygecmis_anne': 'Diyabet (+)',
    'soygecmis_baba': '...',
    'soygecmis_kardes': '...',
    'ilaclar': 'Vasoxen',
    'genel_durum': 'İYİ BİLİNCİ AÇIK KOOPERE',
    'tansiyon': '...',
    'nabiz': '...',
    'ates': '...',
    'solunum': '...',
    'bb': 'KONJOKTİVALAR DOĞAL İKTER YOK SİYANOZ YOK',
    'kvs': 'S1+S2+ RİTMİK DÜZENLİ',
    'sols': 'H2HTSEK RAL YOK RONKUS YOK',
    'batin': 'DOĞAL DEFANS YOK REBAUND YOK',
    'ext': 'NABIZLAR AÇIK PTÖ YOK',
    'aks': '...',
    'hba1c': '...',
    'st4': '...',
    'tsh': '...',
    'kcft': '...',
    'bft': '...',
    'goruntuleme': '...',
    'ontani': 'PCOS, Diyabet, Halsizlik ve Yorgunluk (Etiyoloji araştırılıyor)',
    'oneri': 'Laboratuvar tetkikleri sonrası tedavi planlanacak.'
}

def anamnez_yazdir(v):
    tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    
    cikti = f"""
TARİH: {tarih:<20} BOY: {v['boy']:<6} CM      KİLO: {v['kilo']:<6} KG
ŞİKAYETİ:  
{v['sikayet']}
   
........................................ÖZGEÇMİŞİ:.............................................
{v['ozgecmis']}

............................SOYGEÇMİŞİ:.................................................
ANNE: {v['soygecmis_anne']}
BABA: {v['soygecmis_baba']}
KARDEŞ: {v['soygecmis_kardes']}
.................................KULLANDIĞI İLAÇLAR:....................................
{v['ilaclar']}
  
.................................... FİZİK MUAYENE:........................................
GENEL DURUMU {v['genel_durum']}
TANSİYON: {v['tansiyon']:<15} NABIZ: {v['nabiz']:<15} ATEŞ: {v['ates']:<15} SOL.SAYISI: {v['solunum']}
BB: {v['bb']}
KVS: {v['kvs']}
SOLS: {v['sols']}
BATIN: {v['batin']}
EXT: {v['ext']}
.................................LABORATUVAR...................................................
akş: {v['aks']:<10} hba1c: {v['hba1c']:<10} st4: {v['st4']:<10} tsh: {v['tsh']:<10} kcft: {v['kcft']:<10} bft: {v['bft']}
..........................GÖRÜNTÜLEME(USG/BT/MRI/SİNTİGRAFİ)....................
{v['goruntuleme']}

ÖNTANI: {v['ontani']}
ÖNERİ: {v['oneri']}

1-HASTA BİLGİLENDİRİLDİ İLAÇLARI ANLATILDI
2-POLİKLNİK KONTROLÜ ÖNERİLDİ
"""
    return cikti

print(anamnez_yazdir(hasta_verisi))