import pandas as pd

df = pd.read_parquet(
    "../data_lake/processed/vendas_tratadas.parquet"
)

print(df)