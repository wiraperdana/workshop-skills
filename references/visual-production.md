# Produksi visual workshop

Baca [analisis deck acuan](FGD_Child_Safety-analysis.md) jika pengguna meminta gaya `FGD_Child_Safety.pptx`. Berkas analisis itu hanya tersedia lokal di mesin penulis. Bila tidak ada, pakai [pola visual](pola-visual.md). Deck contoh memiliki 28 slide 16:9. Empat slide memakai objek native; 24 slide memakai satu PNG besar. Struktur itu adalah fakta tentang file, bukan bukti alat pembuat gambarnya. Ciri yang harus direproduksi ialah **gagasan terlihat sebagai gambar**: audiens dapat menunjuk hubungan sebab akibat, urutan, perbedaan, arsitektur, atau keputusan langsung pada visual.

## Definisi infografis penjelas

Sebuah slide dihitung sebagai infografis jika unsur visual utama membawa informasi yang diperlukan untuk memahami pesan. Bentuknya dapat berupa diagram alur, garis waktu, perbandingan adegan, peta sebab akibat, anatomi sistem, grafik data, matriks visual, atau ilustrasi situasi yang diberi penanda konseptual. Teks menamai dan menafsirkan visual. Pada gaya deck acuan, targetkan **setidaknya 90% seluruh slide selain daftar referensi** seperti ini, termasuk slide latihan dan transisi yang relevan.

Hal berikut tidak dihitung: foto dekoratif di belakang judul, gambar hanya pada pembuka bagian, empat kartu dengan paragraf, ikon kecil di samping daftar, atau mockup yang tidak menjelaskan alur. Cover boleh bergambar tetapi tidak menutupi kegagalan proporsi slide isi. Hitung rasio dengan daftar slide dan keputusan manual yang dapat diaudit. Bukti otomatis seperti luas gambar membantu menemukan slide mencurigakan, tetapi tidak dapat menilai apakah gambar benar-benar menerangkan pesan.

## Memilih cara membuat slide

- Untuk konsep, proses, skenario, dan perbandingan yang memerlukan adegan, gunakan GPT Image sebagai **badan infografis**. Mintalah komposisi dengan ruang untuk penanda dan hubungan yang jelas. Satu gambar dapat mengisi slide atau bagian besar slide; label native menjadikan maknanya eksplisit. Gunakan tool gambar bawaan yang tersedia. Di Claude Code, periksa ketersediaan GPT Image. Jangan diam-diam berpindah ke API berbayar atau model lain.
- Untuk angka, grafik, matriks, dan sistem yang harus presisi, gunakan bentuk atau chart PowerPoint native. Slide itu tetap harus menjelaskan pola atau hubungan, bukan menumpuk teks dalam kartu.
- GPT Image boleh menghasilkan komposisi infografis penuh. Periksa setiap teks di dalam gambar dengan OCR dan pembacaan visual. Angka, istilah, nama, sitasi, serta panah berlabel yang penting sebaiknya native. Jika gambar salah secara semantik, regenerasi komposisinya. Menutup kesalahan dengan label kecil tidak cukup bila visual masih menyesatkan.
- Gunakan PNG sebagai keluaran alami GPT Image. SVG hanya berarti vektor bila objeknya benar-benar dibuat sebagai vektor; SVG yang membungkus PNG harus diberi keterangan sebagai gambar raster dalam wadah SVG. PDF dapat memuat gambar raster dan teks native.

## Bahasa visual acuan

Gunakan bidang 16:9. Pakai navy sebagai dasar, teal untuk konsep dan alur, emas untuk fokus, merah hanya untuk risiko atau peringatan. Judul besar di bagian atas atau kiri. Buat satu pesan utama per slide. Pilih tata letak sesuai relasi yang diajarkan: pembuka, dua sisi, urutan proses, contoh temporal, perbandingan, peta jalan, atau penutup. Banyak slide acuan mempunyai satu kalimat kesimpulan di bar bawah. Rotasikan komposisi agar bagian berurutan tidak tampak sebagai satu template dengan isi berbeda.

Untuk audiens literasi awal, ikuti [panduan bahasa dan pengajaran](language-and-teaching.md). Batas teks layar mengikuti [mode slide](mode-slide.md). Pada mode Normal, yang menjadi default, isi slide paling banyak 45 kata di luar judul dan sitasi, dan rinciannya pindah ke naskah bicara di slide notes. Pada mode Detail, slide boleh padat seperti deck acuan asalkan tertata sebagai infografis berlapis. Label harus terbaca pada proyektor, jadi teks kecil ditulis native.

Font native yang tercantum di deck adalah `Inter Display` dan `Inter`. Periksa apakah font tersedia sebelum merender. Jika tidak, jelaskan substitusi yang dipakai dan nilai ulang tata letak. Teks yang sudah menjadi piksel pada PNG tidak memberi bukti nama font yang tepat.

## Storyboard dan prompt gambar per slide

Pilih pola dari [katalog pola visual](pola-visual.md) menurut hubungan yang diajarkan. Katalog itu juga memuat arah gambar, daftar klise yang dihindari, templat prompt, dan audit prinsip multimedia.

Sebelum membuat gambar, catat: **pola**, **pesan utama**, **hubungan yang harus dilihat**, **objek atau adegan**, **urutan baca**, **teks yang akan ditambahkan native**, **sumber klaim**, dan **status fakta atau simulasi**. Sketsa kecil atau uraian posisi elemen sudah cukup. Uji dua sampai tiga slide isi yang berbeda lebih dulu. Bila ketiganya masih terbaca sebagai kartu teks dengan ilustrasi tempelan, ubah pendekatan sebelum membuat seluruh deck.

Tulis prompt berdasarkan fungsi slide, bukan kata kunci topik. Sebut rasio 16:9, palet, posisi ruang label, subjek, sudut kamera, suasana, **relasi visual yang harus terlihat**, dan hal yang harus dihindari. Contoh: untuk otorisasi sebelum akses, minta dua adegan berurutan dengan gerbang persetujuan yang jelas sebelum jalur data, bukan hanya gambar petugas dan ikon gembok. Untuk diagram dengan teks native, minta gambar tanpa teks, angka, logo, atau label final. Gunakan prompt tersendiri bagi setiap komposisi substantif dan catat gambar yang dipilih. Hindari pemakaian ulang ilustrasi yang sama pada banyak slide isi. Jangan menyalin gambar, identitas, data, atau konteks klien lain ke workshop baru.

## Pemeriksaan hasil

Jalankan gerbang `python3 -I scripts/audit_deck.py <deck.pptx> --mode <normal|detail>` lebih dulu. Revisi setiap slide bertanda `KISI_KARTU`, `TEKS_`, `TANPA_NASKAH`, atau `GAMBAR_ULANG` sampai skrip lolos. Lalu render setiap slide dengan PowerPoint atau renderer PPTX yang setia, kemudian periksa pada ukuran presentasi. Catat jumlah slide infografis dan pengecualian. Tandai semua slide yang tampil seperti daftar atau kartu teks; revisi sebelum menyerahkan. Periksa apakah visual memberi informasi sebelum teks dibaca, keterbacaan dari jarak proyeksi, keseimbangan ruang, kesalahan huruf, variasi komposisi, dan posisi sitasi. Cocokkan istilah, angka, arah panah, serta urutan proses dengan sumber. Tandai gambar generatif yang dapat disalahartikan sebagai bukti foto. Simpan aset, prompt, versi yang dipilih, dan keputusan audit visual. Pratinjau bentuk buatan skrip dapat membantu diagnosis, tetapi tidak menggantikan pemeriksaan render PPTX final.
