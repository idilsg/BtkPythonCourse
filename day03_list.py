ogrenci_adi = "İdil"
ogrenci_soyadi = "Gürsoy"
ogrenci_no = 507
ogrenci_cinsiyeti = True
ogrenci_ortalama = 3.21

ogrenci1 = [ogrenci_adi, ogrenci_soyadi, ogrenci_no, ogrenci_cinsiyeti, ogrenci_ortalama]
print(ogrenci1)  # ['İdil', 'Gürsoy', 507, True, 3.21]
print(type(ogrenci1))  # list

ogrenci2 = ["Ertuna", "Aykaç", "434", False, 2.70]
print(ogrenci2)  # ['Ertuna', 'Aykaç', '434', False, 2.7]
print(type(ogrenci2))  # list

print(ogrenci1[0])  # İdil
print(type(ogrenci1[0]))  # str
print(len(ogrenci1))  # 5
print(ogrenci1[:3])  # ['İdil', 'Gürsoy', 507]
print("İdil" in ogrenci1)  # True
print("Ertuna" in ogrenci1)  # False

print("\n")

x = list()
print(x)  # [] (boş liste)

print("\n")

isim = "Lidya"
isim_harfleri = list(isim)
print(isim_harfleri)  # ['L', 'i', 'd', 'y', 'a']
print(len(isim_harfleri))  # 5
yeni = str(isim_harfleri)
print(yeni)  # ['L', 'i', 'd', 'y', 'a']
print(len(yeni))  # 25

print("\n")

meyveler = ["elma", "armut", "kavun", "erik", "kiraz"]
print(meyveler)  # ['elma', 'armut', 'kavun', 'erik', 'kiraz']

meyveler.append("uzum")  # değişken ekleme
print(meyveler)  # ['elma', 'armut', 'kavun', 'erik', 'kiraz', 'uzum']

print(meyveler.count("erik"))  # 1
print(meyveler.index("kavun"))  # 2

meyveler.insert(3, "nar")
print(meyveler)  # ['elma', 'armut', 'kavun', 'nar', 'erik', 'kiraz', 'uzum']

meyveler[5] = "mandalina"
print(meyveler)  # ['elma', 'armut', 'kavun', 'nar', 'erik', 'mandalina', 'uzum']

meyveler.sort()  # alfabetik olarak sıralar
print(meyveler)  # ['armut', 'elma', 'erik', 'kavun', 'mandalina', 'nar', 'uzum']

meyveler.reverse()  # ters alfabetik olarak sıralar
print(meyveler)  # ['uzum', 'nar', 'mandalina', 'kavun', 'erik', 'elma', 'armut']

yeni_meyveler = ["kivi", "ahududu"]
meyveler.extend(yeni_meyveler)
print(meyveler)  # ['uzum', 'nar', 'mandalina', 'kavun', 'erik', 'elma', 'armut', 'kivi', 'ahududu']

yeni_meyveler2 = ["böğürtlen", "dut"]
meyveler.append(yeni_meyveler2)
print(meyveler)  # ['uzum', 'nar', 'mandalina', 'kavun', 'erik', 'elma', 'armut', 'kivi', 'ahududu', ['böğürtlen', 'dut']]

meyveler.pop()  # silme için
print(meyveler)  # ['uzum', 'nar', 'mandalina', 'kavun', 'erik', 'elma', 'armut', 'kivi', 'ahududu']

meyveler.pop(1)
print(meyveler)  # ['uzum', 'mandalina', 'kavun', 'erik', 'elma', 'armut', 'kivi', 'ahududu']

meyveler.remove("mandalina")
print(meyveler)  # ['uzum', 'kavun', 'erik', 'elma', 'armut', 'kivi', 'ahududu']

del meyveler[4]
print(meyveler)  # ['uzum', 'kavun', 'erik', 'elma', 'kivi', 'ahududu']

meyveler.clear()
print(meyveler)  # []

# del meyveler
# print(meyveler) :meyveler boş olduğu için hata verir

print("\n")

# versiyon 1
urun_sayisi = int(input("kaç tane ürün alacaksınız? "))
urunler = []
for i in range(urun_sayisi):
    print(f"{i + 1}. ürün olarak ne alacaksınız? ")
    urun = input("ürün: ")
    urunler.append(urun)
for urun in urunler:
    print(urun)

print("\n")

# versiyon 2
mesaj = "-listeden çıkmak için x tuşlayınız-"
print(mesaj)
urunler = []
while True:
    urun = input("Ürün girişi yapınız: ")
    if urun.lower() == "x":
        print(f"listeniz: {urunler}")
        break
    elif urun == "":
        continue
    else:
        urunler.append(urun)

print("n")

sebze = ["patates", "soğan"]
meyve = ["ahududu", "böğürtlen"]
sarkuteri = ["bal", "peynir"]
yesillik = ["maydonoz", "roka", "marul"]
pazar_listesi = [sebze, meyve, sarkuteri, yesillik]
print(pazar_listesi)  # [['patates', 'soğan'], ['ahududu', 'böğürtlen'], ['bal', 'peynir'], ['maydonoz', 'roka', 'marul']]
print(len(pazar_listesi))  # 4 (4 tane liste)
print(pazar_listesi[0])  # ['patates', 'soğan'] (0. liste)
print(pazar_listesi[0][1])  # soğan (0. listenin 1. elemanı)
print(pazar_listesi[0][0])  # patates (0. listenin 0. elemanı)
for kategori in pazar_listesi:
    print(kategori)
    for urun in kategori:
        print("\t", urun)










