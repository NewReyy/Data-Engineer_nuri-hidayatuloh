# RESUME DATA WAREHOUSE & DATA LAKE PART 2

## 1. Pengenalan Data Warehouse
Data Warehouse merupakan sebuah sistem yang mengagregasikan data dari berbagai sumber menjadi data yang konsisten untuk mendukung proses seperti Data Analysis, Data Mining, AI, dan Machine Learning. Berikut adalah contoh flow Data Warehouse yang paling relevan:
   
   a. **Data Sources**: Data diambil dari berbagai sumber seperti sistem operasi, ERP, CRM, dsb.
   b. **Data Validation, Cleaning, Transforming, Aggregating**: Data melalui proses validasi, pembersihan, transformasi, dan aggregasi untuk memastikan konsistensi dan keakuratan.
   c. **ETL (Extract, Transform, Load)**: Proses integrasi data dari berbagai sumber ke dalam data warehouse.
   d. **Data Warehouse**: Tempat penyimpanan data yang telah diproses dan dimuat.
   e. **Datamarts**: Sub-bagian dari data warehouse untuk tujuan analisis tertentu.
   f. **OLAP (Online Analytical Processing)**: Teknologi untuk melakukan analisis data di data warehouse.
   g. **Analysis, Data Mining, Data Visualization, Reports, Dashboards, Alerts**: Hasil analisis data ditampilkan dalam berbagai bentuk.

## 2. Perbedaan antara Data Lake & Data Warehouse
   - **Data Lake** adalah tempat penyimpanan data mentah tanpa tujuan pasti, mudah diupdate, dan digunakan oleh data scientist.
   - **Data Warehouse** adalah repositori untuk data yang telah diproses dan memiliki tujuan tertentu, lebih rumit, dan digunakan oleh profesional bisnis.

## 3. Data Lakehouse
Data Lakehouse menggabungkan fleksibilitas dan efisiensi biaya dari data lake dengan fitur manajemen dan struktur data dari data warehouse pada satu platform.

## 4. Teknologi Penggunaan Data Warehouse
   - AWS Redshift
   - Google Big Query
   - Clickhouse
   - Snowflake
   - Databricks
   - Apache Dorris
   - PostgreSQL Citus Extension: Menyediakan skabilitas, kinerja, keandalan, dan kesederhanaan.

 PostgreSQL Citus Extension

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

1. Membuat Tabel Terpartisi:

```sql
-- Membuat tabel terpartisi berdasarkan kolom tanggal
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL
)
PARTITION BY RANGE (sale_date);

-- Membuat partisi untuk setiap bulan dalam satu tahun
CREATE TABLE sales_2024_01 PARTITION OF sales
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
CREATE TABLE sales_2024_02 PARTITION OF sales
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
-- Lanjutkan untuk setiap bulan...
```

2. Menjalankan Kueri:

```sql
-- Menjalankan kueri untuk mencari penjualan pada bulan Januari 2024
SELECT * FROM sales_2024_01 WHERE sale_date BETWEEN '2024-01-01' AND '2024-02-01';
```

2. Menjalankan Kueri:

```sql
-- Menjalankan kueri untuk menghitung total pendapatan dan biaya pada tanggal tertentu
SELECT SUM(revenue), SUM(cost) FROM analytics_data WHERE date = '2024-01-01';
```

### PostgreSQL Citus Extension

#### Contoh Penggunaan

Untuk menggunakan Citus dalam PostgreSQL, Anda perlu menginstal ekstensi Citus terlebih dahulu. Berikut adalah contoh penggunaan untuk membuat tabel terdistribusi dan menjalankan kueri menggunakan Citus.

1. Membuat Tabel Terdistribusi dengan Citus:

```sql
-- Membuat tabel terdistribusi dengan Citus
CREATE TABLE distributed_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Menjadikan tabel terdistribusi menggunakan Citus
SELECT create_distributed_table('distributed_table', 'id');
```

2. Menjalankan Kueri dengan Citus:

```sql
-- Menjalankan kueri menggunakan Citus
SELECT * FROM distributed_table WHERE id = 1;
```

# Columnar Table

Columnar table adalah format penyimpanan data yang menyimpan data dalam kolom, bukan baris. Format ini menawarkan beberapa keuntungan dibandingkan format penyimpanan baris tradisional:

- **Kompresi**: Dapat dikompresi lebih efektif daripada format penyimpanan baris tradisional.
- **Kinerja**: Memberikan kinerja yang lebih baik untuk kueri analitik yang melibatkan kolom tertentu.
- **Skalabilitas**: Menskalakan secara lebih efisien daripada format penyimpanan baris tradisional.

## Contoh Penggunaan

Columnar table menyimpan data dalam kolom, yang dapat meningkatkan kinerja untuk kueri analitik. Berikut adalah contoh penggunaan untuk membuat tabel dengan format penyimpanan kolom.

* Membuat Tabel Columnar:

```sql
-- Membuat tabel dengan format penyimpanan kolom
CREATE COLUMNAR TABLE analytics_data (
    id SERIAL PRIMARY KEY,
    date DATE,
    revenue DECIMAL,
    cost DECIMAL
);
```

Replikasi dan sharding adalah dua teknik berbeda yang digunakan untuk meningkatkan skalabilitas dan ketahanan database, namun mereka menangani masalah tersebut dengan cara yang berbeda.

