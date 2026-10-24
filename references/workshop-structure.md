# Struktur materi workshop

Sesuaikan jumlah slide dan latihan dengan durasi, audiens, serta tujuan belajar. Rundown yang diberikan pengguna adalah sumber durasi sesi. Deck acuan 28 slide untuk 105 menit hanya contoh komposisi visual, dan jumlahnya bukan target untuk workshop lain.

## Anggaran slide dan gambar

Hitung anggaran sebelum menulis storyboard, lalu tunjukkan ke pengguna.

1. Kurangi durasi dengan waktu praktik, pembahasan, tanya jawab, dan transisi. Sisanya adalah waktu presentasi.
2. Bagi waktu presentasi dengan patokan menit per slide dari [mode slide](mode-slide.md). Hasilnya adalah batas atas jumlah slide.
3. Hitung jumlah gambar GPT Image yang dibutuhkan, termasuk cadangan regenerasi sekitar 30%.
4. Sampaikan anggaran itu bersama storyboard. Bila jumlah gambar terlalu besar untuk dikerjakan, kurangi slide. Sedikit slide yang kaya lebih berguna daripada banyak slide tipis.

Anggaran ini mencegah kegagalan yang paling sering terjadi: deck berisi puluhan slide, gambar tidak cukup, lalu slide sisanya diam-diam diisi kisi kartu teks.

## Running example

Pilih satu running example untuk seluruh sesi atau seri. Running example adalah satu tokoh atau satu kasus konkret yang muncul berulang dari awal sampai akhir, misalnya seorang warga yang gagal menyelesaikan satu layanan. Setiap konsep baru diperkenalkan tepat pada saat kasus itu membutuhkannya.

Running example mengubah urutan materi. Urutan buku teks berjalan dari definisi ke definisi. Urutan running example berjalan dari masalah yang dialami tokoh ke konsep yang menyelesaikannya. Peserta mengingat tokohnya, lalu konsepnya menempel pada cerita itu.

Running example disusun dari sumber workshop yang sedang dikerjakan. Bila datanya sensitif, pakai tokoh dan angka sintetis yang diberi label.

## Pola satu segmen

Setiap segmen konsep mengikuti lima langkah:

1. **Masalah konkret.** Running example menemui kesulitan.
2. **Contoh kerja.** Tunjukkan satu penyelesaian lengkap, langkah demi langkah.
3. **Nama konsepnya.** Baru sekarang istilah teknis diperkenalkan dan didefinisikan.
4. **Cek pemahaman.** Satu pertanyaan ke audiens yang bisa dijawab dalam 30 detik.
5. **Praktik.** Peserta mencoba kasus yang mirip, atau segmen berikutnya menambah satu kerumitan.

Untuk seri beberapa pertemuan, rancang satu tujuan belajar dan satu hasil praktik per pertemuan. Anggarkan waktu untuk penjelasan, demonstrasi, praktik peserta, pembahasan hasil, tanya jawab, dan transisi. Contoh pembagian sesi dua jam ialah 10 menit pembuka, 40 menit konsep serta demonstrasi, 40 menit praktik, 20 menit pembahasan, dan 10 menit penutup. Sesuaikan berdasarkan literasi peserta dan alat yang tersedia. Pertimbangkan jumlah slide sesudah waktu praktik ditetapkan; banyaknya slide sendiri tidak mengukur bobot materi.

Jika topiknya spektrum AI, jelaskan jenis tugas yang diselesaikan oleh AI prediktif atau klasifikasi, AI generatif, agen tunggal, dan sistem multiagen. Jenis ini dapat saling dipadukan, sehingga jangan menampilkannya sebagai tingkat yang otomatis menggantikan tingkat sebelumnya. Untuk audiens pemula, mulai dari masukan, keluaran, batas kesalahan, dan contoh dekat pekerjaan mereka. Baru perkenalkan prompt engineering, context engineering, serta harness engineering. Untuk harness, baca [cakupan harness agen](agent-harness-curriculum.md) dan ajarkan perjalanan satu tugas melalui komponen yang relevan. Jangan membatasi harness pada tools, MCP, skills, dan memory.

Setiap kelompok kemampuan utama yang dijadikan tujuan belajar harus punya demonstrasi atau latihan yang dapat diuji. Tandai judul slide praktik, keluaran peserta, dan prasyarat alat pada tahap outline. Workbook lengkap mengikuti materi yang telah disetujui pengguna. Untuk satu sesi yang mengambil bagian dari seri, pilih jalur inti dengan satu latihan yang selesai dalam waktunya; tandai slide pendalaman yang dapat dilewati.

Jika pengguna memberi tangkapan layar dashboard, pisahkan pembacaan metrik dari perumusan peluang AI. Catat waktu pengambilan, unit, definisi pembilang dan penyebut, serta apakah angka harian atau akumulasi. Satu tangkapan layar menunjukkan keadaan pada satu saat; latihan prediksi membutuhkan deret waktu atau dataset yang sesuai. Pakai data sintetis untuk praktik bila data riil belum tersedia atau belum boleh dipakai. Untuk brainstorming, bedakan peluang deskriptif, prediktif, generatif, dan agentic dari solusi yang telah diterapkan.

## Alur yang dapat diadaptasi

Mulai dari masalah yang dikenali audiens. Jelaskan batas pengetahuan dan status bukti. Perkenalkan sistem, proses, atau kerangka utama. Tunjukkan contoh dan kompromi desain. Hubungkan hasil teknis dengan tindakan manusia. Bahas risiko serta pengaman. Tutup dengan pertanyaan, langkah lanjut, dan ajakan yang relevan. Jika workshop berisi praktik, sisihkan waktu untuk instruksi, pengerjaan, diskusi hasil, dan transisi.

## Hubungan antar keluaran

- `/buat-outline-judul` menetapkan urutan dan tujuan setiap slide tanpa mengarang rincian konten.
- `/buat-alternatif-judul` mengusulkan lima nama workshop sebelum judul resmi dipilih.
- `/buat-outline` menambah pesan utama, isi, contoh, sumber per klaim, ide visual, dan perkiraan waktu.
- `/buat-materi` memakai outline yang disetujui atau menyusunnya dari input yang cukup, lalu membuat PPTX dengan gambar, teks, dan sitasi.
- `/buat-slide` mengambil satu pesan dari outline atau input mandiri dan menghasilkan satu slide dalam format yang dipilih.
- `/buat-workbook` mengubah bagian yang dapat dipraktikkan menjadi instruksi, latihan, lembar kerja, pemeriksaan hasil, dan refleksi.
- `/workshop-to-skill` menyusun materi akhir, transkrip, dan diskusi menjadi skill baru dengan rujukan ke sumbernya.

Jangan menganggap sumber proposal sebagai dukungan bagi seluruh klaim teknis atau etis. Cari dan verifikasi sumber tambahan yang tepat. Bedakan deskripsi sistem yang sudah diuji dari rancangan atau arah riset. Tulis jawaban outline dan workbook dalam respons. Buat file Markdown hanya jika pengguna memintanya atau menyetujui keluaran file. Untuk PPTX, PNG, SVG, atau PDF yang diminta, simpan hasil di `_output/` pada scope kerja terdekat sesuai aturan WiraOS.
