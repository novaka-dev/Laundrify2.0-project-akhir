from manage_data import * #data_json, save_data, FILE_KILOAN, FILE_ORDER, FILE_CUSTOMER
from datetime import *
import math
import json
import uuid
from satuan import *

# list customer
def list_customers():
    customers = data_json(FILE_CUSTOMER)
    if not customers:
        print("Belum ada pelanggan.")
        return
    print(f"{'ID':10} {'Nama':25} {'No.Telp':15} {'Alamat':15}")
    print("-"*55)
    for c in customers:
        print(f"{c['id']:10} {c['name'][:25]:25} {c.get('phone','')[:15]:15} {c['address'][:25]:25}")

# def pembulatan(berat):
#     return math.ceil(berat * 2) /2

# kiloan
def kiloan(customer):
    data = data_json(FILE_KILOAN)
    if len(data) == 0:
        print("Layanan belum ada, silahkan tambahkan layanan terlebih dahulu!\n")
        while True:
            nama = input("Input Nama Menu Baru (Contoh: Cuci + Setrika): ")
            if nama == "":
                print("Nama menu tidak boleh kosong!")
                continue
            else:
                break
        while True:
            harga = input("Input harga Menu Baru (Contoh: 12000) : ")
            if type(harga) == str:
                try:
                    harga = float(harga)
                    break
                except ValueError:
                    print("Inputan harus berupa angka!")
                    continue
            elif harga == "":
                print("Harga menu tidak boleh kosong!")
                continue
            else:
                break
        while True:
            estimasi = input("Input Estimasi Menu Baru (3 jam): ")
            if estimasi.find("jam") == -1:
                print("Inputan harus sesuai contoh!")
                continue
            elif estimasi == "":
                print("Harga menu tidak boleh kosong!")
                continue
            else:
                break
        kode_baru = str(len(data) + 1)

        layanan = {
            "kode" : kode_baru,
            "nama" : nama,
            "harga_per_kg" : harga,
            "est_days" : estimasi,
        }

        data.append(layanan)
        save_data(FILE_KILOAN, data)

        print("Menu Layanan Kiloan Berhasil Dibuat🤘😎🤘")

    else:

        print(f'{"kode":8} {"Nama Layanan":41} {"Harga/kg":13} {"Estimasi":13}')
        print("-"* 58)
        for item in data:
            print(f'{item["kode"]:8} {item["nama"]:<41} Rp{item["harga_per_kg"]:<10,.0f}  {item["est_days"]}')
        print(f"0.       Keluar")
        print("-"* 58)

        while True:
                pilihan = input("Pilih layanan : ")

                if not pilihan.isdigit():
                    print("Inputan harus berupa angka!")
                    continue
                if pilihan == "0":
                    return None
                item = next((x for x in data if x["kode"] == pilihan), None)
                if item is None:
                    print("kode tidak ditemukan")
                    continue
                break

        while True:
            try:
                kg = float(input("Masukan berat (kg) : "))

                if kg < 1 :
                    print("Minimal berat harus 1 kg")
                    continue
                break

            except ValueError:
                print("Inputan harus berupa angka")

        # if str(kg).find(".") != -1:
        #     kg = pembulatan(kg)
        total = kg * item["harga_per_kg"]
        stats = ["Belum dibayar","Proses", "Selesai", "Diantar", "Diterima", "Dibayar"]
        # today = datetime.date.today().isoformat()
        today = datetime.now()
        est = item["est_days"]
        index = est.find(" ")
        est = est[:index]
        est = int(est)
        estimasi_hasil = today + timedelta(hours=est)

        today = today.isoformat()
        estimasi_hasil = estimasi_hasil.isoformat()
        # simpan order ke json
        orders = data_json(FILE_ORDER)
        new_order = {
            "id": gen_id("ORD-KIL"),
            "tipe": "kiloan",
            "customer": {
                "id": customer["id"],
                "name": customer["name"],
                "phone": customer.get("phone", ""),
                "address": customer.get("address", "")
            },
            "detail": {
                "layanan": item["nama"],
                "harga_per_kg": item["harga_per_kg"],
                "berat": kg,
                "estimasi": int(est),
                "total_harga": total
            },
            "tanggal_diterima": today,
            "tanggal_selesai": estimasi_hasil,
            "status": stats[0]
        }
        print("Order berhasil dibuat!\n")
        orders.append(new_order)
        save_data(FILE_ORDER, orders)

        return new_order
# ringkasan order
def ringkasan_kiloan(transaksi):
    print("\n===== RINGKASAN ORDER (KILOAN) =====")
    print(f"Id order                  : {transaksi['id']}")
    print(f"Nama Pelanggan            : {transaksi['customer']['name']}")

    # Detail inside transaksi["detail"]
    detail = transaksi["detail"]

    print(f"Jenis Layanan             : {detail['layanan']}")
    print(f"Berat                     : {detail['berat']} kg")
    print(f"Harga / kg                : Rp{detail['harga_per_kg']:,}")
    print(f"Total Harga               : Rp{detail['total_harga']:,}")
    print(f"Estimasi                  : {detail['estimasi']} jam")
    print(f"Tanggal Order Dibuat      : {format_tanggal(transaksi['tanggal_diterima'])}")
    print(f"Tanggal Selesai           : {format_tanggal(transaksi['tanggal_selesai'])}")
    print("====================================\n")
