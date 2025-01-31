class Ogrenci():
    pass


ogrenci1 = Ogrenci()
ogrenci1.ad = "Ertuna"
ogrenci1.soyad = "Aykaç"
print("-", ogrenci1.ad, ogrenci1.soyad)  # - Ertuna Aykaç
print(type(ogrenci1))  # __main__.Ogrenci
print(vars(ogrenci1))  # {'ad': 'Ertuna', 'soyad': 'Aykaç'}

ogrenci2 = Ogrenci()
ogrenci2.ad = "İdil"
ogrenci2.soyad = "Gürsoy"
ogrenci2.bolum = "Yazılım"
print("-", ogrenci2.ad, ogrenci2.soyad, ogrenci2.bolum)  # - İdil Gürsoy Yazılım
print(type(ogrenci2))  # __main__.Ogrenci
print(vars(ogrenci2))  # {'ad': 'İdil', 'soyad': 'Gürsoy', 'bolum': 'Yazılım'}

print("")


def func():
    print("deneme", a)
    global b
    b = 2


a = 1
func()
print(a)
print(b)

print("")


class Kitap():
    ad = ""
    yazar = ""
    basim_yili = ""


kitap1 = Kitap()
kitap1.ad = "Doğu Ekspresinde Cinayet"
kitap1.yazar = "Agatha Christie"
print(kitap1.ad, "-", kitap1.yazar)  # Doğu Ekspresinde Cinayet - Agatha Christie
kitap_bilgileri1 = vars(kitap1)
print(kitap_bilgileri1)  # {'ad': 'Doğu Ekspresinde Cinayet', 'yazar': 'Agatha Christie'}
print(vars(Kitap))

kitap_listesi = []
for i in range(3):
    kitap = Kitap()
    kitap.ad = input("Kitap adını giriniz: ")
    kitap_listesi.append(kitap)

for i in kitap_listesi:
    print(i.ad)

print("")


class Ogrenci2():
    bolum = "bilişim"
    kurs = "btk"

    def __init__(self, ad, soyad, tc):
        print("Öğrenci oluşturuldu.")
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.ortalama = None


    def tam_ad(self):
        self.tamad = self.ad + self.soyad
        return self.tamad


    def __str__(self):
        return self.tam_ad


ogr1 = Ogrenci2("Hilal", "Yelekçi", 12345678910)
print(ogr1.tam_ad())  # HilalYelekçi
print(Ogrenci2.tam_ad(ogr1))  # HilalYelekçi











