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

2. **Instalar o Astro CLI** (Windows, via winget) —
   [documentação oficial](https://www.astronomer.io/docs/cli/v1.44/get-started-cli#windows-with-winget):
   ```bash
   winget install -e --id Astronomer.Astro
   ```

3. **Iniciar o Airflow localmente** (requer Docker Desktop rodando):
   ```bash
   astro dev start
   ```

4. **Acessar a Interface Web:**
   Após a inicialização, abra o navegador e acesse:
   * **URL:** `http://localhost:8080`
   * **Usuário:** `admin`
   * **Senha:** `admin`

## 📁 Estrutura de Pastas Principal
* `dags/`: scripts Python dos fluxos de dados (DAGs).
  * `first_dag.py`: pipeline de estudo, uma task upstream e duas em paralelo.
  * `example_astronauts.py`: exemplo do Astro consumindo a API Open Notify.
* `include/`: arquivos auxiliares usados pelas DAGs (SQL, configs, dados).
* `tests/dags/`: teste de integridade — garante que toda DAG importa sem erro.
* `requirements.txt`: dependências Python instaladas na imagem.
* `packages.txt`: pacotes de sistema (apt) instalados na imagem.

## 🧪 Rodar os testes

```bash
astro dev pytest
```

## 📝 Notas

* As DAGs rodam dentro do container, não no Python local — por isso a IDE pode
  acusar `airflow.sdk` como não resolvido. É esperado.
* Toda dependência nova precisa entrar no `requirements.txt` e exige
  `astro dev restart`.
