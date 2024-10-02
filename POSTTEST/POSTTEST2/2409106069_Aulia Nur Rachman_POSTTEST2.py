#Menginput nama barang (nb), harga barang (hb), jumlah barang(jb)
nb=str (input("Masukkan nama barang: "))
hb=float (input("Masukkan harga barang: "))
jb=int (input("Masukkan jumlah barang: "))

#Masukkan diskon berdasarkan dua digit terakhir NIM
diskon=float (input("Masukkan diskon dalam persen:"))
#diskon dalam persen
diskon_dalam_persen = diskon/100

#Proses penghitungan harga
total_harga = hb*jb
total_diskon = diskon_dalam_persen*total_harga
total = total_harga-total_diskon
sisa_pembagian = diskon%3

#output
print (f"Anda membeli {int(jb)} {nb} dengan harga satuan Rp.{int(hb)} ,total sebelum diskon adalah Rp.{int(total_harga)}, total diskon adalah Rp.{int(total_diskon)} ,dan total yang harus dibayar adalah Rp.{int(total)}")
print (f"{int(diskon)} dibagi dengan 3 adalah  {int(sisa_pembagian)}")
