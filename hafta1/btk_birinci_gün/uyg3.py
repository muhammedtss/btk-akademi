class Kullanici:
    """
    Base Class (Temel Sınıf):
    Tüm kullanıcıların ortak özelliklerini (isim, email) tutar.
    DRY (Don't Repeat Yourself) prensibi gereği ortak özellikleri burada topladık.
    """
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email

    def bilgi(self):
        # f-string kullanımı ile temiz ve okunabilir string birleştirme.
        return f"İsim: {self.isim} | Email: {self.email}"


class Ogrenci(Kullanici):
    """
    Inheritance (Miras Alma):
    Kullanici sınıfından miras alır, üzerine 'ogrenci_no' ekler.
    """
    def __init__(self, isim, email, ogrenci_no):
        # super() ile üst sınıfın (Kullanici) __init__ metodunu çağırıyoruz.
        # Böylece self.isim ve self.email atamalarını tekrar yazmak zorunda kalmıyoruz.
        super().__init__(isim, email)
        self.ogrenci_no = ogrenci_no

    # Polymorphism (Çok Biçimlilik):
    # Üst sınıftaki 'bilgi' metodunu eziyoruz (Override) ve öğrenciye özel hale getiriyoruz.
    def bilgi(self):
        # SENİN HATAN: Eski kodda 'Ogrenci_isim = self.isim' gibi gereksiz değişkenler tanımlamıştın.
        # Bellek israfı. Direkt self.isim kullanmalısın.
        return f"[Öğrenci] {super().bilgi()} | Numara: {self.ogrenci_no}"


class Ogretmen(Kullanici):
    """
    Ogretmen sınıfı da Kullanici'dan türetilmiştir. Ek olarak 'brans' özelliği vardır.
    """
    def __init__(self, isim, email, brans):
        super().__init__(isim, email)
        self.brans = brans

    def bilgi(self):
        # Yazım hatası düzeltildi: "Merhana" -> "Merhaba" (Profesyonellik detayda gizlidir).
        return f"[Öğretmen] {super().bilgi()} | Branş: {self.brans}"


class Ders:
    """
    Composition (Bileşim):
    Ders sınıfı, içinde bir Ogretmen nesnesi ve notlar sözlüğü barındırır.
    """
    def __init__(self, ders_adi, ogretmen):
        # Encapsulation (Kapsülleme):
        # __notlar değişkeni 'private' yapıldı (baına iki alt çizgi).
        # Sınıf dışından direkt erişilemez, metodlar aracılığıyla yönetilmelidir.
        self.__notlar = {} 
        self.ders_adi = ders_adi
        self.ogretmen = ogretmen

    def not_ekle(self, ogrenci, not_degeri):
        # Validation (Doğrulama): Hatalı veri girişini engelliyoruz.
        if not (0 <= not_degeri <= 100):
            print(f"HATA: {ogrenci.isim} için girilen not ({not_degeri}) geçersiz! (0-100 arası olmalı)")
            return

        # SENİN MANTIĞINDAKİ RİSK: İsimler benzersiz değildir (İki tane 'Ali' olabilir).
        # Doğrusu 'ogrenci.ogrenci_no' kullanmaktır ama şimdilik isme sadık kalıyoruz.
        self.__notlar[ogrenci.isim] = not_degeri
        print(f"Bilgi: {ogrenci.isim} öğrencisine {not_degeri} notu eklendi.")

    def notlari_goster(self):
        # Getter metodu: Private veriyi dışarıya kontrollü açıyoruz.
        return dict(self.__notlar)

    def ortalama(self):
        if not self.__notlar:
            return 0.0
        # Notların toplamını alıp kişi sayısına bölüyoruz.
        return sum(self.__notlar.values()) / len(self.__notlar)


class Platform:
    """
    Sistemi yöneten ana sınıf. Kullanıcıları ve dersleri burada topluyoruz.
    """
    def __init__(self):
        self.kullanicilar = []
        self.dersler = []

    def kullanici_ekle(self, k):
        # Type Checking (Opsiyonel ama önerilir): Gelen veri Kullanici tipinde mi?
        if isinstance(k, Kullanici):
            self.kullanicilar.append(k)
        else:
            print("Hata: Sadece Kullanıcı nesneleri eklenebilir!")

    def ders_ekle(self, d):
        self.dersler.append(d)

    def listele(self):
        print("\n" + "="*30)
        print("PLATFORMDAKİ KULLANICILAR")
        print("="*30)
        for k in self.kullanicilar:
            print(k.bilgi())

        print("\n" + "="*30)
        print("PLATFORMDAKİ DERSLER")
        print("="*30)
        # SENİN HATAN: 'Platformdaki Dersler' yazısını döngü içine koymuştun.
        # Her ders için başlığı tekrar yazdırıyordu. Döngü dışına aldım.
        if not self.dersler:
            print("Henüz ders eklenmemiş.")
        else:
            for d in self.dersler:
                print(f"- {d.ders_adi} (Eğitmen: {d.ogretmen.isim})")


# --- TEST SENARYOSU ---
if __name__ == "__main__":
    
    # 1. Nesneleri Oluştur
    t1 = Ogretmen("Beytullah", "beytullah@btk.com", "Uçuş Eğitimi")
    
    # Dikkat: İki öğrencinin numarası aynıydı, bunu düzelttim. ID benzersiz olmalı.
    s1 = Ogrenci("Muhammed", "muhammed@firat.edu.tr", 240576045)
    s2 = Ogrenci("Diren", "diren@firat.edu.tr", 240576046) 

    # 2. Platformu Başlat
    plt = Platform()

    # 3. Kullanıcıları Kaydet
    plt.kullanici_ekle(t1)
    plt.kullanici_ekle(s1)
    plt.kullanici_ekle(s2)

    # 4. Ders Oluştur ve İşlemler Yap
    btk_python = Ders("BTK Python Eğitimi", t1)
    
    # SENİN UNUTTUĞUN ADIM: Dersi oluşturdun ama platform listesine eklememiştin.
    plt.ders_ekle(btk_python) 

    btk_python.not_ekle(s1, 85)
    btk_python.not_ekle(s2, 25)
    btk_python.not_ekle(s1, 150) # Hatalı not testi

    # 5. Raporlama
    plt.listele()

    print(f"\n--- {btk_python.ders_adi} Detayları ---")
    print(f"Not Listesi: {btk_python.notlari_goster()}")
    print(f"Sınıf Ortalaması: {btk_python.ortalama():.2f}") # .2f ile virgülden sonra 2 basamak