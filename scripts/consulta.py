import duckdb

con = duckdb.connect()

resultado = con.execute("""
    SELECT
        categoria,
        SUM(valor) AS total_vendas,
        COUNT(*) AS quantidade_vendas
    FROM '../data_lake/processed/vendas_tratadas.parquet'
    GROUP BY categoria
    ORDER BY total_vendas DESC
""").fetchdf()

print("\nRELATÓRIO ANALÍTICO")
print(resultado)