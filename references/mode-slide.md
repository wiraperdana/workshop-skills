# Dua mode slide: Normal dan Detail

Setiap deck dan setiap slide dibuat dalam satu dari dua mode. **Normal adalah default.** Mode Detail dipakai hanya bila pengguna memintanya, misalnya dengan menulis `mode: detail`. (Keputusan Wira, K-261024-01, 24 Oktober 2026.)

Bedanya terletak pada siapa yang membawa penjelasan. Pada mode Normal, pembicara yang menjelaskan, dan slide menjadi panggungnya. Pada mode Detail, slide harus bisa dipahami tanpa pembicara, karena ia akan dibaca sendiri.

Analoginya seperti papan petunjuk jalan dan peta lipat. Papan petunjuk dibaca sekilas sambil bergerak, jadi isinya sedikit dan besar. Peta lipat dibaca sambil duduk, jadi ia boleh padat asalkan tertata. Slide Normal adalah papan petunjuk. Slide Detail adalah peta lipat.

| Aspek | Normal (panggung) | Detail (dokumen) |
|---|---|---|
| Dipakai untuk | Diproyeksikan saat sesi berlangsung | Dibaca sendiri, dibagikan, atau dikirim sesudah sesi |
| Teks layar | Paling banyak 45 kata di luar judul dan sumber | Padat boleh, sekitar 220 kata sebagai batas atas |
| Pembawa penjelasan | Naskah bicara di catatan pembicara | Slide itu sendiri |
| Visual | Satu hubungan besar yang terlihat dari jauh | Infografis berlapis: contoh, angka, langkah, dan kesimpulan dalam satu bidang |
| Bar kesimpulan bawah | Opsional, satu kalimat pendek | Dianjurkan |
| Patokan waktu | Sekitar 1,5 sampai 3 menit per slide | Sekitar 3 sampai 4 menit per slide bila dipresentasikan |
| Contoh | Satu skenario besar dengan tiga label | `The Accuracy Paradox` dan `From Alert to Action` di deck acuan |

Patokan waktu Detail diturunkan dari deck acuan, yaitu 28 slide untuk sesi 105 menit. Patokan Normal adalah titik awal kerja. Sesuaikan setelah durasi praktik ditetapkan.

## Aturan yang berlaku di kedua mode

- Sekitar 90% slide selain daftar referensi adalah infografis penjelas menurut [produksi visual](visual-production.md).
- Setiap slide isi punya naskah bicara di catatan pembicara. Pada mode Detail naskahnya boleh lebih pendek, karena slide sudah menjelaskan sendiri.
- Sitasi tampil sebagai teks native yang terbaca.
- Gerbang `scripts/audit_deck.py` dijalankan dengan mode yang sama dengan deck.

## Menjalankan gerbang

```bash
python3 -I scripts/audit_deck.py <deck.pptx> --mode normal
python3 -I scripts/audit_deck.py <deck.pptx> --mode detail
```

Skrip menandai lima hal. Kode-kode di bawah adalah label deskriptif milik workshop-skills (K-261024-03), dan tempat rujukannya di sini.

| Kode | Arti | Menggagalkan gerbang? |
|---|---|---|
| `KISI_KARTU` | Tiga kotak teks atau lebih yang seukuran, tanpa gambar besar | Ya, bila melebihi 10% slide isi |
| `TEKS_n>batas` | Teks layar sebanyak n kata, melebihi batas mode | Ya |
| `TANPA_NASKAH` | Slide notes kosong atau hanya berisi daftar sumber | Ya |
| `GAMBAR_ULANG` | Gambar besar yang sama dipakai di beberapa slide | Tidak, periksa manual |
| `TANPA_VISUAL?` | Slide tanpa gambar dan tanpa kisi kartu, mungkin hanya teks | Tidak, periksa manual |

Skrip hanya membaca teks native. Teks yang sudah menjadi piksel di dalam gambar tidak terhitung. Karena itu slide bergambar penuh pada mode Normal tetap diperiksa jumlah katanya lewat pembacaan visual. Tanda dari skrip adalah petunjuk. Putusan akhir apakah visual benar-benar menjelaskan tetap dibuat dari render setiap slide.

## Bila mode dicampur

Satu deck boleh memakai mode Normal untuk sesi dan menyertakan beberapa slide Detail sebagai lampiran rujukan di akhir. Tandai slide lampiran itu di judulnya, lalu audit kedua bagian dengan mode masing-masing.
