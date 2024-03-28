# Perbandingan antara Data Lake dan Data Warehouse

Data Warehouse merupakan suatu sistem yang menyatukan data dari berbagai sumber untuk mendukung analisis data, data mining, AI, dan machine learning.

Perbedaan antara Data Lake dengan Data Warehouse:

- **Data Lake**: Cenderung mencakup data mentah dalam jumlah yang besar dengan tujuan yang mungkin belum ditentukan. Digunakan oleh data scientists, sangat mudah diakses, dan cepat diperbarui.

- **Data Warehouse**: Merupakan repository untuk data terstruktur dan terfilter yang telah diproses untuk tujuan tertentu. Digunakan oleh business professionals, cenderung lebih rumit, dan memerlukan biaya lebih mahal untuk membuat perubahan.

# Data Lakehouse

Data Lakehouse adalah arsitektur manajemen data terbuka yang menggabungkan fleksibilitas dan efisiensi biaya dari data lake dengan manajemen dan fitur struktur data warehouse, yang terdapat pada satu platform data.

# PostgreSQL Citus Extension

Citus adalah ekstensi open source untuk PostgreSQL yang mengubah Postgres menjadi database terdistribusi. Menggunakan tabel yang didistribusikan, tabel referensi, dan SQL query engine yang terdistribusi.

## Keuntungan Citus

- **Skalabilitas**: Citus dapat menskalakan secara horizontal untuk menangani data yang lebih besar dan beban kerja yang lebih tinggi.
- **Kinerja**: Dioptimalkan untuk kueri analitik dan dapat memberikan kinerja yang lebih baik daripada PostgreSQL tradisional untuk beban kerja tersebut.
- **Keandalan**: Dirancang untuk menjadi sangat andal dan dapat terus beroperasi bahkan jika beberapa node gagal.
- **Kesederhanaan**: Mudah digunakan dan dikelola, dan kompatibel dengan sebagian besar alat dan aplikasi PostgreSQL.

## Kapan tidak menggunakan Citus?

- Ketika tidak mengharapkan beban kerja tumbuh melampaui satu node Postgres.
- Analisis offline tanpa kebutuhan untuk pengambilan real-time.
- Aplikasi analisis yang tidak perlu mendukung sejumlah besar pengguna yang bersamaan.
- Kueri yang mengembalikan hasil ETL berat data daripada ringkasan.

# Table Partitioning

Table partitioning adalah teknik membagi tabel menjadi beberapa bagian yang lebih kecil. Teknik ini menawarkan beberapa keuntungan:

- **Kinerja**: Meningkatkan kinerja kueri dengan memungkinkan database untuk hanya memindai partisi yang relevan.
- **Manajemen data**: Memudahkan untuk mengelola data dengan memungkinkan untuk menghapus atau memindahkan partisi secara individual.
- **Skalabilitas**: Membantu menskalakan database dengan memungkinkan untuk mendistribusikan partisi di beberapa node.

# Columnar Table

Columnar table adalah format penyimpanan data yang menyimpan data dalam kolom, bukan baris. Format ini menawarkan beberapa keuntungan dibandingkan format penyimpanan baris tradisional:

- **Kompresi**: Dapat dikompresi lebih efektif daripada format penyimpanan baris tradisional.
- **Kinerja**: Memberikan kinerja yang lebih baik untuk kueri analitik yang melibatkan kolom tertentu.
- **Skalabilitas**: Menskalakan secara lebih efisien daripada format penyimpanan baris tradisional.

Replikasi dan sharding adalah dua teknik berbeda yang digunakan untuk meningkatkan skalabilitas dan ketahanan database, namun mereka menangani masalah tersebut dengan cara yang berbeda.

**Replikasi (Replication)**

Replikasi adalah proses menduplikasi data dari satu server database ke server database lainnya. Hal ini membuat salinan data yang dapat digunakan untuk berbagai keperluan, seperti:

* **Ketahanan (High Availability):**  Jika server database utama gagal, server replika dapat digunakan untuk melanjutkan operasi. Ini meminimalkan downtime dan memastikan aksesibilitas data yang tinggi.
* **Beban Baca (Read Load Balancing):**  Replika dapat digunakan untuk menangani beban baca dari database, sehingga mengurangi beban pada server utama dan meningkatkan kinerja keseluruhan.
* **Backup dan Pemulihan (Backup and Recovery):**  Replika dapat digunakan sebagai cadangan terkini dari data, sehingga proses pemulihan dari kegagalan menjadi lebih cepat dan mudah.

