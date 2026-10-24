# Bahasa materi workshop

Gunakan panduan ini untuk judul, outline, slide, naskah bicara, latihan, dan skill turunan. Bila bekerja di WiraOS, aturan gaya di `AGENTS.md` root tetap mengikat. Panduan ini menerjemahkan aturan itu menjadi keputusan menulis materi workshop.

Aturan gaya WiraOS sebagian besar membatasi: tanpa em dash, anggaran kalimat, dan bentuk afirmatif. Pembatasan itu menghapus tanda tulisan mesin. Suara yang hidup datang dari bahan positif di bawah ini, jadi kedua bagian wajib dipakai bersama.

## Suara yang terdengar seperti orang bicara

Tulis seperti Wira menjelaskan pekerjaan kepada rekan kerja peserta: hangat, langsung, teliti. Lima bahan berikut membuat kalimat terdengar manusiawi.

1. **Ada pelaku.** Sebut siapa yang berbuat: petugas, warga, guru, AI, Bapak Ibu. Kalimat tanpa pelaku terdengar seperti dokumen kebijakan.
2. **Kata kerja konkret.** Pilih `mengetik`, `menunggu`, `menolak`, `salah kutip`. Hindari kata benda abstrak seperti `optimalisasi` dan `pemanfaatan`.
3. **Angka dan detail kecil.** `40 halaman`, `jam 10.15`, `antrean nomor 37`. Detail kecil membuat pendengar membayangkan situasinya.
4. **Satu kejadian spesifik.** Ceritakan satu kasus, lalu tarik polanya. Urutan ini lebih mudah diikuti daripada pola dulu, contoh belakangan.
5. **Irama yang bervariasi.** Campur kalimat sangat pendek dengan kalimat sedang. Deretan kartu yang semuanya berbentuk "Label + kalimat enam kata" terdengar seperti mesin.

Contoh perbaikan:

| Terdengar seperti mesin | Terdengar seperti orang bicara |
|---|---|
| Keluaran yang lancar belum tentu benar, terbaru, atau berwenang. | AI bisa menjawab dengan yakin, padahal aturannya sudah berganti bulan lalu. |
| Di setiap tahap, AI menyiapkan bantuan. Petugas menjaga keputusan dan jalur koreksi. | AI menyiapkan draf. Bapak Ibu yang memutuskan. |
| Model memilih bagian yang salah. | Kita beri 40 halaman, AI malah mengutip halaman yang salah. |
| Pelatihan dan inferensi model | AI belajar dari contoh, lalu mencoba kasus baru |
| Harness mengelola agentic loop | Siapa mengatur langkah, alat, izin, dan batas kerja agen? |
| Context engineering memilih bahan kerja | Jawaban AI bergantung pada bahan yang kita berikan |

Baca [contoh suara](contoh-suara.md) sebelum menulis naskah bicara. Berkas itu berisi sepuluh pola dari naskah yang pernah dibawakan penulis, urutan prioritas suara, dan cara menerima contoh suara baru dari pengguna lewat input `contoh-suara`. Contoh asli lebih kuat daripada aturan apa pun.

## Tanda tulisan mesin yang dihindari

*Tanda tulisan mesin* adalah label deskriptif milik workshop-skills untuk kata dan pola kalimat yang khas tulisan AI (K-261024-03). Label ini disusun untuk skill ini, tanpa sitasi.

Periksa setiap judul, label, dan naskah terhadap daftar ini. Ganti dengan kalimat yang punya pelaku dan detail.

- Kata pengisi: `memastikan`, `secara efektif`, `secara optimal`, `berperan penting`, `memberdayakan`, `komprehensif`, `holistik`, `lanskap`, `ekosistem` bila tidak merujuk sistem nyata, `di era digital`, `di tengah pesatnya`.
- Pembuka basa-basi: `Pada kesempatan ini`, `Tidak dapat dipungkiri`, dan `Mari kita` yang tidak diikuti tindakan. `Mari kita rangkum` di naskah bicara wajar, karena ia mengajak audiens melakukan sesuatu.
- Pola oposisi: `tidak hanya X, tetapi juga Y`, `bukan sekadar X`, `X bukan Y, melainkan Z`. Nyatakan Y secara langsung.
- Kebiasaan struktur: setiap slide berisi tepat tiga atau empat butir, setiap slide ditutup moral, setiap judul berbentuk `Kata: Penjelasan`.
- Label serba huruf kapital untuk semua kotak. Pakai kapital hanya untuk penekanan yang jarang.

