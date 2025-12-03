import os
import json
from manage_data import *
import uuid

def detail_order():
  while True:
    orders = data_json(FILE_ORDER)

    print(f"{"No":4} {'Id Pelanggan':18} {'Id Order':18} {'Nama Pelanggan':18} {'No Telp':15} {'Alamat':50} {'Tanggal Estimasi'}")
    print("-" * 150)

    # Loop tiap order
    for i, order in enumerate(orders , start=1):
        id_pelanggan = order["customer"].get("id", "")
        id_order = order.get("id", "")
        nama = order["customer"].get("name", "")
        no_telp = order["customer"].get("phone", "")
        alamat = order["customer"].get("address", "")
        tanggal_estimasi = order.get("tanggal_diterima", "")

        print(f"{i:<4} {id_pelanggan:18} {id_order:18} {nama:18} {no_telp:15} {alamat:50} {tanggal_estimasi}")

    print("-" * 150)
    print("1.  Edit Status Order")
    print("2.  Kembali ke Menu Utama")
    opsi = int(input("Pilih Opsi: "))
    if opsi == 1:
        print("awokawok belum dibikin")
        #Function update order nanti
        return
    else:
        return
    print("\n")