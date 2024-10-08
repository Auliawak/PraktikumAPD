print("USER")
print("ADMIN")
print("KELUAR")
pilihan = input("masukkan pilihan:")

while True:
    if pilihan == "USER":
        print("="*30)
        print("LIST HP TERBAIK DI TAHUN 2024".center(30))
        print("="*30)
        xiaomi = ("Xiaomi 14", "Xiaomi 13T", "Xiaomi Redmi Note 13 Pro+ 5G")
        Samsung = ("Samsung S24 Ultra", "Samsung Galaxy Fold 5", "Samsung Galaxy Flip 5")
        Vivo = ("Vivo X100 Pro", "Vivo X Fold-3", "iQoo Z9 5G")
        print("[1] Xiaomi")
        print("[2] Samsung")
        print("[3] Vivo")
        print("[4] Keluar")
        pilihlah = input("Masukkan pilihan:")
        indeks = 0
        if pilihlah == "1":
            for i in xiaomi:
                print(f"{indeks+1} ", i)
                indeks +=1
                
        elif pilihlah == "2":
            for i in Samsung:
                print(f"{indeks+1} ", i)
                indeks +=1
                
        elif pilihlah == "3":
            for i in Vivo:
                print(f"{indeks+1} ", i)
                indeks +=1
        else:
            print("anda meninggalkan sistem")
            break

    
    elif pilihan == "ADMIN":
        print("="*30)
        print("Program Admin".center(30))
        print("="*30)
        
        while True:
            print("[1] Tambah list")
            print("[2] Edit list")
            print("[3] Hapus list")
            print("[4] Keluar")
            pilih = input("masukkan pilihan:")
            
            if pilih == "1":
                print("silahkan menambahkan list")
                tambah_xiaomi = input("list yang ingin di tambah ke Xiaomi:")
                tambah_samsung = input("list yang ingin di tambah ke Samsung:")
                tambah_vivo = input("list yang ingin di tambah ke Vivo:")
                xiaomi.append(tambah_xiaomi)
                Samsung.append(tambah_samsung)
                Vivo.append(tambah_vivo)
            elif pilih == "2":
                print("Silahkan mengedit list")
                nomor_xiaomi = input("Masukkan 0-2 untuk menentukan yang ingin di edit di xiaomi:")
                xiaomi[nomor_xiaomi] = input("")
                nomor_samsung = input("Masukkan 0-2 untuk menentukan yang ingin di edit di Samsung:")
                Samsung[nomor_samsung] = input("")
                nomor_vivo = input("Masukkan 0-2 untuk menentukan yang ingin di edit di Vivo:")
                Vivo[nomor_vivo] = input("")
            elif pilih == "3":
                print("Silahkan menghapus data")
                Nomor_xiaomi = input("Masukkan 0-2 untuk menentukan yang ingin di hapus di xiaomi:")
                del xiaomi[Nomor_xiaomi]
                Nomor_samsung = input("Masukkan 0-2 untuk menentukan yang ingin di hapus di Samsung:")
                del Samsung[Nomor_samsung]
                Nomor_vivo = input("Masukkan 0-2 untuk menentukan yang ingin di hapus di Vivo:")
                del Vivo[Nomor_vivo]
            else:
                print("Anda meninggalkan sistem")
                break
    
    else:
        print("Anda meninggalkan sistem")
        break