import string

dosya_adi = "uygulama1.txt"

# 1. Adım: Güvenli Okuma
try:
    with open(dosya_adi, "r", encoding="utf-8") as f:
        icerik = f.read()
except FileNotFoundError:
    print(f"HATA: '{dosya_adi}' bulunamadı.")
    icerik = None

if icerik is not None:
    # 2. Adım: Temizlik ve Hazırlık
    temiz_metin = icerik
    for isaret in string.punctuation:
        temiz_metin = temiz_metin.replace(isaret, "")

    kelimeler_listesi = temiz_metin.lower().split()

    # 3. Adım: Sayma
    kelime_sayilari = {}
    for kelime in kelimeler_listesi:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1
        else:
            kelime_sayilari[kelime] = 1

    # 4. Adım: Sıralama (En çoktan en aza)
    sirali_liste = sorted(kelime_sayilari.items(), key=lambda x: x[1], reverse=True)[:3]

    print(f"\n--- Analiz Edilen Toplam Kelime Sayısı: {len(kelimeler_listesi)} ---")

    # ---------------------------------------------------------
    # 5. ADIM: UZUNLUĞU 5'TEN BÜYÜK EN TEKRAR EDEN KELİME
    # ---------------------------------------------------------
    secilen_kelime = None
    secilen_adet = 0

    # Listemiz zaten "en çok geçenler" en üstte olacak şekilde sıralı.
    # Bu yüzden listeyi dönüyoruz ve şartı sağlayan İLK kelimeyi alıp kaçıyoruz.
    for kelime, adet in sirali_liste:
        if len(kelime) > 5:
            secilen_kelime = kelime
            secilen_adet = adet
            break  # HEDEFİ BULDUK, DÖNGÜYÜ KIR (Performans kazancı)

    # Sonuç Raporlama
    print("-" * 30)
    if secilen_kelime:
        print("KRİTER: Uzunluğu 5'ten büyük olup en çok geçen kelime:")
        print(f"KELİME: '{secilen_kelime}'")
        print(f"TEKRAR: {secilen_adet} kez")
    else:
        print("UYARI: Uzunluğu 5'ten büyük hiç kelime bulunamadı.")
    print("-" * 30)

    # Genel listeyi de görelim (İstersen kapatabilirsin)
    print("\nDiğer Kelimeler (Top 5):")
    for kelime, adet in sirali_liste[:5]:  # Sadece ilk 5 tanesini basar
        print(f"{kelime}: {adet}")
