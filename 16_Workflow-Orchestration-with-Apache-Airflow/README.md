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

### Eksekusi DAG melalui Antarmuka Web

**Definisi/Pengertian:**
Eksekusi DAG melalui antarmuka web Apache Airflow adalah proses menjalankan alur kerja yang telah didefinisikan melalui antarmuka pengguna web yang tersedia pada alamat `localhost:8080`. Pengguna akan masuk menggunakan kredensial yang valid, kemudian dapat mengklik tombol toggle untuk memulai atau menjeda eksekusi DAG yang diinginkan.

**Penjelasan:**
Dalam Apache Airflow, DAG (Directed Acyclic Graph) adalah representasi visual dari alur kerja yang ingin dijalankan. Melalui antarmuka web, pengguna dapat dengan mudah menjalankan atau mengelola eksekusi DAG tanpa perlu menggunakan perintah baris perintah (CLI). Ini memberikan fleksibilitas dan kenyamanan dalam menjalankan alur kerja tanpa perlu pengetahuan teknis yang mendalam.

**Contoh Penggunaan:**
Misalnya, pengguna telah membuat DAG untuk mengumpulkan dan memproses data dari sumber eksternal. Setelah mendaftar ke antarmuka web Airflow, pengguna dapat dengan mudah menavigasi ke halaman DAG yang diinginkan, memilih DAG yang ingin dieksekusi, dan kemudian mengklik tombol toggle untuk memulai eksekusi. Proses ini memulai alur kerja yang telah ditentukan dalam DAG, menjalankan setiap langkah tugas secara berurutan.

### Eksekusi DAG melalui Antarmuka Web

```python
# Import modul yang diperlukan
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Tentukan argumen default untuk DAG
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Inisialisasi DAG
dag = DAG(
    'example_dag',
    default_args=default_args,
    description='Contoh DAG sederhana',
    schedule_interval='@once',
)

# Tugas pertama dalam DAG
start_task = DummyOperator(task_id='start_task', dag=dag)

# Tugas terakhir dalam DAG
end_task = DummyOperator(task_id='end_task', dag=dag)

# Hubungkan tugas
start_task >> end_task
```

**Penjelasan:**
- Program di atas mendefinisikan sebuah DAG sederhana yang terdiri dari dua tugas dummy (`start_task` dan `end_task`).
- DAG diinisialisasi dengan argumen default yang ditentukan, termasuk pemilik, waktu mulai, dan pengaturan email.
- Tugas-tugas dibuat dan disertakan dalam DAG dengan menggunakan operator `DummyOperator`.
- Kedua tugas dihubungkan dengan operator `>>`, menunjukkan bahwa `end_task` akan dijalankan setelah `start_task`.
- Ketika DAG dieksekusi, tugas-tugas tersebut akan ditampilkan dalam antarmuka web Airflow dan pengguna dapat menjalankannya dengan mengklik tombol toggle.

### XCOM dalam Apache Airflow

**Definisi/Pengertian:**
XCOM adalah sistem dalam Apache Airflow yang memfasilitasi pertukaran data antara tugas-tugas yang berbeda dalam sebuah alur kerja (DAG). Ini digunakan untuk mengirim dan menerima data kecil antara tugas-tugas.

**Penjelasan:**
Dalam alur kerja Airflow, tugas-tugas sering kali perlu berkomunikasi satu sama lain dan berbagi data untuk menjalankan alur kerja secara efektif. XCOM memungkinkan tugas-tugas ini untuk bertukar informasi dalam bentuk data kecil seperti string, angka, atau struktur data sederhana lainnya. Namun, XCOM tidak cocok untuk mentransfer data besar seperti DataFrame atau file karena kinerja dan keterbatasan memori.

