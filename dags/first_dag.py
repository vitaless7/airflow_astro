from time import sleep
from datetime import datetime
from airflow.decorators import dag, task

@dag(
    dag_id="minha_primeira_dag",
    description="etl",
    schedule="* * * * *",     
    start_date=datetime(2025, 3, 24),
    catchup=False
)
def meu_pipeline():

    @task
    def primeira_atividade():
        print("Minha primeira atividade!")
        sleep(2)

    @task
    def segunda_atividade():
        print("Minha segunda atividade!")
        sleep(2)

    @task
    def terceira_atividade():
        print("Minha terceira atividade!")
        sleep(2)


    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

    t1 >> [t2,t3]

minha_dag = meu_pipeline()