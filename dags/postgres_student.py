from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'copy_table_postgresql',
    default_args=default_args,
    description='A DAG to copy a table from one PostgreSQL instance to another',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['example'],
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

# Extract data from source PostgreSQL
extract_task = PostgresOperator(
    task_id='extract_data',
    postgres_conn_id='source',
    sql='COPY source_table TO STDOUT WITH CSV HEADER',
    filename='/tmp/source_table.csv',
    dag=dag,
)

# Load data into destination PostgreSQL
load_task = PostgresOperator(
    task_id='load_data',
    postgres_conn_id='destination',
    sql='COPY destination_table FROM STDIN WITH CSV HEADER',
    filename='/tmp/source_table.csv',
    dag=dag,
)

start >> extract_task >> load_task
