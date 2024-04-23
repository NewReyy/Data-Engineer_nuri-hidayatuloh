## No. 1 Jenis Data Pipeline yang Cocok

Berdasarkan kasus e-commerce yang ingin mendapatkan pengetahuan mengenai jumlah transaksi per bulan, jenis barang yang sering dibeli, dan persentase keuntungan, jenis data pipeline yang cocok adalah **Batch Processing Pipeline**.

**Alasan:**

* Data yang diproses **berupa data historis** yang disimpan dalam database, seperti data transaksi, data produk, dan data keuangan.
* Data pipeline ini **tidak memerlukan pemrosesan real-time**. Pengetahuan yang ingin diperoleh platform e-commerce dapat dihitung secara berkala, seperti per bulan atau per kuartal.
* Batch processing pipeline **lebih hemat biaya** dibandingkan dengan stream processing pipeline, karena tidak memerlukan infrastruktur yang kompleks untuk menangani data streaming.

## No. 2 Diagram Data Pipeline

Berikut adalah diagram sederhana dari Batch Processing Pipeline untuk kasus e-commerce:

<img alt="diagram" width="1000" src="../Screenshots/Diagram Data Pipeline.png">

**Penjelasan diagram:**

**1. Sumber Data:**
* Data transaksi, data produk, dan data keuangan disimpan dalam database.

**2. Batch Ingestion:**

* **Penjadwalan:** Menentukan waktu dan frekuensi pengambilan data dari database (misalnya, setiap tanggal 1 setiap bulan).
* **Ekstraksi Data:** Mengambil data dari database sesuai dengan periode yang ditentukan (misalnya, data transaksi bulan Januari).
* **Transformasi Data:** Mengubah format data agar kompatibel dengan sistem pemrosesan data (misalnya, mengubah format tanggal).
* **Pemuatan Data:** Menyimpan data yang telah diekstrak dan diubah formatnya ke staging area.

**3. Data Cleansing:**

* **Identifikasi Kesalahan:** Mencari data yang tidak valid, duplikat, atau tidak lengkap.
* **Koreksi Kesalahan:** Memperbaiki data yang tidak valid, duplikat, atau tidak lengkap.
* **Penghapusan Data:** Menghapus data yang tidak dapat diperbaiki.

**4. Data Processing:**

* **Perhitungan Jumlah Transaksi:** Menghitung jumlah transaksi per bulan.
* **Analisis Jenis Barang yang Sering Dibeli:** Menghitung jumlah dan persentase penjualan setiap jenis barang.
* **Perhitungan Persentase Keuntungan:** Menghitung keuntungan dari penjualan produk dan membaginya dengan total pendapatan untuk mendapatkan persentase keuntungan.

**5. Data Aggregation:**

* **Penggabungan Data:** Menggabungkan hasil perhitungan dari data processing.
* **Penyimpanan Data:** Menyimpan hasil agregasi data ke data warehouse.

**6. Data Visualization:**

* **Pembuatan Dashboard:** Membuat dashboard visualisasi data yang menampilkan jumlah transaksi per bulan, jenis barang yang sering dibeli, dan persentase keuntungan.
* **Pembuatan Laporan:** Membuat laporan tertulis yang menjelaskan hasil analisis data.
