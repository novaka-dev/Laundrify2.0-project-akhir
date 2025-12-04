from manage_data import *

def edit_layanan():
    while True:
        kiloan = data_json(FILE_KILOAN)
        satuan = data_json(FILE_SATUAN)

        print("=== Pilih Jenis Layanan ===")
        print("1. Kiloan")
        print("2. Satuan")
        print("0. Kembali")
        jenis = int(input("Masukan jenis layanan (1/2): "))

        if jenis == 1:
            print("=== DAFTAR LAYANAN KILOAN ===")
            for item in kiloan:
                print(f"{item['kode']}. {item['nama']} - Rp.{item['harga_per_kg']} - {item['est_days']}")

            kode = input("Masukan kode layanan yang mau di ubah🤪🤘 : ")
            layanan = next((x for x in kiloan if x['kode'] == kode), None)

            if not layanan:
                print("Kode tidak ditemukan!")
                return

            print("\n=== EDIT LAYANANAN KILOAN ===")
            nama = input(f"Input Nama Layanan Baru ({layanan['nama']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
            harga = input(f"Input harga Kg Layanan Baru ({layanan['harga_per_kg']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
            estimasi = input(f"Input estimasi Layanan Baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()

            if not nama and not harga and not estimasi:
                print("Tidak ada data yang diubah👍")
                return

            if nama:
                layanan['nama'] = nama
            if harga:
                layanan['harga_per_kg'] = float(harga)
            if estimasi:
                layanan['est_days'] = estimasi

            save_data(FILE_KILOAN, kiloan)
            print("Layanan kiloan berhasil diubah🤘😎🤘")
            break
        
        elif jenis == 2:
            print("=== DAFTAR LAYANAN SATUAN ===")
            for item in satuan:
                print(f"{item['kode']}. {item['nama']} - Rp.{item['harga_per_kg']} - {item['est_days']}")

            kode = input("Masukan kode layanan yang mau di ubah🤪🤘 : ")
            layanan = next((x for x in satuan if x['kode'] == kode), None)

            if not layanan:
                print("Kode tidak ditemukan!")
                return

            print("\n=== EDIT LAYANANAN SATUAN ===")
            nama = input(f"Input Nama Layanan Baru ({layanan['nama']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
            harga = input(f"Input harga Kg Layanan Baru ({layanan['harga_item']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
            estimasi = input(f"Input estimasi Layanan Baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()

            if not nama and not harga and not estimasi:
                print("Tidak ada data yang diubah👍")
                return

            if nama:
                layanan['nama'] = nama
            if harga:
                layanan['harga_item'] = float(harga)
            if estimasi:
                layanan['est_days'] = estimasi

            save_data(FILE_SATUAN, satuan)
            print("Layanan satuan berhasil  diubah🤘😎🤘")
            break
        elif jenis == 0:
            break

        else:
            print("Input salah ulangi!!!😡😡")
