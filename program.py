import json
import getpass
from prettytable import PrettyTable

# Inisiasi data user(Role & Password)
users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'iyas123', 'role': 'user'}
}

# File tempat penyimpanan data pendaftar
FILE_PENDAFTAR = 'pendaftars.json'

# simpan data ke json
def simpan_data():
    with open(FILE_PENDAFTAR, 'w') as file:
        json.dump(pendaftars, file)

# membaca dari json
def baca_data():
    global pendaftars
    try: 
        with open(FILE_PENDAFTAR, 'r') as file:
            pendaftars = json.load(file)
    except FileNotFoundError:
        pendaftars = [] #list kosong jika file tidak ditemukan

# login
def login():
    print("===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]['password'] == password:
        print(f"Login berhasi! Selamat datang, {username}")
        return users[username]['role']
    else: 
        print("Login Gagal le, Password Salah")
        return None
    
# Menu CRUD untuk Admin
def menu_admin():
    while True:
        print("\n===== Menu Admin =====")
        print("1. Tambah Pendaftar")
        print("2. Lihat Pendaftar") 
        print("3. Ubah Data Pendaftar")
        print("4. Hapus Data Pendaftar")
        print("5. Keluar?")
        choice = input("Pilih menu: ")

        if choice == '1':
            tambah_pendaftar()
        elif choice == '2':
            lihat_pendaftar()
        elif choice == '3':
            ubah_pendaftar()
        elif choice == '4':
            hapus_pendaftar()
        elif choice == '5':
            break
        else:
            print("Pilihan tidak ada!")

# Menu Pendaftaran untuk User
def menu_user():
    print("\n===== Pendaftaran SNPMB =====")
    nama = input("Masukkan nama Anda: ")
    pilihan = input("Pilih jenis pendaftaran (SNBP/SNBT): ")
    pendaftar_baru = {
        'nama': nama,
        'jenis_pendaftaran': pilihan
    }
    pendaftars.append(pendaftar_baru)
    print(f"Pendaftaran {pilihan} untuk {nama} berhasil!")
    simpan_data()

# Tambah Pendaftar/CREATE (Admin)
def tambah_pendaftar():
    print("\n===== Tambah Pendaftar =====")
    nama = input("Masukkan nama: ")
    jenis_pendaftaran = input("Masukkan jenis pendaftaran (SNBP/SNBT): ")
    pendaftar = {
        'nama' : nama,
        'jenis_pendaftaran' : jenis_pendaftaran
    }
    pendaftars.append(pendaftar)
    print(f"Pendaftar {nama} berhasil ditambahkan")
    simpan_data()

# Lihat Pendaftar(admin & user)
def lihat_pendaftar():
    if not pendaftars:
        print("Belum ada pendaftar.")
        return

    table = PrettyTable(["No", "Nama", "Jenis Pendaftaran"])
    for idx, pendaftar in enumerate(pendaftars, start=1):
        table.add_row([idx, pendaftar['nama'], pendaftar['jenis_pendaftaran']])

    print(table)

# Ubah data pendaftar/UPDATE (Admin)
def ubah_pendaftar():
    lihat_pendaftar()
    if not pendaftars:
        return

    try:
        no = int(input("Masukkan nomor pendaftar yang ingin diubah: "))
        pendaftar = pendaftars[no - 1]
        pendaftar['nama'] = input(f"Nama ({pendaftar['nama']}): " or pendaftar['nama'])
        pendaftar['jenis_pendaftaran'] = input(f"Jenis Pendaftaran ({pendaftar['jenis_pendaftaran']}): ") or pendaftar['jenis_pendaftaran']
        print(f"Pendaftar nomor {no} berhasil diubah!")
        simpan_data()
    except (IndexError, ValueError):
        print("Nomor tidak valid!")

# Hapus data pendaftar/DELETE (Admin)
def hapus_pendaftar():
    lihat_pendaftar()
    if not pendaftars:
        return


    try:
        no = int(input("Masukkan nomor pendaftar yang ingin dihapus: "))
        pendaftar = pendaftars.pop(no - 1)
        print(f"Pendaftar {pendaftar['nama']} berhasil dihapus!")
        simpan_data()
    except (IndexError, ValueError):
        print("nomor tidak ada!")

# Main Program
def main():
    baca_data()
    role = None
    while role is None:
        role = login()
    
    if role == 'admin':
        menu_admin()
    elif role == 'user':
        menu_user()

if __name__ == "__main__":
    main()
