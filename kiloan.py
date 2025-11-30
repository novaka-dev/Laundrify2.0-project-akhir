import os
import json

DATA_DIR = "data_laundry"
MENU_FILE = os.path.join(DATA_DIR, "kiloan.json")

with open(MENU_FILE, "r", encoding="utf-8") as file:
    data_kiloan = json.load(file)

def kiloan(data):
    print(f"{"kode":8} {"Nama Layanan":25} {"Harga/kg":13} {"Estimasi":13}")
    print("-"* 58)
    for item in data_kiloan:
        print(f'{item["kode"]}. {item["nama"]:<31} Rp{item["harga_per_kg"]:<10,.0f}  {item["est_days"]}')
    print("-"* 58)
    
    while True:
            pilihan = input("masukan input layanan : ")

            if not pilihan.isdigit():
                print("pilihan tidak ada")
                continue

            item = next((x for x in data if x["kode"] == pilihan), None)

            if item is None:
                print("kode tidak ditemukan")
                continue

            break

    while True:
        try:
            kg = float(input("masukan berat(kg) : "))

            if kg <= 0 :
                print("berat harus lebih dari 0")
                continue

            break
        
        except ValueError:
            print("harus angka contoh 2/3")

    total = kg * item["harga_per_kg"]

    return{
        "layanan": item["nama"],
        "harga_per_kg": item["harga_per_kg"],
        "estimasi": item["est_days"],
        "berat": kg,
        "total_harga": total
    }

transaksi = kiloan(data_kiloan)

print(f"layanan     : {transaksi['layanan']}")
print(f"Berat       : {transaksi['berat']}")
print(f"Harga/kg    : Rp{transaksi['harga_per_kg']}")
print(f"Total Bayar : {transaksi['total_harga']}")
print(f"estimasi    : {transaksi['estimasi']}")