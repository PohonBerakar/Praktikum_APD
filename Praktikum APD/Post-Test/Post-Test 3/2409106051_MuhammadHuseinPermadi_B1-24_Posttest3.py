print("""Menghitung Bangun Datar
Silahkan pilih bangun datar yang ingin dihitung!
1. Persegi
2. Persegi Panjang
3. Segitiga
4. Lingkaran
5. Jajar Genjang""")

hitung= int(input("Pilih salah satu yang ingin anda hitung! (Pilih Menggunakan angka) "))

if hitung==1:
    print("""1. Luas
2. Keliling""")
    hitung2=int(input("Apa yang ingin anda hitung? "))
    if hitung2==1:
        angka=float(input("Masukkan panjang Persegi(cm) "))
        print(f"Luas Persegi adalah : {angka*angka} cm")
    elif hitung2==2:
        angka=float(input("Masukkan panjang Persegi(cm) "))
        print(f"Keliling Persegi adalah : {angka*4} cm")
    else:
        print("Mohon maaf pilihan anda tidak tersedia saat ini")

elif hitung==2:
    print("""1. Luas
2. Keliling""")
    hitung2=int(input("Apa yang ingin anda hitung? "))
    if hitung2==1:
        angka=float(input("Masukkan Panjang Persegi Panjang(cm) "))
        angka2=float(input("Masukkan Lebar Persegi Panjang(cm) "))
        print(f"Luas Persegi adalah : {angka*angka2} cm")
    elif hitung2==2:
        angka=float(input("Masukkan Panjang Persegi Panjang(cm) "))
        angka2=float(input("Masukkan Lebar Persegi Panjang(cm) "))
        print(f"Keliling Persegi Panjang adalah : {(2*angka)+(2*angka2)} cm")
    else:
        print("Mohon maaf pilihan anda tidak tersedia saat ini")

elif hitung==3:
    print("""1. Luas
2. Keliling""")
    hitung2=int(input("Apa yang ingin anda hitung? "))
    if hitung2==1:
        angka=float(input("Masukkan Alas Segitiga(cm) "))
        angka2=float(input("Masukkan Tinggi Segitiga(cm) "))
        print(f"Luas Segitiga adalah : {(angka*angka2)/2} cm")
    elif hitung2==2:
        angka=float(input("Masukkan sisi AB "))
        angka2=float(input("Masukkan sisi BC "))
        angka3=float(input("Masukkan sisi AC "))
        print(f"Keliling Segitiga adalah : {angka+angka2+angka3}")
    else:
        print("Mohon maaf pilihan anda tidak tersedia saat ini")

elif hitung==4:
    print("""1. Luas
2. Keliling""")
    hitung2=int(input("Apa yang ingin anda hitung? "))
    if hitung2==1:
        angka=float(input("Masukkan Jari Jari Lingkaran(cm) "))
        print(f"Luas Lingkaran adalah : {3.14*(angka**2)} cm")
    elif hitung2==2:
        angka=float(input("Masukkan Jari Jari Lingkaran(cm) "))
        print(f"Keliling Lingkaran adalah : {2*(3.14*angka)} cm")
    else:
        print("Mohon maaf pilihan anda tidak tersedia saat ini")

elif hitung==5:
    print("""1. Luas
2. Keliling""")
    hitung2=int(input("Apa yang ingin anda hitung? "))
    if hitung2==1:
        angka=float(input("Masukkan Alas Jajar Genjang(cm) "))
        angka2=float(input("Masukkan Tinggi Jajar Genjang(cm) "))
        print(f"Luas Jajar Genjang adalah : {angka*angka2} cm")
    elif hitung2==2:
        angka=float(input("Masukkan Alas Jajar Genjang(cm) "))
        angka2=float(input("Masukkan sisi miring Jajar Genjang(cm) "))
        print(f"Keliling Jajar Genjang adalah : {2*(angka+angka2)} cm")
    else:
        print("Mohon maaf pilihan anda tidak tersedia saat ini")
    

else:
    print("Mohon maaf pilihan anda tidak tersedia saat ini")