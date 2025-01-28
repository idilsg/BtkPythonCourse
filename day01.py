print('first commit')

# tek satır yorum

"""
çok satırlı
yorum 
"""

print("\n")  # sonraki satıra geçmek için

# temel veri tipleri
print(41)
print(type(41))  # int
print(type(7.04))  # float
print(type(7.0))  # float

print("bu kurs \"izmir\" ilinde düzenleniyor.")
print("bu kurs 'izmir' ilinde düzenleniyor.")
print("bu kurs \tizmir ilinde düzenleniyor.")
print("bu kurs \nizmir ilinde düzenleniyor.")

print(True)
print(type(True))  # bool

print("\n")

# aritmetiksel operatörler
print(7 + 2)  # 9
print(7 - 2)  # 5
print(7 * 2)  # 14
print(7 / 2)  # 3.5
print(7 ** 2)  # 49 (power işlemi)
print(7 % 2)  # 1 (bölümden kalan, mod)
print(7 // 2)  # 3 (bölümün tam kısmı)

print("abc " * 3)  # abc abc abc
print("abc" + "def")  # abcdef
print("abc", "def")  # abc def
print("abc" + "1")  # abc1

print("\n")

# karşılaştırma operatörleri
print(3 == 5)  # False
print(7 == 7)  # True
print(4 != 4)  # False
print("özlem" == "dilara")  # False
print("besti" == "besti")  # True
print("ırmak" != "esin")  # True
print(False == False)  # True
print("1" == 1)  # False
print(1 > 2)  # False
print(1 <= 2)  # True

print((55 == 45) and (8 > 4))  # False (0 ∧ 1 = 0)
print((55 == 45) or (8 > 4))  # True (0 v 1 = 1)
print(not (55 == 88))  # True (~0 = 1)

print("\n")

isim = "Ertuna"
print(isim)  # Ertuna
print(type(isim))  # str

sayi = 7
print(sayi)  # 7
print(type(sayi))  # int

print(sayi == 10)  # 7 != 10, False
print(sayi * 4)  # 7 * 4 = 28

isim = "İdil"
soyisim = "Gürsoy"
tam_isim = isim + " " + soyisim
print(tam_isim)  # İdil Gürsoy

sayi = 10
print(sayi)  # 10
# sayi = sayi*2
sayi *= 2
print(sayi)  # 10 * 2 = 20

isim = "idil "
isim += "gürsoy "
print(isim)  # idil gürsoy
isim *= 3
print(isim)  # idil gürsoy idil gürsoy idil gürsoy

sayi = 5
print(sayi * 2, type(sayi))  # 10 int
yeni_sayi = str(sayi)
print(yeni_sayi * 2, type(yeni_sayi))  # 55 str

print("\n")

isim = input("İsminizi giriniz: ")  # kullanıcıdan input alır (default str)
yas = int(input("Yaşınızı giriniz: "))  # kullanıcıdan input alır ama int
sonuc = isim * yas
print(sonuc)  # isimisimisim (boşluksuz print eder yani)

