from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests
import pandas as pd
import os
import logging

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,  # Retry tugas hingga 3 kali jika gagal
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'fakestore_dag',
    default_args=default_args,
    description='DAG untuk fetch data dari API kedalam bentuk CSV & txt',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=['example'],
)

OUTPUT_DIR = os.path.join('16_Workflow-Orchestration-with-Apache-Airflow', 'Praktikum', 'Prioritas-2')

def get_api_data(**kwargs):
    try:
        response = requests.get("https://fakestoreapi.com/products")
        response.raise_for_status()  # Angkat eksepsi jika respons tidak sukses (status code >= 400)
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch data from API: {e}")
        raise

def write_to_csv(**kwargs):
    ti = kwargs['ti']
    response_data = ti.xcom_pull(task_ids='get_api_data')
    csv_file_path = os.path.join(OUTPUT_DIR, "data.csv")
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        df = pd.json_normalize(response_data)  # Flatten JSON
        df.to_csv(csv_file_path, index=False)
        logging.info(f"Data written to CSV file: {csv_file_path}")
    except Exception as e:
        logging.error(f"Failed to write to CSV file: {e}")
        raise

def write_to_txt(**kwargs):
    ti = kwargs['ti']
    response_data = ti.xcom_pull(task_ids='get_api_data')
    txt_file_path = os.path.join(OUTPUT_DIR, "data.txt")
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(txt_file_path, "w") as txt_file:
            for item in response_data:
                txt_file.write(f"{item['title']}\n")  
        logging.info(f"Data written to TXT file: {txt_file_path}")
    except Exception as e:
        logging.error(f"Failed to write to TXT file: {e}")
        raise

def print_done():
    print("done!")

get_api_data_task = PythonOperator(
    task_id='get_api_data',
    python_callable=get_api_data,
    dag=dag,
)

write_to_csv_task = PythonOperator(
    task_id='write_to_csv',
    python_callable=write_to_csv,
    provide_context=True,
    dag=dag,
)

write_to_txt_task = PythonOperator(
    task_id='write_to_txt',
    python_callable=write_to_txt,
    provide_context=True,
    dag=dag,
)

print_done_task = PythonOperator(
    task_id='print_done',
    python_callable=print_done,
    dag=dag,
)

get_api_data_task >> write_to_csv_task
get_api_data_task >> write_to_txt_task
write_to_csv_task >> print_done_task
write_to_txt_task >> print_done_task