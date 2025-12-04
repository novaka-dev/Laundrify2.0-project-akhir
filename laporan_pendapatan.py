from datetime import datetime, timedelta
from manage_data import *

# ====== LAPORAN HARIAN ======
def laporan_pendapatan_harian():
    orders = data_json(FILE_ORDER)
    hari = datetime.now().strftime("%Y-%m-%d")

    total_pendapatan = 0
    data_filter = []

    for order in orders:
        tanggal = order.get("tanggal_diterima", "").split("T")[0]
        
        if tanggal == hari:
            harga = order["detail"].get("total_harga", 0)

            total_pendapatan += int(harga)

            data_filter.append(order)

    print("\n==== LAPORAN PENDAPATAN HARIAN ====")
    print(f"Tanggal : {hari}")
    print(f"Total pendapatan : Rp{int(total_pendapatan):,}")
    print("-"*60)

    if not data_filter:
        print("Tidak ada transaksi hari ini.")
        return

    for o in data_filter:
        print(f"- {o['id']} | {o['customer']['name']} | Rp{int(o['detail']['total_harga']):,}")


# ====== LAPORAN MINGGUAN ======
def laporan_pendapatan_mingguan():
    orders = data_json(FILE_ORDER)

    hari_ini = datetime.now().date()
    minggu_lalu = hari_ini - timedelta(days=7)

    total_pendapatan = 0
    data_filter = []

    for order in orders:
        tanggal_raw = order.get("tanggal_diterima", "").split("T")[0]

        try:
            tanggal_order = datetime.strptime(tanggal_raw, "%Y-%m-%d").date()
        except:
            continue  # skip data rusak

        if minggu_lalu <= tanggal_order <= hari_ini:
            harga = order["detail"].get("total_harga", 0)
            total_pendapatan += int(harga)
            data_filter.append(order)

    print("\n==== LAPORAN PENDAPATAN MINGGUAN ====")
    print(f"Periode : {minggu_lalu} s/d {hari_ini}")
    print(f"Total pendapatan : Rp{int(total_pendapatan):,}")
    print("-"*60)

    if not data_filter:
        print("Tidak ada transaksi dalam minggu ini.")
        return

    for o in data_filter:
        print(f"- {o['id']} | {o['customer']['name']} | Rp{int(o['detail']['total_harga']):,}")

# ====== LAPORAN BULANAN ======
def laporan_pendapatan_bulanan():
    orders = data_json(FILE_ORDER)

    bulan_ini = datetime.now().strftime("%Y-%m")

    total_pendapatan = 0
    data_filter = []

    for order in orders:
        tanggal_raw = order.get("tanggal_diterima", "")

        if tanggal_raw.startswith(bulan_ini):
            harga = order["detail"].get("total_harga", 0)
            total_pendapatan += int(harga)
            data_filter.append(order)

    print("\n==== LAPORAN PENDAPATAN BULANAN ====")
    print(f"Periode : {bulan_ini}")
    print(f"Total pendapatan : Rp{int(total_pendapatan):,}")
    print("-"*60)

    if not data_filter:
        print("Tidak ada transaksi bulan ini.")
        return

    for o in data_filter:
        print(f"- {o['id']} | {o['customer']['name']} | Rp{int(o['detail']['total_harga']):,}")


# ========= MENU =========
def menu_laporan():
    while True:
        print("\n==== LAPORAN PENDAPATAN ====")
        print("1. Pendapatan Harian")
        print("2. Pendapatan Mingguan")
        print("3. Pendapatan Bulanan")
        print("0. Kembali")
        menu = input("Pilih Menu : ")

        if menu == "1":
            laporan_pendapatan_harian()
        elif menu == "2":
            laporan_pendapatan_mingguan()
        elif menu == "3":
            laporan_pendapatan_bulanan()
        elif menu == "0":
            break
        else:
            print("Menu tidak valid.")