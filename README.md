# Klinik Dokümantasyon ve Poliklinik Asistanı - README

## Genel Bakış

Bu uygulama, sağlık profesyonellerinin (hekimlerin) yoğun poliklinik akışı içerisinde dağınık, ham veya eksik formatta girdikleri hasta verilerini; anamnez, fizik muayene, laboratuvar, görüntüleme, öntanı ve öneriler içeren uluslararası standartlarda **yapılandırılmış poliklinik notu formatına** dönüştüren akıllı bir klinik asistan sistemidir.

Sistem, endokrinoloji, dahiliye ve yan dal polikliniklerinin dinamiklerine uygun olarak tasarlanmış olup, hekimin manuel dokümantasyon yükünü minimuma indirmeyi ve klinik karar destek süreçlerini hızlandırmayı amaçlar.

---

## Temel Özellikler

* **Akıllı Metin Yapılandırma:** Dağınık ve kısmi notları; *Şikayet, Özgeçmiş, Soygeçmiş, Kullanılan İlaçlar, Fizik Muayene, Klinik İzlem, Laboratuvar, Görüntüleme, Öntanı ve Öneriler* başlıkları altında standart forma sokar.
* **Branş Odaklı Sörveyans:** Tiroid hastalıkları (Hashimoto, MNG, Graves, tiroidektomi takipleri), Diabetes Mellitus (T1DM, T2DM, insülin rejimleri), sürrenal insidentalomalar, romatolojik ve otoimmün bağ dokusu hastalıkları (Sm/RNP, RA) gibi özel durumlarda kritik parametreleri (TSH, sT4, HbA1c, HU dansiteleri vb.) otomatik olarak takip eder.
* **Çoklu Vaka ve Takip Entegrasyonu:** Hastanın geçmiş poliklinik vizitlerini, kronolojik laboratuvar/patoloji sonuçlarını (örneğin mide biyopsileri, sürrenal BT raporları) ve reçete/ilaç uyum geçmişlerini hafızasında tutarak bütüncül değerlendirme sunar.
* **Entegre Diyetisyen ve Öneri Yönetimi:** Her vaka için otomatik diyetisyen konsültasyonu, hasta bilgilendirme notları ve kontrol planlamalarını standartlaştırır.

---

## Çıktı Mimarisi (Poliklinik Notu Formatı)

Oluşturulan her bir klinik doküman aşağıdaki hiyerarşik yapıyı takip eder:

```markdown
TARİH: GG.AA.YYYY             BOY: ... CM      KİLO: ... KG
ŞİKAYETİ: [Aktif yakınmalar ve semptom süresi]

........................................ÖZGEÇMİŞİ:.............................................
* [Kronik hastalıklar, cerrahi geçmişi ve alışkanlıklar]

............................SOYGEÇMİŞ:.................................................
* [Aile bireylerindeki (anne, baba, kardeş) metabolik ve kronik hastalık öyküleri]

.................................KULLANIĞI İLAÇLAR:....................................
* [Düzenli reçeteli ilaçlar, dozajlar ve son eklenen tedaviler]

.................................... FİZİK MUAYENE:........................................
GENEL DURUMU İYİ BİLİNCİ AÇIK KOOPERE
TANSİYON: .../... mmHg    NABIZ: .../dk     ATEŞ: ... °C
BB / KVS / SOLS / BATIN / EXT / Özel Bulgular ve Ödem (PTÖ) Durumu

..................KLİNİK İZLEM & ENDOKRİNOLOJİK SÖRVEYANS..................
* [Hastalığın güncel seyri, patoloji veya görüntüleme bulgularının klinik yansıması]

..................LABORATUVAR..................
akş: ...   hba1c: ...   st4: ...   tsh: ...   kcft: ...   bft: ...

..................GÖRÜNTÜLEME (USG / BT / MRG / SİNTİGRAFİ)....................
* [Radyolojik ve nükleer tıp rapor özetleri]

ÖNTANI: [ICD uyumlu veya klinik ön tanılar]

ÖNERİ:
1- [Medikal tedavi düzenlemeleri ve reçeteler]
2- [İstenen tetkikler ve kontrol planı]
3- Diyetisyen konsültasyonu
4- HASTA BİLGİLENDİRİLDİ [...]

```

---

## Kullanım Senaryoları

1. **Hızlı Not Dönüşümü:** Hekimin serbest metin veya kısa notlar şeklinde girdiği bulguları (örn: *"45y kadın, Hashimoto, TSH 4.6, dispepsi"*), saniyeler içinde eksiksiz tıbbi rapora çevirir.
2. **Kronik Hastalık Takibi:** Yıllık diyabet, hipertansiyon veya tiroid operasyonu geçiren hastaların geçmiş vizitlerini karşılaştırarak tedavi değişikliklerini (örn: *Jardiance eklenmesi, insülin doz ayarı*) kaydeder.
3. **Komplike Vaka Analizi:** Sürrenal kitleler (HU değerleri), subakut tiroidit tabloları veya dirençli anemilerde eksik tetkiklerin tamamlanmasını koordine eder.

---

## Sistem Gereksinimleri ve İş Akışı

* **Girdi:** Hekim tarafından sesli dikte veya klavye ile girilen ham klinik veriler, laboratuvar değerleri ve hasta hikayeleri.
* **Çıktı:** Hastane bilgi yönetim sistemine (HBYS) veya doğrudan poliklinik defterine kopyalanmaya hazır, taranabilir, profesyonel Markdown formatında tıbbi epikriz / poliklinik notu.
