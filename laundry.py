# print("****************************************************")
# print("                    ✦  Kelompok 2  ✦             ")
# print("----------------------------------------------------")
# print("   -Muhamad Adli Akbar                              ")
# print("   -Novaka Rizky Heny Saputra                       ")
# print("   -Restu Aji Prasetyo                              ")
# print("   -Rifky Al Adli                                   ")
# print("   -Arya Luqmannul Hakim                            ")
# print("****************************************************")

from satuan import *
from kiloan import *

import random
data_pelanggan = []
keluar = True
while keluar:
    print("                     ★ LAUNDRIFY ★                 ")
    print("****************************************************")
    print("1.  Buat Order")
    print("2.  Lihat Detail Order")
    print("3.  Pembayaran Order")
    print("4.  Tambah Layanan")
    print("5.  Edit Layanan")
    print("6.  Laporan Pendapatan")
    print("0.  Keluar Program")
    menu = int(input("Pilih Menu:"))
    #Tambah Pelanggan
    if menu == 1:
      print("\n=== PILIH KATEGORI LAYANAN ===")
      print("1. Laundry Kiloan")
      print("2. Laundry Satuan")

      kategori = int(input("Silahkan Memilih Kategori Layanan : "))

      # layanan kiloan
      if kategori == 1 :
          # print("\n=== LAYANAN KILOAN ===")
          # print(f"{"kode":8} {"Nama Layanan":25} {"Harga/kg":15} {"Estimasi":15}")
          # print("-" * 63)
          # print(f"{"1":8} {"Cuci Kering":25} {"Rp8.000":15} {"2 Hari":15}")
          # print(f"{"2":8} {"Cuci + Gosok (Reguler)":25} {"Rp10.000":15} {"3 Hari":15}")
          # print(f"{"3":8} {"Cuci + Gosok (Express)":25} {"Rp15.000":15} {"1 hari":15}")
          # print(f"{"4":8} {"Cuci + Gosok (Super Express)":25} {"Rp20.000":15} {"6 Jam":15}")
          # print("-" * 63)

          # pilihan = int(input("Silahkan Pilih Layanan : "))

          # if pilihan == 1 :
          #     Layanan = "Cuci Kering"
          #     Harga = 8000
          #     estimasi = "2 hari"
          # elif pilihan == 2 :
          #     Layanan = "Cuci + Gosok (Reguler)"
          #     Harga = 10000
          #     estimasi = "3 hari"
          # elif pilihan == 3 :
          #     Layanan = "Cuci + Gosok (Express)"
          #     Harga = 15000
          #     estimasi = "1 hari"
          # elif pilihan == 4 :
          #     Layanan = "Cuci + Gosok (Super Express)"
          #     Harga = 20000
          #     estimasi = "6 jam"
          # else :
          #     print("Pilihan Tidak Valid!")
          #     continue

          # berat = float(input("Masukan berat (kg): "))
          # total = Harga * berat
          transaksi = kiloan()
          print_ringkasan_kiloan(transaksi)

      # Layanan Satuan
      elif kategori == 2:
          # print("\n=== LAYANAN SATUAN ===")
          # print(f"{"kode":8} {"Nama Layanan":25} {"Harga/kg":15} {"Estimasi":15}")
          # print("-" * 63)
          # print(f"{"1":8} {"Selimut":25} {"Rp40.000":15} {"3 Hari":15}")
          # print(f"{"2":8} {"Bed Cover":25} {"Rp30.000":15} {"3 Hari":15}")
          # print(f"{"3":8} {"Jas":25} {"Rp25.000":15} {"3 hari":15}")
          # print(f"{"4":8} {"Karpet":25} {"Rp50.000":15} {"5 Hari":15}")
          # print("-" * 63)

          # pilihan = int(input("Pilih Layanan : "))

          # if pilihan == 1 :
          #     Layanan = "Selimut"
          #     Harga = 40000
          #     estimasi = "3 hari"
          # elif pilihan == 2 :
          #     Layanan = "Bed Cover"
          #     Harga = 30000
          #     estimasi = "3 hari"
          # elif pilihan == 3 :
          #     Layanan = "Jas"
          #     Harga = 25000
          #     estimasi = "3 hari"
          # elif pilihan == 4 :
          #     Layanan = "Karpet"
          #     Harga = 50000
          #     estimasi = "5 hari"
          # else :
          #     print("Pilihan Tidak Valid!")
          #     continue

          # jumlah = int(input("Masukan Jumlah Item: "))
          # total = Harga * jumlah
          transaksi = satuan()
          print_ringkasan_satuan(transaksi)


      else:
          print("Kategori Tidak Valid!")
          continue
      
      input("tekan ENTER untuk kembali ke menu...")
      print("\n")
    else:
        keluar = False
