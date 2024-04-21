from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd

def fetch_data():
    # Mengambil data dari API endpoint
    response = requests.get("https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json")
    data = response.json()
    return data

def clean_data(**kwargs):
    # Mendapatkan data dari output task sebelumnya
    data = kwargs['ti'].xcom_pull(task_ids='fetch_data_task')
    
    # Mengubah format nomor telepon dan nilai transaksi
    for transaction in data:
        transaction['phone_number'] = '+62' + transaction['phone_number']
        transaction['transaction_amount'] = 'Rp ' + '{:,.0f}'.format(transaction['transaction_amount']).replace(",", ".")
    
    # Filter data untuk hanya menyertakan transaksi dengan status 'success'
    success_transactions = [transaction for transaction in data if transaction['transaction_status'] == 'success']
    
    # Menyimpan data ke dalam file CSV lokal
    df = pd.DataFrame(success_transactions)
    df.to_csv('transactions.csv', index=False)

default_args = {
    'owner': 'nuri',
    'start_date': datetime(2024, 4, 20),
    'schedule_interval': '@daily'
}

with DAG('data_cleaning_workflow', default_args=default_args, catchup=False) as dag:
    
    fetch_data_task = PythonOperator(
        task_id='fetch_data_task',
        python_callable=fetch_data
    )
    
    clean_data_task = PythonOperator(
        task_id='clean_data_task',
        python_callable=clean_data,
        provide_context=True
    )
    
    fetch_data_task >> clean_data_task