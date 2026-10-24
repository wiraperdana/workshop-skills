---
name: buat-slide
description: Buat satu slide workshop dari pesan, sumber, atau bagian outline, dalam mode Normal (default) atau Detail. Pilih pola visual yang cocok dan hasilkan PNG, SVG, PDF, atau PPTX sesuai pilihan pengguna, lengkap dengan naskah bicara.
---

# /buat-slide

Buat tepat satu slide yang menjelaskan lewat gambar. Baca [bahasa dan pengajaran](../../references/language-and-teaching.md), [mode slide](../../references/mode-slide.md), [pola visual](../../references/pola-visual.md), [produksi visual](../../references/visual-production.md), dan [sumber dan sitasi](../../references/sources-and-citations.md). Bila pengguna meminta gaya deck acuan, baca juga [analisis deck acuan](../../references/FGD_Child_Safety-analysis.md) dan [resep slide acuan](../../references/slide-recipes.md).

## Mode

Pakai mode **Normal** kecuali pengguna menulis `mode: detail`. Normal berarti paling banyak 45 kata di layar. Detail berarti slide padat yang bisa dibaca tanpa pembicara.

## Langkah

1. Ambil pesan utama, audiens, sumber, rasio, mode, gaya, dan format yang sudah disebut pengguna.
2. Pilih pola dari katalog menurut hubungan yang diajarkan. Bila dua pola sama-sama masuk akal dan hasilnya akan berbeda secara material, tawarkan pilihan sebagai satu keputusan ber-ID `K-YYMMDD-NN` sesuai aturan workspace, dengan rekomendasi. Bila pengguna sudah memilih, langsung kerjakan.
3. Buat badan infografis dengan GPT Image memakai templat prompt di katalog, tanpa teks di dalam gambar. Untuk angka dan diagram presisi, bentuk native boleh menjadi visual utama. Di Claude Code, periksa dulu apakah GPT Image terhubung. Bila belum, pakai diagram native atau gambar dengan izin pakai yang jelas.
4. Tambahkan judul, label, angka, dan sitasi sebagai teks native, dekat objek yang dinamainya. Judul dan label bisa dipahami sebelum istilah teknisnya dijelaskan. Bila istilah baku perlu muncul, beri padanan singkat di slide yang sama.
5. Tulis naskah bicara dengan empat bagian: pembuka, inti, satu pertanyaan ke audiens, dan transisi. Untuk PPTX, letakkan di slide notes. Untuk PNG, SVG, atau PDF, tampilkan di respons dan simpan sebagai berkas `.md` pendamping bila pengguna meminta berkas.
6. Untuk PPTX, jalankan `python3 -I scripts/audit_deck.py <slide.pptx> --mode <normal|detail>` dari folder skill ini. Lalu render pada ukuran presentasi dan periksa keterbacaan, ejaan, klise visual, serta uji lima detik dan uji baca keras.

## Format

PNG memerlukan teks yang sudah tepat pada hasil akhir. PPTX dan PDF memakai teks native bila memungkinkan. PPTX dirakit dari `templates/workshop-template.pptx` di folder skill ini, dengan layout yang dipilih menurut tabel di [produksi visual](../../references/visual-production.md). SVG dari gambar GPT Image tetap berisi raster di dalam wadah SVG, dan hal itu disebutkan dengan jelas.

Kredit visual dan label contoh hipotetis ditulis terpisah dari sitasi isi. Tampilkan pratinjau di respons bila tersedia. Simpan berkas final di `_output/` scope terdekat bila pengguna meminta atau menyetujui keluaran berkas.
