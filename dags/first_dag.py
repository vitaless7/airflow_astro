"""
## Minha primeira DAG

Pipeline de estudo com três atividades fictícias, usado para praticar
dependências entre tasks.

A primeira atividade é upstream das outras duas, que rodam em paralelo:

    primeira ──┬── segunda
               └── terceira
"""

from time import sleep

from airflow.sdk import dag, task
from pendulum import datetime, duration

default_args = {
    "owner": "felipe.vital",
    "retries": 2,
    "retry_delay": duration(minutes=1),
}


@dag(
    dag_id="minha_primeira_dag",
    description="ETL de estudo: uma task upstream e duas downstream em paralelo.",
    schedule="@hourly",
    start_date=datetime(2025, 3, 24),
    catchup=False,
    max_active_runs=1,
    default_args=default_args,
    tags=["estudo", "etl"],
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

    t1 >> [t2, t3]


minha_dag = meu_pipeline()
