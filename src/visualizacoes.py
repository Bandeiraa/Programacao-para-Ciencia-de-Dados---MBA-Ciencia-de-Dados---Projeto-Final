import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Gera e salva visualizações em /relatorios/
def gerar_graficos(df: pd.DataFrame):

    # Consumo por região
    plt.figure(figsize=(8,5))
    df.groupby("Região")["Consumo_kWh"].mean().plot(kind="bar", color="teal")
    plt.title("Consumo Médio por Região")
    plt.xlabel("Região")
    plt.ylabel("Consumo (kWh)")
    plt.tight_layout()
    plt.savefig("relatorios/consumo_regional.png")
    plt.close()

    # Heatmap de correlação
    plt.figure(figsize=(6,4))
    sns.heatmap(df[["Consumo_kWh", "PIB_per_capita", "Consumo_per_capita"]].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlação entre Indicadores Energéticos e Econômicos")
    plt.tight_layout()
    plt.savefig("relatorios/correlacao_consumo_pib.png")
    plt.close()
