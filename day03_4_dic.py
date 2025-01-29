treng = {"araba": "car", "kalem": "pencil", "kırmızı": "red"}
print(treng)
print(treng["araba"])

print(treng.values())
print(treng.keys())
print(treng.items())

for dd in treng:
    print(dd, treng[dd])

for key, value in treng.items():
    print(key, "=>", value)

for key, value in zip(treng.keys(), treng.values()):
    print(key, "==", value)

print("\n")

oyuncular = {"bjk": ["silva", "immobile", "mert"],
             "gs": ["mertens", "icardi", "osimhen"],
             "fb": ["dzeko", "livakovic", "osayi"]}
print(oyuncular["gs"])
for i in oyuncular:
    print(i, "takımının oyuncuları : ", oyuncular[i])
    for oyuncu in oyuncular[i]:
        print("\t", oyuncu)
