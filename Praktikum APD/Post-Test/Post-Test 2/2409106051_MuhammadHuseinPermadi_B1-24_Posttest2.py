print("Input Biodata Diri")
nama = str(input("Masukkan Nama : "))
umur = int(input("Masukkan Umur anda : "))
kelas = str(input("Masukkan Kelas A/B/C : "))
angkatan = int(input("Masukkan angkatan anda : "))
panjang = float(input("Masukkan Panjang badan anda : "))
berat = float(input("Masukkan Berat badan anda : "))

print("Biodata Anda")
print(f"Nama      :  {nama}")
print(f"Umur      :  {umur}")
print(f"Kelas     :  {kelas}")
print(f"Angkatan  :  {angkatan}")
print(f"Panjang   :  {panjang} cm")
print(f"Berat     :  {berat} Kg")
#Boolean
print(f"Apakah umur 18 atau lebih?  {umur>=18}")
#Jumlah int dan float
print (f"Total penjumlahan semua int dan float adalah : {umur + angkatan + panjang + berat}")