**Replikasi (Replication)**

Replikasi adalah proses menduplikasi data dari satu server database ke server database lainnya. Hal ini membuat salinan data yang dapat digunakan untuk berbagai keperluan, seperti:

* **Ketahanan (High Availability):**  Jika server database utama gagal, server replika dapat digunakan untuk melanjutkan operasi. Ini meminimalkan downtime dan memastikan aksesibilitas data yang tinggi.
* **Beban Baca (Read Load Balancing):**  Replika dapat digunakan untuk menangani beban baca dari database, sehingga mengurangi beban pada server utama dan meningkatkan kinerja keseluruhan.
* **Backup dan Pemulihan (Backup and Recovery):**  Replika dapat digunakan sebagai cadangan terkini dari data, sehingga proses pemulihan dari kegagalan menjadi lebih cepat dan mudah.
* **Contoh Penggunaan Replikasi**:

```sql
-- Menambahkan server replika
CREATE SERVER replica_server FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host 'replica.example.com', dbname 'database_name');

-- Membuat tabel replika
CREATE FOREIGN TABLE replica_table (LIKE original_table) SERVER replica_server;

-- Menjalankan kueri pada server replika
SELECT * FROM replica_table WHERE id = 1;
```

**Sharding (Pemisahan Data)**

Sharding adalah teknik memecah data menjadi beberapa bagian yang lebih kecil dan menyimpannya di server database yang berbeda.  Ini berguna untuk:

* **Skalabilitas Horizontal (Horizontal Scalability):**  Dengan menambahkan lebih banyak server database, dapat meningkatkan kapasitas penyimpanan dan pemrosesan data secara keseluruhan. 
* **Kinerja Query Tertentu (Performance for Specific Queries):**  Sharding dapat mengoptimalkan kueri yang hanya melibatkan sebagian data dengan mengarahkannya ke shard yang relevan.

* Sharding:

```sql
-- Membuat shard
CREATE TABLE shard1 (LIKE original_table INCLUDING ALL) PARTITION BY RANGE (id);
CREATE TABLE shard2 (LIKE original_table INCLUDING ALL) PARTITION BY RANGE (id);

-- Menambahkan data ke setiap shard
INSERT INTO shard1 SELECT * FROM original_table WHERE id < 1000;
INSERT INTO shard2 SELECT * FROM original_table WHERE id >= 1000;

-- Menjalankan kueri pada shard yang relevan
SELECT * FROM shard1 WHERE id = 1;
```

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
1. Star Schema:

```sql
-- Membuat tabel fakta dan tabel dimensi untuk skema star
CREATE TABLE sales_fact (
    product_id INT,
    date_id DATE,
    amount DECIMAL
);

CREATE TABLE product_dim (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT
);
-- Lanjutkan dengan tabel dimensi lainnya (misalnya, date_dim, category_dim)
```

**Snowflake Schema:**

Skema snowflake adalah pengembangan dari skema star. Skema ini membagi tabel dimensi menjadi beberapa tabel yang lebih kecil berdasarkan atributnya. Hal ini membantu:

* **Mengurangi redundansi data:**  Atribut yang sama tidak disimpan di beberapa tabel.
* **Meningkatkan kinerja query:**  Hanya tabel yang relevan yang perlu dipindai untuk query tertentu.

Namun, skema snowflake lebih kompleks untuk dirancang dan dikelola dibandingkan skema star.

**Contoh:**  Tabel dimensi produk dibagi menjadi tabel kategori produk, subkategori produk, dan merek produk.
2. Snowflake Schema:

```sql
-- Membuat tabel dimensi yang lebih terpisah untuk skema snowflake
CREATE TABLE product_category_dim (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE product_subcategory_dim (
    subcategory_id INT PRIMARY KEY,
    subcategory_name VARCHAR(100),
    category_id INT REFERENCES product_category_dim(category_id)
);
-- Lanjutkan dengan tabel dimensi lainnya (misalnya, date_dim, brand_dim)
```

**One Big Table (OBT):**

OBT adalah skema yang menyimpan semua data dalam satu tabel besar. Skema ini mudah diimplementasikan dan ideal untuk data yang tidak terstruktur atau semi-terstruktur. 

Namun, OBT dapat:

* **Menjadi tidak efisien:**  Data yang jarang digunakan disimpan bersama dengan data yang sering digunakan.
* **Menyebabkan kinerja query yang lambat:**  Memindai seluruh tabel untuk query tertentu bisa memakan waktu lama.

**Contoh:**  Menyimpan semua data sensor dari perangkat IoT dalam satu tabel.

```sql
-- Membuat satu tabel besar untuk skema One Big Table
CREATE TABLE big_table (
    id SERIAL PRIMARY KEY,
    data JSONB
);
```

**Tips Memilih Skema Database:**

* **Pertimbangkan jenis data :**  Skema star ideal untuk data numerik, skema snowflake ideal untuk data atribut yang kompleks, dan OBT ideal untuk data yang tidak terstruktur.
* **Pertimbangkan kebutuhan analisis :**  Skema star ideal untuk agregasi data dan analisis OLAP, skema snowflake ideal untuk query yang kompleks, dan OBT ideal untuk analisis data real-time.
* **Pertimbangkan skalabilitas dan kinerja:**  Skema snowflake lebih skalabel daripada skema star, dan OBT dapat berkinerja buruk untuk query yang kompleks.