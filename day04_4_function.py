def selamla1(ad1, ad2):
    print(f"selam {ad1} ve {ad2}, kursumuza hoşgeldin.")


a = selamla1("idil", "ertuna")
print(a)  # void döndürdüğü için (void = doesn't return anything) a = None
print(type(a))  # NoneType

print("---")


def selamla2(ad3):
    print(f"selam {ad3}, kursumuza hoşgeldin.")
    return "fonksiyon çalıştırıldı."


b = selamla2("mustafa")
print(b)  # fonksiyon çalıştırıldı. (fonksiyon void döndürmüyor)
print(type(b))  # str (döndürdüğünün type'ı)

print("\n")


def toplama(i, j):
    return i + j


sonuc = toplama(3, 5)
print(sonuc)  # 8


def yas_hesapla(dogum_yili):
    yas = 2025 - dogum_yili
    return yas


kullanici_yasi = yas_hesapla(2004)
print(kullanici_yasi)  # 21

print("\n")


# toplama çıkarma programı
def toplam(x, y):
    return x + y


def fark(x, y):
    return x - y


def islem_yapma(islem, sayi1, sayi2):
    match islem:
        case "+":
            print(toplam(sayi1, sayi2))
        case "-":
            print(fark(sayi1, sayi2))
        case "x":
            exit()
        case _:
            print("hatalı işlem seçimi")


def program():
    islem = input("Bir işlem seçiniz (+, -), çıkış için x: ")
    # hata: x yazıldığında program durmuyor.

    def sayi_sor():
        return int(input("Sayı giriniz: "))
    sayi1 = sayi_sor()
    sayi2 = sayi_sor()
    islem_yapma(islem, sayi1, sayi2)
    return program()


if __name__ == "__main__":
    print("Programa hoşgeldiniz.")
    program()

print("\n")


def daire_alani(r=1, pi=3.14):
    alan = pi * (r**2)
    return alan


d_alan = daire_alani(3, 3.45)
print(d_alan)


def ortalama(*args):
    print(args, type(args))
    print(*args)
    toplamx = 0
    for i in args:
        toplamx += i
    sonucx = toplamx / len(args)
    return sonucx


s_ortalama = ortalama(1, 2, 3, 4, 5)
print(s_ortalama)
