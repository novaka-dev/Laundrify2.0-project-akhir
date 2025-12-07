Beress bro, ini versi **simple**, **rapi**, dan **langsung siap tempel** dalam format **Markdown**.

---

# 🚀 Panduan Git Singkat untuk Kolaborasi

Panduan ini dibuat biar kerja bareng lebih rapi dan menghindari konflik saat menggunakan GitHub.

---

## ## 🌿 Nama Branch (Gunakan Prefix Ini)

* **feat/** → fitur baru
  Contoh: `feat/about-page`
* **fix/** → perbaikan bug
  Contoh: `fix/navbar-mobile`
* **docs/** → update dokumentasi
* **style/** → perubahan tampilan (CSS/UI)
* **refactor/** → rapihin kode tanpa ubah fungsi
* **chore/** → update config/dependensi

---

## ## 🆕 Buat & Pindah Branch

### Buat branch + langsung pindah:

```bash
git checkout -b nama-branch
```

### Pindah ke branch lain:

```bash
git checkout nama-branch
```

---

## ## 🚀 Push ke GitHub

### Push pertama kali:

```bash
git push -u origin nama-branch
```

### Push selanjutnya:

```bash
git push
```

---

## ## 🔄 Merge ke Branch Dev/Main

1. Pindah ke `dev`:

   ```bash
   git checkout dev
   git pull origin dev
   ```

2. Merge:

   ```bash
   git merge nama-branch
   ```

3. Push hasil merge:

   ```bash
   git push origin dev
   ```

---

## ## 🧹 Hapus Branch

### Hapus branch lokal:

```bash
git branch -d nama-branch
```

### Hapus branch remote (GitHub):

```bash
git push origin --delete nama-branch
```

---

## ## 📝 Format Commit yang Benar

Gunakan format **Conventional Commits**:

```
type(scope): pesan singkat
```

Contoh:

```bash
git commit -m "feat(contact): tambah form kontak"
git commit -m "fix(ui): perbaiki tombol tidak bisa diklik"
```

---

## ## 🔍 Perintah Penting Lain

Lihat semua branch:

```bash
git branch -a
```

Cek kamu lagi di branch apa:

```bash
git branch --show-current
```

---

Siap untuk dipake, bro. Mau versi **lebih minimal** atau **lebih lengkap** tinggal bilang aja 🔥
