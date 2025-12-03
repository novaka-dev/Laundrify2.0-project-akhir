import os
import json
import uuid
DATA_DIR = "data_laundry"
FILE_KILOAN = os.path.join(DATA_DIR, "kiloan.json")
FILE_SATUAN = os.path.join(DATA_DIR, "satuan.json")
FILE_CUSTOMER = os.path.join(DATA_DIR, "customers.json")
FILE_ORDER = os.path.join(DATA_DIR, "orders1.json")

def data_manage():
    os.makedirs(DATA_DIR, exist_ok=True)

    for path in (FILE_KILOAN, FILE_SATUAN, FILE_ORDER):
        if not os.path.exists(path):
            with open(path , "w") as file:
                json.dump([], file)

def data_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except :
        return[]

def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f , indent=2)

def gen_id(prefix: str):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

def back(a):
    kembali = a
    return kembali
