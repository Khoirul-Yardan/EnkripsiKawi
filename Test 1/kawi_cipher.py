
# Auto-generated secure cultural cipher (Kawi + Random Symbol)
latin_to_kawi_base = {'a': 'ꦄ', 'b': 'ꦧ', 'c': 'ꦕ', 'd': 'ꦢ', 'e': 'ꦌ', 'f': 'ꦥ', 'g': 'ꦒ', 'h': 'ꦲ', 'i': 'ꦆ', 'j': 'ꦗ', 'k': 'ꦏ', 'l': 'ꦭ', 'm': 'ꦩ', 'n': 'ꦤ', 'o': 'ꦎ', 'p': 'ꦥ', 'q': 'ꦐ', 'r': 'ꦫ', 's': 'ꦱ', 't': 'ꦠ', 'u': 'ꦈ', 'v': 'ꦮ', 'w': 'ꦮ', 'x': 'ꦼ', 'y': 'ꦪ', 'z': 'ꦗ'}
digit_map = {'0': '⎈jOK', '1': '⎈kJM', '2': '⎈COi', '3': '⎈TGK', '4': '⎈M2a', '5': '⎈lJf', '6': '⎈9vF', '7': '⎈tFa', '8': '⎈KNI', '9': '⎈XM5'}
symbol_map = {'!': '◉tAH', '@': '◉G73', '#': '◉Xe3', '$': '◉bhx', '%': '◉Jxg', '^': '◉Oth', '&': '◉ohr', '*': '◉8AY', '(': '◉RHy', ')': '◉dKP', '-': '◉4jn', '_': '◉gY3', '=': '◉suC', '+': '◉4bT', '[': '◉fHj', '{': '◉45K', ']': '◉2q4', '}': '◉rmR', '\\': '◉d7s', '|': '◉2Ke', ';': '◉NYT', ':': '◉jEW', "'": '◉VPy', '"': '◉uZq', ',': '◉FFB', '<': '◉skl', '.': '◉FXi', '>': '◉J1t', '/': '◉EnL', '?': '◉RZy', '`': '◉3Jd', '~': '◉Alu'}
full_encrypt_map = {**latin_to_kawi_base, **digit_map, **symbol_map}
full_decrypt_map = {v: k for k, v in full_encrypt_map.items()}

def encrypt_text(text):
    return ''.join(full_encrypt_map.get(char, char) for char in text.lower())

def decrypt_text(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i] in ['⎈', '◉']:
            symbol = text[i:i+4]
            if symbol in full_decrypt_map:
                result += full_decrypt_map[symbol]
                i += 4
                continue
        if text[i] in full_decrypt_map:
            result += full_decrypt_map[text[i]]
        else:
            result += text[i]
        i += 1
    return result

if __name__ == "__main__":
    sample = "apalah ini?"
    encrypted = encrypt_text(sample)
    decrypted = decrypt_text(encrypted)
    print("Plain    :", sample)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