## Tiga lapis bahasa

1. **Judul dan visual:** kata yang langsung dikenali peserta, misalnya `Siapa memeriksa jawaban AI sebelum dikirim?`.
2. **Label pada slide:** istilah kerja dan objek nyata, misalnya `data tiket`, `draf jawaban`, `petugas memeriksa`. Bila istilah baku harus muncul, beri padanan singkat di slide yang sama.
3. **Naskah bicara dan workbook:** definisi penuh, istilah kanonik, batas konsep, rujukan tepat, contoh berhasil dan gagal, serta cara memeriksa hasil.

Istilah teknis memakai bentuk Inggris bila itu yang lazim diucapkan praktisi, misalnya `prompt`, `context`, `harness`. Definisikan pada pemakaian pertama.

## Naskah bicara di catatan pembicara

*Naskah bicara* adalah label deskriptif milik workshop-skills untuk teks lisan per slide yang ditulis di slide notes (K-261024-03). Label ini disusun untuk skill ini, tanpa sitasi.

Suara pembicara hidup di naskah bicara. Setiap slide isi punya naskah dengan empat bagian:

1. **Pembuka.** Satu atau dua kalimat yang mengaitkan slide dengan slide sebelumnya atau dengan running example.
2. **Inti.** Penjelasan lisan, termasuk analogi bila konsepnya sukar. Bangun analogi bertahap: situasi sehari-hari, urutan sebab akibatnya, lalu petakan tiap unsur ke istilah teknis.
3. **Pertanyaan ke audiens.** Satu pertanyaan yang bisa dijawab dalam 30 detik, untuk memeriksa pemahaman.
4. **Transisi.** Satu kalimat yang membuka slide berikutnya.

Tulis naskah dalam bahasa lisan. Kalimat pendek, sapaan langsung, dan jeda yang wajar. Letakkan daftar sumber lengkap di bawah naskah dengan judul `Sumber:`, terpisah dari naskah.

## Istilah sumber dan ketidakpastian

- Susun daftar istilah dari sumber sebelum menulis. Pertahankan nama resmi kerangka, komponen, dan kontrol dari sumber. Terjemahkan fungsinya untuk peserta dengan nama kanonik tetap utuh.
- Bedakan istilah baku, terjemahan penjelas, dan contoh buatan untuk latihan. Istilah, singkatan, atau kerangka baru melewati prosedur persetujuan istilah karangan di `AGENTS.md` WiraOS.
- Pisahkan yang sudah diamati, isi paper, usulan rancangan, dan contoh sintetis. Kalimat pada slide membuat status itu tampak. Usulan AI ditulis sebagai usulan, dengan kata `usulan` atau `rencana`.
- Kutip hanya sumber yang telah dibaca dan mendukung klaim. Sertakan halaman, slide, bagian, atau waktu bila tersedia. Tandai kebutuhan verifikasi secara terbuka.

## Pemeriksaan sebelum menyerahkan

1. **Uji lima detik.** Peserta dengan literasi awal melihat slide selama lima detik, lalu dapat menyebut hal yang terjadi atau keputusan yang harus dibuat.
2. **Uji baca keras.** Bacakan judul dan naskah. Apakah Wira akan mengucapkan kalimat ini apa adanya di depan peserta? Bila terdengar seperti surat dinas, tulis ulang dengan pelaku dan detail.
3. **Uji tanda mesin.** Cari kata dan pola di daftar tanda tulisan mesin.
4. **Uji status.** Klaim tidak terdengar lebih pasti daripada sumbernya, dan usulan tidak terdengar sebagai capaian.

Revisi judul, label, dan naskah bersama-sama agar bahasanya konsisten.