**Contoh Penggunaan:**
Misalkan dalam sebuah alur kerja, tugas pertama menghasilkan sebuah nilai atau informasi yang dibutuhkan oleh tugas kedua. Dengan menggunakan XCOM, nilai ini dapat dikirim dari tugas pertama ke tugas kedua sebagai pesan kecil. Contoh implementasi XCOM adalah saat sebuah tugas menghasilkan hasil yang akan digunakan sebagai input untuk tugas berikutnya dalam alur kerja.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Fungsi untuk tugas pertama
def push_function(**context):
    return 'Data yang dikirim oleh tugas pertama'

# Fungsi untuk tugas kedua
def pull_function(**context):
    data = context['ti'].xcom_pull(task_ids='task_id_tugas_pertama')
    print(data)

# Inisialisasi DAG
dag = DAG(
    'xcom_example',
    description='Contoh penggunaan XCOM dalam Airflow',
    schedule_interval=None,
    start_date=datetime(2024, 4, 10),
)

# Tugas pertama mengirim data menggunakan XCOM
push_task = PythonOperator(
    task_id='task_id_tugas_pertama',
    python_callable=push_function,
    provide_context=True,
    dag=dag,
)

# Tugas kedua menerima data menggunakan XCOM
pull_task = PythonOperator(
    task_id='task_id_tugas_kedua',
    python_callable=pull_function,
    provide_context=True,
    dag=dag,
)

# Hubungkan tugas
push_task >> pull_task
```

**Penjelasan:**
- Dalam contoh ini, terdapat dua tugas yang dijalankan secara berurutan.
- Tugas pertama (`push_task`) menghasilkan data yang dikirim menggunakan XCOM ke tugas kedua (`pull_task`).
- Tugas kedua kemudian menerima data yang dikirim oleh tugas pertama menggunakan XCOM.
- Dalam fungsi `pull_function`, `context['ti'].xcom_pull(task_ids='task_id_tugas_pertama')` digunakan untuk menerima data yang dikirim oleh tugas pertama.

### Taskflow dalam Apache Airflow

**Definisi/Pengertian:**
Taskflow adalah paradigma pemrograman dalam Apache Airflow yang memungkinkan pengguna untuk membuat pipeline data yang kompleks dan terstruktur dengan lebih mudah. Ini memberikan pendekatan yang lebih deklaratif untuk mendefinisikan alur kerja daripada menggunakan pendekatan tradisional yang berbasis pada tugas-tugas individu.

**Penjelasan:**
Taskflow memungkinkan pengguna untuk mendefinisikan alur kerja menggunakan komponen-komponen yang lebih abstrak, seperti serangkaian langkah-langkah yang terkait secara logis, daripada hanya mendasarkan alur kerja pada tugas-tugas individu. Hal ini memungkinkan untuk membuat alur kerja yang lebih mudah dipahami, dikelola, dan dikembangkan.

**Contoh Penggunaan:**
Misalkan pengguna ingin membuat alur kerja untuk memproses data mentah, membersihkannya, dan menyimpan hasilnya ke dalam database. Dengan menggunakan Taskflow, pengguna dapat mendefinisikan langkah-langkah ini sebagai serangkaian tindakan yang saling terkait secara logis, seperti "mengumpulkan data", "membersihkan data", dan "menyimpan data". Kemudian, pengguna dapat menyusun langkah-langkah ini ke dalam sebuah DAG dengan lebih mudah dan intuitif.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Fungsi untuk langkah pertama dalam Taskflow
def collect_data():
    print("Mengumpulkan data")

# Fungsi untuk langkah kedua dalam Taskflow
def clean_data():
    print("Membersihkan data")

# Fungsi untuk langkah ketiga dalam Taskflow
def save_data():
    print("Menyimpan data")

# Inisialisasi DAG
dag = DAG(
    'taskflow_example',
    description='Contoh penggunaan Taskflow dalam Airflow',
    schedule_interval=None,
    start_date=datetime(2024, 4, 10),
)

# Definisikan langkah-langkah dalam Taskflow
collect_task = PythonOperator(
    task_id='collect_data',
    python_callable=collect_data,
    dag=dag,
)

clean_task = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    dag=dag,
)

save_task = PythonOperator(
    task_id='save_data',
    python_callable=save_data,
    dag=dag,
)

# Hubungkan langkah-langkah dalam urutan yang diinginkan
collect_task >> clean_task >> save_task
```

