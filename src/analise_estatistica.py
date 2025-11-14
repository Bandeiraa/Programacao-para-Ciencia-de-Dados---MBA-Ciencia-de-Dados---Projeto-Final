import pandas as pd

# Calcula métricas estatísticas e agrupamentos por região.
def gerar_estatisticas(df: pd.DataFrame) -> dict:

    resultados = {
        "consumo_medio": df["Consumo_kWh"].mean(),
        "consumo_total": df["Consumo_kWh"].sum(),
        "desvio_padrao": df["Consumo_kWh"].std(),
        "correlacao_consumo_pib": df["Consumo_kWh"].corr(df["PIB_per_capita"]),
    }

    consumo_por_regiao = df.groupby("Região")["Consumo_kWh"].sum().to_dict()
    resultados["consumo_por_regiao"] = consumo_por_regiao

    return resultados