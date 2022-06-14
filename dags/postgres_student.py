from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
dag_params = {
    'dag_id': 'postgres_student_migration'
}
with DAG(**dag_params) as dag:
    src = PostgresHook(postgres_conn_id='source')
    dest = PostgresHook(postgres_conn_id='destination')
    src_conn = src.get_conn()
    cursor = src_conn.cursor()
    dest_conn = dest.get_conn()
    dest_cursor = dest_conn.cursor()
    dest_cursor.execute("SELECT CAST(MAX(S_ID) AS INTEGER) FROM STUDENT;")
    student_id = dest_cursor.fetchone()[0]
    if student_id is None:
        student_id = 0
    cursor.execute("SELECT s_id, s_name, s_birth, s_sex, CURRENT_TIMESTAMP as s_insert_dt  FROM STUDENT WHERE CAST(S_ID AS INT) > %s", [student_id])
    dest.insert_rows(table="STUDENT", rows=cursor)