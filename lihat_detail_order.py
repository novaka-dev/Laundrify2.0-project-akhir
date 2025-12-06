import os
import json
from datetime import *
from satuan import format_tanggal
from manage_data import *
import uuid

def detail_order():
    orders = data_json(FILE_ORDER)

    if not orders:
        print("Tidak ada data order.")
        return None

    print("\n===== DAFTAR ORDER =====\n")

    for i, order in enumerate(orders, start=1):
        tipe = order.get("tipe", "")
        detail = order.get("detail", {})

        # ini buat tentuin berat sama kiloan
        if tipe == "kiloan":
            qty_label = f"Berat           : {detail.get('berat', 0)} Kg"
        else:  # ini satuan nih
            qty_label = f"Jumlah          : {detail.get('jumlah', 0)} item"

        print(f"{i}.ID ORDER        : {order.get('id', '')}")
        print(f"   TIPE            : {tipe}")
        print(f"   CUSTOMER        : {order['customer'].get('name', '')}")
        print(f"   NO TELP         : {order['customer'].get('phone', '')}")
        print(f"   ALAMAT          : {order['customer'].get('address', '')}")
        print(f"   LAYANAN         : {detail.get('layanan', '')}")
        print(f"   {qty_label}")
        print(f"   TOTAL HARGA     : Rp{int(detail.get('total_harga', 0)):,}")
        print(f"   TANGGAL ORDER   : {format_tanggal(order.get('tanggal_diterima', ''))}")
        print(f"   ESTIMASI SELESAI: {format_tanggal(order.get('tanggal_selesai', ''))}")
        print(f"   STATUS          : {order.get('status', '')}")
        print("-" * 50)

    while True:
        pilihan = input("\nPilih nomor order untuk update. Pilih 0 untuk kembali ke menu utama: ")
        try:
            pilihan = int(pilihan)
        except ValueError:
            print("Anda harus memasukkan angka!")
            continue

        if pilihan == 0:
            return None
                
        if 1 <= pilihan <= len(orders):
            selected = orders[pilihan - 1]
            
            # cek status pembayaran
            if selected['status'].lower() == "belum dibayar":
                print("Order ini belum dibayar. Harap Lakukan pembayaran terlebih dahulu.")
                continue
            return selected
            
        else:
            print("Nomor yang anda masukkan tidak sesuai dengan data yang ada!")
            continue
            

def update_order():
    orders = data_json(FILE_ORDER)
    selected = detail_order()

    if not selected:
        # print("Batal update.")
        return
    
    print("\n=== UPDATE ORDER ===")
    print(f"ID Order       : {selected['id']}")
    print(f"Nama Pelanggan : {selected['customer']['name']}")
    print(f"Status Saat Ini: {selected['status']}")

    stats2 = ["Belum dibayar","Proses", "Selesai", "Diantar", "Diterima"]
    while True:
        new_status = input("Masukkan status baru (Proses / Selesai / Diantar / Diterima): ")
        if new_status not in stats2:
            print("Input yang anda masukkan tidak valid!")
            continue
        else:
            selected["status"] = new_status

            # Update ke list asli
            for i, order in enumerate(orders):
                if order["id"] == selected["id"]:
                    orders[i] = selected
                    break

            save_data(FILE_ORDER, orders)

            print("\nStatus berhasil diperbarui!\n")
            break