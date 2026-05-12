import pandas as pd

csv_df = pd.read_csv("../data_lake/raw/vendas_janeiro.csv")

json_df = pd.read_json("../data_lake/raw/vendas_fevereiro.json")

print("CSV carregado:")
print(csv_df)

print("\nJSON carregado:")
print(json_df)

df = pd.concat([csv_df, json_df], ignore_index=True)

df = df.dropna()

df["categoria"] = df["categoria"].str.upper()

print("\nDados tratados:")
print(df)

df.to_parquet(
    "../data_lake/processed/vendas_tratadas.parquet",
    index=False
)

print("\nArquivo Parquet salvo com sucesso!")