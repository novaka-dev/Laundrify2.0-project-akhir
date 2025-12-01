from manage_data import data_json, save_data, FILE_KILOAN, FILE_ORDER
import datetime

def list_customers():
    customers = load_json(CUSTOMERS_FILE)
    if not customers:
        print("Belum ada pelanggan.")
        return
    print(f"{'ID':10} {'Nama':25} {'Phone':15}")
    print("-"*55)
    for c in customers:
        print(f"{c['id']:10} {c['name'][:25]:25} {c.get('phone','')[:15]:15}")
def kiloan():
    data = data_json(FILE_KILOAN)

    print(f"{"kode":8} {"Nama Layanan":25} {"Harga/kg":13} {"Estimasi":13}")
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
    stats = ["Proses", "Selesai", "Diantar", "Diterima"]
    today = datetime.date.today().isoformat()
    order = {
        "layanan": item["nama"],
        "harga_per_kg": item["harga_per_kg"],
        "estimasi": item["est_days"],
        "berat": kg,
        "total_harga": total,
        "tanggal_diterima": today,
        "status": stats[0]
    }
    data = data_json(FILE_ORDER)
    data.append(order)
    save_data(FILE_ORDER, data)

    return order

def print_ringkasan_kiloan(transaksi):
    print("\n===== RINGKASAN ORDER (KILOAN) =====")
    print(f"Jenis Layanan : {transaksi['layanan']}")
    print(f"Berat         : {transaksi['berat']} kg")
    print(f"Harga / kg    : Rp{transaksi['harga_per_kg']:,}")
    print(f"Total Harga   : Rp{transaksi['total_harga']:,}")
    print(f"Estimasi      : {transaksi['estimasi']}")
    print("====================================\n")

# tanggal_received = datetime.date.today()


