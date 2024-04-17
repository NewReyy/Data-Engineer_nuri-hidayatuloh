from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from matplotlib import pyplot as plt
import os
import zipfile

default_args = {
    'owner': 'nuri',
    'start_date': datetime(2024, 4, 16),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_analysis_workflow_dag',
    default_args=default_args,
    description='Sebuah DAG untuk Automasi Workflow, meliputi Ekstraksi Data & Transformasi Data, Lalu mengekspor hasil dari analisis data nya',
    schedule_interval='@daily',
    catchup=False,
)

def extract_data():
    os.system('kaggle datasets download -d ayushparwal2026/shopping-dataset -p D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform')
    with zipfile.ZipFile('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/shopping-dataset.zip', 'r') as zip_ref:
        zip_ref.extractall('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform')

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

def transform_data():
    df = pd.read_csv('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/Shopping_data.csv')
    
    # Handling missing values
    df['Genre'].fillna('Unknown', inplace=True)
    
    # Encoding kolom Genre
    df = pd.get_dummies(df, columns=['Genre'], drop_first=True)
    
    # Normalisasi kolom Annual Income (k$)
    df['Annual Income (k$)'] = (df['Annual Income (k$)'] - df['Annual Income (k$)'].min()) / (df['Annual Income (k$)'].max() - df['Annual Income (k$)'].min())
    
    # Menyimpan DataFrame yang sudah diubah
    df.to_csv('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/transformed_shopping_data.csv', index=False)

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

def export_to_excel():
    df = pd.read_csv('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/transformed_shopping_data.csv')
    df.to_excel('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/shopping_analysis_result.xlsx', index=False)

export_to_excel_task = PythonOperator(
    task_id='export_to_excel',
    python_callable=export_to_excel,
    dag=dag,
)

def visualize_data():
    df = pd.read_csv('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/transformed_shopping_data.csv')
    
    # Visualisasi data
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Genre_Male'], cmap='viridis', alpha=0.7)
    plt.title('Annual Income vs. Spending Score')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.colorbar(label='Gender (Male)')
    plt.savefig('D:/Nuri/MSIB-ALTERRA/Data-Engineer_nuri-hidayatuloh/15_Data-Transformation/Praktikum/Eksplorasi_Transform/visualization.png')

visualize_data_task = PythonOperator(
    task_id='visualize_data',
    python_callable=visualize_data,
    dag=dag,
)

extract_data_task >> transform_data_task >> export_to_excel_task >> visualize_data_task