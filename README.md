# 🔐 Enkripsi Kawi Harian — Sistem Cipher Dinamis Seperti Enigma

Proyek ini adalah sistem enkripsi modern berbasis aksara **Jawa Kawi** yang menggabungkan:
- Cipher berbasis simbol harian
- Mapping karakter yang **berubah setiap hari** secara otomatis
- Kemampuan **dekripsi yang konsisten** selama mapping harian tersedia

Mirip seperti **mesin Enigma** pada masa Perang Dunia II, tapi dikombinasikan dengan budaya lokal.

---

## 📁 Struktur Folder

EnkripsiKawi/
├── generate_mapping.py # Membuat mapping simbol acak harian
├── encrypt_kawi.py # Enkripsi berdasarkan mapping hari ini
├── decrypt_kawi.py # Dekripsi berdasarkan mapping hari ini
├── kawi_cipher_dynamic.py # Tes otomatis encrypt + decrypt
└── mapping_archive/
└── mapping_key_YYYY-MM-DD.json # File mapping yang digunakan hari itu

---

## ⚙️ Cara Kerja

1. Huruf a-z diubah ke **aksara Kawi**
2. Angka (0-9) dan simbol (!, ?, dll) diubah ke token acak seperti:
   - ⎈A1b
   - ◉X9z
3. Mapping ini disimpan di folder `mapping_archive/` berdasarkan tanggal (`YYYY-MM-DD`)
4. Hasil enkripsi berubah setiap hari, **meskipun input-nya sama**

---

## 🚀 Cara Menjalankan

### 🔧 Persiapan Awal
Pastikan sudah install Python 3.x dan berada di folder proyek.

### 1. Buat Mapping Harian
```bash
python generate_mapping.py
✅ Mapping disimpan otomatis di mapping_archive/mapping_key_YYYY-MM-DD.json

2. Jalankan Enkripsi

python encrypt_kawi.py
Kamu akan diminta memasukkan teks yang ingin dienkripsi.

3. Jalankan Dekripsi

python decrypt_kawi.py
Masukkan hasil enkripsi tadi, dan akan dikembalikan ke teks asli.

4. Tes Otomatis (Encrypt + Decrypt)

python kawi_cipher_dynamic.py
Menampilkan hasil enkripsi dan dekripsi dari contoh teks secara otomatis.

📌 Contoh
Input:

pesan rahasia 2025?!
Encrypted (hari ini):
ꦥꦌꦱꦄꦤ ꦫꦄꦲꦄꦱꦆꦄ ⎈K2z⎈3Fs⎈K2z⎈Zb9◉WQe
Decrypted:
pesan rahasia 2025?!
```

## 🔐 Keamanan
- Mapping hanya berlaku 1 hari, mirip One-Time Pad ringan

- Mapping hanya diketahui jika kamu punya file mapping_key_YYYY-MM-DD.json

- Aman untuk komunikasi internal yang dibatasi waktu

## 🧠 Inspirasi
Sistem ini terinspirasi dari:

- Mesin Enigma Jerman pada Perang Dunia II

- Aksara Jawa Kuno (Kawi) sebagai bentuk pelestarian budaya

- Kombinasi dengan kriptografi modern berbasis token

## 📅 Penggunaan Jangka Panjang
Simpan file mapping_key_YYYY-MM-DD.json jika ingin mendekripsi pesan dari masa lalu.

Jika mapping hilang, maka dekripsi tidak akan berhasil (demi keamanan).

## 📧 Kontak
Dibuat oleh [Khoirul Yardan] — Mahasiswa D3 Teknik Informatika
Untuk riset, edukasi, dan pengembangan budaya digital

## Kemungkinan Attack
-  [Macam Kemungkinan penyerangan enkripsi](MacamAttack.md)