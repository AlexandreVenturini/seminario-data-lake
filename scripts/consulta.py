import duckdb

con = duckdb.connect()

resultado = con.execute("""

SELECT *
FROM read_csv_auto('../data_lake/raw/vendas_janeiro.csv')

UNION ALL

SELECT *
FROM read_json_auto('../data_lake/raw/vendas_fevereiro.json')

""").fetchdf()

print(resultado)