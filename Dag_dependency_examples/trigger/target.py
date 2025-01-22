from airflow.decorators import dag,task
from datetime import datetime 

@dag(start_date=datetime(2025,1,1),schedule='@None' ,catchup = False)
def target():

    @task
    def message(dag_run = None):
        print(dag_run.conf.get("message"))

    message()

target()