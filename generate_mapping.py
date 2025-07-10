import os
import json
import random
import string
from datetime import datetime

def generate_random_map(characters, prefix):
    mapping = {}
    used = set()
    for ch in characters:
        while True:
            token = prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            if token not in used:
                used.add(token)
                break
        mapping[ch] = token
    return mapping

def generate_mapping_file():
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?`~'
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f"mapping_key_{today}.json"
    archive_folder = os.path.join("mapping_archive")
    os.makedirs(archive_folder, exist_ok=True)
    filepath = os.path.join(archive_folder, filename)

    if os.path.exists(filepath):
        print(f"[✓] File mapping hari ini sudah ada: {filepath}")
        return filepath

    mapping = {
        "generated_by": "AUTO_ENIGMA",
        "date": today,
        "digit_map": generate_random_map(digits, '⎈'),
        "symbol_map": generate_random_map(symbols, '◉')
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=4)
    print(f"[+] Mapping baru dibuat: {filepath}")

if __name__ == "__main__":
    generate_mapping_file()
