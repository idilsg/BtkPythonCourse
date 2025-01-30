import math
# import math as m
from math import pi as pi_sayisi, sqrt as karekok

a = math.factorial(5)
print(a)  # 120

b = math.sin(math.radians(90))
print(b)  # 1

c = math.pi
print(c)  # 3.141592653589793

d = math.pow(2, 5)
print(d)  # 32.0

e = math.sqrt(16)
print(e)  # 4.0

x = pi_sayisi
y = karekok(16)
print(round(x, 4), y)  # 3.1416 4.0

print("\n")

import random

print(random.randint(1, 100))  # 1-100 arası rastgele sayı (1 ve 100 dahil)
print(random.random())  # örn: 0.7885570290400251
print(random.randrange(0, 100, 5))  # 0-100 arası 5 aralıklı rastgele sayı (10 dahil değil)

print("\n")

# sayı tahmin etme oyunu
print("Sayı Tahmin Etme Oyunu")
baslangic = 0
bitis = 100
tutulan_sayi = random.randint(baslangic, bitis)
tahmin_sayisi = 5
taban = baslangic
tavan = bitis

while tahmin_sayisi > 0:
    istek = f"{taban} - {tavan} aralığında bir sayı giriniz: "
    tahmin = int(input(istek))
    if tahmin == tutulan_sayi:
        print(f"Tebrikler. Tutulan sayı: {tutulan_sayi}")
        break
    else:
        tahmin_sayisi -= 1
        if tahmin_sayisi == 0:
            print(f"Tahmin hakkınız doldu. Tutulan sayı: {tutulan_sayi}")
            break
        elif tahmin > tutulan_sayi:
            print("Daha küçük bir sayı giriniz.")
            tavan = tahmin
        elif tahmin < tutulan_sayi:
            print("Daha büyük bir sayı giriniz.")
            taban = tahmin
        print(f"Kalan tahmin hakkınız: {tahmin_sayisi}")

print("\n")

# sayı tahmin ettirme oyunu
print("Sayı Tahmin Ettirme Oyunu")

baslangic = 0
bitis = 100
tutulan_sayi = 0
check = False

# sayı tutma bloğu
while not check:
    tutulan_sayi = int(input(f"{baslangic}-{bitis} arasında bir sayı tutunuz: "))
    if tutulan_sayi > bitis or tutulan_sayi < baslangic:
        check = False
        print("Belirtilen aralıkta bir sayı girmediniz.")
    else:
        check = True

print("---")
correct = False
taban = baslangic
tavan = bitis
while not correct:
    tahmin = random.randint(taban, tavan)
    print(f"Tahmin edilen sayı: {tahmin}")
    if tahmin == tutulan_sayi:
        correct = True
        print(f"Buldunuz. Tutulan sayı: {tutulan_sayi}")
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir sayı giriniz.")
        tavan = tahmin
    elif tahmin < tutulan_sayi:
        print("Daha büyük bir sayı giriniz.")
        taban = tahmin
