from day06_2_sql import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def birim_listele():
    birimler = session.query(Birim).all()
    for birim in birimler:
        print(birim.birimId, birim.birimAdi)
    return birimler


def birim_ekle():
    birimAdi = input("Birim adı giriniz: ")
    yeni_birim = Birim(birimAdi=birimAdi)
    session.add(yeni_birim)
    session.commit()


def birim_sil():
    birim_listele()
    birimId = int(input("Silinecek birim id giriniz: "))
    birim = session.query(Birim).filter(Birim.birimId == birimId).delete()
    session.commit()
    return birim_listele()


while True:
    cevap = input("e, l, s, x ")
    if cevap == "e":
        birim_ekle()
    elif cevap == "l":
        birim_listele()
    elif cevap == "s":
        birim_sil()
    elif cevap == "x":
        exit()
