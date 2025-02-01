import json

x = '{"ad": "Irmak", "soyad": "Soguksu", "sehir": "Ankara"}'

bilgiler = json.loads(x)

print(bilgiler)  # {'ad': 'Irmak', 'soyad': 'Soguksu', 'sehir': 'Ankara'}
print(type(bilgiler))  # dict

for bilgi in bilgiler:
    print(bilgi, bilgiler[bilgi])
# ad Irmak
# soyad Soguksu
# sehir Ankara

bilgiler["yas"] = 22

z = json.dumps(bilgiler)
print(z)  # {"ad": "Irmak", "soyad": "Soguksu", "sehir": "Ankara", "yas": 22}
print(type(z))  # str

print("")


class Ogrenci():
    def __init__(self, kwargs):
        self.name = kwargs["name"]
        self.city = kwargs["city"]
        self.age = kwargs["age"]


ogrenci1_bilgi = {"name": "Ezgi", "city": "Istanbul", "age": 17}
ogrenci1 = Ogrenci(ogrenci1_bilgi)
print(ogrenci1.age)  # 17

ogr_bilgileri = ('{"1": {"name": "Ezgi", "city": "Izmir", "age": 20},'
                 ' "2": {"name": "Mina", "city": "Ankara", "age": 24}}')

ogrenci_listesi = []
json_data = json.loads(ogr_bilgileri)
print(json_data)  # {'1': {'name': 'Ezgi', 'city': 'Izmir', 'age': 20}, '2': {'name': 'Mina', 'city': 'Ankara', 'age': 24}}
for data in json_data:
    print(data, json_data[data])
    # 1 {'name': 'Ezgi', 'city': 'Izmir', 'age': 20}
    # 2 {'name': 'Mina', 'city': 'Ankara', 'age': 24}
    ogr = Ogrenci(json_data[data])
    ogrenci_listesi.append(ogr)

print(ogrenci_listesi)  # [<__main__.Ogrenci object at 0x0000027243EC1E20>, <__main__.Ogrenci object at 0x0000027243EC1E50>]



