## Fundamental Data Engineer Part 2

**1. Structured & Unstructured Data**

**Pengenalan:**

Data terbagi menjadi dua kategori utama: Structured Data dan Unstructured Data. Memahami perbedaan keduanya penting dalam memilih teknologi penyimpanan dan analisis data yang tepat.

**Structured Data:**

* Definisi: Data yang terorganisir dalam tabel, baris, dan kolom dengan format yang konsisten.
* Contoh: Database relasional seperti MySQL, spreadsheet seperti Microsoft Excel.
* Penggunaan: Ideal untuk aplikasi yang membutuhkan transaksi cepat dan mudah dianalisis dengan SQL, seperti sistem e-commerce, database pelanggan, dan inventaris.

**Unstructured Data:**

* Definisi: Data yang tidak terstruktur dalam format yang baku dan beragam bentuknya.
* Contoh: Teks, gambar, video, email, log sensor, data media sosial.
* Penggunaan: Ideal untuk aplikasi yang membutuhkan wawasan dan pembelajaran mesin, seperti analisis sentimen, pengenalan gambar, dan prediksi perilaku.

**2. Relational Database vs NoSQL Database**

**Pengenalan:**

Memilih database yang tepat tergantung pada jenis data dan kebutuhan aplikasi. Berikut perbandingan dua jenis database utama:

**Relational Database:**

* Definisi: Database yang terstruktur dalam tabel dengan relasi antar tabel didefinisikan dengan kunci.
* Kelebihan:
    * Mendukung transaksi ACID (Atomicity, Consistency, Isolation, Durability)
    * Mudah dianalisis dengan SQL
    * Skalabilitas horizontal dengan sharding
* Kekurangan:
    * Kurang fleksibel untuk data non-relasional
    * Skalabilitas vertikal terbatas

**NoSQL Database:**

* Definisi: Database yang dirancang untuk data tidak terstruktur dengan berbagai model data (dokumen, key-value, kolom).
* Kelebihan:
    * Fleksibel untuk data non-relasional
    * Skalabilitas horizontal dan vertikal yang tinggi
* Kekurangan:
    * Tidak mendukung transaksi ACID
    * Kompleksitas query

**Contoh:**

* **Relational Database:** MySQL, PostgreSQL, Oracle
* **NoSQL Database:** MongoDB, Cassandra, Redis

**3. OLTP vs OLAP & Difference Database**

**Pengenalan:**

Sistem database dapat dikategorikan berdasarkan tujuan penggunaannya:

**OLTP (Online Transaction Processing):**

* Definisi: Sistem database yang berfokus pada operasi CRUD (Create, Read, Update, Delete) dengan latensi rendah dan throughput tinggi.
* Penggunaan: Transaksi online seperti pemesanan, pembayaran, dan pencatatan inventaris.

**OLAP (Online Analytical Processing):**

* Definisi: Sistem database yang berfokus pada analisis data agregat dan kompleks untuk pengambilan keputusan.
* Penggunaan: Pelaporan, analisis tren, dan prediksi.

**Difference Database:**

* Definisi: Menyimpan data diferensial dari database utama untuk sinkronisasi data dan replikasi.
* Penggunaan: Memperbarui data di beberapa server secara efisien.

**Contoh:**

* **OLTP:** MySQL, PostgreSQL
* **OLAP:** Amazon Redshift, Google BigQuery
* **Difference Database:** Apache Kafka, Debezium

**4. Data Lake**

**Pengenalan:**

Data Lake adalah repositori data terpusat dalam format mentah yang menyimpan berbagai jenis data dari berbagai sumber.

**Manfaat:**

* Skalabilitas tinggi untuk menyimpan data besar
* Fleksibilitas untuk analisis data dengan berbagai alat
* Wawasan baru dari kombinasi data yang berbeda

**Tantangan:**

* Kualitas data yang perlu dijaga
* Keamanan data yang perlu dipastikan
* Kompleksitas pengelolaan dan analisis data

**Contoh:**

* Amazon S3
* Google Cloud Storage

**5. Data Warehouse**

**Pengenalan:**

Data Warehouse adalah gudang data terstruktur yang dirancang untuk analisis. Data dikurasi, dibersihkan, dan diubah untuk mendukung kueri kompleks dan pelaporan.

**Manfaat:**

* Integrasi data dari berbagai sumber
* Performa yang dioptimalkan untuk analisis
* Akses data yang mudah untuk pengambilan keputusan

**Tantangan:**

* Biaya infrastruktur yang tinggi
* Kompleksitas pengembangan dan pemeliharaan

**Contoh:**

* Snowflake
* Teradata

**6. Data Mart**

**Pengenalan:**

Data Mart adalah subset data warehouse yang difokuskan pada topik atau departemen tertentu.

**Manfaat:**

* Akses data yang lebih cepat dan mudah untuk pengguna
* Keamanan dan kontrol data yang lebih baik

**Tantangan:**

* Duplikasi data
* Ketidakkonsistenan data dengan data warehouse

**Contoh:**

* Data Mart penjualan
* Data Mart