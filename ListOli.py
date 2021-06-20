"""
Rudiansyah/20083000008/2A
19-06-2021
Program Menampilkan List Harga Serta Perhitungan Penjualan Oli Mesin
"""
print("=================================")
print("Transaksi Penjualan Oli Mesin")
print("=================================")
print("Kode = a. Duration SW20")
print("Kode = b. Castrol Magnatec")
print("Kode = c. Federal Supreme XX")
print("Kode = d. Yamalube")
print("Kode = e. Shell")
print("==================================")

#Siapkan Variabel
Kode = ['a','b','c','d','e']
OliMesin = ['Duration SW20','Castrol Magnatec','Federal Supreme XX','Yamalube','Shell']
Harga = [53000,50000,54000,45000,46000]
diskon = [0.05]
Ppn = [0.01]
pilihan = input(">> Masukkan Kode Pilihan Oli = ")

#Identifikasi Pilihan
if pilihan=="a":
    harga = 53000
elif pilihan=="b":
    harga = 50000
elif pilihan=="c":
    harga = 54000
elif pilihan=="d":
    harga = 45000
elif pilihan=="e":
    harga = 46000
else:
    harga = 0
qty = int(input(">> Masukkan Jumlah Pembelian = "))
if pilihan=="a":
    Total= harga*qty+0.01
    print(">>Total Tagihan = Rp." , Total)
elif pilihan=="b":
    Total= harga*qty+0.01
    print(">>Total Tagihan = Rp." , Total)
elif pilihan=="c":
    Total= harga*qty+0.01
    print(">>Total Tagihan = Rp." , Total)
elif pilihan=="d":
    Total= harga*qty+0.01
    print(">>Total Tagihan = Rp." , Total)
elif pilihan=="e":
    Total= harga*qty+0.01
    print(">>Total Tagihan = Rp." , Total)

#Total Tagihan dengan diskon apabila jumlah pembelian mencapai >=200.000
if Total>=200000:
    Total= Total-0.05*Total
    print(">>Total Harga = Rp." , Total)
Bayar = int(input("Jumlah Nominal Uang = Rp."))
Kembalian = (Bayar-Total)
print(">>Uang Kembalian = Rp." , Kembalian)