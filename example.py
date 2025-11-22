"""
laundry_kiloan_with_receipt.py
Sistem Laundry Kiloan (CLI) - Tanpa database (pakai JSON files)

Ditambahkan fitur: CETAK STRUK (nota) - tampil di terminal dan simpan ke file

Files:
- data_laundry/services.json    -> daftar jenis layanan (harga per kg)
- data_laundry/customers.json   -> daftar customer sederhana
- data_laundry/orders.json      -> daftar pesanan / transaksi
- data_laundry/receipts/       -> folder tempat menyimpan file struk (.txt)

Main features:
- Semua fitur sebelumnya + print & save receipt saat pembayaran / manual
"""

import os
import json
import uuid
import datetime
from typing import List, Dict, Any

DATA_DIR = "data_laundry"
SERVICES_FILE = os.path.join(DATA_DIR, "services.json")
CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.json")
ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
RECEIPT_DIR = os.path.join(DATA_DIR, "receipts")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(RECEIPT_DIR):
        os.makedirs(RECEIPT_DIR)
    for path in (SERVICES_FILE, CUSTOMERS_FILE, ORDERS_FILE):
        if not os.path.exists(path):
            with open(path, "w") as f:
             json.dump([], f)


def load_json(path):
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def gen_id(prefix: str):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

# -----------------------
# Service management
# -----------------------
def add_service():
    services = load_json(SERVICES_FILE)
    kode = input("Masukkan kode layanan (enter auto): ").strip()
    if not kode:
        kode = gen_id("SV")
    if any(s["kode"] == kode for s in services):
        print("Kode layanan sudah ada. Batal.")
        return
    nama = input("Nama layanan (contoh: 'Cuci + Gosok Express'): ").strip()
    try:
        harga_per_kg = float(input("Harga per kg (contoh 10000): ").strip())
        duration_days = int(input("Estimasi hari pengerjaan (hari): ").strip())
    except ValueError:
        print("Input angka salah. Batal.")
        return
    layanan = {
        "kode": kode,
        "nama": nama,
        "harga_per_kg": harga_per_kg,
        "est_days": duration_days
    }
    services.append(layanan)
    save_json(SERVICES_FILE, services)
    print(f"Layanan '{nama}' ({kode}) berhasil ditambahkan.")


def list_services():
    services = load_json(SERVICES_FILE)
    if not services:
        print("Belum ada layanan terdaftar.")
        return
    print(f"{'Kode':10} {'Nama Layanan':30} {'Harga/kg':10} {'Est Hari':8}")
    print("-"*65)
    for s in services:
        print(f"{s['kode']:10} {s['nama'][:30]:30} {s['harga_per_kg']:10.0f} {s['est_days']:8}")

# -----------------------
# Customer management
# -----------------------
def add_customer():
    customers = load_json(CUSTOMERS_FILE)
    name = input("Nama pelanggan: ").strip()
    if not name:
        print("Nama wajib diisi.")
        return
    phone = input("No. HP (opsional): ").strip()
    existing = next((c for c in customers if c["name"].lower()==name.lower() and c.get("phone","")==phone), None)
    if existing:
        print("Pelanggan sudah terdaftar:", existing["id"])
        return
    cid = gen_id("CU")
    customers.append({"id": cid, "name": name, "phone": phone})
    save_json(CUSTOMERS_FILE, customers)
    print(f"Pelanggan berhasil ditambahkan. ID: {cid}")


def list_customers():
    customers = load_json(CUSTOMERS_FILE)
    if not customers:
        print("Belum ada pelanggan.")
        return
    print(f"{'ID':10} {'Nama':25} {'Phone':15}")
    print("-"*55)
    for c in customers:
        print(f"{c['id']:10} {c['name'][:25]:25} {c.get('phone','')[:15]:15}")

