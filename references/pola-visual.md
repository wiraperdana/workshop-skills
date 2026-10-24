# Katalog pola visual

Pilih pola menurut **hubungan yang diajarkan**, lalu baru pikirkan gambarnya. Sebuah slide menjelaskan karena bentuk visualnya meniru bentuk gagasannya. Urutan tampil sebagai garis waktu. Perbandingan tampil sebagai dua sisi. Sebab akibat tampil sebagai rantai.

Nama kedua belas pola di katalog ini adalah label deskriptif milik workshop-skills (K-261024-03), disusun untuk skill ini tanpa sitasi. Istilah mapan yang paling dekat dengan pola "Contoh hitungan lengkap" adalah `worked example`, yang cakupannya lebih luas.

Setiap pola di bawah memuat kapan dipakai, susunan bidang 16:9, lapisan gambar dan lapisan native, serta catatan untuk mode [Normal dan Detail](mode-slide.md). Lapisan gambar dibuat dengan GPT Image tanpa teks. Lapisan native berisi judul, label, angka, panah berlabel, dan sitasi.

## Dua pola terkuat dari deck acuan

Kedua pola ini kuat karena konkret. Pakai keduanya sebagai titik awal.

### 1. Skenario berjam

- **Dipakai saat:** mengajarkan proses yang melibatkan manusia dan sistem, misalnya dari peringatan sampai tindakan.
- **Susunan:** judul di kiri atas, adegan pembuka di kanan atas. Di bawahnya lima sampai enam panel berurutan, tiap panel diberi jam (`10.15`, `10.16`). Cabang hasil di bawah, misalnya kasus nyata dan alarm palsu.
- **Gambar:** satu adegan per panel, tokoh sama di semua panel.
- **Native:** jam, nomor langkah, label tindakan, cabang, label `contoh hipotetis`.
- **Normal:** tiga panel besar, satu kalimat per panel. **Detail:** enam panel dengan keterangan dan cabang.
- **Rujukan acuan:** slide 20, `From Alert to Action`.

### 2. Contoh hitungan lengkap

- **Dipakai saat:** angka melawan intuisi, misalnya akurasi tinggi dengan banyak alarm palsu.
- **Susunan:** premis dengan angka bulat di atas, matriks atau tabel di tengah, satu angka kejutan besar di kanan, kesimpulan di bar bawah.
- **Gambar:** latar suasana kecil di sudut. Angka dan tabel seluruhnya native.
- **Native:** semua angka, rumus, dan label `contoh hipotetis` bila angkanya disusun untuk mengajar.
- **Normal:** premis dan satu angka kejutan saja, hitungannya di naskah bicara. **Detail:** matriks dan rumus lengkap.
- **Rujukan acuan:** slide 10, `The Accuracy Paradox`.

## Pola lain

| No | Pola | Dipakai saat | Susunan inti |
|---|---|---|---|
| 3 | Sebelum dan sesudah | Menunjukkan efek sebuah perubahan | Dua adegan sejajar dengan objek sama, satu perbedaan disorot emas |
| 4 | Rantai sebab akibat | Menjelaskan mengapa sesuatu terjadi | Tiga sampai lima simpul berpanah, satu simpul akar disorot |
| 5 | Anatomi sistem | Mengenalkan bagian sebuah sistem | Satu objek besar di tengah, label native menunjuk bagiannya |
| 6 | Perjalanan satu permintaan | Mengajarkan alur kerja agen atau layanan | Satu tokoh bergerak melewati titik-titik, komponen aktif menyala di tiap titik |
| 7 | Kontras benar dan salah | Mengajarkan kebiasaan kerja, misalnya prompt | Dua contoh berdampingan dengan anotasi native di bagian yang membedakan |
| 8 | Spektrum | Membedakan jenis yang saling terkait | Satu sumbu dengan posisi tiap jenis, contoh dekat pekerjaan di setiap posisi |
| 9 | Matriks dua sumbu | Memilih di antara opsi menurut dua kriteria | Kuadran dengan opsi diletakkan sebagai objek, satu kuadran disorot |
| 10 | Satu frame dan rangkaian | Menunjukkan bahwa konteks waktu mengubah makna | Satu gambar terisolasi di kiri, rangkaian sebelum, saat, dan sesudah di kanan |
| 11 | Tangga atau peta jalan | Posisi saat ini dan langkah berikutnya | Anak tangga atau garis waktu, posisi saat ini disorot, tonggak rencana dibedakan dari capaian |
| 12 | Tugas latihan | Memberi instruksi praktik | Satu contoh hasil jadi di kanan, tiga langkah bergambar di kiri, waktu dan keluaran di bar bawah |

