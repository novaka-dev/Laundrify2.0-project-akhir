import os
import json

DATA_DIR = "data_laundry"
MENU_FILE = os.path.join(DATA_DIR, "kiloan.json")

for item in kiloan:
    print(f"{item['id']}")