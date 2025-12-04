from manage_data import * #data_json, save_data, FILE_KILOAN, FILE_ORDER, FILE_CUSTOMER
from datetime import *
import json
import uuid
from satuan import *
# def load_json(path):
#     with open(path, "r") as f:
#         try:
#             return json.load(f)
#         except json.JSONDecodeError:
#             return []
# tambahkan pelanggan
# pilih_customer()
# def add_customer():
#     customers = data_json(FILE_CUSTOMER)
#     name = input("Nama pelanggan: ").strip()
#     if not name:
#         print("Nama wajib diisi.")
#         return
#     phone = input("No. HP (opsional): ").strip()
#     address = input("Alamat: ").strip()
#     existing = next((c for c in customers if c["name"].lower()==name.lower() and c.get("phone","")==phone and c["address"]==address), None)
#     if existing:
#         print("Pelanggan sudah terdaftar:", existing["id"])
#         return
#     cid = gen_id("CU")
#     customers.append({"id": cid, "name": name, "phone": phone, "address": address})
#     save_data(FILE_CUSTOMER, customers)
#     print(f"Pelanggan berhasil ditambahkan. ID: {cid}")
#     return cid, name

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

# kiloan
def kiloan(customer):
    data = data_json(FILE_KILOAN)

    print(f'{"kode":8} {"Nama Layanan":25} {"Harga/kg":13} {"Estimasi":13}')
    print("-"* 58)
    for item in data:
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
    stats = ["Belum dibayar","Proses", "Selesai", "Diantar", "Diterima"]
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

    orders.append(new_order)
    save_data(FILE_ORDER, orders)

    return new_order
# ringkasan order
def print_ringkasan_kiloan(transaksi):
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
