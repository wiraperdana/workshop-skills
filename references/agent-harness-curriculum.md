# Cakupan pembelajaran harness agen

Baca panduan ini saat workshop membahas agent, Agentic AI, Codex, Claude Code, atau harness engineering. Harness adalah sistem di sekitar model yang menjalankan siklus agen, mengelola state dan konteks, menyalurkan tindakan melalui alat, serta menampilkan hasil untuk diperiksa. Definisi dan pembagian tanggung jawab perlu dicek terhadap dokumentasi produk saat materi dibuat, karena antarmuka serta fitur berubah.

## Tiga lapisan yang perlu dibedakan

1. **Harness inti:** menerima tugas, memanggil model, mengulangi langkah baca atau tindakan, mengelola sesi dan konteks, merutekan alat, mengoordinasikan agen, meminta persetujuan, merekam jejak, menangani kegagalan, dan menentukan kapan pekerjaan selesai.
2. **Lingkungan eksekusi:** tempat perintah berjalan dan artefak dibuat. Periksa sandbox, file, jaringan, dependensi, kredensial, batas sumber daya, serta cara memulihkan lingkungan.
3. **Aplikasi dan institusi:** menentukan antarmuka pengguna, sumber data yang sah, aturan bisnis, peran dan hak akses, tindakan yang perlu otorisasi, sistem pencatatan resmi, serta siapa bertanggung jawab atas keluaran.

Skills adalah paket instruksi dan sumber yang dipanggil saat perlu. MCP adalah cara menghubungkan alat atau sumber data. Memory adalah cara mempertahankan informasi terpilih antar langkah atau sesi. Ketiganya merupakan mekanisme yang dapat dipakai oleh harness, bukan daftar lengkap harness.

## Pertanyaan desain yang harus terlihat dalam materi

- **Tugas dan tujuan:** siapa meminta apa, keluaran seperti apa yang dianggap selesai, dan kapan agen harus berhenti?
- **Model dan anggaran:** model mana untuk tugas mana, berapa batas waktu, biaya, langkah, dan pemanggilan alat?
- **Instruksi dan kebijakan:** aturan tetap apa yang mengikat, dan apa yang hanya masukan pengguna atau dokumen sumber?
- **Konteks dan retrieval:** dokumen apa yang dipilih, kapan dicari, apa yang disimpan dalam konteks, dan bagaimana informasi lama diringkas?
- **State dan memory:** apa yang perlu bertahan selama tugas, antar sesi, dan dalam catatan resmi? Apa masa simpannya?
- **Alat dan koneksi:** tool apa yang tersedia, apa beda tool dengan skill atau MCP, dan bagaimana identitas serta hak aksesnya dibatasi?
- **Eksekusi:** di mana perintah atau kode berjalan, file dan jaringan apa yang bisa dijangkau, serta bagaimana kredensial dijaga?
- **Orkestrasi:** kapan satu agen cukup, kapan subtugas dapat dibagi ke beberapa agen, dan bagaimana hasil digabung serta diperiksa?
- **Persetujuan dan pengawasan:** tindakan mana yang boleh otomatis, mana yang menunggu petugas, dan bagaimana petugas dapat menghentikan proses?
- **Kegagalan dan pemulihan:** apa yang terjadi saat tool gagal, data berubah, permintaan berulang, konteks habis, atau pekerjaan terputus? Bagaimana retry, pembatalan, dan rollback diputuskan?
- **Observabilitas:** apa yang dicatat tentang input, keputusan, panggilan alat, hasil, durasi, dan kegagalan? Siapa dapat melihatnya?
- **Evaluasi:** bagaimana menguji ketepatan isi, pemilihan alat, kepatuhan izin, hasil tugas, dan perubahan mutu dari versi ke versi?
- **Operasi:** bagaimana versi instruksi, skill, alat, dan model dikelola? Siapa menangani biaya, latensi, insiden, dan perubahan?

Untuk audiens awal, ajarkan sebagai perjalanan satu permintaan. Tampilkan satu contoh kerja dengan data sintetis yang diambil dari dunia kerja audiens: petugas meminta analisis pola sebuah layanan, sistem mengambil sumber yang diizinkan, agen menyusun draf temuan, pemeriksaan menilai bukti, lalu petugas menyetujui tindak lanjut. Tunjukkan komponen yang aktif di setiap langkah. Dashboard historis saja belum menyediakan deret waktu untuk prediksi. Jangan memberi agen akses ke data identitas riil dalam latihan.

## Pemetaan ke latihan

Latihan dasar: peserta menggambar satu siklus tugas, menyebut sumber konteks dan alat yang diperlukan, lalu menetapkan keluaran dan titik berhenti. Latihan lanjutan: peserta membatasi hak baca/tulis, menetapkan persetujuan, memilih antara agen tunggal dan multiagen, merancang log, menguji satu kegagalan, serta menilai hasil dengan rubrik. Workbook penuh dibuat setelah materi disetujui bila itu urutan yang diminta pengguna.

## Sumber teknis untuk diperiksa ulang saat produksi

- OpenAI, `https://developers.openai.com/api/docs/guides/agents-api/architecture`: harness, environment, application server.
- OpenAI, `https://developers.openai.com/blog/codex-as-a-platform`: siklus agen, konteks, alat, persetujuan, hasil, dan batas aplikasi.
- OpenAI, `https://developers.openai.com/api/docs/guides/agents-api/tracing`: jejak pemanggilan model, alat, dan subagen.
- Anthropic, `https://code.claude.com/docs/en/how-claude-code-works`: siklus konteks, tindakan, verifikasi, ekstensi, dan izin.
- Anthropic, `https://www.anthropic.com/research/managed-agents`: pemisahan session, harness, dan sandbox.
