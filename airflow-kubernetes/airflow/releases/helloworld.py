from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

dag = DAG("helloworld", schedule_interval=None, start_date=days_ago(2))

parameterized_task = BashOperator(
    task_id='parameterized_task',
    bash_command="echo value Hello Wolrd",
    dag=dag,
)

parameterized_task
