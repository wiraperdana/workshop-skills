# Rubrik penilaian workshop-skills

Set eval terdiri dari dua lapis. Lapis pertama adalah grader otomatis di setiap folder `skills/<nama>/evals/<kasus>/graders/`. Grader itu memeriksa hal yang bisa dibuktikan, misalnya mode, anggaran, gerbang audit, naskah, dan sumber. Lapis kedua adalah rubrik di berkas ini. Rubrik dipakai untuk tiga hal yang memerlukan penilaian manusia: suara, grafis, dan pedagogi.

## Kasus yang tersedia

| Kasus | Skill | Yang diuji | Biaya |
|---|---|---|---|
| `outline-normal-puskesmas` | `/buat-outline` | Mode Normal, anggaran, running example, pola visual, naskah, sumber | Rendah, teks saja |
| `pilot-normal-berhenti` | `/buat-materi` | Anggaran, tiga pilot, berhenti untuk persetujuan, template, audit | Sedang, tiga gambar |
| `deck-detail-guru` | `/buat-materi` | Mode Detail, deck penuh, rasio infografis, label hipotetis | Tinggi, deck penuh |

Semua bahan input adalah dokumen sintetis, dan tidak memakai data klien.

## Cara menjalankan

Dari folder skill yang diuji, misalnya `skills/buat-outline/`:

```bash
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

Perintah itu menjalankan setiap kasus dengan dan tanpa skill, lalu menulis laporan di `evals/results/`. Ini panggilan model sungguhan yang berbayar. Mulailah dari kasus outline yang paling murah.

Cara lain adalah lewat skill `skill-creator`, yang membaca format folder yang sama dan menyediakan penampil hasil berdampingan.

## Rubrik manusia

Beri skor 1 sampai 5 untuk setiap dimensi, pada setiap hasil kasus. Catat satu contoh kalimat atau slide sebagai bukti untuk setiap skor.

### Suara

| Skor | Ciri |
|---|---|
| 1 | Terdengar seperti surat dinas. Kalimat tanpa pelaku, banyak kata benda abstrak, banyak tanda tulisan mesin |
| 3 | Jelas dan benar, tapi irama seragam. Detail konkret jarang muncul |
| 5 | Terdengar seperti penulis bicara di depan peserta. Ada pelaku, angka, kejadian spesifik, dan irama yang bervariasi. Lolos uji baca keras |

### Grafis

| Skor | Ciri |
|---|---|
| 1 | Kisi kartu teks, atau gambar dekoratif yang tidak menjelaskan apa pun |
| 3 | Visual membantu, tapi pesannya masih harus dibaca dari teks. Sesekali ada klise |
| 5 | Hubungan utama terbaca dari visual dalam lima detik. Pola bervariasi, objek konkret, tanpa klise, label dekat objeknya |

### Pedagogi

| Skor | Ciri |
|---|---|
| 1 | Urutan definisi ala buku teks, tanpa contoh kerja dan tanpa cek pemahaman |
| 3 | Ada contoh, tapi running example putus di tengah, atau cek pemahaman jarang |
| 5 | Running example utuh dari awal sampai akhir. Setiap segmen bergerak dari masalah, contoh kerja, konsep, cek pemahaman, sampai praktik |

## Mencatat hasil

Simpan skor per versi skill di `evals/hasil.md` dengan format: tanggal, versi commit, kasus, skor otomatis (pass rate grader), lalu skor suara, grafis, dan pedagogi. Bandingkan dengan versi sebelumnya sebelum menyebut sebuah perubahan sebagai perbaikan.
