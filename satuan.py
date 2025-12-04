import os
import json
from datetime import *
from manage_data import *

DATA_DIR = "data_laundry"
MENU_FILE = os.path.join(DATA_DIR, "satuan.json")
CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.json")
ORDERS_FILE = os.path.join(DATA_DIR, "orders1.json")

# with open(MENU_FILE, "r", encoding="utf-8") as file:
#     data_satuan = json.load(file)

# ============================================
#         FUNGSI FORMAT TANGGAL
# ============================================
def format_tanggal(dt: str):
    d = datetime.fromisoformat(dt)
    return d.strftime("%d-%m-%Y %H:%M")


# ============================================
#         PILIH LAYANAN SATUAN
# ============================================
def satuan(customer):
    data_satuan = data_json(FILE_SATUAN)
    print("\n=== TRANSAKSI SATUAN ===")

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
    stats = ["Belum dibayar","Proses", "Selesai", "Diantar", "Diterima"]

    # tanggal diterima (hari ini)
    today = datetime.now().isoformat()

    # Ambil angka hari ini dari string
    est_jam = int(item["est_days"].split()[0])

    # estimasi selesai = hari ini + est hari
    tanggal_selesai = (datetime.now() + timedelta(hours=est_jam)).isoformat()

    # === BUAT ID DULUAN ===
    order_id = gen_id("ORD-SAT")

    # RETURN RINGKASAN
    ringkasan = {
        "layanan": item["nama"],
        "harga_satuan": item["harga_satuan"],
        "jumlah": jumlah,
        "estimasi": f"{est_jam} jam",
        "total_harga": total
    }

    print("\n=== RINGKASAN ORDER SATUAN ===")
    print(f"ID Order            : {order_id}")
    print(f"Customer            : {customer['name']}")
    print(f"Layanan             : {ringkasan['layanan']}")
    print(f"Harga/unit          : Rp{ringkasan['harga_satuan']}")
    print(f"Jumlah              : {ringkasan['jumlah']}")
    print(f"Estimasi            : {ringkasan['estimasi']}")
    print(f"Tanggal order Dibuat: {format_tanggal(today)}")
    print(f"Tanggal Selesai     : {format_tanggal(tanggal_selesai)}")
    print(f"Total Harga         : Rp{ringkasan['total_harga']}")

    # simpan order ke json
    orders = data_json(ORDERS_FILE)
    new_order = {
        "id": order_id,
        "tipe": "satuan",
        "customer": customer,
        "detail": ringkasan,
        "tanggal_diterima": today,
        "tanggal_selesai": tanggal_selesai,
        "status": stats[0]
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
