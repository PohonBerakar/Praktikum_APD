# Import adalah untuk memanggil library baik dari pandas dan os
import pandas as pd
import os

# Ini adalah fungsi atau def untuk pengecekan inputan pengguna, agar tidak ada inputan kosong
# Apabila kosong maka akan muncul pesan dibawah, lalu disuruh untuk input lagi sampai inputan tidak kosong
def entry_input(entry): 
    file_input = input(entry) 
    while not file_input: 
        print("Input tidak boleh kosong atau spasi, tolong ulangi lagi !") 
        file_input = input(entry) 
    return file_input 

# Ini adalah fungsi atau def untuk membaca data
def read(df):
    # Kode ini bertujuan untuk membaca data CSV
    df = pd.read_csv('Data_CSV.csv')
    if len(df) == 0:
        print("belum ada data")
    else:
        df.index = range(1, len(df) + 1)
        print(df)

# Ini adalah fungsi atau def untuk mengubah data, dengan cara dia akan menampilkan data yang ada
# Kemudian meminta pengguna untuk memilih data yang ingin diubah
def ubah(df):
    try:
        # Kode ini bertujuan untuk membaca data CSV
        df = pd.read_csv('Data_CSV.csv')
        
        print("="*28)
        print("Ubah Data".center(28))
        print("="*28)
        print("List Nama".center(28))
        for i, nama in enumerate(df['nama']):
            print(f"{i+1}. {nama.capitalize()}") 
        print("="*28)
        nama = entry_input("Nama lama : ")
        if nama not in df['nama'].values:
            print("Data tidak ditemukan !")
            return df
        name = entry_input("Nama baru : ")
        kontak = int(entry_input("Nomor kontak (+62): "))
        jk = int(entry_input("kendaraan roda : "))
        merek = entry_input("Merek kendaraan : ")
        warna = entry_input("Warna kendaraan : ")
        plat = entry_input("Plat kendaraan : ")
        durasi = int(entry_input("Durasi penitipan : "))
        tiket = f"S{len(df)+1}A{durasi}H"
        if jk == 2:
            biaya = durasi*30000
        elif jk == 4:
            biaya = durasi*50000
        else :
            biaya = durasi*100000 
        harga = biaya
        bayar = entry_input("Pembayaran Cash/Dp : ")
        if jk == 2:
            lokasi = "lantai 3"
        elif jk == 4:
            lokasi = "lantai 2"
        else:
            lokasi ="lantai 1"
        tempat = lokasi

        # Ini adalah kode dimana mengubah DataFrame (df) menjadi data yang baru sesuai inputan user
        df.loc[df['nama'] == nama, 
        ['nama','kontak','tiket','roda','merek','warna',
        'plat','durasi','biaya','bayar','lokasi']
        ] = [
        name,kontak,tiket,jk,merek,warna,
        plat,durasi,harga,bayar,tempat]
        
        # Kode ini bertujuan untuk menyimpan data yang baru
        # Dengan index false yang artinya tidak ada index (0 1 2 3)
        df.to_csv('Data_CSV.csv', index=False)
        print(f"Data {nama} Berhasil di ubah ")
    except ValueError :
        print("Masukkan data dengan Benar !")
    return df

# Ini adalah fungsi atau def untuk menghapus data
def delete(df):
    # Kode ini bertujuan untuk membaca data CSV
    df = pd.read_csv('Data_CSV.csv')
    
    print("="*28)
    print("Hapus Data".center(28))
    print("="*28)
    print("List Nama & Plat".center(28))
    for i, row in df.iterrows():
        print(f"{i+1}. {row['nama'].capitalize()} {row['plat']}")
        
    print("="*28)
    # Kode ini bertujuan untuk pengguna memasukan inputan yang ingin dihapus, Lalu akan dicarikan di DataFrame (df)
    # Setelah ditemukan maka data tersebut akan dihapus
    nama = entry_input("Nama yang ingin di hapus : ").strip().lower() 
    plat = entry_input("Plat kendaraan : ").strip().lower()
    
    # Menjadikan nama dan plat menjadi huruf kecil
    df['nama'] = df['nama'].str.lower()  
    df['plat'] = df['plat'].str.lower()  
    
    # Variabel data akan menampung data yang ingin dihapus
    data = df[(df['nama'] == nama) & (df['plat'] == plat)]
    
    if len(data) == 0:
        print("Data tidak ditemukan !")
        return df
    else:
        # Kode ini bertujuan untuk menghapus data
        # Drop digunakan untuk menghapus data (Pandas)
        df = df.drop(data.index)
        df.to_csv('Data_CSV.csv', index=False)
        print("Data berhasil dihapus")
    return df

