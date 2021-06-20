"""
Rudiansyah/20083000008/2A
19-06-2021
Program Menghitung Total Biaya Ekspedisi
"""
print("==============================")
print("Transaksi Biaya Ekspedisi")
print("==============================")
print("Kode = A. Surabaya")
print("Kode = B. Bandung")
print("==============================")
    
#Siapkan Variabel
kode = ['a','b']
kota = ['surabaya','bandung']
jarak = [169,452]
ongkirperkm = [2500,4000]
pilihan = input(">> Masukkan Kode Tujuan = ")

#Identifikasi Pilihan
if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
else:
    idx = 0
#Cetak tampilan layar
print(">>> Pilihan Tujuan = " + kota[idx])
print(">>> Jarak          = " + str(jarak[idx]) + " km")
print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

#Hitung transaksi
fixjarak = jarak[idx]
fixongkirkm = ongkirperkm[idx]
totongkir = fixjarak + fixongkirkm
#Tampilkan total ongkir
print(">>>-----------------------------")
print(">>> Total Biaya    = Rp." + str(totongkir))
