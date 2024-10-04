#List
data = [1, 2, 3, 4, True,[1,2],"adi"]
data_2 = list((1,2,3,4,5))

print(type(data))
print(data)
print(data[6])
print(data[5][0])


# penambahan data
datab=["Apel","Jeruk","Durian"]
print(datab)
print()
datab.append("Semangka")
print(datab)
print()
datab.insert(0,"Rambutan")
print(datab)
print()
datab.extend(["Jambu","Anggur"])
print(datab)
print()
print(len(datab))
print()
datab[1]="Hewan"
print()
print(datab)
print()

#hapus data
del datab[3]
print(datab)
print()
datab.pop(4)
print(datab)
print()
print(datab[4])
print()
datab.remove("Jeruk")
print(datab)

data_mahasiswa= [
    ["060","Ifnu",["APD","ORSIKOM"]],
    ["065","Adi"]
]
print(data_mahasiswa[0][1])
print()
print(data_mahasiswa[0][2][0])
print()

buah=["Apel","Durian","Jeruk"]
index=1
for duta in buah:
    print(f"Data ke {index}")
    print(duta)
    print("="*10)
    index=index+1

indexz=1
for indexz, item in enumerate(buah):
    print(f"Data ke {indexz+1}")
    print(item)

#topel