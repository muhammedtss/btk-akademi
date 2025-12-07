import string


def cumle_analizi(file_name): #DOSYAYI OKUTMA FONKSİYONUNU OLUŞTURDUK
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content: str = f.read()
    except FileNotFoundError:
        print(f"HATA: '{file_name}' bulunamadı.")
    for p in string.punctuation: #NOKTALAMA İŞARETLERİNİ TEMİZLEDİK
        text = filter.replace(p, " ") #değişebilir!!!!

    words = text.lower().split() #KÜÇÜK HARFE ÇEVİRİP KELİMELERE AYIRDIK

    if not words:
        print("UYARI: Dosya boş veya kelime bulunamadı.")
        return

    counts = {}
    for w in words: #KELİMELERİ SAYDIK
        counts[w] = counts.get(w, 0) + 1

    toplam_kelime = len(words)
    toplam_benzersiz_kelime = len(counts)
    print(f"\n--- Analiz Edilen Toplam Kelime Sayısı: {toplam_kelime}.Benzersiz kelime sayısı {toplam_benzersiz_kelime} ---")


    top3 = sorted(counts.items(), key=lambda x: (x[1],x[0]), reverse=True)[:3]
    print("EN ÇOK GEÇEN 3 KELİME:")

    uzun_kelimeler = {w: c for w, c in counts.items() if len(w) > 5}
    en_uzun_kelimeler = max(uzun_kelimeler, key=lambda x: (x[1], len(x[0])), default=0, reverse=True)


    alpha_kelimeler = {w:c for w,c in counts.items() if w.isalpha()}
    en_uzun_alpha = max(alpha_kelimeler, key=lambda x: (x[1],x[0]), default=("yok",0), reverse=True)