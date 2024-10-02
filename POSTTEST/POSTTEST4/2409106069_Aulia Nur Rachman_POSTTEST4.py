print("Pendaftaran Akun")

usn = input("Masukkan nama sebagai username: ")
NIM = input("Masukkan 3 digit terakhir NIM anda: ")
print("jika 3 digit terakhir NIM anda berawalan 0 akan terhapus otomatis")
pw = NIM[-3:].lstrip("0")

salah = 0
max_salah = 3

print("Silahkan Login")

while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if usn == username and pw == password:
        print("Anda telah login")
        break

    else:
        salah += 1
        print(f"login gagal, anda salah {salah} kali")
        if salah == max_salah:
            print("Anda gagal login")
            print("Silahkan coba lagi lain kali")
            exit()

print("Selamat datang di Kalkulator BMI")

while True:
    def bmi(berat, tinggi):
        tinggi_meter = tinggi / 100
        berat_ideal = berat / (tinggi_meter * tinggi_meter)
        print(f"hasil indeks bmi anda adalah {berat_ideal}")

        if berat_ideal < 18.5:
            print("berat badan anda kurang")
        elif berat_ideal < 24.9:
            print("berat badan anda normal")
        elif berat_ideal < 29.9:
            print("berat anda berlebih")
        else:
            print("anda memiliki penyakit obesitas")

    
    berat = float(input("Masukkan berat badan:"))
    tinggi = float(input("Masukkan tinggi anda:"))
    hasil = bmi(berat, tinggi)
    print(hasil)

    print("ketik 'keluar' untuk meninggalkan sistem")
    perintah = input(">>> ")
    if perintah == "keluar":
        print("Anda telah meninggalkan sistem")
        break
    else:
        print("Silahkan mencoba lagi")