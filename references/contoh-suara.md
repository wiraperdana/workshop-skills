# Contoh suara

Berkas ini berisi pola suara yang diambil dari naskah bicara yang pernah dibawakan penulis. Pakai sebagai acuan nada untuk naskah bicara di slide notes dan untuk judul slide. Aturan umumnya ada di [panduan bahasa](language-and-teaching.md). Contoh di sini memperlihatkan aturan itu dalam praktik.

**Sumber dan statusnya.** Semua kutipan berasal dari satu naskah talk tentang GenAI untuk penelitian, Juli 2026, untuk audiens dosen dari lima program studi. Penulis menetapkan naskah ini sebagai acuan suara utama (K-261024-04). Nama acara dan institusi sudah dihapus.

## Urutan prioritas suara

1. **Contoh suara yang diberikan pengguna pada run ini**, lewat input `contoh-suara`. Lihat bagian [Menerima contoh suara dari pengguna](#menerima-contoh-suara-dari-pengguna).
2. **Pola tambahan yang pernah disimpan** di bagian akhir berkas ini.
3. **Sepuluh pola di bawah.**
4. **Aturan umum** di [panduan bahasa](language-and-teaching.md).

Bila dua lapis bertentangan, lapis dengan nomor lebih kecil yang dipakai. Aturan sumber, sitasi, dan larangan em dash tetap berlaku di semua lapis.

## Sepuluh pola

### 1. Pesan utama disebut di depan

> Jadi begini pesan utama hari ini, saya sampaikan di depan supaya jelas arahnya.

Pendengar tahu arah sebelum detail datang. Ini bentuk piramida dalam bahasa lisan.

### 2. Pengalaman pribadi sebagai bukti

> Saya sudah coba sendiri, minta ChatGPT membuat tabel state of the art (...). Tapi ketika saya klik tautannya satu per satu, sebagian besar rusak.

Klaim tentang risiko AI terasa nyata karena pembicara menunjukkan apa yang ia lakukan dan apa yang ia lihat. Satu kejadian seperti ini lebih meyakinkan daripada tiga kalimat peringatan umum.

### 3. Satu contoh dibawa sepanjang sesi

> Supaya tidak abstrak, saya kasih satu contoh nyata, yang akan saya pakai berulang sepanjang sesi ini.

Contoh penilaian kerusakan bangunan setelah gempa muncul di bagian tahapan penelitian, prompt, dan metode. Ini running example dalam praktik.

### 4. Analogi pendek yang langsung dipetakan

> (...) mirip cara mata terlatih membandingkan dua sketsa untuk mencari beda.

Satu klausa analogi, tepat setelah penjelasan teknis, tanpa paragraf tambahan.

### 5. Istilah teknis disebut, lalu langsung diartikan

> Mencari Celah Penelitian, atau dalam bahasa Inggris disebut research gap, yaitu jarak antara apa yang sudah diketahui dan apa yang belum diketahui di bidang itu.

Pola "istilah, atau ..., yaitu ..." dipakai konsisten untuk setiap istilah baru.

### 6. Contoh diterjemahkan ke bidang setiap kelompok audiens

> Coba saya bayangkan versi untuk Ibu dari PGPAUD. (...) Rumusnya sama persis dengan versi computer vision tadi. Hanya isinya yang berbeda.

Audiens campuran tetap ikut, karena setiap kelompok melihat versinya sendiri.

### 7. Angka yang mengejutkan ditunjuk langsung

> Akurasinya masing-masing sekitar 87 persen, 95 persen, dan 42 persen. Perhatikan angka terakhir itu turun jauh. Itu justru pelajaran penting.

Pembicara menunjuk angka yang harus dilihat, lalu menyebut maknanya.

### 8. Akronim pengingat untuk resep kerja

> Saya beri nama supaya gampang diingat, KORAN LAPANGAN. Lima huruf tebalnya adalah lima unsur prompt yang harus ada.

Akronim baru selalu melewati prosedur persetujuan istilah karangan sebelum dipakai di materi.

### 9. Isyarat panggung di dalam naskah

> [jeda, nada lebih serius]

Naskah memberi tahu pembicara kapan berhenti, kapan memindai wajah audiens, dan kapan mengubah nada. Isyarat ini ditulis dalam kurung siku dan tidak dibacakan.

### 10. Ajakan praktik yang spesifik di penutup

> Bapak Ibu dari PGSD dan PGPAUD, coba susun prompt mencari celah penelitian di bidang pendidikan dasar dan anak usia dini.

Penutup menyebut tindakan konkret untuk setiap kelompok, dengan tenggat "hari ini juga".

## Pantun sebagai ciri khas

Naskah memakai **pantun** di pembukaan, di pergantian bagian, dan di penutup. Empat pantun dalam 30 menit bicara. Penulis menetapkan pantun sebagai ciri khasnya (K-261024-04).

Di naskah bicara, pakai paling banyak satu pantun di setiap titik itu. Isi dua baris terakhirnya mengikat pesan bagian yang baru selesai atau yang akan dimulai. Pantun ditulis di slide notes dengan isyarat `[pantun]`, tidak di layar. Lewati pantun bila pengguna meminta nada formal penuh, atau bila audiens lintas negara dan sesinya berbahasa Inggris.

## Yang tidak ditiru dari naskah ini

Beberapa kalimat naskah masih memakai pola oposisi, misalnya `bukan pengambil keputusan akhir` dan `bukan cuma soal teknis`. Di naskah bicara, pola itu wajar bila memang menegaskan batas. Di judul dan label slide, tulis bentuk afirmatifnya.

## Menerima contoh suara dari pengguna

Setiap skill penulis menerima input opsional `contoh-suara`. Isinya contoh tulisan atau ucapan yang suaranya ingin ditiru. Bentuknya boleh berupa transkrip (`.vtt`, `.srt`, `.txt`), naskah (`.md`, `.docx`), deck dengan slide notes, teks yang ditempel langsung, atau rekaman audio dan video.

Langkahnya:

1. **Baca contohnya.** Rekaman audio atau video ditranskripsi dulu dengan alat transkripsi yang tersedia di sesi, misalnya skill `tulis-catatan`. Bila tidak ada alat transkripsi, minta pengguna mengirim transkripnya.
2. **Ambil hanya suara orang yang dimaksud.** Transkrip rapat atau kelas berisi banyak pembicara. Pakai label pembicara untuk memisahkan kalimat orang yang suaranya ditiru. Bila label tidak ada atau tidak jelas, tanyakan siapa orangnya.
3. **Saring data sensitif.** Bila contoh berasal dari sesi klien, ambil polanya saja. Nama orang, nama lembaga, angka, dan kasus dari contoh itu tidak dibawa ke materi baru.
4. **Susun pola.** Tulis tiga sampai sepuluh pola dengan bentuk yang sama seperti di atas: nama pola, satu kutipan pendek, dan alasan pola itu bekerja. Catat juga kebiasaan yang tidak perlu ditiru, misalnya pengisi seperti "ya, kan" yang berulang.
5. **Tunjukkan pola itu ke pengguna** dalam satu daftar singkat sebelum menulis materi. Lalu pakai pola itu sebagai lapis prioritas pertama di run ini.
6. **Tawarkan penyimpanan.** Setelah materi selesai, tanyakan apakah pola itu perlu disimpan untuk run berikutnya. Bila pengguna setuju, tambahkan di bagian "Pola tambahan yang disimpan" di bawah, lengkap dengan jenis sumber, tanggal, dan pemilik suaranya. Kutipan yang memuat data klien diganti dengan parafrase.

Bila repo skill ini publik, periksa ulang bagian yang baru ditambahkan sebelum commit. Kutipan tetap dibatasi pada kalimat yang aman dibaca orang lain.

## Pola tambahan yang disimpan

Belum ada.
