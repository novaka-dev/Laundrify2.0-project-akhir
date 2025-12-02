import datetime
import json
import uuid
from manage_data import *

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
        if o.get("order_id") == order_id:
            order = o
            break

    if order is None:
        print("Order tidak ditemukan.")
        return

    if order.get("status") == "LUNAS":
        print("Order ini sudah lunas.")
        return

    total = order.get("total_harga", 0)

    # Detail yang rapi
    print("\nDetail Order:")
    print(f"ID Order     : {order.get('order_id')}")
    print(f"Layanan      : {order.get('layanan', '-')}")
    
    if "berat" in order:
        print(f"Berat        : {order.get('berat')} kg")
        print(f"Harga/kg     : Rp{order.get('harga_per_kg'):,}")

    if "detail" in order and isinstance(order["detail"], dict):
        d = order["detail"]
        print(f"Jumlah       : {d.get('jumlah', '-')} item")
        print(f"Harga/item   : Rp{d.get('harga_satuan', 0):,}")

    print(f"Estimasi     : {order.get('estimasi', '-')}")
    print(f"Total Harga  : Rp{total:,}")

    bayar = int(input("\nMasukkan nominal pembayaran: "))

    if bayar < total:
        print("Uang kurang.")
        return

    kembalian = bayar - total

    print("\nPembayaran Berhasil:")
    print(f"Uang bayar   : Rp{bayar:,}")
    print(f"Total        : Rp{total:,}")
    print(f"Kembalian    : Rp{kembalian:,}")

    # Update status
    order["status"] = "LUNAS"
    save_data(FILE_ORDER, orders)

    print("\nTransaksi berhasil yey horrey\n")

