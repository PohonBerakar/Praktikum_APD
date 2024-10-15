import os
os.system('cls || clear')
ulang1="yes"
newuser=False
newpassw=False
role=False
while ulang1=="yes":
    print("====== HALO PETUALANG ======")
    print("Silahkan pilih menu dibawah ini")
    print()
    print("1. Daftar")
    print("2. Login")
    print("3. Keluar Program")
    print("")
    pLogin=input(" ")
    if pLogin=="1":
        os.system('cls || clear')
        while True:
            print("=== HALO PEMULA ===")
            print("Silahkan isi form registrasi berikut!")
            print()
            print("NOTE: Registrasi hanya berlaku 1 kali untuk setiap Petualang")
            print("")
            newuser=input("Masukkan Username : ")
            newpassw=input("Masukkan Password : ")
            confirmnewpassw=input("Konfirmasi Password : ")
            if (newuser=="") or (newpassw==""):
                print("Registrasi gagal")
                print("Username dan Password baru tidak boleh kosong !!!")
                input("Enter.....")
                os.system('cls || clear')
            elif newpassw==confirmnewpassw:
                print("Berhasil Registrasi")
                input("Enter.....")
                os.system('cls || clear')
                break
            else:
                print("Password tidak sesuai, silahkan ulang")
                input("Enter.....")
                os.system('cls || clear')

    elif pLogin=="2":
        os.system('cls || clear')
        while True :
            print("==LOGIN==")
            print("Kosongkan jika belum memiliki akun")
            print("")
            usern1=input("Masukkan Username : ")
            passw1=input("Masukkan Password : ")
            if (usern1=="" and passw1==""):
                input("Enter.....")
                os.system('cls || clear')
                break
            elif (usern1=="Husein" and passw1=="admin051") or (usern1=="admin" and passw1=="admin1234") :
                print("Berhasil Login sebagai ADMIN")
                role="admin"
                ulang1="no"
                input("Enter.....")
                os.system('cls || clear')
                break
            elif (usern1=="kroco" and passw1=="kroco1234") or (usern1=="user" and passw1=="user") or (usern1==newuser and passw1==newpassw):
                print("Berhasil Login sebagai KROCO")
                role="user"
                ulang1="no"
                input("Enter.....")
                os.system('cls || clear')
                break
            else:
                print("Username atau Password Salah")
                input("Enter.....")
                os.system('cls || clear')
    elif pLogin=="3":
        break
    else:
        print("Silahkan pilih menu Daftar atau Login !!!")
        input("Enter.....")
        os.system('cls || clear')

database=[
    {"nama"  : "Fufufafa",
    "ras"    : "Raja Iblis",
    "senjata": "Kursi",
    "power"  : "Full Roast"},
    {"nama"  : "Bayu Saber",
    "ras"    : "Cyborg",
    "senjata": "Dual Sword",
    "power"  : "Skill 1, Ulti"}
]
if role=="user":
    while True:
        os.system('cls || clear')
        print("===== Data Petualang kerajaan =====")
        print("")
        print("1. Lihat Data")
        print("2. Keluar")
        useraccess=input(" ")
        os.system('cls || clear')
        if useraccess=="1":
            print("==== Data Petulalang ====")
            print("")
            for i, player in enumerate(database):
                print(f"Data Petualang No. {i+1}")
                print(f"Nama    : {player["nama"]}")
                print(f"Ras     : {player["ras"]}")
                print(f"Senjata : {player["senjata"]}")
                print(f"Power   : {player["power"]}")
                print("")
            input("Enter 2x untuk kembali.....")
            input("")
            os.system('cls || clear')
        elif useraccess=="2":
            print("Keluar Program")
            input("Enter untuk lanjutkan...")
            os.system('cls || clear')
            break
        else:
            print("Pilih menu yang tersedia !!!")
            input("Enter.....")
            os.system('cls || clear')

