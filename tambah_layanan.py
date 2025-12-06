from manage_data import*
import uuid

def tambah_layanan():
    while True:
        orders = data_json(FILE_ORDER)
        kiloan = data_json(FILE_KILOAN)
        satuan = data_json(FILE_SATUAN)

        print("=== Pilih Jenis Layanan ===")
        print("👍1. Kiloan")
        print("✌️2. Satuan")
        print("👌0. Kembali")
        while True:
            jenis = input("Masukan jenis layanan (1/2)🤔🤔: ")

            # tambah menu layanan
            if jenis == "1":
                print("=== Tambah Layanan Kiloan ===")
                while True:
                    nama = input("Input Nama Menu Baru (Contoh: Cuci + Setrika): ")
                    if nama == "":
                        print("Nama menu tidak boleh kosong!")
                        continue
                    else:
                        break
                while True:
                    harga = input("Input harga Menu Baru (Contoh: 12000) : ")
                    if type(harga) == str:
                        try:
                            harga = float(harga)
                            break
                        except ValueError:
                            print("Inputan harus berupa angka!")
                            continue
                    elif harga == "":
                        print("Harga menu tidak boleh kosong!")
                        continue
                    else:
                        break
                while True:
                    estimasi = input("Input Estimasi Menu Baru (3 jam): ")
                    if estimasi.find("jam") == -1:
                        print("Inputan harus sesuai contoh!")
                        continue
                    elif estimasi == "":
                        print("Harga menu tidak boleh kosong!")
                        continue
                    else:
                        break
                kode_baru = str(len(kiloan) + 1)

                layanan = {
                    "kode" : kode_baru,
                    "nama" : nama,
                    "harga_per_kg" : harga,
                    "est_days" : estimasi,
                }

                kiloan.append(layanan)
                save_data(FILE_KILOAN, kiloan)

                print("Menu Layanan Kiloan Berhasil Dibuat🤘😎🤘")
                break

            # tambah menu satuan
            elif jenis == "2":
                print("=== Tambah Layanan Satuan ===")
                # nama = input("Input Nama Menu Baru : ")
                while True:
                    nama = input("Input Nama Menu Baru (Contoh: Cuci Boneka): ")
                    if nama == "":
                        print("Nama menu tidak boleh kosong!")
                        continue
                    else:
                        break
                while True:
                    harga = input("Input harga Menu Baru (Contoh: 12000) : ")
                    if type(harga) == str:
                        try:
                            harga = float(harga)
                            break
                        except ValueError:
                            print("Inputan harus berupa angka!")
                            continue
                    elif harga == "":
                        print("Harga menu tidak boleh kosong!")
                        continue
                    else:
                        break
                # harga = float(input("Input harga Menu Baru : "))
                while True:
                    estimasi = input("Input Estimasi Menu Baru (3 jam): ")
                    if estimasi.find("jam") == -1:
                        print("Inputan harus sesuai contoh!")
                        continue
                    elif estimasi == "":
                        print("Harga menu tidak boleh kosong!")
                        continue
                    else:
                        break
                # estimasi = input("Input Estimasi Menu Baru : ")
                kode_baru = str(len(satuan) + 1)

                layanan = {
                    "kode" : kode_baru,
                    "nama" : nama,
                    "harga_satuan" : harga,
                    "est_days" : estimasi,
                }

                satuan.append(layanan)
                save_data(FILE_SATUAN, satuan)
                print("Menu Layanan Satuan Berhasil Dibuat!🤘😎🤘\n")
                break
            # menu keluar
            elif jenis == "0":
                return  

            else:
                print("Jenis Layanan Tidak Ada!!😡😡")
