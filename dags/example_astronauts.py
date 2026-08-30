"""
## DAG de exemplo: astronautas no espaço

Consulta a API Open Notify e imprime o nome de cada astronauta atualmente
no espaço e a nave em que está.

São duas tasks: uma busca os dados na API, a outra imprime o resultado.
A segunda usa *dynamic task mapping* — cria uma cópia da task por
astronauta retornado, ajustando a quantidade a cada execução.

Tutorial: https://docs.astronomer.io/learn/get-started-with-airflow

![Foto da ISS](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2010/02/space_station_over_earth/10293696-3-eng-GB/Space_Station_over_Earth_card_full.jpg)
"""

from airflow.sdk import Asset, dag, task
from pendulum import datetime, duration
import requests


@dag(
    start_date=datetime(2025, 4, 1),  # a partir de quando pode ser agendada
    schedule="@daily",
    max_consecutive_failed_dag_runs=5,  # pausa após 5 falhas seguidas (experimental)
    doc_md=__doc__,  # exibe esta docstring na UI
    default_args={
        "owner": "Astro",
        "retries": 3,
        "retry_delay": duration(seconds=5),
    },
    tags=["exemplo", "espaco"],
    is_paused_upon_creation=False,  # já nasce ativa
)
def example_astronauts():

    # outlets: marca que esta task atualiza um Asset, permitindo que outras
    # DAGs sejam agendadas por essa atualização.
    @task(outlets=[Asset("current_astronauts")])
    def get_astronauts(**context) -> list[dict]:
        """Busca os astronautas no espaço e devolve a lista.

        A contagem vai para o XCom; a lista é o retorno usado pela próxima task.
        """
        try:
            r = requests.get("http://api.open-notify.org/astros.json")
            r.raise_for_status()
            number_of_people_in_space = r.json()["number"]
            list_of_people_in_space = r.json()["people"]
        except:
            print("API indisponível, usando dados fixos.")
            number_of_people_in_space = 12
            list_of_people_in_space = [
                {"craft": "ISS", "name": "Marco Alain Sieber"},
                {"craft": "ISS", "name": "Claude Nicollier"},
            ]

        context["ti"].xcom_push(
            key="number_of_people_in_space", value=number_of_people_in_space
        )
        return list_of_people_in_space

    @task
    def print_astronaut_craft(greeting: str, person_in_space: dict) -> None:
        """Imprime o nome do astronauta, a nave e uma saudação fixa."""
        craft = person_in_space["craft"]
        name = person_in_space["name"]

        print(f"{name} is in space flying on the {craft}! {greeting}")

    # expand() cria em runtime uma cópia da task por item da lista, em paralelo.
    # Ver: https://www.astronomer.io/docs/learn/dynamic-tasks
    print_astronaut_craft.partial(greeting="Hello! :)").expand(
        person_in_space=get_astronauts()
    )


example_astronauts()
