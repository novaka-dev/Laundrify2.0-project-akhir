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
from pembayaran_order import *
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
      cid , name = add_customer()
      print("\n=== PILIH KATEGORI LAYANAN ===")
      print("1. Laundry Kiloan")
      print("2. Laundry Satuan")

      kategori = int(input("Silahkan Memilih Kategori Layanan : "))

      # layanan kiloan
      if kategori == 1 :
          transaksi = kiloan(cid,name)
          print_ringkasan_kiloan(transaksi)

      # Layanan Satuan
      elif kategori == 2:
          transaksi = satuan()
          


      else:
          print("Kategori Tidak Valid!")
          continue

      input("tekan ENTER untuk kembali ke menu...")
      print("\n")

    #Lihat Detail Order
    elif menu == 2:
        pass

    #Pembayaran Order
    elif menu == 3:
        pass

    #Tambah Layanan
    elif menu == 4:
        pass

    #Edit Layanan
    elif menu == 5:
        pass

    #Laporan Pendapatan
    elif menu == 6:
        pass

    #Keluar Program
    elif menu == 0:
        keluar = False
    
