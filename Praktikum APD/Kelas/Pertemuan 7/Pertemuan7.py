# def hasil(nama):
    
#     print("Hello World " + nama)

# hasil("Husein")
# hasil("Budi")
# hasil("Wilson")

# def luas_persegi_panjang(panjang,lebar):
#     luas = panjang*lebar
#     # print(f"Luas Persegi panjang adalah {luas}")
#     return luas

# luas_persegi_panjang(5,12)

# luas_persegi= luas_persegi_panjang

# print(luas_persegi)


# nama="Dimas" #Variabel Global

# def say_hello():
#     #Variable Lokal
#     nama="Daffa"
#     print(nama, "Dalam Fungsi")

# print(nama,"Luar Fungsi")
# say_hello()



import os
data_mahasiswa =["Ifnu","Adi","ucup","michael"]
def clear():
    os.system('cls || clear')
def show():
    print("===Lihat Data===")
    for i in range(len(data_mahasiswa)):
        print(f"data ke {i+1}")
        print(f"Nama : {data_mahasiswa[i]}")
        print("="*10)

def add():
    print("MENU TAMBAH DATA")
    print("=" * 10)
    inputUser = input("Data yang mau ditambahkan : ")
    data_mahasiswa.append(inputUser)
    print(f"{inputUser} telah ditambahkan")

def ubah():
    print("Menu ubah data")
    for i in range(len(data_mahasiswa)):
        print(f"data ke {i+1}")
        print(f"Nama : {data_mahasiswa[i]}")
        print("="*10)
    index= int(input("masukkan index yang mau diedit : "))
    data_baru =input("masukkan nama anda :")
    data_mahasiswa[index-1]=data_baru
    print("data berhasil diubah")

def deldata():
    print("Menu Hapus Data")
    for i in range(len(data_mahasiswa)):
        print(f"data ke {i+1}")
        print(f"Nama : {data_mahasiswa[i]}")
        print("="*10)
    index_user = int(input("masukkan index yang ingin dihapus: "))
    del_user = data_mahasiswa.pop(index_user-1)
    print(f"{del_user} telah dihapus")
clear()
while True:
    print("""
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
""")
    pilih = input("Masukan Pilihan menu >> ")
    os.system('cls || clear')
    match(pilih):
        case "1":
            show()
            input("Enter.....")
            clear()
        case "2":
            show()
            add()
            input("Enter....")
            clear()
        case "3":
            ubah()
            input("Enter.....")
            clear()
        case "4":
            deldata()
            input("Enter......")
            clear()
        case "5":
            print("Anda memilih menu 5")
            exit()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")
            os.system('cls || clear')


# def faktorial(n):
#     if n == 1 :
#         return 1
#     else:
#          return n* faktorial(n-1)
    
# print(faktorial(5))
