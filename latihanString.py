nama = "ASEP SUKANDAR"
alamat = "Kp. Pasirjati, Cikakak, Sukabumi"

print("Nama Saya",nama)
print("Alamat Saya",alamat)
print("Hurup Pertama Saya",nama[0])
print("Hurup Terakhir Saya",nama[-1])
print("Nama Depan Saya",nama[:4])
print("Nama Terakhir Saya",nama[-8:])

print("=============Split========")
#Spit
alamat_array = alamat.split(', ')
kampung = alamat_array[0]
kecamatan = alamat_array[1]
kabupaten = alamat_array[2]
print("Alamat Saya array",alamat_array)
print("Alamat Kampung Saya",kampung)
print("Alamat Kecamatan Saya",kecamatan)
print("Alamat Kabupaten Saya",kabupaten)

print("Saya Tinggal di Kampung",kampung," Kecamatan", kecamatan,"Kabupaten",kabupaten)
print(f'Saya Tinggal di Kampung {kampung} Kecamatan {kecamatan} Kabupaten{kabupaten}')

print("=============Join String========")
#Join String
pemisah = "+"
print("Alamat Kabupaten Saya",pemisah.join(alamat_array))
