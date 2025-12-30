# Rastgele-Sayı-Üreteci
XOR Sayı Üreteci Algoritması
  "Bu program, seed ve count değerleri alarak XOR işlemi ile rastgele sayı üreten bir algoritmayı uygular. 
Üretilen sayılar, asal olup olmama durumuna göre farklı binary maskeler ile XOR'lanır ve bir liste oluşturulur. 
Son olarak seed değeri kullanılarak mod işlemi ile listeden bir final sayı seçilir."

Akış Adımları:
* Seed ve Count Girilir:
Kullanıcıdan seed (tohum) ve üretilecek sayı adedi alınır.

* Rastgele Sayı Üretimi:
random.seed() ile rastgelelik seed değerine bağlanır.
Her döngüde 0-100 arası rastgele bir tam sayı üretilir.

* Asal Kontrolü ve XOR Uygulaması:
Sayı asal ise: 00101010 (42) maskesi ile XOR'lanır.
Sayı asal değil ise: 01001001 (73) maskesi ile XOR'lanır.
XOR işlemi binary seviyede uygulanır ve detaylı çıktı verilir.

* Listeye Ekleme:
XOR sonucu oluşan sayı generated_numbers listesine eklenir.

* Final Seçimi:
index = seed % liste_uzunluğu formülü ile bir indeks belirlenir.
Belirlenen indeksteki sayı final seçim olarak belirlenir.

Kullanım Alanları:
- Şifreleme ve güvenlik simülasyonları
- Deterministik rastgelelik testleri
- Algoritmik XOR işlemlerinin eğitim amaçlı gösterimi
