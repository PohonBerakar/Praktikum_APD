# # Dictionary

# data_mhs = {
#     "nama" : "ucup",
#     "nim" : 1,
#     "nama" : "micahel"
# }
# print(data_mhs)
# print(data_mhs['nama'])
# print(data_mhs['nim'])

# print(data_mhs.get('kelas', 'tidak tersedia'))
# print("")

# for data in data_mhs:
#     print(data)

# for data_key, value_data in data_mhs.items():
#     print(f"Key : {data_key}\nValue : {value_data}\n")

# data_mhs['alamat'] = "Samarinda"
# data_mhs['alamat'] = "Tenggarong"

# data_mhs.update({"alamat": "Budi"})
# data_mhs.update({"nama": "Yanto"})

# print(data_mhs)

# del data_mhs ["nim"]

# print(data_mhs)

# cache = data_mhs.pop("nama")
# print(data_mhs)
# print(cache,"cache")

# data_mhs['id'] = cache
# print(data_mhs)
# print(len(data_mhs))

# key="apel", "jeruk", "mangag"
# value = 1
# buah= dict.fromkeys(key,value)
# print(buah)

# for value in data_mhs.keys():
#     print(value)

# nilai={
#     "Matematika": 80,
#     "kimia" : 20
# }

# #Nestedd
# mahasawi={
#     "nama": "Samsul",
#     "kelas" : "inforb24",
#     "dosen": {
#         "nama" : "pak awang",
#         "mastkul" : "apd"
#     }
# }
# print(mahasawi["dosen"]["nama"])

datam= [
    {"nama" : "Ucup",
     "role" : "Admin"},
    {"nama" : "Budi",
     "role" : "Kroco"}
]

print("")
print(datam[0])
print(datam[0]["nama"])
print(datam[1]["nama"])
print("")
