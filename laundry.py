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
          transaksi = kiloan()
          print_ringkasan_kiloan(transaksi)

      # Layanan Satuan
      elif kategori == 2:
          transaksi = satuan()
          print_ringkasan_satuan(transaksi)


      else:
          print("Kategori Tidak Valid!")
          continue

      input("tekan ENTER untuk kembali ke menu...")
      print("\n")
    else:
        keluar = False