Variasikan pola di sepanjang deck. Dua slide berurutan sebaiknya memakai pola berbeda, kecuali keduanya memang satu rangkaian.

## Arah gambar

Gambar yang memukau sekaligus jelas lahir dari objek konkret dunia audiens.

- **Objek dari pekerjaan peserta.** Layar aplikasi yang mereka pakai, formulir, nomor antrean, ruang layanan, papan tulis kelas. Mockup layar digambar tanpa teks, lalu diisi native.
- **Gaya dokumenter.** Cahaya alami, sudut kamera setinggi mata, ruang yang tampak dipakai sungguhan.
- **Tokoh yang konsisten.** Tetapkan dua sampai tiga tokoh untuk running example, lalu deskripsikan mereka sama persis di setiap prompt. Variasikan usia, pakaian, dan peran sesuai audiens.
- **Satu titik fokus.** Satu warna aksen emas menunjuk hal yang harus dilihat pertama.

**Klise yang dihindari:** otak bercahaya, sirkuit di kepala, robot humanoid sebagai lambang AI, ikon hologram mengambang, cahaya cyan di semua permukaan, tangan manusia dan tangan robot bersentuhan, jaringan titik dan garis tanpa makna, wajah yang sama berulang di banyak panel tanpa alasan cerita. Klise ini membuat deck tampak seperti stok gambar AI dan tidak menerangkan apa pun.

## Templat prompt gambar

```text
Ilustrasi 16:9 bergaya foto dokumenter, untuk slide workshop.
Pola: <nama pola dari katalog>.
Hubungan yang harus terlihat: <urutan / perbedaan / sebab akibat yang diajarkan>.
Adegan: <tempat konkret, objek dari pekerjaan audiens, tokoh dan deskripsi tetapnya>.
Susunan: <posisi tiap elemen>. Ruang kosong untuk label di <posisi>.
Palet: navy #061D32 sebagai dasar, teal #2697AF untuk alur, emas #F5B84A untuk satu titik fokus, merah hanya untuk risiko.
Tanpa teks, angka, logo, atau label apa pun di dalam gambar.
Hindari: otak bercahaya, robot humanoid, ikon hologram, cahaya cyan berlebihan.
```

Palet di atas mengikuti deck acuan. Ganti bila pengguna memberi palet lain.

## Audit dengan prinsip multimedia

Prinsip pembelajaran multimedia dari Mayer (2020) dipakai sebagai daftar periksa desain. Rujukan: Mayer, R. E. (2020). *Multimedia Learning* (edisi ke-3). Cambridge University Press. https://doi.org/10.1017/9781316941355. DOI diresolusi dan metadatanya dicocokkan pada 24 Oktober 2026. Nama prinsip di bawah perlu dicocokkan dengan bab bukunya sebelum dikutip di materi peserta.

| Prinsip | Pertanyaan audit |
|---|---|
| Coherence | Adakah gambar, ikon, atau kalimat yang bisa dihapus tanpa mengurangi pemahaman? |
| Signaling | Apakah satu hal yang harus dilihat pertama ditandai jelas? |
| Redundancy | Apakah pembicara akan membacakan teks yang sama dengan yang ada di layar? Pada mode Normal, pindahkan teks itu ke naskah. |
| Spatial contiguity | Apakah label berada dekat objek yang dinamainya, bukan di kotak terpisah? |
| Segmenting | Apakah konsep sukar dipecah menjadi beberapa slide yang bisa diikuti? |
| Pre-training | Apakah istilah kunci sudah dikenalkan sebelum slide yang memakainya? |