**Penjelasan:**
- Dalam contoh ini, terdapat tiga langkah yang dijalankan secara berurutan dalam sebuah DAG.
- Setiap langkah diimplementasikan sebagai fungsi Python yang dieksekusi oleh operator `PythonOperator`.
- Ketika DAG dieksekusi, langkah-langkah ini akan dieksekusi sesuai dengan urutan yang ditentukan.
- Dalam implementasi ini, langkah-langkah hanya mencetak pesan sederhana, tetapi dalam kasus nyata, langkah-langkah ini dapat melakukan tugas yang lebih kompleks seperti mengumpulkan, membersihkan, dan menyimpan data.

### Pembuatan DAG dengan Gambar Kustom

**Definisi/Pengertian:**
Pembuatan DAG dengan Gambar Kustom dalam Apache Airflow melibatkan penggunaan perpustakaan Python tambahan yang dibangun khusus untuk menjalankan alur kerja yang membutuhkan dependensi tambahan yang tidak tersedia secara default di Python.

**Penjelasan:**
Kadang-kadang, alur kerja yang ingin dijalankan dalam Airflow memerlukan dependensi tambahan yang tidak disertakan dalam instalasi Python standar atau gambar Docker Airflow yang umum digunakan. Dalam kasus seperti itu, pengguna dapat membuat Gambar Kustom yang mengandung dependensi tambahan yang diperlukan untuk menjalankan alur kerja tersebut.

**Contoh Penggunaan:**
Misalkan pengguna ingin menjalankan alur kerja yang menggunakan sebuah perpustakaan Python khusus untuk berinteraksi dengan layanan pihak ketiga yang tidak tersedia secara default. Pengguna dapat membuat Gambar Kustom yang mencakup perpustakaan tambahan ini, kemudian menggunakan gambar tersebut untuk menjalankan DAG dalam lingkungan Airflow. Ini memastikan bahwa semua dependensi yang diperlukan tersedia dalam lingkungan yang dijalankan, sehingga alur kerja dapat berjalan dengan benar.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Fungsi untuk membuat tabel-tabel posting
def create_tables():
    print("Membuat tabel-tabel posting")

# Fungsi untuk mengumpulkan data dari sebuah API
def collect_data_from_api():
    print("Mengumpulkan data dari API")

# Fungsi untuk memasukkan data ke dalam tabel
def insert_data_into_table():
    print("Memasukkan data ke dalam tabel")

# Inisialisasi DAG
dag = DAG(
    'custom_image_dag',
    description='Contoh pembuatan DAG dengan Gambar Kustom',
    schedule_interval=None,
    start_date=datetime(2024, 4, 10),
)

# Definisikan langkah-langkah dalam DAG
create_tables_task = PythonOperator(
    task_id='create_tables',
    python_callable=create_tables,
    dag=dag,
)

collect_data_task = PythonOperator(
    task_id='collect_data',
    python_callable=collect_data_from_api,
    dag=dag,
)

insert_data_task = PythonOperator(
    task_id='insert_data',
    python_callable=insert_data_into_table,
    dag=dag,
)