elif role=="admin":
    while True:
        os.system('cls || clear')
        print("===== Data Petualang kerajaan =====")
        print("")
        print("1. Lihat Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus data")
        print("5. Keluar")
        adminaccess=input(" ")
        os.system('cls || clear')
        if adminaccess=="1":
            print("==== Data Petulalang ====")
            print("")
            for i, player in enumerate(database):
                print(f"Data Petualang No. {i+1}")
                print(f"Nama    : {player["nama"]}")
                print(f"Ras     : {player["ras"]}")
                print(f"Senjata : {player["senjata"]}")
                print(f"Power   : {player["power"]}")
                print("")
            input("Enter 2x untuk kembali.....")
            input("")
            os.system('cls || clear')
        elif adminaccess=="2":
            ullangg="yes"
            while ullangg=="yes":
                print("==== Menambahkan data Petualang ====")
                print("")
                print("==== Data Petualang ====")
                print("")
                for i, player in enumerate(database):
                    print(f"Data Petualang No. {i+1}")
                    print(f"Nama    : {player["nama"]}")
                    print(f"Ras     : {player["ras"]}")
                    print(f"Senjata : {player["senjata"]}")
                    print(f"Power   : {player["power"]}")
                    print("")
                nama=input("Nama Petualang yang ingin ditambahkan : ")
                ras=input("Ras Petualang yang ingin ditambahkan : ")
                senjata=input("Senjata Petualang yang ingin ditambahkan : ")
                power=input("Jenis kekuatan Petualang yang ingin di tambahkan : ")
                database.append({"nama" : nama, "ras" : ras, "senjata" : senjata, "power" : power})
                print("Data telah Ditambahkan")
                print("Enter.....")
                os.system('cls || clear')
                while True:
                    print("Apakah ingin menambahkan data lagi?")
                    print("1. ya")
                    print("2. tidak")
                    tambahlagi=input(" ")
                    if tambahlagi=="2":
                        input("Enter.....")
                        ullangg="no"
                        os.system('cls || clear')
                        break
                    elif tambahlagi=="1":
                        input("Enter untuk melanjutkan.....")
                        os.system('cls || clear')
                        break
                    else:
                        print("Pilihan tidak tersedia !!!")
                        input("")
                        os.system('cls || clear')
        elif adminaccess=="3":
            ullangg="yes"
            while ullangg=="yes":
                print("==== Mengubah data Petualang ====")
                print("")
                print("Harap melihat data terlebih dahulu sebelum mengubah data")
                print("")
                print("==== Data Petulalang ====")
                print("")
                for i, player in enumerate(database):
                    print(f"Data Petualang No. {i+1}")
                    print(f"Nama    : {player["nama"]}")
                    print(f"Ras     : {player["ras"]}")
                    print(f"Senjata : {player["senjata"]}")
                    print(f"Power   : {player["power"]}")
                    print("")
                revisi=int(input("Data berapa yang ingin diubah? "))-1
                ubahnama=input("Masukkan nama baru petualang : ")
                ubahras=input("Masukkan ras baru petualang : ")
                ubahsenjata=input("Masukkan senjata baru petualang : ")
                ubahpower=input("Masukkan kekuatan baru petualang : ")
                database[revisi]={"nama" : ubahnama, "ras" : ubahras, "senjata" : ubahsenjata, "power" : ubahpower}
                print("Data telah Diupdate!")
                input("Enter untuk melanjutkan...")
                os.system('cls || clear')
                while True:
                    print("Apakah ingin mengubah data lagi?")
                    print("1. ya")
                    print("2. tidak")
                    ubahlagi=input(" ")
                    if ubahlagi=="2":
                        input("Enter untuk melanjutkan.....")
                        ullangg="no"
                        os.system('cls || clear')
                        break
                    elif ubahlagi=="1":
                        input("Enter untuk melanjutkan...")
                        os.system('cls || clear')
                        break
                    else:
                        print("Pilihan tidak tersedia !!!")
                        input("")
                        os.system('cls || clear')
        elif adminaccess=="4":
            ullangg="yes"
            while ullangg=="yes":
                print("====-- Menghapus Data Petualang --====")
                print("")
                print("Harap melihat data terlebih dahulu sebelum mengubah data")
                print("")
                for i, player in enumerate(database):
                    print(f"Data Petualang No. {i+1}")
                    print(f"Nama    : {player["nama"]}")
                    print(f"Ras     : {player["ras"]}")
                    print(f"Senjata : {player["senjata"]}")
                    print(f"Power   : {player["power"]}")
                    print("")
                pilihhapus=int(input("Data berapa yang ingin dihapus : "))-1
                database.pop(pilihhapus)
                print(f"Data {pilihhapus+1} Telah dihapus ! ")
                print("")
                input("Enter untuk lanjutkan...")
                os.system('cls || clear')
                while True:
                    print("Apakah ingin mengubah data lagi?")
                    print("1. ya")
                    print("2. tidak")
                    hapuslagi=input(" ")
                    if hapuslagi=="2":
                        input("Enter untuk melanjutkan.....")
                        ullangg="no"
                        os.system('cls || clear')
                        break
                    elif hapuslagi=="1":
                        input("Enter untuk melanjutkan...")
                        os.system('cls || clear')
                        break
                    else:
                        print("Pilihan tidak tersedia !!!")
                        input("")
                        os.system('cls || clear')

        elif adminaccess=="5":
            print("Keluar Program")
            input("Enter untuk lanjutkan...")
            os.system('cls || clear')
            break
        else:
            print("Pilih menu yang tersedia !!!")
            input("Enter.....")
            os.system('cls || clear')
            
print("Program Selesai")
input("")
os.system('cls || clear')
