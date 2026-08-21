#  Apache Airflow com Astro CLI

Este repositório contém o projeto desenvolvido para o curso de Engenharia, focado na orquestração de pipelines de dados utilizando o Apache Airflow e a ferramenta Astro CLI.

## 🚀 Tecnologias Utilizadas
* **Apache Airflow:** Orquestração dos fluxos de trabalho.
* **Astro CLI:** Gerenciamento do ambiente Airflow local via Docker.
* **Python:** Desenvolvimento das DAGs e lógica de dados.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/vitaless7/airflow.git
   cd airflow
   ```

2. **Iniciar o Airflow localmente:**
https://www.astronomer.io/docs/cli/v1.44/get-started-cli#windows-with-winget
   ```bash
   astro dev start
   ```

3. **Acessar a Interface Web:**
   Após a inicialização, abra o navegador e acesse:
   * **URL:** `http://localhost:8080`
   * **Usuário:** `admin`
   * **Senha:** `admin`

## 📁 Estrutura de Pastas Principal
* `dags/`: Local onde ficam guardados os scripts Python dos fluxos de dados (DAGs).
* `execution_logs.log`: Arquivo de registro das execuções do pipeline.# ETL_Pandas_JSON_Parquet
