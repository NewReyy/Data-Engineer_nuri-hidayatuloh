from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests
import firebase_admin
from firebase_admin import credentials, storage
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

cred = credentials.Certificate("/home/newrey/airflow/dags/accountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'de-in-cloud-nuri-hidayatuloh.appspot.com'
})

default_args = {
    'owner': 'nuri',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG('fake_store_data_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    def extract_data():
        response = requests.get('https://fakestoreapi.com/products')
        data = response.json()
        return data

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    def transform_data(**kwargs):
        data = kwargs['ti'].xcom_pull(task_ids='extract_data')
        transformed_data = []
        for product in data:
            if product['price'] > 100:
                transformed_product = {
                    'title': product['title'],
                    'price': product['price'],
                    'description': product['description'],
                    'category': product['category']
                }
                transformed_data.append(transformed_product)
        return transformed_data

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    def save_as_parquet(**kwargs):
        transformed_data = kwargs['ti'].xcom_pull(task_ids='transform_data')
        df = pd.DataFrame(transformed_data)
        pq.write_table(pa.Table.from_pandas(df), 'transformed_data.parquet')

    save_as_parquet_task = PythonOperator(
        task_id='save_as_parquet',
        python_callable=save_as_parquet
    )

    def upload_to_firebase(**kwargs):
        bucket_name = 'de-in-cloud-nuri-hidayatuloh.appspot.com'
        blob = storage.bucket(bucket_name).blob('transformed_data.parquet')
        blob.upload_from_filename('transformed_data.parquet')

    upload_task = PythonOperator(
        task_id='upload_to_firebase',
        python_callable=upload_to_firebase
    )

    extract_task >> transform_task >> save_as_parquet_task >> upload_task