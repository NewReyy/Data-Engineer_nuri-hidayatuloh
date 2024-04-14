from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import csv

# Mendefinisikan argumen default untuk DAG
default_args = {
    'owner': 'nuri',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Mendefinisikan DAG
dag = DAG(
    'books_data_extraction_dag',  # Nama DAG
    default_args=default_args,
    description='DAG untuk mengekstraksi data dari API dan menyimpannya dalam CSV',  # Deskripsi DAG
    schedule_interval='0 9 * * 1',  # Jadwal eksekusi DAG menggunakan cron expression (setiap hari Senin jam 09:00)
)

# Fungsi untuk mengekstraksi data dari API dan menyimpannya dalam CSV
def extract_data():
    url = "https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json"
    response = requests.get(url)
    
    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        data = response.json()
        # Memeriksa apakah kunci 'data' ada dalam respons JSON
        if "data" in data:
            books = data["data"]
            with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["Judul", "Pengarang", "Tahun Terbit", "Genre"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                # Menulis baris untuk setiap buku
                for book in books:
                    writer.writerow({
                        "Judul": book["title"],
                        "Pengarang": book["author"],
                        "Tahun Terbit": book["year"],
                        "Genre": book["genre"]
                    })
            print("Data berhasil diekstraksi dan disimpan dalam file 'books.csv'")
        else:
            print("Kunci 'data' tidak ditemukan dalam respons JSON.")
    else:
        print("Gagal mengambil data. Status code:", response.status_code)

# Mendefinisikan task untuk mengekstraksi data
extract_data_task = PythonOperator(
    task_id='extract_data_task',  # ID task
    python_callable=extract_data,  # Fungsi yang akan dijalankan oleh task
    dag=dag,  # DAG yang terkait dengan task
)

# Menambahkan task ke dalam DAG
extract_data_task