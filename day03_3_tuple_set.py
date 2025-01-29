# tuple
info = "aslı", "sena"
print(info)  # ('aslı', 'sena')
print(type(info))  # tuple
info2 = ("ela",)
print(info2)  # ('ela',)
print(type(info2))  # tuple

# set
kisiler = {"melisa", "sıla", "özge", "lara"}
print(kisiler)  # {'sıla', 'melisa', 'lara', 'özge'}
kisiler.add("merve")
print(kisiler)  # {'merve', 'lara', 'sıla', 'melisa', 'özge'}
kisiler.add("ceren")
print(kisiler)  # {'merve', 'lara', 'sıla', 'melisa', 'özge'}

if "merve" in kisiler:
    print("merve kümede")

for i in kisiler:
    print(i)
# merve
# lara
# ceren
# sıla
# melisa
# özge
