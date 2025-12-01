import os
import json
from manage_data import *

DATA_DIR = "data_laundry"
MENU_FILE = os.path.join(DATA_DIR, "satuan.json")
CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.json")
ORDERS_FILE = os.path.join(DATA_DIR, "orders1.json")

with open(MENU_FILE, "r", encoding="utf-8") as file:
    data_satuan = json.load(file)

# ============================================
#                PILIH CUSTOMER
# ============================================
def pilih_customer():
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
        # daftar baru
        nama = input("Nama customer: ")
        telepon = input("No. telepon: ")
        alamat = input("Alamat: ")

        new_cus = {
            "id": gen_id("CUS"),
            "nama": nama,
            "telepon": telepon,
            "alamat": alamat
        }

        customers.append(new_cus)
        save_data(CUSTOMERS_FILE, customers)

        return new_cus


# ============================================
#         PILIH LAYANAN SATUAN
# ============================================
def satuan():
    print("\n=== TRANSAKSI SATUAN ===")
    customer = pilih_customer()

    # Tampilkan menu layanan
    print(f'{"kode":8} {"Nama Layanan":25} {"Harga":13} {"Estimasi":10}')
    print("-" * 60)

    for item in data_satuan:
        print(f'{item["kode"]:<8} {item["nama"]:<25} Rp{item["harga_satuan"]:<10,.0f} {item["est_days"]:<10}')

    # Pilih layanan
    while True:
        kode = input("Pilih layanan: ")
        item = next((x for x in data_satuan if x["kode"] == kode), None)
        if item:
            break
        print("Kode tidak ditemukan!")

    jumlah = int(input("Masukkan jumlah item : "))
    total = jumlah * item["harga_satuan"]

    # RETURN RINGKASAN
    ringkasan = {
        "layanan": item["nama"],
        "harga_satuan": item["harga_satuan"],
        "jumlah": jumlah,
        "estimasi": item["est_days"],
        "total_harga": total
    }

    print("\n=== RINGKASAN ORDER SATUAN ===")
    print(f"Layanan      : {ringkasan['layanan']}")
    print(f"Harga/unit   : Rp{ringkasan['harga_satuan']}")
    print(f"Jumlah       : {ringkasan['jumlah']}")
    print(f"Estimasi     : {ringkasan['estimasi']} hari")
    print(f"Total Harga  : Rp{ringkasan['total_harga']}")

    # simpan order ke json
    orders = data_json(ORDERS_FILE)
    new_order = {
        "id": gen_id("ORD-SAT"),
        "tipe": "satuan",
        "customer": customer,
        "detail": ringkasan
    }
    orders.append(new_order)
    save_data(ORDERS_FILE, orders)

    return new_order

# ======================================
#        RINGKASAN ORDER DI SINI
# ======================================
# def print_ringkasan_satuan(transaksi):
#     print("\n===== RINGKASAN ORDER (SATUAN) =====")
#     print(f"Jenis Layanan : {transaksi['layanan']}")
#     print(f"Jumlah        : {transaksi['jumlah']} item")
#     print(f"Harga Satuan  : Rp{transaksi['harga_satuan']:,}")
#     print(f"Total Harga   : Rp{transaksi['total_harga']:,}")
#     print(f"Estimasi      : {transaksi['estimasi']}")
#     print("====================================\n")
