# **Soal Prioritas 1 (80)**

1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.
## Jawaban:

### Perbedaan Data Terstruktur dan Data Tidak Terstruktur

**Data terstruktur** adalah data yang terorganisir dalam format yang rapi dan konsisten, seperti tabel atau spreadsheet. Data ini mudah dicari, diurutkan, dan dianalisis menggunakan alat dan metode tradisional. Berikut adalah penjelasan lebih rinci tentang data terstruktur:

* **Karakteristik:**
    * Memiliki format yang pasti dan terdefinisi dengan baik
    * Terdiri dari elemen data yang terorganisir dalam baris, kolom, dan tabel
    * Memiliki tipe data yang konsisten (misalnya, string, integer, tanggal)
    * Mudah dipahami dan diinterpretasikan oleh manusia dan mesin
* **Contoh:**
    * Daftar kontak
    * Database pelanggan
    * Data keuangan
    * Transaksi penjualan
    * Data sensus
    * Jadwal penerbangan
* **Penyimpanan:**
    * Disimpan dalam basis data relasional, seperti MySQL, PostgreSQL, atau Oracle
    * Setiap tabel memiliki struktur yang terdefinisi dengan baik, termasuk nama kolom, tipe data, dan kunci utama
* **Pemrosesan:**
    * Dapat dianalisis dengan mudah menggunakan SQL (Structured Query Language)
    * Alat dan aplikasi BI (Business Intelligence) dapat digunakan untuk memvisualisasi dan menganalisis data

**Data tidak terstruktur** adalah data yang tidak memiliki format yang pasti, seperti teks bebas, gambar, video, dan audio. Data ini lebih sulit dicari dan dianalisis dibandingkan data terstruktur. Berikut adalah penjelasan lebih rinci tentang data tidak terstruktur:

* **Karakteristik:**
    * Tidak memiliki format yang pasti dan terdefinisi dengan baik
    * Terdiri dari elemen data yang tidak terorganisir
    * Tipe data tidak konsisten
    * Sulit dipahami dan diinterpretasikan oleh mesin
* **Contoh:**
    * Email
    * Postingan media sosial
    * Dokumen teks
    * Rekaman audio/video
    * Foto
    * Situs web
* **Penyimpanan:**
    * Disimpan dalam sistem penyimpanan file tradisional atau danau data (data lake)
* **Pemrosesan:**
    * Memerlukan teknik khusus, seperti pemrosesan bahasa alami (NLP) dan visi komputer
    * Alat dan aplikasi AI (Artificial Intelligence) dapat digunakan untuk menganalisis data

2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.
## Jawaban:

### Basis Data Relasional

**Basis data relasional** adalah sistem manajemen basis data yang menyimpan data dalam tabel yang saling terkait. Setiap tabel memiliki baris (record) dan kolom (field). Data diakses melalui kunci unik yang disebut primary key. Berikut adalah penjelasan lebih rinci tentang basis data relasional:

* **Struktur:**
    * Terdiri dari tabel-tabel yang saling terkait
    * Setiap tabel memiliki struktur yang terdefinisi dengan baik
    * Setiap baris dalam tabel mewakili satu record data
    * Setiap kolom dalam tabel mewakili satu jenis data (misalnya, nama, alamat, tanggal lahir)
    * Kunci utama (primary key) digunakan untuk mengidentifikasi setiap record secara unik
    * Kunci asing (foreign key) digunakan untuk menghubungkan tabel-tabel yang saling terkait
* **Operasi:**
    * INSERT: Menambahkan record baru ke dalam tabel
    * UPDATE: Memperbarui record yang ada dalam tabel
    * DELETE: Menghapus record dari tabel
    * SELECT: Mengambil data dari tabel
* **Keuntungan:**
    * Mudah digunakan dan dipahami
    * Efisien dalam mengakses data terstruktur
    * Mendukung skalabilitas dan kinerja tinggi
    * Memiliki banyak pilihan alat dan aplikasi

3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.
## Jawaban:

### Normalisasi Basis Data

**Normalisasi** adalah proses untuk mengoptimalkan struktur basis data relasional dengan tujuan:

* Menghilangkan redundansi data
* Meningkatkan integritas data
* Mempermudah akses dan manipulasi data

Proses normalisasi melibatkan beberapa tahap, di antaranya:

* **Normalisasi Bentuk Pertama (1NF):** Menghilangkan duplikasi data dengan mengelompokkan data yang terkait ke dalam tabel-tabel yang terpisah.
* **Normalisasi Bentuk Kedua (2NF):** Menghilangkan dependensi parsial pada primary key.
* **Normalisasi Bentuk Ketiga (3NF):** Menghilangkan dependensi transitif pada primary key.

Normalisasi basis data memiliki beberapa keuntungan, di antaranya:

* Meningkatkan kinerja dan efisiensi basis data
* Mengurangi anomali data
* Mempermudah pemodifikasian dan skalabilitas data

## Referensi

* Data Terstruktur vs. Data Tidak Terstruktur: [https://gleematic.com/indonesia/perbedaan-data-terstruktur-semi-terstruktur-dan-tidak-terstruktur-dalam-rpa-dan-cognitive-automation/](https://gleematic.com/indonesia/perbedaan-data-terstruktur-semi-terstruktur-dan-tidak-terstruktur-dalam-rpa-dan-cognitive-automation/)
* Apa itu Basis Data Relasional?: [https://en.wikipedia.org/wiki/Relational_database](https://en.wikipedia.org/wiki/Relational_database)
* Normalisasi Basis Data 1NF, 2NF, 3NF oleh Medium: [https://medium.com/telematika/normalisasi-1nf-2nf-3nf-1018bdecf028]