# Import adalah untuk memanggil library baik dari pandas, os dan juga memanggil def dari file lain
import pandas as pd
import os
from FileExt import add, ubah, delete, search, ubah_item,read
from login import login,register,data
import time

# Ini adalah fungsi atau def untuk membersihkan terminal
def clear():
    os.system('cls')

# Ini adalah variabel df yang berarti dataframe yang berfungsi untuk membaca data dari CSV
df = pd.read_csv('Data_CSV.csv')

admin = {
    'username'  : 'admin',
    'password'  : 'admin',
    'role'      : 'admin'
}

user = []
user.append(admin)

# Ini adalah fungsi atau def untuk menu
def menu(role,df):

    while True:
        clear()
        data(role['role'])
        choice = (
            input("Pilih menu 1-7 : ")
            if role['role'] == 'admin'
            else input ("Pilih menu 1-3 : ")
        )
        if choice == '1':
            clear()
            read(df)
            input("Enter untuk melanjutkan ....")
        elif choice == '2':
            clear()
            add(df)
            time.sleep(3)
        elif choice == '3' and role['role']== 'admin':
            clear()
            ubah(df)
            time.sleep(3)
        elif choice == '3':
            break
        elif choice == '4' and role['role'] == 'admin':     
            clear()
            df = delete(df)
            df.to_csv('Data_CSV.csv', index = False)
            time.sleep(3)
        elif choice == '5' and role['role'] == 'admin':
            clear()
            search(df)
            input("Enter untuk melanjutkan ....")
        elif choice == '6' and role['role'] == 'admin':
            clear()
            ubah_item(df)
            time.sleep(3)
        elif choice == '7' and role['role'] == 'admin':
            break
        else :
            print("Tidak ada pilihan!")
            time.sleep(3)

# Ini adalah fungsi atau def untuk main
def main():
    while True:
        os.system('cls')
        print("=" * 55)
        print("==== Selamat Datang Di Program Penitipan kendaraan ====")
        print("=" * 55)
        print("1. Login")
        print("2. Register")
        print("3. Logout")
        print("=" * 55)
        choice = input("Pilih Salah satu untuk Masuk ke program : ")
        if choice == '1':
            # Ini adalah blok kode yang akan memanggil fungsi atau def login
            role = login(user)
            if not role:
                print("Login Gagal")
            else:
                # Ini adalah blok kode yang akan memanggil fungsi atau def menu
                menu(role,df)
        elif choice == '2':
            # Ini adalah blok kode yang akan memanggil fungsi atau def register
            register(user)
        elif choice == '3':
            # Ini adalah blok kode yang akan membuat program berhenti
            break
        else:
            print("Tidak ada menu pilihan!")
            time.sleep(3)

# Ini adalah blok kode yang akan memanggil fungsi atau def main    
main()