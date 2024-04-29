from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import pandas as pd
from data_ingestion import DataLakeBuilder
from data_transformation import DataWarehouseLoader

default_args = {
    'owner': 'nuri',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('DAG_Code-Competance-2', 
          description='Ingestion dan Menyiapkan Data kedalam Data Lake/Data Warehouse sampai dengan Data Transform dan Load to Warehouse Storage',
          default_args=default_args,
          schedule_interval=timedelta(1),
          start_date=datetime(2024, 4, 29), catchup=False)

def execute_data_ingestion():
    data_lake_builder = DataLakeBuilder()
    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']
    parquet_files = ['events.parquet', 'customers.parquet', 'tickets.parquet', 'transactions.parquet', 'customer_feedback.parquet']

    for i in range(len(csv_files)):
        df = data_lake_builder.read_csv_data(csv_files[i])
        data_lake_builder.handle_missing_values(df)
        data_lake_builder.handle_duplicates(df)
        if i == 3:
            data_lake_builder.handle_outliers(df, 'total_amount')
        data_lake_builder.save_to_parquet(df, parquet_files[i])
        data_lake_builder.validate_data(parquet_files[i])
        
def execute_data_transform_and_load_to_storage():
    # Data transformation
    loader = DataWarehouseLoader()
    events_df = loader.load_data('events.parquet')
    customers_df = loader.load_data('customers.parquet')
    tickets_df = loader.load_data('tickets.parquet')
    transactions_df = loader.load_data('transactions.parquet')
    customer_feedback_df = loader.load_data('customer_feedback.parquet')

    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)
    
    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')

execute_data_ingestion_task = PythonOperator(
    task_id='execute_data_ingestion',
    python_callable=execute_data_ingestion,
    dag=dag)

execute_data_transform_and_load_to_storage_task = PythonOperator(
    task_id='execute_data_transform_and_load_to_storage',
    python_callable=execute_data_transform_and_load_to_storage,
    dag=dag)

execute_data_ingestion_task >> execute_data_transform_and_load_to_storage_task