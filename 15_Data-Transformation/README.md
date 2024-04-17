# Resume Data Transformation

Data transformation adalah langkah mendasar dalam proses integrasi data yang mengacu pada proses mengkonversi data dari suatu format atau struktur ke dalam jenis lainnya. Data transformation memiliki peran penting karena:

1. **Mengizinkan penyatuan data dari berbagai sumber**: Ini memungkinkan penggabungan data yang berasal dari sumber-sumber yang berbeda menjadi satu kesatuan, memudahkan analisis lintas platform.
   
2. **Memastikan kualitas dan konsistensi data**: Proses ini membantu memastikan bahwa data yang digunakan dalam analisis memiliki kualitas yang baik dan konsisten, mengurangi risiko kesalahan atau bias dalam analisis.

3. **Memfasilitasi analisis data dan intelijen bisnis**: Dengan mentransformasi data ke dalam format yang lebih sesuai, proses analisis data dan pengambilan keputusan bisnis menjadi lebih efisien dan efektif.

## Jenis-Jenis Data Transformation:

1. **Normalization**: Normalisasi bertujuan untuk menyesuaikan skala data ke dalam rentang standar. Hal ini dilakukan untuk memastikan bahwa setiap fitur memberikan kontribusi yang seimbang dalam perhitungan dalam algoritma machine learning. Metode umum normalisasi antara lain adalah min-max scaling dan z-score normalization. Use cases: neural networks dan algoritma yang mengandalkan besaran fitur.

2. **Encoding**: Encoding adalah proses mengubah data kategorikal ke dalam format numerik. Hal ini diperlukan karena sebagian besar algoritma pembelajaran mesin memerlukan masukan yang bersifat numerik. Metode umum encoding meliputi one-hot encoding (mengkodekan setiap kategori menjadi kolom biner) dan label encoding (menetapkan bilangan bulat untuk setiap kategori). Use cases: analisis regresi dan tugas klasifikasi.

3. **Aggregation**: Agregasi merupakan proses merangkum atau menggabungkan data untuk keperluan analisis. Hal ini dilakukan untuk memberikan tampilan yang lebih ringkas dari data yang ada. Metode umum aggregasi meliputi fungsi-fungsi seperti sum, average, count, max, dan min. Use cases: analisis data time series dan analisis berbasis kelompok.

## Tantangan dalam Data Transformation:

1. **Nilai-nilai yang Hilang**: Nilai-nilai yang hilang dapat muncul karena berbagai alasan dan dapat mengganggu hasil analisis atau menyebabkan kesalahan dalam model pembelajaran mesin. Metode umum untuk menangani nilai yang hilang termasuk deletion, imputation, dan forward/backward fill.

2. **Outlier**: Outlier adalah titik data yang signifikan secara statistik dan dapat mempengaruhi hasil analisis. Metode identifikasi outlier meliputi z-score dan interquartile range (IQR).

3. **Memastikan Integritas dan Menghindari Kehilangan Data**: Penting untuk memastikan bahwa data tetap akurat, konsisten, dan tidak berubah selama penyimpanan atau transfer. Metode umum untuk memastikan integritas data termasuk regular backups, validasi checks, dan checksums.

## Alat-Alat Data Transformation:

Alat ETL (Extract, Transform, Load) membantu dalam mengumpulkan data dari berbagai sumber, memodifikasinya sesuai kebutuhan, lalu menyimpannya di tempat terpusat.

## Data Wrangling dengan Pandas di Python:

Data wrangling adalah proses pembersihan dan pengorganisasian data yang berantakan untuk membuatnya cocok untuk analisis. Beberapa metode yang umum digunakan dalam data wrangling dengan Pandas di Python antara lain:

1. **Discovering**: Melakukan eksplorasi awal terhadap data untuk memahami isinya, mengevaluasi ukuran, dan mengidentifikasi jenis datanya.

   - `df.head()`: Melihat beberapa baris pertama dari kumpulan data.
   - `df.info()`: Mendapatkan ringkasan tentang kumpulan data, termasuk tipe data dan jumlah nilai non-null.
   - `df.describe()`: Mendapatkan statistik deskriptif untuk kolom numerik.

2. **Structuring**: Mengatur ulang data agar sesuai untuk analisis. Beberapa metode untuk melakukan hal ini antara lain `df.pivot()`, `df.melt()`, dan `df.set_index('column_name')`.

3. **Cleaning**: Mengatasi masalah kualitas data seperti nilai yang hilang, duplikat, atau data yang salah. Beberapa metode yang umum digunakan termasuk `df.dropna()`, `df.drop_duplicates()`, dan `df.replace(old_value, new_value)`.

4. **Enriching**: Menambahkan informasi baru ke dalam kumpulan data atau mengintegrasikannya dengan sumber data lainnya. Contoh metode termasuk `df['new_column'] = ...` dan `pd.merge(df1, df2, on='key')`.

5. **Validating**: Memastikan bahwa kumpulan data mematuhi aturan atau standar tertentu. Ini bisa meliputi pemeriksaan tipe data, rentang nilai, atau kriteria lainnya. Contoh metode termasuk `df.dtypes` dan `assert condition`.

6. **Publishing**: Persiapan data untuk analisis lebih lanjut atau visualisasi. Langkah ini melibatkan penyimpanan data yang sudah dibersihkan dan disusun. Contoh metode termasuk `df.to_csv('cleaned_data.csv')` dan `df.to_excel('cleaned_data.xlsx')`.