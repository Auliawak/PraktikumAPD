#memasukkan berat badan dalam satuan mg
bb=float(input("Masukkan Berat badan dalam satuan mg: "))
#mwmasukkan tinggi badan dalam satuan km
tb=float(input("Masukkan Tinggi badan dalam satuan km: "))

tinggi_meter = tb*1000
berat_kg = bb/1000000
berat_ideal = berat_kg/(tinggi_meter*tinggi_meter)
tinggi_cm = tinggi_meter*100

print (f"Tinggi badan anda=  {int(tinggi_cm)}cm")
print (f"Berat badan anda=  {int(berat_kg)}kg")

if berat_ideal < 18.5:
    print ("berat badan anda kurang (underweight)")
elif berat_ideal < 24.9:
    print ("berat anda normal")
elif berat_ideal < 29.9:
    print ("berat badan anda berlebih (overweight)")
else:
    print ("anda memiliki penyakit obesitas")