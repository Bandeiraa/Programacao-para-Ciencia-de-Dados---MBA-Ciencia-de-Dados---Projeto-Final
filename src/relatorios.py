# Salva os resultados principais em um arquivo de texto.
def salvar_relatorio(resultados: dict, caminho_saida: str = "relatorios/resultados_analise.txt"):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write("=== Relatório de Análise Energética ===\n\n")
        for chave, valor in resultados.items():
            f.write(f"{chave}: {valor}\n")
            
    print(f"Relatório gerado em: {caminho_saida}")
