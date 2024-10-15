import os

print("[1] ADMIN")
print("[2] USER")
print("[3] KELUAR")
pilih = input("Masukkan pilihan: ")
input("\nKlik enter untuk melanjutkan...")

os.system('cls')

while True:
    merk_HP = {
        "Xiaomi" : "Xiaomi 14",
        "Samsung" : "Samsung S24 Ultra",
        "Vivo" : "Vivo X100 Pro"
        }
    if pilih == "1":
        usn = "admin"
        pw = "admin123"
        salah = 0
        max_salah = 3
        while True:
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            if usn == username and pw == password:
                os.system('cls')
                print("="*30)
                print("PROGRAM ADMIN".center(30))
                print("="*30)
                while True:
                    print("[1] Tambah list")
                    print("[2] Edit list")
                    print("[3] Hapus list")
                    print("[4] Keluar")                
                    pilihan = input("Masukkan pilihan: ")
                    input("\nKlik enter untuk melanjutkan...")

                    if pilihan == "1":
                        os.system('cls')
                        tambah_Hp = input("Merk Hp apa yang ingin dimasukkan: ")
                        tambah_jenis = input("Apa series/jenisnya: ")
                        merk_HP[tambah_Hp] = tambah_jenis
                        input("\nKlik enter untuk melanjutkan...")
                    
                    elif pilihan == "2":
                        os.system('cls')
                        ganti_Hp = input("Merk Hp apa yang ingin diganti:")
                        ganti_jenis = input("Mau ganti jadi series/jenis apa:")
                        merk_HP[ganti_Hp] = ganti_jenis
                        input("\nKlik enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system('cls')
                        hapus = input("HP mana yang ingin dihapus: ")
                        del merk_HP[hapus]

                    else:
                        os.system('cls')
                        print("Anda meninggalkan system")
                        input("\nKlik enter untuk melanjutkan...")
                        exit()

            else:
                salah += 1
                print("Username atau password anda tidak cocok")
                print("Silahkan masukkan username dan password dengan benar")
                input("\nKlik enter untuk melanjutkan...")
                os.system('cls')
                if salah == max_salah:
                    print("Kesempatan anda telah habis")
                    print("Silahkan coba lagi lain kali")
                    input("\nKlik enter untuk melanjutkan...")
                    exit()

    elif pilih == "2":
        os.system('cls')
        print("="*30)
        print("PROGRAM USER")
        print("="*30)
        print("[1] Melihat merk dan jenis hp terbaik 2024")
        print("[2] Keluar")
        pilihlah = input("Masukkan pilihan: ")

        while True:
            if pilihlah == "1":
                for i, j in merk_HP.items():
                    print(f"merk HP {i} series yang terbaik adalah : {j}")
                
                input("\nKlik enter untuk melanjutkan...")
                exit()

            else:
                os.system('cls')
                print("Anda Meninggalkan system")
                input("\nKlik enter untuk melanjutkan...")
                exit()

    else:
        os.system('cls')
        print("Anda meninggalkan system")
        input("\nKlik enter untuk melanjutkan...")
        exit()