from manage_data import *
def edit_layanan():
    while True:
        kiloan = data_json(FILE_KILOAN)
        satuan = data_json(FILE_SATUAN)

        print("=== Pilih Jenis Layanan ===")
        print("1. Kiloan")
        print("2. Satuan")
        print("0. Kembali ke Menu Utama")
        jenis = input("Masukan jenis layanan (1/2)🤔🤔: ")

        if jenis == "1":
            if len(kiloan) == 0:
                print("Tidak ada layanan. Tambahkan terlebih dahulu di menu utama\n")
                break
            else:                
                print("=== DAFTAR LAYANAN KILOAN ===")
                print(f"{'Kode':5} {'Nama Layanan':28} {'Harga/Kg':15} {'Estimasi'}")
                print("-" * 70)

                #Ambil Data
                for item in kiloan:
                    harga = int(item['harga_per_kg'])
                    print(
                        f"{item['kode']:5}"
                        f"{item['nama']:30}"
                        f"Rp.{harga:<13}"
                        f"{item['est_days']}"
                    )
                while True:
                    kode = input("Masukan kode layanan yang ingin anda ubah🤔🤔: ")
                    layanan = next((x for x in kiloan if x['kode'] == kode), None)

                    if not layanan:
                        print("Kode tidak ditemukan!😡😡")
                        continue

                    print("\n=== EDIT LAYANANAN KILOAN ===")
                    nama = input(f"Input nama layanan baru ({layanan['nama']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    while True:
                        harga = input(f"Input harga layanan baru (Rp{layanan['harga_per_kg']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                        if harga:
                            try:
                                harga = float(harga)
                                break
                            except ValueError:
                                print("Inputan harus berupa angka!")
                                continue
                        else:
                            break
                    # harga = input(f"Input harga layanan baru ({layanan['harga_per_kg']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    while True:
                        estimasi = input(f"Input estimasi layanan baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                        if estimasi.find("jam") == -1:
                            if estimasi == "":
                                break
                            else:
                                print("Inputan harus sesuai (contoh: 2 jam).")
                                continue
                        else:
                            break
                    # estimasi = input(f"Input estimasi layanan baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()

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
                    print("Layanan kiloan berhasil diubah🤘😎🤘\n")
                    break
        elif jenis == "2":
            if len(satuan) == 0:
                print("Tidak ada layanan. Tambahkan terlebih dahulu di menu utama!\n")
                break
            else:
                print("=== DAFTAR LAYANAN SATUAN ===")
                print(f"{'Kode':5} {'Nama Layanan':28} {'Harga/Jumlah':15} {'Estimasi'}")
                print("-" * 70)

                #Ambil Data
                for item in satuan:
                    harga = int(item['harga_satuan'])
                    print(
                        f"{item['kode']:5}"
                        f"{item['nama']:30}"
                        f"Rp.{harga:<13}"
                        f"{item['est_days']}"
                    )
                while True:
                    kode = input("Masukan kode layanan yang mau di ubah🤔🤔: ")
                    layanan = next((x for x in satuan if x['kode'] == kode), None)

                    if not layanan:
                        print("Kode tidak ditemukan!😡😡")
                        continue

                    print("\n=== EDIT LAYANANAN SATUAN ===")
                    # nama = input(f"Input nama layanan baru ({layanan['nama']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    # harga = input(f"Input harga layanan baru ({layanan['harga_satuan']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    # estimasi = input(f"Input estimasi layanan baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    nama = input(f"Input nama layanan baru ({layanan['nama']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    while True:
                        harga = input(f"Input harga layanan baru (Rp{layanan['harga_satuan']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                        if harga:
                            try:
                                harga = float(harga)
                                break
                            except ValueError:
                                print("Inputan harus berupa angka!")
                                continue
                        else:
                            break
                    # harga = input(f"Input harga layanan baru ({layanan['harga_per_kg']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                    while True:
                        estimasi = input(f"Input estimasi layanan baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()
                        if estimasi.find("jam") == -1:
                            if estimasi == "":
                                break
                            else:
                                print("Inputan harus sesuai (contoh: 2 jam).")
                                continue
                        else:
                            break
                    # estimasi = input(f"Input estimasi layanan baru ({layanan['est_days']}) (ENTER JIKA TIDAK INGIN DIUBAH) : ").strip()

                    if not nama and not harga and not estimasi:
                        print("Tidak ada data yang diubah👍")
                        return

                    if nama:
                        layanan['nama'] = nama
                    if harga:
                        layanan['harga_satuan'] = float(harga)
                    if estimasi:
                        layanan['est_days'] = estimasi

                    save_data(FILE_SATUAN, satuan)
                    print("Layanan satuan berhasil diubah🤘😎🤘\n")
                    break
        elif jenis == "0":
            break

        else:
            print("Kode yang anda masukkan tidak sesuai dengan jenis layanan yang ada!😡😡\n")