# Hubungkan langkah-langkah dalam urutan yang diinginkan
create_tables_task >> collect_data_task >> insert_data_task
```

**Penjelasan:**
- Dalam contoh ini, terdapat tiga langkah yang dijalankan secara berurutan dalam sebuah DAG.
- Setiap langkah diimplementasikan sebagai fungsi Python yang dieksekusi oleh operator `PythonOperator`.
- Langkah-langkah ini terkait dengan pembuatan tabel-tabel, pengumpulan data dari sebuah API, dan memasukkan data ke dalam tabel.
- Dalam implementasi ini, fungsi-fungsi hanya mencetak pesan sederhana, tetapi dalam kasus nyata, fungsi-fungsi ini akan melakukan tugas yang sesuai dengan namanya.

### Pembuatan Koneksi ke Database Postgres

**Definisi/Pengertian:**
Pembuatan koneksi ke database Postgres dalam Apache Airflow adalah proses mengonfigurasi sistem untuk berkomunikasi dengan database PostgreSQL. Ini memungkinkan Airflow untuk mengakses dan memanipulasi data yang tersimpan dalam database PostgreSQL.

**Penjelasan:**
Dalam lingkungan Apache Airflow, koneksi ke database Postgres diatur melalui antarmuka pengguna Airflow. Pengguna dapat menentukan detail koneksi seperti nama layanan, host, nama pengguna, kata sandi, dan skema atau database yang digunakan. Setelah koneksi dikonfigurasi, Airflow dapat menggunakannya untuk melakukan tugas-tugas seperti mengambil atau menyimpan data dari atau ke database Postgres.

```python
from airflow.models import Connection

# Definisikan detail koneksi ke database Postgres
postgres_connection = Connection(
    conn_id='postgres_default',  # ID koneksi
    conn_type='postgres',         # Tipe koneksi
    host='postgres',              # Host dari layanan Postgres (nama layanan dalam Docker Compose)
    login='postgres_user',        # Nama pengguna
    password='password',          # Kata sandi
    schema='my_database'          # Nama skema/database
)

# Simpan koneksi
postgres_connection.add()
```

**Penjelasan:**
- Langkah-langkah ini digunakan untuk membuat koneksi ke database Postgres dalam Apache Airflow.
- Kode program ini mendefinisikan detail koneksi seperti `conn_id`, `conn_type`, `host`, `login`, `password`, dan `schema`.
- Setelah mendefinisikan detail koneksi, koneksi tersebut disimpan menggunakan metode `add()`.

### Konfigurasi Pengiriman Email dalam Apache Airflow

**Definisi/Pengertian:**
Konfigurasi pengiriman email dalam Apache Airflow adalah proses menyiapkan sistem Airflow untuk mengirim email saat DAG berhasil atau gagal dieksekusi. Ini memungkinkan pengguna untuk menerima notifikasi melalui email tentang status eksekusi DAG.

**Penjelasan:**
Apache Airflow memungkinkan pengguna untuk mengonfigurasi pengiriman email dengan menyediakan detail SMTP seperti host, port, nama pengguna, dan kata sandi. Ini memungkinkan Airflow untuk mengirim email melalui server SMTP yang ditentukan pengguna. Pengguna dapat menggunakan server SMTP internal atau eksternal, tergantung pada kebutuhan. Konfigurasi email biasanya disimpan sebagai variabel Airflow, yang dapat diakses dari dalam DAG atau task untuk mengirim notifikasi ke pengguna melalui email tentang status eksekusi alur kerja.

```python
from airflow.models import Variable

# Konfigurasi SMTP
smtp_config = {
    'smtp_host': 'smtp.example.com',
    'smtp_user': 'user@example.com',
    'smtp_password': 'your_password',
    'smtp_port': 587,  # Port SMTP
    'smtp_starttls': True,
}

# Simpan konfigurasi SMTP sebagai variabel Airflow
Variable.set("smtp_config", smtp_config)
```

**Penjelasan:**
- Langkah-langkah ini digunakan untuk mengkonfigurasi pengiriman email dalam Apache Airflow.
- Kode program ini mendefinisikan detail konfigurasi SMTP seperti `smtp_host`, `smtp_user`, `smtp_password`, `smtp_port`, dan `smtp_starttls`.
- Setelah mendefinisikan konfigurasi SMTP, konfigurasi tersebut disimpan sebagai variabel Airflow menggunakan metode `set()`. Variabel Airflow ini kemudian dapat digunakan dalam pengaturan DAG atau task yang memerlukan pengiriman email.