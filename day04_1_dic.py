# dictionary devam
menu = {"Çorbalar": {"etli": ["işkembe", "kelle paça"],
                     "sebzeli": ["brokolili", "domates"]},
        "Yemekler": {"pizza": ["margarita", "mozarella"],
                     "makarna": ["fettucini", "arabiata"],
                     "pide": ["kıymalı", "kaşarlı"]},
        "İçecekler": ["kola", "ice tea", "su"]}

print(menu["Yemekler"]["pizza"])  # ['margarita', 'mozarella']

menu["Yemekler"]["pide"].append("kuşbaşı")
print(menu["Yemekler"]["pide"])  # ['kıymalı', 'kaşarlı', 'kuşbaşı']

menu["Çorbalar"]["etli"] = {"dana": ["ayakpaça"],
                            "kuzu": ["tirit"]}
print(menu["Çorbalar"]["etli"])  # {'dana': ['ayakpaça'], 'kuzu': ['tirit']}

sutlu_tatli = ["profiterol"]
menu["Tatlılar"] = {"sütlü tatlılar": sutlu_tatli}
print(menu)  # menünün sonuna tatlılar kategorisi eklendi, tüm menüyü yazdırdık

menu["Tatlılar"]["şerbetli tatlılar"] = ["künefe"]
print(menu)  # tatlılara yeni alt kategori eklendi, tüm menüyü yazdırdık

sutlu_tatli.append("magnolia")
print(menu["Tatlılar"])  # {'sütlü tatlılar': ['profiterol', 'magnolia'], 'şerbetli tatlılar': ['künefe']}

print("\n")

for ana_kategori in menu:
    print(ana_kategori)
    if type(menu[ana_kategori]) is dict:
        for alt_kategori1 in menu[ana_kategori]:
            print("\t", alt_kategori1)
            if type(menu[ana_kategori][alt_kategori1]) is dict:
                for alt_kategori2 in menu[ana_kategori][alt_kategori1]:
                    print("\t\t", alt_kategori2)
                    for alt_kategori3 in menu[ana_kategori][alt_kategori1][alt_kategori2]:
                        print("\t\t\t", alt_kategori3)
            else:
                print("\t\t", menu[ana_kategori][alt_kategori1])
    else:
        print("\t", menu[ana_kategori])