# Ini adalah fungsi atau def untuk menambahkan data
def add(df):
    try:
        print("="*28)
        print("Buat Data Baru".center(28)) 
        print("="*28)
        nama = entry_input("Nama Pemilik : ")
        kontak = int(entry_input("Nomor kontak (+62): "))
        roda = int(entry_input("kendaraan roda : "))
        merek = entry_input("Merek kendaraan : ")
        warna =entry_input("Warna kendaraan : ")
        plat =entry_input("Plat kendaraan : ")
        durasi = int(entry_input("Durasi penitipan (Hari): "))
        tiket = f"S{len(df)+1}A{durasi}H"
        if roda == 2:
            biaya = durasi*30000
        elif roda == 4:
            biaya = durasi*50000
        else :
            biaya = durasi*100000 
        harga = biaya
        bayar = entry_input("Pembayaran Cash/Dp : ")
        if roda == 2:
            lokasi = "lantai 3"
        elif roda == 4:
            lokasi = "lantai 2"
        else:
            lokasi ="lantai 1"
        tempat = lokasi

        # Ini adalah kode dimana mengubah DataFrame (df) menjadi data yang baru sesuai inputan user
        # Columns berfungsi untuk memasukan data baru sesuai dengan kolom yang ada di CSV 
        databaru = pd.DataFrame(
            [[nama,kontak,tiket,roda,merek,warna,plat,durasi,harga,bayar,tempat]], columns = df.columns
            )
        
        # Concat adalah versi lebih baru dari append untuk pandas
        # Yang gunanya untuk memasukan data baru ke dalam variabel df
        df = pd.concat([df, databaru], ignore_index = True)
        
        # Ini baris kode yang berfungsi untuk memasukkan data baru kedalam CSV
        df.to_csv('Data_CSV.csv', index = False)
        print(f"Data atas Nama {nama} Berhasil ditambahkan")

    except ValueError :
        print("Masukkan data dengan Benar!")
    return df
    
# Ini adalah fungsi atau def untuk mencari data
def search(df):
    # Kode ini bertujuan untuk membaca data CSV
    df = pd.read_csv('Data_CSV.csv')
    
    print("="*28)
    print("Cari Data".center(28))
    print("="*28)
    nama = input("Masukkan Nama : ").strip().lower() 
    
    # Kode ini bertujuan untuk mencari data sesuai inputan user
    df.loc[:,'nama'] = df['nama'].str.lower()
    df = df[df['nama'] == nama]
    if len(df) == 0:
        print(f"Data atas nama {nama} tidak ditemukan")
    else:
        df.index = range(1, len(df) + 1)
        print(df)

# Ini adalah fungsi atau def untuk mengubah salah satu data saja
def ubah_item(df):
    # Kode ini bertujuan untuk membaca data CSV
    df = pd.read_csv('Data_CSV.csv')
    
    print("="*28)
    print("Ubah Data".center(28))
    print("="*28)
    print("List Nama".center(28))
    for i, nama in enumerate(df['nama']):
        print(f"{i+1}. {nama.capitalize()}")
    print("="*28)
    nama = input("masukkan data nama pemilik yang ingin diubah : ").strip().lower()
    pemilik = df[df['nama'].str.lower() == nama]
    if len(pemilik) == 0 :
        print("data tidak ditemukan!")
    else:
        os.system('cls')
        print("="*28)
        print("List Kolom".center(28))
        print("="*28)
        print("1. Nama\n2. Kontak\n3. Tiket\n4. Roda\n5. Merek\n6. Warna\n7. Plat\n8. Durasi\n9. Biaya\n10. Bayar\n11. Lokasi")
        diubah = input("apa yang ingin diubah : ").strip().lower()
        pilihan = ['nama','kontak','tiket','roda','merek','warna','plat','durasi','biaya','bayar','lokasi']
        if diubah in pilihan:
            # Kode ini bertujuan agar data baru di cek terlebih dahulu
            # lalu akan diubah sesuai inputan user
            new = input(f"Masukkan {diubah.capitalize()} baru : ")
            df.loc[df['nama'].str.lower() == nama, diubah] = new
            print(f"Berhasil mengubah {diubah} pada data {nama} menjadi {new}")
        else :
            print("kolom tidak ditemukan")
        
        df.to_csv('Data_CSV.csv', index = False)
        return df