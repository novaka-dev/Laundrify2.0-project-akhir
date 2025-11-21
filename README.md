# 👥 Panduan Kolaborasi Proyek (Git + GitHub)

Panduan ini dibuat agar semua kolaborator dapat bekerja secara
**tertata, aman, dan tidak menimpa pekerjaan satu sama lain.**\
Gunakan README ini sebagai pedoman utama saat bekerja di repository ini.

------------------------------------------------------------------------

# 🚀 1. Clone Repository (Hanya Pertama Kali)

``` bash
git clone https://github.com/novaka-dev/Laundrify2.0-project-akhir.git
cd Laundrify2.0-project-akhir
```

------------------------------------------------------------------------

# 🔄 2. Workflow Diagram (Alur Kerja Kolaborator)

              ┌──────────────┐
              │   git pull   │   ← ambil update terbaru
              └──────┬───────┘
                     │
          ┌──────────▼───────────┐
          │   Buat / Masuk Branch │
          └──────────┬───────────┘
                     │
              ┌──────▼───────┐
              │     Coding    │
              └──────┬───────┘
                     │
             ┌───────▼────────┐
             │  git add .      │
             │  git commit -m  │
             └───────┬────────┘
                     │
             ┌───────▼────────┐
             │   git push      │
             └───────┬────────┘
                     │
             ┌───────▼──────────────┐
             │  Pull Request (PR)    │ ← merge ke main
             └──────────────────────┘

------------------------------------------------------------------------

# 🌿 3. Cara Kerja Menggunakan Branch (Sangat Direkomendasikan)

Agar kode aman dan tidak bentrok, setiap kolaborator **WAJIB bekerja di
branch masing-masing.**

## ✔️ Buat branch baru (pertama kali)

``` bash
git checkout -b fitur-transaksi
```

## ✔️ Pindah ke branch yang sudah ada

``` bash
git checkout fitur-transaksi
```

## ✔️ Cek branch yang aktif

``` bash
git branch
```

------------------------------------------------------------------------

# 🔄 4. WAJIB: git pull Sebelum Mulai Kerja

Selalu lakukan ini supaya branch kalian up-to-date:

``` bash
git pull origin main
```

------------------------------------------------------------------------

# ✏️ 5. Add → Commit → Push (Langkah Kerja Harian)

## ✔️ Add file yang berubah

``` bash
git add .
```

## ✔️ Commit perubahan

``` bash
git commit -m "deskripsi perubahan yang jelas"
```

## ✔️ Push ke branch masing-masing

``` bash
git push origin nama-branch-kamu
```

------------------------------------------------------------------------

# 🔃 6. Buat Pull Request (PR) untuk Merge ke Main

Setelah push:

1.  Buka repo di GitHub\
2.  Klik **Compare & Pull Request**\
3.  Isi deskripsi PR\
4.  Klik **Create Pull Request**

------------------------------------------------------------------------

# ⚠️ 7. Aturan Penting Kolaborasi

-   Jangan coding tanpa git pull dulu\
-   Jangan push langsung ke main\
-   Semua perubahan harus lewat branch → PR\
-   Commit harus jelas & deskriptif\
-   Jangan ubah file orang tanpa izin

------------------------------------------------------------------------

# 🎉 8. Selesai!

Selamat bekerja tim!
