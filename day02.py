# if - else
isim = "mina"

if isim == "mina":  # koşul True ise bu blok çalışır
    print("isim mina'dır")
else:  # yukarıdaki koşul False ise bu blok çalışır
    print("isim mina değildir")
# output: isim mina'dır

if isim == "ayça" or isim == "ezgi":
    print("isim bu ikisinden biri")
else:
    print("isim bu ikisinden biri değil")
# output: isim bu ikisinden biri değil

print("\n")

dogum_yili = int(input("Doğum yılınızı giriniz: "))
yas = 2025 - dogum_yili
if yas >= 18:
    print("Ehliyet alabilecek yaştasınız.")
if yas < 18:
    print(f"Ehliyet almak için {18 - yas} yıl beklemelisiniz.")

print("\n")

yemek = "pide"
icecek = "ayran"
if yemek == "lahmacun" and icecek == "ayran":  # tüm koşulun True olması için ikisi de True olmalı
    print("Siparişiniz lahmacun ve pidedir.")
else:  # koşullardan en az biri False ise bu kod çalışır
    print(f"{yemek} ve {icecek} siparişi doğru değildir.")

print("\n")

yemek = input("Yemek bilgisi giriniz: ")
if yemek == "pide":
    icecek = input("İçecek siparişi giriniz: ")
    if icecek == "ayran":
        print(f"{yemek} ve {icecek} siparişi doğrudur.")
    else:
        print(f"{yemek} siparişi doğrudur fakat {icecek} siparişi doğru değildir.")
else:
    print("Sipariş doğru değildir.")

print("\n")

# elif = else if
# ilk koşul sağlanmadı, yeni koşul yazılıyor
puan = int(input("Ortalamanızı giriniz: "))
if puan < 0 or puan > 100:
    print("Geçerli bir not girilmedi.")
elif puan < 70:
    print("Belge kazanamadınız.")
elif puan < 85:
    print("Teşekkür belgesi kazandınız.")
else:
    print("Takdir belgesi kazandınız.")

print("\n")

# çoklu değişken tanımlama
a = 12
b = 24
print(a, b)  # 12 24
a, b = b, a
print(a, b)  # 24 12

# java gibi bazı dillerde bu işlem için geçici bir değişken tanımlanır (temp)
# python'da geçici değişken tanımlamaya gerek yoktur, kısa yolla yapabiliriz.
# yukarıdaki açıklamanın örneği:
a = 12
b = 24
print(a, b)  # 12 24
temp = a
a = b
b = temp
print(a, b)  # 24 12

# kısa if yazımı
a = 1
if a < 5:
    b = "küçük"
else:
    b = "büyük"

b = "büyük" if a >= 5 else "küçük"

print("\n")

renk = input("Bir renk giriniz: ")
match renk:
    case "kırmızı":
        print("Seçtiğiniz renk kırmızıdır.")
    case "mavi":
        print("Seçtiğiniz renk mavidir.")
    case "sarı":
        print("Seçtiğiniz renk sarıdır.")
    case _:
        print("Seçtiğiniz renk listede yoktur.")

print("\n")

ad = "idilgürsoy"
print(len(ad))  # 10
print(ad[0])  # i
print(ad[-1])  # y
print(ad[5], ad[-7])  # ü l
print(ad[-5], ad[2])  # ü i
print(ad[0:5])  # idilg
print(ad[:7])  # idilgür
print(ad[5:7])  # ür
print(ad[5:])  # ürsoy
print(ad[0:7:1])  # idilgür
print(ad[0:7:2])  # iigr
print(ad[-7:-5])  # lg
print(ad[-7:-4:2])  # lü
print(ad[::])  # idilgürsoy
print(ad[::-1])  # yosrüglidi
print(ad[-5:-7:-1])  # üg
print("g" in ad)  # True
print("ilg" in ad)  # True

print("\n")

ad1 = "zeynep"
ad2 = "sueda"
ad3 = "hilal"

print(ad1 + ad2 + ad3)  # zeynepsuedahilal
print(f"{ad1} {ad2} {ad3}")  # zeynep sueda hilal

metin = "Merhaba sayın {} kursumuza hoşgeldin"
print(metin.format(ad1))  # Merhaba sayın zeynep kursumuza hoşgeldin
print("hoşgeldin {}".format(ad1))  # hoşgeldin zeynep

metin2 = "yarışmamızın başarı listesi {}, {}, {}"
print(metin2.format(ad2, ad3, ad1))  # yarışmamızın başarı listesi sueda, hilal, zeynep

metin3 = "{k1}, Merhaba {k1}, {k2}, {k3}".format(k1=ad1, k2=ad2, k3=ad3)
print(metin3)  # zeynep, Merhaba zeynep, sueda, hilal
print(metin3.capitalize())  # Zeynep, merhaba zeynep, sueda, hilal
print(metin3.count("an"))  # 2

print("\n")

print("zeynep", "sueda", "hilal")  # zeynep sueda hilal
print("zeynep", "sueda", "hilal", sep="*")  # zeynep*sueda*hilal
print("zeynep", "sueda", "hilal", end="-")
print("zeynep", "sueda", "hilal")  # zeynep sueda hilal-zeynep sueda hilal
print("zeynep", "sueda", "hilal", sep="---", end="\t")
print("zeynep", "sueda", "hilal")  # zeynep---sueda---hilal     zeynep sueda hilal

print("\n")

print(list(range(10)))
for dd in range(1, 3):  # (baslangıç : bitiş : artış)
    print(dd, ". sıra")
# 1 . sıra
# 2 . sıra

for harf in "abc":
    print(harf)
# a
# b
# c

for dd in range(2, 8, 3):  # 8 dahil değil
    print(dd)
# 2
# 5

ad = "abcdefghi"
for dd in ad[5:]:
    print(dd, end=" - ")
# f - g - h - i -