# -----------------------
# Orders (transactions)
# -----------------------
def create_order():
    services = load_json(SERVICES_FILE)
    customers = load_json(CUSTOMERS_FILE)
    orders = load_json(ORDERS_FILE)

    if not services:
        print("Belum ada layanan. Tambah layanan dulu.")
        return

    list_customers()
    use_existing = input("Pakai pelanggan existing? (y/n): ").strip().lower()
    if use_existing == "y":
        cid = input("Masukkan ID pelanggan: ").strip()
        cust = next((c for c in customers if c["id"] == cid), None)
        if not cust:
            print("Pelanggan tidak ditemukan.")
            return
    else:
        name = input("Nama pelanggan baru: ").strip()
        phone = input("No. HP (opsional): ").strip()
        cid = gen_id("CU")
        cust = {"id": cid, "name": name, "phone": phone}
        customers.append(cust)
        save_json(CUSTOMERS_FILE, customers)
        print(f"Pelanggan baru ditambahkan. ID: {cid}")

    list_services()
    kode_srv = input("Masukkan kode layanan: ").strip()
    srv = next((s for s in services if s["kode"] == kode_srv), None)
    if not srv:
        print("Layanan tidak ditemukan.")
        return

    try:
        berat = float(input("Berat (kg) (boleh desimal, contoh 2.5): ").strip())
        if berat <= 0:
            print("Berat harus > 0.")
            return
    except ValueError:
        print("Input berat salah.")
        return

    notes = input("Catatan khusus (stain, item fragile, dll) (opsional): ").strip()

    tanggal_received = datetime.date.today()
    expected_ready = tanggal_received + datetime.timedelta(days=srv["est_days"])

    subtotal = berat * srv["harga_per_kg"]

    order = {
        "id": gen_id("OR"),
        "customer_id": cust["id"],
        "customer_name": cust["name"],
        "service_code": srv["kode"],
        "service_name": srv["nama"],
        "weight_kg": berat,
        "subtotal": round(subtotal, 2),
        "notes": notes,
        "tanggal_received": tanggal_received.isoformat(),
        "expected_ready": expected_ready.isoformat(),
        "actual_ready": None,
        "tanggal_delivered": None,
        "status": "RECEIVED",
        "paid": False,
        "paid_amount": 0.0,
        "late_fee_per_day": 5000.0,
        "damage_fee": 0.0
    }
    orders.append(order)
    save_json(ORDERS_FILE, orders)
    print("Order berhasil dibuat. ID:", order["id"])
    print(f"Estimasi siap: {order['expected_ready']}  | Total: Rp {order['subtotal']:.0f}")

def list_orders(filter_status: str = None):
    orders = load_json(ORDERS_FILE)
    if not orders:
        print("Belum ada order.")
        return
    header = f"{'ID':12} {'Customer':20} {'Svc':8} {'Wt(kg)':7} {'Total':10} {'Status':10} {'Received':10}"
    print(header)
    print("-"*90)
    for o in orders:
        if filter_status and o["status"] != filter_status:
            continue
        print(f"{o['id']:12} {o['customer_name'][:20]:20} {o['service_code']:8} {o['weight_kg']:7.1f} {o['subtotal']:10.0f} {o['status']:10} {o['tanggal_received']}")
    print("-"*90)

