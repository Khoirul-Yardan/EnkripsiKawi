import os
import json
from datetime import datetime

latin_to_kawi_base = {
    'a': 'ꦄ', 'b': 'ꦧ', 'c': 'ꦕ', 'd': 'ꦢ', 'e': 'ꦌ',
    'f': 'ꦥ', 'g': 'ꦒ', 'h': 'ꦲ', 'i': 'ꦆ', 'j': 'ꦗ',
    'k': 'ꦏ', 'l': 'ꦭ', 'm': 'ꦩ', 'n': 'ꦤ', 'o': 'ꦎ',
    'p': 'ꦥ', 'q': 'ꦐ', 'r': 'ꦫ', 's': 'ꦱ', 't': 'ꦠ',
    'u': 'ꦈ', 'v': 'ꦮ', 'w': 'ꦮ', 'x': 'ꦼ', 'y': 'ꦪ', 'z': 'ꦗ'
}

def load_mapping():
    today = datetime.now().strftime('%Y-%m-%d')
    filepath = os.path.join("mapping_archive", f"mapping_key_{today}.json")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"[✗] File mapping untuk hari ini ({today}) tidak ditemukan.")
    
    with open(filepath, "r", encoding="utf-8") as f:
        mapping_data = json.load(f)
    digit_map = mapping_data.get("digit_map", {})
    symbol_map = mapping_data.get("symbol_map", {})
    full_encrypt_map = {**latin_to_kawi_base, **digit_map, **symbol_map}
    full_decrypt_map = {v: k for k, v in full_encrypt_map.items()}
    return full_encrypt_map, full_decrypt_map

def encrypt_text(text, enc_map):
    return ''.join(enc_map.get(char, char) for char in text.lower())

def decrypt_text(text, dec_map):
    result = ""
    i = 0
    while i < len(text):
        if text[i] in ['⎈', '◉']:
            symbol = text[i:i+4]
            if symbol in dec_map:
                result += dec_map[symbol]
                i += 4
                continue
        if text[i] in dec_map:
            result += dec_map[text[i]]
        else:
            result += text[i]
        i += 1
    return result

if __name__ == "__main__":
    try:
        enc_map, dec_map = load_mapping()
        sample = "pesan rahasia 2025?!"
        encrypted = encrypt_text(sample, enc_map)
        decrypted = decrypt_text(encrypted, dec_map)
        print("Plain    :", sample)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)
    except Exception as e:
        print(e)
