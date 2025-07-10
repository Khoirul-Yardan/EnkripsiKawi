# 🔐 Jenis-Jenis Serangan pada Sistem Enkripsi Kawi Dinamis

Proyek enkripsi menggunakan aksara Kawi dengan token acak harian adalah sistem yang cukup kuat. Namun, untuk memperkuat keamanan, kita harus memahami berbagai jenis potensi serangan (attack vectors) yang dapat dilakukan oleh penyerang (attacker).

---

## 🧨 1. Known Plaintext Attack (KPA)

**Deskripsi:**  
Penyerang mengetahui sebagian isi plaintext dan juga ciphertext-nya.

**Contoh:**  
- Attacker tahu bahwa `pesan` = `ꦥꦌꦱꦄꦤ`
- Lalu ia lihat ciphertext lengkap: `ꦥꦌꦱꦄꦤ⎈X9A⎈oT3`
- Maka attacker bisa menebak token `⎈X9A` = `' '` dan `⎈oT3` = `'2'`

**Risiko:** Sedang → bisa membuka sebagian mapping

---

## 🧨 2. Chosen Plaintext Attack (CPA)

**Deskripsi:**  
Penyerang dapat mengenkripsi pesan pilihannya melalui sistem.

**Contoh:**  
- Penyerang mengirim teks `"12345?!@"` ke sistem
- Sistem mengembalikan hasil enkripsi token acak seperti `⎈A3d⎈Bf9...`
- Mapping token dapat dipecah

**Risiko:** Tinggi → jika sistem publik tanpa kontrol

---

## 🧨 3. Ciphertext-Only Attack (COA)

**Deskripsi:**  
Penyerang hanya melihat ciphertext, tanpa tahu plaintext.

**Contoh:**  
- Attacker melihat `ꦥꦌꦱꦄꦤ⎈A7q⎈Xr1`
- Lalu mencoba brute-force semua kombinasi token

**Risiko:** Rendah → sistem Kawi cukup kuat terhadap ini

---

## 🧨 4. Frequency Analysis

**Deskripsi:**  
Penyerang menganalisis frekuensi token atau aksara.

**Contoh:**  
- Token `⎈A3d` muncul paling sering → bisa jadi '0' atau ' '

**Risiko:** Rendah → sistem dengan mapping harian aman

---

## 🧨 5. Replay Attack

**Deskripsi:**  
Penyerang mengirim ulang ciphertext lama ke sistem.

**Contoh:**  
- Attacker menangkap ciphertext valid untuk login
- Lalu mengirim ulang untuk akses

**Solusi:** Tambahkan timestamp atau hash unik

**Risiko:** Sedang → jika tidak ada proteksi waktu/session

---

## 🧨 6. Mapping File Exposure

**Deskripsi:**  
Penyerang mendapatkan akses ke file mapping token harian.

**Contoh:**  
- File `mapping_key_2025-07-09.json` bocor
- Semua pesan hari itu bisa didekripsi

**Solusi:** Encrypt mapping, simpan dengan aman

**Risiko:** Tinggi → sangat krusial

---

## 🧨 7. Hybrid AI Attack

**Deskripsi:**  
Penyerang menggunakan model AI/NLP untuk menebak kata dalam Bahasa Indonesia.

**Contoh:**  
- Menggunakan model statistik bahasa + OCR aksara Kawi

**Risiko:** Rendah (untuk saat ini) → butuh resource besar

---

## ✅ Rangkuman Risiko

| Serangan                | Risiko Saat Ini | Keterangan |
|------------------------|------------------|------------|
| Ciphertext-Only        | ❌ Rendah         | Aman karena token acak |
| Known Plaintext        | ⚠️ Sedang         | Bisa bongkar sebagian |
| Chosen Plaintext       | ⚠️ Tinggi         | Harus dicegah sistem terbuka |
| Frequency Analysis     | ❌ Rendah         | Mapping harian menyulitkan |
| Replay Attack          | ⚠️ Sedang         | Perlu proteksi waktu |
| Mapping File Exposure  | ⚠️ Tinggi         | Mapping = kunci utama |
| Hybrid AI              | ❌ Rendah         | Masih skenario riset |

