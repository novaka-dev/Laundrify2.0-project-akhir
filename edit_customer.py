import os
import json
from manage_data import *


# edit customer
def edit_customer():
    customers = data_json(FILE_CUSTOMER)

    print("="*105)
    print("                  DATA CUSTOMER")
    print("="*105)
    print(f"{"Id Customer":15} {"Nama Customer":30} {"No Telpon":20} {"Alamat"}")
    print("-"*105)
    for data in customers:
        print(f"{data['id']:<15} {data['name']:<30} {data['phone']:<20} {data['address']}")
    print("-"*105)

    while True:
        id_customer = input("Masukkan Id Customer🤔🤔: ")
        data_pelanggan = next((x for x in customers if x['id'] == id_customer), None)

        if not data_pelanggan:
            print("Id Customer tidak ditemukan!😡😡")
            continue
        
        print("\n         EDIT DATA CUSTOMER")
        # nama_cus = input("Input Nama Customer Baru (ENTER jika tidak ingin diubah):").strip()
        # phone_cus = input("Input No Telp Customer Baru  (ENTER jika tidak ingin diubah):").strip()
        # address_cus = input("Input Alamat Customer Baru (ENTER jika tidak ingin diubah):").strip()
        while True:
            nama_cus = input("Input Nama Customer Baru (ENTER jika tidak ingin diubah):").strip()
            if nama_cus == "":
                break
            elif not nama_cus.replace(" ", "").isalpha():
                print("Nama tidak boleh mengandung angka!")
                continue
            else:
                break
        while True:
            phone_cus = input("Input No Telp Customer Baru  (ENTER jika tidak ingin diubah):").strip()
            if phone_cus.isdigit():  # cek semuanya angka
                break
            elif phone_cus == "":
                break
            else:
                print("Anda harus memasukkan angka!")
                continue
        address_cus = input("Input Alamat Customer Baru (ENTER jika tidak ingin diubah):").strip()
        

        if not nama_cus and not phone_cus and not address_cus:
            print("Tidak ada data yang diubah!👍")
            return

        if nama_cus:
            data_pelanggan['name'] = nama_cus
        if phone_cus:
            data_pelanggan['phone'] = phone_cus
        if address_cus:
            data_pelanggan['address'] = address_cus

        save_data(FILE_CUSTOMER, customers)
        print("Data Customer Berhasil Diubah🤘😎🤘")
        break