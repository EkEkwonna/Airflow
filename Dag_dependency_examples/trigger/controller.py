
from airflow.decorators import dag,task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime 

@dag(start_date=datetime(2025,1,1),schedule = '@None',catchup= False)
def controller():

    @task
    def start():
        print("start")

    trigger = TriggerDagRunOperator(
        task_id='trigger_target_dag',         
        trigger_dag_id = 'target',              # The DAG ID of the DAG you want to trigger
        conf = {"message":"my_data"},           # configuration parameter with data you want to pass to trigger DAG
        wait_for_completion = True              # will wait till the end of completion of this task before the trigger is set 
    )

    @task
    def done():
        print("done")
