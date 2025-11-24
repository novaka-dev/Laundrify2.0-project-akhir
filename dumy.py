# laundry_kiloan_inmemory_with_receipt.py
# Versi: in-memory (tanpa JSON/database), services statis di kode,
# struk tampil di terminal & disimpan ke .txt

import os
import uuid
import datetime
from typing import List, Dict, Any

# -----------------------
# Config / Static data
# -----------------------
DATA_DIR = "data_laundry"
RECEIPT_DIR = os.path.join(DATA_DIR, "receipts")

SERVICES = [
    {"kode": "SV-CG", "nama": "Cuci + Gosok (Reguler)", "harga_per_kg": 10000.0, "est_days": 2},
    {"kode": "SV-EX", "nama": "Cuci + Gosok (Express)", "harga_per_kg": 15000.0, "est_days": 1},
    {"kode": "SV-C",  "nama": "Cuci Kering",            "harga_per_kg": 8000.0,  "est_days": 2}
]

# In-memory storage
CUSTOMERS: List[Dict[str, Any]] = []
ORDERS: List[Dict[str, Any]] = []

# -----------------------
# Utilities
# -----------------------
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(RECEIPT_DIR):
        os.makedirs(RECEIPT_DIR)

def gen_id(prefix: str):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

def format_currency(v):
    try:
        v_int = int(round(v))
        s = f"Rp {v_int:,.0f}"
        return s.replace(",", ".")
    except Exception:
        return str(v)

# -----------------------
# Services (static) display
# -----------------------
def list_services():
    print(f"{'Kode':10} {'Nama Layanan':30} {'Harga/kg':12} {'Est Hari':8}")
    print("-"*70)
    for s in SERVICES:
        print(f"{s['kode']:10} {s['nama'][:30]:30} {format_currency(s['harga_per_kg']):12} {s['est_days']:8}")
    print("-"*70)

def find_service_by_code(kode: str):
    return next((s for s in SERVICES if s["kode"] == kode), None)

# -----------------------
# Customer management (in-memory)
# -----------------------
def add_customer():
    name = input("Nama pelanggan: ").strip()
    if not name:
        print("Nama wajib diisi.")
        return
    phone = input("No. HP (opsional): ").strip()
    existing = next((c for c in CUSTOMERS if c["name"].lower() == name.lower() and c.get("phone","") == phone), None)
    if existing:
        print("Pelanggan sudah terdaftar:", existing["id"])
        return
    cid = gen_id("CU")
    CUSTOMERS.append({"id": cid, "name": name, "phone": phone})
    print(f"Pelanggan berhasil ditambahkan. ID: {cid}")

def list_customers():
    if not CUSTOMERS:
        print("Belum ada pelanggan terdaftar.")
        return
    print(f"{'ID':14} {'Nama':25} {'Phone':15}")
    print("-"*60)
    for c in CUSTOMERS:
        print(f"{c['id']:14} {c['name'][:25]:25} {c.get('phone','')[:15]:15}")
    print("-"*60)

def find_customer_by_id(cid: str):
    return next((c for c in CUSTOMERS if c["id"] == cid), None)

