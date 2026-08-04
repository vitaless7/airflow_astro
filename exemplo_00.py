from time import sleep
from loguru import logger

logger.add(
    "execution_logs.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO"
)


def primeira_atividade():
    logger.info("Iniciando primeira atividade")
    print("Minha primeira atividade!")
    sleep(2)
    logger.success("Primeira atividade finalizada")


def segunda_atividade():
    logger.info("Iniciando segunda atividade")
    print("Minha segunda atividade!")
    sleep(2)
    logger.success("Segunda atividade finalizada")


def terceira_atividade():
    logger.info("Iniciando terceira atividade")
    print("Minha terceira atividade!")
    sleep(2)
    logger.success("Terceira atividade finalizada")


def pipeline():
    logger.info("Pipeline iniciada")

    primeira_atividade()
    segunda_atividade()
    terceira_atividade()

    logger.success("Pipeline finalizada com sucesso!")


if __name__ == "__main__":
    pipeline()