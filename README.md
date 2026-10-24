# workshop-skills

Tujuh skill untuk merancang materi workshop dan mengubah hasilnya menjadi skill yang bisa dipakai ulang. Sumber boleh berupa teks, path file, URL, gambar, transkrip, PDF, PPTX, atau Markdown. Setiap keluaran yang memuat klaim menelusurkan isinya ke sumber yang benar-benar diperiksa.

Tiga hal yang dijaga di semua skill:

1. **Suara manusia.** Kalimat punya pelaku, kata kerja konkret, dan detail kecil. Setiap slide isi punya naskah bicara di slide notes.
2. **Grafis yang menjelaskan.** Sekitar 90% slide isi berupa infografis penjelas, dipilih dari katalog pola visual menurut hubungan yang diajarkan.
3. **Pedagogi.** Satu running example sepanjang sesi, dan setiap segmen bergerak dari masalah konkret ke contoh kerja, konsep, cek pemahaman, lalu praktik.

## Perintah

| Perintah | Hasil |
|---|---|
| `/buat-alternatif-judul` | Lima pilihan judul workshop beserta alasan dan rekomendasi |
| `/buat-outline-judul` | Judul dan fungsi seluruh slide, langsung di respons |
| `/buat-outline` | Judul, pesan utama, pola visual, inti naskah, waktu, dan sumber per slide |
| `/buat-materi` | Deck PowerPoint 16:9 siap presentasi, dengan naskah bicara di slide notes |
| `/buat-slide` | Satu slide dalam format yang dipilih pengguna |
| `/buat-workbook` | Panduan praktik peserta dengan langkah, lembar kerja, dan cara memeriksa hasil |
| `/workshop-to-skill` | Skill bersumber yang bisa dipakai ulang dari materi satu workshop |

## Dua mode slide

| Mode | Dipakai untuk | Teks layar |
|---|---|---|
| **Normal** (default) | Diproyeksikan saat sesi | Paling banyak 45 kata, penjelasan dibawa naskah bicara |
| **Detail** | Dibaca sendiri atau dibagikan | Padat dan berlapis, bisa dipahami tanpa pembicara |

Rincian ada di [mode slide](references/mode-slide.md). Contoh pemanggilan:

```text
/buat-materi
judul: <judul sesi>
audiens: <siapa pesertanya dan literasi awalnya>
durasi: <menit, atau rundown>
materi: <path atau URL sumber>
mode: normal
gaya: <deck acuan, bila ada>
contoh-suara: <transkrip, naskah, atau rekaman pembicara, opsional>
```

`/buat-materi` membuat tiga slide pilot lebih dulu, lalu berhenti menunggu persetujuan sebelum produksi penuh.

Input `contoh-suara` diterima oleh semua skill penulis. Skill mengambil pola suara dari contoh itu, menunjukkannya, lalu memakainya sebagai acuan utama. Setelah selesai, skill menawarkan untuk menyimpan polanya di [contoh suara](references/contoh-suara.md). Tanpa input itu, skill memakai pola yang sudah tersimpan.

## Gerbang audit deck

```bash
python3 -I scripts/audit_deck.py <deck.pptx> --mode normal
```

Skrip ini hanya memakai pustaka standar Python. Ia menandai kisi kartu teks, teks layar yang melebihi batas mode, slide tanpa naskah bicara, dan gambar besar yang dipakai ulang. Kode keluar 1 berarti deck wajib direvisi. Tandanya adalah petunjuk, dan putusan akhir tetap dibuat dari render setiap slide.

## Template PowerPoint

`templates/workshop-template.pptx` berisi delapan layout 16:9: Cover, Pembuka bagian, Visual penuh, Sebelum dan sesudah, Skenario berjam, Detail, Tugas latihan, dan Referensi. Setiap layout punya zona tetap untuk judul, gambar, bar kesimpulan, sumber, dan nomor slide. `workshop-template.potx` berisi template yang sama untuk dipakai langsung di PowerPoint.

Template dibangun ulang dengan `python3 scripts/build_template.py`, yang memerlukan `python-pptx`. Palet, font, dan posisi zona diatur lewat konstanta di skrip itu. Font `Inter Display` dan `Inter` perlu terpasang agar tampilan sesuai rancangan.

## Eval

Tiga kasus uji berbahan sintetis tersedia di `skills/buat-outline/evals/` dan `skills/buat-materi/evals/`, dalam format yang dibaca `claude plugin eval` dan skill `skill-creator`. Suara, grafis, dan pedagogi dinilai dengan [rubrik manusia](evals/RUBRIK.md).

## Referensi

| Berkas | Isi |
|---|---|
| [language-and-teaching.md](references/language-and-teaching.md) | Suara, tanda tulisan mesin, tiga lapis bahasa, naskah bicara |
| [contoh-suara.md](references/contoh-suara.md) | Sepuluh pola suara dari naskah yang pernah dibawakan penulis |
| [mode-slide.md](references/mode-slide.md) | Normal dan Detail |
| [workshop-structure.md](references/workshop-structure.md) | Anggaran slide dan gambar, running example, pola segmen |
| [pola-visual.md](references/pola-visual.md) | Dua belas pola visual, arah gambar, klise, templat prompt, audit multimedia |
| [visual-production.md](references/visual-production.md) | Definisi infografis penjelas, produksi, dan pemeriksaan hasil |
| [sources-and-citations.md](references/sources-and-citations.md) | Pemetaan bukti dan cara menampilkan sumber |
| [agent-harness-curriculum.md](references/agent-harness-curriculum.md) | Cakupan materi untuk workshop tentang agent |
## Deck acuan

Skill ini dapat meniru gaya visual sebuah deck acuan. Deck acuan milik penulis, beserta analisis dan resep per slidenya (`references/FGD_Child_Safety-analysis.md` dan `references/slide-recipes.md`), disimpan lokal dan tidak ikut repo ini karena memuat rincian proyek asal. Tanpa berkas itu, skill tetap berjalan memakai [pola visual](references/pola-visual.md), yang sudah merangkum pola umumnya.

Untuk memakai deck acuan sendiri, letakkan deck di root repo, lalu tulis analisis dengan struktur yang sama: jumlah slide, palet, font, dan fungsi visual tiap slide. Deck acuan dipakai untuk alur dan komposisi visual. Isi materi baru selalu berasal dari sumber yang cocok dengan klaimnya.

## Instalasi

Setiap skill tinggal di `skills/<nama>/SKILL.md`. Folder `references`, `scripts`, dan `templates` di dalam folder skill adalah symlink ke folder bersama di root repo.

Untuk Claude Code, tautkan folder skill ke `~/.claude/skills/`. Untuk Codex, tautkan ke `~/.agents/skills/`. Mulai sesi baru bila daftar perintah belum diperbarui.

```bash
for s in skills/*/; do ln -s "$PWD/$s" ~/.claude/skills/; done
```

Gambar infografis dibuat dengan GPT Image bila tool itu tersedia di sesi. Bila tidak tersedia, skill membuat infografis native yang setara fungsinya dan melaporkan perbedaannya.
