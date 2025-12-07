import json
from satuan import format_tanggal
from manage_data import *
from typing import List , Dict , Any

folder_path = "data_laundry/receipts"
os.makedirs(folder_path, exist_ok=True)

def pembayaran_order():
    orders = data_json(FILE_ORDER)

    belum_dibayar = [order for order in orders if order.get("status") == "Belum dibayar"]

    if not orders:
        print("Belum ada order.🤔🤔")
        return

    if not belum_dibayar:
        print("tidak ada status yang belum dibayar.🤔🤔")
        return

    print("\n================================================= PEMBAYARAN ORDER =================================================")
    print(f"{'ID Order':20} {'Nama Pelanggan':20} {'Layanan':30} {'Status':15} {'Tanggal Diterima'}")
    print("====================================================================================================================")
    for i in belum_dibayar:
        print(
            f"{i['id']:20} "
            f"{i['customer']['name']:20} "
            f"{i['detail']['layanan']:30} "
            f"{i['status']:15} "
            f"{format_tanggal(i['tanggal_diterima'])}"
        )
    print("="*116)
    
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
# <<<<<<< Updated upstream
#             elif cocok["status"] != "Lunas" and cocok['status'] != "Belum dibayar":
#                 print(f"Order ini sudah di {cocok['status']}")
# =======
            elif cocok["status"] != "Lunas" and cocok["status"] != "Belum dibayar":
                print(f"Order ini sudah memiliki status: {cocok['status']}")
# >>>>>>> Stashed changes
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

   
# <<<<<<< Updated upstream
#     print("\nDetail Pemabayaran Order:")
#     print(f"ID Order     : {cocok.get('id')}")
#     print(f"Customer     : {cstm.get('name')}")
#     print(f"Layanan      : {detail.get('layanan', '-')}")
# =======
    print("\nDetail Pembayaran Order:")
    print(f"ID Order       : {cocok.get('id')}")
    print(f"Customer       : {cstm.get('name')}")
    print(f"Layanan        : {detail.get('layanan', '-')}")
# >>>>>>> Stashed changes

    # ==============================
    #   AUTO DETECT KILOAN / SATUAN
    # ==============================
    if "berat" in detail:   # ← KILOAN
        print(f"Berat          : {detail.get('berat')} kg")
        print(f"Harga/kg       : Rp{detail.get('harga_per_kg', 0):,}")

    if "jumlah" in detail:  # ← SATUAN
        print(f"Jumlah       : {detail.get('jumlah')} item")
        print(f"Harga/item       : Rp{detail.get('harga_satuan', 0):,}")

# <<<<<<< Updated upstream
#     print(f"Estimasi     : {detail.get('estimasi', '-')}")
#     print(f"Total Harga  : Rp{total:,}")
# =======
    print(f"Estimasi       : {detail.get('estimasi', '-')}")
    print(f"Tanggal Terima : {format_tanggal(cocok.get('tanggal_diterima', '-'))}")
    print(f"Tanggal Selesai: {format_tanggal(cocok.get('tanggal_selesai', '-'))}")
    print(f"Total Harga    : Rp{total:,}")
# >>>>>>> Stashed changes

    # ============================
    #        LOOP PEMBAYARAN
    # ============================
    while True:
        try:
            bayar = int(input("\nMasukkan nominal pembayaran: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if bayar < total:
            print(f"transaksi gagal. Uang bayar kurang Rp{total - bayar:,}. Coba lagi🤘🤪🤘.")
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

    struk.append(f"Tanggal Terima : {format_tanggal(order.get('tanggal_diterima','-'))}")
    struk.append(f"Tanggal Selesai: {format_tanggal(order.get('tanggal_selesai','-'))}")
    struk.append("")
    struk.append("=" * 45)
    struk.append("    TERIMA KASIH TELAH MENGGUNAKAN")
    struk.append("         LAYANAN LAUNDRY KAMI")
    struk.append("=" * 45)

    return "\n".join(struk)
