import json
from satuan import format_tanggal
from manage_data import *
from typing import List , Dict , Any

folder_path = "data_laundry/receipts"
os.makedirs(folder_path, exist_ok=True)

def pembayaran_order():
    orders = data_json(FILE_ORDER)

    if not orders:
        print("Belum ada order.🤔🤔")
        return

    print("\n================================================= PEMBAYARAN ORDER =================================================")
    print(f"{'ID Order':20} {'Nama Pelanggan':20} {'Layanan':30} {'Status':15} {'Tanggal Diterima'}")
    print("====================================================================================================================")
    for i in orders:
        print(
            f"{i['id']:20} "
            f"{i['customer']['name']:20} "
            f"{i['detail']['layanan']:30} "
            f"{i['status']:15} "
            f"{format_tanggal(i['tanggal_diterima'])}"
        )
    print("="*116)

    # ulang = True
    # while ulang:
    #     order_id = input("Masukkan ID Order: ").strip()

    #     # Cari order
    #     order = None
    #     for o in orders:
    #         # if o.get("id") == order_id:
    #         #     order = o
    #         #     break
    #         if o["id"] == order_id:
    #             order = o

    #     if order is None:
    #         print("Order tidak ditemukan.")
    #         ulang = False

    #     # if order.get("status") == "P":
    #     #     print("Order ini sudah lunas.")
    #     #     return
    #     if order["status"] == "P":
    #         print("Order ini sudah lunas.")
    #         return
    
    while True:
            order_id = input("Masukkan ID Order: ").strip()
            cocok = next((c for c in orders if c["id"] == order_id), None)
            if cocok is None:
                print("ID tidak ditemukan, coba lagi🤘🤪🤘.\n")
                continue
            if cocok["status"] == "Lunas":
            # if cocok.get("status") == "Lunas":
                print("Order ini sudah lunas🤘😎🤘.\n")
                continue
            else:
                # return cocok
                # detail = c.get("detail", {})
                detail = cocok.get("detail", {})
                cstm = cocok.get("customer", {})
                total  = detail.get("total_harga", 0)
                break
            # print("ID tidak ditemukan, coba lagi.")

    # detail = order.get("detail", {})
    # total  = detail.get("total_harga", 0)

   
    print("\nDetail Order:")
    print(f"ID Order     : {cocok.get('id')}")
    print(f"Customer     : {cstm.get('name')}")
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

    print(f"Estimasi     : {detail.get('estimasi', '-')} jam")
    print(f"Total Harga  : Rp{total:,}")

    # ============================
    #        LOOP PEMBAYARAN
    # ============================
    while True:
        try:
            bayar = int(input("\nMasukkan nominal pembayaran: "))
        except ValueError:
            print("transaksi gagal. Coba lagi🤪🤪.")
            return

        if bayar < total:
            print(f"transaksi gagal. Uang bayar kurang Rp{total:,}. Coba lagi🤘🤪🤘.")
        else:
            break

    # Hitung kembalian
    kembalian = bayar - total

    #struk pembayaran

    # Update status jadi LUNAS
    cocok['status'] = "Lunas"
    save_data(FILE_ORDER, orders)

    print("\nTransaksi berhasil yey horrey🤘🤪🤘!\n")

    # ubah menjadi file txt
    nama_file = os.path.join(folder_path , f"{cocok['id']}.txt")
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write(struk_pembayaran(cocok, bayar , kembalian))
    print(struk_pembayaran(cocok , bayar , kembalian))

def struk_pembayaran(order: Dict[str, Any], bayar: int, kembalian: int) -> str:
    struk = []
    struk.append("=" * 45)
    struk.append("              NOTA LAUNDRY")
    struk.append("=" * 45)
    struk.append(f"ID Order       : {order.get('id','-')}")

    cust = order.get("customer", {})
    struk.append(f"Nama Customer  : {cust.get('name','-')}")

    tipe = order.get("tipe", "-")
    detail = order.get("detail", {})
    struk.append(f"Tipe Layanan   : {tipe.upper()}")
    struk.append(f"Nama Layanan   : {detail.get('layanan','-')}")

    if tipe == "kiloan":
        struk.append(f"Berat          : {detail.get('berat')} kg")
        struk.append(f"Harga/kg       : {detail.get('harga_per_kg' , 0):,}")
    elif tipe == "satuan":
        struk.append(f"Jumlah         : {detail.get('jumlah')} pcs")
        struk.append(f"Harga Satuan   : {detail.get('harga_satuan'):,}")

    struk.append("")
    total = detail.get("total_harga", 0)
    struk.append(f"Subtotal       : {total:,}")
    struk.append(f"Bayar          : {bayar:,}")
    struk.append(f"Kembalian      : {kembalian:,}")
    struk.append(f"Estimasi       : {detail.get('estimasi','-')}")
    struk.append("")

    struk.append(f"Tanggal Terima : {order.get('tanggal_diterima','-')}")
    struk.append(f"Tanggal Selesai: {order.get('tanggal_selesai','-')}")
    struk.append("")
    struk.append("=" * 45)
    struk.append("    TERIMA KASIH TELAH MENGGUNAKAN")
    struk.append("         LAYANAN LAUNDRY KAMI")
    struk.append("=" * 45)

    return "\n".join(struk)

pembayaran_order()