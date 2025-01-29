baslangic = 2
bitis = 5
toplam = 0
carpim = 1

for i in range(1, bitis + 1):  # bitiş dahil olsun diye 1 ekledik
    toplam = toplam + i
    print("sıra:", i, toplam, "(toplam)")
    carpim = carpim * i
    print("sıra:", i, carpim, "(çarpım)")
print("Genel toplam:", toplam)

# sıra: 1 1 (toplam)
# sıra: 1 1 (çarpım)
# sıra: 2 3 (toplam)
# sıra: 2 2 (çarpım)
# sıra: 3 6 (toplam)
# sıra: 3 6 (çarpım)
# sıra: 4 10 (toplam)
# sıra: 4 24 (çarpım)
# sıra: 5 15 (toplam)
# sıra: 5 120 (çarpım)
# Genel toplam: 15

print("\n")

# while döngüsü
i = 0
while i < 5:
    i += 1
    print(i)
print("döngü sonu:", i)  # döngü sonu: 5

print("\n")

pizza_dilimi = int(input("Kaç dilim pizza istersiniz? "))

adet_azalan = pizza_dilimi
i = 1
while adet_azalan > 0:
    print(f"{i}. pizza dilimi")
    adet_azalan = adet_azalan - 1
    i += 1

print("***")

adet_artan = pizza_dilimi
j = 1
while j <= adet_artan:
    print(f"{j}. pizza dilimi")
    j += 1

print("\n")

cevap = bool(input("Pizza ister misiniz? "))
# cevap inputu girildiğinde çalışıyor
while cevap:  # cevap == True da yazılabilir
    print("Pizza isteniyor.")
    break  # döngü durdurulur

print("\n")

# sıfırdan farklı 10 adet sayının çarpımı
i = 0
carpim = 1
while i < 10:
    sayi = int(input("Sıfırdan farklı bir sayı giriniz: "))
    if sayi == 0:
        print("Geçersiz sayı girdiniz.")
    else:
        print(f"{i + 1}. sayı: {sayi}")
        carpim = carpim * sayi
        print(f"Sıra {i + 1}: çarpım {carpim}")
        i += 1

print("\n")

# 5'e kadar çarpım tablosu
for x in range(1, 6):
    print(x, "ler")
    for y in range(1, 6):
        print("\t {}*{}={}".format(x, y, x*y))












