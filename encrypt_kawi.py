import os
import json
from datetime import datetime
from generate_mapping import generate_mapping_file  # pastikan file ini berada di folder yang sama

# Mapping huruf latin ke aksara Jawa Kawi
latin_to_kawi_base = {
    'a': 'ꦄ', 'b': 'ꦧ', 'c': 'ꦕ', 'd': 'ꦢ', 'e': 'ꦌ',
    'f': 'ꦥ', 'g': 'ꦒ', 'h': 'ꦲ', 'i': 'ꦆ', 'j': 'ꦗ',
    'k': 'ꦏ', 'l': 'ꦭ', 'm': 'ꦩ', 'n': 'ꦤ', 'o': 'ꦎ',
    'p': 'ꦥ', 'q': 'ꦐ', 'r': 'ꦫ', 's': 'ꦱ', 't': 'ꦠ',
    'u': 'ꦈ', 'v': 'ꦮ', 'w': 'ꦮ', 'x': 'ꦼ', 'y': 'ꦪ', 'z': 'ꦗ'
}

def load_encrypt_map():
    path = generate_mapping_file()
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {
        **latin_to_kawi_base,
        **data["digit_map"],
        **data["symbol_map"]
    }

def encrypt_text(text, enc_map):
    return ''.join(enc_map.get(c, c) for c in text.lower())

if __name__ == "__main__":
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    enc_map = load_encrypt_map()
    encrypted = encrypt_text(plaintext, enc_map)
    print("Encrypted:", encrypted)
