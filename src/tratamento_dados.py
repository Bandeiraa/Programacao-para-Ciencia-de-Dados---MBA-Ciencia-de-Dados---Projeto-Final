import pandas as pd
import numpy as np

# Lê e prepara os dados da ANEEL para análise.
# Remove nulos, converte tipos e cria colunas derivadas.
def preparar_dados(caminho_csv: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_csv)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df["Consumo_kWh"] = df["Consumo_kWh"].astype(float)
    df["PIB_per_capita"] = df["PIB_per_capita"].astype(float)
    df["Consumo_per_capita"] = df["Consumo_kWh"] / df["População"]
    
    return df