**Sharding (Pemisahan Data)**

Sharding adalah teknik memecah data menjadi beberapa bagian yang lebih kecil dan menyimpannya di server database yang berbeda.  Ini berguna untuk:

* **Skalabilitas Horizontal (Horizontal Scalability):**  Dengan menambahkan lebih banyak server database, dapat meningkatkan kapasitas penyimpanan dan pemrosesan data secara keseluruhan. 
* **Kinerja Query Tertentu (Performance for Specific Queries):**  Sharding dapat mengoptimalkan kueri yang hanya melibatkan sebagian data dengan mengarahkannya ke shard yang relevan.

**Ringkasan Perbedaan Replikasi dan Sharding**

| Fitur               | Replikasi                            | Sharding                                        |
|---------------------|--------------------------------------|-------------------------------------------------|
| **Tujuan**          | Ketahanan, Beban Baca                | Skalabilitas Horizontal, Kinerja Query Tertentu |
| **Duplikasi Data**  | Seluruh data direplikasi             | Data dibagi dan disimpan di tempat berbeda      |
| **Server Database** | Beberapa server (primer dan replika) | Banyak server untuk shard yang berbeda          |
| **Penggunaan Umum** | Failover, backup, baca seimbang      | Mengelola data besar, kueri tertarget           |

## Skema Database: Star Schema, Snowflake Schema, dan One Big Table

Skema database adalah cara untuk mengatur data dalam database. Skema yang tepat dapat meningkatkan kinerja, skalabilitas, dan kemudahan penggunaan database. 

Berikut adalah tiga skema database yang umum digunakan:

**Star Schema:**

Skema star adalah skema yang paling sederhana dan paling umum digunakan untuk data warehouse. Skema ini terdiri dari:

* **Tabel Fakta:**  Menyimpan data numerik yang menjadi fokus analisis.
* **Tabel Dimensi:**  Menyimpan data atribut yang mendeskripsikan data fakta.

Tabel fakta terhubung ke tabel dimensi melalui kunci primer. Skema star mudah dipahami dan digunakan, dan performanya optimal untuk agregasi data dan analisis OLAP.

**Contoh:**  Tabel fakta penjualan yang berisi data penjualan, terhubung ke tabel dimensi produk, pelanggan, dan waktu.

**Snowflake Schema:**

Skema snowflake adalah pengembangan dari skema star. Skema ini membagi tabel dimensi menjadi beberapa tabel yang lebih kecil berdasarkan atributnya. Hal ini membantu:

* **Mengurangi redundansi data:**  Atribut yang sama tidak disimpan di beberapa tabel.
* **Meningkatkan kinerja query:**  Hanya tabel yang relevan yang perlu dipindai untuk query tertentu.

Namun, skema snowflake lebih kompleks untuk dirancang dan dikelola dibandingkan skema star.

**Contoh:**  Tabel dimensi produk dibagi menjadi tabel kategori produk, subkategori produk, dan merek produk.

**One Big Table (OBT):**

OBT adalah skema yang menyimpan semua data dalam satu tabel besar. Skema ini mudah diimplementasikan dan ideal untuk data yang tidak terstruktur atau semi-terstruktur. 

Namun, OBT dapat:

* **Menjadi tidak efisien:**  Data yang jarang digunakan disimpan bersama dengan data yang sering digunakan.
* **Menyebabkan kinerja query yang lambat:**  Memindai seluruh tabel untuk query tertentu bisa memakan waktu lama.

**Contoh:**  Menyimpan semua data sensor dari perangkat IoT dalam satu tabel.

**Tips Memilih Skema Database:**

* **Pertimbangkan jenis data :**  Skema star ideal untuk data numerik, skema snowflake ideal untuk data atribut yang kompleks, dan OBT ideal untuk data yang tidak terstruktur.
* **Pertimbangkan kebutuhan analisis :**  Skema star ideal untuk agregasi data dan analisis OLAP, skema snowflake ideal untuk query yang kompleks, dan OBT ideal untuk analisis data real-time.
* **Pertimbangkan skalabilitas dan kinerja:**  Skema snowflake lebih skalabel daripada skema star, dan OBT dapat berkinerja buruk untuk query yang kompleks.