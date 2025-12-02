import os
import json
from manage_data import *
import uuid

def detai_order():
    orders = data_json(FILE_ORDER)

    print(f"{"No":3} {'Id Pelanggan':15} {'Id Order':15} {'Nama Pelanggan':20} {'No Telp':15} {'Alamat':15} {'Tanggal Estimasi'}")
    print("-" * 105)

    # Loop tiap order
    for i, order in enumerate(orders , start=1):
        id_pelanggan = order["customer"].get("id", "")
        id_order = order.get("order_id", "")
        nama = order["customer"].get("name", "")
        no_telp = order["customer"].get("no_telp", "")
        alamat = order["customer"].get("alamat", "")
        tanggal_estimasi = order.get("tanggal_diterima", "")

        print(f"{i:<3} {id_pelanggan:15} {id_order:15} {nama:20} {no_telp:15} {alamat:15} {tanggal_estimasi}")

    print("-" * 105)

detai_order()