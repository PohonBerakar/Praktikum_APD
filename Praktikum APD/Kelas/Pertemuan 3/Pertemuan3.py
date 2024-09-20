cuaca = "mendung"
if cuaca == "cerah" :
     print("kamu pergi keluar rumah")

#variable akan bernilai false jika string kosong, 0, [], (), {}, false
uang = "true"
if uang : 
     print("pergi ke pasar!")
else :
     print("pergi kerumah teman")

nilai = 70

if nilai < 70 :
     print(" Tidak Lulus")
else: 
     print("Lulus")

#menentukan bilangan positif atau negatif
nilai = int(input("Masukkan Bilangan : "))
if nilai < 0 :
     print("Bilangan Negatif")
else : 
     print("Bilangan Positif")

#Percabangan dengan banyak kondisi
umur = int(input("Masukkan umur anda : "))
if umur <= 10:
     print("anak anak")
elif umur <= 18:
     print("Remaja")
elif umur <= 35:
     print ("Dewasa")
elif umur <= 65:
     print("Paruh baya")
else :
     print ("Tua")

nilai = 90
if nilai >= 80 :
    if nilai>=85 :
          print("nilai A+")
    else:
         print("Nilai A-")
else : 
     print("Tidak lulus")

#Pilihan Menu

print("Menu")
print("1. Nonton Film")
print("2. Ngoding")
print("3. Keluar")

menu= int(input("Pilih Menu Anda"))
if menu==1 :
     print("Sedang Nonton Film")
elif menu==2 :
     print("Sedang Ngoding")
elif menu==3 :
     print("Sedang Keluar")
else:
     print("Menu tidak tersedia")

#Perkodisian Pertama

angka= int(input("Masukkan angka"))

if angka %2 == 0 :
     print("Genap")
if angka > 0:
     print("Bilangan Positif")

#Perkondisian Kedua

if angka % 2 ==0:
     print("Genap")
elif angka > 0:
     print("Bilangan Positif")
