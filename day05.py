"""
dosya = open("ornek.txt")
icerik = dosya.read()

print(icerik)

print(type(icerik))  # str
print(icerik[:6])  # 6. karaktere kadar

# sırayla tek tek dosyadaki satırları okuyor
# kodun önceki kısmında dosyayı zaten okuttuğumuz için istediğimiz gibi çalışmayacaktır
# çalışması için önceki kodları comment içine almalıyız
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())

# tüm satırları okuyor
# kodun önceki kısmında dosyayı zaten okuttuğumuz için istediğimiz gibi çalışmayacaktır
# çalışması için önceki kodları comment içine almalıyız
print(dosya.readlines())

# tüm satırları okuyor
# kodun önceki kısmında dosyayı zaten okuttuğumuz için istediğimiz gibi çalışmayacaktır
# çalışması için önceki kodları comment içine almalıyız
satirlar = dosya.readlines()
for satir in satirlar:
    print(satir, end="")

print("\n")

# eğer yukarıdaki gibi "dosya zaten okundu" problemiyle karşılaşmak istemiyorsak:
dosya_adi = "ornek.txt"
with open(dosya_adi) as dosya:
    print(dosya.readlines())

with open(dosya_adi) as dosya:
    print(dosya.readlines())

# output:
# ['idil gursoy\n', 'yazilim muhendisligi\n', '3. sinif\n', '20220601040']
# ['idil gursoy\n', 'yazilim muhendisligi\n', '3. sinif\n', '20220601040']

print("\n")
"""

# önceki kısmı comment içine alıp çalıştır
import os
import time

dosya_adi_2 = "ornek.txt"
with open(dosya_adi_2, "a") as dosya:
    dosya.write("\nsinif basari sirasi 1")  # her çalıştırdığımızda dosyanın üzerine ekleniyor.

with open(dosya_adi_2, "r") as dosya:
    print(dosya.read())

dosya_adi_2 = "ornek2.txt"
with open(dosya_adi_2, "w") as dosya:
    dosya.write("sinif basari sirasi 1")  # dosyadaki yazıları silip bunu yazıyor.

with open(dosya_adi_2, "r") as dosya:
    print(dosya.read())





dosya.close()










