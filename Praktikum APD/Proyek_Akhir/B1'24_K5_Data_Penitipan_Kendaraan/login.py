# Import adalah untuk memanggil library dari os
import time 
import os
from time import sleep

# Ini adalah fungsi atau def untuk login
def login(users):
    try:
        username = input('Enter username : ')
        password = input('Enter Password : ')

        user_exist = [user for user in users if user['username'] == username and user['password'] == password]

        if len(user_exist) == 0:
            print((f'Username {username} tidak ditemukan, silahkan daftar dahulu!'))
            raise Exception (input("Enter to Continue....."))
            

        print('Login Berhasil!')
        time.sleep(2)
        return user_exist[0]
    
    except Exception as e:
        print(e)
        time.sleep(2)
    except:
        print('Login error')
        return


# Ini adalah fungsi atau def untuk register
def register(users):
    
    # Ini berfungsi agar username dan password tidak berisi spasi atau kosong saja
    username = input('Create username : ').strip()
    password = input('Create password : ').strip()

    if not username or not password:
        print("Username dan Password tidak boleh kosong!")
        time.sleep(2)
        return None

    user = {'username' : username,'password' : password, 'role' : 'user'} 
    users.append(user)
    
    print("Registrasi Succesful")
    time.sleep(2)
    return user

# Ini adalah fungsi atau def untuk menu
def data(role):
    os.system('cls')
    print("="*55)
    print("======= Menu Program Penitipan Kendaraan =======")
    print("="*55)
    print("1. Lihat Data")
    print("2. Buat Data")
    if role == 'admin':
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("6. Ubah Salah Satu Data")
        print("7. Keluar")
        print("="*28)
    else:
        print("3. Keluar")
        print("="*28)
    return role