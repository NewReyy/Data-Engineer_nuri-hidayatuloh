from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_1', default_args=default_args, schedule_interval=None)

t1 = BashOperator(
    task_id='print_hello_airflow',
    bash_command='echo "hello airflow"',
    dag=dag)

t2a = BashOperator(
    task_id='create_about_us_directory',
    bash_command='mkdir -p about_us',
    dag=dag)

t2b = BashOperator(
    task_id='create_our_works_directory',
    bash_command='mkdir -p our_works',
    dag=dag)

t3a = BashOperator(
    task_id='create_about_us_about_txt_file',
    bash_command='mkdir -p about_us && touch about_us/about.txt',
    dag=dag)

t3b = BashOperator(
    task_id='create_our_works_works_txt_file',
    bash_command='mkdir -p our_works && touch our_works/works.txt',
    dag=dag)

t4 = BashOperator(
    task_id='print_done',
    bash_command='echo "done!"',
    dag=dag)

t1 >> t2a
t1 >> t2b
t2a >> t3a
t2b >> t3b
t3a >> t4
t3b >> t4