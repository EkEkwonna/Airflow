
from airflow.decorators import dag, task 
from airflow import Dataset 
from datetime import datetime 

data_a = Dataset("s3://bucket_a/data_a")
data_b = Dataset("s3://bucket_b/data_b")

#define the DAG object
@dag(start_date = datetime(2025,1,1),schedule = '@daily',catchup = False)
def producer():

    #outlets decide where the destination 
    @task(outlets = [data_a])
    def update_a():
        print("Data A has been updated")

    @task(outlets=[data_b])
    def update_b():
        print("Data B has been updated")

    #Defines the dependency 
    update_a() >> update_b()

producer()