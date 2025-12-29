import random

def is_prime(n):
    """Bir sayının asal olup olmadığını kontrol eder"""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def apply_xor(number, mask_bin):
    """Sayıyı binary maske ile XOR'lar ve detayları gösterir"""
    mask_int = int(mask_bin, 2)
    result = number ^ mask_int
    print(f"    İşlem: {number} (bin: {bin(number)[2:].zfill(8)})")
    print(f"    Maske: {mask_int} (bin: {mask_bin})")
    print(f"    Sonuç: {result} (bin: {bin(result)[2:].zfill(8)})")
    return result

def main():
    print("=== Gelişmiş XOR ve Sayı Üretici ===\n")
    
    try:
        seed_val = int(input("Seed değeri girin (0-100): "))
        count = int(input("Kaç adet sayı üretilsin: "))
        
        random.seed(seed_val)
        
        # XOR Maskeleri
        PRIME_MASK = "00101010"     # 42
        NON_PRIME_MASK = "01001001" # 73
        
        generated_numbers = []

        for i in range(1, count + 1):
            raw_num = random.randint(0, 100)
            print(f"\n{i}. Üretilen Ham Sayı: {raw_num}")
            
            # 1. XOR Aşaması
            if is_prime(raw_num):
                print(f"  -> {raw_num} ASAL. Prime maske uygulanıyor...")
                current_num = apply_xor(raw_num, PRIME_MASK)
            else:
                print(f"  -> {raw_num} ASAL DEĞİL. Non-prime maske uygulanıyor...")
                current_num = apply_xor(raw_num, NON_PRIME_MASK)

            # 2. Kontrol ve Final (Burada mantık hatasını önlemek için 
            # sadece durum bildirip listeye ekliyoruz)
            status = "ASAL" if is_prime(current_num) else "ASAL DEĞİL"
            print(f"  -> XOR sonrası yeni durum: {current_num} ({status})")
            
            generated_numbers.append(current_num)

        # Final Seçimi (Mod işlemi)
        index = seed_val % len(generated_numbers)
        final_choice = generated_numbers[index]
        
        print("\n" + "="*40)
        print(f"Üretilen Liste: {generated_numbers}")
        print(f"Mod İndeksi ({seed_val} % {len(generated_numbers)}): {index}")
        print(f"SEÇİLEN FİNAL SAYI: {final_choice}")
        print("="*40)

    except ValueError:
        print("Lütfen sadece tam sayı giriniz!")

if __name__ == "__main__":
    main()