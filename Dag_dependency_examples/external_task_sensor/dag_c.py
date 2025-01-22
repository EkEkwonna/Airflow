from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date = datetime(2025,1,1),schedule = '@daily',catchup= False)
def dag_c():

    @task
    def task_c():
        print("task_c")

    task_c()

dag_c()