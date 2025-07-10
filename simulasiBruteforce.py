import random
import string
import itertools

# Konfigurasi Token
token_prefixes = ['⎈', '◉']
token_charset = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
token_length = 3  # Token = prefix + 3 karakter
max_attempts = 100000  # Batas simulasi

# Target token (disimulasikan sebagai token rahasia)
target_token = random.choice(token_prefixes) + ''.join(random.choices(token_charset, k=token_length))
print(f"🎯 Token target (rahasia sistem): {target_token}")

# Mulai simulasi brute-force
print("\n🔓 Mulai brute-force...")
found = False
attempts = 0

for prefix in token_prefixes:
    for combo in itertools.product(token_charset, repeat=token_length):
        guess_token = prefix + ''.join(combo)
        attempts += 1
        if guess_token == target_token:
            found = True
            break
        if attempts >= max_attempts:
            break
    if found or attempts >= max_attempts:
        break

# Hasil
print("\n📊 Hasil Simulasi:")
print(f"- Token yang dicari     : {target_token}")
print(f"- Jumlah percobaan      : {attempts}")
print(f"- Berhasil ditemukan    : {'Ya' if found else 'Tidak (limit tercapai)'}")
print(f"- Total kombinasi token : {len(token_prefixes) * len(token_charset) ** token_length:,}")
print(f"- Estimasi waktu jika 1 juta token/detik: {(len(token_prefixes) * len(token_charset) ** token_length) / 1_000_000:.2f} detik")
