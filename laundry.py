# print("****************************************************")
# print("                    ✦  Kelompok 2  ✦             ")
# print("----------------------------------------------------")
# print("   -Muhamad Adli Akbar                              ")
# print("   -Novaka Rizky Heny Saputra                       ")
# print("   -Restu Aji Prasetyo                              ")
# print("   -Rifky Al Adli                                   ")
# print("   -Arya Luqmannul Hakim                            ")
# print("****************************************************")

import random
data_pelanggan = []
keluar = True
while keluar:
    print("                     ★ LAUNDRIFY ★                 ")
    print("****************************************************")
    print(f"{"Kode":8} {"Nama Layanan":25} {"Harga/kg":15} {"Estimasi":15}")
    print("-" * 63)
    print(f"{"SV-CG":8} {"Cuci + Gosok (Reguler)":25} {"Rp10.000":15} {"2":15}")
    print(f"{"SV-EX":8} {"Cuci + Gosok (Express)":25} {"Rp15.000":15} {"1":15}")
    print(f"{"SV-C":8} {"Cuci Kering":25} {"Rp8.000":15} {"2":15}")
    print("-" * 63)
    print("1.  Tambah Pelanggan")
    print("2.  Lihat Pelanggan")
    print("3.  Buat Order")
    print("4.  Lihat Daftar Order")
    print("5.  Lihat Detail Order")
    print("6.  Update Status Order")
    print("7.  Pembayaran Order")
    print("8.  Laporan Pendapatan")
    print("9.  Laporan Pending")
    print("10. Cetak Struk") #Ini mau disatuin sama menu ke-7 atau kaga?
    print("0.  Keluar Program")
    menu = int(input("Pilih Menu:"))
    #Tambah Pelanggan
    if menu == 1:
         nama_pelanggan = input("Nama Pelanggan: ")
         no_telp = input("Nomor Telpon: ")
         cust_id = f"CU-{random.randrange(000, 999)}"
         data_pelanggan.append((nama_pelanggan, no_telp, cust_id))

         print(f"Pelanggan berhasil ditambahkan dengan ID: {cust_id}")
         for i, item in enumerate(data_pelanggan, start=1):
             nama_pelanggan, no_telp, cust_id = item
             # print(f"{nama_pelanggan:8} {no_telp:25} {cust_id:15}")

             #Tes kalo datanya udah kesimpen di list
             print(f"nama pelanggan: {nama_pelanggan}")
             print(f"nomor telepon: {no_telp}")
             print(f"customer id: {cust_id}")
    else:
        keluar = False