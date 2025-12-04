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
from tambah_layanan import *
from edit_layanan import *
from lihat_detail_order import *
from pembayaran_order import *
from laporan_pendapatan import *
import random

import os
from manage_data import *

DATA_DIR = "data_laundry"
CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.json")

def pilih_customer():
    customers = data_json(CUSTOMERS_FILE)

    print("\n=== DATA CUSTOMER ===")
    if len(customers) == 0:
        print("(Belum ada customer)")

    # for c in customers:
    #     print(f"{c['id']} - {c['name']} ({c['phone']}) {c['address']}")

    #edit
    print(f'{"ID Customer":20} {"Nama":30} {"No. Telp":20} {"Alamat":10}')
    print("-" * 130)

    for c in customers:
        print(f'{c["id"]:<20} {c["name"]:<30} {c["phone"]:<20} {c["address"]:<10}')
    #edit

    opsi = input("\nPakai customer existing? (y/n): ").lower()

    if opsi == "y":
        while True:
            cid = input("Masukkan ID customer: ")
            cocok = next((c for c in customers if c["id"] == cid), None)
            if cocok:
                return cocok
            print("ID tidak ditemukan, coba lagi.")
    else:
        nama = input("Nama customer: ")
        telepon = input("No. telepon: ")
        alamat = input("Alamat: ")
        cus_id = gen_id("CUS")

        new_cus = {
            "id": cus_id,
            "name": nama,        # PERBAIKAN
            "phone": telepon,
            "address": alamat
        }

        customers.append(new_cus)
        save_data(CUSTOMERS_FILE, customers)
        print("-" * 80)
        print("Data Customer berhasil disimpan")
        print("-" * 80)
        return new_cus

# def pilih_customer():
    customers = data_json(CUSTOMERS_FILE)

    print("\n=== DATA CUSTOMER ===")
    if len(customers) == 0:
        print("(Belum ada customer)")

    for c in customers:
        print(f"{c['id']} - {c['name']} ({c['phone']}) {c['address']}")

    opsi = input("\nPakai customer existing? (y/n): ").lower()

    if opsi == "y":
        while True:
            cid = input("Masukkan ID customer: ")
            cocok = next((c for c in customers if c["id"] == cid), None)
            if cocok:
                return cocok
            print("ID tidak ditemukan, coba lagi.")
    else:
        nama = input("Nama customer: ")
        telepon = input("No. telepon: ")
        alamat = input("Alamat: ")
        cus_id = gen_id("CUS")

        new_cus = {
            "id": cus_id,
            "name": nama,        # PERBAIKAN
            "phone": telepon,
            "address": alamat
        }

        customers.append(new_cus)
        save_data(CUSTOMERS_FILE, customers)
        print("-" * 80)
        print("Data Customer berhasil disimpan")
        print("-" * 80)
        return new_cus

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
      customer = pilih_customer()
      # layanan kiloan
      if kategori == 1 :
          transaksi = kiloan(customer)
          print_ringkasan_kiloan(transaksi)

      # Layanan Satuan
      elif kategori == 2:
          transaksi = satuan(customer)
      else:
          print("Kategori Tidak Valid!")
          continue

      #tekan enter maka akan kembali
      input("tekan ENTER untuk kembali ke menu...")
      print("\n")

    #Lihat Detail Order
    elif menu == 2:
        update_order()

    #Pembayaran Order
    elif menu == 3:
        pembayaran = pembayaran_order()
        input("tekan ENTER untuk kembali ke menu...")
        print("\n")

    #Tambah Layanan
    elif menu == 4:
        tambah_layanan()

    #Edit Layanan
    elif menu == 5:
        edit_layanan()

    #Laporan Pendapatan
    elif menu == 6:
        menu_laporan()

    #Keluar Program
    elif menu == 0:
        keluar = False