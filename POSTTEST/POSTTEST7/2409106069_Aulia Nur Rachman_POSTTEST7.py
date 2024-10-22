import os

merk_HP = {
    "Xiaomi": "Xiaomi 14",
    "Samsung": "Samsung S24 Ultra",
    "Vivo": "Vivo X100 Pro"
}
usn = "admin"
pw = "admin123"
max_salah = 3

def tampilkan_menu():
    print("[1] ADMIN")
    print("[2] USER")
    print("[3] KELUAR")
    pilih = input("Masukkan pilihan: ")
    os.system('cls')
    return pilih

def validasi_login(username, password):
    return username == usn and password == pw

def ambil_hp():
    return merk_HP

def admin_prosedur():
    salah = 0
    while True:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        if validasi_login(username, password):
            program_admin()
            break
        else:
            salah += 1
            print("Username atau password anda tidak cocok")
            input("\nKlik enter untuk melanjutkan...")
            os.system('cls')
            if salah == max_salah:
                print("Kesempatan anda telah habis")
                exit()

def program_admin():
    while True:
        os.system('cls')
        print("="*30)
        print("PROGRAM ADMIN".center(30))
        print("="*30)
        print("[1] Tambah list")
        print("[2] Edit list")
        print("[3] Hapus list")
        print("[4] Liat list")
        print("[5] Keluar")
        pilihan = input("Masukkan pilihan: ")
        input("\nKlik enter untuk melanjutkan...")
        os.system('cls')

        if pilihan == "1":
            tambah_hp()
        elif pilihan == "2":
            edit_hp()
        elif pilihan == "3":
            hapus_hp()
        elif pilihan == "4":
            liat_hp()
        else:
            print("Anda meninggalkan sistem")
            exit()

def tambah_hp():
    tambah_Hp = input("Merk Hp apa yang ingin dimasukkan: ")
    tambah_jenis = input("Apa series/jenisnya: ")
    merk_HP[tambah_Hp] = tambah_jenis
    print(f"{tambah_Hp} ditambahkan dengan jenis {tambah_jenis}")
    input("\nKlik enter untuk melanjutkan...")

def edit_hp():
    ganti_Hp = input("Merk Hp apa yang ingin diganti: ")
    ganti_jenis = input("Mau ganti jadi series/jenis apa: ")
    merk_HP[ganti_Hp] = ganti_jenis
    print(f"{ganti_Hp} diubah menjadi {ganti_jenis}")
    input("\nKlik enter untuk melanjutkan...")
    
def hapus_hp():
    hapus = input("HP mana yang ingin dihapus: ")
    if hapus in merk_HP:
        del merk_HP[hapus]
        print(f"{hapus} telah dihapus")
        input("\nKlik enter untuk melanjutkan...")
        
    else:
        print(f"{hapus} tidak ditemukan")
        input("\nKlik enter untuk melanjutkan...")

def liat_hp():
    for i, j in ambil_hp().items():
        print(f"merk HP {i} series yang terbaik adalah : {j}")
        input("\nKlik enter untuk melanjutkan...")
        os.system('cls')

    

def program_user():
    os.system('cls')
    print("="*30)
    print("PROGRAM USER")
    print("="*30)
    print("[1] Melihat merk dan jenis hp terbaik 2024")
    print("[2] Keluar")
    pilihlah = input("Masukkan pilihan: ")

    if pilihlah == "1":
        for i, j in ambil_hp().items():
            print(f"merk HP {i} series yang terbaik adalah : {j}")
        input("\nKlik enter untuk melanjutkan...")
        os.system('cls')
    else:
        print("Anda Meninggalkan sistem")
        input("\nKlik enter untuk melanjutkan...")
        exit()

os.system('cls')
pilih = tampilkan_menu()

if pilih == "1":
    admin_prosedur()
elif pilih == "2":
    program_user()
else:
    print("Anda meninggalkan sistem")