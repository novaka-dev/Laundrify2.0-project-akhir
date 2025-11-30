import os
import json

DATA_DIR = "data_laundry"
MENU_FILE = os.path.join(DATA_DIR, "satuan.json")

with open(MENU_FILE, "r", encoding="utf-8") as file:
    data_satuan = json.load(file)

def satuan():
    print(f"{"kode":8} {"Nama Layanan":25} {"Harga/kg":13} {"Estimasi":13}")
    for item in data_satuan:
        print(f'{item["kode"]:<8} {item["nama"]:<25} Rp{item["harga_per_kg"]:<11,.0f} {item["est_days"]:<10}')

satuan()