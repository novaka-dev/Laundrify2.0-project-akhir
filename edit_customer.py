import os
import json
from manage_data import *

def edit_customer():
    orders = data_json(FILE_ORDER)

    print("="*105)
    print("                  DATA CUSTOMER")
    print("="*105)
    print(f"{'Id Customer':15} {'Nama Customer':30} {'No Telpon':20} {'Alamat'}")
    print("-"*105)

    tampil = set()
    for data in orders:
        cid = data['customer']['id']
        if cid not in tampil:
            tampil.add(cid)
            c = data['customer']
            print(f"{c['id']:<15} {c['name']:<30} {c['phone']:<20} {c['address']}")

    print("-"*105)
    while True:
        id_customer = input("Masukkan Id Customer🤔🤔: ").strip()
        data_pelanggan = next((x for x in orders if x['customer']['id'] == id_customer), None)

        if not data_pelanggan:
            print("Id Customer tidak ditemukan!😡😡")
            continue

        print("\n         EDIT DATA CUSTOMER")
        while True:
            nama_cus = input("Input Nama Customer Baru (ENTER jika tidak ingin diubah): ").strip()
            if nama_cus == "":
                break
            elif not nama_cus.replace(" ", "").isalpha():
                print("Nama tidak boleh mengandung angka!")
            else:
                break

        while True:
            phone_cus = input("Input No Telp Customer Baru (ENTER jika tidak ingin diubah): ").strip()
            if phone_cus == "" or phone_cus.isdigit():
                break
            else:
                print("Anda harus memasukkan angka!")

        address_cus = input("Input Alamat Customer Baru (ENTER jika tidak ingin diubah): ").strip()

        if not nama_cus and not phone_cus and not address_cus:
            print("Tidak ada data yang diubah!👍")
            return

        # 🔥 UPDATE SEMUA ORDER
        for order in orders:
            if order['customer']['id'] == id_customer:
                if nama_cus:
                    order['customer']['name'] = nama_cus
                if phone_cus:
                    order['customer']['phone'] = phone_cus
                if address_cus:
                    order['customer']['address'] = address_cus

        save_data(FILE_ORDER, orders)
        print("Data Customer Berhasil Diubah 🤘😎🤘")
        return
