# 🤖 ConsumerFi Automation Bot

Bot ini dibuat untuk menjalankan otomatisasi **klaim reward**, **klaim harian (daily)**, dan **menjawab pertanyaan thumbs up/down** di platform [ConsumerFi](https://www.consumerfi.ai/app) menggunakan token Bearer dari masing-masing akun.

---

## 🧰 Fitur

- ✅ Klaim reward otomatis (`interval-rewards`)
- 🗓️ Klaim harian otomatis (`daily-rewards`)
- 👍 Jawab thumbs up/down
- 🧑‍🤝‍🧑 Mendukung multi-akun (token banyak)
- ⏱️ Delay antar akun
- 🧾 Log hasil sukses/gagal

---

## 📁 Struktur File

```
.
├── main.py           # Skrip utama
├── tokens.txt           # Token akun-akun
└── README.md            # Dokumentasi ini
```

---

## 📝 Format File `tokens.txt`

Setiap baris harus berisi 1 token lengkap **dengan awalan** `Bearer`, contoh:

```
Bearer eyJhbGciOi...
Bearer eyJ0eXAiOi...
```

> ⚠️ Penting: Wajib ada `Bearer` di awal, jangan dihapus!

---

## 🚀 Cara Menjalankan

1. Install Python (minimal versi 3.8)
2. Install dependensi:
   ```bash
   pip install requests
   ```
3. Jalankan:
   ```bash
   python belajar.py
   ```

---

## 🔁 Alur Bot

Untuk setiap akun:

1. ✅ Kirim klaim **interval reward**
2. 🗓️ Kirim klaim **daily reward**
3. 👍 Jawab semua pertanyaan thumbs up/down
4. ⏱️ Tunggu 3 detik lalu lanjut ke akun berikutnya

---

## ❗ Error Umum

| Masalah | Penyebab | Solusi |
|--------|----------|--------|
| `JWS Protected Header is invalid` | Format token salah / token kadaluarsa | Cek apakah token dimulai dengan `Bearer ` dan masih valid |
| Status 401 / 403 | Token tidak sah / akun diblokir | Ganti token |
| Tidak ada respon sukses | Server down atau endpoint berubah | Cek manual endpoint dan format request |

---

