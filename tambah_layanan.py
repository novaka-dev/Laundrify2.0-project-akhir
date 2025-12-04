from manage_data import*
import uuid

def tambah_layanan():
    while True:
        orders = data_json(FILE_ORDER)
        kiloan = data_json(FILE_KILOAN)
        satuan = data_json(FILE_SATUAN)

        print("=== Pilih Jenis Layanan ===")
        print("1. Kiloan")
        print("2. Satuan")
        print("0. Kembali")
        jenis = int(input("Masukan jenis layanan (1/2): "))

        # tambah menu layanan
        if jenis == 1:
            print("=== Tambah Layanan Kiloan ===")
            nama = input("Input Nama Menu Baru : ")
            harga = float(input("Input harga Menu Baru : "))
            estimasi = input("Input Estimasi Menu Baru : ")
            kode_baru = str(len(kiloan) + 1)

            layanan = {
                "kode" : kode_baru,
                "nama" : nama,
                "harga_per_kg" : harga,
                "est_days" : estimasi,
            }

            kiloan.append(layanan)
            save_data(FILE_KILOAN, kiloan)

            print("Menu Layanan Kiloan Berhasil Dibuat🤪🤪")
            break

        # tambah menu satuan
        elif jenis == 2:
            print("=== Tambah Layanan Satuan ===")
            nama = input("Input Nama Menu Baru : ")
            harga = float(input("Input harga Menu Baru : "))
            estimasi = input("Input Estimasi Menu Baru : ")
            kode_baru = str(len(satuan) + 1)

            layanan = {
                "kode" : kode_baru,
                "nama" : nama,
                "harga_satuan" : harga,
                "est_days" : estimasi,
            }

            satuan.append(layanan)
            save_data(FILE_SATUAN, satuan)

            print("Menu Layanan Satuan Berhasil Dibuat🤪🤪")
            break
        # menu keluar
        elif jenis == 0:
            break

        else:
            print("Nomor Layanan Tidak Ada!!")
