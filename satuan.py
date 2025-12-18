import os
import json
from datetime import *
from manage_data import *

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
    print("\n=== LAYANAN LAUNDRY SATUAN ===")

    # Tampilkan menu layanan
    print(f'{"kode":8} {"Nama Layanan":25} {"Harga":13} {"Estimasi":10}')
    print("-"* 80)

    for item in data_satuan:
        print(f'{item["kode"]:<8} {item["nama"]:<25} Rp{item["harga_satuan"]:<10,.0f} {item["est_days"]:<10}')
    print("-"* 80)
    print("0.       Keluar")

    # Pilih layanan
    while True:
        kode = input("Pilih layanan: ")
        if kode == "0":
            return None
        item = next((x for x in data_satuan if x["kode"] == kode), None)
        if item is None:
            print("Layanan tidak ditemukan!")
            continue
        break

    while True:
        try:
            jumlah = int(input("Masukkan jumlah item : "))

            if jumlah <= 0:
                print("jumlah harus lebih dari 0!😡")
                continue
            break

        except ValueError:
            print("input harus angka!😡 2/3")

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
    print(f"Harga/unit          : Rp{ringkasan['harga_satuan']:,}")
    print(f"Jumlah              : {ringkasan['jumlah']}")
    print(f"Estimasi            : {ringkasan['estimasi']}")
    print(f"Tanggal order Dibuat: {format_tanggal(today)}")
    print(f"Tanggal Selesai     : {format_tanggal(tanggal_selesai)}")
    print(f"Total Harga         : Rp{ringkasan['total_harga']:,}")

    # simpan order ke json
    orders = data_json(FILE_ORDER)
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
    save_data(FILE_ORDER, orders)

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
