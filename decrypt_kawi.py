import os
import json
from datetime import datetime

# Mapping huruf latin ke aksara Jawa Kawi
latin_to_kawi_base = {
    'a': 'ꦄ', 'b': 'ꦧ', 'c': 'ꦕ', 'd': 'ꦢ', 'e': 'ꦌ',
    'f': 'ꦥ', 'g': 'ꦒ', 'h': 'ꦲ', 'i': 'ꦆ', 'j': 'ꦗ',
    'k': 'ꦏ', 'l': 'ꦭ', 'm': 'ꦩ', 'n': 'ꦤ', 'o': 'ꦎ',
    'p': 'ꦥ', 'q': 'ꦐ', 'r': 'ꦫ', 's': 'ꦱ', 't': 'ꦠ',
    'u': 'ꦈ', 'v': 'ꦮ', 'w': 'ꦮ', 'x': 'ꦼ', 'y': 'ꦪ', 'z': 'ꦗ'
}

def load_decrypt_map():
    today = datetime.now().strftime('%Y-%m-%d')
    path = os.path.join("mapping_archive", f"mapping_key_{today}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"[✗] Mapping untuk tanggal {today} tidak ditemukan.")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    enc_map = {**latin_to_kawi_base, **data["digit_map"], **data["symbol_map"]}
    return {v: k for k, v in enc_map.items()}

def decrypt_text(text, dec_map):
    result = ""
    i = 0
    while i < len(text):
        if text[i] in ['⎈', '◉']:
            token = text[i:i+4]
            if token in dec_map:
                result += dec_map[token]
                i += 4
                continue
        if text[i] in dec_map:
            result += dec_map[text[i]]
        else:
            result += text[i]
        i += 1
    return result

if __name__ == "__main__":
    ciphertext = input("Masukkan teks terenkripsi: ")
    dec_map = load_decrypt_map()
    decrypted = decrypt_text(ciphertext, dec_map)
    print("Decrypted:", decrypted)
