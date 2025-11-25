
# 🎯 Student Data Scraper  
**Automated Multi-Account Scraping Tool using Python + Selenium**

Student Data Scraper adalah tool otomatis untuk mengambil data siswa dari halaman berbasis Google Apps Script.  
Program ini dapat:

✓ Login otomatis  
✓ Navigasi iframe berlapis  
✓ Menjalankan fungsi JavaScript  
✓ Mengambil puluhan field data siswa  
✓ Menyimpan tiap data ke file **JSON** sesuai nama siswa  
✓ Mendukung list akun (multi user scraping)

---

## 🚀 Features

- 🔐 **Auto-login** (NIS + Password)
- 🪟 **Auto-navigate nested iframes** (`sandboxFrame` → `userHtmlFrame`)
- ⚙ **Auto-run JavaScript** → `cekData()`
- 📥 **Extract 50+ data fields** (Biodata, Orang Tua, Wali, dll)
- 📁 **Auto-save JSON per siswa**
- 📄 **Input dari file akun.txt**
- 🔁 **Error-handling** → akun gagal tetap lanjut akun berikutnya
- 🖥 **Mini Chrome window** (lebih bagus untuk screen recording)
- 🎨 **Cool ASCII banner** saat program dijalankan

---

## 📂 Struktur File

```

scraper.py        # Main script
akun.txt          # File akun berisi NIS,PW per baris
output/           # Folder output JSON (opsional)
README.md         # Dokumentasi proyek

```

---

## 📄 Format `akun.txt`

Isi file harus seperti ini:

```

23007,20080601
23010,20080411
23015,20080719

```

Setiap baris:

```

NIS,password

````

---

## 🛠 Cara Menjalankan

### 1. Install dependency
```bash
pip install selenium
````

### 2. Download ChromeDriver (jika belum)

Sesuai versi Google Chrome kamu.

Letakkan di folder PATH atau satu folder dengan script.

### 3. Jalankan script

```bash
python scraper.py
```

### 4. Masukkan path file akun

```
Input Path (contoh: C:/Users/kamu/akun.txt)
Path file:
```

---

## 📦 Output

Setiap akun yang berhasil akan menghasilkan file JSON:

```
Budi_Santoso.json
...
```

Formatnya rapi dan siap digunakan.

---

## ⚠ Error Handling

Program **tidak berhenti** jika:

* Login gagal
* Iframe gagal dimuat
* JavaScript gagal dijalankan
* Koneksi lambat / elemen belum muncul

Akan menampilkan error dan lanjut ke akun selanjutnya.

---
```
