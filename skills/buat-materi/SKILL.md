---
name: buat-materi
description: Buat deck workshop PPTX dari judul, arahan, rundown, dan sumber yang diberikan pengguna. Dua mode, Normal (default, untuk diproyeksikan) dan Detail (padat, untuk dibaca sendiri). Setiap slide isi berupa infografis penjelas, membawa sitasi, dan punya naskah bicara di slide notes.
---

# /buat-materi

Hasil akhirnya adalah deck PPTX 16:9 yang siap dipresentasikan. Setiap slide isi menjelaskan lewat gambar, dan setiap slide isi punya naskah bicara di slide notes.

Baca referensi ini sebelum mulai:

- [bahasa dan pengajaran](../../references/language-and-teaching.md), untuk suara, naskah bicara, dan tanda tulisan mesin
- [mode slide](../../references/mode-slide.md), untuk Normal dan Detail
- [struktur workshop](../../references/workshop-structure.md), untuk anggaran, running example, dan pola segmen
- [pola visual](../../references/pola-visual.md) dan [produksi visual](../../references/visual-production.md)
- [sumber dan sitasi](../../references/sources-and-citations.md)
- [cakupan harness agen](../../references/agent-harness-curriculum.md), bila topiknya agent
- [analisis deck acuan](../../references/FGD_Child_Safety-analysis.md) dan [resep slide acuan](../../references/slide-recipes.md), bila pengguna meminta gaya deck acuan dan kedua berkas itu tersedia lokal

## Mode

Pakai mode **Normal** kecuali pengguna menulis `mode: detail` atau meminta deck untuk dibaca sendiri. Normal berarti paling banyak 45 kata di layar dan penjelasan dibawa naskah bicara. Detail berarti slide padat yang bisa dipahami tanpa pembicara. Sebutkan mode yang dipakai di awal balasan.

## Input

Terima judul, arahan bebas, audiens, nama pembicara, durasi atau rundown, tujuan belajar, mode, dan sumber dalam bentuk path, URL, teks, gambar, rekaman, transkrip, PDF, PPTX, atau Markdown. Pakai semua input yang tersedia. Tanyakan hanya bagian yang menentukan isi atau durasi dan tidak bisa disimpulkan.

Bahan setiap workshop hanya dipakai untuk workshop itu. Nama, angka, kasus, dan gambar dari klien lain tetap di tempatnya.

## Langkah kerja

### 1. Baca sumber

Baca sumber lengkap yang relevan. Susun daftar istilah kanonik beserta lokasi buktinya. Pisahkan capaian, rencana, contoh hipotetis, dan rekomendasi.

### 2. Rancang alur dan anggaran

Tetapkan waktu demonstrasi, praktik, pembahasan, dan diskusi lebih dulu. Lalu hitung anggaran slide dan gambar menurut [struktur workshop](../../references/workshop-structure.md). Pilih satu running example dan susun setiap segmen dengan pola lima langkah: masalah konkret, contoh kerja, nama konsep, cek pemahaman, praktik.

### 3. Tulis storyboard

Untuk setiap slide, tulis satu baris berisi: pesan utama, pola visual dari katalog, unsur yang harus terlihat, teks layar, sumber, status fakta atau simulasi, dan inti naskah bicara. Slide latihan memakai pola tugas latihan: satu contoh hasil jadi, langkah bergambar, waktu, dan keluaran. Bila seri mungkin dipadatkan menjadi satu sesi, tandai jalur inti dan slide pendalaman.

### 4. Buat tiga slide pilot, lalu berhenti

Produksi tiga slide isi dari bagian yang berbeda, lengkap dengan gambar, teks native, sitasi, dan naskah bicara. Render ketiganya. Tunjukkan pratinjau, anggaran slide dan gambar, serta storyboard ringkas kepada pengguna.

**Berhenti di sini dan tunggu persetujuan pengguna.** Produksi penuh baru dimulai setelah pengguna menyetujui arah visual, suara, dan anggarannya. Bila pengguna sudah menyatakan di awal bahwa pilot tidak perlu ditunjukkan, lanjutkan ke langkah 5.

### 5. Produksi penuh

Buat gambar dengan GPT Image untuk badan infografis slide konseptual, memakai templat prompt di [pola visual](../../references/pola-visual.md). Di Codex, pakai tool gambar bawaan sesuai skill `imagegen`. Di Claude Code, periksa koneksi GPT Image lebih dulu. API berbayar atau model gambar lain dipakai hanya dengan izin pengguna. Bila GPT Image tidak tersedia, buat infografis native yang setara fungsinya dan laporkan perbedaannya.

Rakit PPTX 16:9 dari `templates/workshop-template.pptx` di folder skill ini, kecuali pengguna memberi template sendiri. Pilih layout menurut pola visual, mengikuti tabel di [produksi visual](../../references/visual-production.md). Label, angka, rumus, panah berlabel, dan sitasi ditulis sebagai teks native di atas gambar, dekat objek yang dinamainya. Variasikan pola visual sepanjang deck.

### 6. Tulis naskah bicara di slide notes

Setiap slide isi punya naskah bicara di slide notes PPTX, pada kedua mode. Naskah ditulis dalam bahasa lisan dengan empat bagian: pembuka, inti termasuk analogi bila perlu, satu pertanyaan ke audiens, dan transisi ke slide berikutnya. Di bawah naskah, tulis `Sumber:` diikuti rujukan lengkap, URL atau DOI, dan tanggal akses.

Naskah ini yang membawa suara pembicara. Ikuti bagian suara dan tanda tulisan mesin di [panduan bahasa](../../references/language-and-teaching.md). Pada mode Normal, semua penjelasan yang dipangkas dari layar pindah ke sini.

### 7. Pasang sitasi

Tampilkan rujukan singkat yang terbaca pada setiap slide dengan klaim bersumber. Rincian bibliografi masuk slide notes atau slide referensi. Kredit visual dipisah dari sitasi isi. Tandai ilustrasi AI dan contoh hipotetis bila bisa disangka bukti nyata. Sumber `[UNVERIFIED]` tetap di draft kerja dan tidak tampil sebagai sitasi final.

### 8. Audit, lalu serahkan

1. Jalankan gerbang `python3 -I scripts/audit_deck.py <deck.pptx> --mode <normal|detail>` dari folder skill ini. Revisi sampai lolos.
2. Render **setiap slide** di PowerPoint atau renderer PPTX yang setia. Klasifikasikan setiap slide sebagai infografis penjelas atau pengecualian, lalu hitung rasionya terhadap target 90%.
3. Baca ulang teks di dalam gambar dengan pembacaan visual, dan OCR bila tersedia.
4. Jalankan uji lima detik, uji baca keras, dan uji tanda tulisan mesin dari [panduan bahasa](../../references/language-and-teaching.md) pada judul, label, dan naskah.
5. Periksa daftar klise dan audit prinsip multimedia di [pola visual](../../references/pola-visual.md).

Bila renderer PPTX tidak tersedia, katakan dengan jelas, dan tahan sebutan "siap presentasi" sampai ada pemeriksaan visual yang setara.

## Keluaran

Simpan PPTX final di `_output/` scope kerja terdekat. Simpan juga sumber, gambar terpilih, dan prompt gambar agar deck bisa direvisi. Deck acuan tetap utuh. Bila pengguna meminta PDF pendamping, ekspor dari deck final lalu periksa jumlah dan tampilan halamannya.

Laporkan di akhir: mode, jumlah slide, rasio infografis, hasil gerbang audit, slide yang masih menjadi pengecualian beserta alasannya, dan keterbatasan produksi.
