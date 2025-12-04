import json
from manage_data import data_json, save_data, FILE_ORDER

def pembayaran_order():
    orders = data_json(FILE_ORDER)

    if not orders:
        print("Belum ada order.")
        return

    print("\n=== PEMBAYARAN ORDER ===")

    order_id = input("Masukkan ID Order: ").strip()

    # Cari order
    order = None
    for o in orders:
        if o.get("id") == order_id:
            order = o
            break

    if order is None:
        print("Order tidak ditemukan.")
        return

    if order.get("status") == "P":
        print("Order ini sudah lunas.")
        return

    detail = order.get("detail", {})
    total  = detail.get("total_harga", 0)

    print("\nDetail Order:")
    print(f"ID Order     : {order.get('id')}")
    print(f"Layanan      : {detail.get('layanan', '-')}")

    # ==============================
    #   AUTO DETECT KILOAN / SATUAN
    # ==============================
    if "berat" in detail:   # ← KILOAN
        print(f"Berat        : {detail.get('berat')} kg")
        print(f"Harga/kg     : Rp{detail.get('harga_per_kg', 0):,}")

    if "jumlah" in detail:  # ← SATUAN
        print(f"Jumlah       : {detail.get('jumlah')} item")
        print(f"Harga/item   : Rp{detail.get('harga_satuan', 0):,}")

    print(f"Estimasi     : {detail.get('estimasi', '-')} hari")
    print(f"Total Harga  : Rp{total:,}")

    # ============================
    #        LOOP PEMBAYARAN
    # ============================
    while True:
        try:
            bayar = int(input("\nMasukkan nominal pembayaran: "))
        except ValueError:
            print("transaksi gagal. Coba lagi.")
            continue

        if bayar < total:
            print(f"transaksi gagal. Uang bayar kurang Rp{total:,}. Coba lagi.")
        else:
            break

    # Hitung kembalian
    kembalian = bayar - total

    print("\nPembayaran Berhasil:")
    print(f"Uang bayar   : Rp{bayar:,}")
    print(f"Total        : Rp{total:,}")
    print(f"Kembalian    : Rp{kembalian:,}")

    # Update status jadi LUNAS
    order["status"] = "LUNAS"
    save_data(FILE_ORDER, orders)

    print("\nTransaksi berhasil yey horrey!\n")
