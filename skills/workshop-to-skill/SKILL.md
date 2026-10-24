---
name: workshop-to-skill
description: Ubah seluruh materi satu workshop, termasuk slide, dokumen, rekaman, transkrip, latihan, dan tanya jawab, menjadi skill yang dapat menjawab atau memandu praktik dengan rujukan ke sumbernya.
---

# /workshop-to-skill

Baca [panduan bahasa dan pengajaran](../../references/language-and-teaching.md) dan [contoh suara](../../references/contoh-suara.md) sebelum menulis keluaran untuk peserta atau fasilitator. Bila pengguna memberi input `contoh-suara`, olah dulu dengan prosedur di berkas contoh suara, lalu pakai sebagai acuan suara utama.

Buat satu skill turunan dari satu workshop atau seri pertemuan. Skill baru harus dapat digunakan ulang tanpa mencampur data antar klien. Baca [panduan sumber](../../references/sources-and-citations.md) dan [struktur workshop](../../references/workshop-structure.md). Gunakan `skill-creator` atau validator skill yang tersedia untuk menulis serta memeriksa paketnya.

## Input dan cakupan

Terima folder workshop, nama skill yang diinginkan bila ada, tujuan pemakaian ulang, serta materi dalam bentuk PDF, PPTX, Markdown, teks, gambar, audio, video, transkrip, workbook, dan URL. Temukan seluruh materi dalam scope yang diberikan. Jika sebagian berkas tidak dapat dibaca, catat secara jelas dan jangan menyebut korpus lengkap. Simpan sumber asli di tempatnya. Jangan menyalin data pribadi, materi terbatas, atau karya pihak ketiga ke lokasi global atau repo publik.

## Bangun skill turunan

1. Inventaris setiap sumber dengan judul, jenis, tanggal bila diketahui, path atau URL, SHA-256 untuk file, dan status akses. Periksa slide atau halaman bergambar secara visual, bukan dari teks hasil ekstraksi saja. Untuk rekaman atau transkrip, petakan topik ke timestamp.
2. Susun peta materi yang mengaitkan topik, definisi, langkah kerja, contoh, batasan, dan pertanyaan peserta dengan halaman, slide, atau timestamp. Bedakan pernyataan pembicara, sumber eksternal yang telah diperiksa, usulan, dan hasil yang benar-benar diamati. Bila dua sumber otoritatif bertentangan, minta keputusan pengguna sebelum menggabungkannya.
3. Tentukan pekerjaan konkret skill baru, misalnya menjelaskan materi kepada peserta, menjawab pertanyaan dengan rujukan, memandu latihan, atau membantu fasilitator. Tulis `SKILL.md` yang ringkas serta referensi topik yang dapat dibuka saat diperlukan. Hindari menyimpan seluruh teks sumber dalam satu prompt.
4. Setiap jawaban skill turunan harus menunjukkan lokasi dukungan yang tepat. Nyatakan ketidakpastian dan pisahkan isi di luar korpus. Verifikasi DOI hidup sebelum memasukkan sitasi akademik baru. Gunakan istilah kanonik dari materi. Jangan menyajikan contoh konseptual sebagai implementasi yang telah diuji.
5. Letakkan skill sumber di folder produk atau workshop yang sesuai. Pasang sebagai symlink ke `~/.agents/skills/` dan `~/.claude/skills/` bila pengguna meminta skill siap pakai lintas agent. Untuk WiraOS, pasang prompt Codex melalui `_system/scripts/codex_prompts.py --scope global --only <nama>`.
6. Validasi frontmatter, semua tautan referensi, rujukan sampel terhadap sumber, dan satu tugas nyata yang menjadi tujuan skill. Laporkan jumlah sumber yang terbaca, cakupan yang belum masuk, nama perintah, lokasi, serta batas pakainya.

Jika materi workshop berasal dari pihak atau klien tertentu, gunakan hanya untuk scope tersebut. Abstraksikan pola menjadi templat kosong dan minta izin yang sesuai sebelum pemakaian lintas klien. Jangan menghapus atau memindahkan berkas sumber.
