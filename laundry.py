from satuan import *
from edit_customer import *
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
FILE_CUSTOMER = os.path.join(DATA_DIR, "customers.json")

def pilih_customer():
    customers = data_json(FILE_CUSTOMER)

    # print("\n=== DATA CUSTOMER ===")
    if len(customers) == 0:
        
        while True:
            nama2 = input("Nama customer: ")
            if not nama2.replace(" ", "").isalpha():
                print("Nama tidak boleh mengandung angka!")
                continue
            else:
                # nama3 = nama2
                break

        while True:
            telepon2 = input("No. telepon: ")
            try:
                telepon2 = int(telepon2)
                break
            except ValueError:
                print("Anda harus memasukkan angka!")
                continue
        while True:
            alamat2 = input("Alamat: ")
            if alamat2 == "":
                print("Alamat wajib diisi!")
                continue
            else:
                break
        cus_id2 = gen_id("CUS")

        new_cus2 = {
            "id": cus_id2,
            "name": nama2,        # PERBAIKAN
            "phone": telepon2,
            "address": alamat2
        }

        customers.append(new_cus2)
        save_data(FILE_CUSTOMER, customers)
        print("-" * 80)
        print("Data Customer berhasil disimpan")
        print("-" * 80)
    print("\n=== DATA CUSTOMER ===")
    print(f'{"ID Customer":20} {"Nama":30} {"No. Telp":20} {"Alamat":10}')
    print("-" * 130)

    for c in customers:
        print(f'{c["id"]:<20} {c["name"]:<30} {c["phone"]:<20} {c["address"]:<10}')

    while True:
        opsi = input("\nPilih customer yang sudah ada? (y/n): ").lower()

        if opsi == "y":
            while True:
                cid = input("Masukkan ID customer: ")
                cocok = next((c for c in customers if c["id"] == cid), None)
                if cocok:
                    return cocok
                print("ID tidak ditemukan, coba lagi.")
        elif opsi == "n":
            # nama = input("Nama customer: ")
            # telepon = input("No. telepon: ")
            # alamat = input("Alamat: ")
            while True:
                nama = input("Nama customer: ")
                if not nama.replace(" ", "").isalpha():
                    print("Nama tidak boleh mengandung angka!")
                    continue
                else:
                    # nama3 = nama2
                    break

                while True:
                    telepon = input("No. telepon: ")
                    try:
                        telepon = int(telepon)
                        break
                    except ValueError:
                        print("Anda harus memasukkan angka!")
                        continue
                while True:
                    alamat = input("Alamat: ")
                    if alamat == "":
                        print("Alamat wajib diisi!")
                        continue
                    else:
                        break
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
        else:
            print("Input tidak valid!")
            continue

# data_pelanggan = []
keluar = True
while keluar:
    print("****************************************************")
    print("                     ★  LAUNDRIFY ★                 ")
    print("****************************************************")
    print("1.  Buat Order")
    print("2.  Lihat Detail Order")
    print("3.  Edit Data Customer")
    print("4.  Pembayaran Order")
    print("5.  Tambah Layanan")
    print("6.  Edit Layanan")
    print("7.  Laporan Pendapatan")
    print("0.  Keluar Program")
    menu = input("Pilih Menu:")

    #Tambah Pelanggan
    if menu == "1":
        print("\n=== PILIH KATEGORI LAYANAN ===")
        print("1. Laundry Kiloan")
        print("2. Laundry Satuan")
        print("0. Kembali ke Menu Utama")

        back = False
        while True:
            kategori = input("Silahkan Memilih Kategori Layanan : ")
        
            if kategori == "1" or kategori == "2":
                break
            elif kategori == "0":
                back = True
                break
            else:
                print("Kode yang anda masukkan tidak sesuai dengan kategori yang ada!😡\n")

        if back:
            continue
        customer = pilih_customer()
        # layanan kiloan
        if kategori == "1" :
            transaksi = kiloan(customer)
            if transaksi is None:
                continue
            ringkasan_kiloan(transaksi)
        # Layanan Satuan
        elif kategori == "2":
            transaksi = satuan(customer)
            if transaksi is None:
                continue
        #tekan enter maka akan kembali
        input("tekan ENTER untuk kembali ke menu...")
        print("\n")

    #Lihat Detail Order
    elif menu == "2":
        update_order()

    # edit data order
    elif menu == "3":
        edit_customer()

    #Pembayaran Order
    elif menu == "4":
        pembayaran = pembayaran_order()
        input("tekan ENTER untuk kembali ke menu...")
        print("\n")

    #Tambah Layanan
    elif menu == "5":
        tambah_layanan()

    #Edit Layanan
    elif menu == "6":
        edit_layanan()

    #Laporan Pendapatan
    elif menu == "7":
        menu_laporan()

    #Keluar Program
    elif menu == "0":
        keluar = False

    else:
        print("Kode yang anda masukkan tidak sesuai dengan menu yang ada!\n\n")