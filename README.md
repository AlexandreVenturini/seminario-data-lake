# Seminário — Data Lake e Lakehouse

Projeto desenvolvido para a disciplina de Banco de Dados III.

## Objetivo

Simular uma arquitetura moderna de Data Lake utilizando:

* Arquivos CSV e JSON
* Processo ETL
* Armazenamento em Parquet
* Consultas analíticas com DuckDB

O projeto demonstra conceitos relacionados a:

* Data Lakes
* Lakehouse
* ETL (Extract, Transform, Load)
* OLAP
* Engenharia de Dados
* Armazenamento analítico

---

# Tecnologias utilizadas

* Python
* Pandas
* DuckDB
* PyArrow
* Parquet

---

# Estrutura do projeto

```txt
seminario-data-lake/
│
├── data_lake/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── etl.py
│   └── consulta.py
│
├── venv/
│
└── README.md
```

---

# Fluxo do projeto

## 1. Ingestão de dados

Os dados são simulados através de arquivos:

* CSV
* JSON

Armazenados na camada `raw`.

---

## 2. ETL

O script `etl.py` realiza:

* Extração dos dados
* Transformação e limpeza
* Padronização
* Conversão para Parquet

Os dados tratados são salvos em:

```txt
/data_lake/processed/
```

---

## 3. Consulta analítica

O script `consulta.py` utiliza DuckDB para executar consultas SQL diretamente sobre arquivos Parquet.

Exemplo:

```sql
SELECT categoria, SUM(valor)
FROM vendas
GROUP BY categoria;
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
pip install pandas duckdb pyarrow
```

---

## Executar ETL

```bash
cd scripts
python etl.py
```

---

## Executar consultas analíticas

```bash
python consulta.py
```

---

# Conceitos abordados

* Cloud Storage (simulado localmente)
* Data Lake
* Lakehouse
* ETL
* OLAP
* Big Data
* Arquitetura moderna de dados

---

# Integrantes

* Alexandre Luiz Demuner Venturini
* Julia de Souza Sacht
* Jéssica Jamilli Pandolfi Magdalão
* Paulo André Soares da Silva