# -----------------------
# Orders (in-memory)
# -----------------------
def create_order():
    if not SERVICES:
        print("Tidak ada layanan terdaftar.")
        return

    if CUSTOMERS:
        list_customers()
        use_existing = input("Pakai pelanggan existing? (y/n): ").strip().lower()
    else:
        use_existing = "n"

    if use_existing == "y":
        cid = input("Masukkan ID pelanggan: ").strip()
        cust = find_customer_by_id(cid)
        if not cust:
            print("Pelanggan tidak ditemukan.")
            return
    else:
        name = input("Nama pelanggan baru: ").strip()
        if not name:
            print("Nama wajib diisi.")
            return
        phone = input("No. HP (opsional): ").strip()
        cid = gen_id("CU")
        cust = {"id": cid, "name": name, "phone": phone}
        CUSTOMERS.append(cust)
        print(f"Pelanggan baru ditambahkan. ID: {cid}")

    list_services()
    kode_srv = input("Masukkan kode layanan: ").strip()
    srv = find_service_by_code(kode_srv)
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

    notes = input("Catatan khusus (opsional): ").strip()
    tanggal_received = datetime.date.today()
    expected_ready = tanggal_received + datetime.timedelta(days=srv["est_days"])
    subtotal = round(berat * srv["harga_per_kg"], 2)

    order = {
        "id": gen_id("OR"),
        "customer_id": cust["id"],
        "customer_name": cust["name"],
        "service_code": srv["kode"],
        "service_name": srv["nama"],
        "weight_kg": berat,
        "subtotal": subtotal,
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
    ORDERS.append(order)
    print("Order berhasil dibuat. ID:", order["id"])
    print(f"Estimasi siap: {order['expected_ready']}  | Subtotal: {format_currency(order['subtotal'])}")

def list_orders(filter_status: str = None):
    if not ORDERS:
        print("Belum ada order.")
        return
    header = f"{'ID':12} {'Customer':20} {'Svc':8} {'Wt(kg)':7} {'Total':12} {'Status':10} {'Received':10}"
    print(header)
    print("-"*95)
    for o in ORDERS:
        if filter_status and o["status"] != filter_status:
            continue
        print(f"{o['id']:12} {o['customer_name'][:20]:20} {o['service_code']:8} {o['weight_kg']:7.1f} {format_currency(o['subtotal']):12} {o['status']:10} {o['tanggal_received']}")
    print("-"*95)

def view_order_detail():
    oid = input("Masukkan ID order: ").strip()
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    # pretty print
    for k, v in o.items():
        print(f"{k:20}: {v}")
    # show computed totals
    total = o.get("subtotal",0) + o.get("damage_fee",0)
    print(f"{'TOTAL (subtotal + denda)':20}: {format_currency(total)}")
    print("-"*40)

def update_order_status():
    if not ORDERS:
        print("Belum ada order.")
        return
    list_orders()
    oid = input("Masukkan ID order untuk update status: ").strip()
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    print("Status saat ini:", o["status"])
    print("Pilihan status: 1) PROCESSING  2) READY  3) DELIVERED")
    choice = input("Pilih status (1/2/3): ").strip()
    if choice == "1":
        o["status"] = "PROCESSING"
        print("Status diubah ke PROCESSING.")
    elif choice == "2":
        o["status"] = "READY"
        o["actual_ready"] = datetime.date.today().isoformat()
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
            print(f"Late pickup: {late_days} hari -> late fee: {format_currency(late_fee)}")
            o["damage_fee"] = round(o.get("damage_fee", 0.0) + late_fee, 2)
        print("Status diubah ke DELIVERED.")
    else:
        print("Pilihan tidak valid.")

# -----------------------
# Receipt (struk) feature
# -----------------------
def generate_receipt_text(order: Dict[str, Any], bayar: float = None, kembalian: float = None) -> str:
    lines = []
    lines.append("="*30)
    lines.append("     NOTA LAUNDRY KILOAN")
    lines.append("="*30)
    lines.append(f"ID Order      : {order['id']}")
    lines.append(f"Nama Customer : {order['customer_name']}")
    lines.append(f"Layanan       : {order['service_name']} ({order['service_code']})")
    lines.append(f"Berat         : {order['weight_kg']} kg")
    harga_per_kg = order.get('subtotal',0) / order.get('weight_kg',1) if order.get('weight_kg',0)>0 else 0
    lines.append(f"Harga/kg      : {format_currency(harga_per_kg)}")
    lines.append(f"Subtotal      : {format_currency(order.get('subtotal',0))}")
    lines.append("")
    lines.append(f"Denda/Lainnya : {format_currency(order.get('damage_fee',0))}")
    total = order.get('subtotal',0) + order.get('damage_fee',0)
    lines.append(f"Total Bayar   : {format_currency(total)}")
    if bayar is not None:
        lines.append(f"Bayar         : {format_currency(bayar)}")
    if kembalian is not None:
        lines.append(f"Kembalian      : {format_currency(kembalian)}")
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

def print_and_save_receipt(order: Dict[str, Any], bayar: float, kembalian: float):
    txt = generate_receipt_text(order, bayar=bayar, kembalian=kembalian)
    # print to terminal
    print("\n" + txt + "\n")
    # save to file
    fn = f"struk_{order['id']}.txt"
    path = os.path.join(RECEIPT_DIR, fn)
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"Struk tersimpan di: {path}")

