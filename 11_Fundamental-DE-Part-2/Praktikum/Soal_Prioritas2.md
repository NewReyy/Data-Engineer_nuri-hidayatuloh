# Soal Prioritas **2 (20)**

1. Anda diberi tugas untuk merancang sistem basis data untuk sebuah perusahaan e-commerce. Perusahaan ini memiliki data yang sangat beragam, mulai dari data transaksi pelanggan hingga log interaksi pengguna di website. Diskusikan pendekatan yang akan Anda gunakan untuk mengelola data ini, termasuk pemilihan antara basis data relasional dan NoSQL, serta strategi untuk mengintegrasikan data terstruktur dan tidak terstruktur.

## Pendekatan Merancang Sistem Basis Data untuk Perusahaan E-commerce

Berikut adalah pendekatan yang akan saya gunakan untuk merancang sistem basis data untuk perusahaan e-commerce:

**1. Memahami Kebutuhan Bisnis**

Langkah pertama adalah memahami kebutuhan bisnis secara menyeluruh. Ini termasuk:

* Jenis data yang dikumpulkan
* Bagaimana data digunakan
* Persyaratan kinerja dan skalabilitas
* Anggaran dan sumber daya yang tersedia

**2. Memilih Arsitektur Basis Data**

Setelah memahami kebutuhan bisnis, langkah selanjutnya adalah memilih arsitektur basis data yang tepat. Ada dua pilihan utama:

* **Basis Data Relasional:** Cocok untuk data terstruktur yang terorganisir dalam tabel dan kolom.
* **Basis Data NoSQL:** Cocok untuk data tidak terstruktur yang tidak memiliki format yang pasti.

**3. Memilih Jenis Basis Data**

Setelah memilih arsitektur basis data, langkah selanjutnya adalah memilih jenis basis data yang tepat. Ada banyak pilihan basis data relasional dan NoSQL yang tersedia, masing-masing dengan kelebihan dan kekurangannya.

**Berikut beberapa contohnya:**

* **Basis Data Relasional:** MySQL, PostgreSQL, Oracle
* **Basis Data NoSQL:** MongoDB, Cassandra, CouchDB
- Saya lebih memilih menggunakan Basis Data Relasional dikarenakan isi dari keperluan perusahaan yakni **data transaksi pelanggan hingga log interaksi pengguna di website** sudah tertera jelas tentunya isi dari setiap transaksi pelanggan apa saja seperti produk yang dibeli, kapan dibeli, menggunakan metode pembayaran apa, quantitas produk yang dibeli. Dan log interaksi pengguna bisa berisi seperti log aktivitas pengguna ketika menggunakan aplikasi e-commerce.

**4. Merancang Skema Basis Data**

Langkah selanjutnya adalah merancang skema basis data. Skema mendefinisikan struktur tabel dan hubungan antar tabel.

**5. Integrasi Data Terstruktur dan Tidak Terstruktur**

Perusahaan e-commerce umumnya memiliki data terstruktur dan tidak terstruktur. Untuk mengintegrasikan kedua jenis data ini, beberapa strategi dapat digunakan:

* **Polyglot Persistence:** Menyimpan data terstruktur dan tidak terstruktur dalam basis data yang berbeda.
* **Hybrid Database:** Menyimpan data terstruktur dan tidak terstruktur dalam satu basis data.
* **Data Lake:** Menyimpan semua data dalam satu tempat, baik terstruktur maupun tidak terstruktur.

**6. Implementasi dan Pengujian**

Setelah merancang sistem basis data, langkah selanjutnya adalah mengimplementasikannya dan mengujinya secara menyeluruh.

**7. Pemeliharaan dan Monitoring**

Sistem basis data perlu dipelihara dan dipantau secara berkala untuk memastikan performanya optimal.

**Berikut beberapa pertimbangan tambahan:**

* **Skalabilitas:** Sistem basis data harus dapat menskalakan dengan pertumbuhan bisnis.
* **Keamanan:** Data harus disimpan dengan aman dan terjamin.
* **Ketersediaan:** Sistem basis data harus selalu tersedia untuk pengguna.

## Referensi

* **Memilih Database Ideal untuk Toko E-Commerce Anda:** [https://appmaster.io/id/blog/database-ideal-untuk-toko-e-commerce](https://appmaster.io/id/blog/database-ideal-untuk-toko-e-commerce)
* **Perbandingan Lengkap Relational Database vs NoSQL Database:** [URL yang tidak valid dihapus]
* **10 Jenis Database NoSQL Terbaik untuk Digunakan pada Tahun 2023:** [https://www.g2.com/categories/nosql-databases](https://www.g2.com/categories/nosql-databases)
* **Merancang Database E-Commerce: Praktik Terbaik:** [https://appmaster.io/id/blog/merancang-database-e-niaga](https://appmaster.io/id/blog/merancang-database-e-niaga)
* **Perancangan Database E-Commerce dengan PostgreSQL:** [https://medium.com/@naputami/desain-database-dengan-postgresql-b32e79f204f2](https://medium.com/@naputami/desain-database-dengan-postgresql-b32e79f204f2)
* **Normalisasi Basis Data:** [https://en.wikipedia.org/wiki/Database_normalization](https://en.wikipedia.org/wiki/Database_normalization)