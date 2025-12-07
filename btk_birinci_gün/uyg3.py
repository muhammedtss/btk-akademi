class Kullanici:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email

    def bilgi(self):
    
        return f"kullanıcı isim:  {self.isim} \n Kullanıcı email: {self.email}"
class Ogrenci(Kullanici):
    def __init__(self, isim, email, ogrenci_no):
        super().__init__(isim, email)
        self.ogrenci_no = ogrenci_no

    def bilgi(self):
        Ogrenci_isim = self.isim
        Ogrenci_email = self.email
        Ogrenci_no = self.ogrenci_no
        return f"Merhana adım: {Ogrenci_isim}, mail adresim: {Ogrenci_email} ve öğrenci numaram: {Ogrenci_no}"
    

class Ogretmen(Kullanici):
    def __init__(self, isim, email, brans):
        super().__init__(isim, email)
        self.brans = brans


    def bilgi(self):
        Ogretmen_isim = self.isim
        Ogretmen_email = self.email
        Ogretmen_brans = self.brans
        return f"Merhana adım: {Ogretmen_isim}, mail adresim: {Ogretmen_email} ve branşım: {Ogretmen_brans}"
    
class Ders:
    def __init__(self, ders_adi, ogretmen):
        self.__notlar = {}
        self.ders_adi = ders_adi
        self.ogretmen = ogretmen

    def not_ekle(self, ogrenci, not_degeri):
        if 0<= not_degeri <= 100:
            self.__notlar[ogrenci.isim] = not_degeri
        else:
            print("Hata: Not değeri 0 ile 100 arasında olmalıdır.")
        
    def notlari_goster(self):
        return dict(self.__notlar)
    
    def ortalama(self):
        if not self.__notlar:
            return 0
        return sum(self.__notlar.values()) / len(self.__notlar)
    

class Platform:
    def __init__(self):
        self.kullanicilar = []
        self.dersler = []

    def kullanici_ekle(self, k):
        self.kullanicilar.append(k)
    def ders_ekle(self, d):
        self.dersler.append(d)
    
    def listele(self):
        print(f"Platformdaki Kullanıcılar:")
        for k in self.kullanicilar:
            print(k.bilgi())

        for d in self.dersler:
            print(f"\nPlatformdaki Dersler: {d.ders_adi}")


if __name__ == "__main__":
    
    t1 = Ogretmen("Beytullah","beytullah@btk.com","Uçuş Eğitimi")
    s1 = Ogrenci("Muhammed","muhammed@firat.edu.tr",240576045)
    s2= Ogrenci("Diren","diren@firat.edu.tr",240576045)


    plt = Platform()

    plt.kullanici_ekle(t1)
    plt.kullanici_ekle(s1)
    plt.kullanici_ekle(s2)

    btk_python = Ders("BTK Python Eğitimi",t1)
    btk_python.not_ekle(s1,85)
    btk_python.not_ekle(s2,25)

    plt.listele() 

    print(f"\nDers Notları: {btk_python.notlari_goster()}")
    print(f"Dersin Not Ortalaması: {btk_python.ortalama()}")


            
    