def view_order_detail():
    oid = input("Masukkan ID order: ").strip()
    orders = load_json(ORDERS_FILE)
    o = next((x for x in orders if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    print(json.dumps(o, indent=2))

def update_order_status():
    orders = load_json(ORDERS_FILE)
    if not orders:
        print("Belum ada order.")
        return
    list_orders()
    oid = input("Masukkan ID order untuk update status: ").strip()
    o = next((x for x in orders if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    print("Status saat ini:", o["status"])
    print("Pilihan status: 1) PROCESSING  2) READY  3) DELIVERED")
    choice = input("Pilih status (1/2/3): ").strip()
    if choice == "1":
        o["status"] = "PROCESSING"
        save_json(ORDERS_FILE, orders)
        print("Status diubah ke PROCESSING.")
    elif choice == "2":
        o["status"] = "READY"
        o["actual_ready"] = datetime.date.today().isoformat()
        save_json(ORDERS_FILE, orders)
        print("Status diubah ke READY.")
    elif choice == "3":
        if o["status"] != "READY":
            print("Order harus READY sebelum DELIVERED (cek dulu).")
            return
        today = datetime.date.today()
        expected = datetime.date.fromisoformat(o["expected_ready"])
        late_days = (today - expected).days
        late_days = late_days if late_days > 0 else 0
        late_fee = late_days * o.get("late_fee_per_day", 0.0)
        o["tanggal_delivered"] = today.isoformat()
        o["status"] = "DELIVERED"
        if late_fee > 0:
            print(f"Late pickup: {late_days} hari -> late fee: Rp {late_fee:.0f}")
            o["damage_fee"] = round(o.get("damage_fee", 0.0) + late_fee, 2)
        save_json(ORDERS_FILE, orders)
        print("Status diubah ke DELIVERED.")
    else:
        print("Pilihan tidak valid.")

# -----------------------
# Receipt (struk) feature
# -----------------------

def format_currency(v):
    try:
        return f"Rp {int(round(v)):,.0f}".replace(",", ".")
    except Exception:
        return str(v)


def generate_receipt_text(order: Dict[str, Any]) -> str:
    lines = []
    lines.append("="*30)
    lines.append("     NOTA LAUNDRY KILOAN")
    lines.append("="*30)
    lines.append(f"ID Order      : {order['id']}")
    lines.append(f"Nama Customer : {order['customer_name']}")
    lines.append(f"Layanan       : {order['service_name']} ({order['service_code']})")
    lines.append(f"Berat         : {order['weight_kg']} kg")
    lines.append(f"Harga/kg      : {format_currency(order.get('subtotal',0)/order.get('weight_kg',1)) if order.get('weight_kg',0)>0 else format_currency(order.get('subtotal',0))}")
    lines.append(f"Subtotal      : {format_currency(order.get('subtotal',0))}")
    lines.append("")
    lines.append(f"Denda/Lainnya : {format_currency(order.get('damage_fee',0))}")
    total = order.get('subtotal',0) + order.get('damage_fee',0)
    lines.append(f"Total Bayar   : {format_currency(total)}")
    lines.append("")
    lines.append(f"Tanggal Terima  : {order.get('tanggal_received','-')}")
    lines.append(f"Estimasi Selesai: {order.get('expected_ready','-')}")
    lines.append(f"Tanggal Diambil  : {order.get('tanggal_delivered') or '-'}")
    lines.append("")
    status = order.get('status','-')
    paid = order.get('paid', False)
    lines.append(f"Status: {status} {'& PAID' if paid else ''}")
    lines.append("="*30)
    lines.append("   TERIMA KASIH, SEMOGA HARI ANDA MENYENANGKAN!")
    lines.append("="*30)
    return "\n".join(lines)


def print_and_save_receipt(order: Dict[str, Any], save_file: bool = True):
    txt = generate_receipt_text(order)
    print('\n' + txt + '\n')
    if save_file:
        fn = f"struk_{order['id']}.txt"
        path = os.path.join(RECEIPT_DIR, fn)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(txt)
        print(f"Struk tersimpan di: {path}")

# -----------------------
# Payment and reports
# -----------------------
def pay_order():
    orders = load_json(ORDERS_FILE)
    list_orders(filter_status="DELIVERED")
    oid = input("Masukkan ID order yang mau dibayar: ").strip()
    o = next((x for x in orders if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    if o.get("paid"):
        print("Order sudah dibayar.")
        return
    total_due = o["subtotal"] + o.get("damage_fee", 0.0)
    print(f"Total yang harus dibayar: {format_currency(total_due)}")
    try:
        bayar = float(input("Masukkan jumlah pembayaran (Rp): ").strip())
    except ValueError:
        print("Input salah.")
        return
    if bayar < total_due:
        print("Pembayaran kurang. Bisa terima uang muka? (y/n)")
        ans = input().strip().lower()
        if ans != "y":
            print("Pembayaran dibatalkan.")
            return
    o["paid"] = True
    o["paid_amount"] = bayar
    save_json(ORDERS_FILE, orders)
    print("Pembayaran dicatat. Terima kasih.")
    # print & save receipt otomatis
    print_and_save_receipt(o, save_file=True)


def report_income():
    orders = load_json(ORDERS_FILE)
    if not orders:
        print("Tidak ada data order.")
        return
    total_income = sum(o.get("paid_amount", 0.0) for o in orders if o.get("paid"))
    print(f"Total pendapatan (sudah dibayar): {format_currency(total_income)}")
    by_date = {}
    for o in orders:
        if o.get("paid"):
            date = o.get("tanggal_delivered") or o.get("actual_ready") or o.get("tanggal_received")
            by_date.setdefault(date, 0.0)
            by_date[date] += o.get("paid_amount", 0.0)
    print("\nPendapatan per tanggal (ringkasan):")
    for d in sorted(by_date.keys()):
        print(f"{d}: {format_currency(by_date[d])}")


def report_pending_orders():
    print("Order yang belum selesai / belum di-pickup:")
    list_orders(filter_status=None)
    print("Gunakan filter manual jika ingin melihat hanya RECEIVED/PROCESSING/READY.")

# -----------------------
# Utility / Seed
# -----------------------
def seed_sample_data():
    services = [
        {"kode": "SV-CG", "nama": "Cuci + Gosok (Reguler)", "harga_per_kg": 10000.0, "est_days": 2},
        {"kode": "SV-EX", "nama": "Cuci + Gosok (Express)", "harga_per_kg": 15000.0, "est_days": 1},
        {"kode": "SV-C", "nama": "Cuci Kering", "harga_per_kg": 8000.0, "est_days": 2}
    ]
    customers = [
        {"id": "CU-demo01", "name": "Budi Santoso", "phone": "081234567890"}
    ]
    today = datetime.date.today()
    orders = [
        {
            "id": "OR-demo01",
            "customer_id": "CU-demo01",
            "customer_name": "Budi Santoso",
            "service_code": services[0]["kode"],
            "service_name": services[0]["nama"],
            "weight_kg": 3.5,
            "subtotal": round(3.5 * services[0]["harga_per_kg"],2),
            "notes": "Baju kerja, tas kecil",
            "tanggal_received": today.isoformat(),
            "expected_ready": (today + datetime.timedelta(days=services[0]["est_days"])).isoformat(),
            "actual_ready": None,
            "tanggal_delivered": None,
            "status": "RECEIVED",
            "paid": False,
            "paid_amount": 0.0,
            "late_fee_per_day": 5000.0,
            "damage_fee": 0.0
        }
    ]
    save_json(SERVICES_FILE, services)
    save_json(CUSTOMERS_FILE, customers)
    save_json(ORDERS_FILE, orders)
    print("Seed data berhasil ditambahkan.")

# -----------------------
# Manual receipt printing
# -----------------------
def manual_print_receipt():
    orders = load_json(ORDERS_FILE)
    oid = input("Masukkan ID order untuk cetak struk: ").strip()
    o = next((x for x in orders if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    print_and_save_receipt(o, save_file=True)

# -----------------------
# Main menu
# -----------------------
def main_menu():
    ensure_data_dir()
    menu = {
        "1": ("Tambah layanan (service)", add_service),
        "2": ("Lihat layanan", list_services),
        "3": ("Tambah pelanggan", add_customer),
        "4": ("Lihat pelanggan", list_customers),
        "5": ("Buat order (terima laundry)", create_order),
        "6": ("Lihat daftar order", list_orders),
        "7": ("Lihat detail order", view_order_detail),
        "8": ("Update status order", update_order_status),
        "9": ("Pembayaran order (tunai)", pay_order),
        "10": ("Laporan pendapatan", report_income),
        "11": ("Laporan pending / all orders", report_pending_orders),
        "12": ("Seed sample data (demo)", seed_sample_data),
        "13": ("Cetak struk (manual)", manual_print_receipt),
        "0": ("Keluar", None)
    }
    while True:
        print("\n=== SISTEM LAUNDRY KILOAN (CLI) ===")
        for k, v in menu.items():
            print(f"{k}. {v[0]}")
        choice = input("Pilih menu: ").strip()
        if choice == "0":
            print("Keluar. Sampai jumpa!")
            break
        action = menu.get(choice)
        if action:
            try:
                action[1]()
            except Exception as e:
                print("Error saat menjalankan aksi:", e)
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_menu()
