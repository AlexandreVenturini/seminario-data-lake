# Seminário — Data Lake e Lakehouse

Projeto desenvolvido para a disciplina de Banco de Dados III.

## Objetivo

Simular um ambiente de Data Lake utilizando arquivos CSV e JSON, realizando consultas SQL diretamente sobre os dados através do DuckDB.

O projeto demonstra conceitos relacionados a:

* Cloud Storage (simulado localmente)
* Data Lake
* Lakehouse
* Armazenamento moderno de dados
* Consultas analíticas com SQL
* Engenharia de Dados

---

# Tecnologias utilizadas

* Python
* DuckDB
* CSV
* JSON

---

# Estrutura do projeto

```txt
seminario-data-lake/
│
├── data_lake/
│   └── raw/
│       ├── vendas_janeiro.csv
│       └── vendas_fevereiro.json
│
├── scripts/
│   └── consulta.py
│
├── venv/
│
└── README.md
```

---

# Funcionamento do projeto

## 1. Ingestão de dados

Os dados são armazenados em diferentes formatos:

* CSV
* JSON

Simulando um Data Lake moderno capaz de armazenar múltiplos tipos de dados.

---

## 2. Consulta analítica

O script `consulta.py` utiliza DuckDB para realizar consultas SQL diretamente sobre os arquivos do Data Lake.

Exemplo:

```sql
SELECT *
FROM read_csv_auto('vendas_janeiro.csv')
UNION ALL
SELECT *
FROM read_json_auto('vendas_fevereiro.json')
```

---

# Como executar

## Criar ambiente virtual

```bash
python -m venv venv
```

## Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install duckdb
```

---

## Executar consulta

```bash
cd scripts
python consulta.py
```

---

# Conceitos abordados

* Cloud Storage
* Data Lake
* Lakehouse
* SQL Analytics
* Big Data
* Arquitetura moderna de dados

---

# Integrantes

* Alexandre Luiz Demuner Venturini
* Julia de Souza Sacht
* Jéssica Jamilli Pandolfi Magdalão
* Paulo André Soares da Silva