import os
import json

DATA_DIR = "data_laundry"
MENU_FILE = os.path.join(DATA_DIR, "satuan.json")

with open(MENU_FILE, "r", encoding="utf-8") as file:
    data_satuan = json.load(file)


def satuan():
    # Tampilkan menu
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
    return {
        "layanan": item["nama"],
        "harga_satuan": item["harga_satuan"],
        "jumlah": jumlah,
        "estimasi": item["est_days"],
        "total_harga": total
    }

# ======================================
#        RINGKASAN ORDER DI SINI
# ======================================
def print_ringkasan_satuan(transaksi):
    print("\n===== RINGKASAN ORDER (SATUAN) =====")
    print(f"Jenis Layanan : {transaksi['layanan']}")
    print(f"Jumlah        : {transaksi['jumlah']} item")
    print(f"Harga Satuan  : Rp{transaksi['harga_satuan']:,}")
    print(f"Total Harga   : Rp{transaksi['total_harga']:,}")
    print(f"Estimasi      : {transaksi['estimasi']}")
    print("====================================\n")
