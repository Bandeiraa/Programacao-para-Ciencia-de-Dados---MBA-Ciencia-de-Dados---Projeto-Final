import csv

# Lê um arquivo CSV e retorna uma lista de dicionários com os dados.
def ler_dados_csv(caminho_arquivo: str) -> list:
    dados = []
    
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados.append(linha)

        return dados
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return []