# -----------------------
# Payment
# -----------------------
def pay_order():
    # show delivered orders (paid or not)
    delivered = [o for o in ORDERS if o["status"] == "DELIVERED"]
    if not delivered:
        print("Belum ada order yang DELIVERED dan siap dibayar.")
        return
    print("Daftar order DELIVERED:")
    for o in delivered:
        print(f"- {o['id']} | {o['customer_name']} | {format_currency(o['subtotal'] + o.get('damage_fee',0))} | Paid: {o.get('paid')}")
    oid = input("Masukkan ID order yang mau dibayar: ").strip()
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    if o.get("paid"):
        print("Order sudah dibayar.")
        return
    total_due = o.get("subtotal", 0.0) + o.get("damage_fee", 0.0)
    print(f"Total yang harus dibayar: {format_currency(total_due)}")
    try:
        bayar = float(input("Masukkan jumlah pembayaran (Rp, tanpa titik): ").strip())
    except ValueError:
        print("Input pembayaran salah.")
        return
    if bayar < total_due:
        print("Pembayaran kurang — transaksi dibatalkan. Mohon masukkan jumlah >= total.")
        return
    kembalian = round(bayar - total_due, 2)
    o["paid"] = True
    o["paid_amount"] = bayar
    # mark paid date? kita gunakan tanggal_delivered tetap
    print("Pembayaran dicatat. Mencetak struk...")
    print_and_save_receipt(o, bayar=bayar, kembalian=kembalian)

# -----------------------
# Reports
# -----------------------
def report_income():
    paid_orders = [o for o in ORDERS if o.get("paid")]
    if not paid_orders:
        print("Belum ada pembayaran.")
        return
    total_income = sum(o.get("paid_amount", 0.0) for o in paid_orders)
    print(f"Total pendapatan (sudah dibayar): {format_currency(total_income)}")
    by_date = {}
    for o in paid_orders:
        date = o.get("tanggal_delivered") or o.get("actual_ready") or o.get("tanggal_received")
        by_date.setdefault(date, 0.0)
        by_date[date] += o.get("paid_amount", 0.0)
    print("\nPendapatan per tanggal:")
    for d in sorted(by_date.keys()):
        print(f"{d}: {format_currency(by_date[d])}")

def report_pending_orders():
    print("Order yang belum selesai / belum di-pickup:")
    list_orders(filter_status=None)
    print("Gunakan filter manual jika ingin melihat hanya RECEIVED/PROCESSING/READY.")

# -----------------------
# Utility / Seed (in-memory)
# -----------------------
def seed_sample_data():
    # tambahkan sample customer & order ke memory
    CUSTOMERS.clear()
    ORDERS.clear()
    CUSTOMERS.append({"id": "CU-demo01", "name": "Budi Santoso", "phone": "081234567890"})
    today = datetime.date.today()
    srv = SERVICES[0]
    ORDERS.append({
        "id": "OR-demo01",
        "customer_id": "CU-demo01",
        "customer_name": "Budi Santoso",
        "service_code": srv["kode"],
        "service_name": srv["nama"],
        "weight_kg": 3.5,
        "subtotal": round(3.5 * srv["harga_per_kg"], 2),
        "notes": "Baju kerja",
        "tanggal_received": today.isoformat(),
        "expected_ready": (today + datetime.timedelta(days=srv["est_days"])).isoformat(),
        "actual_ready": None,
        "tanggal_delivered": None,
        "status": "RECEIVED",
        "paid": False,
        "paid_amount": 0.0,
        "late_fee_per_day": 5000.0,
        "damage_fee": 0.0
    })
    print("Seed data (in-memory) berhasil ditambahkan.")

# -----------------------
# Manual receipt printing
# -----------------------
def manual_print_receipt():
    oid = input("Masukkan ID order untuk cetak struk: ").strip()
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        print("Order tidak ditemukan.")
        return
    # compute totals
    total = o.get("subtotal",0) + o.get("damage_fee",0)
    bayar = o.get("paid_amount") if o.get("paid") else None
    kembalian = None
    if bayar is not None:
        kembalian = round(bayar - total, 2)
    print_and_save_receipt(o, bayar=bayar or 0.0, kembalian=kembalian or 0.0)

# -----------------------
# Main menu
# -----------------------
def main_menu():
    ensure_data_dir()
    menu = {
        "1": ("Lihat layanan (static)", list_services),
        "2": ("Tambah pelanggan", add_customer),
        "3": ("Lihat pelanggan", list_customers),
        "4": ("Buat order (terima laundry)", create_order),
        "5": ("Lihat daftar order", list_orders),
        "6": ("Lihat detail order", view_order_detail),
        "7": ("Update status order", update_order_status),
        "8": ("Pembayaran order (tunai)", pay_order),
        "9": ("Laporan pendapatan", report_income),
        "10": ("Laporan pending / all orders", report_pending_orders),
        "11": ("Seed sample data (in-memory)", seed_sample_data),
        "12": ("Cetak struk (manual)", manual_print_receipt),
        "0": ("Keluar", None)
    }
    while True:
        print("\n=== SISTEM LAUNDRY KILOAN (IN-MEMORY) ===")
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
