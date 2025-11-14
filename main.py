from src.leitura_dados import ler_dados_csv
from src.tratamento_dados import preparar_dados
from src.analise_estatistica import gerar_estatisticas
from src.visualizacoes import gerar_graficos
from src.relatorios import salvar_relatorio

def main():
    print("Análise de Consumo Energético")
    caminho = "dados/consumo_energia_brasil.csv"
    df = preparar_dados(caminho)
    gerar_graficos(df)
    resultados = gerar_estatisticas(df)
    salvar_relatorio(resultados)

if __name__ == "__main__":
    main()
