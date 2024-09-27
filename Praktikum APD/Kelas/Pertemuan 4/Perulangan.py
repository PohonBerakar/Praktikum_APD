#perulangan for

print("perulangan ke-0")

batas = 5
for i in range(batas):
    print(f"Perulangan ke-{i}")

batas1 = 5
for i in range(1, batas1):
    print(f"Perulangan 2 ke-{i}")

batas2 = 10
for i in range(1, batas2 ,3):
    print(f"Perulangan 3 ke-{i}")

buah = ["Apel", "Mangga", "Anggur"]
for i in buah:
    print(i)

buah_banyak = ["Apel", "Mangga", "Anggur"]
for buah in buah_banyak:
    print(buah)

#perulangan for didalam for

for baris in range(1,4):
    print("Baris ke",baris)
    for kolom in range(1,4):
        print(kolom,"kolom", end=" ")
    print()
    print()

#Perulangan While

#while True:
    #print("Hello")

lagi="yes"
ulang= 0
while lagi=="yes":
    print("Mabar")
    lagi=input("Mabar lagi ga?")
    ulang+=1
print("Selesai Mabar")
print(f"Perulangan terjadi sebanyak {ulang} kali")

for i in range(1,10):
    if i ==4:
        break
    else:
        print(f"Perulangan ke {i}")

buah_banyakk=["Anggur", "Apel", "Kucing", "Ayam", "Semangka"]



while True:
    ulang=input("Mabar lagi ga? ")
    if ulang=="ga":
        break
    print("Mabar Lagi? ")

#Continue

for i in range(1,10):
    if i == 4:
        continue
    print(f"Perulangan ke-{i}")

#sistem autentikasi
kesempatan=3
while kesempatan > 0:
    username=input("Masukkan Username ")
    password=input("Masukkan Password ")

    if username=="admin" and password=="admin#1234":
        print("Berhasil Login")
        break
    else:
        print("Username atau Password salah!")
        kesempatan-=1
        print(f"Kesempatan login tersisa {kesempatan} kali")
print("Masuk Program")