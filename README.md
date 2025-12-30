*** Pseudocode - XOR Sayı Üreteci Algoritması ***

    TRY
        // Kullanıcı girdileri
        seed_val ← INTEGER(INPUT("Seed değeri girin (0-100): "))
        count ← INTEGER(INPUT("Kaç adet sayı üretilsin: "))
        
        // Rastgelelik tohumu
        SET_RANDOM_SEED(seed_val)
        
        // Maskeleri tanımla
        PRIME_MASK ← "00101010"     // 42 decimal
        NON_PRIME_MASK ← "01001001" // 73 decimal
        
        generated_numbers ← EMPTY_LIST
        
        // Sayı üretim döngüsü
        FOR i FROM 1 TO count DO
            // 1. Ham sayı üret
            raw_num ← RANDOM_INTEGER(0, 100)
            PRINT i + ". Üretilen Ham Sayı: " + raw_num
            
            // 2. Asal kontrolü ve XOR uygula
            IF IS_PRIME(raw_num) THEN
                PRINT raw_num + " ASAL. Prime maske uygulanıyor..."
                current_num ← APPLY_XOR(raw_num, PRIME_MASK)
            ELSE
                PRINT raw_num + " ASAL DEĞİL. Non-prime maske uygulanıyor..."
                current_num ← APPLY_XOR(raw_num, NON_PRIME_MASK)
            ENDIF
            
            // 3. XOR sonrası durum kontrolü
            IF IS_PRIME(current_num) THEN
                status ← "ASAL"
            ELSE
                status ← "ASAL DEĞİL"
            ENDIF
            PRINT "XOR sonrası yeni durum: " + current_num + " (" + status + ")"
            
            // 4. Listeye ekle
            APPEND(generated_numbers, current_num)
        ENDFOR
        
        // 5. Final seçim (Mod işlemi)
        index ← seed_val MOD LENGTH(generated_numbers)
        final_choice ← generated_numbers[index]
        
        // Sonuçları göster
        PRINT "Üretilen Liste: " + generated_numbers
        PRINT "Mod İndeksi (" + seed_val + " % " + LENGTH(generated_numbers) + "): " + index
        PRINT "SEÇİLEN FİNAL SAYI: " + final_choice
        
    CATCH ValueError
        PRINT "Lütfen sadece tam sayı giriniz!"
    ENDTRY
END
---------------------------------------------------------------------------------------------------------------------
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
