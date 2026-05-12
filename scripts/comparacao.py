import pandas as pd
import time
import os

inicio_csv = time.time()

csv_df = pd.read_csv("../data_lake/raw/vendas_janeiro.csv")

fim_csv = time.time()

tempo_csv = fim_csv - inicio_csv

inicio_parquet = time.time()

parquet_df = pd.read_parquet(
    "../data_lake/processed/vendas_tratadas.parquet"
)

fim_parquet = time.time()

tempo_parquet = fim_parquet - inicio_parquet

tamanho_csv = os.path.getsize(
    "../data_lake/raw/vendas_janeiro.csv"
)

tamanho_parquet = os.path.getsize(
    "../data_lake/processed/vendas_tratadas.parquet"
)

print("\nCOMPARAÇÃO DE FORMATOS\n")

print(f"Tamanho CSV: {tamanho_csv} bytes")
print(f"Tamanho Parquet: {tamanho_parquet} bytes")

print()

print(f"Tempo leitura CSV: {tempo_csv:.6f} segundos")
print(f"Tempo leitura Parquet: {tempo_parquet:.6f} segundos")