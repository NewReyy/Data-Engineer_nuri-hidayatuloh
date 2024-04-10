# RESUME WORKFLOW ORCHESTRATION WITH AIRFLOW

Apache Airflow adalah alat manajemen alur kerja (workflow) yang kuat yang digunakan untuk mengatur alur kerja yang kompleks. Alat ini didasarkan pada beberapa konsep kunci:

1. **Alur Kerja (Workflow)**: Sejumlah tugas yang saling terhubung yang bertujuan untuk mencapai tujuan tertentu.
2. **Tugas (Task)**: Satuan kerja individual dalam suatu alur kerja.
3. **Operator**: Komponen yang bertanggung jawab untuk mengeksekusi sebuah tugas.
4. **DAG (Directed Acyclic Graph)**: Graf yang digunakan untuk merepresentasikan sebuah alur kerja. DAG dalam Airflow memiliki sifat-sifat berikut:
   - Mereka adalah graf berarah tanpa siklus.
   - Dapat terdiri dari berbagai tugas dengan operator-operator yang berbeda.
   - Tugas dapat bercabang ke tugas lain.
   - Berbagai tugas dapat berkumpul menjadi satu tugas.

## Menyiapkan Apache Airflow di Docker

Untuk mendeploy Airflow menggunakan Docker Compose, perlu mengikuti langkah-langkah berikut:

1. Instal Docker Community Edition.
2. Instal Docker Compose versi 1.27.0 atau yang lebih baru.

Bisa dengan cara mengambil file `docker-compose.yaml` untuk Airflow dengan menjalankan:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.2/docker-compose.yaml'
```

Beberapa direktori dalam kontainer sudah terpasang, yang berarti isinya disinkronkan antara mesin host dan kontainer.

Pada semua sistem operasi, setelah mengambil file YAML, jalankan perintah berikut untuk menginisialisasi Airflow, melakukan migrasi database, dan membuat akun pengguna pertama:

```bash
docker-compose up airflow-init
```

Setelah inisialisasi, maka akan terlihat pesan seperti ini:

```
Upgrades done
Admin user airflow created
2.0.2
```

Akun yang dibuat memiliki login `airflow` dan kata sandi `airflow`.

Mulai semua layanan Airflow menggunakan:

```bash
docker-compose up
```

Di terminal kedua, dapat memeriksa status kontainer untuk memastikan semuanya Healthy:

```bash
docker ps
```

## Berinteraksi dengan Apache Airflow

Anda dapat berinteraksi dengan Airflow melalui tiga cara:

1. **Perintah CLI**: Menjalankan perintah seperti `airflow info` menggunakan Docker Compose atau langsung melalui bash atau Python dalam kontainer.

   ```bash
   docker-compose run airflow-worker airflow info
   ```

   Atau di Linux atau macOS:

   ```bash
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.2/airflow.sh'
   chmod +x airflow.sh
   ./airflow.sh info
   ```

2. **Antarmuka Web**: Akses antarmuka web di `http://localhost:8080` menggunakan kredensial default (`airflow`/`airflow`).

3. **REST API**: Berinteraksi dengan REST API menggunakan alat seperti cURL. Misalnya, untuk mengambil daftar kolam (pools):

   ```bash
   ENDPOINT_URL="http://localhost:8080/"
   curl -X GET \
       --user "airflow:airflow" \
       "${ENDPOINT_URL}/api/v1/pools"
   ```

## Menghentikan dan Menghapus Kontainer

Untuk menghentikan dan menghapus kontainer, hapus volume yang berisi data database, dan unduh gambar, jalankan:

```bash
docker-compose down --volumes --rmi all
```

## Fitur dan Penggunaan Apache Airflow

Apache Airflow dipilih karena fiturnya yang lengkap, pengaturan yang mudah, sifat open-source, dan skalabilitasnya.

Membuat sebuah DAG di Airflow dapat diibaratkan sebagai:

1. Mengumpulkan kedelai
2. Membuat tempeh dan/atau susu kedelai
3. Mendistribusikan produk

DAG dapat dieksekusi dengan membuka `localhost:8080`, masuk dengan kredensial, dan mengklik tombol toggle.

XCOM memfasilitasi komunikasi lintas-tugas untuk pertukaran data kecil. Namun, tidak cocok untuk data besar seperti DataFrame atau file.

Taskflow dapat digunakan untuk membuat pipeline data di Airflow.

Membuat sebuah DAG dengan Gambar Kustom memerlukan penggunaan perpustakaan Python bawaan untuk:

1. Membuat tabel-tabel posting
2. Mengumpulkan data dari sebuah API
3. Memasukkan data ke dalam tabel

Gambar Kustom ini dapat digunakan untuk menjalankan sebuah DAG yang membutuhkan dependensi tambahan yang tidak tersedia secara default di Python, terutama saat menjalankan Airflow dengan Docker Compose.

Untuk membuat koneksi ke database Postgres, ikuti langkah-langkah berikut:

1. Pilih "Connections" dalam antarmuka pengguna.
2. Klik "Add" dan isi detail seperti nama layanan (misalnya, `postgres` jika menggunakan Docker Compose) dan nama skema.
3. Simpan koneksi tersebut.

Apache Airflow memungkinkan pengiriman email saat DAG berhasil atau gagal, dapat dikonfigurasi dengan pengaturan SMTP atau server SMTP lokal seperti MailHog untuk pengujian.